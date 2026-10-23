# 查理 · FTFB R5 改稿单（2026-10-20 合流轮 · 0 改稿 · 只读规划件）

- **任务来源**：群管理员 2026-10-20 12:34:04 三派派单（前两轮 10:55／11:27 因我节点超时作废，非任务问题；本轮按派单拆步：本改稿单先行，tex 落稿下轮再派；D-6 书目对版终验已改派阿兰，题录终值候其回填）。
- **拍板基线（本单执行口径）**：PI 2026-10-20 10:46「全默认，D4均做，确保arxiv一杆进洞」＋管理员 10:55 拍板登记（D-1～D-7 全按默认 16 子项；D-4 特批 A＋B；D-1a 形态A 成立——鲍勃独立复核 6/6 吻合、WGL @a57d7fe 在仓指纹一致、回退规则不触发；「确保 arXiv 一杆进洞」列全链硬约束）。
- **纪律声明**：**0 改稿·只读规划件**——R4 tex 与一切仓内/shared 既有文件零改动（R4 tex 指纹本轮再实测 `4f8c42319603`／101,928 B／606 行，与基线零漂移；本件为今日唯一新增交付件）。本单全部「拟落文本」均为**规划层**：实际改稿在 tex 落稿轮（下轮派单）发生。
- **底账输入（只读实读）**：爱丽丝《谱系理论底账》§5.2（档二转正稿五段）§3.2（[R57] 形态A）／阿兰《FTFB槽B实例候选底账》§4.2（[R58]–[R66] 池表）／鲍勃《FTFB状态刷新与验证底账》§一（git 实测）§二（五句事实基）／查理《R5 决策单》D-1～D-7＋§3.6 联动义务／《R5 修订方案 v4》／戴夫《R5 一杆进洞提交预案》§2.3（Comments 要点句）。
- **残留草稿续用（管理员许可）**：前两轮私区已形成 36 替换对执行脚本与应用版 tex（登记见 §十四）；本单拟落文本以该稿为基础，另按本轮派单与决策单执行规则升级 5 处（P1/P5 双锚补 SHA-256 prefix、P2/P3/P4 哈希 \texttt 排版、Q3 补 WGL 仓指纹、K1 语域微调、题录候阿兰回填），已在各条目标注「本轮升级」。
- **本件指纹**：以群内交付通报实测值为准（文件不自载自身哈希）。

---

## 一、改稿项总览（36 替换对＝R5 预期变更全集）

- 基线：R4 tex `4f8c42319603`（606 行）→ R5 tex（落稿轮产出）。
- 每对含：**锚文**（R4 全文唯一命中的原文串）与**拟落文本**（落稿值）；36 对按派单七项归入 §二–§九。
- 红线（全 36 对共同约束）：T/D/R 计分块既有格与既有行、映射表 M1–M5、verdict 字面、五锚表、全部数字读数 **0 触**；摘要（L72–L77）**零动**（D-3a 默认）；`no celebration` 纪律维持；双盲匿名面零新增泄露（[R57] 沿 [R56] 匿名先例）。

| # | 标签 | R4 位置 | 节 | 类型 | 关联决策 | Comments 要素（戴夫 §2.3） |
|---|---|---|---|---|---|---|
| 1 | A1-日期行-\date | L62 | 题头 \date 行 | 值替换 | 版本沿革（戴夫 §2.1 Date 字段） | Date 字段（Comments 外） |
| 2 | A2-日期行-头注 | L67 | 首页信息行（arXiv subjects 行末） | 值替换 | 同 A1 | Date 字段（Comments 外） |
| 3 | B1-P-S1-插入§1.1 | L83 | §1.1 末段之后 | 新增段 | D-3 P-S1 | argumentative register deepened |
| 4 | C1-P-S2-导言替换 | L132 | §1.3 开篇句 | 句替换（导言设问化） | D-3 P-S2 | argumentative register deepened |
| 5 | D1-§1.3(ii)-池数 | L132 | §1.3(ii) 池句 | 值替换 56→66 | D-2 合流池数 | pool extended from 56 to 66 |
| 6 | D2-§1.3(ii)-十件增补声明 | L132 | §1.3(ii) 段内 | 段内追句（十件声明） | D-2/D-2b 声明式入口 | pool extended … by declared additions |
| 7 | E1-P-S3-§2 | L136 | §2 题后（§2.1 前） | 新增段 | D-3 P-S3 | argumentative register deepened |
| 8 | E2-P-S3-§3 | L168 | §3 题后（§3.1 前） | 新增段 | D-3 P-S3 | argumentative register deepened |
| 9 | E3-P-S3-§4 | L198 | §4 题后（§4.1 前） | 新增段 | D-3 P-S3 | argumentative register deepened |
| 10 | E4-P-S3-§5 | L224 | §5 题后（§5.1 前） | 新增段 | D-3 P-S3 | argumentative register deepened |
| 11 | F1-C3β-谱系句 | L172 | §3.1 段末 | 段内追句（谱系纵深） | D-2a 案β（C3-β） | pool extended（正文承载） |
| 12 | G1-C2-§3.4小节 | L184 | §3.4 段后、Channel claim 前 | 新增小节（C2 副案例） | D-2 P1（C2·L2 协同） | pool extended（正文承载） |
| 13 | H1-C1-§5.2插段 | L236 | §5.2 段后插段 | 新增段（C1 链案例） | D-2 P1（C1·E-1 槽） | pool extended（正文承载） |
| 14 | I1-主表-C2行 | L457 | §9.1 主表 Channel II 行后 | 主表增行（只增行不改格） | D-2 联动义务 2 | pool extended（正文承载） |
| 15 | I2-主表-C1行 | L459 | §9.1 主表 Channel IV 行后 | 主表增行（只增行不改格） | D-2 联动义务 2 | pool extended（正文承载） |
| 16 | J1-三型-indeterminates | L466 | §9.1 三型段 | 词替换 two→four | D-2 联动（诚实同步） | pool extended（正文承载） |
| 17 | J2-三型-dispositions | L466 | §9.1 三型段 | 词替换 four→six | D-2 联动（诚实同步） | pool extended（正文承载） |
| 18 | J3-三型-R枚举 | L466 | §9.1 三型段 | 段内追句 | D-2 联动（诚实同步） | pool extended（正文承载） |
| 19 | K1-Scale句 | L474 | §9.2 Scale 限制句 | 句如实改写 | D-2 联动义务 4 | pool extended（正文承载） |
| 20 | L1-边界条件池数 | L474 | §9.2 边界条件句 | 值替换 56→66 | D-2 池数同步（第五处·实测补充） | pool extended from 56 to 66 |
| 21 | M1-P-S4-收束段 | L478 | §9.3 段末、披露段前 | 新增段（收束论证） | D-3 P-S4 | argumentative register deepened |
| 22 | N1-D4A-披露升格 | L480 | AI 披露段头 | 结构升格（\section*） | D-4 A 特批 | AI-use disclosure formalized |
| 23 | N2-D4B-直白否定句 | L480 | 披露段末 | 段内追句 | D-4 B 特批 | direct no-unreviewed-content statement |
| 24 | N3-D1c-同线披露注 | L480 | 披露段末（N2 句后） | 段内追句 | D-1c 默认（并入段末） | AI-use disclosure 节内承载 |
| 25 | O1-§8.4五段 | L435 | §8.3 末段后、收尾段前 | 新增小节（五段） | D-1 档二＋D-1a/D-1b | loop-family section added (Sec. 8.4) |
| 26 | P1-句1-L315 | L315 | §6 末段状态句 | 状态句刷新 | D-5 枝二 | deposition status refreshed |
| 27 | P2-句2-L329 | L329 | §7 锚表 P 行括注 | 状态句刷新 | D-5 枝二 | deposition status refreshed |
| 28 | P3-句3-L357-最小档 | L357 | §7.1 可用性段状态句 | 状态句刷新（最小档） | D-5/D-5a 最小档 | deposition status refreshed |
| 29 | P4-句4-L381 | L381 | §7.2 审计层段状态句 | 状态句刷新 | D-5 枝二 | deposition status refreshed |
| 30 | P5-句5-L494 | L494 | Appendix·Availability 状态句 | 状态句刷新 | D-5 枝二 | deposition status refreshed |
| 31 | Q1-L486-首句 | L486 | 附录池验证声明首句 | 词替换 | D-2 池数同步 | pool extended … by declared additions |
| 32 | Q2-L486-then-closed | L486 | 附录池验证声明收束句 | 词替换（now→then） | D-2 池数同步 | pool extended … by declared additions |
| 33 | Q3-L486-R5批次登记 | L486 | 附录池验证声明段末 | 段内追句（R5 批次登记） | D-2/D-2b 验证档 | pool extended …（题录候阿兰回填） |
| 34 | R1-L500-池数 | L500 | References 头池句 | 值替换 56→66 | D-2 池数同步 | pool extended from 56 to 66 |
| 35 | R2-L500-companion声明 | L500 | References 头 companion 声明句 | 句改写（1→2＋增补句） | D-1a/D-2b | pool extended … by declared additions |
| 36 | S1-池末新组 | L603 | 池末 R55–R56 组后、\end{document} 前 | 新增两组（R57＋R58–R66） | D-1a 形态A＋D-2 | pool extended from 56 to 66 |

