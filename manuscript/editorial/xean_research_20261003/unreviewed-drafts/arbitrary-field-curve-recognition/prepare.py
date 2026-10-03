#!/usr/bin/env python3
"""Assemble the self-contained argument from inspected proof bodies and primary texts.

Only this fresh workspace is written. Source slicing uses newline boundaries, never
str.splitlines(). Copied mathematical arguments are proof text to be checked here,
not assertions adopted by virtue of their earlier origin or disposition.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent
R11 = Path('/workspace/research/campaigns/round-11/P06.2-completed-algebraic-curve-continuation/artifacts/codex-Ntn6OZ')
R04 = Path('/workspace/research/campaigns/round-04/P06.2-curve-recognition-continuation/artifacts/codex-7SD6B9')
R07 = Path('/workspace/research/deliverables/round-07')
SHARED = Path('/workspace/research/shared-sources')
BOOK = Path('/workspace/research/book-source/manuscript')
(ROOT/'sources').mkdir(exist_ok=True)
(ROOT/'evidence').mkdir(exist_ok=True)
manifest = []

def read(path):
    data = path.read_bytes()
    manifest.append({'origin': str(path), 'bytes': len(data),
                     'sha256': hashlib.sha256(data).hexdigest(),
                     'role': 'evidence, never a predecessor theorem grant'})
    return data.decode('utf-8')

def copy_source(path, name):
    text = read(path) if path.suffix != '.pdf' else None
    if text is None:
        data=path.read_bytes()
        manifest.append({'origin':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'role':'primary PDF'})
    shutil.copyfile(path, ROOT/'sources'/name)
    return text

def between(text, start, end):
    return text[text.index(start):text.index(end, text.index(start))]

old_t = read(R11/'P06.2-argument.md')
old_c = read(R07/'P06.2-curve-recognition-argument.md')
transport = between(old_t, '## 2. Exact analytic dependencies', '## 14. Comparison')
transport = re.sub(r'^(## |### )(\d+(?:\.\d+)*)\.', r'\1T\2.', transport, flags=re.M)
transport = re.sub(r'\bSections? (\d+)(?:--(\d+))?', lambda m: ('T'+m[1]+('--T'+m[2] if m[2] else '')), transport)
transport = transport.replace('T15', 'Appendix S')
transport = transport.replace('t_{gf}^{,k}', 't_{gf}^{k}')
transport = transport.replace('All these source statements apply', 'The stated calibration and form statements apply')
setup = between(old_t, 'For finite\nseparable ascent', 'This is a scalar transport theorem') if 'For finite\nseparable ascent' in old_t else ''
# Recreate the local equation references without importing the old result's status.
setup = r'''
For a finite Galois stage the approximation assertion proved below is that an
invariant compact ordinary scalar test $\beta$ has downstairs compact smooth
approximants $\alpha_j$ supported in one compact $H$, with all errors supported
in $\pi^{-1}H$, such that
\[
 \big\|(D(\beta-\pi^*\alpha_j))_{\mathrm{Rad}}\big\|_{\mathrm{TV}}\to0.\tag{2}
\]
Set
\[
 B_u(\psi)=\int_Zu(D\psi)_{\mathrm{Rad}}.\tag{3}
\]
Equation (1) denotes the equivalence in the transport lemma, while (2) and
(3) are local equation labels for T. The proof handles finite separable,
finite inseparable, mixed embedded finite stages, then the completion.

'''

prime_positive = between(old_c, '## Elementary reducedness and prime avoidance', '## Closed-embedding test lifting')
pl_cut = between(old_c, '## Poincare--Lelong on an S1 source', '## Finite-residue-field scalar germs')
cuts = between(old_c, '## Proper effective cuts containing a prescribed analytic curve', '## Normalization: isomorphism')
q = prime_positive + pl_cut + cuts
q = q.replace('Lemma 2', 'C1').replace('Theorem B', 'the puncture-removal lemma C2')
q = q.replace('This proves Theorem A.', 'This proves the closed-curve restriction lemma in the stated arbitrary-field scope.')
q = re.sub(r'input[s]? [1-8]', 'the exact analytic/calculus foundations stated in T, C, and Q', q, flags=re.I)
q = q.replace('Lemma 5', 'the rigid-germ assertion C2').replace('Lemma 6', 'the radial-cutoff construction C2')
q = q.replace('A fresh BGR', 'A BGR')
q = q.replace('the exact analytic/calculus foundations stated in T, C, and Q supplies', 'the relative-dimension foundations stated above supply')

image = between(old_c, '## The affinoid branch lemma, including Banach factorization', '## Intrinsic equations on local images')
image = image.replace('Lemma 3', 'the image branch lemma').replace('As in Lemma 1', 'As in C4')
image = image.replace('**the image branch lemma.**', '**Image branch lemma.**')
image = image.replace('Proof of Proposition B', 'Proof of the local-image lemma')
image = image.replace('S2', 'the affinoid foundations stated in C and T').replace('S3', 'the local finiteness foundations stated here')
image = image.replace("the affinoid foundations stated in C and T's", 'The stated')
image = image.replace('the affinoid foundations stated in C and T and', 'the stated affinoid foundations and')
image_open = r'''
## Q-local images. Exact hypotheses and statement

CLD 11.4.4 says finite analytic maps to an affinoid are equivalent to finite
Banach algebra maps; their finite-module quotient topologies are determined
by the ring module structure. For a nontrivially valued ground field and a
strict affinoid base, a Banach algebra finite as a ring algebra is finite
Banach. CLD 11.4.5 says the locus of relative fibre dimension at least a
fixed integer is Zariski closed, and a morphism is finite at a point exactly
when its local relative dimension is zero and it has no relative boundary
there. Finite at a point means finite from an analytic neighbourhood to an
analytic neighbourhood. These are pointwise criteria; the different entire
fibre criterion with a compactness hypothesis, CLD 11.6.6, is not used.
The exact statements and Berkovich's local-finiteness proof bodies appear
below. The boundary equality of C shows no relative boundary for a smooth
curve map to a separated boundaryless target.

**Local-image lemma.** For an analytic map $f:Y\to X$ from a separated
smooth strict curve to a good separated strict boundaryless analytic space,
near every analytic source point either the map is constant with value a
rigid point, through a finite field over $K$, or there are actual strict
affinoid neighbourhoods $W,V$ on which the map is finite, with a reduced
closed pure curve image $C\hookrightarrow V$ and $W\to C$ finite surjective.
The source neighbourhood can be chosen connected and normal and the map
then lifts finitely to the normalization of $C$. No perfection, separability,
or finite flatness assumption occurs. The following proves the statement.

'''

source_texts = {}
for label in ['CLD','GR']:
    source_texts[label]=copy_source(R04/'sources'/f'{label}.txt',f'{label}.txt')
    copy_source(R04/'sources'/f'{label}.pdf',f'{label}.pdf')
source_texts['CLD-curve']=source_texts['CLD']
copy_source(R04/'sources/CLD.txt','CLD-curve.txt')
source_texts['CLD']=copy_source(R11/'sources/CLD.txt','CLD.txt')
assert hashlib.sha256((R11/'sources/CLD.pdf').read_bytes()).digest()==hashlib.sha256((ROOT/'sources/CLD.pdf').read_bytes()).digest(), 'CLD PDF versions differ'
for label, stem in [('Wanner','Wanner-1801.04713v3'),('GJR','GJR-2111.05741'),
                    ('van-der-Put','van-der-Put-AIF-1980-30-4-155'),
                    ('Berkovich','Berkovich-PMIHES-1993-78-5'),
                    ('Thuillier','Thuillier-tel-00010990v1'),
                    ('Ducros','Ducros-S1793744212500077')]:
    source_texts[label]=copy_source(SHARED/f'{stem}.txt',f'{label}.txt')
    copy_source(SHARED/f'{stem}.pdf',f'{label}.pdf')
corrected = read(SHARED/'completed-algebraic-corrected-primary-bodies.md')
copy_source(SHARED/'Thuillier-verified-transcription.md', 'Thuillier-verified-transcription.md')
copy_source(SHARED/'curve-recognition-review-primary-bodies.md','curve-primary-bodies.md')
copy_source(BOOK/'parts/part6/ch72_major_open_problems.tex', 'controlling-ch72.tex')
copy_source(BOOK/'appendices/appM_ch18_frontiers.tex', 'controlling-appM.tex')

checks=[]
for match in re.finditer(r'## (?:Additional complete body: )?(CLD|GR)\.txt, newline lines (\d+)–(\d+)\n\n```text\n(.*?)\n```',corrected,re.S):
    label,a,b,body=match.groups(); a=int(a);b=int(b)
    extracted='\n'.join(source_texts[label].split('\n')[a-1:b]).replace('\f','')
    assert extracted==body,(label,a,b,'corrected passage mismatch')
    checks.append({'source':label,'first_newline':a,'last_newline':b,'exact_match':True,'characters':len(body)})
assert len(checks)>=25, len(checks)

appendix = '\n# Appendix S. Primary bodies, extracted by newline boundaries\n\n'
appendix += ('The following are primary source data. Statements and complete proof bodies\n'
             'are included so applications can be checked in this document. Quotation\n'
             'does not assert correctness of every unused sentence. In particular the\n'
             'universal moment-dimension reading of CLD 12.2.4, the broad fixed-index\n'
             'compact-support reading of 15.2.9, and the unsupported S1 reduction\n'
             'in 16.7.5 are unused. Form-feed page markers alone are removed.\n\n')
appendix += corrected[corrected.index('## CLD.txt, newline lines'):]

# Whole identifiers and their proof boundaries were inspected in the actual text.
ranges={
 'CLD-curve':[(910,978),(15082,15286),(15362,15566),(15605,15677),(15700,15755),
        (19240,19275),(19660,19720),(21280,21445),(23340,23453),(23454,23586),
        (7910,8188),(9290,9445),(6860,7020)],
 'GR':[(70,138),(250,405),(454,1190),(1832,1859)],
 'Wanner':[(168,202),(447,519),(680,742),(991,1606)],
 'van-der-Put':[(1,230)],
 'GJR':[(1610,1799),(1800,1985),(1986,2307),(2308,2435),(3890,4047)],
 'Berkovich':[(1350,1444),(2200,2347)],
 'Thuillier':[(3070,3455),(3550,3765)]
}
extra=[]
for label, pairs in ranges.items():
    lines=source_texts[label].split('\n')
    for a,b in pairs:
        assert 1<=a<=b<=len(lines),(label,a,b,len(lines))
        body='\n'.join(lines[a-1:b]).replace('\f','')
        appendix+=f'\n## {label}, newline lines {a}--{b}\n\n```text\n{body}\n```\n'
        extra.append({'source':label,'first_newline':a,'last_newline':b,'sha256':hashlib.sha256(body.encode()).hexdigest()})
appendix += '\n## Thuillier: visually checked primary transcription\n\n'+(ROOT/'sources/Thuillier-verified-transcription.md').read_text()
appendix += '\n# Bibliography\n\n'+r'''
* A. Chambert-Loir and A. Ducros, *Formes différentielles réelles et courants
  sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025.
* W. Gubler and J. Rabinoff, *Classically psh and pluriharmonic functions on
  Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025.
* W. Gubler, P. Jell, and J. Rabinoff, *Forms on Berkovich spaces based on
  harmonic tropicalizations*, cached arXiv:2111.05741v3. Cached numbering,
  not an uninspected journal renumbering, controls applications here.
* V. Wanner, *Comparison of two notions of subharmonicity on non-archimedean
  curves*, cached arXiv:1801.04713v3; published Math. Z. 293 (2019), 443--474.
* M. van der Put, *The class group of a one-dimensional affinoid space*,
  Ann. Inst. Fourier 30(4) (1980), 155--164, Theorem 1.1.
* A. Thuillier, thesis, HAL tel-00010990v1, Theorem 2.3.8 and the explicit
  algebraic-domain assertion in its proof; Lemma 2.3.9 and the scalar
  harmonic functoriality used in GR's supplied proof.
* V. Berkovich, *Étale cohomology for non-Archimedean analytic spaces*,
  Publ. Math. IHÉS 78 (1993), Sections 1.5--1.6 and 3.1.
* S. Bosch, U. Güntzer, R. Remmert, *Non-Archimedean Analysis*, Springer
  (1984), 3.2.4/2 and 6.1.2/1, the finite-valued-field and strict
  Nullstellensatz foundations stated exactly in the text.
* A. Ducros, *Variation de la dimension relative en géométrie analytique
  p-adique*, Compositio Math. 143 (2007), 1511--1532, Theorem 4.9, in the
  local fibre-dimension formulation stated by CLD 11.4.5. The additional
  cached polyhedrality body is separately included with the corrected
  transport sources; no universal dimension equality is used.
'''

argument=(ROOT/'bridge.md').read_text()+setup+transport+(ROOT/'curve-proof.md').read_text()
argument+=(ROOT/'consequence-opening.md').read_text()+q+image_open+image
argument+=(ROOT/'consequence-ending.md').read_text()+appendix
(ROOT/'P06.2-argument.md').write_text(argument)
(ROOT/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(ROOT/'evidence/source-checks.json').write_text(json.dumps({'newline_only':True,'corrected_exact_bindings':checks,'additional_primary_ranges':extra,'limit':'Byte binding is not mathematical verification.'},indent=2)+'\n')
print(json.dumps({'argument_bytes':len(argument.encode()),'corrected_ranges_bound':len(checks),'additional_ranges':len(extra),'predecessor_results_as_premises':False}))
