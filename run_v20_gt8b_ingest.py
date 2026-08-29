# -*- coding: utf-8 -*-
# GT-8b 新真实语义域图摄入（docs/SPEC_GT8B.md §3）：
#   读 results/gt8b_cache/{domain}.json → parse_familyL_response 校验 →
#   图 JSON 写入 results/gt8b_cache/graphs/L_{domain}.json（独立目录，
#   不污染 corpus/v20，不进既有语料索引）。
#   本脚本不发起任何 LLM 调用（no LLM API calls issued）：缓存缺失 →
#   CacheMissingError 显式报错并列出缺失文件，绝不伪造数据。
import hashlib
import json
import os

from mindmap_corpus_v20 import (STRUCTURE_NAMES, CacheMissingError,
                                _canonical_sha256, longest_path_family,
                                parse_familyL_response)
from run_v20_gt8b_fetch import (CACHE_DIR, GT8B_DOMAINS,
                                gt8b_prompt_manifest)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
GRAPH_DIR = os.path.join(CACHE_DIR, "graphs")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt8b_ingest.json")


def graph_path_for(domain: str, graph_dir: str = GRAPH_DIR) -> str:
    return os.path.join(graph_dir, f"L_{domain}.json")


def ingest_domain(domain: str, cache_dir: str = CACHE_DIR,
                  graph_dir: str = GRAPH_DIR) -> dict:
    """单域摄入：缓存 → 校验 → graph_dir/L_{domain}.json。返回图记录。"""
    if domain not in GT8B_DOMAINS:
        raise ValueError(f"unknown GT-8b domain: {domain}")
    path = os.path.join(cache_dir, f"{domain}.json")
    if not os.path.exists(path):
        raise CacheMissingError(
            f"GT-8b cache missing: {path} — API 调用由主代理另行执行"
            "（run_v20_gt8b_fetch.py）；no LLM API calls issued by this "
            "script, 绝不伪造数据。")
    with open(path, encoding="utf-8") as f:
        cache = json.load(f)
    for key in ("domain", "prompt_sha256", "response_text"):
        if key not in cache:
            raise CacheMissingError(f"cache {path} missing key '{key}'")
    if cache["domain"] != domain:
        raise CacheMissingError(
            f"cache domain mismatch: file={domain}.json domain={cache['domain']}")
    expected_sha = gt8b_prompt_manifest()[domain]["prompt_sha256"]
    prompt_sha_ok = bool(cache["prompt_sha256"] == expected_sha)

    parsed = parse_familyL_response(cache["response_text"])
    nodes, edges = parsed["nodes"], parsed["edges"]
    N = len(nodes)
    edge_tuples = [tuple(e) for e in edges]
    named, _L, start, end = longest_path_family(N, edge_tuples)
    # 族 L 冻结口径：DAG 最长路径族=named，其余=filler
    filler = sorted(set(edge_tuples) - named)
    seed = int(hashlib.sha256(
        cache["response_text"].encode("utf-8")).hexdigest()[:8], 16) % (2 ** 31)
    rec = {"graph_id": f"L_{domain}", "family": "L", "real_semantics": 1,
           "structure": STRUCTURE_NAMES["L"], "N": N,
           "nodes": list(range(N)), "labels": list(nodes),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in sorted(named)],
           "filler_edges": [list(e) for e in filler],
           "source": int(start), "target": int(end), "seed": seed,
           "generator_version": "v2.0-gt8b-ingest",
           "provenance": {
               "cache_path": path,
               "cache_sha256": hashlib.sha256(
                   json.dumps(cache, ensure_ascii=False, sort_keys=True)
                   .encode("utf-8")).hexdigest(),
               "prompt_sha256": cache["prompt_sha256"],
               "prompt_sha256_matches_preregistered": prompt_sha_ok,
               "model": cache.get("model"),
               "same_source_contamination": (
                   "先验臂与生成臂同模型族 ⇒ 同源污染风险（SPEC_GT8B §6 声明）"),
               "named_filler_rule": "DAG 最长路径族=named，其余=filler（冻结口径）"}}
    rec["sha256"] = _canonical_sha256(rec)
    os.makedirs(graph_dir, exist_ok=True)
    with open(graph_path_for(domain, graph_dir), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    return rec


def main():
    ingested, errors = [], {}
    for domain in GT8B_DOMAINS:
        try:
            rec = ingest_domain(domain)
            ingested.append({"graph_id": rec["graph_id"], "N": rec["N"],
                             "n_edges": len(rec["edges"]),
                             "n_named": len(rec["named_edges"]),
                             "real_semantics": rec["real_semantics"],
                             "sha256": rec["sha256"]})
        except CacheMissingError as e:
            errors[domain] = str(e)
    out = {"experiment": "deposon_v20_gt8b_ingest",
           "spec": "docs/SPEC_GT8B.md §3",
           "ingested": ingested, "cache_errors": errors,
           "graph_dir": GRAPH_DIR,
           "honesty": [
               "no LLM API calls issued: 本脚本只读 results/gt8b_cache/；"
               "缓存缺失域显式报错（CacheMissingError），绝不伪造数据。",
               "named/filler 按族 L 冻结口径（DAG 最长路径族）划分；"
               "prompt_sha256 与预登记 manifest 不一致时如实标记，不阻断摄入。",
               "图写入 results/gt8b_cache/graphs/ 独立目录，不污染 corpus/v20。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if errors and not ingested:
        raise CacheMissingError(
            f"no GT-8b caches ingested: {sorted(errors)}")


if __name__ == "__main__":
    main()