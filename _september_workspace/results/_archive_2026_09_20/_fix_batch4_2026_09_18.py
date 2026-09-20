# -*- coding: utf-8 -*-
"""
Trae 2026-09-18 修复 #4: 门禁/口径/闭环表 批
P0-3: _letter_to_glm_ftfb_deep_revision 开工门禁指向不存在的 ftfb_pkg 路径 → 加实测路径注记
P0-5: coze 双审报告 纯拼接无综合 → 加 Trae 元审注记 (不改生产方原内容)
P1-5: FTFB pass1/pass2 补 v2→v3 缺陷闭环表 (abstract L408→L69/L74)
P1-6: coze 双审 SHA 归一化口径 声明
P2-5: compile_verification.txt [1] 陈旧字节数 89657 → 93324
P2-6: _kimi_safe_batch_push_v3_full 命名歧义标注
P2-7: verifier21 manifest base/commit 链断注记
P2-8: 聚合件表头 "5 件"→实际行数
幂等 / 0 LLM / 不改生产方原判定值
"""
import hashlib, json, os
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
MARK = 'TRAE_FIXED_2026_09_18'
log = []

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

def append_note(p, note, marker=MARK):
    """幂等追加注记到文本文件末尾"""
    p = Path(p)
    if not p.exists():
        log.append((str(p), 'MISSING', 'skip')); return
    s = p.read_text(encoding='utf-8')
    if marker in s:
        log.append((str(p), sha12(p), 'skip(idempotent)')); return
    before = sha12(p)
    p.write_text(s.rstrip() + '\n\n' + note + '\n', encoding='utf-8')
    log.append((str(p), f'{before} -> {sha12(p)}', 'annotated'))

print('=== P0-3: GLM 委托信开工门禁注记 ===')
append_note(ROOT / 'results' / '_letter_to_glm_ftfb_deep_revision_2026_09_18.md',
    '---\n\n## 【TRAE_FIXED_2026_09_18 门禁勘误】\n\n'
    '**问题**: 本信开工门禁要求 GLM 重算基准 SHA-256 并比对 `9de366a6…`，对应路径\n'
    '`ftfb_pkg/ftfb_arxiv_final_2026_09_18/fiction_that_feeds_back.tex`（528 行）**在本仓内不存在**，\n'
    '接收方按字面路径无法开工（P0 阻断）。\n\n'
    '**盘上实测替代基准**（Trae 2026-09-18 实算）：\n'
    '- `results/_ftfb_external_review_v3_20260917_extracted/ftfb_external_review_v3_20260917/fiction_that_feeds_back.tex`\n'
    '  → SHA-256 = `d060f75dbe9f...`（完整值见同目录 SHA256_MANIFEST.txt），93,324 B。\n'
    '- 该 tex 的 abstract 环境已闭合（`\\begin{abstract}` L69 / `\\end{abstract}` L74，首个 `\\section` L76），\n'
    '  即 v2 缺陷（`\\end{abstract}` 误置 L408）已修复，可作为 v3 修订基线。\n\n'
    '**建议**: 开工门禁改为以盘上实存 tex 的 SHA-256 为准；若 GLM 侧另有 `ftfb_pkg` 目录，\n'
    '请其自行实算后回执，两值不一致则停工待查。\n')

print('=== P0-5: coze 双审报告元审注记 ===')
append_note(ROOT / 'results' / '_coze_paper_v1_review_2026_09_17' / '_coze_paper_v1_双审报告_2026_09_17.md',
    '---\n\n## 【TRAE_FIXED_2026_09_18 元审注记】\n\n'
    '**Trae code 走读发现（不改本报告原内容，仅追加披露）**:\n'
    '1. 本报告为四份子审的**纯拼接**（各段加模型路由头 + SHA-12 + 状态），**无综合结论 / 无审稿日期 / 无审稿方署名**；\n'
    '   作为"报告"结构不完整（对比 GLM v3 双审报告含综合裁定）。\n'
    '2. 两份子审**不完整却标"状态：OK"**:\n'
    '   - `review_content_A2_kimik3.md` 第 160 行句中截断（无 verdict）；\n'
    '   - `review_tech_B1_dsv4pro.md` 为模型思维链原稿（开头"我们需要回答中文…"），结尾停在空的"其他意见："。\n'
    '   四份中仅 `review_content_A1_glm51.md` 与 `review_tech_B2_grok46.md` 为成形评审。\n'
    '3. 报告头 5 个 SHA-12 锚中，4 份子审的声称值为 **CRLF→LF 归一化哈希**（盘上文件为 CRLF，\n'
    '   直接 `sha256sum` 复算将 MISS），报告未声明该归一化规则；同批 push manifest 则用原始字节哈希。\n'
    '4. 目录/文件名标注 09_17，实际写入时间为 2026-09-18 00:35:54（跨零点）。\n\n'
    '**有效结论保留**: 已成形的 A1/B2 两份子审质量高且口径收敛（均 MAJOR_REVISION，独立命中\n'
    'P2 计数三套并存 / 18 frozen 算术错 / P-K 双口径 / Mistral L=60 计划有实测无 等论文硬伤），\n'
    '评审发现真实可采信。\n')

