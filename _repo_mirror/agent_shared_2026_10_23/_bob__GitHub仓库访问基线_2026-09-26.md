# 鲍勃·GitHub 仓库访问基线备忘（2026-09-26）

**任务来源**：管理员 18:02:43 派发（旧挂载目录失效，GitHub 仓为唯一数据源）
**执行方式**：完整 git clone + 全仓 SHA-256 索引 + 两轮实测基准逐项复测（本端只读实测，未执行任何冻结工件）

---

## 一、新固定路径与基线指纹

| 项 | 值 |
|---|---|
| 仓库 | https://github.com/zeroandcat/Deposon（main 分支） |
| 本地固定路径 | **/home/z/my-project/repos/Deposon**（完整 clone，含 .git 历史） |
| 克隆时 commit | **29f6fd264f2aa204a25cd1f21ad18caa65a60c01**（短 29f6fd2；2026-09-20 13:07:04 +0800；提交说明 "Phase 3: separate September from main tree (remove 522 mirrored files); main tree = August published-paper lineage + undated work; B-class same-name-diverged files kept pending version ruling"）——与管理员通报 29f6fd26 一致 |
| 远端复核 | 2026-09-26 18:0x `git ls-remote origin main` = 同一 commit，HEAD 未漂移 |
| 规模 | 1108 个文件（不含 .git）；全仓 57MB（.git 14MB） |
| 环境 | git 2.47.3；**无 git-lfs**；网络实测 github.com 直连 HTTP 200，clone 无阻断 |
| LFS 判定 | **仓库无 .gitattributes，全仓零 LFS 指针 → 无需安装 git-lfs**，普通 clone/pull 即得全量内容 |
| 旧挂载实测 | /home/z/my-project/upload/mount_agent_directory/deposon-repo/ 仅剩 attacks/、docs/ 空壳，确认失效 |

---

## 二、目录重排事实（Phase 3 关键变化，直接影响寻址）

1. **九月工作区整体分离**：旧挂载中的九月带日期工件现集中于 `_september_workspace/<原相对路径>`。权威映射清单＝`_september_workspace/_mirror_manifest.json`（701 条，字段 `origin`＝旧挂载相对路径 → `path`＝GitHub 新路径，另含 size/mtime；生成于 2026-09-20T12:50:00，source 标注 `_repo_mirror`）。
2. **主树保留**八月发表线＋无日期工件（原位不动，如 `corpus/v20/S*_n*.json`、`run_v21_gtformal.py`、`docs/GT_FORMALIZATION_v1.md`、`verifier/v1–v35` 等）。
3. **B 类同名分叉实测为零**：双树同名文件仅 2 个且逐字节一致（`deposon_team/plugins/_verify_15frozen.py`＝efae9274962e、`_verify_pg_v0.py`＝cdd3415ad993，主树与九月区两份全同）。
4. **1 个 redacted 文件**：`_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json`（manifest 自记 "secrets masked as ***REDACTED***; original bytes remain local"）——该件与旧挂载版字节必不一致，属**预期差异**，不在我的核验基准集内。
5. **V4 主题邀请函三件不在仓**：`_v4_experiment_invitation_2026_09_20.md`、`_v4_distillation_invitation_2026_09_20_v1.0.md`、`_v4_distillation_prompt_pack_2026_09_20_v1.0.md` 全仓检索零命中（HEAD 早于其落盘时刻；仓内仅有 09-17 的 `_v3x_d0_5_experiment_invitation_2026_09_17.md`）。**引用该三件须向用户另索**，不可再从仓内寻址。

---

## 三、旧挂载路径 → GitHub 相对路径映射表

**规则**：带 2026_09_ 日期的九月工件 → 前缀 `_september_workspace/`；八月线/无日期工件 → 主树原位。逐文件以 `_mirror_manifest.json` 的 origin→path 为准。

