#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# lean_axiom_audit.py — DeposonThermo.lean 守恒机证审计（逐 theorem 公理台账）
# ----------------------------------------------------------------------------
# 两档：
#   编译档（本机有 lean）：实编 harness/DeposonThermo.lean（core-only·0 mathlib），
#       捕获全部 #print axioms 输出 → 逐 theorem 核：15/15 在册 · 0 sorryAx ·
#       0 Classical.choice · 公理集 ⊆ {propext, Quot.sound}（Lean 自带两大基础公理）·
#       decide 数据定理（settle_close/settle_conserved）0 公理。编译日志落 --log。
#   静态档（CI 无 lean）：只核源文件——每个 `theorem NAME` 都有 `#print axioms NAME`
#       行（覆盖完备）·源内 0 `sorry`·0 `admit`·0 `native_decide`。
# 用法：python3 harness/lean_axiom_audit.py [--lean ~/.elan/bin/lean] [--log build.log]
# 退出码：0 全过 · 1 失配（fail-loud）。
# ============================================================================
import argparse, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "DeposonThermo.lean")
ALLOWED_AXIOMS = {"propext", "Quot.sound"}
FORBIDDEN_TOKENS = ("sorry", "admit", "native_decide")


def theorem_names(source):
    return re.findall(r"^\s*theorem\s+([A-Za-z_][A-Za-z0-9_']*)", source, re.M)


def print_axiom_names(source):
    return re.findall(r"^#print axioms\s+([A-Za-z_][A-Za-z0-9_']*)", source, re.M)


def static_audit(source):
    thm, prn = theorem_names(source), print_axiom_names(source)
    ok = []
    ok.append(("every theorem has a #print axioms line (%d/%d)" % (len(set(prn) & set(thm)), len(thm)),
               set(thm) <= set(prn) and len(prn) == len(set(prn))))
    # `sorry`/`admit` only as proof tokens, never inside prose comments
    body = re.sub(r"/-.*?-/", "", source, flags=re.S)
    body = re.sub(r"--.*", "", body)
    for tok in FORBIDDEN_TOKENS:
        ok.append(("no '%s' in proof bodies" % tok, re.search(r"\b%s\b" % tok, body) is None))
    ok.append(("theorem count == 15 (ledger core: 6 conservation + 5 monotone + 2 settle + sum_set + sum_drop_zero)",
               len(thm) == 15))
    return ok, thm


def compile_audit(lean, log_path):
    source = open(SRC, "r", encoding="utf-8").read()
    thm = theorem_names(source)
    with tempfile.TemporaryDirectory() as td:
        dst = os.path.join(td, "DeposonThermo.lean")
        open(dst, "w", encoding="utf-8").write(source)
        p = subprocess.run([lean, "DeposonThermo.lean"], cwd=td, capture_output=True, text=True)
    out = p.stdout + p.stderr
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(out)
    ok = [("lean exit code 0", p.returncode == 0)]
    ok.append(("no 'error' in compiler output", "error:" not in out))
    ok.append(("no sorryAx in compiler output", "sorryAx" not in out))
    reported = {}
    for name, ax in re.findall(r"'[^']*\.([A-Za-z_][A-Za-z0-9_']*)' (?:depends on axioms: \[(.*?)\]|does not depend on any axioms)", out):
        reported[name] = [] if not ax else [a.strip() for a in ax.split(",")]
    ok.append(("#print axioms reported for every theorem (%d/%d)" % (len(set(thm) & set(reported)), len(thm)),
               set(thm) <= set(reported)))
    bad = {n: sorted(set(a) - ALLOWED_AXIOMS) for n, a in reported.items() if set(a) - ALLOWED_AXIOMS}
    ok.append(("axiom set ⊆ {propext, Quot.sound} (no sorryAx, no Classical.choice)", not bad))
    ok.append(("data theorems axiom-free (settle_close, settle_conserved)",
               reported.get("settle_close") == [] and reported.get("settle_conserved") == []))
    ok.append(("no theorem depends on sorryAx", all("sorryAx" not in a for a in reported.values())))
    return ok, reported, thm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean", default=shutil.which("lean") or os.path.expanduser("~/.elan/bin/lean"))
    ap.add_argument("--log", default=None, help="write the compiler output here (compile mode only)")
    a = ap.parse_args()
    source = open(SRC, "r", encoding="utf-8").read()
    results = []

    def show(label, ok, detail=""):
        results.append(bool(ok))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", label, (" — " + detail) if detail else ""))

    static_ok, thm = static_audit(source)
    for label, ok in static_ok:
        show("[static] " + label, ok)
    if os.path.exists(a.lean) and os.access(a.lean, os.X_OK):
        ok, reported, thm = compile_audit(a.lean, a.log or os.devnull)
        for label, good in ok:
            show("[compile] " + label, good)
        for n in thm:
            ax = reported.get(n)
            show("  %s" % n, n in reported, "axioms: %s" % (", ".join(ax) if ax else "none"))
        if a.log:
            print("compiler log written: %s" % a.log)
        mode = "compile+static"
    else:
        print("  [SKIP] lean toolchain not found at %s — static audit only (CI mode)" % a.lean)
        mode = "static only"
    good = all(results)
    print("lean_axiom_audit (%s): %s · %d/%d" % (mode, "ALL PASS" if good else "FAIL", sum(results), len(results)))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
