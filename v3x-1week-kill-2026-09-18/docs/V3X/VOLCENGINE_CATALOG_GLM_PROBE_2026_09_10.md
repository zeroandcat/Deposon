# 火山方舟 Coding Plan Catalog GLM 探活报告

- **任务 ID**: volc-catalog-glm-probe-20260910
- **时间**: 2026-09-10 18:00 (Asia/Shanghai)
- **运行者**: Mavis worker 子代理
- **触发原因**: user 2026-09-10 17:53 建议试 GLM-5.3 主线,17:58 选 C = 探活 catalog
- **结果文件**: `D:\私人资料\deposon-repo\results\deposon_volcengine_coding_plan_catalog_2026_09_10.json`

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan (ark.cn-beijing.volces.com) |
| Base URL | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| Endpoint | `GET /models`(只读,**0 LLM calls**) |
| Auth | `Bearer ark-de0b484e-0...` (从 `LLM API.txt` 读出,`os.environ['ARK_CODING_PLAN_KEY']` 内存使用,**不落盘**) |
| Proxy | **未设**(已 strip `HTTP_PROXY` / `HTTPS_PROXY` / `http_proxy` / `https_proxy` / `NO_PROXY` / `ALL_PROXY`) |
| HTTP 状态 | **200 OK** |
| total_models | **130** |
| response 形态 | OpenAI-compatible `{object: "list", data: [...]}` |
| sample entry 字段 | `id, name, version, status, features, created, domain, object` + (部分有) `token_limits, modalities, task_type` |

---

## §2 130 model 提供方分布

| Provider | 数量 | 占比 | 备注 |
|---|---:|---:|---|
| Doubao (字节豆包) | 100 | 76.9% | 主力,含 lite / pro / seed / seedance / seedream 全系 |
| DeepSeek | 13 | 10.0% | 含 v3 / v4 / flash / pro 多版本 |
| 其他 | 6 | 4.6% | 不含 glm/qwen/deepseek/kimi 前缀 |
| Qwen (通义千问) | 5 | 3.8% | |
| GLM / Z.ai / 智谱 | **3** | 2.3% | **本次探活目标** |
| Kimi / Moonshot | 3 | 2.3% | |
| **合计** | **130** | 100% | |

> 注: GLM 占比仅 2.3%,且无 GLM-5.3。

---

## §3 GLM 搜索结果(关键词命中清单)

**搜索关键词**: `glm` / `z-ai` / `zhipu` / `chatglm` / `thudm` / `智谱`
**命中数 (K)**: **3**
**GLM-5.3 是否存在**: **否** (`glm_5_3_present: false`)

### 候选清单(全 3 个)

| # | model_id | 版本日期后缀 | 推测实际 model | 备注 |
|---|---|---|---|---|
| 1 | `glm-4-5-air-20250728` | 2025-07-28 | GLM-4.5 Air | 最老,轻量版 |
| 2 | `glm-4-7-251222` | 2025-12-22 | GLM-4.7(命名疑点:可能是 GLM-4.6 被命名 4.7,或真实 4.7 提前发布) | 唯一一个带 `status` 字段,可能为 preview |
| 3 | `glm-5-2-260617` | 2026-06-17 | **GLM-5.2**(注意:是 5.2 不是 5.3) | **最新,最接近 user 想要的主线目标** |

### 关键判断

- ❌ **GLM-5.3 不在 catalog**(user 17:53 提的版本)
- ✅ **GLM-5.2 在 catalog** (`glm-5-2-260617`, 2026-06-17 标记)
- 候选 1 GLM-4.5 Air 较旧(2025-07),候选 2 命名存疑(2025-12),**主线最佳候选 = `glm-5-2-260617`**

### raw_keys(GLM 三候选字段分布)

```
glm-4-5-air-20250728 : [created, domain, features, id, modalities, name, object, token_limits, version]
glm-4-7-251222       : [created, domain, features, id, modalities, name, object, status, task_type, token_limits, version]
glm-5-2-260617       : [created, domain, features, id, modalities, name, object, task_type, token_limits, version]
```

