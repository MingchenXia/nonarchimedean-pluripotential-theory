from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');D=R/'root-checks/public-P12.3-continuation401-toric-weight-envelopes-and-primary-correction-obstruction-unreviewed'
q=D/'ROOT-whole-proof-source-scope-and-binding.json';b=json.loads(q.read_text())
assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='pending'
for e in b['public_files']:assert hashlib.sha256(Path(e['path']).read_bytes()).hexdigest()==e['sha256']
result=dict(path=str(D/'P12.3-audit-and-toric-envelopes.tex'),kind='success',message="The current source compiled successfully with the desktop editor's compiler.")
p=R/'root-checks/ROOT401-native-editor-compiler-success-20261009.json'
p.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),compiler_result=result,source_sha256=hashlib.sha256(Path(result['path']).read_bytes()).hexdigest(),mathematical_certification=False,protected_editor_OPEN_UNCHANGED=True),indent=2)+'\n')
b['compiler']=dict(result,actual_ROOT_copy_compilation_verified=True,record=str(p));b['recorded_utc']=datetime.now(timezone.utc).isoformat();q.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(binding=str(q),compiler=result,accepted=False,original_closed=False)))

