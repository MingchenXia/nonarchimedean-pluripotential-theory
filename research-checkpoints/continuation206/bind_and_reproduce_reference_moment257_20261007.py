from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-199').iterdir())
D=K/'public-P16.4-continuation257-general-reference-moment-and-intrinsic-targets'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round199-settled-inspection-LOCALONLY.json').read_text())
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
pb=json.loads((C/'private-primary-packet-bindings.json').read_text()); assert len(pb)==26
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
extracts=json.loads((A/'data-bindings.json').read_text()); assert len(extracts)==27
bylabel={e['label']:e for e in units}
for e in extracts:
    original=bylabel[e['label']]
    assert sha(A/e['path'])==e['sha256']==original['sha256']
    assert (A/e['path']).read_bytes()==Path(original['source']).read_bytes()
assert sum(e['grant'] for e in extracts)==16
hashes=json.loads((A/'artifact-hashes.json').read_text()); assert len(hashes)==64
for p,h in hashes.items():assert sha(A/p)==h
saved=json.loads((A/'local-notes.json').read_text()); assert saved!=n
assert saved['candidate'] is False and len(saved['notes'])==6
assert all(a['id']==b['id'] and a['support']==b['support'] for a,b in zip(saved['notes'],n['notes']))
assert len((A/'P16.4-paper.tex').read_text().splitlines())==982
assert len((A/'P16.4-argument.md').read_text().splitlines())==370
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P16.4-round199-actual-registered-partial-author-result-20261007.json'
native=K/'P16.4-round199-exact-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round199-whole-reference-moment-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n')
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','finite_checks.py'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-hashes.json','data-bindings.json','verification.json','packet-verification.json','build-result.json','environment.json','commands.json','finite-checks.json','source-reads.jsonl'):
    shutil.copyfile(A/name,D/'evidence'/('native-'+name))
for name in ('pdflatex-1.log','pdflatex-2.log','finite-checks.log','build-summary.log'):
    shutil.copyfile(A/'logs'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','finite_checks.py'],cwd=D,capture_output=True)
(D/'evidence/root-finite-check.stdout').write_bytes(q.stdout); (D/'evidence/root-finite-check.stderr').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads((D/'finite-checks.json').read_text())
assert checks==json.loads((A/'finite-checks.json').read_text())
assert (checks['bernstein_time_pairs'],checks['scaling_pairs'],checks['laurent_residue_decompositions'],checks['koszul_diagonal_terms'],checks['cycle_path_tests'],checks['weighted_maximum_path_tests'])==(492,240,2904,552,1296,11664)
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout); (D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode==0
assert sha(D/'P16.4-paper.tex')==sha(A/'P16.4-paper.tex')
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
assert not any('undefined' in w or 'Overfull' in w or w.startswith('!') for w in warnings)
pdf=fitz.open(D/'P16.4-paper.pdf'); assert len(pdf)==14
for i in (0,13):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=199,continuation=257,atom='P16.4',candidate=False,
    canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
    exact_decoded_native_task_assignment_notes_equal_frozen_input=True,native_artifact_input_equal_frozen_input=True,
    native_artifact_input_raw_sha256=sha(A/'input.json'),retained_workspace_added_to_prompt=True,
    all_six_exact_native_final_notes_equal_canonical_except_kernel_artifact_suffix=True,all_support_ids_valid_earlier_local=True,
    saved_long_notes_differ_from_exact_native_final=True,saved_notes_whole_root_read=False,saved_note_emitter_executed_by_root=False,
    saved_notes_preserved_private_as_unregistered_data=True,
    whole_six_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,
    root_tex_read_lf_ranges=[[1,330],[331,650],[651,982]],source_lf_lines=982,
    whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,190],[191,370],[252,292]],argument_lf_lines=370,
    whole_quote_free_source_application_ledger_root_read=True,ledger_lf_lines=195,
    whole_finite_check_code_root_read=True,all_native_artifact_hashes_validated=True,native_artifact_hash_count=64,
    all_seven_grant_bodies_equal_exact_accepted_caller_sources=True,all_seven_unchanged_clarification_objects_match=True,all27_native_input_extracts_exact=True,
    all_frozen_mathematical_units_and_lf_bindings_verified=True,frozen_mathematical_units=len(units),all_26_original_primary_bindings_valid=True,
    source_sha256=sha(D/'P16.4-paper.tex'),argument_sha256=sha(D/'P16.4-argument.md'),native_pdf_sha256=sha(A/'P16.4-paper.pdf'),root_pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=14,
    root_local_build_exit_codes=passes,root_local_final_warnings=warnings,own_finite_checks_reproduced=True,
    finite_Bernstein_time_pairs=492,finite_scaling_pairs=240,finite_Laurent_decompositions=2904,finite_Koszul_terms=552,finite_cycle_path_checks=1296,finite_weighted_maximum_checks=11664,finite_checks_only=True,
    root_exact_public_source_builtin_compiler_success=False,builtin_compiler_not_yet_requested=True,
    root_visual_pages_read=[],pdf_visually_root_read=False,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],
    frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
    caller_grants=['O217','D214','N220','T171','Q222','C218','G227'],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
    scope='Whole14-page partial manuscript: actual same-original-reference finite initial points and residual coordinate degree in every dimension; genuine CLD atomic SUPPORT only; common full-coefficient-Gauss smooth geometrically integral curve and actual type-II lifts preserving original section values; one fixed skeleton with all cycles, honest map degree/annular residue-index slope bounds for every weighted FS family; uniform reference moment BEFORE E1 membership; intrinsic all-test integrability iff finite unit bound iff finite continuous dual; MATERIAL finite-U coercivity repair; own-output dual attainment. General prescribed-target attainment and every-solution all-point uniqueness remain open.',
    protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n'); (D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('General reference moment and intrinsic targets: unreviewed whole14-page paper\n\n982 TeX lines,370 argument lines,195 ledger lines and six exact native final notes read completely. Seven complete caller grants/all unchanged clarifications;26 original primary file bindings,43 whole input units,27 exact native extracts and64 artifact hashes verified. Saved longer notes differ and remain private unregistered data. Material finite-U coercivity correction preserved; no independent acceptance or original closure. Own finite checks and exact-source local builds are verification only. Existing editor preserved.\n')
print(json.dumps(dict(round=199,continuation=257,source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],native_artifact_hash_count=64,local_build_exit_codes=passes,warnings=warnings,binding_sha256=sha(binding),original_closed=False),indent=2))
