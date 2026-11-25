#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
查理 · FTFB R6 增补轮 F18 执行脚本（单锚 · 摘要压缩 · 前置指纹门）

任务来源：群管理员 2026-10-20 20:14:23 派单【R6 增补轮·单点：摘要压缩】——
  唯一阻断项（戴夫 20:02 登记）：R6 摘要（M-3 版）实测 1,973 字符（arXiv paste
  口径）＞常设限 1,920（超 53）。用户 20:17 追加指令：新元数据一并交付。

基线纪律（沿 apply_r5_final.py / apply_r6_final.py 先例）：
  - 前置门：输入 tex sha256 前 12 位必须等于 45887c4316d3（R6 落稿轮登记指纹）；
    任何其它状态（含已应用 F18 后态）即停——单轮语义，防重放多写。重跑复验需以
    F18 前态正本为输入（私区备份 r6/pre_f18_45887c4316d3_fiction_that_feeds_back.tex
    或戴夫 R6 打包目录内同字节正本）。
  - F18 old＝自 tex 提取的摘要行（0 手抄）；F18 new＝本脚本内嵌压缩稿
    （Δ=96 字符；语义零损约束＝F01 四要点＋爱丽丝 19 点结论不漂移）。
  - R5 tex ba2f157196f5、改稿单、apply_r6_final.py、R5_to_R6_unified_diff.txt、
    selfcheck_pairs_log.json、戴夫 R6 打包目录全部文件及一切历史件：只读零改。
    本脚本写集＝R6 tex 本体（整行替换）＋四随件（diff/pairs/metadata）＋
    自检记录追加段＋私区前态备份。

压缩四刀（砍冗词不砍要点；逐刀语义依据登记于自检记录 §八）：
  F18-a 三检括注对齐 §1.2 itemize 正典命名：
      "dispensability of the fictional input" → "dispensability"
      （§1.2 正典：T (temporal priority) / D (dispensability) / R (operative residue)；
        检查对象由主张句主题 fiction-as-input 默认承载，三检名全保）
  F18-b 摘要内重复申报删：
      "The argument separates the four channels," → "The four channels are"
      （「分离」纪律已由主张句 "four channels — … — separate under three checks" 承载，
        头句重复申报；"each anchored in cases" 与四例证清单逐字保留）
  F18-c 同指合并（原句双 one 同指：artifact＝instance＝§7 同一受检件）：
      "demonstrated on one artifact at the stated power; one engineering-grade,
       mid-strength instance is examined with its negative results disclosed in full"
      → "demonstrated on one engineering-grade, mid-strength artifact at the stated
         power, with its negative results disclosed in full"
      （五要素 one / engineering-grade / mid-strength / at the stated power /
        negative results in full 逐项保留，三短语逐字沿 §1.2/§7.3 原措辞）
  F18-d 范围标记冗词删："for the engineering record, " 整删
      （存储链内容要素由其后各分句自身显式承载；沿 R4 摘要削减先例删范围限定语）

硬约束自检（全部通过后方落盘；任一失败即停、零写入）：
  1. 字符数：old 1,973 → new 1,877（Δ=96 ≥ 53 ✓；new ≤ 1,880 ✓；距 1,920 余 43）；
     口径＝whitespace-normalized（arXiv paste caliber，与戴夫 20:02 登记同口径）。
  2. F01 四要点逐字在场：问题化开篇句／主张句头 "We argue that fiction is not
     evidence but a recurrent, checkable input:"／objection 纪律句（＝爱丽丝 5b
     逐字引文）／"position paper" 自报保持 0 命中。
  3. 逐字保留锚串 19 段恰 1 次（资产句、三检正典名、四例证、M1–M5 映射句、
     四阶段流水线、not-asserted/adjudication/how-it-would-die、第三方可核链、
     author-attested freeze/provisional (§7.4) 链等——全清单落 pairs log）。
  4. 禁形 0（新摘要内）：position paper / position statement / KIMI / kimi / kill /
     death / will show / has been generalized / is expected to succeed /
     inherits this paper's / inspired by / originates in / traces back to /
     the source of / onewithdream；objection 小写恰 1（G-4 摘要句计数不变）。
  5. 全文词族与匿名面计数逐项与输入恒等（摘要行外零改的直接推论，仍逐项断言）。
  6. 数字 token：新摘要数字集 {1, 5, 7.4}＝旧摘要集，0 新增。
  7. 非 ASCII 仅 U+00A7/U+2013/U+2014；em-dash 6 / en-dash 1 / § 1（与旧一致）。
  8. 池 66：References 区块字节恒等；[R01]–[R66] 条目恰 66；a57d7fe 恰 1。
  9. 反向回放（new→old）还原输入字节恒等；前缀/后缀字节恒等（除摘要行外全文字节不变）。
 10. 行数不变 689；体量 132,269 − 96 = 132,173 B；无双空格；摘要行以句号收束。
