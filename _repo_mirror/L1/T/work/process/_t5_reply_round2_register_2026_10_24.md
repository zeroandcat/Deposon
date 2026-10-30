# T5 第二轮委托之回函登记（Codex 面 · 2026-10-24）

> 📌 **件之性质**：**回函登记件**（只登记受托方之回函与其开启项；⛔0 代 PI 裁 · ⛔0 判其采纳）。
> 📌 **委托件（第二轮）**：`letters\_commission_t5_inputs_external_EN_round2_draft_2026_10_24.md`（**64,125 B／`e2cd66b1b543`**·416 行）——PI 于 v270 §1-1 **准发**（发出动作归 PI）。
> 📌 **回函件**：`〔本地路径已脱敏〕` —— **37,866 B／`7b750f1a02bd`**（本代理实测：末字节 `0x0A`、LF 250、BOM／CR／U+FFFD 皆 0；与受托方回执**逐位相符**）。
> 📌 **附件**：**9 件 CSV sidecar**（`〔本地路径已脱敏〕*.csv`·mtime 皆 2026-10-24 02:06:05）——其中 **6 件极小**（37／39／55／64／72／97 B），与「六表明示不完整」相符。
> 📌 **观测时点**：2026-10-24 02:4x。

---

## §0 一句话

🟢 **回函合规**：**七节**（`§R-1` 文件表／`§R-2` 二十条逐条／`§R-3` 可复现包／`§R-4` 具名缺口／`§R-5` 盲构造自证／`§R-6` 不采纳确认／`§R-7` 开启项与歧点）——正对委托稿之六项要求 ＋ 3A 四规程。**且未在明令不得自证处自证**（见 §2）。**但**其 `§R-7` 指出**我方委托稿自身的一处内在矛盾**（见 §3），此为我方之失。

---

## §1 回函之实（逐项登记 · ⛔0 判其优劣）

| 面 | 内容 |
|:--|:--|
| **`§R-1` 文件表** | 两包（A／B）＋ 9 件 CSV sidecar |
| **`§R-2` 二十条** | `A1-1…A1-10`／`A2-1…A2-10` **逐条**给「holds ／ does not hold ／ not certifiable…」＋理由：多数为「**does not hold**」，因所需输入（states／kernel／priors／likelihoods／occupancy／constraint operators）**未获**；`A2-10` 为「**holds（仅配对／域之文档面）**」 |
| **`§R-3` 可复现包** | 给可复现之读法（含 `digest_stream` 只读指定区段之代码骨架） |
| **`§R-4` 具名缺口** | **五类**：`A-S`（环境状态与逐格支撑）／`A-V`（反事实核·单位与域处置）／`A-P`（先验·观测·似然·后验）／`B-O`（独立接地之动作占有与情境单位校准）／`B-F`（精确约束算子·初值·动作组合·与另行步限之绑定）。明写「**no numerical result is filled with zero, a mean, median, default or placeholder**」 |
| **`§R-5` 盲构造自证** | 有专节 attestation |
| **`§R-6` 不采纳确认** | 有专节 acknowledgement |
| **`§R-7` 开启项** | **四点**（见 §3） |

---

## §2 3A 之遵守面（**本条为准**）

📌 我于委托稿 §1-2(b) 明令：「**You are not asked to certify `A1-6` / `A2-6`, and you must not claim to have certified them**」，并要求逐字写明保留措辞。

🔴 **其实际写法（照录）**：
> `A1-6` ｜ **not certifiable by the commissioned party under 3A — verification reserved to the requesting side** ｜ All twenty expected-utility maximizers are unavailable (R-4); no guessed list or comparison against correct.
>
> `A2-6` ｜ **not certifiable by the commissioned party under 3A — verification reserved to the requesting side** ｜ All twenty feasible maximizers are unavailable.
>
> `A1-6` and `A2-6` are each **not certifiable by the commissioned party under 3A — verification reserved to the requesting side**. Their twenty-cell argmax lists and full computation inputs are not delivered; this reservation is not a substitute for those missing outputs. **No maximizing labels are guessed.**

