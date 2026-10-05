#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
def read(p): return json.loads((root/p).read_text())
def digest(b): return hashlib.sha256(b).hexdigest()
checks=[]
def check(name,value):
    checks.append({'check':name,'pass':bool(value)})
    assert value,name
check('byte-identical original input',(root/'input.json').read_bytes()==(root/'input-original.json').read_bytes())
x=read('input.json')
check('unchanged task',read('task-original.json')==x['task'])
check('unchanged assignment',(root/'assignment-original.txt').read_text()==x['assignment'])
status=read('status.json')
check('exact status schema',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
notes=read('canonical-notes.json'); seen=set()
check('at most four notes',0<len(notes)<=4)
for i,n in enumerate(notes,1):
    check('note schema '+n['id'],set(n)=={'id','summary','detailedSummary','text','support'})
    check('canonical local ID '+n['id'],n['id']=='n'+str(i))
    check('backward supports '+n['id'],set(n['support'])<=seen)
    check('nonempty full note '+n['id'],len(n['text'])>1000)
    seen.add(n['id'])
check('candidate false',read('result.json')['candidate'] is False)
check('result notes match',read('result.json')['notes']==notes)
prov=read('source-extracts/source-provenance.json')
sources={s['id']:s for s in prov['sources']}
for s in prov['sources']:
    for f in s['files']:
        check('local primary hash '+f['local_copy'],digest((root/f['local_copy']).read_bytes())==f['sha256']==f['expected_sha256'])
for e in prov['units']:
    f=next(f for f in sources[e['source']]['files'] if '-literal_extract.' in f['local_copy'])
    lines=(root/f['local_copy']).read_bytes().decode('utf-8').split('\n')
    a,b=e['inclusive_LF']; literal='\n'.join(lines[a-1:b]).encode()
    check('inclusive LF literal '+e['id'],literal==(root/e['artifact']).read_bytes()==e['literal'].encode())
    check('literal hash '+e['id'],digest(literal)==e['sha256'])
build=read('build-report.json')
for c in build['commands']:
    check('successful command '+c['stdout'],c['returncode']==0)
    check('retained command output '+c['stdout'],(root/c['stdout']).exists() and (root/c['stderr']).exists())
for i in [1,2]: check('TeX pass log '+str(i),(root/f'build-logs/pdflatex-pass{i}.log').stat().st_size>0)
for typ in ['tex','pdf']:
    check('standalone '+typ+' hash',digest((root/f'P16.1-paper.{typ}').read_bytes())==build[typ+'_sha256'])
check('finite diagnostics declared',read('finite-checks.json')['total_cases']==4467)
(root/'validation-report.json').write_text(json.dumps({'checks':checks,'total':len(checks),'all_passed':True,
    'limit':'Artifact consistency and finite diagnostics only; no mathematical proof validation.'},indent=2)+'\n')
print(json.dumps({'artifact_checks':len(checks),'all_passed':True,'candidate':False}))
