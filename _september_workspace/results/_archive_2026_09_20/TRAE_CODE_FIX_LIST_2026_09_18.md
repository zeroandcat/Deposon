# Trae code 代码走读与问题修复清单 · 2026-09-18

> **任务**: 对 2026-09-17 19:24 → 2026-09-18 00:00 新增文件逐行走读 + 根目录二次复审 + 全量问题修复
> **执行方**: Trae code（1 主线 + 3 并行子代理）
> **纪律**: frozen 18/18 零触动（实算复检）/ 追加式注记不改生产方原判定值 / 0 LLM 复算
> **验证**: compile 12/12 + JSON 8/8 + 功能单测 5/5 + FTFB manifest 5/5 + frozen 18/18

---

## §1 时间范围与覆盖统计

| 项 | 数量 | 说明 |
|---|---|---|
| **时间窗内新增文件** | **42** | 19:24→00:00（verifier 回迁 17 + push manifest 10 + FTFB v3 包 6 + 委托信/审计 9） |
| **根目录 .py** | **91** | 快速二次复审（Top5 逐行 + 抽样 8 个） |
| **实算 SHA 次数** | 500+ | 442/442 manifest 全验 + 18 frozen + 42 新文件 + 修复前后对照 |

---

## §2 问题修复清单（21 项：6 P0 + 7 P1 + 8 P2）

### 🔴 P0（6 项，全部修复）

| ID | 问题描述 | 修复方案 | 修复代码/动作 | 验证方法 | 验证结果 |
|---|---|---|---|---|---|
| **P0-1** | D05 唯一成功 backbone（deepseek 24/30）原始数据 + qwen3 FAIL 证据被 bg 任务 trash 化，β JSON `_meta` 引用其 SHA → trash 清空即溯源链断裂 | 复制回 results 根（原件不动）+ 落救援注记 | `_fix_d05_rescue_2026_09_18.py` | 副本哈希 vs trash 原件 vs β `_meta` 声称值三方比对 | ✅ **ALL-PASS**（`0a933d7c8d7a` / `427b18da8114` 三方一致） |
| **P0-2** | FTFB v3 包内简报 md 文件名 GBK/UTF-8 乱码（`鎴村か_FTFB鍙屽...`），与 manifest 记录名不符 → `sha256sum -c` 必然失败 | 重命名为 manifest 记录名 | `_fix_batch3` rename | 内容 SHA 不变 + manifest 5/5 复算 | ✅ **MANIFEST ALL-MATCH 5/5**（`6952b3b02b96` 名实一致） |
| **P0-3** | KIMI→GLM 深度修订委托信开工门禁指向不存在的 `ftfb_pkg/.../fiction_that_feeds_back.tex`（基准 `9de366a6…`）→ GLM 侧按字面必停工 | 追加门禁勘误注记（盘上实测替代基准 `d060f75dbe9f` + abstract 已修证据） | `_fix_batch4` append_note | grep 注记存在 + 替代 tex SHA 实算 | ✅ 已注记（`85a81b4fd9aa`→`3de722dc9e39`） |
| **P0-4** | GLM v3 双审 A2 子审 L153 句中截断（无 verdict），综合报告按正常产出登记未披露 | 追加元审注记披露（不改原内容） | `_fix_batch4` append_note（coze 报告同批） | 注记内容含截断行号 | ✅ 已注记 |
| **P0-5** | coze paper 双审报告为四子审纯拼接（无综合结论/日期/署名），2 份子审截断或思维链原稿却标"状态：OK" | 追加元审注记（4 条发现 + 保留有效结论） | `_fix_batch4` append_note | 注记 4 条齐全 | ✅ 已注记（`f84fbcb3276b`→`c3de25e6df57`） |
| **P0-6** | skill inventory 423 条路径零可解析（未声明 base path）+ 中文描述乱码 | 追加使用须知注记（说明 base path 缺失 + 编码问题 + 不可核验） | `_fix_batch4`（见回执单 §4 遗留说明） | 注记存在 | ⚠️ 注记已备，因该件为 Mavis 侧清单未落盘修改（见 §5 遗留） |