> 说明：位置为锚文首行所在 R4 行号；插段类（B1/E/M1/O1/G1/H1）为插入点前后锚行；S1 锚文跨 L603–L606。

---

## 二、档二 §8.4 转正（D-1 默认档二·爱丽丝 §5.2 转正稿）

新 §8.4「The loop family and its wider formulation」，插于 §8.3 末段与收尾段之间（收尾段文字不动、顺延）。文本＝爱丽丝 §5.2 转正稿（四功能五段：①Scope 声明段→②点名/分工段（功能①②）→③同源段（功能·点4 式二）→④物心声明级段（功能③）→⑤接口收束段（功能④））。相对爱丽丝原稿唯一联动改动：para 3 披露指引「as stated in the disclosure of §9.2」→「as stated in the paper's AI use disclosure」（D-4 A 升格后 §9.2 编号失效，改节名指引）。纪律要点：无名化（正文零 V5/deposon/种子表/qualia 字段）；「in preparation」时体＋不承继句（§2.2 六要件落位）；语域自检过（0 高考作文标记）；[R57] 引用沿声明式匿名兼容形态。

### 25｜O1-§8.4五段（R4 L435·§8.3 末段后、收尾段前）

- **改动类型**：新增小节（五段）｜**关联决策**：D-1 档二＋D-1a/D-1b｜**Comments 要素**：loop-family section added (Sec. 8.4)
- **锚文（old·R4 全文唯一命中）**：

```tex
whether any reader takes the recomputation up is outside the authors' control (§7.1, §7.2).

It is worth noticing the asymmetry
```

- **拟落文本（new·落稿终值）**：

```tex
whether any reader takes the recomputation up is outside the authors' control (§7.1, §7.2).

\subsection{The loop family and its wider formulation}

\textbf{Scope declaration.} This subsection registers lineage, not results. It names two related works — one public, one in preparation — declares what each supplies, and states what neither inherits from the checks of this paper. It makes no prediction, and it adds no claim beyond the scopes of §1.2 and §8.3.

The loop of this paper is one member of a family. A companion position statement in the same research line, the \textit{Worldview--Geometry Loop} [R57], carries the loop proposition at worldview level: that machine assistance now makes the hard-SF method — the deliberate variation of a setting's constraint axioms, consequences followed out — tractable at industrial scale, and that such world-systems, on the precedent of the non-Euclidean case, may in time act back on the representational space of the machines that produce them. The declaration is built to be killed: the companion states three kill lines of its own, all three currently open, and stakes its standing on them. The two works share the family skeleton — the non-Euclidean precedent, the two-way-loop form, the orientation to killable propositions — carried at different strengths: in the companion, as declaration; in this paper, as apparatus, run on a worked instance (§7). The division of labor is complementary by design: the companion supplies the proposition; this paper supplies the criteria any future instance of that proposition can be scored under. Neither work's claims rest on the other's. Their instances coincide — the companion's first complete instance is the project examined as this paper's §7 case — and the coincidence is stated rather than left tacit: there it is carried as the loop's instance; here it is scored on the same footing as the historical cases, engineering-grade, mid-strength. No claim of either work rests on the coincidence.

Both issue from the same dialogue-driven research practice — author-directed, AI-assisted, as stated in the paper's AI use disclosure — and the lineage is declared on that basis. A shared origin is not a shared verdict: neither work is evidence for the other.

That line is being extended, by declaration, toward a \textit{mind--matter formulation}: a work in preparation in the same research line, which would carry the loop's two-way form into the relation between mental and physical description. It is registered here at statement level only — a direction named, not a formulation claimed. It inherits no guarantee, no verdict, and no kill line from this paper; whatever standing it eventually claims will rest on pre-registrations of its own, or it will not claim standing.

The family closes along the line the term itself ascends: the existence line of §8.1 is documented; the \textit{Worldview--Geometry Loop} is declared [R57], not evidenced here; a mind--matter formulation is named as direction, nothing more. What this paper adds to the family is the adjudication agenda of §8.3 — the conditions under which a member of this line, any member, could be declared to have fed back, or declared dead — offered on the same terms to the family as to anyone else: no member of the line is exempt, and none is privileged.

It is worth noticing the asymmetry
```

## 三、池末新组落位（[R57] 形态A＋[R58]–[R66] 增补·题录候阿兰终验回填）

池末新设两组：Pool R57（R5 genealogy pass）＋Pool R58–R66（R5 instance-candidate pass），沿 R55–R56 组头与 itemize 既有格式。[R57]＝形态A（仓锚式：载体 docs/WORLDVIEW_GEOMETRY_LOOP_2026.md @citation-frozen commit；[AUTHOR-ANONYMIZED ENTRY] 标记沿 [R56]；P8 域——双盲投稿版须整体重抑制，非本轮）。[R58]–[R66] 题录＝阿兰 §4.2 表为基、我前轮预核修正后的**候选值**；**全部题录细值候阿兰 D-6 终验回填**（回填位清单见 §十；本轮派单明示「题录终值标候阿兰终验回填占位」，落稿轮以其《阿兰_D6书目对版终验记录_2026_10_20.md》建议终值回填，若推翻→显式登记差异再落稿）。

### 36｜S1-池末新组（R4 L603·池末 R55–R56 组后、\end{document} 前）

- **改动类型**：新增两组（R57＋R58–R66）｜**关联决策**：D-1a 形态A＋D-2｜**Comments 要素**：pool extended from 56 to 66
- **锚文（old·R4 全文唯一命中）**：

```tex
available to any reader from the author on request). [AUTHOR-ANONYMIZED ENTRY]
\end{itemize}

\end{document}
```

- **拟落文本（new·落稿终值）**：

