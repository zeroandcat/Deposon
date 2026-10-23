# 鲍勃：GLM V2 回函模板待填栏值清单（deposon 线对应项实测，2026-09-18）

- **版本：R5 刷新版（GATE-R5-B-20260918，17:29 派单；R4 旧值已存档见文末）**
- 依据：用户裁定「模板所待『GLM 完稿 V2』即本 deposon_v3_final」；对齐对象＝挂载仓 `results/_glm_response_v2_template_2026_09_18.md`（SHA-12 972401e056f6，只读零改动）＋`shared/鲍勃_GLM完稿V2回函模板事实核验_2026-09-18.md` 基准。
- 纪律：挂载仓只读，不直接改模板；0 LLM；全部值为本轮本机实测。
- 用途：供填入/转呈回函模板的可机械复算待填栏；FTFB 专属栏如实标注「非本线对象，不适用」。

---

## §2.1「GLM 完稿 V2 状态」待填栏（deposon 线对应值，R5 终版）

| 模板待填栏 | 填入值（实测） | 备注 |
|---|---|---|
| 完稿提交时间 | **2026-09-18 17:27**（R5 重建轮戴夫交付消息 17:27:43；盘上交付件 mtime 17:25） | R4 轮旧值 11:17 已存档 |
| 新指纹 SHA-256（tex） | `95fc9ba9a1a497ec1cf2172277285dcfc305f11953db19a4bd60b4ca23f6dba5`（52,877 B） | deposon_v3_final.tex（R5） |
| 新指纹 SHA-256（PDF） | `3b792178acbcc041441f22fc5351db388fe70f995ee5d449934221533d34de5a` | R5；指纹链 42e4310f→1dd27184→95fc9ba9→3b792178 全长实测一致（注：模板原比对基准 d060f75dbe9f 为 FTFB v3 快照，非本线对象） |
| pdflatex 三遍四零 | 本机无 pdflatex，**如实标注不可独立复算**；旁证全测：未定义引用 0、字体 88 行全嵌入、Type3＝0、页数 12 与交付记录一致 | 四零全绿（交付记录＋旁证） |
| 摘要字符数（≤1,920 阈值栏） | deposon 线为中文摘要：**CJK＝260**（摘要不联动，R4→R5 不变） | 1,920 阈值为 FTFB 英文摘要口径，**非本线口径** |
| 正文词数（降幅≥15% 栏） | **非本线对象，不适用**（deposon 线全稿 CJK＝7,743，与 FTFB 词数基线 12,286 不可比） | |
| 页数 | **12 页（838,422 B）** | 基线 24 页为 FTFB 口径，不适用比对 |
| 5 锚不变式（aeefb8ef6972 等） | **非本线对象，不适用**（fiction_that_feeds_back.tex 专属锚） | |
| 池数（55+1=56/56+1=57） | **非本线对象，不适用**（FTFB 参考池口径；deposon 线文献 44 条） | |
| 修订块新旧行号对照 | R5 两 hunk：A-2 md L178→tex L193（PDF 第 8 页）、A-1 md L224→tex L235（PDF 第 9 页）；AM1：md L226→tex L236（＋§3.3 L154）；AM2：md 附录 A 末→tex L315；tex 头部另有 R4→R5 溯源注释 4 行（2 hunk，构建元数据非内容） | R5＝R4＋2 hunk/362 字符（两句逐字）；增量≡全量双保险：r6 构建器全管线重跑≡增量 tex（逐字节，S2 记录核对属实） |
| underfull 残余 | **已如实记录**：9 处（badness 1048–10000；与 R3/R4 轮同数同落点） | 披露项，非门禁 |

## R4 轮旧值存档（GATE-R4-B，11:17 终版，已被 R5 取代）

- tex `14c067a8671bb71a5bcf5ebbd9b3e32f508582a97f7e96893b69acf568da1756`（52,034 B）／PDF `f60da69607ee566a4c997d6e5e8687093b5915d9a42ece6f9f817867181176de`（12 页，833,171 B）／全稿 CJK 7,597／完稿时间 11:17。全套原件在 `dave-v3-final-20260918/archive_preR5_20260918/`。

## §2.5 五制品 SHA-12 待填栏（GLM 完稿后实测；R5 轮挂载仓只读复算，仍 5/5）

