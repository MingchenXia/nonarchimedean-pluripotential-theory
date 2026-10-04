"""Reproduce the full independently reconstructed argument and source bodies."""
from pathlib import Path
import json

p=Path(__file__).resolve().parent
old=(p/'sources/rank-one-argument.md').read_text()
support=old[old.index('## Definitions, source checks'):old.index('## Full strictly negative contact and the fixed-real-pair conclusion')]
support=support.replace('snapshots are in `sources/` and `source-hashes.json`', 'snapshots of the current read-only origins are in `sources/` and `source-hashes.json`')
# Insert the new all-rank lemmas after exact reference decomposition.
marker='## Graph geometry, real weights, and genuine cofaces'
idx=support.index(marker)
support=support[:idx]+(p/'intrinsic-graph-proof.md').read_text()+'\n\n'+support[idx:]
support=support.replace(marker,'## Rank-one supporting graph geometry, real weights, and genuine cofaces')
support=support.replace('At a vertex the full kernel of the rational direction matrix is one-dimensional.',
 'From this point through the two-branch reconstruction, assume all local relation cones in both graphs have rank one. This is a supporting case, not a new hypothesis in the broader theorem. At a vertex the full kernel of the rational direction matrix is one-dimensional.')
support=support.replace('contradicting (1).','contradicting the rank-one condition.')
mass_boundary=r'''
The total mass for any constructed \(P\in\gamma+O(1)\) also equals the
raw reference degree, directly. Mixed commutativity (M) gives
\[
 P\cdot(P\cdot[X])-\gamma\cdot(\gamma\cdot[X])
      =(P-\gamma)\cdot((P+\gamma)\cdot[X]).                 \tag{Deg}
\]
The inner divisor is a balanced finite real one-cycle on a common rational
structure. Sum its outer coefficients over all vertices. Every bounded edge
occurs twice with equal inherited weight and opposite primitive outgoing
directions, so its slopes cancel. Every unbounded edge has zero slope for the
bounded affine function \(P-\gamma\). Full lines have no endpoint contribution.
Thus the difference has total degree zero. This is the whole mass identity,
including every actual intermediate edge and end, with no probability
normalization. It is not used to infer contact. The explicit constant-shift
regularization has these same measures at every stage.

'''
support=support.replace('## Elementary finite-dimensional facts used in the reconstruction',
 mass_boundary+'## Elementary finite-dimensional facts used in the reconstruction')
support=support.replace('Suppose one factor is unbranched.', 'Suppose both factors have rank-one relation cones and one factor is unbranched.')
support=support.replace('Assume both graphs branch, and choose original branched vertices \\(A,B\\).',
 'The following whole-space growth estimate applies to every product, with no rank condition. Choose any rational centre \\(A,B\\); in the rank-one two-branch construction these will be original branched vertices.')
support=support.replace('## Rational maps on the original stars and a potential in the fixed class',
 '## Supporting rank-one two-branch obstruction: maps on the original stars')
support=support.replace('By the graph kernel proof, the primitive directions at \\(A,B\\)',
 'For this supporting construction assume both graphs have rank-one cones and choose branched vertices \\(A,B\\). By the graph kernel proof, the primitive directions at \\(A,B\\)')

rank_conclusion=r'''## Complete contact failure in the supporting rank-one two-branch case

The complete PA measure is a finite nonnegative zero-cycle on \(\Pi^{(0)}\).
The exact gap from (37) and (39) is \(P-\gamma-u=-b_0\). It is \(-1\) at
\(o\) and zero at every other \(\Pi\)-vertex, giving the full integral
\[
 \int_X(P_\gamma(u)-\gamma-u)
       \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))
                         =-8\varepsilon^2ab<0.              \tag{48}
\]
Refining for the obstacle can introduce vertices with nonzero bump, but
successive refinement compatibility gives them zero second coefficient.
All singular lower faces, axes, kinks, remote vertices, bounded cycles,
ends and disconnected components are included. The PA operator is this
finite zero-cycle on \(X\), with no point at infinity. The explicit
regularization \(P+1/n\) has identical measures and adds no boundary term.
This reconstruction proves the supporting negative case without granting
a predecessor result. In the broader theorem its coefficient
\(\varepsilon\) is denoted \(\kappa\) to distinguish it from the cap
slope parameter used next.

'''

