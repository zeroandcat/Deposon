# V4 Track 2 qwen_plan 401 重试棒 · 登记件

**件名**：`results/_v5_track2_qwen_retry_2026_09_29.md`
**登记日**：2026-09-29（上午）
**执行棒**：worker（Mavis）
**PI 处置来源**：ask_0b4c1577f0d727e239e55095 q2 ——「最新文件包含了 URL 与 key」⇒ 401 重试须用**最新文件**中的 URL 与 key
**承接问项**：Q-H1-1（X-25 / Z-14）—— Track 2 qwen_plan 401 处置（换 key / 换 model / 换 endpoint 三选一）

---

## 0. 一句话结论

**四态判定 = ① 成功（401 解除）**。用**最新文件**（`Desktop/AI/LLM API.txt`，mtime 2026-09-23 15:00:05）中的 URL + key，对 Track 2 qwen_plan 目标（token-plan 端点 + `qwen3.7-max`）最小验证调用 **HTTP 200**，`response.model = qwen3.7-max`（**无降级**）。

⚠️ **但根因不是「key 失效」**——见 §4「诚实的根因」：原 401 与本次 200 **不是同一个 URL / model / key 文件版本**。本件**不构成**对原 401 那次调用的翻案。

---

## 1. 所选文件实况（PI 处置第一问）

### 1.1 候选排查（`Desktop/AI/` 全目录，仅 3 件；0 明文）

| mtime (local) | size | SHA-12 | 模式计数 | 主机名 | 判定 |
|---|---:|---|---|---|---|
| 2026-09-24 11:56:49 | 105 B | `E5304225B1E6` | urls=1, sk/ark 类 secret=**0** | `mcp.sellersprite.com` | **非 key 文件**（MCP 端点，无 key） |
| **2026-09-23 15:00:05** | **947 B** | **`D35EE9ECC881`** | urls=8, sk/ark 类 secret=5 + opaque=2 | 含 `token-plan.maas.qianwenaiapi.com` 等 | **★ 本棒所选**（唯一含 URL+key 者） |
| 2026-08-25 13:45:50 | 662 B | `DD75D7BC9AD8` | urls=0, secret=0 | — | 非文本（快捷方式） |

**如实登记**：`Desktop/AI/` 下**唯一**同时含 URL 与 key 的文件即 `LLM API.txt`。目录内**不存在**比它更新的 key 文件——09-24 那件更新但**无 key**（卖家精灵 MCP，非 LLM 凭据）。故 PI 所谓「最新文件」在本机落为该 09-23 件。

### 1.2 所选文件元数据

| 项 | 值 |
|---|---|
| 路径 | `C:\Users\Administrator\Desktop\AI\LLM API.txt`（**workspace 外，PI 授权只读**） |
| 大小 | 947 B |
| mtime (local) | `2026-09-23T15:00:05` |
| mtime (UTC) | `2026-09-23T07:00:05+00:00` |
| CreationTime | `2026-09-01T15:27:29` |
| SHA-12 | **`D35EE9ECC881`** |
| 总行数 | 30 |

### 1.3 URL ↔ Q-H1-2「三 URL 200 OK」一致性核对

Q-H1-2 待裁的「两套 URL 字面并存」，本棒对所选文件内 URL **逐条比对**（**实测一致**）：

| 槽位 | 所选文件内 URL（host） | Q-H1-2 / Track 2 棒落定的「三 URL 200 OK」 | 一致性 |
|---|---|---|---|
| qwen_plan | `token-plan.maas.qianwenaiapi.com` | `https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | **✓ 逐字一致** |
| mimo | `token-plan-cn.xiaomimimo.com` | `https://token-plan-cn.xiaomimimo.com/v1` | **✓ 逐字一致** |
| teamo | `api.teamorouter.cn` | `https://api.teamorouter.cn/v1` | **✓ 逐字一致** |

**结论（Q-H1-2 侧证，不代 PI 裁）**：所选最新文件内的 URL **与 Track 2 棒「三 URL 200 OK」那套完全一致**；不一致的是 V3 补实验件所用的**旧 URL**（`dashscope.aliyuncs.com` / `api.mioplus.mi.com` / `api.teamo.ai`）。⇒ 对 Q-H1-2 而言，**「PI 派工/实测三 URL」这一套**有最新文件侧的字面支持。

### 1.4 key 行位与前缀类（**0 明文**，仅类别 + 长度 + 行号）

| 行（1-based） | 内容类 | 备注 |
|---|---|---|
| L22 | URL | `token-plan.maas.qianwenaiapi.com` |
| **L23** | **SECRET[opaque-token] len=116** | **本棒所用 qwen key**（**非** `sk-`/`ark-` 厂商前缀样式） |
| L14 / L15 | URL / SECRET[sk 类] len=57 | teamo 槽（teamo/openrouter ⇒ 走 tun，本棒**未调用**） |
| L26 / L27 | URL / SECRET[opaque-token] len=51 | mimo 槽（本棒未调用） |
| L3 / L7 | SECRET[ark 类] len=46 | 火山 ark 槽（本棒未调用） |
| L10 / L11 / L18 / L19 | URL / SECRET[sk 类] | openrouter / deepseek 槽（本棒未调用） |

