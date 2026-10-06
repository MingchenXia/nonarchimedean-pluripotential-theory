from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,x):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation130.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='ee15585af9645fd48b0d1d17407eac57951e06a2'
assert sha(G/'upload-manifest-continuation130.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-rooftop-energy-and-countable-barriers-draft-20261006-continuation151.md',
       K/'P16.5-general-big-Zariski-and-reference-pole-nullness-draft-20261006-continuation152.md',
       K/'P16.5-general-big-polar-barriers-by-section-tail-counting-draft-20261006-continuation153.md']
C126=R/'campaigns/round-126/P16.5-original-general-big-relative-operator-and-equation-research'
C128=R/'campaigns/round-128/P16.5-general-big-entire-genuine-E1-operator-independent-review'
assert sha(C126/'input.json')=='1c64769676bd26ada2357d53b701bf14499388fcd13d311c55d773943787d76d'
assert sha(C128/'argument.md')=='aea004b853460b8fb5b2709ebda3fc47982b0dc1bff70429ddf88add287e40e4'
assert not (C126/'work.sqlite').exists() and not (C128/'review.sqlite').exists()
S=K/'current-small-batch124-125-20261006-continuation131'
public={}
for round in [124,125]:
    p=S/f'P16.5-round{round}-public-native-status.json';s=json.loads(p.read_text())
    assert s['status']=='running' and s['work']['active']==1 and s['work']['completed']==0
    assert s['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    public[round]={'path':str(p),'sha256':sha(p),'observed_utc':s['observedAt'],'whole_public_compact_status_root_read':True}
b={'recorded_utc':now,'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
   'scope':'Own151 flag intersections/sums yield rooftop energy and countable finite-cost barriers; own152 deficient positive-product moments and B/c tails yield each proper Zariski subset and reference pole nullness; own153 actual products of normalized ample section stages with H0(m(L-beta Omega)) yield a gamma<1/2 integrable spectral tail and a genuine big-class E1 barrier for every original psh pole set. Finite intrinsic relative-dual targets are polar null. Output dual energy, mixed/weighted estimates, comparison and all-target inverse remain open.',
   'independently_accepted':False,'original_closed':False,'all_recursive_background_foundations_reproved':False,
   'primary_algebraic_application':'C1 volume and actual section-volume limits on L-beta Omega in the big cone; all arbitrary-field original hypotheses retained from own143.',
   'current_native_small_batch':public,'prepared_native_launch_order':[126,128],
   'new_notes_in_frozen_native128':False,'active_or_prepared_inputs_modified':False,'hot_feedback_sent':False,
   'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
B=K/'P16.5-root-continuation151-153-whole-proofs-and-exact-scope-binding-20261006.json';save(B,b)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
    assert [i['round'] for i in a['current_small_batch']['items']]==[124,125]
    a.update({'updated_utc':now,'continuation151_153_general_big_rooftops_poles_and_barriers_candidate':b,
              'github_pending_checkpoint':'continuation131 frozen'})
    batch=a['current_small_batch'];batch['recorded_utc']=now
    for item in batch['items']:
        s=public[item['round']];item.update({'public_status':s['path'],'public_status_sha256':s['sha256'],
                                           'observed_status':'running','observed_utc':s['observed_utc']})
    batch['active_items']=list(batch['items'])
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t');cols[2]='Original123 PARTIAL; independent124/125 active. General-big143--153 unreviewed: entire genuine energy/operator/outer derivatives, finite-divisorial attainment, zero-energy separation, minimal recession, rooftops, reference pole nullness and finite-energy barriers for all original psh pole sets. Original126/complete scoped128 prepared; unlaunched127 preserved/superseded. Output dual energy, mixed/weighted/comparison/all-target unique inverse remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation131-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
                               'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,
                               'new_unreviewed_support':[151,152,153],'current_native_small_batch':[124,125],
                               'prepared_next_native_launch_order':[126,128],'original_closed':False,
                               'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation131/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,K/'P16.5-root-continuation151-152-whole-proofs-and-exact-scope-binding-20261006.json',
                previous,R/'record_verified130_and_rooftop_pole_drafts_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation131.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
        'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
        'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
        'historical_reviewed_scoped_papers':47,
        'commit_message':'Record general-big rooftops and finite-energy polar barriers',
        'scope':b['scope']+' All new mathematics unreviewed. Seven originals solved,35open,47 independently accepted scoped papers. Native124125 active; original126 and complete operator128 prepared.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[124,125],
                  'next_launches':[126,128],'originals_solved':7,'originals_open':35},indent=2))
