#!/usr/bin/env python3
"""Retain literal selected pages from the six supplied published primary caches."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-extracts'
META = {
 'CD': {'pages':list(range(195,202))+list(range(344,348))+[421,422,432,433,213,214],
        'version':'arXiv v2, 25 July 2025',
        'applications':[
          '8.1.1/8.1.4: ordinary smooth stage 0; decreasing sequences define successors; v2 is a version, not stage 2.',
          '8.1.5 with 12.4.5: analytic morphisms, including analytic field extensions, preserve each ordinal stage.',
          '12.4.1/12.4.6; 15.1.1(b)/15.1.2: canonical refined analytic G-tropical structure; ordinary open moment charts.',
          '15.7.1/15.7.2: pure dimension and actual relative boundary; all positive proofs use boundaryless domains.',
          '8.3.1(b): positive current implies positive form only after ordinary smoothness is established.',
          '8.9.4: convex log-sum-exp moment functions are ordinary smooth psh.']},
 'GJR':{'pages':[30,31,46,47,48,49,50,64,65,77,78,79,80,81],
        'version':'exact supplied arXiv:2111.05741 version',
        'applications':[
          '5.1/5.4 and 7.6: real PL, semipositivity and their scalar/morphism pullbacks.',
          '7.8/7.9: LFS is semipositive RPL; ordinary local finite maxima of unit log norms.',
          '7.10 and full proof: interior point is required; common ordinary open tube with uniformly convergent LFS sequence. New stage bookkeeping gives stage 2.',
          '10.10: ordinary smooth sheaf is the CLD ordinary smooth sheaf.',
          '15.7: rig-smooth curve harmonic definitions agree; boundary cases distinguished.',
          '15.10: residue algebraic over finite field or potentially locally P1 implies ordinary/weak smooth equality; no necessity claim.',
          '15.11 and full proof: smooth means rig-smooth without boundary; decreasing net of weakly smooth psh functions on relatively compact ordinary opens.']},
 'GRc':{'pages':[2,3]+list(range(10,19))+[21,22,23]+list(range(29,36)),
        'version':'arXiv v2, 17 September 2025',
        'applications':[
          '3.4/3.4.1/3.5 and proofs: extended -infinity convention, smooth-curve subharmonicity, scalar stability, curve functoriality and decreasing limits.',
          '3.9 and entire proof: reduced strict curve; perfect field; normalization rig-smooth, quotient topology, non-normal rigid points, boundaries.',
          '4.1/4.2/4.3 and proofs: all analytic extensions and curve tests; semipositive RPL iff classical psh.',
          '6.1 and proof: interior maximum principle, applied on proper connected projective-space fibers.',
          '6.4 and proof: singleton-Shilov maximum principle, used in fresh split-node calculation.']},
 'GRs':{'pages':[4,5,15,16,17],
        'version':'exact supplied arXiv:2503.05513 version',
        'applications':['5.1 and full proof: smooth strict curve RPL subharmonic iff nef residue. Current numbering is 5.1, not the older 3.1 cross-citation.']},
 'Thu':{'pages':[15,16,71,72,73,76,77,82,83,84,103,104,105],
        'version':'HAL tel-00010990v1 thesis',
        'applications':[
          '3.1.8(iii), printed 62/PDF 76: increasing locally bounded family. The new application uses two-sided local bounds from a baseline and usc obstacle.',
          '2.3.21/2.3.22 and proofs: harmonic/log-unit sheaf distinction and residue/genus hypotheses.',
          '3.2.4/3.2.5 and proofs: Thuillier lisse is G-local real PL, not ordinary CLD smooth.',
          '3.4.2 and full proof, printed 89-90/PDF 103-104: decreasing family of subharmonic lisse functions on relatively compact ordinary opens.',
          '3.4.5 and proof: scalar stability of smooth-curve subharmonicity.']},
 'Ber':{'pages':[], 'version':'Publications Mathematiques IHES 78 (1993), 5-161',
        'applications':['3.7.4: smooth morphisms are open; applied to ordinary locally trivial projective-space bundles, not scalar maps. Local structure statements and proof retained.']}
}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    assignment=json.loads((ROOT/'input.json').read_text())['assignment']
    marker='Read-only published source caches:'
    sources,_=json.JSONDecoder().raw_decode(assignment.split(marker,1)[1].lstrip())
    OUT.mkdir(exist_ok=True)
    data={'purpose':'Literal primary-source pages with checked applications; provenance is not a mathematical certificate.',
          'sources':[], 'page_number_convention':'1-based formfeed-separated PDF pages; selected Thu printed pages are PDF minus 14.',
          'pdf_visual_checks':[
            {'id':'Thu','pdf_page':76,'artifact':'source-extracts/Thu-pdf76.png','finding':'3.1.8(iii) actually says famille croissante et localement bornee; proof application is locally bounded on both sides.'},
            {'id':'CD','pdf_page':196,'artifact':'source-extracts/CD-pdf196.png','finding':'Stage 0 is smooth and positive; successors are local decreasing limits; ordinal bounds are preserved by 8.1.5. 8.1.1 explicitly uses sequences.'},
            {'id':'GJR','pdf_page':80,'artifact':'source-extracts/GJR-pdf80.png','finding':'15.11: smooth means rig-smooth without boundary; decreasing net; weakly smooth. 15.10 supplies ordinary smoothness only in its extra geometric/residue cases.'}],
          'dependency_policy':'No earlier generated theorem, unpublished book source or dossier proof verdict imported.',
          'checked_application_proofs':'All new applications are fully written in P03.2-argument.md and embedded in standalone P03.2-paper.tex.'}
    for supplied in sources:
        name=Path(supplied['pdf']).name
        if name.startswith('CD-'): ident='CD'
        elif name.startswith('GJR-'): ident='GJR'
        elif '2506.' in name: ident='GRc'
        elif '2503.' in name: ident='GRs'
        elif name.startswith('Thuillier'): ident='Thu'
        else: ident='Ber'
        pdf=Path(supplied['pdf']); txt=Path(supplied['literal_extract'])
        assert digest(pdf)==supplied['pdf_sha256'], pdf
        assert digest(txt)==supplied['extract_sha256'], txt
        chunks=txt.read_text().split('\f')
        meta=META[ident].copy()
        if ident=='Ber':
            first=next(i+1 for i,p in enumerate(chunks) if '3.7.1. Definitions.' in p)
            meta['pages']=list(range(first,first+5))
        directory=OUT/ident; directory.mkdir(exist_ok=True)
        literals=[]
        for n in sorted(set(meta['pages'])):
            dest=directory/f'pdf-page{n:04d}.txt'
            dest.write_text(chunks[n-1])
            literals.append({'pdf_page':n,'file':str(dest.relative_to(ROOT)),'sha256':digest(dest),'literal':True})
        data['sources'].append(dict(supplied,id=ident,**meta,verified_hashes=True,literal_pages=literals))
    (OUT/'source-provenance.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'sources_verified':len(sources),'literal_pages_retained':sum(len(s['literal_pages']) for s in data['sources'])}))

if __name__=='__main__': main()
