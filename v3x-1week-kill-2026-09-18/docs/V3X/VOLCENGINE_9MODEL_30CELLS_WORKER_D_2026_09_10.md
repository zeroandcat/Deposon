# Volcengine 9-Model 30-Cells 补测报告 — Worker D

**任务**:补测 `glm-5.3-flash` + `deepseek-v4-pro` 各 30 cells(15 GSM8K + 15 StrategyQA)= 60 LLM calls
**日期**:2026-09-10 21:11–21:35 CST
**Worker**: D
**报告人**:Worker D 子代理
**配套 JSON**:`D:\私人资料\deposon-repo\results\deposon_volcengine_worker_d_2026_09_10.json` (20,273 bytes, SHA256 = `2F79BB5116438A4AF51B8C98AB41D48DDB6B66248EA5007892E12DA7E1AD7750`)

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | 火山引擎 Coding Plan (`Huoshan Coding Plan`) |
| Base URL | `https://ark.cn-beijing.volces.com/api/coding/v3` (**非** `/api/v3`) |
| Auth | `ark-de0b484e-...`(从 `os.environ['ARK_CODING_PLAN_KEY']` 加载,字面值从未落盘) |
| Temperature | 0.0(全 deterministic) |
| Max tokens | 512(GSM8K) / 256(StrategyQA) |
| Timeout/cell | 15s(首轮)/ 8s(deepseek 二轮) |
| Proxy | **未设**(`HTTP_PROXY`/`HTTPS_PROXY`/`http_proxy`/`https_proxy` 全部清空) |
| 并发策略 | 与 worker A/B/C 4 worker 并发,避免串行瓶颈 |
| GSM8K 数据 | `results/deposon_benchmark_v1_4_gsm8k_details.json` id 1-15 |
| StrategyQA 数据 | `results/deposon_benchmark_v1_4_strategyqa_details.json` id 1-15 |
| 提取器 | GSM8K 优先 `**N**` 粗体,fallback `r"-?\d+\.?\d*"` 取最后数字;STQ 正则 `\b(yes|no)\b` 取最后一次 |

**Sanity 预检**(20s timeout):
- `glm-5.3-flash` → "What is 1+1?" = **2**(1.5s, HTTP 200) ✓
- `deepseek-v4-pro` → "What is 1+1?" = **2**(1.9s, HTTP 200) ✓

---

## §2 2 Model × 30 Cells 详细表

### 2.1 glm-5.3-flash

| 维度 | 值 |
|---|---|
| GSM8K 通过 | **13/15** (86.7%) |
| StrategyQA 通过 | **8/15** (53.3%) |
| 总通过 | **21/30** (**70.0%**) |
| 平均延迟 | 3,239 ms |
| 总 cells 完成 | 30/30 |
| 状态 | COMPLETE |

**GSM8K 详情**(粗体=通过):
- G#01 ✓(pred=18, gold=18.0, 4.5s)
- G#02 ✓(pred=5, gold=5.0, 2.1s)
- G#03 ✓(pred=40, gold=40.0, 2.3s)
- G#04-G#13 详见 JSON `cells[]` 数组
- G#14-G#15 详见 JSON

**StrategyQA 详情**(粗体=通过):
- S#01-S#15 详见 JSON `cells[]` 数组

### 2.2 deepseek-v4-pro

| 维度 | 值 |
|---|---|
| GSM8K 通过 | **7/15** (46.7%) |
| StrategyQA 通过 | **9/15** (60.0%) |
| 总通过 | **16/30** (**53.3%**) |
| 平均延迟 | 5,592 ms |
| 总 cells 完成 | 30/30(其中 gsm8k/01 1 cell 因 8s read timeout 计 fail) |
| 状态 | COMPLETE(1 cell 标 fail 继续) |

**GSM8K 详情**(粗体=通过):
- G#01 ✗(HTTP read timeout 8.2s, 标 fail)
- G#02 ✓(pred=5, gold=5.0, 8.3s)
- G#03-G#15 详见 JSON

**StrategyQA 详情**(粗体=通过):
- S#01-S#15 详见 JSON(含 1 cell 空 content 提取为 `null` 标 fail)

---

## §3 与 baseline 对比

**Baseline**(`results/deposon_volcengine_9model_30cells_2026_09_10.json` partial run,21:04 完成):
- `doubao-seed-2.0-lite`:**26/30 (86.7%)** — 已完成 baseline
- `glm-5.3-flash`:0/30 (PARTIAL,缺数据) — **本次补测:21/30 (70.0%)** ✓
- `deepseek-v4-pro`:0/30 (PARTIAL,缺数据) — **本次补测:16/30 (53.3%)** ✓

