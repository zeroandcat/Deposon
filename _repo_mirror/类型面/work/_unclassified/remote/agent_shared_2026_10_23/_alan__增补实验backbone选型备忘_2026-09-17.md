# 增补实验 Backbone 选型备忘（提案 §1 素材）

- **调研人**：阿兰-文献调研员（群管理员 2026-09-17 10:29 派单）
- **对应邀请**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md`（Mavis，09:33 CST）
- **任务**：为 P-L v2 Spearman=1 同序单调缺口增补实验选 1 主 + 至多 2 备 backbone
- **纪律**：零推断、全部可溯源、API key 永不入文。挂载仓库全程只读（Read/Glob/Grep，未执行任何写操作）。
- **证据分级**：〔仓〕=挂载仓库一手探针；〔OR〕=OpenRouter 公开模型目录 API 一手拉取（2026-09-17 ~11:05 CST，444 模型，快照存 `shared/or_models_snapshot_2026_09_17.json`）；〔外〕=外部 web 检索（仅辅助定位，不作可用性依据）。

---

## 0. 结论速览

| 槽位 | Backbone | 确切 model ID | 网关路由 | 可用性证据等级 |
|---|---|---|---|---|
| **主** | DeepSeek V4 | `deepseek-v4-pro-ga-260813`（或 `deepseek-v4-flash-ga-260731`） | 火山方舟 coding-plan：`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` | 仓：sanity 200 ×2 + catalog 在列 ×4 + GT3 真实调用缓存 |
| **备 1** | Qwen3 | `qwen3-32b-20250429`（次选 `qwen3-14b-20250429`） | 同上（火山 coding/v3） | 仓：catalog 在列 ×5；**无调用痕迹，须 sanity 先行** |
| **备 2** | NVIDIA Nemotron 3.5 Lightning | `nvidia/nemotron-3.5-lightning`（付费档）或 `nvidia/nemotron-3.5-lightning:free` | OpenRouter：`https://openrouter.ai/api/v1/chat/completions`（直连，不设 proxy） | OR：目录在列；仓：OpenRouter key 可用（embedding 探针 16 calls 全过） |

**重要勘误（影响邀请函候选池 4/7 名称）**：OpenRouter 实际目录（〔OR〕，444 模型）中**不存在** "Nemotron 5"、"Llama 3.4"、"Cohere North（通用档）" 这三个命名的 model ID；"Mistral Large 2" 存在但为 2024-07 旧版。详见 §4。

---

## 1. 5 制品既有基线事实（差异点论证的基础）

### 1.1 认证状态〔仓〕

`results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json`（2026-09-16 23:33，5/5 PASS，18 frozen 0 触动）：

| 制品 | path（verify JSON 记录） | size(B) | sha12 |
|---|---|---|---|
| KIMI | corpus/v20/index_v2_2026_09_16.json | 24,150 | efe05ad775de |
| GLM_1 | 鲍勃 P-K 盲测 GLM 槽位产出/three_way_glm_slot_blind_test JSON | 19,685 | （verify JSON 原文可查） |
| GLM_2 | 鲍勃 P-K 盲测 GLM 槽位产出/glm_artifact_v_2026_09_16.json | 13,150 | 39732a92b5c9 |
| coze | Coze Drive 下载/coze_artifact_v_2026_09_16.json | 10,978 | fee04170aa73 |
| minimax | deposon_team/products/minimax_artifact_v_2026_09_16.json | 25,347 | 9e1ccbdceacc |

### 1.2 30-cell 源数据链路（以 minimax 制品 meta 为样板）〔仓〕

`deposon_team/products/minimax_artifact_v_2026_09_16.json` meta 层：subject=`minimax-m3`；source_data=`results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json`（read-only，0 LLM 抽取）；artifact_count=30（15 GSM8K + 15 StrategyQA）。

源跑参数（`deposon_volcengine_minimax_m3_30cells_2026_09_10.json`，2026-09-10 21:37，COMPLETE 22/30，158.4s）：网关=火山方舟 Coding Plan（coding/v3），temperature=0.0，max_tokens=1024，timeout=30s/cell，不重试。

### 1.3 Prompt format 与评分抽取约定（新 backbone 须对照的差异基准）〔仓〕

源脚本 `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py`（一手）：

