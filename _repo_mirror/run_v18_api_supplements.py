# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.8 API 补实验脚本 (docs/SPEC_v1.8.md)
#   → results/deposon_v18_api_supplements.json
#
# 动机 (评审三点担忧):
#   (a) v1.6/v1.7.1 的阴性对照是程序生成的 synthetic null (随机边/置信度打乱),
#       缺少「同模型但标签打乱」的 LLM 输出对照 → E1。
#   (b) 先验命中 named 边可能来自训练数据污染而非语义推断 → E2 (自陈式探针)。
#   (c) hybrid_norm@2 named=0.471 对 prompt 措辞/方向定义的稳健性未知 → E3。
#
# 复用口径 (全部 import, 不复制改写):
#   - llm_prior: ENDPOINT/MODEL/MAX_ATTEMPTS/TIMEOUT/build_prior_prompt/
#     _sanitize/_extract_json_array/_validate_prior/load_prior (v1.6 模块, 只读复用)。
#   - run_v15_experiment.reconstruct_mindmap: 返回 (N, adj, edges, labels, meta),
#     labels 在索引 [3]; 金边=edges (49 条), named 边=meta["path_edges_named"] (17 条)。
#   - run_v17_fusion_fix: minmax_mask/norm_hybrid/raw_hybrid/prior_only
#     (该脚本 main 在 __main__ 守卫内, import 无副作用, 可直接复用纯函数)。
#   - run_v16_llm_prior.prior_score_matrix。
#   留一评分与 v1.7.1 完全一致: 同图/同种子 70000+ei/同 N_NEG=10/同行负采样池/
#   top-3; base 臂按 field_guided→random→degree 顺序消耗 rng 后再取 tiebreak,
#   使 real 先验臂数字可逐位复现 v1.7.1 (tests/test_v18.py 有回归断言)。
#
# 红线:
#   - 零泄漏: 三个 prompt 只含节点标签列表, 不含任何边/图结构信息;
#     E1 的打乱只对标签顺序操作 (确定性置换 seed=188001)。
#   - key 仅从环境变量 KIMI_API_KEY 读取 (main 中唯一一处), 不打印/不落盘;
#     错误文本一律经 llm_prior._sanitize 兜底剔除 key; 严禁 mock 冒充真实调用。
#   - API 预算: 3 个 prompt, 每个 ≤ MAX_ATTEMPTS=2 次 HTTP 尝试, 合计 ≤ 6 次。
#   - --dry-run 不读 key、不发请求, 可在无 KIMI_API_KEY 环境运行。
# ============================================================
import argparse
import hashlib
import json
import os
import re
import time

import numpy as np
import requests

from deposon_diffusion import DiffusionConfig, config_dict
import llm_prior
from llm_prior import (ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT,
                       build_prior_prompt, _sanitize, _extract_json_array,
                       _validate_prior, load_prior)
from run_v15_experiment import (N_NEG, TOP_K, arm_scores, mean_std,
                                reconstruct_mindmap, row_normalize,
                                top3_hit_per_edge)
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import minmax_mask, norm_hybrid, raw_hybrid, prior_only  # noqa: F401  (minmax_mask 经 norm_hybrid 间接使用, 显式 import 表明口径出处)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v18_api_supplements.json")
CACHE_V16 = os.path.join(RESULTS, "llm_prior_cache.json")            # 只读
CACHE_E1 = os.path.join(RESULTS, "llm_prior_cache_v18_labelshuffle.json")
CACHE_E2 = os.path.join(RESULTS, "llm_prior_cache_v18_contamination.json")
CACHE_E3 = os.path.join(RESULTS, "llm_prior_cache_v18_direction.json")
CACHE_E4 = os.path.join(RESULTS, "llm_prior_cache_v18_contentless.json")
V171_PATH = os.path.join(RESULTS, "deposon_v17_fusion_fix.json")     # 只读参考

PERM_SEED = 188001                  # E1 确定性标签置换种子 (预登记)
LAMBDAS_V18 = (0.5, 2.0)            # 预登记 λ 子集, 全报
EXPERIMENTS = ("E1", "E2", "E3", "E4")
# 预登记判定容差 (SPEC v1.8):
NULL_TOL = 0.06                     # E1 named 与 synthetic null 水平的「≈」带宽
REAL_GAP = 0.06                     # E1 须低于 real 先验的最小差距
E3_TOL = 0.12                       # E3 融合 named 相对 v1.7.1 hybrid_norm@2 (0.471) 的容差
CHANCE_RATIO = 3.0                  # E2 recalled_edges 重叠「显著超机会」的倍数门槛