"""

import difflib
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime

SHARED = "〔本地路径已脱敏〕"
R6_PATH = SHARED + "/fiction_that_feeds_back.tex"
DIFF_PATH = SHARED + "/F18_abstract_unified_diff.txt"
JSON_PATH = SHARED + "/selfcheck_f18_pairs_log.json"
META_PATH = SHARED + "/arxiv_metadata_abstract_F18_2026_10_20.txt"
MD_PATH = SHARED + "/查理_FTFB_R6落稿自检记录_2026_10_20.md"
DAVE_SHEET = "〔本地路径已脱敏〕"
BACKUP_PATH = ("〔本地路径已脱敏〕"
               "pre_f18_45887c4316d3_fiction_that_feeds_back.tex")

PRE_SHA12 = "45887c4316d3"
ARXIV_LIMIT = 1920
SUGGESTED = 1880

# ---------------------------------------------------------------- F18 new text
NEW_SENTENCES = [
    "When may fiction count as an input to the exact sciences, rather than as their contrast case?",
    "We argue that fiction is not evidence but a recurrent, checkable input: four channels — formal, controlled, quantitative, narrative — separate under three checks (temporal priority, dispensability, operative residue), and whether machine worldviews open the reverse channel stands or falls on the same falsifiability criteria we specify.",
    "Each channel is stated against its strongest available objection and answered on the record, concessions included.",
    "The four channels are each anchored in cases: non-Euclidean geometry as formal language prior to physical reference; thought experiments as controlled fiction under a translatability criterion; entropy as an abstract quantity that entered engineering by formal analogy and re-entered physics carrying a measurable price; and narrative fiction that supplies vocabulary and sets agendas, from a wormhole question to the singularity.",
    "A mapping (M1–M5) pairs the hardness criteria of hard science fiction with the falsifiability criteria of AI research claims in a constructed structural parallel — criteria with shared failure modes, one row an import from the pre-registration literature, declared as such — and a four-stage pipeline — setting, formalization, pre-registration, experiment — ports the mapping into a worked method, demonstrated on one engineering-grade, mid-strength artifact at the stated power, with its negative results disclosed in full.",
    "The reverse channel is not asserted; an adjudication agenda states what would count as feedback and how it would die.",
    "Every claim is stated to be checkable by a third party; the frozen artifacts and full digests are deposited in a public repository, cited at its frozen commit, and the instance's temporal anchor is an author-attested freeze, recorded as provisional (§7.4).",
]
NEW = " ".join(NEW_SENTENCES)

# 逐字保留锚串（F01 四要点＋爱丽丝 5b 引文＋正文回声资产句＋冻结链）
PRESERVED_ANCHORS = [
    "When may fiction count as an input to the exact sciences, rather than as their contrast case?",
    "We argue that fiction is not evidence but a recurrent, checkable input:",
    "formal, controlled, quantitative, narrative",
    "temporal priority, dispensability, operative residue",
    "whether machine worldviews open the reverse channel stands or falls on the same falsifiability criteria we specify",
    "Each channel is stated against its strongest available objection and answered on the record, concessions included.",
    "each anchored in cases",
    "non-Euclidean geometry as formal language prior to physical reference",
    "thought experiments as controlled fiction under a translatability criterion",
    "entropy as an abstract quantity that entered engineering by formal analogy and re-entered physics carrying a measurable price",
    "narrative fiction that supplies vocabulary and sets agendas, from a wormhole question to the singularity",
    "A mapping (M1–M5) pairs the hardness criteria of hard science fiction with the falsifiability criteria of AI research claims",
    "in a constructed structural parallel — criteria with shared failure modes, one row an import from the pre-registration literature, declared as such —",
    "a four-stage pipeline — setting, formalization, pre-registration, experiment — ports the mapping into a worked method",
    "engineering-grade, mid-strength",
    "at the stated power",
    "with its negative results disclosed in full",
    "The reverse channel is not asserted; an adjudication agenda states what would count as feedback and how it would die.",
    "Every claim is stated to be checkable by a third party",
    "the frozen artifacts and full digests are deposited in a public repository, cited at its frozen commit",
    "the instance's temporal anchor is an author-attested freeze, recorded as provisional (§7.4).",
]

# 摘要内必须为 0 的禁形（匿名面／诗引文来源箭头／C-2 四禁形／判死线题面）
ABSTRACT_BANNED = [
    "position paper", "position statement", "KIMI", "kimi", "Kill", "kill",
    "Death", "death", "will show", "has been generalized",
    "is expected to succeed", "inherits this paper's",
    "inspired by", "originates in", "traces back to", "the source of",
    "onewithdream",
]

# 全文级词族/匿名面恒等断言（输入 vs 产物逐项相等）
FILE_FAMILIES = [
    "position paper", "position statement", "KIMI", "kimi", "onewithdream",
    "Objection", "will show", "has been generalized",
    "is expected to succeed", "inspires", "inspired by", "originates in",
    "traces back to", "the source of", "a57d7fe", "Position Paper",
]

# 四刀逐刀实测（旧片段 → 新片段；用于 §八 刀账表）
CUTS = [
    ("F18-a", "dispensability of the fictional input", "dispensability"),
    ("F18-b",
     "The argument separates the four channels, each anchored in cases:",
     "The four channels are each anchored in cases:"),
    ("F18-c",
     "demonstrated on one artifact at the stated power; one engineering-grade, "
     "mid-strength instance is examined with its negative results disclosed in full",
     "demonstrated on one engineering-grade, mid-strength artifact at the stated "
     "power, with its negative results disclosed in full"),
    ("F18-d", "for the engineering record, ", ""),
]


class Stop(Exception):
    pass


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def main() -> None:
    failures = []

    # ---- 前置指纹门 --------------------------------------------------------
    raw = open(R6_PATH, "rb").read()
    src = raw.decode("utf-8")
    if sha12(raw) != PRE_SHA12:
        raise Stop("前置门失败：输入 tex 指纹 %s ≠ 登记值 %s（单轮语义：F18 前态方可执行）"
                   % (sha12(raw), PRE_SHA12))
    pre_bytes, pre_lines = len(raw), src.count("\n")

    # ---- F18 old：自 tex 提取摘要行（0 手抄） ------------------------------
    m = re.search(r"\\begin\{abstract\}\n\n\n(.*?)\n\n\\end\{abstract\}", src, re.S)
    if not m:
        raise Stop("摘要环境未按登记结构命中（begin/3 空行/单行/2 空行/end）")
    OLD = m.group(1)
    if "\n" in OLD:
        raise Stop("摘要非单行——与落稿轮结构断言冲突")
    if src.count(OLD) != 1:
        raise Stop("F18 old 锚串在全文命中 %d 次（应恰 1）" % src.count(OLD))
    raw_between_old = len("\\begin{abstract}") and len(
        src.split("\\begin{abstract}")[1].split("\\end{abstract}")[0])

    # ---- 期望值独立复测（戴夫 20:02 登记值交叉） ---------------------------
    if len(OLD) != 1973:
        failures.append("旧摘要长度实测 %d ≠ 戴夫登记 1,973" % len(OLD))
    if len(NEW) != 1877:
        failures.append("新摘要长度实测 %d ≠ 申报 1,877" % len(NEW))
    delta = len(OLD) - len(NEW)
    if delta < 53:
        failures.append("压缩量 %d < 53" % delta)
    if len(NEW) > SUGGESTED:
        failures.append("新摘要 %d > 建议目标 1,880" % len(NEW))
    if len(NEW) > ARXIV_LIMIT:
        failures.append("新摘要 %d > arXiv 限 1,920" % len(NEW))
    if " ".join(NEW.split()) != NEW or "  " in NEW:
        failures.append("新摘要非单距空格形态")

    # ---- 应用（整行替换）＋ 反向回放＋ 前后缀恒等 --------------------------
    product = src.replace("\n" + OLD + "\n", "\n" + NEW + "\n", 1)
    if product == src:
        failures.append("替换未生效")
    replay = product.replace("\n" + NEW + "\n", "\n" + OLD + "\n", 1)
    if replay != src:
        failures.append("反向回放不还原（失配或多写）")
    pre_part, post_part = src.split(OLD, 1)
    if not (product == pre_part + NEW + post_part):
        failures.append("前缀/后缀拼接证明失败")
    if pre_part not in product or product.count(pre_part) < 1:
        failures.append("前缀不在产物中")
    if not product.endswith(post_part):
        failures.append("后缀不恒等")
    new_raw = product.encode("utf-8")

    # ---- 逐字保留锚串 19 段恰 1 次 -----------------------------------------
    anchor_report = []
    for p in PRESERVED_ANCHORS:
        c = NEW.count(p)
        anchor_report.append({"anchor": p, "count": c})
        if c != 1:
            failures.append("保留锚串非恰 1 次（%d）：%s" % (c, p[:60]))
    # 爱丽丝 5b 逐字引文（摘要承诺句）单独点名
    alice_5b = ("stated against its strongest available objection and answered "
                "on the record, concessions included")
    if NEW.count(alice_5b) != 1:
        failures.append("爱丽丝 5b 引文不在新摘要（逐字）")
    # F01 主张句头
    if NEW.count("We argue that fiction is not evidence but a recurrent, checkable input:") != 1:
        failures.append("F01 主张句头不在新摘要（逐字）")

    # ---- 摘要内禁形 0／objection 恰 1 --------------------------------------
    for b in ABSTRACT_BANNED:
        c = NEW.count(b)
        if c:
            failures.append("新摘要禁形命中 %d：%s" % (c, b))
    n_obj = len(re.findall(r"objection", NEW))
    if n_obj != 1:
        failures.append("新摘要 objection 小写计数 %d ≠ 1（G-4 摘要句口径）" % n_obj)
    if len(re.findall(r"Objection", NEW)) != 0:
        failures.append("新摘要 Objection 大写计数 ≠ 0")

    # ---- 数字 token 集＝旧集（0 新增） --------------------------------------
    nums_old = sorted(set(re.findall(r"\d+(?:\.\d+)?", OLD)))
    nums_new = sorted(set(re.findall(r"\d+(?:\.\d+)?", NEW)))
    if nums_old != nums_new:
        failures.append("数字 token 集漂移：%s → %s" % (nums_old, nums_new))

    # ---- 非 ASCII 审计 -------------------------------------------------------
    na_new = sorted(set(hex(ord(ch)) for ch in NEW if ord(ch) > 127))
    na_old = sorted(set(hex(ord(ch)) for ch in OLD if ord(ch) > 127))
    if na_new != ["0x2013", "0x2014", "0xa7"]:
        failures.append("新摘要非 ASCII 集漂移：%s" % na_new)
    if (NEW.count("—"), NEW.count("–"), NEW.count("§")) != (6, 1, 1):
        failures.append("破折号/节号计数与旧不一致")
    if not NEW.endswith("."):
        failures.append("新摘要不以句号收束")

    # ---- 全文词族/匿名面恒等（输入 vs 产物） --------------------------------
    fam_report = {}
    for f in FILE_FAMILIES:
        c_in, c_out = src.count(f), product.count(f)
        fam_report[f] = [c_in, c_out]
        if c_in != c_out:
            failures.append("全文词族计数漂移：%s %d→%d" % (f, c_in, c_out))
    for rx in (r"[Kk]ill", r"[Dd]eath"):
        c_in = len(re.findall(rx, src))
        c_out = len(re.findall(rx, product))
        fam_report["regex:" + rx] = [c_in, c_out]
        if c_in != c_out:
            failures.append("全文词族计数漂移（regex %s）：%d→%d" % (rx, c_in, c_out))
    c_in = len(re.findall(r"objection", src))
    c_out = len(re.findall(r"objection", product))
    fam_report["regex:objection"] = [c_in, c_out]
    if c_in != c_out:
        failures.append("全文 objection 计数漂移：%d→%d" % (c_in, c_out))

    # ---- 池 66／引用冻结／结构不变 ------------------------------------------
    def refs_block(t):
        return t.split("\\section*{References}", 1)[1]
    if refs_block(src) != refs_block(product):
        failures.append("References 区块不字节恒等")
    n_pool = len(re.findall(r"\\item\[R\d\d\.\]", refs_block(product)))
    if n_pool != 66:
        failures.append("References 条目 %d ≠ 66" % n_pool)
    n_cit_in = len(re.findall(r"\[R\d\d\]", src.split("\\section*{References}", 1)[0]))
    n_cit_out = len(re.findall(r"\[R\d\d\]", product.split("\\section*{References}", 1)[0]))
    if n_cit_in != n_cit_out or n_cit_out != 190:
        failures.append("正文引用实例 %d→%d（应恒等 190）" % (n_cit_in, n_cit_out))
    if product.count("a57d7fe") != 1:
        failures.append("a57d7fe 计数 ≠ 1")
    new_lines = product.count("\n")
    if new_lines != pre_lines:
        failures.append("行数漂移 %d→%d" % (pre_lines, new_lines))

    # ---- 四刀逐刀账（用于登记表） -------------------------------------------
    cut_rows = []
    for cid, o, n in CUTS:
        if OLD.count(o) != 1:
            failures.append("四刀旧片段非恰 1 次：%s" % cid)
        cut_rows.append({"id": cid, "old": o, "new": n,
                         "delta": len(o) - len(n)})
    if sum(r["delta"] for r in cut_rows) != delta:
        failures.append("四刀账之和 %d ≠ 总压缩量 %d"
                        % (sum(r["delta"] for r in cut_rows), delta))
    # 四刀顺序回放于 old（a→b→c→d）须逐步收敛到 new（结构性验证）
    temp = OLD
    for cid, o, n in CUTS:
        temp = temp.replace(o, n, 1)
    if temp != NEW:
        failures.append("四刀顺序回放（a→b→c→d）不收敛到 new")

    # ---- 失败即停（零写入） -------------------------------------------------
    if failures:
        print("[失败登记] %d 项：" % len(failures))
        for x in failures:
            print("  -", x)
        raise Stop("自检存在失败项——即停（零写入，产物不交付）")

    # ---- 落盘：私区前态备份 → tex 本体 → 四随件 -----------------------------
    shutil.copyfile(R6_PATH, BACKUP_PATH)
    with open(R6_PATH, "wb") as f:
        f.write(new_raw)
    # 落盘后复读复核（防半写）
    if sha12(open(R6_PATH, "rb").read()) != sha12(new_raw):
        raise Stop("落盘复读指纹不符（半写）——即停")
    out_sha12, out_bytes, out_lines = sha12(new_raw), len(new_raw), new_lines
    raw_between_new = len(product.split("\\begin{abstract}")[1]
                          .split("\\end{abstract}")[0])

    # diff（1 hunk · 摘要行整行替换）
    diff = "".join(difflib.unified_diff(
        src.splitlines(keepends=True), product.splitlines(keepends=True),
        fromfile="fiction_that_feeds_back.tex (R6 pre-F18, sha12 %s)" % PRE_SHA12,
        tofile="fiction_that_feeds_back.tex (R6 F18, sha12 %s)" % out_sha12, n=2))
    with open(DIFF_PATH, "w", encoding="utf-8") as f:
        f.write(diff)
    n_hunks = sum(1 for ln in diff.splitlines() if ln.startswith("@@"))

    # pairs log（JSON · old/new 全文机器可核）
    log = {
        "round": "R6-F18 增补轮",
        "task_source": "群管理员 2026-10-20 20:14:23 派单【R6 增补轮·单点：摘要压缩】＋用户 20:17「新元数据一并交付」",
        "pair": {
            "id": "F18",
            "old_abstract": OLD,
            "new_abstract": NEW,
            "old_chars_paste_caliber": len(OLD),
            "new_chars_paste_caliber": len(NEW),
            "delta": delta,
            "old_raw_between_markers": raw_between_old,
            "new_raw_between_markers": raw_between_new,
            "old_words": len(OLD.split()),
            "new_words": len(NEW.split()),
        },
        "limits": {
            "arxiv_form_limit": ARXIV_LIMIT,
            "admin_suggested_ceiling": SUGGESTED,
            "margin_vs_limit": ARXIV_LIMIT - len(NEW),
            "margin_vs_suggested": SUGGESTED - len(NEW),
        },
        "cuts": cut_rows,
        "checks": {
            "preserved_anchors_count_1": anchor_report,
            "alice_5b_verbatim_in_new": True,
            "f01_claim_head_verbatim_in_new": True,
            "abstract_banned_zero": True,
            "objection_lower_in_new": n_obj,
            "nums_old": nums_old,
            "nums_new": nums_new,
            "non_ascii_new": na_new,
            "non_ascii_old": na_old,
            "em_en_dash_section": [NEW.count("—"), NEW.count("–"), NEW.count("§")],
            "file_families_input_vs_product": fam_report,
            "references_block_byte_identical": True,
            "pool_entries": n_pool,
            "citation_instances": [n_cit_in, n_cit_out],
            "a57d7fe_count": product.count("a57d7fe"),
            "reverse_replay_byte_identical": True,
            "prefix_suffix_byte_identical": True,
            "lines": [pre_lines, new_lines],
        },
        "input_tex": {"sha12": PRE_SHA12, "bytes": pre_bytes},
        "output_tex": {"sha12": out_sha12, "bytes": out_bytes, "lines": out_lines},
        "artifacts": {
            "diff": "F18_abstract_unified_diff.txt",
            "pairs_log": "selfcheck_f18_pairs_log.json",
            "metadata": "arxiv_metadata_abstract_F18_2026_10_20.txt",
            "selfcheck_md_append_section": "八",
            "private_backup_of_pre_state": BACKUP_PATH,
        },
        "errata_registered": {
            "source": "阿兰_R6体裁验收_2026_10_20.md §四.1 移交（只记录不回改）",
            "pairs": [
                {"term": "position paper（LeCun [R22] 第三方描述语豁免位）", "old": "L437", "new": "L458"},
                {"term": "position statement（companion 描述）", "old": "L461", "new": "L482"},
                {"term": "position statement（AI 披露节）", "old": "L518", "new": "L541"},
                {"term": "position statement（附录）", "old": "L524", "new": "L547"},
                {"term": "position statement（[R57] 池条目）", "old": "L648", "new": "L671"},
                {"term": "kimi（Mori 术语 bukimi no tani 罗马字子串）", "old": "L256", "new": "L271"},
                {"term": "kimi（冻结审计迹文件名）", "old": "L401", "new": "L422"},
            ],
            "note": "派单简称「6 处」；按阿兰原表逐行展开为 7 行号对（kimi 系两行；标签依爱丽丝观察③细分）。内容零差异；改稿单已入档不回改。",
        },
        "zero_write_list": ["R5 tex ba2f157196f5", "改稿单（F01–F17 已入档）",
                            "apply_r6_final.py", "R5_to_R6_unified_diff.txt",
                            "selfcheck_pairs_log.json", "戴夫 R6 打包目录全部文件"],
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

    # ---- 新元数据（Abstract 字段新值 paste 件；其余字段沿戴夫 R6 表逐字承用）--
    dave = open(DAVE_SHEET, encoding="utf-8").read()
    fields = dave.split("--------")[0]
    fields = fields[fields.index("Title:"):].rstrip() + "\n"
    meta = (
        "================================================================================\n"
        "arXiv Submission Metadata — Fiction That Feeds Back (R6 edition, F18 amendment)\n"
        "Prepared 2026-10-20 by the writing chain (Charlie). Paste fields verbatim.\n"
        "This sheet amends ONE field (Abstract) of the R6 sheet; every other field is\n"
        "carried verbatim from that sheet (source, read-only: 戴夫_FTFB_R6编译打包_2026/\n"
        "arxiv_metadata.txt). The repack chain re-issues the final sheet with the\n"
        "re-measured page count.\n"
        "================================================================================\n"
        "\n" + fields +
        "\n"
        "--------------------------------------------------------------------------------\n"
        "Verification notes (not for pasting):\n"
        "\n"
        "F18 amendment (this sheet):\n"
        "  Abstract field ONLY, per the 20:14 dispatch (blocking item: the R6 abstract\n"
        "  measured 1,973 whitespace-normalized characters — arXiv paste caliber —\n"
        "  53 over the standing form limit of 1,920). New value: %d characters\n"
        "  (same caliber), margin %d under 1,920 and %d under the 1,880 working\n"
        "  target; raw-between-markers caliber %d. Compression = %d characters in\n"
        "  four redundancy cuts; semantic zero-loss verified against the F01 key\n"
        "  points and the 19-point semantic verification (the one abstract-quoted\n"
        "  point 5b preserved verbatim). Non-ASCII characters only U+00A7, U+2013,\n"
        "  U+2014; no TeX markup, no math-mode delimiters; UTF-8 safe for the web\n"
        "  form.\n"
        "  Other fields: carried VERBATIM from the R6 sheet (zero-change; sole\n"
        "  author unchanged — no moderation-approval trigger). The Comments field's\n"
        "  page count (31) is the pre-F18 measured value: the repack chain\n"
        "  re-measures after recompiling from the F18 tex (abstract 96 characters\n"
        "  shorter) and stamps the final value.\n"
        "  Fingerprints: pre-F18 tex %s (%d B, %d lines); F18 tex %s (%d B, %d\n"
        "  lines); pair / diff / checks: selfcheck_f18_pairs_log.json,\n"
        "  F18_abstract_unified_diff.txt, apply_r6_f18_abstract.py (shared\n"
        "  查理_FTFB_R6重构稿_2026/).\n"
        "  M-2 (Comments AI-annotation clause): unchanged posture — NOT ADDED, per\n"
        "  the standing decision (add only on PI's explicit request).\n"
        "\n"
        "Paste value (verbatim, single line — source whitespace is single-spaced;\n"
        "paste as one paragraph):\n"
        "\n"
        + NEW + "\n"
    ) % (len(NEW), ARXIV_LIMIT - len(NEW), SUGGESTED - len(NEW),
         raw_between_new, delta,
         PRE_SHA12, pre_bytes, pre_lines, out_sha12, out_bytes, out_lines)
    with open(META_PATH, "w", encoding="utf-8") as f:
        f.write(meta)

    # ---- 自检记录追加段（§八） ----------------------------------------------
    stamp = datetime.now().strftime("%H:%M")
    md_append = """

