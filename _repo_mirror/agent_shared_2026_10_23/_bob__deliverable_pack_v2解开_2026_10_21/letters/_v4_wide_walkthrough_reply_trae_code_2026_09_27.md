# 回函（扩大范围）：全仓新件走读 + 直接修复 + 缺陷登记 · Trae code → deposon PI

> **回函方（受托方）**：Trae code
> **授权**：PI 2026-09-27 指令字面「**扩大走读范围，deposon-repo 与 deposon-sub 的自上次走读即 9 月 23 日中午起全部新文件，直接修 bug，写完整回函**」
> **范围**：`_repo_mirror` 与 `_repo_mirror` 内 **mtime ≥ 2026-09-23 12:00** 的全部新件 = **460 件**
> **方法声明**：0 LLM 调用 / 0 外部 URL / 0 明文密钥；**18 frozen / 9 网格 / P-G v0+v01 / plugin spec / verifier 内置 / V4 `_v4_*` 全链 0 触动**；**0 擅调阈值**；0 新增外部文献号。
> **诚实纪律**：凡「已修 / 已验」均附实测命令与读数；凡未跑、未独立复核者一律写明「未跑 / 未复核」。**测量仪器自身的误差也一并登记**（见 §5）。

---

## §0 范围盘点与方法

### §0.1 新件盘点（mtime ≥ 2026-09-23 12:00，两仓）

| 归组 | 件数 |
|---|---:|
| `deposon-repo/results` | 289 |
| `deposon-repo/.tmp` | 87 |
| `deposon-repo/deposon_team`（含 `plugins/`） | 33 |
| `deposon-repo/letters` | 27 |
| `deposon-sub/results` | 7 |
| `deposon-sub`（根） | 6 |
| `deposon-repo/corpus` | 5 |
| `deposon-repo/.mavis` | 4 |
| `deposon-repo`（根） | 1 |
| `deposon-repo/docs` | 1 |
| **合计** | **460** |

其中 **`.py` 186 件**（其余为 md / json / txt / ps1 / pyc）。

### §0.2 走读方式（三路并行）

1. **机扫面**（受托方本机实跑，5 个扫描器）：全量 `compile` 语法检查 / tokenize 级无效转义 / BOM / `__main__` guard / 仓外绝对路径 / 密钥样式正则；**引用图**（谁能安全原地改）；修复执行 + 后验证。
2. **人读面**（3 个只读走读棒，逐件读全文）：letters 簇 25 件 / LLM 补充链 56 executor + 53 result + 8 预登记 / `_v4_pi_cot_v2_*` + `_v4_track2_*` + `_v3n_*` + corpus + deposon-sub 全件。
3. **交叉面**：关键读数**独立重算**（见 §3）。

### §0.3 全量编译结果（机扫）

**186 件新 `.py` 全部 `compile()` 通过 —— 0 语法错误、0 真实无效转义。** 这是本轮唯一「零 defect」的面。

---

## §1 直接修复（本轮实际写入 26 件，全部可复算）

### §1.1 修复判据：**先判「能否安全原地改」**

受托方先建**引用图**（谁的新件文本里含谁的 SHA-12）——结果：**186 件新 `.py` 中 72 件被其它件引用、114 件未被引用**。

**关键安全发现（决定了本轮修法）**：

> **执行器 SHA-12 被跨批引用。** 例：`_v4_supp_l14v3_batch10_r2_executor.py` 与 `batch10_r2_result.json` 均记录 `batch10_r1_executor.py` 的 SHA-12 `d4dd5c949443`；`_v4_supp_t15_verdict.md` / `t15r2_verdict.md` 记录 `t15`/`t15r2` executor 的 SHA-12；`batch10_r1` 被引 **8 处**、`r2` 6 处、`r3` 4 处、`r4` 2 处。⇒ **对「被引件」原地改 = 制造跨件 stale 锚**。

**据此定修法**：**只对「未被任何新件引用」的 114 件中的有缺陷者原地修**；**被引件的缺陷一律只登记**（§2）。这一约束与项目既有「只追加不回改 / 修复落新名」纪律同源。

### §1.2 修复清单（改前 → 改后 SHA-12 全登记）

