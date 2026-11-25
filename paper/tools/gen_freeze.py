#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# gen_freeze.py — 冻结清单生成器（v5preR2 重做令③·就既有树·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# v5 补冻①（2026-11-25 16:46:40 令·⑪ 同窗）：L54 总索引路径改八位形（戴夫改名·sha12 恒等）；launch 行 kind 由相对路径字串改 "source"（戴夫旁注·本席定修·path 不换）；freezer/rule 补冻文案。
# v5 令源：PI 2026-11-25 15:36:56 裁决④「合流后重冻 v5·merge·bundle 往返·0 推」＋群管理员 16:03:29 派单（bundle 校验→--no-ff 合入 b8cbbeb→重跑本器→与 v4 逐行对拍）。
#   本轮改动：LAUNCH_V5→LAUNCH_V7（爱丽丝 PI1536裁决五项/5_launch_v7·5714ae414657）；STALE 增第五轮三条（§8／evidence-rounds／launch v5→v7）；FACTS F2 入册位改已裁＋F3 合流记录；
#   阈值 PR-1/PR-2/ST-6 状态按 PI ①；pending_ruling 改已裁留档；render_md 标题/令源/谱系改 v5。量测逻辑 0 触。
# v4 令源（前轮留档）：群管理员 2026-11-25 12:05:07「重冻 §8 一行（爱丽丝已按令追加 OpenSDK 重试与
#   本地轮记录）：docs/thermo-generation.md 现役 497a5aa3d61f · 676 行 · 46046 字节（原
#   9d616afc08ef · 544 行 · 35934 B）。只重冻这一行，其余 40 项指纹不动；FREEZE v3→v4，
#   重出比对 0 失配。论文与冻结清单同步两笔事实：① OpenSDK 四个官方 SDK、生成族 8 例仍全
#   400「Request path cannot be relayed」，拒中继在路径层，载体不变；② 本地 Qwen3-0.6B 轮
#   （Apache-2.0·非预注册载体·不填槽）第三幕 0 次读工具，幻肢回射空集不可算。本地轮是否入册
#   由 PI 定：先不入册，稿内标为待裁。」
# 重冻规则（见 §零）：现役 v4 为准·旧 v3 冻结指纹作废并留档；本轮只动 1 行（§8 一行），
#   其余 40 项指纹逐位不动。
# 旧令源：群管理员 2026-11-25 10:14:57 重做令③「冻结」＋ 10:37:13「两帐树要在既有帐树上
#       更新，不得另起一套」＋ 爱丽丝报两处待处置：
#         ① launch-v5preR2.md 冻的是 v2（221a454c81e9）而现役 v3（8d7b1727a3b1）
#         ② thermo-generation.md §8 已按令更新（c323a7c / 0127ca353bef），冻结指纹需重冻或豁免
# 冻结对象（**全部指向既有树固定名件·不另建并行树**）：
#   ① 记忆帐树 = 既有记忆册树 10 件 ＋ 既有帐树现态面 2 件（12 件）
#   ② 实验帐树 = 既有实验册树 5 件（含归档 4）＋ 证据件 5 ＋ 仓内证据面 13（23 件）
#   ③ 记忆 RAG ＋ 实验 RAG（各自独立·索引与入口脚本）
#   ④ 预注册带阈值（13 条·候 PI 冻结）
# 重冻规则（见 §五）：现役 v3 为准·旧 v2 冻结指纹作废并留档；thermo-generation.md §8 更新
#   属 docs 类，按「重冻不豁免」处置——重冻后旧指纹留档备查、现役指纹入册。
# 纪律：冻结后不再改动；本件只读实测·0 改源文件·凭据 0 入册。
# 用法：python3 paper/tools/gen_freeze.py
# ============================================================================
import hashlib, json, os, sys, time

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHARED = "/home/z/my-project/shared"
OUT = os.path.join(HERE, "paper", "evidence")

