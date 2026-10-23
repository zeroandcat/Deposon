# arXiv 投稿过载与限投传闻核实＋我方影响评估

**执行**：阿兰-文献调研员（管理员 2026-10-15 10:49 派单）
**查证时点**：2026-10-15 10:50–10:58（北京时间），全部一手页面直读
**留档**：agents/6a962cc259312f271f3f1e71/arxiv_check_2026_10_15/（s01–s05 检索、p01–p05 页面快照）

---

## 一、核实结论：传闻属实，有官方书面来源

PI 10:48 所述「arXiv 被海量投稿搞得崩溃、以至于限制投稿了」——**核心事实成立，定性需修正**：

1. **限投属实**：arXiv 官方博客 2026-10-01 发布《Fair Moderation, Equitable Access, and AI: arXiv's Updated Rate Limit Policy》（作者 Kat Boboris，发布 10-01 15:00 EDT，页面 10-09 有过修订），明文更新全站限投政策。
2. **海量投稿属实**：官方数据——2026 年 9 月单月收到 **40,363 份投稿**（历史新高），引发近 **9,000 张 support tickets**；对比 2016-09 为 9,869、2024-09 为 20,569，**两年翻倍**；cs.AI 类两年增幅超 6 倍。
3. **「崩溃」定性不确**：官方未称系统宕机；官方定性为 "watershed moment"，症结是**志愿审核（moderation）容量被低质量投稿挤占**（thin papers、salami 拆分投稿、AI 密集写作论文），政策定位为 **stopgap（临时过渡措施）**，官方称将持续监测并按需调整。PI 体感的 on hold 延迟正是该容量紧张的下游表现，**属当前背景下的预期现象，不指向我方稿件本身有问题**。

## 二、限制条款（官方公告原文口径）

| 条款 | 内容 | 备注 |
|---|---|---|
| 生效时点 | **2026-10-01 起** | 覆盖所有提交者、所有类别 |
| 月度限额 | 每提交者每**日历月最多 2 份新投稿** | 新政主体 |
| 在途限额 | 任一时刻最多 **3 份 active submissions** | **2024 年起即有的既有限额**，维持不变 |
| 拒稿计数 | **计入**月度配额（"this rate limit is for submissions, not announced papers, because it is submissions that consume moderator time"） | |
| 跨月 on hold | 上月投稿下月仍 on hold：**不计入下月配额**，但**计入 3-active** | 与我方现状直接相关 |
| 宣布前删除 | **不计入**月度与 active 配额 | |
| 计数主体 | 只计 submitter 本人，合作者不占配额 | |

## 三、「限新投稿」vs「更新既有提交」——任务重点区分

1. **公告限额条款明文只针对「submissions（新投稿）」**：公告全文与 FAQ 的计数场景（拒稿、跨月 hold、宣布前删除、代投）全部围绕新投稿展开，**未出现将 replace/更新纳入 2/月限额的条款**。
2. **官方帮助页《Submit a new version of a work》（info.arxiv.org/help/replace.html，今日现读）维持既有口径未变**："We ask that articles be replaced no more than once per week. After version 5 replacements are limited to no more than once per week."——replace 的节奏规则仍是「每周一次」，未叠加月度限额。
3. **但官方尚未书面澄清 replace 是否计入月度配额**：公告评论区多位作者 10-02 追问（如 GABRIEL ISTRATE "What about NEW VERSIONS of an already-published paper? Do they count towards the monthly limit as well?"、TTTT "How about replacements of existing articles? Do they count?"），**截至查证时点未见 arXiv 官方回复**。
4. **诚实登记**：「replace/更新不受 2/月新投稿限额约束」是基于公告条款文义＋replace 帮助页现状的**合理推断，非官方明示**。政策理由（限的是消耗 moderator 时间的新投稿）支持该推断，但若后续官方出补充澄清，须回访。
5. **注意：限额豁免 ≠ 延迟豁免**。官方状态页（help/submit_status.html）明确："A new submission **or an update to an article (replacement, cross list, journal reference or DOI addition, or withdrawal)** may traverse several status values"——更新/replace 同样要过 moderation 队列、同样可能 on hold。

## 四、on hold 延迟的官方口径（与我方现状直接相关）

