# V4 §4.6 统一术语代拟稿（Mavis 代拟，PI 委托 2026-09-22）

**委托留痕**：PI 于组 A 首批问卷（ask_f8837a5b3c168ef3d6e8c18a，2026-09-22）对 §4.6 答复「委托 Mavis 代拟」。本稿为代拟草案，回填问卷作答栏后**待 PI 复核确认生效**。本稿起草过程：0 LLM / 0 外部 URL / 0 GitHub / 0 WeChat / 0 密钥；未触动任何 V1–V3 冻结资产（18 frozen / schema v1 / verifier / P-G v0+v01 / plugin spec 全部只读）。

**作答对象**：问卷 §4.6（`results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md`，行号对回填前基线 SHA-12 `88F48F82E08B` / 739 行；所引行均在本轮回填点 L581 之前，回填后行号不变）。PI 已于组 D 收尾批（2026-09-22）拍路径 B「统一为单一术语」；本稿给出该路径的待收内容：具体统一术语 + 每条原引用重写规则。

---

## 1 统一术语（主术语）

**V4 主术语 = `18 frozen`**。

- **语义**：16 链上锚（7 spec + 4 plugin + 2 anchor_json 条目 + 2 benchmark + 1 corpus）+ 2 anchor JSON 文件自身 = 18 件冻结资产。
- **口径来源**：`deposon_team/plugins/_verify_15frozen.py:4`（"链 16 anchor 锚定 + 2 anchor JSON 自身 = 18 frozen total"）。
- **选择依据**（盘上事实陈述，非偏好排序）：
  1. `18 frozen` 是校验器 `_verify_15frozen.py` 实际校验的操作单元（整链 16 锚 + 2 anchor JSON 自身）；
  2. 引用面最广：本仓文件系统级 census 实测 `18 frozen` 118 处 / 36 件（592 件文本池；详见 §4）；
  3. 邀请函 v1.0 已采用该词根（§3.2 S-11 L168："18 frozen anchors + 22 caption entries + 5 KT anchors"，`3D9F73519F6C:168`）。

## 2 保留术语（子结构计数，不并入主术语；引用时限定词不可省略）

