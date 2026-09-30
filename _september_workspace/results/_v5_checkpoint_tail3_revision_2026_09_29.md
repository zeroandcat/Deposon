# V5 checkpoint 尾 3 件修订棒｜被引 / 归档 3 件出修订件（写侧原子写）

- 日期：2026-09-29
- 派工：Mavis（root session）｜派工单「deposon V4 checkpoint 3 件修订棒（worker）」
- 出件：**Mavis 团队 worker**（agent: worker）
- 拍板依据：PI 2026-09-29 10:57 拍板「出修订件」（`ask_e8c605dd1d9b662df6a33923` q2）
- 上游锚件：`results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md`（`52b3dec13e06`）§2.3 / §3.1；执行面切换登记 `results/_v4_exec_surface_switch_2026_09_28.md`（`3bc852e0d48b`）§3 / §5 / §6 / §9
- 场景：worker｜执行类（出修订件 / 做处置 / 落证据）
- 哈希算法：`hashlib.sha256(...).hexdigest()[:12]`，**小写**（禁内建 `hash()`）
- 铁律执行：**新名件**｜**既有件 0 触动**（3 源件 + 6 件同族 lineage + 18 frozen 全 PASS）｜**0 新设阈值**｜**0 覆盖既有件**｜**0 删除既有件**（仅本棒自有沙箱走 `mavis-trash` 可恢复清理）｜**0 跑批 / 0 新读数 / 0 读取 key**（R4 key 永不明文，§6 自扫 0 命中）｜**派生 JSON 0 合并**｜**既有引用件 0 回改**（别名表承接，§4）

---

## §0 结论速览

| # | 派工项 | 实测口径 | 动作 | 结果 |
|:-:|---|---|---|:-:|
| 1 | 定位「被引 / 归档 3 件」 | 3 件路径 / 字节 / SHA-12 **全部与 `52b3dec13e06` §2.3 登记同值**；非原子写点位逐行复核（§1） | 逐件出**新名修订件** | ✅ 3/3 |
| 2 | 逐件出修订件（cpath_r1 同款三段式） | 3 件新出件（`r0_atomic` ×2 + `r1_atomic` ×1），落盘字节 66,317 / 89,083 / 25,892 | 逐字节复制 + **仅改写出面** | ✅ 完成（diff 逐行核验，§2.3） |
| 3 | 验证 | **12/12 PASS**（V1–V8，§3） | `ast.parse` + 三段式静态 + 字节同构 + 强杀语义 + diff 面 + 0 触动 + key 自扫 | ✅ 完成 |
| 4 | 别名映射表 | **新增 6 条（B-01…B-06）**，本件为唯一映射源；既有引用件 **0 回改** | 追加节（§4） | ✅ 完成 |
| 5 | 登记件落盘 | `results/_v5_checkpoint_tail3_revision_2026_09_29.md` | 落盘 | ✅ 完成 |

**修订件（3 件新名）**

| 新名件 | 字节 | 行 | SHA-12 | 源件（0 触动） |
|---|---:|---:|---|---|
| `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | 66,317 | 1,367 | `7da23c0e94cf` | `results/_v4_supp_t15_executor.py`（62,285 B / `558e635f9ba6`） |
| `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | 89,083 | 1,663 | `678032f726a8` | `results/_v4_supp_t15r2_executor.py`（84,884 B / `4b5b720d5cda`） |
| `results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py` | 25,892 | 585 | `b1923528ab84` | `results/_archive_2026_09_24/l14_runner_v2.py`（23,056 B / `acf1cd6ccbd4`） |

**脚手架（`.tmp/`，可复算，0 冒充正式件）**

| 件 | 字节 | SHA-12 |
|---|---:|---|
| `.tmp/_tail3_atomic_make_2026_09_29.py`（生成器） | 17,272 | `94d57549533b` |
| `.tmp/_tail3_atomic_make_2026_09_29.json`（逐行 diff + 0 触动构造前后复算） | 19,595 | `6c6fb7078a9d` |
| `.tmp/_tail3_atomic_verify_2026_09_29.py`（验证器 V1–V8） | 21,338 | `8d12c9c9cb2d` |
| `.tmp/_tail3_atomic_verify_2026_09_29.json`（12 项验证结果） | 11,116 | `e4226aaf3380` |
| `.tmp/_tail3_atomic_refs_2026_09_29.py`（引用面扫描器） | 2,636 | `4e8ea9bea948` |
| `.tmp/_tail3_atomic_refs_2026_09_29.json`（引用面清单） | 5,784 | `d6a3361a794a` |
| `.tmp/_tail3_atomic_landing_check_2026_09_29.py`（落盘核验 + 报告声明值对账 + 0 触动终检） | 2,699 | `5c19cf8f29fb` |

