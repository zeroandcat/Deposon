# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 非原子 JSON 覆盖写 全仓登记扫描（修复面 + 登记面）。

判定口径（逐条写死, 0 主观）：
  原子写 = 写临时件 + os.replace 同卷替换（`os.replace` 出现于同函数/邻近行）
  非原子 = 直接以 "w" 模式写**目标路径**本身（0 临时件 0 replace）
  checkpoint 类 = 增量/续跑状态落盘（被 load_* 读回决定 skip/续跑）
  终端产出类 = 跑完一次性交付 JSON（崩半路只损本次产出, 不损已累计状态）

分类处置：
  FIXED_NEW_NAME   本棒出新名件修复（原件 0 触动）
  REGISTER_NO_FIX  被引件 / 归档件 / 终端产出类 —— 登记不修（派工单口径）
"""
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path("D:/私人资料/deposon-repo")
SKIP_DIRS = {".git", "__pycache__", ".mavis", ".trae", "node_modules"}

# 非原子写：目标路径直接 "w"
RE_DUMP_OPEN = re.compile(r"json\.dump\([^)]*?,\s*open\(\s*([^,)]+?)\s*,\s*[\"']w[\"']")
RE_WRITETEXT = re.compile(r"([A-Za-z_][\w\.\(\)\[\]\"'\s/+\-]*?)\.write_text\(\s*json\.dumps\(")
RE_HAS_REPLACE = re.compile(r"os\.replace\(")

# 已修复面（本棒新名件）
FIXED = {
    "results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py": (
        "results/_v4_supp_t15r2_executor_r1_2026_09_28.py",
        "checkpoint 类: .tmp/_t15r2_records.json (T1.5r2 records 62 条)"),
    "results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py": (
        "results/_v4_supp_t15_executor_r1_2026_09_27.py",
        "checkpoint 类: .tmp/_t15_records.json (T1.5 状态锚 120 条)"),
}

# 逐件人工判定（探针实测后写入, 附判定依据; 未列者 = 登记不修 + 默认终端产出类）
JUDGE = {
    "results/_v4_supp_t15r2_executor_r1_2026_09_28.py":
        ("REGISTER_NO_FIX", "checkpoint 类", "被引（R1 告警块 L477-479 自登记缺陷 (c)「本棒只登记不修」）"),
    "results/_v4_supp_t15r2_executor.py":
        ("REGISTER_NO_FIX", "checkpoint 类", "被引（R1 前身, 被 R1 与 verdict 引用）"),
    "results/_v4_supp_t15_executor_r1_2026_09_27.py":
        ("REGISTER_NO_FIX", "checkpoint 类", "被引（T15 verdict `52C985429C91` 等引用）"),
    "results/_v4_supp_t15_executor.py":
        ("REGISTER_NO_FIX", "checkpoint 类", "被引（T15 verdict 记 `558E635F9BA6`）"),
    "results/_archive_2026_09_24/l14_runner_v2.py":
        ("REGISTER_NO_FIX", "checkpoint 类", "归档件 + 被 L14 verdict §9.1 引用"),
    ".tmp/_t15_update_result.py":
        ("REGISTER_NO_FIX", "终端产出类", "覆盖写被引交付件 results/_v4_supp_t15_result.json"),
}


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def referenced(rel: str, stems) -> int:
    """粗判是否被仓内其它件按文件名引用（>=1 命中即视为被引）。"""
    n = 0
    for f in stems:
        if f == rel:
            continue
        try:
            t = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if Path(rel).name in t:
            n += 1
    return n


def main():
    py = [p for p in ROOT.rglob("*.py")
          if not any(s in p.parts for s in SKIP_DIRS)]
    doc = [p for p in ROOT.rglob("*")
           if p.suffix in {".md", ".json", ".txt", ".ps1"} and p.is_file()
           and not any(s in p.parts for s in SKIP_DIRS)]

    rows = []
    for f in py:
        rel = f.relative_to(ROOT).as_posix()
        txt = f.read_text(encoding="utf-8", errors="ignore")
        lines = txt.splitlines()
        hits = []
        for i, ln in enumerate(lines, 1):
            for m in RE_DUMP_OPEN.finditer(ln):
                hits.append({"line": i, "kind": "json.dump(open(...,'w'))", "target": m.group(1).strip()})
            for m in RE_WRITETEXT.finditer(ln):
                hits.append({"line": i, "kind": ".write_text(json.dumps(...))", "target": m.group(1).strip()})
        if not hits:
            continue
        # 排除: 目标本身是 .tmp 临时件（= 已具备原子写三段式）
        atomicish = [h for h in hits if ".tmp" in h["target"] or ".tmp_" in h["target"]]
        real = [h for h in hits if h not in atomicish]
        if not real:
            continue
        disp, klass, why = JUDGE.get(rel, ("REGISTER_NO_FIX", "终端产出类", "默认登记不修（非 checkpoint 类 / 未单列）"))
        rows.append({
            "path": rel,
            "bytes": f.stat().st_size,
            "sha12": sha12(f),
            "n_sites": len(real),
            "sites": real,
            "has_os_replace_elsewhere": bool(RE_HAS_REPLACE.search(txt)),
            "disposition": disp,
            "class": klass,
            "reason": why,
        })

    rows.sort(key=lambda r: (r["class"] != "checkpoint 类", r["path"]))
    n_cp = sum(1 for r in rows if r["class"] == "checkpoint 类")
    rep = {
        "schema": "v4_cpatomic_register/1", "date": "2026-09-28",
        "n_files_with_nonatomic": len(rows),
        "n_checkpoint_class": n_cp,
        "n_terminal_class": len(rows) - n_cp,
        "fixed_new_name": {k: {"source": v[0], "role": v[1]} for k, v in FIXED.items()},
        "rows": rows,
    }
    out = ROOT / ".tmp/_cpatomic_register_2026_09_28.json"
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"非原子 JSON 覆盖写 落盘件 = {len(rows)} 件"
          f"（checkpoint 类 {n_cp} / 终端产出类 {len(rows)-n_cp}）")
    print("\n--- checkpoint 类（修/登记分界所在）---")
    for r in rows:
        if r["class"] == "checkpoint 类":
            print(f"  [{r['disposition']:16s}] {r['path']}")
            print(f"       {r['bytes']:7d} B  sha12={r['sha12']}  sites={r['n_sites']}"
                  f"  os.replace_elsewhere={r['has_os_replace_elsewhere']}")
            print(f"       依据: {r['reason']}")
    print("\n--- 终端产出类（前 12 件, 其余见 JSON）---")
    for r in [x for x in rows if x["class"] != "checkpoint 类"][:12]:
        print(f"  {r['path']:62s} {r['sha12']}  sites={r['n_sites']}")
    print(f"\nOUT -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
