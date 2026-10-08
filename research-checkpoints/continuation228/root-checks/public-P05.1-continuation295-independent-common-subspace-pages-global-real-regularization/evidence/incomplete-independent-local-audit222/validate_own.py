#!/usr/bin/env python3
"""Own final validation and binding; never edits supplied paths."""
import pathlib,json,hashlib
P=pathlib.Path(__file__).resolve().parent
B=json.loads((P/'frozen-bindings.json').read_text())
checks=[]
for group in ('math','history','primary'):
    for r in B[group]:
        b=pathlib.Path(r['path']).read_bytes()
        checks.append(hashlib.sha256(b).hexdigest()==r['sha256'] and len(b)==r['bytes'])
notes=json.loads((P/'native-notes.json').read_text()); seen=set()
for n in notes['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    assert set(n['support'])<=seen
    seen.add(n['id'])
assert notes['candidate'] is False
cov=json.loads((P/'whole-read-coverage.json').read_text())
assert sum(r['whole_text_displayed'] for r in cov['math'])==19
run=json.loads((P/'own-build-finite-records.json').read_text())
assert run['exact_output_bytes_equal'] and run['markdown_bytes_equal']
assert len(run['runs'])==6 and all(r['returncode']==0 for r in run['runs'])
hist=json.loads((P/'history-audit-records.json').read_text())
assert hist['saved_equal_actual_after_parsing'] and not hist['saved_equal_bytes']
assert hist['actual_notes']==hist['registered_notes_count']==6
assert all(v['starts_with_actual_text'] and all(v['other_fields_equal'].values()) and v['suffix'].startswith('\n\nArtifacts: ') for v in hist['registered_note_suffixes'])
result={'all_136_bound_objects_still_unchanged':all(checks),'bound_objects':len(checks),
    'own_notes':len(notes['notes']),'candidate':False,'earlier_local_supports_valid':True,
    'whole_math_bodies_displayed':19,'required_whole_audit_complete':False,
    'finite_output_exact':True,'source_to_gfm_exact':True,'fresh_runs_exit_zero':True,
    'saved_actual_json_equal':True,'registered_suffix_only':True,
    'mathematical_source_verdict':'INCONCLUSIVE','historical_evidence_verdict':'INCONCLUSIVE'}
(P/'validation-output.json').write_text(json.dumps(result,indent=2)+'\n')
artifacts=[]
for path in sorted(P.rglob('*')):
    if not path.is_file() or path.name=='own-artifact-bindings.json': continue
    if any(part in {'.git','.agents','.codex','__pycache__'} for part in path.relative_to(P).parts): continue
    b=path.read_bytes()
    artifacts.append({'file':str(path.relative_to(P)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(P/'own-artifact-bindings.json').write_text(json.dumps(artifacts,indent=2)+'\n')
print(json.dumps(result,indent=2))
