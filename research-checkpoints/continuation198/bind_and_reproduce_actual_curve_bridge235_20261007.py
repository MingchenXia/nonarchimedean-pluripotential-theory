from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, shutil, re, fitz

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-191').iterdir())
D=K/'public-P16.4-continuation235-positive-graph-and-conditional-actual-curve'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x=json.loads((K/'round191-completed-inspection-LOCALONLY.json').read_text())
c=x['campaign']; assert c['status']=='completed' and c['error'] is None
k=c['result']; assert k['candidate'] is False and len(k['notes'])==5
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
n=finals[0]; assert n['candidate'] is False and len(n['notes'])==5
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
ids={a['id'] for a in n['notes']}
assert all(set(a['support'])<=ids for a in n['notes'])
A=Path(k['workspace']); frozen=json.loads((C/'input.json').read_text())
prompt=json.loads(req['prompt']); f=json.loads((C/'freeze.json').read_text())
assert set(prompt)==set(frozen)|{'workspace'}
assert all(prompt[q]==frozen[q] for q in frozen) and prompt['workspace']==str(A)
assert json.loads((A/'input.json').read_text())==frozen
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','workspace-write',True)
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
grants={'O':'public-P16.4-continuation217-general-E1-mixed-operator','D':'public-P16.4-continuation214-completed-closure-descent','N':'public-P16.4-continuation220-norming-reference-target-criterion','T':'public-P16.4-round171-partial-reader','Q':'public-P16.4-continuation222-projective-line-kernel-equation','C':'public-P16.4-continuation218-strict-locality-comparison'}
for label,folder in grants.items(): assert sha(A/f'sources/grant-{label}.tex')==sha(K/folder/'P16.4-paper.tex')
hashes=json.loads((A/'artifact-hashes.json').read_text())
assert len(hashes)==59
assert all(sha(A/p)==h for p,h in hashes.items())
assert sha(A/'P16.4-paper.tex')=='3e517c6b9ce68a29f11d5c35e2bc9f809de728812c7e5a73db1d34a7d0f1e110'
assert len((A/'P16.4-paper.tex').read_text().splitlines())==884
assert len((A/'P16.4-argument.md').read_text().splitlines())==330
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
actual=K/'P16.4-round191-completed-actual-author-result-20261007.json'
native=K/'P16.4-round191-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round191-settled-partial-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n')
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','result.json','source-application-ledger.md','source-application-ledger.json','graph_checks.py'):
    shutil.copyfile(A/name,D/name)
for name in ('artifact-hashes.json','build-manifest.json','final-validation.json','source-retrieval.json','source-line-coverage.json','graph-checks-output.json','graph-checks.stdout.txt','graph-checks.stderr.txt','pdflatex-1.stdout.txt','pdflatex-1.stderr.txt','pdflatex-2.stdout.txt','pdflatex-2.stderr.txt'):
    shutil.copyfile(A/name,D/'evidence'/('native-'+name))
q=subprocess.run(['python','graph_checks.py'],cwd=D,capture_output=True)
(D/'evidence/root-finite-check.stdout').write_bytes(q.stdout)
(D/'evidence/root-finite-check.stderr').write_bytes(q.stderr)
assert q.returncode==0
checks=json.loads(q.stdout)
assert checks==json.loads((D/'evidence/native-graph-checks-output.json').read_text())
assert checks['interpolation_cases']==140 and checks['raw_mass_cases']==210
passes=[]
for i in (1,2):
    q=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout)
    (D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode==0
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
assert not any('undefined' in w or 'Overfull' in w or w.startswith('!') for w in warnings)
pdf=fitz.open(D/'P16.4-paper.pdf'); assert len(pdf)==13
for i in (0,12): pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b=dict(recorded_utc=now,round=191,atom='P16.4',continuation=235,candidate=False,canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),exact_decoded_native_task_assignment_notes_equal_frozen_input=True,retained_workspace_added_to_prompt=True,native_artifact_input_equal_frozen_input=True,all_native_note_math_equal_canonical=True,kernel_only_text_addition='Two newlines and Artifacts: followed by retained workspace',all_support_ids_valid_local=True,whole_five_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,310],[311,610],[611,910]],source_lf_lines=884,whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,170],[145,205],[171,350]],argument_lf_lines=330,whole_quote_free_markdown_source_application_ledger_root_read=True,json_ledger_separately_whole_root_read=False,whole_finite_check_code_root_read=True,all_recorded_native_artifact_hashes_validated=True,native_artifact_hash_count=len(hashes),source_sha256=sha(D/'P16.4-paper.tex'),native_pdf_sha256=sha(A/'P16.4-paper.pdf'),root_pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=13,root_native_exact_author_source_compiler_success=True,root_native_exact_public_source_compiler_success=False,root_local_build_exit_codes=passes,root_local_final_warnings=warnings,root_own_finite_check_reproduced=True,finite_interpolation_cases=140,finite_raw_mass_energy_cases=210,finite_checks_only=True,pdf_visually_root_read=False,all_native_grant_bodies_equal_exact_accepted_caller_sources=True,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],caller_grants=['O217','D214','N220','T171','Q222','C218'],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,unconditional_all_genus_claim=False,scope='New finite-graph positive-curvature interpolation including loops, signed starting curvature and irrational edge lengths, finite-core kernel and maximum-support proofs. Conditional actual all-genus curve equation with R1-R5 actual-model/skeleton/chart/finite-orbit antecedents explicitly unverified. Raw V^2/2 constants, arbitrary support, terminal all-point values and descent are argued conditionally. No unconditional curve or arbitrary-dimensional equation accepted.',protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n')
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Positive graph interpolation and the conditional actual curve bridge\n\nUnchanged native191 thirteen-page draft, candidate=false. All884 TeX lines,330 argument lines, five canonical notes, the128-line quote-free Markdown source ledger and202-line finite-check code read by ROOT. Six complete accepted caller grants; new actual curve geometry remains conditional on R1-R5 and has no independent mathematical verdict. Neither an unconditional all-genus theorem nor original P16.4 is closed.\n\nThe own exact140 interpolation/210 raw-mass cases were reproduced. Two local builds and the built-in compiler on the native source succeeded. These are finite/compiler observations only. No private active output was read. The protected existing editor remains open and untouched.\n')
print(json.dumps(dict(round=191,continuation=235,candidate=False,source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],warnings=warnings,binding_sha256=sha(binding),native_artifact_hash_count=len(hashes),independent_verdict=None,original_closed=False),indent=2))
