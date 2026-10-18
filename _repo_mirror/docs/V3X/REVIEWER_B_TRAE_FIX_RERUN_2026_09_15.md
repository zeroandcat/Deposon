# Reviewer-b /tmp 重跑 Trae 修复关键实算 (2026-09-15)

> **委托**: Mavis 父会话 (沿 user 2026-09-15 14:56 "Mavis 委托双审时一并"),沿委托信 `LETTER_TO_TRAE_REVIEW_2026_09_16.md` §12 复审纪律
> **执行**: reviewer-b Worker(branch 子会话)
> **任务 ID**: REVIEWER-B-TRAE-FIX-RERUN-2026-09-15
> **方法**: 0 LLM / 0 proxy / 0 网关 / 0 key; 纯 Python stdlib; /tmp 临时副本例外(验证后清理)
> **范围**: 3 个 patch 脚本 (fix_boss_naming / fix_verify_freeze_policy / fix_proactive_audit) + 9 个 SELF-CHECK 尾块 (boss_pc_1/2/3 + attack_pc_a1/a2/a3 + boss_pg_1/2/3)
> **不动**: 16 frozen + P-G V0 + P-G V0.1 + verifier/mavis/.builtin/scripts/(只读)

---

## §0 TL;DR — 关键结论

| # | 关键实算项 | 比对结果 | 备注 |
|---|---|---|---|
| 1 | `fix_boss_naming_2026_09_16.py` 二跑幂等性 | **PASS** | 20/20 mutable 文件 UNCHANGED + 16 frozen 后置 0 触动 |
| 2 | `fix_verify_freeze_policy_2026_09_16.py` 二跑幂等性 | **PASS** | 同上 |
| 3 | `fix_proactive_audit_2026_09_16.py` 二跑幂等性 | **PASS** | 同上 |
| 4 | boss_pc_1/2/3 + attack_pc_a1/a2/a3 + boss_pg_1/2/3 SELF-CHECK 尾块 实跑 | **FAIL (5/9)** | **捕获 2 类 patch footer() 模板缺陷**(详见 §3) |
| 5 | 16 frozen 修后 verify (含 P-G V0 / V0.1) | **PASS** | 16/16 全 PASS |

**整体裁定**:
- **patch 脚本本身** (修复点 1/2/3/4/5/6 + 主动审查 A1/A2/B4/B5/B6/C7) **修后双跑幂等性全 PASS**
- **SELF-CHECK 尾块实跑** 暴露 5 个 FAIL — Trae 报告 §6 "两次跑(首跑执行 + 复跑幂等)均 ALL PASS" 的承诺与实跑不符(patch 脚本内置 SC 只做 `compile()`,未实际执行尾块)
- **建议**: Mavis 复审时将 5 个 FAIL 退回 Trae 修 footer() 模板(2 类 bug, 修复预计 < 30 行); 16 frozen + patch 幂等性 PASS 可保留不动

---

## §1 /tmp 副本设置

| 项 | 值 |
|---|---|
| 临时根目录 | `D:/tmp/deposon_reviewer_b_trae_2026_09_15/` |
| 镜像子目录 | `D:/tmp/deposon_reviewer_b_trae_2026_09_15/deposon-repo/` |
| 镜像内容 | `deposon_team/` + `docs/` + `results/` + `verifier/` + `corpus/` (全量递归) |
| 文件总数 | 764 个文件 |
| 验证后处置 | 见 §5 清理步骤(保留至报告落盘后清理) |

**BASE 覆写**: 3 个 fix 脚本的 `BASE = r'D:\私人资料\deposon-repo'` 在 /tmp 副本内覆写为 `BASE = r'D:\tmp\deposon_reviewer_b_trae_2026_09_15\deposon-repo'`; 验证完已恢复原值。

---

## §2 patch 脚本二跑幂等性比对

### 2.1 baseline frozen 16 (0 触动声明前提)

执行 3 patch 脚本前,先核验 /tmp 副本内 16 frozen 文件 SHA-12 全部匹配期望值:

