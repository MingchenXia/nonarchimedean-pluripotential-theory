from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P05.1-continuation323-coefficient-separated-dual-classification-candidate'
C=next((R/'campaigns/round-237').iterdir());A=C/'artifacts/codex-H1kGZS'
actual=K/'round237-actual-native-final.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(D/'P05.1-paper.tex')=='3a229463393ceb724ce492cab8607cdc51001f0ca730383f8f7fe88b396d6f73'
assert sha(D/'P05.1-paper.pdf')=='ef4eaa3eefd4d7997b752723653a3cac0afee47cb210474325d05f5aecbfd8dc'
assert sha(actual)=='5f3e070dfc505d029757b78945a64ed03b8211942e7d5b4886ec802ba939dd89'
final=json.loads(actual.read_text());assert final['candidate']and len(final['notes'])==7
own=json.loads((A/'own-bindings.json').read_text())['artifacts'];assert len(own)==15
for e in own:
    p=A/e['filename'];assert p.is_relative_to(A)and p.stat().st_size==e['bytes']and sha(p)==e['sha256']
frozen=[]
for name,count in[('mathematical-packet-bindings.json',31),('historical-own-evidence-bindings.json',17),('private-primary-packet-bindings.json',4)]:
    rows=json.loads((C/name).read_text());assert len(rows)==count
    for e in rows:assert Path(e['path']).stat().st_size==e['bytes']and sha(e['path'])==e['sha256'];frozen.append(e)
notes=json.loads((C/'input.json').read_text())['notes'];bindings=json.loads((C/'qualified-imported-note-bindings.json').read_text());assert len(notes)==len(bindings)==5
for n,e in zip(notes,bindings):
    b=n['text'].encode();assert n['id']==e['id']and len(b)==e['text_bytes']and hashlib.sha256(b).hexdigest()==e['text_sha256']
known={n['id']for n in notes}
for n in final['notes']:assert n['id']not in known and all(s in known for s in n['support']);known.add(n['id'])
verdict=json.loads((A/'verdicts.json').read_text());assert verdict['independent_original_closure_recommendation']and not verdict['automatic_acceptance']and not verdict['closure_mutation_performed']
assert len(verdict['candidate_note_verdicts'])==5 and all(e['mathematical']==e['essential_source']=='PASS'for e in verdict['candidate_note_verdicts'])
saved=json.loads((A/'review-notes.json').read_text());assert saved['candidate']and len(saved['notes'])==7
comparison=[]
for n,s in zip(final['notes'],saved['notes']):
    assert n['id']==s['id']and n['support']==s['support'];comparison.append(dict(id=n['id'],equal_fields=[k for k in n if n[k]==s[k]],differing_fields=[k for k in n if n[k]!=s[k]]))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
