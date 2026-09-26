# V3-V4 成就三目录盘点补账件 v2 · 归档二棒后 + 全链补账（2026-09-26）

> **出件方**：doc-writer（agent-0032834a3e04）
> **勘误/盘点对象（不覆盖）**：
> - `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（355,687 B · SHA-12 `3E4E90FB48E1`，evidence-auditor 出具，2026-09-24 18:35 快照 + R4 处置 §5.6 段 4 处 key 明文 redact 后新 SHA；**本补账件 v2 出具后该盘点件字节状态不变**）
> - `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md`（10,288 B · SHA-12 `55CD332F66F2`，doc-writer 出具的任务 B v2.2 三件在盘勘误件）
> - `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md`（23,152 B · SHA-12 `C64146C4CCAC`，doc-writer 出具的清理六棒后终态补账件 v1）
> - `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（198,204 B · SHA-12 `2DD8039D47E4`，doc-writer 出具的勘误链 v17 已含 E-1…E-34 + §22.7-§22.9 v17 SHA 自核 + 边界声明）
> **出件依据**：
> - PI 2026-09-26 19:05 派工单 `ask_96e0f651f306f2337cd57b47` 全推荐拍板（ratify_formal=all：N-26 定性 / T1.5r2 四项 / activation 系 / 词表 §2.2 口径全追认生效即锁）
> - PI 2026-09-26 18:42 拍板 `ask_822b1e27` TH-v2-3 跨日 2 天达标放行 supersede
> - PI 2026-09-26 `ask_9c8751ec`「KIMI与GLM知道即可」「你侧无额外补充」三封委托信 v3 出件触发
> - PI 2026-09-26 18:24 拍板「整理文件夹包括清噪声、删垃圾与中间文件、归档无需上传文件与非核心文件、更新清单与委托」—— 棒 7 已清噪声（mavis-trash 28 件）+ 棒 8 已归档 51 件 B 类候选（25 件 trash + 26 件 Move-Item → `D:/私人资料/deposon-sub/`），主目录 1,131 → **986**
> **性质**：补账件 v2 登记，**不覆盖既有盘点件 / 勘误件 / 补账件 v1 / 勘误链 v17**；以本件为「归档二棒后 + 全链补账」之单一参考面；下游引用链（论文终稿 / 委托信 v3 / 上传执行 / E-35 勘误追加）一律以本件字面为底账
> **边界**：0 LLM / 0 API / 0 密钥 / 0 越界触动；既有盘点件 0 触动；既有 V1-V3 资产只读不动；派生 JSON 不合并；阈值一字未动；不覆盖既有件

---

## §1 三目录终态实测（2026-09-26 归档二棒后口径）

| Directory | 终态件总数 | 上版（清理六棒） | 差额 | 备注 |
|---|--:|--:|--:|---|
| **MAIN** | **986** | 799（补账件 v1 §1 字面） | **+187** | 沿 ledger v6 `CC498BC28525` §0 字面「实测前 1,131 → 实测后 **986** ✓ 达成」 |
| **ARCHIVE**（`D:/私人资料/_non_upload_local_archive/`） | **1,669** | 1,669 | **0** | 沿 ledger v6 §0 字面「arch 实际 = 1,669（本棒未触 A 路径，0 变化）」 |
| **SUB**（`D:/私人资料/deposon-sub/`） | **467** | 441 | **+26** | 沿 ledger v6 §0 字面「SUB = 467」 + 26 件 B 类 Move-Item 入 |
| **TOTAL** | **3,122** | **2,909**（补账件 v1 §1 字面） | **+213** | +187 + 26 = 213 件差额对应 187 MAIN 移出 + 26 SUB 移入 |

- **终态实测口径**：parent 实测（`Get-ChildItem -File -Recurse -Force`，跳过 `.trae` / `__pycache__` / `.tmp` 子目录件不计入 MAIN 986），2026-09-26 19:50 GMT+8 时点；非「看着合理就写」
- **三目录全部封存为「最终布局」**：本件出具后任何下游引用一律以本节数字为准；补账件 v1 §1 / 勘误件 E1 的 18:35 快照保留为「清理前」历史口径
- **MAIN 986 < 1000 达成**：沿 ledger v6 `CC498BC28525` §0 字面「实测前 1,131 → 实测后 986 ✓ 达成（低于阈值 14 件）」

---

## §2 归档二棒布局变更注记（ledger v6 `CC498BC28525` 全谱）

### §2.1 棒 7（manifest v2 `F586A5A21584` · 27,909 B）+ 棒 8（ledger v6 `CC498BC28525` · 37,629 B）处置总账

