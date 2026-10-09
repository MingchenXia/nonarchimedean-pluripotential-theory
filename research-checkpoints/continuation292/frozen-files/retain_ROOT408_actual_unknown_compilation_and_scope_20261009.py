from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P12.3-continuation408-canonical-obstacle-filtration-and-finite-generation-envelopes-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
B=D/'ROOT-whole-proof-source-scope-and-binding.json';b=load(B)
assert b['compiler']['kind']=='pending' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
P=D/'P12.3-obstacle-filtration.tex';assert sha(P)=='fe9f3d25b69a62eb2867f3a63f6fa091dbc4e4ee95c70c41208e73a49448cd60'
now=datetime.now(timezone.utc).isoformat()
result=dict(recorded_utc=now,path=str(P),paper=408,sha256=sha(P),kind='unknown',actual_result_observed=True,tool='codex_app.compile_latex_document',attempts=3,message='LaTeX compilation did not complete. Compilation status is unknown; do not change the source based on this result.',source_errors_reported=False,source_changed=False,success_claimed=False,mathematical_certification=False,protected_editor_OPEN_UNCHANGED=True,UNREVIEWED=True,original_closed=False,accepted=False)
Q=D/'ROOT408-actual-native-editor-compiler-unknown-20261009.json';write(Q,result)
scope=D/'ROOT-review-scope.md';s=scope.read_text();assert s.count('Compiler pending.')==1
scope.write_text(s.replace('Compiler pending.','Built-in compiler returned unknown status on three attempts; no source errors were reported, source is preserved unchanged, and successful compilation is NOT claimed.'))
b.update(recorded_utc=now,compiler=dict(kind='unknown',actual_result_observed=True,result_record=str(Q),result_record_sha256=sha(Q),success_claimed=False),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file() and p!=B]);write(B,b)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[282]
    x.update(updated_utc=now,ROOT408_actual_compiler_result=result,next_work='Regular verified NONFORCE checkpoint292 with whole408 and honest compiler unknown qualification. Continue actual original P12.3 residual in frozen284, at mostTWO while282 continues; no count change.');write(p,x)
print(json.dumps(dict(paper=408,source_sha256=sha(P),compiler='unknown',source_preserved=True,files=len(b['public_files'])+1),indent=2))
