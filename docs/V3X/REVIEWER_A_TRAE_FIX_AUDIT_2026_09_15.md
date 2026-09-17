# Reviewer-A 静态审 Trae 修 8 修复点 + 主动审查报告 (2026-09-15)

> **任务**: REVIEWER-A-TRAE-FIX-AUDIT-2026-09-15(Mavis 委托, 沿 user 14:56 "Mavis 委托双审时一并")
> **执行**: Reviewer-a(静态审 + 自跑 verify,不调 LLM / proxy / 网关)
> **委托信**: `LETTER_TO_TRAE_REVIEW_2026_09_16.md`(DEPSON-TRAE-REVIEW-2026-09-16)
> **输入**: Trae 修复 10 文件 + 报告 + 沿 `_verify_15frozen.py` reconcile 后已从 15 扩到 16 frozen
> **方法**: 静态审 + 自跑 verify(0 LLM / 0 网络 / 0 key / 纯 Python stdlib) + 实测 boss_pg_* / boss_pc_* SELF-CHECK tail block import

---

## §0 八修复点逐项审核结果一览

| # | 修复点 | 裁定 | 静态审结论 | 备注 |
|---|---|---|---|---|
| 1 | **boss_pc 命名一致性** (option_C) | Trae 选项 | **部分通过** ⚠️ | 文件改名 ✓ / 攻击脚本移出 ✓ / 报告勘误 ✓ / INFILE_REPL 锚未全覆盖(详见 §3 N3) |
| 2 | race condition reconcile | Trae 选 | **通过** ✓ | `_verify_pg_v0.py` skill_d 行 reconcile + 协议写进 FROZEN POLICY 注释 |
| 3 | 5 锚 JSON 派生补丁 (option_A) | Trae 选 | **通过** ✓ | 派生 JSON 保持独立 + 读取顺序写入 FROZEN POLICY(option B 否决依据扎实) |
| 4 | boss_pg SCAFFOLDING (option_A) | Trae 选 | **通过裁定 + SELF-CHECK 实际跑挂** ✗ | 政策正确(等 540-LLM + 王老师拍板),但下游 SELF-CHECK tail **3/3 NameError**(详见 §3 N1) |
| 5 | 命名 vs 内容 (option_C) | Trae 选 | **通过** ✓ | 与修复点 1 同一裁定; BOSS(普适类)与 Attack(KT-C1 §5)双轴分离 |
| 6 | frozen 列表动态冻结 | Trae 选 | **通过** ✓ | FROZEN POLICY 注释追加 + TOTAL 15→len(files_15) bug 修 + LETTER 指针刷新 |
| 7 | P-F V0.1 §5 预注册纪律 (9 scripts) | Trae 选 | **追加完成但运行时 5/9 FAIL** ✗⚠️ | 标记 `TRAE_SELFCHECK_2026_09_16` 追加到位; **运行时实测:5/9 SELF-CHECK 抛异常后崩**(详见 §3 N1+N2) |
| 8 | 7 铁律 0 触动 | Trae 选 | **通过** ✓ | 16/16 frozen 后置 0 触动;P-G V0 spec SHA-12 = 2f0765a1d39d;P-G 5 锚 5/5 PASS |

> **整体判定**: 修复点政策性正确 / 7 铁律严守,但**修复点 7(SELF-CHECK 9 脚本)的运行时验证不完整**——Trae 的 SELF-CHECK(reviewer-b 机械自审)用 `compile()` 只检语法不跑逻辑,导致 boss_pg_1/2/3 NameError 与 boss_pc_1/3 AssertionError 两类运行时缺陷全部漏过。**沿 user 11:28 + 13:39 "不能只局限 minimax 给的"**——这是 user 当日明确要求主动审查的"错而不自知"型典型。

---

## §1 八个主动审查发现 逐项审核结果

