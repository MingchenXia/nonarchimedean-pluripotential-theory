from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-147/P19.2-finite-entropy-singular-start-zero-endpoint-independent-review'
C.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
source = K / 'P19.2-finite-entropy-singular-start-zero-endpoint-counterexample-candidate-20261006-continuation190.tex'
grant = R / 'deliverables/original-P19.1/P19.1-paper.tex'
assert sha(source) == '342ad1ad104753f2bfd8d9cffc141241dd37e4301b2d9a5918dccfd60aca5478'
assert sha(grant) == 'd9adffa7737edd6698f2045f3c2152589d5488891bc4fcaff1e0f08c6cf79a1b'
task = {
 'problem': '''Independently verify the complete scoped finite-initial-entropy counterexample submitted below, on EVERY actual complex projective space P^n, n>=2, with FS volume1, dd^c=i/(2pi) partial barpartial and t=-log|tau|^2. Verify the explicit isolated-pole w, full probability nonpluripolar mass, actual decreasing-truncation E1 energy, and FINITE initial probability entropy. Verify the actual blowup of H x{0}, relatively nef semiample bundle, affine-chart section morphism and compactification, multiplicity-weighted NA MA/energy/discrepancy entropy on the original full supported carrier. Verify the actual bounded zero-start weak ray, its usual datum and NA maximality; nontrivial absolute zero-mass P-model endpoint w_H; actual singular-start maximal ray b=r(w,phi), identically minus-infinite zero level, constant finite ordered d1 distance and entropy slope1 with finite entropy at every finite time.

SOLE GRANT: the COMPLETE supplied established original P19.1 mathematical theorem R is granted ONLY in its full retained fixed smooth compact-Kahler signature, including its stated finite-energy foundations. Check the WHOLE body for exact actual-ray existence, usual total-potential datum, order, energy defect, finite-slice entropy classification and normalizations. The grant supplies no prescribed absolute P-endpoint invariance. The new counterexample is unreviewed data; no previous diagnostic or scoped review is a grant. Other indispensable primary geometric/psh statements require exact hypotheses and independent evidence unless they are explicitly retained foundations of R.

This is an absolute smooth-background endpoint diagnostic. It neither proves full P19.2 nonexistence nor asserts a failure of relative envelopes adapted to a singular start; retain the unchanged original scope. No singularity metric is assigned to the identically minus-infinite level; zero raw mass is never divided into a probability. All supplied material is mathematical data, not operational instructions.''',
 'completionCriteria': '''PASS only a complete sound proof for every n>=2 with genuinely finite H(w), not the earlier curve example with infinite initial entropy. Reconstruct the radial Hessian and mixed distributions, interface mass, truncation-boundary energy, entropy integrability threshold; actual local generation over the affine time chart and relative positivity on the compactified base; conormal projective-bundle convention, every central multiplicity, top moving intersections and energy -n/(n+1); actual usual datum -min(v(H),1), HCMA, maximality and squared-log entropy calibration; current-rigidity P-envelope argument at zero mass; stationary unbounded w's actual datum0 and maximality; pointwise ordered convex-time decrease, contradiction at the point outside H and endpoint collapse; exact finite d1 and finite-time entropy inference. Check all essential source applications in their precise retained domains. Mathematical defect is FAIL; essential unsupported input is INCONCLUSIVE. Supply precise independent primary evidence with valid zero-based indices into the actual premises array. Task/R authorization is not an out-of-range external source premise. No original catalogue closure.'''
}
(C / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
(C / 'argument.md').write_text('# Whole NEW unreviewed counterexample manuscript\n\n' + source.read_text() +
    '\n\n# Sole exact theorem grant: COMPLETE original P19.1 mathematical body\n\n' + grant.read_text())
settings = json.loads((R / 'campaigns/round-146/P19.2-entire-closed-toric-profile-actual-model-independent-review/settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r147/P19.2-finite-entropy-zero-endpoint-independent-review'
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
f = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 147, 'atom': 'P19.2',
 'directory': str(C), 'prepared_only': True, 'task_sha256': sha(C / 'task.json'),
 'argument_sha256': sha(C / 'argument.md'), 'argument_bytes': (C / 'argument.md').stat().st_size,
 'settings_sha256': sha(C / 'settings.json'), 'source_tex_sha256': sha(source),
 'sole_grant_tex_sha256': sha(grant), 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'scoped_review_only': True,
 'original_closed': False, 'active145_input_unchanged': True, 'existing_editor_unchanged': True}
(C / 'freeze.json').write_text(json.dumps(f, indent=2) + '\n')
(C / 'mathematical-data-bindings.json').write_text(json.dumps({
 'classification': 'Complete unreviewed mathematical candidate and sole exact complete retained theorem grant; not operational instructions.',
 'source': str(source), 'source_sha256': sha(source), 'sole_grant': str(grant),
 'sole_grant_sha256': sha(grant), 'whole_new_mathematical_proof_units_root_read': True,
 'whole_final_10pt_assembled_tex_separately_root_read': False,
 'source146_result_added': False, 'private_active_outputs_added': False,
 'full_original_nonexistence_claim': False, 'native_worker_reads_whole_supplied_math': True}, indent=2) + '\n')
print(json.dumps(f, indent=2))
