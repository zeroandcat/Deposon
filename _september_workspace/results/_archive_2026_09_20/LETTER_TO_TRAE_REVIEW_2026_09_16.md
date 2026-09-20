# 致 Trae:deposon V3X 审核 + 修复代码委托信(2026-09-16)

> **致**: Trae code(Mavis → Trae 双工模式,沿 P_F_SPEC V0 + V7 §8.A + v3 §6 + P-D V0.1.2 "无参+临时副本自建"风格)
> **发自**: Mavis(任务 ID DEPSON-TRAE-REVIEW-2026-09-16,沿 user 2026-09-15 13:39 指令)
> **日期**: 2026-09-15 13:46
> **配套**:
> - `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` (D5 决策落盘综合报告, 20292 B, SHA-12 `a229c3248f79`)
> - `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` (3 风险修正报告, 沿 Trae fix 基础)
> - `deposon_team/plugins/_verify_15frozen.py` (16 frozen + P-G V0/V0.1 verify 工具)
> - `deposon_team/plugins/_verify_pg_v0.py` (P-G 5 锚算法预注册 verify 工具)
> - `docs/V3X/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` (上一封委托信, 沿 Trae 完成 3 风险修)
> **严守**: 7 铁律 0 触动(0 LLM / 0 proxy / 0 网关 / key 不入 prompt/JSON/落盘 / 不动 18 frozen / 不动 verifier/mavis/.builtin/scripts/ / 不创建临时文件)
> **触发**: user 2026-09-15 13:39 "准备这周内全额收束...适时安排暂停进度并写信让trea审核与修复代码"

---

## §0 委托原则(Trae 必读,沿 V3X + Trae 上一次合作模式)

1. **0 LLM 严守**:本审核 + 修复全程纯 Python stdlib (json + hashlib + math + numpy), 0 LLM calls
2. **不动 18 frozen**(沿 `_verify_15frozen.py` 验证):
 - 5 锚 JSON `03c6c01f3697`
 - 4 SPEC V0.1 (`78b71d404366` / `0410ca0fbdae` / `59d8f56347d5` / `cce8e9a1b00e`)
 - P-F V0.1 upgrade `b10fae0da66d`
 - v19/v21/corpus_v20 (`910c4333eead` / `9d9ae5001c57` / `8423ffe266af`)
 - P-F V0 + placeholder + research (`b41c98bf90cc` / `de90faf362c5` / `98085df7811a`)
 - skill_a/b/c plugin (`b1463bb24403` / `e5a299f69a22` / `e19e76c5da7e`)
 - skill_d plugin `3e369a1f6171` (沿 user 12:01 拍板 1A 合法改动, 严守不再动)
 - P-G V0 spec `2f0765a1d39d`
