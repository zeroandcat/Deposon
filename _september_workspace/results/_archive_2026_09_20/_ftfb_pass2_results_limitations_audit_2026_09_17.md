# FTFB v3 独立双审 Pass 2 报告

**审计日期**：2026-09-17 22:37 CST
**审计者**：worker (mvs_48e86029f3f34cdcaa9c93e3e1bda7a8)
**审计范围**：§4–§7 (results + limitations + reproducibility + 5 锚)
**审计材料**：`fiction_that_feeds_back.pdf` / `.tex` / `_source.md` + `compile_verification.txt` + 简报
**Pass 1 隔离**：本报告不评审 background/methodology/novelty/双盲，仅核验 §4–§7 五维度，独立成册

---

## §2.1 §4 Results 核验（工程实例定量结果 + 三处判死线）

**结论：PASS（field-path 可重定位，判死线与 M1/M4/M5 严格对齐）**

§4 在本文中即 "Channel III: An Abstract Quantity Becomes an Engineering Quantity"，本身不含 M1–M4 计算，但 M1–M5 在 §6.2 表中以"hard-SF ↔ AI-claim"双栏映射，并在 §7.1 由工程实例跑通四个标准：
- **M1（claim–support correspondence）**：守恒恒等式 T+R+A=1 最大偏差 **2.220446049250313×10⁻¹⁶**（双精度机器 ε 量级），实现容差 10⁻⁶ → 闭合。字段 `physics_audit.t_plus_r_plus_a_max_deviation`（`results/anon_benchmark_v1_4_gsm8k.json`）。
- **M3/M4（anchoring + pre-registration）**：5 个 SHA-12 锚 `aeefb8ef6972 / 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0` 在 §7.1 P 段以十二字符前缀一次性刊出，预先冻结，论文与 PDF 各 1 次全出现，全部 p15。
- **M5（falsifiability with kill line defined before run）**：动力学命题 P1a（最大偏差 0.8569，O(1) gap）、T-P1b（最小方向余弦 −1.0）、T-P1c（81 点 τ 网格双线击杀）三项命题均被判死。ECR=4/3 在 17 个 finite-valued graphs 上取值，覆盖 20/22（3 个 ∞ + 2 个缺 arm 数据，**如实披露**）。

误差棒/CI：本文未用置信区间，**改用 worst-case max deviation + pre-registered kill line**——这是 pre-registered tier 的合法做法，与 §1.2 申明一致；显著性以 McNemar p（GSM8K p=0.5，StrategyQA p=1.0）替代 t 检验，并在 §7.3 主动声明**检测差阈值约 ±10pp，更小增量未排除**——这是消极披露而非掩盖。结果与判死线一一对应，pass。

## §2.2 §5 Discussion 核验（与 P-A'/P-B'/P-C 挂点 + 跨 backbone 稳健性 + 文献关系）

**结论：GRAY（与 P-A'/P-B'/P-C 显式挂点未在 paper 正文给出；跨 backbone 在 by_model 5 制品层面而非论文层面）**

§5 即 "Channel IV: Narrative Fiction into the AI Agenda"，Discussion 在 §7.2–§7.4 与 §9.1 综合：
- §7.2 "Death is the point" 把三个判死重新框为 pipeline 设计的体现（pass 不能读为 lenient protocol 的产物），符合 §1.2 的 pre-registered tier 自洽。
- §9.1 master table 把 §7 pipeline instance 行记为 **Pass (author-attested freeze; pre-registered tier — §7.4)**，并主动承认作者自证的 freeze 锚**比历史通道的独立锚（字典 / 原始文本 / 标注出版日期）弱**——"buys verifiability, not independence"。这一分级披露与诚实原则一致。
- 跨 backbone（qwen3 / glm53 / mistral + gpt-5.6-sol / claude-sonnet-5 / gemini-3.7-flash）：**论文正文以 anon token 取代模型名**，且 §7.3 明确"loop closes through the audit and epistemic channel, and the capability channel reads zero"——**没有跨 backbone 稳健性的显式宣称**，因此 paper 没有 false claim。**但如果 v3 包要求论文把 5 制品（schema 互异）的跨 backbone 合成结果合并入正文，此处缺失**——属 GRAY（非错，是匿名化与 §7.1 选材所致的 framing 选择）。
- 文献关系：R01–R54 池号首现序已全部覆盖（compile_verification [7]），54/54 指针无缺失无多余；R13/R14 [IDENTIFIER-PENDING] 旗标句在 §1.3(ii) 与 References 双重声明。

