# -*- coding: utf-8 -*-
"""v171 落账件辅助工具：全仓 SHA-12 反向指纹扫描 + 字节级体检。
纪律：只读；输出落 UTF-8 文件；控制台仅 ASCII。
"""
import hashlib
import json
import os
import sys

ROOT = r"_repo_mirror"
OUT = os.path.join(ROOT, "_tools_v171_fp_out.json")

TARGETS = {
    "170ab543d941": "清路判定件 (v171 Q1 判定件)",
    "609943436a0d": "Q0 口径件 (v171 Q3)",
    "c7ef49e7ced3": "释触发态拟案件 (v171 Q2)",
    "45f1ea5e5b23": "同门二拟辨明件 (v171 Q4 辨明果)",
    "356ef2e9db1c": "甲-C5 新构造草案 (v171 Q1 读甲)",
    "c013aeb1235f": "K-SEPCAL-7 终判件 (v168-Q2 PI 复核采认先例)",
    "77bc92c9d227": "K-FKD-2-1 拟案件 (v171 Q4)",
}


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def main():
    found = {k: [] for k in TARGETS}
    total = 0
    errors = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for name in filenames:
            p = os.path.join(dirpath, name)
            if os.path.abspath(p) == os.path.abspath(OUT):
                continue
            total += 1
            try:
                s = sha12(p)
            except Exception as e:  # noqa: BLE001
                errors.append({"path": p, "err": repr(e)[:120]})
                continue
            if s in found:
                found[s].append(os.path.relpath(p, ROOT))
    data = {
        "scanned_files": total,
        "errors": errors,
        "targets": {
            k: {"label": TARGETS[k], "hits": sorted(found[k]), "hit_count": len(found[k])}
            for k in TARGETS
        },
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("SCANNED=" + str(total))
    print("ERRORS=" + str(len(errors)))
    for k in sorted(TARGETS):
        print(k + " -> " + str(len(found[k])))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
