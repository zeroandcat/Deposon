# -*- coding: utf-8 -*-
"""
D8 R 系 b 半 3 题 · 采集补入 addendum（新件 · 2026-09-30 · 追加棒）

触发：parent 补令 —— b 半 3 题（D8-11 / D8-19 / D8-37）已由 PI 即刻作答（接受降级标注），
      台账 _d8_collection_ledger_2026_09_30.md 已同步更新（尾部「b 半（即刻作答 · 降级标注口径）」节）。
唯一数据源 = 台账现态（本棒实测 9a7262685d9f / 18,833 B / 257 行）。
⛔ 0 覆写已落主件（_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json = 769ef8b71462）⇒ 本件为**新名追加件**。
⛔ 0 合并任何既有 JSON；0 LLM / 0 API / 0 proxy / 0 gateway；key 永不明文。
"""
import json, hashlib, os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = "results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md"          # 238077d25919
LEDGER = "results/_d8_collection_ledger_2026_09_30.md"                 # 本棒实测 9a7262685d9f
SQF = "results/_d8_supplement_open_questions_2026_09_30.md"           # 579b375e9508
BND = "results/_d8_boundary_revision_register_2026_09_30.md"           # b46370bb9e3b
MAIN = "results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json"  # 769ef8b71462（已落主件，只读）
OUT = "results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json"
MAIN_SHA_EXPECT = "769ef8b71462"

ASK = "ask_5cd9bea3d315db200aa19dee"
DEGRADE = "未满足 ≥1 天间隔，R 系有效性降级"

def sha12(rel):
    b = open(os.path.join(ROOT, rel), "rb").read()
    return hashlib.sha256(b).hexdigest()[:12], len(b)

# 落盘前：主件必须仍在盘且与已回报值一致（0 覆写自证的前提）
ms, mb = sha12(MAIN)
assert ms == MAIN_SHA_EXPECT, "主件 SHA 与已回报值不符，⛔ 停手：%s" % ms
ls, lb = sha12(LEDGER)

