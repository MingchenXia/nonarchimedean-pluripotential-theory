from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-194/P05.2-original-contact-classification-after-whole-continuous-completion'
A=C/'artifacts/codex-zS8OiG'
D=K/'public-P05.2-continuation247-finite-PA-contact-circuits-and-plane-counterexample'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round194-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='blocked' and x['campaign']['result'] is None
assert x['campaign']['error']=='Unknown, dead, or forward support: B225'
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(t['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}:finals.append(n)
assert len(finals)==1 and finals==json.loads((K/'P05.2-round194-exact-native-final-unregistered-LOCALONLY.json').read_text())
n=finals[0];assert n['candidate'] is False and len(n['notes'])==5
assert n['notes'][0]['support']==['B225','R230']
assert n['notes'][-1]['support']==['n1','n2','n3','n4','A224']
f=json.loads((C/'freeze.json').read_text()); frozen=json.loads((C/'input.json').read_text())
prompt=json.loads(req['prompt']);assert set(prompt)==set(frozen)|{'workspace'}
assert all(prompt[q]==frozen[q] for q in frozen) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==frozen
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
pb=json.loads((C/'private-primary-packet-bindings.json').read_text());assert len(pb)==4
for e in pb:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
mb=json.loads((C/'mathematical-data-bindings.json').read_text())
assignment=frozen['assignment'].splitlines()
for e in mb:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf'];assert assignment[lo-1:hi]==Path(e['source']).read_text().splitlines()
for g in f['complete_grant_bindings']:
    label=g['label'];native={'A':'A224','B':'B225','R':'R230'}[label]
    assert sha(A/f'caller-grants/{native}.tex')==sha(g['source'])==g['source_sha256']
    assert sha(A/f'caller-grants/{native}-clarifications.json')==sha(g['clarifications'])==g['clarifications_sha256']
    assert json.loads(Path(g['acceptance']).read_text())['verdict']=='PASS'
manifest=json.loads((A/'evidence/artifact-manifest.json').read_text());assert len(manifest['files'])==41
for e in manifest['files']:assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
assert sha(A/'P05.2-paper.tex')=='6cd62476334083dad3496bea5fe35d27ea083e5c23ac29c96e0d263d7aeba082'
assert len((A/'P05.2-paper.tex').read_text().splitlines())==693
assert len((A/'argument.md').read_text().splitlines())==710
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
native=K/'P05.2-round194-exact-native-final-unregistered-20261007.json'
binding=K/'P05.2-round194-unregistered-author-and-whole-paper-binding-20261007.json'
assert not native.exists() and not binding.exists()
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir();(D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','notes.json','source-application-ledger.md','check_certificates.py','certificate-input.json','execution-commands.md'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-manifest.json','certificate-output.json','certificate-stdout.json','environment.json','latex-pass1.txt','latex-pass2.txt','latex-pass3.txt','latex-pass4.txt','primary-provenance.json','preparation-output.json','artifact-build-output.json'):
    shutil.copyfile(A/'evidence'/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python3','check_certificates.py'],cwd=D,capture_output=True)
(D/'evidence/root-certificate.stdout').write_bytes(q.stdout);(D/'evidence/root-certificate.stderr').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads(q.stdout);assert checks==json.loads((D/'evidence/native-certificate-output.json').read_text())
assert checks['all_assertions_passed'] and checks['contact_integral']=='-2' and checks['raw_masses']==['8','4','4']
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout);(D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode);assert q.returncode==0
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(errors='replace'),re.M)
assert not any('undefined' in w or 'Overfull' in w or w.startswith('!') for w in warnings)
pdf=fitz.open(D/'P05.2-paper.pdf');assert len(pdf)==10
for i in (0,5,6,9):pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
saved=json.loads((A/'notes.json').read_text())
assert saved['candidate'] is False and len(saved['notes'])==5
assert [(a['id'],a['support']) for a in saved['notes']]==[(a['id'],a['support']) for a in n['notes']]
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=194,atom='P05.2',continuation=247,candidate=False,
    canonical_result=None,canonical_registration_succeeded=False,native_campaign_status='blocked',native_registration_error=x['campaign']['error'],
    native_final=str(native),native_final_sha256=sha(native),native_call_exit_code=0,native_call_failed=False,
    native_final_preserved_unchanged=True,external_grant_support_labels_not_registered_as_kernel_note_ids=True,
    exact_decoded_native_prompt_equal_frozen_input_with_workspace=True,native_saved_input_equal_frozen_input=True,
    saved_notes_equal_native_final=saved==n,saved_notes_same_ids_and_supports=True,saved_note_artifact_reproduced_from_generator=False,
    saved_note_distinction='Saved long notes and exact native final are separate unregistered artifacts; neither is a canonical registered result. No native generator rerun or support-label correction.',
    whole_native_final_five_notes_root_read=True,whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,150],[151,360],[361,510],[511,693]],source_lf_lines=693,
    whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,245],[246,485],[486,710]],argument_lf_lines=710,
    whole_quote_free_markdown_ledger_root_read=True,ledger_lf_lines=62,whole_finite_check_code_root_read=True,finite_check_code_lf_lines=214,
    all_recorded_native_artifact_hashes_validated=True,native_artifact_hash_count=41,artifact_manifest_self_excluded=True,
    all_three_complete_accepted_grants_and_all_clarifications_exact=True,caller_grants=['A224','B225','R230'],all_four_frozen_private_primary_bindings_valid=True,
    root_primary_publisher_read='BBGS2022 version of record: complete definitions and Propositions3.12/3.15, Lemma3.18, Proposition3.19, LF443–704 of bound extraction. Lattice-to-Euclidean conversion reconstructed in the paper remains unreviewed.',
    source_sha256=sha(D/'P05.2-paper.tex'),argument_sha256=sha(D/'argument.md'),native_pdf_sha256=sha(A/'P05.2-paper.pdf'),root_pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=10,
    root_local_build_exit_codes=passes,root_local_final_warnings=warnings,root_exact_public_source_builtin_compiler_success=False,
    own_finite_checks_reproduced=True,finite_checks_only=True,finite_slope_vectors=729,finite_grid_points=561,finite_radial_chords=448,finite_flat_PCC_cases=3,finite_kink_cases=85,
    raw_mass_examples=['8','4','4'],raw_contact_example='-2',pdf_visually_root_read=False,
    model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
    independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
    scope='Finite PA local affine-support and positive-circuit characterization; strict-support roof necessity/sufficiency for the stated all-PA-envelope endpoint sector, and an actual nonseparable two-coordinate-plane integral-PA counterexample with raw masses8,4,4 and contact-2. Fixed-structure semialgebraic certificate only; no bounded refinement search, global jet realization, general regularizable endpoint or full original contact/regularization classification.',
    native_failed_initial_latex_log_overwritten_history_limitation_preserved=True,protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n');(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Finite PA contact circuits and a nonseparable plane counterexample\n\nUnchanged ten-page native194 manuscript; candidate=false. The author call exited successfully but kernel registration failed with Unknown, dead, or forward support: B225. There is no canonical author result. The exact native final and the longer saved notes are preserved separately without repairing their external support labels.\n\nROOT read all693 TeX lines, all710 argument lines, all62 quote-free ledger lines, all214 finite-check code lines and all five exact native final notes. All41 manifest artifacts, three complete accepted caller grants with all clarifications, four original-primary bindings and the frozen/native prompt were checked. Finite checks were reproduced in a separate public copy; two local builds succeeded. No independent mathematical verdict or new original closure is claimed. Original P05.2 remains open. Existing editor untouched.\n')
print(json.dumps(dict(continuation=247,pages=10,source_sha256=b['source_sha256'],binding_sha256=sha(binding),native_registration_error=b['native_registration_error'],root_local_build_exit_codes=passes,warnings=warnings,original_closed=False),indent=2))
