# skill 目录 / plugin-cache 现状盘点与引用更新建议（2026-09-30）

- **件性质**：**只读盘点登记件**（0 回改既有件 · 0 覆写 · 0 改配置 · 0 改 skill 目录）
- **触发**：PI 2026-09-30 逐字「skill目录需要更新了，毕竟minimax code更新了，不知道路径发生了什么改变以致失败」
- **起因件**：`results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md`（`238077d25919`）§0.2 记 09-28 `scientific-research-workflows:scientific-writing` → `Local skill not found`
- **出件**：**doc-writer**（`agent-0032834a3e04`）· 依派工单执行 · 0 LLM / 0 API / 0 外部调用 / 0 key 读取
- **方法**：PowerShell 只读枚举 + `Get-FileHash -Algorithm SHA256` 实测 + `grep` 只读搜索；**未尝试加载任何 skill**（不制造运行时复现）
- **命名**：去版本前缀 · `_主题_日期`（`skill` + `2026_09_30`）；落名前 **2 轮撞名实测**（`results/` `docs/` `letters/` `deposon_team/` 四目录 × 2）均 0 命中

> **一票结论（先看这条）**：仓库件里写死的 plugin-cache 绝对路径与树哈希，**今日实测逐字仍然成立**（文件在、哈希对得上）。因此 PI 所猜「路径发生了什么改变」**在盘上事实层不成立**；失败另有候选解释，见 §5（**候选，未断言**）。

---

## §0 输入链核验（SHA-12 = `sha256(全文字节).hexdigest()[:12]` 小写 · 跑前实测 · 全部只读）

