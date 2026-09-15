# Feshbach RAG 30 Cells 边际验证报告

**日期**: 2026-09-10 22:04-22:09 CST
**Worker**: Feshbach RAG (B 路径,user 21:57 C = A+B)
**模型**: `doubao-seed-2.0-lite` (火山方舟 Coding Plan,严格 baseline 对比)
**目的**: 验证沿 v3 §6 Feshbach 共振公式 S_eff(E) 重排序 22 caption top-3,能否提升 LLM 答对率

---

## §1 测试环境

| 项 | 值 |
|---|---|
| 模型 | `doubao-seed-2.0-lite` (Volcano Ark Coding Plan) |
| 端点 | `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` |
| auth | `ark-de0b484e-0889-46...e219` (runtime env,永不入 prompt/JSON/disk) |
| proxy | 未设 (火山国内,严守 user 17:38+17:41) |
| max_tokens | 1024 |
| timeout | 60s/cell |
| temperature | 0.0 |
| 30 cells | 15 GSM8K + 15 StrategyQA (沿用 worker_b/c 同一组 cell_id) |
| gamma (凝华率) | 0.1 |
| RAG top-K | 3 |
| 总耗时 | 282.5s (avg 9.4s/cell, min 4.2s, max 29.1s) |

**严禁条款自检** (7 铁律):
- [x] coding-plan key runtime 读 GB18030 → env
- [x] 不设 proxy (HTTP_PROXY/HTTPS_PROXY/ALL_PROXY 全清)
- [x] 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan
- [x] key 永不入 prompt / JSON / disk (`auth` 字段 `ark-de0b484e-0889-46...e219` 截断)
- [x] 30 calls 严格 (不重试 / 不切 model / 全程 `doubao-seed-2.0-lite`)
- [x] 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` 未动
- [x] 4 SPEC V0.1 + v19 + v21 + corpus/v20 未动

---

## §2 Feshbach-aware RAG 流程

### 2.1 物理公式 (v3 §6)
```
S_eff(E) = S_bg - (S_bg |W><W| S_bg) / (E - E_0 + i*Γ/2)
```

### 2.2 实施步骤

```
[1] 22 caption SVD 2D 投影 (已有,76.5% var)
    S_bg = 22 caption × 2D coords (svd2_coords)
    ↓
[2] Feshbach 参数
    W = S_bg.mean(axis=0)         # 22 caption 平均向量
    |W> = W / |W|                 # 单位化
    E_0 = mean(|s|) for s in S_bg # 22 caption 平均幅度 ≈ 0.873
    Γ = 0.1                       # 凝华率
    ↓
[3] 30 cells 题目编码 (E)
    E_vec = [n_chars_norm, n_words_norm] × E_0
    归一化到 22 caption 能量尺度
    ↓
[4] 沿 S_eff 通道 similarity
    S_bg_perp = S_bg - proj(S_bg, W)         # 22 caption 垂直分量
    E_perp    = E - proj(E, W)                # 题目垂直分量
    sim(c, q) = <S_bg_perp[c] · E_perp[q]>   # 内积 (cosine)
    ↓
[5] top-3 caption (沿 S_eff 距离最近)
    每 cell 取 sim 最高的 3 个 caption
    ↓
[6] 拼 prompt
    "Context (3 most relevant concepts, ranked by Feshbach S_eff similarity):
     - {caption_id} (sim={score})
     - {caption_id} (sim={score})
     - {caption_id} (sim={score})
     Question: {q}
     Let's think step by step.
     Answer with one number only, ending with **N** format."  (GSM8K)
     or
     "Answer with Yes or No only, ending with **Yes** or **No** format."  (StrategyQA)
    ↓
[7] doubao-seed-2.0-lite 答
    ↓
