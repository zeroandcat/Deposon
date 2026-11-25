# T3_Trap 可答化（KD-3 构造缺陷修复）· 执行件（2026-10-15）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_t3trap_answerable_build_exec_2026_10_15.md` |
| **件性质** | **实验执行件**（判死线冻结面＋字面对照＋重测读数＋证书符合性评估）· ⛔ 0 代 PI 裁 · ⛔ 0 宣告①毕 · ⛔ 0 回改任何既有件（除授权面） |
| **出件方** | mavis（worker · T3 可答化棒 · v18 派生动作 C） |
| **姊妹件** | `results/_t3trap_answerable_drift_authorized_register_2026_10_15.md`（锚漂移登记件 · 另立） |
| **授权面（逐字）** | PI 2026-10-15 17:03 交互卡 `ask_4b8a0b5856efd3c921e051c8`（schemaVersion 2 · mode questionnaire · submittedAt ms `1792054988755`）**Q1 逐字裁「裁 B′（留全族＋登记不可证）（推荐）」**（选项 id `q1_bc2782c2_opt1`）｜登记件 `results/_pi_card_answers_register_2026_10_15_v18.md`（SHA-12 `318d176e027c` ／ 4,670 B · **本棒实测验明正身**） |
| **授权之推导（逐字照录 · ⛔ 0 以本棒曲解）** | v18 §1 Q1 登记注记逐字：「……**附带 T3 可答化授权**（选项题注已明示「T3 可答化（`tools/*` 变更须授权·锚漂移三要件）」，PI 于明知该题注下采 B′ ⇒ 可答化之授权随 B′ 成立——执行面按授权漂移例外三要件落账）」；§2 派生动作 C 派本棒；§3-2 逐字载该推导链并载「PI 若意在「可答化另行再裁」则以 PI 后示为准」 |
| **跑禁** | 已解（v6 `7e95b053e249`） |
| **状态** | **已落盘 · 候 PI 核准**（⛔ **0 径行采认**）｜⛔ 0 宣告①毕 · ⛔ 0 代 PI 裁 · ⛔ 0 回改任何既有件（除 `exp_harness.py` 之授权面） |

> 📌 **本件之一级结论（先于一切读数）**：可答化**成就**（`T3` 之 15 个 prompt
> **全部自足可判**——机械判据见 §5 之 V3：15/15 含显式判准、15/15 之正解可自 prompt 字面推出）；
> 重测 **45/45 call 全产出有效动作、0 拒答**（旧面为 10/15 拒答），`KL-M41-1` 之 `R_no-action`
> 门**未触发**；`T3` 三格之 `S̄_H(γ=1/10)` ＝ **`0.08426`／`0.07702`／`0.04537`**，
> **均 ≤ `τ_cert=1/10`**（旧面 `0.36671` 违反）。
> ⚠ **然本棒 ⛔ 0 由此宣告「证书成立」**（理由逐条见 §6-3）——
> 新面为 `T3` 单族×单模型×单 seed×`H_face=15`，且实测**同一批逐字相同之 prompt 在
> `temperature=0` 下三格误点位置互异**（§4-4）⇒ 符合性**不稳健**。

---

## §0 一句话结论

`T3_Trap` 之构造缺陷 `KD-3`（prompt 无可判据 ⇒ 模型无从判读）**已由 PI 授权之可答化修复**：
prompt 改为携带**两选项之实体含义**（各型之净值明数）＋**显式判准**（「higher net total over
the two rounds」），而 `options`／`correct`／`value`／`shuffle` **四行逐字未动**
（仍为 2 选 1 ⇒ `C1` 类成员关系不变；`greedy→A`、`deposit/cost→B` 之映射未动；**0 新增随机数**）
⇒ **`T1`/`T2`/`T4`/`T5` 之 prompt 集逐字不变**（§3-3 机械证）。重测得 **`T3` 三格 0 拒答、
`D=2/15`、`S̄` 落于 `τ_cert` 内**；**新旧读数属不同 treatment，⛔ 0 直接可比**。

---

## §1 判死线先冻（FTFB · 冻结面早于任何改动与任何测量）

### §1-1 冻结件与时序证据（盘上实测 mtime）

| 项 | 值 |
| :-- | :-- |
| **冻结件** | `.tmp/t3_freeze_2026_10_15.json`（SHA-12 `313f091718cc` ／ 7,436 B） |
| **冻结时点** | **`2026-10-15T17:17:18+08:00`** |
| **`tools/exp_harness.py` 写入时点** | **`2026-10-15T17:17:49+08:00`**（冻结后 **31 秒**） |
| **测量产物（`t3_nt_measurement_2026_10_15.json`）落盘时点** | **`2026-10-15T17:21:54+08:00`** |
| **独立复算件落盘时点** | `2026-10-15T17:22:46+08:00` |
| **序之成立** | ✅ **冻结（17:17:18）＜ 改动（17:17:49）＜ 测量（17:21:54）** ⇒ **0 先跑后补线、0 事后调阈值** |

