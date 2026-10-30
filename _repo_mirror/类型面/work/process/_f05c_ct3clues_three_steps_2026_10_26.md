# `F-05`③ 之三步（联网／外委／消融）：轨迹面正解集 `C_T3_clues` 之实体 —— **已找到并经三重机验**

**棒** `F05C-CT3CLUES`｜**拟稿** protocol-keeper（口径与预登记官）｜**日期** 2026-10-26｜**性质** 🔴 **取数＋复原件（非判定件）**
**令源** PI 2026-10-26 裁 242「`F-05`③ 走完五步后三步」（依裁 226：核盘→联网→预实验→外委→消融实验；仍无则交 `verdict-keeper` 终判）
**裁面归属** PI（⛔ 0 代裁）｜**终判权属** `verdict-keeper`（⛔ 0 代落）｜**观测时点** 2026-10-26 16:0x–17:2x（GMT+8）
**skill（实带）** `evidence-contract` ＝ `〔本地路径已脱敏〕`（本棒加载取其律：claim 分级＋证据锚＋「找不到 claim ID 则上报而非猜」；弃其载体——本工程无 `paper/paper.md` 链）
**本件唯一新件 ＝ 本件**（落位 `results\work\process\`；落盘前 `Test-Path` ＝ **False**）；**既有件触动数 ＝ 0**
**本棒 0 外委 · 0 自行外发 · 0 改／移／改名／删任何既有件 · 0 读 `〔本地路径已脱敏〕` · 0 读归档区正文（仅按名与指纹认人）· `deposon-sub` 只读不读正文 · 0 读 key**
**本棒联网 1 记（见 §2）· 本棒跑「预实验／消融实验」＝ 本地重放核（0 调用 LLM、0 外发、0 落盘至 `results\`）**

---

## §0 一行式

**找到。** 轨迹面正解集 `C_T3_clues` 之实体＝登记面所载 OLD hunk（**546 B／8 行／sha-256[:12] `cf22f72eaebb`**）之**逐字本体**，已自登记链之 diff 照录**逐字重建**并以**同一指纹逐位坐实**；其正解映射（`greedy→Option A`、`deposit/cost→Option B`）另经**三 seed 面级 digest12 逐位复现（3/3）**与**逐 prompt `correct` 序列逐位相符（3/3）**双重机验。**三步之内已闭 ⇒ 未至外委（末阶）。**

- **联网**：有果 —— 公开面**无**同源题库（检索式① 0 相关命中）；上游公开仓 `zeroandcat/Deposon` 之镜像**含登记链两件且与本地逐位同** ⇒ 复原之取源**公开可独立复核**。
- **外委**：无果亦无必要（所缺已闭，未至末阶）；**⛔ 0 自行外发**。
- **消融**：有果 —— 剥维①（剥字节窗／按内容＋逐字重建）**命中**；剥维②（剥名／只按指纹）**0 命中**；剥维③（剥根／扩域按名）**0 命中**（新增在册载体 OLD 侧 `.pyc`）；剥维④（剥至构造面＋机验复现）**3/3 逐位相符**。

---

## §1 缺什么（回源复核）

| 项 | 登记／在册所载 | 本棒直算 | 判 |
|:--|:--|:--|:-:|
| **hunk 之登记面** | `results\review\audit\_material_expansion_drift_authorized_register_2026_10_16.md` 15,044／`edf98dc7da62` | 15,044／`edf98dc7da62` | ✅ MATCH |
| **第一棒出据** | `results\work\process\_f05_data_fetch_2026_10_26.md` 21,398／`d19731286f46` | 21,398／`d19731286f46` | ✅ MATCH |
| **10-15 执行件**（登记链中段·本棒复原之取源） | 31,808／`b9e9c9b5a06b` | 31,808／`b9e9c9b5a06b` | ✅ MATCH |

**登记面 L56 逐字**（`edf98dc7da62`）：

```
| `C_T3_clues` | `cf22f72eaebb` | 546／8 | `b913b9910f29` | 4,205／55 | +3659 |
```

⇒ **所缺者** ＝ OLD 侧之实体：546 B／8 行／sha-256[:12] ＝ `cf22f72eaebb`。

**本棒之复核（扫描 v3·token 锚定·完备法）**——四根合计 **6,257 件**（repo_plain **4,739**（读 4,738／675,789,280 B）＋仓内归档区 **240**（41,498,718 B）＋`deposon-sub` **1,275**（61,704,837 B）＋回收站 **3**（89,559 B）），耗时 17.1 s；**未读之 1 件已补扫**（`.tmp\kdcensus_20261020_ea_data.json`，**286,347,176 B／`0de1aec6020d`**，>120 MB 阈值故首轮跳过）——其 clue 串 **0** 命中（`C_T3_clues` ×634）⇒ **不可能含 OLD hunk** ⇒ 覆盖 **6,257／6,257**：

| 测项 | 结果 | 正控 |
|:--|:--|:--|
| 目标文件指纹 `7a097d7802d1`／`d5c8d676bb5b`／`7957bac14455`／`275e480ba4d9`／`0f8532aefdff`／`b913b9910f29`／`cf22f72eaebb` | **四根皆 0 命中** | 正控 **6 枚命中**（`ce64b9b97489`×2／`edf98dc7da62`×2／`b9e9c9b5a06b`×2／`ff5ed4b0e329`×1／`46260e3b8426`×1／`d19731286f46`×1） |
| 字节窗 546 B→`cf22f72eaebb`／4,205 B→`b913b9910f29` | **0 命中**（token 锚定法：OLD hunk 必含 `take the fast route`，NEW hunk 必含 `hidden-carry` 等 ⇒ 只验含 anchor 之窗口，完备） | 同上正控证明仪器非假阴性 |
| 内容 token | `C_T3_clues` **67** 件（66＋大件 1）／`take the fast route` **15**／`play the balanced line` **13**／`deposit all 3 units into the growth` **13**／`random.choice(['greedy', 'deposit', 'cost'])` **8** | —— |
| 按名（`harness`／`t2b`／`snapshot`／`exp_harness`／`three_seed`） | repo **29**／`deposon-sub` **1**／归档区 **0**／回收站 **0** | —— |

⇒ **复核结论**：与第一棒相符——**登记面在盘；文件级实体不在盘**。惟本棒另得：**该实体可自登记链逐字复原**（§4 剥维①④），故「缺」之性质由「不可得」改判为**「可复原」**。

**口径声明（区分于阈值调整）**：以上「0 命中」为**实测态之登记**，非任何阈值之设定或调整；本棒未改任何 `TH-*`／`K-*` 字面。

---

## §2 联网（检索式与取回）

**解禁依据**：PI 2026-10-26 裁 242 本面解禁「可联网」；旧「⛔ 0 联网」于此作废，余铁律不动。

| # | 检索式／动作 | 结果（取回字面） |
|:-:|:--|:--|
| 1 | `"Trap scenario" "type=greedy" "play the balanced line" "net 6"`（web_search，8 结果） | **0 相关命中**：返回皆为噪声（fighting-game「Character archetypes」、greedy-assignment 博客、sample pack、DND trap 名表、balance-loop 谜题、剧情「诱饵」等）⇒ **公开面无同型题面／题库** |
| 2 | `deposon benchmark github "exp_harness.py" T3 trap clues` | 命中 `https://github.com/zeroandcat/Deposon/blob/main/README.md`；取回字面：「**Deposon (凝子) An auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths. · Paper: arXiv:2609.09001 · License: MIT**」 |
| 3 | 通道实测 | `raw.githubusercontent.com` **不可达**（TLS「基础连接已经关闭」×2）；`api.github.com` **可达** ⇒ 改走 contents API（base64 解码） |
| 4 | 上游全树枚举 `GET /repos/zeroandcat/Deposon/git/trees/main?recursive=1` | **3,573 entries**、`truncated=false`；harness 相关 **7** 条；T3/trap 相关 **22** 条 |
| 5 | 上游 `tools/exp_harness.py` 提交史 `GET /commits?path=tools/exp_harness.py` | 仅 **2** 条：`1b75311677`（2026-09-17T15:34:04Z）、`29f6fd264f`（2026-09-20T05:07:04Z）——**皆早于 10-15** ⇒ **轨迹面版（10-15 17:17:49 写入）不在上游该路径历史** |
| 6 | 上游镜像 harness 取回并直算 | `_repo_mirror/source/tool/exp_harness.py` ＝ **45,590／`ce64b9b97489`** ＝ 本地现行件**逐位同** ⇒ 上游公开面**不含** OLD harness |
| 7 | 上游镜像**登记链两件**取回并直算 | `_repo_mirror/verdict/kd/_t3trap_answerable_build_exec_2026_10_15.md` ＝ 31,808／**`b9e9c9b5a06b`**；`_repo_mirror/verdict/pi/_material_expansion_drift_authorized_register_2026_10_16.md` ＝ 15,044／**`edf98dc7da62`** ⇒ **与本地逐位同** ⇒ 本棒复原之取源**在公开面可由他方独立复核** |

