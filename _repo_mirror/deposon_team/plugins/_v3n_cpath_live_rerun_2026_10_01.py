# -*- coding: utf-8 -*-
"""
_v3n_cpath_live_rerun_2026_10_01.py
=========================================
V3-N #32 CPATH 理论模拟实测 (Trae 回函 §1.2 标注表 #32「不明」的补齐实测面)

来源件 (先核后用, 逐件登记):
- docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md  (设计字面来源)
    §7.2「若实测 C 路径(成本 ~0.05 USD)」5 步字面:
      1. 拿 30 cells question 文本 → Volcengine doubao-embedding-vision-251215 算 2048-d embedding
      2. cos sim(30 question, 22 caption) → top-3 caption per cell
      3. 拼 prompt:`Question: ... \n Context: caption1, caption2, caption3 \n Answer in one number/Yes or No:`
      4. GLM-5.3 实测 30 cells with context
      5. 对比 no-RAG 22/30 vs with-RAG ?/30
- results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json  (no-RAG 30 cells baseline, 22/30)
- results/deposon_volcengine_22caption_embedding_2026_09_10.json     (22 caption 构造字面 + 端点/model)
- corpus/v20/strip_captions_22.json + corpus/v20/index.json          (22 caption 原文可复算)

判定: 沿原报告 §4.3 判据字面 —— 实测 with-RAG 答对率 vs no-RAG 73.3%,
      理论边际区间原报告写死 0% ~ +26.7% (完美 oracle 边界)。0 新设阈值。

铁律:
- LLM 调用: 串行, 间隔 >= 2.5s, 最小必要次数 (6 embeddings + 30 chat = 36)
- key 永不明文: 仅 runtime 从 env ARK_API_KEY 读, 不落盘/不入 prompt/不入 JSON/不入 log
- 端点即用即探 (无预探)
- 既有件 0 触动 (只读输入, 只写新 JSON)

符号口径留注 (E3 裁定 2026-10-01, 登记件 results/_cpath_e3_sign_normalization_2026_10_01.md):
- 原字面 `top3_T_frac_mean` 裸取 svd2 PC1 **带号** 坐标 (22 条实测全负, 均值 -0.8181),
  落盘 avg = -0.8219; 报告 de772cd9e7ba §2「T(透射)占比」列全为正 (0.423~0.996)。
- E3 裁: **统一采报告侧正号约定** -> 本副本 PC1 项改为取绝对值 (abs), 后续运行落盘为正。
- 改前本副本 3e932a5409b5 / 20,831 B -> 改后指纹见登记件 §4 (本件不自指)。
- 0 改判定: 本字段**不参与** verdict 计算 (verdict 段 0 引用 T_frac), 仅检索面描述量;
  既有数据件 7c26d08ece3b 与判定件 a91efbfec3d0 **0 写入**, 其 -0.8219 为历史留痕字面。
- 上游源 runner _v3n_cpath_live_2026_09_27.py (5248ba7ac21c) 为输入链证据项, **0 触动**。
- 量种仍不同 (未裁): 报告 T 占比 = PC1^2/(PC1^2+PC2^2) 能量占比 (平方天然消号),
  本字段 = |PC1| 投影坐标; 正号已统一, 量种对齐**待 PI**。

作者: Mavis 团队 worker | 2026-09-27 (E3 符号口径改动: Mavis 团队 worker | 2026-10-01)
"""
from __future__ import annotations

import io
import json
import math
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = r"D:\私人资料\deposon-repo"
BASELINE_30 = os.path.join(REPO, "results", "deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json")
CAPTION_EMB = os.path.join(REPO, "results", "deposon_volcengine_22caption_embedding_2026_09_10.json")
CAPTION_TXT = os.path.join(REPO, "corpus", "v20", "strip_captions_22.json")
CORPUS_IDX = os.path.join(REPO, "corpus", "v20", "index.json")
OUT_JSON = os.path.join(REPO, "results", "_v3n_cpath_live_rerun_2026_10_01.json")  # 新名: 0 覆写既有件 25374af92f88

