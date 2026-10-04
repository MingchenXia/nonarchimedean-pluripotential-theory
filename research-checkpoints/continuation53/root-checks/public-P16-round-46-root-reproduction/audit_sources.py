#!/usr/bin/env python3
"""Verify only the ten authorized public caches and save literal extracts."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
inp = json.loads((ROOT / 'input-original.json').read_bytes())
marker = 'Read-only published source caches:\n'
sources = json.loads(inp['assignment'].split(marker, 1)[1].strip())
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)

# Line numbers refer to the supplied literal text, not regenerated OCR.
selections = {
    '1201.0187': [('standing-and-compactness', 89, 171)],
    '1201.0188': [('v1-theorem-and-curve-background', 62, 131)],
    '1805.01016': [('continuous-volume-and-curve-envelopes', 119, 170),
                   ('continuous-psh-and-nef', 2286, 2340),
                   ('continuous-ma-proof', 2665, 2785),
                   ('continuous-energy', 3540, 3590)],
    '1801.08229': [('trivial-valuation-calabi-yau', 102, 203)],
    '2307.01697': [('measure-completion-scope', 54, 164),
                   ('orthogonality-and-density-proof', 1109, 1172),
                   ('measure-quasimetric-proof', 1173, 1230)],
    '2209.04879': [('continuous-ma-and-unbounded-gap', 1968, 1996)],
    '2506.13548': [('scope-and-exclusion', 55, 88),
                   ('disk-tree-topology', 1930, 1980)],
    'thuillier': [('field-convention', 1155, 1196),
                  ('laplacian-solvability-proof', 4957, 5075),
                  ('metric-regularization-proof', 5670, 5759),
                  ('hilbert-space-proof', 5793, 5897),
                  ('finite-energy-proof', 5995, 6093)],
    'berkovich': [('identity-and-general-field', 1, 110)],
    'cd': [('continuous-product-proof', 10291, 10339),
           ('iteration-and-uniform-convergence', 10410, 10494)]
}

checks = {
    '1201.0187': 'v2: complete discrete valuation field, residue characteristic zero; smooth projective analytification, ample line bundle. Compactness and regularization are not arbitrary-field statements in this version. Used only in the audit.',
    '1201.0188': 'Actual saved v1, not the later published theorem. Theorem A: complete discrete valuation field of residue characteristic zero; smooth projective algebraizable variety; ample L; positive Radon measure of raw mass (L^n), supported on one SNC dual complex. Its introduction separately records curve background over any complete nontrivially valued field. No arbitrary-support higher-dimensional application.',
    '1805.01016': 'Boucksom--Eriksson, Spaces of norms, v3. Theorems 7.8 and 8.4 apply to the partial sector: K complete nontrivially valued, X=P^1 smooth projective, L=O(d) ample. Continuous psh means uniform closure of FS; hence psh-regularizable. Theorem 8.4 is a uniform-continuity result for continuous metrics, not decreasing continuity for unbounded metrics. The curve envelope statement in the introduction/7.30 has the same valid smooth-curve hypotheses; it is background and not used to obtain our explicit solution.',
    '1801.08229': 'v4: algebraically closed trivially valued field. Theorem A constructs the finite-energy extension; surjectivity stated for smooth X with characteristic zero or dimension at most two. A nontrivial valuation is outside its standing domain. No base-field descent application.',
    '2307.01697': 'v1: synthetic formalism includes projective Berkovich spaces over complete non-Archimedean fields. Test space D, model numerical forms, positive interior polarization. Theorem A/2.23/2.24 give strong density and complete quasi-metric on measures; they do not identify a completion element with an actual unbounded psh potential. Orthogonality is stated unconditional for this formalism in Example 2.20, distinct from continuity of all psh envelopes. Used only for audit; no inference of a full unbounded operator.',
    '2209.04879': 'Saved v2: Theorem 4.3 continuous metrics over complete valued fields; Remark 4.4 explicitly distinguishes definition of E^1 from extension of MA. Its phrase characteristic zero is quoted literally; retained BFJ standing assumption checked separately is residue characteristic zero. Used only for audit.',
    '2506.13548': 'v2 dated 17 September 2025: classically psh functions, arbitrary complete non-Archimedean field (possibly trivial), maximum principles. Introduction explicitly excludes MA construction. Appendix A describes the disk tree/topology; used for background tree structure on P^1 over algebraically closed nontrivially valued K. The coordinate disks in Z and 1/Z are identified along their overlap; their intersection is not only the Gauss root. No inference from classically psh to a higher-dimensional finite-energy equation.',
    'thuillier': 'Thesis tel-00010990v1: chapter 2 standing field complete, nontrivially valued; smooth strictly analytic curves. Section 3.5 additionally connected and proper. P^1 in the partial theorem meets every condition. Green functions and Hilbert energy are compatible background; our tree kernel and E^1 identification are proved explicitly. PDF pages 111,117,118 visually checked: additive weights use -log norm, regularization decreases weights, Proposition 3.5.7 includes the full raw mass times delta_x. OCR/sign slips are not copied into our formulas. No normalization, resolution or field-descent assertion is imported.',
    'berkovich': 'Etale cohomology for non-Archimedean analytic spaces, PMIHES 78 (1993), pages 5-161. General analytic foundations, not a finite-energy Monge--Ampere source. No theorem from this paper is indispensable to our partial construction.',
    'cd': 'Actual saved v2, July 2025, expanded to 591 PDF pages. Uses transfinite psh definitions. Lemma 8.5.5 explicitly requires continuous psh u; Proposition 8.7.2 assumes continuous functions and local uniform convergence. The shorthand psh in 8.7.1 cannot remove the continuity hypothesis of the cited product lemma. It supplies no global unbounded E^1 all-support equation in the audited statements. Section numbers of v1 must not be applied to v2.'
}

records = []
for source in sources:
    url = source['public_source']
    sid = source.get('arxiv_id')
    if sid is None:
        sid = ('2506.13548' if '2506.13548' in url else
               'thuillier' if 'tel-00010990' in url else
               'berkovich' if 'numdam' in url else 'cd')
    record = dict(source)
    record['local_id'] = sid
    record['application_check'] = checks[sid]
    record['verified_hashes'] = {}
    for key, hkey in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256'),
                      ('abstract_html', 'abstract_sha256')]:
        if key not in source:
            continue
        p = Path(source[key])
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest != source[hkey]:
            raise RuntimeError(f'Hash mismatch: {p}')
        record['verified_hashes'][key] = digest
    rawtext = Path(source['literal_extract']).read_text()
    record['extracts'] = []
    for label, lo, hi in selections[sid]:
        # splitlines() treats form-feed as a line break; rg/sed do not.
        # Therefore use newline-only splitting for exact supplied line numbers.
        literal = '\n'.join(rawtext.split('\n')[lo-1:hi]) + '\n'
        fname = f'{sid}-{label}.txt'
        (OUT / fname).write_text(literal, encoding='utf-8')
        prefix = '\n'.join(rawtext.split('\n')[:lo-1])
        last = '\n'.join(rawtext.split('\n')[:hi])
        record['extracts'].append({'file': 'source-extracts/' + fname,
                                  'supplied_line_start': lo, 'supplied_line_end': hi,
                                  'pdf_page_start': prefix.count('\f') + 1,
                                  'pdf_page_end': last.count('\f') + 1,
                                  'sha256': hashlib.sha256(literal.encode()).hexdigest(),
                                  'kind': 'literal supplied pdftotext, including original OCR defects'})
    records.append(record)

provenance = {'scope': 'Exactly the ten user-authorized public caches; no other research files read.',
              'sources': records,
              'visual_checks': [
                  {'file': 'source-extracts/thuillier-regularization-111.png', 'finding': 'Printed page 97 confirms weights are -log norm and regularization increases norms/decreases weights. A preceding displayed curvature sign in the source is inconsistent with this convention; our sign is independently fixed by integration by parts.'},
                  {'file': 'source-extracts/thuillier-energy-117.png', 'finding': 'Printed page 103, Proposition 3.5.7: mu - (integral mu) delta_x, g_x,mu in W^1, and g_x,mu in L^1(mu) are equivalent.'},
                  {'file': 'source-extracts/thuillier-energy-118.png', 'finding': 'Printed page 104 contains energy equality and Proposition 3.5.9; retained as original-PDF evidence.'},
                  {'file': 'source-extracts/ps-remark-35.png', 'finding': 'Printed/PDF page 35 is the continuous-operator/Remark 4.4 distinction; retained as original-PDF evidence.'},
                  {'file': 'source-extracts/cd-continuity-207.png', 'finding': 'PDF page 207, Lemma 8.5.5 explicitly says toute fonction continue psh.'}
              ],
              'limitations': 'Hash matches and saved literal extracts prove file identity, not mathematical validity or completeness of a literature search.'}
(OUT / 'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
print(f'PASS: verified {len(records)} authorized sources and saved {sum(len(r["extracts"]) for r in records)} literal extracts.')
