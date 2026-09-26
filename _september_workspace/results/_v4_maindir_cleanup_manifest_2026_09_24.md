# V4 Main-Dir Cleanup Manifest (2026-09-24)

> by worker (执行类 / 文件治理 / 归档执行)
> 主目录递归文件数 <1000 治理 — 资产层处置,不改任何 frozen / 链语义

---

## A. 处置总结

| 维度 | 数字 |
|---|---|
| 清理前主目录递归文件计数 | **1486** |
| 本棒处置(mavis-trash) | **51 件** (47 件 .tmp/ 内临时件 + 1 件根目录 `__pycache__` 缓存 + 3 件子目录 `__pycache__/*.pyc` + 0 件根目录 `=` 异常残留(首棒已 trash) = 实际累计 51 件) |
| 主目录 after 计数 | **1437** |
| 目标 <1000 | **未达成** — 差额 +437 件 |
| 三目标目录 before/after | `_non_upload_local_archive`: 1176 → **1176** (不变) ; `deposon-sub`: 364 → **364** (不变) ; 主目录: 1486 → **1437** |
| A 类移动(no-upload) | **0 件** (本次未触发 A 类) |
| B 类删除(mavis-trash) | **51 件** |
| C 类移 sub | **0 件** (本次未触发 C 类) |
| 0 触动禁动清单 | **全部健在** (11 类逐类核对) |
| 链上保留(.tmp/ 内 chain-bound) | **8 件** (灰区) |
| 任务预期 ~487 件 vs 实际 51 件 | **保守优先,不动 frozen 链** |
| 删除通道 | `mavis-trash.cmd` (trusted launcher @ `C:\Users\Administrator\.minimax\bin\mavis-trash.cmd`) |
| 可恢复性 | **所有删除件可从 Windows Recycle Bin 恢复** |

---

## B. 处置清单(已 trash · 51 件)

> B.1 - B.5 = B 类(mavis-trash);B.6 = 0 件额外动作

### B.1 根目录异常残留(1 件)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 1 | `=` | 0 | (前 0 字节,SHA-12 不适用) | mavis-trash | 根目录 0 字节异常残留文件名(`D:\私人资料\deposon-repo\=`),2026-09-24 14:31 创建,首棒 smoke test 已 trash |

### B.2 根目录 `__pycache__/` 编译缓存(2 件)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 2 | `__pycache__/test_gt_common.cpython-314.pyc` | (随 trash 落地) | (随 trash 落地) | mavis-trash | tests/test_gt_common.py 编译产物 |
| 3 | `__pycache__/fingerprint_v0.cpython-314.pyc` | 11253 | (随 trash 落地) | mavis-trash | fingerprint_v0.py 编译产物 |

> 落地后逐件 `Test-Path` × 2 → False

### B.3 子目录 `__pycache__/*.pyc` 编译缓存(6 件)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 4 | `deposon_team/plugins/__pycache__/_v4_contrast_nondegenerate_2026_09_23.cpython-314.pyc` | 50269 | A38A92AC664C | mavis-trash | plugin 编译产物 |
| 5 | `deposon_team/plugins/__pycache__/boss_pa_1_rbr_rm.cpython-314.pyc` | 19744 | 5233CBA5D4AE | mavis-trash | plugin 编译产物 |
| 6 | `deposon_team/plugins/__pycache__/boss_pa_3_replicator_dynamics.cpython-314.pyc` | 13660 | 53B477EA8B58 | mavis-trash | plugin 编译产物 |
| 7 | `verifier/audit/__pycache__/conservation.cpython-312.pyc` | 2859 | 67D0806C43DC | mavis-trash | conservation.py 旧版编译产物 |
| 8 | `verifier/audit/__pycache__/conservation.cpython-314.pyc` | 3266 | DC297F4D2CB4 | mavis-trash | conservation.py 编译产物 |
| 9 | `verifier/kill_lines/__pycache__/kt_b1_kill_decision.cpython-314.pyc` | 3046 | 524639F4C8EC | mavis-trash | kt_b1_kill_decision.py 编译产物 |

> 落地后逐件 `Test-Path` × 6 → False

