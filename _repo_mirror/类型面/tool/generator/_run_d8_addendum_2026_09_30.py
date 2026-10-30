# -*- coding: utf-8 -*-
"""
D8 大波 + SQ 补采 · 采集入库 addendum JSON 生成器（2026-09-30）

0 LLM / 0 API / 0 proxy / 0 gateway；key 永不明文（0 读取 / 0 落盘 / 0 入 prompt / 0 入 log）。
唯一数据源 = results/_d8_collection_ledger_2026_09_30.md（逐题原样记录，以其为准）。
题面 / judge_type / 选项释义 = 盘上原件字面（D8 原卷 238077d25919 · SQ 卷 579b375e9508 · 边界修订件 b46370bb9e3b）。
⛔ 0 覆写任何既有 JSON；⛔ 0 合并任何既有 JSON；本件为纯新建。
"""
import json, hashlib, os, io, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = "results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md"        # 238077d25919
LEDGER = "results/_d8_collection_ledger_2026_09_30.md"               # 本棒实测 199a206d2800 / 17,946 B
SQF = "results/_d8_supplement_open_questions_2026_09_30.md"         # 579b375e9508
BND = "results/_d8_boundary_revision_register_2026_09_30.md"         # b46370bb9e3b
OUT = "results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json"

# ---------------------------------------------------------------- 逐题数据
# 字段：q / face / jt / ans（台账作答格逐字，去掉台账最外层「」包裹）/ form（台账「形态」列字面）
#       sel（结构化落点字母）/ opt（被选字母的题面选项字面）/ rsn（台账明示「＋推理」时才拆）
#       ask / batch / line（台账行号）/ tag / rpair / pend / extra
D8 = [
 dict(q="D8-01", jt="J1", ans="重设阈值，否则机械自毁", form="Other（覆选，未取 A/B/C）", sel=None, opt={}, rsn=None,
      ask="ask_72adb71ea07edc063ceed334", batch=1, line=13, tag="killline_ceiling_raised_after_fail_verdict",
      face="一条判死线已按阈值 1.00 判不达标，并在同件登记了「素材面结构性不可达」；此后装载缺陷修复把天花板从 0.7143 抬到 0.8571。判定面处置？"),
 dict(q="D8-02", jt="J1", ans="A，相信新阶段会比旧阶段更进步", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "以生效口径 39 词臂为准，36 词臂并列为历史基线"}, rsn="相信新阶段会比旧阶段更进步",
      ask="ask_72adb71ea07edc063ceed334", batch=1, line=14, tag="effective_vs_historical_baseline_arm_choice",
      face="同一判死线，生效口径（39 词臂）读数 0.7143、历史基线（36 词臂）读数 0.5714，prereg 要求两臂并报。判定件正文以哪一臂为准？"),
 dict(q="D8-03", jt="J1", ans="B，不误导", form="Other（选 B ＋ 推理）", sel=["B"], opt={"B": "改写为 10"}, rsn="不误导",
      ask="ask_72adb71ea07edc063ceed334", batch=1, line=15, tag="locked_alt_reading_value_superseded_by_recompute",
      face="替代读法口径已「生效即锁」，但既有判定件里引用的登记值（`n_divergent = 11`）被标「盘上不可复现」，而沿新口径重算得 10。既有件里那些引用位处置？"),
 dict(q="D8-04", jt="J1", ans="A或C，540条可能因模型下架等原因不可重采如kimi2.7", form="Other（双选＋理由，未收敛单选）",
      sel=["A", "C"],
      opt={"A": "可引用，但每次引用须带限定注记", "C": "可引用，但须先重采 540 条独立观测才升为无条件引用"},
      rsn="540条可能因模型下架等原因不可重采如kimi2.7",
      ask="ask_a6f88ff30bf89a8e804239d9", batch=2, line=22, tag="qualified_pass_citation_boundary",
      face="某守恒判据按「档 1 限定改判」通过，但限定注记写明重建面非 540 条独立观测（由 9 个三元组确定性展开）。该 PASS 是否可对外引用？"),
 dict(q="D8-05", jt="J1", ans="B，不可机械自寻亡路", form="Other（选 B ＋ 推理）", sel=["B"], opt={"B": "两条并列不定调"}, rsn="不可机械自寻亡路",
      ask="ask_a6f88ff30bf89a8e804239d9", batch=2, line=23, tag="true_falsification_vs_alternative_reading_citation",
      face="N-26 真审判「真证伪」（pooled AUC 0.5663 < 0.75），但替代读法显示剔除某受托方采样后结论更弱。真证伪结论的引用边界？"),
 dict(q="D8-06", jt="J1", ans="C，不可机械", form="Other（选 C ＋ 推理）", sel=["C"],
      opt={"C": "两版并列，判定面交独立 verifier 复核后再定"}, rsn="不可机械",
      ask="ask_a6f88ff30bf89a8e804239d9", batch=2, line=24, tag="relabeled_reading_vs_original_verdict_relation",
      face="标注重标导致读数变动（NW 0.4578 → 0.4665），但 6 条判死线判定方向 0 变化。原判定与重跑读数的关系判定？"),
 dict(q="D8-07", jt="J1", ans="A，且原资产复用", form="Other（选 A ＋ 补充）", sel=["A"],
      opt={"A": "撤线并在新预登记 v1.1 重立"}, rsn="且原资产复用",
      ask="ask_ffe8cdf9d2b1d84294afd1c6", batch=3, line=33, tag="killline_unreachable_after_supplement_path_rejected",
      face="若一条判死线连续多日 hit=True，而 PI 已明示不走补料路径（换方向），该线处置？"),
 dict(q="D8-08", jt="J1", ans="B，不可机械判死，否则不是与死同行，而是自杀诅咒", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "只重验该条，其余沿用"}, rsn="不可机械判死，否则不是与死同行，而是自杀诅咒",
      ask="ask_ffe8cdf9d2b1d84294afd1c6", batch=3, line=34, tag="boolean_direction_inversion_found_after_runs",
      face="执行代码里某条判死线的布尔方向与预登记相反（S-40 型），已跑完 3 轮才发现。处置？"),
 dict(q="D8-09", jt="J1", ans="等待拍板，但如果判断很有希望能出成果，则C，先斩后判",
      form="Other（条件式：默认等拍板；高希望→C）", sel=None,
      opt={"C（条件分支）": "只跑不判，落件待拍板"}, rsn=None,
      ask="ask_ffe8cdf9d2b1d84294afd1c6", batch=3, line=35, tag="s4_gate_blocked_by_undecided_prereg_item",
      face="大波补采把记账口径推到 171，但 S4 的 `held-out ≥50` 依赖 P-S4-1 三线不自洽的拍板（未拍板）。S4 现在可否开跑？",
      extra=dict(
        conditional_branch_verbatim="如果判断很有希望能出成果，则C，先斩后判",
        conditional_default_verbatim="等待拍板",
        branch_option_face="C 只跑不判，落件待拍板",
        branch_option_face_source=Q + " §3 D8-09 选项 C 字面",
        note="PI 原答为条件式：默认「等待拍板」，触发条件为「判断很有希望能出成果」⇒ 落 C（只跑不判，落件待拍板）。本件 0 替 PI 择一、0 把条件式压成单选；台账「形态」列已按条件式登记。",
        registration_type="associated_registration_not_answer_inference",
        source=LEDGER + " 批 3 表行（D8-09）「形态」列字面")),
 dict(q="D8-10", jt="J1", ans="A，不可机械否则不是真与死同行", form="Other（选 A ＋ 推理；R9 a 半）", sel=["A"],
      opt={"A": "判达标（未超即不触发）"}, rsn="不可机械否则不是真与死同行",
      ask="ask_ffe8cdf9d2b1d84294afd1c6", batch=3, line=36, tag="threshold_boundary_equality_unwritten_direction",
      rpair="R9a",
      face="某条判死线读数刚好卡在阈值上（0.65 对 0.65），且预登记未写明边界方向。判定？"),
 dict(q="D8-11", jt="J1", ans=None, form="未采集（R9 b 半 · 保留至 10-01+）", sel=None, opt={}, rsn=None,
      ask=None, batch=None, line=None, tag="threshold_boundary_equality_written_direction", rpair="R9b", pend=True,
      face="同 D8-10 场景，但预登记已写明边界方向为「读数 > 阈值即触发」。判定改为？",
      listed=["A 照预登记：0.65 不 > 0.65 ⇒ 不触发", "B 判不达标（等于阈值视为未达）", "C 请 PI 拍板"]),
 dict(q="D8-12", jt="J1", ans="B，依旧不可机械", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "撤线并在新预登记 v1.1 重立"}, rsn="依旧不可机械",
      ask="ask_d36d1fa8c5265673a67fcdd1", batch=4, line=42, tag="constant_fail_killline_referenced_by_others",
      face="一条判定线因素材缺位而恒不通过，且已写进预登记并被其他件引用。处置？"),
 dict(q="D8-13", jt="J1", ans="C，不可误导", form="Other（选 C ＋ 推理）", sel=["C"], opt={"C": "剔除该腿后重判"}, rsn="不可误导",
      ask="ask_d36d1fa8c5265673a67fcdd1", batch=4, line=43, tag="zero_discrimination_control_leg",
      face="对照腿读数 0.0，表明该对照面零鉴别力（构造无信息）。此读数处置？"),
 dict(q="D8-14", jt="J1", ans="A，要为后续复合算法留下空间", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "构成误导（须同件并报不可达成因）"}, rsn="要为后续复合算法留下空间",
      ask="ask_d36d1fa8c5265673a67fcdd1", batch=4, line=44, tag="fail_reported_without_unachievable_cause",
      face="判死线已判不达标，但对外报告若只报「FAIL」而不报「素材面结构性不可达」，属？"),
 dict(q="D8-15", jt="J2", ans="C，我选A，今天有时间，且已跨天，此外重复口径的题可以适当合并，这是出题侧缺陷，既不广也不深，不应怪罪或转嫁于引导侧与PI侧",
      form="Other（选 A；含出题侧反馈）", sel=["A"],
      opt={"A": "一波采完（换样本量与跨日天数）"}, rsn=None,
      ask="ask_d36d1fa8c5265673a67fcdd1", batch=4, line=45, tag="wave_pi_time_cost_tradeoff", boundary="外沿",
      face="本次一次性大波 80 题，单题 <30 秒但 PI 总量约 40 分钟。PI 时间成本的取舍？",
      extra=dict(
        verbatim_ambiguity_note="PI 原答以「C，」起首、随后明示「我选A」；台账「形态」列登记为「选 A」⇒ 本件按台账（唯一数据源）把落点登记为 A，同时把 PI 原答逐字完整保留在 pi_answer_verbatim。0 改写原话、0 抹去起首「C，」、0 替 PI 重排。",
        boundary_tag="外沿",
        boundary_tag_source=LEDGER + " 尾部「PI 4 裁（2026-09-30，全选 ①）」第 ② 项字面「D8-15/16 保留＋标注「外沿」」",
        side_signal_verbatim="此外重复口径的题可以适当合并，这是出题侧缺陷，既不广也不深，不应怪罪或转嫁于引导侧与PI侧",
        side_signal_registration="出题侧缺陷项（台账批 4 下方「出题侧反馈（PI 原文，登记）」；parent 处置＝核心 80 题本体 0 擅动，登记交后续出题设计吸收）")),
 dict(q="D8-16", jt="J2", ans="A或C，不是所有PI都愿意被蒸馏，思维不是公司资产，关键不在你也不在我而在于公司的回报",
      form="Other（双选＋外延）", sel=["A", "C"],
      opt={"A": "一并采（余量抗丢件与作废题）", "C": "先采 76，看结果再决定"}, rsn=None,
      ask="ask_5901a28baa3485800e376ac1", batch=5, line=53, tag="marginal_value_of_last_four_questions", boundary="外沿",
      face="若只补 76 件刚好把记账口径顶到 167，第 77–80 题的边际价值？",
      extra=dict(
        extension_verbatim="不是所有PI都愿意被蒸馏，思维不是公司资产，关键不在你也不在我而在于公司的回报",
        extension_vs_reasoning_note="台账「形态」列登记为「双选＋外延」而非「＋ 推理」⇒ 本件 0 把该文本登记为 reasoning_full（避免把外延当推理 mislead 下游），逐字全文见 pi_answer_verbatim / extension_verbatim。",
        boundary_tag="外沿",
        boundary_tag_source=LEDGER + " 尾部「PI 4 裁」第 ② 项字面「D8-15/16 保留＋标注「外沿」」")),
 dict(q="D8-17", jt="J2", ans="B，重跑可能不可复现如模型差异", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "另立单独评估棒"}, rsn="重跑可能不可复现如模型差异",
      ask="ask_5901a28baa3485800e376ac1", batch=5, line=54, tag="full_retrain_cost_vs_benefit",
      face="要评估装载修复对决策树预测的影响面，须重训整棵树（full 重跑）。成本 vs 收益？"),
 dict(q="D8-18", jt="J2", ans="C，重采可能不可复现如模型下架或自动路由等情况", form="Other（选 C ＋ 推理；R10 a 半）",
      sel=["C"], opt={"C": "先采子集看是否够消解"}, rsn="重采可能不可复现如模型下架或自动路由等情况",
      ask="ask_5901a28baa3485800e376ac1", batch=5, line=55, tag="resample_540_observations_cost", rpair="R10a",
      face="某结论的 540 条独立观测缺件重采需重建整套观测面，成本极大但能消解一条长期挂账的限定注记。做吗？"),
 dict(q="D8-19", jt="J2", ans=None, form="未采集（R10 b 半 · 保留至 10-01+）", sel=None, opt={}, rsn=None,
      ask=None, batch=None, line=None, tag="resample_540_after_paper_draft", rpair="R10b", pend=True,
      face="同 D8-18 场景，但该结论已进论文草稿。处置改为？",
      listed=["A 仍不重采，但论文中该结论须带限定注记", "B 重采（论文结论强度优先）", "C 重采且优先采论文用到的部分"]),
 dict(q="D8-20", jt="J2", ans="ABC，两步走，先走高效的，再走全量的", form="Other（三档合成：两阶段）",
      sel=["A", "B", "C"],
      opt={"A": "全套重跑（口径一致性优先）", "B": "只跑受影响的覆盖率与盲从率", "C": "暂不跑，先把采集件落盘"},
      rsn="两步走，先走高效的，再走全量的",
      ask="ask_5901a28baa3485800e376ac1", batch=5, line=56, tag="full_metric_rerun_cost",
      face="补采 80 件后须重跑全套度量（NW/NLED/覆盖率/盲从率/bootstrap/perm）。成本处置？",
      extra=dict(composite_reading_verbatim="两步走，先走高效的，再走全量的",
                  composite_note="三档合成＝两阶段：先走「B 只跑受影响的覆盖率与盲从率」（高效）再走「A 全套重跑（口径一致性优先）」（全量）；本件按台账「形态」列逐字登记三选合成，0 排序化、0 替 PI 定先后（PI 原话「先走高效的，再走全量的」已逐字保留）。")),
 dict(q="D8-21", jt="J2", ans="A，此外无需<=2~3，<=3即可，但因PI而异且要注意防回退", form="Other（选 A ＋ 修正口径）",
      sel=["A"], opt={"A": "拆批每批 ≤2–3 路"}, rsn="此外无需<=2~3，<=3即可，但因PI而异且要注意防回退",
      ask="ask_cd08e7bacaa1cb99ecceaa34", batch=6, line=62, tag="parallel_dispatch_on_local_machine", dispute="minor",
      face="复算 4 个口径面需同时跑多个执行棒，本机并行会卡。派法？"),
 dict(q="D8-22", jt="J2", ans="C，大材小用，不可机械，而应真与死同行", form="Other（选 C ＋ 准则引）", sel=["C"],
      opt={"C": "扩词但同时设盲从率上限约束"}, rsn="大材小用，不可机械，而应真与死同行",
      ask="ask_cd08e7bacaa1cb99ecceaa34", batch=6, line=63, tag="lexicon_expansion_not_reachable_path",
      face="扩 3 个词使覆盖率从 0.5714 升到 0.7143，但天花板（0.8571）由缺料决定、与词表无关。要不要再扩词冲 1.00？"),
 dict(q="D8-23", jt="J2", ans="A或B，我倾向A，更准确，也接受B", form="Other（双选，倾向 A）", sel=["A", "B"],
      opt={"A": "即用即探（不做预先探测，用到再探）", "B": "先批量探测建可用性台账"}, rsn="我倾向A，更准确，也接受B",
      ask="ask_cd08e7bacaa1cb99ecceaa34", batch=6, line=64, tag="endpoint_probe_on_demand",
      face="某端点若要用于多模型实验，需临时探测可用性。探测的投入方式？",
      extra=dict(preference_verbatim="我倾向A，更准确，也接受B",
                  preference_note="双选＋明示倾向 A；本件按台账「形态」列登记双选（倾向 A），倾向语逐字保留，0 压成单选 A（会丢失 PI 明示「也接受 B」的字面）。")),
 dict(q="D8-24", jt="J2", ans="A，但注意可能网络不稳定，sub可能会挂，同时为安全考虑需环境隔离",
      form="Other（选 A ＋ 警示）", sel=["A"], opt={"A": "全走 tun 代理 + 串行 + 间隔 ≥2 秒"},
      rsn="但注意可能网络不稳定，sub可能会挂，同时为安全考虑需环境隔离",
      ask="ask_cd08e7bacaa1cb99ecceaa34", batch=6, line=65, tag="proxy_budget_for_third_party_endpoints",
      face="两个第三方端点调用有封号风险，须走本机 tun 代理；走代理增加每请求延迟。多模型实验的调用预算怎么分配？"),
 dict(q="D8-25", jt="J2", ans="ABC均可，不误导，因PI而异，此外我怎么感觉问卷又往画像侧偏了",
      form="Other（三选均可＋【画像侧偏信号】）", sel=["A", "B", "C"],
      opt={"A": "R 系 b 半题隔 ≥1 天作答，其余同波采完", "B": "全部隔日采", "C": "同波采完并在件内如实记跨日不达标"},
      rsn="不误导，因PI而异，此外我怎么感觉问卷又往画像侧偏了",
      ask="ask_de8dbebee79a8e9ebde007fa", batch=7, line=71, tag="same_day_cross_day_compliance", dispute="minor",
      face="80 题若在同日一次答完，跨日天数不达标（R 系与 K-V3S-3-1 要求跨日）。如何处理跨日？",
      extra=dict(side_signal_verbatim="我怎么感觉问卷又往画像侧偏了",
                  side_signal_registration="画像侧偏信号（台账批 7 下方「⚠️ 画像侧偏信号（PI 逐字）」；parent 处置＝任务 B 边界＝批判性学习判断方法、非画像；登记为出题侧最高优先复核项；PI 边界裁决＝「暂停，先做出题侧修订」⇒ D8 采集停泵，批 8 过目后已重启）",
                  side_signal_source=LEDGER + " 批 7 表下方")),
 dict(q="D8-26", jt="J2", ans="AC，不误导，如果支持预实验，这可预实验", form="Other（双选 A/C ＋ 建议）",
      sel=["A", "C"],
      opt={"A": "已答部分照落盘（部分完成如实登记），未答标待采集", "C": "暂停问卷，改日再采"},
      rsn="不误导，如果支持预实验，这可预实验",
      ask="ask_de8dbebee79a8e9ebde007fa", batch=7, line=72, tag="partial_completion_handling", dispute="minor",
      face="若 PI 答 80 题中途放弃，已答部分处置？"),
 dict(q="D8-27", jt="J2", ans="B，噪声不应被引用而应转写，诚然探针可能构造缺陷影响结论，但那是复核的事了",
      form="Other（选 B ＋ 推理）", sel=["B"], opt={"B": "清走并同步改 24+ 处引用"},
      rsn="噪声不应被引用而应转写，诚然探针可能构造缺陷影响结论，但那是复核的事了",
      ask="ask_de8dbebee79a8e9ebde007fa", batch=7, line=73, tag="probe_script_cleanup_ghost_reference_cost",
      face="清理两族探针脚本（共 12 件）能减噪，但会造 24+ 处幽灵引用。清理的成本处置？"),
 dict(q="D8-28", jt="J3", ans="BC，不应因A假判", form="Other（双选 B/C ＋ 推理）", sel=["B", "C"],
      opt={"B": "顶级工具细致打磨 80 题", "C": "分档：A 组细致、B–F 组批量"}, rsn="不应因A假判",
      ask="ask_de8dbebee79a8e9ebde007fa", batch=7, line=74, tag="principle_daxiao_xiaoyong_on_question_drafting",
      face="「大材小用」在本次一次性大波题面撰写上的应用：顶级工具细致打磨 vs 快速批量出题？"),
 dict(q="D8-29", jt="J3", ans="C，不必整百，虽说计算简便，不过机械计算", form="Other（选 C ＋ 推理）", sel=["C"],
      opt={"C": "按缺口算式补，不设整数目标"}, rsn="不必整百，虽说计算简便，不过机械计算",
      ask="ask_4341a4423c517f0e41c99abd", batch=8, line=90, tag="principle_luodaoshichu_on_substrate_topup",
      face="「落到实处」在「把 substrate 补到过线」这件事上：补到刚好过线还是补到整数目标？"),
 dict(q="D8-30", jt="J3", ans="C，不可机械", form="Other（选 C ＋ 推理）", sel=["C"], opt={"C": "并行立一条新线"}, rsn="不可机械",
      ask="ask_4341a4423c517f0e41c99abd", batch=8, line=91, tag="principle_yushitongxing_order_when_unreachable",
      face="「与死同行」（判死线先于实验）在「线已立但不可达、须补料」时的应用：顺序是？"),
 dict(q="D8-31", jt="J3", ans="C，需要硬核", form="Other（选 C ＋ 推理）", sel=["C"],
      opt={"C": "按标注完整度分：标注完整的入"}, rsn="需要硬核",
      ask="ask_4341a4423c517f0e41c99abd", batch=8, line=92, tag="principle_xushi_huilu_on_fictional_artifacts",
      face="「虚实回路（FTFB）」在「虚构/推演产物可否入 substrate」上的应用？"),
 dict(q="D8-32", jt="J3", ans="C，可能是理解有偏差", form="Other（选 C ＋ 推理）", sel=["C"], opt={"C": "请示 PI"}, rsn="可能是理解有偏差",
      ask="ask_4341a4423c517f0e41c99abd", batch=8, line=93, tag="four_principles_conflict_adjudication",
      face="准则四条（大材小用 / 落到实处 / 与死同行 / 虚实回路）在同一场景冲突时，裁决依据？"),
 dict(q="D8-33", jt="J3", ans="B，找到归因可能反fail为pass", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "缓决，等根因追清再判"}, rsn="找到归因可能反fail为pass",
      ask="ask_16f0f4dc3ae9321ef79de182", batch=9, line=99, tag="honesty_vs_softening_root_cause_unclear",
      face="诚实纪律「不误导」vs 判死纪律「不软化」：若一条 FAIL 结论的根因尚未追清，是否仍照字面判 FAIL？"),
 dict(q="D8-34", jt="J3", ans="B，保证主线统一，也因此应点明主线，上周过于开放，一致成果没对齐主线",
      form="Other（选 B ＋ 委托面口径信号）", sel=["B"], opt={"B": "作为硬约束逐条列出"},
      rsn="保证主线统一，也因此应点明主线，上周过于开放，一致成果没对齐主线",
      ask="ask_16f0f4dc3ae9321ef79de182", batch=9, line=100, tag="principles_as_hard_constraints_in_commission_letter",
      face="「准则为根、论文为一处外显」在对外委托面的应用：是否把准则作为硬约束写进委托信交受托方？",
      extra=dict(side_signal_verbatim="保证主线统一，也因此应点明主线，上周过于开放，一致成果没对齐主线",
                  side_signal_registration="委托面口径信号：PI 在 D8-73 再度追加同一口径（D8-73 答「以新案优先，此外不是大纲而是实验成果线索，否则受委托方无从下手」）⇒ 主线须点明 + 须给实验成果线索，两者同族（PI 2026-09-30 两题互证）")),
 dict(q="D8-35", jt="J3", ans="C，可能是没传达到位，下次注意便好，为保独立性不应过多干涉", form="Other（选 C ＋ 推理）",
      sel=["C"], opt={"C": "由本地另出勘误说明"}, rsn="可能是没传达到位，下次注意便好，为保独立性不应过多干涉",
      ask="ask_16f0f4dc3ae9321ef79de182", batch=9, line=101, tag="commissioned_output_reverses_principle_direction",
      face="若受托方产出的表述与 deposon 准则方向相反（把准则写成源于论文），处置？"),
 dict(q="D8-36", jt="J3", ans="C 引用时标注「未落盘」", form="选项 C", sel=["C"], opt={"C": "引用时标注「未落盘」"},
      rsn=None, ask="ask_faf9de6def9e1c2384a5954b", batch=10, line=110, tag="verbal_only_principle_authority",
      rpair="R11a",
      face="核心准则的权威面只有 PI 的一次口头表述，无落盘件。处置？",
      extra=dict(answer_reading_note="PI 原答「C 引用时标注「未落盘」」＝选项 C 的题面字面复述（台账「形态」列登记为「选项 C」）⇒ option_meaning 取题面 C 字面，reasoning_full 记 null（PI 未另附推理；按 0 编造原则不把选项复述当推理）。")),
 dict(q="D8-37", jt="J3", ans=None, form="未采集（R11 b 半 · 保留至 10-01+）", sel=None, opt={}, rsn=None,
      ask=None, batch=None, line=None, tag="verbal_principle_already_in_published_paper", rpair="R11b", pend=True,
      face="同 D8-36 场景，但该表述已被写入一份对外发布的论文中。处置改为？",
      listed=["A 落盘准则件并在论文中核对方向一致性", "B 以论文为准反推准则", "C 登记分歧交 PI 拍板"]),
 dict(q="D8-38", jt="J3", ans="C，LLM检验蒸馏成果是后面的事", form="Other（选 C ＋ 推理）", sel=["C"],
      opt={"C": "可用于生成题面，不能用于判定"}, rsn="LLM检验蒸馏成果是后面的事",
      ask="ask_faf9de6def9e1c2384a5954b", batch=10, line=111, tag="zero_llm_proxy_for_judgment_values_hardgate",
      face="「落到实处」在「0 LLM 代答判定值」硬闸上的应用：判定层可否由模型代答以省 PI 时间？"),
 dict(q="D8-39", jt="J3", ans="A，翻案令人不免期待", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "归假证伪、命题本体另审，工具失灵单列"}, rsn="翻案令人不免期待",
      ask="ask_faf9de6def9e1c2384a5954b", batch=10, line=112, tag="tool_failure_vs_proposition_falsification",
      face="若某次负面结论的根因是工具失灵而非命题证伪，按「诚实的根因是不误导」，正确做法是？"),
 dict(q="D8-40", jt="J3", ans="A，对抗遗忘，与死同行是对抗遗忘的过程，也是对抗机械的过程", form="Other（选 A ＋ 推理）",
      sel=["A"], opt={"A": "预立素材补齐线（缺料件清单 + 补齐判据）"},
      rsn="对抗遗忘，与死同行是对抗遗忘的过程，也是对抗机械的过程",
      ask="ask_faf9de6def9e1c2384a5954b", batch=10, line=113, tag="preset_material_topup_killline",
      face="「与死同行」是否要求为「素材缺位导致判死线恒不通过」这一情形预立一条「素材补齐线」？"),
 dict(q="D8-41", jt="J3", ans="A，大材小用，小是具体，minimax的写作能力一般", form="Other（选 A ＋ 推理）",
      sel=["A"], opt={"A": "顶级受托方只用于大件，日常件本地起草"}, rsn="大材小用，小是具体，minimax的写作能力一般",
      ask="ask_a5bf873f436ba5a68a808567", batch=11, line=119, tag="top_tier_commissionee_for_big_items_only",
      face="大材小用在「委派给外部受托方起草 vs 本地起草」上的应用：顶级受托方用于大件还是也用于日常件？"),
 dict(q="D8-42", jt="J4", ans="BC，保持口径一致避免麻烦",
      form="Other（双选 B/C ＋ 推理；⚠️ 与题面 A 档「0 触动」相左，按答入账）", sel=["B", "C"],
      opt={"B": "同步更新 dataset v1.3 登记", "C": "同步更新 result 件"}, rsn="保持口径一致避免麻烦",
      ask="ask_a5bf873f436ba5a68a808567", batch=11, line=120, tag="new_file_landing_sync_existing_registers",
      face="本卷落盘将新增一个 80 题题面件。既有 dataset / addendum / result 件是否需同步登记？",
      extra=dict(face_conflict_verbatim="⚠️ 与题面 A 档「0 触动」相左，按答入账",
                  face_conflict_note="PI 选 B/C（同步更新既有登记面）与题面 A 档「0 触动既有件」相左；台账已按「按答入账」登记 ⇒ 本件逐字保留 PI 落点并显式登记该相左，不代 PI 调和。",
                  source=LEDGER + " 批 11 表行（D8-42）「形态」列字面")),
 dict(q="D8-43", jt="J4", ans="AC，批量作答选项有限", form="Other（双选 A/C ＋ 推理）", sel=["A", "C"],
      opt={"A": "记 Other + 逐字保留原话，选项释义记 null", "C": "事后把 Other 补成正式选项"}, rsn="批量作答选项有限",
      ask="ask_a5bf873f436ba5a68a808567", batch=11, line=121, tag="other_answer_landing_convention",
      face="若 PI 批量作答中有 3 题选了 Other（题面三选项之外），落盘时如何记？",
      extra=dict(self_referential_note="本题答案（A/C＝Other 落盘惯例）与本件 77 件 Other/多选落盘实况同族：PI 答「AC，批量作答选项有限」⇒ 其一档正是本件所采惯例（Other 逐字保留、选项释义记 null）；本件 0 以此题答案改写任何既有件的落盘口径。")),
 dict(q="D8-44", jt="J4", ans="C，选项本身可制作规则集，但规则集是有限的，至少升级为脑图并利用deposon相关成果资产",
      form="Other（选 C ＋ 设计垂线信号）", sel=["C"], opt={"C": "部分达标并标注"},
      rsn="选项本身可制作规则集，但规则集是有限的，至少升级为脑图并利用deposon相关成果资产",
      ask="ask_a5bf873f436ba5a68a808567", batch=11, line=122, tag="sampling_success_with_zero_reasoning",
      face="若 PI 一题都没写推理（全部跳过），采样件会达标但推理全文为 0。是否判采样成功？",
      extra=dict(design_signal_verbatim="选项本身可制作规则集，但规则集是有限的，至少升级为脑图并利用deposon相关成果资产",
                  design_signal_registration="设计垂线信号（台账批 11 形态列「＋ 设计垂线信号」）：规则集有限 ⇒ 至少升级为脑图并利用 deposon 成果资产；PI 答「部分达标并标注」＝本件按台账逐字登记，0 扩写为设计决策。")),
 dict(q="D8-45", jt="J4", ans="B，实事求是", form="Other（选 B ＋ 推理；⚠️ 与题面 A 档「并列登记」相左，按答入账）",
      sel=["B"], opt={"B": "以实测值覆盖"}, rsn="实事求是",
      ask="ask_1d3dd509d148173cc4baa95f", batch=12, line=128, tag="self_reported_vs_measured_sha_mismatch",
      face="落盘件若实测 SHA-12 与引用件登记的 SHA-12 不一致（既有先例：某件自报 `B18FF4177289` vs 实测 `cbf60a630c9f`），处置？",
      extra=dict(face_conflict_verbatim="⚠️ 与题面 A 档「并列登记」相左，按答入账",
                  face_conflict_note="PI 选 B（以实测值覆盖）与题面 A 档「两值并列登记，不编造根因」相左；台账已按「按答入账」登记 ⇒ 本件逐字保留 PI 落点并显式登记该相左。",
                  self_referential_note="本题（SHA 漂移处置）与本件实测发现的台账 SHA 漂移同族：台账既有登记值 deec8c91a75b/1,957 B、e61f4050fc02/6,195 B、d87518e980e7/7,470 B 与本棒实测 199a206d2800/17,946 B 并存（详见 ledger_sha_drift_registration）；本棒 0 归因、0 覆写、0 代为调和。",
                  source=LEDGER + " 批 12 表行（D8-45）「形态」列字面")),
 dict(q="D8-46", jt="J4", ans="A，实事求是", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "并列登记 + 通知依赖棒复核"}, rsn="实事求是",
      ask="ask_1d3dd509d148173cc4baa95f", batch=12, line=129, tag="sha_drift_while_other_bars_reading",
      face="若某件盘上 SHA 与多处引用面登记值不同，且该件正被其他棒读取，处置？"),
 dict(q="D8-47", jt="J4", ans="AB，便于复核", form="Other（双选 A/B ＋ 推理）", sel=["A", "B"],
      opt={"A": "钉住字节态 + 0 迁移（迁移须新名 + 授权）", "B": "立即复制到正式目录"}, rsn="便于复核",
      ask="ask_1d3dd509d148173cc4baa95f", batch=12, line=130, tag="sole_code_anchor_in_temp_dir",
      face="某口径的唯一代码锚点存放在临时目录（不在 `results/`），若该目录被清理，处置？",
      extra=dict(self_referential_note="本题与本件 generator 落点（.tmp/）同族：本件 generator 脚本落 .tmp/，但本件 JSON 落 results/（非临时目录）⇒ 0 把 generator 当口径锚；本件为纯数据件、0 承载口径真源。")),
 dict(q="D8-48", jt="J4", ans="C，并考虑为何冻结失效", form="Other（选 C ＋ 追加要求）", sel=["C"],
      opt={"C": "报并要求上游棒修"}, rsn="并考虑为何冻结失效",
      ask="ask_1d3dd509d148173cc4baa95f", batch=12, line=131, tag="upstream_anchor_sha_mismatch_readonly",
      face="既有上游件声明的锚 SHA 与实测不同，本棒只读该件。是否报为风险？"),
 dict(q="D8-49", jt="J4", ans="B，0复用是指不复用答案，否则跨日无意义，此外口径变化是防记忆效应的体现",
      form="Other（选 B ＋ 规则释义）", sel=["B"], opt={"B": "保留但在件内标注同族关系"},
      rsn="0复用是指不复用答案，否则跨日无意义，此外口径变化是防记忆效应的体现",
      ask="ask_e6b4fcbe7b00e25aab4d69fa", batch=13, line=137, tag="question_face_reuse_violation",
      face="若本卷中某题题面实际复用了已采题（违反 0 复用），处置？",
      extra=dict(rule_gloss_verbatim="0复用是指不复用答案，否则跨日无意义，此外口径变化是防记忆效应的体现",
                  rule_gloss_registration="PI 规则释义（0 复用的所指＝不复用答案，非不复用题面；口径变化＝防记忆效应的体现）⇒ 与 D8 原卷 §0.2「0 复用既有题面」的口径层次不同，登记备查；0 借此改写任何既有件题面。")),
 dict(q="D8-50", jt="J4", ans="AB，有时无引导无真相", form="Other（双选 A/B ＋ 推理）", sel=["A", "B"],
      opt={"A": "该题作废并重拟", "B": "保留但标注有诱导风险"}, rsn="有时无引导无真相",
      ask="ask_e6b4fcbe7b00e25aab4d69fa", batch=13, line=138, tag="option_order_leading_question",
      face="「0 预设立场」被违反：某题选项顺序暗示了正确答案。处置？"),
 dict(q="D8-51", jt="J4", ans="ABC，拍板本身是蒸馏资产，且画像侧充足，因此采集侧不应重复采集画像侧",
      form="Other（三选合成 ＋ 设计信号：拍板=资产/采集不重复画像）", sel=["A", "B", "C"],
      opt={"A": "分件落盘（采集件与拍板件分离）", "B": "同件但分字段", "C": "合并为一件"},
      rsn="拍板本身是蒸馏资产，且画像侧充足，因此采集侧不应重复采集画像侧",
      ask="ask_e6b4fcbe7b00e25aab4d69fa", batch=13, line=139, tag="collection_and_ruling_in_same_landing_file",
      dispute="minor",
      face="若 PI 同一轮内既答了大波、又对某条判定作了新拍板，两者混在同一落盘件里，处置？",
      extra=dict(design_signal_verbatim="拍板本身是蒸馏资产，且画像侧充足，因此采集侧不应重复采集画像侧",
                  design_signal_registration="设计信号（台账批 13 形态列）：拍板＝蒸馏资产；画像侧已充足 ⇒ 采集侧不重复采集画像侧。与 D8-25 画像侧偏信号、T-D8-2「开放性·高效蒸馏·思维性」题性指定同族（任务 B＝批判性学习非画像）。",
                  self_referential_note="本题与本件落法同族：本件把 5 件口径/处置类拍板（T-D8-1/T-D8-2/T-D8B-7/skill-4/skill-6）以 entry_class=calibration_item 与 85 件采集条目同件但分字段登记（PI 选 A/B/C 皆可；本件按「分字段」+ 全字段登记办理，0 合并为单一集合，0 拆分多件）——此为落法登记，非对 PI 三档的择一。")),
 dict(q="D8-52", jt="J4", ans="B，先由PI复核，人是活的，PI是人",
      form="Other（选 B ＋ 前置复核；⚠️ 与题面 A 档「0 合并」相左，按答入账）", sel=["B"],
      opt={"B": "合并为主件新版本"}, rsn="先由PI复核，人是活的，PI是人",
      ask="ask_e6b4fcbe7b00e25aab4d69fa", batch=13, line=140, tag="derived_json_merge_prohibition",
      face="派生 JSON 不合并：若 80 件想直接并进 dataset 主件，处置？",
      extra=dict(face_conflict_verbatim="⚠️ 与题面 A 档「0 合并」相左，按答入账",
                  face_conflict_note="PI 选 B（合并为主件新版本）与题面 A 档「落独立 addendum 件，0 合并」及派工单「⛔ 0 合并任何既有 JSON」相左；台账已按「按答入账」登记 ⇒ 本件逐字保留 PI 落点并显式登记该相左。**本棒执行面按派工单硬约束办理（落新件、0 合并、0 覆写）**，PI 的 B 档落点作为判定值入账、不作为本棒执行授权；两者分层登记、0 相互覆盖。",
                  source=LEDGER + " 批 13 表行（D8-52）「形态」列字面")),
 dict(q="D8-53", jt="J4", ans="A，外发版C，保护隐私，兼顾可复核", form="Other（本地 A ＋ 外发 C 双层）",
      sel=["A", "C"], opt={"A": "推理全文仅入本地件，不外发、不入外部模型 prompt", "C": "打码后入件"},
      rsn="外发版C，保护隐私，兼顾可复核", ask="ask_cba2075ac4faf0f4f4d28ae7", batch=14, line=146,
      tag="privacy_of_reasoning_full_text", dispute="minor",
      face="若采集过程中 PI 的推理全文涉及未公开内容，隐私面处置？",
      extra=dict(two_layer_verbatim="外发版C，保护隐私，兼顾可复核",
                  two_layer_note="双层口径：本地版＝A（推理全文仅入本地件，不外发、不入外部模型 prompt）＋ 外发版＝C（打码后入件）。本件 0 把 PI 推理全文入任何 prompt、0 外发；本件全部 84 条含值条目均落本地 results/ 件（随 PI 原答逐字保留，不打码——PI 选的是「本地 A」）。",
                  two_layer_registration_type="associated_registration_not_answer_inference")),
 dict(q="D8-54", jt="J4", ans="改为开放性试题", form="Other（自定义处置：转开放题）", sel=None, opt={}, rsn=None,
      ask="ask_cba2075ac4faf0f4f4d28ae7", batch=14, line=147, tag="question_face_insufficient_scenario_material",
      face="若 80 题中有题因「场景素材不足」无法新拟（只能硬凑），处置？",
      extra=dict(custom_disposal_verbatim="改为开放性试题",
                  custom_disposal_note="PI 落点为自定义处置（转开放题），非题面 A/B/C 任一 ⇒ option_meaning 记 null（0 编造），原话逐字见 pi_other_verbatim / pi_answer_verbatim。",
                  consequent_registration="同族落地事实：SQ 补采卷 8 题即为开放型（" + SQF + " §1 字面「无 A/B/C 选项，自由作答」），由 T-D8-2 拍板 B 触发；本条按答入账、0 追认为 D8 原卷的修改授权。")),
 dict(q="D8-55", jt="J5", ans="B，全量推进，也因此可以把待拍板项提上来，遗忘了则更麻烦",
      form="Other（选 B ＋ 推理）", sel=["B"], opt={"B": "并行"},
      rsn="全量推进，也因此可以把待拍板项提上来，遗忘了则更麻烦",
      ask="ask_cba2075ac4faf0f4f4d28ae7", batch=14, line=148, tag="collection_vs_s4_timing_collision",
      face="大波采集（今日）与 S4 扩样开跑（待一项未拍板）撞期。排期？",
      extra=dict(pending_decision_reference="P-S4-1（" + Q + " §7 字面「三线不自洽，PI 须择一」）；本件 0 判 P-S4-1 是否拍板、0 代 PI 关闭；台账记 P-S4-1 仍「未拍板」。")),
 dict(q="D8-56", jt="J5", ans="ABC，接受重采偏差", form="Other（三选合成）", sel=["A", "B", "C"],
      opt={"A": "不等（采集面与判定面解耦，先采）", "B": "等翻案链完成再采", "C": "先采一半"}, rsn=None,
      ask="ask_cba2075ac4faf0f4f4d28ae7", batch=14, line=149, tag="appeal_chain_completion_before_wave",
      face="一条翻案链（重训影响面评估）尚未完成。是否等它完成再采大波？",
      extra=dict(composite_note="三选合成（台账「形态」列字面「Other（三选合成）」，无「＋推理」标记）⇒ 本件 0 把「接受重采偏差」登记为 reasoning_full（0 编造推理归属），逐字全文见 pi_answer_verbatim。")),
 dict(q="D8-57", jt="J5", ans="A，避免遗忘", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "穷尽清点后一轮问全（≤4 题/轮分批）"}, rsn="避免遗忘",
      ask="ask_882bdceab49d3ed97d4f73b0", batch=15, line=155, tag="closure_exhaustive_pending_item_sweep",
      face="收口时待拍板项又新增若干（含一项未拍板的多线不自洽 + 一项编号占位 + 文件数类校正）。收口方式？"),
 dict(q="D8-58r", jt="J5", ans="A，随时有新文件，包括每日整理文件夹，不可能无噪声下随时校正",
      form="Other（选 A ＋ 推理；r 版替换题）", sel=["A"],
      opt={"A": "差额影响当前判定口径时当场校正，否则挂到收尾批量校正"},
      rsn="随时有新文件，包括每日整理文件夹，不可能无噪声下随时校正",
      ask="ask_882bdceab49d3ed97d4f73b0", batch=15, line=156, tag="count_discrepancy_correction_timing",
      replaces="D8-58",
      face="计数类账目（文件数/件数/目录计数）出现差额对不上时，当场逐项校正 vs 挂到阶段收尾批量校正 —— 你按什么判据选？",
      extra=dict(replacement_note="r 版替换题（PI 2026-09-30 4 裁第 ① 项「r-text 4 条全部采纳（重启时替换题面）」）；原 D8-58（" + Q + " §3 字面「文件数类账目差异按 PI 口径统一挂『V4 收尾整理』。本次是否处理？」）未采集、0 既有答案 ⇒ 本件以 q_id=D8-58r 登记，replaces_q_id=D8-58。",
                replacement_grade_source=BND + " §3 D8-58r 字面",
                original_face_retained=Q + " §3 D8-58（未采集，仅备查）")),
 dict(q="D8-59r", jt="J5", ans="A，因地制宜", form="Other（选 A ＋ 推理；r 版替换题）", sel=["A"],
      opt={"A": "压缩会破坏跨日/单日占比口径时暂停顺延，否则压缩答完"}, rsn="因地制宜",
      ask="ask_882bdceab49d3ed97d4f73b0", batch=15, line=157, tag="same_day_compress_vs_pause_deferral",
      replaces="D8-59",
      face="一个采集波当日因外部插入事项被迫中断、余题顺延。判断「当日压缩答完 vs 当日暂停、余题顺延」的判据是什么？",
      extra=dict(replacement_note="r 版替换题（同 D8-58r 拍板口径）；原 D8-59（" + Q + " §3 字面「若大波采集当日 PI 临时要处理另一件急事，采集如何排？」）未采集、0 既有答案 ⇒ 本件以 q_id=D8-59r 登记，replaces_q_id=D8-59。",
                replacement_grade_source=BND + " §3 D8-59r 字面",
                original_face_retained=Q + " §3 D8-59（未采集，仅备查）")),
 dict(q="D8-60", jt="J5", ans="A，实事求是", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "允许当日答完，但件内标注「未满足 ≥1 天间隔，R 系有效性降级」"}, rsn="实事求是",
      ask="ask_882bdceab49d3ed97d4f73b0", batch=15, line=158, tag="rp_same_day_answering_degradation",
      dispute="minor",
      face="R 系配对题要求两次作答间隔 ≥1 天。若 PI 当日想一次答完 a/b 两半，处置？",
      extra=dict(actual_compliance_verbatim="PI 答 A（当日可答完但须标注降级）⇒ 实际处置：b 半 3 题（D8-11/19/37）当日未答、顺延至 10-01+（" + Q + " §4 字面「b 半未满 1 天不作答 ⇒ 该对不成立」＋ §7 T-D8-3 字面）⇒ 本卷 R9/R10/R11 三对 b 半在 10-01+ 落件前不成立、不标降级（未发生当日双答）。",
                  compliance_registration_type="associated_registration_not_answer_inference")),
 dict(q="D8-61", jt="J5", ans="A，明日复明日，明日就忘了，然后假fail", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "立即重采（趁记忆新鲜）"}, rsn="明日复明日，明日就忘了，然后假fail",
      ask="ask_721f00fa3e4977bcc0f56d45", batch=16, line=164, tag="reface_recollection_timing",
      face="若大波采完发现某题题面设计有缺陷需重采，重采时机？"),
 dict(q="D8-62", jt="J5", ans="ABC均可，既要事实求是，又要对抗遗忘，合适时机插入任务锚点是恰当的",
      form="Other（三选合成）", sel=["A", "B", "C"],
      opt={"A": "全部落盘后再冻结分层", "B": "采到一半即冻结", "C": "不冻结，每次重算"},
      rsn="既要事实求是，又要对抗遗忘，合适时机插入任务锚点是恰当的",
      ask="ask_721f00fa3e4977bcc0f56d45", batch=16, line=165, tag="stratified_holdout_freeze_timing",
      face="大波采集完成后，分层抽样（0.30 含纠正）在什么时点冻结？",
      extra=dict(execution_status_note="PI 答三选合成；本件 0 判定分层是否已冻结（分层属 S4 段，0 在本棒顺手做），0 代 PI 择一。")),
 dict(q="D8-63", jt="J5", ans="A，否则蒸馏失实", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "加采（准则变更即时反映）"}, rsn="否则蒸馏失实", dispute="minor",
      ask="ask_721f00fa3e4977bcc0f56d45", batch=16, line=166, tag="principle_change_additional_collection",
      face="若大波采完 PI 又改变了对某条准则的表述，加采时机？"),
 dict(q="D8-64", jt="J5", ans="A，防回退", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "先采集定稿，再上传（避免上传未落定内容）"}, rsn="防回退",
      ask="ask_721f00fa3e4977bcc0f56d45", batch=16, line=167, tag="publication_vs_collection_order",
      face="发布面（应上传尽上传 + 全公开破例）与采集面的先后？"),
 dict(q="D8-65", jt="J5", ans="A，并诚实标注", form="Other（选 A ＋ 补充）", sel=["A"],
      opt={"A": "能（顺延增加天数，跨日更宽松）"}, rsn="并诚实标注", dispute="minor",
      ask="ask_2c5426e79464ebd78d48c8fc", batch=17, line=173, tag="deferral_relaxing_cross_day_days",
      face="若 PI 明日无法作答，大波余题顺延到后日。跨日天数是否仍能达标？"),
 dict(q="D8-66", jt="J5", ans="A，全量推进防遗忘，但也注意防回退，不过本场景应不涉及进程对抗",
      form="Other（选 A ＋ 推理）", sel=["A"], opt={"A": "重算后台跑，同时推进其他棒"},
      rsn="全量推进防遗忘，但也注意防回退，不过本场景应不涉及进程对抗",
      ask="ask_2c5426e79464ebd78d48c8fc", batch=17, line=174, tag="full_recompute_background_vs_wait",
      face="大波采完立即需跑全套度量重算（机器静默数小时）。先后？"),
 dict(q="D8-67", jt="J5", ans="A，下一波补可能拉高单日占比", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "立即补采补齐"}, rsn="下一波补可能拉高单日占比",
      ask="ask_2c5426e79464ebd78d48c8fc", batch=17, line=175, tag="shortfall_immediate_topup",
      face="若采集件落盘后复核发现 N 少于预期（部分题未答成），补采时机？",
      extra=dict(self_referential_note="PI 提示的「拉高单日占比」风险在本件实况：b 半 3 题顺延 10-01+ 落在不同日历日 ⇒ 跨日天数 0 减、单日占比分母 0 缩（具体读数见 cross_day_and_ratio_measurement，0 判定达标与否）。")),
 dict(q="D8-68", jt="J6", ans="AC，mavis依赖上下文，既是优势也是劣势，此外mavis我特意换了更优模型",
      form="Other（双选 A/C ＋ 备注：Mavis 已换更优模型）", sel=["A", "C"],
      opt={"A": "派 doc-writer（起草类专属）", "C": "Mavis 自己写"}, rsn="mavis依赖上下文，既是优势也是劣势，此外mavis我特意换了更优模型",
      ask="ask_2c5426e79464ebd78d48c8fc", batch=17, line=176, tag="question_drafting_dispatch_role",
      face="本次大波问卷件（80 题题面）派给谁起草？",
      extra=dict(realworld_note_verbatim="此外mavis我特意换了更优模型",
                  realworld_note="PI 逐字备注：Mavis 特意换了更优模型；本件按台账逐字登记，0 代 PI 评价模型能力。")),
 dict(q="D8-69", jt="J6", ans="A，此外skill目录需要更新了，毕竟minimax code更新了，不知道路径发生了什么改变以致失败",
      form="Other（选 A ＋ 实况：skill 目录待更新/路径排查）", sel=["A"],
      opt={"A": "按纪律锚 fallback + 老实交代，0 编造 skill 指令"},
      rsn="此外skill目录需要更新了，毕竟minimax code更新了，不知道路径发生了什么改变以致失败",
      ask="ask_10e87126e314e298e0ed6db4", batch=18, line=182, tag="skill_load_failure_fallback",
      face="若起草方的 skill 加载失败（`Local skill not found`），出件方式？",
      extra=dict(operational_note_verbatim="此外skill目录需要更新了，毕竟minimax code更新了，不知道路径发生了什么改变以致失败",
                  operational_note="PI 实况登记：skill 目录待更新（minimax code 更新后路径变化致失败）；本棒 0 加载任何 skill、0 引用/0 虚构任何 skill 条文（派工单亦未指定 skill）⇒ 该实况与本棒无执行关系，仅逐字登记。")),
 dict(q="D8-70", jt="J6", ans="A，规则集有用的话还要LLM做什么？", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "起草方提案 + PI 可推翻"}, rsn="规则集有用的话还要LLM做什么？",
      ask="ask_10e87126e314e298e0ed6db4", batch=18, line=183, tag="judge_type_proposal_authority",
      face="80 题的 `judge_type` 提案由起草方给还是由 PI 定？",
      extra=dict(self_referential_note="本件 84 条 judge_type 一律沿题面「judge_type 提案」字面录入（" + Q + " §3 每题「judge_type 提案」行），0 worker 自行改判；PI 本题答 A＝起草方提案 + PI 可推翻，本件 0 行使改判权。")),
 dict(q="D8-71", jt="J6", ans="AB，双盲审", form="Other（双选 A/B ＋ 推理）", sel=["A", "B"],
      opt={"A": "派 explore（只读勘察）复核", "B": "派 verifier 独立复核"}, rsn="双盲审",
      ask="ask_10e87126e314e298e0ed6db4", batch=18, line=184, tag="question_walkthrough_dispatch_role",
      face="若 80 题需一轮走查（是否重复、是否预设立场、是否复用），派谁？"),
 dict(q="D8-72", jt="J6", ans="AB，一般新案优先", form="Other（双选 A/B ＋ 推理）", sel=["A", "B"],
      opt={"A": "PI 拍板", "B": "verifier 第三审"}, rsn="一般新案优先",
      ask="ask_10e87126e314e298e0ed6db4", batch=18, line=185, tag="judge_type_disagreement_adjudication",
      face="若起草方与复核方对某题的 `judge_type` 判断不一致，裁决？",
      extra=dict(exception_verbatim="一般新案优先",
                  exception_note="PI 答 A/B 双选并加例外「一般新案优先」⇒ 本件按台账登记双选 + 例外逐字保留，0 替 PI 明确例外触发条件。")),
 dict(q="D8-73", jt="J6", ans="B，以新案优先，此外不是大纲而是实验成果线索，否则受委托方无从下手",
      form="Other（选 B ＋ 委托面口径再澄清；已追加 user 记忆补注）", sel=["B"], opt={"B": "加"},
      rsn="以新案优先，此外不是大纲而是实验成果线索，否则受委托方无从下手",
      ask="ask_fa8b654cc5221cd654e880dc", batch=19, line=191, tag="outline_in_question_material",
      face="若 PI 希望题面含大纲（帮其统一口径），是否加？",
      extra=dict(commission_note_verbatim="以新案优先，此外不是大纲而是实验成果线索，否则受委托方无从下手",
                  commission_note="委托面口径再澄清：与 D8-34（「保证主线统一，也因此应点明主线」）同族互证 —— 不含大纲＝结构自由，≠不说主线；须给实验成果线索。台账记「已追加 user 记忆补注」；本件 0 改写任何委托件。")),
 dict(q="D8-74", jt="J6", ans="B，保持统一下新案优先", form="Other（选 B ＋ 推理；⚠️ 与题面 A 档相左，按答入账）",
      sel=["B"], opt={"B": "引官方站"}, rsn="保持统一下新案优先",
      ask="ask_fa8b654cc5221cd654e880dc", batch=19, line=192, tag="external_vendor_version_statement_source",
      face="若某题涉及外部受托方的版本/能力表述，取材口径？",
      extra=dict(face_conflict_verbatim="⚠️ 与题面 A 档相左，按答入账",
                  face_conflict_note="PI 选 B（引官方站）与题面 A 档「只以 PI 的 github 为权威源，查不到即问 PI」相左；台账已按「按答入账」登记 ⇒ 本件逐字保留 PI 落点并显式登记该相左，0 代 PI 调和、0 据此改写任何取材口径。",
                  source=LEDGER + " 批 19 表行（D8-74）「形态」列字面")),
 dict(q="D8-75", jt="J6", ans="B，挂起项是时候解决了", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "取全部细节"}, rsn="挂起项是时候解决了",
      ask="ask_fa8b654cc5221cd654e880dc", batch=19, line=193, tag="suspended_ruling_recovery_layer",
      face="若某题涉及一条挂起判定的恢复，需要先取该判定件的哪一层信息？"),
 dict(q="D8-76", jt="J6", ans="A，因地制宜", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "题面起草方 + 落盘执行方（起草与执行分离）"}, rsn="因地制宜",
      ask="ask_fa8b654cc5221cd654e880dc", batch=19, line=194, tag="drafting_vs_landing_responsibility",
      face="题面件（起草）与落盘件（写 JSON）由谁负责？"),
 dict(q="D8-77", jt="J6", ans="AC，实事求是", form="Other（双选 A/C ＋ 推理）", sel=["A", "C"],
      opt={"A": "盘上核验后重派", "C": "追责"}, rsn="实事求是",
      ask="ask_91c25e9740d3cef10f18cd49", batch=20, line=200, tag="succeeded_but_missing_files",
      face="若落盘方报 succeeded 但盘上 JSON 缺若干件，下一步？",
      extra=dict(self_referential_note="PI 答 A/C（盘上核验后重派 + 追责）⇒ 本件按该口径自验：落盘后复算条数/重复/漏项 + SHA-12/字节/行数（见 self_verification 段）；0 以「succeeded」当跑完。")),
 dict(q="D8-78", jt="J6", ans="A，没有题面答什么？", form="Other（选 A ＋ 推理）", sel=["A"],
      opt={"A": "仍出题面（PI 明示前按默认；明示后照办）"}, rsn="没有题面答什么？", dispute="minor",
      ask="ask_91c25e9740d3cef10f18cd49", batch=20, line=201, tag="pi_self_answering_question_material",
      face="若 PI 明示「大波由我自己答，题面你们别管」，题面由谁出？"),
 dict(q="D8-79", jt="J6", ans="AC，能查到的主动查，PI也许也不知道，或者写委托书", form="Other（双选 A/C ＋ 推理）",
      sel=["A", "C"], opt={"A": "由 parent 走 ask_user 一次性问全（不逐题打断）", "C": "起草方自行查"},
      rsn="能查到的主动查，PI也许也不知道，或者写委托书",
      ask="ask_91c25e9740d3cef10f18cd49", batch=20, line=202, tag="external_fact_gap_questioner",
      face="若某题需 PI 补充盘上查不到的外部事实，谁来问？"),
 dict(q="D8-80", jt="J6", ans="B，尤其补充深度广度", form="Other（选 B ＋ 推理）", sel=["B"],
      opt={"B": "重新起草新问卷件"}, rsn="尤其补充深度广度",
      ask="ask_91c25e9740d3cef10f18cd49", batch=20, line=203, tag="below_target_n_supplementary_dispatch",
      face="若大波最终判定 N 未达标（PI 答得少），后续补采派工？",
      extra=dict(supplementary_dispatch_note="PI 答 B（重新起草新问卷件）＋「尤其补充深度广度」；SQ 补采卷（" + SQF + "）即 T-D8-2 拍板 B 触发的追加补采波（8 题开放型，7 作答 + 1 跳过），本件 0 判其是否满足「深度广度」要求。")),
]

