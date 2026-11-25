# -*- coding: utf-8 -*-
import hashlib, io, os, sys, time

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


sys.stdout.reconfigure(encoding='utf-8')

P = r_dep_path("results/_copilot_agent_t2_t3_reply_register_2026_10_17.md")

BODY = """# ①段 · copilot agent 回执**转入登记件** —— `C5-b` 机械三要件（`K-C5B-1..3`）之**初核**（⛔ **0 代裁**闭否）

> **件性质**：**回执转入登记件 · 初核件**（**现态登记 ≠ 终判**）
> **出件**：`doc-writer`（`agent-0032834a3e04`）｜**日期**：2026-10-17｜**棒别**：起草类（登记成文）
> **仪器声明**：SHA-12 ＝ `hashlib.sha256(bytes).hexdigest()[:12]`（⛔ **0** 用语言内建 `hash()`）；bytes ＝ 字节流长度；**本件全部元数据为本棒直算，⛔ 0 沿用他件自报值**。
> **⛔ 状态边界**：⛔ **0 回改**任何既有件一字（本棒触动既有件数 ＝ **0**，源件**一律只读**）｜⛔ **0 宣告** `C5-b` 之**终判**（闭之终判归 `verdict-keeper`／PI）｜⛔ **0 代裁**闭否｜⛔ **0 断言**回函本体之内容（**本体不在盘**）｜⛔ **0 调**任何阈值／**0 改** `K-*`／`TH-*`／终判词表字面｜⛔ **0 宣告**①毕之任何面｜⛔ **0 联网**｜⛔ **0 涉实验**。

---

## §0 一句话结论

转入文本（PI 于主会话粘贴）已**逐字登记**（§1-2）；`C5-b` 机械三要件**本棒初核**：**要件① 未满足**（`REPLY_FROM_COPILOT_AGENT_*.md` 与 `RECEIPT_*.txt` 于 `letters/` 与 `〔本地路径已脱敏〕` **两面实测 0 在盘**，15:44:50 CST）｜**要件② 形式上或可满足 · 逐格表之在载不可核**｜**要件③ 已给惟不可核**（本体不在盘 ⇒ 指纹 0 可核）⇒ **`C5-b` 现态之闭之机械判定本棒 ⛔ 0 落档**，候 `verdict-keeper`／PI 裁（§2-2、§3）。

---

## §1 转入源、时点与通道

### §1-1 通道与时点（如实限定）

| 项 | 内容 |
|:-:|:--|
| **转入通道** | **PI 主会话粘贴**（派工单逐字载「**Filing into `letters/` is left to you**」）—— 即受托方自陈「归档入册由你方为之」 |
| **转入时点** | **2026-10-17 ≈15:41 CST（UTC+8）**（**依派工单转录**；⛔ **0 断言卡面原文逐字** —— 我方**卡面 0 在盘**，承拆桩件 `c9e304e43274` §6 KD-S-1 之射程） |
| **本棒实测时点** | **2026-10-17 15:44:50 CST**（epoch ms `1792223090594`） |
| **转入文本之载体** | **本件 §1-2** —— 所据者 ＝ 派工单所附之**逐字照录**；⛔ **0 断言**其与主会话原文**逐字节一致**（转录链，我方无第二份载体可校） |
| **本体状态** | 🔴 **回函本体 0 在盘** —— `REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` 与 `RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt` 于 `letters/`、`〔本地路径已脱敏〕`、`results/` **三面实测 0 命中**（§2-2 要件①） |

### §1-2 转入文本·**逐字照录**（0 改写）

> **已完成任务:** Reply is in `REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md`. I am the copilot-agent addressee. No repository file was modified.
>
> Both items are **underivable as stated**. No numerical proposed true value is offered for any of the 30 cells.
>
> - **T-2:** On this harness, `choose` receives the key-bearing context, so the information-constrained minimum is a structural zero to register, not an IC solution. Mechanism singletons are policy evaluations. `3/14·H` is rejected: it is one sampler's error rate at unfrozen constructor defaults, and only for 4-choice `{1,0,0,0}`.
> - **T-3:** All three mechanisms are memoryless. `M2` has `D ≡ 0` on the coded surface, so `U` is registered and not assigned. The Route 乙 formula is a sufficient condition on a state process that is not the harness; it is not an iff (`H=2`, `γ=1/2`, `τ=1/2` gives displayed `4/3` but tight robust total `3/2`).
>
> Fingerprint receipt, outside the reply file: SHA-12 `597caf8ba5bc`, 30,459 bytes, 318 lines. Also written to `RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt`. Filing into `letters/` is left to you.

---

## §2 `C5-b` 机械三要件之**初核**（⛔ **0 代裁**）

### §2-1 判死线·**逐字回读**（⛔ **0 凭派工单转述**）

**源件（本棒直算）**：`results\\_c5_split_into_c5a_c5b_2026_10_17.md`｜**SHA-12 `c9e304e43274`／28,902 B／260 LF／BOM 0／CRLF 0／U+FFFD 0**（**本棒实测**，与派工单所附指纹逐位相符）。

**权源逐字**（委托函 `letters\\_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md`｜**SHA-12 `385003e41ce2`／23,919 B／176 LF**（本棒实测）｜姊妹封 grok 版 `6922929bfda8`／23,906 B／176 LF）：

- **§7.6（L147 逐字节选）**：「A reply counts as **received for our registry** when a reply artefact is present **either** in the repository's `letters/` **or** under `〔本地路径已脱敏〕` (our stable delivery surface; the other location may be swept at any time), **and** it carries the **per-cell delivery table for both `T-2` and `T-3`**, **and** the **out-of-file fingerprint receipt** (SHA-12 / bytes / line count) required by §5.2. Our `C5` item (G-D03 adjudication, receipt-in-place) is judged mechanically on that artefact's presence. The artefact must state **which addressee it answers** — grok or copilot agent — so the registry can attribute the receipt per face; **an unattributable receipt cannot be counted against `C5`.**」
- **§5.2（L121 逐字）**：「With the delivery, report the fingerprint of each delivered file as **path + SHA-12 + byte count + line count** (SHA-256, first 12 hex, lowercase; `hashlib.sha256`, not a language built-in `hash()`). Fingerprints are reported **with** the delivery, **outside the delivered files**.」
- **§7.1（L142 逐字节选）**：「A structured written reply addressing `T-2` and `T-3` in that order, carrying a per-cell table across all 15 cells for each, and **ending each of the two items with a one-line verdict**: *derivable (with value/rule)* / *derivable-with-relaxation (name the relaxation)* / *underivable as stated (obstruction)*.」
- **§5.3（L125 逐字节选）**：「Mark every cell you cannot supply, item by item, **with its reason**. A cell left `null` with a stated reason is a complete delivery for that cell and does not disqualify the rest.」
- **§5.4（L129 逐字节选，主体同一性条款）**：「**Confirm that you are the addressee named on the header**: a prior reply on this project merely restated the header without confirming its own identity, and that was recorded as a compliance defect — **restating the header is not a confirmation**.」

**三条判死线·逐字**（`c9e304e43274` §4-4 **L169–171**）：

| **id** | **判据（逐字）** | 拆桩件之当时实测 |
| :-: | :-- | :-- |
| **`K-C5B-1`** | 「**载体在位** —— 回执件在 `letters/` **或** `〔本地路径已脱敏〕`（**稳定交付面**）在位；且**归属面**须自陈所答受托方（grok／copilot agent）——**unattributable receipt ⛔ 0 计入**」 | 🔴 不满足（两面 **0 命中** grok／copilot 回执件） |
| **`K-C5B-2`** | 「**逐格交付表在载** —— 回执件载 `T-2`／`T-3` **各 15 格**（3 机制 × 5 任务族）之**逐格交付表**（§7.1：每项须以**一行终判词**收束：*derivable (with value/rule)*／*derivable-with-relaxation*／*underivable as stated (obstruction)*）」 | 🔴 不满足（无回执件） |
| **`K-C5B-3`** | 「**函外指纹回执在载** —— 附 `path + SHA-12 + bytes + line count` 之指纹回执，且**在交付文件之外**（`hashlib.sha256`·⛔ **0** 用语言内建 `hash()`）」 | 🔴 不满足（无回执件） |

### §2-2 三要件·**初核**（本棒实测；⛔ **0 代裁**闭否）

> 📌 **本表所载为「初核」** —— 凡涉「是否满足」之**实质判定**，一律候 `verdict-keeper`／PI 落档；本棒**0** 将任一要件宣告为「满足」或「不满足」之终局。

| **id** | **初核结论** | **本棒实测依据**（2026-10-17 15:44:50 CST） |
| :-: | :-- | :-- |
| **`K-C5B-1`** | 🔴 **未满足**（载体面 0 在盘） | `os.path.exists` 精确名测试：`letters/`／`〔本地路径已脱敏〕`／`results/` **三面皆 False**（`REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md`、`RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt`）；关键词全树遍历：`letters/` 仅 **2 命中**（`REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`＝`44311ade19de`／44,520 B／266 LF；本方委托函 `_commission_…_copilot_agent_…md`＝`385003e41ce2`）｜GLM 面全树 **16 件 · 0 命中**（遍历有效性已核：含拆桩件 §3-1 所引之 `鲍勃_PI双裁定登记_G-E02验收线_G-E01就绪判定_2026_10_12.md`）｜`results/` **0 命中** |
| **`K-C5B-2`** | 🟡 **形式上或可满足 · 逐格表之在载不可核**（⛔ 0 代裁） | 转入文本载**逐项一行终判词**（「Both items are **underivable as stated**」——与 §7.1 之第三档 *underivable as stated (obstruction)* 同形）＋载 `T-2`／`T-3` **各自之阻断理由**（structural zero 之辨／`3/14·H` 之拒：单一采样器·**解冻**构造默认值·仅 4-choice `{1,0,0,0}`／Route 乙为**充分非 iff**：`H=2`、`γ=1/2`、`τ=1/2` 显 `4/3` 而 tight robust total `3/2`）＋载「30 cells」之计数（15＋15，与委托函 §0 之十五格口径相合）｜⚠ 转入文本**未见 30 格之逐格表本体**，惟**本体不在盘 ⇒ 本体是否载该表不可断言** ⇒ 本棒 ⛔ 0 判定「满足」 |
| **`K-C5B-3`** | 🟡 **已给惟不可核**（本体不在盘 ⇒ 指纹 0 可核） | 转入文本载「Fingerprint receipt, **outside the reply file**: SHA-12 `597caf8ba5bc`, 30,459 bytes, 318 lines」＋「Also written to `RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt`」｜⚠ **本体与 RECEIPT 件 0 在盘 ⇒ `597caf8ba5bc` 之正确性、SHA-256 算法、字节/行数一致性皆不可核**；另 §5.2 之 **`path` 要素** —— 转入文本所载者为**文件名**（见首行）而非完整路径，满足度 ⛔ 0 代裁（待本体入盘后逐字回读） |

### §2-3 归属面（attribution）·**初核**（⛔ **0 代裁**）

| 项 | 内容 |
|:-:|:--|
| **自陈之归属** | 转入文本首段逐字：「**I am the copilot-agent addressee.**」⇒ 就 §7.6 之字面要求（「state which addressee it answers — grok or copilot agent」）而言，**归属面已自陈** |
| **§5.4 之同一性确认** | 条款要求「**Confirm that you are the addressee named on the header**」，并明示「**restating the header is not a confirmation**」；转入文本之「I am the copilot-agent addressee」为**自称确认**而非逐字复述抬头 —— 其**满足度**（是否构成条款所指之 confirmation、是否需并含模型/端点/工具披露）**属实质判定，本棒 ⛔ 0 代裁** |
| **⚠ 不可断言面** | §5.4 之**模型名/版本、服务端点、工具调用**之披露，在转入文本中**未见**；惟**本体不在盘 ⇒ 不可断言其未披露**（§4 KD-C3） |

---

## §3 后续面（U ／ 候裁）

| # | **U** | **须** | **关联** |
| :-: | :-- | :-- | :-- |
| **U-1** | **回函本体＋RECEIPT 件之传入** —— 请 PI 将 `REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` 与 `RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt` 传入 `letters/` **或** `〔本地路径已脱敏〕`（稳定交付面）—— 此为**指纹可核**与**要件①可判**之前提 | **PI 传入** | §2-2 要件①③ |
| **U-2** | **grok 面回执未至** —— 姊妹封 `6922929bfda8`（23,906 B／176 LF）之回执**两面 0 在盘** ⇒ copilot 面之到件**不构成**两方齐备 | **PI 传入**（候） | §4 KD-C5 |
| **U-3** | **「一回执足否闭 `C5-b`」之射程问** —— 拆桩件 `K-C5B-1..3` 之判据**未载**「须两方受托方回执齐备」抑或「任一方回执即足」；本棒**⛔ 0 择**该射程 | **`verdict-keeper`／PI 裁** | §2-1（判死线逐字无载） |
| **U-4** | **要件②之逐格表核验** —— 本体入盘后须逐字回读其**逐项一行终判词**（§7.1）＋**逐格表 15×2**（§5.1-4 之 per-cell 适用性声明）＋ **§5.3** 之逐项理由 | **后续棒（依 U-1 而发）** | §2-2 要件② |
| **U-5** | **§5.2 之 `path` 要素与「函外」面之核** —— 入盘后核：所载路径是否为完整路径；指纹回执是否确在**交付文件之外**（`RECEIPT_*.txt` 为**另一文件**，其自身指纹**未**被报告） | **后续棒（依 U-1 而发）** | §2-2 要件③ |

---

## §4 KD（本棒共 **6** 条）

| # | **KD** | **严重度** | **本棒实测依据** | **本棒处置** |
| :-: | :-- | :-: | :-- | :-- |
| **KD-C1** | 🟠 **转入文本与函件本体之关系不可知（摘要 or 全文）** —— 本棒**0 在盘**本体，故**不可断言** §1-2 之转入文本即为回函本体之全文、亦不可断言其为 PI 之摘要 | **中高** | §1-1（三面 0 命中） | **如实登记**；⛔ **0 断言**本体内容；一切要件之实质判定悬置（§2-2） |
| **KD-C2** | 🟠 **指纹 `597caf8ba5bc`／30,459 B／318 行 不可核** —— 载体不在盘；且该组值系**受托方自报**，本棒 ⛔ 0 沿用他方自报值充作已核事实 | **中高** | §2-2 要件③ | **如实登记**；列 U-1、U-5 |
| **KD-C3** | 🟡 **要件②之「形式上或可满足」非判定** —— 转入文本载**逐项终判词＋逐项理由**（与 §5.3 之「有理由之 `null` ＝ 该格完整交付」同形），惟**30 格之逐格表不可见**；本体入盘前**不可判** | **中高** | §2-2 要件② | **如实登记**；⛔ 0 代裁；列 U-4 |
| **KD-C4** | 🟡 **§5.4 主体同一性之满足度 ⛔ 0 代裁** —— 自称「I am the copilot-agent addressee」**形式上**指向 confirmation；然条款另含模型/端点/工具披露之要求，而转入文本**未见**该披露（本体不在盘 ⇒ 不可断言其缺） | **中** | §2-3 | **如实登记**；⛔ 0 代裁；列 U-4 |
| **KD-C5** | 🟠 **「一回执足否闭」之射程未载于判死线** —— `K-C5B-1..3` 之逐字（§2-1）**0 提及**「须两方齐备」；两方同以 `C5-b` 为对象（`C5-b` 射程含 T-2／T-3 之母面余项），故一方回执之归属计法具实质影响 | **中高** | §2-1 逐字 | **如实登记**；⛔ 0 择射程；列 U-2、U-3 |
| **KD-C6** | 🟡 **低阶记法面** —— ①受托方文件名采 `T2_T3`（大写）而我方既有件采 `t2_t3`（小写）；②与既有先例 `REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` 之命名构式不同（缺受托方名之外的项序标识）｜**两皆非要件要素**（§7.6 只要求「artefact 在位＋载表＋载指纹＋自陈归属」） | **低** | §1-2 首行 ／ `letters/` 遍历 | **如实登记**；⛔ 0 以命名差异影响要件判定；入盘时按原名登记 |

---

## §5 落盘前检查

| 项 | 值 |
| :-- | :-- |
| 目标路径 | `〔本地路径已脱敏〕` |
| `Test-Path`（落盘前） | **False** |
| glob `results/` 内 `_copilot_agent_t2_t3_reply_register*`（落盘前） | **0 命中** |
| 处置 | **0 覆盖**，未需 `_r1` |

---

## §6 本棒 ⛔ 0 作之事项（逐条）

① ⛔ **0 回改**任何既有件一字（本棒触动既有件数 ＝ **0**；`c9e304e43274`、`385003e41ce2`、`6922929bfda8` **一律只读回读**）｜② ⛔ **0 宣告** `C5-b` 之**终判**（§2-2 仅为初核；终判归 `verdict-keeper`／PI）｜③ ⛔ **0 代裁**闭否／满足度｜④ ⛔ **0 断言**回函本体之内容｜⑤ ⛔ **0 沿用**受托方自报指纹充作已核｜⑥ ⛔ **0 改**判死线／阈值／终判词表任何字面｜⑦ ⛔ **0 宣告**①毕之任何面｜⑧ ⛔ **0 联网**（本棒网络动作 ＝ **0 次**）｜⑨ ⛔ **0 涉实验／0 执行**任何 runner｜⑩ ⛔ **0 读** `.env`／**0 录**任何凭据｜⑪ ⛔ **0 移动／0 重命名／0 删除**任何件｜⑫ ⛔ **0 用**他名头署名（本件署名 ＝ **`doc-writer`**）｜⑬ ⛔ **0 择**「一回执足否闭」之射程｜⑭ ⛔ **0 生成**派生 JSON／⛔ **0 合并**任何件。

---
"""