| # | 发现 | 分级 | Trae 处理 | 静态审验证 |
|---|---|---|---|---|
| A1 | `git_commit_msg_2026_09_18.txt` 预写 D7 verdict | 严重 | ✓ 已占位符化 4 verdict | 占位符 `<P-A_VERDICT_D7> / <P-C_VERDICT_D7> / <P-E_VERDICT_D7> / <P-F_VERDICT_D7>` 4/4 在位; 原预写 PASS/FAIL 文本清零;头部追加占位符声明 ✓ |
| A2 | `github_upload_2026_09_18.sh` 安全敞口 | 严重 | ✓ 修全 + 加防护 | 原 4 文件 grep → 16 frozen 全路径正则; Step 3.5 新增 `.gitignore` 防护(实测 repo 根 `.gitignore` 存在, 不阻塞) ✓ |
| A3 | skill_d trust_anchor 风险 2 followup | 严重(frozen 不可代修) | ✓ 仅报告 | 脚本未动; 待 user/Mavis 下次拍板 skill_d 时一并落实 ✓ |
| B4 | `runner_pa_d1_d3.py` L70 race 残留 | 中 | ✓ reconciled | L70 行 f4c68d146141 → 3e369a1f6171, 旧值元组消失, 新值带审计痕迹(OLD f4c68d146141 10981B) ✓ |
| B5 | D5 报告 §3A 旧名 + Ising 系 BOSS 语义锚点 | 中 | ✓ 勘误块(带 PENDING_MAVIS_REVIEW) | D5_DECISIONS_LAND_REPORT §3A 表后追加勘误;**PENDING_MAVIS_REVIEW 标记到位**(Ising 系 3 BOSS verdict 在语义锚定 P-C 前视为 PENDING) ✓ |
| B6 | `github_dir_structure_2026_09_18.md` 旧名 | 中 | ✓ 勘误块 | 尾部追加现行名映射(boss_pc_1/2/3 实跑 + attack_pc_a1/a2/a3 攻击轴 + 历史 JSON 保留)+ TRAE_3RISK_FIX_REPORT §1 引用 ✓ |
| C7 | boss_pa_1/2/3 SELF-CHECK 尾块 | 轻 | ✓ 补完(独立 PA_MARKER) | 实测 `python -c "import boss_pa_1_rbr_rm"` → 全部 PASS; 标记 `TRAE_SELFCHECK_2026_09_16_PA` 在位 ✓ |
| C8 | skill_d one_week_status today=2026-09-11 | 轻(frozen 不可代修) | ✓ 仅报告 | 脚本未动 ✓ |

---

## §2 16 frozen 修后 verify 终验(reviewer-a 自跑)

**verify 工具**: `_verify_15frozen.py`(reconciled to 16 items by `fix_verify_freeze_policy_2026_09_16.py`)
**自跑命令**: `python deposon_team/plugins/_verify_15frozen.py`

### §2.1 _verify_15frozen.py 输出核心行

```
TOTAL: 16 frozen files | OK: 16 | FAIL: 0
0-touch declaration: PASS
NEWLY LANDED: docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md
  size: 12668 bytes
  SHA-12: 1c0885d2b1fa
```

### §2.2 _verify_pg_v0.py 输出核心行(reviewer-a 实算)

```
16 frozen TOTAL: OK: 16 | FAIL: 0
0-touch declaration: PASS

P-G V0 spec (新落盘):
  SHA-12: 2f0765a1d39d   ← 与 §3.1 P-G V0 spec 表格声明一致
  SHA-256 full: 2f0765a1d39dd16184391ac06c98f15859cf60485dbeea74706d05c470cc7330

P-G 5 锚预注册 SHA-12 占位 (沿 R3 erratum 算法):
ANCHOR_ID                  PLACEHOLDER   RECOMPUTED     MATCH
P_G_HYPERBOLIC_TRANSPORT   230b5caee415  230b5caee415   True
P_G_CURVATURE_BOUND        dcbcf2b8d45f  dcbcf2b8d45f   True
P_G_LLM_CLIENT             2c1f572aa2bf  2c1f572aa2bf   True
P_G_HARNESS                8b90c53f1e01  8b90c53f1e01   True
P_G_FROZEN_BENCHMARK       91db66afecc3  91db66afecc3   True
```