### §1-2 冻结内容（逐字照录冻结件 · ⛔ 0 事后增补）

- **`KL-M41-1`**：`任一臂或任务族 R_no-action > 0.05(>5%) ⇒ Per-Protocol 效度门失败; 主推断必须默认转全分母 ITT 读数(no-action 计为 A_t∉K_t)`
- **`KL-M41-2`**：`候选剥离规则 C_k 之采纳当且仅当: (i) 3-seed 配对 bootstrap 95% CI 上界 CI_hi(ΔR_ITT) < 0, 且 (ii) 点估计缩减超单格离散地板 |ΔR| ≥ 1/60; 否则不剥离(保留全未剥离分母)`
- **`KL-M41-3`**：`seed∈(42,123,456) 三套; 若 std(R)/mean(R) > 0.20 ⇒ 标记 SEED_SENSITIVE(kd / GRAY)`
- **`ε*(H)=H/10`** ⇒ **`ε*(T3)=2`**（锁值件 v2 §2-2 之成就值 · 依 `H_T3=20`）
- **`γ=1/10` ＋ `τ_cert=1/10`**（锁值件 v2 §2-4 · PI 裁 Q3）· ⛔ 0 代改
- **`S` 递归与证书式**：`S_{t+1} = (1−γ)·S_t + γ·1{A_t∉K_t}, γ∈(0,1), S_0=0`；`E[S̄_H] ≤ τ_cert, S̄_H=(1/H)·Σ_{t=1..H} S_t`
- **`kill_decision` 三档**：`mean_mult>=2.0 or theory_U_hit_rate>=0.3 ⇒ FAIL_H0; elif mean_mult<=1.5 and ci_hi<=1.8 and theory_U_hit_rate<=0.1 ⇒ PASS_H1; else ⇒ GRAY`
- **`theory_U_hit_rate` 退役面**（`1ba41ba3bbe9`）：**判死面不启用** ⇒ **⛔ 0 跑 `kill_decision`**（跑了必以缺参产出误导之 `GRAY`）
- **本面之禁**：⛔ 0 事后调阈值 · ⛔ 0 以重测读数反推改判死线 · ⛔ 0 以 `T3` 读数改 `KL-M41-1..3` · ⛔ 0 新设数值切点 · ⛔ 0 代 PI 锁 `H_T3`/`γ`/`τ_cert` · ⛔ 0 以新读数充旧面读数 · ⛔ 0 宣告①毕 · ⛔ 0 代 PI 裁
- **⚠ `H` 之两面区分（如实登记 · 勿混用）**：入锁之 **`H_T3=20`**（锁值 v2 §2-1）⇒ `ε*(T3)=2`；
  本 LLM 重测面沿 **M-41 前棒逐字之每族 15 决策** ⇒ **`H_face=15`**，其面内 `H/10=3/2` 仅为面内局部量，
  **⛔ 0 替代入锁之 `2`**。`S̄_H` 之递归按**本面实测 `H=15`** 计算（与旧面 `S̄` 表之 `H=15` 同口径）。

---

## §2 改前 → 改后字面对照（授权变更 · 逐字）

### §2-1 三 hunk 之声明（实施前预登记于冻结件 `OLD_to_NEW_literal_preregistered`）

| # | hunk | 面 | 增／删 |
| :-: | :-- | :-- | :-- |
| 1 | **A** | docstring 追加 `V0.4 可答化(T3…)` 注记块（V0／V0.2／V0.3 原字面**一字未动**） | `+16 / −0` |
| 2 | **B** | `TrapTask.generate_prompts` 内新增局部线索表 `clues`（3 型 × 两选项实体含义与净值） | `+15 / −0` |
| 3 | **C** | prompt 之 f-string 由 1 行改为 3 行（携带线索表＋判准） | `+2 / −1` |

### §2-2 hunk C 之字面对照（**核心变更**）

**改前（OLD · 逐字）**：

```python
                'prompt': f'Trap scenario {i+1} (type={trap}). Which option?',
```

**改后（NEW · 逐字）**：

```python
                'prompt': f'Trap scenario {i+1} (type={trap}). {clues[trap]} Choose the '
                          f'option with the higher net total over the two rounds. '
                          f'Which option?',
```

**新增之 `clues`（hunk B · 逐字）**：

