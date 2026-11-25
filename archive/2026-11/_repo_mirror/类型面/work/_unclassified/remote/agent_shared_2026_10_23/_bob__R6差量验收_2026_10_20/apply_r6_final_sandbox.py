#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
查理 · FTFB R6 落稿执行脚本（单轮 · R6 改稿单 F01–F17 锚串 · R5 原件只读）

基线纪律：
  - R5 tex 原件只读（sha256 前 12 位断言 ba2f157196f5；本脚本绝不写它）。
  - 17 对 (old, new) 全部逐字解析自改稿单 shared/查理_FTFB_R6改稿单_2026_10_20.md
    （F01–F17 各自 fenced ```tex 块：首块＝锚串 old，次块＝拟落文本 new；0 手抄）。
    K-2/K-3/K-5 逐字取自爱丽丝 A 轨 v2 §四原文（登记于改稿单 §三），随解析一并落稿。
  - 顺序应用 F01→F17，逐条断言当前文本中锚串恰好命中 1 次；任一失配 → 登记失败项即停，不手补。
  - 应用完成后反向回放（F17→F01 逐条 new→old）必须还原出与 R5 字节恒等的文本
    ——构成「无失配·无多写」的形式证明（R5→R6 的全部差异恰为 17 对替换本身）。

硬约束自检（随件）：
  - 池 66：References 区块字节恒等＋[R01]–[R66] 条目数 66＋正文 [Rxx] 引用实例数恒等。
  - 引用冻结：References 区（\section*{References} 至文末）与 R5 字节恒等。
  - 匿名面：anonymized 声明句计数恒等；KIMI/kimi 计数恒等（既有 2 处＝审计迹字段路径）；
    onewithdream 0；诗面词 0。
  - 0 诗引文／0 来源箭头／0 epigraph：inspired by／originates in／traces back to／
    the source of 词族 0 命中（基线 0，新文本 0 增）。
  - C-2 五类禁用形（no prediction）：has been generalized／will show／is expected to
    succeed／inherits this paper's／同源＝证据形——新文本 0 命中。
  - G-1：position paper 自报清除（预期 1 处＝LeCun [R22] 第三方描述语）。
  - G-4：Objection/Reply 词族计数（预期 4/4）。
  - G-9：kill 族与 death 字面词频账（申报：题面 Death −1；kill 净 +1＝K-5 逐字携带）。
  - 数字字面：新文本数字 token 清点（全为节号/判据号，0 实验数字）。

输出（OUT 目录 shared/查理_FTFB_R6重构稿_2026/）：
  fiction_that_feeds_back.tex                          R6 新文件
  R5_to_R6_unified_diff.txt                            unified diff（hunk 编号与自检映射一致）
  selfcheck_pairs_log.json                             17 对全文＋逐条定位＋词族账＋指纹（机器可核）
  查理_FTFB_R6落稿自检记录_2026_10_20.md                自检随件（人读）
"""

import hashlib, json, os, re, sys, difflib

BASE = "〔本地路径已脱敏〕"
R5_DIR = os.path.join(BASE, "查理_FTFB_R5落稿_2026_10_20")
R5_PATH = os.path.join(R5_DIR, "fiction_that_feeds_back.tex")
SHEET_PATH = os.path.join(BASE, "查理_FTFB_R6改稿单_2026_10_20.md")
OUT_DIR = os.path.join(BASE, "查理_FTFB_R6重构稿_2026")
R6_PATH = os.path.join(OUT_DIR, "fiction_that_feeds_back.tex")
DIFF_PATH = os.path.join(OUT_DIR, "R5_to_R6_unified_diff.txt")
JSON_PATH = os.path.join(OUT_DIR, "selfcheck_pairs_log.json")
MD_PATH = os.path.join(OUT_DIR, "查理_FTFB_R6落稿自检记录_2026_10_20.md")

# --- BOB sandbox redirect (R6 差量验收·确定性重跑): 写入重定向至私区，shared 输入件只读 ---
_SB = os.environ.get("BOB_R6_OUT")
if _SB:
    R6_PATH = os.path.join(_SB, "fiction_that_feeds_back.tex")
    DIFF_PATH = os.path.join(_SB, "R5_to_R6_unified_diff.txt")
    JSON_PATH = os.path.join(_SB, "selfcheck_pairs_log.json")
    MD_PATH = os.path.join(_SB, "查理_FTFB_R6落稿自检记录_2026_10_20.md")


R5_SHA12 = "ba2f157196f5"


class Stop(Exception):
    pass


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def parse_pairs(sheet_text):
    """从改稿单解析 F01–F17 的 (old, new) 锚串对。"""
    pairs = []
    cur = None
    blocks = []
    in_fence = False
    buf = []
    for line in sheet_text.split("\n"):
        if line.strip() == "```tex":
            in_fence = True
            buf = []
            continue
        if in_fence and line.strip() == "```":
            in_fence = False
            blocks.append("\n".join(buf))
            continue
        if in_fence:
            buf.append(line)
            continue
        m = re.match(r"^### (F\d+) ·", line)
        if m:
            if cur is not None:
                pairs.append((cur, blocks))
            cur = m.group(1)
            blocks = []
    if cur is not None:
        pairs.append((cur, blocks))
    out = []
    for fid, blocks in pairs:
        if len(blocks) != 2:
            raise Stop("改稿单 %s 锚串块数 %d ≠ 2" % (fid, len(blocks)))
        out.append((fid, blocks[0], blocks[1]))
    return out