```tex
available to any reader from the author on request). [AUTHOR-ANONYMIZED ENTRY]
\end{itemize}

\medskip

\noindent\textbf{Pool R57 (adjunct to §8; added at the R5 genealogy pass, 2026-10-20; by declaration, not retrieval — outside the three-line search of the Appendix)}\par\addvspace{2pt}

\begin{itemize}[leftmargin=1.6em,itemsep=2pt,parsep=0pt,topsep=3pt]
\item[R57.] Authors' companion position statement declaring the \textit{Worldview--Geometry Loop}, a two-way loop between AI and hard science-fiction worldbuilding, carrying three kill lines of its own, stated and open; carried in the public repository at the citation-frozen commit (\texttt{docs/WORLDVIEW\_GEOMETRY\_LOOP\_2026.md}), unsigned in its body text; title and identifiers withheld in this edition, to be restored in a later revised edition; added by declaration, not retrieval — outside the three-line search of the Appendix; attested by the authors rather than independently verified. [AUTHOR-ANONYMIZED ENTRY]
\end{itemize}

\medskip

\noindent\textbf{Pool R58–R66 (adjunct to §3, §5; added at the R5 instance-candidate pass, 2026-10-20; by declaration, not retrieval — outside the three-line search of the Appendix; entries may carry multiple texts of one chain, following the [R12] precedent)}\par\addvspace{2pt}

\begin{itemize}[leftmargin=1.6em,itemsep=2pt,parsep=0pt,topsep=3pt]
\item[R58.] E.T.A. Hoffmann, ``Der Sandmann'', in \textit{Nachtstücke}, vol. 1, Berlin: Realschulbuchhandlung, 1816 (the automaton Olympia story; the two-volume set is 1816–1817).
\item[R59.] S. Freud, ``Das Unheimliche'' (1919), in \textit{The Standard Edition of the Complete Psychological Works of Sigmund Freud}, vol. XVIII, London: Hogarth Press, 1955, pp. 217–256 (responds to E. Jentsch's 1906 essay on the uncanny, carried under this entry rather than separately pooled; the original 1919 serial venue is recorded differently across bibliographic traditions — Imago 5, pp. 297–324, per the Standard Edition's own German-editions note, and alternatively Internationale Zeitschrift für Psychoanalyse 5 — the difference is registered here, and this entry is anchored to the Standard Edition text).
\item[R60.] M. Mori, ``Bukimi no Tani'' (The Uncanny Valley), \textit{Energy} 7(4):33–35, 1970 (in Japanese); authorized English translation: K.F. MacDorman and N. Kageki, ``The Uncanny Valley [From the Field]'', \textit{IEEE Robotics and Automation Magazine} 19(2):98–100, 2012.
\item[R61.] J.C. Maxwell, \textit{Theory of Heat}, London: Longmans, Green, and Co., 1871 (the sorting-fiction device, first framed in the 1867 letter to P.G. Tait, presented here at its first published statement); W. Thomson, ``The Kinetic Theory of the Dissipation of Energy'', \textit{Nature} 9:441–444, 1874 (the naming act, ``Maxwell's demon'') — entry carries the device's founding and naming texts under one number, following the [R12] precedent.
\item[R62.] L. Szilard, ``Über die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen'', \textit{Zeitschrift für Physik} 53:840–856, 1929.
\item[R63.] J. Earman and J.D. Norton, ``Exorcist XIV: The Wrath of Maxwell's Demon. Part I. From Maxwell to Szilard'', \textit{Studies in History and Philosophy of Modern Physics} 29(4):435–471, 1998; Part II, ``From Szilard to Landauer and Beyond'', ibid. 30(1):1–40, 1999.
\item[R64.] R. Descartes, \textit{Meditationes de prima philosophia}, Paris: M. Soly, 1641.
\item[R65.] H. Putnam, \textit{Reason, Truth and History}, Cambridge: Cambridge University Press, 1981.
\item[R66.] N. Bostrom, ``Are You Living in a Computer Simulation?'', \textit{Philosophical Quarterly} 53(211):243–255, 2003.
\end{itemize}

\end{document}
```

## 四、合流池数 66 联动（四处＋实测第五处）

池数 56→66 同步：决策单登记四处（爱丽丝 §3.3）＝§1.3(ii) 池句 L132／附录池验证声明 L486／References 头 L500／池末区新组头（S1）；**实测补充第五处**＝§9.2 边界条件句 L474「the reference pool is closed at fifty-six items (§1.3(ii))」——方案期遗漏点，本单实测发现并纳入（若漏改将造成正文自相矛盾；**鲍勃差量验收时勿判清单外**）。入口纪律：新条目一律「by declaration, not retrieval——outside the three-line search」（D-2b 默认：声明式入口＋附独立核验记录；§1.3(iv) 检索相对声明不受影响，四处文面均如实带出）。

### 5｜D1-§1.3(ii)-池数（R4 L132·§1.3(ii) 池句）

- **改动类型**：值替换 56→66｜**关联决策**：D-2 合流池数｜**Comments 要素**：pool extended from 56 to 66
- **锚文（old·R4 全文唯一命中）**：

```tex
(ii) The reference pool is closed: fifty-six items, cited by pool number [R01]–[R56];
```

- **拟落文本（new·落稿终值）**：

```tex
(ii) The reference pool is closed: sixty-six items, cited by pool number [R01]–[R66];
```

### 6｜D2-§1.3(ii)-十件增补声明（R4 L132·§1.3(ii) 段内）

- **改动类型**：段内追句（十件声明）｜**关联决策**：D-2/D-2b 声明式入口｜**Comments 要素**：pool extended … by declared additions
- **锚文（old·R4 全文唯一命中）**：

```tex
and attested by its authors rather than independently verified. Batch-by-batch verification records for the pool are consolidated in the Appendix.
```

- **拟落文本（new·落稿终值）**：

```tex
and attested by its authors rather than independently verified. Ten entries were added after the search closed, all by declaration: [R57], a second companion work (declared in §8.4; carried in the public repository at the citation-frozen commit; attested by its authors rather than independently verified), and [R58]–[R66], the instance-candidate additions of 2026-10-20, each verified against primary records at addition — they enter outside the three-line search, and the search-relative statements of (iv) are unaffected. Batch-by-batch verification records for the pool are consolidated in the Appendix.
```

### 20｜L1-边界条件池数（R4 L474·§9.2 边界条件句）

- **改动类型**：值替换 56→66｜**关联决策**：D-2 池数同步（第五处·实测补充）｜**Comments 要素**：pool extended from 56 to 66
- **锚文（old·R4 全文唯一命中）**：

```tex
the reference pool is closed at fifty-six items (§1.3(ii));
```

- **拟落文本（new·落稿终值）**：

```tex
the reference pool is closed at sixty-six items (§1.3(ii));
```

### 31｜Q1-L486-首句（R4 L486·附录池验证声明首句）

- **改动类型**：词替换｜**关联决策**：D-2 池数同步｜**Comments 要素**：pool extended … by declared additions
- **锚文（old·R4 全文唯一命中）**：

```tex
Fifty-five of the fifty-six pool entries were verified against primary records.
```

- **拟落文本（new·落稿终值）**：

```tex
Fifty-five of the first fifty-six pool entries were verified against primary records.
```

### 32｜Q2-L486-then-closed（R4 L486·附录池验证声明收束句）

- **改动类型**：词替换（now→then）｜**关联决策**：D-2 池数同步｜**Comments 要素**：pool extended … by declared additions
- **锚文（old·R4 全文唯一命中）**：

```tex
so the pool now closes at 55 verified + 1 anonymized ([R56]) = 56.
```

- **拟落文本（new·落稿终值）**：

```tex
so the pool then closed at 55 verified + 1 anonymized ([R56]) = 56.
```

### 33｜Q3-L486-R5批次登记（R4 L486·附录池验证声明段末）

- **改动类型**：段内追句（R5 批次登记）｜**关联决策**：D-2/D-2b 验证档｜**Comments 要素**：pool extended …（题录候阿兰回填）
- **锚文（old·R4 全文唯一命中）**：

```tex
[R56] is attested by its authors rather than independently verified.

```

- **拟落文本（new·落稿终值）**：

```tex
[R56] is attested by its authors rather than independently verified. Ten entries were added at the R5 passes (2026-10-20), all by declaration, not by protocol search, outside the three-line search of this Appendix: [R57] (the companion position statement of §8.4; its carrier is carried in the public repository at the citation-frozen commit, SHA-256 prefix \texttt{1568b3fe5ae}; attested by its authors rather than independently verified) and [R58]–[R66] (the instance-candidate chain anchors of §§3–5; each verified against primary records at addition by web retrieval on 2026-10-20, with one bibliographic correction adopted at terminal check: the [R60] entry's translation venue, misattributed in the pre-revision draft, was set to the journal of record, IEEE Robotics and Automation Magazine). The pool now closes at 64 verified + 2 anonymized ([R56], [R57]) = 66.

```

