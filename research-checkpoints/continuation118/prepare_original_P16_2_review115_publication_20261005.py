"""Prepare one standalone edition from the exact complete proof accepted by native review115."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, re, difflib, subprocess

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-115/P16.2-original-common-collar-and-canonical-reference-independent-review'
P=K/'public-P16.2-round113-final-reader';D=R/'deliverables/original-P16.2'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
review=K/'P16.2-round115-actual-full-original-review-20261005.json'
v=json.loads(review.read_text());f=json.loads((C/'freeze.json').read_text())
assert v==json.loads((C/'run.json').read_text())['campaign']['result']
assert v['verdict']=='PASS' and v['operationId']=='63a8f039-5e78-4261-bae2-d574390ee20f'
assert len(v['premises'])==32 and len(v['passages'])==54
for name,key in [('task.json','task_sha256'),('task-original.json','original_task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
assert (C/'task.json').read_bytes()==(C/'task-original.json').read_bytes()
task=json.loads((C/'task.json').read_text())
granttext=task['problem']+'\n'+task['completionCriteria']
for i,e in enumerate(v['passages']):
    assert e['id']==v['operationId']+'/'+str(i)
    assert e['statement']==v['premises'][e['premise']]
    assert e['url'].startswith('https://') or e['url']=='urn:xean:task'
    if e['url']=='urn:xean:task':assert e['quote'] in granttext,e['quote']
assert {e['premise'] for e in v['passages']}==set(range(32))
assert {e['premise'] for e in v['passages'] if e['url'].startswith('https://')}==set(range(31))
paths={
 'main':P/'P16.2-paper.md',
 'A':K/'P16.2-compatible-valuative-centers-and-local-factoriality-20261005-continuation115.md',
 'B':K/'P16.2-original-section-local-products-and-common-collar-gate-20261005-continuation116.md',
 'collar':K/'P16.2-common-ample-collar-and-intrinsic-generated-local-operator-20261005-continuation117.md',
 'C':K/'P16.2-all-point-continuous-canonical-reference-and-local-frame-compatibility-20261005-continuation119.md',
 'D':K/'P16.2-continuation117-common-collar-primary/complete-original-PL-contact-bridge-and-collar-reconstruction.LF25-149.txt'}
packet=(C/'argument.md').read_text()
for p in paths.values():assert p.read_text() in packet,str(p)
assert not D.exists();D.mkdir()
binding=K/'P16.2-round115-canonical-reading-and-publication-binding-20261005.json'
save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'canonical_result':str(review),'sha256':sha(review),'verdict':'PASS',
 'operation_id':v['operationId'],'reported_utc':v['reportedAt'],
 'whole_report_root_read':True,'all32_premises_root_read':True,'all54_passage_objects_root_read':True,
 'all_zero_based_exact_statement_bindings_verified':True,
 'indexed_HTTPS_premises':list(range(31)),'task_granted_premise':31,
 'all_task_URN_quotes_verified_in_current_problem_or_completion_criteria':True,
 'HTTPS_passages':52,'task_URN_passages':2,
 'review_task_sha256':sha(C/'task.json'),'original_task_sha256':sha(C/'task-original.json'),
 'reviewed_full_packet_sha256':sha(C/'argument.md'),
 'entire_accepted_own_proof_units':[{'name':n,'path':str(p),'sha256':sha(p),'whole_literal_in_review_packet':True} for n,p in paths.items()],
 'accepted_original_scope':'Every smooth integral proper positive-dimensional original X over every algebraically closed trivially valued characteristic-zero field of arbitrary cardinality, every actual big rational L and every retained actual projective ample-plus-effective presentation M; entire genuine original dominated cone, original metric operator, intrinsic raw-mass dual-energy targets, all original C0 variations, attainment, comparison and uniqueness.',
 'author113_candidate_false_and_notes_preserved':True,
 'full_primary_works_or_all_recursive_proofs_read':False,
 'mathematical_acceptance_limit':'Independent source-aware native model reconstruction; not formal certification or priority.',
 'new_unreviewed120_125_proofs_imported_into_accepted_edition':False})
for source,name in [(review,'P16.2-original-scope-review.json'),(binding,'P16.2-review-reading-binding.json'),
 (C/'task-original.json','P16.2-original-task.json'),(C/'freeze.json','P16.2-review-input-freeze.json'),
 (P/'canonical-native-result.json','P16.2-author113-canonical-result.json'),
 (P/'external-premises.json','P16.2-author113-external-premises.json')]:
    shutil.copyfile(source,D/name)
for name,p in paths.items():shutil.copyfile(p,D/('P16.2-reviewed-proof-'+name+'.md'))
old=paths['main'].read_text();text=old;edits=[]
def replace(before,after):
    global text
    assert text.count(before)==1,(before[:100],text.count(before))
    text=text.replace(before,after);edits.append({'before':before,'after':after})
replace('subtitle: "Proof reconstruction, original sections, and a remaining local-operator bridge"','subtitle: "Genuine local products, intrinsic finite energy, and equations for retained polar data"')
replace('author: "Research draft"','author: "Research manuscript"')
start=text.index('# Abstract and status');end=text.index('# 1. Exact domain')
abstract="""# Abstract

