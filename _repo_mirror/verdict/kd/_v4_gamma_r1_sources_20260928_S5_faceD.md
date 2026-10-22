# γ-R1 面 D 0 命中登记（讲义 / 开放教材面 · worker · 2026-09-28）

> 出证方 = **worker**（本棒执行段），不冒充他方。依预登记件 `02c072833cca` `K-GR1-0-C`：检索不到 ⇒ 如实登记 **0 命中面**（端点 + 检索式 + 时刻 CST + 返回条数 + 0 命中范围）；**0 编造、0 用「应该存在」替代检索**。

## 面 D 登记条目（逐次，含失败）

| # | 端点 | 检索式 / 目标 | 时刻(CST) | 返回 | 命中范围 |
|---|---|---|---|---|---|
| D3 | `https://www.bing.com/search`（通用网页检索，含开放讲义/教材 PDF） | `"sinh(2K)" "sinh(2Gamma)" Ising critical filetype:pdf` | 2026-09-28 17:29:23 | HTTP 200，100,184 B；解析出 13 条外部链接 | **0 命中**：13 条全部为与检索式无关的中文站点（`sinh` 双曲正弦计算器/词条等）⇒ 经本机 tun 出口的区域化检索结果不可用 |
| D5 | `https://www.bing.com/search` | `"sinh(2K)" "sinh(2Gamma)" transverse field Ising exact critical site:arxiv.org` | 2026-09-28 17:30:38 | HTTP 200，101,170 B；解析出 13 条外部链接 | **0 命中**：与 D3 同类区域化无关结果 |
| D4 | `https://www.ulri.kari.fi/publications/lecture-notes.pdf`（开放讲义 PDF 直取，Z. Kari《Introduction to Quantum Computing》） | 直取 PDF（面 D 目标件） | 2026-09-28 17:29:55 | **失败**：`URLError [SSL: UNEXPECTED_EOF_WHILE_READING]` | **0 命中**：端点经本机 tun 代理 TLS 握手被中断，正文 0 取得 ⇒ 该源**未取得任何正文**，**0 判读、0 入级** |

## 面 D 结论

- 面 D 本棒**未取得任何可读讲义/教材全文** ⇒ 面 D 的 `r` 读数贡献 = **0**。
- **0 声称**已核该讲义内容；`K`、`Γ` 在面 D 的定义因子**至今未核**。
- 未覆盖范围：开放教材 PDF（Kardar / Huang 等可公开下载讲义）、大学课程站讲义 PDF —— **本棒未及检索**（STOP-0 预算触顶，见执行件 §3），**不并入「0 命中」计数，仅登记为未覆盖**。

## 诚实边界

本面 3 次尝试均为**真实发出的在线请求**（含 1 次失败握手），已计入执行件 §3 的查询台账；**0 用未查渠道声称 0 命中**（面 B / 面 C 未查者已单列，见执行件 §2）。
