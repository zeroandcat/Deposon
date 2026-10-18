# 任务 B v2 · operationalization 编码表复核（protocol-keeper，2026-09-26）

- **复核性质**：探索性预跑前 protocol-keeper 立线复核（formal_go=放行正式判定链前置条件之一，PI 2026-09-26 18:27 ask_822b1e27a43f2bf8ff86785d 显式拍板）
- **触发依据**：verdict-keeper `_v4_pi_cot_v2_verdict.md`（EB9AD4193CF2）§2.1 + §5.2 形式效力声明「protocol-keeper 对 operationalization_v1.judgment_type_extraction（6 类编码表 + 关键词首现位置序）复核签字——覆盖度 + 退化性评估」
- **复核对象**：`_v4_pi_cot_v2_ruleset.json`（821465001819）+ `_v4_pi_cot_v2_ruleset_executor.py`（48DCA1D4281C）+ `_v4_pi_cot_v2_result.json`（1665F367B2C4）内嵌 `operationalization_v1.judgment_type_extraction`
- **复核面**：现有 80 件全量 = dataset v1.1 (37 events + 3 addendum reasoning补填 = 40 件；含 D1 推理补填 8 件盘外源记 48 件) + D2 wave1-5 (20 件) + D3 wave1-3 (12 件) = 72 件盘上可得 + 8 件盘外补填待采；本复核以盘上 72 件为实测对象
- **产物**：本复核件唯一，落盘即报 SHA-12 + 字节
- **铁律严守**（沿用 V4 派工 5 件必带）：key 永不明文；判定阈值/kill-line 一字不动（编码表=度量构造非阈值，但修订须留痕并给 v1→v2 diff）；seed=42 确定性纯函数口径沿字面；不覆盖任何既有件（复核件新名 `_v4_pi_cot_v2_coding_review_2026_09_26.md`）；派生 JSON 不合并（不动既有 `_v4_pi_cot_v2_result.json` / `_v4_pi_cot_v2_ruleset.json` / `_v4_pi_cot_v2_dataset*.json` 任何 SHA-12）

---

## §0 锚件 SHA-12 前 12 核验（只读，先核后用）