We construct a finite-energy non-Archimedean equation theory on every smooth integral proper variety of positive dimension over an arbitrary algebraically closed trivially valued characteristic-zero field. Projectivity and an ample bundle on the original carrier are unnecessary. Every specified actual big rational line bundle admits a retained polar presentation on a smooth projective modification. Its prescribed original-section cone consists of actual metrics on the original carrier, with normalized compactness and genuine envelopes. Common actual ample collars construct intrinsic local products, independent of admissible local nets, collars and frames, including bounded discontinuous endpoints. Relative reference floors give the genuine nonpluripolar operator and raw mass $(A^n)$. Its intrinsic dual-energy condition characterizes all targets; every such positive Radon measure is realized by an actual finite-energy metric, unique modulo constants. No cardinality, toric, skeletal, support or finite-generation restriction replaces the stated domain.

This edition combines the manuscript with the complete center, local-product, common-collar and canonical-reference proofs independently reconstructed by native review115. The earlier manuscript's incomplete drafting status remains preserved in its separate historical record. The only task-granted theorem is the exact actual-ample P16.1 theory, used on explicitly ample projective auxiliary carriers; the new cone, descent and local-operator applications are proved here. Source-aware computational review is not a formal proof certificate or a priority claim.

"""
text=text[:start]+abstract+text[end:]
replace('This is the raw mass of the constructed pairing.','This is the raw mass of the genuine operator constructed below.')
replace('# 8. Pretarget mixed pairing and the local progress','# 8. Pretarget mixed products from original section metrics')
replace('## 8.1. A measure-valued pairing, without calling it the missing operator','## 8.1. The candidate pairing identified by the local construction')
replace('This is constructed for the entire cone before any target is chosen. It is a positive symmetric Radon measure of raw mass $V$. It gives $P$ zero mass by Section 6. Its local finite and limiting properties proved next give more information than a bare transported-measure definition, but we retain the tilde until the remaining bridge in Section 10 is established.',
 'This pairing is constructed for the entire cone before any target is chosen. It is a positive symmetric Radon measure of raw mass $V$, giving $P$ zero mass by Section 6. Section 10 constructs the intrinsic local products of the actual original metric and proves that their nonpluripolar reference-floor extension equals this pairing. Thus it is the genuine original-carrier operator; the equality with the ample measure is a conclusion of that local construction.')
replace('This proves a genuine decreasing local limit for a specified actual-section category, with all-point endpoints and germ independence inside that category. It does not yet prove the comparison with a construction made from only locally defined contact nets and a collar; that comparison is the remaining issue.',
 'This proves a genuine decreasing local limit for the full type-preserving original-section category, with all-point endpoints and germ independence. Section 10 proves its equality with independently supplied admissible local contact nets using one common actual ample collar.')
replace('## 8.4. Relative floors and an unbounded candidate in the same category','## 8.4. Relative floors and the unbounded nonpluripolar product')
replace('a Radon candidate of mass exactly $V$','a Radon measure of mass exactly $V$')
replace('These assertions prove the relative nonpluripolar *candidate* in the divided category, including mass and weighted limits. They do not silently define an independent local Bedford--Taylor product by declaring (8.1) to be it.',
 'These assertions prove the relative nonpluripolar extension in the original-section category, including mass and weighted limits. The independently constructed local product in Section 10 agrees with these restrictions and floors, completing the intrinsic operator identification before any target is chosen.')
replace('# 9. Original envelopes, all continuous variations, and conditional equations','# 9. Original envelopes, all continuous variations, and equations')
replace('The deductions of this section apply to the pretarget pairing $\\widetilde M$. They become an actual P16.2 equation theorem if the local bridge in Section 10 is established.',
 'Section 10 identifies the pretarget mixed pairing with the intrinsic local original-carrier operator. The following deductions therefore give the equation theorem for that genuine operator.')
replace('## 9.3. An actual attained maximizer and the conditional equation','## 9.3. An actual attained maximizer and the equation')
replace('This is an actual equation for the pairing (8.1). It is not yet labeled the genuine original local Monge--Ampere equation because Section 10 remains.',
 'By the local identification proved in Section 10, this is the genuine original-carrier finite-energy Monge--Ampere equation. The attained solution is an actual original-section metric.')
replace('## 9.4. Comparison and domination for the pairing','## 9.4. Comparison and domination for the genuine operator')
s=text.index('# 10. The exact unclosed local-operator statement');e=text.index('# 11. A genuinely nonprojective test')
collar=paths['collar'].read_text()
collar=collar[collar.index('Retain the datum'):collar.index('## 7. Exact conclusion')]
collar=collar.replace('genuine cone hypotheses of116','genuine cone conclusions of Section 5 and Appendix B')
collar=collar.replace('The complete earlier reconstruction of that bridge is saved as\npublic-P16.1-round-92-final-reader/granted/supplied-02.txt, Sections2-3.\nIts historical labels are documentary, not new grants. The pertinent\nbody was read at LF25-110.',
 'Appendix D includes the complete pertinent reconstruction of this bridge, using actual algebraic PL extensions, represented models and same-bundle Gauss descent. Its new application here is established from that proof, rather than granted by a historical label.')
collar=collar.replace('Sections1-4 of116','Appendix B, Sections1-4')
collar=collar.replace('the independently required114 converse','the whole-cone converse proved in Section 5')
localintro="""# 10. Intrinsic local products through a common actual ample collar

