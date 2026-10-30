"""P-6 切换落地：6 项验证（新名件，落 .tmp，可复跑）。

① 修前抛错复现  ② 修后通过（族 S=16 图）  ③ 真孤儿反例仍抛
④ ast.parse     ⑤ 下游冒烟（3 个 import 方）  ⑥ r1 件与原件修后等价性

反例一律在 tempfile 临时目录内构造（真语料 0 写）。0 LLM / 0 网络 / 0 key。
"""
import ast
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
FIXED = os.path.join(ROOT, "mindmap_corpus_v20.py")
R1 = os.path.join(ROOT, "mindmap_corpus_v20_r1.py")
BACKUP = os.path.join(ROOT, ".tmp/_v5_loadcorpus_switch_2026_09_29",
                      "mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak")
# .bak 后缀不可 import -> 沙箱内复制为 .py 供「修前」侧加载（字节相同）
OLD_PY = os.path.join(os.path.dirname(BACKUP), "_old_corpus_view.py")

# ── 2026-09-29 追加（protocol-keeper · PI 确认批 5 ⑱③ 授权修正）─────────────────
# 事实：修订件 mindmap_corpus_v20_r1.py 已由 parent 按**可恢复删除通道**清除
#       （回执 `mavis-trash: moved to trash`；删除前实测 SHA-12 `e77e7f3455e0` / 25,791 B）。
# 本脚本 L58 逐件哈希含 r1、L155 做「r1 == 修后原件」字节比对 ⇒ 该腿已 0 对象。
# **0 静默改指原件**：改指后第 ⑥ 项退化为自比较，等于伪造「等价性 PASS」＝ 误导面。
# 改为**显式失效 ＋ 出处可追**；原件侧的 ①②③④⑤ 项在本脚本内**一并冻结**（避免只跑半套
# 而被误读为「修后侧已验」）。
# 落册：results/_v5_confirm_b5_decisions_register_2026_09_29.md（⑱③）
# ──────────────────────────────────────────────────────────────────────────────
if not os.path.exists(R1):
    raise SystemExit(
        "[HISTORICAL / 0-RUNNABLE] 本脚本第 ⑥ 项依赖已删除的修订件：%s\n"
        "  该件已于 2026-09-29 经可恢复删除通道清除（0 永久删除，可自回收站复原）。\n"
        "  本脚本**0 改指原件**：第 ⑥ 项将退化为原件自比较，等于伪造「等价性 PASS」。\n"
        "  如需复跑「修后侧」验证：请另立新名脚本，直接以已含该修复的原件为被验对象。\n"
        "  落册出处：results/_v5_confirm_b5_decisions_register_2026_09_29.md（⑱③）" % R1
    )
if not os.path.exists(OLD_PY):
    shutil.copy2(BACKUP, OLD_PY)
assert open(OLD_PY, "rb").read() == open(BACKUP, "rb").read()
RESULTS = []


def rec(name, ok, detail):
    RESULTS.append((name, ok, detail))
    print("[%s] %-28s %s" % ("PASS" if ok else "FAIL", name, detail))


def sha12(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]


def load_mod(path, name):
    # 显式 utf-8 读源码再 exec：绕开 importlib 按本机 locale(GBK) 解码的坑，
    # 否则 check.py 这类无 coding 声明的件会假失败。
    src = open(path, encoding="utf-8").read()
    mod = type(sys)(name)
    mod.__file__ = path
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(src, path, "exec"), mod.__dict__)
    return mod


