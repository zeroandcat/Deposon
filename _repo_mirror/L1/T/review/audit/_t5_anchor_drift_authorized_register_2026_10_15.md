# 锚漂移登记件 · `P_A_HARNESS` 之 T5 授权补造（另立 · 合法返工）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_t5_anchor_drift_authorized_register_2026_10_15.md` |
| **件性质** | **锚漂移登记件（另立 · ⛔ 0 回改既有锚 JSON 与根因件）** · 依「授权漂移例外三要件」落账 · ⛔ 0 代 PI 裁 · ⛔ 0 宣告①毕 |
| **落盘方** | mavis（worker · T5 生成器补造棒） |
| **对象** | `P_A_HARNESS` ＝ `tools/exp_harness.py`（P-A 5 冻结工件之一） |
| **授权面（逐字）** | PI 2026-10-15 15:41 交互卡 `ask_0da60eeb3df8c8918df158a3` · §1 Q2 逐字答**「授权补 T5 生成器」**（选项 `q2_02b44195_opt1`）· 登记件 `results/_pi_card_answers_register_2026_10_15_v16.md`（SHA-12 `b8036d12e28f` ／ 5070 B · **本棒实测吻合**） |
| **三要件出处** | `results/_mq_rollout_v2_effect_register_2026_10_14.md`（SHA-12 `652da23484e2`）§2-3 `MQ-08` 之 PI 裁「按推荐档打包过」· `P-8` 三要件 |
| **显式声明** | **合法返工**（详见 §5） |
| **执行件（姊妹）** | `results/_t5_generator_build_exec_2026_10_15.md` |

---

## §1 要件 (a) · 授权链

### §1-1 授权事件（逐字 · ⛔ 0 凭转述）

| 项 | 逐字 |
| :-- | :-- |
| **卡号** | `ask_0da60eeb3df8c8918df158a3`（schemaVersion 2 · mode questionnaire） |
| **提交时点** | submittedAt ms `1792051262380` ≈ 2026-10-15 15:41:02 CST |
| **PI 逐字答** | **「授权补 T5 生成器」**（Q2 · 选项 id `q2_02b44195_opt1`） |
| **登记注记（逐字）** | 「补 T5 生成器＝**设计面授权**（沿既有四族之实现体例·判死线先于测量冻结）；⚠ `exp_harness.py` 属 P-A 5 冻结工件之一（`P_A_HARNESS`）⇒ 补造构成锚漂移，执行面须按**授权漂移例外三要件**（授权链＝本卡裁＋登记面 `anchor_status: drift_authorized`＋显式声明「合法返工」）落账，锚面变更另立登记（⛔ 0 回改既有锚 JSON）。」 |
| **登记正身** | `b8036d12e28f` ／ 5070 B · **本棒实测**（⛔ 0 沿用他件自报） |

### §1-2 授权射程（本棒据以动作之边界 · 逐字）

- **PI 授权者**：**设计面之补造**（新建 `T5` 实现体并登记入族表）。
- **PI 未授权者（本棒 ⛔ 0 触）**：⛔ 0 改任何既有族之实现体；⛔ 0 改 spec 实体；⛔ 0 reconcile 或回写既有锚 JSON；⛔ 0 回改根因件 `ba19ab186747`；⛔ 0 改 `distortion_calculator.py`；⛔ 0 代锁 `H_T5`。

---

## §2 要件 (a) · OLD → NEW 对照（本棒实测）

| 面 | **OLD** | **NEW** | 差 |
| :-- | :-- | :-- | :-- |
| **SHA-12** | `275e480ba4d9` | **`7957bac14455`** | 变 |
| **bytes** | 10090 | **13342** | **`+3252`** |
| **任务族数** | 4（`T1_GSM8K`／`T2_StrategyQA`／`T3_Trap`／`T4_2x2`） | **5**（＋`T5_LowResource`） | `+1` |
| **`task_families`** | L247 单行 4 族 | **L307–L308** 两行 5 族（T5 置末位） | 改 1 行 |
| **新增类** | — | **`LowResourceTask`**（**L248–L294**，`generate_prompts` L257、`scenarios` L260–L277、选项面 L280–L288、`name()` L294） | 新增 47 行 |
| **docstring** | V0 头 ＋ V0.2 修复注记 | **追加** V0.3 补造注记（**L24–L37**） | 追加，V0 原字面未动 |
| **`T1–T4` 之行为** | — | — | **0 变更**（prompt 面 12 项 digest 逐项一致） |

### §2-1 变更 hunk 之逐项（真实 diff · ⛔ 0 口头声明）

| # | hunk | 增／删 | 锚 |
| :-: | :-- | :-: | :-- |
| 1 | docstring 追加 `V0.3 补造(T5…)` 注记块 | `+36 / −0` | NEW L24–L37 |
| 2 | 新增 `class LowResourceTask(TaskFamily)` 及其 `generate_prompts`／`name` | `+26 / −0` | NEW L248–L294 |
| 3 | `self.task_families` 由 4 族改 5 族（T5 置末位） | `+1 / −1` | NEW L307–L308 |
| — | **合计** | **`+62 / −1`（3 hunks）** | diff 指纹 `6f1e9689201b` ／ 4043 B |

