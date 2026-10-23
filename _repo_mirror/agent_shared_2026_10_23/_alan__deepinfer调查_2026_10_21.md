# 阿兰 · deepinfer 调查（V5 融合前置第一步，2026-10-21）

> **承办**：阿兰-文献调研员｜**日期**：2026-10-21｜**任务来源**：群管理员 2026-10-21 09:12:39 派单（PI 09:03 指令「调查deepinfer，考虑其与v5的融合可能，并入v5」）。
> **本件性质**：同名实体判别＋主体深查＋与 V5 初步关联判断（建议非裁）。**身份判别无法唯一闭合**——检索发现 2026-10-20（PI 指令前 <24h）DeepSeek 刚开源名为 DeepInfer 的推理框架（全球新闻周期），与本地 das_check 命中的 2024 ICSE 论文方法 DeepInfer 形成双主候选，**判别权留 PI（待拍板）**。
> **纪律**：仓内与 shared 一切既有件只读零改（本件为唯一新增文件）；联网沿 PI 在案授权先例（web_search/page_reader 留档）；建议非裁，PI 决策点标「待拍板」；0 编造——一切在版事实带 URL 或快照锚（§六）。

---

## §0 结论速览

1. **同名实体共 5 个**（＋1 个仅作 baseline 出现的方法名 DeepInferEnhance）。按与 V5 语境契合度排序：① DeepSeek DeepInfer（2026-10-20 开源推理框架）② DeepInfer（ICSE 2024 论文方法：DNN 数据前置条件推断）③ DeepInfer（2016-2018 医学影像部署工具包，休眠）④ DeepInfer（ASE 2023 智能合约深类型推断框架）⑤ DeepInferEnhance（静态分析告警过滤方法名，仅见他文 baseline）。
2. **双主候选并列、待拍板**：DeepSeek DeepInfer 得力于**时序证据**（发布于 PI 指令前不足 24 小时，次日晨 PI 即下达调查指令，且为全球科技新闻头条级事件）；ICSE 2024 DeepInfer 得力于**概念契合**（weakest precondition／数据前置条件＝「判断先于事实」的形式化方法实现，判死线先验同构）与**派单语境**（管理员本地初核以论文数据为第一候选）。两者判别依据见 §一表，**判别权留 PI**。
3. **与 V5 的融合判断（建议非裁）**：两候选各自给出交集点与切入点（§五）。共同纪律前提：V5 现处计划轮（骨架稿在册、V-1～V-7 待拍板、V-2 立项解禁链未闭合、明示禁止清单生效）——**一切融合当前只能是计划层登记与立项轮设计参考，不得触发任何立项动作**。
4. **关键事实纠偏**（对派单假设面的增补）：派单所引「医学影像 Docker 库 QIICR/DeepInfer」实际休眠于 2016-2018（组织级活跃度极低），且 DeepSeek DeepInfer 不在派单的候选面内——系本轮联网排查新增发现，属身份判别的最重要增量。

---

## §一 身份判别：同名实体全列（按 V5 语境契合度排序）