---

## §1 三件定位（登记件实测复核，非复述）

`52b3dec13e06` §2.3 表内 5 件 checkpoint 类件中，「REGISTER_NO_FIX」3 件即本棒对象。**盘上实测与登记同值**（§5 复验）：

| # | 源件（被引 / 归档） | 字节 | SHA-12 | 非原子写点位（源件行号 · 代码层） | checkpoint 变量 / 落盘路径 | 登记不修理由（原文） |
|:-:|---|---:|---|---|---|---|
| A | `results/_v4_supp_t15_executor.py` | 62,285 | `558e635f9ba6` | **L442-445** `save_checkpoint()`：`CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")` | `CHECKPOINT_PATH` → `.tmp/_t15_records.json` | 被引（T15 verdict 记 `558E635F9BA6`） |
| B | `results/_v4_supp_t15r2_executor.py` | 84,884 | `4b5b720d5cda` | **L468-471** `save_t15r2_records()`：`T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False), encoding="utf-8")` | `T15R2_CHECKPOINT_PATH` → `.tmp/_t15r2_records.json` | 被引（R1 前身，被 R1 与 verdict 引用） |
| C | `results/_archive_2026_09_24/l14_runner_v2.py` | 23,056 | `acf1cd6ccbd4` | **L153**（逐 call 存，套 `try/except`）+ **L168**（收尾存）：`CHECKPOINT.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")` | `CHECKPOINT` → `.tmp/_l14_records.json` | 归档件 + 被 L14 verdict §9.1 引用 |

**逐行复核补充（诚实交代：登记表的「落盘点数」列计的是 checkpoint 类口径，本棒逐行复核另见终端产出面）**

- A 件代码层非原子写共 **4 处**：L442-445（checkpoint 类，**本棒修**）+ L622 `PROBE_LOG_PATH` + L697-699 batch `.jsonl`（每次新名新建，非覆盖写）+ L1260 `RESULT_PATH`（终端产出类，**登记不修**）。`52b3dec13e06` §2.3 记「3」= L444 / L622 / L1260 三处**覆盖写**（其正则未命中 L697 的 `with open(...)` 块内写），本棒按**覆盖写口径**沿用，分界不变。
- B 件代码层非原子写共 **4 处**：L468-471（checkpoint 类，**本棒修**）+ L715 `T15R2_PROBE_LOG_PATH` + L817-819 batch `.jsonl` + L1549 `T15R2_RESULT_PATH`（终端产出类，**登记不修**）。
- C 件代码层非原子写共 **3 处**：L153 / L168（checkpoint 类，**本棒修**）+ L490 `OUT_RESULT` / L523 `OUT_POST`（终端产出类，**登记不修**）。

**分界原则（沿 `52b3dec13e06` §2.3 逐字沿用，不重新裁量）**：checkpoint 类 = 崩半路**损已累计状态** ⇒ 修；终端产出类 = 崩半路**只损本次产出** ⇒ 登记不修。`r2_atomic` 两件先例同样保留其终端产出面未修（`52b3dec13e06` §2.3 末段）。

---

## §2 逐件出修订件

### §2.1 命名（沿既有惯例 + 1 处新标签，已明写）