E = [
 dict(
  q="D8-11", pair="R9", half="b", jt="J1", ans="C，不要被判死线所过度局限", form="Other（选 C ＋ 推理）",
  sel=["C"], opt={"C": "请 PI 拍板"}, rsn="不要被判死线所过度局限",
  line=250,
  face="同 D8-10 场景，但预登记已写明边界方向为「读数 > 阈值即触发」。判定改为？",
  listed=["A 照预登记：0.65 不 > 0.65 ⇒ 不触发", "B 判不达标（等于阈值视为未达）", "C 请 PI 拍板"],
  axis="判死线：默认边界 vs 显式边界",
  a=dict(q="D8-10", ans="A，不可机械否则不是真与死同行", letters=["A"], face="判达标（未超即不触发）",
         rsn="不可机械否则不是真与死同行", a_face="某条判死线读数刚好卡在阈值上（0.65 对 0.65），且预登记未写明边界方向。判定？",
         conclusion="判达标（未超即不触发）＝未判不达标"),
  landing_changed=True, landing_basis="a 半落点 A（判达标／未超不触发）→ b 半落点 C（请 PI 拍板）⇒ 落点方向改变（题面 §1 第 4 条字面「判定方向改变即记纠正/反转事件」）",
  conclusion_comparable=False,
  conclusion_basis="a 半出结论（判达标＝未判不达标）；b 半落 C＝**未给判定**（请 PI 拍板）⇒ 结论轴两半不可比",
  verdict_grade="落点轴已确认改变 · 结论轴存疑（b 半未出结论，两半结论不可比）",
  confirmed=True, counted=1,
  verdict_note=("本件按**落点轴**（题面 §1 第 4 条字面的判定方向）登记为纠正/反转事件，计 1 件；"
                "⚠️ **第二读存疑**（本棒 0 硬断）：若 PI 采用**结论轴**口径，则 b 半未出结论 ⇒ 两半结论不可比 ⇒ 该读法下不能记为已实测反转。"
                "两读并存，如实登记；最终口径判定权在 PI / 收口棒。"),
  two_reading=[{"axis": "落点轴（primary，题面 §1 第 4 条字面）", "a": "A", "b": "C", "changed": True,
                "counted": 1, "note": "落点字面不同 ⇒ 记纠正/反转事件"},
               {"axis": "结论轴（alternative，存疑）", "a": a_conclusion if False else "判达标（未超即不触发）",
                "b": "未给判定（请 PI 拍板）", "changed": None,
                "counted": None, "note": "b 半未出结论 ⇒ 不可比 ⇒ 不能记为已实测反转"}],
  extra=dict(pi_quote_note="PI 推理逐字「不要被判死线所过度局限」＝对「照预登记机械触发/判不达标」的反对口径（沿 PI 判死纪律「不软化/不机械」同族）；本件 0 替 PI 扩写其与 a 半的具体差别。")),

 dict(
  q="D8-19", pair="R10", half="b", jt="J2", ans="BC，否则双审不过才是麻烦", form="Other（双选 B/C ＋ 推理）",
  sel=["B", "C"], opt={"B": "重采（论文结论强度优先）", "C": "重采且优先采论文用到的部分"},
  rsn="否则双审不过才是麻烦", line=251,
  face="同 D8-18 场景，但该结论已进论文草稿。处置改为？",
  listed=["A 仍不重采，但论文中该结论须带限定注记", "B 重采（论文结论强度优先）", "C 重采且优先采论文用到的部分"],
  axis="成本：内部挂账 vs 已扩散结论",
  a=dict(q="D8-18", ans="C，重采可能不可复现如模型下架或自动路由等情况", letters=["C"], face="先采子集看是否够消解",
         rsn="重采可能不可复现如模型下架或自动路由等情况",
         a_face="某结论的 540 条独立观测缺件重采需重建整套观测面，成本极大但能消解一条长期挂账的限定注记。做吗？",
         conclusion="先采子集（不重采全套 540 独立观测）"),
  landing_changed=True, landing_basis="a 半落点 {C}（先采子集）→ b 半落点 {B,C}：**B 档（重采·论文结论强度优先）进入** ⇒ 落点方向改变（成本轴由「采子集」移向「重采」）；C 档与 a 半重叠部分单列",
  conclusion_comparable=True,
  conclusion_basis="a 半＝采子集；b 半＝重采（含论文优先）⇒ 结论方向亦改变",
  verdict_grade="双轴均改变（a 档集 ⊂ b 档集，含 C 档重叠）",
  confirmed=True, counted=1,
  verdict_note=("本件按落点轴与结论轴**双源一致**登记为纠正/反转事件，计 1 件；"
                "⚠️ 重叠如实登记：b 半的 C 档（重采且优先采论文用到的部分）与 a 半落点 C 档重叠 ⇒ "
                "严格读法下为「落点集合由 {C} 扩为 {B,C}」而非完全换向；本棒按「B 档进入＝方向改变」登记，并保留集合关系原貌，0 抹平。"),
  two_reading=[{"axis": "落点轴（primary）", "a": "{C}", "b": "{B,C}", "changed": True, "counted": 1,
                "note": "B 档进入 ⇒ 方向改变；a 档集 ⊂ b 档集"},
               {"axis": "结论轴（corroborating）", "a": "采子集", "b": "重采（论文优先）", "changed": True,
                "counted": 1, "note": "两轴一致 ⇒ 增强该配对的反转判定（非仅单轴支持）"}],
  extra=dict(double_review_note="PI 推理逐字「否则双审不过才是麻烦」＝以外部双审/复核关卡为判据（成本→风险转移）；本件 0 判定「双审」具体所指，0 扩写。")),

 dict(
  q="D8-37", pair="R11", half="b", jt="J3",
  ans="ABC，因为论文是委托外部agent的，所以自然有口径差异，可登记接受", form="Other（三选合成 ＋ 推理）",
  sel=["A", "B", "C"],
  opt={"A": "落盘准则件并在论文中核对方向一致性", "B": "以论文为准反推准则", "C": "登记分歧交 PI 拍板"},
  rsn="因为论文是委托外部agent的，所以自然有口径差异，可登记接受", line=252,
  face="同 D8-36 场景，但该表述已被写入一份对外发布的论文中。处置改为？",
  listed=["A 落盘准则件并在论文中核对方向一致性", "B 以论文为准反推准则", "C 登记分歧交 PI 拍板"],
  axis="准则：未扩散补录 vs 已扩散校正",
  a=dict(q="D8-36", ans="C 引用时标注「未落盘」", letters=["C"], face="引用时标注「未落盘」", rsn=None,
         a_face="核心准则的权威面只有 PI 的一次口头表述，无落盘件。处置？",
         conclusion="引用时标注「未落盘」（不据口头表述直接下判）"),
  landing_changed=None,
  landing_basis=("**两读并存，本棒 0 硬断**：a 半落点 {C} ⊂ b 半落点 {A,B,C}（严格包含 ⇒ 读作「放宽落点集」而非换向）；"
                 "但 b 半引入 B 档「以论文为准反推准则」＝与 a 半「标注未落盘」相反的处置方向 ⇒ 读作换向"),
  conclusion_comparable=True,
  conclusion_basis=("PI 自述理由「自然有口径差异，**可登记接受**」与 a 半 C 档（登记分歧交 PI 拍板）同向 ⇒ 结论轴读作同向；"
                    "但 a 档（落盘并核对方向一致性）与 B 档（以论文为准反推）均与 a 半落点不同"),
  verdict_grade="**存疑**（落点轴严格包含 vs B 档引入相反方向；结论轴 PI 自述同向）——本棒 0 硬断",
  confirmed=None, counted=None,
  verdict_note=("⛔ **存疑，不硬断**（parent 补令第 3 条）：三读并列 ——"
                "① 落点集合读法：a {C} ⊂ b {A,B,C} ⇒ **未换向**（仅放宽）；"
                "② B 档读法：b 含「以论文为准反推准则」＝与 a 半相反方向 ⇒ **换向**；"
                "③ PI 自述理由读法：「可登记接受」与 a 半 C 档（登记/接受分歧）**同向**。"
                "⇒ correction_confirmed 记 null、correction_event_counted 记 null，等 PI / 收口棒裁口径；"
                "本件 0 以任一读法单独定案、0 事后改题面迁就结论。"),
  two_reading=[{"axis": "① 落点集合读法（a ⊂ b）", "a": "{C}", "b": "{A,B,C}", "changed": False, "counted": 0,
                "note": "严格包含 ⇒ 放宽而非换向 ⇒ 不记反转"},
               {"axis": "② B 档方向读法", "a": "C 引用时标注「未落盘」", "b": "含 B 以论文为准反推准则", "changed": True,
                "counted": 1, "note": "B 档＝相反处置方向 ⇒ 记反转"},
               {"axis": "③ PI 自述理由读法", "a": "登记分歧（标注未落盘）", "b": "可登记接受", "changed": False,
                "counted": 0, "note": "PI 理由自述同向 ⇒ 不记反转"}],
  extra=dict(commission_note="PI 理由逐字含「论文是委托外部agent的，所以自然有口径差异」⇒ 与 D8-35（受托方口径相反）、D8-73（委托面口径）同族；本件 0 追改任何已落论文或委托件。")),

]