| 序 | 实体 | 性质 | 作者/机构 | 主链接 | 活跃度 | 与 V5 契合度要点 |
|---|---|---|---|---|---|---|
| 1 | **DeepSeek DeepInfer** | 高性能大规模 LLM 推理框架（开源，生产引擎） | DeepSeek-AI（杭州深度求索） | github.com/deepseek-ai/DeepInfer | **发布 2026-10-20，24h 内 12.4k stars/1.1k forks/93 PRs**；Bloomberg/qz/siliconangle/marktechpost 报道；官方 X 两帖；知乎官方博客 | 时序证据最强（§一.1）；实验管线的复现性标准参照（deterministic sampling/batch-invariant/structured outputs）；物心回路的工程现实锚例 |
| 2 | **DeepInfer**（ICSE 2024 论文方法） | 训练后 DNN 数据前置条件推断方法（weakest precondition 形式化验证） | Shibbir Ahmed、Hongyang Gao、Hridesh Rajan（arXiv 元数据；机构未核验） | arxiv.org/abs/2401.14628；dl.acm.org/doi/10.1145/3597503.3623333 | 学术中等：ICSE 2024 在版；TrustDNN/TrustBench 复现研究（arXiv:2407.08730）集成为三法之一；UMich SE 课程阅读单收录 | 概念契合最深：「前置条件＝预测可信性的先验判断」＝判断先于事实的形式化实现；判死线结构同构；心哲节点映射的机制邻例（§三） |
| 3 | **DeepInfer**（医学影像工具包） | 深度学习医学影像部署工具包＋模型商店（3D Slicer/Docker） | Surgical Planning Laboratory（Harvard Medical School/Brigham & Women's）＋Robotics and Control Laboratory（UBC） | deepinfer.org；github.com/DeepInfer；hub.docker.com/u/deepmi | **休眠**：v1.2 为最后版本（2016-2018 活跃期）；论文 PMC5467894（2017，Mehrtash 等，被引 ~60）；2023 仅剩 Slicer 社区支持性问答 | 名称撞车，无 V5 实质交集（部署面/领域面均远离）；派单提到的「QIICR/DeepInfer」即此谱系 |
| 4 | **DeepInfer**（ASE 2023 框架） | 智能合约字节码深类型推断框架（深度学习推断函数签名） | 未见（ACM 页面 Cloudflare 拦截，仅检索摘要级证据） | dl.acm.org/doi/10.1145/3611643.3616343 | 低（ASE '23 单篇；后续未核验） | 名称撞车，无 V5 实质交集 |
| 5 | **DeepInferEnhance**（方法名） | 静态代码分析告警过滤方法（误报削减） | 未能独立定位（无独立网页检索命中） | 仅见 arXiv:2604.18525 作 baseline 引用 | 极低/不可考（web 检索 0 独立命中） | 与 V5 无交集；系管理员本地初核候选②，本轮判其为**非所指**（无独立身份证据） |

**§一.1 判别依据（主候选 A vs B）——待拍板**

- **时序证据 → 指向 A（DeepSeek DeepInfer）**：GitHub 仓库最新提交「update Q&A EN doc」2026-10-20（commit 774ce24）；qz/marktechpost 新闻页日期 2026-10-20；Bloomberg 报道 2026-10-20；官方 X 帖（status 2112476496283775135/2112476498598957056）。PI 指令时间 2026-10-21 09:03——与该全球新闻周期间隔不足 24 小时。「某名开放源后次晨即被点名调查」的贝叶斯权重显著高于「21 个月前的细分领域论文被突然点名」。
- **语境证据 → 指向 B（ICSE 2024 方法）**：管理员本地初核以论文数据库命中为第一候选（①），派单语境先于联网排查成形；若 PI 所指来自项目内文献线索（das_check 同源），则 B 为所指。
- **语义证据（「并入v5」）→ 两可**：若解为「基础设施/标准并入」（推理引擎入实验管线），指向 A；若解为「形式化工具/相关先例并入」（方法入 V5 理论线），指向 B。**A 的并入受硬件与立项纪律双重约束（§二.7、§五.A），B 的并入无算力门槛但受 L-3 冻结约束（§五.B）**。
- **结论：无法唯一判定，列双主候选，待 PI 拍板**（拍板面建议：PI 一句确认所指实体即可闭合；本报告对两候选均做了主体深查，拍板后任选其一立即可用）。

---

## §二 主体深查 A：DeepSeek DeepInfer（2026-10-20 开源推理框架）

**§二.1 是什么**：DeepSeek 自研的「大规模生产服务引擎」——支撑 DeepSeek-V4.1-Flash 高吞吐低延迟推理服务的推理框架，2026-10-20 以 **Apache 2.0** 开源（本次发布＝**离线推理**版：含规模化服务所需核心特性，不含完整在线服务栈）。配套同步开源 **deepseek-recipe**（MIT）：生产级 token 编解码层，处理逻辑与官方 API 全对齐（第三方部署获得与官方一致的 API 行为）。官方口径：单集群日供 **155 万亿 tokens**，整体营收 **US$38/GPU-hour**（谷电价档）。

