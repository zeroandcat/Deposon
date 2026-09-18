# Trae code 改进需求 V2 · deposon V3X D7 推送前协同（2026-09-18 12:07 CST）
## 沿 `scientific-research-workflows:peer-review` + `superpowers:verification-before-completion` 复核 5 件 audit · 起草改进清单

> **起草方**: Mavis (deposon V3X 1 周判死主理, team lead 主导)
> **起草时点**: 2026-09-18 12:07 CST
> **起草依据**: 7 输入资产已 SHA-12 + size 实算 (5/5 MATCH + 7/7 size 精确)
> **起草目的**: V1 委托信 §1.1-§1.5 5 件 audit 已收口, 起草 V2 改进需求清单以备 D7 推送前最终对账
> **沿用 skill (Mavis plugin-cache 实际加载)**:
> - `scientific-research-workflows:peer-review` → `C:\Users\Administrator\.minimax\v2\plugin-cache\official\sha256-tree-v1-611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb\skills\peer-review\SKILL.md` (skill 路径 ✅ 实存, SKILL.md ✅ 已读)
> - `superpowers:verification-before-completion` → 真实路径 `sha256-tree-v1-ade95665080e6912a4564249bd38b02cbea0666552b6c5169831cfe4286f5e1d` (用户 V1 信中 sha256=`273bbe859ab6...` 经本轮 `Get-ChildItem` 列举证实 **不存在该 sha256 目录**, 已老实落账 §4.2)
> **严守**: 7 铁律 0 触动 (18 frozen + 5 P-G + 5 制品 + schema v1 + 4 plugin spec + verifier/mavis/.builtin/scripts/) + 9 铁律 key runtime 读不入 prompt/JSON/log

---

## §0 上下文对齐 (V1 → V2)

| 项 | V1 (2026-09-17 18:18 CST) | V2 (本轮 2026-09-18 12:07 CST) |
|---|---|---|
| 5 件 audit 状态 | 派工 18:30-19:30 / 收口 19:00-20:00 | **5/5 已收口** (PASS/FAIL/GRAY 各见 §1) |
| D7 推送时点 | 2026-09-18 晚 CST (user 执行) | 同 V1 |
| 改进机制 | V1 委托信 §1-§6 首次起草 | **本轮 = V2 = 5 件 audit 后再核**, 处置叙述层 + 改进措施层 |
| 接收方 | Trae code (read-only 副审) | Trae code (read-only V2 复核 + 改进清单执行) |

**V2 起点**: V1 委托信派 5 件 audit 已落盘 (`_trae_5audit_aggregated_2026_09_17.md`), V2 起草目的是把 5 件 audit 的发现收敛为**改进需求清单 + 验收标准**, 让 Trae code 在 D7 推送前 (晚 CST) 完成最终对账。

---

## §1 V2 改进需求总览 (沿 §1.1-§1.5)

### §1.1 D7 文稿 V1.1 数字修正（沿 Trae code §1 audit）

**audit 判定**: **PASS 带 3 处数字修正**

**必改清单**:

| # | 原文 | 修正 | 盘上实值依据 |
|---|---|---|---|
| 1 | `87.0%` 复现 (委托信 L61 / 8ch outline §3) | `85.0%` (51/60) | `deposon_v2_phase1_60cells_2026_09_11.json` L2621/2627 + .log L83 |
| 2 | `Adendum 13 + 2 + 1 = 16` (文稿 §0 拍板(2)/L32) | `11 + 2 + 1 + 2 + 1 = 17` (含 M/N PASS_for_death + F/G PARTIAL) | `_trae_paper_8ch_双审_20260917_200000.md` §一 数据点 3 |
| 3 | `P2 跨 backbone 强稳健` | `P2 PASS (β CI 3/3 重叠, 3 开源 + 3 闭源 backbone; doubao 10/30 INCOMPLETE + GPT-4o UNAVAILABLE; β 为 cell-level 代理斜率)` | `_p_l_v3_phase1_report_20260917_132341.md` §9.4 自披露 |

**验收 (verification-before-completion Gate)**:
1. IDENTIFY: `Select-String -Pattern '87\.0%|Adendum 13|强稳健' D:\私人资料\deposon-repo\docs\V3X\LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md`
2. RUN: 实跑命令
3. READ: 0 命中即为修正完成
4. VERIFY: 必改 3 处全 0 命中才声明 PASS

