# 主线下增补实验设计邀请函
## Deposon V3X 1 周判死 D7 前增补实验 · D+0.5 阶段

**起草日期**：2026-09-17（周四）09:33 CST
**提案截止**：2026-09-17 14:00 CST
**主送协作方**：KIMI-K3 / Trae code / GLM (Z.ai GLM 5.x) / Coze 共 4 方
**起草**：Mavis（deposon V3X 1 周判死主理）

---

## 0. 时点与定位

本邀请函处于 **D+0.5 阶段**——V3 主线已近闭合，仅缺 1 个真实验验证项。背景已锁定如下：

- **V3X 判死**：5 候选 P-A/P-B/P-C/P-D/LLM 议价已评估；其中 **P-C + P-D 双 PASS**，60 cells 51/60 (85.0%) STRONG_PASS；F-3 DELTA 1.05 NOISE 推翻。
- **18 frozen 0 触动**：含 conservation.py V0 = `4bdec2683f06`（沿 Q2 reconcile）；4 plugin spec + P-G V0/V0.1 全 PASS。
- **5 制品 P-K verify 全 PASS**：KIMI (24,150 B) + GLM_1 (19,685 B) + GLM_2 (13,150 B) + coze (10,978 B) + MiniMax (25,347 B)。
- **D7 终极判死**：2026-09-18 王老师 WeChat 推送（用户委托 coze 转，Mavis 不动钥匙）。
- **唯一缺口**：**P-L v2 沿 Trae §6.7 诚实降级**——Spearman=1 由同序单调变量产生，非真实 data collapse 拟合。本邀请函目标即填补此缺口。

---

## 1. 待解决问题（P-L v2 缺口详解）

Trae 在 §6.7 节沿诚实降级原则披露：

> P-L v2 Spearman=1 不是真实 data collapse 拟合，而是**同序单调变量产生的 artifacts**。

**判定依据**：
1. 5 制品 backbone 不同，但 prompt format / 评分 scale 一致 → 输出呈同序单调；
2. 任何同序单调变量之间 Spearman 计算结果恒为 1；
3. Spearman=1 不能支持 P-L v2 的 "data collapse 拟合" 主张。

**结论**：现有 P-L v2 数据不可作为 P-L 主线的实证支撑，必须重测。

---

## 2. 拟结论（事先公开，避免实验设计带偏）

为最大化本轮实验价值，先公开**所有可能的拟结论**，禁止实验设计倾向其中任一：

| 实验结果 | 拟结论 | 后续动作 |
|---|---|---|
| 新 backbone 仍 Spearman=1 | 同序单调实证成立 | **P-L 假设正式证伪**，入 paper §7.2 失败案例 |
| 新 backbone Spearman ∈ (0.5, 0.95) | data collapse 部分成立 | 跑原 R² 拟合，D7 推送 P-L v3 真实数据 |
| 新 backbone Spearman < 0.5 | 完全不同序 | 退回 P-L v0 重设计，再等 1 周判死 |
| 任一结果 | 均推动 P-L 论文进展 | PASS/FAIL 都是真数据，不允许 reassign |

> **诚实降级承诺**：本轮实验不预设 PASS。即使实验失败，P-L v2 的 §6.7 降级披露也保留为 paper 的局限性章节。

---

## 3. 各协作方邀请的具体产出（D+0.5）

请各方在 **2026-09-17 14:00 CST 前** 提交 1 份《增补实验设计提案》，含以下 5 节（任一节缺失即视为未提交）：

### §1 Backbone 选择
- 推荐挑选**与现有 5 制品 prompt format 不一致**的 backbone；
- 候选源（沿 7 铁律第 6 条，国内走火山，海外开源走 OpenRouter）：
  - OpenRouter 调 NVIDIA Nemotron 5 / Meta Llama 3.4 / Mistral Large 2 / Cohere North（海外开源，不受 layer-2 user_id 门控限制）；
  - 火山方舟 coding-plan 调 DeepSeek V4 / Qwen3 / 智谱 GLM 5.x（国内，prompt format 与现存 baseline 不一致）；
  - 自家模型 MiniMax M3 via minimax.chat 官方 API（仅作对照，不作主 backbone）；
- 至少 1 个 + 最多 3 个 backbone。

### §2 同序单调破局方法
- **禁止**"换 prompt format"破局——那是 pass-through，不是真破局；
- 必须是 backbone 内部差异导致的输出分布偏移；
- 阐述预期破局机制（例：RLHF 后训练差异 / attention head 分布差异 / tokenizer 边界差异 / 长上下文衰减差异）。

