from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, shutil, re, fitz

R = Path('/workspace/research'); K = R/'root-checks'
C = next((R/'campaigns/round-190').iterdir())
D = K/'public-P05.2-continuation230-continuous-completion-and-envelope'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
x = json.loads((K/'round190-completed-inspection-LOCALONLY.json').read_text())
c = x['campaign']; assert c['status'] == 'completed' and c['error'] is None
k = c['result']; assert k['candidate'] is False and len(k['notes']) == 3
req = next(t['data']['payload'] for t in x['records'] if t['kind'] == 'xean.call.request')
msg = next(t['data']['message'] for t in x['records'] if t['kind'] == 'xean.call.settled')
assert msg['exitCode'] == 0 and not msg['failed'] and not msg['isCanceled']
finals = []
for line in msg['stdout'].splitlines():
    t = json.loads(line)
    if t.get('type') == 'item.completed' and t.get('item', {}).get('type') == 'agent_message':
        try: n = json.loads(t['item']['text'])
        except (ValueError, TypeError): continue
        if isinstance(n, dict) and set(n) == {'notes', 'candidate'}: finals.append(n)
assert len(finals) == 1
n = finals[0]; assert n['candidate'] is False and len(n['notes']) == 3
for a, b in zip(n['notes'], k['notes']):
    assert all(a[q] == b[q] for q in ('id', 'summary', 'detailedSummary', 'support'))
    assert b['text'] == a['text'] + '\n\nArtifacts: ' + k['workspace']
ids = {a['id'] for a in n['notes']}
assert all(set(a['support']) <= ids for a in n['notes'])
prompt = json.loads(req['prompt']); frozen = json.loads((C/'input.json').read_text())
A = Path(k['workspace']); f = json.loads((C/'freeze.json').read_text())
assert set(prompt) == set(frozen) | {'workspace'}
assert all(prompt[q] == frozen[q] for q in frozen) and prompt['workspace'] == str(A)
assert json.loads((A/'input.json').read_text()) == frozen
assert (req['model'], req['reasoning'], req['sandbox'], req['shell']) == ('gpt-6.1-sol', 'xhigh', 'workspace-write', True)
for name, key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name) == f[key]
for grant, folder in [('A224','public-P05.2-continuation224-strict-growth-obstruction'),('B225','public-P05.2-continuation225-balanced-support-maximum-principle')]:
    assert sha(A/f'sources/{grant}-caller-grant.tex') == sha(K/folder/'P05.2-paper.tex')
provenance = json.loads((A/'evidence/provenance.json').read_text())
assert len(provenance['files']) == 38
assert all(sha(A/r['path']) == r['sha256'] and (A/r['path']).stat().st_size == r['bytes'] for r in provenance['files'])
assert sha(A/'P05.2-paper.tex') == 'ffadbcedcb0eb49c893ae81f3d7696ef4cba25a9df6179644eedb7b51286cc3a'
assert len((A/'P05.2-paper.tex').read_text().splitlines()) == 337
assert len((A/'argument.md').read_text().splitlines()) == 467
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
actual = K/'P05.2-round190-completed-actual-author-result-20261007.json'
native = K/'P05.2-round190-native-model-final-partial-author-20261007.json'
binding = K/'P05.2-round190-settled-partial-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k, ensure_ascii=False, indent=2)+'\n')
native.write_text(json.dumps(n, ensure_ascii=False, indent=2)+'\n')
D.mkdir(); (D/'evidence').mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','notes.json','source-application-ledger.md','proof-audit.md','star-input.json','check_star_estimates.py'):
    shutil.copyfile(A/name,D/name)
shutil.copyfile(A/'evidence/provenance.json',D/'evidence/native-artifact-provenance.json')
shutil.copyfile(A/'evidence/star-check-output.json',D/'evidence/native-star-check-output.json')
for name in ('final-build-pass-1.txt','final-build-pass-2.txt','build-summary.json'):
    shutil.copyfile(A/'evidence'/name,D/'evidence'/('native-'+name))
q = subprocess.run(['python','check_star_estimates.py'],cwd=D,capture_output=True)
(D/'evidence/root-finite-check.stdout').write_bytes(q.stdout)
(D/'evidence/root-finite-check.stderr').write_bytes(q.stderr)
assert q.returncode == 0
assert json.loads((D/'evidence/star-check-output.json').read_text()) == json.loads((D/'evidence/native-star-check-output.json').read_text())
passes = []
for i in (1,2):
    q = subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex'],cwd=D,capture_output=True)
    (D/f'evidence/root-latex-pass{i}.stdout').write_bytes(q.stdout)
    (D/f'evidence/root-latex-pass{i}.stderr').write_bytes(q.stderr)
    passes.append(q.returncode); assert q.returncode == 0
warnings = re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P05.2-paper.log').read_text(errors='replace'),re.M)
assert warnings == []
pdf = fitz.open(D/'P05.2-paper.pdf'); assert len(pdf) == 13
for i in (0,12): pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
b = dict(recorded_utc=now,round=190,atom='P05.2',continuation=230,candidate=False,canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),exact_decoded_native_task_assignment_notes_equal_frozen_input=True,retained_workspace_added_to_prompt=True,native_artifact_input_equal_frozen_input=True,all_native_note_math_equal_canonical=True,kernel_only_text_addition='Two newlines and Artifacts: followed by retained workspace',all_support_ids_valid_local=True,whole_three_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,240],[241,360]],source_lf_lines=337,whole_native_argument_separately_root_read=True,root_argument_read_lf_ranges=[[1,235],[236,480]],argument_lf_lines=467,whole_quote_free_source_application_ledger_root_read=True,whole_proof_audit_root_read=True,all_38_native_artifact_hashes_validated=True,source_sha256=sha(D/'P05.2-paper.tex'),native_pdf_sha256=sha(A/'P05.2-paper.pdf'),root_pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=13,root_native_exact_author_source_compiler_success=True,root_native_exact_public_source_compiler_success=False,root_local_build_exit_codes=passes,root_local_final_warnings=warnings,root_own_finite_check_reproduced=True,finite_barycentric_cases=1035,finite_convex_function_cases=2070,finite_checks_only=True,pdf_visually_root_read=False,all_native_grant_bodies_equal_exact_accepted_caller_sources=True,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],caller_grants=['A224','B225'],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,scope='Every finite positive balanced rational embedded polyhedral space in arbitrary dimension; finite-valued rational-endpoint PC continuous dominating representative and exact upper-semicontinuous hull without boundedness premise; all bounded continuous obstacle envelopes continuous under the actual continuous reference/global growth; sharp fan-vertex diagnostic, separately named compact rational-affine chart constant endpoint and genuine raw zero measure, exact entire-class half-unit density obstruction. General PA regularization/operator and all-obstacle contact classification remain open.',protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n')
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'README.md').write_text('Continuous completion and unrestricted envelope continuity\n\nEntire unchanged thirteen-page native190 draft. All337 source lines,467 argument lines, all3 canonical notes, quote-free application ledger and proof audit read by ROOT. Every finite positive balanced embedded rational space and every bounded continuous obstacle; no general PA approximation, MA operator domain or full original closure. Exactly complete accepted A224/B225 caller grants. Independent mathematical review remains pending.\n\nOwn finite rational checks reproduced at1035 barycentric/2070 convex-function cases; two clean local compiler passes. These observations do not certify continuum mathematics. The protected existing editor remains open and untouched.\n')
print(json.dumps(dict(round=190,continuation=230,candidate=False,source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],binding_sha256=sha(binding),independent_verdict=None,original_closed=False),indent=2))
