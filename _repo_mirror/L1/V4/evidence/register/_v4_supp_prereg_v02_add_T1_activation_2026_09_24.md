# V4 T1 追加件生效留痕（draft，2026-09-24，待 PI 复核生效）

- **追加件**：`results/_v4_supp_prereg_v02_add_T1_2026_09_24.md`（T1 · L2/L14 温度敏感性 + mimo/teamo 端点补测 稳健性探针），SHA-12 见落盘报值（**48,738 B / 末态文件 hash**）——**待 PI 复核生效，生效即锁，一字不改**
- **PI 拍板**：待 `ask_T1_*` 问卷（PI 2026-09-24 派工单「T1 辅助检验预登记」待复核生效）
- **生效时刻**：待 PI 复核生效时填入（沿 `AD42992DC75D` 锁先例「生效时刻」字段填法）
- **T1 探针定位硬约束**（沿 T1 §0 + §1.3 + §4 边界声明）：
  - **T1 = 稳健性辅助检验（sensitivity probe）**，**不翻 L2/L14 正式判定**
  - 结论仅作**稳健性注记**入勘误链
  - 除 K-T1-S1 / K-T1-S2 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**，**不得据此改判** L2/L14 既定结论一字不动
  - L2 verdict `E433A06E7BFB` §11「FAIL（K-N11-3 真证伪）」+ L14 verdict `764F24A21AC8` §11「FAIL（K-N11-3 真证伪 qwen 固有方差）」既定结论一字不动

---

## T1 探针字面（沿 T1 §1.5，0 新设数值阈值）

### 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1 探针放宽至 N_min=10** 不动此字面）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

### T1 新增 kill-line（0 新设数值阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定端点（mimo 或 teamo）下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点, 维度, 温度) cell 教师 J 中位 ≥ 0.85
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 字面，**0 新设**）
  - **不翻 L2/L14 正式判定**（沿定位声明）：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 既定结论一字不动
