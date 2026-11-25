# 48 条空摘录之读取状态·回查（`_mat48_recheck_`）

- 作成：verifier（独立回查）｜2026-10-25｜**作用域**：仅辨 `armB` 之 48 条空 `examplesB` 件之**读取状态**。
- ⛔ 本件不判终判、不代 PI 裁、不宣告 `TR-3S` 生效或门② 成就、不宣告①段毕；不评该语料分类结果之对错。
- ⛔ 未回改任何既有件；本件为新建单件；既有件一律只读。
- 实带 skill：**`evidence-contract`**（自测 `〔本地路径已脱敏〕`，**3,921 B／SHA-12 `e7fd7b39c22f`**，与在册实测值相符）。行文依其 Step 1–3「逐断言取证、断言不得超出证据」之纪律。

## 0 · 授料与自测指纹（自测，非转引）

| 件 | BYTES | SHA-12 | 用途 |
|---|---:|---|---|
| `.tmp\_g2narrow_out_stripped_v5_2026_10_25.json` | 32,945 | `2be2fd92fe9f` | 主语料（v5·去分类） |
| `.tmp\_g2narrow_out_2026_10_25.json` | 83,175 | `d7bc95b29298` | 原语料（**仅取 `roots`/`controls` 元数据**；其 `armB` 之 `classA`/`classB`/`nB`/`nC`/`nBA`/`nCA`/`fam` 未读、未引） |
| `.tmp\_g2narrow_2026_10_25.py` | 23,813 | `bf6765033645` | **语料生成器（口径之权威源）** |
| `results\verdict\judgement\_tr3s_r5_A_reading_2026_10_25.md` | 68,758 | `657f27f07447` | 读者 A 件（读其所据） |
| `results\verdict\judgement\_tr3s_r5_B__reader_B_independent_judgement_2026_10_25.md` | 59,652 | `4dcad1414260` | 读者 B 件（读其所据） |

元数据一致性（自测）：v5 与原语料之 `roots`、`controls` **逐字相等**（`True`／`True`）⇒ v5 确为原语料之去分类裁体，元数据未被裁改。

## 1 · 语料内生之决定性事实（生成器源码）

`_g2narrow_2026_10_25.py:458-476`（自读）：

- `ARCHIVE`／`MINIMAX` 根 → 写 `classB/classA='SKIP_NOREAD'`、**写 `reason='name+fingerprint only; content not read'`、不写 `examplesB` 字段**，并 `continue`（在 `open()` 之前）。
- `REPO`／`SUB` 根 → `txt = open(path,'r',encoding='utf-8',errors='replace').read()` → `classify(txt, COMP_FULL)` → **写 `examplesB`**（可为 `[]`）。
- 读失败 → 写 `classB/classA='READERR'`、**写 `reason=str(e)`、不写 `examplesB`**。

⇒ **内生判据**：`examplesB` 字段之存在 ⟺ 该件于扫描时**成功读入**（`SKIP_NOREAD`／`READERR` 两路皆不写该字段）。

## 2 · 六问之逐条结论

**问1 · 48 条之根分布**（据：v5 `roots`＋`armB` 之 `root`/`examplesB` 字段；自测）

| 根 | `content_read` | 48 条中属该根 | 该根命中件（有摘录） | 该根无 `examplesB` 字段件 |
|---|---|---:|---:|---:|
| REPO | **true** | **31** | 12 | 0 |
| SUB | **true** | **17** | 8 | 0 |
| ARCHIVE | false | **0** | 0 | **10** |
| MINIMAX | false | 0 | 0 | 0（语料自注：GLM root deliberately excluded (no read)） |

⇒ 48/48 落于 `content_read=true` 之根；`content_read=false` 之根在 48 之内**零条**。

**问2 · 目录交叉**（据：自测按「**根＋相对目录**」聚合；REPO 与 SUB 之同名相对目录**分计**，故 48 条共处 **15** 个目录，若不按根分计则为 12 个）

与命中件**共处**者 **8** 个目录：

| 目录 | 空 | 命中 |
|---|---:|---:|
| `REPO\.tmp\_c514_remote_blobs_2026_10_18` | 5 | 1 |
| `REPO\results\evidence\register` | 1 | 4 |
| `REPO\results\readout\run` | 8 | 3 |
| `SUB\results` | 10 | 2 |
| `SUB\results\doc\document` | 1 | 1 |
| `SUB\results\evidence\register` | 3 | 1 |
| `SUB\results\readout\reading` | 1 | 1 |
| `SUB\results\readout\run` | 1 | 1 |

⚠ **读甲之此一环不成立于全量**：共目录之据只覆盖 **30/48**；另 **7** 个目录（`REPO\.tmp`、`REPO\corpus\v20`、`REPO\docs\V3X`、`REPO\results\readout\reading`（空 8／中 0）、`REPO\results\tool\generator`（空 5／中 0）、`REPO\results\verdict\pi_register`、`SUB\results\work\process`）**无任何命中件**，共 18 件。故「同处 8 目录」为真但**不足**为全 48 之据（此不足不影响结论，因另有内生判据）。

