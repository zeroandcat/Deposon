# 上传委托信 v3（KIMI 受托 · 归档二棒后 + on-disk SHA-12 锚口径）

> **出件方**：doc-writer（agent-0032834a3e04）
> **受托方**：KIMI（上传执行方；沿 PI 2026-09-26 `ask_9c8751ec`「KIMI与GLM知道即可」字面——KIMI 已知上传清单与 no-upload 清单口径；**涉 KIMI 表述一律以 PI 的 github 为唯一权威源（受托方已知）**）
> **日期**：2026-09-26
> **版本**：v3（沿 v2 `ADFA7DD03F76` 13,012 B 的路径/计数/上传清单更新面 + on-disk SHA-12 锚口径 + 归档二棒后终态）
> **派工依据**：
> - PI 2026-09-24 19:15 提醒「记得文件移动后清单与委托要更新」
> - PI 2026-09-26 19:05 拍板 `ask_96e0f651f306f2337cd57b47` 全推荐（ratify_formal=all）
> - PI 2026-09-26 18:42 拍板 `ask_822b1e27` TH-v2-3 跨日 2 天达标 supersede
> - PI 2026-09-26 `ask_9c8751ec`「KIMI与GLM知道即可」「你侧无额外补充」（涉 KIMI / GLM 表述一律以 PI github 为唯一权威源，受托方已知）
> - PI 2026-09-26 18:24 拍板「整理文件夹包括清噪声、删垃圾与中间文件、归档无需上传文件与非核心文件、更新清单与委托」—— 棒 7 + 棒 8 已完成，主目录 1,131 → **986**
> **v2 件状态**：v2 `letters/_v4_commission_upload_executor_2026_09_24_v2.md` 0 触动（沿 PI 2026-09-23「v1/v2 件一律不覆盖」纪律）
> **边界**：本件**不含上传工具 / 通道 / 凭据**——任何凭据 / key 严禁内填；上传执行方自备工具与凭据，runtime 读不入 prompt / JSON / log

---

## 1. 委托事项

委托 KIMI **按本件 §2 上传清单**将 deposon V3-V4 阶段性材料上传至公开渠道（arXiv / 项目主页 / 协作圈知识库等——**通道由 KIMI 按 §2 上传清单各项指定的目标渠道**执行）；**§3 no-upload 清单内件严禁以任何形式上传 / 转储 / 复制到公网 / 第三方服务**。

> **v3 与 v2 关键差异**：
> - v2 字面以补账件 v1 19:50 快照（MAIN 799）为底账；**v3 以补账件 v2 19:50 快照（MAIN 986）为底账**——上传清单与 no-upload 清单均按最终布局重排
> - 锚链统一 on-disk SHA-12（沿 E-35 §E.3 字面，所有 SHA-12 字段 = 盘实测 `Get-FileHash -Algorithm SHA256` 前 12 字符 + uppercase）
> - 任务 B v2.2 正式判定 `5D79E67A4E9D` 复合定性落定素材（FAIL · 2 复合 + 2 β）+ N-26 真审终裁 `F4435801D09F` 字面加入负面结果章素材清单

## 2. 上传清单（按 Tag-A「正式成果」+ Tag-B「cleanup 链」+ 本轮新出件为底账）

### 2.1 上传范围原则

