# probe URL 更新 log (2026-09-23)

> **任务**: `results/_v4_v5_multimodel_probe.py` 端点段更新为新三端点
> **PI 拍板**: ask_7844adffe9c7d56b73a8d2ca Q2 (2026-09-23)
> **Worker**: Mavis worker (分支 session `mvs_b7dee76f62ac4130838ebde362917c71`)
> **派工模式**: 改构建配置类工作 → 待 parent 复审
> **skill**: superpowers:verification-before-completion
> **plugin**: @superpowers (plugin-cache sha256 prefix `ade95665080e`)
> **本档状态**: 待 parent 复审

---

## 1. 哈希对账 (旧 → 新)

| 件 | SHA-12 | SHA-256 | 字节 |
|---|---|---|---|
| 主本(新) | **`B65619A07B10`** | `b65619a07b103bbaa3f519d82b404353062649def6331b7912f81b8df6fa3607` | 6209 |
| 主本(旧, 已备份为 `.bak_2026_09_23`) | `5FE4CBD93D92` | `5fe4cbd93d92937de5830c9dd9f3957277b03993293bdc0f5192db13d7a15190` | 6159 |
| 权威探活 JSON (不动) | `C846F7FC79EE` | `c846f7fc79eee24f15c5be0356d74d098a74eb27a3bbcd42a97f0d2870db3f92` | 5803 |

旧 sha12 `5FE4CBD93D92` 与本任务 brief 一致 ✓
新 sha12 `B65619A07B10` 实算确认 ✓
权威 JSON sha12 `C846F7FC79EE` 与本任务 brief 一致 ✓

---

## 2. Diff 摘要

#### 1.1 模块 docstring (头部)
- 新增 `(2026-09-23 端点更新版)` 标题
- 新增 PI 拍板来源引用 `ask_7844adffe9c7d56b73a8d2ca Q2`
- 新增权威源引用 `results/_track2_endpoints_probe_2026_09_23.json (SHA-12 C846F7FC79EE)`
- 新增代理硬要求说明 "teamo 槽位必走 tun 防封号"

#### 1.2 常量段
- 新增 `PROXY_SOCKS5 = "socks5://127.0.0.1:1018"`(备用, 全部走 http_proxy 即足够)
- 新增 `INTER_PROBE_SLEEP_S = 2.5`(PI 防封硬纪律: 串行 ≥2s)
- `PROXY_HTTP` 保留

#### 1.3 ROUTE_TEMPLATES (端点段, 主要变更)
**从 6 路由精简为 3 路由 (按 PI 拍板三 URL)**:

| 槽位 | 旧 URL | 新 URL | 旧 model | 新 model | 旧 key_idx | 新 key_idx | use_proxy |
|---|---|---|---|---|---|---|---|
| qwen_plan | `dashscope.aliyuncs.com/compatible-mode/v1/chat/completions` | `token-plan.maas.qianwenaiapi.com/compatible-mode/v1/chat/completions` | `qwen-turbo` | `qwen3.7-max` | 20 | **23** | False |
| mimo | `api.mioplus.mi.com/v1/chat/completions` | `token-plan-cn.xiaomimimo.com/v1/chat/completions` | `mimo-7b` | `mimo-v2.6-pro` | 23 | **27** | False |
| teamo | `api.teamo.ai/v1/chat/completions` | `api.teamorouter.cn/v1/chat/completions` | `deepseek/deepseek-v4.1-flash` | `deepseek-v4-flash` (响应自版本化为 `deepseek-v4-flash-0731`) | 11 | **15** | **True** |

**删除**:
- `openrouter` 路由 (openrouter.ai)
- `deepseek_direct` 路由 (api.deepseek.com)
- `qwen` (非 plan) 路由

理由: PI 拍板三 URL ↔ 三槽位对应实际工作槽; 其余旧路由本次不探活

#### 1.4 探活逻辑
- 删除全局 `setup_proxy()`; 改为路由级条件代理 (`rt["use_proxy"]`)
- 新增 `INTER_PROBE_SLEEP_S` 串行间隔, 在 `main()` loop 中 `time.sleep(INTER_PROBE_SLEEP_S)` (除首次外)
- `max_tokens`: 5 → **1** (PI 拍板最小必要探活)
- 成功返回 dict 新增 `proxy_used` 字段
- banner 头部新增 "端点更新版" 标识 + 权威源 SHA-12

---

## 3. 探活结果 (worker 自验)

执行: `python results/_v4_v5_multimodel_probe.py`
时间: 2026-09-23 15:55 CST (实际)
环境: Python 3.14.7 + requests 2.34.2, Windows 10

| 槽位 | URL | model | use_proxy | status | latency | 结果 |
|---|---|---|---|---|---|---|
| qwen_plan | `token-plan.maas.qianwenaiapi.com/compatible-mode/v1/chat/completions` | `qwen3.7-max` | False | **200** | 6433.9 ms | ✓ OK |
| mimo | `token-plan-cn.xiaomimimo.com/v1/chat/completions` | `mimo-v2.6-pro` | False | **200** | 916.9 ms | ✓ OK |
| teamo | `api.teamorouter.cn/v1/chat/completions` | `deepseek-v4-flash` | **True** (tun:1018) | **200** | 2771.7 ms | ✓ OK |

**三端点全 200 ✓** (PI 拍板完成条件达成)

---

## 4. 自验记录

#### 4.1 py_compile
```
python -m py_compile results/_v4_v5_multimodel_probe.py
EXIT=0
```

#### 4.2 最小探活 (max_tokens=1, 串行 2.5s, teamo 强制走代理)
见 §3 表格

#### 4.3 备份校验
- `.bak_2026_09_23` 文件 6159 字节
- SHA-256 与原主本一致: `5fe4cbd93d92937d...`
- 备份不被修改, 仅作存档 ✓

---

## 5. 铁律遵守对账

| 铁律 | 状态 | 备注 |
|---|---|---|
| R4 key 永不明文 | ✓ | 仅 `read_key()` runtime 内存读, log/产物零 key 字段 (`"runtime-env (redacted)"`) |
| R5 V4 frozen 只追加 | ✓ | probe 非 frozen 件 (PI 明示授权可改), 其余 frozen 件前后指纹自证 0 触动; 本档无 frozen 触动 |
| 改构建配置类 parent 复审 | ✓ | 本档标注「待 parent 复审」 |
| teamorouter 走 tun 防封号 | ✓ | teamo 槽 `use_proxy=True` 强制走 `http://127.0.0.1:1018` |

---

## 6. 老实交代

- 探活结果如实回报: 三端点全 200 (含 latency 实测, 无编造)
- 旧件已备份为 `.bak_2026_09_23` (6159B), 主本 6209B (新)
- 权威 JSON 未触动 (`C846F7FC79EE` 与 brief 一致)
- py_compile EXIT=0 + 三端点 200 + 产物哈希实算齐备 → 达成"完"标准
- 产物: 更新正本 + `.bak_2026_09_23` + 本 log (3 件齐)

---

## 7. 派工下游

- **parent 复审** (硬纪律): 改构建配置类工作, 等 parent 复审后才宣告冻结
- V5 补强 D2/D3 仍可继续用本 probe 作前置探活 (PI 后续派工范围)
- 若后续某端点切到不同 URL, 重做探活并附新 probe JSON (权威源轮换, 与本档同模式)