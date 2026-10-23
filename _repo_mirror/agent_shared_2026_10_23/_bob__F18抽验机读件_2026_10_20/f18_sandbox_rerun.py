#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""鲍勃 · F18 沙箱确定性重跑驱动（0 改稿 · 只读 shared）

方法（沿 R6 差量验收轮先例）：cp 脚本 → 常量块 env 重定向补丁 → 临时目录执行
→ 产物与交付件逐字节比对。shared 输入件全程只读。
"""
import os, sys, json, hashlib, subprocess, shutil

BASE = "/home/z/my-project/agents/6a962cc259312f271f3f1e73/f18_check_2026_10_20"
SB = BASE + "/sandbox"
SNAP = BASE + "/snap"
PRE_TEX = BASE + "/pre_f18_from_tar/fiction_that_feeds_back.tex"   # 45887c4316d3（归档 tar 内件）
DAVE_SHEET = BASE + "/pre_f18_from_tar/arxiv_metadata.txt"          # 戴夫 20:01 版（归档 tar 内件）

os.makedirs(SB, exist_ok=True)
res = {"checks": [], "fail": 0}
def chk(name, ok, detail):
    res["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok: res["fail"] += 1
    print(("PASS " if ok else "FAIL ") + name + " | " + detail)
    return ok

def sha12(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]

# ---- 0. 预 F18 态正本门 ------------------------------------------------------
chk("S0 输入正本＝45887c4316d3·132,269 B（归档 tar 内件）",
    sha12(PRE_TEX) == "45887c4316d3" and os.path.getsize(PRE_TEX) == 132269,
    "sha12 %s · %d B" % (sha12(PRE_TEX), os.path.getsize(PRE_TEX)))
chk("S0b 输入元数据表＝戴夫 20:01 归档版（7e5e739c8b58·6,074 B）",
    sha12(DAVE_SHEET) == "7e5e739c8b58", "sha12 %s" % sha12(DAVE_SHEET))

# ---- 1. 补丁：常量块 env 重定向 ----------------------------------------------
src = open(SNAP + "/apply_r6_f18_abstract.py", encoding="utf-8").read()
OLD_BLOCK = '''SHARED = "/home/z/my-project/shared/查理_FTFB_R6重构稿_2026"
R6_PATH = SHARED + "/fiction_that_feeds_back.tex"
DIFF_PATH = SHARED + "/F18_abstract_unified_diff.txt"
JSON_PATH = SHARED + "/selfcheck_f18_pairs_log.json"
META_PATH = SHARED + "/arxiv_metadata_abstract_F18_2026_10_20.txt"
MD_PATH = SHARED + "/查理_FTFB_R6落稿自检记录_2026_10_20.md"
DAVE_SHEET = "/home/z/my-project/shared/戴夫_FTFB_R6编译打包_2026/arxiv_metadata.txt"
BACKUP_PATH = ("/home/z/my-project/agents/6a962cc259312f271f3f1e74/r6/"
               "pre_f18_45887c4316d3_fiction_that_feeds_back.tex")'''
NEW_BLOCK = '''import os
SHARED = "/home/z/my-project/shared/查理_FTFB_R6重构稿_2026"
R6_PATH = os.environ.get("BOB_F18_R6", SHARED + "/fiction_that_feeds_back.tex")
DIFF_PATH = os.environ.get("BOB_F18_DIFF", SHARED + "/F18_abstract_unified_diff.txt")
JSON_PATH = os.environ.get("BOB_F18_JSON", SHARED + "/selfcheck_f18_pairs_log.json")
META_PATH = os.environ.get("BOB_F18_META", SHARED + "/arxiv_metadata_abstract_F18_2026_10_20.txt")
MD_PATH = os.environ.get("BOB_F18_MD", SHARED + "/查理_FTFB_R6落稿自检记录_2026_10_20.md")
DAVE_SHEET = os.environ.get("BOB_F18_SHEET", "/home/z/my-project/shared/戴夫_FTFB_R6编译打包_2026/arxiv_metadata.txt")
BACKUP_PATH = os.environ.get("BOB_F18_BACKUP", ("/home/z/my-project/agents/6a962cc259312f271f3f1e74/r6/"
               "pre_f18_45887c4316d3_fiction_that_feeds_back.tex"))'''
assert src.count(OLD_BLOCK) == 1, "常量块未唯一命中"
patched = src.replace(OLD_BLOCK, NEW_BLOCK)
open(SB + "/apply_r6_f18_sandbox.py", "w", encoding="utf-8").write(patched)
chk("S1 沙箱件生成：原脚本＋仅常量块 env 重定向补丁（7 路径）",
    True, "补丁量＝%d→%d 行常量块重写，逻辑零改" % (OLD_BLOCK.count("\n") + 1, NEW_BLOCK.count("\n") + 1))

# ---- 2. 沙箱输入布置 ----------------------------------------------------------
# tex 输入（将被脚本就地覆写为产物）
shutil.copyfile(PRE_TEX, SB + "/in.tex")
# md 前态重构：交付 md 截去 §八追加段（模板以两个换行起首："""\n\n---\n\n## 八、…）
dmd = open(SNAP + "/delivered_selfcheck_md.md", encoding="utf-8").read()
marker = "\n\n---\n\n## 八、F18 摘要压缩增补轮"
i = dmd.find(marker)
assert i > 0 and dmd.count(marker) == 1, "md §八边界未唯一命中"
pre_md = dmd[:i]
assert pre_md.endswith("建议非裁\n"), "md 前态应以 19:38 签名行收束"
open(SB + "/md_base.md", "w", encoding="utf-8").write(pre_md)
chk("S2 md §八前态重构：交付 md － 追加段（边界唯一命中，前态收于 19:38 签名行）",
    True, "前态 %d B；追加段 %d B" % (len(pre_md.encode()), len(dmd[i:].encode())))