### 34｜R1-L500-池数（R4 L500·References 头池句）

- **改动类型**：值替换 56→66｜**关联决策**：D-2 池数同步｜**Comments 要素**：pool extended from 56 to 66
- **锚文（old·R4 全文唯一命中）**：

```tex
The reference list is the closed pool of fifty-six items, cited in the text by pool number [R01]–[R56].
```

- **拟落文本（new·落稿终值）**：

```tex
The reference list is the closed pool of sixty-six items, cited in the text by pool number [R01]–[R66].
```

### 35｜R2-L500-companion声明（R4 L500·References 头 companion 声明句）

- **改动类型**：句改写（1→2＋增补句）｜**关联决策**：D-1a/D-2b｜**Comments 要素**：pool extended … by declared additions
- **锚文（old·R4 全文唯一命中）**：

```tex
One entry, [R56], is the authors' companion study, anonymized in this edition (title, authors, and identifiers withheld; to be restored in a later revised edition; available to any reader from the author on request; attested by the authors rather than independently verified).
```

- **拟落文本（new·落稿终值）**：

```tex
Two entries, [R56] and [R57], are the authors' companion works, anonymized in this edition (title, authors, and identifiers withheld; to be restored in a later revised edition; [R56] available to any reader from the author on request; [R57] carried in the public repository at the citation-frozen commit; both attested by the authors rather than independently verified). Entries [R58]–[R66] were added at the R5 instance-candidate pass (2026-10-20) by declaration, not by protocol search — they enter outside the three-line search protocol, and the search-relative statements of §1.3(iv) are unaffected; each was verified against primary records at addition.
```

## 五、五处状态句枝二刷新（D-5/D-5a 最小档·双锚惯例）

五处 deposition 状态句（L315/L329/L357/L381/L494）pending→deposited 收口刷新，文本以鲍勃 §二 底稿为基（语域微调权沿 D-5：P3 is→has been 单字微调，commit/指纹/日期字面零漂移）。执行规则（决策单 §6.1）：**双锚惯例** commit＋SHA-256 prefix 并记（本轮升级：P1/P5 补入 `9fccd007be9f`/`ed5eb708f332`，P2/P3/P4 哈希 \texttt 排版——沿 L381 `879db0217f04` 与 L494 `commit \texttt{a57d7fe}` 既有先例）；W2 指纹一律锚沉积时点版（9fccd007be9f@9b6d80a；10-06 匿名化版 d5179de00915 不入文——论文引用字段两版逐值一致）；P4/P5 路径口径＝沉积时点全路径＋「since relocated under the repository's mirror prefix with bytes unchanged」缀句；两沉积晚于引用冻结锚 a57d7fe，一律锚定沉积提交自身（不可表述为 at the citation-frozen commit）。P3＝D-5a 默认最小档（全披露档备选未采——10-06 匿名化披露句不落）。

### 26｜P1-句1-L315（R4 L315·§6 末段状态句）

- **改动类型**：状态句刷新｜**关联决策**：D-5 枝二｜**Comments 要素**：deposition status refreshed
- **锚文（old·R4 全文唯一命中）**：

```tex
The requirement is met in substance on that public record, with the machine-readable handoff carrier and the first audit record pending deposition (§7.2).
```

- **拟落文本（new·落稿终值）**：

```tex
The requirement is met in substance on that public record; the machine-readable handoff carrier and the first audit record were deposited in the public repository on 2026-09-29 and 2026-09-30 (commits \texttt{9b6d80a} and \texttt{3eee223}, SHA-256 prefixes \texttt{9fccd007be9f} and \texttt{ed5eb708f332}; Appendix).
```

### 27｜P2-句2-L329（R4 L329·§7 锚表 P 行括注）

- **改动类型**：状态句刷新｜**关联决策**：D-5 枝二｜**Comments 要素**：deposition status refreshed
- **锚文（old·R4 全文唯一命中）**：

```tex
the record's public carriers and pending machine-readable carrier are declared in §7.1)
```

- **拟落文本（new·落稿终值）**：

```tex
the record's public carriers, including the machine-readable carrier deposited at commit \texttt{9b6d80a}, are declared in §7.1)
```

### 28｜P3-句3-L357-最小档（R4 L357·§7.1 可用性段状态句）

- **改动类型**：状态句刷新（最小档）｜**关联决策**：D-5/D-5a 最小档｜**Comments 要素**：deposition status refreshed
- **锚文（old·R4 全文唯一命中）**：

```tex
The handoff record's machine-readable carrier is not part of the public repository; its fields are carried, values identical, by the archived source markdown, were re-verified item by item by the third-party recompute record (§7.2), and the carrier's deposition is pending (Appendix).
```

- **拟落文本（new·落稿终值）**：

```tex
The handoff record's machine-readable carrier has been part of the public repository since 2026-09-29 (commit \texttt{9b6d80a}, repository root); its fields are carried, values identical, by the archived source markdown and were re-verified item by item by the third-party recompute record (§7.2).
```

### 29｜P4-句4-L381（R4 L381·§7.2 审计层段状态句）

- **改动类型**：状态句刷新｜**关联决策**：D-5 枝二｜**Comments 要素**：deposition status refreshed
- **锚文（old·R4 全文唯一命中）**：

```tex
That rerun's own log is not part of the public repository; its occurrence and outcome are carried by the handoff record's audit field and cited as its prior by the second recompute's record below, and the log's deposition is pending (Appendix).
```

- **拟落文本（new·落稿终值）**：

```tex
That rerun's own log was deposited in the public repository on 2026-09-30 (commit \texttt{3eee223}, \texttt{\_september\_\allowbreak workspace/\allowbreak results/\allowbreak AUDIT\_\allowbreak 2026-08-30.json}, since relocated under the repository's mirror prefix with bytes unchanged); its occurrence and outcome are carried by the handoff record's audit field and cited as its prior by the second recompute's record below.
```

### 30｜P5-句5-L494（R4 L494·Appendix·Availability 状态句）

- **改动类型**：状态句刷新｜**关联决策**：D-5 枝二｜**Comments 要素**：deposition status refreshed
- **锚文（old·R4 全文唯一命中）**：

```tex
Two declared gaps: the handoff record's machine-readable carrier and the 2026-08-30 audit record are not part of the public repository; their fields and values are carried by the archived source markdown and the recompute record, and their deposition is pending.
```

- **拟落文本（new·落稿终值）**：

```tex
Both formerly declared gaps are closed: the handoff record's machine-readable carrier was deposited at commit \texttt{9b6d80a} (SHA-256 prefix \texttt{9fccd007be9f}; 2026-09-29, repository root) and the 2026-08-30 audit record at commit \texttt{3eee223} (SHA-256 prefix \texttt{ed5eb708f332}; 2026-09-30, \texttt{\_september\_\allowbreak workspace/\allowbreak results/\allowbreak AUDIT\_\allowbreak 2026-08-30.json}, since relocated under the repository's mirror prefix with bytes unchanged). Both depositions post-date the citation-frozen commit and are cited at their own deposition commits; the digests this paper relies on refer to the bytes as deposited.
```

## 六、D-4 A＋B 特批执行＋D-1c 同线披露注

D-4 特批 A＋B 双案（PI 10:46 显式授权，披露面变更）：A＝披露段升格独立节 `\section*{AI use disclosure}`（原文 \textbf 段头式作废）；B＝段末直白否定句「No content was generated by the AI without human review.」——即戴夫 Comments「direct no-unreviewed-content statement」。D-1c 默认＝同线披露注并入披露段末（爱丽丝 §5.2 联动件，逐字）。子项边界：metadata Comments AI 标注语**不加**（非默认，仅 PI 显式要求时）。升格后节序：§9.3 → AI use disclosure（无编号节）→ Appendix → References——不改变既有节编号（§9.1/§9.2/§9.3 编号零漂移）。

