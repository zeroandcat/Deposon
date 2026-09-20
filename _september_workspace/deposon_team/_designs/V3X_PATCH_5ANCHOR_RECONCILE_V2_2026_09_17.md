# V3X PATCH 5 ANCHOR RECONCILE V2 (2026-09-17, B2.2 task)
## deposon V3X 1 周判死 D7 前 schema 重设计 reconcile

**Author**: Mavis (B2.2 task, user 23:21 拍板)
**Date**: 2026-09-17 (Thu) 10:32 CST
**Trigger**: User 拍板 B2.2 (全 schema 重设计 + 完整 reconcile 流程)

---

## 0. 背景

v0 schema 在 2026-09-15 锁死 (Trae 修复点 6)。冻结 16 frozen anchors + 5 P-G anchors = 18 frozen 总数。

2026-09-17 file trim (本 repo 1,327 → 817 files) 导致：
- `verifier/` 整体移 archive 25% (含 18 frozen 锚中的 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` + `verifier/handoff/P_F_PREDECISION_2026_09_09.json`)
- `results/deposon_v19_benchmark_fixes.json` 在 R5 误移至 archive（已 restore）

为此重设计 schema v1:
- 16 frozen + 5 P-G 锚定
- 加 `path_fallback` 字段（repo → archive 自动降级）
- 加 `anchor_type` 分类（spec / benchmark / corpus / plugin / anchor_json）
- 加 `touched_history` 字段记录 2026-09-17 file trim 后的位移

---

## 1. Schema v0 vs v1 diff

| 字段 | v0 (Python tuple) | v1 (JSON) |
|---|---|---|
| 格式 | `(rel, sha12, name)` tuple 硬编码 | 单一 `_v3x_frozen_schema_v1.json` 文件 |
| fallback | 无 | 自动 repo → archive fallback |
| 类型分类 | 无 | `anchor_type` 5 类 |
| Touched history | 注释硬编码 | `touched_history` 字段可扩展 |
| 文档化 | 16 frozen 名字混在 .py 注释 | JSON schema + PATCH 文档 |

---

## 2. 16 frozen anchors v0 → v1

| ID | expected_sha12 | path_primary | path_fallback | type | touched_history |
|---|---|---|---|---|---|
| KT_ABC1_anchors_sha256_12 | 03c6c01f3697 | verifier/handoff/KT_ABC1_anchors_sha256_12.json | archive/verifier/handoff/KT_ABC1_anchors_sha256_12.json | anchor_json | 整体挪 verifier/ → archive; 16 frozen 锚 |
| KT_A1_SPEC_V0_1 | 78b71d404366 | docs/V3X/KT_A1_SPEC_V0.1.md | (在 repo) | spec | 无 |
| KT_B1_SPEC_V0_1 | 0410ca0fbdae | docs/V3X/KT_B1_SPEC_V0.1.md | (在 repo) | spec | 无 |
| KT_C1_SPEC_V0_1 | 59d8f56347d5 | docs/V3X/KT_C1_SPEC_V0.1.md | (在 repo) | spec | 无 |
| KT_D0_SPEC_V0_1 | cce8e9a1b00e | docs/V3X/KT_D0_SPEC_V0.1.md | (在 repo) | spec | 无 |
| P_F_V0_1_UPGRADE_2026_09_11 | b10fae0da66d | docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md | (在 repo) | spec | 无 |
| v19_benchmark_fixes | 910c4333eead | results/deposon_v19_benchmark_fixes.json | (restore 自 R5 archive) | benchmark | R5 误移 archive → restore 真 anchor |
| v21_gtformal | 9d9ae5001c57 | results/deposon_v21_gtformal.json | (在 repo) | benchmark | 无 |
| corpus_v20_index | 8423ffe266af | corpus/v20/index.json | (在 repo) | corpus | 无 |
| P_F_PREDECISION_2026_09_09 | b41c98bf90cc | verifier/handoff/P_F_PREDECISION_2026_09_09.json | archive/verifier/handoff/P_F_PREDECISION_2026_09_09.json | anchor_json | 整体挪 verifier/ → archive |
| P_F_SPEC_V0 | de90faf362c5 | docs/V3X/P_F_SPEC_V0.md | (在 repo) | spec | 无 |
| P_F_RESEARCH_2026_09_09 | 98085df7811a | docs/V3X/P_F_RESEARCH_2026_09_09.md | (在 repo) | spec | 无 |
| plugin_a_skill_a_p_a_60cells | b1463bb24403 | deposon_team/plugins/skill_a_p_a_60cells.py | (在 repo) | plugin | 无 |
| plugin_b_skill_b_p_c_alpha_beta | e5a299f69a22 | deposon_team/plugins/skill_b_p_c_alpha_beta.py | (在 repo) | plugin | 无 |
| plugin_c_skill_c_p_e_3modality | e19e76c5da7e | deposon_team/plugins/skill_c_p_e_3modality.py | (在 repo) | plugin | 无 |
| plugin_d_skill_d_p_f_observer | 3e369a1f6171 | deposon_team/plugins/skill_d_p_f_observer.py | (在 repo) | plugin | 无 |

**SHA-12 值不变**：v0 → v1 仅 format 变, 16 文件内容未触动。

---

## 3. 5 P-G anchors v0 → v1

| ANCHOR_ID | placeholder | recomputed_seed (v0 → v1 算法) |
|---|---|---|
| P_G_HYPERBOLIC_TRANSPORT | 230b5caee415 | `P_G_V0_PLACEHOLDER_{id}_2026_09_15` SHA-256[:12] |
| P_G_CURVATURE_BOUND | dcbcf2b8d45f | 同 |
| P_G_LLM_CLIENT | 2c1f572aa2bf | 同 |
| P_G_HARNESS | 8b90c53f1e01 | 同 |
| P_G_FROZEN_BENCHMARK | 91db66afecc3 | 同 |

**P-G placeholder 值不变**：v0 → v1 算法相同 (R3 erratum)。

---

## 4. Reconciliation flow

```
v0 verify script (_verify_15frozen.py + _verify_pg_v0.py)
  ↓ file trim (verifier/ → archive)
  ↓ patch: add resolve() repo → archive fallback
  ↓ verify OK 16/16 + 5/5 P-G
  ↓
v1 schema design (B2.2 task, 2026-09-17)
  ↓ extract 16 anchors to JSON with metadata
  ↓ add path_fallback, anchor_type, touched_history fields
  ↓ write _v3x_frozen_schema_v1.json (12,919 B)
  ↓ write _verify_15frozen_v1.py + _verify_pg_v0_v1.py
  ↓
v0 + v1 dual verify
  ↓ v0 still PASS (backward compat)
  ↓ v1 PASS (new schema-driven)
  ↓
PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md (this doc)
  ↓
Q3 reconcile done (V2)
  ↓ Ready for D7 王老师 WeChat push
  ↓ KIMI 凝子-agent GitHub upload
```

---

## 5. 文件清单

### 产出 (新增)
- `deposon_team/plugins/_v3x_frozen_schema_v1.json` (12,919 B) - schema v1 定义
- `deposon_team/plugins/_verify_15frozen_v1.py` (~2.5 KB) - 16 frozen v1 verify
- `deposon_team/plugins/_verify_pg_v0_v1.py` (~3 KB) - 16 frozen + 5 P-G v1 verify
- `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` (this file)

### 不变 (保留 v0)
- `deposon_team/plugins/_verify_15frozen.py` (v0 patched with archive fallback)
- `deposon_team/plugins/_verify_pg_v0.py` (v0 patched with archive fallback)
- `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md` (Q2 reconcile)

### Archive 备份
- `_archive_deposon_2026_09_17/verify_archive_backup/_verify_15frozen.py` (3883 B, 原版)
- `_archive_deposon_2026_09_17/verify_archive_backup/_verify_pg_v0.py` (4172 B, 原版)
- `_archive_deposon_2026_09_17/results/_v3x_conservation_anchor_2026_09_17.txt` (D fix stub)

---

## 6. 边界 / 不变量

### 0 触动声明
v0 16 frozen + 5 P-G anchors (18 总) SHA-256[12] 值**未变**。仅 format 升级 Python tuple → JSON。

### 文件守恒
1 个 schema JSON (12,919 B) + 2 个 v1 verify script (~5.5 KB) + 1 个本 PATCH 文档 = ~20 KB 新增
预计 file count: 817 → 820-821 (在 < 1000 阈值内)

### Iron 7 兼容
- ✓ no_llm
- ✓ no_proxy
- ✓ no_gateway
- ✓ no_key_in_prompt_json_disk
- ✓ no_18_frozen_touch (SHA values unchanged)
- ✓ no_p_g_v0_touch
- ✓ no_p_g_v01_touch
- ✓ no_plugin_spec_touch (4 plugin scripts unchanged)
- ✓ no_verifier_mavis_builtin_scripts_touch (B fix keeps .mavis/ in archive)

---

## 8. D7 推送 RAG path

minerax 凝子-agent 负责:
1. `git init` (当前不是 git 仓库)
2. `git add .` (含 by_model/ + v1 schema + v1 verify + PATCH V2)
3. `git commit` (按 `deposon_team/plugins/git_commit_msg_2026_09_18.txt`)
4. `git push` (user 提供新 PAT, 旧 `ghp_[REDACTED]` 已吊销)

---

**Mavis 起草**
**deposon V3X 1 周判死主理**
**2026-09-17 10:32 CST**
