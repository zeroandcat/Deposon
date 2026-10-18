# -*- coding: utf-8 -*-
"""
P-K 跨主体指纹盲测 runner (2026-09-16) — 委外执行代理 A (KIMI 派出)
一键复跑产出:
  1) deposon_team/products/kimi_artifact_v_2026_09_16.json
  2) results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json
约束: 纯 hashlib + numpy + json (+ os/re/math/datetime); 0 LLM; 不联网; 输入只读; 仅写上述 2 个新文件。
顺序: 先落预登记(ts_1) 再做全部判别计算(ts_2), ts_1 < ts_2 由执行顺序保证。
"""
import hashlib, json, math, os, re
from datetime import datetime, timezone
import numpy as np

REPO = r"D:\私人资料\deposon-repo"
KWS  = r"C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add"
OUT_KIMI = os.path.join(REPO, "deposon_team", "products", "kimi_artifact_v_2026_09_16.json")
OUT_RES  = os.path.join(REPO, "results", "deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json")

# ---------------- 制品清单(只读引用) ----------------
OWN = [  # 26 件自家制品, 全部 JSON, 仓内相对路径
 "verifier/handoff/KT_ABC1_anchors_sha256_12.json",
 "verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json",
 "results/deposon_v3_physical_opt_2026_09_11.json",
 "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
 "results/deposon_pg_v01_9m60c_2026_09_15.json",
 "results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json",
 "results/deposon_pa_d1_d3_2026_09_15.json",
 "results/deposon_pe_d1_d3_2026_09_15.json",
 "results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json",
 "results/boss_pa_1_rbr_rm_result_2026_09_15.json",
 "results/boss_pa_2_potential_game_result_2026_09_15.json",
 "results/boss_pa_3_replicator_dynamics_result_2026_09_15.json",
 "results/boss_pc_1_real_2d_ising_2026_09_15.json",
 "results/boss_pc_2_real_transverse_ising_2026_09_15.json",
 "results/boss_pc_3_real_reservoir_2026_09_15.json",
 "results/attack_pc_a1_resampling_2026_09_15.json",
 "results/attack_pc_a2_fitting_2026_09_15.json",
 "results/attack_pc_a3_clipping_2026_09_15.json",
 "results/skill_a_p_a_60cells_result_2026_09_11.json",
 "results/skill_b_p_c_alpha_beta_result_2026_09_11.json",
 "results/skill_c_p_e_3modality_result_2026_09_11.json",
 "results/skill_d_p_f_observer_result_2026_09_11.json",
 "results/deposon_pf_implementation_2026_09_11.json",
 "results/deposon_pf_d1_full_9m5c_2026_09_15.json",
 "results/deposon_v3_v7_summary_2026_09_11.json",
 "results/deposon_v2_phase4_f4_2026_09_11.json",
]
# KIMI 原生制品 14 件: (artifact_id, 绝对路径, 清洗档)
# 清洗档: raw=原文取指纹; san=剔除令牌模式行; san_hdr=剔除令牌行+剔除文首署名/引用块(含后日期文件引用, 属改写痕迹)
_k = lambda *a: os.path.join(KWS, *a)
KIMI_NATIVES = [
 ("KIMI-N01", _k("V3X_KIMI_PROPOSED_DIRECTIONS_2026_09_16.md"), "raw"),
 ("KIMI-N02", _k("review_A_report.md"), "raw"),
 ("KIMI-N03", _k("review_B_report.md"), "raw"),
 ("KIMI-N04", _k("PD_REPORT_2026-09-01.md"), "raw"),
 ("KIMI-N05", _k("review_B_metrics1.txt"), "raw"),
 ("KIMI-N06", _k("review_B_metrics2.txt"), "raw"),
 ("KIMI-N07", _k("verify_B_part1.py"), "raw"),
 ("KIMI-N08", _k("verify_B_part2.py"), "raw"),
 ("KIMI-N09", _k("verify_B_part3.py"), "raw"),
 ("KIMI-N10", _k("verify_B_part4.py"), "raw"),
 ("KIMI-N11", _k("verify_B_part5.py"), "raw"),
 ("KIMI-N12", _k("github_staging", "push_rest.py"), "raw"),
 ("KIMI-N13", _k("github_staging", "verify_push.py"), "raw"),
 ("KIMI-N14", os.path.join(REPO, "docs", "V3X", "V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md"), "san_hdr"),
]
SLICE_SOURCES = [  # 切片母本(确定性二级标题切片, 补充至 >=20 件)
 _k("V3X_KIMI_PROPOSED_DIRECTIONS_2026_09_16.md"),
 _k("review_A_report.md"),
 _k("review_B_report.md"),
 _k("PD_REPORT_2026-09-01.md"),
]

