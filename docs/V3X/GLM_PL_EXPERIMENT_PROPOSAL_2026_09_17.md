# GLM 方《增补实验设计提案》——V3X D+0.5（Mavis 邀请函响应件）

**提交方**：GLM（Z.ai GLM 5.x），GLM chat 通道
**提交日期**：2026-09-17（周四）CST（邀请函 14:00 截止前）
**响应文件**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md`（Mavis，09:33 CST）
**结构**：一页速览 ＋ §1 Backbone 选择 ＋ §2 同序单调破局方法 ＋ §3 测法 ＋ §4 期望阈值 ＋ §5 风险评估 ＋ §6 主线其他可能方向的增补实验设计（用户 11:05 指示并入）＋ 尾部合规声明。邀请函 §3 要求的 5 节齐备。
**数值纪律**：本文全部数值来自挂载仓库一手文件或今日 0-LLM 复算（溯源索引见尾部 E）；标注〔推导〕者为对已溯源数值的显式算术，不引入新数源；正文 0 个 API key；挂载仓库全程只读。

---

## 0. 一页速览

1. **Backbone（§1）**：主推 **DeepSeek V4**（`deepseek-v4-pro-ga-260813`，火山 coding/v3——sanity 200 ×2 ＋ catalog 在列 ×4 ＋ GT3 真实调用缓存三重证据）；备 1 **Qwen3**（`qwen3-32b-20250429`，同网关，须 1-call sanity 先行）；备 2 **NVIDIA Nemotron 3.5 Lightning**（`nvidia/nemotron-3.5-lightning`，OpenRouter，**仅 reference_only**——user 17:38 拍板 OpenRouter 不进 V3X baseline）。GLM 5.x 自我回避（家族重复，§1.7）；MiniMax M3 对照零成本复用既有火山 30-cell 基线，不开 minimax.chat 新通路（§1.8）。另附邀请函候选池 4 处名称礼貌勘误（§1.6）。
2. **破局方法（§2）**：v2 的 Spearman=1 是同一向量 t 的两个严格单调变换之间的**代数恒等式**（plugins runner L64–66 代码实证），不是测量。v3 判死统计量＝**并列校正 Spearman**（二值向量下闭式等价于 2×2 表 φ 系数），**判死对唯一锚定（新 backbone × minimax-m3 基线）**——唯一两侧全量在库、I1–I5 协议逐字段匹配、0-LLM 可复算的对。仓内实测校准：minimax-m3 vs glm-latest 同 30 题 φ=0.659/0.641——跨 backbone 同序**不是**自动成立。Trae 的分辨率批评部分成立，以「空带定理＋0 成本 triage＋条件式 S2」三层处理；温度轴不采纳为破局手段（归因混杂，§2.5）。
3. **测法（§3）**：30 cells（gsm8k_1–15 ＋ stq_1–15）零改动＋I1–I5 五不变量＋四层流水线（题源/判分 0 改动克隆 → API 调用参数化 → 制品构建 0 LLM → 0-LLM hashlib 复算层，沿 `_verify_15frozen.py`）；制品逐字段对齐 minimax 制品三列 sha256[:12] hash。
4. **阈值（§4）**：三档判死表逐行沿邀请函 §2/§4 原文。n=30 二值下 φ 可达值存在可证**空带 [0.9354, 1)**——[0.95, 1.0) 档操作上不可达，判定语义等价于 D=0 vs D≥1，且对 (0.9354, 1] 内任何阈值线**结论不变**（阈值不变性）；档内信息量由 D 与 triage 承载。φ∈(0.5, 0.95) 时启动 Rasch 真实 data collapse 拟合（LOCO 交叉验证为主指标）。
5. **风险（§5）**：API 风险集中于超时长尾与 wall-clock（9 模型 run 85 min PARTIAL、47/270 前科）；18 frozen 0 触动（写入面全部为新文件）；单 backbone × 30 cells 含 1 次整轮重跑与报告总计 **30–60 min**，落在邀请函 15:00–18:00 窗口内余量 >2 h。
6. **主线其他方向（§6）**：五条增补设计（全部不触动 18 frozen、触发均须拍板）——A. 9-model run 7 个 sanity-200-0-cells 槽位补跑作跨 backbone φ 分布估计；B. n=30→60 升档（空带收窄至 [0.9672, 1)）；C. 条件式次级连续测量 S2；D. M3 对照零成本复用；E. 多尺寸轴（30/45/60/100）D+1 升级选项（closeout 报告 §2.4 一手溯源）。

---

## §1 Backbone 选择

### 1.1 推荐总表（1 主＋2 备，满足邀请函「至少 1 个＋最多 3 个」）

| 槽位 | Backbone | 确切 model ID | 网关路由 | 可用性证据（一手） |
|---|---|---|---|---|
| **主** | DeepSeek V4 | `deepseek-v4-pro-ga-260813`（能力/延迟平衡可换 `deepseek-v4-flash-ga-260731`；若 GA 全称路由异常可降级无后缀写法 `deepseek-v4-pro`/`deepseek-v4-flash`，沿 9model「无后缀别名可路由」先例） | 火山方舟 coding-plan：`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` | 仓：sanity 200 ×2（1813/1691 ms）＋ catalog 在列 ×4 ID ＋ GT3 prior 缓存 6 件真实调用痕迹 |
| **备 1** | Qwen3 | `qwen3-32b-20250429`（算力紧张降 `qwen3-14b-20250429`） | 同上（火山 coding/v3） | 仓：catalog 在列 ×5 ID；**零调用痕迹，须 1-call sanity 先行** |
| **备 2** | NVIDIA Nemotron 3.5 Lightning | `nvidia/nemotron-3.5-lightning`（付费档 $0.08/M＋$0.2/M，ctx 262,144）或 `:free` 档（$0，ctx 1M） | OpenRouter：`https://openrouter.ai/api/v1/chat/completions`（直连不设 proxy） | OpenRouter 目录一手在列（2026-08-08 created）；仓：OpenRouter key 与直连通路已经 embedding 探针 16 calls 全过验证；chat 模型无仓内先例，同须 sanity |
| （对照） | MiniMax M3 | 既有基线 `minimax-m3`（火山） | 火山 coding/v3 | 仓：既有 30-cell 基线 COMPLETE 22/30（§1.8 零成本复用） |

### 1.2 选型三准则

1. **家族未覆盖**：5 制品（KIMI 24,150 B／GLM_1 19,685 B／GLM_2 13,150 B／coze 10,978 B／MiniMax 25,347 B，P-K verify 5/5 PASS）已覆盖 Kimi／GLM（双槽位）／MiniMax／coze／Doubao（探针级）；**DeepSeek、Qwen、NVIDIA/Meta/Mistral/Cohere 均未覆盖**——主推与两备全部落在未覆盖家族。
2. **可用性证据分级**：DeepSeek V4 是候选池中唯一具备「网关 sanity＋真实调用痕迹」双证据的未覆盖家族；Qwen3 仅 catalog 在列；Nemotron 3.5 依赖 OpenRouter 通道（受 baseline 准入约束，见备 2 注）。
3. **协议同构**：主/备 1 与 minimax 基线同网关（火山 coding/v3，OpenAI 兼容），调用路径完全同构、仅换 model 字段——同 prompt 异 backbone 的最干净对照。

### 1.3 主推 DeepSeek V4 详述

