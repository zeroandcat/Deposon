# -*- coding: utf-8 -*-
# A 主胞 switch 段补射（v4.2 冻结面派生·新件）·基=P2' v4.1 复跑已毕三段（form10+wd4+dv4）
# prev 基线：{"rr":17,"seq_next":2592}——calls 件 252 行实证三段全毕·smoke 后 seq 重置 0 起·18 回合×144 ops/回合
# confirm 头协议逐字节同构：seg12 只传 seq/rr/devalued（ss=0/fp="00fp" 恒定默认·不依赖 v4.1 丢失的 ops 明细）
# 预算：a 案闸 <cap> − v4.1 复跑 registry 终值（env P2P_PATCH_BUDGET 注入·发射器读 summary 算）
# 时盒：1200s（M2 max 档 96 calls 保守盒·ES-1 原则沿）
import sys, os, json, time, types

RUN_A = "<internal-path>"
os.environ.setdefault("P2P_PLAN", "a")
MOD = types.ModuleType("v4"); MOD.__file__ = os.path.join(RUN_A, "p2p_launch_v4_2.py")
exec(compile(open(MOD.__file__, encoding="utf-8").read(), MOD.__file__, "exec"), MOD.__dict__)

PATCH_BUDGET = int(os.environ["P2P_PATCH_BUDGET"])       # 发射器注入：a 案闸−v4.1 复跑终耗
V41_FINAL = int(os.environ["P2P_V41_FINAL"])             # v4.1 复跑 registry 终值（发射时点 summary 读）
MOD.BUDGET = PATCH_BUDGET                                 # 补射进程闸（registry 从 0 起·回合前检查沿）

CELL = "A主胞switch补射"; OUT = RUN_A
t0 = time.time(); ops = []; calls = []
out = {"cell": CELL, "seed": MOD.SEED, "m1": MOD.M1_A, "m2": MOD.M2_A, "t_launch": time.strftime("%H:%M:%S"),
       "plan": "a", "patch": True,
       "base": {"prev_rr": 17, "prev_seq_next": 2592,
                "basis": "v4.1 复跑 A 主胞 calls 252 行三段全毕（form10+wd4+dv4·pf=0 净面）·smoke 后 seq 重置 0 起·18 回合×144 ops",
                "v41_readout": "FAIL_partial@13:05:30（sb NameError·switch 段未跑）"},
       "budget": {"a案闸": int(os.environ.get("HARNESS_PATCH_CAP", "0")), "v41复跑终耗": V41_FINAL, "补射闸": PATCH_BUDGET}}
prev = {"rr": 17, "seq_next": 2592}

def _dump(status, err=None):
    out["status"] = status
    if err: out["err"] = str(err)[:200]
    out["elapsed_s"] = round(time.time() - t0, 1); out["ops_n"] = len(ops)
    out["tok_registry"] = sum(getattr(mm, "tok", 0) for mm in MOD.C.API_REGISTRY)   # 加固：构造期残缺实例兜底
    try:
        json.dump(ops, open(os.path.join(OUT, "p2p_ops_%s.json" % CELL), "w"), ensure_ascii=False)
        json.dump(out, open(os.path.join(OUT, "p2p_readout_%s.json" % CELL), "w"), ensure_ascii=False, indent=1, default=str)
        with open(os.path.join(OUT, "p2p_calls_%s.jsonl" % CELL), "w") as cf:
            for c_ in calls: cf.write(json.dumps(c_, ensure_ascii=False) + "\n")
    except Exception as dump_err:
        out["dump_err"] = str(dump_err)[:120]

try:
    model = MOD.P2PModel(MOD.M2_A, MOD.mf["t0"]["placebo"])   # M1→M2 换模（v4.2 修①构造位）
    out["m2_model"] = model.name if hasattr(model, "name") else MOD.M2_A
    sh, msh, ku, fq, prev, st = MOD.seg12(model, "switch", "d", 18, 8, prev, ops,
                                          t0=t0, time_budget=1200, calls=calls, cell=CELL)
    out["all_shares"] = {"switch": {"shares": [round(x,3) for x in sh], "main": [round(x,3) if x is not None else None for x in msh]}}
    out["seg_stats"] = {"switch": st}
    out["kh_used_post_fp12"] = sorted({MOD.hashlib.sha256(repr(k).encode()).hexdigest()[:12] for k in ku})
    out["freq_post"] = fq; out["kh_used_post_n"] = len(ku)
    out["tok"] = model.tok + model.rescuer_tok
    out["pf_total"] = model.parse_fails; out["rescues"] = model.rescues; out["invalid"] = model.invalid
    out["prev_final"] = {"rr": prev["rr"], "seq_next": prev["seq_next"]}
    _dump("DONE")
except Exception as e:
    _dump("FAIL_partial", e)
    print("PATCH_FAIL: %r" % e); sys.exit(1)
print(json.dumps({"cell": CELL, "status": out.get("status"), "elapsed_s": out.get("elapsed_s"),
                  "ops_n": out.get("ops_n"), "tok": out.get("tok"), "tok_registry": out.get("tok_registry"),
                  "kh_used_post_n": out.get("kh_used_post_n"), "pf_total": out.get("pf_total"),
                  "rescues": out.get("rescues"), "prev_final": out.get("prev_final")}, ensure_ascii=False))
