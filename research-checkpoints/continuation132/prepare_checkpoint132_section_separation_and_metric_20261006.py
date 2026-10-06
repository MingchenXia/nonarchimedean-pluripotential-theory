from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation131.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='29ad1cbe2b42b6bfa9d200bea21fd8917f47f493'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation131.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-uniform-half-order-outer-error-and-cubic-root-stability-draft-20261006-continuation154.md',
       K/'P16.5-general-big-genuine-rooftop-pseudometric-and-fast-chain-barriers-draft-20261006-continuation155.md',
       K/'P16.5-general-big-actual-section-separation-and-genuine-rooftop-metric-draft-20261006-continuation156.md']
for round,label,db in [
    (126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite'),
    (128,'P16.5-general-big-entire-genuine-E1-operator-independent-review','review.sqlite')]:
    c=R/f'campaigns/round-{round}'/label
    freeze=json.loads((c/'freeze.json').read_text())
    for name in ['settings.json','input.json' if round==126 else 'argument.md']:
        key='settings_sha256' if name=='settings.json' else 'input_sha256' if round==126 else 'argument_sha256'
        assert sha(c/name)==freeze[key]
    assert not (c/db).exists()
S=K/'current-small-batch124-125-20261006-continuation132'
S.mkdir(exist_ok=False)
public={}
for round,label in [
    (124,'P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review'),
    (125,'P16.5-entire-nef-big-variational-equation-independent-review')]:
    db=R/f'campaigns/round-{round}'/label/'review.sqlite'
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(r.stdout)
    assert status['status']=='running' and status['work']['active']==1
    assert status['work']['completed']==0 and status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    p=S/f'P16.5-round{round}-public-native-status.json';save(p,status)
    public[round]={'path':str(p),'sha256':sha(p),'observed_utc':status['observedAt'],'whole_public_compact_status_root_read':False}
now=datetime.now(timezone.utc).isoformat()
P=K/'P16.5-DXZ2025-primary-comparison-scope-observation-20261006.json'
save(P,{'recorded_utc':now,'primary_url':'https://ems.press/content/serial-article-files/50355',
        'doi':'10.4171/CMH/586','title':'A transcendental approach to non-Archimedean metrics of pseudoeffective classes',
        'authors':['Tamas Darvas','Mingchen Xia','Kewei Zhang'],'published_year':2025,
        'source_scope':'Compact complex Kahler manifolds; numerical comparison for actual projective complex bundles.',
        'whole_pertinent_primary_units_root_read':[
            {'unit':'Theorem3.14 and entire proof','renderer_lines':[2663,2764]},
            {'unit':'Energy definition34, finiteness convention, and Theorem3.17','renderer_lines':[2890,3026]},
            {'unit':'Theorem4.14 and entire proof','renderer_lines':[3863,4148]}],
        'limited_comparison':'Published complex ray theory identifies its psh objects with the genuine algebraic cone and approximates its finite-energy rays by flag configurations. Its energy agrees with the standard algebraic energy in the ample case. Equality with the present general-big section-volume energy and an original-carrier big-class operator/inverse cannot be inferred from these statements alone.',
        'whole_book_or_recursive_proof_verification_claimed':False,
        'imported_as_general_big_operator_or_inverse_grant':False,'used_in_own154_156_proofs':False,
        'extended_primary_transcript_uploaded':False})
binding={'recorded_utc':now,
         'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
         'scope':'Own154 affine product-class positive-product pairings yield a uniform |t|^(3/2) outer error and cubic-root ordered measure stability. Own155 proves the genuine rooftop/max energy inequality, pseudometric triangle/nonexpansion and fast-chain lower barriers. Own156 actual-L section approximation at finite model constraints plus a uniform high-weight section rank proves strict ordered energy separation, all-point rooftop metric separation and normalized divisorial-plus-energy metric convergence. No weighted integration, comparison, output dual energy, completeness or all-target inverse.',
         'independently_accepted':False,'original_closed':False,
         'all_recursive_background_foundations_reproved':False,
         'current_native_small_batch':public,'prepared_native_launch_order':[126,128],
         'active_or_prepared_native_inputs_modified':False,'hot_feedback_sent':False,
         'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
B=K/'P16.5-root-continuation154-156-whole-proofs-and-exact-scope-binding-20261006.json';save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    assert [item['round'] for item in data['current_small_batch']['items']]==[124,125]
    data.update({'updated_utc':now,'continuation154_156_general_big_section_separation_and_metric_candidate':binding,
                 'github_pending_checkpoint':'continuation132 frozen'})
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
        cols[2]='Original123 PARTIAL; independent124/125 active. General-big143--156 unreviewed: entire genuine relative energy/operator, finite-divisorial attainment, reference/polar barriers, quantitative outer derivatives, rooftop metric triangle and actual-section energy separation. Original126/complete scoped128 prepared. Weighted integration, comparison, output dual energy, completeness, all-target coercivity and unique inverse remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation132-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
                               'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,
                               'new_unreviewed_support':[154,155,156],'current_native_small_batch':[124,125],
                               'prepared_next_native_launch_order':[126,128],'original_closed':False,
                               'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation132/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,P,previous,R/'record_verified131_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation132.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
        'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
        'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
        'historical_reviewed_scoped_papers':47,
        'commit_message':'Record actual-section energy separation and general-big rooftop metric',
        'scope':binding['scope']+' All new mathematics unreviewed. Seven originals solved,35open,47 independently accepted scoped papers.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[124,125],
                  'next_launches':[126,128],'originals_solved':7,'originals_open':35},indent=2))