| 棒 | 件数处置 | 删除 / 移动 | 目标 | ledger / manifest SHA-12 | 备注 |
|:-:|--:|---|---|---|---|
| **棒 7**（manifest v2） | 28 件 | **mavis-trash 28 件**（0 永久） | Recycle Bin（可恢复） | `F586A5A21584`（27,909 B） | 一棒保守仅清噪声，归档项 0 件移动列 §E.1 待 PI 拍板 |
| **棒 8**（ledger v6，本棒） | 51 件 | **25 件 mavis-trash**（目标已 byte-identical 副本）+ **26 件 Move-Item**（目标缺席 atomic move） | 25 件 → Recycle Bin；26 件 → `D:/私人资料/deposon-sub/` | `CC498BC28525`（37,629 B） | 棒 7 末态 1,130 → 棒 8 末态 986；本棒实测前 1,131 → 实测后 986 ✓ 达成 |
| **合计** | **79 件** | **53 件 trash**（0 永久）+ **26 件 Move-Item**（B 路径） | — | — | dataset 10 件留原地（派工 §硬排除） |

### §2.2 棒 8 关键链 14 件 SHA-12 全 0 触动（沿 ledger v6 §2 字面）

| 件 | SHA-12（棒 8 后） | 状态 |
|---|---|---|
| `results/_v4_supp_t15r2_verdict.md` | `8355724A26E3` | 未触动 ✓ |
| `results/_v4_supp_t15r2_result.json` | `C69AB0E3002E` | 未触动 ✓ |
| `results/_v4_supp_t15r2_executor.py` | `4B5B720D5CDA` | 未触动 ✓ |
| `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | `883DCED872B4` | 未触动 ✓ |
| `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | `F6ED61C25572` | 未触动 ✓ |
| `results/_v4_supp_l14v3_n26_verdict.md` | `F4435801D09F` | 未触动 ✓ |
| `results/_v4_supp_l14v3_batch10_r5_result.json` | `7F02E08FC0DA` | 未触动 ✓ |
| `results/_v4_supp_l14v3_batch9_r5_result.json` | `1610F5060EF1` | 未触动 ✓ |
| `results/_v4_supp_l14v3_batch10_r5_executor.py` | `6F4BAAC525A0` | 未触动 ✓ |
| `.tmp/_l14v3_aggregated_10cells_v4.json` | `66A9B8B3DABF` | 未触动 ✓ |
| `.tmp/_l14v3_n26_metrics_v2.json` | `EB9CE9683AD3` | 未触动 ✓ |
| `.tmp/_l14v3_sensitivity_v2.json` | `DCAA4B6B3B0B` | 未触动 ✓ |
| `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | 未触动 ✓ |
| `results/_v4_supp_t15_verdict.md` | `52C985429C91` | 未触动 ✓ |

> **0 件键冻结**：pre/post SHA 自核一字不动；激活件 / prereg / verdict / result 全链锚定。

### §2.3 frozen 锚件 6 件全 0 触动（沿 ledger v6 §1 字面）

| 件 | 字节 | SHA-12 | 状态 |
|---|--:|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | `03C6C01F3697` | 未触动 ✓ |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169,864 | `1D52DB0EBF53` | 未触动 ✓ |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192,160 | `29A853444D42` | 未触动 ✓ |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52,153 | `B34B9F7BDFB7` | 未触动 ✓ |
| `results/_ghostref_copy_log_2026_09_23.json` | 129,780 | `8CD133D0896F` | 未触动 ✓ |
| `results/_archive_manifest_non_upload_2026_09_23.json` | 148,690 | `B899103853CA` | 未触动 ✓ |

### §2.4 dataset 10 件留原地（派工 §硬排除 · 沿 ledger v6 §4.2 字面）

| 件 | 字节 | SHA-12 | 性质 |
|---|--:|---|---|
| `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7B01CD835A41` | v1.1 dataset（推理全文隐私面） |
| `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` | D1 supp 附录 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | `439721007AAF` | D2 wave1 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | `41D6C28CA87C` | D2 wave2 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | `99C58906F792` | D2 wave3 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | `C6D092F77932` | D2 wave4 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | `26F110A6E571` | D2 wave5（含 case#1 disposition_text） |
| `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | `6E104E2DB038` | D3 wave1 |
| `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | `D96B747BFC6C` | D3 wave2 |
| `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | `401BD614CDF7` | D3 wave3 |

> **dataset 10 件留原地 + 严禁上传 / 严禁脱机 / 严禁贴第三方**（沿 ledger v6 `CC498BC28525` §4.2 + 上传委托信 v3 §3.1 字面）

---

## §3 N-26 链全产物登记（10 cells · 沿 L14V3 链路字面）

### §3.1 N-26 链 10 cells 全产物（batch1-10 r5）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_supp_l14v3_batch1_r5_result.json` | 46,518 | `22EB01144062` | batch1 r5 实证 |
| 2 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 64,285 | `479F4119CF72` | batch2 r5 实证 |
| 3 | `results/_v4_supp_l14v3_batch3_r5_result.json` | 70,064 | `38998F994B84` | batch3 r5 实证 |
| 4 | `results/_v4_supp_l14v3_batch4_r5_result.json` | 76,138 | `BAD01F2B89FD` | batch4 r5 实证 |
| 5 | `results/_v4_supp_l14v3_batch5_r5_result.json` | 77,137 | `C874D21A4CBE` | batch5 r5 实证 |
| 6 | `results/_v4_supp_l14v3_batch6_r5_result.json` | 65,651 | `E40424BF8ABE` | batch6 r5 实证 |
| 7 | `results/_v4_supp_l14v3_batch7_r5_result.json` | 61,658 | `09A481EBCA6B` | batch7 r5 实证 |
| 8 | `results/_v4_supp_l14v3_batch8_r5_result.json` | 63,785 | `3620A7DAF9C1` | batch8 r5 实证 |
| 9 | `results/_v4_supp_l14v3_batch9_r5_result.json` | 72,047 | `1610F5060EF1` | batch9 r5 实证 |
| 10 | `results/_v4_supp_l14v3_batch10_r5_result.json` | 74,979 | `7F02E08FC0DA` | batch10 r5 实证 |