> 详细 `token_limits` / `modalities` / `features` 值本次未展开(只取 raw_keys),如需下一步 sanity chat,需先用 `GLM_CANDIDATE_ID` 试一次 `/chat/completions` 验证是否真的支持 coding-plan(沿用之前 `doubao-1-5-pro-32k-250115` 的 "UnsupportedModel" 教训)。

---

## §4 与 doubao-seed-code-preview-251028 对比

- `doubao-seed-code-preview-251028` **未在 last_5_models 出现**,但因总数 130 涵盖多 provider,该 model 仍可能存在(仅是排位不在末尾)。
- 本次探活**目标不是 doubao-seed-code** 故未独立 sanity;只需确认: **GLM-5.2 候选 = 火山方舟 catalog 内部 model**(满足 user 17:38 "主线 = 火山引擎内 model" 硬性指令)。
- 之前 bg_67558c58 sanity 3 个 Doubao 全部 "UnsupportedModel — 不支持 coding-plan",**GLM 三个候选在 coding-plan 实际是否可调需另一次 sanity**(本次 0 LLM 调用的边界必须遵守)。

---

## §5 七铁律自检

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | key 永不入 prompt / JSON / 落盘 | ✅ | JSON 中 `auth` 字段 = `ark-de0b484e-0... (truncated)` |
| 2 | 不设 proxy | ✅ | 脚本内显式 `os.environ.pop` 6 个 proxy 变量 |
| 3 | 不调任何 LLM | ✅ | 0 chat / 0 embedding,只 1 GET `/models` |
| 4 | key 永不写盘 | ✅ | API key 只进 `os.environ`,脚本外无任何文件含 key |
| 5 | 不动 5 锚 JSON | ✅ | `D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json` 未触碰 |
| 6 | 不动 4 SPEC V0.1 / v19 / v21 frozen | ✅ | 全部未触碰 |
| 7 | 结果落盘(不含 key/IP) | ✅ | JSON 在 `results/`, 报告在本文件 |

---

## §6 下一步(给 Mavis 父代理)

### 路径 A(若 user 接受 GLM-5.2 替代 GLM-5.3)
- 在 catalog 已确认 `glm-5-2-260617` 存在,user 17:38 "主线 = 火山引擎内 model" 约束仍满足
- 建议下次任务:sanity chat 一次 `glm-5-2-260617`,沿用 `doubao-1-5-pro-32k-250115` 失败时的同样 prompt 模板
- 若 sanity 通过 → 进入 KT_ABC1 1 周判死线

### 路径 B(若 user 坚持 GLM-5.3 不可降级)
- 17:38 "主线 = 火山引擎内 model" 硬性指令**需要 user 主动撤销**(违反 = 撤销)
- 撤销后候选 = 智谱官方 API (`https://open.bigmodel.cn/api/paas/v4`) 或 Z.ai endpoint
- 探活需另起一个 task,**本次任务不擅自动作**

### 路径 C(若 user 接受 GLM-4.5 Air / GLM-4.7 试水)
- `glm-4-5-air-20250728`: 轻量版,2025-07
- `glm-4-7-251222`: 命名存疑(`status` 字段存在,可能 preview)
- 建议:先 sanity `glm-5-2-260617`(最新最稳),失败再回退到 `glm-4-7-251222` / `glm-4-5-air-20250728`

**本次任务明确:只探活 catalog,不做下一步。Mavis 父代理需向 user 同步 §3 结论(GLM-5.3 不存在,GLM-5.2 候选),并询问走路径 A / B / C。**

---

## §7 审计

- JSON 落盘: `D:\私人资料\deposon-repo\results\deposon_volcengine_coding_plan_catalog_2026_09_10.json` (无 key / 无 IP)
- 脚本: `D:\私人资料\deposon-repo\scripts\probe_volc_coding_plan_catalog_2026_09_10.py`
- 报告: 本文件
- 报告时间: 2026-09-10 18:00 +08:00
- worker session: `mvs_0c4c5b3d246c4aedbe18b7b7858adf5f`
- parent session: `mvs_bbeb804b1a6a41109be740636eed1709`
