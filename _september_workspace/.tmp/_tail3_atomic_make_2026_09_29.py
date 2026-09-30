# -*- coding: utf-8 -*-
"""[V4 checkpoint 尾 3 件修订棒 | 2026-09-29] 修订件生成器 (可复算, 一次性跑)

本脚本 = 纯本地 byte 级复制 + 定点替换, 0 网络 / 0 LLM / 0 读 key / 0 跑实验。
- 3 件源件 (被引 / 归档, 仍带 checkpoint 非原子写) **逐字节只读**, 0 覆盖;
- 修订件一律**新名件** (r0_atomic / r1_atomic), 既有件 0 触动;
- 处方 = cpath_r1 同款三段式 (同目录临时件 + flush + os.fsync + os.replace),
  实现沿 results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py L546-562 同款;
- **仅改写出面**: 实验逻辑 / 阈值字面 / 常量 / cells 矩阵 / 调用面 / 返回值 0 触动。
  终端产出类写出面 (probe log / result.json / batch jsonl / OUT_RESULT / OUT_POST)
  按 52b3dec13e06 §2.3 分界原则**登记不修**, 本棒 0 触动 (沿 r2_atomic 先例)。

落盘: results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py
      results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py
      results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py
登记: .tmp/_tail3_atomic_make_2026_09_29.json
"""
import difflib
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")
STAMP = "2026-09-29"
DISPATCH = "Mavis (root session)「V4 checkpoint 尾 3 件修订棒」(PI 拍板 ask_e8c605dd1d9b662df6a33923 q2)"

P1_SRC = "results/_v4_supp_t15_executor.py"
P1_DST = "results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py"
P1_NAME = "_v4_supp_t15_executor_r0_atomic_2026_09_29.py"

P2_SRC = "results/_v4_supp_t15r2_executor.py"
P2_DST = "results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py"
P2_NAME = "_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py"

P3_SRC = "results/_archive_2026_09_24/l14_runner_v2.py"
P3_DST = "results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py"


