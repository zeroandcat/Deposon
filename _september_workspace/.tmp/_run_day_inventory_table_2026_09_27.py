import json
import os
import re

WS = r"D:\私人资料\deposon-repo"
raw = open(os.path.join(os.environ["TEMP"], "day_inv.json"), "rb").read()
for enc in ("utf-16", "utf-8-sig", "utf-8"):
    try:
        rep = json.loads(raw.decode(enc))
        break
    except (UnicodeDecodeError, json.JSONDecodeError):
        continue
else:
    raise SystemExit("cannot decode day_inv.json")

files = rep["today_inventory"]["files"]


def cat(rel):
    b = rel.split("/")[-1]
    if rel.startswith("docs/"):
        return "6 勘误链版本"
    if rel.startswith("letters/"):
        if "indep_judgment" in b or "calibration_change" in b:
            return "5 委托件 / 独立judgment请求"
        return "5 委托件"
    if "_v4_pi_cot_v3" in rel:
        return "4 V4 线 pi_cot v3 系"
    if "_v4_supp_t15r2" in rel:
        return "4 V4 线 pi_cot v3 系"
    if b in ("_v4_maindir_count_monitor_2026_09_27.md",
             "_v4_day_inventory_measure_2026_09_27.py"):
        return "7 审链 / 治理件"
    if "_v3_s" in rel:
        if "preexp" in rel:
            return "1b 预实验件（preexp 面）"
        return "2 V3-S 系"
    if "_v3_n_" in rel:
        return "3 V3 采集件"
    if "_v3_recheck" in rel:
        if "preexp" in rel:
            return "1b 预实验件（preexp 面）"
        if "jsv_phase_data" in rel:
            return "3 V3 采集件"
        if "verdict_register" in rel:
            return "1a· V3-R 系 · 汇总登记"
        return "1a V3-R 系（recheck 主系）"
    return "9 未归类"


order = ["1a V3-R 系（recheck 主系）", "1a· V3-R 系 · 汇总登记",
         "1b 预实验件（preexp 面）", "2 V3-S 系", "3 V3 采集件",
         "4 V4 线 pi_cot v3 系", "5 委托件", "5 委托件 / 独立judgment请求",
         "6 勘误链版本", "7 审链 / 治理件", "9 未归类"]

groups = {}
for f in files:
    groups.setdefault(cat(f["rel"]), []).append(f)

out = []
total = 0
totalb = 0
for k in order:
    g = groups.get(k, [])
    if not g:
        continue
    gb = sum(x["bytes"] for x in g)
    total += len(g)
    totalb += gb
    out.append("")
    out.append("### %s — %d 件 / %s B" % (k, len(g), format(gb, ",")))
    out.append("")
    out.append("| # | 相对路径 | 字节 | SHA-12 | mtime |")
    out.append("|:-:|---|---:|:-:|---|")
    for i, f in enumerate(g, 1):
        out.append("| %d | `%s` | %s | `%s` | %s |" %
                   (i, f["rel"], format(f["bytes"], ","), f["sha12"], f["mtime"]))

print("\n".join(out))
print("")
print("TOTAL %d 件 / %s B" % (total, format(totalb, ",")))
print("CHECK json total %d 件 / %s B" % (rep["today_inventory"]["count"],
                                         format(rep["today_inventory"]["total_bytes"], ",")))