### §3 测法
- 沿现有 5 制品的 GSM8K + StrategyQA 测试 cell 结构；
- **至少 30 cells**（实验预算够跑 60 cells，但 30 cells 足够判死级别统计）；
- 0 LLM 纯 hashlib 复算层（沿 `_verify_15frozen.py` 兼容）；
- 副产出：原 P-L v2 5 制品输出作 baseline 对照。

### §4 期望阈值
| Spearman | 含义 | 后续 |
|---|---|---|
| < 0.95 | data collapse 假设成立 | ≥ 95% 置信，可直接入 P-L v3 paper |
| [0.95, 1.0) | 部分破单调 | 需补测另一 backbone |
| = 1.0 | 同序单调实证 | P-L 假设证伪 |

### §5 风险评估
- 列出 backbone API 调用风险（rate limit / region gate / TOS）；
- 列出 frozen 触动风险（**本实验不应再触动新 frozen**——任何触动需先冻结新锚再回算）；
- 列出时间预算（1 backbone × 30 cells × 30 min ≈ 实际 30-60 min 派 worker 可完成）。

---

## 4. 协调原则（7 铁律 + 实验纪律）

**7 铁律（任何参与方遵守）**：
1. API key 永远 runtime `Path().read_text()` 读，不入 prompt / 不落盘 / 不写入检测规则；
2. 国内模型走火山引擎（已有 ark-* key，不限区域）；
3. 海外模型走 OpenRouter（只能调非 OpenAI/Anthropic/Google，避免 layer-2 user_id 门控）；
4. 节省原则：小模型跑 30 cells 验证边际，不一次跑 300 cells；
5. 钥匙不写进任何 markdown / code / memory；
6. 国内模型用火山引擎调用，OpenRouter 仅作国外模型备用（已老实承认限制）；
7. 不动 `.minimax/agents/verifier/mavis/.builtin/scripts/`。

**实验纪律**：
- 0 LLM 纯 hashlib 复算层：不依赖 LLM call 来确认实验结果，沿 `_verify_15frozen.py` 模式；
- 18 frozen 完整列表 0 触动：本实验不应新增 frozen 触发条件；
- 诚实降级：Spearman=1 / Spearman<1 都可推动 paper，禁止"修饰实验以得 PASS"。

---

## 5. 提交方式

| 方 | 通道 | 期望反馈格式 |
|---|---|---|
| **KIMI-K3** | KIMI chat 协作窗口 | markdown 提案（1 份） |
| **Trae code** | Trae 协作窗口 | PR comment 或 markdown |
| **GLM**（Z.ai GLM 5.x） | GLM chat | markdown 提案（1 份） |
| **Coze** | Coze bot 消息 | 短文本 + 配套 markdown |

**聚合流程**：Mavis 收到 4 份提案后聚合为 1 份《增补实验设计 V1》→ 用户拍板 → 派 worker 跑实验。

---

## 6. 时间表

| 时间 | 动作 |
|---|---|
| 09:33 CST（now） | 邀请函发出（本文件） |
| 14:00 CST | 各方提案截止 |
| 14:00 – 15:00 CST | Mavis 聚合 + 用户拍板 |
| 15:00 – 18:00 CST | 派 worker 跑实验（沿 30-60 min 单 backbone 估） |
| 18:00 – 22:00 CST | 验证 + 写 P-L v3 制品 |
| 22:00 CST | 提交 D7 王老师 WeChat 文稿草稿（含 P-L v3 真实数据） |
| D7（2026-09-18） | 用户委托 coze 转推王老师 WeChat |

---

## 7. 边界与不变量（任何触动需先冻结新锚）

| 项目 | 不变量值 / 路径 |
|---|---|
| 18 frozen 完整列表 | 16 anchor 路径 + 2 anchor JSON 自身 |
| `conservation.py` V0 | `4bdec2683f06` |
| 4 plugin spec | 0 触动 |
| P-G V0/V0.1 | 0 触动 |
| 5 制品 baseline JSON | KIMI/GLM_1/GLM_2/coze/MiniMax |

任何上述不变量的触动需先冻结新锚再回算（沿 Q2 reconcile 流程）。

---

## 8. 老实话披露（透明起见）

1. **minimax task() 派工限制**：本轮实验 worker 派工只接受 mavis/explorer/worker/verifier 4 系统 agent；如需凝子-pa-deepen（已派 1 次 mavis-trash 删原 deposon-*）需走 `.minimax/agents/agent-XXX/` 实例路径。
2. **P-L v2 §6.7 降级不能翻案**：本邀请函目标不是"重新辩护 P-L v2"，而是**用真实验替代 Spearman=1 的不可验证结论**。
3. **D7 WeChat 文稿由 Mavis 起草 + 你复制粘贴**：Mavis 仍不动 WeChat 钥匙。

---

**Mavis 起草**
**Deposon V3X 1 周判死主理**
**2026-09-17 09:33 CST**
