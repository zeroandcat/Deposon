# Worker A 补测报告 — 火山方舟 Coding Plan 2 model x 30 cells

**生成时间**: 2026-09-10 21:13 (Asia/Shanghai)  
**Worker**: A  
**测试目标**: kimi-k2.7-code + minimax-m3  
**题目数**: GSM8K 15 + StrategyQA 15 = 30 cells/model x 2 model = 60 LLM calls  

## §1 测试环境

| 字段 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan |
| base_url | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| auth | `ark-de0b484e-08...e219` (key 永不入 prompt/JSON/磁盘) |
| max_tokens | 1024 |
| timeout/cell | 30 s |
| temperature | 0.0 |
| proxy | **无** (火山国内直连) |

**Sanity check** (2 model x 1 cell 'What is 1+1?'):

- `kimi-k2.7-code`: status=200 ok=True ms=1685.5 has_2=True text=`2`
- `minimax-m3`: status=200 ok=True ms=8096.0 has_2=True text=`2`

## §2 2 model x 30 cells 结果

| Model | GSM8K (15) | StrategyQA (15) | Total | Pass Rate | Avg ms |
|---|---|---|---|---|---|
| `kimi-k2.7-code` | 10/15 | 9/15 | 19/30 | 63.3% | 9271.2 |
| `minimax-m3` | 12/15 | 9/15 | 21/30 | 70.0% | 4933.9 |

### 各 model GSM8K 详情 (15 cells)

**`kimi-k2.7-code` - GSM8K**:

| # | gold | pred | passed | ms |
|---|---|---|---|---|
| 1 | 18.0 | 18.0 | PASS | 10891.8 |
| 2 | 5.0 | 5.0 | PASS | 5019.0 |
| 3 | 40.0 | 40.0 | PASS | 5210.5 |
| 4 | 1430.0 | 1430.0 | PASS | 4254.2 |
| 5 | 36.0 | 36.0 | PASS | 8309.6 |
| 6 | 8000.0 | 8000.0 | PASS | 3052.2 |
| 7 | 36.0 | 36.4 | FAIL | 8126.1 |
| 8 | 6.0 | 6.0 | PASS | 10545.6 |
| 9 | 40.0 | 40.0 | PASS | 4399.7 |
| 10 | 140.0 | 140.0 | PASS | 6150.0 |
| 11 | 2125.0 | 2125.0 | PASS | 13689.4 |
| 12 | 32.0 | 17.0 | FAIL | 10620.5 |
| 13 | 50.0 | 54.0 | FAIL | 4631.5 |
| 14 | 122.0 | 40.0 | FAIL | 3121.6 |
| 15 | 34.0 | None | FAIL | 30151.0 |

**`minimax-m3` - GSM8K**:

| # | gold | pred | passed | ms |
|---|---|---|---|---|
| 1 | 18.0 | 18.0 | PASS | 5676.1 |
| 2 | 5.0 | 5.0 | PASS | 2948.6 |
| 3 | 40.0 | 40.0 | PASS | 2510.5 |
| 4 | 1430.0 | None | FAIL | 30154.6 |
| 5 | 36.0 | 36.0 | PASS | 3001.2 |
| 6 | 8000.0 | 8000.0 | PASS | 2958.5 |
| 7 | 36.0 | None | FAIL | 18689.0 |
| 8 | 6.0 | 6.0 | PASS | 3542.7 |
| 9 | 40.0 | 40.0 | PASS | 2506.2 |
| 10 | 140.0 | 140.0 | PASS | 3472.6 |
| 11 | 2125.0 | 2125.0 | PASS | 5086.2 |
| 12 | 32.0 | 32.0 | PASS | 8500.2 |
| 13 | 50.0 | 50.0 | PASS | 5005.3 |
| 14 | 122.0 | 1.0 | FAIL | 2665.3 |
| 15 | 34.0 | 34.0 | PASS | 4161.7 |

### 各 model StrategyQA 详情 (15 cells)

**`kimi-k2.7-code` - StrategyQA**:

| # | gold | pred | passed | ms |
|---|---|---|---|---|
| 1 | Yes | yes | PASS | 2563.7 |
| 2 | No | no | PASS | 2350.6 |
| 3 | Yes | yes | PASS | 5626.7 |
| 4 | No | no | PASS | 2978.2 |
| 5 | Yes | None | FAIL | 30061.6 |
| 6 | No | no | PASS | 2516.4 |
| 7 | No | yes | FAIL | 1825.4 |
| 8 | No | no | PASS | 2144.8 |
| 9 | Yes |  | FAIL | 27041.1 |
| 10 | No | yes | FAIL | 4963.1 |
| 11 | No | no | PASS | 3215.0 |
| 12 | No | None | FAIL | 30096.2 |
| 13 | Yes | yes | PASS | 3519.3 |
| 14 | Yes |  | FAIL | 27371.7 |
| 15 | Yes | yes | PASS | 3689.3 |

**`minimax-m3` - StrategyQA**:

| # | gold | pred | passed | ms |
|---|---|---|---|---|
| 1 | Yes | no | FAIL | 5678.0 |
| 2 | No | no | PASS | 1986.1 |
| 3 | Yes | yes | PASS | 2860.2 |
| 4 | No | no | PASS | 4580.4 |
| 5 | Yes | no | FAIL | 4056.4 |
| 6 | No | no | PASS | 1738.6 |
| 7 | No | yes | FAIL | 2298.8 |
| 8 | No | no | PASS | 3076.6 |
| 9 | Yes | no | FAIL | 2955.9 |
| 10 | No | yes | FAIL | 2717.4 |
| 11 | No | no | PASS | 2251.5 |
| 12 | No | no | PASS | 2982.9 |
| 13 | Yes | yes | PASS | 2817.8 |
| 14 | Yes | no | FAIL | 3756.6 |
| 15 | Yes | yes | PASS | 3380.8 |

## §3 与已有 baseline 对比

| Model | Pass / 30 | 来源 |
|---|---|---|
| doubao-seed-2.0-lite | 26/30 (86.7%) | 已有 baseline |
| V4.1-Flash | 25/30 (83.3%) | 已有 baseline |
| `kimi-k2.7-code` | 19/30 (63.3%) | 本次 worker A 补测 |
| `minimax-m3` | 21/30 (70.0%) | 本次 worker A 补测 |

## §4 7 铁律自检

- [x] 1. coding-plan key 从 `LLM API.txt` GB18030 读 -> `os.environ['ARK_CODING_PLAN_KEY']`
- [x] 2. 无 proxy (env 全清)
- [x] 3. 仅调 2 model (`kimi-k2.7-code` + `minimax-m3`),不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan
- [x] 4. key 永不入 prompt / JSON / 磁盘 (auth 字段只截断)
- [x] 5. 60 calls 严格,无重试,无切超 2 model
- [x] 6. 未触碰 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`)
- [x] 7. 未触碰 4 SPEC V0.1 冻结版 / v19 frozen JSON / v21 frozen JSON

## §5 下一步

- 等待 worker B / C / D 补测结果汇总
- 9 model 完整 pass rate 表生成
- 与 baseline 26/30 (doubao-seed-2.0-lite) / 25/30 (V4.1-Flash) 对比决定是否进入下一阶段

---

*报告生成: worker A, 2026-09-10 21:13 (Asia/Shanghai)*