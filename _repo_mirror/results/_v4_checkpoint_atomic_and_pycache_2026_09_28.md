# V4 收口修复+清理棒｜checkpoint 原子写 + `__pycache__` 全清

- 日期：2026-09-28
- 派工：Mavis（root session）｜派工单「收口修复+清理棒（worker）：checkpoint 原子写＋pycache 全清」
- 出件：**Mavis 团队 worker**（agent: worker）
- 拍板依据：`ask_79fd9fad41e57ba8040361a8` q3/q4（8 个 `__pycache__` 目录下棒全清；checkpoint 非原子写按下棒加，cpath_r1 同款处方）
- 场景：worker｜执行类（跑修复 / 做处置 / 落证据）
- 哈希算法：`hashlib.sha256(...).hexdigest()[:12]`，**小写**（禁内建 `hash()`）
- 铁律执行：**0 LLM / 0 proxy**（纯本地 hashlib + re）｜**key 永不明文**（§6 自扫 0 命中）｜新名件不覆盖｜清理走 **mavis-trash 可恢复删除**（0 永久删除）｜**0 改阈值字面 / 0 改实验逻辑 / 0 改返回值**｜frozen 贴邻件 0 触动（§5）

---

## §0 结论速览

| # | 派工项 | 实测口径 | 动作 | 结果 |
|:-:|---|---|---|:-:|
| 1 | checkpoint 原子写修复 | 全仓非原子 JSON 覆盖写落盘件 **51 件**（checkpoint 类 **5** / 终端产出类 46） | checkpoint 类中可新名者出 **2 件 `_r2_atomic` 新名件**；被引/归档 3 件 + 终端产出类 46 件**登记不修** | ✅ 完成（验证 **22/22 PASS**） |
| 2 | `__pycache__` 8 目录全清 | **33 件 `.pyc` / 1,898,147 B**（清前逐件 SHA-12 登记，§4.1） | 逐目录 `mavis-trash` **可恢复删除** | ✅ 完成（8/8 GONE，全仓 0 残留） |
| 3 | frozen 0 触动自证 | 18 frozen 清前 **18/18 PASS** → 清后 **18/18 PASS**，**触动数 = 0** | 只读复算 | ✅ 完成（§5） |

**修复件（2 件新名）**

| 新名件 | 字节 | SHA-12 | 源件（0 触动） |
|---|---:|---|---|
| `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | 92,915 | `215db16a0556` | `_v4_supp_t15r2_executor_r1_2026_09_28.py`（90,390 B / `e0936a68fa82`） |
| `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | 70,056 | `9e89e021ea03` | `_v4_supp_t15_executor_r1_2026_09_27.py`（67,517 B / `6d22444c65af`） |

**证据件（`.tmp` 脚手架，可复算）**

| 件 | 字节 | SHA-12 |
|---|---:|---|
| `.tmp/_cpatomic_pycache_pre_2026_09_28.json`（清前登记，**后续 0 覆盖**） | 10,772 | `0f62453472b7` |
| `.tmp/_cpatomic_pycache_post_2026_09_28.json` | 6,476 | `1eb3c5c9c62d` |
| `.tmp/_cpatomic_verify_2026_09_28.json`（22 项验证结果） | 3,144 | `6b820f7da4a4` |
| `.tmp/_cpatomic_register_2026_09_28.json`（全仓非原子写登记 51 件） | 29,361 | `b68d7ff817bb` |
| `.tmp/_cpatomic_keyscan_2026_09_28.json`（key 自扫） | 2,672 | `b4e45cffa5cd` |
| `.tmp/_cpatomic_patch_manifest_2026_09_28.json` | 357 | `cdb8ebc2ece3` |
| `.tmp/_cpatomic_pycache_pre_2026_09_28.py` | 3,912 | `b86619676bf4` |
| `.tmp/_cpatomic_pycache_post_2026_09_28.py` | 5,164 | `171b2a31c0e1` |
| `.tmp/_cpatomic_make_fix_2026_09_28.py` | 7,796 | `76c822b640a0` |
| `.tmp/_cpatomic_verify_2026_09_28.py` | 11,036 | `85139011457c` |
| `.tmp/_cpatomic_keyscan_2026_09_28.py` | 3,074 | `393a8d3fa68f` |
| `.tmp/_cpatomic_register_2026_09_28.py` | 6,322 | `98fe9fa24e80` |

