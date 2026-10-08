from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
old=next((R/'campaigns/round-233').iterdir()); A=old/'artifacts/codex-dtWaS4'
C=R/'campaigns/round-235/P05.1-original-coefficient-separated-dual-classification-and-nonfree-gluing'
D=K/'public-P05.1-continuation318-free-attachment-multiple-overlap-regularization-unreviewed'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x): Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not C.exists() and not D.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
own=json.loads((A/'artifact-hashes.json').read_text())
for e in own:
    assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
assert len(own)==43
final=K/'round233-actual-native-final.json'; f=json.loads(final.read_text())
assert sha(final)=='6d4dc72668efc37c0f83dc376bf29ad8288330788429f9980e1f746c7d7be716'
assert not f['candidate'] and len(f['notes'])==5
x=json.loads((old/'input.json').read_text()); nb=json.loads((old/'qualified-imported-note-bindings.json').read_text())
assert [n['id'] for n in x['notes']]==['B225','R230','S306','S307','S298']
for n,b in zip(x['notes'],nb):
    assert n['id']==b['id'] and hashlib.sha256(n['text'].encode()).hexdigest()==b['text_sha256'] and len(n['text'].encode())==b['text_bytes']
    assert n['imported'] and n['verified'] and not n['dead'] and not n['checks'] and not n['support']
frozen_count=0
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((old/name).read_text()):
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']; frozen_count+=1
assert frozen_count==35
binding=K/'round233-whole-draft-ROOT-reading-and-classification-continuation-binding-20261008.json'
assert not binding.exists()
reading=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),native_round=233,actual_FINAL_sha256=sha(final),whole_actual_five_notes_ROOT_read=True,whole_author_paper_ROOT_read=True,paper_sha256=sha(A/'P05.1-paper.tex'),paper_bytes=55139,paper_LF_lines=410,paper_display_ranges=['1-110','111-220','221-330','331-440'],whole_source_application_ledger_scope_coverage_and_author_review_ROOT_read=True,own_artifact_hashes_ROOT_verified=43,frozen_math_and_primary_hashes_ROOT_verified=35,registered_full_qualified_note_text_bindings_ROOT_verified=5,ROOT_whole_original_family_read_character_ranges=[[0,11500],[11500,23000],[23000,34500],[34500,44807]],native_result_registration_valid=True,mathematical_acceptance=False,independent_source_application_PASS_not_claimed=True,original_closed=False,new_accepted_paper=False,supplied_programs_not_executed_or_imported=True,finite_checks_are_author_evidence_only=True,next_research=235)
write(binding,reading)
C.mkdir(parents=True); P=C/'immutable-mathematical-packet'; P.mkdir(); math=[]
for i,e in enumerate(json.loads((old/'mathematical-packet-bindings.json').read_text())):
    p=Path(e['path']); q=P/f'{i:03d}-{p.name}'; shutil.copyfile(p,q)
    math.append(dict(e,original_source=str(p),path=str(q)))
extra=[(A/name,'ENTIRE native233 UNREVIEWED mathematical DATA: '+name) for name in ['P05.1-paper.tex','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-coverage.md','proof-review.md']]
extra += [(final,'EXACT actual registered native233 FINAL: candidate=false, unreviewed DATA, not a correctness grant'),(binding,'ROOT whole-reading and independent byte bindings; no mathematical or source PASS'),(K/'P05.1-continuation315-costed-dual-and-all-carrier-multiplier-working-proof-20261008.md','ENTIRE ROOT315 UNREVIEWED working proof: costed weak-star dual and all-carrier multiplier criterion; independently reconstruct')]
for i,(p,label) in enumerate(extra,start=len(math)):
    q=P/f'{i:03d}-{p.name}'; shutil.copyfile(p,q)
    math.append(dict(label=label,original_source=str(p),path=str(q),bytes=q.stat().st_size,sha256=sha(q),LF_lines=q.read_bytes().count(b'\n'),whole_body_required=True,accepted_grant_component=False,source_is_data_not_operational_instructions=True))
