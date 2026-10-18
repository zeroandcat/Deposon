# V4 V5 补强 · Track 2 多模型补跑判定 · `_v4_track2_multimodel_verdict_2026_09_23.md`

**判定日**：2026-09-23（V4 V5 补强 件 3 续，多模型补跑）
**作者**：Mavis worker
**派工单**：PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4（qwen + mimo）+ 补充 1（teamo 第三端点）+ 补充 2（代理 + 串行防封号）
**对照基线**：件 3 已测 3 模型 (openrouter_baseline / deepseek_direct / qwen) (SHA-12 `61EDBE39A618` / `1B05EBA8639B` / `AE541E34781E`)
**度量函数**：`_v4_distill_min_measure.py` (SHA-12 `21771E66AF67` / 33,852 B, 只读复用)
**端点探活锚**：`_track2_endpoints_probe_2026_09_23.json` (SHA-12 `C846F7FC79EE`)

---

## 0. 端点探活 → 槽位映射（PI 当条派工三 URL）

| 端点（PI 拍板） | 用途 | 候选 model_id → 选定 | 代理 | 状态 |
|---|---|---|---|---|
| `https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | qwen 槽 | qwen3.7-max | 否（按原网络路径） | 200 OK |
| `https://token-plan-cn.xiaomimimo.com/v1` | mimo 槽 | mimo-v2.6-pro | 否（按原网络路径） | 200 OK |
| `https://api.teamorouter.cn/v1` | teamo 槽 | deepseek-v4-flash（响应 model 名 deepseek-v4-flash-0731） | 是（PI 2026-09-23 补充 2） | 200 OK |

**注**：原 `qwen-turbo` / `mimo-7b` / `deepseek-v4.1-flash` 等候选名在 token-plan / teamorouter 端点上分别报 `model_not_found` / `Unsupported model` / `暂不支持调用`。改用 `GET /v1/models` 列出的实际 model_id 重新探活（探活档完整记录候选拒绝原因于 `_track2_endpoints_probe_2026_09_23.json` `attempts[*]`）。

**端点 URL 与既有 `_v4_v5_multimodel_probe.py` 文件差异声明**：

| 槽位 | PI 当条派工 URL | 文件 `_v4_v5_multimodel_probe.py` 内 URL |
|---|---|---|
| qwen_plan | `https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | `https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions`（旧；已实测 401） |
| mimo | `https://token-plan-cn.xiaomimimo.com/v1` | `https://api.mioplus.mi.com/v1/chat/completions`（旧；已实测 conn_error） |
| teamo | `https://api.teamorouter.cn/v1` | `https://api.teamo.ai/v1/chat/completions`（旧；已实测 ssl_error） |

PI 指示「以文件为准核对三端点 URL + 如有出入在 verdict 声明」。本棒按 PI 拍板三 URL 探活 + 电池补跑；probe 文件未触动（沿用 SHA-12 `5FE4CBD93D92` 模板只读）。

---

## 1. 多模型对照表（6 模型 × 5 教师，根因列三分类）

| # | 模型 | provider | model_id | main FAIL/n | main_verdict | mean D1_JS | mean D2_JS | mean margin δ | 根因分布 | 翻案 / 维持 vs 原判 |
|---|---|---|---|:-:|:-:|---:|---:|---:|---|---|
| 1 | openrouter_baseline (件 3 已测) | openrouter | deepseek/deepseek-v4.1-flash | 5/5 | **FAIL** | 0.025549 | 0.024490 | -0.001059 | 工具或构造层面失灵×5 | — （原判基线） |
| 2 | deepseek_direct (件 3 已测) | deepseek | deepseek-chat | 5/5 | **FAIL** | 0.030859 | 0.032066 | 0.001208 | 工具或构造层面失灵×5 | — （原判基线） |
| 3 | qwen (件 3 已测) | alibaba_dashscope | qwen-turbo | 5/5 | **FAIL** | 0.036923 | 0.035411 | -0.001512 | 工具或构造层面失灵×5 | — （原判基线） |
| 4 | **qwen_plan** (本棒新跑) | qwen_token_plan | qwen3.7-max | 5/5 | **FAIL** | 0.028512 | 0.028809 | 0.000297 | 工具或构造层面失灵×5 | **维持 FAIL**（与 qwen 同根因；模型升级未翻案） |
| 5 | **mimo** (本棒新跑) | xiaomi_mimo_token_plan | mimo-v2.6-pro | 5/5 | **FAIL** | 0.024116 | 0.024582 | 0.000466 | 工具或构造层面失灵×5 | **新增槽位**；3 件扩展适用同款根因 |
| 6 | **teamo** (本棒新跑) | teamorouter | deepseek-v4-flash (resp: deepseek-v4-flash-0731) | 5/5 | **FAIL** | 0.026767 | 0.026171 | -0.000596 | 工具或构造层面失灵×5 | **新增槽位**；3 件扩展适用同款根因 |