**来源之性质（裁定）**：`C_T3_clues` 之正解集**非源自任何公开数据集，亦非某 tool 之 clue 文件格式**——系**本仓自撰之合成构造**（三型题面皆自撰）。依据：①本棒独立复检（检索式① 0 相关命中）；②在册来源件 `results\evidence\register\_material_expansion_sourcing_2026_10_16.md` §1.3 逐字载「T3 向联网**未获任何许可清晰且构造同源之题**…公开面无同型题库」（该件之联网通道与检索式清单见其 §5；T2／T4 之 MIT 外源仅及于 T2 20 条与 T4 5 博弈，**不及于 T3**）。

**联网步之净得**：**未取回实体本身**（上游无轨迹面版）；**取回的是「登记链可公开复核」之证明**——即本棒复原链条（登记件＋执行件）之二环皆在公开面且与本地逐位同。

---

## §3 外委（委件草案，若须）

**本棒判定：⛔ 0 外委、⛔ 0 自行外发。** 依裁 226 之序，外委为**末阶**；本棒于第一阶（核盘＋复原）即闭所缺，故未至外委面。

**候 PI 裁之备位（⛔ 0 自发）**：若 PI 另裁须委，所托将限于一项——「于上游公开仓 3,573 件中逐件取回并验指纹，以证 OLD harness（`7a097d7802d1`／15,708 B）之文件级实体是否曾入上游任一历史版本」；**代价不对称**：该径须 3,573 次网络取回（配额与耗时皆高），而**所缺者已闭**，故其收益仅及于「文件级实体之附证」，不及其缺；**本棒不代 PI 择**。