---

## §1 勘察面：全仓非原子 JSON 覆盖写登记

### §1.1 判定口径（写死，0 主观）

| 概念 | 判据 |
|---|---|
| **原子写** | 写同目录临时件 + `flush` + `os.fsync` + `os.replace`（同卷原子替换）三段式 |
| **非原子** | 以 `"w"` 模式直接写**目标路径本身**，0 临时件、0 replace |
| **checkpoint 类** | 增量/续跑状态落盘 —— 被 `load_*` 读回以决定 skip / 续跑；**崩半路即损已累计状态** |
| **终端产出类** | 跑完一次性交付 JSON；崩半路只损本次产出，**不损已累计状态** |

扫描实现：`.tmp/_cpatomic_register_2026_09_28.py`（`re` 命中 `json.dump(…, open(…,"w"))` 与 `.write_text(json.dumps(…))`，并剔除目标本身为 `.tmp*` 的已具备三段式者）。

### §1.2 勘察结论

- **非原子 JSON 覆盖写落盘件 = 51 件**：**checkpoint 类 5 件** + 终端产出类 46 件。
- **checkpoint 类 5 件全部在 T15/T15r2/L14 系**（本棒点名重点面），逐件见 §2.3 / §3.1。
- **`.tmp` runner 类**：派工点名「`.tmp` runner 类」为勘察重点。**实测 `.tmp` 内 0 件 checkpoint 写入面** —— `.tmp` 内非原子写 8 件全为终端产出类（`_run_v3r1_relabel.py` 3 面、`_t15_update_result.py` 1 面覆盖写被引交付件 `results/_v4_supp_t15_result.json`、`_r4_key_scan_r1_files_2026_09_27.py` 1 面，及本棒 6 件自有脚手架）。`.tmp` 内对 checkpoint **只读不写**（`_t15r2_verify.py` / `_t15_update_result.py` 等为读面）。
- **`deposon_team/plugins/` 面**：`_v3n_cpath_live_2026_09_27.py`（`5248ba7ac21c`，与 V3 勘误链 E-15 记值一致 ✓）1 处 = **已由 `_r1` 同款处方修复过**；其 `_r1` 件（`321d39c7df41`）实码 L277 走 `_atomic_write_json`，正则命中的 L18 / L246 **在缺陷说明注释行内**，属**注释假阳**，非活代码（已逐行确认）。

---

## §2 修复：checkpoint 原子写（cpath_r1 同款处方）

### §2.1 缺陷面与处方来源

**主修目标**：`results/_v4_supp_t15r2_executor_r1_2026_09_28.py` L553-556

```python
def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:
    T15R2_CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False),
                                     encoding="utf-8")     # ← 非原子全量覆盖写
```

该缺陷**由件自身登记**：同件 L477-479 自述 `(c) save_t15r2_records 为**非原子写** … 正是 (a)(b) 的触发源。**本棒只登记不修**`。PI 本棒拍板「按下棒加（cpath_r1 同款处方）」⇒ 本棒执行修复。

**危害面（不误导提示，写明根因链）**：`.tmp/_t15r2_records.json` 是 T1.5r2 的 62 条 records 唯一落盘面；该件 L470-473 自记后果 = 「`load_t15r2_records` 静默 `[]` ⇒ `cmd_aggregate` 照常产出 result.json，但 `records_all` 少掉 T1.5r2 全集 ⇒ **K-N11-N1_T1relax 的 N_min=10 字面 PASS 根因消除结论被无声抽掉**，字面读起来仍像「已跑完」」。**R1 让损坏可见（响亮告警），R2 让损坏不发生（原子写）—— 二者互补，缺一不闭合。**

