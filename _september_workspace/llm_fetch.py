# -*- coding: utf-8 -*-
# ============================================================
# Deposon LLM fetch 管道统一模块（docs/ARCH_AUDIT_v2.md 候选 3 落地）
#
# 历史：同一套 "requests.post 重试/缓存/落盘" 逻辑被复制在 llm_prior.py +
# 8 个 run_v20_*_fetch.py（≈1636 行），根因是 ENDPOINT/MODEL/TIMEOUT 硬编码
# 为模块常量，换模型/换厂商只能整文件 fork（gt3b vs gt3c 85 行 diff 仅 30 行）。
#
# 本模块提供单一入口：
#   EndpointSpec       —— 端点/模型/超时/预算/错误脱敏口径的显式配置
#   fetch_text(spec, prompt, key, counter=, transport=) -> FetchOutcome
#                        唯一一份重试主循环；transport 依赖注入（默认
#                        requests.post），假 transport 即可 Mock 测试
#   post_once(spec, prompt, key, transport=) -> str
#                        单次尝试（HTTP 状态检查 + content 抽取），供
#                        重试作用域含解析/校验的调用方（llm_prior）复用
#   is_fresh / save_record —— 缓存新鲜度判断与落盘格式（逐位不变）
#   sha / sanitize_secret / parse_json_array —— 原 7 份 def sha、
#                        llm_prior._sanitize、llm_prior._extract_json_array
#                        的唯一实现（旧名为薄别名，既有 import 路径不破）
#
# 红线纪律（与 llm_prior 一致）：
# - API key 只由调用方从环境变量读取后经参数传入；本模块不读环境变量、
#   不打印 key、不把 key 写入任何文件/异常消息（错误文本经 sanitize_secret）。
# - 缓存文件名、prompt_sha256 落盘格式、预算计数语义与各旧副本逐位一致
#   （差异点全部收敛为 EndpointSpec 字段，逐脚本显式钉定）。
# ============================================================
import hashlib
import json
import os
import re
import time as _t
from dataclasses import dataclass, replace
from typing import NamedTuple, Optional

import requests


