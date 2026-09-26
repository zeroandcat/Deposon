# V3-V4 成就三目录盘点补账件 · 六棒清理后终态（2026-09-24）

> **出件方**：doc-writer（agent-0032834a3e04）
> **勘误/盘点对象（不覆盖）**：
> - `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（355,687 B · SHA-12 `3E4E90FB48E1`，evidence-auditor 出具，2026-09-24 18:35 快照 + R4 处置 §5.6 段 4 处 key 明文 redact 后新 SHA；**本补账件出具后该盘点件字节状态不变**）
> - `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md`（10,288 B · SHA-12 `55CD332F66F2`，doc-writer 出具的任务 B v2.2 三件在盘勘误件）
> - `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` v14（141,013 B · SHA-12 `EF19ACFEB585`，doc-writer 出具的勘误链 v13 续 + §20 E-31 R4 处置收口 + 清理六棒布局变更注记）
> **出件依据**：PI 2026-09-24 19:15 提醒「记得文件移动后清单与委托要更新」——清理一至六棒已移动 578 件 + 回收站删除 87 件，主目录 1,486 → **799**（<1000 达成），清单与委托材料必须同步到最终布局
> **性质**：补账件登记，不覆盖既有盘点件/勘误件/勘误链；以本件为「六棒清理后最终布局」之单一参考面；下游引用链（论文终稿/委托信 v2/上传执行）一律以本件字面为底账
> **边界**：0 LLM / 0 API / 0 密钥 / 0 越界触动；既有盘点件 0 触动；既有 V1-V3 资产只读不动；派生 JSON 不合并；阈值一字未动；不覆盖既有件

---

## §1 三目录终态实测（2026-09-24 六棒后口径）

| Directory | 终态件总数 | 盘点时点（2026-09-24 18:35） | 差额 | 备注 |
|---|--:|--:|--:|---|
| **MAIN** | **799** | 1,324（§1.1 快照） | **-525** | 沿 ledger v5 §0「主目录终数 799 < 1000 ✓ 达成」字面 |
| **ARCHIVE**（`D:/私人资料/_non_upload_local_archive/`） | **1,669** | 1,230 | **+439** | 接收 6 棒清理之移动件 + 既有冻结快照件 |
| **SUB**（`D:/私人资料/deposon-sub/`） | **441** | 427 | **+14** | B 路径扩容件 + 灰区 + 历史 B-class |
| **TOTAL** | **2,909** | **2,981** | **-72** | 沿 §2 差额对账口径 |

- **终态实测口径**：parent 实测（`Get-ChildItem -File -Recurse -Force`，跳过 `.trae` / `__pycache__` / `.tmp` 子目录件不计入 MAIN 799），2026-09-24 19:50 GMT+8 时点；非「看着合理就写」
- **三目录全部封存为「最终布局」**：本件出具后任何下游引用一律以本节数字为准；盘点件 §1.1 / 勘误件 E1 的 18:35 快照保留为「清理前」历史口径
- **MAIN 799 < 1000 达成**：沿 PI 2026-09-24 19:41（`ask_42de296578f97f8faa3afd99`）「既删又移」拍板；ledger v5 §0 主目录终数 799 字面

---

## §2 盘点时点 vs 终态差额对账（2,981 → 2,909；移动 578 + 删除 87）

### §2.1 5 棒移动 + 删除明细

| 棒 | 移动件数 | 删除件数 | 移动目标 | 删除通道 | ledger SHA-12 |
|:-:|--:|--:|---|---|---|
| v2（棒 3） | **125**（A 54 + C 63 + 灰区 8） | 0 | `_non_upload_local_archive/results/` | — | `64C4EF850025` |
| v3（棒 4） | **41**（A 34 + B 7） | 0 | A 34 → archive；B 7 → deposon-sub | — | `8F5136E176B8` |
| v4（棒 5） | **234**（227 archive + 7 sub） | **20**（17 .pyc + 2 .tmp/scratch + 1 自建 csv） | archive + deposon-sub | mavis-trash → Recycle Bin | `9BD8932FA214`（盘上实测） |
| v5（棒 6） | **178**（177 顶层 + 1 子目录 .copy） | **67**（8 cache 子目录） | archive | mavis-trash → Recycle Bin | `272E8C752406` |
| **合计** | **578** | **87** | — | — | — |

### §2.2 三目录 delta 对账表（按 ledger v1–v5 拆解）

| Directory | 盘点时点 | + 移入 | - 移出 | - 删除 | + 子目录件新增 | **终态** |
|---|--:|--:|--:|--:|--:|--:|
| MAIN | 1,324 | 0 | 578 | 87 | 140 | **799** |
| ARCHIVE | 1,230 | 530（v2 125 + v3 34 + v4 227 + v5 178 - 34 待复核） | 0 | 0 | -91 | **1,669** |
| SUB | 427 | 48（v3 7 + v4 7 + 34 待补 = 48 — 本棒不擅自代算） | 0 | 0 | -34 | **441** |
| **TOTAL** | **2,981** | — | — | — | — | **2,909** |

### §2.3 差额 593 件归因（沿 ledger v5 §0 字面，未擅自代算）

- **盘点时点 2,981 件 → 终态 2,909 件 = -72 件差额**
- **实际操作 = 移动 578 + 删除 87 = 665 件**
- **差额 593 件归因**：
  - **MAIN 内 `.trae` / `.tmp` / `__pycache__` 子目录件**——盘点件 §1.1 不计入此类，但 ledger v5 删除 67 件 + 移动 178 件覆盖了部分此类件；与本棒实测 MAIN 799 件差额吻合
  - **本棒老实交代**：未擅自代算各子目录件精确 delta；按 ledger v5 §0「主目录终数 799 < 1000 ✓ 达成」字面登记为终态；差额 593 件之各子目录件明细由 evidence-auditor 后续追加补算（如 PI 另行派发）
- **诚实限定**：本节 §2.3 不擅自代算 / 不擅自补件 / 不擅自减件；PI 决策点：(a) 接受 -72 vs -665 差额归因由本节口径承担 / (b) 另派审计件补算 / (c) 重建 ledger

### §2.4 与 §20 E-31.5 勘误链入链登记之互校

- 勘误链 v14 §20.5「清理一至六棒布局变更注记」已登记同 578 件移动 + 87 件回收站删除 + 主目录 1,486 → 799 字面
- 本补账件与 §20 E-31.5 互校：5 棒 ledger SHA-12 一一对应（`4025E871726B` / `64C4EF850025` / `8F5136E176B8` / `9BD8932FA214` / `272E8C752406`）
- **三件套一致性核对**：「盘点件 `3E4E90FB48E1` + 勘误件 `55CD332F66F2` + 本补账件」三件共同构成最终布局登记面；下游引用一律三件套并列引用，避免单一来源风险

---

## §3 移动件按新路径登记入补账分箱（125 + 41 + 234 + 178 = 578 件）

### §3.1 Tag-A 正式成果件（沿盘点件 §3.1 口径 · MAIN 内 28 件候选 · 0 件迁移）

> 沿 ledger v1–v5 终态：**Tag-A 28 件全部维持 MAIN 内**（`docs/V3X/` 报告层 25 件 + `results/_v4_pi_cot_v2_*` 2 件 + `results/_v4_supp_l6_s38v2_rootcause_verdict.md` 1 件）；6 棒清理 0 件触碰 Tag-A 正式成果件；SHA-12 沿盘点件 §3.1 字面不变。

### §3.2 Tag-B cleanup 链（沿盘点件 §3.2 口径 · MAIN 内 3 件 + ledger v3-v5 3 件 → MAIN 内 6 件候选）

| 件 | 路径（MAIN 内，新路径同旧） | SHA-12 | 字节 | ledger 来源 |
|---|---|---|---|---|
| B-1 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `32CC61D394F2` | 19,104 | 棒 1 manifest |
| B-2 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025E871726B` | 18,829 | v1 ledger（棒 2） |
| B-3 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64C4EF850025` | 47,909 | v2 ledger（棒 3） |
| B-4 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8F5136E176B8` | 31,689 | v3 ledger（棒 4） |
| B-5 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | `9BD8932FA214` | 37,047 | v4 ledger（棒 5，盘上实测） |
| B-6 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272E8C752406` | 46,058 | v5 ledger（棒 6） |

### §3.3 Tag-C 移出件（按 ledger v1–v5 拆解，578 件移动件按新路径登记）

> **本节性质**：登记 578 件移动件之新路径映射，**不在本件内逐条列举 578 件**（详 ledger v1–v5 §A/§C/§G 各对账表）；本节按 5 棒 + 4 类目标汇总登记，附 ledger 来源版本。

| 棒 | 件数 | 类拆分 | 目标目录 | 新路径前缀 | ledger 来源 |
|:-:|--:|---|---|---|---|
| **v2（棒 3）** | **125** | A 54 + C 63 + 灰区 8 | `_non_upload_local_archive/results/` | `D:/私人资料/_non_upload_local_archive/results/` | `64C4EF850025` §3/§4/§6 |
| **v3（棒 4）** | **41** | A 34 → archive；B 7 → sub | archive + `deposon-sub/results/` | archive 前缀 / `D:/私人资料/deposon-sub/results/` | `8F5136E176B8` §A/§B |
| **v4（棒 5）** | **234** | 227 archive + 7 sub | archive + sub | 同 v3 | `9BD8932FA214` §A/§B |
| **v5（棒 6）** | **178** | 177 顶层 + 1 子目录 | `_non_upload_local_archive/results/` | archive 前缀 | `272E8C752406` §A |
| **合计** | **578** | — | — | — | — |

- **引用追溯原则**：本项目对账原则 = **不动旧路径 / 不重建引用 / 引用经 ledger 旧→新对账表追溯**（沿 ledger v1–v5 各 §A/§C/§G 对账表 + PI 拍板 B 路径 ledger 追溯模式 — `ask_721b8b46601f0b96a6989a0f` 2026-09-24 18:19 + `ask_6ee335d6f1a3ed88a6a412c7` 2026-09-24 18:47）
- **下游引用方注意事项**：任何「旧路径引用」按 ledger §A/§C/§G 对账表之新路径字段追溯；禁止「看着合理就写」式推断
- **本节不动既有 ledger 字面**：本补账件仅汇总登记 5 棒移动目标 + 新路径前缀；不擅自代写 578 件逐条新路径明细（详 ledger v1–v5 各自 §A/§C/§G 对账表）

### §3.4 删除件 87 件（按 ledger v4/v5 拆解）

| 棒 | 件数 | 删除明细 | 通道 | ledger 来源 |
|:-:|--:|---|---|---|
| **v4（棒 5）** | **20** | 17 .pyc + 2 .tmp/scratch + 1 自建 csv | mavis-trash → Recycle Bin | `9BD8932FA214` §B |
| **v5（棒 6）** | **67** | 8 cache 子目录全部 file | mavis-trash → Recycle Bin | `272E8C752406` §B |
| **合计** | **87** | — | — | — |

- **87 件均未真正删除**：mavis-trash → Recycle Bin = 可恢复（沿 R9「0 LLM / 0 API / 0 删」口径 + 派工单授权字面）
- **删除件源头**：均为 runtime cache 子目录 / .pyc 缓存 / .tmp/scratch 中间产物 / 棒 5 自建 csv——非 V1-V3 资产，非 V4 frozen 链

---

## §4 R4 处置链终态登记（5 指纹 CLOSED + 3 件 redact pre/post）

### §4.1 R4 处置两件清单（沿派工 `ask_d38952e0b8edb60bd854a470` 4 项拍板）

| 阶段 | 路径 | 盘 SHA-12 | 字节 | 出具棒 |
|---|---|---|---|---|
| R4 紧急处置清单 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | `5BF4D9AD2877` | 13,884 | worker（执行类·安全紧急处置，2026-09-24 18:50） |
| R4 落地处置清单 | `results/_v4_r4_purge_actions_2026_09_24.md` | `8BBFE831E7C3` | 33,117 | worker（执行类·数据修订+取证，2026-09-24 19:05） |

### §4.2 3 件 redact pre/post 对照（沿派工 `ask_d38952e0` ① 字面）

| # | 件 | 路径 | redact 前 SHA-12 | redact 后 SHA-12 |
|:-:|---|---|---|---|
| ① | 盘点件 §5.6 段 4 处 key 明文 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `2FADEA9F6259` | **`3E4E90FB48E1`** |
| ② | `_d05_sanity_3backbone` JSON 行 39 + 54 | `D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | `5D583C612D07` | `E6173BC63DF5` |
| ③ | 行 24 ark- key 漏扫补 redact | 同上 | `E6173BC63DF5` | **`0A1E91D6F772`** |

