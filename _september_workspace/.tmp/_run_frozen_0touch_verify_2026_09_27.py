import hashlib
import os

WS = r"D:\私人资料\deposon-repo"


def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()


ANCHORS = [
    ("FROZEN-1", "verifier/handoff/KT_ABC1_anchors_sha256_12.json", "03C6C01F3697"),
    ("FROZEN-2", "results/_v3_v4_ghostref_reconciliation_2026_09_23.md", "1D52DB0EBF53"),
    ("FROZEN-3", "results/_v3_v4_achievements_inventory_2026_09_24.md", "29A853444D42"),
    ("FROZEN-4", "results/_archive_manifest_deposon_sub_2026_09_23.json", "B34B9F7BDFB7"),
    ("FROZEN-5", "results/_ghostref_copy_log_2026_09_23.json", "8CD133D0896F"),
    ("FROZEN-6", "results/_archive_manifest_non_upload_2026_09_23.json", "B899103853CA"),
    ("KEYCHAIN-1", "results/_v4_supp_t15r2_verdict.md", "8355724A26E3"),
    ("KEYCHAIN-2", "results/_v4_supp_t15r2_result.json", "C69AB0E3002E"),
    ("KEYCHAIN-3", "results/_v4_supp_t15r2_executor.py", "4B5B720D5CDA"),
    ("KEYCHAIN-4", "results/_v4_supp_l14v3_n26_verdict.md", "F4435801D09F"),
    ("KEYCHAIN-5", "results/_v4_supp_l14v3_batch10_r5_result.json", "7F02E08FC0DA"),
    ("KEYCHAIN-6", "results/_v4_supp_l14v3_batch9_r5_result.json", "1610F5060EF1"),
    ("KEYCHAIN-7", "results/_v4_supp_t1_verdict.md", "F1B5E49F3058"),
    ("KEYCHAIN-8", "results/_v4_supp_t15_verdict.md", "52C985429C91"),
    ("TEMPKEY-1", ".tmp/_l14v3_aggregated_10cells_v4.json", "66A9B8B3DABF"),
    ("TEMPKEY-2", ".tmp/_l14v3_n26_metrics_v2.json", "EB9CE9683AD3"),
    ("TEMPKEY-3", ".tmp/_l14v3_sensitivity_v2.json", "DCAA4B6B3B0B"),
    ("ANCHOR-A", "results/_v4_maindir_count_monitor_2026_09_27.md", "71E9CC179BEC"),
    ("ANCHOR-B", "results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md", "CC498BC28525"),
]

ok = 0
bad = 0
missing = 0
for tag, rel, exp in ANCHORS:
    p = os.path.join(WS, rel.replace("/", os.sep))
    if not os.path.exists(p):
        print("XX  %-10s MISSING  %s" % (tag, rel))
        missing += 1
        continue
    got = sha12(p)
    m = (got == exp)
    ok += m
    bad += (not m)
    print("%s  %-10s %s  %9d B  %s   expect=%s" %
          ("OK" if m else "XX", tag, got, os.path.getsize(p), rel, exp))

print("--- MATCH=%d  MISMATCH=%d  MISSING=%d  触动数=%d ---" % (ok, bad, missing, bad))
