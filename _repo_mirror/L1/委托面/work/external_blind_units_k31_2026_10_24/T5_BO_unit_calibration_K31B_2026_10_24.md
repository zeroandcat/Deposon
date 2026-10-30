# T5 B-O 单位、换算与可通约性（窄交付·如实报缺）

日期：2026-10-24｜句柄：K31B｜范围：仅量纲、单位、与 `B_t=3` 之换算，以及方向、可通约性。本文不含占用量数值、收益或代价数值、动作排序或逐格动作语义载荷。

## §R-1 逐格三列表（另附方向与可通约性）

`UNOBTAINED` 表示该格该列未获可核证据；不是零、估算值、默认值或空集。

| 格 | ①量纲 | ②单位 | ③与 `B_t=3` 之换算 | ④方向 | ⑤可通约性 |
|:--|:--|:--|:--|:--|:--|
| `t_01` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_02` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_03` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_04` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_05` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_06` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_07` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_08` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_09` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_10` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_11` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_12` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_13` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_14` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_15` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_16` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_17` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_18` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_19` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |
| `t_20` | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED | UNOBTAINED |

## §R-2 来源与逐格逐列依据

### 来源件

- **S-1**：`_commission_t5_inputs_external_EN_round2_draft_2026_10_24.md`，64,125 B／SHA-12 `e2cd66b1b543`，§2-1 与 §3.2 `A2-2`。其清单称逐格预算摘要含 budget type/value/unit/step limit，并述及全局单位类别 `units/days/rounds/hours`；但附件本体不在本次可用材料中，故没有“格→单位”的实际映射。复核时点：2026-10-24T20:36:06.595+08:00。
- **S-2**：`_t5_inputs_construction_plan_2026_10_23.md`，85,336 B／SHA-12 `3982b82f095b`，§2-4、§4-1。其载总额约束及 `cap/limit/quota/reserve floor` 等措辞类别，但未给这些措辞与 `t_01…t_20` 的逐一对应。复核时点同上。
- **S-3**：`_t5_inputs_three_track_2026_10_23_redacted_v1_2026_10_24.md`，53,734 B／SHA-12 `ee07d58a1ee2`，§6-2。其支持 `B_t=3` 与另行步限的存在，并明确总额约束不等于逐动作占用；未给逐格资源单位或单位换算。复核时点同上。
- **S-4**：NIST, *Guide to the SI, Appendix B.9, Time*，https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9 。条款：`day → second = 8.64E+04`、`hour → second = 3.6E+03`。检索时点：2026-10-24T16:22:04.154+08:00。此源只在某格已被独立证明采用 day 或 hour 时适用，不能反向证明该格单位。

### 依情境定义可推得的规则（不指派给任何格）

1. 只有实际约束短语为 cap/limit/quota 等上界语义时，方向才可写作“用量不得超过”；只有实际短语为 floor 等下界语义时，方向才可写作“存量不得低于”。S-2 没有给出格与短语的映射，故不能逐格套用。
2. 可通约须同时满足：量纲相同、资源指称相同、换算系数已知。仅仅两个单位都能换成秒，不足以证明两种资源可通约。
3. day/hour 的秒换算由 S-4 给出；`round` 的情境起讫未给，不能换算成秒；`units` 的资源指称未给，不能跨情境换算。

### 每格每列之依据

`U(S-1/S-2/S-3)` 表示三件合观仍无该格映射；`C(S-4)` 表示换算源仅作条件式，尚未被单位证据触发。

| 格 | 量纲依据 | 单位依据 | 换算依据 | 方向依据 | 可通约性依据 |
|:--|:--|:--|:--|:--|:--|
| `t_01` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_02` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_03` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_04` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_05` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_06` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_07` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_08` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_09` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_10` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_11` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_12` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_13` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_14` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_15` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_16` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_17` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_18` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_19` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |
| `t_20` | U(S-1/S-2/S-3) | U(S-1/S-2/S-3) | U(S-1/S-2/S-3)；C(S-4) | U(S-2 无格映射) | U(S-1/S-3) |

