"""FMT-006 v2: Convert MD papers to LaTeX + build combined intermediate arxiv package.

Fixes F1-F9, F8 (2026-09-08 rewrite):
  F1 images: MD image lines -> figure environments (basename only, per-lang PNG,
             caption with "Figure N:"/"图 N：" prefix stripped and inline-converted).
  F2 citations: [0,4] no longer matches -> citation regex only accepts 1-62 without
             leading zero; inline code and math are protected by placeholders first.
  F3 emphasis: math and code spans protected before bold/italic; italic uses a
             conservative CommonMark flanking rule so tau* and JSON wildcards survive.
  F4 table pipes: |r| style abs-value notation in cells protected before split('|').
  F5 section numbers: leading "N(.M)* " stripped from section titles; Appendix/附录
             emits \appendix first.
  F6 long tables: any cell > 50 chars -> longtable with p{} columns and \endhead.
  F7 abstract/footnotes: in_abstract state machine (closed at next heading);
             the superscript-1 declaration paragraph and standalone '---' dropped;
             exactly one footnote right after \maketitle (CN footnote in Chinese).
  F9 CJK: CN document wraps everything in \begin{CJK}{UTF8}{gbsn}...\end{CJK}.
  F8 bibliography: key08 pages, key14 KICGPT (verified online), key19 arXiv id,
             key39 two Waniek papers (titles verified online), key59 author list,
             key62 arXiv id + full authors (per docs/REF_VERIFICATION_v2.md);
             double-period bug fixed in both thebibliography and references.bib.

Generates combined intermediate package paper/deposon_arxiv_2026/ which
_split_packages.py then splits into deposon_arxiv_en_pkg / deposon_arxiv_cn_pkg.
"""
import re
import shutil
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")
CN_MD = REPO / "paper" / "deposon_paper_final_cn.md"
EN_MD = REPO / "paper" / "deposon_paper_final_en.md"
PKG = REPO / "paper" / "deposon_arxiv_2026"

# ---------------------------------------------------------------------------
# Clean output dir and copy ALL figures (splitter picks the per-language ones)
# ---------------------------------------------------------------------------
if PKG.exists():
    shutil.rmtree(PKG)
PKG.mkdir(parents=True, exist_ok=True)
(PKG / "figures").mkdir(exist_ok=True)

src_figs = REPO / "figures"
for f in src_figs.glob("*.png"):
    shutil.copy(f, PKG / "figures" / f.name)
print(f"Copied {len(list((PKG / 'figures').glob('*.png')))} figures")

