# GLM 制品 FPR 4.4% GRAY 排查 + 3 方盲测重跑 (2026-09-17)

**作者**: Worker (Mavis 委派)  
**触发**: O P-K v2 三方盲测中 GLM 制品 2/45 被判自家, FPR 4.44% > 1% 阈值, 沿 KIMI 7 方向不调阈值 → GRAY  
**任务 ID**: PK-V3-GLM-FPR-2026-09-17  
**严守**: 7 铁律 0 触动 18 frozen + 5 制品 JSON + schema v1 + 4 plugin spec + runner 代码

## §1 触发 (Trigger)

- O P-K v2 三方盲测 (`corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json`) 报告 GLM 制品 2/45 被判自家
- 沿 KIMI 7 方向"不允许为新数据调阈值", FPR 4.44% > 1% 阈值 → GRAY (FAIL)
- 戴夫+鲍勃备忘: 13 维特征空间中 GLM 与自家可能分布重叠
- user 拍板: 派 worker 排查 GLM JSON 结构 + 3 方盲测重跑 (2-3 h wall-clock)

## §2 输入 (Input, 只读)

| 路径 | SHA-12 | 字节数 |
|---|---|---|
| `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | `268ab1239a8a` | 19685 |
| `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` | `39732a92b5c9` | 13150 |
| `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | `576eaf8d7431` | 11341 |

## §3 方法 (Method, 0 重算 + 0 触动)

- **Step 1 排查**: 沿 `twoway_glm.glm_predictions` 冻结 d/pred 找出 2 件被判自家的 GLM JSON, 比对自家 26 件 d 分布 + GLM 制品 metadata (provenance/source_path/struct_signature), 0 重算 d
- **Step 2 重跑**: 沿 `twoway_glm.frozen + kimi_results.frozen d/pred` 直接读取, 仅重排三方制品列表 (按 origin + artifact_id 字典序), 重算混淆矩阵与 4 判死线
- **Step 3 决策**: 沿 FPR 重判 + paper §7.2/§4.4 引用
- **严守**: 0 重算 d, 0 触动 18 frozen anchors + 5 制品 JSON + schema v1 + 4 plugin spec + runner 代码

## §4 结果 (Result, Step 1 排查)

### 4.1 自家 26 件 d 分布 (判别阈值 T=2.0)

- min=0.2299, max=1.2960, mean=0.6559
- 全部 26 件 pred=自家 ✓

### 4.2 误判 GLM JSON 定位 (2/45)

| artifact_id | byte_sha12 | n_bytes | is_json | d | pred | struct_signature |
|---|---|---|---|---|---|---|
| `GLM-N10` | `392c2ac0daf4` | 11785 | 1 | 1.3137 | 自家 | `J:5dc4a329c802` |
| `GLM-N11` | `4ffd8652f2e9` | 2612 | 1 | 1.8832 | 自家 | `J:6d35f90b5c09` |

### 4.3 GLM JSON 结构对比

| artifact_id | source_path | provenance |
|---|---|---|
| `GLM-N10` | `/home/z/my-project/agents/6a962cc259312f271f3f1e73/bob-repro/bob_pd2_repro_results.json` | GLM-N09 复现 runner 的结果 JSON(GLM 代码直接输出, 2026-09-01) |
| `GLM-N11` | `/home/z/my-project/agents/6a962cc259312f271f3f1e73/bob-repro/rerun_diff_summary.json` | GLM 构造的重跑 diff 汇总 JSON(2026-09-01 重跑审计) |

### 4.4 13 维特征差异表 (误判件 vs 最近自家 + 最近正确分类 GLM JSON)

GLM-N10 (d=1.314):

**GLM-N10 (d=1.3137)**

- 最近自家 3 件 (按 |d_glm - d_own| 升序):

| rel_path | d | delta |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 1.2960 | -0.0177 |
| `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | 1.2269 | -0.0868 |
| `results/deposon_v3_v7_summary_2026_09_11.json` | 1.1201 | -0.1936 |

- 最近正确分类 GLM JSON 3 件 (按 |d_glm - d_glm| 升序):

| artifact_id | byte_sha12 | d | delta |
|---|---|---|---|
| `GLM-N12` | `a9efc1761aa0` | 2.5157 | +1.2021 |
| `GLM-N13` | `113f927f54be` | 2.5369 | +1.2232 |
| `GLM-N15` | `bee9b6b99faa` | 2.6659 | +1.3522 |

**GLM-N11 (d=1.8832)**

- 最近自家 3 件 (按 |d_glm - d_own| 升序):

| rel_path | d | delta |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 1.2960 | -0.5872 |
| `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | 1.2269 | -0.6564 |
| `results/deposon_v3_v7_summary_2026_09_11.json` | 1.1201 | -0.7631 |

- 最近正确分类 GLM JSON 3 件 (按 |d_glm - d_glm| 升序):

| artifact_id | byte_sha12 | d | delta |
|---|---|---|---|
| `GLM-N12` | `a9efc1761aa0` | 2.5157 | +0.6325 |
| `GLM-N13` | `113f927f54be` | 2.5369 | +0.6537 |
| `GLM-N15` | `bee9b6b99faa` | 2.6659 | +0.7827 |

### 4.5 排查结论 (audit findings)

