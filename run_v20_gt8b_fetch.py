# -*- coding: utf-8 -*-
# GT-8b「领域鉴定器 v0」real_semantics 轴 API 获取（docs/SPEC_GT8B.md §4，
# 主代理执行）：2 新真实语义域
#   A) 图生成 prompt（逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE，只换域）
#      → results/gt8b_cache/{domain}.json
#   B) 先验臂 prompt（llm_prior.build_prior_prompt，labels-only 零泄漏）
#      → results/gt8b_cache/prior_{domain}.json
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；错误经 llm_prior._sanitize。
# 预算（SPEC_GT8B §4 预登记）: 4 prompt × MAX_ATTEMPTS=2 → 总 HTTP ≤ 8；
# 缓存新鲜(prompt_sha256 一致)则跳过；超时/失败如实记 fetch_failed。
# B 阶段依赖 A 阶段缓存中的标签：A 缓存缺失/失效 → 该域先验挂起并清晰报告，
# 绝不伪造标签（与 run_v20_crossval_fetch.py 同一纪律）。
import hashlib
import json
import os

import requests

import llm_prior
from llm_prior import (ENDPOINT, MAX_ATTEMPTS, MODEL, TIMEOUT, _sanitize,
                       build_prior_prompt)
from mindmap_corpus_v20 import (_PROMPT_TEMPLATE, CacheMissingError,
                                parse_familyL_response)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
CACHE_DIR = os.path.join(RESULTS, "gt8b_cache")

# ------------------------------------------------- SPEC_GT8B §2 冻结常量
GT8B_DOMAINS = ("chemical_elements", "chinese_dynasties")
GT8B_DOMAIN_BRIEF = {
    "chemical_elements": (
        "化学元素与周期律（抽象→具体：从「化学元素」逐层细化到周期/族/"
        "具体元素，方向语义 = 类别指向其成员）"),
    "chinese_dynasties": (
        "中国历史朝代（过程→结果：从早期朝代经关键制度/事件指向后继朝代"
        "与影响，方向语义 = 前朝/原因指向后继/结果）"),
}


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def build_gt8b_prompts() -> dict:
    """按 SPEC_GT8B §2 生成 2 个新域的建图 prompt（不执行 API）。
    模板逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE（与族 L 同款，只换域）。"""
    return {d: _PROMPT_TEMPLATE.format(domain=d, brief=GT8B_DOMAIN_BRIEF[d])
            for d in GT8B_DOMAINS}


def gt8b_prompt_manifest() -> dict:
    """{domain: {"prompt_sha256": ...}}；prompt_sha256 落盘纪律。"""
    return {d: {"prompt_sha256": sha(p)}
            for d, p in build_gt8b_prompts().items()}


def fresh(path, s):
    if not os.path.exists(path):
        return False
    try:
        rec = json.load(open(path, encoding="utf-8"))
    except Exception:
        return False
    return rec.get("prompt_sha256") == s and bool(rec.get("response_text"))


def post(prompt, key, counter):
    """单 prompt 调用，≤ MAX_ATTEMPTS 次尝试；失败抛 RuntimeError（已 sanitize）。"""
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "max_tokens": 8000,
               "messages": [{"role": "user", "content": prompt}]}
    last = None
    for _ in range(MAX_ATTEMPTS):
        counter["n"] += 1
        try:
            r = requests.post(ENDPOINT, headers=headers, json=payload,
                              timeout=TIMEOUT)
            if r.status_code != 200:
                raise RuntimeError(
                    _sanitize(f"HTTP {r.status_code}: {r.text[:200]}", key))
            c = r.json()["choices"][0]["message"]["content"]
            if c:
                return c
        except Exception as e:
            last = _sanitize(f"{type(e).__name__}: {e}", key)
    raise RuntimeError(f"API failed after {MAX_ATTEMPTS} attempts: {last}")


def load_labels_from_graph_cache(domain):
    """A 阶段缓存 → 校验后的标签列表；缓存缺失/失效 → CacheMissingError。"""
    path = os.path.join(CACHE_DIR, f"{domain}.json")
    manifest = gt8b_prompt_manifest()
    if not fresh(path, manifest[domain]["prompt_sha256"]):
        raise CacheMissingError(
            f"GT-8b graph cache missing/stale: {path} — 先验臂 prompt 需要"
            "已摄入图的标签；请先完成 A 阶段图生成 fetch。绝不伪造标签。")
    rec = json.load(open(path, encoding="utf-8"))
    return parse_familyL_response(rec["response_text"])["nodes"]


def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(CACHE_DIR, exist_ok=True)
    counter = {"n": 0}
    manifest = gt8b_prompt_manifest()
    fetch_failed = {}
    # ---- A) 图生成（每域 1 prompt）
    for domain, prompt in build_gt8b_prompts().items():
        path = os.path.join(CACHE_DIR, f"{domain}.json")
        if fresh(path, manifest[domain]["prompt_sha256"]):
            print(f"{domain} graph: fresh cache")
            continue
        try:
            c = post(prompt, key, counter)
        except RuntimeError as e:
            fetch_failed[f"{domain}.graph"] = str(e)
            print(f"{domain} graph: FETCH_FAILED ({e})")
            continue
        json.dump({"domain": domain, "kind": "gt8b_graph_gen",
                   "prompt_sha256": manifest[domain]["prompt_sha256"],
                   "model": MODEL, "response_text": c,
                   "note": "SPEC_GT8B §2 冻结域; key 仅在运行时环境变量"},
                  open(path, "w", encoding="utf-8"), ensure_ascii=False,
                  indent=1)
        print(f"{domain} graph: cached {len(c)} chars")
    # ---- B) 先验臂（每域 1 prompt，labels-only 零泄漏）
    for domain in GT8B_DOMAINS:
        path = os.path.join(CACHE_DIR, f"prior_{domain}.json")
        try:
            labels = load_labels_from_graph_cache(domain)
        except CacheMissingError as e:
            fetch_failed[f"{domain}.prior"] = str(e)
            print(f"{domain} prior: DEFERRED ({e})")
            continue
        p = build_prior_prompt(labels)
        s = sha(p)
        if fresh(path, s):
            print(f"{domain} prior: fresh cache")
            continue
        try:
            c = post(p, key, counter)
        except RuntimeError as e:
            fetch_failed[f"{domain}.prior"] = str(e)
            print(f"{domain} prior: FETCH_FAILED ({e})")
            continue
        json.dump({"domain": domain, "kind": "labels_only_prior",
                   "prompt_sha256": s, "model": MODEL, "response_text": c,
                   "note": "零泄漏: prompt 只含标签列表; key 仅在运行时环境变量"},
                  open(path, "w", encoding="utf-8"), ensure_ascii=False,
                  indent=1)
        print(f"{domain} prior: cached {len(c)} chars")
    print(f"total_http_attempts={counter['n']} "
          f"(budget <= {4 * MAX_ATTEMPTS}, SPEC_GT8B §4)")
    if fetch_failed:
        print("fetch_failed: " + json.dumps(fetch_failed, ensure_ascii=False))


if __name__ == "__main__":
    main()