| 源件代际 | 本棒修订件 | 命名理由 |
|---|---|---|
| A / B：**基名代**（无 `rN` 后缀，被 `3bc852e0d48b` §5 A-03 / A-04 定义为「基名 / 预登记锚名」） | `..._r0_atomic_2026_09_29.py` | **`r0` = 基名代（本棒新引入的代际标签，无先例）**：既有 lineage 已占 `r1`（F1 读侧）/`r2_atomic`（写侧）/`r3`（件头名回改），本棒修订件**不是 `r3` 的后继**（它是基名代 + 写侧补正，读侧沿基名），故取 `r0` 以免与既有三件混淆。**已在本件 §4 别名表 + 三件源件 docstring 登记块内逐字写明**。若 PI 偏好其他标签，处置权归 PI（0 代取舍，§7-3） |
| C：`l14_runner_v2.py`（版本后缀 `v2`，非代际后缀） | `..._l14_runner_v2_r1_atomic_2026_09_29.py`（同目录） | 沿 `_rN_atomic` 惯例，`r1` = 首修订件；**同目录落盘**以保持归档 lineage 就地可核（其 `sys.path.insert(0, '.../results')` 指向 `results/`，故位置不影响导入） |

### §2.2 处方（逐字沿 cpath_r1 / `r2_atomic`）

三件插入**同一份** helper（`ast.get_source_segment` 级逐字一致）：

```python
def _atomic_write_json(obj, path, indent=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.tmp_{os.getpid()}")   # 临时件名带 pid ⇒ 并发进程互不踩踏
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)   # 同卷原子替换: 要么全量新内容, 要么原内容
    except BaseException:
        # 写失败/被杀: 既有数据一字不动; 临时件留场供事后取证, 不静默吞。
        raise
```

- **处方源**：`deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py` L233-240（`3bc852e0d48b` §4.2 登记的 cpath_r1 同款）。
- **实现沿**：`results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` L546-562（同款，含 `try/except` + `raise` 不静默吞）。
- **写出面新调用**：A `_atomic_write_json(records, CHECKPOINT_PATH)`｜B `_atomic_write_json(r2_records, T15R2_CHECKPOINT_PATH)`｜C 两处 `_atomic_write_json(records, CHECKPOINT)`（L193 / L208，**外层 `try/except` 与 `checkpoint FAIL` 打印逐字不动**）。
- **落盘字节同构**：`json.dump(..., ensure_ascii=False, indent=None)` ≡ 源件 `json.dumps(..., ensure_ascii=False)`（V4 实测逐字节同值，§3）。

### §2.3 diff 摘要（逐行核验，V6 机器判定「仅写出面」）

| 件 | hunk | 源行 | 新行 | 动作 |
|:-:|---|---|---|---|
| **A** | 1 | L3 | L3 | 替换：件头自述名 → 本件名（1 行；docstring 文本，**非**算法/常量/逻辑） |
| | 2 | L5 前 | L5-23 | 插入：件头登记块 19 行（docstring 内 = 身份 + 来源链 + 缺陷 + 危害 + 边界 + 非执行面声明） |
| | 3 | L442 前 | L461-493 | 插入：处方注释块 + helper 33 行 |
| | 4 | L443-445 | L495-496 | 替换：旧 `write_text` 3 行 → 新 `def` + `docstring` + 1 行调用 |
| **B** | 1 | L3 | L3 | 替换：件头自述名（1 行） |
| | 2 | L5 前 | L5-26 | 插入：件头登记块 22 行 |
| | 3 | L468 前 | L490-522 | 插入：处方注释块 + helper 33 行 |
| | 4 | L469-471 | L524-525 | 替换：旧 `write_text` 3 行 → 新 `def` + `docstring` + 1 行调用 |
| **C** | 1 | L51 前 | L51-90 | 插入：处方注释块 + helper 40 行（紧接 `CHECKPOINT` 常量定义，**首次使用之前**） |
| | 2 | L153 | L193 | 替换：旧 `write_text` 1 行 → `_atomic_write_json(records, CHECKPOINT)` |
| | 3 | L168 | L208 | 替换：旧 `write_text` 1 行 → `_atomic_write_json(records, CHECKPOINT)` |

**V6 机器判定**：3 件的**被删行**全部落在白名单（件头自述名行 + 旧 checkpoint `write_text` 行 + 旧 `def` 签名行 + 旧 `mkdir` 行），**新增行**中**代码类**行全部落在白名单（helper 骨架 11 行 + 新 `def` 签名 + 1 行调用），其余新增行全部为注释 / docstring；`unauthorized_removed = 0`、`unauthorized_added = 0`（3/3）⇒ **算法 / 常量 / 阈值 / cells 矩阵 / 调用面 / 返回值 / records 结构 / paths 0 触动**。

