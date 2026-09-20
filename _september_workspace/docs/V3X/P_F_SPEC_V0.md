# P-F 可验证审计 SPEC V0 草稿(模型指纹 + 透明审计)

> **作者**: Mavis(执行线,Worker-P-F 子代理撰写)
> **日期**: 2026-09-09
> **状态**: V0 草稿(待 D1 改 P-F 调研 V0.1 + 5 BOSS URL 落地后升级)
> **位置**: `docs/V3X/P_F_SPEC_V0.md`
> **关联**:
> - v3 提案 §6(王老师致,2026-09-04,4 页 PDF)Phase 0 一周判死承诺 6 方向之第 5 备选
> - Mavis 内部 `QUICK_KILL_6_DIRECTIONS.md` V0.2 方向 6 + BOSS-F1~F5
> - Mavis 内部 `P_F_RESEARCH_2026_09_09.md` V0 调研稿(本任务配套)
> - 7 条铁律(双审、API key 不入 prompt、术语红线、数字溯源、verifier 纪律、预登记、推送策略)

---

## 0. 元信息与启动条件(必读)

### 0.1 P-F 是什么 / 不是什么

P-F = **模型指纹 + 透明审计方向**。V0 主指标 = 在 deposon 散射层 + IMMACULATE 风格可验证计算(VC)联合下,GSM8K / StrategyQA 等任务的 accuracy-perf-cost 是否比"单 deposon"或"单 IMMACULATE"提升 >5pp(任一)。

P-F **不是**:
- ❌ P-D 指纹的替代(P-D 已 PASS 抵御 3 BOSS,见 QUICK_KILL_6_DIRECTIONS.md 方向 4;P-F 是 P-D 的扩展层,不是替代)
- ❌ "用密码学替代守恒律"(P-F 与 P-A 守恒律**正交**,P-F 关注可验证性,P-A 关注稳定性)
- ❌ 立即启动的 V3X 方向(见 §0.2 启动条件)

### 0.2 启动条件(P-F V0 仅"预登记" 不"启动")

P-F **不**与 P-A / P-B / P-C / P-D 并行 1 周判死。P-F 启动必须先满足:
- ✅ P-A / P-B / P-C / P-D 4 方向中**至少 3 个 FAIL / BOSS 撞上 / 主动放弃**
- ✅ 王老师新指令(若王老师主动指定 P-F 优先,则此条件豁免)
- ✅ P-F 调研 V0.1 落地(5 BOSS 各 ≥ 2 个可访问 URL 补查完成)
- ✅ IMMACULATE GitHub 仓库可访问性验证通过
- ✅ D1 reviewer-a 静态审通过

**当前状态(2026-09-09)**: P-A / P-B / P-C / P-D **均在跑**,P-F 启动条件未触发。本文是 P-F V0 预登记 + 调研 + SPEC,**不**触发 1 周判死。

### 0.3 §0.5 BOSS 测法节(沿用 7 条铁律,5 BOSS 路径 + SHA 占位 + 测法占位)

> **本节为占位, D0 末 / D1 由 successor 子代理算 5 BOSS 测法脚本的 SHA-256 前 12 位, 写入 `verifier/handoff/P_F_PREDECISION_2026_09_09.json`**。

| 锚 ID | 对象 | 算法 | SHA-256[0:12](占位) |
|---|---|---|---|
| `PF_BOSS_01_fingerprint` | `boss_f1_model_fingerprinting.py`(测法占位) | SHA-256 全文 → 前 12 位 | `<TO_BE_FILLED>` |
| `PF_BOSS_02_tee` | `boss_f2_tee_sgx.py`(测法占位) | SHA-256 全文 → 前 12 位 | `<TO_BE_FILLED>` |
| `PF_BOSS_03_merkle` | `boss_f3_merkle_inference_log.py`(测法占位) | SHA-256 全文 → 前 12 位 | `<TO_BE_FILLED>` |
| `PF_BOSS_04_zkml` | `boss_f4_zkml.py`(测法占位) | SHA-256 全文 → 前 12 位 | `<TO_BE_FILLED>` |
| `PF_BOSS_05_cot` | `boss_f5_cot_transparency.py`(测法占位) | SHA-256 全文 → 前 12 位 | `<TO_BE_FILLED>` |

