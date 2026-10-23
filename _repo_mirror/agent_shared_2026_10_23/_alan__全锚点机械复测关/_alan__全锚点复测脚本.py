#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全锚点机械复测关（anchor audit gate）· v1.0
受托：群管理员（2026-10-12 派单）｜承办：阿兰（文献调研员）
用途：论文终稿（v0.3 之后、排版之前）的强制机械复测门。
  输入论文 md，自动抽取全部「路径 + SHA-12 + 字节数」证据锚，
  对照 ①克隆实测值 ②线索册登记值 ③仓内登记源（可选），
  输出三档报告：全等 / 漂移-须并报 / 失配-报警。
铁律：0 改动论文本体（只读输入）；0 编造（所有未命中如实登记）。

用法：
  python3 阿兰_全锚点复测脚本.py <论文.md> \
      [--clone /home/z/my-project/repos/Deposon] \
      [--cluebook <双版合一线索册.md>] \
      [--no-registry]        # 关闭仓内登记源扫描（默认开启）
      [--inline]             # 加扫行内锚（正文反引号「路径 · sha」式，默认只扫附录表行）
      [-o 输出报告.md]       # 默认 ./anchor_audit_report_<时间戳>.md

三档判定语义（重要）：
  全等          ＝ 克隆实测 sha256[:12]+bytes 与稿值一致
                   （若线索册登记值与稿值不同而实测一致，附注登记值——已知「远端脱敏版 vs 本地原件」
                     差（如 2 字节级）属正常面，不降档）
  漂移-须并报   ＝ 实测 ≠ 稿值，但稿值可在登记面对上（线索册登记 或 仓内登记源命中）
                   ⇒ 稿值非虚构，但盘上已漂移，论文须按分歧并报纪律登记差异
  失配-报警     ＝ 实测 ≠ 稿值 且无任何登记可对；或路径克隆 0 命中（含真名可追时给出追查线索）
