"""Final all-files verification for the D3r2 + D5 pair."""
import hashlib, json, os, re

ROOT_R = "D:/私人资料/deposon-repo/results"

files = {
    "_v4_manifest_distill_min_v1.json": ("6D1563A4AE23", 6563),
    "_v4_manifest_distill_min_v1_addendum_d1b.json": ("C3934C17B315", 6290),
    "_v4_distill_min_measure.py": ("21771E66AF67", 33852),
    "_v4_distill_min_measure_result_v1.json": ("A7156D3EFE19", 32789),
    "_v4_distill_min_measure_result_v1r2.json": ("EFA97C1D1B52", 34355),
    "_v4_d5_verdict_data.json": ("B2A390C37D52", 7324),  # updated after LF fix
    "_v4_distill_min_verdict_v1.md": (None, None),  # self-ref
    "_v4_d3r2_revision.py": (None, None),  # helper
    "_v4_d3r2_verify.py": (None, None),  # helper
    "_v4_d3r2_independent_diff.py": (None, None),  # helper
    "_v4_d5_verdict_build.py": (None, None),  # helper
}

def sha12(path):
    with open(path, "rb") as f:
        b = f.read()
    return hashlib.sha256(b).hexdigest()[:12].upper(), len(b)

SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"\bBearer\s+[A-Za-z0-9_.-]{20,}"),
    re.compile(r"\bsk_[A-Za-z0-9]{20,}"),
    re.compile(r"\bapi[_-]?key\b", re.IGNORECASE),
    re.compile(r"\bpassword\s*=", re.IGNORECASE),
    re.compile(r"\btoken\s*=\s*['\"]"),
]

def scan_secrets_in_file(path):
    """Scan a file for secret-like patterns. Read as text."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        return []
    findings = []
    for pat in SECRET_PATTERNS:
        for m in pat.finditer(text):
            findings.append((pat.pattern, m.group(0), m.span()))
    return findings

print("=== ALL FILES VERIFICATION ===\n")

all_ok = True

for fname, (expected_sha, expected_size) in files.items():
    path = os.path.join(ROOT_R, fname)
    if not os.path.exists(path):
        print("MISSING: " + fname)
        all_ok = False
        continue
    actual_sha, actual_size = sha12(path)
    size_ok = (expected_size is None) or (actual_size == expected_size)
    sha_ok = (expected_sha is None) or (actual_sha == expected_sha)
    status_str = ("SIZE OK" if size_ok else "SIZE MISMATCH") + " / " + ("SHA OK" if sha_ok else "SHA MISMATCH")
    extra = ""
    if expected_sha is None:
        extra = "  (expected: helper)"
    elif expected_size is None:
        extra = "  (expected size: ~approx)"
    print("  " + fname + ": " + actual_sha + " (" + str(actual_size) + " B) " + status_str + extra)
    if not size_ok or not sha_ok:
        all_ok = False

print()
print("=== V1 UNTOUCHED CHECK ===")
v1_path = os.path.join(ROOT_R, "_v4_distill_min_measure_result_v1.json")
v1_sha, _ = sha12(v1_path)
if v1_sha == "A7156D3EFE19":
    print("  PASS: v1 SHA-12 = A7156D3EFE19 (untouched since D3 base)")
else:
    print("  FAIL: v1 SHA-12 = " + v1_sha + " (expected A7156D3EFE19)")
    all_ok = False

print()
print("=== SECRET PATTERN SCAN ===")
secret_findings_total = 0
for fname in files:
    path = os.path.join(ROOT_R, fname)
    if not os.path.exists(path):
        continue
    findings = scan_secrets_in_file(path)
    if findings:
        print("  " + fname + ":")
        for pat, m, span in findings:
            print("    " + pat + " -> " + m + " at " + str(span))
        secret_findings_total += len(findings)
        all_ok = False
print("  total findings: " + str(secret_findings_total) + (" (PASS)" if secret_findings_total == 0 else " (FAIL)"))

print()
print("=== UTF-8 / LF / NO BOM CHECK ===")
for fname in files:
    if fname.endswith(".json") or fname.endswith(".md") or fname.endswith(".py"):
        path = os.path.join(ROOT_R, fname)
        if not os.path.exists(path):
            continue
        with open(path, "rb") as f:
            raw = f.read()
        has_bom = raw.startswith(b"\xef\xbb\xbf")
        cr_count = raw.count(b"\r")
        try:
            raw.decode("utf-8")
            utf8_ok = True
        except UnicodeDecodeError:
            utf8_ok = False
        verdict = "PASS" if (not has_bom and cr_count == 0 and utf8_ok) else "FAIL"
        print("  " + fname + ": BOM=" + str(has_bom) + " CR=" + str(cr_count) + " UTF8=" + str(utf8_ok) + " " + verdict)
        if verdict != "PASS":
            all_ok = False

print()
print("=== JSON VALIDITY ===")
for fname in files:
    if not fname.endswith(".json"):
        continue
    path = os.path.join(ROOT_R, fname)
    if not os.path.exists(path):
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
        print("  " + fname + ": PASS")
    except Exception as e:
        print("  " + fname + ": FAIL (" + str(e)[:100] + ")")
        all_ok = False

print()
print("=" * 30)
print("OVERALL: " + ("PASS" if all_ok else "FAIL"))