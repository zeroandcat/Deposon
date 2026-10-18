# V5 #21 锚版复算棒 · KT-B1 BOSS-B1/B2/B3 · worker · 2026-09-28

> **性质**：V4 #21（KT-B1 守恒审计 vs OT/KD/LLMLingua）执行棒；**0 判定**——判定归 verdict-keeper
> **上游**：`results/_v5_item21_asset_recovery_2026_09_28.md`（`6c80ff43bdd7`，锚版 3 件定位）
> **读数件**：`results/_v5_item21_anchor_recompute_2026_09_28.json`（本棒落盘）
> **0 LLM / 0 proxy / 0 gateway / 0 key 读取**

---

## §0 结论摘要（1 行）

**锚版 3 件在本棒登记的输入面上 0/3 可执行**——三件以完全相同的 `TypeError` 硬崩于 `_extract_200_questions`，**锚版读数 0 件产出**；漂移版 3/3 则逐位精确复现 09-27 值（`0.00044522183946429185` / `0.002813601952161043` / `0.46342184490589095`）。

---

## §1 锚版复算结果：0/3 可执行（硬崩，非数值差异）

三件**原样执行**（`python <锚版 .bak>`，CWD = `D:/私人资料/deposon-repo`），报错逐字一致：

| BOSS | 锚版 SHA-12 | 字节 | 崩溃行 | 报错 | 读数 |
|---|---|---|---|---|---|
| B1 Sinkhorn OT | `19325960b8be` | 14,956 | `boss_b1_sinkhorn_ot.py.bak:114` | `TypeError: float() argument must be a string or a real number, not 'NoneType'` | **无产出** |
| B2 KD | `1781ea2f742d` | 14,224 | `boss_b2_kd.py.bak:95` | 同上，逐字一致 | **无产出** |
| B3 LLMLingua | `c0b55e0385a4` | 13,966 | `boss_b3_llmlingua.py.bak:88` | 同上，逐字一致 | **无产出** |

崩溃点三件同构：`_extract_200_questions` 内 `"predicted": float(p.get("predicted", 0.0))`。

### §1.1 根因（机械事实，非归因主张）

v19 frozen 中 gsm8k 有 **12 条记录 `predicted` 键存在但值为 `null`**（`no_deposon` 6 条 + `v2_tunneling` 6 条）。`dict.get("predicted", 0.0)` 对「键存在、值为 `None`」返回的是 `None` 而**不是**默认值 `0.0`，随后的 `float(None)` 必抛 `TypeError`。

| condition | n | `predicted` 为 null | `predicted` 键缺失 |
|---|---|---|---|
| gsm8k/no_deposon | 100 | **6** | 0 |
| gsm8k/v1_blocking | 100 | 0 | 0 |
| gsm8k/v2_tunneling | 100 | **6** | 0 |
| gsm8k/unified | 100 | 0 | 0 |
| gsm8k/high_couple | 100 | 0 | 0 |
| strategyqa/全 5 臂 | 495 | 0 | **495**（改用 `pred`） |

**独立旁证（非我自证）**：09-27 `_v3_recheck_21_result_2026_09_27.json`（`354ae9c14fe2`）的 `face_3_d_dec.field_availability_audit` 已登记 `gsm8k/no_deposon` 与 `gsm8k/v2_tunneling` 的 `predicted.value_nonnull = 94`（= 100 − 6），与本棒实测 6 条 null **逐位吻合**。同一批 null 在漂移版由 `_norm_pred` 容错吃掉，在锚版无任何容错 ⇒ 崩。

### §1.2 第二层落差：即便补了 null 容错，锚版仍推不出漂移版读数

strategyqa 495 条的实测键集为 `id / is_correct / path / pred / trap_hit`——**没有 `predicted`、没有 `answer`、没有 `best_path`**。锚版无回退 ⇒ 这 495 条将静默取 `predicted=0.0`、`answer=0.0`、`best_path=[]`；漂移版则有三重回退 `p.get("pred", p.get("predicted", 0.0))` / `p.get("best_path", p.get("path", []))` / `_to_float`。

