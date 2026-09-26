# V4 拍板问卷 · 组 B · 三 sub + Mavis 自读 raw idea 整合补充（增量稿）

- **性质**：组 B 代拟稿 `_v4_group_b_17letters_judgment_draft_2026_09_22.md`（已生效 `99B835595DFB`/24,822 B/176 行）的**整合补充**——PI 2026-09-22 贴出 explore 三 sub（Explore-A/B/C）+ Mavis 自读盘 3 条 idea 的产出（**此前未入代拟稿**），本稿逐条吸收
- **本稿不动**：`99B835595DFB` 代拟稿本体；任何 V1–V3 资产（letters/、corpus/、docs/、deposon_team/、verifier/、attacks/、scripts/、invitation、prompt pack）
- **本稿动**：仅 `D:\私人资料\deposon-repo\results\` 下新增一份本文件
- **数据基础**：
  - Explore-A 子代理 `bg_07d2f308`（session `mvs_ab29ef091f8c43dfa8e41f6bb5063bdf`）：12 条 raw idea（N-01 ~ N-12），4 条 disk fact
  - Explore-B 子代理 `bg_ca668ff1`（session `mvs_7f1607ae4f3646709550171a4d701d8f`）：7 个原 7 维之外新维度（D8–D14）+ 3 个空档（D1/D2/D7-Gap）= 10 条 raw idea
  - Explore-C 子代理 `bg_6ff9a02c`（session `mvs_60db8ad990fb4eb2a13c1620fee79ba8`）：Part 1 逐条质证 14 条（overstated/understated/misstated）/ Part 2 可证伪性审计 6 条 / Part 3 新形式化工具类比 6 个
  - Mavis 自读盘 3 条 idea 原料（miss_rate_curve GT 标签反转 / null 刺激 no-op 噪声地板 / 攻击载荷未施伪 FAIL）
  - 邀请函 §3 S-20/S-23 vs `attacks/` 目录语义不一致的磁盘确认
- **判定依据**：核心准则三问（沿种子稿已拍）+ 代拟稿已立 productive / blocking 框架
- **状态**：**PI 已复核确认生效**（PI 2026-09-22，问卷 ask_4e6dbcd296637dfdfc3809ed：「通过生效」）——17 件 292 条 + Mavis 自读 3 条 + Explore-A 12 条 + Explore-B 10 条 + Explore-C 三部分按本稿生效；与代拟稿 `99B835595DFB` 并列；§6 `attacks/` 语义反转作为 V4 seed field 出口过滤器（N-32 meta-seed）

---

## §0 与代拟稿差异点对账

| 新块条目 | 代拟稿（99B835595DFB） | 本稿处置 |
|---|---|---|
| Mavis 自读 ① miss_rate_curve GT 标签反转 | 未含 | §1 新增 N-23 |
| Mavis 自读 ② null 刺激 no-op 噪声地板 | 未含 | §1 新增 N-24 |
| Mavis 自读 ③ 攻击载荷未施伪 FAIL | 未含 | §1 新增 N-25 |
| Explore-A N-01 logits/调用侧 metadata | 未含 | §1 新增 N-26 |
| Explore-A N-02 content+path+anchor 三指纹定位 | 未含 | §1 新增 N-27 |
| Explore-A N-03 复用盲测结构 provenance | 已部分含于 §2.1 「S-17 跨模型归约」相关 productive 条 | 本稿 §1 不重列，仅在 §6 边界明示「artifact 非为此造」 |
| Explore-A N-04 GT 计数语义反转 | = §1 N-23 | 同条合并 |
| Explore-A N-05 no-op 漏检 | = §1 N-24 | 同条合并 |
| Explore-A N-06 攻击未施 | = §1 N-25 | 同条合并 |
| Explore-A N-07 A1–A5 × budget 反蒸馏攻击面 | 未含 | §1 新增 N-28 |
| Explore-A N-08 22 graphs BOSS 当 distiller–defender 博弈初值 | 代拟稿 §2.1 blocking「S-28 已有负向结果」已暗含；本稿显化为 §1 N-29（初值表 ≠ 博弈路径）+ 复评条件 | §1 新增 N-29 |
| Explore-A N-09 「22 graphs 是不是 potential game」作博弈收敛路径特征 | 未含 | §1 新增 N-30 |
| Explore-A N-10 图族重采样预探测 | 未含 | §1 新增 N-31 |
| Explore-A N-11 60 cells × 9 models T/R/A 时间序列当漂移代理 | 代拟稿已含（S-40 productive + S-37 + 4.4% FPR）；本稿 §1 不重列，§6 边界明示「7 天窗口不足」 | 仅边界标注 |
| Explore-A N-12 meta-seed 误标 | 未含 | §1 新增 N-32 |
| Explore-B D8–D14 7 新维度 + 3 空档 | 代拟稿 §2.1 仅含部分（学生从哪来 / 单侧失效）；其余维度与空档未含 | §1 新增 N-33 ~ N-39 |
| Explore-C Part 1 14 条逐种质证 | 代拟稿已含 corrective 框架但不含逐种「overstated/understated/misstated」诊断文本 | §3 全文重列 |
| Explore-C Part 2 6 条可证伪性改写 | 未含 | §3 全文重列 |
| Explore-C Part 3 6 个新形式化工具类比 | 代拟稿 §2.1 X 轨迹 8 项含部分（X-3 率失真）；其余工具类比（TVD / Le Cam / Chernoff–Stein / Rényi / Kolmogorov / closeness testing）未含 | §3 全文重列 + 在 X 轨迹条目下补全 |
| `attacks/` 语义反转 | 代拟稿 §2.1 含 coze §S-20「只动审计底座」+ §S-23「输入空间扰动无原型」；未明示邀请函 §3 S-20/S-23 与磁盘 `attacks/` 语义不一致 | §6 边界新增（明示目录语义反转） |

---

## §1 新增种建议集（15 条：N-23 ~ N-39；与代拟稿 §3 N-09 ~ N-22 并列）

| 编号 | 新种 | 原提议方 | 核心准则理由（三问） | 性质标签 |
|---|---|---|---|---|
| **N-23** | GT 标签反转（计数语义）是否误判漏检率主因 | Mavis 自读 ① `0A8ED127D6DE` L62–82 | Q1✓ miss_rate_curve 现成；Q2✓ 计数语义反转对漏检率影响可设计可证伪实验；Q3✓ 证伪「计数语义正确」 | **disk fact** |
| **N-24** | 检测器把等价变换（no-op）当漏检 = 假阴性还是真漏检 | Mavis 自读 ② 同文件 L437 + L327 budget=1 / L332 miss_rate=0.1 / 独立测单交换等值字节概率 0.0818 (20000 次采样 seed=7) | Q1✓ 等值字节概率实测现成；Q2✓ no-op vs 真实漏检可设计；Q3✓ 证伪「no-op 不可分离」 | **disk fact** |
| **N-25** | 攻击载荷「声明施加、实际未施」时，防御方「被攻破」是误警 — 如何审计伪信号 | Mavis 自读 ③ `attacks\a1_delete_anchor.py` `78AC391D16FC` L11–16 | Q1✓ a1 源码现成 + fp.compute_root 行为可重放；Q2✓ 伪信号审计可设计；Q3✓ 证伪「伪信号不可检出」 | **disk fact** |
| **N-26** | 无 logits / 无权重下，仅凭调用侧 metadata（latency / token usage 细分 / reasoning_tokens）能否识别被蒸馏模型 | Explore-A N-01 `corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` `9E1CCBDCEACC` L19–23、L36–54 | Q1✓ 调用侧 metadata 字段在 artifact 中现成；Q2✓ metadata-vs-output 二维分类实验可设计；Q3✓ 证伪「metadata 不可作蒸馏信号」 | re-fit，artifact 非为此造 |
| **N-27** | `content+path+anchor` 三指纹能否让蒸馏产物事后被「定位到具体出处件」 | Explore-A N-02 `corpus\v20\by_model\coze\coze_artifact_v_2026_09_16.json` `FEE04170AA73` L9–11、L17–20 | Q1✓ 三指纹结构现成；Q2✓ 蒸馏产物 ↔ 出处件定位实验可设计；Q3✓ 证伪「三指纹不可定位」 | re-fit |
| **N-28** | A1–A5 五类攻击（bit_flip / multi_bit / byte_swap / truncation / manifest_replay）× budget 档能否当反蒸馏攻击面 scaffold | Explore-A N-07 `miss_rate_curve` A1–A5 全段 | Q1✓ A1–A5 实测档现成；Q2✓ 攻击面 scaffold 实验可设计；Q3✓ 证伪「任一 A 不可作 scaffold」 | re-fit |
| **N-29** | 22 graphs × {RBR / Regret Matching} BOSS 实测当 distiller–defender 博弈的**初始参数表**（非博弈路径本身） | Explore-A N-08 `boss_pa_1_rbr_rm_result_2026_09_15.json` `C7C59E0D2F6C` L27–36、L339、L341–348 | Q1✓ 22 graphs 仿真数据现成；Q2✓ 初始参数表作实验输入可设计（与 S-28 共底物，但用途为初值非路径）；Q3✓ 证伪「初值表 ≠ 路径」 | re-fit |
| **N-30** | 「22 graphs 是不是 potential game」（3/22 = 0.1364）能否作为区分蒸馏博弈收敛路径的观测特征 | Explore-A N-09 `boss_pa_2_potential_game_result_2026_09_15.json` `5C76137D6430` L26–33 | Q1✓ 势函数判据已落盘；Q2✓ 收敛路径特征实验可设计；Q3✓ 证伪「potential game 性 ≠ 收敛特征」 | re-fit |
| **N-31** | 蒸馏正式发起前，能否用「图族重采样」类预探测判断目标防御是否在位 | Explore-A N-10 `boss_pc_1_a1_resampling_2026_09_15.json` `D21912A05D79` L7–10、L35–37 | Q1✓ 重采样数据现成；Q2✓ 预探测实验可设计；Q3✓ 证伪「预探测无效」 | re-fit |
| **N-32** | meta-seed：当 seed 把 A 类 artifact 当 B 类用途时，收件人该不该接受 | Explore-A N-12 邀请函 `3D9F73519F6C` L190/L196 + `attacks\__init__.py` `D11E085D9ECC` | Q1✓ §3 S-20/S-23 vs `attacks/` 实测；Q2✓ meta-seed 接受标准实验可设计；Q3✓ 证伪「误标不可检出」 | **disk fact**（误标） |
| **N-33** | 经济学/成本结构：蒸馏 ROI 与成本临界点 | Explore-B D8 | Q1✓ V4 自有 manifest 可锚定成本维度；Q2✓ ROI 临界实验可设计；Q3✓ 证伪「蒸馏 ROI 不可测量」 | pure speculation |
| **N-34** | 法律/合规/许可：ToS 对蒸馏的限定（**故意不引具体法条编号** — 知识截止后无法核实） | Explore-B D9 | Q1✓ ToS 文档可获取；Q2✓ 合规边界实验可设计；Q3✓ 证伪「合规边界与蒸馏检测无关」 | pure speculation |
| **N-35** | 数据来源可追溯性 / provenance：可审计血缘账本 vs 统计判别是两种范式 | Explore-B D10 | Q1✓ 已存对照（GLM_1 跨模型协议面 = 可审计 vs 统计判别）；Q2✓ 范式对比可设计；Q3✓ 证伪「两者等价」 | re-fit |
| **N-36** | Agentic / 多智能体蒸馏：工具调用 / 规划 / 记忆轨迹（比 CoT 更难） | Explore-B D11 | Q1✓ 工具调用 / 规划 / 记忆轨迹资产缺失（pure speculation）；Q2✓ 实验可行性受资产面约束；Q3✓ 证伪「agentic 蒸馏 = CoT 蒸馏」 | pure speculation |
| **N-37** | 端侧 / 量化 / 部署侧：RAM / latency / 能耗约束下的可达性 | Explore-B D12 | Q1✓ latency_ms 在 `deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` 532 cells 现成；Q2✓ 端侧可达性实验可设计；Q3✓ 证伪「端侧 ≠ 云侧」 | re-fit |
| **N-38** | 供应链 / 第三方市场：「声称蒸馏的产品实际是什么」 | Explore-B D13 | Q1✓ 产品声明可获；Q2✓ 实测对照实验可设计；Q3✓ 证伪「声明 ≠ 实测」 | pure speculation |
| **N-39** | 人因 / 认知：人类评审能否分辨蒸馏产物 | Explore-B D14 | Q1✓ V4 自有评审协议可锚定；Q2✓ 人类分辨实验可设计；Q3✓ 证伪「人 ≠ 机」 | pure speculation |
| **D1-Gap** | 蒸馏的负迁移 / 失败模式（现有 6 条都预设正迁移） | Explore-B D1-Gap | Q1✓ §1.1.1 代拟稿证伪判据三分支 (a)(b)(c) 现成；Q2✓ 负迁移实验可设计（与 R3 排列检验互校）；Q3✓ 证伪「负迁移不可分离」 | re-fit |
| **D2-Gap** | teacher 升级后已蒸馏 student 的相对漂移 | Explore-B D2-Gap | Q1✓ V2（09-11）→ V3（09-11）→ D7（09-18）时间序列现成 + S-40 productive 已立；Q2✓ 升级后相对漂移实验可设计；Q3✓ 证伪「相对漂移 = 全漂移」 | re-fit |
| **D7-Gap** | benchmark 污染作为「蒸馏」的替代解释（confound） | Explore-B D7-Gap | Q1✓ S-37 任务族翻转零分布现成；Q2✓ confound 对照实验可设计；Q3✓ 证伪「benchmark 污染 ≠ 蒸馏」 | re-fit |

> **总数**：17 件回函 292 条 + Mavis 自读 3 条 + Explore-A 12 条 + Explore-B 10 条（**与代拟稿重合部分已合并**，去重后净增 17 条：N-23 ~ N-39 + D1/D2/D7-Gap 三 Gap 已在表中显化）。

---

## §2 资产面情况（老实交代段）

**Explore-A 自报的两条路径不存在**（我未复核，按 Explore-A 报告转述）：

- `_v3x_18frozen_remeasure_2026_09_16.json` 路径
- `boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` 路径

PI 复核时请用 `node_size > 0` 验证；Mavis 不擅自补列。

**Mavis 自读环节一处旧记更正**（代拟稿 + 本稿均用更正值）：

- `deposon_v42_v2_miss_rate_curve_2026_09_16.json` 实测 24,435 B（Mavis 旧记 31,689 B 错；Explore-A 24,435 B 正确）
- `boss_pa_1_rbr_rm_result_2026_09_15.json` 实测 8,753 B（邀请函 §2.2 L66 写 8,674 B 错；Explore-A/B 各自确认）

---

## §3 Explore-C 三部分（14 条逐种质证 + 6 条可证伪改写 + 6 个新形式化工具类比）

### §3.1 Part 1 — 逐条质证 14 条（覆盖 7 维）

各判 **overstated / understated / misstated** 并给改写后一句话。要害类型与对应：

| Seed | 要害类型 | 处置建议（代拟稿已收 corrective 框架，本节列改写示例） |
|---|---|---|
| **S-01** | 把假设当结论 | 改写为「权重级迁移的可达上限 = 实盘不可观测，须以 reverse-attribution 间接构造证据」 |
| **S-03** | 无对照组 | 改写为「行为指纹迁移须有『同 lineage vs 异 lineage』对照盲测」 |
| **S-05** | 因果转相关 | 改写为「置信差异相关 ≠ 蒸馏传递因果」 |
| **S-06** | 因果转相关 | 改写为「拒答边界形态相关 ≠ 蒸馏因果」 |
| **S-07** | 复述设定 | 改写为「输出分布可测 ≠ 蒸馏已发生」 |
| **S-09** | 形容词堆叠 + 资产缺位 | 改写为「logit 级产物盘上不可得，本条改记 non-productive」 |
| **S-11** | 双向 superlative 未定义「长尾」 | 改写为「长尾须预注册 ≥ 阈值再谈一致性」 |
| **S-13** | 把 capacity 当可兼得 | 改写为「隐写标记植入与质量退化分两轴测」 |
| **S-17** | 资产脱节 | 改写为「跨模型归约须 anchor 实物 lineage 而非目录名」 |
| **S-21** | 比喻 | 改写为「信息瓶颈 = 退化算子族 × 输出保真度量化关系」 |
| **S-25** | 类别标签 | 改写为「对抗升级须多主体 + 多时间锚」 |
| **S-30** | 把猜想当已知 | 改写为「曲率指标须先校准（与 d_E 对比胜出）再谈独立信息」 |
| **S-32** | 跨域类比硬套 | 改写为「不可克隆类比远弱于定理，仅作概念词汇」 |
| **S-35** | 把 Bell 当现成工具 | 改写为「Bell 型检验形式化未就，本条 productive 但需形式化完成」 |

### §3.2 Part 2 — 可证伪性审计 6 条（按现有写法不可证伪）

| Seed | 现状问题 | 最小可证伪改写（Explore-C 原文） |
|---|---|---|
| **S-21** | 比喻性陈述 | 改写为「退化算子族 × 输出保真度的单调关系是否在 n=1000 组上以皮尔逊 ≥ 0.7 成立」 |
| **S-28** | 任何观察可被吸收 | 改写为「ε-greedy 双方跨 T=10⁵ 轮 per-round payoff 是否收敛到混合 Nash（CV < 0.05）」 |
| **S-32** | 类比硬套 | 改写为「Sha-256(content|anchor) 在 1000 蒸馏 vs 1000 独立训练上碰撞率差异是否 ≥ 1 个数量级」 |
| **S-33** | 不可证伪 | 改写为「多轮对话的『教师语料被污染』命题在 60 cell × 9 model 上的交叉熵差距 ≥ 0.05」 |
| **S-34** | 不可证伪 | 改写为「长链任务蒸馏后 step-by-step 准确率衰减是否 ≥ 30%」 |
| **S-39** | 被评测对象递归 | 改写为「同一 detector 在被评测模型已知 vs 未知状态下的检出率差异是否 ≥ 2 倍 FPR」 |

### §3.3 Part 3 — 6 个新形式化工具类比（在代拟稿 X 轨迹 8 项之上补全）

| 工具类比 | 接到 | 摘要 |
|---|---|---|
| **TVD**（全变差距离） | → S-31（observer） | 全变差 ≤ 1 的可证伪框架 |
| **Minimax 下界 / Le Cam 两点法** | → S-16（成员推断）/ S-37（任务族翻转） | 不可分离性的统计下界 |
| **Chernoff–Stein 检测论误差指数** | → S-07（输出分布）/ S-17（跨模型归约） | 大 n 下的指数型错误衰减 |
| **Rényi 散度** | → S-08（嵌入几何）/ S-09（logit） | 阶数 α 自由选取的散度族 |
| **Kolmogorov 复杂度 / NCD** | → S-11（长尾一致性）/ S-15（统计异常） | 不可压缩度作指纹 |
| **closeness testing 样本复杂度** | → S-36（GT 困境）/ S-38（复现性） | 两分布不可分离的样本量下界 |

**Explore-C 自报**：

- T-03 / T-05 / T-06 的「标准首引」没有唯一标准号，不写具体论文号。
- 邀请函 §8（L366–404）的 22 个 SHA-12 已逐条用 `Get-FileHash` 实测等于声明值（**Explore-C 实测验证邀请函 §8 表内 22 件 SHA-12 全相等**——这是块内唯一一处独立磁盘确认）。

---

## §4 代拟稿 §2.1 productive / blocking 框架对本稿的适用

新块 17 条 raw idea（§1 N-23 ~ N-39 + 3 Gap）按代拟稿已立的三问框架（Q1 锚 + Q2 改 + Q3 验）全部 productive，**唯一例外**：

- **N-34（法律/合规/许可）**：Q1 锚 ✓（ToS 文档可获）/ Q2 改 ✓（合规边界实验可设计）/ Q3 验 ✗（合规边界无明确且 PI 拒绝引法条编号）——**判 borderline productive**：可作 §4 开放问题而非可证伪实验条目——PI 复核时按此分类。

---

## §5 已坐实不稳健读数自律（沿 §3.8 路径 C「五条分两类」+ workbuddy (d) §4-OQ-3）

代拟稿 §2.4 已列 49 条风险报告中含新块的扩展：

- **单侧失效三处同构（workbuddy_brainstorm §4）**：归因仪 FNR/FPR + DELTA f3/独立复算 + 语法擦除测过 / 语义擦除未测——三处单侧失效是否同一结构（§4-OQ-4）
- **保序恒等式伪影（trae_work N-08 + coze §4 (d)）**：归 §4-OQ-10「多处一致不证明独立」
- **P_G transport 非真平行移动 + κ 入参缺失**：归 §3.8「档案管理不稳健」类（claude_code §5.10）

---

## §6 边界声明（必收：邀请函 §3 S-20/S-23 vs `attacks/` 语义反转）

### §6.1 磁盘确认（三条独立证据）

- **证据 ①**：`attacks\__init__.py` `D11E085D9ECC` L1–L4 自述「P-D 攻击脚本包」，输出 `{"attack": "A1|A2|A3", "verdict": "PASS|FAIL"}`。
- **证据 ②**：`attacks\a1_delete_anchor.py` `78AC391D16FC` L2–L8 头部写「A1 工件删除攻击」「判死: 检出 -> verdict=PASS, 漏检 -> verdict=FAIL」，攻击对象是 `fingerprint_v0.compute_root`。a2/a3 同口径（`3D54B277620E` / `F02B3EEE8D6E`）。
- **证据 ③**：Explore-A 全文读 `attacks/` 全部 4 个文件得出同样结论。

### §6.2 与邀请函冲突

邀请函 §3 S-20（约 L190）+ S-23（约 L196）把 `attacks\` 描述为 discrimination 攻击资产；磁盘上 `attacks\` 是 verifier 工件完整性攻击脚本。**两条独立证据**（Mavis 自读 + Explore-A）。Explore-C 也得出同样结论但**未读** a2/a3 源码不算独立磁盘确认。

### §6.3 处置

- 不改鉴为正（沿 §3.3「不再邀请函」）；邀请函文本不再升版。
- 新增 §1 N-32「meta-seed 接受标准实验」（disk fact）作 V4 自有种子场出口过滤器：凡可被独立证明属于「机制错配」的 seed，V4 自有出口不接受。
- 代拟稿 §2.1 coze §S-20「三件只动审计底座」+ §S-23「输入空间扰动无原型」两条已对应此处置——本稿 §6 为其显化根因（邀请函 vs 磁盘语义不一致）。

---

## §7 边界声明

本稿由 Mavis 起草（PI 2026-09-22 贴出 explore 三 sub + Mavis 自读盘 3 条 idea 后整合补充）。起草过程 0 LLM 调用、0 外部 URL、0 GitHub/WeChat 操作、0 密钥、0 frozen 制品/schema/锚文件/任何 V1–V3 资产触动；本稿仅**新增**一份整合补充件（`D:\私人资料\deposon-repo\results\_v4_group_b_explore_subs_integration_2026_09_22.md`）；组 B 代拟稿本体 `99B835595DFB` 与问卷 v1.1 不动。**PI 已复核通过，已生效**（PI 2026-09-22，问卷 ask_4e6dbcd296637dfdfc3809ed）；与代拟稿并列生效，问卷回填在 §1.2.x / §2.x / §4.x 决策点后续执行。问卷本体仍为权威。

**未处置的悬挂项**（PI 已声明，未在本稿处理）：
- 21 vs 22 caption 口径（沿 §1.2.2 已派）
- `V7` vs `R5`（沿 §1.2.5 别名表已派，具体语义待 PI 补注）
- `KIMI-K3` 公开名 vs `kimi-for-coding` API 端点（沿别名表表 1 已派）
- 两枚明文密钥待吊销 / 轮换
- 邀请函 §2.2 8,674→8,753 + §2.6 L93「5 KT anchors」实为 15 锚
- §3.7 L218 `behated` 三处错字
- 约 39 个未读 background task（沿 52 条旧后台任务已知噪声，忽略）

---

## §8 待 PI 复核决定项（落盘后回填面）

1. **新增 17 条是否全部入 V4 修订种子场**：与代拟稿 §3 N-09 ~ N-22 共 31 条新种子如何分维落位？
2. **N-34（法律/合规）borderline productive 是否一并上采为 §4 开放问题**？
3. **Explore-C Part 1 14 条改写是否直接覆盖种子稿边界声明 2 + S-09 / S-32 / S-35 productive 复评条件栏**？
4. **Explore-C Part 2 6 条可证伪改写**是否入 §1.1.1 代拟稿实验轮廓扩展节？
5. **Explore-C Part 3 6 个新形式化工具类比**是否订入 X 轨迹 8 项的扩展节？
6. **§6 `attacks/` 语义反转**是否落盘为 V4 自有 seed field 出口过滤器（N-32 meta-seed）？