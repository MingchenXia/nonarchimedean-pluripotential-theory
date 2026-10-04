#!/usr/bin/env python3
"""Reproduce a bounded, read-only audit of precisely the ten supplied caches."""
from pathlib import Path
import hashlib
import json
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

EXTRACTS = {
    '1201.0187': [(88, 101), (150, 194), (1648, 1766), (1774, 1823), (1894, 1955)],
    '1201.0188': [(60, 102), (700, 753), (1190, 1411), (1412, 1460), (1544, 1685)],
    '1805.01016': [(125, 170), (2281, 2308), (2550, 2586), (2611, 2761)],
    '1801.08229': [(102, 206), (2797, 2828), (2894, 2928), (2977, 3064),
                   (3650, 3717), (3977, 4067), (4212, 4251), (4529, 4605),
                   (4840, 4874), (4964, 5024), (5182, 5314), (6080, 6148)],
    '2307.01697': [(89, 166), (346, 386), (508, 532), (677, 705), (850, 923),
                   (1020, 1047), (1115, 1168), (1169, 1290), (2314, 2328)],
    '2209.04879': [(1978, 1997), (2018, 2029)],
    '2506.13548': [(1, 19), (64, 88)],
    'Thuillier': [(5516, 5527), (5676, 5717)],
    'Berkovich': [(1, 10), (30, 45)],
    '1204.6277': [(1, 29), (636, 680)],
}