We now prove the category comparison needed to identify the pairing of Section 8 with the intrinsic original metric operator. Admissible local inputs are decreasing finite affine FS/contact weights on a common ordinary neighborhood, with the actual metric cocycles and bounded endpoint. The associated entire original cone is recovered by its reference floors; no density theorem for arbitrary unrelated classical currents is asserted. Appendix D gives the finite contact-to-genuine-ample reconstruction used in the proof. Appendix C proves continuous canonical original references and signed frame compatibility.

"""
localend="""
The construction proves independence of admissible local nets, common collars, compatible frames and generated continuous references. Its bounded products and relative nonpluripolar extension equal the original-section limits of Section 8. Thus (8.1) is the genuine local operator, before the choice of target, and Sections 5--9 establish the full retained-datum theory on the original carrier.

"""
text=text[:s]+localintro+collar+localend+text[e:]
start=text.index('# 12. External-premise ledger')
text=text[:start]
theorem=r"""
**Main theorem.** Every $X$ and specified big actual rational $L$ in Section 1 admits a datum $\mathcal M$ as in (1.1). For each retained datum, the entire dominated original-section cone $\mathcal P_{\mathcal M}$ of Section 5, its actual finite-energy space $\mathcal E^1_{\mathcal M}$ and the local nonpluripolar operator of Sections 8 and 10 have normalized compactness, envelopes, decreasing mixed and integrable weighted continuity, comparison and domination. Their raw diagonal mass is $V$. The intrinsic target condition of Section 7 is finite exactly for the positive Radon measures of mass $V$ integrating every genuine relative finite-energy test. Each such measure is the genuine operator of an actual $u\in\mathcal E^1_{\mathcal M}$, unique modulo constants. The variational objective is attained, and its outer energy has the two-sided derivative in every original $C^0(X^{\rm an})$ direction. The choices in $\mathcal M$ are retained; compatibility between distinct prescribed types is not part of this assertion.

