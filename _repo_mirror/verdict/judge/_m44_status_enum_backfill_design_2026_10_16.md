# M-44-A-ENUM-BACKFILL ｜ ①段·「5 锚 JSON 之 status 合法枚举」**枚举复测面 ＋ 甲型 schema 回填设计面**（**候 PI 核准** · ⛔ 0 径行采认 · ⛔ 0 直接入锁 · ⛔ 0 改任何既有件一字）

> 棒 ID：`M-44-A-ENUM-BACKFILL`｜夜间接力续棒（PI 令「静默续棒」）｜署名：**protocol-keeper**（口径/schema 设计专官）｜日期：2026-10-16｜工作区：`_repo_mirror`
>
> **性质**：**枚举复测（测量面）＋ 纯设计件**。本件 ⛔ **0 改动**任何既有件一字（含 `verifier/handoff/` 下全部锚件）、⛔ **0 入锁**任何 schema、⛔ **0 采认**任何推断值、⛔ **0 代** PI 裁/释/择/给值、⛔ **0 网络**（本棒纯本地）。全部产出**标「候 PI 核准」**。
>
> **FTFB 时序自证**：枚举测量面（§2）**全部**先于设计面（§3）落笔落盘——测量面终版扫描完成时点 **2026-10-16T08:43:11.660580+00:00**（UTC，见 §2-1 之 `scan_ts_utc`）**早于**设计面文本定稿与本件落盘；设计面所载之 `anchor_status`／`status_detail` 定义、取值登记域、既有值归置、迁移纪律，其每一项均可回溯至 §2 之实测数据，⛔ **0 先写结论后凑数据**。

---

## §1 背景、授权与输入件实测指纹

### §1-1 授权链（本棒之由来 · 逐字回读）

| 层 | 逐字依据 | 出处（本棒实测行号） |
| :-- | :-- | :-- |
| 事起 | M-44＝「5 锚 JSON 之 `status` 合法枚举」列 B 类联网取证面 | `_pi_give_b_class_retrieval_2026_10_14.md` §2 B 类表（`:55`） |
| 事实基座更正 | 「在盘锚 JSON `03c6c01f3697` **实无 `status` 字段**（5 锚字段集 `{object, path, algorithm, value, field}`）；既有登记所称之「5 锚 JSON 之 `status`」实为 `0a031a9795a9` §3-5 之**草拟 schema** 与两件判断件**自填**之 `anchor_status`（值 `drift_authorized`）；全库实测 `status`／`verdict`／`state` 共 **44** 种值 ⇒ 现为**开集**」 | 同上 §3-4（`:139`–`:142`）＋ §5-1 `KD-3`（`:204`） |
| PI 裁（型） | **「按推荐档打包过（推荐）」**（选项 id `q1_90353e85_opt1`）—— 题面摘要逐字含「`【推】M-44 采甲型（44 值映射未处置，径采闭集将致 44 件失配）」；甲型＝**开集字符串＋`status_detail`**；乙型＝闭集枚举（⚠ 须先处置既有 44 值映射） | `_pi_card_answers_register_2026_10_14_v7.md` §1 Q1（`:19`） |
| PI 裁（派棒） | **「项25采信（豁免H8）＋项26派棒＋项27知悉」**（选项 id `q4_64b21b38_opt2`）；登记注记逐字「**项26 派棒**（M-08 实测枚举择优／M-41 剔 vs 不剔双读数对照实验／**M-44 实测枚举后回填**——三支棒获准派出，原「⛔ 0 派 ⛔ 0 代跑」之禁令由 PI 本裁解除）」 | 同上 §1 Q4（`:36`）＋ §2 派生动作 B（`:47`） |

> 声明：本棒之「甲型」采 PI 已裁之**字面**（开集字符串＋`status_detail`），⛔ **0 重开**型之择（乙型已被 PI 否，本棒 ⛔ 0 复提乙型、⛔ 0 径采闭集）；本棒 ⛔ 0 将「设计」当「入锁」。

### §1-2 输入件实测指纹（本棒逐件 `sha256(b)[:12]` 复算 · ⛔ 0 沿用他件自报值）

| SHA-12（本棒实测） | bytes | mtime | 件名（`results/`／`verifier/handoff/`） | 本棒用其何面 |
| :-: | --: | :-: | :-- | :-- |
| `74e25d75d59d` | 31,463 | 2026-10-14 01:57:09 | `results/_pi_give_b_class_retrieval_2026_10_14.md` | §1-1 之事实基座与 `KD-3`；§2-4 之 44 值对照基准 |
| `d114b7576b78` | 5,851 | 2026-10-14 22:12:13 | `results/_pi_card_answers_register_2026_10_14_v7.md` | §1-1 之 PI 裁（型／派棒）逐字 |
| `36f70c0a844c` | 28,728 | 2026-10-14 00:12:17 | `results/_batch7_deliberation_judgment_2026_10_13.md` | `KD-6`（`:187`）所指出之 `status` 枚举未定义（转引自取证件 `:19`，**本棒未逐字回读其正文**） |
| `a68b2971b8e1` | 49,012 | 2026-10-14 00:52:01 | `results/_batch8_deliberation_judgment_2026_10_14.md` | `anchor_status` 自填出处（转引自取证件 `:20`，**本棒未逐字回读其正文**） |
| `03c6c01f3697` | 6,680 | 2026-09-09 13:19:32 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | §4 之**在盘现版 KT 锚件**字段集实测 |
| `c4f029f780d8` | 7,796 | 2026-10-15 09:53:17 | `verifier/handoff/P_A_V0_anchors_sha256_12.json` | §4 之**最新在盘锚件**（按 mtime 末位） |
| `0c269b9558da` | 35,911 | 2026-10-15 13:00:07 | `results/_ge01_prereg_5anchor_v3.json` | §4 之 GE01 预注册锚件 v3（v2/v3 迭代之实证） |
| `f06313373fc6` | 21,629 | 2026-10-15 11:21:14 | `results/_ge01_prereg_5anchor_v2.json` | §4 迭代替换链之中间版 |
| `4b020eb04605` | 10,701 | 2026-10-14 17:52:13 | `results/_ge01_prereg_5anchor.json` | §4 迭代替换链之 v1 |
| `c43a84c70935` | 16,043 | 2026-10-16 11:42:27 | `results/_pa_harness_anchor_value_update_v2.json` | §2-5 之 `anchor_status` 全库唯一定位与取值实测 |

> 断言：上列 **10/10** 件本棒以 `sha256(b)[:12]` 逐件复算并实测 bytes 与 mtime；其中 `03c6c01f3697`／`36f70c0a844c`／`a68b2971b8e1` 与取证件 §1-1 所载自报值**逐位相符**（`74e25d75d59d` 与派工 briefing 之 `5b9478c7e86b` **不符**，见 §5 `KD-4`）。
> 逐字回读声明：本棒**逐字回读** `74e25d75d59d`（全文，`:19`／`:36`–`:47`／`:127`–`:154`／`:189`／`:204`／`:223`–`:233`）与 `d114b7576b78`（§1 Q1／Q4 逐字、§2 派生动作 B 逐字）；本件全部行号以本棒实测为准。

### §1-3 落盘前占用检查（本棒实测 · 双通道）

`os.walk` 全树遍历 **123** 目录；目标名 `_m44_status_enum_backfill_design_2026_10_16.md` **同名命中 ＝ 0**；`os.path.exists` 精确路径 ＝ **False** ⇒ **未需 `_r1` 后缀**，⛔ 0 覆盖、⛔ 0 回改他件。

---

## §2 枚举复测面（测量面 · FTFB 之「判死线先于设计」之同源纪律）

### §2-1 扫描方法与完整性自证

| 项 | 本棒实测 |
| :-- | :-- |
| 遍历引擎 | **Python 3.14.7 `os.walk`**（⛔ **0 用** PowerShell `-Recurse`＋`SilentlyContinue`——后者静默吞错，不可作完整性依据） |
| 遍历错误处理 | `onerror=` 回调**显式收集**；本棒实测**遍历错误 ＝ 0**（断言：回调未捕获任何 `OSError`） |
| 根目录 | `_repo_mirror`（**主仓**） |
| 排除 | `.git`（本棒实测：**仓内 `.git` 目录不存在**，故该排除规则**无实效**——如实登记，见 §5 `KD-5`）；仓外归档区 `〔归档件引用·未上传:〔归档区〕〕` 在根之外，**天然未扫**，⛔ 0 触归档区 |
| 目录数 | **123** |
| 文件总数（全树） | **2,598** |
| JSON 总件数 | **509** |
| 解析失败件数 | **0**（见 §2-2 之三通道回退） |
| 实取编码分布 | `utf-8` 503／`utf-16` 4／`utf-8-sig` 2 |
| 终版扫描完成时点 | **2026-10-16T08:43:11.660580+00:00**（UTC） |
| 命中文件数（含命中键） | **174** |

### §2-2 解析失败件之三通道回退（如实报 · ⛔ 0 静默吞错）

**首轮严格 `utf-8` 解析实测得解析失败 6 件**，逐件列出（⛔ 0 以 `SilentlyContinue` 掩盖）：

| # | 件（相对路径） | bytes | 首 6 字节 hex | 根因 |
| :-: | :-- | --: | :-- | :-- |
| 1 | `.tmp/_m5_k5_net.json` | 92,060 | `fffe7b000d00` | **UTF-16LE ＋ BOM** |
| 2 | `.tmp/_m5_k5_net2.json` | 952,252 | `efbbbf7b0d0a` | **UTF-8 ＋ BOM** |
| 3 | `.tmp/_m5_k5_scan.json` | 9,530 | `fffe7b000d00` | **UTF-16LE ＋ BOM** |
| 4 | `.tmp/_m5_reaudit_archive_out.json` | 654 | `fffe7b000d00` | **UTF-16LE ＋ BOM** |
| 5 | `.tmp/_rj5_convention_check_2026_09_27.out.json` | 8,983 | `efbbbf7b0d0a` | **UTF-8 ＋ BOM** |
| 6 | `.tmp/_t2_t3_prex_a_route_out.json` | 22,640 | `fffe7b000d00` | **UTF-16LE ＋ BOM** |

**回退复测**：`utf-8` → `utf-8-sig` → `utf-16` 逐级尝试后，**6/6 全部解出**，其中 4 件含命中键（`#1` 7 处／`#2` 119 处／`#5` 4 处；`#3`／`#4`／`#6` 命中 0）⇒ **终版扫描解析失败 ＝ 0**，此 6 件之取值已**计入**终版枚举（`#2` 之 `added`／`modified` 等为 `status` 键之第三方 HTTP 语义值，见 §5 `KD-6`）。

