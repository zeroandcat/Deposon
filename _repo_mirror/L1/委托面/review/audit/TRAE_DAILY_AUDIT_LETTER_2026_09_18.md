# Trae code 走读回函 · 2026-09-18 全日新增实验审查与改进（正式）

> **委托**: user「对今日新添加的实验内容进行全面审查与走读……系统性改进……撰写正式回函」
> **走读方**: Trae code（审校/走读），1 主线自走读 + 2 并行子代理
> **纪律**: 0 LLM 复算 / frozen 全 0 触动 / 追加式改进不改生产方原值 / 诚实降级不 reassign

---

## §0 摘要（一段话）

今日新增 40 个文件（四批：coze paper 双审凌晨批 / GLM v3 双审批 / **D05 主跑实验批** / FTFB v3 审计+信件批）。走读结论：**实验设计与纪律执行总体优秀**（I1-I5 不变量全 PASS、退化预检落实、0 占位污染、失败 backbone 诚实披露不擅自换 ID），但抓到 **6 项 P0 级证据链/管护问题**（最严重者：D05 唯一成功 backbone 的原始数据被 bg 任务 trash 化）与 7 项 P1 纪律缺口。本轮已直接实施 **3 项改进**（数据抢救 + verify 修复 + SELF-CHECK 补齐，全部验证 PASS），其余 10 项列入生产方实施建议。

---

## §1 走读情况（范围与方法）

| 批次 | 文件数 | 走读方式 | 结论概要 |
|---|---|---|---|
| D05 主跑实验链 | 13 | 主线自走读（runner 源码 + 6 JSON 逐字段 + 时间线还原） | I1-I5 严守；发现 trash 化数据风险 + 脚本缺陷 |
| v2scripts 复验链 | 5 | 子代理 1（源码 + 产物对账 + 13 项 SHA 抽验） | PASS 46/0/0 属实，但纪律缺口 5 项 |
| FTFB v3 修正审计链 | 3 | 子代理 1（与 v2 缺陷闭环对账 + 独立复算 5 锚） | 修复属实，但审计未点名头号缺陷闭环 |
| 双审 + 信件批 | 19 | 子代理 2（结构/口径/SHA 实算 ~25 次） | 评审发现真实，但证据链断裂 4 处 |

**D05 时间线还原**（走读核心成果）：main runner 10:08 落 6 JSON 至 results 根 → MD 生成段因 `ds_total_acc/nm_total_acc` 变量 bug 崩溃 → 10:16 以 `md_report_only` 只读补生成综合报告（正确的修复路径）→ **bg_21191cee 任务随后被删，其工作区（runner、sanity 脚本、deepseek 主跑结果、qwen3 FAIL 证据）被移入 `_d05_bg_21191cee_trash_2026_09_18/`**——唯一 PASS backbone 的原始数据从此躺在 trash 目录。

## §2 走读发现汇总（分级）

### 🔴 P0（证据链/数据管护，6 项）

| # | 发现 | 位置 | 状态 |
|---|---|---|---|
| 1 | **D05 主跑原始数据 trash 化**：deepseek_v4 30 cells 完整结果（24/30, acc 0.8, Spearman 0.7917，D05 唯一 sanity PASS backbone）+ qwen3 FAIL 证据在 trash 目录，β JSON `_meta` 引用其 SHA——trash 清空即 D05 溯源链断裂 | `_d05_bg_21191cee_trash_2026_09_18/results/` | ✅ **本轮已抢救** |
| 2 | GLM v3 综合报告自引复算证据 `.tmp/verify_glm_claims*.py`（14 轮脚本）不存在——报告一边批评论文"脚本不可得"，一边自己的复算脚本失联 | `_glm_v3_双审报告` §7 | 待生产方 |
| 3 | KIMI→GLM 深度修订委托信的**开工门禁基准指纹指向不存在的文件**（`ftfb_pkg/.../fiction_that_feeds_back.tex` 基准 sha256 `9de366a6…` 无对象可比）——将直接阻塞 GLM 修订开工 | `_letter_to_glm_ftfb_deep_revision` | 待生产方（**D+1 前必须闭合**） |
| 4 | GLM v3 双审 A2 子审第 153 行句中截断（无 verdict、无总结），综合报告按正常产出登记未披露——"2 份内容审"实际 1.5 份 | `_glm_v3_review_2026_09_18/review_content_A2_kimik3.md` | 待生产方重派 |
| 5 | coze paper 双审报告为四子审**纯拼接**（无综合结论/无审稿日期/无署名），且 2 份子审截断或思维链原稿却标"状态：OK" | `_coze_paper_v1_review_2026_09_17/` | 待生产方 |
| 6 | skill inventory（423 条）路径**零可解析**（未声明 base path，抽查 5 条全不存在）+ 中文描述大面积编码乱码 | `_mavis_skill_inventory_2026_09_18.md` | 待生产方 |

