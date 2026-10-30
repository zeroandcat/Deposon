# `B-F` 动作组合面 · CP（约束规划）体例正文来源件 · 2026-10-24

> **件性质**：**体例来源件**（裁 19 之落地）—— 就 PI 裁「动作组合**属**本实验面，须采 CP 体例」（裁 15）所遗留之「体例无据」缺口，取 `cumulative`／`precedence` 之**正文**（定义＋形式化写法），并核其与本案 `3 steps`／cost-bounded 之关系。
> ⛔ **0 回改**他件一字｜⛔ **0 移动／重命名／删除**｜⛔ **0 新建目录**｜⛔ **0 跑实验**｜⛔ **0 调 LLM／API**（检索器与 arXiv API 属**取文献**之工具）｜⛔ **0 读** `〔本地路径已脱敏〕`｜⛔ **0 读归档区正文**（仅按名与计数）｜⛔ **0 落**五终判｜⛔ **0 闭** `KD`｜⛔ **0 宣告**段毕或门槛成就｜⛔ **0 代 PI 裁**｜**实携 skill 0 个**（如实登记）｜**观测窗** 2026-10-24 19:29–19:41 UTC+8（窗内锚点：arXiv API 回执 `<updated>2026-10-24T11:34:57Z</updated>`）。
> 📌 **前棒**：阶② `c6d2e7dbb004`／56,078 B（其 `F5` 之 IBM URL **fetch 403**）｜阶③ `e168c6f0ebec`／44,097 B（其 §6 自陈「该来源本棒未获正文」）—— 本棒**⛔ 0 回改**其一字，仅**接续**。
> 📌 **代号首现即附其义之白话**：`cumulative`＝累积约束（同时进行之任务，其资源需求总和在任一时点不得超该资源之容量）｜`precedence`＝先后约束（两活动在时间上相对位置之限制）｜`cumulFunction`＝累积函数表达式（以时间之函数表示资源占用剖面之构件）｜`cost-bounded`＝代价有界（解之动作代价总和不得超给定界之赛道体例）｜`FEAS`＝外委件之可行集判定函数｜`UPDATE`＝外委件之状态递推函数。

## §0 一句话

**取到**：`cumulative` 逐字定义（IBM 官方 ＋ MiniZinc 官方 ＋ 学术公式）、`precedence` 逐字定义（IBM 官方八式）、并施之可入模型写法（IBM OPL 逐字代码）。**未取到**：IBM 页**直接 fetch**（403，正文经**检索器抽取**同 URL 得）、IBM 页内**以图渲染之公式**（公式面改由学术承担）、IBM 之 `cumulative`／`precedence` **单一全局约束关键字页**、MiniZinc 之调度 `precedence` 谓词、OR-Tools 文档（超时）。

## §1 令源（裁 15 ＋ 裁 19）

| 项 | 逐字 | 出处 · 位置 |
|:--|:--|:--|
| **裁 15** | 「**PI 之裁**：属，须采 CP 体例。」 | `pi_rulings\_pi_card_answers_register_2026_10_24_v285.md` §2-3（其 §1 表载「\| 15 \| **`B-F` 动作组合是否属本实验面** \| **乙：属**（须采 CP 体例） \|」） |
| **裁 19** | 「\| 19 \| `B-F` 组合体例来源 \| **甲：联网取 CP 正文** \| 同荐 \|」 | `pi_rulings\_pi_card_answers_register_2026_10_24_v287.md` §1 第 22 行（§4 第 73 行载「\| T-5 \| **联网取 CP 体例正文**（裁 19 之落地） \|」） |
| **阶③ 缺口自陈** | 「若 PI 明定组合属本实验面，则取 CP 之 `cumulative`／`precedence` 体例——⚠ 该来源（**IBM CPLEX／`F5`**）**本棒未获正文** ⇒ ⛔ **0** 逐字引其语义。」 | 阶③ `e168c6f0ebec` §6 ②第 5 条（第 270 行） |
| 阶③ 步限面 | 「`only 3 steps may be spent`（17/17 格恒 3）＝ **cost-bounded**：「动作序列之代价之和 ≤ 3」；⛔ **`3` 仍是本案之字面值**，⛔ **0** 称其为文献值。」 | 同上 §6 ②（第 268 行） |

