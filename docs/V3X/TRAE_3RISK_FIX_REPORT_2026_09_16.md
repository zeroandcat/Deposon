# Trae 修 8 修复点综合报告 (2026-09-16)

> **委托**: `LETTER_TO_TRAE_REVIEW_2026_09_16.md`(Mavis, 任务 ID DEPSON-TRAE-REVIEW-2026-09-16, 沿 user 2026-09-15 13:39 指令)
> **执行**: Trae code — successor 裁定 + reviewer-a 静态审 + reviewer-b 机械自审(断言嵌入 patch) + 二跑验证
> **方法**: 0 LLM / 0 网络 / 0 key; 纯 Python stdlib; 判定线全部预注册
> **frozen**: 修前双跑(16/16 PASS + **15/16 FAIL**[_verify_pg_v0 skill_d 期望值滞后, race 残留实锤]) → 修后双跑(**16/16 + 16/16 全 PASS** + P-G spec 2f0765a1d39d + P-G 5 锚占位 recomputed 5/5 PASS)

---

## §0 八修复点裁定一览

| # | 修复点 | 裁定 | 一句话 |
|---|---|---|---|
| 1 | boss_pc 命名一致性 | **option_C** | 预注册回正: Ising 系实跑脚本(曾被 D5 以 P-E 框架落盘为 boss_pe_*)改名回报告 §4 预注册名 boss_pc_1/2/3; 攻击脚本移出 boss_ 命名空间 |
| 2 | race condition | ✅ 已 reconcile | _verify_pg_v0.py skill_d 期望值 f4c68d146141 → 3e369a1f6171(Mavis 只更新了 _verify_15frozen.py, 残留即信中 BOSS-PE-3 worker 观察到的 1/15 FAIL) |
| 3 | 5 锚 JSON 派生补丁 | **option_A** | 派生 JSON 保持独立; 读取顺序(先派生 value_v3x_new, fallback 5 锚旧值)写入 FROZEN POLICY 注释; D7 后统一 reconcile。option B 否决: 保持 03c6c01f3697 同时改内容在 SHA 语义上不可能 |
| 4 | boss_pg SCAFFOLDING | **option_A** | 保持 scaffolding——540-LLM 数据(bg_44d89fa8)未落盘 + 王老师未拍板, 提前升实跑违反预注册纪律; 风格差异是分阶段管线非 bug |
| 5 | 命名 vs 内容 | **option_C** | 与修复点 1 同一裁定: BOSS(普适类自测, boss_ 前缀)与 Attack(KT-C1 §5 抗攻击检查, attack_ 前缀)两条独立命名轴, 每文件单一语义, 不混合 |
| 6 | frozen 列表动态冻结 | ✅ 已写注释 | "动态冻结 + reconcile 协议"政策块插入 _verify_15frozen.py(拍板记录→OLD→NEW 审计痕迹→其余条目须全 PASS); 附修 "TOTAL: 15"标签 bug(实为 16 项) + NEWLY LANDED 指针刷新 |
| 7 | P-F V0.1 §5 预注册纪律 | ✅ 已落地 | 9 个 boss/attack 脚本全部追加 SELF-CHECK 尾块(标记 TRAE_SELFCHECK_2026_09_16: 文件名防漂移 + 预注册常数锁定 + OUT round-trip + scaffolding TODO 锁定); 2 个 patch 脚本自带预注册判定线 + SELF-CHECK + 二跑 |
| 8 | 7 铁律 0 触动 | ✅ PASS | 修前/修后两轮 verify: 16 frozen + P-G V0 + P-G V0.1 全 0 触动(skill_d 为 user 12:01 拍板 1A 合法改动, 已带审计痕迹 reconcile) |

## §1 修复点 1/5 详解 — 矛盾真相与裁定依据

**取证发现的实况比委托信描述更立体——是双重错位, 不是单点命名冲突**:

| 资产 | 报告 §4 预注册(2026-09-15) | D5 3A 实际落盘 | 矛盾 |
|---|---|---|---|
| 2D Ising / transverse / reservoir | `boss_pc_1/2/3_<ising 名>`(P-C 槽位) | 落成 `boss_pe_1/2/3`(P-E 框架, "检查 P-E 3-modality 是否 Ising 特例") | Ising 系实跑脚本**占了错的命名空间** |
| 攻击测法 A1/A2/A3 | 未预注册为 BOSS(KT-C1 SPEC §5 是另一条轴) | 落成 `boss_pc_N_attack_*`(占了 boss_pc_N 编号槽) | 攻击脚本**占了 BOSS 槽位** |

