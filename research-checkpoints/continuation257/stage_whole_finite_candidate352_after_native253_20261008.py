from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-253').iterdir()); A=C/'artifacts/codex-6QnA00'
D=K/'public-P12.6-continuation352-geometric-finite-transfer-and-envelope-obstructions-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
freeze=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
    assert sha(C/name)==freeze[name.replace('.json','').replace('-','_')+'_sha256']
binding_counts={}
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    entries=json.loads((C/name).read_text()); binding_counts[name]=len(entries)
    for e in entries:
        p=Path(e['path']);assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
        if 'origin' in e:assert sha(e['origin'])==e['sha256']
assert json.loads((A/'input.json').read_text())==json.loads((C/'input.json').read_text())
actual=json.loads((K/'round253-actual-native-final.json').read_text())
assert actual['candidate'] is False and len(actual['notes'])==7
expanded=json.loads((A/'native-notes.json').read_text())
assert expanded['candidate'] is False and [n['id'] for n in expanded['notes']]==[n['id'] for n in actual['notes']]
known={'G331','G345'}
for n,e in zip(actual['notes'],expanded['notes']):
    assert n['support']==e['support'] and all(s in known for s in n['support']);known.add(n['id'])
proof=(A/'proof.tex').read_text();paper=(A/'P12.6-paper.tex').read_text();argument=(A/'argument.md').read_text()
assert proof in paper and sha(A/'P12.6-paper.tex')=='0f29595f68589c7f179146bd8417f60fed51592be8621cea9e8c802f9dcc2a2e'
starts=[m.start() for m in re.finditer(r'\\section\{',proof)];assert len(starts)==7
for i,s in enumerate(starts):
    body=proof[s:starts[i+1] if i+1<len(starts) else len(proof)]
    assert body in argument and body in expanded['notes'][i]['text']
math=json.loads((C/'mathematical-packet-bindings.json').read_text())
assert len(math)==17
for e in math:
    p=Path(e['path']);q=A/'attachments'/p.name
    assert q.stat().st_size==e['bytes'] and sha(q)==e['sha256']
for e in math[:14]:assert Path(e['path']).read_text() in paper
audit=json.loads((A/'reports/input-audit.json').read_text())
assert len(audit['inputs'])==53
for e in audit['inputs']:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
final=json.loads((A/'reports/final-audit.json').read_text());assert len(final['files'])==16
for e in final['files']:assert (A/e['file']).stat().st_size==e['bytes'] and sha(A/e['file'])==e['sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    live=json.loads((R/name).read_text());assert len(live['fully_solved_original_atoms'])==15 and live['remaining_open_original_atoms']==27 and live['historical_reviewed_scoped_papers']==96 and live['github_pending_checkpoint'] is None
shutil.copytree(A,D)
for name in ['original-task.json','task.json','freeze.json','launch-record.json','qualified-imported-note-bindings.json']:
    shutil.copyfile(C/name,D/('native253-'+name))
shutil.copyfile(K/'round253-actual-native-final.json',D/'actual-native253-final.json')
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=253,continuation=352,atom='P12.6',status='Complete new mathematical draft and ROOT reading; UNREVIEWED, originalOPEN, no accepted paper',native_candidate=False,actual_FINAL=dict(path=str(K/'round253-actual-native-final.json'),bytes=(K/'round253-actual-native-final.json').stat().st_size,sha256=sha(K/'round253-actual-native-final.json'),notes=7,intermediates_excluded=5),paper=dict(path=str(D/'P12.6-paper.tex'),bytes=(D/'P12.6-paper.tex').stat().st_size,sha256=sha(D/'P12.6-paper.tex')),proof=dict(path=str(D/'proof.tex'),bytes=(D/'proof.tex').stat().st_size,sha256=sha(D/'proof.tex')),ROOT_reading='All seven actual FINAL notes and every field read completely. Entire 53282-byte proof.tex read physically in overlapping bounded chunks. Entire source ledger and coverage re-read after initial outer truncation. Whole scope, original-scope and decision read. All seven entire proof sections match argument.md and expanded note bodies; every expanded-note field and all prose outside those matched sections read completely. Paper header read, full fourteen qualified components checked literal; no fresh whole 344405-byte reader claim.',fresh_primary_reading='SH17.1.6 full statement/sketch and entire SH17.4.1 setup, 17.4.2 proof, 17.4.3 convention, 17.4.4 proof freshly read from immutable author text. Primary PDFs/text/pixels remain LOCALONLY; no fresh pixel claim.',current_body_checks=dict(frozen_manifest_counts=binding_counts,native_input_equals_controller=True,native_input_audit_current_files=53,native_final_audit_current_files=16,whole_proof_in_reader=True,all_fourteen_qualified_components_literal=True,all_seven_whole_sections_in_argument_and_expanded_notes=True),bounded_evidence='Native 802 finite arithmetic observations and 26 consistency checks are retained as data, not proof. ROOT ran no supplied native scripts.',only_grants=['Entire qualified G331','Entire qualified G345'],new349_351_not_in_native253_input=True,scope_question='Next independent reviewer must judge exact P12.6 separately from P12.3 general envelope existence. Native253 candidate=false and all reported gaps remain preserved; new conductor-admissible trace and noninjective counterexamples are unreviewed reconstruction DATA.',original_closed=False,accepted_paper=False,compile_status='NOT RUN for this new source; pending built-in cell1010 concerns P12.5, not P12.6; no PDF verification',protected_editor_open_unchanged=True,source_bodies_pixels_LOCALONLY=True)
write(D/'mandatory-source-scope-and-ROOT-reader-qualifications-before-review255-20261008.json',record)
B=K/'P12.6-round253-whole-geometric-finite-candidate352-ROOT-proof-source-scope-and-binding-20261008.json';assert not B.exists();write(B,record)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,P12_6_candidate352=dict(directory=str(D),paper=record['paper'],status=record['status'],native_candidate=False,ROOT_binding=str(B),original_closed=False),current_active_batch=[254],next_work='Prepare and launch independent255 whole-originalP12.6 with entire new349/351 reconstructed, onlyqualifiedG331/G345. Native254 remains frozen P12.3. Push257 full newdraft/frozen packets. 15solved27OPEN96papers; compile1010 pending.')
    write(p,x)
print(json.dumps(dict(staged_candidate352=str(D),paper=record['paper'],binding=str(B),current_input_files=53,current_own_artifact_files=16,accepted=False,original_closed=False,counts_unchanged=True),indent=2))