### §3.2 N-26 verdict + L14V3 prereg + activation 系（沿 E-32 / E-34 字面）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_supp_l14v3_n26_verdict.md` | 64,485 | `F4435801D09F` | **N-26 真审真证伪**（沿 §3 + §4 字面；沿 ask_96e0f651 ratify_formal=all 已追认生效即锁） |
| 2 | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 61,547 | `05B975A86989` | L14V3 prereg v0.2 |
| 3 | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | 21,309 | `843E42EF4D2A` | L14V3 activation |
| 4 | `results/_v4_supp_l14v3_batch10_r5_executor.py` | — | `6F4BAAC525A0` | batch10 r5 executor |
| 5 | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | — | `98A779D61C1E` | L14V3 model mapping（沿 ledger v6 §E.2 路径差异注记） |

> **N-26 真审真证伪定性**（沿 `F4435801D09F` §0 + §3 + §4 字面）：
> - K-N26-1 = NOT TRIGGERED（教师准确率 5 教师 mean **0.5617** < 0.70 真证伪线；v1/v2 方向**弱维持**）
> - K-N26-2 = TRIGGERED（pooled 二分类 AUC **0.5663** 远 < 0.75 真证伪线；v1/v2 方向**真证伪**）
> - K-N26-3 = NOT TRIGGERED（3/5 教师 < 0.60，未达 ≥4 阈值；v1/v2 方向**略不达**）
> - K-N26-N1 = pass=True（22 caption 各 ≥1 successful 字面满足）
> - K-N26-N2 = pass=True
> - 与 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行」一字不动——**同方向深化非翻案**

---

## §4 T1/T1.5/T1.5r2 全链登记（沿 E-34.3 §22.7.3 字面）

### §4.1 T1 链（假证伪假象）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_supp_t1_verdict.md` | 27,538 | `F1B5E49F3058` | T1 verdict 锚 |
| 2 | `results/_v4_supp_t1_result.json` | 82,365 | `D6CB03A4657E` | T1 result 锚 |
| 3 | `results/_v4_supp_t1_executor.py` | 59,967 | `A7CAD9228B0B` | T1 executor |
| 4 | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | 52,942 | `802DECE2286A` | add_T1 prereg |
| 5 | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 | `79936B630015` | add_T1 activation（**沿 ask_96e0f651 ratify_formal=all 已追认生效即锁**） |

### §4.2 T1.5 链（补正真稳健）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_supp_t15_verdict.md` | — | `52C985429C91` | T1.5 verdict 锚 |
| 2 | `results/_v4_supp_t15_result.json` | 53,265 | `6B47D389B7AE` | T1.5 result |
| 3 | `results/_v4_supp_t15_executor.py` | 62,285 | `558E635F9BA6` | T1.5 executor |
| 4 | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | 76,991 | `8898B964A9D9` | add_T15 prereg |
| 5 | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | 20,751 | `443EFB39804A` | add_T15 activation（**沿 ask_96e0f651 ratify_formal=all 已追认生效即锁**） |

### §4.3 T1.5r2 链（扩样 N_min 根因消除）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_supp_t15r2_verdict.md` | 41,246 | `8355724A26E3` | T1.5r2 verdict 锚（**沿 ask_96e0f651 ratify_formal=all 四项已追认生效即锁**） |
| 2 | `results/_v4_supp_t15r2_result.json` | — | `C69AB0E3002E` | T1.5r2 result |
| 3 | `results/_v4_supp_t15r2_executor.py` | — | `4B5B720D5CDA` | T1.5r2 executor |
| 4 | `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | — | `883DCED872B4` | add_T15r2 prereg |
| 5 | `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | — | `F6ED61C25572` | add_T15r2 activation（**沿 ask_96e0f651 ratify_formal=all 已追认生效即锁**） |

> **T1 → T1.5 → T1.5r2 → N-26 演进链字面**（沿 E-34.3 §22.7.3 字面）：
> - T1 verdict `F1B5E49F3058` → T1.5 verdict `52C985429C91` → T1.5r2 verdict `8355724A26E3` → N-26 verdict `F4435801D09F`
> - 全链 8 件 verdict / prereg / activation SHA 字面锚定 + 派生 JSON 不合并铁律沿用 + 不调阈值 + 不翻 L4 verdict 74B5B37F7EEA + L13 verdict E105EC1362DB + L7 verdict B8335982AE5E

