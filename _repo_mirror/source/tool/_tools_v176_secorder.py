import re, os
p = r"〔幽灵引用·原件已缺席·未上传:_v175_adoption_effect_2026_10_21.md〕"
t = open(p, encoding="utf-8").read()
lines = t.split("\n")
out = []
out.append(f"=== v175 TOTAL LINES: {len(lines)}  CHARS: {len(t)} ===")
out.append("=== v175 HEADING SKELETON ===")
for i,l in enumerate(lines,1):
    if re.match(r"^#{1,6}\s", l):
        out.append(f"{i:5d}| {l}")
out.append("=== v175 FIRST 40 LINES ===")
for i,l in enumerate(lines[:40],1):
    out.append(f"{i:5d}| {l}")
open(r"_repo_mirror/verdict/pi/_tools_v176_secorder.txt","w",encoding="utf-8").write("\n".join(out))
print("written")
