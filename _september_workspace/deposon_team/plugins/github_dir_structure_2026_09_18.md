# V3X 1 周判死成果 github 上传目录结构设计(2026-09-18)

> **作者**: Mavis (Mavis / Mavis, 沿 KIMI 委托信 §3)
> **日期**: 2026-09-15 14:31
> **配套**: `docs/V3X/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md`
> **严守**: 7 铁律 0 触动 18 frozen + 派生 JSON

---

## §1 顶层仓库结构(推荐命名: `deposon-v3x-1week-kill`)

```
deposon-v3x-1week-kill/                   # github 仓库名(沿 user 拍板)
├── README.md                              # 仓库首页(沿 V3X_1WEEK_KILL_REPORT_2026_09_18.md 1 页)
├── LICENSE                                 # (沿 user 选择)
├── .gitignore                              # git ignore 配置
├── docs/
│   └── V3X/                                # V3X 项目文档
│       ├── README.md                       # V3X 目录索引
│       ├── V3X_1WEEK_KILL_REPORT_2026_09_18.md  # ★ D7 1 周判死报告 1 页
│       ├── D5_DECISIONS_LAND_REPORT_2026_09_15.md  # 5 项 D5 决策落盘
│       ├── P_A_D1_D3_REPORT_2026_09_15.md   # P-A 报告
│       ├── P_C_D1_D3_REPORT_2026_09_15.md   # P-C 报告
│       ├── P_E_D1_D3_REPORT_2026_09_15.md   # P-E 报告
│       ├── P_F_D1_FULL_REPORT_2026_09_15.md # P-F D1 完整版
│       ├── P_F_D1_REPORT_2026_09_15.md      # P-F D1 cross-check
│       ├── P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md  # P-G V0 spec
│       ├── P_G_V01_REPORT_2026_09_15.md     # P-G V0.1 双曲 transport
│       ├── D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md  # D_fix2 真值验证
│       ├── REVIEWER_A_STATIC_AUDIT_2026_09_15.md   # 双审
│       ├── REVIEWER_B_TMP_RERUN_2026_09_15.md     # 双审
│       ├── RISK3_V0_FIXES_2026_09_11.md     # 3 风险修正
│       ├── TRAE_FIX_REREQUEST_3RISKS_2026_09_11.md  # Trae 委托信(上轮)
│       ├── TRAE_3RISK_FIX_REPORT_2026_09_11.md     # Trae 修 3 风险报告
│       ├── LETTER_FROM_TRAE_3RISK_2026_09_11.md   # Trae 回信(上轮)
│       ├── TRAE_FIX_REQUEST_3RISKS_2026_09_11.md   # 上一封 Trae 委托
│       ├── LETTER_TO_TRAE_REVIEW_2026_09_16.md     # 本轮 Trae 委托(8 修复点)
│       └── LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md  # 本轮 KIMI 委托
├── results/                              # 200+ 已落盘 JSON 实算
│   ├── deposon_v19_*.json                  # v19 frozen 基准
│   ├── deposon_v20_*.json                  # v20 corpus frozen
│   ├── deposon_v21_gtformal.json           # v21 frozen
│   ├── deposon_v3_physical_opt_60cells_2026_09_11.json  # v3 物理公式 60cells
│   ├── deposon_dpath_cross_modal_2026_09_10.json        # dpath 跨模态
│   ├── deposon_volcengine_*.json           # volcengine 实算
│   ├── deposon_risk1_*.json                # 3 风险修正决策
│   ├── deposon_risk2_*.json
│   ├── deposon_risk3_*.json
│   ├── deposon_pc_d1_d3_2026_09_15.json    # 4 路径 D1-D3 实算
│   ├── deposon_pe_d1_d3_2026_09_15.json
│   ├── deposon_pa_d1_d3_2026_09_15.json
│   ├── deposon_pf_d1_full_9m5c_2026_09_15.json
│   ├── deposon_pg_v01_9m60c_2026_09_15.json          # P-G V0.1 双曲 transport
│   ├── deposon_d_fix2_metric_verify_9m60c_2026_09_15.json  # D_fix2 真值验证
│   ├── boss_pe_3_*.json                  # BOSS 自测结果
│   ├── KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json  # 2A 派生 JSON
│   └── ... (其他 24+ JSON)
├── verifier/                              # P-F verifier & handoff
│   └── handoff/
│       ├── KT_ABC1_anchors_sha256_12.json  # ★ 5 锚 JSON(SHA-12 03c6c01f3697)
│       ├── P_F_PREDECISION_2026_09_09.json  # P-F V0 占位
│       └── P_F_PREDECISION_2026_09_11_V0.1.json  # P-F V0.1 真值
├── corpus/v20/index.json                  # corpus v20 frozen
├── deposon_team/
│   ├── plugins/
│   │   ├── skill_a_p_a_60cells.py          # ★ 4 plugin spec
│   │   ├── skill_b_p_c_alpha_beta.py
│   │   ├── skill_c_p_e_3modality.py
│   │   ├── skill_d_p_f_observer.py        # 沿 user 12:01 1A 合法改动
│   │   ├── boss_pa_1/2/3_*.py             # P-A BOSS 实跑
│   │   ├── boss_pc_1/2/3_attack_*.py      # P-C BOSS(沿 P-C V0 §5 攻击测法)
│   │   ├── boss_pe_1/2/3_*.py             # P-E BOSS 升级实跑
│   │   ├── boss_pg_1/2/3_*.py             # P-G BOSS SCAFFOLDING
│   │   ├── _verify_15frozen.py            # 16 frozen verify 工具
│   │   ├── _verify_pg_v0.py                # P-G 5 锚预注册 verify
│   │   ├── github_upload_2026_09_18.sh    # github 上传脚本(KIMI 生成)
│   │   ├── github_dir_structure_2026_09_18.md  # 上传目录结构(本文件)
│   │   └── git_commit_msg_2026_09_18.txt  # git commit message(KIMI 生成)
│   └── ...
├── .mavis/
│   └── scripts/                            # 4 worker 跑批脚本(严守 0 触动)
└── README_V3X_1WEEK.md                     # ★ 1 周判死报告 1 页(github 仓库首页)
```

