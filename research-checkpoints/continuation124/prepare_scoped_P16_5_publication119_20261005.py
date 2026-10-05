from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/scoped-P16.5-round119'
assert not D.exists();D.mkdir(parents=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
A=K/'public-P16.5-round117-final-reader';canonical=K/'P16.5-round119-actual-scoped-independent-review-20261005.json'
report=json.loads(canonical.read_text());assert report['verdict']=='PASS'
assert len(report['premises'])==10 and len(report['passages'])==2694
groups=json.loads((K/'P16.5-round119-lossless-unique-passage-reading-groups-20261005.json').read_text())
assert groups['canonical_result_sha256']==sha(canonical)
assert len(groups['unique_groups'])==156 and sum(x['multiplicity'] for x in groups['unique_groups'])==2694
assert all(x['statement']==report['premises'][x['premise']] and x['url'].startswith('https://') for x in report['passages'])
text=(A/'P16.5-argument.md').read_text();first=text.index('# 9. A concrete mechanism')
main=text[:first]
assert main.count('# 8. New zero-volume')==1
main=main.replace('P16.5: reference compatibility, numerical zero mass, and the remaining big-class gates','Bounded divisorial references and numerical-zero non-Archimedean equations')
main=main.replace('Standalone reconstruction from the frozen packet','Research paper with independent scoped review119')
old=main[main.index('The unchanged original P16.5'):main.index('# 1. Scope')]
new='''Independent review119 returned **PASS** for two exact extensions: every bounded genuine change of one prescribed divisorial reference, and every actual numerically trivial rational bundle on the entire genuine numerical cone. All indispensable prescribed-reference constructions are included below. The field is algebraically closed, trivially valued, characteristic zero and of arbitrary cardinality; the original variety is smooth integral projective of positive dimension. Raw metric products and masses are retained.

Original P16.5 remains **open**. Its general minimal-big and nonzero numerical pseudoeffective equations are not certified by this scoped result. The exact actual-ample G0 theorem is the sole equation grant and is used only within that original ample domain. Historical author117 candidate=false and original review114 INCONCLUSIVE remain preserved.

'''
main=main.replace(old,new)
main=main.replace('nonzero outside the divisor.','not identically zero on the divisor complement; additional zeros are allowed.')
main=main.replace('The actual relative $I$ functional is','Here $I_A$ denotes the probability-normalized ample functional, with measure $V_D^{-1}\\operatorname{MA}_A$; the original relative functional retains raw mass. The actual relative $I$ functional is')
main=main.replace('The complete exact grant is preserved at `evidence/block-001.txt`; its 68 supplied primary units are individually preserved in `evidence/G0-dictionary/`. The other source facts used here are itemized in Section 12. They are supplied mathematical evidence, not new task grants or claims of fresh external retrieval.', 'The complete actual-ample grant is the accepted standalone G0 proof identified in the source provenance. The external primary premises and their precise applications are itemized in Section 9. Historical evidence filenames are provenance coordinates, not additional theorem grants.')
ledger=text[text.index('| ID | Statement, hypotheses'):text.index('The nine external premises and all sixteen actual HTTPS')]
ledger='\n'.join(s for s in ledger.split('\n') if not s.startswith('| D0 |'))
appendix='''# 9. Primary applications, independent review and original boundary

'''+ledger+'''
The source table retains the author's literal extraction coordinates as provenance. Independent review119 additionally retrieved and checked the pertinent complete primary statements and proofs from BJ v4, Fujino--Miyamoto v1, BE v3, CLD v2 and the named Stacks tags. Its canonical report and exact premise/passage bindings accompany this paper. These checks do not claim whole-book or recursive foundational verification.

The harmless mathematical clarifications from review119 are incorporated: the polar section need only be not identically zero outside the reference divisor, and equation (42) explicitly uses probability-normalized $I_A$. The external transcription of BE Lemma 8.6 needs its curvature-difference minus sign; that transcription is not reproduced or used with an erroneous sign here. The retained actual signed-product identities already have their stated metric differences.

The certified scope comprises the two extensions and their indispensable supporting Sections 1--8. It supplies no general nonnef minimal-reference membership, full-volume equation, or general nonbig nonzero numerical carrier. Bounded reference changes retain one singularity type and raw mass $A^n$; changing singularity type need not preserve mass. The numerical-zero target is the zero measure, with uniqueness modulo constants only because the entire genuine cone was proved to be constants. A nonconstant zero-top-mass cone is not given that uniqueness conclusion.

Compilation checks document production only. The frozen review task and mathematical input hashes are retained in the accompanying provenance manifest.
'''
(D/'P16.5-argument.md').write_text(main+appendix)
shutil.copyfile(canonical,D/'P16.5-correctness-review.json')
shutil.copyfile(K/'P16.5-round119-lossless-unique-passage-reading-groups-20261005.json',D/'lossless-review-passage-groups.json')
shutil.copyfile(A/'source-application-ledger.json',D/'author-source-application-ledger.json')
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'original_closed':False,'verdict':'PASS','scoped_additions':['Every bounded genuine prescribed-divisorial reference change','Entire actual numerical-zero cone and equation'],
 'author_argument_sha256':sha(A/'P16.5-argument.md'),'canonical_review_sha256':sha(canonical),'actual_external_premises':10,'actual_passages':2694,'distinct_lossless_passage_groups':156,
 'all_actual_passages_match_their_indexed_premises':True,'all_actual_passage_urls_https':True,
 'whole_report_all10_premises_and_all156_distinct_lossless_passage_groups_root_read':True,
 'whole_unchanged_author_supporting_proof_previously_root_read':True,'publication_new_intro_scope_and_two_harmless_corrections_root_read':True,
 'whole_generated_tex_separately_root_read':False,'whole_final_publication_argument_separately_reread':False,
 'missing_minus_one_grant_passage_not_invented':True,'native_compiler_success_asserted':False}
(D/'publication-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
cmd=['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']
r=subprocess.run(cmd,cwd=D,capture_output=True,text=True);(D/'pandoc.stdout').write_text(r.stdout);(D/'pandoc.stderr').write_text(r.stderr);assert r.returncode==0
returns=[]
for i in [1,2]:
 cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']
 r=subprocess.run(cmd,cwd=D,capture_output=True,text=True);(D/f'compile-{i}.stdout').write_text(r.stdout);(D/f'compile-{i}.stderr').write_text(r.stderr);returns.append(r.returncode)
 assert r.returncode==0,(i,r.stdout[-2000:])
record.update({'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),'pdf_sha256':sha(D/'P16.5-paper.pdf'),'local_compilations':returns})
(D/'publication-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
