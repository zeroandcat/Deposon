# 增补实验设计提案（KIMI-K3）
## P-L v2 缺口重测 · D+0.5 阶段 · 响应 Mavis 邀请函 2026-09-17 09:33

**提交方**:KIMI-K3 | **日期**:2026-09-17 | **截止响应**:14:00 CST 前
**立场声明**:本提案不预设任何拟结论;四象限结果(=1 / ∈(0.5,0.95) / <0.5 / 退化)均为合法产出,禁止 reassign。

---

## §1 Backbone 选择(2 个,主 + 备)

| 序 | Backbone | 通道 | 与 5 制品 baseline 的内部差异 | 选它的理由 |
|---|---|---|---|---|
| **主** | **Qwen3**(阿里) | 火山方舟 coding-plan(ark-* key,runtime 读取) | tokenizer 词表与切分边界不同系;预训练语料配比不同;RLHF 管线独立 | 与现有 9 model 主源中的 doubao/deepseek/glm/minimax/kimi 均不同族,内部差异最大且国内可直连 |
| **备** | **Mistral Large 2** | OpenRouter(非 OpenAI/Anthropic/Google,合规) | 欧洲系预训练 + 独立 tokenizer + 不同指令微调分布 | 若 Qwen3 仍 Spearman≥0.95,跨洲不同系 backbone 提供第二次破局机会 |

**不选** DeepSeek V4 作主 backbone:deepseek-v4-flash/pro 已在 9 model 主源内,同族架构(MLA)相似性高,破局增量小。MiniMax M3 仅对照,不入主测(沿邀请函)。

## §2 同序单调破局方法(真破局,非 pass-through)

**机制声明**:prompt format 与评分 scale 与 baseline **逐字节保持一致**(否则就是邀请函禁止的换皮)。破局只来自 backbone 内部差异,三条可检验的传导链:

1. **能力剖面错位(cell-level capability profile mismatch)**:不同预训练配比 → GSM8K(算术链)与 StrategyQA(隐式常识)的逐 cell 成功率模式不同 → cell 难度排序在两个 backbone 间重排。这是 Spearman 的主项。
2. **tokenizer 边界差异**:同一 prompt 文本在不同 tokenizer 下的 token 数与切分点不同 → 等效任务难度逐 cell 微移 → 边缘 cell(成功率 0.3–0.7 带)的排序抖动最大。
3. **长上下文衰减差异**:cell 内 prompt 长度不一,不同 backbone 的有效上下文衰减曲线不同 → 长 cell 的相对难度排序位移。

**退化防线(本提案新增,邀请函未列)**:若所选 cell 在 baseline 侧准确率过高(天花板)或过低(地板),秩次大量并列,Spearman 在数学上退化(并列秩恒等相关),会假性复现"=1"。因此 §3 加一条 cell 筛选规则。

## §3 测法(0 LLM 复算层,沿 _verify_15frozen.py 模式)

1. **cell 集**:沿现有 GSM8K + StrategyQA cell 结构,取 **30 cells**;**信息带筛选**:只保留 baseline 5 制品准确率落在 [0.2, 0.8] 的 cell(退化防线;若筛后不足 30,放宽至 [0.15, 0.85] 并在报告披露)。
2. **跑测**:主 backbone 同 prompt 同 scale 跑 30 cells;判分纯规则(GSM8K 数值 exact-match / StrategyQA 布尔匹配),**0 LLM 评判**。
3. **复算层**:每 cell 输出 → SHA-256[0:12] 落证;全流程 hashlib 可复算,兼容 _verify_15frozen 模式;原始响应逐 cell 落盘(新文件,不触 frozen)。
4. **统计**:主指标 Spearman(新 backbone 逐 cell 得分率排序 vs 5 制品 baseline 各排序,5 组 ρ);稳健性副指标 Kendall τ(对并列秩更诚实,防退化带偏)。
5. **副产出**:P-L v2 原 5 制品输出作 baseline 对照,重算其两两 Spearman 以复核"=1 artifact"声明(若 5 制品两两不恒为 1,Trae §6.7 的同序单调解释本身也需修正——如实披露)。

## §4 期望阈值(预登记,计算前锁定)

| Spearman(主 backbone vs baseline 中位数) | 判定 | 后续 |
|---|---|---|
| < 0.95 | data collapse 假设成立(≥95% 置信) | 跑原 R² 拟合,P-L v3 真实数据入 D7 |
| [0.95, 1.0) | 部分破单调 | 启动备选 backbone(Mistral Large 2)补测 |
| = 1.0 或退化(并列秩 >50%) | 同序单调实证 / 测法退化 | 前者 P-L 假设证伪入 §7.2;后者换信息带重筛重测一次,仍退化则判测法死 |

**判死线(机械)**:主+备两 backbone 均 ≥0.95 → P-L 假设正式证伪,本轮即终局,不再追加 backbone。

## §5 风险评估

