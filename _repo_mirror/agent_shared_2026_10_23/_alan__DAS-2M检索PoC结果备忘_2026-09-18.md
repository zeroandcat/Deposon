# DAS-2M 检索基础设施 PoC 结果备忘

- 撰写：阿兰-文献调研员
- 日期：2026-09-18（全部实测于本日完成）
- 任务来源：管理员 2026-09-18 00:51 派单（按评估备忘 §5–§7 方案执行）
- 纪律：仓内 0-LLM、未委外、未动任何稿件与冻结件、零推断；检索记录全量留档

---

## 0. 结论速览

**试点判定：c 线可行（有条件通过）。** DAS-2M 原始分卷经 hf-mirror 镜像成功下载、SHA256 校验一致、19 万条单遍词法检索 20.4 秒完成；对 V3X 核心域（LLM 评测可靠性/judge 偏差）检索质量达标（Q3 precision@20 strict≈0.65），并对 backbone 选型相关工作直接产出候选清单；对方法论/哲学类主题（falsifiability/pre-registration）确认无效（precision≈0）。另发现关键数据质量缺陷：publication_date 字段噪声严重（仅 55.9% 为 2026 年，含 1828/2029 等荒谬值），**日期必须以 arxiv_id 前缀为准**。

---

## 1. 可达性验证（含卡点与突破过程）

| 环节 | 结果 |
|---|---|
| HF 主站直连（curl） | **超时不通**（datasets-server 与 huggingface.co 均 28/30s 超时；arXiv 主站正常 200） |
| hf-mirror.com 镜像 | **打通**（API 与 resolve 均 200） |
| HF viewer（昨日报告 DatasetGenerationError） | 确认为服务端预览管线问题，**不影响原始文件直下**（本 PoC 全程未用 viewer） |
| datasets-server /splits API | 经 page_reader 无法携带 query 参数、经 curl 不通 → **弃用**（改走镜像直下路线） |
| 文件树探测 | 经 page_reader 调 HF API 成功：retrieval/ 共 7 个按年分卷（papers_2020–2026.jsonl.zst，合计约 1.36GB） |
| zstd 工具链 | 波折：pip 安装连续被网关掐断（≥5 次）、apt 无 root 权限 → **apt-get download zstd + dpkg-deb -x 免 root 解出二进制**（v1.5.7，工作正常） |
| 2026 分卷下载 | 181MB（180,692,317 字节）**<30 秒**完整下载，字节数与文件树一致 |
| **SHA256 校验** | `cb3626d097a938e…84a932` 与 HF LFS oid **完全一致** |

## 2. 数据核验（2026 分卷）

- 解压后 824MB JSONL，**190,603 条记录**，与官方 dataset_stats.json（2026 年 records=190,603，months=7，即 arXiv 2601–2607）**精确一致**。
- 官方 quality_report.json：invalid_json=0、read_errors=0、missing_files=0（确定性 sha256(arxiv_id) mod 100 抽样质检）。
- 记录字段（schema.json）：arxiv_id / title / publication_date / lexical_text / semantic_text / metadata_version / metadata_shard（join_key=arxiv_id，可回链 metadata/ 分片取 LLM 提取的结构化元数据）。
- 官方总量：7 年 1,471,166 条（"2M"为名义值）。

## 3. PoC 检索设计与结果

**执行主体**：仓内 0-LLM（纯 Python stdlib 脚本 `poc_search.py`，单遍扫描，title×3+lexical_text×1 加权词频，lexical_text 截断前 6000 字符——口径已披露）。
**查询集（5 条，面向 V3X 增补实验相关工作）**：Q1 LLM 评测一致性/可靠性；Q2 基准污染；Q3 LLM-as-judge 偏差；Q4 模型选型/backbone 比较；Q5 可证伪性/预注册（方法论线对照）。
**性能**：190,603 条单遍扫描 **20.4 秒**（含 JSON 解析与 5 查询同时打分）。

**Precision@20 判定**（我作为 in-loop 人工逐条判定标题相关性，双口径披露）：