**问3 · `reason` 面**（据：自测逐件读 `reason` 键）

48 条中带 `reason` 者 **0 条**。语料内 `reason` 字段仅见于 10 条（皆 ARCHIVE），字面逐字为 `name+fingerprint only; content not read`（与生成器源码 `:463` 字面一致）。
⇒ 48 与那 10 **不同型**：10 ＝「无 `examplesB` 字段 ＋ 有未读 `reason`」；48 ＝「有 `examplesB` 字段（空列表）＋ 无 `reason`」。
阴性断言齐备：① 射程写死＝v5 语料 `armB` 68 条（有 `examplesB` 者）；② 同批正控＝**同批 10 条 ARCHIVE 确带该 `reason` 字面**（故本项检出不空转）。

**问4 · `controls` 面（正控）**（据：自测复核）

- 语料 `controls`：`alive_buming` `token_hits=12`、`alive_wuhe` `token_hits=7`、`identity_positive_control` `sha12=ce64b9b97489`；**今日复核三者仍相符**（12／7／`ce64b9b97489`）⇒ 同批扫描确产命中，扫描器于 REPO 面有效。
- 更强之同批正控：**以原仪器复算**，67 件可复算者之 `examplesB`（`line`／`tok`／`ctx`）**逐字复现，0 例不符**（47 空 ＋ 20 命中）⇒ 同一扫描器、同一批参数，对该 48 之产出可信。
- 仪器自身受控语料自检（我复算，非引原语料）：30 例中 **29 例相符**；1 例失配＝`K26`「散句：某处提到不明，但不在字段值位。」（预期 A 得 C）——仪器于「散句提及」面有已知 1/30 失配，宜载。

**问5 · 第三读（并出）**

甲乙之外更妥者为**读丙「分层读甲」**：

1. **读丙-a（读取状态层）**：48 条**全部已读**（内生判据，见 §1）⇒ 空摘录 ＝ **零存活候选**，非材料缺失 ⇒ **读乙（未读）被证伪**。
2. **读丙-b（命中层）**：「零存活候选」≠「文件内零 token」。47 件可复算者原始命中共 **38 处**，**全部**被仪器具名排除规则滤尽：`X_R4`（`不明` ＋「不明文」窗）32、`X_METHOD`（方法面行）9、`X_SELF`（本棒自指）13（一处可同时触发多规则，故分项之和大于实例数）。⇒ 48 之内分 **raw 真零 26 件**、**有原始命中而全被规则滤尽 21 件**。
3. 故沿用「真实零命中」之粗名不确；精确名为 **「已读·零存活候选」**，其下分两层。

**问6 · 我的判**

**判：已读且零命中（读甲）成立，但名须精确为「已读·零存活候选」；读乙（未读／材料缺失）被生成器源码证伪。**
**非「分根不一」**：REPO（31）与 SUB（17）两根本皆 `content_read=true`、皆经同一路径读入且复算可复现；无一根之 48 条为未读。

最强三条据：

1. 生成器源码 `:458-476`：48 条全在 REPO/SUB 且**皆带 `examplesB` 字段**；而 `SKIP_NOREAD`／`READERR` 两路皆不写该字段 ⇒ **扫描时已读成功**。此为语料内生之判据，不依赖任何读者主张。
2. 原仪器复算 67/67 件 `examplesB` 逐字复现、47/47 可复算空件复算仍为空 ⇒ 空摘录是**仪器之可复现输出**，非缺失、非错位。
3. 语料自用编码之对立面：同批 10 条未读件＝「无 `examplesB` 字段＋`reason` 明载 content not read」；48 条＝「有 `examplesB` 字段（空）＋无 `reason`」⇒ 语料自身已把「未读」与「已读而零」分作两型。

**分根明细**（问六附）：

- **REPO**｜`content_read=true`｜空 **31**（`results\readout\run` 8、`results\readout\reading` 8、`results\tool\generator` 5、`.tmp\_c514_remote_blobs_2026_10_18` 5、`results\evidence\register` 1、`.tmp` 1、`corpus\v20` 1、`docs\V3X` 1、`results\verdict\pi_register` 1；共 **9** 目录，其中与命中件共处者 **3** 目录、含 14 件，另 6 目录含 17 件）｜命中 **12**
- **SUB**｜`content_read=true`｜空 **17**（`results` 10、`results\evidence\register` 3、`results\doc\document` 1、`results\readout\reading` 1、`results\readout\run` 1、`results\work\process` 1；共 **6** 目录，其中与命中件共处者 **5** 目录、含 16 件，另 1 目录含 1 件）｜命中 **8**
- **ARCHIVE**｜`content_read=false`｜空 0｜命中 0｜另有 10 条未读件；**MINIMAX**｜`content_read=false`｜0｜0

**分层明细**（读丙-b）：raw 真零 **26**／原始命中全被规则滤尽 **21**／今日不可复算 **1**（`REPO\.tmp\_item35_v3_collinear_recompute_2026_10_01.py`，`sha12=c8d859cbb69e`、`bytes=16493`；按大小与文件名全域搜寻 repo＋sub＋archive **未得副本**）⇒ 该 1 条之今日复核**未核**；惟其 `examplesB` 字段存在且无 `reason`，据内生判据可断言**扫描时已读成功**。

