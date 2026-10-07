from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-197').iterdir())
D=K/'public-P05.2-continuation255-coupled-nonPA-and-regularizable-raw-completion'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round197-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
k=x['campaign']['result']; assert k['candidate'] is False and len(k['notes'])==7
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    z=json.loads(line)
    if z.get('type')=='item.completed' and z.get('item',{}).get('type')=='agent_message':
        try:n=json.loads(z['item']['text'])
        except (ValueError,TypeError):continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}:finals.append(n)
assert len(finals)==1
n=finals[0]; assert n['candidate'] is False and len(n['notes'])==7
seen=set()
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
    assert set(a['support'])<=seen; seen.add(a['id'])
A=Path(k['workspace']); inp=json.loads((C/'input.json').read_text()); f=json.loads((C/'freeze.json').read_text())
prompt=json.loads(req['prompt']); assert set(prompt)==set(inp)|{'workspace'}
assert all(prompt[q]==inp[q] for q in inp) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==inp
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
lines=inp['assignment'].splitlines(); units=json.loads((C/'mathematical-data-bindings.json').read_text())
assert len(units)==14
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf']; assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
pb=json.loads((C/'private-primary-packet-bindings.json').read_text()); assert len(pb)==4
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
manifest=json.loads((A/'artifact-manifest.json').read_text()); assert len(manifest['files'])==61
for e in manifest['files']: assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
saved=json.loads((A/'notes.json').read_text()); assert saved['candidate'] is False
assert len(saved['notes'])==7 and all(a['id']==b['id'] and a['support']==b['support'] for a,b in zip(saved['notes'],n['notes']))
for e in json.loads((A/'preserved/manifest.json').read_text()): assert sha(A/e['file'])==e['sha256']
assert len((A/'P05.2-paper.tex').read_text().splitlines())==1367
assert len((A/'argument.md').read_text().splitlines())==1371
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P05.2-round197-actual-registered-partial-author-result-20261007.json'
native=K/'P05.2-round197-exact-native-model-final-partial-author-20261007.json'
binding=K/'P05.2-round197-whole-coupled-nonPA-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n'); native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','source-application-ledger.md','material-changes.md','check_certificates.py','certificate-input.json'):shutil.copyfile(A/name,D/name)
for name in ('artifact-manifest.json','execution-commands.md'):shutil.copyfile(A/name,D/'evidence'/('native-'+name))
for name in ('primary-provenance.json','build-validation.json','environment.json','certificate-output.json','checker-final.stdout.txt','checker-final.stderr.txt','checker-initial-failure.txt','checker-second-failure.txt','latex-initial-failure.log'):
    shutil.copyfile(A/'evidence'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','check_certificates.py'],cwd=D,capture_output=True)
(D/'evidence/root-checker.stdout.txt').write_bytes(q.stdout); (D/'evidence/root-checker.stderr.txt').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads((D/'evidence/certificate-output.json').read_text())
assert checks==json.loads((A/'evidence/certificate-output.json').read_text())
assert checks['status']=='all finite assertions passed' and checks['distinct_grid_points']==3321 and checks['interior_radial_chord_checks']==90
assert checks['quadratic_chord_error_cases']==1143 and checks['coupled_contact_integral']=='-3' and checks['literal_nonPA_gap']=='3/64'
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout.txt').write_bytes(q.stdout); (D/f'evidence/root-latex-pass{i}.stderr.txt').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode==0
assert sha(D/'P05.2-paper.tex')==sha(A/'P05.2-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(errors='replace'),re.M)
assert not warnings
pdf=fitz.open(D/'P05.2-paper.pdf'); assert len(pdf)==20
for i in (0,13,15,19):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=197,continuation=255,atom='P05.2',candidate=False,canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),exact_decoded_native_task_assignment_notes_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,native_artifact_input_sha256=sha(A/'input.json'),retained_workspace_added_to_prompt=True,all_seven_exact_native_final_notes_equal_canonical_except_kernel_artifact_suffix=True,all_support_ids_valid_earlier_local=True,saved_notes_equal_exact_native_final=saved==n,saved_notes_used_as_grants=False,all61_native_artifact_manifest_entries_valid=True,native_artifact_manifest_sha256=sha(A/'artifact-manifest.json'),all14_frozen_whole_mathematical_units_and_lf_bindings_valid=True,all4_private_primary_bindings_valid=True,complete_caller_grants=['A224','B225','R230'],all_unchanged_clarifications_supplied=True,whole1367_tex_root_read=True,whole1371_native_argument_separately_root_read=True,whole50_ledger_root_read=True,whole_seven_canonical_final_notes_root_read=True,whole_material_change_record_root_read=True,checker_and_build_scripts_root_read=True,native_generation_scripts_executed=False,own_checker_reproduced=True,root_local_build_exit_codes=passes,root_local_warnings=warnings,source_sha256=sha(D/'P05.2-paper.tex'),source_bytes=(D/'P05.2-paper.tex').stat().st_size,argument_sha256=sha(D/'argument.md'),argument_bytes=(D/'argument.md').stat().st_size,native_pdf_sha256=sha(A/'P05.2-paper.pdf'),root_pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=20,pages_rendered_for_later_root_visual_read=[1,14,16,20],root_actual_visual_read_pages=[],whole_pdf_visually_read=False,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],worker_requested_model_not_exposed_claim_scope='Worker did not independently select a route; ROOT verifies the actual native call request model61 and reasoning xhigh. No model switch occurred.',independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,scope='Explicit material PC-floor repair; genuinely coupled PA masses12,6,6/reference24/contact-3; rational-reference real-category local-jet realization and finite-PA geometric criterion; genuine sequence-independent raw mixed completion on the actual rational-reference regularizable domain; explicit non-PA real-regularizable segment/parabola measure and contact-3 with literal approximation gap3/64; reconstructed literal noncompact regularity antecedent obstruction. Full real-reference all-obstacle/non-PA contact classification remains open.',third_party_primary_images_published=False,root_new_BMPS_or_BBGS_pixels_read=False,no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'README.md').write_text('Unreviewed twenty-page coupled non-PA and raw-completion paper\n\nWhole1367-line TeX,1371-line argument,50-line quote-free ledger,material-change record and seven exact canonical final notes ROOT-read. All61 native artifact hashes,14 frozen mathematical units and4 private original primary bindings valid. Failed247/196 remain failed; three whole caller grants/all clarifications only. New mathematical results have no independent acceptance yet. Original P05.2 remains open.\n\nCopied exact-source checker output reproduced, and two local builds succeeded with no warnings. Source remains unchanged. Native generation emitters were not rerun. Actual ROOT PDF visual pages and built-in compilation are separately recorded; rendering is not reading. Verify using python check_certificates.py and pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.2-paper.tex twice in this directory. Protected current editor remains open and unchanged.\n')
print(json.dumps(dict(directory=str(D),binding_sha256=sha(binding),source_sha256=sha(D/'P05.2-paper.tex'),pdf_pages=20,checker_reproduced=True,local_build_exit_codes=passes,local_warnings=warnings,saved_notes_equal_final=saved==n,new_accepted_paper=False,original_closed=False),indent=2))