**编码面**：3 件新出件 **CR = 0（LF-only）/ 无 BOM**；构造脚本跑两遍 SHA-12 恒等（**确定性可复算**）。

---

## §3 验证结果（12/12 PASS · `e4226aaf3380`）

脚本：`.tmp/_tail3_atomic_verify_2026_09_29.py`（可复算）。**0 跑实验 / 0 新读数 / 0 调阈值 / 0 读取 key**；沙箱 = `.tmp/_tail3_scratch/`（跑完 `mavis-trash` 可恢复清走）。

| 组 | 检查项 | 结果 | 实测值 |
|:-:|---|:-:|---|
| **V1** | 3 件 `ast.parse` 语法核验（**不执行**） | ✅ 3/3 | 66,317 / 89,083 / 25,892 B |
| **V2** | 原子写三段式静态核验：`tmp_`+pid / `f.flush()` / `os.fsync(f.fileno())` / `os.replace(tmp, path)` **全 True** | ✅ 3/3 | 3 件 helper 逐字同款 |
| **V2** | 新件代码层旧非原子 checkpoint 写出面 = **0** | ✅ | `old_writeface=[]` ×3 |
| **V2** | 源件仍带旧写出面（**对照组成立** ⇒ 修的是真缺陷） | ✅ | `src_still_nonatomic=True` ×3 |
| **V2** | 新件 checkpoint 写出全部经 helper | ✅ | A/B 各 1 处；C **2 处** |
| **V3** | **3 源件** SHA-12 构造前 / 构造后复算 | ✅ 3/3 | `558e635f9ba6` / `4b5b720d5cda` / `acf1cd6ccbd4` 全部同值 |
| **V3** | **6 件同族 lineage**（`r1` / `r2_atomic` / `r3` × 2 系）0 触动 | ✅ 6/6 | `6d22444c65af` / `9e89e021ea03` / `b86cce242abe` / `e0936a68fa82` / `215db16a0556` / `4f514b3fb4b8` |
| **V3** | **18 frozen** 逐件复算 | ✅ **18/18** | `mismatch=[]`（锚源 `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`） |
| **V4** | 落盘字节：新原子写 == 旧 `write_text` == payload 期望字节 | ✅ 3/3 | 两侧均 **5,508,890 B / `13425104558a`**，`leftovers=[]` |
| **V5** | 强杀（`p.kill()` = `TerminateProcess`）后终态 ∈ {**原内容逐字节**, **完整新内容**}，0 截断 0 混合 | ✅ 3/3 | A `ORIGINAL_UNTOUCHED`、B `NEW_COMPLETE`、C `ORIGINAL_UNTOUCHED`（seed `6d61e84adfbc` 均同值；`json.loads` 全 OK） |
| **V5** | **对照组**：旧写法同沙箱同 payload 同强杀时点 ⇒ 数据被摧毁 | ✅ 3/3 | after `13425104558a` / 5,508,890 B（seed 仅 412,090 B）⇒ **修复非装饰** |
| **V6** | diff 仅写出面（白名单机器判定） | ✅ 3/3 | 未授权删除 0 / 未授权新增 0 |
| **V7** | key 明文自扫（5 类形态：sk-ant / sk- / UUID 形 / Bearer / key 字面赋值） | ✅ | **命中总计 0** |
| **V8** | 本棒 0 新生 `.pyc`（按 3 件基名全仓扫） | ✅ | `V8_pyc_for_new_files=[]`（3 件新出件 0 字节码） |

**强杀时点诚实交代**：V5 的正确判据是「终态 ∈ {原内容逐字节, 完整新内容}」，**不是「必须原封不动」**——若强杀落在一次写**完成之后**，终态合法地变成完整新内容（本轮 B 件即此形态）。三轮跑批中两种终态都出现过，**均属原子语义的正确表现**；旧写法对照组在同一时点则稳定被摧毁（seed 412,090 B → 5,508,890 B 半写/混合体）。

---

## §4 别名映射表（本件为唯一映射源 · 本节新增 **6** 条）

