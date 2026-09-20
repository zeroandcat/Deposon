# LETTER TO TRAE CODE · 2026-09-17 · D+0.5 委托
## deposon V3X 1 周判死 D7 前协同 · 第 4 协作方锚点

> **起草方**: Mavis (deposon V3X 1 周判死主理, team lead 主导)
> **起草时点**: 2026-09-17 18:18 CST
> **起草目的**: 派委托 Trae code 沿 D+0.5 已建立协作关系, 协同 D7 王老师 WeChat 推送 + KIMI push audit + 派遣论文初稿需求 双审
> **委托严守**: 7 铁律 0 触动 (18 frozen + 5 P-G + 5 制品 + schema v1 + 4 plugin spec + verifier/mavis/.builtin/scripts/ 全不修改)
> **不在此委托**: Mavis 不写 spec / 不跑代码 / 不动 WeChat 钥匙 (Trae code 沿 §1-§5 提案继续做文档协同即可, 不需 Trae 跑 P-L v3 实测)

---

## §0 时点对齐

- **D7 王老师 WeChat 推送强制明晚 (2026-09-18 晚 CST)** = user 拍板 2026-09-17 13:14
- **现时点 (2026-09-17 18:18 CST) → D7 推送 ~24 h 余**
- **8 worker 已全部完成** (5 个 done, 1 个豆包旧版 failed, 1 个豆包补测 v2 done, 1 个加速器 v2 done)
- **Trae code 委托 = 派 D+0.5 邀请函 §3.1 第五行 §5 §6 §7 区域**, 沿 Trae code 自身 system prompt "proposal & audit" 角色

---

## §1 5 件待委托任务（沿 D+0.5 邀请函 §3 协作方分工）

### §1.1 D7 王老师 WeChat 文稿 V1.1 草稿双审 (Trae code 主)

**任务**:
- Mavis 起草 V1.1 (含 4 挂点结论, 源 = 提案 v3 §3-§7, 不源 D7 report)
- 派 doc-writer 凝子-agent (agent-0032834a3e04) 写 V1.0 FINAL (14:38 落, 9,891 B)
- 派 doc-writer 凝子-agent 写 V1.1 (含 4 挂点 + 5 worker 进展 + 诚实降级, 18:30 派工)

**Trae code 委托**:
- **audit 模式**: 沿 Trae code 自身 §1-§5 提案对账 V1.1, 确认 4 挂点 (KT-A1/B1/C1/D0) 内容完整
- 不写新文稿 (Mavis 派 doc-writer 写, Trae code 沿 §6 退化预检族 audit)
- 重点: 挂点 §1 与 §2/§3 §4 §5 协同 (不矛盾)
- 产出: audit 报告 (1-2 页, 含 V1.1 是否与 §1-§5 提案一致, 若有偏差列具体差异)

### §1.2 KIMI GitHub push 第 3 批 audit (Trae code 副审)

**任务**:
- KIMI 凝子-agent 已推第 1 批 (25 files) + 第 2 批 (79 files / 1.1 MB)
- 第 3 批待派 (全量收束后), 含加速器 v2 + 豆包 v2 + P-D 实测 + GLM FPR 全部产物
- d7-pusher 凝子-agent (agent-3e0c193da529) audit push 前

**Trae code 委托**:
- **副审模式**: 沿 Trae code §6 退化预检族, 审第 3 批 manifest 是否有:
  - P-J convergence_rates 常量占位
  - P-M detection=0 vs SECURE 自相矛盾
  - P-C exp_3_3 r2_per_eta 9 model 逐字相同
  - P-O 24/26 PASS 闭合状态
  - P-F V0.1 复跑 vs V0 结论一致性
- 产出: 退化预检 audit 报告 (≤ 1 页, 列具体 gap)

### §1.3 派遣论文初稿需求双审 (Trae code 副审)

**任务**:
- Mavis 起草 8 章 outline + 每节内容需求 (§1 Introduction / §2 V3X 设计 / §3 P-C + P-D 双 PASS / §4 P-L v3 三态分离 / §5 17 Adendum / §6 限制 / §7 结论 + paper §7.2 / §8 派生建议)
- 沿 KIMI 7 方向 + Trae §6 退化预检 + Coze 3 态分离 + GLM §5 复现前提
- 引用规范: 5 制品 + 18 frozen + 4 plugin spec + schema v1

**Trae code 委托**:
- **副审模式**: 沿 §1-§5 提案对账需求, 确认:
  - §3 P-C + P-D 双 PASS 数据 完整 (60 cells 51/60, 87.0%)
  - §4 P-L v3 三态分离 (Phase 1 R²=0.7447 FAIL, Phase 2 β CI 重叠 3/3 PASS, P2 verdict 跨 backbone 强稳健)
  - §5 17 Adendum (10 零成本 + 7 中成本) PASS 13 + GRAY/UNVERIFIED 2 + FAIL_NO_MODEL 1