# ---- 既有树固定名件（不另起一套）----
MEM_MEMORY = [
    ("记忆册树", "查理_底账树/分册1_建账与故障恢复协议.md", "frozen"),
    ("记忆册树", "查理_底账树/分册2_PI补喂逐字_P01-P54.md", "frozen"),
    ("记忆册树", "查理_底账树/分册3_PI补喂逐字_P55-P93.md", "frozen"),
    ("记忆册树", "查理_底账树/分册4_PI补喂逐字_P94-P133.md", "frozen"),
    ("记忆册树", "查理_底账树/分册5_指令链与裁定总目_P01-P133.md", "frozen"),
    ("记忆册树", "查理_底账树/分册6_诗面文本与R6约束.md", "frozen"),
    ("记忆册树", "查理_底账树/分册7_尾注续跑清单.md", "frozen"),
    ("记忆册树", "查理_底账树/分册8_尾行滚动史_折入53-147.md", "frozen"),
    ("记忆册树", "查理_底账树/查理_底账树_根索引_2026_11_11.md", "index"),
    ("记忆册树", "查理_底账树/查理_底账树_活跃分册_P134起_2026_11_11.md", "active"),
    ("帐树现态面", "查理_帐树实例_现态快照面.md", "live"),
    ("帐树现态面", "查理_帐树实例_鲜活例案面.md", "live"),
]
EXP_TREE = [
    ("实验册树", "查理_全量实验谱系总索引_20261122.md", "index"),   # ⑪ 八位形（原 _2026_11_22·sha12 249d8ec2ff7a 恒等）
    ("实验册树", "02_归档/2026-11/_散件/爱丽丝_实验树记忆树并列审计_A轨主笔_20261116.md", "frozen"),
    ("实验册树", "02_归档/2026-11/_散件/戴夫_实验树记忆树并列审计_B副签双盲复核_20261116.md", "frozen"),
    ("实验册树", "02_归档/2026-11/_散件/戴夫_实验树记忆树审计_交叉对账合判_AB双审闭合_20261116.md", "frozen"),
    ("实验册树", "02_归档/2026-11/_散件/查理_遗忘实验普查与实验册树增补_v1.2_20261119.md", "frozen"),
]
EXP_EVIDENCE = [
    ("实验证据件", "paper/evidence/python_tree.json", "tree"),
    ("实验证据件", "paper/evidence/python_tree.md", "tree"),
    ("实验证据件", "paper/evidence/lean_tree.json", "machine"),
    ("实验证据件", "paper/evidence/lean_tree.md", "machine"),
    ("实验证据件", "paper/evidence/lean_build_66b53fc.log", "machine"),
]
REPO_EVIDENCE = [
    "docs/thermo-generation.md", "docs/evidence-rounds.md", "docs/readings-package-spec.md",
    "docs/slot-space-caliber.md", "README.md", "BENCHMARK.md",
    "mcp/thermo_core.py", "mcp/thermo_demo.py", "mcp/thermo_crosscheck.py",
    "harness/DeposonThermo.lean", "harness/lean_axiom_audit.py", "harness/thermo_live_round.py",
]
# 发射案现役 v7（PI 15:36 裁决回填轮·冻结落档·爱丽丝 5_launch_v7/freeze_record.txt 5714ae414657·368 行·46865 B）
LAUNCH_V7 = ("仓内证据面", os.path.join(
    SHARED, "爱丽丝_PI1536裁决五项_20261125/5_launch_v7/launch-v5preR2.md"),
    "source")  # 补冻修正：kind 原误填相对路径字串（戴夫旁注）→ 类别词 source；path 维持绝对路径（v3 起·compare 键不换）