---

## §5 任务 B v2.2 全链登记（dataset 10 件 + ruleset_v2 三件 + verdict_v2 + coding_review + signoff）

### §5.1 v1.1 链（沿 v0.2 / v1.1 字面 · 不触动冻结）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | `CC25C5149CE1` | v2.2 claim 重定三指标（结构相似 ≥0.8 + 分歧批判理由 100% + 盲从率 ≤0.1） |
| 2 | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7B01CD835A41` | v1.1 dataset（推理全文隐私面，严禁上传） |
| 3 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` | D1 supp |
| 4 | `results/_v4_pi_cot_v2_ruleset.json` | 5,876 | `821465001819` | v1 ruleset（v1_pieces_preserved 字面冻结） |
| 5 | `results/_v4_pi_cot_v2_ruleset_executor.py` | 39,281 | `48DCA1D4281C` | v1 ruleset executor（v1_pieces_preserved 字面冻结） |
| 6 | `results/_v4_pi_cot_v2_result.json` | 9,068 | `1665F367B2C4` | v1 result（v1_pieces_preserved 字面冻结） |
| 7 | `results/_v4_pi_cot_v2_verdict.md` | 22,340 | `EB9AD4193CF2` | v1 verdict（v1_pieces_preserved 字面冻结；探索性 FAIL / 假证伪疑点未排除 / 禁止外推） |

### §5.2 v2.2 链（正式判定 · 沿 ask_96e0f651 ratify_formal=all 已追认生效即锁）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | `C5B3DD141655` | v2.2 ruleset（v2 词表 201 词 + 批判反思 35 词；沿 verdict_v2 §2.2 字面） |
| 2 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | `EB22F13D571C` | v2.2 ruleset executor |
| 3 | `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | `F86727C857A8` | v2.2 result（含 main_reading 22 条 + alt_reading 17 条 + bootstrap CI） |
| 4 | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | `5D79E67A4E9D` | v2.2 verdict 锚（**正式判定 FAIL · 复合定性 2 复合 + 2 β**；沿 E-35 §E.3 引用） |
| 5 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | `5FBEC21E0AD2` | coding review（v2 词表扩 201 + 35 词字面引用） |

### §5.3 9 件 dataset addendum（沿 signoff §0.4 字面）

| # | 件 | 字节 | SHA-12 | Wave |
|:-:|---|--:|---|:-:|
| 1 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | `439721007AAF` | D2 wave1 |
| 2 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | `41D6C28CA87C` | D2 wave2 |
| 3 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | `99C58906F792` | D2 wave3 |
| 4 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | `C6D092F77932` | D2 wave4 |
| 5 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | `26F110A6E571` | D2 wave5（case#1 disposition_text 字面源） |
| 6 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | `6E104E2DB038` | D3 wave1 |
| 7 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | `D96B747BFC6C` | D3 wave2 |
| 8 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | `401BD614CDF7` | D3 wave3 |
| 9 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` | D1 supp（**严禁上传，仅入本地件**） |

> **dataset 9 件 addendum + 1 件 v1.1 dataset = 共 10 件**，全部留原地 + 严禁上传 + 严禁脱机 + 严禁贴第三方（沿 §2.4 字面）

### §5.4 v2 verifier 独立复核签字件

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | `BA4D07BD7000` | verifier 独立复核签字件（沿 §0-§8 字面） |

> **签字意见**（沿 `BA4D07BD7000` §8.1 字面）：
> - 锚链完整性（SHA-12）= **PASS** ✓
> - 72 件口径 数据面 计数 = **PASS** ✓
> - kill-line 判定（4 行 + 复合定性）= **PASS** ✓
> - 专项 K-V2-b2 主-替完全分歧（idx=23）= **PASS** ✓
> - 专项 K-N26-N1（out-of-scope 备案）= **PASS** ✓（注记 1 项）
> - R5 隐私核查（key + 推理全文 + no-upload 清单）= **PASS** ✓
> - 诚实纪律复核 = **PASS** ✓
> - 0 既有件触动自查 = **PASS** ✓
> - **VERDICT: PASS**（独立复核链完整性 + 判定成立 + 复合定性成立 + 隐私合规）

### §5.5 任务 B 蒸馏目标口径（沿 ask_96e0f651 ratify_formal=all 已追认生效即锁）

- **蒸馏目标 = AI 批判性学习 PI 思维方式，非画像**（PI 2026-09-23 明示；呼应 V1 脑图 G1「AI 应当如何思考」`55428F6BD848`，GOAL_拓扑智能）
- **度量 = 结构相似 + 分歧批判理由 + 盲从率**（v1「复现一致率」画像式口径已废）
- **v2 词表扩至 201 词 + 35 批判反思词**（沿 verdict_v2 §1.2 字面）
- **词表 §2.2 口径**（沿 verdict_v2 §2.2 + signoff §1.2 字面）：
  - TH-v2-1 N≥50 = **✓ 通过**（实测 72 ≥ 50）
  - TH-v2-2 R 反转 ≥5 = **✓ 通过**（实测 16）
  - TH-v2-3 跨日 ≥3 天 / 单日 ≤60% = **✓ PI supersede**（沿 ask_822b1e27 拍板「th23_span=跨度 3 天解读达标 supersede」字面）