### §2-3 全量枚举结果（本棒实测 · 任务口径：4 键全收、含 `.tmp`、含非字符串值）

| 键 | 实测不同值数 | 实测出现次数 | 备注 |
| :-- | --: | --: | :-- |
| `status` | **125** | **659** | 含 HTTP 状态码数字（`<num:200>` 141 次）与 `null`（52 次）等非字符串值 |
| `verdict` | **117** | **970** | 含 `<non-scalar:dict>` 23 次（verdict 值为对象） |
| `state` | **12** | **17** | 大量值为长句公式/状态描述（自由文本） |
| `anchor_status` | **1** | **1** | 唯值 `drift_authorized`（全库唯一定位见 §2-5） |
| **四键并集 distinct** | **251** | — | 任务口径之总数 |

**全量取值登记域（251 值 · 任务口径 · 按出现次数降序 · 本节即「取值登记域」之附件清单）**：

| # | 值 | 出现次数 | 所属键 | 类型 |
| --: | :-- | --: | :-- | :-- |
| 1 | `correct` | 209 | verdict | 字符串 |
| 2 | `PASS` | 164 | status, verdict | 字符串 |
| 3 | `<num:200>` | 141 | status | 非字符串 |
| 4 | `FAIL` | 135 | status, verdict | 字符串 |
| 5 | `modified` | 102 | status | 字符串 |
| 6 | `incorrect` | 89 | verdict | 字符串 |
| 7 | `FAIL (N=6 < 10)` | 77 | verdict | 字符串 |
| 8 | `<null>` | 52 | status, verdict | 非字符串 |
| 9 | `FAIL (N=15 < 20)` | 30 | verdict | 字符串 |
| 10 | `ok` | 28 | status | 字符串 |
| 11 | `⛔0动·系谱/历史对照引用(非现行指纹)` | 28 | status | 字符串 |
| 12 | `COMPLETE` | 27 | status | 字符串 |
| 13 | `FAIL (任一教师 J < 0.85)` | 24 | verdict | 字符串 |
| 14 | `<non-scalar:dict>` | 23 | verdict | 非字符串 |
| 15 | `FAIL (>=1 教师 N < 10)` | 18 | verdict | 字符串 |
| 16 | `supplemented` | 18 | status | 字符串 |
| 17 | `GRAY` | 17 | verdict | 字符串 |
| 18 | `clean` | 17 | status | 字符串 |
| 19 | `added` | 16 | status | 字符串 |
| 20 | `not_found (2026-09-22 C7 复核): 本地+远端全树均无此文件 (远端全树 0 条 .mavis 路径); 原值保留为 2026-09-09 冻结时声明值` | 14 | status | 字符串 |
| 21 | `FAIL (N=3 < 10)` | 11 | verdict | 字符串 |
| 22 | `supports_H_GT8` | 10 | verdict | 字符串 |
| 23 | `拟刷·N型行级指针(真陈旧·行号另核)` | 10 | status | 字符串 |
| 24 | `NOISE` | 9 | verdict | 字符串 |
| 25 | `REAL_RUN` | 9 | status | 字符串 |
| 26 | `待PI裁·未归入 A/B/C/D/E 任一现行分类` | 9 | status | 字符串 |
| 27 | `PASS (温度方向一致)` | 8 | verdict | 字符串 |
| 28 | `evaluated` | 8 | status | 字符串 |
| 29 | `on_disk_verified` | 8 | status | 字符串 |
| 30 | `PARTIAL (0/30)` | 7 | status | 字符串 |
| 31 | `<num:-1>` | 6 | status | 非字符串 |
| 32 | `DIFFERENTIATED` | 6 | verdict | 字符串 |
| 33 | `FAIL (>=1 教师 N < 20)` | 6 | verdict | 字符串 |
| 34 | `PASS (端点方向一致)` | 6 | verdict | 字符串 |
| 35 | `unfrozen_pending_PI` | 6 | status | 字符串 |
| 36 | `<num:-2>` | 5 | status | 非字符串 |
| 37 | `fetch_failed` | 5 | status | 字符串 |
| 38 | `pending` | 5 | status | 字符串 |
| 39 | `triggered` | 5 | status, verdict | 字符串 |
| 40 | `HTTP_200` | 4 | status | 字符串 |
| 41 | `Local skill not found — 〔本地绝对路径·脱敏略:plugins〕 实测 0 项（空目录）` | 4 | status | 字符串 |
| 42 | `PASS (>= 7/9 model significantly deviate from transverse Ising)` | 4 | verdict | 字符串 |
| 43 | `unachieved` | 4 | state | 字符串 |
| 44 | `⛔ 0 判档 (归 verdict-keeper)` | 4 | verdict | 字符串 |
| 45 | `⛔0改·PI 轮38 裁「对外稿 0 改」` | 4 | status | 字符串 |
| 46 | `拟刷·M型台账三元组(真陈旧)` | 4 | status | 字符串 |
| 47 | `NOT_MET` | 3 | verdict | 字符串 |
| 48 | `NOT_RUN` | 3 | status | 字符串 |
| 49 | `OBSERVED` | 3 | verdict | 字符串 |
| 50 | `SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)` | 3 | status | 字符串 |
| 51 | `_v4_pi_cot_v2_verdict.md (EB9AD4193CF2) — 字面冻结` | 3 | verdict | 字符串 |
| 52 | `seed′ 已 PI 裁「照采」，规则冻结生效（生效即锁）` | 3 | status | 字符串 |
| 53 | `seed″ 已落定（6904852f8ceb）＋ S0′ 已生效（fd4ec7559342）⇒ 抽取解锁` | 3 | status | 字符串 |
| 54 | `⛔0刷·规则条体(载「键」之规则,非身份引用)` | 3 | status | 字符串 |
| 55 | `⛔0动·Q型条文直引/历史登记` | 3 | status | 字符串 |
| 56 | `⛔0擅改·P型计数核验键` | 3 | status | 字符串 |
| 57 | `COMPUTED` | 2 | verdict | 字符串 |
| 58 | `FAIL (N=1 < 10)` | 2 | verdict | 字符串 |
| 59 | `GRAY (marginal deviation, expand graph family needed)` | 2 | verdict | 字符串 |
| 60 | `KD` | 2 | verdict | 字符串 |
| 61 | `Local skill not found —— 〔本地绝对路径·脱敏略:plugins〕 实测 0 项（空目录）；本 turn 0 挂载任何 skill 加载工具；skills/ 下 0 命中 experimental-design` | 2 | status | 字符串 |
| 62 | `MATCH (未动)` | 2 | status | 字符串 |
| 63 | `N/A` | 2 | verdict | 字符串 |
| 64 | `OK` | 2 | status | 字符串 |
| 65 | `PARTIAL` | 2 | status | 字符串 |
| 66 | `PARTIAL (52/60)` | 2 | status | 字符串 |
| 67 | `PASS (A channel independent, \|Spearman-1\|>0.10)` | 2 | verdict | 字符串 |
| 68 | `PASS (判定稳健 + T1 verdict 信息量补正)` | 2 | verdict | 字符串 |
| 69 | `PASS (沿 T1 verdict 结论引用 — 不重测)` | 2 | verdict | 字符串 |
| 70 | `PENDING` | 2 | state | 字符串 |
| 71 | `READY_PRIOR` | 2 | status | 字符串 |
| 72 | `REJECTED` | 2 | verdict | 字符串 |
| 73 | `STRONG_PASS` | 2 | verdict | 字符串 |
| 74 | `UNVERIFIED（判据退化）` | 2 | verdict | 字符串 |
| 75 | `anchored_canonical_measured_under_PI_Q2_backfill` | 2 | status | 字符串 |
| 76 | `anchored_under_PI_Q2_backfill_case_甲; carrier_form_adjudicated` | 2 | status | 字符串 |
| 77 | `frozen_by_PI_2026_09_27_ruling_2` | 2 | status | 字符串 |
| 78 | `locked_pending_effective` | 2 | status | 字符串 |
| 79 | `mixed` | 2 | verdict | 字符串 |
| 80 | `恒等 (mathematically identical under this construction)` | 2 | verdict | 字符串 |
| 81 | `本棒未加载任何 skill（派工单未指定 skill）` | 2 | status | 字符串 |
| 82 | `草案态 · 保留并列` | 2 | state | 字符串 |
| 83 | `**下游派生**（hamming 最小值 = 0.1042 > 阈值 0.1）` | 1 | verdict | 字符串 |
| 84 | `**前存构造面事实, 非 S2 引入**: S2 模板面按 PI 拍板① 维持 v3 短语 5 类 0 改动, v3 / S1 同一模板面下同样不达; 已作为独立登记项披露 (rescript §3.1), 0 隐含触发 G-3、0 私改 G-3 字面、0 补覆盖率。处置 (a) 承认 substr` | 1 | status | 字符串 |
| 85 | `**本棒已修哨兵实现（新名件内）**；既有 8 图在修好哨兵下重算并登记；**0 回改 34ff826f97c2**` | 1 | status | 字符串 |
| 86 | `**构造恒等**（22/22 图 \|a12-a21\| ≡ 0 < 1e-3）` | 1 | verdict | 字符串 |
| 87 | `**硬编码常量**（函数无条件 return 0.5，与入参 t_frac 无关）` | 1 | verdict | 字符串 |
| 88 | `**精确不动点 + 早退双钉**（22/22 图 dx1(x=0.5) ≡ 0）` | 1 | verdict | 字符串 |
| 89 | `**量纲错配**（V3 把 R_frac 与「归一化到 T_frac 单位」的常数 0.5 相减）` | 1 | verdict | 字符串 |
| 90 | `0 判档 (归 verdict-keeper)` | 1 | verdict | 字符串 |
| 91 | `2 态 (T vs rest)，ẋ = x(1−x)(f_T − f_A)，RK4 (dt=5e-3)；fitness 由扰动条件植入 f=(x0, 1−x0)；命中 = 到最近边界不动点距离 <= TOL` | 1 | state | 字符串 |
| 92 | `2 态离散 replicator 映射 x_{k+1}=x·u_T/(x·u_T+(1−x)·u_A)；收益矩阵 A(x0)=[[0,x0],[1−x0,0]]（反协调，内点稳定 NE = x0，收益差 D(x)=x0−x 斜率 −1）` | 1 | state | 字符串 |
| 93 | `2 态，logit(x_{k+1}) = (1−s)·logit(x_k) + s·logit(x0)，s=0.25（softmax 响应映射的logit 正规形）；内点不动点 ≡ x0，几何收敛` | 1 | state | 字符串 |
| 94 | `2026-09-22 C7 修订: 055e874ea5c1 → 1722500da4aa (2026-09-22 本地实测; 2026-09-15 已 DRIFT_AUTHORIZED)` | 1 | status | 字符串 |
| 95 | `2026-09-22 C7 修订: 3aa661cfbab5 → 4bdec2683f06 (2026-09-22 本地实测)` | 1 | status | 字符串 |
| 96 | `2026-09-22 C7 修订: 9f383935c00c → 275e480ba4d9 (2026-09-22 本地实测; 2026-09-15 已 DRIFT_AUTHORIZED)` | 1 | status | 字符串 |
| 97 | `2026-09-22 C7 修订: v18 62c1a41e1db8 与 v17 af51da229652 移除 (本地+远端全树+远端 git 历史均无, PI Q1 拍板); v20 改远端 main 实测值 84ce9b028b0c (commit 6afa134348; 声明值 6edb2a` | 1 | status | 字符串 |
| 98 | `3 态 (T,R,A)，ẋ_i = x_i(g_i − ḡ)，g_i = c·(f_i − x_i)，c=0.5，RK4 (dt=0.05)；f = 扰动目标三元组（归一化份额）=> 内点不动点 ≡ f、负频依赖稳定、Σx_i 严格守恒` | 1 | state | 字符串 |
| 99 | `60-cell 整数三元组 (T,R,A) 每步 1 个 cell 从盈余最大类移到亏缺最大类，直到命中扰动目标三元组；步数 = n_iter；结构上限 60 必收敛` | 1 | state | 字符串 |
| 100 | `<bool:True>` | 1 | verdict | 非字符串 |
| 101 | `<num:404>` | 1 | status | 非字符串 |
| 102 | `ADOPTED` | 1 | verdict | 字符串 |
| 103 | `ALL_NOISE` | 1 | verdict | 字符串 |
| 104 | `BLOCKED: TeamoRouter base_url (https://api.teamorouter.com/v1) 在本机无法连通 (TCP 443 timeout) + DNS 解析到 Facebook IP 段(31.13.x.x),疑似域名失效/被劫持。无法验证 model 列表,无` | 1 | verdict | 字符串 |
| 105 | `BLOCKED_AT_STEP1` | 1 | status | 字符串 |
| 106 | `BLOCKED_BY_ENDPOINT_QUOTA` | 1 | status | 字符串 |
| 107 | `COMPLETED` | 1 | status | 字符串 |
| 108 | `COMPLETED_WITH_LIMITATION` | 1 | status | 字符串 |
| 109 | `COMPLETE_PARTIAL` | 1 | status | 字符串 |
| 110 | `DEAD` | 1 | verdict | 字符串 |
| 111 | `DELTA 1.30 GRAY 不稳健 (本次独立复算 1.05 NOISE)` | 1 | verdict | 字符串 |
| 112 | `EXC (urllib)` | 1 | status | 字符串 |
| 113 | `FAIL (>= 7/9 model enter transverse Ising region)` | 1 | verdict | 字符串 |
| 114 | `FAIL (>= 7/9)` | 1 | verdict | 字符串 |
| 115 | `FAIL (exploratory, 探索性预跑, 非正式判定)` | 1 | verdict | 字符串 |
| 116 | `FAIL (formal v2, 正式判定)` | 1 | verdict | 字符串 |
| 117 | `FAIL (ε=0.41 远大于 round-off 1.11e-16)` | 1 | verdict | 字符串 |
| 118 | `FAIL_ENDPOINT_UNREACHABLE` | 1 | verdict | 字符串 |
| 119 | `G-3 按「全序列 + 短语模式」子集判读；嵌入子项如实记未启用 = 模板面未升，0 补 0、0 顶替` | 1 | status | 字符串 |
| 120 | `GRAY (mixed distribution)` | 1 | verdict | 字符串 |
| 121 | `GRAY (失真界) / 死 (双相结构, 沿 V3 v4)` | 1 | verdict | 字符串 |
| 122 | `GRAY/NOISE 边界` | 1 | verdict | 字符串 |
| 123 | `GRAY_NOISE_BOUNDARY` | 1 | verdict | 字符串 |
| 124 | `HTTP_401` | 1 | status | 字符串 |
| 125 | `INCOMPLETE_BLOCKED` | 1 | status | 字符串 |
| 126 | `INCOMPUTABLE_GAMMA` | 1 | verdict | 字符串 |
| 127 | `INDEPENDENT` | 1 | verdict | 字符串 |
| 128 | `LANDED（读数面）—— 三分量各自四项读数已报；0 独立复算其数值（依赖 0 落盘之 raw embeddings）` | 1 | status | 字符串 |
| 129 | `LIFTED` | 1 | status | 字符串 |
| 130 | `LIMITED —— link_verified/self_verified_only 之全链哈希关系已由非同源重算验证（22/22 吻合）；但 dual 后 6 hex（semantic_hash）所依 18 hyperplanes 权重矩阵 0 随件落盘 ⇒ 该段不可非同源重算` | 1 | status | 字符串 |
| 131 | `Local skill not found` | 1 | status | 字符串 |
| 132 | `MARGINAL` | 1 | verdict | 字符串 |
| 133 | `MATCH against this v2's registered value 7a097d7802d1` | 1 | verdict | 字符串 |
| 134 | `N/A (本机无 EZKL/Halo2/Plonky2 后端)` | 1 | verdict | 字符串 |
| 135 | `N/A (本机无 SGX/SEV/H100 硬件)` | 1 | verdict | 字符串 |
| 136 | `NOISE (C 路径理论可行,但 22 caption 2D SVD ratio=1.0562 已证 NOISE,加 RAG 不改变结论)` | 1 | verdict | 字符串 |
| 137 | `NOISE (本次独立复算 DELTA 1.05)` | 1 | verdict | 字符串 |
| 138 | `NONE - K-V3S-4-2 NOT judged (out of scope this wave by work order)` | 1 | verdict | 字符串 |
| 139 | `OBSERVED (沿 P-D V0.1 PASS)` | 1 | verdict | 字符串 |
| 140 | `OBSERVED_WITH_QUALIFIER` | 1 | verdict | 字符串 |
| 141 | `OBSERVED_WITH_QUALIFIER (2 model 0.867 但 CoT 未公开对比)` | 1 | verdict | 字符串 |
| 142 | `P-4 ② 已定为**并报披露**（0 归并）；若 PI 后续要归并 ⇒ 属类推，须另行拍板` | 1 | status | 字符串 |
| 143 | `P-5 ① **不设** ⇒ 本棒 0 预填、new_thresholds_added = 0` | 1 | status | 字符串 |
| 144 | `P-A 均衡带稳定信号 = V3 终极形式 no-RAG + 双 model baseline 物理基础` | 1 | verdict | 字符串 |
| 145 | `P-C 失真界 α-β 模板冗余修正(饱和函数 + 向量余弦双修正) 物理稳健度提升` | 1 | verdict | 字符串 |
| 146 | `PARTIAL (17/30)` | 1 | status | 字符串 |
| 147 | `PARTIAL (30 cells V2 接入但准确率 <80%,需人工复审)` | 1 | verdict | 字符串 |
| 148 | `PARTIAL —— 期望全集 {0,1} 已报、实到已报、覆盖判定 PASS；但盘上 0 有 source 编码表的冻结件字面 ⇒ 出处为「未核得」` | 1 | status | 字符串 |
| 149 | `PASS (delta_hash 必要性下降)` | 1 | verdict | 字符串 |
| 150 | `PASS (delta_hash↓)` | 1 | verdict | 字符串 |
| 151 | `PASS (全 6 cells N≥10/教师; plan 字面 15 pairs/教师 ≥ N_min=10 字面满足)` | 1 | verdict | 字符串 |
| 152 | `PASS (判定稳健, 不入勘误链)` | 1 | verdict | 字符串 |
| 153 | `PASS_BEST` | 1 | status | 字符串 |
| 154 | `PASS（22/22 全吻合，0 分歧）` | 1 | verdict | 字符串 |
| 155 | `PHYSICAL_FORMULA_OPT (Lindblad 静态拟合 3 通道衰减率, 物理映射清晰)` | 1 | verdict | 字符串 |
| 156 | `PHYSICAL_FORMULA_OPT (α-β 模板冗余修复, V2 阶段 3 ratio 1.30 沿用 + 双修正)` | 1 | verdict | 字符串 |
| 157 | `PHYSICAL_FORMULA_OPT (三模态 ε 修复, 沿 V2 阶段 5 F-5 FAIL 修复路径)` | 1 | verdict | 字符串 |
| 158 | `PHYSICAL_FORMULA_OPT (双指纹同源聚集度, 沿 PD_V0.2 §3 算法)` | 1 | verdict | 字符串 |
| 159 | `PHYSICAL_FORMULA_OPT (沿 v3 §6 修正 2 向量余弦, 9 model × 60 cells)` | 1 | verdict | 字符串 |
| 160 | `PHYSICAL_FORMULA_OPT (沿 v3 §6 散射公式, 9 model S_eff 物理信号稳定)` | 1 | verdict | 字符串 |
| 161 | `PHYSICAL_FORMULA_OPT_GRAY (沿 v3 §6 三模态守恒, 9 model × 60 cells; Trae R4 勘误后维持 GRAY)` | 1 | verdict | 字符串 |
| 162 | `PI 复核生效即锁（裁项经派工单载明；件B §11 勾选栏盘上空白、件B 字节 0 改动 —— 如实登记，0 编造勾选）` | 1 | state | 字符串 |
| 163 | `PI 复核生效（确认批 3）` | 1 | status | 字符串 |
| 164 | `PI 拍板② 门不变 + 二值/常量单列；th_v3_19_compliance 如实记 false，门限 0 改动；S2 新增 3 项 n_distinct 全 >3 ⇒ 警报不来自新增面` | 1 | status | 字符串 |
| 165 | `PI 拍板③ 门不变 + 二值单列；th_v3_19_compliance 如实记 false，门 0 改动` | 1 | status | 字符串 |
| 166 | `PI_adjudicated (Q1/Q2/Q3 逐字依卡 ask_207b060a5273ab88912e451f)；余留开口项 U-2（version 子字段）pending；⛔ 0 宣告项闭 / 0 宣告①毕` | 1 | status | 字符串 |
| 167 | `P_F_IMPLEMENTATION_V1_REPORT_FILED_5_BOSS_EVAL_9MODEL_CONSERVATION_6_CANDIDATE_USER_1144_TRIGGER_RECEIVED_7_IRON_RULES_PASS` | 1 | verdict | 字符串 |
| 168 | `RECOMMENDED strict, 但 strict/loose 二选一拍板权属 user/Mavis (本任务不擅自落 spec verdict)` | 1 | status | 字符串 |
| 169 | `STRICT_CONSERVATION (1.11e-16 round-off, 沿 V2 阶段 2)` | 1 | verdict | 字符串 |
| 170 | `STRICT_CONSERVATION (三层守恒: 9 model + v19 + KT-B1 + V2 60 cells 全 PASS)` | 1 | verdict | 字符串 |
| 171 | `STRICT_CONSERVATION (三层守恒: 9 model + v19 + KT-B1 attack 全 PASS)` | 1 | verdict | 字符串 |
| 172 | `STRICT_CONSERVATION (双主线 60 cells T+R+A=1 strict 1.11e-16)` | 1 | verdict | 字符串 |
| 173 | `STRUCTURALLY_INCOMPUTABLE` | 1 | status | 字符串 |
| 174 | `THEORETICAL` | 1 | verdict | 字符串 |
| 175 | `TRIGGERED` | 1 | verdict | 字符串 |
| 176 | `TRIGGERED (V0 → V0.1 已升级, 5 锚真值已算)` | 1 | verdict | 字符串 |
| 177 | `TRUST_ANCHOR (100% 可复算; 本脚本抽验 6 项全 PASS, 全量 15 项见 R3 报告)` | 1 | status | 字符串 |
| 178 | `UNVERIFIED (无算法工件; 拼接锚复算 PASS 仅证明"先有值后拼锚"的生成方式)` | 1 | status | 字符串 |
| 179 | `V0_PRE_REGISTERED (P-F SPEC 草稿 + 5 BOSS 沿用占位 + user 11:44 主动 trigger)` | 1 | verdict | 字符串 |
| 180 | `V3 26-cell v2 穿越均衡 2 model 精确重合 = P-A 均衡带稳定信号` | 1 | verdict | 字符串 |
| 181 | `V7_COMPREHENSIVE_FINAL_REPORT_FILED_5_CANDIDATES_2_PASS_3_GRAY_1_DEAD_1_PF_TRIGGERED_6_CANDIDATES_PF_INTEGRATED_V2_PHASE_1_3_5_PLUS_P_F_IMPLEMENTATION` | 1 | verdict | 字符串 |
| 182 | `abstained` | 1 | status | 字符串 |
| 183 | `anchored_under_PI_Q2_P-甲; value independently recomputed bit-identical; awaiting PI final close-out of the ECR anchor line` | 1 | status | 字符串 |
| 184 | `anchored_under_PI_Q2_backfill; value independently recomputed bit-identical; awaiting PI final close-out of the ECR anchor line` | 1 | status | 字符串 |
| 185 | `anchored_under_PI_Q2_backfill; value independently recomputed bit-identical; binding face adjudicated by PI 2026-10-15 (裁丁 · ask_207b060a5273ab88912e4` | 1 | status | 字符串 |
| 186 | `b 半 3 题入账后现态（本棒实测）` | 1 | state | 字符串 |
| 187 | `b 半 3 题已入账的**现态**（本棒 2026-09-30 落盘前实测）` | 1 | state | 字符串 |
| 188 | `byte + semantic 双指纹 PASS, delta_hash 必要性下降` | 1 | verdict | 字符串 |
| 189 | `canceled` | 1 | status | 字符串 |
| 190 | `carried by the batch register (another separately established face), 0 retroactive edit of any spec` | 1 | status | 字符串 |
| 191 | `carried by the batch register as a separately established state-migration face; 0 retroactive edit of patch carrier da517c115f3c` | 1 | status | 字符串 |
| 192 | `carrier_anchored_effective; field_adjudicated_by_PI (C-甲 · ask_207b060a5273ab88912e451f §1-Q1)` | 1 | status | 字符串 |
| 193 | `carrier_anchored_effective; field_pending_PI` | 1 | status | 字符串 |
| 194 | `control_only_not_threshold` | 1 | status | 字符串 |
| 195 | `deviation_registered` | 1 | status | 字符串 |
| 196 | `double PASS (final) -> cross-day full collection confirmed` | 1 | verdict | 字符串 |
| 197 | `downgraded_to_approximate_potential_game` | 1 | verdict | 字符串 |
| 198 | `drift_authorized` | 1 | anchor_status | 字符串 |
| 199 | `field_coordination_value_supported` | 1 | verdict | 字符串 |
| 200 | `frozen vs unfrozen_pending_PI -- un-adjudicated (Q7)` | 1 | status | 字符串 |
| 201 | `glm-latest 接入 + GSM8K 5 cells 全 PASS` | 1 | verdict | 字符串 |
| 202 | `glm-latest 接入成功` | 1 | verdict | 字符串 |
| 203 | `inconclusive` | 1 | verdict | 字符串 |
| 204 | `inconclusive_preregistered_undefined_band` | 1 | verdict | 字符串 |
| 205 | `killed` | 1 | verdict | 字符串 |
| 206 | `measured_pending_PI` | 1 | status | 字符串 |
| 207 | `no_separation_adaptive_attack_not_decisive` | 1 | verdict | 字符串 |
| 208 | `not_found (2026-09-22 C7 复核): 本地+远端全树均无 docs/V3X/KT_C1_SPEC_V0.md; 另有 KT_C1_SPEC_V0.1.md 本地+远端各一份 (31241B, 远端版 sha256=59d8f56347d5, 名与哈希均不符本声明值); 原值保留` | 1 | status | 字符串 |
| 209 | `not_locked_reference_only` | 1 | status | 字符串 |
| 210 | `patch_status: PENDING REMAINS UNRESOLVED - outside this card's subject and outside reconcile 4de10aad8f0b's scope (that reconcile covers P_A_HARNESS o` | 1 | state | 字符串 |
| 211 | `potential_game_explanation_complete` | 1 | verdict | 字符串 |
| 212 | `registered_as_arm_level_limit` | 1 | status | 字符串 |
| 213 | `registered_as_scope_limit` | 1 | status | 字符串 |
| 214 | `registered_for_pi_decision_not_self_disposed` | 1 | status | 字符串 |
| 215 | `rejected as expected` | 1 | verdict | 字符串 |
| 216 | `replaced_by_kimi_artifacts` | 1 | status | 字符串 |
| 217 | `supplementary_measured_not_counted_in_judgment_b` | 1 | status | 字符串 |
| 218 | `supports_H_GT8B` | 1 | verdict | 字符串 |
| 219 | `supports_narrowed_monotonicity` | 1 | verdict | 字符串 |
| 220 | `supports_potential_game_framework` | 1 | verdict | 字符串 |
| 221 | `triggered_for_strategyqa` | 1 | status | 字符串 |
| 222 | `unverifiable_no_attribution` | 1 | status | 字符串 |
| 223 | `⛔0刷·自指承载(修订关系本体)` | 1 | status | 字符串 |
| 224 | `⛔0刷·自指承载(系谱事实本体 A 型)` | 1 | status | 字符串 |
| 225 | `✅ 修正成功(原公式恒退化, 修正 1/2 恢复 9 model 区分度)` | 1 | verdict | 字符串 |
| 226 | `❌ 不成立 (实测) — 如实登记, 0 掩饰` | 1 | status | 字符串 |
| 227 | `不触发处置 (沿 result_v3 §feature_degradation_check 字面: 二值/低基数特征 n_distinct ≤3 是设计预期, 非退化); 沿 PI 拍板③ 二值单列不展开` | 1 | verdict | 字符串 |
| 228 | `主读法按 T-3 记不可判（剔除非补 0）；另并报算式读数作敏感性面；字面是否改写待 PI 拍板` | 1 | status | 字符串 |
| 229 | `主读法沿 v3 executor 实现字面 (SEED+13) 以保与 v3 CI 逐位可比；另并报 RandomState(42) 字面 敏感性面 CI，两者下界同判；0 擅改 seed，0 隐藏差异` | 1 | status | 字符串 |
| 230 | `仍挂 PI；本件 0 静默沿用 v3 值` | 1 | status | 字符串 |
| 231 | `仍挂 PI；本棒 0 擅调` | 1 | status | 字符串 |
| 232 | `口径缺位（提案 P-S1-1 未拍板落地）` | 1 | status | 字符串 |
| 233 | `可反推 (非不可反推): 唯一**独立**复现构造 = P0 (剔 correction 后整链重跑含重训); P3 为其同义改写; 其余 6 种自然读法均不复现` | 1 | verdict | 字符串 |
| 234 | `可行：0 触饱和（PASS 面待 verdict-keeper 裁）` | 1 | verdict | 字符串 |
| 235 | `在案（只解释 γ-21，0 削弱之）` | 1 | status | 字符串 |
| 236 | `如实登记为未评估项：idx 37 / 38 / 39 的 rf_len_bucket / rf_pos_density / n_keywords_hit 三项特征随文本变化 ⇒ 若重训，全部 pred 可能变动；**本棒 0 擅开重训**（会改 result_v3 判定本体，超出本派工范围）` | 1 | status | 字符串 |
| 237 | `如实登记为派生退化/口径冗余；E sentinel 方向一致性结论不变（四腿同向），但证据基数记 3；口径是否需换构造使二者独立待 PI 拍板` | 1 | status | 字符串 |
| 238 | `如实登记为登记粒度差别；门限与判定 0 改动，两段结论方向一致` | 1 | status | 字符串 |
| 239 | `差 0 之全部可归因于 .tmp 之并发写入（剔 .tmp 后三走恒定）` | 1 | verdict | 字符串 |
| 240 | `已冻结（测量前）· 生效即锁` | 1 | status | 字符串 |
| 241 | `已按 PI 2026-09-28 拍板落**订正新名件** results/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md；原 result_v3 ledger 0 改` | 1 | status | 字符串 |
| 242 | `已按 PI 拍板① 执行并登记；嵌入腿 null 不参与方向一致性判定` | 1 | status | 字符串 |
| 243 | `已施测 (附限制)` | 1 | status | 字符串 |
| 244 | `已核准生效（生效即锁）` | 1 | status | 字符串 |
| 245 | `待 PI；本件只报读数 0 判` | 1 | status | 字符串 |
| 246 | `本件 0 复用「6 对」字面（0 回改派生件）；本面权威对数 = 6（含新增 2 对）` | 1 | status | 字符串 |
| 247 | `条款落地与否本棒 0 核；若本面触发 ⇒ 按 K-V5R3-0-A 落 KD 并 γ` | 1 | status | 字符串 |
| 248 | `母本在 KIMI 工作区 (Windows 路径), 本环境不可寻址; KIMI 22 件 d/pred 采用已冻结结果逐件引用 (results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json · blind_res` | 1 | status | 字符串 |
| 249 | `沿 S1 D-4 同构如实登记为口径冗余；E sentinel 方向一致性结论不受影响；口径是否需换构造待 PI 拍板` | 1 | status | 字符串 |
| 250 | `测量前预检已报（见 feasibility）；0 触饱和` | 1 | status | 字符串 |
| 251 | `生效即锁（PI 2026-09-29 11:52 批）` | 1 | status | 字符串 |

