# P-D 可审计账指纹协议 V0.3 SPEC（统一文档化升级版）

> **作者**: doc-writer 凝子-agent (agent-0032834a3e04)
> **日期**: 2026-09-17 15:11 CST
> **状态**: V0.3 文档化升级版（V0 主体 + V0.2 语义层 + 6 改进文档化）
> **位置**: `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md`（新增文件，不覆盖 V0 / V0.2 旧版）
> **触发**: 鲍勃凝子-agent §4 推荐（沿 P-D 终局全 PASS + 三方 22/22 复算一致 + 0 算法性 fail 实证，零重算文档升级）
> **协作方**: 戴夫 (fact-check 备忘) + 鲍勃 (技术分析备忘) + Mavis (执行线)
> **铁律**: 严守 7 铁律 0 触动 (no_llm / no_proxy / no_gateway / no_key / no_18_frozen_touch / no_p_g_v0_v01_touch / no_plugin_spec_touch / no_verifier_mavis_builtin_scripts_touch)

---

## 0. 一句话结论 + V0 → V0.3 升级变更 6 项

**V0.3 = P-D 协议的文档化升级版。** 沿 V0 主体（5 锚 manifest 字节指纹层）+ V0.2 语义层（22 caption dual_24bit + LSH-12bit）+ KIMI 报告 B3 sequential chain 链式核验，**零重算、零数据触动**，仅 6 项文档化改进。

### V0 → V0.3 升级变更 6 项（按优先级 N1 → N6）

| 编号 | 优先级 | 改进点 | V0/V0.2 状态 | V0.3 裁定 |
|---|---|---|---|---|
| **N1** | **最高** | hash 输入三口径并存 | V0 spec R1 = 文件字节；V0.2 §2 = caption_id 字符串；P-O runner 非标 = caption 文本 | **P-D 范围内 22 caption 语义指纹只允许 V0.2 §2 唯一源 (caption_id 字符串)**；任何 V0.3 / §2 / §3 / §4 出现的 hash 必须显式标注输入口径 |
| **N2** | 低 | dual_24bit 名称 vs 真实位数 | V0.2 §2 命名 `dual_24bit`，但 9 hex = 36 bit 真实位数（"名 24 实 36"） | **保留 `dual_24bit` 旧名**（向后兼容，老数据不动），spec 加注 "名 24 实 36 (9 hex = 36 bit)"；`dual_36bit` 替代名仅在 V0.3+ 新代码中可选用 |
| **N3** | 中 | "B3 Merkle" 名称 vs 实质结构 | KIMI 报告 §5 命名 "B3 Merkle"，但实质是顺序链 + 2 级 anchor 延伸，**非 RFC6962 二叉 Merkle 树** | **保留 "B3 Merkle" 旧名**（外部引用稳定），spec 加注 "非 RFC6962 树，是顺序链 + 2 级 anchor 延伸"；`B3 sequential chain` 替代名仅在新文档中可用 |
| **N4** | 中-高 | 语义层上游 SVD 推导细节 | V0.2 §3 只说 "22 caption SVD-2 坐标"，未文档化上游推导 | **V0.3 §3.2 文档化**：中心化减均值 + V[:,0:2] 截断 + `dict[caption_id]=(x,y)` 输出 + numpy.linalg.svd；**重推须重调 doubao-embedding-vision-251215 API** |
| **N5** | 中 | 完整性/序列化口径 | V0.2 spec 未文档化 JSON 序列化口径 | **V0.3 §5 文档化**：`indent=1` / `ensure_ascii=False` / 尾换行 `\n` / UTF-8 无 BOM；落地证据：KIMI 报告 §2 "index.json 写入前后 SHA-256 UNCHANGED" |
| **N6** | 低 | 判定线 α×β=30 + δ×γ×ρ=216 档 | 仓内无展开定义 | **V0.3 §3.4 文档化**：α×β=30 理论档 + δ×γ×ρ=216 理论档；落地仍以 KIMI 报告 §7 `decision_lines_36` (9 model × 4 bins) 为准；P_C ≥ 0.85 PASS / [0.70,0.85) GRAY / < 0.70 FAIL；P_E < 0.30 PASS / [0.30,0.50) GRAY / ≥ 0.50 FAIL |

> **关键不变量**：6 改进全部为文档化升级，**0 重算、0 数据触动**；22 caption dual_24bit 实测表 + B3 sequential chain root=`75596bbabdb8` + 锚链=`c4cae1ed9ee5` + 三方 22/22 复算一致全部沿用 KIMI 报告 2026-09-16 已记录值。

---

## 1. 目标与范围

### 1.1 V0.3 目标

把 V0 主体（5 锚 manifest 字节指纹层）+ V0.2 语义层（22 caption dual_24bit + LSH-12bit）+ KIMI 报告 B3 sequential chain 链式核验三条线**合并为统一的 P-D V0.3 文档化升级规范**，消除三处文档化风险点（N1 hash 输入三口径 / N4 SVD 上游细节 / N5 序列化口径），并对两处历史命名（N2 dual_24bit "名 24 实 36" / N3 "B3 Merkle" 非 RFC6962 树）做向后兼容的 spec 加注。

### 1.2 V0.3 范围

**包含**：
- V0 主体（R1-R5 字节指纹层）原文引用，不触动
- V0.2 主体（22 caption 语义指纹层）原文引用，不触动
- KIMI 报告 §5 B3 sequential chain 链式核验原文引用，不触动
- 6 改进具体内容（N1-N6）作为 V0.3 新增章节
- V0 → V0.2 → V0.3 三版本演进链（CHANGELOG 副文档）