env = dict(os.environ)
env.update({
    "BOB_F18_R6": SB + "/in.tex",
    "BOB_F18_DIFF": SB + "/out_diff.txt",
    "BOB_F18_JSON": SB + "/out_pairs.json",
    "BOB_F18_META": SB + "/out_meta.txt",
    "BOB_F18_MD": SB + "/md_base.md",
    "BOB_F18_SHEET": DAVE_SHEET,
    "BOB_F18_BACKUP": SB + "/out_backup.tex",
})

# ---- 3. 执行 ------------------------------------------------------------------
r = subprocess.run([sys.executable, SB + "/apply_r6_f18_sandbox.py"],
                   capture_output=True, text=True, env=env, cwd=SB, timeout=300)
print(r.stdout[-2000:])
chk("S3 沙箱重跑执行：自检全绿零失败（rc=%d）" % r.returncode,
    r.returncode == 0 and "全绿" in r.stdout, "rc=%d；stderr=%s" % (r.returncode, r.stderr[:300]))

# ---- 4. 产物逐字节比对 --------------------------------------------------------
def cmpb(a, b):
    da, db = open(a, "rb").read(), open(b, "rb").read()
    return da == db, len(da), len(db), hashlib.sha256(da).hexdigest()[:12], hashlib.sha256(db).hexdigest()[:12]

ok, la, lb, sa, sb_ = cmpb(SB + "/in.tex", SNAP + "/delivered_f18.tex")
chk("S4 tex 逐字节恒等：沙箱产物＝交付 69125dd78382",
    ok, "沙箱 %s·%d B ＝ 交付 %s·%d B" % (sa, la, sb_, lb))

ok, la, lb, sa, sb_ = cmpb(SB + "/out_diff.txt", SNAP + "/F18_abstract_unified_diff.txt")
chk("S5 diff 逐字节恒等：沙箱产物＝交付 6173b09acfbb",
    ok, "沙箱 %s·%d B ＝ 交付 %s·%d B" % (sa, la, sb_, lb))

