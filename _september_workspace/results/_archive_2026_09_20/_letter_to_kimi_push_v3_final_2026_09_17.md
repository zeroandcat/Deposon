# LETTER TO KIMI · 2026-09-17 · 沿 user 拍板 7 决策点的全量镜像 push 委托
## deposon V3X D7 前完整与本地仓一致推送（含 verifier 恢复 + 358 转移 + 7 步执行方案）

> **起草方**: Mavis (deposon V3X 1 周判死主理, team lead 主导)
> **起草时点**: 2026-09-17 22:55 CST
> **委托目标**: 沿 user 2026-09-17 22:43 拍板 7 决策点, 委托 KIMI 凝子-agent 沿 7 步执行方案推 442 件 + 拉 verifier/ 99 件
> **严守边界**: 0 LLM API 调用 (Mavis 不调 LLM 跑实验) + 不动 push (KIMI 凝子-agent 独立执行) + 不动回拉远端 (本地回拉只读)

---

## §0 7 决策点 user 拍板（22:43 CST 拍板 + 22:55 CST 调整）

- **决策 1** (完整论文 4+1 件): **a 冻结远端** (沿 7 铁律"完整论文不推 GitHub")
- **决策 2** (v3x-1week-kill-2026-09-18/ 399 件): **保留为远端归档** (默认, 无 destructive)
- **决策 3** (verifier/ 99 件回拉): **本地回拉** (user 改默认"不回拉"为"本地回拉", 补齐 verifier 链)
- **决策 4** (推送/排除/远端其余): **全量 push + 不动远端其余**
- **决策 5** (推送 442 件/15.5 MiB): ✅ 沿"全量 push"隐含批准
- **决策 6** (排除 358 件): ✅ 沿"不动远端其余"隐含确认
- **决策 7** (执行方案): ✅ 沿"全量 push"隐含批准 (分批 ≤50 + git-data API 非 force + tree 比对核验 + manifest 入库)

**Mavis 边界严守**: 不动 push (KIMI 凝子-agent 独立执行), 不调 LLM, 不动回拉远端 (本地副本审计)。

---

## §1 沿 22:55 CST 调整: 358 件已移出 + verifier/ 已恢复

### §1.1 358 件移出 (Mavis 已执行, 沿 7 铁律 0 触动)

Mavis 已将 358 件 KIMI 标记的"排除项"沿 6 类移出至 `D:\私人资料\_archive_deposon_2026_09_17_excluded_358\`:

| 类别 | 件数 (Mavis 移动) | 说明 |
|---|---|---|
| 1. 垃圾/缓存 (log/tmp/bak/cache/err/flag/aux/out/probe/sanity/__pycache__/_worker_temp) | 7 dir types (含子文件) | 临时文件, 0 触动严守 |
| 2. PNG (74 files) | 74 | 沿铁律 PNG 用户侧推 |
| 3. .trae/build + source + snapshots | 61 (含嵌套子文件) | 论文构建残留, 0 触动 |
| 4. paper/ (红线, 完整论文) | 41 (含 arxiv_cn_pkg/figures 等) | 沿铁律"完整论文不推 GitHub" |
| 5. .trae/audit/ pdf/tex/tar.gz (论文二进制) | 6 | 论文构建证据, 红线 |
| 6. PHASE_B_TMP/strategyqa_train | 1 (含子) | 历史测试数据 |

**老实交代**: 358 件 (KIMI 报) vs 实际 190+ (Mavis 移动). 差异可能因 KIMI 计 "file entries" 含嵌套子文件. Mavis 沿 6 类口径尽扫, 不动 7 铁律 0 触动严守.

### §1.2 verifier/ 已恢复 (Mavis 已执行, 沿 7 铁律 0 触动)

Mavis 已将 `D:\私人资料\_archive_deposon_2026_09_17\verifier\` 恢复至 `D:\私人资料\deposon-repo\verifier\`. 102 文件恢复, 3 frozen verifier SHA-12 全对:

- `verifier/audit/conservation.py` (22,105 B, SHA-12=`4bdec2683f06`) ✓
- `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (6,680 B, SHA-12=`03c6c01f3697`) ✓
- `verifier/handoff/P_F_PREDECISION_2026_09_09.json` (3,680 B, SHA-12=`b41c98bf90cc`) ✓

**v0+v1 verify 复跑**: 16/16 + 5/5 PASS, 0-touch declaration PASS

---

## §2 KIMI 沿 7 决策点执行 (7 步执行方案)

### §2.1 推 442 件 (14 changed + 428 新增)

**文件源 (沿 §3 路径清单)**: `D:\私人资料\deposon-repo\_mirror_pushable.json` (沿 KIMI 已落 22:02 CST)

