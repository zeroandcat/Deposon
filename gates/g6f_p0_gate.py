# -*- coding: utf-8 -*-
# P0''' mock 门·G6′ 补位发射器（0 API）：七项全过=launch-ready 界（0 现场改）
import os, sys, json, time, types
MOD = types.ModuleType("g6f"); MOD.__file__ = os.path.abspath("g6f_launch_exec.py")
os.environ["P2P_PLAN"] = "g6f"
exec(compile(open(MOD.__file__, encoding="utf-8").read(), MOD.__file__, "exec"), MOD.__dict__)
G = {}
# ① 盲面恒等（与 shared 读数包冻结件逐字节·b3693a8c1804 沿）
blind_ref = json.load(open("<readings-package-dir>"))["blind_kh"]
G["①盲面恒等"] = MOD.BLIND_KH == blind_ref and len(MOD.BLIND_KH) == 32
# ② manifest 恒等门（fail-loud 加载成功）
G["②manifest门"] = MOD.mf is not None and "t0" in MOD.mf
# ③ 预算闸（护栏 <guardrail>−全累计 <spent>=<cap>·盒 <box>·min 取小）
G["③预算闸"] = (MOD.GLOBAL_CAP == MOD.BUDGET)  # 结构不变量：闸值与生效预算恒等（运行位数值经 env 注入）
# ④ 预算充足（需求＋波动 ≤ 闸·运行位数值经 env 注入）
G["④预算充足"] = int(os.environ.get("HARNESS_REQUIRED_BUDGET", str(MOD.BUDGET))) <= MOD.BUDGET
# ⑤ 段结构（0 API·FakeModel 全程注入：A 主胞 smoke3+form10+wd4+dv4 无 switch·KIMI smoke3+form10）
SEG_LOG = []
class FakeBoom:
    tok = 0; parse_fails = 0; rescues = 0; invalid = 0; rescuer_tok = 0
    def __init__(self, name, sb): pass
    def choose12(self, prompt, round_idx=0):
        time.sleep(0.001)
        return [{"op": "read", "slot": i % 128} for i in range(12)], False, False
_orig_seg12 = MOD.seg12
def spy_seg12(model, seg, salt, round_start, n_rounds, *a, **kw):
    SEG_LOG.append((kw.get("cell"), seg, n_rounds))
    return _orig_seg12(model, seg, salt, round_start, n_rounds, *a, **kw)
MOD.seg12 = spy_seg12; MOD.P2PModel = FakeBoom
MOD.TIME_BUDGET = {"A主胞": 600, "KIMI": 600}; MOD.BUDGET = int(os.environ.get("HARNESS_BOX", "0"))
TEST_OUT = os.path.abspath("_p0_dump_test"); os.makedirs(TEST_OUT, exist_ok=True); MOD.OUT = TEST_OUT
try:
    MOD.run_cell("A主胞", "qwen3.7-flash", 18, time_budget=600)
    MOD.run_cell("KIMI", "kimi-k3.1-pro", 10, time_budget=600)
    segs_a = [x for x in SEG_LOG if x[0] == "A主胞"]; segs_k = [x for x in SEG_LOG if x[0] == "KIMI"]
    G["⑤段结构A主胞"] = [(s, n) for _, s, n in segs_a] == [("smoke", 3), ("form", 10), ("withdraw", 4), ("devalue", 4)]
    G["⑤段结构KIMI"] = [(s, n) for _, s, n in segs_k] == [("smoke", 3), ("form", 10)]
    ops_a = json.load(open(f"{TEST_OUT}/g6f_ops_A主胞.json", encoding="utf-8"))
    G["⑤ops台账"] = len(ops_a) == 18 * 144  # 18 正式回合×144 per-op（12 交互×12 槽·smoke 已 clear·与补射 1,152=8×144 口径互证)
    ro = json.load(open(f"{TEST_OUT}/g6f_readout_A主胞.json", encoding="utf-8"))
    G["⑤status_DONE"] = ro.get("status") == "DONE"
except Exception as e:
    G["⑤段结构A主胞"] = "EXC:" + str(e)[:120]
# ⑥ dump-on-exit FAIL 路径（时盒 0→RuntimeError→三件落盘+FAIL_partial 标注）
SEG_LOG.clear(); MOD.TIME_BUDGET["A主胞"] = 0
try:
    MOD.run_cell("A主胞", "qwen3.7-flash", 18, time_budget=0)
    G["⑥dump_FAIL路径"] = False
except RuntimeError:
    G["⑥dump_FAIL路径"] = all(os.path.exists(f"{TEST_OUT}/g6f_{k}_A主胞.{ext}") for k, ext in [("readout","json"),("ops","json"),("calls","jsonl")])
    if G["⑥dump_FAIL路径"]:
        ro2 = json.load(open(f"{TEST_OUT}/g6f_readout_A主胞.json", encoding="utf-8"))
        G["⑥FAIL标注"] = ro2.get("status") == "FAIL_partial" and "err" in ro2
# ⑦ per-call 9 字段明细行
calls = [json.loads(l) for l in open(f"{TEST_OUT}/g6f_calls_A主胞.jsonl", encoding="utf-8")]
nine = ["cell","seg","round","ts","elapsed","tok_this","pf","rescued","n_ops"]
G["⑦per_call_9字段"] = len(calls) > 0 and all(set(nine) <= set(c.keys()) for c in calls[:50])
ok = all(v is True for v in G.values())
for k, v in G.items(): print(("PASS" if v is True else "FAIL"), k, ("" if v is True else v))
print("P0''' G6′ 门：%s（%d/7）" % ("全绿 launch-ready" if ok else "未过门", sum(1 for v in G.values() if v is True)))
json.dump({"gate": G, "all_pass": ok}, open("g6f_p0_gate_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sys.exit(0 if ok else 1)
