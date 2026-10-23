# 查理 · FTFB R4 更新版修订记录（2026-09-27）

- **任务来源**：群管理员 2026-09-27 02:34 派单（用户指示「初稿完成后更新 FTFB 以解决 on hold」）。
- **执行规格**：鲍勃《FTFB 更新差异清单（2026-09-27）》§3 五项口径层改写＋§4.1 方案 B（GitHub 相对路径＋引用日冻结 commit）＋管理员五项范围与纪律。
- **选基**：R3 排版重打包（最新验收版，tex SHA-16 `51f4e0c8a0f83daf`，98,972 B，606 行）——沿差异清单 §1.3 建议。
- **本版命名**：**R4 revision edition**（沿提交包 R 系列：B01→R2 排版→R3 重打包→R4 更新）。防混淆声明：与 2026-09-18 内容侧「R4 链头」（鲍勃全稿 R4 摘要合规版，arXiv 终版载体）**无涉**——两者是不同系列的同名标号；本 R4 是提交包（submission package）系列的第四轮。
- **改写纪律**：全部改写在本目录副本执行（`agents/…e74/work/ftfb_r4/ftfb_r4.tex`），shared/ R3 目录与仓内冻结件**零触碰**，仓库只读。

## 〇、指纹

| 件 | 值 |
|---|---|
| 基线 R3 tex | `51f4e0c8a0f83daf`（98,972 B，606 行） |
| **R4 更新 tex** | `4f8c42319603fca6`（101,928 B，606 行；SHA-256 全值 `4f8c42319603fca69473ad07673f236fd0d688a043fdd23d9ebcdec0e2c9fd0a`） |
| 仓库引用基线 | commit `a57d7fe`（全值 `a57d7fe80d151f93e74e1b1a85c20242af39f26d`，2026-09-26 22:05:31 +0800） |
| diff 证据 | `查理_FTFB_R3基线到R4_diff_2026-09-27.txt`（24 个改动块，68 行差异） |

---

## 一、逐项改写前后对照（5 项口径层，数值层零改动）

### 项 1｜anon_* 匿名路径→实名切换（方案 B：仓相对路径 @ a57d7fe）

**改写位点 9 处**（逐项 before→after，详见 diff 件）：

| # | 位点（R4 行号） | before（R3） | after（R4） |
|---|---|---|---|
| 1 | L319 §7 标题 | Case Study: **An Anonymized** Engineering Instance | Case Study: **An** Engineering Instance |
| 2 | L321 §7 开头段 | 「identity is anonymized in this edition and to be restored in a revised version…(replaced below by the marker ``anon''); full names, path prefixes, and the public pointer are withheld…available from the author on request…byte-identical modulo the declared `anon` substitution」 | 「a public engineering project, the Deposon project, whose identity was anonymized in the previous edition and is restored in this revised edition…restoration covers the project's name, the fictitious entity's name (the Deposon)…path prefixes, and the public pointer: the repository github.com/zeroandcat/Deposon at the citation-frozen commit…byte-identical to the frozen record, now printed at their repository-relative paths with the previous edition's `anon` substitution retired」 |
| 3 | L325 S 段 | a fictitious scattering entity **(anonymized here)** | a fictitious scattering entity, **the Deposon**, |
| 4 | L336-347 表 2 | 2 列（件名短名＋SHA-12），宽 0.88 | 3 列（**仓相对路径**＋SHA-12＋**字节**），宽 0.94；五锚逐条：`docs/GT_FORMALIZATION_v1.md` 19,100 B / `run_v21_gtformal.py`（仓根）16,600 B / `run_v22_p1c.py`（仓根）7,236 B / `docs/SPEC_GT2B.md` 3,318 B / `docs/SPEC_GT8C.md` 6,326 B |
| 5 | L368-371 表 3 | `results/anon_benchmark_v1_4_gsm8k.json`、`results/anon_v22_p1c.json`、`results/anon_v21_gtformal.json` | `results/deposon_benchmark_v1_4_gsm8k.json`、`results/deposon_v22_p1c.json`、`results/deposon_v21_gtformal.json` |
| 6 | L397-398 表 4 | `results/anon_v22_e95ci.json`、`results/anon_benchmark_v1_4_gsm8k.json`、`results/anon_v20_crossval.json` | `results/deposon_v22_e95ci.json`、`results/deposon_benchmark_v1_4_gsm8k.json`、`results/deposon_v20_crossval.json` |
| 7 | L381 §7.2 | kimi 重算件印短名 `_kimi_ftfb_s7_independent_recompute_2026_09_18.json` | 实名全路径 `_september_workspace/results/_kimi_ftfb_s7_independent_recompute_2026_09_18.json`（＋「deposited in the public repository at the citation-frozen commit」）；gsm8k/crossval 两件同步实名 |
| 8 | L375/L401 两表 caption | 「byte-identical … modulo the declared `anon` substitution」 | 「byte-identical to the frozen record at the repository's citation-frozen commit」 |
| 9 | L132 等四处 | —（R56 类，见「范围边缘修正」节） | —（见后） |

