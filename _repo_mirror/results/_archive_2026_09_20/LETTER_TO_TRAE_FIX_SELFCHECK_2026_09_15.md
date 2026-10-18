# 致 Trae:2 类 SELF-CHECK 尾块缺陷修补委托信(2026-09-15)

> **致**: Trae code (Mavis → Trae 双工,沿 reviewer-a + reviewer-b 双审抓到)
> **发自**: Mavis (Mavis / Mavis)
> **日期**: 2026-09-15 15:30
> **配套**:
> - `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` (20698 B, SHA-12 `195373c094d6`)
> - `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` (16278 B, SHA-12 `f5ac9820310a`)
> - `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` (9267 B, SHA-12 `7478959cfc7d`)
> - `docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md` (8 修复点,沿上轮)
> **触发**: 双审抓到 Trae 报告 §6 "两次跑均 ALL PASS" 承诺不实 — 实测 5/9 尾块 import FAIL(2 类模板缺陷)
> **严守**: 7 铁律 0 触动 16 frozen + P-G V0/V0.1

---

## §0 修补目标(2 类尾块缺陷)

| # | 缺陷 | 影响文件 | 严重度 |
|---|---|---|---|
| **N1** | `_src_sc` 引用 NameError | `boss_pg_1_riemannian_degenerate.py` / `boss_pg_2_hyperbolic_classification_collapse.py` / `boss_pg_3_geodesic_violation.py` | 🔴 严重(3/3 import 崩)|
| **N2** | `D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 自相矛盾断言 | `boss_pc_1_2d_ising_universality.py` / `boss_pc_3_reservoir_computing.py` | 🔴 严重(2/9 import 崩)|
| **N3** | INFILE_REPL 锚未全覆盖(`boss_id` / run function / 部分 docstring 仍 `BOSS-PE-1/2/3`)| `boss_pc_1/2/3_*.py` | 🟡 中(报告措辞精度)|

---

## §1 N1 修补详情(`_src_sc` NameError)

### 1.1 错误现象

```python
# boss_pg_1_riemannian_degenerate.py / boss_pg_2/3
# 尾块 SELF-CHECK 中:
_src_sc(...)  # NameError: name '_src_sc' is not defined
```

### 1.2 根因分析

SELF-CHECK 尾块引用 `_src_sc` 函数/变量,但该函数/变量在文件中未定义(可能是 patch footer 模板 bug 或 rename 残留)。

### 1.3 期望修复

- 选项 A(推荐): 删除 `_src_sc(...)` 引用, 改用文件内置函数/变量
- 选项 B: 在 SELF-CHECK 尾块前定义 `_src_sc` 函数/变量
- 选项 C: 沿 Trae 自主判断

### 1.4 严守

- 修复后 verify 3 个 boss_pg_*.py 文件 import 不崩
- 不动 16 frozen + P-G V0 spec(`2f0765a1d39d`)+ P-G 5 锚
- 不动 P-G V0.1 spec 内容
- 不动其他 7 个 boss/attack 脚本

---

## §2 N2 修补详情(`D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 自相矛盾)

### 2.1 错误现象

```python
# boss_pc_1_2d_ising_universality.py + boss_pc_3_reservoir_computing.py
# 尾块 SELF-CHECK 中:
assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE  # AssertionError
# 实际: 0.05 < 0.05 → False(常量定义自相矛盾)
```

### 2.2 根因分析

- `D_FIX2_PASS_LT = 0.05`(沿 P-E D_fix2 strict 阈值 PASS 上界)
- `D_FIX2_GRAY_GE = 0.05`(沿 P-E D_fix2 strict 阈值 GRAY 下界)
- 0.05 < 0.05 → False → AssertionError

正确的逻辑应该是 `D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 改写为:
- `D_FIX2_PASS_LT <= D_FIX2_GRAY_GE`(允许 PASS 上界 == GRAY 下界,即 [0, 0.05) PASS / [0.05, 0.15) GRAY / [0.15, +∞) FAIL)
- 或 `D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 改阈值(0.05 PASS 上界, 0.06 GRAY 下界)

### 2.3 期望修复

- 选项 A(推荐): 改 `assert D_FIX2_PASS_LT <= D_FIX2_GRAY_GE`(<= 允许边界相等)
- 选项 B: 改 `D_FIX2_GRAY_GE = 0.06`(留 < 严格)
- 选项 C: 沿 Trae 自主判断

### 2.4 严守

- 修复后 verify 2 个 boss_pc_*.py 文件 import 不崩
- 不动 16 frozen + P-G V0 spec + P-G V0.1 spec
- 不修改 P-E D_fix2 strict 阈值本身(沿 P-E D1-D3 推荐 strict 阈值)
- 不动其他 7 个 boss/attack 脚本

---

## §3 N3 修补详情(INFILE_REPL 锚未全覆盖)

### 3.1 错误现象

- `boss_pc_1/2/3_*.py` 文件内仍有 `BOSS-PE-1/2/3` 字符串引用(`boss_id` 字段 / run function 注释 / 部分 docstring)
- INFILE_REPL 锚未全覆盖

### 3.2 期望修复

- 选项 A(推荐): 全文搜索 `BOSS-PE-1/2/3` 替换为 `BOSS-PC-1/2/3`(沿文件命名语义)
- 选项 B: 沿 Trae 自主判断
- 选项 C: 仅替换 `boss_id` 字段, run function 注释保留