5 锚 SHA-256 闭环纪律:**任一锚漂移 → 全 P-F 撤回**(沿用 P-D V0.1.2 纪律)。

---

## 1. 简介(P-F 是什么 / 与 P-A-D 关系)

### 1.1 P-F 主张

P-F 主张 = **deposon 散射层 + IMMACULATE 风格可验证计算(VC) + TEE 远程认证 + CoT 公开 的"四源联合"比任一单源在 100-200 节点 GSM8K / StrategyQA 上 accuracy-perf-cost 提升 >5pp**。

- 主张分两半:
  - **前半**: deposon + IMMACULATE 联合 > 单 deposon(这是 P-F 必须 1 周判死的核心)
  - **后半**: + TEE / CoT 是否进一步提升(可选项,1 周可只跑前半)

### 1.2 与 P-A-D 关系

(沿用 `P_F_RESEARCH_2026_09_09.md` §1.3 表格 + P-D P1 教训 + V1 六关键词规则撞 BOSS 经验)

- **与 P-D(已 PASS)**: P-D 是 P-F 的"指纹基线",P-F 复用 P-D 5 锚 SHA-256 闭环 + 1% 开销,只在 P-D 基础上加 TEE / VC / CoT 三个新维度。
- **与 P-A / P-B / P-C**: P-F 不依赖动力学(P-A)/ 保真度(P-B)/ 相变(P-C);P-F 关注可验证性。
- **与 LLM 议价**: 不直接相关。

---

## 2. 任务族划分(建议 4 任务族:指纹 / 黑盒 / 透明 / 协议)

| 任务族 | ID | 内容 | 与 P-F BOSS 关系 |
|---|---|---|---|
| **指纹族** | T1 | 模型指纹识别(被动 + 水印) | 直接对 BOSS-F1 测法 |
| **黑盒族** | T2 | 黑盒审计(无密码学 / 硬件辅助,只统计输出) | 间接对 BOSS-F3 Merkle 日志 + BOSS-F4 ZKML 测法 |
| **透明族** | T3 | 透明审计(CoT 公开 + 探针 + 电路分析) | 直接对 BOSS-F5 CoT 测法 |
| **协议族** | T4 | 协议层审计(TEE 远程认证 + 密码学 VC) | 直接对 BOSS-F2 TEE 测法 + BOSS-F4 ZKML 测法 |

**任务族设计理由**:
- 4 任务族 × 4 玩家(LLM × 3 类 verifier) = 16 cells(轻量级,1 周可跑完)
- 任务族与 BOSS 一一对应,便于 1 周判死时 BOSS 测法直接复用 harness
- 不引入 P-A 22 受控概念图(那是 P-A V0 spec §2 资产,P-F 不消费)

---

## 3. 主实验设计(目标 200-300 cells,与 P-A 22 受控概念图同量级)

### 3.1 玩家

- **LLM 玩家**: Doubao(volces_ark_bytedance)+ DeepSeek,沿用 `tools/llm_client.py`(P-A V0 spec §3.1)
- **3 类 verifier 玩家**:
  - V1: IMMACULATE 风格 VC verifier(密码学)
  - V2: TEE 远程认证 verifier(硬件)
  - V3: CoT 公开 + 探针 verifier(透明)

### 3.2 机制(3 个)

- **M1: deposon + VC + TEE + CoT 联合(全开)**
- **M2: deposon + VC 联合(无 TEE,无 CoT)**——P-F 主张的"最小核心"
- **M3: 单 deposon(基线)**

> 测法思路: 比较 M2 vs M3 是否 >5pp(主张前半成立)。若成立,再比较 M1 vs M2(主张后半)。

### 3.3 任务族(4 个,见 §2)