"""
import argparse
import datetime
import hashlib
import os
import re
import subprocess
import sys

HEX12 = re.compile(r'\b[0-9a-f]{12}\b')

# 附录表行主模式：| E01 | `path` | `sha12` | 12,345 | note |
ROW = re.compile(
    r'^\|\s*(E\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{12})`\s*\|\s*([\d,]+)\s*\|',
    re.M)
# 行内宽松模式（--inline）：`path` · `sha12`（路径须含 / 或 . 且形似文件）
INLINE = re.compile(
    r'`([A-Za-z0-9_\-./]+[/.][A-Za-z0-9_.\-]+)`\s*(?:·|,|\|)\s*`?([0-9a-f]{12})`?')

NUM = re.compile(r'\d[\d,\u00a0 ]*\d|\d')


def read(p):
    with open(p, 'rb') as f:
        return f.read()


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def git_head(clone):
    try:
        return subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=clone,
                              capture_output=True, text=True, timeout=15
                              ).stdout.strip()
    except Exception:
        return '(git 不可用)'


def resolve(path, clone):
    """路径解析：paper/ 前缀→克隆根；其余→_september_workspace/ 优先，次试根级。"""
    cands = []
    if path.startswith('paper/'):
        cands.append(os.path.join(clone, path))
    else:
        cands.append(os.path.join(clone, '_september_workspace', path))
        cands.append(os.path.join(clone, path))
    for c in cands:
        if os.path.isfile(c):
            return c, None
    base = os.path.basename(path)
    hits = []
    for root, _, files in os.walk(clone):
        if '.git' in root:
            continue
        if base in files:
            hits.append(os.path.relpath(os.path.join(root, base), clone))
    return None, hits


def parse_cluebook(cb_path):
    """线索册登记抽取：表格行内 反引号路径 + 12hex + 数字（本地列）。"""
    reg = {}
    if not cb_path:
        return reg
    try:
        text = read(cb_path).decode('utf-8', errors='replace')
    except Exception:
        return reg
    for line in text.splitlines():
        if '|' not in line:
            continue
        m = re.search(r'`([^`\s|]+)`', line)
        if not m or ('/' not in m.group(1) and '.' not in m.group(1)):
            continue
        path = m.group(1)
        rest = line[m.end():]
        h = HEX12.search(rest)
        if not h:
            continue
        n = NUM.search(rest[h.end():h.end() + 24])
        if not n:
            continue
        try:
            bts = int(n.group(0).replace(',', '').replace('\u00a0', '').replace(' ', ''))
        except ValueError:
            continue
        reg.setdefault(path, (h.group(0), bts))
    return reg


def registry_lookup(clone, sha):
    """仓内登记源：克隆 _september_workspace 的 md/json/txt 内检索稿 sha。"""
    hits = []
    for root, _, files in os.walk(os.path.join(clone, '_september_workspace')):
        if '.git' in root:
            continue
        for fn in files:
            if not fn.endswith(('.md', '.json', '.txt')):
                continue
            p = os.path.join(root, fn)
            try:
                if sha.encode() in read(p):
                    hits.append(os.path.relpath(p, clone))
                    if len(hits) >= 3:
                        return hits
            except Exception:
                pass
    return hits


def extract(paper, inline=False):
    text = read(paper).decode('utf-8', errors='replace')
    anchors = []
    seen = set()
    for eid, path, sha, byts in ROW.findall(text):
        key = (eid, path, sha, byts)
        if key in seen:
            continue
        seen.add(key)
        anchors.append({'id': eid, 'path': path, 'sha': sha,
                        'bytes': int(byts.replace(',', '')), 'ctx': '附录表行'})
    if inline:
        for i, (path, sha) in enumerate(INLINE.findall(text), 1):
            if any(a['path'] == path and a['sha'] == sha for a in anchors):
                continue
            anchors.append({'id': f'IN{i}', 'path': path, 'sha': sha,
                            'bytes': None, 'ctx': '行内'})
    return anchors


def audit(paper, clone, cluebook, use_registry=True, inline=False):
    anchors = extract(paper, inline)
    cb = parse_cluebook(cluebook) if cluebook else {}
    results = []
    for a in anchors:
        r = dict(a)
        real, alt = resolve(a['path'], clone)
        if real is None:
            cbv = cb.get(a['path'])
            if cbv and cbv[0] == a['sha']:
                r['verdict'] = '漂移-须并报'
                r['detail'] = (f"路径克隆 0 命中（同名他址：{', '.join(alt[:3]) if alt else '无'}）；"
                               f"稿值=线索册登记 {cbv[0]}/{cbv[1]:,}")
            else:
                r['verdict'] = '失配-报警'
                r['detail'] = '克隆 0 命中'
                if alt:
                    r['detail'] += '；同文件名见他址：' + ', '.join(alt[:3])
            results.append(r)
            continue
        b = read(real)
        gsha, gb = sha12(b), os.path.getsize(real)
        r['measured'] = (gsha, gb)
        if a['bytes'] is not None and gsha == a['sha'] and gb == a['bytes']:
            r['verdict'] = '全等'
            notes = []
            cbv = cb.get(a['path'])
            if cbv and (cbv[0] != a['sha'] or cbv[1] != a['bytes']):
                notes.append(f'线索册登记值 {cbv[0]}/{cbv[1]:,}（与稿值不同，'
                             f'疑远端脱敏版 vs 本地原件差，未降档）')
            r['detail'] = '；'.join(notes) or '实测与稿值一致'
        else:
            reg_hits = registry_lookup(clone, a['sha']) if use_registry else []
            cbv = cb.get(a['path'])
            anchored = reg_hits or (cbv is not None and cbv[0] == a['sha'])
            if anchored:
                r['verdict'] = '漂移-须并报'
                src = []
                if cbv and cbv[0] == a['sha']:
                    src.append(f'线索册登记 {cbv[0]}/{cbv[1]:,}')
                if reg_hits:
                    src.append('仓内登记源：' + ', '.join(reg_hits))
                r['detail'] = (f"实测 {gsha}/{gb:,} ≠ 稿值；稿值见〔{'；'.join(src)}〕"
                               f"⇒ 登记后漂移，须在稿内并报差异")
            else:
                r['verdict'] = '失配-报警'
                r['detail'] = f'实测 {gsha}/{gb:,} ≠ 稿值且无登记可对'
        results.append(r)
    return results


def report(results, paper, clone, cb_path, use_registry, inline, out):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    head = git_head(clone)
    n = {k: sum(1 for r in results if r['verdict'] == k)
         for k in ('全等', '漂移-须并报', '失配-报警')}
    L = []
    L.append('# 全锚点机械复测报告')
    L.append('')
    L.append(f'- **复测时间**：{now}　**克隆**：`{clone}` @ HEAD `{head}`')
    L.append(f'- **对象**：`{paper}`（0 改动本体，只读复测）')
    L.append(f'- **参数**：线索册 `{os.path.basename(cb_path) if cb_path else "未启用"}`'
             f'｜仓内登记源扫描：{"开" if use_registry else "关"}｜行内锚：{"开" if inline else "关"}')
    L.append(f'- **锚点抽取**：{len(results)} 条（附录表行模式）')
    L.append('')
    L.append(f'## 总判定：全等 **{n["全等"]}** / 漂移-须并报 **{n["漂移-须并报"]}** / 失配-报警 **{n["失配-报警"]}**')
    L.append('')
    for tier in ('失配-报警', '漂移-须并报', '全等'):
        if not n[tier]:
            continue
        L.append(f'## {tier}（{n[tier]} 条）')
        L.append('')
        L.append('| 锚 | 路径 | 稿值 | 实测 | 说明 |')
        L.append('|---|---|---|---|---|')
        for r in results:
            if r['verdict'] != tier:
                continue
            m = r.get('measured')
            ms = f"`{m[0]}` / {m[1]:,}" if m else '—'
            vs = (f"`{r['sha']}` / {r['bytes']:,}" if r['bytes'] is not None
                  else f"`{r['sha']}` / —")
            L.append(f"| {r['id']} | `{r['path']}` | {vs} | {ms} | {r['detail']} |")
        L.append('')
    L.append('---')
    L.append(f'*件止。全锚点机械复测关 v1.0 · 承办：阿兰（文献调研员）· {now} ·'
             f' 三档判定语义见使用说明；0 改动论文本体*')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    return n


def main():
    ap = argparse.ArgumentParser(description='全锚点机械复测关 v1.0')
    ap.add_argument('paper')
    ap.add_argument('--clone', default='/home/z/my-project/repos/Deposon')
    ap.add_argument('--cluebook', default=None)
    ap.add_argument('--no-registry', action='store_true')
    ap.add_argument('--inline', action='store_true')
    ap.add_argument('-o', '--out', default=None)
    a = ap.parse_args()
    if not os.path.isfile(a.paper):
        sys.exit(f'论文不存在：{a.paper}')
    out = a.out or (f'anchor_audit_report_{datetime.datetime.now():%Y%m%d_%H%M%S}.md')
    results = audit(a.paper, a.clone, a.cluebook,
                    use_registry=not a.no_registry, inline=a.inline)
    n = report(results, a.paper, a.clone, a.cluebook,
               not a.no_registry, a.inline, out)
    print(f'复测完成：全等 {n["全等"]} / 漂移-须并报 {n["漂移-须并报"]} / 失配-报警 {n["失配-报警"]}')
    print(f'报告：{out}')
    sys.exit(1 if n['失配-报警'] else 0)


if __name__ == '__main__':
    main()
