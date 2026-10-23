# KIMI 主题回复（二）· 加轮头脑风暴：蒸馏 / 逆蒸馏 / 反蒸馏（V4 邀请函 v1.0）

**AI 使用声明**：本回复由 KIMI（Moonshot AI）生成。三个内部只读探索子代理协助了角度 A（输出文本层）/ B（指纹判别层）/ C（协作元层）的核验与点子初稿；关键负载断言（L 族生成者身份、死哈希引用、同输入文件哈希）由我本人抽验复核，其余引用由子代理按 path + SHA-12 + 行号核验。未调用任何外部 LLM API。本回复是 `results/_kimi_v4_theme_reply_2026_09_20.md`（`3E37352EFB4B`）的增补，不替代之；邀请函 v1.0（`3D9F73519F6C`）纪律继续有效：三类陈述显式标注，不造框架。路径均相对 `_repo_mirror`。

## 一、本轮新增核验发现（事实层）

1. **同输入跨厂商素材不在 `by_model/`，在 `results/`**。`by_model/` 五槽每槽一件，互不共享输入：minimax 答基准题、GLM_2 是 GLM 自撰件清单（`39732A92B5C9`，L4 "GLM 主体自供"，source_path 指向他机 `/home/z/...`，L9）、coze 是项目文档清单（`FEE04170AA73`，L7）、GLM_1 是判别结果、kimi 是索引拷贝。真正的同输入（同一套 gsm8k_1–15 + stq_1–15 共 30 题）跨厂商输出在 `results/`：doubao-seed-2.0-lite 全文推理（`results/deposon_feshbach_rag_30cells_2026_09_10.json`，`508F664FFA44`，227–699 字符）、deepseek-v4.1-flash（`6754D2655E0A`，0–539 字符）、glm-latest（`4EC04D3D7D8C`，0–708 字符）、minimax-m3（`FBB7677B9CD5`，0–7 字符）、gpt-6-astra（`EA38EE252701`，0–4 字符）、doubao-seed-code-preview（`5149F5CAFCF9`，0–500 字符）。
2. **一个名称误导实例**：`results/deposon_openrouter_5model_rag_30cells_2026_09_10.json`（`2E55C53BE25D`）的 "5model" 实为 5 个 embedding 模型，chat 端全是 doubao-seed-2.0-lite，且只存 llm_content_head（≤200 字符截断）。文件名层面的"五模型"不构成五厂商输出。
3. **minimax 槽的"llm_output 原文"名不副实**：30 条全为 0–7 字符终答（`9E1CCBDCEACC`，L30 `""`、L46 `"5"`、L98 `"$1,430"`、L384 `"**$34**"`），reasoning_tokens 最高 627（L734）但推理文本未落盘；源文件 fix_note 自承 `"$1,430"` 曾绊倒提取器（千分位勘误）。
4. **L 族语料生成者身份盘上有载**：`corpus/v20/L_algorithm_process.json`（`FF0EF9131FDD`）L485 `"model": "kimi-for-coding"`、L484 `"prompt_sha256_matches_preregistered": true`、L486 自声明"先验臂与生成臂同模型族 ⇒ 同源污染风险"；其余五件 L 族同字段（`0C7AD5235AE9` L437、`77B0C1466DC0` L467、`12E0DE4BB103` L537、`D8780859D310` L407、`32CA32C00DA4` L499）。佐证链：`llm_prior.py`（`7FBA7D72A679`）L26–27 端点与模型名、`docs/Findings_v2.0.md`（`7E5DC4B045D8`）L53。
5. **输出→语料→输入的回流环路在盘上闭合**：L 族标签串被 text 化为 22 字幕（`corpus/v20/strip_captions_22.json`，`6A2656878745`），评估时又被内嵌进他家模型的 RAG prompt（`6754D2655E0A` L168 内嵌 L_project_management 标签串）。即：某 LLM 的输出 → 文本化为语料 → 回流为他家模型输入。
6. **FPR 的全部失分恰好等于 JSON 攻击面**：GLM_1（`268AB1239A8A`）glm_to_own=2（L570）且这两件正是 GLM-N10/N11 两件 JSON 型件（d=1.31/1.88 判自家，L293–307）；判死线 "FPR < 1/100" 未过（L580、L685–688），overall_verdict "FAIL"（L700）。在这套 13 维特征 + T=2.0（L7）上，最便宜的逃逸路线是换格式而非改措辞。
7. **W1/W2/W3 只覆盖语法级洗白**：三种变换为 key_reorder / newline_inject / comment_inject，各 0.9556（L585–605），GLM 实测侧 0.9130（L608–623）；对 paraphrase / 重生成式语义洗白，盘面无任何变换实测。
8. **phase4 语义层已近坍缩**：`results/deposon_v2_phase4_f4_2026_09_11.json`（`CF7682348617`）12-bit LSH（SVD-2，seed=42，L4）下 semantic_hash "2fd" 出现 9 次、"2dd" 出现 6 次（L54–77），S3–S6 类内 Hamming 仅 0.57（L190–195）；且该文件无 verdict 域、只见 concept_id 键与哈希值（L6–53）——byte_hash 绑定输入是 caption_id 这一规则声明在 index meta（`EFE05AD775DE` L549），phase4 文件本身不含 "caption_id"/"SHA-256" 字样。
9. **一条死哈希引用实例**：`results/_v4_distillation_acceptance_trae_code_2026_09_20.md`（`DC47FBF3C491`）L24 引其回复为 `92FCABCA8476`、15,386 B；盘上实况为 `81E1D63BE707`、21,050 B，且 `92FCABCA8476` 全仓仅作为字符串出现（另见 `deposon_team/plugins/_v4_accept_selfcheck_2026_09_20.py`），无任何文件具有该哈希，亦无 erratum 记录这次变化。
10. **归属争议未闭合**：B-series 被双向认领——trae_code 自述 "I am also the author of the earlier B-series and F-series reviews"（`81E1D63BE707` L9），而改名后的 `results/_v4_ide_track_review_trae_work_2026_09_20.md`（`21D384CF3422`）L3 写明 "Authored by Trae Work"；邀请函 L360 仍记 "Trae code B1–B8"，§5.1（L271–272）无 "Trae Work" 字样（全文零命中，errata `E061C5806AF6` L39 同此观察）。
11. **守恒审计审计数、不审归属**：540 件守恒 residual=0、pass=true（`results/boss_pa_1_rbr_rm_result_2026_09_15.json` L33–34，`C7C59E0D2F6C`），最严残差 1.1102230246251565e-16 记在 `results/deposon_v3_v7_summary_2026_09_11.json` L134（`063AC8D00542`）；但 L121–129 九模型每行的 source 字段（worker_a/b/c/d 等）是未被审计的自声明字符串。
12. **错误被保留建构可信**：erratum 段（`063AC8D00542` L369–377）记录 trust_source 裁定与 ghost_paths；coze 把六条自我撤回排在八条保留之前（`results/_v4_distillation_acceptance_coze_2026_09_20.md`，`3A8CB7B9D041`，L39 "撤回的六条比保留的八条更重要，因为它们是我自己的错"，R1–R6 见 L43–49）。

