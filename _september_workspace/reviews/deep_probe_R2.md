# Deep Probe R2 — 工程复现与流程线独立追问（Deposon v2.0）

> 2026-08-28。追问者：R2（工程复现与流程线）。范围：E1 冷启动复现 / E2 verifier 可靠性 /
> E3 缓存与状态泄漏 / E4 测试覆盖盲区 / E5 API 预算审计 + 新增发现。
> 方法：只读仓库 + 干净目录实跑（git clone → /tmp/cold）+ 远端清单比对（GitHub API）。
> 未修改任何仓库已有文件；未使用任何 API key。

---

## E1 冷启动复现：仅靠 GitHub + MANIFEST + README 能否复现 v2.0 核心结果？

### 问题
干净目录中，仅凭 zeroandcat/deposon 已推送内容，能否复现 v2.0 核心结果
（`results/deposon_v20_corpus_eval.json`，MANIFEST 再生命令 `python3 run_v20_corpus_eval.py --families=S,L`）？

### 证据

**(a) 远端 vs 本地清单比对**（GitHub API 逐目录拉取 vs 本地 ls）：

仅本地有、远端无（按类别）：
- **脚本（关键断点）**：`run_v17_fixed_sampler.py`、`run_v17_fusion_fix.py`、`run_v17_multigraph.py`
- 数据：`strategyqa_train.json`、`corpus/v20/` 全部 22 张图 JSON（远端只有 `index.json` + `README.md`；
  注意远端 README.md 本地反而没有）
- 结果 JSON（15 个，均在 `results/MANIFEST_large_files.md` 留痕，含 sha256 + 再生命令）：
  v15_diffusion×2、v17×3、v19_benchmark_fixes、v1_3/v1_4 details×3、v20_corpus_eval、
  quizbank×2、bigquiz_eval、v20_regression_field、audits_outliers
- **无留痕**：`results/deposon_v18_api_supplements.json`（不在 MANIFEST！）、`results/cot_quiz_cache/`（8 个缓存）、
  `deposon_cache/`（README 声称复现 v1.3/1.4 details 所需，.gitignore 排除）、`_paper_backup_v181/`、
  paper 下 fig1/converted/备份/pdfbuild/r01-r06

**(b) 实跑复现断点**（`git clone --depth 1 https://github.com/zeroandcat/deposon /tmp/cold`，逐断点实跑）：

| # | 断点 | 实跑输出 |
|---|---|---|
| 1 | **`run_v17_fusion_fix.py` 未推送，但被 6 个在库脚本 import** | `python3 run_v20_corpus_eval.py --families=S,L` → `ModuleNotFoundError: No module named 'run_v17_fusion_fix'`。受影响：run_v20_corpus_eval、run_v20_crossval_eval、run_v18_api_supplements、run_v19_fullrank、run_v19_meanfield、run_v19_quickwins。**v2.0 核心结果在远端状态下不可再生** |
| 2 | MANIFEST 三条再生命令指向不存在的脚本 | `deposon_v17_fixed_sampler.json`/`deposon_v17_fusion_fix.json`/`tieartifact_negativeresult.json` 的再生栏均写 `python3 run_v17_fusion_fix.py` —— 死命令 |
| 3 | 连锁依赖：v18 结果再生需 `results/deposon_v17_fusion_fix.json`（本地独有）→ 又需断点 1 的脚本；`deposon_v18_api_supplements.json` 本身未推送且不在 MANIFEST | verifier/v9/check.py 硬性 require 该文件 → 冷克隆上 v9 验收必 FAIL |
| 4 | `strategyqa_train.json` 未推送 | `run_benchmark_v1_4_strategyqa.py` 读本地 DATA_FILE → v1.4 strategyqa details 不可再生（数据为公开数据集但未给获取路径） |
| 5 | `audits_outliers.json` 再生命令指向 `/app/.agents/skills/outlier-scan/scripts/anomaly_detector.py` | 外部技能脚本不在仓库 → verifier/v11 在冷克隆上必 FAIL |
| 6 | 语料图 JSON 未推送（但可完整再生，非断点） | 实跑：`build_corpus()`（0.1s，16 张 S 图）+ `python3 run_v20_familyL_ingest.py`（离线读远端已有 familyL_cache）→ 22 张图全部 sha256 与远端 index.json 逐位一致（22/22 match） |
| 7 | 语料版本未钉住（时间漂移） | 补断点 1 后实跑 corpus_eval 成功（exit 0），但产出 sha256=`bda10c47…` ≠ MANIFEST 留痕 `c4b04014…`：当前 index 已扩为 22 图（6 域），冻结结果是 20 图（4 域）口径；H-A1 p 从 0.0075 漂到 0.0118（仍过 Holm）。**MANIFEST 的"确定性再生"只对语料快照成立，无人能从远端知道冻结结果对应 4 域语料状态** |