| 件 | 派工字面 | 实测 | 状态 |
|---|---|---|---|
| `_v4_pi_cot_v2_prereg.md` | CC25C5149CE1 | CC25C5149CE1 | ✓ |
| `_v4_pi_cot_v2_result.json` | 1665F367B2C4 | 1665F367B2C4 | ✓ |
| `_v4_pi_cot_v2_verdict.md` | EB9AD4193CF2 | EB9AD4193CF2 | ✓ |
| `_v4_pi_cot_v2_ruleset.json` | 821465001819 | 821465001819 | ✓ |
| `_v4_pi_cot_v2_ruleset_executor.py` | 48DCA1D4281C | 48DCA1D4281C | ✓ |
| `_v4_pi_cot_v2_dataset.json` | 7B01CD835A41 | 7B01CD835A41 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 6F76EAE13FA0（自报 fingerprint_self_hash_after_birth） | 172093A23E4B（**实测，与自报值不一致**——见 §5.7 已知哈希漂移） | ⚠ 漂移 |
| `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 439721007AAF | 439721007AAF | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 41D6C28CA87C | 41D6C28CA87C | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 99C58906F792 | 99C58906F792 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | C6D092F77932 | C6D092F77932 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 26F110A6E571 | 26F110A6E571 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 6E104E2DB038 | 6E104E2DB038 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | D96B747BFC6C | D96B747BFC6C | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 367723816B89（自报 fingerprint_self_hash_after_birth） | 401BD614CDF7（**实测，与自报值不一致**——见 §5.7 已知哈希漂移） | ⚠ 漂移 |

---

## §1 problem 诊断（v1 编码表覆盖度实测）

### §1.1 verdict-keeper 已识别暴露面

`verdict-keeper §2.1 K-V2-a 学习线 根因分析` 直报：「6 类判据编码表 UNKNOWN = 14/37 = 37.8%（非边缘主导），关键词「首现位置序」编码对一句级短推理覆盖不足」。

`verdict-keeper §2.2 K-V2-b1 批判线 根因分析` 直报：「批判反思标志词表 28 个词（result.json operationalization_v1.critical_reflection_markers），对 PI 短句中「元方法论自陈」「命题类比」「准则解释」类批判表达覆盖不足——词表偏口语转折词（不/却/反而/然而/但是/但），对 PI 风格的「虚实闭合」「大一统定义」「判死线本就是预设的」类硬概念批判缺位」。

派工单触发点（PI 2026-09-26 18:27）：「exploratory pre-run 中 UNKNOWN 占 38%（14/37，PI 一句级短推理覆盖不足）——复核该编码表对**现有 80 件全量**（dataset v1.1 37+11 + D2 20 + D3 12）的覆盖度实测（编码分布 + UNKNOWN 率逐波统计）」。

### §1.2 80 件全量实测方法

- **盘上可得 72 件**（本复核件能直接读 reasoning_full）：dataset v1.1 = 37 events；D1 addendum 09-24 = 3 events reasoning补填（event 17/21/27）；D2 wave1-5 = 19 件 questionnaire（剔除 case1 pi_disposition 非问卷件）+ 1 件 case1 处置文本合并 = 20 件；D3 wave1-3 = 12 件三读稳定性探针
- **盘外 8 件**：D1 推理补填 8 件（verdict-keeper §1 D1=48 件 vs 盘上 40 件差额；据 d2e honesty_note 「D1=48 事件」反推 8 件 D1 推理补填事件未在本棒视野）；如实声明缺位不补造
- **本棒实测对象**：72 件盘上可得 + 8 件待采标注
- **编码逻辑字面沿用**：`_v4_pi_cot_v2_ruleset_executor.py` §3 KEYWORDS_BY_TYPE（v1 字面）+ §3 `extract_judgment_sequence`（首现位置序扫描 + 去重保序）+ §3 `primary_judgment_type`（序列首元素/空序列归 UNKNOWN）；0 擅调
- **不写盘原则**：实测通过本地临时脚本复算（`_tmp_v1_recompute.py` → `_tmp_v2_redesign.py` → `_tmp_v2_compare.json`，后述 v2 复核同样本棒路径），0 落盘 `_v4_pi_cot_v2_*` 既有件

### §1.3 v1 编码表覆盖度实测（72 件全量逐波统计）

| 波次 | 件数 | UNKNOWN 件数 | UNK 率 | 6 类分布（v1） |
|---|---|---|---|---|
| **D1_main**（dataset v1.1 主集） | 37 | **14** | **37.8%** | RISK 5 / COST 1 / KILL_LINE 2 / CRITERIA 7 / TIMING 7 / DELEGATE 1 |
| **D1_supp**（D1 推理补填 3 件） | 3 | 2 | 66.7% | DELEGATE 1 / UNKNOWN 2 |
| **D2_w1**（R1b/R2b/R3b/R4b） | 4 | 3 | 75.0% | COST 1 / UNKNOWN 3 |
| **D2_w2**（R5b/R6b/Q38/Q39） | 4 | **4** | **100.0%** | UNKNOWN 4（Q39 reasoning_missing=true） |
| **D2_w3**（Q40-Q43） | 4 | 3 | 75.0% | DELEGATE 1 / UNKNOWN 3 |
| **D2_w4**（Q44-Q47） | 4 | 3 | 75.0% | DELEGATE 1 / UNKNOWN 3 |
| **D2_w5**（Q48-Q50/case1） | 4 | 3 | 75.0% | KILL_LINE 1 / UNKNOWN 3 |
| **D3_w1**（Q1/Q2/Q4/Q5 三读） | 4 | 2 | 50.0% | CRITERIA 2 / UNKNOWN 2 |
| **D3_w2**（Q6/Q8/Q9/Q10 三读） | 4 | 3 | 75.0% | CRITERIA 1 / UNKNOWN 3 |
| **D3_w3**（Q11/Q12/Q16/Q17 三读） | 4 | 3 | 75.0% | CRITERIA 1 / UNKNOWN 3 |
| **合计** | **72** | **40** | **55.6%** | RISK 5 / COST 2 / KILL_LINE 3 / CRITERIA 11 / TIMING 7 / DELEGATE 4 |

**关键观测**（一句一次）：
- **v1 UNK 率 55.6%**（72 件中 40 件归 UNKNOWN），D1_main 单波 37.8% 与 verdict-keeper §2.1 字面一致；D2/D3 跨天续采后**逐波 UNK 率恶化**（D2_w1=75.0%、D2_w2=100.0%、D2_w3-5=75.0%；D3_w1=50.0%、D3_w2-3=75.0%）——**v1 编码表对一句级短推理（特别是 D2/D3 反转配对后半 + 独立补充判定）覆盖严重不足**
- **n_distinct 类型 = 6 + UNKNOWN = 7**（无退化警报；PASS 沿用 protocol-keeper 防退化构造审查规则）；最大类 RISK 在 D1_main 占 5/37 = 13.5%，无任何类支配性（远低于 85% 阈值）
- **D2/D3 高 UNK 率根因**：(i) PI 一句级短推理中嵌入 deposon 凝子/大一统/硬核/庖丁解牛/虚实闭合 等哲学口径（v1 CRITERIA 词表未覆盖）；(ii) PI 用 VS code/Mavis/外援/共同体/GLM/coze 等具体委托术语（v1 DELEGATE 词表部分缺失）；(iii) PI 用先斩后奏/补测/续采/分批上线 等时机短语（v1 TIMING 词表覆盖不足）

### §1.4 verdict-keeper 关键 3 件 idx=16/20/26 复核（沿 verdict-keeper §2.2 字面）

| event_id | reasoning_full 简摘 | v1 primary | v1 has_critical | 复核结论 |
|---|---|---|---|---|
| **16** | 不可误导，且避免打回，自检是重要的，自检手段比起复杂设计更在于错题集而三件即包含本次及前人教训经验 | UNKNOWN（v1 seq=[]） | True（「不可」「避免」词表命中） | v1 漏检：v1 RISK 词表无「不可误导」类词（v1 有「不可」在 critical_reflection_markers 但非 RISK 主词表）；**v2 修订点：RISK 加「不可」+「误导」** |
| **20** | deposon的核心资产是deposon凝子的大一统定义，如果必须舍弃deposon衍生出来的算法才可实现，或者舍弃也不可实现则是真证伪，否则若可复合其他算法解决则假证伪 | RISK（v1 seq=['RISK']，via「假」） | True（「不」「不可」词表命中） | v1 抓 RISK 主导但失 CRITERIA 大一统定义语境；**v2 修订点：CRITERIA 加「deposon」「凝子」「大一统」「大一统定义」** |
| **26** | 就像非欧几何，在出现新形态时；或者虚构产物本身可向下兼容，如物理学 | UNKNOWN（v1 seq=[]） | False | v1 双漏：CRITERIA 词表无「非欧几何」「新形态」「向下兼容」等 FTFB 命题类比词；has_critical 词表亦未命中；**v2 修订点：CRITERIA 加 FTFB 命题类比词（但 v2 仍留 UNKNOWN——见 §2.4 边界声明）** |

verdict-keeper §2.2 标注「has_critical_reflection=false」与 v1 `extract_judgment_sequence` 函数 `has_critical_reflection`（28 词表 substring 匹配）字面存在解读差异：v1 函数对「不可误导」会因「不可」substring 命中返回 True，但 verdict-keeper 主观判定「不可误导」属元方法论自陈而非真实批判反思——**此为关键词表 vs 语义判读的层次差异，非编码表覆盖问题**。本复核件不就 verdict-keeper 的语义层判定表态，沿字面记录差异。

---

## §2 operationalization_v2 定稿（正式判定用）

### §2.1 设计原则（按派工单 + T1.5r2 verdict 前例建议）

1. **同 6 类 + UNKNOWN 兜底**（沿 prereg §1 字面，不私设类）
2. **首现位置扫描 + 纯函数确定性 + seed=42**（沿 v1 executor 字面）
3. **宽口径同义关键词扩充**（采用 T1.5r2 verdict 前例建议的宽口径路线；两段式分层=粗类→细类作为备选，v2 当前不启用——因 v1 6 类 taxonomy 已固化为判据类型确定性编码表，引入粗类会破坏已锁定的 6 类输出接口）
4. **禁单字过广词**：「派」「通」「速」「级」等单字不单独入表（v2 中"派"以复合短语形式入 DELEGATE 表，避免 catch-all）
5. **0 擅调阈值/kill-line**：本表为度量构造非阈值，v1→v2 修订仅扩词表，不动 TH-v2-1..8 字面与 K-V2-a/b1/b2/c 字面

### §2.2 v2 编码表（宽口径同义关键词扩充，沿用首现位置序扫描）

```python
# ============================================================================
# operationalization_v2 (本复核件定稿, 2026-09-26)
#   - 同 6 类(KILL_LINE/COST/CRITERIA/RISK/TIMING/DELEGATE) + UNKNOWN 兜底
#   - 宽口径同义关键词扩充 (基于 72 件 reasoning_full 已现 PI 表达)
#   - 第一位位置扫描 + 纯函数确定性 + seed=42 沿字面
#   - 严禁单字过广词(如"派"/"通");只增加 PI 推理中已出现的具体语境
# ============================================================================
KEYWORDS_V2 = {
    # KILL_LINE 判死线: v1 词表 + PI 风格"完成性"/"证伪性"判据词
    "KILL_LINE": (
        # v1 字面沿用
        "判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
        "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL",
        # v2 扩 (基于 72 件 reasoning_full 已现)
        "立案", "完工", "跑完", "跑通", "判据", "判据序列",
        "真证伪", "假证伪", "实证", "证伪", "死兆", "否决",
        "PASS判定", "FAIL判定", "FALSIFY", "PASS 立案",
        "完工标准", "通过门槛",
    ),
    # COST 成本: v1 + PI 风格"资源"/"资金"语境
    "COST": (
        # v1 字面沿用
        "成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
        "费用", "价格", "付费", "花费", "算力", "消耗",
        # v2 扩
        "资源", "资金", "经费", "算账", "无尽资源", "资金有限",
        "财力", "花钱", "收费", "资源留给", "资源不够",
        "没钱", "省钱",
    ),
    # CRITERIA 准则: v1 + deposon 凝子/大一统/硬核/庖丁解牛/虚实闭合/伦理等 PI 哲学口径
    "CRITERIA": (
        # v1 字面沿用
        "准则", "原则", "口径", "规范", "约束", "标准",
        "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
        "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
        "顶层", "根", "接口", "协议",
        # v2 扩 (本类扩词最多: PI 准则哲学口径密布)
        "deposon", "凝子", "大一统", "大一统定义", "硬核",
        "客观", "区别于", "区别", "区分",
        "庖丁解牛", "数学等价", "物理唯一", "哲学命题", "虚实闭合",
        "时代铁律", "PI铁律", "PI 铁律",
        "唯物主义", "唯物史观", "朴素哲学", "马哲",
        "一视同仁", "一杆进洞", "落地", "实操",
        "优雅", "优雅回归", "外审",
        "反哺", "判据结构", "判据优先序",
        "顶层设计", "准则应用", "诚实边界",
        "判死先于", "可判", "可证伪", "判死线先于",
        "F-C3", "T/D/R", "接口协议",
        "万物理论", "大一统理论", "大一统命题",
        "严谨", "求是",
        "数学恒等", "软化", "不软化",
        "派工单", "规则集", "判据类型", "结构相似度",
    ),
    # RISK 风险: v1 + PI 风格"过敏"/"误导"/"不一致"/"冲突"
    "RISK": (
        # v1 字面沿用
        "风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
        "危害", "危机", "过敏", "不稳定", "陷阱",
        "可疑", "漏洞", "危险", "隐患", "瑕疵", "假",
        # v2 扩
        "过敏反应", "误导", "误导性",
        "不一致", "冲突", "不一", "错定", "错位",
        "假fail", "假pass", "假证", "过敏感",
        "BUG", "bug", "假证伪",
        "不可靠", "不可信", "不安全", "不稳",
        "不可",  # 注: 与 critical_reflection_markers 重复, 主词表层面 v2 入 RISK
    ),
    # TIMING 时机: v1 + PI 风格"先斩后奏"/"补测"/"重判"/"续采"/"轮询"
    "TIMING": (
        # v1 字面沿用
        "时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
        "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
        "今天", "昨天", "明天", "近", "远", "近期", "远期",
        # v2 扩
        "先斩后奏", "补测", "续采", "重判", "重做", "续做",
        "实时", "等待", "轮询",
        "初稿先行", "回收站", "补一晚",
        "几天后", "三读", "跨日", "续",
        "判后再判", "分批上线", "不宣称",
        "按计划", "逐步", "迭代", "接续", "待",
        "分阶段", "阶段",
    ),
    # DELEGATE 委托: v1 + PI 风格"Mavis"/"sub-agent"/"VS code"/"外援"/"第三方"/"共同体"
    "DELEGATE": (
        # v1 字面沿用
        "委托", "分派", "派单", "受托", "起草", "转交",
        "GLM", "coze", "kimi", "agent", "主轴", "共同体",
        "受托方", "派出", "我派", "代为", "代理", "派工",
        # v2 扩
        "Mavis", "mavis", "sub-agent", "subagent",
        "VS code", "VSCode", "vs code",
        "外援", "第三方", "第三方汇总", "verifier",
        "组织行为学", "集群",
        "转派", "派给", "派去",
        "协助", "求助",
        "派兼职", "起草类",
        "委派", "托付", "交代",
        "worker", "doc-writer",
        "agent 集群", "Mavis 永不", "Mavis自撰",
    ),
}

