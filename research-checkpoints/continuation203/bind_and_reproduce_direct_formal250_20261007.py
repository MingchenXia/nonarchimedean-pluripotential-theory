from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-195').iterdir())
D=K/'public-P16.4-continuation250-direct-formal-recognition-and-target-bounds'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round195-settled-inspection-LOCALONLY.json').read_text())
c=x['campaign']; assert c['status']=='completed' and c['error'] is None
k=c['result']; assert k['candidate'] is False and len(k['notes'])==6
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
n=finals[0]; assert n['candidate'] is False
seen=set()
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
    assert set(a['support'])<=seen; seen.add(a['id'])
A=Path(k['workspace']); frozen=json.loads((C/'input.json').read_text()); f=json.loads((C/'freeze.json').read_text())
prompt=json.loads(req['prompt']); assert set(prompt)==set(frozen)|{'workspace'}
assert all(prompt[q]==frozen[q] for q in frozen) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==frozen
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
assignment=frozen['assignment'].splitlines()
units=json.loads((C/'mathematical-data-bindings.json').read_text())
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf']; assert assignment[lo-1:hi]==Path(e['source']).read_text().splitlines()
pb=json.loads((C/'private-primary-packet-bindings.json').read_text()); assert len(pb)==22
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
grants={'O':('public-P16.4-continuation217-general-E1-mixed-operator',179),'D':('public-P16.4-continuation214-completed-closure-descent',176),'N':('public-P16.4-continuation220-norming-reference-target-criterion',182),'T':('public-P16.4-round171-partial-reader',173),'Q':('public-P16.4-continuation222-projective-line-kernel-equation',185),'C':('public-P16.4-continuation218-strict-locality-comparison',181)}
for label,(folder,review) in grants.items():
    p=K/folder
    assert sha(A/f'sources/grant-{label}.tex')==sha(p/'P16.4-paper.tex')
    q=next(p.glob('harmless-reader-clarifications*.json'))
    assert json.loads((A/f'sources/grant-{label}-clarifications.json').read_text())==json.loads(q.read_text())
hashes=json.loads((A/'artifact-hashes.json').read_text()); assert len(hashes)==69
for p,h in hashes.items():assert sha(A/p)==h
saved=json.loads((A/'local-notes.json').read_text()); assert saved!=n
assert saved['candidate'] is False and len(saved['notes'])==6
assert all(a['id']==b['id'] and a['support']==b['support'] for a,b in zip(saved['notes'],n['notes']))
assert len((A/'P16.4-paper.tex').read_text().splitlines())==1320
assert len((A/'P16.4-argument.md').read_text().splitlines())==440
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P16.4-round195-actual-registered-partial-author-result-20261007.json'
native=K/'P16.4-round195-exact-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round195-whole-direct-formal-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n')
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','finite_checks.py'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-hashes.json','grant-bindings.json','packet-verification.json','build-result.json','environment.json','commands.json','finite-checks.json','source-reads.jsonl'):
    shutil.copyfile(A/name,D/'evidence'/('native-'+name))
for name in ('pdflatex-1.stdout.txt','pdflatex-2.stdout.txt','finite-checks.stdout.txt','verify-packet.stdout.txt'):
    shutil.copyfile(A/'logs'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','finite_checks.py'],cwd=D,capture_output=True)
(D/'evidence/root-finite-check.stdout').write_bytes(q.stdout); (D/'evidence/root-finite-check.stderr').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads((D/'finite-checks.json').read_text())
assert checks==json.loads((A/'finite-checks.json').read_text())
assert (checks['irrational_cycle']['accepted_grid_variants'],checks['scaling_dimension_time_pairs'],checks['cech_monomial_base_checks'],len(checks['nilradical_witnesses']),len(checks['raw_curve_checks']))==(34969,168,532,64,3)
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout); (D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode==0
assert sha(D/'P16.4-paper.tex')==sha(A/'P16.4-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
assert not any('undefined' in w or 'Overfull' in w or w.startswith('!') for w in warnings)
pdf=fitz.open(D/'P16.4-paper.pdf'); assert len(pdf)==18
for i in (0,17):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=195,continuation=250,atom='P16.4',candidate=False,
    canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
    exact_decoded_native_task_assignment_notes_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,
    native_artifact_input_raw_sha256=sha(A/'input.json'),retained_workspace_added_to_prompt=True,
    all_six_exact_native_final_notes_equal_canonical_except_kernel_artifact_suffix=True,all_support_ids_valid_earlier_local=True,
    saved_long_notes_differ_from_exact_native_final=True,saved_notes_whole_root_read=False,saved_note_emitter_executed_by_root=False,
    saved_notes_preserved_private_as_unregistered_data=True,
    whole_six_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,
    root_tex_read_lf_ranges=[[1,320],[321,650],[651,950],[951,1320]],source_lf_lines=1320,
    whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,110],[111,220],[221,440]],argument_lf_lines=440,
    whole_quote_free_source_application_ledger_root_read=True,ledger_lf_lines=73,
    whole_finite_check_code_root_read=True,all_native_artifact_hashes_validated=True,native_artifact_hash_count=69,
    all_six_native_grant_bodies_equal_exact_accepted_caller_sources=True,all_six_clarification_objects_match=True,
    all_frozen_mathematical_units_and_lf_bindings_verified=True,frozen_mathematical_units=len(units),all_22_original_primary_bindings_valid=True,
    source_sha256=sha(D/'P16.4-paper.tex'),argument_sha256=sha(D/'P16.4-argument.md'),native_pdf_sha256=sha(A/'P16.4-paper.pdf'),root_pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=18,
    root_local_build_exit_codes=passes,root_local_final_warnings=warnings,own_finite_checks_reproduced=True,
    finite_positive_bend_variants=34969,finite_scaling_pairs=168,finite_cech_cases=532,finite_nilradical_witnesses=64,finite_raw_mass_cases=3,finite_checks_only=True,
    root_exact_public_source_builtin_compiler_success=False,builtin_compiler_not_yet_requested=True,
    root_visual_pages_read=[],pdf_visually_root_read=False,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],
    frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
    caller_grants=['O217','D214','N220','T171','Q222','C218'],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
    scope='Whole18-page partial manuscript: nonnegative flat Cech base change, direct same-original-bundle pure FS recognition on an explicitly existing positive formal pair, compatible horizontal and vertical Cartier implications, signed-reference positive graph approximation preserving irrational cycles, canonical single-Shilov residual-field lemma, all-dimension intrinsic unit-bound equivalence and conditional coercivity, own-output dual attainment, alternative whole genus-zero finite-orbit norming/descent equation. Actual universal model/raw-coefficient/all-genus/higher-dimensional equation applications remain open.',
    protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n'); (D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Direct formal recognition and target bounds: unreviewed whole18-page partial paper\n\n1320 TeX lines,440 argument lines,73 quote-free ledger lines and six exact registered native notes read completely. Six whole accepted caller grants and all clarifications;22 frozen original primary bindings and69 native artifact hashes verified. Saved longer notes differ from exact final and remain private data. Original P16.4 remains open. No independent acceptance yet.\n\nOwn exact finite checks reproduced; two exact-source local builds succeeded. Built-in source compilation and PDF visual reading are separately recorded; rendering alone is not visual inspection. Existing editor preserved.\n')
print(json.dumps(dict(round=195,continuation=250,source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],native_artifact_hash_count=69,local_build_exit_codes=passes,warnings=warnings,binding_sha256=sha(binding),original_closed=False),indent=2))