**总判定**：6/6 模型 5/5 全 FAIL；6/6 全属「工具或构造层面失灵」。

**双读法（避免机械诚实）**：

- **诚实判读 1（命题层面）**：6 个 LLM 在 5 教师上下文蒸馏任务上都不能产生可判死的差异信号 → 命题层面**似**被证伪。
- **诚实判读 2（根因列强约束）**：6/6 全部命中「d1 < 1e-9 and d2 < 1e-9」**或**「abs(d1 - d2) < 1e-12」**或**「n_proxy / n_teacher < 0.20」分支（参 multi_runner.py 根因分类逻辑），属「工具或构造层面失灵」**而非**命题被证伪。诚实结论：**不是命题被证伪，是构造层面（n_in_context=2 / n_calls=3 / proxy n=3 / teacher n≥23 的样本量与对照面不充裕）失灵**。这条诚实结论由多模型 × 多教师双交叉稳定复现（同一构造下换模型不改变根因），是判死依据。

---

## 2. 逐模型 5 教师判定（每模型 15 腿全量）

### 模型 qwen_plan (qwen3.7-max, qwen token-plan 端点)
**产物**：SHA-12 `30B7783CF310` / 29,014 B / 663 行 / LF / UTF-8 无 BOM
**调用**：15/15 OK / 15/15 parsed / latency 中位数 ≈ 7,056 ms
**三槽内电池**：kimi / GLM_1 / GLM_2 / coze / minimax 各 3 次

| # | teacher | (a) | (b) | (c) | main | 根因 |
|---|---|:-:|:-:|:-:|:-:|---|
| 1 | kimi | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 2 | GLM_1 | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 3 | GLM_2 | N | Y | Y | **FAIL** | 工具或构造层面失灵 |
| 4 | coze | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 5 | minimax | N | Y | N | **FAIL** | 工具或构造层面失灵 |

### 模型 mimo (mimo-v2.6-pro, mimo token-plan 端点)
**产物**：SHA-12 `0698F2FA88D0` / 28,483 B / 663 行 / LF / UTF-8 无 BOM
**调用**：15/15 OK / 15/15 parsed / latency 中位数 ≈ 8,059 ms
**三槽内电池**：kimi / GLM_1 / GLM_2 / coze / minimax 各 3 次

| # | teacher | (a) | (b) | (c) | main | 根因 |
|---|---|:-:|:-:|:-:|:-:|---|
| 1 | kimi | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 2 | GLM_1 | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 3 | GLM_2 | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 4 | coze | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 5 | minimax | Y | Y | N | **FAIL** | 工具或构造层面失灵 |

