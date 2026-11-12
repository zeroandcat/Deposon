# M0 窗 F3 参数 8 项对照·差异表（P81-乙回填机制承载件）

- 判据唯一源：`m0_window_config.yaml`（sha16 `66af77376843b3fc`·readonly·**0 现场定参**）
- 编译模式：本地预编译（今夜数据）·生成 2026-11-12T07:46:05
- 读数性质分级：G0＝合成管线级 / W1＝底模实测级——分列登记·不冒充

| # | key | 初值（配置字面） | 实测 | 性质/状态 | mismatch | 建议（候 PI） | PI 裁 |
|---|---|---|---|---|---|---|---|
| 1 | F3_N_weeks | 3 周线（基线·候正式立项冻结） | — | —·pending（时序未至·0.6B 深化继续〔PI 23:19:51〕·切位后移） | 否 | — | （留空候 PI） |
| 2 | dilution_detect_threshold | ±10pp | W1 双臂终态差 11.86pp（BAcc500：R1 0.561 vs R2 0.6796·faceA 逐位复算） | W1 底模实测级（0.6B 先例·M2 四臂语义不同·仅检测力信号·非定参依据）·measured（先例面） | 是 | 维持 ±10pp（先例不触发改判） | （留空候 PI） |
| 3 | delta_dispersion_gate | 分歧率门 1.53%（BIR 上界在册） | BIR disp_max=0.0（gate 0.0153·未触） | G0 合成管线级＋W1 faceB 底模级（δ 三域 W3 位未测）·partial（δ 时序未至） | 否 | — | （留空候 PI） |
| 4 | J1_hamming_gate | （M0 窗口径·配置字面） | — | —·pending（M2 四臂位） | 否 | — | （留空候 PI） |
| 5 | eps_closure | 1e-6 | max|CE|=2.220446049250313e-16（朴素）/ 2.220446049250313e-16（fsum）；viol=0＋deployed_charge_sha256 恒等（守恒机器成立·W1 间接背书面） | G0 合成管线级（双实现）＋W1 底层级（守恒背书·ε 逐命题位 M1 未测）·measured（有效但过宽） | 是 | 有效但过宽：max|CE_p|≤1e-12 → 建议收紧 ε 至 1e-12 级（保留安全余量） | （留空候 PI） |
| 6 | D20_detectable_diff | ±10pp | power@10pp(n=1000)=1.0·MDE@0.95=6.09pp（G0 锚 P0=0.75）；W1 实测双臂差 11.86pp≥10pp（可测阈达成） | G0 统计级＋W1 底模实测级（果判位触发）·measured（触发果判） | 是 | R4 补三角对照升优先（定参单 §2.2 字面触发·候 PI 终判） | （留空候 PI） |
| 7 | D4_dependency_threshold | CoT 前后准确率差≥10pp 判「高依赖」 | W1 faceB GRAY 画像：R1 0.052·R2 0.047（tie→GRAY 路由实测·非依赖度本身） | W1 faceB 参考面（依赖度梯度 D4 小实验〔首月〕未测）·partial（画像面·判读阈时序未至） | 否 | — | （留空候 PI） |
| 8 | D4_tie_tolerance_tau | 1e-6 | G0 档位扫描非敏区（首触发 1e-3·区间不触发·容差非敏区（读数登记·不作失效）——τ=1e-6 维持（初值不受挑战））；W1 faceB 实测 GRAY：R1 0.052·R2 0.047@τ=1e-6 | G0 合成管线级＋W1 底模实测级·measured（非敏区不受挑战） | 否 | τ=1e-6 维持（初值不受挑战） | （留空候 PI） |

**纪律自陈**：0 GPU·0 服务器触（本地模式）·0 现场定参（差异表只登记）·实测值逐项挂源指纹（m0_window_config.yaml:66af77376843b3fc·m0_results.json:29ebab8ede0fbcc2·R1__w1x_results.json:9d50673955befad3·R2__w1x_results.json:70837fdd0d042d28）·红绿如实。