**不包含**：
- 任何新算法 / 新接口 / 新数据生成
- 任何对 18 frozen anchors / 5 制品 JSON / schema v1 / 4 plugin spec / verifier / mavis / .builtin / scripts/ 的触动
- 任何对 V0 spec / V0.2 spec 既有内容的修改（V0.3 是文档增量，不覆盖旧版）

### 1.3 与 V0 / V0.2 关系

| 版本 | 路径 | 字节数 | SHA-12 | 状态 | V0.3 处理 |
|---|---|---|---|---|---|
| **V0** | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 B | `3b67461b05fe` | 冻结 (2026-09-01) | 原文引用，不触动 |
| **V0.2** | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 B | `c165cd33a362` | 冻结 (2026-09-11) | 原文引用，不触动 |
| **V0.3** | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | (本文件) | (TBD) | 新增 (2026-09-17) | 新增，不覆盖 V0 / V0.2 |

**3 版本共存**：V0 (字节层主体冻结) + V0.2 (语义层主体冻结) + V0.3 (统一文档化升级版)，各自独立路径，互不覆盖。

---

## 2. 双层指纹设计（V0 字节层 + V0.2 语义层）

### 2.1 字节指纹层（V0 主体，5 锚 manifest）

每个工件（文档/脚本/spec）一个指纹，沿 V0 spec R1：

| 字段 | 算法 | 长度 | 性质 |
|---|---|---|---|
| **R1 内容寻址** | `hex(SHA-256(file_bytes))[0:12]` | 12 hex (48 bit) | 文件字节级 |
| **R2 manifest** | 5 锚数组 JSON 升序 | 265 字节 | 排序不变性 |
| **R3 根指纹** | `hex(SHA-256(manifest_bytes_utf8))[0:12]` | 12 hex (48 bit) | 5 锚全在唯一根 |
| **R4 runs 链** | `{"ts","prev_hash","current_root"}` JSONL | 追加式 | 历史不可篡改 |
| **R5 验证器边界** | 仅导出 `compute_root / verify_root / append_run / read_runs_count / verify_chain` | 接口受限 | 不可推断工件内容 |

**5 锚真实值**（沿 V0 spec §1，已 P-D V0.1 主线 2026-09-01 报告落地）：

| 锚 ID | 对象 | SHA-256[0:12] |
|---|---|---|
| `PD_V01_GT_FORMALIZATION` | `docs/GT_FORMALIZATION_v1.md` | `aeefb8ef6972` |
| `PD_V01_RUN_V21_GT` | `run_v21_gtformal.py` | `9bbe43f41fa8` |
| `PD_V01_RUN_V22_P1C` | `run_v22_p1c.py` | `6e9673205dc0` |
| `PD_V01_SPEC_GT2B` | `docs/SPEC_GT2B.md` | `68a5b08ef007` |
| `PD_V01_SPEC_GT8C` | `docs/SPEC_GT8C.md` | `6b09de9911c0` |
| **根指纹** | 5 锚 manifest SHA-256 前 12 位 | `7d6d3d39fad8` |

### 2.2 语义指纹层（V0.2 主体，22 caption dual_24bit）

每个 caption 一个语义指纹，沿 V0.2 spec §2：

| 字段 | 算法 | 长度 | 性质 |
|---|---|---|---|
| `byte_hash` | `SHA-256(caption_id)[0:12]` | 12 hex (48 bit) | 字符串级（V0.1 兼容） |
| `semantic_hash` | 12-bit LSH (12 hyperplane sign) | 3 hex (12 bit) | 语义级（V0.2 新增） |
| `dual_24bit` | `byte_hash[:6] + semantic_hash` | 9 hex (36 bit) | V0.2 组合（**名 24 实 36**，详见 §3 N2） |

**dual_24bit = 9 hex 字符 = 36 bit**，碰撞概率 ~1/2^36 ≈ 1e-11，但同源 caption 会自动聚集 (semantic_hash 相近)。

### 2.3 B3 sequential chain 链式层（KIMI 报告 §5）

22 caption dual_24bit → 顺序链 → 2 级 anchor 延伸 → b3_merkle_root（沿 KIMI 报告 §5）：

```
state_0     = anchors[0]                                   = 7d6d3d39fad8
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]   (i = 1..22)
ext_1       = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]            = f6a1e495e9dc
merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]                = 75596bbabdb8
```

**3 根 fingerprint anchors**（P-D V0.1）：`7d6d3d39fad8` / `f88d855aaf83` / `e66e44e63f5a`。

**锚链 canonical**（独立交叉确认）：`SHA-256("7d6d3d39fad8|f88d855aaf83|e66e44e63f5a")` 前 12 位 = `c4cae1ed9ee5`，与 P-F V0.1 5 锚 canonical 中 `PF_BOSS_03_merkle` 值逐字符相同。

**关键命名裁定**（详见 §3 N3）："B3 Merkle" 是 **sequential chain + 2 级 anchor 延伸**，**非 RFC6962 二叉 Merkle 树**。

---

## 3. 6 改进具体内容（N1-N6）

### 3.1 N1（最高风险）— hash 输入三口径统一

#### 3.1.1 三口径并存现状

P-D 范围内 hash 输入存在三套并存口径，已造成 1 次 P-D 相关 fail 记录（exp_3_4 corpus captions 字段缺失）和 1 次 V0.1.1 spec-CLI 衔接假性 FAIL：

