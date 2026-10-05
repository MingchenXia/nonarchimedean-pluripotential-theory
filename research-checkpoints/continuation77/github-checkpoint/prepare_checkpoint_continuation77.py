"""Publish completed round68 evidence and the frozen smooth weak successor."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation77-publication-records'
assert not D.exists()
receipt=json.loads((G/'push-receipt-continuation76.json').read_text())
assert receipt['commit_sha']=='8e6f5f0ccb9309925d5a2283dea39ed6f6ad09ca'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat();D.mkdir()
C=R/'campaigns/round-70/P16.1-public-source-smooth-weak-globalization-open-trace-and-unibranch-equation'
m=json.loads((C/'input-manifest.json').read_text());inp=json.loads((C/'input.json').read_text())
assert sha(C/'input.json')==m['input_sha256'] and sha(C/'settings.json')==m['settings_sha256']
assert inp['notes']==[] and len(m['public_sources'])==10 and len(m['embedded_context'])==15
for s in m['public_sources']:assert sha(s['pdf'])==s['pdf_sha256'] and sha(s['literal_extract'])==s['extract_sha256']
for b in m['embedded_context']:assert sha(b['path'])==b['sha256'] and Path(b['path']).read_text() in inp['assignment']
S=Path(m['new_source_read_record']).parent;sr=json.loads((S/'source-read-record.json').read_text())
assert len(sr['units'])==7
for u in sr['units']:
    assert sha(u['source'])==u['source_sha256'] and sha(u['literal_file'])==u['literal_sha256']
    first,last=u['inclusive_one_based_LF']
    assert '\n'.join(Path(u['source']).read_bytes().decode().split('\n')[first-1:last])==Path(u['literal_file']).read_text()
reader=R/'root-checks/public-P16.1-round-68-final-reader'
rs=json.loads((reader/'root-preservation-and-read-state-continuation77.json').read_text())
assert rs['whole_argument_root_read'] and rs['all_four_actual_canonical_notes_root_read']
assert rs['candidate'] is False and rs['literal_excerpts']==84 and rs['primary_files_hash_bound']==23
assert sha(reader/'P16.1-argument.md')==rs['argument_sha256']
assert sha(reader/'P16.1-paper.tex')==rs['tex_sha256'] and sha(reader/'P16.1-paper.pdf')==rs['pdf_sha256']
items=[]
for atom,roundno,stem,role,db,session in [
    ('P13.1',63,'P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation-original-review','complete original correctness review','review.sqlite',None),
    ('P16.1',70,C.name,'author','campaign.sqlite',24247)
]:
    c=R/'campaigns'/('round-'+str(roundno))/stem
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/(atom+'-native-status.json');p.write_text(proc.stdout)
    items.append({'atom':atom,'round':roundno,'role':role,'directory':str(c),'tool_session_id':session,
        'observed_status':json.loads(proc.stdout)['status'],'status':str(p),'status_sha256':sha(p),
        'settings_sha256':sha(c/'settings.json'),'accepted':False})
assert len([i for i in items if i['observed_status']=='running'])<=2
batch={'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
write(D/'current-small-batch-observation.json',batch)
successor={'round':70,'directory':str(C),'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],
    'source_count':10,'embedded_diagnostic_body_count':15,'new_literal_source_units':7,'launched':True,
    'launch_tool_session_id':24247,'saved_new_prefix_settings_and_unchanged_completion_criteria_root_read':True,
    'inherited_prefix_byte_identical_to_previous_root_read':True,'new_proposal_whole_root_read':True,
    'new_proposal_independently_reviewed':False,'original_task_unchanged':True,'round69_preserved_unlaunched':True}
write(D/'P16.1-round70-launch-and-input-bindings.json',successor)
completion={'round':68,'candidate':False,'frozen_reader':str(reader),
    'actual_result':str(R/'root-checks/P16.1-round68-actual-result-20261005.json'),
    'actual_result_sha256':rs['actual_result_sha256'],'argument_sha256':rs['argument_sha256'],
    'tex_sha256':rs['tex_sha256'],'pdf_sha256':rs['pdf_sha256'],
    'all_four_notes_and_whole_proof_root_read':True,'accepted_scoped_paper':False,
    'fully_solved_original_atom':False,'new_math_review':'NOT_LAUNCHED',
    'native_compile':'Requested in cell53; result pending at this checkpoint preparation',
    'concrete_gaps':json.loads((reader/'status.json').read_text())['concrete_gaps']}
write(D/'P16.1-round68-completion-and-native-compile-pending.json',completion)
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint77: completed candidate=false68 proof/paper/provenance, unreviewed smooth weak proposal, seven actual source units and active70. No new accepted original.'
a['selected_atoms']=['P13.1','P16.1'];a['current_small_batch']=batch
a['P16.1_round68_author_completion']=completion;a['prepared_P16.1_round70']=successor
a['continuation77_unreviewed_root_proposal']={'path':m['embedded_context'][-1]['path'],
    'sha256':m['embedded_context'][-1]['sha256'],'source_read_record':str(S/'source-read-record.json'),
    'independently_reviewed':False,'originals_solved':[]}
a['next_work']='Read the actual complete P13.1 original review when published; reconstruct the smooth weak/open-trace and singular Runge/envelope/equation chain in active P16.1 round70. Keep at most two active mathematical targets and push concrete evidence regularly.'
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=batch
c['active_atoms']=['P13.1','P16.1']
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation77/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S,reader]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
for n in ['input.json','settings.json','input-manifest.json']:add(C/n)
for p in [Path(m['embedded_context'][-1]['path']),R/'prepare_public_P16_1_smooth_weak_trace_repair_20261005.py',
    R/'prepare_public_P16_1_round68_reader_20261005.py',R/'root-checks/P16.1-round68-actual-result-20261005.json',
    G/'push-receipt-continuation76.json',G/'prepare_checkpoint_continuation77.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation77.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,
    'historical_reviewed_scoped_papers':40,'current_native_batch':items,
    'commit_message':'Preserve singular bounded mass draft and smooth weak trace reconstruction',
    'scope':'Actual completed candidate=false68 full proof,20-page author paper,84 literal units/23 source bindings; unreviewed smooth weak proposal and seven actual units; active native70 and complete-original review63. No private transcripts, SQL, auth, Git database or book source edits.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':3},indent=2))