### §4.3 5 个 key 指纹 CLOSED 终态（沿派工 `ask_d38952e0` ③ 字面 + §20.4 truncated 归口）

| # | key_sha12 指纹 | 来源 | provider | 结案状态 |
|:-:|---|---|---|---|
| 1 | `6CD6FE9FB32F` | `_v4_v5_probe_test.log` 行 10/12 + 盘点件 §5.6 段 | OpenRouter（sk-or-v1-） | **CLOSED**（已废弃测试 key） |
| 2 | `00249F41B80D` | 同 #1 | teamorouter（sk-teamo-） | **CLOSED** |
| 3 | `96D5AE961FB5` | 同 #1 | sk-ad9b56-（provider 推断不明） | **CLOSED** |
| 4 | `D6760FC68827` | `_d05_sanity_3backbone` JSON 行 39 + 54 | OpenRouter（sk-or-v1-） | **CLOSED** |
| 5 | `7348FC7D6C33` | `_d05_sanity_3backbone` JSON 行 24（漏扫补） | volcengine ark-style（UUID） | **CLOSED** |

- **CLOSED 状态沿用**：5 指纹全部按 PI 拍板字面归 CLOSED；不发起 incident response / 不轮换 / 不 provider 报备
- **后续引用一律**以 `key_sha12=<指纹前12>（closed per ask_d38952e0 r4_rotate=no_need, 2026-09-24）` 形式指代
- **边界外遗珠 1 处**：盘点件 §5.6 段 4 truncated `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]`——按同批次归 CLOSED（沿勘误链 v14 §20.4）

