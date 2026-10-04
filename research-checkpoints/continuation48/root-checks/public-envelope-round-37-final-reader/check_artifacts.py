#!/usr/bin/env python3
"""Administrative reproducibility checks, not a mathematical verifier."""
import hashlib
import json
from pathlib import Path

checks=[]
def check(label,condition):
    checks.append({'check':label,'passed':bool(condition)})
    if not condition:raise AssertionError(label)

status=json.loads(Path('status.json').read_text())
check('exact status keys',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('honest partial status',status['id']=='P03.1' and status['status']=='partial' and bool(status['concrete_gaps']))
check('input bytes preserved',Path('input.json').read_bytes()==Path('input-original.json').read_bytes())
inp=json.loads(Path('input.json').read_text())
check('assignment preserved',Path('assignment-original.txt').read_text()==inp['assignment'])
check('task preserved',json.loads(Path('task-original.json').read_text())==inp['task'])
packet=json.loads(Path('canonical-notes.json').read_text())
check('at most four notes',0<len(packet['notes'])<=4)
seen=[]
for i,n in enumerate(packet['notes'],1):
    check('local note id '+str(i),n['id']=='n'+str(i))
    check('nonempty note fields '+n['id'],all(n[k] for k in ['summary','detailedSummary','text']))
    check('support only earlier local IDs '+n['id'],set(n['support'])<=set(seen))
    seen.append(n['id'])
check('candidate false for unresolved original target',packet['candidate'] is False)
tex=Path('P03.1-paper.tex').read_text()
check('standalone TeX',r'\begin{document}' in tex and r'\end{document}' in tex and r'\input{' not in tex)
check('both new obstruction sections embedded','codimension-two pinching' in tex and 'nonsplit-node surface' in tex)
execution=json.loads(Path('execution.json').read_text())
check('two actual successful TeX builds',len(execution['commands'])==2 and all(x['exit_code']==0 for x in execution['commands']))
check('no model invocations',execution['additional_models_or_workers_invoked'] is False)
check('no mathematical certificate claimed',execution['mathematical_verification'] is False)
check('PDF exists',Path('P03.1-paper.pdf').exists())
for name,key in [('input.json','input_sha256'),('P03.1-argument.md','argument_sha256'),('P03.1-paper.tex','tex_sha256'),('P03.1-paper.pdf','pdf_sha256')]:
    check('execution hash '+name,hashlib.sha256(Path(name).read_bytes()).hexdigest()==execution[key])
provenance=json.loads(Path('source-provenance.json').read_text())
check('five primary sources',len(provenance['sources'])==5)
for source in provenance['sources']:
    for selection in source['retained_extracts']:
        file=Path(selection['file'])
        check('literal extract '+file.name,hashlib.sha256(file.read_bytes()).hexdigest()==selection['sha256'])
check('PDF check transcriptions retained',Path('source-extracts/checked-applications.md').exists())
Path('artifact-checks.json').write_text(json.dumps({'kind':'administrative checks only','checks':checks,'all_passed':True},indent=2)+'\n')
print(len(checks),'administrative checks passed. Mathematical correctness is not certified.')