# 待处置项留档（爱丽丝报·旧指纹作废留档）
STALE = [
    {"item": "launch-v5preR2.md", "old_fp": "221a454c81e9", "old_version": "v2（2026-11-25 08:36）",
     "new_fp": "8d7b1727a3b1", "new_version": "v3（2026-11-25 根因分诊轮修订）",
     "action": "旧 v2 冻结指纹作废并留档；现役 v3 入册（288 行·29,526 B）",
     "reason": "发射案随真机 L1 根因分诊轮修订至 v3，冻结须以现役为准"},
    {"item": "thermo-generation.md", "old_fp": None,
     "old_version": "§8 第二次分诊（66b53fc 时点）",
     "new_fp": "0127ca353bef", "new_version": "§8 第三次分诊＋(b) 试验记录（c323a7c·428 行·27,923 B）",
     "action": "重冻不豁免——现役指纹入册·旧时点读数留档备查",
     "reason": "§8 已按令更新（第三次分诊 55 例＋(b) 试验），属 docs 类证据更新，不豁免·重冻"},
    # ---- 第三轮重冻（2026-11-25 11:29 令·载体换新）----
    {"item": "thermo-generation.md", "old_fp": "0127ca353bef",
     "old_version": "§8 第三次分诊（c323a7c·428 行·27,923 B）",
     "new_fp": "9d616afc08ef", "new_version": "§8 载体换新轮（f2bf413·544 行·35,934 B）",
     "action": "重冻不豁免——现役指纹入册·旧时点读数留档备查",
     "reason": "载体按用户令 11:23 换为 `xiaomi/mimo-v2.6-flash-mopd`（2026-11-23 发布·MIT）后 11:26 点火仍被挡；§8 增载体换新段"},
    {"item": "launch-v5preR2.md", "old_fp": "8d7b1727a3b1",
     "old_version": "v3（2026-11-25 根因分诊轮修订·288 行·29,526 B）",
     "new_fp": "b305ae811efa", "new_version": "v5（2026-11-25 载体换新轮修订·298 行·32,351 B）",
     "action": "重冻不豁免——现役 v5 入册·旧 v3 作废留档",
     "reason": "载体换新轮修订至 v5（v4 = 11:00 换正式版·v5 = 11:23 换最新开源载体）；路径改指「最新开源载体点火_BLOCKED」包"},
    # ---- 第四轮重冻（2026-11-25 12:05 令·重冻 §8 一行）----
    {"item": "thermo-generation.md", "old_fp": "9d616afc08ef",
     "old_version": "§8 载体换新轮（f2bf413·544 行·35,934 B）",
     "new_fp": "497a5aa3d61f", "new_version": "§8 OpenSDK 重试＋本地轮记录（b8887c0·676 行·46,046 B）",
     "action": "重冻不豁免·只动这一行——现役指纹入册·旧指纹作废留档",
     "reason": "爱丽丝按令追加 OpenSDK 四官方 SDK 重试（生成族 8 例仍全 400·拒中继在路径层·载体不变）"
               "与本地 Qwen3-0.6B 轮（第三幕 0 次读工具·幻肢回射空集不可算）；增 132 行"},
    # ---- 第五轮重冻（2026-11-25 16:03 令·PI 15:36 裁决④ 合流后重冻 v5）----
    {"item": "thermo-generation.md", "old_fp": "497a5aa3d61f",
     "old_version": "§8 OpenSDK 重试＋本地轮记录（b8887c0·676 行·46,046 B）",
     "new_fp": "0f6f96f1e4de", "new_version": "§8 AgentMore 假设分诊记录＋改道 teamorouter＋L1 PASS（7796c7e·829 行·56,917 B）",
     "action": "重冻不豁免——合流入册后现役指纹入册·旧指纹作废留档",
     "reason": "爱丽丝私支 4 提交（28bf95b/2d4402f/1ac596e/7796c7e）经 bundle 校验后 --no-ff 合入 b8cbbeb；§8 增 153 行"},
    {"item": "evidence-rounds.md", "old_fp": "c6e4ce8e66dd",
     "old_version": "v4 时点在册版",
     "new_fp": "d3d662acce82", "new_version": "本地 Qwen3-0.6B 轮退化轮指针行（1ac596e·42 行·8,786 B）",
     "action": "重冻不豁免——PI ② 追认「退化轮指针行」·合流后现役指纹入册",
     "reason": "爱丽丝 13:11 令下自择第 3 件：入册为退化轮指针行（不计预注册判据·不填槽·L1 仍 BLOCKED）→PI 15:36:56 追认"},
    {"item": "launch-v5preR2.md", "old_fp": "b305ae811efa",
     "old_version": "v5（2026-11-25 载体换新轮修订·298 行·32,351 B）",
     "new_fp": "5714ae414657", "new_version": "v7（2026-11-25 PI 15:36 裁决回填轮·冻结落档·368 行·46,865 B）",
     "action": "重冻不豁免——现役 v7 入册·旧 v5 作废留档；路径改指「PI1536裁决五项/5_launch_v7」包",
     "reason": "§8.3 五项按 PI 裁决回填（OR 关闭确认／键级账本 L2 首轮／基准⑤缓至 L2 出数后／预注册带冻结现三带／双出口选做）；v6 = 13:54 AgentMore 分辨＋端点改道轮"},
]

