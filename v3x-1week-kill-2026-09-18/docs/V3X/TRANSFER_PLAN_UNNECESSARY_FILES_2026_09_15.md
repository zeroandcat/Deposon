# D:\私人资料\deposon-repo 共享母目录转移计划(2026-09-15)

> **触发**: user 2026-09-15 15:40 "转移不必要的文件,共享母目录太大了"
> **沿**: user 14:54 "minimax 的生态太烂了"
> **作者**: Mavis
> **日期**: 2026-09-15 15:40
> **严守**: 7 铁律 0 触动 18 frozen + P-G V0 + P-G V0.1

---

## §0 共享母目录现状

- **D:\私人资料\deposon-repo\**
 - **总大小**:**299.74 MB**(1653 files)
 - 顶层目录按大小排序:
 1. **`.mavis/` 234.15 MB(78.1%)** ← 最大
 2. `.trae/` 27.99 MB(9.3%)
 3. `paper/` 15.96 MB(5.3%)
 4. `results/` 9.58 MB(3.2%)
 5. `figures/` 4.92 MB(1.6%)
 6. `docs/` 2.32 MB(0.8%)
 7. 其他 < 1 MB

---

## §1 `.mavis/` 详细分解(234.15 MB, 78%)

| 子目录 | 大小 | 文件数 | 内容 | 评估 |
|---|---|---|---|---|
| **`.mavis/installers/`** | **203.97 MB** | 4 | agent 工具 installers(node_modules / Python venv / IDE 安装) | 🔴 **可全部转移**(非项目必要) |
| `.mavis/cache/rendered_arxiv/` | 11.84 MB | 47 | arxiv 渲染缓存 | 🟡 可清理(可重新生成) |
| `.mavis/backups/` | 10.07 MB | 10 | minimax agent 备份 | 🟡 可转移到外部(用户工作区外) |
| `.mavis/cache/deposon_arxiv_2026/figures/` | 3.61 MB | 10 | arxiv figures 缓存 | 🟡 可清理(可重新生成) |
| `.mavis/cache/pdfbuild/` | 2.52 MB | 69 | pdfbuild 中间文件 | 🟡 可清理(最终 PDF 在 `paper/`) |
| `.mavis/cache/pdfbuild/fonts/` | 1.03 MB | 60 | 字体缓存 | 🟡 可清理 |
| `.mavis/logs/` | 0.49 MB | 219 | minimax agent logs | 🟡 可转移(诊断用,可不留项目内) |
| `.mavis/proposals/` | 0.56 MB | 3 | minimax agent 提案 | 🟡 可转移 |
| `.mavis/scripts/` | 0.55 MB | 127 | minimax agent 脚本 | 🟡 可转移 |
| `.mavis/cache/deposon_arxiv_2026/` | 3.77 MB | 13 | arxiv 缓存 | 🟡 可清理 |
| `.mavis/reports/` | 0.03 MB | 2 | minimax reports | 🟡 可转移 |

---

## §2 可转移 candidates(按优先级)

### 2.1 🔴 **优先级 1(必转)**:`.mavis/installers/` 203.97 MB

**理由**:
- 占整个项目 68%
- agent 工具 installers(node_modules / Python venv / IDE)— 非项目必要
- 沿 user 14:54 "minimax 生态太烂了" — minimax 工具不应污染项目目录

