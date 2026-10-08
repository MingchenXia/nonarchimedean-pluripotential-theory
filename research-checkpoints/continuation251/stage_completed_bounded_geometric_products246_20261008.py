from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-246').iterdir());A=C/'artifacts/codex-FwCorE'
D=K/'public-P12.4-continuation341-bounded-moment-measures-and-geometric-curve-reference-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def binding(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not D.exists()
own=json.loads((A/'reports/own-bindings.json').read_text())['files']
for e in own:
    p=Path(e['path']);p=p if p.is_absolute() else A/p
    assert p.is_file() and p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],str(p)
records=json.loads((A/'reports/input-hashes.json').read_text())['records'];input_count=0
for e in records:
    for p in [Path(e['original']),A/e['local']]:
        assert p.is_file() and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']==e['expected_sha256'],str(p)
        input_count+=1
assert json.loads((C/'input.json').read_text())==json.loads((A/'input.json').read_text())
actual_path=K/'round246-actual-native-final.json';actual=json.loads(actual_path.read_text());expanded=json.loads((A/'native-notes.json').read_text())
assert actual['candidate'] is False and expanded['candidate'] is False
assert [(n['id'],n['support']) for n in actual['notes']]==[(n['id'],n['support']) for n in expanded['notes']]
D.mkdir();(D/'reports').mkdir();(D/'inert-author-programs-DATA').mkdir()
for name in ['P12.4-paper.tex','P12.4-paper.pdf','argument.md','source-application-ledger.md','exact-scope.md',
    'whole-proof-coverage.md','original-scope-and-noncircularity-decision.md','native-notes.json','bounded-evidence-input.json']+[f'n{i}.md' for i in range(1,8)]:shutil.copyfile(A/name,D/name)
for name in ['own-bindings.json','environment.json','exact-diagnostics.json','input-hashes.json','build-results.json','final-audit.json']:shutil.copyfile(A/'reports'/name,D/'reports'/name)
for name in ['audit_inputs.py','exact_diagnostics.py','build_delivery.py','final_audit.py']:shutil.copyfile(A/name,D/'inert-author-programs-DATA'/name)
shutil.copyfile(actual_path,D/'actual-native-FINAL.json');shutil.copyfile(C/'original-task.json',D/'exact-original-task.json')
grant=json.loads((C/'input.json').read_text())['notes'][0];write(D/'G331-qualified-grant.json',grant)
math=json.loads((C/'mathematical-packet-bindings.json').read_text())
for index,name in [(2,'G331-paper.tex'),(3,'G331-mandatory-source-scope.json'),(4,'G331-source-application-ledger.md'),(5,'G331-exact-scope.md'),(6,'G331-acceptance.json')]:shutil.copyfile(math[index]['path'],D/name)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=246,atom='P12.4',continuation=341,
    status='UNREVIEWED complete partial mathematical draft; original OPEN',original_closed=False,paper_accepted=False,author_candidate=False,
    ROOT_all_actual_FINAL_notes_and_fields_physically_read=True,ROOT_whole_TeX_source_physically_read=True,
    ROOT_TeX_read_chunks='Characters0:18000,18000:36000,36000:end',
    ROOT_whole_source_ledger_scope_coverage_and_original_decision_physically_read=True,
    parallel_argument_separately_whole_ROOT_read=False,
    actual_FINAL=binding(actual_path),source=binding(D/'P12.4-paper.tex'),native_pdf=binding(D/'P12.4-paper.pdf'),
    all_current_author_own_bindings_match=True,checked_author_own_records=len(own),checked_input_bodies=input_count,
    whole_controller_native_decoded_objects_equal=True,
    actual_expanded_whole_equal=actual==expanded,
    actual_expanded_fields_equal=[{k:n[k]==m[k] for k in n} for n,m in zip(actual['notes'],expanded['notes'])],
    G331_whole_qualified_grant_object_equal=True,
    supplied_author_programs_ROOT_executed_or_imported=False,
    private_primary_bodies_extracts_pixels_and_private_provider_outputs_not_copied=True,
    ROOT339_not_in_native246_frozen_input=True,independent_review_required=True,
    accepted_papers=93,originals_solved=13,originals_open=29,protected_editor_open_unchanged=True)
write(D/'ROOT-public-draft-status-20261008.json',record)
(D/'ROOT-README.md').write_text('UNREVIEWED15-page P12.4 supporting mathematical paper: arbitrary-field bounded moment construction and actual geometric zero-arity reduced-curve reference measure. The whole original remains OPEN: higher-dimensional actual Cartier comparison and open-set locality are unproved. Entire source/nativePDF and all actual7FINAL notes preserved. ROOT read every actual note field, the entire TeX and complete source/scope/coverage/decision; parallel argument retained without a separate whole-read claim. Current own/input body bindings match. Actual and expanded notes are distinct as recorded. Qualified G331 includes its entire source annotation and ledger; no product grant. Academic primary bodies/extracts/pixels and private provider output stay local. Supplied programs are inert DATA, never ROOT-executed/imported. Compilation/hashes/read receipts are not mathematical acceptance.13solved29OPEN93accepted unchanged; protected P16.4 editor open unchanged.\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(directory=str(D),own_records=len(own),input_bodies=input_count,source_sha256=sha(D/'P12.4-paper.tex'),native_pdf_sha256=sha(D/'P12.4-paper.pdf')),indent=2))
