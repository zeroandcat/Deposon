# D0 冻结 SPEC 准备清单(明日开工)

> **作者**: Mavis(执行线)
> **日期**: 2026-09-09
> **状态**: V0.1(综合 3 信息源)
> **位置**: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md`
> **触发**: 用户指令"综合之前的计划 + 明日开工清单 + 给王老师的提案来推进一周计划"

---

## 0. 3 信息源综合(决策依据)

| 信息源 | 路径 | 关键贡献 |
|---|---|---|
| **王老师 v3 提案**(2026-09-04,对外承诺) | `_Coze_Drive_扣子_deposon-project_proposals_V3X_Collab_Prop.pdf`(272KB, 4 页) | 4 条 KT 判死线 + D0-D7 排程 + 三问默认值 + Phase 0/1/2 路线图 |
| **Mavis 内部 6 方向 quick-kill** | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2(15KB, 21 BOSS) | 防 BOSS 突袭 + 6 方向 BOSS baseline 测法 |
| **Mavis 内部 V0 spec 5 份** | `docs/V3X/P_{A,B,C,D,E}_..._V0_SPEC.md` | 工程实施细节(成本倍数 / 5 锚 / 攻击脚本) |

**Mapping**(v3 提案 KT vs Mavis 内部 spec):

| v3 提案 KT | 对外判死线(王老师视角) | 对应 Mavis 内部 spec | 内部主指标 | 差异 |
|---|---|---|---|---|
| **KT-A1** | g_a* 随 λ_gap 单调(Mann-Whitney 单侧) | P-A 平衡稳定化 V0 spec(10.3KB) | 成本倍数 ≤ 1.3× / ≥ 2.0× | 王老师版"耗散-谱"vs Mavis 版"成本-ε-纳什" — **不同指标,需双跑** |
| **KT-B1** | 合成操纵者 n=200 攻击 ≥50% | P-B 失真上界 V0 spec(7.1KB) | 失真上界 ≥ 0.95 | 王老师版"对抗性攻击"vs Mavis 版"失真度" — **不同视角,互补** |
| **KT-C1** | 残余 r vs 维数 d log-log, R²<0.3 死 | P-C 两相结构 V0 spec(6.3KB) | η 扫描相变点 ± 20% | 王老师版"图族回归"vs Mavis 版"参数扫描" — **数据集同源 v21,可双跑** |
| **KT-D0** | 证据卡(账指纹协议引用) | P-D 指纹 V0 spec(9.2KB, V0.1 PASS) | 5 锚 SHA-256 + 3 攻击 PASS | 王老师版"引用既有"vs Mavis 版"复跑" — **已闭合,零新实验** |

**关键发现**: v3 提案 4 条 KT 是"对外承诺简化版",Mavis 内部 4 份 V0 spec 是"工程实施细节版"。**两者不冲突,需双跑**:王老师版出"对外 1 页摘要",Mavis 版出"内部 10-15 页判死报告"。

---

## 1. D0 任务定义(对外承诺 + 内部准备)

### 1.1 D0 对外任务(王老师 v3 提案第六节)

> "D0 冻结三份 SPEC(群内公布 SHA-256 前 12 位锚,先公布后运行)+ 发送三问"

- **冻结 3 份 SPEC** = KT-A1 / KT-B1 / KT-C1 的 SPEC(零 LLM API 调用,零新数据采集)
- **公布锚点** = SHA-256 前 12 位,先公布后运行
- **三问**(全部带默认值,不答即按默认):
  1. 稳定化成本中烧掉的耗散,计入机制侧预算还是参与者效用?**默认:机制侧预算**
  2. 攻击实验的"结论错误",按终态标签翻转还是评分阈值判?**默认:标签翻转**
  3. 标度实验更关心审计强度参数还是环结构参数?**默认:环结构 d**
- **D0 微信中期简报**:三行判死状态(每条线生/死/在跑)

### 1.2 D0 内部准备(Mavis 视角)

- **3 份 SPEC 草稿** = KT-A1 / KT-B1 / KT-C1 完整 SPEC(含 5 锚预登记 + 攻击脚本 + 95% bootstrap CI 协议)
- **3 份 SPEC 锚点** = SHA-256 前 12 位计算
- **BOSS baseline 占位** = KT-A1 BOSS-A1/A2/A3(KT-A1 对应 P-A 平衡稳定化);KT-B1 BOSS-B1/B2/B3;KT-C1 BOSS-C1/C2/C3
- **1 份证据卡** = KT-D0 引用 P-D V0.1 PASS 既有结果,根指纹 7d6d3d39fad8(注意:v3 提案附录说"e66e44e63f5a"是 EIS 复现根指纹,与 P-D V0.1 PD2 根指纹 f88d855aaf83 略有差异,**需在 D0 准备时核对 Mavis 线 PD2 实际根指纹**)
- **D7 交付草稿** = 一页摘要 + 锚定工件包(完整中文判死报告备查)

---

## 2. 明日(D0)开工清单

### 2.1 上午段(D0 AM, 派子代理 + 准备 3 份 SPEC 草稿)

| # | 任务 | 派给 | 输出 | 阻塞? |
|---|---|---|---|---|
| 1 | 写 KT-A1 SPEC V0 草稿 | Mavis | `docs/V3X/KT_A1_SPEC_V0.md`(10-15 页) | 否 |
| 2 | 写 KT-B1 SPEC V0 草稿 | Mavis | `docs/V3X/KT_B1_SPEC_V0.md`(10-15 页) | 否 |
| 3 | 写 KT-C1 SPEC V0 草稿 | Mavis | `docs/V3X/KT_C1_SPEC_V0.md`(5-8 页) | 否 |
| 4 | 派 successor 子代理算 3 组锚 SHA-256 前 12 位 | successor | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 依赖 1/2/3 |
| 5 | 写 KT-D0 证据卡(引用 P-D V0.1) | Mavis | `docs/V3X/KT_D0_EVIDENCE_CARD.md`(1-2 页) | 否 |
| 6 | 写 D0 微信中期简报模板 | Mavis | `docs/V3X/D3_WECHAT_MIDTERM_TEMPLATE.md` | 否 |

### 2.2 下午段(D0 PM, 群内公布 + 发送三问)

| # | 任务 | 派给 | 输出 | 阻塞? |
|---|---|---|---|---|
| 7 | 群内公布 4 份 SPEC + 4 组锚(KT-A1/B1/C1/D0) | Mavis 草稿 + 人工发送 | WeChat 群消息 | 依赖 1-6 |
| 8 | 发送 D0 三问(全部带默认) | 人工发送 | WeChat 私信给王老师 | 依赖 7 |
| 9 | 触发 D1 KT-C1 准备(机械回归) | Mavis | D1 起 KT-C1 跑 | 依赖 4 |

### 2.3 D0 末产出物清单

- [ ] 3 份 SPEC V0(KT-A1 / KT-B1 / KT-C1)+ 1 份证据卡(KT-D0)
- [ ] 1 份 3 组锚 JSON(`verifier/handoff/KT_ABC1_anchors_sha256_12.json`)
- [ ] 1 份 D3 微信中期简报模板
- [ ] 1 份 D7 一页摘要模板(`docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md`)
- [ ] 4 份 BOSS baseline 占位脚本(`.mavis/scripts/kt_*/boss_*.py`,无实现只占位)

---

## 3. D1-D7 排程(从 v3 提案附录 C 直接复用 + 内部补全)

| Day | 对外任务(v3 提案) | 内部补全(Mavis 视角) | 派给 | 输出 |
|---|---|---|---|---|
| **D0** | 冻结三份 SPEC + 发送三问 | 3 份 SPEC V0 + 3 组锚 + 1 证据卡 + 4 BOSS 占位 | Mavis + successor | 4 SPEC + 锚 JSON + 证据卡 |
| **D1** | KT-C1 冻结并跑完机械回归 | KT-C1 实施:log-log 回归 + R² + 95% CI + BOSS-C1/C2/C3 baseline | data | KT-C1 报告 1-2 页 |
| **D2** | KT-A1 冻结 | KT-A1 实施:十分位 + Mann-Whitney + BOSS-A1/A2/A3 baseline | data | KT-A1 SPEC 冻结 |
| **D3** | KT-B1 冻结 + 中期简报 | KT-B1 实施:合成操纵者 n=200 攻击 + BOSS-B1/B2/B3 baseline + D3 微信三行判死状态 | data + Mavis | KT-B1 SPEC 冻结 + WeChat 中期简报 |
| **D4** | 独立重跑审计 + 缓冲 | reviewer-b 在 `/tmp/deposon_kt_audit_<timestamp>/` 副本上独立重跑 1 cell/SPEC + 攻击脚本 | reviewer-b | 4 份审计报告 |
| **D5** | 附赠臂收尾 | BPA 先导数据(探索性档,v3 机制激励相容手术) | Mavis | BPA 先导数据 1-2 页 |
| **D6** | 工件入账、成稿 | 4 份 KT 报告 + 1 份证据卡 → 完整中文判死报告(10-15 页)成稿 | paper-cn | 中文判死报告草稿 |
| **D7** | 交付一页摘要 + 锚定工件包 | 一页摘要 + 锚定工件包(微信友好版)+ 完整报告备查 | Mavis | D7 一页摘要 + 工件包 |

---

## 4. BOSS baseline 占位脚本(明日一并写,无实现只占位)

按 QUICK_KILL_6_DIRECTIONS.md V0.2 BOSS 列表:

- `.mavis/scripts/kt_a1/boss_a1_rbr_rm.py` — RBR/RM 在 22 受控概念图上跑
- `.mavis/scripts/kt_a1/boss_a2_potential_game.py` — 套 Monderer & Shapley 1996 框架
- `.mavis/scripts/kt_a1/boss_a3_replicator_dynamics.py` — 跑 Replicator Dynamics
- `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` — Sinkhorn OT 失真度
- `.mavis/scripts/kt_b1/boss_b2_kd.py` — Knowledge Distillation 基线
- `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` — LLMLingua 提示词压缩
- `.mavis/scripts/kt_c1/boss_c1_2d_ising.py` — 2D Ising 普适类预测
- `.mavis/scripts/kt_c1/boss_c2_transverse_ising.py` — Transverse field Ising
- `.mavis/scripts/kt_c1/boss_c3_reservoir.py` — Reservoir Computing 双稳态

**禁示条款**(沿用 P-D P1 + V1 六关键词规则教训):
- 不得在真实仓库跑 BOSS baseline(必须 `/tmp/deposon_kt_audit_<timestamp>/` 副本)
- 不得让 BOSS baseline 脚本诱导操作者删除冻结锚
- 不得在 BOSS 测法跑通前宣称 KT 方向 PASS
- 不得跳过 BOSS 测法只跑主实验(防 V1 撞 BOSS 重演)

---

## 5. 风险与缓解(沿用 v3 提案第七节 + 内部补全)

| 风险 | 缓解 |
|---|---|
| 王老师没空看微信 | 三问全部带默认值,不回复即按默认执行;每月至多一次简报 |
| 挂点跑不出来 | 判死即有效交付,留痕后调方向,不浪费前序冻结资产 |
| 方向分歧 | 微信一句话调整,判死线 SPEC 不受影响(先于答复冻结) |
| 进度延期 | D7 硬截止,最多宽限 1-2 天;延误会在中期简报中提前报 |
| Mavis 线 PD2 根指纹核对 | D0 准备时核对 P-D V0.1 vs v3 提案附录根指纹差异(7d6d3d39fad8 / e66e44e63f5a / f88d855aaf83) |
| BOSS 测法撞上 | 按 §0.5 降级主张,回写 QUICK_KILL V0.3 |
| 7 条铁律 | 双审 / API key 不入 prompt / 术语红线 / 数字溯源 / verifier 纪律 / 预登记 / 推送策略 |

---

## 6. 与 7 条铁律的兼容性

- ✅ 不改 P-D V0.1.1(已 PASS,只引用)
- ✅ 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
- ✅ key 安全:runtime `Path(file).read_text()` 读取,不入 prompt
- ✅ /tmp 副本做所有重跑
- ✅ 不签 18 月 / 多论文规划(Phase 0 1 周 + Phase 1 1-3 月 + Phase 2 3-12 月,逐步)
- ✅ 不上生产
- ✅ 不重做王老师已有工作(所有数据基于冻结 JSON)
- ✅ BOSS 测法 + §0.5 已知陷阱节(沿用 spec 必带"已知陷阱"铁律)

---

## 7. 下一步(等 user 拍板)

1. **开跑 D0 准备**:派 1 个 worker 子代理写 3 份 SPEC V0 草稿 + Mavis 写 1 份证据卡 → D0 末冻结并群内公布
2. **先校对 PD2 根指纹**:核对 P-D V0.1 vs v3 提案附录(7d6d3d39fad8 / e66e44e63f5a / f88d855aaf83),避免 D0 公布错误
3. **继续调研**:深读 Project Ariadne / Auditing Multi-Agent / LIMEN 补强 BOSS 测法
4. **改选其他 KT**:KT-B1 或 KT-C1 优先(根据 user 战略判断)

**推荐**:选项 1(明日开跑 D0,按"按之前的计划来"原则推进)。如选 2,先派 1 个 verifier 核对 P-D V0.1 PD2 实际根指纹。

---

**D0 准备清单结束,等 user 拍板"开跑 D0"或"先校对根指纹"。**