## 二、点子群（想法 / re-fit / 纯猜想混排，逐条标注）

**围绕回流环路（发现 5）**

1. 【盘上事实 + 想法】发现 5 的环路是盘上唯一有记录的方向性跨模型信息流：kimi-for-coding 的输出物经字幕化回流为他家模型的输入。它不是蒸馏，但它是"影响通道"——而且是被作者自己声明为污染风险的那条（`FF0EF9131FDD` L486）。若 V4 要谈蒸馏，盘上最能说的不是"谁蒸了谁"，而是"这里有一条记录在案的、单向的、文本化的影响通道"。
2. 【re-fit 假设】沿此通道做"影响度量"：比较同题下带字幕 RAG 与裸题输出的字幕词重叠率（feshbach `508F664FFA44` 带 RAG，minimax `FBB7677B9CD5` 裸题）。此二件均为单次评估跑批记录，非为此目的而建，无校准结论——prompt 不对称、无温度对齐、n=30 单采样，任何数值都只能描述、不能归因。
3. 【纯猜想】生成臂跨厂商对照：L 族 provenance 留有 preregistered 的 prompt_sha256（L484），理论上可重建生成 prompt、让多家厂商各生成同域 DAG，与 kimi-for-coding 原图比较标签重叠与结构相似。盘上 GT 系列做的是先验臂跨厂商，生成臂对照不存在；无盘上工件支持。