### 3.4 数据集

- 100-200 节点 GSM8K(沿用 v19 冻结管线)+ 100-200 节点 StrategyQA(沿用 v20_gt)
- **不引入新数据集**(沿用 P-D "不新增冻结工件" 纪律)

### 3.5 总 cell 数量

3 机制 × 4 任务族 × 25 决策/任务 = **300 cells**(沿用 P-A V0 spec §3.3 同量级)

### 3.6 收敛判据

- **联合 PASS**: accuracy-perf-cost 提升 >5pp(任一机制对 vs 基线)
- **联合 FAIL**: ≤5pp
- **GRAY**: 1-5pp 灰区,扩 cell(n=300 → n=900)重判

---

## 4. 5 BOSS baseline 占位脚本(每个 200-500 行,NotImplementedError)

### 4.1 占位脚本清单(本任务不实现,只占位)

> **本节为占位, 1 周判死 D2 由 data 子代理实现, 当前阶段 `boss_fX_*.py` 仅含 NotImplementedError**。

```python
# .mavis/scripts/p_f/boss_f1_model_fingerprinting.py
"""
P-F BOSS-F1: model fingerprinting baseline
- 测法: 跑 model fingerprinting baseline (DeepMind 2022 / Google 2023)
- 数据: 100-200 节点 GSM8K + StrategyQA
- 指标: accuracy-perf-cost vs deposon+IMMACULATE 联合
- 沿用 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F1 测法
"""
import sys
def main() -> int:
    raise NotImplementedError("P-F BOSS-F1: D2 由 data 子代理实现")
if __name__ == "__main__":
    sys.exit(main())
```

```python
# .mavis/scripts/p_f/boss_f2_tee_sgx.py
"""
P-F BOSS-F2: TEE/SGX/SEV-SNP/H100 CC 测法
- 测法: TEE-only 方案 vs deposon+IMMACULATE 联合, 5pp 优势是否还在
- 沿用 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F2 测法
- 注意: Intel SGX 已退出服务器市场 (2023), 实测需用 AMD SEV-SNP 或 NVIDIA H100 CC
"""
def main() -> int:
    raise NotImplementedError("P-F BOSS-F2: D2 由 data 子代理实现")
```

```python
# .mavis/scripts/p_f/boss_f3_merkle_inference_log.py
"""
P-F BOSS-F3: Merkle 推理日志 (vLLM/SGLang 现成)
- 测法: 跑 vLLM 推理日志 + 简单哈希链, 看是否 1% 开销 + 95% 审计率
- 沿用 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F3 测法
"""
def main() -> int:
    raise NotImplementedError("P-F BOSS-F3: D2 由 data 子代理实现")
```

```python
# .mavis/scripts/p_f/boss_f4_zkml.py
"""
P-F BOSS-F4: ZKML (Modulus Labs / EZKL)
- 测法: 跑 EZKL 证明 LLaMA-7B 单步推理, 对比证明时间 + accuracy
- 沿用 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F4 测法
"""
def main() -> int:
    raise NotImplementedError("P-F BOSS-F4: D2 由 data 子代理实现")
```

```python
# .mavis/scripts/p_f/boss_f5_cot_transparency.py
"""
P-F BOSS-F5: CoT 透明审计
- 测法: 跑 CoT 公开 baseline, 看审计准确率是否 >= 95%
- 沿用 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F5 测法
- 注意: 7 条铁律 "术语红线" 禁止 "承诺装置" 等比喻, 严守工程术语
"""
def main() -> int:
    raise NotImplementedError("P-F BOSS-F5: D2 由 data 子代理实现")
```

5 个占位脚本在 P-F V0 草稿期全部 NotImplementedError,D2 由 data 子代理实现。

### 4.2 5 BOSS 测法映射(沿用 QUICK_KILL_6_DIRECTIONS.md V0.2)

