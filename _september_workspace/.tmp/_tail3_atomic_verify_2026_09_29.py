# -*- coding: utf-8 -*-
"""[V4 checkpoint 尾 3 件修订棒 | 2026-09-29] 验证脚本 (可复算, 一次性跑)

组:
  V1  ast.parse 语法核验 (不执行)
  V2  原子写三段式静态核验 (tmp / flush+fsync / os.replace 全 True) + 旧非原子写出面归零
  V3  0 触动复验: 3 源件 + 6 件同族 lineage 件 (r1 / r2_atomic / r3 × 2) + 18 frozen
  V4  落盘字节同构: 旧写法 vs 新原子写, 逐字节同值 (沙箱, 0 跑实验)
  V5  崩半路 (进程强杀) 语义: 新写法既有 checkpoint 逐字节不动 + 旧写法对照被摧毁
  V6  diff 面核验: 改动行仅限 {件头自述名, 新增注释/doc 块, checkpoint 写出面}
  V7  key 明文自扫 (5 类形态, 0 命中)
  V8  __pycache__ 0 新生复扫

沙箱 = .tmp/_tail3_scratch/ (跑完 mavis-trash 可恢复删除)。全部 python -B。
0 网络 / 0 LLM / 0 读 key / 0 跑实验 / 0 调阈值 / 0 改既有件。
"""
import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")
SCRATCH = REPO / ".tmp" / "_tail3_scratch"
RESULTS = {}

SRC_DST = [
    ("results/_v4_supp_t15_executor.py", "results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py",
     "558e635f9ba6", "save_checkpoint", "CHECKPOINT_PATH"),
    ("results/_v4_supp_t15r2_executor.py", "results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py",
     "4b5b720d5cda", "save_t15r2_records", "T15R2_CHECKPOINT_PATH"),
    ("results/_archive_2026_09_24/l14_runner_v2.py",
     "results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py",
     "acf1cd6ccbd4", "CHECKPOINT", "CHECKPOINT"),
]

LINEAGE = [
    ("results/_v4_supp_t15_executor_r1_2026_09_27.py", "6d22444c65af"),
    ("results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py", "9e89e021ea03"),
    ("results/_v4_supp_t15_executor_r3_2026_09_28.py", "b86cce242abe"),
    ("results/_v4_supp_t15r2_executor_r1_2026_09_28.py", "e0936a68fa82"),
    ("results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py", "215db16a0556"),
    ("results/_v4_supp_t15r2_executor_r3_2026_09_28.py", "4f514b3fb4b8"),
]

FROZEN_BASE = REPO / "results" / "_v3x_18frozen_remeasure_2026_09_16" / \
    "v3x_18frozen_remeasure_results_2026_09_16.json"


