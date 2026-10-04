#!/usr/bin/env python3
"""Audit only the eleven user-supplied public caches; save literal extracts."""
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)
data = json.loads((ROOT / 'input.json').read_bytes())
sources = json.loads(data['assignment'].split('Read-only published source caches:\n', 1)[1])

# Inclusive line numbers refer to the exact supplied layout extraction, never OCR fixes.
SELECTIONS = {
    '1201.0187': [('standing-and-main', 84, 219), ('positivity', 291, 368),
                 ('psh-compactness', 1615, 1770), ('base-ideal-proof', 1842, 1900)],
    '1201.0188': [('standing-and-Theorem-A', 58, 108), ('psh-background', 473, 553),
                 ('intersection-calculus', 602, 692), ('bounded-operator-proof', 737, 874),
                 ('regularization-locality', 934, 1102), ('energy-E1-proof', 1190, 1400),
                 ('envelope-derivative-proof', 1400, 1545), ('uniqueness-existence-proof', 1546, 1717)],
    '1805.01016': [('title-and-scope', 1, 99)],
    '1801.08229': [('title-and-standing', 1, 110), ('trivial-valued-variational-proof', 5220, 5265),
                 ('trivial-valued-surjectivity-proof', 6080, 6160)],
    '2307.01697': [('synthetic-standing-and-Theorem-A', 59, 163),
                 ('NA-positive-cone', 250, 539), ('Holder-and-defect-proof', 791, 914),
                 ('maxima-orthogonality', 989, 1125), ('density-and-uniform-integral-proof', 1120, 1206)],
    '2209.04879': [('Remark-4.4', 1975, 2001)],
    '1712.00980': [('title-and-introduction', 1, 250), ('model-envelope-and-descent', 280, 422),
                 ('test-ideals-resolution-proof', 655, 825), ('geometric-test-ideal-proof', 826, 997),
                 ('envelope-and-equation-proof', 998, 1197), ('appendix-obstruction', 1198, 1250)],
    '2506.13548': [('title-and-scope', 1, 105)],
    'Thuillier': [('curve-equation-and-regularization', 5518, 5535), ('regularization', 5697, 5743)],
    'Berkovich': [('title', 1, 35)],
    '1204.6277': [('title-and-version', 1, 26)],
}
APPLICATIONS = {
    '1712.00980': 'Applied: Definition 8.1 with d=1, n=2 and perfect characteristic-p k; Theorem 6.3 discharges both Definitions 6.1 and 6.2 in dimension 3. Proposition 5.2 and section 9 give cofinal projective SNC models. Theorem 8.2/Corollary 8.3 and Corollary 9.1 give continuous envelopes and monotone regularization for every ample curvature class on this X. Section 9 explicitly transfers BFJ sections 3-6. Theorem 9.2 gives orthogonality. Theorem 9.3 itself retains skeleton support; it is not cited for arbitrary-support surjectivity. Only published model/envelope descent is used; no new unbounded base-change statement is inferred.',
    '1201.0187': 'Applied through the exact positive-characteristic transfer in GJKM section 9: sections 1-7 supply psh compactness, sup continuity, and determination by divisorial values once projective SNC models are cofinal. Its multiplier-ideal section 8 and characteristic-zero Appendix B are replaced by GJKM sections 4,7,8. This cached v2 has compactness Theorem 7.10.',
    '1201.0188': 'Actual v1: Theorem A assumes residue characteristic zero, algebraizability, and SNC-dual-complex support. Applied bounded operator Theorem 3.1; locality Theorem 5.1; energy Proposition 6.2; nonpluripolar construction Definition 6.4; full mass Lemma 6.7; independence Proposition 6.9; comparison Proposition 6.11; differentiation Proposition 6.12 and Theorem 7.2/Corollary 7.3. GJKM explicitly transfers sections 3-6 and supplies orthogonality for section 7. Uniqueness Proposition 8.2 proof is checked as characteristic-free finite-energy calculus; its last vertical Hodge kernel step is independently proved in the argument. Saved v1 sequence regularization is Proposition 4.5, not the later-version Proposition 4.7 cited by GJKM.',
    '2307.01697': 'Applied on the actual Berkovich compact space with real spans of model functions/forms: model intersection symmetry and seminegativity are supplied by BFJ intersection calculus transferred by GJKM; positivity datum has ample class; test functions are dense and admit maxima. The smooth geometrically integral X has V>0. GJKM orthogonality verifies Definition 2.15. Theorem 1.33, Proposition 2.2, Theorem 2.23, Lemma 2.25 are used only on model/test potentials and finite-energy Radon probability measures. New extension of the uniform integration estimate to E1 and actual variational attainment are proved in the argument. Theorem A(iii), completion of measures, is not used to infer surjectivity.',
    '1801.08229': 'Scope audit and proof comparison only: actual v4 concerns a trivially valued field. Theorem 12.9, including its dimension-at-most-two endpoint, is not applied to k((t)). The analogous variational proof motivates the new explicit finite-energy integration argument but is not transplanted as a theorem.',
    '1805.01016': 'Scope audit only: actual v3 is Boucksom-Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Not a general finite-energy surjectivity theorem; no theorem from it is needed in the positive-residue proof.',
    '2209.04879': 'Scope audit only: Remark 4.4 distinguishes definition of E1 over arbitrary fields from construction of its MA operator; the exact phrase characteristic zero is preserved rather than strengthened to residue characteristic zero.',
    '2506.13548': 'Scope audit only: Gubler-Rabinoff v2 explicitly says additional hypotheses may be needed for regularization and MA and that this is not the subject of the paper. No BFJ E1 equation result is inferred from its maximum principles.',
    'Thuillier': 'Scope audit only; curve singular equation/regularization is not substituted for the higher-dimensional surface proof, and no OCR-corrupted French statement is used as an indispensable input.',
    'Berkovich': 'Scope audit only: 1993 Etale cohomology paper, not the 1990 book cited internally by GJKM. No unseen base-change theorem is imported from it.',
    '1204.6277': 'Scope audit only: actual v2 is dated July 2025, real forms and currents on Berkovich spaces. No local wedge-product or transfinite psh construction is used to assert global BFJ E1 surjectivity.',
}