---

## 八、F18 摘要压缩增补轮（2026-10-20 20:14 派单 · 单锚 · 唯一阻断项清除）

- **任务来源**：群管理员 2026-10-20 20:14:23 派单【R6 增补轮·单点：摘要压缩】——唯一阻断项（戴夫 20:02 登记）：R6 摘要（M-3 版）1,973 字符（arXiv paste 口径）＞常设限 1,920（超 53），包不得提交；用户 20:17 追加指令「新元数据一并交付」。
- **执行**：`apply_r6_f18_abstract.py`（前置门 sha12 `45887c4316d3`）单锚 F18 应用。old＝自 tex 提取的摘要行（0 手抄）；new＝压缩稿（四刀）。反向回放（new→old）还原输入**字节恒等**；前缀/后缀字节恒等＝除摘要行外全文零改；落盘后复读复核指纹一致。
- **字符数实证**（whitespace-normalized＝arXiv paste caliber，与戴夫 20:02 登记同口径）：old **1,973** → new **{new_chars}**（Δ=**{delta}** ≥ 53 ✓；≤ 1,880 ✓；距 1,920 限余 **{margin_limit}**）。词数 291 → {new_words}。raw-between-markers 口径（戴夫表单同列）：old 1,978 → new {raw_new}。
- **四刀账**（砍冗词不砍要点；每刀旧→新全文登记于 `selfcheck_f18_pairs_log.json`）：

