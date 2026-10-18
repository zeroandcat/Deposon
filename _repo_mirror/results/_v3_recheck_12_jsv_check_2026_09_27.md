# V3-R #12 补审 (b) 专项 · Jordan-Sucher-Votek 1999 相图联网调取核验件（check）

> **性质**：`results/_v3_recheck_prereg_v1_2026_09_27.md` §1.2 #12(b) 字面要求的 **JSV 1999 专项对照**的联网调取结果；**V3 原报告与 #12 三件套全部 byte 0 触动**，本件**并列**登记
> **配套件**：`results/_v3_recheck_12_jsv_phase_data_2026_09_27.json`（检索留痕 + 核验明细）
> **授权**：PI 2026-09-27 问卷 `ask_421d7df4aa0929633c265c47` Q3「授权联网」；**联网仅限检索/调取公开文献数值**
> **PI 复核栏**：待 PI 签字生效即锁

---

## 0. 一句话结论

**「Jordan-Sucher-Votek 1999」查无**（3 个独立权威索引 21 次检索，姓氏 **Votek** 在 Crossref 与 OpenAlex 作者索引中**完全不存在**）。⇒ **(b) 专项对照无法按预登记字面执行；本件 0 编造任何 JSV 数值**；#12 主判定（真相界 FAIL / 维持「假成立」）**不变**。

---

## 1. 文献核验结论

| 项 | 结论 |
|---|---|
| 引文原字面 | `Jordan-Sucher-Votek 1999` |
| **核验判定** | **查无（NOT_FOUND）** —— 疑似误记或虚构；**不可判定为任何真实文献的拼写变体** |
| 真实存在？ | **否** |
| 拼写变体？ | **否** —— 4 条变体假设（Sucher→Schuch、Votek→Vojta、Sucher 为 Jordan 转写误差、Votek 为 Votrubá 类斯洛伐克语拼写）**全部 0 产出** |
| JSV 相图数值 | **无（null）**；本件 0 编造 |
| 是否拿相似文献冒充 JSV | **否**（见 §3） |

### 1.1 核心证据（姓氏级否定，可复核）

| # | 索引 | 查询 | 实测返回 | 权重 |
|---|---|---|---|---|
| E1 | Crossref | `works?query.author=Votek` | `total-results = 0` | **核心** |
| E2 | Crossref | `works?query.bibliographic=Votek` | `total-results = 0` | **核心** |
| E3 | OpenAlex | `authors?search=Votek` | `meta.count = 0`（空数组） | **核心** |
| E4 | arXiv | `all:Votek` | `totalResults = 0` | **核心** |
| E5 | arXiv | `all:"transverse field Ising" AND au:Votek` | `totalResults = 0` | 佐证 |
| E6 | arXiv | `au:"Sucher" AND abs:"Ising"` | `totalResults = 0` | 佐证 |
| E7 | Crossref | `query.author=Jordan+Sucher+Votek`，窗口 1998-01-01…2000-12-31 | 该三人组合 0 命中 | 佐证 |
| E8 | OpenAlex | `works?search=Jordan Sucher Votek` | `count = 13`，top-5 全为无关文献（in-context learning / 公司治理 / LLM 综述） | 佐证 |
| E9 | OpenAlex | `works?filter=publication_year:1999&search=transverse Ising chain critical line phase diagram` | `count = 21`，无 Jordan/Schuch/Vojta 署名者 | 佐证 |
| E10 | OpenAlex | `authors?search=Sucher` | `count = 130`；top-5 = Nikolaus J. / Joseph / Robert / Kathryn P. / Joseph F. Sucher，**领域为数学教育、QED 多体、医学**，无一为横场 Ising | 反向界定 |

**读法**：**Sucher 是真姓氏**（E10），但**Votek 在两个作者级索引中计数为 0**（E1/E3）—— 三人组合中只要「Votek」不成立，引文即不成立。arXiv 全库 `all:Votek` 亦为 0（E4），排除「索引遗漏作者字段」这一反驳。

### 1.2 方法学自保（不采信反证）

检索中 2 次 DOI 直查返回 "Resource not found"（`10.1103/PhysRevB.60.730`），**本件明确不将其计入证据** —— 已用对照探针（`10.1007/978-3-540-49865-0_2` 直查 OK）证明端点本身有效，失败归因于 **Crossref/APS DOI 大小写敏感性未排除**（OpenAlex 侧实测同一 DOI 记为小写 `10.1103/physrevb.…`）。**把不成立的探针拿来说事 = 误导，主动剔除。**