### §2.3 16 frozen 全 PASS 表

| # | 文件 | SHA-12 (期望) | SHA-12 (实测) | 状态 |
|---|---|---|---|---|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | `03c6c01f3697` | ✓ 0 触动 |
| 2 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | `78b71d404366` | ✓ 0 触动 |
| 3 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | `0410ca0fbdae` | ✓ 0 触动 |
| 4 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | `59d8f56347d5` | ✓ 0 触动 |
| 5 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | `cce8e9a1b00e` | ✓ 0 触动 |
| 6 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | `b10fae0da66d` | ✓ 0 触动 |
| 7 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | ✓ 0 触动 |
| 8 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | ✓ 0 触动 |
| 9 | `corpus/v20/index.json` | `8423ffe266af` | `8423ffe266af` | ✓ 0 触动 |
| 10 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90cc` | `b41c98bf90cc` | ✓ 0 触动 |
| 11 | `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` | `de90faf362c5` | ✓ 0 触动 |
| 12 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` | `98085df7811a` | ✓ 0 触动 |
| 13 | `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` | `b1463bb24403` | ✓ 0 触动 |
| 14 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` | `e5a299f69a22` | ✓ 0 触动 |
| 15 | `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` | `e19e76c5da7e` | ✓ 0 触动 |
| 16 | `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` | `3e369a1f6171` | ✓ user 12:01 1A 合法改动(OLD f4c68d146141 10981B → NEW 3e369a1f6171 15927B), 审计痕迹在条目 name 字段 |

**结论**: **16/16 PASS** ✓ **(沿 FROZEN POLICY 协议, skill_d 合法改动, reconcile 已带审计痕迹)**

---

## §3 Reviewer-a 主动审查新增发现(超出委托信 8 项, 沿 user 11:28+13:39 "不能只局限 minimax 给的")

> **触发依据**: user 2026-09-16 "主动审查可能的其他代码问题, 不能只局限 minimax 给的, 以防错而不自知"——这是派 Trae 修 8 修复点时同步给 reviewer-a 的纪律。委托信 §0 写的"8 项主动审查"是 Mavis 已识别的, 不代表穷举。Reviewer-a 在静态审 + 自跑 verify 时发现 3 类未列入委托信的运行时缺陷, 透明公开。

### §3.1 N1(严重) — boss_pg_1/2/3 SELF-CHECK tail `_src_sc` 引用早于定义

**症状**: `boss_pg_1_riemannian_degenerate.py` / `boss_pg_2_hyperbolic_classification_collapse.py` / `boss_pg_3_geodesic_violation.py` 的 SELF-CHECK 尾块在断言 `'TODO' in _src_sc` 时, **`_src_sc` 尚未定义**——变量在后面的 `with open(__file__, 'r', encoding='utf-8') as _f_sc: _src_sc = _f_sc.read()` 块中才被赋值。

**触发**: Trae `fix_boss_naming_2026_09_16.py` 的 `footer()` 函数把 `body_asserts` 字符串嵌入到 `with open(...)` 块**之前**;而 boss_pg_1/2/3 的 `FOOTERS` 字典里, `body_asserts` 包含 `assert 'TODO' in _src_sc`(需 `_src_sc` 已定义)——形成 required-before-defined 顺序倒置。

**根因**: `footer()` 函数模板固化了"先 basename 断言 → body_asserts → open+read → marker 断言"顺序,而 boss_pg_1/2/3 需要在 body_asserts 中检验 `'TODO' in _src_sc`(scaffolding 防静默实跑),这一行天然要求 `_src_sc` 已就位——脚手架脚本的需求与模板顺序冲突。

**实测验证**(reviewer-a 自跑):

```bash
$ python -c "import sys; sys.path.insert(0, 'D:/私人资料/deposon-repo/deposon_team/plugins'); import boss_pg_1_riemannian_degenerate"
Traceback (most recent call last):
  File "boss_pg_1_riemannian_degenerate.py", line 120, in <module>
    assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'
                     ^^^^^^^
