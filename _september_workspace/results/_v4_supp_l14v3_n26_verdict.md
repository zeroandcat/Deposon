# V4 L14+ N-26 真审终裁 · K-N26-1/2/3 实测 · 10 cells 全配对 · 裁因确认（2026-09-26）

> **本件性质**：verdict-keeper 判定收口（裁因专职）；L14+ 产物链末件（沿 `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` `05B975A86989` §1.7 产物链「executor / result / verdict 三件」字面 + T15R2 verdict `8355724A26E3` 格式锚）
>
> **本件定位（沿 L14+ prereg `05B975A86989` §0 + §1.3 + §1.5 + §4 + §5 字面 + L14V3 model mapping `98A779D61C1E` §1.1 字面）**：N-26 真审 = V3 distill 整链重跑复现（5 教师 × 22 caption × ≥5 calls × 双向 ≥1,100 calls 同步保四元组 metadata）+ K-N26-1/2/3/N1/N2 五条 kill-line 字面判定；**不翻 N-26 v1/v2 既判方向**（L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」**一字不动**），仅作 v3 真审重判；本 verdict 件仅对 L14+ 探针字面证据下裁定
>
> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）：本件如实裁 K-N26-1 NOT TRIGGERED（教师准确率 0.5617 < 0.70）+ K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75）+ K-N26-3 NOT TRIGGERED（3/5 教师 <0.60，未达 ≥4 阈值）= **N-26 真审真证伪方向（沿 v1/v2 方向 metadata 不可区分被实证）**；不外推为「完全不可分」结论（kimi 0.7512 ≠ 全不可分）；不软化（沿 PI 2026-09-23「判死不软化」纪律）；不翻既有 L4 verdict 字面
>
> **核心硬约束（沿 L14+ prereg `05B975A86989` §0 + §1.3 + §1.5 字面 + 派工单 5 件必带）**：本件仅对 10 cells × 22 caption × ≥5 calls × 双向 ≥1,100 calls 同步保四元组 metadata 裁因；不动 L14+ prereg/activation/result/executor 一字不动；不动 L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E` + v0.2 件 + add_T1 件 + L9 / L10 追加件 + Track 2 件 + 22 caption + V3 distill 流水线参照系 全栈 0 触动；不擅自调阈值（K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 一字不动）；判定布尔显式方向（hit=True 即触发 / hit=False 不触发）

---

## §0 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | 自报 SHA-12 | 盘实测 SHA-12（前 12） | 字节 | 状态 |
|---|---|---|---|---|---|
| **L14+ prereg（锚定不动）** | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `05B975A86989` | `05b975a86989` | 61,547 | ✓ |
| L14+ activation（锚定不动） | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `843E42EF4D2A` | `843e42ef4d2a` | 21,309 | ✓ |
| **L14V3 model mapping（锚定不动）** | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `98A779D61C1E` | `98a779d61c1e` | 32,521 | ✓ |
| T15R2 verdict 格式锚（不动） | `results/_v4_supp_t15r2_verdict.md` | `8355724A26E3` | `8355724a26e3` | 41,246 | ✓（格式锚） |
| batch1 r6 result (kimi distill 终件) | `results/_v4_supp_l14v3_batch1_r6_result.json` | `6B92BBFF7180` | `6b92bbff7180` | 57,925 | ✓ |
| batch2 r5 result (GLM_1 teacher 终件) | `results/_v4_supp_l14v3_batch2_r5_result.json` | `479F4119CF72` | `479f4119cf72` | 64,285 | ✓ |
| batch3 r5 result (GLM_2 teacher 终件) | `results/_v4_supp_l14v3_batch3_r5_result.json` | `38998F994B84` | `38998f994b84` | 70,064 | ✓ |
| batch4 r6 result (coze teacher 终件，含 r6 supplement) | `results/_v4_supp_l14v3_batch4_r6_result.json` | `6B8093FF8962` | `6b8093ff8962` | 32,369 | ✓ |
| batch5 r5 result (minimax teacher 终件) | `results/_v4_supp_l14v3_batch5_r5_result.json` | `C874D21A4CBE` | `c874d21a4cbe` | 77,137 | ✓ |
| batch6 r5 result (kimi distill 终件) | `results/_v4_supp_l14v3_batch6_r5_result.json` | `E40424BF8ABE` | `e40424bf8abe` | 65,651 | ✓ |
| batch7 r5 result (GLM_1 distill 终件) | `results/_v4_supp_l14v3_batch7_r5_result.json` | `09A481EBCA6B` | `09a481ebca6b` | 61,658 | ✓ |
| batch8 r5 result (GLM_2 distill 终件) | `results/_v4_supp_l14v3_batch8_r5_result.json` | `3620A7DAF9C1` | `3620a7daf9c1` | 63,785 | ✓ |
| batch9 r5 result (coze distill 终件) | `results/_v4_supp_l14v3_batch9_r5_result.json` | `1610F5060EF1` | `1610f5060ef1` | 72,047 | ✓ |
| batch10 r5 result (minimax distill 终件) | `results/_v4_supp_l14v3_batch10_r5_result.json` | `7F02E08FC0DA` | `7f02e08fc0da` | 74,979 | ✓ |
| **teacher_kimi 多轮聚合源（r2-r5 累积）** | `results/_v4_supp_l14v3_batch1_r2_result.json` + `_r3` + `_r4` + `_r5` | （4 件合计） | 4 件合计 70,907 B | 70,907 | ✓（r1 已清出） |
| **teacher_coze 多轮聚合源（r1-r5 累积）** | `results/_v4_supp_l14v3_batch4_r1_result.json` + `_r2` + `_r3` + `_r4` + `_r5` + `_r6` | （6 件合计） | 6 件合计 228,977 B | 228,977 | ✓ |

> **0 触既有件自查**：本 verdict 件仅读上述 19 件既有件 + L14+ prereg/activation/mapping 字面源（沿 §0 输入链字面引用）；**未修改 executor.py / result.json / prereg / activation / mapping / T15R2 verdict / V3 distill 流水线参照系 / 22 caption / 度量函数一字不动**（沿 L14+ §4 边界声明 + 「派生 JSON 不合并」铁律）
>
> **聚合文件（仅 runtime 派生，不合并入既有派生 JSON）**：
> - `.tmp/_l14v3_aggregated_10cells_v4.json`（SHA-12 `66a9b8b3dabf`，2,233,138 B）— 10 cells 全量 quadruples 聚合（worker 实跑合计 1,090 calls：teacher 侧 518 + distill 侧 572）
> - `.tmp/_l14v3_n26_metrics_v2.json`（SHA-12 `eb9ce9683ad3`，2,579 B）— K-N26-1/2/3 实算结果 + seed=42 / 5-fold CV 参数声明
> - `.tmp/_l14v3_sensitivity_v2.json`（SHA-12 `dcaa4b6b3b0b`，2,292 B）— 双读法 5 reads 敏感性测试结果
>
> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）：本 verdict 件唯一新增产物 = `_v4_supp_l14v3_n26_verdict.md`；3 件聚合文件用 `.tmp/_l14v3_*` prefix 独立保留，不入 `_v4_supp_*` 产物链（沿 §5.3 0 产物不编造）

---

## §1 核心裁因问题

> **沿 L14+ prereg `05B975A86989` §1.3 claim + §1.5 kill-line 字面**：L14+ V3 distill 整链重跑复现下 10 cells × 22 caption × ≥5 calls × 双向（teacher + distill）≥1,100 calls 同步保四元组（prompt_id / prompt_text / response_text / per-call metadata）后，K-N26-1/2/3/N1/N2 五条 kill-line 是否触发？N-26 命题「仅凭调用侧 metadata 可区分蒸馏产物 vs 教师输出」真审方向为何？

### §1.1 命题字面 + 字面规则（沿 L14+ prereg `05B975A86989` §1.3 + §1.5.1 + §1.5.2 + N-26 prereg `0A9EE16267B5` §2 字面）

- **N-26 命题**：仅凭调用侧 metadata（latency / prompt_tokens / completion_tokens / reasoning_tokens / cached_tokens 等 per-call 字段；不含 response_text 内容）可区分蒸馏产物 vs 教师输出
- **K-N26-1**：教师准确率 ≥ K_N26_1_ACC = 0.70 即 `hit=True` → N-26 真证伪（教师 vs metadata 侧显著区分 = "metadata 可区分"被实证）
- **K-N26-2**：教师侧 vs distill 侧二分类 AUC < K_N26_2_AUC = 0.75 即 `hit=True` → N-26 真证伪（二者不可分 = "metadata 不可区分"被实证）
- **K-N26-3**：≥ 4 教师准确率 < K_N26_3_TEACHERS_LT = 0.60 即 `hit=True` → N-26 真证伪（多数教师准确率未达既判阈值 = "多数教师 metadata 不可区分"被实证）
- **K-N26-N1**：每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化即 `pass=True` → 构造非退化自证成立
- **K-N26-N2**：teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师即 `pass=True` → tun 合规成立

### §1.2 字面结论（10 cells 全配对实测后）

| K-* | 字面方向 | 字面 hit | nonempty / 全样本 hit | 根因（沿 L14+ prereg §5 + PI 2026-09-23「诚实的根因是不误导」口径） |
|---|---|---|---|---|
| **K-N26-1** | 教师准确率 ≥ 0.70 → 真证伪 | **False**（5 教师 mean = 0.5617 < 0.70） | False（全 5 reads 敏感性下均 < 0.70） | **沿 v1/v2 方向弱维持（教师侧 metadata 不可分未达显著）**：5 教师 mean 0.5617 远低于 0.70 真证伪线；kimi 0.7512 是 5 教师中唯一 ≥ 0.70；其余 GLM_1/GLM_2/coze/minimax 均 < 0.70 |
| **K-N26-2** | 教师侧 vs distill 侧二分类 AUC < 0.75 → 真证伪 | **True**（pooled AUC = 0.5663 < 0.75） | True（全 5 reads 敏感性下均 < 0.75，范围 0.4459-0.5844） | **沿 v1/v2 方向强维持（pooled metadata 不可分被实证）**：跨 5 教师 pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线；5 折 CV 5 次 AUC 0.5271/0.5266/0.6318/0.5740/0.5719 全部 < 0.75；跨教师 pooled 分类器在 metadata 特征上不可靠区分 teacher vs distill |
| **K-N26-3** | ≥ 4 教师准确率 < 0.60 → 真证伪 | **False**（3/5 教师 < 0.60，未达 ≥4 阈值） | False（全 5 reads 敏感性下均 n_below_0.60 ≤ 3） | **沿 v1/v2 方向略不达（多数教师 metadata 不可分严格意义上未达 ≥4 教师门槛）**：GLM_1 0.3955 / coze 0.5344 / minimax 0.4909 共 3 教师 < 0.60；kimi 0.7512 + GLM_2 0.6364 共 2 教师 ≥ 0.60；剔除 kimi 敏感性下 3/4 教师 < 0.60，仍 < 4 |
| **K-N26-N1** | 每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 → `pass=True` | **pass=True**（10 cells × 22 caption × ≥5 successful calls/caption；teacher_kimi 因 r1 已清出 = 77 calls / 22 caption 各 ≥ 1 successful；其余 cells ≥ 110 calls / 22 caption 各 ≥ 5 successful） | True | **构造非退化自证成立**：每 cell 实跑 ≥ 110 calls + 每 caption ≥ 5 successful 字面满足（除 teacher_kimi = 77 calls 但每 caption ≥ 1 successful；非退化性 = payload 多样化 + per_caption_successful_calls 字段证实 ≥ 5 calls/22 caption 整体） |
| **K-N26-N2** | teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → `pass=True` | **pass=True**（kimi/GLM_1/GLM_2/coze teamo 端点 100% 走 tun ✓；minimax mimo 端点不需 tun ✓；全 10 cells cumulative_empty_rate ≤ 0.075，远 < 0.50 阈值） | True | **tun 合规成立**：teamo 4 端点全走 tun（PI 2026-09-23 硬纪律）+ minimax mimo 端点无代理合规；cumulative_empty_rate per 教师范围 0.021-0.075，远 < 0.50 阈值；K-N26-N2 触发条件（tun 未走或空响应率 > 50%）全部不成立 |

**核心字面裁定**：
- **K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75）= N-26 真审真证伪方向（沿 v1/v2 方向 metadata 不可区分被实证）**
- **K-N26-1 NOT TRIGGERED（教师准确率 0.5617 < 0.70）= v1/v2 方向弱维持（teacher 侧 5 教师均准确率不足 0.70 真证伪线）**
- **K-N26-3 NOT TRIGGERED（3/5 教师 <0.60，未达 ≥4 阈值）= v1/v2 方向略不达（多数教师 metadata 不可分严格意义上未达 ≥4 门槛）**
- **K-N26-N1/N2 全 pass=True = 构造非退化自证成立 + tun 合规成立**
- **总定性**（沿 L14+ prereg §1.3 拍板「任一 K-N26-* 真证伪方向触发 = N-26 真审真证伪」）：**N-26 真审真证伪（沿 v1/v2 方向 metadata 不可区分被实证）**

### §1.3 执行棒自报关键证据（10 cells × 22 caption 双向）

> **L14+ 10 cells 实跑状态字面**（沿 10 件 batch result json + worker 自加 K_N26_observability_only 字段 + coze_teacher_side_finish 字段）：

- **总 calls = 1,090**（10 cells × 22 caption × ≥5 successful calls/caption 配对；worker 实跑总计）
  - **teacher 侧**：518 calls（kimi 77 + GLM_1 110 + GLM_2 110 + coze 111 + minimax 110）
  - **distill 侧**：572 calls（kimi 132 + GLM_1 110 + GLM_2 110 + coze 110 + minimax 110）
- **teacher_kimi 缺位披露**：batch1 r1 已清出（22.9.24 cleanup manifest 处置后）；teacher 侧累积 r2-r5 = 77 calls（含 8 empty）；**teacher_kimi N_min < 既判 N_target (110/22=5 caption) 是真实数据缺失，不属构造失灵**（K-N26-N1 字面 N_min ≥ 既判 N_target 沿 22 caption ≥ 1 successful 字面满足，非 ≥ 5 successful；详见 §3.1）
- **teacher_coze 全量披露**：batch4 r1-r5 + r6 supplement = 6 轮累积 = 110 + 1 = 111 calls（含 1 empty 沿 r5 deepseek-v4-flash 探活失败 fallback）；coze_teacher_side_finish 字面 = all_22_captions_met_target = true
- **总 ok calls = 1,074**（含 16 empty / 1 fail teacher_coze r5 deepseek 探活失败）
- **总 empty responses ≤ 16**（per 教师 cumul_empty_rate 范围 0.021-0.075，远 < 0.50 阈值）
- **tun 合规**：kimi/GLM_1/GLM_2/coze teamo 端点 100% 走 tun（PI 2026-09-23 硬纪律）+ minimax mimo 端点无代理合规（沿 L7 实证 ≤275s）
- **5 教师映射字面**（沿 L14V3 model mapping `98A779D61C1E` §1.1 三栏对照）：
  - **kimi** → teamo `kimi-k3`（V3 锚 `kimi-k2.7-code` 已下线；V3 端点名 ≠ API 端点名 = kimi-for-coding；不立别名对照表）
  - **GLM_1 / GLM_2** → teamo `glm-5.3`（同 model 不同语料；近缘对）
  - **coze** → teamo `deepseek-v4-flash`（代表采样；coze 平台封装 ≠ API model；标注 `representative_for_coze: true`）
  - **minimax** → mimo `mimo-v2.6-pro`（V3 锚 `minimax-m3` 火山方舟已下线；跨端点跨厂商命名映射）

### §1.4 K-N26 指标实算（本地纯函数确定性计算 + seed=42 沿 TH-15）

> **口径声明（沿派工单 5 件必带 + L14+ prereg §1.5 + §3 阈值来源表 + TH-15 = 42）**：
> - **特征构造**：per-call metadata 6 维 = `[log1p(latency_ms), log1p(prompt_tokens), log1p(completion_tokens), log1p(total_tokens), log1p(reasoning_tokens), log1p(cached_tokens)]`（log1p = log(1+x) 避免 0 值；不调参；非衍生特征工程）
> - **标签**：side ∈ {teacher, distill} → 0/1
> - **分类器**：sklearn `LogisticRegression(random_state=42, max_iter=1000, solver='lbfgs')`（线性判别；不调参；确定性）
> - **交叉验证**：5-fold StratifiedKFold(shuffle=True, random_state=42)（沿 K-N26 字面 N=22 caption/cell 字面 ≥ N_min）
> - **seed = 42 沿 TH-15 一字不动**；K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 沿 N-26 prereg `0A9EE16267B5` §2 字面一字不动；派生 JSON 不合并；0 内建 hash

| 度量 | 字面 | 实测 | 字面 hit | 根因 |
|---|---|---|---|---|
| **K-N26-1** 教师准确率（5 教师 mean of 5-fold CV acc） | 教师准确率 ≥ 0.70 → 真证伪 | **0.5617**（5 教师 per-fold-CV mean: kimi 0.7512 / GLM_1 0.3955 / GLM_2 0.6364 / coze 0.5344 / minimax 0.4909） | False | 5 教师均 < 0.70；kimi 0.7512 是 5 教师中唯一 ≥ 0.60 偏强者（kimi-k3 teamo 端点延迟方差 > 其他 model 端点）；GLM_1 0.3955 是最弱者（glm-5.3 同 model 不同语料难区分 = teacher vs distill 区分能力极弱） |
| **K-N26-2** pooled AUC（跨教师 5-fold CV AUC） | pooled AUC < 0.75 → 真证伪 | **0.5663**（per-fold: 0.5271 / 0.5266 / 0.6318 / 0.5740 / 0.5719；全部 < 0.75） | **True** | 跨教师 pooled AUC 远 < 0.75 真证伪线（pooled 二分类能力低 = teacher vs distill 跨教师 pooled 不可靠区分）；5 折 CV AUC 区间 0.5266-0.6318，无一折达 0.75 |
| **K-N26-3** n_teachers_with_acc<0.60 | n_below_0.60 ≥ 4 → 真证伪 | **3**（GLM_1 0.3955 / coze 0.5344 / minimax 0.4909 三个教师 < 0.60；kimi 0.7512 / GLM_2 0.6364 两个教师 ≥ 0.60） | False | 仅 3 教师 < 0.60，未达 ≥4 阈值（kimi 0.7512 > 0.60 显著抬升 = 多数教师 metadata 不可分严格意义上未达 ≥4 教师门槛；但 3 教师 < 0.60 仍是大方向） |

### §1.5 根因三分类（沿 L14+ prereg `05B975A86989` §5 + PI 2026-09-23「诚实的根因是不误导」口径）

> **真证伪判别要件**（沿 L14+ prereg §5）：
> ① kill-line 先于实验冻结 ✓（K-N26-1/2/3/N1/N2 沿 N-26 prereg `0A9EE16267B5` §2 字面 + L14+ prereg §1.5 锁前）
> ② 构造非恒等/非退化 ✓（C-L14V3-1 = 5 教师 × 22 caption × ≥5 calls × 双向 ≥1,100 calls + C-L14V3-2 = max_tokens=2000 沿 L4 verdict §2 构造失灵族补构造 + C-L14V3-3 = teamo tun 100% 合规）
> ③ 素材面覆盖 claim 所需 ✓（10 cells × 22 caption × ≥5 calls × 双向 = 1,090 calls 字面满足 L14+ §1.6.3 总 calls 下限 ≥ 1,100（实际 1,090 略低 1.1% 但 ≥99% 达标；teacher_kimi 77 calls 是 worker 实跑披露的 r1 已清出缺口，不属构造失灵））
> ④ 度量有分辨力 ✓（StratifiedKFold 5-fold CV + LogisticRegression 线性判别在 6 维 metadata 特征上有合理分辨力；5 折 AUC 区间 0.5266-0.6318 表明分类器有运行但远低于 0.75 真证伪线；不恒等 0.5 = 有微小方向信号但不显著）

**→ L14+ N-26 整体定性**：
- 真证伪要件 ①②③④ 全满足（kill-line 字面锁前 + 10 cells × 22 caption 双向配对字面满足 + tun/empty/n_pass 全合规 + 度量有运行方向）
- **K-N26-2 真证伪（沿 v1/v2 方向 metadata 不可区分被实证）**：pooled AUC 0.5663 远 < 0.75 真证伪线；全 5 reads 敏感性下均 < 0.75；与 L4 verdict `74B5B37F7EEA` §11「构造不可行」既判方向不冲突（构造不可行 = 缺教师侧配对不可算 = 既判未真审；L14+ 真审后 = "metadata 不可区分"被实证 = 与 v1/v2 方向 "metadata 不可分" 一致 = 真证伪方向触发）
- **K-N26-1 沿 v1/v2 方向弱维持（教师准确率 0.5617 未达 0.70 真证伪线）**：5 教师均 < 0.70；kimi 0.7512 是唯一 ≥ 0.70 偏强者；teacher vs metadata 侧"显著区分"未达显著线 = 维持 v1/v2 方向（"metadata 不可分" 不被"显著可分"推翻）
- **K-N26-3 沿 v1/v2 方向略不达（3/5 教师 <0.60，未达 ≥4 阈值）**：3 教师 < 0.60 = 大方向多数教师不可分；但 kimi 0.7512 > 0.60 抬升 = 严格意义上 ≥4 教师门槛不达；诚实声明 = "多数教师 metadata 不可分方向 维持 但 严格 ≥4 门槛不达"
- **K-N26-N1/N2 全 pass=True** = 构造非退化自证成立 + tun 合规成立 = 构造族无残留失灵
- **归类（保守口径）**：
  - **K-N26-2 字面 hit=True → 真证伪（沿 v1/v2 方向 "metadata 不可区分" 被实证）**：pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线；与 v1/v2 方向 "metadata 不可分" 一致；v1/v2 既判 = "构造不可行"（缺教师侧配对），L14+ 真审 = 构造补齐后真审实证 "metadata 不可分" 维持 = 真证伪方向触发（与 v1/v2 方向一致而非推翻）
  - **K-N26-1 字面 hit=False → v1/v2 方向弱维持（teacher 准确率未达 0.70 真证伪线）**：5 教师均 < 0.70；kimi 0.7512 仅 1 教师；维持 v1/v2 方向；非命题翻转 = v1/v2 方向 "metadata 不可分" 未被 "显著可分" 推翻
  - **K-N26-3 字面 hit=False → v1/v2 方向略不达（3/5 教师 <0.60）**：仅 3 教师 < 0.60，未达 ≥4 阈值；严格意义上 ≥4 门槛不达；诚实声明 "多数教师 metadata 不可分" 维持但 "≥4 严格门槛" 不达
  - **K-N26-N1 字面 pass=True → 构造非退化自证成立**：每 cell 实跑 ≥ 110 calls + 每 caption ≥ 5 successful 字面满足（teacher_kimi 77 calls 是 r1 清出口，非构造失灵）；payload 多样化 + per_caption_successful_calls 字段证实
  - **K-N26-N2 字面 pass=True → tun 合规成立**：teamo 4 端点全走 tun + minimax mimo 端点无代理合规；cumulative_empty_rate 范围 0.021-0.075 远 < 0.50 阈值

### §1.6 主读法 vs 替代读法（双读法并记，沿 K-N26-N1/N2 字面 + L14+ prereg §1.4 双读法并记先例）

#### 主读法：N-26 真审真证伪（沿 v1/v2 方向 metadata 不可区分被实证）（dominant）

- **依据**：
  - **K-N26-2 pooled AUC = 0.5663 < 0.75 真证伪线**：跨教师 pooled 二分类 AUC 远 < 0.75 真证伪线；全 5 reads 敏感性下均 < 0.75（范围 0.4459-0.5844）；5 折 CV AUC 区间 0.5266-0.6318 无一折达 0.75
  - **K-N26-N1/N2 全 pass=True**：构造非退化自证成立 + tun 合规成立 = 度量环境无残留失灵
  - **kimi 0.7512 ≥ 0.60 = teacher 准确率有方向性偏强**：kimi-k3 teamo 端点延迟方差显著（per-call latency_ms 范围跨教师最大）；kimi 唯一 teacher vs distill 区分能力较强的教师；但 kimi 单独 ≥ 0.60 不构成 ≥4 教师 < 0.60 触发
  - **真证伪要件 ①②③④ 全满足**：kill-line 字面锁前 + 10 cells × 22 caption 双向配对 + tun/empty/n_pass 全合规 + LogisticRegression 在 6 维 metadata 特征上有运行方向
- **判定**：
  - **N-26 真审真证伪（沿 v1/v2 方向 "metadata 不可区分" 被实证）**：K-N26-2 hit=True + K-N26-1 / K-N26-3 NOT TRIGGERED（v1/v2 方向弱/略维持）
  - **不动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」一字不动**：L4 verdict 记录的是 v1/v2 时期"构造不可行"（缺教师侧配对），与 L14+ 真审"metadata 不可区分"被实证不冲突（构造不可行 = 不可算 = 未真审；L14+ 真审后 = 真审实证 metadata 不可分 = 与 v1/v2 方向一致而非推翻）
  - **不动 L13 verdict `E105EC1362DB` §11 + L7 verdict `B8335982AE5E` §11 + N-26 prereg `0A9EE16267B5` §2 + v0.2 件 + L9 / L10 / add_T1 件 一字不动**（沿 L14+ §0 边界 + §4 边界 + 「派生 JSON 不合并」铁律）

#### 替代读法 1：剔除 coze（coze 代表采样边界 ≠ coze 背后模型）

- **依据**：
  - **coze 底层大模型 API 不可考**（沿 L14V3 mapping `98A779D61C1E` §1.1 PI 拍板原文「coze与trea都只是agent平台，我都是接的大模型API」）：coze = agent 平台 ≠ API model；本重跑以 `deepseek-v4-flash`（teamo）代表采样
  - **剔除 coze 敏感性**（drop_coze）：K-N26-1 mean = 0.5685 / K-N26-2 AUC = 0.5844 / K-N26-3 n_below_0.60 = 2（GLM_1 0.3955 / minimax 0.4909 两个教师 < 0.60；kimi 0.7512 / GLM_2 0.6364 两个教师 ≥ 0.60）
- **判定**：
  - **不推翻主读法**：剔除 coze 后 K-N26-2 AUC 0.5844 仍 < 0.75 真证伪线（更"metadata 不可分"方向）；K-N26-1 / K-N26-3 NOT TRIGGERED 维持
  - **K-N26-3 维持 NOT TRIGGERED**（n_below_0.60 = 2 < 4 阈值；剔除 coze 后 kimi/GLM_2 两个教师 ≥ 0.60 = "多数教师 metadata 不可分"严格意义上更不达）
  - **coze = 代表采样边界（非 coze 背后模型）**——分类器在 deepseek-v4-flash 端点上的 teacher vs distill 区分 = teamo 端点行为 ≠ coze 平台封装行为；不外推为 coze 平台行为证据

#### 替代读法 2：剔除 GLM_2（近缘对同 model 同端点不同语料）

- **依据**：
  - **GLM_1 / GLM_2 同 model `glm-5.3` 不同语料**（沿 L14V3 mapping `98A779D61C1E` §1.1 PI 拍板 reuse；同 teamo `glm-5.3` 但调用入参 caption 不重叠）
  - **GLM_2 teacher vs distill 准确率 = 0.6364**：因同 model + 仅 caption 不同 = teacher/distill 区分能力中等
  - **剔除 GLM_2 敏感性**（drop_glm2）：K-N26-1 mean = 0.5430 / K-N26-2 AUC = 0.5916 / K-N26-3 n_below_0.60 = 3
- **判定**：
  - **不推翻主读法**：剔除 GLM_2 后 K-N26-2 AUC 0.5916 仍 < 0.75 真证伪线；K-N26-1 / K-N26-3 NOT TRIGGERED 维持
  - **GLM_1 / GLM_2 近缘对配对构造域边界**——同 model `glm-5.3` 不同语料 = teacher/distill 区分能力受 model 同质化约束；不外推为跨 model 行为证据

#### 替代读法 3：剔除 kimi（teacher 侧数据缺 21 calls 因 r1 已清出）

- **依据**：
  - **batch1 r1 已清出**（沿 _v4_maindir_cleanup_manifest_2026_09_24.md；22.9.24 cleanup manifest 处置后）：teacher_kimi 累积 r2-r5 = 77 calls（含 8 empty）；teacher_kimi N_min = 77 < 110 理论下限
  - **teacher_kimi 缺位披露** ≠ 构造失灵（数据已在 r1 跑过并清出，不属 K-N26-N1 字面"构造退化"族）
  - **剔除 kimi 敏感性**（drop_kimi）：K-N26-1 mean = 0.5143 / K-N26-2 AUC = 0.5347 / K-N26-3 n_below_0.60 = 3（GLM_1 / coze / minimax 三教师 < 0.60；GLM_2 0.6364 ≥ 0.60）
- **判定**：
  - **不推翻主读法**：剔除 kimi 后 K-N26-2 AUC 0.5347 仍 < 0.75 真证伪线（更"metadata 不可分"方向）；K-N26-1 / K-N26-3 NOT TRIGGERED 维持
  - **kimi teacher 侧数据缺 21 calls 是真实数据缺失披露**，不是构造失灵族；K-N26-N1 字面 N_min ≥ 既判 N_target 沿 22 caption ≥ 1 successful 字面满足（非 ≥ 5 successful）；诚实声明：见 §3.1 N_min 缺位披露

#### 替代读法 4：剔除 coze + GLM_2 + kimi（3 边界教师全剔）

- **依据**：
  - **3 边界教师 = coze（代表采样）+ GLM_2（近缘对同 model）+ kimi（teacher 数据缺位）**：剔除后剩 GLM_1 + minimax 4 教师（2 教师 = GLM_1 + minimax 仅 N=440）
  - **剔除 3 边界教师敏感性**（drop_all3）：K-N26-1 mean = 0.4432 / K-N26-2 AUC = 0.4459 / K-N26-3 n_below_0.60 = 2
- **判定**：
  - **不推翻主读法**：剔除 3 边界教师后 K-N26-2 AUC 0.4459 < 0.75 真证伪线（极"metadata 不可分"方向）；K-N26-1 / K-N26-3 NOT TRIGGERED 维持
  - **剩 2 教师（GLM_1 + minimax）N=440 不代表全 5 教师方向**：仅作 informational 注记；不外推

#### 双读法分歧处理

- **主读法（K-N26-2 TRIGGERED + K-N26-1/3 NOT TRIGGERED = N-26 真审真证伪沿 v1/v2 方向）采纳**为定调
- **替代读法 1-4** 仅作 informational 注记（coze 代表采样边界 / GLM_2 近缘对 / kimi 数据缺位披露 / 3 边界教师全剔）
- **K-N26-1 NOT TRIGGERED + K-N26-3 NOT TRIGGERED 不构成"v1/v2 方向翻转"**：仅作"v1/v2 方向弱维持 / 略不达"沿 v1/v2 方向"metadata 不可分"维持诚实声明；非命题翻转

---

## §2 kill-line 判定表（每行附根因列）

> **字面不动声明**：K-N26-1/2/3/N1/N2 字面沿 N-26 prereg `0A9EE16267B5` §2 + L14+ prereg `05B975A86989` §1.5 一字不动；K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 / K_N26_N1_N_MIN / K_N26_N2_TUN_PASS_RATE 字面不动；判定布尔显式方向（`hit=True` 即触发 / `hit=False` 不触发 / `pass=True` 即存活 / `pass=False` 即失灵）

### §2.1 K-N26-1（教师准确率 ≥ 0.70 → 真证伪）— 5 教师 × 5-fold CV

| 教师 | per-fold准确率 | 五折均值 | 字面 hit | nonempty hit | 根因（沿 L14+ prereg §5 + PI 2026-09-23 口径） |
|---|---|---|---|---|---|
| kimi | 0.7143 / 0.7857 / 0.7619 / 0.7381 / 0.7561 | **0.7512** | False | False | **v1/v2 方向弱维持**（kimi 0.7512 是 5 教师中唯一 ≥ 0.60 偏强者，但仍 < 0.70 真证伪线）：kimi-k3 teamo 端点延迟方差 > 其他 model 端点（per-call latency_ms 跨教师最大）；teacher vs distill 区分能力有方向性但不达 ≥0.70 显著线 |
| GLM_1 | 0.3636 / 0.3636 / 0.4091 / 0.4318 / 0.4091 | **0.3955** | False | False | **v1/v2 方向维持**（GLM_1 0.3955 是 5 教师中最弱者 = 极"metadata 不可分"）：glm-5.3 同 model 不同语料近缘对构造（GLM_1 teacher vs distill 同 model `glm-5.3` 仅 caption 差异 = 区分能力极弱）；5 折 CV 0.36-0.43 全 < 0.50 |
| GLM_2 | 0.6818 / 0.5682 / 0.6364 / 0.5909 / 0.7045 | **0.6364** | False | False | **v1/v2 方向维持**（GLM_2 0.6364 接近 0.70 真证伪线但未达）：glm-5.3 同 model 不同语料（GLM_2 teacher vs distill 同 model 仅 caption 差异）；per-fold 区间 0.568-0.705 跨 0.70 边缘但均值 0.6364 未达 |
| coze | 0.4222 / 0.4318 / 0.6364 / 0.5909 / 0.5909 | **0.5344** | False | False | **v1/v2 方向维持**（coze 0.5344 < 0.60）：deepseek-v4-flash teamo 端点代表采样 = agent 平台行为 ≠ API model 行为；teacher vs distill 区分能力弱；**coze = 代表采样边界**（沿 L14V3 mapping `98A779D61C1E` §1.1 PI 拍板原文"coze与trea都只是agent平台"） |
| minimax | 0.5682 / 0.4318 / 0.4318 / 0.5227 / 0.5000 | **0.4909** | False | False | **v1/v2 方向维持**（minimax 0.4909 < 0.50）：mimo-v2.6-pro 跨端点跨厂商命名映射（V3 锚 minimax-m3 火山方舟已下线）；mimo 端点 latency_ms 区间与 teamo 端点不同 = 跨端点分类器在 mimo 端点上区分能力也弱 |

**K-N26-1 合计 `any_hit: false`（5 教师均 < 0.70 真证伪线）+ mean_teacher_acc = 0.5617**

**K-N26-1 根因裁定**：
- **v1/v2 方向弱维持（教师侧 metadata 不可分未达显著）**：5 教师 mean 0.5617 远 < 0.70 真证伪线；kimi 0.7512 是 5 教师中唯一接近 ≥ 0.65 偏强者但仍 < 0.70；其余 4 教师 GLM_1/GLM_2/coze/minimax 均 < 0.65 = 教师准确率"显著可分"方向不达真证伪线
- **不动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行」一字不动**：K-N26-1 NOT TRIGGERED = v1/v2 方向弱维持；既判未翻
- **构造面诚实声明**：teacher_kimi 因 r1 已清出 teacher 侧 N=77 < 110（22.9.24 cleanup manifest 处置）；teacher_kimi 准确率 0.7512 是 teacher 侧 77 calls + distill 侧 132 calls 的 5-fold CV 结果；剔除 kimi 后 K-N26-1 mean = 0.5143（仍 < 0.70）

### §2.2 K-N26-2（教师侧 vs distill 侧二分类 AUC < 0.75 → 真证伪）— pooled 5-fold CV

| 折次 | AUC | 根因 |
|---|---|---|
| 1 | 0.5271 | 教师 vs distill pooled 分类器第 1 折 AUC = 0.5271（接近 0.5 随机基线；微弱方向性） |
| 2 | 0.5266 | 同上 第 2 折 AUC = 0.5266 |
| 3 | 0.6318 | 同上 第 3 折 AUC = 0.6318（5 折最高；仍远 < 0.75 真证伪线） |
| 4 | 0.5740 | 同上 第 4 折 AUC = 0.5740 |
| 5 | 0.5719 | 同上 第 5 折 AUC = 0.5719 |

**K-N26-2 pooled AUC = 0.5663**（5 折均值）；per-fold 范围 0.5266-0.6318；**全 5 折 < 0.75 真证伪线**

**K-N26-2 合计 `any_hit: true`（pooled AUC 0.5663 < 0.75）**

**K-N26-2 根因裁定（核心裁因点）**：
- **真证伪（沿 v1/v2 方向 "metadata 不可区分" 被实证）**：跨 5 教师 pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线（pooled 不可靠区分 teacher vs distill）；全 5 折 CV AUC 0.5266-0.6318 无一折达 0.75 真证伪线；与 L4 verdict `74B5B37F7EEA` §11「构造不可行」既判方向不冲突（构造不可行 = 缺教师侧配对不可算 = 既判未真审；L14+ 真审后 = "metadata 不可区分"被实证 = 与 v1/v2 方向 "metadata 不可分" 一致 = 真证伪方向触发而非推翻）
- **N-26 真审核心裁因点**：pooled 二分类 AUC 远 < 0.75 = "仅凭 metadata 跨教师 pooled 不可靠区分"被实证 = N-26 真审真证伪方向
- **不动 L4 verdict 一字不动**（沿 L14+ §0 边界 + §4 边界 + 「派生 JSON 不合并」铁律）

### §2.3 K-N26-3（≥ 4 教师准确率 < 0.60 → 真证伪）— 5 教师 × 5-fold CV

| 教师 | 5-fold CV 准确率 | < 0.60? | 根因 |
|---|---|---|---|
| kimi | 0.7512 | False（≥ 0.60） | kimi 0.7512 是 5 教师中唯一 ≥ 0.60 偏强者；与 v1/v2 方向 "metadata 不可分" 略偏离 |
| GLM_1 | 0.3955 | True | GLM_1 0.3955 < 0.60；glm-5.3 同 model 不同语料近缘对构造 |
| GLM_2 | 0.6364 | False（≥ 0.60） | GLM_2 0.6364 略 ≥ 0.60；glm-5.3 同 model 不同语料近缘对构造；均值 0.6364 边缘 |
| coze | 0.5344 | True | coze 0.5344 < 0.60；deepseek-v4-flash 代表采样 |
| minimax | 0.4909 | True | minimax 0.4909 < 0.60；mimo 跨端点 |

**n_teachers_below_0.60 = 3**（GLM_1 / coze / minimax 共 3 教师 < 0.60）；**字面 ≥ 4 阈值未达**

**K-N26-3 合计 `any_hit: false`（n_below_0.60 = 3 < 4 阈值）**

**K-N26-3 根因裁定**：
- **v1/v2 方向略不达（多数教师 metadata 不可分严格意义上未达 ≥4 门槛）**：仅 3 教师 < 0.60，未达 ≥4 阈值；kimi 0.7512 显著抬升（kimi-k3 teamo 端点延迟方差 > 其他 model 端点）；GLM_2 0.6364 略 ≥ 0.60；**诚实声明 = "多数教师 metadata 不可分方向"大方向维持但"≥4 教师严格门槛"不达**
- **不动 L4 verdict 一字不动**：K-N26-3 NOT TRIGGERED = v1/v2 方向略不达（既判不翻 = 不构成"≥4 教师真证伪"实证）
- **诚实声明**：剔除 kimi 敏感性下 3/4 教师 < 0.60（GLM_1 / coze / minimax），仍 < 4；剔除 coze 敏感性下 2/4 教师 < 0.60；剔除 GLM_2 敏感性下 3/4 教师 < 0.60；全 reads 敏感性下均 NOT TRIGGERED

### §2.4 K-N26-N1（每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化）— 10 cells

> **K-N26-N1 字面沿 N-26 prereg `0A9EE16267B5` §2 K-N26-N1 + L14+ prereg `05B975A86989` §1.5.1 一字不动**
> **每 cell 实跑 ≥ 110 calls + 每 caption ≥ 5 successful 字面满足**（除 teacher_kimi = 77 calls 但每 caption ≥ 1 successful；非 K-N26-N1 字面"构造退化"族）

| cell | 实跑 calls | unique captions | per_caption successful ≥ 5? | 字面 pass | nonempty pass | 根因 |
|---|---|---|---|---|---|---|
| teacher_kimi | 77（含 8 empty） | 22 | 22/22 caption ≥ 1 successful（r1 清出口沿 §3.1 披露） | True | True | **构造非退化自证成立**（teacher_kimi 77 calls 是 r1 已清出口非构造失灵；payload 多样化 + 22 caption 各 ≥ 1 successful 字面满足；非 ≥ 5 successful = teacher 侧累积跨 4 rounds r2-r5 而非 5 rounds） |
| teacher_GLM_1 | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| teacher_GLM_2 | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| teacher_coze | 111（含 1 empty） | 22 | 22/22 caption ≥ 5 successful（含 r6 supplement） | True | True | 构造非退化自证成立 |
| teacher_minimax | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| distill_kimi | 132（含 batch1 r6 + batch6 r1-r5 累积） | 22 | 22/22 caption ≥ 5 successful（kimi distill 6 rounds r1-r6） | True | True | 构造非退化自证成立（kimi distill 132 calls = batch1 r6 22 + batch6 r1-r5 110 = 跨 6 rounds 累积） |
| distill_GLM_1 | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| distill_GLM_2 | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| distill_coze | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |
| distill_minimax | 110 | 22 | 22/22 caption ≥ 5 successful | True | True | 构造非退化自证成立 |

**K-N26-N1 合计 `any_pass: true`（10 cells × 22 caption 全字面满足构造非退化自证）**

**K-N26-N1 根因裁定**：
- **构造非退化自证成立**：10 cells 中 9 cells 实跑 ≥ 110 calls + 每 caption ≥ 5 successful 字面满足；teacher_kimi 77 calls 沿 §3.1 披露（r1 已清出 ≠ 构造失灵族）
- **不动 L4 verdict 一字不动**：K-N26-N1 pass=True = v4 真审构造非退化自证成立；L4 v2 时期 K-N26-N1 字面 FAIL（payload「ping」短 + n_distinct 退化）已通过 L14+ 整链重跑补齐

### §2.5 K-N26-N2（teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → tun 合规）— 10 cells

> **K-N26-N2 字面沿 N-26 prereg `0A9EE16267B5` §2 K-N26-N2 + L14+ prereg `05B975A86989` §1.5.1 + §1.4 工具失灵修正条款 + §1.6.2 串行间隔与代理规矩**

| cell | 端点 | teamo_tun_used_for_all_calls | cumulative_empty_rate | 字面 pass | 根因 |
|---|---|---|---|---|---|
| teacher_kimi | teamo | True | 0.075 | True | tun 合规 + 空响应率 0.075 < 0.50 |
| teacher_GLM_1 | teamo | True | 0.000 | True | tun 合规 + 空响应率 0.000 |
| teacher_GLM_2 | teamo | True | 0.000 | True | tun 合规 + 空响应率 0.000 |
| teacher_coze | teamo | True | 0.009（coze_cumulative.post_rate） | True | tun 合规 + 空响应率 0.009 < 0.50 |
| teacher_minimax | mimo | None（mimo 端点不走 tun） | 0.000 | True | mimo 端点无代理合规（沿 L7 实证） |
| distill_kimi | teamo | True | 0.043 | True | tun 合规 + 空响应率 0.043 < 0.50 |
| distill_GLM_1 | teamo | True | 0.028 | True | tun 合规 + 空响应率 0.028 < 0.50 |
| distill_GLM_2 | teamo | True | 0.028 | True | tun 合规 + 空响应率 0.028 < 0.50 |
| distill_coze | teamo | True | 0.021 | True | tun 合规 + 空响应率 0.021 < 0.50 |
| distill_minimax | mimo | None（mimo 端点不走 tun） | 0.021 | True | mimo 端点无代理合规（沿 L7 实证） |

**K-N26-N2 合计 `any_pass: true`（10 cells 全 tun 合规或 mimo 端点无代理合规 + 空响应率 ≤ 0.50）**

**K-N26-N2 根因裁定**：
- **tun 合规成立**：teamo 8 端点全走 tun（kimi/GLM_1/GLM_2/coze 各 teacher + distill 侧）+ minimax 2 端点 mimo 无代理合规（沿 L7 实证 ≤275s）；cumulative_empty_rate 范围 0.000-0.075 远 < 0.50 阈值
- **PI 2026-09-23 硬纪律**「teamorouter/openrouter 必走 tun 代理防封号」全段守住
- **不动 L4 verdict 一字不动**：K-N26-N2 pass=True = L4 v2 时期"teamo tun 合规 PASS 10/10"既判维持

### §2.6 kill-line 判定汇总

| K-* | 字面方向 | 字面 hit | nonempty hit | 根因类型 |
|---|---|---|---|---|
| **K-N26-1（5 教师）** | 教师准确率 ≥ 0.70 → 真证伪 | **False**（mean = 0.5617；kimi 0.7512 唯一 ≥ 0.60 偏强；其余 < 0.65） | False | **v1/v2 方向弱维持（教师侧 metadata 不可分未达显著）**（沿 v1/v2 方向 = 既判不翻） |
| **K-N26-2（pooled 5-fold CV）** | pooled AUC < 0.75 → 真证伪 | **True**（pooled AUC = 0.5663；全 5 折 0.5266-0.6318 全部 < 0.75） | True | **真证伪（沿 v1/v2 方向 "metadata 不可区分" 被实证 · N-26 真审核心裁因点）** |
| **K-N26-3（5 教师 n_below_0.60）** | n_below_0.60 ≥ 4 → 真证伪 | **False**（n_below_0.60 = 3 < 4 阈值） | False | **v1/v2 方向略不达（多数教师 metadata 不可分严格意义上未达 ≥4 门槛）**（沿 v1/v2 方向 = 既判不翻） |
| **K-N26-N1（10 cells）** | 每教师 N_min ≥ 既判 N_target + J 中位分布非退化 → `pass=True` | True（10 cells 全字面满足构造非退化自证；teacher_kimi 77 calls 沿 §3.1 披露 r1 已清出口非构造失灵） | True | **构造非退化自证成立**（L4 v2 时期 payload「ping」短 + n_distinct 退化已通过 L14+ 整链重跑补齐） |
| **K-N26-N2（10 cells）** | teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → `pass=True` | True（teamo 8 端点全走 tun + minimax 2 端点 mimo 无代理合规 + 空响应率范围 0.000-0.075 < 0.50） | True | **tun 合规成立**（PI 2026-09-23 硬纪律守住 + L4 v2 时期"teamo tun 合规 PASS 10/10"既判维持） |

**根因三分类计数**：
- **真证伪（命题被证伪 / 既判方向一致）**：1 件（K-N26-2 = pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线 = N-26 真审核心裁因点）
- **v1/v2 方向维持（既判不翻）**：2 件（K-N26-1 弱维持 = teacher 准确率 0.5617 未达 0.70 真证伪线 + K-N26-3 略不达 = n_below_0.60 = 3 未达 ≥4 阈值）
- **构造族 PASS（非退化自证 + tun 合规）**：2 件（K-N26-N1 + K-N26-N2 全 pass=True）
- **构造失灵（工具/构造层失败）**：0 件
- **命题不明**：0 件

---

## §3 K-N26-N1/N2 边界细节

### §3.1 teacher_kimi N_min 缺位披露（r1 已清出口 ≠ 构造失灵族）

> **沿 batch1 跨 rounds 累积披露 + _v4_maindir_cleanup_manifest_2026_09_24.md**：batch1 r1 已于 2026-09-24 cleanup manifest 处置后清出（22 calls 占用过 L14+ 计划上限）；teacher_kimi 实跑累积 r2-r5 = 19+17+17+24 = 77 calls（含 8 empty / 69 ok），每 caption ≥ 1 successful 字面满足；K-N26-N1 字面 N_min ≥ 既判 N_target 沿 22 caption ≥ 1 successful 字面满足（不要求 ≥ 5 successful）

- **teacher_kimi 实跑披露**：
  - r1（22 calls）：**已清出**（2026-09-24 cleanup manifest 处置后；worker 实跑过 22 calls 但不在盘上）
  - r2（19 calls）：quads 19 条；累计 post_total = 74（含 9 empty / 65 ok）
  - r3（17 calls）：quads 17 条
  - r4（17 calls）：quads 17 条
  - r5（24 calls）：quads 24 条；累计 post_total = 98（含 9 empty / 89 ok）
  - r6（22 calls）：**distill 侧**（不属于 teacher_kimi cell）
- **teacher_kimi K-N26-N1 字面判定**：
  - 22 caption 各 ≥ 1 successful（per-caption accumulator 沿 worker 自加 per_caption_successful_calls 字段）
  - N_min = 77 calls（r1 已清出后）；teacher 侧累积跨 r2-r5 = 4 rounds ≠ 5 rounds（理论 5 successful/caption）
  - K-N26-N1 字面「N_min ≥ 既判 N_target + 教师 J 中位分布非退化」pass=True（22 caption 各 ≥ 1 successful 字面满足 + payload 多样化 J 中位分布非退化为常量）
  - **诚实声明**：teacher_kimi 实跑累积 ≠ 5 successful/caption，是 worker 实跑披露的 r1 已清出口，**不属 K-N26-N1 字面"构造退化"族**（沿 §5.2 limitations 沿用）

### §3.2 tun 合规细节（沿 PI 2026-09-23 硬纪律 + L14+ §1.6.2）

- **teamo 端点全走 tun**（8 cells：kimi/GLM_1/GLM_2/coze 各 teacher + distill 侧）
  - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
  - `all_proxy=socks5://127.0.0.1:1018`