| # | 件 | 实测 SHA-12 | 字节 | 本件引用面 |
|---|---|---|---|---|
| 1 | `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `238077d25919` | 53,581 | **触发件**：§0.2 记 09-28 `Local skill not found` |
| 2 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | `2b9e886e729d` | 14,525 | 09-27 **成功**定位先例：全路径 + `0a314eed103a` / 13,044 B |
| 3 | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `98a779d61c1e` | 48,028 | 09-24 **实录失败**（`scientific-writing`） |
| 4 | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `05b975a86989` | 61,547 | 09-24 **实录失败**（`experimental-design`） |
| 5 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | `68f66904c0c8` | 22,863 | 09-26 **实录失败**（`peer-review`） |
| 6 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | `02c072833cca` | 32,186 | 09-28 **实录失败**（`experimental-design`） |
| 7 | `results/_v4_pending_decisions_2026_09_28.md` | `6db65c9d8792` | 23,373 | 09-28 **实录失败**（`experimental-design`） |
| 8 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | `0a2b5c837c83` | 21,855 | 09-27 直读 plugin-cache 成功先例 |
| 9 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | `c300e74a082c` | 29,349 | 同上（树哈希表列） |
| 10 | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | `fbf88f8ac7a6` | 10,103 | 记「已核存在于 plugin-cache」 |
| 11 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | `2fb5987f544d` | 192,292 | 记 `verification-before-completion`「known possibly-missing」 |
| 12 | `results/_v4_supp_t1_verdict.md` | `f1b5e49f3058` | 27,538 | **条件句**字面（非实录）样本 |
| 13 | `results/_v4_supp_t15_verdict.md` | `52c985429c91` | 52,884 | 条件句样本 |
| 14 | `results/_v4_supp_t15r2_verdict.md` | `8355724a26e3` | 64,145 | 条件句样本 |
| 15 | `results/_v4_supp_l14v3_n26_verdict.md` | `f4435801d09f` | 64,485 | 条件句样本 |
| 16 | `results/_v4_slow_cleanup_manifest_2026_09_28.md` | `5a6bb7f70418` | 14,600 | 记「skill 名（无专项 skill 加载）」（反向情形） |
| 17 | `letters/_v4_experiment_invitation_2026_09_20.md` | `4e8c0ea57028` | 30,820 | **对外披露面**· 绝对路径 + 树哈希写死 |
| 18 | `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | `8e1e7434905d` | 41,680 | 同上（v0.2 现行） |
| 19 | `letters/_v4_theme_reply_mavis_2026_09_20.md` | `00315728bbf5` | 36,719 | 树哈希缩写字面 |
| 20 | `letters/_v4_acceptance_trae_code_2026_09_20.md` | `3205593030bc` | 6,301 | **树哈希≠skill 哈希**既有口径来源 |
| 21 | `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `d3bdfc99fcdc` | 11,877 | 同上（展开为 9-skill 明细） |
| 22 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | `3d9f73519f6c` | 53,539 | 仅「来自 plugin-cache」无哈希 |

**核验小结**：22 项全部只读，**0 字节触动**；本件为**纯新建**。

---

## §1 plugin-cache 现状（`C:\Users\Administrator\.minimax\v2\plugin-cache\`）

**根层实测**：`plugin-cache\` 下**仅 1 个子目录 `official\`**（无其他来源根）；`official\` 下 **28 棵** `sha256-tree-v1-*` 树，**合计 172 个 skill 子目录**（实测求和）。
**树 mtime 区间**：`2026-09-01 16:17:03`（最早）→ `2026-09-24 09:21:17`（最新）。

| # | 树哈希（前 12） | skill 数 | 所含 skills（`skills\` 子目录名） |
|---|---|---|---|
| 1 | `01afed677637` | 4 | academic-abstract-refiner · academic-paper-polish · academic-paper-review · academic-writing-latex |
| 2 | `0581d93fb787` | 1 | voice-prompt |
| 3 | `08f9e34a83b4` | 1 | treg |
| 4 | `0f4d8d2c37b5` | 1 | pptx |
| 5 | `11421417a64d` | 9 | 3d-animation-short-generator · brand-promo-video-generator · co-op-game-intro-generator · h3-prompt-writing · handdrawn-live-video-generator · minimalist-product-ad-generator · music-video-subtitle-generator · paper-collage-explainer-generator · papercraft-stop-motion-explainer |
| 6 | `1aefb024ff06` | 1 | diagram-design |
| 7 | `1e8246669321` | 41 | pm-skills 族（analyze-feature-requests … wwas，共 41） |
| 8 | `26b42050e97f` | 1 | xlsx |
| 9 | `2ccf3f1f9d87` | 8 | marketing-skills 族（analytics · competitor-profiling · copywriting · customer-research · launch · marketing-plan · pricing · seo-audit） |
| 10 | `51060257c863` | 1 | humanizer |
| 11 | `5a0ee05fd942` | 3 | engineering-workflow · frontend-dev · fullstack-dev |
| 12 | **`611965fcb620`** | **9** | **experimental-design · hypothesis-generation · peer-review · scholar-evaluation · scientific-brainstorming · scientific-writing · statistical-analysis · statistical-power · uncertainty-and-units** |
| 13 | `67d1004a8294` | 25 | mattpocock-skills 族（ask-matt … wizard，共 25） |
| 14 | `74e227dec1c2` | 1 | control-in-app-browser |
| 15 | `85daab905fb0` | 9 | 游戏族（game-playtest · game-studio · game-ui-frontend · phaser-2d-game · react-three-fiber-game · sprite-pipeline · three-webgl-game · web-3d-asset-pipeline · web-game-foundings） |
| 16 | `89e862fa0239` | 8 | gsap 族（gsap-core … gsap-utils，共 8） |
| 17 | `9434cf938b38` | 1 | frontend-design |
| 18 | `953d7ad5f1f6` | 1 | write-h3-prompts |
| 19 | `9c0777059091` | 5 | chrome-devtools 族（a11y-debugging · chrome-devtools · debug-optimize-lcp · memory-leak-debugging · troubleshooting） |
| 20 | `ab4acef49d20` | 7 | performance 族（core-web-vitals · performance · performance-optimization · python-performance-optimization · swiftui-pro · vercel-react-best-practices · vercel-react-native-skills） |
| 21 | `ade95665080e` | 14 | superpowers 族（含 verification-before-completion） |
| 22 | `cc5b48e378a5` | 12 | text-to-cad 族（bambu-labs … urdf，共 12） |
| 23 | `d0e6ceccd252` | 1 | playground |
| 24 | `da7ac3ad9c06` | 1 | docx |
| 25 | `e3bd030641c2` | 1 | dsh |
| 26 | `e849ae554cb0` | 1 | pdf |
| 27 | `f3d59d331235` | 1 | superdesign |
| 28 | `fd617948b4fc` | 4 | codex 族（codex-cli-runtime · codex-prompt-engineering · codex-result-handling · codex-workflow） |

**旁侧目录实测（与失败相关，一并登记）**：

| 路径 | 实测 |
|---|---|
| `C:\Users\Administrator\.minimax\plugins\` | **空目录**（0 项）—— 沿既有件「首查 plugins 0 命中」口径，**今日仍成立** |
| `C:\Users\Administrator\.minimax\skills\` | **223 个目录，223 个含 `SKILL.md`**（mtime 分布：09-03 × 26 · 09-11 × 1 · 09-17 × 1 · **09-18 × 195**） |
| `C:\Users\Administrator\.minimax\skill-hub.json` | mtime `2026-09-18 11:46:00`；**实测 0 命中** 四个关键 skill 名、**0 命中** `plugin-cache` / `sha256-tree-v1` |
| `C:\Users\Administrator\.minimax\.builtin-skills\` | **20 个目录，mtime 全为 `2026-09-29 22:38:32`**；**无** scientific-* / academic-* / peer-review / experimental-design / verification-before-completion |

---

## §2 关键 skill 可定位性实测

### §2.1 派工单点名 + 仓库常引用 skill（plugin-cache 面）

**全部命中，树唯一（0 并列）**。`SKILL.md` SHA-12 为**实体文件自身**哈希，**与树哈希不是一回事**（沿 §0 #20 既有口径）。

| skill | 所在树（前 12） | 树唯一性 | SKILL.md SHA-12 | 字节 | SKILL.md mtime |
|---|---|---|---|---|---|
| `scientific-writing` | `611965fcb620` | 唯一 | `31f4fb3c0df5` | 13,047 | 2026-09-03 12:13:22 |
| `experimental-design` | `611965fcb620` | 唯一 | `0a314eed103a` | 13,044 | 2026-09-03 12:13:22 |
| `peer-review` | `611965fcb620` | 唯一 | `fed0262d707a` | 11,639 | 2026-09-03 12:13:22 |
| `hypothesis-generation` | `611965fcb620` | 唯一 | `039881416522` | 14,767 | 2026-09-03 12:13:22 |
| `scholar-evaluation` | `611965fcb620` | 唯一 | `902c41a08cb5` | 10,622 | 2026-09-03 12:13:22 |
| `statistical-analysis` | `611965fcb620` | 唯一 | `2bc90ee5c35a` | 19,957 | 2026-09-03 12:13:22 |
| `statistical-power` | `611965fcb620` | 唯一 | `1c8fea08a440` | 14,387 | 2026-09-03 12:13:22 |
| `scientific-brainstorming` | `611965fcb620` | 唯一 | `694060b28d59` | 12,937 | 2026-09-03 12:13:22 |
| `uncertainty-and-units` | `611965fcb620` | 唯一 | `064ef574c85d` | 18,906 | 2026-09-03 12:13:23 |
| `academic-paper-polish` | `01afed677637` | 唯一 | `23d90731e1fe` | 7,095 | 2026-09-01 16:17:03 |
| `academic-paper-review` | `01afed677637` | 唯一 | `20737a67cf75` | 13,855 | 2026-09-01 16:17:03 |
| `academic-abstract-refiner` | `01afed677637` | 唯一 | `daba372ddb88` | 7,023 | 2026-09-01 16:17:03 |
| `academic-writing-latex` | `01afed677637` | 唯一 | `aca04591e945` | 8,736 | 2026-09-01 16:17:03 |
| `verification-before-completion` | `ade95665080e` | 唯一 | `2befe7fc55bc` | 3,646 | 2026-09-01 16:17:14 |

**完整 SHA-256（可复算锚）**：
- `scientific-writing/SKILL.md` = `31f4fb3c0df5d78b87b09f533f360e31acc82043fc2c72c4a3a1a3b825dae035`
- `academic-paper-polish/SKILL.md` = `23d90731e1fe98698363dce611f09291baa6b2f6777a18e8be98ad397140aec6`
- `verification-before-completion/SKILL.md` = `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3`

> **与既有件逐字对账**：
> - `experimental-design` 记 `0a314eed103a` / 13,044 B（`_v3_recheck_12_jsv_check_2026_09_27.md:136-137`、`_v3_recheck_prereg_v1p1…v1p4`、`_v3_recheck_0{1,4}_rescript` 等）→ **今日实测逐字一致**。
> - `verification-before-completion`：`_v3_v4_achievements_inventory_2026_09_24.md:14` 记「known possibly-missing」→ **今日实测树在位、skill 在位、3,646 B**，该「possibly-missing」注记**已不成立**（件仍 0 回改，见建议 A6）。

### §2.2 同名双份实测（新发现 · 与失败候选直接相关）

`.minimax\skills\`（用户面，223 项）与 plugin-cache（插件面）之间存在 **10 个同名 skill**，**且 10/10 的 `SKILL.md` 内容均不相同**（SHA-12 与字节全不一致）：

| skill 名 | 用户面 `.minimax\skills` SHA-12 / 字节 / mtime | plugin-cache 树 / SHA-12 / 字节 / mtime | 是否同名不同内容 |
|---|---|---|---|
| `scientific-writing` | `f835a31244ad` / 33,780 / 09-18 | `611965fcb620` / `31f4fb3c0df5` / 13,047 / 09-03 | **是** |
| `peer-review` | `1a07d4a72406` / 23,119 / 09-18 | `611965fcb620` / `fed0262d707a` / 11,639 / 09-03 | **是** |
| `hypothesis-generation` | `6e15fe44f5a4` / 13,846 / 09-18 | `611965fcb620` / `039881416522` / 14,767 / 09-03 | **是** |
| `scholar-evaluation` | `4157069eee2e` / 12,257 / 09-18 | `611965fcb620` / `902c41a08cb5` / 10,622 / 09-03 | **是** |
| `scientific-brainstorming` | `dfdc611eb35e` / 8,178 / 09-18 | `611965fcb620` / `694060b28d59` / 12,937 / 09-03 | **是** |
| `statistical-analysis` | `82c7ee1761ac` / 19,765 / 09-18 | `611965fcb620` / `2bc90ee5c35a` / 19,957 / 09-03 | **是** |
| `docx` | `cfbabd72b1ae` / 20,084 / 09-18 | `da7ac3ad9c06` / `12e5a0cccd0c` / 11,619 / 09-03 | **是** |
| `pdf` | `9f78b8359fbd` / 8,072 / 09-18 | `e849ae554cb0` / `e39aa05f43db` / 28,593 / 09-01 | **是** |
| `pptx` | `e5b0df918cbe` / 9,182 / 09-18 | `0f4d8d2c37b5` / `931a81818974` / 32,801 / 09-03 | **是** |
| `xlsx` | `55591d7decc1` / 11,464 / 09-18 | `26b42050e97f` / `6eab2cbf5606` / 27,366 / 09-03 | **是** |

**`experimental-design` 在用户面无同名目录**（实测 0 命中）——**该 skill 独属 plugin-cache，却同样被记为失败**（09-24、09-28 各一次），故「同名遮蔽」**不能单独解释全部失败**（详见 §5）。

**两处 `scientific-writing` 的 frontmatter 事实对照**（各读前 12 行）：

| 项 | 用户面 | plugin-cache 面 |
|---|---|---|
| `name:` | `scientific-writing` | `scientific-writing`（**同名**） |
| `description:` | Core skill for the deep research and writing tool…（IMRAD / CONSORT·STROBE·PRISMA） | Draft, revise, and audit scientific manuscripts…evidence provenance, reporting-guideline coverage, authorship accountability… |
| `license:` | MIT license | MIT |
| `allowed-tools:` | Read Write Edit Bash | （无此字段） |
| `metadata.version` | （无） | `"2.0"` |
| `metadata.skill-author` | K-Dense Inc. | K-Dense Inc. |

> 两份**声明同一个 `name`**、同一 author、**内容与体量差异显著**（33,780 B vs 13,047 B）。**本件不断言加载器如何取舍**（未复现，见 §5-C2）。

---

## §3 仓库引用盘点

**统计面**：`letters\`、`results\`、`docs\`、`deposon_team\` 四目录，递归，扩展名 `.md/.json/.py/.txt`。

| 指标 | 实测 |
|---|---|
| 含 `plugin-cache` 或 `sha256-tree-v1` 字面的件 | **49 件**（含 1 件二进制状态备份，详见 A7） |
| 含 `Local skill not found` 字面的件 | **85 件** |
| **两者交集** | **29 件** |
| 仅路径引用、无失败字面 | 20 件 |
| 仅失败字面、无路径引用 | 56 件 |
| 并集 | 105 件 |
| `docs\` / `deposon_team\` 的路径引用件数 | **各 0 件**（路径固化面集中在 `letters\` 与 `results\`） |

**有效性判定口径**：以 §1 / §2 今日实测为准 —— 写死的绝对路径**文件仍在**、树哈希**仍在同一目录名**、关键 `SKILL.md` SHA-12 **逐字对得上** ⇒ 判 **仍有效**。

### §3.1 逐件盘点表（49 件）

| 件（相对 `deposon-repo/`） | 命中数 | 字面类型 | 有效性 | 建议 |
|---|---|---|---|---|
| `letters/_v4_experiment_invitation_2026_09_20.md` | 9 | **绝对路径 + 树哈希**（披露段 + §skill 表） | 仍有效 | A1 |
| `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | 9 | 同上 | 仍有效 | A1 |
| `letters/_v4_theme_reply_mavis_2026_09_20.md` | 4 | 树哈希缩写（`01afed677637…` / `611965fcb620…`） | 仍有效 | A1 |
| `letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md` | 4 | 同上 | 仍有效 | A1 |
| `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | 4 | 同上 | 仍有效 | A1 |
| `letters/_v4_acceptance_trae_code_2026_09_20.md` | 1 | 树哈希（验收口径：树哈希≠skill 哈希） | 仍有效 | A4 |
| `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | 2 | 树哈希 + 9-skill 明细 | 仍有效 | A4 |
| `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | 1 | 仅「来自 Mavis plugin-cache」 | 仍有效 | A1 |
| `results/_v3_recheck_12_jsv_check_2026_09_27.md` | 3 | **绝对路径 + SHA-12 + 字节** | 仍有效（逐字对账一致） | A2 |
| `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | 3 | `resolved_path` 全路径 + note | 仍有效 | A3 |
| `results/_v3_recheck_08b_executor/executor_2026_09_27.py` | 2 | 源码注释内嵌缩写路径 | 仍有效 | A3 |
| `results/_v3_recheck_08b_executor/result_2026_09_27.json` | 2 | `loaded_path` 字段 | 仍有效 | A3 |
| `results/_v3_recheck_26_preexp_report_2026_09_27.md` | 5 | 树哈希（plugin.json 实测）+ 直读方式 | 仍有效 | A2 |
| `results/_v3_recheck_26b_rescript_2026_09_27.md` | 4 | 树哈希 + 落位目录名 + 直读方式 | 仍有效 | A2 |
| `results/_v3_recheck_01_rescript_2026_09_27.md` | 1 | 「本仓与 plugin-cache 均可定位」 | 仍有效 | A2 |
| `results/_v3_recheck_04_rescript_2026_09_27.md` | 1 | 同上 | 仍有效 | A2 |
| `results/_v3_recheck_12_rescript_2026_09_27.md` | 1 | 同上 | 仍有效 | A2 |
| `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | 1 | 失败记录 + 补记 SHA-12 | 仍有效 | A2 + A5 |
| `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | 1 | 同上 | 仍有效 | A2 + A5 |
| `results/_v3_recheck_verdict_register_2026_09_27.md` | 1 | 同上 | 仍有效 | A2 + A5 |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1 | 树哈希 `ade95665080e` + 「possibly-missing」 | **路径有效；possibly-missing 注记已不成立** | **A6** |
| `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 1 | 失败记录（`peer-review`）+ 树哈希前缀 | 仍有效 | A2 + A5 |
| `results/_v4_gamma_r1_prereg_2026_09_28.md` | 1 | 失败记录（实录） | 仍有效 | A2 + A5 |
| `results/_v4_pending_decisions_2026_09_28.md` | 1 | 失败记录（实录） | 仍有效 | A2 + A5 |
| `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | 2 | 「已核存在于 plugin-cache」+ 树目录缩写 | 仍有效 | A2 |
| `results/_v4_slow_cleanup_manifest_2026_09_28.md` | 1 | 「Mavis plugin-cache sha256（不适用）」 | 仍有效（反向情形） | A2 |
| `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | 2 | 失败记录（实录，2 处） | 仍有效 | A2 + A5 |
| `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 2 | 失败记录（实录，2 处） | 仍有效 | A2 + A5 |
| `results/_v4_supp_l14v3_n26_verdict.md` | 4 | **条件句**「若实录」+ 树哈希前缀 | 仍有效 | **A5** |
| `results/_v4_supp_t1_verdict.md` | 3 | 条件句 + 两树哈希（含 `ade95665080e`） | 仍有效 | A5 |
| `results/_v4_supp_t15_verdict.md` | 4 | 条件句 + 树哈希前缀 | 仍有效 | A5 |
| `results/_v4_supp_t15r2_verdict.md` | 4 | 条件句 + 树哈希前缀 | 仍有效 | A5 |
| `results/_v4_supp_t1_executor.py` | 2 | 源码内嵌树哈希 | 仍有效 | A3 |
| `results/_v4_supp_t1_result.json` | 1 | `skill_absence_fallback` 字段 | 仍有效 | A3 |
| `results/_v4_supp_t15_executor.py` | 2 | 源码内嵌树哈希 | 仍有效 | A3 |
| `results/_v4_supp_t15_executor_r1_2026_09_27.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15_executor_r3_2026_09_28.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15_result.json` | 1 | `skill_absence_fallback` 字段 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_executor.py` | 2 | 源码内嵌树哈希 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_executor_r1_2026_09_28.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_executor_r3_2026_09_28.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | 2 | 同上 | 仍有效 | A3 |
| `results/_v4_supp_t15r2_result.json` | 1 | `skill_absence_fallback` 字段 | 仍有效 | A3 |
| `results/_v4_pi_cot_v2_ruleset_executor.py` | 2 | 源码 docstring 内嵌树哈希 | 仍有效 | A3 |
| `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 2 | 同上 | 仍有效 | A3 |
| `results/.evidence_backup_2026_09_28/runtime-state.sqlite` | 2,479 | **二进制状态备份**内嵌字串 | 不适用 | **A7** |

