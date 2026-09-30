# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 修复件生成：checkpoint 非原子写 → 原子写（cpath_r1 同款处方）。

产物（新名件，0 覆盖）：
  results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py   ← _r1 (e0936a68fa82)
  results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py     ← _r1 (6d22444c65af)

被引原件逐字节不动（被引件登记不修，见派工单口径）。
0 LLM / key 永不明文 / 0 改实验逻辑 / 0 改返回值 / 0 改阈值字面。
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("D:/私人资料/deposon-repo")
RESULTS = ROOT / "results"

ATOMIC_HELPER = '''
# ============================================================
# [R2 原子写修复, 2026-09-28] cpath_r1 同款处方
#   缺陷: checkpoint 落盘为非原子全量覆盖写 (write_text 直接覆盖)
#         → 进程被杀 / 断电 / 磁盘写满 即留半写截断文件,
#           而 loader 侧 R1 告警只报告「不可读」不报告「为何不可读」。
#   修法: 同目录临时件 + flush + os.fsync + os.replace (同卷原子替换)
#         ⇒ 要么全量新内容, 要么**原内容一字不动**, 崩在半路不毁既有数据。
#   边界: 0 改实验逻辑 / 0 改调用面 / 0 改返回值 / 0 改阈值字面 /
#         0 改 records 结构 / 0 改 paths。落盘字节与修复前**逐字节同构**
#         (同 json.dumps 参数, 仅写入经由临时件)。
# ============================================================
def _atomic_write_json(obj: Any, path: Path, indent: Optional[int] = None) -> None:
    """原子落盘: 同目录临时件 + fsync + os.replace —— 崩在半路不毁既有数据。

    沿 deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py L233-240 同款处方。
    临时件名带 pid ⇒ 并发进程互不踩踏 (双跑不互毁)。
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.tmp_{os.getpid()}")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)   # 同卷原子替换: 要么全量新内容, 要么原内容
    except BaseException:
        # 写失败/被杀: 既有数据一字不动; 临时件留场供事后取证, 不静默吞。
        raise

'''

FIX_NOTE_R2 = """#
# ============================================================
# [R2 原子写修复, 2026-09-28] 派工: Mavis (root session)「收口修复+清理棒」
#   处方 = cpath_r1 同款 (临时件 + fsync + os.replace), 见下方 _atomic_write_json。
#   本件 = **新名件**, 由 R1 件逐字节复制 + 仅改 checkpoint 写函数而成;
#          被引原件一字不动 (被引件登记不修)。
#   与 R1 的关系: R1 修「读侧静默失败」(响亮告警), R2 修「写侧非原子覆盖」
#          —— 二者互补: R1 让损坏**可见**, R2 让损坏**不发生**。
#   验证: 见 results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md §2
#          (双跑不互毁 + 崩半路数据不动, 两项均实测通过)。
# ============================================================
#"""

JOBS = [
    {
        "src": RESULTS / "_v4_supp_t15r2_executor_r1_2026_09_28.py",
        "dst": RESULTS / "_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
        "old": '''def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:
    T15R2_CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False),
                                     encoding="utf-8")
''',
        "new": '''def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:
    """[R2 原子写] 改前 = write_text 全量覆盖 (非原子); 改后 = 临时件+fsync+os.replace。"""
    _atomic_write_json(r2_records, T15R2_CHECKPOINT_PATH)
''',
        # 缺陷块 (c) 说「本棒只登记不修」→ 改前留原字面, 由 R2 说明块在其后追加
        "anchor": "#   4. 告警路径**永不 raise** —— 修复本身不得引入新的失败面 (日志写失败也只提示)。\n#\n",
        "defect": "(c) `save_t15r2_records` 为**非原子写**",
    },
    {
        "src": RESULTS / "_v4_supp_t15_executor_r1_2026_09_27.py",
        "dst": RESULTS / "_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
        "old": '''def save_checkpoint(records: List[Dict[str, Any]]) -> None:
    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False),
                               encoding="utf-8")
''',
        "new": '''def save_checkpoint(records: List[Dict[str, Any]]) -> None:
    """[R2 原子写] 改前 = write_text 全量覆盖 (非原子); 改后 = 临时件+fsync+os.replace。"""
    _atomic_write_json(records, CHECKPOINT_PATH)
''',
        "anchor": None,
        "defect": None,
    },
]


def sha12(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def main():
    report = []
    for job in JOBS:
        src, dst = job["src"], job["dst"]
        assert not dst.exists(), f"新名件已存在, 拒绝覆盖: {dst}"
        src_bytes = src.read_bytes()
        text = src_bytes.decode("utf-8")

        # 1) 原子写助手插在 save 函数之前
        assert text.count(job["old"]) == 1, f"save 函数定位失败: {src.name}"
        text = text.replace(job["old"], ATOMIC_HELPER.lstrip("\n") + "\n" + job["new"], 1)

        # 2) R2 说明块插在 R1 缺陷块之后 (仅 t15r2 件有显式登记锚)
        if job["anchor"]:
            assert text.count(job["anchor"]) == 1, f"缺陷块锚定位失败: {src.name}"
            text = text.replace(job["anchor"], job["anchor"] + FIX_NOTE_R2, 1)
        else:
            # 无显式缺陷块锚者: 插在 R1 告警块常量之后。逐行补回 `#` 前缀
            # (FIX_NOTE_R2 首行 `#` 为分隔线, 不可参与 lstrip)。
            anchor = "CHECKPOINT_WARNINGS: List[Dict[str, Any]] = []\n"
            assert text.count(anchor) == 1, f"告警块锚定位失败: {src.name}"
            note = "\n".join(
                line if line.startswith("#") else "#" + line
                for line in FIX_NOTE_R2.splitlines()
            )
            text = text.replace(anchor, anchor + "\n" + note + "\n", 1)

        dst_bytes = text.encode("utf-8")
        dst.write_bytes(dst_bytes)
        report.append({
            "src": src.relative_to(ROOT).as_posix(),
            "src_bytes": len(src_bytes), "src_sha12": sha12(src_bytes),
            "dst": dst.relative_to(ROOT).as_posix(),
            "dst_bytes": len(dst_bytes), "dst_sha12": sha12(dst_bytes),
        })
        print(f"NEW  {dst.relative_to(ROOT).as_posix()}")
        print(f"     {len(dst_bytes):7d} B  sha12={sha12(dst_bytes)}"
              f"   (源 {src.name}: {len(src_bytes)} B / {sha12(src_bytes)})")

    # 3) 复验原件逐字节未动
    print("--- 原件 0 触动复验 ---")
    for j, job in zip(report, JOBS):
        b = job["src"] and job["src"].read_bytes()
        ok = sha12(b) == j["src_sha12"] and len(b) == j["src_bytes"]
        print(f"  {'OK ' if ok else 'FAIL'} {job['src']}  {j['src_sha12']}  {j['src_bytes']} B")

    out = ROOT / ".tmp/_cpatomic_patch_manifest_2026_09_28.json"
    out.write_text(json.dumps({"schema": "v4_cpatomic_patch/1", "date": "2026-09-28",
                               "jobs": report}, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"OUT -> {out}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        idx = [int(x) for x in sys.argv[1].split(",")]
        JOBS = [JOBS[i] for i in idx]
        print(f"仅重跑 job idx={idx}")
    main()