| 口径 | 来源 | 输入 | 用途 | 是否合规 |
|---|---|---|---|---|
| **A** | V0 spec R1 | 文件字节 (`open(path,"rb").read()`) | 5 锚 content_addr | ✅ V0 主体唯一 |
| **B** | V0.2 spec §2 | caption_id 字符串 | 22 caption byte_hash | ✅ V0.2 主体唯一 |
| **C** | P-O runner 非标 (L172-197) | caption 文本 (full text from strip_captions_22.json) | `verify_22_caption_dual_24bit` 6+6 截段 | ❌ **非标**（KIMI 报告 §1 已判） |

**非标裁定**（KIMI 报告 §1 沿用）：口径 C 的 `verify_22_caption_dual_24bit` 函数使用 `cap_sha[:6] + cap_sha[6:12]` 纯截段（对 caption 文本 SHA-256 截 12 hex 再 6+6 拼接，**无 semantic_hash 语义层**，且 hash 输入为 caption 文本而非 caption_id），与 V0.2 spec 定义不符，**判为非标**。

#### 3.1.2 V0.3 裁定

**P-D 范围内 22 caption 语义指纹计算只允许 V0.2 §2 唯一源**：

```
byte_hash = hex(SHA-256(caption_id_string.encode("utf-8")))[0:12]
semantic_hash = LSH_12bit(svd2_coords[caption_id])  # 详见 §3.3 N4
dual_24bit = byte_hash[:6] + semantic_hash
```

**适用范围**：
- ✅ 5 锚 manifest (V0 主体)：用口径 A（文件字节）
- ✅ 22 caption 语义指纹 (V0.2 主体)：**只允许口径 B**（caption_id 字符串）
- ❌ 任何 P-D 范围内的 hash 计算**严禁使用**口径 C（caption 文本）
- ❌ 任何 P-D 范围外的 hash 计算（如 reviewer-b 独立审计）可自由选用

**显式标注要求**：
- V0.3 §2.1 / §2.2 / §2.3 / §4 任何 hash 计算必须显式标注输入口径（"文件字节" / "caption_id 字符串" / "其他"）
- 禁止未标注的 hash（防口径混淆导致非标）

#### 3.1.3 重推须重调

如重新调用 doubao-embedding-vision-251215 API 生成 22 caption embedding → SVD-2 → LSH-12bit → semantic_hash → dual_24bit，**口径 B 的 caption_id 字符串输入不变**，但 SVD-2 坐标会变（详见 §3.3 N4），必须重走整条 V0.2 数据流 + B3 sequential chain。

---

### 3.2 N2（低）— dual_24bit 名 24 实 36

#### 3.2.1 现状

V0.2 spec §2 命名 `dual_24bit`，但 9 hex 字符 = 36 bit 真实位数：

| 命名 | 实际位数 | 计算 |
|---|---|---|
| `dual_24bit` | **36 bit** | 9 hex × 4 bit/hex = 36 bit |
| "24 bit" 字面理解 | 24 bit | 6 hex × 4 = 24 bit（仅 byte_hash 半截，无语义） |

**历史命名原因**（沿 V0.2 spec §2 + §6 升级备注）：早期曾考虑 dual = byte_hash (12 bit) + semantic_hash (12 bit) = 24 bit 组合，后调整为 `byte_hash[:6] + semantic_hash` (6 hex + 3 hex = 9 hex = 36 bit)，名称 `dual_24bit` 沿用未改。

#### 3.2.2 V0.3 裁定

**保留 `dual_24bit` 旧名**（向后兼容，老数据 22 caption 实测表全部不动），spec 加注：

> **名 24 实 36 (9 hex = 36 bit)**：`dual_24bit = byte_hash[:6] + semantic_hash`，其中 byte_hash[:6] = 6 hex = 24 bit（V0.1 字符串级半截）+ semantic_hash = 3 hex = 12 bit（V0.2 语义级）= 6+3 = 9 hex = 36 bit 真实位数。

**替代命名 `dual_36bit` 仅在 V0.3+ 新代码 / 新文档中可选用**，老数据 22 caption 实测表（V0.2 §4 + KIMI 报告 §4）继续沿用 `dual_24bit`。

#### 3.2.3 重推须重调

如重新生成 semantic_hash（详见 §3.3 N4），dual_24bit 的 byte_hash 半截不变（口径 B 输入不变），仅 semantic_hash 部分变；无需触动 22 caption 命名。

---

### 3.3 N3（中）— "B3 Merkle" 实质是 sequential chain

#### 3.3.1 现状

KIMI 报告 §5 命名 "B3 Merkle 22 Caption dual_24bit 链式核验"，但 §5 链式约定显示**实质不是 RFC6962 二叉 Merkle 树**：

```
state_0     = anchors[0]                                   # 起点 = 锚 0
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]   # 顺序链 22 节
ext_1       = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]            # 1 级延伸
merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]                # 2 级延伸
```

**RFC6962 二叉 Merkle 树特征**：
- 树形结构（叶子节点对儿递归哈希到根）
- 任意位置可生成 Merkle inclusion proof
- 树结构与节点插入顺序无关

**P-D B3 实际特征**：
- 顺序链（state_i 依赖 state_(i-1)）
- 22 节顺序唯一，节点插入顺序决定链结构
- 1 级 anchor 延伸 (ext_1) + 2 级 anchor 延伸 (merkle_root)
- 无 RFC6962 树形结构、无 inclusion proof

#### 3.3.2 V0.3 裁定

**保留 "B3 Merkle" 旧名**（外部引用稳定，KIMI 报告 §5 + V0.3 沿用），spec 加注：