# --- 端点/模型: 逐字沿用 baseline 件 (0 新设) ---
CHAT_BASE = "https://ark.cn-beijing.volces.com/api/coding/v3"
CHAT_MODEL = "glm-latest"
EMB_BASE = "https://ark.cn-beijing.volces.com/api/coding/v3/embeddings"
EMB_MODEL = "doubao-embedding-vision-251215"
EMB_BATCH = 10  # baseline 件记: Volc Ark Embeddings input limit = 10

MIN_INTERVAL_S = 2.5   # 派工单硬纪律
TOP_K = 3              # 原报告 §4.2 top_k = 3
CALL_LOG: list[dict] = []
_LAST_CALL_T = [0.0]


def _key() -> str:
    """runtime 读 key (env 优先)。key 永不入返回值之外的任何去处。"""
    v = os.environ.get("ARK_API_KEY", "").strip()
    if not v:
        raise RuntimeError("ARK_API_KEY 未设置 (runtime env 读, 不落盘)")
    return v


def _throttle() -> None:
    dt = time.time() - _LAST_CALL_T[0]
    if dt < MIN_INTERVAL_S:
        time.sleep(MIN_INTERVAL_S - dt)


class QuotaBlocked(RuntimeError):
    """端点月度配额耗尽 —— 硬阻断, 不重试轰炸, 不编造替代值。"""


def _post(url: str, body: dict, timeout: int = 60) -> dict:
    _throttle()
    t0 = time.time()
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + _key()},
        method="POST",
    )
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                out = json.loads(r.read().decode("utf-8"))
            CALL_LOG.append({
                "url_suffix": url.split("/api/")[-1], "model": body.get("model"),
                "kind": "embeddings" if "embeddings" in url else "chat",
                "n_items": len(body.get("input", [])) if "input" in body else 1,
                "http": 200, "ms": round((time.time() - t0) * 1000, 1), "attempt": attempt + 1,
            })
            return out
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                pass
            if e.code == 429 and "AccountQuotaExceeded" in detail:
                CALL_LOG.append({
                    "url_suffix": url.split("/api/")[-1], "model": body.get("model"),
                    "http": 429, "error_code": "AccountQuotaExceeded",
                    "reset_hint": "2026-09-30 23:59:59 +0800 CST (端点返回原文)",
                    "retried": False, "ms": round((time.time() - t0) * 1000, 1),
                })
                raise QuotaBlocked("AccountQuotaExceeded (月度配额耗尽, 2026-09-30 重置)")
            last_err = e
            time.sleep(3.0)
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(3.0)
    CALL_LOG.append({
        "url_suffix": url.split("/api/")[-1], "model": body.get("model"), "http": "ERROR",
        "error_type": type(last_err).__name__, "ms": round((time.time() - t0) * 1000, 1),
    })
    raise RuntimeError(f"API 调用失败(不编造): {type(last_err).__name__}")


def _checkpoint(out: dict) -> None:
    """每阶段落盘, 保证被配额阻断时已完成部分不丢。"""
    out["llm_call_ledger"] = {
        "total_calls": len(CALL_LOG),
        "embeddings_calls": sum(1 for c in CALL_LOG if c.get("kind") == "embeddings"),
        "chat_calls": sum(1 for c in CALL_LOG if c.get("kind") == "chat"),
        "min_interval_enforced_s": MIN_INTERVAL_S, "serial": True, "concurrent_burst": False,
        "key_plaintext_in_outputs": False,
        "key_source": "runtime env ARK_API_KEY (不落盘/不入 prompt/不入 JSON/不入 log)",
        "per_call": CALL_LOG,
    }
    json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- 判分器
# 注: baseline 件的 extracted_number / extracted_label 由一个**已不可得**的抽取器产生
# (baseline 件只落盘了抽取结果, 未落盘抽取器本体)。为隔离 RAG 效应, 本脚本对
# 「原 no-RAG 30 条已存 response_text」与「新 with-RAG 30 条」用**同一个**抽取器重判,
# 0 新设阈值; 抽取规则本身在本件显式声明, 可复算。
_BOLD = re.compile(r"\*\*\s*(-?\d[\d,]*(?:\.\d+)?)\s*\*\*")
_NUM = re.compile(r"-?\d[\d,]*(?:\.\d+)?")


