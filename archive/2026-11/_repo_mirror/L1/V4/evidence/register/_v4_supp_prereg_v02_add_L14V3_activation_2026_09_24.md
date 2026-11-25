# V4 L14+ 追加件生效留痕（draft，2026-09-24，待 PI 复核生效）

- **追加件**：`results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（L14+ · N-26 V3 distill 整链重跑 真审唯一路径），SHA-12 见落盘报值（**61,547 B / 末态文件 hash**）——**待 PI 复核生效，生效即锁，一字不改**
- **PI 拍板**：待 `ask_L14V3_*` 问卷（PI 2026-09-24 派工单「L14+ V3 整链重跑预登记——N-26 真审唯一路径」待复核生效）
- **生效时刻**：待 PI 复核生效时填入（沿 `AD42992DC75D` 锁先例「生效时刻」字段填法）
- **L14+ 真审唯一路径定位硬约束**（沿 L14+ §0 + §1.3 + §4 边界声明）：
  - **L14+ = N-26 真审唯一路径**（V3 distill 整链重跑复现 + 采集阶段同步保四元组 (prompt_id / prompt_text / response_text / per-call metadata)）
  - **改判 N-26 既定结论须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字**
  - L4 verdict `74B5B37F7EEA` §11「FAIL（构造不可行，问题收窄，4/5 教师 metadata 缺位）」既定结论一字不动
  - 本棒执行后判死 = N-26 真审重判，**不预设立场**

---

## L14+ 字面（沿 L14+ §1.5，0 新设数值阈值）

### 既有 K-N26 字面（沿 N-26 主预登记 `0A9EE16267B5` §2 一字不动，锁前痕迹保留）

- **K-N26-1**：教师准确率 ≥ K_N26_1_ACC = 0.70 即 `hit=True` → N-26 真证伪（教师准确率命中既判阈值）—— **沿 `0A9EE16267B5` §2 K-N26-1 字面**（**L14+ 主度量核心沿此字面**）
- **K-N26-2**：教师侧 vs distill 侧二分类 AUC < K_N26_2_AUC = 0.75 即 `hit=True` → N-26 真证伪（二者不可分）—— **沿 `0A9EE16267B5` §2 K-N26-2 字面**
- **K-N26-3**：≥ 4 教师准确率 < K_N26_3_TEACHERS_LT = 0.60 即 `hit=True` → N-26 真证伪（多数教师准确率未达既判阈值）—— **沿 `0A9EE16267B5` §2 K-N26-3 字面**
- **K-N26-N1**：每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化即 `pass=True` → 构造非退化自证成立；否则 `pass=False` → 命题不明 —— **沿 `0A9EE16267B5` §2 K-N26-N1 字面**（**L14+ 构造面判定沿此字面**）
- **K-N26-N2**：teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师即 `pass=True` → tun 合规成立；否则 `pass=False` → 构造失灵 —— **沿 `0A9EE16267B5` §2 K-N26-N2 字面**（**L14+ 工具层判定沿此字面**）

### L14+ kill-line 字面总览（沿 N-26 主预登记 `0A9EE16267B5` §2 字面）

| K-* | 字面 | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N26-1 | 教师准确率 ≥ 0.70 → 真证伪 | 教师准确率 ≥ 0.70 | N-26 真证伪（教师准确率命中既判阈值） | `0A9EE16267B5` §2 |
| K-N26-2 | 教师侧 vs distill 侧二分类 AUC < 0.75 → 真证伪 | AUC < 0.75 | N-26 真证伪（二者不可分） | `0A9EE16267B5` §2 |
| K-N26-3 | ≥ 4 教师准确率 < 0.60 → 真证伪 | ≥ 4 教师准确率 < 0.60 | N-26 真证伪（多数教师准确率未达既判阈值） | `0A9EE16267B5` §2 |
| K-N26-N1 | 每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 → 构造非退化自证 | N_min 不足或 J 中位分布退化 | 命题不明 / 构造失灵 | `0A9EE16267B5` §2 |
| K-N26-N2 | teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → tun 合规 | teamo 端点未走 tun 或空响应率 > 50% | 构造失灵 / tun 不合规 | `0A9EE16267B5` §2 |

### L14+ 探针阈值一览

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| K_N26_1_ACC | 0.70 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-1 字面 |
| K_N26_2_AUC | 0.75 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-2 字面 |
| K_N26_3_TEACHERS_LT | 0.60 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-3 字面 |
| K_N26_1_ACC | 0.70 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| K_N26_2_AUC | 0.75 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| K_N26_3_TEACHERS_LT | 0.60 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| K-N26-N1 非退化自证 | N_min ≥ 既判 N_target + J 中位分布非退化 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N1 字面 |
| K-N26-N2 tun 合规 | teamo 端点 100% 走 tun + 空响应率 ≤ 50% | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |
| **TH-L14+-1 单批上限** | **≤275s** | `results/_v4_supp_l7_e_n20_verdict.md` | `B8335982AE5E` | §11 实证字面 |
| **TH-L14+-2 600s watchdog** | **≤600s** | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 字面（沿 add_T1） |
| **TH-L14+-3 N_min** | **≥ 既判 N_target / 教师** | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N1 字面 |
| **TH-L14+-4 tun 合规率** | **100%** | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |
| **TH-L14+-5 空响应率上限** | **≤ 50% per 教师** | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |

> **0 新设数值阈值声明**：K-N26-1/2/3/N1/N2 五条**0 新设数值阈值**；K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 沿 `0A9EE16267B5` §2 + `74B5B37F7EEA` §2 字面一字不动；TH-L14+-1~5 均为字面引用 L7 实证 `B8335982AE5E` ≤275s + K-N26-N1/N2 字面，**非本棒新设数值**；L14+ 探针字面「hit=True 即触发真证伪 / pass=False 即构造失灵」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**

---

## 锁定范围

> 沿 R5 frozen 只追加 + 锁后不改字面 + 派生 JSON 不合并

- **§0 输入件 SHA-12 链 19 件**（N-26 主预登记 `0A9EE16267B5` + L4 verdict `74B5B37F7EEA` + L4 result `065DD4393AB8` + L13 verdict `E105EC1362DB` + L13 executor `FF6A280BE11A` + L7 verdict `B8335982AE5E` + L7 runner `D5640CA314E2` + v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + add_T1 件 + add_T1 activation + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 22 caption `6A2656878745` + V3 distill 流水线参照系 `scripts/run_v3x_*.py`）
- **§1 L14+ 10 cells 矩阵**（5 教师 × 22 caption × 双向（teacher + distill））+ K-N26-1/2/3/N1/N2 字面不动 + TH-L14+-1~5 字面引用（非本棒新设）+ 工具失灵修正条款（max_tokens 2000 + teamo reasoning-only 空响应重试口径）
- **§0.5 过渡声明 1 件**：L14+ N-26 真审唯一路径定位过渡（N-26 v1/v2 既定 FAIL · 构造不可行 · 缺教师侧配对不动 + L14+ 执行前不预设立场）
- **§5 根因三分类 + L14+ 探针与 N-26 既判的根因关联**（沿拍板 #15 口径 + 根因三分类每行附）
- **既有 K-N26-1/2/3/N1/N2 字面锁前痕迹保留**（沿 `0A9EE16267B5` §2 + `74B5B37F7EEA` §2 + `E105EC1362DB` §11 + `B8335982AE5E` §11 + V3 distill 流水线字面一字不动）
- **L14+ 定位硬约束**：N-26 真审唯一路径（V3 distill 整链重跑复现 + 采集阶段同步保四元组），**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字**

---

## 过渡声明 1 件随生效继续有效

- **L14+ N-26 真审唯一路径定位过渡**：自 L14+ 件立线起标「**已知 N-26 v1 FAIL · 构造不可行 · 4/5 教师 metadata 缺位（kimi/GLM_1/GLM_2/coze 全 False×3 metadata；仅 minimax 有 latency / token_usage / reasoning_tokens 全 True）+ L4 v2 metadata 1/5 → 5/5 全补齐（kimi/GLM_1/GLM_2/coze 由 V3 缺位补全）+ 但缺教师侧配对（V3 调用侧未保留）= 后续重采大工程 + L13 V4 三元组基底立定 + L7 实证 background session ≤275s 可行**——
  - L4 verdict `74B5B37F7EEA` §11 总判定 = 「FAIL（构造不可行，问题收窄）」（v2 metadata 5/5 + 缺教师侧配对 = V3 调用侧未保留）
  - L13 verdict `E105EC1362DB` §11 总判定 = （V4 三元组基底立定，N-26 重审参照系就位）
  - L7 verdict `B8335982AE5E` §11 总判定 = （E-N20 实证 background session ≤275s / 600s watchdog 内可行）
  - N-26 主预登记 `0A9EE16267B5` §2 字面 K-N26-1/2/3/N1/N2 一字不动 = 准确率 ≥0.70 / AUC <0.75 / ≥4 教师准确率 <0.60 / K-N26-N1 非退化自证 / K-N26-N2 tun 合规
  - 本棒 = **唯一真审路径**（V3 distill 整链重跑复现 + 采集阶段同步保四元组）—— 历史 V3 调用侧 metadata 断点不可回溯，唯一补法 = 整链重跑
  - L14+ 在 V3 distill 流水线复现下探「K-N26-1/2/3/N1/N2 是否仍按既判方向触发」—— **不预设 PASS / FAIL 翻转**（沿 PI 2026-09-23「诚实的根因是不误导」+ 沿 add_T1 §0.5 同口径）
  - 真证伪触发（任一 K-N26-* hit=True 重新落定真证伪方向）= **N-26 重审真证伪**（与 v1/v2 方向可能一致或新方向）
  - 假证伪族 / 命题不明触发 = **N-26 重审构造不可行 / 命题不明**（与 v1/v2 方向可能一致或新定性）
- **本件不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 既有 3 件** + **不动 L10 §0.5 既有 2 件** + **不动 add_T1 §0.5 T1 稳健性探针定位过渡 1 件**

---

## 起跑条件（L14+ 接力 worker · V3 distill 整链重跑复现 + 采集阶段同步保四元组）

> 沿 L14+ §1.4 启动条件 + §1.6 调用预算与节制 + 工具失灵修正条款

### 10 cells 矩阵执行（worker 接力棒）

- **5 教师 × 22 caption × ≥5 calls × 双向（teacher + distill）= ≥1,100 calls**（理论下限；按需扩展至 ≥5 calls/教师/侧）
- **每 cell = 5 calls 拆批 ≤275s**：
  - 拆批策略：每 caption 拆 1 批（5 calls/批 × 2.5s 串行 ≈ 12.5s + 处理开销 ≈ 110s/批，含 60% 安全冗余 ≤275s 内完成）
  - 22 caption × 1 批 = 22 批 / 教师 / 侧
- **10 cells × 22 批 = 220 批**（理论上限；按需扩展）

### 小→大序列（worker 第 1 棒接力，先行 sanity check）

1. **单 cell sanity check**：教师侧 kimi × 22 caption × ≥5 calls = ≥110 calls（**先行探活 + 端点切换可行性验证 + 四元组保真采集可行性验证**）
2. **教师侧全 5 教师**：kimi / GLM_1 / GLM_2 / coze / minimax × 22 caption × ≥5 calls = 5 cells × ≥110 calls = ≥550 calls（**教师侧全跑**）
3. **distill 侧全 5 教师**：kimi / GLM_1 / GLM_2 / coze / minimax × 22 caption × ≥5 calls = 5 cells × ≥110 calls = ≥550 calls（**distill 侧全跑**）
4. **全集**：10 cells × ≥110 calls = ≥1,100 calls（**全集**）

### 单批 calls 上限（看门狗约束）

- **单批 ≤ 22 calls**（沿 L7 实证 `B8335982AE5E` ≤275s 上限：22 calls × 2.5s 串行 + 处理开销 ≈ 110s，含 60% 安全冗余 ≤275s 内完成）
- **每 caption 拆批**：每 caption ≤ 5 calls / 单批 ≤ 22 calls（含教师侧 + distill 侧 + 重试预留）
- **22 caption × 单批 = 22 批 / 教师 / 侧**（理论上限）
- **10 cells × 22 批 = 220 批**（理论上限；按需调整）

### 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 add_T1 §1.6.2 INTER_CALL_SLEEP_S + L2 verdict `E433A06E7BFB` §2 INTER_CALL_SLEEP_S + L14 verdict `764F24A21AC8` §2 INTER_CALL_SLEEP_S + Track 2 runner INTER_CALL_SLEEP_S 沿用）
- **qwen_plan 端点**：**无代理**（沿 L7 实证）
- **mimo 端点**（token-plan-cn.xiaomimimo.com/v1）：**无代理**（沿 add_T1 §1.6.2 + L7 实证）
- **teamo 端点**（api.teamorouter.cn/v1）：**必走 tun 防封号**（PI 2026-09-23 硬纪律）：
  - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
  - `all_proxy=socks5://127.0.0.1:1018`
  - 直连 = 封号风险（沿 user memory 「teamorouter/openrouter 必走 tun 代理防封号」2026-09-23）

