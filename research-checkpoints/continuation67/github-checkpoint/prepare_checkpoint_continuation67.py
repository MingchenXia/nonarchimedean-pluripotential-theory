"""Freeze new direct FS/trace proposals and the unlaunched exact-domain repair."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation67-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads((G/'push-receipt-continuation66.json').read_text())
assert receipt['commit_sha']=='ce752475f89f4d106168f59292c02f1ff6e91f8a'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert not D.exists();D.mkdir()
C=R/'campaigns/round-57/P16.1-public-source-direct-FS-trace-and-unibranch-equation'
m=json.loads((C/'input-manifest.json').read_text());inp=json.loads((C/'input.json').read_text())
assert sha(C/'input.json')==m['input_sha256']=='4f0bba9e9e4f29e4ca8f89aa682a09ef619ae665729a99f1853ce77c0668aa6a'
assert sha(C/'settings.json')==m['settings_sha256']=='8b8b187851950be00b6aca4a64b60ad619ee28c3e3cff982b0c14d2473d5e746'
assert not (C/'campaign.sqlite').exists() and inp['notes']==[]
assert inp['task']==json.loads((R/'campaigns/round-56/P16.1-public-source-noncircular-local-extension-unibranch-equation/input.json').read_text())['task']
for s in m['public_sources']:
 assert sha(s['pdf'])==s['pdf_sha256'] and sha(s['literal_extract'])==s['extract_sha256']
for e in m['embedded_context']:
 assert sha(e['path'])==e['sha256'] and not e['accepted_dependency']
 assert '\n## '+e['kind']+'\n\n'+Path(e['path']).read_text()+'\n' in inp['assignment']
follow=R/'root-checks/P16.1-round56-reader-followup-continuation67'
f=json.loads((follow/'read-and-build-followup.json').read_text())
assert f['whole_argument_root_read'] and f['whole_tex_root_read']
assert f['first_and_last_actual_pdf_pages_visually_root_read']
assert [x['returncode'] for x in f['root_tex_passes']]==[0,0]
assert f['native_editor_compilation'].startswith('UNVERIFIED')
now=datetime.now(timezone.utc).isoformat()
reads=R/'root-checks/continuation67-primary-trace-curve-and-weak-reads'
assert not reads.exists();reads.mkdir()
units=[]
WAN=R/'shared-sources/Wanner-1801.04713v3-20261004.txt'
WU=R/'shared-sources/new-primary-2609.27610v1-20261004.txt'
for label,source,version,a,b,limit in [
 ('Wanner-continuous-psh-subharmonic-complete-proof',WAN,'1801.04713v3',1096,1608,'Whole Theorem4.7 proof read; standing complete algebraically closed nontrivial scope separately bound in checkpoint66; not whole article.'),
 ('Wu-connected-fiber-descent-and-constant-sign',WU,'2609.27610v1',566,638,'Complete Proposition2.24/Lemma2.25 proof; printed -m phi sign must be corrected for phi<=0.'),
 ('Wu-affine-FS-projective-correspondence',WU,'2609.27610v1',800,847,'Selected correspondence proof and decreasing restriction; not entire section.'),
 ('Wu-localization-statement-and-initial-proof',WU,'2609.27610v1',1766,1841,'Selected preceding hull/radial statements and5.10 statement/initial proof only; not full5.10/5.11 proof.'),
 ('Wu-weak-definition-and-smooth-base',WU,'2609.27610v1',1868,1930,'Exact weak upper-growth definition, smooth-base proof and6.3 statement; indispensable replacements remain unreviewed.'),
]:
 p=reads/(label+'.txt');p.write_text('\n'.join(source.read_text().split('\n')[a-1:b]))
 units.append({'id':label,'source':str(source),'source_version':version,'source_sha256':sha(source),'LF_one_based_inclusive':[a,b],'extract':str(p),'extract_sha256':sha(p),'exact_selected_body_root_read':True,'whole_primary_body_root_read':False,'scope_and_limits':limit})
(reads/'source-read-record.json').write_text(json.dumps({'recorded_utc':now,'line_convention':'UTF-8 read_text().split("\\n"), inclusive one-based LF','units':units,'mathematical_claims_independently_reviewed':False},ensure_ascii=False,indent=2)+'\n')
items=[]
for atom,roundno,stem,role,db,session in [
 ('P13.1',55,'P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation','author','campaign.sqlite',92187),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2','correctness review','review.sqlite',3702),
]:
 directory=R/'campaigns'/('round-'+str(roundno))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':roundno,'role':role,'directory':str(directory),'tool_session_id':session,'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
obs=D/'current-small-batch-observation.json'
obs.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','items':items,'next_prepared_round':57,'next_task_launched':False,'hot_feedback_sent':False},indent=2)+'\n')
prepared={'round':57,'atom':'P16.1','directory':str(C),'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],'original_task_unchanged':True,'notes_imported':[],'source_count':6,'embedded_diagnostic_bodies':10,'saved_task_assignment_prefix_and_settings_root_read':True,'embedded_whole_bodies_already_root_read_and_byte_reproduced':True,'state':'PREPARED LOCAL ONLY; not launched. Preserve current two-item native batch.','fully_solved_original_atom':False}
(D/'round57-preparation-and-binding.json').write_text(json.dumps(prepared,indent=2)+'\n')
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint67: three unreviewed direct FS/trace/curve proposals, round56 whole-reader and two clean builds, five literal units and prepared six-primary-source round57 repair. No new original closure.'
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items,'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['prepared_P16.1_round57']=prepared
a['P16.1_round56_repair']['reader_followup']=str(follow/'read-and-build-followup.json')
a['continuation67_unreviewed_root_proposals']={'paths':[str(p) for p in sorted((R/'root-checks').glob('*-20261004-continuation67.md'))],'source_read_record':str(reads/'source-read-record.json'),'independently_reviewed':False,'new_originals_solved':[]}
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch_launch']=str(obs);c['current_small_batch_launch_sha256']=sha(obs)
for t in c['targets']:
 if t['id']=='P16.1':t['current_focus']='Round57 original-domain repair prepared, not launched; direct real-log FS approximation, determinant finite-flat trace and curve boundary/slicing-independence proposals unreviewed. Original remains open.'
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file();files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation67/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,reads,follow]:
 for p in sorted(directory.rglob('*')):
  if p.is_file():add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['input.json','settings.json','input-manifest.json']:add(C/name)
for p in sorted((R/'root-checks').glob('*-20261004-continuation67.md')):add(p)
for p in [R/'prepare_public_P16_1_direct_trace_repair_20261005.py',G/'push-receipt-continuation66.json',G/'prepare_checkpoint_continuation67.py']:add(p)
assert len({f['path'] for f in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,'historical_reviewed_scoped_papers':40,'current_native_batch':items,'commit_message':'Develop direct affine FS trace and curve boundary repairs; prepare exact unibranch reconstruction','scope':'Three unreviewed mathematical proposals; completed partial reader and two fresh local TeX passes with native service unverified; five exact primary units; round57 six-source repair prepared but unlaunched. No new accepted paper/original closure; no private transcripts, SQL, credentials, Git databases or book-source changes.'}
p=G/'upload-manifest-continuation67.json';assert not p.exists();p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),'originals_solved':3,'reviewed_scoped_papers':40,'statuses':[(x['atom'],x['observed_status']) for x in items]},indent=2))
