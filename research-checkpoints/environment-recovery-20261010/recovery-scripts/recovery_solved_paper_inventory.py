from pathlib import Path
import json, hashlib
repo=Path('/workspace/recovered-research-repository')
base=repo/'manuscript/editorial/xean_research_20261003'
data=json.loads((base/'checklist-current.json').read_text())
rows=[]
for t in data['targets']:
    if t['id'] not in data['fully_solved_original_atoms']:
        continue
    candidates=[]
    for p in Path('/workspace/research/deliverables').glob('original-'+t['id']+'/*.tex'):
        candidates.append(str(p))
    for r in t.get('reviewed_papers',[]):
        p=r.get('source')
        if isinstance(p,dict):
            p=p.get('path')
        if isinstance(p,str) and Path(p).is_file():
            candidates.append(p)
    rows.append({'id':t['id'],'historical_solved':True,'candidate_sources':list(dict.fromkeys(candidates)),'reviewed_paper_records':len(t.get('reviewed_papers',[])),'new_acceptance':False})
out=Path('/workspace/research/recovery-LOCALONLY/solved-paper-inventory.json')
out.write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows))
