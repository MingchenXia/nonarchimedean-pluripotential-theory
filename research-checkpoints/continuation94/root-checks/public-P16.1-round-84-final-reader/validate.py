#!/usr/bin/env python3
"""Artifact consistency checks only; no mathematical validation."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
count=0
def check(v,msg):
    global count
    assert v,msg
    count+=1
def get(f):return json.loads((ROOT/f).read_text())
raw=(ROOT/'input.json').read_bytes()
check(raw==(ROOT/'input-original.json').read_bytes(),'byte preservation')
x=json.loads(raw)
check(get('task-original.json')==x['task'],'exact task')
check((ROOT/'assignment-original.txt').read_text()==x['assignment'],'exact assignment')
for f in get('source-files.json'):
    b=(ROOT/f['path']).read_bytes()
    check(hashlib.sha256(b).hexdigest()==f['sha256'],f['path']+' hash')
    check(len(b)==f['bytes'],f['path']+' bytes')
p=get('source-extracts/source-provenance.json')
for u in p['units']:
    b=(ROOT/u['source_file']).read_bytes();a,z=u['inclusive_LF']
    literal='\n'.join(b.decode('utf8').split('\n')[a-1:z])
    check(hashlib.sha256(b).hexdigest()==u['source_text_sha256'],u['id']+' source hash')
    check(literal==u['literal'],u['id']+' LF equality')
    check(hashlib.sha256(literal.encode()).hexdigest()==u['sha256'],u['id']+' unit hash')
    check((ROOT/u['artifact']).read_bytes()==literal.encode(),u['id']+' retained bytes')
    check(u['url'].startswith(('https://','http://')),u['id']+' primary HTTP evidence')
reg=get('premises.json');indices={p['index'] for p in reg['premises']}
check(indices==set(range(len(indices))),'contiguous nonnegative indices')
check({p['premise'] for p in reg['passages']}==indices,'complete external coverage')
uids={u['id']:u for u in p['units']}
for passage in reg['passages']:
    check(passage['premise']>=0,'nonnegative passage index')
    check(passage['quote'] in uids[passage['unit']]['literal'],'literal quote locator')
notes=get('canonical-notes.json');previous=set()
check(len(notes['notes'])<=4 and not notes['candidate'],'partial canonical notes')
for n in notes['notes']:
    check(n['id']==f'n{len(previous)+1}','native ID sequence')
    check(set(n['support'])<=previous,'backward registered supports')
    check(all(n.get(k) for k in ['summary','detailedSummary','text']),'full note fields')
    previous.add(n['id'])
status=get('status.json')
check(set(status)=={'id','status','exact_result','proof_file','concrete_gaps'},'exact status keys')
check(bool(status['concrete_gaps']),'gaps preserved')
check(get('finite-checks.json')['status']=='pass','declared finite diagnostics')
commands=get('commands.json')
for name in ['pandoc','pdflatex-pass1','pdflatex-pass2']:
    check(any(c['stdout']==f'logs/{name}.stdout' and c['exit_code']==0 for c in commands),name+' succeeded')
for number in [1,2]:
    check((ROOT/f'logs/pdflatex-pass{number}.log').is_file(),'full pass log')
    check('Output written on' in (ROOT/f'logs/pdflatex-pass{number}.log').read_text(),'pass PDF produced')
check((ROOT/'P16.1-paper.pdf').read_bytes().startswith(b'%PDF'),'standalone PDF')
rendered=(ROOT/'proof-rendered.txt').read_text()
check('Original-reference contact lemma' in rendered,'reference lemma rendered')
check(all(f'P16.{i}' in rendered for i in range(1,8)),'full original family rendered')
check('does not prove C1-original' in rendered,'conditional gap rendered')
result={'status':'artifact checks passed','checks':count,'candidate':False,'limit':'No mathematical correctness claim. All proofs remain unverified drafts.'}
(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