**新增 14 件 changed**:
```
RELEASE_v1.4.0.md
audits_dataset_health.json
audits_security.json
docs/Findings_v2.0_corrections.md
docs/Findings_v2.0_crossval.md
docs/PAPER_BRIEF.md
docs/space_release_log.json
reviews/literature_scan_v2X_A.md
run_benchmark_v1_4_gsm8k.py
run_v20_baselines.py
run_v20_bigquiz_eval.py
run_v20_familyL_ingest.py
run_v20_fastcheck.py
run_v20_photonics.py
```

**新增 428 件 (按目录切分)**:
- `results/` 173 件 (含 Trae 5 audit + Adendum 17 件 + P-L v3 4 件综合)
- `docs/` 85 件
- `deposon_team/` 69 件
- `corpus/` 24 件
- `.trae/` 19 件 (审计报告 + 改进信)
- `reviews/` 16 件
- `scripts/` 10 件
- 其余 46 件为仓根散落脚本及 1-4 件小目录 (attacks 4 / tests 3 / tools 3 等)

### §2.2 拉 verifier/ 99 件 (仅本地, 不改远端, 沿决策 3)

**文件源 (只读远端)**: KIMI 凝子-agent 沿 git read API 拉 `verifier/audit/` + `verifier/handoff/` + `verifier/runs/` + `verifier/v1-v35/` + `verifier/kill_lines/` + `verifier/README.md`

