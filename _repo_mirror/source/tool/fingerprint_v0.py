# -*- coding: utf-8 -*-
# ============================================================
# P-D 可审计账指纹算法 V0 实现
#
# 契约来源: docs/V3X/P_D_FINGERPRINT_V0_SPEC.md
# 范围    : R1 内容寻址 / R2 规范 manifest / R3 根指纹
#           R4 追加式 runs/ 链 / R5 验证器安全边界
# 不在范围: 二叉 Merkle 聚合 / 成本线判死 / 任何外部对接
#
# 公开 API (V0 §5 + V0.1 增 verify_chain):
#     compute_root(artifact_paths) -> str           # 12hex
#     verify_root(manifest_str, claimed_root) -> bool
#     append_run(prev_hash, current_root) -> dict
#     read_runs_count() -> int
#     verify_chain() -> dict                         # V0.1 补 spec §4 A3 缺口
#
# Spec §3/§5 签名差异处置:
#   §3 伪代码 append_run 含 ts 参数; §5 实现签名只有 (prev_hash, current_root).
#   按派单指令采用 §5 字面签名, ts 内部用 datetime.now(timezone.utc).isoformat().
#   后续若 spec 修订, 由 reviewer-b / v3x 处理.
#
# R5 安全边界落实:
#   - 模块顶层不打开任何锚文件
#   - 不导出任何 read_file / listdir / open(锚文件) 类 API
#   - 不在模块顶层写出锚点路径字符串 (5 个冻结工件的路径属于外部 spec,
#     由调用方传入)
# ============================================================
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List  # noqa: F401  (类型提示保留, 当前未直接用)

# 模块私有: anchor 路径不在此处出现
_RUNS_DIRNAME = "runs"
_RUNS_FILENAME_PREFIX = "pd_v0"
_RUNS_FILENAME_SUFFIX = ".jsonl"
_GENESIS_PREV_HASH = "0" * 12  # 链头 (spec §2 R4)

# 错误码 (spec §5)
_E_FILE_MISSING = "E_FILE_MISSING"
_E_ROOT_MISMATCH = "E_ROOT_MISMATCH"
# _E_CHAIN_BREAK_AT_<n> 形式在攻击 A3 中动态拼出


