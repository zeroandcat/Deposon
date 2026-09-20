# KT-B1 Option A 返工修复总结报告

> **日期**: 2026-09-10  
> **执行方**: orchestrator（独立复跑+验收）  
> **任务来源**: 工单#14 Option A 打回补齐真 T+R+A 重算检测器 + 75 攻击测试  
> **范围**: P0 真守恒重算检测器 → P2 BOSS-B 管线 → P3/P4 BOSS-A/KT-C 验证  

---

## 一、任务背景

用户派单要求 data 子代理按 Option A 执行返工：将 conservation.py 从"仅查顶层锚"升级为"真 T+R+A 重算 + 审计链账本交叉对账"，并补齐 75 攻击测试。返工交付后由 orchestrator 独立复跑验收，验收中发现并修复了交付质量问题与未报告的 BOSS 漂移。

---

## 二、修复清单（共 9 文件）

### P0：conservation.py + audit_full.py（orchestrator 修 3 bug）

| # | 文件 | bug | 根因 | 修复 |
|---|---|---|---|---|
| 1 | `verifier/audit/conservation.py` | **语法错误**（line 391 `{` never closed） | data 子代理交付时 `_mini_dataset()` 的 FORM_A 闭合括号数不足（3 个 `}` 应为 4 个），且混入尾随单引号残渣 | 补齐闭合括号 `]}}}},` |
| 2 | `verifier/audit/conservation.py` | **v19 真件自检误报 FAIL**（18 条误报） | `_check_record` 把 `pv is None`（值为 None）当作"字段不存在"；v19 有 18 条合法 `predicted=None` 记录，自检时原件有该字段 → 误判为"被删" | 改为 `has_pred_field` 标志位，区分"键不存在"与"值为 None" |
| 3 | `C:\tmp\...\kt_b1\audit_full.py` | **75 攻击 seed 伪造独立性** | 5 cells 全用 harness 默认 `seed=42`，75 攻击实为 25 独立+50 复读，违背"5 次独立重复实验（每次不同随机种子）"定义 | 每 cell 用 `seed=42+cell_idx`（42..46）；同时 import 从 /tmp 冻结旧栈改为主仓返工栈 |

**验收证据**：
- conservation.py `--test_edge_cases`：16/16 PASS，零异常，v19 真件 1592 条自检 PASS（layer1_dev=2.22e-16）
- 75 攻击：攻击者成功 16/75 = 21.3% < 50% → PASS（各 cell 因独立 seed 呈现真实波动 11/15~13/15）
- 600 攻击主实验：攻击者成功 135/600 = 22.5% < 50% → PASS
- 分型抓出率：deletion 100%、manifest_swap 100%、chain_modify 32.5~36%（SPEC §3.3 预期带 30-60% 内，非盲点）

### P2：BOSS-B1/B2/B3 loader（orchestrator 发现并修复未报告漂移）

**发现过程**：锚 JSON 全量核验时发现 3 个 BOSS-B 脚本 SHA-12 与锚值不一致。/tmp 冻结快照（reviewer-b 原始跑）SHA = 锚值 → 漂移发生在快照之后。diff 显示统一把 `predicted` 硬改名为 `pred`。

**根因分析**：v19 有两种记录形态——gsm8k 用 `predicted`/`best_path`（800 条），strategyqa 用 `pred`/`path`（792 条）。有人做了半吊子修复：只改了 strategyqa 的 `pred`，却把 gsm8k 的 `predicted` 读取全丢失（`p.get("pred", 0.0)` 在没有 `pred` 键时返回默认值 0.0）。且三个脚本从未在真实 v19 上跑通过：

- gsm8k `predicted` 有 12 条值为 None → 快照原版 `float(p.get("predicted", 0.0))` 遇 None 会 TypeError 崩溃（`get` 返回 None 而非默认值）
- strategyqa `pred` 是字符串 'Yes'/'No' → 漂移版 `float(p.get("pred", 0.0))` 遇字符串会 ValueError 崩溃
- strategyqa `answer` 实测全为 None → 任何版本 `float(None)` 必崩

| # | 文件 | 修复内容 |
|---|---|---|
| 4 | `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` | loader 双形态回退 + None/字符串容错 |
| 5 | `.mavis/scripts/kt_b1/boss_b2_kd.py` | 同上 |
| 6 | `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` | 同上 |

**统一修复模式**（3 文件同一套）：
```python
def _norm_pred(v) -> float:
    """v19 双形态预测值归一化（不 clamp——BOSS 分布需保留原始量级/负值，gsm8k min=-2.5e14）"""
    # None→0.0; bool→1.0/0.0; 数值原样; 'yes'→1.0/'no'→0.0; 数值串→float; 非法→0.0

def _to_float(v) -> float:
    """数值字段容错（strategyqa answer 实测全 None）"""

# 记录构建:
"pred": _norm_pred(p.get("pred", p.get("predicted", 0.0))),
"answer": _to_float(p.get("answer", 0.0)),
"best_path": list(p.get("best_path", p.get("path", []))),
```