- **K-T1-S2（端点敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定温度（0.0 / 0.3 / 0.5）下，沿 L2 维度或 L14 维度，教师 J 中位数跨端点 {mimo, teamo} 中**任一端点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (温度, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**：同 K-T1-S1，仅 (端点) 维度替换 (温度) 维度
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1
- **K-T1-S3（稳健性确认线 · 副判定）**：
  - **字面**：12 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1 探针不命中 K-T1-S1 / K-T1-S2 → 仅入稳健性确认注记，**不入勘误链**（K-N11-3 真证伪方向在 temp / 端点维度稳定）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2 = 探针命中；全 12 cells 不触发 = 探针不命中

### T1 探针阈值一览

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| K_N11_1_DIFF | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| K_N11_2_DELTA | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| K_N11_3_THRESHOLD | 0.85 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| TH-17 N_TARGET | 20 / 教师 | `_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-T1-1 N_min** | **10 对/教师**（T1 探针放宽） | 本棒 T1 §1.4 新立 | （本棒） | §1.4 非退化自证 + §1.8 新增条款 |

> **0 新设数值阈值声明**：K-T1-S1/S2/S3 三条**0 新设数值阈值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 字面一字不动；T1 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**

---

## 锁定范围

> 沿 R5 frozen 只追加 + 锁后不改字面 + 派生 JSON 不合并

- **§0 输入件 SHA-12 链 16 件**（既有 3 件预登记 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 22 caption `6A2656878745`）
- **§1 T1 矩阵 12 cells**（{L2, L14} × {temp 0.0/0.3/0.5} × {mimo, teamo}）+ K-N11-1/2/3/N1/N2 字面不动 + K-T1-S1/S2/S3 新增（0 新设数值阈值）+ TH-T1-1 = 10 对/教师（T1 探针放宽）
- **§0.5 过渡声明 1 件**：T1 稳健性探针定位过渡（L2/L14 既定 K-N11-3 真证伪不动 + T1 探针 12 cells 跑出前不预设 PASS/FAIL 翻转）
- **§5 根因三分类 + T1 探针与 L2/L14 既判的根因关联**（沿拍板 #15 口径）
- **既有 K-N11-1/2/3/N1/N2 字面锁前痕迹保留**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）
- **T1 探针定位硬约束**：稳健性辅助检验，**不翻 L2/L14 正式判定**；除 K-T1-S1/S2 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判 L2/L14 既定结论一字不动**

---

## 过渡声明 1 件随生效继续有效

- **T1 稳健性探针定位过渡**：自 T1 件立线起标「**已知 L2 N-11 supp（qwen t=0.7, N=2）教师 J 中位 0.41-0.52 + L14 N-11 full（qwen t=0.7, N=20）教师 J 中位 0.36-0.39 均 < 0.85 = K-N11-3 真证伪既判；T1 矩阵 12 cells 跑出前不预设 PASS / FAIL 翻转**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（构造不可行 — 一等结论，归假证伪族）」（前棒 N=2 致 K-N11-N1 FAIL，但 K-N11-3 字面真证伪方向一致）
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 在 {temp 0.0 / 0.3 / 0.5} × {mimo / teamo} 矩阵下探「教师 J 中位是否仍 < 0.85」—— 若任一 cell 翻 ≥0.85，**仅记「稳健性存疑」注记**（qwen 固有方差 vs 教师端点固有 vs 温度敏感性三源），**不据此翻 K-N11-3 真证伪既定判**（qwen 端点 + temp=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）
  - 全 12 cells 仍 J < 0.85（无翻转） = 「**判定稳健**」 = 不入勘误链（仅作稳健性确认注记）
- **本件不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件**

---

## 起跑条件（T1 接力 worker · L2/L14 温度敏感性 + mimo/teamo 端点补测）

> 沿 T1 §1.4 启动条件 + §1.6 调用预算与节制

### 12 cells 矩阵执行（worker 接力棒）

- **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面）：
  - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell
  - 6 cells（L2 × {temp 0.0/0.3/0.5} × {mimo/teamo}）= ≤ 156 calls / L2 维度
- **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面）：
  - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell
  - 6 cells（L14 × {temp 0.0/0.3/0.5} × {mimo/teamo}）= ≤ 156 calls / L14 维度
- **总 cells = 12 cells × ≤ 26 calls/cell = ≤ 312 calls**（理论 ≤ 720 calls 硬上限，按需减少）

### 小→大序列（worker 第 1 棒接力，先行 sanity check）

1. **单 cell sanity check**：L2 维度 × temp=0.3 × mimo = 1 cell × ≤ 26 calls（**先行探活 + 端点 / 温度切换可行性验证**）
2. **维度扩展**：L2 维度 × {temp 0.0/0.3/0.5} × mimo = 3 cells × ≤ 26 calls（**L2 维度温度敏感性**）
3. **维度扩展**：L2 维度 × {temp 0.0/0.3/0.5} × teamo = 3 cells × ≤ 26 calls（**L2 维度端点敏感性**）
4. **维度扩展**：L14 维度 × {temp 0.0/0.3/0.5} × mimo = 3 cells × ≤ 26 calls（**L14 维度温度敏感性**）
5. **全集**：L14 维度 × {temp 0.0/0.3/0.5} × teamo = 3 cells × ≤ 26 calls（**全集**）

### 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「sub-batch strategy」双向沿用）
- **每 cell 拆批**：每 cell ≤ 26 calls / 单批（≤ 30 calls 看门狗内）
- **12 cells × 单批 = 12 批**（理论；按需拆 24 批按 L14 §9.1 280s hard limit 模式）

### 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict §2 + L14 verdict §2 + Track 2 runner `INTER_CALL_SLEEP_S`）
- **mimo 端点**：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False`）
- **teamo 端点**：**必走 tun 防封号**（PI 2026-09-23 硬纪律）
  - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
  - `all_proxy=socks5://127.0.0.1:1018`

### 总预算上限

- **总 calls 上限 ≤ 720 calls**（12 cells × 60 calls/cell 硬上限）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束）
- **实际预计 ≤ 312 calls**（沿 §1.4 + §1.6 字面）

### 中断-恢复与分批拆跑

- **同 worker 接力棒**：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1 先例）
- **checkpoint 文件**：`.tmp/_t1_records.json`（沿 L14 runner `.tmp/_l14_records.json` 惯例）
- **元组 skip**：(teacher, caption_id, reask_idx, temp, endpoint) 已跑 skip
- **撞限应急**：已启动 cells 部分完成记「T1 部分完成」注记；未启动 cells 留待 worker 下一棒接力

---

## 产物链

> 派生 JSON 不合并（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_t1_*` prefix 分列

- `_v4_supp_t1_executor.py`（T1 矩阵 runner + checkpoint 模式 + 端点 / 温度切换）
- `_v4_supp_t1_result.json`（12 cells 矩阵结果聚合：每 cell per teacher J 中位 + 端点 + 温度 + schema `v4_t1_sensitivity/1` + 跨端点 / 跨温度 J 中位标准差）
- `_v4_supp_t1_verdict.md`（T1 探针判定：12 cells 字面 K-N11-3 实测 + K-T1-S1/S2/S3 触发判定 + 根因三分类每行附 + **不翻 L2/L14 既判声明**）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）

---

## 边界

> 沿 V1–V3 资产只读不动 + R4 key 永不明文 + R5 V4 frozen 只追加 + R6 P-G 不动 + R7 plugin spec 不动

- **V1–V3 资产只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **R4 key 永不明文**（**无例外**）
- **R5 V4 frozen 只追加**：v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` + 22 caption `6A2656878745` **16 件一字不改**
- **R6 P-G v0/v01 不动**
- **R7 plugin spec 不动**
- **生效即锁不重开不调**
- **T1 追加件正文「待 PI 复核生效」字样保留不删**（沿「锁后不改字面」+ 留锁前痕迹纪律；本 activation 件由 draft 转生效时，PI 复核通过状态以本 activation 件为准）
- **派生 JSON 不合并**
- **论文 §4 去向未拍板**（沿拍板 #9 缓定；本棒产物不进 §4，K-N11-N2 字面 + T1 探针稳健性注记沿 L2/L14 既定路径）
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（沿 v0.2 + L9 + L10 同惯例；sk- / AIza / Bearer 三模式自扫 0 hit）
- **T1 探针定位硬约束再声明**：**稳健性辅助检验（sensitivity probe）**，**不翻 L2/L14 正式判定**；除 K-T1-S1 / K-T1-S2 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判 L2/L14 既定结论一字不动**
- **0 新设数值阈值声明**：K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 均为布尔条件显式化；TH-T1-1 = 10 对/教师为 T1 探针放宽口径（与 L2/L14 既定 N=20/教师两层并存）
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）