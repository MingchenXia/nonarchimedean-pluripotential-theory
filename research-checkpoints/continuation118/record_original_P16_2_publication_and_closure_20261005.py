from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,fitz,subprocess

R=Path('/workspace/research');D=R/'deliverables/original-P16.2';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
canonical=K/'P16.2-round115-actual-full-original-review-20261005.json'
v=json.loads(canonical.read_text());assert v['verdict']=='PASS'
assert sha(canonical)=='ce6d0c3aadf67cce1171315d997acbf8ed58a79235fd47da8b8e3b61a3051189'
binding=K/'P16.2-round115-canonical-reading-and-publication-binding-20261005.json'
b=json.loads(binding.read_text());assert b['all_zero_based_exact_statement_bindings_verified']
assert b['all32_premises_root_read'] and b['all54_passage_objects_root_read']
assert b['all_task_URN_quotes_verified_in_current_problem_or_completion_criteria']
assert sha(D/'P16.2-original-scope-review.json')==sha(canonical)
assert sha(D/'P16.2-core.md')=='4b8934b31ebf1fdafb613fedacaf97dd2c41d9b0d9a224664db8f0123d662a25'
assert sha(D/'P16.2-paper.tex')=='fd60dde5676ff84d62b1eee371054c993704b87ed1eacd85536fe02d897155d6'
for i in [1,2]:
    assert '(28 pages)' in (D/f'local-success-build-pass{i}.stdout.txt').read_text()
log=(D/'P16.2-paper.log').read_text()
assert not any(x in log for x in ['Undefined control sequence','Missing character','Overfull','LaTeX Error','Warning:'])
pdf=fitz.open(D/'P16.2-paper.pdf');assert len(pdf)==28
layout=K/'P16.2-original-publication-layout-20261005'
now=datetime.now(timezone.utc).isoformat()
build={'recorded_utc':now,'atom':'P16.2','pages':28,
    'core_sha256':sha(D/'P16.2-core.md'),'source_sha256':sha(D/'P16.2-paper.tex'),
    'pdf_sha256':sha(D/'P16.2-paper.pdf'),
    'local_two_pass_compilation':'SUCCESS','source_errors_missing_glyphs_overfull_or_warnings':False,
    'native_compile':'Built-in compilation was requested before and after the formatting repair, cells1280/1286 remain pending without diagnostics; no native success asserted.',
    'native_repair_attempts':1,'whole_assembled_core_and_all_subsequent_saved_editorial_patches_root_read':True,
    'whole_generated_tex_separately_root_read':False,
    'visually_root_read_pages':[{'page':i,'image':str(layout/f'page-{i}.png'),
        'sha256':sha(layout/f'page-{i}.png')} for i in [1,14,28]],
    'whole_PDF_visually_read':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
save(D/'publication-build-and-root-reading.json',build)
closure={'atom':'P16.2','fully_solved_original_atom':True,'original_statement_unchanged':True,
    'published_utc':now,'exact_scope':b['accepted_original_scope'],
    'retained_positivity':'Actual big rational L, actual isomorphism pi*L=A+D on a smooth projective modification, prescribed original dominated singularity type retained before any target.',
    'mass':'Raw (A^n); unrestricted minimal-type vol(L), (L^n) and compatibility between different retained types are not claimed.',
    'source':str(D/'P16.2-paper.tex'),'source_sha256':sha(D/'P16.2-paper.tex'),
    'pdf':str(D/'P16.2-paper.pdf'),'pdf_sha256':sha(D/'P16.2-paper.pdf'),'pages':28,
    'argument':str(D/'P16.2-core.md'),'argument_sha256':sha(D/'P16.2-core.md'),
    'review':str(canonical),'review_sha256':sha(canonical),'verdict':v['verdict'],
    'operation_id':v['operationId'],'reported_utc':v['reportedAt'],
    'premises':32,'passages':54,'HTTPS_passages':52,'exact_task_URN_passages':2,
    'entire_report_premises_and_passages_root_read':True,
    'all_zero_based_exact_statement_bindings_verified':True,
    'canonical_binding':str(binding),'canonical_binding_sha256':sha(binding),
    'local_two_pass_compilation':'SUCCESS','native_compilation':build['native_compile'],
    'publication_build':str(D/'publication-build-and-root-reading.json'),
    'publication_build_sha256':sha(D/'publication-build-and-root-reading.json'),
    'publication_changes':'Rearrange the exact accepted six proof units, resolve historical drafting wording, label subsection/equation cross-references, align one frame-sign prose sentence with the reviewed minus formula, and typeset four analytic set differences. No later unreviewed proof imported.',
    'review_limit':b['mathematical_acceptance_limit']}
save(D/'P16.2-original-closure.json',closure)
save(K/'P16.2-original-scope-closure-20261005.json',closure)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==6 and 'P16.2' not in a['fully_solved_original_atoms']
    if name=='checklist-current.json':assert a['historical_reviewed_scoped_papers']==44
    a['fully_solved_original_atoms']=sorted(a['fully_solved_original_atoms']+['P16.2'])
    a['remaining_open_original_atoms']=35;a['original_P16_2_full_solution']=closure
    a['updated_utc']=now
    a['goal_state']='7/42 original problems solved;35 remain open;44 historical reviewed scoped papers. Continue small batches until the requested goal.'
    a['prepared_full_original_review115']['status']='completed_PASS_original_closed'
    a['prepared_full_original_review115']['original_closed']=True
    a['prepared_full_original_review115']['canonical_review']=str(canonical)
    a['github_pending_checkpoint']='Checkpoint118: full-original P16.2 canonical PASS and standalone 28-page integrated proof; seventh original closure.'
    if name=='active-work.json':
        a['next_work']='Checkpoint the complete P16.2 result, continue public full-original P16.5 review114, then advance one new original target in the freed slot.'
    else:
        a['active_atoms']=[x for x in a['active_atoms'] if x!='P16.2']
        target=next(x for x in a['targets'] if x['id']=='P16.2')
        target.update({'closure':'solved','fully_solved':True,'research_status':'original_scope_completed',
            'reviewed_papers':[closure],
            'current_focus':'Full original proper nonprojective retained-datum scope accepted PASS115, with the independently reconstructed local operator and standalone 28-page paper.',
            'current_remaining_gaps':[],'exact_scope':closure['exact_scope']})
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
rows=[];count=0
for line in lines:
    row=line.split('\t')
    if row[0]=='P16.2':
        assert row[1]=='open';row[1:4]=['solved','original_scope_completed','1'];count+=1
    rows.append('\t'.join(row))
assert count==1;p.write_text('\n'.join(rows)+'\n')
print(json.dumps({'fully_solved_original_atoms':7,'remaining_open_originals':35,
    'scoped_papers_unchanged':44,'P16.2_pdf_pages':28,'native_compilation_success_asserted':False},indent=2))