| 证据 | 出处（仓内一手） |
|---|---|
| catalog GET /models（2026-09-10 18:00:21，http 200，130 模型）在列 4 个 V4 ID：`deepseek-v4-pro-260425`、`deepseek-v4-flash-260425`、`deepseek-v4-flash-ga-260731`、`deepseek-v4-pro-ga-260813` | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json`；`results/deposon_ark_models_2026_09_10.json` |
| sanity http 200：`deepseek-v4-flash` 1813 ms、`deepseek-v4-pro` 1691 ms（coding/v3 端点；cells 因 9model 全程 85 min wall-clock 超时未跑到） | `results/deposon_volcengine_9model_30cells_2026_09_10.json` |
| `deepseek-v4-pro-260425` ×6 图 GT3 prior 缓存——V4 真实调用痕迹 | `results/gt3_prior_cache/deepseek-v4-pro-260425__*.json`（6 件） |
| **端点教训**：`deepseek-v3-2-251201` 走 `/api/v3/chat/completions`（非 coding 路径）→ 404，0/30。DeepSeek 必须走 coding/v3 | `docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` |

V4 为 2026-08 GA 新代（pro-ga-260813 为 GA 最新）；5 制品零 DeepSeek 且仓库内 DeepSeek 从未有完整 30-cell 数据——「不同家族」论证成立。输出侧风险（V4 无仓内完整 cell 输出样本）在 sanity/首 cell 验证抽取兼容性（答案为末 token 数字/Yes-No，无长 reasoning 前缀干扰），并全程由 §2.5 triage 捕获归类。

### 1.4 备 1 Qwen3（须 sanity 先行）

catalog 在列 5 个 Qwen ID（`qwen3-8b/14b/32b-20250429`、`qwen3-0-6b-20250429`、`qwen2-5-72b-20240919`）〔仓：`deposon_ark_models_2026_09_10.json`〕；探针与缓存均无 Qwen——**无 sanity、无 cell 数据**。前置动作：1-cell sanity（成本 1 call）再放全 30 cells。已知风险：Qwen3 系原生 thinking 输出模式（外部信息，仓库无一手）——sanity 时确认输出形态，必要时请求参数显式关闭或抽取端只取最终答案段；若触发翻转属 triage 类②（抽取边界），可被 §2.5 机制如实归类。`qwen2-5-72b-20240919` 为 2024 旧代不推。

### 1.5 备 2 Nemotron 3.5 Lightning（仅 reference_only）

NVIDIA 训练范式（开放权重＋开放数据配方）与已覆盖 6 家族不同源，海外系对照价值最高：若跨族 Spearman 仍=1，「同序单调与家族无关」结论最有力。**通道约束（如实披露）**：user 17:38 拍板「OpenRouter 不进 V3X baseline」〔仓：`docs/V3X/EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md` §4 原文〕＋铁律 6——该通道产出只能作 reference_only 对照，制品 meta 须如实标注；**判死级主张的主 backbone 应落火山通道**。限额事实：free-tier 有 2/30 read timeout 前科（`docs/V3X/OPENROUTER_5MODEL_30CELLS_2026_09_10.md` 附录 B），批间加 1–2 s 间隔或用付费档（30 cells × ~1k tok 约 $0.003，可忽略）。

### 1.6 候选名称礼貌勘误（供 Mavis 聚合时参考）

以 2026-09-17 ~11:05 CST OpenRouter 公开目录一手拉取（`https://openrouter.ai/api/v1/models`，444 模型，快照 `shared/or_models_snapshot_2026_09_17.json`）核对，邀请函 §1 候选名单中 4 处名称与实际目录不符。**为免聚合版按原名派工时无法落地，谨作如下勘误**：

| 邀请函候选名 | OpenRouter 实际状态（一手） | 建议 |
|---|---|---|
| NVIDIA Nemotron 5 | 无 "nemotron-5" ID；NVIDIA 通用系最新为 Nemotron 3.5 系列（`nvidia/nemotron-3.5-lightning` 及 `:free`，另有 nemotron-3-ultra/super/nano 等） | 改推 **nemotron-3.5-lightning**（本方备 2） |
| Meta Llama 3.4 | 无 llama-3.4 ID；Meta 通用系为 `llama-4-maverick`（$0.1875/M＋$0.6525/M，ctx 1,048,576）／`llama-4-scout`（$0.1/M＋$0.3/M）；3.x 止于 `llama-3.3-70b-instruct`（2024-12-06，较旧） | 若需 Meta 家族改 llama-4-maverick；本轮不占推荐名额 |
| Mistral Large 2 | `mistralai/mistral-large-2407` 在列（$2/M＋$6/M，2024-11-19，较旧较贵）；同厂更新旗舰 `mistral-large-2512`（Large 3，$0.5/M＋$1.5/M，ctx 262,144，2025-12-01） | 若选 Mistral 家族建议 mistral-large-2512（更便宜且更新，同为 MoE），写明确切 ID |
| Cohere North | 无通用对话档 North ID；唯一 North 系为 `cohere/north-mini-code:free`（code 特化＋moderated）；Cohere 通用系为 `cohere/command-a`（$2.5/M＋$10/M） | code 特化与 GSM8K/StrategyQA 通用推理任务错位；作对照须接受偏移或改 command-a |

### 1.7 GLM 5.x 落选声明（自我回避）

本方为 GLM 系，但**不推自家**：5 制品已有 GLM_1/GLM_2 双槽位；glm-latest 30-cell V2 22/30（PARTIAL，HTTP 29/30）已在库；火山 catalog GLM 族仅 3 ID（glm-4-5-air-20250728／glm-4-7-251222／glm-5-2-260617），glm-5.3 不在目录（9model 中 `glm-5.3`/`glm-5.3-flash` 无后缀写法 sanity 200 但 0 cells，与 catalog 并存的事实张力如实记录）。选 GLM 5.x 无法支撑邀请函「与现有 5 制品家族不一致」原则——落选。

### 1.8 MiniMax M3 对照处理（零成本复用，不开新通路）

1. 仓库事实：M3 既有基线走的是**火山 coding-plan**（`minimax-m3`，22/30 COMPLETE，`results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json`），并非 minimax.chat 官方 API。对照直接复用该基线 → 制品链路（`deposon_team/products/minimax_artifact_v_2026_09_16.json`），0 成本、0 frozen 触动；「同 prompt 同评分 scale 下新 backbone 与 M3 是否同序」的对照目的已可满足。
2. 不建议为对照新开 minimax.chat 通路：新增 key/端点/TOS 三重未验证变量，网关差异会混入 backbone 归因，削弱对照效力。仓库内无 minimax.chat 通道 key 事实（铁律 5：不假设钥匙存在）。
3. M3 不可作正式 backbone：MiniMax 家族已在 5 制品内。

### 1.9 与 Trae 提案 §1 的交叉核验（聚合口吻）

Trae code 提案（`docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md`，主 Mistral Large 2／备 Qwen3／对照 Cohere North）与本方选型在 **Qwen3 备位重合**，另作三点事实补强供聚合参考：① Mistral Large 2 确切 ID `mistralai/mistral-large-2407` 在列但旧且贵，同厂 `mistral-large-2512` 更便宜更新且同为 MoE——若取 Trae「MoE 架构差异」意图，建议二选一并写明 ID；② Cohere North 无通用档（唯一 North 系为 code 特化），其「非 RLHF-dominant 训练范式」对照若坚持 Cohere 家族须接受 code 特化偏移或改 `command-a`；③ Qwen3 有零调用痕迹风险，本方补充「sanity 先行」前置条件。分歧不掩盖采纳：Trae 的方法层主张见 §2.5/§2.8。

---

## §2 同序单调破局方法

### 2.1 v2 根因：Spearman=1 是代数恒等式，不是测量

`deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py` L64–66（只读复核，逐字）：

```python
transformed = [t ** nu for t in T_frac60]
eta_transformed = [t * eta for t in T_frac60]
corr, _ = spearmanr(transformed, eta_transformed)
```

t 为**同一个** 9 维向量（9 模型 T_frac60，源：`results/deposon_v3_physical_opt_60cells_2026_09_11.json` input_data.9_models）。对 ν>0、η>0，t↦t^ν 与 t↦t×η 均为严格保序变换（并列亦保持），故 rank 恒同，Spearman ≡ 1——对全部 25 个网格点（ν∈{0.5,…,2.5}×η∈{0.1,…,0.5}）恒成立，与数据内容零比特信息量；v2 的「R²=1.0」即该恒等式的平方。**与 Trae §0 诊断一致：v2 Spearman=1 是构造保证。**

### 2.2 v3 检验量：并列校正 Spearman（二值下闭式 φ）

