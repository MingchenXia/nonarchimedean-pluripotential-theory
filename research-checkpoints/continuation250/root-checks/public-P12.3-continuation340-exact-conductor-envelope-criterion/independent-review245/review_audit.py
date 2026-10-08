"""Owned, inert standard-library input audit. Never executes supplied code."""
import hashlib,json,pathlib,platform,sys
BASE=pathlib.Path('/workspace/research/campaigns/round-245/P12.3-geometric-envelope-whole-proof-source-scope-and-conductor-criterion-review')
HERE=pathlib.Path(__file__).resolve().parent
def digest(b): return hashlib.sha256(b).hexdigest()
def dump(p,o): p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
(HERE/'evidence').mkdir(exist_ok=True)
(HERE/'review-data').mkdir(exist_ok=True)
rows=[]
for manifest in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json']:
    mb=(BASE/manifest).read_bytes(); data=json.loads(mb)
    rows.append(dict(kind='manifest',path=str(BASE/manifest),bytes=len(mb),sha256=digest(mb)))
    (HERE/'review-data'/manifest).write_bytes(mb)
    for row in data:
        b=pathlib.Path(row['path']).read_bytes()
        rows.append(dict(kind=manifest,path=row['path'],bytes=len(b),sha256=digest(b),expected_bytes=row['bytes'],expected_sha256=row['sha256'],match=len(b)==row['bytes'] and digest(b)==row['sha256']))
for name in ['original-task.json','qualified-imported-note-bindings.json','author-reader-qualifications.json','settings.json','freeze.json','launch-record.json']:
    b=(BASE/name).read_bytes(); rows.append(dict(kind='control',path=str(BASE/name),bytes=len(b),sha256=digest(b)))
    (HERE/name).write_bytes(b)
current=json.loads((HERE/'input.json').read_text())
math=BASE/'immutable-mathematical-DATA'; ev=BASE/'immutable-evidence-DATA'
grant=json.loads((math/'07-G331-qualified-grant.json').read_text())
(HERE/'G331-qualified-grant.json').write_bytes((math/'07-G331-qualified-grant.json').read_bytes())
for src,dst in [('08-G331-mandatory-source-scope.json','G331-mandatory-source-scope.json'),('09-G331-source-application-ledger.md','G331-source-application-ledger.md'),('10-G331-exact-scope.md','G331-exact-scope.md')]:
    (HERE/dst).write_bytes((math/src).read_bytes())
objects={n:json.loads((ev/n).read_text()) for n in ['00-input.json','07-input.json']}
actual=json.loads((math/'11-round242-actual-native-final.json').read_text())
expanded=json.loads((math/'06-native-notes.json').read_text())
for label,o in [('actual242',actual),('expanded242',expanded)]:
    for note in o['notes']:
        (HERE/'review-data'/f'{label}-{note["id"]}.txt').write_text(json.dumps(note,ensure_ascii=False,indent=2)+'\n')
comparisons={
 'historical_controller_native_decoded_whole_equal':objects['00-input.json']==objects['07-input.json'],
 'current_grant_whole_equal_bound_grant':current['notes'][0]==grant,
 'historical_controller_grant_whole_equal_bound_grant':objects['00-input.json']['notes'][0]==grant,
 'actual_expanded_whole_equal':actual==expanded,
 'actual_candidate':actual['candidate'],'expanded_candidate':expanded['candidate'],
 'per_note':[dict(id=a['id'],whole_equal=a==b,summary_equal=a['summary']==b['summary'],detailedSummary_equal=a['detailedSummary']==b['detailedSummary'],text_equal=a['text']==b['text'],actual_support=a['support'],expanded_support=b['support'],actual_text_bytes=len(a['text'].encode()),expanded_text_bytes=len(b['text'].encode())) for a,b in zip(actual['notes'],expanded['notes'])],
}
dump(HERE/'input-bindings.json',rows)
dump(HERE/'evidence'/'decoded-comparisons.json',comparisons)
original=json.loads((HERE/'original-task.json').read_text())
ct=objects['00-input.json']['task']
encoded=(json.dumps(ct,ensure_ascii=False,indent=2)+'\n').encode()
(HERE/'review-data'/'native242-reconstructed-saved-original-task.json').write_bytes(encoded)
saved_own=json.loads((ev/'09-own-bindings.json').read_text())
saved_inputs=json.loads((ev/'08-input-bindings.json').read_text())
available={}
for man in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json']:
    for row in json.loads((BASE/man).read_text()):available[row['origin']]=row
matched=[]; unavailable=[]
native_root='/workspace/research/campaigns/round-242/P12.3-original-geometric-singular-envelope-positivity-and-regularity/artifacts/codex-lnKQHd/'
expanded_by_id={n['id']:n for n in expanded['notes']}
for row in saved_own['records']:
    mapped=available.get(native_root+row['path'])
    if mapped:
        bb=pathlib.Path(mapped['path']).read_bytes()
    elif row['path'] in [f'{i}.md' for i in expanded_by_id]:
        bb=expanded_by_id[row['path'][:-3]]['text'].encode()
    elif row['path']=='original-task.json':bb=encoded
    else: unavailable.append(row['path']);continue
    matched.append(dict(path=row['path'],match=len(bb)==row['bytes'] and digest(bb)==row['sha256']))
freeze=json.loads((ev/'02-freeze.json').read_text())
grant_binding=json.loads((HERE/'qualified-imported-note-bindings.json').read_text())[0]
audit=dict(
 exact_original_bytes=len((HERE/'original-task.json').read_bytes()),exact_original_sha256=digest((HERE/'original-task.json').read_bytes()),
 original_problem_is_full_prefix=ct['problem'].startswith(original['problem']),
 augmented_completion_original_is_prefix=ct['completionCriteria'].startswith(original['completionCriteria']),
 actual_original_whole_equal_augmented_task=original==ct,
 reconstructed_author_saved_original_bytes=len(encoded),reconstructed_author_saved_original_sha256=digest(encoded),
 reconstruction_equals_frozen_augmented_task_hash=digest(encoded)==freeze['task_sha256'],
 reconstruction_equals_exact_original_hash=digest(encoded)==freeze['original_task_sha256'],
 saved_own_verified=matched,saved_own_not_available=unavailable,
 saved_input_record_count=len(saved_inputs['records']),saved_input_declared_all_match=all(r['match'] for r in saved_inputs['records']),
 qualified_grant_text_binding_match=len(grant['text'].encode())==grant_binding['text_bytes'] and digest(grant['text'].encode())==grant_binding['text_sha256'],
 expanded_bodies_exact_in_argument=[dict(id=n['id'],match=n['text'] in (math/'01-argument.md').read_text()) for n in expanded['notes']],
 scope='Checks only available inert bytes, reconstructed standard JSON, and declared old inventories. No missing origin path followed; no provider attestation.')
dump(HERE/'evidence'/'historical-inventory-audit.json',audit)
dump(HERE/'evidence'/'environment.json',dict(python=sys.version,platform=platform.platform(),cwd=str(HERE),no_network=True,no_supplied_code_execution=True,model='caller requested native gpt-6.1-sol xhigh; no provider attestation',heavy_compute='not needed; no supervised facility exposed'))
print(json.dumps(dict(bound_count=sum('match' in r for r in rows),all_match=all(r.get('match',True) for r in rows),comparisons=comparisons),indent=2))