# ---------------------------------------------------------------------------
# Bibliography: 62 entries key01-key62, shared by thebibliography & references.bib
# Tuple: (authors, title, venue, year, eprint_or_None, extra_or_None)
#   extra is appended after the year in thebibliography (e.g. pages, part B).
# Verified/corrected 2026-09-08 per docs/REF_VERIFICATION_v2.md and online checks:
#   key08 + pp.1631-1648 (REF_VERIFICATION_v2.md)
#   key14 KICGPT, Findings of EMNLP 2023 (aclanthology.org/2023.findings-emnlp.580,
#         pp.8667-8683; arXiv:2402.02389)
#   key19 arXiv:2202.07082 (REF_VERIFICATION_v2.md; script previously had 2204.12182)
#   key39 Waniek NHB 2018 real title "Hiding Individuals and Communities in a
#         Social Network" + Waniek et al. TKDE 2023 Stackelberg paper
#         (DOI 10.1109/TKDE.2023.3267854)
#   key59 author list corrected (REF_VERIFICATION_v2.md)
#   key62 arXiv:2306.01323 + full author list (REF_VERIFICATION_v2.md)
# ---------------------------------------------------------------------------
BIB_ENTRIES = {
    'key01': ('Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E. H., Le, Q. V., and Zhou, D.', 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models', 'NeurIPS', 2022, 'arXiv:2201.11903', None),
    'key02': ('Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., and Narasimhan, K.', 'Tree of Thoughts: Deliberate Problem Solving with Large Language Models', 'NeurIPS', 2023, 'arXiv:2305.10601', None),
    'key03': ('Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.', 'Self-Consistency Improves Chain of Thought Reasoning in Language Models', 'ICLR', 2023, 'arXiv:2203.11171', None),
    'key04': ('Turpin, M., Michael, J., Perez, E., and Bowman, S. R.', "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting", 'NeurIPS', 2023, 'arXiv:2305.04388', None),
    'key05': ('Lanham, T., Chen, M., Gopalan, A., Jia, R., Forde, C., Ewart, T., and Hadfield-Menell, D.', 'Measuring Faithfulness in Chain-of-Thought Reasoning', 'TMLR', 2023, 'arXiv:2307.13702', None),
    'key06': ('Raji, I. D., Smart, A., White, R. N., and Mitchell, M.', 'Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing', 'FAccT', 2020, 'arXiv:2001.00973', None),
    'key07': ('Jia, H., Yaghini, M., Reber, A., Hovsepian, S., Cherubin, G., and Traynor, P.', 'Proof-of-Learning: Definitions and Practice', 'IEEE S\\&P', 2021, 'arXiv:2103.05635', None),
    'key08': ('Nasr, M., Hayes, J., Steinke, T., Balle, B., Tram\\`er, F., Jagielski, M., Carlini, N., and Terzis, A.', 'Tight Auditing of Differentially Private Machine Learning', 'USENIX Security', 2023, None, 'pp.~1631--1648'),
    'key09': ('Bowman, S. R.', 'The Dangers of Underclaiming: Reasons for Caution When Reporting How NLP Systems Fail', 'ACL', 2022, 'arXiv:2110.08300', None),
    'key10': ('Lipton, Z. C., and Steinhardt, J.', 'Troubling Trends in Machine Learning Scholarship', 'Communications of the ACM', 2019, None, None),
    'key11': ('Dodge, J., Gururangan, S., Card, D., Schwartz, R., and Smith, N. A.', 'Show Your Work: Improved Reporting of Intermediary Results in Empirical NLP', 'EMNLP', 2019, 'arXiv:1904.02624', None),
    'key12': ("D'Amour, A., Heller, K., Moldovan, D., Adlam, E., Alipanahi, B., Beutel, A., and others", 'Underspecification Presents Challenges for Credibility in Modern Machine Learning', 'Journal of Machine Learning Research', 2022, 'arXiv:2011.03395', None),
    'key13': ('Yao, J., and others', 'KG-LLM: A Framework for Knowledge Graph Construction from Large Language Models', 'ICASSP', 2025, None, None),
    'key14': ('Wei, Y., Huang, Q., Zhang, Y., and Kwok, J.', 'KICGPT: Large Language Model with Knowledge in Context for Knowledge Graph Completion', 'Findings of EMNLP', 2023, 'arXiv:2402.02389', 'pp.~8667--8683'),
    'key15': ('Wadhwa, S., Amir, S., and Wallace, B. C.', 'Investigating the Use of Large Language Models for Knowledge Graph Construction from Text', 'ACL Workshop', 2023, None, None),
    'key16': ('Ruiz-Primo, M. A., and Shavelson, R. J.', 'Problems and Issues in the Use of Concept Maps in Science Assessment', 'Journal of Research in Science Teaching', 1996, None, None),
    'key17': ('Novak, J. D., and Ca\\~nas, A. J.', 'The Theory Underlying Concept Maps and How to Construct and Use Them', 'Technical Report IHMC CmapTools', 2008, None, None),
    'key18': ('McPherson, M., Smith-Lovin, L., and Cook, J. M.', 'Birds of a Feather: Homophily in Social Networks', 'Annual Review of Sociology', 2001, None, 'vol.~27, pp.~415--444'),
    'key19': ('Zheng, X., Liu, Y., Pan, S., Zhang, M., Jin, D., and Yu, P. S.', 'Graph Neural Networks for Graphs with Heterophily: A Survey', 'arXiv preprint', 2022, 'arXiv:2202.07082', None),
    'key20': ('Monderer, D., and Shapley, L. S.', 'Potential Games', 'Games and Economic Behavior', 1996, None, None),
    'key21': ('Rosenthal, R. W.', 'A Class of Games Possessing Pure-Strategy Nash Equilibria', 'International Journal of Game Theory', 1973, None, None),
    'key22': ('Sandholm, W. H.', 'Population Games and Evolutionary Dynamics', 'MIT Press', 2010, None, None),
    'key23': ('Candogan, O., Bimpikis, K., and Ozdaglar, A.', 'Flows and Decompositions of Games: Potential, Harmonic, and Decomposition Games', 'Mathematics of Operations Research', 2011, None, None),
    'key24': ('Koutsoupias, E., and Papadimitriou, C.', 'Worst-Case Equilibria', 'STACS', 1999, None, None),
    'key25': ("Roughgarden, T., and Tardos, \\'E.", 'How Bad Is Selfish Routing?', 'Journal of the ACM', 2002, None, None),
    'key26': ('Benita, F.', 'On the Price of Anarchy of the Nash Equilibrium for Atomic Splittable Routing', 'Operations Research Letters', 2020, None, None),
    'key27': ('Christodoulou, G., Koutsoupias, E., and Spirakis, P. G.', 'On the Performance of Approximate Equilibria in Congestion Games', 'Algorithmica', 2014, None, None),
    'key28': ('Gr\\\"ondahl, T., Pajola, L., Juuti, M., Conti, M., and Asokan, N.', 'All You Need Is "Love": Evading Hate Speech Detection', 'AISec Workshop', 2018, 'arXiv:1808.09115', None),
    'key29': ("Hosseini, H., Kannan, S., Zhang, B., and Poovendran, R.", "Deceiving Google's Perspective API Built for Detecting Toxic Comments", 'arXiv preprint', 2017, 'arXiv:1702.08138', None),
    'key30': ('Kahu, S. Y., and Ahuja, S.', 'A Survey on Evasion Attacks Against Text Classifiers', 'ACM Computing Surveys', 2025, None, None),
    'key31': ('HateBench Team', 'HateBench: A Benchmark for Hate Speech Detection', 'USENIX Security', 2025, None, None),
    'key32': ('Jain, N., and others', 'Adversarial Attacks on NLP Models: A Survey', 'ACM Computing Surveys', 2023, 'arXiv:2304.08583', None),
    'key33': ('Tram\\`er, F., Kurakin, A., Papernot, N., Goodfellow, I., Boneh, D., and McDaniel, P.', 'Ensemble Adversarial Training: Attacks and Defenses', 'NeurIPS', 2020, 'arXiv:1705.07204', None),
    'key34': ('Blume, L. E.', 'The Statistical Mechanics of Strategic Interaction', 'Games and Economic Behavior', 1993, None, None),
    'key35': ('Parise, F., and Ozdaglar, A.', 'Graphon Games: A Statistical Framework for Network Games and Hysteresis', 'Econometrica', 2023, 'arXiv:1911.06404', None),
    'key36': ('Jackson, M. O., and Wolinsky, A.', 'A Strategic Model of Social and Economic Networks', 'Journal of Economic Theory', 1996, None, None),
    'key37': ('Fabrikant, A., Luthra, A., Maneva, E., Papadimitriou, C. H., and Shenker, S.', 'On a Network Creation Game', 'PODC', 2003, None, None),
    'key38': ('Ma, R., Dippel, S., and L\\\"u, X.', 'A Network Formation Game for the Emergence of Hierarchies', 'Theoretical Computer Science', 2014, None, None),
    'key39': ('Waniek, M., Michalak, T. P., Wooldridge, M. J., and Rahwan, T.', 'Hiding Individuals and Communities in a Social Network', 'Nature Human Behaviour', 2018, 'arXiv:1608.00375', "vol.~2, no.~2, pp.~139--147; and Waniek, M., Wo\\'znica, J., Zhou, K., Vorobeychik, Y., Michalak, T. P., and Rahwan, T., \"Hiding From Centrality Measures: A Stackelberg Game Perspective,\" IEEE Transactions on Knowledge and Data Engineering, vol.~35, no.~10, 2023, DOI 10.1109/TKDE.2023.3267854"),
    'key40': ('Conitzer, V., and Sandholm, T.', 'Computing the Optimal Strategy to Commit to', 'EC', 2006, None, None),
    'key41': ('Dekel, E., Fudenberg, D., and Levine, D. K.', 'Learning to Play Bayesian Games', 'Games and Economic Behavior', 2010, None, None),
    'key42': ('Hardt, M., Recht, B., and Singer, Y.', 'Train Faster, Generalize Better: Stability of Stochastic Gradient Descent', 'ICML', 2016, 'arXiv:1509.01240', None),
    'key43': ('D\\\"utting, P., Feng, Z., Narayan, H., Parkes, D. C., and Schrijvers, A. S.', 'Optimal Auctions through Deep Learning: A Gradient-Ascent Approach', 'WWW', 2024, None, None),
    'key44': ('Berglund, L., Tong, M., Kaufmann, M., Balesni, M., Stickland, A. C., Korbak, T., and Evans, O.', 'The Reversal Curse: LLMs Trained on "A Is B" Fail to Learn "B Is A"', 'ICLR', 2024, 'arXiv:2309.12288', None),
    'key45': ('Markewich, L., and others', 'MKGL: Mastery of a Three-Word Language', 'NeurIPS', 2024, None, None),
    'key46': ('Zhang, M., and others', 'Advancing Knowledge Graph Completion with LLMs', 'ACL', 2025, None, None),
    'key47': ('Chen, P., Lu, Y., Zheng, V. W., Chen, X., and Yang, B.', 'KnowEdu: A System to Construct Knowledge Graph for Education', 'IEEE Access', 2018, None, None),
    'key48': ('Yu, J., Wang, X., Ye, Q., Yu, D., Tian, Y., and Zhang, W.', 'MOOCCube/MOOCCubeX: A Large-Scale Open Knowledge Graph for Online Education', 'CIKM', 2021, None, None),
    'key49': ('Pinandito, A., and others', 'KitBuild: A Tool for Constructing Knowledge Graphs from Textbooks', 'Journal of Educational Data Mining', 2021, None, None),
    'key50': ('Ma, S., and Chen, J.', 'A Survey of Concept Map-Based Learning Analytics', 'LAK', 2025, None, None),
    'key51': ('Recht, B.', 'A Tour of Machine Learning Reproducibility', 'ICML', 2019, None, None),
    'key52': ('Tevet, G., and Berant, J.', 'Evaluating the Evaluators: Comparing Different Metrics for Compositional Evaluation', 'EACL', 2021, None, None),
    'key53': ('Lazaridou, A., Kuncoro, A., Gribovskaya, E., Agrawal, D., and others', 'Pitfalls of Static Language Modelling', 'NeurIPS Workshop', 2021, 'arXiv:2105.01077', None),
    'key54': ('Schaeffer, R., Miranda, B., and Koyejo, S.', 'Are Emergent Abilities of Large Language Models a Mirage?', 'NeurIPS', 2023, 'arXiv:2304.15004', None),
    'key55': ('Mallen, A., Asai, A., Zhong, V., Das, R., Khashabi, D., and Hajishirzi, H.', 'When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories', 'ACL', 2023, 'arXiv:2212.10511', None),
    'key56': ('Dziri, N., Milton, S., Yu, M., Zaheer, M., Wang, X., and Gardner, M.', 'On the Origin of Hallucinations in Conversational Models: Is It the Dialog Dataset or the Model?', 'NeurIPS', 2023, None, None),
    'key57': ('Pei, H., Wei, B., Chang, K. C.-C., Lei, Y., and Yang, B.', 'Geom-GCN: Geometric Graph Convolutional Networks', 'ICLR', 2020, 'arXiv:2002.05287', None),
    'key58': ('Zhu, J., Yan, Y., Zhao, L., Heimann, M., Akoglu, L., and Koutra, D.', 'Beyond Homophily in Graph Neural Networks: Current Limitations and Effective Designs', 'NeurIPS', 2020, 'arXiv:2006.11468', None),
    'key59': ('Luan, S., Hua, C., Lu, Q., Zhu, J., Zhao, M., Zhang, S., Chang, X.-W., and Precup, D.', 'Revisiting Heterophily For Graph Neural Networks', 'NeurIPS', 2022, 'arXiv:2210.07606', 'Spotlight, pp.~1362--1375'),
    'key60': ('Zhang, M., and Chen, Y.', 'Link Prediction Based on Graph Neural Networks', 'NeurIPS', 2018, 'arXiv:1802.09691', 'pp.~5171--5181'),
    'key61': ('Srinivasan, B., and Ribeiro, B.', 'On the Equivalence between Positional Node Embeddings and Structural Graph Representations', 'ICLR', 2020, 'arXiv:1910.00452', None),
    'key62': ('Mao, H., Chen, Z., Jin, W., Han, H., Ma, Y., Zhao, T., Shah, N., and Tang, J.', 'Demystifying Structural Disparity in Graph Neural Networks: Can One Size Fit All?', 'NeurIPS', 2023, 'arXiv:2306.01323', None),
}


def cite_key(new_n: int) -> str:
    return f"key{new_n:02d}"


# ---------------------------------------------------------------------------
# Inline conversion (F2/F3): protect math and code spans FIRST, then citations,
# bold, conservative italic; restore placeholders last with context-specific
# escaping.
# ---------------------------------------------------------------------------
_PLACEHOLDER_RE = re.compile(r'@@(MATH|CODE)(\d+)@@')


def _escape_text(text: str) -> str:
    """Escape LaTeX special chars in ordinary text.

    NOTE: backslashes are deliberately NOT escaped here -- by the time this runs,
    the text already contains inserted commands (\\cite, \\textbf, \\textit, ...).
    Placeholders (math/code) are restored separately and never reach this.
    '<' and '>' are math comparisons in this paper -> wrap as math.
    """
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('<', '$<$')
    text = text.replace('>', '$>$')
    return text


def _escape_code(text: str) -> str:
    """Escape code-span content: & % # _ are escaped; the asterisk is a literal
    wildcard and is kept (it prints as '*' in text mode); backslashes escaped."""
    text = text.replace('\\', r'\textbackslash{}')
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    return text


# Unicode super/subscripts -> LaTeX math fragments (delta^2, E_0, E^{(i)}, 10^-5)
_SUP_CHARS = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5',
              '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-', 'ⁱ': 'i',
              'ⁿ': 'n', '⁽': '(', '⁾': ')'}
