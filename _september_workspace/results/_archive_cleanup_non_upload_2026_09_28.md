# 归档区处置棒 · 清理/转移/manifest 登记件（2026-09-28）

- **棒**：deposon V4 归档区处置棒 · worker（出证 = worker，未冒名他方）
- **授权**：PI 拍板 `ask_ddebd3637cef1fe364ee6fe7`（2026-09-28 18:34）· 归档区承接转移 + 清垃圾，**前置 = 重生成追踪 manifest**
- **整理三口径**（同轮生效）：简写点名＝已点名禁转移／**可复算性优先**／manifest `sha12` 小写（09-21 先例为 UPPERCASE，差异并记）
- **处置面**：`D:/私人资料/_non_upload_local_archive/`（1,696 件 · 338,433,933 B · 322.76 MiB）
- **两件产物**：
  1. `results/_archive_manifest_non_upload_v2_2026_09_28.json` · 236,651 B · SHA-12 `84eef669234b`
  2. `results/_archive_cleanup_non_upload_2026_09_28.md`（本件）

---

## 1. 第 1 动作 · manifest v2 重生成

| 项 | 实况 |
|---|---|
| 生成器 | `_gen_manifest_v2.py`（收尾时随中间件清走，不留盘；重生成＝对该目录做一次 `sha256(data).hexdigest()[:12]` 全量 walk） |
| schema | 沿 2026-09-23（`generated_at`/`source_dir`/`file_count`/`files[{path,size,sha12}]`）＋新增 `diff_vs_2026_09_23` 对账节 ＋ `hash_rule`/`supersedes`/`generated_by` |
| 哈希口径 | `hashlib.sha256(data).hexdigest()[:12]`，**全部小写**（实测 `all(sha12 == sha12.lower()) == True`，1,630/1,630） |
| 行尾 | CRLF（与旧 manifest 一致） |
| 清理前态 | 1,696 件 · 338,433,933 B · 同名件 SHA-12 `ef951928bdb2`（本棒内被后写的清理后态覆写，故在此登记留痕） |
| 清理后态（**终版**） | **1,630 件 · 337,169,408 B · SHA-12 `84eef669234b`** |
| 旧件 `results/_archive_manifest_non_upload_2026_09_23.json` | **0 覆盖 0 回改**：收尾复测 SHA-12 `b899103853ca` · 148,690 B（与开棒首测同值） |

### 1.1 旧/新差异对账（v2 `diff_vs_2026_09_23` 节实测）

| 口径 | 件数 | 说明 |
|---|---:|---|
| 旧 manifest 登记 | 1,176 | 2026-09-23 快照 |
| 新 manifest 实测 | 1,630 | 2026-09-28 清理后态 |
| **新增**（旧无、盘有） | 517 | 2026-09-23 之后落入归档区者 |
| **移除**（旧有、盘无） | 63 | 其中 **63 件**＝旧 manifest 在册、本棒清走；另 **3 件**（`scripts/scripts/kt_b1/__pycache__/boss_b1_sinkhorn_ot|boss_b2_kd|boss_b3_llmlingua.cpython-314.pyc`）旧 manifest 未在册，故净表现为「新增即清走」，不进 `removed[]` |
| 内容变更 | 0 | 同名同尺但哈希不同者 **0** |
| 未变 | 1,113 | 旧 1,176 件逐件 size+sha12 全等 |
| 本棒清走全账 | 66 | v2 内 `removed_this_run_by_worker` 节逐件登记 path/size/sha12/理由，可完整回溯 |

**新旧大小写差异实测结论**：旧 `_archive_manifest_non_upload_2026_09_23.json` 内 `sha12` **0 处 UPPERCASE**（实测统计），故本 manifest 与旧件**无大小写差异需并记**；大小写差异仅存在于 `deposon-sub/_movedout_manifest_2026_09_21.json`（先例 UPPERCASE 359/363），其消费方仍须 case-fold，本棒未触该件。

---

## 2. 第 2 动作 · 清垃圾（判定口径与实测分类）

**候选池**＝派工单点名三类面：`*.pyc`／`__pycache__`／`cache/`／`logs/`／`tmp/`，实测 **447 件 · 21,302,781 B（20.32 MiB）** —— 与上一棒登记的「可清类合计约 21 MB」量级吻合（那一棒整类粗估，本棒逐件过判据）。

**判定判据（逐件过）**：① 纯派生物可实证（CPython 字节码 magic 检定／0 字节无内容）；② 内容已入权威件（**SHA-256 逐件实测同值**，非同名推断）；③ **0 引用**（对 `deposon-repo` 全仓 `md/txt/json/bib/tex/py/ps1` 共 1,053 件做**全路径字符串**检索）。三条同时满足才进删除集；任一不满足 ⇒ 留＋登记。

