from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-211').iterdir());A=C/'artifacts/codex-sTEhTQ'
D=K/'public-P16.4-continuation279-higher-dimensional-stability-and-maximizing-output-limits'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
final=K/'P16.4-round211-exact-native-model-final-unreviewed-stability-20261007.json'
native=json.loads(final.read_text());assert not native['candidate'] and native==json.loads((A/'native-notes.json').read_text())
inspection=json.loads((K/'round211-settled-inspection-LOCALONLY.json').read_text());registered=inspection['campaign']['result']
assert inspection['campaign']['status']=='completed' and not registered['candidate']
assert len(native['notes'])==len(registered['notes'])==4
for a,b in zip(native['notes'],registered['notes']):
    for key in ['id','summary','detailedSummary','support']:assert a[key]==b[key]
    assert b['text']==a['text']+'\n\nArtifacts: '+str(A)
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
author=json.loads((A/'artifact-hashes.json').read_text());assert isinstance(author,list)
for e in author:assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
D.mkdir();E=D/'evidence';E.mkdir();S=E/'root-reproduction';S.mkdir()
for name in ['P16.4-paper.tex','P16.4-argument.md','source-application-ledger.md','scope-and-gaps.md','native-notes.json','finite_checks.py','finite-inputs.json','finite-output.json','build_deliverable.py','build-result.json','commands.json','environment.json','whole-body-read-ranges.json','primary-read-units.json','binding-audit.json','artifact-hashes.json']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(final,E/'exact-native-final.json');write(E/'registered-native-worker-result.json',registered)
shutil.copyfile(A/'finite_checks.py',S/'finite_checks.py');runs=[]
def run(argv,cwd,stem):
    p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True)
    (S/(stem+'.stdout.txt')).write_text(p.stdout);(S/(stem+'.stderr.txt')).write_text(p.stderr)
    runs.append(dict(argv=argv,cwd=str(cwd),exit_code=p.returncode,stdout=str(S/(stem+'.stdout.txt')),stderr=str(S/(stem+'.stderr.txt'))));assert p.returncode==0
run(['python',str(S/'finite_checks.py')],S,'finite-checks')
for name in ['finite-inputs.json','finite-output.json']:assert (S/name).read_bytes()==(A/name).read_bytes()
run(['pandoc','--from=markdown+tex_math_single_backslash',str(D/'P16.4-argument.md'),'--standalone','--number-sections','-o',str(S/'P16.4-paper.tex')],S,'markdown-conversion')
assert (S/'P16.4-paper.tex').read_bytes()==(D/'P16.4-paper.tex').read_bytes()
for i in [1,2]:run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],D,f'local-pass{i}')
diagnostics=[l for l in (D/'P16.4-paper.log').read_text(errors='replace').splitlines() if any(w in l for w in ['Warning:','Overfull','Underfull','! '])];assert not diagnostics
info=subprocess.run(['pdfinfo',str(D/'P16.4-paper.pdf')],capture_output=True,text=True,check=True).stdout
pages=int(next(l for l in info.splitlines() if l.startswith('Pages:')).split(':')[1]);assert pages==9
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P16.4',continuation=279,author_round=211,source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=len((D/'P16.4-paper.tex').read_text().splitlines()),argument=str(D/'P16.4-argument.md'),argument_sha256=sha(D/'P16.4-argument.md'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=pages,full_tex_argument_ledger_scope_four_registered_notes_ROOT_read=True,exact_native_FINAL_equals_saved_author_notes=True,exact_registered_suffix_checked=True,whole_26_math_62_primary_byte_bindings_match=True,whole_62_primary_read_claimed=False,finite_reproduction_exact=True,coefficient_rows=136,formal_defect_grid_rows=1089,grid_not_actual_metrics=True,markdown_to_tex_exact=True,root_commands=runs,local_build_exit_codes=[0,0],local_diagnostics=diagnostics,builtin_compile_not_yet_requested=True,mathematical_acceptance=False,original_closed=False,scope='New whole unreviewed higher-dimensional stability/mixed-measure rigidity and canonical intrinsic weak maximizing-output limit; no inverse, lambda=target, actual maximizer or every-point potential uniqueness.',protected_editor_unchanged_open=True)
write(D/'root-reproduction-binding-20261007.json',record)
(D/'README.md').write_text('Unreviewed continuation279: higher-dimensional stability and maximizing-output limits\n\nThe original P16.4 remains open. This draft proves energy-defect/PL-measure estimates, mixed-measure rigidity and a canonical intrinsic limit of maximizing outputs. It does not identify that limit with every target, produce an actual maximizing potential or prove every-point potential uniqueness. ROOT read the whole source/argument/ledger/scope and four exact native notes, checked26 mathematical/62primary bindings, reproduced136 exact coefficient rows and1089 formal grid rows, exact markdown conversion and two clean local builds. No mathematical acceptance follows from these acts. Complete independent mathematical/source review follows. Protected editor stays unchanged; no new tab.\n')
print(json.dumps({k:record[k] for k in ['source','source_sha256','argument_sha256','pdf_sha256','pdf_pages','mathematical_acceptance','original_closed']},indent=2))
