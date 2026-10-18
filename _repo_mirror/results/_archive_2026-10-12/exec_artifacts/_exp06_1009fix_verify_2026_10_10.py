# -*- coding: utf-8 -*-
"""EXP-06 · 10-09 版修正副本 ＋ 键名勘正副本 · 静态验证探针（工具件 · 0 属证据面）。

⛔0 运行任何 runner；⛔0 导入被验件（仅 ast.parse 文本层）。
⛔0 以注释判读赋值站点（沿 09-29 版探针之审计提示）—— 判读一律以 AST 为准。
"""
import ast
import hashlib
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = Path(r"_repo_mirror")
PLUG = BASE / "deposon_team" / "plugins"
SRC = PLUG / "_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py"
FIX = PLUG / "_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py"
REN = PLUG / "_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py"

KEY_OLD = "self_verified_only"
KEY_NEW = "verification_basis_self_rewalk_only"


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def enc(p):
    b = p.read_bytes()
    t = b.decode("utf-8")
    return dict(sha12=sha12(p), bytes=len(b), bom=b[:3] == b"\xef\xbb\xbf",
                crlf=t.count("\r\n"))


def assign_sites(path, key):
    """AST 级: 返回 key 之全部赋值站点 (行号, 值表达式文本)。"""
    tree = ast.parse(path.read_bytes().decode("utf-8"))
    sites = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AugAssign):
            targets = [node.target]
        for t in targets:
            if (isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                    and t.slice.value == key):
                sites.append((node.lineno, ast.unparse(node.value)))
    return sites


def const_sites(path, key):
    tree = ast.parse(path.read_bytes().decode("utf-8"))
    return [n.lineno for n in ast.walk(tree)
            if isinstance(n, ast.Assign) and any(
                isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                and t.slice.value == key for t in n.targets)
            and isinstance(n.value, ast.Constant)]


print("== 0. 编码/指纹 ==")
for p in (SRC, FIX, REN):
    print(f"  {p.name[:62]:62s} {enc(p)}")

print("\n== 1. 语法/语义可编译 (ast.parse + compile) ==")
for p in (FIX, REN):
    src = p.read_bytes().decode("utf-8")
    try:
        ast.parse(src)
        compile(src, str(p), "exec")
        print(f"  {p.name[:62]:62s} PASS")
    except SyntaxError as e:
        print(f"  {p.name[:62]:62s} FAIL {e}")

print("\n== 2. 硬写残留 (AST 级 · 唯一语义改动之核) ==")
print(f"  原件 {KEY_OLD} 赋值站点: {assign_sites(SRC, KEY_OLD)}")
print(f"  ①   {KEY_OLD} 赋值站点: {assign_sites(FIX, KEY_OLD)}")
print(f"  ①   {KEY_OLD} 硬写字面量站点: {const_sites(FIX, KEY_OLD)}  (应为空)")
print(f"  ②   {KEY_NEW} 赋值站点: {assign_sites(REN, KEY_NEW)}")
print(f"  ②   {KEY_OLD} 赋值站点: {assign_sites(REN, KEY_OLD)}  (应为空 ⛔0 双写)")
print(f"  ②   {KEY_NEW} 硬写字面量站点: {const_sites(REN, KEY_NEW)}  (应为空)")

print("\n== 3. 字面量残留计数 (全文 · 命中应仅在头块/注记之文档引述) ==")
for p in (FIX, REN):
    t = p.read_bytes().decode("utf-8")
    hits = [i + 1 for i, ln in enumerate(t.split("\n"))
            if f'"{KEY_OLD}"] = True' in ln]
    print(f"  {p.name[:62]:62s} {hits}")

print("\n== 4. 新增键面/函数面在位 ==")
faces = ["INDEP_VERIFY_DECL", "probe_independent_evidence", "independence_verification",
         "independence_deficiency_alarm", "independent_verification_ref",
         "independent_verification_status", "runner_fix_notice",
         f"{KEY_OLD}_basis", "key_rename_migration", "prescription_ref"]
for p in (FIX, REN):
    t = p.read_bytes().decode("utf-8")
    print(f"  {p.name[:62]:62s} " + "  ".join(
        f"{f}={'Y' if f in t else 'N'}" for f in faces))

