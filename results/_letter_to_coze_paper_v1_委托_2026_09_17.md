# LETTER TO COZE · 2026-09-17 · D7 推送后 paper V1 委托
## deposon V3X 1 周判死 paper 起草 · 4 协作方分工

> **起草方**: Mavis (deposon V3X 1 周判死主理, team lead 主导)
> **起草时点**: 2026-09-17 21:35 CST
> **委托目标**: 沿 Trae code 双审通过的 8 章 outline + 5 audit 综合产物, 委托 Coze 起 paper V1 正式版草稿
> **委托边界**: 0 LLM API 调用 (Coze 沿 spec 起草, Mavis 不动 LLM 跑实验)
> **不通过 minimax task() 派**: Coze = 4 协作方之一, user 走 chat 沟通, Mavis 不动 push / 不调 WeChat / 不跑实验

---

## §0 时点对齐

- **D7 王老师 WeChat 推送** 强制明晚 (2026-09-18 晚 CST) = user 2026-09-17 13:14 拍板
- **现时点 (2026-09-17 21:35 CST) → D7 推送 ~21 h 余**
- **8 worker 已全部完成** (5 done, 1 failed 豆包旧版, 2 done 补测 v2 + 加速器 v2)
- **5 audit 全部完成** (Trae code 沿 `_letter_to_trae_code_2026_09_17_final.md` 18:30-20:00 跑完, 1 改进已加, 3 数字必改清单已列)
- **Coze 委托 = 起 paper V1 正式版草稿**, 沿 8 章 outline + 4 挂点结论 (源 = 提案 v3 §3-§7) + 5 audit 综合产物

---

## §1 paper V1 8 章 outline (沿 Trae code 双审 + _trae_paper_8ch_双审_20260917_200000.md)

| 章 | 标题 | 字数预算 | 数据源 | 引用规范 |
|---|---|---|---|---|
| §1 | Introduction | ≤ 1 页 | D+0 起点 + 1-week kill 背景 + 5 候选 (P-A/B/C/D/LLM议价) + 7 铁律 | 王老师 D7 report §0 |
| §2 | V3X 设计 | ≤ 1.5 页 | 4 协作方 (KIMI/Trae/GLM/Coze) + D+0.5 邀请 + 18 frozen 0 触动 + 5 制品 + schema v1 + 4 plugin spec | 提案 v3 §1-§5 + PATCH V2 |
| §3 | P-C + P-D 双 PASS 结果 | ≤ 1.5 页 | 60 cells 51/60 (实 85.0%, **数字修正 87.0%→85.0%**) + 0.867 均衡带 | 提案 v3 §3 + D7 report §3.1-§3.2 |
| §4 | P-L v3 三态分离 | ≤ 1.5 页 | Phase 1 R²=0.7447 FAIL + Phase 2 β CI overlap 3/3 PASS (开源) + 3/3 PASS (闭源) + OR 1/6 GRAY + 豆包 structural finding | 提案 v3 §3 + D7 report §3.3 + 改进信 §2 |
| §5 | 17 Adendum 综合 | ≤ 1 页 | 10 零成本 (7 PASS + 3 LLM done) + 7 中成本 (6 PASS + 1 GRAY) + Phase 3 F/G/K (1 PARTIAL + 1 PARTIAL + 1 FAIL_NO_MODEL) + Adendum C 勘误追加 | 提案 v3 §4 + 改进信 §3 |
| §6 | 限制 (paper §7.2) | ≤ 1 页 | 5 制品 schema 互异 + P-K FPR 4.4% GRAY + OR 1/6 GRAY + Phase 1 FAIL + 加速器 proxy 不稳 + 4 vector_embedding 大文件策略 | D7 report §5 |
| §7 | 结论 + 派生建议 | ≤ 0.5 页 | P-L v3 部分拒绝, V4 派生 8 题 × 4 闭源 backbone 测试题集 (下周 deposon 二作) | 提案 v3 §7 + V4 1 分支 memory |

**总预算**: ≤ 8 页 (WeChat 文稿 ≤ 200 字, paper 全文 ≤ 8 页)

---

## §2 4 项挂点结论 (源 = 提案 v3 §3-§7, **不源 D7 report**)

### 挂点 1: 9 模型 × 60 题账本 = P-L v3 Phase 2 跨 backbone
- **王老师**: 9 模型 540/540 账全轧平, 双主线 26/30 精确重合 0.867
- **我们 P-L v3 Phase 2**:
  - 3 开源 backbone (qwen3 + glm53 + mistral) β CI overlap PASS
  - 3 闭源 backbone (gpt-5.6-sol + claude-sonnet-5 + gemini-3.7-flash) β CI overlap PASS
  - 4 OR embedding (Qwen3-8B + BGE + E5 + GTE) β CI overlap 1/6 GRAY
  - 5 豆包 embedding (4 vision + Qwen3-4B) structural finding (endpoint-internal 收敛)