# ---------------------------------------------------------------- 工具
def sha256_text(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def _write_json(path: str, obj: dict) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def _load_cache_if_fresh(path: str, sha: str) -> dict | None:
    """缓存存在且 prompt_sha256 与本次构造一致 → 复用 (幂等重跑, 0 次 API)。"""
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            rec = json.load(f)
    except Exception:
        return None
    return rec if rec.get("prompt_sha256") == sha else None


def _prior_from_entries(entries: list) -> dict:
    """缓存 prior 列表 → dict[(int,int), float] (与 llm_prior.load_prior 同口径)。"""
    out = {}
    for it in entries:
        u, v = int(it["parent"]), int(it["child"])
        if u == v:
            continue
        out[(u, v)] = min(1.0, max(0.0, float(it["confidence"])))
    return out


# ---------------------------------------------------------------- prompt 构造
def shuffle_labels(labels: list, seed: int = PERM_SEED):
    """E1 确定性置换: shuffled_labels[i] = labels[perm[i]]。只动标签顺序。"""
    rng = np.random.default_rng(seed)
    perm = rng.permutation(len(labels))
    shuffled = [labels[int(perm[i])] for i in range(len(labels))]
    return shuffled, perm


def map_shuffled_prior(prior_shuffled: dict, perm) -> dict:
    """E1 索引映射: 打乱空间边 (i,j) → 原节点空间 (perm[i], perm[j]), confidence 保留。"""
    return {(int(perm[u]), int(perm[v])): float(c)
            for (u, v), c in prior_shuffled.items()}


def build_e1_prompt(labels: list) -> str:
    """E1 prompt = v1.6 同一 build_prior_prompt 作用于打乱后的标签。"""
    shuffled, _perm = shuffle_labels(labels)
    return build_prior_prompt(shuffled)


def build_e2_prompt(labels: list) -> str:
    """E2 训练污染自陈探针。零泄漏: 只给标签列表, 询问来源识别;
    输出严格 JSON 对象 (recognized/confidence/basis/recalled_edges)。"""
    lines = [f"{i}: {lab}" for i, lab in enumerate(labels)]
    return (
        "你是训练数据审计探针。下面是一张脑图的全部节点标签列表"
        "（只有标签，没有给你任何连接关系）。\n"
        + "\n".join(lines)
        + "\n\n请回答：这组节点标签整体是否可能来自你训练数据中出现过的"
        "某份具体脑图或文档？只凭你自己的判断如实回答，"
        "输出严格 JSON 对象（不要任何额外文字、不要 markdown 围栏），格式：\n"
        '{"recognized": true或false, "confidence": 0到1的浮点数, '
        '"basis": "一句话判断依据", '
        '"recalled_edges": [{"parent": 父节点索引, "child": 子节点索引}, ...]}\n'
        "规则：\n"
        "1. recognized 表示你是否认为认得这个节点集合的具体来源。\n"
        "2. recalled_edges 仅在你确实能回忆起具体关联时填写，parent 与 child "
        "必须是上面列表中出现的索引（整数），不得自指；回忆不出就填空数组。\n"
        "3. 不得编造：没有把握就令 recognized=false。只输出 JSON 对象本身。"
    )


def build_e3_prompt(labels: list) -> str:
    """E3 prompt = v1.6 build_prior_prompt + 显式方向定义 + justification 字段。
    解析时忽略 justification, 只取 (parent, child, confidence)。"""
    return (
        build_prior_prompt(labels)
        + "\n补充规则（方向定义，必须遵守）：\n"
        "5. 方向定义：parent 为语义上位/原因/整体，child 为语义下位/结果/部分。\n"
        "6. 每条关联附 justification 字段：一句中文说明该方向为何成立"
        "（不超过 30 字）。\n"
        "输出格式相应为：\n"
        '[{"parent": 父节点索引, "child": 子节点索引, "confidence": 0到1的浮点数, '
        '"justification": "方向理由"}, ...]\n'
        "仍然只输出 JSON 数组本身。"
    )


def contentless_tokens(n: int) -> list:
    """E4 无语义标签: 等长不透明占位符, 与原节点索引一一对应 (无置换)。"""
    return [f"item_{i:02d}" for i in range(n)]


def build_e4_prompt(labels: list) -> str:
    """E4 语义摧毁阴性对照 (SPEC v1.8.1 增补) = v1.6 同一 build_prior_prompt
    作用于无语义占位标签。与 E1 的区别: E1 只置换标签顺序 (语义对置换透明,
    不构成语义阴性对照), E4 直接抹除标签语义内容 —— 若先验仍携带信号,
    则该信号只能来自索引偏置等形式 artifact。"""
    return build_prior_prompt(contentless_tokens(len(labels)))


def build_all_prompts(labels: list) -> dict:
    return {"E1": build_e1_prompt(labels),
            "E2": build_e2_prompt(labels),
            "E3": build_e3_prompt(labels),
            "E4": build_e4_prompt(labels)}


# ---------------------------------------------------------------- 解析器
def _extract_json_object(text: str) -> dict:
    """从 LLM 响应中抽出 JSON 对象 (容忍 markdown 围栏与前后杂文本)。
    与 llm_prior._extract_json_array 同一容错模式, 对象为 {} 而非 []。"""
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.MULTILINE).strip()
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j <= i:
        raise ValueError("响应中未找到 JSON 对象")
    obj = json.loads(t[i:j + 1])
    if not isinstance(obj, dict):
        raise ValueError("抽出的 JSON 不是对象")
    return obj


def parse_contamination_response(text: str, n_labels: int) -> dict:
    """E2 响应解析+校验; 非法输入抛 ValueError (confidence 截断到 [0,1],
    与 llm_prior._validate_prior 的截断口径一致)。"""
    obj = _extract_json_object(text)
    if "recognized" not in obj or "confidence" not in obj or "basis" not in obj:
        raise ValueError("E2 响应缺少 recognized/confidence/basis 字段")
    recognized = bool(obj["recognized"])
    confidence = min(1.0, max(0.0, float(obj["confidence"])))
    basis = str(obj["basis"])
    recalled_raw = obj.get("recalled_edges", [])
    if not isinstance(recalled_raw, list):
        raise ValueError("recalled_edges 必须是数组")
    recalled = []
    for it in recalled_raw:
        u, v = int(it["parent"]), int(it["child"])
        if not (0 <= u < n_labels and 0 <= v < n_labels):
            raise ValueError(f"recalled_edges 索引越界: ({u}, {v}) n_labels={n_labels}")
        if u == v:
            continue  # 自指忽略 (双保险)
        recalled.append({"parent": u, "child": v})
    return {"recognized": recognized, "confidence": confidence,
            "basis": basis, "recalled_edges": recalled}