**转移目标**(待 user 拍板):
- 选项 A:`D:\私人资料\_mavis_external\`(用户工作区外)
- 选项 B:`D:\_mavis_external\`(D 盘根)
- 选项 C:`C:\Users\Administrator\AppData\Local\minimax\`(用户家目录)
- 选项 D:删除(如果能重新下载)

**风险评估**:
- ⚠️ 转移后,minimax agent 工具可能无法使用(因为不在路径)
- ✅ 但项目本身不依赖 minimax agent 工具(沿 7 铁律,严守 0 网关 0 LLM)
- ✅ 转移后,可让 minimax agent 工具通过 symlink 或环境变量重新找到

### 2.2 🟡 优先级 2(可清理):`.mavis/cache/` 内 6 个子目录

**总大小**:**~24.8 MB**
- `cache/rendered_arxiv/` 11.84 MB(可重新生成)
- `cache/deposon_arxiv_2026/figures/` 3.61 MB(可重新生成)
- `cache/pdfbuild/` 2.52 MB(可重新生成)
- `cache/pdfbuild/fonts/` 1.03 MB(可重新生成)
- `cache/deposon_arxiv_2026/` 3.77 MB(可重新生成)

**理由**:
- 都是 arxiv 渲染/pdfbuild 缓存
- 中间文件,最终产品在 `paper/` 和 `figures/`
- 不会影响项目本身

**转移/清理选项**:
- 选项 A:删除(节省 24.8 MB)
- 选项 B:转移到 `D:\私人资料\deposon-repo\_archive\cache\`
- 选项 C:保留(不主动清理)

### 2.3 🟡 优先级 3(可转移):`.mavis/backups/` 10.07 MB

**理由**:
- minimax agent 备份(对话历史 / 状态快照)
- 沿 7 铁律第 7 条不严守 `.mavis/`(只严守 `.minimax/agents/...`)
- 但 minimax agent 备份不应在项目目录

**转移选项**:
- 选项 A:转移到 `D:\私人资料\_mavis_external\backups\`
- 选项 B:保留(不主动转移)

### 2.4 🟡 优先级 4(可转移):`.mavis/{logs,proposals,scripts,reports}/` 共 ~1.6 MB

**理由**:
- minimax agent 内部文件
- 沿 user 14:54 "minimax 生态太烂了" — minimax 不应在项目目录

**转移选项**:
- 选项 A:一起转移到 `D:\私人资料\_mavis_external\`
- 选项 B:保留(诊断用)

### 2.5 🟡 优先级 5(可清理):`.tmp/`, `.tmp_volcengine_2026_09_10/`, `__pycache__/`, `.pytest_cache/`

**总大小**:**~200 KB**
- `.tmp/` 90 KB
- `.tmp_volcengine_2026_09_10/` 61 KB
- `__pycache__/` 46 KB
- `.pytest_cache/` 896 B

**理由**:
- 临时文件 / Python 缓存 / pytest 缓存
- 沿 7 铁律第 8 条"不创建临时文件"原则,这些是历史遗留
- 不影响项目

**清理选项**:
- 选项 A:删除(节省 ~200 KB)
- 选项 B:保留

### 2.6 🟡 优先级 6(可选):`.trae/` 27.99 MB(109 files)

**理由**:
- Trae 工具目录(沿 LETTER_TO_TRAE 修复过程中的工具)
- 与 `.mavis/` 类似,minimax 生态
- 但 Trae 修复有持续价值(沿 user 14:56 时机合并的 KIMI 上传准备)

**转移选项**:
- 选项 A:转移到 `D:\私人资料\_trae_external\`
- 选项 B:保留(可能 Trae 后续还需用)

### 2.7 🟡 优先级 7(可清理):`paper/_paper_backup_v181/` 0.41 MB

**理由**:
- 已 superseded 的论文备份(v181 → 当前 v183?)
- 沿 _paper_backup 命名,已 superseded

**清理选项**:
- 选项 A:删除(节省 0.41 MB)
- 选项 B:保留(历史归档)

---

## §3 不可动(严守 7 铁律 + 18 frozen)

| 路径 | 状态 |
|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (03c6c01f3697) | ❌ 0 触动 |
| 4 SPEC V0.1 (`78b71d404366` / `0410ca0fbdae` / `59d8f56347d5` / `cce8e9a1b00e`) | ❌ 0 触动 |
| P-F V0.1 upgrade `b10fae0da66d` | ❌ 0 触动 |
| v19 / v21 / corpus_v20 | ❌ 0 触动 |
| P-F V0 / placeholder / research | ❌ 0 触动 |
| 4 plugin spec(`b1463bb24403` / `e5a299f69a22` / `e19e76c5da7e` / `3e369a1f6171`) | ❌ 0 触动 |
| P-G V0 spec `2f0765a1d39d` | ❌ 0 触动 |
| `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | ❌ 0 触动(只读)|
| `.minimax/agents/{verifier,mavis,.builtin,scripts}/` | ❌ 0 触动(7 铁律第 7 条)|

---

## §4 转移计划(待 user 拍板)

### 4.1 默认建议计划