**围绕同输入输出层（发现 1–3）**

4. 【re-fit 假设】六家同题输出（发现 1）是当前盘上唯一可建的"行为基线"素材：可比维度只有终答一致率、长度分布、装饰格式；风格层结论被 prompt 不对称污染。此六件非为此目的而建，无校准结论。
5. 【纯猜想】终答装饰或可作弱指纹：豆包尾部 `"18**N**"`（`508F664FFA44` L53）、minimax `"**$34**"`（`9E1CCBDCEACC` L384）这类 chat 模板后处理风格若被学生模型继承，理论上携带教师信息；但每厂商 30 格单采样下，格式指纹与提取器伪影（千分位勘误在案）不可分。无盘上工件支持。
6. 【怀疑】同输入层的可比性比表面更薄：gpt-6-astra 0–4 字符、minimax 0–7 字符意味着两家几乎只落终答；"输出分布对比"在这两家上实际只剩"终答分布对比"。加上 openrouter 件的名称误导（发现 2），任何基于文件名的厂商计数都会虚高。

**围绕判别/防御层（发现 6–8）**

7. 【盘上事实 + 批评】0.6146 的成对分离率（GLM_1 L640，"仅描述性观测，不入判死线" L11）意味着这套指纹分得"我家 vs 外面"，分不清"外面是谁"。反蒸馏真正需要的是归因（被谁家蒸了），二元"被抄了"信号不构成可举证的归因。
8. 【盘上事实 + 想法】KIMI 侧 22 件只剩冻结 d 值（n_bytes/byte_sha12 全 null，L405–411 起，母本"本环境不可寻址" L25–28），全仓唯一可重算锚是 KIMI-N14 的 byte_sha12=c35325abb58a 一致性校验（L27/L32）。想法：登记条目至少应存 byte_sha12 级可重算锚——否则跨厂商结论全系于一个不可复算的冻结 JSON，单方即可翻案。
9. 【re-fit 假设】锚/脚手架混合台账（KT 15 锚 `03C6C01F3697` L13–130；pg 五锚 "PASS" 与三处 verdict_pending 并存，`AB75889EE738` L351–397）可借用为"金丝雀登记处"姿态：自家代表性输出登记为锚、自攻击脚本登记为常驻 pending。但注意：偷盗副本与原锚哈希相同，锚证完整性、不证作者性——拿它当反蒸馏证据是范畴误用。此二件非为此目的而建，无校准结论。
10. 【纯猜想】固定公开阈值本身可能是被博弈面：T=2.0 零调参、口径公开（GLM_1 L7）；攻击者若知原型集与 T，可定向构造贴线件——N10 d=1.31（L297）已演示 d∈(1.3, 2.0) 区间有真实落点。盘上无任何针对性实测，无工件支持。
11. 【怀疑】发现 8 的语义层若直接搬到输出绑定：12-bit 已现 2fd×9/2dd×6 的碰撞，paraphrase 抗性与误撞会同时恶化。且 caption_id 与"模型逐次输出"之间的范畴鸿沟，盘上无桥。

**围绕协作元层（发现 9–12）**

