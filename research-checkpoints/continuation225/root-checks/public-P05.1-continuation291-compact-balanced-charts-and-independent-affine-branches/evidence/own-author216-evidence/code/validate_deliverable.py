"""Finite artifact/schema checks only, not mathematical verification."""
import json,hashlib
from pathlib import Path
n=json.loads(Path('native-notes.json').read_text());seen=set()
for row in n['notes']:
    assert set(row['support'])<=seen
    assert row['text'] and row['detailedSummary'] and row['summary']
    seen.add(row['id'])
assert n['candidate'] is False
report=json.loads(Path('evidence/build-report.json').read_text())
assert report['source_sha256_after']==hashlib.sha256(Path('P05.1-paper.tex').read_bytes()).hexdigest()
assert all(x['exit_code']==0 for x in report['commands'])
manifest=json.loads(Path('artifact-bindings.json').read_text())
for row in manifest['files']:
    raw=Path(row['filename']).read_bytes()
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
print(json.dumps({'native_notes':len(n['notes']),'valid_earlier_supports':True,'candidate':False,
                  'artifact_bindings_valid':len(manifest['files']),'build_source_current':True}))
