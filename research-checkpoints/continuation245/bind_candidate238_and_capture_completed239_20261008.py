from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'
C = next((R / 'campaigns/round-238').iterdir()); A = C / 'artifacts/codex-2eREYM'
D = K / 'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
B = K / 'round238-whole-candidate-ROOT-reading-and-independent-review-binding-20261008.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, x): Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

assert not D.exists() and not B.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:
    assert sha(C / name) == f[key]
assert json.loads((C / 'input.json').read_text())['notes'] == []
own = json.loads((A / 'reports/own-hashes.json').read_text())['artifacts']
assert len(own) == 77
for e in own:
    p = (A / e['path']).resolve()
    assert p.is_relative_to(A.resolve()) and p.stat().st_size == e['bytes'] and sha(p) == e['sha256']
frozen = []
for name in ('mathematical-packet-bindings.json','private-primary-packet-bindings.json'):
    for e in json.loads((C / name).read_text()):
        assert Path(e['path']).stat().st_size == e['bytes'] and sha(e['path']) == e['sha256']
        frozen.append(e)
assert len(frozen) == 36
ih = json.loads((A / 'reports/input-hashes.json').read_text()); assert len(ih) == 39
for e in ih:
    assert sha(e['path']) == e['sha256']
    if 'bytes' in e: assert Path(e['path']).stat().st_size == e['bytes']
actual_path = K / 'round238-actual-native-final.json'
actual = json.loads(actual_path.read_text()); saved = json.loads((A / 'native-notes.json').read_text())
assert actual['candidate'] is True and saved['candidate'] is True and len(actual['notes']) == len(saved['notes']) == 12
known = set(); diff = []
for n, m in zip(actual['notes'], saved['notes']):
    assert n['id'] == m['id'] and n['support'] == m['support'] and n['id'] not in known
    assert all(s in known for s in n['support']); known.add(n['id'])
    diff.append(dict(id=n['id'],equal_fields=[k for k in n if n[k] == m.get(k)],different_fields=[k for k in n if n[k] != m.get(k)],actual_text_bytes=len(n['text'].encode()),saved_text_bytes=len(m['text'].encode())))
assert (A / 'P12.2-paper.tex').read_bytes().count(b'\n') == 496
pdfinfo = subprocess.run(['pdfinfo',str(A / 'P12.2-paper.pdf')],capture_output=True,text=True,check=True).stdout
pages = next(int(line.split(':',1)[1].strip()) for line in pdfinfo.splitlines() if line.startswith('Pages:'))
assert pages == 23
now = datetime.now(timezone.utc).isoformat()
write(B, dict(recorded_utc=now,round=238,role_status='completed',author_candidate=True,actual_FINAL_path=str(actual_path),actual_FINAL_sha256=sha(actual_path),whole_twelve_actual_notes_all_fields_ROOT_read=True,actual_note_display_groups=['n7,n8','n1,n2,n3','n4,n5,n6','n9,n10,n11,n12'],whole_authoritative_paper_ROOT_read=True,paper_display_ranges=['1-100','101-200','201-300','301-400','401-520'],paper_LF_lines=496,source_sha256=sha(A / 'P12.2-paper.tex'),pdf_sha256=sha(A / 'P12.2-paper.pdf'),pdf_pages=23,whole_source_ledger_exact_scope_coverage_decision_ROOT_read=True,whole_original_statement_family_dossier_completionCriteria_ROOT_read=True,expanded_argument_and_saved_native_notes_separately_whole_ROOT_read_not_claimed=True,own_artifact_hashes_independently_verified=77,frozen_math_and_primary_hashes_independently_verified=36,input_hash_records_independently_verified=39,all_frozen_control_file_hashes_verified=True,saved_and_actual_note_ids_supports_and_candidate_match=True,saved_and_actual_prose_differs=diff,saved_note_prose_not_substituted_for_actual_FINAL=True,supplied_programs_not_executed_or_imported=True,source_recursive_historical_proofs_not_claimed=True,original_scope_and_independent_whole_review_pending=True,source_or_math_acceptance=False,new_accepted_paper=False,original_closed=False))
D.mkdir(); E = D / 'evidence'; E.mkdir()
for name in ('P12.2-paper.tex','P12.2-paper.pdf','argument.md','native-notes.json','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-decision.md','note-index.json'):
    shutil.copyfile(A / name,D / name)
for name in ('own-hashes.json','input-hashes.json','build-report.json','build-attempt-1.json','build-attempt-2.json','build-attempt-3.json','build-attempt-4.json','final-audit.json','final-audit-initial.json','final-audit-attempt-2.json','final-audit-attempt-3.json','execution-history.md','environment.json','exact-checks.json'):
    p = A / 'reports' / name
    if p.is_file(): shutil.copyfile(p,E / name)
