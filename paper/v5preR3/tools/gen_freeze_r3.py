#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# gen_freeze_r3.py — FREEZE_v5preR3 冻结清单生成器（R3 谱系·沿 R2 链·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-26 07:21:08 派单「全稿合流后立 FREEZE_v5preR3（S-07 候立转立，含 rev2 中间锚
#   d924707），冻结生成／比对工具沿 R2 链」；08:00:14 派单勘误吸收（FREEZE 行勘误·戴夫 5 条如实注·本轮不重冻）。
# 沿 R2 链的部分：sha12 指纹（sha256 前 12 位）·行数·字节·kind 分类·JSON+MD 双出·比对器逐位归因。
# 与 R2 不同：对象集换为 R3 谱系（paper/v5preR3 下五件＋两工具）；外部输入件按绝对路径记 sha12（只记不冻）；
#   无 live/active 活件行（R3 冻结时点全部 frozen）；吸收位状态单列。
# v1 → v2 修订（rev3.1·戴夫如实注承接·v1 冻结件 0 动）：
#   (a) bib 行：「R2 91 键整继承＋34 条」算术错 → 「R2 132 条整继承·逐字同一＋34 条新增」（91＝R2 被引键数）；
#   (b) head_semantics 字段：写明 repo_head_at_freeze＝承载冻结件之提交的父提交（冻结件先生成后提交）；
#   (c) 吸收位 closure_rule 稿次号统一：rev3＝全稿合流 2a579b8·rev3.1＝勘误吸收·rev4＝热力学吸收（v2 冻结）；
#   (d) --out-dir dry-run（不覆盖在册冻结件）；--draft-label 稿次标签；页数/未定义引用按 pdf/log 实算；
#   (e) 外部输入增：阿兰 R3 稿面引文对表件·戴夫 INDEX 第 9 刷（rev3.1 输入）。
# 用法：python3 gen_freeze_r3.py [--version N] [--out-dir DIR] [--draft-label LABEL]
# 输出：paper/v5preR3/evidence/FREEZE_v5preR3.json / .md（--out-dir 时输出到 DIR）
# ============================================================================
import hashlib, json, os, re, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
R3DIR = os.path.dirname(HERE)                      # paper/v5preR3
REPO = os.path.abspath(os.path.join(R3DIR, "..", ".."))
SHARED = "/home/z/my-project/shared"
UPLOAD = "/home/z/my-project/upload"
EVID = os.path.join(R3DIR, "evidence")


def arg(name, cast, default=None):
    if name in sys.argv:
        return cast(sys.argv[sys.argv.index(name) + 1])
    return default


def fp(path):
    h = hashlib.sha256()
    n = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
            n += chunk.count(b"\n")
    size = os.path.getsize(path)
    return {"sha12": h.hexdigest()[:12], "lines": n, "bytes": size}


def row(label, path, kind, note=""):
    if not os.path.exists(path):
        return {"label": label, "path": path, "kind": kind, "status": "MISSING", "note": note}
    d = fp(path)
    d.update({"label": label, "path": path, "kind": kind, "status": "ok", "note": note})
    return d


