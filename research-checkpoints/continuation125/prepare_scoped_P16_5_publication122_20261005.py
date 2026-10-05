from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; D=R/'deliverables/scoped-P16.5-round122'
assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical=K/'P16.5-round122-actual-scoped-independent-review-20261005.json'
report=json.loads(canonical.read_text())
assert report['verdict']=='PASS' and report['operationId']=='24e26550-f051-464e-a568-66224d8fe7de'
assert len(report['premises'])==18 and len(report['passages'])==30
assert all(p['statement']==report['premises'][p['premise']] for p in report['passages'])
external=[p for p in report['passages'] if p['premise']!=17]
grant=[p for p in report['passages'] if p['premise']==17]
assert len(external)==29 and all(p['url'].startswith('https://') for p in external)
assert len(grant)==1 and grant[0]['url']=='urn:xean:task'
source=K/'P16.5-nef-bounded-products-and-continuous-obstacle-differentiability-draft-20261005-continuation132.md'
s=source.read_text()
old=s[s.index('This is a new unreviewed'):s.index('## 1.')]
s=s.replace(old,'''This paper constructs the actual raw bounded metric products and proves both derivatives of continuous-obstacle energy for every nef rational line bundle in the stated domain. Independent review122 returned PASS for this exact bounded scope. The original general P16.5 problem remains open: no complete unbounded finite-energy equation or general nonnef reference theorem is asserted here.

''')
s=s.replace('Thus u belongs to the actual ambient vector space E~1 of Definition7.12.', 'Thus the restriction of u to X^lin belongs to the actual ambient vector space E~1 of Definition7.12. The bounded potential itself remains a function on the entire original X^an; the auxiliary restriction is only the published pairing domain.')
s=s.replace('On continuous potentials the published CLD compatibility of Remark7.23 applies.', '''For continuous nef inputs, CLD compatibility follows by the actual metric decomposition (L,u)=(L+H,u)-(H,0). Each term has an actual ample class and a verified continuous psh metric. BJ Remark7.23 applies to those ample terms; BE v3 Sections7.14 and8.4--8.7 provide the multilinear difference-of-psh extension and regularization. Expanding the actual metric differences identifies the continuous nef products. Remark7.23 alone is not cited as a nonample statement.''')
s=s.replace('## 3. Genuine envelopes at the nef boundary', r'''## 3. Genuine envelopes at the nef boundary

For clarity we can prove the nef class-closure step directly, without a general abstract monotone-net diagonal assertion. There is an equality of genuine cones

$$\operatorname{PSH}(\theta)=\bigcap_{\epsilon\in\mathbb Q_{>0}}\operatorname{PSH}(\theta+\epsilon h).$$

The forward inclusion is numerical addition with the genuine constant h-psh metric. For the converse, the actual ample approximation theorem gives finite continuous FS functions f_{epsilon,j} decreasing to a member u of every displayed ample cone. Use triples (epsilon,j,delta), with delta>0, and functions f_{epsilon,j}+delta. Given two triples, choose a smaller positive epsilon_3 and delta_3 smaller than both previous deltas. Their old minimum b is finite continuous, and u+delta_3<b at every point. The increasing open sets {f_{epsilon_3,j}+delta_3<b} cover compact X^an. A finite subcover, followed by one common later net index, provides a third triple dominated by both old functions. Including epsilon and delta as ordered coordinates makes this a decreasing defining FS net. Refining any prescribed finite pointwise threshold, including at a pole, proves its endpoint is u. Its classes approach theta, so the numerical definition gives u in PSH(theta).

Consequently a decreasing family whose classes approach theta and which stays above a finite constant belongs, at its endpoint, to every fixed approaching ample cone and hence to PSH(theta). This proves the particular closure needed below. It does not claim a proof of the source's general abstract Lemma4.6.
''')
s=s.replace('and BJ(PSH2) makes its limit theta-psh.', 'and the preceding genuine nef intersection proves that its limit is theta-psh.')
s=s.replace('Every finite polynomial coefficient has a finite limit, so the positive powers of epsilon vanish without an unproved uniform estimate over arbitrary E1(theta).', '''For each signed measure coefficient, expand every factor (theta,u) as (theta+h,u)-(h,0). This is a fixed finite sum of positive mixed products, with their signs retained. Each positive summand has the fixed finite numerical mixed mass of its ample classes, independent of u and epsilon. The sum of those masses bounds total variation uniformly, so multiplying a coefficient by a positive power of epsilon makes it tend weakly to zero. The corresponding energy coefficients converge by the bounded published pairing theorem in the same common ample cone. This justifies the varying-epsilon polynomial passage with actual signed coefficients, rather than only PL test functions.''')
s=s.replace('All new conclusions here require independent reconstruction. Original P16.5 remains open.', 'These bounded conclusions received the scoped independent PASS identified below. Original P16.5 remains open.')
s=s.replace('The exact whole accepted ample G0 proof is `/workspace/research/root-checks/public-P16.1-round-92-final-reader/argument.md`, SHA256 `6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9`.', 'The exact accepted ample G0 theorem is the actual-ample variational theorem on the original projective analytic space, with canonical reference and raw top-intersection normalization. Its exact proof provenance and SHA256 are recorded with this paper.')
s += '''
Independent review122 checked 17 external primary premises with 29 HTTPS source passages, and one separately indexed inline task grant for the exact actual-ample G0 theorem. The latter passage uses the task URI urn:xean:task and is not an external web citation. All 30 literal passage statements match their indexed premises. The canonical report is preserved without replacing its conclusion or inventing additional source passages.

The source-domain clarifications incorporated here retain the X^lin restriction only for the ambient pairing membership and retain the ample domain of Remark7.23. The nef continuous compatibility uses the explicit actual metric difference above. No continuity of all nef envelopes, or equality of the larger intrinsic E1(theta) with ambient E~1, is inferred. All-cardinality decreasing nets and the full original continuous test space are retained.
'''
D.mkdir(parents=True)
(D/'P16.5-argument.md').write_text(s)
shutil.copyfile(canonical,D/'P16.5-correctness-review.json')
meta={'recorded_utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','original_closed':False,
 'scope':'All actual nef rational bundles: genuine bounded raw metric products, decreasing bounded nets, continuous-obstacle envelopes and both continuous-direction derivatives; no entire intrinsic unbounded equation asserted.',
 'reviewed_original_argument_sha256':sha(source),'canonical_review_sha256':sha(canonical),
 'external_premises':17,'external_https_passages':29,'inline_G0_grants':1,'inline_task_grant_passages':1,
 'inline_task_grant_uri':'urn:xean:task','all30_statements_match_indexed_premises':True,
 'whole_actual_report_all18_premises_and_all30_passages_root_read':True,
 'whole_final_publication_argument_separately_root_read':False,'whole_generated_tex_separately_root_read':False,
 'published_support_clarification':'The already root-read native121 genuine-nef finite-continuous-FS intersection proof is included explicitly; full intrinsic extension is independently reviewed in native124.',
 'G0_proof_sha256':'6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9',
 'native_compiler_success_asserted':False}
commands=[['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']]
commands += [['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']]*2
returns=[]
for i,cmd in enumerate(commands):
 r=subprocess.run(cmd,cwd=D,capture_output=True,text=True)
 (D/f'build-{i}.stdout').write_text(r.stdout);(D/f'build-{i}.stderr').write_text(r.stderr)
 assert r.returncode==0,(i,r.stdout[-2000:]);returns.append(r.returncode)
meta.update({'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),'pdf_sha256':sha(D/'P16.5-paper.pdf'),'local_build_returns':returns})
(D/'publication-preparation.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(meta,ensure_ascii=False,indent=2))
