from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,re
R=Path('/workspace/research');K=R/'root-checks';src=K/'public-P19.2-round149-partial-singular-start-reader';D=R/'deliverables/scoped-P19.2-singular-start-relative-profile';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=K/'P19.2-round152-actual-scoped-independent-review-20261006.json';j=json.loads(p.read_text());assert sha(p)=='a123c0d03b48c70a578ade36207c358aa6ca0eb86b4a39d93dfc0979436fbe77' and j['verdict']=='PASS'
assert len(j['premises'])==12 and len(j['passages'])==20 and {x['premise'] for x in j['passages']}==set(range(12))
for x in j['passages']:assert x['statement']==j['premises'][x['premise']] and x['url'].startswith('https://') and x['quote']
D.mkdir(parents=True,exist_ok=True)
changes={'.md':[
 ('author: "Research draft"','author: "Independently reviewed supporting theorem"'),
 ('**PARTIAL; candidate=false. The entire unchanged original P19.2 is not solved.**','**Independent review PASS for the theorem below; original P19.2 remains open.**'),
 ('On smooth active pieces the two-variable gradient lies on\n$(x,-(x-a)_+)$, so its Hessian determinant is zero.','On smooth active pieces the gradient in $(\\rho,t)$ lies on\n$(x,-(x-a)_+)$. Since $t=-\\log|\\tau|^2$, the gradient in\n$(\\rho,\\log|\\tau|^2)$ is $(x,(x-a)_+)$. Thus its Hessian determinant is zero.'),
 ('They are $C^1$, strictly convex and increasing with bounded global\npotentials,','They are $C^1$ in the radial variable $\\rho$, strictly convex and\nincreasing, with bounded global potentials; global $C^1$ regularity\nat $p$ is not asserted. They have'),
 ('entropy recovery in the polarized\nfinite-radial-entropy domain.','entropy recovery for zero-start rays in the polarized\nfinite-radial-entropy domain.')
 ],'.tex':[
 ('\\author{Research draft}','\\author{Independently reviewed supporting theorem}'),
 ('\\textbf{PARTIAL; candidate=false. The entire unchanged original P19.2 is\nnot solved.}','\\textbf{Independent review PASS for the theorem below; original P19.2\nremains open.}'),
 ('in \\(\\rho\\), hence psh. On smooth active pieces the two-variable\ngradient lies on \\((x,-(x-a)_+)\\), so its Hessian determinant is zero.','in \\(\\rho\\), hence psh. On smooth active pieces the gradient in\n\\((\\rho,t)\\) lies on \\((x,-(x-a)_+)\\). Since \\(t=-\\log|\\tau|^2\\),\nthe gradient in \\((\\rho,\\log|\\tau|^2)\\) is \\((x,(x-a)_+)\\).\nThus its Hessian determinant is zero.'),
 ('\\] They are \\(C^1\\), strictly convex and increasing with bounded global\npotentials, endpoint slopes zero and one, and decrease to \\(Q\\). The','\\] They are \\(C^1\\) in the radial variable \\(\\rho\\), strictly convex\nand increasing, with bounded global potentials; global \\(C^1\\) regularity\nat \\(p\\) is not asserted. Their endpoint slopes are zero and one,\nand they decrease to \\(Q\\). The'),
 ('entropy recovery in the polarized finite-radial-entropy domain.','entropy recovery for zero-start rays in the polarized\nfinite-radial-entropy domain.')
 ]}
for suffix,edits in changes.items():
 t=(src/('P19.2-paper'+suffix)).read_text()
 for a,b in edits:assert t.count(a)==1,(suffix,a);t=t.replace(a,b)
 (D/('P19.2-paper'+suffix)).write_text(t)
shutil.copyfile(src/'source-application-ledger.json',D/'source-application-ledger.json')
builds=[]
for k in (1,2):
 argv=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(D),str(D/'P19.2-paper.tex')];z=subprocess.run(argv,capture_output=True,text=True);(D/f'compile-pass{k}-LOCALONLY.txt').write_text(z.stdout+z.stderr);builds.append({'argv':argv,'returncode':z.returncode});assert z.returncode==0
log=(D/'P19.2-paper.log').read_text();info=subprocess.run(['pdfinfo',str(D/'P19.2-paper.pdf')],capture_output=True,text=True,check=True).stdout;pages=int(re.search(r'Pages:\s+(\d+)',info)[1])
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'classification':'Scoped supporting theorem passed whole independent review152; original P19.2 still open. Final adoption pending root visual check.','tex':str(D/'P19.2-paper.tex'),'tex_sha256':sha(D/'P19.2-paper.tex'),'md_sha256':sha(D/'P19.2-paper.md'),'pdf':str(D/'P19.2-paper.pdf'),'pdf_sha256':sha(D/'P19.2-paper.pdf'),'pages':pages,'builds':builds,'warnings':log.count('Warning'),'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'underfull':log.count('Underfull'),'review':str(p),'review_sha256':sha(p),'review_verdict':'PASS','all12premises_and20passages_root_read':True,'exact_statement_index_bindings_valid':True,'all_external_premises_covered':True,'whole_original_687_line_md_root_read':True,'all_final_changed_proof_units_root_read':True,'whole_final_tex_separately_root_read':False,'harmless_clarifications':['Gradient signs explicitly distinguished in (rho,t) and (rho,log|tau|^2).','C1 for Q_m is radial, no global C1 assertion at retained pole p.','DZ recovery theorem explicitly zero-start.'],'original_closed':False,'accepted_paper_count_after_adoption':58,'independent_acceptance':True,'actual_visual_pages':[],'native_compile_success_observed':False,'existing_editor_unchanged':True,'review_scope':'General genuine-level relative-ceiling lemma; actual singular-start CPn n>=2 rational relatively ample model approximations of the retained finite-H radial start, all closed relative Legendre ceilings, collapsing minus-infinite boundary raw mixed masses, calibrated genuine-only singularity distances, joint entropy slopes; stated general maximal mechanism limitations and toric diagnostic only.'}
assert b['warnings']==b['overfull']==b['undefined']==0
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
for p in sorted({1,4,7,pages}):subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','1200','-png',str(D/'P19.2-paper.pdf'),str(D/f'page-{p}-LOCALONLY')],check=True)
print(json.dumps({k:b[k] for k in ('pages','tex_sha256','pdf_sha256','warnings','overfull','undefined')},indent=2))
