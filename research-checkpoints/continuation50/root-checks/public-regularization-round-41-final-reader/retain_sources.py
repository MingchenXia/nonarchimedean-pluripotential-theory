#!/usr/bin/env python3
"""Retain only the seven authorized public caches and selected literal pages."""
from pathlib import Path
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = Path('/workspace/research/shared-sources')
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)

SOURCES = [
    ('GR-2506.13548v2-20261004', 'https://arxiv.org/pdf/2506.13548v2',
     '83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726',
     '3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b',
     [5, 6, 7, 10, 11, 18, 19, 21, 22, 23, 30, 31]),
    ('GR-2503.05513-20261004', 'https://arxiv.org/pdf/2503.05513',
     '2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b',
     '5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c',
     [15, 16, 17]),
    ('Thuillier-tel-00010990v1', 'https://theses.hal.science/tel-00010990v1/document',
     '9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a',
     'e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570',
     [19, 20, 21, 33, 34, 56, 57, 67, 68, 82, 83, 84, 87, 88, 89, 103, 104, 105]),
    ('GJR-2111.05741', 'https://arxiv.org/pdf/2111.05741',
     '572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42',
     '57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3',
     [8, 31, 32, 33, 34, 35, 36, 45, 46, 47, 76, 77, 78, 79, 80, 81]),
    ('Berkovich-PMIHES-1993-78-5', 'https://www.numdam.org/item/PMIHES_1993__78__5_0/',
     'bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af',
     '694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d',
     [30, 31, 32, 39, 40]),
    ('CD-1204.6277v2-20261004', 'https://arxiv.org/pdf/1204.6277v2',
     '5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719',
     '64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085', []),
    ('Wanner-1801.04713v3-20261004', 'https://arxiv.org/pdf/1801.04713v3',
     '8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7',
     'e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f', [2, 3, 31]),
]