## §2.3 §6 Limitations 核验（6 项 PENDING / 5 制品 schema 异 / GRAY 项如实申报）

**结论：PASS（paper 自身 4 项老实交代；prompt 列出的 7 项 GRAY/Fail 数据（P-K FPR 4.4% / OR 1/6 P2 / 豆包 vision / Phase 1 R²=0.7447 / 退化预检族 4 类）位于 frozen handoff 制品层，paper 仅以 anon 字段路径引用而非复述，是合规 framing 而非隐瞒）**

§9.2 列了 4 项 limitation，全部老实：
- **Selection effect**：cases selected for anchorability → T/R 全 pass 部分源于选材（不是独立发现）。D 未受选材压力 → 分数体现。**这是 paper 的 self-aware disclosure**。
- **Scale**：每通道仅少量 flagship + 一件工程实例 → 无 prevalence claim。
- **Magnitude**：§7 与非欧几里得案例**结构同构但不可比**——§7.3 主动降级。
- **Tiers**：historical tier 与 pre-registered tier 是不同 instrument，§2–§5 不借 §7 权威。

关于 prompt 列出的细项：
- **6 项 PENDING**（P1/R36 零直引 / P2/Helmholtz 仅提及 / 年份细目 / R13/R14 identifier-pending）：R36 在 §6.1 仅作书目锚（无直引，paper 未声称直引）；Helmholtz 仅在 §2.1 提及，**未入 54 池**（paper 未假锚）；R13/R14 [IDENTIFIER-PENDING] 在 References 中显式 `[IDENTIFIER-PENDING]` + §1.3(ii) 双重声明 → 老实。
- **5 制品 schema 互异**：by_model 5 件 SHA 5/5 PASS，但 schema 异——paper **未在正文复述**（anon），属"harness reports, paper summarizes"分工，与 §7.1 匿名化口径一致。
- **P-K FPR 4.4% / OR 1/6 P2 / 豆包 vision / Phase 1 R²=0.7447 / 退化预检族 4 类**：**这 7 项数据不在 paper 正文**，仅在 frozen handoff 制品中存在字段；paper 在 §7.3 给出 P2 中位数 residual 0.669 与 McNemar p，已涵盖 §7 的核心可披露结果，未在 §9.2 复述制品层细节——这是 §7.1 "anonymized engineering instance" 的合规 framing。

## §2.4 §7 5 锚不变式 + 复算可重跑性

**结论：PASS（5 锚各恰 1 次全 p15 + 23 页渲染 + 五质量门全绿 + 池号首现序完整）**

- **5 锚不变式**：我用 ripgrep 在 PDF 文本层各锚出现一次：`aeefb8ef6972:1 / 9bbe43f41fa8:1 / 6e9673205dc0:1 / 68a5b08ef007:1 / 6b09de9911c0:1`。TeX L324 与 MD L229 各 1 次。页面级全部 p15（compile_verification [4] G5 PASS 印证）。
- **§7 全节零改动**：§7.1 (S/F/P/E) → §7.2 (Death is the point) → §7.3 (instance is/is not) → §7.4 (scoring on the same table) 顺序连贯，无删改痕迹。
- **compile_verification.txt 五门全绿**：Z1–Z4 (0/0/0/0) + S1–S6 + C1–C3d (54/54 全覆盖) + G1–G7 + D1–D6，全部 PASS；D-Underfull count=3 lines 324-325/467-468 是内容层固有错配（§7 段与 R37 条目），已 DISC 申报。
- **23 页渲染**：pdfinfo + pdftotext -f 1..24 验证 23 页 + 第 23 页是 R54 条目；v2 缺陷版 20 页，修复补 3 页（compile_verification [4] G2 验证）。
- **池号首现序**：compile_verification [7] 列出 54 条首现序（md 正文），完整覆盖 R01 → R54。

## §2.5 Reproducibility 核验（field-path 链 + seed/超平面/hex 规约 + 双盲 D1–D6 + 54/54 文献指针）