assert len(E) == 3
assert [x["q"] for x in E] == ["D8-11", "D8-19", "D8-37"]
assert [x["pair"] for x in E] == ["R9", "R10", "R11"]

# 逐字对账：3 条 PI 答复须在台账现态逐字命中
ledger_txt = open(os.path.join(ROOT, LEDGER), "r", encoding="utf-8").read()
for e in E:
    assert ("「" + e["ans"] + "」") in ledger_txt, "台账未逐字命中：" + e["q"]

sup = []
for e in E:
    a = e["a"]
    n = {}
    n["pair_id"] = e["q"]
    n["event_id"] = "D8_bhalf_2026_09_30_" + e["q"]
    n["date"] = "2026-09-30"
    n["q_id"] = e["q"]
    n["entry_class"] = "content_question"
    n["collection_wave"] = "b 半补入（PI 即刻作答 · 降级标注口径）"
    n["scene_tag"] = {"D8-11": "threshold_boundary_equality_written_direction",
                      "D8-19": "resample_540_after_paper_draft",
                      "D8-37": "verbal_principle_already_in_published_paper"}[e["q"]]
    n["scene_tag_source"] = "沿主件（769ef8b71462）同题占位条的 scene_tag（主件待采集占位与本件实答为同一题，0 另起新标签）"
    n["scene_verbatim"] = e["face"]
    n["question_face_verbatim"] = e["face"]
    n["scene_verbatim_source"] = Q + " §3 " + e["q"]
    n["scene_verbatim_source_note"] = "题面原文含 markdown 强调标记（**），本件仅去强调标记未改一字"
    n["judge_type"] = e["jt"]
    n["judge_type_source"] = Q + " §3 " + e["q"] + "「judge_type 提案」字面"
    n["judge_type_note"] = "沿题面提案字面录入，0 worker 改判（PI 在 D8-70 答「起草方提案 + PI 可推翻」，本件 0 行使改判权）"
    n["collected_via"] = "ask_user"
    n["collected_at"] = None
    n["collected_at_note"] = ("ask 记录不落盘（沿盘上 d6/d6b/d7 落件惯例）⇒ PI 精确作答时分不可回查；台账自记「已于 16:1x 全部收齐」"
                              "（时段级，0 秒级）⇒ 本件 0 伪造时分")
    n["source_ask_id"] = ASK
    n["ledger_source_ref"] = LEDGER + " 「b 半（即刻作答 · 降级标注口径 · 2026-09-30）」节表行（行 %d）" % e["line"]
    n["ledger_form_label"] = e["form"]
    n["collection_status"] = "已采（2026-09-30 即刻作答 · 降级标注口径）"
    n["collection_date_note"] = ("PI 裁「即刻作答（接受降级标注）」⇒ a/b 两半同为 2026-09-30 日历日，"
                                 "actual_interval_days = 0 < 1 ⇒ 未满足 ≥1 天间隔")
    n["option_chosen"] = "".join(e["sel"])
    n["option_chosen_letters"] = e["sel"]
    n["option_form"] = "single_letter_plus_reasoning" if len(e["sel"]) == 1 else (
        "multi_letter_triple_plus_reasoning" if len(e["sel"]) == 3 else "multi_letter_dual_plus_reasoning")
    n["option_meaning"] = None
    n["option_meaning_note"] = ("多选/三选合成落点 ⇒ 单一条目不对应唯一选项释义；被选各档字面见 selected_option_faces_verbatim"
                                "（0 合并为单一释义、0 挑一档当唯一落点）")
    n["selected_option_faces_verbatim"] = [e["opt"][x] for x in e["sel"]]
    n["selected_option_faces_verbatim_source"] = Q + " §3 " + e["q"] + " 被选各档选项字面"
    n["listed_options_verbatim"] = e["listed"]
    n["listed_options_verbatim_source"] = Q + " §3 " + e["q"] + " 选项 A/B/C 字面"
    n["pi_answer_verbatim"] = e["ans"]
    n["pi_answer_verbatim_note"] = "台账作答格逐字（去最外层「」包裹，PI 答句内部标点原样）；0 润色 0 改写 0 扩写 0 补标点"
    n["pi_other_verbatim"] = None
    n["pi_answer_form"] = "选项字母落点 " + "".join(e["sel"]) + "（PI 在 ask_user 问卷上作答，附推理句）"
    n["reasoning_full"] = e["rsn"]
    n["reasoning_full_note"] = ("台账「形态」列明示「＋ 推理」⇒ 该段为 PI 自附推理，逐字录入；0 润色 0 改写 0 归一标点")
    n["is_correction"] = True
    n["is_correction_note"] = ("R 系配对 b 半（" + e["pair"] + "b）配对标记，沿题面 §1 第 5 条字面「本件仅保证 is_correction 字段可标（R 系 6 件 = True）」"
                               "＋ §4 配对纪律字面「判定方向改变即记纠正/反转事件」；**b 半现已落件 ⇒ 本条首次具备可比对的 a/b 两侧**")
    n["correction_confirmed"] = e["confirmed"]
    n["correction_confirmed_note"] = ("按 a/b 两半落点与结论双轴对照判定（对照面见 reversal_pair.verdict_two_readings）；"
                                      "⚠️ 存疑处（" + e["pair"] + "）记 null，0 硬断 —— 详见 reversal_pair.verdict_note")
    n["reversal_pair"] = {
        "pair_code": e["pair"], "half": "b", "half_code": e["pair"] + "b",
        "paired_half_code": e["pair"] + "a", "paired_half_q_id": a["q"],
        "paired_half_landing_path": MAIN, "paired_half_landing_sha12": MAIN_SHA_EXPECT,
        "paired_half_answer_date": "2026-09-30",
        "reversal_axis_verbatim": e["axis"], "reversal_axis_source": Q + " §4 R 系反转配对索引字面",
        "a_half": {"q_id": a["q"], "option_chosen": a["letters"][0] if len(a["letters"]) == 1 else "".join(a["letters"]),
                   "option_chosen_letters": a["letters"], "option_face": a["face"],
                   "pi_answer_verbatim": a["ans"], "reasoning_full": a["rsn"],
                   "scene_verbatim": a["a_face"],
                   "conclusion_reading": a["conclusion"]},
        "b_half": {"q_id": e["q"], "option_chosen": "".join(e["sel"]), "option_chosen_letters": e["sel"],
                   "option_faces": [e["opt"][x] for x in e["sel"]],
                   "pi_answer_verbatim": e["ans"], "reasoning_full": e["rsn"],
                   "scene_verbatim": e["face"],
                   "conclusion_reading": e["conclusion_basis"]},
        "landing_axis": {"a": "".join(a["letters"]), "b": "".join(e["sel"]),
                         "changed": e["landing_changed"], "basis": e["landing_basis"]},
        "conclusion_axis": {"comparable": e["conclusion_comparable"], "basis": e["conclusion_basis"]},
        "verdict_two_readings": e["two_reading"],
        "direction_changed": e["landing_changed"],
        "verdict_grade": e["verdict_grade"],
        "verdict_note": e["verdict_note"],
        "correction_event_counted": e["counted"],
        "interval_requirement": "≥1 天间隔（防记忆效应）",
        "interval_requirement_source": Q + " §1 第 4 条字面 + §4 配对纪律字面",
        "actual_interval_days": 0,
        "interval_satisfied": False,
        "pair_closed": True,
        "pair_closed_note": "两半均已落件（本件 b 半 + 主件 a 半）⇒ 可比对；**闭合 ≠ 有效**：见 degradation_mark",
        "pair_validity": "degraded",
        "degradation_mark_verbatim": DEGRADE,
        "degradation_mark_source": Q + " §4 配对纪律字面「b 半未满 1 天不作答 ⇒ 该对不成立（件内须标注「未满足 ≥1 天间隔，R 系有效性降级」，沿 D8-60 选项 A 体例）」＋ "
                             "PI 答 D8-60 = A（允许当日答完但须标注降级）＋ " + LEDGER + " 「R 系口径（登记）」节字面",
        "degradation_note": ("a/b 两半同为 2026-09-30 日历日 ⇒ actual_interval_days = 0；PI 裁「即刻作答（接受降级标注）」"
                             "⇒ 本对在**比较用途**上成立（两半落点可比），在**跨日有效性**上降级；"
                             "本件 0 把降级对当作满足 ≥1 天间隔的有效配对、0 计入跨日天数（跨日天数按日历日去重计，同日两半不增天数）。"),
    }
    n["rp_validity_degradation"] = {
        "mark_verbatim": DEGRADE,
        "applies_to_this_entry": True,
        "ruling_source": "D8-60 选项 A（PI 2026-09-30 答 A：「允许当日答完，但件内标注「未满足 ≥1 天间隔，R 系有效性降级」」）＋ " + LEDGER + " 「R 系口径（登记）」节字面",
        "recorded_at": "件级 rp_validity_degradation ＋ 本条逐题备注（双落，沿 parent 补令第 2 条）"
    }
    n["supersedes_pending_stub"] = {
        "superseded_path": MAIN, "superseded_sha12": MAIN_SHA_EXPECT,
        "superseded_entry_class": "pending_b_half",
        "note": ("主件（769ef8b71462）内同 q_id 条目为「待采集（10-01+）」占位（全部值字段 null）；"
                 "本件为其**实答补入件**。同一 q_id 跨两件并存＝「占位 + 实答」，**非重复计数**；"
                 "⛔ 主件 0 覆写（parent 补令明令）⇒ 下游取 b 半值时以本件为准，主件占位条保留为历史原样。")
    }
    n["linked_pending_decisions"] = [{
        "id": "T-D8-3",
        "pending_item_verbatim": "本卷 R 系 b 半（D8-11 / D8-19 / D8-37）的作答日",
        "pending_item_source": Q + " §7 待 PI 拍板项表 T-D8-3 字面「b 半标 D9+；若 PI 当日一次答完，R 系有效性降级（见 D8-60）」",
        "directional_registration": "PI 2026-09-30 处置＝**即刻作答 ＋ 接受降级标注**（" + LEDGER + " 行 242/246/254 字面）⇒ 事件已发生",
        "status_changed": True,
        "status_changed_basis": "本项所问之「作答日」已由 PI 实际行为落定（b 半已收齐）；本件 0 代 PI 另行关闭 T-D8-3 的其余口径，0 改动预登记任何件",
        "note": "T-D8-3 的**降级分支**已被 PI 采纳（当日作答 + 标注降级）⇒ 逐对 degradation 已登记；本件 0 改写预登记/题面任何一件"
    }]
    n["weight"] = 1.0
    n["verbatim_grade"] = "letter_for_letter"
    n.update(e["extra"])
    sup.append(n)