def extract_gsm8k(resp: str):
    m = _BOLD.search(resp)
    if m:
        return float(m.group(1).replace(",", ""))
    m = _NUM.search(resp)
    if m:
        return float(m.group(0).replace(",", ""))
    return None


def extract_sqa(resp: str):
    m = re.search(r"\b(yes|no)\b", resp, re.IGNORECASE)
    if m:
        return m.group(1).capitalize()
    return None


def score(cell: dict, resp: str):
    if cell["benchmark"] == "gsm8k":
        got = extract_gsm8k(resp)
        exp = float(cell["expected_answer"])
        ok = got is not None and abs(got - exp) <= max(1e-6, abs(exp) * 1e-6)
        return {"extracted": got, "expected": exp, "is_correct": bool(ok)}
    got = extract_sqa(resp)
    exp = str(cell["expected_answer"]).capitalize()
    return {"extracted": got, "expected": exp, "is_correct": bool(got == exp)}


# ---------------------------------------------------------------- caption 复原
def rebuild_captions() -> list[dict]:
    """按 baseline 22caption 件的 caption_construction 字面复原 22 条 caption 原文。"""
    strip = json.load(open(CAPTION_TXT, encoding="utf-8"))
    idx = json.load(open(CORPUS_IDX, encoding="utf-8"))
    meta = {g["graph_id"]: g for g in idx["graphs"]}
    out = []
    for s in strip:
        g = meta[s["id"]]
        text = (
            f"Concept graph {g['graph_id']} (family={g['family']}, structure={g['structure']}, "
            f"N={g['N']}, n_named={g['n_named']}): " + s["text"]
        )
        out.append({"id": s["id"], "family": s["family"], "text": text,
                    "N": g["N"], "n_named": g["n_named"]})
    return out


def embed(texts: list[str], tag: str = "") -> list[list[float]]:
    vecs: list[list[float]] = []
    for i in range(0, len(texts), EMB_BATCH):
        chunk = texts[i:i + EMB_BATCH]
        r = _post(EMB_BASE, {"model": EMB_MODEL, "input": chunk})
        for it in r["data"]:
            vecs.append(it["embedding"])
    return vecs


