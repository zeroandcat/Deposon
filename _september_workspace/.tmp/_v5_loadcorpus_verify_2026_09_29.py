# -*- coding: utf-8 -*-
"""P-6 修加载器验证脚本（worker, 2026-09-29）。

只读验证，不写 corpus/ 与不动原件：
  ① 修前复现：原件 mindmap_corpus_v20.load_corpus 对 corpus/v20 抛 RuntimeError（3 件误判）
  ② 修后通过：修订件 mindmap_corpus_v20_r1.load_corpus 同一目录不抛
  ③ 真孤儿反例：临时目录内塞 1 件真图记录（未入册）⇒ 修订件仍抛（防放宽过度）
     ③b 不可解析 .json ⇒ 修订件仍抛
     ③c 非图记录冒充（graph_id 齐备但无 edges/family/N）⇒ 修订件不抛
  ④ ast.parse 双件语法通过
  ⑤ 原件/语料跑前跑后 sha256[:12] 复验 0 触动
"""
import ast
import hashlib
import json
import os
import shutil
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(REPO, "corpus", "v20")
ORIG = os.path.join(REPO, "mindmap_corpus_v20.py")
REV = os.path.join(REPO, "mindmap_corpus_v20_r1.py")

# ── 2026-09-29 追加（protocol-keeper · PI 确认批 5 ⑱③ 授权修正）─────────────────
# 事实：修订件 mindmap_corpus_v20_r1.py 已由 parent 按**可恢复删除通道**清除
#       （回执 `mavis-trash: moved to trash`；删除前实测 SHA-12 `e77e7f3455e0` / 25,791 B）。
# 本脚本硬编该路径作「修后腿」⇒ **0 静默改指原件**：改指会使「修后腿」退化为与原件
# 自比较，等于把自比较伪装成「修后通过」＝ 制造误导。故改为**显式失效 ＋ 出处可追**。
# 落册：results/_v5_confirm_b5_decisions_register_2026_09_29.md §（⑱③）
# ──────────────────────────────────────────────────────────────────────────────
if not os.path.exists(REV):
    raise SystemExit(
        "[HISTORICAL / 0-RUNNABLE] 本脚本的「修后腿」依赖已删除的修订件：%s\n"
        "  该件已于 2026-09-29 经可恢复删除通道清除（0 永久删除，可自回收站复原）。\n"
        "  本脚本**0 改指原件**：自比较会伪装成「修后通过」⇒ 属误导面。\n"
        "  如需复验修后侧：请直接用已含该修复的原件 mindmap_corpus_v20.py 另立新名验证脚本。\n"
        "  落册出处：results/_v5_confirm_b5_decisions_register_2026_09_29.md（⑱③）" % REV
    )

NON_GRAPH_3 = ["all.json", "index_v2_2026_09_16.json", "strip_captions_22.json"]


