from pathlib import Path
import json,hashlib

root=Path(__file__).resolve().parent
d=json.loads((root/'input.json').read_bytes())
checks=[]
def check(name,result):
    assert result,name
    checks.append(name)
check('byte-identical original input',(root/'input.json').read_bytes()==(root/'input-original.json').read_bytes())
check('unchanged task value',json.loads((root/'task-original.json').read_text())==d['task'])
check('unchanged assignment value',(root/'assignment-original.txt').read_text()==d['assignment'])
status=json.loads((root/'status.json').read_text())
check('exact status keys',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('partial status',status['status']=='partial')
notes=json.loads((root/'canonical-notes.json').read_text())
check('candidate is false',notes['candidate'] is False)
check('at most four notes',len(notes['notes'])<=4)
seen=set()
for note in notes['notes']:
    check('canonical keys '+note['id'],set(note)=={'id','summary','detailedSummary','text','support'})
    check('backward support '+note['id'],set(note['support'])<=seen)
    seen.add(note['id'])
prov=json.loads((root/'source-extracts/source-provenance.json').read_text())
for source in prov['sources']:
    raw=(root/source['copy']).read_bytes()
    check('source hash '+source['id'],hashlib.sha256(raw).hexdigest()==source['sha256'])
    for f in source['primary_files']:
        check('primary copy '+source['id']+' '+f['kind'],hashlib.sha256((root/f['copy']).read_bytes()).hexdigest()==f['sha256'])
for excerpt in prov['excerpts']:
    record=next(s for s in prov['sources'] if s['id']==excerpt['id'].split('-')[0])
    lines=(root/record['copy']).read_bytes().decode('utf-8').split('\n')
    a,b=excerpt['inclusive_one_based_LF'];expected='\n'.join(lines[a-1:b]).encode()
    raw=(root/excerpt['literal_file']).read_bytes()
    check('inclusive LF '+excerpt['id'],raw==expected and excerpt['literal']==expected.decode())
    check('excerpt hash '+excerpt['id'],hashlib.sha256(raw).hexdigest()==excerpt['literal_sha256'])
build=json.loads((root/'build-report.json').read_text())
check('three successful build commands',len(build['results'])==3 and all(r['returncode']==0 for r in build['results']))
for r in build['results']:
    check('build outputs retained '+r['label'],(root/r['stdout']).exists() and (root/r['stderr']).exists())
    if r['pass_log']:check('distinct TeX pass log '+r['label'],(root/r['pass_log']).exists())
for name,record in build['artifacts'].items():
    check('built artifact hash '+name,hashlib.sha256((root/name).read_bytes()).hexdigest()==record['sha256'])
report={'all_passed':True,'count':len(checks),'checks':checks,'finite_checks':json.loads((root/'finite-checks.json').read_text())['counts'],
        'input_sha256':hashlib.sha256((root/'input.json').read_bytes()).hexdigest(),
        'epistemic_limit':'Preservation, provenance and execution observations only; no certification of mathematics.'}
Path('validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'all_passed':True,'artifact_checks':len(checks),'finite_counts':report['finite_checks']}))
