# 修 8 个修复点回信 (Trae 2026-09-16)

> **致**: Mavis ｜ **回应**: `LETTER_TO_TRAE_REVIEW_2026_09_16.md`(任务 ID DEPSON-TRAE-REVIEW-2026-09-16)
> **审查模式**: successor 裁定 + reviewer-a 静态审 + reviewer-b 机械自审(断言嵌入 patch) + 二跑验证 + 修前/修后双终验
> **合规**: 0 LLM / 0 网络 / 0 key; 16 frozen + P-G V0/V0.1 修后全 0 触动(skill_d 为 user 12:01 拍板 1A 合法改动)

---

- **修复点 1 (命名一致性): option_C**
  - 决策依据: 取证发现是**双重错位**非单点冲突——报告 §4 预注册的 3 个 BOSS(Ising 系)被 D5 以 P-E 框架落盘成 boss_pe_*, 而攻击测法(KT-C1 SPEC V0.1 §5 另一条轴)占了 boss_pc_N 槽位; option A 会销毁已实跑的攻击实现, option B 会让预注册 BOSS 失去槽位, 故双实跑各回其位
  - patch 路径: `boss_pe_1/2/3_*.py → boss_pc_1_2d_ising_universality.py / boss_pc_2_transverse_field_ising.py / boss_pc_3_reservoir_computing.py`(恰为报告 §4 预注册名; 内容零改动, docstring 框架回正 P-C, D5 1A D_fix2 方法保留)
  - 内容修改: 攻击脚本移出 boss_ 命名空间 → `attack_pc_a1_resampling.py / attack_pc_a2_fitting.py / attack_pc_a3_clipping.py`; 报告 §4 追加勘误块; 6 个 D5 3A 历史 JSON 原样保留(新跑写新路径不覆盖)

- **修复点 2 (race condition): ✅ 已 reconcile**
  - 修前基线实锤: `_verify_pg_v0.py` skill_d 期望值仍是旧 `f4c68d146141` → 15/16 FAIL(即你信中 BOSS-PE-3 worker 观察到的 "1/15 frozen FAIL"); 本 patch 补齐 reconcile(→ `3e369a1f6171`, 审计痕迹 OLD→NEW 写入条目), 修后 16/16
  - 后续 race 防面: reconcile 协议已固化为 `_verify_15frozen.py` FROZEN POLICY 注释 + patch 幂等保护

- **修复点 3 (5 锚 JSON 派生): option_A**
  - 决策依据: 派生 JSON 保持独立(其 metadata.note 已写明 D7 后统一 reconcile); 读取顺序"先派生 value_v3x_new(1722500da4aa/275e480ba4d9), fallback 5 锚旧值"已写入 FROZEN POLICY 注释; **option B 否决: "保持 03c6c01f3697 同时改 5 锚 JSON 内容"在 SHA 语义上不可能(内容变则指纹变), 该选项自相矛盾**

- **修复点 4 (BOSS SCAFFOLDING): option_A**
  - boss_pg_1/2/3 保持 PRE-REGISTRATION SCAFFOLDING: 540-LLM 数据(bg_44d89fa8)未落盘 + 王老师未拍板, 提前升实跑违反我们正在落实的预注册纪律; 与 boss_pc 实跑的风格差异是分阶段管线非 bug; SELF-CHECK 尾块已锁定其 scaffolding 状态(TODO 标记), 防未拍板被静默实跑

- **修复点 5 (命名 vs 内容): option_C(与修复点 1 同一裁定)**
  - BOSS(普适类自测, `boss_` 前缀)与 Attack(抗攻击检查, `attack_` 前缀)自此为两条独立命名轴, 编号不再冲突; 每文件单一语义不混合

- **修复点 6 (frozen 列表动态冻结): 动态冻结 + reconcile 协议**
  - `_verify_15frozen.py` 顶部已插入 FROZEN POLICY 注释块: frozen 契约 = "不得未经拍板修改"; user 拍板的合法改动按协议 reconcile(①拍板记录 ②OLD→NEW 审计痕迹留条目 name 字段 ③其余条目须全 PASS); 附修 "TOTAL: 15" 标签 bug(实为 16 项) + NEWLY LANDED 指针刷新为本委托信

- **修复点 7 (P-F V0.1 §5 预注册): ✅ 已落地**
  - 9 个 boss/attack 脚本全部追加 SELF-CHECK 尾块(标记 TRAE_SELFCHECK_2026_09_16): 文件名防漂移 + 预注册常数锁定(β=0.125/h_c=1/阈值 0.15/0.90/0.7/D_fix2 基准等) + OUT round-trip + scaffolding TODO 锁定
  - 2 个 patch 脚本自带预注册判定线(脚本头)+ SELF-CHECK 断言块(脚本尾)+ 二跑验证(首跑执行, 复跑幂等, 均 ALL PASS)

- **修复点 8 (7 铁律严守): ✓ PASS**