| 制品 | 挂载仓路径 | 实测 SHA-12 | 模板冻结值 | 判定 |
|---|---|---|---|---|
| KIMI | `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` | `efe05ad775de` | EFE05AD775DE | **MATCH** |
| GLM_1 | `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | `268ab1239a8a` | 268AB1239A8A | **MATCH** |
| GLM_2 | `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` | `39732a92b5c9` | 39732A92B5C9 | **MATCH** |
| coze | `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` | `fee04170aa73` | FEE04170AA73 | **MATCH** |
| minimax | `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | `9e1ccbdceacc` | 9E1CCBDCEACC | **MATCH** |

**5/5 全 MATCH**，冻结体系零触动。（路径附注沿我核验报告：模板写 `by_model/KIMI/`，盘上实为小写 `kimi/`；Windows 大小写不敏感能过，Linux 字面路径会 miss，填值时建议按实况。）

## §2.6 16 frozen anchors 待填栏（R5 轮逐件复算，仍 16/16 MATCH）

| # | 锚（路径域） | 实测 SHA-12 | # | 锚 | 实测 SHA-12 |
|---|---|---|---|---|---|
| 1 | verifier/handoff/KT_ABC1 | `03c6c01f3697` | 9 | corpus/v20/index.json | `8423ffe266af` |
| 2 | docs/V3X/KT_A1_SPEC | `78b71d404366` | 10 | verifier/handoff/P_F_PRED | `b41c98bf90cc` |
| 3 | docs/V3X/KT_B1_SPEC | `0410ca0fbdae` | 11 | docs/V3X/P_F_SPEC_V0 | `de90faf362c5` |
| 4 | docs/V3X/KT_C1_SPEC | `59d8f56347d5` | 12 | docs/V3X/P_F_RESEARCH | `98085df7811a` |
| 5 | docs/V3X/KT_D0_SPEC | `cce8e9a1b00e` | 13 | plugins/skill_a | `b1463bb24403` |
| 6 | docs/V3X/P_F_V0_1_UPGRADE | `b10fae0da66d` | 14 | plugins/skill_b | `e5a299f69a22` |
| 7 | results/deposon_v19_benchmark | `910c4333eead` | 15 | plugins/skill_c | `e19e76c5da7e` |
| 8 | results/deposon_v21_gtformal | `9d9ae5001c57` | 16 | plugins/skill_d | `3e369a1f6171` |

**16/16 MATCH**（含 KT-D0 主锚 `03c6c01f3697` 一手源小写形态）。与我事实核验报告③「17/17 全 MATCH」交叉一致。

## FTFB 专属待填栏（非本线对象，不适用——如实标注清单）

- 委托信/基准指纹栏（`d060f75dbe9f`、`9de366a6c4d6`）：FTFB arXiv 线对象。
- `fiction_that_feeds_back.tex` 指纹、词数基线 12,286、摘要基线 1,849、页数基线 24、5 锚不变式、池数 56/57、P0×4/P1×4/P2×7 修订项验收、grep 清零清单（double-blind/camera-ready/IDENTIFIER-PENDING）：**均为 FTFB 深度修订线验收协议，非本线对象，不适用**。

## 对齐核验（与《鲍勃_GLM完稿V2回函模板事实核验_2026-09-18.md》交叉）

- 模板自体指纹 972401e056f6（R5 轮复测不变；挂载仓只读零改动）。
- R5 轮 5 制品＋16 锚逐件复算值与前轮/核验报告**完全一致**（5/5＋16/16＝17/17）。
- 沿核验报告已登记的模板自体三处登记失真（§0.1/§8.4 字节数 stale：应 26,990/20,117/28,579；§2.3 引源失真；KIMI 路径大小写）**均不属本线待填栏，不影响本清单出值**；模板零改动纪律下原样保留，供转呈方知悉。
- R5 轮 B 路门审（GATE-R5-B-20260918）已同步完成：指纹链五级全长实测/复现（md 42e4310f→工作副本 1dd27184 逐位重建→tex 95fc9ba9→PDF 3b792178）、A1′–A6′ 独立重跑全过、双盲四层零命中、增量≡全量双保险 cmp 记录核对属实。

**产出人**：鲍勃-实验分析师｜0 LLM、挂载仓与 shared 只读（清单本件为派单授权刷新）｜2026-09-18（R5 刷新版）
