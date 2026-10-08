from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
observations=[]
for number,atom,workspace,continuation in [(242,'P12.3','codex-lnKQHd',336),(244,'P03.1','codex-ytC4Hb',337)]:
    C=next((R/f'campaigns/round-{number}').iterdir());A=C/'artifacts'/workspace
    own=json.loads((A/'own-bindings.json').read_text());checked=[];mismatches=[]
    for e in own['records']:
        p=Path(e['path']);p=p if p.is_absolute() else A/p
        ok=p.is_file() and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
        checked.append(dict(path=str(p),match=ok))
        if not ok:mismatches.append(str(p))
    assert not mismatches,dict(round=number,mismatches=mismatches)
    inp=json.loads((A/'input-bindings.json').read_text());input_checked=[]
    for e in inp['records']:
        choices=[e['path']] if 'path' in e else [e['source'],str(A/e['retained'])]
        for name in choices:
            p=Path(name);p=p if p.is_absolute() else A/p
            assert p.is_file() and p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],str(p)
            input_checked.append(str(p))
    controller=json.loads((C/'input.json').read_text());native=json.loads((A/'input.json').read_text());assert controller==native
    actual_path=K/f'round{number}-actual-native-final.json';actual=json.loads(actual_path.read_text());saved=json.loads((A/'native-notes.json').read_text())
    assert actual['candidate'] is False and saved['candidate'] is False
    assert [(n['id'],n['support']) for n in actual['notes']]==[(n['id'],n['support']) for n in saved['notes']]
    D=K/(f'public-{atom}-continuation{continuation}-'+('geometric-envelope-obstruction-and-positive-sectors-unreviewed' if number==242 else 'full-envelope-category-defect-and-scalar-diagnostic-unreviewed'))
    assert not D.exists();D.mkdir();(D/'evidence').mkdir()
    names=[atom+'-paper.tex',atom+'-paper.pdf','argument.md','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md','native-notes.json','input-bindings.json','own-bindings.json','original-task.json']
    if number==242:names+=['G331-qualified-grant.json','G331-mandatory-source-scope.json','G331-source-application-ledger.md','G331-exact-scope.md']+[f'n{i}.md' for i in range(1,7)]
    for name in names:
        p=A/name
        if p.is_file():shutil.copyfile(p,D/name)
    shutil.copyfile(actual_path,D/'actual-native-FINAL.json')
    evidence_names=['commands.json','reading-record.json','environment.json','build.json','final-audit.json'] if number==242 else ['execution.json','diagnostics.json','build.json','check.json']
    for name in evidence_names:
        p=A/'evidence'/name
        if p.is_file():shutil.copyfile(p,D/'evidence'/name)
    owned_program_names=['audit_inputs.py','repair_initial_delimiters.py','build_delivery.py','final_audit.py'] if number==242 else ['prepare_evidence.py','diagnostics.py','build_artifacts.py','make_notes.py','check_artifacts.py','run_all.py']
    P=D/'inert-author-programs-DATA';P.mkdir()
    for name in owned_program_names:
        p=A/name
        if p.is_file():shutil.copyfile(p,P/name)
    record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=number,atom=atom,continuation=continuation,status='UNREVIEWED scoped mathematical draft; original OPEN',original_closed=False,paper_accepted=False,author_candidate=False,ROOT_whole_actual_FINAL_note_fields_read=True,ROOT_whole_TeX_source_read=True,ROOT_whole_source_scope_coverage_and_decision_read=True,parallel_argument_separately_whole_ROOT_read=False,actual_FINAL_sha256=sha(actual_path),source_tex_sha256=sha(A/(atom+'-paper.tex')),native_pdf_sha256=sha(A/(atom+'-paper.pdf')),all_current_author_own_records_match=True,checked_author_own_records=len(checked),checked_input_body_bindings=len(input_checked),whole_controller_native_decoded_objects_equal=True,actual_saved_expanded_objects_equal=actual==saved,actual_saved_prose_fields_equal=[[n[k]==m[k] for k in ['summary','detailedSummary','text']] for n,m in zip(actual['notes'],saved['notes'])],note_ids_support_candidate_equal=True,supplied_author_programs_ROOT_executed_or_imported=False,private_primary_bodies_and_extracts_and_provider_output_not_published=True,independent_review_round=245 if number==242 else None,counts_unchanged=dict(solved=13,open=29,papers=91))
    write(D/'ROOT-public-draft-status-20261008.json',record)
    (D/'ROOT-README.md').write_text(atom+' standalone draft, UNREVIEWED; original remains OPEN.\n\nThe source and native PDF are unchanged exact completed-worker artifacts. ROOT read all actual FINAL note fields, the entire TeX source, and complete source/scope/coverage/decision ledgers. Own/input bindings and decoded whole controller/native input identity were independently checked. Expanded saved notes and actual FINAL prose are distinct; both are retained. Hashes, compilation and reading are not acceptance. Inert author programs are DATA and ROOT has not executed/imported them. Academic primary bodies/extracts and provider/controller output stay local.13solved29OPEN91accepted unchanged.\n')
    observations.append(dict(directory=str(D),round=number,atom=atom,own_records=len(checked),input_bindings=len(input_checked),source_sha256=record['source_tex_sha256']))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
write(K/'completed-native242-244-ROOT-source-reading-and-current-binding-20261008.json',dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=observations,originals_closed=[],papers_accepted=[],counts_unchanged=dict(solved=13,open=29,papers=91),private_ACTIVE_outputs_read=False,supplied_programs_executed_or_imported=False))
print(json.dumps(observations,indent=2))
