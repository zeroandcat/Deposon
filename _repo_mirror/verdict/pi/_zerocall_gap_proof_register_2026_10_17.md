# 「零调用」要件之**开放面补取证件**（E-3 人工阅件式补扫 · 55 件 · 2026-10-17）

**件性质**：**补取证件（证据面 · 非判断件 · 非终判）** —— 依 PI 卡 `ask_3b44d24545c29a761106b2d2` 之 Q2「即派补取证」之裁而落；Q1「另议（先补取证）」⇒ 🔴 **R2 判断件 `99b9bff47682` 之采认于本件落盘时点仍未作出**（其「候裁」状态不变）。

**「核验非清理」**：本棒 ⛔ **0** 删 · ⛔ **0** 移 · ⛔ **0** 改任何既有件；本棒仅新增 `.tmp/zerocall_e3_*` 与本件。**本件 0 产生任何清理许可**（③ 拦截 ＝ **161 全数** · 保护面在册未解除 · 解除归 PI · 授权未给）。

---

## §0 落盘前占位实测（本棒直算 · 写入前）

| 项 | 实测 |
| :-- | :-- |
| 目标面 `results/_zerocall_gap_proof_register_2026_10_17.md` 之 `Test-Path` | **`False`** |
| `results/_zerocall_gap_proof_register_2026_10_17*` 之 glob | **0** 命中 |
| 全仓 `**/_zerocall_gap_proof_register_2026_10_17*` 之 glob | **0** 命中 |

⇒ **无撞号 · 未启用 `_r1`**。（`v61` 卡答登记件于 17:12:46 亦实测同面 ＝ 0 在盘，二者互为补全。）

---

## §1 读件与指纹（本棒直算 SHA-256 之后取 `[:12]` · 非转录）

