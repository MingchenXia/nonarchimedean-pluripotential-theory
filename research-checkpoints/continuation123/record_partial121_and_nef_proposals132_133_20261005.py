from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); K=R/'root-checks'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,a):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
C=R/'campaigns/round-121/P16.5-original-minimal-reference-and-nonbig-carrier-research'
A=C/'artifacts/codex-gTiUva'; D=K/'public-P16.5-round121-final-reader'
result=K/'P16.5-round121-actual-original-research-result-20261005.json'
res=json.loads(result.read_text()); assert res['candidate'] is False
assert len(res['notes'])==3 and Path(res['workspace'])==A
assert json.loads((A/'input.json').read_text())==json.loads((C/'input.json').read_text())
assert (A/'input.json').read_bytes()==(A/'input-original.json').read_bytes()
for name in ['P16.5-argument.md','P16.5-paper.tex','source-application-ledger.json','status.json']:
    assert sha(A/name)==sha(D/name)
assert json.loads((D/'status.json').read_text())['status']=='PARTIAL'
record={
 'recorded_utc':now,'atom':'P16.5','round':121,'canonical_result':str(result),
 'canonical_result_sha256':sha(result),'candidate':False,'status':'PARTIAL','original_closed':False,
 'whole_canonical_three_notes_root_read':True,'whole_final_argument_root_read':True,
 'argument_literal_LF_entries':405,'root_read_ranges':[[1,105],[106,245],[246,371],[372,405]],
 'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),
 'pdf_sha256':sha(D/'P16.5-paper.pdf'),'PDF_pages':14,
 'final_local_latex_return_codes':[0,0],'final_missing_glyph_or_overfull_warnings':False,
 'actual_final_PDF_pages_visually_read':[1,7,14],'native_compiler_success_asserted':False,
 'frozen_launch_input_sha256':sha(C/'input.json'),'native_staged_input_sha256':sha(A/'input.json'),
 'native_staged_input_bytes':(A/'input.json').stat().st_size,
 'parsed_native_staged_input_equals_frozen_launch_input':True,
 'native_byte_preservation_is_between_native_input_and_native_input_original':True,
 'new_scoped_independent_acceptance':False,'reviewed_scope_count_changes':0,
 'remaining_original_gaps':json.loads((D/'status.json').read_text())['concrete_gaps'],
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
save(K/'P16.5-round121-actual-partial-result-root-reading-and-publication-binding.json',record)
save(D/'publication-preparation.json',record)
p=K/'P16.5-entire-nef-floor-energy-operator-and-weighted-floor-limits-draft-20261005-continuation133.md'
binding={'recorded_utc':now,'note':str(p),'note_sha256':sha(p),
 'whole_final_own_note_root_read':True,'independent_acceptance':False,'original_closed':False,
 'scope':'Entire intrinsic nef floor E1 top operator, actual bounded Borel-locality coefficient passage, full raw mass, total-variation floor limits, all intrinsic E1 test integrability and fixed/simultaneous-floor weighted limits.',
 'selected_primary_literal_LF_ranges_root_read':[[3880,3977],[3978,4068],[4070,4215],[4215,4295],[4490,4540],[4540,4620]],
 'complete_named_units_root_read':['Theorem7.14','Lemma7.15','Remark7.16','Theorem7.18','Proposition7.19','Proposition7.21','Lemma7.22','Proposition7.27','Lemma7.30','Corollary7.31','Theorem7.40','Lemma7.43'],
 'constants_dimension_only_primary_LF':473,'primary_url':'https://arxiv.org/pdf/1801.08229v4',
 'whole_primary_work_or_recursive_foundation_reading_claimed':False,
 'active119_122_inputs_modified_or_hot_feedback_sent':False,
 'proof_draft_only':True}
save(K/'P16.5-root-continuation133-final-own-proof-reading-and-source-binding.json',binding)
batch=K/'current-small-batch119-122-20261005';batch.mkdir(exist_ok=False)
items=[]
for rd,label,db,pty in [(119,'P16.5-bounded-reference-and-numerical-zero-independent-review','review.sqlite',83713),(122,'P16.5-nef-bounded-products-and-continuous-obstacle-independent-review','review.sqlite',82906)]:
    c=R/f'campaigns/round-{rd}'/label
    import subprocess
    s=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(s.stdout); q=batch/f'P16.5-round{rd}-public-native-status.json';save(q,d)
    assert d['status'] in ['running','completed']
    items.append({'round':rd,'atom':'P16.5','directory':str(c),'database':db,'tool_session_id':pty,
      'observed_status':d['status'],'public_status':str(q),'public_status_sha256':sha(q),
      'scoped_review_only':True,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
b={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
   'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
   'focus':'Scoped119 bounded-reference/numerical-zero review and scoped122 all-nef bounded-products/continuous-obstacle review. Original121 returned partial.',
   'native122_prelaunch_long_usage_label_rejected_before_database_or_provider_call':True}
save(batch/'launch-and-public-status-record.json',b)
for name in ['active-work.json','checklist-current.json']:
    f=R/name;a=json.loads(f.read_text());assert len(a['fully_solved_original_atoms'])==7
    assert a['historical_reviewed_scoped_papers']==45
    a['updated_utc']=now;a['current_small_batch']=b
    a['P16_5_actual_original_research121']=record
    a['continuation132_unreviewed_nef_bounded_proof']=json.loads((K/'P16.5-root-continuation132-final-own-proof-reading-and-review-input-binding.json').read_text())
    a['continuation133_unreviewed_nef_intrinsic_floor_proof']=binding
    a['goal_state']='7/42 original problems solved;35 remain open;45 independently reviewed scoped papers. Continue small batches until the requested goal.'
    if name=='active-work.json': a['next_work']='Read completed scoped119/122 actual reports when available; independently audit all-nef intrinsic-floor and weighted/outer extensions, retain original P16.5 gaps, and continue remaining originals in small batches.'
    a['github_pending_checkpoint']='continuation123 preparation'
    f.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'canonical121_partial':True,'original_count':7,'remaining_originals':35,'scoped_count':45,'native_batch':[i['round'] for i in items]},indent=2))
