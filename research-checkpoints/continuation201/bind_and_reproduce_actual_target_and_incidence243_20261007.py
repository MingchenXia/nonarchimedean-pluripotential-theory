from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-193').iterdir())
D=K/'public-P16.4-continuation243-target-integrability-incidence-and-local-formal-bridge'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round193-completed-inspection-LOCALONLY.json').read_text())
c=x['campaign']; assert c['status']=='completed' and c['error'] is None
k=c['result']; assert k['candidate'] is False and len(k['notes'])==6
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(t['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}: finals.append(n)
assert len(finals)==1
n=finals[0]; assert n['candidate'] is False and len(n['notes'])==6
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
ids={a['id'] for a in n['notes']}; assert all(set(a['support'])<=ids for a in n['notes'])
A=Path(k['workspace']); frozen=json.loads((C/'input.json').read_text()); f=json.loads((C/'freeze.json').read_text())
prompt=json.loads(req['prompt']); assert set(prompt)==set(frozen)|{'workspace'}
assert all(prompt[q]==frozen[q] for q in frozen) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==frozen
saved_notes=json.loads((A/'notes.json').read_text())
assert saved_notes['candidate'] is False and len(saved_notes['notes'])==6
assert all(a['id']==b['id'] and a['support']==b['support'] for a,b in zip(saved_notes['notes'],n['notes']))
# The saved artifact contains full paper sections; the registered native final
# contains condensed self-contained notes. Reproduce the saved artifact from
# the fully read emitter, with its final write/print expressions removed.
tree=ast.parse((A/'emit_notes.py').read_text())
assert isinstance(tree.body[-2],ast.Expr) and isinstance(tree.body[-2].value,ast.Call) and isinstance(tree.body[-2].value.func,ast.Attribute) and tree.body[-2].value.func.attr=='write_text'
assert isinstance(tree.body[-1],ast.Expr) and isinstance(tree.body[-1].value,ast.Call) and isinstance(tree.body[-1].value.func,ast.Name) and tree.body[-1].value.func.id=='print'
tree.body=tree.body[:-2]
ns={'__file__':str(A/'emit_notes.py'),'__name__':'root_readonly_note_reproduction'}
exec(compile(tree,str(A/'emit_notes.py'),'exec'),ns)
assert ns['result']==saved_notes and saved_notes!=n
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
grants={'O':'public-P16.4-continuation217-general-E1-mixed-operator','D':'public-P16.4-continuation214-completed-closure-descent','N':'public-P16.4-continuation220-norming-reference-target-criterion','T':'public-P16.4-round171-partial-reader','Q':'public-P16.4-continuation222-projective-line-kernel-equation','C':'public-P16.4-continuation218-strict-locality-comparison'}
for label,folder in grants.items(): assert sha(A/f'sources/grant-{label}.tex')==sha(K/folder/'P16.4-paper.tex')
pb=json.loads((C/'private-primary-packet-bindings.json').read_text()); assert len(pb)==16
for e in pb: assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
hashes=json.loads((A/'artifact-hashes.json').read_text()); assert len(hashes)==66
for p,h in hashes.items(): assert sha(A/p)==h['sha256'] and (A/p).stat().st_size==h['bytes']
assert sha(A/'P16.4-paper.tex')=='03d38508af696c982c399fb5e51a217470c10f99685eae75c374e6f6b0c5fdcb'
assert len((A/'P16.4-paper.tex').read_text().splitlines())==1084
assert len((A/'P16.4-argument.md').read_text().splitlines())==361
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P16.4-round193-completed-actual-author-result-20261007.json'
native=K/'P16.4-round193-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round193-settled-partial-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','notes.json','source-application-ledger.md','source-application-ledger.json','finite_checks.py'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-hashes.json','grant-bindings.json','packet-verification.json','final-verification.json','environment.json','commands.json','finite-check-output.json'):
    shutil.copyfile(A/name,D/'evidence'/('native-'+name))
for name in ('pdflatex-1.log','pdflatex-2.log','finite-checks.log','packet-verification.log'):
    shutil.copyfile(A/'build-logs'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','finite_checks.py'],cwd=D,capture_output=True)
(D/'evidence/root-finite-check.stdout').write_bytes(q.stdout); (D/'evidence/root-finite-check.stderr').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads(q.stdout);assert checks==json.loads((D/'evidence/native-finite-check-output.json').read_text())
assert (checks['interpolation_cases'],checks['energy_cases'],checks['raw_curve_mass_cases'],checks['nilpotence_cases'])==(81,1995,16,100)
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout);(D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode);assert q.returncode==0
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
assert not any('undefined' in w or 'Overfull' in w or w.startswith('!') for w in warnings)
pdf=fitz.open(D/'P16.4-paper.pdf');assert len(pdf)==15
for i in (0,14):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=193,atom='P16.4',continuation=243,candidate=False,
    canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
    exact_decoded_native_task_assignment_notes_equal_frozen_input=True,retained_workspace_added_to_prompt=True,
    native_artifact_input_equal_frozen_input=True,native_saved_notes_equal_exact_native_final=False,
    native_saved_long_note_artifact_exactly_reproduced_from_whole_argument_and_read_emitter=True,
    native_saved_long_notes_and_native_final_same_local_ids_and_supports=True,
    saved_note_artifact_distinction='Saved notes contain full paper sections; the registered native final contains condensed self-contained versions. Both are preserved. Only the exact native final is bound to canonical registered notes.',
    note_emitter_rerun_read_only=True,note_emitter_final_write_and_print_ast_expressions_removed=True,
    first_attempt_incorrect_saved_final_identity_assumption_failed_before_any_public_write=True,
    all_native_final_note_math_equal_canonical=True,
    kernel_only_text_addition='Two newlines and Artifacts: followed by retained workspace',all_support_ids_valid_local=True,
    whole_six_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,260],[261,560],[561,850],[851,1084]],source_lf_lines=1084,
    whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,145],[146,255],[256,361]],argument_lf_lines=361,
    whole_quote_free_markdown_source_application_ledger_root_read=True,json_ledger_separately_whole_root_read=False,
    whole_finite_check_code_root_read=True,all_recorded_native_artifact_hashes_validated=True,native_artifact_hash_count=len(hashes),
    all_six_native_grant_bodies_equal_exact_accepted_caller_sources=True,all_six_complete_grants_and_clarifications_in_frozen_input=True,all_sixteen_frozen_original_primary_bindings_valid=True,
    source_sha256=sha(D/'P16.4-paper.tex'),argument_sha256=sha(D/'P16.4-argument.md'),native_pdf_sha256=sha(A/'P16.4-paper.pdf'),root_pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=15,
    root_native_exact_source_builtin_compiler_success=False,root_native_exact_source_builtin_compiler_observation='Request did not return diagnostics before the waiting orchestration cell was terminated; compilation remains unverified by this service. Source preserved unchanged.',
    root_exact_public_source_builtin_compiler_success=False,root_local_build_exit_codes=passes,root_local_final_warnings=warnings,
    own_finite_checks_reproduced=True,finite_interpolation_cases=81,finite_scaling_cases=1995,finite_raw_mass_cases=16,finite_nilpotence_examples=100,finite_checks_only=True,
    pdf_visually_root_read=False,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
    caller_grants=['O217','D214','N220','T171','Q222','C218'],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,unconditional_all_genus_claim=False,
    scope='Whole13 numbered draft results: Radon continuous-net integration, finite continuous dual implying intrinsic all-E1 integrability, unconditional intrinsic/unit-bound equivalence by actual FS-majorant convex-series recognition, exact scaling bound and conditional coercivity, variational attainment only for already genuine outputs; actual common generic coefficient-Gauss field and actual curve points preserving all original section values under stated initial residual-coordinate and cohomological hypotheses; positive irrational-cycle graph interpolation; local actual Cartier gluing and exact degree correction; formal section lifting and same-bundle pure-FS recognition with explicit whole-mod-a and analytic/algebraic-section premises. General geometric premises, M0, prescribed-target attainment and original equation remain open.',
    root_new242_positive_margin_correction_applies_to_older_working238241_only=True,native193_graph_positive_mixture_already_correct=True,protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n');(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Actual target estimates, generic incidence points, and a local formal bridge\n\nUnchanged native193 fifteen-page draft, candidate=false. All1084 TeX lines,361 argument lines, six canonical notes, the whole235-line quote-free Markdown source ledger and finite-check code read by ROOT. Six complete accepted caller grants and all clarifications;16 frozen original-primary bindings. All66 native artifact hashes and exact native/canonical/request/input equalities checked. No independent verdict, original closure, unconditional all-genus equation, general M0, or prescribed-target attainment.\n\nOwn81 interpolation,1995 scaling,16 raw-mass and100 nilpotence finite cases reproduced. Two local builds passed; the built-in native-source compilation request did not return diagnostics before the orchestration cell was terminated and remains unverified. Only finite/compiler evidence is claimed. Protected existing editor untouched and kept open.\n')
print(json.dumps(dict(round=193,continuation=243,candidate=False,source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],warnings=warnings,binding_sha256=sha(binding),native_artifact_hash_count=len(hashes),independent_verdict=None,original_closed=False),indent=2))