# ----------------------------------------------------------------
# R1: 内容寻址
# ----------------------------------------------------------------
def _content_addr(path: str) -> str:
    """内部 R1: 读文件字节 -> sha256[0:12]。

    安全防御 (V0.1.1):
      - 软链拒绝: Path.is_symlink() == True 时抛 OSError("E_SYMLINK: ...")
        防攻击者用软链替换锚指向恶意文件 (S5b 攻击模型)
      - 缺失文件抛 FileNotFoundError (A1 由调用方翻译为 E_FILE_MISSING)
    """
    p = Path(path)
    if p.is_symlink():
        # 软链 = 攻击者可能用软链替换锚指向恶意文件; 拒绝静默跟随
        raise OSError(
            f"E_SYMLINK: refusing to follow symlink at {path} "
            f"(target: {p.resolve() if p.exists() else '<broken>'})"
        )
    # 仅内部读取 (R5: 不导出为模块 API)
    with open(path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()[:12]


# ----------------------------------------------------------------
# R2: 规范 manifest
# ----------------------------------------------------------------
def _manifest(artifact_paths: List[str]) -> str:
    """内部 R2: 5 锚 -> 排序 JSON 字符串。

    spec §2 R2 严格编码: ensure_ascii=False, separators=(",", ":"),
    无 BOM, 元素按 path ASCII 升序。
    """
    rows = [{"path": p, "hash": _content_addr(p)} for p in artifact_paths]
    rows.sort(key=lambda r: r["path"])  # ASCII 升序
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


# ----------------------------------------------------------------
# R3: 根指纹
# ----------------------------------------------------------------
def _root(manifest_str: str) -> str:
    """内部 R3: sha256(manifest_utf8)[0:12]"""
    return hashlib.sha256(manifest_str.encode("utf-8")).hexdigest()[:12]


# ----------------------------------------------------------------
# 公开 API 1: compute_root  (R1 + R2 + R3 合并)
# ----------------------------------------------------------------
def compute_root(artifact_paths: List[str]) -> str:
    """R1+R2+R3: 5 锚路径集合 -> 12hex 根指纹。

    失败时:
        - 任一锚缺失 -> FileNotFoundError (与内置行为一致, spec §4 A1)
        - 调用方应捕获并按 E_FILE_MISSING 翻译
    """
    return _root(_manifest(artifact_paths))


# ----------------------------------------------------------------
# 公开 API 2: verify_root
# ----------------------------------------------------------------
def verify_root(manifest_str: str, claimed_root: str) -> bool:
    """R3 验证: 用调用方提供的 manifest 字符串重算 root,
    与 claimed_root 逐位比对。

    注意: 此函数不读磁盘, 调用方负责构造 manifest_str (spec §5 字面)。
    """
    if not isinstance(claimed_root, str) or len(claimed_root) != 12:
        return False
    return _root(manifest_str) == claimed_root


# ----------------------------------------------------------------
# R4 链文件路径 (模块私有, 内部用, 不导出)
# ----------------------------------------------------------------
def _runs_dir() -> Path:
    """verifier/runs/ 绝对路径, 兼容 /tmp 副本: 用 __file__ 父目录锚定。"""
    here = Path(__file__).resolve().parent
    return here / "verifier" / _RUNS_DIRNAME


def _today_chain_path() -> Path:
    d = _runs_dir()
    d.mkdir(parents=True, exist_ok=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return d / f"{day}_{_RUNS_FILENAME_PREFIX}{_RUNS_FILENAME_SUFFIX}"


# ----------------------------------------------------------------
# 公开 API 3: append_run
# ----------------------------------------------------------------
def append_run(prev_hash: str, current_root: str) -> Dict[str, str]:
    """R4: 追加一条 {ts, prev_hash, current_root} 到今日 runs jsonl。

    ts 内部自动生成 (ISO8601 UTC, spec §2 R4)。
    返回写入的 dict (含 ts)。
    """
    if not isinstance(prev_hash, str) or len(prev_hash) != 12:
        raise ValueError(f"prev_hash must be 12hex, got {prev_hash!r}")
    if not isinstance(current_root, str) or len(current_root) != 12:
        raise ValueError(f"current_root must be 12hex, got {current_root!r}")

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "prev_hash": prev_hash,
        "current_root": current_root,
    }
    chain = _today_chain_path()
    # 追加 (spec §2 R4: 仅 append, 禁止 update/delete/truncate)
    with open(chain, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
        f.write("\n")
    return record


# ----------------------------------------------------------------
# 公开 API 4: read_runs_count
# ----------------------------------------------------------------
def read_runs_count() -> int:
    """R4: 扫 verifier/runs/*.jsonl, 累加非空行数。"""
    runs = _runs_dir()
    if not runs.exists():
        return 0
    total = 0
    for jl in sorted(runs.glob(f"*_{_RUNS_FILENAME_PREFIX}{_RUNS_FILENAME_SUFFIX}")):
        with open(jl, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    total += 1
    return total


# ----------------------------------------------------------------
# R4 公开 API 5: verify_chain  (V0.1 新增, 补 spec §4 A3 缺口)
# ----------------------------------------------------------------
def verify_chain() -> dict:
    """V0.1 新增: 校验 verifier/runs/ 链完整性 (within-file scope).

    Per-file 检查:
      - Record 0 必 prev_hash == "0"*12 (GENESIS)
      - Record i (i>0) 必 prev_hash == record[i-1].current_root

    跨文件链连续性**不在 V0 范围** (V1 再定, 见 P_D_V0_REPORT_mavis §11)

    返回结构化报告 (对齐 spec §4 A3 错误码风格):
      {
        "valid": bool,             # True iff 无任何 break / genesis violation
        "total_records": int,      # 跨所有 jsonl 文件的非空记录数
        "breaks": [
          {"file": str, "record_index": int,
           "expected_prev_hash": str, "got_prev_hash": str,
           "error_code": "E_CHAIN_BREAK_AT_<file>:<n>"},
          ...
        ],
        "genesis_violations": ["<file>:0: <reason>", ...],
        "parse_errors":     ["<file>:<line>: <reason>", ...],
      }
    """
    runs = _runs_dir()
    result = {
        "valid": True,
        "total_records": 0,
        "breaks": [],
        "genesis_violations": [],
        "parse_errors": [],
    }
    if not runs.exists():
        return result

    for jl in sorted(runs.glob(f"*_{_RUNS_FILENAME_PREFIX}{_RUNS_FILENAME_SUFFIX}")):
        prev_root = None  # 本文件内上一条 current_root
        with open(jl, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                s = line.strip()
                if not s:
                    continue
                try:
                    rec = json.loads(s)
                except json.JSONDecodeError as e:
                    result["valid"] = False
                    result["parse_errors"].append(
                        f"{jl.name}:{line_idx}: {e!s}"
                    )
                    continue

                result["total_records"] += 1
                got_prev = rec.get("prev_hash", "")
                curr = rec.get("current_root", "")

                if line_idx == 0:
                    # Genesis check: 每文件首条必 prev_hash == "0"*12
                    if got_prev != _GENESIS_PREV_HASH:
                        result["valid"] = False
                        result["genesis_violations"].append(
                            f"{jl.name}:0: prev_hash={got_prev!r} != "
                            f"GENESIS={_GENESIS_PREV_HASH!r}"
                        )
                else:
                    # Chain continuity
                    expected = prev_root
                    if got_prev != expected:
                        result["valid"] = False
                        result["breaks"].append({
                            "file": jl.name,
                            "record_index": line_idx,
                            "expected_prev_hash": expected,
                            "got_prev_hash": got_prev,
                            "error_code": (
                                f"E_CHAIN_BREAK_AT_{jl.name}:{line_idx}"
                            ),
                        })

                prev_root = curr

    return result


# ----------------------------------------------------------------
# V0 §7 占位 (不消费, 不导出为常用 API)
# ----------------------------------------------------------------
# P-B 高层对接位: V0 仅占位, 不实接
P_B_INTERFACE_RESERVED = None  # noqa: F841 - spec §7 占位


__all__ = [
    "compute_root",
    "verify_root",
    "append_run",
    "read_runs_count",
    "verify_chain",
    "P_B_INTERFACE_RESERVED",
]


# 链头常量供调用方初始化 (A3 测试用)
GENESIS_PREV_HASH = _GENESIS_PREV_HASH