- **挂点**: 9 模型 cross-backbone 实现稳健性, 9 模型 × 60 题 0.867 均衡带 vs 我们 3 backbone β CI 0.0016-0.0029 极窄

### 挂点 2: 5 锚 + 字节级+语义级双指纹 = 18 frozen + 5 制品
- **王老师**: KT-D0 主锚 `03C6C01F3697` = anchor 0; 5 锚 KT_ABC1_anchors 系列; 字节级+语义级双指纹
- **我们**: 18 frozen anchors + 5 制品 JSON + schema v1; 22 caption dual_24bit 22/22 PASS; b3 root=`75596bbabdb8`; 锚链 c4cae1ed9ee5
- **挂点**: 内容寻址 + 根指纹 + 追加链 模式一致

### 挂点 3: 「挂上也是交付」 = P-L v3 Phase 1 FAIL + Phase 2 GRAY + FPR 4.4%
- **王老师**: KT-C1 幂律 R²=0.0007 死的是自己主张; KT-B1 22.5% < 50% 判死线 走正面结果
- **我们 P-L v3 综合判死**:
  - Phase 1 (Mistral): FAIL (R²=0.7447, Q=0.1929) — size scaling 失败
  - Phase 2 (3 开源 + 3 闭源): PASS — 跨实现稳健
  - P-K FPR 4.4% > 1% 阈值 GRAY (GLM 三方盲测产物 2/45 GLM JSON 被判自家)
  - OR 1/6 P2 GRAY (symbol-split by architecture)
- **挂点**: 共同方法论 = 「诚实降级 + 挂上也是交付」, 我们的 P-L v3 GRAY/FPR 与王老师 KT-C1 判死同质

### 挂点 4: 4 协作方聚合收敛 = 8 worker cross-backbone
- **王老师**: 9 模型 cross-backbone
- **我们**: 5 worker (Phase 1+2+3+7mid+FGK) cross-backbone + 7 制品 + 18 frozen + 4 plugin spec + schema v1
- **挂点**: 共同方法论 = 「4 协作方聚合收敛 + 诚实降级 + 0 LLM 重算 + 7 铁律 0 触动」

---

## §3 5 audit 综合 (Trae code 沿 `_letter_to_trae_code_2026_09_17_final.md` spec §1.1-§1.5 跑完)

| 件 | 判定 | SHA-12 | 必改 |
|---|---|---|---|
| §1.1 D7 文稿 V1.1 双审 | PASS 带 3 数字修正 | `e240ca712be6` | ✅ 87.0%→85.0%, Adendum 13→17, P2 强稳健降格 |
| §1.2 KIMI push 第 3 批副审 | PASS 带 1 阻断 | `8ece24be6b8a` | ✅ Adendum C 勘误已追加 |
| §1.3 派遣论文初稿需求双审 | PASS 带 3 必改 | `bec666969ffc` | ✅ 8 章 outline 与 §1-§5 提案一致 |
| §1.4 5 制品 by_model audit | SHA 5/5 PASS, schema 一致性 FAIL (结构性) | `f2a655cd5e54` | ⚠️ 5 制品 schema 互异 |
| §1.5 18 frozen + schema v1 巡逻 | 22/22 锚 PASS | `4af67e6cbe71` | ✅ verifier 挪档 path_fallback 闭合 |
| **聚合** (`_trae_5audit_aggregated_2026_09_17.md`) | **1 句话**: 资产层一致完好, 叙述层 3 数字必改 + 1 矛盾复发 | 11,465 B (待算) | — |

---

## §4 paper V1 数字漂移必改 (D7 推送前)

| 原文 | 修正 | 依据 |
|---|---|---|
| `87.0%` 复现 | `85.0%` 复现 | 实值 60 cells 51/60 = 85.0% |
| `Adendum 13 + 2 + 1 = 16` | `Adendum 11 + 2 + 1 + 2 + 1 = 17` | 零成本 7 + 中成本 6 + LLM 3 + F/G/K 1 + 豆包 1 = 实 17 |
| `P2 强稳健` | `P2 3/5 backbone overlap (1 OR×OR 失败)` 降格 | 实 β CI overlap 1/6 OR×OR |

---