def parse_direction_response(text: str, n_labels: int):
    """E3 响应解析: 复用 llm_prior._extract_json_array/_validate_prior
    (justification 字段被 _validate_prior 自然忽略, 只取 parent/child/confidence)。
    返回 (prior dict, 含 justification 的完整边列表)。"""
    items = _extract_json_array(text)  # 非法输入在此抛错
    prior = _validate_prior(items, n_labels)
    full = []
    for it in items:
        u, v = int(it["parent"]), int(it["child"])
        if u == v or (u, v) not in prior:
            continue
        full.append({"parent": u, "child": v,
                     "confidence": prior[(u, v)],
                     "justification": str(it.get("justification", ""))})
    return prior, full


def parse_contentless_response(text: str, n_labels: int) -> dict:
    """E4 响应解析: 与 _validate_prior 同规则, 但空数组为合法弃权 → 返回 {}。
    弃权本身即阴性对照结果 (无语义内容则模型无可输出)。"""
    items = _extract_json_array(text)  # 找不到 JSON 数组仍抛错 (非弃权, 是解析失败)
    if not items:
        return {}
    return _validate_prior(items, n_labels)


# ---------------------------------------------------------------- API 调用
def _post_prompt(prompt: str, key: str, parse_fn, counter: dict):
    """单次 prompt 的真实 API 调用。传输/重试/错误消毒模式复用
    llm_prior.call_llm_prior (出处: llm_prior.py §调用), 参数化了解析器。
    预算: ≤ MAX_ATTEMPTS=2 次 HTTP 尝试; counter["http_attempts"] 记实际尝试数。"""
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "max_tokens": 4000,
               "messages": [{"role": "user", "content": prompt}]}
    last_err = None
    for _attempt in range(MAX_ATTEMPTS):
        counter["http_attempts"] += 1
        try:
            resp = requests.post(ENDPOINT, headers=headers, json=payload,
                                 timeout=TIMEOUT)
            if resp.status_code != 200:
                raise RuntimeError(
                    _sanitize(f"HTTP {resp.status_code}: {resp.text[:200]}", key))
            content = resp.json()["choices"][0]["message"]["content"]
            if not content:
                raise RuntimeError("空 content 响应")
            return parse_fn(content), content
        except Exception as e:  # 网络/解析错误; 重试一次后放弃 (预算上限)
            last_err = _sanitize(f"{type(e).__name__}: {e}", key)
    raise RuntimeError(
        f"API 调用失败 ({MAX_ATTEMPTS} 次尝试, SPEC v1.8 预算上限): {last_err}")


# ---------------------------------------------------------------- E1/E2/E3
def run_e1(labels: list, key: str | None, counter: dict, force: bool):
    """E1 标签打乱阴性对照。返回 (section, mapped_prior|None)。"""
    n = len(labels)
    shuffled, perm = shuffle_labels(labels)
    prompt = build_prior_prompt(shuffled)
    sha = sha256_text(prompt)
    sec = {"spec_version": "v1.8-E1", "cache_path": CACHE_E1,
           "prompt_sha256": sha, "perm_seed": PERM_SEED,
           "status": None, "source": None, "error": None}
    cached = None if force else _load_cache_if_fresh(CACHE_E1, sha)
    if cached is not None:
        sec.update(status="ok", source="cache_reuse",
                   n_prior_edges=len(cached.get("prior", [])))
        return sec, _prior_from_entries(cached["prior"])
    if not key:
        raise RuntimeError(llm_prior.NO_KEY_MSG)
    (prior_sh, _content) = _post_prompt(
        prompt, key, lambda t: _validate_prior(_extract_json_array(t), n), counter)
    mapped = map_shuffled_prior(prior_sh, perm)
    rec = {"spec_version": "v1.8-E1", "model": MODEL, "endpoint": ENDPOINT,
           "n_labels": n, "prompt_sha256": sha, "perm_seed": PERM_SEED,
           "perm": [int(x) for x in perm],
           "prior_shuffled_space": [
               {"parent": int(u), "child": int(v), "confidence": float(c)}
               for (u, v), c in sorted(prior_sh.items())],
           "prior": [
               {"parent": int(u), "child": int(v), "confidence": float(c)}
               for (u, v), c in sorted(mapped.items())],
           "note": "E1 同模型标签打乱阴性对照: prompt 只含打乱后的标签列表; "
                   "perm 为确定性置换 (seed=188001), 完整落盘供审计, 非秘密; "
                   "API key 仅存在于运行时环境变量, 不写入本文件。"}
    _write_json(CACHE_E1, rec)
    sec.update(status="ok", source="live_api", n_prior_edges=len(mapped))
    return sec, mapped