def sha12(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def write_lines(p: Path, lines) -> None:
    p.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def set_line(lines, idx0: int, expected: str, new: str) -> None:
    got = lines[idx0]
    if got != expected:
        raise SystemExit(f"ABORT set_line idx={idx0}\n  expected={expected!r}\n  got     ={got!r}")
    lines[idx0] = new


def expect_line(lines, idx0: int, expected: str) -> None:
    got = lines[idx0]
    if got != expected:
        raise SystemExit(f"ABORT expect_line idx={idx0}\n  expected={expected!r}\n  got     ={got!r}")


def insert_at(lines, idx0: int, new_lines) -> None:
    lines[idx0:idx0] = list(new_lines)


HELPER = '''def _atomic_write_json(obj, path, indent=None):
    """原子落盘: 同目录临时件 + flush + fsync + os.replace —— 崩在半路不毁既有数据。

    沿 deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py L233-240 同款处方 (cpath_r1);
    实现同款沿 results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py L546-562。
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
        raise'''


def doc_block(dst_name, src_sha, src_bytes, face, defect, hazard, boundary, extra=()):
    """件头登记块 (落 docstring 内, 紧随件头标题行) = 身份 + 来源链 + 修复面 + 边界。"""
    b = [
        f"# {dst_name} ({STAMP} 新名件: 写侧原子写补正)",
        "# " + "=" * 88,
        f"#   源件: {src_path_of(dst_name)}",
        f"#         SHA-12 `{src_sha}` / {src_bytes:,} B  (hashlib.sha256(全文字节).hexdigest()[:12], 小写)",
        "#         —— checkpoint 被引 / 归档三件之一 (52b3dec13e06 §2.3 REGISTER_NO_FIX)",
        "#            且 0 改写面; **源件逐字节只读, 一字未改**。",
        f"#   本件: {dst_path_of(dst_name)}  (新名件; SHA-12 见登记件 + 落盘回报)",
        f"#   修复面: {face}",
        f"#   缺陷:   {defect}",
        f"#   危害:   {hazard}",
    ]
    for ln in extra:
        b.append(f"#   {ln}" if ln else "#")
    b += [
        f"#   边界:   {boundary}",
        "#           终端产出类写出面按 52b3dec13e06 §2.3 分界原则**登记不修**, 本棒 0 触动。",
    ]
    return b


def site_block(fn_old, hazard, extra=()):
    """被改写出面紧上方的处方注释块 (沿 r2_atomic 件同位置同形)。"""
    b = [
        "# ============================================================",
        f"# [写侧原子写补正 {STAMP}] 派工: {DISPATCH}",
        f"#   缺陷: `{fn_old}` 为**非原子全量覆盖写** (write_text 直接覆盖目标路径本身) ⇒",
        f"#         {hazard}",
        "#   修法: 同目录临时件 (名带 pid) + f.flush() + os.fsync(f.fileno())",
        "#           + os.replace(tmp, path) (同卷原子替换) —— 三段式。",
        "#   处方: cpath_r1 同款 (deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py L233-240),",
        "#         实现沿 results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py L546-562。",
        "#   边界: 0 改实验逻辑 / 0 改调用面 / 0 改返回值 / 0 改阈值字面 / 0 改 records 结构 /",
        "#         0 改 paths; 落盘字节与补正前**逐字节同构** (同 json.dumps 参数, 仅写入经由临时件)。",
    ]
    for ln in extra:
        b.append(f"#   {ln}" if ln else "#")
    b.append("# ============================================================")
    return b


_SRC_DST = {
    "_v4_supp_t15_executor_r0_atomic_2026_09_29.py": (P1_SRC, P1_DST),
    "_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py": (P2_SRC, P2_DST),
}


def src_path_of(name: str) -> str:
    return _SRC_DST[name][0] if name in _SRC_DST else P3_SRC


def dst_path_of(name: str) -> str:
    return _SRC_DST[name][1] if name in _SRC_DST else P3_DST


def make_p1():
    src, dst = REPO / P1_SRC, REPO / P1_DST
    raw = src.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    n0 = len(lines)

    set_line(lines, 2, "_v4_supp_t15_executor.py", P1_NAME)

    site = site_block(
        "save_checkpoint(records) -> CHECKPOINT_PATH (.tmp/_t15_records.json)",
        "崩半路留半写截断文件, 而 loader 侧只报「不可读」不报「为何不可读」。",
        extra=(
            "本件**非执行面** (t15 系执行面 = r3 件, 见 3bc852e0d48b §9.6);",
            "读侧面沿源件 (无 F1 告警) —— 本棒**只改写出面**。",
        ),
    )
    new_save = [
        *site,
        HELPER,
        "",
        "",
        "def save_checkpoint(records: List[Dict[str, Any]]) -> None:",
        f'    """[写侧原子写补正 {STAMP}] 改前 = write_text 全量覆盖 (非原子); 改后 = 临时件 + flush + fsync + os.replace。"""',
        "    _atomic_write_json(records, CHECKPOINT_PATH)",
    ]
    # 源件相对索引: 先补写出面 (再插件头块, 避免索引漂移)
    expect_line(lines, 441, "def save_checkpoint(records: List[Dict[str, Any]]) -> None:")
    expect_line(lines, 442, "    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)")
    expect_line(lines, 443, "    CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False),")
    expect_line(lines, 444, '                               encoding="utf-8")')
    lines[441:445] = new_save

    insert_at(lines, 4, doc_block(
        P1_NAME, sha12(raw), len(raw),
        face="**仅 1 处** = `save_checkpoint()` (源件 L442-445), 目标 `.tmp/_t15_records.json`。",
        defect="`CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False), encoding=\"utf-8\")` = 非原子全量覆盖写。",
        hazard="`.tmp/_t15_records.json` = 120 条 T1.5 状态锚 (被 `load_checkpoint()` 读回决定\nskip / 续跑); 崩半路 ⇒ 半写截断文件 ⇒ 续跑重复计 calls 账 / 静默丢已跑数据。",
        boundary="0 改实验逻辑 / 0 改调用面 / 0 改返回值 / 0 改阈值字面 (K_N11_3_THRESHOLD=0.85 /\nK_N11_1_DIFF=0.05 / K_N11_2_DELTA=0.05 / TH-T1-1=10) / 0 改 cells 矩阵 / 0 改\nN_REASKS / 0 改 kill-line / 0 改 records 结构 / 0 改 paths。",
        extra=(
            "本件**非执行面**: t15 系执行面 = `_v4_supp_t15_executor_r3_2026_09_28.py`\n"
            "(`b86cce242abe`, 见 3bc852e0d48b §9.6); 本件只补**基名代**写侧原子面。\n"
            "读侧面: 本件**无 F1 响亮告警** (与源件同: `except Exception: return []` 静默);\n"
            "F1 只在 r1 / r2_atomic / r3 线 ⇒ **执行面不受影响** (r3 = 读写两侧齐备)。",
        ),
    ))

    return src, dst, raw, lines, n0


def make_p2():
    src, dst = REPO / P2_SRC, REPO / P2_DST
    raw = src.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    n0 = len(lines)

    set_line(lines, 2, "_v4_supp_t15r2_executor.py", P2_NAME)

    site = site_block(
        "save_t15r2_records(r2_records) -> T15R2_CHECKPOINT_PATH (.tmp/_t15r2_records.json)",
        "崩半路留半写截断文件 = 读侧静默 `[]` 的触发源 (R1 件 L477-479 自述 (c) 面)。",
        extra=(
            "本件**非执行面** (t15r2 系执行面 = r3 件, 见 3bc852e0d48b §9.6);",
            "读侧面沿源件 (无 F1 告警) —— 本棒**只改写出面**。",
        ),
    )
    new_save = [
        *site,
        HELPER,
        "",
        "",
        "def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:",
        f'    """[写侧原子写补正 {STAMP}] 改前 = write_text 全量覆盖 (非原子); 改后 = 临时件 + flush + fsync + os.replace。"""',
        "    _atomic_write_json(r2_records, T15R2_CHECKPOINT_PATH)",
    ]
    # 源件相对索引: 先补写出面 (再插件头块, 避免索引漂移)
    expect_line(lines, 467, "def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:")
    expect_line(lines, 468, "    T15R2_CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)")
    expect_line(lines, 469, "    T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False),")
    expect_line(lines, 470, '                                     encoding="utf-8")')
    lines[467:471] = new_save

    insert_at(lines, 4, doc_block(
        P2_NAME, sha12(raw), len(raw),
        face="**仅 1 处** = `save_t15r2_records()` (源件 L468-471), 目标 `.tmp/_t15r2_records.json`。",
        defect="`T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False), ...)` = 非原子全量覆盖写。",
        hazard="`.tmp/_t15r2_records.json` = 62 条 T1.5r2 records 唯一落盘面; 崩半路 ⇒ 半写文件 ⇒\n`load_t15r2_records()` 静默 `[]` ⇒ `cmd_aggregate` 照常产出 result.json, 但\n`records_all` 少掉 T1.5r2 全集 ⇒ K-N11-N1_T1relax 的 N_min=10 字面 PASS 根因消除结论\n被无声抽掉, 字面读起来仍像「已跑完」。",
        boundary="0 改实验逻辑 / 0 改调用面 / 0 改返回值 / 0 改阈值字面 (0.85 / 0.05 / 0.05 /\nTH-T1-1=10) / 0 改 N_REASKS / 0 改 cells 矩阵 / 0 改 kill-line / 0 改 records\n结构 / 0 改 paths。",
        extra=(
            "本件**非执行面**: t15r2 系执行面 = `_v4_supp_t15r2_executor_r3_2026_09_28.py`\n"
            "(`4f514b3fb4b8`, 见 3bc852e0d48b §9.6); 本件只补**基名代**写侧原子面。\n"
            "读侧面: 本件**无 F1 响亮告警** (与源件同: `load_t15_records` / `load_t15r2_records`\n"
            "两处 `except Exception: return []` 静默); F1 只在 r1 / r2_atomic / r3 线 ⇒\n"
            "**执行面不受影响** (r3 = 读写两侧齐备)。",
        ),
    ))
    return src, dst, raw, lines, n0


def make_p3():
    src, dst = REPO / P3_SRC, REPO / P3_DST
    raw = src.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    n0 = len(lines)

    head = [
        "# ============================================================",
        f"# [写侧原子写补正 {STAMP}] 派工: {DISPATCH}",
        f"#   源件: {P3_SRC}",
        f"#         SHA-12 `{sha12(raw)}` / {len(raw):,} B  (hashlib.sha256(全文字节).hexdigest()[:12], 小写)",
        "#         —— 归档件 (52b3dec13e06 §2.3 REGISTER_NO_FIX 三件之一; 被 L14 verdict §9.1 引用);",
        "#            **源件逐字节只读, 一字未改**。",
        f"#   本件: {P3_DST}  (新名件; SHA-12 见登记件 + 落盘回报)",
        "#   缺陷面: **2 处, 同一 checkpoint 变量** = 源件 L153 (逐 call 存) + L168 (收尾存),",
        "#           目标 `.tmp/_l14_records.json`;",
        "#           写法 `CHECKPOINT.write_text(json.dumps(records, ...), encoding=\"utf-8\")` = 非原子全量覆盖写。",
        "#   危害面: `.tmp/_l14_records.json` = L14 续跑状态锚 (读回决定哪些 (teacher, prompt, reask) 已跑);",
        "#           崩半路 ⇒ 半写截断文件 ⇒ 续跑重复计 calls 账 / 静默丢已跑数据。",
        "#   修法:   同目录临时件 (名带 pid) + f.flush() + os.fsync(f.fileno())",
        "#           + os.replace(tmp, path) (同卷原子替换) —— 三段式。",
        "#   处方:   cpath_r1 同款 (deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py L233-240),",
        "#           实现沿 results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py L546-562。",
        "#   边界:   0 改实验逻辑 / 0 改调用面 / 0 改返回值 / 0 改阈值字面 / 0 改 records 结构 /",
        "#           0 改 paths / **0 改 L153 外层 `try/except` 与 `checkpoint FAIL` 打印 (逐字不动)** /",
        "#           0 改 L490 `OUT_RESULT` 与 L523 `OUT_POST` 终端产出面 (登记不修, 沿 52b3dec13e06 §2.3)。",
        "#   读侧面: 本件沿源件 (无 F1 告警); 归档件不在执行面 ⇒ 影响面 0。",
        "# ============================================================",
        HELPER,
        "",
    ]
    insert_at(lines, 51, head)   # 紧接 L50 `CHECKPOINT = Path(...)` + L51 空行

    set_line(lines, 152 + len(head),
             '            CHECKPOINT.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")',
             "            _atomic_write_json(records, CHECKPOINT)")
    set_line(lines, 167 + len(head),
             'CHECKPOINT.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")',
             "_atomic_write_json(records, CHECKPOINT)")
    return src, dst, raw, lines, n0


def diff_report(src_lines, dst_lines):
    ops = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, src_lines, dst_lines, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        ops.append({
            "tag": tag,
            "src_lines_1based": [i1 + 1, i2],
            "dst_lines_1based": [j1 + 1, j2],
            "src_removed": src_lines[i1:i2],
            "dst_added": dst_lines[j1:j2],
        })
    return ops


def main() -> int:
    out = {
        "generated_by": "Mavis 团队 worker (agent: worker)",
        "date": STAMP,
        "dispatch": DISPATCH,
        "note": "纯本地 byte 级复制 + 定点替换; 0 网络 / 0 LLM / 0 读 key / 0 跑实验 / 0 覆盖既有件。",
        "items": [],
    }
    for fn in (make_p1, make_p2, make_p3):
        src, dst, raw, lines, n0 = fn()
        before = src.read_bytes()          # 构造前复算
        write_lines(dst, lines)
        after = src.read_bytes()           # 构造后复算 (0 触动实证)
        raw_new = dst.read_bytes()
        dst_lines = raw_new.decode("utf-8").splitlines()
        ops = diff_report(raw.decode("utf-8").splitlines(), dst_lines)
        out["items"].append({
            "src": str(src.relative_to(REPO)).replace("\\", "/"),
            "src_bytes": len(raw),
            "src_sha12_before": sha12(raw),
            "src_sha12_after": sha12(after),
            "src_untouched": sha12(raw) == sha12(after) and before == after,
            "dst": str(dst.relative_to(REPO)).replace("\\", "/"),
            "dst_bytes": len(raw_new),
            "dst_sha12": sha12(raw_new),
            "src_lines": n0,
            "dst_lines": len(dst_lines),
            "bom": raw_new[:3] == b"\xef\xbb\xbf",
            "cr_count": raw_new.count(b"\r"),
            "changed_hunks": len(ops),
            "diff": ops,
        })
    (REPO / ".tmp" / "_tail3_atomic_make_2026_09_29.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    for it in out["items"]:
        print(f"SRC {it['src']}  {it['src_bytes']:,} B / {it['src_sha12_before']}"
              f"  -> after {it['src_sha12_after']}  untouched={it['src_untouched']}")
        print(f"DST {it['dst']}  {it['dst_bytes']:,} B / {it['dst_sha12']}"
              f"  lines {it['src_lines']}->{it['dst_lines']}  hunks={it['changed_hunks']}"
              f"  CR={it['cr_count']}  BOM={it['bom']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