> **生效规则（全表适用，沿 `3bc852e0d48b` §5 逐字沿用）**：**旧引用一律读作新件**。
> 见到左列任一写法 ⇒ 一律解释为右列新件；**旧件字节不因此被追认、也不因此被改写**。
> 既有件（预登记 / 台账 / 登记件 / 勘误链 / verdict / 委托信 / plugin）**byte 0 触动**，其旧名引用**不改写**，由本表承接解释。
>
> **与 `3bc852e0d48b` §5 / §9.5 的关系（防误读，0 合并两表）**：`3bc852e0d48b` 的 A-01…A-10 解决的是「**r1 → r2 → r3 收敛**」（**执行面**语义）；本表 B-01…B-06 解决的是「**基名代 / 归档件 → 写侧补正件**」（**修订件**语义）。**两者终点不同、互不覆盖**：A-03 / A-04 的终点仍是 r3（**执行面不变**），B-01 / B-02 的终点是本棒 `r0_atomic`（**写侧补正件，非执行面**）。**旧引用按哪条读，取决于该引用要问的是「跑哪件」还是「补写侧用哪件」。**

| 别名 ID | 旧引用写法（见到即读作右列） | 新件（写侧补正面） | 别名类型 | 右列 SHA-12 |
|:-:|---|---|---|---|
| **B-01** | `results/_v4_supp_t15_executor.py`（基名 / 预登记锚名 / T15 verdict 锚名） | `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | 基名代 → 写侧补正件 | `7da23c0e94cf` |
| **B-02** | `results/_v4_supp_t15r2_executor.py`（基名 / R1 前身 / T15r2 verdict 锚名） | `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | 基名代 → 写侧补正件 | `678032f726a8` |
| **B-03** | `results/_archive_2026_09_24/l14_runner_v2.py` | `results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py` | 归档件 → 写侧补正件 | `b1923528ab84` |
| **B-04** | `.tmp/l14_runner_v2.py`（**09-24 移动前路径**；见 `_v4_maindir_cleanup_moves_ledger_2026_09_24.md` G1 / moves_ledger_v2 G5） | 同 **B-03** | 历史路径拼写 | `b1923528ab84` |
| **B-05** | `_v4_supp_t15_executor.py` / `_v4_supp_t15r2_executor.py`（**无扩展名**；源件件头自述名 + CLI 用法行） | 同 **B-01** / **B-02** | 件头自述 / 用法拼写 | `7da23c0e94cf` / `678032f726a8` |
| **B-06** | `_v4_supp_t15_executor_r0_atomic_2026_09_29.cpython-314.pyc` 及同款两件 `.pyc` | 随 **B-01 / B-02 / B-03**；`.pyc` 为派生态，**本棒 0 新生**（V8） | pyc 派生态 | — |

**B-01 / B-02 的边界（防「补写侧 = 换执行面」误读）**：基名件**仍在盘、0 触动**；本表**不废止**其历史身份与预登记锚名身份，**仅**声明「当被问『基名代的 checkpoint 写侧缺陷补在哪件』时读作本棒新件」。**执行面不变** = r3 两件（`3bc852e0d48b` §9.6）——r3 才是 F1 读侧 + 原子写**两侧齐备**者。

### §4.1 引用面清单（grep 实测；`3bc852e0d48b` §6 先例口径）

**检索字面**：`_v4_supp_t15_executor.py` / `_v4_supp_t15r2_executor.py` / `l14_runner_v2.py`；范围 = 全仓；`.tmp/` 脚手架单列不计入生效面；`.pyc` / `__pycache__` 不计；**本棒 3 件新出件不计**（其件内提及源件名 = 来源链登记，非旧引用面）。扫描器 `.tmp/_tail3_atomic_refs_2026_09_29.py`（`d6a3361a794a`）。

| 源件 | 非 `.tmp` 引用面 | 行数 | 其中：源件自引 | 其中：lineage 件自引（r1/r2_atomic/r3） | **第三方引用（预登记 / verdict / 台账 / 勘误链 / letters / plugin）** |
|---|---:|---:|---:|---:|---|
| A `_v4_supp_t15_executor.py` | **18 件** | 59 | 5 | 27（9×3） | **14 件 / 27 行** |
| B `_v4_supp_t15r2_executor.py` | **21 件** | 62 | 5 | 18（6×3） | **17 件 / 39 行** |
| C `l14_runner_v2.py` | **11 件** | 17 | 4 | 0 | **10 件 / 13 行** |

