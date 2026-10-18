# V4 R4 key 明文违规 紧急处置清单 (2026-09-24)

> by **worker** (执行类·安全紧急处置)
> Generated: 2026-09-24 18:50
> Predecessor scan: `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (SHA-12 `2FADEA9F6259`) §5.6 R4 finding
> 派工单授权来源: 本棒 R4 违规最高纪律 (`key 永不明文 / 无例外`)

---

## 0. Dispatch Record (5-item checklist)

| slot | value |
|---|---|
| 1. agent name | worker (执行类) |
| 2. skill name | `superpowers:verification-before-completion` (sha256 `ade95665080e...`) — 老实交代 skill 缺位纪律锚 fallback = `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` §5.6 R4 finding 段 + `results/_v4_maindir_cleanup_manifest_2026_09_24.md` (SHA-12 `32CC61D394F2`) B 类删除留痕格式; **未编造 skill 不存在的虚构指令** |
| 3. plugin | `@superpowers` |
| 4. iron rules (7+9) | **R4 key 永不明文 (无例外) = 本棒授权来源**; V1–V3 frozen 只读不动; 派生 JSON 不合并; 0 擅调阈值; 不覆盖既有件 (本棒仅写本清单新件 + 1 件中间扫描产物于 `.tmp/`); 处置清单/落盘/log 全文 **不含任何 key 明文** |
| 5. honest disclosure | 0 产物报 0 产物; succeeded ≠ 跑完落盘核验; **本棒全程未输出任何 key 明文**; 删除走 `mavis-trash` 回收站 (可恢复, 禁止永久删除); 链上件 (被 manifest/prereg/verdict/manifest-archive 引用) 含 key 的**不动**, 单独列入待拍板清单 |

---

## 1. 扫描方法 (multi-encoding)

- **编码集**: UTF-8 / UTF-8-BOM / GB18030 / GBK / UTF-16LE / UTF-16BE / Big5 (6 套)
- **key 形态正则** (严格, 排除 `ask_` 工具 ID 类假阳性):
  - `sk-or-v1-[A-Za-z0-9]{16,}` (OpenRouter)
  - `sk-teamo-[A-Za-z0-9]{16,}` (teamorouter)
  - `sk-ad9b[A-Za-z0-9]{16,}`
  - `sk-[A-Za-z0-9]{20,}` (generic OpenAI-style, ≥20 字符避 `sk_<short>` 误报)
  - `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` (volcengine ark)
  - `AKIA[A-Z0-9]{16}` (AWS)
  - `AIza[A-Za-z0-9_-]{35}` (Google)
  - `ghp_[A-Za-z0-9]{36}` / `gho_[A-Za-z0-9]{36}` (GitHub)
  - `xoxb-[A-Za-z0-9-]{20,}` / `xoxp-[A-Za-z0-9-]{20,}` (Slack)
- **大小过滤**: 跳过 >10MB 文件 (避免卡顿)
- **目录扫描**: 跳过 `__pycache__/` 缓存
- **key 引用**: 命中处一律记 `文件 + 行号 + key 前缀 4 字符 + key SHA-12 指纹`; key 文本**全文不输出**
- **扫描脚本**: `.tmp/_r4_key_scan_2026_09_24.py` (中间产物, 留存审计)
- **扫描 JSON**: `.tmp/_r4_key_scan_results_2026_09_24.json` (含路径 + 编码 + 行号 + 4 字符前缀 + key SHA-12; **无任何 key 明文**)

---

## 2. 扫描结果 (pre-disposal)

| 字段 | 值 |
|---|---|
| 扫描文件总数 | 2901 (post = 2903, 因本棒新增 .tmp/ 2 件审计产物) |
| 命中文件数 (前) | 3 |
| 命中文件数 (后) | 2 |
| 处置 trashed | 1 |
| 处置 kept_pending_PI | 2 |
| 处置 false_positive | 0 (上轮 41 件 GB18030 假阳性 (Mavis `ask_` 工具 ID 类) 已严格排除; 本轮 3 件命中全部为真实 API key 形态) |

### 2.1 命中文件摘要

| # | 文件 (Rel) | 编码 | 命中行号 | key 4 字符前缀 (去重) | 唯一 key SHA-12 指纹 (去重) | 命中次数 | 处置 | 理由 |
|---|---|---|---|---|---|---|---|---|
| 1 | `results/_v4_v5_probe_test.log` | utf-8 + gb18030 + gbk + big5 | 10/12/14/20/22/24/30/32/34 | `sk-o`, `sk-t`, `sk-a` | `6CD6FE9FB32F`, `00249F41B80D`, `96D5AE961FB5` | 48 | **trashed** | 派工单 Task 1 显式 `立即处置` + `mavis-trash 回收站删除`; **多编码命中证实 GB18030-only 误识别风险**; 注: 该文件被 4 件 v4_supp hash manifest 引用 (见 §3.1 链副作用) |
| 2 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | utf-8 | 3773 | `sk-o`, `sk-t`, `sk-a` | `6CD6FE9FB32F`, `00249F41B80D`, `96D5AE961FB5` | 4 | **kept_pending_PI** | **链上件**: 本件为证据链锚根 (本轮 §5.6 段即在引述 #1 之 key 内容, **形为违规实为证据**); 同时被 `_v4_maindir_cleanup_manifest_2026_09_24.md` (SHA-12 `32CC61D394F2`) §0.2 引用为前驱 inventory; redact 改写会破坏 SHA-12 + 锚根引用, **需 PI 决定 redact 方式** (建议: 保留 §5.6 段但以 key SHA-12 指纹替代明文指代) |
| 3 | `deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | utf-8 | 39, 54 | `sk-o` | `D6760FC68827` | 2 | **kept_pending_PI** | **链上件** (in archive, 引用链存在): 被 `_archive_2026_09_20/_archive_manifest_2026_09_20.json` 第 3/318 行 + `_archive_manifest_deposon_sub_2026_09_23.json` 第 702 行 + `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` 第 3383 行 引用为 ARCHIVED 件; key 指纹 `D6760FC68827` 与 #1/#2 之 3 个指纹**不同** (独立 sk-or-v1- key); delete 会破坏 archive manifest 引用, **需 PI 决定 redact 或保留** |

