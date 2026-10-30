# -*- coding: utf-8 -*-
"""2026-09-28 每日收尾整理棒 · 陈旧缓冲件「信息是否已落盘」实质探测 (worker)

对每个候选缓冲件:
  1) 抽出全部 12-hex token (SHA-12, 忽略大小写)
  2) 全仓(含 .tmp 之外的所有工作区文件 + 〔归档区〕) 建 SHA-12 -> 路径 反查表
  3) 报出「有实体的 token」与「查无实体的 token」
若 token 全部可反查到现存实体 => 该缓冲件所断言的事实全部现仍在盘 => 内容已入权威件
SHA-12 = hashlib.sha256(data).hexdigest()[:12] 小写
"""
import hashlib
import pathlib
import re
import sys

REPO = pathlib.Path(r"_repo_mirror")
TMP = REPO / ".tmp"
EXT_ARCHIVE = pathlib.Path(r"〔归档件引用·未上传:〔归档区〕〕")
HEX12 = re.compile(r"\b([0-9A-Fa-f]{12})\b")

CANDIDATES = [
    "_d4_relabel_run1.log", "_recheck_r1_run1.log", "_recheck_r1_runA.log",
    "_recheck_r1_runB.log", "_recheck_r1_runC.log", "_recheck_r1_runD.log",
    "_run_output.log", "_v3r1_run1.log", "_v3r1_run2.log",
    "_gaps.txt", "_gaps2.txt", "_r10.txt", "_r6_evidence.txt", "_r11_ctx.txt",
    "_e3536.txt", "_final_sha.txt", "_audit3b.txt", "_audit_part3_out.txt",
    "_audit_part4.txt", "_postcheck_v16_alt_stdout.txt", "_v16_tail_only.txt",
    "_t15r2_checkpoint_warn.jsonl", "_t15_probe_log.json",
    "_rj5_mapping_test_2026_09_27.out.txt", "_t15_percell_out.txt",
]


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def build_index():
    idx = {}
    n = 0
    for base in (REPO, EXT_ARCHIVE):
        for p in base.rglob("*"):
            try:
                if p.is_file() and not p.is_symlink():
                    # 项目口径: 盘实测 SHA-12 以 UPPERCASE 展示; 反查表统一大写键
                    idx.setdefault(sha12(p).upper(), str(p))
                    n += 1
            except Exception:  # noqa: BLE001
                continue
    return idx, n


def main():
    idx, n = build_index()
    print(f"[index] 索引 {n} 件 / {len(idx)} 个唯一 SHA-12\n")
    rows = []
    for name in CANDIDATES:
        p = TMP / name
        if not p.exists():
            print(f"{name}\tMISSING")
            continue
        toks = sorted({t.upper() for t in HEX12.findall(
            p.read_text(encoding="utf-8", errors="replace"))})
        resolved = [t for t in toks if t in idx]
        ghost = [t for t in toks if t not in idx]
        rows.append((name, len(toks), len(resolved), len(ghost), ghost))
    print("name\ttokens\tresolved\tghost\tghosts")
    for name, nt, nr, ng, ghosts in rows:
        print(f"{name}\t{nt}\t{nr}\t{ng}\t{ghosts[:6]}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
