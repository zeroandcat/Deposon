# 戴夫·第三作 v0.4 排版轮交付报告（口径注册轮：tex 转换＋保真检查）

**日期**：2026-09-28
**执行**：戴夫-格式专家
**任务书口径**：本轮仅做 md→tex 转换＋保真检查两件；**不做** 8-gram、**不回填** R8/§22.5、**不编译**（三件均留待鲍勃重测值到位后的终收尾轮）。

---

## 一、对象与交付物指纹

| 件 | 指纹 | 说明 |
|---|---|---|
| 源 md：`shared/_v3v4_merged_paper_2026_09_27_v0.4.md` | 191,119 B / 1008 行 / SHA-256-12 `e6c76f9be292` | 与派单一致，转换前核验通过；完整值 `e6c76f9be292cef66f448cf72a1493d5b5401dee4bcd05f7cd5fed583011bcaa` 已写入 tex 头部注释 |
| 交付 tex：`shared/戴夫_第三作排版交付_2026-09-28/_v3v4_merged_paper_2026_09_27_v0.4.tex` | 210,168 B / 872 行 / SHA-256-12 `4b513e2dc6e6` | 脚本化生成（`build_third_tex_v3.py`，断言内建，可复跑复验） |

**v0.3 交付目录零触碰**（`shared/戴夫_第三作排版交付_2026-09-27/` 未动）。

## 二、转换方法

体例沿 v1.1 tex 模板与 v0.3 轮 v2 转换器全量逻辑（pdflatex / 11pt article / T1-fontenc+lmodern / booktabs / geometry 1in / CJKutf8 / hyperref(unicode)；引用保留 `[n]` 字面数字体系；References 以 `\noindent\hangindent` 条目排；SHA-12 走 `\sha{}`；verdict 字面纯文本不引入 `\hit` 宏）。

**v3 转换器相对 v2 的适配**（源件为注册层改动，10 hunk）：

1. **表 23→24**：新增表 idx 22 = App A「R4 re-adjudication evidence」五行表（Item/Bytes/SHA-12 三列 longtable，spec 沿 21 号 Merged-draft input anchors 同构）；原 22 号（App C.1）平移为 23。列数断言在转换器内建通过，colspec 花括号自检 24/24 PASS。
2. **PREAMBLE 事实字段**：头部注释与 `\date` 更新为 v0.4 / 2026-09-28 / 源 SHA-256 全值；**R8 与 §22.5 的 deferred 声明两句逐字沿旧**（机器比对 `v0.3 tex ↔ v0.4 tex` 逐字相等）。
3. **零新增非 ASCII 字符**：v0.4 相对 v0.3 字符集差为空（× U+00D7 于 v0.3 已在场，走 utf8.def→\texttimes 原生渲染路径），Unicode 声明层零改动。
4. 其余（inline 状态机、书签净化、行首 `[L]`/`[R]` 前置空组、表格转义）零改动沿用。

**tex 侧改动面审计**：v0.3 tex ↔ v0.4 tex diff 共 12 hunk，逐个核对全部对应计划内改动——md 侧 10 hunk＋PREAMBLE 事实字段（3 行合并 1 hunk）＋`\date`（1 hunk）＋一处 pdfbookmark key 行号平移（`substar914`→`substar916`，系转换器以 md 源行号为 key 的机械后果）。**零计划外漂移**。

## 三、保真检查结果（沿 v0.3 轮 20 项标准＋v0.4 注册层专项，共 27 项，FAIL 0）

**沿旧 20 项**（口径与 v0.3 轮一致，词边界精确 token 计数）：

| # | 检查项 | 结果 |
|---|---|---|
| 1 | F 系 22 项数值 token（30 token 覆盖）md↔tex 计数 | PASS，全部相等 |
| 2 | F1 two-composite 定性项（composite 计数） | PASS，md=26 tex=26 |
| 3 | verdict 五族字面（FAIL×32 / hit×9 / TRIGGERED 净×4 / NOT TRIGGERED×10 / composite×26） | PASS，md↔tex 全等 |
| 4–7 | References 64↔64：条目数、编号集 {1..64} 闭合、正文引用闭合、条目-引用互达 | PASS ×4 |
| 8 | E-37 两处注记 token 级比对（§13.3 E-37.2：79 token；§14.2 E-37.1：72 token） | PASS，逐位一致 |
| 9–18 | 结构 10 项：Part I/II/III、App A/B/C、References 节、表环境 **24 个**（tabularx 14＋longtable 10）、编号表 caption 4 条（Table 1/2/4/5；Table 3 跳号=未刊综述源件引用，本稿无本体）、Table 1–5 文字引用计数、**v0.4 新节 C.0.2 在场**、**v0.4 新节 R4-evidence 在场** | PASS ×10 |
| 19–20 | 占位保留原样：§22.5 自重叠披露占位＋App C R8 注册行 | PASS，tex 中原样在场（未回填，断言双在场） |

**v0.4 注册层专项 7 项**（本轮新增，派单规定）：

| # | 检查项 | 结果 |
|---|---|---|
| 21 | R4-evidence 表 10 项新数值 token md↔tex 计数 | PASS：15,247 / 11,609 / 28,207 / 21,869 / 292,215 / B70211BFA83E / C8D539A58D29 / 9BB22099DB3B / A5C33BD45D78 / 083087218A8D 各×1 |
| 22 | signoff 双指纹字面 md↔tex 计数 | PASS：26,637×3、BA4D07BD7000×3、26,633×1、739245682D40×1（md 基准，两侧全等） |
| 23 | **注册层 10 hunk 逐块 token 级比对** | PASS，各块逐位一致（明细见 §四） |
| 24 | R4-evidence 表 5 行×3 列 cell 级 token 比对 | PASS，15/15 cell 逐位一致 |
| 25 | tex 头部事实字段（版本 v0.4 / 日期 / 源 SHA-256 全值 / `\date`）与 v0.4 源一致 | PASS |

