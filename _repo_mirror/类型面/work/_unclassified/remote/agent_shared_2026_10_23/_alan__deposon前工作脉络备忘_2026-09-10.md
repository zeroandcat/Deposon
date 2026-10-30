# deposon 前工作脉络备忘

整理：阿兰-文献调研员 ｜ 2026-09-10
材料源：本环境 〔本地路径已脱敏〕 现有文件（用户已澄清所指为本机 Deposon_v1_2_0_交付包内的 upload 目录，该包尚未上传；故本备忘先基于环境内现有文件梳理，包上传后可对照补核；包内脚本 bug 已修正，不作关注）

## 一、deposon 之前是什么研究

**起点概念**：v1「阻塞」与 v2「穿越」两个独立机制——v1 对错误路径本地反射衰减（PII-BT 基线上 blocked→final_prob×0.1）；v2 经节点共轭对走推理捷径（tunneling→computation_cost×0.5）。

**理论收拢**（2026-08-21《凝子统一场论研究报告 v1.0》＋《Deposon_Requirements_v1.md》，定义期）：命名 Deposon＝Deposition＋-on（凝子，取「凝华」义）。核心主张：
① 认知能量三通道散射 E_in＝E_trans＋E_ref＋E_aether，错误能量凝华入无限维正交以太、不可逆（Poincare 回归失效）；
② v1/v2 非两种粒子，是同一凝子按以太耦合 g_aether＝0／≫0 的两个极限态（现口径：两相划分）。
配套件：Feshbach 共振式、PCM/MZI/ECM 器件映射、GoT/ReAct/R1/Kimi 集成设想、DeposonField 逐路径审计概念代码。

**关键结果定性**：纯定义期文档——全文无冻结 JSON 实证数字（PCM 等器件参数属外部概念参数），自带六条诚实边界（无限维须截断、参数无通用调优理论、认知能量仅为隐喻等）。
〔出处：统一场论报告_v1.pdf；deposon-repo/docs/Deposon_Requirements_v1.md；一致性核对_20260907.md〕

## 二、如何演进到 Deposon（凝子）框架

**衔接点（终稿继承的零件）**：三通道守恒→会计恒等式 T+R+A=1（逐路径审计最大偏差 2.2×10⁻¹⁶，机器精度）；逐路径审计→「持双精度算术的第三方可逐步重算」的账本主张；耗散不可逆→谱前提证据（g_aether=0 且含环时 58/338 发散）。

**转折点**：① 物理隐喻大面积退场（暗物质/以太/共振/硬件映射未入终稿主线）；② 引入预登记判定＋判死纪律——三层级「动力学≈最优响应」(P1a/P1b/T-P1c) 全灭、P2 降级为近似势博弈、P3 双向判死，「与死同行」成为论文最硬章节；③ E9.5 阴性边界（真实基准与 6 关键词规则过滤器不可区分）后，主张收缩为「散射层不更准，但它记账且账可重算」；④ 博弈论形式化（ECR/势博弈/近梯度性）成为主线，2026-08-30 收束，中英终稿（CN 17p／EN 24p）双审 PASS 交付。
〔出处：成果汇报_2026.md；handoff_machine_readable.json；deposon_paper_final_cn/en.pdf〕

## 三、后续协作关键事实（10 条）

1. **唯一机读事实源**：handoff_machine_readable.json（schema deposon-handoff/v1，2026-08-30 生成）；继任先读 headline_results／terminology_redlines／preregistration_anchors_sha256_12／environment_recipes 四字段。〔粘贴文本1.txt〕
2. **术语红线**：PoA→ECR（分布级协调比）；「已证」→已闭合（预登记判定）；「穷举」→系统采样 61 图×338 任务×6760 状态；「相变」→两相划分；另禁「统一终稿/阶段稿/存在性实证」等元表述。〔粘贴文本1.txt；handoff json〕
3. **判死资产**：P1a max_dev_inf=0.8569；T-P1c τ∈[0,4] 81 档 min cos=−1.0、τ* 中位 0；P2 含环中位 0.669（占比 0.924）；P3 双向 0.1585/0.8442。〔handoff json；成果汇报〕
4. **ECR／E9.5**：ECR median=4/3（17 张有限值图，∞×3 单计，覆盖 20/22）；E9.5 非配对 Newcombe CI：GSM8K −2pp [−11.8,+7.8]pp。〔handoff json；成果汇报溯源表〕
5. **数字溯源公理**：任何数字须指向冻结 JSON 字段路径，否则砍掉；审计＝重跑对比而非字符串锚点（AUDIT-2026-08-30 首次真实重跑 PASS；pytest 398 passed）。〔粘贴文本1.txt；handoff json〕
6. **治理铁律**：论文修改只由独立子代理执行，成稿前双审全 PASS；verifier/vN 版本化不覆盖；重跑一律在 〔本地路径已脱敏〕 副本执行，不触冻结工件。〔粘贴文本1.txt；handoff json〕
7. **预登记锚点**：SHA-256 前 12 位×5（如 GT_FORMALIZATION_v1.md=aeefb8ef6972、run_v22_p1c.py=6e9673205dc0），可机械复跑。〔handoff json；成果汇报〕
8. **活态方向**：P-A 均衡稳定化成本＞P-B 可验证宣言＞P-D 可审计账指纹＞P-C 两相结构；学术挂点〔当事人W〕（〔高校R〕；STOC'23 双边贸易固定价格机制、AAAI 均衡迁移成本），接口为「稳定化成本 vs 迁移成本」对偶。〔handoff json；v3定义与博弈论贡献思考_2026.md〕
9. **安全红线**：两枚 API key（Kimi/Ark）永不落盘、永不进子代理提示词；密钥扫描正则自身须泛化并纳入扫描（历史事故在案）。〔粘贴文本1.txt；handoff json〕
10. **历史档定位**：统一场论 PDF 为定义期历史件（08-21），不在 08-30 交付清单内；其结论句旧措辞与「两相划分」红线冲突（对外复用须先整改）；Chapter 7 代码以 detuning² 简化共振，与 §2.3 完整 Feshbach 式有实现差异。〔一致性核对_20260907.md〕

> 备注：本备忘全部数字均可溯源至上列文件；未见于出处文件的数字一律未采用。
