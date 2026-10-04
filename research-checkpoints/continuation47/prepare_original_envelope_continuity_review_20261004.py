"""Freeze an exact abstract-theorem review; original P03.3 closure is separate."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path('/workspace/research')
author = R / 'campaigns/round-36/P03.3-original-envelope-continuity'
run = json.loads((author / 'run-v2.json').read_text())
assert run['campaign']['status'] == 'completed' and run['campaign']['error'] is None
result = run['campaign']['result']
assert result['candidate'] is False
w = Path(result['workspace'])
status = json.loads((w / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['id'] == 'P03.3' and status['status'] == 'partial'
proof = w / status['proof_file']
snapshot = R / 'root-checks/original-envelope-round-36-final-reader'
assert proof.read_bytes() == (snapshot / proof.name).read_bytes()
preliminary = R / 'root-checks/original-envelope-continuity-preliminary-reader/P03.3-argument.md'
assert proof.read_text().splitlines()[:145] == preliminary.read_text().splitlines()[:145]
ids = set()
for n in result['notes']:
    assert set(n['support']) <= ids
    ids.add(n['id'])
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review = author.with_name(author.name + '-review')
review.mkdir(exist_ok=False)
task = {
    'problem': 'Independently reconstruct the following exact abstract statements produced while investigating original P03.3: ' + status['exact_result'] + '\n\nThe full proof and all actual canonical notes are supplied directly. This review judges only these explicitly conditional abstract/finite-graph results. No analytic realization, positive-dimensional geometric application, sharp classification, or original catalogue closure is claimed.',
    'completionCriteria': 'Check every mathematical theorem and supporting deduction: greatest feasible vector on a finite connected metric graph, boundary contact and harmonic complementarity, empty boundary and isolated vertex, exhaustive nonsingular contact-set algorithm with parallel edges; compact connected Hausdorff harmonic-skeleton criterion with exact global realization, harmonic lifting, dense obstacles and comparison for EVERY competitor; existence of contact and nonempty boundary in the comparison set; global minorants and two-sided uniform stability; lattice-density proof and counterexample to a common competitor modulus; full-family fibre reduction under a continuous closed open surjection with compact nonempty fibres and a class-preserving section; and the density-based scalar transfer with separately assumed exact skeletal identities and nonemptiness. Independently reconstruct all essential proofs. Conditional analytic gates remain conditional and may not be silently granted. Distinguish finite execution evidence from mathematical proof. Use the requested native gpt-6.1-sol/xhigh route. Do not read private transcripts, SQL, auth, frozen P15 audit files or other generated draft workspaces. No external messages, installs, runtime/account/sandbox changes, or additional model/worker/subagent invocations. PASS only if the entire exact abstract scope is correct and complete. FAIL for a substantive false statement or proof defect; INCONCLUSIVE for a genuine unresolved indispensable premise. Original P03.3 acceptance is separate.'
}
argument = ('# Exact abstract scope and explicit original limitations\n\n' + json.dumps(status, ensure_ascii=False, indent=2)
            + '\n\n# Full final proof\n\n' + proof.read_text()
            + '\n\n# All actual canonical notes\n\n' + json.dumps(result['notes'], ensure_ascii=False, indent=2)
            + '\n\n# Actual source provenance: no primary analytic application claimed\n\n' + (w / 'source-provenance.json').read_text())
(review / 'argument.md').write_text(argument)
(review / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((R / 'campaigns/round-32/P15.2-minimum-reference-full-mass-operator-review/settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r36/P03.3-exact-abstract-review'
assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
(review / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
freeze = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope': status['exact_result'], 'original_atom_solved': False,
          'argument_sha256': sha(review / 'argument.md'), 'argument_bytes': (review / 'argument.md').stat().st_size,
          'task_sha256': sha(review / 'task.json'), 'settings_sha256': sha(review / 'settings.json'),
          'author_proof_sha256': sha(proof), 'author_tex_sha256': sha(w / 'P03.3-paper.tex'),
          'canonical_result_sha256': sha(snapshot / 'canonical-result.json'),
          'root_full_proof_read': 'Final LF1-145 exactly identical to fully read preliminary snapshot; final LF146-289 fully read. All3 canonical text/summary/detailedSummary/support fields fully read.',
          'root_primary_provenance_build_verification_read': True,
          'blocked_P15_payload_included': False, 'provider_submission_attempted': False}
(review / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(review), 'freeze_sha256': sha(review / 'freeze.json'),
                  'argument_bytes': freeze['argument_bytes'], 'original_atom_solved': False}, indent=2))
