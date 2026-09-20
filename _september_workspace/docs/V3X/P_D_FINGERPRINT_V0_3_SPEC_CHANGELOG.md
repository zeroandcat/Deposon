# P-D 可审计账指纹协议 V0 → V0.2 → V0.3 演进链 CHANGELOG

> **作者**: doc-writer 凝子-agent (agent-0032834a3e04)
> **日期**: 2026-09-17 15:11 CST
> **位置**: `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md`
> **关联**: `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md`（V0.3 主 spec，副文档）
> **作用**: 透明化 V0 → V0.2 → V0.3 三版本演进过程，便于审查与回退

---

## 0. 一句话演进结论

P-D 协议历经 3 个版本迭代（V0 → V0.2 → V0.3），**3 版本共存**于 `docs/V3X/` 各自独立路径，互不覆盖：

| 版本 | 文件 | 字节数 | SHA-12 | 状态 | 关键特征 |
|---|---|---|---|---|---|
| **V0** | `P_D_FINGERPRINT_V0_SPEC.md` | 9,192 B | `3b67461b05fe` | 冻结 (2026-09-01) | 5 锚 manifest 字节指纹层，R1-R5 |
| **V0.2** | `PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 B | `c165cd33a362` | 冻结 (2026-09-11) | 22 caption dual_24bit 语义指纹层 + LSH-12bit |
| **V0.3** | `P_D_FINGERPRINT_V0_3_SPEC.md` | (本副文档对应) | (TBD) | 新增 (2026-09-17) | V0 + V0.2 + 6 改进文档化升级版 |

---

## 1. V0 → V0.2 升级点（2026-09-01 → 2026-09-11）

### 1.1 触发背景

P-D V0 仅用 `SHA-256(caption_id)[0:12]` 算 byte_hash，这是基于字符串的指纹，**对同源 caption (如 L 家族 6 个) 无任何区分度**(全部独立 hash)。

### 1.2 升级变更（6 项）

| 编号 | 变更类型 | V0 状态 | V0.2 增量 | 出处 |
|---|---|---|---|---|
| **V0.2-N1** | 新增字段 | V0 仅 byte_hash (12 hex 字符串级) | 新增 semantic_hash (3 hex 12-bit LSH from SVD-2) | V0.2 §2 + §3 |
| **V0.2-N2** | 新增字段 | V0 无 | 新增 dual_24bit (byte_hash[:6] + semantic_hash = 9 hex 名 24 实 36) | V0.2 §2 |
| **V0.2-N3** | 新增算法 | V0 仅 SHA-256 | 新增 12-bit LSH（12 hyperplane sign，`np.random.seed(42)` 固定） | V0.2 §3 |
| **V0.2-N4** | 新增实测数据 | V0 仅 5 锚 SHA-12 | 新增 22 caption 实测表（22 行 dual_24bit） | V0.2 §4 |
| **V0.2-N5** | 新增验证手段 | V0 仅 5 锚 manifest + 攻击 3/3 | 新增类内 Hamming 距离（4 档家族聚集：L 2.47 / S1 2.67 / S2 2.80 / S3-S6 0.57 bits/12） | V0.2 §5 |
| **V0.2-N6** | 后续工作预留 | V0 无 | V0.3 候选（embedding-2048-d 直接 LSH-128bit / permutation-based LSH / fingerprint 模块集成） | V0.2 §7 |

### 1.3 V0 主体保持冻结

- §0 标题 + 5 锚清单（R1 内容寻址 + R2 manifest + R3 根指纹 + R4 runs 链 + R5 验证器安全边界）
- §1 目标与范围
- §3 数据结构伪代码
- §4 三类攻击 → 检测信号映射（A1 删锚 / A2 洗 manifest / A3 改运行链）
- §5 实现接口签名（`compute_root / verify_root / append_run / read_runs_count / verify_chain`）
- §6 判死线（机械命令模板）
- §7 接口预留位

### 1.4 V0 → V0.2 严守 7 铁律

- 0 新 API 调用（仅用既有 `volcengine_22caption_embedding_2026_09_10.json` SVD-2 坐标）
- 0 触动 5 锚 SHA-12 锁（`7d6d3d39fad8` unchanged）
- 0 触动 `corpus/v20/index.json`
- 0 触动 4 SPEC V0.1 + v19 + v21
- 严守 user 17:38（仅火山 catalog）+ 17:41（仅 coding-plan）

### 1.5 V0 → V0.2 终局 PASS

- 22 caption dual_24bit 22/22 一致（spec 复算 = F4 = v3phys 三方一致）
- B3 sequential chain 链式核验 22/22 PASS（root=`75596bbabdb8`，锚链=`c4cae1ed9ee5`）
- KT_D0 V0.1 spec 引用 P-D V0.1 + PD2 + EIS 三组独立实验 + 3 根指纹逐位一致（已闭合）

---

## 2. V0.2 → V0.3 升级点（2026-09-11 → 2026-09-17）

### 2.1 触发背景

P-D 终局全 PASS 后（V0 9/9 + KT_D0 三方收敛 + D7 V7 终判 + QUICK_KILL 方向 4 + 4 次复跑 22/22），仓库内 2 条 P-D 相关 fail 记录均非算法性：
- **V0.1.1 "A1 假性 FAIL"**（spec-CLI 衔接）
- **exp_3_4 corpus captions 字段缺失**（数据完整性）

机制本身无 fail 实证（三方 22/22 复算一致，root=75596bbabdb8，锚链 B3 canonical c4cae1ed9ee5）。

**鲍勃凝子-agent §4 推荐**：spec 升级 (V0.2 → V0.3 文档化)，零重算，frozen 0 触动。

### 2.2 升级变更（6 项，V0.3-N1 ~ V0.3-N6）

##### V0.3-N1（最高风险）— hash 输入三口径统一

**V0/V0.2 状态**：
- 口径 A (V0 spec R1)：文件字节 → SHA-256 → 前 12 hex（仅 5 锚 manifest）
- 口径 B (V0.2 spec §2)：caption_id 字符串 → SHA-256 → 前 12 hex（22 caption byte_hash）
- 口径 C (P-O runner 非标 L172-197)：caption 文本 → SHA-256 → 截 12 hex → 6+6 拼接（**非标**，KIMI 报告 §1 已判）

**V0.3 增量**：
- P-D 范围内 22 caption 语义指纹**只允许口径 B**（caption_id 字符串）
- V0.3 §2.1 / §2.2 / §2.3 / §4 任何 hash 计算必须显式标注输入口径（"文件字节" / "caption_id 字符串" / "其他"）
- 口径 C 维持非标裁定（KIMI 报告 §1 沿用）

**diff 摘要**：新增 §3.1 N1 章节（共 30 行）+ §4.1 表格加注口径列 + §4.2 表格加注口径列。

##### V0.3-N2（低）— dual_24bit 名 24 实 36

**V0.2 状态**：命名 `dual_24bit` 但实际 9 hex = 36 bit（历史命名原因：早期曾考虑 dual = 12 bit + 12 bit = 24 bit 组合，后调整为 `byte_hash[:6] + semantic_hash` = 6 hex + 3 hex = 9 hex = 36 bit，名称沿用未改）。

**V0.3 增量**：
- 保留 `dual_24bit` 旧名（向后兼容，老数据不动）
- spec 加注 "名 24 实 36 (9 hex = 36 bit)"
- 替代命名 `dual_36bit` 仅在 V0.3+ 新代码中可选用

**diff 摘要**：新增 §3.2 N2 章节（共 15 行）+ §4.1 表格 dual_24bit 列名加注 "(名 24 实 36)"。

##### V0.3-N3（中）— "B3 Merkle" 实质是 sequential chain

**V0.2 + KIMI 报告 §5 状态**：命名 "B3 Merkle"，但实质是顺序链 + 2 级 anchor 延伸，**非 RFC6962 二叉 Merkle 树**。

**V0.3 增量**：
- 保留 "B3 Merkle" 旧名（外部引用稳定）
- spec 加注 "非 RFC6962 树，是顺序链 + 2 级 anchor 延伸（state_i = SHA(state_(i-1)|caption_id|dual_24bit)，再 SHA 2 次得 merkle_root）"
- 替代命名 `B3 sequential chain` 仅在新文档中可用

**diff 摘要**：新增 §3.3 N3 章节（共 18 行）+ §2.3 章名改 "B3 sequential chain 链式层" + §4.2 章名改 "B3 sequential chain 链式核验"。

##### V0.3-N4（中-高）— 语义层上游 SVD 推导细节文档化

**V0.2 状态**：spec §3 只说 "22 caption SVD-2 坐标 (从 volcengine_22caption_embedding_2026_09_10.json)"，未文档化上游推导细节（中心化 / 符号约定 / 库 / 截断）。

**V0.3 增量**：
- 5 步推导文档化：doubao-embedding-vision-251215 API → 22 × 2048-d → 中心化减均值 → SVD 截断取 V[:, 0:2] → dict[caption_id]=(x,y) → 12 hyperplane LSH (np.random.seed(42) 固定)
- 库依赖文档化：`numpy.linalg.svd` + `np.random.randn` + `hashlib.sha256`（无第三方 LSH 库）
- 重推须重调：API endpoint / model name / prompt template / centroid / SVD 截断 / 符号约定 / seed 任一变化 → 22 caption dual_24bit 必须重算 + B3 sequential chain 必须重走

**diff 摘要**：新增 §3.4 N4 章节（共 35 行，最长章节）+ §2.2 表格加注 "semantic_hash = LSH_12bit(svd2[caption_id])"。

##### V0.3-N5（中）— 完整性/序列化口径文档化

**V0.2 状态**：spec + KIMI 报告均未文档化 JSON 序列化口径。

**V0.3 增量**（4 项口径）：
- 缩进：`json.dumps(..., indent=1)`（换行 + 1 空格缩进）
- 中文编码：`json.dumps(..., ensure_ascii=False)`（caption_id 字符串不转义为 `\uXXXX`）
- 末尾换行：文件末追加单换行 `\n`（POSIX 标准；不写 `\r\n`）
- BOM：UTF-8 无 BOM（不写 `\ufeff` 头标）

**diff 摘要**：新增 §3.5 N5 章节（共 12 行）+ §2.1 / §2.2 / §2.3 表格加注 "序列化口径见 §3.5"。

##### V0.3-N6（低）— 判定线 α×β=30 + δ×γ×ρ=216 档文档化

**V0.2 状态**：仓内无展开定义；KIMI 报告 §7 采用 `decision_lines_36` (9 model × 4 bins = 36 档) 作为 P-D V0.2 评级落地版。

**V0.3 增量**：
- 理论档文档化：α×β=30 档（α=3 维度 × β=10 等级）+ δ×γ×ρ=216 档（δ=3 等级 × γ=6 区间段 × ρ=12 model 评估组）
- 落地档文档化：`decision_lines_36` (9 model × 4 T_frac bins = 36 档，9 in_bin + 27 out_of_bin)
- 阈值文档化：P_C_cosine ≥ 0.85 PASS / [0.70, 0.85) GRAY / < 0.70 FAIL；P_E_eps < 0.30 PASS / [0.30, 0.50) GRAY / ≥ 0.50 FAIL；P_D 类内 Hamming < 6 bits/12 强聚集

**diff 摘要**：新增 §3.6 N6 章节（共 18 行）+ §2.2 表格 P_D 列加注阈值。

### 2.3 V0.3 触动清单

**新增文件**（2 个）：
- `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md`（V0.3 主 spec）
- `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md`（本副文档）

**未触动文件**（声明 0 触动）：
- `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md`（V0 主体冻结，9,192 B / 3b67461b05fe）
- `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`（V0.2 主体冻结，4,587 B / c165cd33a362）
- `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md`（KIMI 报告冻结，10,979 B / 7f1492fbe657）
- `docs/V3X/KT_D0_SPEC_V0.1.md`（KT_D0 冻结，20,927 B / cce8e9a1b00e）
- `corpus/v20/` 32 个 JSON（已建 SHA-12 baseline，0 触动）
- `deposon_team/plugins/` 2 个 runner（0 触动）
- `verifier/runs/2026-09-04_pd_v0.jsonl`（0 触动）
- `results/deposon_volcengine_22caption_embedding_2026_09_10.json` + F4 / v3phys / 60cells 数据源（0 触动）
- 18 frozen anchors + 5 制品 JSON + schema v1 + 4 plugin spec + verifier/mavis/.builtin/scripts/（全部 0 触动）

### 2.4 V0.2 主体保持冻结

- §0 动机
- §2 双指纹设计（byte_hash + dual_24bit 命名引入）
- §3 LSH 算法（12-bit hyperplane sign）
- §4 22 caption 实测表（22 行）
- §5 类内 Hamming 距离（4 档家族聚集）
- §6 V0.1 → V0.2 升级点
- §7 后续工作（V0.3 候选）
- §9 输出文件

### 2.5 V0.2 → V0.3 严守 8 铁律

- ✅ no_llm：V0.3 spec 起草 0 LLM 调用
- ✅ no_proxy：V0.3 spec 起草 0 网络代理调用
- ✅ no_gateway：V0.3 spec 起草 0 网关调用
- ✅ no_key：V0.3 spec 起草 0 API key 调用
- ✅ no_18_frozen_touch：V0.3 spec 起草 0 触动 18 frozen anchors
- ✅ no_p_g_v0_v01_touch：V0.3 spec 起草 0 触动 V0 spec + V0.2 spec + V0/V0.1 frozen JSON
- ✅ no_plugin_spec_touch：V0.3 spec 起草 0 触动 4 plugin spec
- ✅ no_verifier_mavis_builtin_scripts_touch：V0.3 spec 起草 0 触动 verifier/mavis/.builtin/scripts/

---

## 3. V0 → V0.2 → V0.3 演进总览表

| 维度 | V0 (2026-09-01) | V0.2 (2026-09-11) | V0.3 (2026-09-17) |
|---|---|---|---|
| **字节指纹（R1-R5）** | ✅ 5 锚 manifest + 攻击 3/3 | ✅ 沿用 V0 | ✅ 沿用 V0 + §2.1 整合 |
| **语义指纹（dual_24bit）** | ❌ 无 | ✅ 22 caption dual_24bit + LSH-12bit + 类内 Hamming | ✅ 沿用 V0.2 + §2.2 整合 + N1/N2/N4 文档化 |
| **链式核验（B3 sequential chain）** | ❌ 无 | ✅ 22 caption B3 链式核验 (KIMI 报告 §5) | ✅ 沿用 KIMI 报告 + §2.3 整合 + N3 文档化 |
| **判定线档位** | ❌ 无 | ⚠️ α×β=30 + δ×γ×ρ=216 仓内无展开 | ✅ §3.6 N6 文档化（理论档 + 落地档 + 阈值） |
| **序列化口径** | ⚠️ V0 R2 只提 `separators=(",",":")` + `ensure_ascii=False` | ⚠️ V0.2 未文档化 | ✅ §3.5 N5 文档化（indent=1 / ensure_ascii=False / 尾换行 / UTF-8 无 BOM） |
| **SVD 上游推导** | ❌ 无 | ⚠️ V0.2 §3 只说 "22 caption SVD-2 坐标" | ✅ §3.4 N4 文档化（5 步推导 + 库依赖 + 重推须重调） |
| **3 处文档化风险点** | — | — | ✅ N1 + N4 + N5 全部消除 |
| **2 处历史命名加注** | — | — | ✅ N2 dual_24bit 名 24 实 36 + N3 B3 Merkle 非 RFC6962 |
| **1 处判定线档位** | — | — | ✅ N6 α×β=30 + δ×γ×ρ=216 档 |
| **0 重算 / 0 数据触动** | ✅ | ✅ | ✅ |
| **7 铁律遵守** | ✅ | ✅ | ✅ + 升级为 8 铁律逐条展开 |

---

## 4. V0 → V0.2 → V0.3 关键数字不变性

| 数字 | 出处 | V0 → V0.2 → V0.3 不变性 |
|---|---|---|
| 5 锚 SHA-256[0:12] | V0 spec §1 | ✅ 全程不变（V0/V0.2/V0.3 均沿用 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0 / aeefb8ef6972） |
| 5 锚 manifest 根指纹 | V0 spec §1 + KT_D0 V0.1 §3.1 | ✅ 全程不变（`7d6d3d39fad8`） |
| PD2 根指纹 | KT_D0 V0.1 §3.2 | ✅ 全程不变（`f88d855aaf83`） |
| EIS 根指纹 | KT_D0 V0.1 §3.3 | ✅ 全程不变（`e66e44e63f5a`） |
| 22 caption byte_hash 22 个 | V0.2 §4 + KIMI 报告 §4 | ✅ 全程不变（22 行表，沿用 KIMI 报告 2026-09-16 实测值） |
| 22 caption semantic_hash 22 个 | V0.2 §4 + KIMI 报告 §4 | ✅ 全程不变（22 行表） |
| 22 caption dual_24bit 22 个 | V0.2 §4 + KIMI 报告 §4 | ✅ 全程不变（22 行表） |
| 22 caption node_state 22 个 | KIMI 报告 §5 | ✅ 全程不变（22 个 12 hex 字符串） |
| ext_1 锚延伸 | KIMI 报告 §5 | ✅ 全程不变（`f6a1e495e9dc`） |
| **merkle_root B3 sequential chain** | KIMI 报告 §5 | ✅ 全程不变（`75596bbabdb8`） |
| **锚链 canonical** | KIMI 报告 §5 独立交叉确认 | ✅ 全程不变（`c4cae1ed9ee5`） |
| 4 档家族类内 Hamming | V0.2 §5 | ✅ 全程不变（L 2.47 / S1 2.67 / S2 2.80 / S3-S6 0.57 bits/12） |
| 36 档落地判定线 | KIMI 报告 §7 | ✅ 全程不变（`decision_lines_36`） |

---

## 5. V0.3 spec 字节数 + SHA-12 自验证

> **自验证步骤**（V0.3 spec 起草后）：
> 1. 算 `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` 字节数 + SHA-12
> 2. 算 `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` 字节数 + SHA-12
> 3. 算 4 个引用素材 SHA-12（沿用 §1.3 表，确保环境一致）
> 4. 算 `corpus/v20/` 32 JSON SHA-12 baseline（确保 0 触动）

**自验证结果**（V0.3 spec 起草后填入）：
- V0.3 主 spec: (待算)
- V0.3 CHANGELOG: (待算)
- V0 spec: 9,192 B / `3b67461b05fe` ✅ 已验证
- V0.2 spec: 4,587 B / `c165cd33a362` ✅ 已验证
- KIMI 报告: 10,979 B / `7f1492fbe657` ✅ 已验证
- KT_D0 V0.1 spec: 20,927 B / `cce8e9a1b00e` ✅ 已验证
- corpus/v20/ 32 JSON: 全部 SHA-12 baseline 已建 ✅ 已验证

---

## 6. 演进链总结

**V0**（2026-09-01）= 5 锚 manifest 字节指纹层（主体协议冻结）
↓
**V0.2**（2026-09-11）= + 22 caption dual_24bit 语义指纹层（语义层主体冻结）
↓
**V0.3**（2026-09-17）= + 6 改进文档化升级（N1 hash 口径 / N2 dual_36bit 命名 / N3 B3 sequential chain / N4 SVD 上游 / N5 序列化口径 / N6 判定线档位）

**3 版本共存**，互不覆盖；任何 P-D 范围内协议引用可根据需要选择 V0 (字节层) / V0.2 (语义层) / V0.3 (统一文档化升级版)；**P-D V1 启动时** U-V03-01/02/05 决定是否重命名 / 重新起草 / 升级实测表。

---

**P-D V0 → V0.2 → V0.3 演进链 CHANGELOG 结束。3 版本共存，6 改进 (N1-N6) 已文档化，0 重算 0 数据触动，22 caption dual_24bit + B3 sequential chain 22/22 PASS 不变。**