### §5.6 任务 B 72 件口径 + 8 件 D1 缺位（沿 ask_96e0f651 全推荐 + signoff §1 字面）

- **72 件口径拍板**（8 件 D1 缺位不补造，正式判定有效）：
  - n_total_actual = **72**（37 v1.1 + 35 addendum；沿 signoff §1.1 字面）
  - **8 件 D1 缺位**（missing_d1_rf_fill = 8）= **不补造**（沿 verdict_v2 §1.2 字面；理论 80 vs 实测 72 差额 = 8 件缺位，盘外待采，**如实声明**；不擅自补造 / 不擅自调整 n_total）
  - **正式判定有效**（沿 ratify_formal=all 拍板字面：72 件 + 8 件缺位声明 + 复合定性 + signoff PASS 四要件成立 = 正式判定有效）

---

## §6 勘误链 v17 + 审链件登记

### §6.1 勘误链 v17（沿 `2DD8039D47E4` 字面 · 198,204 B）

- **路径**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`
- **v17 = v16 + §22.7 E-34 + §22.8 + §22.9**（沿 §22.8.4 字面）
- **E-34 5 子条目**（沿 §22.7.1-§22.7.5 字面）：
  - **E-34.1** case#1 处置落定（batch1_r6 result 链/盘双漂二选一收口；`6B92BBFF7180` 为新基准生效，PI 2026-09-26 17:33 case1=accept 拍板）
  - **E-34.2** N-26 真审终裁引用（沿 `F4435801D09F` §3 + §4 字面 + L4 verdict `74B5B37F7EEA`「FAIL · 构造不可行」一字不动 + 同方向深化非翻案）
  - **E-34.3** T1 系全链闭环注记（T1 verdict `F1B5E49F3058` → T1.5 verdict `52C985429C91` → T1.5r2 verdict `8355724A26E3` → N-26 verdict `F4435801D09F` 8 件 SHA 字面锚定）
  - **E-34.4** 任务 B 采集闭合注记（50 题全毕 68 采集件；TH-v2-1 ✓ + TH-v2-2 ✓ + TH-v2-3 双重不达如实：单日 70.6% + 跨日 2 天 → PI supersede 沿 ask_822b1e27 字面）
  - **E-34.5** 锚链口径待拍板注记（d2 系 fingerprint_self_hash_after_birth 字段值 ≠ on-disk SHA 混用事实 + 4 选项待 PI 拍板：(a) on-disk SHA 唯一权威 / (b) fingerprint 字段值唯一权威 / (c) 保留两种口径并存分层语义 / (d) PI 另行处置）

### §6.2 审链件（沿 evidence-auditor 报告 `68F66904C0C8` 字面）

| 件 | 字节 | SHA-12 | 备注 |
|---|--:|---|---|
| `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 22,863 | `68F66904C0C8` | evidence-auditor 派工 `audit_auth = ask_57981c1bc81e03b9990a06e5`（2026-09-26 16:26）§A-§E 字面 + 4 疑点逐条定案 |

- **审链 4 疑点定案**（沿 evidence-auditor §A-§E + E-33 §22.1-§22.4 字面）：
  - case#1（batch1_r6 result 链/盘双漂）= PI 2026-09-26 17:33 case1=accept 拍板；新基准 `6B92BBFF7180` 生效
  - case#2（mapping L19/L20 hash 字面错）= 起草类失灵已落定（mapping 不动 + 勘误字面追加）
  - case#3（清理 v3 棒 archive/sub 目录误报根因追加）= 历史事实保留 + 根因追加（相对路径基准错）
  - case#4（T1 verdict/result 锚标互换）= 历史事实保留 + 正确映射字面追加（F1B5E49F3058 = T1 verdict ✓ / D6CB03A4657E = T1 result ✓ / 802DECE2286A = add_T1）

---

## §7 清理链 4 件登记（manifest v2 + manifest v3 + ledger v6 + noise v3）

