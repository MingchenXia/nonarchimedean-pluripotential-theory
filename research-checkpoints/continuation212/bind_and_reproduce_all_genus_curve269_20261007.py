from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-205').iterdir())
D=K/'public-P16.4-continuation269-all-genus-original-field-curve-equation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round205-settled-inspection-LOCALONLY.json').read_text())
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
assert n==json.loads((K/'round205-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert n['candidate'] is False and len(n['notes'])==5
seen=set()
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
    assert set(a['support'])<=seen;seen.add(a['id'])
A=Path(k['workspace']);inp=json.loads((C/'input.json').read_text());f=json.loads((C/'freeze.json').read_text())
prompt=json.loads(req['prompt']);assert set(prompt)==set(inp)|{'workspace'}
assert all(prompt[q]==inp[q] for q in inp) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==inp
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
units=json.loads((C/'mathematical-data-bindings.json').read_text());assert len(units)==46
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf'];assert inp['assignment'].splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
pb=json.loads((C/'private-primary-packet-bindings.json').read_text());assert len(pb)==62
assert json.loads((A/'frozen-manifest.json').read_text())==pb
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
manifest=json.loads((A/'artifact-manifest.json').read_text());assert len(manifest)==26
for name,e in manifest.items():assert sha(A/name)==e['sha256'] and (A/name).stat().st_size==e['bytes']
preserved=json.loads((A/'supplied-index.json').read_text());assert len(preserved)==46
pattern=r'BEGIN COMPLETE MATHEMATICAL BODY ([^\n]+)\n(.*?)\nEND COMPLETE MATHEMATICAL BODY \1'
blocks=list(re.finditer(pattern,inp['assignment'],re.S));assert len(blocks)==46
for e,m in zip(preserved,blocks):
    assert e['label']==m.group(1) and e['sha256']==hashlib.sha256(m.group(2).encode()).hexdigest()
    assert e['bytes']==len(m.group(2).encode()) and (A/e['file']).read_bytes()==m.group(2).encode()
saved=json.loads((A/'native-notes.json').read_text())
assert saved['candidate'] is False and len(saved['notes'])==5
assert len((A/'P16.4-paper.tex').read_text().splitlines())==1105
assert len((A/'P16.4-argument.md').read_text().splitlines())==399
assert len((A/'source-application-ledger.md').read_text().splitlines())==47
assert len((A/'scope-and-gaps.md').read_text().splitlines())==9
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P16.4-round205-actual-registered-partial-author-result-20261007.json'
native=K/'P16.4-round205-exact-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round205-whole-all-genus-curve-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir();(D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','scope-and-gaps.md','finite_checks.py','finite-inputs.json'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-manifest.json','finite-output.json','finite-checks.log','environment.json','reproduce.sh','supplied-index.json','frozen-manifest.json'):
    shutil.copyfile(A/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','finite_checks.py'],cwd=D,capture_output=True)
(D/'evidence/root-checker.stdout.txt').write_bytes(q.stdout);(D/'evidence/root-checker.stderr.txt').write_bytes(q.stderr)
assert q.returncode==0
assert (D/'finite-output.json').read_bytes()==(A/'finite-output.json').read_bytes()
assert (D/'finite-inputs.json').read_bytes()==(A/'finite-inputs.json').read_bytes()
checks=json.loads((D/'finite-output.json').read_text())
assert checks['positive_bend_cases']==450 and checks['energy_cases']==150
assert checks['tree_kernel_pairs']==36 and checks['trace_cancellation'] is True
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout.txt').write_bytes(q.stdout);(D/f'evidence/root-latex-pass{i}.stderr.txt').write_bytes(q.stderr)
    passes.append(q.returncode);assert q.returncode==0
assert sha(D/'P16.4-paper.tex')==sha(A/'P16.4-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
q=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash','P16.4-argument.md','--standalone','--number-sections','-t','latex'],cwd=D,capture_output=True,check=True)
assert q.stdout==(D/'P16.4-paper.tex').read_bytes()
pdf=fitz.open(D/'P16.4-paper.pdf');assert len(pdf)==15
for i in (0,5,8,11,14):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=205,continuation=269,atom='P16.4',candidate=False,
 canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
 exact_decoded_native_task_assignment_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,
 all_five_exact_final_notes_equal_registered_except_kernel_artifact_suffix=True,all_local_support_ids_valid=True,
 saved_notes_equal_exact_final=saved==n,saved_notes_used_as_grants=False,saved_notes_whole_root_read=False,
 all26_native_artifact_hashes_valid=True,all46_frozen_whole_math_units_valid=True,all62_frozen_private_primary_bindings_valid=True,
 all46_actual_delimited_preserved_bodies_valid=True,
 first_root_attempt_pre_mutation_failed_on_different_native_index_schema=True,
 native_index_uses_label_and_exact_body_without_added_newline=True,
 complete_grants=['O217','D214','N220','T171','Q222','C218','G227','M257'],all_clarifications_supplied=True,
 whole1105_tex_root_read=True,whole399_argument_separately_root_read=True,whole47_ledger_root_read=True,
 whole9_scope_root_read=True,whole_five_exact_final_notes_root_read=True,checker_and_build_scripts_root_read=True,
 native_note_emitters_executed=False,own_finite_checker_reproduced=True,finite_diagnostics_only=True,
 whole_pandoc_markdown_to_tex_conversion_reproduced=True,root_local_build_exit_codes=passes,root_local_warnings=warnings,
 source_sha256=sha(D/'P16.4-paper.tex'),argument_sha256=sha(D/'P16.4-argument.md'),
 native_pdf_sha256=sha(A/'P16.4-paper.pdf'),root_pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=15,
 rendered_for_later_root_visual_read_pages=[1,6,9,12,15],root_actual_visual_read_pages=[],whole_pdf_visually_read=False,
 frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
 model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],
 independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
 scope='NEW UNREVIEWED all-genus curve actual original-bundle positive models/unconditional FS recognition, genuine raw curvature, arbitrary-support intrinsic-target inverse, EVERYsolution EVERYpoint uniqueness and original-field descent. General n>=2 original inverse/attainment/everypoint remains OPEN. Native n4 uses O positive-reference-atom integrability, not changed-reference M moment.',
 new_ROOT273_274_applications_not_frozen_into_round205=True,old250_and198_FAIL_unchanged=True,
 third_party_primary_images_published=False,no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,indent=2)+'\n');(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Unreviewed 15-page all-genus original-field curve equation paper.\n\nWhole1105line source,399line argument,47line application ledger,9line scope and FIVE exact native final notes ROOT-read. Frozen46wholeunits/62originals and exact conversion verified; own finite checker and two local builds reproduced. New original-bundle formal FS recognition, true raw coefficients, arbitrary-support target inverse and EVERYsolution EVERYpoint field descent require independent WHOLE mathematical/source/application review. General n>=2 original remains open. O integrability proves the finite E1 anchor; M reference covariance transfers intrinsic finiteness only. ROOT273/274 are newer unreviewed future data and do not repair or replace submitted proofs. No new acceptance or original closure. Protected editor unchanged and open.\n')
print(json.dumps(dict(directory=str(D),binding_sha256=sha(binding),source_sha256=b['source_sha256'],pdf_pages=15,local_build_exit_codes=passes,warnings=warnings,saved_notes_equal_final=saved==n,original_closed=False),indent=2))