| 分类 | 件数 | 字节 | MiB | 处置 |
|---|---:|---:|---:|---|
| **垃圾（清）** | 66 | 1,264,525 | 1.21 | 可恢复删除 |
| 留 · 被权威件按路径点名引用 | 173 | 7,480,071 | 7.13 | 留＋登记（§3） |
| 留 · 无法证明「已入权威件或纯派生」 | 208 | 12,558,185 | 11.98 | 留＋登记（§3） |
| 非候选面（`attacks/`、`deposon_team/`、`paper/`、`corpus/`、`installers/` 等） | 1,249 | 317,131,152 | 302.44 | **0 读 0 写 0 删** |

> **回收量如实报数**：派工单预估「~21MB，以实测为准」；本棒**实际清走 1.21 MiB / 66 件**，占候选池 5.9%。差额主因有二：① **被权威件按路径点名引用**（7.13 MiB，见 §3）；② **无法证明内容已入权威件**（11.98 MiB，多为论文 PDF/HTML 构建产物与逐条编译日志，见 §3）。**未为凑回收量放宽判据。**

### 2.1 删除通道实况

| 项 | 实况 |
|---|---|
| 通道 | 本地 runtime **可恢复删除通道**，工作目录 `cd D:/私人资料/_non_upload_local_archive` 后顶层 `rm -- <相对路径…>`，**相对路径** |
| 运行时回执 | `mavis-trash: moved to trash: '<path>'` **逐件 66 条** |
| 永久删除 / 绕过恢复机制 | **0 / 0**（未用绝对路径删除命令、未用内联脚本删除、未直呼回收站） |
| 批次数 | **6 次顶层 `rm` 调用**：第 1 次列 66 路径，命中执行器 180 s 上限、完成 **11** 件后被超时截断（**非删除失败**）；余 55 件按 12/12/12/12/7 分 5 次顶层调用完成。全部经同一可恢复通道，**无一次改道** |
| 删除后盘上复核 | 66 件逐一 `os.path.exists()` 实测 **0 件在盘**（`still_on_disk = 0`） |
| 回收站可恢复性 | 是（66 件原件在回收站内可取回） |

### 2.2 清走逐件表（66 件 · 1,264,525 B）