CHECKS = {
    '1201.0187': {
        'identity': 'Boucksom--Favre--Jonsson, Singular semipositive metrics in non-Archimedean geometry, arXiv:1201.0187v2; banner 21 Jan 2014, internal date 22 Oct 2018.',
        'applications': ['Complete nontrivially discretely valued K, residue characteristic zero, smooth projective geometrically integral X, ample L satisfy the standing hypotheses. No function-field algebraizability is imposed here.', 'Theorem 7.10 gives compact normalized PSH and continuity of divisorial evaluations; Theorem 8.3 gives continuous psh envelopes; Theorem B/8.7 gives decreasing model regularization. These apply only at this field endpoint.'],
        'limitations': ['Do not transport these inputs to a densely valued field or positive residue characteristic. Retractions are used for topology, not to restrict a target measure.'],
    },
    '1201.0188': {
        'identity': 'Boucksom--Favre--Jonsson, Solution to a non-Archimedean Monge-Ampere equation, actual arXiv:1201.0188v1; banner 30 Dec 2011, internal date 29 Oct 2018.',
        'applications': ['Theorem A requires smooth projective X, complete discrete K with residue characteristic zero, extra function-field algebraizability, and target supported on one SNC dual complex. We do not cite it for arbitrary targets.', 'Sections 2--7 construct the genuine bounded and E1 operators for the discrete residue-zero smooth projective setting: Theorem 3.1, Definition 6.4, Lemmas 6.7--6.8, Propositions 6.9, 6.11--6.12. These do not require target support or algebraizability.', 'Proposition 8.2 gives E1 uniqueness without orthogonality. Corollary 7.3 requires orthogonality, supplied separately by the proved transfer from the synthetic source.'],
        'limitations': ['Later versions are not in this packet. The actual PDF statement of Lemma 6.10 has a positive integral of -psi, whereas its proof uses psi. Its displayed bound alone does not show integrability; manuscript (7a)--(7b) prove the needed negative-integral bound directly. Other unused printed/OCR slips are not imported.'],
    },
    '1805.01016': {
        'identity': 'Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry, actual arXiv:1805.01016v3.',
        'applications': ['Theorem 8.4 provides the uniform-continuous extension of genuine mixed MA to continuous psh metrics; smooth projective geometrically integral X and ample L are within its domain.', 'Corollary B is conditional on continuity of envelopes. It is not an unbounded E1 surjectivity theorem.'],
        'limitations': ['This is not a paper with a different pluripotential title. No general finite-energy equation theorem is inferred from its continuous operator.'],
    },
    '1801.08229': {
        'identity': 'Boucksom--Jonsson, Global pluripotential theory over a trivially valued field, arXiv:1801.08229v4.',
        'applications': ['Algebraically closed trivially valued k of characteristic zero, smooth connected integral projective X of arbitrary dimension, ample L meet Theorems 5.20 and 12.9.', 'Theorems 7.1, 7.18 and Proposition 7.19 construct the genuine finite-energy operator by the intersection pairing, with mass V before probability normalization.', 'Theorem 8.5/Corollary 8.6, Proposition 9.19, and the printed proof of Theorem 12.8 give energy differentiation, L1 continuity on bounded-energy sets, and attainment; Theorems 7.40 and 7.44 give locality/comparison.', 'Theorem 9.20 identifies finite dual energy with integrability of every E1 potential at this endpoint.'],
        'limitations': ['The trivial-field theorem is not transferred by unproved base change to the discrete or arbitrary-field settings. The characteristic-p dimension-at-most-two extension in its statement is not used.'],
    },
    '2307.01697': {
        'identity': 'Boucksom--Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach, arXiv:2307.01697v1, banner 4 Jul 2023.',
        'applications': ['Section 1.2.2 realizes the synthetic formalism on projective Berkovich spaces via model functions and intersection measures. Section 1.3.2 identifies the ample positivity class in the discrete smooth residue-zero case.', 'Example 2.20 states test-function orthogonality for projective Berkovich spaces over arbitrary non-Archimedean fields, using BE21 and BGM22 as published background. We use this stated result, not an independently fetched BGM source.', 'Proposition 2.2 (2.7), Theorem 1.26, Theorem 2.23, and Lemma 2.25 (2.27) apply to our semipositive reference theta and finite-dual-energy probability nu. The proof document proves the extension of these test estimates to BFJ E1 and the consequent discrete-field existence.', 'Theorem 2.26 and Theorem A prove completeness and density on the measure side. They alone assert neither a general unbounded-potential operator nor its surjectivity.'],
        'limitations': ['Remark 2.14 explicitly sets aside the potential theory. General-field test orthogonality is weaker than a proved continuous/finite-energy envelope theory.'],
        'published_background_used_via_this_source': [
            {'citation': 'BE21', 'identity': 'Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry, Adv. Math. 378 (2021), article 107501, 124 pp.', 'used_result': 'Theorem A in Example 2.20', 'application': 'Our smooth geometrically integral projective X is geometrically reduced; L is ample; K is complete. The corresponding supplied arXiv cache is actual 1805.01016v3.'},
            {'citation': 'BGM22', 'identity': 'Boucksom--Gubler--Martin, Differentiability of relative volumes over an arbitrary non-Archimedean field, IMRN 2022 no. 8, 6214--6242.', 'used_result': 'Lemma 3.2 in Example 2.20', 'application': 'Invoked through the explicit projective-Berkovich orthogonality assertion of supplied 2307.01697v1 Example 2.20; no independent BGM22 file was supplied or fetched. We claim only the domain expressly asserted there.'},
        ],
    },
    '2209.04879': {
        'identity': 'Pille-Schneider, Global pluripotential theory on hybrid spaces, arXiv:2209.04879v2.',
        'applications': ['Remark 4.4 explicitly separates definition of E1 over arbitrary fields from the generally unclear operator extension.', 'Theorem 4.7 treats smooth polarized varieties over k((t)) of equicharacteristic zero and skeleton-supported probability measures. Its probability convention is translated back to raw mass V in our argument.'],
        'limitations': ['The phrase discretely-valued of characteristic zero in Remark 4.4 does not license dropping the residue-characteristic-zero hypotheses of BFJ.'],
    },
    '2506.13548': {
        'identity': 'Gubler--Rabinoff, Classically psh and pluriharmonic functions on Berkovich spaces, arXiv:2506.13548v2, 17 Sep 2025.',
        'applications': ['Audit-only: introduction explicitly says defining MA and regularization may need extra hypotheses and are not its subject.'],
        'limitations': ['Its curve-pullback psh class is not substituted for the BFJ global psh cone or its finite-energy operator.'],
    },
    'Thuillier': {
        'identity': 'Thuillier thesis, supplied HAL tel-00010990v1 PDF.',
        'applications': ['Audit-only: cited potential and metric statements are for smooth strictly analytic curves.'],
        'limitations': ['No projective-line or dimension-one restriction is silently added to a general-dimension claim; the corrupted cached OCR is not used for a new theorem.'],
    },
    'Berkovich': {
        'identity': 'Berkovich, Etale cohomology for non-Archimedean analytic spaces, PMIHES 78 (1993), pp. 5--161.',
        'applications': ['Audit-only: analytic-space/cohomological background, not a finite-energy MA existence result.'],
        'limitations': ['Cohomological base change is not used as a substitute for compatibility of unbounded MA or energy.'],
    },
    '1204.6277': {
        'identity': 'Chambert-Loir--Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, actual arXiv:1204.6277v2, 25 Jul 2025; internal 29 July 2025.',
        'applications': ['Audit-only: local currents/Bedford--Taylor and model-metric material. No application to all BFJ E1 targets in arbitrary fields is established in this work.'],
        'limitations': ['No identification of its local psh class with all unbounded BFJ global potentials, compactness, dual-energy attainment or global uniqueness is inferred.'],
    },
}