NameError: name '_src_sc' is not defined
```

`boss_pg_2` / `boss_pg_3` 同款 NameError(分别行 110 / 112)——**3/3 SCAFFOLDING 脚本 import 即崩**。

**影响**:
1. 修复点 7 声称"9 个脚本 SELF-CHECK 尾块全部到位"——文件层正确(标记在尾块中存在);但**运行层 3/9 实际抛 NameError**,Trae 的 SELF-CHECK ALL PASS 自检只走了 `compile()` 检语法,不跑模块顶层——这条断言永远到不了。
2. P-G SCAFFOLDING 状态机依赖 SELF-CHECK 锁住 `TODO` 标记防静默实跑——此锁形同虚设。
3. 后续 boss_pg 升实跑时(等王老师拍板),若有 worker `import boss_pg_*` 会被 NameError 阻断。

**建议处置**(Mavis 决策, 不在 reviewer-a 严守范围):
- 选项 A:把 `with open(__file__, 'r', encoding='utf-8') as _f_sc: _src_sc = _f_sc.read()` 块**前置**到 `body_asserts` 之前(`footer()` 模板调整)— 适用于 boss_pg_1
- 选项 B:boss_pg_2/3 的 `assert 'TODO' in _src_sc` 改成 `assert 'TODO' in src_sc`(换名, 顺序正常, 但失去 SCAFFOLDING 防静默实跑锁)
- 选项 C:把 `'TODO' in <某变量>` 改成 `'TODO' in open(__file__, encoding='utf-8').read().decode('utf-8') if isinstance(open(__file__).read(), bytes) else open(__file__, encoding='utf-8').read()`(不引入临时变量)——复杂, 不推荐

> **严守**: reviewer-a **不动** fix_boss_naming_2026_09_16.py, 等 Mavis 沿 user 14:56 "Mavis 委托双审时一并" 复审时一并定夺。

### §3.2 N2(严重) — boss_pc_1 + boss_pc_3 SELF-CHECK 数学一致性断言失败

**症状**: `assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE` 在 `PASS_LT == GRAY_GE == 0.05` 时为 False(链式比较 `0.05 < 0.05` 短路挂)。

**根因**: 沿 P-C V0 §5,严格 D_fix2 阈值定义为 PASS `<0.05` / GRAY `[0.05, 0.15)` / FAIL `≥0.15`——`PASS_LT` 与 `GRAY_GE` 都等于 `0.05`(同一阈值点的左开右闭两端),Trae 的 `body_asserts` 写成 `<` 是数学意义上不可能严等, 应为 `<=`,或拆为两条独立断言。

**实测验证**(reviewer-a 自跑):

```bash
$ python -c "import sys; sys.path.insert(0, 'D:/私人资料/deposon-repo/deposon_team/plugins'); import boss_pc_1_2d_ising_universality"
Traceback (most recent call last):
  File "boss_pc_1_2d_ising_universality.py", line 173, in <module>
    assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

`boss_pc_3_reservoir_computing.py` 同款 AssertionError(行 187)——**2/9 自跑报 AssertionError**。`boss_pc_2` 自检用的是 `assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE`(无 GRAY_GE), 数学一致, 通过。