📌 裁 15 已定「组合**属**本实验面、须采 CP 体例」，裁 19 已定「联网取 CP 正文」之一途 ⇒ 阶③ §6 之 ⛔（未获正文 ⇒ 不得逐字引）之**触发条件**在本棒内解除；本棒**不裁**新事项，**只供正文**。

📌 **四根**（写死；实枚举件数本棒实测）：`deposon-repo`（工作根 · 唯一写入面）**7,591**｜`deposon-sub`（只读 0 写）**1,275**｜`〔归档区〕`（仅按名与计数）**40,242**｜`〔本地路径已脱敏〕`（运行时只读自测）**103,879**。**同批正控**：`tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`**（双通道一致）⇒ 与派工单**逐位相符** ✅；⛔ 0 用内建 `hash()`，⛔ **0 跑**其任何 `run()`。R3 之 40,242 与阶③ 全等；R1 由 7,489 增至 **7,591**；R4 103,879——⛔ 0 就此增量作逐件对账（如实登记）。

## §2 检索式与命中（逐条）

- **S1** `IBM CP Optimizer documentation cumulative function scheduling "cumulative" constraint task demand capacity` → **10** 命中；采 IBM 官方 8 条 → A1／A2／A3。
- **S2** `IBM CP Optimizer documentation "Precedence constraints" scheduling interval variables precedence constraint` → **8** 命中；采 IBM 官方 3 条 → D1／D2。
- **S3** `IBM CPLEX Optimization Studio OPL keyword "cumulative" constraint scheduling cumulativeTask cumulativeResource capacity demand` → **6** 命中；采 IBM 官方 5 条 → A3／A4。
- **S4** `MiniZinc global constraint "precede" specification precedence x + 1 <= y std library documentation` → **6** 命中；**弃**：全为**字典序**约束。
- **S5** `MiniZinc documentation global constraint cumulative tasks capacity demands minizinc.org std library` → 产物 224,863 B；→ B1。
- **S6／S7／S8**（arXiv 逐定义式二条 ＋ OR-Tools `AddCumulative` 式一条）→ 各 **0** 命中；三次皆工具侧失败 `MATRIX_TOOL_REQUEST_FAILED`。

**直取（`web_fetch`）**：IBM 之 `icos/22.2.0`／`icos/22.1.0`／`SSSA5P_22.1.1`／`SSSA5P_22.2.0` **一律 403**；MiniZinc 两路径 **404**；OR-Tools 两页 **两次均超时**；阶② `F5` 之 `icos/20.1.0?...` 本棒**未**直取 ⇒ **阶②之 403 记载依然为实**。**成功**：F5／F6 `ar5iv.org/abs/{2508.01751,2602.15635}`（各约 79／81 k token，**中段被工具上限截断**）；F7 `export.arxiv.org/api/query?search_query=all:"cumulative constraint" AND all:"scheduling"&max_results=10`（回执 `totalResults` ＝ 5）。
📌 **取文径（须与「直取」分记）**：IBM 官方正文**非直取**（直取 403），系由检索器抽取**同一 IBM 官方 URL** 之页面正文（回执 `source: IBM`；22.2.0 与 22.1.1 两页经**同题之土耳其语／保加利亚语镜像 URL** 抽取英文正文）⇒ 所引 IBM 文字**为官方文档正文**，而**取得径为检索器抽取**。MiniZinc 正文经 S5 命中 **2.5.2** 文档页；学术正文经 F5／F6／F7 **直取成功**。

## §3 `cumulative` 之逐字定义

> `cumulative`（累积约束：同时进行之任务，其资源需求总和在任一时点不得超该资源之容量）——**A**＝IBM 官方｜**B**＝MiniZinc 官方全局约束库｜**C**＝学术。**A**／**D** 各条之取得径＝检索器抽取（直取 403，详见 §2 末段）。