- **底账四件套**：
  - 盘点件：`results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（355,687 B · SHA-12 `3E4E90FB48E1`，evidence-auditor 出具，R4 redact 后新 SHA）
  - 勘误件：`results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md`（10,288 B · SHA-12 `55CD332F66F2`，doc-writer 出具）
  - 补账件 v1：`results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md`（23,152 B · SHA-12 `C64146C4CCAC`，doc-writer 出具，清理六棒后最终布局登记面）
  - **补账件 v2（本轮新出）**：`results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md`（SHA-12 实测）· **归档二棒后 + 全链补账，2026-09-26 19:50**
- **路径取数**：以本轮归档二棒后**新路径**为准——v6 ledger `CC498BC28525` §3 旧→新路径对账表（v1 ledger `4025E871726B` 不动 + v2-v5 ledger 各自 §A/§B `64C4EF850025` / `8F5136E176B8` / `9BD8932FA214` / `272E8C752406`）作为补充核对源
- **锚链口径**：**所有 SHA-12 字段 = on-disk SHA-12**（盘实测 `Get-FileHash -Algorithm SHA256` 前 12 字符 + uppercase）；指纹字段口径（fingerprint_self_hash_after_birth 派生字段）待 PI 拍板（沿 E-34.5 §22.7.5 字面），**本上传信仅用 on-disk SHA 单一口径**
- **通报截止时点**：**2026-09-26 19:50 GMT+8**（本件出件时点 = 补账件 v2 出件时点）；凡此之后 PI 拍板之新口径以 PI 当日拍板为准

### 2.2 Tag-A 上传清单（MAIN 内正式成果候选 · 沿补账件 v2 §8.1 字面）

KIMI 按下列件**逐件上传**；上传前**实测 SHA-12 与本表一致方可执行**；任何不一致立即停手并报告。

| # | 新路径（归档二棒后） | SHA-12（on-disk） | 字节 | 目标渠道（建议） |
|---|---|---|---|---|
| 1 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `C28F7F0B530F` | 11,079 | 项目主页 / 协作圈知识库 |
| 2 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `DE772CD9E7BA` | 6,825 | 项目主页 |
| 3 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `8FF1A7C5413F` | 21,756 | 项目主页 |
| 4 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `240A7AE4BDFB` | 17,803 | 项目主页 |
| 5 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `0A63824F0805` | 7,352 | 项目主页 |
| 6 | `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | `BAEF94E393DE` | 11,478 | 项目主页 |
| 7 | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | `825337B10A2D` | 8,753 | 项目主页 |
| 8 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `977FE1B48F75` | 19,751 | 项目主页 |
| 9 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | `79C7321056B8` | 13,419 | 项目主页 |
| 10 | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | `EE043A13F801` | 3,899 | 项目主页 |
| 11 | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | `00C7B7CECCDC` | 4,885 | 项目主页 |
| 12 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | `7F1492FBE657` | 10,979 | 项目主页 |
| 13 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `900DA300D11E` | 13,109 | 项目主页 |
| 14 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `817EFDC2F0AD` | 15,985 | 项目主页 |
| 15 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `E47D0348922E` | 12,608 | 项目主页 |
| 16 | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | `4D970E9C0AEC` | 4,188 | 项目主页 |
| 17 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `9A6B08D03E0C` | 15,479 | 项目主页 |
| 18 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `7478959CFC7D` | 9,267 | 项目主页 |
| 19 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | `4020B1809780` | 8,849 | 项目主页 |
| 20 | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | `813B34DCAC70` | 6,493 | 项目主页 |
| 21 | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | `226F740AA120` | 4,840 | 项目主页 |
| 22 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `4FFB21BB6BFA` | 8,526 | 项目主页 |
| 23 | `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `4A08521F8DE1` | 38,545 | 项目主页（终稿候选） |
| 24 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `3D847F9F3151` | 22,427 | 项目主页 |
| 25 | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | `914053FC3E17` | 11,080 | 项目主页 |
| 26 | `results/_v4_pi_cot_v2_ruleset_v2.json` | `C5B3DD141655` | 6,179 | 协作圈知识库（v2 词表扩 201 词 + 35 批判反思词） |
| 27 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | `EB22F13D571C` | 52,465 | 协作圈知识库 |
| 28 | `results/_v4_pi_cot_v2_verdict_v2.md` | `5D79E67A4E9D` | 33,723 | 协作圈知识库（**论文 §4 负面结果章素材**） |
| 29 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | `5FBEC21E0AD2` | 42,914 | 协作圈知识库 |
| 30 | `results/_v4_supp_l6_s38v2_rootcause_verdict.md` | `973103878D6F` | 24,847 | 协作圈知识库 |

> v3 与 v2 字面差异：Tag-A 由 v2 之 28 件扩展为 **30 件**（v2.2 ruleset_v2 executor + v2.2 verdict + coding review 为本轮新增正式成果件；沿补账件 v2 §8.1 字面 30 件）

### 2.3 Tag-B 上传清单（MAIN 内 cleanup 链 10 件 · v3 较 v2 增 4 件）

| # | 新路径（MAIN 内） | SHA-12（on-disk） | 字节 | 目标渠道（建议） |
|---|---|---|---|---|
| B-1 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `32CC61D394F2` | 19,104 | 协作圈知识库（治理透明面） |
| B-2 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025E871726B` | 18,829 | 协作圈知识库（v1 ledger） |
| B-3 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64C4EF850025` | 47,909 | 协作圈知识库（v2 ledger · 棒 3） |
| B-4 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8F5136E176B8` | 31,689 | 协作圈知识库（v3 ledger · 棒 4） |
| B-5 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | `9BD8932FA214` | 37,047 | 协作圈知识库（v4 ledger · 棒 5） |
| B-6 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272E8C752406` | 46,058 | 协作圈知识库（v5 ledger · 棒 6） |
| B-7（v3 新增） | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `6F3F6FA3AB1D` | 24,491 | 协作圈知识库（noise v3 manifest） |
| B-8（v3 新增） | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `F586A5A21584` | 27,909 | 协作圈知识库（棒 7 manifest v2） |
| B-9（v3 新增） | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `CC498BC28525` | 37,629 | 协作圈知识库（v6 ledger · 归档二棒） |
| B-10（v3 新增） | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | `68F66904C0C8` | 22,863 | 协作圈知识库（evidence-auditor 审链件） |

> v3 与 v2 字面差异：Tag-B 由 v2 之 6 件扩展为 **10 件**（noise v3 + manifest v2 + ledger v6 + 审链件 4 件为归档二棒 / 证据链期间新增）

### 2.4 本轮出具之勘误件 + 补账件 + 补账件 v2 + 勘误链 v17（v3 较 v2 增补账件 v2 + 勘误链 v17）

| # | 新路径（MAIN 内） | SHA-12（on-disk） | 字节 | 目标渠道（建议） |
|---|---|---|---|---|
| E-1 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | `55CD332F66F2` | 10,288 | 协作圈知识库（与 §2.2 项 1-30 同步发布，避免下游误读盘点件） |
| E-2 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `C64146C4CCAC` | 23,152 | 协作圈知识库（清理六棒后最终布局登记面，与 E-1 + 盘点件同步发布） |
| E-3（v3 新增） | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | （落盘后实测） | （落盘后实测） | 协作圈知识库（**归档二棒后 + 全链补账**，与 E-1 + E-2 + 盘点件同步发布） |
| E-4 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v17） | `2DD8039D47E4` | 198,204 | 协作圈知识库（含 E-1…E-34 完整登记 + v17 §22.7 E-34 5 子条 + v14 §20 E-31 R4 处置收口） |

> v3 与 v2 字面差异：E 由 v2 之 3 件扩展为 **4 件**（E-3 补账件 v2 + E-4 勘误链 v17 为归档二棒 / 拍板留痕后新增；E-4 字节由 v14 141,013 增至 v17 198,204，差异源于 §21 E-32 + §22 E-33 + §22.7 E-34 三段追加）

### 2.5 上传前实测校验（强制）

KIMI 上传前**逐件实测 SHA-12**（`Get-FileHash -Algorithm SHA256` 或等价工具），与本表 SHA-12 字段**逐字符一致方可执行**；任何不一致立即停手并报告 PI / doc-writer / parent；禁止「差不多就传」。

## 3. no-upload 清单（严禁上传）

### 3.1 dataset 推理全文隐私面（v3 沿 v2 字面 · 沿 ledger v6 §4.2 字面 10 件留原地）

下列件**禁止上传 / 禁止转储到公网 / 禁止贴第三方服务 / 禁止贴 chat 类工具**：

| 件 | 性质 | 处置 |
|---|---|---|
| `results/_v4_pi_cot_v2_dataset.json`（12,672 B · SHA-12 `7B01CD835A41`） | 任务 B v2.2 dataset，**含推理全文 / 拍板痕迹 / 原始 prompt / 原始输出** | **仅入本地件；禁止公网化** |
| `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json`（4,103 B · `172093A23E4B`） | dataset addendum | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json`（6,132 B · `439721007AAF`） | D2 wave1 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json`（7,566 B · `41D6C28CA87C`） | D2 wave2 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json`（6,666 B · `99C58906F792`） | D2 wave3 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json`（7,668 B · `C6D092F77932`） | D2 wave4 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json`（10,257 B · `26F110A6E571`） | D2 wave5 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json`（11,589 B · `6E104E2DB038`） | D3 wave1 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json`（14,722 B · `D96B747BFC6C`） | D3 wave2 | **仅入本地件** |
| `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json`（19,615 B · `401BD614CDF7`） | D3 wave3 | **仅入本地件** |