- 状态页原文："Due to the large volume of submissions the process **may take several days**. We appreciate your patience."
- 公告中 arXiv 编辑咨询委员会主席 Thomas Dietterich（Oregon State University）引语：高质量论文 "can be **delayed for days or weeks** as a result"（被低质量投稿挤占 moderator 时间所致）。
- **官方明确禁忌**："Please do not make a duplicate submission while your work is on hold. **Deleting and resubmitting your work will lead to further delays.**"（on hold 期间勿重复投稿、勿删除重投）
- On hold submissions will not expire（不会过期失效）。

## 五、我方两条在案动作影响评估

### ① MOD-108421 修复包上传（仪表板「更新→添加文件」路径）

- **配额影响：不受 2/月新投稿限额约束**——该路径是对既有在途 submission 的 update/add files，不产生新 submission（推断属性见 §三.4，已标注）。
- **该动作本身恰是官方认可的合规路径**：官方明确 on hold 期间应通过 user page 更新在途稿件、勿删除重投——我方「更新→添加文件」与此吻合。
- **延迟影响：存在**——上传后稿件仍须待 moderation 解除 hold，当前过载背景下解除周期官方口径为「数天」至「数周」（Dietterich 引语）。另注意：更新会重置 14 天过期计时，且 on hold 件不过期，无丢件风险。
- **应对口径：照常执行，无需择窗等待**。政策 10-01 已生效，我方 v9 已在队列中，等待只会更晚；上传后按官方口径静待，不做重复动作。
- 操作细节（帮助页）：工作日 14:00 US Eastern（北京次日凌晨 02:00）前完成编辑不影响当日版本戳与公告节奏——若在意时点，建议 PI 在工作日美东 14:00 前完成上传。

### ② 下一版轮（实验侧更新到位后）

- **若 v9 届时已 announce**：走 replace 路径，遵守既有「每周不超过 1 次」规则即可；月度限额未见叠加（推断属性同上）。
- **若 v9 届时仍在 hold**：优先考虑**并入在途 update 打包**（一次更新打包到位，减少重复排队），继续避免删除重投。
- **3-active 限额**：我方在途仅此 1 件，无约束。
- **2/月新投稿配额**：对本版轮无影响（版本更新非新投稿）；即便未来有全新论文投稿，v9 提交（10-13 前后，MOD-108421 链为参照）在新政生效后仅占 10 月配额 1/2，余量充足。
- **应对口径：择窗而非等待**——以实验侧就绪为准，不受限投政策实质约束；仅公告节奏（周中 14:00 ET 规则、节假日公告调整，如 10-08 官方曾发 Labor Day/秋季假期公告节奏调整通知）需在排期时顺带注意。

## 六、来源清单（全部一手直读）

| # | 来源 | 时点 |
|---|---|---|
| 1 | arXiv 官方博客《Fair Moderation, Equitable Access, and AI: arXiv's Updated Rate Limit Policy》 blog.arxiv.org/2026/10/01/updated-rate-limit-policy | 发布 2026-10-01 15:00 EDT；本人直读 2026-10-15 10:5x（北京时间） |
| 2 | arXiv 帮助页《Submission Overview》 info.arxiv.org/help/submit/index.html | 直读 2026-10-15 |
| 3 | arXiv 帮助页《Submit a new version of a work》 info.arxiv.org/help/replace.html | 直读 2026-10-15 |
| 4 | arXiv 帮助页《Status Information》（含 On Hold 节） info.arxiv.org/help/submit_status.html | 直读 2026-10-15 |
| 5 | 旁证（非官方，仅 corroborate）：Terry Tao 博客 10-01 转载评述、mlq.ai 10-12 报道、Reddit r/math 讨论串、HN 讨论串 | 检索 2026-10-15 |

## 七、一句话结论

**传闻属实且已有官方书面来源（10-01 博客公告）：新投稿限 2/日历月＋同时 3-active（后者 2024 年既有）；我方两条动作（仪表板更新上传、下一版轮）均非新投稿路径，不受月度限额实质约束，可照常/择窗执行；但 moderation 队列过载导致的 on hold 延迟（数天至数周）是真实的、会波及更新件，属预期现象，静待即可、切勿删除重投。**