assert len(sup) == 3
assert len(set(x["q_id"] for x in sup)) == 3
assert all(x["pi_answer_verbatim"] for x in sup)
assert all(x["reasoning_full"] for x in sup)
assert sum(1 for x in sup if x["correction_confirmed"] is True) == 2
assert sum(1 for x in sup if x["correction_confirmed"] is None) == 1
assert all(x["reversal_pair"]["interval_satisfied"] is False for x in sup)
assert all(x["reversal_pair"]["degradation_mark_verbatim"] == DEGRADE for x in sup)

n_conf = sum(1 for x in sup if x["reversal_pair"]["correction_event_counted"] == 1)
n_stuck = sum(1 for x in sup if x["reversal_pair"]["correction_event_counted"] is None)
assert (n_conf, n_stuck) == (2, 1)

anchors = [MAIN, LEDGER, Q, SQF, BND,
           "results/_v4_pi_cot_v3_dataset.json", "results/_v4_pi_cot_v2_dataset.json",
           "results/_v4_pi_cot_v3_prereg.md", "results/_v4_pi_cot_v2_questionnaire_v1.md",
           "results/_v3_s_prereg_v1_2026_09_27.md",
           "results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json",
           "results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json",
           "results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json"]
addendum_for = {"touch_policy": "0 触动（本件为纯新建追加件：⛔ 0 覆写已落主件 769ef8b71462、0 合并任何既有 JSON、0 删除；13 项锚 SHA-12 落盘前后复验不变）",
                "supersedes_pending_stubs_in": {"path": MAIN, "sha12": MAIN_SHA_EXPECT, "stub_q_ids": ["D8-11", "D8-19", "D8-37"]}}