> v3 字面较 v2 字面差异：v2 字面以 5 件 dataset + verdict/result 列严禁；**v3 字面明示 10 件 dataset（v1.1 + 9 件 addendum）全部严禁**（沿 ledger v6 §4.2 字面「dataset 七件 / 实测 10 件」口径 + signoff `BA4D07BD7000` §0.4 字面 9 件 addendum 实测）

**判定准则**：任何含「完整 prompt / 完整输出 / 推理 chain-of-thought 原文」的件 = **仅入本地件**；结论 / 摘要 / 数字结论 = 可入协作圈通报 / 论文 / 项目主页（按既有口径）。

> **可入协作圈口径例外**：
> - `results/_v4_pi_cot_v2_prereg.md`（4,247 B · SHA-12 `CC25C5149CE1`）= 任务 B v2.2 prereg（claim 重定三指标）= **可入协作圈知识库**（无隐私面）；dataset / verdict / result 严禁跟随
> - `results/_v4_pi_cot_v2_verdict_v2.md`（33,723 B · SHA-12 `5D79E67A4E9D`）= 任务 B v2.2 verdict **可入协作圈知识库**（沿 §2.2 #28 列入 Tag-A）；verdict 全文含 kill-line 字面 + 复合定性字面 + 诚实纪律复核字面（非推理全文隐私面）；但 verdict 字面外**严禁跟随 dataset / result / addendum**

