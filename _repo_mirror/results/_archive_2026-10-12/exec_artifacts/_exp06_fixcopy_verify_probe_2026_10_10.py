# -*- coding: utf-8 -*-
"""EXP-06 self_verified_only 修正版副本 · 静态验证探针（工具件 · 0 属证据面）"""
import ast
import difflib
import hashlib
import pathlib

BASE = pathlib.Path(r"_repo_mirror")
ORIG = BASE / "deposon_team" / "plugins" / "_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py"
COPY = BASE / "deposon_team" / "plugins" / "_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py"

o = ORIG.read_text(encoding="utf-8")
c = COPY.read_text(encoding="utf-8")

# --- 1. parse / compile ---
ast.parse(c)
compile(c, str(COPY), "exec")
print("AST_PARSE_OK COMPILE_OK")
print("orig_lines", len(o.splitlines()), "copy_lines", len(c.splitlines()))

# --- 2. hard-write residue ---
hard = 'c["chain"]["self_verified_only"] = True'
print("orig_hardwrite_count", o.count(hard))
print("copy_hardwrite_count", c.count(hard))
print("copy_svo_true_literal_any", c.count('"self_verified_only"] = True'))

# --- 3. AST assignment sites for self_verified_only ---
tree = ast.parse(c)
sites = []
for n in ast.walk(tree):
    if isinstance(n, ast.Assign):
        for tgt in n.targets:
            if isinstance(tgt, ast.Subscript):
                sl = tgt.slice
                if isinstance(sl, ast.Constant) and sl.value == "self_verified_only":
                    sites.append((n.lineno, ast.unparse(n.value)))
print("copy_svo_assign_sites", sites)
otree = ast.parse(o)
osites = [
    (n.lineno, ast.unparse(n.value))
    for n in ast.walk(otree)
    if isinstance(n, ast.Assign)
    for tgt in n.targets
    if isinstance(tgt, ast.Subscript)
    and isinstance(tgt.slice, ast.Constant)
    and tgt.slice.value == "self_verified_only"
]
print("orig_svo_assign_sites", osites)

# --- 4. diff registration ---
ol = o.splitlines()
cl = c.splitlines()
sm = difflib.SequenceMatcher(None, ol, cl, autojunk=False)
add = rep = 0
regions = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    regions.append((tag, i1 + 1, i2, j1 + 1, j2, i2 - i1, j2 - j1))
    if tag == "replace":
        rep += max(i2 - i1, j2 - j1)
    elif tag == "insert":
        add += j2 - j1
    elif tag == "delete":
        rep += i2 - i1
print("diff_opcode_regions", len(regions))
print("orig_lines_touched", sum(r[5] for r in regions), "copy_lines_touched", sum(r[6] for r in regions))
print("net_line_delta", len(cl) - len(ol))
for r in regions:
    print("  region tag=%s origL%d-%d(%d) -> copyL%d-%d(%d)" % (r[0], r[1], r[2], r[5], r[3], r[4], r[6]))

# --- 5. semantic (non-comment, non-identity) site scan ---
print("copy_probe_fn_present", "def probe_independent_evidence" in c)
print("copy_INDEP_DECL_present", "INDEP_VERIFY_DECL = None" in c)
print("copy_new_keys", sorted({k for k in [
    "self_verified_only_basis",
    "independent_verification_ref",
    "independent_verification_status",
    "independence_deficiency_alarm",
    "independence_verification",
    "runner_fix_notice",
] if '"%s"' % k in c}))

# --- 6. identity rewrites ---
for tok in ["2026-09-29", "_v0_4_2026_09_29.py", "V3X-C5B-RUNNER-2026-09-29-A1",
            "index_v3_2026_09_29.json"]:
    print("copy_occurrences[%s]" % tok, c.count(tok))
print("copy_output_paths", [l.strip() for l in c.splitlines() if l.strip().startswith(("P_OUT_", "REL_", "GENERATOR", "DATE ="))])

# --- 7. hashes ---
for p in (ORIG, COPY):
    b = p.read_bytes()
    print("FILE", p.name, "sha12=" + hashlib.sha256(b).hexdigest()[:12], "bytes=" + str(len(b)),
          "BOM=" + str(b[:3] == b"\xef\xbb\xbf"),
          "CRLF=" + str(b.count(b"\r\n")), "LF=" + str(b.count(b"\n")))