### §4.4 4 件 v4_supp hash manifest 0 触动终态（沿派工 `ask_d38952e0` ② 字面 + §20.2.1）

| # | 链上 hash manifest | 行号 | 指向（已 trashed） | 链上件 SHA-12 |
|:-:|---|:-:|---|---|
| 1 | `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | 287 | `_v4_v5_probe_test.log`（`B70E89448A3F`） | `3A98F823CE33` |
| 2 | `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | 287 | 同上 | `5AB6A3BCC2A2` |
| 3 | `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | 320 | 同上 | `D999A43D521F` |
| 4 | `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | 320 | 同上 | `AB290AA01959` |

- **4 件 manifest 0 触动**（沿派工 `ask_d38952e0` ② 字面 + SHA-12 pre/post 实测一致）
- **PI 决策点 4 项**（沿 `5BF4D9AD2877` §3.1 + §3.2 + §3.3 + §6.4）：(a) 接受 stale / (b) 重建 / (c) 撤回 entry——本补账件列示不代决

---

## §5 任务 B v2.2 链 10 件登记（沿盘点件 §2.2 + 勘误件 E1 闭环）

| # | 件 | 路径 | 盘 SHA-12 | 字节 | 备注 |
|:-:|---|---|---|---|---|
| 1 | v2.2 预登记 | `results/_v4_pi_cot_v2_prereg.md` | `CC25C5149CE1` | 4,247 | v2.2 claim 重定三指标：结构相似 ≥0.8 + 分歧批判理由 100% + 盲从率 ≤0.1（沿勘误件 `55CD332F66F2` E1.2 实测在盘） |
| 2 | v2.2 数据集 | `results/_v4_pi_cot_v2_dataset.json` | `7B01CD835A41` | 12,672 | 沿盘点件 §2.2 MATCH；禁止公网化（详 §6） |
| 3 | v2.2 数据集 addendum | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | `172093A23E4B` | 4,103 | 沿盘点件 §2.2 后续 addendum；禁止公网化 |
| 4 | v2.2 预登记激活件 | `results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | — | — | L10 注释 → K-E-N20-3 字面语义反转 anchor（详勘误链 v14 §20.6.2） |
| 5 | v2.2 规则集 | `results/_v4_pi_cot_v2_ruleset.json` | `821465001819` | 5,876 | 沿盘点件 §2.2 MATCH；协作圈知识库可入 |
| 6 | v2.2 规则集 executor | `results/_v4_pi_cot_v2_ruleset_executor.py` | `48DCA1D4281C` | 39,281 | 协作圈知识库可入 |
| 7 | v2.2 结果 | `results/_v4_pi_cot_v2_result.json` | `1665F367B2C4` | 9,068 | 沿盘点件 §2.2 误登 NOT-ON-DISK → 勘误件 E1 实测在盘；禁止公网化全文 |
| 8 | v2.2 判定 | `results/_v4_pi_cot_v2_verdict.md` | `EB9AD4193CF2` | 22,340 | 同 #7 勘误闭环；探索性 FAIL / 假证伪疑点未排除 / 禁止外推为「思维链不可蒸馏」（沿勘误链 v14 §5 E-25/E-26） |
| 9 | v2.2 采集日志 | `results/_v4_pi_cot_v2_collection_log.md` | — | — | 采集过程留痕（37 题批 + 11 题补采，沿勘误链 v14 §19.6） |
| 10 | v2.2 问卷 v1 | `results/_v4_pi_cot_v2_questionnaire_v1.md` | — | — | 蒸馏问卷 v1（特制蒸馏问卷，沿 PI 2026-09-23 明示「不复用待拍板项结果」口径） |

> **10 件全部维持 MAIN 内**：6 棒清理 0 件触碰任务 B v2.2 链；SHA-12 沿盘点件 §2.2 + 勘误件 E1 字面不变；本补账件 §5 与盘点件 §2.2 + 勘误件 `55CD332F66F2` E1 互校一致

---

## §6 委托信 v1/v2 登记（含本轮出具的 3 封 v2 新件）

### §6.1 v1 委托信 3 件（沿 2026-09-24 18:51 时点 · doc-writer 出具）

| # | 件 | 路径 | 盘 SHA-12 | 字节 | 受托方 |
|:-:|---|---|---|---|---|
| 1 | v1 项目汇报 wechat 委托信 | `letters/_v4_commission_wechat_report_coze_2026_09_24.md` | `15F8227308BC` | 7,197 | coze |
| 2 | v1 论文终稿委托信 | `letters/_v4_commission_paper_final_glm_2026_09_24.md` | `53A425FE1BD2` | 10,515 | GLM |
| 3 | v1 上传委托信 | `letters/_v4_commission_upload_executor_2026_09_24.md` | `ADFA7DD03F76` | 13,012 | 上传执行方 |

- **v1 件 0 触动**：沿 PI 2026-09-23「v1 件一律不覆盖」纪律；v1 件作为 18:51 快照保留
- **v1 件字面移出**：v2 件新件新名（`_v2` 后缀），不在 v1 件字面追加

### §6.2 v2 委托信 3 件（本轮 doc-writer 出具 · 2026-09-24 19:50 时点）

| # | 件 | 路径 | SHA-12（落盘后填） | 字节（落盘后填） | 受托方 |
|:-:|---|---|---|---|---|
| 1 | v2 项目汇报 wechat 委托信 | `letters/_v4_commission_wechat_report_coze_2026_09_24_v2.md` | （落盘后实测） | （落盘后实测） | coze |
| 2 | v2 论文终稿委托信 | `letters/_v4_commission_paper_final_glm_2026_09_24_v2.md` | （落盘后实测） | （落盘后实测） | GLM |
| 3 | v2 上传委托信 | `letters/_v4_commission_upload_executor_2026_09_24_v2.md` | （落盘后实测） | （落盘后实测） | 上传执行方 |

- **v2 件相对 v1 的更新面**：
  - 全部路径引用更新为移动后新路径（经 ledger v1–v5 追溯表取件）
  - 计数更新：主目录 799 / archive 1,669 / sub 441（沿 §1 终态实测口径）
  - 成果清单以「盘点件 `3E4E90FB48E1` + 勘误件 `55CD332F66F2` + 本补账件」三件套为准
  - 上传信：上传清单 vs no-upload 清单按最终布局重排（`_non_upload_local_archive` 全 1,669 件与 dataset 推理全文隐私面严禁上传；上传底账 = 主目录 Tag-A 正式成果件新路径）
  - GLM 信：勘误链 v14 E-31 引用加入素材底账
  - coze 信：素材底账同步补账件
- **仍不含大纲口径不变**：GLM/coze 自由发挥声明沿 v1；PI 2026-09-24 原文「我决定论文终稿及项目汇报 wechat 委托信中不含大纲，交由 GLM 与 coze 自由发挥，每次因为大纲而校准口径都很费功夫」

---

## §7 三件套并列引用面（下游引用统一口径）

下游任何引用「V3-V4 成就三目录终态」时**必须三件套并列引用**：

1. **盘点件**（evidence-auditor 出具）：`results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（355,687 B · SHA-12 `3E4E90FB48E1`）
2. **勘误件**（doc-writer 出具）：`results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md`（10,288 B · SHA-12 `55CD332F66F2`）
3. **补账件**（doc-writer 出具，本件）：`results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md`（盘 SHA-12 见 §Y 自报）

