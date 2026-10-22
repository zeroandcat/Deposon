# -*- coding: utf-8 -*-
"""
_tdf_s2_apply — A 类追加式注记（3 件 rescript）+ B 类新名新件（项 2 修正实现）
授权：委托 §1.2 射程 1（追加式注记 / 新名新件）；0 回改历史行。
幂等：重复运行不重复追加（以标记行探测）。
"""
import hashlib
from pathlib import Path

REPO = Path(r'_repo_mirror'); RES = REPO / 'results'
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

MARK = '附录 · 勘误注记（受托方 Trae code · 2026-10-12'

def append_note(rel, note_body):
    p = REPO / rel.replace('/', os.sep) if False else REPO / rel
    import os
    p = REPO / Path(rel)
    before = p.read_bytes()
    if MARK.encode('utf-8') in before:
        print(f'[skip] {rel} 已含追加节')
        return None
    n = len(before)
    sh = hashlib.sha256(before).hexdigest()
    after = before + note_body.encode('utf-8')
    p.write_bytes(after)
    ok = hashlib.sha256(p.read_bytes()[:n]).hexdigest() == sh
    print(f'[追加] {rel}: {sha12b(before)}({n:,}B) -> {sha12b(after)}({len(after):,}B)  前缀SHA逐字未变={ok}')
    return (sha12b(before), n, sha12b(after), len(after), ok)

import os

# ---------- 项 1 · S2 rescript ----------
n1 = """

---

## 附录 · 勘误注记（受托方 Trae code · 2026-10-12 · 委托件 `_commission_trae_direct_fix_2026_10_09_v0.1.md` 项 1 / C-7 授权）

> **性质**：纯追加。本件 §1–§9 及 L48/L49/L32 历史行**一字不动**（追加前 23,039 B / SHA-12 `331022480a57` 逐字保留）。授权依据：委托件 §1.2 射程 1「追加式注记（新出节 · 0 回改历史行）」+ 项 1②「0 回改 L49 原行」。

### A.1 「用到 19 项特征」之精确化（数字语义勘误）

本件 L49「v3 侧深度 6 / **用到 19 项特征**；复现侧深度 6 / 用到 19 项特征」之「19」为**项次计数（节点×特征出现次数）**，非**特征池大小**。精确表述：

> **19 项次（节点×特征出现次数）／9 distinct；特征池 ＝ v3 既有 12 项。**

### A.2 三读数机检（vs `result_2026_09_27.json`，实测逐位吻合）

| 读数 | 本附录实测 | result 实测位 |
|---|---:|---|
| `v3_n_features`（特征池） | **12** | `construction_equivalence.v3_n_features`（L191 位） |
| `n_features_used_v3`（项次） | **19** | `construction_equivalence.n_features_used_v3`（L195 位） |
| `n_features_used_repro`（项次） | **19** | `construction_equivalence.n_features_used_repro`（L196 位） |

### A.3 distinct 9 项之构成（`features_used_v3` 实测计数）

| 特征 | 项次 |
|---|---:|
| `is_corr_pair` | 3 |
| `opt_bucket_8` | 3 |
| `rf_len_bucket` | 3 |
| `judge_type_J1` | 2 |
| `judge_type_J2` | 2 |
| `judge_type_J3` | 2 |
| `scene_bucket_8` | 2 |
| `n_keywords_hit` | 1 |
| `rf_pos_density` | 1 |
| **合计** | **19 项次 / 9 distinct** |

distinct 9 键集合 ⊆ 委托件项 1③ 所列 9 键（机检 `True`）。

### A.4 边界

- **0 回改** L49/L48/L32 原行；**0 改** `result_2026_09_27.json` 任何读数（19 本身为实测真值，0 是数据错，是**表述**错）。
- 本附录为受托方独立复核结论，**以引述形式**入勘误链，不自动生效。

*追加：受托方 Trae code · 2026-10-12（复算脚本 `deposon_team/plugins/_tdf_s1_2026_10_12.py`，实跑 exit 0）*
"""