### 工具失灵修正条款（沿「工具/构造失灵族可补构造」先例，明确非擅调阈值）

- **max_tokens 上调规避 L4 触顶**（沿 L4 verdict `74B5B37F7EEA` §2 字面 + §11 构造失灵族补构造先例）：
  - max_tokens 从默认上调至 **2000**（规避 L4 触顶；非擅调阈值，仅补构造层 token 上限）
  - 仅适用于 V3 distill 整链重跑复现阶段（不改 V3 资产）
- **teamo reasoning-only 空响应重试口径**（沿 V3 distill 流水线实测）：
  - **空响应定义** = response_text 为空字符串 / 仅含空白字符
  - **空响应计数如实入 result.json 空响应计数字段**（不 silently 丢弃）
  - **空响应触发重试**：单 call 触发 teamo reasoning-only 模式空响应 → 内层重试 1 次（最多 3 次内层重试预留）
  - **重试仍空响应** = 计入 result.json 空响应计数字段 + **不入主度量**
  - **空响应率 > 50% per 教师** = K-N26-N2 tun 合规触发 pass=False（构造失灵族）
- **本棒 0 触既有阈值**（K-N26-1/2/3/N1/N2 字面一字不动）

### 总预算上限

- **总 calls 下限 ≥ 1,100 calls**（5 教师 × 22 caption × ≥5 calls × 双向 = ≥1,100 calls；按需扩展）
- **总 calls 上限 ≤ 5,500 calls**（5 教师 × 22 caption × 25 calls × 双向 = 5,500 calls 硬上限；含重试预留）
- **总 wall time ≤ 30h**（10 cells × 单批 ≤275s × 22 批/cell + 5h × 6 批 Token Plan 配额 ≤ 30h；含中断-恢复时间）
- **实际预计 ≥1,100 calls**（理论下限）