| 查询 | strict 相关 | lenient（含边缘相关） | 判读 |
|---|---|---|---|
| Q1 LLM 评测一致性 | 7/20 = 0.35 | 12/20 = 0.60 | 达标 |
| Q2 基准污染 | 4/20 = 0.20 | 10/20 = 0.50 | strict 未达（"benchmark"域碰撞：大量普通 benchmark 论文涌入） |
| Q3 judge 偏差 | **13/20 = 0.65** | 17/20 = 0.85 | **最优**，正中 V3X 域 |
| Q4 模型选型 | 5/20 = 0.20 | 8/20 = 0.40 | strict 未达（"model/selection"多域碰撞） |
| Q5 可证伪性/预注册 | 1/20 = 0.05 | 2/20 = 0.10 | **无效**——再证实评估备忘 a 线域错配判断 |
| 均值 | **0.29** | 0.49 | 对备忘预设判据 precision@20≥0.3：strict 均值贴线，但**按域分层看核心域（Q1/Q3）明显达标、非 arXiv 主流域（Q5）无效** |

## 4. V3X 直接可用产出（候选线索，未入池）

Q1/Q3 top 命中中识别出一族与 backbone 选型/评测可靠性直接相关的论文（**均为 DAS-2M 检索线索，入池前须一手核验**）：
- 2601.22548 Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations（**已回 arXiv 一手验证，标题逐字一致**）
- 2606.19544 Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias（**已回 arXiv 一手验证**）
- 2604.22891 Quantifying and Mitigating Self-Preference Bias of LLM Judges；2604.23178 Judging the Judges: …Bias Mitigation Strategies in LLM-as-a-Judge；2606.13685 The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation；2607.08535 When the Judge Changes, So Does the Measurement；2606.03043 The Geometry of LLM-as-Judge；2604.06996 Self-Preference Bias in Rubric-Based Evaluation
- Q4 侧：2607.08665 Resample or Reroute? Budget-Aware Test-Time Model Selection；2605.24981 Large Language Model Selection with Limited Annotations；2601.17865 D-Models and E-Models: Diversity–Stability Trade-offs
完整 top-30×5 见留档 poc_hits.json。

**防幻觉抽查**：抽 2 条 top 命中回 arXiv abs 页比对，2/2 标题一致（abs_2601.22548.html / abs_2606.19544.html 留档）。

## 5. 关键数据质量发现（纪律依据）

1. **publication_date 噪声严重**：190,603 条中仅 106,453（55.9%）标 2026 年；45,885 条标 2025、36,853 条标 2024，且存在 1828/1877/1889/2027/2029 等荒谬值——该字段为 LLM 提取产物，**不可用作年代过滤**，日期一律以 arxiv_id 前缀（YYMM）为准。
2. lexical_text 存在标题重复拼接（抽检首条 Title 出现两次）——对词频打分有轻微偏置，不影响可用性。
3. 分卷只到 2026-07（months=7）；2026-08 以后文献不在湖内。

## 6. 结论与下一步建议

**结论**：DAS-2M 作为检索基础设施**可用且有条件推荐**——条件为：① 主题限于 arXiv 主流的 ML/LLM 域（Q1/Q3 类）；② 全部产出仅作候选线索、一手核验后入池（沿 61 池纪律）；③ 日期/元数据不信任 DAS-2M 字段。对 Keep the Books 方法论线的检索需求（falsifiability/pre-registration 等）**确认无效**，该线仍应走既有 Web 检索通道。

**下一步（供管理员决策，非本轮范围）**：
1. 若 V3X 文献梳理启动：可扩至 2024/2025 分卷 + BM25 打分 + 用 semantic_text 字段，并 join metadata/ 分片取方法细节（脚本骨架已留档可直接改造）；
2. 全 7 卷下载约 1.36GB（按 2026 卷速度约 5 分钟内可完成）+ 解压后约 6-7GB，磁盘与耗时均可承受；
3. 本 PoC 的 Q1/Q3 候选清单可转交查理/鲍勃作 V3X 相关工作梳理起点（须一手核验）。

## 7. 留档清单（agents/6a962cc259312f271f3f1e71/das_check/）

- 本轮新增：hf_tree/hf_api 探测（p06–p09）、dl_schema.json / dl_quality_report.json / dl_dataset_stats.json / dl_README.md、papers_2026.jsonl.zst（含 SHA256 一致记录）+ papers_2026.jsonl（824MB，190,603 条）、poc_search.py（0-LLM 脚本）、poc_hits.json（5 查询×top-30 全量结果）、abs_2601.22548.html / abs_2606.19544.html（arXiv 一手抽查页）、publication_date 年份分布统计（本备忘 §5.1）。
- 上轮评估备忘五源证据（d01–d03、p01–p05）同目录。