**冒烟证据**：995 条（500+495）逐项核对——gsm8k 零值恰好 12 条（None 记录）、strategyqa 零值恰好 250 条（'No' 语义映射）、gsm8k 负值 32 条保留（未 clamp），全部与实测分布吻合，零崩溃。

### P3/P4：BOSS-A1/A2/A3 + KT-C1（未修改，管线验证）

| # | 文件 | 状态 |
|---|---|---|
| 7 | `.mavis/scripts/kt_a1/boss_a1_rbr_rm.py` | 未改，管线跑通 |
| 8 | `.mavis/scripts/kt_a1/boss_a2_potential_game.py` | 未改，管线跑通 |
| 9 | `.mavis/scripts/kt_a1/boss_a3_replicator_dynamics.py` | 未改，管线跑通 |
| - | `.mavis/scripts/kt_c1/harness.py` | 未改，管线跑通 |

---

## 三、管线级验证结果（全 8 脚本首次跑通）

### BOSS-B1/B2/B3（修复后首次跑通）

| 脚本 | 失真上界 | deposon 基线 | 裁定 | 耗时 |
|---|---|---|---|---|
| B1 Sinkhorn OT | 0.0004 | 0.5（占位） | GRAY_BOTH_BELOW | ~10 min |
| B2 KD | 0.0028 | 0.5（占位） | GRAY_BOTH_BELOW | <1 min |
| B3 LLMLingua | 0.4634 | 0.05（占位） | GRAY_BOTH_ABOVE | <1 min |

无 FAIL（通用基线未跑赢 deposon）。三个裁定全为 GRAY 是预期行为——deposon 失真上界是占位值。

### BOSS-A1/A2/A3（未改，首次跑通）

| 脚本 | 关键指标 | 裁定 |
|---|---|---|
| A1 RBR/RM | 成本倍数 RBR=22x、RM=4400x（>>2.0） | DIFFERENTIATED |
| A2 Potential Game | 22/22 图全为势博弈，H1 证明成立 | H1 降级（工程化路径） |
| A3 Replicator+ESS | Hamming 均距 0.6874（>0.30），ESS 0/22 | DIFFERENTIATED |

A1+A3 差异化、A2 降级——三者交叉与项目既有定性一致。

### KT-C1 harness（未改，首次跑通）

| 指标 | 结果 |
|---|---|
| 主（loglog fit） | R²=0.0007 < 0.3 → **DEAD**（slope=0.284, b_CI 含 0） |
| η 扫描 | eta_crit_05=0.333, eta_crit_03=0.778 |
| BOSS-C1 (2D Ising) | diff 0.88% < 20% → **FAIL（拍平）** |
| BOSS-C2 (Transverse) | diff 67.9% → **PASS（抵御）** |
| BOSS-C3 (Reservoir) | 非双稳态 → **PASS（抵御）** |

与锚 JSON 自检标注完全一致。

---

## 四、SHA-12 变更总表

### 返工涉及文件（锚旧值 → 当前）

| 文件 | 锚(旧) | 当前 | 说明 |
|---|---|---|---|
| `verifier/audit/conservation.py` | `3aa661cfbab5` | `4bdec2683f06` | V0.3 返工 + 修 2 bug |
| `.mavis/scripts/kt_b1/attacker.py` | `4b37a40cc984` | `dc78f9a89b1c` | data 子代理返工 |
| `.mavis/scripts/kt_b1/harness.py` | `39dacb572f2e` | `3bcd1b03e4fd` | data 子代理返工 |
| `tools/llm_client.py` | `055e874ea5c1` | `1722500da4aa` | 返工 5 文件之一 |
| `tools/exp_harness.py` | `9f383935c00c` | `275e480ba4d9` | 返工 5 文件之一 |
| `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` | `19325960b8be` | `7c2b41c008a5` | 漂移修复 |
| `.mavis/scripts/kt_b1/boss_b2_kd.py` | `1781ea2f742d` | `8c6e98034005` | 漂移修复 |
| `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` | `c0b55e0385a4` | `2ded5cf0e863` | 漂移修复 |
| `/tmp audit_full.py` | `bc0fb1620bec` | `fff5ab62a68c` | seed 独立性修复 |

### 冻结区核验（28 项锚）