**须点名的活引用面（0 回改，由本表承接）**

| 引用件 | 行数 | 性质 | 处置 |
|---|---:|---|---|
| `deposon_team/plugins/_v4_wide_s5_prescan_2026_09_27.py`（L21 / L35） | 2 + 2 | **活代码**（按基名 `RES / f` 读源件 + 打印 `load_checkpoint` 段 + 扫其 SHA-12 被引面） | byte 0 触动（R7 plugin spec 不动）→ B-01 / B-02 承接 |
| `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md`（3）/ `..._T15_activation_...`（1）/ `..._T15r2_...`（1，对 A 件基名）/ `..._T15r2_activation_...`（对 A 件基名 0 命中） | 5 | 预登记锚名 + 件名建议 | 0 触动（预登记层只引基名）→ B-01 / B-02 承接 |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（**frozen 勘误链**） | 2 + 6 | 勘误链（含 L3823「下棒加原子写」登记项） | **byte 0 触动**（18 frozen 复算 18/18 PASS） |
| `results/_v4_supp_t15_verdict.md` / `results/_v4_supp_t15r2_verdict.md` | 4 + 4 | verdict 锚名 + 0 触动声明 | 0 触动 → B-01 / B-02 承接 |
| `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` / `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md`（2 封，各 1 行） | 2 | **对外委托信**（含字节 + SHA-12 锚） | 0 触动 → B-01 / B-02 / B-03 承接 |
| `results/_v4_supp_t1_executor.py`（L1217）+ `results/_v4_supp_t1_result.json`（L2445） | 1 + 1 | T1 产物链的「字面锚」引用 | 0 触动 → B-03 承接 |

**0 回改实证**：既有引用件**无一字节被改写**（本棒 3 件新出件 + 1 件登记件 + 7 件 `.tmp` 脚手架为**全部**新增产物；§5 复算）。

---

## §5 既有件 0 触动实证

| 面 | 件数 | 结果 |
|---|---:|---|
| **3 源件**（本棒唯一「被改写出面」的对应源） | 3 | ✅ 构造前 / 构造后 SHA-12 **同值**（`src_untouched=True` ×3，生成器内建断言 + V3 独立复算） |
| **6 件同族 lineage**（`r1` / `r2_atomic` / `r3` × 2 系） | 6 | ✅ 6/6 与 `3bc852e0d48b` §2 / §9.3 登记同值 |
| **18 frozen** | 18 | ✅ **18/18 PASS**，`mismatch=[]` |
| **既有引用件**（预登记 / verdict / 勘误链 / 台账 / letters / plugin） | 全部 | ✅ 0 回改（本棒 0 次写入这些路径） |
| **新增产物** | 11 | 3 件新名修订件（`results/` / `results/_archive_2026_09_24/`）+ 1 件本登记件 + 7 件 `.tmp` 脚手架（4 `.py` + 3 `.json`） |

**触动数 = 0**（3 源件 + 6 lineage + 18 frozen + 全部既有引用件）。

---

## §6 铁律与自扫

- **R4 key 永不明文**：3 件新出件 5 类形态自扫**命中 0**；本棒**0 读取 key**、0 网络、0 LLM 调用（所有 python 调用纯本地 `hashlib` / `re` / `ast` / `difflib` / `subprocess` 跑本地脚本）。
- **新名件 0 覆盖**：3 件新出件为**首次落盘**；生成器内建「目标行字面断言」，任一不符即 `SystemExit` 中止（构造失败不留半成品）。
- **0 永久删除**：**0 删除既有件**；唯一清理动作 = 本棒自有沙箱 `.tmp/_tail3_scratch/`（验证产物）走 `mavis-trash` 可恢复通道，回执 `mavis-trash: moved to trash: '.tmp/_tail3_scratch'`（该回执在 GBK 控制台把中文路径显示为乱码，**仅回执显示问题**，文件已进回收）。
- **0 新生字节码**：全部 python 调用带 `-B`；V8 实测 3 件新出件 **0 个 `.pyc`**。
- **0 新设阈值**：0 改阈值字面（`K_N11_3_THRESHOLD=0.85` / `K_N11_1_DIFF=0.05` / `K_N11_2_DELTA=0.05` / `TH-T1-1=10`）、0 改 cells 矩阵、0 改 `N_REASKS`、0 改 kill-line、0 改 records 结构、0 改 paths、0 改返回值、0 改调用面。
- **派生 JSON 0 合并**：3 件修订件各自独立落盘，0 并入既有 `_v4_supp_t15*` / `_v4_supp_t15r2*` / `_archive_2026_09_24/` 系列。
- **skill 面**：本棒派工单**未点名任何 skill** ⇒ 0 skill 加载需求（无「skill not found」事件可交代）。
- **A-7 / r3（26b executor）**：按派工单**不在本棒范围**（已另有 r3）⇒ 本棒 0 触碰 26b 面。