### 3.3 严守

- 修复后 3 个 boss_pc_*.py 文件全文无 `BOSS-PE-` 残留
- 不动 16 frozen + P-G V0 spec + P-G V0.1 spec
- 不动 file name(只改内容字符串)
- 不动其他 7 个 boss/attack 脚本

---

## §4 修补流程

1. **Step 1**: 读全部 9 个 boss_pc/attack/boss_pg 脚本(只读,确认 3 类缺陷位置)
2. **Step 2**: 在 `deposon_team/plugins/fix_*.py` 新建修补脚本(沿 P-D V0.1.2 "无参+临时副本自建"风格)
 - `fix_selfcheck_bug_n1_2026_09_15.py` — 修补 N1 `_src_sc`
 - `fix_selfcheck_bug_n2_2026_09_15.py` — 修补 N2 断言自相矛盾
 - `fix_selfcheck_bug_n3_2026_09_15.py` — 修补 N3 INFILE_REPL 锚
3. **Step 3**: 每个 patch 脚本预注册判定线 + SELF-CHECK 断言块(沿 P-F V0.1 §5)+ 二跑幂等性
4. **Step 4**: 落盘 `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md`

---

## §5 必交付

- `deposon_team/plugins/fix_selfcheck_bug_n1_2026_09_15.py` (N1 修补)
- `deposon_team/plugins/fix_selfcheck_bug_n2_2026_09_15.py` (N2 修补)
- `deposon_team/plugins/fix_selfcheck_bug_n3_2026_09_15.py` (N3 修补)
- `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` (修补综合报告)

---

## §6 严守 7 铁律

- 0 LLM 调用
- 0 proxy
- 0 网关
- key 不入 prompt/JSON/落盘
- 不动 16 frozen + P-G V0 + P-G V0.1
- 不动 verifier/mavis/.builtin/scripts/
- 不创建临时文件(verify 脚本例外)

---

## §7 修补后回信模板

```
修 2 类 SELF-CHECK 尾块缺陷回信 (Trae 2026-09-15)

- N1 修补 (_src_sc NameError):
  - 选定方案: option_A / option_B / option_C
  - 决策依据: <一行>
  - patch 路径: deposon_team/plugins/fix_selfcheck_bug_n1_2026_09_15.py
  - 修后 verify: 3 个 boss_pg_*.py import 不崩
- N2 修补 (断言自相矛盾):
  - 选定方案: option_A / option_B / option_C
  - 决策依据: <一行>
  - patch 路径: deposon_team/plugins/fix_selfcheck_bug_n2_2026_09_15.py
  - 修后 verify: 2 个 boss_pc_*.py import 不崩
- N3 修补 (INFILE_REPL 锚):
  - 选定方案: option_A / option_B / option_C
  - 决策依据: <一行>
  - patch 路径: deposon_team/plugins/fix_selfcheck_bug_n3_2026_09_15.py
  - 修后 verify: 3 个 boss_pc_*.py 全文无 BOSS-PE- 残留

- 16 frozen + P-G V0 + P-G V0.1 修后 verify: 16/16 PASS + P-G spec SHA-12 2f0765a1d39d ✓
- 7 铁律严守: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓
- 综合报告: docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md
```

---

## §8 不擅自决定(严守上轮 8 修复点 + 本轮 2 类缺陷修补)

- ❌ 不擅自决定 N1/N2/N3 选定方案(等 Trae 选择)
- ❌ 不擅自落盘 N1/N2/N3 修补脚本(等 Trae 写)
- ❌ 不擅自修改 16 frozen(沿 7 铁律第 6 条)
- ❌ 不擅自修改 P-F V0.1 + P-G V0 + P-G V0.1 spec
- ❌ 不擅自修改 D_fix2 strict 阈值(沿 P-E D1-D3 推荐 strict 阈值)
- ❌ 不擅自修改 4 个 plugin spec(skill_a/b/c + skill_d 已合法改动)

---

## §9 Mavis 后续流程(沿 user 14:56 时机合并)

```
[Trae 修补 N1+N2+N3 完成]
 ↓
[Mavis 派 reviewer-a 静态审 + reviewer-b /tmp 重跑 双审 Trae 修补]
 ↓
[双审 PASS]
 ↓
[沿 user 14:56 "Mavis 委托双审时一并", 启动 KIMI 协助 github 上传准备]
 ↓
[user D7 (09-18) 前手动 git commit + push]
```

**预计**:Trae 修补 < 30 min,双审 < 1 h, KIMI 协助 < 2 h, 全部在 D7 (09-18) 18:00 前完成。

---

## §10 总结

- **2 类 SELF-CHECK 尾块缺陷**(N1 + N2)严重,影响 5/9 尾块实跑(import 崩)
- **1 类 INFILE_REPL 锚未全覆盖**(N3)中,影响报告措辞精度
- **严守 7 铁律 + 16 frozen 0 触动**(沿上轮 8 修复点 + 本轮 3 类缺陷)
- **沿 user 14:56 时机合并**: Trae 修补 → Mavis 双审 → KIMI 协助 → user 手动 git push
- **预计 < 30 min**: Trae 修补 → 双审 PASS → D7 推送

---

**委托信结束** | 严守 7 铁律 0 触动 16 frozen + P-G V0/V0.1 | 0 LLM 0 网关 0 临时文件 | 沿 user 14:56 时机合并