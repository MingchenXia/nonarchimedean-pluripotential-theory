#!/usr/bin/env python3
"""Retain exact cached pages and selected PDF images; no network operations."""
import hashlib
import json
from pathlib import Path
import fitz

ROOT = Path('/workspace/research/shared-sources')
OUT = Path('source-extracts')
OUT.mkdir(exist_ok=True)
SOURCES = [
    dict(id='GR1', url='https://arxiv.org/pdf/2506.13548v2',
         stem='GR-2506.13548v2-20261004',
         pdf_hash='83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726',
         text_hash='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b',
         selections=[('foundations',6,9),('curve-definitions-and-proofs',10,21),
                     ('classical-definition-and-PL-positivity',21,23),
                     ('local-maximum-principle',30,31),('affinoid-maximum-and-nets',33,34)],
         applications=['Definition 3.4 and 4.1 quantify over all analytic extensions.',
                       '3.4.1 identifies the extended and Thuillier conventions on smooth connected curves.',
                       'Proposition 3.5(3,7,8) supplies boundary extension and scalar/finite descent.',
                       'Lemmas 3.7--3.9 supply the perfected/reduced curve normalization facts.',
                       'Proposition 4.2(5,6) and Theorem 4.3 supply pullback/scalar stability and PL classical positivity.',
                       'Theorem 6.1 makes continuous competitors constant on connected proper boundaryless fibers.',
                       'Theorem 6.4 applies to the entire competitor family on closed polydisc and extended-disc tests.']),
    dict(id='GR2', url='https://arxiv.org/pdf/2503.05513',
         stem='GR-2503.05513-20261004',
         pdf_hash='2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b',
         text_hash='5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c',
         selections=[('standing-boundary-conventions',4,5),('curve-comparison',15,17)],
         applications=['Standing convention: smooth means rig-smooth and boundaryless.',
                       'Proposition 5.1 and Corollary 5.4 are the comparison statements in this cached version.',
                       'GR1 references an older GR2 numbering (3.1/3.5); no argument here treats the differing numbers as identical.']),
    dict(id='Thu', url='https://theses.hal.science/tel-00010990v1/document',
         stem='Thuillier-tel-00010990v1',
         pdf_hash='9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a',
         text_hash='e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570',
         selections=[('field-convention',29,30),('standing-curve-and-supremum',75,76),
                     ('curve-pullback',78,78),('scalar-pullback',105,105)],
         applications=['Proposition 3.1.8(iii): increasing locally bounded subharmonic family on an open subset of a smooth strict curve.',
                       'Anchored finite maxima ensure the two-sided local boundedness literally required.',
                       'This result is used only on the interior of a rig-smooth normalized curve.',
                       'The PDF was visually checked: the result is 3.1.8(iii), not Lemma 3.1.9.']),
    dict(id='GJR', url='https://arxiv.org/pdf/2111.05741', stem='GJR-2111.05741',
         pdf_hash='572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42',
         text_hash='57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3',
         selections=[('PL-definition-and-pullback',30,32),('finite-PL-descent',34,36),
                     ('residue-and-semipositivity',44,47)],
         applications=['Definition 5.1 makes R-PL functions finite continuous and uses the strict G-topology.',
                       'Lemma 5.4 and Proposition 7.6 preserve PL/semipositivity under morphisms and arbitrary analytic extensions.',
                       'Corollary 5.12 with Lambda=R descends the base function from one finite extension giving a point of the projective factor.',
                       'Definition 7.8 says LFS is R-PL with semiample residues, hence semipositive.',
                       'The PDF 7.9 presentation uses nonnegative combinations and max of NEGATIVE logs of INVERTIBLE functions.',
                       'Only rational common-denominator maxima are used in the new examples; arbitrary R-PL max closure is not assumed.']),
    dict(id='Ber', url='https://www.numdam.org/item/PMIHES_1993__78__5_0/',
         stem='Berkovich-PMIHES-1993-78-5',
         pdf_hash='bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af',
         text_hash='694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d',
         selections=[('coherent-finite-modules',22,23),('proper-and-boundary',31,32),('regularity-of-domains',36,40),
                     ('analytification-and-properness',48,51),('smooth-morphisms',64,66),
                     ('openness',73,74),('proper-connectedness-comparison',125,127)],
         applications=['Proposition 1.3.4 and the preceding finite-module discussion identify coherent analytic germ kernels for the explicit irreducible point pinching.',
                       'Propositions 2.6.1 and 2.6.9 give boundaryless analytification, base change, and projective properness.',
                       'Theorem 7.1.1 in degree zero, for a finite constant sheaf on a proper scheme, proves connectedness of every projective analytic fiber.',
                       'Proposition 3.5.8 and 3.5.2 prove the product projection smooth, even when the base has absolute boundary.',
                       'Corollary 3.7.4 says a smooth morphism is an open map, in the ordinary topology.',
                       'Corollaries 2.2.7--2.2.8 identify regularity on algebraic analytifications and affinoid domains.']),
]

provenance = {'kind':'checked public primary source selections', 'sources':[]}
for source in SOURCES:
    stem = source['stem']
    pdf = ROOT / (stem+'.pdf')
    txt = ROOT / (stem+'.txt')
    actual_pdf = hashlib.sha256(pdf.read_bytes()).hexdigest()
    actual_txt = hashlib.sha256(txt.read_bytes()).hexdigest()
    assert actual_pdf == source['pdf_hash'], stem+' PDF bytes changed'
    assert actual_txt == source['text_hash'], stem+' text bytes changed'
    pages = txt.read_text().split('\f')
    extracts = []
    for label,first,last in source['selections']:
        filename = OUT / (source['id']+'-'+label+'.literal.txt')
        filename.write_text('\f'.join(pages[first-1:last]))
        extracts.append({'file':str(filename),'pdf_pages':[first,last],
                         'sha256':hashlib.sha256(filename.read_bytes()).hexdigest()})
    provenance['sources'].append({**source,'pdf':str(pdf),'literal_extract':str(txt),
                                 'actual_pdf_sha256':actual_pdf,'actual_text_sha256':actual_txt,
                                 'retained_extracts':extracts})

images = [('Thu',76,'Thuillier-3.1.8-pdf.png'),('GJR',47,'GJR-7.8-7.9-pdf.png'),
          ('Ber',74,'Berkovich-3.7.4-pdf.png'),('Ber',125,'Berkovich-7.1.1-pdf.png'),
          ('GR1',21,'GR1-4.1-pdf.png')]
provenance['pdf_images'] = []
for sid,page,filename in images:
    src = next(s for s in SOURCES if s['id']==sid)
    doc = fitz.open(ROOT/(src['stem']+'.pdf'))
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(str(OUT/filename))
    provenance['pdf_images'].append({'source':sid,'pdf_page':page,'file':str(OUT/filename)})
provenance['proof_scope'] = 'Published foundations are cited; all new geometric applications are proved in P03.1-argument.md and P03.1-paper.tex.'
provenance['warning'] = 'Hashes identify bytes and rendering records OCR checks; neither verifies mathematics.'
Path('source-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
print('Retained',sum(len(s['selections']) for s in SOURCES),'literal page selections and',len(images),'PDF images.')