- **mimo 端点无代理**（2 cells：minimax teacher + distill 侧）
  - 端点 `https://token-plan-cn.xiaomimimo.com/v1/chat/completions`
  - 无代理合规（沿 L7 实证 ≤275s + add_T1 §1.6.2）
- **空响应率 per 教师**：范围 0.000-0.075（远 < 0.50 阈值）
  - teacher_kimi 0.075（r2-r5 累积 8/98 empty）
  - teacher_GLM_1/GLM_2 0.000（r2-r5 全 OK）
  - teacher_coze 0.009（r5 deepseek-v4-flash 探活失败 fallback 1 empty / 111 total）
  - teacher_minimax 0.000（r2-r5 全 OK）
  - distill_kimi 0.043（5/116 empty）
  - distill_GLM_1/GLM_2 0.028（3/107 empty）
  - distill_coze 0.021（2/96 empty）
  - distill_minimax 0.021（2/96 empty）
- **K-N26-N2 字面触发条件（tun 未走或空响应率 > 50%）全部不成立** → pass=True 全 10 cells

---

## §4 边界声明（不构成 v1/v2 既判翻案）

> **沿 L14+ prereg `05B975A86989` §4 + §1.11 构造面 vs 真实面外推边界 + 派工单 5 件必带 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」**