# ---------- 项 3 + 项 6 · 短语 rescript ----------
n2 = """

---

## 附录 · 勘误注记（受托方 Trae code · 2026-10-12 · 委托件项 3 / C-9 + 项 6 / B13 授权）

> **性质**：纯追加。本件 §0–§9 及 L20/L171 历史行**一字不动**（追加前 14,510 B / SHA-12 `6df402298557` 逐字保留）。

### B.1 「完整 8 行 T-4 表并报」之精确化（C-9）

本件 L20「v3 / S1 / S2 **完整 8 行** T-4 表 …… **并报，0 省略**」与 L171「完整 8 行并报」之「完整 8 行」系**过度声明**。精确表述：

> **冻结表（`T4_FROZEN_READINGS.rows`）实承 9 个标量，其中 4 键非 T-4 键；相对 S2 之 8 行（`t4_same_substrate_comparison.rows`），缺 3 行。**

**机检读数（实测）**：
- `T4_FROZEN_READINGS.rows` 键数 = **9**：`nw_sim_mean_v3_rule` / `nw_sim_mean_s2` / `nw_sim_mean_v3_construct` / `nled_sim_mean_v3` / `div_critical_coverage_v3` / `blind_obey_rate_v3` / `full_sequence_coverage` / `phrase_coverage_s2` / `n_events_with_multi_step_seq`。
- **非 T-4 键（4 键，委托件项 3③ 字面）**：`nw_sim_mean_s2` / `full_sequence_coverage` / `phrase_coverage_s2` / `n_events_with_multi_step_seq`（计数 = **4** ✓）。
- **S2 有而该表无（3 行）**：bootstrap CI 下界（NW 主读法）、排列检验 `perm_p`（沿 TH-v3-16）、树深（实测）（计数 = **3** ✓）。

### B.2 bit-exact 两读数分列（C-9 附带）

「bit-exact 自证」须**分列两记**，⛔ 0 合写为单一「4/4」：
- **本件（短语预实验）自证面 = 3/3**（L171 字面）；
- **S2 侧 `bit_exact_check` = 4/4**（S2 result 自有读数，另件）。
二者**分记**（原「bit-exact 4/4」口径拼接不再沿用）。

### B.3 短语实现截断之登记与双记（B13）

**机检读数（实测 `PHRASE_PATTERNS_V3`）**：
- 实现结构 = **5 个 dict 元组**（非 10 字符串）：每 dict 含 `pattern`（匹配字面）/ `target_seq` / `v2_anchor`。
- 第 4 类 pattern 字面 = **`大一统定义`**（**只取首项**）；第 5 类 = **`判据序列`**（同）。
- `ruleset_v3.json` 侧字面 = `大一统定义 / 万物理论` 与 `判据序列 / 判据优先序`（含 `/` ⇒ 5 类 = **7 候选式**）。
- ⇒ **`万物理论` / `判据优先序` 在实现面 0 出现为可命中模式**（结构性不可达）——此为**实现截断**，⛔ 非探针失效、非门槛变更。

**双记纪律**：`n_classes` = **5**；`n_patterns_candidates` = **7**；另记 `n_patterns_in_impl` = **5**（实现面 pattern 字面数）。⛔ 互换即错。

**分母差额**：门槛字面分母 85 vs 实测 substrate 77，差额 **8 件** —— **只登记、不动门槛**。

### B.4 边界

- **0 回改** L20/L171 原行；**0 触动** executor 冻结常量 `T4_FROZEN_READINGS`（冻结面）；**0 改** v3 executor `PHRASE_PATTERNS_V3`（是否修实现留 PI 拍板，本附录 0 自裁）。
- 本附录为受托方独立复核结论，以引述形式入勘误链。

*追加：受托方 Trae code · 2026-10-12（复算脚本 `_tdf_s1b/s1c_2026_10_12.py`，实跑 exit 0）*
"""

