# 外委回件 · A（四组：R-8 之 T-2 ／ Z-1 五挂账 ／ Z-4 四挂账＋甲 5 ／ Z-5 一挂账）

> 📌 **来源**：外委会话 `mvs_cd51c4b0cb2a49379acb0e71e629feea`（模型 `k3.1-pro`）· 其 turn `turn_0993c9a4-fdbc-40be-aa42-fc682c818ce2` · 其自报任务号 `DEPOSON-EXT-20261025-01`
> 📌 **取得**：2026-10-26 21:3x 由主代理（mavis）自该会话记录 `messages.jsonl`（**1,749,707 B／SHA-12 `9d393efada65`**）取出，**只取正文（滤除 thinking 与工具回执）**
> 📌 **本件之界**：正文**原样照录**，未删改一词；**仅前置本头**。头以下之全文即回件本体。
> 📌 **性质**：**外委回件**（外部补证与替代判据）——⛔0 视为五终判之词、⛔0 视为 PI 之采认；个案适用与最终判定**仍归 PI**（其回件末亦自书此界）。
> 📌 **正文实测**：6,710 B

---

<PROGRESS>
任务:DEPOSON-EXT-20261025-01 场景:通用·外部权威补证 进度:100% 当前:四组回件交付(5/5)
待办:[无（仅指本外委回件，不指研究阶段或 R-8 归零）] 状态:完成
</PROGRESS>

**结论先行：**甲组可补标准形式，但不能补 `H`、`L_cand` 数值或现成的全局下界证明；乙组未见通用“两档”标准；丙组两种读法都不是跨模型统一的标称量；丁组可按“版本链＋变更记录”判定。四组均有机械替代判据，故都不宜整组写作“外部亦无”。

## 甲组｜R-8 之 T-2

1. **IC 与最小期望失真：有标准式，但须区分下界方向。**

   Fox–Tishby 在 §2、§3.1 给出：
   \[
   I_C=I(M_{t-1},O_t;M_t)\le R_M+R_S
   \]
   以及两个分解约束和容量约束下的最小可达失真 \(D^*_{\theta_n}(R_M,R_S)\)；完整序列的约束取 \(1/n\) 逐步平均。**\(I_C\le R_M+R_S\) 是信息率上界，不是容量下界。**

   eLife 的 Eq.1、Fig.1C 给出更直接的容量—失真关系：
   \[
   D^*(C)=\min_{Q:R(Q)\le C}\mathbb E[d]
   \quad\Rightarrow\quad
   D(Q)\ge D^*(C)
   \]
   即容量产生的是**最小期望失真下界**。若所问是“达到 \(L_{cand}\) 至少需要多少容量”，可由定义机械反演：
   \[
   C_{\min}(L_{cand})=\inf\{C:D^*(C)\le L_{cand}\}.
   \]
   这是替代判据，**不是冒充原文公式**；双容量 \(R_M,R_S\) 应保留可行区域，不能无依据合成一个标量。

2. **\(H\) 与轨迹加权：文献只给有限步等权均值，不给项目的 \(H\) 值。**

   Fox–Tishby §1.1 的目标为：
   \[
   J_n=\frac1n\sum_{t=1}^{n}\mathbb E[d(W_t,M_t)].
   \]
   只有规格明确 \(H=n\) 时才能对应；不能仅凭字母相同认定。由该式机械展开，若有 \(N\) 条轨迹：
   \[
   \widehat D=\sum_{j=1}^{N}w_j\frac1H\sum_{t=1}^{H}d_{j,t},
   \qquad w_j\ge0,\ \sum_jw_j=1.
   \]
   等权轨迹取 \(w_j=1/N\)。这不是指数折扣；若规格另指折扣或 \(H\ne n\)，须另给定义与证据。