### §2-4 与取证件「44 值」之复测对照（逐位核对 · 如实报差异）

**（a）取证件 §3-4 具名 12 值（含括注截断写法）之逐位对照**：

| 取证件所载值 | 取证件计数 | 本棒实测计数 | 逐位判定 |
| :-- | --: | --: | :-: |
| `PASS` | 40 | 40（`status`）／164（并计 `verdict` 键） | ✅ **`status` 键计数逐位相符** |
| `FAIL` | 4 | 4（`status`）／135（并计 `verdict` 键） | ✅ **`status` 键计数逐位相符** |
| `ok` | 28 | 28（`status`） | ✅ 逐位相符 |
| `COMPLETE` | 27 | 27（`status`） | ✅ 逐位相符 |
| `REAL_RUN` | 9 | 9（`status`） | ✅ 逐位相符 |
| `on_disk_verified` | 8 | 8（`status`） | ✅ 逐位相符 |
| `fetch_failed` | 5 | 5（`status`） | ✅ 逐位相符 |
| `triggered` | 4 | 5（`status`） | ⚠ **＋1**（见 (b) 根因） |
| `pending` | 1 | 5（`status`） | ⚠ **＋4**（见 (b) 根因） |
| `locked_pending_effective` | 2 | 2（`status`） | ✅ 逐位相符 |
| `unfrozen_pending_PI` | 2 | 6（`status`） | ⚠ **＋4**（见 (b) 根因） |
| `not_found (2026-09-22 C7 复核: …)`（取证件为**截断写法**） | 14 | **14**（`status`；全串为「`not_found (2026-09-22 C7 复核): 本地+远端全树均无此文件 (远端全树 0 条 .mavis 路径); 原值保留为 2026-09-09 冻结时声明值`」） | ✅ **计数与字面均相符**（取证件以「…」截断） |

