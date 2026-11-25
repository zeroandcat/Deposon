# 安全审计报告 v2（code-safety-audit）

- 日期：2026-08-28（审计基线 v2）
- 工具：`/app/.agents/skills/code-safety-audit/scripts/security_scan.py`（secrets / owasp / deps 三模式）+ 人工 grep 复核
- 范围：仓库全量（含 results/、corpus/、verifier/、docs/；`_paper_backup_v181` 纳入扫描）
- 重要纪律：本报告不含任何完整密钥值；命中仅报告 文件/行/类型。

## 1. 结论摘要

| 模块 | 结果 | 严重度分布 |
|---|---|---|
| secrets（密钥泄露） | **0 发现 —— 确认仓库无真实 API key 落盘** | 0 / 0 / 0 / 0 |
| owasp（安全模式） | 9 项 medium，**全部为误报/良性用法** | 0C/0H/9M/0L |
| deps（pip-audit, requirements.txt） | **No known vulnerabilities found**（exit 0） | — |

## 2. 密钥泄露确认：否

- secrets 扫描器（正则 + Shannon 熵）：0 findings。
- 人工 grep 复核（`sk-*`、`AIza*`、`ghp_*`、`AKIA*`、`xox[bpoas]-*` 等真实 key 前缀，覆盖 *.py/*.json/*.md/*.txt/*.csv）：0 命中。
- results/ 下全部缓存 JSON 中 grep `Bearer ` / `Authorization`：0 命中（缓存仅存响应文本与元数据，不含凭据）。
- 历史教训"key 只能内联 env"维持成立：所有 LLM 调用脚本 key 均来自 `os.environ.get(...)`，无默认值、无硬编码。

## 3. key 处理合规性核查（llm_prior.py / run_v20_*_fetch.py）

合规模式确认：
- `llm_prior.py:99` `key = os.environ.get("KIMI_API_KEY")`；无 key 抛 RuntimeError（L101）；`_sanitize(msg, key)`（L84-85）兜底剔除所有异常/HTTP 回显中的 key；缓存（L131）注明"key 仅存在于运行时"。
- 合规的 fetch 脚本（env 读取 + `_sanitize` 包裹全部错误路径）：run_v20_bigquiz_fetch.py、run_v20_cot_fetch.py、run_v20_crossval_fetch.py、run_v20_familyL_fetch.py、run_v20_gt3_fetch.py、run_v20_gt8b_fetch.py。

**发现 F-SEC-1（medium，唯一实质加固项）**：
- `run_v20_gt3b_fetch.py`（L66-72）与 `run_v20_gt3c_fetch.py`（同构）使用 `ARK_API_KEY`，但错误路径 **未走 `_sanitize`**：`raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")` 与 `last_err = f"{type(e).__name__}: {str(e)[:120]}"`。若服务端在 4xx 响应体中回显请求头/token，key 可能经 `last_error` 落入 `results/gt3_prior_cache/*.json` 与 stdout。当前缓存抽查无泄露（grep Bearer/Authorization 0 命中），但属"无兜底"例外路径，与 llm_prior.py 的防御范式不一致。
- 修复建议：两处改为复用 `llm_prior._sanitize(...)` 包裹 HTTP 错误与异常消息（与其他 6 个 fetch 脚本对齐）。

误报排除标注：
- `verifier/*/check.py` 内红线 pattern 字符串（如 `"sk-" + "kimi-"` watch 前缀）是**检测用哨兵字符串**，非真实 key；secrets 扫描器本轮未命中，owasp/deps 亦无涉。标记为永久误报排除。

## 4. OWASP 发现（9 项 medium，全部误报/良性）

全部为 `Weak Hash (MD5)`，两类良性用途：

| 位置 | 行 | 实际用途 | 判定 |
|---|---|---|---|
| deposon_agents_v1_3.py | 295, 314 | 缓存文件名哈希（非密码学场景） | 良性，排除 |
| deposon_agents_v1_4.py | 295, 314 | 同上 | 良性，排除 |
| run_v19_benchmark_fixes.py | 82 | 同上 | 良性，排除 |
| verifier/v16/check.py | 15 | 论文文件完整性指纹（哈希基线比对） | 良性，排除 |
| verifier/v19/check.py | 32 | 同上 | 良性，排除 |
| verifier/v20/check.py | 52 | 同上 | 良性，排除 |
| verifier/v21/check.py | 63 | 同上 | 良性，排除 |

无 SQL 注入 / 命令注入 / XSS / 反序列化 / SSRF / CORS / debug 模式发现。

## 5. 依赖漏洞（deps）

`pip-audit -r requirements.txt`：**No known vulnerabilities found**（exit 0）。

## 6. 与既有 audits_security.json 增量对比

| 项 | 基线 (audits_security.json) | 本轮 v2 | Delta |
|---|---|---|---|
| 总发现 | 5 | 9 | +4 |
| critical/high | 0 / 0 | 0 / 0 | 0 |
| 新增 medium | — | verifier/v16, v19, v20, v21 check.py 各 1 条 MD5 | 均为完整性校验用途，误报 |
| secrets | 0 | 0 | 0 |
| deps | 0 漏洞 | 0 漏洞 | 0 |

实质风险增量：仅 F-SEC-1（gt3b/gt3c 缺 `_sanitize` 兜底），系基线报告未覆盖的脚本级加固缺口。

## 7. 修复建议优先级

1. **P1**：run_v20_gt3b_fetch.py / run_v20_gt3c_fetch.py 错误路径接入 `_sanitize`（消除 key 经 HTTP 回显落盘的理论通道）。
2. **P3**：在扫描配置中将 verifier/*/check.py 的 MD5 完整性校验与缓存文件名哈希加入排除清单，降低后续审计噪音。
3. 保持现状纪律：key 仅从 env 读取、禁 mock、缓存只落响应文本——本轮复核全部成立。