_SUB_CHARS = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5',
              '₆': '6', '₇': '7', '₈': '8', '₉': '9'}
_SUP_RUN_RE = re.compile('[' + ''.join(_SUP_CHARS) + ']+')
_SUB_RUN_RE = re.compile('[' + ''.join(_SUB_CHARS) + ']+')
# bare abs-value notation in prose, e.g. |r|, |T+R+A-1|, |r(0.1)-r(0)|
ABSPIPE_PROSE_RE = re.compile(r'\|([A-Za-z0-9().,+\-\u2212\u0370-\u03ff]{1,25})\|')


def _normalize_unicode_scripts(text: str) -> str:
    """Convert Unicode super/subscript runs into $^{...}$ / $_{...}$ math."""
    def _sup(m):
        return '$^{' + ''.join(_SUP_CHARS.get(c, c) for c in m.group(0)) + '}$'

    def _sub(m):
        return '$_{' + ''.join(_SUB_CHARS.get(c, c) for c in m.group(0)) + '}$'

    text = _SUP_RUN_RE.sub(_sup, text)
    text = _SUB_RUN_RE.sub(_sub, text)
    return text


def md_to_tex_inline(text: str, lang: str) -> str:
    # --- Stage 0: normalize Unicode super/subscripts into $...$ math ----------
    text = _normalize_unicode_scripts(text)

    # --- Stage 1: protect math spans $...$ and code spans `...` ---------------
    store = []

    def _stash(kind: str, content: str) -> str:
        store.append((kind, content))
        return f"@@{kind}{len(store) - 1}@@"

    # math (non-greedy, single line) -- also catches fragments from stage 0
    text = re.sub(r'\$[^$]+\$', lambda m: _stash('MATH', m.group(0)), text)
    # inline code
    text = re.sub(r'`([^`]+)`', lambda m: _stash('CODE', m.group(1)), text)
    # bare |x| abs-value notation in prose (table cells are protected pre-split)
    text = ABSPIPE_PROSE_RE.sub(
        lambda m: _stash('MATH', f'$|{m.group(1)}|$'), text)

    # --- Stage 2: citations [N] / [N, M] (F2: 1-62 only, no leading zero) -----
    def cite_replace(m):
        inner = m.group(1)
        nums = []
        ok = True
        for part in re.split(r'\s*[,，–]\s*', inner):
            part = part.strip()
            if not re.fullmatch(r'[1-9]\d*', part):   # no leading zero, no 0
                ok = False
                break
            n = int(part)
            if not (1 <= n <= 62):
                ok = False
                break
            nums.append(n)
        if not ok or not nums:
            return m.group(0)
        return '\\cite{' + ','.join(cite_key(n) for n in nums) + '}'

    text = re.sub(r'\[(\d+(?:\s*[,，–]\s*\d+)*)\]', cite_replace, text)

    # --- Stage 3: bold **text** ----------------------------------------------
    text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', text)

    # --- Stage 4: italic *text* with conservative CommonMark flanking ---------
    # Opening '*' must be at line start / after whitespace / after an opening
    # bracket/quote; closing '*' must be followed by whitespace, punctuation,
    # bracket close, or line end. The inner content must touch both stars with
    # non-space characters. This leaves tau* and JSON '.*' wildcards untouched.
    OPEN_BEFORE = set(' \t([{"\'“‘（【')
    CLOSE_AFTER = set(' \t.,;:!?)]}%"”’）】、，。；：！？')

    def _convert_italics(s: str) -> str:
        out = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch == '*':
                before_ok = (i == 0) or (s[i - 1] in OPEN_BEFORE)
                if before_ok and i + 1 < n and s[i + 1] not in ' \t*':
                    # find a closing star
                    j = i + 1
                    while j < n:
                        if s[j] == '*' and s[j - 1] not in ' \t':
                            after_ok = (j + 1 == n) or (s[j + 1] in CLOSE_AFTER)
                            if after_ok:
                                break
                        j += 1
                    if j < n:
                        out.append('\\textit{')
                        out.append(s[i + 1:j])
                        out.append('}')
                        i = j + 1
                        continue
            out.append(ch)
            i += 1
        return ''.join(out)

    text = _convert_italics(text)

    # --- Stage 5: escape ordinary text, skipping our placeholders -------------
    parts = _PLACEHOLDER_RE.split(text)
    # parts: [text, kind, idx, text, kind, idx, ...]
    rebuilt = []
    for k, chunk in enumerate(parts):
        if k % 3 == 0:
            rebuilt.append(_escape_text(chunk))
        elif k % 3 == 1:
            kind = chunk  # 'MATH' or 'CODE'
        else:  # k % 3 == 2 -> index
            idx = int(chunk)
            k2, content = store[idx]
            if k2 == 'MATH':
                rebuilt.append(content)  # math: kept verbatim
            else:
                rebuilt.append('\\texttt{' + _escape_code(content) + '}')
    text = ''.join(rebuilt)
    return text