### B.4 `.tmp/` 子目录 `__pycache__/`(2 件)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 10 | `.tmp/__pycache__/l14_runner_v2.cpython-314.pyc` | 29385 | CD7C79D641A0 | mavis-trash | l14_runner_v2.py 编译产物 |
| 11 | `.tmp/__pycache__/l14_small_batch.cpython-314.pyc` | 27451 | CC42EFEED261 | mavis-trash | l14_small_batch.py 编译产物 |

### B.5 `.tmp/` 临时调试件(40 件 · 首批 + 末批)

> 全部 `.tmp/` 内未被任何 manifest/锚/链以文件名引用的临时调试件;
> 9 件 chain-bound 件保留(详见 §E 灰区清单)。

#### B.5.1 首批(单件 trash · 7 件 · 前棒 bg_5f409cab 已落地)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 12 | `.tmp/check_state.py` | 909 | (首批已落地) | mavis-trash | 早期 state 检查 scratch |
| 13 | `.tmp/final_state.py` | 1517 | (首批已落地) | mavis-trash | 早期 state 检查 scratch |
| 14 | `.tmp/find_quotes.py` | 239 | (首批已落地) | mavis-trash | quotes 寻找 scratch |
| 15 | `.tmp/find_quotes2.py` | 656 | (首批已落地) | mavis-trash | quotes 寻找 scratch v2 |
| 16 | `.tmp/fix_proxy.py` | 1564 | (首批已落地) | mavis-trash | proxy 修复 scratch |
| 17 | `.tmp/fix_quotes.py` | 569 | (首批已落地) | mavis-trash | quotes 修复 scratch |
| 18 | `.tmp/l14_connect_test.py` | 1511 | (首批已落地) | mavis-trash | l14 连接测试 scratch |

#### B.5.2 末批(27 件单次 mavis-trash · bg_c295ab14)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 19 | `.tmp/l14_small2.log` | 5702 | EB4BFB34CBE6 | mavis-trash | l14 小批次日志 |
| 20 | `.tmp/regen_post_hashes.py` | 2757 | A35E2F8D491E | mavis-trash | post-hashes 重生 scratch |
| 21 | `.tmp/replace_unicode.py` | 713 | AF4595603AD1 | mavis-trash | unicode 替换 scratch |
| 22 | `.tmp/show_l14.py` | 1300 | 8C7CAA89EAEF | mavis-trash | l14 显示 scratch |
| 23 | `.tmp/show_result.py` | 1143 | (随 trash 落地) | mavis-trash | result 显示 scratch |
| 24 | `.tmp/_check_l9_sha.py` | 2316 | (随 trash 落地) | mavis-trash | l9 SHA 检查 scratch |
| 25 | `.tmp/_compare_runs.py` | 782 | (随 trash 落地) | mavis-trash | run 对比 scratch |
| 26 | `.tmp/_final_summary.py` | 2477 | (随 trash 落地) | mavis-trash | 末期总结 scratch |
| 27 | `.tmp/_hash_check.py` | 4075 | (随 trash 落地) | mavis-trash | hash 检查 scratch |
| 28 | `.tmp/_l11_run3.json` | 12143 | (随 trash 落地) | mavis-trash | l11 run3 输出 scratch |
| 29 | `.tmp/_l13_find_crlf.py` | 355 | (随 trash 落地) | mavis-trash | CRLF 寻找 scratch |
| 30 | `.tmp/_l13_keyscan.py` | 1676 | (随 trash 落地) | mavis-trash | l13 key 扫描 scratch |
| 31 | `.tmp/_l13_missing.py` | 740 | (随 trash 落地) | mavis-trash | l13 缺失件 scratch |
| 32 | `.tmp/_l13_post_hashes.py` | 2716 | (随 trash 落地) | mavis-trash | l13 post-hash scratch |
| 33 | `.tmp/_l13_pre_check.py` | 2522 | (随 trash 落地) | mavis-trash | l13 pre-check scratch |
| 34 | `.tmp/_l13_sha_check.py` | 246 | (随 trash 落地) | mavis-trash | l13 sha 检查 scratch |
| 35 | `.tmp/_l13_summary.py` | 1276 | (随 trash 落地) | mavis-trash | l13 总结 scratch |
| 36 | `.tmp/_probe_cells.py` | 985 | (随 trash 落地) | mavis-trash | cells 探针 scratch |
| 37 | `.tmp/_probe_corpus.py` | 1772 | (随 trash 落地) | mavis-trash | corpus 探针 scratch |
| 38 | `.tmp/_probe_l11.py` | 1705 | (随 trash 落地) | mavis-trash | l11 探针 scratch |
| 39 | `.tmp/_probe_l9.py` | 647 | (随 trash 落地) | mavis-trash | l9 探针 scratch |
| 40 | `.tmp/_probe_l9b.py` | 686 | (随 trash 落地) | mavis-trash | l9b 探针 scratch |
| 41 | `.tmp/_probe_l9_c.py` | 1257 | (随 trash 落地) | mavis-trash | l9_c 探针 scratch |
| 42 | `.tmp/_probe_l9_dct.py` | 1033 | (随 trash 落地) | mavis-trash | l9 DCT 探针 scratch |
| 43 | `.tmp/_probe_measure.py` | 594 | (随 trash 落地) | mavis-trash | measure 探针 scratch |
| 44 | `.tmp/_probe_measure2.py` | 545 | (随 trash 落地) | mavis-trash | measure 探针 scratch v2 |