**第二修目标**：`results/_v4_supp_t15_executor_r1_2026_09_27.py` L522-525 `save_checkpoint` —— 同款缺陷，checkpoint = `.tmp/_t15_records.json`（120 条 T1.5 状态锚）。该件缺陷面为 T1.5r2 件 L474-476 所记 `(b)` 面的载体：状态锚消失 ⇒ `ok_keys` 骤降 ⇒ **续跑重复计 calls 账**。

### §2.2 处方（逐字沿 cpath_r1）

沿 `deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py` L233-240：

```python
def _atomic_write_json(obj, path, indent=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.tmp_{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)      # 同卷原子替换: 要么全量新内容, 要么原内容
```

**边界（0 改实验逻辑）**：0 改调用面 / 0 改返回值 / 0 改阈值字面（`0.85` / `0.05` / `0.05` / `TH-T1-1=10`） / 0 改 `N_REASKS` / 0 改 cells 矩阵 / 0 改 kill-line / 0 改 records 结构 / 0 改 paths。`json.dumps` 参数逐字沿用，**落盘字节与修复前逐字节同构**（T1 实测证）。

临时件名带 **pid** ⇒ 并发进程互不踩踏（T2 实测证）。

### §2.3 修复 vs 登记分界

| checkpoint 类件 | 字节 | SHA-12 | 落盘点数 | 处置 | 依据 |
|---|---:|---|---:|---|---|
| `_v4_supp_t15r2_executor_r1_2026_09_28.py` | 90,390 | `e0936a68fa82` | 3 | **FIXED → 新名件**（原件 0 触动） | 可新名；缺陷由件自身登记待修 |
| `_v4_supp_t15_executor_r1_2026_09_27.py` | 67,517 | `6d22444c65af` | 3 | **FIXED → 新名件**（原件 0 触动） | 同上；`.tmp/_t15_records.json` 为活状态锚 |
| `_v4_supp_t15r2_executor.py` | 84,884 | `4b5b720d5cda` | 3 | REGISTER_NO_FIX | 被引（R1 前身，被 R1 与 verdict 引用） |
| `_v4_supp_t15_executor.py` | 62,285 | `558e635f9ba6` | 3 | REGISTER_NO_FIX | 被引（T15 verdict 记 `558E635F9BA6`） |
| `_archive_2026_09_24/l14_runner_v2.py` | 23,056 | `acf1cd6ccbd4` | 2 | REGISTER_NO_FIX | 归档件 + 被 L14 verdict §9.1 引用 |

**分界原则（派工单口径「只修未被引/可新名者；被引件登记不修」）**：原件一律 0 字节改动；修复只以**新名件**交付。**被引件不原地改**（原地改 = 制造幽灵引用 + 破 SHA 链）。

两新名件**剩余的 2 处非原子写**均为**终端产出类**（`T15R2_PROBE_LOG_PATH` / `T15R2_RESULT_PATH` / `PROBE_LOG_PATH` / `RESULT_PATH`），**不在本棒修复面**（崩半路只损本次产出、不损已累计 checkpoint 状态），登记不修，逐字节位置见 §3.2。

### §2.4 验证：22/22 PASS（`6b820f7da4a4`）

沙箱 = `.tmp/_cpatomic_scratch/`（跑完已 `mavis-trash` 清走）；全部 `python -B` + `sys.dont_write_bytecode` ⇒ **0 新生 `__pycache__`**。

