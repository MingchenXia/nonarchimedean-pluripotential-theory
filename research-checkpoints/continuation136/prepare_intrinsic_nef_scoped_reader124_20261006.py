from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, shutil

R=Path('/workspace/research'); K=R/'root-checks'; D=K/'public-P16.5-round124-final-reader'
assert not D.exists(); D.mkdir()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review_path=K/'P16.5-round124-actual-scoped-independent-review-20261006.json'
review=json.loads(review_path.read_text())
assert review['verdict']=='PASS' and review['operationId']=='17bacb62-99e4-4d2d-ae29-f4aaec3874d7'
assert sha(review_path)=='2309386d15eeb384b96bcefe494e45264059f733344e40a6fe6b4862f105b5e3'
bindings=json.loads((R/'campaigns/round-124/P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review/mathematical-data-bindings.json').read_text())
parts=[('I. Bounded genuine metric products and continuous obstacles',bindings['units'][0]),
       ('II. The entire intrinsic floor operator and integrable weights',bindings['units'][1]),
       ('III. Arbitrary mixed weighted nets and both outer signs',bindings['units'][2]),
       ('IV. Weak energy, intrinsic targets and coercivity',bindings['units'][3])]
text=r'''# Intrinsic finite-energy Monge--Ampere products in nef classes

This paper states and proves the exact nef operator and variational-support theorem independently accepted in Xean review124. The field is algebraically closed, trivially valued, of characteristic zero and arbitrary cardinality; the original variety is smooth integral and projective of dimension $n\geq1$. The datum is any actual nef rational line bundle $L$, with no semiampleness or finite-generation assumption. All potentials and measures remain on the entire original $X^{\mathrm{an}}$.

The reference is the canonical zero metric. The raw mass is $V=c_1(L)^n$. On the entire genuine numerical cone define

$$E_\theta(u)=\inf_{k\geq1}E_\theta(\max(u,-k)),\qquad
\mathcal E^1(\theta)=\{u\in\operatorname{PSH}(\theta):E_\theta(u)>-\infty\}.$$

The theorem constructs a target-independent positive Radon top operator and common-class mixed products of mass $V$ on this whole intrinsic domain, including endpoints outside the auxiliary ample finite-energy vector space. It proves reference-floor total-variation convergence, integrability of every intrinsic test, weighted arbitrary decreasing-net convergence against all original continuous tests, both signs of the original continuous-direction outer derivative, weak upper semicontinuity and compact energy-cost sublevels. At $V>0$, the intrinsic finite-dual condition is equivalent to integration of every genuine finite-energy test, every constructed output satisfies it, and its variational objective is coercive.

At $V=0$, the positive top and common-class mixed operators, energies and weighted products vanish. No probability normalization, inverse equation or uniqueness is claimed in this range. This paper proves no all-target attainment or uniqueness theorem at positive volume either. Thus its reviewed scope is a supporting theorem for original P16.5; it does not close that original problem, and supplies no general nonnef big-class extension.

The only supplied equation input is the exact actual-ample G0 theorem, used solely at positive actual ample perturbations. The published model-pairing, envelope and numerical inputs are named in each proof part and remain in their stated domains. They are imported mathematical foundations, not claims of recursively proving every cited theorem. The four proof parts below preserve the frozen mathematical bodies independently reconstructed in review124. Their earlier draft-status sentences and chronological remaining-obligation paragraphs are retained as provenance; the present theorem and Part V specify the accepted final scope.

## 0. The ample input and the finite-continuous closure replacement

The supplied ample theorem concerns an actual ample rational bundle on the retained original characteristic-zero projective variety. It constructs its genuine finite-energy metric operator, raw energy and continuous-obstacle envelopes, supplies compactness and all-point divisorial determination, and proves both continuous-direction outer energy derivatives. It gives no assertion for a nonample class. Its exact full mathematical source is the previously accepted P16.1 paper; the independently frozen review packet includes that entire body. Within the present proof every invocation has an actual ample class, such as $\theta+\epsilon h$ with $\epsilon>0$.

For clarity, the closure step avoids an arbitrary extended-valued flattening lemma. Genuine nef membership equals the intersection of the genuine cones for $\theta+\epsilon h$. The forward section embeddings preserve the scalar, since generating canonical section norms have maximum zero. For the reverse direction choose finite continuous ample FS majorants of a potential in every positive perturbed cone, allowing positive constant shifts. They form a single directed decreasing family: for any finite collection of old continuous majorants, their finite continuous minimum is an upper bound; with a positive strict tolerance, eventual approximation below that minimum holds on an open cover, and compactness provides one common later approximant. Refine the positive perturbation at the same step. Infimizing tolerances and majorants gives the desired original genuine all-point limit, including its poles. This uses finite continuous old minima, never a general varying-class flattening principle for arbitrary discontinuous functions. Closed intersections in one normalized ample compact cone provide the genuine normalized nef compactness and the envelope passage used below.

'''
outbindings=[]
for title,unit in parts:
    p=Path(unit['path']);assert sha(p)==unit['sha256']
    s=p.read_text();lines=s.split('\n');assert lines[0].startswith('# ')
    body='\n'.join(lines[1:]);body=re.sub(r'^(#{2,6}) ',lambda m:'#'+m.group(1)+' ',body,flags=re.M)
    text+='\n## '+title+'\n'+body+'\n'
    outbindings.append({'part':title,'path':str(p),'sha256':sha(p),'whole_constituent_proof_root_read':True,
                        'transformation':'Remove only repeated top title and shift headings; frozen mathematical body retained verbatim.'})
text+='\n## V. Complete independent reconstruction and final scope\n\n'+review['report']+'\n'
(D/'P16.5-argument.md').write_text(text)
command=['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']
result=subprocess.run(command,cwd=D,capture_output=True,text=True)
(D/'source-build.stdout').write_text(result.stdout);(D/'source-build.stderr').write_text(result.stderr)
assert result.returncode==0,result.stderr
shutil.copyfile(review_path,D/'canonical-independent-review.json')
ledger={'recorded_utc':datetime.now(timezone.utc).isoformat(),'scope':'Entire intrinsic nef operator, common-class mixed weighted decreasing nets, outer derivatives, energy usc and intrinsic dual/coercivity support; no inverse or original closure.',
        'canonical_result':str(review_path),'canonical_result_sha256':sha(review_path),'whole_canonical_report_premises_and_passages_root_read':True,
        'premises':review['premises'],'passages':review['passages'],'parts':outbindings,
        'sole_actual_ample_G0_sha256':'6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9',
        'extended_primary_transcripts_uploaded':False,'all_recursive_foundations_reproved':False}
(D/'source-application-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
meta={'recorded_utc':datetime.now(timezone.utc).isoformat(),'scoped_independent_verdict':'PASS','original_closed':False,
      'canonical_result_sha256':sha(review_path),'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),
      'all_constituent_math_root_read':True,'whole_assembled_argument_separately_root_read':False,'whole_generated_tex_separately_root_read':False,
      'native_compiler_success_asserted':False,'PDF_layout_checked':False,'existing_P16_4_editor_modified_or_new_tab_opened':False}
(D/'publication-preparation.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'reader':str(D),'argument_bytes':(D/'P16.5-argument.md').stat().st_size,'source_bytes':(D/'P16.5-paper.tex').stat().st_size,
                  'argument_sha256':meta['argument_sha256'],'source_sha256':meta['source_sha256'],'scoped_verdict':'PASS','original_closed':False},indent=2))