**五锚与数字源件在 a57d7fe 的逐件复核**（本人实测 sha256sum，与差异清单 §2 一致）：

| 仓相对路径 | 字节 | SHA-12 | 差异清单判定 |
|---|---|---|---|
| docs/GT_FORMALIZATION_v1.md | 19,100 | aeefb8ef6972 | ✓ 一致 |
| run_v21_gtformal.py | 16,600 | 9bbe43f41fa8 | ✓ 一致 |
| run_v22_p1c.py | 7,236 | 6e9673205dc0 | ✓ 一致 |
| docs/SPEC_GT2B.md | 3,318 | 68a5b08ef007 | ✓ 一致 |
| docs/SPEC_GT8C.md | 6,326 | 6b09de9911c0 | ✓ 一致 |
| results/deposon_benchmark_v1_4_gsm8k.json | 2,741 | 5cd6269d7baf | ✓ 在仓 |
| results/deposon_v21_gtformal.json | 69,204 | 9d9ae5001c57 | ✓ 在仓 |
| results/deposon_v22_p1c.json | 763 | 2bed4de3a57c | ✓ 在仓 |
| results/deposon_v22_e95ci.json | 1,496 | 928bcfbdb7c3 | ✓ 在仓 |
| results/deposon_v20_crossval.json | 8,404 | 76479b7a5ed6 | ✓ 在仓 |
| _september_workspace/results/_kimi_ftfb_s7_independent_recompute_2026_09_18.json | 3,605 | 879db0217f04 | ✓ 与 §7.2 印刷前缀一致 |
| _september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md | 84,388 | 543479649b3e | ✓ 在仓（handoff 字段人读载体） |

（表 2 新增字节列为差异清单 §4.1 方案 B 明示口径「GitHub 相对路径＋新 SHA-12＋字节」；SHA-12 五值与基线印刷值逐字相同——数值零漂移的实证。）

### 项 2｜HANDOFF_MACHINE_READABLE.json 缺件处置（差异清单 W2）

