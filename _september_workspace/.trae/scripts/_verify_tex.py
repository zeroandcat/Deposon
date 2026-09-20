# -*- coding: utf-8 -*-
"""FMT-verify (revised): verify the two single-language arXiv packages.

Checks paper/deposon_arxiv_en_pkg and paper/deposon_arxiv_cn_pkg plus their
tar.gz archives. Exits with code 1 if any check fails; prints a full report.
"""
import re
import sys
import tarfile
from pathlib import Path

PAPER = Path(r"D:\私人资料\deposon-repo\paper")
BS = chr(92)        # one literal backslash, for str ops (`in`, count, find)
RB = BS + BS        # two backslashes in a regex pattern = one literal backslash

PKGS = {
    "en": {
        "dir": PAPER / "deposon_arxiv_en_pkg",
        "tex": "deposon_paper_en.tex",
        "tar": PAPER / "deposon_arxiv_en.tar.gz",
        "arcroot": "deposon_arxiv_en",
        "fig_suffix": "_en.png",
        "cjk": False,
    },
    "cn": {
        "dir": PAPER / "deposon_arxiv_cn_pkg",
        "tex": "deposon_paper_cn.tex",
        "tar": PAPER / "deposon_arxiv_cn.tar.gz",
        "arcroot": "deposon_arxiv_cn",
        "fig_suffix": "_cn.png",
        "cjk": True,
    },
}

failures = []


def check(cond, msg):
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {msg}")
    if not cond:
        failures.append(msg)


# ---------------------------------------------------------------------------
# Stack-based \begin{...} / \end{...} environment pairing (2026-09-08 hardening).
# Scans EVERY line, tracking verbatim so literal text inside a verbatim block
# cannot be mistaken for an environment. On \end{env}: empty stack or a stack
# top that names a different env -> mismatch (line number + env recorded).
# At EOF a non-empty stack -> unclosed environments. Returns (errors, unclosed,
# stack_events) where stack_events is the final ordered list of (kind, env,
# lineno) for reporting.
# ---------------------------------------------------------------------------
BEGIN_END_RE = re.compile(RB + r"(begin|end)\s*\{([^}]*)\}")


def check_env_stack(tex_text: str):
    stack = []          # list of (env_name, begin_lineno)
    errors = []
    in_verbatim = False
    for lineno, line in enumerate(tex_text.splitlines(), start=1):
        # track verbatim: code fences in the MD would become verbatim; its body
        # is emitted verbatim and must not be scanned for environments.
        stripped = line.strip()
        vb = re.search(RB + r"begin\{verbatim\}", stripped)
        ve = re.search(RB + r"end\{verbatim\}", stripped)
        if in_verbatim:
            if ve:
                in_verbatim = False
            continue
        if vb and not ve:
            in_verbatim = True
            continue
        for m in BEGIN_END_RE.finditer(line):
            kind, env = m.group(1), m.group(2).strip()
            if kind == "begin":
                stack.append((env, lineno))
            else:  # end
                if not stack:
                    errors.append(f"line {lineno}: \\end{{{env}}} with empty stack "
                                  f"(no matching \\begin)")
                else:
                    top_env, top_line = stack[-1]
                    if top_env != env:
                        errors.append(
                            f"line {lineno}: \\end{{{env}}} does not match "
                            f"\\begin{{{top_env}}} opened at line {top_line}")
                    stack.pop()
    unclosed = [(env, ln) for env, ln in stack]
    for env, ln in unclosed:
        errors.append(f"line {ln}: \\begin{{{env}}} never closed "
                      f"(unclosed at end of file)")
    return errors, unclosed