def cos(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


def main() -> int:
    t_start = time.time()
    base = json.load(open(BASELINE_30, encoding="utf-8"))
    emb_meta = json.load(open(CAPTION_EMB, encoding="utf-8"))
    cells = base["cells"]
    captions = rebuild_captions()
    assert len(captions) == 22, f"caption 数不符: {len(captions)}"

    out: dict = {
        "task": "V3-N #32 CPATH 理论模拟实测 (补齐 Trae 回函 §1.2 #32「不明」实测面)",
        "date": "2026-10-01",
        "author": "Mavis 团队 worker (agent: worker)",
        "rerun_of": "deposon_team/plugins/_v3n_cpath_live_2026_09_27.py (5248ba7ac21c / 19,823 B) — 执行逻辑逐字沿用, 0 改动",
        "rerun_trigger": "T1 ark key 恢复 (runtime env 存在性已核) + T2 配额重置点 2026-09-30 23:59:59 +0800 已过 + T3 PI 放行 (排期 v4 T1-5 「#32 补跑」 + 本晨开工批)",
        "rerun_extractor_open_face": "抽取器口径未裁 (426cfe18cf65 §8-2 待 PI): stored 22/30 vs 同抽取器重判 24/30, 差额 -2 全在 gsm8k; 本次按 runner 现字面执行, 0 新设 0 代裁",
        "rerun_prior_state": "_v3_n_cpath_live_data_2026_09_27.json (25374af92f88) 09-30 重跑停在第 1 次 embedding 即 429 AccountQuotaExceeded, with-RAG 0 条; 首跑 09-27 768c 12/30 仅 stdout 存活已丢失(不补写)",
        "rerun_no_overwrite": "上游 runner OUT_JSON 指向既有件 _v3_n_cpath_live_data_2026_09_27.json; 本副本改新名输出, 既有件 0 触动",
        "design_source": "docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md §7.2 (5 步字面)",
        "verdict_criteria_literal": {
            "theoretical_margin_band": "0% ~ +26.7% (原报告 §5, 完美 oracle 边界)",
            "no_rag_baseline": "22/30 = 73.3% (原报告 §3/§4.3)",
            "new_thresholds_introduced": 0,
        },
        "endpoints": {
            "chat_base": CHAT_BASE, "chat_model": CHAT_MODEL,
            "embedding_endpoint": EMB_BASE, "embedding_model": EMB_MODEL,
            "note": "逐字沿用 baseline 件; Volcengine Ark 非 teamorouter/openrouter → tun 代理不适用",
        },
        "extractor_declaration": {
            "why_redeclared": "baseline 件只落盘抽取结果, 抽取器本体不可得; "
                              "为隔离 RAG 效应, no-RAG 与 with-RAG 用同一抽取器重判",
            "gsm8k": "优先首个 **bold** 数字, 否则首个数字; 与 expected 比 |Δ| <= 1e-6*|exp|",
            "strategyqa": "首个 \\b(yes|no)\\b (忽略大小写); 与 expected 字符串比",
        },
        "input_chain": {}, "retrieval": [], "no_rag_rescored": [], "with_rag": [],
        "llm_call_ledger": {}, "outcome": {},
    }

    for k, v in {
        "baseline_30cells": "results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json",
        "caption_embedding_meta": "results/deposon_volcengine_22caption_embedding_2026_09_10.json",
        "caption_text_22": "corpus/v20/strip_captions_22.json",
        "corpus_index": "corpus/v20/index.json",
    }.items():
        p = os.path.join(REPO, v.replace("/", os.sep))
        out["input_chain"][k] = {
            "path": v, "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else None,
        }

    print("[1/5] 复原 22 caption 原文 ...")
    print("      sample:", captions[0]["text"][:110])
    out["caption_22_rebuilt"] = [{"id": c["id"], "family": c["family"],
                                  "N": c["N"], "n_named": c["n_named"],
                                  "text_len": len(c["text"])} for c in captions]
    out["caption_construction_literal"] = emb_meta["caption_construction"]

    print("[2/5] no-RAG 30 条用同一抽取器重判 (0 LLM, 隔离 RAG 效应) ...")
    for c in cells:
        s = score(c, c["response_text"] or "")
        out["no_rag_rescored"].append({
            "id": c["id"], "benchmark": c["benchmark"], **s,
            "stored_is_correct": c["is_correct"], "stored_ms": c["ms"],
        })
    gsm = [r for r in out["no_rag_rescored"] if r["benchmark"] == "gsm8k"]
    sqa = [r for r in out["no_rag_rescored"] if r["benchmark"] == "strategyqa"]
    no_rag_pass = sum(1 for r in out["no_rag_rescored"] if r["is_correct"])
    no_rag_rate = no_rag_pass / 30.0
    stored_pass = sum(1 for c in cells if c["is_correct"])
    out["no_rag_summary"] = {
        "rescored_pass": no_rag_pass, "rescored_rate": round(no_rag_rate, 4),
        "gsm8k": f"{sum(1 for r in gsm if r['is_correct'])}/15",
        "strategyqa": f"{sum(1 for r in sqa if r['is_correct'])}/15",
        "stored_pass": stored_pass, "stored_rate": round(stored_pass / 30.0, 4),
        "note": "stored 22/30 由不可得抽取器产生; 本脚本以声明抽取器重判得 "
                f"{no_rag_pass}/30, 差额根因 = 抽取器口径差异(非 RAG 效应)",
    }
    _checkpoint(out)   # 0-LLM 部分先落盘
    print(f"      no-RAG 重判 {no_rag_pass}/30 = {no_rag_rate:.1%} "
          f"(stored {stored_pass}/30, 抽取器口径差 {stored_pass - no_rag_pass:+d})")

    print("[3/5] embed 22 captions + 30 questions (doubao-embedding-vision-251215) ...")
    try:
        cap_vecs = embed([c["text"] for c in captions])
        q_vecs = embed([c["question"] for c in cells])
    except QuotaBlocked as e:
        out["blocked"] = {"stage": "embedding (step 2/§7.2.1+2.2)",
                          "error": "AccountQuotaExceeded (HTTP 429)",
                          "message": str(e),
                          "reset": "2026-09-30 23:59:59 +0800 CST (端点返回原文)",
                          "consequence": "cos sim -> top-3 检索与 with-RAG 实测**均无法执行**; "
                                         "本条 CPATH 实测登记为**未决**(不编造边际数据)"}
        out["outcome"] = {"status": "BLOCKED_BY_ENDPOINT_QUOTA",
                          "completed_parts": ["输入链核验", "22 caption 原文复原", "no-RAG 30 条同抽取器重判"],
                          "blocked_parts": ["30 question + 22 caption embedding", "top-3 检索", "with-RAG 30 cells 实测", "边际判定"],
                          "elapsed_s": round(time.time() - t_start, 1)}
        _checkpoint(out)
        print(f"      !! 配额阻断: {e}")
        print(f"OUT: {OUT_JSON}")
        return 0
    assert len(cap_vecs) == 22 and len(q_vecs) == 30
    out["embedding_dim"] = len(cap_vecs[0])
    print(f"      dim={out['embedding_dim']}, caption 22 + question 30 向量就绪")

    print("[4/5] cos sim -> top-3 caption per cell ...")
    for i, c in enumerate(cells):
        sims = [cos(q_vecs[i], cv) for cv in cap_vecs]
        order = sorted(range(22), key=lambda j: sims[j], reverse=True)
        top = order[:TOP_K]
        out["retrieval"].append({
            "id": c["id"], "benchmark": c["benchmark"],
            "top3": [{"caption_id": captions[j]["id"], "cos": round(sims[j], 4)} for j in top],
            "top3_T_frac_mean": round(sum(
                # [E3 2026-10-01] 报告侧「T(透射)占比」为正号约定 -> PC1 取绝对值。
                # 改前为裸取带号坐标 (本语料 22 条全负); 0 改判定面 (本字段不参与 verdict)。
                abs(emb_meta["svd2_coords"][captions[j]["id"]][0]) for j in top) / TOP_K, 4),
        })
    _checkpoint(out)
    print(f"      top-3 检索完成, avg_top3_T_frac = "
          f"{sum(r['top3_T_frac_mean'] for r in out['retrieval']) / 30:.4f}")

    print("[5/5] GLM-5.3 with-context 30 cells (串行, >=2.5s) ...")
    blocked_at = None
    for n, c in enumerate(cells, 1):
        r = out["retrieval"][n - 1]
        ctx_ids = [t["caption_id"] for t in r["top3"]]
        ctx_text = "; ".join(next(x["text"] for x in captions if x["id"] == cid)
                             for cid in ctx_ids)
        lines = c["prompt"].split("\n")
        prompt = lines[0] + "\nContext: " + ctx_text + "\n" + lines[-1]
        t0 = time.time()
        try:
            resp = _post(CHAT_BASE + "/chat/completions", {
                "model": CHAT_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0, "max_tokens": 512,
            }, timeout=120)
        except QuotaBlocked as e:
            blocked_at = {"cell_index": n, "id": c["id"], "error": str(e),
                          "reset": "2026-09-30 23:59:59 +0800 CST"}
            print(f"      !! 配额阻断于第 {n}/30 条 (id={c['id']}): {e}")
            _checkpoint(out)
            break
        text = resp["choices"][0]["message"]["content"]
        s = score(c, text)
        rec = {
            "id": c["id"], "benchmark": c["benchmark"], **s,
            "top3_caption_ids": ctx_ids,
            "top3_cos": [t["cos"] for t in r["top3"]],
            "ms": round((time.time() - t0) * 1000, 1),
            "usage": resp.get("usage", {}),
            "response_text": text,
        }
        out["with_rag"].append(rec)
        _checkpoint(out)   # 逐条落盘
        print(f"      [{n:2d}/30] {c['benchmark']:11s} id={c['id']:2d} "
              f"got={s['extracted']!r:>10} exp={s['expected']!r:>6} "
              f"{'OK ' if s['is_correct'] else 'X  '} {rec['ms']:>7.0f}ms")

    n_done = len(out["with_rag"])
    wr_pass = sum(1 for r in out["with_rag"] if r["is_correct"])
    out["with_rag_summary"] = {
        "n_completed": n_done, "n_planned": 30,
        "pass_on_completed": wr_pass,
        "note": ("全部 30 条完成" if n_done == 30 else
                 f"仅前 {n_done}/30 条完成, 后续被端点配额阻断"),
        "total_tokens": sum(r["usage"].get("total_tokens", 0) for r in out["with_rag"]),
    }
    if n_done < 30:
        out["blocked"] = {"stage": "with-RAG chat (step 4/§7.2.4)",
                          "error": "AccountQuotaExceeded (HTTP 429)",
                          "detail": blocked_at,
                          "reset": "2026-09-30 23:59:59 +0800 CST (端点返回原文)",
                          "consequence": "30-cell 实测不完整; 边际**不判定**(不外推不编造)"}
        out["outcome"] = {
            "status": "PARTIAL_BLOCKED_BY_ENDPOINT_QUOTA",
            "completed_parts": ["输入链核验", "22 caption 复原", "no-RAG 重判", "embedding", "top-3 检索"],
            "blocked_parts": [f"with-RAG 第 {blocked_at['cell_index']}/30 条起"],
            "elapsed_s": round(time.time() - t_start, 1),
        }
        _checkpoint(out)
        print()
        print(f"VERDICT  with-RAG 实测不完整 ({n_done}/30) → 边际**不判定**, 登记未决")
        print(f"OUT: {OUT_JSON}")
        return 0

    wr_gsm = sum(1 for r in out["with_rag"] if r["benchmark"] == "gsm8k" and r["is_correct"])
    wr_sqa = sum(1 for r in out["with_rag"] if r["benchmark"] == "strategyqa" and r["is_correct"])
    margin = wr_pass / 30.0 - no_rag_rate
    out["with_rag_summary"].update({
        "pass": wr_pass, "rate": round(wr_pass / 30.0, 4),
        "gsm8k": f"{wr_gsm}/15", "strategyqa": f"{wr_sqa}/15",
    })
    out["verdict"] = {
        "no_rag_rescored": f"{no_rag_pass}/30 ({no_rag_rate:.1%})",
        "with_rag": f"{wr_pass}/30 ({wr_pass/30.0:.1%})",
        "measured_margin_vs_rescored_no_rag": f"{margin:+.4f} ({margin*100:+.1f} pp)",
        "original_report_band": "0% ~ +26.7%",
        "margin_in_band": bool(0.0 <= margin <= 0.267),
        "verdict_literal": None,
    }
    v = out["verdict"]
    if margin < 0:
        v["verdict_literal"] = "证伪 (实测边际 < 0, 落在原报告 0% 下界之外)"
    elif margin <= 0.267:
        v["verdict_literal"] = "成立 (实测边际落在原报告 0% ~ +26.7% 带内)"
    else:
        v["verdict_literal"] = "超出原报告带 (实测边际 > +26.7%, 超理论 oracle 边界)"

    out["outcome"] = {"status": "COMPLETED", "elapsed_s": round(time.time() - t_start, 1)}
    _checkpoint(out)
    print()
    print(f"VERDICT  no-RAG(重判) {no_rag_pass}/30  vs  with-RAG {wr_pass}/30")
    print(f"         边际 {margin*100:+.1f} pp   原报告带 0% ~ +26.7%")
    print(f"         -> {v['verdict_literal']}")
    print(f"OUT: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