```python
        clues = {
            'greedy': ('Two rounds remain. Option A: play the balanced line, gaining 2 '
                       'this round and 4 next round (net 6). Option B: play the greedy '
                       'line, gaining 5 this round and 0 next round (net 5). '),
            'deposit': ('Two rounds remain. Option A: deposit all 3 units into the growth '
                        'fund, which pays 3 this round and 0 next round (net 3). Option B: '
                        'keep 1 unit in the steady fund, which pays 2 this round and 2 '
                        'next round (net 4). '),
            'cost': ('Two rounds remain. Option A: take the fast route, which pays 4 this '
                     'round but charges a service cost of 1 in each of the two rounds '
                     '(net 2). Option B: take the slow route, which pays 3 this round '
                     'and charges no service cost (net 3). ')
        }
```

> ✅ **正解自洽性（机械判据 · 非设计意图之声明）**：三型之正解与既有 `correct` 映射
> （`greedy→Option A`；`deposit`/`cost→Option B`）**逐项相符**——`greedy` 净值 `6>5` ⇒ A；
> `deposit` `3<4` ⇒ B；`cost` `2<3` ⇒ B。**15/15 prompt 之正解可自其字面推出**（§5 之 V3 实测）。

### §2-3 未动之四行（逐字 · 与旧件一致）

```python
            options = ['Option A', 'Option B']
            correct = 'Option A' if trap == 'greedy' else 'Option B'
            random.shuffle(options)
                'value': {o: 1.0 if o == correct else 0.5 for o in options}
```

⇒ `len(options)==2`（`C1_二选一负荷不等` 之成员关系**不变**）· `trap→correct` 映射**不变** ·
`value` 编码**不变** · **0 新增随机数调用**（`clues` 之构造不耗随机态）。

### §2-4 真实 unified diff（`.tmp/t3_harness_diff_2026_10_15.diff` · `0f8532aefdff` ／ 3463 B · 逐字照录）

```diff
--- tools/exp_harness.py@OLD(7957bac14455)
+++ tools/exp_harness.py@NEW(7a097d7802d1)
@@ -32,6 +32,20 @@
 - 锚漂移按授权漂移例外三要件落账(合法返工), 登记面见
   results/_t5_anchor_drift_authorized_register_2026_10_15.md
 - 上方 V0 原字面(4 任务族 / 300 cells)历史留痕, 一字未改
+
+V0.4 可答化(T3, 2026-10-15, PI 2026-10-15 17:03 卡 Q1「裁 B′」附带授权):
+- 修复 T3_Trap 之构造缺陷 KD-3(M-41 b9feb5df8d44 §7: prompt 无可判据 ⇒
+  10/15 拒答、读数不可解释为「模型失真」): prompt 改为携带两选项之实体
+  含义与显式判准(净值两轮合计), 三型陷阱之正解均可自 prompt 推出
+- options / correct / value / shuffle 四行逐字未动(仍为 2 选 1 ⇒ C1 类成员
+  关系不变; greedy→Option A、deposit/cost→Option B 之映射未动; 0 新增随机数)
+- T1/T2/T4/T5 之实现体一字未动 ⇒ 其 prompt digest 与既有 12 格读数不受扰动
+- 判死线先冻(FTFB): KL-M41-1..3 与 kill_decision 之 2.0/0.3/1.5/1.8/0.1
+  五切点逐字未动; H_T3=20 与 ε*(T3)=2 之锁值权属 PI(本棒只读, ⛔ 0 代改)
+- 锚漂移按授权漂移例外三要件落账(合法返工), 登记面见
+  results/_t3trap_answerable_drift_authorized_register_2026_10_15.md
+- 新旧 prompt 属不同 treatment ⇒ 新旧读数不可直接可比(如实声明)
+- 上方 V0/V0.2/V0.3 原字面历史留痕, 一字未改
 """
 
 from __future__ import annotations
@@ -201,13 +215,30 @@
 
     def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
         prompts = []
+        # V0.4 可答化: 三型陷阱之实体含义与显式判准(净值两轮合计之较高者);
+        # 解: greedy→A(净6>净5)、deposit→B(净4>净3)、cost→B(净3>净2)
+        clues = {
+            'greedy': ('Two rounds remain. Option A: play the balanced line, gaining 2 '
+                       'this round and 4 next round (net 6). Option B: play the greedy '
+                       'line, gaining 5 this round and 0 next round (net 5). '),
+            'deposit': ('Two rounds remain. Option A: deposit all 3 units into the growth '
+                        'fund, which pays 3 this round and 0 next round (net 3). Option B: '
+                        'keep 1 unit in the steady fund, which pays 2 this round and 2 '
+                        'next round (net 4). '),
+            'cost': ('Two rounds remain. Option A: take the fast route, which pays 4 this '
+                     'round but charges a service cost of 1 in each of the two rounds '
+                     '(net 2). Option B: take the slow route, which pays 3 this round '
+                     'and charges no service cost (net 3). ')
+        }
         for i in range(n):
             trap = random.choice(['greedy', 'deposit', 'cost'])
             options = ['Option A', 'Option B']
             correct = 'Option A' if trap == 'greedy' else 'Option B'
             random.shuffle(options)
             prompts.append({
-                'prompt': f'Trap scenario {i+1} (type={trap}). Which option?',
+                'prompt': f'Trap scenario {i+1} (type={trap}). {clues[trap]} Choose the '
+                          f'option with the higher net total over the two rounds. '
+                          f'Which option?',
                 'options': options,
                 'correct': correct,
                 'value': {o: 1.0 if o == correct else 0.5 for o in options}

```

