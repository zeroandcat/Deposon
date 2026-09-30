# V5 #21 资产回填棒 · KT-B1 锚版 3 件多路定位 · worker · 2026-09-28

> **性质**：V4 #21（KT-B1 守恒审计 vs OT/KD/LLMLingua）备料棒；**0 判定**——判定归 verdict-keeper
> **上游输入（只读，0 触动）**：`results/_v3_recheck_21_result_2026_09_27.json`（`26c0d0b0ffb6` 系件登记的锚版 SHA-12 三值）、`results/_v3_recheck_21_rescript_2026_09_27.md`
> **产出件**：`results/_v5_item21_asset_recovery_2026_09_28.md`（本件，1 件登记）
> **0 LLM / 0 proxy / 0 key 读取**；只读检索，命中资产 0 触动 0 移动 0 复制入仓

---

## §0 结论摘要（1 行）

**锚版 3 件全部找到**（此前记「全仓 0 命中」为**检索方法假阴性**，非实体不存在）：3 件以 `.bak` 后缀与漂移版同目录并存，已逐件哈希实测命中锚版 SHA-12。

---

## §1 锚版 3 件定位结果（哈希实测）

**位置**：与漂移版**同目录、同 basename 的 `.bak` 兄弟文件**
`D:\私人资料\_non_upload_local_archive\scripts\scripts\kt_b1\`

| BOSS | 锚版 SHA-12（实测） | 字节 | 锚版路径 | mtime |
|---|---|---|---|---|
| B1 Sinkhorn OT | **`19325960b8be`** | 14,956 B | `scripts/scripts/kt_b1/boss_b1_sinkhorn_ot.py.bak` | 2026-09-09 11:55:40 |
| B2 KD | **`1781ea2f742d`** | 14,224 B | `scripts/scripts/kt_b1/boss_b2_kd.py.bak` | 2026-09-09 11:55:40 |
| B3 LLMLingua | **`c0b55e0385a4`** | 13,966 B | `scripts/scripts/kt_b1/boss_b3_llmlingua.py.bak` | 2026-09-09 11:55:41 |

**独立旁证（0 依赖我的实测）**：`results/_archive_manifest_non_upload_v2_2026_09_28.json` 第 7327/7337/7347 行已按 `path`+`size`+`sha12` 三字段登记同 3 件，与本件实测逐字一致（14,956 / 14,224 / 13,966 B）。

**唯一性实测**：全 3 扫描根逐文件 SHA-256 全扫（**3,338 件**），3 个锚版 SHA-12 各命中 **1 份**，无副本、无第二份锚版。

### §1.1 前次「全仓 0 命中」的根因（机械事实，登记）

- 前次检索式按 `*.py` 后缀/文件名匹配 ⇒ **`.bak` 后缀件不在检索面内** ⇒ 报「0 命中」。
- 锚版与漂移版是**同目录相邻两代**：锚版 `.bak` mtime `2026-09-09 11:55:40`，漂移版 `.py` mtime `2026-09-10 10:04:29`。
- ⇒ **哈希未命中 ≠ 实体不存在**（记忆纪律在本例得到实证支持）。

---

## §2 检索证据面（3 路 × 3 扫描根）

**扫描根显式声明**：`deposon-repo`、`deposon-sub`、`_non_upload_local_archive`（`deposon-repo/deposon-sub` 与 `D:/私人资料/Downloads` **不存在**，已实测登记）。

| 路 | 检索式 | 命中数 | 命中物 |
|---|---|---|---|
| ① 文件名 glob | `*_v3_recheck_21*` / `*recheck_21*` | 2 | 09-27 改判件本体（供锚版 SHA-12 取值源） |
| | `*KT_B1*` | 0 | 仓内命名为下划线式 |
| | `*KT_B1*`（下划线 `KT_B1`） | 24 | spec / rework report / kill_line / 仓外 PHASE_B_TMP / Trae 快照 |
| | `*anchor*` | 23 | 含 `KT_ABC1_anchors_sha256_12.json` 系 |
| ② 历史登记路径字面 | 锚版 SHA-12 三值全仓 grep | **25 文件** | 含 `_archive_manifest_non_upload_v2_2026_09_28.json`（**含 `.bak` 三行登记**） |
| ③ 内容特征 | 路径含 `kt_b1|boss_b1|boss_b2|boss_b3|sinkhorn|llmlingua|distortion_calc` | 38 | **命中 3 件 `.bak` 锚版** |

**③ 的扩展面（0 命中项，如实登记）**：`distortion_calculator.py` 按名全扫 **0 命中**；`tools/` 目录实存（deposon-repo 5 件 / _non_upload_local_archive 20 件）但**不含**该文件 ⇒ deposon 侧 D(M,T) 资产缺口**本棒未解除**。

---

## §3 锚版 vs 漂移版差异面（机械登记，0 归因）

**常量/超参层：3/3 完全一致**（逐常量行比对）——阈值 `0.95`/`0.95`/`0.05`、`reg=0.1`、`T=2.0`、`alpha=0.5`、`lr=1e-3`、`epochs=50`、`batch=32`、压缩比 `0.5`、`SEED_LOCK=42`、`N_NODES/N_QUESTIONS=200` 全部逐字相同。

**差异层：收敛于预测字段抽取（唯一差异面）**

| 项 | 锚版（`.bak`） | 漂移版（`.py`） |
|---|---|---|
| 字段名 | `p.get("predicted", 0.0)` | `p.get("pred", p.get("predicted", 0.0))` |
| 归一函数 | 无 | 新增 `_norm_pred(v)` / `_to_float(v)`（None→0.0、bool→1/0、yes/no/true/false→1/0、字符串浮点强转） |
| B2 权重 | `max(0.0, abs(q.get("predicted", 0.0))) + 1.0` | `max(0.0, abs(q.get("pred", 0.0))) + 1.0` |
| B3 prompt 串 | `predicted=` / 正则 `r"predicted=(...)"` | `pred=` / `r"pred=(...)"` |
| 行数 | B1 428 / B2 389 / B3 380 | B1 470 / B2 431 / B3 422 |

**机械登记（不作归因、不作判定）**：差异全部落在「v19 两形态预测字段（gsm8k `predicted` vs strategyqa `pred`）的抽取兼容层」；数值层超参零差异。

---

## §4 真判备料清单（三腿所需输入面，0 判定）

### 腿 (a) · 面 2 通用基线复现性 3/3 ±5%

| 输入件 | 状态 | 位置 / SHA-12 |
|---|---|---|
| B1 锚版 | ✅ **已就位** | `…/kt_b1/boss_b1_sinkhorn_ot.py.bak` `19325960b8be` |
| B2 锚版 | ✅ **已就位** | `…/kt_b1/boss_b2_kd.py.bak` `1781ea2f742d` |
| B3 锚版 | ✅ **已就位** | `…/kt_b1/boss_b3_llmlingua.py.bak` `c0b55e0385a4` |
| v19 frozen 数据 | ✅ **已就位** | `results/deposon_v19_benchmark_fixes.json` `910c4333eead` / 409,104 B（实测复核通过） |

- **运行注意（可执行性提示，非判定）**：3 件锚版均以**相对路径** `results/deposon_v19_benchmark_fixes.json` 载入 ⇒ 跑测须以 `deposon-repo` 为 CWD 或显式传 path，否则 `FileNotFoundError`（脚本自带该报错分支）。
- **锚版声明规模**：`N_NODES=200` / `N_QUESTIONS=200` / `N_BOSS_RESAMPLES=1000`；锚版 `_extract_200_questions` 覆盖 `E9.3_high_couple_fix` 的 gsm8k + strategyqa，双 benchmark 均读 `predicted` 字段。

### 腿 (b) / (c) · 面 3 非恒等 D_dec

- 输入面与 BOSS 脚本**无关**：全部来自 v19 frozen 的 `predicted` / `trap_hit` / `n_paths` / `n_filtered` 四字段。
- 该输入面 09-27 已完成抽取并落盘于 `_v3_recheck_21_result_2026_09_27.json` ⇒ **(b)(c) 备料不依赖本棒**；本棒解锁的是 (a) 的资产前提。
- **锚版回填不自动改判**：腿 (a) 的 3/3 结论须以锚版复算值重跑落盘后由 verdict-keeper 裁，本棒 0 代判。

### 判死候选处置（PI「不接受不明」口径下）

**本棒不触发判死候选**：锚版资产**可回填**，证据链断裂项（γ-G21-4「漂移差异内容不可核」）的**前提消失**。三腿真判所需输入面已齐备 (a) 全 4 件、(b)(c) 已落盘 ⇒ 可直接推向真实 PASS/FAIL，判定动作归 verdict-keeper。

**仍未解除的资产缺口（1 项，如实登记）**：deposon 侧 D(M,T) 的 `tools/distortion_calculator.py` 全扫 0 命中 + 理论输入 `u*(a_t)` 与理论界 `L/U` 未交付 ⇒ 该项**结构性不可算**状态不变，**不因锚版回填而改变**。

---

## §5 只读与 0 触动声明

- **命中资产 0 触动 0 移动**：3 件 `.bak` 仅经 `Get-FileHash`（SHA-256）与 `Get-Content`（UTF-8）读取；0 写入、0 重命名、0 删除、0 改 ACL、0 复制入仓。
- **既有件 0 字节改动**：`_v3_recheck_21_result_2026_09_27.json`、`_v3_recheck_21_rescript_2026_09_27.md`、`_archive_manifest_non_upload_v2_2026_09_28.json`、`deposon_v19_benchmark_fixes.json`（`910c4333eead` 复核一致）全部只读。
- **新增产物**：仅本件 1 件登记。
- **0 判定**：未对 (a)(b)(c) 任一腿给出 PASS/FAIL/不明结论；未对锚版复算值做任何断言（**锚版复算本棒未执行**，B1 单次复算约十余分钟，须派执行棒跑）。
- **派生 JSON 0 合并**。
- **key**：0 明文密钥、0 key 读取（3 件锚版实测 0 `openai` / 0 `api_key` / 0 `os.environ`，纯本地数值）。

---

## §6 老实交代

- **skill 未加载**：本 Turn 工具集内无 skill 加载入口（无 `skill` / `tool_search`）⇒ 派工单指定 skill **未加载到**；按纪律锚 fallback 按派工单字面执行，**0 编造 skill 指令**。
- **本棒未跑锚版复算**：只做资产回填与备料登记。锚版 3 件的 D(M,T) 复算值**未产出**，腿 (a) 的真判仍待执行棒跑数后由 verdict-keeper 裁。
- **锚版唯一性结论边界**：「各 1 份」限于本棒 3 个扫描根；仓外 `D:/私人资料/Downloads` 实测**不存在**，未纳入该结论。
- **`.trae` 快照层未判为锚版**：`_non_upload_local_archive/.trae/snapshots/p0p1_fix_20260909/` 下扁平命名快照（`ec18de386ff5` / `2c33c5395df0` / `51b57f13a731`）哈希**不等于**锚版三值 ⇒ 为**第三版更早态**，0 冒充锚版。
- **succeeded ≠ 跑完**：完成宣告以本件落盘核验（字节 + SHA-12）为准，值见最终汇报。

---

出件｜Mavis 团队 worker｜2026-09-28