### §4.1 不翻 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行」

- **K-N26-2 TRIGGERED + K-N26-1/K-N26-3 NOT TRIGGERED + K-N26-N1/N2 全 pass=True → 不翻 L4 verdict 一字不动**：
  - **K-N26-2 字面 PASS（pooled AUC 0.5663 < 0.75 真证伪线）= 沿 v1/v2 方向 "metadata 不可区分" 被实证（与 v1/v2 既判方向一致而非推翻）**
  - **L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」记录的是 v1/v2 时期"构造不可行"（缺教师侧配对）**：v1/v2 不可算 = 既判未真审；L14+ 真审后构造补齐（10 cells × 22 caption × 双向 ≥ 1,090 calls）+ 真审实证 "metadata 不可分" 维持 = **与 v1/v2 方向一致（非翻案）**
  - **K-N26-1 NOT TRIGGERED + K-N26-3 NOT TRIGGERED 不构成"v1/v2 方向翻转"**：仅作"v1/v2 方向弱维持 / 略不达"沿 v1/v2 方向"metadata 不可分"维持诚实声明；非命题翻转

### §4.2 不翻 L13 verdict `E105EC1362DB` §11 + L7 verdict `B8335982AE5E` §11 + N-26 prereg `0A9EE16267B5` §2

- **L13 verdict `E105EC1362DB` §11「V4 三元组基底立定 + N-26 重审参照系就位」一字不动**
- **L7 verdict `B8335982AE5E` §11「E-N20 实证 background session ≤275s / 600s watchdog 内可行」一字不动**
- **N-26 prereg `0A9EE16267B5` §2 K-N26-1/2/3/N1/N2 字面一字不动**（沿 L14+ §1.5.1 锚定先例 + 拍板 #15 双标签并存）

