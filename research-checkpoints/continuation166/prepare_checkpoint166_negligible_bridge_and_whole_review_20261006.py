from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
prior=json.loads((G/'push-receipt-continuation165.json').read_text())
assert prior['commit_sha']=='15097e35c1ccc41e82e2e2304f0b4ea5abc1ccdd'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
D=K/'public-P16.5-round160-partial-negligible-transfer-reader'
b=json.loads((D/'publication-binding.json').read_text())
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256'] and b['whole_final_tex_root_read']
assert b['actual_visual_pages']==[1,3,5,7,9] and b['native_compile_success_observed'] and not b['independent_acceptance']
S=K/'small-batch158161-public-status-20261006-continuation166';S.mkdir()
items=[]
for n in (158,161):
    C=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';save(p,st)
    items.append({'round':n,'atom':'P16.5','directory':str(C),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Entire actual foundation158 audit and independent whole159/160/201/202 finite/scalar/conditional bridge audit161. No hot feedback between reviews.'}
F=G/'continuation166-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==59 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_scalar_negligible_big_pole160=b,github_pending_checkpoint='continuation166 frozen',goal_state='8/42 originals solved;34 open;59 accepted supporting papers. Completed1609-page unreviewed single-net scalar foundations and exact ample-negligible-to-actual-big-pole transfer, conditional outer-nullness. Four whole159/160/201/202 manuscripts (40 pages) now independently reviewed in161; actual foundation158 remains under separate review. All actual energy/output antecedents, all simultaneously unbounded physical weighted independence and further nonzero zero-volume range remain open. Native LaTeX success observed for four current sources, editor unchanged.')
    for target in j.get('targets',[]):
        if target['id']=='P16.5':
            target['current_focus']='Independent foundation158 audit plus whole40-page bridge audit161. New160 exact single-net scalar closure and all-point ample negligible-to-big-pole section transfer; measure nullness conditional on energy/contraction and all-test integrability.159 conditional arbitrary-target attainment/every-solution uniqueness;201 conditional strict Borel comparison;202 conditional genuine mixed map and canonical weighted continuity. Full actual energy/output/moving antecedents and every simultaneously unbounded physical weighted system remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P16.5':
        row[2]='New160 unreviewed single-net scalar closure and exact negligible-to-actual-big-pole bridge; conditional outer-nullness. Entire40-page159/160/201/202 bridge audit161 and actual foundation158 audit active. All actual energy/output/moving antecedents and all unbounded physical weighted independence open.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'completed_unreviewed_author':160,'pages':9,'new_original_closure':None,'new_independent_acceptance':None,'active_batch':[x['round'] for x in active],'whole_bridge_review_pages':40,'active_private_outputs_read':False,'hot_feedback_sent':False,'native_compiler_success_observed':True,'native_compile_cells':['469','502','468','492'],'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation166/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for p in sorted(D.iterdir()):
    if p.suffix in ('.tex','.pdf','.json','.md'):add(p)
for folder in ('public-P16.5-round159-partial-conditional-attainment-reader','public-P16.5-continuation201-strict-Borel-comparison-reader','public-P16.5-continuation202-genuine-mixed-measures-reader'):
    add(K/folder/'publication-binding.json')
for name in ('P16.5-round160-actual-canonical-author-result-20261006.json','P16.5-round160-completed-partial-root-reading-and-scope-record-20261006.json','P16.5-native-compile-success-receipts-159160201202-20261006.json'):
    add(K/name)
C=R/'campaigns/round-161/P16.5-conditional-attainment-negligible-Borel-mixed-independent-review'
for name in ('task.json','settings.json','argument.md','freeze.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for p in (G/'push-receipt-continuation165.json',R/'record_verified165_20261006.py',R/'prepare_conditional_bridge_review161_20261006.py',R/'launch_frozen_conditional_bridge_review161_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation166.json'
save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Preserve negligible-to-big-pole bridge and launch whole conditional audit','scope':'Completed1609-page unreviewed exact single-net scalar closure and all-point ample negligible-to-original big-pole transfer, conditional outer-nullness for every non-Borel negligible subset.161 fresh independent review of all40 pages159/160/201/202; actual foundation158 separate review ongoing. Four current native LaTeX compilations succeeded.8/42 originals and59 supporting papers unchanged; no new acceptance, no active private output read or hot feedback. Entire actual energy/output/moving antecedents and every simultaneously unbounded physical weighted system remain open.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'public_states':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
