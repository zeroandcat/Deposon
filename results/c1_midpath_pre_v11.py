# [V1.1-HEADER] c1_midpath_pre_v11.py —— OOM-fix 补丁版（2026-11-12 10:4x·鲍勃）
# 根因：v1 首跑 OOM（10:44 发射·S4/eval 走 ForCausalLM 完整前向 [16,512,151936] 全词表 logits
# ≈2.32GiB 连续块×双模型驻留）——与 deepen_r1 v1 OOM 同机制差（训练稳/eval 界炸）。
# patch 三点全披露：①eval_bacc last-pos 路径 ②S4 双模型 base 前向+lm_head 补算 [B,1,V] ③读数件名 _v11 区分。
# 数值等价声明：lm_head 逐位置线性·last-pos 与全序列计算等价（deepen_r1_v11 GATE-0 等价性实证先例在册）。
# 判据/门/预注册读数面 0 改（gates_prereg 字面不动）·红绿如实。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""c1_midpath_pre.py —— 中径 3 配置（附带并行·预注册执行件）｜零点窗附带位脚本
================================================================================================
承办：鲍勃-实验分析师｜派单：群管理员 2026-11-11 19:11:33〔零点窗实验前置就绪轮·检查表⑤〕
基据：中径位裁决＝附带并行（3 配置预注册·<10 GPU min）＋B 轨执行细节（G1-A 门下预注册·定位
      0.432 免除集贡献的组件归属——lm_head 件单列账沿规格）＋A 轨技术注记（tied 约束
      E＝W_lmᵀ（155.6M/596M≈26%）·「嵌入-LN 分离」在 E/lm_head 面结构不可分·LN 参数量<0.5%；
      可行变体＝嵌入 int8 混合精度需新代码路径）。
预注册三配置（执行前冻结·红绿如实·0 现场定参）：
  M1 embedexempt  196 线性＝三值+补偿（v2-2 同面）·lm_head(+tied embed) 免除·LN 113 件三值（v2-1 LN 同面）
       → 定位嵌入/lm_head 组件贡献（对照 v2_1 与 v2_2）
  M2 lnexempt     196 线性＝三值+补偿（v2-2 同面）·lm_head(+tied embed) 三值+补偿（Rm=None 面）·LN 免除
       → 定位 LN 组件贡献（对照 v2_1 与 v2_2）
  M3 int8embed    196 线性＝三值+补偿（v2-2 同面）·lm_head(+tied embed) int8 per-row absmax（新代码位）·LN 三值（v2-1 同面）
       → 混合精度中径读数（部署覆盖面方向·A 轨可行变体）
预注册门与读数（执行前冻结）：
  · 逐配置 G1-A 三判据面登记：ED_energy≤0.26（compatibility face）·S4_cos_layer0≥0.7·方向性（ED≤v2_1 红臂 0.68964 在册）
  · lm_head 件单列 ED 账（M2/M3 面三值/int8 单件 ED·M1 免除＝0）
  · 归属账：ΔED(M1−v2_1)＝嵌入免除贡献·ΔED(M2−v2_1)＝LN 免除贡献·ΔED(M3−M1)＝int8 对 bf16 嵌入面增量
    （v2_2−v2_1＝0.432 总免除集增益在册·免重跑）
  · S5_bacc＝500 样本评估集（与 v2 复跑同口径同 seed·对照 v2_2 在册 0.6165）
预算：H 采集 ~2 min＋3×(量化+S4+S5) ≈ 6–8 GPU min（<10 min 裁决字面内）。
纪律：0 改既有件（c1_v2.py 原件只读·本件纯新增）；红绿如实；服务器侧执行件（本轮本地
      py_compile＋预注册冻结·执行候零点窗附带位凭据到即跑）。
