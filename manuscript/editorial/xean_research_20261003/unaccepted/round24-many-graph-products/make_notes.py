"""Canonical native notes, with explicit local support and no closure claim."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
b=json.loads((root/'build-evidence.json').read_text())
diag=json.loads((root/'diagnostic-output.json').read_text())
evidence=(
 'Observations and exhaustive finite arithmetic for the four specified local product germs only. '
 'The universal theorem, global raw-envelope identification and interpretation of the complete negative integrals use the mathematical proofs in n1 and n2; execution does not establish them.\n\n'
 'diagnostics.py uses exact Fraction arithmetic. At each product facet it computes every incident integral primitive normal lift, its linear function evaluation, the full weighted normal sum and the tangential correction. '
 'For a primitive pair-plane ray (p,q), Bezout integers pu+qv=1 give the primitive integral lift (-v,u), whose sign is selected by the adjacent cone determinant. '
 'The original primitive graph axes embed these lifts into actual ambient lattices. The program retains every saturated plane index and checks each weighted normal sum is tangential before every divisor coefficient. '
 'It directly evaluates all stages, separately every surviving order and a repeated exhausted factor. It does not input a top mass as an assumption.\n\n')
for r in diag['records']:
 counts=[s['nonzero_cells'] for s in r['stages']]
 evidence+=(f"{r['name']}, dimension {r['dimension']}: nonzero cells in successive divisors {counts}; full computed mass {r['full_mass']}; "
            f"{r['surviving_orders']} surviving orders, each {r['each_order_mass']}. Repeated-factor calculation gives zero.\n")
evidence+=(
 '\nAll recorded nonnegativity, tangent-balancing, identical-order and repeated-factor-zero assertions pass. '
 'The higher-rank input uses primitive directions +/- (1,0), +/- (1,2), with actual weights 3/2 on the horizontal pair and 5/3 on the second pair, and outgoing values 0,1/7,0,1/7. '
 'Its ray span has index two. Extra primitive edge directions are (2,3),(3,5),(1,-2),(4,7), with weights 4/5,7/6,5/8,9/11 and values 2/7,3/7,4/7,5/7. '
 'The two-branch input uses first directions (1,0),(1,2),(-3,-2) with relation (2,1,1), second directions (1,0),(0,1),(-1,-1) with relation (1,1,1), actual scales a=3/2,b=5/7 and kappa=1/9. '
 'The first whole-star ray span is index two, while the actual pair plane axes split primitively; its function cones have indices one and two. '
 'Extra directions (2,3),(3,5),(1,-2) have weights 4/5,7/6,5/8 and values 2/9,3/9,4/9. '
 'These are arbitrary local tensor inputs, not an enumeration of global obstacles.\n\n'
 'Source snapshots preserve both root proposals, the entire authoritative two-graph argument and all three canonical campaign.result.notes, the full multivariate graph-cylinder proof and both canonical notes of its actual source campaign, and the authentic installed primary PDFs/texts. '
 'Both supplied proposal hashes match. The selected primary source units, with complete available proof bodies and exact identifiers, are included directly in P05.2-argument.md. '
 'Extraction uses explicit LF splitting, not splitlines on formfeeds. Allermann--Rau arXiv:0709.3705v3, PDF header 20 January 2009, is byte-identical to a fresh local text extraction. '
 'BMPS arXiv:2603.08664v1, manuscript 10 March 2026, has unrelated extraction-layout differences, while every selected non-header body is byte-for-byte present in the fresh extraction. '
 'Source and review provenance are not theorem grants. Original task.problem, completionCriteria and assignment are copied unchanged from input.json.\n\n'
 'The first two compilation attempts failed on an inherited ungrouped mathbb subscript and are preserved as initial-failed-* and second-failed-* logs/evidence. '
 'Explicit TeX grouping and declared typography-only parenthesis/control/script-ell transcriptions repaired rendering without changing mathematics. '
 f"Both final compilation passes exit zero. PDF bytes {b['pdf_bytes']}, SHA256 {b['pdf_sha256']}. "
 'P05.2-argument.md is the authoritative complete proof; P05.2-partial.tex is standalone and P05.2-partial.pdf is compiled twice. '
 'status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with id P05.2, status partial and proof_file P05.2-argument.md. '
 'No full original-scope resolution is claimed.\n\n'
 'Rerun in the assigned fresh workspace: python3 snapshot_sources.py; python3 diagnostics.py; python3 compose_argument.py; python3 build.py; python3 make_notes.py; python3 final_checks.py. '
 'Exact inputs/outputs are diagnostic-input.json and diagnostic-output.json; the program stdout is diagnostic-stdout.txt. '
 'Programs, sources, full LF excerpts, environment.json, source-authentication.json, source-hashes.json, commands.txt, build-evidence.json, build logs, author-self-audit.md, research-notes.md, original inputs, status and canonical result-notes.json are retained. '
 'No operator-supervised heavy-compute facility is exposed or needed; none was launched. '
 'No additional model/subagent, network, external message, installation, authentication/proxy/CA/HOME/CODEX_HOME change, old-artifact write, SQL/recovery or arbitrary deadline was used. '
 'All findings are unverified drafts. Same-author audit, source authentication, compilation and finite arithmetic do not establish mathematical correctness, formal verification or priority.\n\n'
 'Artifacts: '+str(root)+'\n')
notes=[
 {'id':'n1',
  'summary':'Unverified supporting reconstruction in every dimension: saturated quotient-normal balancing/commutativity with the full tangential term, refinement/locality, product and zero-repeat rules, all ordinary-open real-cycle PC/PAPC tests, finite rational all-centre PC cones and exact real-reference decomposition. No prior verdict or source theorem grant is used.',
  'detailedSummary':'Direct all-k codimension-two fan cancellation proves the full recursively defined real-coefficient operator with actual saturated indices. Rational tangent-family generators characterize genuine PC at every real centre and on every allowed structure; rational local one-cycles supply the PAPC converse without irrational vertex insertion. An active-face rational box decomposes every prescribed positive-growth real reference exactly into rational PC references on unchanged rational spatial domains. Product-normal rules, elementary multivariate convex facts and full-recursion vanishing are proved for use in n2. Original P05.2 remains open.',
  'text':(root/'note-foundations.md').read_text(),'support':[]},
 {'id':'n2',
  'summary':'Unverified finite-product classification for every d>=2, every prescribed positive-growth real reference and actual positive real factor weights: regularizable rational-domain PAPC raw envelopes with complete contact for all bounded real-PA obstacles iff every local relation cone has rank one and at most one factor branches. Both failures yield exact PAPC envelopes and complete negative integrals. Original P05.2 remains open.',
  'detailedSummary':'Using n1, rank-one weight ratios normalize each connected factor component rationally, and at most one branched factor gives graph-times-affine components; the full multivariate partial-Legendre/incidence proof, rational spatial maximizer domains and every noncontact stratum are reconstructed. A higher-rank factor yields a proper-support intrinsic cap, global exact-reference localization and fibrewise rational raw pinning, with complete integral -d!(delta epsilon M) product_{j>=2}(2delta b_jw_j). Two rank-one branching factors yield a tensor tripod obstruction; rational apex-fibre PCCs and uniformly available rational radial outer points pin the entire raised-dimensional bump. Full saturated-normal intermediate-cycle formulas give -(d!/2!)8kappa^2ab product_{j>=3}(2kappa b_jw_j). Homogeneous germ support, zero new refinement coefficients and identical constant-shift measures justify both complete integrals. The original arbitrary balanced-carrier atom and literal/analytic/P06.2 scopes are not solved.',
  'text':(root/'note-theorem.md').read_text(),'support':['n1']},
 {'id':'n3',
  'summary':'Exact finite full-recursion diagnostics in dimensions 3 and 5 pass, including an index-two kink, every surviving order and repeated-factor zero. Complete argument, canonical notes, five-key partial status and twice-compiled standalone PDF are retained. Arithmetic, source consistency, author audit and compilation are not mathematical verification.',
  'detailedSummary':'Computed masses are 64/49 and 576000/26411 for the higher-rank product germs, and 64/567 and 6400/6561 for the two-branch tensor germs. Successive nonzero-cell counts are [20,8,1], [144,128,56,12,1], [26,9,1] and [200,164,66,13,1]; 6/120/3/60 surviving orders respectively agree. Every recorded primitive-normal, tangential-balance, nonnegativity and repeat-zero assertion passes. All selected primary bodies are present in fresh local PDF extraction, original task strings and source snapshots are retained, and final TeX compiles twice. Evidence is about these finite programs/artifacts only.',
  'text':evidence,'support':['n1','n2']}]
result={'notes':notes,'candidate':False}
(root/'result-notes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for n in notes:(root/('native-note-'+n['id']+'.md')).write_text(n['text'])
print(json.dumps({'canonical_notes':[n['id'] for n in notes],'note_text_bytes':[len(n['text'].encode()) for n in notes],'candidate':False},indent=2))
