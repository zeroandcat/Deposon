# -*- coding: utf-8 -*-
# llm_fetch（候选 3 统一 fetch 管道）边界测试：假 transport 注入，零网络。
# 覆盖：重试预算/超时透传/sanitize（含 gt3b/gt3c 截断加固）/缓存命中跳过/
# 落盘格式/预算计数语义。全部 synthetic，不写 results/，不假充真实调用。
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import llm_fetch
from llm_fetch import (EndpointSpec, FetchOutcome, fetch_text, is_fresh,
                       parse_json_array, post_once, sanitize_secret,
                       save_record, sha)

KEY = "UNIT-TEST-SENTINEL-NOT-A-REAL-KEY"
SPEC = EndpointSpec(endpoint="https://example.invalid/v1/chat", model="m0",
                    timeout=12.5, max_tokens=123, max_attempts=2)


class Resp:
    def __init__(self, content="ok", status=200, text="fine"):
        self.status_code = status
        self.text = text
        self._c = content

    def json(self):
        return {"choices": [{"message": {"content": self._c}}]}


def recorder(script):
    """script: list of Resp 或 Exception 实例；返回 (transport, calls)。"""
    calls = []

    def transport(endpoint, headers=None, json=None, timeout=None):
        calls.append({"endpoint": endpoint, "headers": headers,
                      "json": json, "timeout": timeout})
        item = script[len(calls) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    return transport, calls


# ---------------------------------------------------------------- 基础件
def test_sha_single_source():
    assert sha("abc") == (__import__("hashlib")
                          .sha256("abc".encode("utf-8")).hexdigest())
    import llm_prior
    assert not hasattr(llm_prior, "sha") or llm_prior.sha is sha


def test_sanitize_secret_and_alias():
    assert sanitize_secret(f"token {KEY} leaked", KEY) == "token *** leaked"
    assert sanitize_secret("plain", "") == "plain"
    import llm_prior
    assert llm_prior._sanitize is sanitize_secret


def test_parse_json_array_and_alias():
    assert parse_json_array('```json\n[{"a": 1}]\n``` 尾部噪声') == [{"a": 1}]
    assert parse_json_array('[1, 2]') == [1, 2]
    with pytest.raises(ValueError):
        parse_json_array("没有数组")
    import llm_prior
    assert llm_prior._extract_json_array is parse_json_array


# ---------------------------------------------------------------- post_once
def test_post_once_transport_contract():
    transport, calls = recorder([Resp("hello")])
    c = post_once(SPEC, "PROMPT", KEY, transport=transport)
    assert c == "hello"
    assert calls[0]["endpoint"] == SPEC.endpoint
    assert calls[0]["timeout"] == 12.5                    # 超时口径透传
    assert calls[0]["json"] == {"model": "m0", "max_tokens": 123,
                                "messages": [{"role": "user",
                                              "content": "PROMPT"}]}
    assert calls[0]["headers"]["Authorization"] == f"Bearer {KEY}"


def test_post_once_http_error_sanitized():
    transport, _ = recorder([Resp(status=500, text=f"boom {KEY} tail")])
    with pytest.raises(RuntimeError) as ei:
        post_once(SPEC, "p", KEY, transport=transport)
    assert KEY not in str(ei.value) and "***" in str(ei.value)


def test_post_once_err_text_chars():
    spec = EndpointSpec("https://e.invalid", "m", 1.0, 10, err_text_chars=5)
    transport, _ = recorder([Resp(status=400, text="0123456789")])
    with pytest.raises(RuntimeError, match="01234"):
        post_once(spec, "p", KEY, transport=transport)
    transport, _ = recorder([Resp(status=400, text="0123456789")])
    with pytest.raises(RuntimeError) as ei:
        post_once(spec, "p", KEY, transport=transport)
    assert "012345" not in str(ei.value)


# ---------------------------------------------------------------- fetch_text
def test_fetch_text_success_first_try():
    transport, calls = recorder([Resp("c1")])
    counter = {"n": 0}
    out = fetch_text(SPEC, "p", KEY, counter=counter, transport=transport)
    assert out == FetchOutcome("c1", None, 1)
    assert counter["n"] == 1 and len(calls) == 1


def test_fetch_text_retry_after_timeout_then_success():
    class Boom(Exception):
        pass
    transport, calls = recorder([Boom("timed out"), Resp("c2")])
    counter = {"n": 0}
    out = fetch_text(SPEC, "p", KEY, counter=counter, transport=transport)
    assert out.content == "c2" and out.attempts == 2
    assert counter["n"] == 2 and len(calls) == 2  # 预算计数语义


def test_fetch_text_budget_exhausted_sanitized():
    transport, _ = recorder([Resp(status=500, text=f"e1 {KEY}"),
                             Resp(status=500, text=f"e2 {KEY}")])
    out = fetch_text(SPEC, "p", KEY, transport=transport)
    assert out.content is None and out.attempts == 2
    assert KEY not in out.last_err and "e2 ***" in out.last_err


def test_fetch_text_err_msg_chars_truncation():
    """gt3b/gt3c 加固口径：str(e)[:120]。"""
    spec = EndpointSpec("https://e.invalid", "m", 1.0, 10, err_msg_chars=120)
    long_err = "x" * 200
    transport, _ = recorder([ValueError(long_err), ValueError(long_err)])
    out = fetch_text(spec, "p", KEY, transport=transport)
    assert out.last_err == f"ValueError: {'x' * 120}"


def test_fetch_text_empty_content_records_empty_err():
    """bigquiz 口径：空 content 记 empty_err，继续重试直到预算耗尽。"""
    spec = EndpointSpec("https://e.invalid", "m", 1.0, 10, max_attempts=2,
                        empty_err="empty content (finish_reason=length, "
                                  "reasoning overflow)")
    transport, _ = recorder([Resp(""), Resp("")])
    out = fetch_text(spec, "p", KEY, transport=transport)
    assert out.content is None
    assert out.last_err == ("empty content (finish_reason=length, "
                            "reasoning overflow)")
    # 无 empty_err 钉定的口径（gt3 族）：空 content 不改写 last_err
    transport, _ = recorder([Resp(""), Resp("")])
    out = fetch_text(SPEC, "p", KEY, transport=transport)
    assert out.content is None and out.last_err is None


def test_fetch_text_backoff_schedule(monkeypatch):
    """bigquiz 口径：异常后 sleep(3 * 2**i)，含最后一次尝试。"""
    spec = EndpointSpec("https://e.invalid", "m", 1.0, 10, max_attempts=2,
                        backoff_base=3)
    sleeps = []
    monkeypatch.setattr(llm_fetch._t, "sleep", lambda s: sleeps.append(s))
    transport, _ = recorder([ValueError("a"), ValueError("b")])
    out = fetch_text(spec, "p", KEY, transport=transport)
    assert out.content is None
    assert sleeps == [3, 6]


def test_fetch_text_no_counter_ok():
    transport, _ = recorder([Resp("z")])
    out = fetch_text(SPEC, "p", KEY, transport=transport)
    assert out.content == "z"


# ---------------------------------------------------------------- 缓存
def _write(path, rec):
    path.write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")


def test_is_fresh_matrix(tmp_path):
    p = str(tmp_path / "c.json")
    assert not is_fresh(p, "s")                       # 缺失
    _write(tmp_path / "c.json",
           {"prompt_sha256": "s", "response_text": "x", "model": "m"})
    assert is_fresh(p, "s")
    assert is_fresh(p, "s", model="m")
    assert not is_fresh(p, "s", model="other")        # 模型不符（gt3 口径）
    assert not is_fresh(p, "other-sha")               # prompt 漂移
    _write(tmp_path / "c.json", {"prompt_sha256": "s", "response_text": ""})
    assert not is_fresh(p, "s")                       # 空响应不新鲜


def test_is_fresh_strict_modes(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{{{corrupt", encoding="utf-8")
    assert not is_fresh(str(p), "s", strict=True)     # 损坏按不新鲜
    with pytest.raises(Exception):                    # 旧 gt3/familyL/cot 口径
        is_fresh(str(p), "s", strict=False)


def test_save_record_format(tmp_path):
    p = str(tmp_path / "r.json")
    save_record(p, {"domain": "域", "response_text": "中文内容"})
    raw = open(p, encoding="utf-8").read()
    assert "域" in raw                                # ensure_ascii=False
    assert raw.startswith('{\n "domain":')            # indent=1 逐位格式


# ---------------------------------------------------------------- llm_prior 经注入 transport
def test_call_llm_prior_injected_transport(tmp_path, monkeypatch):
    monkeypatch.setenv("KIMI_API_KEY", KEY)
    import llm_prior
    transport, calls = recorder([
        Resp('[{"parent": 0, "child": 1, "confidence": 0.5}]')])

    def explode(*a, **k):
        raise AssertionError("走了真实 requests.post")

    monkeypatch.setattr(llm_fetch.requests, "post", explode)
    cache = str(tmp_path / "prior.json")
    prior = llm_prior.call_llm_prior(cache, labels=["甲", "乙", "丙"],
                                     transport=transport)
    assert prior[(0, 1)] == pytest.approx(0.5)
    assert len(calls) == 1
    raw = open(cache, encoding="utf-8").read()
    assert KEY not in raw and "prompt_sha256" in raw


def test_call_llm_prior_retry_on_parse_failure(tmp_path, monkeypatch):
    monkeypatch.setenv("KIMI_API_KEY", KEY)
    import llm_prior
    transport, calls = recorder([
        Resp("garbage"),
        Resp('[{"parent": 1, "child": 0, "confidence": 0.2}]')])
    prior = llm_prior.call_llm_prior(str(tmp_path / "p.json"),
                                     labels=["甲", "乙", "丙"],
                                     transport=transport)
    assert prior[(1, 0)] == pytest.approx(0.2)
    assert len(calls) == 2  # 解析失败计入重试预算（旧语义保留）


# ---------------------------------------------------------------- 脚本 spec 钉定
def test_fetch_script_specs_pinned():
    import run_v20_bigquiz_fetch as bq
    import run_v20_cot_fetch as cot
    import run_v20_crossval_fetch as cv
    import run_v20_familyL_fetch as fl
    import run_v20_gt3_fetch as g3
    import run_v20_gt3b_fetch as g3b
    import run_v20_gt3c_fetch as g3c
    import llm_prior
    assert g3.GT3_SPEC.endpoint == llm_prior.ENDPOINT
    assert g3.GT3_SPEC.max_tokens == 8000
    assert g3b.GT3B_SPEC.err_msg_chars == 120 and g3b.GT3B_SPEC.timeout == 240.0
    assert g3c.GT3C_SPEC.max_tokens == 16000 and g3c.GT3C_SPEC.err_msg_chars == 120
    assert g3b.GT3B_SPEC.model == "doubao-seed-evolving"
    assert g3c.GT3C_SPEC.model == "deepseek-v4-pro-260425"
    assert bq.BIGQUIZ_SPEC.backoff_base == 3 and bq.BIGQUIZ_SPEC.max_tokens == 16000
    assert bq.BIGQUIZ_SPEC.err_text_chars == 150
    assert cot.COT_SPEC.max_tokens == 2000 and cot.COT_SPEC.err_text_chars == 150
    assert cv.CROSSVAL_SPEC.max_tokens == 8000
    assert fl.FAMILYL_SPEC.max_tokens == 8000
    assert llm_prior._FETCH_SPEC.max_tokens == 4000
    # 各脚本不再自带 def sha / 私有重试循环：统一从 llm_fetch 取
    assert g3.sha is sha and g3b.sha is sha and g3c.sha is sha
    assert bq.sha is sha and cot.sha is sha and cv.sha is sha