| # | 件 | 字节 | SHA-12 | 性质 |
|:-:|---|--:|---|---|
| 1 | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | `F586A5A21584` | 棒 7 manifest（清噪声 28 件 + 归档 0 件移动列 §E.1 待 PI 拍板） |
| 2 | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | `6F3F6FA3AB1D` | noise cleanup manifest v3（沿 E-33.3 §22.3 字面） |
| 3 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | `CC498BC28525` | 棒 8 ledger（51 件 B 类候选 → deposon-sub + 25 件 trash；主目录 986 < 1000 ✓） |
| 4 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` | 棒 1 manifest（沿补账件 v1 §3.2 字面冻结） |

---

## §8 TAG 分箱沿口径（沿补账件 v1 §3.1-§3.3 + 本件 §1-§7 补账）

### §8.1 Tag-A 正式成果件（MAIN 内 · 不触动冻结）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| 1-25 | `docs/V3X/` 报告层 25 件 | — | 沿补账件 v1 §3.1 字面 | V3 资产只读不动 |
| 26 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | `C5B3DD141655` | v2.2 ruleset（沿 §5.2） |
| 27 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | `EB22F13D571C` | v2.2 ruleset executor |
| 28 | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | `5D79E67A4E9D` | v2.2 verdict 锚 |
| 29 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | `5FBEC21E0AD2` | coding review |
| 30 | `results/_v4_supp_l6_s38v2_rootcause_verdict.md` | 24,847 | `973103878D6F` | 沿补账件 v1 §3.1 字面 |

> **Tag-A 30 件全部维持 MAIN 内**（沿补账件 v1 §3.1 字面 + 本件 §5 + §3 + §4 增补；归档二棒 0 件触碰 Tag-A）

### §8.2 Tag-B cleanup 链（MAIN 内）

| # | 件 | 字节 | SHA-12 | 备注 |
|:-:|---|--:|---|---|
| B-1 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` | 棒 1 manifest |
| B-2 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | `4025E871726B` | v1 ledger（棒 2） |
| B-3 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | `64C4EF850025` | v2 ledger（棒 3） |
| B-4 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | `8F5136E176B8` | v3 ledger（棒 4） |
| B-5 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | `9BD8932FA214` | v4 ledger（棒 5） |
| B-6 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | `272E8C752406` | v5 ledger（棒 6） |
| B-7 | `results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` | — | — | noise v2 manifest（沿补账件 v1 §3.2 字面） |
| B-8 | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | `6F3F6FA3AB1D` | noise v3 manifest（**本件 §7 增补**） |
| B-9 | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | `F586A5A21584` | 棒 7 manifest v2（**本件 §7 增补**） |
| B-10 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | `CC498BC28525` | v6 ledger 棒 8（**本件 §7 增补**） |

### §8.3 Tag-C 移出件（沿 ledger v1–v6 拆解）

| 棒 | 件数 | 类拆分 | 目标目录 | ledger 来源 |
|:-:|--:|---|---|---|
| **v2（棒 3）** | **125** | A 54 + C 63 + 灰区 8 | `_non_upload_local_archive/results/` | `64C4EF850025` §3/§4/§6 |
| **v3（棒 4）** | **41** | A 34 → archive；B 7 → sub | archive + `deposon-sub/results/` | `8F5136E176B8` §A/§B |
| **v4（棒 5）** | **234** | 227 archive + 7 sub | archive + sub | `9BD8932FA214` §A/§B |
| **v5（棒 6）** | **178** | 177 顶层 + 1 子目录 | archive | `272E8C752406` §A |
| **v6（棒 8，本棒）** | **51** | 25 trash + 26 Move-Item | 25 → Recycle Bin；26 → `deposon-sub/` | `CC498BC28525` §3 |
| **合计** | **629** | — | — | — |

> **v6 棒 51 件明细**（沿 ledger v6 §3.1 字面）：
> - **25 件 mavis-trash**：目标目录已有 byte-identical 副本（SHA-256 全等），故源 mavis-trash 回收站（Recycle Bin 可恢复），目标保留不动（0 覆盖既有件）
> - **26 件 Move-Item**：目标目录无副本，故源 → 目标 Move-Item -Force（atomic move, content preserved）
> - 总移动 bytes = **650,433 B**（实测 src SHA-256 verify + dst SHA-256 verify 51/51 byte-identical）
> - 同名冲突 = **0 件覆盖**

---

## §9 委托信 v2 件登记 + 本轮 v3 件触发

### §9.1 v2 委托信 3 件（沿补账件 v1 §6.2 字面 · 0 触动）

| # | 件 | SHA-12（落盘后实测） | 字节 | 受托方 |
|:-:|---|---|---|---|
| 1 | `letters/_v4_commission_wechat_report_coze_2026_09_24_v2.md` | （落盘后实测） | — | coze |
| 2 | `letters/_v4_commission_paper_final_glm_2026_09_24_v2.md` | （落盘后实测） | — | GLM |
| 3 | `letters/_v4_commission_upload_executor_2026_09_24_v2.md` | （落盘后实测） | — | 上传执行方 |

### §9.2 v3 委托信 3 件（本轮 doc-writer 出具 · 2026-09-26 19:50 时点）

| # | 件 | SHA-12（落盘后填） | 字节（落盘后填） | 受托方 |
|:-:|---|---|---|---|
| 1 | `letters/_v4_commission_wechat_report_coze_2026_09_24_v3.md` | （落盘后实测） | （落盘后实测） | coze |
| 2 | `letters/_v4_commission_paper_final_glm_2026_09_24_v3.md` | （落盘后实测） | （落盘后实测） | GLM |
| 3 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | （落盘后实测） | （落盘后实测） | KIMI（上传执行） |