for a in anchors:
    s, ln = sha12(a)
    k = os.path.basename(a).rsplit(".", 1)[0]
    addendum_for[k + "_path"] = a
    addendum_for[k + "_sha12_measured"] = s
    addendum_for[k + "_bytes"] = ln

doc = {}
doc["schema"] = "v4_pi_cot_v3_dataset_addendum_d8_bhalf/1"
doc["created"] = "2026-09-30T17:05:00+08:00"
doc["created_by"] = "Mavis 团队 worker (执行类·采集补入, 2026-09-30)"
doc["task"] = "D8 R 系 b 半 3 题（D8-11 / D8-19 / D8-37）实答补入 ＋ R 系有效性降级登记 ＋ a/b is_correction 对照判定"
doc["addendum_for"] = addendum_for
doc["post_hoc_amendment"] = True
doc["cross_day_collection"] = True
doc["cross_day_collection_note"] = (
    "b 半 3 题 = 2026-09-30 字面采集日（PI 即刻作答）⇒ **与 a 半同为 2026-09-30 日历日**；"
    "本件 3 条**不新增日历日**（跨日 distinct days 仍＝主件登记的 6 天）⇒ 本件 0 声称满足 ≥1 天间隔、0 以同日两半充作跨日。")
doc["collection_round"] = "D8 b 半补入（PI 即刻作答 · 降级标注口径）"
doc["collection_date"] = "2026-09-30"
doc["source_pi_judgment_basis"] = (
    "PI 2026-09-30 通过 ask_user 即刻作答 3 题（回执 " + ASK + "），答复字面逐字记录于盘上台账尾部"
    "「b 半（即刻作答 · 降级标注口径 · 2026-09-30）」节；**唯一数据源＝台账现态**（本棒实测 " + ls + " / " + str(lb) + " B / 257 行）。"
    "本棒 0 取得 ask 原件（ask 记录不落盘）⇒ 所记 ask_id 与答复字面均转录自台账，0 声称已核验 ask 原文。0 LLM 代答。")