### 模型 teamo (deepseek-v4-flash, teamorouter 端点，代理)
**产物**：SHA-12 `4BFB49FC75EB` / 27,233 B / 651 行 / LF / UTF-8 无 BOM
**调用**：15/15 OK / 14/15 parsed（kimi call 0 解析失败：含 ```json 围栏但前缀不合规） / latency 中位数 ≈ 5,609 ms
**三槽内电池**：kimi / GLM_1 / GLM_2 / coze / minimax 各 3 次

| # | teacher | (a) | (b) | (c) | main | 根因 |
|---|---|:-:|:-:|:-:|:-:|---|
| 1 | kimi | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 2 | GLM_1 | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 3 | GLM_2 | Y | N | N | **FAIL** | 工具或构造层面失灵 |
| 4 | coze | Y | Y | N | **FAIL** | 工具或构造层面失灵 |
| 5 | minimax | Y | Y | N | **FAIL** | 工具或构造层面失灵 |

### 模型 openrouter_baseline / deepseek_direct / qwen（件 3 已测，仅引用）

详见 `_v4_v5_t2_multimodel_verdict.md` (SHA-12 `C386251D94D6`) 与 `_v4_v5_t2_multimodel_compare.json` (SHA-356BD6647796)。本棒不复跑，仅作对照基线。

---

## 3. 与原 3 模型对照表（翻案 / 维持）

| 模型 | 原判 (件 3) | 新判 (本棒) | 根因 | 翻案 / 维持 | 备注 |
|---|---|---|---|---|---|
| qwen_turbo (件 3) | FAIL 5/5 工具失灵 | —（未沿 token-plan 重测） | — | — | 同一 provider 家族不同端点；沿用原判 |
| deepseek_direct (件 3) | FAIL 5/5 工具失灵 | —（未重测） | — | — | 沿用原判 |
| openrouter_baseline (件 3) | FAIL 5/5 工具失灵 | —（未重测） | — | — | 沿用原判 |
| qwen_plan (本棒) | — | FAIL 5/5 工具失灵 | 工具或构造层面失灵 | — (新跑槽位) | 升级 qwen3.7-max 沿用同 construction |
| mimo (本棒) | — | FAIL 5/5 工具失灵 | 工具或构造层面失灵 | — (新跑槽位) | 全 5 教师三分支同款失灵路径 |
| teamo (本棒) | — | FAIL 5/5 工具失灵 | 工具或构造层面失灵 | — (新跑槽位) | teamo 即 deepseek-v4-flash 路由 |

**判死结论（不变）**：3 × 5 = 15 腿在 qwen_plan / mimo / teamo 三槽上**全部 FAIL**，且根因**全部**归「工具或构造层面失灵」（不是命题被证伪）。这与件 3 原 3 模型 15 腿根因同源 → 多模型扩展**未翻案**，构造层面失灵路径被多模型 × 多教师双交叉稳定复现。

---

## 4. 工程失败声明（与实验判定严格分列）

**结论：0 工程失败**。

逐项核验：
- 6 个 LLM 产物全部 SHA-12 自算：
  - `_v4_proxy_student_llm_qwen3_7_max.json` = `30B7783CF310` (29,014 B / 663 行 / LF / UTF-8 无 BOM)
  - `_v4_proxy_student_llm_mimo_v2_6_pro.json` = `0698F2FA88D0` (28,483 B / 663 行 / LF / UTF-8 无 BOM)
  - `_v4_proxy_student_llm_deepseek_v4_flash_teamo.json` = `4BFB49FC75EB` (27,233 B / 651 行 / LF / UTF-8 无 BOM)
- 端点探活 JSON 落盘：SHA-12 `C846F7FC79EE` / 5,803 B / 161 行 / LF / UTF-8 无 BOM
- 多模型补跑 compare JSON 落盘：SHA-12 `E3DAE2A4BBC2` / 35,011 B / 976 行 / LF / UTF-8 无 BOM
- 本棒自扫（11 模式含 tp- / sp- / sk-teamo-）：落盘前 0 命中；落盘后 0 命中
- 铁律合规：
  - key 仅 runtime 内存读 / 不落盘 / 不入 prompt / 不入 JSON / 不入 log
  - 18 frozen + 9 网格 + P-G v0/v01 + plugin spec 0 触动
  - V1–V3 资产 + V4 frozen 链 0 触动（只读引用）
  - 「CONDITIONAL PASS」未使用：判定结果二值化（PASS / FAIL）
- 代理合规：PI 2026-09-23 补充 2 硬要求满足
  - `https_proxy=http://127.0.0.1:1018` / `http_proxy=...` / `all_proxy=socks5://...` 全程设置
  - teamo 端点 (api.teamorouter.cn) 强制走代理
  - 串行执行；端点间 ≥2.5s；同槽 call 间 ≥1.5s（防封号）