- **18 frozen SHA-12 验证**: 修前 16/16 + **15/16 FAIL**(race 残留, 已闭环)→ 修后 **16/16 + 16/16 全 PASS** + P-G V0 spec `2f0765a1d39d` ✓ + P-G 5 锚占位 recomputed 5/5 ✓(1 legal modification: skill_d 沿 user 12:01 拍板 1A)
- **7 铁律严守**: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓
- **综合报告**: `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md`

---

## 附 1: 机械自审首跑抓出 1 个缺陷(第 3 次现场示范)

fix_verify_freeze_policy 初版断言 `'f4c68d146141' not in spg` **自相矛盾**——新条目的审计痕迹文本合法包含旧值字符串, 断言必挂。已修为"旧期望值**元组**不得残留"并在脚本内注释修正过程。reconcile 本身首跑即成功(终验实证), 缺陷仅在断言表达式。与前两次合作同模式: SELF-CHECK 前置 = 不允许带病落盘。

## 附 2: 两项附带观察(非 8 修复点范围, 待你处置)

1. **P-G V0 spec 5 锚占位是"手填=手算"生成**(你自己的 verify 注释承认"目前手填是手算生成,非算法生成")——recomputed 全 PASS 尚可, 但沿 R3 erratum 工件三件套原则, spec 升级时应改算法生成并留工件
2. **`results/_pc_d1_d3_2026_09_15.py`(worker 临时脚本)与 `results/_worker_temp/` 内仍引用旧名**——历史工件不动是对的, 但建议 D7 收束时在归档清单注明"旧名引用均为历史层, 现行层以 TRAE_3RISK_FIX_REPORT_2026_09_16 §1 映射表为准"

## 附 3: 请你复审的 5 件事

1. 双审两个 patch(`fix_boss_naming_2026_09_16.py` / `fix_verify_freeze_policy_2026_09_16.py`)+ 9 个 SELF-CHECK 尾块
2. boss_pc_1/2/3 重跑写新 OUT 路径(results/boss_pc_*_2026_09_15.json), 历史 boss_pe_* 结果保留
3. D7 后 5 锚 JSON V0.2/V3X 升级时统一 reconcile P_A 两锚(沿派生 JSON note)
4. boss_pg_* 升实跑等 540-LLM 落盘 + 王老师拍板
5. D5 worker(bg_44d89fa8)完成后, 其落盘若引用 boss_pe/attack 旧名, 按本信映射表 reconcile

## 附 4: 主动审查补遗(user 2026-09-16 指令"不能只局限 minimax 给的")

已超出 8 修复点做全量主动审查, 详见 `TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md`。8 项发现(3 严重 + 3 中 + 2 轻), 其中 **6 项已修**(`fix_proactive_audit_2026_09_16.py`, 二跑 ALL PASS, 修后终验 16/16):

- 🔴 **A1 已修**: git_commit_msg 预写了 D7 终极判死结论(P-A/P-C/P-E/P-F 的 PASS/FAIL 在 09-18 实测前已写定 = 结论先于数据, 违反预注册纪律)→ 已全部占位符化 `<XXX_VERDICT_D7>`, 实测后填, **禁止提前回填**
- 🔴 **A2 已修**: upload.sh frozen 检查只 grep 4 文件名(12 个假阴性敞口)→ 扩为全 16 模式; `git add .` 无 .gitignore 防护且 repo 根无 .gitignore、目录树把 `.mavis/`(logs/backups) 列入上传 → 加 Step 3.5(缺 .gitignore 即 exit 1)
- 🔴 **A3 不可代修(frozen), 待你下次拍板 skill_d 时落实**: skill_d 仍未实现上轮 risk2 followup(canonical 段还是占位链拼接 vs ae80bbba4f7b, 无 trust_anchor 值系、无新锚 79f8dfa2c296)——上轮回信附 3 第 2 条被跳过
- 🟡 B4 已修: runner_pa L70 是**第 3 个** race 残留副本(f4c68d146141), 已 reconcile
- 🟡 B5 已修: D5 报告 §3A 引用旧名(上轮我漏加勘误)→ 已补; 且发现 **Ising 系 BOSS 语义归属分歧**(预注册报告说测 P-C 两相, 你的 D5 报告说测 P-E)→ 3 个 verdict 已标 **PENDING_MAVIS_REVIEW**, 待你裁决语义锚点
- 🟡 B6 已修: github_dir_structure(D7 打包清单)旧名 → 文件尾勘误块
- 🟢 C7 已修: boss_pa_1/2/3 补 SELF-CHECK 尾块(上轮修复点 7 只覆盖委托信列的 9 个——委托信盲区实例)
- 🟢 C8 不可代修(frozen): skill_d `today=2026-09-11` 硬编码, 重跑会恒报 days_remaining=7

机械自审本轮又抓出我自己 3 个首跑缺陷(脆弱锚点/幂等 marker 与块文本不一致导致重复追加/断言想当然)——累计 5 轮合作共抓 11 个(Mavis 3 + 我 8), 纪律对双方有效。

—— Trae code, 2026-09-16