| 组 | 测试 | t15r2 件 | t15 件 | 判据 |
|---|---|:-:|:-:|---|
| **T1** | 原子写落盘字节 == 原非原子写字节 | ✅ | ✅ | 两侧同 `1ce7ab9eb58a` / 141,490 B |
| **T1** | 0 临时件残留 | ✅ | ✅ | `leftovers=[]` |
| **T2** | 双进程并发写同一 checkpoint，`exit=0` | ✅ | ✅ | `rc=[0,0]` |
| **T2** | 终态 = 某一方**完整** payload（0 混合 0 截断） | ✅ | ✅ | `matched=['B']`，1,122,490 B |
| **T2** | 终态可 `json.loads`（0 截断） | ✅ | ✅ | — |
| **T2** | 0 临时件残留 | ✅ | ✅ | `[]` |
| **T3** | 写入中途强杀**确实发生** | ✅ | ✅ | `rc=1 err=''`（无异常输出 ⇒ 确为强杀非崩溃） |
| **T3** | **崩半路既有 checkpoint 逐字节不动** | ✅ | ✅ | seed `157c589b06d9`/83,090 B → after **同值** |
| **T3** | 既有 checkpoint 仍可解析 | ✅ | ✅ | — |
| **T4** | **对照组**（旧写法）中途强杀确实发生 | ✅ | ✅ | `rc=1 err=''` |
| **T4** | **旧写法数据被摧毁 ⇒ 修复非装饰** | ✅ | ✅ | after `c51af9d1cfbf`/12,249,258 B（t15r2）、`284a0f51bfe4`/9,697,098 B（t15），seed 仅 83,090 B，`json_loads_ok=False` |

- **强杀语义**：Windows 无 `SIGKILL`；用 `p.kill()` = `TerminateProcess`（不可捕获，等价语义）。**诚实交代**：故「崩半路」在此为**进程被强杀**，非断电/磁盘写满 —— 后二者无法在本机复现，**不代填**。
- **T4 为何必要（诚实纪律，不误导）**：T1–T3 全 PASS 也可能是「原子写根本没用上」的空过。T4 用**同一沙箱、同一 payload 规模、同一强杀时点**跑旧写法对照，坐实缺陷真实 ⇒ T3 的「数据不动」是修复生效，不是构造假象。
- **过程如实交代（留痕）**：本棒验证脚本自身有 3 处 harness 缺陷，均已修正后重跑，最终结论取自**修正后**的完整 22/22 那一轮：① 控制台 GBK 无法编码 `⇒` ⇒ stdout 强制 UTF-8；② 首版 T4 对照组 `_crasher.py` 漏 `import json` ⇒ 以 `NameError` 提前死（**该轮 T4「数据被摧毁」PASS 不成立，已作废重跑**）；③ 首轮 T2「0 残留」报 FAIL，经查为**观察竞态**（子进程 `exit=0` 后 1 秒内 tmp 尚未被观察到清理），加 1 秒收尾窗口后复跑确认 0 残留。

---

## §3 登记不修（0 擅动）

### §3.1 checkpoint 类 3 件（被引 / 归档）

见 §2.3 表。**处置 = 登记不修**，理由逐件写明（被引 / 归档）。**0 字节改动已复验**（§5.2）。

### §3.2 终端产出类 46 件

全表见 `.tmp/_cpatomic_register_2026_09_28.json`（29,361 B）。摘要：

| 面 | 代表件（SHA-12） | 不修理由 |
|---|---|---|
| `deposon_team/plugins/` | `_v3n_cpath_live_2026_09_27.py` `5248ba7ac21c`、`_v3n_ktb1_distortion_bound_2026_09_27.py` `5572ef4055a5`、`_v3n_pg_boss_live_2026_09_27.py`、`boss_pc_{1,2,3}_*.py` | 一次性跑完的交付 JSON；崩半路不损累计状态 |
| `results/` v3 recheck executor 系 | `_v3_recheck_{01,04,05,08}_executor_*.py` 等 | 被预登记 / rescript / prereg 引用；改写 = 破 SHA 链 |
| 仓根 benchmark runner | `run_benchmark_v1_4_{gsm8k,strategyqa}.py`（**其 `DETAILS_FILE` 已是 tmp+`os.replace` 三段式**，仅 `RESULT_FILE` 为终端产出面）、`run_g2_ensemble.py`、`run_v20_vector_audit.py` | 终端产出面 |
| `llm_fetch.py` L186-189 `save_record` | 缓存记录落盘 | **被 `tests/test_llm_fetch.py` 等测试面依赖**，改动面涉测试契约，超本棒授权 |
| `.tmp/` 脚手架 | `_run_v3r1_relabel.py` `55d06ce42b3d`、`_t15_update_result.py` `ad66f242c6a1` 等 8 件 | 临时区；其中 `_t15_update_result.py` 覆盖写**被引交付件** ⇒ 更须登记不修 |

