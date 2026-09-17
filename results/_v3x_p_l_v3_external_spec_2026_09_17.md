# P-L v3 真重测 External Agent 任务 spec
## deposon V3X D7 前 C 重测任务, Mavis 起草 (2026-09-17)

> **任务类型**: 实验复核 worker (recheck-runner 或 worker system agent)
> **派单方**: Mavis (根 root session) — 严守「禁止自行实验」原则
> **背景**: P-L v2 Spearman=1 沿 Trae §6.7 诚实降级,需真重测破局

---

## §0 任务边界

**做**:
1. 选新 backbone (与 V3X 同序单调 backbone 完全不同)
2. 跑 30 cells (GSM8K + StrategyQA subset)
3. 算 Spearman + R² + data collapse fit 状态
4. 输出 P-L v3 JSON + 1-page MD

**不做**:
- ❌ 0 LLM 重 hash / 0 LLM budget 滥用
- ❌ 不动 18 frozen anchors (16 anchor + 2 anchor JSON)
- ❌ 不动 5 制品 JSON (corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/)
- ❌ 不动 schema v1 (`_v3x_frozen_schema_v1.json`)
- ❌ 不动 4 plugin spec (skill_a/b/c/d)
- ❌ 不动 verifier/audit (即使 accessible)
- ❌ 不擅自动 verifier/mavis/.builtin/scripts/
- ❌ 不复用 V3X 同序单调 5 backbone (kimi/glm-5.3/doubao-seed-evolving/moonshot-v1-8k/deepseek-v4-pro)
- ❌ 失败 reassign (Spearman=1 也如实披露)

---

## §1 输入资产 (只读)

| 资产 | 路径 | SHA-12 | 说明 |
|---|---|---|---|
| P-F V0 SPEC | docs/V3X/P_F_SPEC_V0.md | `de90faf362c5` | P-L 主源 |
| P-F RESEARCH V0 | docs/V3X/P_F_RESEARCH_2026_09_09.md | `98085df7811a` | P-L 设计 |
| P-F V0 占位 JSON | verifier/handoff/P_F_PREDECISION_2026_09_09.json | `b41c98bf90cc` | P-L V0 placeholder |
| P-F V0.1 JSON (V0.1 真值) | verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json | (待算) | V0.1 真值, 只读 |
| corpus v20 index | corpus/v20/index.json | `8423ffe266af` | corpus 主源 |
| v19 frozen | results/deposon_v19_benchmark_fixes.json | `910c4333eead` | 9 model T/R/A 主表 |
| v21 frozen | results/deposon_v21_gtformal.json | `9d9ae5001c57` | v21 gtformal |
| schema v1 | deposon_team/plugins/_v3x_frozen_schema_v1.json | (待算) | v1 schema |

**所有输入只读, 落新文件前 Test-Path + 校验 SHA-12。**

---

## §2 新 backbone 选择 (推荐顺序)

### 国内 (走火山引擎, ark-key 已就绪)
- DeepSeek V4 (火山方舟 coding-plan)
- Qwen3 (火山方舟)
- 智谱 GLM 5.x (火山方舟)

### 海外开源 (走 OpenRouter, 不受 layer-2 user_id gate)
- NVIDIA Nemotron 5
- Meta Llama 3.4 / 3.5
- Mistral Large 2
- Cohere North

### 严选规则
- 与 V3X 同序单调 5 backbone **完全不同**:
  - ❌ kimi, glm-5.3, doubao-seed-evolving, moonshot-v1-8k, deepseek-v4-pro
- 与 prompt format / 评分 scale 一致性**最低**:
  - 优先选 RLHF 路径差异大 (Nemotron 5 vs V3X) / tokenizer 边界差异 (GLM 5.x vs DeepSeek)

---

## §3 30 cells 测法

### §3.1 数据源
- GSM8K subset (test split 80-80): 取 15 cells (Q1+D2 MATH)
- StrategyQA subset (test split): 取 15 cells (Q3+D4 COMMONSENSE)
- 共 30 cells

