#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F2 分支修复棒 · 机械改写脚本 v2（scratch · .tmp/ · 非交付件）

源件：results/_v3_recheck_26b_executor_r3_2026_09_29.py（6c83e7a7ca2e，只读）
产出：results/_f2_reading_b_runner_2026_09_29.py（PI 2026-09-29 22:44 授权另立的新名 runner）

v2 相对 v1 的唯一差别：字面替换改为**行区间锚点替换**（唯一起始锚 + 唯一结束锚），
消除手工缩进转录风险。纪律不变：fail-closed / 0 改源件 / 判据面 0 改动。
"""
import ast
import difflib
import hashlib
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "results/_v3_recheck_26b_executor_r3_2026_09_29.py"
DST = REPO / "results/_f2_reading_b_runner_2026_09_29.py"

SESSION = "mvs_6d1226a6a8e246adb652741216e8c95f"

# ---------------------------------------------------------------- 替换块定义
# 每项 = (标签, 起始锚, 结束锚, 新块文本)
BLOCKS = [
    # ---- 1. 件头（插入授权与谱系块；r3 原标题行下移保留） ----
    ("件头",
     'V3-R #26 P-J 收敛盆地 — 三本体正式实验 executor（**26b r3 修订版** · worker · 2026-09-29）',
     'V3-R #26 P-J 收敛盆地 — 三本体正式实验 executor（**26b r3 修订版** · worker · 2026-09-29）',
     [
         'V3-R #26 P-J 收敛盆地 — 三本体正式实验 executor（**F2 读法乙新名 runner** · worker · 2026-09-29）',
         '',
         '**本件 = PI 2026-09-29 22:44 授权另立的新名 runner**（授权：`ask_1aca8ed0bef608fff8298b2c` Q3',
         '「授权改实现」＋「另立新名 runner」；**盘上 0 原始记录**，本件按 E-C 派工单转述登记，',
         '不冒充问卷原件）。',
         '',
         '**为何在既有 r3 件之后仍另立本件（老实交代 · 非开脱）**：F2 分支（`n_distinct > 3 ∧ std > 0`）',
         '按读法乙落 **FAIL + γ** 这一**语义**已由 r3 件 `6c83e7a7ca2e`（09-29 10:50 落盘）实现，',
         '且已于 **19:08:57** 产出首份读法乙读数 `c9d3c9f819f1`（PI 裁 B）。但 r3 件自载的授权',
         '（PI 09-29 10:44 · `ask_90009bd33020f0b43a270672` q1）为**盘上 0 原始记录的转述**',
         '⇒ 本件以 **22:44 在案授权**补授权溯源。',
         '',
         '**本件相对 r3 的改动面（逐条 · 判据面 0 差异）**：',
         '  1. 件头：本块授权与谱系说明（r3 原标题行**逐字保留**于下方，0 改写）；',
         '  2. `OUT` → 落**新名** `results/_f2_reading_b_result_2026_09_29.json`（0 覆写 26b 原派生件 /',
         '     r2 派生件 / r3 派生件 `c9d3c9f819f1`；0 合并派生 JSON）；',
         '  3. payload 溯源面（`revision` / `revision_lineage` / `revision_of` / 署名 / `runtime` /',
         '     `verdict_note` / 读法乙注记）指向 22:44 授权；',
         '  4. stdout 标签 `[26b-r3]` → `[F2-rB]`（11 处）。',
         '',
         '**未改动面（逐条）**：`judge_K_V3R_26` **全部四枝 + KD 拦截**逐字沿 r3；`KILL_LINE_LITERAL` /',
         '`TH_LITERAL` 逐字 0 改动；构造常数（`SEED` / `N_BUDGET` / `JITTER` / `N_CELLS` / `CLASSES` /',
         '`PRIORITY` / `TOL` / `O1_MAX_STEP` / `O3_*` / `O5_*`）逐字 0 改动；判据切点（`n > 3` /',
         '`std > 0` / `n ≤ 1`）一字不动；O1/O3/O5 求解器 / `draw_perturbation` / `stat_block` /',
         '`spearman` / `ols_r2` 逐字 0 改动。',
         '',
         '**0 回溯**：r3 派生件与其 19:08 读数、as-run 3/3 PASS 历史读数，**全部维持原判、byte 0 触动**',
         '（沿生效登记件 §3.4 `K-V5RB-E-3` 0 回溯）。',
         '',
         '（↓ 以下为 r3 件原头，逐字沿 `_v3_recheck_26b_executor_r3_2026_09_29.py`，供谱系追溯）',
         'V3-R #26 P-J 收敛盆地 — 三本体正式实验 executor（**26b r3 修订版** · worker · 2026-09-29）',
     ]),

    # ---- 2. OUT 常量 ----
    ("OUT",
     '# r3：同样落**新名**派生件，0 覆写 r2 派生件（防覆写历史派生件）',
     'OUT = REPO / "results/_v3_recheck_26b_r3_result_2026_09_29.json"',
     [
         '# r3：同样落**新名**派生件，0 覆写 r2 派生件（防覆写历史派生件）',
         '# F2 新名 runner（PI 2026-09-29 22:44 授权）：再落**新名**派生件，0 覆写 26b 原派生件 /',
         '#   r2 派生件 / r3 派生件（_v3_recheck_26b_r3_result_2026_09_29.json · c9d3c9f819f1 ·',
         '#   19:08:57 · PI 裁 B 读数）—— 0 合并、0 覆写',
         'OUT = REPO / "results/_f2_reading_b_result_2026_09_29.json"',
     ]),

    # ---- 3. payload：date + revision + lineage ----
    ("revision",
     '"date_r3": "2026-09-29",',
     '"0 新设阈值、0 新增第四态、0 回溯、0 回改既有件）"),',
     [
         '"date_r3": "2026-09-29",',
         '        "date_f2_runner": "2026-09-29（PI 22:44 授权 · 新名 runner）",',
         '        "revision": ("F2 读法乙新名 runner · 判据面逐字沿 r3（6c83e7a7ca2e）· 改动面 = 件头溯源 + "',
         '                     "输出新名 + stdout 标签 + 署名出处（PI 2026-09-29 22:44 授权改实现、另立新名 "',
         '                     "runner · ask_1aca8ed0bef608fff8298b2c Q3 · 派工单转述）；F2 分支语义"',
         '                     "（读法乙 ⇒ 归属表 v2 全域 FAIL；真分布域 PASS 翻 FAIL + γ 沿 K-V5RB-0-D "',
         '                     "强制改写）由 r3 件首次实现，本件 0 改写；0 新设阈值、0 新增第四态、0 回溯、"',
         '                     "0 回改既有件）"),',
         '        "revision_lineage": [',
         '            {"piece": "results/_v3_recheck_26b_executor_2026_09_27.py", "sha12": "5c906113a210",',
         '             "role": "原始件 · F2 分支 PASS 字面（读法甲）原样保留 · byte 0 触动"},',
         '            {"piece": "results/_v3_recheck_26b_executor_r2_2026_09_28.py", "sha12": "0808af6212c5",',
         '             "role": "r2 修订件 · 字面空档两枝终局化 · byte 0 触动"},',
         '            {"piece": "results/_v3_recheck_26b_executor_r3_2026_09_29.py", "sha12": "6c83e7a7ca2e",',
         '             "role": "r3 修订件 · **F2 分支读法乙语义首次实现**（PI 09-29 10:44 转述授权）· byte 0 触动"},',
         '            {"piece": "results/_f2_reading_b_runner_2026_09_29.py", "sha12": "(本件 · 见交付回执)",',
         '             "role": "F2 读法乙新名 runner · PI 09-29 22:44 授权 · 判据面与 r3 逐字等价"},',
         '        ],',
     ]),

    # ---- 4. payload：revision_of 指向 r3 ----
    ("revision_of",
     '            "path": "results/_v3_recheck_26b_executor_r2_2026_09_28.py",',
     '            "sha12": "0808af6212c5",',
     [
         '"path": "results/_v3_recheck_26b_executor_r3_2026_09_29.py",',
         '            "sha12": "6c83e7a7ca2e",',
     ]),

    # ---- 5. payload：changed_surface 追加本棒改动面 ----
    ("changed_surface",
     '"changed_surface": ("仅 judge_K_V3R_26 的 **F2 分支**（n_distinct>3 且 std>0：PASS → FAIL + "',
     '"种子/预算/抖动全未触动"),',
     [
         '"changed_surface": ("r2→r3 沿革：仅 judge_K_V3R_26 的 **F2 分支**（n_distinct>3 且 std>0：PASS → FAIL + "',
         '                                "γ 改写，kill_line_fail_hit / kill_line_pass 随之翻转）+ 随之失效的',
         '                                "kill_line_fail_hit / kill_line_pass 随之翻转）+ 随之失效的',
         '                                "登记表述（gamma_source / dual_caliber_consistency / summary 分支 / "',
         '                                "档位元数据 / 输出路径 / 件头说明）；判死线字面、构造常数、本体实现、"',
         '                                "种子/预算/抖动全未触动"),',
         '            "changed_surface_of_this_piece": ("r3→本件**仅改**：件头授权与谱系块、OUT 输出新名、"',
         '                                              "payload 溯源面（revision / revision_lineage / "',
         '                                              "revision_of / 署名 / runtime / verdict_note / "',
         '                                              "读法乙注记 / upstream 列表）、stdout 标签 "',
         '                                              "[26b-r3]→[F2-rB]；**judge_K_V3R_26 四枝与 KD 拦截、"',
         '                                              "判死线字面、构造常数、切点、求解器全部逐字 0 改动**"',
         '                                              "（等价性自测见 results/_f2_branch_fix_register_'
         '2026_09_29.md §4）"),',
     ]),

    # ---- 6. payload：upstream_untouched 追加 r3 ----
    ("upstream",
     '{"path": "results/_v3_recheck_26b_executor_r2_2026_09_28.py", "sha12": "0808af6212c5",',
     '"byte_0_touched": True, "note": "r2 修订件，空档两枝终局化原样保留"},',
     [
         '{"path": "results/_v3_recheck_26b_executor_r2_2026_09_28.py", "sha12": "0808af6212c5",',
         '                 "byte_0_touched": True, "note": "r2 修订件，空档两枝终局化原样保留"},',
         '                {"path": "results/_v3_recheck_26b_executor_r3_2026_09_29.py",',
         '                 "sha12": "6c83e7a7ca2e",',
         '                 "byte_0_touched": True,',
         '                 "note": "r3 修订件，F2 分支读法乙语义首次实现；本件判据面沿之"},',
     ]),

    # ---- 7. payload：署名 ----
    ("produced_by",
     '"produced_by_r3": "Mavis 团队 worker（session mvs_ce8c37cbf1944b19800d7c3a28543591；"',
     '"如实署名，不冒充 PI / protocol-keeper / verdict-keeper / evidence-auditor / verifier）",',
     [
         '"produced_by_f2_runner": ("Mavis 团队 worker（session __SESSION__；',
         '                                  "PI 2026-09-29 22:44 授权改实现 + 另立新名 runner · "',
         '                                  "ask_1aca8ed0bef608fff8298b2c Q3 · **派工单转述 · 盘上 0 原始记录**；"',
         '                                  "如实署名，不冒充 PI / protocol-keeper / verdict-keeper / "',
         '                                  "evidence-auditor / verifier / doc-writer / r3 棒出证方 "',
         '                                  "mvs_ce8c37cbf1944b19800d7c3a28543591）"),',
         '        "f2_semantic_author": ("F2 分支（n_distinct>3 且 std>0 ⇒ FAIL + γ 沿 K-V5RB-0-D）由 "',
         '                               "**r3 件** 6c83e7a7ca2e 首次实现（PI 09-29 10:44 转述授权）；"',
         '                               "本件 0 改写该语义，仅补 22:44 授权溯源"),',
         '        "r3_reading_intact": ("r3 派生件 results/_v3_recheck_26b_r3_result_2026_09_29.json"',
         '                              "（c9d3c9f819f1 · 54,294 B · 19:08:57 · PI 裁 B 产出）"',
         '                              "维持原判、byte 0 触动、0 回溯（沿生效登记件 §3.4）"),',
     ]),

    # ---- 8. payload：读法乙注记（首读数事实） ----
    ("not_run",
     '"not_run_this_turn": ("**本件未跑全量**',
     '"混同）。派生 JSON 由届时重跑产出，本 Turn 0 落 JSON"),',
     [
         '"lineage_of_first_reading": ("F2 语义首份读数**已产出**：r3 派生件 "',
         '                                         "_v3_recheck_26b_r3_result_2026_09_29.json"',
         '                                         "（c9d3c9f819f1 · 19:08:57 · PI 裁 B「重跑并落盘」）；"',
         '                                         "本件为 22:44 授权下的新名 runner，**尚未跑全量**"',
         '                                         "（跑不跑属读数生产决策，须 PI / verdict-keeper 另派）"),',
     ]),

    # ---- 9. payload：runtime ----
    ("runtime",
     '"runtime": ("0 LLM; numpy + hashlib + json only; no network; read-only inputs; 0 改动既有件"',
     '"触动，本件落新名派生件 _v3_recheck_26b_r3_result_2026_09_29.json）"),',
     [
         '"runtime": ("0 LLM; numpy + hashlib + json only; no network; read-only inputs; "',
         '                    "0 改动既有件（源件 5c906113a210、r2 件 0808af6212c5、r3 件 6c83e7a7ca2e、"',
         '                    "26b 原派生件、r3 派生件 c9d3c9f819f1 均 byte 0 触动；本件落新名派生件 "',
         '                    "_f2_reading_b_result_2026_09_29.json）"),',
     ]),

    # ---- 10. payload：verdict_note ----
    ("verdict_note",
     '"verdict_note": ("正式判定档：本件出 K-V3R-26 逐本体正式 verdict',
     '（K-V5RB-0-K 已授权改实现，本件为授权后首个实现面）。"),',
     [
         '"verdict_note": ("正式判定档：本件出 K-V3R-26 逐本体正式 verdict（3 本体独立判定）+ "',
         '                         "双口径并报。**读法乙注记**：本读数域内 PASS 档已全域消失（归属表 v2）"',
         '                         "⇒ new_verdict 预期恒为 FAIL；若出现 PASS 即为异常取值，须 γ 升级"',
         '                         "（K-V5RB-0-K 已授权改实现；授权后首个实现面为 r3 件 6c83e7a7ca2e，"',
         '                         "本件为 PI 2026-09-29 22:44 授权下的新名 runner，判据面与之逐字等价）"),',
     ]),
]

STDOUT_OLD = "[26b-r3]"
STDOUT_NEW = "[F2-rB]"
STDOUT_EXPECT = 11


def find_block(lines, start_anchor, end_anchor, used):
    """唯一起始锚定位行区间；起始/结束锚都必须未被前序块占用。"""
    si = [i for i, ln in enumerate(lines) if start_anchor in ln and i not in used]
    if len(si) != 1:
        sys.exit("[FAIL] 起始锚命中 %d 次（期望 1）：%r" % (len(si), start_anchor))
    i = si[0]
    ei = [k for k, ln in enumerate(lines) if k >= i and end_anchor in ln]
    if not ei:
        sys.exit("[FAIL] 结束锚未命中：%r" % end_anchor)
    j = ei[0]
    for k in range(i, j + 1):
        used.add(k)
    return i, j


def slice_between(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


def main() -> int:
    src_bytes = SRC.read_bytes()
    src_text = src_bytes.decode("utf-8")
    if "\r\n" in src_text or src_bytes.startswith(b"\xef\xbb\xbf"):
        sys.exit("[FAIL] 源件行尾/BOM 异常，停止")
    if DST.exists():
        sys.exit("[FAIL] 目标新名件已存在（撞名风险）—— 停止，0 覆写")

    src_lines = src_text.split("\n")

    # stdout 标签先改（此时文本 == 源件，故命中数 = 源件真实处数 11；块改写后计数会被说明文字污染）
    n_std = src_text.count(STDOUT_OLD)
    if n_std != STDOUT_EXPECT:
        sys.exit("[FAIL] 源件 stdout 标签命中 %d 次（期望 %d）—— 停止，0 落盘" % (n_std, STDOUT_EXPECT))
    src_text = src_text.replace(STDOUT_OLD, STDOUT_NEW)
    src_lines = src_text.split("\n")

    used = set()
    edits = []
    for name, sa, ea, new in BLOCKS:
        i, j = find_block(src_lines, sa, ea, used)
        # 首行缩进自动带出：若新块首行未带原行前导空白，则补之（消除手写缩进漂移）
        orig0 = src_lines[i]
        pre = orig0[:len(orig0) - len(orig0.lstrip())]
        if pre and not new[0].startswith(pre):
            new = [pre + new[0]] + list(new[1:])
        edits.append((i, j, new, name))
        print("[transform] 块 %-14s L%d-L%d（%d 行 → %d 行）" % (name, i + 1, j + 1, j - i + 1, len(new)))
    edits.sort(key=lambda e: e[0], reverse=True)

    out_lines = list(src_lines)
    for i, j, new, name in edits:
        out_lines[i:j + 1] = new
    out = "\n".join(out_lines)

    out = out.replace("__SESSION__", SESSION)
    if "__SESSION__" in out:
        sys.exit("[FAIL] session 占位符未全部替换")

    # 判据面 0 差异硬门（5 处切片逐字比对）
    for a_s, a_e, tag in [
        ("def judge_K_V3R_26(", "\n\ndef draw_block", "judge_K_V3R_26 全函数"),
        ("GAMMA_ROOT_CAUSE_READING_B = ", "\n\n# ---- 防退化门", "γ 字面常量块"),
        ("# ---- 冻结构造常量", "\n\n# ---- K-V3R-26 字面阈值", "构造常量块"),
        ("# ---- K-V3R-26 字面阈值", "\n\n# ---- 强制 γ 根因字面", "阈值常量块"),
        ("KILL_LINE_LITERAL = ", "\nTH_LITERAL = ", "KILL_LINE_LITERAL"),
    ]:
        if slice_between(src_text, a_s, a_e) != slice_between(out, a_s, a_e):
            sys.exit("[FAIL] 判据/构造面出现差异：%s —— 停止，0 落盘" % tag)

    ast.parse(out)

    dst_bytes = out.encode("utf-8")
    DST.write_bytes(dst_bytes)

    sm = difflib.SequenceMatcher(None, src_text.split("\n"), out.split("\n"), autojunk=False)
    ops = sm.get_opcodes()
    changed = [o for o in ops if o[0] != "equal"]
    same = sum(o[2] - o[1] for o in ops if o[0] == "equal")
    added = sum(o[4] - o[3] for o in ops if o[0] in ("insert", "replace"))
    deleted = sum(o[2] - o[1] for o in ops if o[0] in ("delete", "replace"))

    def sha12(b):
        return hashlib.sha256(b).hexdigest()[:12]

    n_src = len(src_text.split("\n"))
    print("[transform] src : %s sha12=%s bytes=%d LF=%d" % (SRC.name, sha12(src_bytes), len(src_bytes), src_text.count("\n")))
    print("[transform] dst : %s sha12=%s bytes=%d LF=%d lines=%d"
          % (DST.name, sha12(dst_bytes), len(dst_bytes), out.count("\n"), len(out.split("\n"))))
    print("[transform] hunk=%d  +%d / -%d  逐字相同行=%d/%d (%.1f%%)"
          % (len(changed), added, deleted, same, n_src, 100.0 * same / n_src))
    print("[transform] dst CRLF=%d BOM=%s" % (dst_bytes.count(b"\r\n"), dst_bytes.startswith(b"\xef\xbb\xbf")))
    print("[transform] ast.parse OK · 判据/构造面 5 处切片逐字相同")
    return 0


if __name__ == "__main__":
    sys.exit(main())
