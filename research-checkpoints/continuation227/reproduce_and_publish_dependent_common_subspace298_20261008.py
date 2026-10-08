from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, sys

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-221/P05.1-arbitrary-dependent-common-subspace-pages-joint-dual-global-real-regularization-paper'
A=C/'artifacts/codex-C4WoKs'
D=K/'public-P05.1-continuation298-dependent-common-subspace-pages-joint-dual-global-real-regularization'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
source=A/'P05.1-paper.tex'
assert sha(source)=='738b023af49002450cac0a3df5aa2a62fc1a3e21ff750b2aa572cfb141647603'
assert source.read_bytes().count(b'\n')==493
manifest=json.loads((A/'artifact-bindings.json').read_text());assert len(manifest['inputs'])==30 and len(manifest['artifacts'])==82
for e in manifest['inputs']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in manifest['artifacts']:assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert json.loads((A/'input.json').read_text())==json.loads((C/'input.json').read_text())
exact=K/'round221-actual-native-final.json';final=json.loads(exact.read_text());saved=json.loads((A/'native-notes.json').read_text())
assert final['candidate'] is False and saved['candidate'] is False and len(final['notes'])==len(saved['notes'])==7
assert sha(exact)=='5387c68d6124a2f006fd1b4411804d4b1e1c762b59ffc8fd906edc871abb6129'
differences=[]
for f,s in zip(final['notes'],saved['notes']):
    assert f['id']==s['id'] and f['support']==s['support']
    differences.append(dict(id=f['id'],unequal_fields=[k for k in f if f[k]!=s[k]],FINAL_text_sha256=hashlib.sha256(f['text'].encode()).hexdigest(),saved_text_sha256=hashlib.sha256(s['text'].encode()).hexdigest(),saved_presentation_not_controlling=True))