# 本轮同步入册的两笔事实（令：论文与冻结清单同步·读数诚实不填估值）
FACTS = [
    {"id": "F1", "item": "OpenSDK 重试（拒中继在路径层·载体不变）",
     "reading": "四个官方 SDK（openai-node 7.64.0、@openrouter/sdk 1.5.139、openai-py 3.59.0、"
                "openrouter-py 1.3.211）·生成族 8 例（chat/completions ×6、responses ×2）"
                "全部 400「Request path cannot be relayed」·响应体逐字节相同·同一网关 release·"
                "error-origin=client；同 SDK 同 key 读路径 4 例全 200（models 440 条·credits 20 / 11.313）",
     "reading_is": "拒中继在路径层（与 SDK·请求头·序列化无关）；载体不变，仍 `xiaomi/mimo-v2.6-flash-mopd`；"
                   "未作第四次点火，S1–S13 待测、S14 BLOCKED、S16 载体与 S16b/S17 不变",
     "slots_filled": 0},
    {"id": "F2", "item": "本地 Qwen3-0.6B 轮（非预注册载体·不填槽）",
     "reading": "载体 `Qwen/Qwen3-0.6B`（Apache-2.0·非预注册·比 11:23「近期」档旧）·驱动器 0 改动"
                "（sha12 e4bd79583ce8·仅覆盖 API_URL）·11:56:00–11:59:29·208 s·6 次请求·cost 0；"
                "幕一写 3/3·D=1672·利用率 64.31%·守恒 2620=20+0+1672+928；幕三 0 次读工具调用 "
                "⇒ 幻肢回射 n_ph=0 / R=0·空集不可算·honest=True 属空集退化值·不作 PASS",
     "reading_is": "本地轮 0 云调用跑通管线，但幻肢读数在这台载体上测不出；不填任何槽位、不是 L1；"
                   "入册位已裁（PI 15:36:56 ②）：**追认爱丽丝自择「退化轮指针行」**——`docs/evidence-rounds.md` 指针行在册（1ac596e·合流入册）·"
                   "稿面 §4.7 已同步（1ad9218）：entered as a degradation-round pointer row·不计预注册判据·不填槽·L1 仍 BLOCKED（OpenRouter 径）",
     "slots_filled": 0},
    {"id": "F3", "item": "私仓合流＋§8 L1 PASS 记录（PI 15:36 裁决④·管理员 16:03 派单）",
     "reading": "爱丽丝私支 `7796c7e`（分叉点 `b8887c0` 后 4 提交·11 文件：docs/ 2＋openrouter/ 9 新目录·+1306/−0）"
                "经 bundle（sha256 bae132fd…478f·complete history·凭据扫描 0 命中）校验后 `--no-ff` 合入 → `b8cbbeb`（父 `1ad9218`＋`7796c7e`·0 冲突·0 推）；"
                "已验代码 0 触（mcp/ harness/ scripts/ package.json tests/ gates/ plugin/ diff 空·thermo_core f47d4ab7700c／thermo_live_round e4bd79583ce8 恒等）；"
                "稿面 paper/ 0 触（tex efeaa8053ca0／pdf 1b925c0a1f6a 恒等）。§8 现役载 L1 真机轮 PASS 13:51（用户令 13:47 改道 teamorouter·载体 mimo-v2.6-flash·16.6 s·13,853 tok·门拒 2·D 1692·利用率 65.08%）",
     "reading_is": "合流口径：两席各自 2／4 提交分立合入·0 改对方件；**稿面 §4.7「The real-model round is blocked」系 b8887c0 时点口径·滞后于 13:51 L1 PASS——稿面是否吸收 L1 PASS 读数候裁（非本轮令·0 自改）**；"
                   "L1 PASS 读数归爱丽丝件（回执 9cf1bc0fe700·读数包 l1_teamorouter_1351）",
     "slots_filled": 0},
]


def fp(p):
    raw = open(p, "rb").read()
    return hashlib.sha256(raw).hexdigest()[:12], raw.count(b"\n"), len(raw)


def measure(rows, base):
    out, missing = [], []
    for tree, rel, kind in rows:
        p = rel if os.path.isabs(rel) else os.path.join(base, rel)
        if not os.path.exists(p):
            missing.append(rel); continue
        h, ln, by = fp(p)
        out.append({"tree": tree, "path": rel, "kind": kind, "sha12": h, "lines": ln, "bytes": by})
    return out, missing