### §3.3 「未修」是否掩盖风险 —— 不误导提示

不修 ≠ 无风险。**checkpoint 类 3 件被引/归档面仍带非原子写**，其 checkpoint（`.tmp/_t15r2_records.json` / `.tmp/_t15_records.json`）**至今仍是活状态面**。本棒已交付可新名的修复件，但**是否切换执行面属 PI 处置**，本棒 0 代取舍。**如实结论：修复件已就位且验证通过，但在 PI 明示切换前，跑的仍是原件。**

---

## §4 `__pycache__` 8 目录全清

### §4.1 清前逐件 SHA-12 登记（33 件 `.pyc` / 1,898,147 B）

登记表 = `.tmp/_cpatomic_pycache_pre_2026_09_28.json`（`0f62453472b7`）。**逐件登记完成后本棒 0 覆盖该文件**（清后复验另写 `_post`）。

**DIR `.tmp/__pycache__/` — 0 件 / 0 B**（空目录）

**DIR `verifier/kill_lines/__pycache__/` — 0 件 / 0 B**（空目录，贴邻 verifier 面）

**DIR `verifier/audit/__pycache__/` — 1 件 / 27,641 B** ｜⚠ **贴邻 18 frozen 之一 `verifier/audit/conservation.py`**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `conservation.cpython-314.pyc` | 27,641 | `32376299b40f` |

**DIR `results/__pycache__/` — 25 件 / 1,563,285 B**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `_v3_recheck_26b_executor_2026_09_27.cpython-314.pyc` | 55,314 | `f5fbfa3126c7` |
| `_v4_pi_cot_v2_ruleset_v2_executor.cpython-314.pyc` | 59,327 | `eaca6469925c` |
| `_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | 67,049 | `bd231a2482ae` |
| `_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | 69,630 | `e7ab1adbf898` |
| `_v4_supp_l14v3_batch1_executor.cpython-314.pyc` | 31,984 | `8d956eb6b97e` |
| `_v4_supp_l14v3_batch1_r2_executor.cpython-314.pyc` | 34,126 | `0d03f4f85333` |
| `_v4_supp_l14v3_batch1_r3_executor.cpython-314.pyc` | 46,358 | `8846a6df8b7a` |
| `_v4_supp_l14v3_batch1_r4_executor.cpython-314.pyc` | 48,525 | `f6d1473f1621` |
| `_v4_supp_l14v3_batch1_r5_executor.cpython-314.pyc` | 52,830 | `78916ede0872` |
| `_v4_supp_l14v3_batch1_r6_executor.cpython-314.pyc` | 50,606 | `629042265f54` |
| `_v4_supp_l14v3_batch3_r4_executor.cpython-314.pyc` | 67,589 | `67ef0e56fcbf` |
| `_v4_supp_l14v3_batch3_r5_executor.cpython-314.pyc` | 70,314 | `5d9d5bc3b5f6` |
| `_v4_supp_l14v3_batch4_r6_executor.cpython-314.pyc` | 78,250 | `53a5fafe3063` |
| `_v4_supp_l14v3_batch5_r1_executor.cpython-314.pyc` | 62,920 | `a8e130c3b759` |
| `_v4_supp_l14v3_batch5_r2_executor.cpython-314.pyc` | 65,449 | `01a29ec3dad2` |
| `_v4_supp_l14v3_batch5_r3_executor.cpython-314.pyc` | 66,963 | `77ae98fc1ac8` |
| `_v4_supp_l14v3_batch6_r2_executor.cpython-314.pyc` | 55,324 | `106605dcf464` |
| `_v4_supp_l14v3_batch6_r3_executor.cpython-314.pyc` | 55,983 | `be8c31f4d3f5` |
| `_v4_supp_l14v3_batch6_r4_executor.cpython-314.pyc` | 57,153 | `470437c653de` |
| `_v4_supp_l14v3_batch6_r5_executor.cpython-314.pyc` | 60,285 | `49fefa14c065` |
| `_v4_supp_t15_executor.cpython-314.pyc` | 70,099 | `72a379ca1f2a` |
| `_v4_supp_t15_executor_r1_2026_09_27.cpython-314.pyc` | 74,681 | `612fafeb24ca` |
| `_v4_supp_t15r2_executor.cpython-314.pyc` | 95,036 | `239ff51f1523` |
| `_v4_supp_t15r2_executor_r1_2026_09_28.cpython-314.pyc` | 99,075 | `773bb05aa7d0` |
| `_v4_supp_t1_executor.cpython-314.pyc` | 68,415 | `bb75067f0444` |

