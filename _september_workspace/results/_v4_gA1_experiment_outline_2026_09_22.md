# V4 §1.1.1 最小可证伪实验轮廓代拟稿（Mavis 代拟，PI 委托 2026-09-22）

**委托留痕**：PI 于组 A 首批问卷（ask_f8837a5b3c168ef3d6e8c18a，2026-09-22）对 §1.1.1 答复「委托 Mavis 代拟」。本稿为代拟草案，回填问卷作答栏后**待 PI 复核确认生效**。本稿起草过程：0 LLM / 0 外部 URL / 0 GitHub / 0 WeChat / 0 密钥；未触动任何 V1–V3 冻结资产（教师侧素材全部只读）。

**作答对象**：邀请函 §4.1（`3D9F73519F6C:252`）——"What is the smallest, falsifiable experiment that can distinguish 'distilled from teacher X' from 'trained independently on similar data'?"——按题面要求克服 R5（KIMI-K3，散度定义）与 B6（Trae code，binning/KDE）两个 blocker。

**依赖注记**：本题依赖 §3.1（铁律边界，组 C 未拍）、§3.2（无学生侧；PI 已拍路径 B：构造 proxy student，问卷 L200）、§3.8（不稳健读数）。本轮廓按**铁律现状**（`no_llm` / `no_proxy` / `no_gateway` 均未放开）给出双轨设计：Track 1 铁律现状下可直接执行；Track 2 以 §3.1 路径 B/C/D 放开为前提（组 C 未拍，未决）。

---

## 1 GT 来源声明（S-36 困境的正面回答）

本实验**无真实学生侧真值**。GT 为**构造性**：正类 = 以 teacher X 输出为唯一素材构造的 proxy student 输出集合（§3.2 路径 B 已拍，落盘 `results/_v4_proxy_student_*`）；负类 = 独立构造的对照集合。任何「蒸馏检测」结论的适用域限定为「在构造性 proxy 上可分」，不外推到真实学生模型。此声明按 S-36（`3D9F73519F6C:230`「who labels the GT for distillation detection」）与豆包工作 S-36（「GT 是**不存在**的，而非不唯一」，`19C97B5CFF3C:23`）锁定。

## 2 双轨设计

**Track 1（铁律现状，0 LLM，可直接执行）**：proxy student 由**确定性变换**构造——对冻结教师侧输出（corpus v20 / benchmark v19/v21 / 5 制品中的教师侧输出，全部只读）施加预注册的退化算子族。算子族候选（D1 从中选定并冻结，可增删）：

- n-gram 截断（保留前 k 元，k 钉死）；
- 词表收缩重写（按冻结词频表截断到 top-v，v 钉死）；
- 温度式重采样（按冻结统计量的类别分布重采样，温度 t 钉死）；
- 嵌入空间投影回归（对冻结教师嵌入做降维投影后回写）。

每一算子 = 一个「蒸馏强度」档位。算子与全部超参在 D1 冻结为纯函数（B3：mode 估计器同纪律，全超参钉死）。0 LLM / 0 proxy / 0 gateway；18 frozen 与 9 网格完全不动（沿 §3.2 路径 B，问卷 L200）。

**Track 2（前提 §3.1 路径 B/C/D 放开，组 C 未拍）**：proxy student 由真 LLM 学生生成（以教师输出为素材的 SFT / 上下文蒸馏）。Track 2 继承 Track 1 的度量与统计层，不重写；**继承风险显式**（B7：Track 2 继承 Track 1 未冻结嵌入——嵌入若已在 Track 1 产生，Track 2 引用时标 `[inherited, not frozen]`）。Track 2 在 §3.1 拍板前不启动。

## 3 素材与路径表（B1 / B2）

教师侧路径集 = `{kimi, GLM_1, GLM_2, coze, minimax}`（B1）。5 件教师素材文件名不一（B2）：D1 冻结**显式 5 路径表**（每教师一条 `path:SHA-12` 锚）入 V4 manifest；后续所有度量只引用该表，不散引。

## 4 度量与分布构造（R5 / B6 修复）

1. **嵌入点 ≠ 分布**（R5）：不直接比较嵌入点；先做**分布构造**，再算分布间距离。
2. 分布构造三选一，D1 预注册并记录选择（B6）：
   - KDE，带宽 h 钉死（Silverman 经验式或固定值，选哪个记哪个）；
   - Voronoi 直方图，锚点集钉死（锚点 = 冻结教师嵌入的预注册子样本）；
   - 闭式度量 sliced-Wasserstein，投影数与随机种子钉死（绕开 binning/KDE 冻结问题）。