| 旧挂载路径（deposon-repo/ 下） | GitHub 相对路径（@29f6fd2） |
|---|---|
| corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/** | _september_workspace/corpus/v20/by_model/…/**（五槽目录俱在） |
| corpus/v20/index_v2_2026_09_16.json | _september_workspace/corpus/v20/index_v2_2026_09_16.json（另一同容副本在 by_model/kimi/ 下＝双 index_v2） |
| corpus/v20/strip_captions_22.json | _september_workspace/corpus/v20/strip_captions_22.json |
| corpus/v20/all.json | _september_workspace/corpus/v20/all.json |
| corpus/v20/{S*_n*.json, L_*.json, index.json} | 主树原位 corpus/v20/（未动） |
| results/**（九月带日期件） | _september_workspace/results/**（含 _adendum_*、_archive_2026_09_18/、boss_pa_1_rbr_rm_result_2026_09_15.json 等） |
| results/gt3_prior_cache/ 等八月线 | 主树原位 results/ |
| docs/V3X/**（D7 报告、KT SPEC、P_A/P_C/P_E D1_D3、1WEEK_KILL 等） | _september_workspace/docs/V3X/** |
| docs/GT_*（GT_FORMALIZATION、SPEC_GT2B/GT8C） | 主树原位 docs/ |
| verifier/handoff/**（KT_ABC1 锚等） | _september_workspace/verifier/handoff/**（**主树 verifier/ 无 handoff 目录**） |
| verifier/v1–v35、runs/ | 主树原位 verifier/ |
| deposon_team/plugins/**（_verify_15frozen、18frozen_remeasure py 等） | _september_workspace/deposon_team/plugins/**（同名 2 件主树亦有且一致） |
| deposon_team/products/minimax_artifact_v_2026_09_16.json | _september_workspace/deposon_team/products/…（与 by_model/minimax 副本同容） |
| run_v2*.py、deposon_*.py、gt_common.py 等根目录脚本 | 主树原位（未动） |

---

## 四、资产核验结论表（两轮实测基准 vs GitHub @29f6fd2）

**基准**：2026-09-20 两轮（V4 主题回应 §8 表 #1–#12 ＋ D1 审查 KT/18frozen/4-path），另含 09-01 五枚预注册锚与备忘录中已固化的 SHA-12。方法＝全仓 1108 文件逐一 SHA-256 前 12 位索引（索引存 `agents/6a962cc259312f271f3f1e73/repo_sha_index.json`）＋字节数比对＋内容锚 grep。

### A. SHA-12 ＋字节 双吻合（26 项，全部【吻合】）

| # | 名称 | 基准(字节/SHA-12) | GitHub 落位（:字节） | 结论 |
|---|---|---|---|---|
| 1 | by_model·kimi index_v2 | 24150/efe05ad775de | _september_workspace/corpus/v20/by_model/kimi/index_v2_2026_09_16.json:24150 | 吻合 |
| 2 | by_model·GLM_1 three_way | 19685/268ab1239a8a | …/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json:19685 | 吻合 |
| 3 | by_model·GLM_2 | 13150/39732a92b5c9 | …/by_model/GLM_2/glm_artifact_v_2026_09_16.json:13150 | 吻合 |
| 4 | by_model·coze | 10978/fee04170aa73 | …/by_model/coze/coze_artifact_v_2026_09_16.json:10978 | 吻合 |
| 5 | by_model·minimax | 25347/9e1ccbdceacc | …/by_model/minimax/artifact_v_2026_09_16.json:25347（另有同容副本 deposon_team/products/） | 吻合 |
| 6 | v2_phase1_60cells | 85508/a18bbc703b42 | _september_workspace/results/deposon_v2_phase1_60cells_2026_09_11.json:85508 | 吻合 |
| 7 | v2_phase2 | 3189/e337b824c4b9 | …/results/deposon_v2_phase2_dual_mainline_2026_09_11.json:3189 | 吻合 |
| 8 | v2_phase4 | 5212/cf7682348617 | …/results/deposon_v2_phase4_f4_2026_09_11.json:5212 | 吻合 |
| 9 | v3_v7_summary | 25049/063ac8d00542 | …/results/deposon_v3_v7_summary_2026_09_11.json:25049 | 吻合 |
| 10 | D7md | 38545/4a08521f8de1 | _september_workspace/docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md:38545 | 吻合 |
| 11 | d7_5anchor | 2456/4505cca79c15 | …/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json:2456 | 吻合 |
| 12 | boss_pa_1_rbr_rm_result | 8753/c7c59e0d2f6c | …/results/boss_pa_1_rbr_rm_result_2026_09_15.json:8753 | 吻合 |
| 13 | strip_captions_22 | 6a2656878745 | _september_workspace/corpus/v20/strip_captions_22.json:12798 | 吻合 |
| 14 | KT_ABC1_anchors(＝KT-D0 主锚) | 03c6c01f3697 | _september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12.json:6680 | 吻合 |
| 15 | KT_A1_SPEC | 78b71d404366 | _september_workspace/docs/V3X/KT_A1_SPEC_V0.1.md:29570 | 吻合 |
| 16 | KT_B1_SPEC | 0410ca0fbdae | …/docs/V3X/KT_B1_SPEC_V0.1.md:35688 | 吻合 |
| 17 | KT_C1_SPEC | 59d8f56347d5 | …/docs/V3X/KT_C1_SPEC_V0.1.md:31241 | 吻合 |
| 18 | KT_D0_SPEC | cce8e9a1b00e | …/docs/V3X/KT_D0_SPEC_V0.1.md:20927 | 吻合 |
| 19 | _trae_5audit_aggregated | 11465/43265e4bf2be | …/results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md:11465 | 吻合 |
| 20 | V3X_PATCH_5ANCHOR_RECONCILE | 27db4950f710 | _september_workspace/deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md:8222 | 吻合 |
| 21 | GT_FORMALIZATION_v1 | aeefb8ef6972 | docs/GT_FORMALIZATION_v1.md:19100（主树原位） | 吻合 |
| 22 | run_v21_gtformal | 9bbe43f41fa8 | run_v21_gtformal.py:16600（主树原位） | 吻合 |
| 23 | run_v22_p1c | 6e9673205dc0 | run_v22_p1c.py:7236（主树原位） | 吻合 |
| 24 | SPEC_GT2B | 68a5b08ef007 | docs/SPEC_GT2B.md:3318（主树原位） | 吻合 |
| 25 | SPEC_GT8C | 6b09de9911c0 | docs/SPEC_GT8C.md:6326（主树原位） | 吻合 |
| 26 | S2_n35.json | e20a1bbeaee7 | corpus/v20/S2_n35.json:2480（主树原位） | 吻合 |

### B. 结构/内容锚复测（6 项，全部【吻合】）

| # | 对象 | 基准事实 | GitHub 实测 | 结论 |
|---|---|---|---|---|
| 27 | 双 index_v2 | 全 SHA-256 逐位一致（efe05ad775de…dc79261），同容两路径 | 两副本全 SHA-256 ＝ efe05ad775de2398…dc79261，24150B 逐位一致 | 吻合 |
| 28 | 18frozen 复测件 | 18/18 PASS | _september_workspace/results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json：PASS×18、FAIL×0（runner py 同在 plugins/） | 吻合 |
| 29 | V3X 4-path·1WEEK_KILL | 45/45×2、FAIL_H0×3、R²=0.1986/0.2670 各 1、PARTIAL_PASS | _september_workspace/docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md（8526B/4ffb21bb6bfa）：45/45×2、FAIL_H0×3、0.1986×1、0.2670×1、PARTIAL_PASS×8 | 吻合 |
| 30 | V3X 4-path·P_A_D1_D3 | 51/60＝85.0% | P_A_D1_D3_REPORT_2026_09_15.md：51/60×1、85.0%×1（P_C/P_E_D1_D3_REPORT 亦在位） | 吻合 |
| 31 | b3 merkle 22caption | b3 root＝75596bbabdb8、per_caption＝22 | …/results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json：件内含 75596bbabdb8、per_caption len＝22 | 吻合 |
| 32 | minimax 30cells 源件 | fbb7677b9cd5、顶层 temperature=0.0 | _september_workspace/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json:23472（SHA 命中）、"temperature": 0.0 在位 | 吻合 |

**附加内容锚抽验**（与 09-20 轮记录一致）：GLM_1 0.0444×2＋glm_to_own 在位；phase1 total_passed":51＋pass_rate":0.85＋STRONG_PASS 在位；v7_summary 0.867×14＋86.67%×3＋"DEAD"×2＋0.0007×2 在位；d7_5anchor FAIL_H0＋P-A{deepseek-v4-pro}/P-E{kimi-k2.7-code,doubao-seed-2.1-turbo} 三模型名各×2 在位。

### 总判

- **基准 32 项（26 SHA 项＋6 结构/内容项）全部【吻合】，0 项不吻合。**
- 已知预期差异仅 2 处，均不属基准集：①redacted 1 件（§二.4）；②V4 邀请函三件不在仓（§二.5）。

---

## 五、LFS／同步注意事项

1. **无 LFS**：仓库无 .gitattributes、全仓零 LFS 指针。本环境虽无 git-lfs，**普通 clone/pull 已获全量内容**，无需安装。
2. **后续更新**：`cd /home/z/my-project/repos/Deposon && git pull --ff-only origin main`；pull 后应重跑本备忘的核验（全仓 SHA 索引脚本与 `repo_sha_index.json` 存我私有目录，可直接复算），并核对 commit hash 变化。
3. **引用口径切换**：今后盘上证据引用一律写「GitHub 相对路径@29f6fd2 ＋ SHA-12 ＋行号」；旧 `_repo_mirror` 与旧挂载路径仅作为历史文档中的陈迹出现，不再用于寻址。
4. **只读纪律沿用**：/home/z/my-project/repos/Deposon 视同冻结挂载——重跑任何工件先 `cp -r` 到 /tmp 或私有沙箱，绝不原地执行（沿用既有铁律）。
5. **mtime 不可作时间证据**：clone 后所有文件 mtime＝克隆时刻（2026-09-26 18:0x），与 09-18 教训同理；需时间证据时用 git log / manifest 内 mtime 字段。
6. **网络/权限实测记录**：github.com 直连可达（HTTP 200）；匿名 clone 57MB 无鉴权障碍；push 权限未测（本团队只读用途，无需 push）。
7. **密钥红线不变**：两枚 API key（Kimi/Ark）永不落盘；redacted 件即用户侧密钥遮蔽的先例，任何同步操作不得逆向还原该件。

---

*核验工具链：git 2.47.3 / python3 hashlib 全仓索引（1108 文件）/ rg 内容锚。基准来源：shared/鲍勃_V4主题回应_证据素材_2026-09-20.md、shared/鲍勃_V4邀请函D1审查_可执行性_2026-09-20.md、shared/鲍勃_V4追加脑暴_证据新种子_2026-09-20.md 及长期记忆锚表。*

---

## 六、事件登记（2026-09-29 追加）

- **HEAD 漂移一行**：2026-09-29 00:28:38–40 +0800 W2 归仓推送后，远端 main HEAD `a57d7fe80d151f93e74e1b1a85c20242af39f26d` → **`9b6d80aaad9032610af2eff64b18f6d00e604ab3`**（短 9b6d80a）。单一 commit 仅新增仓根 `handoff_machine_readable.json`（0 触动既有文件，文件数 1517→1518）；本地冻结克隆已 `git pull --ff-only` 同步至该 commit、工作树 clean、`git diff a57d7fe..HEAD`＝仅 `A` 该一件。执行记录：`shared/鲍勃_W2归仓上传执行记录_2026-09-29.md`。
- **W2 就位登记**：FTFB 引用面 gap 件 W2（handoff 机读载体，deposon-handoff/v1）已就位仓根：6,452 B／SHA-256 全值 `9fccd007be9f9db8883a29bc7bf012455bda1efa20fc98dd0b9c15c337a55134`，raw 回取字节级一致。**R4 pending 统一关闭仍待 W3（KIMI 上传）入库，本轮不收束。**
- **push 权限状态更新**：§五.6「push 权限未测」→ 已于 2026-09-29 实测一次（W2 归仓推送；PAT 一次性认证、零落盘、值不入任何记录；用户 2026-09-29 00:11 群消息交付，用后建议按约吊销）。
- **SHA 索引待复算**：`repo_sha_index.json` 为 29f6fd2 时点（1108 件）索引；a57d7fe 时点树为 1517 件，本次 +1 后 1518 件，全仓索引复算列为后续项（新增件文件级 SHA-256 同上全值，git blob `9ab60b6e428c6b59b43b58899988f269d5c6aaf4`，mode 100644）。
- **PAT 生命周期闭合（2026-09-29 11:58 追记）**：W2 归仓所用 GitHub PAT 生命周期已闭合——交付（用户 09-29 00:11 群渠道）→ 仅 W2 推送单次使命使用（00:28:38–40，即 §五.6 登记的 push 实测）→ **PI 确认已吊销**（用户 2026-09-29 11:50 确认）；值全程零抄录、不落任何文件。§五.6 push 权限条目至此完全关闭（唯一一次 PAT 使用已终结，此后团队对该仓恢复纯匿名只读）。
- **吊销后只读复核（2026-09-29 11:58:19–27 实测，三路全正常）**：①`git ls-remote` 匿名返回 main＝`9b6d80aaad9032610af2eff64b18f6d00e604ab3`（＝§六首行登记值，无漂移）；②主克隆匿名 `git pull --ff-only`＝Already up to date、HEAD 同值、工作树 clean；③GitHub API 匿名旁证 HTTP 200（private=false、default_branch=main、pushed_at 2026-09-28T16:28:40Z＝W2 推送时刻后零新推送）。**结论：PAT 吊销不影响匿名只读访问，团队数据源完好。**
- **变更说明（2026-09-29 11:58）**：本节就地追加 PAT 生命周期闭合与吊销后只读复核两行（小体量补记，未出独立件），其余内容零改动；PAT 使用原始记录见 `shared/鲍勃_W2归仓上传执行记录_2026-09-29.md` §六。