⇒ 机械登记：**锚版与漂移版不是可互推的两代**；漂移版读数不可由锚版推出。此项**超出派工单预期**（预判为「读数有差，差在字段抽取层」），实况为「锚版 0 读数」。

---

## §2 与 09-27 漂移版逐位比对

**比对结论：NOT_COMPARABLE。** 锚版读数为 `null`，逐位比对不成立——不是「读数有差」，而是「锚版跑不出读数」。

| BOSS | 锚版读数 | 漂移版读数（本棒实测） | 09-27 登记值 | 漂移版逐位比对 |
|---|---|---|---|---|
| B1 | `null`（崩溃） | `0.00044522183946429185` | `0.00044522183946429185` | **逐位一致** |
| B2 | `null`（崩溃） | `0.002813601952161043` | `0.002813601952161043` | **逐位一致** |
| B3 | `null`（崩溃） | `0.46342184490589095` | `0.46342184490589095` | **逐位一致** |

漂移版实测附加量（均为只读执行、0 字节改动）：

| 项 | 实测 |
|---|---|
| B1 漂移版 SHA-12 | `7c2b41c008a5`（16,404 B） |
| B1 实抽记录数 / 脚本声明 | **995** / `N_QUESTIONS=200`（沿用 09-27 已登记的口径差，0 归因） |
| B1 词表规模 | 30 |
| B1 选中 reg | 0.1 |
| B1 耗时 | **111.28 s** |
| B2 漂移版 SHA-12 / 耗时 | `8c6e98034005`（15,677 B）/ 0.39 s |
| B3 漂移版 SHA-12 / 耗时 | `2ded5cf0e863`（15,389 B）/ 0.44 s |

**归因层**：字段抽取层（已落实为「null 容错缺失」+「strategyqa 形态回退缺失」两层）；超参层沿用 `6c80ff43bdd7` §3 的 3/3 零差异结论，本棒未重测。

---

## §3 三腿输入面齐备核对（0 判定）

| 腿 | 需求 | 齐备/缺失 | 依据 |
|---|---|---|---|
| **(a)** 面 2 通用基线复现性 3/3 ±5% | 锚版 3 件读数 | ❌ **BLOCKED** | 锚版资产 ✅ 就位（3/3 SHA-12 本棒复核通过），但 **0/3 可执行** ⇒ 3/3 复现性**无从比较**；漂移版 3/3 精确复现，但 implementation 为漂移版 ≠ 锚版，不满足腿 (a) 的锚版要求 |
| **(b)** 面 3 非恒等 D_dec | v19 frozen 四字段抽取 | ✅ **READY_PRIOR** | 09-27 已落盘（`354ae9c14fe2`）；**不依赖本棒** |
| **(c)** 面 3 序稳定（3 seed × 10k resamples） | 同腿 (b) | ✅ **READY_PRIOR** | 09-27 已落盘；**不依赖本棒** |
| — | deposon 侧 D(M,T) | ❌ **结构性不可算** | 沿用 `6c80ff43bdd7` §4；本棒独立复核 `**/distortion_calculator.py` over `D:/私人资料` = **0 命中**，缺口**未解除**，**不因锚版回填而改变** |

**腿 (b)/(c) 输入面附带缺口（如实带过，0 掩盖）**：09-27 `field_availability_audit` 显示 `n_paths` / `n_filtered` 两字段在**全 10 个 condition 上 `key_hits` 均为 0**；strategyqa 的 `predicted` `key_hits` 亦全为 0（改用 `pred`）。本棒只读未重算、未改判。

**本棒不提出修复方案**：给锚版打 null 容错补丁、或为锚版另配输入面，均属改动受保护资产 / 变更冻结输入，需 PI 或 verdict-keeper 拍板后方可动。