⇒ 📌 **判**：**逐字合规**——它既写了保留措辞，又明写「本保留不替代缺失的产出」，且「不猜 argmax」。⚠ 且其自陈「inputs are not delivered」——即 **3A 之 (b) 在我方这一侧仍无从执行**（无输入可核）。

---

## §3 `§R-7` 四点（**其中第三点系我方之失**）

| # | 其所述 | 本代理之核 |
|:-:|:--|:--|
| **1** | 位置式动作 ID 属私有整合问题；本地别名与委托稿 L275 之顺序不同，而 L159–L161 未给选项序 ⇒ **不得要求其返回私有序或 key** | ⚠ 属实（我方稿以位置指代而未附序）——**记为委托稿之缺陷** |
| **2** | （同上族之细化） | 照录 |
| **3** | 🔴 **`A2-6` 之要求自相矛盾**：委托稿 **L89–L90 把核对置于请求方**，而 **L198 又要受托方给 argmax 列表**；在多可行动作下，maximizer **无法仅由 occupancy 推定**（须 payoffs，而 payoffs 被扣）。其明写「不请求 payoff 数据」「请求方可在有接地 Feas 后私下最大化」「为躲此问题而造单点 Feas 集合属未接地之选」 | 🔴 **成立——此系我方委托稿之内在矛盾**。我在 §1-2(b) 写了保留，却在 §3 之判据栏仍要 argmax 列表 ⇒ **两处相抵**。**⛔0 诿于受托方** |
| **4** | 数值完成前须**独立接地**（独立测得或可证之资源需求／时序／尺度／约束语义，排除 key／payoff／私有选项序）；且「**本回函未受任何外部测量或来源之委托**」 | ⚠ 属实——我方确未委托其做外部测量 |

📌 **故**：`§R-7` 第 3 点为**我方稿件之自相矛盾**，第 1 点为**我方指代之不完备**。⇒ 二者皆入候 PI 之处置（见 §4）。

---

## §4 候 PI 之项（本件之主要产出 · 并入末轮卡）

| # | 项 | 类 |
|:-:|:--|:--|
| **R-1** | 本回函之**采纳与否**（沿上次「不采纳只入册」之例？抑或本次因有实体交付而部分采纳？） | 裁 |
| **R-2** | **委托稿自身两处缺陷之处置**：① `A2-6` 之 argmax 要求与「核对归请求方」相抵（`§R-7`-3）；② 位置式动作 ID 未附序（`§R-7`-1） | 裁／改稿 |
| **R-3** | **五类缺口**（`A-S`／`A-V`／`A-P`／`B-O`／`B-F`）**谁补、以何径补**——我方自造？另委外部实测？抑或本面暂挂 | 裁 |
| **R-4** | `§R-7`-4 之「**独立接地**」是否另委（其明写未受此委托） | 裁 |

---

## §5 本件之限

1. ⛔ **0 判该回函之质量或可否采纳**（采纳归 PI）；⛔ **0 代 PI 裁**；⛔ **0 落五终判**。
2. ⚠ **本件未做者**：① ⛔ 0 逐行复核 `§R-2` 二十条之理由是否皆成立（只登记其结论与理由类别）；② ⛔ 0 校验 9 件 CSV 之内容（只取体积与 mtime）；③ ⛔ 0 复算 `§R-3` 之可复现包；④ ⛔ 0 读 `§R-5` 之 attestation 全文（只登记其存在）。
3. ⚠ **回函在 `codex-workspace`（非四根之内）**：本件只按名与指纹登记，**未纳入树之根清单**（repo／sub／归档／运行时四面）。
4. 📌 **一处须记之对照**：上次（第一轮）回函 `727d85d20aff`／31,050 B；本轮 `7b750f1a02bd`／37,866 B——**均无虚构数值**，两轮一致。

---

**状态行**：`T5 第二轮回函登记 · 七节合规 · 3A 之 (b) 逐字遵守 · §R-7 揭我方稿两缺陷 · 呈 PI`
**落款**：主代理 mavis 亲编 · 2026-10-24 02:4x · ⛔0 代 PI 裁
