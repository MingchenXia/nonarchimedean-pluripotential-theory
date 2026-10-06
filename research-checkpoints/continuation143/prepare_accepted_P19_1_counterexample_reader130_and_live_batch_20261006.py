from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
source=K/'P19.1-arbitrary-bounded-rays-trivial-NA-infinite-entropy-counterexample-candidate-20261006-continuation176.md'
assert sha(source)=='3f7eea7bf2780df68a92560497d2590f68be473cdd6c56f48ca8b2e992687a51'
canonical=K/'P19.1-round130-actual-original-independent-review-20261006.json'
review=json.loads(canonical.read_text());assert review['verdict']=='PASS'
assert review['operationId']=='136c6629-b514-4f05-9a7e-39cef58da22b'
assert len(review['premises'])==10 and len(review['passages'])==10
assert sorted({p['premise'] for p in review['passages']})==list(range(10))
D=K/'public-P19.1-round130-final-reader';D.mkdir(exist_ok=False)
body=source.read_text()
old='**Status.** Root-authored candidate, not independently reviewed. This proves an obstruction to the unrestricted entropy-slope identity. The original P19.1 residual problem remains open pending an independent comparison with its exact completion criterion. In particular, an example does not establish the entropy-slope theorem for every maximal ray on every compact Kähler manifold.'
new='**Status.** Independently reviewed theorem in the stated counterexample scope. Native Xean review130 accepted the complete analytic counterexample and explicitly retained original P19.1 as open: the maximal-ray entropy theorem on arbitrary compact Kähler manifolds is a separate remaining question.'
assert body.count(old)==1;body=body.replace(old,new).replace('**Candidate theorem.**','**Theorem.**')
old='The original P19.1 task asks for the residual entropy-slope statement with its precise ray hypotheses. This candidate definitively rules out the **unrestricted equality using the usual datum**. It does not establish the missing upper entropy recovery for all maximal rays in arbitrary transcendental Kähler classes. An independent reviewer must determine whether a correctly formulated negative answer is sufficient for the original atom; until then its solved count remains unchanged.'
new='The original P19.1 task asks for the residual entropy-slope statement with its precise ray hypotheses. This theorem rules out the **unrestricted equality using the usual datum**. Independent review130 confirms that it does not establish the missing upper entropy recovery for all maximal rays in arbitrary transcendental Kähler classes. The full original atom remains open.'
assert body.count(old)==1;body=body.replace(old,new)
body=body.replace('Only three established inputs enter the proof:','Three principal specialized inputs enter the proof:')
old='No third-party source PDF or lengthy source extract is included in this candidate. No native campaign input has been modified, no active independent-review workspace has been inspected, and no feedback has been sent to either active reviewer. At preparation, rounds 125 and 129 are the two running native Xean reviews using the requested gpt-6.1-sol xhigh route. Original totals remain 7 solved and 35 open; independently accepted scoped papers remain 49.'
new='The complete proof was independently accepted in its exact counterexample scope by native Xean review130, using gpt-6.1-sol xhigh. The full original problem remains open. No third-party source PDF or lengthy source extract is included in this paper.'
assert body.count(old)==1;body=body.replace(old,new)
body+=r'''

### Analytic conventions and background

Darvas--Xia's printed convention is $dd^c=i\partial\bar\partial/(2\pi)$. Apply their correspondence with background $\omega/2$ and the same potential functions. Every associated current is half the corresponding current in this paper. Top masses and the reference volume therefore scale by the same power of two; normalized Monge--Ampère measures, normalized energies, test-curve mass profiles and the displayed energy formula are unchanged. The homogeneous geodesic equation is unchanged by the same positive rescaling. This makes the application to the convention in Section1 explicit.

The standard analytic background consists of bounded Bedford--Taylor products and non-pluripolar restriction (Boucksom--Eyssidieux--Guedj--Zeriahi, arXiv:0812.3674, Section1.2 and Proposition1.4); bounded integration by parts (their Theorem1.14); psh removability across a closed pluripolar subset and divisorial-current subtraction (Demailly, *Complex Analytic and Differential Geometry*, ChapterI Theorem5.24 and ChapterIII Section8); maximal-ray order (Mesquita--Piccione, Definition5.1.6 and Theorem5.1.7); and the Riemann criterion for nonprojective complex tori (Demailly, ChapterVII Corollary14.5). These are background inputs in addition to the three specialized inputs above. The entropy lower estimate in this paper is derived directly and does not import a general slope-equality theorem.
'''
(D/'P19.1-argument.md').write_text(body)
projection={k:v for k,v in review.items() if k!='passages'}
projection['source_evidence_bindings']=[{'premise':p['premise'],'url':p['url'],
    'quote_sha256':hashlib.sha256(p['quote'].encode()).hexdigest()} for p in review['passages']]
