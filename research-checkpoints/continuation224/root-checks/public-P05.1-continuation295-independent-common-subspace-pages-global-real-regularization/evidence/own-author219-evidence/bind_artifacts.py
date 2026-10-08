#!/usr/bin/env python3
"""Own explicit artifact manifest; no circular self-hash and no unknown files read."""
import pathlib,json,hashlib
P=pathlib.Path(__file__).resolve().parent
names=['clarification-control.md','P05.1-paper.tex','P05.1-paper.pdf','P05.1-paper.aux','P05.1-paper.log','P05.1-paper.out','P05.1-paper.toc','argument.md','source-application-ledger.md','proof-source-coverage.md','scope-and-gaps.md','README-reproduce.md','execution-history.md','mathematical-packet-bindings.json','private-primary-packet-bindings.json','source-byte-bindings.json','retained-original-task.json','environment.json','read_bound.py','read-coverage.jsonl','whole-read-coverage.json','primary-unit-coverage.json','audit_inputs.py','audit-inputs-output.txt','make_ledger.py','source-ledger-output.txt','exact-check-input.json','exact_checks.py','exact-check-output.txt','build_paper.py','build-runs.json','build-output.txt','markdown-build.stdout.txt','markdown-build.stderr.txt','initial-failed-P05.1-paper.tex','initial-failed-build-runs.json','initial-failed-build-output.txt','pre-layout-build-runs.json','make_native_notes.py','native-notes.json','native-notes-output.txt','bind_artifacts.py','validate_delivery.py']
for stem in ['initial-failed-build','pre-layout-build-pass-1','pre-layout-build-pass-2','build-pass-1','build-pass-2','build-pass-3']:
 for suffix in ['stdout.txt','stderr.txt','tex.log']:names.append(stem+'.'+suffix)
rows=[]
for name in names:
 p=P/name; assert p.is_file(),name
 b=p.read_bytes();rows.append({'name':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
obj={'schema':'own-artifact-bindings-v1','input_binding_files':['source-byte-bindings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json'],'artifacts':rows,'excluded_from_self_hash':['artifact-bindings.json','artifact-binding-output.txt','validation-output.txt','__pycache__'],'note':'Saved-run hashes; rerun timestamps can change PDF/log bytes. These are bindings, not mathematical verification.'}
(P/'artifact-bindings.json').write_text(json.dumps(obj,indent=2)+'\n')
print(f'Bound {len(rows)} explicitly enumerated own artifacts; no circular self-hash.')