| BOSS ID | QUICK_KILL 测法 | P-F V0 复现 | 预期判死 |
|---|---|---|---|
| **BOSS-F1** | model fingerprinting baseline | `boss_f1_model_fingerprinting.py` | 看 5pp 优势是否被拍平 |
| **BOSS-F2** | TEE-only 方案 vs deposon+IMMACULATE | `boss_f2_tee_sgx.py` | 看 5pp 优势是否输给硬件 |
| **BOSS-F3** | vLLM 推理日志 + 简单哈希链 | `boss_f3_merkle_inference_log.py` | 看 1% 开销 + 95% 审计率是否被拍平 |
| **BOSS-F4** | EZKL 证明 LLaMA-7B 单步推理 | `boss_f4_zkml.py` | 看证明时间 + accuracy |
| **BOSS-F5** | CoT 公开 baseline | `boss_f5_cot_transparency.py` | 看审计准确率 ≥ 95% |

**5 BOSS 任何 1 个 PASS = P-F 主张降级**(与 V1 六关键词规则同款逻辑)。

---

## 5. 判死标准(类比 P-A cost_mult 1.3× / P-B 攻击成功率 50%)

### 5.1 P-F 判死标准(accuracy-perf-cost 5pp)

- **PASS**: M2(deposon+IMMACULATE 联合) vs M3(单 deposon) 提升 >5pp,**且** M1(全开) vs M2 进一步提升 >0pp(可选项)
- **FAIL**: M2 vs M3 提升 ≤1pp
- **GRAY**: 1-5pp 灰区,扩 cell 重判

### 5.2 类比 P-A / P-B 判死标准

- **P-A 判死**: cost_mult ≤ 1.3× = PASS, ≥ 2.0× = FAIL(P-A V0 spec §1)
- **P-B 判死**: 攻击成功率 ≥ 50% = BOSS PASS, ≤ 30% = BOSS FAIL
- **P-F 判死**: 5pp accuracy-perf-cost 提升 = PASS, ≤ 1pp = FAIL

### 5.3 判死线 SPEC 冻结纪律

- SPEC 文本先于运行冻结(2026-09-09 V0 草稿; D1 改 P-F 调研 V0.1 + 本 SPEC §1.2 启动条件细化)
- 5 锚 SHA-256 前 12 位在 P-F 启动 D1 由 successor 子代理算
- 任何 ≥ 1 锚漂移 → 全 P-F 撤回

---

## 6. 锚占位(5 个 SHA-256 前 12 位,占位,实现时算)

> **本节为占位, P-F 启动 D1 由 successor 子代理算 5 锚 SHA-256 前 12 位**。

| 锚 ID | 对象 | 字段 | SHA-256[0:12](占位) |
|---|---|---|---|
| `PF_F1_FINGERPRINT` | `boss_f1_model_fingerprinting.py` | `version=2026-XX-XX` | `<TO_BE_FILLED>` |
| `PF_F2_TEE` | `boss_f2_tee_sgx.py` | `version=2026-XX-XX` | `<TO_BE_FILLED>` |
| `PF_F3_MERKLE` | `boss_f3_merkle_inference_log.py` | `version=2026-XX-XX` | `<TO_BE_FILLED>` |
| `PF_F4_ZKML` | `boss_f4_zkml.py` | `version=2026-XX-XX` | `<TO_BE_FILLED>` |
| `PF_F5_COT` | `boss_f5_cot_transparency.py` | `version=2026-XX-XX` | `<TO_BE_FILLED>` |

**说明**: 5 锚对应 5 BOSS 测法脚本,沿用 Mavis 内部"测法即锚"纪律(P-D 5 锚 = 5 锚工件, P-F 5 锚 = 5 测法脚本)。

---

## 7. 数据源(frozen JSON 同 P-A)

- **GSM8K 100-200 节点**: 沿用 v19 冻结管线 `results/deposon_v19_benchmark_fixes.json`
- **StrategyQA 100-200 节点**: 沿用 v20_gt frozen run
- **不引入新数据集**(沿用 P-D "不新增冻结工件" 纪律)

---