---

## §3 最小增量之机械证明（沿 T5 先例体例）

### §3-1 反演复原（可复算）

| 项 | 值 |
| :-- | :-- |
| **复算脚本** | `.tmp/t3_prove_minimal_increment_2026_10_15.py`（**⛔ 0 写 `tools/exp_harness.py`**，只读＋内存还原＋另存 diff） |
| **3 hunk 各命中次数** | A ＝ **1** · B ＝ **1** · C ＝ **1**（各恰 1 次 ⇒ 反演无歧义） |
| **反演后 sha-256 前 12** | **`7957bac14455`** ／ **13342 B** |
| **OLD 基准** | `7957bac14455` ／ 13,342 B ⇒ **逐字节吻合（`restore_exact=True`）** |
| **NEW 实测** | `7a097d7802d1` ／ 15708 B（差 **+2366 B**） |
| **difflib 统计** | **2 hunks ／ +32 ／ −1** |

### §3-2 可运行性复测（现值）

- `python tools/exp_harness.py` ⇒ `OK: ran 30 cells (mini test, seed=42)` ＋ `OK: 同 seed 两次运行结果完全一致(可复现)`
- 行尾／编码：**CR ＝ 0**（纯 LF）· **0 BOM** · U+FFFD ＝ 0

### §3-3 不扰动之机械证明（他族逐字不变）

| 口径 | 结果 |
| :-- | :-- |
| **方法** | 将内存复原之 OLD 模块另存 `.tmp/ref_exp_harness_OLD_2026_10_15.py`（**非源件**）后与现盘 NEW 模块**分别 import**，逐族逐 seed **逐条比较 prompt 列表（列表相等判定）** |
| **`T1`/`T2`/`T4`/`T5`（3 seeds × 各族）** | **`nonT3_all_identical=True`** ⇒ **他族 prompt 集逐字不变** ⇒ 既有 12 格读数不受扰动 |
| **`T3`（3 seeds）** | **`T3_changed_as_intended=True`** ⇒ 三 seed 之 `T3` prompt digest **均已变更**（treatment 变更之预期结果） |
| **对 T5 基线 digest 之复核（口径 B）** | 以**单一 seed 逐族顺序生成**之口径重算 12 项 ⇒ **12/12 复现** `.tmp/t5_prefix_T1T4_digest_2026_10_15.json` 之值 |
| ⚠ **口径注记（如实登记 · 判死不软化）** | 「每族前重播种」口径（A）与「单 seed 逐族顺序」口径（B）对 **`T2`/`T3` 给出不同 digest**（族间随机态是否连续）——二者**均自洽但不可混用**；本棒之前棒基线文件系口径 **B**，故一切 digest 比对**须同口径**。此为**方法面口径差**，**非**数据矛盾、**非**改动所致（口径 B 下 OLD 与 NEW 对 `T1`/`T2`/`T4`/`T5` 逐字一致） |

---

## §4 重测（`T3` 三格 × 3 机制 · 逐 call 留痕）

### §4-1 面与处理条件（⛔ 0 变更 treatment 之非授权项）

| 项 | 取值 |
| :-- | :-- |
| **面** | `T3_Trap` 可答化后之重测（**3 格 ＝ M1/M2/M3 × `T3_Trap`**）· `seed=42` · 每格 **15** 决策 ⇒ 45 cell · ⛔ 0 与 M-41 旧面合并计数 |
| **LLM 通路** | `ANTHROPIC_BASE_URL` 之 host ＋ `/v1/messages`（chat/messages 协议）· 模型 id 自 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 读（实测 `claude-haiku-5-5`） |
| **处理条件** | system 模板 / `max_tokens=48` / `temperature=0` —— **与 M-41 前棒逐字同** |
| **解析规则** | 照录 `.tmp/m41_r15_collect_readout.py:61-77` 逐字（`EXACT` > `TAIL_LAST` > `FULL_LAST`；**⛔ 0 兜底选首项**，无匹配即记「0 有效动作」） |
| **唯一变更项** | `exp_harness.TrapTask.generate_prompts` 之 prompt 字面（**授权面**） |
| **key 处置（R4）** | token 仅自 runtime env 读入 client 内部；⛔ 0 打印 · 0 入件 · 0 入日志 · 0 入 prompt；落盘后经形态扫描实测 **0 命中**（§5 之 V4） |

