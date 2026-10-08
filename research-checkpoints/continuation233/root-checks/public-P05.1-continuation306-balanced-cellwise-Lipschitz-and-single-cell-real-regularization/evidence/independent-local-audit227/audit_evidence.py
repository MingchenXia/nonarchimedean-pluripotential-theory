"""Fresh immutable-evidence inspection; never executes a supplied runner."""
import hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent
rows = json.loads((ROOT/'frozen-bindings-verified.json').read_text())
ev = [r for r in rows if r['kind']=='evidence']
def data(r):
    b = pathlib.Path(r['path']).read_bytes()
    assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
    return b
def warning_rows(b):
    return [{'LF':i,'text':s} for i,s in enumerate(b.decode(errors='replace').split('\n'),1)
            if 'Warning' in s or 'Overfull' in s or 'Underfull' in s or s.startswith('!')]
result = {'scope':'Supplied immutable own artifacts only; no universal past-operation certificate', 'historical_runs':[]}
for n in range(1,7):
    token=f'/run-{n:03}/'
    subset=[r for r in ev if token in r['path']]
    reportrow=next(r for r in subset if r['path'].endswith('/build-report.json'))
    report=json.loads(data(reportrow))
    entry={'run':n, 'report':report, 'passes':[]}
    for p in [1,2,3]:
        r=next(r for r in subset if r['path'].endswith(f'/pass{p}.log'))
        b=data(r)
        entry['passes'].append({'pass':p,'sha256':r['sha256'],'warnings':warning_rows(b),
          'output_lines':[s for s in b.decode(errors='replace').split('\n') if 'Output written' in s or 'shell escape' in s or 'write18' in s]})
    snaps=[r for r in subset if r['path'].endswith('/prior-paper.tex')]
    entry['prior_snapshots']=[{'sha256':r['sha256'],'bytes':r['bytes']} for r in snaps]
    result['historical_runs'].append(entry)
root=[]
for p,i in [(1,93),(2,95),(3,97)]:
    r=next(r for r in ev if r['index']==i)
    root.append({'pass':p,'sha256':r['sha256'],'warnings':warning_rows(data(r))})
result['ROOT_passes']=root
# Check only bindings to files actually supplied here. Never follow old paths.
artrow=next(r for r in ev if r['index']==2)
art=json.loads(data(artrow))
result['artifact_binding_top_type']=type(art).__name__
result['artifact_binding_top_keys']=list(art) if isinstance(art,dict) else None
actualrow=next(r for r in rows if r['kind']=='math' and r['index']==32)
savedrow=next(r for r in ev if r['index']==1)
actual=json.loads(data(actualrow));saved=json.loads(data(savedrow))
result['actual_candidate']=actual['candidate'];result['saved_candidate']=saved['candidate']
result['actual_saved_field_equality']=[{'id':a['id'],'fields':{k:a[k]==s[k] for k in a}} for a,s in zip(actual['notes'],saved['notes'])]
result['actual_note_count']=len(actual['notes']);result['saved_note_count']=len(saved['notes'])
result['ROOT_comparison_prose_read_claim']=json.loads(data(next(r for r in ev if r['index']==80)))['whole_saved_prose_ROOT_read_claimed']
result['all_bound_files_verified']=all(r['match'] for r in rows)
result['counts']={k:sum(r['kind']==k for r in rows) for k in ['math','evidence','primary']}
(ROOT/'historical-evidence-report.json').write_text(json.dumps(result,indent=2)+'\n')
for e in result['historical_runs']:
    r=e['report']
    print('RUN',e['run'],'exits',[c.get('exit_code') for c in r.get('commands',[])], 'TeX',r.get('tex_sha256_before_build'), 'warning-counts',[len(x['warnings']) for x in e['passes']])
    for x in e['passes']:
        for w in x['warnings']:
            if 'Overfull' in w['text']: print('  ',x['pass'],w)
print('ROOT warning-counts',[len(x['warnings']) for x in root])
print('artifact bindings structure',result['artifact_binding_top_type'],result['artifact_binding_top_keys'])
print('actual/saved notes',result['actual_note_count'],result['saved_note_count'])