# ---------- 项 5 · 08c rescript ----------
n3 = """

---

## 附录 · 勘误注记（受托方 Trae code · 2026-10-12 · 委托件项 5 / B11 授权）

> **性质**：纯追加。本件历史行**一字不动**（追加前 15,211 B / SHA-12 `aa02cbfc84e3` 逐字保留）。

### C.1 「与 no-op 同一读数」之两层精确表述（B11）

原措辞「FIX-D 与 no-op 同一读数」精确化为两层：

| 层 | FIX-D（纯幂律零残差） | 恒等族（FIX-B / FIX-B2） |
|---|---|---|
| **门判层**（verdict） | **null**（9/9；本档全 45 run `verdict` 均 null + `verdict_is_null` = True——FROZEN_EVAL_CRITERIA 探索档） | 同归 **null**（9/9 each） |
| **读数层**（delta / r2） | `delta` = **0.0**（9/9 精确成立，`delta_is_defined` = True 9/9）；`r2_full` = `r2_clipped` = **1.0**（DEFINED 9/9） | `delta` = **None**（`delta_is_defined` = False）；`r2` = **None**，`r2_status` = `UNDEFINED_SS_TOT_ZERO` / `UNDEFINED_FLOAT_NOISE`（**未定义**，非 0 亦非 1） |

**恒等族「未定义」的实现形态（如实注明）**：字段**存在**、值 = **None**、状态字 = `UNDEFINED_*`（属「属性存在但值未定义」型；非「属性不存在」、非「读取抛错」）。

### C.2 机检读数（实测 `result_2026_09_27.json`）

- `FIX-D_powerlaw_exact` 9 条：`delta` 取值集 = `{0.0}`（**9/9 逐条 = 0.0** ✓）。
- 恒等族 18 条（FIX-B + FIX-B2 各 9）：`delta` = None、`r2` = None、status = UNDEFINED_* ✓。
- 门判：全 45 run `verdict` = None + `verdict_is_null` = True ✓。

### C.3 边界

- **0 回改**原措辞所在历史行；**0** 将「未定义」改写为任何具体数值（⛔ 0 以估计值/自拟值填充）；**0** 触动 result 落盘值。
- 本附录以引述形式入勘误链。

*追加：受托方 Trae code · 2026-10-12（复算脚本 `_tdf_s1c_2026_10_12.py`，实跑 exit 0）*
"""

r1 = append_note('results/_v3_s2_executor/rescript_2026_09_27.md', n1)
r2 = append_note('results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md', n2)
# 08c rescript 改前值须实测写入注记正文——先实测
p08c = REPO / 'results' / '_v3_recheck_08c_preexp_data' / 'rescript_2026_09_27.md'
b08c = p08c.read_bytes()
pre_sha, pre_n = sha12b(b08c), len(b08c)
print(f'08c rescript 改前实测: {pre_sha} / {pre_n:,} B')
n3 = n3.replace('15,211 B / SHA-12 `aa02cbfc84e3`', f'{pre_n:,} B / SHA-12 `{pre_sha}`')
r3 = append_note('results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md', n3)

print()
print('=== B 类新件：项 2 修正实现（新名新件） ===')
fixer = '''# -*- coding: utf-8 -*-
"""
_v3_recheck_08c_sha12fix_r1_2026_10_12.py — 项 2 / C-8 修正实现（新名新件 · 0 原地改写）
成因登记：08c executor L526 用 `hasattr(ex08b, "sha12_file")` 前缀判空 ⇒ r2_function_sha12 落 null。
事实：ex08b 的哈希函数名为 `sha12`（def sha12(data: bytes)），非 `sha12_file`。
本件：以修正后取法（ex08b.sha12(08b件字节)）产出 r2_function_sha12，并断言 == b292410d9a69。
沿委托项 2③(c)：若仅登记未实现则写明；本件为「已实现」档，跑 exit 0 即自证。
"""
import hashlib, importlib.util, sys
from pathlib import Path

RES = Path(__file__).resolve().parents[2] / 'results'
EX08B = RES / '_v3_recheck_08b_executor' / 'executor_2026_09_27.py'

spec = importlib.util.spec_from_file_location('e08b_r1', str(EX08B))
ex08b = importlib.util.module_from_spec(spec)
sys.modules['e08b_r1'] = ex08b
spec.loader.exec_module(ex08b)

raw = EX08B.read_bytes()
print(f'hasattr(ex08b, "sha12_file") = {hasattr(ex08b, "sha12_file")}')
print(f'hasattr(ex08b, "sha12")      = {hasattr(ex08b, "sha12")}')
val = ex08b.sha12(raw)
print(f'r2_function_sha12 (修正取法) = {val}')
assert val == 'b292410d9a69', f'修正取法产出 {val} != b292410d9a69'
assert hashlib.sha256(raw).hexdigest()[:12] == 'b292410d9a69'
print('ASSERT PASS: r2_function_sha12 == "b292410d9a69"')
'''
fp = RES / '_v3_recheck_08c_preexp_data' / '_v3_recheck_08c_sha12fix_r1_2026_10_12.py'
fp.write_text(fixer, encoding='utf-8')
print(f'新件写入: {fp.name}  SHA-12={sha12b(fp.read_bytes())}')
import subprocess
rc = subprocess.run(['python', '-B', str(fp)], capture_output=True, text=True)
print(f'新件实跑 exit {rc.returncode}:')
for ln in (rc.stdout or '').splitlines():
    print(f'    {ln}')
print('_tdf_s2 DONE')
