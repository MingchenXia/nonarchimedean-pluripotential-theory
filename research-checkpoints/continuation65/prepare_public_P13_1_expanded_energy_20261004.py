"""Freeze an expanded primary-source-only P13.1 task; do not launch it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-54/P13.1-public-source-signed-energy-uniform-Reeb-differentiation'
C = R / 'campaigns/round-55/P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous_input = json.loads((old / 'input.json').read_text())
previous_manifest = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == previous_manifest['input_sha256']
sources = previous_manifest['public_sources']
extra = json.loads((R / 'shared-sources/P13-extra-primary-cache-20261004-continuation64.json').read_text())
extra.append(json.loads((R / 'shared-sources/P13-BHJ-primary-cache-20261004-continuation64.json').read_text()))
titles = {
    '1805.11160v1': 'Boucksom--Jonsson, A non-Archimedean approach to K-stability',
    '1204.6277v2': 'Chambert-Loir--Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich',
    '1504.06568v3': 'Boucksom--Hisamoto--Jonsson, Uniform K-stability, Duistermaat--Heckman measures and singularities of pairs',
}
for s in extra:
    s['title'] = titles[s['saved_version']]
sources = sources + extra
assert len(sources) == 8
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
assignment = previous_input['assignment'].split('\nRead-only published source caches:\n')[0]
assignment = assignment.replace('five actual public primary sources', 'eight actual public primary sources')
assignment += '''

Additional primary-source obligations for this fresh expanded-source task:

Boucksom--Jonsson1805.11160v1 Theorem4.13 has a smooth projective standing hypothesis. Do not apply it unchanged to singular normal Reeb quotients. The actual normal-projective test-configuration/Duistermaat--Heckman route is available in BHJ1504.06568v3: inspect Proposition2.15, Proposition3.12, Theorem5.9, and the actual intersection/Monge--Ampere energy formula in Section7. A measure-distribution theorem alone does not identify the mean with the genuine energy. Check finite-generation, signed rational weights, normalization, projective normality and any passage from a filtration to a model metric. If an FS list generates a primary ideal rather than the coordinate algebra, prove the needed finite-type representation or approximation and ensure all estimates survive it. Relations in the coordinate algebra may increase the quotient norm's actual generator weights.

Use the actual CLD1204.6277v2 body for local uniform mixed-MA convergence, calibrated integration, and any finite morphism or Veronese reduction. Its scope includes singular analytic spaces and trivial valuations, with its explicitly stated separation, pure-dimensionality, boundary and structural hypotheses. Inspect the actual weighted-current continuity in Theorem8.7.2 and structure in Theorem15.7.1 rather than assuming classical smooth Bedford--Taylor theory. In Wu2106.13395v2 Proposition5.13 the local sections lie in mL; verify the coefficient of the radial local coordinate, the possible finite degree of the associated moment map and the integral lattice/calibration. A written product trivialization with an mL section does not by itself trivialize L. State the volume and genuine mixed-MA normalization for eta=s eta0 and O_ProjR(d)/(s d), including nonstandard weighted gradings and ineffective integral Reeb actions.

The envelope input is mathematically pivotal. Inspect Lyuhui Wu2609.27610v1 Definitions3.15 and6.1, Theorem4.19 and Theorems6.2/6.3/6.5/7.1 as an actual dependency chain. The lower-growth reading of Definition3.15 and the upper-growth reading of Definition6.1 disagree, for example on log|z|; state a consistent convention. Theorem4.19's invocation of Theorem3.25(1) requires prior membership in the regularizable logarithmic class, so correcting an inequality sign alone cannot prove the desired regularization. Reconstruct a noncircular replacement wherever used. Local truncation and gluing on a smooth projective compactification is one possible route, but its local psh definition, boundary neighborhoods, smooth local/global theorem, global FS approximation, countable-base reductions and any singular induction must actually be proved or justified. Do not infer projective envelopes on a singular quotient from an invalid intermediate assertion. Unretrieved supporting preprints are neither established premises nor evidence of falsity; prove their exact necessary replacements or state the genuine remaining condition.

This remains a cold source-only task: no previous generated proof, root mathematical note or review report is included or accepted as a dependency. The original problem and completion criteria are byte-preserved from the prepared round54 task. Do not assume that these diagnostic instructions establish any missing theorem. A conditional or incomplete envelope argument remains partial even if all algebraic energy estimates succeed.

Read-only published source caches:
'''
inp = {'task': previous_input['task'], 'notes': [], 'assignment': assignment + json.dumps(sources, ensure_ascii=False, indent=2) + '\n'}
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r55/P13.1-expanded-signed-energy-uniform-Reeb-differentiation'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
manifest = {
    'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 55, 'atom': 'P13.1',
    'directory': str(C), 'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'original_dossier_sha256': previous_manifest['original_dossier_sha256'],
    'task_equal_to_round54': inp['task'] == previous_input['task'], 'public_sources': sources,
    'generated_preceding_mathematical_payload_included': False,
    'supersedes_unlaunched_round54_for_next_slot': True,
    'state': 'PREPARED LOCAL ONLY; not launched. Active batch remains round56 P16.1 author and round51 P13.2 review.',
    'fully_solved_original_atom': False,
}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: manifest[k] for k in ['directory', 'input_sha256', 'settings_sha256', 'task_equal_to_round54', 'state']}, indent=2))
