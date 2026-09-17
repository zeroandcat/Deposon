# -*- coding: utf-8 -*-
"""v42_v2 分层 verifier (2026-09-16)
执行代理 B (KIMI 派出) — 重设计 v42 verifier。

重设计动机 (旧 v42 的真实短板, 经侦察核实):
  1. 仅 5 文件覆盖: 旧语义只对 5 锚制品字节做 SHA-256[0:12] 集合比对
     (deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py L30-45)。
  2. 单值比对无定位能力: 拒绝时不知哪个文件、哪一层。
  3. 无 manifest / 链结构: 任何合法更新都使全局指纹失效, 且旧基线可被整体
     回滚 (重放) 而无任何机制察觉。

更正声明 (强制): P-M 初报"旧 v42 漏检率 100%"系计数语义反转 —— 该 runner
L82-87 把 is_valid=True 计入 detected_count, 把 is_valid=False (即拒绝 =
检出) 计入 missed_count, 两个分支记反。按正确语义 (检出 = verifier 拒绝),
旧 v42 对单 bit 翻转的检出率为 100%。v42_v2 的设立依据是上述三项真实短板,
而非漏检率。

分层语义 (保护集 n = 8 文件):
  L1 逐文件 SHA-256[0:12] 比对 (沿 fingerprint_v0 R1 口径)。
     攻击面 O(n): 攻击者须同时伪造通过逐文件比对的全部目标文件,
     防御方复算成本与保护集大小 n 成线性关系。
  L2 canonical manifest + 根指纹 (沿 fingerprint_v0 R2/R3 口径:
     rows 按 path ASCII 升序, json.dumps ensure_ascii=False,
     separators=(",",":"), root = sha256(manifest utf-8)[0:12])。
     绑定文件集合结构: 增 / 删 / 改名 / 基线 manifest 整体替换在此层暴露。
  L3 追加式 runs 链 (新链文件 v42_v2_runs_2026_09_16.jsonl,
     记录格式沿 R4: {ts, prev_hash, current_root}, 扩展 manifest 字段用于
     重放攻击后的文件级定位; 链头 = 最近一次合法基线根)。
     旧基线 + 旧文件整体回滚 (重放) 在此层暴露: 重放根 != 链头根。

拒绝输出契约: 每次拒绝给出 {layer, file, expected, actual, detail}。

基线自举: 首次运行从受保护文件实算生成基线并落盘
  deposon_team/verifier/v42_v2_baseline_2026_09_16.json

铁律: 0 LLM 调用 (纯 hashlib + json + 标准库), 不调网关, 不 pip install,
不设 proxy, 不改动 verifier/runs/2026-09-04_pd_v0.jsonl 旧链。
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

# ----------------------------------------------------------------
# 常量
# ----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # 仓库根
VERIFIER_DIR = Path(__file__).resolve().parent
BASELINE_PATH = VERIFIER_DIR / "v42_v2_baseline_2026_09_16.json"
CHAIN_PATH = VERIFIER_DIR / "v42_v2_runs_2026_09_16.jsonl"  # 新链, 不触旧链

GENESIS_PREV_HASH = "0" * 12  # 沿 fingerprint_v0 spec §2 R4 链头

# 保护集 (n = 8): 5 锚 JSON + 4 plugin spec + corpus/v20/index.json + v19 + v21
# 路径为仓库相对 posix 路径, 按 ASCII 升序排列 (R2 排序口径)。
PROTECTED_SET: List[str] = sorted([
    "verifier/handoff/KT_ABC1_anchors_sha256_12.json",
    "deposon_team/plugins/skill_a_p_a_60cells.py",
    "deposon_team/plugins/skill_b_p_c_alpha_beta.py",
    "deposon_team/plugins/skill_c_p_e_3modality.py",
    "deposon_team/plugins/skill_d_p_f_observer.py",
    "corpus/v20/index.json",
    "results/deposon_v19_benchmark_fixes.json",
    "results/deposon_v21_gtformal.json",
])

E_FILE_MISSING = "E_FILE_MISSING"
E_L1_MISMATCH = "E_L1_FILE_HASH_MISMATCH"
E_L2_ROOT_MISMATCH = "E_L2_ROOT_MISMATCH"
E_L2_BASELINE_SELF_INCONSISTENT = "E_L2_BASELINE_SELF_INCONSISTENT"
E_L3_CHAIN_HEAD_MISMATCH = "E_L3_CHAIN_HEAD_MISMATCH"
E_L3_CHAIN_BREAK = "E_L3_CHAIN_BREAK"


# ----------------------------------------------------------------
# R1/R2/R3 原语 (沿 fingerprint_v0 口径, 支持内存字节以模拟攻击)
# ----------------------------------------------------------------
def sha12(data: bytes) -> str:
    """R1: 内容寻址 sha256[0:12]"""
    return hashlib.sha256(data).hexdigest()[:12]


def build_manifest(file_hashes: Dict[str, str]) -> str:
    """R2: canonical manifest — rows 按 path ASCII 升序,
    ensure_ascii=False, separators=(",",":"), utf-8, 无 BOM。"""
    rows = [{"path": p, "hash": file_hashes[p]} for p in sorted(file_hashes)]
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


def manifest_root(manifest_str: str) -> str:
    """R3: sha256(manifest utf-8)[0:12]"""
    return hashlib.sha256(manifest_str.encode("utf-8")).hexdigest()[:12]


def _rejection(layer: str, file: Optional[str], expected: str,
               actual: str, detail: str) -> Dict:
    return {
        "layer": layer,
        "file": file,
        "expected": expected,
        "actual": actual,
        "detail": detail,
    }


# ----------------------------------------------------------------
# v42_v2 verifier
# ----------------------------------------------------------------
class V42V2Verifier:
    """分层 verifier: L1 逐文件 / L2 manifest+根 / L3 追加式 runs 链。"""

    def __init__(self, base_dir: Path = BASE_DIR,
                 baseline_path: Path = BASELINE_PATH,
                 chain_path: Path = CHAIN_PATH):
        self.base_dir = Path(base_dir)
        self.baseline_path = Path(baseline_path)
        self.chain_path = Path(chain_path)

    # ---------------- 读取保护集 ----------------
    def read_file_map(self) -> Dict[str, bytes]:
        """从磁盘读保护集字节 (只读)。"""
        fm = {}
        for rel in PROTECTED_SET:
            p = self.base_dir / rel
            if p.is_symlink():
                raise OSError(f"E_SYMLINK: refusing to follow symlink at {rel}")
            with open(p, "rb") as f:
                fm[rel] = f.read()
        return fm

    # ---------------- 基线自举 ----------------
    def bootstrap_baseline(self, overwrite: bool = False) -> Dict:
        """首次运行: 从受保护文件实算 per-file sha12 + manifest + root 并落盘。"""
        if self.baseline_path.exists() and not overwrite:
            with open(self.baseline_path, "r", encoding="utf-8") as f:
                return json.load(f)
        fm = self.read_file_map()
        file_hashes = {rel: sha12(b) for rel, b in fm.items()}
        manifest = build_manifest(file_hashes)
        root = manifest_root(manifest)
        baseline = {
            "schema": "v42_v2_baseline/1",
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "protected_set": list(PROTECTED_SET),
            "protected_set_size": len(PROTECTED_SET),
            "file_hashes": file_hashes,
            "manifest": manifest,
            "root": root,
            "hash_spec": "sha256(bytes).hexdigest()[0:12]; manifest per fingerprint_v0 R2; root per R3",
        }
        self.baseline_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.baseline_path, "w", encoding="utf-8") as f:
            json.dump(baseline, f, indent=2, ensure_ascii=False)
        return baseline

    # ---------------- L3 链 ----------------
    def chain_head(self) -> Optional[Dict]:
        """读新链最后一条记录; 链不存在返回 None (不触旧链)。"""
        if not self.chain_path.exists():
            return None
        last = None
        with open(self.chain_path, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s:
                    last = json.loads(s)
        return last

    def append_run(self, current_root: str, manifest: str) -> Dict:
        """R4 追加: {ts, prev_hash, current_root, manifest} 到新链。"""
        head = self.chain_head()
        prev = head["current_root"] if head else GENESIS_PREV_HASH
        record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "prev_hash": prev,
            "current_root": current_root,
            "manifest": manifest,  # 扩展字段: 重放攻击后的文件级定位依据
        }
        self.chain_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.chain_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
            f.write("\n")
        return record

    def verify_chain(self) -> Dict:
        """新链完整性: genesis + 逐条 prev_hash 连续性 (沿 fingerprint_v0 V0.1 口径)。"""
        result = {"valid": True, "total_records": 0, "breaks": [],
                  "genesis_violations": [], "parse_errors": []}
        if not self.chain_path.exists():
            return result
        prev_root = None
        with open(self.chain_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                s = line.strip()
                if not s:
                    continue
                try:
                    rec = json.loads(s)
                except json.JSONDecodeError as e:
                    result["valid"] = False
                    result["parse_errors"].append(f"{self.chain_path.name}:{idx}: {e!s}")
                    continue
                result["total_records"] += 1
                got = rec.get("prev_hash", "")
                if prev_root is None:
                    if got != GENESIS_PREV_HASH:
                        result["valid"] = False
                        result["genesis_violations"].append(
                            f"{self.chain_path.name}:0: prev_hash={got!r} != GENESIS")
                elif got != prev_root:
                    result["valid"] = False
                    result["breaks"].append({
                        "record_index": idx,
                        "expected_prev_hash": prev_root,
                        "got_prev_hash": got,
                        "error_code": f"{E_L3_CHAIN_BREAK}_AT_{idx}",
                    })
                prev_root = rec.get("current_root", "")
        return result

    # ---------------- 分层验证 ----------------
    def verify(self, file_map: Optional[Dict[str, bytes]] = None,
               baseline_override: Optional[Dict] = None,
               chain_head_override: Optional[Dict] = None) -> Dict:
        """三层验证。拒绝时输出哪个文件、哪一层、期望 vs 实测。

        Args:
            file_map: 可选 {relpath: bytes} 覆盖磁盘读 (攻击模拟用);
                      值为 None 表示该文件缺失。
            baseline_override: 可选基线覆盖 (重放攻击模拟用)。
            chain_head_override: 可选链头覆盖 (重放攻击模拟用, 避免污染真实新链)。
        Returns:
            {"pass": bool, "rejections": [...], "layers_checked": [...]}
        """
        if baseline_override is not None:
            baseline = baseline_override
        else:
            with open(self.baseline_path, "r", encoding="utf-8") as f:
                baseline = json.load(f)
        if file_map is None:
            file_map = self.read_file_map()

        rejections: List[Dict] = []
        layers_checked: List[str] = []

        # ---- L1: 逐文件 SHA-256[0:12] 比对 ----
        layers_checked.append("L1")
        expected_hashes: Dict[str, str] = baseline["file_hashes"]
        actual_hashes: Dict[str, str] = {}
        l1_bad_files: List[str] = []
        all_paths = sorted(set(expected_hashes) | set(file_map))
        for rel in all_paths:
            exp = expected_hashes.get(rel)
            cur_bytes = file_map.get(rel)
            if exp is None:
                # 集合外新增文件 = 结构变化
                rejections.append(_rejection(
                    "L1", rel, "<not in protected set>", sha12(cur_bytes or b""),
                    E_L1_MISMATCH + ": unexpected file in set"))
                l1_bad_files.append(rel)
                continue
            if cur_bytes is None:
                actual_hashes[rel] = E_FILE_MISSING
                rejections.append(_rejection(
                    "L1", rel, exp, E_FILE_MISSING,
                    E_L1_MISMATCH + ": protected file missing"))
                l1_bad_files.append(rel)
                continue
            act = sha12(cur_bytes)
            actual_hashes[rel] = act
            if act != exp:
                rejections.append(_rejection(
                    "L1", rel, exp, act,
                    E_L1_MISMATCH + ": per-file sha12 mismatch"))
                l1_bad_files.append(rel)

        # ---- L2: canonical manifest + 根指纹 ----
        layers_checked.append("L2")
        # 2a. 基线自洽: root(baseline.manifest) 必须等于 baseline.root
        base_root_recomputed = manifest_root(baseline["manifest"])
        if base_root_recomputed != baseline["root"]:
            rejections.append(_rejection(
                "L2", None, baseline["root"], base_root_recomputed,
                E_L2_BASELINE_SELF_INCONSISTENT +
                ": baseline manifest/root self-inconsistent (baseline tampered)"))
        # 2b. 当前文件集 manifest 根 vs 基线根 (缺失文件不参与 manifest 时
        #     集合结构变化同样改变根)
        cur_manifest = build_manifest(
            {rel: h for rel, h in actual_hashes.items() if h != E_FILE_MISSING})
        cur_root = manifest_root(cur_manifest)
        if cur_root != baseline["root"] and not l1_bad_files:
            # L1 未定位但根不一致 (理论上仅当基线与文件集错位时发生)
            rejections.append(_rejection(
                "L2", None, baseline["root"], cur_root,
                E_L2_ROOT_MISMATCH + ": manifest root mismatch without L1 hit"))

        # ---- L3: 追加式 runs 链 — 链头根必须等于当前基线根 ----
        layers_checked.append("L3")
        head = chain_head_override if chain_head_override is not None else self.chain_head()
        if head is not None:
            if head["current_root"] != baseline["root"]:
                # 重放 / 回滚: 当前基线根 != 链头 (最近一次合法基线) 根
                detail = (E_L3_CHAIN_HEAD_MISMATCH +
                          ": baseline root != chain head root (replay/rollback suspected)")
                rejections.append(_rejection(
                    "L3", None, head["current_root"], baseline["root"], detail))
                # L3 定位: 用链头记录内的 manifest 与当前基线 manifest 做文件级 diff
                head_hashes = {r["path"]: r["hash"]
                               for r in json.loads(head.get("manifest", "[]"))}
                for rel in sorted(set(head_hashes) | set(expected_hashes)):
                    h_old = head_hashes.get(rel)
                    h_new = expected_hashes.get(rel)
                    if h_old != h_new:
                        rejections.append(_rejection(
                            "L3", rel, h_old or "<absent>", h_new or "<absent>",
                            "L3 localization: file differs vs chain-head manifest"))
        # 链为空 = 首次自举后尚未 append, 视为通过 (由 runner 负责 append)

        return {
            "pass": len(rejections) == 0,
            "rejections": rejections,
            "layers_checked": layers_checked,
        }


# ----------------------------------------------------------------
# 自验: 与 fingerprint_v0.compute_root 交叉核对 (只读复用)
# ----------------------------------------------------------------
def cross_check_with_fingerprint_v0() -> Dict:
    """用仓内 fingerprint_v0 (P-D V0 spec 实现, 只读 import) 重算保护集根,
    与 v42_v2 实算根比对。fingerprint_v0 不可用时返回 skipped。"""
    try:
        import sys
        if str(BASE_DIR) not in sys.path:
            sys.path.insert(0, str(BASE_DIR))
        import fingerprint_v0  # noqa: E402  (只读复用, 0 修改)
        abs_paths = [str(BASE_DIR / rel) for rel in PROTECTED_SET]
        ref_root = fingerprint_v0.compute_root(abs_paths)
        v42v2_root = manifest_root(build_manifest(
            {rel: sha12((BASE_DIR / rel).read_bytes()) for rel in PROTECTED_SET}))
        # fingerprint_v0 的 manifest 用调用方传入的绝对路径字符串排序,
        # v42_v2 用仓库相对 posix 路径; 两者路径口径不同则根不同, 仅比对
        # 各自 R1 文件级哈希是否一致 (内容寻址口径必须一致)。
        ref_hashes = {rel: fingerprint_v0._content_addr(str(BASE_DIR / rel))
                      for rel in PROTECTED_SET}
        v42v2_hashes = {rel: sha12((BASE_DIR / rel).read_bytes())
                        for rel in PROTECTED_SET}
        return {
            "skipped": False,
            "r1_per_file_hash_match": ref_hashes == v42v2_hashes,
            "fingerprint_v0_root_abs_path_basis": ref_root,
            "v42_v2_root_relpath_basis": v42v2_root,
            "note": ("R1 per-file content addressing must match exactly; "
                     "root differs by design when path basis differs "
                     "(abs path vs repo-relative posix path)."),
        }
    except Exception as e:  # pragma: no cover
        return {"skipped": True, "reason": repr(e)}


__all__ = [
    "PROTECTED_SET",
    "BASELINE_PATH",
    "CHAIN_PATH",
    "GENESIS_PREV_HASH",
    "sha12",
    "build_manifest",
    "manifest_root",
    "V42V2Verifier",
    "cross_check_with_fingerprint_v0",
]
