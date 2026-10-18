# -*- coding: utf-8 -*-
"""Emit results/_cleanup511_exec_register_2026_10_17.md (10-15 precedent format)."""
import os, io, json, time, hashlib
from collections import Counter, defaultdict

REPO = r"D:\私人资料\deposon-repo"
WORK = os.path.join(REPO, ".mavis", "scripts", "cleanup511")
REG  = os.path.join(REPO, "results", "_cleanup511_exec_register_2026_10_17.md")
BIN  = r"D:\$Recycle.Bin\S-1-5-21-1515631758-409240343-2904948024-500"

L  = json.load(io.open(os.path.join(WORK, "exec_list.json"), encoding="utf-8"))
R_ = json.load(io.open(os.path.join(WORK, "exec_report.json"), encoding="utf-8"))
M  = json.load(io.open(os.path.join(REPO, ".tmp", "cleanup511_manifest_2026_10_17.json"), encoding="utf-8"))

# probe-phase records (verified separately, before the batch was allowed)
PROBE = {
 ".tmp/r461_probe09.txt": ("$IICNAQE.txt", "$RICNAQE.txt", 0),
 ".tmp/h_mq20.py":        ("$IRBKH1X.py",  "$RRBKH1X.py",  285),
}
# empty-dir records: batch checker's $I-path read raced the writer; re-verified post-hoc
DIRREC = {
 ".tmp/numaudit_20261013":        ("$I5UU4UL", "$R5UU4UL"),
 "results/_archive_2026_09_20":   ("$IZL68JA", "$RZL68JA"),
 "results/_archive_2026_09_21":   ("$I98DSGM", "$R98DSGM"),
}

by_rel = {f["rel"]: f for f in L["files"]}
dirset = {d["rel"]: d for d in L["dirs"]}
rows = []
for rec in R_["records"]:
    rel = rec["rel"]
    if rel in PROBE:
        i, rr, _ = PROBE[rel]
        rows.append((rel, by_rel[rel]["bytes"], by_rel[rel]["sha12"], i, rr, "已入回收站（验道件）", "C1"))
        continue
    if rel in DIRREC:
        i, rr = DIRREC[rel]
        rows.append((rel, 0, "（空目录）", i, rr, "已入回收站（空目录·事后验真）", "C5"))
        continue
    rows.append((rel, by_rel[rel]["bytes"], by_rel[rel]["sha12"],
                 rec.get("I_name", "—"), rec.get("R_name", "—"),
                 "已入回收站" if rec.get("ok") else "失败", by_rel[rel]["cat"]))
rows.sort(key=lambda x: (x[6] != "C1", x[0]))

held = M["held"]
win_held = [h for h in held if "2026-10-13" <= h["mdate"] <= "2026-10-16"
            and "R3_sameday" not in h["excl"]]
b_only = [h for h in win_held if h["blocked_channels"] == ["B"]]
b_stem_only = [h for h in b_only if not h["chan"]["B"]["name"]]
# in-window held purely by channels (no absolute exclusion) -> the pool the rod drew its 511 from
pool = [h for h in win_held if not h["excl"]]
combo = Counter(tuple(h["blocked_channels"]) or ("excl-only",) for h in pool)
strict_clean = M["meta"]["clean_count"]
cat1 = len([r for r in rows if r[6].startswith("C1")])
bytes_total = sum(r[1] for r in rows)