# ---------------------------------------------------------------------------
# Block-level conversion
# ---------------------------------------------------------------------------
FIG_MAP = {
    'en': {
        'fig1_boundary_map': 'fig1_boundary_map_en.png',
        'fig2_killsign_scatter': 'fig2_killsign_scatter_en.png',
        'fig3_division_scatter': 'fig3_division_scatter_en.png',
        'fig4_gt7_frontier': 'fig4_gt7_frontier_en.png',
        'fig5_poa_distribution': 'fig5_poa_distribution_en.png',
    },
    'cn': {
        'fig1_boundary_map': 'fig1_boundary_map_cn.png',
        'fig2_killsign_scatter': 'fig2_killsign_scatter_cn.png',
        'fig3_division_scatter': 'fig3_division_scatter_cn.png',
        'fig4_gt7_frontier': 'fig4_gt7_frontier_cn.png',
        'fig5_poa_distribution': 'fig5_poa_distribution_cn.png',
    },
}

IMG_RE = re.compile(r'^!\[(.*?)\]\((?:\.\./figures/|figures/)?([^)]+\.png)\)\s*$')
# abs-value notation inside table cells: escaped \|x\| (MD) or bare |x|
ABSPIPE_ESC_RE = re.compile(r'\\\|([A-Za-z\u0370-\u03ff]{1,3})\\\|')
ABSPIPE_BARE_RE = re.compile(r'\|([A-Za-z\u0370-\u03ff]{1,3})\|')


def _strip_section_number(h: str) -> str:
    """Remove leading 'N' or 'N.M' numbering from MD headings (F5)."""
    return re.sub(r'^\d+(?:\.\d+)*\s+', '', h).strip()


def _strip_appendix_prefix(h: str, lang: str) -> str:
    if lang == 'cn':
        return re.sub(r'^附录\s*[A-Z]\s*[：:]\s*', '', h).strip()
    return re.sub(r'^Appendix\s*[A-Z]\s*:\s*', '', h, flags=re.IGNORECASE).strip()


def _table_row_cells(line: str):
    """Split a MD table row into cells (F4: protect |x| / \\|x\\| abs-value first).

    The cell-internal abs-value notation is replaced by pipe-free placeholders
    BEFORE split('|'), so it cannot create spurious extra columns; placeholders
    are restored to math after splitting.
    """
    stash = []

    def _prot(m):
        stash.append(m.group(1))
        return f' @@ABS{len(stash) - 1}@@ '

    protected = line.strip()
    protected = ABSPIPE_ESC_RE.sub(_prot, protected)   # \|r\| -> placeholder
    protected = ABSPIPE_BARE_RE.sub(_prot, protected)  # |r|  -> placeholder
    raw_cells = [c.strip() for c in protected.strip('|').split('|')]
    cells = []
    for c in raw_cells:
        for i, sym in enumerate(stash):
            c = c.replace(f'@@ABS{i}@@', f'$|{sym}|$')
        cells.append(c.strip())
    return cells


