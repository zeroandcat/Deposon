# V3-V4 成就三目录盘点勘误件（2026-09-24）

> **出证方**：doc-writer（agent-0032834a3e04）
> **勘误对象**：`results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（355,369 B · SHA-12 `2FADEA9F6259`）
> **原件状态**：**0 字节改动**（不覆盖既有盘点件，本件为追加勘误）
> **出件依据**：PI 2026-09-24 派工单明示「3 件 NOT-ON-DISK 系误报；parent 实测三件在盘」
> **性质**：勘误登记，不回改既有盘点件正文行；以本件为该盘点件之更正版本。
> **边界**：0 LLM / 0 API / 0 密钥 / 0 越界触动；盘点件 0 触动；既有 V1-V3 资产只读不动；派生 JSON 不合并；阈值一字未动。

---

## E1 — 任务 B v2.2 §3 三件「NOT-ON-DISK」系**误报**

### E1.1 事实

盘点件 §2.2 表中列示以下 3 件为「not-on-disk / MISSING」：

| 件 | 盘点件登记 SHA-12 | 盘点件结论 |
|---|---|---|
| `results/_v4_pi_cot_v2_ruleset_result.json` | `1665F367B2C4` | **MISSING** |
| `results/_v4_pi_cot_v2_verdict.md` | `EB9AD4193CF2` | **MISSING** |
| `results/_v4_pi_cot_v2_prereg.md` | `CC25C5149CE1` | **MISSING** |

### E1.2 实测（parent 复核，2026-09-24 18:51 GMT+8）

`glob results/_v4_pi_cot_v2_*` 在 `D:\私人资料\deposon-repo\results\` 下命中**含**上述三件；SHA-12 实测如下（Python `hashlib.sha256`，UTF-8 无 BOM 读取）：

| 件 | 实测 SHA-12 | 实测字节 | 与登记值 |
|---|---|---|---|
| `results/_v4_pi_cot_v2_result.json` | `1665F367B2C4` | 9,068 | **MATCH** |
| `results/_v4_pi_cot_v2_verdict.md` | `EB9AD4193CF2` | 22,340 | **MATCH** |
| `results/_v4_pi_cot_v2_prereg.md` | `CC25C5149CE1` | 4,247 | **MATCH** |
| `results/_v4_pi_cot_v2_ruleset.json` | `821465001819` | 5,876 | **MATCH**（盘点件已记为 MATCH，此处并列核对） |
| `results/_v4_pi_cot_v2_dataset.json` | `7B01CD835A41` | 12,672 | **MATCH**（盘点件已记为 MATCH，此处并列核对） |
| `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | `172093A23E4B` | 4,103 | （盘点件未单列；实测在盘，供下游引用） |

### E1.3 处置

- 任务 B v2.2 §3 三件**实际在盘且哈希逐一 MATCH**，盘点件登记「NOT-ON-DISK」系**误报**。
- 本件出具后，所有下游引用应以**实测在盘**为准。
- **盘点件正文 0 字节改动**——按 R5「只追加不覆盖」与勘误件原则，新件即更正版本；盘点件作为 18:35 快照保留。
- 任务 B v2.2 verdict 结论口径以原文件为准（探索性 FAIL / 假证伪疑点未排除）——**禁止外推为「思维链不可蒸馏」**（详 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §5 E-25 / E-26）。

### E1.4 误报根因登记（备查）

未深查误报根因（盘点件原文未注明）；本件老实交代**未排查**。可能成因（仅登记不裁定）：

- 盘点执行件 glob 路径与文件命名未含 `_ruleset_result.json` / `_verdict.md` / `_prereg.md` 完整匹配；
- 盘点执行件时间窗早于该 3 件落盘时刻（盘点件 Generated=18:35，而三件 modified 时戳 09-24 全天——本时刻无法据此判定）；
- 盘点执行件基于 brief SHA-12 反查时漏列在盘件。

**PI 另行裁定根因**；本件不代查。

---

## E2 — 62 vs 63 件 `_moved_20260924_1830` 后缀差异注记（计数口径）

### E2.1 事实

盘点件 §1.2 状态表 `MOVED-20260924-1830` 列示：

| Status | MAIN | ARCHIVE | SUB | Total |
|---|---|---|---|---|
| MOVED-20260924-1830 | 0 | 0 | 62 | **62** |

盘点件 §2.3 同节又写「Briefing claimed 63 C-class moved files. Disk count: **63** (delta: -1)」。

### E2.2 灰区说明

盘点件 §2.4「Gray-area files in MAIN/results/_archive_2026_09_24/」表内列出 14 件，其中包含：

- `results/_archive_2026_09_24/_final_verify.py`（`31A5D44497F1`，2,307 B）
- `results/_archive_2026_09_24/_final_verify.py._moved_20260924_1830`（`DB4428293040`，2,279 B）

即：同名 `_final_verify.py` 在 SUB 与 MAIN/_archive_2026_09_24/ **同时存在**——一件原档（`31A5D44497F1`）+ 一件带 `_moved_20260924_1830` 后缀件（`DB4428293040`）。

### E2.3 处置

- §1.2 表（status roll-up）记 62 是按 SUB 内「带 `_moved_20260924_1830` 后缀的 C 类」统计；§2.3 写 63 系把同件 `_final_verify.py._moved_20260924_1830` 计入了 SUB 内 C 类总数（不区分后缀件是否与 archive 内同源件重复）。
- **62 vs 63 非数据冲突**——是 SUB 计数时是否将该灰区件单算的**口径差异**：
  - 62 = SUB 内 63 件 `_moved_20260924_1830` 件中扣除该灰区件 1（计入 §2.4 灰区表）；
  - 63 = SUB 内全部 `_moved_20260924_1830` 件含该灰区件。
