#!/usr/bin/env python3
"""Reproduce provenance/excerpts using only input.json and the ten allowed caches."""
import hashlib, json, pathlib, platform, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent
data = json.loads((ROOT / 'input.json').read_text())
assignment = data['assignment']
sources = json.JSONDecoder().raw_decode(assignment.split('Read-only published source caches:', 1)[1].lstrip())[0]
out = ROOT / 'source-extracts'
out.mkdir(exist_ok=True)
selections = {
    '1201.0187': [(105, 145), (1315, 1345), (1690, 1750), (1819, 1900), (2034, 2055), (2206, 2291)],
    '1201.0188': [(62, 105), (230, 332), (1400, 1439), (1540, 1564), (1932, 1946), (2054, 2112)],
    '1805.01016': [(1, 21), (2548, 2583), (2640, 2766), (3121, 3215), (3540, 3584), (3587, 3603), (3848, 3876)],
    '1801.08229': [(102, 200), (2808, 2852), (2894, 2916), (2977, 3068), (3649, 3700), (3789, 3850), (3916, 4080), (4130, 4202), (4529, 4605), (4838, 4864), (4865, 4963), (5131, 5159), (5180, 5268), (5245, 5268), (5445, 5459), (6080, 6147), (6310, 6322)],
    '2307.01697': [(50, 158), (346, 383), (508, 532), (1022, 1040), (1113, 1168)],
    '2209.04879': [(354, 394), (1940, 2006)],
    '2506.13548': [(1, 119)],
    'tel-00010990': [(1, 69), (347, 423), (5257, 5280)],
    'Berkovich-PMIHES': [(1, 16), (92, 160)],
    '1204.6277': [(1, 27), (583, 606), (645, 670)],
}
checks = {
    '1201.0187': ['Complete discretely valued K; char(residue K)=0; smooth projective X; ample L.', 'SNC cofinality enters definition, skeleton approximation and compactness; multiplier ideals/vanishing enter model positivity and envelope regularization.', 'No theorem here is applied over positive residue characteristic.'],
    '1201.0188': ['Actual saved PDF is v1, with algebraizability in the function-field-completion sense and SNC-dual-complex support in Theorem A.', 'Algebraizability is not merely that X is an algebraic K-variety; L need not descend in this v1 statement.', 'Appendix A uses algebraizability for orthogonality. No later-version hypothesis is silently substituted.'],
    '1805.01016': ['Actual paper is Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points.', 'Smooth X is geometrically reduced; ample L is semiample, so Theorem 9.15 applies to continuous psh metrics over every complete valued field.', 'Conjecture 7.30 is not a theorem. Section 7.30 reports a characteristic-p discrete envelope result only with function-field descent of (X,L) and assumed resolution in dimension n+d; the cited GJKM19 primary paper is not among the ten inputs.', 'The continuous psh result is not an unbounded E1 existence theorem.'],
    '1801.08229': ['Ground field in the main text is algebraically closed and trivially valued.', 'For the partial theorem use smooth connected projective X, an ample honest line bundle L, canonical trivial reference, n>=1, and char(k)=p>0.', 'Theorem 7.18 and Proposition 7.19 construct the genuine finite-energy operator in every dimension; Theorem A gives strong continuity/injectivity with dense image.', 'Theorem 5.20 and 12.9 give unconditional positive-characteristic surjectivity only for n<=2; the resolution in the envelope proof is on a test configuration of dimension n+1<=3.', 'Theorem 12.8 proves the equivalence of the envelope property, E1 completeness and surjectivity in this trivial-valuation setting only.'],
    '2307.01697': ['Smooth projective X over any complete non-Archimedean K and a positive model curvature representative of an ample L fit the projective Berkovich example.', 'Do not assert HBC=N1 over arbitrary K; Section 1.3.2 uses the preimage of the ample cone instead.', 'Example 2.20 establishes orthogonality using published BE21 and BGM22 inputs; Theorem 2.23 gives strong convergence of measures for maximizing test sequences.', 'The paper explicitly does not investigate potentials of finite energy. Its complete measure space is not identified here with E1/R for positive residue characteristic.'],
    '2209.04879': ['Section 1.2 assumes equicharacteristic zero, even where a later Remark 4.4 uses the shorter words characteristic zero.', 'Theorem 4.3 gives continuous psh MA; Remark 4.4 distinguishes a definition of E1 from an extension of MA to E1.', 'No application to mixed characteristic is inferred from the short wording in Remark 4.4.'],
    '2506.13548': ['Actual cached PDF is v2 dated 17 September 2025.', 'The paper concerns classically psh functions, analytic curves and maximum principles; it expressly excludes the construction of Monge--Ampere measures from its subject.', 'The R-PL positivity identification does not give the global finite-energy equation theorem.'],
    'tel-00010990': ['Thuillier thesis is curve potential theory; title page gives defense 13 October 2005 and version 4 October 2005.', 'No higher-dimensional finite-energy equation result is inferred from curve subharmonicity.', 'The cached text has severe font-encoding omissions; no delicate formula from this extract is used.'],
    'Berkovich-PMIHES': ['Berkovich 1993 is Etale cohomology for non-Archimedean analytic spaces, not a finite-energy equation paper.', 'Analytic-space foundations do not by themselves supply envelopes, energy compactness or unbounded comparison.'],
    '1204.6277': ['Actual PDF is v2 posted 25 July 2025; interior date is 29 July 2025.', 'Section 0.2.15 states characteristic-independent local forms/currents, without resolution or alterations.', 'Local Bedford--Taylor/metric curvature theory is not used as a proof of global E1 compactness or existence.', 'No identification of an arbitrary global BFJ singular metric with the local regularizable psh class is assumed.'],
}

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