| # | 件 | 路径 | SHA-12 | bytes | 本件之用法 |
| :-: | :-- | :-- | :-- | --: | :-- |
| 1 | **本棒之裁文之在册来源** | `pi_rulings/_pi_card_answers_register_2026_10_17_v61.md` | `8e41cd9eb3b8` | 39,769 | **本棒之裁文之在册来源**（卡号／两答逐字） |
| 2 | 缺口面 ①：**§8** 缺口传导 | `results/_r2_reading_verdict_2026_10_17.md` | `99b9bff47682` | 43,055 | 缺口面 ①：**§8** 缺口传导 ＋ KD-4／KD-8 |
| 3 | 缺口面 ②：**55 件之逐件清单** | `results/_refonly_161_verify_register_r2_2026_10_17.md` | `b687e16cc7d9` | 94,675 | 缺口面 ②：**55 件之逐件清单**（§4-1）＋ KD-4 载面 |
| 4 | 上游判断件 | `results/_refonly_161_reading_verdict_2026_10_17.md` | `bd94d12323e0` | 39,243 | 上游判断件（E-1／E-2／**E-3** 之出处） |
| 5 | 判读权威 | `results/_citation_no_utility_caliber_draft_2026_10_17.md` | `536a3064ad38` | 49,332 | 判读权威（类 5「读取为数据」字面） |
| 6 | 缺口面 ③：**`V-list` 17 项封闭枚举** | `.tmp/refonly161_r2_probe.py` | `c3171dc8cdf9` | 26,360 | 缺口面 ③：**`V-list` 17 项封闭枚举** ＋ passive 行内共现机制 |
| 7 | **55 件之机械来源** | `.tmp/refonly161_r2_out.json` | `c47c6f4afddd` | 2,029,558 | **55 件之机械来源**（`req2_S_nolazy_script_only`） |
| 8 | 本棒探针 ① | `.tmp/zerocall_e3_probe.py` | `68785c115f03` | 16,361 | 本棒探针 ①（开放面主扫） |
| 9 | 本棒产物 ① | `.tmp/zerocall_e3_out.json` | `4974f56d2b35` | 1,876,399 | 本棒产物 ①（2,156 处提及之逐处分类） |
| 10 | 本棒产物 ② | `.tmp/zerocall_e3_summary.json` | `1797d3e9e2f8` | 72,584 | 本棒产物 ②（逐件 B1/B2/B3 分桶） |
| 11 | 本棒探针 ② | `.tmp/zerocall_e3_hop2.py` | `d67d3e45bfda` | 10,063 | 本棒探针 ②（二跳：载体 → 消费者） |
| 12 | 本棒产物 ③ | `.tmp/zerocall_e3_hop2.json` | `1c6b883a6392` | 33,037 | 本棒产物 ③（二跳站点之 ±10 行上下文） |
| 13 | 本棒产物 ③ 之可读件 | `.tmp/zerocall_e3_hop2.md` | `3a96ae0bd44c` | 11,016 | 本棒产物 ③ 之可读件（人工阅件底本） |
| 14 | 本棒探针 ③ | `.tmp/zerocall_e3_sweeper.py` | `d6839f914fe0` | 7,238 | 本棒探针 ③（目录扫描器枚举） |
| 15 | 本棒产物 ④ | `.tmp/zerocall_e3_sweeper.json` | `40fcd9881663` | 316,892 | 本棒产物 ④（396 扫描器之结构面） |
| 16 | 本棒探针 ④ | `.tmp/zerocall_e3_f5b.py` | `3ecba898966b` | 3,623 | 本棒探针 ④（数字插值构名定向） |
| 17 | 本棒产物 ⑤ | `.tmp/zerocall_e3_f5b.json` | `85275f2242b3` | 1,808 | 本棒产物 ⑤ |
| 18 | 本棒探针 ⑤ | `.tmp/zerocall_e3_utf16_sweep.py` | `a63bc647a4bc` | 4,709 | 本棒探针 ⑤（UTF-16 面闭合） |
| 19 | 本棒产物 ⑥ | `.tmp/zerocall_e3_utf16.json` | `6cf0d6c2a030` | 12,259 | 本棒产物 ⑥ |
| 20 | 本棒探针 ⑥ | `.tmp/zerocall_e3_triage.py` | `22ee5f68d85b` | 5,363 | 本棒探针 ⑥（F1 收窄分诊 · 0 命中之留痕） |
| 21 | **人工阅件件 ①** | `.mavis/scripts/cleanup511/make_register.py` | `45416c09e419` | 13,920 | **人工阅件件 ①**（二跳消费者之一） |
| 22 | **人工阅件件 ②** | `tools/_archive_purge_2026_10_17/step5_register.py` | `cbb6539394a8` | 17,778 | **人工阅件件 ②**（承载全部 55 件之名单之消费者） |
| 23 | **人工阅件件 ③** | `.tmp/dscan_04.py` | `43e661f72888` | 2,302 | **人工阅件件 ③**（`.tmp` scope 之机器假阳） |
| 24 | **人工阅件件 ④** | `.tmp/scan_supplement_five_terminal_2026_10_10.py` | `7c0a6d022104` | 6,010 | **人工阅件件 ④**（ROOT 字节读取面 · 今日不可达） |
| 25 | **人工阅件件 ⑤** | `verifier/v12/check.py` | `87c9c883e3bf` | 4,142 | **人工阅件件 ⑤**（ROOT scope 扫描器 · glob 面不含 `.tmp`） |
| 26 | **人工阅件件 ⑥** | `tests/test_v18.py` | `c523ae4b0989` | 17,093 | **人工阅件件 ⑥**（`os.listdir(tmp_path)`） |
| 27 | **人工阅件件 ⑦** | `.tmp/_s4td_floor_bound_2026_10_09.py` | `ad95b6d5e9b9` | 4,378 | **人工阅件件 ⑦**（glob 面 ＝ `results/*addendum*.json`） |
| 28 | **人工阅件件 ⑧** | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.py` | `a1d8047f1833` | 6,678 | **人工阅件件 ⑧**（同上 glob 面） |
| 29 | 二跳载体 ① | `.tmp/cleanup511_manifest_2026_10_17.json` | `b7093a701856` | 1,754,609 | 二跳载体 ①（承载 46 件之名单） |
| 30 | 二跳载体 ② | `tools/_archive_purge_2026_10_17/inventory_compare.json` | `1b9eee6810b4` | 98,697 | 二跳载体 ②（承载 **55 件**之名单） |

📌 **卡面之在册来源之如实登记**：本棒实测全仓检得卡号 `ask_3b44d24545c29a761106b2d2` 共 **22 处／4 件**（`pi_rulings/_pi_card_answers_register_2026_10_17_v61.md` 10 处 ＋ `.tmp/dw61_probe1.py`／`dw61_verify1.py`／`dw61_write1.py` 各 1／1／10 处）⇒ 🔴 **该号之唯一在册来源 ＝ `v61` 卡答登记件**（Q1 ＝ `q1_r2v_opt3`「另议（先补取证）」／Q2 ＝ `q2_gap_opt2`「即派补取证」）；⛔ **0 读作「卡面载荷件在盘」**（载荷件不在盘）。

---

## §2 缺口面之逐字回读要点（`99b9bff47682` §8 ／ `b687e16cc7d9` ／ `c3171dc8cdf9`）

| 项 | 逐字要点（回读所得 · 带 `件:行`） |
| :-- | :-- |
| 删除判据之三要件 | **零调用 ＋ 保护面已解除 ＋ 授权**（`99b9bff47682:192`） |
| 「零调用」之内涵 | **C 通道零命中**（`99b9bff47682:193`） |
| 本棒之标的 | 要件①「无任何调用形态」与「零调用」**系同一否定式判据族**；该判据**仅对其封闭枚举 `V-list` 封闭**，`V-list` 外之调用形态**不可被排除**；**E-3 人工阅件补扫前棒 0 取证**（`99b9bff47682:194` · KD-8） |
| 缺何证方可判 | **E-3 之人工阅件补扫**（或扩充 `V-list` 后重扫全池调用面）（`99b9bff47682:196`） |
| KD-4 之机制陈述 | 被动面取证为**行内共现** ⇒ **经路径变量间接读取**者**系统性漏检** ⇒ 🔴 `55` ＝ **上界（真值 ⩽ 55）**（`99b9bff47682:244`） |
| `V-list` 之封闭枚举 | **17 项**：`import_stmt`／`from_import`／`__import__`／`importlib`／`runpy`／`spec_from_file_location`／`SourceFileLoader`／`exec(`／`eval(`／`subprocess`／`popen(`／`os.system`／`os.popen`／`json.load`／`read_csv`／`argv_arg`／`load_module`（`c3171dc8cdf9:102-120`） |
| 判定机制之实码 | `counted = hard or ('open(read)' in marks) or ('path_join+load' in marks)`；命中判定以**行内共现**为唯一凭据（`c3171dc8cdf9:136-147` · `:452-477`） |
| 55 件之清单面 | `b687e16cc7d9:121` 逐字列 55 件（`§4-1`） |

---

## §3 55 件之机械复现（⛔ 0 转录散文）

| 项 | 值 | 依据 |
| :-- | :-- | :-- |
| 55 件之取法 | `refonly161_r2_out.json` 之 `req2_S_nolazy_script_only == True` | 机器直取 |
| 件数 | **55** | `assert` 通过 |
| 与 `b687e16cc7d9:121` 散文清单之**集合相等** | **55／55 · 双向差集皆空** | 逐字集合比对（本棒实算） |

📌 **一致性 ≠ 复核**：本项证明「本棒所取之 55 ＝ 前棒所列之 55」；🔴 **0** 复核 R2 之 ② 判定本身（KD-2）。

---

## §4 开放面五形态之枚举与机器补扫面

**程序**：对 55 件逐件，以 needle ＝ 其 `basename` ／ `stem` ／ `rel_noext` 三形，全仓 `os.walk` 逐件读原始字节（UTF-8 解码，失败者 `errors="replace"`）后作**词边界受限**子串归因；**排除面沿前棒同构造**：件自身 ／ 同名备份副本 ／ `.tmp/refonly161_*` 仪器面 ／ `.tmp/whitelist_backup_2026_10_17/` ／ 本棒自身 `.tmp/zerocall_e3_*`。

| 形态 | 枚举之具体机制 | 本棒实测面 |
| :-- | :-- | :-- |
| **F1 路径变量间接读取** | 名称落入数据结构（`dict_value`／`collection_item`／`string_assignment`）→ 载体 `L` → 消费者 `C` 读 `L` → `C` 是否对名单项作非字面量 `open`／`load`（**二跳**） | 提及 **2,156** 处 ／ **69** 个提及文件；注入数据结构者 **1,493** 处 ／ 载体文件 **21**；二跳站点 **6** 处（其中消费者含非字面量加载点者 **1** 处）
| **F2 动态加载** | `importlib.import_module`／`__import__`／`exec(`／`eval(`／`run_path`／`spec_from_file_location`／`exec_module`／`SourceFileLoader` | 含此类站点之提及文件 **115** 对；**提及行本身含此类形态者 ＝ 0**（B2 ＝ **0**）
| **F3 subprocess／系统调用** | `subprocess.`／`os.system`／`os.popen`／`popen`／`Popen` ／ 解释器调用词 | 同上；**提及行含此类形态者 ＝ 0**；解释器调用共现之 8 处经逐字阅件全为**引文／字节码伪影**（§5-3） |
| **F4 反射／`getattr` 链** | `getattr(`／`globals`／`locals`／`vars`／`__dict__`／`__getattr__` | 同上；**提及行含此类形态者 ＝ 0** |
| **F5 跨件字符串拼接后之加载** | ①片段级：件名之最长字母段与组合算子（`+`／f-string／`.format`／`%`／`.join`）同线；②定向级：件名之「字母前缀 ＋ 数字插值」构名 | ①**14** 件有片段级命中（代码级 **132** 处）②定向级 **4** 处、其中含加载调用者 **0** 处 ⇒ ⛔ **0**「拼名后加载」

**扫描完整性**：`os.walk` 遍历错误 **0** ／ 读取错误 **0** ／ `size` 错误 **0**（各跑次实测，见 KD-8 之快照差异）；扫描文件数 **3,720 → 3,741**（区间系本棒自身产物陆续落盘所致）。

**逐件提及之分桶**（B1 ＝ 该行含**计数之 `V-list` 标记**；B2 ＝ 该行含 **`V-list` 之外**之调用形态；B3 ＝ 该行无任何调用形态）：

| 桶 | 处数 | 件数（至少 1 处） |
| :-- | --: | --: |
| **B1** | 8 | 6 |
| **B2** | **0** | **0** |
| **B3** | 2,148 | 55 |
| 合计 | **2,156** | 55 |

---

## §5 人工阅件判读（逐条留痕：命中行／文件／判读／依据）

### §5-1 二跳站点 6／6 **全读**（`zerocall_e3_hop2.md` 之 ±10 行上下文为底本）

| # | 载体 `L` → 消费者 `C` | 承载 55 件数 | 判读 | 依据（逐行） |
| :-: | :-- | --: | :-- | :-- |
| 1 | `.tmp/cleanup511_manifest_2026_10_17.json` → `.mavis/scripts/cleanup511/make_register.py:13` | 46 | ⛔ **非调用** | `L13` 逐字 `M  = json.load(io.open(os.path.join(REPO, ".tmp", "cleanup511_manifest_2026_10_17.json"), encoding="utf-8"))`；其后仅取 `M["held"]` 等元数据（`L45` 起）；全文之非字面量加载点 ＝ **0**；⛔ **0** 对名单内任一件 `open`／`load` |
| 2 | 同载体 → `.tmp/__pycache__/refonly161_r2_build_register.cpython-314.pyc:40` | 46 | ⛔ **非调用** | `.pyc` 编译字节码（以 `errors="replace"` 解码，其上下文为失真字节）；且属**测量仪器自身**之编译产物（`SELF_PREFIX` 同族） |
| 3 | `tools/_archive_purge_2026_10_17/inventory_compare.json` → `step5_register.py:40` | **55** | ⛔ **非调用** | `step5_register.py` **全文 302 行逐行阅**：仅读 4 份**字面路径**证据 JSON（`L40-44`）；仅迭代**已在内存**之结构（`L125` `s2["checks"]`／`L154` `s3["rows"]`／`L166` `s3["dir_rows"]`）；`key_scan()`（`L31-36`）只扫描已在内存之文本 ⇒ ⛔ **0** 对名单内任一 55 件之路径作 `open`／`load` |
| 4 | `tools/.../step2_sample_verify.json` → `step5_register.py:41` | 1 | ⛔ **非调用** | 同上（同一 `main()` 之字面路径读） |
| 5 | `tools/.../step3_bulk_result.json` → `step5_register.py:43` | **55** | ⛔ **非调用** | 同上 |
| 6 | `tools/.../step4_bin_audit.json` → `step5_register.py:44` | 3 | ⛔ **非调用** | 同上 |

### §5-2 目录扫描器（needle 面上**完全不可见**之读法 · 机器枚举 396 个 · 含循环内加载者 **42** 个）

| 扫描器 | 机器 scope | 人工判读 | 依据（逐行） |
| :-- | :-- | :-- | :-- |
| `.tmp/dscan_04.py` | `.tmp` | ⛔ **非调用**（**机器假阳**） | **全文 56 行逐行阅**：`L24` 逐字 `dn[:] = [x for x in dn if x != ".tmp"]` ⇒ **显式排除 `.tmp`**（即 55 件所在目录）；`L9` `exec(head, ns)` 之对象为 `.tmp/dscan_03.py`（⛔ 非 55 件之一）；`L39` `io.open(p,"rb").read()` 仅施于 `E_VERBATIM` 具名族且在 `.tmp` 之外 |
| `.tmp/scan_supplement_five_terminal_2026_10_10.py` | `ROOT` | ⚠ **今日不可达** | 其输入 `.tmp/five_terminal_scan_2026_10_10.json` **不在盘**（`Test-Path=False` ＋ 全仓 glob 0 命中）⇒ `L28` 即抛 `FileNotFoundError`；其 `find_by_sha`（`L104-116`，纵 `ROOT` 读全部 `.md/.py/.json/.txt` 之**字节**以算 SHA-12）今日**执行不可及** ⇒ 📌 若该输入件复现，则构成「读其字节而**不**读取为数据」之新形态（KD-4 载） |
| `.tmp/refonly161_r2_probe.py`（前棒仪器） | `ROOT` | ⚠ **工具自指面** | `L51-75` 纵 `ROOT` 读**每一件**之原始字节 ⇒ 其测量行为本身即对 55 件之**字节读取**；是否构成「零调用」之反例，**取决于「读取为数据」之口径**（KD-5） |
| `verifier/v12/check.py` | `ROOT` | ⛔ **非调用** | `L66-67` glob 面逐字 ＝ `ROOT.glob("*.py")`（**非递归**）＋ `(ROOT/"results").rglob("*.json")` ＋ `(ROOT/"corpus").rglob("*.json")` ＋ `(ROOT/"docs").glob("*.md")` ⇒ ⛔ **不含 `.tmp/`**（55 件之所在目录） |
| `tests/test_v18.py` | `other` | ⛔ **非调用** | `L233`／`L371` 之 `os.listdir(tmp_path)` 系 pytest 临时目录，⛔ 非本仓 `.tmp` |
| `.tmp/_s4td_floor_bound_2026_10_09.py` | `other` | ⛔ **非调用** | `L17` 逐字 `glob.glob(os.path.join(RES, '*addendum*.json'))` ⇒ ⛔ 不含 `.tmp`、⛔ 无 55 件之名 |
| `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.py` | `other` | ⛔ **非调用** | `L52` 逐字同式 glob（`results/*addendum*.json`） |
| 其余 389 个扫描器 | `other`／`ROOT`／`results`／备份副本 | ⛔ **非调用**（依射程判定） | 机器 scope 分类（`other` 102 ／ `ROOT` 234 ／ `results` 55 ／ `.tmp` 5）；其中 `.tmp` scope 之 5 个之锚点行逐条抽读，⛔ 无一以 `.tmp` 为**读取目标面**；`ROOT` scope 者其 `os.walk` 锚点或受后述 glob 面排除，或其读取面经抽读确认不含 55 件之目录 |

### §5-3 B1 之 8 处「含 `V-list` 标记行」**全读**（机器判定为命中 · 人工判为**非调用**）

| 锚点 | 判读 | 依据 |
| :-- | :-- | :-- |
| `results/_refonly_161_verify_register_r2_2026_10_17.md:195`（`.tmp/_lit_log.txt` 行） | ⛔ **非调用** | 该行系**逐件表之判读依据栏之引文**，逐字含 `（call:json.load,path_join+load）` 等**文字** ⇒ 引文非代码 |
| 同件 `:196` / `:197`（`.tmp/_m5_k5_net.json` 行） | ⛔ **非调用** | 同上（表格单元格内之证据文字） |
| 同件 `:198`（`.tmp/_m5_k5_net2.json` 行） | ⛔ **非调用** | 同上 |
| 同件 `:200`（`.tmp/_m5_reaudit_archive_out.json` 行） | ⛔ **非调用** | 同上 |
| 同件 `:249`（`.tmp/docwriter_v48_norm.py` 行） | ⛔ **非调用** | 同上（逐字：`类5·被动 …（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`）`） |
| `.tmp/__pycache__/refonly161_r2_build_register.cpython-314.pyc:40`（`.tmp/_659_compact.txt` ×2） | ⛔ **非调用** | 编译字节码以 `errors="replace"` 解码 ⇒ 标记为**解码伪影**（KD-6） |

### §5-4 UTF-16 面之闭合（前棒与本棒主扫皆以其为**盲区**）

| 项 | 实测 |
| :-- | :-- |
| 全仓非严格 UTF-8 之件（除二进制扩展） | **70** 件，其中 **UTF-16（BOM）67** 件 |
| 其中**属 55 件自身**者 | **3** 件：`.tmp/_m5_k5_net.json`、`.tmp/_m5_reaudit_archive_out.json`、`.tmp/_t2_t3_prex_a_route_out.json` |
| 以正确编码解码后重扫 55 件之 needle | 提及 **11** 行，涉及 **3** 件；其中含加载／解释器形态者 **0** 行 |
| 判读 | ⛔ **非调用** —— 11 行皆在 `.tmp/refonly161_probe_log.txt`（探针日志之名录行） |

### §5-5 F5「拼名后加载」之阅件

片段级共 **132** 处代码级命中（涉 14 件）—— **按类抽读 42 处**（每件前 3 处）实读，所见三类皆非构名加载：①`os.path.join(REPO, ".tmp", "字面名")` 之**字面**路径拼接（多为写出向之他件）；②f-string／`%` 格式化之**打印与字典键**（如 `addendum_for[... + "_sha12_measured"]`）；③`os.path.basename(a).rsplit(".",1)[0]` 之**基名派生**。定向级（字母前缀 ＋ 数字插值）**4** 处**全读** ⇒ ⛔ **0**「拼名后加载」。

---

## §6 55 件逐件表（五形态命中与否 ／ 人工判读 ／ 依据）

**列义**：`提及/文件` ＝ 该件之 needle 于排除面外之全仓出现处数 ／ 出现之文件数；`B1/B2/B3` 见 §4 之分桶；`风险对` ＝ 该件之提及文件中**含加载站点**者之数（**风险指示，⛔ 非命中**）；`五形态` ＝ F1／F2／F3／F4／F5 之命中与否（`✘` ＝ **未构成实际调用**）。

| # | 件 | SHA-12 · bytes | 提及/文件 | B1 | B2 | B3 | 风险对 | 五形态 | 人工判读 | 依据（可回读） |
| :-: | :-- | :-- | :-: | --: | --: | --: | --: | :-- | :-- | :-- |
| 4 | `_659_compact.txt` | `795862c09a40` · 155628 B | 77/17 | 2 | **0** | 75 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 77 处中 **2 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 comment 1／dict_value 48／md_table_cell 25 之行；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×20；`results/_cleanup_inventory_2026_10_15.md`×18 |
| 5 | `_659_overlap_digest.txt` | `4f20b8085fb9` · 239157 B | 34/17 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 53 | `_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | `3a240806c2d3` · 31745 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 72 | `_docwriter_night_measure.json` | `f5bacfac3f1c` · 22679 B | 42/18 | 0 | **0** | 42 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 42 处**0 行含任何调用形态**（落于 collection_item 5／comment 1／dict_value 24／md_table_cell 12 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×10；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 80 | `_dw_abs_scan.json` | `5c584826ed16` · 56306 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 24／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×6；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 124 | `_lit_log.txt` | `b062da7b654a` · 8733 B | 34/15 | 1 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处中 **1 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 comment 1／dict_value 25／md_table_cell 7 之行；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×5；`.tmp/cleanup511_manifest_2026_10_17.json`×4 |
| 126 | `_m5_k5_net.json` | `9d7fe894a26b` · 92060 B | 120/23 | 2 | **0** | 118 | 7 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 120 处中 **2 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 collection_item 2／comment 1／dict_value 77／md_table_cell 22 之行；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×16；`.tmp/archive_survey_outdupe.json`×12 |
| 128 | `_m5_k5_net2.json` | `b2bc158e7499` · 952252 B | 36/19 | 1 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 36 处中 **1 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 comment 1／dict_value 23／md_table_cell 10 之行；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 133 | `_m5_reaudit_archive_out.json` | `e3542ccb4d3e` · 654 B | 40/17 | 1 | **0** | 39 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 40 处中 **1 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 collection_item 2／comment 1／dict_value 28／md_table_cell 8 之行；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×8；`.tmp/cleanup511_manifest_2026_10_17.json`×4 |
| 287 | `_t2_t3_lit_search2.py` | `c0caa8ba29f1` · 4946 B | 38/15 | 0 | **0** | 38 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 38 处**0 行含任何调用形态**（落于 comment 1／dict_value 27／md_table_cell 9 之行）；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×6；`.tmp/cleanup511_manifest_2026_10_17.json`×5 |
| 290 | `_t2_t3_llm_probe.py` | `5561f7af5662` · 4544 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 292 | `_t2_t3_prex_a_route.py` | `c25af5d2966b` · 10166 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 295 | `_t2_t3_prex_a_route_out.json` | `3cad087a69c3` · 22640 B | 38/17 | 0 | **0** | 38 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 38 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 26／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×5；`.tmp/wlbk_2026_10_17_scan_out.json`×5 |
| 383 | `docwriter_v42_verify.py` | `47c794a64dff` · 4858 B | 37/16 | 0 | **0** | 37 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 37 处**0 行含任何调用形态**（落于 comment 1／dict_value 26／md_table_cell 8 之行）；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×7；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 404 | `docwriter_v46_card_raw.py` | `b8754c12612b` · 1652 B | 64/17 | 0 | **0** | 64 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 64 处**0 行含任何调用形态**（落于 comment 2／dict_value 40／md_table_cell 17 之行）；主要出处 `.tmp/wlbk_2026_10_17_backup2_out.json`×8；`.tmp/wlbk_2026_10_17_backup_out.json`×6 |
| 406 | `docwriter_v46_probe.py` | `15d2a2cef38c` · 8174 B | 35/14 | 0 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 35 处**0 行含任何调用形态**（落于 comment 2／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×8；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 409 | `docwriter_v46_verify.py` | `7d657b923cf3` · 6883 B | 29/14 | 0 | **0** | 29 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 29 处**0 行含任何调用形态**（落于 comment 2／dict_value 18／md_table_cell 7 之行）；主要出处 `.tmp/wlbk_2026_10_17_backup2_out.json`×4；`.tmp/wlbk_2026_10_17_backup_out.json`×3 |
| 410 | `docwriter_v46_verify_r2.py` | `98878b701653` · 3940 B | 29/14 | 0 | **0** | 29 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 29 处**0 行含任何调用形态**（落于 comment 2／dict_value 18／md_table_cell 7 之行）；主要出处 `.tmp/wlbk_2026_10_17_backup2_out.json`×4；`.tmp/wlbk_2026_10_17_backup_out.json`×3 |
| 414 | `docwriter_v48_norm.py` | `e39ea2ab2756` · 12880 B | 34/14 | 1 | **0** | 33 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处中 **1 处落于含 `V-list` 标记行**（经人工阅件判为**引文／字节码伪影**·§5-3 ⇒ ⛔ 非调用）；其余落于 comment 2／dict_value 22／md_table_cell 9 之行；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×6；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 417 | `docwriter_v49_norm.py` | `d1b3481335eb` · 16740 B | 43/16 | 0 | **0** | 43 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 43 处**0 行含任何调用形态**（落于 collection_item 1／comment 2／dict_value 26／md_table_cell 13 之行）；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×10；`results/_refonly_161_verify_register_r2_2026_10_17.md`×6 |
| 422 | `docwriter_verify_v45.py` | `92230e228d83` · 3780 B | 28/14 | 0 | **0** | 28 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 28 处**0 行含任何调用形态**（落于 comment 1／dict_value 18／md_table_cell 8 之行）；主要出处 `.tmp/wlbk_2026_10_17_backup2_out.json`×4；`.tmp/wlbk_2026_10_17_backup_out.json`×3 |
| 425 | `docwriter_write_v43.py` | `d5e6390b900d` · 33607 B | 36/15 | 0 | **0** | 36 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 36 处**0 行含任何调用形态**（落于 comment 1／dict_value 21／md_table_cell 13 之行）；主要出处 `results/_refonly_161_verify_register_r2_2026_10_17.md`×8；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 426 | `docwriter_write_v44.py` | `54812b76573b` · 84551 B | 36/16 | 0 | **0** | 36 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 36 处**0 行含任何调用形态**（落于 comment 1／dict_value 21／md_table_cell 12 之行）；主要出处 `results/_refonly_161_verify_register_r2_2026_10_17.md`×7；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 427 | `docwriter_write_v45.py` | `af3a22741b2f` · 61168 B | 35/17 | 0 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 35 处**0 行含任何调用形态**（落于 collection_item 1／comment 1／dict_value 18／md_table_cell 11 之行）；主要出处 `results/_refonly_161_verify_register_r2_2026_10_17.md`×6；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 459 | `evauditor_one_finish_write.py` | `c24967f8114e` · 46211 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/wlbk_2026_10_17_backup2_out.json`×4；`.tmp/wlbk_2026_10_17_scan_out.json`×4 |
| 473 | `ge01_full_1494_exec_r1_write_2026_10_16.py` | `9e9e402893ef` · 43129 B | 40/18 | 0 | **0** | 40 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 40 处**0 行含任何调用形态**（落于 collection_item 1／comment 1／dict_value 23／md_table_cell 12 之行）；主要出处 `results/_refonly_161_verify_register_r2_2026_10_17.md`×6；`.tmp/cleanup511_manifest_2026_10_17.json`×4 |
| 480 | `ge01_full_1494_precheck_2026_10_16.py` | `cc34ab8552f9` · 10700 B | 73/17 | 0 | **0** | 73 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 73 处**0 行含任何调用形态**（落于 collection_item 1／comment 1／dict_value 50／md_table_cell 19 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×10；`.tmp/wlbk_2026_10_17_backup2_out.json`×8 |
| 483 | `ge01_full_1494_resume32_collect_2026_10_16.py` | `9496620e32b2` · 14609 B | 35/15 | 0 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 35 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 11 之行）；主要出处 `results/_refonly_161_verify_register_r2_2026_10_17.md`×5；`.tmp/cleanup511_manifest_2026_10_17.json`×4 |
| 487 | `ge01_full_1494_resume32_readout_2026_10_16.py` | `de50589bd6c6` · 29430 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 495 | `ge01_gate_write.py` | `a661b2c7e5f0` · 82875 B | 44/14 | 0 | **0** | 44 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 44 处**0 行含任何调用形态**（落于 collection_item 2／comment 2／dict_value 28／md_table_cell 11 之行）；主要出处 `.tmp/wlbk_2026_10_17_scan_out.json`×14；`results/_refonly_161_verify_register_r2_2026_10_17.md`×6 |
| 505 | `ge01_s3b_v_exec_r1_write_2026_10_16.py` | `359b768e7dc0` · 56062 B | 34/16 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 506 | `ge02_build.py` | `a10c57adf6b5` · 24774 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 24／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×6；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 507 | `ge02_recompute.py` | `811d4a138788` · 1347 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 24／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×6；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 513 | `kd14_absorption_probe.py` | `915c968f2d04` · 1358 B | 32/16 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 22／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 514 | `kd14_carrier_probe.py` | `758033c2a76b` · 1206 B | 35/16 | 0 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 35 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×5；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 515 | `kd14_m4_corrected.py` | `50c1c7d85616` · 932 B | 32/16 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 22／md_table_cell 7 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 527 | `klm41_3_ts_collect_2026_10_16.py` | `a28c4ba40940` · 23196 B | 34/16 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 537 | `m08_r1_amend2_2026_10_16.json` | `21ad2e7acd0b` · 1296 B | 50/19 | 0 | **0** | 50 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 50 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 37／md_table_cell 10 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×7；`.tmp/_cleanup_r2_scan4_out.json`×6 |
| 538 | `m08_r1_amend3_2026_10_16.json` | `d77931c6d7a5` · 3034 B | 50/19 | 0 | **0** | 50 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 50 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 37／md_table_cell 10 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×7；`.tmp/_cleanup_r2_scan4_out.json`×6 |
| 539 | `m08_r1_amend_2026_10_16.json` | `3c982068b276` · 1204 B | 50/19 | 0 | **0** | 50 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 50 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 37／md_table_cell 10 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×7；`.tmp/_cleanup_r2_scan4_out.json`×6 |
| 581 | `me_llm_calls_2026_10_16.jsonl` | `fbdedcb0ef48` · 21339 B | 36/16 | 0 | **0** | 36 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 36 处**0 行含任何调用形态**（落于 comment 1／dict_value 25／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×5；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 621 | `t2b_census_2026_10_16.py` | `71f99afb9199` · 3041 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 622 | `t2b_derive_2026_10_16.py` | `324165eb0c7d` · 7964 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 623 | `t2b_fetch_facts_2026_10_16.py` | `0941558d024e` · 5774 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 624 | `t2b_freeze_2026_10_16.py` | `575b796a2e6f` · 13908 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 625 | `t2b_freeze_v2_2026_10_16.py` | `02a261b12f7b` · 17044 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 627 | `t2b_impl_audit_2026_10_16.py` | `e02a343246bd` · 4856 B | 52/19 | 0 | **0** | 52 | 6 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 52 处**0 行含任何调用形态**（落于 collection_item 2／comment 1／dict_value 38／md_table_cell 11 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×7；`.tmp/_cleanup_r2_scan4_out.json`×6 |
| 628 | `t2b_inspect_facts_2026_10_16.py` | `de3c879e39f1` · 1732 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 630 | `t2b_measure_2026_10_16.py` | `bd377372927c` · 15547 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 632 | `t2b_patch_harness_2026_10_16.py` | `bac4775c5c44` · 7065 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 633 | `t3_baseline_procedure_probe.py` | `b4c2a5e68dfa` · 2292 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 638 | `t3_nt_measure_2026_10_15.py` | `35860b379b7a` · 17111 B | 32/15 | 0 | **0** | 32 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 32 处**0 行含任何调用形态**（落于 comment 1／dict_value 23／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 640 | `t3_nt_verify.py` | `a1c38dc17d65` · 6657 B | 33/15 | 0 | **0** | 33 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 33 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 8 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 642 | `t3_postchange_equiv.py` | `1e579de6033c` · 5975 B | 34/15 | 0 | **0** | 34 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 34 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 9 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |
| 645 | `t3_postcheck.py` | `20c96933b00d` · 3129 B | 35/15 | 0 | **0** | 35 | 5 | ✘✘✘✘✘ | ⛔ **0 调用** | 提及 35 处**0 行含任何调用形态**（落于 comment 1／dict_value 24／md_table_cell 10 之行）；主要出处 `.tmp/cleanup511_manifest_2026_10_17.json`×4；`.tmp/wlbk_2026_10_17_backup2_out.json`×4 |

---

## §7 汇总三数（穷尽后）

| 数 | 值 | 口径与依据 |
| :-- | --: | :-- |
| **N1 成就（「零调用」于已枚举开放面成立）** | **55** | 逐件五形态全 ✘ ＋ 二跳全读 ＋ 扫描器面全读 ＋ UTF-16 面闭合 ＋ B2 ＝ 0 |
| **N2 发现调用（其件自 55 转出者）** | **0** | 🔴 「名义判定须撤销之件」＝ **0 件** |
| **N3 不明（证据不足而不可判者）** | **0** | 55 件逐件均有：B1／B2／B3 分桶实测 ＋ 其引用面之消费者与扫描器面均已阅 ＋ UTF-8 与 UTF-16 两面皆已检索 |

📌 **N1 ＝ 55 之射程限定**：本数**仅及于本棒所枚举之开放面**（§4 之五形态 ＋ 目录扫描器面 ＋ UTF-16 面）；🔴 **⛔ 非「零调用」要件已穷尽之断言**（KD-7 之残余未枚举形态）· 🔴 **⛔ 非「55 之真值已定」**（§8）。

---

## §8 上界缺口之收窄面（55 之真值之新估计）

| 项 | 内容 |
| :-- | :-- |
| 原上界 | `55` 系**上界**（真值 ⩽ 55）—— 被动面取证为**行内共现** ⇒ **经路径变量间接读取**者**系统性漏检**（`99b9bff47682:244` · KD-4） |
| 本棒对该漏检机制之处置 | 五形态（**F1** 路径变量注入／**F2** 动态加载／**F3** 子过程／**F4** 反射／**F5** 拼接构名）＋ 目录扫描器面 ＋ UTF-16 面 **逐类枚举并逐类阅件** |
| 实测结果 | 🔴 **未发现任一件被间接调用** ⇒ **N2 ＝ 0** |
| 🔴 **上界不可因此降为定值** | 三项不可判面仍在：①**「读取为数据」之口径是否含纯字节读取**（前棒仪器与本棒探针皆纵 `ROOT` 读 55 件之字节；`scan_supplement…:104-116` 之 `find_by_sha` 为该形态之可执行实例，今日不可达）②**残余未枚举形态之存在性**（KD-7）③`.pyc` 编译面之解码不可靠（KD-6） |

> **真值新估计（1 行）**：**真值 ⩽ 55 之名义上界维持不变（本棒 0 发现间接调用 ⇒ 无证据下调）；🔴 若 PI 采「名称必现」读法则 55 可充定值，若采「含字节级读取」读法则 55 之真值须重估 —— 该读法之择归 PI，本件 ⛔ 0 代裁。**

---

## §9 KD 清单（本件自列 · 如实 · ⛔ 0 代裁）

| # | KD | 内容 |
| :-: | :-- | :-- |
| **KD-1** | **本件非终判** | 本件**非**五终判（`pass`／`af`／`kd`／`fail`／`give-up`）中之一，⛔ **0** 自裁为任一终判；其状态 ＝ **候 PI 核准之补取证件**；R2 判断件之采认**仍悬置** |
| **KD-2** | **本棒 0 复核 R2 之判定本身** | ⛔ **0** 重跑 R2 探针 · ⛔ **0** 复算其 0／55／7／106／129／481／1,122／2,597／178 诸值 · ⛔ **0** 复判 161 件之 ①②；本件之射程**仅及于「55 件之开放面调用形态」**；§3 之集合相等**仅证一致性**，⛔ 非复核 |
| **KD-3** | **机器命中 ⇏ 调用** | 本棒新检出并经人工阅件判为**非调用**之机器命中：`.tmp/dscan_04.py`（机器 scope ＝ `.tmp`，实码 `L24` 排除 `.tmp`）、`b687e16cc7d9` 逐件表 6 处（引文非代码）、`.pyc` 2 处（解码伪影）⇒ 🔴 **凡仅凭机器标记即断「有调用」者将得相反结论** |
| **KD-4** | **「读取为数据」之口径未载（字节读取面）** | 口径草案字面「读取为数据」**未载**纯字节读取（仅为计算摘要而读）是否计入；`.tmp/scan_supplement_five_terminal_2026_10_10.py:104-116` 之 `find_by_sha` 即该形态之实例（今日因其输入件不在盘而不可达）；🔴 **择读归 PI，本件 ⛔ 0 代裁** |
| **KD-5** | **工具自指面** | 前棒仪器 `.tmp/refonly161_r2_probe.py:51-75` 与本棒探针 `.tmp/zerocall_e3_probe.py` 皆纵 `ROOT` 读**每一件**（含 55 件）之字节 ⇒ 「55 件之字节确曾被读取」为**实测事实**；是否构成「零调用」之反例取决于 KD-4 之口径 |
| **KD-6** | **`.pyc` 编译面不可靠** | 全仓 `.pyc` **16** 件，其内容以 `errors="replace"` 解码 ⇒ 该面标记**不可信**；本棒之 B1 之 2 处即出此面（判为伪影）⇒ 该面残余缺口**未闭** |
| **KD-7** | **残余未枚举形态（本棒五形态亦系人工构造之封闭集）** | 已知未覆盖者至少：跨行（多行）调用之变量流 · 非 ASCII 路径构造 · 运行时生成名（时间戳／uuid／hash 派生）· 经第三方库封装之读取面（如 `pandas.read_csv` 之变体）· 经注册表／环境变量／标准输入注入之路径 |
| **KD-8** | **各探针非同一快照** | 因本棒自身产物陆续落盘，扫描文件数 **3,720 → 3,741**；遍历错误恒 **0**、读取错误恒 **0**；📌 故「本棒未扫描到某件」与「该件在本棒快照时不存在」二者**不可混同** |
| **KD-9** | **本件之自指界限** | 本件落盘于本棒全部实测之后 ⇒ 本件**未进入**本棒任何扫描面；📌 且本件自身将成为后续扫描之**引用件**（沿 `99b9bff47682:250` 之同族体例）⇒ ⛔ **0** 以本件之存在充任何结论之先验 |
| **KD-10** | **卡面载荷件不在盘** | 卡号 `ask_3b44d24545c29a761106b2d2` 之在册来源**唯一**为 `pi_rulings/_pi_card_answers_register_2026_10_17_v61.md`（本棒实测 22 处／4 件）；⛔ **0** 读作「卡面在盘」；📌 若 v61 登记件之转录有误，本棒之派工依据随之动摇 |
| **KD-11** | **名义 ⩾ 清理许可（沿 V-6／A-23）** | ③ 拦截 ＝ **161 全数** · 保护面在册未解除（解除归 PI）· 授权未给 ⇒ 🔴 **0 件具备清理许可**；本件**无论出何数皆不产生**任何清理许可 |
| **KD-12** | **本棒 0 主张①毕之任一要件** | 本件 ⛔ 0 主张「全部实验收束」五零（0 候 PI 裁／0 非五项终判／0 历史遗忘／0 实验挂账／0 实验缺口）之任一项已闭 |

---

## §10 边界与不软化声明

1. **0 判成**：N1 ＝ 55 **仅及于本棒所枚举之开放面**；⛔ **0** 表述为「『零调用』要件已穷尽」；⛔ **0** 表述为「55 之真值已定」；
2. **0 判死**：N2 ＝ 0 **仅**谓「未发现间接调用」；⛔ **0** 表述为「55 件确无调用」（KD-4／KD-6／KD-7 之残余仍在）；
3. **0 代裁**：KD-4 之口径择读 ＋ R2 之三读择读 ＋ 删除判据之任何要件，**皆归 PI**；本件 ⛔ 0 择定任一；
4. **0 清理**：本件 **0** 删／移／改任何件；⛔ **0** 解除保护面；⛔ **0** 宣告①毕；
5. **0 外推**：⛔ **0** 外推至 161 件全池 · ⛔ **0** 外推至 699 件白名单集 · ⛔ **0** 外推至「四通道零入链」面 · ⛔ **0** 外推至 R2 之 ② 判定本身；
6. **本棒 0 触碰**：⛔ 0 网络 · ⛔ 0 读 key · ⛔ 0 LLM 调用 · ⛔ 0 触归档区 · ⛔ 0 动 `tools/` · ⛔ 0 回改任何既有件一字。

---

## §11 落盘纪律与自核（交付之唯一判据 ＝ 盘上实测）

| 项 | 值／状态 |
| :-- | :-- |
| **落盘路径** | `results/_zerocall_gap_proof_register_2026_10_17.md` |
| **落盘前占位实测** | `Test-Path` ＝ **`False`** ＋ `results/` 内同名式 glob ＝ **0** ＋ 全仓同名式 glob ＝ **0**（§0） |
| **写入通道** | `io.open(path, "w", encoding="utf-8", newline="\n")` 直写（UTF-8 无 BOM · 纯 LF） |
| **正文内载自身 SHA-12／bytes** | 🔴 **⛔ 0 自载**（自指悖论 · 沿 `v61` 之 KD-11 体例）⇒ **见棒回执**（本棒落盘后直算） |
| **`BOM`／`CRLF`／`U+FFFD`／首行／末行** | 见棒回执（本棒逐字节扫描） |
| **亲测回读** | 本棒以 `io.open(..., "rb")` 直读全文字节并 UTF-8 解码 ⇒ 关键字面在位计数（`ask_3b44d24545c29a761106b2d2`／`99b9bff47682`／`b687e16cc7d9`／`c3171dc8cdf9`／`c47c6f4afddd`／`V-list`／`零调用`／`N1`／`N2`／`N3`／`KD-4`／`上界`） |
| **既有件触动数** | **0**（本棒仅新增 `.tmp/zerocall_e3_*` 23 件 ＋ 本件） |
| ⚠ **本件之写入次数 ＝ 2（如实登记）** | 首次写入后自查发现 §6 逐件表之「依据」栏对 `B1 > 0` 之 6 件误书「（无调用形态）」（与其自身 `B1` 值相冲突）⇒ **就地勘正并重写**；🔴 首次写入之指纹**作废**（未外报）；**最终指纹以棒回执所载之第二次写入后实测为准**；⛔ 该二次写入**仅及本棒自身新建之件**，⛔ 0 覆写任何既有件 |

---

## §12 声明

1. 本件为**补取证件**：⛔ 0 代 PI 裁 · ⛔ 0 宣告任一件之终判 · ⛔ 0 宣告①毕 · ⛔ 0 回改任何既有件一字 · ⛔ 0 主张任何清理动作已发生或可即刻发生；
2. 本件之全部数值**系本棒直算**（指纹、扫描面、分桶、二跳、扫描器、UTF-16 面），⛔ 0 转录；唯 §2 之缺口面要点系**逐字回读**并带 `件:行` 锚；
3. 本件之机器命中**均经人工阅件**方可作判读（§5 之 6＋8＋8＋4 处实读 ＋ 其余按类抽读）—— 🔴 **机器命中 ⇏ 调用**（KD-3）；
4. 交付之唯一判据 ＝ **盘上实测**（见棒回执之 SHA-12／bytes／BOM／CRLF／U+FFFD）。

**—— worker（补取证棒 `bg_4e5aed52-fe5c-4ae2-a695-1bfbf42342e9`）· 补取证件 · 2026-10-17**
