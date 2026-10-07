from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-202').iterdir())
D=K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round202-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
k=x['campaign']['result']; assert k['candidate'] is False and len(k['notes'])==8
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
n=finals[0]; assert n==json.loads((K/'round202-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert n['candidate'] is False and len(n['notes'])==8
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
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
lines=inp['assignment'].splitlines(); units=json.loads((C/'mathematical-data-bindings.json').read_text()); assert len(units)==22
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf']; assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
pb=json.loads((C/'private-primary-packet-bindings.json').read_text()); assert len(pb)==4
for e in pb: assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
manifest=json.loads((A/'evidence/artifact-manifest.json').read_text()); assert len(manifest)==59
for e in manifest: assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
saved=json.loads((A/'notes.json').read_text()); assert saved['candidate'] is False and len(saved['notes'])==8
assert all(a['id']==b['id'] and a['support']==b['support'] for a,b in zip(saved['notes'],n['notes']))
preserved=json.loads((A/'evidence/preserved-bindings.json').read_text()); assert len(preserved)==22
for e in preserved: assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
assert len((A/'P05.2-paper.tex').read_text().splitlines())==1953
assert len((A/'argument.md').read_text().splitlines())==1878
assert len((A/'source-application-ledger.md').read_text().splitlines())==57
assert (A/'raw-completion.tex').read_text() in (A/'P05.2-paper.tex').read_text()
assert (A/'graph-section.tex').read_text() in (A/'P05.2-paper.tex').read_text()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P05.2-round202-actual-registered-partial-author-result-20261007.json'
native=K/'P05.2-round202-exact-native-model-final-partial-author-20261007.json'
binding=K/'P05.2-round202-whole-graph-contact-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n'); native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','raw-completion.tex','graph-section.tex','source-application-ledger.md','material-changes.md','check_certificates.py','certificate-input.json'):
    shutil.copyfile(A/name,D/name)
for name in ('execution-commands.md',):shutil.copyfile(A/name,D/'evidence'/('native-'+name))
for name in ('artifact-manifest.json','build-bindings.json','preserved-bindings.json','primary-provenance.json','environment.json','certificate-output.json','certificate-output.log','check-failure-1.log','check-stderr.log'):
    shutil.copyfile(A/'evidence'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','check_certificates.py'],cwd=D,capture_output=True)
(D/'evidence/root-checker.stdout.txt').write_bytes(q.stdout); (D/'evidence/root-checker.stderr.txt').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads((D/'evidence/certificate-output.json').read_text()); assert checks==json.loads((A/'evidence/certificate-output.json').read_text())
assert checks['limit_moments']==dict(y2='28',z2='1/5',rawtotal=24,contact='-3',literal_gap='3/64')
assert checks['PA']['masses']==[12,6,6] and checks['PA']['raw_contact']=='-3'
assert checks['dyadic_error_cases']==1143 and len(checks['literal_weak_counterexample'])==7 and len(checks['real_BL_counterexample'])==6
assert all(e['evaluation_difference']=='1' for e in checks['real_BL_counterexample'])
assert checks['graph_sector']['irrational_reference']['radius_1/4_contact']=='-1/2'
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout.txt').write_bytes(q.stdout); (D/f'evidence/root-latex-pass{i}.stderr.txt').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode==0
assert sha(D/'P05.2-paper.tex')==sha(A/'P05.2-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(errors='replace'),re.M); assert not warnings
q=subprocess.run(['pandoc','P05.2-paper.tex','-f','latex','-t','markdown+tex_math_dollars','--standalone'],cwd=D,capture_output=True,check=True)
assert q.stdout==(D/'argument.md').read_bytes()
pdf=fitz.open(D/'P05.2-paper.pdf'); assert len(pdf)==27
for i in (0,13,20,23,26):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=202,continuation=262,atom='P05.2',candidate=False,
 canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
 exact_decoded_native_task_assignment_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,
 native_artifact_input_sha256=sha(A/'input.json'),retained_workspace_added_to_prompt=True,
 all_eight_exact_native_final_notes_equal_canonical_except_kernel_artifact_suffix=True,all_support_ids_valid_earlier_local=True,
 saved_notes_equal_exact_native_final=saved==n,saved_notes_used_as_grants=False,saved_notes_whole_root_read=False,
 all59_native_artifact_manifest_entries_valid=True,native_artifact_manifest_sha256=sha(A/'evidence/artifact-manifest.json'),
 all22_frozen_whole_mathematical_units_and_lf_bindings_valid=True,all4_private_primary_bindings_valid=True,
 all22_preserved_actual_delimited_bodies_valid=True,complete_caller_grants=['A224','B225','R230'],all_unchanged_clarifications_supplied=True,
 whole1953_tex_root_read=True,whole1878_native_argument_separately_root_read=True,whole57_ledger_root_read=True,
 whole_eight_exact_canonical_final_notes_root_read=True,whole_material_change_record_root_read=True,
 checker_and_build_scripts_root_read=True,native_generation_scripts_executed=False,own_checker_reproduced=True,
 whole_markdown_exact_pandoc_conversion_reproduced=True,root_local_build_exit_codes=passes,root_local_warnings=warnings,
 source_sha256=sha(D/'P05.2-paper.tex'),source_bytes=(D/'P05.2-paper.tex').stat().st_size,
 argument_sha256=sha(D/'argument.md'),argument_bytes=(D/'argument.md').stat().st_size,
 native_pdf_sha256=sha(A/'P05.2-paper.pdf'),root_pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=27,
 pages_rendered_for_later_root_visual_read=[1,14,21,24,27],root_actual_visual_read_pages=[],whole_pdf_visually_read=False,
 model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],
 frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
 independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
 scope='Material repair of false global weak/BL uniformity: ordinary weak C_b continuity, global vague uniformity, weak/BL uniformity only on each fixed relative-bound family; all completed tuples have exact common K_C. Entire finite PA/raw mixed completion/coupled nonPA examples reconstructed. New all-continuous real graph regularization and genuine Stieltjes/primitive raw operator for arbitrary actual real coefficients on rational geometry; all-continuous graph contact iff every local relation cone is the actual positive weight ray. Full higher-dimensional all-obstacle/nonPA/arbitrary-irrational-reference classification remains open.',
 finite_certificates_only_not_continuum_proof=True,old_whole255_independent200_remains_FAIL=True,no_failed_result_granted=True,
 third_party_primary_images_published=False,root_new_BMPS_or_BBGS_pixels_read=False,
 no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'README.md').write_text('Unreviewed27-page corrected raw uniformities and all-continuous graph contact paper\n\nWhole1953-line source,1878-line Markdown argument,57-line quote-free ledger, material-change record and eight exact native final notes ROOT-read. All59 native artifact hashes,22 whole frozen data units and4 private originals verified. Native longer saved notes were not used as grants. Exact copied checker output and whole Pandoc conversion reproduced; two local builds succeeded without warnings. The source remains unchanged; no emitter rerun. Actual PDF visual read and builtin compile result are separate records. Old255/200 remains FAIL. Three whole A/B/R grants/all clarifications only. New mathematical results await whole independent review; original P05.2 remains open. Protected current editor remains open and unchanged.\n')
print(json.dumps(dict(directory=str(D),binding_sha256=sha(binding),source_sha256=sha(D/'P05.2-paper.tex'),pdf_pages=27,checker_reproduced=True,local_build_exit_codes=passes,local_warnings=warnings,saved_notes_equal_final=saved==n,new_accepted_paper=False,original_closed=False),indent=2))