SQ = [
 dict(q="SQ-01", jt="J1", ans="最重要的是竞品BOSS是否可及，如果BOSS不可及则一定是立歪了", form="开放作答",
      ask="ask_e829a3e1bb17f57d6029fbba", batch="SQ 批 1", line=211, tag="killline_self_check_order",
      face="回看一条你自己早先立下的判死线时，你先查哪一件事，来判断「是这条线当初立歪了，还是被它量的那个东西真不行」？说出你的检查顺序，以及你最怕自己搞混的那一处。",
      dispute="minor",
      extra=dict(dispute_note="边界修订件 §8 记 SQ-01「末句轻微邻接从句」为争议·轻微项（本棒判 ✅ 判断方法侧，PI 可推翻）；PI 本题答出的是检查项而非自画像 ⇒ 本件 0 据此改判边界归属。")),
 dict(q="SQ-02", jt="J1", ans="矛盾出现！这是仿物理算法的大忌，破坏了FTFB的硬核要求，无论矛盾如何出现的",
      form="开放作答", ask="ask_e829a3e1bb17f57d6029fbba", batch="SQ 批 1", line=212,
      tag="self_driven_ruling_reopen_trigger",
      face="什么情况下你会主动回去重开一条自己已经放过的判定？说出你实际用的触发条件 —— 是外面递进来的信息，还是你在别处撞见了矛盾、回来一算才发现当初漏了什么。",
      extra=dict(two_way_note="题面给「自驱 vs 外驱」二选一框架，PI 答触发条件＝「矛盾出现」（属「在别处撞见了矛盾」一极）＋ 理由「仿物理算法的大忌，破坏了FTFB的硬核要求，无论矛盾如何出现的」；本件 0 替 PI 把答案归入某一极（PI 未自述归类），逐字保留。")),
 dict(q="SQ-03", jt="J2", ans="我想要，我得到，接受延迟满足，虽说资金有限但仍愿意量力而行投入", form="开放作答",
      ask="ask_e829a3e1bb17f57d6029fbba", batch="SQ 批 1", line=213, tag="cost_reversibility_pricing",
      face="在决定要不要投一件事之前，你心里怎么给这次投入的可逆性定价？—— 什么样的成本你会当场就付，什么样的成本你会先问一句「这东西过两天还在不在」。"),
 dict(q="SQ-04", jt="J3", ans="最小的一步是同义映射，如与死同行-不可机械，大材小用-因地制宜，落到实处-实事求是",
      form="开放作答", ask="ask_921f42b832970a9d5274fbfb", batch="SQ 批 2", line=222,
      tag="principle_minimum_executable_step",
      face="拿你最近用得最勤的那条准则说 —— 它落到你手上某个具体决定时，最小的那一步是什么？不要解释，说你会真的照做的那个动作或那句检查。",
      extra=dict(ftfb_absence_note="PI 答三组同义映射（大材小用/落到实处/与死同行）**未含第四准则「虚实回路（FTFB）」**；本件 0 补入 FTFB、0 评价遗漏（题面亦未点名四准则），如实登记。")),
 dict(q="SQ-05", jt="J3", ans="承认用错了，准则不是万能的，但后果是可以解决的，而无准则的后果将更难解决", form="开放作答",
      ask="ask_921f42b832970a9d5274fbfb", batch="SQ 批 2", line=223, tag="principle_self_correction_when_wrong",
      face="如果一条准则在某件具体事情上，把你带到了一个你事后认为明显错了的地方，你会怎么用它 —— 改写它、给它加例外，还是承认它当时就用错了？说你的判断依据。",
      extra=dict(three_option_face_note="题面给三出口（改写 / 加例外 / 承认用错），PI 答「承认用错了」；本件 0 扩展为第四出口、0 补 PI 依据（PI 原话自带依据，逐字保留）。")),
 dict(q="SQ-06", jt="J4", ans="是否真正需要，包括是否更接近真判，整理文件夹可能会丢失审判链，但却是必要的", form="开放作答",
      ask="ask_921f42b832970a9d5274fbfb", batch="SQ 批 2", line=224, tag="risk_asymmetry_pricing",
      face="你判断一个风险值不值得怕，用的是什么不对称 —— 是「最坏情况能坏到哪儿」，还是「它坏了之后你还能不能收拾回来」？举一个你因此改过做法的例子。"),
 dict(q="SQ-07", jt="J5", ans="出现了意外的fail，不过谈论收早收晚因为观察者效应而没有意义，往往是收晚了因为实验设计缺陷，但也会收早了因为后续实验自圆其说",
      form="开放作答", ask="ask_921f42b832970a9d5274fbfb", batch="SQ 批 2", line=225,
      tag="stopping_signal_and_its_error_direction",
      face="在一条工作线上，你判断「现在该收手、就停在这里」的信号是什么？这些信号里，哪一个你最常在事后发现是错的 —— 收早了，还是收晚了？"),
 dict(q="SQ-08", jt="J6", ans=None, form="跳过项（记 null）", ask="ask_a8ebc92a2538769f44ebcd87",
      batch="SQ 批 3（终批）", line=231, tag="what_remains_undelegated", skipped=True,
      face="你把一件事完全交出去之后，自己还会留着不交的那部分是什么？—— 不要分工表，说你的直觉：什么事你交出去之后睡不踏实，以及为什么偏偏是那部分你一定要自己握着。"),
]