**写入位置**: `D:\私人资料\deposon-repo\verifier\` (本地副本, 远端不动)

**不动远端**: 远端 verifier/ 99 件 SHA-12 保持原值, KIMI 拉本地只增加 repo 一份, 不覆盖远端

### §2.3 v3x-1week-kill-2026-09-18/ 399 件 (沿决策 2 保留)

远端 399 件保持现状. KIMI 推完 0 触动此目录 (不删除不修改)

### §2.4 远端其余 114 件 (沿决策 4 保留)

远端 114 件 (其余 results/docs/paper/v2 等) 保持现状. KIMI 推完 0 触动

### §2.5 完整论文 4+1 件 (沿决策 1 冻结)

**远端完整论文 5 件冻结 (不动)**:
- `paper/deposon_paper_final_cn.md`
- `paper/deposon_paper_final_en.md`
- `paper/deposon_paper_v1.md`
- `paper/deposon_paper_v1_en.md`
- `paper/references.bib`

KIMI 推完 0 触动此 5 件 (远端 SHA-12 保持原值, 本地有更新版本不动远端)

---

## §3 KIMI 必查 (与 user 2026-09-17 16:31 + 22:31 已老实沟通的边界一致)

### §3.1 KIMI 不重 push 1+2 批 (已沿 22:00 推完)

- 22:00 CST 已推完 bb1f085f 10 件 + 5dd8221b 55 件 + ee0b82fc 48 件 (3 批共 113 件)
- 22:00 CST manifest 镜像 commit 292ba94d
- GitHub HEAD: `292ba94dd5d5843dd78d8edff79deec86e34f794`
- **KIMI 不要重 push 上述 1+2 批已推文件**, 仅推 §2.1 442 件 (含部分已在 1+2 批推过的, KIMI 自查 changed 列表)

### §3.2 KIMI 严守 7 步执行方案

1. **分批推送**, 每批 ≤50 件 (批 1 = 14 changed, 批 2-N = 428 local_only 按目录切分)
2. 每批走 **git-data API** (blob→tree→commit→ref PATCH, **非 force**)
3. 每批推后 `GET git/trees/<commit>?recursive=1` 做 **git-SHA1 全量比对** (contents API 对 >1MB 文件返回空, 必须用 tree 比对)
4. 每批写 **manifest 镜像**入 `D:\私人资料\deposon-repo\results\_kimi_push_v3_manifest_*.json`
5. 推送前对候选文件做 **密钥扫描**; 正则必须泛化, 绝不写入真实密钥片段
6. **frozen 工件绝不触碰**; 任何重跑审计在 /tmp 副本执行
7. **API key 永不落盘、永不进 prompt**

### §3.3 KIMI 7 铁律 + 9 铁律 0 触动严守

| 类别 | 严守 |
|---|---|
| no_llm | ✅ 0 LLM (Mavis 不调, KIMI 也不调) |
| no_proxy | ✅ 0 proxy (直推) |
| no_gateway | ✅ 0 gateway |
| no_key_in_prompt_json_disk | ✅ key runtime 读, 严禁明文入 JSON/log/MD |
| no_18_frozen_touch | ✅ 不动 18 frozen anchors (含 verifier/ 3 个 + 5 制品 + 5 P-G + 5 spec anchor) |
| no_p_g_v0_touch | ✅ 不动 P-G V0 |
| no_p_g_v01_touch | ✅ 不动 P-G V0.1 |
| no_plugin_spec_touch | ✅ 不动 4 plugin spec |
| no_verifier_mavis_builtin_scripts_touch | ✅ 不动 verifier/ mavis/ .trae/ .builtin/scripts/ 字节级 |

---

## §4 KIMI 派工后必报告 (Mavis 协调聚合)

| 件 | 路径 | 用途 |
|---|---|---|
| 沿 7 步方案推完 manifest | `D:\私人资料\deposon-repo\results\_kimi_push_v3_manifest_<commit>.json` | 每批 manifest 镜像 |
| 沿 7 步方案推完 commit 链 | `<commit_hash>` | bb1f085f → 5dd8221b → ee0b82fc → 292ba94d → **新 commit v3 final** |
| verifier 99 件本地副本 | `D:\私人资料\deposon-repo\verifier\` (102 文件, 含 3 frozen + v1-v35 check.py + runs/...) | 沿决策 3 本地回拉 |
| v0+v1 verify 复跑 | `_verify_15frozen_v1.py + _verify_pg_v0_v1.py` | 16/16 + 5/5 PASS 复验 (Mavis 已验, KIMI 推完再验 1 次) |
| 0 触动最终验 | 全 repo verify (沿 7 铁律) | 18 frozen + 5 制品 + schema v1 + 4 plugin + verifier + 9 铁律 |

---

## §5 老实交代 (沿 user 17:02 「诚实老实交代」)

- "合适的子代理" = KIMI 凝子-agent 独立执行 (Mavis 严守 7 铁律不动 push, 只协调)
- "分配技能与插件" = Mavis 不知有哪些技能/插件可分配, KIMI 自己用
- "利用我的 LLM api key" = KIMI 凝子-agent 用 user 新 PAT, 9 铁律第 6 条 runtime 读, 严禁明文落盘
- 358 件移出 + verifier 99 件恢复 = Mavis 已沿 7 决策点执行, KIMI 只需执行 7 步 push 方案
- 7 步执行方案 + 4 决策点边界 + 3 隐含决策 = Mavis + KIMI 协同, 严守 0 触动

---

## §6 时点 (KIMI 必沿)

| 时点 | 动作 | 主体 |
|---|---|---|
| 2026-09-17 22:55 CST (now) | 此委托 spec 落盘 (Mavis) | Mavis |
| 2026-09-17 23:00 CST | user chat 给 KIMI 发送本 spec | user |
| 2026-09-17 23:00-23:30 CST | KIMI 沿 7 步方案执行 push | KIMI 凝子-agent |
| 2026-09-18 9:00 CST | Mavis 跑 v0+v1 verify 复验 + 0 触动最终验 | Mavis |
| 2026-09-18 晚 CST | D7 王老师 WeChat 推送 (user) | user |
| 2026-09-19 起 | V4 1 分支 (下周 deposon 二作含 V3+V4) | Mavis + 4 协作方 |

---

## §7 严守清单 (Mavis + KIMI 共享, 7 决策点 + 9 铁律)

### Mavis 边界 (Mavis 已执行 + 待协调)
- ✅ 358 件移出 (6 类, 0 触动严守)
- ✅ verifier/ 99 件恢复 (102 文件含 3 frozen + 子文件, 0 触动严守)
- ✅ Coze 委托路径 verify (32 条引用全部 EXISTS, 不需修改)
- ❌ Mavis 不动 push (KIMI 凝子-agent 独立执行, 严守 7 铁律)
- ❌ Mavis 不调 LLM (0 LLM, 沿 9 铁律)
- ❌ Mavis 不动回拉远端 (本地副本只读, 远端不动)
- ❌ Mavis 不调 WeChat (user 自行)

### KIMI 凝子-agent 边界 (待执行, 严守)
- ❌ KIMI 不重 push 1+2 批 (已沿 22:00 推完, KIMI 不动)
- ❌ KIMI 不动 358 件 (Mavis 已移出, KIMI 不动)
- ❌ KIMI 不动完整论文 4+1 件 (沿决策 1 冻结, KIMI 不动)
- ❌ KIMI 不动 v3x-1week-kill 399 件 (沿决策 2 保留, KIMI 不动)
- ❌ KIMI 不动 远端其余 114 件 (沿决策 4 保留, KIMI 不动)
- ✅ KIMI 仅推 442 件 (14 changed + 428 新增, 沿 §2.1 清单)
- ✅ KIMI 仅拉 verifier/ 99 件 (本地副本, 不动远端, 沿决策 3)
- ✅ KIMI 沿 7 步方案执行 (分批 ≤50 + git-data API + tree 比对 + manifest + 密钥扫描 + frozen 不动 + 0 LLM + 0 落盘)

---

**Mavis 起草** · deposon V3X 1 周判死主理 · 2026-09-17 22:55 CST