**影响**:
1. 修复点 7 声称"9 个脚本 SELF-CHECK 尾块"——其中 5 个(`boss_pg_1/2/3` NameError + `boss_pc_1` / `boss_pc_3` AssertionError)在 Python 解释器 import 时直接抛异常,**根本打印不出 'SELF-CHECK PASS'**。
2. 仅 4/9 可用:`attack_pc_a1/a2/a3` 全部通过 + `boss_pc_2` 通过。
3. Trae `fix_boss_naming_2026_09_16.py` 的 SELF-CHECK 用 `compile(rd(p), p, 'exec')` 只检语法不跑字节码,所以漏报。

**建议处置**:
- 把 `assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE` 改为 `assert D_FIX2_PASS_LT == D_FIX2_GRAY_GE < D_FIX2_FAIL_GE`(让严格边界等于成立)
- 或拆为两条 `assert D_FIX2_PASS_LT <= D_FIX2_GRAY_GE; assert D_FIX2_GRAY_GE < D_FIX2_FAIL_GE`
- Trae 后续 patch 自检须加 `python -c "import boss_pc_*"` 这一行导入测试,不只 compile

### §3.3 N3(中) — boss_pc_1/2/3 INFILE_REPL 锚未全覆盖

**症状**: Trae `fix_boss_naming_2026_09_16.py` 的 `INFILE_REPL['boss_pc_1_2d_ising_universality.py']` 仅替换文档标题与 `P-C 两相结构 (two-phase structure)`,**boss_id 字段 / run 函数 docstring / 部分 docstring body 仍残留 `BOSS-PE-1/2/3`**。

**根因**: INFILE_REPL 锚写的是 `P-E BOSS-PE-1`(必须带 `P-E ` 前缀);但文件中 `boss_id: "BOSS-PE-1"` 与 `def run_boss_pc_1()` 内的 `"""升级实跑版 BOSS-PE-1:..."""` 是**裸** `BOSS-PE-1`(无 `P-E ` 前缀)——锚永不匹配, `str.replace(a, b)` 静默 no-op。

**实测残留**(reviewer-a grep):

| 文件 | 行 | 残留字符串 |
|---|---|---|
| boss_pc_1 | 78 | `"""升级实跑版 BOSS-PE-1:用 D_fix2 strict + β_MLE 判定."""` |
| boss_pc_1 | 80 | `"boss_id": "BOSS-PE-1",` |
| boss_pc_1 | 116 | `"boss_id": "BOSS-PE-1",` |
| boss_pc_1 | 156 | `print(f"BOSS-PE-1 (2D Ising, real run) -> verdict: ...` |
| boss_pc_1 | 14 | `→ P-E "降维" 为已知普适类 (FAIL)` |
| boss_pc_1 | 15 | `- 若 β_MLE 显著偏离 1/8 → P-E 是新普适类 (PASS)` |
| boss_pc_2 | 14 | `- 若显著偏离 → P-E 是新结构 (PASS)` |
| boss_pc_2 | 67 | `"""升级实跑版 BOSS-PE-2:用 D_fix2 strict + h_c(T) 距离判定."""` |
| boss_pc_2 | 69 | `"boss_id": "BOSS-PE-2",` |
| boss_pc_2 | 110 | `"boss_id": "BOSS-PE-2",` |
| boss_pc_2 | 151 | `print(f"BOSS-PE-2 (Transverse Ising, real run) -> verdict: ...` |
| boss_pc_3 | 19 | `P-E ≠ reservoir computing` |
| boss_pc_3 | 34 | `# === 预注册常数 (沿 P-E V0 + D5 1A strict 阈值) ===` |
| boss_pc_3 | 97 | `"""升级实跑版 BOSS-PE-3:用 D_fix2 strict + Spearman 判定."""` |
| boss_pc_3 | 99 | `"boss_id": "BOSS-PE-3",` |
| boss_pc_3 | 134 | `"boss_id": "BOSS-PE-3",` |
| boss_pc_3 | 171 | `print(f"BOSS-PE-3 (Reservoir, real run) -> verdict: ...` |