sourcefix=D/'source-and-evidence-qualifications-after-review237-20261008.json'
reader=D/'reader-qualifications-after-original-review237-20261008.json'
binding=K/'P05.1-round237-whole-original-coefficient-classification323-binding-20261008.json'
accept=D/'whole-original-paper-acceptance-after-review237-20261008.json'
closure=K/'P05.1-original-coefficient-classification-closure-after-review237-20261008.json'
pub=D/'evidence/independent-whole-review237'
assert not any(p.exists()for p in[sourcefix,reader,binding,accept,closure,pub])
write(sourcefix,dict(recorded_utc=now,source_sha256=sha(D/'P05.1-paper.tex'),source_unchanged=True,qualifications=[
 'Independent237 mathematics and every essential new application PASS under the exact already accepted, fully qualified B225/R230/S306 premises. S307/S298 are scoped context, not universal premises. Qualified imports are caller trust with empty checks, not a fabricated fresh model verification of their histories.',
 'BMPS v1 definitions fix finite closed-face complexes in ONE ambient N_R and a strictly positive pure top cycle. ROOT separately read complete2.1--2.4 LF257--291 and2.27--2.30 LF499--528 to check the decisive domain. Arbitrary charted compactifications, analytic skeletons and line-bundle-valued references are not added to this category.',
 'Source Definition2.30 is LF523--528; LF532--562 supplies Definition2.31/Remark2.33. Source3.22 is a Proposition, not a Definition. Complete needed units were read by237; these harmless descriptor corrections do not change a mathematical premise.',
 'BMPS automatic raw-PC continuity, defective irrational-center insertion, raw-PC density/equality of6.4 and general regularization claims ofRemark6.6 are not imported. New perspective and continuous-completion arguments replace them. Formal rational weights and expressly declared actual positive-real balancing extension remain distinct.',
 'Preserve historical source FAIL/combined FAIL/retrospective INCONCLUSIVE, native231 registration failure, and universal historical read/operation/provider attestation INCONCLUSIVE. Independent237 verifies52current files and5qualified text bindings, not absent historical bodies. ROOT separately verified all32author-owned and44author-frozen hashes earlier; this is not attributed to237.',
 'All seven actual237 FINAL notes were ROOT-read in full, together with complete source-application and original-scope/noncircularity reports. Expanded independent-review.md, coverage and saved review-notes.json are preserved and hash-bound but are not separately claimed whole ROOT semantic reads. Actual and expanded reviewer prose differs; IDs/support agree and exact actualFINAL controls.',
 'Author builds/checks and finite enumeration remain author observations, not continuum proofs or ROOT executions. No supplied program was executed/imported. Current unchanged authoritative source compiled successfully with the builtin compiler in actual returned cell424, recorded in checkpoint241 addendum; compilation is not mathematical certification.'
]))
write(reader,dict(recorded_utc=now,source_sha256=sha(D/'P05.1-paper.tex'),source_unchanged=True,qualifications=[
 'Entire originalP05.1 is solved in its stated finite globally embedded positive-balanced BMPS category. Empty and zero-dimensional pairs are regular in both coefficient conventions. Compact positive-dimensional pairs in this category do not exist, by the proved primitive-lattice/covolume divergence identity; the original named compact branch is resolved as empty, not omitted by an added hypothesis.',
 'Every positive-dimensional admitted literal integral-slope/rational-constant pair has a TRUE bounded literal obstacle whose exact unrestricted raw upper-only envelope has a refinement-independent positive arithmetic approximation gap.',
 'Genuine finite REAL scalar PA regularity is characterized by the explicit INFINITE costed/full-C_b-dual/all-rational-carrier implication. Carrier PC feasibility is eliminated into concrete matching/recession/common ambient support rows, auxiliary variables into nonnegative finite multipliers, and the actual PA-obstacle endpoint problem into the compatible rational generalized-simplex interpolation and independently continuous-envelope bridge. These reductions establish meaningful original classification rather than a bare polar restatement.',
 'The criterion quantifies every finite carrier, the FULL Banach dual and weak-star/product closure with NETS. It supplies no terminating finite algorithm, finite combinatorial taxonomy, computable coefficient oracle, explicit balancedREAL bad pair or claim that every balanced pair is regular. Those stronger claims are not original completion requirements.',
 'The equivalent real properties cover ALL admitted bounded genuinePA obstacles and ALL C_b obstacles, including nonseparable obstacles and multiple overlaps/incidence loops/dependent directions. Successful endpoints have strict decreasing genuinePA-PC uniform approximants, a common relative bound and exact actual recession. Discontinuous raw printedPC modifications are not themselves asserted approximable.',
 'Reference-shift direction: delta=gamma_tilde-gamma bounded gives E_gamma_tilde(u)=E_gamma(u+delta) and K_tilde=K-delta. A bound(ell,t) on K_tilde corresponds to(ell,t+ell(delta)) on K. The ambiguous paper phrase transforms by uses THIS tilde-to-original direction, explicitly correct in actualauthorFINAL n5. Compare finite matrices on common refinements.',
 'ROOT322 compatible-rational-chart compact completion was independently reconstructed by237 only at its stated rational/PCC-preserving overlap, positiveLOCALbalance and scalar-reference hypotheses. Exact literal minima additionally need a finite bounded rational decomposition. It remains a separate category and is not needed to enlarge original closure.',
 'No orthogonality, singular top intersection contact, MA/energy theory, analytic polarized realization or P05.2/P05.5 closure follows. Every accepted supporting theorem keeps its existing mandatory qualifications. Import this paper with BOTH current annotations and the review binding. Ordinary native independent review and ROOT acceptance are distinct from canonical automatic review receipts.'
]))
pub.mkdir()
safe=['independent-review.md','source-application-audit.md','original-scope-and-noncircularity.md','proof-coverage-review.md','verdicts.json','review-notes.json','input-bindings-verified.json','bounded-evidence-verified.json','own-bindings.json','read-spans.jsonl','author-build-observations.json','review-execution-observations.json']
for name in safe:shutil.copyfile(A/name,pub/name)
shutil.copyfile(actual,pub/actual.name)
write(pub/'ROOT-publication-binding.json',dict(recorded_utc=now,frozen_files_verified=52,own_files_verified=15,qualified_note_text_bindings_verified=5,actual_FINAL_controlling=True,actual_saved_field_comparison=comparison,copied_files=[dict(file=n,sha256=sha(pub/n))for n in safe],third_party_primary_sources_not_copied=True,supplied_programs_not_executed_or_imported=True))
write(binding,dict(recorded_utc=now,continuation=323,author_round=235,independent_round=237,source_sha256=sha(D/'P05.1-paper.tex'),pdf_sha256=sha(D/'P05.1-paper.pdf'),pages=17,whole_authoritative_TeX_and_all_five_author_actual_notes_previously_ROOT_read=True,whole_all_seven_reviewer_actual_FINAL_notes_ROOT_read=True,whole_reviewer_source_scope_reports_ROOT_read=True,whole_exact_original_statement_and44807character_dossier_ROOT_read=True,expanded_combined_review_coverage_saved_prose_whole_ROOT_read_not_claimed=True,mathematical_verdict='PASS entire original',essential_source_verdict='PASS exact qualified premises/new applications',original_scope_noncircularity_verdict='PASS meaningful explicit infinite input-only classification',bounded_evidence_verdict='PASS current packet; universal historical/provider facts INCONCLUSIVE',actual_reviewer_FINAL_sha256=sha(actual),frozen_files_verified=52,own_files_verified=15,qualified_note_text_bindings_verified=5,source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),source_unchanged=True,no_supplied_programs_executed_or_imported=True,builtin_current_source_compile_success=True,builtin_compile_receipt='/workspace/research/root-checks/native-built-in-compiler-completion-addendum-after-checkpoint240-20261008.json',ordinary_review_not_canonical_automatic_receipt=True,original_closed=True,protected_editor_unchanged_open=True))
accepted=dict(recorded_utc=now,atom='P05.1',grant_label='O323',cumulative_accepted_paper_number=89,continuation=323,fully_solved_original_atom=True,original_closed=True,completion='Coefficient-separated full envelope regularity classification; meaningful infinite input-only real criterion',mathematical_verdict='PASS entire original with BOTH mandatory annotations',source=str(D/'P05.1-paper.tex'),source_sha256=sha(D/'P05.1-paper.tex'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=sha(D/'P05.1-paper.pdf'),pages=17,review_binding=str(binding),review_binding_sha256=sha(binding),source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),both_annotations_required_on_import=True,original_statement_unchanged=True,other_P05_original_atoms_closed=False,canonical_automatic_acceptance=False,builtin_current_source_compile_success=True,originals_solved=11,originals_open=31)
write(accept,accepted);write(closure,dict(**accepted,acceptance_record=str(accept),acceptance_record_sha256=sha(accept),scope='Exact stated finiteembeddedpositivebalanced category; literal classification and genuineREALinput-only infinite iff includingALLC_bactualenvelopes; no finitealgorithm or P05.2/.5 claims.'))
for name in['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['historical_reviewed_scoped_papers']==88 and len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['github_pending_checkpoint']is None and 'P05.1'not in x['fully_solved_original_atoms']
    x['fully_solved_original_atoms'].append('P05.1');x['fully_solved_original_atoms'].sort(key=lambda a:tuple(int(v)for v in a[1:].split('.')))
    x.update(updated_utc=now,historical_reviewed_scoped_papers=89,remaining_open_original_atoms=31,P05_1_original_coefficient_classification323_acceptance=accepted,original_closure_record=str(closure),original_closure_record_sha256=sha(closure),next_work='Continue all31OPEN originals with at most2nativeXean gpt-6.1-sol xhigh campaigns. OriginalP05.1 now solved with both mandatory qualifications afterwholeindependent237PASS. Native238P12.2 source-completedfullgeometricreconstruction active; prepare verified242checkpoint and next small batch. Preserveauth/protectededitor.')
    x['P05_1_original_candidate235'].update(original_closed=True,new_accepted_paper=True,independent_original_scope_verdict_pending=False,acceptance_record=str(accept),acceptance_record_sha256=sha(accept))
    x['P05_1_original_independent_review237'].update(completed=True,original_closed=True,mathematical_verdict='PASS',essential_source_verdict='PASS',original_scope_noncircularity_verdict='PASS',actual_FINAL=str(actual),actual_FINAL_sha256=sha(actual),universal_historical_provider_verdict='INCONCLUSIVE preserved')
    if name=='active-work.json':x['full_solutions'].append(dict(atom='P05.1',fully_solved_original_atom=True,original_statement_unchanged=True,source=accepted['source'],source_sha256=accepted['source_sha256'],pdf=accepted['pdf'],pdf_sha256=accepted['pdf_sha256'],pages=17,acceptance_record=str(accept),acceptance_record_sha256=sha(accept),both_annotations_required=True))
    else:
        t=next(t for t in x['targets']if t['id']=='P05.1');assert not t['fully_solved'];t.update(closure='solved',fully_solved=True,research_status='original_scope_completed: whole independent237PASS coefficient-separated fullclassification',current_focus='OriginalP05.1 closed by literalclassification and substantiveINFINITEcosted/allcarrier/fullC_bdual criterion; ALLboundedgenuinePA and C_bactualenvelopes included. No finitealgorithm, P05.2orthogonality or P05.5realization conclusion.');t['reviewed_papers'].append(accepted);x['active_atoms']=['P12.2']
    write(p,x)
lines=(R/'checklist-current.tsv').read_text().splitlines();changed=0
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P05.1':
        assert row[1]=='open';row[1]='solved';row[2]='original_scope_completed: whole237PASS coefficient-separated classification, infinite input-only real iff';row[3]=str(int(row[3])+1);lines[i]='\t'.join(row);changed+=1
assert changed==1;(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(original_closed='P05.1',originals_solved=11,originals_open=31,accepted_papers=89,acceptance_sha256=sha(accept),binding_sha256=sha(binding)),indent=2))