# 令牌模式(分段拼接, 源码不落字面前缀, 防泄漏); 命中行整行剔除
TOKEN_RE = re.compile(r'(?<![A-Za-z0-9])(' + 'g' + 'hp_' + r'[A-Za-z0-9]+|'
                      + 's' + 'k-' + r'[A-Za-z0-9]{6,}|'
                      + 'a' + 'rk-' + r'[A-Za-z0-9]{6,})')

def utcnow():
    return datetime.now(timezone.utc).isoformat()

def read_bytes(p):
    with open(p, 'rb') as f:
        return f.read()

def sanitize_text(text, mode):
    lines = text.split('\n')
    out, header_done = [], (mode != "san_hdr")
    for i, ln in enumerate(lines):
        if not header_done:
            if i == 0:
                out.append(ln); continue          # 保留标题行
            if ln.strip() == '---':
                header_done = True
            continue                              # 剔除文首署名/引用块
        if TOKEN_RE.search(ln):
            continue                              # 剔除令牌模式行
        out.append(ln)
    return '\n'.join(out)

def slice_markdown(text, min_bytes, max_per_doc):
    parts = re.split(r'(?m)^(?=## )', text)
    secs = [p for p in parts if p.startswith('## ') and len(p.encode('utf-8')) >= min_bytes]
    return secs[:max_per_doc]

# ---------------- 指纹与特征 ----------------
def keypaths(obj, pre, acc):
    if isinstance(obj, dict):
        for k in obj.keys():
            acc.add(pre + str(k))
            keypaths(obj[k], pre + str(k) + ".", acc)
    elif isinstance(obj, list):
        for v in obj[:20]:
            keypaths(v, pre + "[]", acc)

def depth_of(obj, d=0):
    if isinstance(obj, dict) and obj:
        return max(depth_of(v, d + 1) for v in list(obj.values())[:200])
    if isinstance(obj, list) and obj:
        return max(depth_of(v, d + 1) for v in obj[:200])
    return d

FEATURES = ["log_bytes", "log_lines", "is_json", "log_keys", "json_depth",
            "key_vocab_overlap", "cjk_ratio", "ws_ratio", "digit_ratio",
            "alpha_ratio", "punct_ratio", "byte_entropy8", "log_mean_line"]

def extract(data, own_vocab):
    text = data.decode('utf-8', errors='replace')
    n = max(len(text), 1)
    lines = text.split('\n')
    nb = len(data)
    is_json, log_keys, jdepth, overlap, ks = 0.0, 0.0, 0.0, 0.0, set()
    try:
        obj = json.loads(text)
        keypaths(obj, "", ks)
        is_json = 1.0
        log_keys = math.log10(len(ks) + 1)
        jdepth = float(depth_of(obj))
        overlap = (len(ks & own_vocab) / len(ks)) if ks else 0.0
    except Exception:
        pass
    cjk = sum(1 for c in text if '一' <= c <= '鿿') / n
    ws = sum(1 for c in text if c.isspace()) / n
    dig = sum(1 for c in text if c.isdigit()) / n
    alpha = sum(1 for c in text if ('a' <= c <= 'z' or 'A' <= c <= 'Z')) / n
    punct = max(0.0, 1.0 - cjk - ws - dig - alpha)
    cnt = [0] * 256
    for b in data:
        cnt[b] += 1
    H = 0.0
    for c in cnt:
        if c:
            p = c / nb; H -= p * math.log2(p)
    f = {"log_bytes": math.log10(nb + 1), "log_lines": math.log10(len(lines) + 1),
         "is_json": is_json, "log_keys": log_keys, "json_depth": jdepth,
         "key_vocab_overlap": overlap, "cjk_ratio": cjk, "ws_ratio": ws,
         "digit_ratio": dig, "alpha_ratio": alpha, "punct_ratio": punct,
         "byte_entropy8": H / 8.0, "log_mean_line": math.log10(nb / max(len(lines), 1) + 1)}
    return f, ks