```
verifier/handoff/KT_ABC1_anchors_sha256_12.json  03c6c01f3697  ✓
docs/V3X/KT_A1_SPEC_V0.1.md                      78b71d404366  ✓
docs/V3X/KT_B1_SPEC_V0.1.md                      0410ca0fbdae  ✓
docs/V3X/KT_C1_SPEC_V0.1.md                      59d8f56347d5  ✓
docs/V3X/KT_D0_SPEC_V0.1.md                      cce8e9a1b00e  ✓
docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md          b10fae0da66d  ✓
results/deposon_v19_benchmark_fixes.json         910c4333eead  ✓
results/deposon_v21_gtformal.json                9d9ae5001c57  ✓
corpus/v20/index.json                            8423ffe266af  ✓
verifier/handoff/P_F_PREDECISION_2026_09_09.json b41c98bf90cc  ✓
docs/V3X/P_F_SPEC_V0.md                          de90faf362c5  ✓
docs/V3X/P_F_RESEARCH_2026_09_09.md              98085df7811a  ✓
deposon_team/plugins/skill_a_p_a_60cells.py      b1463bb24403  ✓
deposon_team/plugins/skill_b_p_c_alpha_beta.py   e5a299f69a22  ✓
deposon_team/plugins/skill_c_p_e_3modality.py    e19e76c5da7e  ✓
deposon_team/plugins/skill_d_p_f_observer.py     3e369a1f6171  ✓
```

**BASELINE: 16/16 PASS** (副本与正式仓 frozen 期望值一致,证明 mirror 完整无损)

### 2.2 二跑幂等性 (5 步比对法)

#### Step A — pre-state hash 捕获
捕获 20 个 mutable 文件 SHA-12 (patch 脚本会触及但本身非 frozen):
```
boss_pc_1/2/3_*.py | attack_pc_a1/a2/a3_*.py | boss_pg_1/2/3_*.py | boss_pa_1/2/3_*.py |
_verify_15frozen.py | _verify_pg_v0.py | runner_pa_d1_d3.py |
P_C_D1_D3_REPORT_2026_09_15.md | D5_DECISIONS_LAND_REPORT_2026_09_15.md |
github_dir_structure_2026_09_18.md | git_commit_msg_2026_09_18.txt |
github_upload_2026_09_18.sh
```

#### Step B — 顺序执行 3 patch 脚本(按依赖序: freeze policy → boss naming → proactive audit)

| patch | stdout 末段 (idempotent 信号) | exit code |
|---|---|---|
| `fix_verify_freeze_policy` | `_verify_15frozen.py: 政策注释已存在, 跳过`<br>`_verify_pg_v0.py: skill_d 已 reconcile, 跳过`<br>`[SC] 16 frozen 嵌入式复核 0 触动 PASS`<br>`fix_verify_freeze_policy SELF-CHECK ALL PASS` | 0 |
| `fix_boss_naming` | `[fix_boss_naming] 幂等模式: 改名已完成, 仅复核`<br>`报告勘误已存在, 跳过`<br>`[SC] 9 文件 compile PASS (0 pyc)`<br>`[SC] 命名空间回正 + 9 尾块 PASS`<br>`[SC] 6 个 D5 3A 历史 JSON 全保留`<br>`[SC] P_C_D1_D3_REPORT §4 勘误块 PASS`<br>`[SC] 16 frozen 后置 0 触动 PASS` | 0 |
| `fix_proactive_audit` | `[B4] runner_pa 已 reconcile, 跳过`<br>`[B5] D5 报告勘误已存在, 跳过`<br>`[B6] dir_structure 勘误已存在且唯一, 跳过`<br>`[A1] commit msg 已占位符化, 跳过`<br>`[A2a] upload.sh guard 已修, 跳过`<br>`[A2b] .gitignore 防护已存在, 跳过`<br>`[SC] runner_pa reconcile + compile PASS`<br>`[SC] D5 报告 + dir_structure 勘误块(唯一) PASS`<br>`[SC] commit msg 预写 verdict 清零 + 占位符 4/4 PASS`<br>`[SC] upload.sh frozen 全量 guard + .gitignore 防护 PASS`<br>`[SC] boss_pa 1/2/3 尾块 + compile PASS`<br>`[SC] 16 frozen 后置 0 触动 PASS` | 0 |

#### Step C — post-state hash 复验
20 个 mutable 文件 SHA-12 与 pre-state 完全一致:
```
[IDEMPOTENCY] 20/20 mutable files UNCHANGED (二跑 = 一跑)
```

#### Step D — frozen 16 后置 0 触动
patch 全部执行后,frozen 16 复验:
```
[FROZEN-16 POST] 16/16 PASS
```