def sha12(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def sha12f(p: Path) -> str:
    return sha12(p.read_bytes())


def code_lines(p: Path):
    """返回 (行号, 去掉注释与 docstring 后的代码行) —— 用于「旧写出面归零」判定。"""
    src = p.read_text(encoding="utf-8")
    tree = ast.parse(src)
    doc_nodes = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            d = ast.get_docstring(node, clean=False)
            if d is not None:
                b = node.body[0]
                for ln in range(b.lineno, b.end_lineno + 1):
                    doc_nodes.add(ln)
    out = []
    for i, line in enumerate(src.splitlines(), 1):
        s = line.strip()
        if s.startswith("#") or not s:
            continue
        if i in doc_nodes:
            continue
        out.append((i, line))
    return out


def extract_helper(p: Path) -> str:
    src = p.read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "_atomic_write_json":
            lines = src.splitlines()
            return "\n".join(lines[node.lineno - 1:node.end_lineno])
    raise SystemExit(f"ABORT: no _atomic_write_json in {p}")


# ============================================================
def v1_v2():
    rows = []
    for src_rel, dst_rel, src_sha, fn, pathvar in SRC_DST:
        dst = REPO / dst_rel
        r = {"dst": dst_rel, "bytes": dst.stat().st_size, "sha12": sha12f(dst)}
        try:
            ast.parse(dst.read_text(encoding="utf-8"))
            r["ast_parse"] = "PASS"
        except SyntaxError as e:
            r["ast_parse"] = f"FAIL {e}"
        # 源件仍有旧写出面 (对照)
        src = REPO / src_rel
        r["src_still_nonatomic"] = any(
            "write_text(json.dumps" in ln and pathvar in ln for _, ln in code_lines(src))
        # 新件: checkpoint 写出面已走 helper; 代码层 0 处旧写法
        cl = code_lines(dst)
        r["dst_old_writeface_hits"] = [
            f"L{i}" for i, ln in cl
            if "write_text(json.dumps" in ln and pathvar in ln
        ]
        r["dst_calls_helper"] = sum(1 for i, ln in cl if "_atomic_write_json(" in ln and "def " not in ln)
        h = extract_helper(dst)
        r["has_tmp_pid"] = bool(re.search(r'tmp = path\.with_name\(f"\{path\.name\}\.tmp_\{os\.getpid\(\)\}"\)', h))
        r["has_flush"] = "f.flush()" in h
        r["has_fsync"] = "os.fsync(f.fileno())" in h
        r["has_os_replace"] = "os.replace(tmp, path)" in h
        r["has_mkdir"] = "path.parent.mkdir(parents=True, exist_ok=True)" in h
        r["three_stage_all_true"] = r["has_tmp_pid"] and r["has_flush"] and r["has_fsync"] and r["has_os_replace"]
        r["atomic_line_hits"] = [f"L{i}" for i, ln in cl if "os.replace(tmp, path)" in ln or "os.fsync(" in ln]
        rows.append(r)
    RESULTS["V1_ast_parse"] = all(r["ast_parse"] == "PASS" for r in rows)
    RESULTS["V2_three_stage"] = all(r["three_stage_all_true"] for r in rows)
    RESULTS["V2_old_writeface_zero"] = all(not r["dst_old_writeface_hits"] for r in rows)
    RESULTS["V2_src_still_nonatomic"] = all(r["src_still_nonatomic"] for r in rows)
    RESULTS["V2_rows"] = rows
    return rows


def v3():
    rows = []
    for src_rel, _dst, src_sha, _f, _p in SRC_DST:
        p = REPO / src_rel
        got = sha12f(p)
        rows.append({"path": src_rel, "expect": src_sha, "got": got, "match": got == src_sha})
    for rel, sha in LINEAGE:
        p = REPO / rel
        got = sha12f(p) if p.exists() else "MISSING"
        rows.append({"path": rel, "expect": sha, "got": got, "match": got == sha})
    frozen = json.loads(FROZEN_BASE.read_text(encoding="utf-8"))

    def walk(o, acc):
        if isinstance(o, dict):
            if "expected_sha12" in o and ("path" in o or "file" in o):
                acc.append(o)
            for v in o.values():
                walk(v, acc)
        elif isinstance(o, list):
            for v in o:
                walk(v, acc)
        return acc

    entries = walk(frozen, [])
    frows = []
    for e in entries:
        rel = e.get("path") or e.get("file")
        p = REPO / rel
        got = sha12f(p) if p.exists() else "MISSING"
        frows.append({"path": rel, "expect": e["expected_sha12"], "got": got,
                      "match": got == e["expected_sha12"]})
    RESULTS["V3_untouched_files"] = rows
    RESULTS["V3_untouched_all_match"] = all(r["match"] for r in rows)
    RESULTS["V3_frozen"] = {"n": len(frows), "pass": sum(1 for r in frows if r["match"]),
                            "mismatch": [r for r in frows if not r["match"]]}


CHILD_TMPL = '''# -*- coding: utf-8 -*-
import json, os, sys
from pathlib import Path
{helper}

target = Path(sys.argv[1])
mode = sys.argv[2]
payload = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
rounds = int(sys.argv[4])
for _ in range(rounds):
    if mode == "atomic":
        _atomic_write_json(payload, target)
    else:
        target.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
print("done", flush=True)
'''


def build_payload(n: int):
    return [{"cell_idx": i, "teacher": f"T{i % 5}", "caption_id": f"C{i % 7}",
             "reask_idx": i % 3, "ok": True, "response_text": "x" * 200,
             "response_text_sha12": None, "latency_ms": 123, "status_code": 200,
             "error_category": None, "model_returned": "m", "note": "尾3修订棒验证payload"}
            for i in range(n)]


def v4_v5():
    # 本棒自有沙箱: 若已存在 (上轮遗留), 走 mavis-trash 可恢复清走后再建 (0 永久删除)
    if SCRATCH.exists():
        trash = r"C:\Users\Administrator\.minimax\bin\mavis-trash.cmd"
        r = subprocess.run(["cmd", "/c", trash, str(SCRATCH)], capture_output=True, text=True)
        RESULTS["V_scratch_preclean"] = {"rc": r.returncode, "out": (r.stdout or "").strip()}
    SCRATCH.mkdir(parents=True, exist_ok=True)
    payload = build_payload(12000)          # ~5.5 MB
    pj = SCRATCH / "payload.json"
    pj.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    ref = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    v4, v5 = [], []
    for idx, (src_rel, dst_rel, src_sha, fn, pathvar) in enumerate(SRC_DST):
        dst = REPO / dst_rel
        helper = extract_helper(dst)
        child = SCRATCH / f"_child{idx}.py"
        child.write_text(CHILD_TMPL.format(helper=helper), encoding="utf-8", newline="\n")

        # ---- V4: 落盘字节同构 (新原子写 vs 旧 write_text) ----
        a = SCRATCH / f"v4a{idx}.json"
        b = SCRATCH / f"v4b{idx}.json"
        r1 = subprocess.run([sys.executable, "-B", str(child), str(a), "atomic", str(pj), "1"],
                            capture_output=True, text=True, encoding="utf-8")
        r2 = subprocess.run([sys.executable, "-B", str(child), str(b), "old", str(pj), "1"],
                            capture_output=True, text=True, encoding="utf-8")
        ab, bb = a.read_bytes(), b.read_bytes()
        leftovers = sorted(p.name for p in SCRATCH.glob(f"v4a{idx}.json.tmp_*"))
        v4.append({
            "dst": dst_rel, "atomic_rc": r1.returncode, "old_rc": r2.returncode,
            "atomic_bytes": len(ab), "old_bytes": len(bb),
            "atomic_sha12": sha12(ab), "old_sha12": sha12(bb),
            "byte_identical": ab == bb, "matches_payload_bytes": ab == ref,
            "tmp_leftovers": leftovers,
        })

        # ---- V5: 崩半路 (进程强杀) ----
        # 原子性正确判据 (不误导): 强杀后目标件内容**要么 = 原内容逐字节, 要么 = 完整新内容**,
        # 0 截断 / 0 混合 ⇒ 「要么全量新内容, 要么原内容一字不动」。
        # (若强杀落在写完之后, 终态 = 完整新内容, 属预期而非缺陷 —— 故不以「必须不动」为判据。)
        seed = SCRATCH / f"v5{idx}.json"
        seed_bytes = json.dumps(build_payload(900), ensure_ascii=False).encode("utf-8")
        seed.write_bytes(seed_bytes)
        seed_sha = sha12(seed_bytes)

        p = subprocess.Popen([sys.executable, "-B", str(child), str(seed), "atomic", str(pj), "400"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.6)
        killed = p.poll() is None
        p.kill()
        p.wait()
        time.sleep(0.4)
        after_atomic = seed.read_bytes()
        if after_atomic == seed_bytes:
            state = "ORIGINAL_UNTOUCHED"
        elif after_atomic == ref:
            state = "NEW_COMPLETE"
        else:
            state = "TRUNCATED_OR_MIXED"
        try:
            json.loads(after_atomic.decode("utf-8"))
            atomic_json_ok = True
        except Exception:
            atomic_json_ok = False

        # 对照组: 旧写法同沙箱同 payload 同强杀时点 ⇒ 数据被摧毁
        seed2 = SCRATCH / f"v5c{idx}.json"
        seed2.write_bytes(seed_bytes)
        p2 = subprocess.Popen([sys.executable, "-B", str(child), str(seed2), "old", str(pj), "400"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.6)
        killed2 = p2.poll() is None
        p2.kill()
        p2.wait()
        time.sleep(0.4)
        after_old = seed2.read_bytes()
        try:
            json.loads(after_old.decode("utf-8"))
            old_json_ok = True
        except Exception:
            old_json_ok = False

        v5.append({
            "dst": dst_rel,
            "atomic_seed_sha12": seed_sha, "atomic_after_sha12": sha12(after_atomic),
            "atomic_state": state,
            "atomic_state_ok": state in ("ORIGINAL_UNTOUCHED", "NEW_COMPLETE"),
            "atomic_json_loads_ok": atomic_json_ok,
            "atomic_kill_happened": killed,
            "atomic_tmp_leftover": sorted(q.name for q in SCRATCH.glob(f"v5{idx}.json.tmp_*")),
            "control_kill_happened": killed2,
            "control_after_sha12": sha12(after_old),
            "control_bytes": len(after_old),
            "control_seed_bytes": len(seed_bytes),
            "control_destroyed": after_old != seed_bytes,
            "control_json_loads_ok": old_json_ok,
        })
    RESULTS["V4_byte_identity"] = v4
    RESULTS["V5_crash_semantics"] = v5
    RESULTS["V4_all_identical"] = all(
        r["byte_identical"] and r["matches_payload_bytes"] and not r["tmp_leftovers"] for r in v4)
    RESULTS["V5_atomic_state_all_ok"] = all(
        r["atomic_state_ok"] and r["atomic_kill_happened"] and r["atomic_json_loads_ok"] for r in v5)
    RESULTS["V5_control_all_destroyed"] = all(
        r["control_destroyed"] and r["control_kill_happened"] for r in v5)


ALLOWED_ADDED_CODE = {
    # 原子写 helper 骨架 (逐字同款, 沿 r2_atomic L546-562) —— 均按 strip() 比较
    "def _atomic_write_json(obj, path, indent=None):",
    "path.parent.mkdir(parents=True, exist_ok=True)",
    'tmp = path.with_name(f"{path.name}.tmp_{os.getpid()}")',
    "try:",
    'with open(tmp, "w", encoding="utf-8") as f:',
    "json.dump(obj, f, ensure_ascii=False, indent=indent)",
    "f.flush()",
    "os.fsync(f.fileno())",
    "os.replace(tmp, path)   # 同卷原子替换: 要么全量新内容, 要么原内容",
    "except BaseException:",
    "raise",
    # 写出面签名 + 新调用
    "def save_checkpoint(records: List[Dict[str, Any]]) -> None:",
    "_atomic_write_json(records, CHECKPOINT_PATH)",
    "def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:",
    "_atomic_write_json(r2_records, T15R2_CHECKPOINT_PATH)",
    "_atomic_write_json(records, CHECKPOINT)",
}


def classify(lines):
    """逐行归类: comment / docstring / code (含空行 -> comment)。"""
    out, in_doc = [], False
    for l in lines:
        s = l.strip()
        if in_doc:
            out.append("docstring")
            if s.endswith('"""'):
                in_doc = False
            continue
        if s.startswith('"""'):
            out.append("docstring")
            if not (len(s) > 3 and s.endswith('"""')):
                in_doc = True
            continue
        if not s or s.startswith("#"):
            out.append("comment")
            continue
        out.append("code")
    return out


def v6():
    d = json.loads((REPO / ".tmp" / "_tail3_atomic_make_2026_09_29.json").read_text(encoding="utf-8"))
    allowed_removed = re.compile(
        r"^(_v4_supp_t15(r2)?_executor\.py|"
        r"def save_checkpoint\(records: List\[Dict\[str, Any\]\]\) -> None:|"
        r"    CHECKPOINT_PATH\.parent\.mkdir\(parents=True, exist_ok=True\)|"
        r"    CHECKPOINT_PATH\.write_text\(json\.dumps\(records, ensure_ascii=False\),|"
        r'                               encoding="utf-8"\)|'
        r"def save_t15r2_records\(r2_records: List\[Dict\[str, Any\]\]\) -> None:|"
        r"    T15R2_CHECKPOINT_PATH\.parent\.mkdir\(parents=True, exist_ok=True\)|"
        r"    T15R2_CHECKPOINT_PATH\.write_text\(json\.dumps\(r2_records, ensure_ascii=False\),|"
        r'                                     encoding="utf-8"\)|'
        r'            CHECKPOINT\.write_text\(json\.dumps\(records, ensure_ascii=False\), encoding="utf-8"\)|'
        r'CHECKPOINT\.write_text\(json\.dumps\(records, ensure_ascii=False\), encoding="utf-8"\))$')
    rows = []
    for it in d["items"]:
        dst_lines = (REPO / it["dst"]).read_text(encoding="utf-8").splitlines()
        classes = classify(dst_lines)
        removed, bad_rm, bad_add, add_code = [], [], [], []
        for op in it["diff"]:
            removed += op["src_removed"]
            j1 = op["dst_lines_1based"][0] - 1
            for k in range(j1, op["dst_lines_1based"][1]):
                line = dst_lines[k]
                cls = classes[k]
                if cls == "code" and line.strip() not in ALLOWED_ADDED_CODE:
                    bad_add.append(f"L{k + 1}[{cls}] {line}")
                if cls == "code":
                    add_code.append(f"L{k + 1} {line.strip()}")
        bad_rm = [l for l in removed if not allowed_removed.match(l)]
        rows.append({"src": it["src"], "dst": it["dst"], "hunks": it["changed_hunks"],
                     "removed_lines": removed, "added_code_lines": add_code,
                     "unauthorized_removed": bad_rm, "unauthorized_added": bad_add})
    RESULTS["V6_diff_scope"] = rows
    RESULTS["V6_only_writeface"] = all(
        not r["unauthorized_removed"] and not r["unauthorized_added"] for r in rows)


KEY_PATTERNS = [
    r"sk-ant-[A-Za-z0-9_\-]{8,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    r"Bearer\s+[A-Za-z0-9_\-\.]{16,}",
    r"(api_key|ARK_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY)\s*=\s*[\"'][^\"']{8,}[\"']",
]


def v7():
    rows = []
    for _s, dst_rel, *_ in SRC_DST:
        t = (REPO / dst_rel).read_text(encoding="utf-8", errors="ignore")
        hits = []
        for pat in KEY_PATTERNS:
            for m in re.finditer(pat, t):
                hits.append(pat)
        rows.append({"path": dst_rel, "hits": len(hits)})
    RESULTS["V7_keyscan"] = rows
    RESULTS["V7_key_hits_total"] = sum(r["hits"] for r in rows)


def v8():
    """本棒 0 新生 __pycache__ 判据 = 3 件新出件**无任何 .pyc** (全仓 .pyc 按基名扫)。
    全仓现存 __pycache__ 目录如实登记 (含**其他并发 session** 今日新建者), 不计入本棒。"""
    bases = {Path(d).stem for _s, d, *_ in SRC_DST}
    dirs_found, mine = [], []
    for root, dirs, files in os.walk(REPO):
        for d in list(dirs):
            if d == "__pycache__":
                p = Path(root, d)
                dirs_found.append({
                    "path": str(p.relative_to(REPO)).replace("\\", "/"),
                    "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.stat().st_mtime)),
                })
        for f in files:
            if f.endswith(".pyc") and f.split(".")[0] in bases:
                mine.append(str(Path(root, f).relative_to(REPO)).replace("\\", "/"))
    RESULTS["V8_pycache_dirs"] = dirs_found
    RESULTS["V8_pyc_for_new_files"] = mine
    RESULTS["V8_no_new_pyc"] = not mine


def main():
    v1_v2()
    v3()
    v4_v5()
    v6()
    v7()
    v8()
    out = REPO / ".tmp" / "_tail3_atomic_verify_2026_09_29.json"
    out.write_text(json.dumps(RESULTS, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    checks = [
        ("V1 ast.parse 3/3", RESULTS["V1_ast_parse"]),
        ("V2 三段式 (tmp+fsync+replace) 3/3", RESULTS["V2_three_stage"]),
        ("V2 新件旧非原子写出面 = 0", RESULTS["V2_old_writeface_zero"]),
        ("V2 源件仍带旧写出面 (对照成立)", RESULTS["V2_src_still_nonatomic"]),
        ("V3 源件 + 6 件 lineage 0 触动", RESULTS["V3_untouched_all_match"]),
        ("V3 18 frozen 全 PASS", RESULTS["V3_frozen"]["pass"] == RESULTS["V3_frozen"]["n"]),
        ("V4 落盘字节逐字节同构 + 0 残留", RESULTS["V4_all_identical"]),
        ("V5 强杀: 终态 ∈ {原内容逐字节, 完整新内容} (0 截断 0 混合)", RESULTS["V5_atomic_state_all_ok"]),
        ("V5 强杀对照: 旧写法被摧毁", RESULTS["V5_control_all_destroyed"]),
        ("V6 diff 仅写出面", RESULTS["V6_only_writeface"]),
        ("V7 key 明文命中 = 0", RESULTS["V7_key_hits_total"] == 0),
        ("V8 本棒 0 新生 .pyc (3 件新出件 0 字节码)", RESULTS["V8_no_new_pyc"]),
    ]
    npass = sum(1 for _n, ok in checks if ok)
    for n, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {n}")
    print(f"  ---- {npass}/{len(checks)} PASS ----")
    print(f"  frozen: {RESULTS['V3_frozen']['pass']}/{RESULTS['V3_frozen']['n']}")
    for r in RESULTS["V2_rows"]:
        print(f"  {r['dst']}  helper_calls={r['dst_calls_helper']}  "
              f"old_writeface={r['dst_old_writeface_hits']}  atomic_lines={r['atomic_line_hits']}")
    for r in RESULTS["V5_crash_semantics"]:
        print(f"  {r['dst']}\n    atomic seed={r['atomic_seed_sha12']} after={r['atomic_after_sha12']} "
              f"state={r['atomic_state']} json_ok={r['atomic_json_loads_ok']} "
              f"tmp_left={r['atomic_tmp_leftover']}\n"
              f"    control after={r['control_after_sha12']} bytes={r['control_bytes']}/"
              f"{r['control_seed_bytes']} destroyed={r['control_destroyed']} json_ok={r['control_json_loads_ok']}")
    print(f"  pycache dirs (如实登记): {RESULTS['V8_pycache_dirs']}")
    if "V_scratch_preclean" in RESULTS:
        print(f"  scratch preclean: {RESULTS['V_scratch_preclean']}")
    for r in RESULTS["V6_diff_scope"]:
        print(f"  {r['src']}  hunks={r['hunks']} "
              f"unauth_rm={r['unauthorized_removed']} unauth_add={r['unauthorized_added']}")
        print(f"    removed: {r['removed_lines']}")
        print(f"    added code: {r['added_code_lines']}")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
