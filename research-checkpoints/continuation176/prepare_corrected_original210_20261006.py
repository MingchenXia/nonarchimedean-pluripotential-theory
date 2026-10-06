from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks'
S=K/'public-P16.5-round163-full-original-candidate-reader/paper.tex'
F=K/'P16.5-horizontal-fixed-factor-and-retained-vertical-correction-candidate-20261006-continuation209.tex'
T=K/'P16.5-original-big-equation-with-retained-vertical-moving-factors-candidate-20261006-continuation210.tex'
D=K/'public-P16.5-continuation210-corrected-original-reader'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(S)=='53428fabcc63e9c04ef5f6f05c79dde4b415d833c3b78c27c95224794c58da61'
assert sha(F)=='4e727fcbc6b19c9a5b424ab9a8d8ddc53d0da01c72d6dd0a91933756f6f932da'
assert not T.exists() and not D.exists()
s=S.read_text()
s=s.replace('\\title{Original-carrier finite-energy equations in big rational classes\\\\\n\\large A reconstruction and audit of the supplied moving-system programme}', '\\title{Original-carrier finite-energy equations in big rational classes\\\\\n\\large A proposed proof with retained vertical moving factors}')
s=s.replace('\\author{Unverified research draft}', '\\author{Unreviewed corrected reconstruction, continuation 210}')
s=s.replace('This is an unverified proof draft, not a correctness certification.', 'The full-system model retains the vertical part of its generic fixed divisor.\nAn explicit surface example and the exact horizontal-division proof are\nincluded. This is an unverified corrected draft, not a correctness certification.')
anchor='The exact original task and full\nfamily remain in the frozen input.'
assert s.count(anchor)==1
s=s.replace(anchor, anchor+'\nThis manuscript preserves the whole round-163 proposed proof but corrects\nits complete moving formula (5.2). The exact full-system proof and explicit\nfinite obstruction are included in the appendix. The original candidate\nand separate correction209 remain immutable proof data; neither supplies\nan accepted nonample foundation or an independent verdict for this revision.')
old='''Its infinity endpoints recover every original $s_{mj}$; all nonzero
finite fibers also recover the full generic system. Remove the horizontal
factor $s_{mT_m}$ before resolving the residual ideal. Its residual base
divisor is vertical, and its moving bundle is
\\[
 C_{m,D}=\\rho_X^*A_m+D+cF-G_{m,D}^{\\rm vert}/m.
 \\tag{5.2}
\\]
It is globally generated and nef.'''
new='''Its infinity endpoints recover every original $s_{mj}$; all nonzero
finite fibers also recover the full generic system. On a common smooth
determination mapping to the actual generic product, write the total
pulled fixed divisor as $T_m^{\\rm hor}+T_m^{\\rm ver}$.
Every complete absolute section vanishes along the horizontal part.
Divide only by $s_{mT_m^{\\rm hor}}$. The residual sections belong to
$\\rho_X^*A_m+D+T_m^{\\rm ver}+cF$, and their residual base ideal
is supported at zero. Principalize it to the effective
$G_{m,D}^{\\rm vert}$. The actual complete moving bundle is
\\[
 C_{m,D}=\\rho_X^*A_m+D+T_m^{\\rm ver}+cF
                         -G_{m,D}^{\\rm vert}/m.
 \\tag{5.2}
\\]
It is globally generated and nef, and is exactly the moving part of the
WHOLE absolute system above. Its bounded quotient scalar on $A_m$
has vertical divisor $D+T_m^{\\rm ver}-G_{m,D}^{\\rm vert}/m$.
The appendix proves this full section-space identification and gives
an explicit example where deleting $T_m^{\\rm ver}$ changes the
auxiliary energy from zero to $-1/3$ and changes its unit atom.
In particular the generic factor cannot be removed with all its vertical
components: the original obstacle may already consume that vanishing.'''
assert s.count(old)==1
s=s.replace(old,new)
s=s.replace('Consequently this is\nthe full relative lattice of (9.2), not a selected series.', 'Consequently this is\nthe full relative lattice of (9.2), not a selected series. Its retained\nvertical term is exactly the one used in the corrected complete moving\nformula (5.2), before its effective residual base divisor is removed.')
s=s.replace('its canonical result is\n\\texttt{candidate=true} in that exact assignment scope.', 'this revision proposes\nthe same full-original theorem in that exact scope, but has no native\ncanonical result or independent acceptance of its own.')
appendix_start=s.index('\\appendix\n\\section{Evidence and reproducibility}')
bib_start=s.index('\\begin{thebibliography}',appendix_start)
correction=F.read_text();body=correction[correction.index('\\section*{The actual full-system formula}'):correction.index('\\section*{Application and limits of this correction}')]
body=body.replace('\\section*{The actual full-system formula}', '\\section{Actual horizontal division and an explicit obstruction}')
body=body.replace('\\section*{A complete big nonnef surface computation}', '\\subsection{A complete big nonnef surface computation}')
body=body.replace('\\label{formula}','\\label{verticalformula}')
evidence=r'''\section{Evidence and scope of this revision}
The complete original round-163 TeX body has SHA-256
\texttt{53428fabcc63e9c04ef5f6f05c79dde4b415d833c3b78c27c95224794c58da61}.
The separate whole correction209 has SHA-256
\texttt{4e727fcbc6b19c9a5b424ab9a8d8ddc53d0da01c72d6dd0a91933756f6f932da}.
Their exact bytes and this deterministic revision operation are preserved.
The unchanged entire original task and the only mathematical grants G0/G1
remain the same. Historical other papers, reports, hashes and the author
candidate label are not mathematical grants.

Complete primary proof units retrieved by the original author and reread
in their entirety for the root application are BFJ math/0608260v2
renderer310--441 and445--545; BJ1801.08229v4 renderer2705--3107,
3996--4022 and10614--10647; Addendum2206.07183v2 renderer128--257.
Versions and literal line maps are retained in the source register.
No new primary retrieval, whole-primary reading or recursively complete
background reconstruction is claimed by this revision. A fresh reviewer
must obtain independent primary evidence and audit each new application.

The appendix is an actual full section-space proof, not an additional
assumed foundation. It repairs the complete moving bundle used in the
finite-list energy/measure signature and subsequent common-system arguments.
Every later use of finite top/lower moving convergence refers to this
correct complete moving bundle. The original absolute class and its whole
section spaces remain the ones in (4.1)--(4.3); their positive products,
raw central multiplicities and intercepts therefore still provide the
objects in (5.4), subject to whole mathematical verification.

The stronger fixed-original-unbounded-test assertion at every physical
auxiliary output remains unproved with defect (11.4). It has not been
added as an assumption or silently declared proved. All genuine operator,
canonical weighted, comparison and attainment claims still require a
fresh full-original independent audit. No original problem is closed by
this revision, its compilation or its finite explicit calculation.
'''
s=s[:appendix_start]+'\\appendix\n'+body+'\n'+evidence+'\n'+s[bib_start:]
T.write_text(s)
D.mkdir()
(D/'revision-binding.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'classification':'Unreviewed full-original corrected proof210, not native author result or independent verdict','base_paper':str(S),'base_sha256':sha(S),'whole_correction':str(F),'correction_sha256':sha(F),'corrected_tex':str(T),'corrected_tex_sha256':sha(T),'mathematical_change':'Complete moving bundle retains Tver after horizontal-only fixed divisor division; whole actual section proof and finite blowup obstruction included. No new S-M or equation grants.','original_task_unchanged':True,'g0_g1_only_grants':True,'native_independent_verdict':None,'original_closed':False,'frozen163208_preserved':True,'active158166_feedback_sent':False,'existing_editor_unchanged':True},indent=2)+'\n')
print(json.dumps({'tex':str(T),'sha256':sha(T),'lines':len(s.splitlines()),'original_closed':False},indent=2))