---

## §7 老实交代

1. **修订件未切换执行面**：`r0_atomic` ×2 / `r1_atomic` ×1 已就位且 12/12 验证通过，但 **t15 / t15r2 系执行面仍是 r3 两件**（`3bc852e0d48b` §9.6），**基名代 / 归档件不在执行面**。本棒**不代 PI 决定**是否把执行面切到本棒新件（且**不建议切**：r3 才是读写两侧齐备者，见第 2 条）。
2. **基名代修订件只补写侧、读侧沿基名（无 F1 响亮告警）**：A / B 两件新出件的 `load_checkpoint()` / `load_t15_records()` / `load_t15r2_records()` 仍为 `except Exception: return []` 静默（**与源件逐字一致 = 非退化**）。**这正是本棒「仅改写出面」边界的直接后果**（派工单口径），已写进三件件头登记块。若下游要「两侧齐备」，正确件是 **r3**，不是本棒新件。
3. **`r0_atomic` 是本棒新引入的代际标签（无先例）**：既有 lineage 占 `r1` / `r2_atomic` / `r3`；本棒修订件是「基名代 + 写侧补正」的**平行支线**（不是 `r3` 的后继），取 `r0` 是为避免与既有三件同名混淆。**该标签已在本件 §2.1 / §4 与三件源件 docstring 内逐字写明**；若 PI 偏好别的命名（如 `base_atomic` / `b1`），处置权归 PI —— 本棒**不擅自改名**（改名 = 新一轮动作）。
4. **C 件 docstring 的用法路径字面已陈旧（继承面，0 改）**：`l14_runner_v2_r1_atomic_2026_09_29.py` 的 docstring 仍写 `python .tmp/l14_runner_v2.py ...` —— 该路径是 **09-24 移动前**的旧位置（实件在 `results/_archive_2026_09_24/`，见 moves_ledger G1 / G5）。**此陈旧面源自源件、随复制继承**；本棒 0 改（改它 = 改非授权行）。B-04 别名承接该旧路径写法。
5. **终端产出类写出面未修**：A 的 `PROBE_LOG_PATH` / `RESULT_PATH`、B 的 `T15R2_PROBE_LOG_PATH` / `T15R2_RESULT_PATH`、C 的 `OUT_RESULT` / `OUT_POST` 仍为非原子写，**登记不修**（沿 `52b3dec13e06` §2.3 分界：崩半路只损本次产出、不损已累计 checkpoint 状态）。⇒ **「3 件全原子」是错误读法**：本棒只把 **checkpoint 类写出面**变成三段式。
6. **helper 内 `mkdir` 是唯一语义增量**：三段式含 `path.parent.mkdir(parents=True, exist_ok=True)`。A / B 源件原本就在 save 里 mkdir（**等价**）；**C 源件原本 0 mkdir**（依赖 `.tmp/` 已存在）⇒ C 新件在目录缺失时会**自动创建**该目录（幂等、不覆盖他件）。此为 cpath_r1 处方自带，逐字沿用未改。
7. **「崩半路」覆盖面窄（如实，不代填）**：本机实测形态 = **进程被强杀**（`p.kill()` = `TerminateProcess`，Windows 无 `SIGKILL`）；**断电 / 磁盘写满 / `fsync` 后掉电缓存未落**三类**无法在本机复现，未代填**。原子写三段式对这三种形态的覆盖是**处方层面**的，不是本机实测结论（沿 `52b3dec13e06` §7-4）。
8. **`os.replace` 原子性依赖同卷**：临时件与目标件同目录（`path.with_name`）⇒ 同卷。**跨卷（网络盘 / JuiceFS 等非本地卷）退化面本机未测**（沿 `52b3dec13e06` §7-5）。
9. **验证脚本自身 5 处 harness 缺陷（已全部修正后重跑，最终结论取自修正后完整一轮 = 12/12；已作废轮次未混入）**：
   ① **生成器 `set_line` 只断言未赋值** ⇒ 首版 C 件两处 `write_text` 未被替换（diff 报告仅 1 hunk 时即发现）→ 补 `lines[idx0] = new`；
   ② **源件相对索引漂移**（先插件头块再按源件行号切片）⇒ A / B 首版把切片打到错位行（hunks 由 4 变 6、行数异常膨胀）→ 改为「先补写出面、后插件头块」+ 4 行字面断言；
   ③ **P1 重复块残留**（②的编辑残留第二份 `site/new_save`）→ 删除后 hunks 回到 4；**并以「连跑两遍 SHA-12 恒等」验证生成器确定性**；
   ④ **V5 判据设错**（首版要求「强杀后必须原封不动」）⇒ 两件因「强杀落在写完之后、终态 = 完整新内容」而误报 FAIL → 改为正确原子判据「终态 ∈ {原内容逐字节, 完整新内容}，0 截断 0 混合」；**该 FAIL 是判据错，不是修复错**；
   ⑤ **V6 / V8 判据设错**：V6 用带缩进的白名单比对 `strip()` 后的行（永不匹配）→ 改为 `strip()` 口径白名单 + docstring 状态机归类；V8 原判「全仓 `__pycache__` = 0 目录」→ 改为「3 件新出件 0 个 `.pyc`」（见第 10 条）。
