# -*- coding: utf-8 -*-
"""
r3 件头自述名回改脚手架 (V4 r3 回改棒, 2026-09-28)
=================================================
派工: 「出 r3 回改」 (PI 2026-09-28 17:20, 对话拍板)
上游: results/_v4_exec_surface_switch_2026_09_28.md §8 第 1 条 (件头自述名漂移)

机制:
  - r3 件 = r2 件**逐字节复制** + **仅**件头自述名字符串行就地替换
  - 修改面严格限定为指定行号内的旧名字符串 -> 实际新名字符串
  - 0 覆盖 r2 (r2 仍为历史快照) / 0 删旧件 / 0 回改既有登记件
  - 0 跑实验 / 0 新读数 / 0 调阈值 / 0 改算法字节
"""
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:/私人资料/deposon-repo/results"

# (r2 源件名, r3 新件名, [(1-based 行号, 旧名字符串, 新名字符串), ...])
JOBS = [
    (
        "_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
        "_v4_supp_t15_executor_r3_2026_09_28.py",
        [
            (5, "_v4_supp_t15_executor_r1_2026_09_27.py",
                "_v4_supp_t15_executor_r3_2026_09_28.py"),
            (17, "results/_v4_supp_t15_executor_r1_2026_09_27.py",
                 "results/_v4_supp_t15_executor_r3_2026_09_28.py"),
        ],
    ),
    (
        "_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
        "_v4_supp_t15r2_executor_r3_2026_09_28.py",
        [
            (3, "_v4_supp_t15r2_executor_r1_2026_09_28.py",
                "_v4_supp_t15r2_executor_r3_2026_09_28.py"),
        ],
    ),
]


def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def main():
    for src_name, dst_name, edits in JOBS:
        src = os.path.join(BASE, src_name)
        dst = os.path.join(BASE, dst_name)
        assert not os.path.exists(dst), "目标件已存在, 拒绝覆盖: %s" % dst

        with open(src, "rb") as f:
            raw = f.read()
        text = raw.decode("utf-8")
        assert "\r\n" not in text, "源件含 CRLF, 中止"
        assert not raw.startswith(b"\xef\xbb\xbf"), "源件含 BOM, 中止"

        lines = text.split("\n")
        touched = []
        for lineno, old_s, new_s in edits:
            i = lineno - 1
            before = lines[i]
            n = before.count(old_s)
            assert n == 1, "L%d 期望恰好 1 处旧名, 实得 %d: %r" % (lineno, n, before)
            after = before.replace(old_s, new_s)
            # 回改后该行不应再含任何 _r1_ 自述名
            assert "_r1_2026_09_2" not in after, "L%d 回改后仍残留 r1 自述名" % lineno
            assert len(after) == len(before) - len(old_s) + len(new_s)
            lines[i] = after
            touched.append((lineno, before, after))

        out = "\n".join(lines).encode("utf-8")
        with open(dst, "wb") as f:
            f.write(out)

        print("=" * 78)
        print("源件 %s  %d B  sha12=%s" % (src_name, len(raw), sha12(src)))
        print("新件 %s  %d B  sha12=%s" % (dst_name, len(out), sha12(dst)))
        print("件头自述名替换行数 = %d" % len(touched))
        for lineno, before, after in touched:
            print("  L%-4d -  %s" % (lineno, before))
            print("  L%-4d +  %s" % (lineno, after))


if __name__ == "__main__":
    main()
