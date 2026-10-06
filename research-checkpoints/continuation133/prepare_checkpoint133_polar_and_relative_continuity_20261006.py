from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation132.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='5cccfcf11d8d932d165eef54b9c613816f1ca6e5'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation132.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-model-envelope-fixed-order-trace-and-uniqueness-draft-20261006-continuation157.md',
       K/'P16.5-general-big-output-and-intrinsic-target-full-polar-nullness-draft-20261006-continuation158.md',
       K/'P16.5-general-big-asymptotic-rooftops-and-finite-target-variational-uniqueness-draft-20261006-continuation159.md',
       K/'P16.5-general-big-strong-target-relative-integral-continuity-draft-20261006-continuation160.md']
for round,label,db in [(126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite'),
                      (128,'P16.5-general-big-entire-genuine-E1-operator-independent-review','review.sqlite')]:
    c=R/f'campaigns/round-{round}'/label
    freeze=json.loads((c/'freeze.json').read_text())
    for name in ['settings.json','input.json' if round==126 else 'argument.md']:
        key='settings_sha256' if name=='settings.json' else 'input_sha256' if round==126 else 'argument_sha256'
        assert sha(c/name)==freeze[key]
    assert not (c/db).exists()
S=K/'current-small-batch124-125-20261006-continuation133'; S.mkdir(exist_ok=False)
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
P=K/'P16.5-volume-equality-and-negligible-set-primary-scope-observation-20261006.json'
save(P,{'recorded_utc':now,'imports':[
    {'primary_url':'https://msp.org/ant/2019/13-6/ant-v13-n6-p01-s.pdf',
     'doi':'10.2140/ant.2019.13.1243','authors':['Brian Lehmann','Jian Xiao'],
     'whole_pertinent_units_root_read':['Lemma3.2 proof','Propositions3.3 and3.5 proofs','Proposition3.8 and Theorem3.9 proof','Section2 field statement and Remark3.25'],
     'scope':'Ordinary algebraic big-divisor volume equality identifies proportional numerical divisorial positive parts; smooth projective algebraically closed characteristic-zero domain retained.',
     'application':'Own157 model-envelope uniqueness. No general non-Archimedean inverse imported.'},
    {'primary_url':'https://arxiv.org/abs/1801.08229v4','authors':['Sebastien Boucksom','Mattias Jonsson'],
     'local_frozen_text_sha256':'659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0',
     'whole_pertinent_units_root_read':['Definition5.1 and Theorem5.6 proof (LF2720--2850)','Theorem13.17, Corollary13.18 and Lemma13.19 proofs with capacity support (LF6527--6660)'],
     'scope':'Auxiliary actual ample class only: divisorial points are nonnegligible and characteristic-zero projective negligible sets are pluripolar.',
     'application':'Own160 relative strong integration, using a direct genuine embedding into one auxiliary ample bundle.'}],
    'all_recursive_background_foundations_reproved':False,'extended_primary_transcripts_uploaded':False})
binding={'recorded_utc':now,
    'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
    'scope':'Own157 identifies central fixed-order traces and proves model-envelope operator uniqueness modulo constants using ordinary algebraic volume equality. Own158 proves full pluripolar nullness of output and intrinsic finite-dual targets. Own159 proves shifted-rooftop strong recovery and finite-divisorial variational-maximizer uniqueness on the entire genuine E1 cone. Own160 proves intrinsic-target relative L1 continuity under the genuine rooftop metric. No weighted integration, output dual energy, weak-sublevel target continuity, comparison, completeness, arbitrary-target coercivity or all-E1 operator uniqueness.',
    'independently_accepted':False,'original_closed':False,
    'all_recursive_background_foundations_reproved':False,
    'current_native_small_batch':public,'prepared_native_launch_order':[126,128],
    'active_or_prepared_native_inputs_modified':False,'hot_feedback_sent':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
B=K/'P16.5-root-continuation157-160-whole-proofs-and-exact-scope-binding-20261006.json';save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    assert [item['round'] for item in data['current_small_batch']['items']]==[124,125]
    data.update({'updated_utc':now,'continuation157_160_general_big_polar_and_strong_integration_candidate':binding,
                 'github_pending_checkpoint':'continuation133 frozen'})
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
        cols[2]='Original123 PARTIAL; independent124/125 active. General-big143--160 unreviewed: entire genuine relative energy/operator, finite-divisorial variational attainment/uniqueness, rooftop metric, model-envelope operator uniqueness, full polar nullness and strong relative target integration. Original126/complete scoped128 prepared. Weighted integration, comparison, output dual energy, weak target continuity/completeness, all-target coercivity and all-E1 unique inverse remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation133-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,'new_unreviewed_support':[157,158,159,160],
    'current_native_small_batch':[124,125],'prepared_next_native_launch_order':[126,128],'original_closed':False,
    'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation133/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,P,previous,R/'record_verified132_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation133.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':47,
    'commit_message':'Record general-big model uniqueness, polar nullness and strong target integration',
    'scope':binding['scope']+' All new mathematics unreviewed. Seven originals solved,35open,47 independently accepted scoped papers.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[124,125],
    'next_launches':[126,128],'originals_solved':7,'originals_open':35},indent=2))
