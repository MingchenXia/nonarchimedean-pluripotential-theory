from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, re

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-216/P05.1-original-coefficient-separated-all-obstacle-regularity-classification'
A=C/'artifacts/codex-U7ErDr'
D=K/'public-P05.1-continuation291-compact-balanced-charts-and-independent-affine-branches'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
assert sha(A/'P05.1-paper.tex')=='48903ace22882dbeb879cf262be02ba6476fbff6d26c486af213c592bdc3400d'
assert sha(A/'argument.md')=='8e2b3fe1ea330c64fab81499f3cc748a22591a15bb41ae25ab1f132221958ff8'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert json.loads((C/'input.json').read_text())==json.loads((A/'input.json').read_text())
manifest=json.loads((A/'artifact-bindings.json').read_text())['files']
for e in manifest:
    p=A/e['filename']; assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
F=K/'P05.1-round216-exact-native-model-final-original-regularity-author-20261008.json'
final=json.loads(F.read_text());saved=json.loads((A/'native-notes.json').read_text())
assert not final['candidate'] and not saved['candidate'] and len(final['notes'])==len(saved['notes'])==6
for x,y in zip(final['notes'],saved['notes']):
    assert x.keys()==y.keys()
    for k in x:assert y[k]==(x[k]+'\n' if k=='text' else x[k])
source=(A/'P05.1-paper.tex').read_text()
assert not re.search(r'\\(?:input|include|write18|openin|openout)\b',source)
D.mkdir(); E=D/'evidence';E.mkdir(); H=E/'own-author216-evidence';H.mkdir()
for name in ['P05.1-paper.tex','argument.md','source-application-ledger.md','scope-and-gaps.md','build-report.md']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(F,E/'exact-native-final.json')
for e in manifest:
    src=A/e['filename']
    if src.parts[len(A.parts)]=='LOCALONLY':continue
    dst=H/e['filename'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
shutil.copyfile(A/'artifact-bindings.json',H/'artifact-bindings.json')
W=E/'ROOT-reproduction';W.mkdir()
for sub in ['code','inputs','evidence','logs']:(W/sub).mkdir()
shutil.copyfile(A/'code/exact_checks.py',W/'code/exact_checks.py')
shutil.copyfile(A/'inputs/exact-checks.json',W/'inputs/exact-checks.json')
p=subprocess.run(['python','code/exact_checks.py'],cwd=W,capture_output=True,text=True)
(W/'logs/exact-checks.log').write_text(p.stdout+p.stderr);assert p.returncode==0
assert (W/'evidence/exact-checks-output.json').read_bytes()==(A/'evidence/exact-checks-output.json').read_bytes()
finite=json.loads((W/'evidence/exact-checks-output.json').read_text());assert finite['assertions']==1945
shutil.copyfile(A/'P05.1-paper.tex',W/'P05.1-paper.tex')
commands=[]
for i in [1,2]:
    args=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex']
    p=subprocess.run(args,cwd=W,capture_output=True,text=True)
    log=W/f'logs/build-pass-{i}.log';log.write_text(p.stdout+p.stderr)
    commands.append(dict(argv=args,exit_code=p.returncode,log=str(log)));assert p.returncode==0
args=['pandoc','-f','latex','-t','gfm','--wrap=none','P05.1-paper.tex','-o','argument.md']
p=subprocess.run(args,cwd=W,capture_output=True,text=True)
(W/'logs/pandoc.log').write_text(p.stdout+p.stderr);assert p.returncode==0
assert (W/'argument.md').read_bytes()==(A/'argument.md').read_bytes()
assert sha(W/'P05.1-paper.tex')==sha(A/'P05.1-paper.tex')==sha(D/'P05.1-paper.tex')
shutil.copyfile(W/'P05.1-paper.pdf',D/'P05.1-paper.pdf')
diagnostics=[]
for cmd in commands:
    lines=Path(cmd['log']).read_text().splitlines()
    diagnostics.append([line for line in lines if any(k in line for k in ['Warning','Overfull','Underfull','undefined','Error'])])
info=subprocess.run(['pdfinfo',str(D/'P05.1-paper.pdf')],capture_output=True,text=True,check=True).stdout
(W/'logs/pdfinfo.txt').write_text(info)
binding=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),original='P05.1',continuation=291,source=str(D/'P05.1-paper.tex'),source_sha256=sha(D/'P05.1-paper.tex'),source_LF_lines=source.count('\n'),argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=sha(D/'P05.1-paper.pdf'),exact_FINAL=str(E/'exact-native-final.json'),exact_FINAL_sha256=sha(E/'exact-native-final.json'),exact_FINAL_candidate=False,exact_FINAL_notes=6,saved_notes_text_adds_only_one_terminal_newline_each=True,parent_child_input_semantically_equal=True,author_artifact_bindings_verified=len(manifest),math_bindings_verified=33,primary_bindings_verified=4,ROOT_source_whole_read=True,ROOT_ledger_scope_build_whole_read=True,ROOT_exact_FINAL_all_six_whole_read=True,ROOT_safe_exact_checker_whole_read=True,ROOT_finite_output_exact=True,finite_assertions=1945,finite_scope_only=True,latex_to_markdown_exact=True,local_build_exit_codes=[c['exit_code'] for c in commands],local_build_diagnostics=diagnostics,source_unchanged=True,only_grants=['A224','B225','R230','S262','S272'],all_clarifications_retained=True,new_ROOT286287288289290_not_supplied=True,new_S282_acceptance_not_a_grant=True,mathematical_acceptance=False,original_closed=False,protected_editor_unchanged_open=True)
write(D/'root-reproduction-binding-20261008.json',binding)
print(json.dumps(binding,indent=2))
