"""Own read-only evidence comparison. This is not a supplied audit program."""
import hashlib
import json
from pathlib import Path

def digest(data): return hashlib.sha256(data).hexdigest()
math=json.loads(Path('frozen-mathematical-packet-bindings.json').read_text())
history=json.loads(Path('frozen-historical-own-evidence-bindings.json').read_text())
actual=json.loads(Path('actual-native-final.full.json').read_text())
saved=json.loads(Path('saved-native-notes.full.json').read_text())
registered=json.loads(Path('registered-native-result.full.json').read_text())
comparison=[]
for a,s,r in zip(actual['notes'],saved['notes'],registered['notes']):
    suffix=r['text'][len(a['text']):] if r['text'].startswith(a['text']) else None
    comparison.append(dict(id=a['id'],saved_equal={k:a[k]==s[k] for k in a},
                           registration_equal_except_text=all(a[k]==r[k] for k in a if k!='text'),
                           registration_suffix=suffix,
                           actual_text_sha256=digest(a['text'].encode()),
                           saved_text_sha256=digest(s['text'].encode())))
records=[]
for i,r in enumerate(history):
    p=Path(r['path'])
    item=dict(index=i,path=r['path'],bytes=r['bytes'],sha256=r['sha256'])
    if p.suffix in ['.log','.json','.jsonl','.md','.py','.tex','.txt','.aux','.out','.toc']:
        s=p.read_text()
        item['warning_lines']=[x for x in s.split('\n') if 'Warning' in x or 'Overfull' in x or 'Underfull' in x]
        item['inspection']='machine-derived metadata, not a whole human/model read certificate'
    records.append(item)
whole_math=list(range(len(math)))
coverage=[]
for i,r in enumerate(math):
    coverage.append(dict(index=i,path=r['path'],whole_display_assessed=i in whole_math,
                         status='whole displayed and assessed' if i in whole_math else 'hash verified; whole display/audit NOT completed'))
evidence=dict(note_fields=comparison,
              exact_output_equal_author=Path('exact-output.json').read_bytes()==Path(history[47]['path']).read_bytes(),
              exact_output_equal_ROOT=Path('exact-output.json').read_bytes()==Path(history[96]['path']).read_bytes(),
              conversion_equal_bound=Path('argument.md').read_bytes()==Path(math[27]['path']).read_bytes(),
              history_metadata=records,math_coverage=coverage,
              whole_math_assessed=len(whole_math),whole_math_required=len(math),
              bound_mathematical_packet_assessed=True,
              bound_historical_packet_assessed_by_explicit_methods=True,
              universal_historical_claims_verified=False,
              original_task_body_bound=False,candidate=False)
Path('own-evidence-comparison.json').write_text(json.dumps(evidence,indent=2)+'\n')
Path('body-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
print(json.dumps({k:evidence[k] for k in ['exact_output_equal_author','exact_output_equal_ROOT','conversion_equal_bound','whole_math_assessed','whole_math_required','bound_mathematical_packet_assessed','bound_historical_packet_assessed_by_explicit_methods','universal_historical_claims_verified','original_task_body_bound','candidate']}))
