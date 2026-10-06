from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,re
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-148/P16.5-relative-multiplier-generation-compactification-field-descent-independent-review'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.5-round148-actual-scoped-independent-review-20261006.json'
a=json.loads(review.read_text())
assert sha(review)=='fc427f65245d564a513d2759c2a47b166dd0465d18ef561bada5c32112aa5127'
assert a['verdict']=='PASS' and a['kind']=='codex-report'
assert len(a['premises'])==16 and len(a['passages'])==21
for e in a['passages']:
 assert type(e['premise']) is int and 0<=e['premise']<16
 assert e['statement']==a['premises'][e['premise']] and e['quote'] and e['url'].startswith('https://')
assert {e['premise'] for e in a['passages']}==set(range(16))
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert s['status']=='completed' and s['calls']['settled']==1
now=datetime.now(timezone.utc).isoformat()
source=K/'P16.5-relative-multiplier-generation-by-compactification-and-field-descent-candidate-20261006-continuation192.tex'
assert sha(source)=='9c66760fe896b52ca654202d7c6cd7bdf45c9fce219ce2b79019f934a91063c2'
x=source.read_text().replace('An unreviewed algebraic foundation for Problem P16.5','An algebraic foundation for the big-class equation programme')
x=x.replace('We propose a uniform generation theorem','We prove a uniform generation theorem')
before=r'''associated rational model function is $f$. Our time convention is
$\phi_F=1$.'''
after=r'''The associated rational model function is $f$. Throughout,
$\FS(B)$ denotes the full generically finite section-metric class,
allowing common zeros and supported $-\infty$ poles. Our time convention
is $\phi_F=1$.'''
assert before in x; x=x.replace(before,after)
before=r'''where the order is divisibility. The two assertions use the actual'''
after=r'''Here the membership assertion concerns degrees with $H^0(X,mB)\ne0$;
these contain a cofinal divisibility subset because $B$ is big. The
limit uses that subset, ordered by divisibility. The generation theorem
holds in every admissible degree. The two assertions use the actual'''
assert before in x;x=x.replace(before,after)
before=r'''The claimed algebraic theorem, including field descent and exact
relative generation, is a new candidate and requires independent
verification.'''
after=r'''The algebraic theorem, including field descent and exact relative
generation, and its single FS-net consequence have passed independent
verification in their stated scope. The two section-class and nonempty-degree
clarifications above preserve that scope.'''
assert before in x;x=x.replace(before,after)
D=R/'deliverables/scoped-P16.5-relative-multiplier-generation';D.mkdir(parents=True,exist_ok=False)
tex=D/'P16.5-paper.tex';tex.write_text(x)
rows=[]
for i in (1,2):
 cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(tex)]
 p=subprocess.run(cmd,capture_output=True,text=True);(D/f'build{i}-LOCALONLY.stdout').write_text(p.stdout+p.stderr)
 rows.append({'argv':cmd,'returncode':p.returncode});assert p.returncode==0,p.stdout[-4000:]
log=(D/'P16.5-paper.log').read_text();pdf=D/'P16.5-paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
scope='Every algebraically closed trivially valued characteristic-zero field; every smooth integral projective X and actual big rational B; actual resolved equivariant projective models product off time zero. Uniform relative asymptotic-multiplier-ideal generation by one actual ample equivariant twist for every admissible degree, and the one full generically finite decreasing FS-net limit, including supported poles. No general P-envelope identity, decreasing closure, compactness or equation.'
b={'recorded_utc':now,'classification':'Final independently accepted supporting algebraic generation theorem.', 'tex':str(tex),'tex_sha256':sha(tex),'pdf':str(pdf),'pdf_sha256':sha(pdf),'pages':pages,'source_candidate':str(source),'source_candidate_sha256':sha(source),'builds':rows,'overfull':log.count('Overfull'),'warnings':log.count('Warning'),'undefined':log.lower().count('undefined'),'whole_candidate_final_tex_root_read':True,'whole_assembled_final_tex_separately_root_read':False,'whole_canonical_report_premises_passages_root_read':True,'review':str(review),'review_sha256':sha(review),'review_verdict':'PASS','accepted_paper_count':57,'scope':scope,'original_closed':False,'actual_visual_pages':[],'native_compile_success_observed':False,'existing_editor_unchanged':True,'editorial_changes':'Reviewed status plus precisely the two harmless FS-class and nonempty-degree clarifications in the canonical report; frozen source and native input unchanged.'}
assert b['overfull']==b['warnings']==b['undefined']==0
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
accept={'recorded_utc':now,'atom':'P16.5','classification':'Independently accepted supporting uniform-relative-generation theorem; original remains open.','scope':scope,'original_closed':False,'accepted_papers_before':56,'accepted_papers_after':57,'originals_solved':8,'originals_open':34,'review':str(review),'review_sha256':sha(review),'whole_canonical_report_premises_passages_root_read':True,'strict_structural_schema_and_indices_validated':True,'external_premises':16,'external_evidence_passages':21,'mathematical_theorem_grants':[],'harmless_corrections':['FS means the full generically finite section-metric class allowing supported poles.','Equation (12) membership uses nonempty section degrees, which contain a cofinal divisibility subset. Generation remains valid in all admissible degrees.'],'task_sha256':f['task_sha256'],'argument_sha256':f['argument_sha256'],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
ap=K/'P16.5-round148-generation-acceptance-and-original-scope-record-20261006.json';assert not ap.exists();ap.write_text(json.dumps(accept,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==56 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
 j.update({'updated_utc':now,'historical_reviewed_scoped_papers':57,'P16_5_actual_scoped148':accept,'P16_5_accepted_relative_generation_paper148':b,'current_generation_review148':{'round':148,'observed_status':'completed','review_verdict':'PASS','acceptance_record':str(ap),'original_closed':False},'goal_state':'8/42 originals solved;34 open;57 independently accepted papers. Continue small batches.'});p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';out=[]
for line in p.read_text().splitlines():
 z=line.split('\t')
 if z[0]=='P16.5':z[2]='Uniform actual relative multiplier-ideal generation and one FS-net foundation PASS148, alongside whole-surface and exceptional-family endpoints. General big-class operator, all-target existence and uniqueness remain open.';z[3]=str(int(z[3])+1)
 out.append('\t'.join(z))
p.write_text('\n'.join(out)+'\n')
for n in sorted({1,(pages+1)//2,pages}):subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-scale-to','1500','-png',str(pdf),str(D/f'page-{n}-LOCALONLY')],capture_output=True,check=True)
print(json.dumps({'accepted_papers':57,'originals_solved':8,'final_paper':str(tex),'pages':pages,'scope':scope},indent=2))