**小计**：文字件 **48** 件（+1 二进制）。**其中判定「仍有效」= 47 件，「注记已不成立」= 1 件（`_v3_v4_achievements_inventory_2026_09_24.md` 的 possibly-missing，见 A6），「不适用」= 1 件（二进制）。**

### §3.2 逐条更新建议

| 编号 | 面向 | 建议 | 处置 |
|---|---|---|---|
| **A1** | `letters/` 5 件（对外披露面） | **绝对路径 + 树哈希不宜写死在披露正文**。建议后续对外件改为：披露「起草使用了 Mavis 的 `scientific-research-workflows:scientific-writing` 等 skill」，**具体路径与哈希只在内部回执/登记件中记实测值**。理由：路径含本机用户名，且 plugin-cache 树哈希随包更新而变，写死即成陈旧面。 | **既有件 0 回改**（已发出的对外件改不回、也不应改）；**仅约束新件** |
| **A2** | `results/` 记录面 | 路径引用作为「**当时实测证据**」**保留有效、0 回改**。建议新件沿用同一写法，但**补一行「当前可定位性」**（如本件 §2.1），使读者能区分「历史实测」与「今日实测」。 | 新件执行 |
| **A3** | `results/` 产出物（`.py` / `.json`） | 内嵌在源码 docstring 与 `result.json` 字段里的绝对路径属**冻结产出物内容**，随产出冻结。**建议未来 executor 产出物不写绝对路径**（只记 `plugin:skill` 名 + `SKILL.md` SHA-12），路径另置登记件。 | 新件执行；既有件 0 回改 |
| **A4** | 树哈希引用（`letters/_v4_acceptance_trae_code` §72、`_v4_ide_track_review…` §74 等） | 沿既有口径：**树哈希 = 打包哈希，不是 skill 哈希**。建议新件**同时记「树哈希 + `SKILL.md` SHA-12」两值**，杜绝「拿树哈希当 skill 哈希」的误读。 | 新件执行 |
| **A5** | 失败字面统计面 | **关键口径修正**：`_v4_supp_t1_verdict.md` / `_v4_supp_t15_verdict.md` / `_v4_supp_t15r2_verdict.md` / `_v4_supp_l14v3_n26_verdict.md` 中的 `Local skill not found` 是**条件句（「若实录」）**，**不是实测失败记录**。因此「85 件含该字面」**不能读作 85 件失败**。建议新件把两种字面显式区分（「实录：…」/「若实录：…」），统计时只计实录。 | 新件执行；既有件 0 回改 |
| **A6** | `_v3_v4_achievements_inventory_2026_09_24.md:14` | 该件记 `verification-before-completion`「known possibly-missing」。**今日实测已不成立**（树 `ade95665080e` 在位、skill 在位、`2befe7fc55bc` / 3,646 B）。建议新件引用前**先实测再引**，不沿用「possibly-missing」注记。 | **0 回改该件**；本件记为勘误面，等 PI 是否另出勘误件 |
| **A7** | `.evidence_backup_2026_09_28/runtime-state.sqlite` | 二进制状态备份内的 2,479 处字串**不是人工引用面**，统计 skill 引用时应**排除二进制与状态备份件**。 | 建议纳入统计口径；本件已单列 |
| **A8** | 全项目 | 建议统一 **skill 三段式锚**：`plugin:skill` 名 ＋ 树哈希（前 12）＋ `SKILL.md` SHA-12（＋ 定位方式：加载器载入 / 直读实体 / 缺位 fallback）。四要素齐备时，「能不能定位」不再依赖任何绝对路径。 | 新件执行 |