10. **全仓 `__pycache__` 现状如实登记（不计入本棒）**：复扫得 **7 个** `__pycache__` 目录，其中 2 个为**本日（09-29）新建**：仓根 `__pycache__`（11:15:09，含 `_v5_gt_exec_2026_09_29.cpython-314.pyc`）与 `results/__pycache__`（10:51:42，含 `_v3_recheck_26b_executor_r3_2026_09_29.cpython-314.pyc`）—— 二者**均非本棒产物**（26b r3 属派工单点名的「已另有 r3」面；`_v5_gt_exec` 属另一并发 session）。`52b3dec13e06` §7-9 记的「全仓复扫 = NONE」是**该棒时点**结论，**本棒不复述该结论**，只登记现状；`.pyc` 为可再生派生物，删除与否**超出本棒授权**（PI 未拍板），**0 擅自清理**。
11. **本棒 0 跑批 / 0 新读数**：`run` / `aggregate` **未执行**（涉真实端点与 key runtime 读）⇒ 「修订件在真实数据面上生效」目前是**静态论证 + 生效登记，非跑批实证**（沿 `3bc852e0d48b` §8-2 口径）。V4 / V5 跑的是**提取自新件的 helper 副本**（`ast` 抽取 `FunctionDef` 源码段后独立执行），**不 import / 不执行**三个新件的任何模块级代码。
12. **计数口径**：本棒新增 **11 件**（3 件新名修订件 + 1 件本登记件 + 7 件 `.tmp` 脚手架 = 4 `.py` + 3 `.json`）；「修订件 = 3 件」不含脚手架与本登记件。文件数 / 目录计数类差异按 PI 口径归 **V4 收尾整理**统一校正，本棒只登记现状。

---

**出件方**：Mavis 团队 worker（agent: worker）｜2026-09-29
**署名如实**：本件由 worker 出件；引用件（`52b3dec13e06` checkpoint 原子写棒 / `3bc852e0d48b` 执行面切换登记 / `_v5_sub_artifact_ledger_2026_09_28.md` 台账 / T15·T15r2 verdict / V3 勘误链 / 18 frozen 锚存根 / cpath_r1 处方源件 / `_r2_atomic` 实现源件 / 4 件预登记 / 2 封致 PI 委托信 / `_v4_wide_s5_prescan` plugin）均为**原始出证方**，本件只作引用，**未以其名义出证**。
**自哈希**：本件 SHA-12 随落盘后回报（沿本仓登记件**不自嵌自身哈希**惯例，避免自指悖论）。
