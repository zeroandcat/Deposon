# Deposon v2X 论文 References [待核] 条目核实报告

- 对象文件：`paper/v2/deposon_paper_v2X.md`（只读，未修改）
- 定位方式：`grep -n "待核"` → 共 **9 条**（[21]、[52]–[59]；正文行 66–74、138 与参考文献行 568、599–606 成对出现）
- 工具：scholar 插件（`/app/.agents/plugins/scholar`）+ web_search 补充交叉验证
- 日期：核实完成于本轮任务

## 裁定总表

| 编号 | 原条目（论文行号） | 裁定 | 证据链接 | 建议修正文本 |
|---|---|---|---|---|
| [21] | Nasr et al., USENIX Sec [待核：年份需核实，应为 2025 或 in-press]（行 568） | **CORRECTED** | https://www.usenix.org/conference/usenixsecurity23/presentation/nasr ；DBLP https://dblp.org/pid/187/8997 ；scholar（USENIX Security 2023, pp. 1631–1648, Distinguished Paper） | Nasr, M., Hayes, J., Steinke, T., Balle, B., Tramèr, F., Jagielski, M., Carlini, N., Terzis, A. "Tight Auditing of Differentially Private Machine Learning." 32nd USENIX Security Symposium (USENIX Security 23), pp. 1631–1648, **2023**。注：未发现 Nasr et al. 在 USENIX Security 2025 的论文；若作者原意是"训练数据抽取"一文（Scalable Extraction of Training Data from Production LMs），其实际 venue 为 **ICLR 2025**（OpenReview: vjel3nWP2a）而非 USENIX Sec，需按此改写。结合上下文「自适应攻击侧…提供方法学合法性」（与 Tramèr et al. NeurIPS 2020 并列），Tight Auditing（DP 审计的自适应攻击方法学）最契合，推荐采用前者。 |
| [52] | McPherson, Smith-Lovin & Cook 2001（同质性综述）（行 599） | **VERIFIED** | https://www.annualreviews.org/content/journals/10.1146/annurev.soc.27.1.415 （scholar 命中，被引 28701） | McPherson, M., Smith-Lovin, L., Cook, J. M. "Birds of a Feather: Homophily in Social Networks." Annual Review of Sociology 27: 415–444, 2001. |
| [53] | Pei et al., Geom-GCN, ICLR 2020（行 600） | **VERIFIED** | scholar（author=Pei, 2020 精确命中，"Proceedings of the 8th ICLR"）；OpenReview: https://openreview.net/forum?id=S1e2agrFvS ；arXiv:2002.05287 | Pei, H., Wei, B., Chang, K. C.-C., Lei, Y., Yang, B. "Geom-GCN: Geometric Graph Convolutional Networks." ICLR 2020. |
| [54] | Zhu et al., H2GCN（Beyond Homophily）, NeurIPS 2020（行 601） | **VERIFIED** | scholar 直检未命中，经大量二手引文及 web_search 确认（NeurIPS 2020, Advances in NIPS 33）；arXiv:2006.11468 | Zhu, J., Yan, Y., Zhao, L., Heimann, M., Akoglu, L., Koutra, D. "Beyond Homophily in Graph Neural Networks: Current Limitations and Effective Designs." NeurIPS 2020. |
| [55] | Zheng et al., 异配图 GNN 综述, 2022（行 602） | **VERIFIED** | scholar 命中（arXiv:2202.07082 PDF 链接，被引 492）；二手引文确认作者全名 | Zheng, X., Liu, Y., Pan, S., Zhang, M., Jin, D., Yu, P. S. "Graph Neural Networks for Graphs with Heterophily: A Survey." arXiv:2202.07082, 2022.（注：后续期刊版见 IEEE TKDE，作者与年份略有更新；2022 对应预印本，条目可保留。） |
| [56] | Luan et al., Revisiting Heterophily, NeurIPS 2022（行 603） | **VERIFIED** | https://arxiv.org/abs/2210.07606 ；NeurIPS 2022 Spotlight https://nips.cc/virtual/2022/spotlight/65009 ；NeurIPS 35: 1362–1375 | Luan, S., Hua, C., Lu, Q., Zhu, J., Zhao, M., Zhang, S., Chang, X.-W., Precup, D. "Revisiting Heterophily For Graph Neural Networks." NeurIPS 2022 (Spotlight), 35: 1362–1375. |
| [57] | Zhang & Chen, SEAL, NeurIPS 2018（行 604） | **VERIFIED** | DBLP https://dblp.org/pid/157/5518 ："Link Prediction Based on Graph Neural Networks. NeurIPS 2018: 5171–5181"；arXiv:1802.09691 | Zhang, M., Chen, Y. "Link Prediction Based on Graph Neural Networks." NeurIPS 2018: 5171–5181.（SEAL 为其中提出的方法名。） |
| [58] | Srinivasan & Ribeiro, 位置嵌入与结构表示等价性, ICLR 2020（行 605） | **VERIFIED** | DBLP https://dblp.org/pid/230/3792 ；OpenReview https://openreview.net/forum?id=SJxzFySKwH ；arXiv:1910.00452 | Srinivasan, B., Ribeiro, B. "On the Equivalence between Positional Node Embeddings and Structural Graph Representations." ICLR 2020. |
| [59] | Mao et al., Demystifying Structural Disparity, NeurIPS 2023（行 606） | **VERIFIED** | 二手引文确认（"Mao, H.; Chen, Z.; Jin, W.; Han, H.; Ma, Y.; Zhao, T.; Shah, N.; Tang, J. 2023. ... NIPS'23"）；arXiv:2306.01323 | Mao, H., Chen, Z., Jin, W., Han, H., Ma, Y., Zhao, T., Shah, N., Tang, J. "Demystifying Structural Disparity in Graph Neural Networks: Can One Size Fit All?" NeurIPS 2023. |

## 统计

- **VERIFIED：8**（[52]–[59]）
- **CORRECTED：1**（[21]，年份应为 2023 而非 2025/in-press；若原意指训练数据抽取论文则 venue 应为 ICLR 2025，需在两者间确认）
- **NOT_FOUND：0**

## 备注

1. 所有 8 条 homophily/GNN 文献（[52]–[59]）条目信息（标题、作者、年份、venue）均与真实文献完全一致，仅需按上表补全标准引用格式（作者全名、页码/编号、可验证链接）。
2. [21] 的两候选（USENIX Sec 2023 Tight Auditing vs ICLR 2025 Scalable Extraction）均为真实文献；建议作者按上下文语义（自适应攻击方法学，与 Tramèr et al. 2020「On Adaptive Attacks」并列）二选一并在 bib 落库时消歧。
3. 论文文件未被修改；本报告为唯一新增文件。
4. **待办（2026-08-30 复审 Minor M4 补记）**：论文文献表 [21] 点名作者序「Nasr, Jagielski, Carlini, Tramèr 等」未按原文作者序（Nasr, Hayes, Steinke, Balle, Tramèr, Jagielski, Carlini, Terzis）；现带「等」可容忍。bib 尚未落库（`paper/references.bib` 无 Nasr 条目），bib 落库时应按原文作者序著录，或只留首作者 + et al.，届时再同步文献表条目，不在本轮强行重排。
