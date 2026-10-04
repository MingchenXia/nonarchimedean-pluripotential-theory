#!/usr/bin/env python3
"""Assemble an incomplete diagnostic dossier; do not issue theorem verdicts."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

notes = [
    {
        'id': 'n1',
        'summary': 'Source-scope repair: van der Put applies over C, not arbitrary K; selected complete proof units are retained. No analytic regularization or scalar-current ascent is established.',
        'detailedSummary': 'The algebraically closed field convention in van der Put is explicit. An elementary root-approximation proof verifies that completion of an algebraically closed valued field is algebraically closed, including positive characteristic; its residue field is algebraically closed and its logarithmic value group is dense when nontrivial. Berkovich rigid-domain comparison is distinguished from an ordinary-neighborhood assertion. Literal source/version checks preserve the controlling INCONCLUSIVE review. These repair scope and provenance, not the missing analytic proof.',
        'text': '''The source-scope repair is valid only over C=completion of a valued algebraic closure of K. Van der Put, Ann. Inst. Fourier 30(4) (1980), 155–164, introduction p.155, assumes a complete algebraically closed non-Archimedean field. Theorem 1.1 states: every one-dimensional normal connected affinoid space is an affinoid subspace of a nonsingular complete curve. Its convention is strict Tate affinoids. The final paragraph of its proof, including the complete Lemma 1.2 proof, is retained. This theorem does not grant arbitrary-K finite-separable algebraization.

Here is the needed elementary field proof, independent of predecessor claims. For a monic degree-d polynomial F over the completion of an algebraically closed valued field A, choose B≥1 bounding its coefficients, ε_m decreasing to zero, and monic F_m over A with coefficient error ≤ε_m^d B^{−(d−1)}. All roots of F_m have norm ≤B by leading-term dominance. Given a root r_m of F_m, |F_{m+1}(r_m)|≤ε_m^d. Factoring F_{m+1} over A shows it has a root r_{m+1} within ε_m of r_m. Ultrametricity makes these roots Cauchy. Their limit is a root of F. Induction factors all polynomials, even inseparable ones. A monic integral lift of any residue polynomial has all roots integral, so its reduced factorization proves residue algebraic closure. Taking n-th roots proves divisible value group; nontriviality gives a nonzero logarithmic value whose rational multiples are dense in R. None of this proves scalar-current transport.

Berkovich, Publ. Math. IHÉS 78 (1993), Theorem 1.6.1 and Lemma 1.6.2(i), DOI 10.1007/BF02712916, work with nontrivially valued fields and Hausdorff strict spaces. Full faithfulness and identification of rigid open affinoid domains with Berkovich affinoid domains do not assert ordinary openness. An actual ordinary-interior identification requires the separate analytic boundary theorem and its applicability.

The supplied causal evidence hash dfc96b12afe112f6eccb35d34417a4199892ded5501305edae0aa15f55c912d3 was matched. Its cached official evidence identifies Thuillier tel-00010990v1 and reports byte identity of the official unversioned PDF with v1; this run made no fresh live retrieval. The round-16 canonical review remains INCONCLUSIVE with 23 premises and 19 passages. Exactly three/five/two canonical predecessor notes were taken from the round-16/17/21 run.json campaign result entries. No predecessor theorem or PASS was accepted as a premise. The requested round-17 proof-core.md is absent; the actual repair-core.md was inspected. Different CLD text caches correspond to the identical v2 PDF, hash 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719, so text line numbers must name their cache.

Artifacts: P06.2-argument.md contains the diagnostic record and eight selected complete primary proof units with LF boundaries and hashes; evidence/source-selections.json, evidence/cache-comparisons.json and evidence/canonical-predecessor-notes.json retain the literal checks. Rerun bash reproduce.sh in this workspace. Source authentication, complete printed proof endings and execution success do not certify new theorem applications. This is a scope/provenance repair, not a complete substantive new analytic theorem.''',
        'support': []
    },
    {
        'id': 'n2',
        'summary': 'Proved a fixed-cycle rational-slope obstruction and elementary tree/cap/tail calculations; finite exact diagnostics pass. The obstruction is restricted to unsubdivided edges and is not an analytic counterexample.',
        'detailedSummary': 'Two parallel edges of lengths 1 and sqrt(2) force rational affine slopes to vanish if endpoint continuity is retained, giving uniform error at least 1/2 against a specified harmonic metric-graph function. This rejects independent rounding on those same edges, but does not rule out refinements. On a genuine finite metric tree, the subtree construction gives an integer-slope auxiliary function with Laplacian 1 at every designated interior vertex, and rational rounding preserves a positive margin. Smooth-max caps and geometric tail shifts are proved as elementary calculations conditional on already existing common-domain analytic approximants. Exact enumeration covers 1,441 labelled trees and 85,787 boundary cases.',
        'text': '''A retained failed approach is independently rounding slopes on an arbitrary fixed cyclic graph. Take vertices v0,v1 and boundary vertices b0,b1, two parallel v0–v1 edges of lengths 1 and √2, and length-1 edges vi–bi. Set F(v0)=0, F(v1)=1, F(b0)=−1−1/√2, F(b1)=2+1/√2, extending affinely. Its outgoing slope sums are 1+1/√2−(1+1/√2)=0 at v0 and −1−1/√2+(1+1/√2)=0 at v1, so it is metric-graph harmonic. If G is affine with rational slopes q1,q2 on those SAME UNSUBDIVIDED parallel edges, continuity forces G(v1)−G(v0)=q1=q2√2. Irrationality of √2 forces both slopes zero: a reduced fraction a/b with a²=2b² would make both a and b even. Consequently G(v0)=G(v1), and 1≤|F(v1)−G(v1)|+|G(v0)−F(v0)|≤2||G−F||∞. No such G approximates F within error <1/2. This is not an analytic example, does not obstruct new subdivisions or other approximants, and is not a solution of P06.2.

For comparison, on any given finite metric TREE T with nonempty boundary B, choose root b∈B. Assign μ=1 at interior vertices I, μ(b)=−|I| and zero at other boundary vertices. On an edge child c→parent give slope Σ_{v in the child subtree}μ(v), and integrate from root value zero. Path uniqueness defines a continuous integer-slope affine ψ. Its outgoing sum at c is that subtree sum minus its child subtree sums, hence μ(c); at the root the same follows from Σμ=0. Thus Δψ=1 on I. If ΔF≥0 on I, F+δψ has margin δ. Rational slopes within η integrate to one G on the tree, with uniform error ≤Lη, L=total edge length, and Laplacian error ≤deg(v)η. Choosing η<δ/(2 max interior degree) preserves strict positivity. This proves only the graph calculation, not that a required actual analytic neighborhood is such a tree or that its rounded slopes have analytic unit-log realizations.

The smooth convex cap calculation is also independent. For an even smooth probability kernel supported in (−1,1), let χ_η=|·|*ρ_η and m_η(s,t)=(s+t+χ_η(s−t))/2. Convexity, |χ_η'|≤1 and the zero first moment show that m_η is smooth convex, nondecreasing in both variables, equals max when |s−t|≥η, and is between max and max+η/2. For a,r>0 and η<ar, m_η(c−at,c−ar) on t≥0 equals the old affine function through t≤r−η/a and the NEW constant c−ar from t≥r+η/a. Its error relative to c is at most ar+η/2. Continuing with that constant is essential. An actual whole annular collar and exact ordinary open overlaps are additional unproved analytic inputs here.

If already constructed approximants on ONE compact Y satisfy ||g_n−f||∞≤b_n=4^(−n), then c_n=Σ_{j≥n}(b_j+b_{j+1})=(5/3)b_n gives u_n=g_n+c_n. Since c_n−c_{n+1}=b_n+b_{n+1}, u_n≥u_{n+1}; moreover 0≤u_n−f≤(8/3)b_n. Constants preserve smoothness/psh already possessed by g_n. This does not produce g_n or replace shrinking domains by a fixed domain.

Program evidence: diagnostics/finite_checks.py uses exact fractions and Prüfer enumeration. Its output diagnostics/output.json reports 1,441 labelled trees of orders 2–6, all 85,787 nonempty boundary assignments, and zero subtree-Laplacian failures. Edge k=0,…,n−2 in decoder order has length (k+2)/(k+1). For order n the count is n^(n−2)(2^n−1): [3, 21, 240, 3875, 81648] respectively. It checks 2,209 pairs from 47 rationals a/b with −6≤a≤6 and 1≤b≤6 in Q(√2), finding only (0,0) continuous slopes. It also checks 100 exact tail identities. These are exhaustive finite results only in the stated finite domains; the universal claims have the proofs above. Rerun python diagnostics/finite_checks.py > diagnostics/output.json, or bash reproduce.sh. Complete arguments are in P06.2-argument.md. No curve recognition, current transport or ordinary psh approximation theorem follows from these diagnostics.''',
        'support': []
    },
    {
        'id': 'n3',
        'summary': 'P06.2 repair remains incomplete: no common fixed-affinoid two-sign ordinary CLD-smooth decreasing psh approximation theorem survives. status.json has exact id P06.2, incomplete, proof_file null; full atom remains open.',
        'detailedSummary': 'The unmet obligations are completed-algebraic ordinary-current transport with actual lengths; singular/nilpotent normalization and puncture bridges; actual affinoid semistable formal-open/local-tree realization with the actual Shilov boundary; simultaneous residual unit germs and every-direction slopes on whole annular overlaps; and assembly of both sequences on one common compact neighborhood. The scope corrections and elementary diagnostics are retained, without transferring earlier verdicts, asserting arbitrary-K algebraization, or counting a tropical graph obstruction as an analytic counterexample. General transcendental ascent, downstairs all-K approximation and original P06.2 are unresolved.',
        'text': '''The fresh target has NOT been proved in this submission. It asks, for every complete nontrivially valued K, every actual good separated strict boundaryless PURE analytic curve, ordinary open U and finite continuous ordinary-zero-current h, for two uniformly decreasing ordinary CLD-smooth psh sequences approximating ±h_C on one compact strict affinoid Y inside any prescribed ordinary neighborhood of each point of U_C, with the point in the actual ordinary interior. Singularities, nilpotents, imperfect fields, positive characteristic and all component Artinian lengths must remain. No extra conditional hypothesis has been substituted for that statement.

The scope repairs in n1 and the elementary calculations/failed rounding route in n2 do not close the analytic gates. The indispensable obligations left unproved here are:
(1) reconstruct completed-algebraic-closure ordinary-current ascent from exact compact ordinary-form descent, actual finite field embeddings, wild/Frobenius stages, componentwise purity and canonical top-measure multiplicities; the fallible round-21 theorem and its prior verdict are not grants;
(2) establish the actual reduction/normalization/conductor/continuous rigid-puncture/component-current chain, including unequal generic lengths, and any normalization-harmonicity-to-ordinary-zero-current bridge;
(3) realize the chosen actual compact strict affinoid as the required semistable formal open and obtain local finite trees with the actual Shilov boundary, including all analytic point types and prescribed ordinary neighborhood constraints;
(4) construct simultaneous residual principal unit-log germs with every-direction slopes, whole annular collars and exact ordinary open overlap domains;
(5) assemble both ordinary smooth psh approximations on the same fixed compact Y.

Thuillier 2.3.8's complete printed proof is now accessible; it asserts the formal-open realization after inserting boundary points. The application required here has not been expanded into a complete independent argument. Lemma 2.2.22 distinguishes type-2 model vertices from type-3 points on a skeleton. Lemma 2.3.22's residual exact sequence and Lemma 2.2.25's slope formula for already existing semistable unit charts do not by themselves give this submission a simultaneous actual unit-germ/annular-overlap construction. Bosch–Lütkebohmert 7.1 is for smooth geometrically connected PROJECTIVE curves, not arbitrary analytic singular curves or a prescribed affinoid formal open. Wanner 1801.04713v3, Theorem 4.7, concerns algebraically closed smooth proper ALGEBRAIC curves and current positivity. It does not itself supply first-stage ordinary regularization. Algebraic tests are included in ordinary analytic tests, not conversely. Correct open caps exclude positive-genus vertices, need strict error margins, and must be checked on whole annuli; fixing those local features does not finish the model chain.

These are missing proofs in this attempt, not counterexamples to the target. No ordinary smooth harmonic approximation is claimed. No psh gluing by partitions, G-cover-to-ordinary-open inference, total fibre-product purity assumption, regular-element-to-S1 inference, universal moment-dimension equality, arbitrary noncompact fixed-index cutoff, or non-strict-radius counterexample is used. General transcendental current ascent and all-K downstairs ordinary approximation remain distinct unresolved obligations. Original P06.2 remains open outside the catalogue's verified scopes; no strict analytic counterexample is produced. P05.2 is untouched.

Deliverables: status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with id P06.2, status incomplete and proof_file null. P06.2-argument.md is the directly accessible diagnostic dossier with selected full primary proof bodies, not a claimed theorem proof. notes.json contains canonical native notes n1–n3 and candidate=false. self-audit.md, research-evidence.md, source-evidence.md and build-evidence.md record the author audit, exact gaps, failed extraction attempt, environment and rerun evidence. No standalone theorem TeX/PDF is emitted because no complete substantive new theorem is claimed. Rerun bash reproduce.sh in the fresh workspace. It checks immutable inputs, LF extraction, exact finite diagnostics, schemas and artifact hashes; it is not mathematical certification. All new files remain here; no predecessor was modified, no network/model/subagent/install/external message was used, and no heavy compute service was supplied or needed.''',
        'support': ['n1', 'n2']
    }
]

payload = {'notes': notes, 'candidate': False}
(ROOT / 'notes.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n')
argument = (ROOT / 'argument-core.md').read_text() + '\n\n' + (ROOT / 'evidence/selected-primary-bodies.md').read_text()
(ROOT / 'P06.2-argument.md').write_text(argument)

status = json.loads((ROOT / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['id'] == 'P06.2'
assert status['status'] == 'incomplete'
assert status['proof_file'] is None
assert payload['candidate'] is False
seen = set()
for note in notes:
    assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    assert note['id'] not in seen
    assert all(s in seen for s in note['support'])
    assert all(isinstance(note[x], str) and note[x] for x in ['id', 'summary', 'detailedSummary', 'text'])
    seen.add(note['id'])

for r in json.loads((ROOT / 'evidence/source-selections.json').read_text()):
    data = Path(r['source']).read_bytes()
    assert sha(data) == r['source_sha256']
    lines = data.decode().split('\n')
    body = '\n'.join(lines[r['first_lf_line']-1:r['last_lf_line']]) + '\n'
    assert sha(body.encode()) == r['body_sha256']
    assert body in argument
diag = json.loads((ROOT / 'diagnostics/output.json').read_text())
assert diag['labelled_trees_total'] == 1441
assert diag['boundary_cases_total'] == 85787
assert diag['tree_laplacian_failures'] == 0
assert diag['parallel_edge_candidate_pairs'] == 2209
assert diag['parallel_edge_continuous_pairs'] == [['0', '0']]
assert diag['tail_shift_exact_checks'] == 100
review = json.loads((ROOT / 'evidence/round16-independent-review.json').read_text())
assert len(review['premises']) == 23 and len(review['passages']) == 19

manifest = {}
excluded = {'evidence/artifact-hashes.json', 'evidence/validation-output.json'}
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and '.git' not in p.parts:
        relative = p.relative_to(ROOT).as_posix()
        if relative not in excluded:
            manifest[relative] = {'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}
(ROOT / 'evidence/artifact-hashes.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'status_schema_valid': True, 'id': 'P06.2', 'proof_file': None,
                  'candidate': False, 'canonical_notes': ['n1', 'n2', 'n3'],
                  'source_body_integrity_checks': 8, 'controlling_review_check_counts': [23, 19],
                  'finite_diagnostic_counts_checked': True,
                  'artifact_count': len(manifest), 'argument_bytes': len(argument.encode()),
                  'mathematical_certification': False}))