projection.update({'canonical_result_sha256':sha(canonical),'source_quotations_removed_for_publication':True,
    'original_closed':False,'accepted_scoped_paper_number':50,'complete_verdict_report_premises_and_passages_root_read':True})
save(D/'independent-review-public-projection.json',projection)
commands=[['pandoc','P19.1-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P19.1-paper.tex']]
commands += [['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P19.1-paper.tex']]*2
builds=[]
for i,command in enumerate(commands):
    p=subprocess.run(command,cwd=D,capture_output=True,text=True)
    (D/f'build-{i}.stdout').write_text(p.stdout);(D/f'build-{i}.stderr').write_text(p.stderr)
    builds.append({'argv':command,'returncode':p.returncode})
    assert p.returncode==0,(i,p.stdout[-2200:],p.stderr[-1500:])
pdf=fitz.open(D/'P19.1-paper.pdf');pages=len(pdf)
for i in sorted(set([0,pages//2,pages-1])):
    pdf[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(D/f'layout-page-{i+1}.png')
log=(D/'P19.1-paper.log').read_text()
now=datetime.now(timezone.utc).isoformat()
binding={'recorded_utc':now,'atom':'P19.1','round':130,'verdict':'PASS','original_closed':False,
    'accepted_scoped_paper_number':50,'scope':'All products P1 times arbitrary compact Kahler Y: bounded actual weak rays from zero with usual actual NA datum zero, normalized energy slope -a^2/2 and infinite probability entropy slope.',
    'review_operation_id':review['operationId'],'review_reported_utc':review['reportedAt'],
    'canonical_review_sha256':sha(canonical),'reviewed_original_argument_sha256':sha(source),
    'editorial_changes_only':'Accepted status, original-scope comparison, explicit Darvas--Xia background rescaling, enumerated analytic background. Mathematical construction unchanged.',
    'whole_final_mathematical_argument_root_read':False,
    'whole_original_mathematical_argument_and_complete_independent_review_root_read':True,
    'whole_generated_tex_separately_root_read':False,
    'argument_sha256':sha(D/'P19.1-argument.md'),'tex_sha256':sha(D/'P19.1-paper.tex'),
    'pdf_sha256':sha(D/'P19.1-paper.pdf'),'PDF_pages':pages,'local_builds':builds,
    'overfull_diagnostics':log.count('Overfull'),'undefined_diagnostics':log.count('Undefined'),
    'actual_visual_pages':[],'native_compiler_success_observed':False,
    'existing_P16_4_editor_modified_or_new_tab_opened':False,
    'primary_source_pdfs_or_long_excerpts_in_public_reader':False}
save(D/'source-application-and-publication-binding.json',binding)
(D/'README.md').write_text('Independently accepted analytic counterexample (native review130 PASS). The complete argument, standalone TEX and PDF prove the stated bounded-ray construction, including nonprojective Kahler products. Original P19.1 remains open for the residual maximal-ray theorem; no P19.2--P19.4 closure is claimed. Source quotations are omitted from the public review projection and bound by hashes.\n')
batch=[]
for n,atom,label,session in [
    (131,'P19.1','P19.1-original-transcendental-entropy-recovery-and-ray-normalization-research',9468),
    (132,'P16.5','P16.5-original-genuine-Fubini-Study-decreasing-closure-and-compactness-research',73910)]:
    C=R/f'campaigns/round-{n}'/label;freeze=json.loads((C/'freeze.json').read_text())
    for name,key in [('input.json','input_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==freeze[key]
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(p.stdout);assert status['status'] in ['running','completed']
    dest=C/'launch-public-native-status.json';save(dest,status)
    item={'round':n,'atom':atom,'directory':str(C),'database':'work.sqlite','tool_session_id':session,
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','author_research_only':True,
        'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
        'observed_status':status['status'],'observed_utc':status['observedAt'],
        'public_status':str(dest),'public_status_sha256':sha(dest),'freeze':freeze}
    save(C/'launch-record.json',item);batch.append(item)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==49
    d.update({'updated_utc':now,'historical_reviewed_scoped_papers':50,
        'P19_1_actual_scoped_counterexample130':binding,
        'current_small_batch':{'recorded_utc':now,'items':batch,
            'active_items':[i for i in batch if i['observed_status']=='running'],
            'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
            'focus':'Original P19.1 transcendental entropy and normalization; original P16.5 genuine decreasing closure and compactness.'}})
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reader':str(D),'binding':binding,'batch_rounds':[i['round'] for i in batch],
    'originals_solved':7,'originals_open':35,'accepted_scoped_papers':50},indent=2))