---

## §4 只读与 0 触动声明

**锚版 3 件跑前/跑后哈希复验（逐件一致，0 触动）**：

| 文件 | 跑前 SHA-12 | 跑后 SHA-12 | 跑前/跑后字节 | 跑前/跑后 mtime |
|---|---|---|---|---|
| `boss_b1_sinkhorn_ot.py.bak` | `19325960b8be` | `19325960b8be` | 14,956 / 14,956 | 2026-09-09 11:55:40（未变） |
| `boss_b2_kd.py.bak` | `1781ea2f742d` | `1781ea2f742d` | 14,224 / 14,224 | 2026-09-09 11:55:40（未变） |
| `boss_b3_llmlingua.py.bak` | `c0b55e0385a4` | `c0b55e0385a4` | 13,966 / 13,966 | 2026-09-09 11:55:41（未变） |

- **输入面 0 触动**：`deposon_v19_benchmark_fixes.json` 跑前 = 跑后 = `910c4333eead`（409,104 B）。
- **锚版执行方式**：原样执行（`python <.bak>`）+ 显式 `SourceFileLoader`（Python 3.14 已移除 `load_module`）。**0 字节改动、0 复制入仓、0 重命名、0 删除**。
- **既有件 0 触动**：`_v3_recheck_21_result_2026_09_27.json`（`354ae9c14fe2`）、`_v3_recheck_21_rescript_2026_09_27.md`（`04f6ecd482b9`）均只读。
- **派生 JSON 0 合并**：读数 JSON 为独立新件。
- **驱动脚本**：`.tmp/_v5_item21_anchor_driver.py`、`.tmp/_probe21.py`（执行脚手架，非读数件）。
- **key**：0 明文密钥、0 key 读取、0 网络调用。

---

## §5 老实交代

- **锚版读数产出 = 0 件**。派工单要求的 B1/B2/B3 锚版读数**本棒未能提供**，原因是锚版在本登记输入面上跑不通，非我未执行。**0 编造读数、0 以漂移版读数冒充锚版读数**。
- **派工单「B1 约十余分钟量级」预估未成立**：锚版 B1 在 <1 s 内崩溃（无运行时长可测）；该量级实际对应漂移版 B1 单 `reg=0.1` 的 111.28 s。如实校正，不改派工单原文。
- **预期修正**：派工单预判差异形态为「读数差在字段抽取层」；实况为**锚版硬崩 + 形态回退缺失**，比预判更重，**未作淡化**。
- **本棒未做（越界或待拍板）**：未修改锚版任何字节以绕过崩溃；未新增/替换锚版的输入面；未对腿 (a)(b)(c) 给任何 PASS / FAIL / 不明结论。
- **skill 未加载**：本 Turn 工具集内无 skill 加载入口 ⇒ 派工单指定 skill **未加载到**；按纪律锚按派工单字面执行，**0 编造 skill 指令**。
- **succeeded ≠ 跑完**：完成宣告以本棒产物落盘核验（字节 + SHA-12）为准，值见汇报与本件 §6。

---

## §6 产物登记

| 件 | 字节 | SHA-12 |
|---|---|---|
| `results/_v5_item21_anchor_recompute_2026_09_28.json` | 9,527 | `47177cab0303` |
| `results/_v5_item21_anchor_recompute_2026_09_28.md` | 本件 | 自哈希，见汇报 |

（SHA-12 口径：`hashlib.sha256(...).hexdigest()[:12]`，小写。）

---

**给 verdict-keeper 的一句交接**：腿 (a) 的 3/3 复现性在本棒**无法裁**——不是数据缺失，而是锚版在登记输入面上不可执行；锚版「已回填」与锚版「可复算」是两件事，本棒只证实了前者。是否给锚版打兼容补丁 / 是否为锚版另配输入面，属资产改动，需 PI 拍板。

---

出件｜Mavis 团队 worker｜2026-09-28