**（b）计数差异之根因（本棒实测定位 · 非推测）**：取证件 §3-4 所载「`.json` 共扫描 **391** 件 · 解析错误 **4**」——本棒复测：mtime **< 2026-10-14** 之 JSON 为 **388** 件（与其 391 高度贴近，差 3 件属其扫描时点与本棒 cut 边界之别）；其「解析错误 4」**逐位对应**本棒 §2-2 之 **PRE 层 4 件**（`#1`／`#2`／`#3`／`#5`，其余 2 件 mtime ≥ 10-14）。⇒ 取证件采**严格 `utf-8`** 且**计入**该 4 件之部分取值；本棒之差异（`triggered` ＋1／`pending` ＋4／`unfrozen_pending_PI` ＋4）源于 **10-14 之后新增件**（本棒实测：mtime ≥ 2026-10-14 之 JSON 121 件，其中 `.tmp` 外新增件贡献 `pending` ×4／`unfrozen_pending_PI` ×4／`triggered` ×1）。

**（c）总数值之对照（44 vs 本棒 251／222／207）**：本棒以**任务口径**（4 键、含 `.tmp`、含非字符串）得 **251**；以**取证件近似口径**（`status`/`verdict`/`state`、仅字符串值、**排除 `.tmp`**）得 **222**；以**最严同口径**（限 mtime < 10-14、严格 `utf-8`、排除 4 件解析失败件）得 **207**——**均 ≠ 44**。