### §2-2 最小增量之**机械证明**（可复算）

1. 取 NEW 盘上文件，按上表 3 hunk **反向替换**回 OLD 字面；
2. 计算 sha-256 ＝ **`275e480ba4d9`** ／ 10090 B ＝ **与 OLD 逐字节吻合（`restore_exact=True`，3 hunk 各命中且仅命中 1 次）**；
3. ⇒ **除该 3 hunk 外 0 字节改动**；`difflib` 生成之 unified diff 统计 ＝ **3 hunks ／ +62 ／ −1 ／ +3252 B**。

> 复跑：`.tmp\t5_prove_minimal_increment_2026_10_15.py`（⛔ 0 写 `tools/exp_harness.py`，只读 ＋ 内存还原 ＋ 另存 diff）。

---

## §3 要件 (a) · 现值复测（本棒实测 · 落盘后独立通道）

| 项 | 实测值 |
| :-- | :-- |
| **`tools/exp_harness.py` 现值** | SHA-12 **`7957bac14455`** ／ **13342 B** |
| **写入时点（mtime）** | `2026-10-15T16:17:36+08:00` |
| **可运行性复测** | `python tools/exp_harness.py` → `OK: ran 30 cells (mini test, seed=42)` ＋ `OK: 同 seed 两次运行结果完全一致(可复现)` |
| **`T5` 格可跑复测** | 三套 seed 各生成 **20** 决策；每 prompt `Step ` 计数 ＝ **3**；`len(options)` ＝ **4**（互异）；`correct` ＝ payoff argmax 全 True；`value` 覆盖面全 True |
| **`T1–T4` 不扰动复测** | 12 项 prompt digest（seed 42／123／456 × 四族）改前改后**逐项一致** ⇒ 前棒 12 格读数**仍成立** |
| **行尾／编码复测** | CR 计数 ＝ **0**（纯 LF）· **0 BOM** |

---

## §4 要件 (b) · 登记面（`anchor_status: drift_authorized` ＋ `authorization_refs`）

> 📌 本块为**登记面之机器可读载荷**；⛔ **0 写入既有锚 JSON**（如 `KT_ABC1_anchors_sha256_12.json`、`KT_A1_SPEC_V0.1.md` 锚表、spec 锚表）——**一律只读**，本登记**另立承载**。

```json
{
  "anchor_id": "P_A_HARNESS",
  "path": "tools/exp_harness.py",
  "registered_old_sha256_12": "275e480ba4d9",
  "current_measured_sha256_12": "7957bac14455",
  "current_measured_bytes": 13342,
  "anchor_status": "drift_authorized",
  "authorization_refs": [
    "PI 2026-10-15 15:41 card ask_0da60eeb3df8c8918df158a3 Q2 verbatim「授权补 T5 生成器」(option id q2_02b44195_opt1)",
    "results/_pi_card_answers_register_2026_10_15_v16.md#b8036d12e28f §1 Q2 ＋ §2 派生动作 B",
    "results/_mq_rollout_v2_effect_register_2026_10_14.md#652da23484e2 §2-3 MQ-08 P-8「授权漂移例外三要件」",
    "results/_t5_generator_build_exec_2026_10_15.md（T5 补造执行件 · 判死线先冻 ＋ 三格实测）",
    ".tmp/t5_harness_diff_2026_10_15.diff#6f1e9689201b（3 hunks ＋62/−1 ＋3252 B 之真实 diff）",
    ".tmp/t5_kill_line_freeze_2026_10_15.json#1910a62c1e9f（判死面先冻 · 早于写入 2026-10-15T16:17:11+08:00）"
  ],
  "drift_class": "legal_rework",
  "drift_class_verbatim": "合法返工",
  "rework_scope": "T5 低资源博弈族之设计面补造（新增实现体 ＋ 族表登记 ＋ docstring 追加注记）",
  "authorized_by": "PI 明示裁（Q2）",
  "measured_at": "2026-10-15T16:17:36+08:00",
  "reconcile_status": "PENDING（活锚载体未 reconcile ⛔ 0 回改既有锚 JSON · 另议）",
  "prior_drift_note": "2026-09-15 逐项裁定之 DRIFT_AUTHORIZED 载 OLD=275e480ba4d9 之实体面；本次为同一锚之第二次实体变更，另立登记，新旧并存以新为准"
}
```

---

## §5 要件 (c) · 显式声明（**合法返工**，非「未授权变更」）

**本漂移之显式定性 ＝「合法返工」**（`legal_rework`）。逐条对照三要件第 (c) 项之两面：