## 四、注册层 10 hunk token 级比对明细（第 23 项展开）

比对方法：tex 侧经归一化（剥 `\sha`/`\path`/`\textbf` 等命令壳、还原转义与引号映射）后与 md 侧（剥 `**` 与反引号标记）做空白归一 token 序列逐位比对；表格按 cell 级展开。一处提取口径注记见 §五.3。

| hunk | 内容 | token 数 | 结果 |
|---|---|---|---|
| H1 | L3 版本行（v0.4 轮身份句） | 50 | 逐位一致 |
| H2 | §21(6) 轮次史句（加 v0.4 注册轮） | 206 | 逐位一致 |
| H3 | §21(9) 轮次史句（v0.4 next-day registration round） | 191 | 逐位一致 |
| H4 | App A 前导句（v0.4 行测量口径分号扩展） | 115 | 逐位一致 |
| H5 | **signoff 双指纹注记**（E-37 先例句起至 `pending the PI's ruling)`） | 73 | 逐位一致 |
| H6 | **v20_baselines 废版注记**（E-40.2） | 91 | 逐位一致 |
| H7a | R4-evidence 节前导段（两 on-repo 行＋三 letters 行口径） | 40 | 逐位一致 |
| H7b | R4-evidence 表（5 行×3 cell） | 15 cells | 逐位一致 |
| H8 | C.0.2 注册节（(i)–(iv) 全量） | 367 | 逐位一致 |
| H9 | **C.3 R4 条目**（pending-proof placeholder → registered 整条重写） | 484 | 逐位一致 |
| H10 | C.4 v0.4 注记（provenance disclosures 句） | 88 | 逐位一致 |

## 五、口径注记（如实披露）

1. **F 系 md 基准计数随注册层合法变化（2 token，+1 each）**：`239,387` 由 ×2 → ×3、`849D76BE3A06` 由 ×3 → ×4，增量各 1 处、全部来自 App A R4-evidence 表 PI-side 行（「the on-repository file at this path remains v19 (239,387 B, `849D76BE3A06`, E-1 through E-36...)」）。此为查理 v0.4 计划内注册内容，非转换漂移；本轮保真标准为 md↔tex 全等，两侧同步、检查通过。
2. **signoff 双指纹计数变化**：`26,637` 与 `BA4D07BD7000` 各由 ×1 → ×3（行值 1＋v0.4 注记内 cited pair 2 处表述），`26,633` / `739245682D40` 不变 ×1；两侧全等。
3. **token 比对尾部列表标记剥离口径**：H9 块的结束锚为下一列表项（R5）开头时，块尾带入 md 的 `-` 与 tex 的 `\item` 结构标记（转换器插入件，非内容 token），两侧分别剥离后再比对（仅匹配换行后标记形态，不触及正文字面）；正文 token 全位一致。
4. **计数口径差沿 v0.3 轮注记**：本报告用词边界精确 token 计数（与鲍勃子串口径的两处差异沿旧：`0.75`×11 vs 其 ×14；`500`×1 vs 其 ×4），非稿面变化，不影响 md↔tex 全等结论。
5. **`×`（U+00D7，R4 条目「145.8×」）**：沿 v0.3 已有渲染路径（utf8.def→\texttimes，lmodern 字形），v0.3 轮编译零错误已验证该路径；本轮不编译，编译级验证留待下轮。
6. **md 数值对冻结锚复测**沿旧以鲍勃审读报告为准（其 v0.4 修订记录申报五族字面与 F 系全等）；本轮职责边界为 md↔tex 转换保真。

## 六、交付物清单与下轮衔接

| 文件 | 说明 |
|---|---|
| `shared/戴夫_第三作排版交付_2026-09-28/_v3v4_merged_paper_2026_09_27_v0.4.tex` | 交付件 1：v0.4 全文 tex（R8/§22.5 占位逐字保留，deferred 声明沿旧） |
| `shared/戴夫_第三作排版交付_2026-09-28/戴夫_第三作v0.4排版保真检查报告_2026-09-28.md` | 交付件 2：本报告 |
| 私有工具链 `agents/.../third_paper_v04/scripts/` | `build_third_tex_v3.py`＋`fidelity_check_v04.py`（可复跑复验；check_colspec 沿用 v03 轮脚本，24/24 PASS） |

**下一轮（终收尾）衔接**：待鲍勃 8-gram 重测值到位后——R8（App C 注册表）与 §22.5 披露句回填 → 三遍编译定稿（含 v0.3 轮遗留 49 警告的 Overfull/Underfull 处理）→ 双盲合规终审（metadata / 页眉页脚 / 书签 / 字体嵌入）。届时源件若为 v0.5（回填轮），沿用本轮「注册层专项」框架按新 hunk 展开即可。

（自查链：源件指纹核验 → 10 hunk diff 复算对齐查理申报 → 字符集预扫（零新增）→ 脚本化转换（占位断言双在场）→ colspec 24/24 → tex↔tex 改动面审计（12 hunk 全对应计划内）→ 保真 27 项零 FAIL → 落库＋v0.3 目录零触碰。）

—— 戴夫-格式专家 ｜ 2026-09-28 ｜ AI 生成