### 1.3 检索失败项（如实登记，0 粉饰）

| 端点 | 结果 |
|---|---|
| `html.duckduckgo.com` | network request failed |
| `www.mojeek.com` | HTTP 403 反自动化拦截 |
| `search.marcia.cc`（searx 公共实例） | 域已停放售卖，实例不可用 |
| `api.semanticscholar.org` | HTTP 429（无 key 限流），2 次均失败 |

**影响评估（如实）**：4 类通用搜索引擎/聚合器失败，**但本次判定的 4 条核心证据全部来自 3 个作者级/文献级权威结构化 API（Crossref / arXiv / OpenAlex），未依赖任何通用搜索引擎** ⇒ 失败项**不削弱**查无判定。通用引擎侧留痕为「未取得」，**0 记作「0 命中」**。

---

## 2. (b) 专项对照执行结果

| 项 | 结果 |
|---|---|
| 预登记字面要求 | §1.2 #12(b)：「`transverse_ising_region` 用真 phase boundary 测试（**沿 Jordan-Sucher-Votek 1999 数值解** + per-model empirical 散点）」 |
| 实际可执行性 | **不可执行** —— 所指定数值解**不存在** |
| 是否用替代数值补跑 | **否**（PI 授权字面是「调取该文献数值」；该文献查无 ⇒ 无可调取之物 ⇒ 按派工单 §3.3「若查无 → 该件只登记『查无/γ 注记』，**0 编造数值**」） |
| 是否重跑 #12 判据 | **否** —— 见 §4，#12 主判定不依赖 JSV 数值，重跑不会改变任何输入或结论（诚实交代：非「跑了发现不变」，而是**判定链路本就不经此变量**，故不浪费一次实跑） |
| 本 (b) 专项 | **登记为「查无 + 溯源失效（J-1）」，0 数值** |

---

## 3. 最接近的真实文献（**均非 JSV 1999**，仅供 PI 拍板时选择）

> **本件 0 将以下任何一条当作 JSV 1999，0 用其数值参与任何判定。** 三条均经 Crossref 实测存在（DOI 逐字给出）。

| # | 引文 | DOI | 核验 | 数值是否已调取 |
|---|---|---|---|---|
| C1 | **Pfeuty, P. (1970). The one-dimensional Ising model with a transverse field. Ann. Phys. 57(1), 79–90.** | `10.1016/0003-4916(70)90270-8` | Crossref 直查 **OK**（Elsevier；被引 1542） | **否**（仅书目元数据） |
| C2 | **Chakrabarti, B. K.; Dutta, A.; Sen, P. (1996). Quantum Ising Phases and Transitions in Transverse Ising Models. LNP Monographs. Springer.** | `10.1007/978-3-540-49865-0` | Crossref 直查 **OK**（被引 220） | **否**（仅书目元数据） |
| C3 | Lieb, E.; Schultz, T.; Mattis, D. (1961). Ann. Phys. 16, 407. | `10.1016/0003-4916(61)90115-4` | **间接**（DOI 于 C1 参考文献列表中实测出现，未单独直查） | **否** |

**口径要点（如实标出）**：

- **C1 就是本仓 V3 早已冻结的引用** —— `boss_pc_2_transverse_field_ising.py:30` `PFEUTY_H_C_OVER_J = 1.0  # 1D chain Pfeuty 严格解 h_c/J = 1`，PE-2 JSON `note` 亦只写「h_c(T) 为 Pfeuty 1D chain 简化」。**JSV 与 Pfeuty 是两条独立字面**，二者不可互换冒充。
- **C2 的章节对口**（均为 Crossref 直查所得）：`_2` Transverse Ising Chain (Pure System), pp. 17–49｜`_3` Transverse Ising System in Higher Dimensions (Pure Systems), pp. 50–67｜`_5` Dilute and Random Transverse Ising Systems, pp. 99–117。**若 PI 要一条真正可调取相图数值的来源，C2 是本次检索中最对口的真实对象。**
- **本件 0 取得上述任何一篇的正文/数值表**（Elsevier / Springer 全文需另行授权）。**0 声称已调取其相图数值。**

---

## 4. 与 #12 主判定的一致性检查

### 4.1 结论：一致，**#12 主判定不变**

| 项 | 值 |
|---|---|
| #12 主判定 | **FAIL（K-V3R-12 不一致分支）· 维持「假成立」· 真相界 outside(>0.15) = 0/9** |
| JSV 查无是否改变该判定 | **否** |
| 理由 | #12 真相界来自**自实现 1D 精确临界线** `sinh(2K)sinh(2Γ)=1`（闭式 vs 二分最大偏差 **4.441e-16**，残差 ≤ **2.220e-16**，7/7 自校验通过），**判定链路完全不经 JSV 变量** |