- **定义**：ρ_S(x, y) := Pearson(midrank(x), midrank(y))；等价可执行形式 `scipy.stats.spearmanr(x, y)`。x＝新 backbone 30-cell 对错向量，y＝minimax-m3 基线 30-cell 对错向量。
- **并列处理（预登记）**：二值向量构造性含大量并列，必须用中位秩口径；**禁用**秩差公式 1−6Σd²/(n(n²−1))（并列存在时系统偏差，二值下可偏离真值 >0.2）。
- **闭式**：非退化二值下 ρ_S = Pearson = φ = (ad−bc)/√[(a+b)(c+d)(a+c)(b+d)]；2×2 计数 a＝双对、b＝新对基错、c＝基对新错、d＝双错。
- **关键推论**：ρ_S=1 ⟺ x=y（30/30 逐 cell 恒等）——可证伪。**Runner 自检断言（0-LLM）**：|spearmanr−φ_闭式|<1e-12；x,y∈{0,1}^30；cell_id 集合与 C 精确相等。
- **退化情形处置（预登记）**：任一侧常数向量 → φ 未定义，不进判死档，按「补测」精神升级；极端边际（两侧 pass 均 ≥27/30 或均 ≤3/30）→ 正常进档但标注「分辨率受限」，D7 措辞由 Mavis 裁决。

### 2.3 判死对与旁证对（谁与谁比）

| 对 | 两侧 | 协议匹配 | 角色 |
|---|---|---|---|
| **确认性对（判死口径）** | 新 backbone × minimax-m3 基线 | 完全匹配（I1–I5 同构，同网关） | **唯一判死统计量的输入** |
| 条件旁证对（Tier 2） | 新 × GLM_1/GLM_2/coze 制品 | 制品在 Windows 原机，schema 探针通过则逐 cell，否则制品级（3 列 hash 对照） | 旁证，全部如实报告，不入判死口径 |
| 观察性对（仓内既有） | 新 × glm-latest（V2 辅助 run） | 协议偏差已披露：temp=0.0 一致，max_tokens=2048、timeout=180s/cell ≠ I5 | 旁证，双口径报告 |
| 不可比对 | 新 × KIMI 制品 | KIMI 制品为 22-caption 指纹索引，无逐 cell Q&A | 披露为不可比，不做任何统计 |

**聚合规则（预登记）**：判死结论只由确认性对触发；旁证对逐对报告点估计与 CI；旁证与确认性档位不一致 → 如实披露并上抛 Mavis/用户，**不自动改判**。单锚定理由：minimax 基线是唯一两侧全量在库、协议逐字段匹配、0-LLM 可复算的对——判死统计量必须在任何机器上可独立重算，不依赖原机 Windows 制品可读性。

### 2.4 可证伪性与仓内校准（今日 0-LLM 实测，0 新增 API 调用）

v3 两侧是两个不同物理系统在同一仪器（30 题＋冻结 prompt/抽取/判分＋temp=0.0）上的输出，x 不是 y 的函数——ρ_S=1 当且仅当 30/30 恒等这一**经验事实**成立（任一 cell 翻转即否决）。仓内最小可比跨 backbone 对（minimax-m3 vs glm-latest，同 30 题、同网关、同冻结抽取器）：

| 口径 | 2×2 (a,b,c,d) | 不一致 cell | φ |
|---|---|---|---|
| 存量判分（as-stored） | (20, 2, 2, 6) | gsm8k_6, gsm8k_12, stq_13, stq_15 | **0.6591** |
| 按当前冻结抽取器重判（as-rescored） | (21, 1, 3, 5) | gsm8k_12, stq_13, stq_15 | **0.6407** |

含义：跨 backbone 输出分布偏移是仓内经验常态，φ=1 绝非自动成立；经验基率落在 (0.5, 0.95) 档——该档并非死档。同族旁证：deepseek-v4-flash 0.7667 vs deepseek-v4-pro 0.5333（T_frac30，同家族不同后训练档位尚且分歧）。**基线卫生检查（今日已预检通过）**：minimax 源 run 30 条 raw 以冻结抽取器重判 30/30 一致、0 翻转（含 gsm8k_4 千分位勘误值 1430/True）——基线向量干净，可直接作判死基线。

### 2.5 Trae 分辨率批评的三层处理（本设计核心决策）

批评成立部分：n=30、二值、非退化边际下，凡 D=b+c≥1 则 φ ≤ 0.9354（今日穷举 31³ 全 2×2 表实测，极值表 (14,0,1,15)；闭式 c=0 时 φ=√[a·d/((a+b)(b+d))]）——**[0.9354, 1) 为可达值空带**，邀请函 [0.95, 1.0) 档在 n=30 主统计量下不可达（除退化边际）。三层处理：

1. **空带反而强化判死（阈值不变性）**：0.95 线落在空带内部 ⇒「<0.95 vs =1.0」判定等价于「D≥1 vs D=0」，且对 (0.9354, 1] 内任何阈值线**判定不变**——判死口径对阈值任意性免疫。档内信息量由 D 与 triage 承载，不损失。
2. **0 成本 triage（不一致 cell 三分类，预登记）**：对每个不一致 cell 从已落盘 raw response 复判归类：①知识/方法分歧；②抽取边界伪影（如「8000」vs「**8,000**」）；③仪器伪影（超时/空响应/非 200）。仓内校准例 4 个不一致 cell 实测：gsm8k_12、stq_13=①；gsm8k_6=②；stq_15=③。triage 不改判死档位（防 reassign），但决定 D7 文稿归因诚实度。
3. **条件式次级连续测量 S2（条件触发，不作判死口径、不作破局手段）**：
   - **S2a（默认建议开启，I5 字面合规，＋约 8 分钟）**：新 backbone × 30 cells × K=3 重复采样，设置完全不变（重复采样不是失败重试）——确定性审计：任一 cell 跨重复翻转 → 记录后端非确定性，per-cell 通过率自然成为次级连续测量（此时对 minimax 侧补对称 K=5 重跑，新文件）；30×3 零翻转 → =1.0 档「普查式读法」被加固。成本 90 次调用。
   - **S2b（条件触发＋须拍板，铁律 4）**：τ₀=0.7（预登记值，先于任何 v3 数据选定）、K=5、双侧对称（新 backbone＋minimax-m3 补跑，新文件），per-cell 通过率向量 p∈{0,0.2,…,1}^30；统计量 ρ_S(p_new, p_base)（中位秩口径）＋秩序稳定性 ρ_S(v(τ=0), p(τ₀))。触发条件（任一）：T1 主对 φ=1.0；T2 主对 φ<0.5；T3/T4 退化情形。成本 300 次调用 ≈ 26 min 串行（5.3 s/次锚点）。
   - **温度轴不采纳为破局手段（与 Trae 的核心分歧，如实呈现）**：主跑判死统计量必须保持单因素设计（唯一变量＝backbone）。判死跑若含 τ 变化，φ<1 无法归因于 backbone 差异还是采样熵——归因混杂直接污染三档表全部结论。故温度只出现在 S2b（旁证、条件触发、双侧对称、不覆盖判死），作用限于加强或存疑化对应档位表述，永不改档。

### 2.6 破局机制阐述〔动机档〕

**证据分级声明**：以下为机制级假设——模型内部细节（后训练配方、tokenizer 词表、注意力分布）不可从仓内直接观测，仅用于说明「为何预期输出分布偏移」，不作为任何判定证据；破局手段本身只有一个：换 backbone（I1–I5 全冻结，唯一变量＝model ID），**严禁且未使用任何 prompt format 变化**（模板逐字复用，见 §3.1）。

- **DeepSeek V4（主）**：① RLHF 后训练偏好差异 → 更长思维链前缀与更朴素答案表面（仓内风格事实对照：minimax sanity「1 + 1 = **2**」bold 习惯 vs glm「1 + 1 = 2」朴素——答案表面惯例跨家族确实不同；答案表面 × bold 优先抽取规则＝实际翻转点，仓内 gsm8k_4「$1,430」与 glm gsm8k_6「**8,000**」两个边界事件已证明该机制真实发生过）；② tokenizer 边界差异（千分位/小数/货币符切分不同 → 抽取正则命中改变；同族旁证：flash vs pro T_frac 相差 0.2334）；③ MoE/注意力分布差异 → 边界难度 cell 上不同错误剖面——4–6 个边界 cell 正是 φ 判别力所在。
- **Qwen3（备 1）**：① thinking 前缀输出结构 → 答案 token 位置后移、表面惯例改变（触发则属 triage 类②）；② 阿里系 BPE 数字切分与 DeepSeek/MiniMax 均不同；③ 数学/代码向 RLHF 偏好 → GSM8K 与 stq 错误剖面预期不同。
- **Nemotron 3.5 Lightning（备 2）**：① NVIDIA 开源数据管线主导训练范式 → 答案表面与错误剖面预期系统性不同；② 英文中心 tokenizer（题面均英文）对数字/Yes-No 表面惯例不同；③ 长上下文衰减谱不同 → stq 长题干 cell 偏移（仓内旁证：stq_15 上 glm 180s 超时而 minimax 30s 内完成——完成性/延迟剖面跨 backbone 确实不同）。