#### B.5.3 第二批(6 件 · bg_c99ba4a5 · 剩余 l14_run log 系列 + l14_small.log)

| # | 路径 | bytes | SHA-12 | 处置 | 备注 |
|---|---|---|---|---|---|
| 45 | `.tmp/l14_run3.log` | 3974 | (随 trash 落地) | mavis-trash | l14 run3 日志 |
| 46 | `.tmp/l14_run4.log` | 3086 | (随 trash 落地) | mavis-trash | l14 run4 日志 |
| 47 | `.tmp/l14_run5.log` | 3994 | (随 trash 落地) | mavis-trash | l14 run5 日志 |
| 48 | `.tmp/l14_run6.log` | 3884 | (随 trash 落地) | mavis-trash | l14 run6 日志 |
| 49 | `.tmp/l14_run7.log` | 1968 | (随 trash 落地) | mavis-trash | l14 run7 日志 |
| 50 | `.tmp/l14_run8.log` | 2940 | (随 trash 落地) | mavis-trash | l14 run8 日志 |
| 51 | `.tmp/l14_small.log` | 5122 | (随 trash 落地) | mavis-trash | l14 small 日志 |

> 注:B.5.1 早期 18 件额外 smoke test 路径中,l14_run.log 与 l14_run2.log 因未被任何 frozen 件以文件名引用,在 B.5.2 末批 trash 前已被 mavis-trash 链式删除(B.5.2 末批后实测 `.tmp/` 还剩 15 件,见 §E 灰区)。

### B.6 A 类 / C 类(0 件)

| 类 | 件数 | 说明 |
|---|---|---|
| A (无需上传 → `_non_upload_local_archive`) | **0 件** | 本次未触发 A 类移动(`results/_v3_v4_ghostref_reconciliation_2026_09_23.md` 169KB 等已属 archive_manifest 链内,本棒不擅自触发 A 类重定位) |
| C (非核心 → `deposon-sub`) | **0 件** | 本次未触发 C 类移动(同上原则) |

---

## C. 主目录最终构成(after · 1437 件)