def md_to_tex(md_path: Path, lang: str):
    text = md_path.read_text(encoding="utf-8")

    # 1. Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # 2. Remove author/metadata block lines
    text = re.sub(r'^\*\*作者\*\*：.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*Authors?\*\*[:：].*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*arXiv[^*]*\*\*.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*Date\*\*[:：].*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*代码与数据\*\*[:：].*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*Code & data\*\*[:：].*$', '', text, flags=re.MULTILINE)
    if lang == 'cn':
        text = re.sub(r'^\*\*Deposon: .+\*\*\s*$', '', text, flags=re.MULTILINE)
    # 3. Strip Wang/NSFC
    text = re.sub(r'王子贺（?[^）\n]*）?', '', text)
    text = re.sub(r'王子贺', '', text)
    text = re.sub(r'NSFC\s*[\d\-]+', '', text)
    text = re.sub(r'\(grant\s*\d+[\d–\-]*\)', '', text)

    # 4. Title
    m = re.search(r'^(# .+)$', text, re.MULTILINE)
    title_line = m.group(1).lstrip('# ').strip() if m else "Untitled"
    body_start = m.end() if m else 0
    while body_start < len(text) and text[body_start] in ' \t\n':
        body_start += 1
    body = text[body_start:]

    # 5. Cut at References
    ref_marker = '## 参考文献' if lang == 'cn' else '## References'
    ref_idx = body.find(ref_marker)
    body_text = body[:ref_idx] if ref_idx > 0 else body

    lines = body_text.split('\n')
    tex = []
    in_code = False
    in_list = False
    in_blockquote = False     # True while INSIDE a real, emitted quote env
    bq_dropped = False        # True while inside a pre-abstract blockquote that
                              # is suppressed entirely (no quote env emitted)
    in_abstract = False
    abstract_started = False   # becomes True at the Abstract/摘要 heading
    in_table = False
    table_buf = None          # (rows(list of cell-lists), is_long(bool))
    appendix_emitted = False

    def _close_list():
        nonlocal in_list
        if in_list:
            tex.append('\\end{itemize}')
            in_list = False

    def _close_blockquote():
        nonlocal in_blockquote, bq_dropped
        if in_blockquote:
            # Only a REAL, emitted quote env gets a closing token. A dropped
            # (suppressed) blockquote never emitted \begin{quote}, so emitting
            # \end{quote} here would leave an orphan \end{quote} in the tex
            # (the pre-abstract conventions call-out bug).
            tex.append('\\end{quote}')
        in_blockquote = False
        bq_dropped = False

    def _close_table():
        nonlocal in_table, table_buf
        if not in_table:
            return
        rows, is_long = table_buf
        ncol = len(rows[0])
        if is_long:
            spec = 'p{0.25\\linewidth}p{0.68\\linewidth}' if ncol == 2 else 'l' * ncol
            tex.append(f'\\begin{{longtable}}{{{spec}}}')
            tex.append('\\toprule')
            header = ' & '.join(rows[0]) + ' \\\\'
            tex.append(header)
            tex.append('\\midrule')
            tex.append('\\endhead')
            tex.append('\\bottomrule')
            tex.append('\\endfoot')
            for r in rows[1:]:
                tex.append(' & '.join(r) + ' \\\\')
            tex.append('\\end{longtable}')
        else:
            tex.append(f'\\begin{{tabular}}{{{"l" * ncol}}}')
            tex.append('\\toprule')
            tex.append(' & '.join(rows[0]) + ' \\\\')
            tex.append('\\midrule')
            for r in rows[1:]:
                tex.append(' & '.join(r) + ' \\\\')
            tex.append('\\bottomrule')
            tex.append('\\end{tabular}')
        in_table = False
        table_buf = None

    def _close_abstract():
        nonlocal in_abstract
        if in_abstract:
            tex.append('\\end{abstract}')
            in_abstract = False

    for raw in lines:
        stripped = raw.strip()

        # --- code blocks -----------------------------------------------------
        if stripped.startswith('```'):
            _close_list(); _close_blockquote(); _close_table()
            if in_code:
                tex.append('\\end{verbatim}')
                in_code = False
            else:
                tex.append('\\begin{verbatim}')
                in_code = True
            continue
        if in_code:
            tex.append(raw)
            continue

        # --- F7: standalone horizontal rule and the 1 declaration paragraph --
        if stripped == '---':
            continue
        if stripped.startswith('¹') or stripped.startswith('&sup1;'):
            continue

        # --- images (F1) -----------------------------------------------------
        img = IMG_RE.match(stripped)
        if img:
            _close_list(); _close_blockquote(); _close_table()
            caption_raw, png_name = img.group(1), img.group(2)
            # choose the per-language png by figure stem
            stem = re.sub(r'_(en|cn)\.png$', '', png_name).replace('.png', '')
            fig_file = FIG_MAP[lang].get(stem, png_name)
            # strip "Figure N:" / "图 N：" prefix from caption
            cap = re.sub(r'^Figure\s*\d+\s*[:：]\s*', '', caption_raw)
            cap = re.sub(r'^图\s*\d+\s*[:：]\s*', '', cap)
            cap_tex = md_to_tex_inline(cap, lang)
            tex.append('\\begin{figure}[t]')
            tex.append('\\centering')
            tex.append(f'\\includegraphics[width=0.92\\linewidth]{{{fig_file}}}')
            tex.append(f'\\caption{{{cap_tex}}}')
            tex.append('\\end{figure}')
            tex.append('')
            continue

        # --- headings ----------------------------------------------------------
        if stripped.startswith('#'):
            _close_list(); _close_blockquote(); _close_table()
            level = len(stripped) - len(stripped.lstrip('#'))
            htext = stripped[level:].strip()

            if htext in ('Abstract', '摘要'):
                _close_abstract()
                tex.append('\\begin{abstract}')
                in_abstract = True
                abstract_started = True
                continue
            if htext in ('References', '参考文献'):
                continue

            # any other heading closes the abstract first (F7)
            _close_abstract()

            # appendix (F5)
            is_appendix = bool(re.match(r'^(Appendix\s+[A-Z]|附录\s*[A-Z])', htext, re.IGNORECASE))
            if is_appendix:
                if not appendix_emitted:
                    # Static end matter: data availability, acknowledgments and
                    # the AI-use statement go AFTER the conclusion and BEFORE
                    # \appendix. Content is fixed text (not derived from MD).
                    tex.append(build_tail_sections(lang).rstrip('\n'))
                    tex.append('\\appendix')
                    appendix_emitted = True
                htext = _strip_appendix_prefix(htext, lang)
                htex = md_to_tex_inline(htext, lang)
                tex.append(f'\\section{{{htex}}}')
                continue

            htext = _strip_section_number(htext)
            htex = md_to_tex_inline(htext, lang)
            if level == 2:
                tex.append(f'\\section{{{htex}}}')
            elif level == 3:
                # MD uses ### for all x.y subsections (2.1-2.5, 3.1-3.5); map to
                # \subsection so LaTeX auto-numbering matches the MD hierarchy.
                tex.append(f'\\subsection{{{htex}}}')
            else:
                tex.append(f'\\subsubsection{{{htex}}}')
            continue

        # --- tables (F4/F6) ----------------------------------------------------
        if stripped.startswith('|'):
            cells = _table_row_cells(stripped)
            # separator row
            if all(set(c) <= set('-: ') and c != '' for c in cells) or all('---' in c or c == '' for c in cells):
                continue
            if not in_table:
                in_table = True
                table_buf = ([], False)
            converted = [md_to_tex_inline(c, lang) for c in cells]
            if any(len(c) > 50 for c in cells):
                table_buf = (table_buf[0] + [converted], True)
            else:
                table_buf = (table_buf[0] + [converted], table_buf[1])
            continue
        elif in_table:
            _close_table()

        # --- blockquote --------------------------------------------------------
        if stripped.startswith('>'):
            _close_list()
            # Pre-abstract blockquote = the "Data availability and
            # evidence-strength conventions" call-out. It is DROPPED here in its
            # entirety (the '>' line itself is `continue`d); the substance is
            # re-injected as a real section near the end of the paper
            # (build_tail_sections). We track the suppression with bq_dropped so
            # the later close (blank line / next paragraph / heading) does NOT
            # emit an orphan \end{quote}: the whole block — begin, content, end —
            # vanishes. Any blockquote after the abstract heading is converted
            # to a real quote environment normally.
            if not abstract_started:
                bq_dropped = True
                in_blockquote = False
                continue
            bq = stripped.lstrip('>').strip()
            if not in_blockquote:
                tex.append('\\begin{quote}')
                in_blockquote = True
            tex.append(md_to_tex_inline(bq, lang))
            continue
        elif (in_blockquote or bq_dropped) and stripped == '':
            # blank line ends either a real quote env or a dropped blockquote
            _close_blockquote()
            continue
        elif in_blockquote or bq_dropped:
            # non-'>' content line ends the blockquote
            _close_blockquote()

        # --- lists -------------------------------------------------------------
        mlist = re.match(r'^[-*]\s+(.+)$', stripped)
        if mlist:
            _close_blockquote()
            if not in_list:
                tex.append('\\begin{itemize}')
                in_list = True
            tex.append(f'  \\item {md_to_tex_inline(mlist.group(1), lang)}')
            continue
        if in_list:
            if stripped == '':
                continue  # tolerate blank lines inside a list
            _close_list()

        # --- blank -------------------------------------------------------------
        if stripped == '':
            continue

        # --- ordinary paragraph ------------------------------------------------
        _close_blockquote()
        tex.append(md_to_tex_inline(stripped, lang))
        tex.append('')

    # close everything
    _close_list()
    _close_blockquote()
    _close_table()
    _close_abstract()

    return title_line, '\n'.join(tex)