def run_e2(labels: list, edges: list, named: set, key: str | None,
           counter: dict, force: bool):
    """E2 训练污染自陈探针。返回 (section, None) —— E2 不产出融合先验。"""
    n = len(labels)
    prompt = build_e2_prompt(labels)
    sha = sha256_text(prompt)
    sec = {"spec_version": "v1.8-E2", "cache_path": CACHE_E2,
           "prompt_sha256": sha, "status": None, "source": None, "error": None}
    cached = None if force else _load_cache_if_fresh(CACHE_E2, sha)
    if cached is not None:
        resp = cached["response"]
        sec.update(status="ok", source="cache_reuse")
    else:
        if not key:
            raise RuntimeError(llm_prior.NO_KEY_MSG)
        (resp, _content) = _post_prompt(
            prompt, key, lambda t: parse_contamination_response(t, n), counter)
        rec = {"spec_version": "v1.8-E2", "model": MODEL, "endpoint": ENDPOINT,
               "n_labels": n, "prompt_sha256": sha, "response": resp,
               "note": "E2 训练污染自陈式探针: prompt 只含标签列表; "
                       "API key 仅存在于运行时环境变量, 不写入本文件。"}
        _write_json(CACHE_E2, rec)
        sec.update(status="ok", source="live_api")
    sec["response"] = resp
    sec["overlap_analysis"] = contamination_overlap(resp["recalled_edges"],
                                                    edges, named, n)
    sec["caveat"] = "自陈式探针，仅供定性参考：recognized/回忆边均为模型自述，" \
                    "不能作为污染存在或不存在的直接证据。"
    return sec, None


def run_e3(labels: list, real_prior: dict | None, key: str | None,
           counter: dict, force: bool):
    """E3 方向显式先验稳健性。返回 (section, e3_prior|None)。"""
    n = len(labels)
    prompt = build_e3_prompt(labels)
    sha = sha256_text(prompt)
    sec = {"spec_version": "v1.8-E3", "cache_path": CACHE_E3,
           "prompt_sha256": sha, "status": None, "source": None, "error": None}
    cached = None if force else _load_cache_if_fresh(CACHE_E3, sha)
    if cached is not None:
        prior = _prior_from_entries(cached["prior"])
        sec.update(status="ok", source="cache_reuse", n_prior_edges=len(prior))
    else:
        if not key:
            raise RuntimeError(llm_prior.NO_KEY_MSG)
        (parsed, _content) = _post_prompt(
            prompt, key, lambda t: parse_direction_response(t, n), counter)
        (prior, full) = parsed  # parse_direction_response 返回 (prior, full) 二元组
        rec = {"spec_version": "v1.8-E3", "model": MODEL, "endpoint": ENDPOINT,
               "n_labels": n, "prompt_sha256": sha, "prior": full,
               "note": "E3 方向显式先验: prompt 只含标签列表 + 方向定义; "
                       "justification 仅供审计, 评分时忽略; "
                       "API key 仅存在于运行时环境变量, 不写入本文件。"}
        _write_json(CACHE_E3, rec)
        sec.update(status="ok", source="live_api", n_prior_edges=len(prior))
    if real_prior is not None:
        sec["comparison_vs_v16_prior"] = direction_compare(prior, real_prior)
    return sec, prior


def run_e4(labels: list, key: str | None, counter: dict, force: bool):
    """E4 语义摧毁阴性对照 (SPEC v1.8.1 增补)。返回 (section, prior|None)。
    无语义占位标签下模型弃权 (空数组) 为合法且信息性结果, 不视为错误。"""
    n = len(labels)
    prompt = build_e4_prompt(labels)
    sha = sha256_text(prompt)
    sec = {"spec_version": "v1.8-E4", "cache_path": CACHE_E4,
           "prompt_sha256": sha, "status": None, "source": None, "error": None}
    cached = None if force else _load_cache_if_fresh(CACHE_E4, sha)
    if cached is not None:
        entries = cached.get("prior", [])
        sec.update(status=cached.get("status") or ("ok" if entries else "abstained"),
                   source="cache_reuse", n_prior_edges=len(entries))
        return sec, (_prior_from_entries(entries) if entries else None)
    if not key:
        raise RuntimeError(llm_prior.NO_KEY_MSG)
    (prior, _content) = _post_prompt(
        prompt, key, lambda t: parse_contentless_response(t, n), counter)
    status = "ok" if prior else "abstained"
    rec = {"spec_version": "v1.8-E4", "model": MODEL, "endpoint": ENDPOINT,
           "n_labels": n, "prompt_sha256": sha, "status": status,
           "prior": [{"parent": int(u), "child": int(v), "confidence": float(c)}
                     for (u, v), c in sorted(prior.items())],
           "note": "E4 语义摧毁阴性对照 (SPEC v1.8.1): prompt 只含无语义占位标签 "
                   "item_XX; 弃权(空数组)为合法结果; 占位索引与原节点一一对应无需映射; "
                   "API key 仅存在于运行时环境变量, 不写入本文件。"}
    _write_json(CACHE_E4, rec)
    sec.update(status=status, source="live_api", n_prior_edges=len(prior))
    return sec, (prior if prior else None)


# ---------------------------------------------------------------- 定量分析
def contamination_overlap(recalled: list, edges: list, named: set, n: int) -> dict:
    """E2: recalled_edges 与金边 (全 49 / named 17) 的重叠 vs 随机机会期望。
    机会期望: 从 N(N-1) 个有向对中无放回抽 k 条, 期望重叠 = k·|G|/(N(N-1))。"""
    gold = {tuple(e) for e in edges}
    rec = {(int(it["parent"]), int(it["child"])) for it in recalled}
    k = len(rec)
    universe = n * (n - 1)
    exp_gold = k * len(gold) / universe
    exp_named = k * len(named) / universe
    ov_gold = len(rec & gold)
    ov_named = len(rec & named)
    return {"n_recalled": k, "universe_directed_pairs": universe,
            "overlap_gold49": ov_gold,
            "expected_gold_chance": round(exp_gold, 4),
            "gold_chance_ratio": (round(ov_gold / exp_gold, 3) if exp_gold > 0 else None),
            "overlap_named17": ov_named,
            "expected_named_chance": round(exp_named, 4),
            "named_chance_ratio": (round(ov_named / exp_named, 3) if exp_named > 0 else None),
            "preregistered_alarm_rule": f"recognized=true 且 overlap ≥ {CHANCE_RATIO}×机会期望 → 污染警示增强; 否则作弱反证"}