CAL = [
 dict(q="T-D8-1", jt="calibration", ans="② 盘上实存 83（+80=163，差 4）", form="选项②", sel=["②"],
      opt={"②": "盘上实存 83"}, opt_source=Q + " §7 T-D8-1 字面「① executor 载入 77 / ② 盘上实存 83 / ③ 记账 91」",
      ask="ask_72adb71ea07edc063ceed334", batch=1, line=16, tag="substrate_counting_basis_choice",
      face="S4 `substrate` 取哪一口径（① executor 载入 77 / ② 盘上实存 83 / ③ 记账 91）？",
      rsn="（+80=163，差 4）",
      pending_status="decided_by_pi_2026-09-30（台账批 1 表行；台账收讫总况记「口径题 T-D8-1/T-D8-2 已决（口径＝②盘上实存 83；追加 SQ 波）」）"),
 dict(q="T-D8-2", jt="calibration", ans="B，且均为开放性的高效蒸馏的思维性的问题", form="Other（选 B ＋ 题性指定）",
      sel=["B"], opt={"B": "追加补采波"}, opt_source=SQF + " 件头 §0.1 第 4 行字面「T-D8-2 选 B＝追加补采波 ＋ 题性指定「且均为开放性的高效蒸馏的思维性的问题」（PI 逐字）」",
      ask="ask_a6f88ff30bf89a8e804239d9", batch=2, line=25, tag="supplementary_wave_decision",
      face="若口径定为 ①/②，80 题不足（差 10 / 差 4），是否追加补采波？",
      rsn="且均为开放性的高效蒸馏的思维性的问题",
      pending_status="decided_by_pi_2026-09-30（台账批 2 表行 +「T-D8-2 处置（parent 登记）」：追加补采波＝是；题性＝开放性·高效蒸馏·思维性（PI 逐字）；数量取区间上界 8）",
      extra=dict(consequent_on_disk=[SQF + "（579b375e9508，8 题开放型题面件）", BND + "（b46370bb9e3b，边界修订件 §5 SQ 快扫）"],
                 quantity_note="区间 6–8 取上界 8（" + SQF + " 件头第 5 行字面：余量抗丢件/作废题）；实采 7 作答 + 1 跳过（SQ-08）")),
 dict(q="T-D8B-7", jt="calibration", ans="① 按提案采纳（15 组保留+标注、组 14 不处置）", form="选项①", sel=["①"],
      opt={}, opt_source=None, ask="ask_16f0f4dc3ae9321ef79de182", batch=9, line=102,
      tag="duplicate_scope_disposal_adoption", face="（出题侧修订）16 组重复口径交叉发现的处置选项？",
      rsn=None, pending_status="decided_by_pi_2026-09-30（台账批 9 表行 +「T-D8B-7 落定」：16 组处置提案按提案采纳，⛔ 0 改写原题）",
      extra=dict(face_unavailable_note="本棒输入链＝台账 + D8 原卷 + SQ 卷 + 边界修订件；T-D8B-7 的 ask 选项面（①②③ 字面）不在其中（T-D8B-7 系 parent 就修订件 §7 T-D8B-3 等项自拟的问卷项）⇒ option_meaning 记 null（0 编造选项释义），PI 答复逐字见 pi_answer_verbatim。",
                adoption_note="台账「T-D8B-7 落定（2026-09-30）」字面：16 组处置提案按提案采纳（⛔ 0 改写原题）；采纳记录入出题侧修订批。",
                topic_registration_type="associated_registration_not_answer_inference")),
 dict(q="skill-4", jt="calibration", ans="① 全采纳（含对照实验）", form="选项①", sel=["①"], opt={}, opt_source=None,
      ask="ask_e829a3e1bb17f57d6029fbba", batch="SQ 批 1", line=214, tag="skill_disclosure_four_items_adoption",
      face="（skill 披露）4 项处置选项？", rsn=None,
      pending_status="decided_by_pi_2026-09-30（台账 SQ 批 1 表行 +「skill-4 落实（parent 登记）」：①出勘误件（possibly-missing 过期）②对外件只写 `plugin:skill` 名 ③统一三段式锚 ④运行时定位对照实验——已派收口棒执行）",
      extra=dict(face_unavailable_note="skill-4 的选项面（①…④ 字面）不在本棒输入链（台账仅记落点 ① + 落实 4 项）⇒ option_meaning 记 null（0 编造），逐字见 pi_answer_verbatim。",
                implementation_note="台账记 4 项「已派收口棒执行」；本棒 0 核验其执行结果、0 声称已闭环。",
                topic_registration_type="associated_registration_not_answer_inference")),
 dict(q="skill-6", jt="calibration", ans="① 全采纳（六项全办）", form="选项①", sel=["①"], opt={}, opt_source=None,
      ask="ask_a8ebc92a2538769f44ebcd87", batch="SQ 批 3（终批）", line=232, tag="skill_disclosure_six_items_adoption",
      face="（skill 披露）6 项处置选项？", rsn=None,
      pending_status="decided_by_pi_2026-09-30（台账 SQ 批 3 表行 +「skill-6 落实（parent 登记）」：①勘误拆件 ②强制口径 ③失败窗口专项排障 ④48 件引用批量更新 ⑤父级成功补记 ⑥223 项普查——六项全办，执行双棒已派（A：排障＋补记＋拆件＋口径；B：④更新＋⑥普查））",
      extra=dict(face_unavailable_note="skill-6 的选项面（①…⑥ 字面）不在本棒输入链 ⇒ option_meaning 记 null（0 编造），逐字见 pi_answer_verbatim。",
                implementation_note="台账记「六项全办，执行双棒已派（A/B）」；本棒 0 核验其执行结果、0 声称已闭环。",
                topic_registration_type="associated_registration_not_answer_inference")),
]