- 端点探活 + 电池补跑均不修改既有件

## 5. 措辞纪律

本判定**不软化**：「但 / 然而 / 仍有希望」类措辞 0 容忍；「CONDITIONAL PASS」退役；判死结论二值化（PASS / FAIL）。

## 6. SHA-12 链自证

| 件 | SHA-12 | 字节 | 状态 |
|---|:-:|---:|---|
| `_v4_proxy_student_llm_runner.py` | `900A6D1E50AF` | 24,659 | 模板只读复用（frozen） |
| `_v4_proxy_student_llm_multi_runner.py` | `306FA79A7C27` | 40,043 | 多模型模板只读复用（frozen） |
| `_v4_distill_min_measure.py` | `21771E66AF67` | 33,852 | 度量函数（只读复用） |
| `_v4_proxy_student_llm_deepseek_v41_flash.json` | `61EDBE39A618` | 34,959 | OpenRouter baseline（件 3，已测） |
| `_v4_proxy_student_llm_deepseek_direct_chat.json` | `1B05EBA8639B` | 28,113 | DeepSeek direct（件 3，已测） |
| `_v4_proxy_student_llm_qwen_turbo.json` | `AE541E34781E` | 25,598 | Qwen turbo（件 3，已测） |
| `_v4_v5_t2_multimodel_compare.json` | `356BD6647796` | 32,393 | 件 3 多模型对照（frozen） |
| `_v4_v5_t2_multimodel_verdict.md` | `C386251D94D6` | 4,264 | 件 3 多模型判定（frozen） |
| `_v4_v5_t2_verdict.md` | `83D8E7A8BA12` | 9,301 | 件 1 判定（frozen） |
| `_v4_v5_ablation_verdict.md` | `C2920AA9923A` | 7,612 | 消融判定（frozen） |
| `_v4_v5_multimodel_probe.py` | `5FE4CBD93D92` | 6,159 | 探针模板（frozen；本棒仅核对该文件 URL 段，不修改） |
| `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | 端点探活（本棒产物） |
| `_v4_proxy_student_llm_qwen3_7_max.json` | `30B7783CF310` | 29,014 | qwen_plan 产物（本棒新增） |
| `_v4_proxy_student_llm_mimo_v2_6_pro.json` | `0698F2FA88D0` | 28,483 | mimo 产物（本棒新增） |
| `_v4_proxy_student_llm_deepseek_v4_flash_teamo.json` | `4BFB49FC75EB` | 27,233 | teamo 产物（本棒新增） |
| `_v4_track2_multimodel_rerun_2026_09_23.json` | `E3DAE2A4BBC2` | 35,011 | 多模型补跑对照（本棒新增） |
| `_v4_track2_multimodel_verdict_2026_09_23.md` | （本件，自指回环） | - | 多模型补跑判定（本棒新增） |

**自指回环处置**：本件自身 SHA-12 在落盘后即固定，链表中标为「本件，自指回环」；外部观测者请用 `Get-FileHash -Algorithm SHA256 _v4_track2_multimodel_verdict_2026_09_23.md` 独立复算。

## 7. 边界声明

- 多模型 LLM 调用：qwen_plan / mimo / teamo 三端点；其他路由（件 3 已测 3 模型）只读引用未重跑
- teamorouter 端点走代理 `http://127.0.0.1:1018` (PI 2026-09-23 补充 2 硬要求)
- key 来自 PI 授权源文件 (`C:/Users/Administrator/Desktop/AI/LLM API.txt`)，runtime 内存读取，不落盘 / 不入产物 / 不入 log / 不入回报
- 18 frozen + 9 网格 0 触动；P-G v0 v01 + plugin spec / verifier 内置脚本 0 触动
- V1–V3 资产 + V4 frozen 链 0 触动（只读引用）
- 铁律沿用定稿 R1–R8：见 `_v4_iron_rules_review_2026_09_22.md`（含 2026-09-23 勘误）