# ---------------------------------------------------------------------------
# Footnote text (exactly one footnote, right after \maketitle; F7).
# 2026-09-08 slim-down: version ONLY. The AI-use statement and the
# acknowledgments now live in their own sections at the end of the body
# (build_tail_sections), not in the front-matter footnote.
# ---------------------------------------------------------------------------
FOOTNOTE_EN = "Project version: deposon v0.1.1 (2026-09-08)."

FOOTNOTE_CN = "项目版本：deposon v0.1.1（2026-09-08）。"


# ---------------------------------------------------------------------------
# Static end matter (injected after the Conclusion, before \appendix).
# Fixed text, not derived from the MD sources.
# ---------------------------------------------------------------------------
TAIL_SECTIONS_EN = (
    "\\section{Data and Artifact Availability}\n"
    "Code is publicly available at \\texttt{github.com/zeroandcat/Deposon}. "
    "Every experimental number in this paper is traceable to a specific field of a frozen JSON file "
    "under the repository's \\texttt{results/} directory; the five figures are generated by the "
    "repository's frozen plotting scripts from those JSON files. Every statistical verdict is the "
    "mechanical evaluation of a pre-registered decision rule. Evidence strength is labeled in three "
    "tiers throughout: closed (pre-registered), consistency evidence, and motivation only.\n"
    "\n"
    "\\section{Acknowledgments}\n"
    "The author thanks colleagues for discussions and feedback on early drafts.\n"
    "\n"
    "\\section{Use of Generative AI Tools}\n"
    "The Deposon framework definition and project guidance were provided by the author. The core "
    "algorithm, the experimental pipeline, and the first draft of this manuscript were produced with "
    "the assistance of KIMI (Moonshot AI). The author subsequently reviewed, revised, and verified all "
    "content, including references, and takes full responsibility for the manuscript in accordance with "
    "arXiv's authorship and AI-use policy.\n"
)

TAIL_SECTIONS_CN = (
    "\\section{数据与工件可用性}\n"
    "代码公开于 \\texttt{github.com/zeroandcat/Deposon}。本文全部实验数字可追溯至仓库 "
    "\\texttt{results/} 目录下冻结 JSON 文件的具体字段；五张图由仓库冻结绘图脚本基于这些 JSON "
    "生成。全部统计判定为预登记决策规则的机械求值。证据强度全文分三档标注：已闭合（预登记判定）、"
    "一致性证据、仅有动机。\n"
    "\n"
    "\\section{致谢}\n"
    "感谢同事对初稿的讨论与反馈。\n"
    "\n"
    "\\section{生成式 AI 工具使用声明}\n"
    "Deposon 框架定义与项目指导由作者提供；核心算法、实验管线与论文初稿由 KIMI（月之暗面 "
    "Moonshot AI）协助完成。作者其后审阅、修订并核验了全部内容（含参考文献），并依 arXiv 著作权 "
    "与 AI 使用政策对全文承担完全责任。\n"
)