- **Prompt 模板**（OpenAI 兼容，messages=[{role:'user'}] 单轮）：
  - GSM8K：`Question: {q}\nAnswer with one number only:`
  - StrategyQA：`Question: {q}\nAnswer with Yes or No only:`
  - 注：`docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` §1 另记一版 GSM8K 结尾为 `Answer in one number:`（两版措辞微异，均极简英文模板，引用时注明出处）。
- **评分抽取约定**：extract_number（**bold 优先 → 最后数字 token**）；extract_yesno（bold 优先 → 最后 Yes/No token）。
- **已归档的抽取缺陷勘误**（minimax 源 JSON `fix_note_extract_2026_09_16`）：gsm8k_4 raw=`"$1,430"` 千分位原误提取 430，修正为 1430，total_passed 21→22。新 backbone 若输出带千分位/货币符须沿用此修正。
- **输出风格的一手观察**（同 prompt 下 backbone 差异实例）：minimax-m3 sanity 返回 `1 + 1 = **2**`（bold 包裹习惯）；glm-latest sanity 返回 `1 + 1 = 2`（无 bold）。抽取函数的 bold 优先设计即为此适配。

### 1.4 已覆盖家族清单（「不同家族」判定的排除表）〔仓〕

| 家族 | 覆盖证据 |
|---|---|
| Kimi/Moonshot | 5 制品 KIMI 槽位；9model 探针 kimi-k2.7-code 17/30 partial |
| GLM（智谱） | 5 制品 GLM_1 + GLM_2 **双槽位**；glm-latest 30-cell V2 22/30（PARTIAL，HTTP 29/30） |
| MiniMax | 5 制品 minimax 槽位（minimax-m3 30 cells 22/30 COMPLETE） |
| coze 主体 | 5 制品 coze 槽位（29 件文档制品） |
| Doubao | 9model 探针 doubao-seed-2.0-lite 26/30 COMPLETE（探针级覆盖） |
| DeepSeek | 仅 sanity 200、0 cells——**无完整 30-cell 数据**（未覆盖） |
| Qwen | **零调用痕迹**（未覆盖） |
| NVIDIA / Meta / Mistral / Cohere | 无任何调用（未覆盖） |

---

## 2. 候选池全 7 成员可用性核验

### 2.1 火山方舟 coding-plan 侧（3 成员）

路由基线〔仓〕：`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`，key 从 env runtime 加载（两枚 ark key 之一，coding-plan 段）。

**(a) DeepSeek V4 —— 证据最强**

| 证据 | 出处〔仓〕 |
|---|---|
| catalog GET /models（2026-09-10 18:00:21，http 200，130 模型）在列 4 个 V4 ID：`deepseek-v4-pro-260425`、`deepseek-v4-flash-260425`、`deepseek-v4-flash-ga-260731`、`deepseek-v4-pro-ga-260813` | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json`；`results/deposon_ark_models_2026_09_10.json` |
| sanity http 200：`deepseek-v4-flash` 1813ms、`deepseek-v4-pro` 1691ms（无后缀别名写法，coding/v3 端点，2026-09-10 21:04；cells 因 9model 全程 85 min wall-clock 超时未跑到） | `results/deposon_volcengine_9model_30cells_2026_09_10.json` |
| `deepseek-v4-pro-260425` ×6 图 GT3 prior 缓存（algorithm_process / biological_taxonomy / geography_world / historical_causality / physics_concepts / project_management）——V4 真实调用痕迹 | `results/gt3_prior_cache/deepseek-v4-pro-260425__*.json` |
| **端点教训**：`deepseek-v3-2-251201` 走 `/api/v3/chat/completions`（非 coding 路径）→ 404 InvalidEndpointOrModel.NotFound，0/30。结论：DeepSeek 必须走 coding/v3 端点 | `docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` |

**(b) Qwen3 —— catalog 在列、零调用痕迹**

catalog 在列 5 个 Qwen ID〔仓〕：`qwen3-8b-20250429`、`qwen3-14b-20250429`、`qwen3-32b-20250429`、`qwen3-0-6b-20250429`、`qwen2-5-72b-20240919`。
9model 探针与 gt3_prior_cache 均**无 Qwen**——无 sanity、无 cell 数据。可用性预期：coding/v3 端点对非 Doubao 家族开放有先例（9model 全部 9 ID sanity 200），但 Qwen 本身未验证，**须 1-cell sanity 先行（成本 1 call）**。

**(c) GLM 5.x —— 家族重复，不建议入选**

- catalog〔仓〕GLM 族仅 3 ID：`glm-4-5-air-20250728`、`glm-4-7-251222`、`glm-5-2-260617`；**glm-5.3 不在目录**（`glm_5_3_present: false`）。
- 9model〔仓〕：`glm-5.3` 与 `glm-5.3-flash`（无后缀写法）sanity 200（1483/1725ms）但 0 cells——与 catalog 无 glm-5.3 并存的事实张力如实记录：chat 端点对无后缀别名宽容路由，GET /models 列表不含。
- glm-latest 别名 30-cell V2〔仓〕：22/30 PARTIAL（gsm8k 13/15 + stq 9/15，HTTP 29/30，90s/cell）。
- **不入选理由**：5 制品已有 GLM_1/GLM_2 双槽位（§1.4），选 GLM 5.x 违反邀请函 §1「推荐与现有 5 制品 backbone 家族不一致」原则，无法支撑「不同家族」论证。

### 2.2 OpenRouter 侧（4 成员）——邀请函名称与实际目录对照

〔OR〕2026-09-17 ~11:05 CST 拉取 `https://openrouter.ai/api/v1/models`（公开端点，无需鉴权），444 模型。快照：`shared/or_models_snapshot_2026_09_17.json`。