print("\n== 5. 身份接线 (输出路径 / GENERATOR / task_id / DATE) ==")
for p, tag in ((FIX, "①"), (REN, "②")):
    t = p.read_bytes().decode("utf-8")
    rel = p.relative_to(BASE).as_posix()
    print(f"  {tag} GENERATOR 自指: {'Y' if f'GENERATOR = \"{rel}\"' in t else 'N'}")
    print(f"  {tag} DATE: {[l for l in t.split(chr(10)) if l.startswith('DATE = ')]}")
    print(f"  {tag} task_id: {[l.strip() for l in t.split(chr(10)) if 'task_id' in l]}")
    print(f"  {tag} 输出常量: {[l.strip() for l in t.split(chr(10)) if l.startswith(('P_OUT_', 'REL_'))]}")

print("\n== 6. 0 覆写: 副本声明之输出路径须为新名且不在盘 ==")
for p, tag in ((FIX, "①"), (REN, "②")):
    t = p.read_bytes().decode("utf-8")
    for l in t.split("\n"):
        s = l.strip()
        if s.startswith(("P_OUT_", "REL_")):
            v = s.split("=")[-1].strip().strip('"').replace("BASE / ", "")
            rel = v.strip('"')
            exists = (BASE / rel).exists() if rel.endswith(".json") else None
            print(f"  {tag} {rel:72s} exists={exists}")

print("\n== 7. 既有产出/原件 0 回改 (跑后复测) ==")
for rel, want in (("deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py", "7c095c54fb99"),
                  ("deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py", "de16bc002198"),
                  ("deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py", "041525fd05a2"),
                  ("results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json", "95f3f0957be8"),
                  ("results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json", "33ad1c01f745"),
                  ("corpus/v20/index_v3_2026_10_09.json", "74b27393574f"),
                  ("corpus/v20/index_v3_2026_09_29.json", "3ba2449cf986"),
                  ("results/_criterion_application_scope_prereg_2026_10_01.md", "c4e3338619c6"),
                  ("results/_exp06_selfverified_runner_fix_note_2026_10_10.md", "247398b687e6")):
    p = BASE / rel
    got = sha12(p) if p.exists() else "MISSING"
    print(f"  {'OK ' if got == want else '!! '}{rel:74s} {got} (want {want})")

print("\n== 8. 既有 PINNED 面逐项在盘/哈希 (静态核对; 0 运行) ==")
src = SRC.read_bytes().decode("utf-8")
ns = {}
exec(compile(ast.Module(body=[n for n in ast.parse(src).body
                             if isinstance(n, ast.Assign)
                             and getattr(n.targets[0], "id", "") == "PINNED"],
                      type_ignores=[]), "<pin>", "exec"), ns)
for rel, want in ns["PINNED"].items():
    p = BASE / rel
    got = sha12(p) if p.exists() else "MISSING"
    print(f"  {'OK ' if got == want else '!! '}{rel:74s} {got} (want {want})")

print("\n== 9. 两副本自身 PINNED 面 (含本棒新增 pin) 逐项在盘/哈希 ==")
for p, tag in ((FIX, "①"), (REN, "②")):
    tree = ast.parse(p.read_bytes().decode("utf-8"))
    d = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "PINNED":
            d = ast.literal_eval(n.value)
    print(f"  {tag} PINNED 共 {len(d)} 项")
    for rel, want in d.items():
        f = BASE / rel
        got = sha12(f) if f.exists() else "MISSING"
        print(f"    {'OK ' if got == want else '!! '}{rel:70s} {got} (want {want})")

print("\n== 10. 键名出现分布 (② 应 0 处旧键赋值/双写) ==")
for p, tag in ((FIX, "①"), (REN, "②")):
    t = p.read_bytes().decode("utf-8")
    lines = t.split("\n")
    code = [i + 1 for i, ln in enumerate(lines)
            if KEY_OLD in ln and not ln.lstrip().startswith("#")]
    doc = [i + 1 for i, ln in enumerate(lines) if KEY_OLD in ln and ln.lstrip().startswith("#")]
    print(f"  {tag} {KEY_OLD}: 非注释行 {len(code)} 处 {code[:12]} | 注释/头块行 {len(doc)} 处")