| 风险 | 等级 | 缓解 |
|---|---|---|
| 火山 coding-plan rate limit(30 cells 连发) | 低 | 串行 + 间隔 2s;失败 cell 重试 3 次后记 MISSING 如实披露,不补造 |
| OpenRouter region gate/TOS | 低 | 仅备选;layer-2 user_id 门控已承认,只调非美系模型 |
| 并列秩退化(天花板效应) | **中** | §3 信息带筛选 + Kendall τ 副指标双保险 |
| frozen 触动 | 零 | 全部产出为新文件(新 runner/新 results/新报告);18 frozen + conservation.py(4bdec2683f06)+ 4 plugin spec + P-G V0/V0.1 + 5 制品 baseline 0 触动,无任何新锚需冻结 |
| key 泄漏 | 零 | ark-* runtime `Path().read_text()`,不入 prompt/落盘/检测规则 |
| 时间预算 | 可控 | 1 backbone × 30 cells ≈ 30–60 min;备选 backbone 同量,15:00–18:00 窗口内可两轮 |

---

## §6 主线上未提及的增补实验设计(KIMI 观察,沿 user 10:53 并入)

以下 7 项均为邀请函未覆盖、但在昨日验收/侦察中实际暴露或仍未闭合的回路。每项附判死线;全部新文件产出,0 触 frozen。

### S1 P-O 陌生人复算回归(captions 缺口已补,回路待闭合)⭐ 零成本
- **背景**:P-O 24/26 PASS 的唯一实错 = `only 0 captions, need 22`;昨日 C 任务已产出 `corpus/v20/index_v2_2026_09_16.json`(22 captions + 3 锚,22/22 链式 PASS)。
- **实验**:P-O runner 指向 index_v2 复跑,预登记预期 26/26。
- **判死线**:复跑仍 <26/26 → captions 修复未达复算层,定位新错项如实披露;不得改 P-O runner 判定逻辑凑合 PASS(那是修饰实验)。
- **成本**:5 分钟,0 LLM。

### S2 排序健康审计(把 §6.7 教训推广到全仓)⭐ 高价值
- **背景**:Trae 发现 P-L v2 的 Spearman=1 是并列/同序单调 artifact;仓内还有多处 Spearman 排序增量声明(≥0.95 标度放大类),从未做过并列秩体检。
- **实验**:0 LLM 扫描全部含 Spearman 声明的结果 JSON/报告,逐一重算并附 tie 比例;凡 tie>30% 且剔除并列后 ρ 跌破声明口径的,标记"退化风险"。
- **判死线**:≥1 项既有声明跌破口径 → 该批声明降级披露(不改历史结论,加体检附注)。
- **成本**:半小时,纯 hashlib+统计。

### S3 0.867 均衡聚类的跨 backbone 复现(蹭 D+0.5 同一趟车)
- **背景**:双源稳健的关键证据 = doubao-seed-2.0-lite 与 glm-5.3 在两源实跑中同落 T_frac=26/30=0.867(results/deposon_game_theory_eval_2026_09_10.json)。
- **实验**:D+0.5 跑 Qwen3 30 cells 时,顺带按同口径算其 T_frac:落入 0.867±0.03 带 = 聚类跨 backbone 复现;落在外 = 聚类可能仅是两模型特例。
- **判死线**:Qwen3 落带外且 60 cells 扩展数据也无新聚类 → "均衡聚类"降级为双模型巧合,如实披露。
- **成本**:零增量(同一批响应,多算一个比值)。

### S4 verifier 双实现差分测试(P-M 反转的方法论化)
- **背景**:P-M 100% 漏检是计数语义反转——同一 verify 函数两种读法。教训:**单实现 verifier 的语义正确性本身未被审计**。
- **实验**:同一 spec(v42_v2 三层)由两方独立实现,对 N≥1000 随机输入(含构造边界例)差分比对,输出分歧率与分歧案例分类。
- **判死线**:分歧率 >0 → 全仓单实现 verifier 结论统一挂"未交叉验证"标记,直到双实现归零。
- **成本**:1 小时,0 LLM;是 keep_the_books 综述"第三方可重算"主张在 verifier 层的直接落地。

### S5 P-J 收敛盆地账(仍开放,重申)
- 61 图 × 状态全穷举 6760 资产上测 replicator dynamics 收敛比例 vs 势博弈度量(Spearman);判死线 |ρ|<0.3 则死定理定量遗产路线关闭。沿 KIMI 7 方向原文。

### S6 P-N 曲率×势博弈耦合(口径修正后仍开放)
- P-I 已判死,但死的是"曲率作为审计探针(AUC 用途)";**耦合叙事(d_H 是否比 d_E 更预测最优响应吸引)是另一个可判定命题**,不因 P-I 死而死。判死线:d_H 预测力 ≤ d_E+0.1 → P-N 死,两主线保持并行。

### S7 P-K v2 三方回归(等 GLM 制品自供)
- 昨日盲测自家 26 vs KIMI 22 全分离(FPR=FNR=0);GLM 槽位 pending。GLM 制品到位后原 runner 三方可直接复跑,预登记沿用(SP_t≥0.7 / FPR<1/100 / FNR<1/20 / 抗洗白≥0.6),不允许为新数据调阈值。

**优先级**:S1(零成本闭合)> S2(体检护盘)> S3(蹭车)> S4(方法论补丁)> S5/S6(原判死线不变)> S7(外部依赖)。

---

**KIMI-K3 提交** | 严守 7 铁律 + 诚实降级承诺 | 任一象限结果都如实入报告 | 2026-09-17