VISUAL = {
    'GJR-2111.05741': [31, 35, 46, 77, 78, 80],
    'Thuillier-tel-00010990v1': [20, 34, 56, 57, 83, 87, 103, 104],
    'GR-2506.13548v2-20261004': [22, 23, 30],
    'GR-2503.05513-20261004': [15, 17],
    'Berkovich-PMIHES-1993-78-5': [32],
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

records = []
for name, url, expected_pdf, expected_txt, selection in SOURCES:
    pdf_path = SOURCE_ROOT / (name + '.pdf')
    txt_path = SOURCE_ROOT / (name + '.txt')
    pdf_bytes, txt_bytes = pdf_path.read_bytes(), txt_path.read_bytes()
    actual_pdf, actual_txt = sha(pdf_bytes), sha(txt_bytes)
    assert actual_pdf == expected_pdf, (name, 'PDF hash mismatch')
    assert actual_txt == expected_txt, (name, 'text hash mismatch')
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    # Preserve every byte of each selected cache page, including OCR/control bytes.
    literal_pages = txt_bytes.split(b'\x0c')
    outputs = []
    if selection:
        selected_doc = fitz.open()
        for page in selection:
            selected_doc.insert_pdf(doc, from_page=page-1, to_page=page-1)
            filename = f'{name}-pdf-page-{page}-literal.txt'
            (OUT / filename).write_bytes(literal_pages[page-1])
            outputs.append({'original_pdf_page': page, 'literal_file': filename,
                            'literal_sha256': sha(literal_pages[page-1])})
        selected_doc.save(OUT / (name + '-selected-pages.pdf'))
    for page in VISUAL.get(name, []):
        doc[page-1].get_pixmap(matrix=fitz.Matrix(1.35, 1.35)).save(
            OUT / f'{name}-pdf-page-{page}.png')
    records.append({
        'id': name, 'public_source': url,
        'source_pdf': str(pdf_path), 'source_literal_extract': str(txt_path),
        'pdf_sha256': actual_pdf, 'extract_sha256': actual_txt,
        'supplied_hashes_match': True, 'pdf_page_count': len(doc),
        'selected_pdf_pages': selection, 'literal_page_files': outputs,
        'role': 'unused hash-checked source' if not selection else
                ('comparison only' if name.startswith('Wanner') else 'checked foundation'),
    })

applications = [
    {'claim': 'Starting class and non-rig finiteness',
     'source': 'GR-2506.13548v2-20261004', 'pages': [10, 11, 18, 19, 21, 22],
     'check': 'Smooth separated pure-dimension-one strict curve; use 3.4.1 including '
              'identically -infinity, not a finite-continuous replacement class. '
              'Definition 4.1 quantifies over all analytic extensions.'},
    {'claim': 'A compact-domain lisse net, not a sequence',
     'source': 'Thuillier-tel-00010990v1', 'pages': [103, 104],
     'check': 'Printed 89--90: finite S in I(Y) containing actual boundary; '
              'f_S continuous finite on Y, subharmonic on Y minus boundary. '
              'The new Lindelof extraction in the argument needs second countability.'},
    {'claim': 'Lisse skeletal representation only',
     'source': 'Thuillier-tel-00010990v1', 'pages': [82, 83, 84],
     'check': 'All-domain Definition 3.2.1 is not strict PL. Proposition 3.2.4 proof '
              'treats phi in A^0(Y), compact strict Y, and a finite separable extension. '
              'Original corners need not lie in the value group.'},
    {'claim': 'Skeletal scalar extension and graph positivity',
     'source': 'Thuillier-tel-00010990v1', 'pages': [19, 20, 21, 56, 57, 87, 88, 89, 104, 105],
     'check': 'Weighted outgoing slopes; 2.2.21 weighted G-local skeletal isomorphism; '
              '3.2.10 graph pullback formula on Y minus boundary; 3.4.4 positivity; '
              'new chord proof gives convexity/positive masses at all replacement vertices.'},
    {'claim': 'Actual strict approximant membership',
     'source': 'GJR-2111.05741', 'pages': [31, 32, 33, 77, 78, 79, 80],
     'check': 'All replacement mesh and star/interval cut coordinates are actual '
              'Gamma_M values after finite separable roots. 15.3--15.4 supply admissible '
              'formal models and integral star basis functions. 5.5--5.7 make their '
              'real linear combinations strict R-PL. A finite neighbourhood G-cover '
              'has identical formulas on overlaps.'},
    {'claim': 'Descent to original K',
     'source': 'GJR-2111.05741', 'pages': [34, 35, 36, 46, 47],
     'check': 'Average over finite Galois M/K; continuous quotient descent proved '
              'in the argument; projection finite free flat and surjective; '
              '5.12 with divisible group R supplies strict membership across '
              'the ground fields; its finite case is explicitly 5.11. '
              'GR-classical 3.5(7) supplies subharmonicity descent.'},
    {'claim': 'Semipositivity after membership and all pullbacks',
     'source': 'GR-2506.13548v2-20261004', 'pages': [22, 23],
     'check': 'Theorem 4.3 requires good strict space and nontrivial valuation; '
              'it is applied only after strict R-PL has been proved. '
              'GJR 5.4 and 7.6 give morphism/scalar preservation without requiring '
              'a finite bundle projection.'},
    {'claim': 'Compact projective fibre constancy for arbitrary u',
     'source': 'GR-2506.13548v2-20261004', 'pages': [5, 6, 7, 21, 22, 30, 31],
     'check': 'Scalar pullback to H(b), inclusion of projective fibre; finite '
              'usc maximum on compact boundaryless connected fibre and 6.1. '
              'This fails as an argument on nonsaturated fibre charts.'},
    {'claim': 'Ordinary neighbourhoods and normal geometry',
     'source': 'Berkovich-PMIHES-1993-78-5', 'pages': [30, 31, 32, 39, 40],
     'check': '1.5.5 identifies domain interior with ordinary topological interior '
              'and handles finite scalar boundaries. 2.2.7 gives regularity/normality '
              'of algebraic analytifications. No normalization descent is assumed.'},
    {'claim': 'Cached numbering reconciliation',
     'source': 'GR-2503.05513-20261004', 'pages': [15, 16, 17],
     'check': 'June proof cites earlier 3.1 and 3.5; actual March cache has '
              'Proposition 5.1 and Corollary 5.4, with checked curve hypotheses.'},
    {'claim': 'Ordinary smoothness comparison only',
     'source': 'Wanner-1801.04713v3-20261004', 'pages': [3, 31],
     'check': 'Corollary 5.4 finite continuous input, smooth proper curve, '
              'residue algebraic over finite field or projective line/Mumford. '
              'No ordinary smoothness conclusion is inferred from the new PL proof.'},
]

provenance = {
    'scope': 'Only user-listed public source caches; no unpublished book premise.',
    'sources': records, 'application_checks': applications,
    'primary_pdf_visual_checks': [
        {'source': 'GJR-2111.05741', 'pages': [77, 78],
         'resolved': 'sqrt(Gamma) is the divisible hull; actual Gamma vertices '
                     'suffice for admissible subdivisions. 15.4 uses integral slopes '
                     'and Gamma intercepts, not arbitrary real affine coefficients.'},
        {'source': 'Thuillier-tel-00010990v1', 'pages': [34, 83, 103, 104],
         'resolved': 'X_G is all-domain; X_R is strict. 3.2.4 says finite separable '
                     'extension and its proof covers A^0(Y). 3.4.2 is a decreasing '
                     'family, with compact-domain h_S, not a published sequence.'},
        {'source': 'Thuillier-tel-00010990v1', 'pages': [56, 87],
         'resolved': '2.2.21 states weighted G-local skeletal compatibility. '
                     'OCR target A^0_Y in 3.2.10 is also a printed typographical '
                     'inconsistency: the operator displayed immediately above '
                     'has target A^1_X and (ii) is explicitly in A^1_Y. '
                     'Only the unambiguous graph-to-measure formula is used.'},
        {'source': 'Berkovich-PMIHES-1993-78-5', 'pages': [32],
         'resolved': 'The good composition equality in 1.5.5(ii), printed page 35, '
                     'is Int(Z/X)=Int(Z/Y) intersect psi^-1(Int(Y/X)). '
                     'Only this equality is used for finite scalar-extension '
                     'boundary identities; the preceding printed inclusion '
                     'has inconsistent ambient sets and is not used.'},
    ],
    'limits': 'Literal excerpts and matching hashes are provenance evidence, '
              'not verification of the mathematical claims.',
}
(OUT / 'source-provenance.json').write_text(
    json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'hash_checks': len(records),
                  'selected_pdf_pages': sum(len(x['selected_pdf_pages']) for x in records),
                  'application_checks': len(applications), 'all_match': True}))