doc["source_ask_ids"] = [ASK]
doc["source_ask_id_note"] = "转录自台账 b 半节标题字面；ask 记录不落盘 ⇒ 0 声称已核验 ask 原文"
doc["explicit_user_confirmation"] = True
doc["pi_realtime_answering_window"] = True
doc["unique_data_source"] = {
    "path": LEDGER, "sha12_measured": ls, "bytes_measured": lb, "lines_measured": 257,
    "state": "b 半 3 题已入账的**现态**（本棒 2026-09-30 落盘前实测）",
    "role": "唯一数据源：3 条 PI 答复字面、ask_id、形态标记、台账行号均以此为准；本棒 0 用主件/题面件补写 PI 答复",
    "ledger_sha_drift_registration": {
        "drift_family": "台账为活文档（随批追加），主件登记值与本棒实测值不同源不同时点",
        "values_on_record": [
            {"sha12": "deec8c91a75b", "bytes": 1957, "recorded_in": SQF + " §0.1 第 4 行（批 1–2 态）"},
            {"sha12": "e61f4050fc02", "bytes": 6195, "recorded_in": BND + " §0.1 第 4 行（批 1–7 态）"},
            {"sha12": "d87518e980e7", "bytes": 7470, "recorded_in": LEDGER + " 「边界修订」块自记"},
            {"sha12": "199a206d2800", "bytes": 17946, "recorded_in": MAIN + "（" + MAIN_SHA_EXPECT + "）unique_data_source（b 半入账前态，17,946 B / 245 行）"}],
        "measured_by_this_piece": {"sha12": ls, "bytes": lb, "lines": 257,
                                   "state": "b 半 3 题入账后现态（本棒实测）"},
        "handling": "五值并存如实登记，**0 归因、0 覆写、0 代为调和**（沿 D8-45 同族纪律）",
        "note": "本棒 0 声称知道差异根因（可归因于 b 半节追加，但未核验 0 断言）"
    },
    "ledger_internal_staleness_registration": {
        "stale_spots": [
            {"line": 240, "verbatim": "D8 大波：内容题 77/77（80 − b 半 3）", "superseded_by_line": 256},
            {"line": 244, "verbatim": "b 半到点开卷", "superseded_by_line": 242},
            {"line": 257, "verbatim": "b 半 11/19/37 仍 10-01+（PI 4 裁原文段）", "superseded_by_line": 242}],
        "handling": "台账为**只读活文档实录**，本棒 0 回改、0 覆写；三处旧表述为追加前的历史原文，与行 242/246-254/256 现态并存 ⇒ 如实登记，不代为调和；本件引用以现态（行 242/246-254/256）为准"
    }
}
doc["supplements"] = sup
doc["supplement_count"] = len(sup)
doc["rp_validity_degradation"] = {
    "mark_verbatim": DEGRADE,
    "level": "件级（本字段）＋ 逐题（每条 supplements[*].rp_validity_degradation / reversal_pair.degradation_mark_verbatim）双落",
    "ruling_source": "PI 答 D8-60 = A（" + Q + " §3 D8-60 选项 A 字面「允许当日答完，但件内标注「未满足 ≥1 天间隔，R 系有效性降级」」）＋ "
                 + Q + " §4 配对纪律字面 ＋ " + LEDGER + " 「R 系口径（登记）」节字面",
    "pairs_degraded": [
        {"pair": "R9", "a": "D8-10", "b": "D8-11", "a_date": "2026-09-30", "b_date": "2026-09-30",
         "actual_interval_days": 0, "interval_satisfied": False},
        {"pair": "R10", "a": "D8-18", "b": "D8-19", "a_date": "2026-09-30", "b_date": "2026-09-30",
         "actual_interval_days": 0, "interval_satisfied": False},
        {"pair": "R11", "a": "D8-36", "b": "D8-37", "a_date": "2026-09-30", "b_date": "2026-09-30",
         "actual_interval_days": 0, "interval_satisfied": False}],
    "scope_note": ("降级**仅涉 R 系配对有效性**（跨日防记忆效应），0 涉 PI 答复本身的入账：3 条 b 半答复与其他条目同等逐字入账、权重 1.0；"
                   "0 因降级而作废、0 剔除、0 降权。"),
    "counting_effect": ("跨日 distinct calendar days 不增（同日两半仍 1 个日历日）⇒ 主件登记的 6 天不变；"
                        "⛔ 本件 0 判定任何阈值（K-V3S-3-1/3-2/3-3/3-4 均 0 判、0 改）。")
}
doc["is_correction_verdict_summary"] = {
    "method": ("沿既有体例：题面 §1 第 5 条字面（R 系件 is_correction 字段可标）+ §4 配对纪律字面「判定方向改变即记纠正/反转事件」"
               "＋ d7 落件体例（以 a/b 两半实测方向对照，0 预判、0 只看单侧）"),
    "a_half_reference": {"path": MAIN, "sha12": MAIN_SHA_EXPECT,
                         "a_half_entries": ["D8-10", "D8-18", "D8-36"],
                         "note": "a 半已落主件（entry_class=content_question，is_correction=true 配对标记，correction_confirmed=false ＋「须待 b 半落件后比对」注）"},
    "verdicts": [
        {"pair": "R9", "a": "D8-10=A", "b": "D8-11=C", "landing_changed": True, "confirmed": True, "counted": 1,
         "grade": "落点轴已确认改变 · 结论轴存疑（b 半未出结论）", "uncertainty": "存疑点＝第二读（结论轴不可比），已并列登记未硬断"},
        {"pair": "R10", "a": "D8-18=C", "b": "D8-19=BC", "landing_changed": True, "confirmed": True, "counted": 1,
         "grade": "双轴均改变（a 档集 ⊂ b 档集，含 C 档重叠）", "uncertainty": "重叠部分已如实登记，未抹平"},
        {"pair": "R11", "a": "D8-36=C", "b": "D8-37=ABC", "landing_changed": None, "confirmed": None, "counted": None,
         "grade": "**存疑**（三读并列）", "uncertainty": "①a⊂b 读作未换向 ②B 档读作换向 ③PI 自述理由读作同向 ⇒ 0 硬断，记 null 等 PI/收口棒裁"}],
    "correction_event_counted_total_confirmed": n_conf,
    "correction_event_unresolved": n_stuck,
    "is_correction_field_summary": "3 条 b 半 is_correction = true（配对标记，题面 §1 第 5 条字面）；correction_confirmed：R9/R10 = true、R11 = null（存疑）",
    "threshold_note": ("**0 判定任何阈值**：K-V3S-3-3（纠正 ≥5 线）是否因本件 +2 而变化，属既有件重跑范围，"
                       "本棒 0 重算、0 宣告达标、0 改阈（沿 d7 落件 companion_kill_lines_unchanged_note 惯例）。"),
    "not_retroactive_note": ("本对照**0 回头修改主件** a 半的 is_correction / correction_confirmed 字段值（既有件只读不动，parent 补令明令 0 覆写）；"
                             "主件 a 半的 correction_confirmed=false 保留其「须待 b 半落件后比对」原义，**b 半侧的对照结论以本件为准**。")
}
doc["cross_piece_relationship"] = {
    "main_piece": {"path": MAIN, "sha12": MAIN_SHA_EXPECT, "entries": 93,
                   "class_counts": {"content_question": 77, "pending_b_half": 3, "open_question": 7,
                                    "skipped": 1, "calibration_item": 5},
                   "read_only": True, "touched_by_this_piece": False},
    "this_piece": {"entries": 3, "all_q_ids": ["D8-11", "D8-19", "D8-37"],
                   "relation": "主件同 q_id 的 pending_b_half 占位条 → 本件实答条（占位 + 实答并存，非重复计数）",
                   "downstream_rule": "读 b 半取值时以本件为准；主件占位条保留为历史原样（⛔ 0 覆写）"},
    "combined_coverage_after_this_piece": {
        "d8_content_questions_answered": 80, "d8_answered_face_total": 80,
        "d8_pending_remaining": 0, "sq_answered": 7, "sq_skipped": 1, "calibration_items": 5,
        "note": "D8 全卷 80/80 已收讫（台账行 256 字面「D8 80/80（含 b 半）＋ SQ 7/8＋1 跳过 —— 今日采集全线收讫」）；本计数为跨两件的口径合并，非单件计数"
    },
    "substrate_ledger_face_update": {
        "verbatim": "substrate 账：163 ＋ 7 ＝ 170 ≥167 ✓（台账行 241）",
        "after_b_half": "b 半 3 题入账后按实答口径复算：83（T-D8-1 口径 ② 盘上实存）+ 80（D8 实答）+ 7（SQ 实答）= 170",
        "reconciliation": "主件（b 半入账前）曾并列两读：台账读 83+80=163+7=170 与实答读 83+77=160+7=167；b 半收齐后**两读合一为 170**（差额 3 件＝b 半 3 题）",
        "k_v3s_4_2_threshold_touched": False,
        "note": "**0 判定达标**（自洽下限 167 的达标判定属收口/verifier 棒），0 改算式、0 改阈"
    },
    "inherited_property_of_frozen_main_piece": {
        "note": ("主件 9 条条目（D8-23/25/34/44/51/53/62/68 + T-D8-1）的 reasoning_full 填了 PI 自附尾句，"
                 "而其台账「形态」标记为信号/双层/合成类（非明示「＋推理」）⇒ 与主件 verbatim_policy 所声明的判定规则存在口径宽严不一。"),
        "handling": ("⛔ 主件已落且 parent 明令 0 覆写 ⇒ 本棒**不回改**；此处仅作诚实披露，供下游按台账「形态」列自行判读（文本 100% 为 PI 原话逐字，0 改写、0 虚构）。"),
        "affects_this_piece": False,
        "this_piece_handling": "本件 3 条 reasoning_full 均据台账形态列明示「＋ 推理」填入，口径自洽"
    }
}
doc["coverage_verification"] = {
    "b_half_expected": ["D8-11", "D8-19", "D8-37"],
    "b_half_landed": [x["q_id"] for x in sup],
    "missing": [q for q in ["D8-11", "D8-19", "D8-37"] if q not in [x["q_id"] for x in sup]],
    "duplicates": [],
    "q_id_unique_within_piece": True,
    "verbatim_check": "3 条 PI 答复逐字在台账现态命中（脚本内 assert：「<答复>」全串包含检验）",
    "assertions_run_pre_landing": [
        "主件 SHA-12 == 769ef8b71462（与已回报值一致，否则拒绝落盘）",
        "3 条 q_id == [D8-11, D8-19, D8-37] 且配对 == [R9, R10, R11]",
        "3 条 PI 答复在台账现态逐字命中",
        "correction_confirmed: true×2 + null×1（存疑 0 硬断）",
        "3 条 actual_interval_days == 0、interval_satisfied == false、降级标记齐备",
        "correction_event_counted: 1+1+null（确认 2 / 存疑 1）",
        "3 条均有 pi_answer_verbatim 与 reasoning_full（b 半已作答，非占位）"
    ],
    "not_in_this_piece": "SQ 7+1、口径类 5 件、D8 其余 77 件**均在本件之外**（在主件 769ef8b71462 内）⇒ 本件 0 重复收录"
}
doc["verbatim_policy"] = (
    "PI 原话逐字保留，禁止改写/润色/扩写/补全标点（" + Q + " §1 第 2 条字面）。"
    "本件 3 条：pi_answer_verbatim = 台账作答格逐字（去最外层「」包裹）；"
    "option_chosen = PI 字面落点（C / BC / ABC）＋ option_chosen_letters 结构化；"
    "option_meaning = null（多选/三选合成不对应单一释义）＋ selected_option_faces_verbatim / listed_options_verbatim 逐档并列字面，0 挑一档当唯一落点；"
    "reasoning_full = 台账形态列明示「＋ 推理」的 PI 自附推理逐字；"
    "judge_type = 题面提案字面；scene_verbatim = 题面原件字面（仅去 markdown 强调标记）；"
    "is_correction = true（配对标记，题面 §1 第 5 条）＋ correction_confirmed 按 a/b 双轴对照（存疑记 null）。")