### 3.2 `_non_upload_local_archive` 内件（v3 较 v2 更新件数：全 1,669 件严禁上传）

`_non_upload_local_archive`（路径 `〔本地归档区〕\`）= **V1-V2 时代冻结快照 + 私有归档面 + 清理六棒移动件接收点**——**全 1,669 件严禁上传 / 严禁转储 / 严禁复制到公网 / 严禁贴第三方服务**。

> v3 与 v2 字面差异：v2 字面以「V1-V2 时代冻结快照 + 私有归档面」描述；**v3 字面维持 1,669 件实测数 + 归档二棒 0 件移入（沿 ledger v6 §0 字面「arch 实际 = 1,669（本棒未触 A 路径，0 变化）」）**

KIMI 若发现本目录任何子件出现在 §2 上传清单——**立即停手并报告**；本件出具时确认本目录**0 件**在 §2 上传清单内。

### 3.3 SUB / 其他仓外目录内件（v3 沿 v2 字面 · 沿 ledger v6 §E.2 字面 6 项路径差异注记）

- **SUB**（`_repo_mirror\`）——除 §2 已列入外，**Tag-C / B-path 移出件 / 灰区件 / `_archive_2026_09_20/` 旧归档件严禁上传**（详 v2 ledger `64C4EF850025` §C/§G 对账表 + v3/v4/v6 ledger §A/§B）；本目录终态 467 件中 0 件在 §2 上传清单内
- **仓外其他目录**（`〔本地资料区〕\` 其他子目录）——0 件在 §2 上传清单内
- **6 项路径差异注记**（沿 ledger v6 §E.2 字面，引用方文本不动）：
  1. `_v4_pi_cot_v2_coding_review_2026_09_26.md` 字面引用 `_tmp_*.py`（4 件：`_tmp_degen.py` / `_tmp_v1_recompute.py` / `_tmp_v2_redesign.py` / `_tmp_verify.py`）——已 Move-Item 至 `deposon-sub/_tmp_*.py`（sub root），引用方文本不动
  3-7. `_v3_v4_achievements_inventory_2026_09_24.md` / `_v3_v4_achievements_inventory_3dir_2026_09_24.md` / `_v3_v4_ghostref_reconciliation_2026_09_23.md` / `_archive_manifest_deposon_sub_2026_09_23.json` / `_ghostref_copy_log_2026_09_23.json` 字面引用 50 件 B 类候选——50 件 B 类候选均已 Move / Trash，引用方文本不动
  8-13. `_v4_supp_l14v3_model_mapping_2026_09_24.md` / `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` / `_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` / `_v4_supp_prereg_v02_add_T15_2026_09_24.md` / `_v4_supp_prereg_v02_add_T1_2026_09_24.md` / `_v4_track2_multimodel_verdict_2026_09_23.md` 字面引用 `_track2_endpoints_probe_2026_09_23.json`——已 Move-Item 至 `deposon-sub/results/_track2_endpoints_probe_2026_09_23.json`，引用方文本不动

### 3.4 frozen + verifier + P-G 内件（沿不动底线）

- 18 frozen 件 + 9 网格件（详 `docs/V3X/` 报告层 + `results/_v4_*` 链）——**整段不动**，是否上传由 PI 当日另行拍板
- P-G v0 / v01 链 + plugin spec v0.x + verifier 内置脚本——**整段不动**

## 4. 上传执行规范（强制）

### 4.1 SHA-12 校验（先验后传）

- 上传前**逐件实测 SHA-12**（详 §2.5）
- 上传完成后**逐件回拉**实测 SHA-12（与上传前 + 与本表**三方一致**方可宣告上传完成）
- 任一不一致 = 上传失败；立即重传或报告

### 4.2 通道与凭据

- 本件**不含 API key / 凭据 / token**；KIMI 自备通道与凭据
- 凭据 **runtime 读不入 prompt / JSON / log**——严守 key 永不明文铁律
- 凡经 teamorouter / openrouter 的请求一律走 tun 代理（PI 2026-09-23 拍板防封号；`http://127.0.0.1:1018` / `socks5://127.0.0.1:1018`）