def direction_compare(e3_prior: dict, real_prior: dict) -> dict:
    """E3 与 v1.6 先验 (9 边) 比较: 无向 Jaccard + 共有边的方向一致率。"""
    a_dir = {(u, v) for (u, v) in e3_prior}
    b_dir = {(u, v) for (u, v) in real_prior}
    a_u = {frozenset(p) for p in a_dir}
    b_u = {frozenset(p) for p in b_dir}
    inter = a_u & b_u
    union = a_u | b_u
    agree = sum(1 for fs in inter
                if (tuple(sorted(fs)) in a_dir) == (tuple(sorted(fs)) in b_dir))
    return {"n_e3_edges": len(a_dir), "n_v16_edges": len(b_dir),
            "undirected_jaccard": (round(len(inter) / len(union), 4) if union else 0.0),
            "shared_undirected_pairs": len(inter),
            "direction_agreement": (round(agree / len(inter), 4) if inter else None),
            "note": "方向一致率 = 共有无向对中方向相同的比例; None=无共有对"}


# ---------------------------------------------------------------- 留一评分
def score_loo(cfg: DiffusionConfig, priors: dict) -> dict:
    """对若干先验变体跑 v1.7.1 同口径留一评分。
    协议逐行对齐 run_v17_fusion_fix.main: 同图/同种子 70000+ei/同 N_NEG=10/
    同行负采样池/top-3; base 臂 field_guided→random→degree 同顺序消耗 rng,
    再取 tiebreak —— real 先验臂数字与 v1.7.1 逐位一致 (有测试回归)。
    每先验变体报告: prior-only, hybrid_norm@λ, hybrid_raw@λ (λ∈{0.5,2.0})。"""
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    named = {tuple(e) for e in meta["path_edges_named"]}
    pmats = {tag: prior_score_matrix(p, (N, N)) for tag, p in priors.items()}
    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)  # 与 v1.6/v1.7.1 完全一致
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = np.zeros((N, N), bool); mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        rec = {"edge": [int(u), int(v)], "on_named_path": (u, v) in named,
               "arms": {}}
        # base 臂: 与 v1.7.1 同顺序 (rng 消耗顺序一致 → tiebreak 流逐位一致)
        scores = {a: arm_scores(a, W_obs, mask, cfg, 0, 1, adj_obs, rng,
                                inst_seed=70_000 + ei)
                  for a in ("field_guided", "random", "degree")}
        tiebreak = rng.random(int(mask.sum()))
        for tag, P in pmats.items():
            scores[f"{tag}_prior"] = prior_only(P, mask, tiebreak)
            for lam in LAMBDAS_V18:
                scores[f"{tag}_hybrid_norm@{lam}"] = norm_hybrid(
                    scores["field_guided"], P, mask, lam, tiebreak)
                scores[f"{tag}_hybrid_raw@{lam}"] = raw_hybrid(
                    scores["field_guided"], P, mask, lam)
        for a, s in scores.items():
            hit = top3_hit_per_edge(s, [(u, v)], mask)[0]
            rec["arms"][a] = {"rank": hit["rank"], "hit": hit["hit"]}
        per_edge.append(rec)

    def xs(arm, named_only=None):
        return [float(r["arms"][arm]["hit"]) for r in per_edge
                if named_only is None or (named_only and r["on_named_path"])
                or (named_only is False and not r["on_named_path"])]
    arms = {}
    for a in scores.keys():
        arms[a] = {"top3_hit": mean_std(xs(a)),
                   "top3_hit_named_path": mean_std(xs(a, True)),
                   "top3_hit_filler": mean_std(xs(a, False))}
    return {"arms": arms, "per_edge": per_edge,
            "denominators": {"overall": len(edges), "named": len(named),
                             "filler": len(edges) - len(named)},
            "protocol": "同 v1.7.1: 同图/同种子70000+ei/同N_NEG=10/同行负采样池/"
                        "top-3; hybrid_norm=min-max归一融合+1e-6 tiebreak"}


# ---------------------------------------------------------------- 判定 (预登记口径)
def _v171_references() -> dict:
    """从 v1.7.1 结果只读提取参考水平; 缺失时回退到预登记常量。"""
    refs = {"null_hybrid_norm05_named": 0.17647058823529413,
            "real_hybrid_norm05_named": 0.29411764705882354,
            "null_prioronly_named": 0.11764705882352941,
            "real_prioronly_named": 0.23529411764705882,
            "v171_hybrid_norm2_named": 0.47058823529411764,
            "source": "preregistered_constants_fallback"}
    if os.path.exists(V171_PATH):
        with open(V171_PATH, "r", encoding="utf-8") as f:
            arms = json.load(f)["experiment_B"]["arms"]
        rs = [arms[f"hybrid_norm_rand{s}@0.5"]["top3_hit_named_path"]["mean"]
              for s in range(5)]
        rp = [arms[f"llm_prior_rand{s}"]["top3_hit_named_path"]["mean"]
              for s in range(5)]
        refs.update(
            null_hybrid_norm05_named=float(np.mean(rs)),
            real_hybrid_norm05_named=arms["hybrid_norm@0.5"]["top3_hit_named_path"]["mean"],
            null_prioronly_named=float(np.mean(rp)),
            real_prioronly_named=arms["llm_prior"]["top3_hit_named_path"]["mean"],
            v171_hybrid_norm2_named=arms["hybrid_norm@2.0"]["top3_hit_named_path"]["mean"],
            source="results/deposon_v17_fusion_fix.json (read-only)")
    return refs


