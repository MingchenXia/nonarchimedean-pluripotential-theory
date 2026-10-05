"""Freeze a ten-primary-source successor; preserve unlaunched round59."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-59/P13.1-public-source-signed-cone-energy-and-uniform-outer-differentiation'
C = R / 'campaigns/round-60/P13.1-public-source-relative-volume-and-uniform-Reeb-energy'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous = json.loads((old / 'input.json').read_text())
old_manifest = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == old_manifest['input_sha256']
assert sha(old / 'settings.json') == old_manifest['settings_sha256']
prefix, suffix = previous['assignment'].split('\nActual read-only primary sources:\n', 1)
old_source_list, end = json.JSONDecoder().raw_decode(suffix)
assert old_source_list == old_manifest['public_sources']
context_body = suffix[end:]
extra = json.loads((R / 'shared-sources/P13-relative-volume-primary-cache-20261005-continuation69.json').read_text())
assert [s['saved_version'] for s in extra] == ['2004.03847v1', '1805.01016v3']
sources = old_source_list + extra
assert len(sources) == 10
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
    if 'html' in s:
        assert sha(s['html']) == s['html_sha256']
assert extra[1]['fresh_official_and_cached_pdf_bytes_equal']
assert sha(extra[1]['fresh_official_versioned_pdf']) == extra[1]['pdf_sha256']
prefix = prefix.replace('eight', 'ten')
additional = '''

Two additional primary bodies are supplied to reconstruct the relative-volume part of the proof. Boucksom--Gubler--Martin2004.03847v1 Lemma3.2 has the exact hypotheses: geometrically reduced projective scheme over an arbitrary complete NA field, L ample, phi continuous psh on L, and psi1,psi2 continuous psh on an auxiliary ample M. Its two-sided relative-volume estimate and Theorem3.1 do not assume envelope continuity. In contrast, its Section3.2/Theorem3.4 does. Read the complete Lemma3.2 proof, the field-extension/reduced-model/relatively-regular-section/Riemann--Roch applications and all raw intersection/volume factors. On the rational Reeb quotient, normalize by V_omega and use M=A*omega, with projective dimension d=n-1. A proposed explicit remainder constant is 2*d*A*(1+A*tau)^(d-1)*||f|| for |t|<=tau, for d>=1; treat d=0 directly. Derive it rather than assuming it, and retain both signs and one common f.

The supplied Boucksom--Eriksson body is actual 1805.01016v3, authenticated against a freshly downloaded official versioned PDF. Its title and numbering differ from the v2 bibliography in BJ; do not cite a theorem number without checking the actual statement. In this v3, Definition7.2 and Corollary7.6 supply FS/decreasing/uniform PSH conventions, Theorem9.8 supplies bounded-metric relative-volume existence, and Theorem9.15 identifies relative volume with actual continuous-psh energy without an envelope antecedent. Corollary9.16 is a separate conditional envelope assertion. Check field-extension, uniform limits, scalar clearing and the actual MA/Deligne pairing compatibility.

Continuous-psh energy/volume equality alone does not establish F(g)=vol(g) for a non-psh continuous obstacle. Reconstruct the additional asymptotic FS/graded-filtration argument used in BJ8.7 with its exact scope, or justify the stated actual published lemma and supporting claims. If a finite-generated norm approximation can replace an inaccessible supporting result, prove the exact leading signed-mean convergence and obstacle inequalities. Do not infer a missing hypothesis or mark the entire original task solved from a partial volume identity.
'''
assignment = prefix + additional + '\nActual read-only primary sources:\n' + json.dumps(sources, ensure_ascii=False, indent=2) + context_body
inp = {'task': previous['task'], 'notes': [], 'assignment': assignment}
for context in old_manifest['embedded_context']:
    assert sha(context['path']) == context['sha256']
    assert Path(context['path']).read_text() in assignment
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r60/P13.1-relative-volume-and-uniform-Reeb-energy'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
manifest = {
    'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 60, 'atom': 'P13.1',
    'directory': str(C), 'input_sha256': sha(C / 'input.json'),
    'settings_sha256': sha(C / 'settings.json'),
    'original_task_unchanged_from_round59': inp['task'] == previous['task'],
    'public_sources': sources, 'embedded_context': old_manifest['embedded_context'],
    'notes_imported': [], 'root_proposals_independently_reviewed': False,
    'supersedes_unlaunched_round59': True, 'fully_solved_original_atom': False,
    'state': 'PREPARED LOCAL ONLY; not launched. Round51 P13.2 review completed INCONCLUSIVE; round58 P16.1 author remains active.'
}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: manifest[k] for k in ['directory', 'input_sha256', 'settings_sha256', 'original_task_unchanged_from_round59', 'state']}, indent=2))
print('input_bytes', (C / 'input.json').stat().st_size)