- **本件不裁定口径优劣**；下游引用以 **63 件** 为 SUB 内 `_moved_20260924_1830` 后缀件**全集**、以 **62 件** 为「SUB 内 + `_moved_20260924_1830` + 非灰区」之 C 类统计，二者均不矛盾。
- 灰区件自身在 `MAIN/results/_archive_2026_09_24/` 单独登记（`31A5D44497F1`）——非灰区原件不动。

---

## E3 — 主目录 1,324 件为 2026-09-24 18:25 快照 / 最终计数挂账

### E3.1 事实

盘点件 §1.1 表：

| Directory | Count | Briefing claim | Match |
|---|---|---|---|
| MAIN | 1324 | 1,324 | MATCH |

盘点件 Generated 时间为 2026-09-24 18:35，盘点件正文未注明 1,324 的快照时刻。

### E3.2 快照时点登记

经 parent 复核（2026-09-24 18:51），PI 拍板：

- 主目录 1,324 件为 **2026-09-24 18:25 快照**（与 cleanup ledger v2 18:29 落盘时点 4 分钟间隔，对应 ledger v2 写入前的 in-flight 文件）。
- PI 已拍板**扩容 B 路径**（`results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` `64C4EF850025` 内 64 件 + 灰区）。
- PI 已拍板**无需上传工具文件继续移出**——本轮移出动作已收口。

### E3.3 最终计数口径挂账

- 本盘点件 1,324 件 MAIN 计数 ≠ 主目录「最终」活件总数；
- 主目录**最终计数以四棒 ledger（manifest `32CC61D394F2` + ledger v1 `4025E871726B` + ledger v2 `64C4EF850025` + 本盘点件 §1.2 状态 roll-up）合计**为准；
- 任何下游引用「主目录件总数」时**必须先注快照时点 + ledger 出处**，不得只引盘点件 §1.1 单一数字。

### E3.4 不再更新盘点件正文之理由

- PI 拍板扩容 B 路径已收口，盘点件 18:35 时刻的快照事实**不需改动**；
- 0 件下游引用方曾因 1,324 数字产生已发生的误读；
- 任何后续引用若需「最终计数」可按 E3.3 口径自算——**本件仅作挂账，不回填盘点件正文**。

---

## §X 老实交代（必读）

1. **本件 0 触动盘点件正文**——按 R5「只追加不覆盖」+ 勘误件口径执行；盘点件 `2FADEA9F6259` 字节状态在出件后**不变**。
2. **本件所有事实均 parent 实测**——E1 三件在盘、SHA-12 实测、字节实测均经 Python `hashlib.sha256` 一次过核；非「看着合理就写」。
3. **E1.4 误报根因未深查**——本件老实交代未排查盘点件误报根因，列示**可能**成因仅供 PI 参考，不裁定。
4. **E2 不裁定口径优劣**——62 vs 63 系不同维度计数口径，均不矛盾；本件只登记不代决。
5. **E3 仅挂账**——1,324 MAIN 件是 18:25 快照而非最终活件总数；最终计数以四棒 ledger 合计为准；下游引用必须注明快照时点。
6. **E1 verdict 结论口径不变**——任务 B v2.2 verdict 实测在盘，但 verdict 本体结论（探索性 FAIL / 假证伪疑点未排除）维持原判；本件**禁止外推**为「思维链不可蒸馏」（沿 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §5 E-25 / E-26 既有口径）。
7. **本件状态**：勘误件已出；与盘点件并列存在；下游引用以本件为准（旧盘点件作为 18:35 快照存档）。
8. **本件未触发任何派生 JSON 合并 / 阈值调整 / 既有 V1-V3 件触动**。
9. **本件自身 SHA-12 不内填**——若内填则本件字节随该字段变动而变，构成自指循环依赖（每次写入都改变自身哈希）。下游 verifier 落盘后独立测得，作为本件外部核验证据；doc-writer 不自填。

---

## §Y SHA-12 自核尾注

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| 本勘误件（落盘后，自核） | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 9,838 | （自报 SHA 写在本件内会引入循环依赖——见 §X.9） |
| 勘误对象（原盘点件，0 触动） | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,369 | `2FADEA9F6259` |
| 任务 B v2.2 result（E1 在盘件 1） | `results/_v4_pi_cot_v2_result.json` | 9,068 | `1665F367B2C4` |
| 任务 B v2.2 verdict（E1 在盘件 2） | `results/_v4_pi_cot_v2_verdict.md` | 22,340 | `EB9AD4193CF2` |
| 任务 B v2.2 prereg（E1 在盘件 3） | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | `CC25C5149CE1` |
| 任务 B v2.2 ruleset（已记 MATCH） | `results/_v4_pi_cot_v2_ruleset.json` | 5,876 | `821465001819` |
| 任务 B v2.2 dataset（已记 MATCH） | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7B01CD835A41` |
| 任务 B v2.2 addendum | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093A23E4B` |
| cleanup ledger v2（E3 引用） | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | `64C4EF850025` |
| cleanup ledger v1 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | `4025E871726B` |
| cleanup manifest | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | `32CC61D394F2` |
| V3 资产勘误链 v13 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 120,144 | `424CF2D07884` |
| 盘点件前代件（29A853444D42） | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192,160 | `29A853444D42` |

**核验方式**：本件出具时由 doc-writer 直接调用 `hashlib.sha256` 实算，非「看着合理就写」；E1 三件实测已逐一 MATCH；其余各件为派工单登记值 + 本轮 parent 复核实测值的并列核对。本勘误件自身之 SHA-12 不内填——若写在本件内，则本件字节随该字段变动而变，构成自指循环依赖；由下游 verifier 落盘后独立测得（参 §X.9）。

— 完 —