records = []
for index, s in enumerate(sources, 1):
    pdf = pathlib.Path(s['pdf']); literal = pathlib.Path(s['literal_extract'])
    key = next(k for k in selections if k in str(pdf))
    for field, file in [('pdf_sha256', pdf), ('extract_sha256', literal)]:
        actual = digest(file)
        if actual != s[field]:
            raise RuntimeError(f'{file.name}: {field} mismatch: {actual}')
    stem = f'{index:02d}-{key}'
    shutil.copyfile(pdf, out / (stem + '.pdf'))
    shutil.copyfile(literal, out / (stem + '-cache-literal.txt'))
    if 'abstract_html' in s:
        html = pathlib.Path(s['abstract_html'])
        if digest(html) != s['abstract_sha256']:
            raise RuntimeError(f'{html.name}: abstract hash mismatch')
        shutil.copyfile(html, out / (stem + '-abstract.html'))
    regenerated = out / (stem + '-pdf-layout.txt')
    cmd = ['pdftotext', '-layout', str(out / (stem + '.pdf')), str(regenerated)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    (out / (stem + '-pdftotext-diagnostics.txt')).write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(cmd)
    # rg line numbers count LF only; str.splitlines also splits form feeds.
    raw_literal = literal.read_text()
    lines = raw_literal.splitlines(keepends=True) if '\f' not in raw_literal else raw_literal.split('\n')
    if '\f' in raw_literal:
        lines = [line+'\n' for line in lines[:-1]] + [lines[-1]]
    excerpts = []
    for a, b in selections[key]:
        exact = ''.join(lines[a-1:b])
        name = stem + f'-literal-lines-{a}-{b}.txt'
        (out / name).write_text(exact)
        # Physical PDF page numbers are obtained from the original form-feed text.
        original = literal.read_text()
        line_offset = sum(len(x) for x in lines[:a-1])
        end_offset = sum(len(x) for x in lines[:b])
        excerpts.append({'cache_line_start': a, 'cache_line_end': b, 'file': name,
                         'sha256': digest(out / name), 'literal_text': exact,
                         'pdf_physical_page_start': original[:line_offset].count('\f')+1,
                         'pdf_physical_page_end': original[:end_offset].count('\f')+1})
    records.append({'local_source_id': stem, 'supplied': s,
                    'verified_pdf_sha256': digest(pdf), 'verified_extract_sha256': digest(literal),
                    'pdf_header_first_lines': regenerated.read_text().splitlines()[:24],
                    'regenerated_layout_sha256': digest(regenerated), 'pdftotext_command': cmd,
                    'application_checks': checks[key], 'literal_published_extracts': excerpts})
provenance = {'policy': 'Only the input and ten explicitly allowed public caches were read. Literal extracts retain source wording, typos and OCR. Regenerated PDF text and selected page images arbitrate delicate formulas.',
              'input_sha256': digest(ROOT / 'input.json'), 'input_original_sha256': digest(ROOT / 'input-original.json'),
              'sources': records,
              'mathematical_status': 'Published source applications and audit; no full P16.3 extension proved.'}
(out / 'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')
version = subprocess.run(['pdflatex', '--version'], capture_output=True, text=True)
(ROOT / 'environment.txt').write_text('Python: '+sys.version+'\nPlatform: '+platform.platform()+'\n'+version.stdout+'\nNo installs, remote calls, worker calls, or heavy computation used.\n')
print(json.dumps({'verified_sources': len(records), 'verified_pdf_and_literal_hashes': 2*len(records),
                  'verified_abstract_hashes': sum('abstract_html' in s for s in sources),
                  'byte_identical_input': (ROOT/'input.json').read_bytes() == (ROOT/'input-original.json').read_bytes(),
                  'literal_excerpts': sum(len(r['literal_published_extracts']) for r in records)}, indent=2))