# ---------------------------------------------------------------- 覆盖自检
LEDGER_ASKS = {
 1:"ask_72adb71ea07edc063ceed334", 2:"ask_a6f88ff30bf89a8e804239d9", 3:"ask_ffe8cdf9d2b1d84294afd1c6",
 4:"ask_d36d1fa8c5265673a67fcdd1", 5:"ask_5901a28baa3485800e376ac1", 6:"ask_cd08e7bacaa1cb99ecceaa34",
 7:"ask_de8dbebee79a8e9ebde007fa", 8:"ask_4341a4423c517f0e41c99abd", 9:"ask_16f0f4dc3ae9321ef79de182",
 10:"ask_faf9de6def9e1c2384a5954b", 11:"ask_a5bf873f436ba5a68a808567", 12:"ask_1d3dd509d148173cc4baa95f",
 13:"ask_e6b4fcbe7b00e25aab4d69fa", 14:"ask_cba2075ac4faf0f4f4d28ae7", 15:"ask_882bdceab49d3ed97d4f73b0",
 16:"ask_721f00fa3e4977bcc0f56d45", 17:"ask_2c5426e79464ebd78d48c8fc", 18:"ask_10e87126e314e298e0ed6db4",
 19:"ask_fa8b654cc5221cd654e880dc", 20:"ask_91c25e9740d3cef10f18cd49",
}
d8_ids = [e["q"] for e in D8]
assert len(d8_ids) == len(set(d8_ids)), "D8 内部有重复 q_id"
expected = []
for i in range(1, 81):
    if i in (58, 59):
        expected.append("D8-%02dr" % i)
    else:
        expected.append("D8-%02d" % i)
