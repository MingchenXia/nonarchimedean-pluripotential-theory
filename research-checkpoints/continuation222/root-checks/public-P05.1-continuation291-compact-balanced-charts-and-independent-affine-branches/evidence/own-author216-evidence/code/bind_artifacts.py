"""Own fresh-artifact identifiers, excluding the self-referential manifest."""
from pathlib import Path
import hashlib,json
root=Path.cwd(); entries=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name=='artifact-bindings.json' or '.git' in p.parts:
        continue
    raw=p.read_bytes()
    entries.append({'filename':str(p.relative_to(root)),'bytes':len(raw),
                    'sha256':hashlib.sha256(raw).hexdigest(),
                    'local_only':p.relative_to(root).parts[0]=='LOCALONLY'})
out={'workspace':str(root),'candidate':False,
     'meaning':'artifact identity and reproducibility only; unverified mathematical drafts',
     'files':entries,'rerun':['python code/audit_inputs.py','python code/exact_checks.py > logs/exact-checks.log',
                            'python code/build.py','python code/make_notes.py','python code/bind_artifacts.py']}
Path('artifact-bindings.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'files':len(entries),'candidate':False}))