### 🟡 P1（纪律/口径，7 项）

| # | 发现 | 状态 |
|---|---|---|
| 7 | v2scripts worker 缺 SELF-CHECK 尾块（违反 2026-09-16 已确立的 P-F V0.1 §5 纪律） | ✅ **本轮已补** |
| 8 | v2scripts worker dead import：import 了 4 个 verdict 纯函数从未调用，判定逻辑内联重写；"复算"实为"阈值自洽复验"（若 frozen 脚本函数逻辑有差异捕获不到） | 待生产方 |
| 9 | `_d05_verify_sha` 路径拼接 bug（raw-string 双反斜杠 + 校验列表引用已移位文件，重跑必 FileNotFoundError） | ✅ **本轮已修** |
| 10 | FTFB pass1/pass2 审计全文 **0 处提及 abstract/L408**——v2→v3 的动机性缺陷修复仅由 compile_verification T-1 门覆盖，两 pass 审计未给出闭环证据链（外部读者无法确认已修） | 待生产方补"缺陷闭环表" |
| 11 | FTFB pass2 M1"守恒闭合"证据 `results/anon_benchmark_v1_4_gsm8k.json` 本地不存在（kimi s7 已如实建议拉回，pass2 未披露） | 待生产方 |
| 12 | β JSON `_meta` 键名（`deepseek_v4_main_sha12`）与 main runner 源码写法（`main_deepseek_sha12`）不一致——本轮 verify 脚本首跑即被此口径差绊倒（已适配，实证） | 记录 |
| 13 | coze 双审报告 SHA 锚为 **CRLF→LF 归一化哈希**（直接 sha256sum 复算必 MISS），未声明归一化规则；同批 manifest 却是原始字节哈希——同日两套口径并存 | 待生产方统一 |

### ⚪ P2（次要，8 项）

D05 8 维状态表重复计数（维度 3=7、5=8，实际 6 个独立维度）；`FROZEN_18` 实为 16 项（"18 锚 16/16"自相矛盾句式）；8 维含水分（恒真断言 `assert "OPENAI" not in os.environ.get("_TEST_PROXY","")` 读不存在的环境变量、纯存在性检查计为 1 维）；docstring 口径漂移（60/30 cells、≤0.5/==0）；main runner MD 生成段死代码（ds_total_acc bug 遗留，实际由 md_report_only 替代）；coze 目录名 09_17 实写 09_18 00:35；FTFB pass2 自报字节数三值互不一致 + 最终 SHA 以"自指悖论"为由不落（相对 worker "写盘后实测打印"是纪律退化）；GLM v3 综合报告内部矛盾（§2 三阻塞 vs §6.1"唯一阻塞"、悬空 §4.1 引用、E1 计数失准）。

### ✅ 正向核验通过项

I1-I5 五不变量实算全 PASS（30 题 SHA 唯一集 30/30）；退化预检四条真实落实于 Adendum A 链；10 件评审/信件类占位符扫描 0 命中；verifier21 manifest 哈希口径最干净（4/4 原始字节直算命中）；v2scripts 13 项 SHA 抽验 0 偏差；FTFB 链 5 锚独立复算 5/5 一致 + 论文 4 件 SHA 4/4 一致；失败 backbone（qwen3 HTTP 400 / nemotron sanity 空响应）沿"不擅自换 ID/不重试"纪律诚实披露；key runtime 读取 + `ProxyHandler({})` 直连（HIGH-1 教训已内化）。

## §3 已实施改进（3 项，全部验证 PASS）

| # | 改进 | 内容 | 验证 |
|---|---|---|---|
| 1 | **D05 数据抢救** | deepseek 主跑 + qwen3 FAIL 证据**复制**（非移动）回 results 根，trash 原件不动；随附救援注记 MD（事实链 + 处置 + 哈希） | 副本哈希逐字节==trash 原件==β `_meta` 声称值（`0a933d7c8d7a` / `427b18da8114`）；**D05 溯源链恢复闭合** |
| 2 | **verify 脚本重写** | 修路径 bug + 7 件校验 + β `_meta` 三声称值交叉核对 + trash 双胞胎对照 + SELF-CHECK | 重跑 `VERIFY ALL-PASS` + SELF-CHECK PASS（7/7 OK + 3/3 MATCH） |
| 3 | **v2scripts worker 补 SELF-CHECK 尾块** | 沿 TRAE_SELFCHECK_2026_09_16_V3 标准格式（文件名防漂移 + main/guard 断言） | compile PASS，新 SHA `c3ad0036b46f` |

## §4 预期效果