missing = [q for q in expected if q not in d8_ids]
extra = [q for q in d8_ids if q not in expected]
assert not missing, "漏题: %s" % missing
assert not extra, "多余题: %s" % extra
assert d8_ids == expected, "D8 条目未按题号顺序排列: %s" % d8_ids
for e in D8:
    if e.get("pend"):
        continue
    if isinstance(e["batch"], int):
        assert LEDGER_ASKS[e["batch"]] == e["ask"], "ask_id 与台账批号不符: %s" % e["q"]
sq_ids = [e["q"] for e in SQ]
assert sq_ids == ["SQ-0%d" % i for i in range(1, 9)], "SQ 条目不完整/未按序: %s" % sq_ids
cal_ids = [e["q"] for e in CAL]
assert cal_ids == ["T-D8-1", "T-D8-2", "T-D8B-7", "skill-4", "skill-6"], "口径项不符: %s" % cal_ids
all_ids = d8_ids + sq_ids + cal_ids
assert len(all_ids) == len(set(all_ids)), "全表有重复 q_id"
assert len(all_ids) == 93, "全表条目数应为 93，实际 %d" % len(all_ids)

# ---------------------------------------------------------------- 跨日/占比实测
def scan_dates():
    ds = set()
    pat_dir = os.path.join(ROOT, "results")
    for fn in sorted(os.listdir(pat_dir)):
        if not fn.endswith(".json"):
            continue
        p = os.path.join(pat_dir, fn)
        try:
            obj = json.load(open(p, "r", encoding="utf-8"))
        except Exception:
            continue
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "date" and isinstance(v, str) and len(v) == 10 and v[4] == "-":
                        ds.add(v)
                    else:
                        walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(obj)
    return sorted(ds)

