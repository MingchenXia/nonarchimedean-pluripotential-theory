#!/usr/bin/env python3
"""Make the canonical local notes from the complete authored proof sections."""
import json
from pathlib import Path
import fitz

argument=Path('P03.1-argument.md').read_text()
def before(header):return argument.split(header,1)[0]
def section(start,end=None):
    s=argument.split(start,1)[1]
    if end:s=s.split(end,1)[0]
    return start+s

execution=json.loads(Path('execution.json').read_text())
passes=[x['exit_code'] for x in execution['commands']]
pages=len(fitz.open('P03.1-paper.pdf')) if Path('P03.1-paper.pdf').exists() else None
evidence=("\n\nExecution evidence and artifacts: The complete new argument is in P03.1-argument.md and the standalone P03.1-paper.tex. "
          f"The local command pdflatex -interaction=nonstopmode -halt-on-error P03.1-paper.tex ran twice, with exit codes {passes}; "
          f"P03.1-paper.pdf has {pages} pages. Exact source bodies and PDF checks are in source-extracts and source-provenance.json. "
          "Programs and rerun commands, from this directory: python prepare_sources.py; python build_artifacts.py; "
          "python make_notes.py; python check_artifacts.py. Diagnostics are in execution.json, build-pass-1.txt and build-pass-2.txt; "
          "environment details are in environment.json. status.json has exactly the required five keys. Input bytes are retained in "
          "input.json and input-original.json, with task-original.json and assignment-original.txt. "
          "No heavy compute, installation, network call or additional model invocation was used. "
          "This is a mathematical proof draft; compilation, hashes and administrative checks do not certify mathematical correctness.")

notes=[
 {'id':'n1',
  'summary':'Proved full-family classical positivity for every usc obstacle on perfected-bijective-normalization curve bases times smooth geometrically connected projective factors, and on analytic projective bundles. Exact global real-PL descent includes factors without K-points; boundary and every analytic scalar curve test are covered. Concrete normal and unibranch cusp products are proved. This is a sufficient sector, not a sharp higher-dimensional classification.',
  'detailedSummary':'The exact LFS/semipositive-real-PL union equals the whole semipositive real-PL class under the checked GJR definitions. Continuous competitors are constant on compact connected projective fibers by the classical maximum principle. A finite scalar extension constructed from a closed algebraic point supplies an actual section; finite real-PL and semipositivity descent recovers a global base competitor even without a K-point. Projective bundles use local analytic sections and ordinary sheaf gluing. Smoothness proves ordinary openness, hence the fiber infimum of any usc obstacle is usc, the full raw envelope is the base envelope pulled back, and regularization commutes with this geometric projection. A fresh proof of the required curve-family lemma uses anchored finite maxima on the interior of the perfected normalization, boundary extension, and finite/scalar subharmonic descent. The final pullback is tested along every curve over every analytic field extension without assuming scalar regularization compatibility. The sector includes normal analytic curve domains times smooth projective factors and explicitly normalized geometrically unibranch cusp products; no theorem for arbitrary normal higher-dimensional affinoids, sharp necessity, continuity, or CLD stages follows.',
  'text':before('## 5. Split branches')+evidence,
  'support':[]},
 {'id':'n2',
  'summary':'Explicit continuous-obstacle failures for the full family on split branches and codimension-two point pinchings. This includes a single irreducible bidisc with two rational points identified: its strict affinoid algebra, seminormality, and normality off one codimension-two point are proved, and global rational LFS minorants force a closed-disc failure. Proper projective factors preserve the split obstruction.',
  'detailedSummary':'For A_d=K<X_1,...,X_d,Y_1,...,Y_d>/(X_iY_j), the fiber-product algebra proves reducedness, purity, finite normalization, normality off the origin, and seminormality, including analytic germs. With a=-log|varpi|, f=-a max_j|Y_j| and h_n=(1/n)log max(|varpi|^n,|X_1|,...,|X_d|), every full-family competitor is bounded by -a on the Y-component by its singleton-Gauss maximum principle. The exact raw envelope is 0 on the punctured X-component and -a on the Y-component including the node; regularization raises only the node, and a closed-disc axis fails. An additional irreducible codimension-two example starts from B=K<T,Z> and A={g:g(0,0)=g(1,0)}. Writing U=T(T-1) proves directly the bounded decomposition B=R_0+TR_0 and A=R_0+T(U,Z)R_0, so A is an actual strict affinoid domain algebra with finite normalization B. Its conductor identifies just the two rational points. Equal residue evaluations and the finite coherent-module kernel prove seminormal analytic germs; all other points are normal. A continuous normalization obstacle phi(|T-1|), with phi(r)=-a r/rho for r<=rho and log r for r>=rho, descends since both identified values are 0. The global polynomials T(T-1)^n belong to A and yield rational LFS minorants. The disc at T=1+varpi S forces raw nodal value -a, while T=varpi S gives raw value 0 at nonzero radii approaching that point; the regularization fails the bad disc Gauss principle. The examples are independently proved and not asserted identical to the supplied book construction. They do not classify geometrically unibranch higher-dimensional domains.',
  'text':section('## 5. Split branches','## 6. An irreducible')+evidence,
  'support':['n1']},
 {'id':'n3',
  'summary':'Explicit irreducible nonsplit-node surface over Q_3 with a finite continuous obstacle whose full LFS/semipositive-real-PL regularization fails an actual L=Q_3(sqrt 2) closed-disc test. Global rational LFS minorants are constructed by truncated binomial polynomials. The ground-field curve normalization is pointwise bijective, but its product fiber splits. The sharp original normal/geometrically-unibranch classification remains open.',
  'detailedSummary':'Let C=M(Q_3<X,Y>/(X^2-2Y^2)), D={|Z|<1}, rho=1/3 and b=-log rho. C is an integral curve with normalization L<T>, X=sqrt(2)T, Y=T; away from Y=0 it is an isomorphism and over the origin M(L) is a single point. The product X_0=C x D is an actual reduced irreducible strict surface. At the nodal point with Z^2=18 its normalization fiber is M(L tensor_K L), two points. A continuous cutoff obstacle f in [-3b,0] is built from |Y| and |3X-ZY|/(rho|Y|). For c_j=binom(-1/2,j), A_n=(Z/3)sum_{j<n}c_j(Z^2/18-1)^j, the functions h_n=(1/n)log max(|3|^{3n},|3^{2n}(X-A_nY)|) are global rational LFS. The coefficient identity c_j=(-1)^j binom(2j,j)/4^j bounds them globally by 0, while binomial convergence in every point residue field makes them exactly -3b wherever f<0. Thus all are actual minorants. The plus-branch disc at Z=3sqrt(2) gives the full-family raw nodal value -3b by its Gauss boundary bound; the minus branch gives raw lower bound -2b at every positive radius, hence regularized nodal value at least -2b. The regularized plus-disc Gauss value remains at most -3b because it is bounded by the continuous obstacle. This violates the singleton-Shilov maximum principle after the genuine finite scalar extension. The construction proves the nonsplit necessity obstruction, not a failure on a normal or geometrically unibranch higher-dimensional domain, and does not complete P03.1.',
  'text':section('## 6. An irreducible')+evidence,
  'support':['n1','n2']},
]
packet={'notes':notes,'candidate':False}
Path('canonical-notes.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(notes),'canonical notes; candidate=false.')