---

## §4 消融（剥维表）

| 剥维 | 剥什么／方法 | 命中差 | 结论与射程 |
|:-:|:--|:--|:--|
| **①** | **剥「hunk 字节窗」** → ①改按**内容关键词**搜；②自登记链之 diff 照录**逐字重建**再以指纹验 | 字节窗 0 → 内容面 **`take the fast route` 15 件**、正解映射行 **8 件**；重建：**重建区（1,855 B／30 行／`95ca9dc92363`）内 offset 877 处 546 B 窗 sha-12 ＝ `cf22f72eaebb`、546 B、8 LF 行 —— 三参数与登记面逐位相符** | **命中**。所得＝**OLD hunk 之逐字实体**（正解映射所在之 8 行）。**射程**：限于 OLD 侧该 8 行＋其三型 clue 全文（939 B／12 行／`a958c51074ff`）；⛔ 0 及于整份 harness |
| **②** | **剥「名」** → 只按**指纹**（whole-file sha-256[:12]），四根 6,257 件 | 目标 7 枚 **0 命中**；正控 **6 枚命中** | 文件级实体**确不在盘**（仓／归档区／`deposon-sub`／回收站）。**射程**：仅证「无此文件」，不证「无此字节窗」（该由剥维①治） |
| **③** | **剥根** → 扩至 `.tmp`／`deposon-sub` 按名／归档区按名／回收站／**上游公开仓** | 按名：repo 29／`deposon-sub` 1／归档区 0／回收站 0；上游 0（镜像为现行件，`7a097d7802d1` 不在其路径历史） | 0 命中。**附带在册载体（新增登记）**：`.tmp\whitelist_backup_2026_10_17\__pycache__\ref_exp_harness_OLD_2026_10_15.cpython-314.pyc`（**20,742／`3cfcd753dbdf`**；头：timestamp-based，源 **13,342 B**、mtime **2026-10-15 17:19:10**、`co_filename` ＝ `…\.tmp\whitelist_backup_2026_10_17\ref_exp_harness_OLD_2026_10_15.py`）——其 `TrapTask.generate_prompts` 常量逐字含 **`('greedy','deposit','cost')`**、`'Option A'`、`'Option B'`、`'Trap scenario '`、`'). Which option?'`，而 **0** clue 串 ⇒ 系 **10-15 可答化之 OLD 侧**（13,342 B ＝ 登记之 `7957bac14455` 之字节数），**非**轨迹面版（`7a097d7802d1`）⇒ 轨迹面版之编译码载仍不在盘 |
| **④** | **剥至「构造面＋机验复现」**（不靠检索，靠**行为**）：以复原之 OLD 三型代码重放，逐 seed 比对轨迹面 | **T3 面级 digest12：3/3 逐位相符**（`68dc2160aff4`／`420381d7ea4e`／`4e093712b425`）；**逐 prompt `correct` 序列：3/3 逐位相符**（`BAABBBABAAABABA`／`BAABABAAABAABBB`／`AAABBBBABBBBBAB`）；**T1 正控：3/3 相符**（`45b6f507342b`／`d4a3c7dcc854`／`8fcb322f32e8`） | **决定性命中**。⇒ 复原体**不仅逐字相符，且行为等价于轨迹面**（三 seed 全面面）。**射程**：T3 族三型之正解集与面；⛔ 0 及于 T2／T4／T5 之面（现行件与轨迹面之 digest 0/3 相符，差异归因见 §8） |