## 8. 与王老师 / BPA / 7 铁律关系

### 8.1 王老师 = WeChat 顾问模式(沿用 V3X 锚定)

- D1 / D3 / D5 报告各 5-10 min/周 内可读
- 王老师不主动推,等他回(沿用 7 铁律"推送策略")
- P-F 启动决策由王老师 ack(他回"启动 P-F" 即可,无需长答复)

### 8.2 BPA(Best Practice Alternative)

- 沿用 Mavis 内部 `BPA_PILOT_2026_09_09_mavis.md` V0 模板
- D6 出 BPA 报告给王老师

### 8.3 7 条铁律兼容

- ✅ **双审**: P-F V0 草稿待 D1 reviewer-a 静态审
- ✅ **API key 不入 prompt**: D2 实现 step 才读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt`;V0 草稿期不读
- ✅ **术语红线**: 用"指纹 / 透明 / TEE / 零知识 / CoT / 散射层 / 守恒" 等工程术语,**不**用"承诺装置" 等比喻
- ✅ **数字溯源**: P-F 主张用 ">5pp accuracy-perf-cost" 通用表达,具体数字待 D2 实测
- ✅ **verifier 纪律**: §10 复现协议用 /tmp 副本
- ✅ **预登记**: §6 5 锚先冻结 SHA-256 前 12 位
- ✅ **推送策略**: 不主动发,等 D0 末群内公布

---

## 9. 1 周预筛时序(D1-D7, 启动后)

> **本节仅在 P-F 启动后适用, 当前 V0 草稿期 P-F 未启动**。

- **D1**: P-F 调研 V0.1 落地(5 BOSS 各 ≥ 2 个 URL)+ 5 锚 JSON 落地 + IMMACULATE GitHub 可访问性验证
- **D2**: 实现 4 任务族 harness + 5 BOSS baseline 真实现(pilot 5 cell)
- **D3**: pilot 50 calls 跑通 + D3 WeChat 1(王老师 ack)
- **D4**: 全 300 calls + 5 BOSS 测法全部跑通
- **D5**: reviewer-b 判死 + 5 攻击 + 5 BOSS 测法裁定
- **D6**: 失败模式处理 / GRAY 扩 cell / 若 5 BOSS 测法全 PASS 则 P-F 方向 PASS
- **D7**: 一页摘要(对外, 给王老师)+ 完整中文判死报告(内部)+ BOSS 测法结果回写到 QUICK_KILL_6_DIRECTIONS.md V0.3

---

## 10. 已知边界与陷阱(沿用 P-D P1 教训)

### 10.1 P-D P1 教训(必须避开)

- **A1 攻击脚本诱导操作者删除冻结锚**:P-F 5 BOSS 测法**必须**无参 + 临时副本,绝不触碰真实仓库 5 锚
- **A1/A2/A3 命令模板与 spec §6 衔接缺口**:P-F 5 BOSS 测法命令统一用 `python .mavis/scripts/p_f/boss_fX_*.py` 直跑(沿用 P-D V0.1.2 修复模式)
- **Windows PowerShell 兼容**:路径用 `\` 或 `pathlib`,不依赖 bash

### 10.2 P-F 特有陷阱

- **IMMACULATE GitHub 依赖**:D1 必须先验证可访问性,若不可访问,P-F 主张前半(M2 vs M3)无法测
- **EZKL 大模型证明时间**:LLaMA-7B 单步推理证明时间可能数分钟到数十分钟,1 周预算需先 pilot 测一次
- **TEE 硬件依赖**:TEE 远程认证需要 verifier 与 enclave 厂商建立信任根,跨厂商验证是工程难题
- **CoT 事后合理化**(沿用 THINKING_V3 Q5'): CoT 公开可能被策略性智能体操纵,P-F 主张应**避免** "CoT 透明 = 审计完备" 的过度承诺

### 10.3 4 条禁示条款(沿用 KT-A1 V0 §4.4)

- ❌ **不得**只跑 P-F §3 实验而跳过 5 BOSS baseline(防 V1 撞 BOSS 重演)
- ❌ **不得**在 5 BOSS 测法跑通前宣称 P-F PASS(防 P-D P1 复现: 判死过早)
- ❌ **不得**在真实仓库跑 5 BOSS baseline(必须 /tmp 副本)
- ❌ **不得**让 5 BOSS 测法脚本诱导操作者删除 §6 预登记 5 锚(无参 + 临时副本)

---

## 11. 7 条铁律兼容表(7 项全展开)

| 铁律 | P-F V0 自检 | 状态 |
|---|---|---|
| **双审** | P-F V0 草稿待 D1 reviewer-a 静态审 + P-F 启动后 reviewer-b /tmp 副本审 | ✅ 占位 |
| **API key 不入 prompt** | D2 实现 step 才读 API key,V0 草稿期不读 | ✅ 占位 |
| **术语红线** | 全程用"指纹 / 透明 / TEE / 零知识 / CoT / 散射层 / 守恒" 等工程术语,严守 7 铁律"承诺装置" 禁令 | ✅ |
| **数字溯源** | P-F 主张用 ">5pp accuracy-perf-cost" 通用表达,具体数字待 D2 实测;所有引用数字均带 §N 标号 | ✅ |
| **verifier 纪律** | §10 复现协议用 /tmp 副本,不碰真实仓库 | ✅ |
| **预登记** | §6 5 锚先冻结 SHA-256 前 12 位(占位,实现时算) | ✅ 占位 |
| **推送策略** | 不主动发,等 D0 末群内公布 + 王老师 WeChat 通知 | ✅ |

---

## 12. 已知未决项(10 项,沿用 P-A V0 spec §9 模式)

1. **数据集大小**: 100-200 节点 vs 200-300 节点?待 D1 调研 IMMACULATE 原始 benchmark 规模后定
2. **5 BOSS 测法细化**: 每个 BOSS 的具体阈值(>5pp / 1% 开销 / 95% 审计率 / 证明时间)待 D2 实测
3. **5 锚算锚时机**: P-F 启动 D1 算, V0 草稿期不写死(沿用 P-D V0.1.2 纪律)
4. **王老师三问**: P-F 启动决策需王老师 ack,他回"启动 P-F" 即可
5. **reviewer-b 路径**: /tmp 副本 vs 原仓库复跑?沿用 P-D V0.1.2 模式用 /tmp 副本
6. **GRAY 扩 cell**: 1-5pp 灰区扩 cell 数量(n=300 → n=900?)?待 D2 pilot 跑后定
7. **攻击**: P-F 5 BOSS 测法本身的抗攻击(防 IMMACULATE GitHub 仓库被替换)? 待 D1 调研
8. **D7 摘要**: 对外 1 页摘要 vs 内部 10-15 页判死报告,沿用 P-A V0 spec §8 双报告模式
9. **商用**: P-F 5 BOSS 测法商业可用性(EZKL 是否商用免费?)?待 D1 调研
10. **BOSS 回写**: 1 周判死 PASS/FAIL 后回写到 QUICK_KILL_6_DIRECTIONS.md V0.3,沿用 P-A V0 spec §10 D7 节奏

---

## 13. Self-Review(自审记录)

**V0 草稿自审 1 遍, 逐节核查**:
- ✅ §0 元信息 + 启动条件(必须 P-A-D 至少 3 个 FAIL)+ §0.5 BOSS 测法节
- ✅ §1 简介 + 与 P-A-D 关系明确
- ✅ §2 任务族 4 任务族(指纹 / 黑盒 / 透明 / 协议),与 5 BOSS 一一对应
- ✅ §3 主实验 300 cells,3 机制 × 4 任务族 × 25 决策,类比 P-A 22 受控概念图
- ✅ §4 5 BOSS baseline 占位脚本(5 个 NotImplementedError,各 200-500 行结构)
- ✅ §5 判死标准 5pp accuracy-perf-cost
- ✅ §6 5 锚占位待 P-F 启动 D1 填入
- ✅ §7 数据源沿用 v19 / v20_gt,不引入新数据集
- ✅ §8 王老师 WeChat 模式 + BPA + 7 铁律
- ✅ §9 1 周预筛时序 D1-D7(启动后)
- ✅ §10 已知边界与陷阱(沿用 P-D P1 教训 + P-F 特有陷阱)
- ✅ §11 7 铁律兼容表
- ✅ §12 已知未决项 10 项
- ✅ §14 引用与版本

**未发现冲突**: 与 P-A V0 spec / QUICK_KILL_6_DIRECTIONS.md V0.2 全部兼容。

**待 P-F 启动 D1 由 Mavis 完成**: 5 锚 SHA-256 前 12 位实际计算,写入 `verifier/handoff/P_F_PREDECISION_2026_09_09.json`。

---

## 14. 引用与版本

- **v3 提案**: 《Deposon × 王子贺老师 合作提案》(2026-09-04, 4 页 PDF, 致: 王子贺 人大高瓴人工智能学院)
- **Mavis 内部**:
  - `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2(方向 6 P-F + BOSS-F1~F5)
  - `docs/V3X/P_F_RESEARCH_2026_09_09.md` V0(本任务配套调研)
  - `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` V0.1.2(P-D 已 PASS 模式, 5 锚纪律 / 抗攻击纪律)
  - `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` V0.2(双判死线双跑 + §0.5 BOSS 测法节)
  - `docs/V3X/KT_A1_SPEC_V0.md` V0.2(双判死线 + 300 cells + BOSS 测法结构模板)
  - `docs/THINKING_V3_GT_CONTRIB_2026.md` Q5(硬惩罚冲突) + Q5'(CoT 事后合理化) + Q-C1(守恒≠真值)
  - `verifier/handoff/KT_ABC1_anchors_sha256_12.json`(15 锚 JSON 模式参考)