| 类别 | MATCH | DIFF | MISSING |
|---|---|---|---|
| KT-A1 锚（5） | 3 | 2（llm_client + exp_harness 合法返工） | 0 |
| KT-B1 锚（5） | 2 | 3（attacker + harness + conservation 合法返工） | 0 |
| KT-C1 锚（5） | 5 | 0 | 0 |
| BOSS-A 基线（3） | 3 | 0 | 0 |
| BOSS-B 基线（3） | 0 | 3（漂移已查明并修复） | 0 |
| BOSS-C 基线（3） | 3 | 0 | 0 |
| 5 frozen runs（5） | 5 | 0 | 0 |
| **合计** | **21** | **8** | **0** |

8 个 DIFF 全部查明：5 个是 Option A 授权返工的合法变更，3 个是未报告的 BOSS-B 漂移（已修复）。

### 冻结区专项（绝不许动，全部 MATCH）

| 文件 | SHA-12 | 状态 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | ✅ |
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | ✅ |
| `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | ✅ |
| `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `5e99e79f2e11` | ✅ |
| `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | `ba53d73e3937` | ✅ |

---

## 五、修复的技术发现

### 5.1 v19 数据双形态（写死在认知里）

| benchmark | 预测值字段 | 值形态 | 推理链字段 | answer | trap_hit |
|---|---|---|---|---|---|
| gsm8k | `predicted` | float（min=-2.5e14，可负可>1，12 条 None） | `best_path` | float | None/str |
| strategyqa | `pred` | str（'Yes'/'No'） | `path` | **全 None** | bool |

E9.3 总量 995 条（500+495），全 v19 1592 条（800+792）。任何只认单形态字段的 loader 都会崩——这是三个 BOSS-B 脚本从未跑通过的根本原因。

### 5.2 conservation.py tra_decomposition 与 deposon scatter() 的关系

conservation.py 的 `tra_decomposition` 是从 `pred` 值合成的守恒验和函数，不是 `deposon_agents.DeposonState.scatter()` 的真散射公式。真散射公式（`denom = 1.0 + g_eff + g_aether`，三通道严格归一化）在 `deposon_agents.py` 中，conservation.py 通过 `parse_pred` + `tra_decomposition` 间接验证守恒——对 v19 无显式 T/R/A 字段的记录，合成恒守恒，可检出信号 = NaN/inf 合成异常。这一设计在 V0.3 docstring 中已显式声明。

### 5.3 早期 DeposonState.scatter() 公式演变

前期 PDF《统一场论研究报告 v1》中的 `scatter()` 是非守恒老版（`exp(-g_aether)` 衰减 + `sqrt(1-t²-r²)` 兜底），后来收敛为当前仓库的 `denom = 1.0 + g_eff + g_aether` 三通道归一化。老包 bug 已修正，不用管包内脚本 bug。

---

## 六、遗留事项

1. **锚 JSON 本身未更新**：`KT_ABC1_anchors_sha256_12.json` 保留旧 SHA-12（历史记录），上表即替代关系报告。后续如需冻结新锚，需走正式流程更新该 JSON。
2. **BOSS-B 裁定全 GRAY**：deposon 失真上界是占位值（0.5/0.05），不标榜差异化。如需真正判定差异化，需从 v19 守恒残差（2.22e-16）反向估计 deposon 失真上界。
3. **reviewer-b 原始 75 攻击报告**：所用为 /tmp 旧栈（攻击顶层字段+弱检测器），与返工版口径不同。已在 `PHASE_B_TMP/kt_b1_audit_full_v03_rerun.json` 留档，建议在 REVIEWER_B 文档补勘误说明。
4. **600 攻击日志**：`docs/V3X/KT_B1_FULL_ATTACK_200_V0.2_20260910_095517.log`。

---

## 七、验收命令一览（可复现）

```bash
# 1. conservation 16 edge case 自检
python verifier/audit/conservation.py --test_edge_cases

# 2. 75 攻击（5 cells × 3 类 × 5，独立 seed）
python C:\tmp\review_20260909T140401\kt_b1\audit_full.py

# 3. 600 攻击主实验
python .mavis/scripts/kt_b1/harness.py  # mini 自检
# 或 run_full_attack(200) 写日志

# 4. attacker 自检
python .mavis/scripts/kt_b1/attacker.py

# 5. BOSS-B/A/C 管线
python .mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py
python .mavis/scripts/kt_b1/boss_b2_kd.py
python .mavis/scripts/kt_b1/boss_b3_llmlingua.py
python .mavis/scripts/kt_a1/boss_a1_rbr_rm.py
python .mavis/scripts/kt_a1/boss_a2_potential_game.py
python .mavis/scripts/kt_a1/boss_a3_replicator_dynamics.py
python .mavis/scripts/kt_c1/harness.py
```

所有命令需设 `$env:PYTHONDONTWRITEBYTECODE=1`（沙箱禁写系统 .pyc）。Python 3.14.7 + pypdf 6.16.2。

---

*报告生成: 2026-09-10 orchestrator*
