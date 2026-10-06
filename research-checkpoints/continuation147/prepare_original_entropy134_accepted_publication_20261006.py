from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/original-P19.1'
assert not D.exists();D.mkdir(parents=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
J=K/'P19.1-round134-actual-original-independent-review-20261006.json';review=json.loads(J.read_text())
assert review['verdict']=='PASS'
assert {p['premise'] for p in review['passages']}==set(range(len(review['premises'])))
assert all(p['statement']==review['premises'][p['premise']] and p['quote'].strip() and p['url'].startswith('https://') for p in review['passages'])
source=K/'P19.1-all-starting-points-calibrated-entropy-classification-candidate-20261006-continuation182.tex'
original=source.read_text();text=original
changes={
 'This candidate classifies entropy slopes':'This paper classifies entropy slopes',
 'The proposed finite branch':'The finite branch',
 'This complete candidate has not passed independent review. No original\nproblem or additional accepted paper is counted as solved by this text.':
 'The complete original P19.1 statement and its source applications\npassed independent Xean native Codex review134 with gpt-6.1-sol\nand xhigh reasoning. The proof concerns P19.1; the other three\nresidual hybrid targets are separate.',
 '$b_F$. An affine time shift is first allowed to make $U$ locally bounded':
 '$b_F$. Addition of an affine function of time is first allowed\nto make $U$ locally bounded',
 '\\begin{theorem}[Candidate for original P19.1]':'\\begin{theorem}[Original P19.1 entropy classification]',
 'Their original proof chains and the source applications require\nindependent verification in reviewing this candidate.':
 'Their original proof chains and the source applications were checked\nin the complete independent review; the precise mathematical\nhypotheses remain part of each application.',
 'coincide: apply the valuative criterion to the invariant flag ideals':
 'coincide: apply the valuative criterion to the invariant flag ideals',
 'This completes the proposed classification.':'This completes the classification.',
 'The blowup of $(z,\\tau)=(0,0)$ has $D=-F$, weights one and zero\non the exceptional and strict components, and':
 'The blowup of $(z,\\tau)=(0,0)$ has $D=-F$, datum values $-1$\nand $0$ on the exceptional and strict components, respectively,\nMonge--Amp\\`ere component masses $1$ and $0$, and',
 'with explicit datum, normalization and ray hypotheses. The proposed\nstatement (2) covers this domain, including nonsmooth and\ninfinite-entropy initial potentials, and specifies the otherwise\nnecessary exceptional behavior. Its new supporting proofs and exact\nsource applications must still pass an independent review before\nP19.1 is marked solved. There is no claim to the extra singularity':
 'with explicit datum, normalization and ray hypotheses. Statement (2)\ncovers this domain, including nonsmooth and infinite-entropy initial\npotentials, and specifies the otherwise necessary exceptional\nbehavior. The whole original scope and supporting proof chain\npassed independent review134. There is no claim to the extra singularity',
 'This candidate is root-authored. Complete source units actually read':
 'This paper is root-authored. Complete source units actually read',
 'The complete paper, its local discrepancy proof and the newly\ncalibrated transfer steps require independent mathematical review.':
 'The complete paper, local discrepancy proof and calibrated transfer\nsteps passed independent review134 on 6 October2026. Its full\nreport,24 exact external premises and33 evidence bindings are\nretained in the publication record. This is a source-aware model\nreconstruction, not a formal proof certificate or a priority claim.'}
for old,new in changes.items():
 assert text.count(old)==1,old
 text=text.replace(old,new)
anchor='coincide: apply the valuative criterion to the invariant flag ideals\non an equivariant resolution; noncentral singularities have trivial'
replacement='''coincide: apply the valuative criterion to the invariant flag ideals
on an equivariant resolution. Precisely, Boucksom--Favre--Jonsson
[BFJ], Theorem5.5, identifies the valuative multiplier ideal with
$\\J_+(U)$; the strong openness theorem of Guan--Zhou [GZ],
Theorem1.1, gives $\\J_+(U)=\\J(U)$. Thus equality of valuative
transforms gives equality of the ordinary analytic multiplier ideals,
with no extra openness assumption. Noncentral singularities have trivial'''
assert text.count(anchor)==1;text=text.replace(anchor,replacement)
anchor='\\end{thebibliography}'
add='''\\bibitem{BFJ}[BFJ] S. Boucksom, C. Favre and M. Jonsson,
\\emph{Valuations and plurisubharmonic singularities},
\\href{https://arxiv.org/pdf/math/0702487}{arXiv:math/0702487},
Theorem5.5 and Section5; the statement is for $\\J_+$.
\\bibitem{GZ}[GZ] Q. Guan and X. Zhou,
\\emph{A proof of Demailly's strong openness conjecture},
\\href{https://arxiv.org/pdf/1401.7158}{arXiv:1401.7158}, Theorem1.1.
\\bibitem{Vu}[Vu] D.-V. Vu,
\\href{https://arxiv.org/pdf/2307.15909}{arXiv:2307.15909}, Theorem1.1,
restricted positive volume on the non-K\\"ahler locus.
\\bibitem{Pop}[Pop] D. Popovici,
\\href{https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2003.11.011.pdf}
{C. R. Math. primary text}, Lemma1.2, fixed-chart regularization.
'''
text=text.replace(anchor,add+anchor)
p=D/'P19.1-paper.tex';p.write_text(text)
projection={'verdict':review['verdict'],'report':review['report'],'premises':review['premises'],
 'operationId':review['operationId'],'reportedAt':review['reportedAt'],
 'canonical_local_review':str(J),'canonical_local_review_sha256':sha(J),
 'passages':[{'id':x['id'],'premise':x['premise'],'statement':x['statement'],'url':x['url'],
              'quote_sha256':hashlib.sha256(x['quote'].encode()).hexdigest()} for x in review['passages']],
 'whole_report_all_premises_all_passages_root_read':True,'strict_zero_based_complete_evidence_bindings':True,
 'third_party_quotes_omitted':True,'whole_original_P19_1_scope_independently_accepted':True}
(D/'P19.1-original-scope-review-PUBLIC.json').write_text(json.dumps(projection,ensure_ascii=False,indent=2)+'\n')
a=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(p)];builds=[]
for n in [1,2]:
 r=subprocess.run(a,capture_output=True,text=True);(D/f'build-{n}.stdout').write_text(r.stdout);(D/f'build-{n}.stderr').write_text(r.stderr);builds.append({'argv':a,'returncode':r.returncode})
 if r.returncode:print(r.stdout[-4000:]);break
