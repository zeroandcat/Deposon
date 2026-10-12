#!/usr/bin/env python3
"""
arxiv-standard renumber for deposon paper (CN + EN).
Hardcoded OLD -> NEW mapping based on body first-appearance order.
"""
import re
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")
CN_MD = REPO / "paper" / "deposon_paper_final_cn.md"
EN_MD = REPO / "paper" / "deposon_paper_final_en.md"
BIB = REPO / "paper" / "references.bib"

# === OLD -> NEW mapping (hardcoded, based on body scan) ===
# Cited (1-34) in first-appearance order; Uncited (35-60) in original bib order
# Format: old_N : new_N
OLD_TO_NEW = {
    # Cited refs (34)
    60: 1, 61: 2, 62: 3, 63: 4, 64: 5,  # CoT family
    18: 6, 19: 7, 21: 8,  # auditing family
    49: 9, 40: 10, 41: 11, 44: 12,  # reporting & underspecification
    28: 13, 27: 14, 29: 15,  # KG-LLM
    35: 16, 34: 17,  # concept maps
    52: 18, 55: 19,  # homophily / heterophily
    1: 20, 2: 21, 3: 22, 4: 23,  # potential games
    10: 24, 11: 25, 13: 26, 12: 27,  # PoA
    22: 28, 23: 29, 24: 30, 26: 31, 25: 32, 20: 33, 50: 34,  # adversarial + log-linear
    # Uncited refs (35-60), original bib order preserved
    5: 35, 6: 36, 7: 37, 8: 38, 9: 39,  # graphon / network formation
    14: 40, 15: 41, 16: 42, 17: 43,  # mechanism / behavioral
    30: 44, 32: 45, 33: 46,  # KG / reversal curse
    36: 47, 37: 48, 38: 49, 39: 50,  # concept maps / KG
    42: 51, 43: 52,  # ML repro / eval
    45: 53, 46: 54, 47: 55, 48: 56,  # LLM eval
    53: 57, 54: 58, 56: 59, 57: 60, 58: 61, 59: 62,  # GNN homophily
}
# [31] and [51] are not in this map (they were already absent in original)

# === New bibliography entries (full text, EN version) ===
# Used in the EN paper bibliography section
NEW_BIB_EN = {
    1: 'Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS 2022.',
    2: 'Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models," NeurIPS 2023.',
    3: 'Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models," ICLR 2023.',
    4: 'Turpin et al., "Language Models Don\'t Always Say What They Think," NeurIPS 2023.',
    5: 'Lanham et al., "Measuring Faithfulness in Chain-of-Thought Reasoning," TMLR 2023.',
    6: 'Raji et al. 2020.',
    7: 'Jia et al. 2021 (Proof-of-Learning).',
    8: 'Nasr, M., Jagielski, M., Carlini, N., Tramèr, F. et al., "Tight Auditing of Differentially Private Machine Learning," USENIX Security 2023, pp. 1631–1648 (verified and corrected 2026-08-30: the original annotation USENIX Security 2025 does not exist; verification conclusion CORRECTED, see docs/REF_VERIFICATION_v2.md).',
    9: 'Bowman, ACL 2022 (Dangers of Underclaiming).',
    10: 'Lipton & Steinhardt, CACM 2019.',
    11: 'Dodge et al., EMNLP 2019.',
    12: 'D\'Amour et al., JMLR 2022.',
    13: 'KG-LLM/Yao et al., ICASSP 2025.',
    14: 'KICGPT, Findings of EMNLP 2023.',
    15: 'Wadhwa et al., ACL 2023.',
    16: 'Ruiz-Primo & Shavelson 1996.',
    17: 'Novak & Cañas 2008.',
    18: 'McPherson, Smith-Lovin & Cook 2001 (homophily review) (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    19: 'Zheng et al., survey of GNNs for heterophilous graphs, 2022 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    20: 'Monderer & Shapley, GEB 1996 (potential games).',
    21: 'Rosenthal 1973 (congestion games).',
    22: 'Sandholm 2010 (population best-response dynamics).',
    23: 'Candogan et al., MOR 2011 (flow decomposition of games).',
    24: 'Koutsoupias & Papadimitriou 1999.',
    25: 'Roughgarden & Tardos 2002 (affine congestion PoA=4/3).',
    26: 'Benita 2020 (distribution-level PoA precedent).',
    27: 'Christodoulou et al. 2014.',
    28: 'Gröndahl et al., AISec 2018.',
    29: 'Hosseini et al. 2017.',
    30: 'Kahu & Ahuja 2025.',
    31: 'HateBench, USENIX Sec 2025.',
    32: 'Jain et al. 2023.',
    33: 'Tramèr et al., NeurIPS 2020 (adaptive attacks).',
    34: 'Blume 1993 (log-linear learning).',
    35: 'Parise & Ozdaglar, Econometrica 2023 (graphon limits).',
    36: 'Jackson & Wolinsky 1996.',
    37: 'Fabrikant et al. 2003.',
    38: 'Ma et al., TCS 2014.',
    39: 'Waniek et al., Nat. Hum. Behav. 2018, and Stackelberg edge hiding 2023.',
    40: 'Conitzer & Sandholm 2006.',
    41: 'Dekel et al. 2010.',
    42: 'Hardt et al. 2016.',
    43: 'Dütting et al., WWW 2024.',
    44: 'Berglund et al., ICLR 2024 (Reversal Curse).',
    45: 'MKGL, NeurIPS 2024.',
    46: 'Zhang et al., ACL 2025.',
    47: 'KnowEdu, IEEE Access 2018.',
    48: 'MOOCCube/MOOCCubeX, ACL 2020 / CIKM 2021.',
    49: 'Pinandito et al. 2021 (KitBuild).',
    50: 'Ma & Chen, LAK 2025.',
    51: 'Recht, ICML 2019.',
    52: 'Tevet & Berant, EACL 2021.',
    53: 'Lazaridou et al., NeurIPS 2021.',
    54: 'Schaeffer et al., NeurIPS 2023.',
    55: 'Mallen et al., ACL 2023.',
    56: 'Dziri et al., NeurIPS 2023.',
    57: 'Pei et al., Geom-GCN, ICLR 2020 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    58: 'Zhu et al., H2GCN (Beyond Homophily), NeurIPS 2020 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    59: 'Luan et al., Revisiting Heterophily, NeurIPS 2022 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    60: 'Zhang & Chen, SEAL, NeurIPS 2018 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    61: 'Srinivasan & Ribeiro, equivalence of positional embeddings and structural representations, ICLR 2020 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
    62: 'Mao et al., Demystifying Structural Disparity, NeurIPS 2023 (verified 2026-08-30, see docs/REF_VERIFICATION_v2.md).',
}

