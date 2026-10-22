import os, re
ROOT = r"_repo_mirror"
L=[]
def P(s=""): L.append(str(s))
def head(rel, n=12):
    t=open(os.path.join(ROOT,rel),encoding="utf-8").read().split("\n")
    P(f"########## {rel}  lines={len(t)}")
    for i,l in enumerate(t[:n],1): P(f"{i:4d}| {l}")
    P("  --- 标题骨架 ---")
    for i,l in enumerate(t,1):
        if re.match(r"^#{1,3}\s", l): P(f"{i:4d}| {l}")
    P()
    return t

def grep(rel, pat, ctx=0, maxhits=25, label=""):
    t=open(os.path.join(ROOT,rel),encoding="utf-8").read().split("\n")
    P(f"===== GREP [{label or pat}] in {rel} =====")
    n=0
    for i,l in enumerate(t,1):
        if re.search(pat,l):
            n+=1
            if n<=maxhits:
                P(f"{i:4d}| {l[:600]}")
    P(f"  [total hits={n}]")
    P()

head(r"results\_fake_kd_itemwise_adjudication_2026_10_21.md")
head(r"results\_kabla6_trigger_review_adjudication_2026_10_21.md")
head(r"results\_preexp_design_new_construct_mda8a24_2026_10_20.md", 10)

grep(r"results\_fake_kd_itemwise_adjudication_2026_10_21.md", r"前提不成就|归因层|落 kd 时点|不成立（翻转", 0, 18, "P2/P7 翻转判词")
grep(r"results\_kabla6_trigger_review_adjudication_2026_10_21.md", r"触发|停手报回|真证伪|A6 行|不成立", 0, 20, "A6 触发")
grep(r"results\_kd_identified_defect_attribution_caliber_2026_10_20.md", r"四要件|假证伪排除|第五要件|缺陷已辨明", 0, 20, "Q0 要件面")
grep(r"results\_kd_sepcal7_final_verdict_2026_10_20.md", r"KD-CMP2S-4|G-乙-3|G-乙-4|残余", 0, 20, "SEPCAL-7 残余")
grep(r"results\_preexp_design_new_construct_mda8a24_2026_10_20.md", r"甲-C6|甲-C7|判死线|预登记|候选构造", 0, 20, "新构造草案 甲-C6/C7")
grep(r"results\_d13_rename_candidates_2026_10_21.md", r"DEN16|候选 5|撞名|编号域", 0, 20, "DEN16 荐案")
grep(r"results\_kd_two_gates_boundary_proposal_2026_10_21.md", r"候选甲|阻却行为|候选乙|候选丙", 0, 20, "界线候选甲")
grep(r"results\_mda8a24_release_trigger_proposals_2026_10_20.md", r"释-甲|释-乙|释-丙|三候选|闭集", 0, 20, "释三候选")
grep(r"results\_kd_false9_wave0_calibers_2026_10_20.md", r"K-W0-|P3|P4|P5|P6|P7|P8", 0, 12, "波0 口径")
open(os.path.join(ROOT,"_tools_v176_open2.txt"),"w",encoding="utf-8").write("\n".join(L))
print("ok lines:", len(L))