| 邀请函候选名 | OpenRouter 实际状态 | 建议处置 |
|---|---|---|
| NVIDIA Nemotron 5 | **无 "nemotron-5" ID**。NVIDIA 通用系最新为 Nemotron 3.5 系列：`nvidia/nemotron-3.5-lightning`（$0.08/M in + $0.2/M out，ctx 262,144，created 2026-08-08）及 `:free` 档（$0，ctx 1,000,000）；另有 `nemotron-3-ultra-550b-a55b(:free)`、`nemotron-3-super-120b-a12b(:free)`、`nemotron-3-nano-30b-a3b` 等 | 按实际目录改推 **nemotron-3.5-lightning** |
| Meta Llama 3.4 | **无 llama-3.4 ID**。Meta 通用系：`meta-llama/llama-4-maverick`（$0.1875/M + $0.6525/M，ctx 1,048,576）、`llama-4-scout`（$0.1/M + $0.3/M）；3.x 止于 `llama-3.3-70b-instruct`（created 2024-12-06，较旧） | 若需 Meta 家族改用 llama-4-maverick；本轮不占推荐名额 |
| Mistral Large 2 | `mistralai/mistral-large-2407`（=Large 2 字面 ID，$2/M + $6/M，created 2024-11-19，较旧较贵）；同厂更新旗舰 `mistralai/mistral-large-2512`（Large 3，$0.5/M + $1.5/M，ctx 262,144，created 2025-12-01） | 若选 Mistral 家族，建议 mistral-large-2512（更便宜且更新，同为 MoE） |
| Cohere North | **无通用对话档 North ID**。唯一 North 系：`cohere/north-mini-code:free`（code 特化，$0，ctx 256,000，moderated）；Cohere 通用系为 `cohere/command-a`（$2.5/M + $10/M） | code 特化与 GSM8K/StrategyQA 通用推理任务错位；作对照需接受此偏移，或改 command-a |

OpenRouter key 可用性〔仓〕：embedding 5-model 探针（`docs/V3X/EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md`）16 calls 全过、layer-2 gate 未触发、直连不设 proxy。但 chat completion 模型无仓库内调用先例（既有探针均为 embedding）——NVIDIA/Mistral/Cohere/Meta 均不在 layer-2 禁调名单（OpenAI/Anthropic/Google）内。
限额事实〔仓〕：`docs/V3X/OPENROUTER_5MODEL_30CELLS_2026_09_10.md` 附录 B——30-cell 测试中 2 cell 20s read timeout，归因疑似 free-tier 速率限制；建议批间加 1-2s 间隔。付费档 30 cells × ~1k tok 成本约 $0.003（nemotron-3.5-lightning 计价），可忽略。

---

## 3. 推荐详述（产出①②）

### 3.1 主推：DeepSeek V4（火山 coding-plan）