def verdict_e1(e1_sec: dict) -> dict:
    """E1 重解读 (SPEC v1.8.1): 原预登记口径「E1≈null 且低于 real」基于错误假设——
    以为打乱标签索引可摧毁语义。实际上置换对语义推理透明 (LLM 读标签内容而非
    索引位置), 逆映射必然还原语义边, 故 E1 不构成语义阴性对照 (设计缺陷, 如实披露;
    语义阴性对照由 E4 承担)。E1 的实际信息量为置换不变性检验:
    映射后边集与 real 先验一致 ⇔ 先验是标签语义的函数, 而非索引位置的函数。"""
    if e1_sec.get("status") != "ok":
        return {"status": "pending", "reason": "E1 先验缺失 (无缓存且无 key)"}
    out = {"status": "evaluated",
           "original_rule_voided": ("原预登记判定口径作废: 其假设「索引置换摧毁语义」"
                                    "不成立 (置换对语义推理透明); 该缺陷于 SPEC v1.8.1 "
                                    "披露并修正, 语义阴性对照改由 E4 承担。"),
           "design_flaw_disclosed": True}
    inv = e1_sec.get("permutation_invariance")
    if inv:
        identical = bool(inv["edge_set_identical"])
        out.update(inv)
        out["permutation_invariant"] = identical
        out["statement"] = (
            "E1 映射后边集与 real 先验完全一致 → 先验对节点索引置换不变, "
            "语义由标签内容携带 (置换不变性检验通过); E1 非语义阴性对照, 见 E4。"
            if identical else
            "E1 映射后边集与 real 先验不一致 → 先验含索引位置依赖成分, 如实报告。")
    return out


def verdict_e4(fusion: dict | None, e4_sec: dict, refs: dict) -> dict:
    """E4 语义摧毁阴性对照 (SPEC v1.8.1 增补, 预登记):
    - 弃权 (0 边) → 无语义内容时模型无法产出任何先验, 为最强形式的支持;
    - 非空 → hybrid_norm@0.5 named ≈ synthetic null (±NULL_TOL) 且低于 real
      同臂 ≥ REAL_GAP → 支持「先验携带语义而非形式 artifact」; 否则主张被削弱,
      如实报告。"""
    st = e4_sec.get("status")
    if st == "abstained":
        return {"status": "evaluated", "mode": "abstention",
                "supports_semantic_claim": True,
                "statement": ("E4: 无语义占位标签下模型弃权 (0 边) → 先验信号依赖语义"
                              "内容, 支持语义性主张 (最强形式的阴性对照)")}
    if st != "ok" or fusion is None or "E4_hybrid_norm@0.5" not in fusion["arms"]:
        return {"status": "pending", "reason": "E4 先验缺失 (无缓存且无 key)"}
    e4 = fusion["arms"]["E4_hybrid_norm@0.5"]["top3_hit_named_path"]["mean"]
    real = fusion["arms"]["real_hybrid_norm@0.5"]["top3_hit_named_path"]["mean"]
    null = refs["null_hybrid_norm05_named"]
    near_null = abs(e4 - null) <= NULL_TOL
    below_real = (real - e4) >= REAL_GAP
    supports = bool(near_null and below_real)
    return {"status": "evaluated", "mode": "nonempty_prior",
            "e4_n_edges": e4_sec.get("n_prior_edges"),
            "e4_hybrid_norm05_named": e4,
            "synthetic_null_hybrid_norm05_named": null,
            "real_hybrid_norm05_named": real,
            "near_null_within_tol": near_null, "null_tol": NULL_TOL,
            "below_real_by_gap": below_real, "real_gap": REAL_GAP,
            "supports_semantic_claim": supports,
            "statement": ("E4 非空先验 named 处于 null 水平且明显低于 real → "
                          "支持语义性主张" if supports else
                          "E4 非空先验 named 未同时满足「≈null 且低于 real」→ "
                          "语义性主张被削弱, 如实报告")}


def verdict_e2(e2_sec: dict) -> dict:
    ov = e2_sec.get("overlap_analysis")
    resp = e2_sec.get("response")
    if not ov or not resp:
        return {"status": "pending"}
    ratio = ov["gold_chance_ratio"]
    alarm = bool(resp["recognized"] and ratio is not None and ratio >= CHANCE_RATIO)
    return {"status": "evaluated", "recognized": resp["recognized"],
            "gold_chance_ratio": ratio, "alarm_rule_multiplier": CHANCE_RATIO,
            "contamination_alarm": alarm,
            "statement": ("recognized=true 且重叠显著超机会 → 污染警示增强" if alarm else
                          "未同时满足 recognized=true 与重叠显著超机会 → 弱反证"),
            "caveat": "自陈式探针，仅供定性参考，不能作为污染的直接证据。"}