| # | 修复项 | 件 | 改前 SHA-12 | 改后 SHA-12 |
|---|---|---|---|---|
| **F1** | `load_checkpoint` 静默 `return []` → **响亮告警**（返回语义不变） | `results/_v4_supp_t1_executor.py` | `a7cad9228b0b` | **`91b8f70e4e18`** |
| **F2** | 去 UTF-8 BOM（×8） | `.tmp/_pk_probe.py` | `89f83e4b8e72`ᴿ | `6d79ba939526` |
| | | `.tmp/_pk_probe2.py` | `f0b2e0374213`ᴿ | `caea18365be2` |
| | | `.tmp/_pk_probe3.py` | `e4effb76141d`ᴿ | `4c1bab003027` |
| | | `.tmp/_pk_probe4.py` | `e16c7d5594d5`ᴿ | `999d874ceaaf` |
| | | `.tmp/_pk_probe5.py` | `18fe1283c34a`ᴿ | `1a3c047f383a` |
| | | `.tmp/_pk_probe6.py` | `83da3c8f350d`ᴿ | `0a6b41b66e67` |
| | | `.tmp/_pk_probe7.py` | `411614832b1e`ᴿ | `b666ed0b024f` |
| | | `.tmp/_pk_probe8.py` | `b0d316eb7f43`ᴿ | `b292c8b9152e` |
| **F3** | `fetch_key` 裸 `except:` + `text` 未定义路径 + 行界缺失 → 具名异常 + 显式报错 | `results/_v4_track2_models_probe.py` | `b1f5de36f5a2` | **`da62abaa1e03`** |
| | | `results/_v4_track2_reprobe.py` | `c7dcc4fc6771` | **`f92cc93f1304`** |
| **F4** | 硬编码仓外 key 路径 → **`os.environ["DEPOSON_KEY_FILE"]` 可覆盖**（默认值不变 ⇒ 行为不变） | `results/_v4_supp_l14v3_batch10_r5_executor.py` | `6f4baac525a0` | `04383377b6a2` |
| | | `results/_v4_supp_l14v3_batch2_r5_executor.py` | `56b37db28600`ᴿ | `bf1e4fe02402` |
| | | `results/_v4_supp_l14v3_batch2_r6_executor.py` | `8c7b79dadd0d`ᴿ | `e38d068f309c` |
| | | `results/_v4_supp_l14v3_batch3_r1_executor.py` | `a4731b39343f`ᴿ | `0c284a3dce21` |
| | | `results/_v4_supp_l14v3_batch3_r2_executor.py` | `540c9369dd36`ᴿ | `b1699098c53b` |
| | | `results/_v4_supp_l14v3_batch3_r3_executor.py` | `1b3861943b7e`ᴿ | `3b7381ce5fe8` |
| | | `results/_v4_supp_l14v3_batch3_r5_executor.py` | `ccfaeb115b61`ᴿ | `b7478168f87f` |
| | | `results/_v4_supp_l14v3_batch5_r1_executor.py` | `ef26adf4669f`ᴿ | `dac0648507b9` |
| | | `results/_v4_supp_l14v3_batch5_r2_executor.py` | `f97e46e3739e`ᴿ | `4c40334929bb` |
| | | `results/_v4_supp_l14v3_batch5_r3_executor.py` | `027ef71c0668`ᴿ | `ed9557830f8b` |
| | | `results/_v4_supp_l14v3_batch7_r5_executor.py` | `e00f296ceaca`ᴿ | `38710a448e9c` |
| | | `results/_v4_supp_l14v3_batch9_r5_executor.py` | `56bd65d5013f`ᴿ | `9b1a82a28dfb` |
| | | `results/_v4_supp_l14v3_batch2_r2_models_probe.py` | `facd5d406ced`ᴿ | `a31d54a4b765` |
| | | `results/_v4_track2_endpoints_probe.py` | `a70ab74f9f8c`ᴿ | `e7a6eb42c0af` |
| | | `results/_v4_track2_multimodel_rerun.py` | `295963552fc5`ᴿ | `5c0983eaaf11` |
| | | `deposon-sub/results/_track2_qwen_check_2026_09_23.py` | — | **未改**（该件 key 变量名为 `KEY_SOURCE`，与 F4 目标字面不同形 ⇒ 未误改，如实交代） |

> **`ᴿ` = 改前值由当前字节「逆变换重建」而非修复前快照**（F2：前置回 BOM；F4：env 覆盖式换回硬编码）。逆变换为**精确可逆**（单点替换），故 F2/F4 的重建值可信；**但受托方本轮未留修复前快照，属留痕不足，如实交代**。
> **F1/F3 的改前值取自修复脚本实测**（`a7cad9228b0b` / `b1f5de36f5a2` / `c7dcc4fc6771`），精确。

---

## §2 只登记不修（被引件 / 证据件 / 结论层 —— 共 22 条）

