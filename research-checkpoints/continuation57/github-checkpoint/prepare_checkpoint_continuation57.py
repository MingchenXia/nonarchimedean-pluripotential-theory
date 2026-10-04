"""Freeze final original papers, actual reviews, source checks and the next small batch."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation57-local-records'
now = datetime.now(timezone.utc).isoformat()
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt = json.loads((G / 'push-receipt-continuation56.json').read_text())
assert receipt['commit_sha'] == 'd33321ea81c82c8808e99035a09cb8846b0aee97'
assert receipt['all_file_blob_bindings_verified_remote']
observations = []
for atom, directory, db, session in [
    ('P15.1', R/'campaigns/round-31/P15.1-minimum-reference-finite-energy-original-scope-audit','review.sqlite',48400),
    ('P16.3', R/'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs','campaign.sqlite',99123)]:
    result = subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/db)],cwd='/workspace/xean',capture_output=True,text=True)
    assert result.returncode == 0, result.stderr
    p = D/(atom+'-native-status.json');p.write_text(result.stdout)
    status = json.loads(result.stdout)
    observations.append({'atom':atom,'directory':str(directory),'tool_session_id':session,'observed_status':status['status'],'status':str(p),'status_sha256':sha(p),'input_or_argument_sha256':sha(directory/('argument.md' if atom=='P15.1' else 'input.json')),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
(D/'current-native-batch-observation.json').write_text(json.dumps({'observed_utc':now,'items':observations,'hot_feedback_sent':False},indent=2)+'\n')
a = json.loads((R/'active-work.json').read_text());a['updated_utc']=now;a['github_checkpoint']=receipt;a['current_small_batch']['active_items']=observations
for x in a.get('current_public_P16_characteristic_support_batch',{}).get('campaigns',[]):
    if x.get('atom')=='P16.6':
        x.update({'independently_accepted':True,'original_atom_closed':True,'review_submitted':True,'scope_audit_submitted':True,'original_support_axis_interpretation_independently_pending':False,'state':'Full actual correctness and original-support-axis scope PASS both read; conditional correctness antecedent satisfied; final original paper published with exact T/D hypotheses.'})
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
c=json.loads((R/'checklist-current.json').read_text());c['updated_utc']=now
with (R/'checklist-current.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in c['targets']:w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file();remote=remote or 'research-checkpoints/continuation57/'+str(p.relative_to(R))
    files.append({'local':str(p),'path':remote,'bytes':p.stat().st_size,'sha256':sha(p)})
for atom in ['P15.2','P16.6']:
    for p in sorted((R/'deliverables'/('original-'+atom)).rglob('*')):
        if p.is_file() and p.suffix in ['.tex','.pdf','.json','.md','.log','.txt','.png']:
            add(p,'manuscript/editorial/xean_research_20261003/'+str(p.relative_to(R)))
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for p in sorted((R/'root-checks/BGM-rnaa314-primary-check').iterdir()):add(p)
for name in ['BGM-rnaa314-primary.pdf','BGM-rnaa314-primary.txt']:add(R/'shared-sources'/name)
for directory in [R/'campaigns/round-32/P15.2-minimum-reference-full-mass-operator-original-scope-audit',R/'campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy-review',R/'campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy-original-scope-audit',R/'campaigns/round-31/P15.1-minimum-reference-finite-energy-original-scope-audit']:
    for name in ['task.json','settings.json','argument.md','freeze.json','construction-memo.md']:
        if (directory/name).is_file():add(directory/name)
for name in ['input.json','settings.json','input-manifest.json']:add(R/'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs'/name)
for name in ['publish_original_P15_2_paper_20261004.py','publish_original_P16_6_paper_20261004.py','record_original_closures_P15_2_P16_6_20261004.py','prepare_public_positive_residue_geometry_20261004.py']:add(R/name)
for name in ['push-receipt-continuation56.json','recover_checkpoint_continuation56_bulk.py','finish_checkpoint_continuation56_chunked.py','prepare_checkpoint_continuation57.py','native-continuation56-buffered-push.stderr.txt','bulk-recovery-continuation56/events.jsonl','bulk-recovery-continuation56/final-tree-attempt0.stderr.txt']:add(G/name)
assert len({f['path'] for f in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.2','P16.6'],'remaining_open_atoms':40,'historical_reviewed_scoped_papers':37,'current_native_batch':observations,'scope':'Final two original-scope paper versions, actual complete public review reports, exact source applications, closure ledger and frozen next small batch. Historical evidence preserved. No private transcripts, SQL, credentials, bare Git objects or complete originally uploaded PDF.'}
p=G/'upload-manifest-continuation57.json';assert not p.exists();p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),'fully_solved_original_atoms':payload['fully_solved_original_atoms'],'active_items':[(i['atom'],i['observed_status']) for i in observations]},indent=2))