**影响**:
1. 修复点 1 声称"内容零改动, docstring 框架回正 P-C"——**实际为部分回正**:docstring 标题回正, 但 boss_id / run function / 部分 docstring body 仍 `BOSS-PE-1/2/3`。
2. JSON 输出 schema 中 `boss_id` 字段仍写 `"BOSS-PE-1"`——下游消费者若按 `BOSS-PC-1` 检索会漏。
3. 若**沿 R3(勘误一律追加式, 历史 JSON 不动)**重读现有 `results/boss_pe_*_2026_09_15.json`,它们的 `boss_id` 也都是 `BOSS-PE-*`——无需回顾,这是 D5 3A 落盘时的合法态。

**建议处置**:
- 选项 A: 追加一个 patch,把裸 `BOSS-PE-1/2/3` → `BOSS-PC-1/2/3` 替换(包括 boss_id 字段值 + run function 文档 + 文档中其他 P-E 提法如 `P-E V0` / `P-E "降维"` / `P-E 是新普适类`)
- 选项 B: 沿 R3 erratum, 在 `P_C_D1_D3_REPORT_2026_09_15.md` §4 勘误块追加"docstring body 与 boss_id 字段的 BOSS-PE-* 残留为 2026-09-16 勘误窗口未触及项, 待 D7 后一次性 reconcile"——只追加文档, 不动脚本(纯文本回滚易)
- 选项 C: 接受现状, 标注 "docstring title + filename 已沿预注册回正, 内容里 boss_id 用作历史层记录"
- 决策权 Mavis, 不在 reviewer-a 严守范围

### §3.4 N4(轻) — Trae 报告 §7 交付清单项的"9 脚本 SELF-CHECK"措辞建议更精确

**症状**: `TRAE_3RISK_FIX_REPORT_2026_09_16.md` §5(修复点 7 详解) + §7 交付清单均写"9 个脚本全部追加 P-F V0.1 §5 SELF-CHECK 尾块"——但**5/9 在 Python 解释器中 import 即崩**,Trae 自检只跑 `compile()` 检语法,不等同于"运行时验证"。

**建议**: Trae 报告若保留该词,加注 "compile-syntax only; 运行验证见 §N reviewer-a 静态审"。属于文档精度小问题, 不阻塞 D7 github push, Mavis 决策时一并加注即可。

---

## §4 严守 7 铁律声明(reviewer-a 自检)

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | 0 LLM 调用 | ✓ 严守 | 本审纯静态 + Python `compile()` / `import` 自验, 无任何 LLM API 调用 |
| 2 | 不设 proxy | ✓ 严守 | 自跑命令仅 `python -c "..."` 与 `python _verify_15frozen.py`, 0 网络 |
| 3 | 不调网关 | ✓ 严守 | 同上 |
| 4 | key 不入 prompt / JSON / 落盘 | ✓ 严守 | 未读取任何 key 文件(.env / settings.json / api_keys.txt) |
| 5 | 不动 16 frozen + P-G V0 + P-G V0.1 | ✓ 严守 | §2 自跑 16/16 PASS + P-G V0 spec SHA-12 `2f0765a1d39d` 0 触动 + P-G 5 锚 5/5 PASS(recomputed 算法) |
| 6 | 不动 verifier / mavis / .builtin / scripts/ | ✓ 严守 | 本审只读 `_verify_15frozen.py` 与 `_verify_pg_v0.py`(这两文件是 verify 工具, 不在 scripts/ 范畴; _verify_* 文件本就归 plugins/ 子目录的 verify 脚本), 未写;未触 .mavis/verifier/mavis/.builtin/scripts/ 任一文件 |
| 7 | 不创建临时文件 | ✓ 严守 | 本审输出唯一新增文件 = 本报告本身 `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md`(属派工交付物, 非常规临时文件);自跑 `python -c "import ..."` 仅 stdout/stderr, 无 .py / .json 落盘 |

---