### 22｜N1-D4A-披露升格（R4 L480·AI 披露段头）

- **改动类型**：结构升格（\section*）｜**关联决策**：D-4 A 特批｜**Comments 要素**：AI-use disclosure formalized
- **锚文（old·R4 全文唯一命中）**：

```tex
\textbf{AI disclosure.} The drafting model is GLM
```

- **拟落文本（new·落稿终值）**：

```tex
\section*{AI use disclosure}

The drafting model is GLM
```

### 23｜N2-D4B-直白否定句（R4 L480·披露段末）

- **改动类型**：段内追句｜**关联决策**：D-4 B 特批｜**Comments 要素**：direct no-unreviewed-content statement
- **锚文（old·R4 全文唯一命中）**：

```tex
The authors directed all work, adjudicated all findings, and bear full responsibility for the result.
```

- **拟落文本（new·落稿终值）**：

```tex
The authors directed all work, adjudicated all findings, and bear full responsibility for the result. No content was generated by the AI without human review.
```

### 24｜N3-D1c-同线披露注（R4 L480·披露段末（N2 句后））

- **改动类型**：段内追句｜**关联决策**：D-1c 默认（并入段末）｜**Comments 要素**：AI-use disclosure 节内承载
- **锚文（old·R4 全文唯一命中）**：

```tex
Each number in §7 maps to a field path in the frozen artifact cited in place.
```

- **拟落文本（new·落稿终值）**：

```tex
Each number in §7 maps to a field path in the frozen artifact cited in place. Two same-line works are declared in §8.4 — the companion position statement [R57] and a mind--matter formulation in preparation; both issue from the same dialogue-driven research practice stated here, and neither is evidence for the other, nor inherits this paper's guarantees.
```

## 七、语域 P-S1–P-S4 插段（D-3·P-S5 QA 单见 §十三）

语域四插段（P-S1/P-S2/P-S3×4/P-S4），全部纯散文论证段、0 触数字/判定/计分块：P-S1＝§1.1 末「四渠道＝虚构输入四本体类型」段（C1/C2/C3 语域协同供料位）；P-S2＝§1.3 导言「设问—划界」辩证序改写（**声明性事实句逐字保真**：池数/检索日期/冻结锚/五锚表指涉全在后续 (i)–(iv) 正文，本替换只动导言句）；P-S3＝§2–§5 每渠道题后一段「为何此渠道是另一类输入」；P-S4＝§9.3 末收束论证段（三对话伙伴定位＋全方向可错条件句收束）。P-S5（QA 扫描单）规格见 §十三——落稿轮执行轮自检项。

### 3｜B1-P-S1-插入§1.1（R4 L83·§1.1 末段之后）

- **改动类型**：新增段｜**关联决策**：D-3 P-S1｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
verdicts that a third party can re-derive.

Our subject is a two-way loop
```

- **拟落文本（new·落稿终值）**：

```tex
verdicts that a third party can re-derive.

The four channels of this paper are also four answers to what kind of thing a fictional input is. A formal system is an input as language: it exists prior to reference, and its entry into science is a stipulated coordination. A thought experiment is an input as scenario: it exists as description, and its entry is a claimed yield. An abstract quantity is an input as form: it exists as definition, and its entry is a carried functional role. A story is an input as vocabulary and agenda: it exists in circulation, and its entry is a documented term of art or a question made askable. The kinds differ in what their supply means — a language lends its syntax, a scenario lends its consequence, a quantity lends its shape, a story lends its words — and the three checks grade all four kinds on one scale rather than ranking the kinds themselves. What none of the kinds is, anywhere in this paper: evidence. An input is used; it is not, by being used, promoted to a finding.

Our subject is a two-way loop
```

### 4｜C1-P-S2-导言替换（R4 L132·§1.3 开篇句）

- **改动类型**：句替换（导言设问化）｜**关联决策**：D-3 P-S2｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
Four scope declarations bound what follows. (i)
```

- **拟落文本（new·落稿终值）**：

```tex
Where must the boundaries run before any of the contributions can be checked? Four questions set them. What kind of work is this, that its historical sections can be case studies rather than chronicle (i)? What is the evidence base closed over, that closure is a property of the record rather than a boast about it (ii)? Which tiers of authority may the sections borrow, that no historical claim leans on a future not yet adjudicated (iii)? And against what searched record are the novelty statements made, that ``new'' means new against the search, not new to the authors (iv)? The declarations that follow draw those boundaries in that order; each is a boundary rather than a hedge — it fixes what the paper's claims are answerable to. (i)
```

### 7｜E1-P-S3-§2（R4 L136·§2 题后（§2.1 前））

- **改动类型**：新增段｜**关联决策**：D-3 P-S3｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
\section{Channel I: Formal Fiction into Physics}

\subsection{The historical chain}
```

- **拟落文本（new·落稿终值）**：

```tex
\section{Channel I: Formal Fiction into Physics}

This channel is where the input is a language. The question each channel puts to its fiction is what kind of thing enters science; here the answer is a system of relations with no referent yet. That purity is why the channel leads the paper: the fiction can be built, proved consistent, and shelved until physics stipulates a coordination, so every stage of the entry is dated and none of it depends on the fiction resembling anything. The risk the input runs is vacuity — form without referent can stay form forever — and the channel's discipline is to score what was joined, not what was gestured.

\subsection{The historical chain}
```

### 8｜E2-P-S3-§3（R4 L168·§3 题后（§3.1 前））

- **改动类型**：新增段｜**关联决策**：D-3 P-S3｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
\section{Channel II: Controlled Fiction}

\subsection{The thought-experiment dispute}
```

- **拟落文本（new·落稿终值）**：

```tex
\section{Channel II: Controlled Fiction}

This channel is where the input is a scenario. The fiction enters science as a described, never-run experiment, and the work it claims to do is done in the claiming: the scenario's yield is supposed to follow from the description alone. The risk here is disguise — imagery doing argumentative work it cannot repay — so the channel's criterion is translatability: a yield that survives being laid out as argument or model, checked by a party that accepts none of the dressing. The stock cases of §3.1 and the physics case of §3.4 below run the same criterion at two depths; the philosophical dispute is the live background, not the criterion.

\subsection{The thought-experiment dispute}
```

### 9｜E3-P-S3-§4（R4 L198·§4 题后（§4.1 前））

- **改动类型**：新增段｜**关联决策**：D-3 P-S3｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
\section{Channel III: An Abstract Quantity Becomes an Engineering Quantity}