### 2.2 处置细节 (per-file SHA-12 + bytes)

| # | 文件 (Rel) | 文件 SHA-12 (全) | 字节 | 处置 |
|---|---|---|---|---|
| 1 | `results/_v4_v5_probe_test.log` | `B70E89448A3F` | 1626 | trashed (回收站, 可恢复) |
| 2 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `2FADEA9F6259` | 57179 | kept_pending_PI |
| 3 | `deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | `5D583C612D07` | 2289 | kept_pending_PI |

### 2.3 处置动作证据

```
$ & "C:\Users\Administrator\.minimax\bin\mavis-trash.cmd" "D:/私人资料/deposon-repo/results/_v4_v5_probe_test.log"
mavis-trash: moved to trash: 'D:/私人资料/deposon-repo/results/_v4_v5_probe_test.log'

$ Test-Path "D:/私人资料/deposon-repo/results/_v4_v5_probe_test.log"
False   # 确认 #1 已落盘消失, 入回收站
```

---

## 3. 链副作用 (chain side-effects, PI 需知)

### 3.1 #1 删除导致 4 件 hash manifest 出现 stale entry

`_v4_v5_probe_test.log` (SHA-12 `B70E89448A3F`, CRC32 `920dc342`, 1626B) 在以下 4 件 v4_supp hash manifest 中**仍登记为在盘**:

| 链上 hash manifest (Rel) | 行号 | 登记内容 |
|---|---|---|
| `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | 287 | `results/_v4_v5_probe_test.log  sha12=b70e89448a3f  crc32=920dc342  bytes=1626` |
| `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | 287 | 同上 |
| `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | 320 | 同上 |
| `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | 320 | 同上 |

**PI 决策点**: 这 4 件 hash manifest 现含 stale entry (指向已 trashed 件). 沿派工单纪律 `链上件不动`, 本棒**未触动**这 4 件 hash manifest (SHA-12 应仍为原值, 因本棒 0 修改). 由 PI 决定:
- (a) 接受 stale entry (后续 v4_supp 复核棒自行重派生时一次性更新);
- (b) 重建 v4_supp hash manifest (需 PI 派 `evidence-auditor` / `verdict-keeper` 重派);
- (c) 从 hash manifest 撤回该 entry (需逐件改 4 件, 改 SHA-12).

### 3.2 #2 inventory 的 §5.6 段在文档化 #1 之 R4 违规证据

`results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (SHA-12 `2FADEA9F6259`) §5.6 (line 3652-3786) 段含 3 个 key 明文指代, **形为违规实为证据** (即证据链锚根本身在引述 #1 的 key 内容). 这是 R4 的灰色边缘 — 证据链必须保留违规记录, 否则 #1 的 R4 违规无法被审计追溯.

**PI 决策点**:
- (a) 保留 §5.6 段 key 明文 (作为证据);
- (b) redact §5.6 段为 key SHA-12 指纹 (`6CD6FE9FB32F` / `00249F41B80D` / `96D5AE961FB5` 替代明文) — 建议项;
- (c) 整段 §5.6 删除 (会破坏 §5.7/§5.8 段引用 + §0.2 anchor 链).

注: redact §5.6 段会改 SHA-12 (`2FADEA9F6259` → 新值), 需同步更新本棒 §0 之 SHA-12 + `_v4_maindir_cleanup_manifest_2026_09_24.md` §0.2 之 inventory SHA-12 引用.

### 3.3 #3 archive 文件被 3 件 chain manifest 引用

`deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` (SHA-12 `5D583C612D07`) 含独立 sk-or-v1- key (SHA-12 `D6760FC68827`, 与 #1/#2 之 3 个指纹**不同**). 被引用处:

| 链上 manifest (Rel) | 行号 | 引用方式 |
|---|---|---|
| `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 3, 318 | `src` + `dst` 双向引用 (历史归档记录) |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | 702 | `path` 字段引用 (09-23 deposon-sub 归档清单) |
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3383 | inventory 表 ARCHIVED 件引用 |

**PI 决策点**:
- (a) 接受 archive manifest 含 key 的 stale-but-historical 记录 (archive manifest 本就是历史快照);
- (b) 重建 archive manifest 排除该 entry;
- (c) redact 该 JSON 的 line 39/54 行 (会改 SHA-12, archive manifest 引用失效).

---

## 4. 复扫确认 (post-disposal re-scan)

| 检查项 | 结果 |
|---|---|
| `Test-Path` on `D:/私人资料/deposon-repo/results/_v4_v5_probe_test.log` | **False** ✓ (落盘消失) |
| 多编码复扫 (2903 文件) | `files_with_hits = 2` ✓ (#1 trashed 后, 仅剩 #2 + #3 链上件) |
| `0 假阳性` (本次扫描) | ✓ (上轮 41 件 GB18030 假阳性 (Mavis `ask_` 工具 ID 类) 已严格排除) |
| 新增文件 (本棒) | `.tmp/_r4_key_scan_2026_09_24.py` (扫描脚本, 中间产物, 留存审计) + `.tmp/_r4_key_scan_results_2026_09_24.json` (扫描结果, 含 SHA-12 指纹但**无 key 明文**) |
| V1–V3 frozen 触动 | 0 件 ✓ |
| 派生 JSON 合并 | 0 件 ✓ |
| 阈值调整 | 0 ✓ |
| 既有件覆盖 | 0 件 ✓ (本棒仅写本清单新件 + 2 件 `.tmp/` 中间产物) |

---

## 5. 老实交代 (honest disclosure)

1. **本棒全程未输出任何 key 明文** — 任何对 key 的指代一律以 `文件 + 行号 + key 前缀 4 字符 + key SHA-12 指纹` 形式.
2. **0 假阳性发现**: 上轮 41 件 GB18030 假阳性 (Mavis `ask_` 工具 ID 类) 经严格多编码 + 词边界正则扫描**确认 0 件** — 这些假阳性的字面特征是 GB18030 多字节序列的 `sk_<hex>` 渲染, 实际字节 0x61 ('a') 后接 `sk_` 不构成 API key 形态; 本棒正则要求 `sk-<20+chars>` 形态避开此类误报.
3. **#1 删除后链副作用**: 4 件 v4_supp hash manifest 现含 stale entry (链上件不动, 由 PI 决定重建/撤回); 本棒**未触动**这 4 件 hash manifest.
4. **#2 inventory 自身含 key 明文** (作为 R4 证据链锚根): 这是 R4 灰色边缘 — 派工单授权 R4 文档化保留但要求 `key 永不明文`, 二者张力由 PI 收口 (本棒列出 3 选项, 见 §3.2).
5. **#3 archive 文件含独立 key (D6760FC68827)**, 与 #1/#2 之 3 个 key 指纹**不同** — 是另一处 R4 违规 (deposon-sub 旧归档数据, 来源未追溯, 可能 V3 期 ckpt/sanity 直注现场).
6. **probe 源文件未找到**: 派工单 Task 2 要求顺藤摸瓜 probe 源件 (786 字节源, GB18030 编码, 含 `agent-plan` + `OpenRouter` + 4 类 key), 但全工作区未发现该 786 字节原文件 — 可能已被早期清理或从未落盘 (probe 是直接从 stdin/in-memory 读取). 本棒不擅补.
7. **skill 缺位老实交代**: 派工单指定 `superpowers:verification-before-completion`, 本地 skill 加载器可能未就绪; 本棒**未编造**该 skill 不存在的虚构指令, 沿用 `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` §5.6 R4 finding 段 + `results/_v4_maindir_cleanup_manifest_2026_09_24.md` B 类删除留痕格式为纪律锚.
8. **0 LLM / 0 gateway / 0 key 落盘 / 0 V1–V3 触动 / 0 阈值调整 / 0 既有件覆盖**: 沿派工单 §7+9 铁律本棒 0 违反.
9. **派工单张力说明**: 派工单 Task 1 显式 `立即处置 _v4_v5_probe_test.log` vs Task 2 链上件不动 规则**潜在张力** (probe log 被 v4_supp hash manifest 引用) — 本棒按 Task 1 字面授权执行 trashed, 同时在 §3.1 把 stale hash entry 链副作用诚实报 PI; **未擅自取舍**.

---

## 6. 待拍板项 (PI 决策点汇总, 4 项)

> 沿 `2026-09-21 待拍板项必须用工具提问` 纪律, 本棒先穷尽清点全部未决项成册 (本节), **未用 ask_user 工具** — 派工单未明示需本棒发起问卷, 由父棒统一发起.

1. **#1 stale hash entry**: 4 件 v4_supp hash manifest 现含 trashed 件的 stale entry, 由 PI 决定 (a) 接受 / (b) 重建 / (c) 撤回 entry (见 §3.1)
2. **#2 inventory redact**: §5.6 段含 key 明文 (作为证据), 由 PI 决定 (a) 保留 / (b) redact 为 SHA-12 指纹 / (c) 整段删除 (见 §3.2)
3. **#3 archive JSON redact**: `_d05_sanity_3backbone_20260918_100110.json` line 39/54 含独立 key, 由 PI 决定 (a) 接受 / (b) 重建 archive manifest / (c) redact JSON (见 §3.3)
4. **新发现 key (D6760FC68827) 是否已泄露**: 该 key 仅在 archive 内出现, 但派工单未明示是否需做 incident response (key 轮换 / provider 报备); 由 PI 决定

---

## 7. 清单字段 schema (供下游引用)

```
file_rel       # 相对路径 (相对 / 扫描根)
file_sha12     # 文件 SHA-12 指纹 (前 12 位)
bytes          # 文件字节数
enc            # 命中编码 (utf-8 / gb18030 / gbk / utf-16-le / utf-16-be / big5)
hit_lines      # 命中行号列表
prefix4_set    # 命中 key 前缀 4 字符去重集
key_sha12_set  # 命中 key SHA-12 指纹去重集 (key 文本**全文不存此字段**)
disposition    # trashed / kept_pending_PI / false_positive / none
reason         # 处置理由
```

---

## 8. 指纹 (本清单本身)

| 字段 | 值 |
|---|---|
| 路径 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` |
| SHA-12 | (本清单自我引用存在鸡生蛋问题, 由 verifier 复核时以 `Get-FileHash -Algorithm SHA256` 核) |
| 字节 | (同上) |
| Modified | 2026-09-24 18:51 (worker 写入; 后续 verifier 复核时核最终 SHA-12) |
| 角色 | R4 紧急处置清单 (B-class 留痕, 沿 `_v4_maindir_cleanup_manifest_2026_09_24.md` 格式) |

---

**收口**: 处置清单落盘 ✓; 复扫 2 件链上件 (kept_pending_PI) ✓; 待拍板 4 项诚实上报 ✓; 0 件 V1–V3 触动 ✓; 0 件 key 明文输出 ✓.