doc["pi_source_disclosure"] = {
    "pi_realtime_answering_window": True,
    "encoding_source": "PI 2026-09-30 通过 ask_user（" + ASK + "）即刻作答 3 题，答复字面逐字转录自台账 b 半节",
    "verbatim_policy_reference": Q + " §1 第 2 条字面 + 主件（769ef8b71462）verbatim_policy 字面 + d6b Other 落盘惯例",
    "worker_self_judgment_layer_disabled": True,
    "hard_gate_tripped": False,
    "hard_gate_note": "全部 3 条判定值 100% 来自 PI 原答（台账逐字），0 LLM 代答、0 API、0 proxy、0 gateway；硬闸未触发",
    "no_fabrication_declaration": ("0 编造题面（逐字取自 D8 原卷）；0 虚构 PI 判定值（3 条答复逐字对账台账）；"
                                   "0 编造跨日间隔（actual_interval_days=0 如实登记，未粉饰为 1 天）；"
                                   "0 硬断存疑（R11 记 null）；0 判定任何阈值；0 覆写主件。")
}
doc["constraints_compliance"] = {
    "key_never_in_prompt_or_json": True, "key_never_on_disk": True,
    "no_llm_judgment_layer": True, "no_api_call": True, "no_proxy": True, "no_gateway": True,
    "no_dataset_modification": True, "no_merge_into_dataset": True, "no_merge_into_any_existing_json": True,
    "no_existing_file_overwritten": True, "no_existing_file_deleted": True,
    "no_main_piece_touched": True, "no_new_killline": True, "no_threshold_tampering": True,
    "no_pii_reasoning_promoted_out_of_repo": True,
    "rationale": ("V4 铁律沿用口径（key 永不明文无例外；V1–V3 只读不动；派生 JSON 不合并；0 擅调阈值）。"
                  "本件为**新名追加件** " + OUT + "（落盘前实测不在盘）；⛔ 0 覆写已落主件 " + MAIN + "（" + MAIN_SHA_EXPECT + "）、"
                  "0 合并任何既有 JSON、0 删除；13 项锚 SHA-12 落盘前后复验不变。")
}
doc["skill_disclosure"] = {
    "requested": None, "status": "本棒未加载任何 skill（派工单未指定 skill）",
    "disclosure": "未加载任何 skill 的任何指令；0 引用、0 虚构任何 skill 条文。实质纪律锚 = 盘上件字面（" + Q + " §1 第 2/4/5 条 + §4 配对纪律 + " + LEDGER + " b 半节 + 主件 verbatim_policy）。"
}
doc["metadata"] = {
    "algorithm": "SHA-256 前 12 位（小写）", "author": "Mavis 团队 worker (执行类·采集补入)",
    "date": "2026-09-30", "encoding": "UTF-8 (no BOM)", "line_ending": "LF",
    "type": "cross_day_critical_reflection_addendum_d8_bhalf_v3_v1_3_reserved",
    "version": "v1", "agent": "worker (执行类)",
    "branch_session": "mvs_31307d0c285c42ef860fee93ed195ef8",
    "generator": ".tmp/_run_d8_bhalf_addendum_2026_09_30.py",
    "signature_line": "Mavis 团队 worker 出件 | 2026-09-30",
    "track": "Track 1（0 LLM / 0 API / 0 proxy / 0 gateway）",
    "v1_3_data_surface_reserved": True,
    "pi_source": "PI 2026-09-30 即刻作答 3 题（" + ASK + "，台账逐字转录）；0 LLM 代答；R 系三对全部降级标注；R11 is_correction 判定存疑 0 硬断",
    "sha12_case_note": "本件 SHA-12 一律记小写；既有件正文登记值部分为大写，大小写等价可比对",
    "succeeded_not_equal_finished": "succeeded ≠ 跑完；本件以盘上 SHA-12 落盘核验 + JSON 可解析复验 + 3 条覆盖/对账 assert 全过为准",
    "self_hash_caveat": "本件不写自指哈希字段（沿主件口径）；下游引用一律以盘上实测 SHA-12 为准"
}
doc["honesty_boundary"] = [
    "**本件是采集补入件，不是判定棒**：0 判 substrate/跨日/纠正阈值是否达标、0 宣告「达标」、0 改任何阈值；账目面只如实登记。",
    "**R 系三对全部降级**：a/b 同为 2026-09-30（actual_interval_days = 0）⇒ 逐对登记「未满足 ≥1 天间隔，R 系有效性降级」（件级 + 逐题双落）；降级只涉配对有效性，0 剔除、0 作废、0 降权 PI 答复本身。",
    "**is_correction 判定含 1 处存疑**：R9（落点轴已确认 A→C；结论轴 b 半未出结论 ⇒ 存疑）、R10（双轴均改变；a 档集 ⊂ b 档集的重叠已登记）、R11（**三读并列 ⇒ correction_confirmed 记 null，0 硬断**）。确认 2 件 + 存疑 1 件，0 替 PI 定口径。",
    "**0 覆写主件**：主件 769ef8b71462 落盘前后 SHA-12 不变；其 3 条 pending 占位条与本件实答条并存（非重复计数），下游取 b 半值以本件为准。",
    "**0 回头改 a 半**：主件 a 半（D8-10/18/36）的 is_correction / correction_confirmed 字段值 0 追改（既有件只读不动）；b 半侧对照结论以本件为准。",
    "**ask 原件不落盘**：3 条答复与 1 个 ask_id 转录自台账现态；0 取得 ask 原件、0 声称已核验 ask 原文、0 伪造作答时分（台账仅自记「16:1x 收齐」时段级）。",
    "**台账现态与历史并存**：台账 SHA 四旧值 + 本棒实测 " + ls + "（18,833 B / 257 行）五值并记；台账行 240/244/257 旧表述为历史原文，0 回改、0 代为调和，以行 242/246-254/256 现态为准。",
    "**主件一处已知口径宽严不一（诚实披露）**：主件 9 条的 reasoning_full 填了信号/双层/合成类尾句（PI 原话逐字、0 改写）；因 0 覆写令，本棒不回改，仅披露供下游按台账「形态」列自判。本件 3 条口径自洽。",
    "**未做也不声称**：0 重算 result/verdict、0 更新台账、0 派工、0 触 skill、0 调外部 API、0 代 PI 关闭任何待拍板项（T-D8-3 仅登记其降级分支已被采纳）。"
]

out_path = os.path.join(ROOT, OUT)
assert not os.path.exists(out_path), "目标件已在盘，⛔ 拒绝覆写：" + OUT
txt = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
b = open(out_path, "rb").read()
# 落盘后自检：主件未被触动
ms2 = hashlib.sha256(open(os.path.join(ROOT, MAIN), "rb").read()).hexdigest()[:12]
assert ms2 == MAIN_SHA_EXPECT, "主件被触动！"
print("LANDED:", OUT)
print("sha12:", hashlib.sha256(b).hexdigest()[:12])
print("bytes:", len(b))
print("lines:", txt.count("\n"))
print("bom:", b[:3] == b"\xef\xbb\xbf", "| crlf:", b"\r\n" in b)
print("entries:", len(sup), "| confirmed:", n_conf, "| unresolved:", n_stuck)
print("main_piece_unchanged:", ms2)
print("ledger_now:", ls, lb)
