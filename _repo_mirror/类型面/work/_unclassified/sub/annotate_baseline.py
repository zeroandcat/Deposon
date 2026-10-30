"""P-6 切换落地：向全仓基线追加锚漂移注记（新名件，落 .tmp，可复跑）。

不覆盖原值——基线是 2026-09-28 那棒「0 触动」的证据快照，改其值即毁证。
改为新增独立注记键，原 `mindmap_corpus_v20.py` 条目逐字保留。
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KEY_NOTE = "_anchor_drift_2026_09_29_p6_loadcorpus_r1"

NOTE = {
    "file": "mindmap_corpus_v20.py",
    "snapshot_value": ["7d8d6a30dd8c", 23893],
    "current_value": ["e77e7f3455e0", 25791],
    "changed_at": "2026-09-29",
    "reason": ("P-6 load_corpus 孤儿哨兵 r1 修复应用回原件"
               "（PI 2026-09-29 拍板「就地修+锚更新」ask_ce9d69e725691a5494da3827 q1）；"
               "仅哨兵面变更，其余逐字节不变"),
    "snapshot_meaning": ("本条原值 = 该基线拍摄时（2026-09-28）的盘上真值，"
                         "属历史证据，保留不改；本注记登记其后的授权变更"),
    "register": "results/_v5_loadcorpus_switch_2026_09_29.md",
    "old_bytes_backup": ".tmp/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak",
}


def patch(path):
    with open(path, "rb") as f:
        raw = f.read()
    crlf = raw.count(b"\r\n") > 0
    d = json.loads(raw.decode("utf-8"))
    if KEY_NOTE in d:
        print("SKIP (already annotated): %s" % path)
        return
    d[KEY_NOTE] = NOTE
    out = json.dumps(d, ensure_ascii=False, indent=1 if not crlf else None)
    if crlf:
        out = out.replace("\n", "\r\n")
    else:
        out = out.replace("\r\n", "\n")
    with open(path, "wb") as f:
        f.write(out.encode("utf-8"))
    b = open(path, "rb").read()
    json.loads(b.decode("utf-8"))
    print("OK %s -> sha12 %s (%d B)" % (
        path, hashlib.sha256(b).hexdigest()[:12], len(b)))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        patch(os.path.join(ROOT, p) if not os.path.isabs(p) else p)