SELF = """
## §7 落盘后字节级自报（**写盘后回读直算 · 正文〔即本 §7 之前〕之实测**）

| 项 | 值 |
| :-- | :-- |
| 绝对路径 | `〔本地路径已脱敏〕` |
| SHA-12 | `{sha}` |
| bytes | `{byt}` |
| LF 行数 | `{lf}` |
| BOM | `False`（UTF-8 无 BOM） |
| CRLF | `{crlf}` |
| CR | `{cr}` |
| U+FFFD | `{fffd}` |
| 写入通道 | `io.open(P,"w",encoding="utf-8",newline="\\n",errors="strict")` ＋ 写后回读逐字比对 |
| 仪器 | SHA-12 ＝ `hashlib.sha256(bytes).hexdigest()[:12]`（⛔ **0** 用语言内建 `hash()`） |

📌 **注**：本 §7 系**写盘后追加**之自报栏，故上列值 ＝ **§7 之前之正文**实测；**全文件（含本栏）之最终 SHA-12／bytes 见派工回执**，以免自指循环。
"""

def measure(s):
    b = s.encode('utf-8')
    return {
        'sha': hashlib.sha256(b).hexdigest()[:12],
        'byt': len(b),
        'lf': b.count(b'\n'),
        'crlf': b.count(b'\r\n'),
        'cr': b.count(b'\r'),
        'fffd': s.count('\ufffd'),
    }