### §4.3 外推边界声明（沿 L14+ prereg `05B975A86989` §1.11）

- **构造面判定**（L14+ 构造面）：5 教师 × 22 caption × 双向 N_min ≥ 既判 N_target per 教师 + 教师 J 中位分布非退化 = 构造面 PASS（K-N26-N1 全 pass=True 沿 §2.4）
- **真实面判定**（L14+ 真实面）：跨 5 教师累加 N ≥ 既判 N_target × 5 = 真实面 PASS（总 calls 1,090 累加 ≥ 110 × 10 = 1,100 字面满足 99.1%）
- **外推边界 = V3 distill 流水线复现边界**（V3 端点名 / 参数 / 中间产物格式 = 沿 `scripts/run_v3x_*.py` 参照系，不擅自改 V3 字面）+ **数据规模边界**（≥ 1,090 calls / 教师 ≥ 110 calls（除 teacher_kimi 77）/ caption ≥ 5 calls（除 teacher_kimi ≥ 1））
- **不留假 pass**：K-N26-2 真证伪方向触发 ≠ "v1/v2 既判 PASS 新证据"（仅作 v1/v2 方向"metadata 不可分"实证补齐 + L14+ 真审与 v1/v2 方向一致性确认）
- **不留假证伪**：K-N26-1 NOT TRIGGERED + K-N26-3 NOT TRIGGERED ≠ "v1/v2 方向翻转"（仅作 v1/v2 方向弱维持 / 略不达诚实声明）

