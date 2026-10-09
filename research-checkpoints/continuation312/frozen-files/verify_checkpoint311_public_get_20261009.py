"""Credential-free public GitHub object verification; no mathematics reading credit."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys

D=Path('/workspace/research/github-checkpoint/api-recovery-continuation311')
P=json.loads((D/'connector-plan.json').read_text());base='https://api.github.com/repos/'+P['repository']
def get(s):
    r=subprocess.run(['curl','--fail','--silent','--show-error','--max-time','20',base+s],capture_output=True,text=True)
    if r.returncode:raise RuntimeError('Public GET failed '+s+': '+r.stderr.strip())
    return json.loads(r.stdout)
def treecheck(j,expected):
    assert not j.get('truncated') and j['sha']==expected
    assert len({e['path'] for e in j['tree']})==len(j['tree'])
    return {e['path']:e for e in j['tree']}
mode=sys.argv[1]
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),repository=P['repository'],branch=P['branch'],mode=mode,expected_tree=P['expected_tree'],manifest_sha256=P['manifest_sha256'],mathematical_reading_credit=False)
if mode=='root':
    cache={}
    def readtree(sha):
        if sha not in cache:cache[sha]=treecheck(get('/git/trees/'+sha),sha)
        return cache[sha]
    for e in P['entries']:
        parts=e['path'].split('/');tree=P['expected_tree']
        for part in parts[:-1]:
            node=readtree(tree)[part];assert node['mode']=='040000' and node['type']=='tree';tree=node['sha']
        node=readtree(tree)[parts[-1]];assert all(node[k]==e[k] for k in ['mode','type','sha'])
    record.update(all_frozen_paths_verified=True,actual_file_bindings=len(P['entries']),actual_trees=len(cache))
elif mode in ['parent','created','final']:
    commit=P['parent'] if mode=='parent' else sys.argv[2]
    if mode!='created':
        head=get('/git/ref/heads/'+P['branch']);assert head['object']['type']=='commit' and head['object']['sha']==commit
    obj=get('/git/commits/'+commit)
    if mode in ['created','final']:assert obj['tree']['sha']==P['expected_tree'] and [x['sha'] for x in obj['parents']]==[P['parent']]
    else:assert obj['tree']['sha']==P['base_tree']
    record.update(ref_verified=mode!='created',commit_sha=commit,tree_sha=obj['tree']['sha'],parents=[x['sha'] for x in obj['parents']])
else:raise ValueError(mode)
(D/('public-GET-'+mode+'-verification.json')).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
