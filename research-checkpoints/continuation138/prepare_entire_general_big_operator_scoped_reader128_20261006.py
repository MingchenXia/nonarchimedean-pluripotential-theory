from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.5-round128-final-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical=K/'P16.5-round128-actual-scoped-independent-review-20261006.json'
review=json.loads(canonical.read_text())
assert review['verdict']=='PASS' and review['operationId']=='5b9f3e61-d5c0-4963-8ca5-dbc93261bae9'
assert sha(canonical)=='7481cbf7e4b2d75614218b7456a72ce8e6e90cf49d1f6312624fac78c8676932'
freeze=json.loads((R/'campaigns/round-128/P16.5-general-big-entire-genuine-E1-operator-independent-review/freeze.json').read_text())
assert len(freeze['inputs'])==6
units=freeze['inputs'][:5]
assert freeze['inputs'][5]['sha256']=='6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9'
D.mkdir(exist_ok=False)
text=r'''---
title: 'Relative energy and the entire Monge--Ampere operator for big rational classes'
author: 'Reconstructed proof and independent scope review'
date: '6 October 2026'
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - '\usepackage{amsmath,amssymb,amsthm}'
  - '\usepackage{fvextra}'
  - '\DefineVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,breakanywhere=true,fontsize=\small}'
---

# Abstract and exact theorem

Let $X$ be a smooth integral projective variety of dimension $n\ge1$ over an algebraically closed trivially valued field of characteristic zero and arbitrary cardinality. Let $L$ be any actual big rational line bundle. No nefness, finite generation or finite Zariski decomposition is assumed. The potentials are the literal genuine numerical psh functions on the whole original $X^{\mathrm{an}}$, defined by single decreasing nets of actual section metrics with numerical class tending to $c_1(L)$.

Put $V_L=P_L(0)$ and $v=\operatorname{vol}_X(L)>0$. This paper constructs a target-independent section/volume energy on the entire genuine cone, normalized by $E_L(V_L)=0$, with $E_L(u+c)=E_L(u)+cv$. The intrinsic relative domain is

$$\mathcal E^1(L,V_L)=\{u\in\operatorname{PSH}(L):E_L(u)>-\infty\}.$$

Its energy is characterized by the genuine reference floors $\max(u,V_L-k)$, is concave and upper semicontinuous in the original divisorial topology, and has compact normalized energy-cost sublevels. On that entire domain the construction gives a positive Radon metric operator $M_L(u)$ of raw mass $v$, agreeing with the actual continuous-obstacle section/volume operator. It is independent of decreasing model-majorant nets, including noncofinal nets with the same all-point endpoint. It satisfies both continuous-direction outer derivative signs:

$$\left.\frac{d}{dt}\right|_{t=0}E_L(P_L(u+th))
   =\int h\,dM_L(u),\qquad h\in C(X^{\mathrm{an}}).$$

Every envelope here is an actual original genuine function. The operator is weakly continuous along arbitrary decreasing genuine nets with finite-energy endpoint, and under original divisorial convergence plus energy convergence. All measures and continuous observables remain on the original analytic carrier.

Xean independent review128, using native Codex gpt-6.1-sol with xhigh reasoning, accepted precisely this theorem. It did not review mixed products, integrable weighted limits, pole-nullness, comparison, domination or an all-target inverse equation. Consequently original P16.5 remains open. The reviewed theorem is a supporting result for its full equation. The five complete proof units below retain their frozen mathematical bodies; earlier draft labels and historical gap sentences indicate when those units were written. This abstract and the complete independent report at the end specify the accepted scope.

# 0. Inputs, complete section limits and the sole ample grant

The exact actual-ample G0 theorem is the supplied equation premise. It is invoked only inside an actual ample class for genuine closure, divisorial compactness and all-point determination. Its ample intersection mass, energy, mixed products and inverse equation are never relabeled as nonample statements. The exact full source is the accepted P16.1 round-92 mathematical argument, bound in the source ledger. None of its ample finite-energy memberships is assumed for an unbounded nonnef potential.

The general envelope/reference premise is Boucksom--Jonsson's addendum, arXiv:2206.07183v2, Theorem A and Corollaries 2.1--2.2. Ordinary projective positive products and the volume differential are used in the smooth characteristic-zero domain of Boucksom--Favre--Jonsson, arXiv:math/0608260v2. These are published mathematical inputs; their precise uses occur in the proof units and review report.

In the lattice formulas one needs a complete section limit, rather than just the limsup definition of volume. For a big Cartier divisor on a projective variety the required statement is

$$\lim_{m\to\infty}\frac{d!\,h^0(Y,mA)}{m^d}=\operatorname{vol}_Y(A).$$

The complete-series argument in Lazarsfeld--Mustata, *Convex bodies associated to linear series*, Sections 2.1--2.2, Proposition 2.1, Lemma 2.2 and Theorem 2.3, is the published input for this limit. Its original uncountable-field convention is removed at this particular application by choosing an uncountable algebraically closed extension $K/k$. Flat cohomology base change preserves each actual section dimension $h^0(Y,mA)$ exactly. Thus it preserves the complete numerical sequence, its limsup and the obtained limit. No countability restriction is added to the original field. Clearing denominators gives the corresponding limit through divisible degrees for actual rational bundles. This supplementary application supplies the full section-limit input used throughout the frozen units, without pretending that BFJ's limsup definition alone proves convergence.

Smooth equivariant common refinements are obtained by resolving the closure of the generic graph and its central boundary, using functorial characteristic-zero resolution. Normality and the height-one characterization of regularity justify the section identities and exceptional coefficient vanishing. The precise imported propositions, original domains and source links are recorded in the independent report and source ledger. The proof is relative to these foundations and the exact ample grant; it does not claim a recursive reconstruction of every external foundation.

'''
titles=['I. Genuine minimal reference and the volume obstruction','II. Actual lattices, volume energy and atomic mass',
        'III. Envelope descent and continuous-obstacle derivatives','IV. Entire genuine relative energy and weak compactness',
        'V. Truncated volume, the entire operator and outer derivatives']