def main():
    payload = (ROOT / 'input.json').read_bytes()
    data = json.loads(payload)
    original = ROOT / 'input-original.json'
    if original.exists() and original.read_bytes() != payload:
        raise RuntimeError('input-original.json differs; refusing to overwrite')
    original.write_bytes(payload)
    (ROOT / 'assignment-original.txt').write_text(data['assignment'], encoding='utf-8')
    (ROOT / 'task-original.json').write_text(json.dumps(data['task'], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    sources = json.loads(data['assignment'].split('Read-only published source caches:\n', 1)[1])
    outdir = ROOT / 'source-extracts'
    outdir.mkdir(exist_ok=True)
    entries = []
    for supplied in sources:
        url = supplied['public_source']
        key = next(k for k in EXTRACTS if k in url or k in supplied['pdf'])
        pdf = Path(supplied['pdf'])
        cached = Path(supplied['literal_extract'])
        hashes = {'pdf': digest(pdf), 'literal_extract': digest(cached)}
        checks = {'pdf': hashes['pdf'] == supplied['pdf_sha256'],
                  'literal_extract': hashes['literal_extract'] == supplied['extract_sha256']}
        if supplied.get('abstract_html'):
            hashes['abstract_html'] = digest(supplied['abstract_html'])
            checks['abstract_html'] = hashes['abstract_html'] == supplied['abstract_sha256']
        refreshed = outdir / f'{key}-from-pdf.txt'
        command = ['pdftotext', '-layout', str(pdf), str(refreshed)]
        completed = subprocess.run(command, capture_output=True, text=True)
        (outdir / f'{key}-pdftotext-diagnostics.txt').write_text(completed.stdout + completed.stderr, encoding='utf-8')
        if completed.returncode:
            raise RuntimeError(f'PDF extraction failed: {key}')
        lines = cached.read_text(encoding='utf-8').splitlines(keepends=True)
        literal_blocks = []
        for first, last in EXTRACTS[key]:
            literal = ''.join(lines[first - 1:last])
            name = f'{key}-lines-{first}-{last}.txt'
            (outdir / name).write_text(literal, encoding='utf-8')
            literal_blocks.append({'first_cached_line': first, 'last_cached_line': last,
                                   'file': 'source-extracts/' + name,
                                   'sha256': digest(outdir / name), 'literal_text': literal})
        entries.append({'key': key, 'supplied_pointer': supplied, 'actual_hashes': hashes,
                        'hash_checks': checks, 'pdf_extraction_command': command,
                        'pdf_extraction_returncode': completed.returncode,
                        'from_pdf_sha256': digest(refreshed),
                        'from_pdf_file': str(refreshed.relative_to(ROOT)),
                        'from_pdf_header': refreshed.read_text(encoding='utf-8')[:1800],
                        **CHECKS[key], 'literal_published_extracts': literal_blocks})
        print(key, 'all supplied hashes match:', all(checks.values()), 'PDF re-extraction exit:', completed.returncode)
    inspections = [
        {'source': '2307.01697v1', 'pdf_page': 25, 'file': 'source-extracts/synthetic-page25.png',
         'checked': 'Actual PDF has absolute-value bars on both (2.25) and (2.27); exponent alpha=2^{-n} and gap exponent 1/2 in (2.27). Cached OCR drops the bars.'},
        {'source': '1201.0188v1', 'pdf_page': 27, 'file': 'source-extracts/bfj-v1-page27.png',
         'checked': 'Actual PDF Definition 6.4 is increasing restricted truncation MA. Lemma 6.7 has coefficient t/[2(n+1)] and discarded mass o(t^{-1}); Lemma 6.8 has absolute-value bars.'},
        {'source': '1201.0188v1', 'pdf_page': 28, 'file': 'source-extracts/bfj-v1-page28.png',
         'checked': 'Actual PDF Lemma 6.10 displays positive integral (-psi) in its statement but negative psi integrals in its proof. This is a printed sign slip, not an OCR-only issue. Manuscript (7a)--(7b) reprove the required integrability bound. Proposition 6.9 and the comparison direction in Proposition 6.11 are also visible.'},
        {'source': '1801.08229v4', 'pdf_page': 122, 'file': 'source-extracts/bj-v4-page122.png',
         'checked': 'Actual proof of Theorem 12.8 uses potential compactness and Proposition 9.19 to obtain a maximizer. Theorem 12.9 says every finite-energy target, smooth X, char k=0 or dim X<=2, unique up to translation.'},
    ]
    for inspection in inspections:
        p = ROOT / inspection['file']
        if p.exists():
            inspection['sha256'] = digest(p)
    provenance = {'input_sha256': digest(ROOT / 'input.json'),
                  'original_input_sha256': digest(original),
                  'method': 'Only the ten explicitly supplied read-only caches were read. Literal blocks are byte-preserving UTF-8 excerpts of the cached text. Independent pdftotext -layout output was made from every actual supplied PDF; selected rendered PDF pages were inspected to resolve ambiguous formulas. Hashes establish identity, not mathematical correctness.',
                  'rendered_pdf_inspections': inspections, 'sources': entries}
    (outdir / 'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    versions = {}
    for name in ['python3', 'pdftotext', 'pdftoppm', 'pdflatex', 'latexmk']:
        args = [name, '--version'] if name in ['python3', 'pdflatex'] else [name, '-v']
        p = subprocess.run(args, capture_output=True, text=True)
        versions[name] = {'path': shutil.which(name), 'command': args, 'returncode': p.returncode,
                          'stdout': p.stdout, 'stderr': p.stderr}
    (ROOT / 'environment.json').write_text(json.dumps({'platform': platform.platform(),
                                                      'python': sys.version,
                                                      'working_directory': str(ROOT),
                                                      'versions': versions,
                                                      'external_compute': 'No supervised compute service was supplied or needed. Only lightweight text extraction and TeX compilation were run.',
                                                      'delegation': 'No model, worker, subagent, network request, installation or external message was invoked.'}, indent=2) + '\n')
    if not all(all(e['hash_checks'].values()) for e in entries):
        raise RuntimeError('A supplied hash did not match')

if __name__ == '__main__':
    main()