**OUT OF SCOPE**: 同源表述 `results/_d7_wang_teacher_wechat_publish_v1_20260918.md` L32/L152 需同步 (由 user/Mavis 处置, 不归 Trae code)。

### §1.2 KIMI push 第 3 批 Adendum C 勘误（沿 Trae code §2 audit）

**audit 判定**: **PASS 带 1 阻断项**

**核心矛盾** (P-M 病复发):
- 文件: `_adendum_C_pm_attack_surface_v2_20260917_133852.json` + `133726` 孪生件
- 矛盾: 8 budget 全 `detected_count:0, detection_rate:0.0`, 却 `caught_rate_mean:1.0, verdict:"PASS"`, verdict_reason 自称 "真检测率≥0.5" — 计数反转病以新形态复发

**已采取处置 (Trae code V1)**:
- 追加 `erratum_2026_09_17` 只读注记字段, **不改原值** (沿 §6 退化预检 + 7 铁律 0 触动)
- 改进前 SHA-12: `d64e8e2e2518` / `9c5ca0fed3ef`
- 改进后 SHA-12: `6eba63788ca8` / `193ba7d66412`

**V2 改进需求**:
- 选项 A (沿 Trae code V1): 接受 annotation ≠ mutation 处置, push 时 README 声明
- 选项 B (沿 KIMI 7 方向): 重新跑 Adendum C v3, 修正 verdict 语义 (detection_rate 字段 vs caught_rate 字段二选一)
- 选项 C (trae 推荐): **保留 V1 annotation + push README 双口径**, 不动 5 制品/18 frozen/4 plugin spec
- Mavis 拍板: 待 user 12:30 决策

**验收**:
1. push 前 5 audit 综合 MD (`_trae_5audit_aggregated_2026_09_17.md`) §2.2 双件 SHA-12 必须匹配 `6eba63788ca8` / `193ba7d66412`
2. push README 必须预写 P-M 矛盾说明 + annotation 处置声明
3. **不能动原 verdict 字段值** (7 铁律 0 触动)

### §1.3 派遣论文初稿 8 章 outline 必改（沿 Trae code §3 audit）

**audit 判定**: **PASS 带 3 必改**

**必改清单**:

| # | 章 | 必改 | 改法 |
|---|---|---|---|
| 1 | §3 P-C + P-D | `87.0%` → `85.0%` (51/60 实值); 补 P-C_two_phase=FAIL_H0 负控制注记 | 沿 §1.1 修正 1 同源 |
| 2 | §4 P-L v3 三态分离 | 补 Phase 1 四档表 (L30=0.8000 / L45=0.5111 / L60=0.7111 reference / L100=0.4600) + R²=0.7447 出处 (三点拟合 n=3 p=0.337) + Q=0.1929; 降格"强稳健" → "P2 PASS (3/3 β CI 重叠; β 为代理斜率)" | 沿 §1.1 修正 2/3 同源 |
| 3 | §5 17 Adendum | `13 + 2 + 1 = 16` → `11 + 2 + 1 + 2 + 1 = 17` | 沿 §1.1 修正 2 同源 |
| 4 | §6/§7 P-K 双口径 | OVERALL FAIL (4 判死线 3/4) + paper §7.2 处置 GRAY (T=2.0 严格不调, KIMI 7 方向不允许为新数据调阈值) | 沿 KIMI 7 方向 + Coze 3 态分离 |
| 5 | §6 限制 | 补 doubao hang / GPT-4o DNS+403 / Adendum F 8×APITimeoutError / 向量嵌入 stub 如实入限制章 | 沿 GLM §5 复现前提 |

**OUT OF SCOPE**: 8 章 outline 由 Mavis 起草, **不归 Trae code**; Trae code 仅副审, 不写 outline。

### §1.4 5 制品 by_model schema 互异（沿 Trae code §4 audit）

**audit 判定**: **SHA 5/5 PASS + schema 一致性 FAIL (结构性)**