### 2.7 φ∈(0.5, 0.95) 时的真实 data collapse 拟合程序

- **模型（collapse 的诚实可操作化）**：Rasch 可分性模型 logit P(x_{b,i}=1) = θ_b − δ_i（θ_b＝backbone 能力，δ_i＝cell 难度，约束 Σδ_i=0）；collapse 成立 ⟺ 固定 θ_b 重标定后所有 backbone 的「判对率–难度」曲线落在同一条主曲线 σ(θ_b−δ_i) 上——有限尺寸标度类比中 θ_b↔系统尺寸、δ_i↔标度变量、σ↔标度函数逐项对应。矩阵 X∈{0,1}^{M×30}：确认性对 2 行＋Tier 2 可读则并入＋glm-latest 重判口径行标注观察性（敏感性分析：含/不含观察行各跑一次）。
- **程序（0-LLM，纯 numpy/scipy，秒级）**：① Newton-IRLS 求 MLE；② 对**原始结局**报告 McFadden 伪 R²（null＝仅行边际模型）＋R²_LS（附「二值下非 [0,1] 校准」口径说明）＋**LOCO 留一 cell 交叉验证（预登记为主指标**——M=2 时样本内指标必然虚高，LOCO 是唯一诚实指标）；③ G² 置换校准 p（行内置换保边际，B=2000）为主，χ²(29) 渐近为辅（小样本谨慎标注）。
- **强度分层（预登记）**：STRONG＝置换 p<0.01 且 LOCO 严格优于 null 且 McFadden≥0.2；MODERATE＝p<0.05 且 LOCO 不劣于 null；其余 WEAK/NONE 如实入局限性。分层只影响 paper 措辞强度，**不改变三档判死结论**。
- **诚实性防护（runner 硬编码断言）**：禁单调变换网格（不存在「同一变量的两个单调变换之间的 Spearman/R²」路径——v2 原罪）；采纳 Trae §6.0 退化统计量预检四断言（输入向量方差>0、秩非恒同、标签非硬编码、检测率不低于随机基线）；Spearman 闭式双算断言；零结果如实入报告。

### 2.8 与 Trae 提案的关系（交叉引用，不贬低）

- **采纳**：v2 根因诊断（§0 一致）；分辨率批评的空带部分（§2.5 第 1 条）；Trae §6.0 退化统计量预检四断言全文采纳（§2.7）；Trae §8 双层缺陷中的层 2——P-L v1 委外 runner 的 R²=0.4·exp(−2η)·(1−0.1|ν−1.5|) 为**构造占位公式**（与输入数据无关，max_R2 恒 ≈0.3275）——v3 runner 全新落盘，**严禁复用 v1/v2 两个 runner 模板**（见 §3.8）。
- **澄清（不翻案）**：Trae §1「任何 backbone 的对错序列 Spearman 恒=1」是把 v2 的变量级恒等式外推到 cell 级经验命题——仓内最小反例 φ=0.659/0.641（同题、同抽取、同判分、temp=0.0）说明「换 backbone 不足以破局」在本仓数据下不成立；但其「分辨率不足」批评部分成立并被采纳。分歧不掩盖采纳；其连续规模轴主张的合理内核由 S2b（条件触发、受控 τ₀、双侧对称）承接，温度轴不进判死口径的理由见 §2.5 第 3 条。

---

## §3 测法

### 3.1 可比性不变量（先锚死，再谈设计）

增补实验唯一目标是给 P-L v2 换真数据——**换的只能是 backbone，不能换题目、prompt、抽取、判分**。5 项不变量全部锚定 minimax m3 runner 一手实现：

| # | 不变量 | 锚定来源（一手） |
|---|---|---|
| I1 | 30 道题＝gsm8k_1–15＋stq_1–15，题文与 gold 逐字一致 | `results/deposon_benchmark_v1_4_gsm8k_details.json`（100 题）＋`…_strategyqa_details.json`（99 题）＋minimax runner 加载段 |
| I2 | prompt 模板：GSM8K `Question: {q}\nAnswer with one number only:`；STQ `Question: {q}\nAnswer with Yes or No only:` | minimax runner L154/L163 原文（注：`docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` §1 另记一版 GSM8K 结尾 `Answer in one number:`，两版微异均极简，引用注明出处） |
| I3 | 抽取：`extract_number`（bold 优先→末个数字 token，千分位剥除）；`extract_yesno`（bold 优先→末个 Yes/No token） | minimax runner L113–143（含 2026-09-16 千分位勘误版） |
| I4 | 判分：GSM8K `abs(pred−gold)<1e-3`；STQ `pred==gold.capitalize()`；超时/非 200/空响应→is_correct=0 记 note | minimax runner L216–230 原文 |
| I5 | 采样：temperature=0.0、max_tokens=1024、timeout=30 s/cell、user 单轮、严格不重试不换模型 | minimax runner 文件头与 L69–79（与源 run cells_metadata 逐字段一致） |

> 锚 minimax 而非 9model runner 的理由：9model 用 max_tokens=2048/timeout=60 s（其 JSON 实测），而 5 制品中唯一在库的 30-cell Q&A 制品（minimax 制品）meta.source_data 直接指向 minimax m3 run JSON——**与 5 制品可比＝与 minimax m3 链路同构**。

### 3.2 Runner 四层流水线

```
L0 题源/判分层（0 改动克隆）→ L1 API 调用层（backbone 参数化）→ L2 制品构建层（0 LLM）→ L3 复算层（0 LLM hashlib）
```

- **L0**：读两个冻结 benchmark JSON（只读）组 30 cells 元数据；抽取/判分逐字照搬。唯一允许差异＝MODEL 常量换新 backbone ID。
- **L1**：key 从 runtime `Path().read_text()` 编码循环（GB18030→GBK→UTF-8-sig→UTF-16）→regex 提取→env 注入，literal key 永不落盘/不入 prompt；proxy 6 变量清空；sanity 探针 `'What is 1+1?'` 先行；urlopen 单轮 30 s fast-fail，超时计错不重试；严格模式：no retry / no model switch / no proxy / no TeamoRouter / no GPT-6；**逐 cell append checkpoint**（文件名含 backbone+attempt 双键）。
- **L2**：纯 json/hashlib 变换（沿 `_build_minimax_artifact_2026_09_16.py`），无网络调用；构建自检五项：cells≥20、逐件三列重算、element 零主体标签、拼接锚 `79f8dfa2c296` 核对、源 run JSON 只读。
- **L3**：0-LLM 复算层（§3.4）。

### 3.3 制品 JSON schema（对齐 minimax 制品）

逐字段对齐 `deposon_team/products/minimax_artifact_v_2026_09_16.json`（25,347 B，sha12 `9e1ccbdceacc`，P-K verify PASS）：meta（subject/backbone ID、artifact_count=30、source_data、three_hashes_convention、trust_anchor_5_concat=`d78c42f7bab4|0ff54f8d2f60|a8f81c98ea8a|bff8b1ce1f8c|d9a6a099b905`、trust_anchor_concat_hash=`79f8dfa2c296`、iron_rules 五键 no_llm/no_proxy/no_gateway/no_key/no_frozen_touch 全 true）＋artifacts[30]（artifact_id/source_cell/task/question/llm_output/extracted_answer/is_correct/latency_ms/usage/three_hashes）。

**三列 hash 精确口径**（本提案起草时已在本挂载对 minimax 制品 30/30 逐件＋文件级实测复算通过）：

