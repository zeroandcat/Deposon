# T1 探针 · qwen 温度扫描 · r2 棒 · 执行登记件

> **本棒只跑不判**：全文 ⛔ 0 判读、⛔ 0 宣告达标、⛔ 0 出 `K-T1-S1`/`K-T1-S3` 之 PASS/FAIL。判定归 **verdict-keeper 新 verdict 件**（沿 T15r2 体例）。
> **本件 ⛔ 0 回改任何既有件**；⛔ 0 合并派生 JSON（R5）；⛔ 0 触 `frozen`；R4 key 永不明文。

---

## §0 授权锚与输入链（当轮 `Get-FileHash -Algorithm SHA256` 实测）

### §0.1 授权

| 项 | 字面 |
|---|---|
| **PI 卡** | `ask_52effb1125dc64e6dac3295f`（2026-10-09） |
| **主裁** | **乙** —— 补构造至 ≥10 对；`re-asks 2 → 3`；约 `+60 calls`；T15r2 先例 |
| **附款** | **「并修提取面 ＋ 授权起跑」**（＝ 跑禁解除 ＋ 端点调用与额度给到） |
| **上承** | 修订案 `24DA21074CC2` §2.2 乙档；判定件 `DFC858D3D930` §2.3／§4.2／§7.1 |
| **T15r2 先例** | `963725DBD82A`（verdict）／`C69AB0E3002E`（result）—— 执行路线与合并纪律之体例基准 |

### §0.2 输入件实测表（起跑前与落盘后各一次，两次一致见 §6.1）

