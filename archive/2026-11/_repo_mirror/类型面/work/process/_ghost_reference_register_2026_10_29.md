# 幽灵引用登记件（2026-10-29 · 重构后首轮）

> 📌 **本件之性质**：**登记体**。⛔0 改原引一字（沿「⛔0 回改任何既有件」）；⛔0 落五终判；⛔0 代 PI 裁。
> 📌 **所依**：整理之件体例之末步（`_cleanup_noise_register_2026_10_21.md` §6 之同款）；路径映射 `results\.tmp\_relayout_path_map_2026_10_29.jsonl`（2,885 条）。
> 📌 **仪器**：`.tmp\_ghost_refs2.py`；数据 `.tmp\_ghost_refs_2026_10_29.jsonl`。

---

## §1 结论（三句）

1. 本次依树重构**未新增真幽灵**——凡因移动而「路径变」者 **50,684 处**皆可解析（映射表 154 ＋ 按名在活面 50,530）。
2. **真幽灵 4,598 处**（来自 551 件）之主体系**清单件／合册所载之历史件名**，与本次移动无因果关系。
3. 处置沿铁律：**只登记，⛔0 改原引**；改写之依据即映射表。

---

## §2 全量读数（repo 内 `.md`／`.py` 之 `results\` 路径引用）

| 类 | 处数 | 义 |
|:--|--:|:--|
| **重构所致（按名在活面）** | **50,530** | 件在 repo／sub，仅路径已变 ⇒ 文档漂移，非断链 |
| **真幽灵（三区名皆无）** | **4,598** | 三区按名皆无 ⇒ 见 §4 |
| **历史／已归档（名在归档区）** | **3,463** | 件在 `〔归档区〕` |
| **直中在盘** | **212** | 路径未变 |
| **重构所致（映射表可解析）** | **154** | 映射表逐条可对 |
| **合计** | **58,957** | —— |

---

## §3 「可解析」之两类（50,684 处）

| 类 | 例（本部抽样） |
|:--|:--|
| 映射可解析 | `[letters\_commission_kimi_upload_2026_10_22_v]` → `results\_book_13_pre_execution_report_kimi_2026_10_22.md` |
| 按名在活面 | 件名在三区之 repo／sub 命中，仅目录层已变（如原 `results\work\process\X` → 今 `results\L1\V4\work\process\X`） |

⇒ 📌 此两类**不构成运行期断链**（活代码不以其作 I/O 目标者尤然），但**文档文本已过时**。改写依据 ＝ 映射表；改写之执行**须 PI 逐单令**（涉 50,684 处之批量回改，违「⛔0 回改既有件」）。

---

## §4 真幽灵 4,598 处之性质（⛔0 读作重构之过）

**按引用所载日期分**：2026-09 **2,038**｜2026-10 **1,928**｜无日期 **632**。

**源件前 10（按处数）**：

| 源件 | 处数 |
|:--|--:|
| `results\_book_01_adoption_effect_2026_10_22.md` | 349 |
| `results\_book_03_achievements_inventory_full_2026_10_22.md` | 223 |
| `results\evidence\register\_remote_local_reconciliation_2026_10_2x.md` | 197 |
| `results\doc\document\_results_c_class_index_2026_10_22.md` | 194 |
| `results\readout\reading\_mq19_item6_f12_archive_recompute_…` | 184 |
| `results\doc\document\_zone_balance_inventory_2026_10_13.md` | 177 |
| `results\doc\document\_repo_full_inventory_catalogue_2026_10_12.md` | 148 |
| `results\work\process\_kd_family_census_2026_10_20.md` | 119 |
| `results\work\process\_repo_post_cleanup_snapshot_2026_10_12.md` | 94 |
| `results\L2\doc\document\_b8_b6_retention_plan_2026_10_22.md` | 89 |

**抽样六例（本部开卷）**：

| 源 | 所引 | 判 |
|:--|:--|:--|
| `_v3_v4_achievements_inventory` | `results\deposon_v19_benchmark_fixes.json` | 09 月件，已归档 |
| `_exp06_selfverified_renaming` | `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | 09 月件 |
| `_mq19_item6_f12_archive_recompute` | `results\_nonportrait_...n_design_2026_10_10.md` | 名含省略号（清单原文即截断） |
| `_v4_commission_〔IM〕_report_coze_2026_09_24` | `results\_v4_pi_cot_v2_ruleset.json` | 09 月件 |
| `_book_01_adoption_effect` | `results\_v142_adoption_effect_2026_10_19.md` | 清单所列历史件 |
| `_reorg_survey_and_disposition` | `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 09 月件 |

⇒ 📌 **判**：真幽灵之主体＝**清单／合册逐条列出之历史件名**（其件或已归档、或从只在清单中留名），**非本次移动所致**。此与先例 `_cleanup_noise_register` §6 之「MISS 182」同族（彼时任 182／今 4,598，数异因**本轮纳入 `.py` 与全部清单件全文**，射程更宽）。

---

## §5 处置（⛔0 代裁之界内）

| 类 | 处置 | 据 |
|:--|:--|:--|
| 直中在盘 212 | 无需处置 | —— |
| 重构所致 50,684 | **只登记**；改写须 PI 逐单令（映射表现成） | 铁律「⛔0 回改既有件」 |
| 历史／已归档 3,463 | **只登记**（归档区不上传，引之亦不断链） | 同上 |
| 真幽灵 4,598 | **逐条登记·⛔0 改原引** | 先例 §6 同款 |

---

## §6 老实交代（限）

1. **射程**：只扫 repo 之 `.md`／`.py`；sub 与 archive 未扫；`.json`／`.jsonl` 内所引未扫。
2. **正则口径**：`results\…\.(md|json|jsonl|txt|py|tsv|csv|out|log)`，故**无扩展名之引用**与**含空格之路径**未收。
3. **「按名在活面」只是名中，未证其为同一件**（同名异内容者可存）⇒ 该 50,530 处之「可解析」为**名级**，非**内容级**。
4. 真幽灵之「三区名皆无」以**基名**判，未含**后缀式扁平化名**（如 `results___X`）之变体匹配。
5. 本件**未改任何既有件一字**、**未移动任何件**、**未落终判**。

---

**状态行**：`幽灵引用登记 · 58,957 处 · 可解析 50,684（重构所致）· 真幽灵 4,598（历史清单所列）· 只登记不改`
**落款**：主代理 mavis 亲编 · 2026-10-29 15:4x · ⛔0 回改既有件 · ⛔0 落五终判