3. **不动 verifier/mavis/.builtin/scripts/ 目录**
4. **修 8 个修复点** 在 `deposon_team/plugins/fix_*.py` 新建(用户可选用),或 在 `/tmp/fix_*.py` 临时目录新建(不落盘)→ 修后让 Mavis 复审
5. **key 永不入 prompt / JSON / 落盘**: 不读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt`, 如必须读, 用 `Path().read_text()` runtime 读
6. **0 触动声明**: Trae 修复完后, 须 verify 18 frozen 文件 SHA-12 全 0 触动(沿 §7 验证表 + `_verify_15frozen.py` 双跑)
7. **判定线预注册**: 沿 P-F V0.1 §5 纪律, 计算前锁定判定线, SELF-CHECK 断言块(任一失败不落盘)
8. **D5 (09-16) 当前状态**: bg_44d89fa8 worker 后台跑批(540 LLM), 预计 ~1-2h 完成

---

## §1 修复点 1:命名一致性(boss_pc_* 命名 vs P-C D1-D3 §4 命名)

### 1.1 矛盾描述(Mavis 已实算完整)

D5 worker 在 3A 落盘时,文件名沿 P-C V0 spec §5 攻击测法:
- `deposon_team/plugins/boss_pc_1_attack_a1_resampling.py`
- `deposon_team/plugins/boss_pc_2_attack_a2_fitting.py`
- `deposon_team/plugins/boss_pc_3_attack_a3_clipping.py`

但 P-C D1-D3 worker报告 §4 描述 BOSS 命名:
- BOSS P-C1: 2D Ising universality
- BOSS P-C2: Transverse field Ising
- BOSS P-C3: Reservoir Computing

**矛盾**: D5 worker落盘文件名(攻击测法 A1/A2/A3)与 P-C D1-D3 报告描述(2D Ising 等)不一致。

### 1.2 期望修复(沿 Trae 选择)

**选项 A**(推荐): 把 `boss_pc_1_attack_a1_resampling.py` 重命名为 `boss_pc_1_2d_ising_universality.py`, etc. — 内容也对应改成 2D Ising universality
**选项 B**: 把 P-C D1-D3 报告 §4 改名 (从 "2D Ising 等" 改为 "Attack A1/A2/A3") — 内容已经对应攻击测法
**选项 C**: 沿 Trae 自主判断(命名 vs 内容哪个优先)

### 1.3 严守

- 改名后 verify `boss_pc_*` 新文件名 SHA-12 写入 `_verify_15frozen.py` 期望值(如果新增到 frozen list)
- 内容必须沿 P-C V0 spec §5 攻击测法 OR 2D Ising universality (二选一, 不能混合)
- 不动 16 frozen 中其他文件

---

## §2 修复点 2:race condition(boss_pc_* vs P-C dpath worker 同步)

### 2.1 矛盾描述

2026-09-15 12:54 P-C dpath worker (`bg_769042b6`) 在 Step 1 探查时判断"实跑冗余",未落盘最终文件。
2026-09-15 13:32-13:33 D5 worker (`bg_447381e3`) 落盘 `boss_pc_*` 真实脚本。

两个 worker 都在 ~30 分钟窗口内运行,存在 race condition:
- P-C dpath worker 在 Step 1 后退出, 没影响 boss_pc_* 落盘
- 但 D5 worker 修改 skill_d 时 (13:30:57), 与其他 worker 可能同时跑

**race condition 检查**: skill_d 13:30:57 修改(沿 user 12:01 拍板 1A), 其他 worker mtime:
- D5 worker 报告: Step 4 boss_pc_* 13:32:12-13:33:57(后于 skill_d 改动)
- BOSS-PE-3 worker: 报告 §注意事项 "verifier 显示 1/15 frozen FAIL: `skill_d_p_f_observer.py`" — **这正是 race condition 实证**

### 2.2 期望修复

- Trae 沿 Mavis `_verify_15frozen.py` reconcile 方式(已沿 user 12:01 拍板 1A update 期望值),继续更新 verify 脚本
- 沿 P-D V0.1.2 "无参 + 临时副本自建" 风格处理后续 race condition
- 在每个修复 patch 脚本顶部加 `# DECISION: option_X` 标注 + 幂等保护(已 patch 则跳过)

### 2.3 严守

- 修复 patch 后, Mavis verify 18 frozen 全 0 触动(除 skill_d 合法改动)
- `_verify_15frozen.py` 期望值与实算一致

---

## §3 修复点 3:5 锚 JSON 派生补丁(沿 P-D V0.1.2 风格统一)

### 3.1 矛盾描述

D5 2A 决策落盘 worker 创建了派生 JSON:
- `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` (5049 B, SHA-12 `da517c115f3c`)

这是沿 P-D V0.1.2 "无参 + 临时副本自建" 风格, 但:
- 5 锚 JSON 自身 `03c6c01f3697` 0 触动 ✓
- 下游读 P_A_LLM_CLIENT 时, 派生 JSON 与 5 锚 JSON 不同步
- D7 后需统一 patch 5 锚 JSON 还是保持派生 JSON 独立?

### 3.2 期望修复(沿 Trae 选择)

**选项 A**(推荐):保持派生 JSON 独立,下游读 P_A_LLM_CLIENT 时**先查派生 JSON, fallback 5 锚 JSON**
**选项 B**: D7 后统一 patch 5 锚 JSON,把 P_A_LLM_CLIENT + P_A_HARNESS 新 SHA 写入 5 锚 JSON 自身(需要找到保持 `03c6c01f3697` 的方式)
**选项 C**:沿 Trae 自主判断

### 3.3 严守

- 任何修改必须保持 5 锚 JSON 自身 SHA-12 `03c6c01f3697` (沿 P-D V0.1.2 派生风格)
- 派生 JSON 可独立 SHA-12(已落盘 `da517c115f3c`)