- **现实**：仓内无此件（kimi 重算件以其为 source_of_truth，字段现由源稿 md（人读）＋kimi 重算 json（第二手）承载）。**不得编造，未替作者补造任何字段。**
- **处置**（按公开面可得锚改挂）：
  - L329 P 段：「(frozen handoff artifact, field `preregistration_anchors_sha256_12`)」→「(handoff record, field `preregistration_anchors_sha256_12`; **the record's public carriers and pending machine-readable carrier are declared in §7.1**)」。
  - 表 3/表 4 五处「frozen handoff artifact, field X」→「handoff record (§7.1), field X」。
  - L357 §7.1 新增载体声明句：「The handoff record's machine-readable carrier is not part of the public repository; its fields are carried, values identical, by the archived source markdown, were re-verified item by item by the third-party recompute record (§7.2), and the carrier's deposition is pending (Appendix).」
  - 附录 availability terms 增补：「Two declared gaps: the handoff record's machine-readable carrier and the 2026-08-30 audit record are not part of the public repository; their fields and values are carried by the archived source markdown and the recompute record, and their deposition is pending.」
  - 源稿 md 实名全路径在附录 availability terms 单点钉死：`_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md`。
- **pending 登记**：见第三节 P1。

### 项 3｜AUDIT_2026-08-30.json 缺件处置（差异清单 W3）

- **现实**：仓内无此件；其 occurrence/outcome 由 handoff record 的 audit 字段（源稿 md 承载）与 kimi 重算件的 `prior_independent_audit` 字段（引其为首次独立重跑）双载。
- **处置**（降格表述，如实）：L381 §7.2 于 2026-08-30 审计句后新增：「**That rerun's own log is not part of the public repository; its occurrence and outcome are carried by the handoff record's audit field and cited as its prior by the second recompute's record below, and the log's deposition is pending (Appendix).**」
- **pending 登记**：见第三节 P2。

### 项 4｜仓内 FTFB 版本滞后两代的陈述修正（差异清单 W4）

- **现实**：仓内归档面 `_archive_2026_09_20/` 存 v3（23 页，356,123 B，`2D9EDC8C7303`），落后提交面（v4/终版，24 页）一代、落后验收面（R3 重打包，24 页）两代。
- **处置**（陈述层）：附录 availability terms 新增版本现实句：「The repository additionally archives an earlier, 23-page edition of this paper (`…_archive_2026_09_20/fiction_that_feeds_back.pdf`, 356,123 bytes, SHA-256 prefix `2d9edc8c7303`); this revised edition supersedes that archived edition, and no measurement artifact differs between the two — the supersession touches only the paper's own text.」——读者可循公开仓实测核对该归档本指纹，版本口径与公开现实对齐。
- **动作面**（归档三件同位刷新）＝ **pending**：见第三节 P3；触发第三作 v0.1 联动换锚（见同包《查理_第三作v0.1联动换锚清单_2026-09-27.md》）。

### 项 5｜availability「confidential channel」表述改公开仓现实（差异清单 W5）

**改写位点 6 处**：

| # | 位点 | before（R3） | after（R4） |
|---|---|---|---|
| 1 | L75 摘要 | 「the full frozen record and digests are available from the author on request, public availability deferred to a revised version」 | 「the frozen artifacts and full digests are deposited in a public repository, cited at its frozen commit」 |
| 2 | L315 §6.4 | 「in this edition, third-party executability runs through the full digests available from the author on request (§7.1), public executability is deferred to a revised version…The requirement is therefore only partially met in this edition.」 | 「in this revised edition, third-party executability runs through the public repository and its full digests (§7.1)…The requirement is met in substance on that public record, with the machine-readable handoff carrier and the first audit record pending deposition (§7.2).」 |
| 3 | L357 §7.1 E 段 | 「A reader working from the public text alone cannot execute the recomputation…That demand is now half met…while public availability of the record remains deferred to a revised version.」 | 「A reader working from the public text and the public repository can now execute the recomputation that M4 asks of a third party — hashing the five anchors of Table 2…tracing every field path of Tables 3 and 4…That demand is now met in substance…record is public at the citation-frozen commit (Appendix).」 |
| 4 | L435 §8.3 | 「that availability runs through the on-request channel declared in §7.1 until a revised version; whether the offer is taken up…」 | 「that availability now runs through the public repository declared in §7.1; whether any reader takes the recomputation up is outside the authors' control (§7.1, §7.2).」 |
| 5 | L494 附录 availability terms | 「The complete frozen repository and the full SHA-256 digests…available from the author on request in this edition; the public pointer is deferred to a revised version…」 | 全段重写：公开仓 URL（github.com/zeroandcat/Deposon）@ commit `a57d7fe`（引用冻结口径：所有仓内引文在该 commit 解析、后续仓史不影响）＋仓内含物清单（五锚/数字源件/源稿 md/重算件）＋归档旧版句（项 4）＋两缺件句（项 2/3）＋检索快照 on-request 保留（不在仓，如实） |
| 6 | L488 检索快照 | 「available from the author on request in this edition, under the availability terms stated below」 | 保留（快照确不在公开仓；与新版 availability terms 中 on-request 分支一致） |

**说明**：原稿「请求方是否接受 offer 不在作者控制」句改写为「公开面是否被取用不在作者控制」，原自谦边界保留；M4 可执行性从「半满足」升为「实质满足＋两缺件如实声明」，与 kimi 重算件 limitation 声明（不证明 freeze ordering）不冲突——freeze ordering 仍为作者自证（附录 Anchor standing 段零改动）。

---

## 二、范围边缘一致性修正（超出 5 项字面范围，单列披露）

**R56 恢复承诺句歧义消除**（4 处：L132、L292、L500、L603）：「to be restored in a revised version」→「to be restored in a **later revised edition**」。

- 动因：本版自身即「revised edition」且**未**恢复 R56（按差异清单 §4.3，R56 处置沿既有清单、留 camera-ready）；原句在本版语境下产生「本版应已恢复」的字面歧义，属 on hold 审稿方可挑剔的内在矛盾。
- 策略零变化：R56 匿名条目、on-request 可得性、作者自证（非独立核验）标注全部原样保留。
- 附观察（供用户拍板，非本版动作）：companion 全文本已在公开仓 `paper/` 目录在位（`paper/deposon_paper_final_en.md` 等），R56 恢复实名与否及匿名条目与公开现实的口径选择，留 camera-ready 轮（沿差异清单 §4.3 与 §5-④）。

---

## 三、pending 项如实登记（仓内无载体/待授权/待后续轮）

| # | 项 | 触发条件 | 责任侧 |
|---|---|---|---|
| P1 | HANDOFF_MACHINE_READABLE.json 归仓 | PI 授权（若件在 PI 本地面）→ 归仓后 §7.1/附录「pending deposition」可再升级为实名件直挂（差异清单 §5-⑤） | 用户/PI |
| P2 | AUDIT_2026-08-30.json 归仓 | 同上（§5-⑤） | 用户/PI |
| P3 | 归档三件（pdf/tex/source）同位刷新 `_archive_2026_09_20/` | 解 hold 后执行；新 SHA/字节/页数落库即触发第三作 v0.2 联动换锚（本包联动清单） | 用户/排版轮后 |
| P4 | pdflatex 三遍四零＋页数实测 | 排版轮（戴夫）；本环境无 pdflatex；tectonic 因引擎不兼容无法编译（R3 基线同样失败于 L27 `newunicodechar/utf8` 在 XeTeX 下的预置不兼容，非本次改动引入） | 戴夫 |
| P5 | kimi 式独立重算复跑（五锚＋12 数字锚＋9 溯源抽查） | 引用面改写后按差异清单 §3.3-R2 建议 | 鲍勃 |
| P6 | 实际提交版确认（v4/终版/更晚） | 差异清单 §5-①；本版以 R3 重打包为基＝最新验收面；若 arXiv 侧确认提交面为终版，两者引用面零差异（diff 仅摘要段），影响限于摘要层 | 用户 |
| P7 | on hold 修改要求（arXiv 审核意见） | 差异清单 §5-②；仓内无载体，本版按差异清单口径先行改写，若 arXiv 有具体意见需再叠一轮 | arXiv 侧 |
| P8 | R56 恢复实名决策 | camera-ready 轮（含 paper/ 目录公开现实的口径选择） | 用户 |

---

## 四、纪律自检（四门全过）

1. **verdict 字面零改动**：三判定句（「The conservation identity survives audit.」/「The dynamical tier dies.」/「All three formalized dynamical-equivalence propositions are falsified.」）与 §7.4/§9.1 评分行、Appendix「Anchor standing」段均不在 diff 触及范围——byte-identical。
2. **12 组数字锚一字不动**：全文数值 token 对比（R3 vs R4），新增仅引用层（表 2 字节×5、附录归档行 356,123/2d9edc8c7303、日期 09-18→09-27×2、表宽 0.88→0.94、节指针 §7.1/§7.2），移除仅旧表宽与两日期位；2.220446049250313×10⁻¹⁶、4/3、20/22、61、6,760、338、20、0.8569、−1.0、0.669、0.87/0.85/p=0.5、0.899/0.899/p=1.0、±10pp、0.97/0.85、0.484→0.452、0.783→0.739、5/5 全部零漂移。
3. **冻结件零触碰**：shared/戴夫_FTFB_R3排版重打包_2026-09-18/ 未动；仓内五锚、数字源件、归档三件只读复核（sha256sum），零写入。
4. **结构自检**：`\begin/\end` 环境配对全平；`\ref`→`\label` 全闭合；花括号平衡；`anon_` 残留 0；`frozen handoff artifact` 残留 0；`deferred` 残留 0；「on request」残留 6 处均为 R56 条目（4）＋检索快照（2）——策略性保留。

## 五、摘要 1,920 字符合规核验（arXiv 贴入口径）

- R3 基线：1,846 字符（空白归一化）→ **R4：1,822 字符，裕度 98，PASS**（摘要环境内 raw 同为 1,822）。
- 摘要唯一改动＝availability 从句（净 −24 字符，见项 5 位点 1）。

## 六、arXiv 重投元数据要点（贴给提交面）

- **Date**: 2026-09-27
- **Comments** 建议：`24 pages; R4 revision edition: public-record citation switch (repository-relative paths at the frozen commit); availability terms updated; measurement anchors unchanged`（页数以排版轮 pdflatex 实测为准；R3 为 24 页，本版净增约 3 KB 文字，预计 24 页不变）
- **Subjects / License / Conflicts**：不变（cs.AI primary; physics.hist-ph; cs.CY / CC BY 4.0 / none declared）
- **摘要**：自 tex abstract 环境逐字粘贴（1,822 字符空白归一化）

---

—— 查理-论文主笔 ｜ 2026-09-27 02:34 接单，03:0x 落版 ｜ AI 生成