# ---------------------------------------------------------------- 基础件
def sha(text: str) -> str:
    """sha256 hexdigest（全仓唯一一份；旧各 fetch 脚本的 def sha 收敛于此）。"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sanitize_secret(msg: str, secret: str) -> str:
    """兜底: 异常/HTTP 回显中若意外含有 secret, 一律剔除 (key 不写入日志/异常)。

    （原 llm_prior._sanitize 逐字搬运，含 gt3b/gt3c 的 str(e)[:120] 截断
    加固——截断口径经 EndpointSpec.err_msg_chars 显式钉定。）
    """
    return msg.replace(secret, "***") if secret else msg


def parse_json_array(text: str) -> list:
    """从 LLM 响应中抽出 JSON 数组 (容忍 markdown 围栏与前后杂文本)。

    （原 llm_prior._extract_json_array 逐字搬运转正；旧名保留为薄别名。）
    """
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.MULTILINE).strip()
    i, j = t.find("["), t.rfind("]")
    if i < 0 or j <= i:
        raise ValueError("响应中未找到 JSON 数组")
    return json.loads(t[i:j + 1])


# ---------------------------------------------------------------- 配置
@dataclass(frozen=True)
class EndpointSpec:
    """一次 fetch 的全部显式配置（旧各复制版之间的全部差异点）。

    err_text_chars : HTTP 错误回显截断（200=llm_prior/gt3 族, 150=bigquiz/cot）
    err_msg_chars  : 异常消息 str(e) 截断（None=不截断; 120=gt3b/gt3c 加固）
    backoff_base   : 异常后 sleep(backoff_base * 2**i)（None=不退避; 3=bigquiz）
    empty_err      : content 为空时记录的 last_err（None=不记录;
                     bigquiz 用 "empty content (finish_reason=length, ...)"）
    """
    endpoint: str
    model: str
    timeout: float
    max_tokens: int
    max_attempts: int = 2
    err_text_chars: int = 200
    err_msg_chars: Optional[int] = None
    backoff_base: Optional[float] = None
    empty_err: Optional[str] = None

    def for_model(self, model: str, **kw) -> "EndpointSpec":
        """同端点换模型的薄派生（gt3 逐评估者场景）。"""
        return replace(self, model=model, **kw)


class FetchOutcome(NamedTuple):
    """fetch_text 结果：content 为 None 表示全部尝试失败（不抛异常，
    是否抛错/如何记缓存由调用方按各自旧口径决定）。"""
    content: Optional[str]
    last_err: Optional[str]
    attempts: int


# ---------------------------------------------------------------- 调用
def _headers(key: str) -> dict:
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def _payload(spec: EndpointSpec, prompt: str) -> dict:
    return {"model": spec.model, "max_tokens": spec.max_tokens,
            "messages": [{"role": "user", "content": prompt}]}


def post_once(spec: EndpointSpec, prompt: str, key: str,
              transport=None) -> str:
    """单次 HTTP 尝试：状态检查 + content 抽取。

    返回 content（可能为 falsy 空串，由调用方判定）；HTTP 非 200 抛
    RuntimeError（已脱敏）；网络/解析异常原样上抛（脱敏在 fetch_text
    或调用方 except 中进行，与旧副本语义一致）。
    transport 依赖注入：签名同 requests.post；None 时用 requests.post
    （调用时解析，monkeypatch requests.post 的旧测试路径保持有效）。
    """
    if transport is None:
        transport = requests.post
    r = transport(spec.endpoint, headers=_headers(key), json=_payload(spec, prompt),
                  timeout=spec.timeout)
    if r.status_code != 200:
        raise RuntimeError(sanitize_secret(
            f"HTTP {r.status_code}: {r.text[:spec.err_text_chars]}", key))
    return r.json()["choices"][0]["message"]["content"]


def fetch_text(spec: EndpointSpec, prompt: str, key: str, counter=None,
               transport=None) -> FetchOutcome:
    """唯一一份 fetch 重试主循环（旧 8 份逐行复制的统一体）。

    语义逐位对应旧副本：每次尝试 attempts+=1（且 counter["n"]+=1，若给）；
    content 非空即成功停止；异常脱敏（err_msg_chars 截断口径）后记 last_err，
    按 backoff_base 指数退避；空 content 按 spec.empty_err 记录。
    不抛异常——失败返回 FetchOutcome(None, last_err, attempts)。
    """
    content, last_err, attempts = None, None, 0
    for i in range(spec.max_attempts):
        attempts += 1
        if counter is not None:
            counter["n"] += 1
        try:
            c = post_once(spec, prompt, key, transport=transport)
            if c:
                content = c
                break
            if spec.empty_err is not None:
                last_err = spec.empty_err
        except Exception as e:
            if spec.err_msg_chars is None:
                last_err = sanitize_secret(f"{type(e).__name__}: {e}", key)
            else:
                last_err = sanitize_secret(
                    f"{type(e).__name__}: {str(e)[:spec.err_msg_chars]}", key)
            if spec.backoff_base is not None:
                _t.sleep(spec.backoff_base * (2 ** i))
    return FetchOutcome(content, last_err, attempts)


# ---------------------------------------------------------------- 缓存
def is_fresh(path: str, prompt_sha: str, model: str = None,
             strict: bool = True) -> bool:
    """缓存新鲜度：prompt_sha256 一致（且 model 一致，若给）且 response_text
    非空。strict=True 时缓存损坏按不新鲜处理（旧 bigquiz/crossval/gt8b 口径）；
    strict=False 时 json 解析错误原样上抛（旧 gt3/gt3b/gt3c/familyL/cot 口径）。
    """
    if not os.path.exists(path):
        return False
    if strict:
        try:
            rec = json.load(open(path, encoding="utf-8"))
        except Exception:
            return False
    else:
        rec = json.load(open(path, encoding="utf-8"))
    if rec.get("prompt_sha256") != prompt_sha:
        return False
    if model is not None and rec.get("model") != model:
        return False
    return bool(rec.get("response_text"))


def save_record(path: str, rec: dict) -> None:
    """落盘缓存记录：ensure_ascii=False, indent=1（全 fetch 族统一格式）。"""
    json.dump(rec, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