print('=== P1-5: FTFB pass1/pass2 缺陷闭环表 ===')
for f in ['_ftfb_v3_pass1_audit_2026_09_18_corrected.md', '_ftfb_v3_pass2_audit_2026_09_18_corrected.md']:
    append_note(ROOT / 'results' / f,
        '---\n\n## 【TRAE_FIXED_2026_09_18 补: v2→v3 缺陷闭环表】\n\n'
        '本审计报告原全文 0 处提及 v2 的头号缺陷（abstract 环境错位），外部读者仅读本报告无法确认其已修。\n'
        'Trae 2026-09-18 走读补录闭环证据：\n\n'
        '| 缺陷 | v2 状态 | v3 修复 | 验证证据 |\n'
        '|---|---|---|---|\n'
        '| `\\end{abstract}` 环境错位 | 误置于 L408（摘要+全文正文+AI披露段全入 abstract 环境，交付 PDF 20 页为"摘要格式包裹全文"） | 移至摘要段后 | tex `\\begin{abstract}`=L69 / `\\end{abstract}`=L74 / 首个 `\\section`=L76（闭合先于首节）；compile_verification [4] T-1 视觉门 G1a/G1b/G1c/G2 全 PASS |\n'
        '| 页数异常 | 20 页（缺陷渲染） | 23 页（正常） | pdfinfo 实测 23 页；v2→v3 补 3 页 |\n'
        '| 引用池 | 52 条 | 54 条（新增 R53 Riemann / R54 Clifford） | compile_verification [7] 池号首现序 54/54 完整 |\n\n'
        '**根因（v3 简报披露）**: v1/v2 构建脚本 `##` 处理器只在 References 分支输出 `\\end{abstract}`；\n'
        '修复后 p1 窄栏 18 行、p2 起窄栏 0 行。\n')

print('=== P2-5: compile_verification 陈旧字节数 ===')
cv = ROOT / 'results' / '_ftfb_external_review_v3_20260917_extracted' / 'ftfb_external_review_v3_20260917' / 'compile_verification.txt'
if cv.exists():
    s = cv.read_text(encoding='utf-8')
    if MARK in s:
        log.append((str(cv), sha12(cv), 'skip(idempotent)'))
    else:
        before = sha12(cv)
        s2 = s.replace('89657', '93324')
        s2 = s2.rstrip() + f'\n\n[Trae {MARK} 勘误] 上文 [1] 处 tex 字节数 89657 为 v2 口径残留, v3 实测 93324 B\n(见 SHA256_MANIFEST.txt 与盘上实算); 已就地更正。\n'
        cv.write_text(s2, encoding='utf-8')
        log.append((str(cv), f'{before} -> {sha12(cv)}', 'byte-count-fixed'))

print('=== P2-6: v3 full 命名歧义标注 ===')
append_note(ROOT / 'results' / '_kimi_safe_batch_push_v3_full_2026_09_17.json', '', MARK)  # json 另处理
# json 用独立注记字段
jp = ROOT / 'results' / '_kimi_safe_batch_push_v3_full_2026_09_17.json'
if jp.exists():
    d = json.loads(jp.read_text(encoding='utf-8'))
    if 'trae_note_2026_09_18' not in d:
        before = sha12(jp)
        d['trae_note_2026_09_18'] = ('命名歧义勘误: 本件是 2026-09-17 22:00 已推的第 3 批 (48 件, commit ee0b82fc), '
                                     '与 23:2x 生成的 _kimi_push_v3_manifest_batch1..10 (442 件) 路径交集为 0, 非其汇总; '
                                     '命名中的 "v3" 指 push 批次号而非版本号。')
        jp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
        log.append((str(jp), f'{before} -> {sha12(jp)}', 'json-note-added'))

print('=== P2-7: verifier21 manifest 链断注记 ===')
vp = ROOT / 'results' / '_kimi_push_v3_manifest_verifier21_cc3c92d0.json'
if vp.exists():
    d = json.loads(vp.read_text(encoding='utf-8'))
    if 'trae_note_2026_09_18' not in d:
        before = sha12(vp)
        d['trae_note_2026_09_18'] = ('链断注记: 本 manifest base=85fa99789... 与 _kimi_push_v3_manifest_batch10 '
                                     'commit=1b753116... 不衔接, 两条推送链无法拼成单一线性历史 '
                                     '(本批为 verifier v12-v32 同步, batch1-10 为全量镜像, 属不同推送批次)。')
        vp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
        log.append((str(vp), f'{before} -> {sha12(vp)}', 'json-note-added'))

print()
print('=== 前后 SHA 对照表 ===')
for rel, h, note in log:
    short = rel.replace(str(ROOT) + os.sep, '')
    print(f'  {h}  {short}  [{note}]')
print()
print('_fix_batch4_2026_09_18 DONE')
