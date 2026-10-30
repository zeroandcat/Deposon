# 《2》走读件（先行 · 2026-10-29）

## §0 已确证缺陷（先行 · 落盘时点 12:1x）

| # | 何处（件＋行） | 何病 | 严重度 | 是否已修 |
|:-:|:--|:--|:--|:--|
| 1 | `tools/rag_index.py:52-65`（对照其自述 `:5-6`、`:19-20`；另核 `tools/rag_map.py:35-39`） | `targets()` 实扫仅 `results/` 根层 `*.md` 与 `pi_rulings/*.md`，不递归 `results/` 子目录，也未纳入其自述之两份备忘录；大量在册件因此不能进入通用索引。`rag_map.py` 仅映射三册，不构成通用递归索引之修复。 | 高 | 未修（待以新件直接修复） |
| 2 | `tools/rag_index.py:85-90` | 更新 `heading` 时对块内任一标题都写入 `i+1`，而非该标题在块内的实际行号；同一块含多个标题时还会全取末者并共享同一错行号，导致检索回指错位。 | 高 | 未修（待以新件直接修复） |
| 3 | `tools/rag_index.py:73-78` | `raw.decode('utf-8', errors='ignore')` 静默丢弃非法字节；异常又经裸 `except Exception: continue` 跳过，索引可在无警报下缺内容、缺文件，破坏“未找到”的可解释性。 | 高 | 未修（待以新件直接修复） |

## §0-A 追加确证与首批修复登记

**#1–#3 已修**：新立 `tools/rag_index_stage2_fix_2026_10_29.py`，不改旧件；新索引 `results/.tmp/_rag_index_stage2.jsonl` 实测 2,137 件／18,276 块／错误 0。合成正控通过（跨块标题 `L3`、`L45`、非法字节登记、防覆盖）；实仓正控「接递之式」命中嵌套件，阴断 `__STAGE2_DEFINITELY_ABSENT_9f3c7a__` 0 命中。

| # | 何处（件＋行） | 何病 | 严重度 | 是否已修 |
|:-:|:--|:--|:--|:--|
| 4 | `tools/rag_map.py:46`（漏读实例：`results/work/process/_experiment_tree_v2_main_2026_10_23.md:3281`、`:3330`、`:3393`） | `RE_HEAD` 只识别 `##`／`###`，不识别一级 `#` 标题，致使树册 §60-90／91／92 等节不进入映射。以同一当前字节快照对照，新增规则另捕得树册 4 个、主册 4 个、子册 1 个一级标题（含各册题名）。 | 高 | 已修（新立 `tools/rag_map_stage2_fix_2026_10_29.py`） |
| 5 | `tools/rag_map.py:96-98` | 与旧通用索引器同类：`errors='ignore'` 静默丢字节，缺内容时无错误登记。 | 高 | 已修（同上；新错误清单实测 0） |

**#4–#5 修复验证**：新映射 `results/.tmp/_rag_map_stage2.jsonl` 在盘；同字节对照证明一级标题已纳入，而非把并发追加造成的差值冒充修复效果。

## §0-B 工具实现之追加缺陷

| # | 何处（件＋行） | 何病 | 严重度 | 是否已修 |
|:-:|:--|:--|:--|:--|
| 6 | `tools/distortion_calculator.py:98-99`、`:305-356`、`:628-671`；最新口径见 `pi_rulings/_pi_card_answers_register_2026_10_29_v613.md:73-80` | `max_u` 之默认与文档仍作单值 `1`，公开适配面未落实族级 `U-C3`；族级 4／9 亦不在原自测面内。原函数虽可接收 `c`，但当前实现与最新族级口径之间缺少明确适配层。 | 高 | 适配层已修（新立 `tools/distortion_calculator_family_c_stage2_2026_10_29.py`）；原锚与生产调用面未改 |
| 7 | `tools/llm_client.py:120-144` | 选项解析使用 `opt in content or content in opt`，会把单字母、解释性句子等误配为合法选项，直接改变决策归属；与“只返回选项文本”的契约不符。 | 高 | 严格解析层已修（新立 `tools/llm_client_strict_stage2_2026_10_29.py`）；原客户端与凭据面未改 |

