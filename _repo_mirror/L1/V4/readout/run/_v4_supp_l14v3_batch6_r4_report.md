# worker r4 回报 — L14V3 kimi 蒸馏侧 round 4（reask=3）

## Result
执行类任务完成。已落盘两份产物：
- `results/_v4_supp_l14v3_batch6_r4_executor.py`（SHA-12 `08f329b36e9d`，54,588 bytes）
- `results/_v4_supp_l14v3_batch6_r4_result.json`（SHA-12 `b7377ba019a1`，65,254 bytes）

distill 侧独立计数：本棒 22 caption × 1 call = 22 calls，全部 OK，0 empty，0 fail。distill 侧每个 caption 由 r3 后的 3/5 顺利补至 4/5。empty_rate = 0.0；累计 empty_rate（含 batch1+r2+r3+r4+r5+r1+r2+r3+r4）= 4.84%；K-N26-N2 未触发；tun_compliance = True；wall_time = 645.4s。

注：本棒 L_physics_concepts 触发 1 次 ssl_error 内层 retry 后成功（retry_count_distribution = {0: 21, 1: 1}）；属正常工具失灵族修正路径，retry 修复沿 r3。

## Changes made

### 写入
- `results/_v4_supp_l14v3_batch6_r4_executor.py`（新建；r3 基础上扩展 ROUND=4 / REASK_R1=3 / prompt_id `_r4` 后缀；沿 r3 distill 侧独立计数口径）
- `results/_v4_supp_l14v3_batch6_r4_result.json`（新建；22 quadruples + predecessor 链 + counting_scope_correction 块沿 r3）

### 未触动（核验）
- `results/_v4_supp_l14v3_batch6_r3_result.json`：SHA-12 仍为 `15a7fecdffe7`（与派工单字面 SHA-12 一致；未触动）✓
- `results/_v4_supp_l14v3_batch6_r3_executor.py`：未触动
- `results/_v4_supp_l14v3_batch6_r2_result.json`：SHA-12 仍为 `96e1de46ed30`（未触动）✓
- `results/_v4_supp_l14v3_batch6_r1_result.json`：SHA-12 仍为 `0d29e1ab4ae2`（未触动）✓
- 前棒所有 batch1_r{2,3,4,5} result/executor：未触动
- `corpus/v20_caption_surface/strip_captions_22.json`（`6a2656878745`）：未触动
- `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（`05B975A86989`）：未触动

## Validation run & results

### 实际执行（沿 r3 端点/口径）
- 端点：`https://api.teamorouter.cn/v1` + tun 代理（`http://127.0.0.1:1018`）+ `kimi-k3`
- 超参：temperature=0.7，max_tokens=2000，read_timeout_initial_s=60，read_timeout_retry_s=90，inner_retry_max=3
- 串行间隔 ≥2.5s 全程
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 r3）
- 22 calls 全 OK；其中 L_physics_concepts 触发 1 次 ssl_error retry（自动恢复）

### 计数口径沿 r3（保守口径，标注待 PI 复核）
- distill 侧独立计数；filter 域 = prompt_id 前缀 `kimi_t01_distill_`
- r1 混合数据不视为废数据；r1 result 文件完整保留
- `counting_scope_correction` 块内 `pending_pi_review` 字段如实注明

### 产物自扫（key pattern hits）
- `self_scan.key_pattern_hits_in_product`：空列表
- R4 key 永不明文：无例外 ✓

### 落盘核验
- r4_executor SHA-12 = `08f329b36e9d`
- r4_result SHA-12 = `b7377ba019a1`（与 executor 落盘 report 一致 ✓）
- r3_result SHA-12 = `15a7fecdffe7`（落盘前/后一致；r3 文件未触动 ✓）
- r2_result SHA-12 = `96e1de46ed30`（落盘前/后一致；r2 文件未触动 ✓）
- r1_result SHA-12 = `0d29e1ab4ae2`（落盘前/后一致；r1 文件未触动 ✓）
- r4 result LF-only = True（已 normalize CRLF → LF）

### distill 侧 per_caption（r4 后）
| caption_id | distill_succ_count | total_calls | met_target (≥5) |
| --- | --- | --- | --- |
| 22 caption | 各 4/5 | 各 4 | 0/22 met（待 r5 接力） |

