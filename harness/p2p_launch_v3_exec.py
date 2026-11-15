# -*- coding: utf-8 -*-
# P2' 发射（v7-2 冻结面·12 槽+盲化+差分表+两级兜底+双闸）·seed 20261115
# 主胞 A 对（flash↔max·前置 3 回合 smoke）→ KIMI 条件胞（M1 单换·form 10+3 smoke）
# 预算双闸：ES-2' 盒闸 <box> ＋ ES-2 全局等效闸 <cap>（P2 已耗 <spent> 扣除）先到先停
import sys, os, json, math, time, hashlib, requests
sys.path.insert(0, os.environ.get("HARNESS_LIB_PATH", "."))
import comp_t0t3_api as C

SEED = C.SEED; K_TURN = C.K_TURN
OUT = os.path.dirname(os.path.abspath(__file__))
M1_A, M2_A, M1_KIMI, M_RESCUE = "qwen3.7-flash", "qwen3.7-max", "kimi-k3.1-pro", "deepseek-v4-flash-free"
N_FORM, N_WD, N_DV, N_SW = 10, 4, 4, 8
BOX_BUDGET = int(os.environ.get("HARNESS_BOX", "0"))                       # ES-2' 盒闸
GLOBAL_BASELINE = int(os.environ.get("HARNESS_GLOBAL_BASELINE", "0"))                 # P2 四胞已耗（registry 链终值）
GLOBAL_CAP = int(os.environ.get("HARNESS_GLOBAL_GUARDRAIL", "0")) - GLOBAL_BASELINE    # ES-2 全局等效闸 = int(os.environ.get("HARNESS_全局等效闸", "0"))
BUDGET = min(BOX_BUDGET, GLOBAL_CAP)      # 先到先停（更紧者生效）
TIME_BUDGET_S = 20 * 60                   # ES-1 每链 ≤20min

mf = C.load_manifest()                    # manifest 恒等门（fail-loud）

# ---- v7-2 冻结面：盲化映射（与 P0' 认证件同源·冻结） ----
def gen_blind_kh(seed):
    fs = C.FrozenStream(seed, "v72|blindkh")
    pool = list(range(128)); out = []
    for _ in range(32): out.append(pool.pop(fs.next_int(len(pool))))
    return sorted(out)
BLIND_KH = gen_blind_kh(SEED); BLIND_SET = set(BLIND_KH)
BG_POOL = [k for k in range(128) if k not in BLIND_SET]
json.dump({"blind_kh": BLIND_KH, "seed": SEED, "frozen_at": "P2'-launch"},
          open(os.path.join(OUT, "p2p_blind_kh_frozen.json"), "w"), indent=1)

# ---- v7-2 三段差分表（G8' 预注册文本·发射时逐字节冻结落件） ----
CTX_P2P = {
  "form": "回合{round:02d}·日常维护会话（语境稳定）。任务：本回合 12 个编号槽·对每槽各执行一次候选键操作（写入或读取·12 项互不重复）。本会话按固定规程逐回合推进，请继续维护会话状态。",
  "wd":   "回合{round:02d}·日常维护会话（语境稳定）。任务：本回合 12 个编号槽·对每槽各执行一次候选键操作（写入或读取·12 项互不重复）。",
  "dv":   "回合{round:02d}·日常维护会话（语境稳定）。任务：本回合 12 个编号槽·对每槽各执行一次候选键操作（写入或读取·12 项互不重复）。",
}
CTX_P2P["dv"] = CTX_P2P["wd"]             # dv≡wd 逐字节（G8'·干预走 op 载荷）
INSTR = ("\n输出格式（严格单行 JSON·示例）：{{\"ops\":[{{\"op\":\"write\",\"slot\":42}},{{\"op\":\"read\",\"slot\":7}}]}}（共 12 项·slot 为 0–127 整数·互不重复）\n"
         "候选键（128 个·序号即 slot）：{cands}\n只回一行 JSON·不要输出其他内容。")