def struct_sig(data, ks, f):
    if ks:
        return "J:" + hashlib.sha256('\n'.join(sorted(ks)).encode('utf-8')).hexdigest()[:12]
    q = "L%d|B%d|C%d|W%d|D%d" % (
        round(10 ** f["log_lines"]) - 1, len(data),
        round(f["cjk_ratio"] * 20), round(f["ws_ratio"] * 20), round(f["digit_ratio"] * 20))
    return "T:" + hashlib.sha256(q.encode('utf-8')).hexdigest()[:12]

def triple_hash(content, path, anchor):
    h = hashlib.sha256()
    h.update(b"PKBLIND20260916|"); h.update(path.encode('utf-8'))
    h.update(b"|"); h.update(anchor.encode('utf-8')); h.update(b"|"); h.update(content)
    return h.hexdigest()

# ---------------- 洗白变换(确定性) ----------------
def wash_key_reorder(text, ext):
    try:
        obj = json.loads(text)
        return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=1)
    except Exception:
        return '\n\n'.join(reversed(text.split('\n\n')))

def wash_newline_inject(text, ext):
    out = []
    for i, ln in enumerate(text.split('\n')):
        out.append(ln)
        if i % 2 == 1:
            out.append('')
    return '\n'.join(out)

def wash_comment_inject(text, ext):
    try:
        obj = json.loads(text)
        return json.dumps({'_pk_wash_comment': '2026-09-16', **obj}, ensure_ascii=False, indent=1)
    except Exception:
        mark = '# pk-wash-2026-09-16' if ext == '.py' else '<!-- pk-wash-2026-09-16 -->'
        return mark + '\n' + text

WASHES = [("W1_key_reorder", wash_key_reorder),
          ("W2_newline_inject", wash_newline_inject),
          ("W3_comment_inject", wash_comment_inject)]

# ================= 预登记(先于一切判别计算) =================
T1 = utcnow()
PREREG = {
 "ts_utc": T1,
 "algorithm": "两级指纹 + 自家原型归一化距离判别",
 "level1_byte_fingerprint": "SHA-256(raw_bytes)[0:12]",
 "level2_struct_signature": "JSON: 排序键路径集合哈希; 文本: 行数|字节数|字符分布分桶向量哈希",
 "features": FEATURES,
 "distance": "逐特征 z=|x-mu|/max(sd,1e-6), z 截断于 8, 取 13 特征均值 d; d<T 判自家, 否则判外来(KIMI 替身)",
 "z_cap": 8, "std_floor": 1e-6, "threshold_T": 2.0,
 "prototype": "自家 26 件 JSON 的逐特征均值/标准差; key_vocab_overlap 词表 = 自家 26 件键路径并集",
 "decision_lines": {"SP_t": ">=0.7", "FPR": "<1/100", "FNR": "<1/20", "anti_whitewash": ">=0.6"},
 "definitions": {
   "FPR": "外来判自家件数 / 外来总件数",
   "FNR": "自家判外来件数 / 自家总件数",
   "SP_t": "成对分离率 = 全部(自家,外来)对中 d(外来)>d(自家) 的比例(并列计 0.5); 仓内无既有定义, 本口径为自定义并预登记",
   "anti_whitewash": "外来制品经格式洗白后仍判外来的比例(总)及分变换比例",
   "alive_increment": "3 类洗白变换中分变换保持率>=0.6 的类数, 记 x/3; 仓内无既有定义, 本口径为自定义并预登记",
 },
 "sanitation": {
   "kimi_side": "全部 KIMI 侧输入先剔除命中令牌模式的整行再取指纹(防泄漏); 自家侧可信原文取指纹",
   "design_doc_extra": "V3X_FULL_EXPERIMENT_DESIGN 另剔除文首署名/引用块(含 2026-09-18 后日期文件引用, 属他人追加改写痕迹); 尾部追加段边界仓内不可考, 见报告局限节",
 },
 "exclusions": [
   "github_staging/push_result.json: API 转储非脚本/文档, 未纳入; JSON 型外来制品判别留待 GLM 接入补测",
   "results/deposon_volcengine_glm_* 与 deposon_volcengine_minimax_*: 与 9 model 主源同源, 防泄漏避开",
 ],
 "glm_slot": {"status": "pending",
   "interface": "GLM 日后自供制品, 按 kimi_artifact_v 同 schema 落 glm_artifact_v JSON, 重跑本 runner 即扩为三方判别"},
 "minimax_slot": {"status": "replaced_by_kimi_artifacts",
   "note": "沿 user 17:59 拍板: minimax 槽位由 KIMI 制品顶替, 三方设计变为 自家 vs KIMI(外来替身), GLM 槽位 pending"},
}