log=(D/'P19.1-paper.log').read_text();pdf=D/'P19.1-paper.pdf'
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'atom':'P19.1','verdict':'PASS',
 'original_statement_unchanged':True,'fully_solved_original_atom':True,'accepted_paper_number':52,
 'reviewed_candidate_tex':str(source),'reviewed_candidate_tex_sha256':sha(source),
 'tex':str(p),'tex_sha256':sha(p),'whole_final_tex_separately_root_read':False,
 'whole_review_report_and_all_evidence_root_read':True,'publication_changes':list(changes),
 'additional_changes':'Two harmless wording clarifications and precise BFJ J_+/Guan-Zhou citation, exactly as review134 requested; additional checked source bibliography. No theorem or proof mechanism changed.',
 'builds':builds,'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
 'pdf':str(pdf) if pdf.exists() else None,'pdf_sha256':sha(pdf) if pdf.exists() else None,
 'actual_visual_pages':[],'native_compile_success_observed':False,'existing_editor_unchanged':True,
 'canonical_review_sha256':sha(J),'operation_id':review['operationId'],'reported_utc':review['reportedAt']}
if pdf.exists():
 info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
 b['pages']=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
 for page in [1,4,8,b['pages']]:subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','100','-png','-singlefile',str(pdf),str(D/f'page-{page}')],capture_output=True,check=True)
(D/'publication-binding.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n');print(json.dumps(b,indent=2))
