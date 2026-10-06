from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation133.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='7ebd61e715488b22cac1961105ef4be8c58a6420'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation133.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-moving-series-quadratic-contraction-and-coercivity-draft-20261006-continuation161.md',
       K/'P16.5-general-big-moving-series-output-dual-finiteness-draft-20261006-continuation162.md',
       K/'P16.5-general-big-cross-moment-Holder-and-uniform-floor-tails-draft-20261006-continuation163.md']
for round,label,db in [(126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite'),
                      (128,'P16.5-general-big-entire-genuine-E1-operator-independent-review','review.sqlite')]:
    c=R/f'campaigns/round-{round}'/label
    freeze=json.loads((c/'freeze.json').read_text())
    for name in ['settings.json','input.json' if round==126 else 'argument.md']:
        key='settings_sha256' if name=='settings.json' else 'input_sha256' if round==126 else 'argument_sha256'
        assert sha(c/name)==freeze[key]
    assert not (c/db).exists()
S=K/'current-small-batch124-125-20261006-continuation134'; S.mkdir(exist_ok=False)
public={}
for round,label in [(124,'P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review'),
                    (125,'P16.5-entire-nef-big-variational-equation-independent-review')]:
    db=R/f'campaigns/round-{round}'/label/'review.sqlite'
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(r.stdout)
    assert status['status']=='running' and status['work']['active']==1
    assert status['work']['completed']==0 and status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    p=S/f'P16.5-round{round}-public-native-status.json';save(p,status)
    public[round]={'path':str(p),'sha256':sha(p),'observed_utc':status['observedAt'],
                   'whole_public_compact_status_root_read_at_freeze':False}
now=datetime.now(timezone.utc).isoformat()
P=K/'P16.5-moving-system-Fujita-and-bounded-ample-Holder-primary-scope-observation-20261006.json'
save(P,{'recorded_utc':now,'imports':[
    {'primary_url':'https://arxiv.org/pdf/math/0608260v2',
     'authors':['Sebastien Boucksom','Charles Favre','Mattias Jonsson'],
     'whole_pertinent_units_root_read':['Proposition1.5 proof L511--516','Lemma2.2 and Proposition2.3 proofs L595--635','Definition2.5 and Lemmas2.6/2.7 whole proofs L650--708','Theorem3.1 ordinary Fujita statement and characteristic-zero algebraic field scope'],
     'scope':'Ordinary algebraic positive products, compact directed-order limits and imported Fujita approximation. Complete-system cofinality is derived in own161/162.',
     'application':'Auxiliary complete moving parts and their intersection limits; no nonample equation grant.'},
    {'primary_url':'https://arxiv.org/abs/1801.08229v4','authors':['Sebastien Boucksom','Mattias Jonsson'],
     'local_frozen_text_sha256':'659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0',
     'whole_pertinent_units_root_read':['Lemma7.30 complete proof and comparison identities LF4180--4332','Theorem7.34 and Lemma7.36 complete proofs LF4330--4465'],
     'scope':'Apply Lemma7.30 only to bounded model potentials in actual auxiliary ample A_m+epsilon H_m on smooth X_m; take epsilon to zero for fixed m using finite polynomials.',
     'application':'Own163 dimension-uniform bounded nef cross moment, then original-carrier lsc transfer.'}],
    'all_recursive_background_foundations_reproved':False,'extended_primary_transcripts_uploaded':False})
binding={'recorded_utc':now,
    'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
    'scope':'Own161 complete moving-series intersections and a missing-rank flag trace prove quadratic relative energy contraction, intrinsic target integrability equivalence and coercivity. Own162 fixed original lsc tests transfer bounded nef cross moments to finite intrinsic output dual energy on the entire genuine cone. Own163 proves Holder cross moments, uniform fixed-test relative floor tails, and finite-divisorial maximizing output measures weakly approaching every intrinsic target. No mixed nonnef operator, joint weighted continuity, full comparison, weak target continuity, metric completeness, arbitrary-target attainment or all-E1 uniqueness.',
    'independently_accepted':False,'original_closed':False,
    'all_recursive_background_foundations_reproved':False,
    'current_native_small_batch':public,'prepared_native_launch_order':[126,128],
    'active_or_prepared_native_inputs_modified':False,'hot_feedback_sent':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
B=K/'P16.5-root-continuation161-163-whole-proofs-and-exact-scope-binding-20261006.json';save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    assert [item['round'] for item in data['current_small_batch']['items']]==[124,125]
    data.update({'updated_utc':now,'continuation161_163_general_big_coercivity_output_dual_candidate':binding,
                 'github_pending_checkpoint':'continuation134 frozen'})
    batch=data['current_small_batch'];batch['recorded_utc']=now
    for item in batch['items']:
        s=public[item['round']]
        item.update({'public_status':s['path'],'public_status_sha256':s['sha256'],'observed_status':'running','observed_utc':s['observed_utc']})
    batch['active_items']=list(batch['items'])
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t')
        cols[2]='Original123 PARTIAL; independent124/125 active. General-big143--163 unreviewed: entire genuine relative energy/operator, finite-divisorial variational attainment/uniqueness, rooftop metric, model-envelope uniqueness, full polar nullness, strong target integration, quadratic energy contraction/coercivity, output dual finiteness, Holder moments and uniform fixed-test floor tails. Original126/complete scoped128 prepared. Mixed products, joint weighted continuity, comparison, weak target continuity/completeness, arbitrary-target attainment and all-E1 unique inverse remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation134-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,'new_unreviewed_support':[161,162,163],
    'current_native_small_batch':[124,125],'prepared_next_native_launch_order':[126,128],'original_closed':False,
    'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation134/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,P,previous,R/'record_verified133_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation134.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':47,
    'commit_message':'Record moving-series general-big coercivity, output dual energy and uniform tails',
    'scope':binding['scope']+' All new mathematics unreviewed. Seven originals solved,35open,47 independently accepted scoped papers.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[124,125],
    'next_launches':[126,128],'originals_solved':7,'originals_open':35},indent=2))