def sha12(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def corpus_digest():
    """语料目录全量 sha256[:12]（0 触动复验用）。"""
    h = hashlib.sha256()
    for fn in sorted(os.listdir(CORPUS)):
        fp = os.path.join(CORPUS, fn)
        if not os.path.isfile(fp):
            continue
        h.update(fn.encode("utf-8"))
        with open(fp, "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:12]


def load_mod(name, path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    out = {}
    pre_corpus = corpus_digest()
    pre_orig = sha12(ORIG)
    out["pre"] = {"orig_sha12": pre_orig, "corpus_digest12": pre_corpus,
                  "orig_bytes": os.path.getsize(ORIG)}

    # ④ 语法
    for label, path in (("orig", ORIG), ("rev", REV)):
        with open(path, encoding="utf-8") as f:
            ast.parse(f.read(), filename=path)
        out.setdefault("ast_parse", {})[label] = "PASS"

    orig = load_mod("m_orig", ORIG)
    rev = load_mod("m_rev", REV)

    # ① 修前复现（原件对真语料目录）
    try:
        orig.load_corpus(CORPUS, families=("S",))
        out["pre_fix_repro"] = {"raised": False, "verdict": "FAIL_NO_REPRO"}
    except RuntimeError as e:
        msg = str(e)
        hit = [n for n in NON_GRAPH_3 if n in msg]
        out["pre_fix_repro"] = {"raised": True, "exc": "RuntimeError",
                                "n_non_graph_in_msg": len(hit),
                                "names": hit, "verdict": "PASS" if len(hit) == 3 else "PARTIAL"}

    # ② 修后通过（修订件对真语料目录，0 写）
    try:
        graphs = rev.load_corpus(CORPUS, families=("S",))
        out["post_fix"] = {"raised": False, "n_graphs_S": len(graphs),
                           "verdict": "PASS" if len(graphs) == 16 else "FAIL_COUNT"}
    except RuntimeError as e:
        out["post_fix"] = {"raised": True, "msg": str(e), "verdict": "FAIL_STILL_RAISES"}

    # ③ 反例：全部在临时目录做，真语料 0 写
    with tempfile.TemporaryDirectory() as td:
        cp = os.path.join(td, "v20")
        shutil.copytree(CORPUS, cp)

        # ③a 真孤儿：一件真图记录副本改名后未入册
        with open(os.path.join(cp, "S1.json"), encoding="utf-8") as f:
            g = json.load(f)
        g["graph_id"] = "S_true_orphan_probe"
        with open(os.path.join(cp, "S_true_orphan_probe.json"), "w", encoding="utf-8") as f:
            json.dump(g, f, ensure_ascii=False, indent=1)
        try:
            rev.load_corpus(cp, families=("S",))
            out["true_orphan"] = {"raised": False, "verdict": "FAIL_SENTINEL_LOOSENED"}
        except RuntimeError as e:
            msg = str(e)
            out["true_orphan"] = {"raised": True,
                                  "names_probe": "S_true_orphan_probe.json" in msg,
                                  "non_graph_absent": not any(n in msg for n in NON_GRAPH_3),
                                  "verdict": "PASS" if ("S_true_orphan_probe.json" in msg
                                                        and not any(n in msg for n in NON_GRAPH_3))
                                            else "FAIL_MSG"}
        os.remove(os.path.join(cp, "S_true_orphan_probe.json"))

        # ③b 不可解析 .json
        with open(os.path.join(cp, "_broken_probe.json"), "w", encoding="utf-8") as f:
            f.write("{not json")
        try:
            rev.load_corpus(cp, families=("S",))
            out["unparsable"] = {"raised": False, "verdict": "FAIL_SILENTLY_IGNORED"}
        except RuntimeError as e:
            out["unparsable"] = {"raised": True,
                                 "mentions": "_broken_probe.json" in str(e),
                                 "verdict": "PASS" if "_broken_probe.json" in str(e) else "FAIL_MSG"}
        os.remove(os.path.join(cp, "_broken_probe.json"))

        # ③c 半个核心键（graph_id 有、edges/family/N 缺）⇒ 判非图记录，不抛
        with open(os.path.join(cp, "half_record_probe.json"), "w", encoding="utf-8") as f:
            json.dump({"graph_id": "half", "nodes": [0, 1]}, f, ensure_ascii=False)
        try:
            n = len(rev.load_corpus(cp, families=("S",)))
            out["half_record"] = {"raised": False, "n_graphs_S": n, "verdict": "PASS"}
        except RuntimeError as e:
            out["half_record"] = {"raised": True, "msg": str(e), "verdict": "FAIL"}
        os.remove(os.path.join(cp, "half_record_probe.json"))

        # ③d 无非图记录对照：删掉 3 件非图记录后原件应当通过（反证误判源）
        for n_ in NON_GRAPH_3:
            os.remove(os.path.join(cp, n_))
        try:
            n = len(orig.load_corpus(cp, families=("S",)))
            out["orig_without_3"] = {"raised": False, "n_graphs_S": n,
                                     "verdict": "PASS" if n == 16 else "FAIL_COUNT"}
        except RuntimeError as e:
            out["orig_without_3"] = {"raised": True, "msg": str(e), "verdict": "FAIL"}

    # ⑤ 0 触动复验
    post_corpus = corpus_digest()
    post_orig = sha12(ORIG)
    out["post"] = {"orig_sha12": post_orig, "corpus_digest12": post_corpus,
                   "orig_bytes": os.path.getsize(ORIG)}
    out["zero_touch"] = {
        "orig_untouched": pre_orig == post_orig,
        "corpus_untouched": pre_corpus == post_corpus,
        "rev_sha12": sha12(REV), "rev_bytes": os.path.getsize(REV),
    }

    print(json.dumps(out, ensure_ascii=False, indent=1))
    ok = (out["pre_fix_repro"]["verdict"] == "PASS"
          and out["post_fix"]["verdict"] == "PASS"
          and out["true_orphan"]["verdict"] == "PASS"
          and out["unparsable"]["verdict"] == "PASS"
          and out["half_record"]["verdict"] == "PASS"
          and out["orig_without_3"]["verdict"] == "PASS"
          and out["zero_touch"]["orig_untouched"]
          and out["zero_touch"]["corpus_untouched"])
    print("OVERALL:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