| 刀 | 旧片段 | 新片段 | 字符 |
|---|---|---|---|
| F18-a | dispensability of the fictional input | dispensability | −{d_a} |
| F18-b | The argument separates the four channels, each anchored in cases: | The four channels are each anchored in cases: | −{d_b} |
| F18-c | demonstrated on one artifact at the stated power; one engineering-grade, mid-strength instance is examined with its negative results disclosed in full | demonstrated on one engineering-grade, mid-strength artifact at the stated power, with its negative results disclosed in full | −{d_c} |
| F18-d | for the engineering record, | （删） | −{d_d} |

  逐刀依据：a＝对齐 §1.2 itemize 正典命名「T (temporal priority)／D (dispensability)／R (operative residue)」，检查对象由主张句主题（fiction-as-input）默认承载，三检名全保；b＝「分离」纪律已由主张句「four channels — … — separate under three checks」承载，头句系摘要内重复申报，「each anchored in cases」与四例证清单逐字保留；c＝原句双 one 同指（artifact＝instance＝§7 同一受检件），五要素（one／engineering-grade／mid-strength／at the stated power／negative results in full）逐项保留，且「carrying a measurable price」（§4 逐字回声）与「with its negative results disclosed in full」（§1.2 逐字回声）两处两轮压缩存活资产句**逐字不动**；d＝范围标记冗词，存储链内容要素（冻结工件／全摘要存储／公开仓冻结 commit 引用）由其后各分句自身显式承载，沿 R4 摘要削减先例（删「on the same footing as the historical cases」类范围限定语）。