parts=[]
for title,unit in zip(titles,units):
    p=Path(unit['path']);assert sha(p)==unit['sha256']
    body=p.read_text().split('\n',1)[1]
    body=re.sub(r'^(#{2,6}) ',lambda m:'#'+m.group(1)+' ',body,flags=re.M)
    text+='\n# '+title+'\n'+body+'\n'
    parts.append({'part':title,**unit,'whole_constituent_math_root_read':True,
                  'transformation':'Remove repeated top title and shift headings only; mathematical body preserved.'})
text+='\n# VI. Complete independent reconstruction and final scope\n\n'+review['report']+'\n'
text+='\n# VII. Documentary corrections and public evidence\n\n'
text+='The references in own144 to section poles mean section zeros, where the scalar is minus infinity. The unavailable own148 path mentioned in own150 is not a premise: its needed ample statements are in the exact G0 body. The independent report supplies the complete-series section-limit premise as explained in Section0. These documentary clarifications change neither the frozen proof nor the accepted theorem.\n\n'
text+='The canonical native report has 11 external premises and 248 passage records, many repeating the same indexed statement with a short quote. Its task-grant passage is the final record at urn:xean:task; its numerical premise index0 is a serialization association and does not turn the ample grant into the addendum theorem. The public projection preserves the report, statements, links, ids and indices, while omitting all verbatim source quotes. The local raw canonical result is bound by its exact hash in the ledger. No private transcripts, logs, inputs or databases accompany this reader.\n'
(D/'P16.5-argument.md').write_text(text)
public={k:v for k,v in review.items() if k!='passages'}
public['passages']=[{**{k:v for k,v in p.items() if k!='quote'},'verbatim_source_quote_omitted':True} for p in review['passages']]
public['projection']={'raw_canonical_sha256':sha(canonical),'raw_canonical_bytes':canonical.stat().st_size,
                      'sole_change':'All passage quote fields omitted for public distribution; report, premises and remaining passage fields preserved.'}