### §3.2 评分
- prompt format: 沿现有 V3X 同结构 (Q+A+json schema)
- 评分 scale: 0-1 浮点 (与 corpus/v20/index_v2 同)

### §3.3 算 Spearman + R²
```python
import scipy.stats as stats
import numpy as np
def fit_data_collapse(x, y, log_x, log_y):
    spearman, p_spearman = stats.spearmanr(x, y)
    slope, intercept, r_squared, _, _ = stats.linregress(log_x, log_y)
    return spearman, p_spearman, slope, r_squared
```

### §3.4 期望阈值
- Spearman < 0.95 → data collapse 假设成立 (≥ 95% 置信)
- Spearman ∈ [0.95, 1.0) → 部分破单调, 需补测另一 backbone
- Spearman = 1.0 → 同序单调实证 (PASS/FAIL 都是真数据)

---

## §4 输出物

| 路径 | 类型 | 大小 |
|---|---|---|
| results/_v3x_p_l_v3_<backbone>_<timestamp>.json | 实验数据 | 5-10 KB |
| results/_v3x_p_l_v3_summary_<timestamp>.md | 1-page 报告 | 3-5 KB |

### JSON schema
```json
{
  "target_hypothesis": "P-L data collapse",
  "new_backbone_used": "<backbone_name>",
  "api_vendor": "OpenRouter / 火山方舟",
  "cells_completed": 30,
  "cells_breakdown": {
    "gsm8k": 15,
    "strategyqa": 15
  },
  "spearman": 0.0,
  "spearman_p_value": 0.0,
  "r_squared": 0.0,
  "slope": 0.0,
  "intercept": 0.0,
  "fit_status": "PASS / FAIL / GRAY",
  "iron_7_compliance": {
    "no_llm": true,
    "no_proxy": true,
    "no_gateway": true,
    "no_key_in_prompt_json_disk": true,
    "no_18_frozen_touch": true,
    "no_p_g_v0_touch": true,
    "no_p_g_v01_touch": true,
    "no_plugin_spec_touch": true,
    "no_verifier_mavis_builtin_scripts_touch": true
  }
}
```

### MD 报告模板 (沿 AGENT_TEAM_OPT_V2 8 节)
```
§0 一句话总结
§1 新 backbone + 30 cells 详细数据
§2 Spearman + R² + fit_status
§3 4 候选对账更新 (P-L 状态)
§4 主源 + 交叉源双源稳健性自检 (新 backbone vs V3X)
§5 公式-数值-口径-参数四一致自检
§6 锚 SHA-12 实算
§7 7 铁律严守 0 触动声明
§8 附录: 全部 hash 复算 + 新增工件 SHA-12
```

---

## §5 严守清单

| 类别 | 严守 |
|---|---|
| API key | runtime `Path().read_text()` 读,不入 prompt 不落盘 不写入检测规则 |
| Iron 7 | 0 LLM / 0 proxy / 0 gateway / 0 PAT / 0 锚定触动 |
| 失败披露 | Spearman=1 也按 FAIL 上报,不 reassign |
| 输出位置 | results/_v3x_p_l_v3_<backbone>_<timestamp>.{json,md} |

---

## §6 时点

- 任务 spec 落盘: 2026-09-17 11:00 CST
- 任务派工: Mavis 派 external agent (worker system 或 recheck-runner 凝子)
- D7 (2026-09-18) 王老师 WeChat push 前必须有 P-L v3 结果

---

## §7 报告路径 (3 选 1)

(a) `results/_v3x_p_l_v3_<backbone>_<timestamp>.json` + `.md`
(b) `deposon_team/_designs/V3X_P_L_V3_REPORT_<timestamp>.md`
(c) 凝子-agent 主线报告路径 (沿 user 拍板)

---

**Mavis 起草** · deposon V3X D+0.5 spec · 严守「禁止自行实验」原则
**2026-09-17 11:00 CST**