### 中断-恢复与分批拆跑方案

- **同 worker 接力棒**（沿 L14 verdict §9.1 先例）：
  - v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2
  - **同 agent 唤醒（task_append）**：worker session 不重启，沿 task_append 续跑（沿 L14 verdict §9.1 同棒续跑 + L7 实证 ≤275s 同 session 续跑）
  - checkpoint 文件：`.tmp/_l14v3_records.json`（沿 L14 runner `.tmp/_l14_records.json` + add_T1 `.tmp/_t1_records.json` 惯例）
  - 每 call 后 checkpoint 累积（沿 L14 runner L151-156 惯例）
  - 已跑 (teacher, caption_id, reask_idx, side, endpoint) 元组 skip（沿 L14 runner L107-110 + add_T1 §1.6.4 惯例）
- **分批拆跑**：
  - 撞 5h 配额自动恢复（worker 接力棒续跑）
  - 单批撞 275s 看门狗自动停（沿 L7 实证 ≤275s）
  - 中断-恢复同 agent 唤醒语义（task_append 续跑）
- **额度撞限应急**（如 10 cells 未跑完撞 5h 配额）：
  - 仅跑已启动 cells，不补未启动 cells
  - 已启动 cells 部分完成记「L14+ 部分完成」注记
  - 未启动 cells 留待 worker 下一棒接力