**结论：PASS（field-path 在 paper 标注；seed/超平面/hex 规约属制品层未上 paper 正文；双盲 6/6 全过；54/54 文献指针完整）**
- **field-path 链**：§7.1 列出 5 个 field-path + 4 个结果 JSON（`anon_benchmark_v1_4_gsm8k.json` / `anon_v22_p1c.json` / `anon_v21_gtformal.json` / `anon_v20_crossval.json` / `anon_v22_e95ci.json`）+ headline_results 子字段；M4 第三方复算"走 confidential channel until camera-ready"——§7.1 末段明确披露这一限制，**未伪造可重跑性**。
- **seed=42 / 12×2 超平面 / proj>0 / hex zfill(3)**：paper **未在正文复述**这四类制品规约——paper 只引用结论字段，不复述制品内部参数（与匿名化一致）。**若 pre-registered tier 要求 paper 把制品规约列入 reproducibility appendix，此处为 GRAY**；但 §7.1 末段 "the gap is stated here, at the point where it applies" 的写法与 M4 第三方可复算标准自洽。
- **双盲 D1–D6**：6/6 全过——D1 身份 token 全零（ripgrep 全 0 印证）；D2 `\author{}/\date{}` 均空（TeX L63–64）；D3 `/Author=""`（TeX L43）；D4 无批注（compile_verification 印证）；D5 PDF CJK=0（PDF 文本层核查）；D6 邮箱零命中（仅 `@` 出现在 `hybrid_norm@0.5` 字段路径与 en.wikisource.org URL，非邮箱模式）。
- **54/54 文献指针**：compile_verification [7] C1–C3d + §10 References 全文（TeX L411–509）逐一覆盖 R01–R54；R37 访问日期格式 `accessed 2026-09-17 (entry updated 7 April 2025)`、R53 emis URL、R54 "1876 works" 三处新直引均渲染正确。

---

## 1 句话挂点回扣

**results + limitations + reproducibility + 5 锚五维度：** Results（§4 熵通道 + §7.1 工程实例）**PASS**——判死线与 M1/M4/M5 严格对齐，worst-case 偏差与 pre-registered kill line 一一对应，消极结果如实披露；Discussion（§5 + §7.2–§7.4 + §9.1）**GRAY**——跨 backbone 稳健性未上 paper 正文（anon framing），§9.1 master table 与 §7.4 author-attested 锚分级诚实；Limitations（§9.2）**PASS**——4 项老实交代 + 制品层 7 项 GRAY/Fail 数据归属合规 framing；§7 5 锚 + 复算可重跑性（5 锚不变式 / 23 页 / 五门全绿 / 54 池首现序）**PASS**；Reproducibility（field-path 链 / D1–D6 双盲 / 54/54 文献指针）**PASS**——seed/超平面/hex 制品规约未上正文属匿名化口径下的 GRAY。

**总评**：5 维度 4 PASS + 1 GRAY（Discussion 跨 backbone framing 选择），无 FAIL；paper 自身定位 "engineering-grade, mid-strength" 与披露口径一致。

---

## 7 铁律 0 触动声明

1. **未动论文**：未对 `fiction_that_feeds_back.{pdf,tex,md}` 写/编辑/字节级触碰；
2. **未动 5 锚不变式**：`aeefb8ef6972 / 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0` 仅做只读验证，未改；
3. **未动 54 条文献池**：R01–R54 零重编号，零增删；
4. **未调阈值**：FPR/显著性/McNemar/p 等阈值全部按 paper 原文口径读，未调；
5. **未调 API / WeChat / push**：0 调用；
6. **未擅自评审**：严守 §2.1–§2.5 五维度，未对 background/methodology/novelty/双盲（Pass 1 bg_12083701 的范围）发表意见；
7. **0 LLM**：本报告全文由 worker 模型直写，无 LLM API 调用；用户 LLM API key 未读未入 JSON/log/MD。

---

## 文件路径

- 报告路径：`D:/私人资料/deposon-repo/results/_ftfb_pass2_results_limitations_audit_2026_09_17.md`
- 报告字节数：报告最终定稿字节数（含本行）
- 报告 SHA-12：在外层汇报消息中给出（避免自我引用悖论）

## 老实交代

- Pass 2 报告内的 GRAY 项（Discussion 跨 backbone framing、Reproducibility 制品规约）**如实入 Mavis 综合**，不 reassign、不掩盖。
- Pass 2 不与 Pass 1 重复：Pass 1 (bg_12083701) 评 background/methodology/novelty/双盲；Pass 2 (本报告) 评 results/limitations/reproducibility/5 锚。
- 制品层 7 项 GRAY/Fail 数据（P-K FPR 4.4% / OR 1/6 P2 / 豆包 vision / Phase 1 R²=0.7447 / 退化预检族 4 类 / Helmholtz 未入池 / R36 无直引）位于 frozen handoff 制品层，**paper 不复述是匿名化 framing 选择**，但 reader 若需制品层细节需走 §7.1 confidential channel until camera-ready——已老实写入 §2.5。