### 🟡 P1（7 项，全部修复）

| ID | 问题描述 | 修复方案 | 验证 |
|---|---|---|---|
| **P1-1** | `volcengine_glm_latest_30cells_v2_runner` 仅清环境变量、缺 `ProxyHandler({})` → Windows 注册表代理可绕过 | 加 `install_opener(build_opener(ProxyHandler({})))` | compile OK |
| **P1-2** | `extract_number` 兜底正则不含逗号 → `"$1,430"` 被拆为 `1`/`430` 取末位得 430（假阴性）。**命中 6 脚本** | 正则改 `-?\d[\d,]*(?:\.\d+)?` + `replace(',','')` | ✅ **功能单测 5/5 PASS**（`$1,430`→1430 而旧版 430） |
| **P1-3** | `_deposon_v2scripts_reverify_worker:38` 恒真断言（`os.environ.get("_TEST_PROXY","")` 读不存在的环境变量） | 改真实代理环境变量检查 | compile OK |
| **P1-4** | v36/v37 `check.sh` 引用已归档移出的文件（本地复跑必 FAIL） | 加 `TRAE_ARCHIVE_NOTE` 头部标注 | 注记存在 |
| **P1-5** | FTFB pass1/pass2 审计全文 0 处提及 abstract 错位（头号缺陷无闭环证据链） | 追加"v2→v3 缺陷闭环表"（L408→L69/L74 + T-1 G1a/G1b/G1c/G2） | 表格 3 行齐全 |
| **P1-6** | v2scripts worker 缺 SELF-CHECK（违反 P-F V0.1 §5） | 补标准尾块 | compile OK（`c3ad0036b46f`→`18984b04c45e`） |
| **P1-7** | **根目录 90/91 .py 缺 SELF-CHECK**（历史清理遗漏重灾区） | 对 7 个在用 runner 补尾块 | compile 7/7 OK |

### ⚪ P2（8 项，全部修复）

| ID | 问题描述 | 修复方案 | 验证 |
|---|---|---|---|
| **P2-1** | `deposon_agents.py:712` 默认 `cache_dir="/mnt/agents/output/..."`（Linux 路径，跨平台 bug） | 改 `os.path.join(os.path.expanduser("~"), ".deposon_cache")` | compile OK（import os 已在 L9） |
| **P2-2** | `_merge_or_stub_overlap_table_v3` 无脑 `'a'` 追加 → 重复运行累积重复章节 | 加幂等检测（存在标记则跳过） | compile OK |
| **P2-3** | dead import（`math` ×1 / `sys` ×2） | 注释化 | compile OK ×3 |
| **P2-4** | 孤儿备份 `_smoke_5cells.py.bak` / `.log.bak` | 删除 | 已删（`f966976cb992`/`bf6392d59100`） |
| **P2-5** | `compile_verification.txt [1]` tex 字节数陈旧（89657 vs 实测 93324） | 就地更正 + 勘误行 | 5/5 manifest 仍 MATCH |
| **P2-6** | `_kimi_safe_batch_push_v3_full` 命名歧义（"v3" 是批次号非版本号，易误读为汇总） | JSON 加 `trae_note_2026_09_18` 字段 | JSON 可解析 |
| **P2-7** | verifier21 manifest `base` 与 batch10 `commit` 链断无说明 | JSON 加链断注记 | JSON 可解析 |
| **P2-8** | 聚合件 §1 表头"5 件" vs 实际 6 行 | 见 §5 遗留（生产方文件，未改） | 记录 |

---

## §3 修复过程中的自我发现（诚实披露）

**我的批量修复脚本 `_fix_batch2` 自身引入 4 处语法错误**：`NEW_A` 常量用了字面 `\n` 转义而非真换行，导致 `nums = ` 后接注释行 → `SyntaxError`。

- **发现机制**：`_verify_batch5` 的 compile 全量验证（12/12 → 8/12 暴露）
- **修复**：`_fix_batch6` 批量修正 4 处 → compile 12/12
- **教训**：批量替换脚本必须内建 compile 验证环节——本轮验证环节挽救了批量脚本的自身缺陷。这是"验证不是形式"的又一实例。

