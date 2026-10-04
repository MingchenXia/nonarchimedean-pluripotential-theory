"""Freeze the completed partial repair and the current two-item native batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation66-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads((G/'push-receipt-continuation65.json').read_text())
assert receipt['commit_sha']=='e7427acaabe5c80eaac8b0ebdb44384c041264c5'
assert receipt['all_file_blob_bindings_verified_remote'] and receipt['remote_ref_verified']
assert not D.exists()
D.mkdir()
reader=R/'root-checks/public-P16.1-round-56-final-reader'
preservation=json.loads((reader/'root-preservation-and-read-state-continuation66.json').read_text())
assert preservation['candidate'] is False and preservation['whole_argument_root_read']
assert preservation['literal_excerpts']==40 and preservation['all_literal_excerpts_byte_reproduced']
assert not preservation['all_literal_excerpt_bodies_root_read']
items=[]
for atom,roundno,stem,role,db,session in [
 ('P13.1',55,'P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation','author','campaign.sqlite',92187),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2','correctness review','review.sqlite',3702),
 ('P16.1',56,'P16.1-public-source-noncircular-local-extension-unibranch-equation','completed partial author','campaign.sqlite',56950),
]:
 directory=R/'campaigns'/('round-'+str(roundno))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':roundno,'role':role,'directory':str(directory),'tool_session_id':session,'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
assert items[2]['observed_status']=='completed'
C=Path(items[0]['directory'])
assert sha(C/'input.json')=='fde0115749ccffb7791ccc494ad69284b2f96848cdf68add58978e575aa8cef0'
assert sha(C/'settings.json')=='e84fcfe271b2e983ffa0c1ccef6fed71c641c96f0b744e7d8c7bf6c3cd8b9c06'
now=datetime.now(timezone.utc).isoformat()
(D/'P13.1-round55-launch-route.json').write_text(json.dumps({'recorded_utc':now,'initial_outer_sandbox_launch':'EPERM listening on required native local control socket; before worker admission','authorized_retry':'Exact same frozen native command with outer sandbox escalation, preserving native research sandbox and current account environment','successful_tool_session_id':92187,'auto_review_rejection':False,'provider':'native Codex','model':'gpt-6.1-sol','reasoning':'xhigh'},indent=2)+'\n')
observation=D/'current-small-batch-observation.json'
observation.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items[:2],'completed_partial':items[2],'hot_feedback_sent':False},indent=2)+'\n')
reads=R/'root-checks/continuation66-primary-PL-fiber-and-curve-reads'
assert not reads.exists();reads.mkdir()
CLD=R/'shared-sources/new-primary-1204.6277v2-20261004-continuation64.txt'
GM=R/'shared-sources/GM1608.08030v3-20261004-continuation66.txt'
WU=R/'shared-sources/new-primary-2609.27610v1-20261004.txt'
WAN=R/'shared-sources/Wanner-1801.04713v3-20261004.txt'
THU=R/'shared-sources/Thuillier-tel-00010990v1.txt'
units=[]
for label,source,version,a,b,description in [
 ('GM-standing-scope-and-main-statement',GM,'1608.08030v3',1,173,'Scope explicitly excludes trivial valuation; Theorem1.1 model/PL equivalence'),
 ('GM-scope-continuation',GM,'1608.08030v3',181,196,'Nontrivial standing field hypothesis'),
 ('GM-formal-algebraic',GM,'1608.08030v3',256,275,'Proper formal/algebraic model relation'),
 ('GM-local-PL-formal',GM,'1608.08030v3',347,378,'Formal metric/PL gluing proof'),
 ('GM-local-nef',GM,'1608.08030v3',731,743,'Local formal semipositivity'),
 ('GM-global-nef',GM,'1608.08030v3',754,782,'Local nefness to global curve degrees'),
 ('CLD-flat-fiber-integration',CLD,'1204.6277v2',26470,26492,'Actual fiber integration and pushforward'),
 ('CLD-pulled-back-curvature-fiber-currents',CLD,'1204.6277v2',27561,27606,'Actual fiber integration current coefficients'),
 ('CLD-one-variable-Gauss-radial-mass',CLD,'1204.6277v2',27608,27672,'Gauss dd^c log-max calibration'),
 ('CLD-model-positivity-and-field-pullback',CLD,'1204.6277v2',27926,28068,'Residual positivity theorem and exact field extension corollary'),
 ('Wu-finite-flat-norm',WU,'2609.27610v1',2105,2206,'Multiplicity, actual regularizable-input norm and proof'),
 ('Wu-Hs-norm-and-closed-point',WU,'2609.27610v1',2207,2371,'Complete challenged application and closed-point lemma'),
 ('Wanner-scope-and-subharmonic-disk-comparison',WAN,'1801.04713v3',168,311,'Nontrivial algebraically closed scope; disk comparison definition'),
 ('Wanner-continuous-psh-subharmonic-statement',WAN,'1801.04713v3',134,139,'Theorem2 statement only; not its entire proof'),
 ('Thuillier-subharmonic-decreasing-and-disk-definition',THU,'tel-00010990v1',3765,3854,'Definition3.1.5, decreasing stability3.1.8 and relevant proofs'),
]:
 data='\n'.join(source.read_text().split('\n')[a-1:b]);p=reads/(label+'.txt');p.write_text(data)
 units.append({'id':label,'source':str(source),'source_version':version,'source_sha256':sha(source),'LF_one_based_inclusive':[a,b],'extract':str(p),'extract_sha256':sha(p),'description':description,'exact_selected_body_root_read':True,'whole_primary_source_root_read':False})
(reads/'source-read-record.json').write_text(json.dumps({'recorded_utc':now,'line_convention':'UTF-8 read_text().split("\\n"), inclusive one-based LF','units':units,'whole_primary_sources_read':False,'mathematical_claims_independently_reviewed':False},ensure_ascii=False,indent=2)+'\n')
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint66: unreviewed completed P16.1 repair, concrete H(s) application gap, four root proposals, new primary GM source and15 literal source units; active two-item batch P13.1 author/P13.2 review. No original closure.'
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items[:2],'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['prepared_P13.1_round55']['state']='LAUNCHED: exact frozen native task, session92187; active alongside round51 P13.2 correctness review.'
a['prepared_P13.1_round55']['tool_session_id']=92187
a['P16.1_round56_repair'].update({'observed_status':'completed','accepted':False,'state':'Completed partial, candidate=false; original remains open. Whole argument and four canonical notes read;40 source bindings reproduced, independent review not launched.','reader':str(reader)})
a['continuation66_unreviewed_root_proposals']={'paths':[str(p) for p in sorted((R/'root-checks').glob('*-20261004-continuation66.md'))],'source_read_record':str(reads/'source-read-record.json'),'independently_reviewed':False,'new_originals_solved':[]}
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch_launch']=str(observation);c['current_small_batch_launch_sha256']=sha(observation)
for t in c['targets']:
 if t['id']=='P16.1':t['current_focus']='Round56 partial identifies nondiscrete H(s) curve application; root boundary-trace repair proposed, unreviewed. Singular envelope/existence original remains open.'
 if t['id']=='P13.1':t['current_focus']='Round55 cold eight-primary-source native author active; original all-Reeb finite-energy comparison and uniform differentiation remain open.'
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file();files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation66/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,reads]:
 for p in sorted(directory.rglob('*')):
  if p.is_file():add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['P16.1-argument.md','P16.1-paper.tex','P16.1-paper.pdf','canonical-notes.json','status.json','mathematical-audit.json','root-preservation-and-read-state-continuation66.json','build-results.json','checks.json','source-extracts/source-provenance.json']:add(reader/name)
prov=json.loads((reader/'source-extracts/source-provenance.json').read_text())
for e in prov['excerpts']:add(reader/e['excerpt_file'])
for p in sorted((R/'root-checks').glob('*-20261004-continuation66.md')):add(p)
for p in [R/'prepare_public_P16_1_round56_reader_20261004.py',G/'push-receipt-continuation65.json',G/'prepare_checkpoint_continuation66.py']:add(p)
for p in sorted((R/'shared-sources').glob('GM*-20261004-continuation66.*')):add(p)
assert len({f['path'] for f in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,'historical_reviewed_scoped_papers':40,'current_native_batch':items[:2],'commit_message':'Preserve partial unibranch repair and investigate residue-field curve boundary trace','scope':'Completed candidate=false draft and paper,40 source bindings, four unreviewed root proposals, public GM primary cache,15 selected literal units and current two-item native batch. No new independently reviewed paper or original closure; no private transcripts, SQL, credentials, Git databases or book-source edits.'}
p=G/'upload-manifest-continuation66.json';assert not p.exists();p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),'originals_solved':3,'reviewed_scoped_papers':40,'statuses':[(x['atom'],x['observed_status']) for x in items]},indent=2))
