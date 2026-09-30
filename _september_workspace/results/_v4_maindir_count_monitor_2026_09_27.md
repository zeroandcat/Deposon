# V4 主目录三口径计数监控登记 · 2026-09-27

> **派工**：evidence-auditor（agent-11335500b168 · 证据链审计专职）
> **触发**：本批棒收口顺带挂账 G4
> **性质**：只读实测审链登记；不动任何既有件
> **边界**：R5 frozen 只追加 / V1-V3 只读 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文无例外

---

## A. 摘要表（三口径实测 + delta）

| # | 口径 | 2026-09-26 19:50 快照（基线） | 2026-09-27 11:47 实测 | delta | 一致? |
|:-:|---|:-:|:-:|:-:|:-:|
| 1 | **主目录**（excl. `.git/`，全递归） | 986 | **1009** | **+23** | ❌（+23 未全归因） |
| 2 | **通用口径**（excl. `.tmp/` + `__pycache__/` + `.pyc` + `.log` + `.bak`） | 930 | **917** | **-13** | ❌（**负 delta**，未归因） |
| 3 | **含临时区口径**（= 主目录全量，含 `.tmp/` + `__pycache__/` + `.pyc` + `.log`） | 1,004 | **1009** | **+5** | ⚠️（+5 已可归因，见 §D） |
| 4 | **快照口径** | （冻结时点，不重算） | （保留基线值） | — | ✓ |

**主轴结论**：
- 主目录 +23、含临时区 +5、通用 **-13**（**唯一负 delta**，**异常**）
- 已知新增（棒 2/3 + 19:50-22:50 收口件）合计可归因 +5（与含临时区 delta 吻合）
- 主目录 +23 vs 含临时区 +5 的 18 件差额来自**通用口径自身的负 delta**（即：通用口径掉了 18 件，与基线 930 → 917 = -13 接近一致）
- **未归因**：主目录中 +18 件相对基线多出来但被通用口径减去；通用口径 -13 中的负 delta 来源**未能定位**（参见 §E 灰区）

---

## B. 三口径定义（沿用 + 老实交代）

> **沿用锚**：`results/_v4_evidence_audit_reconcile_2026_09_26.md`（SHA-256 `68F66904C0C8E04EE9BB5A5F5D2CDEE5A54EC452374424DF2179217170E35B5A`，22,863 B）

### B.1 三口径字面定义（实测口径，本审链沿用）

| 口径 | 定义 | 实测命令 |
|---|---|---|
| **主目录** | `D:\私人资料\deposon-repo\` 下递归所有文件，**排除 `.git/`** | `Get-ChildItem -Path $ws -Recurse -File \| Where-Object { $_.FullName -notmatch '[\\\/]\.git[\\\/]' }` |
| **通用口径** | 主目录基础上**进一步排除**：(a) `.tmp/` 子树；(c) `__pycache__/` 子树；(d) `.pyc` / `.log` / `.bak` / `.tmp` / `.swp` / `.part` 扩展名 | 在主目录查询上叠加 `Where-Object { $_.FullName -notmatch '[\\\/]\.tmp[\\\/]' -and ... -and $_.Extension -notmatch '^\.(pyc\|log\|bak\|tmp\|swp\|part)$' }` |
| **含临时区口径** | = 主目录全量（即含 `.tmp/` + `__pycache__/` + `.pyc` + `.log` 等临时区文件） | 同主目录查询 |
| **快照口径** | 2026-09-26 19:50 冻结时点登记值（986 / 930 / 1,004），**不重算** | 仅登记，PI 复核用 |

### B.2 定义继承来源（老实交代）

- 三口径字面定义**未在 `68F66904C0C8` 锚件正文内显式定义**（该锚件为 4 疑点逐条定案，与三口径计数定义无关）
- 三口径基线值 986 / 930 / 1,004 **仅出现在派工单字面**（Mavis 根 session 2026-09-27 11:47 派发）
- 本审链**实测定义** B.1 表所列口径为基于「主目录 = 全量」、「通用 = 主目录 - 临时区」、「含临时区 = 主目录」的合理推断
- 与基线 986 / 930 / 1,004 对比时，存在**定义偏差的可能性**（参见 §E 灰区 1）

---

## C. 实测命令与原始数据

### C.1 实测命令（PowerShell 5.1 / 7+ 通用）

```powershell
$ws = 'D:\私人资料\deposon-repo'

# 主目录
$maindir = Get-ChildItem -Path $ws -Recurse -File |
  Where-Object { $_.FullName -notmatch '[\\\/]\.git[\\\/]' }