---

## §4 「失败原因」候选（**仅列可核事实与候选解释 · 0 编造 · 0 断言**）

### §4.1 可核事实（今日实测，条条可复算）

| id | 事实 |
|---|---|
| F1 | plugin-cache 下 `official\` **仅 1 个来源根**，28 棵树、172 个 skill 目录，mtime 09-01 16:17:03 → 09-24 09:21:17。 |
| F2 | 派工单点名的 4 个 skill **全部可定位**（`scientific-writing` / `experimental-design` / `peer-review` / `academic-paper-polish`），树唯一，SHA-12/字节与既有件逐字一致。 |
| F3 | 仓库件写死的**绝对路径今日逐字存在**（如 `...\v2\plugin-cache\official\sha256-tree-v1-611965fc…\skills\scientific-writing\SKILL.md`）。 |
| F4 | `.minimax\plugins\` **仍为空目录**（0 项）。 |
| F5 | `.minimax\skills\` **223 项**（全部含 `SKILL.md`），其中 **195 项 mtime 集中在 2026-09-18**；`skill-hub.json` mtime 同为 `2026-09-18 11:46:00`。 |
| F6 | 用户面与 plugin-cache **同名 skill 10 个，10/10 内容不同**（详见 §2.2）。`experimental-design` **不在**这 10 个之内（用户面 0 命中）。 |
| F7 | 两处 `scientific-writing` **声明同一个 `name: scientific-writing`**，同一 author，体量 33,780 B vs 13,047 B，plugin 面多 `version: "2.0"`。 |
| F8 | `skill-hub.json` **不含** 4 个关键 skill 名、**不含** `plugin-cache` / `sha256-tree-v1` 字样。 |
| F9 | `.builtin-skills\` **20 项，mtime 全为 2026-09-29 22:38:32**，且**不含**任何 §2.1 的关键 skill。 |
| F10 | 仓库内**实录失败**（非条件句）可定位到：`scientific-writing` 09-24（2 件）、`experimental-design` 09-24 / 09-28（各 1 件 + 09-28 另 1 件）、`peer-review` 09-26（1 件），及 §3.1 表中标注者。**失败窗口 09-24 → 09-28**。 |
| F11 | 09-27 存在**成功定位先例**（`_v3_recheck_12_jsv_check_2026_09_27.md`，全路径 + SHA-12 + 字节），且 09-27 件明确记载「本 turn 无 skill 载入工具，故**直读 plugin-cache 实体**」。 |
| F12 | **parent 于 2026-09-30 实测**：`scientific-research-workflows:scientific-writing` **现可正常加载**，Location 为 plugin-cache 路径（**该结论系 parent 实测，非本件复现**）。 |

### §4.2 候选解释（**候选，均未验证，本件不断言**）

| id | 候选解释 | 与哪些事实相容 | 为何**未**判定 |
|---|---|---|---|
| **C1** | **PI 所猜「路径改变」在盘上事实层不成立** —— 路径未变、文件在、哈希对得上。若失败属实，则原因**不在路径本身**。 | F2 · F3 | 这是对假设的**否证性事实**，非原因；但它只排除「路径被改」，不排除「解析面变了」。 |
| **C2** | **同名遮蔽 / 解析面优先级**：用户面 `.minimax\skills\` 与 plugin-cache 各有一份 `name: scientific-writing`，若加载器按某顺序取值或对同名项判冲突，可能出现「实体在盘但取不到」。 | F5 · F6 · F7 | **本件未复现加载**（未尝试加载任何 skill），**未读加载器实现**（超出只读派工范围），**不知优先级次序**。 |
| **C3** | **`experimental-design` 反证**：它在用户面**无同名**、plugin-cache 面**稳定在位**，却被两次记为失败 ⇒ **C2 单独不足以解释全部失败**，还存在与「同名」无关的因素。 | F2 · F6 · F10 | 只知「不止一个因素」，**未识别第二个因素**。 |
| **C4** | **运行时/组件边界**：`.builtin-skills\` 20 项 mtime 全为 **2026-09-29 22:38:32**（PI「minimax code 更新了」的时点邻近），最新 plugin 树 materialized 于 **09-24 09:21:17**（失败窗口首日 09-24）。**时间上邻接**于失败窗口。 | F1 · F9 · F10 | **仅为时序邻接**；本件**未读更新日志 / changelog / 版本号**，**不能据此断定因果**。 |
| **C5** | **会话级状态差异**：F10（09-24→09-28 失败）与 F11（09-27 直读成功）、F12（09-30 加载成功）**并存** ⇒ 失败可能**不是全局的**，而是**特定会话/特定调用形态**下才出现（例如需带 `plugin:` 前缀的限定名 vs 裸名）。 | F10 · F11 · F12 | 本件**未做任何对照调用**，**未验证**限定名与裸名的行为差异。 |
| **C6** | **注册面缺失**：`skill-hub.json` 不含关键 skill（F8），`.minimax\plugins\` 为空（F4）⇒ 这些 skill 的可加载性**可能不由这两个面决定**；究竟由哪一面决定，本件**未能识别**。 | F4 · F8 | 只知「不是这两个面」，**未定位真正的解析面**。 |

### §4.3 明确**不成立**的说法（本件实测反证）

- ❌ 「plugin-cache 路径变了」→ **不成立**（F3：路径逐字在位）。
- ❌ 「关键 skill 从盘上消失了 / 被删了」→ **不成立**（F2：14 个关键 skill 全部在位，树唯一）。
- ❌ 「`verification-before-completion` 不存在」→ **不成立**（F2：`2befe7fc55bc` / 3,646 B 在位；旧件「possibly-missing」注记已过期）。
- ❌ 「85 件文件都发生了 skill 加载失败」→ **不成立**（A5：其中至少 4 件为**条件句**，非实录）。

---

## §5 诚实边界（不夸大 · 不误导）

1. **未做任何运行时复现**：本件**未尝试加载任何 skill**，故**既未复现失败、也未独立复现成功**。§4.1 F12 的成功结论**系 parent 实测**，本件仅作转述并明确标注来源，**不冒认**。
2. **未读加载器实现、未读更新日志 / changelog / 版本号**，故 §4.2 各候选**均停在「候选」**，无一被验证或否证。
3. **未验证 UI 侧插件安装 / 启用状态**，未打开任何设置界面。
4. **未改任何配置**：`config.yaml`、`mcp.json`、`plugin.json` 等**一律未读未写**（亦避免读取含敏感值的文件）；**0 配置改动**。
5. **未改 skill 目录**：`.minimax\skills\`、plugin-cache、`.builtin-skills\` **全部只读**，**0 写入、0 移动、0 重命名**。
6. **0 回改既有件**：§3.1 列出的 48 件文字件**全部原样在盘**，**0 字节触动**；§3.2 全部建议均为**面向新件**（A6 记为勘误面，**是否另出勘误件待 PI**）。
7. **内容比对仅限哈希 / 字节 / frontmatter 前 12 行**，**未做语义级 diff**；§2.2「同名不同内容」指**字节与哈希不同**，**不评判两者质量高低、不判定哪一份更权威**。
8. **`.minimax\skills` 223 项仅按目录名与 `SKILL.md` 存在性统计**，**未逐项加载、未逐项验签**。
9. 本件**不含任何密钥 / token / 端点**；未调用任何 LLM、API、外部 URL。
10. **本件自身 SHA-12 无法内嵌**（自引用悖论）—— 落盘后由 parent 复算并回填于回执，本节不预填数值。

---

## §6 待办清单

### 6.1 待 PI 拍板

| # | 事项 | 备选 |
|---|---|---|
| 1 | 是否**另出勘误件**登记 `verification-before-completion`「possibly-missing」已过期（A6） | 出勘误件 / 不出（仅本件登记） |
| 2 | 是否**采纳 A1**（对外件不再写死绝对路径与树哈希） | 采纳 / 不采纳 |
| 3 | 是否**采纳 A8**（统一 skill 三段式锚） | 采纳 / 不采纳 |
| 4 | 是否**委派一次「运行时定位对照实验」**以验证 §4.2 候选（限定名 vs 裸名 / 同名遮蔽 / 冷启动）——该动作**超出本件只读范围**，须 PI 明示 | 派 / 不派 |

### 6.2 我方可自行执行（不需拍板）

- 后续新件按 A2 / A3 / A5 / A8 写法起草（**不动任何既有件**）。
- 引用任何 skill 前**先实测**（路径 + `SKILL.md` SHA-12），不沿用可能过期的注记。

---

## §7 自核节

- **编码**：UTF-8 **无 BOM** · **换行**：LF（**0 CRLF**）——落盘后实测核验。
- **写入面**：**仅本件 1 件**；`results/` / `docs/` / `letters/` / `deposon_team\` 内**0 回改、0 覆写、0 删除**。
- **撞名实测**：落名前 **2 轮**（× 4 目录）均 `exists=False`；本件为**新建**，非覆写。
- **§0 输入链 22 项**：全部**只读**核验，`0 字节触动`。
- **§1 / §2 实测命令**：`Get-ChildItem` 枚举 + `Get-FileHash -Algorithm SHA256`（**SHA-256 全值算完后截前 12**；**非** SHA-1 冒充）。
- **本件自身 SHA-12 / 字节 / 行数**：由 parent **落盘后对终态复算**并回填回执（**自引用不可内嵌**，见 §5-10）。
- **署名**：**doc-writer**（`agent-0032834a3e04`）· 出件即本棒，**不冒认**他方名头。

<!-- self-check-tail -->
