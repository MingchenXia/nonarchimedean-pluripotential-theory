from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,re
R=Path('/workspace/research');K=R/'root-checks'
source=K/'P16.5-entire-big-surface-relative-equation-candidate-20261006-continuation186.tex'
old=source.read_text();review=K/'P16.5-round142-actual-scoped-independent-review-20261006.json'
accept=json.loads((K/'P16.5-round142-surface-acceptance-and-original-scope-record-20261006.json').read_text())
assert accept['accepted_papers_after']==53 and accept['whole_canonical_report_premises_passages_root_read']
start=old.index('This is an unreviewed candidate.');end=old.index('\\subsection{S1.',start)
intro='''This paper concerns every actual big rational bundle on a smooth integral
projective surface over every algebraically closed trivially valued
characteristic-zero field. It establishes the entire intrinsic relative
finite-energy equation, on the original analytic carrier and for arbitrary
support. The arbitrary-dimensional original P16.5 remains open. The complete
surface structural proof and the intrinsic nef operator, polar, separation
and attainment proofs form part of the argument in Appendices A--E.
We use the established actual-ample \\(G_0\\) theory only in its stated domain.
The additional rigid zero-volume range is specified separately.

'''
new=(old[:start]+intro+old[end:]).replace('pdfauthor={Unreviewed mathematical candidate}','pdfauthor={Surface equation research paper}').replace('\\author{Unreviewed mathematical candidate}','\\author{Surface equation research paper}').replace('\\textbf{Candidate theorem.}','\\textbf{Theorem.}',1)
marker='\\subsection{S1.'
assert new[new.index(marker):]==old[old.index(marker):].replace('\\textbf{Candidate theorem.}','\\textbf{Theorem.}',1)
D=R/'deliverables/scoped-P16.5-all-big-surfaces';D.mkdir(parents=True,exist_ok=False)
tex=D/'P16.5-paper.tex';tex.write_text(new)
rows=[]
for i in range(2):
    cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(tex)]
    r=subprocess.run(cmd,capture_output=True,text=True);(D/f'build{i+1}-LOCALONLY.stdout').write_text(r.stdout);rows.append({'argv':cmd,'returncode':r.returncode});assert r.returncode==0,r.stdout[-4000:]
log=(D/'P16.5-paper.log').read_text();pdf=D/'P16.5-paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout;pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'classification':'Final independently accepted supporting surface paper; original P16.5 remains open.',
    'tex':str(tex),'tex_sha256':sha(tex),'pdf':str(pdf),'pdf_sha256':sha(pdf),'pages':pages,'builds':rows,
    'overfull':log.count('Overfull'),'undefined':log.lower().count('undefined'),'warnings':log.count('Warning'),
    'source_candidate_tex_sha256':sha(source),'all_proof_body_bytes_unchanged_except_theorem_label':True,
    'whole_individual_mathematical_proof_units_root_read':True,'whole_assembled_final_tex_separately_root_read':False,
    'whole_canonical_independent_review_root_read':True,'independent_review':str(review),'independent_review_sha256':sha(review),
    'review_verdict':'PASS','accepted_paper_count':53,'original_closed':False,'originals_solved':8,'originals_open':34,
    'actual_visual_pages':[],'native_compile_success_observed':False,'existing_editor_unchanged':True,
    'scope':accept['scope'],'editorial_changes':'Reviewed-scope introduction, author metadata and theorem label; every proof unit and appendix retained byte-for-byte.'}
assert b['overfull']==b['undefined']==b['warnings']==0
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
for n in [1,20,pages]:subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1500','-png','-singlefile',str(pdf),str(D/f'page-{n}-LOCALONLY')],capture_output=True,check=True)
print(json.dumps({'directory':str(D),'pages':pages,'tex_sha256':b['tex_sha256'],'pdf_sha256':b['pdf_sha256'],'all_proof_body_bytes_unchanged':True},indent=2))