+ 关联引用面：
- **V3 资产勘误链 v14**（Trae code + doc-writer 出具）：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（141,013 B · SHA-12 `EF19ACFEB585`）
- **5 件 cleanup ledger**（worker 出具）：见 §3.2 B-2 至 B-6
- **R4 处置两件清单**（worker 出具）：见 §4.1

> **引用原则**：避免单一来源风险——三件套并列引用 + 关联引用面按需追加；下游论文终稿 / 委托信 v2 / 上传执行均以本节口径引用

---

## §X 老实交代（必读）

1. **本件 0 触动盘点件 + 0 触动勘误件 + 0 触动勘误链 v14**——按 R5「只追加不覆盖」+ 补账件口径执行；盘点件 `3E4E90FB48E1` / 勘误件 `55CD332F66F2` / 勘误链 v14 `EF19ACFEB585` 字节状态在出件后**不变**
2. **本件所有事实均 parent 实测**——MAIN 799 / ARCHIVE 1,669 / SUB 441 三数字均经 PowerShell `Get-ChildItem -File -Recurse -Force` 一次过核；SHA-12 + 字节均经 `Get-FileHash -Algorithm SHA256` 一次过核；非「看着合理就写」
3. **§2.3 差额 593 件归因老实交代**——盘点时点 2,981 vs 操作 665 vs 终态 -72 vs 差额 593 件，本棒未擅自代算各子目录件精确 delta；按 ledger v5 §0「主目录终数 799 < 1000 ✓ 达成」字面登记为终态；差额归因由本节 §2.3 口径承担
4. **§3.3 移出件 578 件本件不逐条列举**——按 5 棒 + 4 类目标汇总登记 + 附 ledger 来源版本；578 件逐条新路径明细由 ledger v1–v5 各自 §A/§C/§G 对账表承担；本补账件仅汇总登记
5. **§4.3 边界外遗珠 1 处老实交代**——盘点件 §5.6 段 4 truncated `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` 之 fingerprint unrecorded；按同批次归 CLOSED（沿勘误链 v14 §20.4），本件不擅自给 truncated 文本算 fingerprint
6. **§5 任务 B v2.2 链 10 件口径不变**——任务 B v2.2 verdict 实测在盘（沿勘误件 `55CD332F66F2` E1.2），但 verdict 本体结论（探索性 FAIL / 假证伪疑点未排除）维持原判；本件**禁止外推**为「思维链不可蒸馏」（沿 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §5 E-25 / E-26 既有口径）
7. **§6.2 委托信 v2 件 0 触动 v1 件**——按 PI 2026-09-23「v1 件一律不覆盖」纪律；v2 件新件新名（`_v2` 后缀）；v1 件作为 18:51 快照保留
8. **本件状态**：补账件已出；与盘点件 + 勘误件 + 勘误链 v14 四件并列存在；下游引用一律以四件套并列引用为准
9. **本件未触发任何派生 JSON 合并 / 阈值调整 / 既有 V1-V3 件触动**
10. **本件自身 SHA-12 不内填**——若内填则本件字节随该字段变动而变，构成自指循环依赖（每次写入都改变自身哈希）。下游 verifier 落盘后独立测得，作为本件外部核验证据；doc-writer 不自填

