# -*- coding: utf-8 -*-
# ============================================================
# A2 集合重排攻击 (V0 spec §4, §6)
#
# 动作: 5 锚 -> 算 manifest (按 path 升序) -> 攻击者按"非字典序"
#       (此处用"按文件大小"重排) 生成 tampered_manifest ->
#       重算 root, 与原 root 比对
# 预期: root 必变; verify_root(tampered, original) == False
# 判死: 检出 (root 变 或 verify_root False) -> PASS
# 隔离: 全部操作在 tempfile.mkdtemp() 临时目录
# ============================================================
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import traceback
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import fingerprint_v0 as fp  # noqa: E402


def _make_anchors_with_sizes(root_dir: Path):
    """造 5 锚, 大小非单调: [1, 100, 50, 200, 10] 字节.
    保证: 按 size 排序 ≠ 按 path 排序."""
    sizes = [1, 100, 50, 200, 10]
    paths = []
    for i, sz in enumerate(sizes):
        p = root_dir / f"anchor_{i:02d}.bin"
        p.write_bytes(b"X" * sz)
        paths.append(str(p))
    return paths, sizes


def _emit(verdict: str, diff: str):
    print(json.dumps({"attack": "A2", "verdict": verdict, "diff": diff},
                     ensure_ascii=False, separators=(",", ":")))


def _manifest_by_size(paths):
    """攻击者重排: 按文件大小排序, 生成非规范 manifest 字符串."""
    rows = []
    for p in paths:
        size = os.path.getsize(p)
        # 用 fp._content_addr 拿真 hash, 但排 sequence 不再按 path 升序
        h = fp._content_addr(p)
        rows.append({"path": p, "hash": h, "_size": size})
    rows.sort(key=lambda r: r["_size"])  # 按 size 升序, 非字典序
    # 攻击者只重排了元素顺序, 不改结构 (与 spec §4 A2 描述一致:
    # "manifest 序列化改为按文件大小排序")
    cleaned = [{"path": r["path"], "hash": r["hash"]} for r in rows]
    return json.dumps(cleaned, ensure_ascii=False, separators=(",", ":"))


def run_internal():
    with tempfile.TemporaryDirectory(prefix="deposon_a2_") as td:
        tdp = Path(td)
        anchors, sizes = _make_anchors_with_sizes(tdp)
        # 原始: 按 path 升序
        m_original = fp._manifest(anchors)
        root_original = fp._root(m_original)
        # 攻击: 按 size 升序
        m_tampered = _manifest_by_size(anchors)
        root_tampered = fp._root(m_tampered)
        # 验证
        if root_tampered == root_original:
            return "FAIL", (
                f"size-sorted manifest produced SAME root {root_original} "
                f"(sizes={sizes}, paths={[os.path.basename(p) for p in anchors]})"
            )
        # 二次验证: verify_root 应返回 False
        ok = fp.verify_root(m_tampered, root_original)
        if not ok:
            return "PASS", (
                f"size-sorted manifest changed root: {root_original} -> {root_tampered}; "
                f"verify_root(tampered, claimed)={ok}"
            )
        return "FAIL", (
            f"root changed but verify_root returned True (should be False); "
            f"roots: {root_original} vs {root_tampered}"
        )


def main():
    parser = argparse.ArgumentParser(description="A2 集合重排攻击")
    parser.add_argument("--root", help="(可选) 公布的 claimed root, 用于交叉验证")
    args = parser.parse_args()

    try:
        verdict, diff = run_internal()
    except Exception:
        verdict, diff = "FAIL", f"unexpected crash: {traceback.format_exc()}"
    _emit(verdict, diff)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
