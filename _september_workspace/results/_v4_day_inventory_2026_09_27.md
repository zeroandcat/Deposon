# V4 收尾整理 · 今日（2026-09-27）文件夹四件套台账

> **派工**：evidence-auditor（agent-11335500b168 · 证据链审计专职）
> **触发**：PI 2026-09-27「今日收尾阶段记得整理文件夹四件套」；本棒即 PI 早前拍板「文件数一类均 V4 收尾并整理时再校正」的**校正时点**
> **四件套**：①盘点 ②清理 ③清单台账 ④计数校正（本件即 ③，并汇总 ①②④ 结论）
> **性质**：新建独立审链登记件；只读实测 + 1 次授权范围内的 `.tmp` 临时件清理；不动任何交付件 / 证据件
> **边界**：R5 frozen 只追加 / V1–V3 只读不动 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文无例外 / 仓外目录只读 0 写入
> **口径锚**：`results/_v4_maindir_count_monitor_2026_09_27.md`（SHA-12 `71e9cc179bec`）+ `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md`（SHA-12 `CC498BC28525`）
> **skill 状态**：`scientific-research-workflows:statistical-analysis`（plugin `@scientific-research-workflows`）**本地加载实测 `Local skill not found`**；`C:\Users\Administrator\.minimax\plugins\` 实测为空目录；按纪律锚 fallback 格式字面执行（详见 §F.6）
> **SHA-12 定义**：`hashlib.sha256(bytes).hexdigest()[:12]`（hexdigest 输出已小写）

---

## A. 摘要

| 项 | 值 |
|---|---|
| **① 今日盘点**（mtime = 2026-09-27，results/ + letters/ + docs/ 递归） | **94 件 / 4,622,566 B**（results 90 / letters 3 / docs 1） |
| **② `.tmp` 清理** | 清走 **10 件**一次性探针 / **13,939 B**；保留 22 件（`_run_*` 可复跑 runner + 其日志 + 证据对） |
| **③ 清单台账** | 本件；10 类分类账，**0 件未归类** |
| **④ 计数校正** | 三口径重测 **1,146 / 1,009 / 1,146**（终态，含本棒 4 件新建件）；挂账 5 项中 **4 项对清 / 1 项（994）无盘上来源如实留档** |
| **0 触动自证** | 19 件锚链 SHA-12 全等，**触动数 = 0** |
| **key 形态自扫** | 严格 pattern **0 命中** / 宽 pattern **0 命中** → **CLEAN** |
| **未归因残留** | **2 件**（§E.1，如实登记，不推定成因） |

---

## B. ① 盘点 · 今日新增件全量清单（94 件 / 4,622,566 B）

### B.0 分类小计

| 类 | 件数 | 字节 |
|:-:|---:|---:|
| 1a V3-R 系（recheck 主系） | 45 | 2,493,810 |
| 1a· V3-R 系 · 汇总登记 | 1 | 65,913 |
| 1b 预实验件（preexp 面） | 9 | 441,735 |
| 2 V3-S 系 | 9 | 404,739 |
| 3 V3 采集件 | 5 | 67,392 |
| 4 V4 线 pi_cot v3 系 | 19 | 600,757 |
| 5 委托件 | 1 | 59,958 |
| 5 委托件 / 独立 judgment 请求 | 2 | 57,439 |
| 6 勘误链版本 | 1 | 407,284 |
| 7 审链 / 治理件 | 2 | 23,539 |
| **合计** | **94** | **4,622,566** |

> 分类器首轮把目录嵌套件（如 `_v3_s1_executor/executor_*.py`）误判入「未归类」10 件；**已修分类器改按全相对路径匹配**（测量仪器先审自己），复测未归类 = **0**，件数 / 字节双重复算与 JSON 原始计数全等。

### B.1 — 1a V3-R 系（recheck 主系）· 45 件 / 2,493,810 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 37,346 | `88052d7db895` | 13:33:20 |
| 2 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 42,970 | `bcc3cee23e82` | 14:44:22 |
| 3 | `results/_v3_recheck_26_executor_2026_09_27.py` | 15,056 | `46c326c756c3` | 14:45:28 |
| 4 | `results/_v3_recheck_28_executor_2026_09_27.py` | 17,735 | `4e8c0dd8f54f` | 14:47:05 |
| 5 | `results/_v3_recheck_08_executor_2026_09_27.py` | 15,598 | `21c4ba4d479e` | 14:49:01 |
| 6 | `results/_v3_recheck_26_rescript_2026_09_27.md` | 8,937 | `3d9ad5f1540d` | 14:49:56 |
| 7 | `results/_v3_recheck_28_rescript_2026_09_27.md` | 10,187 | `a0734e0a6860` | 14:50:20 |
| 8 | `results/_v3_recheck_08_rescript_2026_09_27.md` | 10,459 | `2e08b9ae9f09` | 14:50:51 |
| 9 | `results/_v3_recheck_26_result_2026_09_27.json` | 11,994 | `eb6a99dd46dd` | 14:51:06 |
| 10 | `results/_v3_recheck_08_result_2026_09_27.json` | 10,587 | `0d2af01086db` | 14:51:08 |
| 11 | `results/_v3_recheck_28_result_2026_09_27.json` | 26,113 | `c0a8cb9029a7` | 14:53:26 |
| 12 | `results/_v3_recheck_19_executor_2026_09_27.py` | 19,215 | `b133a631b1a8` | 14:55:27 |
| 13 | `results/_v3_recheck_19_rescript_2026_09_27.md` | 11,089 | `82a947f2aebd` | 14:56:14 |
| 14 | `results/_v3_recheck_19_result_2026_09_27.json` | 59,888 | `df07cf80930f` | 14:56:25 |
| 15 | `results/_v3_recheck_10_executor_2026_09_27.py` | 33,647 | `80947906e592` | 15:12:15 |
| 16 | `results/_v3_recheck_08b_executor/executor_2026_09_27.py` | 43,901 | `b292410d9a69` | 15:17:27 |
| 17 | `results/_v3_recheck_08b_executor/result_2026_09_27.json` | 88,052 | `f9a7fa2d65b1` | 15:17:36 |
| 18 | `results/_v3_recheck_27_executor_2026_09_27.py` | 34,084 | `190cbe01d061` | 15:17:40 |
| 19 | `results/_v3_recheck_08b_executor/rescript_2026_09_27.md` | 18,501 | `78f3aba1f24c` | 15:18:54 |
| 20 | `results/_v3_recheck_10_result_2026_09_27.json` | 82,535 | `5d4b6baf1b18` | 15:20:09 |
| 21 | `results/_v3_recheck_27_result_2026_09_27.json` | 42,571 | `e06cb51fb3af` | 15:20:39 |
| 22 | `results/_v3_recheck_27_rescript_2026_09_27.md` | 14,599 | `6f045bdc70e7` | 15:22:57 |
| 23 | `results/_v3_recheck_10_rescript_2026_09_27.md` | 14,445 | `fc0ffd27adca` | 15:23:59 |
| 24 | `results/_v3_recheck_01_executor_2026_09_27.py` | 41,004 | `919fa909381e` | 15:43:40 |
| 25 | `results/__pycache__/_v3_recheck_26b_executor_2026_09_27.cpython-314.pyc` | 55,314 | `f5fbfa3126c7` | 15:50:56 |
| 26 | `results/_v3_recheck_26b_executor_2026_09_27.py` | 43,171 | `5c906113a210` | 15:51:38 |
| 27 | `results/_v3_recheck_26b_result_2026_09_27.json` | 44,379 | `49c6e5a07732` | 15:52:40 |
| 28 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | 29,349 | `c300e74a082c` | 15:52:59 |
| 29 | `results/_v3_recheck_01_rescript_2026_09_27.md` | 13,233 | `434b3213bdce` | 15:54:47 |
| 30 | `results/_v3_recheck_04_executor_2026_09_27.py` | 49,405 | `e098fa21700d` | 15:56:09 |
| 31 | `results/_v3_recheck_04_rescript_2026_09_27.md` | 13,472 | `2e0f6b8bf141` | 15:56:59 |
| 32 | `results/_v3_recheck_12_executor_2026_09_27.py` | 49,430 | `4850b1cbb010` | 16:00:42 |
| 33 | `results/_v3_recheck_12_rescript_2026_09_27.md` | 19,914 | `1cd36ac1b2c0` | 16:03:32 |
| 34 | `results/_v3_recheck_01_result_2026_09_27.json` | 167,831 | `c19e2ab24e63` | 16:04:01 |
| 35 | `results/_v3_recheck_04_result_2026_09_27.json` | 840,158 | `db8cfb974ce3` | 16:04:05 |
| 36 | `results/_v3_recheck_12_result_2026_09_27.json` | 187,612 | `cdb37ed0b32f` | 16:04:05 |
| 37 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | 14,525 | `2b9e886e729d` | 16:21:15 |
| 38 | `results/_v3_recheck_35_rescript_2026_09_27.md` | 13,211 | `138faf395f40` | 16:24:33 |
| 39 | `results/_v3_recheck_35_result_2026_09_27.json` | 34,547 | `e9aa6e5180ca` | 16:25:59 |
| 40 | `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | 37,636 | `bc68854a6eba` | 16:30:17 |
| 41 | `results/_v3_recheck_21_rescript_2026_09_27.md` | 14,618 | `04f6ecd482b9` | 16:44:40 |
| 42 | `results/_v3_recheck_21_result_2026_09_27.json` | 44,928 | `354ae9c14fe2` | 16:54:07 |
| 43 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | 33,904 | `a8da321b64d2` | 17:08:53 |
| 44 | `results/_v3_recheck_12_rj5_provenance_2026_09_27.md` | 23,822 | `20f15c49feb5` | 17:30:07 |
| 45 | `results/_v3_recheck_08b_executor/__pycache__/executor_2026_09_27.cpython-314.pyc` | 52,838 | `5dfa39f98d45` | 17:50:45 |