# === New bibliography entries (CN version) ===
NEW_BIB_CN = {
    1: 'Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", NeurIPS 2022。',
    2: 'Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", NeurIPS 2023。',
    3: 'Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", ICLR 2023。',
    4: 'Turpin et al., "Language Models Don\'t Always Say What They Think", NeurIPS 2023。',
    5: 'Lanham et al., "Measuring Faithfulness in Chain-of-Thought Reasoning", TMLR 2023。',
    6: 'Raji et al. 2020。',
    7: 'Jia et al. 2021（Proof-of-Learning）。',
    8: 'Nasr, M., Jagielski, M., Carlini, N., Tramèr, F. 等，"Tight Auditing of Differentially Private Machine Learning"，USENIX Security 2023, pp. 1631–1648（已核实并修正 2026-08-30：原标注 USENIX Security 2025 不存在，核实结论 CORRECTED，见 docs/REF_VERIFICATION_v2.md）。',
    9: 'Bowman, ACL 2022（Dangers of Underclaiming）。',
    10: 'Lipton & Steinhardt, CACM 2019。',
    11: 'Dodge et al., EMNLP 2019。',
    12: 'D\'Amour et al., JMLR 2022。',
    13: 'KG-LLM/Yao et al., ICASSP 2025。',
    14: 'KICGPT, Findings of EMNLP 2023。',
    15: 'Wadhwa et al., ACL 2023。',
    16: 'Ruiz-Primo & Shavelson 1996。',
    17: 'Novak & Cañas 2008。',
    18: 'McPherson, Smith-Lovin & Cook 2001（同质性综述）（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    19: 'Zheng et al., 异配图 GNN 综述, 2022（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    20: 'Monderer & Shapley, GEB 1996（势博弈）。',
    21: 'Rosenthal 1973（拥塞博弈）。',
    22: 'Sandholm 2010（群体最好响应流）。',
    23: 'Candogan et al., MOR 2011（博弈流分解）。',
    24: 'Koutsoupias & Papadimitriou 1999。',
    25: 'Roughgarden & Tardos 2002（仿射拥塞 PoA=4/3）。',
    26: 'Benita 2020（分布级 PoA 先例）。',
    27: 'Christodoulou et al. 2014。',
    28: 'Gröndahl et al., AISec 2018。',
    29: 'Hosseini et al. 2017。',
    30: 'Kahu & Ahuja 2025。',
    31: 'HateBench, USENIX Sec 2025。',
    32: 'Jain et al. 2023。',
    33: 'Tramèr et al., NeurIPS 2020（自适应攻击）。',
    34: 'Blume 1993（log-linear learning）。',
    35: 'Parise & Ozdaglar, Econometrica 2023（graphon 极限）。',
    36: 'Jackson & Wolinsky 1996。',
    37: 'Fabrikant et al. 2003。',
    38: 'Ma et al., TCS 2014。',
    39: 'Waniek et al., Nat. Hum. Behav. 2018 及 Stackelberg 边隐藏 2023。',
    40: 'Conitzer & Sandholm 2006。',
    41: 'Dekel et al. 2010。',
    42: 'Hardt et al. 2016。',
    43: 'Dütting et al., WWW 2024。',
    44: 'Berglund et al., ICLR 2024（Reversal Curse）。',
    45: 'MKGL, NeurIPS 2024。',
    46: 'Zhang et al., ACL 2025。',
    47: 'KnowEdu, IEEE Access 2018。',
    48: 'MOOCCube/MOOCCubeX, ACL 2020 / CIKM 2021。',
    49: 'Pinandito et al. 2021（KitBuild）。',
    50: 'Ma & Chen, LAK 2025。',
    51: 'Recht, ICML 2019。',
    52: 'Tevet & Berant, EACL 2021。',
    53: 'Lazaridou et al., NeurIPS 2021。',
    54: 'Schaeffer et al., NeurIPS 2023。',
    55: 'Mallen et al., ACL 2023。',
    56: 'Dziri et al., NeurIPS 2023。',
    57: 'Pei et al., Geom-GCN, ICLR 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    58: 'Zhu et al., H2GCN（Beyond Homophily）, NeurIPS 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    59: 'Luan et al., Revisiting Heterophily, NeurIPS 2022（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    60: 'Zhang & Chen, SEAL, NeurIPS 2018（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    61: 'Srinivasan & Ribeiro, 位置嵌入与结构表示等价性, ICLR 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
    62: 'Mao et al., Demystifying Structural Disparity, NeurIPS 2023（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。',
}