---

## §4 修复点 4:4 BOSS SCAFFOLDING(boss_pg_* 落盘风格统一)

### 4.1 矛盾描述

P-G V0.1 worker 落盘 3 个 BOSS SCAFFOLDING:
- `deposon_team/plugins/boss_pg_1_riemannian_degenerate.py`
- `deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py`
- `deposon_team/plugins/boss_pg_3_geodesic_violation.py`

但 boss_pe_* 升级后是实跑(沿 D5 3A 拍板),boss_pg_* 还是 SCAFFOLDING。**风格不统一**。

### 4.2 期望修复(沿 Trae 选择)

**选项 A**(推荐):保持 boss_pg_* 为 SCAFFOLDING(沿 P-F V0.1 §5 预注册,真实实跑等 D7 后)
**选项 B**:把 boss_pg_* 升级为实跑,沿 P-G V0.1 实算数据(540 cells)做 BOSS 自测
**选项 C**:沿 Trae 自主判断

### 4.3 严守

- 沿 P-F V0.1 §5 判定线预注册纪律
- 不动 P-G V0 spec (`2f0765a1d39d`) + P-G V0.1 5 锚(已实算)
- boss_pg_* 修改后 verify 不破 0 触动声明

---

## §5 修复点 5:命名 vs 内容(沿 P-C V0 spec §5 vs P-C D1-D3 §4)

### 5.1 矛盾描述

D5 worker 落盘 boss_pc_* 是沿 P-C V0 spec §5 攻击测法(A1 resampling / A2 fitting / A3 clipping),但内容没明示攻击测法 vs 2D Ising。

需要明确:
- boss_pc_1 内容是 2D Ising universality (P-C D1-D3 §4) 还是 A1 resampling (P-C V0 §5)?
- 二选一,**不能混合**(沿 Trae 修正)

### 5.2 期望修复

- Trae 选择二选一(2D Ising universality 或 A1 resampling)
- 修改 boss_pc_1/2/3 内容与命名一致
- 内容必须在 patch 脚本顶部加 `# DECISION: option_X` 标注

### 5.3 严守

- 内容修改不破 7 铁律
- boss_pc_* 修改后 verify 沿 P-C V0 spec §A BOSS 测法

---

## §6 修复点 6:frozen 列表动态冻结(_verify_15frozen.py reconcile)

### 6.1 矛盾描述

skill_d plugin 沿 user 12:01 拍板 1A 改动(SHA `f4c68d146141` → `3e369a1f6171`),`_verify_15frozen.py` 期望值已 update。

但**frozen 列表动态冻结**的含义需要明确:
- frozen 约束是"不动文件",但文件 SHA 的"契约值"在 user 拍板后可由 verifier 同步 reconcile
- 还是 frozen 一旦设定就永远不变?

### 6.2 期望修复

Trae 在 `_verify_15frozen.py` 顶部加注释,说明:
- "frozen 列表是"动态冻结",user 拍板后可由 verifier reconcile"
- 或 "frozen 列表是"硬冻结",user 拍板后需要 5 锚 JSON 派生补丁"

### 6.3 严守

- `_verify_15frozen.py` 修改不影响其他 15 frozen 文件的 0 触动
- 注释必须清晰、可被 Mavis 复审

---

## §7 修复点 7:沿 P-F V0.1 §5 预注册纪律

### 7.1 含义

P-F V0.1 §5 判定线预注册 = 计算前锁定判定线, SELF-CHECK 断言块(任一失败不落盘)。

boss_pc_* 升级为实跑后, 必须沿此纪律:
- 预注册判定线(在 patch 脚本顶部)
- SELF-CHECK 断言块(脚本尾部)
- 二跑(首跑全抓缺陷, 二跑 ALL PASS)

### 7.2 期望修复

Trae 沿 P-F V0.1 §5 纪律修改 boss_pc_1/2/3 + boss_pe_1/2/3 + boss_pg_1/2/3 的 patch 脚本:
- 添加预注册判定线
- 添加 SELF-CHECK 断言块
- 二跑验证(首跑可能抓到缺陷)

### 7.3 严守

- 不动 P-F V0.1 spec (`b10fae0da66d`)
- boss_* 修改后 verify 沿 P-F V0.1 §5 判定线