audit=r'''## Author audit, source boundaries and reproducibility

The fallible higher-relation proposal was read in full and reconstructed.
Its expected coefficient four is confirmed by (HR17)--(HR19), retaining
both intermediate contributions. Its real-centre pinning requires a repair:
endpoints with an irrational second coordinate are not permitted. Equations
(HR13)--(HR15) first pin at rational coordinates; rational same-face enclosing
boxes then prove the bound at every real centre without raw continuity.
The cap is proved intrinsic PC via (G1) and the finite cone, and product
projection is proved through grouped tangent families in (G2). No ambient
extension of intrinsic cap slopes or assertion that projected cells form
a permitted factor structure is used.

The earlier complete argument and canonical campaign.result.notes were
read; the accepted rendering was compared to its full generated rendering.
Their mathematical proof bodies are unchanged by the recorded editorial
differences, and all invoked lemmas are reproduced and checked here.
The author audit checks finite rational domains, real weights, all ordinary
cycles, actual saturated primitive normals, every raw competitor, compact
localization of every prescribed real reference, and the complete integral.
The one-dimensional accessible-mass dossier is read as an existing theorem
to avoid recasting it as new; its entire statement and proof are included
below as comparison evidence and are not premises. Appendix M was checked
for scope: its continuous zero-current frontier concerns P06.2 and supplies
no graph-product result. No P06.2 claim is made here.

There are no essential external theorem premises: all used supporting
mathematics is proved directly above. BMPS v1 supplies the exact definitions
and displayed recursive operator; statements with external premises appear
below only as source comparison data. Its literal integral-slope/rational-
constant function convention and rational weights are explicitly replaced
by the declared real scalar extension, without altering rational spatial
domains or the actual saturated lattices. The coefficient convention is fixed
throughout; no literal regularity conclusion is inferred.

The authoritative `P05.2-argument.md` includes every load-bearing proof and
the exact essential source definition bodies. It is assembled by
`compose_argument.py` from fresh evidence snapshots and the new proof
fragments. `P05.2-partial.tex` is a standalone rendering and
`P05.2-partial.pdf` is compiled twice. `status.json` has exactly five keys:
id, status, exact_result, proof_file, concrete_gaps. The status is partial,
proof_file is P05.2-argument.md, and candidate is false, because original
arbitrary-balanced-space P05.2 remains open.

The exact finite diagnostics in `higher-relation-diagnostic.py` use the
inputs in `higher-relation-input.json` and retain all axis weights, quotient
normals, saturated index-one plane bases, first-cycle balancing, both second
contributions, rational cap bends and supported PCCs. They include a cross
star, a nonsaturated whole-star ray span, and an exact irrational-weight
input over Q(sqrt(2)). Their scope is those finite specified germs, not a
universal proof or an envelope enumeration. The earlier two-branch and
real-sum diagnostics are also rerun in this fresh directory as supporting
finite checks, with their exact original inputs.

Rerun in this directory: `python3 snapshot_sources.py`;
`python3 compose_argument.py`; `python3 higher-relation-diagnostic.py`;
`python3 local-recursion.py`; `python3 real-sum-diagnostic.py`;
`python3 build.py`; `python3 final_checks.py`.
Programs, inputs, outputs, environment, commands, source hashes, author audit,
research limits and build logs are retained locally. Hashes bind artifacts
and read-only origins; they do not certify the mathematics. No supervised
heavy-compute facility is exposed or needed; none was launched. No additional
model/subagent, network, external message, installation, authentication,
proxy/CA, HOME/CODEX_HOME change, old-artifact write, SQL mutation/recovery,
or arbitrary deadline was used. Same-model author audit, finite arithmetic
and compilation are not formal verification or priority certification.

Bibliography: A. M. Botero, E. Mazzon and L. Pille-Schneider,
*Monge--Ampère measures on balanced polyhedral spaces*, arXiv:2603.08664v1,
manuscript dated 10 March 2026. Source definitions and full inspected comparison
bodies are below; no sequel in preparation or unavailable source is used.

'''
defs=old[old.index('## Exact essential source definitions'):]
bmps=(p/'sources/BMPS2603.08664v1.txt').read_text().split('\n')
def clean(x):
 x=''.join(ch for ch in x if ch in '\n\t' or ord(ch)>=32)
 for c in '\uf8eb\uf8ec\uf8ed':x=x.replace(c,'(')
 for c in '\uf8f6\uf8f7\uf8f8':x=x.replace(c,')')
 return x.replace('⪯',r'\preceq').replace('\ue000','(').replace('\ue001',')').replace('ℓ','ell')
appendix='\n\n## Full available inspected primary proof bodies (comparison only)\n\n'
appendix+='The following cached v1 bodies are directly included for independent review. They are not theorem premises; the proofs used in this paper are the reconstructions above. Nonprinting extraction characters are omitted, private-use parenthesis fragments are displayed as ordinary parentheses, and the source script-ell glyph is transcribed as ell in these text quotations. These are typography changes only; the full read-only-origin snapshots retain exact bytes.\n\n'
for title,start,end in [
 ('Normals, local cycles, intersection, refinement and mixed algebra',420,629),
 ('PAPC equivalence and its full source proof',723,786),
 ('Uniform decreasing regularization: full source body',1005,1030),
 ('Degree invariance and full source proof',1363,1391),
 ('Raw envelope properties and full source proof',2261,2293),
]:
 excerpt=clean('\n'.join(bmps[start-1:end]))
 appendix+=f'BMPS v1: {title}, extraction lines {start}--{end}.\n\n```text\n{excerpt}\n```\n\n'
appendix+='## Existing one-dimensional accessible-mass dossier (not a new result or premise)\n\n'
for name in ['one-dimensional-STATEMENT.tex','one-dimensional-PROOF.tex']:
 appendix+='Complete controlling-book input '+name+':\n\n```latex\n'+(p/'sources'/name).read_text()+'\n```\n\n'
am=(p/'sources/appM_ch18_frontiers.tex').read_text().splitlines(True)
appendix+='## Original Appendix M scope check (no P06.2 premise)\n\nThe warning, lines 917--930:\n\n```latex\n'+''.join(am[916:930])+'\n```\n\nIts scope limitation, lines 955--959:\n\n```latex\n'+''.join(am[954:959])+'\n```\n'
argument=(p/'theorem-intro.md').read_text()+'\n'+support+rank_conclusion+(p/'higher-relation-proof.md').read_text()+'\n\n'+audit+defs+appendix
(p/'P05.2-argument.md').write_text(argument)
print(json.dumps({'argument_bytes':len(argument.encode()),'source_bodies_included':True,'full_new_proof_included':True}))