**复原所得实体之逐字（546 B／8 行／`cf22f72eaebb`）**：

```
            'cost': ('Two rounds remain. Option A: take the fast route, which pays 4 this '
                     'round but charges a service cost of 1 in each of the two rounds '
                     '(net 2). Option B: take the slow route, which pays 3 this round '
                     'and charges no service cost (net 3). ')
        }
        for i in range(n):
            trap = random.choice(['greedy', 'deposit', 'cost'])
            options = ['Option A', 'Option B']
            correct = 'Option A' if trap == 'greedy' else 'Option B'
```

⇒ **正解集之正解映射逐字在实体之内**：`greedy→Option A`；`deposit`／`cost`→`Option B`（`else` 支 ⇒ 两者皆 B）。

**三型 clue 全文**（`a958c51074ff`，939 B／12 行）与现行载体之逐字对照：`tools\exp_harness.py` L463–L512 载 15 型 `clues`（含原三型）＋ L514–L522 载 `t3_answer` 15 型；其中 **`cost` 条目（L471–L474）与复原体之 `cost` 条目归一化尾逗号后逐位同（差异行 0）**，`t3_answer` 之三型子集（`greedy:'Option A'`、`deposit:'Option B'`、`cost:'Option B'`）与复原体之映射行**逐位同**。

**轨迹面读数面（对验之一手源，在盘）**：`.tmp\three_seed_measurement_2026_10_16.json`（226,256／`ff5ed4b0e329`）之 `detail` 720 条（`T3_Trap` **135** 条；逐 prompt 真值 45 格）＋ `digest_by_seed_family` 之 T3 三枚；其**版绑定**在 `.tmp\three_seed_freeze_2026_10_16.json`（10,536／`46260e3b8426`），该件载 `tools/exp_harness.py` 之 sha-12 ＝ `7a097d7802d1`、mtime ＝ `2026-10-15T17:17:49` ⇒ **读数面与轨迹面 harness 之绑定在盘**。另 `.tmp\t3_nt_measurement_2026_10_15.json`（10-15 17:21 实测于 17:17:49 之 harness）45 条逐 prompt `type`＋`correct`：type 分布 `greedy` 24／`cost` 21，**与复原映射相符 45/45、0 不符**。

**可复现路径（脚本皆在 `.tmp`·参数与种子记明）**