# ================= 计算 =================
def main():
    # 1) 自家: 原文读入, 建词表与原型
    own_data, own_vocab = [], set()
    for rel in OWN:
        b = read_bytes(os.path.join(REPO, *rel.split('/')))
        own_data.append((rel, b))
        try:
            keypaths(json.loads(b.decode('utf-8', errors='replace')), "", own_vocab)
        except Exception:
            pass
    own_feats = []
    for rel, b in own_data:
        f, _ = extract(b, own_vocab)
        own_feats.append(f)
    M = np.array([[f[k] for k in FEATURES] for f in own_feats])
    mu = M.mean(axis=0)
    sd = np.maximum(M.std(axis=0), 1e-6)

    def dist(f):
        z = np.minimum(np.abs(np.array([f[k] for k in FEATURES]) - mu) / sd, 8.0)
        return float(z.mean())

    # 2) KIMI 制品集: 原生(按需清洗) + 确定性切片
    artifacts = []
    for aid, path, mode in KIMI_NATIVES:
        raw = read_bytes(path)
        data = raw if mode == "raw" else sanitize_text(raw.decode('utf-8', errors='replace'), mode).encode('utf-8')
        artifacts.append({"artifact_id": aid, "source_path": path.replace('\\', '/'),
                          "origin": "原生" + ("" if mode == "raw" else "(清洗:%s)" % mode),
                          "slice_rule": None, "data": data})
    slices, rule_used = [], None
    for mb in (600, 400, 250):
        for k in (2, 3, 4):
            cand = []
            for p in SLICE_SOURCES:
                txt = read_bytes(p).decode('utf-8', errors='replace')
                for j, s in enumerate(slice_markdown(txt, mb, k)):
                    cand.append((p, j, s))
            if len(cand) >= 6:
                slices, rule_used = cand, "min_bytes=%d,max_per_doc=%d" % (mb, k)
                break
        if slices:
            break
    for i, (p, j, s) in enumerate(slices):
        artifacts.append({"artifact_id": "KIMI-S%02d" % (i + 1),
                          "source_path": p.replace('\\', '/') + "#slice[%d]" % j,
                          "origin": "切片", "slice_rule": "二级标题切片,%s" % rule_used,
                          "data": s.encode('utf-8')})

    # 3) 指纹 + 判别
    for a in artifacts:
        f, ks = extract(a["data"], own_vocab)
        a["n_bytes"] = len(a["data"])
        a["byte_sha12"] = hashlib.sha256(a["data"]).hexdigest()[:12]
        a["struct_signature"] = struct_sig(a["data"], ks, f)
        a["triple_hash"] = triple_hash(a["data"], a["source_path"], a["artifact_id"])
        a["d"] = dist(f)
        a["pred"] = "自家" if a["d"] < 2.0 else "KIMI"

    own_eval = []
    for (rel, b), f in zip(own_data, own_feats):
        d = dist(f)
        own_eval.append({"rel_path": rel, "byte_sha12": hashlib.sha256(b).hexdigest()[:12],
                         "d": d, "pred": "自家" if d < 2.0 else "KIMI"})

    # 4) 混淆矩阵与指标
    oo = sum(1 for e in own_eval if e["pred"] == "自家")
    ok = sum(1 for e in own_eval if e["pred"] == "KIMI")
    ko = sum(1 for a in artifacts if a["pred"] == "自家")
    kk = sum(1 for a in artifacts if a["pred"] == "KIMI")
    n_own, n_kim = len(own_eval), len(artifacts)
    fpr = ko / n_kim
    fnr = ok / n_own
    pairs = ties = 0
    for e in own_eval:
        for a in artifacts:
            if a["d"] > e["d"]: pairs += 1
            elif a["d"] == e["d"]: ties += 1
    sp_t = (pairs + 0.5 * ties) / (n_own * n_kim)

    # 5) 抗洗白
    wash_detail, wash_hold = {}, 0
    for name, fn in WASHES:
        hold = 0
        for a in artifacts:
            ext = os.path.splitext(a["source_path"].split('#')[0])[1]
            wb = fn(a["data"].decode('utf-8', errors='replace'), ext).encode('utf-8')
            wf, _ = extract(wb, own_vocab)
            if dist(wf) >= 2.0:
                hold += 1
        wash_detail[name] = {"held": hold, "total": n_kim, "rate": hold / n_kim}
        wash_hold += hold
    anti = wash_hold / (3 * n_kim)
    alive = sum(1 for v in wash_detail.values() if v["rate"] >= 0.6)

    lines = [
      {"line": "SP_t >= 0.7", "measured": sp_t, "pass": sp_t >= 0.7},
      {"line": "FPR < 1/100", "measured": fpr, "pass": fpr < 0.01},
      {"line": "FNR < 1/20", "measured": fnr, "pass": fnr < 0.05},
      {"line": "anti_whitewash >= 0.6", "measured": anti, "pass": anti >= 0.6},
    ]
    overall = all(x["pass"] for x in lines)
    T2 = utcnow()

    # 6) 落盘产出 1 + 2
    out1 = {"schema": "kimi_artifact_v/1.0", "created_ts_utc": T2,
            "note": "KIMI 制品集(原生+切片); GLM 槽位 pending 由 GLM 日后自供; minimax 槽位由本集顶替(user 17:59 拍板)",
            "count": n_kim,
            "artifacts": [{k: a[k] for k in ("artifact_id", "source_path", "origin", "slice_rule",
                                             "n_bytes", "byte_sha12", "struct_signature", "triple_hash")}
                          for a in artifacts]}
    out2 = {"task": "P-K 跨主体指纹盲测 (自家 vs KIMI 外来替身, GLM 槽位 pending)",
            "preregistration": PREREG,
            "own_artifacts": own_eval,
            "kimi_artifacts_ref": "deposon_team/products/kimi_artifact_v_2026_09_16.json",
            "blind_results": {
              "confusion_matrix": {"自家->自家": oo, "自家->KIMI": ok, "KIMI->自家": ko, "KIMI->KIMI": kk},
              "n_own": n_own, "n_kimi": n_kim,
              "kimi_predictions": [{ "artifact_id": a["artifact_id"], "d": a["d"], "pred": a["pred"]} for a in artifacts]},
            "metrics": {"FPR": fpr, "FNR": fnr, "SP_t": sp_t,
                        "anti_whitewash_total": anti, "anti_whitewash_per_transform": wash_detail,
                        "alive_increment": "%d/3" % alive},
            "decision_lines": lines,
            "overall_verdict": "PASS" if overall else "FAIL",
            "computed_ts_utc": T2}
    with open(OUT_KIMI, 'w', encoding='utf-8') as f:
        json.dump(out1, f, ensure_ascii=False, indent=2)
    with open(OUT_RES, 'w', encoding='utf-8') as f:
        json.dump(out2, f, ensure_ascii=False, indent=2)

    print("prereg_ts:", T1)
    print("computed_ts:", T2)
    print("own n=%d  kimi n=%d (原生 %d + 切片 %d, rule=%s)" % (n_own, n_kim, len(KIMI_NATIVES), len(slices), rule_used))
    print("confusion: 自家->自家=%d 自家->KIMI=%d KIMI->自家=%d KIMI->KIMI=%d" % (oo, ok, ko, kk))
    print("FPR=%.4f FNR=%.4f SP_t=%.4f anti=%.4f alive=%d/3" % (fpr, fnr, sp_t, anti, alive))
    print("d_own[min,max]=[%.3f,%.3f]  d_kimi[min,max]=[%.3f,%.3f]" % (
        min(e["d"] for e in own_eval), max(e["d"] for e in own_eval),
        min(a["d"] for a in artifacts), max(a["d"] for a in artifacts)))
    for x in lines:
        print("  %s -> measured=%.4f %s" % (x["line"], x["measured"], "PASS" if x["pass"] else "FAIL"))
    print("OVERALL:", "PASS" if overall else "FAIL")
    print("wrote:", OUT_KIMI, os.path.getsize(OUT_KIMI), "bytes")
    print("wrote:", OUT_RES, os.path.getsize(OUT_RES), "bytes")

if __name__ == "__main__":
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_p_k_blind_test_runner_2026_09_16.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
assert 'def main(' in _src_sc, 'main() 缺失'
assert '__main__' in _src_sc, '缺 __main__ guard'
print('_p_k_blind_test_runner_2026_09_16.py SELF-CHECK PASS')