> ⚠ **如实登记 · 不臆测其口径**：取证件「44」之确切口径（是否限 `status` 单键、是否仅计特定目录、是否仅计形如 `PASS`/`ok` 之裸枚举词而排除带括号/句子之复合值等）**在册 0 载**，本棒经 5 组口径变体试算（`status` 单键 103／`verdict` 单键 111／`state` 单键 11／三键仅顶层 20／三键深层 222）**未复现 44**。故本棒**不宣称**「44 有误」，⛔ **0 断言**其测量有误；仅如实登记：**本棒之复测实测值为 251（任务口径）／207（最严同口径）**，二者与「44」之差额**主因之一**为取证件仅具名 12 值而未逐条列全（其原文以「等」收尾），故 **44 系其枚举之自报数、非可逐位复核之全表**——登记为 §5 `KD-1`。

**（d）关键口径判读（供 PI 裁 · 我不代裁）**：`44 → 251/207` 之落差**不改变** PI 已裁之型：PI 裁甲型时之理由为「44 值映射未处置，径采闭集将致 **44 件失配**」；本棒复测实测**失配面为 251/207**（数量级**更大**），故**甲型之「⛔ 0 映射改写、既有值合法保留」之取向在复测后更被强化而非削弱**（闭集将使 251/207 值中除骨干外者皆失配）。