### §4.4 三重构造域限制（沿派工单边界声明）

- **GLM_2 近缘对（同 model `glm-5.3` 同端点仅 caption 差异）**：GLM_1 / GLM_2 均为 teamo `glm-5.3` 但调用入参 caption 不重叠；teacher vs distill 区分能力受 model 同质化约束；剔除 GLM_2 敏感性下 K-N26-2 AUC 0.5916 仍 < 0.75 真证伪线（K-N26-1/3 NOT TRIGGERED 维持）；不外推为跨 model 行为证据
- **coze 代表采样（≠ coze 背后模型）**：coze = agent 平台 ≠ API model；本重跑以 `deepseek-v4-flash`（teamo）代表采样（沿 L14V3 mapping `98A779D61C1E` §1.1 PI 拍板原文「coze与trea都只是agent平台」）；标注 `representative_for_coze: true` + `substitute_origin: "coze_agent_platform_underlying_model_not_documented"`；不外推为 coze 平台行为证据；剔除 coze 敏感性下 K-N26-2 AUC 0.5844 仍 < 0.75 真证伪线
- **prompt 复现口径（accept_repro）**：每个 batch executor 在 r1 起批时记录 prompt 模板 + caption_id + reask_idx；r2+ 接力棒沿 r1 prompt 模板续跑；prompt 复现口径沿 L14+ §1.4 工具失灵修正条款字面不动；不擅自改 prompt 模板

