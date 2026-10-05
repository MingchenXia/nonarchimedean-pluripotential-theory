from pathlib import Path
import hashlib
import json

r = Path(__file__).resolve().parent
checks = []
def check(name,condition):
    checks.append({'check':name,'passed':bool(condition)})
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
o = json.loads((r/'input.json').read_text())
check('byte-identical original input',(r/'input.json').read_bytes()==(r/'input-original.json').read_bytes())
check('assignment value preservation',(r/'assignment-original.txt').read_text()==o['assignment'])
check('task value preservation',json.loads((r/'task-original.json').read_text())==o['task'])
p = json.loads((r/'source-extracts/source-provenance.json').read_text())
for s in p['sources']:
    for typ,v in s['local_files'].items(): check(s['saved_version']+' '+typ+' hash',sha(r/v['path'])==v['sha256'])
    lines = (r/s['local_files']['literal_extract']['path']).read_bytes().decode('utf-8').split('\n')
    for e in s['excerpts']:
        literal = '\n'.join(lines[e['start_lf_1based']-1:e['end_lf_1based_inclusive']])
        check(e['artifact']+' LF content',literal==e['literal']==(r/e['artifact']).read_text())
        check(e['artifact']+' hash',hashlib.sha256(literal.encode()).hexdigest()==e['sha256'])
status = json.loads((r/'status.json').read_text())
check('exact five-key status schema',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('honest partial status',status['status']=='partial' and bool(status['concrete_gaps']))
notes=json.loads((r/'canonical-notes.json').read_text())
check('at most four notes',len(notes['notes'])<=4)
check('no completion claimed',notes['candidate'] is False)
seen=set()
for n in notes['notes']:
    check(n['id']+' earlier-only support',set(n['support'])<=seen)
    seen.add(n['id'])
for b in json.loads((r/'build-results.json').read_text()):
    check('build '+b['stdout'],b['returncode']==0)
    check('saved output '+b['stdout'],(r/b['stdout']).exists() and (r/b['stderr']).exists())
    if b['tex_log']: check('saved TeX log '+b['tex_log'],(r/b['tex_log']).exists())
check('standalone TeX', '\\documentclass' in (r/'P16.1-paper.tex').read_text())
check('PDF produced',(r/'P16.1-paper.pdf').read_bytes().startswith(b'%PDF'))
payload={'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),'input_sha256':sha(r/'input.json'),'pdf_sha256':sha(r/'P16.1-paper.pdf'),'mathematical_verdict':None,'limits':'These checks establish preservation and rerunnability, not mathematics or novelty.'}
(r/'verification.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:payload[k] for k in ['passed','total','input_sha256','pdf_sha256']}))
assert payload['passed']==payload['total']
