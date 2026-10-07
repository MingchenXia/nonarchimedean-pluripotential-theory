from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

R = Path('/workspace/research')
old = next((R/'campaigns/round-183').iterdir())
C = R/'campaigns/round-184/P05.2-original-polyhedral-orthogonality-control-glyph-repair'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists() and not (old/'work.sqlite').exists()
log = (old/'controller-output-LOCALONLY.log').read_text()
assert 'Invalid value:' in log and '/task/problem: must match pattern' in log
inp = json.loads((old/'input.json').read_text())
original = inp['task']['problem']
bad = [(i, ord(c)) for i, c in enumerate(original) if ord(c)<9 or 14<=ord(c)<=31 or ord(c)==127]
assert len(bad) == 20
# Retain each unrenderable PDF glyph as an explicit visible marker, rather
# than guessing its mathematical meaning or silently deleting a delimiter.
inp['task']['problem'] = re.sub(r'[\x00-\x08\x0e-\x1f\x7f]', lambda m: '[PDF_GLYPH_U+%04X]' % ord(m[0]), original)
inp['assignment'] += '\n\nInput representation clarification: twenty control glyphs in the PDF-extracted family dossier are preserved as visible [PDF_GLYPH_U+XXXX] markers. These are extraction artifacts, not mathematical assumptions. Determine any essential delimiter/relation from its full formula context and the original primary source; report ambiguity if unresolved. No ordinary mathematical character, hypothesis, obstacle class, or completion criterion has been removed or altered. The failed183 declaration never admitted a model call; all previous failure evidence remains immutable.'
C.mkdir(parents=True)
(C/'task.json').write_text(json.dumps(inp['task'], ensure_ascii=False, indent=2)+'\n')
(C/'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2)+'\n')
(C/'original-task.json').write_bytes((old/'original-task.json').read_bytes())
s = json.loads((old/'settings.json').read_text())
s['codex']['workspace'] = str(C/'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r184/P05.2-original-control-glyph-repair'
(C/'settings.json').write_text(json.dumps(s, indent=2)+'\n')
(C/'mathematical-data-bindings.json').write_bytes((old/'mathematical-data-bindings.json').read_bytes())
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), failed_round=183,
    failed_campaign=str(old), failure_stage='Input declaration schema validation before database creation or model admission',
    failed_input_sha256=sha(old/'input.json'), controller_failure_sha256=sha(old/'controller-output-LOCALONLY.log'),
    model_calls_admitted=0, failure_evidence_preserved=True, repair_round=184,
    control_glyph_locations_and_codepoints=bad, replacement='[PDF_GLYPH_U+XXXX]',
    ordinary_mathematical_characters_removed=0, scope_and_completion_criteria_unchanged=True,
    no_auth_account_runtime_changes=True, original_closed=False)
(C/'input-representation-repair.json').write_text(json.dumps(record, indent=2)+'\n')
(R/'root-checks/P05.2-round183-declaration-failure-and-repair184-20261007.json').write_text(json.dumps(record, indent=2)+'\n')
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=184, atom='P05.2', directory=str(C),
    task_sha256=sha(C/'task.json'), input_sha256=sha(C/'input.json'), input_bytes=(C/'input.json').stat().st_size,
    settings_sha256=sha(C/'settings.json'), original_task_sha256=sha(C/'original-task.json'),
    only_complete_grants=[], route='Xean native Codex', model='gpt-6.1-sol', reasoning='xhigh',
    maximum_concurrent_campaigns=2, complete_original_family_body_supplied=True,
    entire_family_dossier_independently_root_proof_read=False, original_closed=False,
    no_private_active_output_read=True, no_hot_feedback=True, protected_editor_unchanged=True)
(C/'freeze.json').write_text(json.dumps(f, indent=2)+'\n')
assert not re.search(r'[\x00-\x08\x0e-\x1f\x7f]', inp['task']['problem'])
launcher = (R/'launch_frozen_original_polyhedral_orthogonality183_20261007.py').read_text()
launcher = launcher.replace('round-183', 'round-184').replace("'round':183", "'round':184").replace('+[183]', '+[184]')
(R/'launch_frozen_original_polyhedral_orthogonality184_20261007.py').write_text(launcher)
print(json.dumps(f, indent=2))