**option_C 裁定**(A/B 均否决):
- 否决 A(把攻击脚本改名成 Ising 并改内容): 会销毁 D5 3A 已实跑的攻击实现
- 否决 B(把报告 §4 改成攻击命名): 会让预注册的 BOSS 普适类自测失去文件槽位
- **采纳 C**: 两个实跑都保留, 各回其位——`boss_pe_*` 改名回预注册名 `boss_pc_1_2d_ising_universality.py` 等(内容零改动, docstring 框架回正 P-C, D5 1A D_fix2 方法保留); 攻击脚本移出 boss_ 命名空间 → `attack_pc_a1/a2/a3_*.py`; 报告 §4 追加勘误块(不重写历史)

**历史工件保全**: 6 个 D5 3A 结果 JSON(boss_pe_*_real_* / boss_pc_*_a*_*_2026_09_15.json)全部原样保留; 改名后脚本 OUT 指向新规范名, 重跑写新文件不覆盖历史。改名安全性预核: grep 全仓确认无 frozen 文件引用 boss_pe/boss_pc 旧名(引用仅在 boss 文件自身与 非 frozen worker 临时脚本)。

## §2 修复点 2 详解 — race 残留闭环

修前基线双跑实锤: `_verify_15frozen.py` 16/16(Mavis 已 reconcile skill_d) vs `_verify_pg_v0.py` **15/16 FAIL**(期望值仍是旧 f4c68d146141)——两个 verify 工具在 D5 并发窗口内只被同步了一个。本 patch 按同一 reconcile 协议补齐第二个, 并把协议本身写进 FROZEN POLICY 注释(下次拍板改动只需照协议走, 不再有"漏更一个脚本"的 race 面)。后续 race 处理沿 P-D V0.1.2 "无参 + 临时副本自建"风格 + patch 幂等保护(两个 patch 均已内置)。

## §3 修复点 3 详解 — 派生 JSON 读取顺序(option_A)

- 裁定: 派生 JSON(`KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json`, SHA-12 `da517c115f3c`)保持独立; 下游读 P_A_LLM_CLIENT/P_A_HARNESS 先取派生 value_v3x_new(`1722500da4aa`/`275e480ba4d9`), fallback 5 锚旧值; D7 后 5 锚 JSON V0.2/V3X 正式升级统一 reconcile
- option B 否决依据: "保持 `03c6c01f3697` 的同时把新 SHA 写入 5 锚 JSON 自身"在 SHA 语义上不可能——文件内容一变指纹必变, 该选项是自相矛盾任务
- 政策已写入 `_verify_15frozen.py` FROZEN POLICY 注释块; 实际消费者接线(runner_pa 等)属 Mavis D7 工作, 不代改

## §4 修复点 4 详解 — boss_pg 保持 SCAFFOLDING(option_A)

三个 boss_pg 自身 docstring 即预注册("awaiting D5 launch + 王老师 WeChat拍板"); 540-LLM 数据仍在 bg_44d89fa8 跑批; **提前升实跑 = 违反我们正在落实的预注册纪律**。与 boss_pc(已实跑)的风格差异是分阶段管线, 非 bug。升级路径已锁定: D7 拍板后按 P-F V0.1 §5 同款流程(预注册常数已在位 → 实跑 → SELF-CHECK 全过 → 二跑)。本任务给 boss_pg 追加的 SELF-CHECK 仅锁定 scaffolding 状态(TODO 标记 + 常数一致), 防止未拍板被静默实跑。

## §5 修复点 7 详解 — SELF-CHECK 尾块(9 脚本)