### empty_rate 累计（沿 dispatch §4）
- r3 后 cumulative = 164 total, 9 empty, **rate=5.49%**
- r4 后 cumulative = 186 total, 9 empty, **rate=4.84%**
- K-N26-N2 threshold = 0.50 → 未触发 ✓

### predecessor 链核验（result 内）
- r3_executor: `1385d2ca356f` ✓
- r3_result: `15a7fecdffe7` ✓
- r2_executor: `93c931fc3b1c` ✓
- r2_result: `96e1de46ed30` ✓

## Assumptions
1. **沿 r3 计数口径**：filter 域 = prompt_id 前缀 `kimi_t01_distill_`；r1 混合域仅作透明参照；不视为废数据
2. **本棒补 1 call/caption**：按派工单字面「22 caption × 1 call, distill 侧独立目标各补至 4/5 successful」执行；后续 r5 接力（22 calls）可推 distill 侧至 5/5 successful 收官
3. **predecessor 链**：r4_executor predecessor_sha12 包含 r3_executor `1385d2ca356f` + r3_result `15a7fecdffe7`（与派工单字面 SHA-12 核验一致）+ r1/r2/r5/r4/r3 等前棒全链
4. **prompt 构造 = 复现口径**：沿 r3 字面 `kimi_t01_distill_<caption_id>_r4` prompt_id 后缀 + Caption ID + Caption text + 3-5 NEW related concept labels 任务（per prereg §1.6.4 字面 + L13 verdict E105EC1362DB distill style 复现口径）
5. **夜间授权**：PI 2026-09-25 00:46「今晚保守口径下先斩后奏」；保守口径 = distill 侧独立计数 + counting_scope_correction 标注待复核；未越权（未触 V1-V3 / 未动 frozen / 未动 P-G / 未动 plugin spec）
6. **不预探**：沿前棒实测端点 + tun；本棒未重新探活
7. **ssl_error retry 触发的 1 次内层重试**：L_physics_concepts 触发 1 次 ssl_error，自动恢复成功；属工具失灵族修正路径，retry 修复沿 r3；retry_trigger_categories_distribution = {'ssl_error': 1}

## Blockers / remaining risks
- **本棒仅完成 distill 侧 4/5 successful/caption**：22 caption 全未达 ≥5 successful；后续 1 棒接力（r5 22 calls → 收官）
- **counting_scope_correction 待 PI 复核**：PI 若倾向保留 r1 混合域统计，须重审 r2/r3/r4 棒；r5 棒前须 PI 确认口径
- **夜间授权范围有限**：保守口径仅限本棒；若 PI 后续要求回退至 r1 混合域，本棒数据 + r5 棒须相应调整
- **K-N26-N2 累计监控**：本棒未触发；后续 r5 累计监控继续
- **未触动文件核验通过**（r3_result = `15a7fecdffe7` 不变 ✓；r2_result = `96e1de46ed30` 不变 ✓；r1_result = `0d29e1ab4ae2` 不变 ✓）；r5 棒接力前须再次确认 r1/r2/r3/r4 文件 SHA-12 不变

## Iron rules 严守核验（沿 7+9 全套）
- R1 no_llm：False（V4 放开） ✓
- R2 no_proxy：False（V4 放开） ✓
- R3 no_gateway：False（V4 放开） ✓
- R4 key 永不明文：True（self_scan key_pattern_hits_in_product = 空） ✓
- R5 V4 frozen append-only：True（本棒 r4_executor/r4_result 新件；前棒 r1/r2/r3/frozen 未触动） ✓
- R6 P-G v0/v01 untouched：True（未触动） ✓
- R7 plugin spec untouched：True（未触动） ✓
- v1-v3 readonly：True（未触动） ✓
- tun_compliance_teamo_endpoint：True（22/22 calls 走 tun） ✓
- serial_interval_ge_2_5_s：True（全程 2.5s） ✓
- empty_response_counted_not_dropped：True（如实计数 0/0） ✓
- kill_line_locked_K_N26_1_2_3_N1_N2：True（本棒 0 写 verdict） ✓
- no_threshold_adjustment：True（沿 r3） ✓
- no_existing_file_modified：True（r1/r2/r3 SHA-12 不变） ✓
- no_merge_of_derived_json：True（r4 result 与 r1/r2/r3 result 同级独立） ✓
- no_overwrite_prior_results：True（r1/r2/r3/前棒未触动） ✓
- retry_bug_fix_applied：True（22/22 calls，1 次内层 ssl_error retry 触发后自动恢复） ✓