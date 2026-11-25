# -*- coding: utf-8 -*-
"""KD-FLIP-CENSUS anchor reverse-lookup: map SHA-12 content fingerprints -> carriers.
Read-only: walks the repo, hashes every file, no writes. Never uses builtin hash().
"""
import hashlib
import os
import sys

ROOT = r"_repo_mirror"

ANCHORS = [
    "10e40a51c9c1",  # T-2/T-3 撤终态与消解径 生效落账件
    "d52a5d94a002",  # 冻结面设计件（已核准生效）
    "ac0928f38b85",  # N7 -> af
    "25ff6e4f31bc",  # KD-K4-5 R1/R3 补测毕
    "f2a5c4330112",  # 素材根因 4/5 补测毕
    # 今日已消解面之锚（普查件/梳理件已引者，供去重）
    "4a89f8d3ddda",  # T-2/T-3 采认落账件
    "597caf8ba5bc",  # 回函本体
    "e09780d24a7a",  # KD-S3B1 KD1/N7 rulings effect
    "ed36d0171672",  # KD-S3B1 verdict
    "5dc4e089f458",  # KL-M41-3 verdict
    "c8794d87b4b6",  # FAIL_H0 verdict
    "eea5245b31da",  # S3/S5 kd effect
    "905be2174c52",  # append1
    "9e96d0a1ba12",  # 五终判口径件
    "98aabe87ae11",  # killface v1 effect register
    "80a81bd525d4",  # ext5 verdict
    "f54e8a10acde",  # m41 verdict kd effect
    "3e13344783b0",  # 三 seed 执行件
    "6ca1c64c2c44",  # 素材扩充执行件
    "423c84de20d5",  # spec 正身
    "423c84de20d5",
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    want = set(a for a in ANCHORS if a)
    found = {}
    n_files = 0
    n_err = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for name in filenames:
            p = os.path.join(dirpath, name)
            try:
                n_files += 1
                digest = sha256_of(p)
            except Exception:
                n_err += 1
                continue
            s12 = digest[:12]
            if s12 in want:
                found.setdefault(s12, []).append((p, os.path.getsize(p)))
    print("FILES_WALKED=%d ERR=%d" % (n_files, n_err))
    print("-" * 100)
    for a in ANCHORS:
        hits = found.get(a, [])
        if not hits:
            print("ANCHOR %s  MISSING_TRUE" % a)
        for p, size in hits:
            rel = os.path.relpath(p, ROOT)
            print("ANCHOR %s  bytes=%-8d %s" % (a, size, rel))
        if len(hits) > 1:
            print("           ^^ SAME_IDENTITY: %d copies, do not double-count" % len(hits))
    print("-" * 100)
    print("HIT=%d / ASKED=%d" % (len(found), len(set(a for a in ANCHORS))))


if __name__ == "__main__":
    main()