| # | 来源 · 页内位置 | URL | 时点（UTC+8） |
|:-:|:--|:--|:--|
| A1 | IBM「Cumulative functions」· 节「Cumulative functions」首段、节「Constraints on cumul function expressions」 | `https://www.ibm.com/docs/en/icos/22.2.0?topic=scheduling-cumulative-functions` | 19:29–19:31 |
| A2 | IBM「Cumul functions in CP Optimizer」· 节「Constraints on cumul function expressions」、「Semantics」 | `https://www.ibm.com/docs/en/icos/22.2.0?topic=c-cumul-functions-in-cp-optimizer-1`（正文取自同题 `tr` 镜像，**英文正文**） | 19:31 |
| A3 | IBM `cumulFunction` OPL 关键字页 · 节「Syntax」 | `https://www.ibm.com/docs/en/icos/22.1.0?topic=keywords-cumulfunction` | 19:30–19:31 |
| A4 | IBM house-building 教程 · Note「Cumulative function expression」、节「Step 4／6／7」 | `https://www.ibm.com/docs/en/icos/22.1.1?topic=studio-using-cumulative-functions-in-house-building-problem`（经同题 `bg` 镜像抽取） | 19:31 |
| B1 | MiniZinc **2.5.2** 官方文档 · 节「**4.2.1.7. Scheduling constraints**」 | `https://www.minizinc.org/doc-2.5.2/en/lib-globals.html` | 19:32 |
| C1 | Sidorov《On inferring cumulative constraints》（CP 2026）／arXiv:2602.15635 · 节「**2.1 Constraint programming**」·**Definition 1** | `https://arxiv.org/abs/2602.15635`（全文经 `https://ar5iv.org/abs/2602.15635` 直取，**成功**） | 19:34:57（arXiv 回执 `<updated>`） |

**A1**

> "In scheduling problems involving cumulative resources (also known as renewable resources), the cumulated usage of the resource by the activities is usually represented by a function of time."
>
> "alwaysIn(f, u, v, hmin, hmax) means that the values of function f must remain in the range [hmin, hmax] everywhere on the interval [u, v)."

**A2**

> "f ≤ p means that the maximum value taken by f on the whole horizon is less than or equal to p"

（同页另载：post 于累积函数之约束会**自动加入隐含约束** `f>=0`。）

**A3**

> "Syntax cumulFunction f = pulse(u,v, h); cumulFunction f = pulse(a, h); cumulFunction f = pulse(a, hmin, hmax); cumulFunction f = step(u, h); cumulFunction f = stepAtStart(a, h); cumulFunction f = stepAtStart(a, hmin, hmax); cumulFunction f = stepAtEnd(a, h); cumulFunction f = stepAtEnd(a, hmin, hmax);"

**A4**

> "A cumulative function expression can be constrained to model limited resource capacity by constraining that the function be ≤ the capacity."

（其**逐字代码**见 §5-1。）

**B1**

> "predicate cumulative(array [int] of var int: s, array [int] of var int: d, array [int] of var int: r, var int: b) Requires that a set of tasks given by start times s, durations d, and resource requirements r, never require more than a global resource bound b at any one time. Assumptions: forall i, d[i] >= 0 and r[i] >= 0"

**C1**

> "Let T be a set of **tasks**, and let a task i∈T be defined by its start variable s_i, **resource usage** r_i∈ℤ≥0, and duration d_i∈ℤ≥0. Finally, let C∈ℤ≥0 be the **capacity** of the resource. Then the **Cumulative(s, r, d, C)** constraint is the condition that at any time point τ the cumulative resource usage of intervals [s_i, s_i+d_i) covering τ does not exceed the capacity:"
>
> "∀τ∈ℤ : ∑_{i∈T : s_i ≤ τ < s_i+d_i} r_i ≤ C."
>
> "An important special case of Cumulative is where the resource has unit capacity C=1 and each task has resource usage r_i∈{0,1}, known as Disjunctive."

## §4 `precedence` 之逐字定义

| # | 来源 · 页内位置 | URL | 时点（UTC+8） |
|:-:|:--|:--|:--|
| D1 | IBM「Precedence constraints on interval variables」· 全节 | `https://www.ibm.com/docs/en/icos/22.2.0?topic=variables-precedence-constraints-interval`（另见旧式帮助路径） | 19:29–19:30 |
| D2 | IBM「Introduction to Scheduling Concepts in CP Optimizer」· 节同页并列「Precedence constraints」与「Cumul functions in CP Optimizer」 | `https://www.ibm.com/docs/en/icos/22.1.1?topic=c-introduction-scheduling-concepts-in-cp-optimizer-1`（正文取自同题 `fr` 镜像，**英文正文**） | 19:30 |
**D1**

