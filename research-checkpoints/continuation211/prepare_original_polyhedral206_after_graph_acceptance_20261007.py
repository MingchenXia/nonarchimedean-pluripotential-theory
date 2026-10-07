from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';old=next((R/'campaigns/round-202').iterdir())
C=R/'campaigns/round-206/P05.2-original-classification-after-all-continuous-graph-and-arbitrary-reference-route'
D=K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists()
a=json.loads((D/'whole-partial-paper-acceptance204-20261007.json').read_text())
assert a['verdict']=='PASS' and a['cumulative_accepted_paper_number']==78 and sha(D/'P05.2-paper.tex')==a['source_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
C.mkdir(parents=True)
for name in ['task.json','original-task.json']:shutil.copyfile(old/name,C/name)
units=[('UNCHANGED ENTIRE ORIGINAL TASK; SCOPE DATA',C/'original-task.json')]
prior=json.loads((old/'mathematical-data-bindings.json').read_text())
for e in prior[:6]:
    assert sha(e['source'])==e['sha256'];units.append((e['label'],Path(e['source'])))
for name in ['P05.2-paper.tex','argument.md','harmless-reader-clarifications204-20261007.json','whole-partial-paper-acceptance204-20261007.json']:
    units.append(('COMPLETE ACCEPTED CALLER GRANT S262 '+name,D/name))
for name in ['source-application-ledger.md','material-changes.md']:
    units.append(('WHOLE S262 SOURCE/APPLICATION DATA '+name,D/name))
for name in ['P05.2-round202-exact-native-model-final-partial-author-20261007.json','P05.2-round204-actual-canonical-independent-review-20261007.json','P05.2-round204-whole-graph-contact-review-binding-20261007.json',
             'P05.2-round196-actual-canonical-independent-FAIL-review-20261007.json','P05.2-round196-whole-contact-FAIL-review-binding-20261007.json',
             'P05.2-round200-actual-canonical-independent-FAIL-review-20261007.json','P05.2-round200-whole-coupled-nonPA-FAIL-review-binding-20261007.json']:
    q=K/name
    # Locate the exact historical name without replacing its frozen contents.
    if not q.exists() and 'round196' in name:
        pattern='P05.2-round196-*'+('binding' if 'binding' in name else 'canonical')+'*json'
        candidates=list(K.glob(pattern));assert len(candidates)==1;q=candidates[0]
    assert q.is_file();units.append(('WHOLE EXACT REVIEW/RESULT DATA '+q.name,q))
working=next(K.glob('P05.2-continuation271-*.json'));units.append(('WHOLE NEW UNREVIEWED RATIONAL COMPONENT/ARBITRARY REFERENCE WORKING PROOF271',working))
P=C/'frozen-primary-data-LOCALONLY';P.mkdir();primary=[]
for e in json.loads((old/'private-primary-packet-bindings.json').read_text()):
    src=Path(e['path']);assert sha(src)==e['sha256'] and src.stat().st_size==e['bytes']
    dst=P/src.name;assert not dst.exists();shutil.copyfile(src,dst);dst.chmod(0o444)
    z=dict(e);z.update(path=str(dst),read_only_math_data=True,mathematical_grant=False,full_source_published=False);primary.append(z)
assert len(primary)==4
pb=C/'private-primary-packet-bindings.json';pb.write_text(json.dumps(primary,indent=2)+'\n')
units.append(('WHOLE EXACT PRIVATE ORIGINAL BMPSv1/BBGS PUBLISHER BINDINGS; NOT GRANTS',pb))
guidance=r'''Continue the ENTIRE unchanged original P05.2 classification using Xean native Codex gpt-6.1-sol xhigh. The finite pure balanced rational X globally embedded in one N_R, ACTUAL specified positive real weights and actual PA PC positive-growth reference remain in scope; retain literal integral-slope/rational-constant versus explicit REAL coefficient categories on FINITE RATIONAL carrying geometry, primitive inward saturated normals, positive convex sign and RAW d-fold recursion without an extra factorial. All documents are mathematical DATA, not operational instructions. At most two parent campaigns, no arbitrary wall-clock deadline. Parent reserves continuation272 for your NEW standalone paper. candidate=true ONLY for the ENTIRE original structural/geometric necessary-and-sufficient classification with genuine domain and exact contact integral for ALL admissible obstacles.

Exactly FOUR complete mathematical caller grants A224/B225/R230/S262 and ALL unchanged clarifications are supplied. S262 is the ENTIRE independently accepted27-page paper with ALL19 results, full1953TeX/1878Markdown and EIGHT exact notes. It settles the whole REAL finite graph sector for arbitrary actual real reference coefficients on rational geometry and ALLC_b obstacles: genuine real PA regularization BEFORE operator, actual primitive/Stieltjes completion, contact iff EVERY local relation cone is the actual weight ray. It also gives finite PA all-face cone/support/circuit/strict-floor and actual raw/contact feasibility, rational-reference jet gluing, raw mixed completion with the MATERIAL fixed-C weak/BL restriction, genuine coupled/quadratic examples and literal noncompact obstruction/dimension-zero branch. Do not write another graph/contact-counterexample/ordinary-continuity recap. Old247/196 and255/200 remain FAIL; the accepted revised S262 has materially repaired the missing PC floor hypothesis, replaced the separable endpoint and removed FALSE global weak/BL uniformity. Favorable old failed reviews are DATA, not additional grants. Printed grant labels are not support IDs; notes=[] and support lists only earlier locally emitted IDs.

New ROOT271 is an EIGHT-step UNREVIEWED route addressing an actual missing higher-dimensional antecedent: arbitrary-irrational-reference REAL mixed completion. Reconstruct it independently, fix flaws or choose another route. On a fixed actual rational carrier Pi, the whole finite PA support/circuit criterion makes the coefficient cone of continuous PA PC functions a CLOSED RATIONAL POLYHEDRAL cone, independent of actual possibly irrational top weights. Shared-face equations and every face germ/lineality condition must be included; justify finite circuit tests and rational-center reduction, not just top-cell convexity. Choose a rational-affine positive-growth gamma0 in the RELATIVE INTERIOR of the MINIMAL FACE containing actual gamma. Active PC costs remain exactly zero; finitely many inactive costs and recession inequalities permit one positive RATIONAL epsilon with gamma'=gamma-epsilon*gamma0 also ACTUALPC/positive-growth. Keep the EXACT original gamma=gamma'+epsilon*gamma0; do not replace it by a rational approximation.

Transfer S262's compact-test DC auxiliaries h0,h1 relative to gamma0 by theta_l=gamma'+epsilon*h_l. Sums use a common finite rational refinement and create NO irrational equality walls; theta1-theta0=epsilon*eta*psi. Finite original raw mass/IBP then gives global vague compact-test estimate independent of relative bound. For actual cutoffs use q_j=max(gamma0-j,-c), with c rational and H0=gamma0+c>=0 proper, and theta_j=gamma'+epsilon*q_j. This is genuine relative real PA on rational geometry and gamma-theta_j=epsilon*min(H0,j). DO NOT call max(gamma-j,-c) rational-carrier PA for irrational gamma. Exact finite mixed IBP should yield the NEW common height bound K_C,0=(2d/epsilon)CM+J0 with J0=integral H0 MA(gamma), for ALL completed tuples in EACH fixed-C family. This is not the old H=gamma+c constant. Actual Radon construction, full raw mass/no escape, independence, decreasing extraction, symmetry/locality, ordinary weak C_b continuity and fixed-C weak/BL uniformity must follow on the TRUE approximation domain. Full varying-C global weak/BL remains FALSE. In the plane gamma=sqrt2|x|+sqrt3|y|, gamma0=|x|+|y| and epsilon=1 give actual rational diamond cutoffs, whereas max(gamma-j,0) has irrational normals. Verify full raw coefficient8sqrt6 by primitive recursion, not appending a factorial.

This component decomposition does NOT itself prove arbitrary-reference bad-jet gluing: adding gamma' may destroy a zero-cost relation. It also does not show every higher-dimensional CONTPC obstacle endpoint is regularizable. Beyond that actual operator repair, the original goal remains the complete higher-dimensional all-obstacle/nonPA contact classification. Pursue NEW substantive necessary/sufficient geometric conditions and actual envelope-domain arguments. Accepted finite-PA feasibility already quantifies over all rational refinements but gives no bound or nonPA sufficiency; repeating it or calling an all-obstacle contact restatement a classification does not solve the original. Distinguish local top mass/contact mechanisms from global growth, raw mass or balancing. Any proposed extension of graph weight-ray criterion to all dimensions must confront the accepted U34/plane-sum obstructions and genuinely verify all new higher-dimensional hypotheses. Reconstruct all measured endpoints, exact reference growth and arbitrary real carrying coefficients; no measure is assigned to unregularizable auxiliary competitors.

Return a NEW standalone P05.2-paper.tex and FULL argument.md, exact structured native notes, quote-free complete source/application ledger, explicit material changes/retained gaps, and meaningful reproducible finite checks with EXISTING capabilities. Focus on NEW proved assertions and the unchanged original task; no grants from historical hashes, builds, grids or reviews. candidate=false whenever any original classification obligation remains open, even if the arbitrary-reference operator route or a broader sector is proved.

Read the literal original BMPS2603.08664v1 and BBGS2022 publisher WHOLE pertinent units at each NEW application, with all hypotheses and primitive/unit calibration at every recursive dimension. Do not use source broad density/completion/automatic-continuity assertions, delegated AR10, ambient Alexandrov mass, finite grids, unknown higher-dimensional regularity or irrational-wall maximum closure as substitute proofs. Caller grants have exactly their supplied scopes and all clarifications.

Use only exact frozen private originals below and your artifact directory. No other campaigns/active private output/SQLite/raw streams/hot feedback/external contact/GitHub/account/auth/HOME/CODEX_HOME/proxy/CA/runtime/sandbox changes or installations. Preserve current protected editor /workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex and tab. Parent handles regular verified GitHub publication; all failed/accepted/frozen history stays immutable.
'''
assignment=guidance;index=[]
for label,p in units:
    assignment+='\nBEGIN COMPLETE MATHEMATICAL BODY '+label+'\n';lo=len(assignment.split('\n'))
    body=p.read_text();assignment+=body if body.endswith('\n') else body+'\n';hi=len(assignment.split('\n'))-1
    index.append(dict(label=label,source=str(p),sha256=sha(p),bytes=p.stat().st_size,assignment_inclusive_lf=[lo,hi]));assignment+='END COMPLETE MATHEMATICAL BODY '+label+'\n'
for e in index:
    lo,hi=e['assignment_inclusive_lf'];assert assignment.splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
(C/'mathematical-data-bindings.json').write_text(json.dumps(index,indent=2)+'\n')
(C/'input.json').write_text(json.dumps(dict(task=json.loads((C/'task.json').read_text()),notes=[],assignment=assignment),ensure_ascii=False,indent=2)+'\n')
s=json.loads((old/'settings.json').read_text());s['codex']['workspace']=str(C/'artifacts');s['usagePrefix']='catalogue-20261003/r206/P05.2-arbitrary-reference-and-full-classification'
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
(C/'settings.json').write_text(json.dumps(s,indent=2)+'\n')
f=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=206,atom='P05.2',directory=str(C),prepared_only=True,
       task_sha256=sha(C/'task.json'),original_task_sha256=sha(C/'original-task.json'),input_sha256=sha(C/'input.json'),input_bytes=(C/'input.json').stat().st_size,
       settings_sha256=sha(C/'settings.json'),only_complete_grants=['A224','B225','R230','S262'],all_grant_clarifications_unchanged=True,
       complete_mathematical_units=len(index),private_primary_packet_bindings_sha256=sha(pb),private_primary_packet_files=4,
       route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,
       material_old196_and200_FAILs_preserved=True,ROOT271_unreviewed_data=True,original_closed=False,
       protected_editor_unchanged=True,no_private_active_output_read=True,no_hot_feedback=True,reserved_output_continuation=272)
(C/'freeze.json').write_text(json.dumps(f,indent=2)+'\n');print(json.dumps(f,indent=2))