> 判据：① 被其它件引用（改动即造 stale 锚）；② 属已扩散/已上传件（`_v4_commission_*` 等已由 KIMI 上传 42 件至 GitHub ⇒ **已扩散 ⇒ A 档：不动原件 + 补口径说明**）；③ 结论层（改 = 翻案）。

### §2.1 高严重度（6 条）

| # | 宿主件 + 位置 | 现象（已核验） | 核验方式 |
|---|---|---|---|
| **R-1** | `_v4_supp_t1/t15/t15r2_executor.py` L433-439；`_v4_supp_l14v3_batch1..batch10` 同构（**56 件**） | `load_checkpoint` 静默 `except Exception: return []` ⇒ checkpoint 半写/损坏时**静默重置为空**，续跑会为已记录 caption 重发 calls（配额/样本重复）且 0 日志。**被引件，未改**（仅 `t1` 未被引用，已按 F1 修） | 受托方逐行实测 ✅ |
| **R-2** | `_v4_supp_l14v3_batch10_r*_executor.py` L355 | `minimax_distill_meta["proxy_used"] = False` **硬编码**；随后 `no_proxy_used_count` 由该同一字段派生出 `no_proxy_compliance` ⇒ **自证式**（该字段永不可能为 True）。**实测值与正确值同（batch10 确未走代理），故任何历史读数不变**。**被引件，未改** | 受托方逐行实测 ✅（`proxy_used=False` 出现 2 次/件，r1–r5 一致） |
| **R-3** | `_v4_supp_l14v3_batch*_executor.py` L506-508 / L780-782（**56 件**） | `tun_compliance = (tun_used_count == total_calls)`，而 `tun_used_count` 的判据是 `per_call_metadata["endpoint"].endswith("/chat/completions")` —— **只查 endpoint 字符串，不验是否真穿 tun 代理** ⇒ 对任何记录恒成立（端点由本脚本硬编码为 teamo `/chat/completions`）。**注意**：落盘字段名为 `tun_compliance_teamo_endpoint`（**名实相符**），故严格说是「口径读法提示」而非代码 bug；但若被读作「已验走走 tun」，即**证据链自我形式化**。**被引件，未改** | 受托方逐行实测 ✅ |
| **R-4** | `deposon-sub/results/_test_conv_out.txt`（7,568 B） | **实为 `_v4_pi_cot_v2_dataset_addendum_d2b` JSON**，却以 `.txt` 命名；含 **UTF-8 BOM**（`json.load` 直读失败）；且 `fingerprint_self_hash_after_birth` = **占位值 `aaaaabbbbbb`**（两次写入的自指哈希未完成第二遍） | 受托方实测 ✅（BOM 确认、`"aaaaabbbbbb" in t` = True） |
| **R-5** | `_v3_n_recheck_llm_verdict_2026_09_27.md` §2.2/§5 vs `_v3_n_cpath_live_data_2026_09_27.json` | 判决件称 embedding 6/6 成功、top-3 30/30、with-RAG 30 完成、成功调用 18；**数据件实测 `outcome=BLOCKED_BY_ENDPOINT_QUOTA`、`total_calls=1`、`with_rag=[]`** ⇒ **同一实验两份记录互斥** | 子代理所报；受托方**未独立复核**（见 §5） |
| **R-6** | `_v4_commission_paper_final_glm_2026_09_24_v3.md` L6/§Z L167/§7 L155；`_v4_commission_〔IM〕_report_coze_2026_09_24_v3.md` 同构；`_v4_commission_upload_executor_2026_09_24_v3.md` 同构 | 三组 v3 委托信均把 **v2 槽位错挂 v1 的身份值**（paper：10,515/`53A425FE1BD2`；〔IM〕：7,197/`15F8227308BC`；executor：13,012/`ADFA7DD03F76`），件内各 3 处一致重复；且 §Z **均漏列 v1 行**。真值见各组 v2 §Z 与 v4 §Z。**已扩散（v3 族已上传）⇒ A 档：不动原件** | 子代理所报（值对值比对）；受托方**未逐件复核** |

### §2.2 中严重度（9 条）