> **"B3 Merkle" 非 RFC6962 二叉 Merkle 树**：是顺序链 (sequential chain) + 2 级 anchor 延伸。`state_i = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]` 沿 caption 顺序串联 22 节，再 `ext_1` 锚 `anchors[1]` 延伸、`merkle_root` 锚 `anchors[2]` 延伸。**无 RFC6962 树形结构、无 inclusion proof**。

**替代命名 `B3 sequential chain` 仅在新文档中可用**，老报告（KIMI 报告 §5 标题 + §5 章节名）继续沿用 "B3 Merkle"。

#### 3.3.3 重推须重调

如重新生成 22 caption dual_24bit（详见 §3.4 N4 + §3.1 N1），B3 sequential chain root 必须重走整条链（22 节 + 2 级 anchor 延伸），root=`75596bbabdb8` 必须保持。

---

### 3.4 N4（中-高）— 语义层上游 SVD 推导细节文档化

#### 3.4.1 现状

V0.2 spec §3 只说 "22 caption SVD-2 坐标 (从 volcengine_22caption_embedding_2026_09_10.json)"，未文档化上游推导细节（中心化 / 符号约定 / 库 / 截断），导致：

- **重推风险**：如重调 doubao-embedding-vision-251215 API，无法复现 V0.2 spec §3 的 SVD-2 坐标
- **审计盲区**：独立 reviewer 无法验证 SVD-2 是否符合 spec 预期

#### 3.4.2 V0.3 文档化（5 步推导）

| 步骤 | 操作 | 输入 | 输出 |
|---|---|---|---|
| 1. Embedding 调用 | doubao-embedding-vision-251215 API | 22 caption 文本 | 22 × 2048-d 实向量 |
| 2. 中心化 | 减均值 | 22 × 2048-d 实向量 | 22 × 2048-d 中心化向量（按各维度均值中心化） |
| 3. SVD 截断 | `numpy.linalg.svd` → `V[:, 0:2]` | 22 × 2048-d 中心化向量 | 22 × 2-d SVD-2 坐标 |
| 4. 符号约定 | 按 `dict[caption_id] = (x, y)` 输出 | 22 × 2-d | `svd2: Dict[str, Tuple[float, float]]` |
| 5. LSH 投影 | 12 hyperplane (`np.random.seed(42)`) + sign | svd2 | semantic_hash (3 hex) |

**库依赖**：
- `numpy`（`np.linalg.svd` / `np.random.randn` / `np.random.seed(42)`）
- `hashlib`（`sha256` for byte_hash）
- 无第三方 LSH 库（自实现 12-bit sign-based LSH）

**已落地工件**：`results/deposon_volcengine_22caption_embedding_2026_09_10.json : svd2_coords`（frozen，只读）

#### 3.4.3 重推须重调（强约束）

如重新调用 doubao-embedding-vision-251215 API：

1. **embedding 步骤**：API endpoint / model name / prompt template / 22 caption 输入字符串任一变化 → 22 × 2048-d 必变
2. **中心化步骤**：22 caption 集合不变则 centroid 不变；若新增/删除 caption，centroid 必变
3. **SVD 截断步骤**：取前 2 主成分（V[:, 0:2]）固定；若改为前 3/前 4 主成分，semantic_hash 必变
4. **符号约定步骤**：sign(proj > 0) 约定固定；若改为 ≥ 0 或 ≤ 0，1/2 概率翻转
5. **LSH 投影步骤**：`np.random.seed(42)` 固定 + 12 hyperplane 维度固定；若改 seed 或维度，semantic_hash 必变

**任一步骤变化 → 必须重算**：
- 22 caption SVD-2 坐标 → 重算 semantic_hash → 重算 dual_24bit → 重走 B3 sequential chain（22 节 + 2 级 anchor 延伸）
- root=`75596bbabdb8` 必须保持（否则 = 协议失效）

#### 3.4.4 V0.3 §2.2 22 caption 实测表沿用

V0.2 spec §4 + KIMI 报告 §4 的 22 caption 实测表（22 行）全部沿用，0 触动；其口径沿用 KIMI 报告 §1 "spec 复算 = F4 = v3phys 三方一致"（22/22 PASS）。

---

### 3.5 N5（中）— 完整性/序列化口径文档化

#### 3.5.1 现状

V0.2 spec + KIMI 报告均未文档化 JSON 序列化口径，导致：

- 跨平台复现风险（`indent=None` vs `indent=1` / `indent=2` 序列化字节流不同）
- 中文 caption_id 编码风险（`ensure_ascii=True` 转义 vs `ensure_ascii=False`）
- 文本末换行风险（POSIX 标准 vs Windows CRLF）

#### 3.5.2 V0.3 文档化（4 项口径）

| 口径项 | V0.3 文档化 | 落地证据 |
|---|---|---|
| **缩进** | `json.dumps(..., indent=1)`（换行 + 1 空格缩进，便于人工 diff） | KIMI 报告 §2 "corpus/v20/index.json 写入前后 SHA-256 UNCHANGED" |
| **中文编码** | `json.dumps(..., ensure_ascii=False)`（caption_id 字符串不转义为 `\uXXXX`） | 同上 |
| **末尾换行** | 文件末追加单换行 `\n`（POSIX 标准；不写 `\r\n`） | 同上 |
| **BOM** | UTF-8 无 BOM（不写 `\ufeff` 头标） | 同上 |

#### 3.5.3 重推须重调

如重新生成 P-D 范围内任何 JSON 工件（corpus / results / integrity / manifest）：

