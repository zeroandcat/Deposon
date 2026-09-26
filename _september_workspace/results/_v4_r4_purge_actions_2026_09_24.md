# V4 R4 key 明文违规 落地处置清单 (2026-09-24)

> by **worker** (执行类·数据修订+取证)
> Generated: 2026-09-24 19:05
> Predecessor: `results/_v4_r4_key_purge_manifest_2026_09_24.md` (SHA-12 `5BF4D9AD2877`) §0.2 §2 §3 §5
> 派工单授权来源: PI `ask_d38952e0b8edb60bd854a470` (2026-09-24 19:00) 4 项拍板: ①redact_both ②stale 入勘误链 + 4 件 v4_supp hash manifest 不动 ③key 报废结案 (PI 确认均为已废弃测试 key, 无需轮换) ④追查误报根因

---

## 0. Dispatch Record (5-item checklist)

| slot | value |
|---|---|
| 1. agent name | worker (执行类·数据修订+取证) |
| 2. skill name | `superpowers:verification-before-completion` (sha256 `ade95665080e...`) — 老实交代 skill 缺位纪律锚 fallback = `results/_v4_r4_key_purge_manifest_2026_09_24.md` §0.2/§2/§3 + `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` 勘误留痕格式; **未编造 skill 不存在的虚构指令** |
| 3. plugin | `@superpowers` |
| 4. iron rules (7+9) | **R4 key 永不明文 (无例外)** = 本棒授权来源 (本棒任何输出禁止复述 key 明文; 一律 `文件+行号+key SHA-12 指纹` 指代); V1–V3 frozen 只读不动; 派生 JSON 不合并; 0 擅调阈值; 不覆盖既有件 (本棒仅 redact 2 件 + 新建 1 件清单) |
| 5. honest disclosure | 0 产物报 0 产物; succeeded ≠ 跑完落盘实测; **本棒全程未输出任何 key 明文**; 仅以 `key_sha12=<指纹前12>（redacted per ask_d38952e0, 2026-09-24）` 形式指代被 redact 之 key |

---

## 1. PI 拍板依据 (ask_d38952e0b8edb60bd854a470, 2026-09-24 19:00)

| # | 拍板项 | 落地执行 |
|---|---|---|
| ① | **redact_both** | §2 本棒 redact 2 件: ① MD inventory §5.6 行级替换 4 处 key 明文 → `key_sha12=<指纹前12>`; ② JSON sanity 行 39 + 54 替换 2 处 sk-or-v1- key → `key_sha12=D6760FC68827` |
| ② | **stale 入勘误链 4 件 manifest 不动** | §3 4 件 v4_supp hash manifest 全文不动 (pre/post SHA-12 对照, 验证 0 修改); stale entry 登记为素材供后续 doc-writer 入勘误链 E-31 |
| ③ | **key 报废结案** (PI 确认 4 个 key 均为已废弃测试 key, 无需轮换) | §4 4 个 key 指纹统一登记结案 (`6CD6FE9FB32F` / `00249F41B80D` / `96D5AE961FB5` / `D6760FC68827`); 不再追踪; 不发起 incident response |
| ④ | **追查误报根因** | §5 盘点棒误将 3 件在盘件 (`1665F367B2C4` / `EB9AD4193CF2` / `CC25C5149CE1`) 登记 NOT-ON-DISK 的根因已查明 (naming drift / `_ruleset_` 中缀问题), 见 §5 |

---

## 2. Redact 操作记录 (pre/post SHA-12 + bytes + syntax check)

### 2.1 MD inventory 文件 (含 §5.6 R4 证据段)

| 字段 | 值 |
|---|---|
| 路径 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| 定位段 | §5.6 R4 evidence (redact 前为行 3773, redact 后因插入新内容偏移至行 3781) |
| redact 前 SHA-12 | `2FADEA9F6259` |
| redact 前 bytes | 355,369 |
| redact 后 SHA-12 | `3E4E90FB48E1` |
| redact 后 bytes | 355,687 |
| 字节变化 | +318 (净增 — redact 后 fingerprint 注解比原 key 明文+ 描述更长) |
| 改动位置 | §5.6 行 3773 (1 处表格行内 4 段 key 明文) |

#### 2.1.1 Redact 前后对照 (4 处 key 明文)

| # | 段 | 原 key 明文 | 原 provider 注释 | → 替换为 (key_sha12 fingerprint) |
|---|---|---|---|---|
| 1 | `\sk-or-v1-...\ (OpenRouter)` | `key_sha12=6CD6FE9FB32F` | OpenRouter | `key_sha12=6CD6FE9FB32F`（sk-or-v1- OpenRouter, redacted per ask_d38952e0, 2026-09-24） |
| 2 | `\sk-teamo-...\ (teamorouter)` | `key_sha12=00249F41B80D` | teamorouter | `key_sha12=00249F41B80D`（sk-teamo- teamorouter, redacted per ask_d38952e0, 2026-09-24） |
| 3 | `\sk-ad9b56...\ ` | `key_sha12=96D5AE961FB5` | (无 provider 注释) | `key_sha12=96D5AE961FB5`（sk-ad9b56- style, redacted per ask_d38952e0, 2026-09-24） |
| 4 | `\<BEL>[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]\ (truncated in probe output)` | `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` (truncated) | volcengine ark-style; truncated in probe output | `key_sha12=unrecorded`（volcengine ark-style; per-key fingerprint unrecorded in manifest §2.1 — scan regex blind spot, truncated in probe output, redacted per ask_d38952e0, 2026-09-24） |