**(c) 最小补齐集**（按优先级）：
1. 推送 `run_v17_fusion_fix.py`（+ 两个 v17 兄弟脚本）——一处补齐解锁 6 脚本 + 3 条 MANIFEST 死命令；
2. 把 `deposon_v18_api_supplements.json` 补入 MANIFEST（或直接入库，13KB 级结果不大）；
3. `strategyqa_train.json` 入库或写明获取命令；
4. MANIFEST 每条语料相关再生命令加注「语料快照 = index.json sha256」，并说明冻结结果对应 4 域语料；
5. `audits_outliers.json` 的再生脚本内联入库或改为在库脚本路径；
6. （可选）corpus 图 JSON 直接入库——总共 ~70KB，省去再生步骤且消除断点 7 的歧义。

### 建议答案
**不能**直接复现：核心评估管线在干净克隆上因 `run_v17_fusion_fix.py` 缺失而 import 即崩。
补齐 1 个文件后 v2.0 主实验可离线再生（语料 22 图 sha 全对），但产出数值与冻结留痕不同
（语料已扩域），属于"可复现管线、不可复现快照"。

### 置信度
高（断点 1/7 为干净克隆实跑复现；清单比对为 GitHub API 直读）。

---

## E2 verifier 可靠性：检查词与内容漂移

### 问题
v13–v19 多次出现「检查词与内容漂移」假 FAIL（runs 记录 ≥4 次）。归纳模式、清点存量脆性断言、给结构性修复。

### 证据

