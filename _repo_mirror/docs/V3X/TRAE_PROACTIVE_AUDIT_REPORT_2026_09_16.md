# Trae 主动审查报告 — 超委托信范围代码审查 (2026-09-16)

> **触发**: user 2026-09-16 "主动审查可能的其他代码问题, 不能只局限 minimax 给的, 以防错而不自知"
> **审查域**: deposon_team/plugins 全量 25 文件 + 上轮修复 followup 落实核验 + D5 落盘工件引用一致性 + D7 预备件(github 上传三件套)
> **方法**: 静态读 + 全仓 grep + patch 集中修复(`fix_proactive_audit_2026_09_16.py`, 二跑幂等 ALL PASS) + 修后终验 16/16
> **合规**: 0 LLM / 0 网络 / 0 key; 16 frozen 前后两核 0 触动; 历史工件零改写

---

## §0 发现总览(8 项: 3 严重 + 3 中等 + 2 轻微)

| # | 级 | 发现 | 处置 |
|---|---|---|---|
| A1 | 🔴 严重 | **git_commit_msg_2026_09_18.txt 预写 D7 终极判死结论**(P-A PASS/P-C FAIL_H0/P-E PASS/P-F PASS 全写定, 而 D7 是 09-18 未发生)——"结论先于数据", 违反预注册纪律; 若 D7 实测与预写不符, 该文件即成既定结论先行的书面证据 | ✅ 已修: 4 个 verdict + BOSS-PE-3 PASS 全部占位符化(`<XXX_VERDICT_D7>`), 顶部加占位符声明, D7 实测后 Mavis 填真值 |
| A2 | 🔴 严重 | **github_upload_2026_09_18.sh 两处安全敞口**: ①frozen 检查只 grep 4 个文件名, 16 frozen 中 12 个不在检查内(假阴性); ②`git add .` 无 .gitignore 防护(repo 根**无 .gitignore**, dir_structure 目录树里 `.mavis/`(logs/backups/pdfbuild) 也在上传清单——私密目录公开泄露风险) | ✅ 已修: guard 扩为全 16 frozen 路径模式(FROZEN_PAT, skill_d 合法改动特例注释) + 新增 Step 3.5(.gitignore 缺失即 exit 1) |
| A3 | 🔴 严重 | **skill_d(frozen `3e369a1f6171`) 未落实上轮 risk2 followup**: L193-205 仍是占位链(56adce 系)拼接 vs `ae80bbba4f7b` 期望, 既无 trust_anchor 值系(d78c42 系)拼接, 也无新锚 `79f8dfa2c296`; 修复点 3 的"先派生后 fallback"读取顺序同样未体现 | ⛔ **不可代修**(frozen): 报告 Mavis, 下次 user 拍板 skill_d 时一并落实(与上轮回信附 3 第 2 条同源, 被跳过) |
| B4 | 🟡 中 | **runner_pa_d1_d3.py L70 FROZEN_16 期望值滞后** `f4c68d146141`——第 3 个 race 残留副本(修了 _verify_15frozen + _verify_pg_v0, 漏了 runner_pa; 全仓 grep 拿齐) | ✅ 已修: reconcile + 审计痕迹(与 FROZEN POLICY 协议一致) |
| B5 | 🟡 中 | **D5_DECISIONS_LAND_REPORT §3A 引用旧名**(boss_pc_N_attack/boss_pe_* 表格与 verdict 表)——上轮修复 1 勘误只加了 P_C_D1_D3_REPORT, **漏了 D5 报告**(我上轮覆盖面遗漏); 且 D5 报告 L175 "boss_pe_* 测 P-E" 与预注册报告 §4 "BOSS P-C1/2/3 测 P-C 两相" 存在**语义归属分歧** | ✅ 已修: 勘误块追加(旧名映射 + Ising 系 BOSS verdict 标 **PENDING_MAVIS_REVIEW** 待语义锚定) |
| B6 | 🟡 中 | **github_dir_structure_2026_09_18.md 引用旧名**(L71-73)——该文件是 D7 打包清单, 不勘误则 D7 按旧名找文件 | ✅ 已修: 文件尾勘误块(现行名映射) |
| C7 | 🟢 轻 | **boss_pa_1/2/3 实跑脚本无 SELF-CHECK 尾块**——上轮修复点 7 只覆盖委托信所列 9 脚本, boss_pa 属范围外(委托信盲区实例, 正是本次主动审查的价值证明) | ✅ 已修: 补尾块(标记 TRAE_SELFCHECK_2026_09_16_PA: 文件名防漂移 + result JSON round-trip + boss_pa_1 判定线注释) |
| C8 | 🟢 轻 | skill_d `one_week_status` 硬编码 `today=2026-09-11`(L220)——重跑会恒报 days_remaining=7 | ⛔ **不可代修**(frozen): 报告 Mavis |