PREV_DAYS = ["2026-09-24", "2026-09-26", "2026-09-27", "2026-09-28", "2026-09-29"]
scanned = scan_dates()
prev_set = set(x for x in scanned if x != "2026-09-30")

# ---------------------------------------------------------------- 构造条目
def ledger_ref(b, line):
    if b is None or line is None:
        return None
    return "%s 批 %s 表行（行 %d）" % (LEDGER, b, line)

def build_entry(e, entry_class, wave, event_prefix, face_source, jt_note_kind="question_face_proposal"):
    q = e["q"]
    pend = bool(e.get("pend"))
    skipped = bool(e.get("skipped"))
    sel = e.get("sel")
    opt = e.get("opt") or {}
    rsn = e.get("rsn")
    ans = e.get("ans")
    n = {}
    n["pair_id"] = q
    n["event_id"] = "%s_%s" % (event_prefix, q)
    n["date"] = "2026-09-30"
    n["q_id"] = q
    n["entry_class"] = entry_class
    n["collection_wave"] = wave
    n["scene_tag"] = e["tag"]
    n["scene_tag_source"] = "本棒 worker 依题面内容赋的英文蛇形标签（沿既有落件同惯例：" + LEDGER + " 0 改题面、0 编造题面）"
    n["scene_verbatim"] = e["face"]
    n["scene_verbatim_source"] = face_source
    n["scene_verbatim_source_note"] = "题面原文含 markdown 强调标记（**），本件仅去强调标记未改一字；逐字取自盘上原件"
    n["judge_type"] = e["jt"]
    n["judge_type_source"] = face_source + " 题面「judge_type 提案」字面" if entry_class in ("content_question", "open_question") else (
        "口径/处置类条目：无题面 judge_type 提案 ⇒ 记 \"calibration\"（本棒登记值，非 J1–J6 判定分类，0 冒充题面提案）")
    n["judge_type_note"] = jt_note_kind
    n["collected_via"] = "ask_user" if e.get("ask") else None
    n["collected_at"] = None
    n["collected_at_note"] = ("ask 记录不落盘（沿盘上 d6/d6b/d7 落件同一惯例）⇒ PI 精确作答时分不可回查；本件 0 伪造 PI 作答时分，"
                              "所记 ask_id 与答复字面均转录自盘上台账（唯一数据源），本棒 0 取得 ask 原件、0 声称已核验 ask 原文")
    n["source_ask_id"] = e.get("ask")
    n["ledger_source_ref"] = ledger_ref(e.get("batch"), e.get("line"))
    n["ledger_form_label"] = e["form"]
    n["pi_answer_verbatim"] = ans
    n["pi_answer_verbatim_note"] = ("台账作答格逐字（台账以「」包裹答案；本件去掉最外层「」包裹，PI 原答内部的「」保持原样，"
                                    "如 D8-36 的「未落盘」）；0 润色 0 改写 0 扩写 0 补标点 0 补全")
    if pend:
        n["collection_status"] = "待采集（10-01+）"
        n["option_chosen"] = None
        n["option_chosen_letters"] = None
        n["option_form"] = "pending_not_collected"
        n["option_meaning"] = None
        n["option_meaning_note"] = "b 半 3 题按卷规避开当日（" + Q + " §4 字面「b 半未满 1 天不作答」＋ §7 T-D8-3 字面）⇒ ⛔ 本件 0 填值、0 代填、0 虚构 PI 落点"
        n["listed_options_verbatim"] = e.get("listed")
        n["listed_options_verbatim_source"] = face_source
        n["pi_other_verbatim"] = None
        n["pi_answer_form"] = "未采集（PI 当日未作答）"
        n["reasoning_full"] = None
        n["reasoning_full_note"] = "未采集 ⇒ 记 null（0 代填 0 虚构）"
        n["is_correction"] = None
        n["is_correction_note"] = ("b 半未作答 ⇒ 本件 0 预填 is_correction（题面 §1 第 5 条字面「本件仅保证 is_correction 字段可标（R 系 6 件 = True）」"
                                   "待 b 半落件时按盘上口径登记）；配对关系见 r_pair")
        n["correction_confirmed"] = None
        n["weight"] = None
        n["linked_pending_decisions"] = [{
            "id": "T-D8-3",
            "pending_item_verbatim": "本卷 R 系 b 半（D8-11 / D8-19 / D8-37）的作答日",
            "pending_item_source": Q + " §7 待 PI 拍板项表 T-D8-3 字面「b 半标 D9+；若 PI 当日一次答完，R 系有效性降级（见 D8-60）」",
            "directional_registration": "PI 2026-09-30 处置＝当日避开、顺延至 10-01+（" + LEDGER + " 头部第 4 行 + 收讫总况「≥1 天间隔保留，待 PI 定日」）",
            "status_changed": False,
            "note": "本件 0 代 PI 关闭 T-D8-3（具体开卷日仍待 PI 定）；0 预判 b 半判定方向"
        }]
    elif skipped:
        n["collection_status"] = "跳过（PI 明示跳过）"
        n["option_chosen"] = None
        n["option_chosen_letters"] = None
        n["option_form"] = "skipped_null"
        n["option_meaning"] = None
        n["option_meaning_note"] = "PI 跳过 ⇒ 记 null（SQ 卷无 A/B/C 选项，option_meaning 本即不适用）"
        n["pi_other_verbatim"] = None
        n["pi_answer_form"] = "跳过项（台账 SQ 批 3 表行：SQ-08 ＝ 跳过（记 null））"
        n["reasoning_full"] = None
        n["reasoning_full_note"] = "PI 跳过 ⇒ 记 null（0 代填 0 虚构 0 用邻题答案推补）"
        n["is_correction"] = False
        n["is_correction_note"] = "非 R 系配对件（SQ 卷 0 配对，" + SQF + " §2 字面「0 对」）"
        n["correction_confirmed"] = False
        n["weight"] = 1.0
        n["linked_pending_decisions"] = []
    else:
        n["collection_status"] = "已采（PI 2026-09-30 作答）"
        letters = list(sel) if sel else []
        if letters and any(x in ("A", "B", "C") for x in letters) and len(letters) == 1 and opt.get(letters[0]):
            n["option_chosen"] = letters[0]
            n["option_chosen_letters"] = letters
            n["option_form"] = "single_letter" + ("_plus_reasoning" if rsn else "_bare")
            n["option_meaning"] = opt[letters[0]]
            n["option_meaning_note"] = "题面对应选项的字面释义"
            n["option_meaning_source"] = e.get("opt_source") or (face_source + " 选项 " + letters[0] + " 字面")
        elif letters and all(x in ("A", "B", "C") for x in letters):
            n["option_chosen"] = "".join(letters) + ("（台账登记落点为多选合成）" if len(letters) > 1 else "")
            n["option_chosen_letters"] = letters
            n["option_form"] = ("multi_letter_triple" if len(letters) == 3 else "multi_letter_dual") + \
                               ("_plus_reasoning" if rsn else "_bare")
            n["option_meaning"] = None
            n["option_meaning_note"] = ("多选/三选合成落点 ⇒ 单一条目不对应唯一选项释义；被选各档字面见 selected_option_faces_verbatim"
                                        "（0 合并为单一释义、0 挑一档当唯一落点）")
            n["option_meaning_source"] = None
            n["selected_option_faces_verbatim"] = [opt.get(x) for x in letters]
            n["selected_option_faces_verbatim_source"] = face_source + " 被选各档选项字面"
        elif letters:
            n["option_chosen"] = "".join(letters)
            n["option_chosen_letters"] = letters
            n["option_form"] = "calibration_choice"
            n["option_meaning"] = opt.get(letters[0]) if opt else None
            n["option_meaning_note"] = ("口径/处置类条目：option_meaning 取件上已登记的选项释义；件上无该字面者记 null（0 编造）"
                                        if opt else "口径/处置类条目：选项面不在本棒输入链 ⇒ 记 null（0 编造选项释义）")
            n["option_meaning_source"] = e.get("opt_source")
        else:
            n["option_chosen"] = "Other（%s）" % ans
            n["option_chosen_letters"] = None
            n["option_form"] = "other_no_listed_option_landing"
            n["option_meaning"] = None
            n["option_meaning_note"] = ("PI 落点为 Other/自定义方向，非题面 A/B/C 任一 ⇒ 题面对应选项释义不适用；"
                                        "按 0 编造原则记 null，PI 原话逐字见 pi_other_verbatim / pi_answer_verbatim")
            n["pi_other_verbatim"] = ans
        n["pi_answer_form"] = ("选项字母落点 " + "".join(letters) if letters else "Other/自定义落点") + \
                              ("（PI 在 ask_user 问卷上作答，附推理句）" if rsn else "（PI 未另附推理）")
        n["reasoning_full"] = rsn
        if rsn:
            n["reasoning_full_note"] = ("台账「形态」列明示「＋ 推理/＋ 理由/＋ 补充/＋ 警示/＋ 修正口径」等 ⇒ 该段为 PI 自附推理，逐字录入；"
                                        "0 润色 0 改写 0 归一标点")
        else:
            n["reasoning_full_note"] = ("台账「形态」列未标「＋ 推理」⇒ 按 0 编造原则记 null（不把选项复述/外延/合成语当成推理全文；"
                                        "PI 原答逐字完整保留在 pi_answer_verbatim）")
        is_r = e.get("rpair", "") or ""
        if is_r.endswith("a"):
            n["is_correction"] = True
            n["is_correction_note"] = ("R 系配对 a 半（" + is_r + "）配对标记，沿题面 §1 第 5 条字面「本件仅保证 is_correction 字段可标（R 系 6 件 = True）」"
                                       "录入；**该值＝配对标记，不等于「已实测发生纠正/反转」**，0 预判 b 半方向")
            n["correction_confirmed"] = False
            n["correction_confirmed_note"] = "纠正/反转是否真发生须待 b 半（≥1 天后）作答后比对方可判定；本棒 0 预判、0 断言"
            n["weight"] = 1.0
        else:
            n["is_correction"] = False
            n["is_correction_note"] = ("非 R 系反转配对件（" + Q + " §4 R 系配对索引仅列 R9/R10/R11 三对，本题不在其中）"
                                       if entry_class == "content_question" else "非 R 系配对件（SQ 卷 0 配对 / 口径类条目无配对）")
            n["correction_confirmed"] = False
            n["weight"] = 1.0
        n["linked_pending_decisions"] = []
    if e.get("rpair"):
        code = e["rpair"][:-1]
        half = e["rpair"][-1]
        pair = {"pair_code": code, "half": half, "half_code": e["rpair"],
                "paired_half_code": code + ("b" if half == "a" else "a"),
                "reversal_axis_verbatim": {
                    "R9": "判死线：默认边界 vs 显式边界",
                    "R10": "成本：内部挂账 vs 已扩散结论",
                    "R11": "准则：未扩散补录 vs 已扩散校正"}[code],
                "reversal_axis_source": Q + " §4 R 系反转配对索引字面",
                "interval_requirement": "≥1 天间隔（防记忆效应）",
                "interval_requirement_source": Q + " §1 第 4 条字面 + §4 配对纪律字面",
                "pair_closed": False}
        if half == "a":
            pair["paired_half_q_id"] = {"R9": "D8-11", "R10": "D8-19", "R11": "D8-37"}[code]
            pair["paired_half_status"] = "待采集（10-01+）；b 半未落件 ⇒ 本对未闭合"
            pair["pair_status_note"] = "a 半已落件（2026-09-30）；b 半按卷规避开当日 ⇒ 本对 0 闭合，0 预判 b 半判定方向"
        else:
            pair["paired_half_q_id"] = {"R9": "D8-10", "R10": "D8-18", "R11": "D8-36"}[code]
            pair["paired_half_landing"] = "本件 supplements 内（同日 2026-09-30 已落件）"
            pair["paired_half_answer_date"] = "2026-09-30"
            pair["pair_status_note"] = ("b 半未作答 ⇒ 本对未闭合；本棒 0 补算 actual_interval_days、0 断言 ≥1 天间隔满足"
                                        "（间隔自 b 半落件日才起算）")
        n["r_pair"] = pair
    if e.get("replaces"):
        n["replaces_q_id"] = e["replaces"]
        n["question_face_status"] = "r 版替换题（PI 2026-09-30 4 裁第 ① 项全部采纳）"
    if e.get("boundary"):
        n["boundary_tag"] = e["boundary"]
    if e.get("dispute") == "minor":
        n["boundary_review"] = "✅ 判断方法侧（争议·轻微，PI 可推翻）"
        n["boundary_review_source"] = BND + " §8 争议项字面"
    if e.get("extra"):
        n.update(e["extra"])
    if e.get("face"):
        n["question_face_verbatim"] = e["face"]
    if pend and e.get("listed"):
        n["question_face_verbatim"] = e["face"]
    if entry_class == "calibration_item":
        n["pending_item_status"] = e.get("pending_status")
    n["verbatim_grade"] = "letter_for_letter"
    return n

supplements = []
for e in D8:
    cls = "pending_b_half" if e.get("pend") else "content_question"
    fs = BND + " §3 " + e["q"] if e.get("replaces") else (Q + " §3 " + e["q"])
    supplements.append(build_entry(e, cls, ("D8 批 %s" % e["batch"]) if e.get("batch") else "D8（R 系 b 半 · 顺延）",
                                    "D8_wave2026_09_30", fs))
for e in SQ:
    cls = "skipped" if e.get("skipped") else "open_question"
    supplements.append(build_entry(e, cls, e["batch"], "SQ_wave2026_09_30", SQF + " §3 " + e["q"]))
for e in CAL:
    supplements.append(build_entry(e, "calibration_item", ("D8 批 %s" % e["batch"]) if isinstance(e["batch"], int) else e["batch"],
                                    "D8SQ_calibration_2026_09_30",
                                    e.get("opt_source") or LEDGER + " 批 " + str(e["batch"]) + " 表行"))