records = []
for source in sources:
    url = source['public_source']
    sid = source.get('arxiv_id')
    if not sid:
        sid = ('2506.13548' if '2506.13548' in url else 'Thuillier' if 'tel-' in url
               else 'Berkovich' if 'numdam' in url else '1204.6277')
    record = {'id': sid, 'public_source': url,
              'saved_version': source.get('saved_version', url),
              'application_check': APPLICATIONS[sid], 'files': [], 'literal_extracts': []}
    for key in ('pdf', 'literal_extract', 'abstract_html'):
        if key not in source:
            continue
        path = Path(source[key]); raw = path.read_bytes()
        expected_key = {'pdf': 'pdf_sha256', 'literal_extract': 'extract_sha256',
                        'abstract_html': 'abstract_sha256'}[key]
        actual = hashlib.sha256(raw).hexdigest()
        assert actual == source[expected_key], (sid, key, actual)
        record['files'].append({'kind': key, 'path': str(path), 'bytes': len(raw),
                                'sha256': actual, 'matches_supplied_hash': True})
    raw = Path(source['literal_extract']).read_bytes()
    # PDF form feeds are page markers within a newline-defined source line.
    # splitlines() would also split at form feeds and shift sed/rg line numbers.
    decoded = raw.decode('utf-8')
    pieces = decoded.split('\n')
    lines = [line+'\n' for line in pieces[:-1]] + ([pieces[-1]] if pieces[-1] else [])
    for label, first, last in SELECTIONS[sid]:
        literal = ''.join(lines[first-1:last])
        dest = OUT / f'{sid}-{label}.txt'
        dest.write_text(literal, encoding='utf-8')
        # Printed-page ordinal follows layout form feeds; match to PDF page numbers.
        page_first = lines[:first-1]
        record['literal_extracts'].append({
            'filename': str(dest.relative_to(ROOT)), 'source_line_first': first,
            'source_line_last': last, 'pdf_page_first': ''.join(page_first).count('\f')+1,
            'pdf_page_last': ''.join(page_first).count('\f')+literal.count('\f')+1,
            'sha256': hashlib.sha256(dest.read_bytes()).hexdigest(), 'literal_text': literal})
    info = subprocess.run(['pdfinfo', source['pdf']], capture_output=True, text=True)
    (OUT / f'{sid}-pdfinfo.txt').write_text(info.stdout + info.stderr)
    record['pdfinfo_returncode'] = info.returncode
    records.append(record)

provenance = {
    'scope': 'Only input.json, eleven explicitly listed public caches, and fresh workspace artifacts were read.',
    'input_sha256': hashlib.sha256((ROOT/'input.json').read_bytes()).hexdigest(),
    'source_audit_kind': 'Selected relevant statements and proof passages, not an exhaustive literature survey.',
    'version_cautions': [
        '1201.0188 is byte-verified v1; its theorem retains algebraizability and dual-complex support.',
        '1805.01016 is byte-verified Boucksom-Eriksson v3, not a differently named pluripotential paper.',
        '1801.08229v4 has trivial valuation; no nontrivial-valued conclusion is quoted from its theorem.',
        'GJKM Theorem 4.6(iii), visually checked on PDF page 15, says E-lambda D nef; the introduction Theorem 1.3 has a different displayed order. The body theorem is used.',
        'GJKM section 9 assumptions A1-A3 visually checked on PDF page 22; n+d=3 here.',
        'GJKM cites later BFJ numbering: sequence regularization maps to Proposition 4.5 in supplied BFJ v1.',
        'GJKM Theorem 6.3 is used as a published theorem with the exact dimension/perfect-field application; CP08/CP09 themselves were not supplied or independently checked.',
    ],
    'visual_pdf_checks': ['source-extracts/GJKM-page15.png', 'source-extracts/GJKM-page22.png'],
    'sources': records,
}
(OUT/'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')
env = {'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT),
       'input_original_byte_identical': (ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes()}
for tool in ('pdftotext','pdflatex','latexmk'):
    p = subprocess.run([tool, '-v' if tool=='pdftotext' else '--version' if tool=='pdflatex' else '-version'], capture_output=True, text=True)
    env[tool] = {'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
(ROOT/'environment.json').write_text(json.dumps(env, indent=2)+'\n')
print(json.dumps({'sources_verified': len(records), 'literal_extracts': sum(len(r['literal_extracts']) for r in records),
                  'input_original_byte_identical': env['input_original_byte_identical']}, indent=2))