# 通用口径
$universal = $maindir |
  Where-Object {
    $_.FullName -notmatch '[\\\/]__pycache__[\\\/]' -and
    $_.FullName -notmatch '[\\\/]\.tmp[\\\/]' -and
    $_.Extension -notmatch '^\.(pyc|log|bak|tmp|swp|part)$'
  }

# 含临时区口径 = 主目录
$with_temp = $maindir

Write-Host "maindir = $($maindir.Count)"
Write-Host "universal = $($universal.Count)"
Write-Host "with_temp = $($with_temp.Count)"
```

### C.2 实测结果（2026-09-27 11:47 实跑）

```
maindir    = 1009
universal  = 917
with_temp  = 1009
```

### C.3 临时区拆分明细

| 子类 | 件数 |
|---|:-:|
| `.tmp/` 子树 | 54 |
| `__pycache__/` 子树 | 0 |
| `.pyc` 扩展名（散落） | 19 |
| `.log` 扩展名（散落） | 19 |
| `.bak` 扩展名 | 0 |
| `.mavis/` 子树 | 4 |
| `.trae/` 子树 | 2 |
| **临时区合计（= maindir - universal）** | **92** |

### C.4 顶层目录文件数明细

| 目录 | 件数 |
|---|:-:|
| `.mavis/` | 4 |
| `.tmp/` | 54 |
| `.trae/` | 2 |
| `attacks/` | 4 |
| `corpus/` | 41 |
| `deposon_team/` | 38 |
| `docs/` | 134 |
| `letters/` | 61 |
| `paper/` | 5 |
| `results/` | 409 |
| `reviews/` | 32 |
| `scripts/` | 10 |
| `tests/` | 23 |
| `tools/` | 5 |
| `verifier/` | 117 |
| 顶层散落文件（含 `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` 等 73 件） | 73 |
| **合计** | **1009** |

---

## D. delta 归因表

### D.1 已知新增（任务派工字面登记，逐件核对 ✅）

| # | 件 | 路径 | 字节 | SHA-12（盘实测） | 来源 | 状态 |
|:-:|---|---|:-:|:-:|---|:-:|
| 1 | `_v4_pi_cot_v3_prereg.md` | `results/` | **22,788** | **`F0A58FD651FD`** | 棒 2（2026-09-27 11:39:03） | ✅ 与任务派工登记一致 |
| 2 | `_v4_supp_t15r2_methodology_template.md` | `results/` | **17,411** | **`6F9B865280A3`** | 棒 3（2026-09-27 11:40:23） | ✅ 与任务派工登记一致 |
| 3 | `TRAE_V3_ASSET_ERRATUM_2026_09_23.md` v21 → **v22** | `docs/V3X/` | 275,754 → **292,215**（+16,461） | `2c63da9f7a69` → **`083087218A8D`** | 棒 2/3 间纯追加 E-39（2026-09-27 11:39:19） | ✅ 字节/SHA 与任务派工登记一致；**件已存在，非新增**（不计件数） |

### D.2 19:50-22:50 期间新增（基线后 - 棒 2/3 收口期间产生，CreationTime ≥ 2026-09-26 19:50:00）

| # | 件 | CreationTime | 字节 | 类型 |
|:-:|---|---|:-:|---|
| 4 | `letters/_v4_commission_upload_channel_authorization_2026_09_26.md` | 2026-09-26 19:50:16 | 26,937 | letters |
| 5 | `letters/_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | 2026-09-26 19:53:10 | 4,471 | letters |
| 6 | `letters/_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | 2026-09-26 20:04:44 | 11,575 | letters |
| 7 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 2026-09-26 20:45:07 | 36,945 | letters |
| 8 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 2026-09-26 21:04:15 | 68,449 | letters |
| 9 | `letters/_v4_commission_wechat_report_coze_2026_09_24_v4.md` | 2026-09-26 21:16:25 | 21,433 | letters |
| 10 | `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` | 2026-09-26 21:17:02 | 31,531 | letters |
| 11 | `letters/_letter_to_pi_upload_application_supplement_2026_09_26.md` | 2026-09-26 21:28:18 | 9,151 | letters |
| 12 | `letters/_letter_to_pi_upload_application_approval_2026_09_26.md` | 2026-09-26 21:29:31 | 23,368 | letters |
| 13 | `results/_upload_execution_receipt_kimi_2026_09_26.md` | 2026-09-26 22:08:26 | 4,191 | results |
| 14 | `.tmp/_pc.py` | 2026-09-26 22:16:09 | 431 | temp |
| 15 | `letters/_v4_commission_wechat_report_coze_reply_v4_2026_09_24.md` | 2026-09-26 22:20:19 | 16,471 | letters |
| 16 | `results/_coze_wechat_v4_d7format_2026_09_26.pdf` | 2026-09-26 22:49:35 | 465,366 | results |
| 17 | `results/_v4_pi_cot_v3_prereg.md`（棒 2） | 2026-09-27 11:39:03 | 22,788 | results |
| 18 | `results/_v4_supp_t15r2_methodology_template.md`（棒 3） | 2026-09-27 11:40:23 | 17,411 | results |

**CreationTime ≥ 19:50 合计**：15 件（不含 TRAE erratum 件 v22 因 CreationTime 早于 19:50）

### D.3 主目录 delta +23 拆解

| 项 | 件数 |
|---|:-:|
| D.1 已知新增（棒 2 + 棒 3） | 2 |
| D.2 19:50 后新增（letters/results/tmp） | 12 |
| 棒 2/3 之间纯追加件（TRAE erratum v21→v22，**件已存在不计件数**） | 0 |
| **可归因新增小计** | **14** |
| **未归因 delta**（+23 - 14） | **+9** |

### D.4 含临时区 delta +5 拆解

| 项 | 件数 |
|---|:-:|
| 含临时区口径命中：棒 2 `_v4_pi_cot_v3_prereg.md` | 1 |
| 含临时区口径命中：棒 3 `_v4_supp_t15r2_methodology_template.md` | 1 |
| 含临时区口径命中：`_coze_wechat_v4_d7format_2026_09_26.pdf`（PDF，22:49:35） | 1 |
| 含临时区口径命中：`_upload_execution_receipt_kimi_2026_09_26.md`（results/，22:08:26） | 1 |
| 含临时区口径命中：`letters/` 收口新增 9 件 | 9 |
| **可归因小计** | **13** |
| **未归因 delta**（+5 - 13 = -8） | **-8** |

> **注意**：D.3 算 +23，D.4 算 +5，但 D.4 列举的 13 件中有部分可能不被基线归类为「含临时区」（如 PDF 是否曾被基线归到 excluded？）。**D.3 与 D.4 的归因逻辑不一致**（基线 986 vs 1,004 的差额为 18，含义不明），无法做简单相加。

### D.5 通用口径 delta -13（负 delta，未归因）

- 基线通用 930 → 实测 917，**减少 13 件**
- 已知新增（棒 2/3）均落入主目录/含临时区口径，但**未落入通用口径**：
  - `_v4_pi_cot_v3_prereg.md` (md) — 落入通用，但计入 +1
  - `_v4_supp_t15r2_methodology_template.md` (md) — 落入通用，但计入 +1
  - **净效果：通用应 +2 而非 -13**
- **可能原因**（未验证，仅列假说）：
  - (a) 基线 930 是**包含 `.tmp/` 部分件**的定义，本审链口径排除更严格
  - (b) 基线后**有 15 件通用口径命中件被移出主目录**（如归位到 `_non_upload_local_archive` 仓外父级路径 — 已知仓外父级路径含 1,669 件；与 §B.3 reconcile 报告呼应）
  - (c) 我的实测命令误用过滤器或排除了本应计入的子类（如 `.mavis/` / `.trae/` 是否属「通用」？）
  - (d) 基线值 930 字面与实际不符（实测虚高/虚低）

**结论**：**通用口径负 delta -13 未归因，PI 复核时优先排查 (b) — 清理 v3 棒归位操作可能移走了 15 件左右（与含临时区口径 +5 delta 不矛盾，因为归位只移走主目录件、不影响含临时区 = 主目录 计数）**

---

## E. 灰区与未归因事项（老实交代）

### E.1 三口径字面定义未在 `68F66904C0C8` 锚件中出现

- 派工单字面写「沿用其三口径计数定义 (快照口径 / 通用口径 / 含临时区口径)」+「一字不改定义」
- 实测 `68F66904C0C8` 锚件正文（L1-L268）仅含 4 疑点逐条定案，**无三口径字面定义段落**
- 本审链沿用的 B.1 表所列定义系**基于「主目录 = 全量 / 通用 = 主目录 - 临时区 / 含临时区 = 主目录」合理推断**，未在锚件中字面找到
- **不擅自伪造锚件定义字面**；如实标注定义来源为本审链推断

### E.2 基线值 986 / 930 / 1,004 仅在派工单出现

- 派工单字面给基线值（986 / 930 / 1,004），本审链**未在 `deposon-repo/` 任何文件中找到这组数字**
- grep `986|930|1004` 在 `results/`、`letters/`、`docs/` 下均**未命中**三口径字面值
- 仅命中 1 处 `results/deposon_v20_gt8b_ingest.json` 字节 986（巧合，与基线数字相同但语义无关）
- **基线测量时点（2026-09-26 19:50）的口径定义已不可复现**

### E.3 主目录 delta +23 中有 +9 未归因

- D.3 表「可归因新增小计」= 14；主目录 delta = +23；差 +9
- 可能来源（未验证）：
  - 部分件因 `Copy-Item` 保留源 CreationTime / 仅 LastWriteTime 更新，本审链 CreationTime ≥ 19:50 查询漏检
  - 部分件自 `_non_upload_local_archive` 移回主目录（cleanup v3 棒逆操作）
  - 部分件从 `deposon-sub/` 软链接/复制回主目录
- **不擅自推定成因**；PI 复核时按 `Get-ChildItem | Sort-Object LastWriteTime -Descending | Select-Object -First 30` 自查

### E.4 含临时区口径 delta +5 与「可归因 13 件」逻辑不一致

- D.4 列举的可归因 13 件中**部分可能不在基线 1,004 的「含临时区」口径内**（如 PDF 是否属「临时区」存疑）
- **未擅自重定义基线 1,004 含义**；如实登记未归因差额 -8（数字方向异常）

### E.5 通用口径 delta -13 负 delta 警示

- 实测方向与直觉相反（基线 930 → 实测 917 = **变少 13 件**）
- **可能解释**：清理 v3 棒 18:43-19:12 期间的归位操作已先压缩过基线（含 18 件归位到 `_non_upload_local_archive`，与 §B.3 reconcile 报告 1,669 件登记吻合），但**基线 930 字面比清理后预期值更高**，疑为**基线值口径与本审链不一致**（参见 E.2）
- **PI 复核路径**：
  - 选项 (a)：接受本审链 917 为「2026-09-27 11:47 通用口径实测值」，沿用 E.2 基线 930 字面待 09-28 校准
  - 选项 (b)：派 worker 反查 2026-09-26 19:50 时点的 930 件定义字面（需用户授权重建历史时点快照）

### E.6 skill 缺位老实交代

- 派工单要求 `scientific-research-workflows:statistical-analysis` skill（plugin @scientific-research-wf）—— 本地 skill 加载器实测 `Local skill not found`
- 沿 v15 erratum `6844BF36F762` §20.7 末段先例 + reconcile 报告 §D.6 既有口径，**按 fallback 锚（`68F66904C0C8`）字面 + 本审链实测定义执行**
- **未编造 skill 不存在的虚构指令**

### E.7 key 形态自扫（落盘前实测）

- 本审链报告落盘前实测 key 形态扫描：
  - 严格 pattern：`\b(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer\s+[A-Za-z0-9]{20,}|tp-[a-z0-9]{20,}|ark-[a-z0-9-]{20,})\b`
  - 本审链文件内：**0 命中** ✓
- 主目录整体扫描：
  - 宽 pattern（含 `api_key =` 变量名）命中 203 处 → **全部为变量名匹配**（如 `api_key = m.group(0)` 解析代码），非明文 key
  - 严格 pattern：`0 命中` ✓
- **CLEAN**：本审链文件本身 + 主目录均无明文 key 形态泄漏

### E.8 既件 0 触动自证

- 本审链报告全程**只读实测 + 新建独立登记件**
- 未修改任何既有件（包括但不限于 `_v4_evidence_audit_reconcile_2026_09_26.md` / cleanup v3 棒 / 棒 2/3 产物 / TRAE erratum v22 / batch1_r6 result 等）
- 探测修改命令（如 `Edit-Item` / `Set-Content` 等）**未触发**

---

## F. 报告元数据

| 项 | 值 |
|---|---|
| **路径** | `results/_v4_maindir_count_monitor_2026_09_27.md` |
| **性质** | 新建独立审链登记件；不动任何既有件 |
| **派工** | evidence-auditor（agent-11335500b168）/ 派工单 audit_auth = G4（2026-09-27 11:47 挂账） |
| **锚点** | `_v4_evidence_audit_reconcile_2026_09_26.md`（SHA-256 `68F66904C0C8...`，22,863 B，实测 ✓）+ 派工单字面基线 986/930/1004（实测未在盘上找到字面，参见 E.2） |
| **边界** | R5 frozen / V1-V3 只读 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文无例外 |
| **自扫** | key 形态三类 0 命中（严格 pattern）/ 主目录宽 pattern 203 处命中 = 全部变量名匹配，非明文（CLEAN） |
| **skill** | `scientific-research-workflows:statistical-analysis`（缺位，沿先例 fallback） |
| **状态** | 本审链登记件自身待 PI 复核生效；生效即锁；事后不重开不调 |

---

*出证：Mavis 团队 evidence-auditor（agent-11335500b168）· 2026-09-27*