"""
where=text.index('**G0, used only on $(Y,A)$.**')
text=text[:where]+theorem+text[where:]
def appendix(key,title,first,last=None):
    body=paths[key].read_text()
    body=body[body.index(first):body.index(last) if last else None]
    return '\n# '+title+'\n\n'+body+'\n'
text+=appendix('A','Appendix A. Compatible valuative centers and local factoriality','## 1. The precise valuative premise','## 5. Evidence')
text+=appendix('B','Appendix B. Original-section local products and reference floors','## 1. The local finite stage','## 5. The precise remaining')
text+=appendix('C','Appendix C. Continuous original references and signed frame compatibility','Retain any algebraically closed','## 4. Precise dependencies')
text+='\n# Appendix D. Exact finite PL extensions and the genuine contact-to-ample bridge\n\n'+paths['D'].read_text()+'\n'
text+=r"""
# References and verification scope

The retained actual-ample theorem is the full original P16.1 theorem stated in Section 1; its proof and separate source-aware review accompany the P16.1 paper. The present new nonprojective construction was reconstructed independently using Xean's native Codex path with gpt-6.1-sol at xhigh reasoning. Review115 accepted this complete proof packet, with 32 exact external premises and 54 source passages. The canonical report is preserved separately. The manuscript and all mathematical annexes appear in that frozen packet in their entirety; this edition changes their arrangement and resolved-status wording, while preserving their proof content. It imports none of the later unreviewed continuations120--125.

The review does not assert reading every primary work or all recursive background proofs. Primary statements and pertinent proof units, rather than titles, hashes or compilation, support the applications. In particular, BE's continuous theorem is applied only in its uniform continuous category, and its nontrivial-valued nef theorem only over the auxiliary $k((t))$. G0's decreasing-net theorem supplies the discontinuous and finite-energy passages after genuine ample membership is established.