> "Precedence constraints are used to specify when one interval variable must start or end with respect to the start or end time of another interval. The following types of precedence constraints are available; if a and b denote interval variables, both interval variables are present and delay is a number or integer expression (0 by default), then:"
>
> "**endBeforeStart(a, b, delay)** constrains that at least the given delay should elapse between the end of a and the start of b. It imposes the inequality **end(a) + delay <= start(b)**."
>
> "**endBeforeEnd(a, b, delay)** constrains that at least the given delay should elapse between the end of a and the end of b. It imposes the inequality **end(a) + delay <= end(b)**"
>
> "**endAtEnd(a, b, delay)** … It imposes the equality **end(a) + delay == end(b)**."
>
> "**endAtStart(a, b, delay)** … It imposes the equality **end(a) + delay == start(b)**."
>
> "**startBeforeEnd(a, b, delay)** … It imposes the inequality **start(a) + delay <= end(b)**."
>
> "**startBeforeStart(a, b, delay)** … It imposes the inequality **start(a) + delay <= start(b)**."
>
> "**startAtEnd(a, b, delay)** … It imposes the equality **start(a) + delay == end(b)**."
>
> "**startAtStart(a, b, delay)** … It imposes the equality **start(a) + delay == start(b)**."
>
> "If either interval a or b is not present in the solution, the constraint is automatically satisfied, and it is as if the constraint was never imposed."

**D2**（逐字）：「to specify precedence relations between two interval variables (see Precedence constraints)」

📌 **「二者可否并施」之据有二**：①**同一求解器、同一建模语言、同一调度特性集**（D2 同节并列两项）；②**同一模型内并存之实例**（A4：house-building 教程之同一 `.mod` 中同时含 `endBeforeStart(...)`（先后）与 `workersUsage <= NbWorkers`（累积容量））⇒ **判：可并施**，IBM 未载二者互斥之任何限制。⛔ 本棒**未跑**该例模型 ⇒ 此为**文本层面**之并施性，**非运行验证**。

## §5 二者并施之形式化写法（可直接入模型者）

**§5-1 IBM 官方写法（逐字代码，出自 A4）**：

```
cumulFunction workersUsage = sum(h in Houses, t in TaskNames) pulse(itvs[h][t],1);
workersUsage <= NbWorkers;
forall(h in Houses) forall(p in Precedences) endBeforeStart(itvs[h][p.pre], itvs[h][p.post]);
```

**§5-2 经典全局约束写法**｜MiniZinc 官方（B1，逐字）：`predicate cumulative(array [int] of var int: s, array [int] of var int: d, array [int] of var int: r, var int: b)`；其**数学本体**（C1 公式 (1)，逐字）：`∀τ∈ℤ : ∑_{i∈T : s_i ≤ τ < s_i+d_i} r_i ≤ C`——**同一物之两种写法**。📌 IBM **不**以 `cumulative(s,d,r,b)` 之名提供该约束，而以「累积函数 ＋ 容量约束」提供之 ⇒ **本棒不将二者混同**：MiniZinc／学术＝**经典全局约束**；IBM＝**累积函数范式**；二者**约束之量同、写法异**。

**§5-3 本案适配稿**：**因篇幅删并，本棒未留**（体例草稿：含我方自设之时间维与取值缺；⛔ 本棒⛔ 0 定稿、⛔ 0 填值）。

## §6 与本案 `3 steps`／cost-bounded 之关系（**「等价否」之判与据**）

**判：CP `cumulative` 与「Σ 动作代价 ≤ B」之 cost-bounded 形式，⛔ 不等价（非同一物）。**