| 角色 | 件 | 实测 SHA-12 | 字节 | 与派工单给定值 |
|---|---|---|---|---|
| 修订案 §2.2 | `results/_th_t1_n_min_revision_proposal_2026_10_09.md` | `24DA21074CC2` | 34,884 B | ✅ 一致 |
| 判定件 §4.2 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `DFC858D3D930` | 21,672 B | ✅ 一致 |
| r1 执行登记件 | `results/_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | `7AD31E741400` | 17,341 B | ✅ 一致 |
| r1 修订件 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | `BDA5D5F3DFA0` | 16,994 B | ✅ 一致 |
| r1 executor（**只读**） | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | `F0C845864603` | 32,399 B | 派工单未给值，本轮实测在册 |
| T15r2 result（体例） | `results/_v4_supp_t15r2_result.json` | `C69AB0E3002E` | 73,526 B | ✅ 一致 |
| T15r2 verdict（体例） | `results/_v4_supp_t15r2_verdict.md` | `963725DBD82A` | 65,638 B | ✅ 一致 |
| captions | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | 12,798 B | ✅ 沿 r1 硬闸 |

**输入闸**：executor 内建 `verify_input_gates()`，对上述 6 件 results 侧锚件 + captions 逐件比对；**起跑前 `all_match = True`**，⛔ 任一不符即 `sys.exit(1)` 拒绝开跑。

### §0.3 生效件状态（如实登记 · 未落盘）

> **当轮全仓检索 `results/` 下 T1 r2 之 activation／生效件：0 命中。**
> 检索式：`results/` 内 `*t1*` 全量枚举 ＋ 全仓 `*t1*r2*`／`*r2*t1*`／`*t1*activation*`／`*t1*effect*`；T15r2 之 activation（`_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md`）系 **T15 线**件，非 T1 r2 面。
>
> ⇒ **按派工单第 7 项既定处置：生效件未落，按判定件 §4.2 字面执行**（度量为完整教师回复，含 `reasoning_content`；⛔ 不得只取 `message.content`；⛔ 不得截段）。
> ⛔ 本棒 **0 自拟提取面规格**、⛔ 0 推定 protocol-keeper 意图、⛔ 0 等待未落之件。

---

## §1 构造（沿 r1 全同，仅两处并案修正）

### §1.1 矩阵逐项

| 项 | 值 | 来源 |
|---|---|---|
| 端点 | `https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1`（`qwen_plan`，单端点） | 沿 r1 字面 |
| 模型 | `qwen3.7-max` | 沿 r1 字面 |
| 维度 × 温度 | `{L2, L14} × {0.0, 0.3, 0.5}` = **6 cells** | 沿 r1 字面 |
| cell 编号 | 0=L2/0.0　1=L2/0.3　2=L2/0.5　3=L14/0.0　4=L14/0.3　5=L14/0.5 | 沿 r1 字面 |
| 教师（5） | `kimi`、`GLM_1`、`GLM_2`、`coze`、`minimax` | 沿 TH-14，与 r1 全同 |
| L2 prompts（2） | `L_biological_taxonomy`、`S5` | 沿 r1 字面 |
| L14 prompts（2） | `L_geography_world`、`L_historical_causality` | 沿 r1 字面 |
| **re-asks** | **3**（r1 为 2） | **修正 (i)** |
| SEED | 42（**仅登记；本构造 0 用随机数**，逐字沿 r1） | 沿 r1 字面 |
| 阈值 | `TH_T1_N_MIN=10`、`K_N11_3=0.85` | **仅引用；本棒 0 判读** |

### §1.2 calls 算式（逐字）

```
每 cell = 5 教师 × 2 prompts × 3 re-asks      = 30 calls
全矩阵 = 6 cells × 30                         = 180 calls
records/教师/cell = 2 prompts × 3 re-asks      = 6
pairs/教师/cell   = C(6,2)                     = 15
```
相对 r1（`2 prompts × 2 re-asks` = 4 records ⇒ `C(4,2)=6` pairs；20 calls/cell；120 calls）：**re-asks 增量 +60 calls**，pairs 由 6 → 15（`24DA21074CC2` §2.2 算式逐字沿用）。

---

## §2 两处修正逐字

### §2.1 修正 (i) · 样本量面 —— `re-asks 2 → 3`

- **字面**：`N_REASKS = 2` → `3`；`2 prompts × 3 re-asks = 6 records/教师/cell` ⇒ `C(6,2) = 15 pairs/教师`。
- **依据**：`24DA21074CC2` §2.2 乙档；PI 卡主裁乙；`TH_T1_N_MIN = 10` 字面。
- ⛔ **0 改任何门槛字面**（`TH_T1_N_MIN` 仍为 10，未动一字）；⛔ 0 改教师、prompts、温度轴、端点、prompt 文本。

### §2.2 修正 (ii) · 响应提取面 —— 度量对象＝完整教师回复

**判定件 `DFC858D3D930` §4.2 第 1 项字面**（逐字引）：

> 「响应提取面：须以**完整教师回复**（含 `reasoning_content` 或 `max_tokens` 足以容纳完整输出）为度量对象重跑」

**本棒实现（逐字）**：

```python
content   = msg.get("content") or ""
reasoning = msg.get("reasoning_content") or ""
finish_reason = choice0.get("finish_reason")
full = (reasoning + "\n\n" + content) if reasoning else content   # ← 度量对象
```

- ⛔ **0 只取 `message.content`**；⛔ **0 截段**（`finish_reason` 逐条落盘，`finish_reason == "length"` 即计 `truncated=True`）。
- 三个文本面**分列落盘**：`content_text`／`reasoning_text`／`full_reply_text`，各带 `_len` 与 `_sha12`（`full_reply_sha12`），供下游按任一口径择读而 **0 需重跑**。
- **r1 缺陷对照（当轮实算）**：r1 executor `F0C845864603` L236–238 为 `content = data["choices"][0]["message"].get("content") or ""`；r1 records（`.tmp/_t1_qwen_temp_sweep_records.json`，`5B51AF62C640`）**逐键实测 ⛔ 0 含 `reasoning_content` 字段** ⇒ 判定件「被度量的对象不是教师完整回复，而是被推理预算挤出的残缺尾段」之根因，本棒由构造修正。

### §2.3 `max_tokens` 取值（**实测确定 · 逐字记明 · 含依据**）

**校准实测**：`.tmp/_t1_r2_calib_max_tokens_2026_10_09.json`，**6 calls**（`max_tokens ∈ {500, 2000, 4000}` × 2 tuple：`kimi/L_biological_taxonomy` ＋ `GLM_1/L_geography_world`，temp=0.3）：

| `max_tokens` 请求 | `finish_reason` | `content_len` | `reasoning_len` | `usage.completion_tokens` | `usage.reasoning_tokens` | latency |
|---|---|---|---|---|---|---|
| 500 | **stop** | 2 / 3 | 1,733 / 1,724 | 705 / 1,179 | 701 / 1,174 | 10.2 s / 15.3 s |
| 2000 | **stop** | 1 / 3 | 1,994 / 17,620 | 769 / **4,926** | 766 / 4,921 | 9.8 s / **75.6 s** |
| 4000 | **stop** | 1 / 3 | 1,075 / 2,935 | 799 / 1,592 | 795 / 1,587 | 10.4 s / 22.7 s |

**实测结论（3 条）**：

1. **⛔ 0 截段在三档全部成立**：`finish_reason = stop` 6/6 ⇒ 「无截断所需值」之条件在 **500**（r1 原值）即已满足；
2. **端点 ⛔ 0 以 `max_tokens` 约束 reasoning**：`usage.completion_tokens` 705–4,926 ≫ 请求值 500/2000/4000 ⇒ 该参数**不是**本缺陷之杠杆；
3. **上调无收益、且抬高超时风险**：`content_len` 恒 1–3 字符（与 `max_tokens` 0 相关）；2000 档实测 completion 4,926／latency 75.6 s（逼近 90 s 超时线，r1 之 timeout=90 沿用）。

⇒ **`max_tokens = 500`**（保留 r1 原值，该构造轴 **0 漂移**），提取面之实修 = **取 `reasoning_content` + `content` 之完整回复**。
⇒ 与 r1 互证：r1 records 之 `usage.completion_tokens` 实测 **597–1,716 ≫ 500**，与本次校准同向，**证实 r1 之截断本就不是因 `max_tokens=500` 所致**（沿判定件 §4.2 第 1 项「或」字之第二支不成立，第一支成立）。

---

## §3 执行路线、合成规则与 calls 计数口径（逐字）

### §3.1 路线选择：**全量 180 calls**（⛔ 0 承接 r1 120）

T15r2 体例给两条路（「承接 r1 120 ＋ 补 r2 增量」或「全量」）。**本棒选全量**，理由为**实测否决**而非偏好：

> r1 records（`5B51AF62C640`，120 条）逐键实测 **⛔ 0 含 `reasoning_content`**，其 `response_text` 即 `message.content`（1–9 字符残段）。故 r1 之 120 records **在结构上无法充当已修提取面之度量对象**；沿用之等于把待修之缺陷原样带入 r2 读数。

⇒ 合成规则：**r2 result JSON 之 records 集 = r2 自跑之 182 条（含 2 条失败原件）**；r1 之 120 条**仅作状态锚**（`inputs.r1_records_state_anchor`：path／SHA-12／`contains_reasoning_content: false`／复用裁决），**⛔ 0 并入 r2 任何读数**。

### §3.2 calls 计数口径（逐字）

| 口径 | 计数 | 说明 |
|---|---|---|
| **口径 A · 计划 calls** | **180** | 授权锚之「约 +60 calls」之落点（相对 r1 之 120） |
| **口径 B · r2 实际发端点 requests** | **182** | 主跑 180（含 2 条 timeout 失败）＋ 补跑 2（同一 tuple 重发一次） |
| **口径 C · 成功 records** | **180** | `n_records_ok`；与口径 A 逐项对齐 |
| **口径 D · 失败 records** | **2** | 原件保留于 records（沿 T15r2：失败原件不删不改） |
| **口径 E · 计划外辅助 calls** | **9** | 校准 6（§2.3）＋ 即用即探 1（计入账，沿 r1 体例）＋ 补跑 2（口径 B 内已计，此处不重复计）⇒ **净计划外 = 7** |
| **本会话端点总请求数** | **189** | ＝ 182 ＋ 6 ＋ 1 |

> **诚实登记**：PI 授权「约 +60 calls」对应口径 A 之 180；本棒另发校准 6 ＋ 探活 1（**共 7 calls，计划外**）以确定 `max_tokens` 取值（§2.3）——若以「0 计划外」为硬约束，则 `max_tokens` 之取值将只能沿用或臆断，**故如实登记此项超出**。

### §3.3 运行参数（沿 r1 字面）

| 参数 | 值 | 来源 |
|---|---|---|
| 串行间隔 | `INTER_CALL_SERIAL_S = 2.5` s | 沿 r1 字面 |
| 看门狗 | `WATCHDOG_S = 600` s／批 | 沿 r1 字面 |
| 单 call 超时 | `90` s | 沿 r1 字面 |
| 批上限 | `BATCH_CALL_LIMIT = 30` | 沿 r1 字面（登记） |
| 凭据槽 | `key_index_1based = 23`（`〔本地绝对路径·脱敏略:LLM〕 API.txt`） | 沿 r1 字面 |
| 代理 | `use_proxy = False`（`unset_proxy()` 清 `https_proxy`/`http_proxy`/`all_proxy`） | 沿 r1 字面 |
| checkpoint | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | **r2 独立 prefix**；⛔ 0 触 r1 之 `_t1_qwen_temp_sweep_records.json` |
| 起止 | 主跑 16:59:26 → 18:01:09；补跑至 18:03:12 | 当轮实测 |

---

## §4 通道与额度核验（R4 · 硬闸）

| 项 | 实测 | 结论 |
|---|---|---|
| 端点通道 | `probe` HTTP **200**，`model_returned = qwen3.7-max`，`finish_reason = stop`，latency 10,523.6 ms（**1 call，计入账**） | ✅ 可用 |
| **凭据通道** | slot 23 **存在 / len = 116 / 形态 `sk-`**（**仅存在性·长度·形态类别**） | ✅ 在位 |
| **R4 key 永不明文** | ⛔ **0 读出并回显 key 值**；key 仅进程内 runtime 读入用于调用；**0 落盘、0 打印、0 回显、0 写入任何产物** | ✅ 合规 |
| 额度 | 182 次调用中 **2 次 `timeout`（90 s），0 次 401/402/429**；2 次补跑**全 OK**；**⛔ 0 绕过、⛔ 0 改端点** | ✅ 额度可用 |
| 0 自造通道 | ⛔ 0 自造端点／凭据；沿 r1／T15 executor 既有实现 | ✅ 合规 |
| key 形态自扫 | result JSON 全量 `status = clean`（`hits = []`） | ✅ clean |

**探活落盘**：`.tmp/_t1_qwen_temp_sweep_r2_probe_log.json`（**0 含 key 值**）。
**自证落盘**：`.tmp/_t1_qwen_temp_sweep_r2_selfcert.json`（开跑前构造面自证，内建输入闸）。

---

## §5 实跑读数与自证表（**逐项实测 · ⛔ 0 判读**）

### §5.1 calls 与记录

| 项 | 实测 |
|---|---|
| records 总 / ok / 失败 | **182 / 180 / 2** |
| 补跑（失败 tuple 之重发） | **2**（`superseded_by_rerun = true` 2/2） |
| 失败明细 | ① `cell 4 / kimi / L_geography_world / r1 / t=0.3 / timeout / 90,153.1 ms`　② `cell 5 / GLM_2 / L_geography_world / r2 / t=0.5 / timeout / 90,981.2 ms` |
| 构造完整性 | 计划 tuple 180 条　vs　成功 tuple **180** 条；**缺失 0、多余 0**；records/教师/cell **min = max = 6**（30 组齐） |
| `finish_reason = stop` | **180 / 180** |
| **截段（`finish_reason == "length"`）** | **0 / 180** |
| `reasoning_content` 非空 | **180 / 180** |
| `usage.completion_tokens` | min 495 ／ 中位 **981.5** ／ max **5,767**（n=180） |
| `usage.reasoning_tokens` | min 488 ／ 中位 **976.5** ／ max **5,762**（n=180） |

### §5.2 自证项逐项实测

> **下列各项均为实测登记；⛔ 本棒 0 判读、0 宣告达标、0 出任何 PASS/FAIL。**

| 自证项 | 实测 | 备注（⛔ 0 判读） |
|---|---|---|
| **① 空响应率** | 度量对象（`full_reply`）：**0 / 180 = 0.0%**；`content_only`：0 / 180 = 0.0%；`reasoning_only`：0 / 180 = 0.0% | 三口径均 0；**「0 空响应」⛔ 不等于读数有效**（沿 `DFC858D3D930` §7.1） |
| **② pairs/教师 可达性** | records/教师/cell = **6**（30 组齐）⇒ 实得 pairs = `C(6,2)` = **15**／教师／cell；构造上限 15 | `C(6,2)=15 ≥ TH_T1_N_MIN=10` **为算式事实**；达标与否**归判定件** |
| **③ 字节发散度（温度轴有效性面）** | `full_reply` 口径：t=0.3/0.5 对 t=0.0 同教师同 caption，**全同 0 / 90（0.0%）四次全部**；`content_only` 口径：**51/90、56/90、51/90、50/90（55.6%–62.2%）** | 与 r1「16/20 字节全同」**不同源不可直接对照**（构造与口径均变）；**温度轴有效性 ⛔ 本棒 0 擅改、0 预设通过**，仅登记 |
| ④ 截段面 | 截段率 **0 / 180 = 0.0%** | 实测项，非预设 |
| ⑤ 度量对象字符长 | `full_reply`：min **716** ／ 中位 **1,867.5** ／ max **20,459**；`content_only`：min 1 ／ 中位 **3** ／ max **9** | r1 同口径实测 min 1／中位 2／max 9 ⇒ **残段形态在本棒 `content_only` 面复现** |
| ⑥ 文本互异度 | `full_reply` **180 / 180**；`reasoning_only` **180 / 180**；`content_only` **22 / 180** | r1 实测 20 / 120 ⇒ 互异度随口径剧变 |
| ⑦ `reasoning_only` 与 `full_reply` 之 J 读数 | **逐 cell 逐项完全相同**（0.231198／0.250575／0.292754／0.236364／0.159453／0.246269） | 实测观察：`content` 相对 reasoning 体量极小，故两口径 J 同值 |

### §5.3 读数登记（三口径并列 · **⛔ 0 判读**）

**cell 教师 J 中位（`j_median_all`，6 cells × 5 教师）**：

| cell | 维度/温度 | `full_reply`（本棒度量对象） | `content_only`（r1 可比） | `reasoning_only` |
|---|---|---|---|---|
| 0 | L2 / 0.0 | 0.231198 | 0.0 | 0.231198 |
| 1 | L2 / 0.3 | 0.250575 | 0.0 | 0.250575 |
| 2 | L2 / 0.5 | 0.292754 | 0.0 | 0.292754 |
| 3 | L14 / 0.0 | 0.236364 | 0.0 | 0.236364 |
| 4 | L14 / 0.3 | 0.159453 | 0.0 | 0.159453 |
| 5 | L14 / 0.5 | 0.246269 | 0.0 | 0.246269 |

- `full_reply` 口径 6 cells 全 J 中位 ∈ [0.159453, 0.292754]；每 cell 5 教师齐备（`n_teachers_with_data = 5` 6/6）。
- `content_only` 口径 6 cells 全 0.0 —— **复现 r1 之 all-pooled 0.0 形态**（跨 caption 1–9 字符零重叠）。
- ⛔ **本棒 0 就上列任一数值出裁定**；`K-N11-3`（0.85 线）、`K-T1-S1`、`K-T1-S3` 及其 hit 布尔**均未在本件给出**。
- ⚠️ **两读法并列之事实**：本次读数**对度量口径高度敏感**（同一批 responses，`full_reply` 与 `content_only` 之 J 中位相差 0.16–0.29 且后者恒 0）。**该差异本身 ⛔ 0 由本棒解释或裁定**，交判定件处理。

---

## §6 纪律自证

### §6.1 既有件 SHA-12 落盘前后比对（**一字未变**）

| 件 | 落盘前 SHA-12 / 字节 | 落盘后 SHA-12 / 字节 | 结论 |
|---|---|---|---|
| 修订案 `24DA21074CC2` | `24DA21074CC2` / 34,884 B | `24DA21074CC2` / 34,884 B | ✅ 一字未变 |
| 判定件 `DFC858D3D930` | `DFC858D3D930` / 21,672 B | `DFC858D3D930` / 21,672 B | ✅ 一字未变 |
| r1 执行登记件 `7AD31E741400` | `7AD31E741400` / 17,341 B | `7AD31E741400` / 17,341 B | ✅ 一字未变 |
| r1 修订件 `BDA5D5F3DFA0` | `BDA5D5F3DFA0` / 16,994 B | `BDA5D5F3DFA0` / 16,994 B | ✅ 一字未变 |
| r1 executor `F0C845864603` | `F0C845864603` / 32,399 B | `F0C845864603` / 32,399 B | ✅ 一字未变（**只读**） |
| T15r2 result `C69AB0E3002E` | `C69AB0E3002E` / 73,526 B | `C69AB0E3002E` / 73,526 B | ✅ 一字未变 |
| T15r2 verdict `963725DBD82A` | `963725DBD82A` / 65,638 B | `963725DBD82A` / 65,638 B | ✅ 一字未变 |
| captions `6A2656878745` | `6A2656878745` / 12,798 B | `6A2656878745` / 12,798 B | ✅ 一字未变 |
| r1 records（`.tmp`）`5B51AF62C640` | `5B51AF62C640` / 96,866 B | `5B51AF62C640` / 96,866 B | ✅ 一字未变 |
| r1 readings（`.tmp`）`E5E8F024E42E` | `E5E8F024E42E` / 11,013 B | `E5E8F024E42E` / 11,013 B | ✅ 一字未变 |
| r1 selfcert（`.tmp`）`91C2505DEEF3` | `91C2505DEEF3` / 3,866 B | `91C2505DEEF3` / 3,866 B | ✅ 一字未变 |
| r1 probe log（`.tmp`）`B5E4151AF490` | `B5E4151AF490` / 445 B | `B5E4151AF490` / 445 B | ✅ 一字未变 |
| r1 decomposition（`.tmp`）`2D96061318D9` | `2D96061318D9` / 1,312 B | `2D96061318D9` / 1,312 B | ✅ 一字未变 |

**r1 result JSON 之处置**：r1 未落 results 侧 result JSON（其读数在 `.tmp/_t1_qwen_temp_sweep_readings.json`，`E5E8F024E42E`）——**如实登记此事实**，⛔ 0 代其补落、⛔ 0 合并。

### §6.2 其余纪律

- ⛔ **0 覆写撞名**：r2 三件新名落盘前实测 0 命中；executor 内建 `RESULT_PATH.exists()` 硬闸，若撞名则拒绝写入并提示另名 `_r2_result_b_…`（沿撞名纪律）。
- ⛔ **0 合并派生 JSON**（R5）：r2 产物全部独立 `_r2_` prefix，与 `_v4_supp_t1_*`／`_v4_supp_t15*`／r1 各件 **0 合并、0 覆盖**。
- ⛔ **0 触 frozen**；⛔ **0 回改**任何既有件一字（§6.1 逐件实测）。
- ⛔ **0 新设数值阈值**：`0.85`／`10` 逐字沿用，仅作引用登记；`max_tokens` 系**构造参数**（§2.3 实测定值），**0 阈值**。
- ⛔ **0 判读落档**：全文无任何 PASS/FAIL/达标宣告；判定归 verdict-keeper 新件。
- ⛔ **0 改 L2/L14 既判**：L2 verdict、L14 verdict **一字未动**（本棒 0 触）。
- ⛔ **0 编造**：全部 SHA-12／字节／计数／读数均为当轮实测；未落定项（生效件缺失、门禁释义、判定）**如实写未落定**。
- ⛔ **0 网络**（除授权端点调用）；⛔ **0 自造通道**；⛔ **0 skill 加载**；⛔ **0 阶段名自升**（本件不含 `_v5_` 等阶段前缀；命名 `_主题_日期`）。
- 中间产物 **仅落 `.tmp/`**；落 `results/` 者仅 executor、result JSON、本登记件三件。
- 编码：**UTF-8 无 BOM ／ LF（CRLF = 0）**。

### §6.3 产物链（r2 独立 prefix）

| 件 | 路径 | SHA-12 | 字节 | 用途 |
|---|---|---|---|---|
| executor | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `38D0CF7FC9BA` | 53,184 B | 6 cells runner；selfcert/probe/run/retry/aggregate |
| result | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `8D6242DA158C` | 58,712 B | 三口径读数 ＋ 自证表 ＋ failed/superseded tuples |
| 本登记件 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | 见回执自报 | 见回执自报 | 构造／参数／修正／计数／自证／纪律 |
| self-cert | `.tmp/_t1_qwen_temp_sweep_r2_selfcert.json` | — | — | 开跑前构造面自证（含内建输入闸结果） |
| probe log | `.tmp/_t1_qwen_temp_sweep_r2_probe_log.json` | — | — | 即用即探（1 call，计入账） |
| per-call records | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | — | — | 182 records（checkpoint ＋ 终态） |
| 校准件 | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.json` | — | — | `max_tokens` 取值实测依据（6 calls） |
| 驱动/核验 | `.tmp/_t1_r2_run_driver_2026_10_09.py`、`.tmp/_t1_r2_verify_2026_10_09.py` | — | — | 续跑驱动、落盘后核验 |