- **零漂移核验**：F01 四要点逐字在场——问题化开篇句（逐字）／主张句头「We argue that fiction is not evidence but a recurrent, checkable input:」（逐字）／objection 纪律句（逐字，＝爱丽丝 5b 引文「stated against its strongest available objection and answered on the record, concessions included」）／position paper 自报保持 0 命中。爱丽丝 19 点中唯一直接引用摘要的判定位＝5b（逐字保留）；其余 18 点锚位（F03＝§1.2／F13/F14＝§8.4／F11＝题式／论证链各面）全在摘要行外，前缀/后缀字节恒等 ⇒ 19 点结论零漂移。逐字保留锚串 {n_anchors} 段恰 1 次（全清单落 pairs log）。
- **词族账／匿名面**：新摘要内 position paper／position statement／KIMI／kimi／kill／death／C-2 四禁形／来源箭头四词族全 0；objection 小写恰 1（G-4 摘要句计数不变）；全文词族与匿名面计数逐项与输入恒等（machine log）。数字 token 集 {{1, 5, 7.4}} 不变；非 ASCII 仅 §／—／–（em 6／en 1／§ 1，与旧一致）。
- **池 66／引用冻结**：References 区块字节恒等；[R01]–[R66] 恰 66；正文引用实例 190→190；a57d7fe 恰 1；行数 689 不变。
- **新指纹登记**：R6-F18 tex sha12 `{out_sha12}` · {out_bytes} B · 689 行（体量 −{delta} B）。F18 前态正本备份：私区 `r6/pre_f18_45887c4316d3_fiction_that_feeds_back.tex`；戴夫 R6 打包目录内 `fiction_that_feeds_back.tex` 为同字节正本（其 manifest 可复核）。
- **随件**：`F18_abstract_unified_diff.txt`（{n_hunks} hunk · 摘要行整行替换）＋`selfcheck_f18_pairs_log.json`（old/new 全文＋全部检查实测值）＋`arxiv_metadata_abstract_F18_2026_10_20.txt`（新元数据：Abstract 字段新值 paste 件；其余字段沿戴夫 R6 表逐字承用并申报；页数候其重编译实测刷新）。
- **行号漂移勘误追加登记（阿兰 §四.1 移交 · 只记录不回改）**：改稿单 §六/§九 行号系撞窗中间件（131,329 B）口径，R6 终稿（132,269 B，References 区 +119 B 增长）实测漂移——派单简称「6 处」，按阿兰原表逐行展开为 7 行号对（kimi 系两行；标签依爱丽丝观察③细分）：