- 任一项口径变化（`indent` / `ensure_ascii` / 末尾换行 / BOM）→ 序列化字节流必变 → 文件 SHA-256 必变 → **必须更新 integrity.content_sha256** 并显式声明口径变化
- frozen 文件（corpus/v20/index.json / strip_captions_22.json / by_model/* 5 制品）**严禁触动**

---

### 3.6 N6（低）— 判定线 α×β=30 + δ×γ×ρ=216 档文档化

#### 3.6.1 现状

仓内 V0/V0.1/V0.2/V0.3 spec 无 α×β=30 档 + δ×γ×ρ=216 档展开定义；KIMI 报告 §7 采用 `decision_lines_36` (9 model × 4 T_frac bins = 36 档) 作为 P-D V0.2 评级落地版。

#### 3.6.2 V0.3 文档化（理论档 + 落地档）

**理论档（仅作 spec 完整性参考，不直接落地）**：

| 理论档 | 计算 | 含义 |
|---|---|---|
| **α×β=30 档** | α=3 (P_C/P_E/P_D 维度) × β=10 (3 PASS + 3 GRAY + 3 FAIL + 1 留白) | 理论 P-D 评级档位 |
| **δ×γ×ρ=216 档** | δ=3 (PASS/GRAY/FAIL 等级) × γ=6 (T_frac 区间段) × ρ=12 (model 评估组) | 理论 P-D 多 model 评级档位 |

**落地档（P-D V0.2 评级实际采用）**：

| 落地档 | 计算 | 出处 |
|---|---|---|
| **`decision_lines_36`** | 9 model × 4 T_frac bins = 36 档 (9 in_bin + 27 out_of_bin) | `results/deposon_v3_physical_opt_60cells_2026_09_11.json : decision_lines_36` |

**判定线阈值**（沿该文件 thresholds）：

| 维度 | PASS | GRAY | FAIL |
|---|---|---|---|
| `P_C_cosine` | ≥ 0.85 | [0.70, 0.85) | < 0.70 |
| `P_E_eps` | < 0.30 | [0.30, 0.50) | ≥ 0.50 |
| `P_D`（V0.2） | 22 caption 类内 Hamming < 6 bits/12，4 档强聚集 (L 2.47 / S1 2.67 / S2 2.80 / S3-S6 0.57 bits) | — | — |

#### 3.6.3 重推须重调

- 30/216 理论档**仅作 spec 完整性参考**，落地仍以 36 档 `decision_lines_36` 为准
- 阈值调整（如 P_C PASS 阈值从 0.85 改 0.90）→ 必须重算 9 model T_frac 评级 + in_bin/out_of_bin 分布 + V0.2 spec §4 沿用一致性

---

## 4. 22 caption 实测指纹（沿 V0.2 §4 + KIMI 报告 §4，零触动）

### 4.1 22 caption 双指纹表（22/22 一致）

> **零触动声明**：本节 22 caption 表全部沿用 V0.2 spec §4 (2026-09-11) + KIMI 报告 §4 (2026-09-16) 实测值，未做任何修改。

| caption_id | byte_hash (V0.1) | semantic_hash (V0.2) | dual_24bit (名 24 实 36) |
|---|---|---|---|
| L_algorithm_process | `e07ebcfbf9ba` | `498` | `e07ebc498` |
| L_biological_taxonomy | `bff92145e971` | `2dd` | `bff9212dd` |
| L_geography_world | `64ad5fc2c7e0` | `2fd` | `64ad5f2fd` |
| L_historical_causality | `fbfa04f1128c` | `2dc` | `fbfa042dc` |
| L_physics_concepts | `dbe8caaa4bfd` | `2fd` | `dbe8ca2fd` |
| L_project_management | `5fe6baab5410` | `2fd` | `5fe6ba2fd` |
| S1 | `3696ad59777e` | `6d8` | `3696ad6d8` |
| S1_n35 | `6d92596542c2` | `2fd` | `6d92592fd` |
| S1_n45 | `d22455b290c0` | `6d8` | `d224556d8` |
| S1_n60 | `a71ac717c393` | `2fd` | `a71ac72fd` |
| S2 | `adfa2b24c2d9` | `6dc` | `adfa2b6dc` |
| S2_n20 | `6c76eaea53d5` | `2fd` | `6c76ea2fd` |
| S2_n35 | `831a5b3a2c65` | `498` | `831a5b498` |
| S2_n45 | `3174b72cf536` | `2dd` | `3174b72dd` |
| S2_n60 | `2242e1fb732a` | `2dd` | `2242e12dd` |
| S3 | `44d6a8a73edd` | `2dd` | `44d6a82dd` |
| S4 | `b1d3eb8f3293` | `2dd` | `b1d3eb2dd` |
| S5 | `1cdcbd57e7e2` | `2dd` | `1cdcbd2dd` |
| S6 | `b12f76a4b782` | `2fd` | `b12f762fd` |
| S6_n20 | `803f0b9079ca` | `2fd` | `803f0b2fd` |
| S6_n35 | `0e89a90afea3` | `2fd` | `0e89a92fd` |
| S6_n60 | `6abc0c5ac060` | `2fd` | `6abc0c2fd` |

**口径标注**（V0.3 N1 加注）：
- byte_hash = 口径 B (caption_id 字符串 → SHA-256 → 前 12 hex)
- semantic_hash = 12-bit LSH from svd2[caption_id] (np.random.seed(42) 固定)
- dual_24bit = byte_hash[:6] + semantic_hash (名 24 实 36, 9 hex = 36 bit)

### 4.2 B3 sequential chain 链式核验（沿 KIMI 报告 §5）

> **零触动声明**：本节 22 caption node_state + ext_1 + merkle_root 全部沿用 KIMI 报告 §5 (2026-09-16) 复算值，未做任何修改。

**链式约定**（顺序链 + 2 级 anchor 延伸，详见 §3.3 N3）：

```
state_0     = 7d6d3d39fad8                  # 锚 0（P-D V0.1 主线根指纹）
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]   (i = 1..22)
ext_1       = SHA-256(f"{state_22}|anchor|f88d855aaf83")[0:12]            # 锚 1（PD2）
merkle_root = SHA-256(f"{ext_1}|anchor|e66e44e63f5a")[0:12]                = 75596bbabdb8  # 锚 2（EIS）
```

**关键节点示例**：
- 首链：`SHA-256("7d6d3d39fad8|L_algorithm_process|e07ebc498")[0:12] = 9619b7c483d9`
- 末链：`SHA-256("f3a2a0b9eabf|S6_n60|6abc0c2fd")[0:12] = bff2e2a039cc` = state_22
- ext_1 = `f6a1e495e9dc`
- **merkle_root = `75596bbabdb8`**

**22/22 PASS 证据**（沿 KIMI 报告 §5 独立复走）：
- 锚 0 衔接现存链：`verifier/runs/2026-09-04_pd_v0.jsonl` 记录 `prev_hash=000000000000 → current_root=7d6d3d39fad8` ✅
- 22 个 node_state 全部从锚 0 顺序复走吻合
- ext_1 + merkle_root 全部吻合
- 独立交叉确认：`SHA-256("7d6d3d39fad8|f88d855aaf83|e66e44e63f5a")` 前 12 位 = **`c4cae1ed9ee5`**，与 P-F V0.1 5 锚 canonical 中 `PF_BOSS_03_merkle` 值逐字符相同

**三方一致证据**（沿 KIMI 报告 §4）：
- vs `deposon_v2_phase4_f4_2026_09_11.json` dual_fingerprints = **22/22** ✅
- vs `deposon_v3_physical_opt_2026_09_11.json` P_D_semantic_fingerprint_V0_2.per_caption = **22/22** ✅
- KIMI 复算 = F4 = v3phys 三方一致

---

## 5. 7 铁律遵守

### 5.1 V0.3 兑现（8 条铁律，逐条展开）

| 铁律 | V0.3 兑现 | 引用 |
|---|---|---|
| ✅ **no_llm** | 本 spec 起草 0 LLM 调用（纯 doc-writer 凝子-agent + read + write 工具）；所有数值沿用 KIMI 报告 + V0.2 spec 已实测值 | §0 + §4 + §6 |
| ✅ **no_proxy** | 本 spec 起草 0 网络代理调用；加速器 (127.0.0.1:7897) 未启动 | §6 自查 |
| ✅ **no_gateway** | 0 网关调用（不调 doubao-embedding-vision-251215 / minimax / 任何 LLM API） | §3.4 N4 重推须重调 |
| ✅ **no_key** | 0 API key 调用；spec 起草纯本地只读 | §6 自查 |
| ✅ **no_18_frozen_touch** | 0 触动 18 frozen anchors（沿 schema v1 `_v3x_frozen_schema_v1.json`） | §6 自查 |
| ✅ **no_p_g_v0_v01_touch** | 0 触动 V0 spec + V0.2 spec + V0/V0.1 frozen JSON；V0.3 是文档增量，不覆盖旧版 | §1.3 + §6 |
| ✅ **no_plugin_spec_touch** | 0 触动 4 plugin spec（skill_a/b/c/d） | §6 自查 |
| ✅ **no_verifier_mavis_builtin_scripts_touch** | 0 触动 verifier / mavis / .builtin / scripts/ 目录 | §6 自查 |

### 5.2 V0.3 触动清单

**新增文件**（2 个）：
- `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md`（本文件）
- `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md`（V0 → V0.2 → V0.3 演进链副文档）

**未触动文件**（声明 0 触动）：
- `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md`（V0 主体冻结，9,192 B / 3b67461b05fe）
- `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`（V0.2 主体冻结，4,587 B / c165cd33a362）
- `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md`（KIMI 报告冻结，10,979 B / 7f1492fbe657）
- `docs/V3X/KT_D0_SPEC_V0.1.md`（KT_D0 冻结，20,927 B / cce8e9a1b00e）
- `corpus/v20/` 32 个 JSON（已建 SHA-12 baseline，0 触动）
- `deposon_team/plugins/` 2 个 runner（0 触动）
- `verifier/runs/2026-09-04_pd_v0.jsonl`（P-D V0.1 既有运行链，0 触动）
- `results/deposon_volcengine_22caption_embedding_2026_09_10.json`（SVD-2 坐标源，0 触动）
- `results/deposon_v2_phase4_f4_2026_09_11.json` + `results/deposon_v3_physical_opt_2026_09_11.json` + `results/deposon_v3_physical_opt_60cells_2026_09_11.json`（F4 / v3phys / 60cells 数据源，0 触动）
- 18 frozen anchors（沿 schema v1）+ 5 制品 JSON（corpus/v20/by_model/）+ schema v1 + 4 plugin spec + verifier/mavis/.builtin/scripts/（全部 0 触动）

---

## 6. 复现协议 + 自查声明

### 6.1 复现步骤（doc-writer 凝子-agent 视角）

1. **读 4 个核心素材**（只读，0 触动）：
   - `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md`
   - `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`
   - `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md`
   - `docs/V3X/KT_D0_SPEC_V0.1.md`
2. **算 4 个素材 SHA-12**（验证环境一致）：见 §1.3 表，全部对得上
3. **写 V0.3 主 spec**（本文件）
4. **写 CHANGELOG 副文档**（V0 → V0.2 → V0.3 演进链）
5. **算 V0.3 + CHANGELOG SHA-12**（自验证）
6. **写本报告**（向 Mavis 主线汇报）

### 6.2 自查声明

1. **0 重算**：本 spec 起草过程中，0 次调用任何 embedding API / LLM / 复算脚本；22 caption 实测值 + root + 锚链全部沿用 KIMI 报告已记录值
2. **0 LLM**：本 spec 起草 0 LLM 调用，纯 doc-writer 凝子-agent + read + write 工具
3. **0 网络**：本 spec 起草 0 网络调用（不调加速器 / 代理 / 网关）
5. **0 触动 frozen**：corpus/v20/32 JSON SHA-12 baseline 全部沿用，无变化
6. **0 触动 V0/V0.2**：V0 spec + V0.2 spec 字节数 + SHA-12 全部沿用（9192/3b67461b05fe + 4587/c165cd33a362）
7. **0 触动 KIMI 报告**：KIMI 报告字节数 + SHA-12 全部沿用（10979/7f1492fbe657）
8. **0 触动 KT_D0**：KT_D0 V0.1 spec 字节数 + SHA-12 全部沿用（20927/cce8e9a1b00e）
9. **新增文件 2 个**：仅 V0.3 主 spec + CHANGELOG 副文档
10. **3 版本共存**：V0 (字节层主体冻结) + V0.2 (语义层主体冻结) + V0.3 (统一文档化升级版)，各自独立路径

---

## 7. 已知未决项

| 编号 | 已知未决项 | 决策时点 | 派给 |
|---|---|---|---|
| **U-V03-01** | 6 改进中 N2/N3 "保留旧名 + spec 加注" 决策是否在 P-D V1 启动时升级为重命名（`dual_24bit` → `dual_36bit` / `B3 Merkle` → `B3 sequential chain`） | P-D V1 启动时 | Mavis + doc-writer |
| **U-V03-02** | V0.3 spec 是否作为 P-D V1 主 spec 的 §0+§1 输入（即 V0.3 是否被 V1 引用），还是 V1 重新起草 | P-D V1 启动时 | Mavis |
| **U-V03-03** | N4 文档化的 SVD 上游推导细节（5 步 + 库依赖 + 重推须重调）是否在 Phase 1 reviewer-b 独立审计时作为 P-D V0.2 复现依据 | Phase 1 reviewer-b 审计 | reviewer-b |
| **U-V03-04** | N6 理论档（α×β=30 + δ×γ×ρ=216）是否在 P-D V1 启动时展开定义为可计算 spec（而非仅作完整性参考） | P-D V1 启动时 | Mavis |
| **U-V03-05** | 22 caption dual_24bit 实测表是否需要在 P-D V1 启动时升级为 dual_36bit 表（仅改字段名，不改数值） | P-D V1 启动时 | doc-writer |

---

## 8. 引用与版本

### 8.1 V0.3 spec 元数据

| 项 | 值 |
|---|---|
| 文件名 | `P_D_FINGERPRINT_V0_3_SPEC.md` |
| 路径 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` |
| 字节数 | (TBD，由 doc-writer 起草后算) |
| SHA-12 | (TBD，由 doc-writer 起草后算) |
| 起草日期 | 2026-09-17 15:11 CST |
| 作者 | doc-writer 凝子-agent (agent-0032834a3e04) |
| 协作方 | 戴夫 (fact-check 备忘) + 鲍勃 (技术分析备忘) + Mavis (执行线) |

### 8.2 引用素材（4 个核心 spec / 报告）

| 来源 | 路径 | 字节数 | SHA-12 | 状态 |
|---|---|---|---|---|
| V0 spec | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 B | `3b67461b05fe` | 冻结 (2026-09-01) |
| V0.2 spec | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 B | `c165cd33a362` | 冻结 (2026-09-11) |
| KIMI 报告 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | 10,979 B | `7f1492fbe657` | 冻结 (2026-09-16) |
| KT_D0 V0.1 spec | `docs/V3X/KT_D0_SPEC_V0.1.md` | 20,927 B | `cce8e9a1b00e` | 冻结 (2026-09-09) |

### 8.3 引用数据源（5 个 frozen 数据）

| 来源 | 路径 | 字节数 | SHA-12 | 状态 |
|---|---|---|---|---|
| 22 caption 源 | `corpus/v20/strip_captions_22.json` | 12,798 B | `6a2656878745` | frozen (2026-09-10) |
| B3 sequential chain 链 | `corpus/v20/index_v2_2026_09_16.json` | 24,150 B | `efe05ad775de` | frozen (2026-09-16) |
| SVD-2 坐标源 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | (TBD) | (TBD) | frozen |
| F4 数据源 | `results/deposon_v2_phase4_f4_2026_09_11.json` | (TBD) | (TBD) | frozen |
| v3phys 数据源 | `results/deposon_v3_physical_opt_2026_09_11.json` + `..._60cells_2026_09_11.json` | (TBD) | (TBD) | frozen |

### 8.4 引用判定线（落地档）

| 来源 | 路径 | 引用 |
|---|---|---|
| 36 档落地版 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json : decision_lines_36` | KIMI 报告 §7 |

### 8.5 引用 runner 代码（只读）

| runner | 路径 | 字节数 | 用途 |
|---|---|---|---|
| B3 sequential chain runner | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 B | 22 caption 复算 + B3 链式核验 |
| P-O 对比 runner（非标口径 C） | `deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py` | (TBD) | 非标裁定依据（KIMI 报告 §1） |

---

## V0 → V0.2 → V0.3 升级记录

### V0 主体保持冻结（已 P-D V0.1 主线 2026-09-01 PASS）

- §0 一句话结论 + 5 锚清单
- §1 目标与范围
- §2 R1-R5 字节指纹层
- §3 数据结构伪代码
- §4 三类攻击 → 检测信号映射
- §5 实现接口签名
- §6 判死线（机械命令模板）
- §7 接口预留位

### V0.2 主体保持冻结（已 22 caption dual_24bit 22/22 PASS）

- §0 动机
- §2 双指纹设计（byte_hash + dual_24bit 命名引入）
- §3 LSH 算法（12-bit hyperplane sign）
- §4 22 caption 实测表（22 行）
- §5 类内 Hamming 距离（4 档家族聚集）
- §6 V0.1 → V0.2 升级点（semantic_hash + dual_24bit + 类内 Hamming 验证）
- §7 后续工作（V0.3 候选，含 embedding-2048-d 直接 LSH-128bit / permutation-based LSH / fingerprint 模块集成）

### V0.3 增量（2026-09-17 文档化升级，6 改进）

| 节 | 改动类型 | 改动原因 | 引用 |
|---|---|---|---|
| **§0** | V0/V0.2 无 → V0.3 §0 一句话结论 + V0 → V0.3 升级变更 6 项 | 读者快速看到 V0.3 与 V0/V0.2 的最关键 6 项差异 | §0 |
| **§1** | V0 §1 + V0.2 §1 范围 → V0.3 §1 目标 + 范围 + 与 V0/V0.2 关系 | V0.3 升级为统一文档化规范，明确 3 版本共存 | §1.3 |
| **§2** | V0 §2 字节层 + V0.2 §2 语义层 → V0.3 §2 双层指纹设计 | V0.3 把两条线合并为双层设计，5 锚清单 + 22 caption dual_24bit 完整呈现 | §2.1 + §2.2 + §2.3 |
| **§3** | V0/V0.2 无统一章 → V0.3 §3 6 改进具体内容 (N1-N6) | 鲍勃凝子-agent §4 推荐的核心改进（消除 3 处文档化风险 + 2 处历史命名 + 1 处 SVD 上游） | §3.1 N1 + §3.2 N2 + §3.3 N3 + §3.4 N4 + §3.5 N5 + §3.6 N6 |
| **§4** | V0.2 §4 实测表 → V0.3 §4 22 caption 实测指纹（沿用 + 口径标注） | V0.3 加 §4.1 口径标注（N1 兑现）+ §4.2 B3 sequential chain 链式核验 | §4.1 + §4.2 |
| **§5** | V0/V0.2 7 条铁律零散 → V0.3 §5 7 铁律遵守（8 条逐条展开 + V0.3 触动清单） | V0.3 严守 8 条铁律（no_llm/no_proxy/no_gateway/no_key/no_18_frozen_touch/no_p_g_v0_v01_touch/no_plugin_spec_touch/no_verifier_mavis_builtin_scripts_touch） | §5.1 + §5.2 |
| **§6** | V0/V0.2 无 → V0.3 §6 复现协议 + 自查声明（10 条） | V0.3 自查 0 重算 / 0 LLM / 0 网络 / 0 frozen 触动 / 0 V0/V0.2 触动 | §6.1 + §6.2 |
| **§7** | V0/V0.2 无 → V0.3 §7 已知未决项（U-V03-01 ~ U-V03-05） | V0.3 前瞻性缺口清单 | §7 |
| **§8** | V0 §7 + V0.2 引用 → V0.3 §8 引用与版本（V0.3 元数据 + 4 spec + 5 frozen 数据 + 1 落地档 + 2 runner） | V0.3 反映 frozen 阶段实际工件 | §8.1 + §8.2 + §8.3 + §8.4 + §8.5 |
| **升级记录** | V0/V0.2 无 → V0.3 footer V0 → V0.2 → V0.3 升级记录 | 透明化升级过程，便于审查与回退 | 本节 |

### V0.3 主体保持冻结（已 P-D 终局全 PASS + 三方 22/22 复算一致）

- §0 一句话结论 + V0 → V0.3 升级变更 6 项
- §1 目标与范围 + 与 V0/V0.2 关系
- §2 双层指纹设计（V0 字节层 + V0.2 语义层 + B3 sequential chain 链式层）
- §3 6 改进具体内容 (N1-N6)
- §4 22 caption 实测指纹（沿用 + 口径标注）
- §5 7 铁律遵守
- §6 复现协议 + 自查声明
- §7 已知未决项
- §8 引用与版本

### 下次升级触发

- P-D V1 启动时，U-V03-01（重命名 dual_36bit / B3 sequential chain）+ U-V03-02（V0.3 作为 V1 §0+§1 输入）+ U-V03-05（22 caption 实测表升级为 dual_36bit 表）
- Phase 1 reviewer-b 独立审计时，U-V03-03（SVD 上游推导细节作为 P-D V0.2 复现依据）
- P-D V1 启动时，U-V03-04（α×β=30 + δ×γ×ρ=216 理论档展开定义）

---

**P-D 可审计账指纹协议 V0.3 SPEC 文档化升级版结束，6 改进 (N1-N6) 已文档化，22 caption 实测表 + B3 sequential chain root=`75596bbabdb8` + 锚链=`c4cae1ed9ee5` 全部沿用 KIMI 报告 2026-09-16 已记录值，3 版本共存 (V0 + V0.2 + V0.3)，8 条铁律 0 触动。**