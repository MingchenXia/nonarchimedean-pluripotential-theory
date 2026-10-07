from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
S=K/'public-P14.4-round172-partial-reader'
D=K/'public-P14.4-continuation215-corrected-polar-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists();D.mkdir()
assert sha(S/'P14.4-paper.tex')=='a6f7734f6ed598c6e89d6a689226f744a28fb7c4cef23494cb45500bbd12cc29'
assert json.loads((K/'P14.4-round175-whole-partial-review-binding-20261007.json').read_text())['verdict']=='FAIL'
old=(S/'P14.4-paper.tex').read_text()
original_statement=r'''These are actual admissible states in the same class,
$\Phi_{D_j}\downarrow\Phi_D$ everywhere, and their raw products
and masses converge to (5.3). More generally, on states with
support in a common compact affine set, total variation convergence
of measures implies local $L^1$ convergence of their reconstructed
primitives on $X$ and every fixed smooth modification.
This is a topology on the admissible sector, not a formal completion.'''
corrected_statement=r'''These are actual admissible states in the same class,
$\Phi_{D_j}\downarrow\Phi_D$ everywhere, and their raw products
and masses converge to (5.3). More generally, let
$D_j=(a_j,b_j,c_j,\nu_j,\kappa_j)$ and
$D=(a,b,c,\nu,\kappa)$ be admissible states whose measures have
support in a common compact affine set. If
\[
 (a_j,b_j,c_j,\kappa_j)\longrightarrow(a,b,c,\kappa),
 \qquad \|\nu_j-\nu\|_{\TV}\longrightarrow0,
\]
then their reconstructed primitives converge locally in $L^1$
on $X$ and every fixed smooth modification. This gives a product
topology on each fixed compact-support admissible sector;
no formal completion is used. The hypothesis on $a_j,\kappa_j$
is essential for a statement about actual primitives.'''
original_proof=r'''Uniform local $L^1$ kernel bounds give
$\|U_\nu-U_{\nu'}\|_{L^1(K)}\leq C_K\|\nu-\nu'\|_{\TV}$
on the curve. On a fixed modification the uniform logarithmic
bounds from the proof of Lemma~\ref{pulllemma}, and a finite chart
cover, give the same estimate for the composed kernels.
Constants and the smooth parameters can be transported separately.
No density of finite ideals or ordinary PL models is asserted.
Admissibility is not asserted to be closed in arbitrary weak
measure limits.'''
corrected_proof=r'''Uniform local $L^1$ kernel bounds give
$\|U_\nu-U_{\nu'}\|_{L^1(K)}\leq C_K\|\nu-\nu'\|_{\TV}$
on the curve. On a fixed modification $p:W\to X$, the uniform
logarithmic bounds from Lemma~\ref{pulllemma} and a finite chart
cover give the corresponding estimate for the composed kernels.
Fix a compact coordinate region $K_0\Subset W$ and a smooth
volume form there. The divisor logarithm $e\circ p$ is locally
integrable: locally it is the logarithm of the squared norm of a
nonzero holomorphic defining function, plus a smooth function.
The exact primitive formula (3.2) therefore yields
\[
\begin{split}
 \|\Phi_{D_j}\circ p-\Phi_D\circ p\|_{L^1(K_0)}
 &\leq |a_j-a|\,\|e\circ p\|_{L^1(K_0)}\\
 &\quad+C_{K_0}\|\nu_j-\nu\|_{\TV}
       +|\kappa_j-\kappa|\,\operatorname{Vol}(K_0).
\end{split}
\]
Differences are taken almost everywhere; common pole sets have
volume zero. The three terms tend to zero under the stated
hypotheses. The identity modification proves the assertion on $X$.
The parameters $b,c$ determine the smooth background form and
do not occur in this primitive formula; their stated convergence
also transports that form continuously. No density of finite
ideals or ordinary PL models is asserted. Admissibility is not
asserted to be closed in arbitrary weak measure limits.

For clarity, convergence of $\nu_j$ alone is insufficient.
The admissible states $(1,1,1,0,\kappa_j)$, with $\kappa_j=0$
for even $j$ and $-1$ for odd $j$, have identical zero measures
in one big non-nef class. On a positive-volume compact region
outside $E$ their primitives alternate between $e$ and $e-1$,
so no $L^1$ limit exists. Actual primitives are not being
identified modulo constants.'''
for fragment in (original_statement,original_proof):assert old.count(fragment)==1
new=old.replace(original_statement,corrected_statement).replace(original_proof,corrected_proof)
new=new.replace(r'\author{Unverified research draft}',r'\author{Corrected research draft; independent verification pending}')
new=new.replace(r'\date{6 October 2026}',r'\date{7 October 2026; continuation 215}')
new=new.replace(r'\section{Scope, conventions, and external inputs}',r'''\section{Scope, conventions, and external inputs}
This edition corrects the primitive-continuity scope in
Proposition~\ref{approx}: convergence is imposed on the actual
primitive coordinates as well as the diffuse measure, with the
full local estimate given in its proof. The earlier edition remains
preserved. This amended paper is still an unverified partial result;
it does not solve the unchanged original P14.4.
''',1)
(D/'P14.4-paper.tex').write_text(new)
shutil.copyfile(S/'source-application-ledger.json',D/'unchanged-author172-source-application-ledger.json')
note={'id':'ROOT215','recorded_utc':datetime.now(timezone.utc).isoformat(),'type':'New unreviewed mathematical amendment; not a native author result or caller grant',
 'atom':'P14.4','baseline_source':str(S/'P14.4-paper.tex'),'baseline_sha256':sha(S/'P14.4-paper.tex'),
 'corrected_source':str(D/'P14.4-paper.tex'),'corrected_source_sha256':sha(D/'P14.4-paper.tex'),
 'replaces':'The generalized continuity statement and its proof in Proposition5.4. All other mathematical bodies copied exactly from immutable172 source; author/date and explicit amendment notice updated.',
 'old_statement':original_statement,'new_statement':corrected_statement,'new_proof':corrected_proof,
 'supports':[],'historical_baseline_is_not_a_mathematical_grant':True,
 'old_native172_notes_and_failed175_review_preserved':True,'independent_acceptance':False,'original_closed':False,'new_accepted_paper':False}
(D/'ROOT215-new-mathematical-amendment.json').write_text(json.dumps(note,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'directory':str(D),'new_source_sha256':sha(D/'P14.4-paper.tex'),'new_source_lf_lines':len(new.splitlines()),'original_closed':False,'independent_acceptance':False},indent=2))