---

## 产物链

> 派生 JSON 不合并（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_l14v3_*` prefix 分列

- `_v4_supp_l14v3_executor.py`（L14+ V3 distill 整链重跑复现 runner + checkpoint 模式 + 端点切换 + 四元组保真采集 + 拆 5-6 教师批 ≤275s + tun 合规自检 + 空响应率自检）
- `_v4_supp_l14v3_result.json`（5 教师 × 22 caption × 双向 ≥1,100 calls 矩阵结果聚合：每 cell per teacher per side accuracy + AUC + 四元组 metadata + schema `v4_l14v3_n26/1` + tun 合规字段 + 空响应率字段 + 工具失灵修正条款执行日志）
- `_v4_supp_l14v3_verdict.md`（L14+ 探针判定：5 教师 K-N26-1/2/3/N1/N2 实测 + 触发判定 + 根因三分类每行附 + **N-26 真审重判声明** + **改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字声明**）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）
- **schema L14+ 专属**：result JSON 中 `schema` 字段 = `"v4_l14v3_n26/1"`（L14+ 专属 schema，与 L13 `v4_l13_n26pair` + L4 `v4_l4_n26re` + add_T1 `v4_t1_sensitivity/1` 同级独立）

---

## 四段闸门字面化（沿 8 agent 团队主轴：protocol-keeper 立线 → worker 拆批跑 → verdict-keeper 裁因 → evidence-auditor 审链）

> 沿 user memory 2026-09-23「代理换血: 3新代理替旧3」编制（verdict-keeper agent-3a4d09ba3c90 + evidence-auditor agent-11335500b168 + protocol-keeper agent-3e0c193da529 + doc-writer agent-0032834a3e04）

| 段 | agent | 职责 | 输出 | 触发条件 |
|---|---|---|---|---|
| 1 | **protocol-keeper**（立线） | L14+ 预登记立线 + K-N26 字面冻结 + 阈值来源表 + 工具失灵修正条款 | `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` + `_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md`（本双件） | PI 拍板预登记（已派工 2026-09-24） |
| 2 | **worker**（拆批跑） | V3 distill 整链重跑复现 + 采集阶段同步保四元组 + 拆 5-6 教师批 ≤275s + tun 合规 + 空响应率自检 | `_v4_supp_l14v3_executor.py` + `_v4_supp_l14v3_result.json` | 本 activation 件生效 + protocol-keeper 立线签字 |
| 3 | **verdict-keeper**（裁因） | L14+ K-N26-1/2/3/N1/N2 实测裁因 + 根因三分类每行附 + N-26 真审重判定性 | `_v4_supp_l14v3_verdict.md`（worker 跑完 result.json 后接力） | worker result.json 落盘 SHA-12 + 派生 JSON 不合并确认 |
| 4 | **evidence-auditor**（审链） | 证据链审计 + 四元组保真核验 + tun 合规审 + 跨件 SHA 漂移审 + E-30 编号裁定（如有） | `_v4_l14v3_evidence_audit_2026_09_24.md`（新增件） | verdict-keeper 签字后接力 |

> **闸门硬约束**：每段签字 = 落盘 SHA-12 自核 + 派生 JSON 不合并确认；任一段未签字 = 下一段不接力；L14+ N-26 重审判定须四段签字完整生效

---

## 边界

> 沿 V1–V3 资产只读不动 + R4 key 永不明文 + R5 V4 frozen 只追加 + R6 P-G 不动 + R7 plugin spec 不动

- **V1–V3 资产只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）—— **本棒 V3 distill 流水线复现 = 读取 `scripts/run_v3x_*.py` 参照系 + 新建 `scripts/_v4_l14v3_*.py` runner，0 触动原 V3 件**
- **R4 key 永不明文**（**无例外**）
- **R5 V4 frozen 只追加**：N-26 主预登记 `0A9EE16267B5` + L4 verdict `74B5B37F7EEA` + L4 result `065DD4393AB8` + L13 verdict `E105EC1362DB` + L13 executor `FF6A280BE11A` + L7 verdict `B8335982AE5E` + L7 runner `D5640CA314E2` + v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + add_T1 件 + add_T1 activation + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` + 22 caption `6A2656878745` **22 件一字不改**（含 V3 distill 流水线参照系只读不动）
- **R6 P-G v0/v01 不动**
- **R7 plugin spec 不动**
- **生效即锁不重开不调**
- **L14+ 追加件正文「待 PI 复核生效」字样保留不删**（沿「锁后不改字面」+ 留锁前痕迹纪律；本 activation 件由 draft 转生效时，PI 复核通过状态以本 activation 件为准）
- **派生 JSON 不合并**
- **论文 §4 去向未拍板**（沿拍板 #9 缓定；本棒产物不进 §4，K-N26-* 字面 + L14+ 真审重判沿 N-26 既定路径）
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（沿 v0.2 + add_T1 同惯例；sk- / AIza / Bearer 三模式自扫 0 hit）
- **L14+ 定位硬约束再声明**：**N-26 真审唯一路径（V3 distill 整链重跑复现 + 采集阶段同步保四元组）**，**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字**；L4 verdict `74B5B37F7EEA` §11 既定 FAIL · 构造不可行一字不动
- **0 新设数值阈值声明**：K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 沿字面不动；K-N26-N1/N2 均为字面引用 `0A9EE16267B5` §2 字面；TH-L14+-1~5 均为字面引用 L7 实证 + K-N26-N1/N2 字面，非本棒新设数值
- **0 触既有 K-N26-1/2/3/N1/N2 字面**（沿 `0A9EE16267B5` §2 + `74B5B37F7EEA` §2 + `E105EC1362DB` §11 + `B8335982AE5E` §11 一字不动）
- **四件盘上已清出披露**：N-26 主预登记 `0A9EE16267B5` + L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E` 四件 2026-09-24 maindir cleanup 后盘上已清出，但 inventory + ledger 锁定 SHA-12 + 字节 + 落地时间；本棒沿四件 SHA-12 字面引用为权威锚源（沿 add_T1 §9 漂移披露模式），**不擅自以盘 SHA 替代字面引用值**
- **派工单 SHA 漂移披露**：派工单写「L13 verdict 3f9c6a37f1e9」与 ledger 字面 SHA `E105EC1362DB` 不一致；本棒以 ledger 字面 SHA `E105EC1362DB` 为准（沿项目「字面引用锚定 SHA = 字面引用件自报值」惯例，ledger 是字面件 SHA-12 权威源）；派工单 SHA 错误留 PI 裁定，不擅自改派工单字面，仅披露漂移事实