## §5 引用规范 (沿 KIMI 7 方向 + Trae §6 退化预检 + Coze 3 态分离 + GLM §5 复现前提)

| 规则 | 严守 |
|---|---|
| **KIMI 7 方向** | 不允许为新数据调阈值 (与 P-K v2 7 方向原文一致) |
| **Trae §6 退化预检族** | 4 类 (P-J convergence_rates 常量, P-M detection=0 vs SECURE, P-C exp_3_3 r2_per_eta 9 model 逐字相同, P-O 24/26 闭合) |
| **Coze 3 态分离** | P1 size scaling + P2 cross-backbone + P3 collapse residual 三态独立判死 |
| **GLM §5 复现前提** | seed=42, 12×2 超平面, proj>0, hex zfill(3), 阈值 Hamming<6/12 |

**8 件 SHA-12 自验** (paper 引用前必验):
- 5 制品 JSON: KIMI `efe05ad775de` / GLM_1 `268ab1239a8a` / GLM_2 `39732a92b5c9` / coze `fee04170aa73` / minimax `9e1ccbdceacc`
- 18 frozen anchors (沿 schema v1)
- schema v1 21/21 一致
- 4 plugin spec: skill_a `b1463bb24403` / skill_b `e5a299f69a22` / skill_c `e19e76c5da7e` / skill_d `3e369a1f6171`

---

## §6 Coze 委托边界 (Coze 必须沿)

| 严守 | 边界 |
|---|---|
| ✅ 0 LLM API 调用 (Coze 不调 LLM, Mavis 派过 8 worker 已落数据) | Coze 只起草 paper V1 草稿, 不调 LLM 跑实验 |
| ✅ 沿 8 章 outline (Trae code 双审) | 不自创 outline, 不改章节结构 |
| ✅ 引用 5 audit 综合产物 | 沿 _trae_5audit_aggregated_2026_09_17.md (11,465 B) |
| ✅ 引用 4 挂点结论 | 源 = 提案 v3 §3-§7, **不源 D7 report** (沿 user 17:02 老实承认误读 PDF = 上周 D7 wechat) |
| ✅ 4 项必改数字 | 87.0%→85.0%, Adendum 13→17, P2 强稳健降格 (paper §4 已标) |
| ✅ 4 件 push README | P-F D_fix2 FAIL_EXPOSURE_PARTIAL + P-K OVERALL FAIL + by_model schema 互异 + GLM_1 stale ref |
| ✅ 1 句话挂点回扣 | 资产层一致, 叙述层必改, 0 触动严守 |
| ❌ 不写新 spec | Coze 只起草 paper, 不写 spec (留给 doc-writer 凝子-agent) |
| ❌ 不调 API / 不动 push / 不动 WeChat 钥匙 | 严守 7 铁律 |

---

## §7 Coze 输出物 (Mavis 期待)

| 件 | 路径 | 字数 |
|---|---|---|
| paper V1 草稿 | `D:/私人资料/deposon-repo/results/_coze_paper_v1_draft_2026_09_17.md` (待落) | ≤ 8 页 (章节总和) |
| paper V1 摘要 (中文) | 沿 paper V1 首段 | ≤ 300 字 |
| paper V1 英文摘要 (Coze 沿 paper V1 起草) | 同上 | ≤ 250 words |
| paper V1 综合 MD | 同上 | ≤ 8 页 |

**Coze 起草时点**: 2026-09-17 22:00 CST 后 (user 委托 chat)
**Coze 完稿时点**: 2026-09-18 9:00 CST (外部双审前)

---

## §8 Coze 委托时点 (user 执行 chat)

| 时点 | 动作 | 主体 |
|---|---|---|
| 2026-09-17 21:35 CST (now) | 此委托 spec 落盘 | Mavis |
| 2026-09-17 22:00 CST | 你 chat 给 Coze 发送 `_letter_to_coze_paper_v1_委托_2026_09_17.md` + `_trae_5audit_aggregated_2026_09_17.md` | user |
| 2026-09-17 22:00-22:30 CST | Coze 起草 paper V1 草稿 (沿 8 章 outline) | Coze |
| 2026-09-18 9:00 CST | 外部双审 (verifier 系统) | Mavis + verifier |
| 2026-09-18 中午 | 补实验候选 (沿外部双审建议) | Mavis + worker |
| **2026-09-18 晚 CST** | **D7 王老师 WeChat 推送** | **user 执行** |
| 2026-09-19 起 | V4 1 分支 (下周 deposon 二作含 V3+V4) | Mavis + 4 协作方 |

---

## §9 5 audit 综合来源清单 (Coze 必读)