# JSON：唯一容许差＝artifacts.private_backup_of_pre_state（重定向路径）
ja = json.load(open(SB + "/out_pairs.json", encoding="utf-8"))
jd = json.load(open(SNAP + "/selfcheck_f18_pairs_log.json", encoding="utf-8"))
CONST_BAK = "/home/z/my-project/agents/6a962cc259312f271f3f1e74/r6/pre_f18_45887c4316d3_fiction_that_feeds_back.tex"
ja_n = json.loads(json.dumps(ja))
ja_n["artifacts"]["private_backup_of_pre_state"] = CONST_BAK
raw_ident = open(SB + "/out_pairs.json", "rb").read() == open(SNAP + "/selfcheck_f18_pairs_log.json", "rb").read()
chk("S6 JSON 恒等：归一化（private_backup_of_pre_state→登记常量）后逐字节恒等",
    json.dumps(ja_n, ensure_ascii=False, indent=2) == json.dumps(jd, ensure_ascii=False, indent=2),
    "原始件恒等=%s；除该字段外恒等（含 pair 全文/检查实测值/cuts/errata）" % raw_ident)

ok, la, lb, sa, sb_ = cmpb(SB + "/out_meta.txt", SNAP + "/arxiv_metadata_abstract_F18_2026_10_20.txt")
chk("S7 metadata 逐字节恒等：沙箱产物＝交付 ea1170c2cad1（输入＝归档 20:01 戴夫表）",
    ok, "沙箱 %s·%d B ＝ 交付 %s·%d B" % (sa, la, sb_, lb))

# md：唯一容许差＝时间戳行（datetime.now → HH:MM）
ma = open(SB + "/md_base.md", encoding="utf-8").read()
lines_a, lines_d = ma.split("\n"), dmd.split("\n")
diff_lines = [k for k in range(max(len(lines_a), len(lines_d)))
              if (lines_a[k] if k < len(lines_a) else None) != (lines_d[k] if k < len(lines_d) else None)]
stamp_ok = all("查理-论文主笔 ｜ 2026-10-20" in lines_a[k] and "｜ R6 增补轮 F18" in lines_a[k]
               and "查理-论文主笔 ｜ 2026-10-20" in (lines_d[k] if k < len(lines_d) else "")
               for k in diff_lines) and len(diff_lines) <= 1
chk("S8 md §八复现：除时间戳行（%d 行）外逐行恒等" % len(diff_lines),
    stamp_ok and len(lines_a) == len(lines_d),
    "差异行=%s" % (diff_lines or "无"))

ok, la, lb, sa, sb_ = cmpb(SB + "/out_backup.tex", PRE_TEX)
chk("S9 私区前态备份复现：沙箱备份＝输入正本",
    ok, "备份 %s·%d B ＝ 输入 %s" % (sa, la, "45887c4316d3"))

# ---- 5. 单轮门（防重放）测试：对 F18 后态再执行必须被拒 ------------------------
env2 = dict(env); env2["BOB_F18_R6"] = SNAP + "/delivered_f18.tex"
r2 = subprocess.run([sys.executable, SB + "/apply_r6_f18_sandbox.py"],
                    capture_output=True, text=True, env=env2, cwd=SB, timeout=300)
chk("S10 前置门有效：F18 后态（69125dd78382）重跑被拒（单轮语义）",
    r2.returncode == 2 and "前置门失败" in r2.stdout and "69125dd78382" in r2.stdout,
    "rc=%d；门消息命中" % r2.returncode)

json.dump(res, open(BASE + "/verify/sandbox_result.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("\n沙箱重跑结果：%d/%d PASS" % (len(res["checks"]) - res["fail"], len(res["checks"])))
sys.exit(1 if res["fail"] else 0)