- **确切 ID**：`deepseek-v4-pro-ga-260813`（GA 最新，2026-08-13 入目录）；能力/延迟平衡档 `deepseek-v4-flash-ga-260731`。无后缀写法 `deepseek-v4-pro` / `deepseek-v4-flash` 已有 sanity 200 证据，若 GA 全称 ID 调用异常可降级该写法（两者关系沿 9model「无后缀别名可路由」先例）。
- **可用性证据**：见 §2.1(a) 四条（sanity 200 ×2 + catalog ×4 + GT3 缓存 + 端点教训）。候选池 7 成员中唯一具备「网关 sanity + 真实调用痕迹」双证据的未覆盖家族。
- **Prompt format 差异点**：同网关同协议（火山 coding/v3，OpenAI 兼容），§1.3 模板可**逐字复用**，调用路径与 minimax 基线完全同构、仅换 model 字段——同 prompt 异 backbone 的最干净对照。native template 差异体现在输出侧：DeepSeek 系输出风格与 minimax 的 bold 包裹习惯不同（V4 无仓库内完整 cell 输出样本，抽取兼容性需在 sanity/首 cell 验证：确认答案为末 token 数字/Yes-No，无长 reasoning 前缀干扰）。
- **不同家族论证**：5 制品零 DeepSeek（§1.4）；DeepSeek 在仓库内从未有完整 30-cell 数据；V4 为 2026-08 GA 新代。

### 3.2 备 1：Qwen3（火山 coding-plan）

- **确切 ID**：`qwen3-32b-20250429`（catalog 内 Qwen3 dense 最大档）；算力紧张降 `qwen3-14b-20250429`；`qwen2-5-72b-20240919` 为 2024 旧代不推。
- **可用性证据**：仅 catalog 在列〔仓〕；**无任何调用痕迹**。前置动作：先跑 1-cell sanity（1 call 成本）再放全 30 cells。
- **Prompt format 差异点**：同网关同协议，模板逐字复用。Qwen3 系原生带 thinking 输出模式（〔外〕待验证项，仓库无一手）——sanity 时须确认输出形态，必要时在请求参数显式关闭或在抽取端约定只取最终答案段。
- **不同家族论证**：5 制品零 Qwen（§1.4）。

### 3.3 备 2：NVIDIA Nemotron 3.5 Lightning（OpenRouter）

- **确切 ID**：`nvidia/nemotron-3.5-lightning`（付费档，$0.08/M + $0.2/M）或 `:free` 档（$0，ctx 1M）。
- **可用性证据**：〔OR〕目录在列（一手）；〔仓〕OpenRouter key 与直连通路已验证（embedding 探针）。chat 模型在该网关无仓库调用先例——同需 sanity 先行。
- **Prompt format 差异点**：异网关但同 OpenAI 兼容协议，模板逐字复用；海外系 native 输出风格与国内系家族距离最大——若 Spearman 仍=1，「同序单调与家族无关」的结论最有力（对照价值最高）。
- **不同家族论证**：5 制品零 NVIDIA（§1.4）；NVIDIA 训练范式（开放权重+开放数据配方）与已覆盖 6 家族均不同源。

---

## 4. 落选与勘误说明

| 候选 | 处置 | 依据 |
|---|---|---|
| GLM 5.x（火山） | 落选 | 家族重复：GLM_1/GLM_2 双槽位 + glm-latest 22/30 已覆盖（§2.1c） |
| Nemotron 5 / Llama 3.4 / Cohere North | **名称勘误** | OpenRouter 目录无此三 ID（§2.2）；提案 §1 若沿用邀请函原名单将无法落地，须按 §2.2 对照表改写 |
| Mistral Large 2 | 有条件保留 | 字面 ID `mistral-large-2407` 在列但旧且贵；建议聚合时与 `mistral-large-2512` 二选一并写明确切 ID |
| MiniMax M3 | 仅对照（见 §5） | MiniMax 家族已被 5 制品覆盖 |

---

## 5. MiniMax M3 对照处理建议（产出③）

邀请函将 MiniMax M3（via minimax.chat 官方 API）列为「仅作对照」。**仓库事实：M3 既有基线走的是火山 coding-plan（`minimax-m3`，22/30 COMPLETE），并非 minimax.chat 官方 API**〔仓〕。建议：

1. **对照直接复用既有 30-cell 基线**（`deposon_volcengine_minimax_m3_30cells_2026_09_10.json` → minimax_artifact 链路），0 成本、0 frozen 触动；对照目的（同 prompt 同评分 scale 下，新 backbone 与 M3 输出是否同序）已可满足。
2. **不建议**为对照新开 minimax.chat 官方 API 通路：新增 key/端点/TOS 三重未验证变量，且「网关差异」会混入 backbone 归因，削弱对照效力。
3. M3 不可作正式 backbone：MiniMax 家族已在 5 制品内（§1.4），不满足「不同家族」。