The permanent Stacks tags used here are [0200](https://stacks.math.columbia.edu/tag/0200), [07QW](https://stacks.math.columbia.edu/tag/07QW), [0B8X](https://stacks.math.columbia.edu/tag/0B8X), [0AY8](https://stacks.math.columbia.edu/tag/0AY8), [0AG0](https://stacks.math.columbia.edu/tag/0AG0), [01Q3](https://stacks.math.columbia.edu/tag/01Q3), [0B5T](https://stacks.math.columbia.edu/tag/0B5T), [0BEM](https://stacks.math.columbia.edu/tag/0BEM), [0BJ8](https://stacks.math.columbia.edu/tag/0BJ8), [0BFP](https://stacks.math.columbia.edu/tag/0BFP), [0BX5](https://stacks.math.columbia.edu/tag/0BX5), [01KA](https://stacks.math.columbia.edu/tag/01KA), [01KZ](https://stacks.math.columbia.edu/tag/01KZ), [0AFZ](https://stacks.math.columbia.edu/tag/0AFZ), [01KF](https://stacks.math.columbia.edu/tag/01KF) and [0B5N](https://stacks.math.columbia.edu/tag/0B5N).

The other primary sources are:

- Berkovich, *Étale cohomology for non-Archimedean analytic spaces*, 1993, [§2.6](https://www.numdam.org/item/10.1007/BF02712916.pdf).
- Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, [1801.08229v4](https://arxiv.org/pdf/1801.08229v4).
- Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, [1805.01016v3](https://arxiv.org/pdf/1805.01016v3).
- Chambert-Loir--Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, [1204.6277v2](https://arxiv.org/pdf/1204.6277v2).
- Conrad, *Ostrowski's theorem and finite extensions*, [§6](https://math.stanford.edu/~conrad/676Page/handouts/ostrowski.pdf).
- Ducros, *Espaces de Berkovich, polytopes, squelettes et théorie des modèles*, [published Theorem3.2](https://www.numdam.org/item/10.1142/S1793744212500077.pdf).
- Fujino--Miyamoto, *Nakai--Moishezon ampleness criterion for real line bundles*, [2101.00806v1, Theorem1.4](https://arxiv.org/pdf/2101.00806v1).
- Fujino--Sato, [Example4.4](https://www.math.kyoto-u.ac.jp/~fujino/wSato.pdf).
- Gubler--Martin, *On Zhang's semipositive metrics*, [2019](https://ems.press/content/serial-article-files/26466).
- Gubler--Rabinoff, [2503.05513v1](https://arxiv.org/pdf/2503.05513v1) and [2506.13548v1](https://arxiv.org/pdf/2506.13548v1).
- Rohrer, [dissertation, Chapter IV](https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf).
- Temkin, *Desingularization of quasi-excellent schemes in characteristic zero*, [0904.1592v2](https://arxiv.org/pdf/0904.1592v2).

The auxiliary toric example tests genuine nonprojectivity and does not restrict the whole-domain theorem or the admissible measures. All prescribed types, operators and masses are determined before a target is selected.
"""
# This changes notation only after its actual local identification has been supplied.
text=text.replace('\\widetilde M','\\operatorname{MA}')
core=D/'P16.2-core.md';core.write_text(text)
(D/'P16.2-core.publication.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='reviewed/manuscript113.md',tofile='standalone/P16.2-core.md')))
save(D/'publication-only-assembly.json',{'created_utc':datetime.now(timezone.utc).isoformat(),
 'accepted_proof_units':[{'name':n,'path':str(p),'sha256':sha(p)} for n,p in paths.items()],
 'core':str(core),'core_sha256':sha(core),
 'mathematical_new_theorem_or_proof_added':False,
 'assembly':'Resolve historical incomplete-status wording using the accepted whole collar proof; include all accepted own proof annexes and their contact reconstruction; rename the identified tilde pairing to MA.',
 'metadata_and_status_replacements':edits,
 'author113_historical_candidate_false_record_unchanged':True,
 'unreviewed120_125_imported':False,'original_count_incremented':False,
 'existing_P16_4_editor_changed_replaced_or_new_tab_opened':False})
save(D/'publication-preparation.json',{'created_utc':datetime.now(timezone.utc).isoformat(),
 'atom':'P16.2','state':'Full original retained scope accepted PASS; standalone proof assembled; source reading and compilation/export pending.',
 'canonical_review':str(review),'canonical_review_sha256':sha(review),
 'core':str(core),'core_sha256':sha(core),
 'review_input_sha256':sha(C/'argument.md'),'source_tex_created':False,
 'original_counts_incremented':False,
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'native_editor':'Existing P16.4 editor stays open and unchanged; no new tab.'})
print(json.dumps({'publication':str(D),'core_sha256':sha(core),'core_LF':len(text.splitlines()),
 'canonical_review_sha256':sha(review),'canonical_binding_sha256':sha(binding),
 'compile_and_full_saved_core_read_pending':True,'original_count_incremented':False},indent=2))