| # | 据 | 出处 |
|:-:|:--|:--|
| 1 | `cumulative` ＝**逐时点**剖面界 `∀τ : ∑_{i∈T : s_i ≤ τ < s_i+d_i} r_i ≤ C`（求和对象＝**在 τ 处同时覆盖**之任务集）；同义表述「never require more than a global resource bound b **at any one time**」——「at any one time」为**时点限定语**，非全序列总和 | C1 公式 (1)＋B1（皆逐字） |
| 2 | cost-bounded ＝**动作序列之代价总和**之上界，**不含时点／区间／同时性**（外委亦书为 `sum_{k=1..m} occupancy_t[a_k] <= B_t`）。**别之精核**：前者约束「**做过什么**」，后者「**此刻同时占用多少**」；**串行**读法下 `cumulative` 每刻只含一任务 ⇒ 退化为「单动作占用 ≤ 容量」，cost-bounded 仍须校验「全序列之和 ≤ 界」⇒ **cost-bounded 严于** `cumulative`。**可互化之条件**：令全部动作**同窗重叠**、demand ＝ 代价、capacity ＝ B，则 `cumulative` 之剖面界**即化为** `Σ 代价 ≤ B` ⇒ cost-bounded 可由 `cumulative` 表达；⚠ 然须**另加**①**时间轴**（本案素材**无** duration／time point）②**重叠假设**（本案动作为**决策点上的单选**）⇒ 属**额外构造**（＝自拟），**非** `cumulative` 之语义本身 | 阶② `c6d2e7dbb004` §6.2 ④＋阶③ `e168c6f0ebec` §6 ②＋外委 `42e03b658e8a` §B-2.3；素材事实见外委 §B-2.3（「exactly one action is selected at a decision point」） |
| 4 | **步限不属 `cumulative` 之射程**：其 capacity 界约束**资源占用**、**不约束动作计数**（`pulse` 之高度即 demand＝占用量，非次数）⇒ 步限仍走 cost-bounded 体例（阶② `F2` 之 cost-bounded 赛道体例仍为其来源）。**`3` 之归属**：仍为**本案材料之字面值**，⛔ 0 称其为 CP 文献值；其可对应 capacity `b`／`C`、duration `d_i`、或 demand `r_i`——**三者语义各异**，本棒⛔ **0** 自行认定 | A3 之 `pulse(a, h)` 语义＋阶② §6.2 ④＋阶③ §6 ②逐字 |

⇒ **`B-F` 步限之形式化可沿用者，仍为阶② `F2` 之 cost-bounded 体例（`Σ 动作代价 ≤ 3`）；`cumulative`／`precedence` 所补者为「动作组合」面之**约束形状**与**要素语汇**，⛔ **不**取代 cost-bounded。

## §7 与在册件之相容性或差异

**§7-1 与阶③ §6（`e168c6f0ebec`）**｜阶③ 逐字（缺口）：「若 PI 明定组合属本实验面，则取 CP 之 `cumulative`／`precedence` 体例——⚠ 该来源（**IBM CPLEX／`F5`**）**本棒未获正文** ⇒ ⛔ **0** 逐字引其语义。」⇒ **该 ⛔ 之触发条件已解除**（§3／§4 已获正文）；本棒**仍⛔ 0 回改**阶③ 一字，其 16 条归型、4 条二读歧义、初值体例、步限形式化**未动、未改、未裁**；本棒**不触碰**其三态栏。

**§7-2 与外委件（`42e03b658e8a`）§B-2.2／§B-2.3**｜外委逐字（§B-2.2「Exact executable predicate」）：

```
function FEAS(t, k, occupancy_table):
    if occupancy_table[t] is missing or unit_of(B_t) is NOT_IN_RANGE:
        return UNOBTAINED              # not the empty set
    require unit_of(occupancy_t) == unit_of(r_t_k) == unit_of(B_t)
    return { a in options_t : occupancy_t[a] <= r_t_k and h_t_k >= 1 }

function UPDATE(t, k, selected_action):
    require selected_action in FEAS(t, k, occupancy_table)
    r_t_(k+1) = r_t_k - occupancy_t[selected_action]
    h_t_(k+1) = h_t_k - 1
    n_t_(k+1) = n_t_k + 1
    return (r_t_(k+1), h_t_(k+1), n_t_(k+1))
```

外委逐字（§B-2.3「Action combination rule」）：

> "The adopted model is atomic selection: exactly one action is selected at a decision point; a multi-action bundle within one cell is not introduced. Across a sequence `(a_1,...,a_m)`, resource use is additive and the step count is the sequence length:"

```
sequence_feasible((a_1,...,a_m), B_t, H_t) iff
    every prefix satisfies FEAS at its own k
    and sum_{k=1..m} occupancy_t[a_k] <= B_t
    and m <= H_t
```

外委逐字（§B-2.2 末段）：「The resource cap and the step limit are separate dimensions. Resource arithmetic is forbidden across unlike units.」