### §4-2 逐格读数（本棒实测）

| 格（机制） | `H_face` | calls | 0 有效动作 | 拒答率 | 精确值 | `KL-M41-1` 门 | `D`（LLM 臂） | `S̄_H(γ=1/10)` | 余量 `τ_cert−S̄` | 自检轨倍数(`ε=1/10`) | 判死轨倍数(`ε*=2`) | 机制臂正确 | `kill_decision` |
| :-- | --: | --: | --: | --: | :--: | :-: | :--: | --: | --: | :--: | :--: | :--: | :-: |
| `M1_Deposon_TRA` | 15 | 15 | **0** | 0 | 0 | `NOT_TRIGGERED` | `2/15` | **0.08426** | `0.01574` | `4/3` | 1/15 | `10/15` | NOT_RUN |
| `M2_Greedy` | 15 | 15 | **0** | 0 | 0 | `NOT_TRIGGERED` | `2/15` | **0.07702** | `0.02298` | `4/3` | 1/15 | `15/15` | NOT_RUN |
| `M3_Random` | 15 | 15 | **0** | 0 | 0 | `NOT_TRIGGERED` | `2/15` | **0.04537** | `0.05463` | `4/3` | 1/15 | `7/15` | NOT_RUN |

### §4-3 逐 call 采集账（45 call · ⛔ 0 合并计数）

**`M1_Deposon_TRA` × `T3_Trap`**：

| cell | correct | LLM 动作 | 规则 | tries | 判定 |
| :-- | :-- | :-- | :-- | --: | :-- |
| `T3_Trap#00` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#01` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#02` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#03` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#04` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#05` | `Option B` | `Option A` | `EXACT` | 1 | **失真** |
| `T3_Trap#06` | `Option A` | `Option B` | `EXACT` | 1 | **失真** |
| `T3_Trap#07` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#08` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#09` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#10` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#11` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#12` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#13` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#14` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |

**`M2_Greedy` × `T3_Trap`**：

| cell | correct | LLM 动作 | 规则 | tries | 判定 |
| :-- | :-- | :-- | :-- | --: | :-- |
| `T3_Trap#00` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#01` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#02` | `Option A` | `Option B` | `EXACT` | 1 | **失真** |
| `T3_Trap#03` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#04` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#05` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#06` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#07` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#08` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#09` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#10` | `Option B` | `Option A` | `EXACT` | 1 | **失真** |
| `T3_Trap#11` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#12` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#13` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#14` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |

**`M3_Random` × `T3_Trap`**：

| cell | correct | LLM 动作 | 规则 | tries | 判定 |
| :-- | :-- | :-- | :-- | --: | :-- |
| `T3_Trap#00` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#01` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#02` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#03` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#04` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#05` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#06` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#07` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#08` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#09` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |
| `T3_Trap#10` | `Option B` | `Option A` | `EXACT` | 1 | **失真** |
| `T3_Trap#11` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#12` | `Option B` | `Option A` | `EXACT` | 1 | **失真** |
| `T3_Trap#13` | `Option A` | `Option A` | `EXACT` | 1 | 判对 |
| `T3_Trap#14` | `Option B` | `Option B` | `EXACT` | 1 | 判对 |

**采集面汇总**：calls ＝ **45** · 有效动作 ＝ **45** · 0 有效动作 ＝ **0** ·
全域 `R_no_action` ＝ **0** ⇒ `KL-M41-1` 之 5% 门 **NOT_TRIGGERED**；
规则命中：`EXACT` 45／45（**0 次 `TAIL_LAST`／`FULL_LAST`／`NOMATCH`**，解析面**0 争议**）；
`tries` 全为 **1**（**0 重试**）。

### §4-4 ⚠ 新发现：`temperature=0` 下之端点非确定性（判死不软化 · 本棒新立）

三格之 prompt 集**逐字相同**（digest 三格同为 `f188bdf6e17d`，V2 实测），然三格之 **2 处失真落在不同决策序号**：

| 格 | 失真 cell（correct → LLM 动作） |
| :-- | :-- |
| `M1_Deposon_TRA` | 05(Option B→Option A) ／ 06(Option A→Option B) |
| `M2_Greedy` | 02(Option A→Option B) ／ 10(Option B→Option A) |
| `M3_Random` | 10(Option B→Option A) ／ 12(Option B→Option A) |