# pre-check (落盘前)
assert not os.path.exists(P), 'TARGET OCCUPIED'
assert [f for f in os.listdir(os.path.dirname(P))
        if 'copilot_agent_t2_t3_reply_register' in f] == [], 'GLOB HIT'

m = measure(BODY)
assert '\r' not in BODY, 'CR IN BODY'

with io.open(P, 'w', encoding='utf-8', newline='\n', errors='strict') as f:
    f.write(BODY)
    f.write(SELF.format(**m))
    f.flush()

# 写盘后回读逐字比对
b = io.open(P, 'rb').read()
full = b.decode('utf-8')
assert full == BODY + SELF.format(**m), 'ROUND-TRIP MISMATCH'

print('=== POST-WRITE MEASURE ===')
print('sha12      =', hashlib.sha256(b).hexdigest()[:12])
print('bytes      =', len(b))
print('lf lines   =', b.count(b'\n'))
print('bom        =', int(b.startswith(b'\xef\xbb\xbf')))
print('crlf       =', b.count(b'\r\n'))
print('cr         =', b.count(b'\r'))
print('fffd       =', full.count('\ufffd'))
print('--- body-only self-report values (section 7) ---')
print(m)
print('=== TIME ===')
print(time.strftime('%Y-%m-%d %H:%M:%S %Z'))