| hash | 计算式 |
|---|---|
| content | sha256(canonical(core))[:12]；canonical＝json.dumps(core, ensure_ascii=False, sort_keys=True, separators=(",",":"))；**core＝8 字段，不含 artifact_id**（含了就复算不上——实测坑） |
| path | sha256(rel_path + '#' + artifact_id)[:12] |
| anchor | sha256(trust_anchor_5_concat + '\|' + artifact_id + '\|' + content_hash)[:12] |
| 文件级三列 | content＝sha256(canonical(artifacts 全数组))（含各制品自身 three_hashes，不含 meta）；path＝sha256(rel_path)；anchor＝sha256(TA + '\|' + rel_path + '\|' + 文件级 content) |

**新文件命名（全部新落盘，不覆盖既有路径）**：run JSON＋.log＝`results/deposon_v3x_d0_5_<backbone>_30cells_2026_09_17.json`；checkpoint＝同名 `_ckpt.json`；制品＝`deposon_team/products/<backbone>_artifact_v_2026_09_17.json`；复算报告＝`results/_v3x_d0_5_verify_2026_09_17/<backbone>_verify_2026_09_17.json`。

### 3.4 0-LLM 纯 hashlib 复算层（沿 `_verify_15frozen.py`）

(a) 逐制品三列重算（core 8 字段）；(b) 文件级三列重算；(c) **18 frozen 0 触动核验**（16 anchor 路径＋2 anchor JSON，逐条 sha12 比对，完整列表见 §5.4）；(d) 5 制品 baseline 只读核验（before==after，逐件 sha12/size，沿 P-K verify 5 行）；(e) 源 run JSON 只读核验＋题文零改动核验（新制品 question 与 minimax 制品逐 cell sha12 比对，30/30 须全同）。**结构性注意**：2026-09-17 仓库已 trim（verifier/＋.mavis/ 转 archive，816 files）——复算层必须沿 resolve() repo→archive 双基查找，否则 3 项 frozen 假 FAIL（脚本 2026-09-17 更新注记实测教训）。复算耗时亚秒级（P-K verify 全程 elapsed 0.0157 s）。

### 3.5 baseline 对照表（三层，按数据可得性诚实分级）

- **Tier 1｜逐 cell 1:1（判死级核心，全在仓库内）**：新制品 × minimax 制品，30 行：source_cell（对齐键）/question_sha12（30/30 必须全同——I1 复算闸）/extracted_answer（新/基线）/is_correct（新/基线）/Δcorrect/agreement/latency_ms/usage.total_tokens。表尾汇总：GSM8K n/15、STQ n/15、合计 n/30（minimax 基线实测 13/15、9/15、22/30=0.7333）、agreement_rate、均值 latency、总 tokens。
- **Tier 2｜条件逐 cell**：新 × GLM_1/GLM_2/coze 制品（Windows 原机）——worker 先跑 schema 兼容探针（顶层 artifacts[] 且 element 含 source_cell＋extracted_answer 则入同款表，否则降级制品级 3 列 hash 对照）。KIMI 槽位实测只能制品级（22-caption 指纹索引，无 Q&A cell 字段）——如实披露不硬凑。
- **Tier 3｜聚合标量**：新 run JSON summary 字段派生单 backbone 标量，进入 §2 检验量计算；P-L v2 旧输入链（9 模型 T_frac60→L64–66 同序变换→25 网格 R² 全 1.0）作 before 侧存档对照。三层均落 JSON（`results/_v3x_d0_5_…_vs_baseline_2026_09_17.json`）供 Mavis 聚合与论文直引。

### 3.6 30 cells 起步 → 扩 60 cells 的条件（全部满足才扩）

1. 30-cell run 状态 COMPLETE 且 timeout cell ≤1（沿 minimax 重测先例容忍度）；
2. 首轮判读落边缘带（Spearman∈[0.95,1.0) 或分辨力不足/CI 过宽）；
3. 时间余量 ≥40 min（不挤占 18:00–22:00 验证写稿段）；
4. user/Mavis 拍板（铁律 4：禁止未经拍板直跑大网格）。

源可得性已实测：gsm8k 100 题、stq 99 题（keys 1–100）→ gsm8k_16–30＋stq_16–30 全部在冻结源文件内，只读扩档 0 frozen 触动。扩档产物＝新 run JSON＋60 件制品 v2（artifact_001–060）；30-cell 制品与 5 制品基线一律不动；口径不变（60/30/5 制品三者同构可对照）。

### 3.7 执行 SOP（worker 单轮 7 步）

① sanity 探针（失败即停不烧预算）→ ② 30 cells 串行主跑＋逐 cell checkpoint → ③ status 判定：COMPLETE→L2；否则触发一次**整轮重跑**（沿 worker_a 首轮整轮替换先例，不补跑拼盘）→ ④ L2 制品构建＋自检五项 → ⑤ L3 复算＋5 制品 before/after → ⑥ 对照表三层 JSON＋一页汇总 → ⑦ 两次尝试仍 PARTIAL → 如实交 PARTIAL（n/30 checkpoint 全量披露）＋升级 Mavis/user 决策（换 backbone 属新 run 声明，不静默改 model ID）。

### 3.8 v3 runner 洁净性要求（防病灶复发）

P-L v3 runner **全新落盘，严禁复用两个旧模板**：① v1 委外 runner（`_p_l_p_c_finite_size_scaling_runner_2026_09_16.py`）——其 R²=0.4·exp(−2η)·(1−0.1|ν−1.5|) 为构造占位公式，与输入数据无关，max_R2 恒 ≈0.3275（Trae §8 层 2 披露，UNVERIFIED 已降级）；② v2 runner——同序恒等式（§2.1）。新 runner 的 R² 必须是实测 data collapse 拟合（对数变换后线性回归/Rasch 程序，§2.7），UNVERIFIED 降级注释保留为 lineage。若只「换 backbone 重跑」而复用旧 runner，新数据仍流入伪造公式——产出第二个不可验证结论，恰是本轮要消除的病灶类型。

---

## §4 期望阈值

### 4.1 三档判死表（逐行沿邀请函 §2/§4 原文，附操作语义）

| 实验结果 | 拟结论（邀请函原文） | 后续动作（邀请函原文） | n=30 操作语义（本方补充） |
|---|---|---|---|
| 新 backbone 仍 Spearman=1 | 同序单调实证成立 | P-L 假设正式证伪，入 paper §7.2 失败案例 | D=0：30/30 逐 cell 恒等且边际非退化 |
| Spearman ∈ (0.5, 0.95) | data collapse 部分成立 | 跑原 R² 拟合，D7 推送 P-L v3 真实数据 | D≥1（φ≤0.9354）；φ≥0.5 ⟺ 均衡边际下 D≤4–5 或浅嵌套 |
| Spearman < 0.5 | 完全不同序 | 退回 P-L v0 重设计，再等 1 周判死 | D≥6 均衡或深嵌套/大边际差（见 4.5 披露） |
| 任一结果 | 均推动 P-L 论文进展 | PASS/FAIL 都是真数据，不允许 reassign | — |

邀请函 §4 阈值表（<0.95 成立／[0.95,1.0) 补测／=1.0 证伪）与本表同口径：**n=30 下 [0.95, 1.0) 档为空带**（§2.5），该档实际触发源＝退化边际情形或 n=60 扩档（§4.4）。

### 4.2 n=30 分辨力（φ 格点结构，今日实测）

均衡边际（22/22，校准例锚点）φ 格点：均衡翻转对数 k＝0/1/2/3/4/5/6（对应 D＝2k）→ φ＝1.0000/0.8295/0.6591/0.4886/0.3182/0.1477/−0.0227。

- **步长**：均衡边际下每加一对翻转 φ 降 0.1705（＝30/176）——判别粒度为「cell 对」，远细于档位宽度；档内信息由 D 与 triage 承载。
- **单向嵌套族**（新=22 固定、基线=22−j，新 backbone 严格包含基线判对集）：j=1→0.9211，j=2→0.8528，…，j=9→0.5273——「序完全一致只是能力更高」的构型 φ 可低至 0.53。
- **零假设尺度**：独立零假设下 φ 的 SD ≈ 1/√(n−1)＝0.1857；校准例 φ=0.659 ≈ 3.5σ，Fisher 精确检验双侧 p=0.0011（今日实测）。
- **一致率 Wilson 95% CI**：30/30→[0.8865, 1.0]；29/30→[0.8333, 0.9941]；28/30→[0.7868, 0.9815]；26/30→[0.7032, 0.9469]。

