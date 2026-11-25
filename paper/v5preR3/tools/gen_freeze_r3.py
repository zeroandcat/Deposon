#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# gen_freeze_r3.py — FREEZE_v5preR3 冻结清单生成器（R3 谱系·沿 R2 链·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-26 07:21:08 派单「全稿合流后立 FREEZE_v5preR3（S-07 候立转立，含 rev2 中间锚
#   d924707），冻结生成／比对工具沿 R2 链」。
# 沿 R2 链的部分：sha12 指纹（sha256 前 12 位）·行数·字节·kind 分类·JSON+MD 双出·比对器逐位归因。
# 与 R2 不同：对象集换为 R3 谱系（paper/v5preR3 下五件＋两工具）；外部输入件按绝对路径记 sha12（只记不冻）；
#   无 live/active 活件行（R3 冻结时点全部 frozen）；吸收位状态单列。
# 用法：python3 gen_freeze_r3.py [--version N]   （在 repo 根或任意目录运行；路径按本文件位置解析）
# 输出：paper/v5preR3/evidence/FREEZE_v5preR3.json / .md
# ============================================================================
import hashlib, json, os, subprocess, sys, datetime

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


def main():
    version = arg("--version", int, 1)
    # ---- R3 谱系对象（repo 相对路径·frozen）----
    rel = lambda p: os.path.join(REPO, p)
    frozen = [
        row("论文 tex（rev3 全稿）", rel("paper/v5preR3/v5preR3_论文.tex"), "frozen", "§1–§7 合流·0 TODO·§4/§5 块 sha12 dc2665f05529 与 rev2 字节同一"),
        row("论文 pdf（tectonic 0.15.0）", rel("paper/v5preR3/v5preR3_论文.pdf"), "frozen", "22 页·0 未定义引用·0 错误"),
        row("bib（R2 91 键整继承＋34 条）", rel("paper/v5preR3/v5preR3_related_work.bib"), "frozen", "166 条·0 重键·65 条被引"),
        row("点火件（立项件）", rel("paper/v5preR3/v5preR3_点火件.md"), "frozen", "rev2 原件·0 动"),
        row("版本谱系对照表", rel("paper/v5preR3/v5preR3_版本谱系对照表.md"), "frozen", "rev3 更新：R3 状态＝全稿合流·S-07 候立转立"),
        row("冻结生成器", rel("paper/v5preR3/tools/gen_freeze_r3.py"), "frozen", "本件"),
        row("冻结比对器", rel("paper/v5preR3/tools/compare_freeze_r3.py"), "frozen", "沿 R2 compare_freeze 链·R3 口径"),
        row("kimi round10 问单", rel("paper/v5preR3/evidence/kimi_round10_prompt.txt"), "frozen", "F7/L2 原文贴入·逐字"),
        row("kimi round10 答复（逐字）", rel("paper/v5preR3/evidence/kimi_round10_answer_逐字.txt"), "frozen", "finish=stop·model kimi-k3.1-pro·0 代庖"),
        row("kimi round10 元数据", rel("paper/v5preR3/evidence/kimi_round10_answer_逐字.txt.meta.json"), "frozen", "usage/finish/model 原样"),
    ]
    # ---- R2 作废件（0 删·只记指纹·frozen）----
    r2 = [
        row("R2 论文 tex（VOIDED·0 删）", rel("paper/v5preR2_论文.tex"), "frozen", "6 行 VOIDED 头注·其余 0 动"),
        row("R2 作废标注", rel("paper/v5preR2_作废标注.md"), "frozen", ""),
        row("R2 冻结（不沿用·留档）", rel("paper/evidence/FREEZE_v5preR2.json"), "frozen", "S-06 旧位·R3 不建双冻结"),
    ]
    # ---- 外部输入件（绝对路径·external·只记 sha12 不冻）----
    ext = [
        ("S-A 本体源·对话集 docx", os.path.join(UPLOAD, "6b06e69a9f9cb7db60712f58_ai思考与量子突破.docx"), "M1–M4 原文"),
        ("S-B 定稿源·统一场论 v1 PDF", os.path.join(UPLOAD, "6a9e8687e7db4e2eabbaa67f_deposon_凝子_统一场论研究报告_v1.pdf"), "T-CONGELON-003"),
        ("阿兰 Lean 审读件包", os.path.join(SHARED, "阿兰_文献面收尾_T4勘误_引文补核_Lean审读_交付包_20261126"), "目录·v3.1 独立复现"),
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
            "parent_anchor_rev2": "d924707",
            "parent_anchor_rev1": "67a86e0",
            "fork_point_R2_terminal": "ac04a4b",
            "push": "0",
            "r2_freeze_reused": False,
        },
        "compile_state": {
            "engine": "tectonic 0.15.0",
            "pages": 22,
            "undefined_references": 0,
            "errors": 0,
            "overfull_inherited": "§4 标题行 6.37pt（与 rev2 同·§4/§5 0 改）",
            "cjk_warnings": "标题行 19 字·ptmb8t 无 CJK 字形·R2 同款既有状态·正文 0 CJK",
            "todo_markers": 0,
            "absorption_slots": 1,
        },
        "absorption_slot": {
            "section": "§2.8 Thermodynamic reconstruction: absorption slot (label sec:absorption)",
            "status": "OPEN",
            "owner": "爱丽丝（热力学重构·同期在做）",
            "closure_rule": "其件到达后走 rev3 吸收→重冻 FREEZE_v5preR3 v2（加入重构件自身指纹）",
        },
        "frozen": frozen,
        "r2_voided": r2,
        "external_inputs": external,
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "order_source": "群管理员 2026-11-26 07:21:08 派单（R3 全稿覆写·立 FREEZE_v5preR3·S-07 候立转立·含 rev2 中间锚 d924707）",
    }
    os.makedirs(EVID, exist_ok=True)
    jpath = os.path.join(EVID, "FREEZE_v5preR3.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)

    # ---- Markdown ----
    L = []
    L.append(f"# FREEZE_v5preR3 · v{version} — R3 谱系冻结事件（S-07 候立转立）\n")
    L.append(f"- 生成时间：{doc['generated_at']}　引擎：tectonic 0.15.0　页数：22　未定义引用：0　错误：0　TODO：0　吸收位：1（OPEN）")
    L.append(f"- 令源：{doc['order_source']}")
    ln = doc["lineage"]
    L.append(f"- 谱系：分支 `{ln['branch']}`·冻结时 HEAD `{ln['repo_head_at_freeze']}`·rev2 中间锚 `{ln['parent_anchor_rev2']}`·rev1 锚 `{ln['parent_anchor_rev1']}`·自 R2 终态 `{ln['fork_point_R2_terminal']}` 分出·0 推·不沿用 R2 冻结")
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
    L.append("\n## 丙｜外部输入件（external·绝对路径·只记 sha12）\n")
    L.append("| 件 | sha12 | 状态 | 备注 |")
    L.append("|---|---|---|---|")
    for r in external:
        L.append(f"| {r['label']} | `{r.get('sha12','—')}` | {r['status']} | {r.get('note','')} |")
    L.append("\n## 丁｜规则（沿 R2 链·写清）\n")
    L.append("1. **现役为准**：冻结以当前现役版本为准；旧版指纹作废留档，不两版并存。")
    L.append("2. **失效即重冻**：任一 frozen 件指纹变动 ⇒ 冻结失效，须重跑 `tools/gen_freeze_r3.py --version N+1` 并记变动原因。")
    L.append("3. **比对**：`python3 tools/compare_freeze_r3.py evidence/FREEZE_v5preR3.json` 重算现态并逐位比对；任一 frozen 件 content_changed ⇒ 失配·须处置（退出码 1）。")
    L.append("4. **吸收位**：§2.8 OPEN；爱丽丝热力学重构件到达 → rev3 吸收 → v2 重冻并加入重构件指纹；本轮不等。")
    L.append("5. **认证范围**：本冻结只证明「所名之件即所比之件·指纹如记」；不证明任何读数（读数在各席证据包·本稿引用不重测）。")
    L.append("\n## 戊｜边界\n")
    L.append("- 0 推·0 动已验代码（harness/ mcp/ plugin/ tests/ scripts/ paper/tools/ paper/rag/ paper/evidence/ 中 R2 件 0 动；R3 工具为新增件·置于 paper/v5preR3/tools/）·0 改他席在册件。")
    L.append(f"\n*查理-论文主笔 · {doc['generated_at'][:10]} · FREEZE_v5preR3 v{version}*")
    with open(os.path.join(EVID, "FREEZE_v5preR3.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("OK ->", jpath)
    for r in frozen:
        print(f"  {r.get('sha12','MISSING')}  {r['path'].replace(REPO+'/', '')}")


if __name__ == "__main__":
    main()