inputdata=json.loads((A/'exact-input.json').read_text())
assert inputdata['dual_grid_denominator']==16 and len(inputdata['determinant_matrices'])==6 and all(len(m)<=3 for m in inputdata['determinant_matrices'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir();E=D/'evidence';E.mkdir();W=E/'ROOT-reproduction';W.mkdir();L=W/'logs';L.mkdir()
for name in ['P05.1-paper.tex','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-source-coverage.md','execution-record.md']:
    shutil.copy2(A/name,D/name)
for name in ['P05.1-paper.tex','check_exact.py','exact-input.json']:shutil.copy2(A/name,W/name)
shutil.copy2(exact,E/'exact-native-final.json')
shutil.copy2(K/'round221-registered-native-result.json',E/'registered-native-result.json')
shutil.copy2(K/'round221-actual-final-extraction-binding-20261008.json',E/'exact-final-extraction-binding.json')
commands=[]
def run(argv,label):
    cp=subprocess.run(argv,cwd=W,capture_output=True,text=True)
    (L/(label+'.stdout.log')).write_text(cp.stdout);(L/(label+'.stderr.log')).write_text(cp.stderr)
    commands.append(dict(argv=argv,exit_code=cp.returncode,stdout=label+'.stdout.log',stderr=label+'.stderr.log'))
    assert cp.returncode==0,label
    return cp
run([sys.executable,'check_exact.py'],'finite-checks')
assert (W/'exact-output.json').read_bytes()==(A/'exact-output.json').read_bytes()
finite=json.loads((W/'exact-output.json').read_text())
assert finite['raw_orders_checked']==44 and finite['joint_model']['feasible_tuples_checked']==26961 and finite['joint_model']['trace_dual_lowering_points']==33
run(['pandoc','-f','latex','-t','markdown','P05.1-paper.tex','-o','argument.md'],'source-conversion')
assert (W/'argument.md').read_bytes()==(A/'argument.md').read_bytes()
diagnostics=[]
for i in [1,2,3]:
    cp=run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex'],f'tex-pass-{i}')
    shutil.copy2(W/'P05.1-paper.log',L/f'tex-pass-{i}.engine.log')
    diagnostics.append([line for line in (cp.stdout+cp.stderr).splitlines() if any(t in line for t in ['Warning','Overfull','Underfull','Undefined','Error'])])
assert not diagnostics[-1]
info=run(['pdfinfo','P05.1-paper.pdf'],'pdfinfo').stdout
assert re.search(r'^Pages:\s+18\s*$',info,re.M)
assert sha(W/'P05.1-paper.tex')==sha(source)
shutil.copy2(W/'P05.1-paper.pdf',D/'P05.1-paper.pdf')
own=E/'own-author221-evidence';own.mkdir();copied=[]
for e in manifest['artifacts']:
    if e.get('publication')=='LOCALONLY' or e['file'].startswith('LOCALONLY/'):continue
    p=own/e['file'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(A/e['file'],p);copied.append(e)
for name in ['artifact-bindings.json','coverage-audit.json','audit-1.stdout.log','audit-1.stderr.log','audit-2.stdout.log','audit-2.stderr.log']:shutil.copy2(A/name,own/name)
write(own/'ROOT-public-copy-binding.json',dict(all82_author_artifacts_verified=True,copied_safe_artifacts=copied,LOCALONLY_original_extracts_not_copied=True,supplied_emitter_audit_build_orchestration_not_executed=True,controlling_exact_FINAL_separate_from_all7_distinct_saved_drafts=True,saved_drafts_whole_ROOT_read_not_claimed=True))
binding=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),original='P05.1',continuation=298,source=str(D/'P05.1-paper.tex'),source_sha256=sha(source),source_LF_lines=493,argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=sha(D/'P05.1-paper.pdf'),pdf_pages=18,exact_FINAL=str(E/'exact-native-final.json'),exact_FINAL_sha256=sha(exact),exact_FINAL_notes=7,exact_FINAL_candidate=False,exact_FINAL_saved_draft_differences=differences,saved_drafts_not_controlling=True,saved_drafts_whole_ROOT_read_not_claimed=True,initial_ROOT_character_diff_metadata_output_truncated=True,repaired_complete_note_field_equality_summary_read=True,no_whole_diff_read_claimed=True,registered_result_only_Artifacts_suffix=True,parent_child_input_semantically_equal=True,author_artifact_bindings_verified=82,math_bindings_verified=26,primary_bindings_verified=4,ROOT_source_whole_read=True,ROOT_ledger_scope_coverage_execution_whole_read=True,ROOT_exact_FINAL_all7_whole_read=True,ROOT_safe_exact_checker_whole_read=True,ROOT_safe_exact_input_whole_read=True,ROOT_safe_checker_copied_and_exec_once=True,ROOT_finite_output_exact=True,finite_raw_orders=44,finite_dependent_model_tuples=26961,finite_trace_points=33,finite_scope_only=True,latex_to_markdown_exact=True,correct_conversion_argv=['pandoc','-f','latex','-t','markdown','P05.1-paper.tex','-o','argument.md'],local_build_exit_codes=[0,0,0],local_build_diagnostics=diagnostics,source_unchanged=True,only_grants=['A224','B225','R230','S262','S272','S282'],all_clarifications_retained=True,native215_historical_INCONCLUSIVE_retained=True,new_S291_S292_and_native218219220_excluded_from_author=True,ordinary_author_draft_not_independent_audit=True,mathematical_acceptance=False,original_closed=False,protected_editor_unchanged_open=True,commands=commands)
write(D/'root-reproduction-binding-20261008.json',binding)
print(json.dumps(dict(directory=str(D),source_sha256=sha(source),argument_sha256=sha(D/'argument.md'),ROOT_pdf_sha256=sha(D/'P05.1-paper.pdf'),ROOT_pdf_pages=18,all7_actual_FINAL_whole_read=True,all7_saved_draft_prose_differs=True,finite_output_exact=True,local_build_exit_codes=[0,0,0],source_conversion_exact=True,new_accepted_paper=False,original_closed=False),indent=2))