### 4.3 0.95 线的判死级含义（两种读法，预登记）

0.95 落在空带内 ⇒ 判定等价于 D=0 vs D≥1，且对 (0.9354, 1] 内任意阈值线**结论不变**（阈值不变性声明）——判死不依赖阈值精调，这是对「0.95 从哪来」的最强回答：它从哪来都不影响结论。**读法一（普查式）**：temp=0.0 且 S2a 审计确认确定性时，单次 run 即普查，φ 是该 backbone-仪器组合的确定值，无抽样误差；「置信」语言严格说只适用于向 30 题超总体的外推。**读法二（cell 抽样式）**：把 30 cells 视为难度超总体抽样，则 D≥1 时一致率 CI 上界 <1（29/30→0.9941），「两 profile 非恒等」在超总体意义下也稳健成立。两种读法都写入报告，不混用。

### 4.4 n=60 升档后（若触发 §3.6 条件）

44/44 均衡格点：k=1(D=2)→0.9148；k=2→0.8295；k=3→0.7443；k=4→0.6591；k=6→0.4886。单向 j=1→**0.9591**（入 [0.95,1) 档）；j=2→0.9211。全局 D=1 极大值 0.9672，D=2 极大值 0.9357。**结论**：n=60 下空带收窄至 [0.9672, 1)，中档恢复且恰好等价于「全 60 cell 中只有 1 个单向翻转」——「部分破单调」获得非空操作语义；null SD 降至 0.1302，Fisher 功效相应提升。

### 4.5 φ<0.5 档的嵌套陷阱披露（预登记措辞防护）

纯嵌套（c=0：新 backbone 判对集严格包含基线）在难度序意义上是「同序」，但 φ 随边际差增大可降至 <0.5（j=13 时 0.39）——落入「完全不同序」档。处置：判死照表执行（不 reassign）；若 c=0 且 φ<0.5，D7 文稿须按嵌套结构披露（「支配性同序」而非「完全不同序」），由 Mavis 裁定最终表述。对称适用（防 b=0 反向嵌套误读）。

### 4.6 S2 次级测量的阈值对应（若触发并拍板）

ρ_S(p_new, p_base)（τ₀=0.7, K=5 通过率向量）：=1.0 ⟺ 逐 cell 通过率 30/30 恒等（远强于二值恒等）；[0.95,1.0) 档分级向量下真实可达（粒度 1/5 档）；(0.5,0.95) 部分同序，档内由逐 cell |Δp| 分布承载；<0.5 强失序。秩序稳定性 ρ_S(v(τ=0), p(τ₀))：温度不破序则加强主档结论表述；温度本身破序则 S2b 交叉结论仅作存疑旁证。**S2 永不覆盖主判死**。

---

## §5 风险评估

### 5.1 网关 A：火山方舟 Coding Plan（国内主通道，铁律 2/6）

| # | 风险 | 既有事实（可溯源） | 缓解（写入 runner） |
|---|---|---|---|
| A1 | 长尾超时/单 cell 卡死 | 9 模型 run：kimi STQ#02 60 s 超时杀死 worker，仅 47/270 cells（17%），85 min wall-clock 被杀；minimax-m3 标注「已知长 prompt 卡死」；gsm8k_1 在 60 s 轮与 30 s 重测轮两轮均超时 | timeout=30 s fast-fail（2048→1024＋60→30 正是 9model 报告「下次建议」）；超时计错不重试；watchdog 25 min/attempt |
| A2 | rate limit/并发变量 | minimax 重测 30 cells 串行 COMPLETE、notes 无 http 错误（clean×28、bold_used×1、timeout_30s×1） | 判死级单 backbone **串行**优先（并发引入 429 混杂）；仅多 backbone 可选并发 |
| A3 | region gate | 火山国内网关，仓库惯例不设代理直连（proxy 6 变量清空） | 沿惯例清空 proxy；海外模型绝不走火山 |
| A4 | wall-clock 失控 | 9 模型 run 85 min PARTIAL；对照：单模型 30 cells 实测 doubao 397 s、minimax 158.4 s | 单模型预算 ≤25 min 硬顶＋逐 cell checkpoint 防「死锁丢全部进度」 |
| A5 | TOS/配额 | coding-plan 订阅配额内推理（9model 同通道 270 call 级别已跑过未触红线） | 不做多 key 轮换、不绕配额，消耗对齐铁律 4 |

### 5.2 网关 B：OpenRouter（海外备通道，铁律 3；仅 reference_only）

| # | 风险 | 既有事实 | 缓解 |
|---|---|---|---|
| B1 | model 白名单 | 铁律 3：只能调非 OpenAI/Anthropic/Google；候选 Nemotron 3.5 合规（§1.1/§1.6 勘误后确切 ID） | 调用前 1-cell sanity 即验路由 |
| B2 | free-tier 速率限制 | embedding 探针实测 2 失败 cell 均为 20 s read timeout（注「可能 free-tier 速率限制」） | 串行＋失败只记不重试；批间 1–2 s 间隔或付费档（~$0.003） |
| B3 | **baseline 准入（本方案最大网关级风险）** | user 17:38 拍板「OpenRouter 不进 V3X baseline」 | 若聚合选 OpenRouter backbone：输出只作 reference_only，制品 meta 如实标注；判死级主张主 backbone 落火山 |
| B4 | 延迟量级 | embedding 通道实测 avg 1593–2113 ms/call；chat 通道无仓内探针数据（不假设） | 时间预算取 chat 情景上界 |
| B5 | key 通道 | 惯例 runtime 从 env 注入，literal key 永不落盘 | 沿铁律 1 同款处理 |

### 5.3 网关 C：minimax.chat 官方 API（不进执行计划）

仓库内无 minimax.chat 通道 key 事实（铁律 5：不假设钥匙存在）。若 user 侧配置则按铁律 1 runtime 读；否则不进入执行计划。**派工注意**：邀请函 §8——minimax task() 本轮只接受 mavis/explorer/worker/verifier 4 系统 agent，实例走 `.minimax/agents/agent-XXX/` 路径。

### 5.4 frozen 触动风险（18 frozen 完整列表＋0 触动声明）

记账口径（沿 `_verify_15frozen.py` 头注释）：**16 anchor 路径＋2 anchor JSON 自身＝18 frozen total**：