| 术语 | 语义 | 盘上来源 | V4 引用规则 |
|---|---|---|---|
| KT 锚文件 15 条目 | KT-A1 / KT-B1 / KT-C1 × 5 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（C7 修订后 SHA-12 `6E9CD8CD8E07`，11,318 B / 219 行） | 限定词「KT 锚文件」不可省略；禁裸写「15 anchors」 |
| schema anchors 16 条 | 7 spec + 4 plugin + 2 anchor_json + 2 benchmark + 1 corpus | `deposon_team/plugins/_v3x_frozen_schema_v1.json` anchors 数组（16 条；SHA-12 `9E99DCC4D920`，216 行） | 限定词「schema」不可省略；禁裸写「16 anchors」 |
| KT 五值 | 4 个 SPEC V0.1 值 + KT 锚文件自身 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md:42–46`（`C41C1D6AA794`）；`results/deposon_v3_v7_summary_2026_09_11.json:290` | 术语「KT 五值」；禁「5 KT anchors」/「5 anchors JSON」 |

## 3 已知混淆源与过期状态（一律注记，不改盘上物）

1. **schema name 字段混淆源**：`_v3x_frozen_schema_v1.json` 内 KT_ABC1 条目 `name` 字段为「5 anchors JSON」——S-11「5 KT anchors」混淆的源头（问卷 §4.5 路径 C 已注记）。schema 属冻结资产，禁改；V4 引用该字段时括注其语义为「KT 锚文件（自身即 KT 五值中的第 5 值）」。
2. **校验器文件名历史口径**：`_verify_15frozen.py` 文件名含「15」，实际校验 18 frozen（16 锚 + 2 anchor JSON 自身，见其 L4 注释与 L24–L41 的 16 条 + 尾部 2 JSON 逻辑）；「15」系 V3 时代 15 锚口径的历史命名。文件属冻结资产，禁改，注记。
3. **双处过期期望哈希 `03c6c01f3697`**：C7 锚文件修订（2026-09-22，`03C6C01F3697` 6,680 B / 189 行 → `6E9CD8CD8E07` 11,318 B / 219 行）后，schema L12（KT_ABC1 条目 expected 值）与 `_verify_15frozen.py` L25（期望哈希）两处期望值均已过期。两件均属冻结资产，禁改，只注记；fresh 跑 `_verify_15frozen.py` 对 KT_ABC1 条目将 FAIL（repo 现副本 `6E9CD8CD8E07`）——V4 引用校验结果时区分两种口径：「历史 16/16 PASS（修订前）」与「fresh 跑 FAIL（修订后，预期内）」。
4. **外部归档基座不存在**：`_v3x_frozen_schema_v1.json` 的 `path_fallback` 与 `_verify_15frozen.py` ARCHIVE_BASE 指向 `D:\私人资料\_archive_deposon_2026_09_17`；该字面路径 2026-09-22 实测不存在（`Test-Path -LiteralPath` = False）。父目录 `D:\私人资料` 下实际存在 `_non_upload_local_archive`（1,176 件 / 21 个顶级目录，含 .mavis/.trae/corpus/results/verifier 等），其内无 `_archive_deposon_2026_09_17` 子目录。归档 fallback 当前不可用，注记。

## 4 Claude Code §1.7「仅两文出现」陈述的实测修正

Claude Code 回函 §1.7（`D39CB17B051B:54–62`，问卷 §4.6 L544 转录）陈述：「"18 frozen" 仅在 `results/_adendum_FGK_complete_20260917_143033.md:20,166` 与 `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md:19,22,120,132,159` 出现」。

**实测 1（本仓引用面，census 2026-09-22）**：文件系统级枚举 592 件文本池（扩展名 md/json/py/txt/ps1/csv/html/js/ts/yml/yaml/tex；绕开 grep 工具忽略规则），四术语命中如下（raw / 排除探针脚本自身命中）：

| 术语 | raw | 排除探针后 | 探针自身 |
|---|---|---|---|
| `18 frozen` | 118 处 / 36 件 | **115 处 / 33 件** | 3 处（`_tmp_archive_trace_gA1.ps1` / `_tmp_census2_gA1.ps1` / `_tmp_term_census_gA1.ps1` 各 1） |
| `18-frozen` | 7 处 / 4 件 | **5 处 / 2 件**（均在 `letters/_v4_experiment_invitation_2026_09_20.md` 两版本） | 2 处（census2 + term_census） |
| `15 anchors` | 25 处 / 9 件 | **23 处 / 7 件** | 2 处（census2 + term_census） |
| `16 anchors` | 11 处 / 5 件 | **9 处 / 3 件** | 2 处（census2 + term_census） |

「仅两文出现」陈述失实。

**实测 2（两文去向）**：Claude Code 所引两文件**不在本仓**（本仓全仓文件系统级检索 0 命中），实际位于 **deposon-sub 仓**：

| 文件（deposon-sub 内路径） | SHA-12 | 大小 / 行数 | `18 frozen` 命中行 |
|---|---|---|---|
| `D:\私人资料\deposon-sub\results\_adendum_FGK_complete_20260917_143033.md` | `958188C83CF0` | 14,005 B / 231 行 | L20, L166（与 Claude Code 所引**精确吻合**） |
| `D:\私人资料\deposon-sub\results\_archive_2026_09_18\_trae_5audit_aggregated_2026_09_17.md` | `43265E4BF2BE` | 11,465 B / 188 行 | L19, L22, L98, L120, L132, L159, L184（共 7 处；Claude Code 所引 5 处为其子集，未引 L98 / L184） |

结论：Claude Code 的行号引用真实（其所读副本在 deposon-sub 仓）；「仅两文出现」作为引用面陈述失实。V4 引用面不沿用该陈述；deposon-repo 与 deposon-sub 系两仓，跨仓引用一律带仓标识。

**测量口径注**：此前两轮测量差异的消解——grep 工具轮 119 处 / 34 件（受工具忽略规则约束的池）与 term-census 轮 116 处 / 34 件（590 件池，含 term_census 探针自身 1 处）与本 census 118 处 / 36 件（592 件池，含 3 个探针自身 3 处）——差异系池定义与探针自身命中；本稿以文件系统级 census 为准并注明方法。另：本仓归档子集（`results/_archive_*`）内历史命中 7 处 / 2 件（`results/_archive_2026_09_20/mavis_trash_2026_09_18.py` L14/23/26/45/106 + `results/_archive_2026_09_21/_v4_brainstorm_seeds_2026_09_20.md` L76/288），其行号与 Claude Code 所引不吻合——此前「疑似改名归档」假设证伪（两集合 7=7 系巧合）。

## 5 每条原引用重写规则

**适用范围**：邀请函 v1.x 后续版本 + V4 自有新文档（`results/_v4_*`、整合稿、问卷）。V1–V3 冻结资产、已收 letters 回函（他人作品）、deposon-sub 仓资产**不回改**。

| # | 原引用形态 | 实例（census 抽样） | 重写规则 |
|---|---|---|---|
| R-1 | 裸「18 frozen」（泛指冻结资产全集） | 本仓 33 件 115 处正文多数（`_verify_15frozen.py:4`、问卷 v1.1 内 15 处、letters 多件） | 保留「18 frozen」；每文档**首次出现处**括注「= 16 链上锚 + 2 anchor JSON 自身（`_verify_15frozen.py:4`）」 |
| R-2 | 「18 frozen anchors」（复合形态） | 邀请函 §3.2 S-11 L168（`3D9F73519F6C:168`） | 改「18 frozen」；删「anchors」后缀（避免与 15 / 16 锚计数混同） |
| R-3 | 裸「15 anchors」 | 23 处 / 7 件（`letters/_v4_theme_reply_mavis_*` 三版 11 处、整合稿两版 4 处、问卷两版 8 处） | 改「KT 锚文件 15 条目」（限定词「KT 锚文件」不可省略） |
| R-4 | 裸「16 anchors」 | 9 处 / 3 件（`letters/_v4_distillation_reply_claude_code_2026_09_20.md` 1 处、问卷两版 8 处） | 改「schema anchors 16 条」（限定词「schema」不可省略） |
| R-5 | 「5 KT anchors」/「5 anchors JSON」 | 邀请函 L168；schema KT_ABC1 条目 name 字段 | 改「KT 五值」；schema name 字段属冻结资产不回改，引用时按 §3.1 括注 |
| R-6 | 「15 锚 ≠ KT 五值 ≠ 18 frozen」三套区分表述 | 问卷 §4.5（PI 已拍路径 A：三种锚语义不同） | 保留三套区分表述；按 §2 表限定词规则书写（KT 锚文件 15 条目 / KT 五值 / 18 frozen） |
| R-7 | 「18 frozen 22/22」类校验口径 | deposon-sub `trae_5audit` L19/L22（跨仓历史文档） | V4 引用时保留原口径 + 注明「校验器历史跑出口径（C7 修订前）」；不并入主术语、不折算 |

## 6 待 PI 复核项

1. 主术语选 `18 frozen`：确认 / 改选（改选则 §1–§2 重拟）。
2. 重写规则适用范围（§5）：仅约束邀请函后续版 + V4 新文档，或扩大到问卷 / 整合稿自身回改。
3. §4.5「每条最终定义」按本稿 §1 / §2 收口：确认后问卷 §4.5 尾注标「已收」。
4. §3 双处过期哈希与外部归档基座不存在的注记方式：确认或改写。

---

*本稿为 V4 自有资产，诞生即 SHA-12（见落盘后呈报）；LF + 无 BOM。*