1. **D05 实验的溯源链由"悬空"变"闭合"**：β bootstrap 的全部三个输入 backbone 的 main results 现均可在 results 根直接核验，combined report §1.1 的 source 列恢复可解析；
2. **trash 清空不再构成单点灭失**（双副本 + 注记）；
3. verify 工具由"跑必崩"变为"ALL-PASS 校验器"，且具备 β `_meta` 交叉核对能力——下次 bg 任务再 trash 化会立即暴露而非静默断链；
4. v2scripts worker 纳入 30-runner 同等 SELF-CHECK 纪律网。

## §5 实施建议（生产方必办，按优先级）

| 优先级 | 事项 | 责任方 |
|---|---|---|
| **D+1 前** | 闭合 KIMI→GLM 委托信开工门禁（#3）：要么把基准 tex 落盘到声称路径，要么改基准指纹为盘上实存 tex（`d060f75d…`） | KIMI/Mavis |
| **D+1 前** | GLM v3 综合报告：补落 `.tmp/verify_glm_claims*.py` 或改引实际存在路径；重派 A2 截断子审并披露 | Mavis |
| **本周** | coze 双审重整：补综合结论 + 审稿日期/署名 + 子审完整性闸门（截断/思维链原稿不得标 OK）；统一哈希口径并成文（原始字节 vs LF 归一化二选一声明） | Mavis |
| **本周** | FTFB pass1/pass2 补"v2→v3 缺陷闭环表"（abstract L408→L69/L74 + T-1 G1a/G1b/G1c/G2 证据）；pass2 披露 M1 证据缺失并执行 kimi s7 的"拉回 anon_benchmark"建议 | KIMI |
| **复跑前** | v2scripts worker：真正调用 4 个 import 的 verdict 函数（消除 dead import + 内联漂移风险），或把产物措辞从"复算"降格为"阈值自洽复验"；统一 FROZEN_18→16 anchor 口径 | Mavis worker |
| **复跑前** | D05 若复跑：main runner MD 段死代码清理 + 8 维去重 + β `_meta` 键名与源码统一 | Mavis worker |
| **camera-ready** | skill inventory 修复（base path 声明 + 编码修复 + 生成方法说明） | Mavis |

## §6 改进前后 SHA-12 对照表

| 对象 | 改进前 | 改进后 | 备注 |
|---|---|---|---|
| `results/_d05_main_run_results_20260918_100853.json` | （trash 内原件，未动）`0a933d7c8d7a` | 抢救副本 `0a933d7c8d7a` | 逐字节一致 |
| `results/_d05_main_run_results_qwen3_failed_20260918_100853.json` | （trash 内原件，未动）`427b18da8114` | 抢救副本 `427b18da8114` | 逐字节一致 |
| `_d05_verify_sha_2026_09_18.py` | ⚠️ 未及实算（原版 445 B / 5 行，内容已在走读记录中全文保全；覆盖前未落 SHA——诚实交代，不以重建值伪造） | `0b7e50a8a036`（2,938 B） | 重写修复 |
| `deposon_team/plugins/_deposon_v2scripts_reverify_worker_2026_09_18.py` | ⚠️ 未及实算（原版 32,929 B；子代理走读仅记 size 未记 SHA） | `c3ad0036b46f`（33,624 B） | 尾块追加 |
| `deposon_team/plugins/_fix_d05_rescue_2026_09_18.py` | —（新增） | `2c2cc3ff542a`（3,524 B） | 救援脚本 |
| `results/_D05_DATA_RESCUE_NOTE_2026_09_18.md` | —（新增） | `120295a19655`（1,181 B） | 救援注记 |
| 本回函 | —（新增） | `e372cc3084b5`（11,422 B）* | — |

**教训自账**：本轮两处"改进前 SHA 未落账"是我违反自家 v2 优化文档"改进前基线先落账"条款的执行失误（fix 脚本先跑、SHA 后想）——如实入表，不为追溯一致而编造重建哈希；后续改进一律先 `sha12` 落账再动笔。

*本回函含自引用 SHA（写入终算值后文件已变），绝对精确值以落盘后单独复算为准。

## §7 挂点回扣（沿 D7 report §3 模式）

> **KT-A1**（守恒审计）：v2scripts T+R+A 9/9 与 5 锚复算一致，守恒链完好 ✅
> **KT-B1**（75 攻击）：P-M 矛盾件（Adendum C）本轮无新增污染，erratum 在位 ✅
> **KT-C1**（命名）：D05/FTFB 链命名无新增漂移 ✅
> **KT-D0**（D7 流程）：D7 推送不受本轮发现阻断（D05 属 D+0.5 增补批），但 #3 委托信门禁若不闭合将阻塞 D+1 的 GLM 修订线 ⚠

—— Trae code（审校/走读），2026-09-18
