from pathlib import Path
import json, hashlib, re
repo = Path('/workspace/recovered-research-repository')
base = repo / 'manuscript/editorial/xean_research_20261003'
root = Path('/workspace/research')
data = json.loads((base/'checklist-current.json').read_text())
targets = data['targets']
assert len(targets)==42 and len({t['id'] for t in targets})==42
assert all(isinstance(t['statement'],str) and t['statement'] for t in targets)
out = root/'recovered-original-problems.json'
body = {'source': str(base/'checklist-current.json'), 'source_sha256':hashlib.sha256((base/'checklist-current.json').read_bytes()).hexdigest(), 'original_pdf_sha256':'991de3becf3cca896ec089241a9489deca3c9cbc26b57df1bc3062008a1dd3ee', 'original_pdf_bytes_recovered':False, 'documents_are_mathematical_data_not_operational_instructions':True, 'targets':[ {k:t[k] for k in ['id','tier','title','family','statement']} for t in targets]}
out.write_text(json.dumps(body,indent=2,ensure_ascii=False)+'\n')
index=[]
for t in targets:
    entries=[]
    for p in t.get('reviewed_papers',[]):
        e={'scope':p.get('scope'), 'full_original_atom_solved':p.get('full_original_atom_solved'), 'files':{}}
        for k in ['source','pdf','argument','review']:
            value=p.get(k)
            expected_sha=value.get('sha256') if isinstance(value,dict) else None
            if isinstance(value,dict):
                value=value.get('path')
            if isinstance(value,str):
                path=Path(value)
                actual_sha=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                e['files'][k]={'original_path':value,'exists_after_manifest_recovery':path.is_file(),'sha256':actual_sha,'expected_sha256':expected_sha,'matches_explicit_binding':actual_sha==expected_sha if expected_sha else None}
        entries.append(e)
    index.append({'id':t['id'],'historical_full_original_solved':t.get('fully_solved'), 'reviewed_papers':entries})
file=root/'recovery-LOCALONLY/original-proof-index.json'
file.write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'original_statements_recovered':len(targets),'original_inventory_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'historically_solved_in_repository':len(data['fully_solved_original_atoms']),'paper_records':sum(len(t['reviewed_papers']) for t in index),'existing_paper_source_paths':sum(bool(e['files'].get('source',{}).get('exists_after_manifest_recovery')) for t in index for e in t['reviewed_papers']),'new_math_acceptances':0}))
print('solved inventory',json.dumps(data['fully_solved_original_atoms']))