**(a) 漂移事件全记录**（verifier/runs/*_run1.md，共 6 次首轮假 FAIL，全部 run2 改检查词/阈值后转绿）：

| 版本 | run1 FAIL | run2 处置 | 漂移类型 |
|---|---|---|---|
| v15 | 6 FAIL：注册表含「common_neighbors」等 | 「注册表检查词对齐文案」 | 硬编码关键词大小写/命名（文档写 "Common Neighbors"，检查写 snake_case） |
| v16 | 文献 ≥15KB — 实 12142B | 阈值 15KB→10KB | 散文体量阈值拍脑袋 |
| v17 | Hardening 文档含「归纳协议」 | 「文档检查词对齐」 | 文档措辞 vs 检查词 |
| v18 | 「gz.b64 残留已清除」 | 「.sha256 留痕件保留口径」 | 检查口径与处置决定不同步 |
| v19 | 综合文档 ≥10KB — 4029B | 「体量阈值按字符口径修正」 | 字节/字符口径混淆 |
| v20 | 「P3 指标最优 vs 工程推荐双口径」 | 「P3 注记补丁后重跑」 | 结果 JSON 注记文案漂移 |

**(b) v10–v20 现存同类脆性断言逐文件清点**（实读全部 11 个 check.py）：

- **v10**：论文双语文档 12+ 条措辞断言（"骨架检测器"or "skeleton detector"、"非劣"or "non-inferior"…）；
  摘要正则定位失败时 `check("EN 摘要可定位", False)` —— 正则 `(?is)abstract(.{200,4000}?)\n#` 对格式微调极脆
- **v11**：CLOSURE 文档 14 个硬编码中文关键词（量变质变/否定之否定/…）循环断言
- **v12**：`check("族 L 4 图在册", len(L_ids) == 4)` —— **族 L 已扩为 6 域，今天重跑 v12 必 FAIL**
  （冻结版 verifier 被语料生长 retroactively 打破）；S6 复现锚点 1e-6 精确匹配
- **v13**：先验 named 精确值断言（0.7826±0.01、1.0±1e-9）；CrossVal 文档 5 关键词
- **v14**：`"0.003052" in txt or "0.0031" in txt`；Skills 文档关键词含 "92.5%"
- **v15**：注册表 9 关键词（大小写敏感）；"CoT 题库准确率 0.925" 精确 float；BOSS 文档关键词 "92.5%"、"1740"
- **v16**：`≥10KB` 体量阈值 ×N；md5 锁论文（合理）但文献锚点 `"文献已确认" in ol` 等措辞断言
- **v17**：Hardening 文档 7 关键词（"1.34×"、"162s"——连运行时秒数都进了检查词）；
  `pytest 200 全绿` 断言 `int(m.group(1)) >= 200`（测试数阈值）
- **v18**：BigQuiz 文档关键词 "157"、"reasoning_tokens"、"空间释放"；`n_items >= 150`；`idx["n_graphs"] == 22`（语料再扩即破）
- **v19**：综合文档 ≥3500 字 + 19 个证据锚/共进桥关键词（"β=2.12"、"19.6%"）、行动清单按词计数
- **v20**：`"2.9 dB" in note`、`"9/9"`、`"14/22"` 字符串精确匹配；Photonics 文档关键词

**漂移模式归纳**：(i) 断言对象选错层——对**散文**（Findings/Registry/论文）做关键词包含断言，
而散文天然会被润色；(ii) 断言值重复登记——数值同时硬编码在 check.py 与结果 JSON 里，两处手工同步；
(iii) 体量/计数阈值无量纲依据（15KB/10KB/3500字/≥200）；(iv) 冻结检查读活状态
（v12 的 ==4、v18 的 ==22 读的是会生长的 corpus/index）。

**(c) 结构性修复建议**：
1. **断言下移到结构层**：文档类检查只验「文件存在 + 必需小节标题」；一切数值判定读结果 JSON 的
   结构化字段（v12 读 `verdicts.*.supported` 是正面范例，应推广到全部版本）。
2. **单一事实源**：每版本一个 `verifier/vN/anchors.json`（冻结的期望值 + 语料 index sha），
   check.py 只读 anchors，不在代码里散落魔法数；数值容差统一用相对/绝对容差而非精确 float。
3. **冻结检查钉输入**：凡依赖会生长资产（corpus、题库）的冻结检查，改断「快照 sha 匹配或 ≥ 快照超集」，
   而非 ==4/==22 这类活计数。
4. **关键词派生而非硬编码**：必须从文档找数字时，从结果 JSON 取值后格式化为文档实际写法集合
   （0.925/"92.5%"/"37/40"）再匹配；中文措辞类关键词一律视为 smell，替换为小节锚点。
5. **体量断言改结构断言**：≥N KB → ≥N 个小节/表格/引用条目；pytest 计数 → 只断言 returncode==0。

### 置信度
高（6 次漂移事件逐条来自 runs 记录原文；脆性清单逐文件实读）。

---

## E3 缓存/状态泄漏：familyL 摄入与 index.json 重建时机

### 问题
「新域没进 index 导致评估漏 2 域」事件链复现与根因；6 域扩展对既有 4 域缓存 fresh 判定的影响；防复发。

### 证据

**(a) 事件链复现（mtime + 代码实读）**：

```
09:29–09:36  familyL_cache 原 4 域获取
09:38:45     run_v20_familyL_ingest.py main() → 4 张 L 图 + build_index（20 图）
09:42:26     corpus_eval（20 图，即冻结结果）
15:07–15:08  familyL_cache 新增 geography_world / project_management
15:11:44     corpus/v20/L_geography_world.json 写入
15:12:37     corpus/v20/L_project_management.json 写入
             —— 但 index.json 未动 ——
15:53:05     index.json 才重建（22 图）   ← 41 分钟陈旧窗口
15:54:09     quizbank_v20_big / bigquiz_eval（6 域，修复后产出）
```

**根因（在库代码直接证据）**：`run_v20_bigquiz_fetch.py` 第 (a2) 段：
```python
from run_v20_familyL_ingest import ingest_domain
for d in NEW_DOMAINS:
    if not os.path.exists(gpath):
        ingest_domain(d)          # ← 写 corpus 图，但从不调 build_index
```
`ingest_domain()`（run_v20_familyL_ingest.py L36–92）只写 `corpus/v20/L_{domain}.json`，
**不重建 index**；`build_index` 仅在 `main()` 末尾、且仅当本次 `ingested` 非空时执行
（`idx = build_index(CORPUS_DIR) if ingested else None`）。而全部 10 个 v20 评估/审计脚本
（corpus_eval/crossval_eval/bigquiz_eval/quizbank/gt/photonics/vector_audit/baselines/fastcheck）
都经 `load_corpus()` **只读 index.json 在册图**——陈旧 index ⇒ 新域静默漏评，无任何报错。
旁证：4 张旧 L 图 mtime 停在 09:38，若走 main() 全量重摄入必被同时重写；实际只有 2 张新图
有新 mtime ⇒ 确为逐域直接调用。次要风险：`main()` 只捕获 CacheMissingError，
FamilyLParseError 会在 build_index 之前炸掉进程，同样留下「图已写、index 未建」的半态。

**(b) 4→6 域扩展对既有缓存 fresh 判定的影响：无影响（实测）**。
fresh 判定 = `cache.prompt_sha256 == familyL_prompt_manifest()[domain].prompt_sha256`；
逐域 sha 由 `_PROMPT_TEMPLATE.format(domain, brief)` 决定，模板与原 4 域 brief 未变 ⇒
原 4 域 prompt_sha256 不变。实算比对：6/6 域 manifest sha 与 familyL_cache 记录全部 MATCH
（physics 20c6772…、biology 085532…、algo e8edf1…、historical f41b05…、geo 6453d3…、PM be7750…）。
即扩展是纯增量，既有 4 域缓存 fresh 判定不受扰动。

**(c) 防复发机制**：
1. **摄入即建索引**：`ingest_domain()` 成功写图后立即 `build_index()`（或在函数内返回
   `index_dirty=True` 并由所有调用方断言处理）；消除「写图」与「建索引」之间可分离的事务窗口。
2. **load_corpus 一致性哨兵**：读 index 时对照目录扫描，发现 orphan 图 JSON
   （在目录不在册）即 raise，列出孤儿名单——把「静默漏评」变「响亮失败」。
3. **测试锁定**：新增「ingest→load_corpus 往返」测试（tmp_path 摄入 1 域后 load_corpus 必须可见）；
   现有 `test_on_disk_corpus_index_consistent` 只验 S 族 16 图，扩为全族目录-vs-index 计数一致。
4. verifier 增补活检查：`index.n_graphs == len(目录图 JSON)`（替代 v18 的 `==22` 魔法数）。
5. `main()` 把 build_index 移入 try/finally，避免解析异常留下半态。

### 置信度
高（根因有在库代码行 + mtime 链双重证据；(b) 为本地实算）。

---

## E4 测试覆盖盲区

### 问题
tests/ 200 项中族 L 管线（ingest/crossval/bigquiz）与 deposon_fast 族 L 路径的直接测试？
deposon_photonics 有无测试？

### 证据

实跑 `python3 -m pytest -q`：**200 passed**（19.2s）。逐文件 import 分析与断言清点：

| 模块 | 直接测试 | 位置 |
|---|---|---|
| familyL **ingest** | 3 项（缺缓存显式报错、合法缓存往返、prompt manifest 稳定性） | test_v20.py |
| familyL **parser/prompts** | 2 项（合法/围栏接受、坏输入拒绝） | test_v20.py |
| **crossval**（fetch/eval） | **0** | 无 import |
| **bigquiz**（fetch/eval） | **0** | 无 import |
| **quizbank 构建**（run_v20_quizbank） | **0** | 无 import |
| **CoT**（cot_fetch 评分映射） | **0** | 无 import |
| deposon_fast **族 L 路径** | **0**（test_fast 3 项全部 `families=("S",)`，仅 S1/S2/S6） | test_fast.py |
| **deposon_photonics / run_v20_photonics** | **0** | 无任何测试 import |
| run_v20_baselines / run_v20_vector_audit / svg_mindmap_ingest | **0** | 无 import |

零覆盖模块清单：run_v20_crossval_eval、run_v20_crossval_fetch、run_v20_bigquiz_eval、
run_v20_bigquiz_fetch、run_v20_quizbank、run_v20_cot_fetch、deposon_photonics、
run_v20_photonics、run_v20_baselines、run_v20_vector_audit、svg_mindmap_ingest、
deposon_fast 的族 L 输入路径。

**最高价值补测清单（≤8 项）**：
1. ingest→index→load_corpus 往返一致性（E3 事件回归测试，防 stale-index 复发）；
2. 目录-vs-index 孤儿检测哨兵测试（配合 E3 修复 2）；
3. crossval 判定规则重算测试（仿 test_v20 的 gt1/gt4 verdict 重算：小夹具 JSON → no_separation 判定、rule 塌陷 pp）；
4. bigquiz 评分重算测试（小夹具 quizbank + 假缓存 → per_domain/overall 准确率逐位重算，含 answer_index 置换正确性）；
5. quizbank 构建确定性与域覆盖测试（BANK_SEED 锁定 + 覆盖 == FAMILY_L_DOMAINS，防 4/6 域漂移）；
6. photonics P1 守恒与 P2 可探测重算（toy 图：t+r+a=1、损耗预算边界图各一）；
7. deposon_fast 族 L 图快慢路径排序级等价（仿 test_rank_preserved_on_all_families，加 L 图参数）；
8. CoT 选项置换映射测试（bloom L4 题干→选项 perm→answer_index 一致性，锁 92.5% 的评分前提）。

### 置信度
高（import 级证据 + pytest 实跑）。

---

## E5 API 预算审计

### 问题
汇总 results/ 下全部 *_cache 与结果 JSON 的 HTTP 尝试计数，核对 SPEC 预登记预算。

### 证据

**方法与口径发现（先行）**：全部 34 个缓存 JSON **无一个含 attempt/HTTP 计数字段**
（逐文件扫描确认）；结果 JSON 中唯一计数字段 `total_http_attempts_actual` 出现在
deposon_v18_api_supplements.json，值为 **0**——幂等重跑把真实计数自我覆盖
（权威数字只剩 SPEC_v1.8 A4 散文）。即：**实际尝试数的唯一账本在 Findings/SPEC 散文里，
机器可读层不存在**。以下为散文账本 vs 预登记条款逐实验核对：

**(a) 逐实验实际 vs 预登记**：

| 实验 | 预登记条款 | 上限 | 实际（散文账本） | 判定 |
|---|---|---|---|---|
| v1.6 llm_prior | SPEC v1.6 §4（经 llm_prior.py 注释）：1 prompt × MAX_ATTEMPTS=2 | 2 | 未持久化（缓存存在 ⇒ ≥1） | 无法核验 |
| v18 E1–E4 | SPEC_v1.8 §预算 + A4：4 prompt × 2 | 8 | E1=1、E2=1、E3=2、E4≤2（**E4 尝试数未单独持久化**），总 ≤6 | 内，但 E4 不可核验 |
| 族 L 获取（4 域） | SPEC_v2.0 §5：族 L ≤ 8 prompt × 2 | 16（脚本头自写 4 prompt × 2 = 8） | 6 + **3 次误删重取**（Findings 诚实附注）= 9 | SPEC 内；超脚本自报口径 8；**Findings 头条只写「消耗 6 次」，少报 3** |
| crossval（先验 4 + GT-2 攻击者 4） | Findings 自称「预算 ≤16，SPEC v2.0 §5」 | 16 | 10（含 algorithm_process 2 次超时重试 + 断点续传） | 内；但 SPEC §5 原文只登记族 L 与 GT-2，**先验臂预算无 SPEC 出处**（仅 Findings 待办自派 ≤4 prompt），引用错配 |
| CoT 小题库（boss） | **SPEC_v2.0 无条款、无修正案** | — | 8 prompt / 9 HTTP | **未登记消耗** |
| bigquiz（2 新域全管线 + 6 域扩池 + PM 重试） | 脚本头：16 prompt × MAX_ATTEMPTS=2；**SPEC 无条款、无修正案** | 32（脚本口径） | 「~20 次」：分项 6+6+2=**14 与 ~20 对不上**；§二另记 PM 先验 5×120s 超时 + 1 成功 = 6 次 | 模糊记账；**未登记消耗** |
| CoT 新域补齐 | Findings 自列「下轮预算 2 prompt」 | — | 未发生（cot_quiz_cache 仅 4 域 × 2 批） | — |

**(b) PM 先验 16k token 重试的预算口径问题**：
1. **单 prompt 尝试上限被突破**：全局纪律 MAX_ATTEMPTS=2（llm_prior.py L26，SPEC v1.6 §4），
   PM 先验实际 6 次（5 超时 + 1 成功）；若超时发生在脚本外交互会话，则该消耗游离于
   「prompt × MAX_ATTEMPTS」框架之外——预登记口径根本没有容纳交互式重试的格子。
2. **token 维度从未入预算**：预登记只数 prompt 与 HTTP 次数；max_tokens 8000→16000 的参数变更
   （Findings_v2.0_bigquiz §二）改变了单次成本量级，不触发任何预算口径——reasoning 模型下
   「次数预算」与「成本预算」脱钩，本次事故（8000 token 中 7999 被 reasoning 烧光）正是例证。
3. **分项加总不自洽**：头条「~20 次」与分项 14 的差额恰好约等于 PM 的 6 次，
   说明超时重试被「~」模糊吸收，账本精度不足以支持审计。

**(c) 总账（v1.6–v2.0，散文账本加总）**：
- 预登记内消耗：v18 ≤6 + 族 L 9 + crossval 10 = **≤25 次**（其中 3 次为误删重取的浪费性消耗，在案）；
- 未登记消耗：CoT 小题库 9 + bigquiz ~20 = **~29 次**（SPEC_v2.0 自首「修正只能以修正案追加」，
  但全 SPEC 无一条 v2.0 修正案）；
- 不可核验：v1.6 先验、v18 E4、v1.3/v1.4 基准期 deposon_cache（不在库、无账本）；
- **合计已声明 ≈54 次 HTTP，其中约 29 次（53%）无 SPEC 级预登记出处**。
- 结构性建议：① 缓存 schema 增加 `attempts`/`http_log` 字段（每次写缓存落 attempt 数与
  finish_reason），让账本机器可读、幂等重跑不覆盖（v18 的 0 即是反例）；
  ② 预算口径加 token 维度（max_tokens 变更 = 修正案触发条件）；
  ③ 交互式 API 调用一律经统一 post() 入口计数，堵「脚本外重试」漏洞；
  ④ 后续消耗先补 SPEC 修正案再执行（v1.8.1 修正案是已有正面先例）。

### 置信度
中高。缓存/JSON 无计数字段为穷举实证；实际次数依赖散文账本自报，PM 超时次数的归属
（脚本内/外）无法从仓库确证，标为中。

---

## 新增发现（五问之外）

### N1 【高严重度】H_A_dead 斩杀线「叙事与 artifact 直接矛盾」
在库 `results/deposon_v20_corpus_eval.json`（冻结交付物）：
`kill_lines.H_A_dead.triggered = true`，`n_reversals_vs_random = 3`
（L_historical_causality、L_physics_concepts、S2_n45），规则原文「≥3 张图效应反转 → H-A 判死」。
而 `docs/Findings_v2.0.md` L45 写「H_A_dead：未触发（H-A1 显著；反转图 < 3）」——
**符号检验 15+/3−/2 平中的 3 个负号就是 3 张反转图，「<3」为事实性错误陈述**；
按预登记机械规则 H-A 已判死，叙事却报「未触发」。且 verifier 全版本无任何一条检查
kill_lines 字段（v12 验 verdicts 不验 kill_lines）→ 矛盾穿堂而过。冷启动按当前 22 图语料
重算后反转图增至 4 张（+L_project_management），矛盾进一步扩大。
建议：立即以修正案口径更正 Findings 与论文相关表述；verifier 增补
「Findings 斩杀线表述 == 结果 JSON kill_lines」对账检查。

### N2 MANIFEST「确定性再生」对语料生长不成立（复现快照缺失）
E1 实跑：同一再生命令今天产出与留痕 sha 不同的结果（20→22 图，H-A1 p 0.0075→0.0118，
结论方向未变）。MANIFEST 留的是「文件 sha + 命令」，但命令的输出依赖**活语料状态**，
未钉 index.json 快照 sha ⇒ 留痕承诺（"任何人可本地复算校验"）对语料相关条目不可兑现。
建议：MANIFEST 语料相关条目增列「输入快照 = corpus/v20/index.json sha256: …」，
或 corpus 图直接入库（~70KB）。

### N3 v18 结果 JSON 的 HTTP 账本自我擦除
`deposon_v18_api_supplements.json.total_http_attempts_actual = 0`：幂等重跑（缓存全新鲜）
把 E1–E4 真实消耗（SPEC A4：≤6 次）覆盖为 0。机器可读账本与散文账本互相矛盾，
且无任何检查发现。这是 E5「账本只在散文」的最尖锐单例。

### N4 远端 corpus/v20/README.md 本地缺失
远端有 `corpus/v20/README.md`（875B）而本地工作区没有 ⇒ 本地→远端的同步是选择性推送
而非整目录镜像，同类「远端有、本地无」的静默分叉可能再发生（本次仅此 1 例，已全目录核对）。

### N5 交互式直调 ingest_domain 的半态写入模式可泛化
E3 根因不仅是本次事故：`run_v20_familyL_ingest.py` 把「写 corpus 图」做成公共函数、
把「建 index」做成 main() 尾部动作，任何 import 级调用方（bigquiz_fetch 已示范）都会留下
「图在目录、不在册」半态。属 API 设计级陷阱，建议按 E3(c)-1 从函数契约上消除。

---

## 附：本报告关键实跑命令

```bash
# E1 冷启动
git clone --depth 1 https://github.com/zeroandcat/deposon /tmp/cold
cd /tmp/cold && python3 -c "from mindmap_corpus_v20 import build_corpus; build_corpus()"   # 16 图 0.1s
python3 run_v20_familyL_ingest.py        # 22/22 图 sha 与远端 index 一致
python3 run_v20_corpus_eval.py --families=S,L
#   → ModuleNotFoundError: No module named 'run_v17_fusion_fix'（断点 1）
cp <本地>/run_v17_fusion_fix.py . && python3 run_v20_corpus_eval.py --families=S,L
#   → exit 0，但 sha bda10c47…≠MANIFEST c4b04014…；H_A_dead.triggered=true（4 反转）
# E4
cd /mnt/agents/output/deposon-repo && python3 -m pytest -q   # 200 passed in 19.17s
```