1. **类型**: GLM-N10/N11 同为 JSON 型 (is_json=1.0), 与 GLM-N12/N13/N14/N15 同型, 共 6 件 GLM JSON
2. **d 对比**: GLM-N10 d=1.314 < GLM-N12 d=2.516 (差 1.20); GLM-N11 d=1.883 < GLM-N12 d=2.516 (差 0.63); GLM-N10/N11 远低于同型 JSON 外围 (GLM-N12..N15 d 区间 [2.516, 2.781])
3. **自家接近度**: GLM-N10 d=1.314 仅比自家最大 d (1.296, KT_ABC1_anchors_PATCH) 高 0.018; GLM-N11 d=1.883 比自家最大 d 高 0.587 (已远离最近自家件)
4. **struct_signature 模式**: GLM-N10=J:5dc4a329c802 (独立), GLM-N11=J:6d35f90b5c09 (独立), GLM-N12..N15 共用 J:c574608dd86d (同 schema 模板); GLM-N10/N11 走另一 JSON 模板 (PD2 复现输出), 跟自家 KT_ABC1_anchors_PATCH 的 key 路径分布更接近
5. **provenance**: GLM-N10 = GLM-N09 (run_bob_repro.py) 直接生成的 PD2 复现结果 JSON; GLM-N11 = GLM 构造的重跑 diff 汇总 JSON (2026-09-01 重跑审计); 两件均为 deposon PD2 工作流产物, 字段命名/层级贴近 deposon P-D 风格
6. **阈值 T**: T=2.0 固定 (沿 KIMI 7 方向'不允许为新数据调阈值', zero rehash); GLM-N10/N11 d 在 [1.314, 1.883] 区间内, 不调整阈值无法判外来

**主因**: GLM-N10/N11 的 JSON 结构 (键路径集) 与自家 P-D 锚件 (KT_ABC1_anchors 系列) 分布重叠; key_vocab_overlap 特征将这两件 GLM JSON 拉近自家质心

## §5 结果 (Result, Step 2 重跑, frozen d 沿 13 维特征 + 4 判别规则)

### 5.1 三方制品数量

- 自家: 26 件 (全部 pred=自家 ✓)
- GLM: 23 件 (pred=自家: 2, pred=外来: 21)
- KIMI: 22 件 (pred=外来: 22, pred=自家: 0)
- 外来合计: 45 件 (= GLM + KIMI)

### 5.2 混淆矩阵 (3 主体行 × {判自家, 判外来} 二元列)

| 行\列 | 判自家 | 判外来 |
|---|---|---|
| 自家 | 26 | 0 |
| GLM | 2 | 21 |
| KIMI | 0 | 22 |

### 5.3 4 判死线

| 判死线 | 实测 | 通过 |
|---|---|---|
| SP_t >= 0.7 | 1.0000 | ✓ |
| FPR < 1/100 | 0.0444 | ✗ |
| FNR < 1/20 | 0.0000 | ✓ |
| anti_whitewash >= 0.6 | 0.9556 | ✓ |

**OVERALL**: FAIL

### 5.4 GLM vs KIMI 描述性观测 (不入判死线)

- GLM d range: [1.3137, 4.5020]
- KIMI d range: [3.0366, 4.5389]
- GLM vs KIMI 成对分离率: 0.6146

## §6 决策 (Step 3, 沿 FPR 决定 paper 引用)

- **FPR = 0.0444** (> 1% 阈值 0.01)
- 沿 KIMI 7 方向"不允许为新数据调阈值", 严格不动 T=2.0
- 沿 7 铁律, 老实入 paper 限制节 (Honest Limitations), 不擅自重写 §4 引用
- **paper 引用建议**: §7.2 Honest Limitations: GLM JSON FPR 4.4% GRAY (key_vocab_overlap 重叠, T=2.0 严格不调)

## §7 严守 7 铁律声明

| 铁律 | 状态 | 备注 |
|---|---|---|
| 1. 0 LLM 调用 | ✓ 严守 | 纯读 + JSON 重排 + 数值汇总 |
| 2. 不设 proxy | ✓ 严守 | |
| 3. 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan/WeChat API | ✓ 严守 | 仅读本地 JSON |
| 4. key 永不入 prompt/JSON/落盘 | ✓ 严守 | |
| 5. 不动 5 锚 JSON (`03c6c01f3697`) | ✓ 严守 | |
| 6. 不动 4 SPEC V0.1 + v19/v21 + corpus/v20 + 18 frozen + P-G V0 + P-G V0.1 | ✓ 严守 | 仅读 corpus/v20/by_model/ + results/ + deposon_team/_designs/ + docs/V3X/ |
| 7. 不动 verifier/mavis/.builtin/scripts/ | ✓ 严守 | |
| 8. 不创建临时文件 | ✓ 严守 | 仅落 results/_p_k_v3_glm_json_audit_<ts>.json + results/_p_k_v3_three_way_rerun_<ts>.json + results/_p_k_v3_glm_fpr_audit_report_<ts>.md |

## §8 等 user 拍板

- ❌ 不擅自重写 paper §4.4 引用 (FPR 4.44% > 1%, 严格不动 T=2.0, 沿 KIMI 7 方向)
- ❌ 不擅自为新数据调阈值 (沿 KIMI 7 方向)
- ❌ 不擅自合并派生 JSON (2A) 到 5 锚 JSON (等 user 拍板)
- ❌ 不擅自启动 P-A/P-B/P-C/P-D 等其他方向
- ❌ 不擅自吊销 PAT (等 user 操作)

**报告完成**: 7 铁律 0 触动, FPR 4.44% GRAY 如实披露, 沿 KIMI 7 方向老实入 paper §7.2 (限制节)

**3 制品路径 + SHA-12**:
- `D:\私人资料\deposon-repo\corpus\v20\by_model\GLM_1\three_way_glm_slot_blind_test_2026_09_16.json` SHA-12=`268ab1239a8a`
- `D:\私人资料\deposon-repo\corpus\v20\by_model\GLM_2\glm_artifact_v_2026_09_16.json` SHA-12=`39732a92b5c9`
- `D:\私人资料\deposon-repo\results\deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` SHA-12=`576eaf8d7431`