| 操作 | 候选 | 大小 | 风险 | 推荐度 |
|---|---|---|---|---|
| 🔴 必转 | `.mavis/installers/` | 203.97 MB | ⚠️ 转移后 minimax agent 工具可能失效 | ✅ 强烈推荐(68% 节省) |
| 🟡 可清理 | `.mavis/cache/`(6 子目录)| 24.8 MB | 极低(可重新生成) | ✅ 推荐 |
| 🟡 可转移 | `.mavis/backups/` | 10.07 MB | 低(诊断损失) | 推荐 |
| 🟡 可转移 | `.mavis/{logs,proposals,scripts,reports}/` | 1.6 MB | 低(诊断损失) | 推荐(与 backups 一起) |
| 🟡 可清理 | `.tmp/`, `.tmp_volcengine_*/`, `__pycache__/`, `.pytest_cache/` | 200 KB | 极低 | 推荐 |
| 🟡 可选 | `.trae/` | 27.99 MB | ⚠️ Trae 后续修复可能需用 | 看 user 需求 |
| 🟡 可选 | `paper/_paper_backup_v181/` | 0.41 MB | 极低 | 视情况 |
| **总计可节省** | | **268 MB(89%)** | | |

### 4.2 转移目标建议

| 优先级 | 目标 | 理由 |
|---|---|---|
| 选项 A(推荐)| `D:\私人资料\_mavis_external\` | 用户工作区内的 minimax 独立空间,环境变量易配 |
| 选项 B | `D:\_mavis_external\` | D 盘根,完全独立 |
| 选项 C | `C:\Users\Administrator\AppData\Local\minimax\` | 用户家目录下的标准 minimax 位置 |

### 4.3 转移后效果

- **D:\私人资料\deposon-repo**:从 299.74 MB → ~32 MB(节省 89%)
- **D:\私人资料\_mavis_external**:新增 268 MB
- 净效果:minimax 工具独立,不污染项目目录

---

## §5 严守 7 铁律声明

| 铁律 | 状态 |
|---|---|
| 1. 0 LLM 调用 | ✓ 严守(本任务纯目录分析)|
| 2. 不设 proxy | ✓ 严守 |
| 3. 不调网关 | ✓ 严守 |
| 4. key 不入 prompt/JSON/落盘 | ✓ 严守 |
| 5. 不动 5 锚 JSON | ✓ 严守(`03c6c01f3697` 0 触动)|
| 6. 不动 4 SPEC V0.1 + v19/v21 + corpus_v20 + 16 frozen + P-G V0 + P-G V0.1 | ✓ 严守 |
| 7. 不动 verifier/mavis/.builtin/scripts/ | ✓ 严守(.minimax/agents/... 0 触动)|
| 8. 不创建临时文件 | ✓ 严守(本任务纯分析,无文件创建)|

---

## §6 不擅自决定(等 user 拍板)

- ❌ 不擅自转移任何文件(等 user 拍板 transfer candidates + 目标位置)
- ❌ 不擅自删除任何文件(等 user 拍板)
- ❌ 不擅自修改 18 frozen + P-G V0 spec + P-G V0.1 spec
- ❌ 不擅自移动 4 plugin spec / 4 SPEC V0.1 / 5 锚 JSON
- ❌ 不擅自决定 minimax agent 工具转移目标位置(等 user 拍板)

---

## §7 等 user 拍板

```
Mavis 转移计划(沿 user 14:54 "minimax 生态太烂了"):

🔴 必转 (建议):
  1. .mavis/installers/ → ? MB
     目标: A (D:\私人资料\_mavis_external\) / B (D:\_mavis_external\) / C (C:\Users\...\AppData\Local\minimax\) / D (删除)

🟡 可清理(建议):
  2. .mavis/cache/ 6 子目录 → 24.8 MB
     操作: A (删除) / B (转移到 _archive\cache) / C (保留)

  3. .tmp/ + .tmp_volcengine_*/ + __pycache__/ + .pytest_cache/ → ~200 KB
     操作: A (删除) / C (保留)

🟡 可转移(建议):
  4. .mavis/backups/ → 10.07 MB
     操作: A (转移到 _mavis_external\backups) / C (保留)

  5. .mavis/{logs,proposals,scripts,reports}/ → 1.6 MB
     操作: A (与 backups 一起) / C (保留)

🟡 可选:
  6. .trae/ → 27.99 MB
     操作: A (转移到 D:\_trae_external) / C (保留, Trae 后续可能需用)

  7. paper/_paper_backup_v181/ → 0.41 MB
     操作: A (删除) / C (保留)

默认推荐计划(若 user 选 A 全部):
- 总节省 268 MB(89%)
- 转移目标: D:\私人资料\_mavis_external\
- 风险: minimax agent 工具失效,但项目本身不依赖
```

---

**转移计划完成** | 总 299.74 MB → 可节省 268 MB(89%)| 严守 7 铁律 0 触动 18 frozen | 沿 user 14:54 "minimax 生态太烂了" | 等 user 拍板具体转移 candidates + 目标位置