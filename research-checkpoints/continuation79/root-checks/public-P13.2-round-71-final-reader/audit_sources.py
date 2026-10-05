"""Audit only the supplied primary caches and explicitly accepted bindings."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)

def sha(b):
    return hashlib.sha256(b).hexdigest()

RANGES = {
    'A': [(218,286), (344,393), (476,615), (757,804), (923,959),
          (960,1205), (1206,1325)],
    'C': [(2797,3015), (4760,4959), (4964,5301), (6080,6146)],
    'D': [(63,174)],
    'E': [(639,741), (761,995), (1512,1577), (1696,1827),
          (1885,2103), (2105,2692), (2694,2762)],
}
CHECKS = {
 'A': ('Definitions of the actual cone domains, mass-one energy and dual energy; '
       'the new arguments reconstruct duality, maximizing-sequence convergence and midpoint concavity. '
       'A Proposition 7.3 LF1249 has the wrong inequality direction for a concave tangent: '
       'our tangent inequality is proved from accepted concavity and weighted decreasing continuity. '
       'No surjectivity or completeness theorem is taken from A.'),
 'B': ('No new mathematical application. The accepted supporting theorem supplies the corrected '
       'full-ring bridge E=(n+1)S/n; the printed E=S is not imported.'),
 'C': ('Projective analogy and dependency audit only. Theorem 9.11 is independently reconstructed '
       'on the actual cone carrier. The complete relevant proof of Theorem 12.8 retains EP as an '
       'antecedent; it is not applied to an arbitrary singular quotient.'),
 'D': ('No synthetic theorem is applied. Its fixed linear D,Z,ddc, positive mixed products and '
       'Hodge-index antecedents are recorded. Same-ray calculations here use actual cone mixed '
       'products from the accepted theorem, not nonlinear cross-ray roots.'),
 'E': ('Only literal Definitions 3.7,3.8,3.15 and Proposition 4.19 are used for the independently '
       'proved counterexample to the printed lower-growth formulation. The singular envelope '
       'Theorem 7.1 is not used. Other retained bodies expose the unverified corrected-growth, '
       'contact, trace, Rossi/Runge, singular-induction and arbitrary-field descent obligations. '
       'Retaining a proof body does not certify its premises or its conclusion.'),
 'F': ('No new application; smooth-projective standing scope cannot silently cover singular normal quotients.'),
 'G': ('No new source theorem application; accepted P13.1 provides the genuine radial calibration '
       'and bounded current limits. No unbounded moving-Reeb limit is used.'),
 'H': ('No new source theorem application; the accepted P13.1 model bridge gives the canonical '
       'product-model reference mass and the actual fixed-ray intersection calculus.'),
 'I': ('No new source theorem application; accepted P13.1 supplies both-sign outer differentiation '
       'after checking the quantitative relative-volume estimate and its normalization.'),
 'J': ('No new source theorem application; no envelope conclusion is added to continuous-psh '
       'energy/volume equality in this actual v3.'),
 'K': ('No new source theorem application; accepted signed-semigroup obstacle equality is used '
       'only as part of the accepted outer differentiation theorem, not as envelope attainment.'),
}

sources = json.loads((ROOT/'sources.json').read_text())
records = []
for s in sources:
    ident = s['local_id']
    rec = {'id':ident, 'descriptor':s, 'verified_files':[],
           'application_and_limits':CHECKS[ident],
           'read_scope':'Selected bodies only; no whole-body independent correctness claim.',
           'excerpts':[]}
    for name, expected in s.items():
        if not name.endswith('_sha256'):
            continue
        path_key = name[:-7]
        if path_key == 'extract':
            path_key = 'literal_extract'
        if path_key == 'abstract':
            path_key = 'abstract_html'
        if path_key == 'fresh_official_pdf':
            path_key = 'fresh_official_versioned_pdf'
        if path_key not in s:
            continue
        p = Path(s[path_key])
        b = p.read_bytes()
        actual = sha(b)
        if actual != expected:
            raise ValueError(f'Hash mismatch: {ident} {p}')
        rec['verified_files'].append({'path':str(p), 'bytes':len(b),
                                      'sha256':actual, 'matches_expected':True})
    b = Path(s['literal_extract']).read_bytes()
    lines = b.decode('utf-8').split('\n')
    (OUT/f'{ident}-full.txt').write_bytes(b)
    rec['complete_literal_copy'] = f'source-extracts/{ident}-full.txt'
    rec['LF_coordinate_convention'] = "inclusive one-based indices of bytes.decode('utf-8').split('\\n'); no splitlines or newline translation"
    rec['LF_entries'] = len(lines)
    for a,z in RANGES.get(ident,[]):
        assert 1 <= a <= z <= len(lines)
        rec['excerpts'].append({'start_LF':a,'end_LF':z,
                               'literal':'\n'.join(lines[a-1:z]),
                               'purpose':CHECKS[ident]})
    records.append(rec)

accepted = []
for b in json.loads((ROOT/'accepted-bindings.json').read_text()):
    raw = Path(b['path']).read_bytes()
    assert sha(raw) == b['sha256']
    rec = dict(b, actual_sha256=sha(raw), bytes=len(raw))
    if b['path'].endswith('.md'):
        lines = raw.decode('utf-8').split('\n')
        rec['mathematical_body'] = {'start_LF':12, 'end_LF':411,
                                  'literal':'\n'.join(lines[11:411])}
        rec['use'] = ('The accepted full mathematical proof is the supporting premise. '
                      'Canonical notes and review are bindings/documentary confirmation only; '
                      'their operational claims are not mathematical premises. '
                      'No new envelope, completeness, inverse or unbounded moving-field '
                      'claim is attributed to this premise.')
    accepted.append(rec)
report = {'coordinate_rule':"UTF-8 bytes decode then split('\\n')",
          'sources':records, 'accepted_bindings':accepted,
          'all_expected_hashes_match':True,
          'universal_mathematical_verification':False}
(OUT/'source-provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'primary_sources':len(records),
                  'verified_files':sum(len(r['verified_files']) for r in records),
                  'literal_excerpts':sum(len(r['excerpts']) for r in records),
                  'accepted_bindings':len(accepted),
                  'all_expected_hashes_match':True},indent=2))
