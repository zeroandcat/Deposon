# -*- coding: utf-8 -*-
# ============================================================
# A1 工件删除攻击 (V0 spec §4, §6)  [V0.1.2]
#
# 动作: 准备 5 锚 -> 删一个 -> 用原始 5 路径调 compute_root
# 预期: 抛 FileNotFoundError / PermissionError / OSError (或自定义 E_FILE_MISSING)
# 判死: 检出 -> verdict=PASS, 漏检 -> verdict=FAIL
# 隔离: 无参直跑; 全部工件在 tempfile.TemporaryDirectory 内自建自删,
#       绝不触碰真实仓库五锚。与 a2/a3 范式一致。
#
# V0.1.2 修订: 移除原 --missing <path> 真实攻击分支 (run_with_args)。
#   该分支调用 fp.compute_root([missing_path]) 却【从不删除该路径】:
#   若 --missing 指向的文件仍存在, compute_root 正常返回不抛异常,
#   落入假性 FAIL; 且它诱导操作者对真实仓库冻结锚
#   (docs/SPEC_GT8C.md) 执行删除, 危害严重。现统一为无参 tempdir
#   自建自删, --root 仅作占位忽略。
# ============================================================
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import traceback
from pathlib import Path

# 让 `python -m attacks.a1_delete_anchor` 在仓库根或 /tmp 副本下都能 import
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import fingerprint_v0 as fp  # noqa: E402


def _make_anchors(root_dir: Path, n: int = 5):
    paths = []
    for i in range(n):
        p = root_dir / f"anchor_{i:02d}.bin"
        p.write_bytes(f"A1-PAYLOAD-{i:02d}".encode("utf-8"))
        paths.append(str(p))
    return paths


def _emit(verdict: str, diff: str):
    print(json.dumps({"attack": "A1", "verdict": verdict, "diff": diff},
                     ensure_ascii=False, separators=(",", ":")))


def run_internal():
    """默认演练: 在 tmp 准备 5 锚, 删一个, 调 compute_root(原始 5 路径列表).

    注意: 必须传 5 个原始路径 (含被删的), 让 R1 open() 失败抛 FileNotFoundError;
    传 4 个剩余路径反而无法触发 (它们都还存在)。
    """
    with tempfile.TemporaryDirectory(prefix="deposon_a1_") as td:
        tdp = Path(td)
        anchors = _make_anchors(tdp, 5)
        # 删第 3 个
        victim = anchors[2]
        Path(victim).unlink()
        # 仍按 5 路径调用, 触发缺失检测
        try:
            fp.compute_root(list(anchors))  # 传原始 5 路径, 包含已删 victim
        except FileNotFoundError as e:
            # Linux/macOS: 删后立即 open() 抛 FileNotFoundError
            if victim in str(e) or os.path.basename(victim) in str(e):
                return "PASS", f"compute_root raised FileNotFoundError mentioning {victim}"
            return "PASS", f"compute_root raised FileNotFoundError: {e!s}"
        except PermissionError as e:
            # Windows: 删后 open() 可能先抛 PermissionError (race condition,
            # OS 还没释放 handle), 也算"文件不可用", 检出
            if victim in str(e) or os.path.basename(victim) in str(e):
                return "PASS", f"compute_root raised PermissionError mentioning {victim} (Windows race)"
            return "PASS", f"compute_root raised PermissionError: {e!s} (Windows race)"
        except OSError as e:
            # 其他 OS-level 错误 (如 IsADirectoryError 等) 也算"不可读"
            if victim in str(e) or os.path.basename(victim) in str(e):
                return "PASS", f"compute_root raised {type(e).__name__} mentioning {victim}"
            return "PASS", f"compute_root raised {type(e).__name__}: {e!s}"
        except Exception as e:
            # 其他异常 (例如 E_FILE_MISSING 自定义异常) 也算检出
            if "E_FILE_MISSING" in type(e).__name__ or "E_FILE_MISSING" in str(e):
                return "PASS", f"compute_root raised {type(e).__name__}: {e!s} for {victim}"
            return "FAIL", f"compute_root raised unexpected {type(e).__name__}: {e!s}"
        return "FAIL", "compute_root silently succeeded despite missing anchor"


def main():
    parser = argparse.ArgumentParser(description="A1 工件删除攻击 (无参; tempdir 自建自删)")
    parser.add_argument("--root", help="(占位忽略) 与 a2/a3 一致, 演练模式不消费")
    args = parser.parse_args()

    try:
        verdict, diff = run_internal()
    except Exception:
        # 任何意外崩溃都判为漏检 (FAIL), 保留 traceback 在 diff
        verdict, diff = "FAIL", f"unexpected crash: {traceback.format_exc()}"
    _emit(verdict, diff)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