### 4.2 查无的净效应：**加强**（非削弱）

#12 原 PASS 的死因（硬编码常量 `0.5` × 量纲错配相减）本已**独立成立**；JSV 查无进一步证明：**原标注所依赖的「相界对照文献链」在文献层面亦为悬空**。⇒ 假成立标注的证据基础更厚，**0 改判「真成立」**。

### 4.3 ⚠ 必须诚实标出的局限（不掩盖）

**#12 rescript §3.1 所引 1D 精确临界「方程」本身，本次未取得逐字文献出处。** C1/C2 均只取得书目元数据、**未取正文**。该方程目前仍只靠 ①#12 自身数值自校验 与 ②常规教科书结论 支撑，**其文献级引用仍是待补项**。

**⇒ 本件不宣称「已用真实文献核验了 1D 临界方程」；只宣称「核验了 JSV 1999 查无」。**

---

## 5. γ / 补审发现登记

| 项 | 内容 |
|---|---|
| **J-1（文献溯源 · PREROG-PROVENANCE 失效）** | **「Jordan-Sucher-Votek 1999」在 V3 源件中根本不存在，其在盘上的首次出现就是预登记件本身。** 实测：①`boss_pe_2_real_transverse_ising_2026_09_15.json` **无 `reference` 字段**、spec_source 指向内部 spec 文件、全文 0 处 JSV；②`deposon_team/plugins/boss_pc_2_transverse_field_ising.py` 只引 Pfeuty、全文 0 处 JSV；③全仓 9 处 JSV **全部**落在 V3-R 派生物（prereg v1 + #12 三件套）。**连带发现**：预登记自称「…**沿 V3 既引**」与「沿 V3 JSON `reference` / `spec_source` 字面，不另引」两处**溯源声明与盘上事实不符**。**⇒ 预登记 §1.2 #12(b) 的构造要求自始不可满足，这是 K-V3R-12 补审构造层面的一处独立缺陷**；#12 rescript 仅登记为「缺件」（γ₂「0 命中/0 联网」），**未识别其溯源本身即失效**，本件据实升级登记 |
| **J-2** | 2 次 DOI 直查失败（大小写敏感性）**主动剔除、不计入证据**；用对照探针证明端点有效后再剔除，**不拿不成立的探针说事** |
| **J-3** | 4 类通用搜索引擎/聚合器检索失败（DDG 网络失败 / Mojeek 403 / searx 域停放 / Semantic Scholar 429）如实登记；**判定的 4 条核心证据全部来自 3 个结构化权威 API，未依赖通用引擎** ⇒ 失败项不削弱判定，但通用引擎侧**记为「未取得」而非「0 命中」** |
| **J-4** | 本件**0 冒充**、**0 拿相似文献顶替** JSV；C1/C2/C3 全部显式标注「**非 JSV 1999**」且 0 参与任何判定 |
| **J-5（局限）** | #12 §3.1 的 1D 临界**方程**文献级引用**仍缺**（本次仅得书目元数据，未得正文）——**待 PI 另行授权全文调取或直接提供** |
| 既有件触动 | **0** —— prereg v1、#12 三件套、V3 原报告全部 byte 0 触动；0 代为修订，派生 JSON 0 合并 |
| 是否翻案 | **否** —— 本件只登记文献核验结果与溯源缺陷，**不重裁 #12 判定** |

---

## 6. 老实交代段

1. **0 编造**：JSV 相图数值 0 编造；**0 拿相似文献冒充 JSV**。查无即报查无。
2. **联网动作清单（全量，21 次 GET，0 注册 0 登录 0 提交表单）**：
   - Crossref ×11：`query.bibliographic`(JSV) / `query.author=Votek` / `query.bibliographic=Votek` / `query.author=Jordan+Sucher+Votek`(1998-2000) / `works/<DOI>` 直查 ×3（Pfeuty 1970 ✓、Chakrabarti-Dutta-Sen 1996 ✓、对照探针 ✓）/ `filter=doi:` ×1 / 2 次 DOI 直查失败（已剔除）
   - arXiv ×4：`all:Votek` / `all:"transverse field Ising" AND au:Votek` / `au:"Sucher" AND abs:"Ising"` / `au:"Schuch" AND au:"Vojta"`
   - OpenAlex ×4：`authors?search=Votek` / `authors?search=Sucher` / `works?search=Jordan Sucher Votek` / `works?filter=publication_year:1999&search=transverse Ising chain critical line phase diagram`
   - 失败 4 类：DDG html（network failed）、Mojeek（403）、searx marcia.cc（域停放）、Semantic Scholar（429 ×2）
   - **0 teamorouter / 0 openrouter / 0 LLM API 调用 ⇒ 0 代理需求**（PI「teamorouter/openrouter 必走 tun」口径本次**不触发**）；0 key 出现、0 明文密钥
