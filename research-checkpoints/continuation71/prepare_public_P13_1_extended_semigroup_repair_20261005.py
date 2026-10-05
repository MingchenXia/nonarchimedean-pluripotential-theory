"""Freeze an original-domain successor using exact Rebouletv1 and a new semigroup proposal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-60/P13.1-public-source-relative-volume-and-uniform-Reeb-energy'
C = R / 'campaigns/round-62/P13.1-public-source-extended-semigroup-and-uniform-energy-differentiation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous = json.loads((old / 'input.json').read_text())
old_manifest = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == old_manifest['input_sha256']
assert sha(old / 'settings.json') == old_manifest['settings_sha256']
reader = R / 'root-checks/public-P13.1-round-60-final-reader'
result = json.loads((reader / 'canonical-notes.json').read_text())
assert result['candidate'] is False and len(result['notes']) == 4
read_state = json.loads((reader / 'root-preservation-and-read-state-continuation70.json').read_text())
assert read_state['whole_argument_root_read'] and read_state['entire_completed_native_result_and_four_notes_root_read']
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
old_sources, end = json.JSONDecoder().raw_decode(suffix)
assert old_sources == old_manifest['public_sources']
context_body = suffix[end:]
extra = json.loads((R / 'shared-sources/Reboulet-primary-cache-20261005-continuation70.json').read_text())
assert extra['saved_version'] == '2004.11635v1'
sources = old_sources + [extra]
assert len(sources) == 11
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
    if 'html' in s: assert sha(s['html']) == s['html_sha256']
contexts = old_manifest['embedded_context'] + [
    {'kind': 'Entire completed round60 partial argument, unreviewed', 'path': str(reader / 'P13.1-argument.md')},
    {'kind': 'Actual completed round60 four canonical notes, unreviewed', 'path': str(reader / 'canonical-notes.json')},
    {'kind': 'Unreviewed extended-semigroup obstacle-approximation proposal', 'path': str(R / 'root-checks/P13.1-extended-semigroup-obstacle-approximation-20261005-continuation70.md')}
]
assert len(contexts) == 8
prefix = prefix.replace('ten exact', 'eleven exact').replace('ten public', 'eleven public')
additional = '''

New original-domain repair after completed round60: independently reconstruct the entire preceding proof, then close its exact remaining singular-quotient obstacle-volume approximation gate and the original uniform differentiation target. None of the eight embedded generated bodies is an accepted dependency. The original problem and completion criteria stay byte-semantically unchanged; do not add global smoothness or an envelope antecedent to the required normal-cone scope.

An eleventh actual public primary body, Reboulet2004.11635v1, is now supplied. Its variety convention is geometrically integral projective and its approximation results use a regular rational point, not global smoothness. Read actual Theorem4.5.4, Remark4.5.5 and Theorem5.1.1 with their complete proofs and standing hypotheses. The introduction's asymptotic-envelope equality assumes continuity of envelopes; distinguish it from the finite-FS energy convergence statement. The printed5.1.1 proof calls the relevant nets decreasing at LF1873--1878, whereas their divisibility order is increasing. LF1585--1590 omits a probability normalization and LF1837--1839 misses the Hilbert factorial. Correct rather than import these chains. Check every external lattice and Chebyshev premise before using the published result.

The additional whole root proposal offers an elementary alternative sufficient for the reverse obstacle inequality. Reconstruct or refute its extended semigroup Gamma={(m,nu(s),a):-Cm<=a<=chi(s)}. At a regular rational point use a graded-lex valuation and prove one-dimensional-leaf dimension counting and a uniform vanishing-order bound by proper complete-intersection curves through that point. Verify all singular-projective Bertini, proper-intersection and dimension-one conditions; handle dimension zero directly. Choose an ample tensor multiple with full section ring generated in degree one and first jets separated. Explicit degree-one value/weight vectors must generate Z^(p+2), including the integer weight direction and degree period. The finite-semigroup conductor proof via bounded zonotope residues must prove c+(cone intersect full lattice) subset S. Derive exact leading lattice slice counts and compact convex-body volume approximation, retaining lattice index and every scalar.

Use the exact count #Gamma_m=sum_a dim F^a R_m=sum_j floor(w_m,j)+(Cm+1)N_m to obtain the signed first moment without an unproved birational/index assertion for every threshold subseries. For each finite semigroup choose actual section witnesses, include a complete degree-one basis at weight -C, and generate a quotient filtration chi_S<=chi with chi_S>=-Cm. Products must place the entire finite semigroup in its value semigroup. Prove the resulting lower signed-mean bound and directed approximation to the full obstacle norm. Reconstruct the actual finite-generated Rees/test-configuration metric and genuine model-energy/barycenter identity on the possibly singular normal projective quotient with every volume/factorial/central multiplicity factor. Every generated section branch must be under the continuous obstacle, so its genuine FS metric is a feasible competitor. The proposed proof needs only a directed family of finite-generated approximants, not convergence of every degree-m approximant or continuity of energy along arbitrary increasing limits.

Then prove F(g)=vol(L,g,h0)/(L^p) for every continuous obstacle on each normal rational quotient, with no EP premise. Combine it with actual residual torification, cone/projective/radial/finite-degree calibration and the both-sign BGM quadratic remainder from the independently rebuilt preceding proof. Derive one fixed dense direction class on K with common positive auxiliary class A omega_eta over each compact Reeb slice. The bounded-obstacle Reeb continuity, genuine local-uniform MA convergence and common quantified constants should pass the genuine cone estimate to irrational fields. The actual outer E-downarrow equality, defining raw decreasing nets and genuine same-Reeb weighted mixed-MA continuity should pass it to E1, with one estimate uniform in the potential and both signs. Approximate fixed continuous directions only after fixing their finite-direction approximation, correcting the source epsilon squeeze. Preserve normalized-root E1 onto comparison and the distinction between pointwise-all-points and strong topology. Do not manufacture a general moving-field unbounded-tail theorem as a new prerequisite.

Candidate=true is allowed only if the unchanged original normal-cone, all-Reeb comparison and actual uniform differentiation target is completely proved, with a self-contained argument, standalone paper and explicit checked source applications. Finite program checks, a nonnegative-only filtration, relative-volume equality alone, a toric endpoint, or an unproved source extension do not satisfy it. If another indispensable gap remains, record its exact mathematical claim and a partial paper honestly.
'''
assignment = prefix + additional + marker + json.dumps(sources, ensure_ascii=False, indent=2) + context_body
for item in contexts[len(old_manifest['embedded_context']):]:
    assignment += '\n## ' + item['kind'] + '\n\n' + Path(item['path']).read_text() + '\n'
for item in contexts:
    if 'sha256' in item: assert sha(item['path']) == item['sha256']
    item['sha256'] = sha(item['path'])
    item['accepted_dependency'] = False
    assert Path(item['path']).read_text() in assignment
inp = {'task': previous['task'], 'notes': [], 'assignment': assignment}
assert inp['task'] == previous['task']
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r62/P13.1-extended-semigroup-and-uniform-energy-differentiation'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 62, 'atom': 'P13.1',
    'directory': str(C), 'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'original_task_unchanged_from_round60': True, 'public_sources': sources, 'embedded_context': contexts,
    'notes_imported': [], 'root_proposals_independently_reviewed': False,
    'fully_solved_original_atom': False,
    'state': 'PREPARED LOCAL ONLY; not launched. Wait for a free slot in the two-item native batch.'}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
                  'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
                  'sources': len(sources), 'context_bodies': len(contexts), 'original_task_unchanged': True,
                  'launched': False}, indent=2))