3. 主度量 = **JS divergence**；稳健性检查 = **对称 KL**（R5 原文：JS 主度量 + 对称 KL 降稳健性检查）。
4. 全部构造与度量代码为纯函数、全超参钉死、诞生即 SHA-12（B3 + R9 纪律，同 `_verify_15frozen.py` 做法）。

## 5 统计推断（R3 / R6 / R7 / R8）

1. **排列检验** n ≥ 1000：零分布由标签排列生成，锚定 <5% / >95% 分位（R3）；bootstrap CI 同报。
2. **reject 阈值 τ**：用**冻结集外**负对照校准（R6）；复用 V3 P-K FPR 4.4% GRAY 管线作为校准参照。
3. **margin δ = D₂ − D₁**（D₁ = 候选集合与 teacher X 的距离；D₂ = 候选集合与独立对照的距离）；并列 top-2 判 GRAY（R7）。
4. **held-out D1 前冻结**：分割种子、负对照集合、τ、δ 全部在 D1 冻结入 V4 manifest（R8）；测量开始后不改。

## 6 可证伪判据（本题核心）

**最小 claim**：当前度量与构造能把「proxy student（蒸馏式构造）」与「独立构造对照」区分开。

**证伪条件**（预注册，三分支任一成立即 FAIL 并如实落盘）：

- (a) 排列检验在预注册分位上不可分（p 落入 [5%, 95%] 区间）；
- (b) margin δ = D₂ − D₁ 未达预注册阈值；
- (c) 稳健性检查（对称 KL）与主度量（JS）结论翻转。

三分支全不成立 → PASS：最小 claim 在构造域内成立，distillation-detection benchmark 的最小主张获得当前构造 + 度量下的支撑。任一成立 → 最小 claim 被证伪：当前构造 + 度量不足以支撑该主张。

## 7 非独立性、消融与节奏（R4 / R11 / R10）

1. **嵌套非独立性明示**（R4）：18 frozen 锚与 21/22 caption 轴系嵌套非独立结构；报告内显式声明，不做独立样本处理。
2. **消融**（R11）：leave-one-out（逐教师剔除）/ 逐帧消融（caption 逐条剔除）/ caption 排列地板（标签随机化的性能下界）。
3. **节奏**（R10）：一周内三时点——D1（冻结 + Track 1 构造）/ D3（度量 + 排列检验）/ D5（消融 + PASS/FAIL 判定）；不新增嵌入协议（沿用既有嵌入，无新协议）。

## 8 产物清单（V4 独立路径，R9）

| 产物 | 路径 | 诞生纪律 |
|---|---|---|
| 5 教师路径表 | `results/_v4_proxy_student_teacher_paths.json` | D1 冻结，SHA-12 |
| 生成器纯函数 | `results/_v4_proxy_student_generators.py` | D1 冻结，全超参钉死，SHA-12 |
| proxy student 输出集 | `results/_v4_proxy_student_*.json` | 每档位一件，SHA-12 |
| V4 manifest（分割/τ/δ/负对照） | `results/_v4_manifest_distill_min_*.json` | D1 冻结，SHA-12 |
| 度量与检验脚本 | `results/_v4_distill_min_measure.py` | 纯函数，SHA-12 |
| 判定报告 | `results/_v4_distill_min_verdict_*.md` | PASS/FAIL + 证伪判据三分支核对表 |

## 9 KT-B1 KD baseline 勾连（留 PI，沿问卷 L215 注）

问卷 §3.2 注（L215）留 PI 决定 KT-B1 系列 KD baseline（`BAEF94E393DE:83`，"B2 KD 0.0028 / 0.5(占位) / GRAY_BOTH_BELOW"）是否算 V4 学生侧素材。本轮廓默认**不纳入**（该 baseline 的目的是「对照 deposon 失真界」，非 V4 学生侧样本）；若 PI 勾连为纳入，Track 1 增设「既有 baseline 作正类之一」的附加臂，主设计不动。

## 10 待 PI 复核项

1. 双轨设计（Track 1 铁律现状可执行 / Track 2 待 §3.1）：确认或改单轨。
2. 退化算子族（§2 Track 1 四候选）：确认、删减或扩充。
3. 证伪判据三分支（§6）与 margin δ 阈值的预注册值：确认或改定。
4. KT-B1 baseline 勾连（§9）：随 §3.2 注一并裁定。

---

*本稿为 V4 自有资产，诞生即 SHA-12（见落盘后呈报）；LF + 无 BOM。问卷行号对 v1.1 回填前基线（SHA-12 `88F48F82E08B` / 739 行）；所引 L200 / L215 均在本轮回填点 L581 之前，回填后行号不变。*