**验证**：#6 之族级分母、无守卫分母、差值式与产表行精确测试均 PASS，原锚自测 9/9 PASS；#7 仅接受去空白后的精确选项，单字母、解释句及无关串均显式拒绝，真实 API 调用与凭据读取均为 0。

## §0-C 全量 AST 扫描之实证

扫描射程：三根共 2,267 个 `.py` 文件，逐件只读 `ast.parse`，未执行脚本。417 件首行 BOM 导致 `invalid non-printable character U+FEFF`；另三件非 BOM 语法错误如下。

| # | 何处（件＋行） | 何病 | 严重度 | 是否已修 |
|:-:|:--|:--|:--|:--|
| 8 | `.tmp/_n6_trim2_2026_10_27.py:83`、`:94` | 两处多余右括号，`ast.parse` 报 `unmatched ')'`，脚本不可解析。 | 中 | 已修（新副本 `.tmp/_n6_trim2_stage2_fix_2026_10_29.py`，AST PASS） |
| 9 | `.tmp/_n6_trim5_2026_10_27.py:101` | 一处多余右括号，脚本不可解析。 | 中 | 已修（新副本 `.tmp/_n6_trim5_stage2_fix_2026_10_29.py`，AST PASS） |
| 10 | `〔归档区〕/scripts/tool/generator/clean_footnote_hrule.py:3` | 文档字符串前缀写成 `rr"""`，属于确定语法错误。 | 中 | 已修（归档内新副本 `clean_footnote_hrule_stage2_fix_2026_10_29.py`，AST PASS） |
| 11 | 三根 Python 语料之 417 件（上述 AST 扫描全集；错误行均为首行） | 带 BOM 的脚本在当前 Python 解析器下首行即失败，非单纯编码美观问题。 | 中 | 未修（须逐件用途甄别并副本化；不以 417 件批量改写充修复） |

## §1 全量走读射程与方法

1. **三根全量机械覆盖**：`deposon-repo` 5,380 件、`deposon-sub` 1,275 件、归档区 40,360 件，合计 **47,015 件／1,778,413,557 bytes**；读取错误 0。七项必需正控文件均存在，合成阴断路径不存在。此计数来自 `.tmp/_stage2_inventory_2026_10_29_summary.json`。
2. **Markdown 全量索引**：`results/**/*.md` 与 `pi_rulings/*.md` 共 **2,137 件／18,276 块**，严格 UTF-8 错误 0；新索引证明子目录与三册可被检索。
3. **Python 全量 AST**：三根 **2,267 个 `.py`**，只读解析、未执行；发现 417 件首行 BOM 错误与 3 件其他语法错误。417 件不直接等于 417 个应修现行工具，故只单列其处置而未批量改写。
4. **重点逐行开卷**：`AGENTS.md`、《体例之正》、树册／主册／子册末段、`distortion_calculator.py`、`exp_harness.py`、`rag_index.py`、`rag_map.py`、`llm_client.py` 与最新裁答 `v610`–`v613`。
5. **诚实射程**：本次采用“全量机械走读＋高风险处逐行开卷”，**不声称 47,015 件均已逐字人读**。重复指纹、BOM／CR／U+FFFD、无对口与无锚只作审查线索；未逐件分类前，不以总数直接判为缺陷。

## §2 修复与剩余工作之归口

- §0 共列 **11 项确证缺陷**：高严重度 7 项、中严重度 4 项。
- **R-01–R-10 已形成新修复层**，详见 `results/verdict/judgement/_stage2_repairs_2026_10_29.md`。
- **U-01–U-07 尚需后续处置**，详见 `results/verdict/judgement/_stage2_unrepaired_2026_10_29.md`。
- 本件只登记走读与直接修复，**不宣告任何零、门槛成就、《1》毕或《2》毕，不销记，不落／改五终判词**。
FINAL_SELF_REPORT: bytes=00006918; SHA-12=45b5efa4fa72; Test-Path=True; Get-Item.Length=00006918; BOM=0; CR=0; U+FFFD=0; LAST_BYTE=0x0a; ZEROED_FIELD_CONVENTION
