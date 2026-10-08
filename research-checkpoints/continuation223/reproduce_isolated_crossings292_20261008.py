from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-217/P05.1-isolated-affine-crossings-all-continuous-global-regularization-paper';A=C/'artifacts/codex-ybo6Ea'
D=K/'public-P05.1-continuation292-isolated-affine-crossings-global-real-regularization'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
assert sha(A/'P05.1-paper.tex')=='4ece9622c0d97a861dde051ec6a31c0bd0416781bd4c43c0b4aaa0f498ffe11c'
assert sha(A/'argument.md')=='1fd6dcb5810cbb3163158543b2643266bfbb5e92748552a0357135f83fdaffbc'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert json.loads((C/'input.json').read_text())==json.loads((A/'input.json').read_text())
manifest=json.loads((A/'artifact-bindings.json').read_text())['files']
for e in manifest:
    p=A/e['path'];assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
assert (A/'artifact-bindings.sha256').read_text().split()[0]==sha(A/'artifact-bindings.json')
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
F=K/'P05.1-round217-exact-native-model-final-isolated-affine-crossings-author-20261008.json'
f=json.loads(F.read_text());assert not f['candidate'] and len(f['notes'])==6
assert F.read_bytes()==(A/'native-notes.json').read_bytes()
j=json.loads((K/'round217-settled-inspection-LOCALONLY.json').read_text());registered=j['campaign']['result']
assert not registered['candidate'] and len(registered['notes'])==6
for x,y in zip(f['notes'],registered['notes']):
    assert x.keys()==y.keys()
    for key in x:assert y[key]==(x[key]+'\n\nArtifacts: '+registered['workspace'] if key=='text' else x[key])
source=(A/'P05.1-paper.tex').read_text();assert not re.search(r'\\(?:input|include|write18|openin|openout)\b',source)
D.mkdir();E=D/'evidence';E.mkdir();H=E/'own-author217-evidence';H.mkdir();W=E/'ROOT-reproduction';W.mkdir()
for name in ['P05.1-paper.tex','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-coverage.md','execution-log.md']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(F,E/'exact-native-final.json');write(E/'registered-native-worker-result.json',registered)
for e in manifest:
    if e.get('distribution')=='LOCALONLY':continue
    dst=H/e['path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(A/e['path'],dst)
for name in ['artifact-bindings.json','artifact-bindings.sha256']:shutil.copyfile(A/name,H/name)
(W/'logs').mkdir()
for name in ['check_certificates.py','certificate-input.json','P05.1-paper.tex']:shutil.copyfile(A/name,W/name)
p=subprocess.run(['python','check_certificates.py'],cwd=W,capture_output=True,text=True)
(W/'logs/checks.log').write_text(p.stdout+p.stderr);assert p.returncode==0
assert (W/'certificate-output.json').read_bytes()==(A/'certificate-output.json').read_bytes()
out=json.loads((W/'certificate-output.json').read_text())
assert len(out['matrices'])==5 and sum(len(x['ordered_permutations']) for x in out['matrices'])==13
assert sum(x['all_words'] for x in out['matrices'])==40 and sum(x['repeated_words_zero'] for x in out['matrices'])==27
commands=[]
for i in [1,2]:
    args=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex']
    p=subprocess.run(args,cwd=W,capture_output=True,text=True);log=W/f'logs/build-pass-{i}.log';log.write_text(p.stdout+p.stderr)
    commands.append(dict(argv=args,exit_code=p.returncode,log=str(log)));assert p.returncode==0
args=['pandoc','-f','latex','-t','gfm','--wrap=none','P05.1-paper.tex','-o','argument.md']
p=subprocess.run(args,cwd=W,capture_output=True,text=True);(W/'logs/pandoc.log').write_text(p.stdout+p.stderr);assert p.returncode==0
assert (W/'argument.md').read_bytes()==(A/'argument.md').read_bytes()
assert sha(W/'P05.1-paper.tex')==sha(A/'P05.1-paper.tex')==sha(D/'P05.1-paper.tex')
shutil.copyfile(W/'P05.1-paper.pdf',D/'P05.1-paper.pdf')
diagnostics=[[line for line in Path(c['log']).read_text().splitlines() if any(k in line for k in ['Warning','Overfull','Underfull','undefined','Error'])] for c in commands]
assert not diagnostics[-1]
info=subprocess.run(['pdfinfo',str(D/'P05.1-paper.pdf')],capture_output=True,text=True,check=True).stdout;(W/'logs/pdfinfo.txt').write_text(info)
binding=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),original='P05.1',continuation=292,source=str(D/'P05.1-paper.tex'),source_sha256=sha(D/'P05.1-paper.tex'),source_LF_lines=source.count('\n'),argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=sha(D/'P05.1-paper.pdf'),pdf_pages=17,exact_FINAL=str(E/'exact-native-final.json'),exact_FINAL_sha256=sha(E/'exact-native-final.json'),exact_FINAL_candidate=False,exact_FINAL_notes=6,exact_FINAL_saved_native_notes_byte_equal=True,expanded_saved_draft_preserved_not_exact_FINAL=True,registered_result_only_Artifacts_suffix=True,parent_child_input_semantically_equal=True,author_artifact_bindings_verified=len(manifest),math_bindings_verified=19,primary_bindings_verified=4,ROOT_source_whole_read=True,ROOT_ledger_scope_coverage_execution_whole_read=True,ROOT_exact_FINAL_all6_whole_read=True,ROOT_safe_exact_checker_whole_read=True,ROOT_finite_output_exact=True,finite_matrix_cases=5,finite_permutations=13,finite_words=40,repeated_factor_zeros=27,finite_scope_only=True,latex_to_markdown_exact=True,local_build_exit_codes=[c['exit_code'] for c in commands],local_build_diagnostics=diagnostics,source_unchanged=True,retained_presentation_typo='Source equation contains literal qquad after sum_i w_i=0; intended separator is clear in exact FINAL prose. Source remains unchanged.',only_grants=['A224','B225','R230','S262','S272'],all_clarifications_retained=True,new_ROOT289290293294_excluded_from_author=True,new_S282_acceptance_not_a_grant=True,mathematical_acceptance=False,original_closed=False,protected_editor_unchanged_open=True)
write(D/'root-reproduction-binding-20261008.json',binding);print(json.dumps(binding,indent=2))