| # | 路径 | SHA-12 | 字节 | 分类理由（实测） |
|---:|---|---|---:|---|
| 1 | `attacks/__pycache__/__init__.cpython-314.pyc` | `2cbec07fbd15` | 346 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 2 | `attacks/__pycache__/a1_delete_anchor.cpython-314.pyc` | `cc79fd1a7bd1` | 6,006 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 3 | `attacks/__pycache__/a2_reshuffle_manifest.cpython-314.pyc` | `c795f62c5fe6` | 5,322 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 4 | `attacks/__pycache__/a3_rewrite_runs.cpython-314.pyc` | `ea9fdec849ba` | 5,329 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 5 | `cache/cache/__pycache__/_add_preprint_meta.cpython-312.pyc` | `08f6c2b4aaa9` | 5,786 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 6 | `cache/cache/__pycache__/_arxiv_renumber.cpython-312.pyc` | `18a5f56ca32f` | 19,967 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 7 | `cache/cache/__pycache__/_md_to_tex.cpython-310.pyc` | `8215a4ecb2fc` | 33,728 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 8 | `deposon_team/plugins/__pycache__/attack_pc_a1_resampling.cpython-314.pyc` | `8b3ae6111a86` | 6,597 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 9 | `deposon_team/plugins/__pycache__/attack_pc_a2_fitting.cpython-314.pyc` | `9e5e8c6375e1` | 6,116 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 10 | `deposon_team/plugins/__pycache__/attack_pc_a3_clipping.cpython-314.pyc` | `db7d7cffa43c` | 5,985 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 11 | `deposon_team/plugins/__pycache__/boss_pa_2_potential_game.cpython-314.pyc` | `77ba1d38610a` | 11,613 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 12 | `deposon_team/plugins/__pycache__/boss_pc_1_2d_ising_universality.cpython-314.pyc` | `a7e97b33f046` | 8,973 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 13 | `deposon_team/plugins/__pycache__/boss_pc_2_transverse_field_ising.cpython-314.pyc` | `aa214de50a33` | 8,855 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 14 | `deposon_team/plugins/__pycache__/boss_pc_3_reservoir_computing.cpython-314.pyc` | `a538264cb432` | 10,135 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 15 | `deposon_team/plugins/__pycache__/boss_pg_1_riemannian_degenerate.cpython-314.pyc` | `a0f40d7122f8` | 5,724 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 16 | `deposon_team/plugins/__pycache__/boss_pg_2_hyperbolic_classification_collapse.cpython-314.pyc` | `7c50f1267ce9` | 5,304 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 17 | `deposon_team/plugins/__pycache__/boss_pg_3_geodesic_violation.cpython-314.pyc` | `b20a21dcb7e1` | 5,402 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 18 | `deposon_team/verifier/__pycache__/v42_v2_2026_09_16.cpython-312.pyc` | `8427e22d3054` | 18,376 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 19 | `scripts/__pycache__/volcengine_7model_smoke_2026_09_10.cpython-314.pyc` | `a7f430b9bf9e` | 12,898 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 20 | `scripts/scripts/__pycache__/migrate_history.cpython-314.pyc` | `ecedcd29dfe4` | 8,088 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 21 | `scripts/scripts/kt_b1/__pycache__/attacker.cpython-312.pyc` | `98a023430d94` | 11,793 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 22 | `scripts/scripts/kt_b1/__pycache__/attacker.cpython-314.pyc` | `08d23c1c3c6d` | 13,887 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 23 | `scripts/scripts/kt_b1/__pycache__/boss_b1_sinkhorn_ot.cpython-314.pyc` | `3738cacf6dc2` | 20,607 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 24 | `scripts/scripts/kt_b1/__pycache__/boss_b2_kd.cpython-314.pyc` | `3370166faed5` | 19,562 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 25 | `scripts/scripts/kt_b1/__pycache__/boss_b3_llmlingua.cpython-314.pyc` | `53ed1e7fef35` | 18,743 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 26 | `scripts/scripts/kt_b1/__pycache__/harness.cpython-312.pyc` | `8a2a13044fd1` | 9,349 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 27 | `scripts/scripts/kt_b1/__pycache__/harness.cpython-314.pyc` | `3e61e3d164de` | 10,247 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 28 | `scripts/scripts/kt_c1/__pycache__/boss_c1_2d_ising.cpython-314.pyc` | `c799a9f063f8` | 5,890 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 29 | `scripts/scripts/kt_c1/__pycache__/boss_c2_transverse_ising.cpython-314.pyc` | `7ee56beea67a` | 3,131 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 30 | `scripts/scripts/kt_c1/__pycache__/boss_c3_reservoir.cpython-314.pyc` | `fcc6aca3e7e5` | 4,911 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 31 | `scripts/scripts/kt_c1/__pycache__/eta_scan.cpython-314.pyc` | `e7e182208591` | 3,236 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 32 | `scripts/scripts/kt_c1/__pycache__/harness.cpython-314.pyc` | `e3f782d2e29c` | 3,628 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 33 | `scripts/scripts/kt_c1/__pycache__/kt_c1_loglog_fit.cpython-314.pyc` | `6c45c391b85c` | 8,129 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 34 | `tests/__pycache__/test_agents_merge.cpython-312-pytest-9.1.1.pyc` | `6ba5305e9cd2` | 80,864 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 35 | `tests/__pycache__/test_diffusion.cpython-312-pytest-9.1.1.pyc` | `73c4c2b145d3` | 29,193 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 36 | `tests/__pycache__/test_fast.cpython-312-pytest-9.1.1.pyc` | `2196d062e218` | 9,381 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 37 | `tests/__pycache__/test_fingerprint_v0.cpython-312-pytest-9.1.1.pyc` | `c893e7943a1e` | 29,437 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 38 | `tests/__pycache__/test_gt_common.cpython-312-pytest-9.1.1.pyc` | `20d0cec322ad` | 28,928 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 39 | `tests/__pycache__/test_llm_fetch.cpython-312-pytest-9.1.1.pyc` | `cf2cf16abe83` | 68,373 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 40 | `tests/__pycache__/test_llm_prior.cpython-312-pytest-9.1.1.pyc` | `f8b0be5d03d4` | 29,600 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 41 | `tests/__pycache__/test_new_modes.cpython-312-pytest-9.1.1.pyc` | `092af160f0ea` | 64,939 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 42 | `tests/__pycache__/test_protocol.cpython-312-pytest-9.1.1.pyc` | `b8284e86d212` | 45,159 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 43 | `tests/__pycache__/test_v18.cpython-312-pytest-9.1.1.pyc` | `460ccb73678c` | 77,923 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 44 | `tests/__pycache__/test_v19.cpython-312-pytest-9.1.1.pyc` | `3bec19faf294` | 30,286 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 45 | `tests/__pycache__/test_v19_benchmark.cpython-312-pytest-9.1.1.pyc` | `16046a2b2487` | 29,106 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 46 | `tests/__pycache__/test_v20.cpython-312-pytest-9.1.1.pyc` | `0bcc85d6cdb0` | 70,178 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 47 | `tests/__pycache__/test_v20_gt2b.cpython-312-pytest-9.1.1.pyc` | `041265ae43b9` | 18,804 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 48 | `tests/__pycache__/test_v20_gt5.cpython-312-pytest-9.1.1.pyc` | `64c29f5ef056` | 20,853 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 49 | `tests/__pycache__/test_v20_gt5b.cpython-312-pytest-9.1.1.pyc` | `74b6e31e85d6` | 10,701 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 50 | `tests/__pycache__/test_v20_gt6.cpython-312-pytest-9.1.1.pyc` | `70dd604090c6` | 15,854 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 51 | `tests/__pycache__/test_v20_gt7.cpython-312-pytest-9.1.1.pyc` | `e7f1c6aa4205` | 23,708 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 52 | `tests/__pycache__/test_v20_gt8.cpython-312-pytest-9.1.1.pyc` | `0bfca62d572b` | 25,830 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 53 | `tests/__pycache__/test_v20_gt8b.cpython-312-pytest-9.1.1.pyc` | `bf190de9f990` | 38,034 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 54 | `tests/__pycache__/test_v20_gt8c.cpython-312-pytest-9.1.1.pyc` | `2788c7c7140c` | 54,744 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 55 | `tests/__pycache__/test_v21_gtformal.cpython-312-pytest-9.1.1.pyc` | `53e41ab7216c` | 33,336 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 56 | `tests/__pycache__/test_v22_p1c.cpython-312-pytest-9.1.1.pyc` | `f9b00fba22f4` | 20,204 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 57 | `tmp/__pycache__/fingerprint_v0.cpython-314.pyc` | `7f5e43c720a6` | 11,253 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 58 | `tmp/__pycache__/volcengine_glm_latest_30cells_v2_runner_2026_09_10.cpython-314.pyc` | `1326f367148b` | 25,859 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 59 | `tools/__pycache__/exp_harness.cpython-312.pyc` | `f4e13105e9d7` | 13,390 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 60 | `tools/__pycache__/exp_harness.cpython-314.pyc` | `fd93ed6c190f` | 15,163 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 61 | `tools/__pycache__/llm_client.cpython-312.pyc` | `513165e4919d` | 9,902 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 62 | `tools/__pycache__/llm_client.cpython-314.pyc` | `8bbd97deb3ba` | 9,860 | **A 字节码派生物**：文件头为 CPython magic（`cb0d0d0a`=3.12 / `2b0e0d0a`=3.14 / `6f0d0d0a`=3.10，与文件名 tag 一致）；**0 引用**（全仓 1,053 件检索 0 命中） |
| 63 | `logs/logs/_check_en_content.log` | `e3b0c44298fc` | 0 | **E 0 字节空件**（SHA-12 `e3b0c44298fc`＝空内容哈希）：无内容、无证据价值、**0 引用** |
| 64 | `logs/logs/_md2tex4.log` | `e3b0c44298fc` | 0 | **E 0 字节空件**（SHA-12 `e3b0c44298fc`＝空内容哈希）：无内容、无证据价值、**0 引用** |
| 65 | `logs/logs/_pdf_verify.log` | `e3b0c44298fc` | 0 | **E 0 字节空件**（SHA-12 `e3b0c44298fc`＝空内容哈希）：无内容、无证据价值、**0 引用** |
| 66 | `logs/logs/_renumber2.log` | `e3b0c44298fc` | 0 | **E 0 字节空件**（SHA-12 `e3b0c44298fc`＝空内容哈希）：无内容、无证据价值、**0 引用** |

