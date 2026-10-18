# V42_V2 Verifier 性能报告 (2026-09-16)

执行代理 B (KIMI 派出) · 0 LLM (纯 hashlib + numpy + json) · 全部数字可溯源到运行输出

数据来源: [results/deposon_v42_v2_miss_rate_curve_2026_09_16.json](../../results/deposon_v42_v2_miss_rate_curve_2026_09_16.json) (generated_utc = 2026-09-16T10:27:36.957114+00:00, seed = 20260916, elapsed = 10.953 s)

---

## 0. 摘要 (结论先行)

- v42_v2 分层 verifier 对 6 类攻击 × 10 档预算全部实测: 5 类漏检率 0.0, byte_swap 类漏检率 0.01 (全部为该档等值字节交换的无实际操作, 见 §4.3), 定位正确率除该档外均为 1.0。
- P-M 初报"旧 v42 漏检率 100%"系**计数语义反转**, 经 2000 次单 bit 翻转复算更正为: 旧 v42 检出率 100% (单 bit 级)。更正声明见 §3。
- v42_v2 的设立依据是旧 v42 的三项真实短板: 覆盖仅 5 文件、单值比对无定位能力、无 manifest/链结构 (合法更新即全局失效, 旧基线重放无机制察觉)。

## 1. 算法说明

实现: [deposon_team/verifier/v42_v2_2026_09_16.py](../../deposon_team/verifier/v42_v2_2026_09_16.py); 一键复跑: [deposon_team/plugins/_v42_v2_runner_2026_09_16.py](../../deposon_team/plugins/_v42_v2_runner_2026_09_16.py)。

保护集 n = 8 (仓库相对 posix 路径, ASCII 升序): 5 锚 JSON × 1 + plugin spec × 4 + corpus/v20/index.json + v19 结果 + v21 结果。基线 root = `2e2f856bed05`, 逐文件 sha12 基线落盘于 `deposon_team/verifier/v42_v2_baseline_2026_09_16.json` (首次运行自举实算)。

| 层 | 机制 | 口径来源 | 拒绝时输出 |
|---|---|---|---|
| L1 | 逐文件 SHA-256[0:12] 比对 | fingerprint_v0 R1 内容寻址 | 文件 + 层 + 期望 vs 实测 |
| L2 | canonical manifest + 根指纹 | fingerprint_v0 R2 (path ASCII 升序, ensure_ascii=False, separators=(",",":")) / R3 (sha256(manifest utf-8)[0:12]); 另含基线自洽校验 root(baseline.manifest) == baseline.root | 层 + 期望根 vs 实测根 |
| L3 | 追加式 runs 链, 链头根必须等于当前基线根 | fingerprint_v0 R4 记录格式 {ts, prev_hash, current_root}, 扩展 manifest 字段用于重放后的文件级定位 | 层 + 链头根 vs 基线根 + 文件级 diff |

新链文件: `deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` (本次 1 条记录, prev = 000000000000, root = 2e2f856bed05, verify_chain 通过)。旧链 `verifier/runs/2026-09-04_pd_v0.jsonl` (current_root = 7d6d3d39fad8) 未触。

只读复用核验: fingerprint_v0.compute_root 重算保护集, R1 逐文件内容寻址与 v42_v2 **完全一致** (r1_per_file_hash_match = true); 根因路径基不同而不同 (绝对路径基 ca14a716f60f vs 仓库相对路径基 2e2f856bed05), 属设计内差异。

拒绝输出契约实例 (实跑 [3]): 单 bit 翻转 → `layer=L1, file=corpus/v20/index.json, expected=8423ffe266af, actual=cd0eca4ccaf7`。

## 2. 攻击面 O(n) 论证

- 防御方复算成本: 一次全量验证 = n 个文件各一次 SHA-256 + 一次 manifest 根, 时间复杂度 O(n), 实测保护集 534,942 字节的完整三层验证为毫秒级 (全流程 3,202 次 verify() 调用 + 攻击评测总计 10.953 s 墙钟)。
- 攻击方篡改成本下界: 改动任一受保护文件即被 L1 以 48-bit 前缀比对捕获; 要使伪造通过, 须对每个被改文件找到 sha256[0:12] 第二原像, 单文件期望成本约 2^48 次哈希, k 个文件约 k · 2^48。攻击面随保护集文件数 n 线性展开, 故记为 O(n)。
- 结构类攻击 (增/删/改名/集合错位) 改变 manifest 根, 在 L2 暴露; 旧基线 + 旧文件整体回滚 (重放) 使基线根 ≠ 链头根, 在 L3 暴露。重放要不被发现, 须同时重写追加式链的全部历史记录, 而 verify_chain 的 genesis + 逐条 prev_hash 连续性校验使该成本升级为链整体伪造。

## 3. P-M 计数语义反转 · 更正声明 (强制一节)

**反转机制**: [deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py](../../deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py) L82-87 中, `is_valid=True` (篡改后仍通过) 被计入 `detected_count`, `is_valid=False` (verifier 拒绝 = 检出) 被计入 `missed_count` —— 两个分支记反。

**复算** (runner `--confirm-inversion` 模式, 2000 次单 bit 翻转, seed = 20260916):

| 计数口径 | 规则 | 检出 | 漏检 | 报告值 |
|---|---|---|---|---|
| P-M 原口径 (反转) | is_valid → detected | 0 | 2000 | 漏检率 1.0 |
| 正确口径 | 检出 = verifier 拒绝 | 2000 | 0 | 检出率 1.0, 漏检率 0.0 |