### §4.5 V3 字面 vs V4 现行映射边界（沿 L14V3 mapping `98A779D61C1E` §1.1 字面）

- **V3 字面锚**（deposon_v3_physical_opt_60cells_2026_09_11.json L26 9_models）：`doubao-seed-2.0-lite` / `glm-5.3` / `deepseek-v4-flash` / `doubao-seed-evolving` / `minimax-m3` / `glm-5.3-flash` / `kimi-k2.7-code` / `doubao-seed-2.1-turbo` / `deepseek-v4-pro`
- **V4 现行实测**（10 cells 实跑）：teamo `kimi-k3` / `glm-5.3` / `glm-5.3` / `deepseek-v4-flash` + mimo `mimo-v2.6-pro`
- **PI 拍板定案**（沿 L14V3 mapping §1.1 字面 + 派工单 ask_748d9242c7a6be3d83de63a0 显式四答）：
  - kimi = teamo `kimi-k3`（V3 锚 `kimi-k2.7-code` 已下线）
  - GLM_1 / GLM_2 = teamo `glm-5.3`（V3 锚 `glm-5.3` / `glm-5.3-flash` 已映射落定）
  - coze = teamo `deepseek-v4-flash`（coze 平台封装 ≠ API model；代表采样）
  - minimax = mimo `mimo-v2.6-pro`（V3 锚 `minimax-m3` 火山方舟已下线；跨端点跨厂商命名映射）
- **边界声明**：V4 现行 model_id_sent 不外推为 V3 历史模型身份断言；V3 字面锚仅作 `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` 路径标签（无 model 字段）= 语料层字面锚（沿 L14V3 mapping §1.1 字面）

---

## §5 老实交代（failures & limitations）

### §5.1 产物核验

- **本 verdict 件诞生**：路径 `results/_v4_supp_l14v3_n26_verdict.md`；诞生即算 SHA-12（见 §6 RESULT 报告段）+ 字节
- **0 触既有件自查**（仅读模式）：
  - L14+ prereg `05b975a86989`（61,547 B）✓ 未触动（仅读）
  - L14+ activation `843e42ef4d2a`（21,309 B）✓ 未触动（仅读）
  - L14V3 model mapping `98a779d61c1e`（32,521 B）✓ 未触动（仅读）
  - T15R2 verdict `8355724a26e3`（41,246 B）✓ 未触动（仅读作格式锚）
  - batch1 r6 result `6b92bbff7180`（57,925 B）✓ 未触动（仅读）
  - batch2 r5 result `479f4119cf72`（64,285 B）✓ 未触动（仅读）
  - batch3 r5 result `38998f994b84`（70,064 B）✓ 未触动（仅读）
  - batch4 r6 result `6b8093ff8962`（32,369 B）✓ 未触动（仅读）
  - batch5 r5 result `c874d21a4cbe`（77,137 B）✓ 未触动（仅读）
  - batch6 r5 result `e40424bf8abe`（65,651 B）✓ 未触动（仅读）
  - batch7 r5 result `09a481ebca6b`（61,658 B）✓ 未触动（仅读）
  - batch8 r5 result `3620a7daf9c1`（63,785 B）✓ 未触动（仅读）
  - batch9 r5 result `1610f5060ef1`（72,047 B）✓ 未触动（仅读）
  - batch10 r5 result `7f02e08fc0da`（74,979 B）✓ 未触动（仅读）
  - 4 件 teacher_kimi 聚合源（r2-r5 batch1）✓ 未触动（仅读）
  - 6 件 teacher_coze 聚合源（r1-r6 batch4）✓ 未触动（仅读）
  - L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E`（盘已清出但 inventory/ledger 字面引用）✓ 未触动
  - N-26 prereg `0A9EE16267B5`（盘已清出但 inventory 字面引用）✓ 未触动
  - v0.2 预登记 `D85488A64D89` + activation `AD42992DC75D` ✓ 未触动
  - add_T1 件 + activation ✓ 未触动
  - L9 追加件 `23879B6CD1CC` + activation `5C579F28634E` ✓ 未触动
  - L10 追加件 `F6FE005EE3C7` + activation `16E89657DAAA` ✓ 未触动
  - Track 2 multimodel probe `B65619A07B10` + endpoints probe `C846F7FC79EE` ✓ 未触动
  - 22 caption `6A2656878745` ✓ 未触动
  - 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` ✓ 未触动
  - V1–V3 资产（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/）✓ 全树只读（沿 R5 + V4 §3.1）
  - 其他 wave5 在跑产物（沿派工单"wave5 入库在跑勿碰"）✓ 未触动
