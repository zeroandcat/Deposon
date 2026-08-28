# -*- coding: utf-8 -*-
# Deposon v2.0 族 L 摄入（docs/SPEC_v2.0.md §1 族 L / §5 工程纪律）
#   读缓存 JSON → parse_familyL_response 校验 → 转 corpus/v20 图格式。
#   本脚本不发起任何 LLM 调用（no LLM API calls issued）：缓存缺失 →
#   CacheMissingError 显式报错，绝不伪造数据。缓存幂等（同缓存 ⇒ 同图 JSON）。
#
# 缓存格式（由主代理在调用 API 后落盘）：
#   results/familyL_cache/{domain}.json =
#     {"domain": "physics_concepts", "attempt": 1,
#      "prompt_sha256": "<build_familyL_prompts 对应哈希>",
#      "model": "<生成模型名>", "response_text": "<LLM 原始响应>"}
import hashlib
import json
import os

from mindmap_corpus_v20 import (CORPUS_DIR, FAMILY_L_DOMAINS, STRUCTURE_NAMES,
                                CacheMissingError, _canonical_sha256,
                                build_index, familyL_prompt_manifest,
                                longest_path_family, parse_familyL_response)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
CACHE_DIR = os.path.join(RESULTS, "familyL_cache")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_familyL_ingest.json")


def cache_path_for(domain: str, cache_dir: str = CACHE_DIR) -> str:
    return os.path.join(cache_dir, f"{domain}.json")


def ingest_domain(domain: str, cache_dir: str = CACHE_DIR,
                  corpus_dir: str = CORPUS_DIR) -> dict:
    """单域摄入：缓存 → 校验 → corpus/v20/L_{domain}.json。返回图记录。"""
    if domain not in FAMILY_L_DOMAINS:
        raise ValueError(f"unknown family L domain: {domain}")
    path = cache_path_for(domain, cache_dir)
    if not os.path.exists(path):
        raise CacheMissingError(
            f"family L cache missing: {path} — API 调用由主代理另行执行；"
            "no LLM API calls issued by this script, 绝不伪造数据。")
    with open(path, encoding="utf-8") as f:
        cache = json.load(f)
    for key in ("domain", "prompt_sha256", "response_text"):
        if key not in cache:
            raise CacheMissingError(f"cache {path} missing key '{key}'")
    if cache["domain"] != domain:
        raise CacheMissingError(
            f"cache domain mismatch: file={domain}.json domain={cache['domain']}")
    expected_sha = familyL_prompt_manifest()[domain]["prompt_sha256"]
    prompt_sha_ok = bool(cache["prompt_sha256"] == expected_sha)

    parsed = parse_familyL_response(cache["response_text"])
    nodes, edges = parsed["nodes"], parsed["edges"]
    N = len(nodes)
    edge_tuples = [tuple(e) for e in edges]
    named, _L, start, end = longest_path_family(N, edge_tuples)
    # 族 L 同样按冻结口径划 named/filler（DAG 最长路径族=named，其余=filler）
    filler = sorted(set(edge_tuples) - named)
    seed = int(hashlib.sha256(
        cache["response_text"].encode("utf-8")).hexdigest()[:8], 16) % (2 ** 31)
    rec = {"graph_id": f"L_{domain}", "family": "L",
           "structure": STRUCTURE_NAMES["L"], "N": N,
           "nodes": list(range(N)), "labels": list(nodes),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in sorted(named)],
           "filler_edges": [list(e) for e in filler],
           "source": int(start), "target": int(end), "seed": seed,
           "generator_version": "v2.0.0-familyL-ingest",
           "provenance": {
               "cache_path": path,
               "cache_sha256": hashlib.sha256(
                   json.dumps(cache, ensure_ascii=False, sort_keys=True)
                   .encode("utf-8")).hexdigest(),
               "prompt_sha256": cache["prompt_sha256"],
               "prompt_sha256_matches_preregistered": prompt_sha_ok,
               "model": cache.get("model"),
               "same_source_contamination": (
                   "先验臂与生成臂同模型族 ⇒ 同源污染风险（SPEC §1 声明）"),
               "named_filler_rule": "DAG 最长路径族=named，其余=filler（冻结口径）"}}
    rec["sha256"] = _canonical_sha256(rec)
    os.makedirs(corpus_dir, exist_ok=True)
    with open(os.path.join(corpus_dir, f"L_{domain}.json"), "w",
              encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    return rec


def main():
    ingested, errors = [], {}
    for domain in FAMILY_L_DOMAINS:
        try:
            rec = ingest_domain(domain)
            ingested.append({"graph_id": rec["graph_id"], "N": rec["N"],
                             "n_edges": len(rec["edges"]),
                             "n_named": len(rec["named_edges"]),
                             "sha256": rec["sha256"]})
        except CacheMissingError as e:
            errors[domain] = str(e)
    idx = build_index(CORPUS_DIR) if ingested else None
    out = {"experiment": "deposon_v20_familyL_ingest", "spec_version": "v2.0",
           "spec": "docs/SPEC_v2.0.md §1 族 L / §5",
           "ingested": ingested, "cache_errors": errors,
           "corpus_n_graphs": idx["n_graphs"] if idx else None,
           "honesty": [
               "no LLM API calls issued: 本脚本只读 results/familyL_cache/；"
               "缓存缺失域显式报错（CacheMissingError），绝不伪造数据。",
               "族 L 图 named/filler 按冻结口径（DAG 最长路径族）划分；"
               "prompt_sha256 与预登记 manifest 不一致时如实标记，不阻断摄入。",
               "同源污染风险：生成臂与（后续）先验臂同模型族（SPEC §1 声明）。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if errors and not ingested:
        raise CacheMissingError(
            f"no family L caches ingested: {sorted(errors)}")


if __name__ == "__main__":
    main()