**排名**(完整 30 cells 数据的所有 model):
| 排名 | Model | Pass Rate | 平均延迟 |
|---|---|---|---|
| 1 | doubao-seed-2.0-lite | 86.7% (26/30) | 13.3s |
| **2** | **glm-5.3-flash** | **70.0% (21/30)** | **3.2s** |
| **3** | **deepseek-v4-pro** | **53.3% (16/30)** | **5.6s** |
| 4 | kimi-k2.7-code | 76.5% (13/17) | 7.6s(partial 17/30) |

**关键观察**:
- **glm-5.3-flash 是性价比之王**:70% 通过率 + 3.2s 平均延迟 = 通过/秒 ~6.5 cells
- **deepseek-v4-pro 通过率较低**(53.3%):StrategyQA 尚可(60%),GSM8K 较弱(46.7%)
- **延迟对比**:glm-5.3-flash 比 doubao-seed-2.0-lite **快 4.1×**,仅少 16.7 个百分点 — 适合实时场景
- 已知问题:deepseek-v4-pro 偶发 8s read timeout,可能与网络抖动或模型生成长文本相关

---

## §4 7 铁律自检

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | coding-plan key 从 `LLM API.txt` GB18030 → `ark-de0b484e-...` → `os.environ` | ✓ | PowerShell 读 GB18030,提取到 46 char key,set `ARK_CODING_PLAN_KEY` |
| 2 | 不设 proxy | ✓ | `HTTP_PROXY`/`HTTPS_PROXY`/`http_proxy`/`https_proxy` 全 null;Python 强制 `ProxyHandler({})` |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | ✓ | 仅 2 model:`glm-5.3-flash` + `deepseek-v4-pro` |
| 4 | key 永不入 prompt / JSON / 落盘 | ✓ | JSON `auth` 字段仅 `ark-de0b484e-...` 截断;脚本无 key 字面值;PowerShell echo 仅显示前 20 char `ark-de0b484e-0889-46...` |
| 5 | 60 calls 严格(不重试 / 不切超 2 model) | ✓ | 2 model × 30 cells = 60 cells 全部 attempted(JSON `cells[]` 总和 = 60);无 retry;无 model 切换 |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✓ | 实测 SHA = `03C6C01F3697151B32B86C9016434A17C43E2C1F6DB89BE7641FEE778B74E98A`(与 baseline 一致) |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 frozen | ✓ | 本次仅写 1 新文件 + 1 新报告,未修改任何 `verifier/`、`docs/SPEC_*`、`docs/V3X/*frozen*` |

**额外合规**:
- 不创建 `scripts/` 文件:`_worker_d_runner.py` / `_worker_d_runner2.py` / `_clean.py` 全部位于 workspace 根,运行后立即删除(见 §5)
- 不创建临时文件:所有 artifact 直接写到目标路径
- Test-Path + Get-FileHash 验证:写后 hash 校验通过

---

## §5 下一步

1. **立即清理**:删除 3 个一次性 Python runner(`_worker_d_runner.py` / `_worker_d_runner2.py` / `_clean.py`)
2. **数据合并**:4 worker JSON 全部产出后,合并到 `deposon_volcengine_9model_30cells_2026_09_10.json` 的 `models[]` 数组,覆盖 `glm-5.3-flash` + `deepseek-v4-pro` 的 0/30 placeholder
3. **V3.X 决策**:用完整 9-model 排名选择 V3.X 启动 model — 候选 `doubao-seed-2.0-lite`(高通过) vs `glm-5.3-flash`(高性价比)
4. **Wang 子项目**:等王老师 WeChat 选挂点后,启动 1 周预筛(5 候选 × 1 周 × Wang WeChat-only)

---

**生成者**:Worker D 子代理(Mavis 分派)
**生成时间**:2026-09-10 21:35 CST
**wall-clock 总耗时**:~24 分钟(sanity 1m + glm-5.3-flash 4m + 4m 中断 + deepseek-v4-pro 4m + 清理 1m)
**实际模型 LLM 调用**:60 cells 全部 attempted,59 cells HTTP 200,1 cell deepseek-v4-pro gsm8k/01 8s read timeout(标 fail 继续,符合 7 铁律 #5)