### B.2 — 1a· V3-R 系 · 汇总登记 · 1 件 / 65,913 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v3_recheck_verdict_register_2026_09_27.md` | 65,913 | `9708e7ef1f8c` | 17:18:28 |

### B.3 — 1b 预实验件（preexp 面）· 9 件 / 441,735 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v3_recheck_26_preexp_executor_2026_09_27.py` | 38,726 | `775217a462f5` | 15:29:13 |
| 2 | `results/_v3_recheck_26_preexp_data_2026_09_27.json` | 94,658 | `177c88e1bd82` | 15:30:22 |
| 3 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | 21,855 | `0a2b5c837c83` | 15:33:12 |
| 4 | `results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py` | 35,555 | `96f491a8e2bf` | 17:47:47 |
| 5 | `results/_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json` | 36,844 | `fae3c4640507` | 17:47:59 |
| 6 | `results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py` | 37,775 | `cb6eb9164df3` | 17:52:40 |
| 7 | `results/_v3_recheck_08c_preexp_data/result_2026_09_27.json` | 146,601 | `689a6e4427a8` | 17:52:51 |
| 8 | `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | 15,211 | `aa02cbfc84e3` | 17:53:40 |
| 9 | `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | 14,510 | `6df402298557` | 17:53:57 |

### B.4 — 2 V3-S 系 · 9 件 / 404,739 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v3_s_prereg_v1_2026_09_27.md` | 46,836 | `ef5a40554960` | 15:28:46 |
| 2 | `results/_v3_s1_executor/executor_2026_09_27.py` | 54,937 | `10870941c283` | 15:44:50 |
| 3 | `results/_v3_s1_executor/rescript_2026_09_27.md` | 17,253 | `9d49a632ee81` | 15:45:21 |
| 4 | `results/_v3_s1_executor/result_2026_09_27.json` | 24,975 | `bfc99c3133dd` | 15:45:21 |
| 5 | `results/_v3_s1_executor/__pycache__/executor_2026_09_27.cpython-314.pyc` | 67,735 | `52cc4c06dc4e` | 15:56:39 |
| 6 | `results/_v3_s2_executor/executor_2026_09_27.py` | 84,993 | `f1e272a0924a` | 16:03:46 |
| 7 | `results/_v3_s2_executor/rescript_2026_09_27.md` | 23,039 | `331022480a57` | 16:05:12 |
| 8 | `results/_v3_s2_executor/result_2026_09_27.json` | 51,039 | `d73d51e670de` | 16:05:12 |
| 9 | `results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | 33,932 | `7e1323b09030` | 17:11:28 |

### B.5 — 3 V3 采集件 · 5 件 / 67,392 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v3_n_pg_boss_live_data_2026_09_27.json` | 9,220 | `be11c5274807` | 14:15:46 |
| 2 | `results/_v3_n_cpath_live_data_2026_09_27.json` | 12,711 | `25374af92f88` | 14:16:19 |
| 3 | `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | 6,411 | `26c0d0b0ffb6` | 14:17:05 |
| 4 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | 21,332 | `426cfe18cf65` | 14:20:06 |
| 5 | `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | 17,718 | `642582d4fbd1` | 16:20:32 |