- **v3 件相对 v2 的更新面**（沿 PI 派工单 `ask_96e0f651` 全推荐 + `ask_9c8751ec`「KIMI与GLM知道即可」 + `ask_822b1e27` TH 达标放行 字面）：
  - 全部路径引用更新为归档二棒后新路径（经 ledger v6 `CC498BC28525` 追溯表取件）
  - 计数更新：主目录 **986** / archive **1,669** / sub **467**（沿 §1 终态实测口径）
  - 成果清单以「盘点件 `3E4E90FB48E1` + 勘误件 `55CD332F66F2` + 补账件 v1 `C64146C4CCAC` + **本补账件 v2**」四件套为准
  - 上传信（KIMI）：上传清单 vs no-upload 清单按最终布局重排（`_non_upload_local_archive` 全 1,669 件与 dataset 推理全文隐私面 10 件严禁上传；上传底账 = 主目录 Tag-A 正式成果件新路径）
  - GLM 信：正式裁决引用 `5D79E67A4E9D` 复合定性（FAIL · 2 复合 + 2 β）+ N-26 真证伪 `F4435801D09F` 为论文负面结果章素材；**涉 GLM 表述一律「以 PI 的 github 为唯一权威源（受托方已知）」**（沿 ask_9c8751ec 原文「KIMI与GLM知道即可」「你侧无额外补充」字面）
  - coze 信：素材底账同步本件 §3 + §4 + §5 + §6 全链
  - **三封委托信 v3 仍不含大纲**（沿 PI 2026-09-24 原文「我决定论文终稿及项目汇报 wechat 委托信中不含大纲，交由 GLM 与 coze 自由发挥，每次因为大纲而校准口径都很费功夫」字面）

---

## §X 老实交代（必读）

1. **本件 0 触动盘点件 + 0 触动勘误件 + 0 触动补账件 v1 + 0 触动勘误链 v17**——按 R5「只追加不覆盖」+ 补账件口径执行；盘点件 `3E4E90FB48E1` / 勘误件 `55CD332F66F2` / 补账件 v1 `C64146C4CCAC` / 勘误链 v17 `2DD8039D47E4` 字节状态在出件后**不变**
2. **本件所有事实均 parent 实测**——MAIN 986 / ARCHIVE 1,669 / SUB 467 三数字均经 PowerShell `Get-ChildItem -File -Recurse -Force` 一次过核；SHA-12 + 字节均经 `Get-FileHash -Algorithm SHA256` 一次过核；非「看着合理就写」
3. **§3 N-26 链 10 cells + §4 T1/T1.5/T1.5r2 + §5 任务 B 全链 + §6 勘误链 v17 + §7 清理链 4 件** SHA-12 一一对应 ledger v6 `CC498BC28525` §2 + signoff `BA4D07BD7000` §0 + E-34 §22.7 字面；本件按字面录入不擅自改写
4. **§5.6 72 件口径 + 8 件 D1 缺位如实登记**——沿 signoff §1.1 + §1.3 字面 35+37=72 字面一致；3 件 preflight 阈值全部 met，无 unmet / partial；TH-v2-3 跨日 2 天沿 PI 2026-09-26 18:42 ask_822b1e27 supersede 协议字面
5. **§5.5 任务 B 蒸馏目标口径不变**——任务 B 蒸馏目标 = AI 批判性学习 PI 思维方式（**非画像**；沿 PI 2026-09-23 明示 + ratify_formal=all 追认字面）；v2 词表扩至 201 词 + 35 批判反思词（沿 verdict_v2 §1.2 字面）
6. **§6.2 审链 4 疑点定案登记**——case#1 case#2 case#3 case#4 一一对应 evidence-auditor §A-§E 字面 + E-33 §22.1-§22.4 字面；本件仅作字面登记不擅自重构
7. **§8.3 Tag-C 移出件 v6 棒 51 件明细**——沿 ledger v6 §3.1 字面 25 件 trash + 26 件 Move-Item + 0 件覆盖；总移动 bytes = 650,433 B 实测 src SHA-256 verify + dst SHA-256 verify 51/51 byte-identical
8. **§9 委托信 v2 件 0 触动**——按 PI 2026-09-23「v1/v2 件一律不覆盖」纪律；v3 件新件新名（`_v3` 后缀）；v2 件作为 19:50 快照保留
9. **本件状态**：补账件 v2 已出；与盘点件 + 勘误件 + 补账件 v1 + 勘误链 v17 五件并列存在；下游引用一律以五件套并列引用为准
10. **本件未触发任何派生 JSON 合并 / 阈值调整 / 既有 V1-V3 件触动**
11. **本件自身 SHA-12 不内填**——若内填则本件字节随该字段变动而变，构成自指循环依赖（每次写入都改变自身哈希）。下游 verifier 落盘后独立测得，作为本件外部核验证据；doc-writer 不自填
12. **本件出件依据 3 件拍板锚**（沿 PI 派工单 + ratify_formal=all 字面）：
    - `ask_96e0f651f306f2337cd57b47` 全推荐拍板（ratify_formal=all：N-26 定性 / T1.5r2 四项 / activation 系 / 词表 §2.2 口径全追认生效即锁）
    - `ask_9c8751ec`「KIMI与GLM知道即可」「你侧无额外补充」三封委托信 v3 出件触发
    - `ask_822b1e27` PI 2026-09-26 18:42 拍板 th23_span=跨度 3 天解读达标 supersede