### 4.3 通道清单（PI 另行指认）

- arXiv 通道（论文终稿）：PI 另行指认；本件出具时 PI 未明示是否同步上 arXiv
- 项目主页 / 协作圈知识库 / GitHub Pages 等：PI 另行指认
- KIMI 按 PI 当日明示派发执行；本件**不预设**具体通道

### 4.4 失败处置

- 任一件上传失败（SHA 不一致 / 通道报错 / 网络中断 / 凭据失效等）——KIMI 立即停手并以回函件形式报告 PI / doc-writer / parent
- 回函路径：`letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md`（命名建议，与 v1/v2 回函件命名区分）
- 回函含：失败件路径 + 实测 SHA-12 + 通道错误信息 + 已上传件列表

## 5. 引用规范（强制）

- 所有路径引用**仅路径 + SHA-12 + 字节数**（如 `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` · 落盘后实测字节 · SHA-12 落盘后实测）
- v6 ledger 路径对账：详 `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` §3（旧→新路径对账表）+ v1-v5 ledger 各自 §A/§B/§C/§G 作为补充核对源
- **锚链口径统一**：所有 SHA-12 字段 = on-disk SHA-12（盘实测）；指纹字段口径待 PI 拍板，**本上传信不用指纹字段**（沿 E-34.5 §22.7.5 字面）
- 不复制原文段落 / 不贴 JSON 内容 / 不贴 dataset 内部字段
- **三目录盘点 / 勘误 / 补账 v1 / 补账件 v2 引用须四件套并列**（盘点件 `3E4E90FB48E1` + 勘误件 `55CD332F66F2` + 补账件 v1 `C64146C4CCAC` + 补账件 v2 [本轮新出]）

## 6. 回函期望

- **交付物**：上传执行报告（md / JSON，按 KIMI 惯例）
- **交付路径**：`letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md`（命名建议，与 v1/v2 回函件命名区分）
- **回函含**：
  1. 逐件上传前 / 上传后 SHA-12 实测对照表
  2. 失败件列表（如有）+ 失败根因
  3. 通道使用清单（如使用 teamorouter / openrouter，需注明走 tun 代理）
  4. AI-use disclosure（沿 `letters/_v4_distillation_reply_coze_2026_09_20.md` 既有口径）
  5. SHA-12 自核节（回函件本身）

## 7. 老实交代