### §2-5 `anchor_status` 全库唯一定位

| 项 | 本棒实测 |
| :-- | :-- |
| 唯一命中文件 | `results/_pa_harness_anchor_value_update_v2.json`（`c43a84c70935`，16,043 B） |
| 命中路径 | `$.registered_value_update.anchor_status` |
| 命中值 | `drift_authorized` |
| 同层伴随键 | `anchor_status_continuation_face`／`authorization_refs`（载 PI 卡 `ask_83a44986f5d822a1ba7b83ad` Q3 逐字）／`drift_class`／`three_layer_drift_chain` 等 |

⇒ **实证取证件 §3-4 之断言**：「两件判断件**自填**之登记字段……实填之键名为 **`anchor_status`**、值 `drift_authorized`，伴 `authorization_refs`」——本棒独立实测**全库仅此 1 处** `anchor_status`，值与伴随键**逐位相符**。

---

## §3 甲型 schema 回填设计面（**设计件 · 候 PI 核准 · ⛔ 0 入锁 · ⛔ 0 改既有件**）

> **本节全部为设计草案，⛔ 0 已入锁、⛔ 0 已生效、⛔ 0 径行采认**。PI 核准后方可另棒执行；执行时**仍须**逐条复核 `verifier/handoff/` 下既有锚件 ⛔ 0 改动、⛔ 0 回改。

### §3-1 字段定义（甲型 · 开集字符串＋`status_detail`）