---

## §7 诚实限制与残余风险

1. **本棒只跑不判**：读数已出，**判定不在本件**。`K-T1-S3` 之自证表须由判定件**重核**方能闭合——本棒自证项 ①②③ 已逐项实测在册，但**是否足以解除「不明」属裁面**。
2. **口径敏感性（本棒最大残余风险）**：同一批 responses 下 `full_reply` 与 `content_only` 之 J 中位相差 0.16–0.29，且 `content_only` 恒 0.0。**若下游择定 `full_reply` 为准**（派工单字面即如此），则读数面已变更；若沿 `content_only`，则实质回到 r1 之残段口径而样本量已扩。**该择定权不在本棒**，本棒**并列三口径 0 替下游择定**。
3. **温度轴有效性面未解**：`full_reply` 口径下 t=0.3/0.5 对 t=0.0 全同率 0/90，**与 r1「16/20 全同」方向相反**；但**「0 全同」是否即「温度轴有效」亦属判定**（发散幅度、可分辨性均未裁）。⛔ 本棒 0 擅改该面、0 预设通过。
4. **`max_tokens` 之未解面**：校准仅 6 calls、2 tuple、单温度（0.3）；「端点 0 以 `max_tokens` 约束 reasoning」之结论样本有限。**若下游认为须更大 `max_tokens`**，须另行授权重跑（本棒 0 自行加档）。
5. **超时风险**：`timeout=90` 下 2/182 超时（1.1%），均已被补跑覆盖；**若 `max_tokens` 上调或 reasoning 体量再增，超时率将升**（校准 2000 档实测 75.6 s 已逼近该线）。
6. **驱动空转（如实登记）**：驱动脚本以「失败数归零」为终止条件，而失败原件按体例保留 ⇒ 主跑末段空转约 14 次、retry 末段 2 次；**空转迭代 `new_calls = 0`（0 额外端点调用）**，仅耗墙钟。
7. **生效件缺失**：T1 r2 activation／生效件**当轮未落盘**（§0.3）⇒ 提取面规格系**按 `DFC858D3D930` §4.2 字面**执行；若 protocol-keeper 后续落盘规格与本棒实现不一致，**须另立勘正棒**，⛔ 本件 0 预判。
8. **⛔ 未做之事**：0 判读、0 宣告达标、0 合并派生 JSON、0 覆写 r1 任一件、0 触 frozen、0 回改既有件、0 调任何阈值、0 改端点／凭据机制、0 读 key 值、0 加载 skill、0 编造文献号、0 承 PI 裁（门禁释义 O-1、`TH_T1_N_MIN` 口径 O-2 均**原样留待裁面**）。