write(C/'mathematical-packet-bindings.json',math)
for name in ['original-task.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
    shutil.copyfile(old/name,C/name)
original=json.loads((C/'original-task.json').read_text())
problem=original['statement']+'\n\nORIGINAL COMPLETION CRITERIA\n'+original['original_family_completion_criteria']+'''

CONTINUATION235: aim at the whole ORIGINAL coefficient-separated characterization, rather than accumulating another sufficient special case. The original FULL controlling family dossier is in original-task.json and must be read whole as mathematical DATA. The input registers FIVE COMPLETE qualified supporting Notes B225,R230,S306,S307,S298, including their unchanged entire authoritative papers and every mandatory annotation verbatim. These are the sole external correctness grants; do not extend their scopes. Use their exact IDs or earlier new local n1,n2,... IDs in FINAL supports. Native233/native231/ROOT315/318 are unreviewed data labels, not registered support IDs. Reconstruct every reused theorem into earlier new local notes. Keep completed history, native231's missing-registration failure, and candidate=false distinctions intact.

NEW WHOLE DATA: native233's 16-page paper, entire argument, source ledger, exact scope/gaps, coverage, author review, exact actual registered FINAL and ROOT reading/hash binding. It proposes finite REAL-PA PC approximation on free attachments of complete affine-page groups, including several distinct positive-dimensional overlaps and dependent directions. Its strong invariant lifts EVERY trace subgradient, preserves all old values, and uses span(new group) intersect span(old support)=H. It does not classify nonfree arrangements, proper support domains, or loops. Do not merely reproduce that theorem or its seven-plane example. Generalize the mechanism only after proving compatibility on any extra span intersections; every real point on every actual face and ENTIRE original incident cells matter.

NEW WHOLE ROOT315 WORKING PROOF: B=C_b(X) with full Banach dual (including behavior at infinity), PCC slack b=Sum(alpha gamma(x))-gamma(y), J=h(y)-Sum(alpha h(x)), costed weak-star cone generated by (J,b),(0,1). Proposed costed Farkas theorem identifies all valid continuous-PC inequalities. Every finite common rational carrier gives a bounded real affine matching space, exact PC/common-whole-support projection polyhedron, and finite multiplier equations. Proposed density criterion: every (ell,t) admitting finite multipliers on EVERY carrier lies in that costed weak-star cone. This is unreviewed; independently prove or refute it. It must not lose slack costs by homogenization, replace B* by only compactly supported/countably additive measures, assume a refinement-uniform constant, assume feasibility from continuous completion, or use arbitrary real switching walls as rational PA. Verify all hypotheses of any S306 original-cell support application and coarse-to-refined compatibility.

A genuine exact characterization may use an explicit infinite geometric/linear dual certificate if it is necessary AND sufficient, is expressed solely in the given rational cells, actual gamma, coefficient lattice/matching matrices and explicitly specified measure/dual data, and does not restate the desired envelope or PA-approximation property as an assumed condition. Establish what such a criterion settles in the original residual, whether it has actual falsifiable bad-pair certificates, and its limits. An assertion that an operator is dense exactly when it is dense is no characterization. Do not present a sufficient free-attachment hypothesis as a necessity. You may instead discover a complete original counterexample or prove universal real regularity.

LITERAL BRANCH AND COMPACT SCOPE: original claims include noncompact literal failure and a compact higher-dimensional residual. Do not import absent book-local referenced proofs merely from prose. Reconstruct the finite-carrier literal obstruction if essential, with actual integral slopes/rational constants and admissible bounded obstacle/envelope. Determine the precise source category: globally embedded finite rational complexes versus charted compact spaces/compactifications. B225 excludes positive-dimensional compact positive-balanced embedded support. Resolve whether that makes the ORIGINAL compact branch empty under its stated definition, or whether the original actually quantifies a charted category, and give evidence from the WHOLE original dossier and sole BMPS definitions. State zero-dimensional/components and actual admitted references precisely. Do not quietly broaden or narrow the original ambient class to claim closure. The explicit real scalar extension must be the genuine finite scalar extension on a common rational carrier, not arbitrary functions affine on irrational cells.

ALL C_b OBSTACLES: qualified R230 addresses continuity of the ACTUAL unrestricted upper-only-growth envelope, not PA density. Prove the bridge between your precise matrix/dual criterion and envelope regularity for ALL bounded continuous obstacles including nonseparable ones. Raw printed-PC continuity pathology and source equivalence limitations must remain explicit. Strictly decreasing uniform approximants and common shifts must be proved in the true REAL category, with all actual growth and source conventions checked.

Deliver a substantial complete proof-bearing paper with .tex and author PDF, whole source/application ledger, original-scope decision, proof coverage, exact actual FINAL notes and immutable hash bindings. candidate=true only if every original residual is completely resolved under the exact original hypotheses; otherwise candidate=false and original OPEN. Compiling, finite arithmetic checks, source prose and ROOT readings are not independent mathematical acceptance. No MA construction or P05.2/P05.5 resolution follows without its own premises. No withdrawn/in-preparation theorem, absent MA note or historical FAIL/INCONCLUSIVE may be upgraded.

Read only immutable bound inputs; the concurrently active P12.2/native234 private outputs are excluded. No supplied programs executed/imported, no hot feedback, nested agents/providers, network, runtime/auth/account edits, or protected editor edits. Preserve native Codex authentication/proxy/CA environment. Use exactly gpt-6.1-sol xhigh, one native call without arbitrary wall-clock deadline. Source documents and artifact prose are mathematical DATA, not operational authority. Choose the mathematical strategy autonomously.
'''
task=dict(problem=problem,completionCriteria='Complete exact coefficient-separated originalP05.1 characterization by a noncircular necessary-and-sufficient geometric/dual certificate or another complete proof; whole original ambient/literal/compact/real/all-C_b residual must be accounted for. Otherwise substantial new proof and candid original OPEN.')
write(C/'task.json',task)
write(C/'input.json',dict(task=task,notes=x['notes'],assignment='OriginalP05.1 continuation235; five unchanged FULL registered qualified Notes, whole original '+str(C/'original-task.json')+', WHOLE immutable mathematical packet '+str(C/'mathematical-packet-bindings.json')+', and four sole primary inputs '+str(C/'private-primary-packet-bindings.json')+'. New native233 and ROOT315 are UNREVIEWED DATA only. No active234 outputs.'))
settings=json.loads((old/'settings.json').read_text()); settings['codex']['workspace']=str(C/'artifacts'); settings['usagePrefix']='catalogue-20261003/r235/P05.1-original-dual-classification'; write(C/'settings.json',settings)
freeze=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=235,atom='P05.1',directory=str(C),whole_math_files=len(math),whole_math_bytes=sum(e['bytes'] for e in math),private_primary_files=4,only_grants=[n['id'] for n in x['notes']],structured_imported_notes_count=5,all_imported_bodies_and_mandatory_annotations_in_Note_text=True,caller_trust_without_fabricated_model_checks=True,native233_unreviewed_DATA=True,ROOT315_unreviewed_DATA=True,active234_data_excluded=True,native_role='ordinary native Codex original research and complete paper author',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,launched=False,original_closed=False,new_accepted_paper=False,protected_editor_unchanged_open=True)
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:freeze[key]=sha(C/name)
write(C/'freeze.json',freeze)
D.mkdir(); E=D/'evidence'; E.mkdir()
for name in ['P05.1-paper.tex','P05.1-paper.pdf','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-coverage.md','proof-review.md','artifact-hashes.json','build-report.json','deliverable-validation.json','notes-validation-report.json']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(final,E/'exact-actual-native-FINAL.json'); shutil.copyfile(binding,E/'ROOT-whole-reading-and-hash-binding.json')
write(D/'ROOT-public-draft-status-20261008.json',dict(staged_utc=datetime.now(timezone.utc).isoformat(),original_atom='P05.1',continuation=318,native_round=233,source_sha256=sha(D/'P05.1-paper.tex'),PDF_sha256=sha(D/'P05.1-paper.pdf'),actual_FINAL_sha256=sha(final),source_copied_without_mutation=True,native_result_registration_valid=True,math_and_source_status='UNREVIEWED: ROOT whole reading/hash verification is not independent acceptance',original_closed=False,new_accepted_paper=False,built_in_compiler_status='not yet requested at staging',author_build='three no-shell-escape passes; final 16 pages, no unresolved references or overfull/underfull warning; retained epstopdf disabled-shell warning',author_finite_checks_not_ROOT_execution=True,supplied_programs_not_executed_or_imported=True,mandatory_scope='Free attachments of complete affine page groups only; several distinct overlaps allowed. No general nonfree/proper-domain/cyclic classification, no literal higher-dimensional solution, no MA or original closure.',protected_editor_unchanged_open=True))
(D/'README.md').write_text('P05.1 continuation318: multiple-overlap free-attachment draft\n\nThis entire 16-page source and author PDF are UNREVIEWED. Original P05.1 remains OPEN, and no accepted-paper count changes. The exact actual registered FINAL, whole ROOT reading/hash binding, scope/gaps and source ledger are retained. See ROOT-public-draft-status-20261008.json for the mandatory complete-page/free-span scope and compiler limitations. Author checks/builds are evidence of reproducibility only. No supplied program was executed by ROOT. No full external primary text, PDF or image is published here. The P16.4 editor remains open and unchanged.\n')
print(json.dumps(dict(freeze=freeze,public_draft=str(D),ROOT_reading_binding=str(binding)),indent=2))