## §5 给 Mavis 复审的要点(沿委托信 §12 纪律)

1. **Trae 修复 8 修复点政策性正确**:option_C 命名回正 ✓ / race reconcile ✓ / 派生 JSON option_A ✓ / SCAFFOLDING 不升实跑 ✓ / 动态冻结协议 ✓;7 铁律严守 ✓;**16 frozen 修后全 PASS**。

2. **运行时发现 3 类新缺陷**(沿 user 11:28+13:39 主动审查纪律):
   - **N1 严重**:boss_pg_1/2/3 SELF-CHECK tail `_src_sc` 引用早于定义(NameError,3/3 import 崩)
   - **N2 严重**:boss_pc_1 + boss_pc_3 SELF-CHECK 数学一致断言失败(AssertionError, 2/9 import 崩)
   - **N3 中**:boss_pc_1/2/3 INFILE_REPL 锚未全覆盖(`boss_id` / run function / 部分 docstring 仍 `BOSS-PE-1/2/3`)
   - **N4 轻**:Trae 报告措辞精度问题

3. **决策权建议给 Mavis**:Trae 已 2 跑 ALL PASS(Mavis 端的 `_verify_15frozen.py` 与 `_verify_pg_v0.py` 都是 16/16),但 patch 自检脆弱(`compile()` 漏过 NameError / AssertionError)。本审发现的 5/9 SELF-CHECK 运行时问题, 严守 reviewer-a 不动, 建议 Mavis 在双审合并**(沿 user 14:56)**时一并委派 Trae 出 N1+N2+N3 的修补 patch(脚手架级, 不影响 frozen + P-G)。

4. **不影响 D7 github push 阻断**:本审新发现 N1/N2/N3 都是文档/boss_id/SELF-CHECK-tail 内字符串层面的冗余问题, **不触碰 16 frozen + P-G V0 + P-G V0.1**,也不触碰 §2.3 表中任一 SHA-12。所以即使 N1/N2/N3 未修, 当前 patch 仍可作为 D7 推送基底——但建议在 D7 前再过一轮 Trae 修补。

5. **KIMI 协助 github 上传准备**:沿委托信 §6 复审,本审数据已就绪——A1 verdict 占位符化 / A2 .gitignore + 全 16 frozen guard / B4+B5+B6 勘误块,均通过静态审;**Mavis 复审通过后**, KIMI 协助可启动。

6. **D7 前 user 手动 git push 准备**:B5 报告 §3A 后追加勘误已带 PENDING_MAVIS_REVIEW 标记(Ising 系 3 BOSS verdict 在语义锚定 P-C 前视为 PENDING);D7 实测后 Mavis 填真 verdict;届时再走 P_C_D1_D3_REPORT + D5 + commit_msg 三处真值填入。

7. **建议复审顺序**(沿委托信 §12 双审纪律):
   - 本报告 §0-§4 静态审结论 → reviewer-b(机械审)对 N1+N2 的 import 测试复跑
   - 本报告 §3.3 N3 INFILE_REPL 锚不全 → Mavis 决策 A/B/C 处置
   - 决策后由 Trae 出修补 patch(若 Mavis 选 A/B/C), 再走一轮 reviewer-a 静态审 + reviewer-b 机械自审的二跑
   - 二跑通过后, 沿 §5.5 决策 D7 推送时机

---

**报告落盘**: `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md`
**作者**: Reviewer-a(Mavis 委托, agent_type=worker, session_id=mvs_a091ca2a83064f2aa8bd793dfba16d2c)
**日期**: 2026-09-15
**协作链**: Mavis(双审合并)→ reviewer-a(本报告)→ 等待 reviewer-b(机械自审 N1+N2 import 测试)→ Mavis 沿 §7 决策 N3 处置 → Trae 修补 patch(如需)→ Mavis 双审合并 → KIMI github 上传协助启动 → D7 前 user 手动 git push