**更正**: P-M 初报"漏检率 100%"不成立; 正确语义下旧 v42 对单 bit 翻转检出率 100% (单 bit 级)。旧 v42 的真实短板为: ① 仅 5 文件覆盖; ② 单值比对无定位能力; ③ 无 manifest/链结构, 合法更新即全局失效。v42_v2 为此三项短板而设, 而非为漏检率而设。

## 4. 漏检率曲线 (正确语义: 检出 = verifier 拒绝; 漏检 = 篡改后仍通过)

每列: budget / trials / detection_rate / miss_rate / localization_accuracy。全部实跑, 攻击作用于内存字节副本, 保护集 0 写。

### 4.1 A1 单 bit 翻转 (budget = 累计尝试次数, 每档 100 次)

| budget | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 1000, detection = 1.0, miss = 0.0, loc = 1.0。Spearman(budget, miss_rate): rho 未定义 (常数序列)。

### 4.2 A2 多 bit 翻转 (budget = 每文件翻转 bit 数)

| budget | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 500, detection = 1.0, miss = 0.0, loc = 1.0。Spearman: rho 未定义 (常数序列)。

### 4.3 A3 字节交换 (budget = 每文件字节对交换次数)

| budget | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 0.9 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 0.9 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 500, detection = 0.99, miss = 0.01, loc = 0.99。Spearman rho = -0.5222 (并列取平均秩)。
**如实说明**: budget = 1 档 5/50 漏检全部为**等值字节交换** —— 交换两个取值相同的字节后文件字节序列不变, 属无实际操作 (no-op), verifier 放行是正确行为, 此处按保守口径计入漏检。独立测定单交换等值字节概率约 0.0818 (20,000 次采样, seed = 7), 与该档实测 0.10 在 50 次采样涨落内一致。budget ≥ 2 各档漏检率均为 0。

### 4.4 A4 文件截断 (budget = 截断尾部字节比例)

| budget | 0.01 | 0.02 | 0.04 | 0.08 | 0.16 | 0.24 | 0.32 | 0.48 | 0.64 | 0.80 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 500, detection = 1.0, miss = 0.0, loc = 1.0。Spearman: rho 未定义 (常数序列)。

### 4.5 A5 manifest 重放 (旧基线 + 旧文件整体回滚; budget = 回滚文件数)

| budget | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 8 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 200, detection = 1.0, miss = 0.0, loc = 1.0 (L3 拒绝 + 链头 manifest 文件级 diff 定位)。Spearman: rho 未定义 (常数序列)。后三档 budget 封顶于 8 (保护集大小), 为不同随机种子复测。

### 4.6 A6 文件重命名调换 (内容轮换, 路径不变; budget = 参与轮换文件数)

| budget | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 8 | 8 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| detection | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| miss | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loc_acc | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

聚合: trials = 500, detection = 1.0, miss = 0.0, loc = 1.0 (L1 路径 → 哈希绑定逐文件捕获)。Spearman: rho 未定义 (常数序列)。后三档 budget 封顶于 8。

## 5. 与旧 v42 对比

| 维度 | 旧 v42 (P-M runner L30-45 内联语义) | v42_v2 |
|---|---|---|
| 覆盖文件数 | 5 (锚制品) | 8 (保护集) |
| 判定方式 | 制品字节 sha12 属于锚集合 → True | L1 逐文件 + L2 manifest 根 + L3 链头 |
| 定位能力 | 无 (单值集合判定) | 每次拒绝给出文件 + 层 + 期望 vs 实测 |
| 链结构 | 无; 合法更新即全局失效, 旧基线重放无机制察觉 | 追加式 runs 链; 重放在 L3 拒绝并文件级定位 |
| 单 bit 翻转检出率 (正确口径) | 1.0 (复算更正后) | 1.0 (A1 实测) |

**不做"漏检率降低 X 倍"声明**: 旧 v42 在正确口径下对单 bit 翻转检出率已为 1.0, 与新 verifier 持平, 不存在可比较的漏检率差; v42_v2 的增益在覆盖 (5 → 8 文件)、定位 (无 → 文件+层+期望/实测)、链结构 (无 → 抗重放) 三个维度。各攻击 budget-miss_rate 的 Spearman 秩相关随附于 §4 各表与结果 JSON; 除 A3 (rho = -0.5222, 成因见 §4.3) 外, miss_rate 为常数 0 序列, rho 未定义。

## 6. 复跑方法

```
python deposon_team/plugins/_v42_v2_runner_2026_09_16.py                      # 全流程
python deposon_team/plugins/_v42_v2_runner_2026_09_16.py --confirm-inversion  # 反转复算
```

环境: Python 3.12.14 + numpy 2.4.4; 0 LLM 调用, 不调网关, 不 pip install, 不设 proxy; seed = 20260916 全确定性复现。

## 7. 三件套 hash

- 本文件内容 hash: `25077d9e0f9c` —— 口径: sha256(本文件最终字节, 其中本字段 12hex 值以 "000000000000" 参与计算, 其余字段为最终值).hexdigest()[0:12], 任何人可按同口径复算核对。
- 本文件路径 hash: `8014d82e2b97` —— 口径: sha256(绝对路径 "D:\私人资料\deposon-repo\docs\V3X\V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md" utf-8).hexdigest()[0:12]。
- 锚 hash: `03c6c01f3697` —— sha256(verifier/handoff/KT_ABC1_anchors_sha256_12.json 字节).hexdigest()[0:12], 与基线 file_hashes 一致。

## 8. 合规声明

0 LLM; 18 frozen + P-G V0/V0.1 + verifier/v1..v35 既有文件 + 旧 runs 链 + 任何既有文档 0 触动 (仅新建, 自查见返回声明); 全文数字可溯源到上述结果 JSON 与 runner stdout; 未使用禁用术语与任何密钥形态字符串。