| # | 面 | 判 | 据 |
|:-:|:--|:--|:--|
| 1 | **要素语汇** | **相容**（一一对应） | `occupancy_t[a_k]` ↔ demand `r_i`；`B_t` ↔ capacity `b`／`C`；动作序列各项 ↔ tasks（`s_i`,`d_i`）⇒ PI 裁「采 CP 体例」于外委件**有对应物可落** |
| 2 | **约束形状** | **有别** | 外委 `Σ_{k=1..m} occupancy ≤ B_t` ＝**序列总和**界；CP `cumulative` ＝**时点剖面**界（§6 据 1–4）；二者可互化但须加时间轴与重叠假设（§6 据 3） |
| 3 | **`FEAS`／`UPDATE` 之位置** | **有别** | 外委 `FEAS` 为**逐动作**之剩余量门（`occupancy_t[a] <= r_t_k and h_t_k >= 1`）、**不含剖面**；`UPDATE` 之 `r_t_(k+1) = r_t_k - occupancy_t[...]` 为**剩余量**递减。CP 侧**无「剩余量」构件**，其对应物是**逐时点**占用之和（§5-2）与 `step`／`stepAtStart` 之**累计量**增减（可为负）⇒ 「剩余 vs 累计」方向**相反**，⛔ 0 径等同 |
| 4 | **先后／序·单位与数值·时间维·结论** | **形式相近而层级不同；数值与时间维仍缺；体例依据已足** | 外委序列 `(a_1,…,a_m)` 之**决策点序号** ↔ CP `endBeforeStart` 链（D1；A4 之实演代码），⚠ CP 之先后为**时间先后**而本案**无时间轴** ⇒ 只可对应「序号先后」。外委 §B-2.1 逐字：`B_t` 与 `r_t_0` 之单位为 `NOT_IN_RANGE`；`step` 为「one atomic action selection in the model. This is a model-count unit, not a physical-time unit.」；占用量 80 格全缺（`G-BO-t_XX-a_Y`）⇒ CP 之 capacity `b` 于本案**无值可代**；且 CP `cumulative` 必需 `s_i`／`d_i` 与**时点** ⇒ 直接套用须**先补时间维**，而补之即**自拟** ⇒ 本棒⛔ **0** 为之。⇒ 裁 15 之「采 CP 体例」现**有正文可依**；外委组合规则与 CP 要素**相容**（第 1 条）而**约束形状有别**（第 2 条）；可落之实形须先解**时间维**与**数值**——二者**不在本棒职权**内 ⇒ 本棒**不裁**、**不填**、⛔ **0 宣告** |

## §8 未获之面与老实交代