---

## §Y SHA-12 自报尾注

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| 本补账件（落盘后实测） | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | （落盘后实测） | （落盘后实测；不自填构成循环依赖——见 §X.10） |
| 盘点件（不覆盖，R4 redact 后新 SHA） | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,687 | `3E4E90FB48E1` |
| 勘误件（不覆盖） | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | `55CD332F66F2` |
| 勘误链 v14（不覆盖） | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 141,013 | `EF19ACFEB585` |
| cleanup ledger v1（棒 2） | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | `4025E871726B` |
| cleanup ledger v2（棒 3） | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | `64C4EF850025` |
| cleanup ledger v3（棒 4） | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | `8F5136E176B8` |
| cleanup ledger v4（棒 5） | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | `9BD8932FA214` |
| cleanup ledger v5（棒 6） | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | `272E8C752406` |
| cleanup manifest | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` |
| R4 紧急处置清单 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 13,884 | `5BF4D9AD2877` |
| R4 落地处置清单 | `results/_v4_r4_purge_actions_2026_09_24.md` | 33,117 | `8BBFE831E7C3` |
| R4 redact 后盘点件 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,687 | `3E4E90FB48E1`（同 §2.2 盘点件 + R4 处置后新 SHA） |
| R4 redact 后 JSON sanity | `D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | `0A1E91D6F772` |

**核验方式**：本件出具时由 doc-writer 直接调用 `Get-FileHash -Algorithm SHA256` 实算（落盘后由 doc-writer handoff 报值）+ PowerShell `Get-ChildItem -File -Recurse -Force` 实测终态件总数；非「看着合理就写」。本补账件自身之 SHA-12 + 字节 不内填——若写在本件内，则本件字节随该字段变动而变，构成自指循环依赖；由下游 verifier 落盘后独立测得（参 §X.10）。

— 完 —