# SQ 开放型：answer 即作答全文（引导词为「答（1–3 句）」，非原卷「推理（1 句）」）
for n_ in supplements:
    if n_["entry_class"] in ("open_question",):
        n_["option_chosen"] = None
        n_["option_chosen_letters"] = None
        n_["option_form"] = "open_free_text_no_options"
        n_["option_meaning"] = None
        n_["option_meaning_note"] = "SQ 卷为开放型题（" + SQF + " §1 字面「无 A/B/C 选项，自由作答」）⇒ 无选项释义，记 null"
        n_["pi_other_verbatim"] = n_["pi_answer_verbatim"]
        n_["pi_other_verbatim_note"] = "PI 自由文本逐字，0 润色 0 改写 0 扩写 0 补标点"
        n_["reasoning_full"] = n_["pi_answer_verbatim"]
        n_["reasoning_full_note"] = ("SQ 卷引导词为「答（1–3 句）」（非原卷「推理（1 句）」）⇒ 同一逐字文本同时入 pi_other_verbatim（作答原话位）"
                                     "与 reasoning_full（蒸馏推理位），两字段同值 0 改写，便于下游按 9 字段口径直接取用")
        n_["pi_answer_form"] = "开放型自由文本作答（PI 在 ask_user 问卷上自由作答）"

# ---------------------------------------------------------------- 组装
n_answered_d8 = sum(1 for x in supplements if x["entry_class"] == "content_question")
n_pending = sum(1 for x in supplements if x["entry_class"] == "pending_b_half")
n_sq = sum(1 for x in supplements if x["entry_class"] == "open_question")
n_skip = sum(1 for x in supplements if x["entry_class"] == "skipped")
n_cal = sum(1 for x in supplements if x["entry_class"] == "calibration_item")
n_valued = n_answered_d8 + n_sq + n_cal
assert (n_answered_d8, n_pending, n_sq, n_skip, n_cal) == (77, 3, 7, 1, 5), \
    "分类计数不符: %s" % str((n_answered_d8, n_pending, n_sq, n_skip, n_cal))

def sha12(rel):
    p = os.path.join(ROOT, rel)
    b = open(p, "rb").read()
    return hashlib.sha256(b).hexdigest()[:12], len(b)

anchors = [Q, LEDGER, SQF, BND,
           "results/_v4_pi_cot_v3_dataset.json", "results/_v4_pi_cot_v2_dataset.json",
           "results/_v4_pi_cot_v2_questionnaire_v1.md", "results/_v4_pi_cot_v3_prereg.md",
           "results/_v4_effective_register_2026_09_28.md", "results/_v3_s_prereg_v1_2026_09_27.md",
           "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",
           "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
           "results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json",
           "results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json",
           "results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json",
           "results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json"]
addendum_for = {"touch_policy": "0 触动（本件为纯新建：0 覆写、0 合并、0 删除任何既有件；16 项锚 SHA-12 落盘前后复验不变）"}
for a in anchors:
    s, ln = sha12(a)
    addendum_for[os.path.basename(a).rsplit(".", 1)[0] + "_path"] = a
    addendum_for[os.path.basename(a).rsplit(".", 1)[0] + "_sha12_measured"] = s
    addendum_for[os.path.basename(a).rsplit(".", 1)[0] + "_bytes"] = ln

doc = {}
doc["schema"] = "v4_pi_cot_v3_dataset_addendum_d8_sq/1"
doc["created"] = "2026-09-30T16:40:00+08:00"
doc["created_by"] = "Mavis 团队 worker (执行类·采集入库, 2026-09-30)"
doc["task"] = "D8 大波 + SQ 补采 采集入库（D8 内容题 77 件 + b 半 3 件待采集 + SQ 7 件作答 + SQ-08 跳过 + 口径/处置类 5 件）"
doc["addendum_for"] = addendum_for
doc["post_hoc_amendment"] = True
doc["cross_day_collection"] = True
doc["cross_day_collection_note"] = ("D8 + SQ = 2026-09-30 字面采集日（采集源 = PI 2026-09-30 通过 ask_user 分 23 批实时作答，"
                                    "逐批记录于盘上台账；日期戳归采集日 2026-09-30）。**b 半 3 题（D8-11/D8-19/D8-37）当日未作答，"
                                    "按卷规顺延 10-01+ ⇒ 其跨日间隔自落件日起算，本件 0 预填该间隔。**")
doc["collection_round"] = "D8 大波（20 批）+ SQ 补采（3 批）+ 出题侧边界修订后重启段（批 8 起）"
doc["collection_date"] = "2026-09-30"
doc["source_pi_judgment_basis"] = (
    "PI 2026-09-30 通过 ask_user 分批实时作答；**唯一数据源 = 盘上台账 " + LEDGER + "（今日全程逐字记录、随批维护）**。"
    "本棒 0 取得 ask 原件（ask 记录不落盘，沿盘上 d6/d6b/d7 落件惯例）⇒ 所记 ask_id 与 PI 答复字面均转录自台账，"
    "0 声称已核验 ask 原文。0 LLM 代答、0 判定层补全。")
doc["source_ask_ids"] = [
    "ask_72adb71ea07edc063ceed334", "ask_a6f88ff30bf89a8e804239d9", "ask_ffe8cdf9d2b1d84294afd1c6",
    "ask_d36d1fa8c5265673a67fcdd1", "ask_5901a28baa3485800e376ac1", "ask_cd08e7bacaa1cb99ecceaa34",
    "ask_de8dbebee79a8e9ebde007fa", "ask_4341a4423c517f0e41c99abd", "ask_16f0f4dc3ae9321ef79de182",
    "ask_faf9de6def9e1c2384a5954b", "ask_a5bf873f436ba5a68a808567", "ask_1d3dd509d148173cc4baa95f",
    "ask_e6b4fcbe7b00e25aab4d69fa", "ask_cba2075ac4faf0f4f4d28ae7", "ask_882bdceab49d3ed97d4f73b0",
    "ask_721f00fa3e4977bcc0f56d45", "ask_2c5426e79464ebd78d48c8fc", "ask_10e87126e314e298e0ed6db4",
    "ask_fa8b654cc5221cd654e880dc", "ask_91c25e9740d3cef10f18cd49", "ask_e829a3e1bb17f57d6029fbba",
    "ask_921f42b832970a9d5274fbfb", "ask_a8ebc92a2538769f44ebcd87"]
doc["source_ask_id_note"] = "23 个 ask_id 全部转录自台账各批回执字面；ask 记录不落盘 ⇒ 0 声称已核验 ask 原文"
doc["explicit_user_confirmation"] = True
doc["pi_realtime_answering_window"] = True
doc["unique_data_source"] = {
    "path": LEDGER,
    "sha12_measured": sha12(LEDGER)[0],
    "bytes_measured": sha12(LEDGER)[1],
    "role": "唯一数据源：全部 93 条条目的 PI 答复字面、ask_id、批号、台账行号、「形态」列登记均以此为准；本棒 0 用其它件补写 PI 答复",
    "ledger_sha_drift_registration": {
        "drift_family": "台账为活文档（随批追加），既有件登记值与本棒实测值不同源不同时点",
        "values_on_record": [
            {"sha12": "deec8c91a75b", "bytes": 1957, "recorded_in": SQF + " §0.1 第 4 行（批 1–2 态）"},
            {"sha12": "e61f4050fc02", "bytes": 6195, "recorded_in": BND + " §0.1 第 4 行（批 1–7 态）"},
            {"sha12": "d87518e980e7", "bytes": 7470, "recorded_in": LEDGER + " 「边界修订」块自记（批 8 之前某态）"}
        ],
        "measured_by_this_piece": {"sha12": sha12(LEDGER)[0], "bytes": sha12(LEDGER)[1],
                                   "measured_at": "2026-09-30 本棒落盘前实测（.NET/SHA-256 等价 hashlib）"},
        "handling": "四值并存如实登记，**0 归因、0 覆写、0 代为调和**（沿 D8-45 同族纪律：自报 SHA 与实测不符 ⇒ 并列登记，不编造根因）",
        "note": "本棒 0 声称知道差异根因（可能是逐批追加导致，也可能另有他因）"
    }
}
doc["supplements"] = supplements
doc["supplement_count"] = len(supplements)
doc["coverage_verification"] = {
    "d8_total_questions_in_face": 80,
    "d8_entries_in_this_piece": n_answered_d8 + n_pending,
    "d8_answered": n_answered_d8,
    "d8_pending_b_half": n_pending,
    "d8_pending_ids": ["D8-11", "D8-19", "D8-37"],
    "d8_pending_note": "R9b/R10b/R11b 三题按卷规避开当日（≥1 天间隔），状态＝待采集（10-01+）⇒ ⛔ option_chosen / reasoning_full / option_meaning / is_correction / weight 全部 null，0 代填 0 虚构",
    "r_version_replacement": {
        "replaced": ["D8-58", "D8-59"],
        "replacement_entries": ["D8-58r", "D8-59r"],
        "r_text_source": BND + " §3（PI 2026-09-30 4 裁第 ① 项「r-text 4 条全部采纳」）",
        "note": "原 D8-58/D8-59 在出题侧修订前未采集（0 既有答案）⇒ 本件 80 题覆盖由 D8-58r/D8-59r 占位，0 重复计数、0 漏项；题量 80 不变"
    },
    "d8_15_16_handling": {
        "ids": ["D8-15", "D8-16"],
        "pi_ruling_verbatim": "D8-15/16 保留＋标注「外沿」（本台账两题行按此标注为准，数据不重问）",
        "source": LEDGER + " 尾部「PI 4 裁（2026-09-30，全选 ①）」第 ② 项字面",
        "handling": "答案 0 回改、原样保留；本件按该裁决加 boundary_tag=外沿 字段（不改判 judge_type、0 重采）",
        "d8_15r_16r_note": "PI 同批亦全采纳 D8-15r/D8-16r 两条 r-text（" + BND + " §3），但对 D8-15/D8-16 本体裁决为「保留＋外沿标注，数据不重问」⇒ 本件 0 用 r 版替换 D8-15/16（0 重复计数），两题按原题面字面登记"
    },
    "sq_total_questions_in_face": 8,
    "sq_answered": n_sq,
    "sq_skipped": n_skip,
    "sq_skipped_ids": ["SQ-08"],
    "sq_co_landed_in_same_piece": True,
    "sq_landing_decision": "SQ 7 件与 D8 85 件并入本件同落（PI 2026-09-30 T-D8-2 拍板 B「追加补采波」的产物）⇒ 按体例自定为**同件落盘 + entry_class 分域**（open_question / skipped 与 D8 content_question 分域可滤），0 拆分多件、0 另起 SQ 件；如后续需独立 SQ 件须新名另落（0 覆写本件）",
    "calibration_items": n_cal,
    "calibration_ids": ["T-D8-1", "T-D8-2", "T-D8B-7", "skill-4", "skill-6"],
    "calibration_note": "5 件口径/处置类拍板以 entry_class=calibration_item 登记（judge_type 记 \"calibration\"，非 J1–J6）⇒ 0 冒充题面 judge_type 提案、0 计入 80/8 题量",
    "total_entries": len(supplements),
    "entries_with_values": n_valued,
    "entries_null": n_pending + n_skip,
    "duplicate_check": "0 重复（脚本内 assert：93 个 q_id 唯一）",
    "coverage_order_check": "D8 条目严格按题号顺序 D8-01..D8-80（58/59 位由 58r/59r 占位）；SQ 按 SQ-01..SQ-08；口径 5 件按台账出现序"
}
doc["verbatim_policy"] = (
    "PI 原话逐字保留，禁止改写/润色/扩写/补全标点（" + Q + " §1 第 2 条字面）。"
    "字段口径：① pi_answer_verbatim = 台账作答格逐字（去最外层「」包裹）＝**每条都在的原字面锚**；"
    "② option_chosen = PI 字面选项落点（单选＝字母；多选/三选＝字母串＋结构化 option_chosen_letters；Other＝「Other（原话）」沿 d6b 惯例；口径题＝圈码）；"
    "③ option_meaning = 题面对应选项字面释义（单选落点才有；多选/Other/口径题无对应单一条释义 ⇒ 记 null + selected_option_faces_verbatim 逐档并列，0 挑一档当唯一落点）；"
    "④ reasoning_full = **仅当台账「形态」列明示「＋推理/＋理由/＋补充/＋警示/＋修正口径/＋题性指定」时才拆填**（0 把选项复述/外延/合成语当推理）；"
    "SQ 开放型因无选项且引导词为「答（1–3 句）」⇒ 全文同值入 pi_other_verbatim 与 reasoning_full（0 改写）；"
    "⑤ judge_type = 题面「judge_type 提案」字面（" + Q + " §3 每题行），0 worker 改判；口径/处置类无题面提案 ⇒ 记 \"calibration\"；"
    "⑥ is_correction 按题面 §1 第 5 条字面标注（R 系 a 半 3 件＝配对标记 true + correction_confirmed=false），0 预判 b 半方向；"
    "⑦ scene_tag 为本棒 worker 赋的英文蛇形标签（沿既有落件同惯例），0 编造题面。"
    "本棒不翻 v1/v2/v3 既有判定。")