1. **IBM 官方页直取全域 403**（19:29–19:33 UTC+8；阶② 所载 `icos/20.1.0?...` 本棒未另直取 ⇒ **阶②之 403 记载依然为实**）；本棒 IBM 正文**经检索器抽取同 URL 得**，取得径**非直取**。
2. **IBM 页内以图渲染之公式在抽取文本中缺字**（「It is semantically equivalent to .」等）⇒ **IBM 官方公式本体未以文本取得**；本件公式面**改由学术逐字公式承担**（C1 公式 (1)）并**明标二者非同源**，⛔ 0 混同。
3. **未获 IBM 之 `cumulative`／`precedence` 之单一全局约束关键字页**：IBM 现行 CP 侧为**累积函数范式**，**经典 `cumulative` 之名与写法**取自 MiniZinc 官方库与学术（`Cumulative(s,r,d,C)`）⇒ 本件**分列**而不混同（约束之量同、写法异）；所引 `precedence` 为「Precedence constraints on interval variables」一节之**八式**（IBM 之 `precedence` 系**约束族**——**该文档本身之事实**）。**MiniZinc 官方之调度 `precedence` 谓词未获**（其节**只含** `alternative`／`cumulative`／`disjunctive`；S4 所得 `value_precede`／`seq_precede_chain` **属字典序约束**）⇒ ⛔ **0** 以其充调度体例之据；⛔ 未核 MiniZinc 新版（路径 404）与其 2.5.2 之差异。**OR-Tools 官方文档未获**（两次均超时）⇒ ⛔ **0** 撰其 `AddCumulative` 之语义。4. **检索器三次工具侧失败**（S6／S7／S8 报 `MATRIX_TOOL_REQUEST_FAILED`，**0 命中，非 0 结果**）⇒ 本棒**检索面窄于**原计划（OR-Tools 一家未得；学术一面改由 arXiv API 直取补入）。**为压缩篇幅，S6／S7／S8 三条检索式之逐字未列于 §2**（其结果与失败原因已载于 §2 与本项）——此为**本棒之删并**，非「未查」。本件所记命中数**仅为实得**，⛔ 未以「未查」充「查而无果」。
5. **学术正文之取径为 arXiv／ar5iv 预印本，非出版社版**（C1 自陈 `submitted to CP 2026`）⇒ **发表状态以原文自陈为准**，本棒**未**核出版社版；全文经 ar5iv 转换且**中段被工具上限截断** ⇒ 本件所引**皆在实读范围之内**，⛔ 未据截断外之内容作任何断言；其数学以 MathML/alt-text 呈现，本件所引之 `s_i`／`d_i`／`r_i`／`C`／`τ`／`∀`／`∑` 系**据该 alt-text 逐字录出**，本棒**未**逐式与 PDF 校对（⛔ 未取 PDF）。
6. **本棒⛔ 跑实验**（⛔ 0 跑 `tools\exp_harness.py` 之任何 `run()`、⛔ 0 造 RNG 序、⛔ 0 跑 A4 之 house-building 模型、⛔ 0 解本案任何约束实例；**同批正控仅实测其指纹** 45,590 B／`ce64b9b97489`）｜**⛔ 0 调 LLM／API**（检索器与 arXiv API 属**取文献**之工具）｜**⛔ 0 读** `〔本地路径已脱敏〕`｜**⛔ 0 读**归档区正文（仅按名与计数 40,242 件）｜**⛔ 0** 回改任一既有件一字｜**⛔ 0** 移动／重命名／删除任一件｜**⛔ 0** 新建目录（本棒**唯一新增件**为本件）｜**⛔ 0 落五终判｜⛔ 0 闭 `KD`｜⛔ 0 宣告段毕或门槛成就｜⛔ 0 代 PI 裁**（本件**不作任何终判语汇之断言**；§6 之「等价否」之判**仅限体例语义之比较**，⛔ 非对 `B-F` 类之终判；§5-3 适配稿⛔ **0** 定稿）。**在册件引证皆经本棒回读**（阶③ §6 第 268／270 行、阶② §6.2 ④、外委 §B-1.1／§B-2.1／§B-2.2／§B-2.3、`v285` §2-3、`v287` §1 第 22 行与 §4 第 73 行）⇒ ⛔ 未凭记忆引其行。**未被本棒触及之面**：①传播算法与冗余推理；②`cumulative` 之多资源交互（C1 之 lifting 与 3n 问题）；③IBM 之经典旧式 OPL 写法；④本案之初值与 4 条二读歧义（皆⛔ 未取／未动）。

**§8-1 落盘自证（六项 · 落盘后实跑）**

| # | 检查项 | 本棒实测 | 判读 |
|:-:|:--|:--|:-:|
| 1 | **件路径** | `〔本地路径已脱敏〕` | — |
| 2 | **BYTES** | 见本棒之**报回**（自指之循环不入件） | — |
| 3 | **SHA-12** | 见本棒之**报回**（自指之循环不入件） | — |
| 4 | **BOM** | **0**（前 3 字节 ≠ `EF BB BF` ⇒ UTF-8 无 BOM） | ✅ |
| 5 | **CR 计数** | **0** ⇒ **纯 LF**（VT 亦 ＝ 0） | ✅ |
| 6 | **末字节 ＋ U+FFFD** | 末字节 ＝ **`0x0A`**；**U+FFFD ＝ 0**（`python -P .tmp\_bcheck.py` 实测） | ✅ |

📌 **新增件 1 件**（本件；落于既有 `results\evidence\register\`）｜⛔ 0 新建目录｜⛔ 0 移动／重命名／删除任何既有件。**key 形态自扫**（落盘后实跑）：`sk-`／`tp-`／`ark-`（词边界 `\b` ＋ 8 位以上字母数字）｜`API_KEY` **赋形**｜`Authorization` ＋ `Bearer` **首部形**｜`password`／`secret`／`token` **赋形** ⇒ **0 命中** ✅。

---

**状态行**：`B-F 组合面 · CP 体例正文来源件 · cumulative／precedence 正文已获（IBM 官方 ＋ MiniZinc 官方 ＋ 学术 Cumulative(s,r,d,C) 公式；precedence 八式）· 等价判：CP cumulative 与 Σ 代价 ≤ B 不等价（时点剖面 vs 序列总和）· 与外委 FEAS/UPDATE 相容在要素、差异在形状与时间维 · 时间维与数值仍缺 · ⛔ 0 宣告成就 · 呈 PI`
**落款**：证据链审计官 evidence-auditor · 2026-10-24 · ⛔ 0 代 PI 裁 · ⛔ 0 宣告成就