用法（服务器侧）：python3 c1_midpath_pre.py
"""
import time, json, torch, pyarrow.parquet as pq, random, math, collections
from transformers import AutoTokenizer, AutoModelForCausalLM

SEED = 20261110
MP = '/root/autodl-tmp/models/Qwen3-0.6B'
DP = '/root/autodl-tmp/materials/d1_llm_aggrefact/nina_dev.parquet'
OUT = '/root/autodl-tmp/runs/c1midpath'; import os; os.makedirs(OUT, exist_ok=True)
dev = 'cuda'
TAU = 0.6
V21_ED_INRECORD = 0.68964        # 在册红臂（11-10 复跑·f64d59f1ce2d）
V22_READ_INRECORD = {'ED': 0.25758, 'cos_layer0': 0.9127, 'bacc': 0.6165, 'gain': 0.432}
torch.manual_seed(SEED); random.seed(SEED)
torch.backends.cuda.matmul.allow_tf32 = True
RES = {'meta': {'script': 'c1_midpath_pre', 'seed': SEED, 'tau': TAU,
                'prereg': '2026-11-11 冻结（零点窗前置就绪轮·合流中径位裁决附带并行）',
                'configs': ['M1_embedexempt', 'M2_lnexempt', 'M3_int8embed'],
                'inrecord_anchors': {'v2_1_ED': V21_ED_INRECORD, 'v2_2': V22_READ_INRECORD}}}

def stratified(tab, N, seed, exclude=frozenset()):
    rng = random.Random(seed); by = collections.defaultdict(list)
    for i, r in enumerate(tab): by[r['dataset']].append(i)
    pick = []
    for ds, idxs in sorted(by.items()):
        avail = [i for i in idxs if i not in exclude]
        k = max(1, round(N * len(avail) / len(tab)))
        pick += rng.sample(avail, min(k, len(avail)))
    rng.shuffle(pick); return pick[:N]

def fmt(r): return f"Document: {r['doc'][:2000]}\nClaim: {r['claim']}\nIs the claim supported by the document? Answer with Yes or No only."

def hadamard(d):
    H = torch.tensor([[1.]], dtype=torch.float64)
    while H.shape[0] < d: H = torch.cat([torch.cat([H, H], 1), torch.cat([H, -H], 1)], 0)
    return H

def make_R(d, seed, tag):
    b = d & (-d); n = d // b; R = torch.zeros((d, d), dtype=torch.float64)
    for k in range(n):
        gg = torch.Generator().manual_seed(seed + (sum(ord(c) for c in tag + f'#{k}') % 1000))
        sk = (torch.randint(0, 2, (b,), generator=gg, dtype=torch.float64) * 2 - 1)
        R[k * b:(k + 1) * b, k * b:(k + 1) * b] = hadamard(b) * sk.unsqueeze(0) / math.sqrt(b)
    return R.float()

def tern_target(W, alpha, tau):
    thr = tau * alpha
    return torch.where(W.abs() >= thr, torch.where(W >= 0, torch.ones_like(W), -torch.ones_like(W)), torch.zeros_like(W))

def ls_alpha(W, tau, iters=2, mode='row'):
    if mode == 'row':
        a = W.abs().median(dim=1, keepdim=True).values.clamp(min=1e-12)
        for _ in range(iters):
            T = tern_target(W, a, tau)
            den = (T * T).sum(dim=1, keepdim=True).clamp(min=1e-12)
            a = (W * T).sum(dim=1, keepdim=True) / den
            a = a.abs().clamp(min=1e-12)
        return a
    a = torch.full((1, 1), float(W.abs().median()), dtype=W.dtype, device=W.device).clamp(min=1e-12)
    for _ in range(iters):
        T = tern_target(W, a, tau)
        den = (T * T).sum().clamp(min=1e-12)
        a = ((W * T).sum() / den).abs().clamp(min=1e-12).reshape(1, 1)
    return a

def gptq_chol(W, H, alpha, tau, damp=0.05, order=True):
    d = H.shape[0]
    Hc = H.clone()
    dead = torch.diag(Hc) == 0
    Hc[:, dead] = 0; Hc[dead, dead] = 1
    dampv = damp * Hc.diagonal().mean().clamp(min=1e-8)
    Hc.diagonal().add_(dampv)
    cond = float((torch.linalg.eigvalsh(Hc)[[-1]] / torch.linalg.eigvalsh(Hc)[[0]]).item())
    perm = torch.arange(d, device=W.device)
    if order:
        perm = torch.argsort(Hc.diagonal(), descending=True)
        W = W[:, perm]; Hc = Hc[perm][:, perm]
    fallback = 0
    try:
        L = torch.linalg.cholesky(Hc); Hinv = torch.cholesky_inverse(L); U = torch.linalg.cholesky(Hinv, upper=True)
    except Exception:
        fallback = 1
        ev, V = torch.linalg.eigh(Hc.double())
        ev = ev.clamp(min=ev.max().abs() * 1e-10 + 1e-12)
        Hinv = (V / ev.unsqueeze(0)) @ V.t()
        U = torch.linalg.cholesky(Hinv, upper=True).float()
    Wq = torch.empty_like(W)
    for j in range(d):
        w = W[:, j]; thr = tau * alpha.squeeze(1)
        q = torch.where(w.abs() >= thr, torch.where(w >= 0, alpha.squeeze(1), -alpha.squeeze(1)), torch.zeros_like(w))
        Wq[:, j] = q
        err = (w - q) / U[j, j]
        if j + 1 < d:
            W[:, j + 1:].sub_(err.unsqueeze(1) @ U[j, j + 1:].unsqueeze(0))
    if order:
        inv = torch.empty_like(perm); inv[perm] = torch.arange(d, device=W.device); Wq = Wq[:, inv]
    return Wq, (cond, fallback)

# ---------- setup（与 c1_v2 同口径） ----------
tok = AutoTokenizer.from_pretrained(MP)
model = AutoModelForCausalLM.from_pretrained(MP, dtype=torch.bfloat16).to(dev); model.eval()
tab = pq.read_table(DP).to_pylist()
eval_ids = stratified(tab, 500, SEED)
calib_ids = stratified(tab, 512, SEED, exclude=frozenset(eval_ids))
probe_ids = stratified(tab, 512, SEED + 1, exclude=frozenset(eval_ids) | frozenset(calib_ids))
id_yes = tok.encode(' Yes')[0]; id_no = tok.encode(' No')[0]
pristine = {k: v.clone() for k, v in model.state_dict().items()}
def restore(): model.load_state_dict(pristine)

def eval_bacc(mdl, ids):
    preds = []
    with torch.no_grad():
        for i in range(0, len(ids), 16):
            batch = [fmt(tab[j]) for j in ids[i:i + 16]]
            enc = tok(batch, padding=True, truncation=True, max_length=512, return_tensors='pt', padding_side='left').to(dev)
            # [V1.1-PATCH-1] last-pos 路径（OOM 修复·与 deepen_r1_v11 同法·数值等价：lm_head 逐位置线性）
            hs = mdl.model(input_ids=enc['input_ids'], attention_mask=enc['attention_mask']).last_hidden_state
            lg = mdl.lm_head(hs[:, -1:, :])[:, 0, :]
            preds += (lg[:, id_yes] > lg[:, id_no]).long().tolist()
    golds = [tab[j]['label'] for j in ids]
    tp = sum(1 for p, g in zip(preds, golds) if p == g == 1); tn = sum(1 for p, g in zip(preds, golds) if p == g == 0)
    fn = sum(1 for p, g in zip(preds, golds) if p == 0 and g == 1); fp = sum(1 for p, g in zip(preds, golds) if p == 1 and g == 0)
    tpr = tp / (tp + fn) if tp + fn else 0; tnr = tn / (tn + fp) if tn + fp else 0
    return round((tpr + tnr) / 2, 4)

lin_modules = [(n, m) for n, m in model.named_modules() if isinstance(m, torch.nn.Linear)]
LN_names = [n for n, _ in model.named_parameters() if n.endswith('norm.weight')]
Hstat = {}; Nstat = {}; cur_mask = [None]
def mk_hook(name):
    def hook(mod, inp):
        X = inp[0].detach()
        if X.dim() == 3: X = X.reshape(-1, X.shape[-1])
        m = cur_mask[0]
        if m is not None: X = X[m.reshape(-1).bool()]
        X = X.float()
        if name not in Hstat: Hstat[name] = torch.zeros(X.shape[1], X.shape[1], device=dev); Nstat[name] = 0
        Hstat[name] += X.t() @ X; Nstat[name] += X.shape[0]
    return hook
handles = [m.register_forward_pre_hook(mk_hook(n)) for n, m in lin_modules]
with torch.no_grad():
    for i in range(0, len(calib_ids), 16):
        batch = [fmt(tab[j]) for j in calib_ids[i:i + 16]]
        enc = tok(batch, padding=True, truncation=True, max_length=512, return_tensors='pt').to(dev)
        cur_mask[0] = enc['attention_mask']
        model(input_ids=enc['input_ids'], attention_mask=enc['attention_mask'])
for h in handles: h.remove()

RS = {}
def get_R(d):
    if str(d) not in RS: RS[str(d)] = make_R(d, SEED, f'r{d}').to(dev)
    return RS[str(d)]

def int8_row_quant(W):
    """M3 新代码位：嵌入/lm_head（tied 张量）int8 per-row absmax 混合精度（A 轨可行变体·per-row scale schema）"""
    scale = W.abs().max(dim=1, keepdim=True).values.clamp(min=1e-12) / 127.0
    Q = (W / scale).round().clamp(-128, 127) * scale
    return Q

def run_mid(name, embed_mode, ln_exempt):
    """embed_mode: 'exempt' | 'tern' | 'int8'；ln_exempt: bool。196 线性恒为三值+补偿（v2-2 同面）。
    逐配置 restore() 前置（幂等·P4 根因教训内化）＋lm_head 件单列 ED 账。"""
    t0 = time.time()
    restore()
    ed_sq = ed_base = 0.0; lm_ed = None; n_quant = 0; conds = []
    for key, mod in lin_modules:
        p = mod.weight; in_dim = p.shape[-1]
        Hm = Hstat.get(key)
        if key == 'lm_head' or 'embed' in key:
            if embed_mode == 'exempt':
                continue                                    # M1：免除（保精度）
            W0 = p.detach().float()
            if embed_mode == 'int8':
                Wtil = int8_row_quant(W0).to(torch.bfloat16)   # M3：int8 per-row
            else:
                W = W0; Rm = None                            # M2：三值+补偿（lm_head 无旋转面·同 v2_1）
                alpha = ls_alpha(W, TAU, mode='row')
                if Hm is not None:
                    Hz = Hm / Nstat[key]
                    Q, cf = gptq_chol(W.clone(), Hz, alpha, TAU)
                    conds.append(cf[0])
                else:
                    Q = alpha * tern_target(W, alpha, TAU)
                Wtil = Q.to(torch.bfloat16)
            lm_ed = float(((W0 - Wtil.float()) ** 2).sum().item() / (W0 ** 2).sum().item())
            ed_sq += float(((p.detach().float() - Wtil.float()) ** 2).sum().item())
            ed_base += float((p.detach().float() ** 2).sum().item())
            n_quant += 1
            p.data.copy_(Wtil.to(torch.bfloat16))
            continue
        Rm = get_R(in_dim); W = p.detach().float() @ Rm
        alpha = ls_alpha(W, TAU, mode='row')
        if Hm is not None:
            Hz = Rm.t() @ (Hm / Nstat[key]) @ Rm
            Q, cf = gptq_chol(W.clone(), Hz, alpha, TAU)
            conds.append(cf[0])
        else:
            Q = alpha * tern_target(W, alpha, TAU)
        Wtil = ((Q @ Rm.t())).to(torch.bfloat16).float()
        ed_sq += float(((p.detach().float() - Wtil) ** 2).sum().item()); ed_base += float((p.detach().float() ** 2).sum().item())
        n_quant += 1
        p.data.copy_(Wtil.to(torch.bfloat16))
    for n in ([] if ln_exempt else LN_names):               # M2 免除；M1/M3 LN 三值（v2-1 LN 同面）
        p = dict(model.named_parameters())[n]
        Rm = get_R(int(p.shape[-1])); w = p.detach().float()
        wrot = (w.unsqueeze(0) @ Rm).squeeze(0)
        alpha = ls_alpha(wrot.unsqueeze(0), TAU, mode='row').reshape(1, 1)
        q = alpha * tern_target(wrot.unsqueeze(0), alpha, TAU)
        wtil = ((q @ Rm.t()).squeeze(0)).to(torch.bfloat16)
        ed_sq += float(((w - wtil.float()) ** 2).sum().item()); ed_base += float((w ** 2).sum().item())
        n_quant += 1
        p.data.copy_(wtil)
    r = {'config': name, 'embed_mode': embed_mode, 'ln_exempt': ln_exempt, 'n_quant': n_quant,
         'ED_energy': round(ed_sq / ed_base, 6), 'lm_head_ED_single': round(lm_ed, 6) if lm_ed is not None else 0.0,
         'cond_max': max(conds) if conds else None}
    # S4（对照模型逐层余弦·与 v2 同法）
    model_ref = AutoModelForCausalLM.from_pretrained(MP, dtype=torch.bfloat16).to(dev); model_ref.eval()
    acc = collections.defaultdict(lambda: torch.zeros(4, device=dev)); kl_sum = 0.0; kl_n = 0
    with torch.no_grad():
        for i in range(0, len(probe_ids), 16):
            batch = [fmt(tab[j]) for j in probe_ids[i:i + 16]]
            enc = tok(batch, padding=True, truncation=True, max_length=512, return_tensors='pt', padding_side='left').to(dev)
            hb = []; hr = []
            hoks = [l.register_forward_hook(lambda m, ii, oo: hb.append(oo[0].detach() if isinstance(oo, tuple) else oo.detach())) for l in model.model.layers]
            # [V1.1-PATCH-2] base 前向（无 lm_head 全词表大块·hooks 挂 model.model.layers 触发不变）
            out_q = model.model(input_ids=enc['input_ids'], attention_mask=enc['attention_mask'])
            for h in hoks: h.remove()
            hoks = [l.register_forward_hook(lambda m, ii, oo: hr.append(oo[0].detach() if isinstance(oo, tuple) else oo.detach())) for l in model_ref.model.layers]
            # [V1.1-PATCH-2b] base 前向
            out_b = model_ref.model(input_ids=enc['input_ids'], attention_mask=enc['attention_mask'])
            for h in hoks: h.remove()
            m = enc['attention_mask']; mb = m.bool().unsqueeze(-1)
            for li in range(len(hb)):
                a = hb[li].float(); b = hr[li].float()
                av = a[mb.expand_as(a)].reshape(-1, a.shape[-1]); bv = b[mb.expand_as(b)].reshape(-1, b.shape[-1])
                acc[li][0] += (av * bv).sum(); acc[li][1] += (av * av).sum(); acc[li][2] += (bv * bv).sum(); acc[li][3] += ((av - bv) ** 2).sum()
            # [V1.1-PATCH-2c] last-pos logits 由 lm_head 补算（[B,1,V] 小块·数值等价）
            lgB = model_ref.lm_head(out_b.last_hidden_state[:, -1:, :])[:, 0, :]
            lgQ = model.lm_head(out_q.last_hidden_state[:, -1:, :])[:, 0, :]
            pB = torch.log_softmax(lgB.float(), -1); pQ = torch.log_softmax(lgQ.float(), -1)
            kl = (pB.exp() * (pB - pQ)).sum(-1); kl_sum += float(kl.sum().item()); kl_n += len(batch)
            del hb, hr, out_q, out_b
    del model_ref
    cos_layers = [float(acc[li][0].item() / (math.sqrt(float(acc[li][1].item())) * math.sqrt(float(acc[li][2].item())) + 1e-12)) for li in sorted(acc)]
    r['S4_cos_layer0'] = round(cos_layers[0], 4)
    r['S4_cos_median'] = round(sorted(cos_layers)[len(cos_layers) // 2], 4)
    r['S4_KL_lastpos'] = round(kl_sum / max(1, kl_n), 5)
    r['S5_bacc'] = eval_bacc(model, eval_ids)
    # 预注册门（G1-A 三判据面·执行前冻结判读）
    r['gates_prereg'] = {'G1A_ED': r['ED_energy'] <= 0.26,
                         'G1A_cos_layer0': r['S4_cos_layer0'] >= 0.7,
                         'G1A_direction': r['ED_energy'] <= V21_ED_INRECORD}
    r['wall_s'] = round(time.time() - t0, 1)
    restore()
    RES[name] = r
    print(name, json.dumps(r), flush=True)
    return r

t0 = time.time()
m1 = run_mid('M1_embedexempt', 'exempt', False)
m2 = run_mid('M2_lnexempt', 'tern', True)
m3 = run_mid('M3_int8embed', 'int8', False)
# 归属账（预注册读数面·在册对照）
RES['attribution_prereg'] = {
    'embed_lmhead_exempt_gain_ED': round(m1['ED_energy'] - V21_ED_INRECORD, 6),     # ΔED(M1−v2_1)
    'ln_exempt_gain_ED': round(m2['ED_energy'] - V21_ED_INRECORD, 6),               # ΔED(M2−v2_1)
    'int8_vs_bf16_embed_ED': round(m3['ED_energy'] - m1['ED_energy'], 6),           # ΔED(M3−M1)
    'total_exempt_gain_inrecord': V22_READ_INRECORD['gain'],                        # v2_2−v2_1＝0.432 在册
    'M1_vs_v2_2_LN_delta_ED': round(m1['ED_energy'] - V22_READ_INRECORD['ED'], 6),
    'M2_vs_v2_2_embed_delta_ED': round(m2['ED_energy'] - V22_READ_INRECORD['ED'], 6)}
RES['total_wall_s'] = round(time.time() - t0, 1)
json.dump(RES, open(f'{OUT}/c1midpath_results_v11.json', 'w', indent=1, ensure_ascii=False), ensure_ascii=False)
print('ATTRIBUTION', json.dumps(RES['attribution_prereg']), flush=True)
print('C1MIDPATH-V11-DONE', flush=True)