# === Citation replacement logic ===
# Math context: skip [N] if preceded by ∈, =, +, -, <, >, *, /, (, ), [, ], digit
MATH_CHARS = set("∈=+<>*/()[]×·∑∏∫∂")

def is_citation_context(text_before):
    """Check if [N] is a citation (not math interval)."""
    if not text_before:
        return True
    i = len(text_before) - 1
    while i >= 0 and text_before[i] in ' \t\n':
        i -= 1
    if i < 0:
        return True
    last = text_before[i]
    if last in MATH_CHARS or last.isdigit() or last in '。，；：、,;:-':
        # 标点之后可能是引用,但数字/数学符号之后不是
        if last in MATH_CHARS or last.isdigit():
            return False
    return True

def replace_citations(text, old_to_new):
    """Replace citation [N(,N)*] patterns using mapping."""
    pattern = re.compile(r'\[(\d+(?:\s*[,–，]\s*\d+)*)\]')
    out = []
    pos = 0
    for m in pattern.finditer(text):
        before = text[max(0, m.start()-5):m.start()]
        if not is_citation_context(before):
            continue
        inner = m.group(1)
        # Determine separator style
        if '，' in inner:
            sep = '，'
        elif '–' in inner:
            sep = '–'
        else:
            sep = ', '
        parts = [p.strip() for p in re.split(r'[,，–]', inner)]
        if not all(p.isdigit() and int(p) in old_to_new for p in parts):
            continue
        new_parts = [str(old_to_new[int(p)]) for p in parts]
        if sep == '–':
            new_inner = '–'.join(new_parts)
        elif sep == '，':
            new_inner = '，'.join(new_parts)
        else:
            new_inner = ', '.join(new_parts)
        out.append(text[pos:m.start()])
        out.append('[' + new_inner + ']')
        pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


