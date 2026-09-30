"""
_v5_qwen_retry_candidates_20260929.py
=====================================
候选 key 文件排查（**元数据 + 模式类，0 明文**）
用于核实 PI 处置「最新文件包含了 URL 与 key」——盘上是否存在比
Desktop/AI/LLM API.txt 更新的、含 URL+key 的文件。
"""

import hashlib
import os
import re
from datetime import datetime, timezone

CANDIDATES = [
    r"C:\Users\Administrator\Desktop\AI\LLM API.txt",
    r"C:\Users\Administrator\Desktop\AI\卖家精灵MCP.txt",
    r"C:\Users\Administrator\Desktop\AI\AI.lnk",
]
URL_RE = re.compile(r"https?://[^\s\"'<>）)，,；;]+")
SECRET_RX = re.compile(r"\b(?:sk-|sk-ant-|ark-)[A-Za-z0-9_\-]{8,}")

rows = []
for p in CANDIDATES:
    if not os.path.isfile(p):
        rows.append((p, "MISSING", "", "", "", ""))
        continue
    st = os.stat(p)
    raw = open(p, "rb").read()
    sha12 = hashlib.sha256(raw).hexdigest()[:12].upper()
    txt = raw.decode("utf-8", errors="replace")
    n_url = len(URL_RE.findall(txt))
    n_sec = len(SECRET_RX.findall(txt))
    hosts = sorted({m for m in re.findall(r"https?://([^/\s]+)", txt)})
    rows.append((
        p,
        datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
        str(st.st_size),
        sha12,
        f"urls={n_url},sk_ark_secrets={n_sec}",
        ",".join(hosts)[:70] if hosts else "-",
    ))

print("=" * 100)
print("候选 key 文件排查 · 0 明文（仅 路径/mtime/size/sha12/模式计数/主机名）")
print("=" * 100)
for r in sorted(rows, key=lambda x: x[1], reverse=True):
    print(f"mtime={r[1]:<26} size={r[2]:<7} sha12={r[3]:<13} {r[4]:<28} {r[5]}")
    print(f"    path = {r[0]}")
print("=" * 100)