for lang, spec in PKGS.items():
    print("=" * 72)
    print(f"PACKAGE: {lang}   {spec['dir']}")
    print("=" * 72)
    d = spec["dir"]
    tex_path = d / spec["tex"]

    check(d.is_dir(), f"package directory exists: {d.name}")
    check(tex_path.is_file(), f"tex file exists: {spec['tex']} ({tex_path.stat().st_size if tex_path.exists() else 0} bytes)")
    check((d / "references.bib").is_file(), "references.bib exists")
    check((d / "README.md").is_file(), "README.md exists")

    fig_dir = d / "figures"
    pngs = sorted(p.name for p in fig_dir.glob("*.png")) if fig_dir.is_dir() else []
    lang_pngs = [n for n in pngs if n.endswith(spec["fig_suffix"])]
    check(len(pngs) == 5 and len(lang_pngs) == 5,
          f"figures/ contains exactly 5 {spec['fig_suffix']} PNGs (found {len(pngs)}: {pngs})")

    if not tex_path.is_file():
        print("  (skipping content checks - tex missing)\n")
        continue
    tex = tex_path.read_text(encoding="utf-8")

    # F1: no leftover markdown image syntax
    check("![" not in tex, "no markdown image syntax '![' left in tex")
    incl = re.findall(RB + r"includegraphics\[[^\]]*\]\{([^}]+)\}", tex)
    check(len(incl) == 5, f"5 includegraphics directives (found {len(incl)})")
    check(all("/" not in n and "\\" not in n for n in incl),
          "includegraphics use basename only (no path prefix)")
    check(all(n.endswith(spec["fig_suffix"]) for n in incl),
          f"all includegraphics reference {spec['fig_suffix']} figures")
    check(not re.search(RB + r"caption\{[^}]*(Figure\s+\d+\s*:|图\s*\d+\s*[：:])", tex),
          "no 'Figure N:' / '图 N：' prefix inside captions")

    # F2: no key00 anywhere; citation whitelist
    check("key00" not in tex, "no key00 citation ([0,4] must not become \\cite)")
    body = tex.split(BS + "begin{thebibliography}")[0]
    cites = set()
    for m in re.finditer(RB + r"cite\{([^}]+)\}", body):
        for k in m.group(1).split(","):
            cites.add(k.strip())
    nums = sorted(int(k[3:]) for k in cites)
    check(nums == list(range(1, 35)),
          f"body citations are exactly key01..key34 (count={len(nums)}, range=({min(nums) if nums else '-'},{max(nums) if nums else '-'})" if nums else "body citations missing")

    # F3: emphasis matcher must not corrupt
    check((BS + "textit{)") not in tex, "no '\\textit{)' mismatch from (tau*) parsing")
    check(".*" in tex or "per_T." in tex, "JSON wildcard content present (sanity)")
    bad_wild = re.search(RB + r"textit\{\.", tex)
    check(not bad_wild, "no '\\textit{.' corruption of JSON wildcards")

    # F4/F6 tables
    check((BS + "begin{longtable}") in tex, "appendix long table uses longtable environment")

    # F5 section numbering
    sec_titles = re.findall(RB + r"(?:section|subsection|subsubsection)\{([^}]{0,40})", tex)
    bad_titles = [t for t in sec_titles if re.match(r"^\d+(\.\d+)*\s", t)]
    check(not bad_titles, f"no leftover numeric prefixes in section titles (bad: {bad_titles})")
    check((BS + "appendix") in tex, "\\appendix command emitted before appendix")

    # F7 abstract / footnote / hr
    check(tex.count(BS + "begin{abstract}") == 1 and tex.count(BS + "end{abstract}") == 1,
          "abstract environment opened and closed exactly once")
    ab = re.search(RB + r"begin\{abstract\}(.*?)" + RB + r"end\{abstract\}", tex, re.DOTALL)
    if ab:
        after = tex.split(BS + "end{abstract}")[1]
        check((BS + "section{") in after, "sections appear AFTER \\end{abstract} (not swallowed)")
    # arXiv 2026 rule: EN abstract plain text (LaTeX commands stripped, words
    # and spaces kept, matching the web-form paste caliber) must be <= 1920
    # characters. CN abstract is not length-checked (Chinese abstract is well
    # under the limit); the open/close-once check above already covers CN.
    if ab and not spec["cjk"]:
        raw = ab.group(1)
        plain = re.sub(r"\$[^$]*\$", " ", raw)          # drop inline math
        plain = re.sub(RB + r"[a-zA-Z]+\*?", " ", plain)  # drop \commands (\textbf etc.)
        plain = plain.replace("{", "").replace("}", "")
        plain = re.sub(r"\s+", " ", plain).strip()
        check(len(plain) <= 1920,
              f"EN abstract plain-text length {len(plain)} <= 1920 chars (arXiv hard limit)")
    check(tex.count(BS + "footnote{") == 1, "exactly one \\footnote in document")
    check(not re.search(r"^---\s*$", tex, re.MULTILINE), "no standalone '---' horizontal-rule lines")
    check("¹" not in tex, "superscript-1 declaration paragraph removed")
    check("王子贺" not in tex and "NSFC" not in tex, "no 王子贺 / NSFC strings")

    # footnote language
    fnm = re.search(RB + r"footnote\{(.*?)\}", tex, re.DOTALL)
    if fnm:
        fn = fnm.group(1)
        fn_cjk = any(0x4E00 <= ord(c) < 0xA000 for c in fn)
        if spec["cjk"]:
            check(fn_cjk, "cn footnote is in Chinese (contains CJK characters)")
        else:
            check(not fn_cjk, "en footnote is in English (no CJK characters)")
        # footnote must be before abstract / after maketitle, i.e. not dangling after \end{abstract}
        fn_pos = tex.find(BS + "footnote{")
        ab_end = tex.find(BS + "end{abstract}")
        check(fn_pos < ab_end, "footnote placed before \\end{abstract} (front matter, mark #1)")

    # ---- 2026-09-08 structural revision checks ------------------------------
    # (a) first line MUST be \pdfoutput=1
    first_line = tex.splitlines()[0] if tex.splitlines() else ""
    check(first_line.strip() == BS + "pdfoutput=1",
          f"line 1 is \\pdfoutput=1 (got: {first_line.strip()!r})")

    # (b) no external bibliography / file inclusion commands (inline thebib only)
    check(not re.search(RB + r"bibliography\s*\{", tex),
          "no \\bibliography{...} command (references are inline thebibliography)")
    check(not re.search(RB + r"input\s*\{", tex), "no \\input{...} command (self-contained)")
    check(not re.search(RB + r"include\s*\{", tex), "no \\include{...} command (self-contained)")

    # (c) quote environment: BOTH \begin{quote} and \end{quote} must be absent
    #     everywhere. The pre-abstract conventions call-out is dropped; its
    #     substance is re-injected as a static section. A stray \end{quote}
    #     with no \begin{quote} is a hard compile error, so the count of \end
    #     is checked explicitly (the old check only looked for \begin).
    n_quote_b = tex.count(BS + "begin{quote}")
    n_quote_e = tex.count(BS + "end{quote}")
    check(n_quote_b == 0,
          f"no \\begin{{quote}} anywhere in the tex (found {n_quote_b})")
    check(n_quote_e == 0,
          f"no \\end{{quote}} anywhere in the tex (found {n_quote_e}; orphaned end is a hard compile error)")

    # (c2) stack-based environment pairing over the WHOLE tex. Every
    #      \begin{env} must be closed by a matching \end{env} in LIFO order;
    #      empty-stack \end and EOF non-empty stack both FAIL with line numbers.
    stack_errors, unclosed = check_env_stack(tex)
    env_names = sorted({m.group(2).strip() for m in BEGIN_END_RE.finditer(tex)})
    check(not stack_errors,
          f"environment begin/end stack balanced (0 mismatches/unclosed)")
    if stack_errors:
        for e in stack_errors:
            print(f"        FAIL env-stack: {e}")
    print(f"  [INFO] {lang}: environments scanned = {env_names}; "
          f"unclosed at EOF = {len(unclosed)}; stack mismatches = {len(stack_errors)}")

    # (c3) between \maketitle (footnote included) and \begin{abstract} ONLY
    #      blank/whitespace lines are allowed (plus the single version
    #      \footnote, which is emitted right after \maketitle). No other
    #      command or text may appear there (an orphan \end{quote} used to
    #      hide in this gap).
    mk_pos = tex.find(BS + "maketitle")
    ab_start2 = tex.find(BS + "begin{abstract}")
    preface_bad = []
    if mk_pos >= 0 and ab_start2 >= 0:
        gap = tex[mk_pos + len(BS + "maketitle"):ab_start2]
        for gi, gl in enumerate(gap.splitlines(), start=1):
            s = gl.strip()
            if s == "":
                continue
            if s.startswith(BS + "footnote{") and s.endswith("}"):
                continue
            preface_bad.append((gi, s[:80]))
    check(not preface_bad,
          "only blank lines + the version \\footnote between \\maketitle and \\begin{abstract} "
          f"(extra content lines: {preface_bad})")

    # (d) the slim footnote contains ONLY the version string
    expected_fn = ("项目版本：deposon v0.1.1（2026-09-08）。" if spec["cjk"]
                   else "Project version: deposon v0.1.1 (2026-09-08).")
    fnm2 = re.search(RB + r"footnote\{(.*?)\}", tex, re.DOTALL)
    fn_body = fnm2.group(1).strip() if fnm2 else ""
    check(fn_body == expected_fn,
          f"footnote contains version string only (got: {fn_body[:60]!r}...)")
    for banned in ("KIMI", "Moonshot", "Acknowledgments", "致谢", "AI-use", "AI 使用"):
        check(banned not in fn_body, f"footnote does not contain {banned!r}")

    # (e) three static tail sections exist, in order, before \appendix
    if spec["cjk"]:
        tail_titles = ["数据与工件可用性", "致谢", "生成式 AI 工具使用声明"]
    else:
        tail_titles = ["Data and Artifact Availability", "Acknowledgments",
                       "Use of Generative AI Tools"]
    tail_poss = []
    for t in tail_titles:
        p = tex.find(BS + "section{" + t + "}")
        check(p >= 0, f"tail section present: {t}")
        tail_poss.append(p)
    app_pos = tex.find(BS + "appendix")
    if all(p >= 0 for p in tail_poss) and app_pos >= 0:
        check(tail_poss[0] < tail_poss[1] < tail_poss[2] < app_pos,
              "tail sections ordered (availability < acknowledgments < AI) and before \\appendix")
        concl_pat = "结论" if spec["cjk"] else "Conclusion"
        concl_pos = tex.find(BS + "section{" + concl_pat)
        check(concl_pos >= 0 and concl_pos < tail_poss[0],
              "tail sections come after the Conclusion section")

    # (f) every includegraphics basename resolves to a real PNG in figures/
    missing_figs = [n for n in incl if not (fig_dir / n).is_file()]
    check(not missing_figs, f"all 5 includegraphics PNGs exist in figures/ (missing: {missing_figs})")

    # (g) EN abstract plain-text char count, Keywords line EXCLUDED, actual
    #     value printed (arXiv hard limit 1920)
    if ab and not spec["cjk"]:
        raw = ab.group(1)
        raw_lines = [ln for ln in raw.splitlines()
                     if "Keywords" not in ln and "关键词" not in ln]
        plain = "\n".join(raw_lines)
        plain = re.sub(r"\$[^$]*\$", " ", plain)              # drop inline math
        plain = re.sub(RB + r"[a-zA-Z]+\*?", " ", plain)      # drop \commands (\texttt/\textbf...)
        plain = plain.replace("{", "").replace("}", "")
        plain = re.sub(r"\s+", " ", plain).strip()
        print(f"  [INFO] EN abstract plain-text chars (Keywords line excluded): {len(plain)}")
        check(len(plain) <= 1920,
              f"EN abstract plain-text length {len(plain)} <= 1920 chars (Keywords line excluded)")

    # F9 CJK environment
    cjk_b = tex.count(BS + "begin{CJK}")
    cjk_e = tex.count(BS + "end{CJK}")
    if spec["cjk"]:
        check(cjk_b == 1 and cjk_e == 1, f"cn document wraps content in CJK env (begin={cjk_b}, end={cjk_e})")
        # CJK must wrap maketitle + body: begin after \begin{document}, end before \end{document}
        doc_b = tex.find(BS + "begin{document}")
        cjk_bp = tex.find(BS + "begin{CJK}")
        cjk_ep = tex.find(BS + "end{CJK}")
        doc_e = tex.find(BS + "end{document}")
        check(doc_b < cjk_bp < cjk_ep < doc_e, "CJK env sits inside document env and wraps body")
    else:
        check(cjk_b == 0 and cjk_e == 0, f"en document has no CJK environment (begin={cjk_b}, end={cjk_e})")

    # bibliography
    bibitems = re.findall(RB + r"bibitem\{(key\d+)\}", tex)
    check(len(bibitems) == 62 and bibitems[0] == "key01" and bibitems[-1] == "key62",
          f"thebibliography has 62 bibitems key01..key62 (found {len(bibitems)})")
    # every body citation key must resolve to a bibitem (static closure proof)
    bib_set = set(bibitems)
    missing_bib = sorted(k for k in cites if k not in bib_set)
    check(not missing_bib,
          f"every body citation key has a matching bibitem (missing: {missing_bib})")
    cited = sorted(k for k in cites)
    print(f"  [INFO] {lang}: body cites {len(cites)} distinct keys "
          f"({cited[0]}..{cited[-1]}); all resolve to bibitems: "
          f"{not missing_bib}")
    # no cross-reference label/ref commands (paper uses none; verifies static
    # closure: there is nothing for a second LaTeX pass to resolve)
    n_label = len(re.findall(RB + r"label\s*\{", tex))
    n_ref = len(re.findall(RB + r"ref\s*\{", tex))
    n_eqref = len(re.findall(RB + r"eqref\s*\{", tex))
    # note: '\\ref{' cannot match '\\eqref{' (backslash is followed by 'e',
    # not 'r'), so n_ref and n_eqref are disjoint; likewise '\\href{',
    # '\\usepackage{hyperref}' do not match.
    check(n_label == 0, f"no \\label commands in tex (found {n_label})")
    check(n_ref == 0 and n_eqref == 0,
          f"no \\ref/\\eqref cross-references in tex (found ref={n_ref}, eqref={n_eqref})")
    check(not re.search(r"\.\. ", tex), "no double-period '.. ' in bibliography/text")
    bib_text = (d / "references.bib").read_text(encoding="utf-8")
    bib_keys = re.findall(r"@\w+\{(key\d+)", bib_text)
    check(len(bib_keys) == 62, f"references.bib has 62 entries (found {len(bib_keys)})")

    # tar.gz
    tar_path = spec["tar"]
    check(tar_path.is_file(), f"tar.gz exists: {tar_path.name} ({tar_path.stat().st_size if tar_path.exists() else 0} bytes)")
    if tar_path.is_file():
        with tarfile.open(tar_path, "r:gz") as tar:
            names = [t.name for t in tar.getmembers() if t.isfile()]
        root = spec["arcroot"]
        expected = {f"{root}/{spec['tex']}", f"{root}/references.bib", f"{root}/README.md"}
        expected |= {f"{root}/figures/{Path(n).name}" for n in lang_pngs}
        check(set(names) == expected,
              f"tar contains exactly {len(expected)} expected files (got {len(names)}: {sorted(names)})")
        junk = [n for n in names if Path(n).suffix.lower() in (".aux", ".log", ".pdf", ".out", ".toc", ".fls", ".fdb_latexmk")]
        check(not junk, f"no build artifacts (.aux/.log/.pdf) in tar (junk: {junk})")
    print()

print("=" * 72)
if failures:
    print(f"RESULT: {len(failures)} CHECK(S) FAILED")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASSED")
sys.exit(0)