- 重点: §3 §4 §5 与 Mavis 沿 §1-§5 提案对账, 不矛盾
- 产出: 8 章 outline 双审报告 (≤ 2 页, 列具体 gap 或与 §1-§5 不一致处)

### §1.4 5 制品 by_model 维护 audit (Trae code 副审)

**任务**:
- 5 制品 JSON (corpus/v20/by_model/{KIMI,GLM_1,GLM_2,coze,minimax}/) 已就位
- SHA-12 5/5 验过
- v2.0 all.json 索引同步
- P-D V0.3 SPEC 已落 (与 V0 + V0.2 共存, 3 版本)
- file trim 后 5 制品路径不动 (README 强引用)

**Trae code 委托**:
- **副审模式**: 沿 §6 退化预检族, 审 5 制品是否还有:
  - placeholder 制品 (空 dict, 缺 caption 字段, 缺 verified_at 字段)
  - hardcoded 制品 (与 run_history 字段对账, 9 model 验证状态)
  - 不一致制品 (5 制品之间时序 / 维度 / 输出格式不同)
- 产出: 5 制品 audit 报告 (≤ 1 页, 列具体 gap)

### §1.5 18 frozen + schema v1 巡逻双审 (Trae code 副审)

**任务**:
- 16 frozen anchors + 5 P-G anchors 已 0 触动 (沿 schema v1)
- v0/v1 verify 16/16 + 5/5 PASS (含 archive fallback)
- B2.2 schema v1 已落 (12,919 B)
- PATCH V2 reconcile 文档已落 (6,802 B)
- 锚链 B3 canonical c4cae1ed9ee5 一致 (P-D 实测 22/22 PASS)

**Trae code 委托**:
- **副审模式**: 沿 §6 退化预检族, 审 18 frozen 是否还有:
  - 占位锚 (5 锚实际只有 1 个真值)
  - 复用锚 (KT_D0 主锚与 PD2 复现/EIS 独立雷同)
  - 不一致锚 (anchor[0] = 7d6d3d39fad8, 但 verifier/runs/2026-09-04_pd_v0.jsonl 缺失)
- 产出: 18 frozen audit 报告 (≤ 1 页, 列具体 gap)

---

## §2 委托边界 (Mavis 主导, Trae code 协同)

| 项 | Mavis | Trae code | 边界 |
|---|---|---|---|
| 实验设计 + 派工 + 调 agent | ✓ | ✗ | Mavis 主导, Trae code 不调度 |
| 写文稿 / spec | ✗ (派 doc-writer) | ✗ (Trae code 沿 §1-§5 提案) | Mavis 派 doc-writer 写文稿; Trae code audit 沿自身提案 |
| 跑实验 / 算 Spearman/R² | ✗ (派 worker) | ✗ | Mavis 派 worker 系统 + 凝子-agent 跑 |
| audit (read-only) | 部分 (大方向) | ✓ (Trae code 5 件 audit) | Trae code 副审, Mavis 主理 |
| GitHub push | ✗ (Mavis 不动 push) | ✗ (KIMI 凝子-agent 执行) | KIMI 凝子-agent 独自执行 git push |
| 调 WeChat API | ✗ (Mavis 严守) | ✗ | user 自行推送 |

---

## §3 5 件 audit 产出标准 (Trae code 严守)

| 件 | 产出 | 大小 | 时点 |
|---|---|---|---|
| §1.1 D7 文稿 V1.1 双审 | audit_报告.md | ≤ 2 页 | 18:30 CST 派, 19:00 CST 收 |
| §1.2 KIMI push 第 3 批副审 | audit_报告.md | ≤ 1 页 | 19:00 CST 派, 19:30 CST 收 |
| §1.3 派遣论文初稿需求双审 | outline_双审_报告.md | ≤ 2 页 | 19:30 CST 派, 20:00 CST 收 |
| §1.4 5 制品 audit | audit_报告.md | ≤ 1 页 | 19:00 CST 派, 19:30 CST 收 |
| §1.5 18 frozen audit | audit_报告.md | ≤ 1 页 | 19:00 CST 派, 19:30 CST 收 |

**严守**: 5 件 audit 报告 ≤ 7 页总 (沿 §6 退化预检族纪律), 不可沿 §1-§5 提案为题外展。

---

## §4 派遣纪律 (Trae code 必须沿)

- **read-only**: 5 件 audit 全 read-only, 不写脚本, 不跑实验, 不动 corpus
- **沿 §1-§5 提案**: 任何 audit 结论必须能溯源到 §1-§5 提案某节
- **0 LLM 重算**: 不调 LLM 跑 Spearman/R²/β CI, 沿 8 worker 已落数据 audit
- **严守 7 铁律**: 18 frozen + 5 P-G + 5 制品 + schema v1 + 4 plugin spec + verifier/mavis/.builtin/scripts/ 全不修改
- **诚实降级**: 5 件 audit 任一 FAIL 老实入 Mavis 报告 (不 reassign)
- **挂点回扣**: 5 件 audit 完成后, 给出"5 件一致 / 不一致"总结 + 1 句话挂点回扣, 沿 D7 report §3 模式