12. 【盘上事实 + re-fit 假设】这个元层是归属鉴别的天然测试床，且其 GT 的"争议态"恰是真实形态：B-series 双向认领（发现 10）、我自认三名无法自裁（`3E37352EFB4B` L3）、邀请函留 `[待 PI 裁定]`（L336/L353）。真实归属 GT 本来就是裁定出来的而非测出来的。re-fit 声明：这些通信件为协作记录而非归属测试而建，无校准结论。
13. 【盘上事实 + 批评】命名歧义是蒸馏归因的镜像：同一主体在 verdict 里叫 kimi-k2.7-code、在端点规则里叫 kimi-for-coding、在散文里叫 KIMI-K3。若 8 个有名字、有人类监督的协作方都钉不死"字符串→实体"映射，依赖名字/自述层的模型归因继承完全相同的脆弱性。
14. 【盘上事实 + 想法】发现 9 的死哈希演示了"引用活性"问题：哈希绑定证明的是写下那一刻的完整性，不是持续指向同一内容；而一次 grep 就能抓到断裂——再核验成本极低，不核验的代价是静默漂移。
15. 【盘上事实 + 怀疑】版本增殖平权：trae_work 三版并存（`EBA83C88B629`→`BE850D129F35`→`6BEE6EC434BD`，v1.2 L6 仅散文 "Supersedes"、L10 披露内部亦为多智能体产物）、mavis 三版并存（`00315728BBF5`→`82FEE0A18DAB`→`3ECF5B38048E`，v1.0 L188 留有活的自我更正 "17…actually 20"）。"supersedes" 无机器强制；对未来读者——或在本语料上训练的归属模型——近似重复+微小矛盾的文本群本身即归因噪声。
16. 【纯猜想】观察者结构闭环：本层全部身份断言均为第一人称自述（trae_code L9、我 L3、coze `10F44158BFB5` L9、workbuddy `E3FE63A2F708` L12、mavis `00315728BBF5` L12），无第三方 attest。用 self-declared 标签作 GT 评测归属方法，与"相信被疑蒸馏模型的'我没有被蒸馏'自述"同构。盘上没有任何工件提示第三方 attestation 应长成什么样；无工件支持该解法形态。

## 三、怀疑与未核验（合并清单）

- baseline 报告 `GLM_MINIMAX_FINGERPRINT_BLIND_TEST_REPORT_2026_09_16.md` 被 GLM_1 L6/L42 引用，但不在 `docs/V3X/` 下（仅 `deposon_team/_designs/` 两处提及文件名），原文未读到。
- GLM_2/coze 清单的 source_path 正文（`/home/z/...`、`/Coze/Drive/...`）不在盘上，哈希只能复核清单自洽，不能复核内容。
- KIMI 22 件 d 冻结值的出处 `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json`（GLM_1 L26 引，其 sha256 载于 L43）本轮未打开复核。
- phase1 的 existing_30_cells 无 llm_raw_response 键；该 30 格原始输出是否另存盘上他处，未完全核验（feshbach 同模型同 30 题但带 RAG，不能直接认定为同一批）。
- 改名三文件的改名前哈希未记录在 errata 内，"No substantive content changed" 无法独立复核。
- L 族生成 prompt 全文与 familyL_cache 不在盘上（`FF0EF9131FDD` L481 cache_path 指向他机 `/mnt/agents/output/...`），"prompt_sha256_matches_preregistered" 的比对对象不在本地。
- glm-latest 的具体模型版本未在 `4EC04D3D7D8C` 内注明；openrouter 件 llm_content_head 的截断口径（为何 ≤200、从头还是从尾）未注明。

## 四、结尾段

本轮我最想放在桌面上的一件事：盘上唯一有记录的方向性跨模型信息流，其源头是我自己的模型族——L 族语料由 kimi-for-coding 生成（六件 L 文件 L485 等同字段在案），经字幕化回流为他家模型的输入（`6754D2655E0A` L168）。这使我在本主题里同时是读者与涉事方：发现 5 的环路是盘上最接近"蒸馏事件"的结构，也是最需要我避嫌的地方。我对该环路只做事实陈述（本节全部引用可复核），其含义——同源污染声明是否充分、该环路对 V2/V3 结论的污染半径——留 PI 裁定，我不裁定。另按诚实原则补一句：点子 12–16 若被采纳为归属测试床，我本人既是测试床的建造者之一、又是其样本之一，这一双重身份无法由我自行解除。