**关键结构观察**：qwen key 是**无厂商前缀的 116 字符 opaque token**，与文件内其余 5 个 `sk-`/`ark-` 前缀 key **形态不同** ⇒ 该行是 09-23 15:00 修订时**新写入**的条目（与 §4 根因互相印证）。

---

## 2. 401 重试执行记录（四态）

### 2.1 调用配置（沿既有 Track 2 口径，0 擅改）

| 项 | 值 | 依据 |
|---|---|---|
| 端点 | `https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | Track 2 棒（PI 2026-09-23 三 URL） |
| model | `qwen3.7-max` | Track 2 棒探针选定 |
| key | **L23（1-based）**，runtime 内存读 | 本棒实测行位 |
| 代理 | **直连** | qwen_plan **非** teamo/openrouter 系 ⇒ **tun 纪律本棒未触发**（如实登记，非疏漏） |
| 串行 / 间隔 | 串行，≥ 2.0 s | PI 防封号 |
| 预算 | 计划 2 次 / **实跑 2 次** | 节省原则 |

### 2.2 逐次调用实测

| # | 调用 | HTTP | 延迟 | 关键读数 |
|---|---|---:|---:|---|
| 1 | `GET /v1/models`（认证面诊断） | **405** | 405.9 ms | Method Not Allowed（该端点不接受 GET 列举）⇒ **诊断面未取得**，非 401 |
| 2 | `POST /chat/completions` `model=qwen3.7-max` | **200** | 1,866.7 ms | `object=chat.completion`；`finish_reason=stop`；`response.model = qwen3.7-max`；`completion_chars=2`（"OK"）；usage: prompt 17 / completion 79（reasoning 76）/ total 96 |

### 2.3 四态判定

> **① 成功（返回正常响应 ⇒ 401 解除）** —— `http_status=200` 且 `completion_chars>0`。

四态设计说明：单看 chat 的 401 无法区分「key 失效」与「model 端点 mismatch」。故先以**同一 key** 打认证面（`/v1/models`）——本次该路由 405，诊断面未取得，但 chat 200 **直接给出终态**，四态收敛于 ①。**未触发**②（key 失效实锤）、③（model mismatch）、④（网络/端点阻）。

### 2.4 防降级核对

| 项 | 值 |
|---|---|
| 请求 model | `qwen3.7-max` |
| **响应 `response.model`** | **`qwen3.7-max`** |
| 是否降级 | **否（`downgraded=false`）** |

⇒ 端点**按请求 SKU 返答**，未回落 `qwen-turbo` / `qwen3.7-plus` 等其它名。（对照：teamo 槽历史上曾出现 resp 名带后缀 `-0731` 的形态，qwen 槽本次无此现象。）

---

## 3. 产物

| 产物 | 路径 | 说明 |
|---|---|---|
| 重试执行器 | `results/_v5_track2_qwen_retry_executor_20260929.py` | 本棒新建；2 次调用，0 明文闸内置 |
| 结果 JSON | `results/_v5_track2_qwen_retry_2026_09_29.json` | 2,735 B / SHA-12 **`6acafe021aaf`**（**以盘上实测为准**）；落盘前经 `scrub()` 过闸 |
| 本登记件 | `results/_v5_track2_qwen_retry_2026_09_29.md` | SHA-12 见收口回报（自指，落盘后算） |

**既有件 0 触动**：本棒**未修改/未移动**任何既有件；仅新增上述 3 件 + `.tmp/` 下 2 件勘察脚本（`scan` 用，可弃）。

---

## 4. 诚实的根因（不误导优先）

**不能把「今天 200」直接读成「key 换好了」或「PI 处置被证实」。** 时间线对不齐：

| 时点 | 事件 | 端点 / model / key 来源 |
|---|---|---|
| 09-23 11:30 左右 | key 文件第 1 次修订 | — |
| 09-23 14:20:36 | `_v3_construct_degradation_diag_2026_09_23.json` 落盘 | **dashscope** 旧 URL + `qwen-turbo` + key_index=17（**仍 401**） |
| 09-23 14:27:09 | `_v3_supplement_verdict_2026_09_23.md` 记「401 仍在」 | 同上 |
| **09-23 15:00:05** | **key 文件第 2 次修订（本棒所用版本的 mtime）** | qwen key 被写成 L23 的 **116 字符 opaque token** |
| 09-23 15:26:47 | `_v4_track2_multimodel_rerun_2026_09_23.json` | **token-plan** URL + `qwen3.7-max`，**15/15 OK** |
| **09-29 11:10** | **本棒重试** | 同上 URL/model + **L23 key** ⇒ **200** |

**根因判定（三项均据实测，非编造）**：

1. **原 401 的靶子与本棒验证的靶子不是同一个**。原 401 打的是 **旧 dashscope URL + `qwen-turbo`**（见 `_v3_supplement_verdict_2026_09_23.md:138`）；本棒打的是 **token-plan URL + `qwen3.7-max`**。⇒「401 解除」**只对 token-plan 槽成立**，**对原 401 那次 dashscope/qwen-turbo 调用未被本棒复测、也未被翻案**。
2. **猜测 B（key 失效）不成立于当前 key 文件版本**。同一份 `LLM API.txt`（SHA-12 `D35EE9ECC881`）的 L23 key 今日实测 200 ⇒ 该版本 key **未失效**。但**旧修订版本（14:20 当时）的 key 是否失效，本棒无证据，不作结论**。
3. **猜测 C（model 端点 mismatch）已被反证**（就 token-plan 槽而言）：`qwen3.7-max` 被端点接受且 `response.model` 回同名 ⇒ 非 mismatch。历史上 `qwen-turbo` 在该端点报 `model_not_found`，**这正是原 401 配对错误（错 URL + 错 SKU）的可能来源之一**。

**⇒ 对 Q-H1-1「换 key / 换 model / 换 endpoint 三选一」的如实答复**：三选一**都不必做**——按 PI 指示改用**最新文件**的 URL + key 后，**Track 2 qwen_plan 目标直接 200**。真正起作用的是「**URL 与 key 成对取自同一最新版本**」，而非单独换 key / 换 model / 换 endpoint 之一。**原 401 的完整根因仍需一次针对 dashscope + `qwen-turbo` 的定向复测才能收口**——该复测**超出本棒授权范围**（本棒靶子为 Track 2 qwen_plan 目标），**本棒未执行、不代裁**。

---

## 5. 0 明文自查（铁律实证）

**纪律**：key 值**仅 runtime 内存读**（`load_key()` → 请求头 → `del`）；不落盘 / 不入 prompt / 不入 JSON / 不入 log / 不入 stdout / 不入本件。

| 检查面 | 方法 | 结果 |
|---|---|---|
| 结构勘察脚本 stdout | 仅输出「行号 + 类别 + 长度 + 主机名」 | **0 明文** |
| 执行器 stdout | `key` 从不 print；仅打印状态码/错误类/响应 model | **0 明文** |
| 结果 JSON | 落盘前经 `scrub()` 正则闸（厂商前缀串 + ≥60 字符 token） | **0 明文** |
| 本登记件 | 全文不含任何 key 值 | **0 明文** |

**字面自查**：对本件与结果 JSON 全文 grep 厂商 key 前缀（`sk`+`-` / `ark`+`-` 拼接式，**为让本件自身通过该 grep 而刻意断写**）与 60+ 字符连续 token ⇒ **0 命中**（见收口回报）。

> 登记面引用该文件路径时**须带「runtime 读、不落盘」限定**（沿用 Y-11 口径）。

---

## 6. 老实交代 / 剩余风险

1. **`/v1/models` 诊断面 405 未取得** ⇒ 本棒「key 有效 vs model mismatch」的**判别走的是 chat 200 正面证据**，非认证面分离证据。结论够用，但**分离式证据缺失**，如实登记。
2. **本棒 0 次调用 teamo / mimo 槽** ⇒ Q-H1-2 的 URL 一致性结论**仅为「所选文件字面 vs Track 2 棒落定值」的比对**，**未重新实测探活**。不冒充「三 URL 今日 200 OK」。
3. **原 401（dashscope + `qwen-turbo`）未定向复测** ⇒ 根因未收口，见 §4。
4. **n=1 单次验证**（节省原则，1–3 次区间取下限）⇒ 「稳定可用」未证；仅「**此刻可用**」成立。若 PI 要 n≥3 稳定性，可另派。
5. **未验**该 key 的额度/有效期边界（本次 usage 96 tokens 极小，**不足以推断额度充足**）。
6. **skill 未加载**：本棒按派工单字面执行（`no_llm` 类 skill 与本棒无涉；本棒即为「调 LLM」实验棒）。如实交代，未假称按 skill 执行。
7. **执行器 stdout 报的 JSON SHA-12（`60D4CBA4E5F0`）与盘上实测（`6acafe021aaf`）不一致，本件采信盘上值**。根因：执行器对**换行转换前**的 blob 取哈希，而 Windows 文本模式写入把 80 处 LF 转成 CRLF（+80 B：2,655→2,735）。**不掩盖该差异**；盘上文件本身 0 明文（复扫 0 命中，见 §5）。后续 executor 若需自报落盘哈希，应先 `newline='\n'` 或对**重读后的文件**取哈希。

---

**署名**：worker（Mavis）｜2026-09-29｜**如实登记，0 编造，0 明文**