## §R-3 可复算之换算算法

以下仅为条件算法，不是任何格的已获单位或换算结果。

```text
seconds(q, unit) =
    q × 86400,  if unit = day
    q × 3600,   if unit = hour
    UNOBTAINED, otherwise

B_seconds =
    3 × 86400,  if the cell is independently shown to use day as a duration
    3 × 3600,   if the cell is independently shown to use hour as a duration
    UNOBTAINED, otherwise
```

方向判式：`x ≤ B_t` 表示上界；`x ≥ B_t` 表示下界。这里的 `x` 只是代入槽，不代入任何占用数值。方向须先由该格实际约束语义确定，不能由 `B_t=3` 推出。

两量 `q_u` 与 `q_v` 的通约算法：先核量纲与资源指称；二者皆同且存在已知系数 `k` 时，才可写 `q_v = k × q_u`。任一要件缺失即 `UNOBTAINED`。跨格比较还须另核两格是否指同一资源，禁止只按单位字面合并。

## §R-4 具名缺口清单（逐格逐列）

缺口代号及其原因：

- `G-DIM`：缺逐格量纲；S-1 只有单位类别与附件清单，S-2/S-3 无格映射。
- `G-UNIT`：缺逐格具体单位；预算摘要本体未供，不能由全局单位类别指派。
- `G-CONV`：缺量纲、单位及系数适用前提；S-4 只能给 day/hour 的条件换算。
- `G-DIR`：缺“约束短语→格”的映射，不能判定上界或下界。
- `G-COMM`：缺两格各自单位、量纲和资源指称，不能判定可通约或其边界。

| 格 | 量纲缺口 | 单位缺口 | 换算缺口 | 方向缺口 | 可通约性缺口 |
|:--|:--|:--|:--|:--|:--|
| `t_01` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_02` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_03` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_04` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_05` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_06` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_07` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_08` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_09` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_10` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_11` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_12` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_13` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_14` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_15` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_16` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_17` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_18` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_19` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |
| `t_20` | G-DIM | G-UNIT | G-CONV | G-DIR | G-COMM |

## §R-5 整体可得度与结构性障碍

- 三列齐：`0/20` 格；部分可得：`0/20` 格；三列全缺：`20/20` 格。
- 方向与可通约性两附加列亦为 `20/20` 格未获得。`B_t=3` 的数值已知不改变这三列的缺失状态。

结构性障碍有四：①清单所述预算摘要本体未供，逐格映射断裂；②全局单位类别不能替代逐格单位；③公开标准只给条件换算，不能反向创设情境单位；④方向与通约还依赖约束语义及资源指称，单有 `B_t=3` 不足以判定。故本轮的可核结果是逐格报缺与条件算法，而非单位表数值化。

## §R-6 未采纳确认

本交付不等于采纳，也不构成对上一轮任何文件的修改。是否采认、是否入链及如何使用这些报缺与条件式，均归 PI。

## §R-7 自证（定宽零化代入法）

- `SELF_BYTES` = `00010607`
- `SELF_SHA12` = `4a25edaab099`
- `SELF_LF` = `148`
- `BOM` = `0`
- `CR` = `0`
- `U+FFFD` = `0`
- 末字节 = `0x0A`

复算方法：`SELF_BYTES` 为 8 位十进制字节数，`SELF_SHA12` 为 12 位小写 SHA-256 前缀。仅将这两个字段的**值**分别替换为 `00000000` 与 `000000000000`，保持其他字节不变；对替换后的完整文件字节流计算 SHA-256，其前 12 位须等于原 `SELF_SHA12`，且总字节数须等于原 `SELF_BYTES`。LF 按 `0x0A` 字节计数；BOM 指 UTF-8 BOM 前缀；CR 指 `0x0D` 计数。