### B.6 — 4 V4 线 pi_cot v3 系 · 19 件 / 600,757 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v4_supp_t15r2_methodology_template.md` | 17,411 | `6f9b865280a3` | 11:40:23 |
| 2 | `results/_v4_pi_cot_v3_prereg.md` | 27,223 | `b7547329af2e` | 12:02:44 |
| 3 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 20,194 | `cbf60a630c9f` | 12:10:45 |
| 4 | `results/_v4_pi_cot_v3_dataset.json` | 16,025 | `5118f5b44f17` | 12:12:25 |
| 5 | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 58,794 | `8a81d90c69ba` | 12:29:46 |
| 6 | `results/__pycache__/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | 67,049 | `bd231a2482ae` | 12:30:36 |
| 7 | `results/_v4_pi_cot_v3_ruleset_v3.json` | 21,392 | `9d77a5e2cbab` | 12:31:02 |
| 8 | `results/_v4_pi_cot_v3_result_v3.json` | 27,203 | `585714f9660c` | 13:04:21 |
| 9 | `results/_v4_pi_cot_v3_verdict_v3.md` | 53,751 | `bb44fdc7ab0f` | 13:15:20 |
| 10 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 16,587 | `990c0c42a6f6` | 13:17:51 |
| 11 | `results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | 42,157 | `41d29f4deb70` | 13:24:20 |
| 12 | `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | 62,115 | `ee8671a28c2f` | 16:56:08 |
| 13 | `results/__pycache__/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | 69,630 | `e7ab1adbf898` | 16:58:47 |
| 14 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 18,714 | `6eed9acdb99a` | 17:04:40 |
| 15 | `results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | 26,891 | `cbc14a76f038` | 17:13:08 |
| 16 | `results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | 10,251 | `58ed6be022ed` | 17:14:41 |
| 17 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | 12,975 | `ed596914259a` | 17:48:03 |
| 18 | `results/_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | 22,292 | `735c03db1ae9` | 17:48:03 |
| 19 | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | 10,103 | `fbf88f8ac7a6` | 17:49:03 |

### B.7 — 5 委托件 · 3 件 / 117,397 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` | 59,958 | `b0e49a6b09f9` | 16:55:14 |
| 2 | `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | 34,737 | `3b7a4888efd8` | 12:56:14 |
| 3 | `letters/_v3_recheck_indep_judgment_request_2026_09_27.md` | 22,702 | `2c486c1791d5` | 16:18:21 |

### B.8 — 6 勘误链版本 · 1 件 / 407,284 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 407,284 | `aed375c485fb` | 14:27:52 |

> **性质注记**：本件 CreationTime 早于今日（**纯追加**，非新增件）——故计入「今日 mtime 盘点」但**不计件数 delta**。对照 `71e9cc179bec` §D.1 第 3 行（v21→v22 同件纯追加不计件数），本件为同类追加。
> **本棒 0 触动**：未写入、未修改、未移动，仅计算 SHA-12。

### B.9 — 7 审链 / 治理件 · 2 件 / 23,539 B

| # | 相对路径 | 字节 | SHA-12 | mtime |
|:-:|---|---:|:-:|---|
| 1 | `results/_v4_maindir_count_monitor_2026_09_27.md` | 15,313 | `71e9cc179bec` | 11:50:37 |
| 2 | `results/_v4_day_inventory_measure_2026_09_27.py` | 8,226 | `3e903f224f87` | 18:02:27 |

> 第 2 件 = 本棒新建盘点实测器（只读测量，stdout 出 JSON，不写盘内任何既有件）。

### B.10 盘点口径双记（mtime vs ctime）

| 口径 | 值 | 说明 |
|---|---:|---|
| **mtime = 09-27**（results + letters + docs 递归） | **94** | 本台账 B 节采用；含 1 件纯追加件（`aed375c485fb`） |
| **ctime = 09-27**（主目录全域） | **137** | 今日**新建**件；分布 results 90 / .tmp 24 / __pycache__ 13 / deposon_team 6 / letters 3 / verifier 1 |

> 两者差 43 件：`.tmp` 临时件（24）、`__pycache__` 字节码（13）、`deposon_team/`（6）、`verifier/`（1）落在 mtime 口径扫描目录之外；另有 mtime 口径的 docs 纯追加件（1）ctime 非今日。**如实双记，不强行对齐。**

---

## C. ② 清理 · `.tmp` 今日临时探针件（清前 / 清后登记）

### C.1 授权与边界

- 授权：派工单「清理仅限 `.tmp` 临时件（经 mavis-trash 可恢复删除；交付件/证据件 0 动）」
- 通道：`rm -- <path>` → **`mavis-trash`**（路由实测确认，落 Recycle Bin 可恢复；**未使用永久删除，未 inline 脚本删除**）
- 范围：**仅今日（mtime = 2026-09-27）** 一次性探针件；**非今日件（54 件）本棒 0 动**
- 保留惯例：`_run_*` 可复跑 runner 件**全保留**；runner 日志与其配对保留；证据件（自扫结果 / 诊断输出）保留

### C.2 清前 / 清后

| 项 | 清前（2026-09-27 18:02） | 清后（18:05:59） | delta |
|---|---:|---:|---:|
| `.tmp/` 文件数 | **86** | **76** | **−10** |
| `.tmp/` 总字节 | 3,625,532 | 3,611,593 | **−13,939** |
| 今日（09-27）件 | **32** | **22** | **−10** |
| 非今日件 | 54 | 54 | 0 ✓ |
| 主目录 `.tmp/` 子树计数（计入口径） | 86 | 76 | −10 |
| 本棒另建 helper（`.tmp/_run_*_verify/table`） | — | +2 | +2 |

### C.3 清走 10 件逐件登记（清前 SHA-12 留痕）

| # | 相对路径 | 字节 | 清前 SHA-12 | mtime | 判为一次性探针的依据 |
|:-:|---|---:|:-:|---|---|
| 1 | `.tmp/_check2.py` | 692 | `26fa69e6f37e` | 13:06:20 | 无 `_run_` 前缀；无配对输出件；后续被 `_verify_v3.py` 取代 |
| 2 | `.tmp/_dupids.py` | 928 | `0e137d144fa4` | 12:59:29 | 同上（ID 去重一次性核查） |
| 3 | `.tmp/_eventids.py` | 1,003 | `c18b58b3296b` | 12:58:43 | 同上（事件 ID 抽样核查） |
| 4 | `.tmp/_explore_addenda.py` | 1,073 | `93d85c99c661` | 12:55:30 | 同上（附录目录一次性浏览） |
| 5 | `.tmp/_handoff_summary.py` | 1,491 | `aaaf4931580c` | 13:06:47 | 同上（交接摘要一次性生成，无下游引用） |
| 6 | `.tmp/_pk_selfscan_v3s.py` | 638 | `696aad006f89` | 15:29:13 | 一次性 key 自扫探针；本棒已**另出**严格+宽双 pattern 全量自扫（§F.5），功能被覆盖 |
| 7 | `.tmp/_test_fp.py` | 943 | `dcdb011f5ade` | 13:03:29 | 一次性指纹自测探针 |
| 8 | `.tmp/_v2verdict_check.py` | 382 | `ba1694eb0c15` | 12:56:37 | 一次性 v2 判据核查探针 |
| 9 | `.tmp/_verify_btier.py` | 4,727 | `931a59aa1fd1` | 16:25:53 | 一次性 B-tier 核查探针；无配对登记输出件 |
| 10 | `.tmp/_verify_v3.py` | 2,062 | `554ed49adac1` | 13:04:57 | 一次性 v3 核查探针 |
| | **合计** | **13,939** | | | |

> 逐件清后 `Test-Path` 复验：**10/10 = False**（盘上已不存在）✓

### C.4 保留 22 件今日 `.tmp` 件（0 动，逐条理由）

| 保留子类 | 件数 | 保留理由 |
|---|---:|---|
| `_run_*` 可复跑 runner | 6 | 派工单明示惯例：`_run2.py` / `_run_final.py` / `_run_result_v3.py` / `_run_recheck_r1.py` / `_run_d4_relabel_addendum.py` / `_run_v3r1_relabel.py` |
| runner 配对日志 | 9 | `_run_output.log` / `_d4_relabel_run1.log` / `_recheck_r1_run{1,A,B,C,D}.log`（5 件）/ `_v3r1_run{1,2}.log` —— 今日交付件的**运行证据** |
| 自扫脚本 + 结果对 | 2 | `_r4_key_scan_r1_files_2026_09_27.py` + `.json`（key 形态自扫证据，**证据件 0 动**） |
| 溯源核查脚本 + 输出对 | 4 | `_rj5_convention_check_2026_09_27.py` + `.out.json` / `_rj5_mapping_test_2026_09_27.py` + `.out.txt`（背 `20f15c49feb5` 溯源件，**证据件 0 动**） |
| 诊断输出 | 1 | `_v3r1_diag.json`（背 `735c03db1ae9` v3r1 结果件，**证据件 0 动**） |
| **合计** | **22** | **与清后盘上实测 22 件全等 ✓** |

> **同一性重复登记（防重复计数）**：`_recheck_r1_runA.log` 与 `_recheck_r1_runB.log` SHA-12 同为 `68c85cf076d1`；`_recheck_r1_runC.log` 与 `_recheck_r1_runD.log` SHA-12 同为 `b15384cff9f0`。⇒ **4 件实为 2 份内容同哈希**（同 runner 重复跑），**如实列全 4 件但计为 2 份内容**，件数仍按盘上 22 计。
> **本棒修正记录（仪器先审自己）**：本表初稿把「runner 配对日志」误记为 **10 件**、合计误记 **23 件**，并以一段叙述去解释 22 vs 23 的差。复核实为**表格自身算错**（`_recheck_r1_run*.log` 为 5 件而非 6 件），**非口径差异、非盘上差异**。已直接改正表格为 9 / 22，**不以叙述掩盖算错**。

### C.5 非今日 `.tmp` 件（54 件）· 本棒 0 动

- 分布：mtime 09-24 / 09-25 / 09-26
- **处置立场**：派工单本棒口径明写「`.tmp` 内**今日**临时探针件」，故非今日件**不纳入本棒清理范围**，54 件全部原样保留
- 含 v6 ledger §2 关键链 3 件（`.tmp/_l14v3_aggregated_10cells_v4.json` / `_l14v3_n26_metrics_v2.json` / `_l14v3_sensitivity_v2.json`）—— 已按 SHA-12 全等复验，**0 触动**（§F.4）
- **挂账**：54 件是否清理 / 归档，留 PI 另行处置（见 §E.4）

---

## D. ④ 计数校正 · V4 收尾整理时点

### D.1 三口径定义（沿用锚件 `71e9cc179bec` §B.1 字面，0 改定义）

| 口径 | 定义 | 实测命令 |
|---|---|---|
| **主目录** | `D:\私人资料\deposon-repo\` 下递归所有文件，**排除 `.git/`** | `Get-ChildItem -Recurse -File -Force \| Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }` |
| **通用口径** | 主目录基础上再排除 `.tmp/` 子树 + `__pycache__/` 子树 + `.pyc/.log/.bak/.tmp/.swp/.part` 扩展名 | 主目录查询上叠加排除 |
| **含临时区口径** | = 主目录全量（含临时区文件） | 同主目录查询 |

> **定义自洽性**：`主目录` 与 `含临时区口径` 按字面为**同一集合**（同一查询），故两值**必须恒等**。本棒实测 1,144 / 1,144 ✓ 恒等成立。
> **对 11:47 锚件的一处修正**：锚件 §E.1 曾把「986 ≠ 1,004」读作**两个口径的定义冲突**。本棒实测证明二者是**同一口径（主目录全量）在两个时点的读数**（见 §D.2），非定义冲突。**测量仪器先审自己**——此为对前棒读数的勘误，**不回改锚件历史行**。

### D.2 三口径计数时间序列（4 时点）

| 时点 | 主目录 | 通用口径 | 含临时区 | 临时区（主−通用） | 三目录 REPO/ARCH/SUB |
|---|---:|---:|---:|---:|---|
| 2026-09-26 19:09（v6 ledger 实测后） | **986** | 未登记 | = 986 | 未登记 | **986 / 1,669 / 467** |
| 2026-09-26 19:50（快照基线） | **1,004** | **930** | = 1,004 | 74 | — |
| 2026-09-27 11:47（晨间锚件 `71e9cc179bec`） | **1,009** | **917** | = 1,009 | 92 | — |
| 2026-09-27 18:05:59（清后） | **1,143** | **1,008** | = 1,143 | 135 | **1,143 / 1,696 / 467** |
| 2026-09-27 18:15（本棒终测，+2 helper） | **1,144** | **1,008** | **1,144** | 136 | **1,144 / 1,696 / 467** |
| **写入本台账 + 落盘自扫器（+2 件）** | **1,146** | **1,009** | **1,146** | 137 | **1,146 / 1,696 / 467** |

> **终态口径说明（诚实交代）**：本棒共新建 **3 件**审链工具（`results/_v4_day_inventory_measure_2026_09_27.py` 1 件进主目录 + `.tmp/_run_frozen_0touch_verify_2026_09_27.py` / `.tmp/_run_day_inventory_table_2026_09_27.py` / `.tmp/_run_final_selfscan_2026_09_27.py` 3 件进 `.tmp`）**+ 本台账 1 件**。终值 **1,146** 已于落盘后实测复验 ✓。
> **计数是移动靶**：`python` 每跑一次 `.tmp` 内脚本都可能新增 `__pycache__` 字节码（计入临时区、**不**计入通用口径）。故本表取**具体时点**读数，**PI 复核时须同口径重测**，不同步数会差 1–2 件属正常副产物噪声，**非计数错误**。

**仪器交叉自检**：PowerShell `Get-ChildItem -Recurse -File -Force` 与 Python `os.walk` 两独立实现**同读 1,144 件 / 35,368,794 B**（全等）✓

### D.3 三目录（主 / 归档 / 副）计数现状

| 目录 | 路径 | 件数 | 字节 | 对 v6 ledger（09-26 19:09） |
|---|---|---:|---:|---|
| **主** | `D:\私人资料\deposon-repo` | **1,144** | 35,368,794 | 986 → **+158** |
| **归档** | `D:\私人资料\_non_upload_local_archive` | **1,696** | 338,433,933 | 1,669 → **+27** |
| **副** | `D:\私人资料\deposon-sub` | **467** | 34,337,769 | 467 → **0** ✓ |

> **口径对齐实证**：v6 ledger §0 记 `SUB=467`，本棒实测 `SUB=467` **逐件全等** ⇒ 本棒计数方法与既有建制口径**一致**，delta 可跨棒比较。
> **归档 +27 / 副 0**：归档增量来自 09-26 19:09 之后的归档动作；副目录本棒**0 写入**（铁律：仓外目录只读 0 写入，本棒对 `_non_upload_local_archive` 与 `deposon-sub` **全程只读**）。

### D.4 delta 归因：晨间 11:47 → 本棒终测 18:15

**恒等式**：`通用 delta = 主目录 delta − 临时区 delta`

| 项 | 件数 |
|---|---:|
| 晨间基线（11:47 主目录） | 1,009 |
| ＋ 今日新建件（ctime = 09-27，全域，实测） | +137 |
| − 本棒清走 `.tmp` 一次性探针 | −10 |
| ＝ 小计 | **1,136** |
| **实测终值** | **1,144** |
| **未归因差额** | **+8** |

> **未归因 +8 老实交代**：ctime-今日 137 件中，`.tmp` 24 / `__pycache__` 13 / `deposon_team` 6 / `verifier` 1 / `results` 90 / `letters` 3 分布实测在盘；差额 8 件在 11:47→18:15 窗口内被创建后又被移走（`.tmp` 清走仅 10 件且已逐件登记，**故另有 8 件非本棒所删**）。**可能来源（未验证，不推定）**：(a) 11:47 基线 1,009 自身虚高；(b) 并发棒在窗口内创建又清理的中间件；(c) `Move-Item` 移出主目录至仓外。**PI 复核路径**：`Get-ChildItem -Recurse -File | Where-Object CreationTime -ge '2026-09-27 11:47' | Sort-Object LastWriteTime` 逐件核。

**临时区 delta 归因**（92 → 136 = +44）：

| 子类 | 11:47 | 18:15 | delta |
|---|---:|---:|---:|
| `.tmp/` 子树 | 54 | 77 | +23 |
| `__pycache__/` 子树 | 0（锚件口径记为 0，`.pyc` 散落 19） | 42 | +42 |
| `.pyc` 散落 | 19 | 0 | −19 |
| `.log` 散落 | 19 | 19 | 0 |
| **临时区合计** | **92** | **136** | **+44** |

> **口径读数修正（仪器自审）**：11:47 锚件把字节码记作「`__pycache__` 子树 0 + `.pyc` 散落 19」；本棒实测为「`__pycache__` 子树 42 + `.pyc` 散落 0」。二者**字节码族合计 19 → 42** 方向一致，差异源于锚件按**扩展名**分桶、本棒按**路径段**分桶。**字节码族本身净增 +23**（今日 executor 密集跑产生），**0 件凭空消失**。此为分桶口径差异，**非计数错误**。

---

## E. 挂账计数类差额 · 一次性校正登记

> PI 2026-09-27 拍板：「文件数一类均 V4 收尾并整理时再校正」——本节即该时点，**穷尽清点**此前全部挂账计数项，分族结清。

### E.1 挂账 5 项总表

| # | 挂账项 | 域 | 校正结论 | 证据强度 |
|:-:|---|---|---|:-:|
| 1 | **986** | 主目录件数 | ✅ **对清** | 强（v6 ledger 字面 + 口径交叉验证） |
| 2 | **1,004** | 主目录件数 | ✅ **对清** | 强（时间序列自洽 + 口径交叉验证） |
| 3 | **994** | 主目录件数 | ❌ **不能对清**，如实留档 | 弱（盘上无任何登记来源） |
| 4 | **−13**（通用口径负 delta） | 主目录件数 | ✅ **对清**（算术恒等闭合） | 强（4 点算术自洽） |
| 5 | **账式 85 vs 77** | **数据集事件数**（≠ 文件数） | ✅ **对清**（盘上账式字段） | 强（dataset JSON 字面） |

### E.2 986 — 对清 ✓

- **盘上来源**：`results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` L12「实测前 1,131 → 实测后 **986**」+ L33「三目录终数 **REPO=986 / ARCH=1669 / SUB=467**」+ L34「REPO <1000 达成」
- **时点**：2026-09-26 19:09 前后（v6 ledger 自记 19:09 校验 v5 健在）
- **口径判定**：= **主目录全量**（同本棒口径）
- **交叉验证**：该 ledger 的 `SUB=467` 与本棒实测 `SUB=467` 逐件全等 ⇒ 同一计数方法
- **定案**：**986 = 2026-09-26 19:09 主目录全量读数**。挂账「986 vs 994 vs 1,004 差额 18」实为**同一口径的时序读数差**，非三套口径冲突。**对清。**

### E.3 994 — 不能对清（如实留档）

- **盘上检索**：`grep \b994\b` over `results/**/*.md` → 命中项**全部为字节数**（`14,994` / `11,994` / `29,484` 等），**无一处为「994 件」的计数登记**
- **三目录 ledger v1–v6 全系**（`4025E871726B` / `64C4EF850025` / `8F5136E176B8` / `272E8C752406` / `CC498BC28525`）**均无 994 字面**
- **位置推断（标为推断，非证据）**：994 落在 986（19:09）与 1,004（19:50）之间，**与「同口径中间时点读数」相容**
- **定案**：**994 无盘上登记来源，不能对清。** 不编造来源、不反推虚构成因。如实留档，挂 PI 处置。
- **注（诚实修正）**：11:47 锚件 §E.2 曾记「本审链未在盘上找到 986/930/1004 字面」——本棒**找到了 986 与 1,004 的盘上来源（v6 ledger + 时序）**，故该灰区**部分收口**；**994 仍无来源，灰区保持开放**。

### E.4 −13（通用口径负 delta）— 对清 ✓（算术闭合）

**恒等式**（`通用 = 主目录 − 临时区`，两时点相减）：

| 时点 | 主目录 | 通用 | 临时区（= 主 − 通） |
|---|---:|---:|---:|
| 09-26 19:50 | 1,004 | 930 | **74** |
| 09-27 11:47 | 1,009 | 917 | **92** |
| **delta** | **+5** | **−13** | **+18** |

**验算**：`+5 − (+18) = −13` ✓ **恒等式精确闭合，无残差。**

- **根因（方向性，附机制推断）**：临时区增速（+18）**远超**主目录交付件增速（+5）。临时区增量主体为**字节码族**（`__pycache__` / `.pyc`）与 `.log`——09-27 上午至下午密集执行 executor，每次 import 生成 `.pyc`，每次跑批生成 `.log`。**这些是运行副产物、不是研究交付件**，故主目录只 +5 而临时区 +18。
- **性质判定**：**不是**「通用口径掉了 13 件研究件」，**不是**文件丢失。**无任何交付件被删**——本棒 0 触动自证（§F.4）19/19 全等即反证。
- **定案**：**−13 = 临时区副产物增速跑赢交付件增速的算术后果，非缺件。** 前棒 §D.5 列的 4 个假说（(a) 基线含 `.tmp` 部分件 / (b) 15 件被移出主目录 / (c) 过滤器误用 / (d) 基线字面不符）**均不成立**——(c) 已排除（本棒 Python + PowerShell 双实现全等）；(b) 不成立（若有交付件被移出，本棒 ctime-今日 137 件 + 盘点 94 件会缺）；真因即临时区副产物增速。**对清。**

### E.5 账式 85 vs 77 — 对清 ✓（且**不是**文件数）

> **PI 归口校正**：此项原与 986/994/1,004 并列为「文件数一类」，**本棒实测证明它属不同域**——是**数据集事件数**账式，非盘上文件件数。

**盘上字面**（`results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` · `accounting_balance_conservation`）：

```
v2_baseline_N                    = 72
post_v2_added                    =  8
d4_added                         =  5
total_events                     = 85
v3_formal_experiment_substrate   = 77
accounting_formula = "72 (v2 baseline) + 8 (D3 wave2/3 post-v2) + 5 (D4) = 85 events;
                      substrate 77 = 64 v2 on-disk + 8 post-v2 in load + 5 D4"