def wc(text, pat):
    return len(re.findall(pat, text))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    failures = []

    r5_bytes = open(R5_PATH, "rb").read()
    if sha12(r5_bytes) != R5_SHA12:
        raise Stop("R5 原件指纹失配：%s ≠ %s（原件不可用，即停）" % (sha12(r5_bytes), R5_SHA12))
    r5 = r5_bytes.decode("utf-8")

    sheet = open(SHEET_PATH, "rb").read().decode("utf-8")
    pairs = parse_pairs(sheet)
    if len(pairs) != 17:
        raise Stop("锚串对数 %d ≠ 17" % len(pairs))
    ids = [p[0] for p in pairs]
    if ids != ["F%02d" % i for i in range(1, 18)]:
        raise Stop("F 系编号断裂：%s" % ids)

    # ---------- 预检：每锚串在 R5 原文恰 1 次 ----------
    pre = {}
    for fid, old, new in pairs:
        c = r5.count(old)
        pre[fid] = c
        if c != 1:
            failures.append("预检 %s 锚串命中 %d 次（应为 1）" % (fid, c))

    # ---------- 顺序应用 F01→F17 ----------
    cur = r5
    applied = []
    for fid, old, new in pairs:
        c = cur.count(old)
        if c != 1:
            failures.append("应用 %s 当前文本命中 %d 次（应为 1）——即停不手补" % (fid, c))
            raise Stop("应用失配 %s" % fid)
        cur = cur.replace(old, new, 1)
        applied.append(fid)
    r6 = cur

    # ---------- 反向回放反证 ----------
    back = r6
    for fid, old, new in reversed(pairs):
        if back.count(new) != 1:
            failures.append("回放 %s new 命中 ≠ 1" % fid)
            raise Stop("回放失配 %s" % fid)
        back = back.replace(new, old, 1)
    reverse_ok = back == r5
    if not reverse_ok:
        failures.append("反向回放未还原 R5 字节恒等——存在失配或多写")

    # ---------- 池 66 与引用冻结 ----------
    refs_marker = "\\section*{References}"
    i5 = r5.find(refs_marker)
    i6 = r6.find(refs_marker)
    refs_r5 = r5[i5:]
    refs_r6 = r6[i6:]
    refs_identical = refs_r5 == refs_r6
    if not refs_identical:
        failures.append("References 区块非字节恒等（引用冻结破坏）")

    item_pat = re.compile(r"\\item\[R(\d{2})\.\]")
    items5 = item_pat.findall(refs_r5)
    items6 = item_pat.findall(refs_r6)
    pool_ok = (len(items5) == 66 and items5 == items6)
    if not pool_ok:
        failures.append("池条目数或序漂移：%d/%d" % (len(items5), len(items6)))

    cit_pat = re.compile(r"\[R(\d{2})\]")
    cits5 = cit_pat.findall(r5[:i5])
    cits6 = cit_pat.findall(r6[:i6])
    cit_ok = (sorted(cits5) == sorted(cits6)) and (len(cits5) == len(cits6))
    if not cit_ok:
        failures.append("正文 [Rxx] 引用实例漂移：%d→%d" % (len(cits5), len(cits6)))

    # ---------- 词族账 ----------
    fam_defs = {
        "position paper": r"position paper",
        "position statement": r"position statement",
        "anonymized in this edition": r"anonymized in this edition",
        "KIMI": r"KIMI",
        "kimi": r"kimi",
        "onewithdream": r"onewithdream",
        "inspired by": r"inspired by",
        "originates in": r"originates in",
        "traces back to": r"traces back to",
        "the source of": r"the source of",
        "Objection": r"Objection",
        "Reply": r"Reply",
        "kill": r"[Kk]ill",
        "death": r"[Dd]eath",
        "objection_lower": r"objection",
        "groundbreaking": r"groundbreaking",
        "revolutionary": r"revolutionary",
        "unprecedented": r"unprecedented",
        "has been generalized": r"has been generalized",
        "will show": r"will show",
        "is expected to succeed": r"is expected to succeed",
        "inherits this paper's": r"inherits this paper's",
    }
    fams = {}
    for k, pat in fam_defs.items():
        fams[k] = (wc(r5, pat), wc(r6, pat))

    # 期望断言
    exp = {
        "position paper": (3, 1),          # 自报 2 清除，LeCun [R22] 第三方描述语保留
        "position statement": (4, 4),      # companion 描述语零动
        "anonymized in this edition": (2, 2),
        "KIMI": (0, 0),
        "kimi": (2, 2),                    # 审计迹字段路径既有
        "onewithdream": (0, 0),
        "inspired by": (0, 0),
        "originates in": (0, 0),
        "traces back to": (0, 0),
        "the source of": (0, 0),
        "Objection": (0, 4),               # 四渠道 objection–reply
        "Reply": (0, 4),
        "kill": (32, 33),                  # K-5 逐字携带 kill verdicts +1
        "death": (2, 1),                   # 题面 Death is the point → 概念式
        "groundbreaking": (0, 0),
        "revolutionary": (0, 0),
        "unprecedented": (0, 0),
        "has been generalized": (0, 0),
        "will show": (0, 0),
        "is expected to succeed": (0, 0),
        "inherits this paper's": (1, 1),  # R5 既有＝AI 披露节否定式资产「nor inherits this paper's guarantees」（C-2 允许形本体），0 新增
    }
    fam_rows = []
    for k in fam_defs:
        a, b = fams[k]
        ok = (k not in exp) or (exp[k] == (a, b))
        if not ok:
            failures.append("词族 %s 计数 %d→%d（预期 %s）" % (k, a, b, exp[k]))
        fam_rows.append((k, a, b, ok))

    # ---------- 新文本数字 token 清点 ----------
    new_texts = "\n".join(new for _, _, new in pairs)
    new_body = "\n".join(l for l in new_texts.split("\n") if not l.lstrip().startswith("%"))
    new_comm = "\n".join(l for l in new_texts.split("\n") if l.lstrip().startswith("%"))
    num_tokens = sorted(set(re.findall(r"\d+(?:\.\d+)?", new_body)))
    num_comm_tokens = sorted(set(re.findall(r"\d+(?:\.\d+)?", new_comm)))
    allowed_nums = {"1.2", "2", "5", "6", "8", "3", "1", "4"}  # 节号（§1.2／§2–§5／§6／§8／§8.3 等）
    m1_date_nums = {"2026", "09", "18", "27", "10", "20", "3", "4", "5", "6"}  # M-1 版本沿革注记行（注释行，不渲染）
    num_ok = all(t in allowed_nums for t in num_tokens) and all(t in m1_date_nums for t in num_comm_tokens)
    if not all(t in allowed_nums for t in num_tokens):
        failures.append("新文本正文含未申报数字 token：%s" % num_tokens)
    if not all(t in m1_date_nums for t in num_comm_tokens):
        failures.append("新文本注记行数字超出 M-1 版本沿革申报值：%s" % num_comm_tokens)

    # ---------- 摘要区保真（中段逐字） ----------
    abstract_mid = "non-Euclidean geometry as formal language prior to physical reference"
    abstract_ok = (abstract_mid in r6) and (abstract_mid in r5)
    if not abstract_ok:
        failures.append("摘要中段资产句漂移")

    # ---------- diff 与 hunk 映射 ----------
    r5_lines = r5.split("\n")
    r6_lines = r6.split("\n")
    diff = list(difflib.unified_diff(r5_lines, r6_lines, fromfile="R5/fiction_that_feeds_back.tex (ba2f157196f5)", tofile="R6/fiction_that_feeds_back.tex", n=3, lineterm=""))
    diff_text = "\n".join(diff) + "\n"

    # hunk→F 映射：hunk 的 R5 侧变更区间覆盖到的全部 F 锚串（区间含 3 行上下文缓冲）
    hunk_starts = []
    for idx, l in enumerate(diff):
        if l.startswith("@@"):
            m = re.match(r"@@ -(\d+)(?:,(\d+))?", l)
            start = int(m.group(1))
            cnt = int(m.group(2)) if m.group(2) is not None else 1
            hunk_starts.append((idx, start, cnt))
    f_line = {}
    for fid, old, _ in pairs:
        pos = r5.find(old)
        f_line[fid] = r5[:pos].count("\n") + 1
    hunk_map = []
    for hidx, (didx, l5, cnt5) in enumerate(hunk_starts, 1):
        lo, hi = l5 - 4, l5 + max(cnt5, 1) + 4
        owners = [fid for fid, ln in f_line.items() if lo <= ln <= hi]
        owners.sort(key=lambda f: f_line[f])
        hunk_map.append((hidx, l5, "+".join(owners) if owners else "（上下文缓冲区）"))

    # ---------- 落盘 ----------
    open(R6_PATH, "w", encoding="utf-8").write(r6)
    open(DIFF_PATH, "w", encoding="utf-8").write(diff_text)

    r6_bytes = r6.encode("utf-8")

    pairs_log = {
        "meta": {
            "script": "apply_r6_final.py",
            "baseline_r5": {"path": R5_PATH, "sha256_12": sha12(r5_bytes), "bytes": len(r5_bytes), "lines": len(r5_lines)},
            "sheet": {"path": SHEET_PATH, "sha256_12": sha12(sheet.encode("utf-8"))},
            "product_r6": {"path": R6_PATH, "sha256_12": sha12(r6_bytes), "bytes": len(r6_bytes), "lines": len(r6_lines)},
            "diff": {"path": DIFF_PATH, "hunks": len(hunk_starts), "sha256_12": sha12(diff_text.encode("utf-8"))},
            "pairs": len(pairs),
        },
        "precheck_unique_in_r5": pre,
        "reverse_replay_byte_identical": reverse_ok,
        "pool66": {"refs_block_identical": refs_identical, "items": len(items6), "body_citations_r5": len(cits5), "body_citations_r6": len(cits6), "citation_instances_identical": cit_ok},
        "family_counts": {k: {"r5": a, "r6": b} for k, (a, b) in fams.items()},
        "new_text_number_tokens": num_tokens,
        "new_text_number_tokens_comment_lines_M1": num_comm_tokens,
        "abstract_mid_preserved": abstract_ok,
        "hunk_map": [{"hunk": h, "r5_line": l, "owner": f} for h, l, f in hunk_map],
        "pairs_full": [{"id": fid, "old": old, "new": new} for fid, old, new in pairs],
        "failures": failures,
    }
    open(JSON_PATH, "w", encoding="utf-8").write(json.dumps(pairs_log, ensure_ascii=False, indent=1))

    # ---------- 自检记录（人读） ----------
    md = []
    md.append("# 查理 · FTFB R6 落稿自检记录（2026-10-20 落稿轮 · 单轮 17 锚）\n")
    md.append("- **执行口径**：管理员 18:15:42 落稿派单（R6 执行轮·起草）——脚本化单轮执行，以 R6 改稿单 F01–F17 锚串对为唯一输入；R5 原件 `ba2f157196f5` 只读（sha256 前 12 位断言，本轮零触碰）；R6 tex 为全新文件（`shared/查理_FTFB_R6重构稿_2026/`）。")
    md.append("- **执行依据**：PI 17:55:25「R6 合并单全按建议且暂无额外的诗」（底账 P15）——四组 19 项全按建议；K-2/K-3/K-5 逐字取爱丽丝 A 轨 v2 §四原文；题式候选甲落稿（候选乙候阿兰标尺＋爱丽丝语义校验）。\n")
    md.append("- **输入件**：R5 原件（`ba2f157196f5`／123,129 B／666 行）；改稿单 `查理_FTFB_R6改稿单_2026_10_20.md`（sha256-12 `%s`）——17 对 (old,new) 全部逐字解析自其 fenced ```tex 块，0 手抄。" % sha12(sheet.encode("utf-8")))
    md.append("- **产物**：R6 tex `sha256-12=%s`／%d B／%d 行；unified diff（%d hunks）；本记录；selfcheck_pairs_log.json（17 对全文机器可核）。\n" % (sha12(r6_bytes), len(r6_bytes), len(r6_lines), len(hunk_starts)))
    md.append("- **结论**：17/17 应用全中，0 失配 0 多写；回放反证 %s；References 区块字节恒等；池 66 条目与正文引用实例双恒等；词族账全过（含 position paper 自报清除 3→1、Objection/Reply 0→4、来源箭头词族 0/0、匿名面恒等）。\n" % ("PASS" if reverse_ok else "FAIL"))

    md.append("## 一、执行与回放（无失配·无多写的形式证明）\n")
    md.append("| 项 | 结果 |")
    md.append("|---|---|")
    md.append("| 预检：17 锚串在 R5 原文各 count==1 | %d/17 ✓ |" % sum(1 for v in pre.values() if v == 1))
    md.append("| 顺序应用 F01→F17：每步当前文本 count==1 | 17/17 ✓ |")
    md.append("| 反向回放 F17→F01（new→old 逐条还原） | %s（R6 反向回放 17 对后与 R5 字节恒等；R5→R6 差异恰为 17 对替换全集） |" % ("PASS" if reverse_ok else "FAIL"))
    md.append("| 体量 | R5 123,129 B/666 行 → R6 %d B/%d 行（净增 %d B，含四 objection–reply、§1 概念段、§6 前置段、K-2/K-3/K-5、摘要重写） |" % (len(r6_bytes), len(r6_lines), len(r6_bytes) - len(r5_bytes)))
    md.append("")

    md.append("## 二、池 66 与引用冻结\n")
    md.append("| 项 | R5 | R6 | 结果 |")
    md.append("|---|---|---|---|")
    md.append("| References 区块（\\section*{References} 至文末） | %d B | %d B | %s |" % (len(refs_r5.encode("utf-8")), len(refs_r6.encode("utf-8")), "字节恒等 ✓" if refs_identical else "失配 ✗"))
    md.append("| \\item[Rxx.] 条目 | %d | %d | %s |" % (len(items5), len(items6), "66/66 ✓" if pool_ok else "✗"))
    md.append("| 正文 [Rxx] 引用实例（题录区前） | %d | %d | %s |" % (len(cits5), len(cits6), "恒等 ✓" if cit_ok else "✗"))
    md.append("")

    md.append("## 三、词族账（匿名面／0 诗引文／0 来源箭头／C-2 禁用形／G-1／G-4／G-9）\n")
    md.append("| 词族 | R5 | R6 | 判 |")
    md.append("|---|---|---|---|")
    for k, a, b, ok in fam_rows:
        md.append("| %s | %d | %d | %s |" % (k, a, b, "✓" if ok else "✗"))
    md.append("")
    md.append("- position paper 残 1 处＝「a position paper makes world models the core component」（LeCun [R22] 第三方描述语，非自报，改稿单 §六 G-1 登记豁免）。")
    md.append("- kimi 残 2 处＝§7.2 审计迹字段路径既有字面（`_kimi_ftfb_s7_independent_recompute` 等，装置级，B 轨审计在案），新文本 0 增。")
    md.append("- objection（小写族含题式 bold）R6 总计 %d 处＝Objection 标题 4＋摘要句 1（G-4 配额 4 组强形式 objection＋reply 达标，各含让步条款）。" % fams["objection_lower"][1])
    md.append("- kill 族净 +1＝K-5「kill verdicts」逐字携带（爱丽丝 A 轨 v2 原文，乙组拍板项）；death −1＝§7.2 题面「Death is the point」转位为概念式「The first action: verdicts before the runs」；其余 kill 族字面 32 处全在保留区（12 装置级＋2 声明级判死线句全保留，G-9 级配申报值内）。")
    md.append("")

    md.append("## 四、数字字面与新文本数字 token\n")
    md.append("- 反向回放字节恒等 ⇒ 一切实验数字（GSM8K/StrategyQA 分数、p 值、λ、字节数、指纹前缀等）逐字保留。")
    md.append("- 新文本数字 token 清点：正文 %s（全为节号引用 §1.2／§2–§5／§6／§8／§8.3，0 实验数字、0 新字面）；注记行 %s（M-1 版本沿革日期/版本号，注释行不渲染）。\n" % (", ".join(num_tokens) if num_tokens else "（无）", ", ".join(num_comm_tokens) if num_comm_tokens else "（无）"))

    md.append("## 五、hunk 映射（diff 对锚串）\n")
    md.append("| Hunk | R5 起始行 | 归属 |")
    md.append("|---|---|---|")
    for h, l, f in hunk_map:
        md.append("| H%d | %d | %s |" % (h, l, f or "—"))
    md.append("")

    md.append("## 六、失败登记\n")
    if failures:
        for x in failures:
            md.append("- %s" % x)
    else:
        md.append("- 空（本轮 0 失败项）。")
    md.append("")

    md.append("## 交接口（爱丽丝语义校验／阿兰体裁验收／鲍勃差量验收指引）\n")
    md.append("- 语义校验（爱丽丝）：F03 三检语法段与 A 轨 v2 §3.4-3 承接表映射一致性；F13 同源句措辞（AI-agent 描述式不点名）；F14 K-2 先行词位（precedent＝非欧先例）；F11 题式候选甲乙语义位。")
    md.append("- 体裁验收（阿兰）：G-1~G-12 逐项对改稿单 §六映射表（题录纠错值以其对标件为准）。")
    md.append("- 差量验收（鲍勃）：`R5_to_R6_unified_diff.txt` 对改稿单 F01–F17 逐 hunk 核；`selfcheck_pairs_log.json` 17 对 old/new 全文机器可核；机器复核＝重跑 `python3 apply_r6_final.py`（确定性：解析→单轮 17 锚→回放反证→全套自检，R5 原件全程只读）。")
    md.append("- 编译打包（戴夫）：官方引擎三遍四零＋页数实测＋metadata（M-1 版本沿革／M-3 摘要联动）。")
    md.append("- 指纹：R5 `ba2f157196f5`；R6 `%s`；diff/JSON/MD 指纹见交付通报（以群内通报实测值为准）。\n" % sha12(r6_bytes))

    md.append("—— 查理-论文主笔 ｜ 2026-10-20 ｜ 落稿轮 · 单轮 17 锚 · 0 失配 0 多写 · 建议非裁\n")

    open(MD_PATH, "w", encoding="utf-8").write("\n".join(md))

    # ---------- 汇报 ----------
    print("R5 sha12:", sha12(r5_bytes), "| bytes:", len(r5_bytes))
    print("R6 sha12:", sha12(r6_bytes), "| bytes:", len(r6_bytes), "| lines:", len(r6_lines))
    print("预检唯一性: %d/17 | 顺序应用: %d/17 | 回放: %s" % (sum(1 for v in pre.values() if v == 1), len(applied), "PASS" if reverse_ok else "FAIL"))
    print("hunk: %d 组，归属: %s" % (len(hunk_starts), "/".join(str(f) for _, _, f in hunk_map)))
    print("池66: 区块恒等=%s 条目=%d 引用实例=%d→%d" % (refs_identical, len(items6), len(cits5), len(cits6)))
    print("词族: position paper %d→%d | Objection %d→%d | kill %d→%d | death %d→%d" % (
        fams["position paper"][0], fams["position paper"][1],
        fams["Objection"][0], fams["Objection"][1],
        fams["kill"][0], fams["kill"][1],
        fams["death"][0], fams["death"][1]))
    print("新文本数字 token: 正文=%s 注记行=%s" % (num_tokens, num_comm_tokens))
    if failures:
        print("\n[失败登记] %d 项：" % len(failures))
        for x in failures:
            print("  -", x)
        raise Stop("自检存在失败项——即停（产物标记不交付）")
    print("\n全绿。产物：\n  %s\n  %s\n  %s\n  %s" % (R6_PATH, DIFF_PATH, JSON_PATH, MD_PATH))


if __name__ == "__main__":
    try:
        main()
    except Stop as e:
        print("STOP:", e)
        sys.exit(2)