⇒ **同一批逐字相同之 prompt、`temperature=0`，逐次调用仍产出不同动作**
⇒ ① `D=2/15` 三格同值系**计数巧合**，**⛔ 0** 据以作「机制间无差异」之结论；
② 本面之 `S̄` **含端点随机性**，其 `0.01574` 之最小余量**不足以支撑稳健性主张**；
③ 与 M-41 `KD-4` 同族（单模型＋单 seed），**且更甚**：非 seed 敏感而是**同 seed 内非确定**。

---

## §5 复算可核面（独立通道 · 逐项）

| 面 | 指针 |
| :-- | :-- |
| **判死线冻结件** | `.tmp/t3_freeze_2026_10_15.json`（`313f091718cc`） |
| **改前全盘指纹清单（882 件）** | `.tmp/t3_prechange_manifest_2026_10_15.json`（`f1508ebe14e7`） |
| **真实 diff** | `.tmp/t3_harness_diff_2026_10_15.diff`（`0f8532aefdff` ／ 3,463 B） |
| **最小增量机械证明** | `.tmp/t3_prove_minimal_increment_2026_10_15.py` ＋ 结果 `3f858f6958cd` |
| **他族等价性比较（OLD vs NEW 逐条 import）** | `.tmp/t3_postchange_equiv.py` ＋ 结果 `.tmp/t3_postchange_equiv_2026_10_15.json` |
| **基线口径探针（A vs B）** | `.tmp/t3_baseline_procedure_probe.py` ＋ `.tmp/t3_baseline_procedure_probe_2026_10_15.json` |
| **OLD 参考件（非源件 · 内存复原另存）** | `.tmp/ref_exp_harness_OLD_2026_10_15.py`（sha `7957bac14455`） |
| **采集脚本（LLM 面）** | `.tmp/t3_nt_measure_2026_10_15.py` |
| **采集 cache（含 `raw_len` 之返代表征面）** | `.tmp/t3_nt_llm_calls_2026_10_15.jsonl`（`0cb1decec878`） |
| **读数全量（逐 call）** | `.tmp/t3_nt_measurement_2026_10_15.json`（`92f0dc763caf` ／ 19,576 B） |
| **独立复算校验脚本** | `.tmp/t3_nt_verify.py` ＋ 结果 `.tmp/t3_nt_verify_2026_10_15.json`（`700de33ee255`） |
| **写后全盘复测** | `.tmp/t3_postcheck.py` ＋ `.tmp/t3_postchange_manifest_check_2026_10_15.json` |

**独立复算五面结果**（`ALL_ARMS_MATCH=**True**`）：

| 面 | 内容 | 结果 |
| :-: | :-- | :-- |
| **V1** | 自 cache **逐格重算**三格之 `D`／`S̄`／证书判定／拒答计数，与测量件逐项比对 | **三格之 `D`／`S̄`／证书判定／拒答计数**逐项一致**** |
| **V2** | 三格 prompt 集逐字相同（跨机制 0 差异） | **`True`** |
| **V3** | **可答化之机械判据**：15 prompt 逐条自字面解析两选项净值与判准 ⇒ 正解可推出 | **15/15 可推出**（判准 15/15 在场 · 2 选项 15/15） |
| **V4** | key 形态扫描（env token 全值／前 8／尾 8 ＋ `sk-` 形态 ＋ `ANTHROPIC_AUTH_TOKEN=` 形态）于读数件与 cache | **命中 0** |
| **V5** | `S` 递归实现之自检：以旧面 `T3` 误点集复算 `S̄` ⇒ 应复现在册 `0.36671` | **复现（`550063890377939/1500000000000000 = 0.36671`）** |

> 📌 **V5 之作用与界限**：该复算**仅验证本棒 `S` 递归实现之正确性**（对旧面之旧误点集），
> **⛔ 0 并入新读数、⛔ 0 以之充旧面复现**。

---

## §6 证书符合性评估（`τ_cert=1/10` · 判死不软化）

### §6-1 逐格结果

| 格 | `S̄_H(γ=1/10)` | `τ_cert` | 判定 | 余量 |
| :-- | --: | --: | :-: | --: |
| `M1_Deposon_TRA` | `0.08426` | 1/10 | **符合** | `0.01574` |
| `M2_Greedy` | `0.07702` | 1/10 | **符合** | `0.02298` |
| `M3_Random` | `0.04537` | 1/10 | **符合** | `0.05463` |

### §6-2 与旧面之对照（**不同 treatment · ⛔ 0 直接可比**）

| 面 | `T3` 之 `S̄_H(γ=1/10)` | 相对 `τ_cert=0.1` | 拒答 | 出处 |
| :-- | --: | :-: | :-- | :-- |
| **旧面**（M-41 · treatment A） | **`0.36671`** | **违反（超 2.67 倍）** | **10/15** | `6630447e5ec7` §4-2 ／ `b9feb5df8d44` §4-1 |
| **本面**（可答化后 · treatment B） | **`0.08426`／`0.07702`／`0.04537`** | **三格皆符合** | **0/45** | 本件 §4-2 |

