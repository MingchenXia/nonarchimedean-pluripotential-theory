"""Own integrity/support audit. This is not mathematical verification."""
import hashlib,json,pathlib,sys

ROOT=pathlib.Path(__file__).resolve().parent
payload=json.loads((ROOT/'native-notes.json').read_text())
seen={'G331','B341'}
for note in payload['notes']:
    assert note['id'] not in seen
    assert set(note['support'])<=seen
    assert all(isinstance(note[k],str) and note[k] for k in ['id','summary','detailedSummary','text'])
    seen.add(note['id'])
assert payload['candidate'] is True and payload['notes'][-1]['id']=='n9'
request=json.loads((ROOT/'input.json').read_text())
original=request['task']['problem'].partition('ROOT AUTHORIZED WHOLE ORIGINAL RECONSTRUCTION')[0]
assert (ROOT/'original-problem.txt').read_text()==original
tex=(ROOT/'P12.5-paper.tex').read_text()
for incoming in request['notes']:
    grant=(ROOT/'inputs'/'grants'/(incoming['id']+'-qualified.txt')).read_text()
    assert grant==incoming['text'] and grant in tex
for rec in json.loads((ROOT/'reports'/'input-hashes.json').read_text()):
    body=(ROOT/rec['local']).read_bytes()
    assert len(body)==rec['bytes'] and hashlib.sha256(body).hexdigest()==rec['sha256']
diag=json.loads((ROOT/'reports'/'exact-diagnostics.json').read_text())
assert diag['status']=='PASS' and diag['total_assertion_cases']==21520
assert not json.loads((ROOT/'reports'/'tex-generation.json').read_text())['compilation']
records=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and 'inputs' not in path.relative_to(ROOT).parts and path.name not in ['artifact-hashes.json','final-audit.json']:
        body=path.read_bytes();records.append({'path':str(path.relative_to(ROOT)),'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()})
(ROOT/'reports'/'artifact-hashes.json').write_text(json.dumps(records,indent=2)+'\n')
result={'status':'PASS','bound_inputs':52,'notes':len(payload['notes']),'support_order_valid':True,'original_unchanged':True,'full_grants_embedded_verbatim':True,'finite_cases':21520,'compiler_run':False,'artifact_files_hashed':len(records),'mathematical_verification':False,'independent_review_and_ROOT_reading':'still required'}
(ROOT/'reports'/'final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
