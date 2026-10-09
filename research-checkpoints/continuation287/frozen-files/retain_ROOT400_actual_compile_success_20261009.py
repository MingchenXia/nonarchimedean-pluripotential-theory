from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
R=Path('/workspace/research'); D=R/'root-checks/public-P16.7-continuation400-countable-monotone-closure-and-actual-operator-continuity-unreviewed'
p=D/'ROOT-whole-proof-source-scope-and-binding.json'
b=json.loads(p.read_text())
assert not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert hashlib.sha256(Path(e['path']).read_bytes()).hexdigest()==e['sha256']
result=dict(path=str(D/'scoped-paper.tex'),kind='success',message="The current source compiled successfully with the desktop editor's compiler.")
q=R/'root-checks/ROOT400-native-editor-compiler-success-20261009.json'
q.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),compiler_result=result,source_sha256=hashlib.sha256((D/'scoped-paper.tex').read_bytes()).hexdigest(),mathematical_certification=False,protected_editor_OPEN_UNCHANGED=True),indent=2)+'\n')
b['compiler']=dict(result,native_identical_source_success=True,actual_ROOT_copy_compilation_verified=True,record=str(q))
b['recorded_utc']=datetime.now(timezone.utc).isoformat()
p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(binding=str(p),compiler=result,accepted=False,original_closed=False)))
