# Lean 守恒镜像树 · v5preR2 读数（实编·1e27d7c）

> **令源**：群管理员 2026-11-25 09:44:20 派单②＋PI 09:47 校正「两帐树指记忆帐树与实验帐树」。
> **本件性质**：只读 `harness/DeposonThermo.lean` 与 `harness/lean_axiom_audit.py`，实编取公理台账（`Lean (version 4.15.0, x86_64-unknown-linux-gnu, commit 11651562caae, Release)`·core-only·0 mathlib）。
> **可复现**：`python3 paper/tools/gen_tree_lean.py --log paper/evidence/lean_build_1e27d7c.log`·编译日志全留。

## 1. 编译与公理总判

| 判据 | 结果 |
|---|---|
| lean 退出码 | 0 ✓ |
| 输出含 error | 无 ✓ |
| sorryAx | 0 ✓ |
| `#print axioms` 覆盖 | 15/15 |
| 公理集 ⊆ {propext, Quot.sound} | ✓ |
| 数据定理 0 公理（settle_close / settle_conserved） | ✓ |
| 手算向量逐位（Lean decide ↔ Python reducer） | ✓ |
| **总判** | **ALL PASS** |

## 2. 定理公理台账（15 条）

| 定理 | 类别 | 公理集 | 判定 |
|---|---|---|---|
| `sum_set` | algebra | propext, Quot.sound | ✓ |
| `conserved_inject` | conservation | propext, Quot.sound | ✓ |
| `conserved_dissipate` | conservation | propext, Quot.sound | ✓ |
| `conserved_transmit` | conservation | propext, Quot.sound | ✓ |
| `conserved_reflect` | conservation | propext, Quot.sound | ✓ |
| `conserved_deposit` | conservation | propext, Quot.sound | ✓ |
| `diss_monotone_inject` | monotone | 0（无公理） | ✓ |
| `diss_monotone_dissipate` | monotone | propext | ✓ |
| `diss_monotone_transmit` | monotone | 0（无公理） | ✓ |
| `diss_monotone_reflect` | monotone | 0（无公理） | ✓ |
| `diss_monotone_deposit` | monotone | propext | ✓ |
| `pool_monotone` | algebra | propext, Quot.sound | ✓ |
| `settle_close` | settle | 0（无公理） | ✓ |
| `settle_conserved` | settle | 0（无公理） | ✓ |
| `sum_drop_zero` | algebra | propext | ✓ |

## 3. 五转移守恒镜像（Lean 定理 ↔ Python 事件）

| Lean 定理 | Python 事件 | Lean 侧 | Python 侧 |
|---|---|---|---|
| `conserved_inject` | `inject` | 注入 E⁰+=q | E⁰ += q；U += q |
| `conserved_dissipate` | `decay` | 散失 U→D（i,a 越界即炸） | U -= a；D += a |
| `conserved_transmit` | `gate.tx` | 透射 Φ+=c（询㶲支付） | Φ += c_T×|tx| |
| `conserved_reflect` | `gate.ph` | 幻肢回射 R+=c | R += c_P×|ph| |
| `conserved_deposit` | `deposit` | 散失 deposit：U 全额→D·i 断链即炸 | U → 0；D += U |

## 4. 第二律方向锚（diss 单调·5 转移）

| Lean 定理 | Python 事件 |
|---|---|
| `diss_monotone_inject` | `inject` |
| `diss_monotone_dissipate` | `decay` |
| `diss_monotone_transmit` | `tx` |
| `diss_monotone_reflect` | `ph` |
| `diss_monotone_deposit` | `deposit` |

## 5. 手算结算向量逐位对表

| 项 | Lean decide | Python reducer | 判定 |
|---|---|---|---|
| e0 | 210 | 210 | ✓ |
| phi | 10 | 10 | ✓ |
| refl | 0 | 0 | ✓ |
| diss | 150 | 150 | ✓ |
| us | [50, 0] | [50, 0] | ✓ |

守恒核：成立（210 = 10+0+150+50）

## 6. 复现命令

```bash
cd plugin_up_v1 && python3 paper/tools/gen_tree_lean.py --log paper/evidence/lean_build_66b53fc.log
cd plugin_up_v1 && python3 mcp/thermo_crosscheck.py   # 同向量过 Python reducer 15/15
cd plugin_up_v1 && python3 harness/lean_axiom_audit.py # 审计 27/27
```