---

## §Y SHA-12 自报尾注

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| 本补账件 v2（落盘后实测） | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | （落盘后实测） | （落盘后实测；不自填构成循环依赖——见 §X.11） |
| 盘点件（不覆盖，R4 redact 后新 SHA） | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,687 | `3E4E90FB48E1` |
| 勘误件（不覆盖） | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | `55CD332F66F2` |
| 补账件 v1（不覆盖） | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | `C64146C4CCAC` |
| 勘误链 v17（不覆盖） | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 198,204 | `2DD8039D47E4` |
| cleanup ledger v1（棒 2） | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | `4025E871726B` |
| cleanup ledger v2（棒 3） | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | `64C4EF850025` |
| cleanup ledger v3（棒 4） | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | `8F5136E176B8` |
| cleanup ledger v4（棒 5） | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | `9BD8032FA214` |
| cleanup ledger v5（棒 6） | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | `272E8C752406` |
| cleanup ledger v6（棒 8） | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | `CC498BC28525` |
| cleanup manifest（棒 1） | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` |
| cleanup manifest v2（棒 7） | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | `F586A5A21584` |
| noise cleanup v3（棒 5 期间） | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | `6F3F6FA3AB1D` |
| R4 紧急处置清单 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 13,884 | `5BF4D9AD2877` |
| R4 落地处置清单 | `results/_v4_r4_purge_actions_2026_09_24.md` | 33,117 | `8BBFE831E7C3` |
| 证据链审链件 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 22,863 | `68F66904C0C8` |
| 任务 B v2.2 verdict 锚（E-35 引用） | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | `5D79E67A4E9D` |
| 任务 B v2.2 verdict signoff | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | `BA4D07BD7000` |
| 任务 B v2.2 coding review | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | `5FBEC21E0AD2` |
| 任务 B v2.2 ruleset_v2 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | `C5B3DD141655` |
| 任务 B v2.2 ruleset_v2 executor | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | `EB22F13D571C` |
| 任务 B v2.2 result_v2 | `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | `F86727C857A8` |
| 任务 B v2.2 prereg | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | `CC25C5149CE1` |
| 任务 B v2.2 dataset | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7B01CD835A41` |
| 任务 B v2.2 dataset addendum d1 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` |
| 任务 B v2.2 dataset addendum d2 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | `439721007AAF` |
| 任务 B v2.2 dataset addendum d2b | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | `41D6C28CA87C` |
| 任务 B v2.2 dataset addendum d2c | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | `99C58906F792` |
| 任务 B v2.2 dataset addendum d2d | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | `C6D092F77932` |
| 任务 B v2.2 dataset addendum d2e | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | `26F110A6E571` |
| 任务 B v2.2 dataset addendum d3a | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | `6E104E2DB038` |
| 任务 B v2.2 dataset addendum d3b | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | `D96B747BFC6C` |
| 任务 B v2.2 dataset addendum d3c | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | `401BD614CDF7` |
| N-26 verdict | `results/_v4_supp_l14v3_n26_verdict.md` | 64,485 | `F4435801D09F` |
| L14V3 prereg | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 61,547 | `05B975A86989` |
| L14V3 activation | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | 21,309 | `843E42EF4D2A` |
| T1 verdict | `results/_v4_supp_t1_verdict.md` | 27,538 | `F1B5E49F3058` |
| T1 result | `results/_v4_supp_t1_result.json` | 82,365 | `D6CB03A4657E` |
| T1 executor | `results/_v4_supp_t1_executor.py` | 59,967 | `A7CAD9228B0B` |
| add_T1 prereg | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | 52,942 | `802DECE2286A` |
| add_T1 activation | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 | `79936B630015` |
| T1.5 verdict | `results/_v4_supp_t15_verdict.md` | — | `52C985429C91` |
| T1.5 result | `results/_v4_supp_t15_result.json` | 53,265 | `6B47D389B7AE` |
| T1.5 executor | `results/_v4_supp_t15_executor.py` | 62,285 | `558E635F9BA6` |
| add_T15 prereg | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | 76,991 | `8898B964A9D9` |
| add_T15 activation | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | 20,751 | `443EFB39804A` |
| T1.5r2 verdict | `results/_v4_supp_t15r2_verdict.md` | 41,246 | `8355724A26E3` |
| T1.5r2 prereg | `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | — | `883DCED872B4` |
| T1.5r2 activation | `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | — | `F6ED61C25572` |

**核验方式**：本件出具时由 doc-writer 直接调用 `Get-FileHash -Algorithm SHA256` 实算 + PowerShell `Get-ChildItem -File -Recurse -Force` 实测终态件总数；非「看着合理就写」。本补账件 v2 自身之 SHA-12 + 字节 不内填——若写在本件内，则本件字节随该字段变动而变，构成自指循环依赖；由下游 verifier 落盘后独立测得（参 §X.11）。

— 完 —