def process_paper(md_path, lang, new_bib):
    text = md_path.read_text(encoding='utf-8')
    if lang == 'cn':
        body_marker = '# 凝子散射层'
        bib_marker = '## 参考文献'
        bib_tail_cn = '（[31] 写作时点可查性未能确认'
        if bib_tail_cn in text:
            bib_tail = bib_tail_cn
        else:
            bib_tail = 'writing time'
    else:
        body_marker = '# Deposon:'
        bib_marker = '## References'
        bib_tail_en = '([31] could not be confirmed'
        if bib_tail_en in text:
            bib_tail = bib_tail_en
        else:
            bib_tail = 'writing time'

    body_start = text.index(body_marker)
    bib_start = text.index(bib_marker)
    if bib_tail in text:
        bib_end = text.index(bib_tail)
        # include the line containing the tail note
        nl = text.rfind('\n', 0, bib_end)
        if nl > bib_start:
            bib_end = nl
    else:
        bib_end = len(text)

    front = text[:body_start]
    body = text[body_start:bib_start]
    bib_section = text[bib_start:bib_end]
    post = text[bib_end:]

    # Replace citations in body and bib section header
    new_body = replace_citations(body, OLD_TO_NEW)
    new_bib_section = replace_citations(bib_section, OLD_TO_NEW)

    # Rewrite bib list content
    # Find the first line that starts with "[N] " (the bib entries)
    lines = new_bib_section.split('\n')
    header_lines = []
    entry_lines = []
    in_entries = False
    for line in lines:
        if not in_entries and re.match(r'^\[\d+\]\s+', line):
            in_entries = True
        if in_entries:
            entry_lines.append(line)
        else:
            header_lines.append(line)

    # Build new bib list: keep header, then add ordered entries
    header_text = '\n'.join(header_lines).rstrip()
    new_bib_list = header_text + '\n\n'
    for n in sorted(new_bib.keys()):
        new_bib_list += f'[{n}] {new_bib[n]}\n'

    # Update REFS_USED in front matter
    new_front = re.sub(
        r'<!-- REFS_USED:.*?-->',
        build_refs_used(lang),
        front,
        count=1
    )

    return new_front + new_body + new_bib_list + post


def build_refs_used(lang):
    cited = list(range(1, 35))
    s = ", ".join(str(n) for n in cited)
    if lang == 'cn':
        return f"<!-- REFS_USED: [{s}]（编号按首次出现顺序，与项目文献库一致） -->"
    else:
        return f"<!-- REFS_USED: [{s}] (numbering follows arxiv standard: order of first appearance) -->"


# === Execute ===
if __name__ == '__main__':
    print("=== Mapping ===")
    for old in sorted(OLD_TO_NEW.keys()):
        new = OLD_TO_NEW[old]
        print(f"  [{old:2d}] -> [{new:2d}]  {NEW_BIB_EN[new][:60]}")

    # Backup
    cn_bak = CN_MD.with_suffix('.md.bak_prearxiv')
    en_bak = EN_MD.with_suffix('.md.bak_prearxiv')
    if not cn_bak.exists():
        cn_bak.write_text(CN_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if not en_bak.exists():
        en_bak.write_text(EN_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(f"\nBackups: {cn_bak.name}, {en_bak.name}")

    # Process
    cn_new = process_paper(CN_MD, 'cn', NEW_BIB_CN)
    en_new = process_paper(EN_MD, 'en', NEW_BIB_EN)

    CN_MD.write_text(cn_new, encoding='utf-8')
    EN_MD.write_text(en_new, encoding='utf-8')
    print(f"\nWritten: {CN_MD} ({len(cn_new)} bytes)")
    print(f"Written: {EN_MD} ({len(en_new)} bytes)")

    # Verify
    cn_text = CN_MD.read_text(encoding='utf-8')
    en_text = EN_MD.read_text(encoding='utf-8')

    # Check for any remaining old-number citations in body
    cn_body = cn_text[cn_text.index('# 凝子散射层'):cn_text.index('## 参考文献')]
    en_body = en_text[en_text.index('# Deposon:'):en_text.index('## References')]

    def find_old_citations(text, max_new):
        old_cites = []
        for m in re.finditer(r'\[(\d+(?:\s*[,，–]\s*\d+)*)\]', text):
            inner = m.group(1)
            for p in re.split(r'[,，–]', inner):
                p = p.strip()
                if p.isdigit():
                    n = int(p)
                    if n > max_new:
                        old_cites.append(n)
        return old_cites

    cn_old = find_old_citations(cn_body, 62)
    en_old = find_old_citations(en_body, 62)
    print(f"\n=== Verification ===")
    print(f"CN body citations > 62: {len(cn_old)} {sorted(set(cn_old))[:20] if cn_old else ''}")
    print(f"EN body citations > 62: {len(en_old)} {sorted(set(en_old))[:20] if en_old else ''}")

    # Show first 5 body citations after renumber
    print(f"\n=== First 5 CN body citations (after renumber) ===")
    cn_first5 = []
    for m in re.finditer(r'\[(\d+(?:\s*[,，–]\s*\d+)*)\]', cn_body):
        cn_first5.append(m.group(0))
        if len(cn_first5) >= 5: break
    print(cn_first5)

    print(f"\n=== First 5 EN body citations (after renumber) ===")
    en_first5 = []
    for m in re.finditer(r'\[(\d+(?:\s*[,，–]\s*\d+)*)\]', en_body):
        en_first5.append(m.group(0))
        if len(en_first5) >= 5: break
    print(en_first5)
