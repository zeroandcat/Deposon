import hashlib, re
en_b = open('letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md','rb').read()
cn_b = open('letters/_v5_rj5_external_rederive_request_2026_09_28.md','rb').read()
en = en_b.decode('utf-8'); cn = cn_b.decode('utf-8')
print('EN bytes      =', len(en_b))
print('EN sha256_12  =', hashlib.sha256(en_b).hexdigest()[:12])
print('EN CR count   =', en_b.count(b'\r'), '(must be 0)')
print('EN BOM        =', en_b[:3] == b'\xef\xbb\xbf', '(must be False)')
print('EN lines      =', en.count('\n')+1)
print('CN bytes      =', len(cn_b), '(must be 31381)')
print('CN sha256_12  =', hashlib.sha256(cn_b).hexdigest()[:12], '(must be cfd58ae66463)')
print()
# re-run the core verbatim assertions after the edits
checks = {
 'all CN 12-hex tokens present': set(re.findall(r'(?<![0-9a-fA-F])[0-9a-f]{12}(?![0-9a-fA-F])', cn)) <= set(re.findall(r'(?<![0-9a-fA-F])[0-9a-f]{12}(?![0-9a-fA-F])', en)),
 'definition-factor line fullwidth semicolon': 'r_K \u2261 K_lit/(\u03b2\u00b7c_ferro)\uff1br_\u0393 \u2261 \u0393_lit/(\u03b2\u00b7c_trans)' in en,
 'S1 eq(1) quote': 'The Hamiltonian, H, is H =\u2212 \u2211 i (hi\u03c3x i +\u03bb2\u03c3x i\u03c3z i\u22121\u03c3z i+1 +\u03bb1\u03c3z i\u03c3z i\u22121) (1) written in terms of standard Pauli matrices.' in en,
 'S4 Gruneisen line': '\u0393(T,g ) = \u2202Tvg(T,g ) \u2202T\u03f5(T,g ) . (1)' in en,
 'TFIM_CONVENTION fullwidth punctuation kept': 'K \u2261 \u03b2J/4\uff0c\u0393 \u2261 \u03b2h/4\uff1b\u65e0\u91cf\u7eb2\u6e29\u5ea6 t_rel \u2261 k_BT/J = 1/(4K)' in en,
 'anti-downgrade clause present': 'Anti-downgrade clause' in en,
 'model name+version required': 'model name and the full version identifier actually used' in en,
 'request.model comparison': 'request.model' in en,
 '0-hint both candidates side by side': ('r_K \u2261 r_\u0393 \u2261 1/2' in en) and ('r_K \u2261 r_\u0393 \u2261 1' in en),
 'attribution: PI commissioning / doc-writer drafter': ('**Commissioning party' in en) and ('agent-0032834a3e04' in en),
 'counterpart rule': 'Counterpart-version rule' in en,
 'consistency statement': 'Consistency statement' in en,
 'zero-product declaration': 'Zero-product declaration' in en,
 'no-outline clause': 'contains no reply outline' in en,
}
for k,v in checks.items():
    print(('  PASS  ' if v else '  FAIL  ') + k)
print()
print('ALL PASS' if all(checks.values()) else 'SOME FAILED')