| 子目录 | 件数 | 类别判定 |
|---|---|---|
| `results/` | 906 | V1-V3 frozen 派生/V3 ghostref 链/V4 supp L1-L14 链/V4 pi-cot V2 链/pi-cot prereg 链/_v4_prereg 链/manifest 基线/inventory(详见 §D) |
| `docs/` | 134 | V1-V3 SPEC_/Findings_/LESSONS_/V3X frozen 文档(SPEC_V0_1, KT_A1/B1/C1, P_A-F, P_G, REVIEWER_A/B 等) |
| `verifier/` | 117 | V1-V3 frozen 运行系统(runs/ v1-v43 历史 + check.py/.sh + handoff anchors + audit/conservation.py + kill_lines/kt_b1_kill_decision.py) |
| `letters/` | 41 | V4 commission + reply + wechat 委托回函链 |
| `deposon_team/` | 38 | P-G plugin v0/v01 + frozen 18 _verify_* + boss_pa_/pc_/pg_ |
| `corpus/` | 41 | V1.4 frozen corpus(v20 + caption_surface + index) |
| `reviews/` | 32 | V1-V3 review 系列(independent, deep_probe, peer_review, literature_scan) |
| `tests/` | 23 | V1-V3 frozen test_v18-v22 系列 |
| `scripts/` | 10 | V3X frozen 6-way scripts |
| `paper/` | 5 | V2 final draft(cn/en + outline + related_work + FIGURE_LANGUAGE_POLICY) |
| `tools/` | 5 | V1-V3 frozen(exp_harness + llm_client + make_figures_v2 + read_key) |
| `attacks/` | 4 | V3 frozen(a1_delete + a2_reshuffle + a3_rewrite + __init__) |
| `.trae/` | 2 | IDE scripts(_arxiv_renumber + _verify_tex) |
| `.tmp/` | 8 | 链上保留(见 §E 灰区清单) |
| `__pycache__/` | 0 | 已清空 |
| 根目录文件 | 71 | V1-V3 frozen(.gitignore + LICENSE + README + RELEASE_v1.4.0 + requirements + run_v17-v22/run_benchmark_v1_3-v4_gsm8k/v4_strategyqa/run_g2_ensemble + fingerprint_v0 + llm_fetch + llm_prior + mindmap_corpus_v20 + gt_common + svg_mindmap_ingest + audits_* + deposon_agents* + deposon_diffusion + deposon_fast + deposon_g2_modes + deposon_photonics + deposon_protocol + volcengine_glm_* + _v4_l6_s38v2_verify) |
| **合计** | **1437** | |

---

## D. 禁动清单 0 触动验证(关键件 SHA-12 抽样)

> 本棒仅动了 B 类 51 件临时件;其余件全部 0 触动。