| 字段 | 类型 | 必填 | 定义 |
| :-- | :-- | :-: | :-- |
| `anchor_status` | **开集字符串**（free-form string，**非** `enum` 闭集） | 建议必填 | 锚之**登记态**（该锚当前在冻结链中之生效/授权/漂移处置状态）。**取值不封闭**——新状态出现时**直接新增字符串**即可，⛔ 0 需先改 schema |
| `status_detail` | 自由文本（string，可空串） | 可选 | 承载「为何落此态」之**明细/理由/授权引用**。甲型之核心：**判据进明细、态进 `anchor_status`** |

**字段语义分界（⛔ 防串面）**：`anchor_status` ＝ **态**（what）；`status_detail` ＝ **因**（why）。⛔ **0** 将二者互换；⛔ **0** 以 `status_detail` 之有无决定 `anchor_status` 之取值（明细缺失 ⇔ 态仍成立，只是理由未载）。

### §3-2 取值登记域（以 §2-3 实测枚举为附件清单）

甲型为**开集**，故「取值域」以**登记清单**形式承载：① **骨干值**（下表，PI 核准后可作**优先复用**之既有态）；② **全量实测值 251 项**（§2-3 之附件清单，实测全库 `status`/`verdict`/`state`/`anchor_status` 值）——新锚件若落既有值，**沿用原字面**、⛔ 0 另造同义新词。

| 骨干值（**沿用既有字面 · 草案 · 候 PI 核准**） | 本棒实测出处 |
| :-- | :-- |
| `drift_authorized` | 全库唯一定位 `$.registered_value_update.anchor_status`（`c43a84c70935`） |
| `anchored_under_PI_Q2_P-甲; value independently recomputed bit-identical; awaiting PI final close-out of the ECR anchor line` | `verifier/handoff/P_A_V0_anchors_sha256_12.json` 之 `$.anchors.P_A_V0_ECR_BASELINE.status`（`c4f029f780d8`）——**注**：此件用键名 `status`（非 `anchor_status`），见 §3-5 命名口径 |
| `unfrozen_pending_PI` | `results/_ge01_prereg_5anchor.json`／`_v2.json` 之 `$.status`（`4b020eb04605`／`f06313373fc6`） |
| `pending`（及 `locked_pending_effective`） | 全库实测 `status` 键（§2-3） |
| `on_disk_verified`／`REAL_RUN`／`COMPLETE` | 全库实测 `status` 键（§2-3） |

> ⛔ **0 代裁**：骨干值之**取舍**（哪些进「优先复用」层、哪些仅作实测附件）**属 PI 面**，本棒 ⛔ 0 定夺；上表为**草案建议·候 PI 核准**。

### §3-3 既有 251/207 值之归置（甲型下**合法保留 · ⛔ 0 映射改写**）

**明确载（PI 已裁之取向，本设计照录并落实为条款）**：

① 甲型为**开集** ⇒ §2-3 实测之 **251 个既有值全部合法保留**，⛔ **0 映射**、⛔ **0 改写**、⛔ **0 归并**为闭集、⛔ **0 追溯失效**任何既有件之取值。

② 凡既有件已写之 `status`／`verdict`／`state` 值，**原样有效**，新 schema **向后兼容**——不要求任何既有件回改即可继续合规。

③ **0 因「未在新骨干清单」而判既有值为非法**；新值/旧值**同权**（开集之义）。

### §3-4 迁移纪律（旧件一字不动 · 以新件为准）

| # | 纪律 | 内容 |
| :-: | :-- | :-- |
| 1 | **旧件 0 改动** | ⛔ **0** 修改／回改／移动／重命名／删除任何既有锚件（尤其 `verifier/handoff/` 下 `03c6c01f3697`／`c4f029f780d8` 等）任何一字 |
| 2 | **以新件为准** | 若将来落地 schema，**另出新版锚件**（如 `…_v2.json`），**新旧并存以新为准**（沿 `_ge01_prereg_5anchor_v3.json` 之 `supersession` 体例：`policy`＝「新旧并存以新为准 · 旧件一字未动 · 留痕」、`old_file_touched`＝0） |
| 3 | **入锁须 PI 复核** | 本 schema **生效即锁**须经 **PI 复核**；本棒 ⛔ **0 入锁**、⛔ 0 宣告生效 |
| 4 | **构造面 vs 真实面** | 归一化（case）之影响**局限本 schema 之构造域**；⛔ **0 外推**至既有件已冻结之 `status` 面 |

### §3-5 命名口径（`status` vs `anchor_status`）· 待 PI 裁

本棒实测发现**锚件内 status 面命名不统一**：`verifier/handoff/KT_ABC1_anchors_sha256_12.json`（`03c6c01f3697`）**无**任何 status 面；`P_A_V0_anchors_sha256_12.json`（`c4f029f780d8`）用键名 **`status`**；`_pa_harness_anchor_value_update_v2.json` 用键名 **`anchor_status`**；`_ge01_prereg_5anchor*.json` 用**顶层 `status`**。⇒ 建议新 schema **统一以 `anchor_status` 为主键**（锚件专属命名，⛔ 与全库通用 `status` 混同），并**保留旧键名兼容**（旧件 0 改动，读时兼容）。**此项属口径裁，候 PI 核准·本棒 0 代裁**。

---

## §4 现版锚 JSON 实测（`verifier/handoff/` · 按 mtime 定位最新版）

> ⚠ **对派工前提之如实更正**：派工单述「现版锚 JSON（**已非 `03c6c01f3697`**——v2/v3 已迭代）」。本棒实测：`verifier/handoff/KT_ABC1_anchors_sha256_12.json` **仍为 `03c6c01f3697`**（mtime 2026-09-09，**0 迭代**）；v2/v3 之迭代实发生于 **`results/_ge01_prereg_5anchor_v2.json`／`_v3.json`**（`f06313373fc6`／`0c269b9558da`）。⇒ 「KT 锚件已迭代」**不成立**；`verifier/handoff/` 下**最新**锚件为 `P_A_V0_anchors_sha256_12.json`（`c4f029f780d8`，mtime 2026-10-15，末位）。登记 §5 `KD-2`。

### §4-1 在盘现版 KT 锚件（`03c6c01f3697`）字段集实测

- 顶层键：`['anchors', 'boss_baselines', 'metadata']`
- `anchors` 分 3 组（`KT-A1`／`KT-B1`／`KT-C1`），每组 5 锚，**共 15 锚**
- **逐锚字段集**（全 15 锚**逐位一致**）：`['algorithm', 'field', 'object', 'path', 'value']`
- `status`／`verdict`／`state`／`anchor_status`／`status_detail` 键：**全文件各 0 出现**（字面计数 0）

### §4-2 最新在盘锚件（`c4f029f780d8` · P_A_V0）字段集实测

- 顶层键：`['anchors', 'author', 'authorization', 'date', 'existing_anchor_sets_untouched', 'integrity', 'method', 'schema_version']`
- `schema_version` ＝ `"p_a_v0_anchors_sha256_12.v0"`
- 唯一锚组 `anchors.P_A_V0_ECR_BASELINE`，其 7 子面键：`definition_anchor`／`value_anchor`／`upstream_anchor`／`caliber`／`recompute`／`limitation_face`／`deviation_disclosure`
- **含 `status` 面**：`$.anchors.P_A_V0_ECR_BASELINE.status` ＝ 「`anchored_under_PI_Q2_P-甲; value independently recomputed bit-identical; awaiting PI final close-out of the ECR anchor line`」
- `existing_anchor_sets_untouched` 逐字载：对 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（`03c6c01f3697`）之 action ＝ 「`read-only reference; 0 bytes changed`」

### §4-3 GE01 预注册锚件 v1→v2→v3 迭代替换链（v2/v3 迭代之实证）

| 版 | SHA-12 | bytes | `schema_version` | `status` 值（截断） |
| :-: | :-: | --: | :-- | :-- |
| v1 | `4b020eb04605` | 10,701 | `ge01-prereg-5anchor.v0` | `unfrozen_pending_PI` |
| v2 | `f06313373fc6` | 21,629 | `ge01-prereg-5anchor.v2` | `unfrozen_pending_PI` |
| v3 | `0c269b9558da` | 35,911 | `ge01-prereg-5anchor.v3` | `PI_adjudicated (Q1/Q2/Q3 逐字依卡 …)；余留开口项 U-2（version 子字段）pending；⛔ 0 宣告项闭 / 0 宣告①毕` |