class P2PModel(C.ApiModel):
    def __init__(self, name, sysblock):
        super().__init__(name, sysblock)
        self.rescues = 0; self.invalid = 0; self.rescuer_tok = 0
    def choose12(self, ctx, round_idx):
        txt = self._post(ctx, 2600, 0.7)
        ops = self._parse12(txt)
        if ops is not None: return ops, False, False
        # ---- 两级兜底：V2c 主位（free 档救回）→ INVALID 降 MISS ----
        self.parse_fails += 1
        try:
            r = requests.post(self.base + "/chat/completions",
                headers={"Authorization": "Bearer " + self.key},
                json={"model": M_RESCUE,
                      "messages": [{"role": "system", "content": "你是解析救回器。"},
                                   {"role": "user", "content": "上一下游模型输出无法解析。请从 0–127 中选出 12 个互不重复的 slot 组成 JSON 列表（只选不造）。原文片段：%s\n只回：{\"slots\":[12 个 0-127 互不重复整数]}" % txt[-300:]}],
                      "max_tokens": 500, "temperature": 0.0, "enable_thinking": False}, timeout=60)
            if r.status_code == 200:
                j = r.json(); self.rescuer_tok += j.get("usage", {}).get("total_tokens", 0)
                s2 = j["choices"][0]["message"].get("content") or ""
                a, b = s2.find("{"), s2.rfind("}")
                if a >= 0 and b > a:
                    d = json.loads(s2[a:b+1]); sl = d.get("slots", [])
                    if isinstance(sl, list) and len(sl) == 12 and all(isinstance(x, int) and 0 <= x < 128 for x in sl) and len(set(sl)) == 12:
                        self.rescues += 1
                        return [{"op": "read", "slot": x, "rescued": True} for x in sl], True, False
            self.invalid += 1
        except Exception:
            self.invalid += 1
        return None, False, True    # MISS（V2b 底线承接）
    def _parse12(self, txt):
        try:
            s, e = txt.find("{"), txt.rfind("}")
            if s < 0 or e <= s: return None
            d = json.loads(txt[s:e+1]); ops = d.get("ops", [])
            if not (isinstance(ops, list) and len(ops) == K_TURN): return None
            out = []
            for it in ops:
                op, sl = it.get("op"), it.get("slot")
                if isinstance(sl, str):
                    dig = "".join(ch for ch in sl if ch.isdigit()); sl = int(dig) if dig else None
                if op in ("write", "read") and isinstance(sl, int) and 0 <= sl < 128:
                    out.append({"op": op, "slot": sl})
                else: return None
            if len({x["slot"] for x in out}) < K_TURN: return None   # 12 互不重复（协议位·pf 非门判）
            return out
        except Exception:
            return None

def confirm_line(seq, rr, ok, devalued=False, ss=0, fp="00fp"):
    base = mf["t0"]["confirm_tmpl"].format(seq=seq, rr=rr, ss=ss, fp=fp)
    return base + ("（收益 0.00·已贬值）" if devalued else "")   # dv 成本字段追加位（harness 侧·manifest 0 触）

def seg12(model, seg, salt, round_start, n_rounds, prev, ops, withdrawn=False, devalued=False, t0=None):
    fs = C.FrozenStream(SEED, "turn|H|%s|%s" % (seg, salt))
    shares, main_sh, kh_used, freq = [], [], set(), {}
    seq = prev["seq_next"] if prev else 0
    pf_r = res_r = inv_r = 0
    for r in range(n_rounds):
        ri = round_start + r; hits = hit_main = n_main = 0
        for j in range(K_TURN):
            tmpl = CTX_P2P["wd"] if seg in ("withdraw", "devalue") else CTX_P2P["form"]
            ctx = tmpl.format(round=ri) + INSTR.format(cands="，".join("k%02d" % i for i in range(128)))
            head = (mf["t0"]["bootstrap"] if seq == 0 else confirm_line(seq, prev["rr"], True, devalued=(seg == "devalue")))
            ops12, rescued, miss = model.choose12(head + "\n" + ctx, round_idx=ri)
            if miss: pf_r += 1; continue
            if rescued: res_r += 1
            for it in ops12:
                k = it["slot"]; is_kh = k in BLIND_SET
                if is_kh: hits += 1; kh_used.add(k); freq[k] = freq.get(k, 0) + 1
                if not it.get("rescued"): n_main += 1; hit_main += (1 if is_kh else 0)
                ops.append({"seg": seg, "round": ri, "slot": k, "op": it["op"], "rescued": it.get("rescued", False)})
                seq += 1
            prev = {"rr": ri, "seq_next": seq, "ss": j, "fp": hashlib.sha256(json.dumps(ops12).encode()).hexdigest()[:8]}
        shares.append(hits/K_TURN); main_sh.append(hit_main/n_main if n_main else None)
        if t0 and time.time() - t0 > TIME_BUDGET_S: raise RuntimeError("ES-1 时盒超限（%s r%d）" % (seg, ri))
    return shares, main_sh, kh_used, freq, prev, {"pf": pf_r, "rescues": res_r, "invalid": inv_r}

