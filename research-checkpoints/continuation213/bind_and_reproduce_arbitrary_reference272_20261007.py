from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-206').iterdir())
D=K/'public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round206-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
k=x['campaign']['result']; assert k['candidate'] is False and len(k['notes'])==5
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
n=finals[0]
assert n==json.loads((K/'round206-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert n['candidate'] is False and len(n['notes'])==5
seen=set()
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
    assert set(a['support'])<=seen;seen.add(a['id'])
A=Path(k['workspace']); inp=json.loads((C/'input.json').read_text());f=json.loads((C/'freeze.json').read_text())
prompt=json.loads(req['prompt']); assert set(prompt)==set(inp)|{'workspace'}
assert all(prompt[q]==inp[q] for q in inp) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==inp
assert json.loads((A/'retained-task.json').read_text())==inp['task']
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
units=json.loads((C/'mathematical-data-bindings.json').read_text()); assert len(units)==22
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf'];assert inp['assignment'].splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
pb=json.loads((C/'private-primary-packet-bindings.json').read_text());assert len(pb)==4
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
provenance=json.loads((A/'evidence/primary-provenance.json').read_text()); assert len(provenance)==4
for a,b in zip(pb,provenance):
    assert all(a[q]==b[q] for q in ('label','format','path','bytes','sha256','literal_url','version'))
manifest=json.loads((A/'evidence/artifact-manifest.json').read_text()); assert len(manifest)==73
for e in manifest:assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
preserved=json.loads((A/'evidence/input-block-manifest.json').read_text());assert len(preserved)==22
pattern=r'BEGIN COMPLETE MATHEMATICAL BODY ([^\n]+)\n(.*?)\nEND COMPLETE MATHEMATICAL BODY \1'
blocks=list(re.finditer(pattern,inp['assignment'],re.S));assert len(blocks)==22
for e,m in zip(preserved,blocks):
    payload=(m.group(2)+'\n').encode()
    assert e['label']==m.group(1) and e['sha256']==hashlib.sha256(payload).hexdigest()
    assert e['bytes']==len(payload) and (A/e['path']).read_bytes()==payload
saved=json.loads((A/'native-notes.json').read_text());assert saved==n
for name,lines in [('P05.2-paper.tex',1016),('argument.md',290),('source-application-ledger.md',47),('material-changes.md',13)]:
    assert len((A/name).read_text().splitlines())==lines
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P05.2-round206-actual-registered-partial-author-result-20261007.json'
native=K/'P05.2-round206-exact-native-model-final-partial-author-20261007.json'
binding=K/'P05.2-round206-whole-arbitrary-reference-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir();(D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','source-application-ledger.md','material-changes.md','check_certificates.py','certificate-input.json','normalize_argument.py'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-manifest.json','artifact-checks.json','input-block-manifest.json','primary-provenance.json','environment.json','execution-record.json','certificate-output.json','markdown-normalization.json'):
    shutil.copyfile(A/'evidence'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','check_certificates.py'],cwd=D,capture_output=True)
(D/'evidence/root-checker.stdout.txt').write_bytes(q.stdout);(D/'evidence/root-checker.stderr.txt').write_bytes(q.stderr)
assert q.returncode==0 and (D/'evidence/certificate-output.json').read_bytes()==(A/'evidence/certificate-output.json').read_bytes()
checks=json.loads((D/'evidence/certificate-output.json').read_text())
assert checks['plane']['raw_reference_mass']==['0','0','0','8']
assert len(checks['plane']['cutoffs'])==4
assert checks['U34']['origin_supports_examined']==385 and checks['U34']['origin_circuits']==14
assert len(checks['U34']['face_cases'])==22 and checks['U34']['saturated_fine_cones']==12
assert checks['U34']['collar_cases']==291 and checks['U34']['scaled_jet_mass']==['1/1024','0','0','0']
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout.txt').write_bytes(q.stdout);(D/f'evidence/root-latex-pass{i}.stderr.txt').write_bytes(q.stderr)
    passes.append(q.returncode);assert q.returncode==0
assert sha(D/'P05.2-paper.tex')==sha(A/'P05.2-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(errors='replace'),re.M)
scratch=D/'evidence/root-markdown-reproduction';scratch.mkdir();(scratch/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.aux','normalize_argument.py'):shutil.copyfile(D/name,scratch/name)
q=subprocess.run(['pandoc','P05.2-paper.tex','--from=latex','--to=markdown+tex_math_dollars','--wrap=none','--standalone','-o','argument.md'],cwd=scratch,capture_output=True)
(D/'evidence/root-pandoc.stdout.txt').write_bytes(q.stdout);(D/'evidence/root-pandoc.stderr.txt').write_bytes(q.stderr);assert q.returncode==0
q=subprocess.run(['python','normalize_argument.py'],cwd=scratch,capture_output=True)
(D/'evidence/root-normalizer.stdout.txt').write_bytes(q.stdout);(D/'evidence/root-normalizer.stderr.txt').write_bytes(q.stderr);assert q.returncode==0
assert (scratch/'argument.md').read_bytes()==(D/'argument.md').read_bytes()
assert (scratch/'evidence/markdown-normalization.json').read_bytes()==(A/'evidence/markdown-normalization.json').read_bytes()
pdf=fitz.open(D/'P05.2-paper.pdf');assert len(pdf)==14
for i in (0,7,8,13):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=206,continuation=272,atom='P05.2',candidate=False,
 canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
 exact_decoded_native_task_assignment_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,
 retained_task_is_whole_actual_task=True,all_five_exact_final_notes_equal_registered_except_kernel_artifact_suffix=True,
 all_local_support_ids_valid=True,saved_notes_equal_exact_final=True,saved_notes_used_as_grants=False,
 all73_native_artifact_hashes_valid=True,all22_frozen_whole_math_units_valid=True,all4_frozen_private_primary_bindings_valid=True,
 all22_actual_delimited_preserved_bodies_valid=True,native_preservation_adds_one_newline_matching_source=True,
 complete_grants=['A224','B225','R230','S262'],all_clarifications_supplied=True,
 whole1016_tex_root_read=True,whole290_argument_separately_root_read=True,whole47_ledger_root_read=True,
 whole13_material_changes_root_read=True,whole_five_exact_final_notes_root_read=True,checker_normalizer_preservation_and_build_scripts_root_read=True,
 native_note_and_input_emitters_executed=False,own_finite_checker_reproduced=True,finite_diagnostics_only=True,
 whole_pandoc_tex_to_markdown_and_normalization_reproduced=True,root_local_build_exit_codes=passes,root_local_warnings=warnings,
 source_sha256=sha(D/'P05.2-paper.tex'),argument_sha256=sha(D/'argument.md'),
 native_pdf_sha256=sha(A/'P05.2-paper.pdf'),root_pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=14,
 rendered_for_later_root_visual_read_pages=[1,8,9,14],root_actual_visual_read_pages=[],whole_pdf_visually_read=False,
 frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
 model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],
 independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
 scope='NEW UNREVIEWED same-actual-arbitrary-real-reference raw mixed completion, global vague and fixed-C weak/BL uniformities, common rational summand jet gluing and reference-independent finite-PA contact obstruction. Higher-dimensional all-obstacle regularization, non-PA contact sufficiency and exhaustive structural reduction remain OPEN.',
 old247196_and255200_FAILs_unchanged=True,third_party_primary_images_published=False,
 no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,indent=2)+'\n');(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Unreviewed 14-page arbitrary-real-reference completion and finite-PA flat-jet contact paper.\n\nWhole1016line source,290line argument,47line application ledger,13line material changes and FIVE exact native final notes ROOT-read. Frozen22wholeunits/four originals verified; own exact finite checker, full TeX-to-Markdown normalization and two local builds reproduced. Actual same-reference rational component and positive convex decomposition have distinct roles. Every new result, including arbitrary-reference jet gluing, requires independent WHOLE proof/source/application review. Weak/BL uniformity is restricted to each fixed relative-bound family. Higher-dimensional all-obstacle regularization, non-PA contact sufficiency and structural classification remain open. No new acceptance or original closure. Protected editor unchanged and open.\n')
print(json.dumps(dict(directory=str(D),binding_sha256=sha(binding),source_sha256=b['source_sha256'],pdf_pages=14,local_build_exit_codes=passes,warnings=warnings,saved_notes_equal_final=True,original_closed=False),indent=2))