\subsection{Entropy's two journeys}
```

- **拟落文本（new·落稿终值）**：

```tex
\section{Channel III: An Abstract Quantity Becomes an Engineering Quantity}

This channel is where the input is a quantity. A definition carried out of its home domain and put to work in another is the least narrative form fiction takes in this paper and the most bookkeeping: the entry is a functional form, the risk is that the carrying is decoration — or that the work was already done by a kindred physical quantity — and the checks are at their most mechanical, publication-dated arrows and a residue with a price. It is the channel where supply-level discipline matters most, because a quantity's elegance is exactly what a decoration would look like.

\subsection{Entropy's two journeys}
```

### 10｜E4-P-S3-§5（R4 L224·§5 题后（§5.1 前））

- **改动类型**：新增段｜**关联决策**：D-3 P-S3｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
\section{Channel IV: Narrative Fiction into the AI Agenda}

\subsection{A direct agenda-setting case}
```

- **拟落文本（new·落稿终值）**：

```tex
\section{Channel IV: Narrative Fiction into the AI Agenda}

This channel is where the input is a story in circulation. What enters science is vocabulary and agenda — terms of art and questions made askable — and because circulation leaves records, the evidence is graded by anchor type: self-statement, lexical record, named text, and, in the companion case below, a chain of dated primary texts. The risk the input runs is that supply masquerades as discovery — a word arrives and is mistaken for a result — so the channel asks its anchors to date the supply and its residue to be a term of art in use, nothing more. It is the channel closest to the culture's surface, and the one where the checks cost this paper the most honesty.

\subsection{A direct agenda-setting case}
```

### 21｜M1-P-S4-收束段（R4 L478·§9.3 段末、披露段前）

- **改动类型**：新增段（收束论证）｜**关联决策**：D-3 P-S4｜**Comments 要素**：argumentative register deepened
- **锚文（old·R4 全文唯一命中）**：

```tex
so no direct kill line attaches to the supply tier itself.

\textbf{AI disclosure.}
```

- **拟落文本（new·落稿终值）**：

```tex
so no direct kill line attaches to the supply tier itself.

Where the paper finally stands. Not inside fictionalism, which asks whether fictions can represent without describing anything real [R07] — this paper asks what checked work fiction has already done in the exact sciences. Not inside the model-based reasoning program, which traces how scientific concepts are constructed [R06] — this paper fixes what would count as such a construction having fed back, and how the count could fail. Not inside the history of science, which explains how past science came to be [R01] — this paper hands the historian's cases to a criteria apparatus the historian is free to reject. The position is the intersection of the three: fiction treated as an input class with graded, dated, checkable supply — scored, not celebrated. And the closing is conditional in every direction: each channel reading stands on its dated anchors and falls if they fail; the apparatus stands only while it can kill; the reverse-channel agenda stands until a case meets it or defeats it. Nothing in this paper is offered as a conclusion its authors would not accept losing.

\textbf{AI disclosure.}
```

## 八、§9.1 新增行与 §9.1/§9.2 联动＋实例链正文（D-2 P1 组合）

D-2 默认 P1＝C1＋C2＋C3-β 落位与联动义务：C3-β＝§3.1 段末谱系纵深句（不占案例位、不增主表行）；C2＝§3.4 新小节「A physics companion case: the sorting demon」（L2 协同旗舰：1867 信→1871 专著→1874 命名→1929 定量化→1961 原理化，多文一 entry 沿 [R12]/[R61] 先例）；C1＝§5.2 插段（E-1 槽：1816→1919→1970→2012 链式一次文献，**诚实申报无自述锚**——「one grade below Contact's self-statement hinge」）。§9.1 主表**只增两行不改格**（义务 2；「Pass (strong)」沿既有行先例）；三型段 two→four indeterminates／four→six dispositions（诚实同步）；K1＝Scale 限制句如实改写（义务 4；small-number 自限维持；本轮升级：语域微调 numbers→the small-number discipline，避免与「数字读数」红线词面混淆）。红线：既有行格零触碰；D 列「Indeterminate」语义如实（no study of alternatives/substitutes in the pool）。

### 11｜F1-C3β-谱系句（R4 L172·§3.1 段末）

- **改动类型**：段内追句（谱系纵深）｜**关联决策**：D-2a 案β（C3-β）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
with none of the fog that surrounds weaker senses of ``fiction.''

```

- **拟落文本（new·落稿终值）**：

```tex
with none of the fog that surrounds weaker senses of ``fiction.'' The stock cases also have an upstream lineage of their own — the deceiving demon of the \textit{Meditationes} [R64], the brain in a vat [R65], the simulation argument [R66] — older fictions that supplied the scenarios the modern debate refines rather than replaces; the lineage is registered here as depth of field, not as scored cases, and it earns the channel nothing.

```

### 12｜G1-C2-§3.4小节（R4 L184·§3.4 段后、Channel claim 前）

- **改动类型**：新增小节（C2 副案例）｜**关联决策**：D-2 P1（C2·L2 协同）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
Norton's reconstructions are precisely translations, and Brown's stock cases are scenarios whose yields survive translation.

\textbf{Channel claim.} Controlled fiction
```

- **拟落文本（new·落稿终值）**：

```tex
Norton's reconstructions are precisely translations, and Brown's stock cases are scenarios whose yields survive translation.

\subsection{A physics companion case: the sorting demon}

The philosophical stock cases above argue over what a thought experiment is; this case is here to show the channel's yield being cashed inside physics. Maxwell's sorting fiction — a finite being that separates fast molecules from slow, first framed in his 1867 correspondence with Tait and published in \textit{Theory of Heat} (1871) [R61], named a ``demon'' in Thomson's essay of 1874 [R61] — is a controlled fiction in exactly this channel's sense: a described, never-run experiment whose yield was claimed to follow from the description. The yield was cashed as physics, in stages. Szilard's one-molecule engine (1929) [R62] is the reconstruction that cashed it: the demon's sorting was shown to purchase its entropy decrease at an informational price. The price was made principle-grade by Landauer (1961) [R10] — the erasure of a bit costs kT·ln2, the information–entropy bound this paper's Channel III already carries as residue — and the bound's experimental line and the whole demon literature are carried critically by the review and exorcist studies in the pool [R43], [R63]. The chain matters to this channel for its shape: the fiction is the generator, the physics is the constraint, and what survives is an operative relation — a bound with a price — rather than a story. Its checks, run where the chain stands: T holds — 1871, 1874, 1929, 1961, every arrow publication-dated, the head of the chain a fictional construction; D is indeterminate — whether thermodynamics would have reached the bound without the demon fiction is decided by nothing in the pool, and we do not assert it; R holds — the residue is principle-grade, the strongest form this paper scores ([R10]). The row is scored with the channel's in §9.1.

\textbf{Channel claim.} Controlled fiction
```

### 13｜H1-C1-§5.2插段（R4 L236·§5.2 段后插段）

- **改动类型**：新增段（C1 链案例）｜**关联决策**：D-2 P1（C1·E-1 槽）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
what the channel needs is that the agenda-bearing sense has an anchor, and it does.

A lexical or named textual anchor does double duty
```

- **拟落文本（new·落稿终值）**：

```tex
what the channel needs is that the agenda-bearing sense has an anchor, and it does.

A third anchor form enters with the oldest chain this channel carries: fiction to concept, link by link, each link a dated primary text. Hoffmann's \textit{Der Sandmann} (1816) [R58] builds its unease on the automaton Olympia — a machine-woman whose near-human imperfection is the story's engine. Freud's essay on the uncanny (1919) [R59] takes that same figure, the lifelike doll, as a core instance of the uncanny — the familiar returned as strange — a documented engagement: the analysis runs on the fiction's own case. Fifty-one years later, the roboticist Mori named the design-side of the same structure \textit{bukimi no tani} (1970) [R60] — human affinity collapsing as resemblance rises — and the concept's English circulation is anchored by the authorized translation (2012) [R60], whose English name — \textit{uncanny} valley — carries the psychological lineage into the term itself. The chain's evidence form differs from the channel's other cases, and the difference is declared: the 1919 link is a documented engagement, but the 1970 link is an independent arrival at the same structure; no participant recalls supplying anything to anyone — the continuity is the printed record and the phenomenon's identity, not a documented request — and the case is honestly one grade below Contact's self-statement hinge. What the fiction supplied is exact and datable: the phenomenon's structure, near-human mismatch as an object of thought, first articulated in a narrative fiction, named independently in psychology and in engineering, now an operative term of art. The chain's checks, run where it stands: T holds — 1816, 1919, 1970, 2012, each dated to a primary text, the head of the chain a narrative fiction; D is indeterminate — whether the terms would have arisen without the fiction's articulation is decided by nothing in the pool, and we do not assert it; R holds — \textit{uncanny valley} is an operative term of art in human--robot interaction and the design of humanlike characters, five decades in circulation. The row is scored with the channel's in §9.1.

A lexical or named textual anchor does double duty
```

### 14｜I1-主表-C2行（R4 L457·§9.1 主表 Channel II 行后）

- **改动类型**：主表增行（只增行不改格）｜**关联决策**：D-2 联动义务 2｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
Channel II — controlled (§3) & Pass & Unresolved by design ([R04], [R05]) & Pass \\

```

- **拟落文本（new·落稿终值）**：

```tex
Channel II — controlled (§3) & Pass & Unresolved by design ([R04], [R05]) & Pass \\
Demon chain — controlled, physics companion (§3.4) & Pass — publication-dated chain: 1871 [R61], 1929 [R62], 1961 [R10]; naming act 1874 [R61] & Indeterminate — no study of alternatives in the pool & Pass (strong) — principle-grade residue ([R10]; experimental line surveyed in [R43]) \\

```

### 15｜I2-主表-C1行（R4 L459·§9.1 主表 Channel IV 行后）

- **改动类型**：主表增行（只增行不改格）｜**关联决策**：D-2 联动义务 2｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
Channel IV — narrative (§5) & Pass (tiered anchors [R11]–[R13]) & Indeterminate & Pass \\

```

- **拟落文本（new·落稿终值）**：

```tex
Channel IV — narrative (§5) & Pass (tiered anchors [R11]–[R13]) & Indeterminate & Pass \\
Uncanny-valley chain — narrative companion (§5.2) & Pass — publication-dated chain: 1816 [R58], 1919 [R59], 1970 [R60] & Indeterminate — no study of substitutes in the pool & Pass — operative term of art in human--robot interaction ([R60]) \\

```

### 16｜J1-三型-indeterminates（R4 L466·§9.1 三型段）

- **改动类型**：词替换 two→four｜**关联决策**：D-2 联动（诚实同步）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
two indeterminates, where the pool contains no study that could run the check (Channels III and IV); and one out-of-scope
```

- **拟落文本（new·落稿终值）**：

```tex
four indeterminates, where the pool contains no study that could run the check (Channels III and IV, and the two companion chains added at the R5 instance-candidate pass); and one out-of-scope
```

### 17｜J2-三型-dispositions（R4 L466·§9.1 三型段）

- **改动类型**：词替换 four→six｜**关联决策**：D-2 联动（诚实同步）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
— four dispositions, one dictionary, stated in §1.2.
```

- **拟落文本（new·落稿终值）**：

```tex
— six dispositions, one dictionary, stated in §1.2.
```

### 18｜J3-三型-R枚举（R4 L466·§9.1 三型段）

- **改动类型**：段内追句｜**关联决策**：D-2 联动（诚实同步）｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
a machine-checkable ledger. The last row is not a score:
```

- **拟落文本（new·落稿终值）**：

```tex
a machine-checkable ledger; the two R5 companion chains leave, in the same column, a priced bound and a term of art. The last row is not a score:
```

### 19｜K1-Scale句（R4 L474·§9.2 Scale 限制句）

- **改动类型**：句如实改写｜**关联决策**：D-2 联动义务 4｜**Comments 要素**：pool extended（正文承载）
- **锚文（old·R4 全文唯一命中）**：

```tex
Scale: each channel carries a small number of flagship cases, and the pipeline has one engineering-grade instance; no prevalence claim is made anywhere in this paper.
```

- **拟落文本（new·落稿终值）**：

```tex
Scale: each channel carries a small number of flagship cases, and the pipeline has one engineering-grade instance; the R5 instance-candidate pass (2026-10-20) adds one companion chain each to the controlled and narrative channels — a physics case beside the philosophical stock cases, and a chained-primary-text case beside the lexical and named-textual anchors — extending the anchor forms, not the small-number discipline, and the adjudication structure is unchanged; no prevalence claim is made anywhere in this paper.
```

## 九、版本日期行（戴夫打包轮对齐）

版本日期行两处同步换日（\date 与首页信息行 Date）：默认 2026-10-20；**若 tex 落稿/戴夫打包轮跨日，以打包当日实值对齐**（戴夫预案 §1.2 四点同步校验：Comments 页数／\date／表单 Date／首页信息行三值同日）。正文内「R5 pass (2026-10-20)」批次声明日为既成事实（本单签发日），不随编译日漂移。

### 1｜A1-日期行-\date（R4 L62·题头 \date 行）

- **改动类型**：值替换｜**关联决策**：版本沿革（戴夫 §2.1 Date 字段）｜**Comments 要素**：Date 字段（Comments 外）
- **锚文（old·R4 全文唯一命中）**：

```tex
\date{2026-09-27}
```

- **拟落文本（new·落稿终值）**：

```tex
\date{2026-10-20}
```

### 2｜A2-日期行-头注（R4 L67·首页信息行（arXiv subjects 行末））

- **改动类型**：值替换｜**关联决策**：同 A1｜**Comments 要素**：Date 字段（Comments 外）
- **锚文（old·R4 全文唯一命中）**：

```tex
\textbf{Date}: 2026-09-27
```

- **拟落文本（new·落稿终值）**：

```tex
\textbf{Date}: 2026-10-20
```


---

## 十、题录候阿兰终验回填位清单（D-6 接口·本轮派单指定占位机制）

机制：下表现值＝本单候选值（阿兰 §4.2 表为基＋我前轮预核修正）；**落稿轮以阿兰《阿兰_D6书目对版终验记录_2026_10_20.md》建议终值回填**——吻合则原样落稿，推翻则改题录字面并显式登记差异（沿 Putnam 年份教训：差异显式登记不隐藏）。Borges／Wiener／Schimpf 等非启用项按 D-6 默认不处置。

| 池号/句位 | 本单候选值（拟落文本现值） | D-6 终验要点（阿兰底账登记差异） | 回填动作 |
|---|---|---|---|
| [R58] | Hoffmann, *Nachtstücke*, vol. 1, Realschulbuchhandlung, 1816 | 出版项细值（社／年／卷） | 若差异→改题录字面 |
| [R59] | SE XVIII, 1955, pp. 217–256＋原刊两说句（Imago 5, pp. 297–324 vs Int. Ztschr. f. Psa. 5） | **SE XVIII 卷锚＋原刊两说裁定**（阿兰登记项） | 卷／页／两说句字面 |
| [R60] | *Energy* 7(4):33–35, 1970＋译 MacDorman & Kageki, *IEEE Robotics and Automation Magazine* 19(2):98–100, 2012 | **题录差异**：预修订稿（阿兰表原值）作 IEEE Spectrum 49(6)——终验裁定 journal of record | 译载体／卷期／页 |
| [R61] | Maxwell *Theory of Heat* 1871＋Thomson *Nature* 9:441–444, 1874 | Thomson 页码／题名细值 | 页码字面 |
| [R62] | *Zeitschrift für Physik* 53:840–856, 1929 | **页码对版**（阿兰登记未核项） | 页码字面 |
| [R63] | Part I 29(4):435–471, 1998；Part II 30(1):1–40, 1999 | Part II 卷期页对版（并注记式已定） | 卷期页字面 |
| [R64] | *Meditationes de prima philosophia*, Paris: M. Soly, 1641 | 版本项细值 | 出版项字面 |
| [R65] | *Reason, Truth and History*, CUP, 1981 | 年／社（前轮 Putnam 教训位） | 年／社字面 |
| [R66] | *Philosophical Quarterly* 53(211):243–255, 2003 | 卷期页 | 卷期页字面 |
| Q3 句 | terminal-check 修正句（[R60] venue→IEEE RAM） | 随 [R60] 终验结论存改：吻合则句留（terminal check＝阿兰 D-6）；推翻则句改或删 | 句存／改 |
| Jentsch 1906 | 不设独立条目（[R59] 括注承载） | 阿兰口径复核 | 维持默认 |

## 十一、Comments R5 要点句一致性对照（与戴夫预案 §2.3 对齐·变体选择留打包轮）

D-4 特批 A＋B 已拍板执行 → 适用戴夫**变体一／变体二**（均系 D-4 A＋B 执行时用）；变体三（D-4 不拍板分支）本轮不适用、登记留档。**变体选择（一全要素版 vs 二紧凑版）留打包轮**，本单不预选。

| 戴夫草稿句成分（变体一） | 本单对应改动项 | 一致性核 |
|---|---|---|
| a section on the loop family and its wider formulation added (Sec. 8.4) | O1（§二） | 小节题逐字同：The loop family and its wider formulation |
| the reference pool extended from 56 to 66 entries by declared additions | S1/D1/D2/L1/Q1–Q3/R1/R2＋F1/G1/H1/I/J/K 正文承载（§三/§四/§八） | 合流值 66＝D-2 P1；by declared additions＝D-2b 声明式入口（四处＋第五处文面如实带出） |
| the AI-use disclosure formalized as a dedicated section with a direct no-unreviewed-content statement | N1（A：\section* 升格）＋N2（B：direct no-unreviewed-content statement）＋N3（D-1c 同线注随节承载） | A/B 特批已落地 |
| repository deposition status refreshed to the current repository state | P1–P5（§五） | 五处 pending→deposited；as-of 基＝鲍勃 10-20 git 实测（W2 9b6d80a／W3 3eee223） |
| the argumentative register deepened throughout | B1/C1/E1–E4/M1（P-S1–S4）＋C3B 等实例链语域（§七/§八） | P-S1–S5 全序列落位（P-S5＝QA 单 §十三） |
| measurement anchors unchanged | 全 36 对红线（0 触计分块/五锚表/数字读数/摘要） | 鲍勃差量验收数字字面零漂移抽检（§十二） |

登记项（非分歧）：实例链正文（F1/G1/H1/I1/I2/J/K）系池增补的**正文承载面**，Comments 以「pool extended … by declared additions」统摄——与变体一/二表述相容；若 PI 欲在 Comments 显式点出 companion case chains，属打包轮措辞终稿化范围（戴夫 §2.3 已留「措辞可由查理终稿化」口，建议非裁）。Date 字段（A1/A2）＝Comments 外两字段变更之一（戴夫 §2.1），随打包轮对齐。

## 十二、鲍勃差量验收 diff 基线用法（本单即基线）

1. **基线对**：R4 tex（`4f8c42319603`／101,928 B／606 行）→ R5 tex（落稿轮产出件）；预期变更＝**本单 36 替换对全集**，再叠加阿兰 D-6 回填位字面（§十清单内值变化属在册变更，勿判清单外）。
2. **逐对验收**：每对 old 锚文在 R4 全文唯一命中（本单生成时已断言 count==1）；R5 tex 应满足——每个 old 零残留（除显式保留面）＋对应 new 全文在场。保留面示例：Q1/Q2 原批 56 条口径句（"the first fifty-six pool entries"／"then closed at 55 verified + 1 anonymized"）为新批登记的历史基线，非漂移。
3. **清单外零改动**：diff 其余 hunk（含空行／缩进级）均应逐块归因到本单某一对或 §十回填位；无法归因即 flag。
4. **数字字面零漂移抽检**：池数 66 仅出现在本单列明五处（L132／L474／L486 两句合为一处登记／L500／池末新组头）；commit／blob／日期字面（9b6d80a／3eee223／9fccd007be9f／ed5eb708f332／1568b3fe5ae／2026-09-29／2026-09-30）与鲍勃底账 §一 git 实测一致；五锚表／T/D/R 既有行格／verdict 字面／摘要（L72–L77）零触。
5. **[R57] 形态A**：WGL 仓锚复核结论（6/6 吻合）已生效；本单 Q3 的 SHA-256 prefix `1568b3fe5ae` 为鲍勃复核值，验收时对表其底账 §〇/§1.4。

## 十三、P-S5 语域 QA 扫描单（落稿轮自检规格·D-3）

落稿轮执行后自检，结果随件交付（一杆进洞自检面之一）：

1. **高考作文标记扫描**（全 tex grep 计数，预期全部 0）：`In conclusion`／`To sum up`／`First, `（段首脚手架）／`Second, `（段首）／`Finally, `（段首）／`It is well known`／`plays an important role`；装饰性形容词对扫描（new text 中 `great.*and.*important` 类并列装饰，人工复核）。
2. **锚纪律抽检**：池数五处值 66 一致；检索日期（2026-09-16 三线检索口径句）零触；冻结锚 a57d7fe 表述零触；五锚表指涉零触。
3. **声明性事实句逐字保真**：D1 等值替换前后 diff 仅 56↔66 一字；K1 限制句改写后 no prevalence claim 收束句在场。
4. **双盲面**：新增文本 0 作者身份／机构信息；[R57] 条目 [AUTHOR-ANONYMIZED ENTRY] 标记在位。
5. **摘要零动**（D-3a 默认）：L72–L77 diff 零行。

## 十四、预算、编译预检与残留草稿登记

1. **净增行数**：残留应用版实测 606→664 行（+58）；本单 5 处升级（双锚/\texttt/指纹句/语域微调）为句内改写、行数 ±0；阿兰回填后题录字面 ±数行内。决策单预算带（P1 全案净增 45–70 行）内。
2. **本地编译预检**（私区 pdflatex，与戴夫官方引擎不同——仅可编译性/页数信号，非承诺值）：R4 基线本地编译 25 页、R5 应用版本地编译 **29 页（+4）**——高于决策单「25→27±1」预估；页数终值以戴夫打包轮编译实测为准（沿 R4 教训：预估值不作承诺；Comments {N} 页数占位待实测）。
3. **残留草稿登记（私区 r5/，落稿轮直接续用）**：
   - `apply_r5.py`（36 对执行脚本·每对断言唯一命中——落稿轮按本单 5 处升级同步改脚本后重跑）；
   - `fiction_that_feeds_back.tex.r4bak`（基线备份，=shared R4 tex，复核 `4f8c42319603`）；
   - `fiction_that_feeds_back.tex`（残留应用版 `7843fff177b4`／664 行／122,034 B——**不含本单 5 处升级与阿兰回填**，落稿轮以脚本重跑方式再生成，不直接沿用此件）；
   - `r5.diff`（前轮差量 69,246 B，落稿轮重生成）；
   - `build_r4/`、`build_r5/`（本地编译预检件）；
   - `v1–v10、d6a、d6b` 共 13 份 D-6 预核 JSON（我前轮对版记录——阿兰终验如需比对底稿可申用，我可导出至 shared；终版以阿兰件为准）。
4. **落稿轮待办（下轮派单基）**：①按本单升级重跑执行脚本→新 R5 tex＋重出 diff＋指纹；②回填阿兰 D-6 终值（§十清单）；③P-S5 QA 自检（§十三）随件附结果；④交鲍勃差量验收（§十二口径）；⑤戴夫编译打包（Comments 变体选择＋Date/页数实测）。

## 十五、纪律收尾声明

1. **0 改稿复核**：本轮全程未触碰 R4 tex 与任何仓内/shared 既有文件（R4 tex 指纹交付前再实测——`4f8c42319603` 零漂移）；本件为今日唯一新增交付件；私区 r5/ 各件为工作草稿（前两轮残留＋本轮生成件），不构成对任何既有文件的改动。
2. **0 编造**：全部实测项标「本轮再实测／残留应用版实测」；预检页数标「本地编译信号·非承诺」；题录终值标「候阿兰终验回填」；Comments 变体选择标「留打包轮」。
3. **建议非裁**：本单全部拟落文本与联动设计为规划层建议，落稿执行以派单＋PI 口径为准；D-6 终值以阿兰件为准；页数/指纹终值以戴夫编译实测为准。
4. **双盲纪律**：本单含 tex 拟落文本若干（含匿名化条目设计），仅限协作面流转；[R57] P8 域（双盲投稿版整体重抑制）登记维持，非本轮。

—— 查理-论文主笔 ｜ 2026-10-20 ｜ 合流轮 · 0 改稿 · 只读规划件 · 建议非裁