| # | 路径 | 期望 sha12 | # | 路径 | 期望 sha12 |
|---|---|---|---|---|---|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（anchor JSON ①） | `03c6c01f3697` | 9 | `corpus/v20/index.json` | `8423ffe266af` |
| 2 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | 10 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json`（anchor JSON ②） | `b41c98bf90cc` |
| 3 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | 11 | `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` |
| 4 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | 12 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` |
| 5 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | 13 | `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` |
| 6 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | 14 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` |
| 7 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | 15 | `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` |
| 8 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | 16 | `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` |

（`conservation.py` V0=`4bdec2683f06` 为 Q2 metadata，不在 16 锚列表，本实验同样不动。）

**0 触动声明**：本实验**不新增任何 frozen 触发条件**。写入面白名单仅 4 类新文件（§3.3 命名清单＋对照表 JSON＋verify 报告）；读取面白名单：2 个 benchmark details（只读）、minimax run JSON（只读，sha12 `fbb7677b9cd5` 本挂载实测）、5 制品（只读）、`_verify_15frozen.py`（只读）、P-L v2 结果 JSON（只读）。**兜底**：任何不变量被意外触动 → 立即停跑＋沿 Q2 reconcile 流程先冻结新锚再回算（邀请函 §7 原则）；L3 复算层 (c)/(d) 两步是该声明的机读化执行。

### 5.5 时间预算（1 backbone × 30 cells，含失败重试与 PARTIAL 兜底）

实测锚点（同构口径：30 cells、temperature 0.0）：minimax-m3 串行全程 158.4 s（avg 5,280.2 ms/cell）；doubao-seed-2.0-lite 397 s（60 s/2048 参数档）；最坏单 cell 30 s；同规模 0-LLM verify 0.0157 s；9model 反面教训 85 min PARTIAL。

| 阶段 | 估时 | 说明 |
|---|---|---|
| sanity 探针 | ≤0.5 min | 1 call，失败即停 |
| 30-cell 主跑（串行 1 attempt） | 3–16 min | 典型 ≈3 min（5.3 s/cell）～最坏 15 min（全 cell 30 s 超时）；实测区间上界 6.6 min |
| 失败整轮重跑（上限 ×1） | +3–16 min | sanity 挂/status≠COMPLETE/timeout>1 触发 |
| L2 制品构建＋自检 / L3 复算 | 各 <1 min | 纯 JSON/hashlib |
| 对照表＋一页汇总 | 10–30 min | 30 行×10 列＋汇总指标 |
| **单 backbone 总计（顺利/含 1 次重跑）** | **≈5–20 / 30–60 min** | 与邀请函「30–60 min 派 worker」口径一致；15:00–18:00 窗口余量 >2 h |
| 60-cell 扩档（若触发） | +6–32 min | 主跑×2＋同套 L2/L3；第 2 backbone（若聚合选 2 个）≈×2 串行，均在窗口内 |
| PARTIAL 兜底 | watchdog 25 min/attempt ×2 封顶 | 如实交 n/30 checkpoint 全量＋升级拍板；禁止为凑 COMPLETE 静默改参数或补跑拼盘 |

**预算红线**：18:00 前必须拿到 30-cell COMPLETE 或如实 PARTIAL（挤占 18:00–22:00 验证＋P-L v3 制品窗口；22:00 D7 文稿死线不可让）。

### 5.6 工程风险（小项，均有前科）

Windows GBK console 强制 reconfigure utf-8；key 文件 GB18030 编码循环；canonical json 三参数（ensure_ascii=False/sort_keys/separators）缺一 hash 漂移；core 8 字段不含 artifact_id（实测坑）；文件名 backbone+attempt 双键防秒级同名覆盖；hash 敏感行 python repr＋len 双确认不凭显示；挂载 vs 原机双世界——执行主体是 worker 于原机（本挂载只读副本；Tier 2 的 3 件盘外制品与 key 文件只在原机可及）。

---

## §6 主线其他可能方向的增补实验设计（用户 11:05 指示并入）

**范围纪律**：本节只用已落地事实（三素材＋仓库一手），零发明；全部为**条件触发的增补选项**，任何一条的启动均须 user/Mavis 拍板（铁律 4），不挤占主判死（§1–§5）的 15:00–18:00 窗口；全部不触动 18 frozen（写入面均为新文件或纯只读）。

### 6.1 方向 A：9-model run 7 个 sanity-200-0-cells 槽位补跑 → 跨 backbone φ 分布估计

- **仓库事实**：`results/deposon_volcengine_9model_30cells_2026_09_10.json` 中 7 个模型 sanity http 200 但 0 cells（85 min wall-clock 超时未跑到）：`minimax-m3`、`doubao-seed-2.1-turbo`、`deepseek-v4-flash`、`glm-5.3`、`doubao-seed-evolving`、`glm-5.3-flash`、`deepseek-v4-pro`；另 kimi-k2.7-code 17/30 PARTIAL。其中 minimax-m3 已有独立 I5 口径基线 run 无需补跑——**实际补跑池＝其余 6 个**。
- **动机**：判死对目前为单点估计（新 backbone × minimax 基线）。补跑后可得**多 backbone 的 φ 点估计族**→ 跨 backbone φ 经验分布（代替单点），同时为 §2.7 Rasch 矩阵提供 M 行（backbone 行数从 2 增至最多 8），提升可分性拟合与 LOCO 的判别力。聚合表达「多 backbone 点估计代替单点」（阿兰备忘 §1.4 同向）。
- **设计骨架**：逐模型沿 §3 全套口径（I1–I5＋四层流水线＋制品 schema）；注意 9model 原参数为 max_tokens=2048/timeout=60 s——**补跑必须用 I5 口径（1024/30 s）才与 minimax 基线可比**，故所有槽位均为新 run，不沿用 9model 旧 cells（doubao-seed-2.0-lite 的 26/30 亦属 2048/60 s 口径，如需并入须同口径重跑）。
- **成本**：每模型主跑 3–16 min（§5.5 同口径）＋ sanity 1 call；6 模型串行合计约 18–96 min〔推导：6×(3–16)〕＋每模型 L2/L3 <1 min。落在 15:00–18:00 窗口外沿，建议列为窗口后/次日晨选项。
- **触发条件**：主判死完成且回传后；预算与 API 配额允许（铁律 4）；user/Mavis 拍板。
- **0 frozen 声明**：全部新落盘（新 run/制品/复算报告），9model 旧 JSON 只读不动。

### 6.2 方向 B：n=30→60 cells 升档路径

- **动机**：n=30 下 [0.95, 1.0) 档为空带（§2.5）；n=60 后空带收窄至 [0.9672, 1)，中档恢复＝「全 60 cell 中恰 1 个单向翻转」（j=1→0.9591），null SD 0.1857→0.1302，Fisher 功效提升——「部分破单调」档获得非空操作语义，三档表中间档可被真实触发。
- **设计骨架**：沿 §3.6 已预登记的扩档程序：gsm8k_16–30＋stq_16–30 在冻结源内只读扩档；60 件制品 v2（artifact_001–060）；30-cell 制品与 5 制品基线不动；口径不变三者同构。60 档同时是 closeout 报告 §2.4「多尺寸重做（30/45/60/100）」建议中的落位档（`deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` 一手）。
- **成本**：主跑 +6–32 min（§5.5）＋同套 L2/L3（秒级）。
- **触发条件**：§3.6 四条件全满足（COMPLETE 且 timeout≤1；边缘带/CI 过宽；时间余量 ≥40 min；拍板）。
- **0 frozen 声明**：只读扩档（源文件不动），产物全部新文件。

### 6.3 方向 C：条件式次级连续测量 S2

- **动机**：回应 Trae 分辨率批评的连续测量承接（§2.5 第 3 条）：二值主统计量之外，per-cell 通过率向量提供分级粒度（K=5 时 1/5 档），使 [0.95,1.0) 档在分级向量下真实可达。
- **设计骨架**：S2a（确定性审计：K=3 重复采样、I5 全项不变、＋90 calls ≈8 min）默认建议开启；S2b（受控 τ₀=0.7、K=5、双侧对称补跑、300 calls ≈26 min 串行）条件触发＋须拍板，触发条件 T1–T4（主对 φ=1.0 / φ<0.5 / 退化情形）。温度轴仅存在于 S2b 旁证层，永不覆盖主判死（§4.6）。
- **成本**：S2a ＋约 8 min；S2b ＋约 26 min（若触发）。
- **触发条件**：S2a 随主实验默认开启（聚合拍板）；S2b 仅 T1–T4 触发＋user/Mavis 拍板（铁律 4）。
- **0 frozen 声明**：minimax 侧对称补跑亦为全新文件。

### 6.4 方向 D：MiniMax M3 对照零成本复用

- **动机**：邀请函 §1 将 M3（via minimax.chat）列为「仅作对照」；仓库事实是 M3 既有基线走火山（§1.8）——对照目的（同 prompt 同评分 scale 下同序性）**零成本即可满足**，且避免网关差异混入 backbone 归因。
- **设计骨架**：即 §1.8——复用 `deposon_volcengine_minimax_m3_30cells_2026_09_10.json` → `minimax_artifact_v_2026_09_16.json` 制品链，作为 Tier 1 判死对的基线侧；对照表 30 行已内建于 §3.5。
- **成本**：0 API call；0-LLM 复算亚秒级（P-K verify 0.0157 s 锚点）。
- **触发条件**：主实验启动即自带，无额外触发。
- **0 frozen 声明**：纯只读。

### 6.5 方向 E：多尺寸轴（30/45/60/100 cells）——D+1 升级选项

- **一手溯源**：`deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` §2.4 建议「重做 P-L 沿 9 model × 4 尺寸档（30/45/60/100 cells）＋真实 data collapse R² 实算」——收口报告自身对该主线路径的既有建议；方法学上与 §2.7 有限尺寸标度类比（θ_b↔系统尺寸、δ_i↔标度变量、σ↔标度函数）逐项对应。
- **动机**：Trae 提案 §2/§0 的连续规模轴主张（多尺寸）与 Rasch 拟合在此汇流：≥3 个尺寸 bin 才能做真实 data collapse 的跨尺寸拟合；今日 30-cell 预算不可达（爱丽丝 §4.1 明示「多尺寸轴需要 ≥3 个尺寸 bin，今日 30-cell 预算不可达，标注为 D+1 升级选项」）。
- **设计骨架**：4 档（30/45/60/100）×最多 9 模型（沿方向 A 补跑池＋既有 I5 口径行）；题源可得性实测 gsm8k 100 题/stq 99 题〔推导：45/60/100 档（如 100 档＝gsm8k 50＋stq 50）均在该源内〕；R² 为实测拟合（§2.7 程序），严禁复用 v1/v2 runner（§3.8）。
- **成本**：单档主跑 3–16 min/模型（30 档口径）〔推导：按 cell 数线性放大，45/60/100 档分别约为 30 档的 1.5/2/3.3 倍〕× 模型数 × 4 档——远超今日窗口，故为 **D+1（D7 之后）升级选项**。
- **触发条件**：D7 推送后主线延伸拍板；须与方向 A 联动启动。
- **0 frozen 声明**：全部新文件，冻结源只读。

### 6.6 与 Trae 提案 §7 的聚合关系

Trae 提案 §7 已列五项主线增补（E-1 minimax 22/30 下游传播审计、E-2 P-K source_cell 对齐审计、E-3 P-I 真标签、E-4 P-M 量纲、E-5 9-model bootstrap CI）——与本节方向正交互补，本提案不重复展开，建议 Mavis 聚合时统一调度排序。本方方向 A 与其 E-5（bootstrap CI）在「多 backbone 分布化」意图上同向，实现路径不同（A 为新增实测行，E-5 为既有 9 模型 T_frac 的重抽样）。

---

## 尾部

### A. 7 铁律遵守声明（逐条）

| 铁律 | 本提案落实 |
|---|---|
| 1. API key runtime `Path().read_text()` 读，不入 prompt/不落盘/不写入检测规则 | §3.2 L1；检测/自检脚本自身纳入无 key 扫描（历史教训：检测规则自身也可能泄漏） |
| 2. 国内模型走火山引擎 | §1.1 主/备 1 路由（coding/v3） |
| 3. 海外模型走 OpenRouter，只调非 OpenAI/Anthropic/Google | §1.1 备 2（Nemotron 3.5 合规）＋§5.2 B1 |
| 4. 节省原则（小规模验证边际，不一次跑 300 cells） | 30 cells 起步；扩档/增补全部须拍板（§3.6/§6） |
| 5. 钥匙不写进任何 markdown/code/memory | 本文 0 key；全部交付物同扫 |
| 6. 国内用火山、OpenRouter 仅备用 | §1.5/§5.2 B3（user 17:38 baseline 准入，reference_only） |
| 7. 不动 `.minimax/agents/verifier/mavis/.builtin/scripts/` | 写入面白名单无该树（§5.4） |

### B. 不预设 PASS 声明（诚实降级）

本提案不倾向三档拟结论表任一档：新 backbone 若仍 Spearman=1（并列校正后）→ 按邀请函 §2 入「P-L 假设证伪」；若 ∈(0.5, 0.95) → 走真实 R² 拟合；若 <0.5 → 退回 v0 重设计档。任何结果均如实入对照表与 verify 报告，**禁止修饰实验以得 PASS，禁止 reassign**。P-L v2 §6.7 降级不翻案——本实验只提供替代它的真数据；即使实验失败，v2 的降级披露保留为 paper 局限性章节（沿邀请函 §2 诚实降级承诺）。仓内校准例 φ=0.659 只证明判别力存在，不预测新 backbone 结果。

### C. 边界不变量表（沿邀请函 §7，任何触动需先冻结新锚再回算）

| 项目 | 不变量值/路径 |
|---|---|
| 18 frozen 完整列表 | 16 anchor 路径＋2 anchor JSON 自身（§5.4 全表） |
| `conservation.py` V0 | `4bdec2683f06`（沿 Q2 reconcile；不在 16 锚列表，本实验不动） |
| 4 plugin spec | 0 触动 |
| P-G V0/V0.1 | 0 触动 |
| 5 制品 baseline JSON | KIMI（24,150 B，`efe05ad775de`）/GLM_1（19,685 B，`268ab1239a8a`）/GLM_2（13,150 B，`39732a92b5c9`）/coze（10,978 B，`fee04170aa73`）/MiniMax（25,347 B，`9e1ccbdceacc`），只读 |

### D. 内部分工溯源（简短）

本提案由 GLM 方起草组三岗协同产出：**调研岗**（backbone 选型、OpenRouter 目录一手拉取与 4 处名称勘误、家族覆盖核查）→ **架构岗**（检验量数学定义、空带定理与格点实测、阈值统计学理由、Rasch 拟合程序、今日 0-LLM 校准复算）→ **实验岗**（I1–I5 锚定、四层流水线与制品 schema、18 frozen 列表与时间预算、API 风险表）→ 主笔整合成文。三岗内部素材今日已交群，Mavis 聚合只需本文（自含），如需逐项溯源见 §E 索引直查仓库一手文件。

### E. 溯源文件索引（全部只读引用）

| # | 路径 | 用途 |
|---|---|---|
| 1 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | 邀请函（三档表/7 铁律/时间表/边界表） |
| 2 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json`/`.py`/`.log` | 判死对基线（I1–I5 逐字来源；COMPLETE 22/30；sha12 `fbb7677b9cd5`） |
| 3 | `deposon_team/products/minimax_artifact_v_2026_09_16.json` | 制品 schema 基准（30/30 三列 hash 本挂载复算通过） |
| 4 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | 5 制品认证（5/5 PASS） |
| 5 | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | 校准对 glm 侧（协议偏差披露） |
| 6 | `results/deposon_benchmark_v1_4_gsm8k_details.json`/`…_strategyqa_details.json` | 题源（100/99 题，扩档可得性） |
| 7 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | v2 的 t 向量＋同族分歧旁证（9 模型 T_frac） |
| 8/9 | `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py` ＋ `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | v2 根因代码（L64–66）＋结果（25 网格 R²=1.0，UNVERIFIED） |
| 10 | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json`/`deposon_ark_models_2026_09_10.json` | 火山 catalog（130 模型；DeepSeek 13/Qwen 5/GLM 3 ID） |
| 11 | `results/deposon_volcengine_9model_30cells_2026_09_10.json` | 9 模型 sanity 全记录＋85 min PARTIAL＋7 个 0-cell 槽位（§6.1） |
| 12/13 | `docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` ＋ `VOLCENGINE_GLM_LATEST_30CELLS_V2_2026_09_10.md` | v3 端点 404 教训＋prompt 模板另版；glm-latest 22/30＋sanity 输出风格 |
| 14 | `docs/V3X/OPENROUTER_5MODEL_30CELLS_2026_09_10.md`/`EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md` | OpenRouter 限额事实＋key 可用＋user 17:38 baseline 约束 |
| 15 | `results/gt3_prior_cache/deepseek-v4-pro-260425__*.json`（6 件） | DeepSeek V4 真实调用痕迹 |
| 16 | `deposon_team/plugins/_verify_15frozen.py`/`_build_minimax_artifact_2026_09_16.py` | L3 复算层/L2 构建层母本（16 锚表） |
| 17 | `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | §2.4 P-L v2 UNVERIFIED 披露＋多尺寸重做建议（§6.2/§6.5 一手） |
| 18 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | Trae 提案（交叉核验/聚合对象） |
| 19 | `shared/or_models_snapshot_2026_09_17.json` | OpenRouter 444 模型摘要快照（今日一手拉取） |

---

**GLM（Z.ai GLM 5.x）方**
**2026-09-17（周四）CST**