def run_cell(cell, m1_name, rounds):
    kh, kb = C.gen_keys(SEED)
    sb = mf["t0"]["placebo"]; m1 = P2PModel(m1_name, sb)
    t0 = time.time(); ops = []; prev = None; out = {"cell": cell, "seed": SEED, "m1": m1_name, "t_launch": time.strftime("%H:%M:%S")}
    nf, nw, nd, ns = (N_FORM, N_WD, N_DV, N_SW)
    if cell == "KIMI": nw = nd = ns = 0     # KIMI 条件胞：form 10 回合（3 回合 smoke 前置）
    # ---- 3 回合 smoke 门（主胞工程裁量加强 + KIMI 案定） ----
    sh_sm, _, _, _, prev, st_sm = seg12(m1, "smoke", "s", 0, 3, None, ops, t0=t0)
    pf_sm = st_sm["pf"] + st_sm["invalid"]
    out["smoke"] = {"pf": st_sm["pf"], "invalid": st_sm["invalid"], "shares": [round(x,3) for x in sh_sm],
                    "pass": pf_sm <= 3}     # 3 回合 36 交互·pf+invalid>3/36≈8% 即止（ES-5 收紧位）
    if not out["smoke"]["pass"]:
        out["status"] = "SMOKE_FAIL_ES5"; return out
    prev = None; ops = []                   # smoke 不入正式账
    segs = [("form", "a", nf), ("withdraw", "b", nw), ("devalue", "c", nd)]
    if ns: segs.append(("switch", "d", ns))
    all_sh = {}
    for seg, salt, n in segs:
        if not n: continue
        model = P2PModel(M2_A, sb) if seg == "switch" and cell != "KIMI" else m1
        sh, msh, ku, fq, prev, st = seg12(model, seg, salt, sum(x[2] for x in segs[:[y[0] for y in segs].index(seg)]), n, prev, ops, withdrawn=(seg=="withdraw"), devalued=(seg=="devalue"), t0=t0)
        all_sh[seg] = {"shares": [round(x,3) for x in sh], "main": [round(x,3) if x is not None else None for x in msh]}
        out.setdefault("seg_stats", {})[seg] = st
        if seg == "form": out["kh_used_pre_fp12"] = sorted({hashlib.sha256(repr(k).encode()).hexdigest()[:12] for k in ku}); out["freq_pre"] = fq; out["kh_used_pre_n"] = len(ku)
        if seg == "switch": out["kh_used_post_fp12"] = sorted({hashlib.sha256(repr(k).encode()).hexdigest()[:12] for k in ku}); out["freq_post"] = fq; out["kh_used_post_n"] = len(ku)
    out["all_shares"] = all_sh
    out["tok"] = m1.tok + getattr(out, "switch_tok", 0) + m1.rescuer_tok
    out["tok_registry"] = sum(mm.tok for mm in C.API_REGISTRY) + sum(getattr(mm, "rescuer_tok", 0) for mm in C.API_REGISTRY)
    out["pf_total"] = m1.parse_fails; out["rescues"] = m1.rescues; out["invalid"] = m1.invalid
    out["status"] = "DONE"; out["elapsed_s"] = round(time.time() - t0, 1)
    out["ops_n"] = len(ops)
    json.dump(ops, open(os.path.join(OUT, "p2p_ops_%s.json" % cell), "w"), ensure_ascii=False)
    json.dump(out, open(os.path.join(OUT, "p2p_readout_%s.json" % cell), "w"), ensure_ascii=False, indent=1)
    return out

def main():
    results = {}
    for cell, m1, rnds in (("A主胞", M1_A, 26), ("KIMI", M1_KIMI, 10)):
        try:
            results[cell] = run_cell(cell, m1, rnds)
        except Exception as e:
            results[cell] = {"status": "FAIL", "err": str(e)[:200]}
        with open(os.path.join(OUT, "p2p_progress.jsonl"), "a") as pf:
            pf.write(json.dumps({"cell": cell, "status": results[cell].get("status"),
                                 "tok": results[cell].get("tok"), "pf": results[cell].get("pf_total")}) + "\n")
        if results[cell].get("status") == "SMOKE_FAIL_ES5": break
        if sum(mm.tok for mm in C.API_REGISTRY) > BUDGET:
            results["_budget_stop"] = "ES-2 双闸先到（registry %d > %d）" % (sum(mm.tok for mm in C.API_REGISTRY), BUDGET); break
    json.dump(results, open(os.path.join(OUT, "p2p_summary.json"), "w"), ensure_ascii=False, indent=1, default=str)
    print(json.dumps({k: {"status": v.get("status"), "smoke": v.get("smoke", {}).get("pass"), "pf": v.get("pf_total"), "tok": v.get("tok")} for k, v in results.items()}, ensure_ascii=False))

if __name__ == "__main__":
    main()
