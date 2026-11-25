# V42_V2 论文修正条款 (2026-09-16)

执行代理 B (KIMI 派出) · 与 [V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md](V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md) 配套
数据来源: [results/deposon_v42_v2_miss_rate_curve_2026_09_16.json](../../results/deposon_v42_v2_miss_rate_curve_2026_09_16.json) (generated_utc = 2026-09-16T10:27:36.957114+00:00, seed = 20260916)

---

## 条款 1 · 计数语义反转更正 (强制, 最高优先级)

如实记录: **P-M 初报"漏检率 100%"系计数语义反转, 经复算更正为检出率 100% (单 bit 级), 但旧 v42 在覆盖/定位/链结构上的短板成立, v42_v2 为此而设。**

- 反转机制: [deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py](../../deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py) L82-87 将 `is_valid=True` (篡改后仍通过) 计入 `detected_count`, 将 `is_valid=False` (verifier 拒绝 = 检出) 计入 `missed_count`, 两个分支记反。
- 复算证据 (runner `--confirm-inversion`, 2000 次单 bit 翻转, seed = 20260916): P-M 原口径报 missed = 2000/2000 (漏检率 1.0); 正确口径实测 detected = 2000/2000 (检出率 1.0, 漏检率 0.0)。
- 论文中凡引用"P-M 漏检率 100%"作为 v42 重设计动机之处, 一律替换为本条款上文加粗句。

## 条款 2 · 可审计性不等式

可审计性 = f(篡改成本下界, 复算成本), 形式化为:

```
系统可审计  ⟺  C_tamper^min  >  C_verify

其中:
  C_tamper^min = k · 2^48        (篡改成本下界)
  C_verify     = n · c_hash + c_manifest + c_chain   (复算成本)
```

- k = 被篡改文件数; 48 = sha256[0:12] 前缀bit数, 单文件伪造须找到该 48-bit 前缀的第二原像, 期望成本约 2^48 次哈希; 每多改一个文件, 成本下界线性放大。
- n = 保护集文件数 (v42_v2: n = 8); c_hash = 单文件哈希成本; 实测保护集 534,942 字节的完整三层复算为毫秒级 (3,202 次 verify() 调用 + 全部攻击评测合计 10.953 s 墙钟, 含 Python 解释器开销)。
- 结构类篡改 (增/删/改名/集合错位) 在 L2 由 manifest 根捕获; 旧基线整体重放在 L3 由追加式 runs 链链头捕获, 其不被发觉的前提是重写链全部历史记录, 而 genesis + 逐条 prev_hash 连续性校验 (verify_chain) 使该前提等价于链整体伪造。
- 结论: 在 48-bit 前缀口径下 C_tamper^min ≈ 2^48 次哈希 vs C_verify 为毫秒级单次复算, 不等式以约 2^48 : 1 的工作量不对称成立, 系统满足可审计性。

## 条款 3 · 旧 v42 真实短板与 v42_v2 对应处置

| 旧 v42 短板 | 后果 | v42_v2 处置 | 实测证据 |
|---|---|---|---|
| 仅 5 文件覆盖 | 保护集外制品 (plugin spec, corpus, 结果文件) 改动不可见 | 保护集 n = 8: 5 锚 JSON + 4 plugin spec + corpus/v20/index.json + v19 + v21 | baseline root = 2e2f856bed05, file_hashes 8 条 |
| 单值比对无定位能力 | 拒绝时不知哪个文件、哪一层 | 每次拒绝输出 {layer, file, expected, actual} | 实跑: layer=L1, file=corpus/v20/index.json, expected=8423ffe266af, actual=cd0eca4ccaf7 |
| 无 manifest/链结构 | 合法更新即全局失效; 旧基线重放无机制察觉 | L2 canonical manifest + 根; L3 追加式 runs 链 (新链, 旧链 2026-09-04_pd_v0.jsonl 未触) | A5 重放攻击 200  trials, 检出率 1.0, 定位正确率 1.0 |

## 条款 4 · 验证表 (前瞻声明的确认/挑战阈值与行动)

| 声明 | 确认阈值 | 挑战阈值 | 触达行动 |
|---|---|---|---|
| 6 类攻击漏检率 ≤ 0.01 | 复跑 (同 seed) 各 attack 聚合 miss_rate ≤ 0.01 | 任一 attack 聚合 miss_rate > 0.01 | 复算差异档位 trials; 若为等值字节交换 no-op 以外成因, 重审 L1 口径 |
| A3 budget=1 档漏检全为 no-op | 该档漏检 trials 中等值字节交换占比 = 100% | 出现非 no-op 漏检 | 定位该 trial 字节级 diff, 修订本条款 §4 |
| 单 bit 检出率 = 1.0 (新旧两 verifier) | `--confirm-inversion` 正确口径 detection_rate = 1.0 | < 1.0 | 检查锚集合与哈希口径是否漂移 |
| 重放必被 L3 拒绝 | A5 各档 detection_rate = 1.0 | 任一档 < 1.0 | 检查链头读取与 manifest 扩展字段 |
| 复算成本毫秒级 | 全流程 (含评测) 墙钟 < 60 s | ≥ 60 s | 分档计时, 复核是否引入非哈希开销 |

## 条款 5 · 合规与边界

- 0 LLM 调用 (纯 hashlib + numpy + json), 不调网关, 不 pip install, 不设 proxy。
- 仅新建: v42_v2 verifier、baseline、新链、runner、结果 JSON、两份文档; 18 frozen + P-G V0/V0.1 + verifier/v1..v35 既有文件 + 旧 runs 链 + 任何既有文档 0 修改 0 删除。
- 本条款全部数字可溯源到结果 JSON 与 runner stdout; 未使用禁用术语与任何密钥形态字符串。
