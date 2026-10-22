import io, re, os
REPO = r"_repo_mirror"
mp = os.path.join(REPO, "results", "_root_session_history_memo_main_2026_10_14.md")
t = io.open(mp, "r", encoding="utf-8", errors="replace").read()
hs = [(i+1, l) for i, l in enumerate(t.split("\n")) if re.match(r"^#{2,4}\s", l)]
out = ["MAIN_VERSION_HEADINGS (structure面 only · body未读)  total=%d" % len(hs), ""]
for i, h in hs[-14:]:
    out.append("%d| %s" % (i, h))
io.open(os.path.join(REPO, "results", ".tmp", "_audit_s13_main_heads_2026_10_20.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("OK", len(hs))