---

## §8 验收对照（自检）

- [x] 授权锚逐字录入（PI 卡 `ask_52effb1125dc64e6dac3295f`；主裁乙 ＋ 附款「并修提取面 ＋ 授权起跑」）
- [x] 输入件 7 件 SHA-12 逐一核验通过；输入闸 `all_match = True` 方起跑
- [x] 生效件状态如实登记（未落盘 ⇒ 按 §4.2 字面执行）
- [x] 构造逐项在册（6 cells／5 教师／2 prompts／**3 re-asks**／`max_tokens` 及其**实测依据**）
- [x] 两处修正逐字在册（(i) 样本量面 2→3；(ii) 度量对象＝完整回复，含实现片段）
- [x] 路线选择与**否决理由**逐字在册（⛔ 0 承接 r1，实测否决）；calls 计数口径 A–E 逐字登记
- [x] calls 实跑计数含失败/重试（182 / 180 / 2 / 补跑 2）
- [x] 自证项**逐项实测**：空响应率 0.0%；pairs/教师 = `C(6,2)` = 15 可达（6 records × 30 组齐）；字节发散度（三口径登记）
- [x] **0 判读声明**（全文无 PASS/FAIL/达标）
- [x] 0 回改确认（13 件落盘前后哈希对照）
- [x] 编码 UTF-8 无 BOM ／ LF（CRLF = 0）