**DIR `results/_v3_recheck_08b_executor/__pycache__/` — 1 件 / 52,838 B**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `executor_2026_09_27.cpython-314.pyc` | 52,838 | `5dfa39f98d45` |

**DIR `results/_v3_s1_executor/__pycache__/` — 1 件 / 67,735 B**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `executor_2026_09_27.cpython-314.pyc` | 67,735 | `52cc4c06dc4e` |

**DIR `results/_v3_s3_wordexpand_data/__pycache__/` — 2 件 / 93,176 B**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `executor_2026_09_28.cpython-314.pyc` | 48,004 | `dde73101cf15` |
| `executor_r1_2026_09_28.cpython-314.pyc` | 45,172 | `fece5b1e3282` |

**DIR `deposon_team/plugins/__pycache__/` — 3 件 / 93,472 B**

| `.pyc` | 字节 | SHA-12 |
|---|---:|---|
| `_v3n_cpath_live_2026_09_27.cpython-314.pyc` | 31,853 | `828fdcea6bd6` |
| `_v3n_cpath_live_r1_2026_09_27.cpython-314.pyc` | 42,427 | `747aa15e2ec4` |
| `_v3n_pg_boss_live_2026_09_27.cpython-314.pyc` | 19,192 | `648fa1b4f439` |

> **8 目录内非 `.pyc` 件 = 0 件**（逐目录 `non_pyc` 字段实测为空）⇒ 无「混装他件被误清」风险。

### §4.2 处置动作（mavis-trash 可恢复，0 永久删除）

**清理通道**：`C:\Users\Administrator\.minimax\bin\mavis-trash.cmd`（runtime 信任启动器，沿慢处置 B §1.2 同款）。
**处置粒度**：逐**目录**为单元（`.pyc` + 空目录一次清走），沿慢处置 B §3.2 先例。
**回执（8 条逐字）**：

```
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\.tmp\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\verifier\kill_lines\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\verifier\audit\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\results\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\results\_v3_recheck_08b_executor\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\results\_v3_s1_executor\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\results\_v3_s3_wordexpand_data\__pycache__'
mavis-trash: moved to trash: 'D:\私人资料\deposon-repo\deposon_team\plugins\__pycache__'
```

另：验证沙箱 `.tmp/_cpatomic_scratch/` 同通道清走（`moved to trash`），0 永久删除。
本棒自身生成件首版（`results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py`，缩进缺陷版 `64505229f954` / 70,053 B）亦走同通道清走后重生成 ⇒ **0 永久删除、0 覆盖**。

### §4.3 清后复验（`1eb3c5c9c62d`）

