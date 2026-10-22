import os, re, datetime
ROOT = r"_repo_mirror"
L=[]
def P(s=""): L.append(str(s))
files = [
 ("释-甲注记件", r"results\_kreltrig_release_note_2026_10_21.md"),
 ("界线落账件", r"results\_kd_two_gates_boundary_adoption_2026_10_21.md"),
 ("DEN16 别名表修订件", r"results\_den16_alias_table_revision_2026_10_21.md"),
 ("歧义括注注记件", r"results\_d13_current_caliber_parenthesis_note_2026_10_21.md"),
 ("P2/P7 勘误段件", r"results\_fake_kd_p2_p7_reversal_errata_2026_10_21.md"),
]
for nm,rel in files:
    p=os.path.join(ROOT,rel)
    t=open(p,encoding="utf-8").read(); lines=t.split("\n")
    P(f"########## {nm}  ({rel})  lines={len(lines)}")
    P("--- H1 + 头部表 (L1-L14) ---")
    for i,l in enumerate(lines[:14],1): P(f"{i:4d}| {l}")
    P("--- 标题骨架 ---")
    for i,l in enumerate(lines,1):
        if re.match(r"^#{1,4}\s", l): P(f"{i:4d}| {l}")
    P()
open(os.path.join(ROOT,"_tools_v176_open1.txt"),"w",encoding="utf-8").write("\n".join(L))
print("ok", len(L))