## 3 · 未核／未开卷之面（如实载）

1. **原语料之分类面未读未引**：`armB` 之 `classA`/`classB`/`nB`/`nC`/`nBA`/`nCA`/`fam` 未读、未引；原语料顶层 `ablation`/`bing`/`yi`/`plv3_family` 亦未读值（仅作键名与类型普查：`ablation`(dict,7)／`bing`(list,33)／`yi`(list,3)／`plv3_family`(dict,4)）。本件全部结论不依赖之。
2. **48 条之分类结果之对错未判**（越本棒作用域，亦越 PI 授权面）。
3. **今日不可复算 1 件**（上列 `.tmp\_item35_v3_collinear_recompute_2026_10_01.py`）：其原始命中构成未核。
4. **读者 A／B 两件仅读其所据节段**（A 件 §5 材料缺失专节及难例 10、B 件相应段）以核其依据，未取其结论；两件之全文论证未逐段复核。
5. **语料生成时点（`ts=2026-10-25 12:06:37`）之盘上历史状态**未作快照核验；今日盘上 47/48 可复算、1 件已不在盘（`.tmp` 临时件被清）。
6. **MINIMAX 根未开卷**（语料自注排除；本回查亦未扫该根 106,748 件）⇒ 本件一切阴性断言之射程**不含** MINIMAX 根与 GLM 根。

## 4 · 临时件（`.tmp`，并列名；未删改任何既有件）

| 件 | BYTES | SHA-12 |
|---|---:|---|
| `_mat48_recheck_attr_2026_10_25.py` | 6549 | `d081c3a6a636` |
| `_mat48_recheck_attr_out_2026_10_25.json` | 26558 | `3f0b89cf669e` |
| `_mat48_recheck_detail_2026_10_25.py` | 2601 | `e78c368248e0` |
| `_mat48_recheck_detail_out_2026_10_25.json` | 50206 | `d59c62527c24` |
| `_mat48_recheck_detail_readable_2026_10_25.txt` | 9946 | `04c3f647eecf` |
| `_mat48_recheck_dircheck_2026_10_25.py` | 1377 | `c61366f771c0` |
| `_mat48_recheck_dircheck_2026_10_25.txt` | 1322 | `b172747ccb82` |
| `_mat48_recheck_feat2_2026_10_25.py` | 1777 | `fc0ee420b741` |
| `_mat48_recheck_feat_2026_10_25.py` | 4142 | `f57e2486b292` |
| `_mat48_recheck_feat_out_2026_10_25.json` | 74379 | `5fcb57e4e790` |
| `_mat48_recheck_feat_readable_2026_10_25.txt` | 10401 | `37e10f18a1d2` |
| `_mat48_recheck_final_2026_10_25.py` | 1595 | `2b3230e0930a` |
| `_mat48_recheck_final_checks_2026_10_25.txt` | 376 | `1d3e9541e596` |
| `_mat48_recheck_origkeys_2026_10_25.py` | 910 | `bb96afda6428` |
| `_mat48_recheck_origkeys_2026_10_25.txt` | 761 | `5d72e757a709` |
| `_mat48_recheck_probe_2026_10_25.py` | 7104 | `94128575fc3c` |
| `_mat48_recheck_probe_out_2026_10_25.json` | 55297 | `ac78807c5ee0` |
| `_mat48_recheck_readable_2026_10_25.py` | 1563 | `9729ef9551a7` |
| `_mat48_recheck_replay_2026_10_25.py` | 3783 | `5e6ea2e1afdc` |
| `_mat48_recheck_replay_out_2026_10_25.json` | 48163 | `f6a20762c4a4` |
| `_mat48_recheck_rule_2026_10_25.py` | 6998 | `a651193ebe21` |
| `_mat48_recheck_rule_out_2026_10_25.json` | 92953 | `42d7810ed1a3` |
| `_mat48_recheck_rule_readable_2026_10_25.txt` | 14024 | `c099fcbc150a` |
| `_mat48_recheck_tokscan_2026_10_25.py` | 5183 | `dac91242ab32` |
| `_mat48_recheck_tokscan_out_2026_10_25.json` | 31217 | `a7cefb98f4b6` |
| `_mat48_recheck_write_2026_10_25.py` | 11565 | `6856c8184376` |

**回查方法之可复现性**：主证据链＝①生成器源码 `:458-476` 之路径判读；②以该生成器自身 `classify()` 逐件复算 78 件，比对 `examplesB`（`line`／`tok`／`ctx`）；③独立重扫 47 件原始 token 命中并逐处归因至具名规则；④逐根／逐目录／逐 `reason` 键聚合。②之复算脚本为 `_mat48_recheck_replay_2026_10_25.py`（见上表），其输出 JSON 含逐件比对结果，可复跑。

**订正记**：本件写入 2 次——第 1 版「分根明细」之 SUB 目录计数有笔误（1 件分散 4 目录误作 3 目录），经程序化复核后于交付前改正；**结论未变**。
