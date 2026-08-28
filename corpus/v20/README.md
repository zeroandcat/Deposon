# corpus/v20 — 多图语料（20 图）

本目录的 20 张图 JSON **不逐一入库**（与 results/MANIFEST_large_files.md 同一内容寻址原则）：

- **族 S（16 张）**：由 `mindmap_corpus_v20.py` 确定性生成——同 seed 同 sha256
  （`tests/test_v20.py` 锁定）。再生：`python3 mindmap_corpus_v20.py`
- **族 L（4 张）**：由 `run_v20_familyL_ingest.py` 从 `results/familyL_cache/`（已入库）
  摄入生成，幂等。再生：`python3 run_v20_familyL_ingest.py`

每图的 graph_id / 结构 / N / 边数 / named 数 / seed / **sha256** 全部登记在
`index.json`（本目录，已入库）——任何人对再生结果逐图核对 sha256 即可验证一致性。
