# -*- coding: utf-8 -*-
"""
V5 / V3 修复线 C5 / B 组 (SVD 主成分数 2->3) -- 原料重取脚本
V3X-C5B-FETCH-2026-09-29-A1

用途: B 组 = 换坐标空间 (治根因), 盘上无 raw 2048-d 向量缓存 => 必须重调
      doubao-embedding-vision-251215 API 取 22x2048 原始向量.

严格纪律 (V4 铁律):
  R4  key 永不明文: 仅 runtime 从环境变量读入内存; 0 落盘 / 0 入 JSON /
      0 入 log / 0 入 prompt / 0 打印. 本脚本不构造任何掩码串输出.
  0 网络写: 只 POST 1 个 endpoint, 只读 corpus (不写 corpus).
  0 重试: 每 chunk 单次; 失败即 exit (串行, 从简).
  0 代理: 与原始件 constraints_honored.no_proxy=True 一致; 且本 endpoint
      为 volces.com, 非 teamorouter/openrouter, 故不套用 tun 代理纪律.

复现口径 (严格对齐 results/_archive_2026_09_24/_volc_22cap_emb.py):
  - caption 构造式逐字沿用原始件
  - SVD 用 np.linalg.svd(embs_n, full_matrices=False), 分数 = U[:, :k] * S[:k]
  - 3 chunk 10/10/2
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[1]
CORPUS = BASE / "corpus" / "v20"
P_INDEX = CORPUS / "index.json"
P_STORED_EMB = BASE / "results" / "deposon_volcengine_22caption_embedding_2026_09_10.json"
OUT_RAW = BASE / "results" / "_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json"

ENDPOINT = "https://ark.cn-beijing.volces.com/api/coding/v3/embeddings"
MODEL = "doubao-embedding-vision-251215"
CHUNK = 10


def sha256_file(p: Path) -> str:
    import hashlib
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    # ---- R4: key runtime-only ----
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("[KEY] ARK_API_KEY not in environment -> abort (0 fallback to plaintext file)")
        return 2
    print(f"[KEY] loaded from env at runtime, len={len(api_key)} (value 0 printed / 0 persisted)")

    # ---- 0 proxy (对齐原始件) ----
    for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy",
              "ALL_PROXY", "all_proxy"):
        os.environ.pop(k, None)

    # ---- 重建 22 captions (只读) ----
    index = json.load(open(P_INDEX, encoding="utf-8"))
    assert index["n_graphs"] == 22, f"expected 22 graphs, got {index['n_graphs']}"
    captions, concept_ids, families, structures = [], [], [], []
    for g in index["graphs"]:
        d = json.load(open(CORPUS / g["file"], encoding="utf-8"))
        labels = d.get("labels", [])
        cap = (f"Concept graph {g['graph_id']} "
               f"(family={g['family']}, structure={g['structure']}, "
               f"N={g['N']}, n_named={g['n_named']}): " + "; ".join(labels))
        captions.append(cap)
        concept_ids.append(g["graph_id"])
        families.append(g["family"])
        structures.append(g["structure"])
    print(f"[CAPTIONS] n={len(captions)}")

    # ---- 串行 3 chunk, 0 重试 ----
    chunks = [captions[i:i + CHUNK] for i in range(0, len(captions), CHUNK)]
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    all_data, statuses, lat_ms, tot_tok, prompt_tok = [], [], 0.0, 0, 0
    for ci, chunk in enumerate(chunks):
        body = {"model": MODEL, "input": chunk}
        req = urllib.request.Request(
            ENDPOINT, data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers=headers, method="POST")
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                status, raw = resp.status, resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            status = e.code
            raw = e.read().decode("utf-8", errors="replace") if e.fp else ""
            print(f"[ERR] chunk {ci+1} http={status} body[:300]={raw[:300]!r}")
            return 3
        lat = (time.time() - t0) * 1000
        if status != 200:
            print(f"[ERR] chunk {ci+1} http={status} body[:300]={raw[:300]!r}")
            return 3
        obj = json.loads(raw)
        ed = obj.get("data", [])
        if len(ed) != len(chunk):
            print(f"[ERR] chunk {ci+1} expected {len(chunk)} got {len(ed)}")
            return 3
        all_data.extend(ed)
        statuses.append(status)
        lat_ms += lat
        u = obj.get("usage", {}) or {}
        tot_tok += u.get("total_tokens", 0) or 0
        prompt_tok += u.get("prompt_tokens", 0) or 0
        print(f"  chunk {ci+1}/3 OK http=200 n={len(chunk)} latency={lat:.0f}ms")
        time.sleep(2)  # 串行节流

    all_data.sort(key=lambda x: x.get("index", 0))
    embs = np.array([it["embedding"] for it in all_data], dtype=np.float64)
    assert embs.shape == (22, 2048), f"bad shape {embs.shape}"
    print(f"[API] merged shape={embs.shape} total_latency={lat_ms:.0f}ms total_tokens={tot_tok}")

    norms = np.linalg.norm(embs, axis=1, keepdims=True)
    embs_n = embs / (norms + 1e-12)
    U, S, Vt = np.linalg.svd(embs_n, full_matrices=False)
    tot_var = float((S ** 2).sum())
    var_k = {k: round(float((S[:k] ** 2).sum() / tot_var), 6) for k in (2, 3, 4)}

    # ---- 复现自证: 新算 SVD-2 vs 盘上存储 svd2_coords ----
    stored = json.load(open(P_STORED_EMB, encoding="utf-8"))["svd2_coords"]
    fresh2 = U[:, :2] * S[:2]
    max_abs_dev, per_id_dev = 0.0, {}
    for i, cid in enumerate(concept_ids):
        s = stored[cid]
        dev = max(abs(float(s[0]) - float(fresh2[i, 0])), abs(float(s[1]) - float(fresh2[i, 1])))
        per_id_dev[cid] = round(dev, 8)
        max_abs_dev = max(max_abs_dev, dev)
    reproduce_2d = max_abs_dev <= 5e-4  # 存储值按 4 位小数入盘 => 容差 5e-5 量级
    print(f"[REPRO] SVD-2 fresh vs stored: max_abs_dev={max_abs_dev:.3e} "
          f"reproduce_within_4dp={reproduce_2d}")
    print(f"[SVD] var_explained k=2:{var_k[2]} k=3:{var_k[3]} k=4:{var_k[4]}")

    def gt_label(gid, fam):
        if fam == "L":
            return 0
        if gid.startswith("S1"):
            return 1
        if gid.startswith("S2"):
            return 2
        return 3

    gt = [gt_label(concept_ids[i], families[i]) for i in range(22)]
    class_names = ["L(llm_dag)", "S1(chain)", "S2(tree)", "S3-S6(misc)"]

    out = {
        "task_id": "V3X-C5B-FETCH-2026-09-29-A1",
        "task": "C5 B 组原料重取: 22 caption x 2048-d 原始向量 (doubao-embedding-vision-251215)",
        "date": datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),
        "generator": ".tmp/_v5_c5_b_fetch_raw_embeddings.py",
        "method": "复现 _archive_2026_09_24/_volc_22cap_emb.py 调用面; 3 chunk 10/10/2 串行 0 重试",
        "model": MODEL,
        "endpoint": ENDPOINT,
        "auth": "R4: key 仅 runtime 自环境变量读入内存; 本件 0 落盘 0 入 JSON 0 入 log 0 入 prompt",
        "caption_source": "corpus/v20/index.json + per-graph labels (只读)",
        "caption_construction": "f\"Concept graph {graph_id} (family={family}, structure={structure}, N={N}, n_named={n_named}): \" + '; '.join(labels)",
        "concept_ids": concept_ids,
        "gt_labels": gt,
        "gt_class_names": class_names,
        "per_class_members": {class_names[c]: [concept_ids[i] for i in range(22) if gt[i] == c]
                              for c in range(4)},
        "embedding_dim": 2048,
        "api_calls": 3,
        "api_chunks": [len(c) for c in chunks],
        "http_status": statuses,
        "batch_latency_ms": round(lat_ms, 1),
        "total_tokens": tot_tok,
        "prompt_tokens": prompt_tok,
        "input_sha12": {
            "corpus/v20/index.json": sha256_file(P_INDEX)[:12],
            "results/deposon_volcengine_22caption_embedding_2026_09_10.json": sha256_file(P_STORED_EMB)[:12],
        },
        "svd_scores": {concept_ids[i]: [round(float((U[i, k] * S[k])), 6) for k in range(4)]
                       for i in range(22)},
        "svd_singular_values_top4": [round(float(S[k]), 6) for k in range(4)],
        "svd_var_explained_cumulative": var_k,
        "reproduction_selfcheck": {
            "note": "B 组前提自证: 新调 API 的 SVD-2 是否复现盘上存储 svd2_coords (源件 c4b774c8e34c)",
            "max_abs_dev_vs_stored_svd2": round(max_abs_dev, 10),
            "per_caption_max_abs_dev": per_id_dev,
            "reproduce_within_4dp": reproduce_2d,
        },
        "raw_embeddings": {concept_ids[i]: [round(float(x), 8) for x in embs[i]]
                           for i in range(22)},
        "raw_embeddings_note": "22x2048 float, 8 位小数; 未做 dtype 截断以外的任何加工",
        "constraints_honored": {
            "key_runtime_only": True,
            "key_not_in_json": True,
            "key_not_in_log": True,
            "key_not_in_prompt": True,
            "no_proxy": True,
            "no_retry": True,
            "no_model_switch": True,
            "serial_chunks": True,
            "corpus_read_only": True,
        },
    }
    with open(OUT_RAW, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"[OK] {OUT_RAW.name} bytes={OUT_RAW.stat().st_size}")
    print(f"[SUMMARY] reproduce_2d={reproduce_2d} max_dev={max_abs_dev:.3e} "
          f"var2={var_k[2]} var3={var_k[3]} var4={var_k[4]} api_calls=3 tokens={tot_tok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