> **口径依据**：`.pyc`＝环境派生物（项目内既有口径见 `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md:515`「`.pyc` 是被只读 import 的副产物…环境派生物，非产物件、非派生 JSON、非证据」；同件 516 行建议「（甲）随件清理，走可恢复删除通道并登记清理条目」）；本棒亦实测 **62/66** 件的同名 `.py` 源可在 `deposon-repo/` 或 `deposon-sub/` 找到，余 4 件为「源不在本归档区」的孤儿字节码（归档区只搬进了 `__pycache__` 未搬 `.py`），如实登记、不假称有源。

---

## 3. 留痕登记（未清件及理由）

### 3.1 被权威件按路径点名引用 → 173 件 · 7,480,071 B（7.13 MiB）

| 引用件（`deposon-repo/`） | 引用条数 | 字节 | 引用性质 |
|---|---:|---:|---|
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 166 | 7,418,324 | **清单式**：三目录盘点表，逐件列 `path · sha12 · 字节 · IN-EFFECT` |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 5 | 28,343 | **证据式**：以 `sha12` 为键判定「幽灵引用/双区同名」 |
| `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 2 | 33,404 | **清理台账式**：记录同名 `.pyc` 已在**主仓**被 `mavis-trash` 清走 |

| 留痕面 | 件数 | 字节 |
|---|---:|---:|
| `.pyc`（被引用者留） | 7 | 61,747 |
| `cache/cache/` | 78 | 7,417,428 |
| `logs/logs/` | 84 | 0 |
| `tmp/.pytest_cache/` | 4 | 896 |

明细（逐件）：

| 路径 | SHA-12 | 字节 | 引用出处 |
|---|---|---:|---|
| `__pycache__/fingerprint_v0.cpython-312.pyc` | `be6528f29c19` | 9,586 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig1_boundary_map_cn.png` | `cc1067863adc` | 360,334 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig1_boundary_map_en.png` | `921ea0ea7637` | 360,057 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig2_killsign_scatter_cn.png` | `239b1411d3dd` | 259,257 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig2_killsign_scatter_en.png` | `02d70bb1bd2c` | 248,010 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig3_division_scatter_cn.png` | `66c805d0d97a` | 286,354 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig3_division_scatter_en.png` | `a848305eefe7` | 278,252 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig4_gt7_frontier_cn.png` | `22af20586904` | 564,880 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig4_gt7_frontier_en.png` | `2d6d935fb369` | 542,421 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig5_poa_distribution_cn.png` | `b98338c10913` | 443,481 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/deposon_arxiv_2026/figures/fig5_poa_distribution_en.png` | `decfbd34d9ed` | 442,102 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/auto-render.min.js` | `e5372d199bcd` | 3,486 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fig1_architecture.png` | `565e2bf0ad14` | 237,230 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fig1_architecture_en.png` | `2c50ac66e20f` | 358,536 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.ttf` | `68534840bcfd` | 63,632 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.woff` | `30da91e84c89` | 33,516 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.woff2` | `0cdd387c9590` | 28,076 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.ttf` | `07d8e303ce4f` | 12,368 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.woff` | `1ae6bd747559` | 7,716 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.woff2` | `de7701e42cf1` | 6,912 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.ttf` | `ed0b74372fee` | 12,344 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.woff` | `3398dd023025` | 7,656 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.woff2` | `5d53e70ad607` | 6,908 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.ttf` | `9163df9c7122` | 19,584 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.woff` | `9be7ceb88004` | 13,296 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.woff2` | `74444efd593c` | 11,348 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.ttf` | `1e6f9579e90e` | 19,572 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.woff` | `5e28753be717` | 13,208 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.woff2` | `51814d270d06` | 11,316 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.ttf` | `138ac28d1663` | 51,336 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.woff` | `c76c5d696297` | 29,912 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.woff2` | `0f60d1b89793` | 25,324 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.ttf` | `70ee1f64a20f` | 32,968 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.woff` | `a6f7ec0d846a` | 19,412 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.woff2` | `99cd42a3c072` | 16,780 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.ttf` | `0d85ae7cc30f` | 33,580 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.woff` | `f1d6ef86f3b1` | 19,676 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.woff2` | `97479ca6cce9` | 16,988 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.ttf` | `d0332f528683` | 53,580 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.woff` | `c6368d87e8a1` | 30,772 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.woff2` | `c2342cd8b869` | 26,272 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.ttf` | `f9377ab0271c` | 31,196 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.woff` | `850c0af5c223` | 18,668 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.woff2` | `dc47344dbb6c` | 16,400 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.ttf` | `08ce98e51b04` | 31,308 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.woff` | `8a8d24458137` | 18,748 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.woff2` | `7af58c5ec8f1` | 16,440 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.ttf` | `1ece03f79f95` | 24,504 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.woff` | `ece03cfd83e2` | 14,408 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.woff2` | `e99ae51144bf` | 12,216 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.ttf` | `3931dd81faed` | 22,364 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.woff` | `91ee67500cc0` | 14,112 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.woff2` | `00b26ac825e2` | 12,028 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.ttf` | `f36ea897e19f` | 19,436 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.woff` | `11e4dc8a6471` | 12,316 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.woff2` | `68e8c73ef42a` | 10,344 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.ttf` | `1c67f068fea8` | 16,648 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.woff` | `d96cdf2b3bdd` | 10,588 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.woff2` | `036d4e95149b` | 9,644 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.ttf` | `95b6d2f1a501` | 12,228 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.woff` | `c943cc986384` | 6,496 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.woff2` | `6b47c40166b6` | 5,468 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.ttf` | `a6b2099fb555` | 11,508 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.woff` | `2014c523c321` | 6,188 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.woff2` | `d04c54219f9e` | 5,208 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.ttf` | `500e04d54f0d` | 7,588 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.woff` | `6ab6b62e9b62` | 4,420 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.woff2` | `73d591271b16` | 3,624 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.ttf` | `c647367d1dd4` | 10,364 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.woff` | `99f9c6750b48` | 5,980 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.woff2` | `a4af7d414440` | 4,928 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.ttf` | `f01f3e87d9c6` | 27,556 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.woff` | `e14fed02b1ab` | 16,028 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.woff2` | `71d517d67827` | 13,568 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/katex.min.css` | `0289a02cf451` | 23,827 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/pdfbuild/katex.min.js` | `a29d2961d314` | 272,537 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/rendered_arxiv/test_copy.tar.gz` | `b93889476b89` | 1,639,502 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/v2/outline_v2X.md` | `116d193b1607` | 10,476 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `cache/cache/v2/related_work_v2X.md` | `7fb001add973` | 10,114 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `deposon_team/plugins/__pycache__/boss_pa_1_rbr_rm.cpython-314.pyc` | `b39fa0b9d0ac` | 19,744 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` |
| `deposon_team/plugins/__pycache__/boss_pa_3_replicator_dynamics.cpython-314.pyc` | `7008e1f48f9f` | 13,660 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` |
| `logs/logs/_add_labels.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_add_license.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_check_2026.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_check_abs.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_chrome_cn.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_chrome_en.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_clean.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_compr_qa.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_compr_qa2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_deep.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_deep.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_deep2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_download.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_final.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_final2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_final3.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_final5.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_final_render.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_finalize.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_cut.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_miktex.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_overflow.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_overflow2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_overfull.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_pdflatex.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_phrases.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_secs.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_strings.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_wm.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_find_wm.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_all.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn3.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn4.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn5.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn6.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn_fn.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_cn_v2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_en.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_layout.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_layout2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_overflow2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_overflow3.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_texttt.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_texttt2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_fix_v3.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_footnote.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_list_overfull.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_md2tex.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_md2tex2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_md2tex3.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_help.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_help.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_install.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_p3.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_p3.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_portable.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_miktex_portable.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_minor.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_nsis_d.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_nsis_d.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_nsis_help.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_nsis_help.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_pages.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_probe.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_render2026.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_repack_v2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_retest.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_rewrite2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_scan2.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_scan_layout.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_show_after.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_split.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_tinytex_dl.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_tl_dl.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_trace.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_trim.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_try_miktex.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_try_miktex.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_try_tl_perl.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_verify_tex.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_w32tex.log` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `logs/logs/_w32tex.log.err` | `e3b0c44298fc` | 0 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `tmp/.pytest_cache/.gitignore` | `3ed731b65d06` | 37 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `tmp/.pytest_cache/CACHEDIR.TAG` | `37dc88ef9a0a` | 191 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `tmp/.pytest_cache/README.md` | `73fd6fccdd80` | 302 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `tmp/.pytest_cache/v/cache/nodeids` | `8515eeef6a89` | 366 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` |
| `tmp/__pycache__/fingerprint_v0.cpython-312.pyc` | `be6528f29c19` | 9,586 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` |
| `verifier/audit/__pycache__/conservation.cpython-312.pyc` | `67d0806c43dc` | 2,859 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` |
| `verifier/audit/__pycache__/conservation.cpython-314.pyc` | `dc297f4d2cb4` | 3,266 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` |
| `verifier/kill_lines/__pycache__/kt_b1_kill_decision.cpython-314.pyc` | `524639f4c8ec` | 3,046 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` |

### 3.2 无法证明「内容已入权威件或纯派生」→ 208 件 · 12,558,185 B（11.98 MiB）

| 留痕面 | 件数 | 字节 | 未清理由（实测） |
|---|---:|---:|---|
| `cache/cache/rendered_arxiv/` | 46 | 10,779,513 | **逐件 SHA-256 与归档区其余任一件、`deposon-repo/`、`deposon-sub/` 均不同值**（如 `deposon_paper_cn.pdf` 2,600,098 B vs `.trae/audit/compile_evidence/deposon_paper_cn.pdf` 2,591,555 B）⇒ 属**论文产物唯一副本**，按「证据/留痕不清」留 |
| `cache/cache/pdfbuild/` | 4 | 665,527 | 余下 4 件（`v1_cn.html`/`v1_en.html`/`v19_cn.html`/`v19_en.html` 论文 HTML 渲染版），**内容无一与他处同值** ⇒ 留；同目录另 65 件（60 件 `KaTeX_*.ttf/woff/woff2` ＋ `auto-render.min.js`/`katex.min.css/js` ＋ 2 件 `fig1_architecture*.png`）中，前 63 件为**第三方 MIT 资源、可重下**、后 2 件与 `paper/fig1_architecture*.png` **SHA-256 同值**，但**同被 09-24 盘点表按路径引用** ⇒ 一并落 §3.1 留 |
| `cache/cache/deposon_arxiv_2026/` | 3 | 164,851 | 与 `.trae/build/deposon_arxiv_*` **不同版本**的 tex/figures（`deposon_paper_cn.tex` 67,706 B vs 68,987 B）⇒ 另一版论文源唯一副本 |
| `cache/cache/v2/` | 4 | 273,969 | `deposon_paper_v2X{,_en,.converted}.md` ＋ `REVISION_LOG_v2X.md`＝论文正文与修订记录 ⇒ 留 |
| `cache/cache/r0*` | 3 | 12,103 | 渲染探针输出，单件无同值副本 ⇒ 留 |
| `logs/logs/` | 131 | 510,315 | 逐条编译/渲染/校验日志，**内容无一能证明已进入权威件**（与上一棒 `.tmp/` 面同因）⇒ 留 |
| `tmp/` | 17 | 151,907 | `_tmp_volcengine_2026_09_10/` 等 Track2 探针脚本与 cells 输出、V3 frozen 校验脚本 ⇒ 复算脚手架＋证据，留 |

---

## 4. 第 3 动作 · 承接转移

**结论：0 转移**（0 件移入、0 件移出、0 静默移动、0 `_movedout_manifest` 新建）。

| 候选面 | 实测 | 判定 |
|---|---|---|
| `deposon-repo/results/`（517 件 · 24.14 MiB） | 权威判定链/预登记/勘误链所在面 | **0 转移 0 触动**（铁律） |
| `deposon-repo/.scratch_rj5/`（24 件 · 6.62 MiB） | 上一棒登记为**在跑棒目录**（18:10:37 仍被写入），本棒执行期间该目录仍在变动 | 移动即打断在跑棒 ⇒ 留 |
| `deposon-repo/.scratch_gamma_r1/`（30 件 · 2.29 MiB） | 上一棒**明文留痕**目录 | 留 |
| `deposon-repo/.tmp/`（150 件 · 3.84 MiB） | 上一棒已处置（8 件转移 `deposon-sub/tmp_movedout_2026_09_28/`、2 件清走） | 0 追加处置，留 |

派工单第 3 动作字面为「**若有**应转件（非垃圾非主仓核心）」；本棒**未接到点名应转件清单**，且逐面筛选后无一可在不破坏引用/不打断在跑棒的前提下成立 ⇒ 依「拿不准 ⇒ 留＋登记」收口为 **0 转移**，并将该面作为待拍板项列入 §7。

---

## 5. 第 4 动作 · 清单/委托材料同步核与对账表

| 项 | 结论 |
|---|---|
| 旧 manifest `results/_archive_manifest_non_upload_2026_09_23.json` | **0 触动**：收尾复测 SHA-12 `b899103853ca` · 148,690 B（与开棒首测同值） |
| `deposon-repo/results/` 其余既有件 | **0 覆盖 0 回改 0 移 0 删**（本棒仅**新增** 2 件） |
| `deposon-repo/letters/` 委托材料 | **0 变更**。全仓检索 `letters/*.md` 中 `.pyc`/`__pycache__` 共 22 处，**逐处核对全部指向 `deposon-repo/results/…pyc` 等主仓内路径**，无一处指向本棒清走的 66 件归档区路径 ⇒ 委托材料所引路径 **0 失效** |
| 被清 66 件是否被引用 | **0 引用**（对 1,053 件 `md/txt/json/bib/tex/py/ps1` 做全路径字符串检索，66 件命中数 0） |
| 权威件中因本棒而失效的路径 | **0 件**（上一棒曾就 `.tmp/_r1_syntax_check.pyc` 登记过 1 处口径出入；本棒**未产生同类出入**） |
| 需同步改的清单/委托材料 | **0 件** ⇒ 登记「**0 变更**」 |

---

## 6. 铁律遵守表

| 铁律 | 遵守情况 |
|---|---|
| 可恢复删除通道，0 永久删除 0 绕过 | ✅ 6 次顶层 `rm -- <相对路径>`，回执 `mavis-trash: moved to trash` ×66；未用绝对路径删除命令、未用内联脚本删除、未直呼回收站 |
| 旧 manifest 0 覆盖 0 回改 | ✅ 收尾复测 SHA-12 与开棒首测同值 |
| `deposon-repo` 内权威件 0 触动 | ✅ 仅新增 v2 manifest 与本登记件 2 件；`results/`／`letters/`／`verifier/`／`docs/` 0 写 0 移 0 删既有件 |
| SHA-12＝`hashlib.sha256(data).hexdigest()[:12]` 小写 | ✅ 全部哈希 `hashlib` 实测；v2 manifest 1,630/1,630 小写；本登记件表格内 sha12 亦为小写 |
| 宁留勿错删（证据/留痕/唯一副本/被引用件不清；拿不准 ⇒ 留＋登记） | ✅ 候选池 447 件中 **381 件留**（173 被引用 ＋ 208 不可证），仅 66 件三判据同时满足者清走；**未为凑 21 MB 预估放宽判据** |
| 可复算性优先 | ✅ v2 manifest 记 `hash_rule` 全量可复算；本棒清走 66 件**全部**在 `removed_this_run_by_worker` 节留 path/size/sha12，回溯不缺 |
| 署名如实 | ✅ 出证 = worker（session `mvs_899d4f9ad49f4aff8e8fcfe9fd1151c0`）；未冒名 protocol-keeper / verdict-keeper / doc-writer / Trae code 等 |
| 不编造 | ✅ 所有件数/字节/哈希均为盘上实测；预估与实测差额已在 §2 如实交代 |

---

## 7. 待拍板项（穷尽清点 · 本棒 0 自行处置）

1. **清单式引用是否等同「禁清引用」**：173 件 · 7.13 MiB 因被 09-24 三目录盘点表**按路径＋sha12＋字节**逐件登记而留，其中 166 件仅被该盘点表引。若 PI 认定「清单随 v2 manifest 同步更新」即可放行，则可再清约 **7.13 MiB**（并需决定是否新立名件修订那份盘点表）；若维持现口径，则长期留。
2. **0 字节空日志口径不齐**：空日志共 **88 件**，其中 **84 件被盘点表引用**（留）、**4 件未被引用**（本棒已清）。是否统一（全留 or 全清）？
3. **`cache/cache/pdfbuild/` 第三方 KaTeX 资源（63 件 · 1,376,422 B · 1.31 MiB）**：MIT 第三方、可由渲染管线重下，但**既无「已入权威件」实证、又同被 09-24 盘点表按路径引用** ⇒ 双重理由留在 §3.1。若 PI 认定清单式引用可放行且第三方资源可清，则此 63 件可随第 1 项一并清走。同目录另 2 件 `fig1_architecture*.png`（与 `paper/` 下**同值**）同此口径。
4. **`cache/cache/rendered_arxiv/` 论文构建产物（46 件 · 10.28 MiB）**：SHA-256 与他处**均不同值**，属另一版论文 PDF/HTML/TAR 唯一副本。是否确认「论文产物永不入清理面」？
5. **承接转移面 0 转移**：本棒无点名应转件清单，逐面筛选无可安全转移者（§4）。是否需 PI 指定具体应转件清单后再开第 3 动作？

---

## 8. 产物与老实交代

| 项 | 件数 |
|---|---:|
| 落盘产物 | **2**（v2 manifest ＋ 本登记件） |
| 清理删除 | **66 件 · 1,264,525 B（1.21 MiB）**，全部可恢复 |
| 转移 | **0 件** |
| 既有件改动 | **0 件** |
| 中间件 | 扫描/判定 JSON（`_scan_now.json`/`_cand.json`/`_del*.json`/`_ledger.json`/`_repo_scan.json`/`_removed_this_run.json`）与生成器 `_gen_manifest_v2.py`，收尾时经同一可恢复删除通道清走，**不留盘**（重生成 manifest 只需对该目录做一次全量 sha256 walk） |
| 新增待拍板项 | **5**（§7） |

**未完成/受阻事项**：0。本棒四步动作全部落盘并经落盘核验（v2 manifest 收尾复算 1,630 件、逐件 sha12 与盘上实测一致）。

---

出证：**worker**（deposon V4 归档区处置棒 · 2026-09-28）