## §1 语义归属分歧详注(B5, 需 Mavis 裁决)

同组三个 Ising BOSS(2D Ising/transverse/reservoir)在两份 Mavis 报告中有**互相矛盾的归属声明**:

| 文件 | 声明 | 时间 |
|---|---|---|
| `P_C_D1_D3_REPORT_2026_09_15.md` §4 | 预注册为 **P-C BOSS**(boss_pc_1/2/3, 测 P-C 两相结构是否 Ising 特例) | 09-15(预注册, 先) |
| `D5_DECISIONS_LAND_REPORT_2026_09_15.md` §3A | 落盘为 **P-E BOSS**(boss_pe_1/2/3, "测 P-E 3-modality 是否 Ising 特例", 文件 docstring 同) | 09-15(D5 3A, 后) |

我上轮改名按**预注册优先**锚定 P-C(boss_pc_1/2/3), 但两者物理语义不同(P-C 两相 R² vs P-E 三模态守恒), D_fix2 序列在两个解释下都能跑——**verdict 表(BOSS-PC-1 GRAY / PC-2 PASS / PC-3 PASS)在语义锚定前应视为 PENDING_MAVIS_REVIEW**, 已写入 D5 报告勘误块。请 Mavis 复核: 若锚 P-C(预注册优先), verdict 语义成立; 若锚 P-E, 需按 P-E 口径重判。

## §2 机械自审本轮战果(3 个新缺陷被 SC 当场抓出, 透明记录)

| # | 缺陷 | 修正 |
|---|---|---|
| 1 | DIRS_ANCHOR 锚点用 tree 对齐空格——空格数不精确即挂(脆弱锚点) | 改尾部追加策略 |
| 2 | **B6 幂等 marker 与块文本不一致**(块头手写短版"主动审查**", 幂等检查用 ERR_MARKER 完整串)→ 幂等永假 → 首跑重复追加 2 次 | 块文本统一 ERR_MARKER + 归一化逻辑(2 个重复尾段裁齐为 1)——**这正是 fix_risk1 幂等 bug 的同型缺陷, 我在同一位置又犯** |
| 3 | A2 复核断言 `count('skill_c...') >= 2` 想当然(verify 是脚本调用非内联清单, 实际 1 次) | 修 >= 1 |

累计 5 轮合作, 机械自审共抓出 **11 个首跑缺陷**(Mavis 侧 3 + 我侧 8)——"SELF-CHECK 前置 = 不允许带病落盘"持续兑现, 包括对我自己。

## §3 修复验证链

- `fix_proactive_audit_2026_09_16.py` 二跑全 PASS(幂等: 第二遍全部"跳过" + SC 全过)
- 修后终验: `_verify_15frozen.py` **16/16 PASS**
- 16 frozen patch 前后两核 0 触动(skill_d `3e369a1f6171` 合法改动条目原样)
- 历史工件零改写: 6 个 boss_*.json 历史结果 + .tmp/ 运行记录 + 各报告历史文本全部保留

## §4 留给 Mavis 的清单(按优先级)

1. 🔴 **A3**: skill_d 下次拍板时落实 risk2 followup——canonical 段换 trust_anchor 值系 + 新锚 `79f8dfa2c296` + 修复点 3 读取顺序(先派生 value_v3x_new, fallback 旧值)
2. 🔴 **B5 语义裁决**: Ising 系 BOSS 锚 P-C(预注册)还是 P-E(D5 口径)? 锚定前 3 个 verdict 挂 PENDING_MAVIS_REVIEW
3. 🟡 C8: skill_d `today=2026-09-11` 硬编码改 `datetime.date.today()`(同下次拍板窗口)
4. 🟡 D7 打包执行 `github_upload_2026_09_18.sh` 前先建 repo 根 `.gitignore`(至少排除 `.mavis/` `.tmp/` `results/_worker_temp/`)
5. 🟢 commit msg 占位符 D7 实测后填真值——**禁止在实测前回填**(本次占位符化的全部意义所在)

—— Trae code, 2026-09-16
