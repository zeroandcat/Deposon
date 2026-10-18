# -*- coding: utf-8 -*-
"""
_v4_wt_apply_b4_2026_09_27.py — B4 授权追加勘误注记（纯追加，不回改历史行）
授权：letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md §B.4
目标件：results/_v3_recheck_26_rescript_2026_09_27.md
硬约束：只追加；追加前字节前缀 SHA-256 必须逐字保持；改前改后 SHA-12 全登记。
"""
import hashlib
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
TARGET = REPO / 'results' / '_v3_recheck_26_rescript_2026_09_27.md'

def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]

before = TARGET.read_bytes()
n_before = len(before)
sha_before = sha12(before)
sha_full_before = hashlib.sha256(before).hexdigest()
print('=== 追加前 ===')
print(f'  bytes={n_before}  SHA-12={sha_before}')

APPEND = """

---

## 附录 A · 勘误注记（受托方 Trae code 追加 · 2026-09-27 · 委托件 §B.4 授权「勘误注记」档）

> **性质**：纯追加。本附录**不修改本件 §1–§5 及末行署名任何一字**（追加前 {NB} B / SHA-256 全文 `{SH}` 逐字保留）。授权依据：`letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` §B.4「授权修复（勘误注记）：在第一梯队 rescript **追加**勘误注记节（**追加行，不回改 §3.1 历史行**）」。
> **口径**：本附录全部 SHA-12 = `hashlib.sha256(全文字节).hexdigest()[:12]`（小写）。

### A.1 §3.1 输入字段表 4 行不可复现（受托方独立复核，4/4 不符）

受托方以源 JSON 直接重算，逐行对照（std 取总体标准差 population std；另附 sample std 供对照）：

| §3.1 行 | 声明 (n, n_distinct, std) | 实测 (n, nd, std_pop) | 实测 (n, nd, std_sample) | 判定 |
|---|---|---|---|---|
| P-J `T_frac60` | (9, 9, 0.1198) | (9, **7**, **0.106595**) | (9, 7, 0.113061) | **不符** |
| 60cells `cos_sim` | (9, 6, 0.0648) | (9, **8**, **0.060067**) | (9, 8, 0.063711) | **不符** |
| 60cells `D_fix2_cosine` | (9, 8, 0.0596) | (9, 8, **0.060067**) | (9, 8, 0.063711) | **不符**（nd 同、std 不符） |
| 60cells `T30` | (9, 8, 3.24) | (9, **7**, **3.197221**) | (9, 7, 3.391165) | **不符** |

**源件与取数路径（可复算）**：
- P-J：`results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json`（SHA-12 `a9ad1de618f5`，1,669 B）`all_results.T_frac60` = `[0.8667, 0.8667, 0.7667, 0.7333, 0.7, 0.7, 0.6333, 0.6, 0.5333]`
- 60cells：`results/deposon_v3_physical_opt_60cells_2026_09_11.json`（SHA-12 `c659695aa23c`）`decision_lines_36.in_bin_36[*].cos_sim` 与 `P_C_distortion_bound_60cells.per_model[*].{D_fix2_cosine,T30}`

**旁注（实测）**：`cos_sim` 与 `D_fix2_cosine` 的样本在盘上互为线性变换（`D_fix2_cosine = 1 − cos_sim`），故二者 std **实测相等**（均 0.060067）；而 §3.1 记二者 std 为 0.0648 与 0.0596（**不相等**）⇒ 该差异本身亦为「声明值非由盘上该二字段直接算出」的旁证。

### A.2 根因：**未判定**（如实交代，不编造机制）

受托方对上述两件源 JSON **全树枚举**全部叶子数组，逐一对 `(n, n_distinct, std_pop)` 与 `(n, n_distinct, std_sample)` 两口径做精确匹配 —— **0 命中**：即声明值不来自这两件源件的任何字段、任何常见统计口径。受托方**不代为归因**（未取得第一梯队的计算过程，preexp executor 内亦无该表）。

### A.3 门结论不受影响（不软化也不虚增）

门判据 = `n_distinct > 3`（防退化）**且** `std > 0`。4 行在**实测值**与**声明值**两套数字下**均 pass**（实测 nd 最小 = 7 > 3；实测 std 最小 = 0.060067 > 0）⇒ 本件 §3.1「无退化警报」结论与 `degenerate_alarm_hit = false` **仍成立**；`K-V3R-26` 的判据输入为 `convergence_rate`、**不经这 4 个字段** ⇒ 其判定档位不受影响。
**但「4 行数字不可复现」本身是不利读数，不得隐去**（沿委托件 §B.4「影响面」字面）。

### A.4 本件 §5.1 所留「哈希口径不符」未决项的机制补记（受托方独立定因）

本件 §5.1 记：预登记 §0.2 的 SHA 列「复算 6 种候选哈希输入变体（原始字节 / LF 归一 / 去尾换行 / 加尾换行 / UTF-16 / 路径串）**均不命中**」。受托方另作算法口径探测，**机制已定因**：

> **预登记 v1 的 §0.2 / §0.1「实测 SHA-12」列实为 `hashlib.sha1(全文字节).hexdigest()[:12]`（大写展示），非 `sha256`。**

受托方逐件实算：§0.2 表 **15/15 行**、§0.1 表 **3/3 行**，记值**逐一等于该件的 SHA-1[:12]**（如 `boss_pa_1_rbr_rm_result_2026_09_15.json`：记 `D9E14ED29FB9` = SHA-1，实 SHA-256 = `C7C59E0D2F6C`）。字节列 15/15 逐字一致 ⇒ **非内容变更、非转写错位，系哈希算法口径错用**。复算脚本：`deposon_team/plugins/_v4_wt_s3b_b2confirm_2026_09_27.py`（实跑 exit 0）。

⇒ 本件 §5.1 所述「系统性差异指向哈希输入约定不同」**至此可收口为算法口径（SHA-1 vs SHA-256）**；本件 §5.1 历史行**原样保留、不回改**（沿本件「只追加」纪律）。

### A.5 本附录边界

- **0 授权**重跑第一梯队 executor；**0 授权**改其判定档位；本附录**不改 §3.1 / §5.1 历史行**（只追加本节）。
- 本附录为**受托方独立复核**结果，**以引述形式**入勘误链；是否为正式裁定以 PI 拍板为准。

*追加：受托方 Trae code · 2026-09-27（§B.4 授权档；A.4 系 §B.2 同源机制补记）*
""".replace('{NB}', f'{n_before:,}').replace('{SH}', sha_full_before)

after = before + APPEND.encode('utf-8')
TARGET.write_bytes(after)

# 自证：前缀逐字未变
prefix_ok = hashlib.sha256(TARGET.read_bytes()[:n_before]).hexdigest() == sha_full_before
print()
print('=== 追加后 ===')
print(f'  bytes={len(after):,}  SHA-12={sha12(after)}')
print(f'  前缀 [{n_before:,} B] SHA-256 逐字未变: {prefix_ok}')
print(f'  改前 SHA-12 = {sha_before}  →  改后 SHA-12 = {sha12(after)}')
print('_apply_b4 DONE' if prefix_ok else '_apply_b4 FAILED')