| 目标目录 | 清前 `.pyc` | 清后件 | 清后目录 | 判定 |
|---|---:|---:|:-:|:-:|
| `.tmp/__pycache__/` | 0 | 0 | GONE | ✅ |
| `verifier/kill_lines/__pycache__/` | 0 | 0 | GONE | ✅ |
| `verifier/audit/__pycache__/` | 1 | 0 | GONE | ✅ |
| `results/__pycache__/` | 25 | 0 | GONE | ✅ |
| `results/_v3_recheck_08b_executor/__pycache__/` | 1 | 0 | GONE | ✅ |
| `results/_v3_s1_executor/__pycache__/` | 1 | 0 | GONE | ✅ |
| `results/_v3_s3_wordexpand_data/__pycache__/` | 2 | 0 | GONE | ✅ |
| `deposon_team/plugins/__pycache__/` | 3 | 0 | GONE | ✅ |

- **8/8 GONE** ✅｜**清后全仓 `__pycache__` 目录复扫（含本棒脚手架产生面）= `NONE`** ✅
- **语义损失 = 0**：`.pyc` 为**可再生派生物**（`.py` 源件全部未动），删除后下次 import 自动重建。故清走**不影响任何运行结果**，与 09-27 回函 §C.3 受托方口径建议（甲）「随件清理」一致。
- **前提更正（仪器先审自己，如实登记）**：慢处置 B §3.3 把 `results/__pycache__/` 与 `results/_v3_s3_wordexpand_data/__pycache__/` 标注为「含 09-27/09-28 当日新建 `.pyc`，**可能为在跑脚本的活缓存**」。本棒按 PI 拍板「8 目录下棒全清」执行 ⇒ **该「在跑」顾虑已由拍板消解**；但如实登记：**若真有脚本在其运行中被清，其活动缓存已被清走**，因 `.pyc` 可再生，**恢复成本 = 下次 import 自动重建，0 语义损失**。

---

## §5 frozen 0 触动自证

**基线源**：`results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`（18 frozen 逐件 `expected_sha12`）。
**方法**：清前 + 清后**各跑一次**全 18 件 `hashlib.sha256` 复算，逐件对照。

| 时点 | PASS | FAIL | MISSING | 触动数 |
|---|---:|---:|---:|---:|
| 清前（`_pre`） | **18/18** | 0 | 0 | **0** |
| 清后（`_post`） | **18/18** | 0 | 0 | **0** |

### §5.1 贴邻 frozen 的清缓存面（派工单点名）

| 件 | 清前 SHA-12 / 字节 | 清后 SHA-12 / 字节 | 判定 |
|---|---|---|:-:|
| `verifier/audit/conservation.py` | `4bdec2683f06` / 22,105 B | `4bdec2683f06` / 22,105 B | ✅ **逐字节不动** |

- 与 18 frozen 锚存根字面 `4bdec2683f06` **吻合**；与 `results/_v3_recheck_05_rescript_2026_09_28.md` §0 表 0-6 行、`_v3_n_recheck_llm_verdict_2026_09_27.md` §2 表两处独立记录**同值**（三证一致）。
- **清缓存 ≠ 动本体**：本棒只删 `verifier/audit/__pycache__/conservation.cpython-314.pyc`（27,641 B / `32376299b40f`，字节码派生物），**`conservation.py` 本体 0 字节改动**。
- `verifier/kill_lines/`（`kt_b1_kill_decision.py` + 空 `__pycache__`）本棒仅清空目录，**该目录内 `.py` 件 0 触动**。

### §5.2 修复面源件 0 触动复验（清后再次复算）

| 源件 | SHA-12 | 判定 |
|---|---|:-:|
| `results/_v4_supp_t15r2_executor_r1_2026_09_28.py` | `e0936a68fa82` | ✅ 未动 |
| `results/_v4_supp_t15r2_executor.py` | `4b5b720d5cda` | ✅ 未动 |
| `results/_v4_supp_t15_executor_r1_2026_09_27.py` | `6d22444c65af` | ✅ 未动 |
| `results/_v4_supp_t15_executor.py` | `558e635f9ba6` | ✅ 未动 |