### §6-3 ⛔ 本棒**不**宣告「`γ=1/10` 之证书成立」之理由（逐条）

1. **面之不同**：旧面之 `S̄` 表系 **ITT 全族**（`T1`+`T2`+`T3`+`T4` · `H=15`）之族别实测；
   本面系 **`T3` 单族三格**、`H_face=15`、单模型、单 seed ⇒ **本面之符合性 ⛔ 0 外推至全族**。
2. **`T2` 残余项未动**：判断件一之核心判别事实（`T2` 自身 `S̄=0.10873>0.1` ⇒ 剔 `T3` 不解越界）
   **本棒 0 重测、0 消解** ⇒ **全族证书面之残余越界仍在册**。
3. **不确定性未消除且本棒更甚**：`KL-M41-3` 三套 seed 之**读数面未测**（`SEED_SENSITIVE` 未成就亦未否定）；
   且实测 `temperature=0` 下**同 seed 内非确定**（§4-4）⇒ 最小余量仅 `0.01574`，**不足以支撑稳健性主张**。
4. **`H` 之锁值未被本面满足**：入锁 `H_T3=20`，本面 `H_face=15` ⇒ 本面 `S̄` **⛔ 0 充** `H=20` 之 `S̄`
   （`S̄` 随 `H` 变）⇒ **本面 0 成就 `U(20;…)` 之证书面**。
5. **构造成立 ≠ 缺陷已结**：可答化修复的是**构造缺陷 `KD-3`**；
   `T3` 三格之终判是否转正**不属本棒职权**（沿 v18 派生动作 B 之落账件 §2-1 逐字：
   「可答化后**须重跑方有新读数**，⛔ 0 预判其终判」）⇒ **终判候 verdict-keeper 另议**。

### §6-4 新旧可比性声明（逐字 · 冻结件已预登记）

> **可答化变更 treatment（prompt 字面由无判据改为携带两选项实体含义与判准）⇒
> 新旧读数 ⛔ 0 直接可比、⛔ 0 跨 treatment 合并计数、⛔ 0 以新读数回改 M-41 面读数；
> 旧 `T3` 读数（10/15 拒答·5/15 猜标签）仅作构造缺陷之历史留痕。**

---

## §7 具名缺陷（**本棒新立** · 候 verdict-keeper 归并 · ⛔ 0 代裁）

| # | 缺陷 | 判别式／实测 |
| :-: | :-- | :-- |
| **`KD-T3-A1`** | **`temperature=0` 下端点非确定** | 同 prompt 集（digest 三格同为 `f188bdf6e17d`）· 三格失真 cell **各异** ⇒ 单次读数含端点随机性（§4-4） |
| **`KD-T3-A2`** | **`KL-M41-3` 读数面未测** | 仅 `seed=42`；`std(R)/mean(R)` **未算** ⇒ `SEED_SENSITIVE` 标记**未成就亦未否定**（⛔ 0 以计数面冒充读数面） |
| **`KD-T3-A3`** | **基线臂 oracle 饱和未解** | `M2_Greedy` 机制臂 **15/15**（`value` 逐族编码 `correct`）⇒ 基线面**0 判别力**（沿 M-41 `KD-1`，本棒⛔ 0 修，因属设计面调整·候 PI 裁） |
| **`KD-T3-A4`** | **`H_face=15` ≠ 入锁 `H_T3=20`** | 本面 `S̄` 之 `H` 与 `U` 式之 `H` 不同面 ⇒ 本面**0 成就** `U(20;…)` 证书面（§6-3-4） |
| **`KD-T3-A5`** | **锚面未 reconcile（第三层）** | 登记值 `9f383935c00c`（`KT_A1_SPEC_V0.1.md` 锚表）vs 现盘 `7a097d7802d1` ⇒ 不符之第三层；⛔ 0 代裁 reconcile 之径（详见姊妹件） |

---

## §8 五终判归属建议（沿五终判语汇 · ⛔ 0 代 PI 裁）

本棒**建议落 `kd`**（读数已产出 45/45、0 缺格，且可答化后 `T3` 三格于本面落于 `τ_cert` 内，然带 §7 之具名缺陷）；**并登记挂账项**：三套 seed 之读数面未测（`KL-M41-3`）· 基线臂 oracle 饱和未解 · reconcile 之径未裁。⛔ **0** 判 `pass`（判据「`T3` 终判是否转正」不属本棒职权·沿 v18 派生动作 B 之纪律「可答化后须重跑方有新读数·⛔ 0 预判其终判」）· ⛔ **0** 判 `af`（`N-B-3` 第①组件要求剔**具名**伪影实体后取读数，而本面之伪影实体由本棒自设且未经 PI 择定）· ⛔ **0** 判 `give-up`（无 PI 明示放弃⇒悬置属挂账非终判）· ⛔ **0** 判 `fail`（本棒判据「产出新证据面并落三要件账」已达成）。