3. **skill**：`@scientific-research-workflows` / `experimental-design`，**已加载、未 fallback** —— 首查 `.minimax\plugins`（空目录）与 `.minimax\skills`（223 项无此项）均 0 命中，经 **plugin-cache** 定位到
   `C:\Users\Administrator\.minimax\v2\plugin-cache\official\sha256-tree-v1-611965fcb6…\skills\experimental-design\SKILL.md`（13,044 B），实测 **SHA-12 `0a314eed103a`**，与 #12 rescript 所记逐字一致。**0 编造 skill 指令**。适用面：区组 = 9 model、伪重复声明沿 #12 既有字面；本件 0 新增处理格 / 0 新阈值 / 0 新 seed。
4. **0 擅调阈值**：`PFEUTY_H_C_OVER_J=1.0` / `TOL_STRICT=0.05` / `TOL_LOOSE=0.15` / `D_FIX2_*` 全部沿既有字面，**本件一字未动**（本件根本未重跑判据，见 §2）。
5. **不掩盖对自己不利的读数**：J-5 如实标出 **#12 的 1D 临界方程文献级引用本次仍未补上**；C1/C2 **仅得元数据、未得正文**。
6. **主动剔除反证**：J-2 —— 2 次 DOI 查无被自己查出是大小写问题，**不计证据**。
7. **派生 JSON 0 合并**：本件 2 件为**新增并列件**，与 #12 三件套 0 合并、0 覆盖。

---

## 7. 留 PI 拍板（本件不自决）

1. **是否把 §1.2 #12(b) 的字面要求（JSV 1999）正式改挂？** 三选项：(a) 记为**构造缺陷**（本件 J-1 已给出证据），(b) 改挂 **C1 Pfeuty 1970**（V3 早已冻结的同一文献，语义自洽），(c) 改挂 **C2 Chakrabarti-Dutta-Sen 1996 Ch.1/3**（含可调取相图），或 (d) **撤除该字面要求**（因自始不可满足）。
2. **是否授权全文调取**（Elsevier TDM / Springer PDF）以补上 **J-5**（1D 临界方程的文献级出处）？本件仅得书目元数据。
3. **是否授权由 PI 直接提供该相图**（#12 rescript 原文列的第三选项）。

---

**PI 复核栏**：☐ 通过（登记「查无 + J-1 溯源失效」，#12 判定不变）　☐ 打回（要求补充检索源 / 全文授权 / PI 直接提供相图）　签字：__________　日期：__________

---

## 8. 落盘件实测（SHA-12 = `hashlib.sha256(file_bytes).hexdigest()[:12]`，小写）

| 件 | 字节 | SHA-12 |
|---|---|---|
| `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | 17,718 | `642582d4fbd1` |
| `results/_v3_recheck_12_jsv_check_2026_09_27.md`（本件） | 见派工回报 | **自哈希不可内含**（写进去即改自身哈希，自指悖论；实测值由 worker 落盘后在派工回报中给出，不在本件内自封） |

**既有件 0 触动实测**（值与 #12 rescript 所记逐字一致）：`_v3_recheck_prereg_v1_2026_09_27.md` 37,346 B / `88052d7db895`；`boss_pe_2_real_transverse_ising_2026_09_15.json` 3,553 B / `8933d61b180a`。**两件 key 形态自扫 0 命中。**

---

**出证｜Mavis 团队 worker 出件｜2026-09-27**


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L136,137（出现 3 处）· `experimental-design` 已加载未 fallback（绝对路径 + SHA-12 + 字节）
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、`SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：scientific-research-workflows:experimental-design` · 树 ``611965fcb620`` · ``SKILL.md`` SHA-12 ``0a314eed103a`` / 13,044 B（实体直读；运行时加载行为见执行件 §6，**本棒 0 复现**）
> - **「历史实测 vs 今日实测」口径**：本件所记为**当时实测证据**，**保留有效、0 回改**；今日复核值以本附注与执行件为准，读者可据此区分二者（起因件建议 A2）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**