[8] 提取器: **N** 粗体优先 → fallback 末位数字
```

### 2.3 关键观察

**所有 30 cells 拿到同一组 top-3 caption**: `S2_n35, L_algorithm_process, S1_n45`

原因:22 caption SVD 2D 投影 76.5% var,但 W 沿主轴方向,S_bg_perp 大部分都很小且接近;
E 沿 W 投影远大于垂直分量,所以 perp similarity 信号弱,排序被数据噪声主导。

**Sim 分数**: 全部 ~0.99999999 (浮点精度极限),显示 perp 分量几乎正比,排序不稳定。

---

## §3 30 cells 结果

### 3.1 汇总

| 指标 | 值 |
|---|---|
| gsm8k 通过 | 14/15 = 93.3% |
| strategyqa 通过 | 11/15 = 73.3% |
| **total_passed** | **25/30 = 83.3%** |
| verdict | **PASS** (≥24 阈值) |

### 3.2 答错 5 cells

| cell_id | task | pred | gold | 失败原因 |
|---|---|---|---|---|
| gsm8k_7 | gsm8k | 36.36 | 36.0 | 算术精度差(可能是 "8% of 4" 解释) |
| strategyqa_5 | stq | No | Yes | 推理错向(陷阱诱因) |
| strategyqa_7 | stq | Yes | No | 推理错向(陷阱诱因) |
| strategyqa_9 | stq | No | Yes | 推理错向(陷阱诱因) |
| strategyqa_10 | stq | Yes | No | 推理错向(陷阱诱因) |

### 3.3 答对 25 cells (略)

gsm8k: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15 (14 个)
strategyqa: 1, 2, 3, 4, 6, 8, 11, 12, 13, 14, 15 (11 个)

---

## §4 4 baseline 对比

| 路径 | 模型 | RAG | 答对/30 | 答对率 | 备注 |
|---|---|---|---|---|---|
| **A 路径(no LLM)** | 理论模拟 | n/a | 0/30 | 0% | NOISE 边际 |
| **B 路径(本任务)** | doubao-seed-2.0-lite | **Feshbach S_eff RAG** | **25/30** | **83.3%** | 22 caption SVD 2D 76.5% var |
| 旧 RAG baseline | doubao-seed-2.0-lite | 2048-d cosine | 24/30 | 80.0% | 净 -1 回归 |
| no-RAG baseline | doubao-seed-2.0-lite | 无 | 26/30 | 86.7% | 当前最佳 |
| 对照 | V4.1-Flash | 无 | 25/30 | 83.3% | 不切超 doubao-seed-2.0-lite |

**净效果 (vs no-RAG)**: 25/30 vs 26/30 = **-1 cell / -3.3pp** ❌ 仍回归
**净效果 (vs 旧 RAG)**: 25/30 vs 24/30 = **+1 cell / +3.3pp** ✅ 微改善
**净效果 (vs A 路径 NOISE)**: 25/30 vs 0/30 = **+25 cell** ✅ 绝对 LLM 价值

### 4.1 关键解读

1. **Feshbach RAG 比 no-RAG 差 1 cell**: SVD 2D 投影的 Feshbach 公式没有产生有效重排序信号
   - 22 caption SVD 2D 76.5% var,W 沿主轴方向,perp 分量在 2D 中几乎全 0
   - 全部 30 cells 拿到同一 top-3 (S2_n35, L_algorithm_process, S1_n45)
   - 退化为"加 3 个 caption 名到 prompt 头部",对 LLM 推理有干扰但无增益
2. **Feshbach RAG 比旧 2048-d cosine RAG 好 1 cell**: 旧 RAG 加 22 caption 全列同样干扰更强
3. **A 路径 (0% 边际) 完全验证**: 不调 LLM 的理论模拟没有任何预测能力

---

## §5 7 铁律自检

| # | 条款 | 状态 | 证据 |
|---|---|---|---|
| 1 | coding-plan key runtime 读 | ✅ | KEY_OK enc=gb18030 truncated=ark-de0b484e-0889-46...e219 |
| 2 | 不设 proxy | ✅ | proxy_cleared (HTTP_PROXY/HTTPS_PROXY/ALL_PROXY 全清) |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | ✅ | 全程 doubao-seed-2.0-lite |
| 4 | key 永不入 prompt/JSON/disk | ✅ | auth="ark-de0b484e-0889-46...e219" 截断 |
| 5 | 30 calls 严格 (不重试/不切 model) | ✅ | 30/30 全部 200 OK,全 doubao-seed-2.0-lite |
| 6 | 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` 未动 | ✅ | 未访问 |
| 7 | 4 SPEC V0.1 + v19 + v21 + corpus/v20 未动 | ✅ | 未访问 |

---

## §6 下一步

**结果**: 25/30 = 83.3% (PASS 阈值 ≥24, ✅ PASS, 但 < 26/30 baseline)
**判决**: **no-RAG 仍是最佳**;Feshbach RAG 边际验证 = **NOISE 偏正 +1**

### 6.1 V3X 终极形式确认

| 候选 | 答对率 | verdict | 适用 |
|---|---|---|---|
| no-RAG | 26/30 = 86.7% | **最佳** | V3X 默认 |
| 旧 2048-d RAG | 24/30 = 80% | 回归 | 不采用 |
| **Feshbach RAG (本任务)** | **25/30 = 83.3%** | **PASS 但 < baseline** | **不采用** |
| 理论模拟 (A 路径) | 0/30 = 0% | NOISE | 不用 LLM |

**推荐 V3X 默认配置** = `no-RAG + doubao-seed-2.0-lite` (26/30 = 86.7%)
Feshbach RAG 失败原因:22 caption SVD 2D 投影 76.5% var 但 W 沿主轴,perp 分量近 0,公式退化为噪声。
若要继续探索 Feshbach RAG,需用 **完整 2048-d 嵌入**(目前文件只保存 SVD 2D,全嵌入未存盘)。

### 6.2 候选 (P-A/B/C/D) 后续

- 1 周判死 V3.X 5 候选启动: 沿 user 21:57 决策,**B 路径(本任务) = FAIL marginal → 沿 v2 决策**
- Wang WeChat 报告: 1 条消息,**Feshbach RAG = 25/30 PASS but -1 vs no-RAG**
- 不再为 P-A/B/C/D 设 RAG;**no-RAG 锁定**为 V3.X 默认

---

## §7 附录

- 源数据: `D:\私人资料\deposon-repo\results\deposon_feshbach_rag_30cells_2026_09_10.json`
- 脚本: `D:\私人资料\deposon-repo\results\deposon_feshbach_rag_30cells_2026_09_10.py`
- 日志: `D:\私人资料\deposon-repo\results\deposon_feshbach_rag_30cells_2026_09_10.log`
- 22 caption 嵌入: `D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json` (SVD 2D, 76.5% var)
- 30 cells 题目: `D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json` + `_strategyqa_details.json`
- 基线: `D:\私人资料\deposon-repo\results\deposon_volcengine_9model_30cells_2026_09_10.json` (no-RAG doubao-seed-2.0-lite 26/30)
- 旧 RAG: `D:\私人资料\deposon-repo\results\deposon_volcengine_worker_b_2026_09_10.json` (24/30)
- A 路径: `D:\私人资料\deposon-repo\results\deposon_cpath_simulation_2026_09_10.json` (0% 边际)

**报告完成时间**: 2026-09-10 22:09 CST