**18 frozen 触动数 = 0；修复面源件触动数 = 0。**

---

## §6 key 明文自扫

**方法**：`re` 5 类形态扫描（`sk-ant-*` / `sk-*` / UUID 形 / `Bearer <字面>` / `api_key|ARK_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY` 赋值给字面值），扫本棒 **6 件新出件 + 2 件修复源件**。**0 LLM，纯本地。**

**命中总计 = 0**（新出件 0 / 源件 0）→ **0 key 明文落盘** ✅

引用面抽样（应只见 runtime 表述、0 值）：

```
key_source": "runtime env / desktop AI/LLM API.txt"
R4 key 永不明文 (无例外): key 仅 runtime env / desktop AI/LLM API.txt 读, 不落盘
```

**0 读取 key**（本棒无任何 API 调用面；验证脚本只 import 模块对象，0 执行网络路径）。

---

## §7 老实交代

1. **修复件未切换执行面**：`_r2_atomic` 两件已就位且 22/22 验证通过，但**原件一字未动、在 PI 明示切换前跑的仍是原件** ⇒ **checkpoint 非原子写在执行面上「仍在」**。是否切换 = PI 处置，本棒 0 代取舍（§3.3）。
2. **checkpoint 类 3 件（被引/归档）仍带缺陷**：`.tmp/_t15r2_records.json` / `.tmp/_t15_records.json` 仍是活状态面，崩半路风险未被本棒消除（§3.1）。
3. **终端产出类 46 件未修**：其中 `llm_fetch.py` `save_record` 与 v3 recheck executor 系被测试/预登记面依赖，改动面超出本棒授权（§3.2）。
4. **「崩半路」覆盖面窄**：本机实测的崩溃形态是**进程被强杀**（`TerminateProcess`）；**断电 / 磁盘写满 / `fsync` 后掉电缓存未落**三类**无法在本机复现，未代填**。原子写三段式对这三种形态的覆盖是**处方层面**的，不是本机实测结论。
5. **`os.replace` 的原子性依赖同卷**：临时件与目标件同目录（`path.with_name`）⇒ 同卷。若目标落在跨卷网络盘/JuiceFS 等非本地卷，本机未测该退化面。
6. **正则登记有假阳**：`deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py` 的 2 处命中在**注释行**（L18/L246 缺陷说明文字），实码 L277 已原子 —— 已逐行确认并在此声明，不计入未修面。同理 `.tmp` 脚手架件命中含本棒自有代码，登记表未剔除，属已知噪声。
7. **验证脚本自身 3 处 harness 缺陷**（GBK 编码 / 对照组漏 import / 观察竞态），已修正后重跑；最终 22/22 取自修正后完整一轮，**已作废的首轮结论未混入**（§2.4）。
8. **计数口径**：本棒 `1,898,147 B` / 33 件 为**清前逐件实测**；与 09-27 台账 `U-5`（`__pycache__`/`.pyc` 分桶 19→42、字节码净增 +23）**非同一时点、亦非同一分桶**，故**不做跨棒 delta 断言**（差异含自然增长，按 PI「文件数一类归 V4 收尾校正」口径，此处只登记现状）。
9. **本棒 0 新建 `__pycache__`**：全部 Python 调用带 `-B` + `sys.dont_write_bytecode`；清后全仓复扫 `= NONE` 可证。
10. **本棒产物仅 2 件新名修复件 + 本报告**；其余 14 件为 `.tmp` 脚手架（可复算，0 冒充正式件）。**派生 JSON 0 合并**：两修复件各自独立落盘，0 并入既有 `_v4_supp_t15*` 系列。

---

**出件方**：Mavis 团队 worker（agent: worker）｜2026-09-28
**署名如实**：本件由 worker 出件；引用件（慢处置 B manifest `evidence-auditor` 出件 / T15·T15r2 verdict / cpath_r1 件 / V3 勘误链 / 18 frozen 锚存根）均为**原始出证方**，本件只作引用，未以其名义出证。