| 脚本 | 产出 | 关键参数 |
|:--|:--|:--|
| `.tmp\_f05c_recon_2026_10_26.py` | `_f05c_recon_out_2026_10_26.json` | 自执行件之 ```` ```diff ```` 围栏取 NEW 侧（去 `+` 前缀）逐字重建；546 B 窗滑扫 |
| `.tmp\_f05c_replay_2026_10_26.py` | `_f05c_replay_out_2026_10_26.json` | 现行件逐族 digest（口径 B）＋对 `ff5ed4b0e329` 之 `digest_by_seed_family` |
| `.tmp\_f05c_oldreplay_2026_10_26.py` | `_f05c_oldreplay_out_2026_10_26.json` | **决定性重放**：seeds **42/123/456**；口径 B（单 seed 依 `task_families` 之序逐族生成，n：T1–T4=15／T5=20）；`digest12 ＝ sha256(json.dumps(prompts, ensure_ascii=False, sort_keys=True).encode("utf-8"))[:12]`；OLD T3 代码逐字取自复原体 |
| `.tmp\_f05c_scan3_2026_10_26.py` | `_f05c_scan_out_2026_10_26.json` | 四根扫描；token 锚定字节窗 |
| `.tmp\_f05c_xcheck_2026_10_26.py`／`.tmp\_f05c_pyc_codes_2026_10_26.py`／`.tmp\_f05c_bigfile_2026_10_26.py` | `_f05c_xcheck_out…json`／`_f05c_pyc_codes…json`／`_f05c_bigfile_out…json` | 逐字对照；`.pyc` code object 常量；>120 MB 大件补扫 |

---

## §5 结论

**RESULT ＝ 找到。**

1. **实体**：轨迹面正解集 `C_T3_clues` 之 OLD 侧实体＝**546 B／8 行／sha-256[:12] `cf22f72eaebb`**，逐字见 §4；其正解映射逐字在实体之内。
2. **三重机验**：①**指纹**——重建体之三参数（546 B／8 行／`cf22f72eaebb`）与登记面 `edf98dc7da62` L56 逐位相符；②**行为**——三 seed 面级 digest12 **3/3** 逐位复现轨迹面；③**逐格**——逐 prompt `correct` 序列 **3/3** 逐位相符、45 格 `type`×`correct` 与映射 **45/45** 相符。
3. **外推边界**（构造面判定）：本结论之射程 ＝ **「OLD harness `7a097d7802d1` 之 T3 族三型正解集与 T3 面」**；⛔ **0** 及于整份 harness 之他族（`T1` 除外——其三 seed digest 与轨迹面相符）、⛔ 0 及于 `T2`／`T4`／`T5` 之面（现行件与轨迹面 0/3 相符）、⛔ 0 及于 **NEW 侧 hunk `b913b9910f29`（4,205 B／55 行）之实体**（仍不在盘，见 §7）、⛔ 0 及于载判件 `d970bb175672` L150 所问「复跑 `R_ITT` 0 可比」之真伪（⛔ 0 判其真、⛔ 0 判其伪）。
4. **未闭之别项**（须 PI 知悉）：**整份 OLD harness `7a097d7802d1`（15,708 B）之文件级实体**仍不在盘（上游亦无）——惟**所缺者（`C_T3_clues` 之实体）已闭**，二者非同一物。
5. **⛔ 0 落终判**：本件不落 `pass`／`af`／`kd`／`fail`／`give-up`（终判归 `verdict-keeper`），⛔ 0 闭任何 `KD`，⛔ 0 宣告「复跑 0 可比」之结论成立或不成立，⛔ 0 代 PI 裁，⛔ 0 代销记。

---

## §6 尽力度与正控

**五步（依裁 226）之尽力度**：①**核盘**——四根 6,257 件全量逐件（指纹＋按名；仓内件加内容与字节窗）＋登记链三件回源复核；②**联网**——2 条 web 检索式＋1 条 GitHub API 提交史＋1 次全树枚举＋3 件取回并直算；③**预实验**——本地重放核（**0 调用 LLM**、0 外发、0 落 `results\`）；④**外委**——**未至**（末阶，所缺已闭）；⑤**消融实验**——剥维①–④（§4）。

**正控（阴性断言之自证）**：①**仪器正控**——同口径对已知指纹命中 **6 枚**（`ce64b9b97489`／`edf98dc7da62`／`b9e9c9b5a06b`／`ff5ed4b0e329`／`46260e3b8426`／`d19731286f46`），而目标 7 枚 0 ⇒ 0 命中系真阴性；②**行为正控**——重放之 T1 三 seed digest 与轨迹面**逐位相符**（3/3）⇒ RNG 入口态与口径 B 正确，故 T3 之 3/3 相符非抽样波动；③**交叉正控**——独立之 OLD 侧 code object（`.pyc`）载 `('greedy','deposit','cost')`／`Option A`／`Option B`，与复原体之映射行同源一致；④**外部正控**——上游取回两件与本地**逐位同**（字节数＋sha-12 双向相符）。

---

## §7 未核之面

1. **归档区正文／`deposon-sub` 正文**：⛔ 0 读（仅按名与指纹）⇒ 「OLD hunk 之 546 B 字节窗是否嵌于该二区之某他件（非整文件、且其内容不在我方 token 集内）」**未穷尽**；若 PI 欲闭此面，须授权一次内容级扫描（或授权正文开卷）。
2. **回收站**：3 件，按名与指纹已扫；该根未获正控命中（该根仅 3 件，正控件不在其中）⇒ 其 0 命中为「该具体件不在该根」之真阴性，但**该根之仪器自证不足**。
3. **上游公开仓**：仅枚举路径（3,573）与取回 3 件；**未**逐件取回验指纹 ⇒ 「上游 3,573 件中是否另有含 OLD hunk 字节窗之件」未穷尽。
4. **NEW 侧 hunk** `b913b9910f29`（4,205 B／55 行）之实体：**仍不在盘**（字节窗 0 命中）⇒ 第四层 NEW 之 `clues` 15 型＋`t3_answer` 之逐字本体未复原（惟现行载体 L463–L522 载其**后继**形态）。
5. **整份 OLD harness `7a097d7802d1`**（15,708 B）之文件级实体：仍不在盘（仓／归档区／`deposon-sub`／回收站／上游 皆 0）。
6. **10-18 层**（现行 `ce64b9b97489` 相对 10-16 之 `d5c8d676bb5b`）之变更登记件：**未开卷**（与本缺无关，仅记未核）。
7. `.tmp\t3_harness_diff_2026_10_15.diff`（原始 diff，`0f8532aefdff`／3,463 B）**已不在盘** ⇒ 本棒复原之取源为**在册执行件之逐字照录**（非原始 diff 文件），故复原体之权威性系于「照录件逐字」＋「指纹逐位命中」**双重**。

---

## §8 本件之限

1. **⛔ 0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up`）；**⛔ 0 闭任何 `KD`**；**⛔ 0 宣告**「复跑 `R_ITT` 0 可比」之真伪（载判件 `d970bb175672` L150 明禁）；**⛔ 0 代 PI 裁**；**⛔ 0 代销记**。
2. **重放之口径与射程**：口径 B（单 seed 依 `task_families` 之序逐族顺序生成；n：T1–T4=15／T5=20；`digest12` 式见 §4）；OLD 之 `T2` 族正文不在盘（其 RNG 消耗与现行 `T2` 等价之说，系在册复跑件 `_t3_repro_probe_2026_10_16.md`（`1a104886964f`）之层间重放结论；本棒**以 T1 正控 3/3 间接坐实**该入口态）⇒ **T2 正文本身未复原**。
3. **现行件与轨迹面之差异归因（本棒不裁）**：现行件 T2／T3／T4／T5 四族 digest 与轨迹面 **0/3 相符**（T3 归因于「3 型→15 型」之 `random.choice` 取域变更）；此为**归因之登记**，⛔ 0 据以裁任何 `KD`。
4. **本棒 0 联网取回实体本身**：上游未含轨迹面版（§2-5、§2-6）⇒ 联网步之净得为「登记链公开可复核」之证明，非实体之取回。
5. **本件 0 落派生 JSON**（⛔ 派生 JSON 不合并）：除本件与 `.tmp\` 之脚本/产出外，**0 新件**；⛔ 0 改／移／改名／删任何既有件。
6. **与在册之关系**：本件不改任何在册路径字面；§1 所载「登记面三参数」与 §4 所载「复原体三参数」之相符，系**独立直算**（本棒自算），非沿用他件自报。

---

**状态行**：**拟稿完成·待 PI 复核**（本件为取数＋复原件；⛔ 0 落终判、⛔ 0 闭 `KD`、⛔ 0 代裁）｜**所缺已闭**（`C_T3_clues` 之实体：找到）｜**余项**：整份 OLD harness 之文件级实体、NEW 侧 hunk 之实体（§7-4、§7-5）｜**未至外委**（末阶）｜**外推边界**＝ 构造域（OLD harness 之 T3 三型正解集与 T3 面）｜**既有件触动数 ＝ 0**

**落款**：`F05C-CT3CLUES`·protocol-keeper（口径与预登记官）· 2026-10-26 16:0x–17:2x (GMT+8)·**本件为取数＋复原件**：⛔ 0 落终判·⛔ 0 代 PI 裁·⛔ 0 代销记·⛔ 0 改任何既有件·⛔ 0 读 GLM／归档区正文／`deposon-sub` 正文。

RESULT: 找到 —— 轨迹面正解集 `C_T3_clues` 之实体（OLD 侧 546 B／8 行／sha-12 `cf22f72eaebb`）已自登记链逐字重建并经**指纹逐位命中 ＋ 三 seed 面级 digest12 复现 3/3 ＋ 逐 prompt `correct` 序列相符 3/3** 三重机验；整份 OLD harness 之文件级实体仍不在盘（不在本件所缺之射程）。