| 词面 | 改稿单行号（中间件口径） | R6 终稿实测 |
|---|---|---|
| position paper（LeCun [R22] 第三方描述语豁免位） | L437 | L458 |
| position statement（companion 描述） | L461 | L482 |
| position statement（AI 披露节） | L518 | L541 |
| position statement（附录） | L524 | L547 |
| position statement（[R57] 池条目） | L648 | L671 |
| kimi（L271＝Mori 术语 bukimi no tani 罗马字子串） | L256 | L271 |
| kimi（L422＝冻结审计迹文件名） | L401 | L422 |

  内容零差异；改稿单已入档不回改（沿笔误订正先例）。本登记不触发任何文件改动。
- **历史件只读零改确认**：R5 tex `ba2f157196f5`、改稿单（F01–F17）、`apply_r6_final.py`、`R5_to_R6_unified_diff.txt`、`selfcheck_pairs_log.json`、戴夫 R6 打包目录全部文件——本轮零写入（本脚本写集＝tex 本体＋四随件＋本记录追加段＋私区前态备份）。
- **接力**：戴夫重编译重打包（Abstract 字段换 F18 新值；页数实测刷新；M-3 摘要联动以本轮为准）→ 最终提交候 PI 放行。

—— 查理-论文主笔 ｜ 2026-10-20 {stamp} ｜ R6 增补轮 F18 · 单锚 · 摘要 1,973→{new_chars}（Δ{delta}）· 0 失配 0 多写 · 建议非裁
""".format(new_chars=len(NEW), delta=delta, margin_limit=ARXIV_LIMIT - len(NEW),
           new_words=len(NEW.split()), raw_new=raw_between_new,
           d_a=cut_rows[0]["delta"], d_b=cut_rows[1]["delta"],
           d_c=cut_rows[2]["delta"], d_d=cut_rows[3]["delta"],
           n_anchors=len(PRESERVED_ANCHORS), out_sha12=out_sha12,
           out_bytes=out_bytes, n_hunks=n_hunks, stamp=stamp)
    with open(MD_PATH, "a", encoding="utf-8") as f:
        f.write(md_append)

    # ---- 汇报 ---------------------------------------------------------------
    print("前置门：%s · %d B · %d 行" % (PRE_SHA12, pre_bytes, pre_lines))
    print("摘要：old %d → new %d（Δ=%d；≤%d ✓；距 %d 限余 %d）"
          % (len(OLD), len(NEW), delta, SUGGESTED, ARXIV_LIMIT,
             ARXIV_LIMIT - len(NEW)))
    print("词数：%d → %d | raw-between-markers：%d → %d"
          % (len(OLD.split()), len(NEW.split()), raw_between_old, raw_between_new))
    print("四刀账：a −%d / b −%d / c −%d / d −%d（和＝%d）"
          % (cut_rows[0]["delta"], cut_rows[1]["delta"],
             cut_rows[2]["delta"], cut_rows[3]["delta"],
             sum(r["delta"] for r in cut_rows)))
    print("保留锚串 %d 段恰 1 次 ✓ | 禁形 0 ✓ | objection 恰 1 ✓ | 数字集 %s ✓"
          % (len(PRESERVED_ANCHORS), nums_new))
    print("回放恒等 ✓ | 前后缀恒等 ✓ | 池 66 ✓ | 引用实例 190→190 ✓ | a57d7fe 1 ✓")
    print("产物：sha12 %s · %d B · %d 行 | diff %d hunk | 随件 4＋自检记录 §八追加"
          % (out_sha12, out_bytes, out_lines, n_hunks))
    print("\n全绿。产物：\n  %s\n  %s\n  %s\n  %s\n  %s（追加）"
          % (R6_PATH, DIFF_PATH, JSON_PATH, META_PATH, MD_PATH))


if __name__ == "__main__":
    try:
        main()
    except Stop as e:
        print("STOP:", e)
        sys.exit(2)