v3 之 `supersession` 逐字载：`superseded_path`＝`results/_ge01_prereg_5anchor_v2.json`／`policy`＝「**新旧并存以新为准 · 旧件一字未动 · 留痕**」／`old_file_touched`＝**0**——⇒ **§3-4 迁移纪律第 2 条之仓内既有先例已验**（本棒 ⛔ 0 引为规范，仅载其实测先例）。

---

## §5 KD（known defects · 如实列 · 含扫描完整性之任何缺陷）

| 号 | KD | 依据（本棒实测／逐字） | 处置 |
| :-: | :-- | :-- | :-- |
| **KD-1** | **取证件「44 值」之确切口径不可复核**：本棒经 5 组口径变体试算（103／111／11／20／222／207）**均未复现 44**；取证件原文以「等」收尾、**仅具名 12 值**，故 44 系**自报数**而非可逐位复核之全表 | §2-4(c)(d)；`74e25d75d59d`:144 | ⛔ **0 断言**取证件测量有误；如实登记本棒实测值 **251（任务口径）／207（最严同口径）**；**口径之统一待 PI 裁**（本棒 ⛔ 0 代裁） |
| **KD-2** | **派工前提「KT 锚件已 v2/v3 迭代」不成立** —— 实测 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 仍为 `03c6c01f3697`（mtime 2026-09-09，0 迭代）；v2/v3 迭代实发生于 `results/_ge01_prereg_5anchor_v2/_v3.json` | §4 导语；本棒逐件 `sha256` 复算 | 如实更正；本棒设计面以「KT 锚件 `03c6c01f3697` 0 status 面」为事实基座 |
| **KD-3** | **锚件内 status 面命名不统一** —— `03c6c01f3697` 无 status；`c4f029f780d8` 用 `status`；`c43a84c70935` 用 `anchor_status`；`_ge01_prereg_*` 用顶层 `status` | §3-5；§4-1／§4-2／§2-5 | 建议统一主键 `anchor_status`＋旧键名读时兼容；**候 PI 裁·0 代裁** |
| **KD-4** | **取证件件 SHA 与派工 briefing 不符** —— briefing 载 `5b9478c7e86b`，本棒实测 `74e25d75d59d`（31,463 B，mtime 2026-10-14 01:57:09） | 本棒逐件 `sha256(b)[:12]` 复算 | ⛔ **0 断言** briefing 有误（可能 briefing 记于他时点/他版）；如实登记实测值，**以本棒实测为准** |
| **KD-5** | **`.git` 排除规则无实效** —— 本棒实测仓内 `.git` 目录**不存在**（顶层目录 ＝ `.mavis`／`.tmp`／`.trae`／`.vscode`／`attacks`／`corpus`／`deposon_team`／`docs`／`letters`／`paper`／`results`／`reviews`／`scripts`／`tests`／`tools`／`verifier`） | 本棒实测 `os.path.isdir` | 如实登记；该排除规则**无对象**，对结果 **0 影响** |
| **KD-6** | **`.tmp` 内含第三方 HTTP 语义之 `status`/`verdict` 值** —— 如 `status`＝`added`／`modified`／`<num:200>`（git commit 结果）、`verdict`＝`PASS (>= 7/9 model …)`（模型判定）等，属**非锚语义**之异域取值，混入全库枚举 | §2-2（`#1`／`#2`／`#5` 命中）；§2-3 值表 | 如实登记；建议 PI 裁时**斟酌是否以目录/命名空间隔离**（如仅取 `verifier/`＋`results/` 之锚语义值）——**候 PI 裁·0 代裁** |
| **KD-7** | **全库 `state` 键多落长句自由文本**（如 2 态/3 态动力学公式全串），取值 12 值中 6 值系整句公式/状态描述 | §2-3 `state` 值表 | 如实登记；印证甲型「开集」之适配性 |

### §5-1 阴性结论三重自审（扫描完整性）

| 自审维度 | 结论 |
| :-- | :-- |
| ① 扫描完整性 | **通过**：遍历错误 **0**（`os.walk` `onerror` 显式收集，未捕获任何 `OSError`）；509 件 JSON **逐件**尝试解析，解析失败经三通道回退**全部解出（失败 0**）；`.git` 无实效（KD-5）；归档区在根外天然未扫 |
| ② 模式非结构性互斥 | **通过**：四键（`status`/`verdict`/`state`/`anchor_status`）**非结构性互斥**——同名键在不同件指不同语义（`status` 于锚件＝登记态、于 `.tmp`＝HTTP 码、于 result＝模型判定），本棒**已按目录/语境标注**（§2-3 列所属键与类型；KD-6 标明异域）；无「同名键必同义」之误判 |
| ③ 时点新鲜 | **通过**：终版扫描 **2026-10-16T08:43:11Z**（今日）；既有值比对已按 mtime 分层（PRE/POST 10-14）以区分「测量时点漂移」与「口径差异」 |

### §5-2 ⛔ 本棒 0 作之事项（逐条）

① ⛔ **0 回改**任何既有件一字（本棒触动既有锚件数 ＝ **0**，已实测 handoff 下 6 件指纹 0 改动）｜② ⛔ **0 入锁**本 schema／⛔ 0 宣告生效｜③ ⛔ **0 采认**任何推断值（全部标「候 PI 核准」）｜④ ⛔ **0 代** PI 裁/释/择/给值（含 0 代裁骨干值取舍、0 代裁命名口径、0 代裁 44 之统一口径）｜⑤ ⛔ **0 网络**（本棒纯本地，⛔ 0 上传/0 远端写）｜⑥ ⛔ **0 触** `〔归档区〕` 归档区｜⑦ ⛔ **0 断言**取证件「44 值」测量有误｜⑧ ⛔ **0 宣告**①毕/0 宣告任何项闭｜⑨ ⛔ **0** 以他件自报指纹充实测（10/10 逐件复算）｜⑩ ⛔ **0** 用他人名头署名（署 `protocol-keeper`）。

### §5-3 遗留清单

| # | 遗留 | 状态 | 归属 |
| :-: | :-- | :-- | :-- |
| 1 | **甲型 schema 之 PI 复核生效**（生效即锁） | 🔴 **候 PI 核准**（本件为设计草案，⛔ 0 已入锁） | PI |
| 2 | **骨干值取舍**（哪些进优先复用层） | 🟠 **草案·候 PI 核准**（本棒 0 代裁） | PI |
| 3 | **命名口径**（`status` vs `anchor_status` 主键统一） | 🟠 **已建议·候 PI 裁**（KD-3） | PI |
| 4 | **「44 值」与「251/207 值」之口径统一** | 🟠 **已如实登记·候 PI 裁**（KD-1） | PI |
| 5 | **是否隔离异域取值**（`.tmp` 之 HTTP/模型判定语义，KD-6） | 🟡 **已建议·候 PI 裁** | PI |

---

*件止。**M-44-A-ENUM-BACKFILL · 枚举复测面＋甲型 schema 设计面**（`protocol-keeper` · 2026-10-16 · deposon ①段 · 候 PI 核准 · ⛔ 0 径行采认 · ⛔ 0 入锁）—— 测量面：全库 `status`/`verdict`/`state`/`anchor_status` 实测 **251** 值（任务口径，`status` 125／`verdict` 117／`state` 12／`anchor_status` 1，遍历错 0、解析失败 0、509 件 JSON），与取证件「44」对照：具名 12 值 12/12 命中、11 值计数逐位相符、3 值因时点漂移微增、`not_found (…)` 截断写法计数字面均符；44 之确切口径不可复现（KD-1，如实登记，0 断言其有误）；KT 锚件 `03c6c01f3697` 仍无 status 面、v2/v3 迭代实发生于 `_ge01_prereg_5anchor_v2/_v3`（KD-2）｜设计面：甲型（开集 `anchor_status`＋`status_detail`）、取值登记域以实测 251 值为附件、既有值合法保留⛔ 0 映射改写、迁移纪律「旧件一字不动·以新件为准·入锁须 PI 复核」、命名口径建议统一 `anchor_status`（KD-3）；KD 共 **7** 条｜⛔ 0 回改既有件 · 0 入锁 · 0 采认 · 0 代裁/释/择/给值 · 0 网络 · 0 触归档区 · 0 断言他件测量有误 · 0 宣告①毕/闭.*