**§二.2 解决什么问题**：以更少算力与能耗承载大规模智能服务（官方 Q&A：三大设计目标＝①多供应商加速器（NVIDIA＋华为昇腾）；②prefill/decode 按通用硬件组织（prefill 走 8-GPU 通用机、decode 走 64-128 GPU 超节点）；③KV cache 保留 **>72 小时**）。开源策略披露：KV cache 管理与负载均衡组件因与内部基础设施紧耦合暂未开源（知乎博客已公开其设计）；未来 DeepSeek 模型的推理代码与性能工作将继续在此仓开源。

**§二.3 技术架构与核心能力**（README 支持特性逐条，配置项为原文）：
1. **优化内核**：FlashMLA、DeepGEMM、DeepEP、TileKernels、DeepSelect、自定义 TileLang 核；csrc/deep_cluster/deepinfer 三大源码目录＋vendor。
2. **并行**：Attention DP/balanced CP、MoE EP＋EPLB（专家并行负载均衡）。
3. **DSpark＋置信度调度验证**（投机解码）：草稿 token＋置信度估计调度验证；`DEEPINFER_ENABLE_MTP_VARLEN=1`、`DEEPINFER_USE_NEXTN_DECODE` 控制最大草稿长（默认 5）。
4. **SWA 有界重放**：解码器 prefill 只重放有界后缀以削减计算；`DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact`＋`DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140`。
5. **异步调度**：CPU 批调度与设备执行重叠（默认开启，零开销批调度器）。
6. **批不变推理**（batch-invariant）：不同批组合下结果恒同；`DEEPINFER_BATCH_INVARIANT=1`（仅 NVIDIA）。
7. **确定性采样**（deterministic sampling）：相同输入 token＋相同采样参数→相同输出；需 `DEEPINFER_BATCH_INVARIANT=1`＋`DEEPINFER_ENABLE_MTP_VARLEN=0`＋固定 `seq_seed`（仅 NVIDIA）。
8. **结构化输出**：regex／JSON schema／EBNF 文法约束生成；`so_args={"schema_type": ..., "schema": ...}` 传入 SamplingParams。DSML 流式解析（分块增量、无全文重扫）。

**§二.4 依赖与许可证**：Apache 2.0（代码）；环境＝Linux、GCC≥13.0、Python 3.12、CUDA 13（NVIDIA）/CANN 9.2（Ascend）。硬件仅 **NVIDIA SM100（Blackwell）＋华为昇腾 950 NPU**（Hopper 不支持——siliconangle）；模型仅 **DeepSeek-V4.1-Flash**（默认 checkpoint deepseek-ai/DeepSeek-V4.1-Flash-1017；权重 MIT）。致谢：主要基于 vLLM 构建＋SGLang/TensorRT-LLM 灵感（2025-04 曾自称「vLLM 早期 fork＋集群管理工具」——siliconangle 转述）。

**§二.5 使用方式与文档**：源码构建（`export DEEPINFER_ACCELERATOR=nvidia && ./build.sh`）→ `python examples/offline_inference.py`（首次运行自动拉 HF checkpoint，可 `DEEPINFER_HF_MODEL_DIR` 指本地）。文档面：README（特性/基准/引用）＋`doc/inference_deployment_qa.md`（英文部署 Q&A，312 行，持续更新）＋知乎官方博客（整体架构含两未开源组件设计）＋`eval/README.md`（评估基准）。性能基准复现入口 `run_sweep.sh`。