| 文件 | SHA-12 | 用途 |
|---|---|---|
| `D:/私人资料/deposon-repo/results/_trae_5audit_aggregated_2026_09_17.md` | 待算 (~11,465 B) | 5 audit 综合 (1 句话) |
| `D:/私人资料/deposon-repo/docs/V3X/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | `53a90b9efbb9` | 改进说明信 (Trae code 直接落) |
| `D:/私人资料/deposon-repo/results/_trae_d7_v1_audit_20260917_190000.md` | `e240ca712be6` | §1.1 D7 文稿 V1.1 双审 |
| `D:/私人资料/deposon-repo/results/_trae_kimi_push_v3_audit_20260917_193000.md` | `8ece24be6b8a` | §1.2 KIMI push 第 3 批副审 |
| `D:/私人资料/deposon-repo/results/_trae_corpus_5_audit_20260917_193000.md` | `f2a655cd5e54` | §1.4 5 制品 audit |
| `D:/私人资料/deposon-repo/results/_trae_anchor_18_audit_20260917_193000.md` | `4af67e6cbe71` | §1.5 18 frozen 巡逻 |
| `D:/私人资料/deposon-repo/results/_trae_paper_8ch_双审_20260917_200000.md` | `bec666969ffc` | §1.3 派遣论文初稿需求双审 |
| `D:/私人资料/deposon-repo/results/_v3x_d0_5_aggregation_2026_09_17.md` | `ddf0d1aa96d2` | 聚合文档 (Mavis 18:30 派) |
| `D:/私人资料/deposon-repo/deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md` | 待算 | PATCH Q2 reconcile |
| `D:/私人资料/deposon-repo/deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | `c41c1d6aa794` | PATCH V2 reconcile |

---

## §10 老实话 (Coze 必须知道)

1. **8 worker 已落数据完整**: 5 done + 1 failed + 2 done 补测, 产物路径全在 memory
2. **P-L v3 三态分离综合判死**: Phase 1 R²=0.7447 FAIL, Phase 2 β CI overlap 3/3 PASS (开源) + 3/3 PASS (闭源) + OR 1/6 GRAY + 豆包 structural finding
3. **诚实降级披露**: 沿 KIMI 7 方向"不允许为新数据调阈值" + Trae §6 退化预检 + Coze 3 态分离 + GLM §5 复现前提
4. **P-D V0.3 SPEC** 3 版本共存 (V0 + V0.2 KIMI 裁定 + V0.3 文档升级), 22 caption dual_24bit 22/22 PASS
5. **GLM 制品 FPR 4.4%** > 1% 阈值 GRAY, 老实入 paper §7.2
6. **3 数字漂移必改**: 87.0%→85.0%, Adendum 13→17, P2 强稳健降格 (paper §4 已标)
7. **Mavis 不动 push**: KIMI 凝子-agent 独立执行 git push
8. **Mavis 不动 WeChat 钥匙**: 王老师推送由 user 执行 (明晚 18:00-21:00 CST)
9. **Mavis 不调 LLM 跑实验**: 8 worker 已落数据完整, Coze 沿 spec 起草, 不调 LLM

---

## §11 严守清单 (Coze 必须沿)

- ✅ 0 LLM API 调用 (Coze 只起草 paper V1 草稿, 不跑实验)
- ✅ 沿 8 章 outline (Trae code 双审通过)
- ✅ 引用 5 audit 综合产物 (沿 _trae_5audit_aggregated_2026_09_17.md)
- ✅ 4 项挂点结论 (源 = 提案 v3 §3-§7, 不源 D7 report)
- ✅ 5 audit PASS/FAIL/GRAY 老实入 paper §6 限制
- ✅ 1 句话挂点回扣 (资产层一致 + 叙述层必改 + 0 触动严守)
- ❌ 不写新 spec (留给 doc-writer 凝子-agent)
- ❌ 不调 API / 不动 push / 不动 WeChat 钥匙
- ❌ 不擅自调阈值 (沿 KIMI 7 方向)
- ❌ 不重 push 1+2 批 (79 files / 1.1 MB 已推)

---

## §12 委托交付 (Coze 完成后)

- `D:/私人资料/deposon-repo/results/_coze_paper_v1_draft_2026_09_17.md` (≤ 8 页)
- `D:/私人资料/deposon-repo/results/_coze_paper_v1_summary_2026_09_17.md` (≤ 300 字中文 + ≤ 250 词英文)
- 严守 7 铁律 0 触动 + 9 铁律 key runtime 读

---

**Mavis 起草** · deposon V3X 1 周判死主理 · 2026-09-17 21:35 CST