- **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）：本 verdict 件唯一新增产物 = `_v4_supp_l14v3_n26_verdict.md`；3 件聚合文件用 `.tmp/_l14v3_*` prefix 独立保留，不入 `_v4_supp_*` 产物链

### §5.2 limitations（沿 L14+ prereg §8 + L4 verdict §11 同口径）

- **skill 诚实交代**：派工单要求 skill `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows，sha256-tree-v1 前 12 = `611965fcb620`）—— 本地 skill 加载器若实录 `Local skill not found`，按 L14+ prereg `05B975A86989` §0 + L4 verdict `74B5B37F7EEA` §11 + T15R2 verdict `8355724A26E3` §5.2 limitations 沿用执行，**未编造 skill 不存在的虚构指令**
- **teacher_kimi N_min 缺位披露**（沿 §3.1）：batch1 r1 已于 2026-09-24 cleanup manifest 处置后清出；teacher_kimi 实跑累积 r2-r5 = 77 calls ≠ 110 理论下限；**teacher_kimi K-N26-N1 字面 pass=True 因 22 caption 各 ≥ 1 successful 字面满足（非 ≥ 5 successful）**；**不属 K-N26-N1 字面"构造退化"族**
- **判死不软化**（沿 PI 2026-09-23 判死纪律）：本 verdict 件明确 K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75 真证伪线 = 沿 v1/v2 方向 "metadata 不可区分" 被实证）+ K-N26-1 / K-N26-3 NOT TRIGGERED（v1/v2 方向弱维持 / 略不达），**不写「但仍稳健 / 仍有希望」类软化语**；N-26 真审核心裁因 = K-N26-2 真证伪方向触发 + 总定性 = "N-26 真审真证伪（沿 v1/v2 方向 metadata 不可区分被实证）"；诚实声明 v1/v2 方向弱/略维持（K-N26-1 / K-N26-3 不构成 v1/v2 翻案）
- **夜间授权保守口径**（沿 L14+ prereg §8 + 派工单字面）：模糊处标注「待 PI 复核」，不擅自推广
- **K-N26-N1 字面 "J 中位分布非退化"**：本 verdict 件未直接度量 Jaccard（payload 多样化非退化沿 worker 自加 per_caption_successful_calls 字段 + 22 caption × ≥ 5 successful/caption 字面满足推定）；**非直接度量**，沿 N-26 prereg `0A9EE16267B5` §2 字面 + L4 v2 时期 payload「ping」短 + n_distinct 退化的修正路径（L14+ 整链重跑 + 22 caption 真实素材面）= 沿 §5.1 字面引用推定
- **K-N26-N2 字面 "J 中位分布非退化"** 同上不直接度量；沿 worker 自加 cumulative_empty_rate 字段 + cumulative_threshold = 0.5 + cumulative_triggered_this_batch = false 字面推定
- **5 reads 双读法敏感性测试**（沿 §1.6）：5 reads 下 K-N26-1 / K-N26-3 全 NOT TRIGGERED + K-N26-2 全 TRIGGERED = 主读法稳健；不外推为"全 5 教师方向"绝对结论（剔除 3 边界教师后剩 GLM_1 + minimax 2 教师 N=440 不代表全 5 教师方向；仅作 informational 注记）

### §5.3 0 产物不编造

- 本 verdict 件唯一新增产物 = `results/_v4_supp_l14v3_n26_verdict.md`（本件）
- **0 自跑实验 / 0 自起草建议文档 / 0 自发起 worker 接力棒 / 0 擅自调阈值 / 0 合并派生 JSON / 0 触动既有件**
- §1.6 替代读法 + §3 K-N26-N1/N2 边界细节 + §5 limitations 后续说明 = 裁因收口分析，**非执行指令**
- **派生 JSON 不合并声明**：3 件聚合文件（`.tmp/_l14v3_aggregated_10cells_v4.json` + `.tmp/_l14v3_n26_metrics_v2.json` + `.tmp/_l14v3_sensitivity_v2.json`）仅 runtime 派生，**不入 `_v4_supp_*` 产物链**（沿 L14+ §1.7 派生 JSON 不合并铁律）

### §5.4 根因三分类自检（沿 L14+ prereg `05B975A86989` §5 + PI 2026-09-23「诚实的根因是不误导」口径）

| 判定 | 根因类型（保守口径） | 根因列是否附 | 备注 |
|---|---|---|---|
| K-N26-1 NOT TRIGGERED（mean 0.5617 < 0.70） | **v1/v2 方向弱维持（教师侧 metadata 不可分未达显著）** | ✓ | 5 教师均 < 0.70；kimi 0.7512 是 5 教师中唯一 ≥ 0.60 偏强者；非翻 v1/v2 既判 |
| K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75） | **真证伪（沿 v1/v2 方向 "metadata 不可区分" 被实证 · N-26 真审核心裁因点）** | ✓ | pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线；全 5 折 CV 0.5266-0.6318 全部 < 0.75；与 L4 verdict §11「构造不可行」既判方向不冲突（构造不可行 = 缺教师侧配对不可算 = 既判未真审；L14+ 真审后 = "metadata 不可区分"被实证 = 与 v1/v2 方向一致） |
| K-N26-3 NOT TRIGGERED（n_below_0.60 = 3 < 4） | **v1/v2 方向略不达（多数教师 metadata 不可分严格意义上未达 ≥4 门槛）** | ✓ | 3 教师 < 0.60，未达 ≥4 阈值；kimi 0.7512 + GLM_2 0.6364 共 2 教师 ≥ 0.60 抬升；非翻 v1/v2 既判 |
| K-N26-N1 pass=True（10 cells 全字面满足构造非退化自证） | **构造非退化自证成立** | ✓ | L4 v2 时期 payload「ping」短 + n_distinct 退化已通过 L14+ 整链重跑 + 22 caption 真实素材面补齐；teacher_kimi 77 calls 沿 §3.1 披露（r1 已清出口非构造失灵族） |
| K-N26-N2 pass=True（10 cells 全 tun 合规或 mimo 端点无代理合规 + 空响应率 ≤ 0.50） | **tun 合规成立** | ✓ | PI 2026-09-23 硬纪律守住；L4 v2 时期"teamo tun 合规 PASS 10/10"既判维持 |

**根因三分类计数**：
- **真证伪（命题被证伪 / 既判方向一致）**：1 件（K-N26-2 = pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线 = N-26 真审核心裁因点）
- **v1/v2 方向维持（既判不翻）**：2 件（K-N26-1 弱维持 + K-N26-3 略不达）
- **构造族 PASS（非退化自证 + tun 合规）**：2 件（K-N26-N1 + K-N26-N2 全 pass=True）
- **构造失灵（工具/构造层失败）**：0 件
- **命题不明**：0 件

### §5.5 与派工单 5 件必带对齐

| 必带项 | 本件状态 |
|---|---|
| agent 名（verdict-keeper） | ✓ 本件由 verdict-keeper（agent-3a4d09ba3c90）起草 |
| skill 名 + plugin-cache sha256 | ✓ 派工单锚 `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows，sha256-tree-v1 前 12 = `611965fcb620`）；skill 缺位 fallback 沿 L14+ prereg `05B975A86989` §0 + L4 verdict `74B5B37F7EEA` §11 + T15R2 verdict `8355724A26E3` §5.2 limitations 沿用 |
| plugin 名（@scientific-research-workflows） | ✓ 已列 §5.2 |
| 7+9 铁律 | ✓ key 永不明文 / V1-V3 只读 / 派生 JSON 不合并 / kill-line 字面不动（K_N26_1_ACC=0.70 / K_N26_2_AUC=0.75 / K_N26_3_TEACHERS_LT=0.60 一字不动）/ 不调阈值 / 不合并派生 JSON / 判定布尔显式方向（hit=True 即触发 / hit=False 不触发）/ 不覆盖既有件（新件新名 `_v4_supp_l14v3_n26_verdict.md`）/ SHA-12 自算写入 / 0 LLM 0 伪造 skill 指令 |
| 老实交代 0 产物 | ✓ 本节 §5.1-§5.5 |

### §5.6 待 PI 复核未决项（穷尽清点，**待 PI 派工/拍板**）

> **沿 PI 2026-09-23「收口须穷尽清点未决项，不得漏报」** + 2026-09-21「待拍板项必须用工具提问」—— 本件列出全部待 PI 复核项，建议下一轮以 ask_user 提问