def verdict_e3(fusion: dict | None, e3_sec: dict, refs: dict) -> dict:
    """预登记: E3 hybrid_norm@2 named 与 v1.7.1 hybrid_norm@2 (0.471) 同方向且
    不更差超过 E3_TOL=0.12 → named 结果对 prompt 措辞稳健; 方向一致率低则
    如实报告「方向定义敏感」。"""
    if fusion is None or "E3_hybrid_norm@2.0" not in fusion["arms"]:
        return {"status": "pending", "reason": "E3 先验缺失 (无缓存且无 key)"}
    ref = refs["v171_hybrid_norm2_named"]
    e3 = fusion["arms"]["E3_hybrid_norm@2.0"]["top3_hit_named_path"]["mean"]
    robust = bool(e3 >= ref - E3_TOL)
    out = {"status": "evaluated", "e3_hybrid_norm2_named": e3,
           "v171_hybrid_norm2_named": ref, "tolerance": E3_TOL,
           "robust_to_prompt_wording": robust,
           "statement": ("E3 融合 named 与 0.471 同方向且不更差超过容差 → "
                         "named 结果对 prompt 措辞稳健" if robust else
                         "E3 融合 named 低于 0.471 超过容差 → 结果对 prompt 措辞敏感，"
                         "如实报告")}
    cmp16 = e3_sec.get("comparison_vs_v16_prior")
    if cmp16:
        out["comparison_vs_v16_prior"] = cmp16
        da = cmp16["direction_agreement"]
        if da is not None and da < 0.5:
            out["direction_sensitivity_note"] = (
                f"共有边方向一致率仅 {da} → 方向定义敏感，如实报告")
    return out