- 本件不含任何 API key / 凭据 / token——KIMI 自备
- 本件不含上传工具 / 通道 / 凭据预设——KIMI 按 §4.3 PI 当日派发执行
- 本件 §2 上传清单 + §3 no-upload 清单均经 parent 落盘前实测核对（hashlib.sha256）；非「看着合理就写」
- §2.5 上传前实测校验是**强制项**——KIMI 不得跳过
- §3.1 dataset 10 件（v1.1 + 9 件 addendum）严禁公网化——任何「为方便起见贴 chat 工具核验」均违规
- §3.2 `_non_upload_local_archive` 全 1,669 件严禁——KIMI 不得以「归档件已成熟」或「清理移动件已稳定」为由上传
- §3.3 SUB 467 件严禁——6 项路径差异注记（沿 ledger v6 §E.2 字面）引用方文本不动，KIMI 不得以「路径已变」为由擅改被引用件
- v2 件 `ADFA7DD03F76` 0 触动；本件为 v3 新件新名
- 0 触发任何派生 JSON 合并 / 阈值调整 / 既有件触动
- 本件未调用任何外部 LLM / 未调用任何 API
- **涉 KIMI / GLM 表述一律以 PI 的 github 为唯一权威源（受托方已知）**——本委托信不写具体 github URL，不写具体模型版本号，不擅自代填（沿 `ask_9c8751ec`「你侧无额外补充」字面）

---

## §Z SHA-12 自核尾注

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| 本委托信 v3（落盘后） | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | （落盘后填） | （落盘后填） |
| 委托信 v2（0 触动） | `letters/_v4_commission_upload_executor_2026_09_24_v2.md` | 13,012 | `ADFA7DD03F76` |
| 三目录盘点（底账） | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,687 | `3E4E90FB48E1` |
| 三目录盘点勘误件 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | `55CD332F66F2` |
| 三目录盘点补账件 v1 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | `C64146C4CCAC` |
| 三目录盘点补账件 v2（本轮新出） | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | （落盘后实测） | （落盘后实测） |
| cleanup manifest（棒 1） | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` |
| cleanup ledger v1（棒 2） | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | `4025E871726B` |
| cleanup ledger v2（棒 3，路径对账表） | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | `64C4EF850025` |
| cleanup ledger v3（棒 4） | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | `8F5136E176B8` |
| cleanup ledger v4（棒 5） | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | `9BD8932FA214` |
| cleanup ledger v5（棒 6） | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | `272E8C752406` |
| cleanup ledger v6（归档二棒，§3.3 路径差异注记源） | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | `CC498BC28525` |
| cleanup manifest v2（棒 7） | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | `F586A5A21584` |
| noise cleanup v3 | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | `6F3F6FA3AB1D` |
| 证据链审链件 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 22,863 | `68F66904C0C8` |
| V3 资产勘误链 v17 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 198,204 | `2DD8039D47E4` |
| 任务 B v2.2 verdict（§2.2 #28，§3.1 严禁全文） | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | `5D79E67A4E9D` |
| 任务 B v2.2 verdict signoff | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | `BA4D07BD7000` |
| 任务 B v2.2 coding review | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | `5FBEC21E0AD2` |
| 任务 B v2.2 ruleset_v2 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | `C5B3DD141655` |
| 任务 B v2.2 ruleset_v2 executor | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | `EB22F13D571C` |
| 任务 B v2.2 prereg（§3.1 可入协作圈） | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | `CC25C5149CE1` |
| 任务 B v2.2 dataset（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7B01CD835A41` |
| 任务 B v2.2 dataset addendum（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` |
| 任务 B v2.2 dataset addendum d2（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | `439721007AAF` |
| 任务 B v2.2 dataset addendum d2b（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | `41D6C28CA87C` |
| 任务 B v2.2 dataset addendum d2c（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | `99C58906F792` |
| 任务 B v2.2 dataset addendum d2d（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | `C6D092F77932` |
| 任务 B v2.2 dataset addendum d2e（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | `26F110A6E571` |
| 任务 B v2.2 dataset addendum d3a（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | `6E104E2DB038` |
| 任务 B v2.2 dataset addendum d3b（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | `D96B747BFC6C` |
| 任务 B v2.2 dataset addendum d3c（§3.1 严禁） | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | `401BD614CDF7` |

— 委托方：doc-writer（agent-0032834a3e04） · 2026-09-26 19:50 GMT+8 —