def main():
    print("fixed sha12 = %s" % sha12(FIXED))

    # ---- ④ ast.parse（先跑，作为后续项的前置） ----
    for label, p in (("fixed", FIXED), ("r1", R1), ("backup_old", OLD_PY)):
        try:
            ast.parse(open(p, encoding="utf-8").read())
            rec("ast.parse:%s" % label, True, "parse ok")
        except SyntaxError as e:
            rec("ast.parse:%s" % label, False, str(e))

    # ---- ① 修前抛错复现（用备份原件 = 修前内容） ----
    # 旧件副本在 .tmp 下，HERE 相对路径解析不到 corpus/ -> 显式传同一真语料目录，
    # 保证「修前 vs 修后」比的是哨兵判据本身，0 掺路径变量。
    old = load_mod(OLD_PY, "corpus_old")
    new = load_mod(FIXED, "corpus_new")
    REAL_CORPUS = new.CORPUS_DIR
    try:
        old.load_corpus(REAL_CORPUS)
        rec("① 修前抛错复现", False, "未抛错（与登记件不符）")
    except RuntimeError as e:
        msg = str(e)
        hit = [n for n in ("all.json", "index_v2_2026_09_16.json",
                           "strip_captions_22.json") if n in msg]
        rec("① 修前抛错复现", len(hit) == 3,
            "RuntimeError，3 件非图记录命中 %d/3" % len(hit))

    # ---- ② 修后通过 ----
    try:
        g = new.load_corpus()
        rec("② 修后通过 S=16", len(g) == 16, "n_graphs_S=%d" % len(g))
    except Exception as e:
        rec("② 修后通过 S=16", False, "%s: %s" % (type(e).__name__, e))

    # ---- ③ 真孤儿反例 + ③b 不可解析 + ③c 半个核心键 ----
    with tempfile.TemporaryDirectory() as td:
        work = os.path.join(td, "corpus")
        shutil.copytree(new.CORPUS_DIR, work)

        with open(os.path.join(work, "S_true_orphan_probe.json"), "w",
                  encoding="utf-8") as f:
            json.dump({"graph_id": "S_true_orphan_probe", "family": "S",
                       "N": 3, "edges": [[0, 1], [0, 2]]}, f)
        try:
            new.load_corpus(work)
            rec("③ 真孤儿反例仍抛", False, "未抛错")
        except RuntimeError as e:
            m = str(e)
            clean = all(n not in m for n in ("all.json",
                                             "index_v2_2026_09_16.json",
                                             "strip_captions_22.json"))
            rec("③ 真孤儿反例仍抛",
                "S_true_orphan_probe.json" in m and clean,
                "点名真孤儿=%s，非图记录未混入=%s"
                % ("S_true_orphan_probe.json" in m, clean))

        os.remove(os.path.join(work, "S_true_orphan_probe.json"))
        with open(os.path.join(work, "_broken_probe.json"), "w",
                  encoding="utf-8") as f:
            f.write("{not json")
        try:
            new.load_corpus(work)
            rec("③b 不可解析仍抛", False, "未抛错")
        except RuntimeError as e:
            rec("③b 不可解析仍抛", "_broken_probe.json" in str(e),
                "点名 _broken_probe.json")

        os.remove(os.path.join(work, "_broken_probe.json"))
        with open(os.path.join(work, "_half_probe.json"), "w",
                  encoding="utf-8") as f:
            json.dump({"graph_id": "_half_probe", "caption": "x"}, f)
        try:
            g = new.load_corpus(work)
            rec("③c 半个核心键不抛", len(g) == 16, "n_graphs_S=%d" % len(g))
        except RuntimeError as e:
            rec("③c 半个核心键不抛", False, str(e)[:80])

        # 族 L / 混合面
        for fams, exp in ((("L",), 6), (("S", "L"), 22)):
            g = new.load_corpus(work, families=fams)
            rec("族面 families=%s" % (fams,), len(g) == exp,
                "n=%d (期望 %d)" % (len(g), exp))

        # 功能等价：原件（移走 3 件非图记录）vs 修后原件
        eqdir = os.path.join(td, "corpus_clean")
        shutil.copytree(new.CORPUS_DIR, eqdir)
        for n in ("all.json", "index_v2_2026_09_16.json",
                  "strip_captions_22.json"):
            p = os.path.join(eqdir, n)
            if os.path.exists(p):
                os.remove(p)
        a = old.load_corpus(eqdir)
        b = new.load_corpus(eqdir)
        ha = hashlib.sha256(json.dumps(a, sort_keys=True,
                                       ensure_ascii=False).encode()).hexdigest()[:12]
        hb = hashlib.sha256(json.dumps(b, sort_keys=True,
                                       ensure_ascii=False).encode()).hexdigest()[:12]
        rec("功能等价 orig-clean vs fixed", a == b and ha == hb,
            "n=%d/%d sha=%s/%s" % (len(a), len(b), ha, hb))

    # ---- ⑥ r1 与修后原件等价 ----
    same = open(FIXED, "rb").read() == open(R1, "rb").read()
    rec("⑥ r1 == 修后原件", same,
        "byte-identical=%s sha12=%s" % (same, sha12(FIXED)))

    # ---- ⑤ 下游冒烟 ----
    # 候选：模块化 import 方（可 import）。verifier/v21/check.py 是**顶层副作用
    # 脚本**（非 importable 模块：import 即读 results/ 跑 pytest），
    # 且其唯一涉及本件的断言是 line52 文本包含检查，另行直测（见下）。
    cands = ["run_v20_baselines.py", "run_v20_bigquiz_eval.py",
             "run_v20_familyL_ingest.py"]
    downstream = [c for c in cands if os.path.exists(os.path.join(ROOT, c))]
    extra = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in {".git", "__pycache__", "node_modules",
                                    ".tmp", ".scratch_gamma_r1", "corpus"}]
        for fn in filenames:
            if fn.startswith("run_v20_") and fn.endswith(".py"):
                extra.append(os.path.relpath(os.path.join(dirpath, fn), ROOT)
                             .replace(os.sep, "/"))
    picks = list(dict.fromkeys(downstream + sorted(set(extra))))[:3]
    for rel in picks:
        p = os.path.join(ROOT, rel)
        try:
            m = load_mod(p, "smoke_" + os.path.basename(rel)[:-3])
            has = [n for n in ("load_corpus", "corpus_plan", "CORPUS_DIR",
                              "build_index", "generate_graph") if hasattr(m, n)]
            called = ""
            if callable(getattr(m, "load_corpus", None)):
                n = len(m.load_corpus())
                called = ", load_corpus()=%d 图" % n
            # 判据：import 不抛错 + 至少命中 1 个本模块符号 + 若持有 load_corpus
            # 则实调返回族 S 16 图（摄入侧件不持 load_corpus，不强求）。
            ok = bool(has) and (("load_corpus" not in has) or "=16 图" in called)
            rec("⑤ 冒烟 %s" % os.path.basename(rel), ok,
                "import ok, 命中符号=%s%s" % (has, called))
        except Exception as e:
            rec("⑤ 冒烟 %s" % os.path.basename(rel), False,
                "%s: %s" % (type(e).__name__, str(e)[:90]))

    # check.py 对本件的唯一断言（line52 文本包含）——修前/修后均须成立
    v21 = os.path.join(ROOT, "verifier/v21/check.py")
    if os.path.exists(v21):
        old_txt = open(OLD_PY, encoding="utf-8").read()
        new_txt = open(FIXED, encoding="utf-8").read()
        rec("⑤ check.py 断言(孤儿哨兵在案)",
            ("corpus orphan graphs" in old_txt) and
            ("corpus orphan graphs" in new_txt),
            "check.py:52 文本包含，修前修后均成立")

    npass = sum(1 for _, ok, _ in RESULTS if ok)
    print("\n== %d/%d PASS ==" % (npass, len(RESULTS)))
    fails = [r[0] for r in RESULTS if not r[1]]
    if fails:
        print("FAILED: %s" % fails)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