# ---------------------------------------------------------------- dry-run / main
def dry_run(labels: list, selected: tuple) -> int:
    """构造全部选中 prompt, 打印完整文本与 sha256、预算; 不读 key、不发请求。"""
    prompts = build_all_prompts(labels)
    print("=" * 70)
    print("v1.8 DRY-RUN: 仅构造 prompt 并展示; 未读取 KIMI_API_KEY, 未发送任何请求。")
    print(f"预算: 每个 prompt ≤ MAX_ATTEMPTS={MAX_ATTEMPTS} 次 HTTP 尝试; "
          f"model={MODEL}; endpoint={ENDPOINT}")
    print("=" * 70)
    for tag in selected:
        p = prompts[tag]
        cache = {"E1": CACHE_E1, "E2": CACHE_E2, "E3": CACHE_E3,
                 "E4": CACHE_E4}[tag]
        sha = sha256_text(p)
        fresh = _load_cache_if_fresh(cache, sha) is not None
        expect = 0 if fresh else MAX_ATTEMPTS
        print(f"\n----- {tag} prompt ({len(p)} chars) -----")
        print(f"sha256: {sha}")
        print(f"cache: {cache}  fresh_cache={fresh}  "
              f"预计 HTTP 尝试上限={expect} 次")
        print("----- prompt 全文 -----")
        print(p)
    total = sum(0 if _load_cache_if_fresh(
        {"E1": CACHE_E1, "E2": CACHE_E2, "E3": CACHE_E3, "E4": CACHE_E4}[t],
        sha256_text(prompts[t])) is not None else MAX_ATTEMPTS for t in selected)
    print("\n" + "=" * 70)
    print(f"合计 HTTP 尝试预算上限 ({'+'.join(selected)}): ≤ {total} 次 "
          f"(缓存新鲜则为 0); dry-run 实际发起 0 次。")
    print("=" * 70)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Deposon v1.8 API 补实验 (SPEC v1.8)")
    ap.add_argument("--dry-run", action="store_true",
                    help="只构造/打印 prompt 与预算, 不读 key 不发请求")
    ap.add_argument("--only", default=",".join(EXPERIMENTS),
                    help="实验子集, 逗号分隔, 如 E1,E3")
    ap.add_argument("--force", action="store_true",
                    help="忽略新鲜缓存强制重调 API")
    args = ap.parse_args(argv)
    selected = tuple(t.strip() for t in args.only.split(",") if t.strip())
    bad = [t for t in selected if t not in EXPERIMENTS]
    if bad:
        ap.error(f"--only 含未知实验: {bad}; 可选 {EXPERIMENTS}")

    t0 = time.time()
    cfg = DiffusionConfig()
    N, adj, edges, labels, meta = reconstruct_mindmap()
    named = {tuple(e) for e in meta["path_edges_named"]}

    if args.dry_run:
        return dry_run(labels, selected)

    # key 仅此一处读取; 不打印、不落盘; 错误文本一律 _sanitize
    key = os.environ.get("KIMI_API_KEY")
    counter = {"http_attempts": 0}

    # real 先验 (v1.6 缓存, 只读)
    real_prior, real_err = None, None
    if os.path.exists(CACHE_V16):
        real_prior = load_prior(CACHE_V16)
    else:
        real_err = "results/llm_prior_cache.json missing"

    priors = {}
    if real_prior is not None:
        priors["real"] = real_prior
    exp_secs = {}
    for tag in selected:
        try:
            if tag == "E1":
                sec, p = run_e1(labels, key, counter, args.force)
                if p is not None:
                    priors["E1"] = p
            elif tag == "E2":
                sec, _ = run_e2(labels, edges, named, key, counter, args.force)
            elif tag == "E3":
                sec, p = run_e3(labels, real_prior, key, counter, args.force)
                if p is not None:
                    priors["E3"] = p
            else:
                sec, p = run_e4(labels, key, counter, args.force)
                if p is not None:
                    priors["E4"] = p
            exp_secs[tag] = sec
        except Exception as e:  # 单实验失败不阻断其余; 错误经 _sanitize
            exp_secs[tag] = {"spec_version": f"v1.8-{tag}",
                             "status": "error", "source": None,
                             "error": _sanitize(f"{type(e).__name__}: {e}",
                                                key or "")}

    # E1 置换不变性量化 (SPEC v1.8.1): 映射后边集 vs real 先验边集 + 共有边置信度相关
    if "E1" in priors and real_prior is not None and "E1" in exp_secs:
        e1_edges, real_edges = set(priors["E1"]), set(real_prior)
        common = sorted(e1_edges & real_edges)
        pearson = None
        if len(common) > 1:
            a = np.array([priors["E1"][e] for e in common])
            b = np.array([real_prior[e] for e in common])
            if a.std() > 0 and b.std() > 0:
                pearson = round(float(np.corrcoef(a, b)[0, 1]), 4)
        exp_secs["E1"]["permutation_invariance"] = {
            "e1_n_edges": len(e1_edges), "real_n_edges": len(real_edges),
            "shared_edges": len(common),
            "edge_set_identical": e1_edges == real_edges,
            "confidence_pearson_on_shared": pearson,
            "note": "E1 实测量为置换不变性: 索引置换对语义推理透明, 映射后边集一致 "
                    "⇔ 先验是标签语义的函数而非索引位置的函数; E1 不构成语义阴性对照 "
                    "(设计缺陷, SPEC v1.8.1 披露), 语义阴性对照由 E4 承担。"}

    # 融合评分 (零 API; 任何可用先验都跑; real 先验臂应与 v1.7.1 逐位一致)
    fusion = score_loo(cfg, priors) if priors else None
    refs = _v171_references()
    verdicts = {"E1": verdict_e1(exp_secs.get("E1", {})) if "E1" in selected else {"status": "skipped"},
                "E3": verdict_e3(fusion, exp_secs.get("E3", {}), refs) if "E3" in selected else {"status": "skipped"},
                "E4": verdict_e4(fusion, exp_secs.get("E4", {}), refs) if "E4" in selected else {"status": "skipped"}}
    if "E2" in selected:
        verdicts["E2"] = verdict_e2(exp_secs.get("E2", {}))

    prompts = build_all_prompts(labels)
    out = {
        "experiment": "deposon_v18_api_supplements",
        "spec": ("SPEC v1.8.1 (API 补实验: E1 置换不变性/E2 污染探针/E3 方向稳健性/"
                 "E4 语义摧毁阴性对照; v1.8.1 修正: E1 原阴性对照口径作废, 增补 E4)"),
        "spec_version": "v1.8.1",
        "config": config_dict(cfg),
        "api": {"model": MODEL, "endpoint": ENDPOINT,
                "max_attempts_per_prompt": MAX_ATTEMPTS,
                "prompt_budget": len(selected),
                "total_http_attempts_actual": counter["http_attempts"],
                "prompts": {t: {"sha256": sha256_text(prompts[t]),
                                "n_chars": len(prompts[t])} for t in selected}},
        "references_v171": refs,
        "real_prior": {"cache_path": CACHE_V16, "read_only": True,
                       "n_prior_edges": len(real_prior) if real_prior else 0,
                       "error": real_err},
        "experiments": exp_secs,
        "fusion": fusion,
        "verdicts": verdicts,
        "runtime_sec": round(time.time() - t0, 3),
        "honesty": [
            "零泄漏: 四个 prompt 只含节点标签列表 (E4 为无语义占位标签); E1 打乱只对"
            "标签顺序操作 (确定性置换 seed=188001, perm 完整落盘供审计)。",
            "SPEC v1.8.1 修正披露: E1 原预登记口径「打乱索引可摧毁语义」不成立 "
            "(置换对语义推理透明), E1 重定位为置换不变性检验; 语义阴性对照由 E4 "
            "(无语义占位标签) 承担, 判定口径沿用原 E1 (NULL_TOL/REAL_GAP)。",
            "E3 首轮实跑曾遇脚本解包 bug (parse_direction_response 二元组被二次包装), "
            "API 响应本身正常; 正式缓存由首轮真实响应离线解析恢复, 未产生额外 API 调用, "
            "畸形原始记录归档于 llm_prior_cache_v18_direction_run1_malformed_archive.json。",
            "API key 仅从环境变量 KIMI_API_KEY 读取, 不写入任何文件/日志/异常; "
            "错误文本经 llm_prior._sanitize 兜底剔除; 严禁 mock 冒充真实调用。",
            f"API 预算 ≤ {len(selected)} prompt × MAX_ATTEMPTS={MAX_ATTEMPTS}; "
            f"本次实际 HTTP 尝试 {counter['http_attempts']} 次; 缓存新鲜时 0 次 (幂等重跑)。",
            "E2 为自陈式探针, 结论仅供定性参考; 所有结果 (含负面) 如实报告。",
            "留一评分与 v1.7.1 完全同协议 (同图/同种子/同负采样/top-3); "
            "real 先验臂数字应逐位复现 v1.7.1 (tests/test_v18.py 有回归断言)。",
            "判定口径 (NULL_TOL/REAL_GAP/E3_TOL/CHANCE_RATIO) 预登记于 SPEC v1.8, "
            "判定为机械规则求值, 不替代人工解读。"]}
    _write_json(OUT_PATH, out)
    print(f"written {OUT_PATH}  runtime={out['runtime_sec']}s  "
          f"http_attempts={counter['http_attempts']}")
    if fusion:
        for a, b in fusion["arms"].items():
            print(f"  {a:24s} top3={b['top3_hit']['mean']:.3f} "
                  f"named={b['top3_hit_named_path']['mean']:.3f} "
                  f"filler={b['top3_hit_filler']['mean']:.3f}")
    print(json.dumps({k: v.get("statement", v.get("status"))
                      for k, v in verdicts.items()}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