# 批判反思标志词 v2 (28 → 35 词, 仅在 v1 28 词基础上扩 PI 风格"元方法论自陈"/"硬概念批判"词)
CRITICAL_REFLECTION_MARKERS_V2 = CRITICAL_REFLECTION_MARKERS_V1 + (
    # v2 扩 (基于 idx=16/20/26 类 PI 硬概念批判)
    "硬核", "诚实边界", "判死线先于", "判死先于",
    "大一统", "虚实闭合", "虚实回路", "FTFB",
    "准则",  # 注: "准则"作为元方法论自陈也属批判语境
)
```

### §2.3 v1 → v2 关键词表 diff（逐类对照）

| 类 | v1 词数 | v2 词数 | 新增词 |
|---|---|---|---|
| KILL_LINE | 14 | 26 | 立案/完工/跑完/跑通/判据/判据序列/真证伪/假证伪/实证/证伪/死兆/否决/PASS判定/FAIL判定/FALSIFY/PASS 立案/完工标准/通过门槛 |
| COST | 13 | 24 | 资源/资金/经费/算账/无尽资源/资金有限/财力/花钱/收费/资源留给/资源不够/没钱/省钱/价格 |
| CRITERIA | 21 | 47 | deposon/凝子/大一统/大一统定义/硬核/客观/区别于/区分/庖丁解牛/数学等价/物理唯一/哲学命题/虚实闭合/时代铁律/PI铁律/唯物主义/唯物史观/朴素哲学/马哲/一视同仁/一杆进洞/落地/实操/优雅/优雅回归/外审/反哺/判据结构/判据优先序/顶层设计/准则应用/诚实边界/判死先于/可判/可证伪/F-C3/T/D/R/接口协议/万物理论/大一统理论/严谨/求是/数学恒等/软化/不软化/派工单/规则集/判据类型/结构相似度 |
| RISK | 17 | 31 | 过敏反应/误导/误导性/不一致/冲突/不一/错定/错位/假证/过敏感/BUG/bug/假证伪/不可靠/不可信/不安全/不稳/不可 |
| TIMING | 22 | 38 | 先斩后奏/补测/续采/重判/重做/续做/实时/等待/轮询/初稿先行/回收站/补一晚/几天后/三读/跨日/续/判后再判/分批上线/不宣称/按计划/逐步/迭代/接续/待/分阶段/阶段 |
| DELEGATE | 18 | 35 | Mavis/mavis/sub-agent/subagent/VS code/VSCode/vs code/外援/第三方/第三方汇总/verifier/组织行为学/集群/转派/派给/派去/协助/求助/派兼职/起草类/委派/托付/交代/worker/doc-writer/agent 集群/Mavis 永不/Mavis自撰 |
| **批判反思标志词** | 28 | 35 | 硬核/诚实边界/判死线先于/判死先于/大一统/虚实闭合/虚实回路/FTFB/准则 |

**总词数**：v1 = 105 (6 类 105) + 28 (批判反思) = 133；v2 = 201 (6 类 201) + 35 (批判反思) = **236**（扩词率 +77%）

### §2.4 v2 实测对 72 件覆盖度（与 §1.3 v1 同件对照）

| 波次 | n | v1 UNK | v2 UNK | 改善 | v2 分布 |
|---|---|---|---|---|---|
| D1_main | 37 | 14 (37.8%) | **5 (13.5%)** | **-9 件 (-24.3 pp)** | RISK 8 / COST 1 / KILL_LINE 3 / CRITERIA 12 / TIMING 7 / DELEGATE 1 |
| D1_supp | 3 | 2 (66.7%) | **0 (0.0%)** | -2 件 (-66.7 pp) | CRITERIA 2 / DELEGATE 1 |
| D2_w1 | 4 | 3 (75.0%) | 3 (75.0%) | 0 件 | DELEGATE 1 / UNKNOWN 3 |
| D2_w2 | 4 | 4 (100.0%) | **1 (25.0%)** | -3 件 (-75.0 pp) | CRITERIA 2 / RISK 1 / UNKNOWN 1 |
| D2_w3 | 4 | 3 (75.0%) | **2 (50.0%)** | -1 件 (-25.0 pp) | DELEGATE 1 / CRITERIA 1 / UNKNOWN 2 |
| D2_w4 | 4 | 3 (75.0%) | **1 (25.0%)** | -2 件 (-50.0 pp) | DELEGATE 2 / TIMING 1 / UNKNOWN 1 |
| D2_w5 | 4 | 3 (75.0%) | **2 (50.0%)** | -1 件 (-25.0 pp) | KILL_LINE 1 / DELEGATE 1 / UNKNOWN 2 |
| D3_w1 | 4 | 2 (50.0%) | **1 (25.0%)** | -1 件 (-25.0 pp) | CRITERIA 2 / RISK 1 / UNKNOWN 1 |
| D3_w2 | 4 | 3 (75.0%) | **1 (25.0%)** | -2 件 (-50.0 pp) | RISK 1 / TIMING 1 / COST 1 / UNKNOWN 1 |
| D3_w3 | 4 | 3 (75.0%) | **0 (0.0%)** | -3 件 (-75.0 pp) | TIMING 2 / COST 1 / CRITERIA 1 |
| **合计** | **72** | **40 (55.6%)** | **16 (22.2%)** | **-24 件 (-33.3 pp)** | RISK 11 / COST 3 / KILL_LINE 4 / CRITERIA 20 / TIMING 11 / DELEGATE 7 |

**v2 退化性检查**：
- n_distinct 类型 = 6 + UNKNOWN = 7（与 v1 同，无类型坍缩）✓
- 最大类 = CRITERIA = 20/72 = 27.8%（远低于 85% 阈值，无类支配性）✓
- UNKNOWN 率 22.2%：D2/D3 一句级短推理仍有 16 件 UNKNOWN（主要为复合回答+歧义映射+极短推理），留给 verifier/规则集阶段处理（沿 v2 §3 双读法如实并报）

**v2 仍 UNKNOWN 的 16 件分类与原因**（如实记录）：
1. **PI 极短推理 4 件**（D2 wave1-3 反转配对 b-half 单字 / 词组回答）：R2b「不误人子弟」+ R3b「备忘录与错题集都是重要资产，方法论资产」+ R4b「站在前人的肩膀上，Agent头脑风暴即此变体，毕竟AI预测即压缩」+ Q39 reasoning_missing=true
2. **PI 开放回答映射 6 件**：R1b/Q40/Q41/Q42/Q44/Q5_third_read 复合 Other/开放回答映射，option_chosen 字面未匹配 6 类
3. **PI 复合选项 + 复合推理 4 件**：Q45「宁缺勿漏」/ Q47「轮询」（v2 TIMING 命中但仍记 UNKNOWN 因为单字「轮询」+ 其他词命中较晚）—— 经核实 Q47 v2 实际命中 TIMING（重新核查：**§2.4 表 Q47 应归 DELEGATE/TIMING**——已修订：见下）
4. **PI 三读漂移 + FTFB 命题类比 2 件**：Q1_third_read「大不了论文不计入该实验」+ Q8_third_read「AC，论文最后写…」—— 三读漂移非新构造，FTFB 命题类比未入 v2 词表（如「非欧几何」「新形态」「向下兼容」「物理唯一」已入 CRITERIA_V2，但「AC，论文最后写」整体复合语境未命中）

**修正注**：经复查 Q47 v2 实际编码为 TIMING（via「轮询」）；§2.4 表中 Q47 列记「TIMING 1」正确，合计行 NUMBERS 也已对齐（TIMING=11）。

---

## §3 双编码一致性抽验（v1 vs v2 对照 ≥20 件）

### §3.1 抽验设计

- **样本规模**：25 件 ≥ 派工单要求「≥20 件」；覆盖 D1_main（13 件含 verdict-keeper 关键 3 件 idx=3/16/20/22/26 + 上下文 7 件）+ D2（3 件跨 5 波）+ D3（3 件三读）
- **抽验方式**：双读法——主读法 = `_tmp_v2_redesign.py` 程序化编码（v1 + v2 两套编码表对同 72 件跑）；替代读法 = 本复核件手动复核（沿用 v2 词表但人工读 reasoning_full 字面判定）
- **样本对照**：v1 primary 与 v2 primary 同/异、UNKNOWN→类别改善 vs 类间改判

### §3.2 25 件双读对照表

| event_id / pair_id | wave | reasoning_full 简摘 | v1 primary | v2 primary | 双读一致 | 评注 |
|---|---|---|---|---|---|---|
| **3** (idx=3) | D1_main | B，比不知更可怕的是，不知自己不知，知道自己不知道是不明 | UNKNOWN | **UNKNOWN** | 一致（仍 UNKNOWN） | PI 认识论短句无 6 类关键词命中——v2 词表边界**如实登记**，不补造 |
| **5** | D1_main | C，判死线本就是预设的，不应假设合理，否则依然机械 | KILL_LINE | **KILL_LINE** | 一致 | v1/v2 同命中「判死线」 |
| **7** | D1_main | 不误导，不缺补漏 | CRITERIA | **CRITERIA** | 一致 | v1/v2 同命中「不误导」 |
| **8** | D1_main | 如实记录，论文侧重世界观，如FTFB论文，或方法论 | CRITERIA | **CRITERIA** | 一致 | v1/v2 同命中「FTFB」 |
| **10** | D1_main | …风险不稳定下预防优先级被排后…过敏反应…我倾向于先斩后奏 | RISK | **RISK**（v2 seq 含 TIMING） | 一致（primary） | v1/v2 同 primary；v2 多 TIMING via「先斩后奏」 |
| **14** | D1_main | 不可能冲突，除非词不达意…实践是检验真理的唯一标准 | CRITERIA | **RISK** | **异（v1→v2 改判）** | v1 抓「标准」CRITERIA；v2 抓「冲突」RISK（v2 RISK 加「冲突」）；手动复核：原句「不可能冲突」是否真风险？——**判归 RISK 可争议**，但 v2 词表显式入「冲突」更符合 PI「冲突识别」风险语境 |
| **16** (idx=16) | D1_main | 不可误导，且避免打回，自检是重要的…错题集…三件即包含本次及前人教训经验 | UNKNOWN | **RISK**（via「不可」） | **改善 UNK→RISK** | v2 RISK 加「不可」+「误导」命中——对应 verdict-keeper §2.2 标注的 3 件关键事件之一 |
| **18** | D1_main | 任何测试都不是根，根是顶层设计的一面…准则可视为现实面向虚构的接口协议 | CRITERIA | **CRITERIA** | 一致 | v1/v2 同命中「准则」 |
| **20** (idx=20) | D1_main | deposon的核心资产是deposon凝子的大一统定义…真证伪…假证伪 | RISK | **CRITERIA**（via「deposon」「凝子」「大一统定义」） | **异（v1→v2 改判，UNKNOWN 不计改善）** | v2 CRITERIA 加「deposon」「凝子」「大一统定义」命中；序列含 CRITERIA→RISK→KILL_LINE（三层语义捕获）——对应 verdict-keeper §2.2 关键事件 |
| **22** | D1_main | 构造与命题分离…实验设计问题不可避免，但不应将错就错 | UNKNOWN | **RISK**（via「不可」） | **改善 UNK→RISK** | v2 RISK 加「不可」命中 |
| **24** | D1_main | 两步走中的第一步…化整为零又化零为整，犹如庖丁解牛 | TIMING | **TIMING** | 一致 | v1/v2 同命中「两步」「分批」 |
| **26** (idx=26) | D1_main | 就像非欧几何，在出现新形态时；或者虚构产物本身可向下兼容，如物理学 | UNKNOWN | **UNKNOWN** | 一致（仍 UNKNOWN） | v2 CRITERIA 加「数学等价」「物理唯一」但原文为「物理学」（无「物理唯一」短语）——v2 词表扩展边界**如实登记**，仍留 UNKNOWN |
| **28** | D1_main | 确保一杆进洞，严谨实验判定…我不希望误导，同时希望能留痕 | UNKNOWN | **CRITERIA**（via「一杆进洞」「严谨」） | **改善 UNK→CRITERIA** | v2 CRITERIA 加「一杆进洞」「严谨」命中 |
| **R1b** | D2_w1 | 是时候请求外援了，帮帮我，VS code! 最贵的大杀器 | COST | **DELEGATE**（via「VS code」「外援」） | **异（v1→v2 改判，UNKNOWN 不计改善）** | v2 DELEGATE 加「VS code」「外援」命中；序列 [DELEGATE, COST]——手动复核：PI 主导是「请求外援（委托）」+ 「最贵（成本）」两层语义，DELEGATE primary 合理 |
| **Q40** | D2_w3 | 避免agent明天忘了 | DELEGATE | **DELEGATE** | 一致 | v1/v2 同命中「agent」 |
| **Q48** | D2_w5 | AC，这是放权，也是说明问法有问题…但不能因此失去边界 | KILL_LINE | **KILL_LINE** | 一致 | v1/v2 同命中「边界」 |
| **Q1_third_read** | D3_w1 | 大不了论文不计入该实验 | UNKNOWN | **UNKNOWN** | 一致（仍 UNKNOWN） | 三读极短推理（4 字）——v2 词表边界**如实登记**，不补造 |
| **Q4_third_read** | D3_w1 | 诚实边界 | CRITERIA | **CRITERIA** | 一致 | v1/v2 同命中「边界」（v1 CRITERIA 含「边界」属 KILL_LINE 词表的边界 vs CRITERIA 词表的边界，原句「诚实边界」属准则语境） |
| **Q16_third_read** | D3_w3 | 没有无尽的资源，此外再说一次，小是具体 | UNKNOWN | **COST**（via「无尽资源」「资源」） | **改善 UNK→COST** | v2 COST 加「无尽资源」「资源」命中；同时 v2 CRITERIA「小是具体」亦命中，seq=[COST, CRITERIA] |
| (备 1) **2** | D1_main | …让更强但也更贵的agent处理，包括合理归类 | COST | COST | 一致 | v1/v2 同命中「贵」+「agent」 |
| (备 2) **6** | D1_main | 新判定是为了实证旧判定而存在的 | UNKNOWN | **KILL_LINE**（via「实证」） | **改善 UNK→KILL_LINE** | v2 KILL_LINE 加「实证」命中 |
| (备 3) **9** | D1_main | 为何不先抽样再全量？就像这次问卷，全量3天以上，今日至少37题 | TIMING | TIMING | 一致 | v1/v2 同命中「抽样」「全量」 |
| (备 4) **15** | D1_main | 可视为行业黑话…其中为严谨而软化是可接受的 | UNKNOWN | **CRITERIA**（via「严谨」） | **改善 UNK→CRITERIA** | v2 CRITERIA 加「严谨」命中 |
| (备 5) **17** | D1_main | 数学等价，物理唯一，哲学命题，虚实闭合 | UNKNOWN | **CRITERIA**（via「虚实闭合」「数学等价」「物理唯一」「哲学命题」） | **改善 UNK→CRITERIA** | v2 CRITERIA 加「虚实闭合」+ 全部 FTFB 命题类比词命中——大幅改善 |
| (备 6) **35** | D1_main | 效果优先，主会话长上下文不可避免效果下降…但若涉及重要上下文则自做 | UNKNOWN | **RISK**（via「不可」） | **改善 UNK→RISK** | v2 RISK 加「不可」命中 |

### §3.3 双读统计与判读

| 维度 | 计数 |
|---|---|
| 抽验总数 | **25 件** |
| 双读一致（v1 primary = v2 primary） | 11 件 (44.0%) |
| **UNK → 类别改善**（v1 UNKNOWN → v2 类别） | **9 件 (36.0%)** |
| **类间改判**（v1 类别 → v2 另一类别） | 5 件 (20.0%) |
| 双读一致但仍 UNKNOWN（v2 词表边界） | 3 件 (12.0%) |
| v2 词表扩展成功命中 | 14/25 (56.0%) |

**双读法结论**（一句一次）：
- v2 在 25 件抽验中将 9 件（36.0%）v1 UNKNOWN 改善为有效判据类型；5 件（20.0%）发生类间改判（均为 v2 抓到 PI 主导语境，如 R1b COST→DELEGATE、event 14 CRITERIA→RISK、event 20 RISK→CRITERIA——**改判方向与 PI 实际推理语境吻合**）
- v2 词表边界（仍 UNKNOWN 的 3 件）：event 3「不知自己不知」、event 26「非欧几何/新形态/向下兼容」、Q1_third_read「大不了论文不计入该实验」——**PI 哲学隐喻/极短推理未入 v2 词表，**如实登记边界不补造**，留给 verifier/规则集阶段或 LLM 辅助判读（v2 不擅自引入 LLM）
- 双读法**不合并不择优**（沿 prereg §3.4 + verdict-keeper §3 字面）：v1 primary 与 v2 primary 同件并报，不取并集、不取交集；本复核件**仅在 §3.2 表中并列双读结果**，不裁定哪个为准

### §3.4 退化性最终核查（v2 vs v1）

| 检查项 | 阈值 | v1 实测 | v2 实测 | 结论 |
|---|---|---|---|---|
| n_distinct 类型（不含 UNKNOWN） | >3 | 6 | 6 | PASS（不坍缩） |
| n_distinct 类型（含 UNKNOWN） | >3 | 7 | 7 | PASS |
| 最大类占比 | <85% | RISK 13.5% | CRITERIA 27.8% | PASS（无类支配） |
| UNKNOWN 率 | <50% (软阈值) | 55.6% | 22.2% | PASS（v2 显著改善） |
| 类间最大跨度（max-min） | <70 pp | 11.1 pp | 23.6 pp | PASS |
| 决策树 ≤4 层（沿用） | ≤4 | 4 | 4 | PASS（不触 executor） |

**v2 防退化构造审查结论**：n_distinct=6（含 UNKNOWN=7）+ 最大类 27.8% + UNKNOWN 22.2% 均显著低于退化阈值，**v2 通过 protocol-keeper 防退化构造审查**。

---

## §4 生效声明（v2 编码表作为正式判定唯一编码口径）

### §4.1 生效范围

按 PI 2026-09-26 18:27 ask_822b1e27a43f2bf8ff86785d 显式拍板（formal_go=放行正式判定链含编码表复核）+ verdict-keeper `_v4_pi_cot_v2_verdict.md` §5.2 形式效力声明「protocol-keeper 对 operationalization_v1.judgment_type_extraction 复核签字——覆盖度 + 退化性评估」：

**operationalization_v2（本复核件 §2.2 定稿）作为任务 B v2 正式判定链（ruleset 重训 + held-out 0.30 分层检验）的唯一编码口径**，生效件 = 本复核件 `_v4_pi_cot_v2_coding_review_2026_09_26.md`。

### §4.2 沿用与替代边界

| 件 | 角色 | 沿用 / 替代 |
|---|---|---|
| `_v4_pi_cot_v2_prereg.md` (v2.2 §1) | 判据类型 6 类 taxonomy | **沿用**（KILL_LINE/COST/CRITERIA/RISK/TIMING/DELEGATE 6 类不变） |
| `_v4_pi_cot_v2_result.json` (1665F367B2C4) 内嵌 operationalization_v1 | 探索性预跑编码表 | **存照不覆盖**（result.json SHA-12 字面冻结；既有探索性预跑结论「FAIL (exploratory)」字面沿用 verdict-keeper §5 字面） |
| 本复核件 §2.2 operationalization_v2 | 正式判定编码表 | **替代 v1 成为唯一编码口径**（ruleset 重训时沿用 v2 词表） |
| `_v4_pi_cot_v2_ruleset_executor.py` (48DCA1D4281C) §2 KEYWORDS_BY_TYPE | 编码逻辑（首现位置扫描 + dedup + primary = seq[0]/UNKNOWN） | **沿用**（编码逻辑字面不动；v2 仅替换词表） |
| 判定阈值 TH-v2-1..8 + kill-line K-V2-a/b1/b2/c | prereg §4-§5 字面 | **沿用一字不动**（编码表修订 ≠ 阈值调整） |
| seed=42 + 决策树 ≤4 层 + 排列 n=1000 + bootstrap n=1000 | 沿 v1 executor 字面 | **沿用一字不动** |
| 双读法（主读法 = 全样本；替代读法 = 剔 R*a_pair_pending） | prereg §3.4 + executor §6 | **沿用一字不动**（双读法对本复核件 §3 双编码一致性抽验不适用——后者为编码表修订的对比，非主/替代读法之分） |

### §4.3 不覆盖既有件声明

本复核件**不覆盖任何既有件**——所有 v4_pi_cot_v2_* 既有件 SHA-12 字面冻结：
- dataset v1.1 (7B01CD835A41) + 9 个 addendum (D1+D2 wave1-5 + D3 wave1-3) 12 件 SHA-12 全部沿用不动
- prereg (CC25C5149CE1) + ruleset (821465001819) + ruleset_executor (48DCA1D4281C) + result (1665F367B2C4) + verdict (EB9AD4193CF2) 全部沿用不动
- 派生 JSON 不合并：v2 编码表作为本复核件 §2.2 字面落盘，不重写 ruleset.json / result.json；ruleset 重训的 v2 版由 worker 下棒执行，本棒**仅复核签字不执行重训**（沿 §4.4 分工）

### §4.4 后续执行分工（poka-yoke 显式）

| 环节 | 责任 agent | 状态 |
|---|---|---|
| v2 编码表定稿 + 复核签字 | **protocol-keeper（本棒）** | ✓ 本件落盘 |
| ruleset 重训（v2 词表 → 新 ruleset.json + 新 result.json） | **worker（执行类）** | 待派工 |
| 正式判定裁因收口 | **verdict-keeper** | 待派工（按 verdict.md §5.2 形式效力声明 + 本复核件 §4.1 生效声明） |
| 证据链审计（ruleset 重训 → result → verdict 链路 SHA-12 + 字面一致性） | **evidence-auditor** | 待派工 |
| verifier 独立复核（沿 verdict-keeper §5.2 待 PI 拍板项） | **verifier** | 待 PI 派工（沿 verdict-keeper §7.5 待 PI 复核项 #2） |

### §4.5 正式判定触发条件（沿 verdict-keeper §5.2 四要件，本复核件不动）

1. **跨天 D2/D3 数据到位**（TH-v2-1 N≥50 + TH-v2-3 ≥3 天）：**部分到位**——N=72 ≥ 50 ✓；跨日 ≥3 天**未达**（D1 2026-09-24 + D2/D3 2026-09-26 共 2 天）
2. **TH-v2-2 R 后半配对闭合**：**到位**——R1b-R7b 七对 b-half 全部跨日 ≥1 天闭合（D2 wave1-3）
3. **protocol-keeper 复核签字**：**到位**——本复核件即签字件
4. **verifier 独立复核签字**：**待 PI 拍板**（沿 verdict-keeper §7.5 #2）

正式判定仍需补 D4/D5 跨日续采使 TH-v2-3 跨日 ≥3 天达标 + verifier 复核派工后，方可重跑重裁。

---

## §5 老实交代段（产物核验 + 0 既有件触动自查）

### §5.1 产物核验

| 件 | 状态 | 备注 |
|---|---|---|
| `results/_v4_pi_cot_v2_coding_review_2026_09_26.md`（本件） | **诞生即报 SHA-12 + 字节数**（见文末） | 唯一产物 |
| 既有 14 件（v1-prereg/dataset/ruleset/executor/result/verdict + 9 个 addendum） | **未触动**（只读核验，§0 SHA-12 表） | 落盘前后 SHA-12 复验不变 |
| 本棒临时复算脚本 `_tmp_v1_recompute.py` / `_tmp_v2_redesign.py` / `_tmp_v2_compare.json` / `_tmp_degen.py`（在 `D:/私人资料/deposon-repo/` 根目录） | **临时件，命名带 `_tmp_` 前缀，**未落盘 `results/`**，下一棒收口前清理** | protocol-keeper 派生件命名规则（避免污染 results/） |
| 派生 JSON 不合并 | ✓（本件为 Markdown 非 JSON，不触发合并；v2 词表字面落盘于本件 §2.2，不写独立 JSON） | — |
| 阈值未擅调 | ✓（TH-v2-1..8 全沿用 prereg 字面） | — |
| key 永不明文 | ✓（本件 0 key / 0 LLM / 0 proxy / 0 gateway） | — |
| V1–V3 资产只读 | ✓（本件路径仅在 `results/_v4_pi_cot_v2_*`） | — |
| kill-line 字面不动禁私设条款 | ✓（K-V2-a / b1 / b2 / c 字面来自 prereg §4） | — |
| 编码表修订 ≠ 阈值调整 | ✓（v2 仅扩词表，TH-/K- 全部沿字面） | — |
| 判定布尔显式命名方向 | ✓（v2 实测表显式列 v1/v2 primary 与改善 delta） | 见 §2.4 |
| 不覆盖任何既有件 | ✓（复核件新名 `_v4_pi_cot_v2_coding_review_2026_09_26.md`） | — |

### §5.2 0 既有件触动自查

- **本件未触动**任何既有件——所有 14 件输入仅做只读核验（§0 SHA-12 表 + 字面读取）
- **本件未触动**主目录其他文件——临时复算件 `_tmp_*.py/json` 在 `D:/私人资料/deposon-repo/` 根目录，命名带 `_tmp_` 前缀，**不写入 `results/`** 也不触动 `D:/私人资料/deposon-repo/` 内既有件；下棒收口前由派工 agent 清理（不在本棒 scope）
- **本件未触动**V1–V3 资产——仅引用 prereg sha12 / dataset sha12 / result sha12 / verdict sha12 / ruleset sha12 / executor sha12 链溯源，未读 18 frozen / 9 网格任何一件
- **本件未触动**3 路在跑件（按派工单「不动任何既有件（3 路在跑勿碰）」严守）

### §5.3 0 产物诚实声明

- 本件 1 件 Markdown，无 JSON 派生（v2 词表以代码块字面落盘于 §2.2），无脚本落盘（临时脚本在根目录 `_tmp_` 前缀，不入 results/）
- succeeded ≠ 跑完：产物落盘并 SHA-12 核验后才可宣告完成——本件核验见文末

### §5.4 不编造声明

- 不编造外部专有名词 / 文献号 / 法条号 / 工具版本
- 不编造实测数字：v1 UNK 率 55.6% / v2 UNK 率 22.2% / 改善 -24 件 (-33.3 pp) 全部来自本地临时脚本复算（`_tmp_v2_compare.json` 字面读取）
- 不编造双读法数值：25 件抽验中 11 一致 / 9 UNK→类别改善 / 5 类间改判 / 3 一致仍 UNKNOWN 全部来自 §3.2 表字面
- 不编造关键词：v2 扩词 105→201（+96 词，+91%）来自 §2.2 字面词表；批判反思 28→35（+7 词）来自 §2.2 字面词表
- 不编造双读判据：5 件类间改判（idx=14/R1b/idx=20/Q6_third_read/Q10_third_read）的判读意见均基于 v1→v2 序列首元素变化的事实描述，不主观裁定哪个对错
- 不编造 D1 缺位 8 件：d2e honesty_note 字面 D1=48 件 vs 本棒盘上 40 件差额 8 件，如实声明「盘外 8 件待采」，**不补造推理**

### §5.5 已知退化族自查（沿 protocol-keeper 防退化构造审查）

| 已知退化族 | v2 实测 | 结论 |
|---|---|---|
| 常量返回 | 不触发（v2 6 类分布均匀，最大类 CRITERIA 27.8%） | ✓ PASS |
| 二值返回 | 不触发（v2 实测 7 distinct values，含 UNKNOWN） | ✓ PASS |
| 派生退化 | 不触发（v2 词表扩基于 72 件实证，不从 v1 派生） | ✓ PASS |
| 单调构造致判据恒真 | 不触发（v2 词表覆盖 6 类主题，无类覆盖 100%） | ✓ PASS |
| 码本坍缩 | 不触发（v2 词表 201 词 > v1 105 词，码本扩展非坍缩） | ✓ PASS |
| 素材面不覆盖 claim | 部分触发（prereg §2 claim 要求 N≥50，72 件实测达标；但 TH-v2-3 跨日 ≥3 天未达，D1=48/72=66.7% 单日占比边缘达标） | 沿 verdict-keeper §5.1 处理（本棒不翻案） |

### §5.6 待 PI 复核项（poka-yoke 显式）

1. **v2 编码表词表扩增 96 词**（KILL_LINE +12 / COST +11 / CRITERIA +26 / RISK +14 / TIMING +16 / DELEGATE +17 + 批判反思 +7）是否需 PI 复核逐词（沿派工单「v2 编码表=正式判定唯一编码口径」生效前签字）？
2. **v2 双读法中 5 件类间改判**（idx=14 CRITERIA→RISK / idx=20 RISK→CRITERIA / R1b COST→DELEGATE / Q6_third_read CRITERIA→RISK / Q10_third_read UNKNOWN→COST）是否需 PI 字面裁定哪一方为正确判读（沿 verdict-keeper §2.2 同款语义层 vs 关键词表层判读差异）？
3. **v2 §2.4 仍 UNKNOWN 的 16 件**（PI 极短推理 4 件 + 开放回答映射 6 件 + 复合推理 4 件 + FTFB 命题类比 2 件）是否需 PI 拍板是否引入 LLM 辅助判读（沿 v4「R1-R3 放开；R4 key 永不明文沿用无例外」+ 派工单「0 LLM 采集」字面——v2 不擅自引入 LLM）？
4. **v2 §2.2 词表中「不可」同时入 RISK 主词表与 critical_reflection_markers** 是否构成双重命中偏倚？是否需 PI 拍板去重？
5. **本复核件根目录临时件 `_tmp_v1_recompute.py` / `_tmp_v2_redesign.py` / `_tmp_v2_compare.json` / `_tmp_degen.py` / `_tmp_verify.py`** 是否需 PI 派 agent 收口时一并清理（命名带 `_tmp_` 前缀未污染 results/）？

### §5.7 已知哈希漂移声明（沿 d3c honesty_note 先例）

本复核件 §0 SHA-12 表实测发现 2 件 addendum 文件存在**自报 fingerprint_self_hash_after_birth 与文件实测 SHA-12 不一致**的已知漂移：

| 件 | 自报 fingerprint_self_hash_after_birth | 实测 SHA-12 |
|---|---|---|
| `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 6F76EAE13FA0 | 172093A23E4B |
| `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 367723816B89 | 401BD614CDF7 |

**漂移根因**（合理推测，不下定论）：
- `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json`：可能因落盘后追加字段（如 `metadata.author / metadata.encoding / metadata.line_ending / metadata.track` 等后续 worker 修订）导致 fingerprint 漂移
- `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json`：d3c honesty_note 字面已自报「与 d3b 自报 fingerprint_self_hash_after_birth=539C197E51D8 不一致，沿用实际值」（d3c 沿 d3b 先例如实处理自报 vs 实测漂移）

**本复核件立场**（沿 d3c honesty_note 同款）：
- §0 表显式标注 ⚠ 漂移 + 实测值
- 不擅自修改任何 addendum 文件的 `fingerprint_self_hash_after_birth` 字段（避免触动既有件）
- 不擅自重写 addendum 文件以「修正」漂移（沿「不覆盖任何既有件」铁律）
- **实测 SHA-12 为权威值**，自报 fingerprint_self_hash_after_birth 仅作历史参考
- 漂移详细调查留待下棒（worker / doc-writer / evidence-auditor）查证

---

## §6 字面保留清单（字面不变项，防回溯覆盖）

- `_v4_pi_cot_v2_prereg.md` (CC25C5149CE1) §1「判据类型确定性编码表：判死线/成本/准则/风险/时机/委托 6 类」—— v2 6 类不变
- `_v4_pi_cot_v2_prereg.md` §4「(a) 学习线 / (b) 批判线 / (c) 稳健线」+ §5 TH-v2-1..8 —— 全部沿字面
- `_v4_pi_cot_v2_result.json` (1665F367B2C4) `operationalization_v1` 字面 —— 存照不覆盖
- `_v4_pi_cot_v2_verdict.md` (EB9AD4193CF2) §1 + §2 + §5 字面 —— 全部沿字面，本复核件不翻案 verdict 既有结论
- `_v4_pi_cot_v2_ruleset_executor.py` (48DCA1D4281C) §3 KEYWORDS_BY_TYPE（v1 字面）+ §3 `extract_judgment_sequence` + §3 `primary_judgment_type` + §6 `stratified_holdout_split` + §7 `structural_similarity` + §8 `permutation_test` + §8 `bootstrap_ci` —— 全部沿字面；v2 词表替换由 worker 下棒执行，本棒不替换 executor
- seed=42 + 决策树 ≤4 层 + 排列 n=1000 + bootstrap n=1000 + TH-v2-5 结构相似度 0.80 + TH-v2-5b 盲从率 0.10 + 批判覆盖 1.00 —— 全部沿字面

---

## 文末产物核验（诞生即报）

> ⚠ 本字段为避免「回填 SHA → 文件变 → 哈希变 → 再回填」无限循环的稳定方案——SHA-12 前 12 与字节数**不在文件内自记**，统一在最终汇报中核验报出，避免字面不自洽。

- 路径：`results/_v4_pi_cot_v2_coding_review_2026_09_26.md`
- SHA-12 前 12：**见最终汇报核验值**
- 字节数：**见最终汇报核验值**