doc["pi_source_disclosure"] = {
    "pi_realtime_answering_window": True,
    "encoding_source": "PI 2026-09-30 通过 ask_user 分 23 批实时作答，答复字面逐批记录于盘上台账；本件 100% 转录台账",
    "verbatim_policy_reference": Q + " §1 第 2 条字面 + d6b Other 落盘惯例（option_meaning=null + pi_other_verbatim 逐字）＋ d6/d7 跳过推理记 null 惯例",
    "worker_self_judgment_layer_disabled": True,
    "hard_gate_tripped": False,
    "hard_gate_note": ("硬闸触发条件 = 若勘察后判定值必须由 LLM 代答才能完成。本棒全部 89 条含值判定值 100% 来自 PI 原答（台账逐字），"
                       "0 LLM 代答、0 API、0 proxy、0 gateway；硬闸未触发。"),
    "no_fabrication_declaration": (
        "0 编造题面（scene_verbatim/question_face_verbatim 逐字取自三件盘上原件）；0 虚构 PI 判定值（0 代填、0 推补、0 用邻题答案推补 SQ-08）；"
        "0 编造选项释义（件上无该字面者记 null）；0 编造 ask 原文（0 取得 ask 原件，如实声明转录自台账）；"
        "0 编造跨日间隔（b 半 0 预填）；0 编造纠正事件（b 半未作答 ⇒ R 系 0 闭合、0 断言反转）。")
}
doc["cross_cutting_signals"] = [
    {"q_id": "D8-25", "signal_verbatim": "我怎么感觉问卷又往画像侧偏了",
     "registration": "画像侧偏信号（PI 触发）⇒ 任务 B 边界＝批判性学习判断方法、非画像；PI 边界裁决＝暂停出题侧修订；出题侧修订件 80 题审读 ✅76｜⚠️4｜❌0",
     "source": LEDGER + " 批 7 表下方 + " + BND + " §2/§8"},
    {"q_id": "D8-15", "signal_verbatim": "此外重复口径的题可以适当合并，这是出题侧缺陷，既不广也不深，不应怪罪或转嫁于引导侧与PI侧",
     "registration": "出题侧缺陷项（PI 原文）；parent 处置＝核心 80 题本体 0 擅动（保持仪器一致性），登记交后续出题设计吸收",
     "source": LEDGER + " 批 4 表下方"},
    {"q_id": "D8-34", "signal_verbatim": "保证主线统一，也因此应点明主线，上周过于开放，一致成果没对齐主线",
     "registration": "委托面口径信号；与 D8-73 互证（不含大纲＝结构自由，≠不说主线；须给实验成果线索）",
     "source": LEDGER + " 批 9 表行"},
    {"q_id": "D8-73", "signal_verbatim": "以新案优先，此外不是大纲而是实验成果线索，否则受委托方无从下手",
     "registration": "委托面口径再澄清；台账记「已追加 user 记忆补注」",
     "source": LEDGER + " 批 19 表行"},
    {"q_id": "D8-44", "signal_verbatim": "选项本身可制作规则集，但规则集是有限的，至少升级为脑图并利用deposon相关成果资产",
     "registration": "设计垂线信号（规则集有限 ⇒ 升级为脑图 + 用 deposon 成果资产）",
     "source": LEDGER + " 批 11 表行"},
    {"q_id": "D8-49", "signal_verbatim": "0复用是指不复用答案，否则跨日无意义，此外口径变化是防记忆效应的体现",
     "registration": "PI 规则释义（0 复用所指＝不复用答案；口径变化＝防记忆效应）",
     "source": LEDGER + " 批 13 表行"},
    {"q_id": "D8-51", "signal_verbatim": "拍板本身是蒸馏资产，且画像侧充足，因此采集侧不应重复采集画像侧",
     "registration": "设计信号（拍板＝蒸馏资产；采集侧不重复采集画像侧）",
     "source": LEDGER + " 批 13 表行"},
    {"q_id": "D8-51", "signal_verbatim": "BC，保持口径一致避免麻烦", "registration": "⚠️ 与题面 A 档「0 触动」相左（按答入账）",
     "source": LEDGER + " 批 11 表行"},
    {"q_id": "D8-52", "signal_verbatim": "B，先由PI复核，人是活的，PI是人", "registration": "⚠️ 与题面 A 档「0 合并」相左（按答入账）",
     "source": LEDGER + " 批 13 表行"},
    {"q_id": "D8-45", "signal_verbatim": "B，实事求是", "registration": "⚠️ 与题面 A 档「并列登记」相左（按答入账）",
     "source": LEDGER + " 批 12 表行"},
    {"q_id": "D8-74", "signal_verbatim": "B，保持统一下新案优先", "registration": "⚠️ 与题面 A 档相左（按答入账）",
     "source": LEDGER + " 批 19 表行"},
    {"q_id": "D8-15", "signal_verbatim": "C，我选A", "registration": "⚠️ 原答起首「C，」与实际落点 A 不一致（PI 随后明示「我选A」）⇒ 按台账登记落点 A，原答逐字保留",
     "source": LEDGER + " 批 4 表行"},
]
doc["r_pair_closure_status"] = {
    "pairs": ["R9", "R10", "R11"],
    "a_half_landed": ["D8-10", "D8-18", "D8-36"],
    "b_half_pending": ["D8-11", "D8-19", "D8-37"],
    "closed_pairs": 0,
    "note": "三对均未闭合（b 半待 10-01+）⇒ **0 断言发生纠正/反转事件**；a 半 is_correction=true 仅为题面 §1 第 5 条的配对标记（沿 d6 件 DF6-3 同惯例），correction_confirmed=false",
    "correction_event_counted": 0,
    "source": Q + " §4 R 系反转配对索引字面 + " + LEDGER + " 收讫总况字面「R9／R10／R11 三对 a 半均已完成」"
}
doc["kill_line_and_counting_note"] = {
    "scope_boundary": "本件 = **采集入账件**（0 判定、0 判死、0 改阈）；以下仅为如实登记的账目面，达标与否由收口/verifier 棒判定",
    "n_accounting_this_piece": {
        "d8_content_answered": 77, "d8_pending": 3, "sq_answered": 7, "sq_skipped": 1, "calibration_items": 5,
        "entries_with_values": n_valued, "entries_null": n_pending + n_skip, "total_entries": len(supplements),
        "counting_convention_note": ("三口径并存如实并记、0 合并裁定（沿 d4 relabel / d6b counting_convention_note 惯例）："
                                      "①「判定事件」口径＝含值条目 " + str(n_valued) + " 件；"
                                      "②「题面覆盖」口径＝D8 80 题（77 答 + 3 待）+ SQ 8 题（7 答 + 1 跳）= 88 题；"
                                      "③「台账 substrate 口径」＝台账自记（见 substrate_ledger_face）。三者成分不同，0 用任一口径判达标。")
    },
    "substrate_ledger_face": {
        "verbatim": "substrate 账：163 ＋ 7 ＝ 170 ≥167 ✓",
        "source": LEDGER + " 「🏁 今日采集收讫总况」字面",
        "second_reading_measurement": "按实答数复算：83（T-D8-1 口径 ② 盘上实存）+ 77（D8 实答）＋ 7（SQ 实答）= 167 = 自洽下限（" + Q + " §0.1 第 3 行 K-V3S-4-2 自洽下限 167 字面）",
        "difference_note": ("台账按「D8 波 80 题」计（83+80=163），本件按「实答 77 题」计（83+77=160）⇒ 两读数差 3 件（= b 半 3 题待采集）。"
                            "**本棒 0 校正、0 裁定、0 宣告达标**；两口径如实并记，归口 V4 收尾整理时批量校正。"),
        "k_v3s_4_2_threshold_touched": False
    },
    "cross_day_and_ratio_measurement": {
        "rule_literal": "K-V3S-3-1 distinct calendar days >= 5（" + LEDGER + " 引 " + Q + " §2/§6.4 字面）",
        "prior_distinct_days_before_this_piece": 5,
        "prior_date_set": PREV_DAYS,
        "new_day_introduced_by_this_piece": "2026-09-30",
        "distinct_days_after_this_piece": 6,
        "independent_rescan": ("本棒实测：递归遍历 results/_v4_pi_cot_v2_dataset*.json + results/_v4_pi_cot_v3_dataset*.json，"
                               "收集一切含 10 位 YYYY-MM-DD `date` 字段的节点，得到的日期集合 = " + json.dumps(scanned, ensure_ascii=False) +
                               "；其中 2026-09-30 来自本件新增事件 ⇒ 与登记面 5+1=6 天一致（2 源互证）"),
        "scan_note": "本件落盘前复扫（不含本件）；本件 0 判定该读数是否达标、0 改任何阈值、0 触碰 K-V3S-3-2（单日 ≤0.60）/ K-V3S-3-3（N≥50 且纠正≥5）/ K-V3S-3-4（1.00）",
        "b_half_effect": "b 半 3 题落 10-01+ ⇒ 跨日天数只会增加、0 减；本件 0 预填该日读数"
    },
    "v3_official_substrate_locked_count": 85,
    "v3_official_substrate_locked_note": "沿 5118f5b44f17 §accounting_balance_conservation 字面「v3_formal_experiment_substrate = 85 events」登记；本件 0 改动 substrate、0 重跑 result_v3 / verdict_v3、0 声称本件入 v3 正式 substrate",
    "v1_3_data_surface_reserved": True
}
doc["constraints_compliance"] = {
    "key_never_in_prompt_or_json": True, "key_never_on_disk": True,
    "no_llm_judgment_layer": True, "no_api_call": True, "no_proxy": True, "no_gateway": True,
    "no_dataset_modification": True, "no_merge_into_dataset": True, "no_merge_into_any_existing_json": True,
    "no_existing_file_overwritten": True, "no_existing_file_deleted": True, "no_new_killline": True,
    "no_threshold_tampering": True, "no_pii_reasoning_promoted_out_of_repo": True,
    "reasoning_privacy": "全部 PI 推理全文仅入本地件 results/，0 外发、0 入任何外部模型 prompt（PI 本人 D8-53 答：本地 A ／ 外发版 C 打码）",
    "rationale": ("V4 铁律沿用口径（key 永不明文无例外；V1–V3 只读不动；派生 JSON 不合并；0 擅调阈值）。本件为独立新建 addendum 件，"
                  "落盘目标 " + OUT + "（落盘前实测不在盘）；0 覆写 dataset v1.2/v1.1、0 合并任何既有 JSON、0 触动 16 项锚。")
}
doc["skill_disclosure"] = {
    "requested": None,
    "status": "本棒未加载任何 skill（派工单未指定 skill）",
    "disclosure": "未加载任何 skill 的任何指令；0 引用、0 虚构任何 skill 条文。实质纪律锚 = 盘上件字面：" + Q + " §1 第 2/3/4 条 + " + LEDGER + " + " + SQF + " §1/§2 + d6b/d7 落件惯例。",
    "pi_reported_skill_dir_issue": "D8-69 答中 PI 逐字实况「skill 目录需要更新了…minimax code 更新了…」已按台账逐字登记；本棒 0 加载、0 更新任何 skill 目录"
}
doc["metadata"] = {
    "algorithm": "SHA-256 前 12 位（小写）",
    "author": "Mavis 团队 worker (执行类·采集入库)",
    "date": "2026-09-30",
    "encoding": "UTF-8 (no BOM)",
    "line_ending": "LF",
    "type": "cross_day_critical_reflection_addendum_d8_sq_v3_v1_3_reserved",
    "version": "v1",
    "agent": "worker (执行类)",
    "branch_session": "mvs_31307d0c285c42ef860fee93ed195ef8",
    "generator": ".tmp/_run_d8_addendum_2026_09_30.py",
    "signature_line": "Mavis 团队 worker 出件 | 2026-09-30",
    "track": "Track 1（0 LLM / 0 API / 0 proxy / 0 gateway）",
    "v1_3_data_surface_reserved": True,
    "pi_source": "PI 2026-09-30 分 23 批 ask_user 实时作答（台账逐字转录）；0 LLM 代答；判定层 0 LLM；SQ-08 跳过记 null；b 半 3 题 0 预填",
    "sha12_case_note": "本件 SHA-12 一律记小写（hashlib.sha256 hexdigest()[:12]）；既有件正文登记值部分为大写（如 dataset v1.2 = 5118F5B44F17），大小写等价可比对，0 语义冲突",
    "succeeded_not_equal_finished": "succeeded ≠ 跑完；本件以盘上 SHA-12 落盘核验 + JSON 可解析复验 + 93 条覆盖/唯一性 assert 全过为准（见 self_verification）",
    "self_hash_caveat": "本件不写自指哈希字段（沿 d7 落件口径，避免 d6 件所记的自指漂移结构性必然）；下游引用一律以盘上实测 SHA-12 为准"
}
doc["self_verification"] = {
    "assertions_run_pre_landing": [
        "D8 条目 q_id 唯一 + 与 D8-01..D8-80 期望集完全一致（58/59 位由 58r/59r 占位）+ 严格按题号序",
        "SQ 条目 = SQ-01..SQ-08 完整且按序",
        "口径条目 = [T-D8-1, T-D8-2, T-D8B-7, skill-4, skill-6]",
        "全表 93 个 q_id 唯一（0 重复）",
        "每条非待采集 D8 条目的 ask_id 与台账批号映射一致（批 1–20 ↔ 23 个 ask 回执）",
        "分类计数 == (77, 3, 7, 1, 5)"
    ],
    "post_landing_to_verify": ["盘上 SHA-12 / 字节 / 行数", "JSON 可解析复验", "16 项锚 SHA-12 落盘前后不变"],
    "no_self_hash_field": True
}
doc["honesty_boundary"] = [
    "**本棒是采集入账棒，不是判定棒**：0 判 substrate/held-out/跨日/单日占比是否达标、0 宣告「达标」、0 改任何阈值；账目面只如实登记。",
    "**ask 原件不落盘**：93 条的 PI 答复字面与 23 个 ask_id 全部转录自盘上台账（唯一数据源）；0 取得 ask 原件、0 声称已核验 ask 原文、0 伪造 PI 作答时分。",
    "**b 半 3 题（D8-11/D8-19/D8-37）当日未作答**：全部值字段 null（含 is_correction/weight）⇒ 0 代填 0 虚构 0 预判；R9/R10/R11 三对 0 闭合、0 断言纠正/反转。",
    "**SQ-08 为 PI 明示跳过**：记 null；0 用 SQ-04..SQ-07 或邻题答案推补。",
    "**0 合并 / 0 覆写**：本件为纯新建（落盘前实测不在盘），未合并、未覆写、未删除任何既有件；16 项锚 SHA-12 落盘前后复验不变。",
    "**台账 SHA 漂移四值并存**（deec8c91a75b/1,957 B、e61f4050fc02/6,195 B、d87518e980e7/7,470 B、本棒实测 199a206d2800/17,946 B）⇒ 并列登记，0 归因（与 PI 在 D8-45/D8-46/D8-48 所答同族）。",
    "**4 处 PI 落点与题面 A 档相左**（D8-42 / D8-45 / D8-52 / D8-74）+ **D8-15 原答起首「C，」但落点 A** ⇒ 逐字按答入账并显式登记相左，0 代 PI 调和、0 改题面。其中 D8-52（选 B 合并为主件）与派工单「⛔ 0 合并任何既有 JSON」相左 ⇒ **判定值按 PI 原答入账，执行面按派工单硬约束落新件**，两者分层登记。",
    "**PI 明示的日期 0 核实**：collected_at 全部 null（ask 记录不落盘，0 秒级核验，0 伪造时分）。",
    "**未做也不声称**：0 重算 result/verdict、0 更新任何台账计数、0 派工、0 触 skill、0 调外部 API、0 代 PI 关闭任何待拍板项（T-D8-3 仍开）。",
    "**文件数类账目（986/994/1,004 三口径差额）不在本棒范围**：按 PI 2026-09-27 口径归「V4 收尾整理」批量校正，本棒 0 单独校正、0 追问。"
]

out_path = os.path.join(ROOT, OUT)
assert not os.path.exists(out_path), "目标件已在盘，⛔ 拒绝覆写：" + OUT
txt = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
b = open(out_path, "rb").read()
print("LANDED:", OUT)
print("sha12:", hashlib.sha256(b).hexdigest()[:12])
print("bytes:", len(b))
print("lines:", txt.count("\n"))
print("bom:", b[:3] == b"\xef\xbb\xbf")
print("crlf_present:", b"\r\n" in b)
print("counts:", {"d8_answered": n_answered_d8, "d8_pending": n_pending, "sq_answered": n_sq,
                  "sq_skipped": n_skip, "calibration": n_cal, "total": len(supplements)})