def main():
    t0 = time.time()
    mem, miss1 = measure(MEM_MEMORY, SHARED)
    exp, miss2 = measure(EXP_TREE, SHARED)
    exp2, miss3 = measure(EXP_EVIDENCE, HERE)
    exp3, miss4 = measure([("仓内证据面", r, "source") for r in REPO_EVIDENCE], HERE)
    launch, miss5 = measure([LAUNCH_V7], HERE)
    exp += exp2 + exp3 + launch
    missing = miss1 + miss2 + miss3 + miss4 + miss5
    # 两 RAG 实测
    rag = []
    for name, files in {
        "记忆 RAG": ["paper/rag/memory/index.json", "paper/rag/memory/build_memory_rag.py",
                 "paper/rag/memory/query_memory.py"],
        "实验 RAG": ["paper/rag/experiment/index.json", "paper/rag/experiment/build_experiment_rag.py",
                 "paper/rag/experiment/query_experiment.py"]}.items():
        for rel in files:
            p = os.path.join(HERE, rel)
            if os.path.exists(p):
                h, ln, by = fp(p)
                rag.append({"rag": name, "path": rel, "sha12": h, "lines": ln, "bytes": by})
            else:
                missing.append(rel)
    # 冻结分册恒定性核验
    root_txt = open(os.path.join(SHARED, "查理_底账树/查理_底账树_根索引_2026_11_11.md"),
                    encoding="utf-8").read()
    recorded = dict(re.findall(
        r"\|\s*分册(\d)_[^|]*?\.md\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*`([0-9a-f]{12})`\s*\|", root_txt))
    fchk = []
    for n in mem:
        m = re.search(r"分册(\d)_", n["path"])
        if m and m.group(1) in recorded:
            fchk.append({"volume": int(m.group(1)), "recorded": recorded[m.group(1)],
                         "measured": n["sha12"], "equal": recorded[m.group(1)] == n["sha12"]})
    # 逐位对表（Python/Lean 证据件）
    xcheck = []
    pj = os.path.join(HERE, "paper/evidence/python_tree.json")
    lj = os.path.join(HERE, "paper/evidence/lean_tree.json")
    if os.path.exists(pj):
        d = json.load(open(pj, encoding="utf-8")); b = d["bitcheck"]; f = d["final"]
        xcheck += [
            {"item": "守恒核 E⁰=Φ+R+D+U", "left": b["E0"], "right": b["phi_R_D_U"], "equal": b["E0"] == b["phi_R_D_U"]},
            {"item": "E⁰行=D+U", "left": b["E0_rows"], "right": b["D_U"], "equal": b["E0_rows"] == b["D_U"]},
            {"item": "E⁰询=Φ+R", "left": b["E0_q"], "right": b["phi_R"], "equal": b["E0_q"] == b["phi_R"]},
            {"item": "D=Σ成因", "left": b["D"], "right": b["D_by_sum"], "equal": b["D"] == b["D_by_sum"]},
            {"item": "利用率 D/E⁰行", "left": round(f["D"] / f["E0_rows"], 4), "right": round(f["util_A"], 4),
             "equal": round(f["D"] / f["E0_rows"], 4) == round(f["util_A"], 4)},
        ]
    if os.path.exists(lj):
        v = json.load(open(lj, encoding="utf-8"))["vector"]
        for k in ("e0", "phi", "refl", "diss", "us"):
            xcheck.append({"item": "Lean 向量 " + k, "left": str(v["lean"][k]),
                           "right": str(v["python"][k]), "equal": v["lean"][k] == v["python"][k]})
    thresholds = [
        {"id": "PR-1", "name": "利用率（真机小参数账本·L1）", "band": "≥ 50%",
         "status": "预注册带·已冻结（PI 15:36:56 ①「冻结现三带」）", "ref": "L0 70.77%·修复后替身干跑 65.08%（均实测·非同轮）"},
        {"id": "PR-2", "name": "幻肢行回射率（迹／基准位·代价上限）", "band": "≤ 5%",
         "status": "预注册带·已冻结（PI 15:36:56 ①「冻结现三带」）", "ref": "冻结迹 2.45%"},
        {"id": "PR-3", "name": "编造占比（R-d）", "band": "上限候 PI 冻结（未定值）",
         "status": "待定·不得填数", "ref": "发射案 v3 §8.3 候裁 3"},
        {"id": "AN-1", "name": "利用率（冻结迹）", "band": "= 69.23%（105225/152000）逐位",
         "status": "实测锚·回归门", "ref": "thermo_demo --check 13/13"},
        {"id": "AN-2", "name": "期末在场行（冻结迹）", "band": "= 61/256", "status": "实测锚·回归门", "ref": "同上"},
        {"id": "AN-3", "name": "特定键命中率（冻结迹）", "band": "= 78/163；78+4=82", "status": "实测锚·回归门", "ref": "同上"},
        {"id": "AN-4", "name": "幻肢行回射率（冻结迹）", "band": "= 4/163 = 2.45%", "status": "实测锚·回归门", "ref": "同上"},
        {"id": "ST-1", "name": "守恒核", "band": "逐事件逐位成立·SELF-CONSISTENT·n_corrupt=0",
         "status": "结构判据·0 容差", "ref": "thermo_crosscheck 15/15"},
        {"id": "ST-2", "name": "原文泄漏 leak", "band": "= ∅", "status": "结构判据·A4", "ref": "crosscheck 幻肢不变量"},
        {"id": "ST-3", "name": "作答如实", "band": "ack=True ∧ fabricate=∅ ∧ leak=∅",
         "status": "结构判据", "ref": "真机轮·待测"},
        {"id": "ST-4", "name": "在场行（真机小参数账本）", "band": "期结算后 ≤12/12 且 < 注入行数；终核后 = 0",
         "status": "结构判据（终核行＝待测）", "ref": "发射案 v3 §4.1"},
        {"id": "ST-5", "name": "幻肢回射（真机）",
         "band": "每个已散失键 ≥1 行 ⟨幻肢⟩（上限 phantom_k=3/读）·R=c_P×行数 逐位",
         "status": "结构判据", "ref": "真机轮·待测"},
        {"id": "ST-6", "name": "基准位", "band": "M−E ≥ −3pp", "status": "预注册带·已冻结（PI 15:36:56 ①）／排程缓至 L2 出数后（PI ①）·待测",
         "ref": "在册判死线重跑"},
    ]
    data = {
        "version": "v5", "frozen_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "freezer": "查理-论文主笔（PI 15:36 裁决④ 合流后重冻 v5·管理员 16:03:29 派单；**v5 补冻①**＝⑪ 现行件改名同窗·管理员 16:46:40 派单·戴夫受影响行件 1 行）",
        "head": "8a43400", "branch": "private/v5preR2",  # 补冻①：冻结时仓位（生成器改动提交·41 项在其上逐位实测·冻结件落下一提交）
        "rule": "冻结后不再改动；任一指纹变动即视为冻结失效，须重新冻结并记明变动原因。"
                "本冻结 v5 取代 v4、v3、v2 与 v1：v1 指向已作废的并行树（paper/evidence/trees/）与发射案 v2；v2 指向发射案 v3 与 §8 `0127ca353bef`；v3 指向发射案 v5 与 §8 `9d616afc08ef`；v4 指向发射案 v5 包与 §8 `497a5aa3d61f`——一律作废留档。"
                "本轮为合流后重冻（PI 15:36:56 ④「合流后重冻 v5·方式＝merge·bundle 往返·0 推」）：41 项逐项重测，变动项见 stale_resolved 第五轮三条＋记忆树三活件；与 v4 逐行对拍报变更行。"
                "补冻①（同窗·⑪ 现行件改名后）：戴夫 16:37 原地改名 384 条（0 删 0 改内容）→41 行逐核仅 1 行路径变（总索引 _2026_11_22→20261122·sha12 恒等）→生成器改一处重跑；41 项 sha12 预期 0 变动；另顺手修正 launch 行 kind 字段错位（非指纹位）。",
        "lineage": {"v1": "已作废（并行树＋发射案 v2 冻结）",
                    "v2": "已作废留档（就既有树·发射案 v3·thermo-generation §8 `0127ca353bef`）",
                    "v3": "已作废留档（就既有树·发射案 v5·thermo-generation §8 `9d616afc08ef`·载体 xiaomi/mimo-v2.6-flash-mopd）",
                    "v4": "已作废留档（就既有树·发射案 v5 包·thermo-generation §8 `497a5aa3d61f`·只重冻 §8 一行·合流前终态）",
                    "v5": "现役（就既有树·发射案 v7 包·thermo-generation §8 `0f6f96f1e4de`·合流提交 b8cbbeb·载体 mimo-v2.6-flash〔teamorouter 径〕／xiaomi/mimo-v2.6-flash-mopd〔OpenRouter 径·停用〕）"},
        "memory_tree": {"n": len(mem), "bytes": sum(r["bytes"] for r in mem), "rows": mem,
                        "frozen_volumes": {"n": len(fchk), "all_equal": all(c["equal"] for c in fchk) if fchk else None,
                                           "rows": fchk}},
        "experiment_tree": {"n": len(exp), "bytes": sum(r["bytes"] for r in exp), "rows": exp,
                            "xcheck": {"n": len(xcheck), "all_equal": all(x["equal"] for x in xcheck) if xcheck else None,
                                       "rows": xcheck}},
        "rag": rag,
        "thresholds": thresholds,
        "stale_resolved": STALE,
        "facts_sync": FACTS,
        "pending_ruling": "〔已裁·留档〕本地 Qwen3-0.6B 轮入册位——PI 15:36:56 ②：追认爱丽丝自择「退化轮指针行」（不计预注册判据·不填槽·L1 仍 BLOCKED）；v4 时点原文「候 PI 裁；先不入册，稿内标为待裁。",
        "missing": missing,
        "elapsed_s": round(time.time() - t0, 2),
    }
    os.makedirs(OUT, exist_ok=True)
    json.dump(data, open(os.path.join(OUT, "FREEZE_v5preR2.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(OUT, "FREEZE_v5preR2.md"), "w", encoding="utf-8").write(render_md(data))
    print("FREEZE_v5preR2.json / FREEZE_v5preR2.md -> %s" % OUT)
    print("记忆 %d 件·实验 %d 件·两 RAG %d 件·阈值 %d 条·缺 %d·冻结 %s" % (
        len(mem), len(exp), len(rag), len(thresholds), len(missing), data["frozen_at"]))
    return 0 if not missing else 1


def render_md(d):
    L = ["# v5preR2 · 冻结清单（FREEZE v5·就既有树·合流后重冻）", "",
         "> **令源（v4·前轮·留档）**：群管理员 2026-11-25 **12:05:07「重冻 §8 一行（爱丽丝已按令追加 OpenSDK 重试与本地轮记录）：`docs/thermo-generation.md` 现役 497a5aa3d61f · 676 行 · 46046 字节（原 9d616afc08ef · 544 行 · 35934 B）。只重冻这一行，其余 40 项指纹不动；FREEZE v3→v4，重出比对 0 失配。论文与冻结清单同步两笔事实（读数诚实、不填估值）：① OpenSDK 四个官方 SDK、生成族 8 例仍全 400『Request path cannot be relayed』，拒中继在路径层，载体不变；② 本地 Qwen3-0.6B 轮（Apache-2.0·非预注册载体·不填槽）第三幕 0 次读工具，幻肢回射空集不可算。本地轮是否入册由 PI 定：先不入册，稿内标为待裁。私仓、0 推公开仓，不动已验代码。」**",
         "> **规则**：%s" % d["rule"],
         "> **冻结时刻**：%s　**仓位**：`%s`（分支 `%s`）" % (d["frozen_at"], d["head"], d["branch"]),
         "> **谱系**：v1 已作废（并行树＋发射案 v2）→ v2 已作废留档（发射案 v3·§8 `0127ca353bef`）→ v3 已作废留档（发射案 v5·§8 `9d616afc08ef`）→ v4 已作废留档（发射案 v5 包·§8 `497a5aa3d61f`·合流前终态）→ **v5 现役**（发射案 v7 包·§8 `0f6f96f1e4de`·合流提交 `b8cbbeb`·**载体 `mimo-v2.6-flash`〔teamorouter 径〕**）。",
         "> **令源（v5·本轮）**：PI 2026-11-25 **15:36:56 裁决④「合流后重冻 v5·方式＝merge（bundle 往返·0 推）」**＋群管理员 **16:03:29 派单「执行 ④ 合流后重冻 v5（已试合·0 冲突·可直接推）：1. bundle 校验后 `--no-ff` 合入 `private/v5preR2`；2. 重跑 `gen_freeze.py` 出 FREEZE v5，与 v4 逐行对拍，报变更行、指纹与 41 项覆盖；3. 0 推、0 动已验代码」**——本轮：bundle sha256 `bae132fd…478f` 校验 ✓·`7796c7e` 4 提交 11 文件 `--no-ff` 合入 `b8cbbeb`（0 冲突·0 推）；41 项逐项重测；与 v4 逐行对拍见交付件；PI ①② 同步入册（预注册带三带冻结·本地轮退化轮指针行追认）。",
         "", "## 冻结总览", "",
         "| 对象 | 件数 | 字节 | 核验 |", "|---|---|---|---|",
         "| 记忆帐树（**既有**·固定名件） | %d | %d | 冻结分册 %d/%d %s |" % (
             d["memory_tree"]["n"], d["memory_tree"]["bytes"],
             sum(1 for c in d["memory_tree"]["frozen_volumes"]["rows"] if c["equal"]),
             d["memory_tree"]["frozen_volumes"]["n"],
             "✓" if d["memory_tree"]["frozen_volumes"]["all_equal"] else "✗"),
         "| 实验帐树（**既有**·固定名件） | %d | %d | 逐位对表 %d/%d %s |" % (
             d["experiment_tree"]["n"], d["experiment_tree"]["bytes"],
             sum(1 for x in d["experiment_tree"]["xcheck"]["rows"] if x["equal"]),
             d["experiment_tree"]["xcheck"]["n"],
             "✓" if d["experiment_tree"]["xcheck"]["all_equal"] else "✗"),
         "| 两套 RAG（各自独立·不得合并） | %d | %d | 分立 |" % (len(d["rag"]), sum(r["bytes"] for r in d["rag"])),
         "| 预注册带阈值 | %d | — | 三带已冻结（PI 15:36:56 ①）·R-d 上限数值仍候 PI（现无数值可冻·维持不判） |" % len(d["thresholds"]),
         "", "## 零、待处置项（四轮·已处置）", "",
         "| 件 | 旧 | 新 | 处置 | 理由 |", "|---|---|---|---|---|"]
    for s in d["stale_resolved"]:
        L.append("| %s | %s `%s` | %s `%s` | %s | %s |" % (
            s["item"], s["old_version"], s["old_fp"] or "—", s["new_version"], s["new_fp"], s["action"], s["reason"]))
    L += ["", "**重冻规则（写清）**：",
          "1. **现役为准**：冻结以当前现役版本为准；旧版本指纹**作废并留档**（见上表「旧」列），不得两版并存。",
          "2. **重冻不豁免**：docs 类证据（如 thermo-generation.md §8）按令更新后，属证据更新而非豁免——"
          "重冻时旧时点读数留档备查、现役指纹入册；不设「豁免」档，避免冻结被绕过。",
          "3. **失效即重冻**：任一件指纹变动 ⇒ 冻结失效，须重跑 `gen_freeze.py` 重冻并在本件记明变动原因。",
          "4. **版本递增**：每次重冻 version 递增（v1→v2→…），旧版 JSON 留档不删。",
          "", "## 零之二、本轮同步入册的两笔事实（论文与冻结清单同源·读数诚实·不填估值）", "",
          "| 号 | 事实 | 读数（实测·非估值） | 读数是什么／不是什么 | 填槽 |",
          "|---|---|---|---|---|"]
    for f in d["facts_sync"]:
        L.append("| %s | **%s** | %s | %s | %d |" % (
            f["id"], f["item"], f["reading"], f["reading_is"], f["slots_filled"]))
    L += ["", "**入册位（v5 已裁·v4 待裁原文留档）**：%s" % d["pending_ruling"], "",
          "## 一、记忆帐树（**既有**·固定名件·12 件）", "",
          "> 本轮在原树上增了什么：现态快照面第 **183 轮**（P468 裁决落稿落帐窗；v4 时点 176/177 轮→v5 183 轮·期间 178–182 轮逐轮在册）；"
          "活跃分册续喂至 **P466**；冻结分册 8 件 0 改。", "",
          "| 树 | 件 | 类别 | sha12 | 行 | 字节 |", "|---|---|---|---|---|---|"]
    for r in d["memory_tree"]["rows"]:
        L.append("| %s | `%s` | %s | `%s` | %d | %d |" % (
            r["tree"], r["path"].split("/")[-1], r["kind"], r["sha12"], r["lines"], r["bytes"]))
    L += ["", "### 冻结分册恒定性（实测 vs 根索引记录）", "",
          "| 分册 | 根索引记录 | 本次实测 | 判定 |", "|---|---|---|---|"]
    for c in d["memory_tree"]["frozen_volumes"]["rows"]:
        L.append("| 分册%d | `%s` | `%s` | %s |" % (c["volume"], c["recorded"], c["measured"],
                                                     "✓ 恒等" if c["equal"] else "✗ 漂移"))
    L += ["", "## 二、实验帐树（**既有**·固定名件·%d 件）" % d["experiment_tree"]["n"], "",
          "> 本轮在原树上增了什么：实验册树 v3 增补 **N 组 N1–N10**（v5preR2 窗）＋ **N11–N15**（重做轮）；"
          "Python 事件树与 Lean 镜像树**降位为本树证据件**（Lean 镜像归实验侧机证）。", "",
          "| 树 | 件 | 类别 | sha12 | 行 | 字节 |", "|---|---|---|---|---|---|"]
    for r in d["experiment_tree"]["rows"]:
        L.append("| %s | `%s` | %s | `%s` | %d | %d |" % (
            r["tree"], r["path"].split("/")[-1], r["kind"], r["sha12"], r["lines"], r["bytes"]))
    L += ["", "### 逐位对表（两证据件 vs 实测）", "",
          "| 项 | 左 | 右 | 判定 |", "|---|---|---|---|"]
    for x in d["experiment_tree"]["xcheck"]["rows"]:
        L.append("| %s | %s | %s | %s |" % (x["item"], x["left"], x["right"], "✓" if x["equal"] else "✗"))
    L += ["", "## 三、两套 RAG（各自独立·不得合并）", "",
          "| RAG | 件 | sha12 | 行 | 字节 |", "|---|---|---|---|---|"]
    for r in d["rag"]:
        L.append("| %s | `%s` | `%s` | %d | %d |" % (r["rag"], r["path"], r["sha12"], r["lines"], r["bytes"]))
    L += ["", "**分立规则**：记忆 RAG 语料仅记忆帐树 12 件；实验 RAG 语料仅实验帐树 23 件——"
          "语料不交叉、索引分立、入口分立，不得合并成单索引。", "",
          "## 四、预注册带阈值（三带已冻结·PI 15:36:56 ①）", "",
          "| 编号 | 名称 | 阈值／判据 | 类型 | 参照 |", "|---|---|---|---|---|"]
    for t in d["thresholds"]:
        L.append("| %s | %s | %s | %s | %s |" % (t["id"], t["name"], t["band"], t["status"], t["ref"]))
    L += ["", "## 五、复现与核验", "", "```bash",
          "cd plugin_up_v1 && python3 paper/tools/gen_tree_python.py           # Python 事件树（证据件）重出",
          "cd plugin_up_v1 && python3 paper/tools/gen_tree_lean.py --log paper/evidence/lean_build_66b53fc.log   # Lean 镜像树（证据件）重出",
          "cd plugin_up_v1 && python3 paper/rag/memory/build_memory_rag.py          # 记忆 RAG 重建",
          "cd plugin_up_v1 && python3 paper/rag/experiment/build_experiment_rag.py  # 实验 RAG 重建",
          "cd plugin_up_v1 && python3 paper/tools/gen_freeze.py             # 冻结清单重出（重冻）",
          "cd plugin_up_v1 && python3 paper/tools/compare_freeze.py <旧版 FREEZE_v5preR2.json>   # 两版逐位比对·报 0 失配",
          "```", "",
          "**冻结效力**：任一件指纹变动 ⇒ 冻结失效，须重新冻结并记明变动原因；冻结后本轮产物 0 改动。", ""]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    import re
    sys.exit(main())
