# -*- coding: utf-8 -*-
"""轴二实跑之末项: v1.1 面内「命中而序列不变」件之普查 (0 反推, 只报实测)。"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"
spec = importlib.util.spec_from_file_location("exec_v3", RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)
KW3, PAT = ex.KEYWORDS_V3, ex.PHRASE_PATTERNS_V3
NEW = {"CRITERIA": ["复核","质量","保证","对齐","失实"],
       "RISK": ["回退","遗忘","记忆效应","噪声","缺陷","观察者效应"],
       "KILL_LINE": ["推翻","检验"], "TIMING": ["挂起","后面"]}
KW31 = {k: tuple(v) for k, v in KW3.items()}
for L, ws in NEW.items():
    KW31[L] = tuple(KW31[L]) + tuple(ws)

def seq_of(r, kw):
    if not r or not r.strip():
        return []
    e = []
    for jt, kws in kw.items():
        p = -1
        for k in kws:
            i = r.find(k)
            if i >= 0 and (p < 0 or i < p):
                p = i
        if p >= 0:
            e.append((p, jt))
    e.sort(key=lambda x: x[0])
    s, seen = [], set()
    for _, jt in e:
        if jt not in seen:
            seen.add(jt); s.append(jt)
    for p in PAT:
        if p["pattern"] in r:
            for jt in p["target_seq"]:
                if jt not in seen:
                    seen.add(jt); s.append(jt)
    return s

v11 = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))
hit_but_unchanged, unchanged, displaced, per_word = [], 0, 0, {}
for ev in v11["events"]:
    t = ev.get("reasoning_full", "") or ""
    a, b = seq_of(t, KW3), seq_of(t, KW31)
    hits = []
    for L, ws in NEW.items():
        for w in ws:
            if w in t:
                hits.append({"word": w, "layer": L, "char_pos": t.find(w)})
                per_word.setdefault(w, []).append(ev.get("q_id"))
    if a != b:
        displaced += 1
    else:
        unchanged += 1
        if hits:
            hit_but_unchanged.append({"q_id": ev.get("q_id"), "seq": a, "hits": hits,
                                      "reason": "新词所在层已由更早位置命中词在序列内 -> dedup 吸收"})
    for h in hits:
        per_word[h["word"]].append(ev.get("q_id"))

sys.stdout.write(json.dumps({
    "v11_rows": len(v11["events"]), "n_displaced": displaced, "n_unchanged": unchanged,
    "n_hit_but_unchanged": len(hit_but_unchanged),
    "hit_but_unchanged_items": hit_but_unchanged,
    "new_word_hit_map_v11": per_word,
}, ensure_ascii=False, indent=1))