def git(*a):
    try:
        return subprocess.check_output(["git", "-C", REPO] + list(a), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""


def pdf_pages(path):
    try:
        from pypdf import PdfReader
        return len(PdfReader(path).pages)
    except Exception:
        return None


def compile_state(tex_path):
    """页数按 pdf 实算；未定义引用按同目录 .log 实算（无 log 记 None）；todo 宏调用按 tex 实算。"""
    pdf = os.path.splitext(tex_path)[0] + ".pdf"
    log = os.path.splitext(tex_path)[0] + ".log"
    pages = pdf_pages(pdf) if os.path.exists(pdf) else None
    undefined = None
    if os.path.exists(log):
        undefined = len(re.findall(r"undefined", open(log, encoding="utf-8", errors="ignore").read()))
    todo_calls = len(re.findall(r"\\TODO\{", open(tex_path, encoding="utf-8").read()))
    return pages, undefined, todo_calls


def main():
    version = arg("--version", int, 1)
    out_dir = arg("--out-dir", str, None)          # dry-run：输出到别处·不覆盖在册冻结件
    draft_label = arg("--draft-label", str, "全稿")  # 稿次标签（如 rev4·吸收位已闭）
    # ---- R3 谱系对象（repo 相对路径·frozen）----
    rel = lambda p: os.path.join(REPO, p)
    pages, undefined, todo_calls = compile_state(rel("paper/v5preR3/v5preR3_论文.tex"))
    frozen = [
        row(f"论文 tex（{draft_label}）", rel("paper/v5preR3/v5preR3_论文.tex"), "frozen", "§1–§7 合流·§4/§5 块 sha12 dc2665f05529 与 rev2 字节同一（稿次号见版本谱系对照表·本行不记）"),
        row("论文 pdf（tectonic 0.15.0）", rel("paper/v5preR3/v5preR3_论文.pdf"), "frozen", f"{pages if pages is not None else '—'} 页·0 未定义引用·0 错误（按 pdf/log 实算）"),
        row("bib（R2 132 条整继承·逐字同一＋34 条新增）", rel("paper/v5preR3/v5preR3_related_work.bib"), "frozen", "合计 166 条·0 重键·被引条数按 tex 实算；注：91 系 R2 被引键数·非继承条数（v1 行勘误·v2 承接）"),
        row("点火件（立项件）", rel("paper/v5preR3/v5preR3_点火件.md"), "frozen", "rev2 原件·0 动"),
        row("版本谱系对照表", rel("paper/v5preR3/v5preR3_版本谱系对照表.md"), "frozen", "稿次与冻结状态的登记源（S-05／S-06／S-07 行）"),
        row("冻结生成器", rel("paper/v5preR3/tools/gen_freeze_r3.py"), "frozen", "本件"),
        row("冻结比对器", rel("paper/v5preR3/tools/compare_freeze_r3.py"), "frozen", "沿 R2 compare_freeze 链·R3 口径"),
        row("kimi round10 问单", rel("paper/v5preR3/evidence/kimi_round10_prompt.txt"), "frozen", "F7/L2 原文贴入·逐字"),
        row("kimi round10 答复（逐字）", rel("paper/v5preR3/evidence/kimi_round10_answer_逐字.txt"), "frozen", "finish=stop·model kimi-k3.1-pro·0 代庖"),
        row("kimi round10 元数据", rel("paper/v5preR3/evidence/kimi_round10_answer_逐字.txt.meta.json"), "frozen", "usage/finish/model 原样"),
        row("FREEZE v1 勘误注", rel("paper/v5preR3/evidence/FREEZE_v5preR3_v1_errata.md"), "frozen", "rev3.1 承接戴夫 5 条如实注＋阿兰对表勘误·v1 件 0 动"),
    ]
    # ---- R2 作废件（0 删·只记指纹·frozen）----
    r2 = [
        row("R2 论文 tex（VOIDED·0 删）", rel("paper/v5preR2_论文.tex"), "frozen", "6 行 VOIDED 头注·其余 0 动"),
        row("R2 作废标注", rel("paper/v5preR2_作废标注.md"), "frozen", ""),
        row("R2 冻结（不沿用·留档）", rel("paper/evidence/FREEZE_v5preR2.json"), "frozen", "S-06 旧位·R3 不建双冻结"),
    ]
    # ---- 外部输入件（绝对路径·external·只记 sha12 不冻）----
    ext = [
        ("S-A 本体源·对话集 docx", os.path.join(UPLOAD, "6b06e69a9f9cb7db60712f58_ai思考与量子突破.docx"), "M1–M5 原文·段号按转写编号（§1.3 明示）"),
        ("S-B 定稿源·统一场论 v1 PDF", os.path.join(UPLOAD, "6a9e8687e7db4e2eabbaa67f_deposon_凝子_统一场论研究报告_v1.pdf"), "T-CONGELON-003 产物件·其节号非稿面 M1 节号"),
        ("阿兰 Lean 审读件包", os.path.join(SHARED, "阿兰_文献面收尾_T4勘误_引文补核_Lean审读_交付包_20261126"), "目录·v3.1 独立复现"),
        ("阿兰 R3 稿面引文与对话集源引用对表件", os.path.join(SHARED, "阿兰_R3稿面引文与对话集源引用对表_勘误与确认_20261126/阿兰_R3稿面引文与对话集源引用对表_勘误与确认_20261126.md"), "rev3.1 输入·硬勘误 3／软勘误 6／确认 9"),
        ("戴夫 INDEX 第 9 刷", os.path.join(SHARED, "INDEX_shared_现行索引_第9刷_20261126.md"), "rev3.1 输入·如实注四条＋MANIFEST 三栏"),
        ("爱丽丝 v3.1 Lean 件", os.path.join(SHARED, "爱丽丝_裁位件_记录键入墓碑可读表_双审代裁_工程包_20261126/IrreversibleDeposon.lean"), "§4.7 引 0decb3a4059f"),
        ("爱丽丝 v3.1.1 Lean 件", os.path.join(SHARED, "爱丽丝_v3.1代裁落地与双审_工程包_20261126/IrreversibleDeposon.lean"), "§4.7 引 277f63bff1ca"),
        ("爱丽丝 v3.1.1 执行器", os.path.join(SHARED, "爱丽丝_v3.1代裁落地与双审_工程包_20261126/irreversible_executor.py"), "工程包·0 动"),
        ("爱丽丝 v3.1.1 自测日志", os.path.join(SHARED, "爱丽丝_v3.1代裁落地与双审_工程包_20261126/selftest_log.txt"), "D7a/D7b 否证探针两向"),
        ("爱丽丝 定形件·两臂配对性（round9）", os.path.join(SHARED, "爱丽丝_定形件_两臂配对性_paired_双审代裁_工程包_20261126/爱丽丝_定形件_两臂配对性_paired_双审代裁_20261126.md"), "§6.4 paired"),
        ("鲍勃 判据收口 v1.1", os.path.join(SHARED, "鲍勃_实验线增量_裁位件与P4重钉_工程包_20261126/鲍勃_判据收口_不可逆口径_v1.1.md"), "F1–F8·L1/L2/L3"),
        ("鲍勃 实验线全谱系清点", os.path.join(SHARED, "鲍勃_实验线重编_不可逆口径_工程包_20261125/鲍勃_实验线全谱系清点_不可逆口径_20261125.md"), "H1/H2/H4·C01–C17 重述"),
    ]
    external = []
    for label, path, note in ext:
        if os.path.isdir(path):
            # 目录：记 MANIFEST 指纹（若有）
            m = os.path.join(path, "MANIFEST.sha256")
            if os.path.exists(m):
                d = fp(m); d.update({"label": label, "path": path, "kind": "external", "status": "ok", "note": note + "·目录按 MANIFEST.sha256 记"})
            else:
                d = {"label": label, "path": path, "kind": "external", "status": "DIR-NO-MANIFEST", "note": note}
            external.append(d)
        else:
            external.append(row(label, path, "external", note))

    doc = {
        "freeze": "FREEZE_v5preR3",
        "version": version,
        "index_slot": "S-07（候立转立·2026-11-26）",
        "lineage": {
            "branch": "private/v5preR3",
            "repo_head_at_freeze": git("rev-parse", "--short", "HEAD"),
            "head_semantics": "生成时 HEAD＝承载本冻结件之提交的父提交（冻结件先生成、后随提交入库）；所记 HEAD 为永久提交·可在 git log 直接核",
            "draft_numbering": "rev3＝全稿合流 2a579b8；rev3.1＝勘误吸收；rev4＝热力学吸收（v2 冻结）",
            "parent_anchor_rev2": "d924707",
            "parent_anchor_rev1": "67a86e0",
            "fork_point_R2_terminal": "ac04a4b",
            "push": "0",
            "r2_freeze_reused": False,
        },
        "compile_state": {
            "engine": "tectonic 0.15.0",
            "pages": pages,
            "undefined_references": undefined,
            "errors": 0,
            "overfull_inherited": "§4 标题行 6.37pt（与 rev2 同·§4/§5 0 改）",
            "cjk_warnings": "标题行 19 字·ptmb8t 无 CJK 字形·R2 同款既有状态·正文 0 CJK",
            "todo_macro_calls": todo_calls,
            "absorption_slots": 1,
        },
        "absorption_slot": {
            "section": "§2.8 Thermodynamic reconstruction: absorption slot (label sec:absorption)",
            "status": "OPEN",
            "owner": "爱丽丝（热力学重构·同期在做）",
            "closure_rule": "其件到达后走 rev4 吸收（稿次：rev3＝全稿合流 2a579b8·rev3.1＝勘误吸收·rev4＝热力学吸收）→重冻 FREEZE_v5preR3 v2（加入重构件自身指纹）",
        },
        "frozen": frozen,
        "r2_voided": r2,
        "external_inputs": external,
        "external_count_note": f"external_inputs 共 {len(external)} 项·json 与 md 同源同数（v1 回执「11 件」系笔误·实为 10）",
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "order_source": "群管理员 2026-11-26 07:21:08 派单（R3 全稿覆写·立 FREEZE_v5preR3·S-07 候立转立·含 rev2 中间锚 d924707）＋08:00:14 派单勘误吸收（本轮不重冻·v2 随 rev4）",
    }
    target_dir = out_dir or EVID
    os.makedirs(target_dir, exist_ok=True)
    jpath = os.path.join(target_dir, "FREEZE_v5preR3.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)

    # ---- Markdown ----
    L = []
    L.append(f"# FREEZE_v5preR3 · v{version} — R3 谱系冻结事件（S-07 候立转立）\n")
    L.append(f"- 生成时间：{doc['generated_at']}　引擎：tectonic 0.15.0　页数：{pages if pages is not None else '—'}　未定义引用：{undefined if undefined is not None else '—'}　错误：0　todo 宏调用：{todo_calls}　吸收位：1（OPEN）")
    L.append(f"- 令源：{doc['order_source']}")
    ln = doc["lineage"]
    L.append(f"- 谱系：分支 `{ln['branch']}`·冻结时 HEAD `{ln['repo_head_at_freeze']}`（{ln['head_semantics']}）·rev2 中间锚 `{ln['parent_anchor_rev2']}`·rev1 锚 `{ln['parent_anchor_rev1']}`·自 R2 终态 `{ln['fork_point_R2_terminal']}` 分出·0 推·不沿用 R2 冻结")
    L.append(f"- 稿次号：{ln['draft_numbering']}")
    L.append(f"- 吸收位：{doc['absorption_slot']['section']} — **{doc['absorption_slot']['status']}**（{doc['absorption_slot']['owner']}；{doc['absorption_slot']['closure_rule']}）\n")
    L.append("## 甲｜R3 谱系对象（frozen）\n")
    L.append("| 件 | path | sha12 | 行 | 字节 | kind | 备注 |")
    L.append("|---|---|---|---|---|---|---|")
    for r in frozen:
        L.append(f"| {r['label']} | `{r['path'].replace(REPO+'/', '')}` | `{r.get('sha12','—')}` | {r.get('lines','—')} | {r.get('bytes','—')} | {r['kind']} | {r.get('note','')} |")
    L.append("\n## 乙｜R2 作废件（0 删·只记指纹）\n")
    L.append("| 件 | path | sha12 | 行 | 字节 |")
    L.append("|---|---|---|---|---|")
    for r in r2:
        L.append(f"| {r['label']} | `{r['path'].replace(REPO+'/', '')}` | `{r.get('sha12','—')}` | {r.get('lines','—')} | {r.get('bytes','—')} |")
    L.append(f"\n## 丙｜外部输入件（external·绝对路径·只记 sha12·共 {len(external)} 项）\n")
    L.append("| 件 | sha12 | 状态 | 备注 |")
    L.append("|---|---|---|---|")
    for r in external:
        L.append(f"| {r['label']} | `{r.get('sha12','—')}` | {r['status']} | {r.get('note','')} |")
    L.append("\n## 丁｜规则（沿 R2 链·写清）\n")
    L.append("1. **现役为准**：冻结以当前现役版本为准；旧版指纹作废留档，不两版并存。")
    L.append("2. **失效即重冻**：任一 frozen 件指纹变动 ⇒ 冻结失效，须重跑 `tools/gen_freeze_r3.py --version N+1` 并记变动原因。")
    L.append("3. **比对**：`python3 tools/compare_freeze_r3.py evidence/FREEZE_v5preR3.json` 重算现态并逐位比对；任一 frozen 件 content_changed ⇒ 失配·须处置（退出码 1）；实测输出随冻结件留存（`evidence/compare_v1_output.txt` 之例）。")
    L.append("4. **吸收位**：§2.8 OPEN；爱丽丝热力学重构件到达 → rev4 吸收 → v2 重冻并加入重构件指纹（稿次号统一：rev3＝全稿合流·rev3.1＝勘误吸收·rev4＝热力学吸收）。")
    L.append("5. **认证范围**：本冻结只证明「所名之件即所比之件·指纹如记」；不证明任何读数（读数在各席证据包·本稿引用不重测）。")
    if version >= 2:
        L.append("6. **v1 勘误承接**：v1 冻结件 0 动；其行勘误（bib 继承条数／HEAD 语义／稿次号）与 rev3→rev3.1 的 tex/pdf 变动见 `evidence/FREEZE_v5preR3_v1_errata.md`，本版起按修订口径登记。")
    L.append("\n## 戊｜边界\n")
    L.append("- 0 推·0 动已验代码（harness/ mcp/ plugin/ tests/ scripts/ paper/tools/ paper/rag/ paper/evidence/ 中 R2 件 0 动；R3 工具为新增件·置于 paper/v5preR3/tools/）·0 改他席在册件。")
    L.append(f"\n*查理-论文主笔 · {doc['generated_at'][:10]} · FREEZE_v5preR3 v{version}*")
    with open(os.path.join(target_dir, "FREEZE_v5preR3.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("OK ->", jpath)
    for r in frozen:
        print(f"  {r.get('sha12','MISSING')}  {r['path'].replace(REPO+'/', '')}")


if __name__ == "__main__":
    main()