---

## 6. 一句话风险画像（产出④，供提案 §5）

- **DeepSeek V4（主）**：端点路由必须 coding/v3（v3 路径 404 前科）+ 串行跑须防 wall-clock 超时（9model 85 min 教训，建议沿 minimax 专跑模式 30s/cell、fail-fast 不重试）；无 region gate，TOS 沿用既有 ark key access scope。
- **Qwen3（备 1）**：零调用证据为最大不确定项，sanity 先行（1 call）；其余风险同 DeepSeek。
- **Nemotron 3.5 Lightning（备 2）**：free 档速率限制有 2/30 read timeout 前科（批间加 1-2s 间隔或直接用付费档 ~$0.003）；无 region gate（仓库直连证据）；layer-2 禁调名单不涉及 NVIDIA。

---

## 7. 与 Trae 提案 §1 的交叉核验（3 处事实修正/补强）

Trae code 已提交 `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md`（主 Mistral Large 2 / 备 Qwen3 / 对照 Cohere North）。本调研对其 §1 的补强：

1. **Mistral Large 2 确切 ID 确认**：`mistralai/mistral-large-2407` 在 OpenRouter 在列（$2/M + $6/M，2024-11 快照日期）；但同厂 `mistralai/mistral-large-2512`（Large 3）更便宜（$0.5/M + $1.5/M）且更新——若 Trae 取「MoE 架构差异」意图，2512 同为 Mistral MoE 系，聚合时建议二选一写明 ID。
2. **Cohere North 无通用档**：OpenRouter 唯一 North 系 ID 为 `cohere/north-mini-code:free`（code 特化 + moderated）；Trae 的「非 RLHF-dominant 训练范式」对照若坚持 Cohere 家族，须接受 code 特化偏移或改 `cohere/command-a`。
3. **Qwen3 风险补强**：Trae 将 Qwen3 列为火山通道备选但未标注其零调用痕迹——本备忘补充「sanity 先行」前置条件（§3.2）。

（注：Trae 提案主张「换 backbone 不足以破同序单调，根因在离散 0/1 评分测法，须加连续温度轴」——该论断属实验设计层，超出本备忘 backbone 选型范围，不评判，仅提供选型事实。）

---

## 8. 证据文件索引（全部只读引用）

| # | 文件 | 用途 |
|---|---|---|
| 1 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | 邀请函（候选池、7 铁律、时间表） |
| 2 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | 5 制品认证（sha12、path、5/5 PASS） |
| 3 | `deposon_team/products/minimax_artifact_v_2026_09_16.json` | minimax meta 层 source_data 链路 + 30 artifacts |
| 4 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` / `.py` / `.log` | M3 30-cell 源跑：参数、prompt 模板、抽取函数、千分位勘误 |
| 5 | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` | 火山 catalog：130 模型、GLM 3 ID、glm_5_3_present=false |
| 6 | `results/deposon_ark_models_2026_09_10.json` | catalog 明细：DeepSeek 13 / Qwen 5 完整 ID 清单 |
| 7 | `results/deposon_volcengine_9model_30cells_2026_09_10.json` | 9 模型 sanity 200 全记录 + 85min 超时 note |
| 8 | `docs/V3X/LLM_CODINGPLAN_30CELLS_2026_09_10.md` | v3 端点 404 教训 + prompt 模板另版 |
| 9 | `docs/V3X/VOLCENGINE_GLM_LATEST_30CELLS_V2_2026_09_10.md` + run log | glm-latest 22/30 + sanity 输出风格 |
| 10 | `docs/V3X/OPENROUTER_5MODEL_30CELLS_2026_09_10.md` | OpenRouter free-tier 限额事实（2/30 timeout） |
| 11 | `docs/V3X/EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md` | OpenRouter key 可用 + 直连 + layer-2 gate |
| 12 | `results/gt3_prior_cache/deepseek-v4-pro-260425__*.json`（6 件） | DeepSeek V4 真实调用痕迹 |
| 13 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | Trae 提案（交叉核验对象） |
| 14 | `shared/or_models_snapshot_2026_09_17.json` | 〔OR〕OpenRouter 444 模型摘要快照（今日拉取，随本备忘交付） |

---

**阿兰-文献调研员**
**2026-09-17（周四）CST**