**已知 schema 差异 (Trae code V1 已识别)**:
- 顶层 key 集合: 11 / 15 / 5 / 10 / 3 键互不相同
- 时序字段命名: `date` / `ts_utc+computed_ts_utc` / `created_ts_utc` 4 种
- 内容哈希命名: `byte_hash` / `byte_sha12` / `content_sha12` / `three_hashes.content` 4 种
- KIMI = caption 类 (22 caption); GLM_2/coze/minimax = 制品清单类; GLM_1 = 判别结果类 (设计差异)

**V2 改进需求**:
- 选项 A: camera-ready 前出 by_model schema v2 统一三口径 (顶层 key/时序字段/哈希命名), 一次性迁移
- 选项 B: **结构性 feature 不修**, push README 强引用 SHA-12 为准, camera-ready 时再 v2
- Mavis V2 推荐: 沿用 B (不改 5 制品, 沿 7 铁律); README 声明差异

**OUT OF SCOPE**: 5 制品 frozen, 0 触动 (沿 §7 铁律)。

### §1.5 18 frozen + schema v1 巡逻（沿 Trae code §5 audit）

**audit 判定**: **22/22 锚 PASS**

**核心发现**:
- 16 anchor + 5 P-G + schema v1 自身 = 22/22 实算匹配
- P-G 5 锚 = `sha256("P_G_V0_PLACEHOLDER_{id}_2026_09_15")[:12]` 种子占位, 0/5 文件真值 (设计声明, 非事故)
- KT_ABC1 内 3 锚漂移 (llm_client.py/exp_harness.py/conservation.py 三件在 09-09 p0p1 修复中被改) + 5+9 boss 锚指向 `.mavis/scripts/` 已灭失目录
- verifier/runs/2026-09-04_pd_v0.jsonl: 仓库内缺失, 归档区 `D:\私人资料\_archive_deposon_2026_09_17\` 实存 SHA-12=`5042869bdf85`, path_fallback 设计闭合
- anchor[0]=7d6d3d39fad8 出自 by_model/KIMI 的 fingerprint_anchors, **≠** pd_v0.jsonl 文件哈希, 推导链待 P-D V0.3 SPEC 闭合 (GRAY)

**V2 改进需求**:
1. P-G 5 锚升 V1 时 (D7 后 1 周计划) 逐个替换为文件真值, 废除种子占位 (不归本轮)
2. KT_ABC1 的 3 漂移锚 + 5+9 灭失 boss 锚: PATCH V3 声明"锚冻结时点 vs 后续修复"对应关系, 防 GitHub 读者误判
3. pd_v0.jsonl 推导链: P-D V0.3 SPEC 补一节"anchor[0] 的计算输入定义", 闭合 7d6d3d39fad8 溯源

**验收**:
- 22/22 锚 PASS 维持 (无破坏性改动)
- PATCH V3 报告 09-19 落盘 (post-D7)

---

## §2 5 件 audit 综合 (1 句话挂点回扣)

> **资产层 (18 frozen 22/22 + 5 制品 SHA 5/5 + schema v1 21/21) 一致完好**; **叙述层 3 数字漂移必改 (87.0%→85.0% / Adendum 16→17 / P2 强稳健降格) + 1 矛盾复发 (Adendum C v2 detection_rate=0.0×8 + verdict=PASS, 已 annotation 处置)**; **诚实降级入 paper §7.2 (P-K FPR 4.4% GRAY + OR 1/6 P2 GRAY + Phase 1 R²=0.7447 FAIL)**, **0 触动严守 7+9 铁律**。

**KT-A1 / KT-B1 / KT-C1 / KT-D0 4 挂点结论**:
- KT-A1 (守恒审计三层证据): ✅ 22/22 锚 PASS, 数字漂移不触锚
- KT-B1 (75 攻击 5×3×5): ✅ P-M 矛盾复发件属 Adendum C 新产物, 不污染 B1 主链
- KT-C1 (命名回正 attack_pc_*): ✅ P-O 26/26 闭合验证通过
- KT-D0 (D7 终判流程): ✅ 本轮 V2 改进需求 3 处数字修正必须在推送前完成

---

## §3 V2 改进需求执行时点 (D7 推送前 必完成)

| 时点 | 动作 | 主体 |
|---|---|---|
| **12:07 CST** (now) | V2 改进需求 MD 落盘 | Mavis (本轮) |
| 12:30 CST | Mavis 拍板 Adendum C v2 处置 (A/B/C 选项) | Mavis |
| 13:00 CST | Trae code 收 V2 改进需求 → 沿 §1.1-§1.5 复核 | Trae code |
| 14:00 CST | 沿 V2 必改清单执行 (3 数字修正 + Adendum C 勘误验证 + 8 章 outline 必改落库 + schema 互异 README 起草 + PATCH V3 起草) | Trae code + Mavis |
| 18:00 CST | KIMI push 第 3 批 manifest 落盘 (30 文件估) | Mavis |
| 19:00 CST | d7-pusher audit push 前副审 | d7-pusher |
| 21:00 CST | user 委托 KIMI 凝子-agent 执行 git push | user |
| **2026-09-18 晚 CST** | **D7 王老师 WeChat 推送** | **user 执行** |

---

## §4 verification-before-completion 复核结果 (实算)

### §4.1 7 输入资产 SHA-12 + size 实算 (5/5 强制项 MATCH + 2/2 落账项已算)

| # | 文件 | 声称 SHA-12 | 实算 SHA-12 | 声称 size | 实算 size | 结论 |
|---|---|---|---|---|---|---|
| 1 | `_letter_to_trae_code_2026_09_17_final.md` | (落账) | `c1791a7811f3` | 10,690 B | 10,690 B ✅ | size MATCH |
| 2 | `_trae_5audit_aggregated_2026_09_17.md` | (落账) | `43265e4bf2be` | 11,465 B | 11,465 B ✅ | size MATCH |
| 3 | `_trae_d7_v1_audit_20260917_190000.md` | `e240ca712be6` | `e240ca712be6` ✅ | 7,855 B | 7,855 B ✅ | **MATCH** |
| 4 | `_trae_kimi_push_v3_audit_20260917_193000.md` | `8ece24be6b8a` | `8ece24be6b8a` ✅ | 3,281 B | 3,281 B ✅ | **MATCH** |
| 5 | `_trae_paper_8ch_双审_20260917_200000.md` | `bec666969ffc` | `bec666969ffc` ✅ | 4,040 B | 4,040 B ✅ | **MATCH** |
| 6 | `_trae_corpus_5_audit_20260917_193000.md` | `f2a655cd5e54` | `f2a655cd5e54` ✅ | 3,467 B | 3,467 B ✅ | **MATCH** |
| 7 | `_trae_anchor_18_audit_20260917_193000.md` | `4af67e6cbe71` | `4af67e6cbe71` ✅ | 3,449 B | 3,449 B ✅ | **MATCH** |

**Gate 判定**: 5/5 强制 SHA-12 项全 MATCH + 7/7 size 精确 = V2 改进需求可基于 5 件 audit 起草。

### §4.2 skill 路径核对 (老实交代 V1 信中 verify skill 路径错)

| skill | V1 委托信 sha256 | 实存 sha256 | 结论 |
|---|---|---|---|
| `peer-review` | `611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb` | `611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb` | ✅ MATCH |
| `verification-before-completion` | `273bbe859ab6eaca79beb84fba82a8a8e1e6964647995e0eae8dbbbe8dbe2dbb` (V1 信引用) | **`ade95665080e6912a4564249bd38b02cbea0666552b6c5169831cfe4286f5e1d`** (本轮 `Get-ChildItem` 实查) | ⚠️ V1 sha256 错, **V2 用实存 sha256** |

**0 编造**: 不沿 V1 错路径, 不引 `C:\Users\Administrator\.trae-cn\...` IDE 缓存, 不引 Muratkankoylan 等用户拉取的 GitHub skill 仓库。

### §4.3 Trae code 5 件 audit 已交付 vs 委托信 §6 路径

| 委托信 §6 路径 | 实落盘 | SHA-12 实算 |
|---|---|---|
| `D:/私人资料/deposon-repo/results/_trae_d7_v1_audit_20260917_190000.json` | ⚠️ **未落盘** (仅 MD 落) | (n/a) |
| `D:/私人资料/deposon-repo/results/_trae_d7_v1_audit_20260917_190000.md` | ✅ 落 | `e240ca712be6` |
| `D:/私人资料/deposon-repo/results/_trae_corpus_5_audit_20260917_193000.md` | ✅ 落 | `f2a655cd5e54` |
| `D:/私人资料/deposon-repo/results/_trae_anchor_18_audit_20260917_193000.md` | ✅ 落 | `4af67e6cbe71` |
| `D:/私人资料/deposon-repo/results/_trae_kimi_push_v3_audit_20260917_193000.md` | ✅ 落 | `8ece24be6b8a` |
| `D:/私人资料/deposon-repo/results/_trae_paper_8ch_双审_20260917_200000.md` | ✅ 落 | `bec666969ffc` |

**缺口**: 委托信 §6 列了 `_trae_d7_v1_audit_20260917_190000.json` (1 JSON) 但盘上未落 (仅 MD) — 沿 V2 改进需求补落或显式声明不落 JSON (沿 5 audit 综合 MD 已含同等信息)。

---

## §5 本轮 worker 进展 + P-K FAIL 落账

### §5.1 本轮 8 worker 进展 (老实交代 3 bg_ IDs 找不到)

**用户 V2 委托提示中提及**:
> 沿本轮 8 制品 (bg_02d37078 + bg_160a8c86 + bg_2bf99d32) 验证 5 worker 进展 + P-K FAIL 落账

**实查结果 (老实交代)**:
- `bg_02d37078` / `bg_160a8c86` / `bg_2bf99d32` 在仓库 `D:\私人资料\deposon-repo` 内 **0 命中** (`Get-ChildItem -Recurse -Directory -Filter 'bg_*'` 仅返回历史 bg_ IDs: `bg_23aa1031` / `bg_f2fd0574` / `bg_3e071c03` / `bg_224d01a6` / `bg_f688bdba` / `bg_a93672e9` / `bg_a87339c8` / `bg_62ffa890` / `bg_6c848f0c` 9 个, **不含**用户 V2 提的 3 个)
- 推测: 3 bg_ IDs 系 V2 委托起草时另引素材, 未同步到 Mavis 接收路径; 或系示例性 ID 而非实际产物 ID

**0 编造处置**: 不沿 3 bg_ IDs 编造 worker 进展; 改沿 9 bg_ IDs (aggregated §3 实算) 作为本轮 worker 进展落账源。

### §5.2 9 worker 进展落账 (沿 `_trae_5audit_aggregated_2026_09_17.md` §3)

| # | Worker | task_id | 范围 | 状态 | 关键判死 |
|---|---|---|---|---|---|
| 1 | Phase 1 P-L v3 | `bg_23aa1031` | Mistral × L{30, 45, 60, 100} | ✅ FAIL | R²=0.7447, Q=0.1929 |
| 2 | Phase 3 Adendum 10 | `bg_f2fd0574` | 10 零成本 | ✅ 7 PASS/READY | 3 件 LLM 后派 |
| 3 | 7 中成本 Adendum | `bg_3e071c03` | B/C/D/E/M/N/O | ✅ 6 PASS + 1 GRAY | O P-K FPR 4.4% |
| 4 | F/G/K LLM | `bg_224d01a6` | 3 端 LLM dispatch | ✅ 1 PARTIAL + 1 PARTIAL + 1 FAIL_NO_MODEL | text-240715 UnsupportedModel |
| 5 | Phase 2 baseline | `bg_f688bdba` | qwen3 + glm53 + mistral × L{30, 60} | ✅ PASS | 3 backbone β CI overlap 3/3 |
| 6 | P-D V0.3 实测 | `bg_a93672e9` | 22 caption dual_24bit | ✅ 22/22 PASS | b3 root=`75596bbabdb8` |
| 7 | OR 重试 | `bg_a87339c8` | 4 OR embedding | ✅ 4/4 30/30 | P2 GRAY (1/6 OR×OR) |
| 8 | 豆包补测 v2 | `bg_62ffa890` | 4 vision + 1 text + 1 cross-arch | ✅ 5/6 EMBEDDED + 1 FAILED | structural finding |
| 9 | 加速器 v2 retry | `bg_6c848f0c` | 3 闭源 backbone | ✅ 3/3 30/30 | β CI overlap 3/3, P2 PASS |

**P-L v3 综合判死 (诚实降级披露, paper §7.2 已准备)**:
- Phase 1 (Mistral): FAIL (R²=0.7447, Q=0.1929) — size scaling 失败
- Phase 2 (3 开源 backbone): PASS (β CI overlap 3/3) — 跨实现稳健
- Phase 2 (3 闭源 backbone): PASS (β CI overlap 3/3) — 跨实现稳健
- Phase 2 (4 OR embedding): GRAY (1/6 OR×OR) — symbol-split by architecture
- Phase 2 (5 豆包 embedding): structural finding (endpoint-internal 收敛, 跨 endpoint 离散)
- **综合**: P-L data collapse 假设 **部分拒绝** (size scaling 失败, 跨 backbone 跨实现稳健) → paper §7.2 老实入

### §5.3 P-K FAIL 落账 (沿 8ch outline §一 数据点 4)

| 维度 | 实值 | 处置 |
|---|---|---|
| FPR | **0.0444 (4.44%)** | > 1% 阈值 → GRAY |
| 误判具体 | 2/45 GLM JSON 误判自家 (GLM-N10/N11) | 入 §7.2 排第 1 行 |
| 4 判死线 | 3/4 PASS | OVERALL **FAIL** |
| paper §7.2 处置 | **GRAY** (T=2.0 严格不调, 沿 KIMI 7 方向不允许为新数据调阈值) | 沿 KIMI 7 方向 + 诚实降级 |
| 双口径并存 | OVERALL FAIL + 处置 GRAY | outline 必须**两口径都写**, 不可只引其一 |

**OUT OF SCOPE**: P-K 处置由 Mavis 沿 KIMI 7 方向派工, **不归 Trae code**; Trae code 仅 audit 不重算。

---

## §6 7 铁律 + 9 铁律 严守声明 (本轮 0 触动确认)

| 类别 | 状态 | 证据 |
|---|---|---|
| no_llm | ✅ 0 LLM | 5 audit 全 read-only, 本 V2 MD 仅复核 + 起草, 0 LLM 调用 |
| no_proxy | ✅ 0 proxy | 5 audit 沿 Trae code chat |
| no_gateway | ✅ 0 gateway | — |
| no_key_in_prompt_json_disk | ✅ key runtime 读 | V2 MD 0 key 字段, 0 key 入 prompt/JSON/log/MD |
| no_18_frozen_touch | ✅ 0 触动 | 22/22 锚 PASS 维持 |
| no_p_g_v0_touch | ✅ 0 触动 | P-G 5 锚种子占位不变 |
| no_p_g_v01_touch | ✅ 0 触动 | P-G v0.1 未发起 |
| no_plugin_spec_touch | ✅ 0 触动 | skill_a/b/c/d 4 plugin spec 0 触动 |
| no_verifier_mavis_builtin_scripts_touch | ✅ 0 触动 | verifier/audit/ 已挪归档区, fallback 闭合 |

**0 触动确认 (本轮实算)**:
- 18 frozen 22/22 锚 PASS 维持 (沿 §1.5 + Trae code §5 audit)
- 5 制品 SHA 5/5 验过 (沿 §1.4 + Trae code §4 audit, schema 互异为结构性 feature 不改)
- schema v1 21/21 一致 (沿 §1.5 + Trae code §5 audit)
- 4 plugin spec 0 触动 (沿 §1.5)

---

## §7 V2 改进需求交付路径与时点

### §7.1 落盘

| 路径 | 落盘 | SHA-12 | 时点 |
|---|---|---|---|
| `D:/私人资料/deposon-repo/results/_trae_code_improvement_v2_2026_09_18.md` | 本 V2 MD | (本轮算) | 12:07 CST |

### §7.2 V2 MD 内嵌 0 编造 / 0 假设声明

1. 不补 `_trae_d7_v1_audit_20260917_190000.json` (沿 §4.3 缺口显式声明, 待 Mavis 拍板)
2. 沿用户 V2 委托提的 3 bg_ IDs (02d37078 / 160a8c86 / 2bf99d32) 找不到 — 老实交代, 改沿 aggregated §3 9 task IDs 落账
3. V1 信中 verify skill sha256 路径错 — 老实交代, 改沿本轮实查 sha256 (`ade95665...`) 引用

---

## §8 老实话 (V2 必须知道)

1. **5 件 audit 全 PASS 或 PASS 带有限修正** — 资产层一致完好, 仅叙述层 3 数字漂移必改 + 1 矛盾复发已 annotation
2. **3 数字修正必须在 D7 推送前完成** — 87.0%→85.0% / Adendum 16→17 / P2 强稳健降格
3. **Adendum C v2 处置** 待 Mavis 12:30 拍板 (A/B/C 三选项)
4. **5 制品 schema 互异 = 结构性 feature, 不改** — push README 必写声明
5. **P-K FAIL 老实入 paper §7.2** (FPR 4.4% GRAY + OVERALL FAIL 双口径)
6. **OR 4 embedding P2 GRAY (1/6)** 老实入 paper §7.2
7. **Phase 1 R²=0.7447 FAIL** 老实入 paper §7.2
8. **P-L data collapse 部分拒绝** (size scaling 失败, 跨 backbone 跨实现稳健)
9. **2 脚本 (_fix_adendum_c + _goal_completion_audit)** 是 Trae code 写的, Mavis 不写脚本 (沿 7 铁律边界)
10. **Mavis 不调 WeChat 钥匙** (王老师推送由 user 执行, 明晚 18:00-21:00 CST)
11. **Mavis 不动 push** (KIMI 凝子-agent 独立执行 git push, Mavis 准备 manifest)
12. **Mavis 不动 paper 写作** (Coze 凝子-agent 起正式版, Mavis 写需求 + 边界)
13. **用户 V2 委托提的 3 bg_ IDs 找不到** — 老实交代, 落账源 = aggregated §3 9 task IDs
14. **V1 信中 verify skill sha256 路径错** — 老实交代, 改沿实查 sha256
15. **委托信 §6 列的 JSON 缺口** (_trae_d7_v1_audit_20260917_190000.json) — 实盘未落, 待 Mavis 拍板

---

## §9 派工新规强化 (沿 user 10:22 + 本轮 12:07)

| 提示词必带 | 落账 |
|---|---|
| skill 名字 | `scientific-research-workflows:peer-review` + `superpowers:verification-before-completion` ✅ |
| plugin 名字 | `@scientific-research-workflows` + `@superpowers` ✅ |
| 严守 | 7 铁律 + 9 铁律 ✅ |
| 老实 | 0 产物老实交代 ✅ (§4.2 / §5.1) |
| 路径 | Mavis plugin-cache 实际路径 (sha256-tree-v1-...) ✅ |

**禁用路径**:
- ❌ Trae IDE 缓存 `C:\Users\Administrator\.trae-cn\...`
- ❌ Muratkankoylan 等用户拉取的 GitHub skill 仓库
- ❌ 7 铁律/9 铁律 任何触动

---

## §10 挂点回扣 - V2 一句话 (沿 D7 report §3 模式)

> **V2 = V1 5 件 audit 后再核**: 资产层一致完好 (18 frozen 22/22 + 5 制品 SHA 5/5 + schema v1 21/21) → 叙述层 3 数字漂移必改 + 1 矛盾复发 (Adendum C v2 已 annotation) → 诚实降级入 paper §7.2 (P-K FPR 4.4% GRAY + OVERALL FAIL + OR 1/6 P2 GRAY + Phase 1 R²=0.7447 FAIL) → 0 触动严守 7+9 铁律; **KT-A1/B1/C1 3 挂点结论稳定, KT-D0 挂点 = 本轮 V2 改进需求 3 处数字修正必须在推送前完成**。

---

**Mavis 起草 V2 改进需求** · deposon V3X 1 周判死主理 · 2026-09-18 12:07 CST
**沿 skill**: `scientific-research-workflows:peer-review` (实存 sha256 611965fcb...) + `superpowers:verification-before-completion` (实存 sha256 ade9566508..., V1 信 273bbe859... 错已老实落账)
**严守**: 7 铁律 0 触动 + 9 铁律 key runtime 读不入 prompt/JSON/log + 0 LLM 改稿 + 0 编造 (3 bg_ IDs 找不到 / verify skill sha256 错 / JSON 缺口 老实交代)