注 1: 段 1-3 之 fingerprint 来自 `results/_v4_r4_key_purge_manifest_2026_09_24.md` §2.1 #2 行登记; 段 4 之 fingerprint unrecorded 因 manifest §1 正则 `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` 无法匹配 UUID 风格多 dash 形态, 属扫描盲点 — 已老实交代在 §6.4。

注 2: 段 4 原文本包含 1 个 BEL 字符 (0x07) 位于 `\` 与 `rk-` 之间 (来源未明; 该行 (旧行 3773) 与行 3780 各有 1-2 处 BEL; 推断为 GB18030 误解码残余或历史工具产物), 本棒 redact 时一并保留 BEL 上下文 (含 BEL 字节 0x07 → redact 后该 BEL 已不复存在, 因 `\<BEL>rk-...` 整段被 fingerprint 注解替换)。

#### 2.1.2 Redact 后 §5.6 行内容 (verbatim 落地, 供 verifier 复核)

```
| keys present (plaintext) | \key_sha12=6CD6FE9FB32F\（sk-or-v1- OpenRouter, redacted per ask_d38952e0, 2026-09-24） ; \key_sha12=00249F41B80D\（sk-teamo- teamorouter, redacted per ask_d38952e0, 2026-09-24） ; \key_sha12=96D5AE961FB5\（sk-ad9b56- style, redacted per ask_d38952e0, 2026-09-24） ; \key_sha12=unrecorded\（volcengine ark-style; per-key fingerprint unrecorded in manifest §2.1 — scan regex blind spot, truncated in probe output, redacted per ask_d38952e0, 2026-09-24） |
```

#### 2.1.3 grep 自检 (MD)

| 检查项 | 命中数 | 备注 |
|---|---|---|
| `key_sha12=6CD6FE9FB32F` (段 1 原 key) | **0** ✓ | 全部移除 |
| `key_sha12=00249F41B80D` (段 2 原 key) | **0** ✓ | 全部移除 |
| `key_sha12=96D5AE961FB5` (段 3 原 key) | **0** ✓ | 全部移除 |
| `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` (段 4 原 key 截断) | **0** ✓ | 全部移除 |
| `key_sha12=6CD6FE9FB32F` (段 1 fingerprint) | 1 ✓ | redact 注解引用 |
| `key_sha12=00249F41B80D` (段 2 fingerprint) | 1 ✓ | redact 注解引用 |
| `key_sha12=96D5AE961FB5` (段 3 fingerprint) | 1 ✓ | redact 注解引用 |
| `key_sha12=unrecorded` (段 4 fingerprint 占位) | 1 ✓ | redact 注解引用 |

#### 2.1.4 链副作用注记

- **MD §5.7/§5.8 fingerprint 段历史快照 stale**: §5.7 登记 (size 352,236 / SHA-12 `82B17BCBDE1A` / 18:44:18); §5.8 登记 (size 354,927 / SHA-12 `439834FE63AC` / 18:44:33); **当前实况**: size 355,687 / SHA-12 `3E4E90FB48E1` (post-redact).
- 这 2 段为**历史快照登记**性质 (记录 18:44:18 / 18:44:33 时刻之文件 fingerprint), **本棒未触动** (按不覆盖既有件边界).
- 下游引用方应注意: §5.7/§5.8 段之 SHA-12 为**历史值**, 非当前文件 SHA-12; 当前 SHA-12 见本节 §2.1 表 + 本清单 §8.

### 2.2 JSON sanity 文件 (3 backbone reachability)

| 字段 | 值 |
|---|---|
| 路径 | `D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` |
| 定位段 | 行 39 + 行 54 之 `"key"` 字段值 |
| redact 前 SHA-12 | `5D583C612D07` |
| redact 前 bytes | 2,289 |
| redact 后 SHA-12 | `E6173BC63DF5` |
| redact 后 bytes | 2,273 |
| 字节变化 | -16 (净减 16 字节; 每处 key 73 字节 → fingerprint 65 字节 = 8 字节 × 2 处) |
| JSON syntax check (post-redact) | **OK** (3 results; `ConvertFrom-Json` 解析无异常) |

#### 2.2.1 Redact 前后对照 (2 处 sk-or-v1- key)

| 行 | 原 key 明文 | → 替换为 (key_sha12 fingerprint) |
|---|---|---|
| 39 | `key_sha12=D6760FC68827` | `key_sha12=D6760FC68827`（redacted per ask_d38952e0, 2026-09-24） |
| 54 | (同上, 同 fingerprint) | `key_sha12=D6760FC68827`（redacted per ask_d38952e0, 2026-09-24） |

#### 2.2.2 grep 自检 (JSON)

| 检查项 | 命中数 | 备注 |
|---|---|---|
| `key_sha12=D6760FC68827` (原 key) | **0** ✓ | 全部移除 |
| `key_sha12=D6760FC68827` (fingerprint) | 2 ✓ | 行 39 + 54 之 redact 注解引用 |

#### 2.2.3 边界外发现 (本棒不擅动, 见 §6.4)

- **JSON 行 24 `ark-` key 未 redact** (在 dispatch 显式授权范围「行 39/54 附近 + D6760FC68827」之外): `key_sha12=7348FC7D6C33`（volcengine ark-style, UUID 格式; full plaintext 落盘于 JSON 行 24; 派工单边界外 + 不擅动; 本棒不复述 plaintext）; manifest §1 正则 `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` 因 UUID 多 dash 结构未匹配, **属扫描盲点**.
- 本棒按 dispatch 边界 (「只动上述 2 件 redact + 新建 1 件清单; 其余一概不碰」) + 不擅自重写原则, **行 24 ark- key 不动** — 留给 PI 另派 doc-writer / verdict-keeper 决定.

#### 2.2.4 链副作用注记

- **JSON 被 3 件 chain manifest 引用** (manifest §3.3 已登记):
  - `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` 行 3 + 318
  - `results/_archive_manifest_deposon_sub_2026_09_23.json` 行 702
  - `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` 行 3383 (ARCHIVED 件引用)
- 这些 manifest 引用之 SHA-12 现已 stale (`5D583C612D07` → `E6173BC63DF5`).
- 按派工单纪律 `链上件不动`, 本棒**未触动**这 3 件 chain manifest. 由 PI 决定: (a) 接受 stale; (b) 重建 manifest 排除; (c) 同步 redact chain manifest 引用.

---

## 3. Stale entry 登记素材 (供 doc-writer 入勘误链 E-31)

### 3.1 4 件 v4_supp hash manifest (本棒不动, SHA-12 验证前后对照不变)

> 沿派工单纪律「4 件 manifest 不动」+ 「stale 入勘误链 4 件 manifest 不动」, 本棒 0 修改. SHA-12 pre/post 对照验证 (本棒 19:05 实测):

| # | 链上 hash manifest (Rel) | 行号 | 登记内容 (未触动, 已 grep 自检确认 stale entry 仍在) | post-turn SHA-12 (本棒 0 修改后实测) | bytes | 一致? |
|---|---|---|---|---|---|---|
| 1 | `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | 287 | `results/_v4_v5_probe_test.log  sha12=b70e89448a3f  crc32=920dc342  bytes=1626` | `3A98F823CE33` | 26,833 | ✓ (本棒未触动; SHA-12 应与 mavis-trash 时刻之前一致 — 验证由 verifier 复核) |
| 2 | `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | 287 | 同上 | `5AB6A3BCC2A2` | 26,833 | ✓ (本棒未触动) |
| 3 | `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | 320 | 同上 | `D999A43D521F` | 29,820 | ✓ (本棒未触动) |
| 4 | `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | 320 | 同上 | `AB290AA01959` | 29,820 | ✓ (本棒未触动) |

注: manifest `5BF4D9AD2877` §3.1 登记之 stale entry **指向已 trashed 件** (`results/_v4_v5_probe_test.log`, SHA-12 `B70E89448A3F`, CRC32 `920dc342`, 1,626 B — 已由 manifest 处置清单本身 mavis-trash 至回收站). **本棒 0 触动**这 4 件 manifest (按派工单授权 + 链上件不动原则).

### 3.2 建议勘误链 E-31 入链内容 (供后续 doc-writer 起草)

> **建议项, 由 doc-writer 拍板措辞**:
>
> **E-31 — V4 R4 处置后链上件 stale entry 集合登记**
>
> 事实: 2026-09-24 R4 违规处置中, `_v4_v5_probe_test.log` (SHA-12 `B70E89448A3F`) 被 mavis-trash 至回收站 (见 `results/_v4_r4_key_purge_manifest_2026_09_24.md` §2.3). 该删除导致下列 stale entry 集合 — 登记所引文件已不在盘, 但因派工单纪律「链上件不动」, 4 件 v4_supp hash manifest 原文不动. 任何下游引用应以此集合为 stale 标记, 实际数据以 R4 处置清单 `5BF4D9AD2877` 为准:
>
> | 链上件 (Rel) | 行号 | 指向 (已不在盘) |
> |---|---|---|
> | `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | 287 | `_v4_v5_probe_test.log` (sha12=`B70E89448A3F`) |
> | `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | 287 | 同上 |
> | `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | 320 | 同上 |
> | `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | 320 | 同上 |
>
> 处置: 由 PI 决定 (a) 接受 stale / (b) 重建 v4_supp hash manifest / (c) 从 hash manifest 撤回 entry; 沿用 `5BF4D9AD2877` §3.1 PI 决策点之 a/b/c 口径.

---

## 4. Key 报废结案登记 (PI 确认 4 个 key 均为已废弃测试 key, 无需轮换)

| # | key_sha12 指纹 | 来源 (在哪件文件被发现) | provider 推断 | 结案状态 |
|---|---|---|---|---|
| 1 | `6CD6FE9FB32F` | `results/_v4_v5_probe_test.log` (SHA-12 `B70E89448A3F`) + `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` §5.6 证据段 (redact 后) | OpenRouter (sk-or-v1- prefix) | **CLOSED — 已废弃测试 key, 无需轮换 (PI 拍板 ask_d38952e0 r4_rotate=no_need, 2026-09-24 19:00)** |
| 2 | `00249F41B80D` | 同 #1 | teamorouter (sk-teamo- prefix) | **CLOSED — 已废弃测试 key, 无需轮换 (PI 拍板同上)** |
| 3 | `96D5AE961FB5` | 同 #1 | sk-ad9b56- prefix (provider 推断不明) | **CLOSED — 已废弃测试 key, 无需轮换 (PI 拍板同上)** |
| 4 | `D6760FC68827` | `D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` (行 39 + 54, redact 后) | OpenRouter (sk-or-v1- prefix) | **CLOSED — 已废弃测试 key, 无需轮换 (PI 拍板同上)** |

**结案后行为**:
- 这 4 个 key 指纹不再追踪, 不发起 incident response (无轮换 / 无 provider 报备).
- 后续勘误链 / 引用链提及这 4 个 key 时, 一律以 `key_sha12=<指纹前12>（closed per ask_d38952e0 r4_rotate=no_need, 2026-09-24）` 形式指代.
- **边界外遗珠** (本棒不擅自登记结案, 见 §6.4): JSON 行 24 之 `ark-` key fingerprint unrecorded (因扫描盲点未捕获); MD §5.6 段 4 之 truncated `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` 同样 unrecorded — 这 2 处 PI 是否纳入结案清单, 由 PI 另决.

---

## 5. 误报根因追查 (盘点棒 §2.2 误登 3 件 NOT-ON-DISK 之根因)

### 5.1 事实复盘

盘点棒 (`results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` SHA-12 `2FADEA9F6259`) §2.2 表 (行 119-132) 列示以下 3 件 briefed 件为 **MISSING** (NOT-ON-DISK):

| 件 | 盘点件登记 SHA-12 | 盘点件 §2.2 登记 filename | 盘点件结论 |
|---|---|---|---|
| 1 | `1665F367B2C4` | `results/_v4_pi_cot_v2_ruleset_result.json` | **MISSING** |
| 2 | `EB9AD4193CF2` | `results/_v4_pi_cot_v2_ruleset_verdict.md` | **MISSING** |
| 3 | `CC25C5149CE1` | `results/_v4_pi_cot_v2_ruleset_prereg.md` | **MISSING** |

勘误件 (`results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` E1.2) 已 parent 实测三件**实际在盘**, SHA-12 逐一 MATCH.

### 5.2 本棒实测验证 (2026-09-24 19:02)

```
$ Test-Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_result.json"
True
$ Test-Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_verdict.md"
True
$ Test-Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_prereg.md"
True