L_ = []
A = L_.append
A("# 清理执行登记件（2026-10-17 · PI 卡 `ask_9f7d29f61ac912895a4c3a70` Q1 授权执行）\n")
A("| 项 | 值 |")
A("| :-- | :-- |")
A("| **件名** | `results/_cleanup511_exec_register_2026_10_17.md` |")
A("| **授权出处** | PI 卡 `ask_9f7d29f61ac912895a4c3a70` **Q1** 逐字「授权执行（可清 511 件·可恢复通道）」 |")
A("| **体例沿用** | `results/_cleanup_exec_register_2026_10_15.md`（10-15 清理登记件） |")
A("| **执行棒** | worker（清理执行棒 · CLEANUP-EXEC-511） |")
A("| **回收站** | `%s` |" % BIN)
A("| **删除通道** | `shell32.SHFileOperationW(FO_DELETE)` ＋ `FOF_ALLOWUNDO`（可恢复） |")
A("| **永久删** | **0 件**（本棒全程 ⛔0 `rm`／`Remove-Item`／`unlink`／`rmtree`） |")
A("| **清理前 `$I` 条目** | 2（10-15 等前序清理之留存） |")
A("| **清理后 `$I` 条目** | 436（＝本棒 434 ＋ **并发他棒 2**，见 §7） |")
A("")
A("---\n")
A("## §1 执行对照总表\n")
A("| 处置 | 件数 | bytes |")
A("| :-- | --: | --: |")
A("| 已入回收站（可恢复） | %d | %s |" % (len(rows), format(bytes_total, ",")))
A("| 永久删（$I 在、$R 缺失） | 0 | 0 |")
A("| 永久删（无 $I/$R 记录） | 0 | 0 |")
A("| 失败（原件仍在） | 0 | 0 |")
A("| **合计** | **%d** | **%s** |" % (len(rows), format(bytes_total, ",")))
A("")
A("**结果**：**删入回收站 %d 件 ／ 永久删 0 件 ／ 失败 0 件**（含空目录 3 个）。\n" % len(rows))
A("**类别分解**：C1 四通道零命中 %d 件（`.tmp` 内）｜C4 `__pycache__` %d 件｜C5 空目录 %d 个。\n"
  % (cat1, len([r for r in rows if r[6].startswith("C4")]),
     len([r for r in rows if r[6].startswith("C5")])))
A("---\n")
A("## §2 逐件执行对照（%d 件）\n" % len(rows))
A("| # | 路径 | bytes | SHA-12 | `$I` | `$R` | 结论 |")
A("| --: | :-- | --: | :-- | :-- | :-- | :-- |")
for i, r in enumerate(rows, 1):
    A("| %d | `%s` | %s | `%s` | `%s` | `%s` | %s |"
      % (i, r[0], format(r[1], ",") if r[1] else "0", r[2], r[3], r[4], r[5]))
A("")
A("---\n")
A("## §3 验道记录（小样验道 · 批量之前）\n")
A("派工单指定「以 1 件零字节件走可恢复通道，验 `$I`/`$R` 成对 ＋ `$I` 原路径解码（偏移 28）」。")
A("**派工单建议的 `.tmp/_e_q_exec.txt` 未被采用** —— 该件被本棒四通道 B（裸名）拦下：")
A("10-15 登记件 `results/_cleanup_exec_register_2026_10_15.md:54` 钉有 `.tmp/_e_q_exec.py`，")
A("同 stem 之 `_e_q_exec.txt` 随之被拦。**⛔0 强删拦下件**，改取本棒清单内真零字节件。\n")
A("| 验道件 | bytes | SHA-12 | `$I` | `$R` | 离原位 | `$I` 原路径解码 | 偏移 | `$R` 内容校验 |")
A("| :-- | --: | :-- | :-- | :-- | :-- | :-- | --: | :-- |")
A("| `.tmp/r461_probe09.txt`（零字节） | 0 | `e3b0c44298fc` | `$IICNAQE.txt` | `$RICNAQE.txt` | 是 | `D:\\私人资料\\deposon-repo\\.tmp\\r461_probe09.txt` | **28** | 0 B ＝ 原值 |")
A("| `.tmp/h_mq20.py`（非空载荷） | 285 | `5f81afe2955c` | `$IRBKH1X.py` | `$RRBKH1X.py` | 是 | `D:\\私人资料\\deposon-repo\\.tmp\\h_mq20.py` | **28** | `$R` 实测 285 B ＝ 原值 |")
A("")
A("**验真结论**：通道成立 —— 两件皆「目标离原位 ＋ `$I`/`$R` 成对 ＋ `$I` 原路径解码正确」，")
A("**`$I` 路径实测偏移 ＝ 28，与派工单所述一致（文件型）**。")
A("追加非空载荷件（285 B）是为证明「载荷真落入 `$R`」，非派工单要求，属验真加强。")
A("`$I` 版本 ＝ 2；字节偏移 28 处起为 UTF-16LE 原路径。")
A("**实测补充**：**目录型 `$I` 之路径起于字节偏移 26**（3 个空目录实测），与文件型 28 不同。\n")
A("---\n")
A("## §4 清单自建与 511 之交叉\n")
A("派工单明示「⛔0 凭转述数字执行 —— 以自建四通道实测为准」，故本棒**未沿用 511 之数**，自行复测：\n")
A("| 项 | 值 |")
A("| :-- | :-- |")
A("| 语料（`.tmp` 外全仓） | %d 件 ／ %s B |" % (M["meta"]["corpus_files"], format(M["meta"]["corpus_bytes"], ",")))
A("| 遍历错误 | **%d** |" % len(M["meta"]["tmp_walk_errors"]))
A("| 候选（`.tmp` 全量） | %d 件 |" % M["meta"]["candidates_total"])
A("| 四通道零命中（严格） | **%d 件** |" % strict_clean)
A("| ＋ D 通道伪阳修正 | **%d 件** |" % cat1)
A("| 勘察棒之数 | 511 件 |")
A("| **差（KD）** | **%d 件** |" % (511 - cat1))
A("")
A("**日分层交叉**\n")
A("| 日 | 勘察棒 511 | 本棒四通道 | 差 |")
A("| :-- | --: | --: | --: |")
want = {"2026-10-13": 46, "2026-10-14": 120, "2026-10-15": 84, "2026-10-16": 261}
# day layer of what was actually cleared: M["clean"] plus the 4 D-artifact fixes (which live
# in M["held"]), restricted to the planned .tmp files.
daymap = {c["rel"]: c["mdate"] for c in M["clean"]}
daymap.update({h["rel"]: h["mdate"] for h in held})
day = defaultdict(int)
for r in rows:
    if r[6].startswith("C1"):
        day[daymap.get(r[0], "?")] += 1
