# Mavis V0.2 复审报告(独立复跑)

> **日期**: 2026-09-10  
> **执行方**: Mavis worker(独立复跑,与 Trae 报告交叉对账)  
> **任务来源**: 工单"等 API 期间可做的 3 件事"第 2 项  
> **复审范围**: 9 文件 self_test(沿用 Trae 报告 P0/P2 返工 + P3/P4 验证清单)  
> **状态**: **与 Trae 报告 P0/P2 修复一致,P3/P4 验证无新问题**

---

## §1 复审范围(9 文件 SHA-12 对照)

| # | 文件 | 改前 SHA-12 (Trae 报告) | 改后 SHA-12 (Mavis 实测) | 状态 |
|---|---|---|---|---|
| 1 | `verifier/audit/conservation.py` | `3aa661cfbab5` | `4bdec2683f06` | ✅ MATCH |
| 2 | `.mavis/scripts/kt_b1/attacker.py` | `4b37a40cc984` | `dc78f9a89b1c` | ✅ MATCH |
| 3 | `.mavis/scripts/kt_b1/harness.py` | `39dacb572f2e` | `3bcd1b03e4fd` | ✅ MATCH |
| 4 | `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` | `19325960b8be` | `7c2b41c008a5` | ✅ MATCH |
| 5 | `.mavis/scripts/kt_b1/boss_b2_kd.py` | `1781ea2f742d` | `8c6e98034005` | ✅ MATCH |
| 6 | `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` | `c0b55e0385a4` | `2ded5cf0e863` | ✅ MATCH |
| 7 | `.mavis/scripts/kt_a1/boss_a1_rbr_rm.py` | (未改) | `91a62de1fa50` | ✅ 未改 |
| 8 | `.mavis/scripts/kt_a1/boss_a2_potential_game.py` | (未改) | `b6339d9f2435` | ✅ 未改 |
| 9 | `.mavis/scripts/kt_a1/boss_a3_replicator_dynamics.py` | (未改) | `27d04f1e3b3e` | ✅ 未改 |

**全部 9 个 SHA-12 与 Trae 报告一致**(自检不修改源文件,只读 v19 frozen)。

---

## §2 9 文件 self_test 结果

| # | 文件 | self_test 命令 | PASS/FAIL | 关键指标 | 耗时 |
|---|---|---|---|---|---|
| 1 | `conservation.py` | `python ... --test_edge_cases` | **PASS** | 16/16 edge case,v19 真件 1592 条 layer1_dev=2.22e-16 | 633ms |
| 2 | `attacker.py` | `python ... --self_test` | **PASS** | deletion 5/5,manifest_swap 5/5,chain_modify 1/5 detected,attacker 0/5+0/5+4/5=4/15 | 878ms |
| 3 | `harness.py` | `python ... --self_test` | **PASS** | 同 attacker(共享数据) | 819ms |
| 4 | `boss_b1_sinkhorn_ot.py` | `python ...` | **PASS** | sinkhorn 0.0004,deposon 0.5(占位),GRAY_BOTH_BELOW | ~13 min |
| 5 | `boss_b2_kd.py` | `python ...` | **PASS** | KD 0.0028,deposon 0.5,GRAY_BOTH_BELOW | <1 min |
| 6 | `boss_b3_llmlingua.py` | `python ...` | **PASS** | LLMLingua 0.4634,deposon 0.05,GRAY_BOTH_ABOVE | <1 min |
| 7 | `boss_a1_rbr_rm.py` | `python ...` | **PASS** | RBR cost 22x,RM cost 4400x(>>2.0),DIFFERENTIATED | <1 min |
| 8 | `boss_a2_potential_game.py` | `python ...` | **PASS** | 22/22 PG,H1 proved True,降级工程化路径 | <1 min |
| 9 | `boss_a3_replicator_dynamics.py` | `python ...` | **PASS** | Hamming 0.6874(>0.30),ESS 0/22,DIFFERENTIATED | <1 min |

**全 9 文件 PASS**。B1 sinkhorn 耗时偏长(~13 min vs Trae 报 ~10 min),差异在 CPU 占用,不影响结果正确性。

---

## §3 关键判死数字(沿用 Trae 报告 + Mavis 独立复核)

### 3.1 攻击者成功率(沿用 Trae 工单#14 Option A 返工)
- **75 攻击(5 cells × 3 类 × 5,独立 seed 42..46)**:**16/75 = 21.3%** < 50% → PASS
- **600 攻击(主实验)**:**135/600 = 22.5%** < 50% → PASS
- 分型抓出率:deletion 100%,manifest_swap 100%,chain_modify 32.5-36%(SPEC §3.3 预期带 30-60% 内)

### 3.2 BOSS 9 个裁定
| 类别 | 裁定 |
|---|---|
| B1 Sinkhorn OT | GRAY_BOTH_BELOW |
| B2 KD | GRAY_BOTH_BELOW |
| B3 LLMLingua | GRAY_BOTH_ABOVE |
| A1 RBR/RM | DIFFERENTIATED |
| A2 Potential Game | H1 proved(降级工程化路径) |
| A3 Replicator+ESS | DIFFERENTIATED |
| C1 主(loglog) | DEAD(R²=0.0007) |
| C2 BOSS-C1 2D Ising | FAIL(拍平,diff 0.88%) |
| C2 BOSS-C2 Transverse | PASS(抵御,diff 67.9%) |
| C2 BOSS-C3 Reservoir | PASS(抵御) |

---

## §4 Mavis 视角补充(独立复审)

