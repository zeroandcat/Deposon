# P-D 方向事实备忘（仓库只读核查，零推断，结论均挂出处）

> 核查人：戴夫-格式专家 ｜ 日期：2026-09-17 ｜ 仓库：deposon-repo（全程只读）

## 一、fail 记录核查（核心问题）

仓库内确有 **2 条 P-D 相关 fail 记录**，均非算法性失败：

1. **V0.1.1「A1 假性 FAIL」（2026-09-04）**：reviewer-a 报告指出，照 `P_D_FINGERPRINT_V0_SPEC.md` §6 命令字面执行 A1（`--missing docs/SPEC_GT8C.md`），A1 不删除该路径 → `compute_root` 正常返回 → verdict=FAIL，按"任一 FAIL → V0 死"将误杀 V0。定性：spec-CLI 衔接缺口（误杀），V0.1.2 改"无参 + 临时副本自建"修复。
   出处：`docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` L50；`docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` V0.1.2 注记；`docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` L13。

2. **exp_3_4 P-D supplement 失败（2026-09-16 12:35）**：corpus/v20/index.json 缺 captions 字段，报错 "only 0 captions, need 22"。
   出处：`deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` L59；`results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json`（键 `exp_3_4_p_d_supplement`）；本次复核 `corpus/v20/index.json` 顶层键（corpus/generator_version/spec/named_filler_rule/n_graphs/graphs）确无 captions。

**除上述外查无 P-D fail。P-D 终局判定全部 PASS**：
- V0 "9/9 PASS"：`docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` L16/L307；
- KT_D0 主版本+PD2 复现+EIS 独立三方收敛：`docs/V3X/KT_D0_SPEC_V0.1.md` L15；
- D7 V7 终判 P-D PASS（delta_hash 支撑不足）：`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` L48/L614；
- QUICK_KILL 方向 4 "已 PASS"：`docs/V3X/QUICK_KILL_6_DIRECTIONS.md` L59-64；
- 2026-09-17 四次 `_adendum_E_pd_supplement_v2_*.json`（133512/133705/133726/133852）复跑全 22/22 PASS。

## 二、实现思路演进链

1. **V0**（`P_D_FINGERPRINT_V0_SPEC.md`）：5 冻结工件**文件字节** SHA-256[0:12] 内容寻址（R1）+ manifest/根指纹/追加链/验证器边界（R2-R5）；§1 明文"V0 不包含二叉 Merkle 聚合"。
2. **V0.1→V0.2**（`PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`，2026-09-11 F-4）：对象转 22 caption；`byte_hash`=SHA-256(**caption_id**)[0:12]（哈希输入由文件字节改字符串 id）；新增 `semantic_hash`=12-bit LSH（SVD-2 坐标 × 12 超平面，np.random.seed(42)，3 hex）；`dual_24bit`=byte_hash[:6]+semantic_hash（9 hex=36 bit，名 24 实 36）；判据类内 Hamming<6 bits/12，实测 0.57-2.8（`D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` L33）。delta_hash 后判"支撑不足"退回 byte+semantic（D7 V7 L157/L280）。
3. **B3 Merkle 层**（`P_F_V0_1_UPGRADE_2026_09_11.md` §2.3）：3 根锚 `7d6d3d39fad8`/`f88d855aaf83`/`e66e44e63f5a`（V0.1 主版本+PD2 复现+EIS 独立）——V0 明文排除的 Merkle 自 P-F 侧引入。
4. **KIMI B3 核验**（2026-09-16，`P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md`）：复算 vs 既有两份实测 22/22、链 22/22 PASS、frozen corpus SHA 前后不变；"非标说明"实锤：`deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py` L188-190 对 **caption 文本**（非 caption_id）SHA-256 纯 6+6 截段、无语义层，判非标（KIMI 裁定 spec 优先）。

## 三、GLM「思路独特致 fail」假设对照

- **支持面**：P-D 链确高度自研定制（文件锚闭环+验证器状态机+seed-42 LSH+22 caption 专用素材）；09-16 同日两种互斥 dual_24bit 实现并存且其一被判非标；2026-09-16 fail 正是复现侧线依赖 corpus captions 字段（不存在）所致——与"思路独特导致复现失败"相容。
- **不支持面**：两条 fail 根因分别为 spec-CLI 缺口（假性 FAIL 已修）与 frozen corpus 数据字段缺失，均非算法/思路性失败；主线终局全 PASS。故"之前 p-d 实验 fail"若指算法 fail，仓库证据不支持；若指复现/验证尝试 fail，与 exp_3_4 记录吻合，直接原因是数据前提缺失而非"思路独特"本身。
