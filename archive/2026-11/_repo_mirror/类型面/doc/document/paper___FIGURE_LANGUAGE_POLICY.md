# Figure Language Policy（图语言纪律）

本仓库论文同时维护中文版与英文版。为避免图语言与正文语言混用，制定以下纪律：

## 规则

1. **英文版论文只用英文图**：英文版稿件（如 `deposon_paper_v1_en.md`）引用的所有图，其图内标注必须全部为英文，不得出现中文字符。
2. **中文版论文只用中文图**：中文版稿件（如 `deposon_paper_v1.md`）引用的图，其图内标注使用中文。
3. **图文件名必须带语言后缀**：凡含文字标注的图，文件名须以 `_cn`（中文）或 `_en`（英文）结尾，例如 `fig1_architecture_cn.png` / `fig1_architecture_en.png`。历史上无后缀的 `fig1_architecture.png` 视为 `_cn`（中文图），仅允许中文版引用。
4. **禁止共享图**：同一图文件不得被中文版与英文版同时引用。同一内容需为两种语言各绘制一份图，布局与风格保持一致。
5. 新增图时：先确定目标语言版本，按对应语言绘制，命名加后缀，并在对应稿件中引用。

## 1.X 混用案例与修复记录

- **问题**：`paper/fig1_architecture.png` 为全中文标注的架构图（五级流水线 + 三通道散射），同时被中文版 `deposon_paper_v1.md`（合理）与英文版 `deposon_paper_v1_en.md`（第 87 行附近，**混用**）引用。
- **修复**（本次）：
  1. 用 matplotlib 按相同布局与风格绘制全英文标注的 `paper/fig1_architecture_en.png`（figsize 16×9，dpi=220，2771×1568 px）。
  2. 将 `deposon_paper_v1_en.md` 第 87 行的图引用从 `fig1_architecture.png` 改为 `fig1_architecture_en.png`，其余内容不变。
  3. 中文版 `deposon_paper_v1.md` 第 91 行仍引用 `fig1_architecture.png`，保持不变。
- **后续建议**：择机将 `fig1_architecture.png` 重命名为 `fig1_architecture_cn.png` 并同步更新中文版引用，彻底落实命名后缀规则。

## v2X 五图命名与链接记录（2026-08-30）

- v2X 中文稿附录 D 的五张新图已按规则 3/5 加 `_cn` 后缀：`figures/fig1_boundary_map_cn.png`、`fig2_killsign_scatter_cn.png`、`fig3_division_scatter_cn.png`、`fig4_gt7_frontier_cn.png`、`fig5_poa_distribution_cn.png`；生成脚本 `tools/make_figures_v2.py` 输出名与 `docs/FIGURES_v2.md` 记录已同步。
- `paper/v2/deposon_paper_v2X.md` 的图片链接以 `paper/v2/` 为渲染基准写作 `../../figures/figN_*_cn.png`，保证 PDF 构建或文件页预览不断链。