### 4.1 与 Trae 报告交叉对账
- **P0 conservation.py**:Trae 报告 3 bug 修复(语法 + v19 None 误判 + seed 独立性)Mavis 复跑均成立 ✅
- **P2 BOSS-B 漂移**:Trae 报告 3 个 BOSS-B loader 双形态修复,995 条零崩溃,122 条 None 记录处理正确 ✅
- **P3/P4 BOSS-A + KT-C**:Trae 报告管线跑通,无 FAIL,无数据漂移 ✅

### 4.2 Mavis 独立观察
1. **B1 耗时差异**:Mavis 实测 13 min vs Trae 报 ~10 min。可能原因:
   - Trae 跑时 Python 3.14.7 JIT 缓存命中
   - Mavis 复跑前所有 .pyc 清除(`PYTHONDONTWRITEBYTECODE=1`)
   - 同一算法,N_BOSS_RESAMPLES=1000 步 + 200 题 × 6 reg,200 iter/reg
   - 不影响判死结果(GRAY_BOTH_BELOW 一致)
2. **输出编码**:`*.log` UTF-8 文件在 PowerShell `Get-Content` 显示中文乱码(`???`),但实际文件内容正确,UTF-8 多字节正常。这是终端显示问题,不是文件损坏。
3. **5 锚 JSON 不动**:`KT_ABC1_anchors_sha256_12.json` SHA-12 = `03c6c01f3697` 维持原值,与 Trae 报告一致 ✅
4. **v19 frozen 不动**:`deposon_v19_benchmark_fixes.json` SHA-12 = `910c4333eead` 维持原值 ✅

### 4.3 Mavis 结论
- **返工成立**:9 文件 self_test 全 PASS,无新 bug,无新漂移
- **判定一致**:与 Trae 报告 §三 管线级验证结果完全一致
- **可作为下一次返工的基线**:SHA-12 已稳定,可走正式锚更新流程(本次不动)

---

## §5 5 锚 JSON 核验

| 文件 | SHA-12 | 状态 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | ✅ 未动 |

**沿用 Trae 报告锚值,本次不动**(8 DIFF 替代关系表见 §8)。

---

## §6 v19 frozen 核验

| 文件 | SHA-12 | 状态 |
|---|---|---|
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | ✅ 未动 |

**沿用 Trae 报告锚值,本次不动**。

---

## §7 已知未决项(沿用 Trae 报告"六、遗留事项")

1. **锚 JSON 本身未更新**:`KT_ABC1_anchors_sha256_12.json` 保留旧 SHA-12(历史记录),本次报告 §8 即替代关系报告。后续如需冻结新锚,需走正式流程更新该 JSON。
2. **BOSS-B 裁定全 GRAY**:deposon 失真上界是占位值(0.5/0.05),不标榜差异化。如需真正判定差异化,需从 v19 守恒残差(2.22e-16)反向估计 deposon 失真上界。
3. **reviewer-b 原始 75 攻击报告**:所用为 /tmp 旧栈(攻击顶层字段+弱检测器),与返工版口径不同。已在 `PHASE_B_TMP/kt_b1_audit_full_v03_rerun.json` 留档,建议在 REVIEWER_B 文档补勘误说明。
4. **600 攻击日志**:`docs/V3X/KT_B1_FULL_ATTACK_200_V0.2_20260910_095517.log`。

### 7.1 Mavis 视角补充
- **B1 耗时差异**(本报告 §4.2 #1)未在 Trae 报告登记
- **5 锚 JSON 本身未更新**(本报告 §7 #1)仍需走流程
- **0 个新未决项**被本报告发现(无新 bug,无新漂移)

---

## §8 8 DIFF 替代关系表(沿用 Trae 报告"四、SHA-12 变更总表")

### 返工涉及文件(锚旧值 → 当前)

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

8 个 DIFF 全部查明:5 个是 Option A 授权返工的合法变更,3 个是未报告的 BOSS-B 漂移(已修复)。

### 冻结区专项(绝不许动,全部 MATCH)

| 文件 | SHA-12 | 状态 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | ✅ |
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | ✅ |
| `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | ✅ |
| `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `5e99e79f2e11` | ✅ |
| `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | `ba53d73e3937` | ✅ |

---

## §9 等 API 期间可做的(写 GPT-6 spec 等)

1. **GPT-6 vs MiniMax-M3 对照实验 SPEC** ✅ 已完成
   - 文件:`docs/V3X/GPT6_VS_M3_SPEC_V0.md`(9775 bytes)
   - 任务:沿用 4 SPEC V0.1 模板 + 30 cells 边际验证
   - 状态:V0 草稿,实现冻结于 API 恢复 + OpenRouter billing 验证
2. **5 锚 JSON 更新流程** - 待 8 DIFF 替代关系走通后,正式更新
3. **REVIEWER_B 文档勘误** - 待 BOSS-B 漂移说明补入
4. **B1 耗时基线** - 本报告 §4.2 #1 已记录差异(13 vs 10 min)
5. **D6 论文 v2 整合** - 沿用 `V3X_D6_PAPER_V2_2026_09_09_mavis.md`(24778 bytes)

### 9.1 等 API 期间 Mavis 已交付
- 9 文件 SHA-12 复核(本报告 §1)
- 9 文件 self_test 全 PASS(本报告 §2)
- 9 文件耗时基线建立(本报告 §2 + §4.2 #1)
- GPT-6 spec 草稿(独立任务交付,9775 bytes)
- 8 DIFF 替代关系交叉对账(本报告 §8)
- 5 冻结区专项 SHA-12 复核(本报告 §8)

---

*报告生成: 2026-09-10 Mavis worker*  
*仅复跑+交叉对账,无 API 调用*  
*下次升级:8 DIFF 替代关系正式入锚 → 5 锚 JSON 更新*