---

## §9 落盘字节级自报（**盘上实测 · 见交付回执**）

⚠ **自指悖论**（沿体例先例件 `6630447e5ec7` §9 之同一口径）：本件**不自写入**自身 SHA-12／bytes
（填入即改本件内容 ⇒ 其指纹随之变）⇒ 该二项之**盘上实测值载于交付回执**与姊妹件。下表为
**内容无关之字节属性**，可在本件内如实自报且恒真。

| 项 | 本件自报 | 要求 | 判 |
| :-- | :-- | :-:| :-: |
| 落盘方式 | Python `io.open(..., encoding='utf-8', newline='\n', errors='strict')` **直写** | ⛔ 0 经 PowerShell 管道中转 UTF-8 正文 | ✅ |
| Windows 路径 | **一律 raw 字符串** | —— | ✅ |
| SHA-12 | *（见交付回执 · 姊妹件）* | —— | ⚠ 不可自含 |
| bytes | *（见交付回执 · 姊妹件）* | —— | ⚠ 不可自含 |
| BOM | **False** | False | ✅ |
| CRLF | **0** | 0 | ✅ |
| CR | **0** | 0 | ✅ |
| TAB | **0** | 0 | ✅ |
| 其他控制字符（含 0x7F） | **0** | 0 | ✅ |
| U+FFFD | **0**（以 `chr(0xFFFD)` 构造探针计） | 0 | ✅ |
| key 形态扫描（落盘前·正文级） | **0 命中** | 0 | ✅ |

---

## §10 诚实交代（failures ＆ limitations · 判死不软化）

1. **`T3` 三格终判本棒 ⛔ 0 预判**：可答化成就与新读数已产出，但**终判转正与否属 verdict-keeper**；
   本棒只出读数与缺陷登记（沿 v18 派生动作 B 之落账件纪律）。
2. **本面非全族面**：`T2` 之残余越界（`0.10873>0.1`）**0 重测**；全族证书面**仍在册违反**。
3. **`S̄` 最小余量 `0.01574` 薄**：叠加同 seed 内非确定（`KD-T3-A1`）⇒ **⛔ 0 以单次读数充稳健结论**。
4. **机制对比面 0 判别力**：LLM 臂读数之输入**与机制无关**（三格 prompt 逐字相同）⇒ 本面之机制间差异
   **仅**来自端点非确定，**⛔ 0** 解读为机制效应。
5. **设计面未解项沿在册登记**：基线 oracle 饱和（`KD-T3-A3`）、`KL-M41-3` 读数面（`KD-T3-A2`）、
   `33` 之宣告面、`ε` 之 prereg 固定（M-41 `KD-5`/`BL-2`）——**本棒⛔ 0 棒自调**。
6. **并发写入如实交代**：全盘写后复测（`tools/`+`results/` 共 882 件）显示本棒之外另有 **1 件**变动
   —— `results/_t3trap_kd3_bprime_effect_register_2026_10_15.md`（mtime `2026-10-15T17:20:10+08:00`，
   晚于本棒基线 `17:17:35`）⇒ **系姊妹棒（B′ 生效落账棒）之并发写入，非本棒所写**；
   **本棒对既有件之唯一写入 ＝ `tools/exp_harness.py` 之授权面**。

---

*件止。**T3_Trap 可答化执行件**（worker）· 2026-10-15 deposon 链——**FTFB**：判死线冻结
`17:17:18` ＜ harness 写入 `17:17:49` ＜ 测量 `17:21:54`。**改动**：3 hunk（docstring 注记＋
`clues` 表＋prompt 行），反演复原 sha `7957bac14455` 逐字节吻合，**他族 prompt 逐字不变**。
**重测**：45/45 call 全有效、0 拒答、`KL-M41-1` 未触发；`D=2/15`／格；`S̄` ＝ 0.08426／0.07702／0.04537
（皆 ≤ `τ_cert=1/10`）。**⛔ 0** 宣告证书成立、⛔ 0 预判 `T3` 三格终判、⛔ 0 代 PI 裁、⛔ 0 宣告①毕、
⛔ 0 回改任何既有件（除授权面）、⛔ 0 经手 key（key 仅自 runtime env 读入 client 内部·落盘前扫描 0 命中）。
全部产出**候 PI 核准**，⛔ **0 径行采认**。署名：**worker**。*