```

**差额 8 件归因**：`85 − 77 = (72 − 64) = 8` ⇒ **8 件 v2-baseline 事件「在账不在盘」**（计入全量 accounting，未进入正式实验 substrate）。

| 口径 | 值 | 含义 |
|---|---:|---|
| 全量 accounting | **85** | 72 基线 + 8 post-v2 + 5 D4 |
| 正式实验 substrate | **77** | 64 基线在盘 + 8 post-v2 + 5 D4 |
| **差额** | **8** | **记账口径差**（基线在盘 64 vs 基线全量 72） |
| **是否缺件** | **否** | **0 件文件缺失**；8 件是**口径外事件**，非丢失制品 |

**回指挂账出处**：`results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` L229「U-4 §1.4.2 分母 85 vs 77 差额 8 件的归因 — 本件立场：**0 追问、0 归因**（沿 PI 2026-09-27 计数类账目归「V4 收尾整理」）；0 阻塞本件」+ L121「缺口账式（起点 = `dataset v1.2` 字面 85 events 记账 / 77 RUN）」。**本棒即该「V4 收尾整理」时点，故在此一次性结清并回指。**

**⚠ 资产缺陷登记（只登记，不代修）——归因叙述不一致**：

| 出处 | 对同一 8 件的叙述 |
|---|---|
| `results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md:334` | 「v3 substrate=77 RUN + **8 D1 missing declared absent** = 85 accounting」 |
| `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json`（`accounting_formula`） | 「**72 (v2 baseline)** + 8 + 5 = 85；substrate = **64 v2 on-disk** + 8 + 5」⇒ 差 8 = **基线 72 中 64 在盘** |

- **两处差额同为 8，但归因叙述不同**：一者称「D1 missing declared absent」，一者称「v2 基线在盘数不足 8」
- **性质**：**叙述层不一致**（数值层 85/77/8 三者全等，无数字矛盾）
- **处置**：涉及**实验语义归因**，超出资产缺陷层（引用/工件/脚本工程性缺陷）**修复边界** ⇒ **本棒 0 代改**，登记挂 PI 另行处置
- **教训（诚实的根因是不误导）**：拿「8 件 D1 missing」去讲一个实为「基线在盘口径」的问题，就是误导；两说并存且均未撤回，PI 复核时应指定唯一权威叙述

### E.6 本棒新登记的未归因项

| # | 项 | 值 | 状态 |
|:-:|---|---:|---|
| U-1 | 主目录 delta 归因残差 | **+8** | 如实登记，不推定成因（§D.4） |
| U-2 | **994** 盘上来源 | 无 | 如实留档（§E.3） |
| U-3 | 8 件差额归因叙述不一致 | 2 说并存 | 只登记，0 代改（§E.5） |
| U-4 | `.tmp/` 非今日件 | 54 件 | 本棒 0 动，留 PI 处置（§C.5） |
| U-5 | `__pycache__` / `.pyc` 分桶口径 | 19 → 42 | 已判为分桶口径差、非计数错误（§D.4）；字节码净增 +23 待 PI 定是否纳入常规清理 |
| U-6 | **2 件** ctime-今日件窗口内消失 | 2 | 18:02 实测 ctime-今日 145 → 18:15 实测 137，且本棒清走仅 10 件 ⇒ 另有 2 件非本棒所删；**不推定成因** |

---

## F. 老实交代 · 自证

### F.1 skill 缺位（按纪律锚 fallback）

- 派工要求 `scientific-research-workflows:statistical-analysis`（plugin `@scientific-research-workflows`）
- **加载实测**：`Local skill not found: scientific-research-workflows:statistical-analysis`
- **plugin 缓存实测**：`C:\Users\Administrator\.minimax\plugins\` 实测**空目录**（0 项）；`C:\Users\Administrator\.minimax\` 全盘递归检索 `scientific` 命名的 skill / plugin 目录 → **0 命中**
- **处置**：沿 v15 erratum `6844BF36F762` §20.7 末段先例 + `71e9cc179bec` §E.6 既有口径，**按 fallback 纪律锚字面格式**执行
- **未编造** skill 不存在的任何虚构指令

### F.2 只读边界（仓外 0 写入）

- `_non_upload_local_archive`（归档）：**1,696 件全只读**，0 写入 / 0 移动 / 0 删除
- `deposon-sub`（副）：**467 件全只读**，实测 467 与 v6 ledger **全等**，0 变动 ✓
- 主目录内改动**仅 2 类**：① 新建本棒审链件（本件 + 盘点实测器）② 授权范围内 `.tmp` 10 件可恢复删除

### F.3 派生 JSON 不合并

- 本棒**未合并、未改写**任何派生 JSON；`5118f5b44f17` / `cbf60a630c9f` / `990c0c42a6f6` / `6eed9acdb99a` / `ed596914259a` 等今日 dataset 派链条**逐件 0 触动**（只算 SHA-12）

### F.4 0 触动自证（19/19 SHA-12 全等，触动数 = 0）

| # | 锚件 | 字节 | SHA-12（实测） | 期望 | 判定 |
|:-:|---|---:|:-:|:-:|:-:|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | `03C6C01F3697` | `03C6C01F3697` | ✓ 未触动 |
| 2 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169,864 | `1D52DB0EBF53` | `1D52DB0EBF53` | ✓ 未触动 |
| 3 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192,160 | `29A853444D42` | `29A853444D42` | ✓ 未触动 |
| 4 | `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52,153 | `B34B9F7BDFB7` | `B34B9F7BDFB7` | ✓ 未触动 |
| 5 | `results/_ghostref_copy_log_2026_09_23.json` | 129,780 | `8CD133D0896F` | `8CD133D0896F` | ✓ 未触动 |
| 6 | `results/_archive_manifest_non_upload_2026_09_23.json` | 148,690 | `B899103853CA` | `B899103853CA` | ✓ 未触动 |
| 7 | `results/_v4_supp_t15r2_verdict.md` | 64,145 | `8355724A26E3` | `8355724A26E3` | ✓ 未触动 |
| 8 | `results/_v4_supp_t15r2_result.json` | 73,526 | `C69AB0E3002E` | `C69AB0E3002E` | ✓ 未触动 |
| 9 | `results/_v4_supp_t15r2_executor.py` | 84,884 | `4B5B720D5CDA` | `4B5B720D5CDA` | ✓ 未触动 |
| 10 | `results/_v4_supp_l14v3_n26_verdict.md` | 64,485 | `F4435801D09F` | `F4435801D09F` | ✓ 未触动 |
| 11 | `results/_v4_supp_l14v3_batch10_r5_result.json` | 74,979 | `7F02E08FC0DA` | `7F02E08FC0DA` | ✓ 未触动 |
| 12 | `results/_v4_supp_l14v3_batch9_r5_result.json` | 72,047 | `1610F5060EF1` | `1610F5060EF1` | ✓ 未触动 |
| 13 | `results/_v4_supp_t1_verdict.md` | 27,538 | `F1B5E49F3058` | `F1B5E49F3058` | ✓ 未触动 |
| 14 | `results/_v4_supp_t15_verdict.md` | 52,884 | `52C985429C91` | `52C985429C91` | ✓ 未触动 |
| 15 | `.tmp/_l14v3_aggregated_10cells_v4.json` | 2,233,138 | `66A9B8B3DABF` | `66A9B8B3DABF` | ✓ 未触动 |
| 16 | `.tmp/_l14v3_n26_metrics_v2.json` | 2,579 | `EB9CE9683AD3` | `EB9CE9683AD3` | ✓ 未触动 |
| 17 | `.tmp/_l14v3_sensitivity_v2.json` | 2,292 | `DCAA4B6B3B0B` | `DCAA4B6B3B0B` | ✓ 未触动 |
| 18 | `results/_v4_maindir_count_monitor_2026_09_27.md`（**本棒纪律锚**） | 15,313 | `71e9CC179BEC` | `71E9CC179BEC` | ✓ 未触动 |
| 19 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md`（**本棒纪律锚**） | 37,629 | `CC498BC28525` | `CC498BC28525` | ✓ 未触动 |
| | **合计** | | **MATCH = 19** | | **MISMATCH = 0 · 触动数 = 0** |

> 18 frozen 锚 + 3 `.tmp` 关键链 + 2 本棒纪律锚全等。**勘误只追加**：`71e9cc179bec` §E.1 的定义冲突读法、`§E.2` 的「986/1,004 无盘上来源」结论**均不回改历史行**，修正记于本件 §D.1 / §E.2 / §E.3。

### F.5 key 形态自扫（CLEAN）

- **严格 pattern**：`\b(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer\s+[A-Za-z0-9]{20,}|tp-[a-z0-9]{20,}|ark-[a-z0-9-]{20,})\b`
- **宽 pattern**（追加 `api_key =` / `Authorization: Bearer` 赋值形）：`\b(...|api[_-]?key\s*[=:]\s*["'][^"']{16,}|Authorization\s*:\s*Bearer\s+\S{16,})\b`（IGNORECASE）
- **扫描面**：今日盘点 94 件全量（mtime = 09-27 · results/letters/docs）
- **结果**：**严格 0 命中** ✓ / **宽 0 命中** ✓ ⇒ **CLEAN**
- **本棒自身**：落盘后复扫本件 ⇒ 0 命中
- **R4 key 永不明文无例外**：本棒全程**未读取任何 key 值**，无 key 入 prompt / JSON / log

### F.6 老实交代清单（不藏）

| # | 项 | 交代 |
|:-:|---|---|
| 1 | skill | `scientific-research-workflows:statistical-analysis` **本地不存在**，已按纪律锚 fallback；**未编造** skill 内容 |
| 2 | 994 | **无盘上来源，不能对清**；不编造来源、不反推成因 |
| 3 | U-1 delta 残差 +8 | 11:47→18:15 窗口内 8 件创建后被移走，**非本棒所删**；**不推定成因** |
| 4 | U-6 | 另有 **2 件** ctime-今日件在实测窗口内消失；**不推定成因** |
| 5 | 85/77 归因叙述 | 两说并存（`41d29f4deb70` vs `ed596914259a`），**涉及实验语义，0 代改** |
| 6 | 分类器缺陷 | 首轮把 10 件目录嵌套件误判「未归类」；**已修仪器**（改按全路径匹配），复测 0 未归类。**如实记录仪器缺陷，不掩盖** |
| 7 | 保留件数 | C.4 表初稿把 run 日志误记 10 件、合计误记 23 件并以叙述掩盖；**已查明为表格自身算错**，直接改正为 **9 / 22**（与盘上实测全等） |
| 8 | 字节码分桶 | 11:47 锚件按扩展名分桶、本棒按路径段分桶；**字节码族净增 +23，非凭空消失** |
| 9 | 非今日 `.tmp` 54 件 | 派工口径为「今日」，**本棒 0 动**，留 PI |
| 10 | succeeded ≠ 跑完 | 本件以**落盘 + SHA-12 实测 + 0 触动 19/19 + key CLEAN** 四项齐备为准宣告；succeeded 状态**不作完成凭据** |
| 11 | 本件自身 | 本台账 + 3 件审链工具计入后，**终态 = 1,146 / 1,009 / 1,146**（见 §D.2 末行；已落盘后实测复验 ✓）。**计数为移动靶**：`python` 跑 `.tmp` 脚本会新增字节码（入临时区、不入通用口径），不同步重测差 1–2 件属副产物噪声 |

---

## G. 报告元数据

| 项 | 值 |
|---|---|
| **路径** | `results/_v4_day_inventory_2026_09_27.md` |
| **性质** | 新建独立审链登记件（V4 收尾整理时点 · 四件套 ③，并汇总 ①②④） |
| **派工** | evidence-auditor（agent-11335500b168）· 派工单「今日收尾文件夹四件套」 |
| **触发** | PI 2026-09-27「今日收尾阶段记得整理文件夹四件套」+ PI 早前「文件数一类均 V4 收尾并整理时再校正」 |
| **配套件** | `results/_v4_day_inventory_measure_2026_09_27.py`（盘点实测器 · 8,226 B）<br>`.tmp/_run_frozen_0touch_verify_2026_09_27.py`（0 触动复验器）<br>`.tmp/_run_day_inventory_table_2026_09_27.py`（台账表生成器）<br>`.tmp/_run_final_selfscan_2026_09_27.py`（落盘后 key 自扫器） |
| **纪律锚** | `71e9cc179bec`（晨间计数监控）+ `CC498BC28525`（cleanup moves ledger v6） |
| **边界** | R5 frozen 只追加 / V1–V3 只读 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文无例外 / 仓外只读 0 写入 |
| **自证** | 0 触动 **19/19 全等**；key 形态严格 0 命中 + 宽 0 命中 → **CLEAN** |
| **skill** | `scientific-research-workflows:statistical-analysis`（**缺位**，已 fallback，未编造） |
| **状态** | 本审链登记件自身待 PI 复核生效；生效即锁；事后不重开不调 |

---

*出件：Mavis 团队 evidence-auditor（`agent-11335500b168`）｜2026-09-27*