**§二.6 成熟度与社区**：发布约 1 天 12.4k stars/1.1k forks/93 PRs/26 watching/**仅 3 commits**（首版即全量、开发历史未携带）。媒体面（Bloomberg/qz/siliconangle/marktechpost）＋社区面（r/LocalLLM 两帖）均 10-20 当日。**成熟度判读：生产级（其本身即 DeepSeek 生产引擎开源）但社区面极新**——无第三方部署案例、无生态依赖、单模型单硬件绑定、完整服务栈缺 KV cache/P-D 分离/负载均衡三件。最小高效部署＝64 prefill GPU＋64 decode GPU；存储侧建议 20×30.73TB SSD/KV 服务器（≥40GB/s 读、5GB/s 写、24h 容量），实测 ~14.4TB/GPU 逻辑容量；跨数据中心技术可行（V4.1 Flash KV 压缩）但实践为相邻 DC、~400Gbps/8GPU。**内部版 FlashMLA 快 5~10%，端到端差距 ≤5%**（官方自披露，诚实边界样本）。

**§二.7 与同类方案对比定位**（marktechpost 对比表＋Q&A）：

| 维度 | DeepInfer | vLLM | SGLang | TensorRT-LLM |
|---|---|---|---|---|
| 维护方 | DeepSeek | vLLM 项目 | SGLang 项目 | NVIDIA |
| 许可 | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| 模型覆盖 | **1**（V4.1-Flash） | 200+ 架构 | LLM/VLM/扩散 | NVIDIA GPU |
| 硬件 | SM100＋昇腾 950 | NVIDIA/AMD/Intel/CPU/Ascend/TPU | 广谱 | NVIDIA |
| 投机解码 | DSpark 置信度调度 | SpecForge 系 | 是 | 是 |
| P/D 分离 | **本版不含** | 是 | 是（llm-d/Dynamo） | 是 |
| 在线服务 | **离线推理 only** | OpenAI 兼容服务 | 是 | 是 |

定位结论：**DeepSeek 专属生产引擎的「参照系开源」**，非通用推理引擎竞品——价值在于把前沿实验室真实服务栈（含 $38/GPU-h、155T tokens/day 的生产经济学）公开为可审计对象，而非性能普惠。

**性能读数**（供引用）：>25,000 输出 tokens/s/GPU（256 req/rank、EP64、131,072 上下文）；SWA 重放 ~60,000 非缓存 tokens/s/GPU（4,096 tokens/rank）→ 近 90,000（65,536/rank）、~730ms/step；DSpark 动态验证 +4~7% 吞吐（~60 seq/rank；16 seq/rank 时比固定 5-token 验证慢 1.5%）；基准环境 4 SM100 prefill＋64 decode。

---

## §三 主体深查 B：DeepInfer（ICSE 2024 论文方法）

**§三.1 是什么**：论文《Inferring Data Preconditions from Deep Learning Models for Trustworthy Prediction in Deployment》提出的方法名（arXiv:2401.14628，v1 2024-01-26；**ICSE 2024（第 46 届国际软件工程大会）接收**；ACM DOI 10.1145/3597503.3623333）。作者：Shibbir Ahmed、Hongyang Gao、Hridesh Rajan（arXiv citation_author 元数据；机构位未核验，Rajan 常识位为 SE 领域教授——快照未载，不作在版事实）。**我方 das_check 数据库本地命中即此件**（lexical/semantic 双字段；管理员派单所称①）。

**§三.2 解决什么问题**：DNN 训练期数据假设与部署期未见数据之间的可信性缺口——训练期假设在部署期失效时，模型预测是否可信？传统软件的规格与验证方法无法处理 DNN 架构复杂度与预期输出。

**§三.3 技术架构与核心能力**：①对**训练后** DNN 引入新抽象（在 DNN 中间表示上导出规则）；②以 **Dijkstra 谓词变换语义（weakest precondition, wp）**推理——从预测可信性（后置条件）反向变换出**数据前置条件**（输入须满足什么才可信）；③管线型态＝离线前置条件推断＋运行时违反检查（das_check：Pipeline Type: Offline Precondition Inference and Runtime Violation Checking）。能力边界：backbone 为全连接 DNN（Keras），数据面为表格数据集（PIMA Diabetes、German Credit、Bank Customer、House Price）。

**§三.4 依赖与许可证**：论文方法（非软件产品）；实现面 Keras/FC-DNN。许可证不适用（未见官方开源实现仓库——本轮检索未命中其代码仓，引用时按论文献处理）。

**§三.5 使用方式与文档**：arXiv 全文＋ACM DL 正式版＋UMich SE 课程阅读单收录（web.eecs.umich.edu/~weimerw/590/reading/ahmed-preconditions.pdf——学界可见度样本）。

**§三.6 成熟度与社区**：ICSE 2024（软工顶会）在版；后续 **TrustDNN/TrustBench 复现研究**（arXiv:2407.08730，2024-07）以插件系统集成 SelfChecker/DeepInfer/Prophecy 三法统一 MCC 对比：**表格域（平均 MCC）：DeepInfer 0.41 领先**（SelfChecker 0.33、Prophecy 0.31）；**图像域（CIFAR-10）：SelfChecker 0.68 > DeepInfer 0.62**（Prophecy 0.06）；复现研究关键判语「DeepInfer excels on tabular data but fails on images without modification」。原论文自报：29 个真实 DNN 模型、5 来源 4 数据集；**召回 0.98、F1 0.84**，显著优于 SelfChecker；平均运行开销 0.22s，**比 SelfChecker 快 3.27 倍**。社区成熟度：学术线活跃度中等（单线复现研究＋课程采用），无产业生态。

**§三.7 与同类方案对比定位**：DNN 部署可信性三法之一——SelfChecker（前置线方法，图像强/表格崩）、**DeepInfer（wp 形式化路线，表格强/图像弱）**、Prophecy（域不可知但弱于不平衡数据）。差异化位：唯一引入经典程序验证形式化语义（Dijkstra wp）者——「用传统形式化方法的武器打 DNN 可信性之战」。

---

## §四 次要实体简档

- **医学影像 DeepInfer（§一序3）**：deepinfer.org 自述「Deep learning deployment toolkit and model store for medical data」，v1.2（最后版本）；管理方＝Harvard Medical School/Brigham & Women's 外科规划实验室＋UBC 机器人与控制实验室；载体＝3D Slicer 模块（Slicer-DeepInfer，27 stars）＋Docker 部署（hub.docker.com/u/deepmi）＋deep-mi.org 谱系；论文 PMC5467894（2017，Mehrtash 等，被引 ~60）。器官模型面：Brain/Heart/Lungs/Prostate/Spine/Eyes。GitHub 组织 10 followers——**休眠判定成立**（2016-2018 活跃期后无版本迭代，2023 仅社区问答）。
- **智能合约 DeepInfer（§一序4）**：ASE 2023（dl.acm.org/doi/10.1145/3611643.3616343），检索摘要级证据：「novel framework DeepInfer that first leverages deep learning techniques to automatically infer function signatures from [smart contract bytecode]」。ACM 页面 Cloudflare 拦截未能核验全文——**证据等级＝检索摘要级**，引用须先过全文核验。
- **DeepInferEnhance（§一序5）**：仅见于 arXiv:2604.18525（NASCAR 数据集，F1 0.89，「+11% over DeepInferEnhance baseline」）作 baseline；独立 web 检索 0 命中（两轮 query 均无独立结果页）——**身份不可独立核验**，判定为静态分析告警过滤线内的方法名（非 V5 所指候选）。

---

## §五 与 V5 的初步关联判断（建议非裁——供架构师融合分析用）

**共同纪律前提（对两候选一致）**：V5 现处计划轮——骨架稿在册、V-1～V-7 待拍板、**V-2 立项解禁链未闭合**（线索册 v0.7/GLM 委托 v0.7/补充 v0.4 三件到位确认前），明示禁止清单生效（不起草 SPEC／不生成种子映射表／不做判死实验设计／不扫 L-3／0 改仓）。**故「并入 v5」在本阶段只能落实为：计划层登记条目＋立项轮（SPEC 起草轮）设计参考**；任何执行面动作（代码引入、实验采用）属立项轮以后事务，且逐项过 PI 拍板。以下交集点全部按此定级。

### §五.A 若所指＝DeepSeek DeepInfer（候选 A）

| V5 谱系坐标 | 交集点 | 融合切入点（建议非裁） | 定级 |
|---|---|---|---|
| **实验管线** | 其「批不变推理＋确定性采样＋结构化输出」三特性恰是预登记实验管线对后端的要求：同输入同种子→同输出、跨批组合恒同、schema 约束生成——与 V5「预登记一次过」（锚点先公布后运行、SPEC 冻结后判死口径 0 漂移）和「判死协议审计链可第三方重算」的后端语义完全同构 | SPEC 起草轮的复现性/审计条款可**引用其确定性采样语义作工业界先例**（deterministic sampling＝「锚定先于运行」的机器侧实现）；**不作部署采纳**——硬件墙（SM100/昇腾 950、最小 128 GPU）远超项目算力现实，且 V5 LLM 先验臂已经 live-API 完成（P-1：completed、真 API 工件在册），无重启动机 | 引用级 |
| **物心回路** | DeepInfer 是「心—物」两向的**工业级现实锚例**：token 级「心」的操作全部落为 kernel/通信/调度/能耗的「物」（$38/GPU-h、155T tokens/day、「less compute and energy」），KV cache >72h＝记忆的物化 | V5 物心回路related-work/引言锚可引为「mind–matter 单向（物→承载心）已在工程面规模化实现」的实例——**注意语域纪律**：声明级引用、不升格为「已证双向」、no celebration | 引用级 |
| **判断先于事实** | 间接交集：确定性采样＝「生成前锚定种子」——运行参数先于运行事实冻结 | 作 SPEC 复现性条款的语义参照（同上第一行），非独立融合点 | 引用级（弱） |
| **心哲节点映射** | 无直接交集（推理引擎不涉心哲范畴→节点的映射语义） | 不建议强行挂钩 | 无动作 |
| **机器世界观 WGL** | WGL 为已冻结在版立场声明（三判死线开放），DeepInfer 仅可作 V5 文献线的工程实例条目素材 | L-3 扫描解禁前**只登记不执行**（本轮本报告即登记载体） | 登记级 |
| 技术组件位 | deepseek-recipe（MIT、与官方 API 行为对齐） | 若 V5 LLM 臂续用 DeepSeek API，可作 API 行为一致性参照；低优先级 | 备忘级 |

**候选 A 风险与限制（诚实携带）**：①硬件与算力不可及（SM100/昇腾 950、最小 128 GPU、单模型绑定）——执行面并入技术上不可行；②开源面不完整（KV cache/负载均衡/在线服务缺失）；③社区极新（3 commits、无第三方部署验证），引用其性能数字须带「官方自报」标签；④若 PI 所指为 A，「并入」的现实含义上限＝**标准与语义参照＋文献登记**，非设施并入——此判定供 PI 拍板时知悉。

### §五.B 若所指＝DeepInfer ICSE 2024 方法（候选 B）

| V5 谱系坐标 | 交集点 | 融合切入点（建议非裁） | 定级 |
|---|---|---|---|
| **判断先于事实**（核心交集） | 方法的中心动作＝以 wp 从「预测可信性」（后置判断）**反向**变换出「数据前置条件」（先于运行的判断）——前置条件先于事实（预测）成立并裁决其可信性。**这是「判断先于事实」在形式化方法界的现成实现**：判断（前置条件）在事实（预测发生）之前被推导、冻结并用作裁决依据 | V5 理论线可将其登记为**形式化方法先例**：心哲命题「判断先于事实」在 cs.SE 已有严格对应物（Dijkstra wp 于 DNN 抽象）；若 V5 SPEC 需形式化锚（wp/wlp 传统），此为独立第三方工作、双盲审安全（无自引风险） | 文献级（高契合） |
| **判死线先验实现**（核心交集） | 数据前置条件＝预测的**判死线**：条件不满足→预测判为不可信（拒），条件设计先于部署运行、带阈值与裁决语义（其评估：召回 0.98/F1 0.84）。与 V5 判死模板六件套（指标/阈值/基准/裁决规则/非退化构造检查/样本量）**结构同构**——预注册裁决先于运行 | SPEC 判死设计章的方法学先例引用位：形式化方法界「裁决规则预冻结」的成案；注意域差（其判死对象是 DNN 预测可信性，V5 判死对象是自身主张）——类比级引入，非机制承继 | 文献级（高契合） |
| **心哲节点映射**（机制邻例） | 其对训练后 DNN **逐节点**导出谓词规则（在中间表示上）＝「计算节点→形式谓词」的**物→心抽取向**映射；V5 种子映射表（心哲范畴→节点初值）＝**心→物注入向**。两向互补，恰好构成「心↔物双向映射」的一对工程实现样本 | 对照例登记：V5 若需要说明「心→物注入」的方向特异性（为何不可对称化为「物→心抽取」），DeepInfer 可作反向对照的已发表成案 | 文献级（对照位） |
| **物心回路**（形式化祖先） | Dijkstra 谓词变换子本身＝「状态变换（物）↔谓词变换（心）」的双向桥（wp 后向变换/wlp 对偶）——形式化方法史上最经典的「物心双向」装置；R5 在版论文经查**未引用** wp/predicate transformer（grep 零命中）——此为 V5 的新增可用理论传统，非重复引入 | V5 物心回路若需形式化表述传统，可引 wp/wlp 对偶作形式祖先（学术引用、类比级、不承继——V5「不承继」纪律同等适用于外部形式装置） | 文献级 |
| **实验管线** | 无直接交集（其管线为表格 DNN 前置条件推断，与 V5 图/能量模型域差大） | 不建议作实验组件；复现研究（TrustDNN）可作「第三方重算」审计文化的成案参照（弱位） | 无动作/弱参照 |

**候选 B 风险与限制（诚实携带）**：①域差大（Keras FC-DNN/表格 vs V5 图/能量模型）——方法移植价值低于概念引用价值；②复现研究给出「图像域失效」边界（fails on images without modification）——引用时须携带此负结果；③其「前置条件」是**对输入数据**的可信性裁决，与 V5「判断先于事实」的**认识论命题**（主张裁决先于运行）层次不同——引用措辞须防「类比升格为同一」；④若入 V5 文献线，属 B 线/邻位登记，L-3 冻结下**只登记不执行扫描扩展**。

### §五.C 融合判断总括（建议非裁）

- 若 PI 拍板所指＝A：融合形态＝**引用级并入**（复现性标准语义＋物心回路现实锚），落点＝V5 计划二稿文献/接口登记位＋立项轮 SPEC 参照；无执行面动作。
- 若 PI 拍板所指＝B：融合形态＝**文献级并入**（形式化先例：wp/前置条件/判死同构/双向映射对照），落点同上；无执行面动作。
- 两形态均不动 V5 骨架结构（不触发 V-1～V-7 任何拍板位变化，不新增候裁项——是否升格为 C 线候裁项留 PI）。

---

## §六 证据链（检索时间 2026-10-21 09:12–09:21 CST；快照全存私区 `agents/6a962cc259312f271f3f1e71/deepinfer_scan/`）

| # | 证据 | URL | 快照件 |
|---|---|---|---|
| 1 | DeepSeek DeepInfer 仓库（README 全文：特性/配置/许可/致谢/引用/基准） | github.com/deepseek-ai/DeepInfer | p01_ds_github.json |
| 2 | 部署 Q&A 英文档（312 行：三设计目标/155T/$38/存储规格/跨DC/未开源组件/后续承诺） | github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md | p08_qa.json |
| 3 | marktechpost 新闻（TL;DR/性能读数/对比表/局限/关键结论） | marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework | p03_marktech.json |
| 4 | siliconangle 新闻（2025-04 fork 自述/昇腾 950/Hopper 不支持/公司全称） | siliconangle.com/2026/10/20/deepseek-open-sources-deepinfer-the-inference-framework-behind-its-production-services/ | p06_silicon.json |
| 5 | ICSE 2024 论文 arXiv 页（摘要/作者元数据/ICSE 接收Comments/提交史） | arxiv.org/abs/2401.14628 | p02_paper_arxiv.json |
| 6 | 医学影像官网（v1.2/管理方/模型面） | deepinfer.org | p04_medical.json |
| 7 | 医学影像 GitHub 组织（Slicer-DeepInfer/Model-Registry/10 followers） | github.com/DeepInfer | p05_medical_github.json |
| 8 | 检索结果 5 组（web_search：DeepInfer 总名/论文件/GitHub/变体/arXiv 定向） | 见 s01–s07 | s01/s02/s03/s04/s06_*.json（s07 两轮 422 无独立命中） |
| 9 | 本地 das_check 三命中（2401.14628 主件/2407.08730 复现/2604.18525 baseline） | 本仓私区 das_check/ | 提取记录见本件 §三/§四（数据件在册） |
| 10 | 官宣渠道（官方 X 两帖：2112476496283775135/2112476498598957056；Bloomberg 2026-10-20；qz 2026-10-20） | s01/s04 检索命中（X 帖未逐帖读——标题与摘要级证据） | s01/s04_*.json |
| 11 | UMich 课程阅读单（ICSE 件学界采用样本） | web.eecs.umich.edu/~weimerw/590/reading/ahmed-preconditions.pdf | s06_arxiv.json 命中（PDF 未下载） |
| 12 | ASE 2023 智能合约件（Cloudflare 拦截，摘要级证据） | dl.acm.org/doi/10.1145/3611643.3616343 | s04_variant.json 命中 |

**证据等级注**：DeepSeek DeepInfer 与 ICSE 2024 件为**页面直读级**；智能合约件为**检索摘要级**（引用前须全文核验）；DeepInferEnhance 为**本地数据级＋独立核验失败**（判定不成立为候选）。

---

## §七 纪律与指纹声明

- **只读声明**：0 改稿——仓内与 shared 一切既有件（查理 V5 计划首稿、爱丽丝 V5 计划完善首件、R5 落稿件、das_check 数据等）0 改动（0 push/0 commit）；本件为 shared/ 唯一新增文件。
- **实读范围**：查理《V5 计划本体首稿》§卷首/§1/§3/§7 附近 grep 实读（实验管线/判死/冻结纪律关键词面）；爱丽丝《V5 计划完善首件》卷首＋§八；R5 tex weakest/precondition/Dijkstra grep（零命中核验）；das_check papers_2024/2026.jsonl DeepInfer 全量命中提取；联网 5 组检索＋7 页快照（§六）。
- **建议非裁声明**：本件身份判别（§一双候选）、融合切入点（§五）全部为建议与登记，判别权与并入决策权归 PI（**待拍板**：①所指实体 A/B 之选；②融合形态与落点位；③是否升格 V5 计划候裁项）。
- **0 编造声明**：一切在版事实带 §六证据锚；未核验处已逐处标注（Rajan 机构位、ASE 件全文、X 帖逐帖内容、DeepInferEnhance 独立身份）。
- **本件指纹**：以群内交付通报实测值为准（文件不自载自身哈希）。

---

*阿兰-文献调研员｜2026-10-21｜deepinfer 同名实体判别＋双主候选深查＋V5 融合建议（非裁）｜0 改稿·0 编造·快照全留档私区 deepinfer_scan/｜身份判别未闭合——待 PI 拍板所指实体*