for p in (B,actual_path): shutil.copyfile(p,E / p.name)
write(D / 'ROOT-public-candidate-status-20261008.json',dict(recorded_utc=now,continuation=331,native_round=238,author_candidate=True,status='UNREVIEWED whole-original P12.2 solution candidate; original remains OPEN',whole_ROOT_paper_and_twelve_actual_notes_read=True,own_hashes_verified=77,frozen_math_primary_hashes_verified=36,input_hash_records_verified=39,saved_actual_ids_supports_match_but_prose_differs=True,author_23_page_source_PDF_unchanged=True,author_build_not_ROOT_execution=True,built_in_compiler_status='not yet requested',external_source_bodies_images_and_excerpts_excluded=True,protected_P16_editor_unchanged_open=True,new_accepted_paper=False,original_closed=False))
(D / 'ROOT-README.md').write_text('UNREVIEWED 23-page whole-original P12.2 candidate, native238 / continuation331.\n\n11/42 originals solved;31 OPEN;89 accepted papers. Candidate TRUE is an author claim. Whole496-line paper, all12 actual FINAL notes, source ledger, exact scope, proof coverage, scope decision and whole original family dossier ROOT-read. Independent77 own,36 frozen and39 reported input hashes match. Saved expanded notes share actual IDs/supports/candidate, but prose differs; exact actual FINAL is preserved separately. Parallel argument/saved expanded note files are supplied as data, without a separate whole ROOT reading claim.\n\nConstruction: independent curve-nef actual effective Cartier model core on primary blowups, nontrivial uniform comparison to the ideal cone, full smooth BFJ specialization at exact characteristic-zero hypotheses, all-support intrinsic gauge/completion/conductor and finite-injection descent including mixedzero and partialbottom. The full nonreduced-fibre Keeler application uses the corrected version and entire erratum. No arbitrary-model cofinality, CLD/classical radial identity, positive-characteristic singular resolution, envelopes, products, energy, or P12.6 operator theory is asserted. Independent whole-original mathematical/source/scope review is pending. All external source bodies, extracted source excerpts and primary images remain LOCALONLY. Compiler/hash/native execution success does not establish mathematical acceptance. Protected P16.4 editor remains open unchanged.\n')

C239 = next((R / 'campaigns/round-239').iterdir())
out = K / 'round239-completed-inspection-LOCALONLY.json'; ap = K / 'round239-actual-native-final.json'
assert not out.exists() and not ap.exists()
status = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C239 / 'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert status['status'] == 'completed' and status['calls']['unsettled'] == 0
with out.open('xb') as stream:
    subprocess.run(['bash','scripts/cloud.sh','xean','--records','inspect',str(C239 / 'work.sqlite')],cwd='/workspace/xean',stdout=stream,stderr=subprocess.PIPE,check=True)
j = json.loads(out.read_text()); assert j['campaign']['status'] == 'completed' and not j['campaign']['error']
records = [r for r in j['records'] if r['kind'] == 'xean.call.settled']; assert len(records) == 1
m = records[0]['data']['message']; assert m['exitCode'] == 0 and not m['failed'] and not m['isCanceled']
messages = []
for line in m['stdout'].splitlines():
    try: v = json.loads(line)
    except ValueError: continue
    if v.get('type') == 'item.completed' and v.get('item',{}).get('type') == 'agent_message': messages.append(v['item']['text'])
exact = messages[-1].encode(); x = json.loads(exact); assert set(x) == {'notes','candidate'}
known = {n['id'] for n in json.loads((C239 / 'input.json').read_text())['notes']}
for n in x['notes']:
    assert n['id'] not in known and all(s in known for s in n['support']); known.add(n['id'])
ap.write_bytes(exact)
for name in ('active-work.json','checklist-current.json'):
    p = R / name; z = json.loads(p.read_text())
    assert len(z['fully_solved_original_atoms']) == 11 and z['remaining_open_original_atoms'] == 31 and z['historical_reviewed_scoped_papers'] == 89
    z.update(updated_utc=now,current_active_batch=[],P12_2_candidate238=dict(status='completed author whole-original candidate; independent review pending',public_directory=str(D),ROOT_reading_binding=str(B),candidate=True,original_closed=False),P05_2_original_contact_certificate239=dict(round=239,directory=str(C239),status='completed; actual FINAL captured, whole ROOT reading pending',candidate=x['candidate'],actual_FINAL=str(ap),actual_FINAL_sha256=sha(ap),original_closed=False),next_work='Independently review entire original P12.2 candidate238 and read completed P05.2 candidate239. Keep at most2 native campaigns and regular verified GitHub checkpoints.11 solved31 OPEN89 accepted.')
    write(p,z)
print(json.dumps(dict(public_candidate=str(D),reading_binding=str(B),paper_sha256=sha(D / 'P12.2-paper.tex'),pdf_sha256=sha(D / 'P12.2-paper.pdf'),round239_workspace=j['campaign']['result']['workspace'],round239_actual_FINAL=str(ap),round239_actual_FINAL_bytes=len(exact),round239_actual_FINAL_sha256=sha(ap),round239_candidate=x['candidate'],round239_notes=[dict(id=n['id'],summary=n['summary'],support=n['support'],text_bytes=len(n['text'].encode())) for n in x['notes']],round239_intermediate_messages_excluded=len(messages)-1),ensure_ascii=False,indent=2))
