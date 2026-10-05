from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,x):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
C=R/'campaigns/round-123/P16.5-original-intrinsic-nef-variational-and-general-reference-research'
A=C/'artifacts/codex-Fcqm7N'
canonical=K/'P16.5-round123-actual-native-result-20261005.json'
res=json.loads(canonical.read_text())
assert res['candidate'] is False and len(res['notes'])==4
assert Path(res['workspace'])==A
assert json.loads((A/'status.json').read_text())['status']=='PARTIAL'
assert (A/'input.json').read_bytes()==(A/'input-original.json').read_bytes()
assert json.loads((A/'input.json').read_text())==json.loads((C/'input.json').read_text())
core=(A/'P16.5-core.md').read_text()
main='\n'.join((A/'P16.5-argument.md').read_text().split('\n')[:518])
assert main.replace("  - '\\lstset{breaklines=true,basicstyle=\\tiny\\ttfamily,columns=fullflexible}'\n",'').rstrip()==core.rstrip()
D=K/'public-P16.5-round123-main-reader';D.mkdir(exist_ok=False)
(D/'P16.5-argument.md').write_text(core)
for n in ['status.json','source-application-ledger.json']:
    (D/n).write_bytes((A/n).read_bytes())
commands=[['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']]
commands += [['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']]*2
build=[]
for i,cmd in enumerate(commands):
    r=subprocess.run(cmd,cwd=D,capture_output=True,text=True)
    (D/f'build-{i}.stdout').write_text(r.stdout)
    (D/f'build-{i}.stderr').write_text(r.stderr)
    build.append({'argv':cmd,'returncode':r.returncode})
    assert r.returncode==0,(i,r.stderr[-1500:],r.stdout[-1500:])
info=subprocess.run(['pdfinfo',str(D/'P16.5-paper.pdf')],capture_output=True,text=True,check=True)
(D/'pdfinfo.txt').write_text(info.stdout)
pages=int(next(x.split(':',1)[1].strip() for x in info.stdout.split('\n') if x.startswith('Pages:')))
pub={'recorded_utc':now,'atom':'P16.5','round':123,'canonical_result':str(canonical),'canonical_result_sha256':sha(canonical),
     'candidate':False,'status':'PARTIAL','original_closed':False,'independently_accepted':False,
     'whole_actual_canonical_four_notes_root_read':True,'whole_main_math_body_root_read':True,
     'actual_main_body_root_read_literal_LF_ranges':[[1,165],[166,335],[336,518]],
     'public_core_mathematical_body_matches_actual_read_main':True,
     'whole_native_appended_argument_separately_root_read':False,
     'whole_native_source_application_ledger_root_read':True,
     'extended_third_party_source_appendices_published':False,
     'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),'pdf_sha256':sha(D/'P16.5-paper.pdf'),
     'PDF_pages':pages,'local_builds':build,'actual_visual_pages':[],
     'native_compiler_success_asserted':False,
     'scope':'Unreviewed author draft: complete intrinsic nef-big variational equation via polar attenuation and same-class PL approximation, plus all-nef floor and weighted theory, volume equality, strict comparison/domination, numerical-zero endpoint and exact nonbig mixed obstruction. Original general big nonnef and nonbig scopes remain open.',
     'remaining_original_gaps':json.loads((D/'status.json').read_text())['concrete_gaps'],
     'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
save(D/'publication-preparation.json',pub)
save(K/'P16.5-round123-main-body-root-reading-and-publication-binding-20261005.json',pub)
for no,name in [(139,'P16.5-nef-section-volume-and-canonical-minimal-reference-draft-20261005-continuation139.md'),
                (140,'P16.5-intrinsic-nef-strict-comparison-and-domination-draft-20261005-continuation140.md')]:
    p=K/name
    save(K/f'P16.5-root-continuation{no}-whole-own-proof-reading-binding-20261005.json',
         {'recorded_utc':now,'note':str(p),'note_sha256':sha(p),'whole_saved_own_proof_root_read':True,
          'independently_accepted':False,'original_closed':False,'frozen124_125_inputs_changed':False,'hot_feedback_sent':False})
Q=K/'current-small-batch124-125-after-native123-20261005';Q.mkdir(exist_ok=False)
items=[]
for rd,label,pty in [(124,'P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review',49744),
                      (125,'P16.5-entire-nef-big-variational-equation-independent-review',47713)]:
    c=R/f'campaigns/round-{rd}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    st=json.loads(r.stdout);assert st['status'] in ['running','completed']
    p=Q/f'P16.5-round{rd}-public-native-status.json';save(p,st)
    items.append({'round':rd,'atom':'P16.5','directory':str(c),'database':'review.sqlite','tool_session_id':pty,
                  'observed_status':st['status'],'public_status':str(p),'public_status_sha256':sha(p),
                  'scoped_review_only':True,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Independent124 entire intrinsic nef support; independent125 full intrinsic nef-big equation including corrected polar and atomic/separation support. Original123 returned PARTIAL/candidate=false.'}
save(Q/'launch-and-public-status-record.json',batch)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
    a.update({'updated_utc':now,'current_small_batch':batch,'P16_5_actual_original_research123':pub,
              'goal_state':'7/42 original problems solved;35 remain open;47 independently reviewed scoped papers. Continue small batches.',
              'github_pending_checkpoint':'continuation127 preparation'})
    a['prepared_scoped125_nef_big_equation'].update({'prepared_only':False,'launched':True,'tool_session_id':47713,
                                                   'observed_status':next(i['observed_status'] for i in items if i['round']==125)})
    for no in [139,140]:
        bp=K/f'P16.5-root-continuation{no}-whole-own-proof-reading-binding-20261005.json'
        a[f'continuation{no}_unreviewed_supplement']=json.loads(bp.read_text())
    if name=='active-work.json':a['next_work']='Read actual independent124/125 reports when complete; pursue general big nonnef reference and relative operator using full original data, author123 main proof and new volume/comparison supplements; push preserved checkpoints regularly.'
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().split('\n')
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        row=line.split('\t');assert row[1]=='open'
        row[2]='Original123 PARTIAL: unreviewed full intrinsic nef-big candidate and volume/comparison; scoped124 and125 active; own139/140 supplements unreviewed; general big nonnef and nonbig remain open.'
        lines[i]='\t'.join(row)
p.write_text('\n'.join(lines))
print(json.dumps({'original123':'PARTIAL','candidate':False,'reader_pages':pages,'active_small_batch':[124,125],'original_count':7,'reviewed_scoped_count':47},indent=2))