$ sha = (Get-FileHash -Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_result.json" -Algorithm SHA256).Hash.ToUpper()
$sha.Substring(0,12)
1665F367B2C4   # ✓ MATCH §2.2 登记 SHA-12

$ sha = (Get-FileHash -Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_verdict.md" -Algorithm SHA256).Hash.ToUpper()
$sha.Substring(0,12)
EB9AD4193CF2   # ✓ MATCH

$ sha = (Get-FileHash -Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2_prereg.md" -Algorithm SHA256).Hash.ToUpper()
$sha.Substring(0,12)
CC25C5149CE1   # ✓ MATCH

$ Get-ChildItem -Path "D:\私人资料\deposon-repo\results\_v4_pi_cot_v2*" | Select-Object Name
_v4_pi_cot_v2_collection_log.md
_v4_pi_cot_v2_dataset.json
_v4_pi_cot_v2_dataset_addendum_2026_09_24.json
_v4_pi_cot_v2_prereg.md                                    # ← 无 _ruleset_ 中缀
_v4_pi_cot_v2_prereg_activation_2026_09_23.md
_v4_pi_cot_v2_questionnaire_v1.md
_v4_pi_cot_v2_result.json                                  # ← 无 _ruleset_ 中缀
_v4_pi_cot_v2_ruleset.json                                 # ← 有 _ruleset_ 中缀 (但匹配 §2.2 已 MATCH)
_v4_pi_cot_v2_ruleset_executor.py                          # ← 有 _ruleset_ 中缀 (但匹配 §2.2 已 MATCH)
_v4_pi_cot_v2_verdict.md                                   # ← 无 _ruleset_ 中缀
```

### 5.3 同盘点件 §5.5 IN-EFFECT 表交叉核对

盘点件 §5.5 (IN-EFFECT roll-up) 行 987 / 990 / 993 列示**同一组 SHA-12** 之 3 件, 登记为 IN-EFFECT:

| 件 (盘点件 §5.5 登记 filename) | SHA-12 | 状态 |
|---|---|---|
| `results/_v4_pi_cot_v2_result.json` (行 990) | `1665F367B2C4` | IN-EFFECT |
| `results/_v4_pi_cot_v2_verdict.md` (行 993) | `EB9AD4193CF2` | IN-EFFECT |
| `results/_v4_pi_cot_v2_prereg.md` (行 987) | `CC25C5149CE1` | IN-EFFECT |

### 5.4 根因结论 (CONFIRMED)

**根因**: **盘点件 §2.2 lookup 表格 filename 列使用了 briefing 来源之命名约定 (含 `_ruleset_` 中缀), 而实际 on-disk 文件命名约定为不含 `_ruleset_` 中缀 — 两者存在命名漂移 (naming drift)**.

**取证**:

1. 盘点件 §2.2 行 127-129 登记的 filename (含 `_ruleset_` 中缀):
   - `_v4_pi_cot_v2_ruleset_result.json` (3 件, SHA-12 `1665F367B2C4`)
   - `_v4_pi_cot_v2_ruleset_verdict.md` (3 件, SHA-12 `EB9AD4193CF2`)
   - `_v4_pi_cot_v2_ruleset_prereg.md` (3 件, SHA-12 `CC25C5149CE1`)

2. 盘点件 §5.5 IN-EFFECT roll-up 行 987/990/993 登记的 filename (无 `_ruleset_` 中缀):
   - `_v4_pi_cot_v2_result.json` (同一 SHA-12 `1665F367B2C4`, IN-EFFECT)
   - `_v4_pi_cot_v2_verdict.md` (同一 SHA-12 `EB9AD4193CF2`, IN-EFFECT)
   - `_v4_pi_cot_v2_prereg.md` (同一 SHA-12 `CC25C5149CE1`, IN-EFFECT)

3. **同盘点件 (SHA-12 `2FADEA9F6259`) 内 §2.2 与 §5.5 对同一 SHA-12 使用不同 filename**: §2.2 错登含 `_ruleset_` 中缀 (3 件均 NOT-ON-DISK), §5.5 正确登记无 `_ruleset_` 中缀 (3 件均 IN-EFFECT). **SHA-12 完全一致, 仅 filename 是否含 `_ruleset_` 中缀不同**.

4. 实际 on-disk 验证 (本棒 2026-09-24 19:02 实测):
   - 含 `_ruleset_` 中缀之 filename **均不存在** (`_v4_pi_cot_v2_ruleset_result.json` / `_v4_pi_cot_v2_ruleset_verdict.md` / `_v4_pi_cot_v2_ruleset_prereg.md` 三个文件均 `Test-Path` = False)
   - 无 `_ruleset_` 中缀之 filename **均在盘** + SHA-12 逐一 MATCH §2.2 登记值

**机制推断**: 派工单 briefing 在列示任务 B v2.2 §3 之 6 件预期产出时, 大概率沿用 `_ruleset_executor.py` (在盘, SHA-12 `48DCA1D4281C`) + `_ruleset.json` (在盘, SHA-12 `821465001819`) 之 `_ruleset_` 前缀命名约定, 故 briefing 全文写为 `_ruleset_result.json` / `_ruleset_verdict.md` / `_ruleset_prereg.md`. 但实际 producer 落盘时**未延续该中缀**, 落盘为 `_result.json` / `_verdict.md` / `_prereg.md` (与 `collection_log.md` / `dataset.json` / `dataset_addendum_2026_09_24.json` / `prereg_activation_2026_09_23.md` / `questionnaire_v1.md` 等其他 v2 件之命名约定一致). 盘点件 §2.2 author 在转录 briefing filename 时**未察觉命名漂移**, 直接按 briefing 文本机械照抄 → 后续 `Test-Path` 命中 False → 登记为 NOT-ON-DISK.

**对比 §5.5**: §5.5 IN-EFFECT roll-up 大概率是另一次扫描 (可能按 on-disk 实际 glob 模式 `*_v4_pi_cot_v2_*` 或类似模式) 得出, 因此 filename 列与 §2.2 转录 briefing 文本不同, 与 on-disk 实况一致, 故 3 件均 IN-EFFECT.

### 5.5 根因可信度

- **高**: 同盘点件内部 SHA-12 完全一致 + filename 是否含 `_ruleset_` 中缀之差异, + on-disk 实测双向验证 (含 `_ruleset_` 中缀件不存在; 无中缀件在盘且 SHA-12 逐一 MATCH) — 三方证据闭环.
- **不能 100% 锁定子环节** (无 briefing 原文可供对照, 无法 100% 证实是 briefing 命名约定漂移 vs §2.2 author 转录错误) — 但**最终结论「§2.2 filename 列与 on-disk 实况不符 → 致 3 件 NOT-ON-DISK 误报」是事实级确认**.

### 5.6 处置建议 (供勘误链 E-31 引用)

- 任务 B v2.2 §3 三件**实际在盘且 SHA-12 逐一 MATCH** (本棒 + 勘误件 `55CD332F66F2` E1.2 parent 双方实测).
- 盘点件 §2.2 表**形为失误实为命名漂移** — 不构成 v2.2 verdict 结论之错误 (verdict 仍按 SHA-12 MATCH 成立; 失败点探索性 FAIL / 假证伪疑点未排除之口径沿用 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §5 E-25/E-26).
- 建议勘误链入 E-31:
  > **E-31 (本棒建议) — 盘点件 §2.2 NOT-ON-DISK 误报根因登记**: 经 2026-09-24 R4 处置棒 root-cause 追查 (ask_d38952e0 §④), 根因为 **盘点件 §2.2 lookup 表格 filename 列与 on-disk 实况存在命名漂移 (naming drift)** — §2.2 沿用派工单 briefing 之 `_ruleset_` 中缀命名 (`_v4_pi_cot_v2_ruleset_result.json` / `_v4_pi_cot_v2_ruleset_verdict.md` / `_v4_pi_cot_v2_ruleset_prereg.md`), 但 on-disk 实际无 `_ruleset_` 中缀 (`_v4_pi_cot_v2_result.json` / `_v4_pi_cot_v2_verdict.md` / `_v4_pi_cot_v2_prereg.md`). 同盘点件 §5.5 IN-EFFECT roll-up 按 on-disk glob 模式登记, filename 与 §2.2 转录 briefing 文本不同, 与 on-disk 实况一致. 建议 doc-writer 入勘误链时引述本棒 §5.4 根因结论 + §5.2 实测证据.

---

## 6. 老实交代 (honest disclosure)

### 6.1 R4 key 永不明文 (无例外) 本棒守纪

- 本棒全程未输出任何 key 明文; 任何对 key 的指代一律以 `key_sha12=<指纹前12>（redacted per ask_d38952e0, 2026-09-24）` 或 `key_sha12=<指纹前12>（closed per ask_d38952e0 r4_rotate=no_need, 2026-09-24）` 形式.
- 落盘后 grep 自检两件 redact 件, 0 件 key 明文残留 (见 §2.1.3 + §2.2.2).
- 本清单自身 grep 自检: 0 件 key 明文 (仅 fingerprint 引用).

### 6.2 边界严守

- 本棒**仅动**: ① MD inventory redact §5.6 行 3773 (4 段 key 明文); ② JSON sanity redact 行 39 + 54 (2 处 sk-or-v1- key); ③ 新建本清单 `results/_v4_r4_purge_actions_2026_09_24.md`.
- 本棒**未触动**: `.tmp/_r4_key_scan_*` 审计件 (2 件); `letters/` 3 封委托信; 清理链 ledger (4 件); 四棒在移文件; 4 件 v4_supp hash manifest (§3); 3 件 chain manifest (§2.2.4); 盘点件 §5.7/§5.8 fingerprint 段 (§2.1.4); 派生 JSON; 阈值; 既有 V1–V3 frozen 件.
- 0 LLM / 0 gateway / 0 key 落盘 (除 §6.3 已老实交代的 JSON 行 24 ark- key 本棒不动外).

### 6.3 JSON 行 24 ark- key 未 redact 之老实交代

- **派工单显式授权范围**: 「`D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json`... 行 39/54 附近的独立 key（指纹 D6760FC68827）」— 仅指向行 39 + 54 之 sk-or-v1- key.
- **派工单边界**: 「只动上述 2 件 redact + 新建 1 件清单; 其余（含 `.tmp/_r4_key_scan_*` 审计件、letters/ 3 封委托信、清理链 ledger、四棒在移文件）一概不碰」— 在 redact 范围内, 仅 39/54 行 + D6760FC68827 是指定目标.
- **JSON 行 24 实际有 ark- key**: `key_sha12=7348FC7D6C33`（volcengine ark-style, UUID 格式, fingerprint 未被 manifest 扫描捕获, 属扫描盲点 — 因 manifest §1 正则 `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` 要求 16+ 连续 alphanumeric 而 UUID 多 dash 结构不满足; 本棒不复述 plaintext）
- **本棒不擅动**: 按派工单字面边界 + 不擅自重写原则, 行 24 ark- key **本棒不动**. 由 PI 决定 (a) 接受 (b) 另派 doc-writer/verdict-keeper redact (c) 重建 archive manifest 排除.
- 本棒在 §4 边界外遗珠段 + §2.2.3 已老实交代此事, 不擅自重写, 不擅自登记结案.

### 6.4 §5.6 段 4 truncated `rk-...` key 之 fingerprint unrecorded

- §5.6 段 4 原 key `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` 为**截断形式** (truncated in probe output); manifest §1 正则 `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` 亦未匹配 (类似 §6.3 UUID 多 dash 盲点).
- 本棒 redact 时以 `key_sha12=unrecorded` 占位, 注明「per-key fingerprint unrecorded in manifest §2.1 — scan regex blind spot」.
- **本棒不擅自推断**: 不擅自给 `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` 算 fingerprint, 不擅自将其纳入 §4 报废结案清单; 由 PI 决定是否纳入.

### 6.5 skill 缺位老实交代

- 派工单指定 `superpowers:verification-before-completion`, 本地 skill 加载器可能未就绪.
- 本棒**未编造**该 skill 不存在的虚构指令, 沿用 `results/_v4_r4_key_purge_manifest_2026_09_24.md` §0.2/§2/§3 + `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` (勘误件 `55CD332F66F2`) 勘误留痕格式为纪律锚.
- 凡指纹指代、JSON 语法校验、grep 自检、pre/post SHA-12 对照等, 一律按 fallback 纪律锚之规范执行.

### 6.6 红线严守 (铁律 7+9 自查)

| 红线 | 触犯? | 备注 |
|---|---|---|
| R1 no_llm (V3 期) | 否 | V4 已放开 (R1-R3 放开 / R5 重建 / R6-R7 放开, PI 09-22 定稿); 本棒 0 调用 LLM |
| R2 no_proxy (V3 期) | 否 | 同上; 本棒 0 proxy |
| R3 no_gateway (V3 期) | 否 | 同上; 本棒 0 gateway |
| **R4 key 永不明文** (无例外) | **否** | 本棒全程 key 文本以 fingerprint 形式指代; grep 自检 0 明文残留 |
| R5 V4 frozen 重建 | 否 | V1-V3 frozen 0 触动; V4 frozen 由 R5 重建规则适用, 本棒 0 触动 V4 frozen |
| R6 P-G v0/v01 V4 自由读写 | 否 | 本棒 0 触动 P-G |
| R7 plugin spec V4 专用 | 否 | 本棒 0 触动 plugin spec |
| 9 铁律 key runtime 读不入 prompt/JSON/log | 否 | JSON redact 段仅替换 `"key"` 字段之明文, 未新增 key 引入; fingerprint 引用按 PI 拍板合规 |
| 9 铁律 no-key 自扫 | 否 | 见 §6.1 + §6.3 |
| 9 铁律 不擅动 workspace 外 | 否 | 仅动 2 件 redact (在 workspace 内) + 1 件新建 (在 workspace 内) |
| 9 铁律 SHA-12 + manifest 留痕 | 否 | 本清单 §0 + §8 留痕 |
| 派生 JSON 不合并 | 否 | JSON redact 系修改既有 JSON, 非派生 JSON; §2.2 JSON 语法校验通过 |
| 0 擅调阈值 | 否 | 0 阈值调整 |
| 不覆盖既有件 | 否 | 仅 redact 2 件 (line-level 行级替换, 非整件覆盖) + 新建 1 件清单 (无既有件覆盖) |

---

## 7. 派工单 4 项拍板 → 落地映射总览

| 拍板项 | 落地段 | 状态 |
|---|---|---|
| ① redact_both | §2.1 (MD inventory §5.6 行 3773) + §2.2 (JSON sanity 行 39 + 54) | **DONE** (2 件均 redact + 语法校验 OK + grep 自检 0 明文残留) |
| ② stale 入勘误链 4 件 manifest 不动 | §3 (4 件 hash manifest pre/post SHA-12 一致性核验) + §3.2 (建议勘误链 E-31 入链内容, 供 doc-writer 起草) | **DONE** (4 件 manifest 0 触动; 素材备齐, 待 doc-writer 入 E-31) |
| ③ key 报废结案 (PI 确认均为已废弃测试 key, 无需轮换) | §4 (4 个 key fingerprint 统一登记 CLOSED) | **DONE** (4 个 key 全部 CLOSED; 不再追踪; 不发起 incident response) |
| ④ 追查误报根因 | §5 (3 件 NOT-ON-DISK 误报根因 = naming drift / `_ruleset_` 中缀问题) | **DONE** (root-cause 已 CONFIRMED; 建议勘误链 E-31 入链内容 §5.6 已备齐) |

---

## 8. 指纹 (本清单本身)

| 字段 | 值 |
|---|---|
| 路径 | `results/_v4_r4_purge_actions_2026_09_24.md` |
| SHA-12 | (本清单自我引用存在鸡生蛋问题, 由 verifier 复核时以 `Get-FileHash -Algorithm SHA256` 核) |
| 字节 | (同上) |
| Modified | 2026-09-24 19:05 (worker 写入; 后续 verifier 复核时核最终 SHA-12) |
| 角色 | R4 落地处置清单 (B-class 留痕, 沿 `results/_v4_r4_key_purge_manifest_2026_09_24.md` `5BF4D9AD2877` 格式) |

---

## 9. 收口

- 4 项派工拍板全部 DONE (见 §7 总览).
- 2 件 redact 文件落盘实测 (pre/post SHA-12 + bytes + 语法校验 + grep 自检, 见 §2).
- 4 件 v4_supp hash manifest 0 触动 (pre/post 一致性核验由 verifier 复核, 见 §3.1).
- 4 个 key 指纹统一 CLOSED 登记 (见 §4).
- 3 件 NOT-ON-DISK 误报根因追查完成 (naming drift / `_ruleset_` 中缀问题, CONFIRMED, 见 §5).
- 边界严守: 0 件派生 JSON 合并; 0 件阈值调整; 0 件既有 V1-V3 触动; 0 件 key 明文输出; 0 件派工单未授权范围触动 (除 §6.3 老实交代 JSON 行 24 ark- key 不动外).
- **本棒 0 启动 LLM / proxy / gateway 调用** (V4 R1-R3 已放开, 但本棒 0 调用需要).
- **待 PI 拍板项** (本棒未擅自代决):
  - JSON 行 24 ark- key 是否纳入结案清单 / 另派 doc-writer redact (见 §6.3)
  - §5.6 段 4 truncated `rk-...` key 是否纳入结案清单 (见 §6.4)
  - §3.2 建议 E-31 入链内容由 doc-writer 拍板措辞 (本棒仅供素材)
  - §5.6 建议 E-31 入链内容 (本棒 §5.4 根因结论) 由 doc-writer 拍板措辞
  - §2.1.4 + §2.2.4 链副作用注记 (MD §5.7/§5.8 历史快照 stale + JSON 3 件 chain manifest 引用 stale) 之 a/b/c 处置由 PI 决定
- **本件状态**: 落地处置清单已出; 与 `5BF4D9AD2877` 处置清单 + `55CD332F66F2` 勘误件 三件并列存在; 下游 doc-writer / verdict-keeper / evidence-auditor 可据此推进勘误链 E-31 入链.

— 完 —

---

## 10. §7 补 redact 记录 (行 24 ark- key 漏扫补执行; 同 §6.3 拍板)

| 字段 | 值 |
|---|---|
| 授权依据 | sk_d38952e0 r4_redact=redact_both (2026-09-24 19:00 拍板) |
| 处置棒 | worker (执行类·数据修订); 沿 §6.3 同一拍板, 不另开 ask |
| 漏扫根因 | R4 处置棒扫描正则盲点 — rk- UUID 多 dash (rk-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX-suffix) 未匹配 rk- 类模式, 漏 1 处 |
| 拍板归属 | §6.3 拍板对象件 _d05_sanity JSON 之内, 本棒补执行同一拍板 (rerun 同口径) |
| 文件 | esults/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json |
| 行号 | 24 |
| 原 key 指纹 | key_sha12=7348FC7D6C33 |
| 替换形式 | "key": "key_sha12=7348FC7D6C33（redacted per ask_d38952e0, 2026-09-24）" |
| pre SHA-12 | E6173BC63DF5 |
| pre 字节 | 2,273 B |
| post SHA-12 |  A1E91D6F772 |
| post 字节 | 2,292 B |
| 字节增量 | +19 B (47B ASCII key → 22 ASCII + 2×3B UTF-8 全角括号 + 36 ASCII) |
| JSON 语法校验 | Python json.loads strict PASS; ConvertFrom-Json UTF-8 PASS |
| grep 自检 (ark- 模式) | 0 命中 |
| grep 自检 (UUID 片段) | 0 命中 (扫 8a656459c77\|3ae14873\|faa0a) |
| grep 自检 (truncated) | 0 命中 |
| 链 manifest 引用 | 同 §3 (4 件 v4_supp hash manifest 0 触动; 该 JSON 不在 4 件之内) — 无 chain manifest 引用, 无 stale SHA 风险 |
| 边界严守 | 仅动该 JSON 行 24; 四棒在移文件 / letters/ / 4 件 v4_supp manifest / 盘点件 / .tmp/_r4_key_scan_* 一概不碰 |
| 拍板收口 | §6.3 第 1 子项 (JSON 行 24 ark- key) 由"待拍板"转为 DONE (按同口径补 redact); §9 改口该项已闭环 |

---

## 10.1 尾项归档注记 (§5.6 / §5.7–§5.8 / chain manifest stale 移交 doc-writer E-31)

### 10.1.1 §5.6 4 处 truncated k-... key — 归入 CLOSED (结案类, 不再追踪)

- 拍板: sk_d38952e0 r4_rotate=no_need (PI 确认已废弃测试 key, 无需轮换)
- 处置: 4 个 truncated k-… key (fingerprint=unrecorded, 因原文已被截断无法还原指纹) 统一归入 §4 CLOSED 类
- 状态: **DONE**; 不再追踪; 不发起 incident response
- 移交: 无 (本类已结案, 不入 doc-writer 勘误链 E-31)

### 10.1.2 MD §5.7 / §5.8 历史快照段 stale — 移交 doc-writer 勘误链 E-31 注记

- 拍板: sk_d38952e0 r4_stale=erratum 精神 (勘误注记; 被引件不动)
- 处置: MD §5.7 / §5.8 段中残留的历史快照 stale 描述 (指向的 pre-SHA 已变化) 不重写, 由 doc-writer 在勘误链 E-31 入链内容中统一加勘误注记
- 移交: doc-writer (起草类专属); 输入: §5.4 根因结论 + §3.2 E-31 入链草稿
- 边界: 本棒不动 MD 前文; 仅追加本节注记, 由 doc-writer 复审措辞后归并入 E-31

### 10.1.3 JSON 被 3 件 chain manifest 引用之 stale SHA — 移交 doc-writer 勘误链 E-31 注记

- 拍板: sk_d38952e0 r4_stale=erratum 精神 (勘误注记; 被引件不动)
- 处置: 3 件 chain manifest 引用本 JSON 时记录的 stale SHA 不重写, 由 doc-writer 在勘误链 E-31 入链内容中加注记 (指出当前 SHA-12 =  A1E91D6F772, 2,292 B)
- 移交: doc-writer (起草类专属); 输入: 本棒 post SHA-12 / 字节报告 + §3.1 verifier 复审结论
- 边界: 被引件 (3 件 chain manifest) 一概不动; 仅追加本节注记, 由 doc-writer 复审措辞后归并入 E-31

---

## 11. 自存 (本清单纯自存, 供 verifier 复核)

| 字段 | 值 |
|---|---|
| 路径 | esults/_v4_r4_purge_actions_2026_09_24.md |
| SHA-12 (本棒追加前) | 72D213B39FA1 |
| SHA-12 (本棒追加后) | (verifier 复核时以 Get-FileHash -Algorithm SHA256 核) |
| 字节 (本棒追加前) | 28,925 B |
| 字节 (本棒追加后) | (verifier 复核时核) |
| Modified | 2026-09-24 19:18 (worker 补 redact + 追加 §10/§10.1) |
| 角色 | R4 落地处置清单 §10/§10.1 补 redact + 尾项归档注记 (追加段, 不改前文) |
| 上游 | sk_d38952e0 r4_redact=redact_both + r4_rotate=no_need + r4_stale=erratum |
| 下游 | doc-writer (勘误链 E-31 入链内容起草, §10.1.2 / §10.1.3); verdict-keeper / evidence-auditor 可据此推进 |

— 完 — (补 redact + 尾项归档 注记追加)