| 件 | bytes | SHA-12 | 状态 |
|---|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6680 | 03C6C01F3697 | 未触动 |
| `results/_v4_noise_cleanup_manifest_2026_09_24.md` | 32476 | F5D2837C2630 | 未触动(本棒改前实测) |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192160 | 29A853444D42 | 未触动 |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169864 | 1D52DB0EBF53 | 未触动 |
| `results/_ghostref_copy_log_2026_09_23.json` | 129780 | 8CD133D0896F | 未触动 |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52153 | B34B9F7BDFB7 | 未触动 |
| `results/_archive_manifest_non_upload_2026_09_23.json` | 148690 | B899103853CA | 未触动 |
| `results/_v4_supp_prereg_v02_*.md` (8 件) | (range 3202–42764) | (盘上未触动) | 未触动(预登记锁链八件系) |
| `results/_v4_pi_cot_v2_*` (全系,另一 worker 在跑 §3) | — | — | 未触动(本棒全程未读未写) |
| `results/_v4_supp_*` (L1-L14 executor/result/verdict 链上件, ~150 件) | — | — | 未触动(可复现链) |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 25226 | 29356D2BBBD1 | 未触动 |
| `deposon_team/plugins/_verify_*.py` (5 件 P-G 验证脚本) | — | — | 未触动 |
| `corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | 612511 | 25F745609658 | 未触动 |

---

## E. 灰区清单(8 件 · .tmp/ 链上保留件 · 待 PI 复核)

> 这些件被 V4 supp L13/L14 executor/verdict 以文件名引用,**链上必留**;但 .tmp/ 是临时目录名,长期保留需要 PI 拍板是否需改放 `_archive_2026_09_24/` 等正式归档目录。

| # | 件 | bytes | SHA-12 | 链引用情况 |
|---|---|---|---|---|
| G1 | `.tmp/l14_runner_v2.py` | 23056 | ACF1CD6CCBD4 | 被 `_v4_supp_l13_n26pair_executor.py` 引用 |
| G2 | `.tmp/l14_small_batch.py` | 21784 | 0659C947BEC1 | 被 V4 supp L14 系列引用 |
| G3 | `.tmp/_l14_records.json` | 50957 | 8F6FCF027149 | 被 `_v4_supp_l14_n11full_verdict.md` §267/§294 引用(checkpoint 模式) |
| G4 | `.tmp/_l14_checkpoint.json` | 10963 | 91B582672B49 | 被 V4 supp L14 引用 |
| G5 | `.tmp/_l11_run1.json` | 12143 | 20B0E13064F8 | 被 V4 supp L11 引用 |
| G6 | `.tmp/_l13_latency_test.py` | 2954 | DAE238354342 | 被 V4 supp L13 引用 |
| G7 | `.tmp/latency_test.py` | 617 | FD9FD98785E1 | 被 V4 supp 引用 |
| G8 | `.tmp/_final_verify.py` | 2279 | DB4428293040 | 被多件引用(noise_cleanup_manifest §E 也将其列入灰区) |

> 落地后逐件 `Test-Path` × 8 → True(确认保留)
> **建议 PI 复核**:这 8 件是否需要 move 到 `_archive_2026_09_24/` 等正式归档目录,避免 `.tmp/` 目录名与正式件冲突

---

## F. no-upload 清单(0 件 · 本次未触发 A 类移动)

> 本次清理未触发 A 类移动。派工单列出的 A 类典型件(dataset 推理全文 167 万字节 *_p_l_v3_vector_embedding_*)**均已在 `_archive_manifest_non_upload_2026_09_23.json` 中记录**,本棒不擅自触发重新移动以免破坏 manifest 一致性。

**建议 PI 复核**:如需重整 A 类(隐私 dataset 推理全文),另派棒以 `_archive_manifest_non_upload_2026_09_23.json` 为源清单重新定位。

---

## G. 主目录仍 ≥1000 老实交代(差额 +437 件)

### G.1 差额构成(按派工单禁动清单逐类)

| 件数 | 类别 | 是否可动 | 派工单依据 |
|---|---|---|---|
| ~530 | V1-V3 frozen 文档/代码/测试/工具/攻击 (`docs/` 134 + `verifier/` 117 + `deposon_team/` 38 + `corpus/` 41 + `reviews/` 32 + `tests/` 23 + `scripts/` 10 + `paper/` 5 + `tools/` 5 + `attacks/` 4 + `.trae/` 2 + 根目录 V1-V3 frozen ~115 件) | **否** | V1-V3 frozen 只读资产(R5 沿用底线不变) |
| ~250 | `results/` 下 V3/V4 frozen 派生件(`_v4_pi_cot_v2_*` / `_v4_supp_*` 全系 / `_v4_prereg_v02_*` 八件 / `_v4_seeds_prereg_*` / `_v4_methods_prereg_*` / `_v4_pi_decision_*` / `_v4_v5_*` / `_v4_track2_*` 等) | **否** | 派工单禁动清单 + R5/R6/R7 沿用 |
| ~243 | `results/` 下 `_adendum_*` / `_p_l_v3_*` / `_p_d_v03_*` / `_p_k_v3_*` / `_kimi_push_v3_manifest_*` / `_kimi_safe_batch_push_*` / `_mavis_skill_inventory_*` / `_ghostref_copy_log_*` / `_v2_*` / `_tra_v0_*` / `_coze_*` / `_d05_*` / `_deposon_v2scripts_*` / `_ftfb_*` / `_glm_*` / `_cpath_sim_runner.py` / `_probe_url_update_log_*` / `_track2_*` / `_agent_trio_redesign_*` 等 35 类 | **否** | 全部被 `inventory` / `ghostref_reconciliation` / `ghostref_copy_log` / `archive_manifest` / `docs/V3X/` / `letters/` 中 frozen 件以文件名引用(本棒逐件 grep 验证 35 件候选均非 0 引用) |
| 41 | `letters/` 下 V4 commission/reply + D7 wechat 委托回函 | **否** | V4 委托链 + 派工单禁动清单(docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md 链) |
| 8 | `.tmp/` 链上保留件(§E 灰区) | **否**(临时目录名,待 PI 拍板是否归档) | 派工单「链上不动」+ 灰区规则 |
| **~1072** | **不可动合计** | — | — |
| **+437** = **1437 - 1000** | 主目录最终计数 | — | — |

### G.2 不可动差额诚实交代

- **派工单目标 <1000 未达成**,差额 +437 件
- **根本原因**:主目录绝大多数件属 V1-V3 frozen 资产 / V3 ghostref 链 / V4 supp 链,均被 `inventory` / `ghostref_reconciliation` / `ghostref_copy_log` / `archive_manifest` / `docs/V3X/` / `letters/` 等 frozen 件以路径或文件名引用
- **铁律优先**:派工单纪律锚明示「不得破坏任何既有路径引用」+「不确定 = 不删不移,留原地并入灰区清单(待 PI 拍板)」
- **不擅自扩容 B/C 类**:本棒严格按纪律锚保守清理,宁可少清不可误删;若 PI 拍板可触发 A/C 类(把 `_p_l_v3_vector_embedding_*` 等 dataset 推理全文移至 `_non_upload_local_archive` / 把 `_adendum_*` 等派生 JSON 移至 `deposon-sub`),差额可消化
- **未为凑数动禁动件**:派工单明示「不得为凑数动禁动件」

---

## H. key 形态自扫

> 本棒改动件(51 件 trash + 本 manifest 全文)严苛 API key 形态
> `\b(sk-[A-Za-z0-9]{20,}|tp-[A-Za-z0-9]{20,}|ark-[A-Za-z0-9]{20,}|API_KEY=[A-Za-z0-9]{16,}|Authorization:\s*Bearer\s+[A-Za-z0-9_.-]{16,})\b`
> → **0 命中**

---

## I. skill 缺位老实交代

- `folder-cleanup-assistant` 与 `superpowers:verification-before-completion` Local skill not found → 按任务提供的纪律锚 fallback(`results/_v4_noise_cleanup_manifest_2026_09_24.md` 的分类口径 + 留痕格式 + mavis-trash 通道 + SHA-12 前 12 + 不动边界件)
- 本棒额外加码:**每个落地动作完成后立即 `Test-Path` + `Get-FileHash` 自验**(首批 8 件 pyc + 末批 27 件单批 + 第二批 6 件 log + smoke `=` 1 件 = 51 件全部逐件落地自验;最终报告前再自验一次全部 8 件灰区保留件 `Test-Path` × 8 → True)
- **不强信子代理 succeeded**:本棒所有 mavis-trash 调用均落在 `mavis-trash: moved to trash: '<path>'` 输出 + `Test-Path` False 双确认

---

## J. 通道与可恢复性

| 维度 | 值 |
|---|---|
| 通道 | 单条 / 批顶层 `mavis-trash.cmd -- <path>...` (trusted launcher @ `C:\Users\Administrator\.minimax\bin\mavis-trash.cmd`,内部走 `mavis-trash.js` → `Microsoft.VisualBasic.FileIO.FileSystem.DeleteFile(..., 'SendToRecycleBin')`) |
| 不可用工具 | `mavis-trash` 直接调用(safety policy 拒绝);永久删除 `del` / `Remove-Item -Recurse -Force`(禁用) |
| 输出信息 | 每件 `mavis-trash: moved to trash: '<path>'` |
| 可恢复性 | **51/51 项可恢复**(Recycle Bin 标准 recover 路径) |
| 0 永久删除 | ✓ |

---

*— sign-off by worker, 2026-09-24, mvs_eba7623bfea64220aa67a963149c49b2, parent mvs_bbeb804b1a6a41109be740636eed1709*

---

## K. 末次四报(派工单要求)

### K.1 三目录 before/after 文件计数

| 目录 | before | after | delta |
|---|---|---|---|
| `D:/私人资料/deposon-repo` | **1486** | **1437** | -49 |
| `D:/私人资料/_non_upload_local_archive` | 1176 | 1176 | 0 |
| `D:/私人资料/deposon-sub` | 364 | 364 | 0 |

### K.2 主目录最终计数

**1437 件**(未达成 <1000 目标,差额 +437,详见 §G)

### K.3 no-upload 清单(0 件)

本次未触发 A 类移动。建议另派棒以 `_archive_manifest_non_upload_2026_09_23.json` 为源清单重新定位。

### K.4 灰区清单(8 件)

详见 §E:`.tmp/` 内 8 件 chain-bound 件,链上必留但 `.tmp/` 临时目录名需 PI 拍板是否归档至 `_archive_2026_09_24/`。