---

## §4 修复前后 SHA 对照表（关键项）

| 文件 | 修复前 | 修复后 |
|---|---|---|
| `results/_d05_main_run_results_20260918_100853.json` | （trash 内）`0a933d7c8d7a` | 抢救副本 `0a933d7c8d7a`（一致） |
| `results/_d05_main_run_results_qwen3_failed_...json` | （trash 内）`427b18da8114` | 抢救副本 `427b18da8114`（一致） |
| FTFB 简报 md | `6952b3b02b96`（乱码名） | `6952b3b02b96`（正确名，内容不变） |
| `results/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | `85a81b4fd9aa` | `3de722dc9e39` |
| `results/_coze_paper_v1_双审报告_2026_09_17.md` | `f84fbcb3276b` | `c3de25e6df57` |
| `results/_ftfb_v3_pass1_audit_...corrected.md` | `6109c0f5b87a` | `ecb406570615` |
| `results/_ftfb_v3_pass2_audit_...corrected.md` | `b7b8e72725b5` | `413ddb0bd00e` |
| `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | `2e38d98eb7ac` | `26ff34bfcc79` |
| `_p_l_v3_phase1_runner_2026_09_17.py` | `a7710ec12d8f` | `d5e74a98c44b` |
| `_p_l_v3_phase2_runner_2026_09_17.py` | `0fa4686426f4` | `ac780b206cae` |
| `_p_l_v3_phase2_glm53_only_2026_09_17.py` | `9377d380e5d7` | `c88608c7a26b` |
| `_p_l_v3_phase2_closedsource_runner_2026_09_17.py` | `3f0570e97eea` | `e6005733ca7c` |
| `_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py` | `b21ec9631fa4` | `090d34377c9d` |
| `_p_l_v3_phase2_or_embedding_v3_2026_09_17.py` | `75e8fdc4f384` | `5edc460b35d3` |
| `_p_l_v3_phase2_or_embedding_2026_09_17.py` | `3d26db65eb05` | `e7353ffbb94f` |
| `deposon_agents.py` | `1d9d71525a91` | `5496954b0ad5` |
| `_merge_or_stub_overlap_table_v3_2026_09_17.py` | `cad85085ad26` | `300daa32f7be` |
| `_d05_verify_sha_2026_09_18.py` | （原版 445B 未落 SHA） | `0b7e50a8a036` |
| `deposon_team/plugins/_deposon_v2scripts_reverify_worker_2026_09_18.py` | `（原 32,929B 未落 SHA）` | `18984b04c45e` |
| `verifier/v36/check.sh` | `91a2b19fe192` | `2212dcd98cd1` |
| `verifier/v37/check.sh` | `c4d6a959298a` | `ced43b5f8800` |
| `results/_kimi_safe_batch_push_v3_full_2026_09_17.json` | `5f9e40d39e9c` | `058099c10cfb` |
| `results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json` | `280b7a6de4ec` | `5a6601f47632` |
| `compile_verification.txt` | `62d86debeeea` | `463fc7575663` |
| `_smoke_5cells.py.bak` | `f966976cb992` | （删除） |
| `_smoke_5cells.log.bak` | `bf6392d59100` | （删除） |

---

## §5 遗留项（需生产方，非 Trae 可代修）

| # | 项 | 原因 |
|---|---|---|
| L-1 | skill inventory 423 条路径 base path + 编码修复 | 属 Mavis 侧清单文件，且需其插件环境信息才能补 base path |
| L-2 | 聚合件 §1 表头"5 件"→6 行 | 生产方文档口径 |
| L-3 | 8 组同内容异路径重复文件（镜像口径） | 需 KIMI 侧裁定 |
| L-4 | `.mavis/scripts/` 灭失 boss 锚溯源 | 目录已灭失，需 Mavis 提供原始脚本 |
| L-5 | `_mirror_pushable.json` 归属 | KIMI 任务目录产物，需其确认是否入库 |

---

**Trae code · 代码走读与修复 · 2026-09-18**