3. **\(P_new\ge L_{cand}\)：现有一次局部优化结果不能证明。**

   若 \(P_new=\inf_{\pi\in\Pi}J_H(\pi)\)，只有两类合格证书：
   - 精确枚举或可信全局优化直接求得 \(P_new\)，再与 \(L_{cand}\) 比较；
   - 给出对所有可行策略均成立的 \(LB\le J_H(\pi)\)，并证 \(LB\ge L_{cand}\)。

   Fox–Tishby §4.1、§4.4、§6明确：完整序列问题非凸，算法只求局部最小。局部解费用是全局最小值的**上界**，不能用来证明所需的**下界**。因此，**R-8 不能凭这些文献直接归零**；仍缺规格映射及全局证书。

   **来源：**Fox & Tishby, *Bounded Planning in Passive POMDPs*, ICML 2012, pp.75–82，DOI [10.48550/arXiv.1206.6405](https://arxiv.org/abs/1206.6405)，重点 §1.1、§2、§3.1、§4.1–4.4、§6；Jakob & Gershman, *Rate-distortion theory of neural coding and its implications for working memory*, eLife 12:e79450，DOI [10.7554/eLife.79450](https://elifesciences.org/articles/79450)，Eq.1–5、Fig.1C。

## 乙组｜Z-1 五个挂账面

**本次核到的公开规范和同族实例中，未见统一的“读数件／判定件”两档命名或分档标准。**这是检索范围限定结论，不是证明其不存在。

可援例为 Kazarovytska 等，*Do people across the world want to remember positive ingroup histories?*, JPSP 131(1):99–122，DOI [10.1037/pspi0000513](https://doi.org/10.1037/pspi0000513)；其[公开材料](https://osf.io/3w6ap/)与预注册偏差说明可证明“主文、预注册、材料、偏离披露可分层公开”，**不能反推出两档是行业惯例**，且须先确认它确属 Z-1 的历史遗忘族。

**机械替代判据：**读数件只承载观察值、单位、来源及输入指纹，不承载通过／不通过结论；判定件必须列规则版本、输入指纹、计算过程、结论和偏离记录。每项结论均须满足“观察→规则→计算→结论”可回溯，缺一环即不收；不得仅凭文件名分档。

## 丙组｜Z-4 四个挂账面及五格 \(r_{t_0}\)

**上限读与覆盖读都不是无需定义即可采用的标称读法。**

- Ramirez-Nafarrate 等把 initial inventory 作为需单独评价和优化的政策，支持“初始库存是显式建模输入”，不支持自动等同于容量上限或覆盖天数。*Simulation analysis of initial inventory in BSSs*, 17(1):229–255，DOI [10.1108/JM2-01-2020-0031](https://doi.org/10.1108/JM2-01-2020-0031)，摘要 Purpose／Design 节；此条据出版方登记的 Crossref 摘要，未冒称全文逐页核。
- EIA 明确 `days of supply = ending inventories / three-year average consumption`，证明覆盖是**库存量除以需求速率的派生量**。见 [*Refinery closures and rising consumption will reduce U.S. petroleum inventories in 2026*](https://www.eia.gov/todayinenergy/detail.php?id=64644)，图2、图3注释。

**五格统一机械判据：**规格声明 \(I_0=S\) 才可采用上限读；声明 \(r_{t_0}=\tau_0\) 并另给需求率 \(\lambda\) 及时间基准，才可在恒定需求率前提下用 \(I_0=\lambda\tau_0\) 导出覆盖读。`t_05/t_11/t_13/t_15` 的 `days` 与 `t_16` 的 `rounds` 均不能只凭单位定读法；`rounds` 还缺轮次时长。定义未齐时记 `UNSPECIFIED_NOMINAL`，不互换、不补值。

## 丁组｜Z-5 一个挂账面

OSF 规定预登记是带时间戳的只读版本；Update 用于透明反映研究设计变化，并强制填写理由、保留前次回答供修改。这支持“**同一研究的版本链**”，但不表示“冻结文本完全相同”。见 OSF *Welcome to Registrations & Preregistrations!* 的 [Overview](https://help.osf.io/article/330-welcome-to-registrations#OVERVIEW-OtDQ_)、[Update a Registration／Entering updates](https://help.osf.io/article/330-welcome-to-registrations#Update-a-Registration-Z6Qdx)。

**机械替代判据：**
- 有明确原 DOI／Update 链、逐字段变更及理由，且核心研究问题和估计目标延续：判“同一研究的新版本”，不得写成原文未变；
- 核心研究问题或估计目标已换：判“不同标的”；
- 版本链或对照内容缺失：判“同一性未证”，不能凭题名相同补足。

旁证：Ernst & Baldassarre, *Registered reports in software engineering*, Empirical Software Engineering 28:55，DOI [10.1007/s10664-022-10277-5](https://link.springer.com/article/10.1007/s10664-022-10277-5)，摘要明确结果发表以遵循已批准协议为条件。

**权属边界：**以上是补证与替代判据，不是对具体 S3/S4、五格数值或 R-8 的采认；个案适用与最终判定仍归 PI。