| 面 | 判定 | 依据 |
| :-- | :-- | :-- |
| **是否在例外内** | ✅ **在例外内** | PI 于 2026-10-15 15:41 **明示**「授权补 T5 生成器」（卡逐字 ＋ v16 登记件逐字 ＋ 派工动作 B） |
| **属「合法返工」抑或「未授权变更」** | **合法返工** | 授权事件**先于**实体变更（卡 15:41:02 ／ 冻结件 `2026-10-15T16:17:11+08:00` ／ 写入 `2026-10-15T16:17:36+08:00`）⇒ 变更落授权之内 |
| **⛔ 「未授权变更」面之排除** | **排除** | 若为未授权，则**不在例外内**、条款仍自动触发——本棒逐条举证其**未**如此（授权链三要件齐备 ＋ 登记面齐备 ＋ 显式声明齐备） |
| **设置理由（照录 vol2）** | 「否则例外沦为**自证之门**」 | 本登记**未**自证：授权事件取自**他件**（卡 ＋ 登记件），指纹取自**盘上实测**，diff 取自**机械生成** |

> ⛔ **本声明之效力限于本件载明之射程**：`T5` 设计面补造（3 hunk）。**⛔ 0 扩及**本件未载之任何变更；**⛔ 0 以本登记为「自证之门」**——任何后续漂移须**各自**具备授权链与登记面。

---

## §6 与既有 `DRIFT_AUTHORIZED` 面之并存关系

| 项 | 内容 |
| :-- | :-- |
| **既有面（只读）** | 2026-09-15 逐项裁定：2 锚（`P_A_LLM_CLIENT` `055e874ea5c1→1722500da4aa`／`P_A_HARNESS` `9f383935c00c→275e480ba4d9`）判 **`DRIFT_AUTHORIZED`（合法返工）**，5 锚 9 子项 **9/9 PASS**（沿 `KT_B1_REWORK_REPORT` §四 2026-09-10 授权返工） |
| **根因件（只读）** | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md`（`ba19ab186747` ／ 37430 B）：该 2 锚之根因 ＝「已授权返工 ＋ 登记面未 reconcile」之二轨并存；**活锚载体至今仍载 OLD 值**，`patch_status: PENDING` 未竟 |
| **本次之性质** | **同一锚（`P_A_HARNESS`）之第二次实体变更** ⇒ **另立本登记**，**不回改**既有裁定与根因件任一字 |
| **并存规则** | **新旧并存，以新为准**（于本次变更面）；既有 09-15 裁定**继续有效于**其原射程（`9f383935c00c → 275e480ba4d9` 之历史事实不因本次而改） |
| **⚠ 登记 vs 实测之不符（加深一层 · 如实登记）** | 既有面已载「登记 OLD（`9f383935c00c`）vs 实测（`275e480ba4d9`）」之不符；**本次之后**现盘实体值再变为 **`7957bac14455`** ⇒ 不符之**第二层**（登记值 `9f383935c00c` vs 现盘 `7957bac14455`）。**⛔ 0 代裁 reconcile 之径**（另议） |
| **⛔ 0 触之清单** | 既有锚 JSON（`KT_ABC1_anchors_sha256_12.json` 等）、`KT_A1_SPEC_V0.1.md` 锚表、spec 锚表、根因件、卷 2 之三要件裁面 —— **全为只读，逐字节一致**（写后复测见执行件 §10-2） |

---

## §7 纪律自核

| # | 纪律 | 自核结果 |
| :-: | :-- | :-- |
| 1 | ⛔ 0 代 PI 裁 | ✅ 本件只做**登记**；「合法返工」之定性**取自 PI 明示授权**（非本棒自设） |
| 2 | ⛔ 0 回改既有锚 JSON／根因件 | ✅ **0 字节改动**（写后复测逐字节一致） |
| 3 | 另立承载 | ✅ 本件**另立**；⛔ 0 就地改既有锚表 |
| 4 | 指纹实测（⛔ 0 凭转述） | ✅ OLD 由**机械反演复原**（sha 逐字节吻合）· NEW／diff／冻结件 ＋ 8 件源件指纹**均为本棒实测** |
| 5 | ⛔ 0 宣告①毕 | ✅ 0 宣告 |
| 6 | 判死不软化 | ✅ 「登记面未 reconcile」之不符**如实登记**（§6），未以「例外已立」掩盖 |
| 7 | 落盘纪律 | ✅ `io.open(encoding='utf-8', newline='\n', errors='strict')` 直写；⛔ 0 经 PowerShell 管道中转；key 形态扫描**落盘前 0 命中** |

---

## §8 终判归属（**候 PI 核准** · 五终判语汇）

**本件建议落 `pass`**（三要件逐条齐备且可复算）；**并登记一项挂账**：`reconcile_status: PENDING`（活锚载体未 reconcile，⛔ 0 代裁其径）。**⛔ 0 宣告①毕**；终判之落定权属 PI。

> 📌 **本件自身 SHA-12**：自哈希不可自含——由落盘后独立通道复算，自报于执行件与回复。