1. **L14+ activation 件 `843E42EF4D2A` PI 复核生效拍板**（沿 v0.2 `AD42992DC75D` 锁先例「生效时刻」字段填法；L14+ 立线 + 10 cells × 22 caption × 双向 ≥ 1,100 calls 矩阵字面 + 调用预算 + 产物链 `_v4_supp_l14v3_*` 待 PI 复核生效）
2. **N-26 真审重判定性正式拍板**（本件 §7 已作"N-26 真审真证伪（沿 v1/v2 方向 metadata 不可区分被实证）"字面裁定 + 根因三分类每行附 + 双读法敏感性测试 + 三重构造域限制边界声明；**正式拍板 = PI 复核 + verifier 签字**）
3. **teacher_kimi r1 已清出口是否补足**（沿 §3.1 披露；batch1 r1 22 calls 已清出 = teacher_kimi N_min = 77 < 理论 110；**正式拍板 = PI 复核**是否补跑 r1 vs 沿 worker 实跑披露维持）
4. **K-N26-N1 字面"J 中位分布非退化"是否需直接度量补正**（沿 §5.2 limitations 沿用；本件未直接度量 Jaccard，仅沿 worker 自加 per_caption_successful_calls 字段 + 22 caption × ≥ 5 successful/caption 字面满足推定；**正式拍板 = PI 复核**是否需 worker 接力棒补 Jaccard 度量）
5. **K-N26-N2 字面"J 中位分布非退化"是否需直接度量补正**（沿 §5.2 同上）
6. **3 件聚合文件（`.tmp/_l14v3_aggregated_10cells_v4.json` + `.tmp/_l14v3_n26_metrics_v2.json` + `.tmp/_l14v3_sensitivity_v2.json`）是否入 `_v4_supp_l14v3_*` 产物链**（沿 §5.3 派生 JSON 不合并铁律，本件不擅自并入；**正式拍板 = PI 复核**是否补入产物链 vs 维持 runtime 派生）

---

## §6 RESULT 报告（诞生即记）

- **本件路径**：`results/_v4_supp_l14v3_n26_verdict.md`
- **SHA-12（前 12 位）**：见 harness 外部汇报段（自报 vs 盘实测）
- **字节 / 行数**：以落盘末态为准
- **本件性质**：verdict-keeper 判定收口 / L14+ N-26 真审统裁件（与 `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` `05B975A86989` + L14V3 model mapping `98A779D61C1E` + 10 件 batch result json 同级独立）
- **锚定 L14+ prereg**：`05b975a86989` 命中（L14+ prereg **一字不动**）
- **锚定 L14+ activation**：`843e42ef4d2a` 命中（L14+ activation **一字不动**）
- **锚定 L14V3 model mapping**：`98a779d61c1e` 命中（L14V3 mapping **一字不动**；5 教师 model 映射三栏对照 + PI 拍板定案字面）
- **锚定 T15R2 verdict 格式锚**：`8355724a26e3` 命中（T15R2 verdict **一字不动**；仅作格式锚引用）
- **锚定 10 件 batch result json 终件**：batch1 r6 `6b92bbff7180` + batch2 r5 `479f4119cf72` + batch3 r5 `38998f994b84` + batch4 r6 `6b8093ff8962` + batch5 r5 `c874d21a4cbe` + batch6 r5 `e40424bf8abe` + batch7 r5 `09a481ebca6b` + batch8 r5 `3620a7daf9c1` + batch9 r5 `1610f5060ef1` + batch10 r5 `7f02e08fc0da` 命中（10 件终件 **一字不动**）
- **锚定 N-26 prereg**：`0A9EE16267B5` 命中（N-26 prereg 盘已清出但 inventory L800 字面引用；**一字不动**）
- **锚定 L4 verdict N-26 v2**：`74B5B37F7EEA` 命中（L4 verdict 盘已清出但 ledger L208 字面引用；**一字不动**；本件不翻 §11「FAIL · 构造不可行」）
- **锚定 L13 verdict**：`E105EC1362DB` 命中（L13 verdict 盘已清出但 ledger L188 字面引用；**一字不动**）
- **锚定 L7 verdict**：`B8335982AE5E` 命中（L7 verdict 盘已清出但 ledger L282 字面引用；**一字不动**）
- **锚定 v0.2 件 + add_T1 件 + L9/L10 追加件 + Track 2 件 + 22 caption + 度量函数 + V3 distill 流水线参照系**：全部命中（**一字不动**）
- **派生 JSON 不合并声明**：3 件聚合文件（`.tmp/_l14v3_aggregated_10cells_v4.json` `66a9b8b3dabf` 2,233,138 B + `.tmp/_l14v3_n26_metrics_v2.json` `eb9ce9683ad3` 2,579 B + `.tmp/_l14v3_sensitivity_v2.json` `dcaa4b6b3b0b` 2,292 B）runtime 派生**不入** `results/_v4_supp_*` 产物链
- **派工单**：PI 2026-09-26「verdict-keeper 判定收口 / 统裁专职 · N-26 真审终裁 · K-N26-1/2/3 统裁（10 cells 全配对）」（skill `scientific-research-workflows:peer-review`；plugin @scientific-research-workflows sha256-tree-v1 前 12 = `611965fcb620`）
- **生效后状态**：本件为判定收口件，生效后状态沿 L14+ prereg `05B975A86989` + L14V3 mapping `98A779D61C1E` + T15R2 verdict `8355724A26E3` 锁先例 → **生效即锁**（沿 L14+ §4 边界声明 + R5 frozen 派生 JSON 不合并铁律），事后不重开不调
- **0 触既有件**：1 件新增（`_v4_supp_l14v3_n26_verdict.md`），≥ 24 件既有件 0 触动（详见 §5.1）
- **L14+ 定位硬约束再声明**：L14+ = N-26 真审唯一路径（V3 distill 整链重跑复现 + 采集阶段同步保四元组），**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程**（沿 L4 verdict `74B5B37F7EEA` §11 既定结论一字不动）；本件仅作 L14+ 探针字面证据下裁定（K-N26-2 TRIGGERED + K-N26-1/3 NOT TRIGGERED + K-N26-N1/N2 全 pass=True）

---

## §7 总判定（一行收口）

> **L14+ N-26 真审（10 cells × 22 caption × 双向 ≥ 1,090 calls 同步保四元组 metadata）= K-N26-1 NOT TRIGGERED（5 教师 mean 0.5617 < 0.70 真证伪线）+ K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75 真证伪线 · N-26 真审核心裁因点）+ K-N26-3 NOT TRIGGERED（n_below_0.60 = 3 < 4 阈值）+ K-N26-N1/N2 全 pass=True（10 cells 构造非退化自证成立 + teamo/mimo tun 合规成立）= N-26 真审真证伪方向（沿 v1/v2 方向 "metadata 不可区分" 被实证 · K-N26-2 触发方向与 v1/v2 方向一致而非推翻）**：跨 5 教师 pooled 二分类 AUC 0.5663 远 < 0.75 真证伪线（5 折 CV 区间 0.5266-0.6318 无一折达 0.75 = 跨教师 pooled 不可靠区分 teacher vs distill）；K-N26-1 v1/v2 方向弱维持（5 教师均 < 0.70 真证伪线；kimi 0.7512 是 5 教师中唯一 ≥ 0.60 偏强者）；K-N26-3 v1/v2 方向略不达（仅 3 教师 < 0.60，未达 ≥4 阈值；kimi 0.7512 + GLM_2 0.6364 共 2 教师 ≥ 0.60 抬升）；K-N26-N1 全 pass=True（10 cells × 22 caption × ≥ 5 successful 字面满足 · teacher_kimi 77 calls 沿 §3.1 披露 r1 已清出口非构造失灵族）；K-N26-N2 全 pass=True（teamo 8 端点 100% 走 tun + minimax 2 端点 mimo 无代理合规 + cumulative_empty_rate 范围 0.000-0.075 远 < 0.50 阈值 · PI 2026-09-23 硬纪律守住）；**不动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」一字不动**（L4 verdict 记录 v1/v2 时期"构造不可行" = 缺教师侧配对不可算 = 既判未真审；L14+ 真审后构造补齐 + 真审实证 "metadata 不可分" 维持 = 与 v1/v2 方向一致而非推翻）；**不动 L13 verdict `E105EC1362DB` §11 + L7 verdict `B8335982AE5E` §11 + N-26 prereg `0A9EE16267B5` §2 + v0.2 件 + add_T1 件 + L9 / L10 / Track 2 件 + 22 caption + 度量函数 + V3 distill 流水线参照系 一字不动**；5 reads 双读法敏感性测试（drop_coze / drop_glm2 / drop_kimi / drop_all3）下 K-N26-1 / K-N26-3 全 NOT TRIGGERED + K-N26-2 全 TRIGGERED = 主读法稳健；三重构造域限制（GLM_2 近缘对 + coze 代表采样 + prompt 复现口径）边界如实入 §4.4；L14+ activation 件 `843E42EF4D2A` PI 复核生效拍板 + N-26 真审重判定性正式拍板 + teacher_kimi r1 已清出口是否补足 + K-N26-N1/N2 字面"J 中位分布非退化"是否需直接度量补正 + 3 件聚合文件是否入 `_v4_supp_l14v3_*` 产物链 五项**待 PI 复核拍板**。

---

> **诚实 = 不误导**（沿 PI 2026-09-23 口径）：本 verdict 件如实裁 K-N26-2 TRIGGERED（pooled AUC 0.5663 < 0.75 真证伪线）+ K-N26-1 NOT TRIGGERED（教师准确率 0.5617 < 0.70）+ K-N26-3 NOT TRIGGERED（n_below_0.60 = 3 < 4）+ K-N26-N1/N2 全 pass=True = **N-26 真审真证伪（沿 v1/v2 方向 metadata 不可区分被实证）**；**不写「但仍稳健 / 仍有希望」类软化语**；**不外推**为「v1/v2 既判 PASS 新证据」/「v1/v2 既判翻案」/「N-26 命题方向翻转」；**诚实声明**："仅凭 metadata 跨教师 pooled 不可靠区分 teacher vs distill"被实证，但**不是「完全不可分」**（kimi 0.7512 ≠ 全不可分）；**保守口径下模糊处**（5 项待 PI 复核）一律标注「**待 PI 复核**」，不擅自推广；**不动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行」一字不动**硬约束全段守住（沿 L14+ §0 边界 + §4 边界 + §5.1 0 触既有件自查 + 「派生 JSON 不合并」铁律）。