- **外部**(本 SPEC **不**直接引用任何具体 arXiv 编号 / 论文标题——见 `P_F_RESEARCH_2026_09_09.md` §0.1 诚实声明,所有外部引用待 D1 补查):
  - IMMACULATE GitHub: `https://github.com/guo-yanpei/Immaculate` [来源:QUICK_KILL_6_DIRECTIONS.md]
  - EZKL / Modulus Labs / vLLM / SGLang / Anthropic interpretability [来源:同上,具体 URL 待 D1 补查]

---

## 15. V0 → V0.1 升级记录(2026-09-09)

- **V0 草稿**:
  - §0 启动条件明确(P-A-D 至少 3 个 FAIL 才启动)
  - §0.5 BOSS 测法节占位 5 锚
  - §1 简介 + 与 P-A-D 关系
  - §2 4 任务族(指纹 / 黑盒 / 透明 / 协议)
  - §3 300 cells 主实验设计
  - §4 5 BOSS baseline 占位脚本(NotImplementedError)
  - §5 判死标准 5pp accuracy-perf-cost
  - §6 5 锚占位
  - §7 数据源沿用 v19 / v20_gt
  - §8 王老师 + BPA + 7 铁律
  - §9 1 周预筛时序
  - §10 已知边界与陷阱
  - §11 7 铁律兼容表
  - §12 已知未决项 10 项
  - §14 引用与版本
- **触发**: 用户派 P-F 方向 worker 子代理启动预登记
- **下次升级触发**:
  - P-F 启动 D1(P-A-D 至少 3 个 FAIL / 王老师新指令)+ 5 锚 JSON 落地
  - P-F 调研 V0.1 落地(5 BOSS 各 ≥ 2 个可访问 URL)
  - P-F 1 周判死 PASS/FAIL 后,回写 5 BOSS 实测结果到 QUICK_KILL_6_DIRECTIONS.md V0.3

---

**P-F SPEC V0 草稿结束, 待 P-A-D 4 方向至少 3 个 FAIL / 王老师新指令后才进入 V0.1 + 1 周判死。**