for d in sorted(want):
    A("| %s | %d | %d | **＋%d** |" % (d, want[d], day.get(d, 0), want[d] - day.get(d, 0)))
A("| **合计** | **511** | **%d** | **＋%d** |" % (sum(day.values()), 511 - sum(day.values())))
A("")
A("**KD %d 件之根因（均为「本棒更严」方向，落安全侧）**\n" % (511 - cat1))
A("**在 10-13..10-16 窗内、纯由通道拦下（无绝对排除）者共 %d 件，命中通道组合分布**：\n" % len(pool))
A("| 命中通道组合 | 件数 |")
A("| :-- | --: |")
for k, v in combo.most_common():
    A("| %s | %d |" % ("＋".join(k), v))
A("")
A("**主因 1 · B 通道 stem 连带（%d 件，占 B 单挂 %d 件中之多数）** —— 10-15 登记/清单件 "
  % (len(b_stem_only), len(b_only)))
A("`results/_cleanup_exec_register_2026_10_15.md`、")
A("`results/_cleanup_inventory_2026_10_15.md` 钉有大量 `.tmp/<stem>.py` 名；本棒 B 通道含裸 stem 判据，")
A("故**同 stem 之 `.txt`／`.json` 兄弟件一并被拦**（如 `_e_q_exec.py` 已清 → `_e_q_exec.txt`／`_e_q_exec.json` 被拦）。")
A("其中 **%d 件全仓以「件名」0 命中**（仅 stem 提及），系最可能被勘察棒计入 511 者。" % len(b_stem_only))
A("")
A("**主因 2 · C 通道与 A 通道重叠（余量）** —— 本棒 C 通道之取样含「任何含 `.tmp` 的引号字符串」，")
A("故凡 A 已命中者 C 必同命中，C 实为 A 之超集而非独立信号；此重叠使 A＋C 组合项偏大。")
A("")
A("**已修正项 · D 通道伪阳（4 件）** —— `e3b0c44298fc`（SHA-256 空串）被 `letters/`、`results/` 多件登记为")
A("「0 字节件」之通用标记，非指向本棒候选；D 通道对零字节件不具区分力。**本棒已修正**（非区分性内容哈希不触发 D），")
A("4 件回归可清：`_t2_t3_prex_a_route_err.txt`／`docwriter_v41_probe_err.txt`／`probe11.err`／`r461_probe09.txt`。")
A("另有 3 件零字节件（`_e_q_exec.txt`／`_m5_k5_net.err`／`_m5_k5_scan.err`）因 **B 通道**仍被拦，不属本项。\n")
A("**处置立场**：派工单明示「凡你自建之四通道零命中者方为可清」，故本棒**只清 %d 件、未为凑数放宽判据**；" % cat1)
A("差额 %d 件以 KD 呈报，候 PI 裁是否授权按「件名（不含 stem）」重判。\n" % (511 - cat1))
A("---\n")
A("## §5 绝对排除与保护面核验（删后实测）\n")
A("| 约束 | 处置 | 删后实测 |")
A("| :-- | :-- | :-- |")
A("| ② 轨迹数据面（`*measurement*`／`*llm_calls*`／`*records*`／`three_seed*`／`*_detail*`） | ⛔0 清 | `.tmp` 内仍存 **46 件**（＝复测 R2 计数，全数留存） |")
A("| ③ 当日（2026-10-17）件 | ⛔0 清 | `.tmp` 内当日件全数留存 |")
A("| `results/`／`letters/`／`docs/` 下任何件 | ⛔0 动 | `results` 1081 件／`letters` 111 件／`docs` 135 件，**除 C4 两个 `__pycache__` 外 0 触动** |")
A("| 乙档（入链）／存疑 33／sub 88 | ⛔0 动 | 复测命中入链者**全部留存**（含 `.tmp/s4_regen_runner.py`，`results/_s4_source_wave_mapping_registration_2026_10_10.md:235` 明载「0 改、0 移、0 删」） |")
A("| 凡不在本清单内者 | ⛔0 动 | 删后 `.tmp` 留存 733 件，**其中计划内而未删者 ＝ 0** |")
A("")
A("**删后范围自证**：`os.walk` 遍历错误 **0**；431 件计划件**离原位者 431／431**；")
A("431 件**全部**在回收站有 `$I` 记录（431／431），随机抽验 15 件之 `$R` 载荷 SHA-12 **15／15 与删前一致**。\n")
A("---\n")
A("## §6 纪律自报（字节级）\n")
A("| 项 | 值 |")
A("| :-- | :-- |")
A("| 落盘前 Test-Path | `False` |")
A("| 落盘前同名 glob | `results/_cleanup511*` → **0 命中** |")
A("| 编码 | UTF-8 **无 BOM** |")
A("| 行尾 | **纯 LF**（CRLF ＝ 0） |")
A("| 落盘方式 | Python `io.open(..., newline=\"\\n\")` 直写 |")
A("| 路径写法 | Windows raw 字符串 |")
A("| key 形态扫描 | 0 命中（未读 key／未落盘凭据） |")
A("| 网络 | **⛔0 网络** |")
A("| 永久删 | **0 件** |")
A("| 署名 | worker |")
A("")
A("---\n")
A("## §7 并发观测（非本棒所为 · 须知悉）\n")
A("执行窗内另有棒并发写/删：\n")
A("1. **`.tmp` 并发写入** —— 勘察期间 `.tmp` 件数 1149 → 1158（`collision_survey_*` 系列，实测 10:07:57–58 落盘）；")
A("   该批全为 10-17 件，由约束 ③ 全数拦下，未入本棒清单。")
A("2. **他棒删 `results/` 2 件** —— 回收站另有 `$ICQO5B3.json`／`$IICM2TA.json`（`$I` 时刻 **10:19:26／10:19:32**，")
A("   晚于本棒批次结束 10:17:59），指向 `results/_dep_dangling_final.json`／`results/_dep_dangling_scan_raw.json`。")
A("   **该 2 件不在本棒清单内，非本棒所删**，特此区分以免归因错位。")
A("")
A("---\n")
A("## §8 风险与遗留\n")
A("1. **回收站为唯一恢复面** —— 回收站于 10-15 后曾被清空过（10-15 登记件载 `$I` 6→283，本棒开工前盘面仅 `desktop.ini`）；")
A("   本棒 434 件之可恢复性**完全依赖回收站不被清空**。清空即不可逆。")
A("2. **KD %d 件未清** —— 候 PI 裁是否按「仅件名、不含 stem」重判 B 通道（见 §4）。" % (511 - cat1))
A("3. **C4 判定留痕** —— `results/__pycache__` 2 件与 `.tmp/__pycache__/s4_regen_runner.cpython-314.pyc` 系按")
A("   派工单判据 ④「两个 `__pycache__` 可清」纳入，而非四通道零命中；其中后者之源 `.tmp/s4_regen_runner.py` 为")
A("   **受保护唯一实现载体**，删其字节码不删其源码，风险极低但**属判据 ④ 之运用，非四通道结论**，故明示。")
A("4. **⛔ 未宣告①毕** —— 本棒仅执行清理面，⛔0 就①段收束作任何宣告。\n")

body = "\n".join(L_)
with io.open(REG, "w", encoding="utf-8", newline="\n") as f:
    f.write(body)

raw = open(REG, "rb").read()
print(json.dumps({
    "register": REG,
    "bytes": len(raw),
    "sha12": hashlib.sha256(raw).hexdigest()[:12],
    "bom": raw[:3] == b"\xef\xbb\xbf",
    "crlf": raw.count(b"\r\n"),
    "lf": raw.count(b"\n"),
    "rows": len(rows),
    "bytes_recycled": bytes_total,
    "strict_clean": strict_clean,
    "cat1": cat1,
    "kd": 511 - cat1,
    "b_stem_only": len(b_stem_only),
}, ensure_ascii=False, indent=1))