| 脚本 | 尾块断言 |
|---|---|
| boss_pc_1(2D Ising) | 文件名防漂移 + ISING_BETA_2D==0.125 + 容差序 + D_fix2 阈值序 + 基准 [0.8667, 0.0333] + OUT round-trip |
| boss_pc_2(transverse) | PFEUTY_H_C_OVER_J==1.0 + 容差序 + D_fix2 + 基准 + OUT round-trip |
| boss_pc_3(reservoir) | SPEARMAN 容差序 + D_fix2 阈值序 + OUT round-trip |
| attack_pc_a1/a2/a3 | 预注册阈值(0.15/0.90/0.7) + N 档一致性(a3: N_CLIPPED⊂N_FULL 且 -2 档) + OUT round-trip |
| boss_pg_1/2/3 | 文件名 + 预注册常数(pg_1)+ **TODO 标记锁定**(scaffolding 防静默实跑) |

## §6 机械自审首跑抓出的缺陷(第 3 次现场示范, 透明记录)

| # | 缺陷 | 处置 |
|---|---|---|
| 1 | fix_verify_freeze_policy 初版断言 `'f4c68d146141' not in spg` **自相矛盾**——新条目的审计痕迹文本合法包含旧值("OLD f4c68d146141 → NEW 3e369a1f6171"), 断言必挂 | 修为"旧期望值**元组**不得残留"(OLD_SKILLD_PG not in spg); 修正过程已注释在脚本内。reconcile 本身首跑即成功(终验 16/16 实证), 缺陷仅在断言表达式 |

两次跑(首跑执行 + 复跑幂等)均 ALL PASS。与前两次合作(fix_risk1 键名/顺序 bug、fix_risk3 Spearman==1.000 过强断言被实算 0.9958 否定)同模式: **SELF-CHECK 前置 = 不允许带病落盘**。

## §7 交付清单

| 项 | 路径 | 状态 |
|---|---|---|
| patch 1(修复 1/5/7) | `deposon_team/plugins/fix_boss_naming_2026_09_16.py` | ✅ 二跑 ALL PASS |
| patch 2(修复 2/3/6) | `deposon_team/plugins/fix_verify_freeze_policy_2026_09_16.py` | ✅ 二跑 ALL PASS |
| 6 文件改名 | boss_pe_1/2/3 → boss_pc_1/2/3; boss_pc_N_attack → attack_pc_a1/a2/a3 | ✅ 旧名清零 |
| 9 脚本 SELF-CHECK 尾块 | 标记 TRAE_SELFCHECK_2026_09_16 | ✅ |
| 报告勘误 | `P_C_D1_D3_REPORT_2026_09_15.md` §4 追加勘误块 | ✅ |
| verify 工具 | `_verify_15frozen.py`(POLICY 注释+标签修+指针刷) / `_verify_pg_v0.py`(skill_d reconcile) | ✅ |
| 修后终验 | 16/16 + 16/16 + P-G spec + P-G 5 锚 5/5 | ✅ 全 PASS |
| 综合报告 | 本文件 | ✅ |
| 回信 | `LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | ✅ |

## §8 7 铁律严守声明

0 LLM 调用 ✓ / 0 proxy ✓ / 0 网关 ✓ / key 不入 prompt-JSON-落盘(未读任何 key 文件)✓ / 5 锚 JSON `03c6c01f3697` 0 触动 ✓ / 16 frozen 0 触动(skill_d 为 user 12:01 拍板 1A 合法改动, reconcile 带审计痕迹)✓ / 不动 verifier/mavis/.builtin/scripts/ ✓ / 未创建临时文件(patch 脚本落 plugins/ 属委托信 §0.4 明确许可)✓

## §9 遗留给 Mavis(复审要点)

1. 双审两个 patch + 9 个尾块(沿委托信 §12 纪律)
2. boss_pc_1/2/3 重跑时写新 OUT 路径(results/boss_pc_*_2026_09_15.json), 历史 boss_pe_* 结果保留不动
3. D7 后 5 锚 JSON V0.2/V3X 升级时, 按派生 JSON metadata.note 统一 reconcile P_A_LLM_CLIENT/P_A_HARNESS
4. boss_pg_* 升实跑须等 540-LLM 数据落盘 + 王老师拍板, 升级沿 P-F V0.1 §5 流程
5. P-G V0 spec 5 锚占位为"手填=手算"生成(非算法生成), _verify_pg_v0 已给 recomputed 全 PASS——建议 spec 升级时改算法生成留工件(沿 R3 erratum 工件三件套原则)

—— Trae code, 2026-09-16