(D/'independent-review-public-projection.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
cmd=['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']
r=subprocess.run(cmd,cwd=D,capture_output=True,text=True);assert r.returncode==0,r.stderr
p=D/'P16.5-paper.tex';source=p.read_text()
unicode_math={'−':r'-','⊕':r'\oplus','≤':r'\le','α':r'\alpha','∑':r'\sum','⟨':r'\langle','⟩':r'\rangle','·':r'\cdot',
              '≥':r'\ge','μ':r'\mu','δ':r'\delta','∫':r'\int','′':r'\prime','→':r'\to','λ':r'\lambda','Ω':r'\Omega',
              'φ':r'\varphi','↓':r'\downarrow','ε':r'\epsilon','∞':r'\infty','γ':r'\gamma','κ':r'\kappa','±':r'\pm',
              'θ':r'\theta','Δ':r'\Delta','∈':r'\in','↑':r'\uparrow','∉':r'\notin','ℓ':r'\ell','σ':r'\sigma'}
declarations='\n'.join(r'\DeclareUnicodeCharacter{'+format(ord(c),'04X')+r'}{\ensuremath{'+v+'}}' for c,v in unicode_math.items())
source=source.replace(r'\begin{document}',declarations+'\n'+r'\begin{document}',1)
source=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',source)
p.write_text(source)
builds=[]
for i in range(2):
    command=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']
    r=subprocess.run(command,cwd=D,capture_output=True,text=True)
    (D/f'build-{i}.stdout').write_text(r.stdout);(D/f'build-{i}.stderr').write_text(r.stderr)
    builds.append({'argv':command,'returncode':r.returncode});assert r.returncode==0,r.stdout[-2500:]
pdf=fitz.open(D/'P16.5-paper.pdf');pages=len(pdf)
for i in sorted(set([0,pages//2,pages-1])):pdf[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(D/f'layout-page-{i+1}.png')
log=(D/'P16.5-paper.log').read_text()
ledger={'recorded_utc':datetime.now(timezone.utc).isoformat(),'scoped_verdict':'PASS','original_closed':False,
        'canonical_local_path':str(canonical),'canonical_raw_sha256':sha(canonical),
        'public_projection_sha256':sha(D/'independent-review-public-projection.json'),
        'whole_actual_report_premises_and_all_passages_root_read':True,'passages_read_representation':'Report and all11 premises read in full; byte-identical repeated passage statements indexed; all248 passage ids, URLs, indices and quotes read in two complete tuple batches.',
        'premises':review['premises'],'parts':parts,'sole_actual_ample_G0':freeze['inputs'][5],
        'extended_primary_transcripts_or_source_quotes_uploaded':False,'all_recursive_foundations_reproved':False}
(D/'source-application-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
meta={'recorded_utc':datetime.now(timezone.utc).isoformat(),'scoped_independent_verdict':'PASS','operation_id':review['operationId'],
      'original_closed':False,'canonical_raw_sha256':sha(canonical),'argument_sha256':sha(D/'P16.5-argument.md'),
      'source_sha256':sha(p),'pdf_sha256':sha(D/'P16.5-paper.pdf'),'PDF_pages':pages,'local_builds':builds,
      'overfull_diagnostics':log.count('Overfull'),'undefined_diagnostics':log.count('Undefined'),
      'all_whole_constituent_math_root_read':True,'whole_assembled_argument_separately_root_read':False,
      'whole_generated_tex_separately_root_read':False,'native_compiler_success_asserted':False,
      'actual_visual_pages':[],'existing_P16_4_editor_modified_or_new_tab_opened':False}
(D/'publication-preparation.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'reader':str(D),'pages':pages,'source_sha256':meta['source_sha256'],'pdf_sha256':meta['pdf_sha256'],
                  'overfull':meta['overfull_diagnostics'],'undefined':meta['undefined_diagnostics'],'original_closed':False},indent=2))