def build_tail_sections(lang: str) -> str:
    return TAIL_SECTIONS_CN if lang == 'cn' else TAIL_SECTIONS_EN


# ---------------------------------------------------------------------------
# Unicode declarations for pdflatex + inputenc utf8 + T1 (shared by en/cn).
# The MD sources write math as plain Unicode (no $...$); these declarations map
# each non-T1 codepoint to an \ensuremath (text-mode safe) or LaTeX command.
# Greek set is intentionally generous so both papers are fully covered.
# ---------------------------------------------------------------------------
UNICODE_DECLARATIONS = "\n".join(
    [
        "% --- Unicode characters (plain-Unicode math in the MD sources) ---",
        # punctuation / accents
        '\\DeclareUnicodeCharacter{00A7}{\\S}',
        '\\DeclareUnicodeCharacter{00B1}{\\ensuremath{\\pm}}',
        '\\DeclareUnicodeCharacter{00B7}{\\ensuremath{\\cdot}}',
        '\\DeclareUnicodeCharacter{00D7}{\\ensuremath{\\times}}',
        '\\DeclareUnicodeCharacter{00E8}{\\`e}',
        '\\DeclareUnicodeCharacter{00E9}{\\\'e}',
        '\\DeclareUnicodeCharacter{00F1}{\\~n}',
        '\\DeclareUnicodeCharacter{00F6}{\\"o}',
        '\\DeclareUnicodeCharacter{00FC}{\\\"u}',
        # dashes / ellipsis
        '\\DeclareUnicodeCharacter{2013}{--}',
        '\\DeclareUnicodeCharacter{2014}{---}',
        '\\DeclareUnicodeCharacter{2016}{\\ensuremath{\\|}}',
        '\\DeclareUnicodeCharacter{2026}{\\ldots}',
        # arrows
        '\\DeclareUnicodeCharacter{2192}{\\ensuremath{\\to}}',
        '\\DeclareUnicodeCharacter{21D2}{\\ensuremath{\\Rightarrow}}',
        # math operators / relations
        '\\DeclareUnicodeCharacter{2207}{\\ensuremath{\\nabla}}',
        '\\DeclareUnicodeCharacter{2208}{\\ensuremath{\\in}}',
        '\\DeclareUnicodeCharacter{2212}{\\ensuremath{-}}',
        '\\DeclareUnicodeCharacter{2218}{\\ensuremath{\\circ}}',
        '\\DeclareUnicodeCharacter{221A}{\\ensuremath{\\surd}}',
        '\\DeclareUnicodeCharacter{221D}{\\ensuremath{\\propto}}',
        '\\DeclareUnicodeCharacter{221E}{\\ensuremath{\\infty}}',
        '\\DeclareUnicodeCharacter{2248}{\\ensuremath{\\approx}}',
        '\\DeclareUnicodeCharacter{2261}{\\ensuremath{\\equiv}}',
        '\\DeclareUnicodeCharacter{2264}{\\ensuremath{\\leq}}',
        '\\DeclareUnicodeCharacter{2265}{\\ensuremath{\\geq}}',
        '\\DeclareUnicodeCharacter{226B}{\\ensuremath{\\gg}}',
        '\\DeclareUnicodeCharacter{2605}{\\ensuremath{\\star}}',
        # Greek (uppercase)
        '\\DeclareUnicodeCharacter{0391}{\\ensuremath{\\Alpha}}',
        '\\DeclareUnicodeCharacter{0392}{\\ensuremath{\\Beta}}',
        '\\DeclareUnicodeCharacter{0393}{\\ensuremath{\\Gamma}}',
        '\\DeclareUnicodeCharacter{0394}{\\ensuremath{\\Delta}}',
        '\\DeclareUnicodeCharacter{0398}{\\ensuremath{\\Theta}}',
        '\\DeclareUnicodeCharacter{039B}{\\ensuremath{\\Lambda}}',
        '\\DeclareUnicodeCharacter{039E}{\\ensuremath{\\Xi}}',
        '\\DeclareUnicodeCharacter{03A0}{\\ensuremath{\\Pi}}',
        '\\DeclareUnicodeCharacter{03A1}{\\ensuremath{\\Rho}}',
        '\\DeclareUnicodeCharacter{03A3}{\\ensuremath{\\Sigma}}',
        '\\DeclareUnicodeCharacter{03A6}{\\ensuremath{\\Phi}}',
        '\\DeclareUnicodeCharacter{03A8}{\\ensuremath{\\Psi}}',
        '\\DeclareUnicodeCharacter{03A9}{\\ensuremath{\\Omega}}',
        # Greek (lowercase)
        '\\DeclareUnicodeCharacter{03B1}{\\ensuremath{\\alpha}}',
        '\\DeclareUnicodeCharacter{03B2}{\\ensuremath{\\beta}}',
        '\\DeclareUnicodeCharacter{03B3}{\\ensuremath{\\gamma}}',
        '\\DeclareUnicodeCharacter{03B4}{\\ensuremath{\\delta}}',
        '\\DeclareUnicodeCharacter{03B5}{\\ensuremath{\\varepsilon}}',
        '\\DeclareUnicodeCharacter{03B6}{\\ensuremath{\\zeta}}',
        '\\DeclareUnicodeCharacter{03B7}{\\ensuremath{\\eta}}',
        '\\DeclareUnicodeCharacter{03B8}{\\ensuremath{\\theta}}',
        '\\DeclareUnicodeCharacter{03BB}{\\ensuremath{\\lambda}}',
        '\\DeclareUnicodeCharacter{03BC}{\\ensuremath{\\mu}}',
        '\\DeclareUnicodeCharacter{03BD}{\\ensuremath{\\nu}}',
        '\\DeclareUnicodeCharacter{03BE}{\\ensuremath{\\xi}}',
        '\\DeclareUnicodeCharacter{03C0}{\\ensuremath{\\pi}}',
        '\\DeclareUnicodeCharacter{03C1}{\\ensuremath{\\rho}}',
        '\\DeclareUnicodeCharacter{03C3}{\\ensuremath{\\sigma}}',
        '\\DeclareUnicodeCharacter{03C4}{\\ensuremath{\\tau}}',
        '\\DeclareUnicodeCharacter{03C6}{\\ensuremath{\\varphi}}',
        '\\DeclareUnicodeCharacter{03C7}{\\ensuremath{\\chi}}',
        '\\DeclareUnicodeCharacter{03C8}{\\ensuremath{\\psi}}',
        '\\DeclareUnicodeCharacter{03C9}{\\ensuremath{\\omega}}',
        '% --- end Unicode declarations ---\n',
    ]
) + "\n"