#### Step E — /tmp 与原始仓 hash 一致性
3 个 fix 脚本 BASE 覆写已恢复; review 后 /tmp 副本最终状态与原始仓 frozen + mutable 全部 hash 一致。

### 2.3 幂等性裁定

**3 patch 脚本二跑幂等性 PASS**:
- 每个 patch 的 main() 内部全部走"已存在,跳过"分支
- 16 frozen 0 触动(patch 前后双核 + 嵌入式独立复核 — `fix_verify_freeze_policy` 用 SHA-256 全量读 + 比对 16 项,非内联清单)
- 9 个 SELF-CHECK 尾块存在 + 6 个 D5 3A 历史 JSON 保留(均为文本匹配证据)

**与 Trae 报告 §7 比对**: 一致(15/16 → 16/16 实算均为 PASS)。

---

## §3 SELF-CHECK 尾块 实跑 — 5/9 FAIL (捕获 2 类 patch footer() 模板缺陷)

### 3.1 测试方法

不是依赖 patch 脚本内嵌的 `compile()` 语法检查,而是把 9 个 .py 文件作为 module 实际 `python <file>.py` 执行,捕获 assert / NameError 等运行期异常。

### 3.2 实跑结果

| 脚本 | 结果 | 失败原因 |
|---|---|---|
| `boss_pc_1_2d_ising_universality.py` | **FAIL** | `assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE` 必挂 — 常量实际值 `PASS_LT=0.05, GRAY_GE=0.05`,严格 `<` 不成立 (bug #1) |
| `boss_pc_2_transverse_field_ising.py` | **PASS** | boss_pc_2 用 `assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE`(无中间 GRAY_GE 边界),实测过 |
| `boss_pc_3_reservoir_computing.py` | **FAIL** | 同 boss_pc_1 — 同 bug #1 |
| `attack_pc_a1_resampling.py` | **PASS** | `assert A1_R2_CHANGE_THRESHOLD == 0.15` + `N_RESAMPLE_TRIALS >= 3` 成立;OUT round-trip 过 |
| `attack_pc_a2_fitting.py` | **PASS** | `assert EXP_FIT_R2_RATIO_THRESHOLD == 0.9` 成立 |
| `attack_pc_a3_clipping.py` | **PASS** | `assert CLIP_R2_THRESHOLD == 0.7` + `set(N_CLIPPED) < set(N_FULL) and len(N_CLIPPED) == len(N_FULL) - 2` 成立(n_full=7, n_clipped=5)|
| `boss_pg_1_riemannian_degenerate.py` | **FAIL** | `assert 'TODO' in _src_sc` — `_src_sc` 未定义 (bug #2) |
| `boss_pg_2_hyperbolic_classification_collapse.py` | **FAIL** | 同 bug #2 |
| `boss_pg_3_geodesic_violation.py` | **FAIL** | 同 bug #2 |

**结果统计**: 4/9 PASS, 5/9 FAIL。

**复现**: 在原始仓 (非 /tmp) 跑同样命令,得到完全相同结果 → 缺陷在原盘,非 mirror 损坏。

### 3.3 Bug #1 详解 — `D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 自相矛盾

**位置**: `deposon_team/plugins/fix_boss_naming_2026_09_16.py` line 109 (boss_pc_1 footer) + line 128 (boss_pc_3 footer)

**问题代码**:
```python
"assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE"
```

**原仓常量**:
```python
D_FIX2_PASS_LT = 0.05   # D5 1A strict 阈值 (PASS 区间: D_fix2 < 0.05)
D_FIX2_GRAY_GE  = 0.05   # (GRAY 区间: 0.05 <= D_fix2 < 0.15)
D_FIX2_FAIL_GE  = 0.15   # (FAIL 区间: D_fix2 >= 0.15)
```

**语义**: PASS_LT(小于)与 GRAY_GE(大于等于)的边界值相等是合法且常见的严格阈值约定(0.05 同时是 PASS 的上界与 GRAY 的下界)。Patch 的断言 `PASS_LT < GRAY_GE` 在该约定下必然为 False(0.05 < 0.05 = False),实测断言必挂。

**对比 boss_pc_2** (PASS): 用 `assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE`(跳过了中间 GRAY_GE 边界)→ 实测过。

**修复建议**:
- 方案 A (推荐): `assert D_FIX2_PASS_LT == D_FIX2_GRAY_GE`(锁定 LT/GE 边界约定)
- 方案 B: `assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE` (boss_pc_2 同款, 跳中间)
- 方案 C: `assert D_FIX2_PASS_LT <= D_FIX2_GRAY_GE < D_FIX2_FAIL_GE` (宽松, 容 LT/GE 边界相等)

### 3.4 Bug #2 详解 — `boss_pg_1/2/3` footer `_src_sc` 引用顺序

**位置**: `deposon_team/plugins/fix_boss_naming_2026_09_16.py` line 84-98 (footer() 模板函数)

**问题代码** (boss_pg_1 footer):
```python
assert C_NEAR_EUCLIDEAN < C_TRUE_HYPERBOLIC
assert DEGENERACY_DELTA_THRESHOLD_GRAY < DEGENERACY_DELTA_THRESHOLD_PASS
assert POINCARE_BALL_EPSILON > 0
assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'  # ← _src_sc 未定义
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()  # ← 这里才定义
```

**问题**: footer() 模板的 `body_asserts` 位置在 `_src_sc = _f_sc.read()` 之前; boss_pg 三个 footer 都引用 `_src_sc` 做 `'TODO' in _src_sc` 检查 → NameError。

boss_pg_2/3 同样只有 `assert 'TODO' in _src_sc` 一行,后果相同。

**修复建议**: 把 `body_asserts` 与 `with open(__file__) as _f_sc: _src_sc = _f_sc.read()` 的相对位置在 footer() 模板内对调(让 _src_sc 先于 body_asserts 定义)。`out_roundtrip` 的 `if OUT.exists()` 是条件分支,需保留在最后。

### 3.5 缺陷分级 (P-F V0.1 §5 纪律沿用)

| bug | 影响 | 严重度 | 是否阻塞 D7 |
|---|---|---|---|
| #1 (boss_pc_1/3) | SELF-CHECK 尾块断言自相矛盾,无法证明预注册常数锁定(实算常数实际未变 — boss 实跑仍出正确 verdict,只是断言表达错误) | **中** | **否**(verdict 实际正确,断言语义改 1 字符即可) |
| #2 (boss_pg_1/2/3) | SCAFFOLDING TODO 标记检查形同虚设 — 但 boss_pg 是 SCAFFOLDING 状态,本就不应实跑,缺这道检查不影响功能 | **低** | **否**(SCAFFOLDING 状态由 P-G V0 spec 锁,非依赖此 assert)|

**与 Trae 报告 §6 比对**: Trae 只列 1 个 defect (fix_verify_freeze_policy 初版断言),自我宣称"两次跑均 ALL PASS" — 但其 SC 内置 `compile()` 只做语法检查,未实跑尾块。本 /tmp 重跑以实跑暴露 2 类此前漏检缺陷。

---

## §4 16 frozen 修后 verify

执行 3 patch 脚本 + 9 尾块实跑后,/tmp 副本 frozen 16 SHA-12 复验:

```
[FROZEN-16 POST] 16/16 PASS
```

| 项 | 期望 SHA-12 | 实测 | OK |
|---|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | `03c6c01f3697` | ✓ |
| `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | `78b71d404366` | ✓ |
| `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | `0410ca0fbdae` | ✓ |
| `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | `59d8f56347d5` | ✓ |
| `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | `cce8e9a1b00e` | ✓ |
| `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | `b10fae0da66d` | ✓ |
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | ✓ |
| `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | ✓ |
| `corpus/v20/index.json` | `8423ffe266af` | `8423ffe266af` | ✓ |
| `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90cc` | `b41c98bf90cc` | ✓ |
| `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` | `de90faf362c5` | ✓ |
| `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` | `98085df7811a` | ✓ |
| `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` | `b1463bb24403` | ✓ |
| `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` | `e5a299f69a22` | ✓ |
| `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` | `e19e76c5da7e` | ✓ |
| `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` | `3e369a1f6171` | ✓ |

**0 触动声明成立** ✓ — 包含 skill_d 12:01 user 拍板 1A 合法改动(reconcile by Trae 2026-09-16 带审计痕迹 `OLD f4c68d146141 10981B -> NEW 3e369a1f6171 15927B`)。

P-G V0 / V0.1 不在 16 frozen 列表内(委托信 §7 列的是"11 frozen + 4 plugin spec = 15 frozen",本任务 §0 升级为 16 frozen:加 P_F_V0_1_UPGRADE_2026_09_11.md 与 skill_d 12:01 拍板新 SHA)。P-G V0 / V0.1 仅在 SHA 复算层面被引用,本次 patch 0 触动。

---

## §5 /tmp 副本清理步骤

| 步骤 | 内容 | 时间 |
|---|---|---|
| 1 | 建副本 + BASE 覆写 | 2026-09-15 15:25 |
| 2 | frozen 16 baseline | 15:25 |
| 3 | mutable pre-state hash | 15:25 |
| 4 | 3 patch 脚本顺序执行 | 15:25 |
| 5 | mutable post-state hash (= pre) | 15:25 |
| 6 | frozen 16 post-state (= baseline) | 15:25 |
| 7 | 9 个 PC/PG SELF-CHECK 尾块 实跑 | 15:26 |
| 8 | 3 个 boss_pa 尾块 实跑 (C7) | 15:26 |
| 9 | BASE 覆写恢复 | 15:26 |
| 10 | 报告落盘 + 副本保留(待 Mavis 复审)/ 验证后清理 | 15:30 |

**清理时机**: 沿 user 2026-09-15 D7 前手动 git push 完成后,统一清理。/tmp 副本与原仓 frozen + mutable hash 全等,清理不损任何信息。

---

## §6 严守 7 铁律声明

| 铁律 | 实算证据 |
|---|---|
| 0 LLM 调用 | 全程未调任何 LLM API;仅 `python <file>` 执行 patch 与尾块 |
| 0 proxy | 网络栈未启动;无 HTTP/SOCKS 调用 |
| 0 网关 | 同上 |
| key 不入 prompt / JSON / 落盘 | 未读取任何 key 文件;7 铁律 0 key 严守声明成立 |
| 不动 16 frozen + P-G V0 / V0.1 | 16 frozen 修后复验 16/16 PASS;P-G V0 / V0.1 仅读,未触及 |
| 不动 verifier/mavis/.builtin/scripts/ | /tmp 副本仅镜像 `deposon_team/`, `docs/`, `results/`, `verifier/`, `corpus/`;`mavis/`, `.builtin/`, `scripts/` 不在镜像范围 |
| 不创建临时文件 | `/tmp/deposon_reviewer_b_trae_2026_09_15/` 临时副本例外(任务明文许可);报告落 `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md`(非临时)|

---

## §7 复审裁定建议 (致 Mavis 父会话)

1. **patch 脚本本身 (3 个)** 修后双跑幂等性 + 16 frozen 0 触动 — **PASS, 可保留**
2. **SELF-CHECK 尾块 (9 个)** 实跑 5/9 FAIL — **建议退回 Trae 修 footer() 模板的 2 类 bug**:
   - Bug #1 (boss_pc_1/3 断言): 改 `PASS_LT < GRAY_GE` 为 `PASS_LT == GRAY_GE` 或 `PASS_LT < FAIL_GE`
   - Bug #2 (boss_pg_1/2/3 _src_sc 顺序): footer() 模板内对调 body_asserts 与 `_src_sc = _f_sc.read()` 相对位置
   - **修复规模**: < 30 行,预计 1 轮 patch + 1 轮 /tmp 重跑 = < 30 min
3. **boss_pc_2 + attack_pc_a1/a2/a3** 实跑 PASS,可保留
4. **report 落盘**: `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` (本文件) — 落盘时 frozen 0 触动已核验

**优先级**: bug #2 (boss_pg) 不影响 P-G SCAFFOLDING 当前状态(实跑计划待 D7 后);bug #1 (boss_pc_1/3) 影响 9 月 18 日 D7 实跑 verdict 的预注册锁验证 — 建议**修完再落 D7 实跑**。

---

**复审员**: reviewer-b Worker (branch 子会话)
**复审时间**: 2026-09-15 15:30
**任务 ID**: REVIEWER-B-TRAE-FIX-RERUN-2026-09-15
**附**: 与 Trae 报告 `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` §6 "机械自审首跑抓出的缺陷" 比对 — 实际捕获 1 + 2 = **3 类 footer/断言缺陷**, 2 类为 Trae 漏检。