---

## §8 修复点 8:沿 7 铁律严守 0 触动

### 8.1 含义

Trae 修复全程必须严守 7 铁律:
1. 0 LLM 调用
2. 不设 proxy
3. 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan/WeChat API
4. key 永不入 prompt/JSON/落盘
5. 不动 5 锚 JSON 自身 (`03c6c01f3697`)
6. 不动 4 SPEC V0.1 + v19/v21 + corpus_v20 + 200+ 已落盘 + 现有 PDF/MD + 4 个 plugin spec
8. 不创建临时文件(verify 脚本例外)

### 8.2 期望修复

- Trae 修复 patch 脚本中, 不调用任何 LLM API
- 不读 key(如必须读, 用 `Path().read_text()` runtime)
- 修完 verify 18 frozen 全 0 触动

---

## §9 期望交付清单(沿 §4 委托信)

| 项 | 路径 | 状态 |
|---|---|---|
| 修复点 1-8 patch 脚本 | `deposon_team/plugins/fix_*.py` (或 `/tmp/fix_*.py` 不落盘)| 待 Trae 写 |
| 修复后综合报告 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md`(沿上次 Trae 修复报告风格) | 待 Trae 写 |
| 16 frozen + P-G V0 + P-G V0.1 SHA-12 验证 | 修前/修后两轮, 17/18 PASS + 1 legal modification | 待 Trae verify |
| 7 铁律严守声明 | 综合报告 §8 | 待 Trae 写 |

---

## §10 Trae 修复后回信模板

修完后, Trae 须回信以下信息给 Mavis:

```
修 8 个修复点回信 (Trae 2026-09-16 / ...)

- 修复点 1 (命名一致性): option_A / option_B / option_C
  - 决策依据: <一行>
  - patch 路径: deposon_team/plugins/boss_pc_*.py (新名)
  - 内容修改: <一行>
- 修复点 2 (race condition): <一行>
- 修复点 3 (5 锚 JSON 派生): option_A / option_B / option_C
  - 决策依据: <一行>
- 修复点 4 (BOSS SCAFFOLDING): option_A / option_B / option_C
- 修复点 5 (命名 vs 内容): <一行>
- 修复点 6 (frozen 列表动态冻结): <一行>
- 修复点 7 (P-F V0.1 §5 预注册): <一行>
- 修复点 8 (7 铁律严守): ✓ PASS

- 18 frozen SHA-12 验证: 17/18 PASS + 1 legal modification (skill_d 沿 user 拍板 1A)
- 7 铁律严守: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓
- 综合报告: docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md
```

---

## §11 老实老实老实(不擅自决定)

- ❌ 不擅自落盘 boss_pc_*.py 真实脚本(沿 R3 erratum, 等 Trae 修复)
- ❌ 不擅自决定 5 锚 JSON 派生 vs 合并(等 Trae 选择)
- ❌ 不擅自升级 boss_pg_* 为实跑(等 Trae 选择)
- ❌ 不擅自动 18 frozen 文件(除 skill_d 合法改动)
- ❌ 不擅自修改 4 SPEC V0.1 + v19/v21 + corpus_v20
- ❌ 不擅自修改 P-F V0.1 + P-G V0 + P-G V0.1 spec

---

## §12 总结

- **Trae 审核 + 修复代码**: 8 个修复点(命名一致 / race condition / 5 锚 JSON 派生 / 4 BOSS SCAFFOLDING / 命名 vs 内容 / frozen 列表 / P-F V0.1 §5 预注册 / 7 铁律严守)
- **严守 7 铁律 + 18 frozen 0 触动**(除 skill_d 合法改动)
- **回信模板**: 见 §10
- **Mavis 复审纪律**: Trae 修复后, Mavis 派 reviewer-a 静态审 + reviewer-b /tmp 重跑双审
- **D5 (09-16) 收尾**: 等 D_fix2 worker (bg_44d89fa8) 完成 + verify
- **D7 (09-18) 收束**: 5 锚终极 PASS/FAIL + 1 周判死报告 1 页 + 王老师 WeChat 推送

---

**委托信结束** | 严守 7 铁律 0 触动 18 frozen | 0 LLM 0 网关 0 临时文件 | 沿 user 13:39 "适时安排暂停进度并写信让trea审核与修复代码"