---

## §5 Trae code system prompt 沿 (你已有 system prompt)

- **目标**: 与 Mavis 协同 D7 WeChat + KIMI push audit, 不重复 doc-writer 起草, 不重 worker 跑实验
- **做**: read-only 副审, audit 报告
- **不做**: 写 spec / 跑实验 / 调 LLM / 改 corpus / 改 spec
- **包含 deposon 项目专属**: 5 P-? 提案 §1-§5 + 退化预检族 §6 + 不动 §7

---

## §6 5 件 audit 委托交付 (Trae code 完成后落)

| 路径 | 落盘 | SHA-12 | 时点 |
|---|---|---|---|
| `D:/私人资料/deposon-repo/results/_trae_d7_v1_audit_20260917_190000.json` | 5 件 audit 综合 (1 JSON) | 待算 | 19:00 CST |
| `D:/私人资料/deposon-repo/results/_trae_d7_v1_audit_20260917_190000.md` | 5 件 audit 综合 (1 MD) | 待算 | 19:00 CST |
| `D:/私人资料/deposon-repo/results/_trae_corpus_5_audit_20260917_193000.md` | 5 制品 audit | 待算 | 19:30 CST |
| `D:/私人资料/deposon-repo/results/_trae_anchor_18_audit_20260917_193000.md` | 18 frozen audit | 待算 | 19:30 CST |
| `D:/私人资料/deposon-repo/results/_trae_kimi_push_v3_audit_20260917_193000.md` | KIMI push 第 3 批 audit | 待算 | 19:30 CST |
| `D:/私人资料/deposon-repo/results/_trae_paper_8ch_双审_20260917_200000.md` | 8 章 outline 双审 | 待算 | 20:00 CST |

---

## §7 时点表 (5 件 audit 派工收口)

| 时点 | 动作 | 主体 |
|---|---|---|
| **18:18 CST** (now) | 此委托落盘 | Mavis |
| 18:30 CST | 派 doc-writer 凝子-agent 写 D7 文稿 V1.1 | Mavis |
| 19:00 CST | 派 Trae code 凝子-agent 5 件 audit (主+副) | Mavis |
| 19:30 CST | 5 件 audit 综合 MD 落盘 | Trae code |
| 20:00 CST | 8 章 outline 双审 MD 落盘 | Trae code |
| 20:00 CST | 派遣论文初稿需求 Mavis 写 | Mavis |
| 21:00 CST | KIMI push 第 3 批 manifest Mavis 准备 + d7-pusher audit | Mavis + d7-pusher |
| 22:00 CST | user 委托 KIMI 凝子-agent 执行 git push | user |
| **2026-09-18 9:00 CST** | 外部双审 (verifier 系统) | Mavis |
| 2026-09-18 中午 | 补实验候选 (verifier 报告) | Mavis + worker |
| **2026-09-18 晚 CST** | **D7 王老师 WeChat 推送** | **user 执行** |

---

## §8 老实话 (Trae code 必须知道)

1. **8 worker 已落数据完整**: 5 个 done + 1 failed + 2 done 补测, 产物路径全在 memory
2. **P-L v3 三态分离**: Phase 1 R²=0.7447 FAIL, Phase 2 β CI overlap 3/3 PASS, 综合部分拒绝
3. **诚实降级披露**: 沿 KIMI 7 方向"不允许为新数据调阈值" + Trae §6 退化预检 + Coze 3 态分离 + GLM §5 复现前提
4. **P-D V0.3 SPEC** 3 版本共存 (V0 + V0.2 KIMI 裁定 + V0.3 文档升级), 22 caption dual_24bit 22/22 PASS
5. **GLM 制品 FPR 4.4%** > 1% 阈值 GRAY, 老实入 paper §7.2 (排第 1 行, 不 reassign)
6. **Mavis 不动 push**: KIMI 凝子-agent 独立执行 git push, Mavis 严守 7 铁律
7. **D7 文稿 ≤ 200 字** (V1.0 ≤ 150, V1.1 ≤ 200 含 4 挂点 + 5 worker 进展)

---

## §9 严守清单 (Mavis / Trae code / doc-writer 边界)

| 角色 | 严守 |
|---|---|
| **Mavis** | 派工 + 调 agent + 写派遣论文初稿需求 + 协调 + 不动 push / 不调 WeChat / 不跑实验 |
| **Trae code** | 5 件 audit (read-only) + 沿 §1-§5 提案 + 0 LLM 重算 + 7 铁律 0 触动 |
| **doc-writer** | D7 文稿 V1.1 起草 (≤200 字, E/N/F/Q) + 4 挂点 + 5 worker 进展 + 诚实降级 |
| **d7-pusher** | KIMI push 第 3 批 audit (file count < 1000 / 锚定 PASS / invariant 0 触动) |
| **KIMI 凝子-agent** | 实际 git push (Mavis 不参与) |

---

**Mavis 起草** · deposon V3X 1 周判死主理 · 2026-09-17 18:18 CST