| # | 宿主件 + 位置 | 现象 |
|---|---|---|
| **R-7** | `_v3_calibration_change_note_for_coze_glm_2026_09_27.md` §2.8 L329 | 把**在盘件** `results/deposon_v20_baselines.json`（16,987 B / `6EDB2AEC1660`）仍列为「3 件真缺件…不再补件」⇒ 与 09-27 同日 `_v3_recheck_*`（明确「在盘」）**直接冲突** |
| **R-8** | `_v4_pi_cot_v2_result_v2.json`(`v1_to_v2_diff_summary`) / `_v4_pi_cot_v2_coding_review_2026_09_26.md` §2.3 vs `_v4_pi_cot_v2_ruleset_v2.json`(`v2_keyword_count=263`) | v2 词表总数 **201 vs 263** 两口径并存（逐类求和 = 32+26+74+37+48+46 = 263）。受托方**独立复核：263 为 ruleset_v2 自算值** |
| **R-9** | `_v3_supplement_verdict_2026_09_23.md` §1 C3/C4 vs `_v3_construct_degradation_diag_2026_09_23.json` | C3 分布：MD 写 14/22=1 + 8/22=200，**JSON 实为 `{1:18, 200:4}`**；C4：MD 写「16/4/2」，JSON 为 `{1.0:4, 2.0:2, 200.0:16}` ⇒ **互斥** |
| **R-10** | 9 件 `_v4_pi_cot_v2_dataset_addendum_*` 的 `fingerprint_self_hash_after_birth` | **自报指纹与实测 SHA-12 普遍漂移**（d1 自报 `6F76EAE13FA0` vs 实测 `172093A23E4B`；d2/d2b/d2c/d2d/d2e/d3a/d3b/d3c 同型）；且 `coding_review` §5.7 只列 2 件漂移，与 d3c 自述「七件漂移」**不一致** |
| **R-11** | `_v4_commission_upload_channel_authorization_2026_09_26.md` §2.4 L149（「E-1…E-36」）vs §4.2 L214（v18 = +E-35 6 子条） | **同件内 E-35 / E-36 边界自相矛盾**；并波及 `_v4_commission_〔IM〕_report_coze_reply_v4…md` L49「239,387 版已含 E-35」的**版本归属冲突** |
| **R-12** | `_v4_supp_l14v3_batch1_executor.py` L504-508 等（`tun_compliance` 判据） | 见 R-3（同源） |
| **R-13** | `_v4_commission_upload_executor_reply_v3_2026_09_24.md` L14 | 表头「**43** 项（Tag-A 30 + Tag-B 10 + E 表内 3）」，与本件 §2 表 **44 行** 及源件 v3 §2.4 的 **4 件 E 表** 均不符 |
| **R-14** | `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` L22/L526 | 记 `add_T1` = **48,738 B**；而 `add_T15` / `add_T15r2` 两件与 `_v4_evidence_audit_reconcile_2026_09_26.md` L136 均记 **52,942 B / `802DECE2286A`** ⇒ **L14V3 件为陈旧值** |
| **R-15** | `_v4_supp_t15r2_executor.py` L13/L1320/L1487 vs `_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | executor 自报「+**62** calls（cell 2/3 各 11）」vs 预登记「+**60** calls / 180」⇒ **计数口径不一致** |

### §2.3 低严重度（7 条）

| # | 宿主件 + 位置 | 现象 |
|---|---|---|
| **R-16** | `_v3_v4_achievements_inventory_2026_09_24.md` §2.2 | 把 `_v4_pi_cot_v2_result.json` / `_verdict.md` / `_prereg.md` 记为 **NOT-ON-DISK**（误报）；其勘误件 E1 已更正为 MATCH，**原盘点件未回改**（遗留） |
| **R-17** | `deposon-sub/_tmp_v2_redesign.py` `KW_V2` vs `_v4_pi_cot_v2_ruleset_v2_executor.py` `KEYWORDS_V2` | 两个「v2 词表」版本**内容不一致**（如「没资源」vs「没钱/资源不够」，另有多处重复词）⇒ 可复现性风险 |
| **R-18** | `_v4_commission_paper_final_glm_2026_09_24_v4.md` §Z L252 / `_v4_commission_〔IM〕_report_coze_2026_09_24_v4.md` §Z L194 | 自记字节 31,167 / 21,069；实测为 **31,531 / `D5337702CEC9`**、**21,433 / `802C705E1469`**（增补函 §3 L58-59）⇒ 出件后追加致自记值过期 |
| **R-19** | `_v4_maindir_cleanup_manifest_2026_09_24.md` / `_v4_noise_cleanup_manifest_v2/v3…md` | 多轮出现 `after − before ≠ 实际删除数`（如 1437→833 差 −604 ≠ −6；945→908 差 −37 ≠ −47）——文内已老实交代「活态计数」，但数字非确定性 |
| **R-20** | `deposon-sub/_check_conv_archive.ps1` 末尾 | `---DONE---` 后又 `Write-Output 'DONE'` + 4 空行（冗余死输出） |
| **R-21** | `_v4_track2_multimodel_verdict_2026_09_23.md` §4 | 称自扫「11 模式」，`rerun.py` 的 `SENSITIVE_PATTERNS` 实为 10 个（endpoints_probe 6 个） |
| **R-22** | `.tmp/_aggregate_10cells.py` v1 与 `_v4.py`（**均未被引用，可修未修**） | v1 每 cell 只取「最后一个 batch」的四元组，v4 改为跨 r1–r6 累加 ⇒ **同一 10 cells 出现两套四元组集合**，下游 `_compute_metrics*` 读数随脚本版本漂移。**受托方本轮未修**（属方法学分歧，非机械 bug，须 PI 定「哪套为准」后再修） |

---

## §3 关键读数独立重算（交叉面）

受托方与走读棒对下列读数做了**独立重算**，结果**全部吻合**：

| 对象 | 记录值 | 独立重算 | 结论 |
|---|---|---|---|
| `_v4_pi_cot_v2_result.json` mean_similarity | 0.1818 | 2.0 / 11 | ✅ |
| 同上 div_critical_coverage | 0.6667 | 6 / 9 | ✅ |
| `_v4_pi_cot_v2_result_v2.json` mean_similarity | 0.0909 | 2.0 / 22 | ✅ |
| 同上 div_critical_coverage | 0.6842 | 13 / 19 | ✅ |
| 同上 blind_obey_rate | 0.3333 | 1 / 3 | ✅ |
| `_v3_n_pg_boss_live_data` PG-1 median δ | 0.041495 | 0.041495 | ✅ |
| 同上 PG-3 median violation | 3.5599e-16 | 3.5599e-16 | ✅ |
| `corpus/caption_stats_22.json` text_len_mean | 200.41 | 4,409 / 22 | ✅ |
| `_ghostref_copy_log_2026_09_23.json` copy_count | 308 | 308（`COPIED` 计数） | ✅ |
| `_archive_manifest_deposon_sub_2026_09_23.json` 件数 | 364 | 364 | ✅ |
| `_v4_pi_cot_v2_result.json` label_distribution 合计 | 37 | 37 | ✅ |
| `_v4_pi_cot_v2_result_v2.json` label_distribution 合计 | 72 | 72 | ✅ |
| `_v4_supp_l14v3_batch10_r1_result` 内部计数 | — | 与 executor 累计式一致 | ✅ |

**⇒ 主干数值链独立复算全部吻合**；本轮缺陷集中在**引用面 / 计数口径 / 自报指纹 / 状态词**，**不在数值链本身**。

---

## §4 验证记录（0 跑过的不许写成已验）

| 项 | 命令 / 方式 | 结果 |
|---|---|---|
| **全量语法检查** | `python -B` 对 186 件新 `.py` 逐件 `compile()` | **0 语法错误** |
| **无效转义（真语义级）** | tokenize STRING token 级、raw 前缀跳过、合法转义白名单 | **0 处** |
| **修复后验证** | 26 件改后逐件 `compile()` | **全部 OK** |
| **引用图构建** | 对 460 件新件全文检索 186 个 `.py` 的 SHA-12 | 72 件被引 / 114 件未引 |
| **密钥样式全量扫** | 460 件、8 类正则（含 volcengine UUID 型） | **真 key 0 处**；2 类命中经复核**均为仪器误报**（见 §5） |
| **本函脚本** | `_v4_wide_s1_inventory` / `s1b_inv2` / `s2_scan` / `s3_keyscan` / `s3b_uuidctx` / `s3c_keydetail` / `s4_verify` / `s5_prescan` / `s6_unrefscan` / `s7_fix` / `s8_fix3` + 本函 | **实跑 exit 0 × 12** |
| **冻结链 0 触动** | 18 frozen / 9 网格 / P-G v0+v01 / plugin spec / verifier 内置 / V4 `_v4_*` 全链 | **0 触动** |
| 密钥 / 外部依赖 | 本函与全部新增件 | **0 明文密钥 / 0 LLM / 0 外部 URL** |

---

## §5 老实交代

### §5.1 受托方**自己的测量仪器误差（3 处，主动登记）**

沿项目「测量仪器自身即误差源」纪律，先审自己的扫描器：

| # | 误报 | 真相 |
|---|---|---|
| **I-1** | 首轮密钥扫报 **1,743 处 `ark_uuid`** 命中（`_l14v3_aggregated_10cells.json` 等） | 复核后**全部为 API 响应的 `"id"` 字段**（与 `model_returned` / `usage` / `latency_ms` 同现；全文 `key` / `authorization` 命中 **0**）⇒ **非密钥**。**仪器的 UUID 正则是高误报类** |
| **I-2** | 该轮另报 **1 处 `api_key_literal`**（`_track2_qwen_check_2026_09_23.py` L96） | 复核后为 `api_key = read_key_runtime(...)` —— **正则把函数名 `read_key_runtime` 误当字面量**（因 `api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{16,}` 未要求引号）⇒ **非密钥** |
| **I-3** | 首轮 `ODD_ESCAPE`（无效转义）报多处（承 09-23 轮 r4 扫描器同一缺陷） | tokenize 级精扫后**真无效转义 = 0**（原命中全为 `Path(r'〔本机路径〕\...')` 等 **raw string** 的假阳性）⇒ **仪器误差，非文本缺陷** |

**⇒ 密钥面结论以 §1/§4 为准：本轮 460 件新件内真 key 0 处。** 受托方**只修仪器、不修文本**（I-1/I-2 的正则已在本轮脚本中收窄）。

### §5.2 未独立复核项（不掩盖）

1. **R-5（#32 CPATH 判决 vs 数据互斥）、R-6（三组 v3 委托信 v2 槽位错挂）、R-8（v2 词表 201/263 的编码器侧）、R-9（C3/C4 分布）、R-10（9 件 addendum 指纹漂移）** —— 系走读棒所报，受托方**只独立复核了 R-8 的 ruleset 侧（263）**，其余**未逐件复核**，请 PI 以原件为准再核。
2. **`.pyc` 面**：`results/_v3_recheck_26b_executor…pyc`、`results/_v3_s1_executor/__pycache__/…pyc` 等在盘；本轮**未清理**（属环境派生物，口径建议沿 09-27 回函 §C.3）。
3. **`.tmp` 内 87 件**：本轮**未逐件精读**（多为探针脚手架；已做全量机扫）。
4. **`_v3_v4_achievements_inventory_2026_09_24.md`（192 KB）/ `_3dir_2026_09_24.md`（355 KB）/ `_ghostref_reconciliation_2026_09_23.md`（165 KB）/ `_archive_manifest_non_upload_2026_09_23.json`（139 KB）** —— 采用抽读 + 定向 grep，**未逐行读全**。
5. **F2/F4 的「改前 SHA-12」为逆变换重建值（标 `ᴿ`），非修复前快照** —— 逆变换精确可逆（单点替换），故重建值可信；但**本轮未留修复前快照**，属**留痕不足**，如实交代。若 PI 要求「快照级」证据，受托方可在下一轮以 `.bak` 快照方式重做（沿 E-15 处置时的做法）。

### §5.3 受托方**未做**的事

- **未改任何被引件 / 已扩散件 / 冻结件 / 结论层**；本轮唯一写入 = §1 的 **26 件「未被引用」件**。
- **未代 PI 择一**：R-22 两套四元组口径、R-8 词表口径、R-14/R-15 计数口径、R-1/R-2/R-3 是否回改被引执行器（须另立新名件）—— **全部留 PI 拍板**。
- **未删任何件**（含 `_test_conv_out.txt`、`.pyc`、`.tmp` 残留）。

### §5.4 一句话总纲

> 460 件新件：**语法面零缺陷**（186 件 `.py` 全 compile 通过）；**密钥面干净**（真 key 0 处，2 类命中皆为受托方自己的仪器误报）；**数值主干独立复算全吻合**。
> **已直接修 26 件**（未被引件：1 处静默 checkpoint + 8 处 BOM + 2 处 `fetch_key` 裸 except/未定义变量 + 15 处仓外 key 路径硬化）。
> **只登记 22 条**（6 高 / 9 中 / 7 低），其中最须 PI 裁决的是：**R-1/R-2/R-3 三处系统性执行器缺陷（56 件同构，因 SHA 被跨批引用而不可原地改）**、**R-4 占位哈希残留件**、**R-5 同一实验两份互斥记录**、**R-6 三组 v3 委托信的 v2 槽位错挂**。

---

*出证：Trae code · 2026-09-27 · 本函 SHA-12 见落盘报值*
*配套脚本 12 件（落 `deposon_team/plugins/`，均以 `_v4_wide_` 起头、`_2026_09_27` 结尾）*