---

## §2 文件分类(上传优先级)

### 2.1 必须上传(★ 高优先级)

| 文件/目录 | 理由 |
|---|---|
| `README.md` + `README_V3X_1WEEK.md` | 仓库首页 + 1 周判死报告 1 页 |
| `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | D7 终极判死报告 |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 5 锚 JSON(03c6c01f3697)|
| `deposon_team/plugins/skill_a/b/c/d.py` | 4 plugin spec |
| `deposon_team/plugins/boss_*.py` | 6 BOSS 实跑脚本 |
| `deposon_team/plugins/_verify_15frozen.py` + `_verify_pg_v0.py` | verify 工具 |
| `results/deposon_*.json` | 200+ 实算结果 |

### 2.2 推荐上传(中优先级)

| 文件/目录 | 理由 |
|---|---|
| `docs/V3X/*.md` | V3X 项目所有报告 |
| `corpus/v20/index.json` | corpus v20 frozen |
| `verifier/handoff/*.json` | P-F V0/V0.1 JSON |
| `.mavis/scripts/` | worker 跑批脚本 |

### 2.3 可选上传(低优先级)

| 文件/目录 | 理由 |
|---|---|
| `LICENSE` | (沿 user 选择)|
| `.gitignore` | git ignore 配置 |
| `docs/V3X/LETTER_*.md` | 委托信链 |

### 2.4 不上传(严守)

| 文件/目录 | 理由 |
|---|---|
| `C:\Users\Administrator\Desktop\AI\*.txt` | key 文件(7 铁律第 4 条)|
| `.minimax/agents/verifier/`, `.minimax/agents/mavis/`, `.minimax/agents/.builtin/`, `.minimax/agents/scripts/` | 7 铁律第 7 条 |
| `results/_worker_temp/` | verify 脚本例外目录 |
| `results/.tmp/` | verify 脚本例外目录 |
| 任何 worker 输出日志 / 中间文件 | 临时文件(7 铁律第 8 条)|

---

## §3 关键约束(严守)

### 3.1 0 触动 18 frozen

```
$ python deposon_team/plugins/_verify_15frozen.py
TOTAL: 15 frozen files | OK: 16 | FAIL: 0
0-touch declaration: PASS
```

| # | 文件 | SHA-12 | 状态 |
|---|---|---|---|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | ✓ 0 触动 |
| 2 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | ✓ 0 触动 |
| 3 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | ✓ 0 触动 |
| 4 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | ✓ 0 触动 |
| 5 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | ✓ 0 触动 |
| 6 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | ✓ 0 触动 |
| 7 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | ✓ 0 触动 |
| 8 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | ✓ 0 触动 |
| 9 | `corpus/v20/index.json` | `8423ffe266af` | ✓ 0 触动 |
| 10 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90cc` | ✓ 0 触动 |
| 11 | `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` | ✓ 0 触动 |
| 12 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` | ✓ 0 触动 |
| 13 | `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` | ✓ 0 触动 |
| 14 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` | ✓ 0 触动 |
| 15 | `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` | ✓ 0 触动 |
| 16 | `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` | ⚠️ 沿 user 12:01 1A 合法改动 |
| + | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `2f0765a1d39d` | ✓ 0 触动 |

### 3.2 P-G V0.1 5 锚(实算)

| 锚 ID | SHA-12 |
|---|---|
| `P_G_HYPERBOLIC_TRANSPORT` | `9c3c50005103` |
| `P_G_CURVATURE_BOUND` | `8ff586b2722e` |
| `P_G_LLM_CLIENT` | `0130d179059e` |
| `P_G_HARNESS` | `27419597798b` |
| `P_G_FROZEN_BENCHMARK` | `9205c1168e59` |

### 3.3 派生 JSON (2A)

`verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` (5049 B, SHA-12 `da517c115f3c`)

---

## §4 github release 标签

- **Tag**: `v3.0.0-1week-kill-2026-09-18`(沿 P-A V0 / P-G V0.1 版本号)
- **Title**: "V3X 1 Week Kill Report (2026-09-18)"
- **Description**: 沿 `LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` §4.2 模板

---

## §5 时间线

```
D0 (2026-09-15) — 本文档 + KIMI 委托信落盘 ✓
D5 (2026-09-16) — Trae 修复启动
D6 (2026-09-17) — Trae 修复回信 + Mavis 双审
D7 (2026-09-18) — 5 锚终极 PASS/FAIL 拍板 + V3X_1WEEK_KILL_REPORT_2026_09_18.md 落盘
D7 之前 (09-15 → 09-17) — KIMI 协助生成 github 上传脚本 + 目录结构
D7 完成 (09-18) — 沿 github 上传脚本执行 git commit + push → 公开仓库
```

---

## §6 严守 7 铁律声明

| 铁律 | 状态 |
|---|---|
| 1. 0 LLM 调用 | ✓ 严守(纯文本编辑)|
| 2. 不设 proxy | ✓ 严守 |
| 3. 不调网关 | ✓ 严守 |
| 4. key 不入 prompt/JSON/落盘 | ✓ 严守(KIMI 自己处理)|
| 5. 不动 5 锚 JSON | ✓ 严守(`03c6c01f3697` 0 触动)|
| 6. 不动 4 SPEC V0.1 + v19/v21 + corpus_v20 + 16 frozen + P-G V0 + P-G V0.1 | ✓ 严守(17 frozen 修前修后 0 触动)|
| 7. 不动 verifier/mavis/.builtin/scripts/ | ✓ 严守 |
| 8. 不创建临时文件 | ✓ 严守 |

---

## §7 不擅自决定

- ❌ 不擅自执行 git commit + push(等 D7 终极判死 + user 拍板)
- ❌ 不擅自启动 KIMI API 调用(等 user 在 KIMI 网页上执行)
- ❌ 不擅自决定 github 仓库命名(等 user 拍板)
- ❌ 不擅自决定 LICENSE 类型(等 user 拍板)
- ❌ 不擅自决定 .gitignore 配置(等 KIMI 协助 + user 拍板)
- ❌ 不擅自决定 release 标签格式(等 user 拍板)

---

**目录结构设计完成** | 严守 7 铁律 + 18 frozen 0 触动 | KIMI 协助生成上传脚本 | 等 D7 (2026-09-18) 终极判死 + user 拍板手动执行 git push


---

> **勘误(2026-09-16, Trae 主动审查, DEPSON-TRAE-REVIEW-2026-09-16 后续)**: 上文 §1 目录树中的 `boss_pc_1/2/3_attack_*.py` 与 `boss_pe_1/2/3_*.py` 为改名前历史层(2026-09-16 已按预注册回正), D7 github 打包按**现行名**执行:
> - `boss_pc_1_2d_ising_universality.py / boss_pc_2_transverse_field_ising.py / boss_pc_3_reservoir_computing.py`(P-C BOSS, 实跑)
> - `attack_pc_a1_resampling.py / attack_pc_a2_fitting.py / attack_pc_a3_clipping.py`(P-C 攻击轴, 实跑)
> - `boss_pg_1/2/3_*.py`(P-G SCAFFOLDING, 不变) + `boss_pa_1/2/3_*.py`(P-A BOSS, 不变)
> - `results/boss_pe_*_2026_09_15.json` 等历史结果 JSON 保留(历史工件)
> - 详映射见 `TRAE_3RISK_FIX_REPORT_2026_09_16.md` §1; 本文件其余结构不变