def make_tex(lang: str, md_path: Path, out_path: Path):
    title_line, body_tex = md_to_tex(md_path, lang)

    footnote = FOOTNOTE_CN if lang == 'cn' else FOOTNOTE_EN

    # arXiv 2026: force PDFLaTeX processing of the PNG figures. This literal
    # MUST be the very first line of the generated .tex (before
    # \documentclass); arXiv treats \pdfoutput=1 within the first 5 lines as a
    # request to run pdflatex. Emitted for both EN and CN; the CN CJK logic
    # below is unaffected (the CJK block still wraps the document body).
    pdfoutput_marker = "\\pdfoutput=1\n"

    if lang == 'cn':
        en_title = ("Deposon: An Auditable, Conservation-Guaranteed, "
                    "Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths")
        cn_title = title_line
        doc_class = (
            "\\documentclass[11pt,a4paper]{article}\n"
            "\\usepackage{CJKutf8}\n"
        )
        title_block = (
            "\\title{" + cn_title + " \\\\[2mm] \\large \\textit{" + en_title + "}}\n"
            "\\author{袁祺皓 \\\\\n"
            "School of Chemistry and Life Resources, Renmin University of China \\\\\n"
            "\\texttt{github.com/zeroandcat/Deposon}}\n"
            "\\date{2026-09-08}\n"
        )
    else:
        en_title = title_line
        doc_class = "\\documentclass[11pt,a4paper]{article}\n"
        title_block = (
            f"\\title{{{en_title}}}\n"
            "\\author{Qihao Yuan \\\\\n"
            "School of Chemistry and Life Resources, Renmin University of China \\\\\n"
            "\\texttt{github.com/zeroandcat/Deposon}}\n"
            "\\date{2026-09-08}\n"
        )

    preamble = doc_class + (
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage[T1]{fontenc}\n"
        + UNICODE_DECLARATIONS
        + "\\usepackage{amsmath,amssymb}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{booktabs}\n"
        "\\usepackage{longtable}\n"
        "\\usepackage{hyperref}\n"
        "\\usepackage{url}\n"
        "\\usepackage{enumitem}\n"
        "\\usepackage[margin=1in]{geometry}\n"
        "\\graphicspath{{figures/}}\n"
        "\n"
    )

    # Front matter after \maketitle: ONLY the slim version footnote (2026-09-08
    # requirement). The old arXiv/Repository/Date meta rule block was removed;
    # the AI-use statement and acknowledgments are end-of-body sections.
    # F7: the single footnote is numbered 1 and lands on the first page.
    # arXiv 2026: \pdfoutput=1 MUST be line 1, before \documentclass, so that
    # arXiv runs PDFLaTeX (required to process the PNG figures); prepended for
    # both EN and CN.
    document = pdfoutput_marker + preamble + title_block + "\\begin{document}\n"
    if lang == 'cn':  # F9: CJK wraps everything (title, body, footnote)
        document += "\\begin{CJK}{UTF8}{gbsn}\n"
    document += (
        "\\maketitle\n"
        + f"\\footnote{{{footnote}}}\n"
        + "\n"
        + body_tex
        + "\n\n"
        + build_bib_section(lang)
        + "\n"
    )
    if lang == 'cn':
        document += "\\end{CJK}\n"
    document += "\\end{document}\n"

    out_path.write_text(document, encoding="utf-8")
    print(f"Wrote: {out_path} ({len(document)} bytes)")
    return document


# ---------------------------------------------------------------------------
# thebibliography (F8: authors strip trailing period -> template adds it,
# fixing the "Zhou, D.. Chain-of-Thought" double period)
# ---------------------------------------------------------------------------
def _bib_parts(key: str):
    authors, title, venue, year, eprint, extra = BIB_ENTRIES[key]
    authors = authors.rstrip('.')          # template supplies the period
    tail = str(year)
    if extra:
        tail += f", {extra}"
    eprint_part = f" \\texttt{{{eprint}}}" if eprint else ""
    return authors, title, venue, tail, eprint_part


def build_bib_section(lang: str) -> str:
    bib_lines = ["\\begin{thebibliography}{99}\n"]
    keys = sorted(BIB_ENTRIES.keys(), key=lambda k: int(k.replace('key', '')))
    for k in keys:
        authors, title, venue, tail, eprint_part = _bib_parts(k)
        bib_lines.append(
            f"\\bibitem{{{k}}} {authors}. {title}. \\textit{{{venue}}}, {tail}{eprint_part}.\n"
        )
    bib_lines.append("\\end{thebibliography}\n")
    return ''.join(bib_lines)


def build_references_bib() -> str:
    out = [
        "% Deposon paper references (BibTeX)",
        "% Renumbered to arXiv standard (order of first appearance) 2026-09-08",
        "% Keys: key01-key62; corrections per docs/REF_VERIFICATION_v2.md",
        "",
        "",
    ]
    for k in sorted(BIB_ENTRIES.keys(), key=lambda x: int(x.replace('key', ''))):
        authors, title, venue, year, eprint, extra = BIB_ENTRIES[k]
        authors = authors.rstrip('.')
        out.append(f"@article{{{k},")
        out.append(f"  author    = {{{authors}}},")
        out.append(f"  title     = {{{title}}},")
        out.append(f"  journal   = {{{venue}}},")
        out.append(f"  year      = {{{year}}},")
        if extra:
            out.append(f"  note      = {{{extra}}},")
        if eprint:
            out.append(f"  eprint    = {{{eprint.replace('arXiv:', '')}}},")
            out.append("  archivePrefix = {arXiv},")
        out.append("}")
        out.append("")
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
print("Generating LaTeX files...")
make_tex('en', EN_MD, PKG / "deposon_paper_en.tex")
make_tex('cn', CN_MD, PKG / "deposon_paper_cn.tex")

print("\nGenerating references.bib...")
bib_content = build_references_bib()
(PKG / "references.bib").write_text(bib_content, encoding="utf-8")
print(f"Wrote: {PKG / 'references.bib'} ({len(bib_content)} bytes)")

print("\n=== Combined intermediate package contents ===")
for f in sorted(PKG.rglob("*")):
    if f.is_file():
        rel = f.relative_to(PKG)
        print(f"  {rel}  ({f.stat().st_size} bytes)")
