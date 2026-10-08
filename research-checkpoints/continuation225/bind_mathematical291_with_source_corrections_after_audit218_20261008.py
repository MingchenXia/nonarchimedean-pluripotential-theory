from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); K=R/'root-checks'
D=K/'public-P05.1-continuation291-compact-balanced-charts-and-independent-affine-branches'
A=R/'campaigns/round-218/P05.1-unchanged-compact-balanced-charts-and-independent-bouquets-whole-native-local-source-audit/artifacts/codex-IIclyq'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert sha(D/'P05.1-paper.tex')=='48903ace22882dbeb879cf262be02ba6476fbff6d26c486af213c592bdc3400d'
assert sha(D/'argument.md')=='8e2b3fe1ea330c64fab81499f3cc748a22591a15bb41ae25ab1f132221958ff8'
rep=json.loads((D/'root-reproduction-binding-20261008.json').read_text())
assert rep['ROOT_source_whole_read'] and rep['ROOT_exact_FINAL_all_six_whole_read'] and rep['ROOT_safe_exact_checker_whole_read'] and rep['ROOT_finite_output_exact'] and rep['finite_assertions']==1945 and rep['local_build_exit_codes']==[0,0] and rep['latex_to_markdown_exact']
audit=json.loads((A/'audit-report.json').read_text())
coverage=json.loads((A/'wholeproof-premise-coverage.json').read_text())
source=json.loads((A/'source-application-audit.json').read_text())
history=json.loads((A/'historical-evidence-audit.json').read_text())
saved=json.loads((A/'native-notes.json').read_text())
final=json.loads((K/'round218-actual-native-final.json').read_text())
assert audit['verdicts']==dict(mathematical_proofs='PASS',source_ledger='FAIL',mathematical_source='FAIL',historical_evidence='INCONCLUSIVE',concrete_historical_reproduction='PASS')
assert audit['coverage']==coverage and audit['source_audit']==source and audit['historical_audit']==history and audit['own_full_reasoning_notes']==saved['notes'] and audit['ordinary_and_granted_premises']==source['calibration']
assert len(coverage['units'])==23 and len(coverage['mathematical_bodies'])==38 and len(saved['notes'])==len(final['notes'])==7 and final['candidate'] is False
aliases=[]
for i,u in enumerate(coverage['units']):
    matching=[n['id'] for n in saved['notes'] if n['text']==u['reasoning']]
    assert len(matching)==1 and matching[0]==u['own_note']
    aliases.append(dict(index=i,unit=u['unit'],source_LF=u['source_LF'],reasoning_exact_saved_note=matching[0],reasoning_sha256=hashlib.sha256(u['reasoning'].encode()).hexdigest(),verdict=u['verdict']))
assert history['reasoning']==next(n['text'] for n in saved['notes'] if n['id']=='n6')
for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
    c=A.parent.parent
    for e in json.loads((c/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in json.loads((A/'frozen-file-bindings.json').read_text()):assert e['matches'] and sha(e['path'])==e['sha256']==e['expected_sha256']
for e in json.loads((A/'own-artifact-bindings.json').read_text())['files']:
    assert sha(A/e['filename'])==e['sha256'] and (A/e['filename']).stat().st_size==e['bytes']
assert (A/'evidence/exact-checks-output.json').read_bytes()==(D/'evidence/ROOT-reproduction/evidence/exact-checks-output.json').read_bytes()
assert (A/'code/exact_checks.py').read_bytes()==(D/'evidence/ROOT-reproduction/code/exact_checks.py').read_bytes()
fix=D/'harmless-source-ledger-corrections-after-audit218-20261008.json'
correction=json.loads(fix.read_text());assert len(correction['corrections'])==2 and correction['unchanged_paper_ledger_and_frozen_input_preserved']
now=datetime.now(timezone.utc).isoformat()
reader=D/'harmless-reader-clarifications-after-full-audit218-20261008.json'
binding=K/'P05.1-round218-whole-compact-bouquet291-source-FAIL-and-ROOT-corrected-mathematical-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-with-source-corrections-after-audit218-20261008.json'
assert not any(p.exists() for p in [reader,binding,accept])
clarifications=[
 'The original TeX, argument and ledger are unchanged. Read the whole paper together with the separately bound source-ledger corrections: BMPS Definitions2.19/2.20 define rational weights; the real extension is independently reconstructed and has a separate BBGS domain. The complete BBGS Proposition3.15 unit is LF604-670. These are verified source corrections, not mathematical changes or evidence of historical reading.',
 'Native218 geometric PASS, original source-ledger FAIL, combined mathematical/source FAIL and historical INCONCLUSIVE remain verbatim. ROOT accepts the whole mathematical sector with the explicit corrected source-application annotations; no unqualified PASS is assigned to the unchanged source ledger and no automatic or canonical research acceptance is claimed.',
 'All7 actual native218 FINAL notes and all7 distinct expanded saved notes were read in their entirety. All23 coverage reasoning strings exactly equal a specified expanded saved note; all unique coverage claims, source/historical fields and remaining audit fields were read. Repeated report subtrees were verified structurally identical after JSON parsing, with exact string comparisons. Initial oversized metadata display was truncated and repaired by complete bounded compact-JSON reads; it is not counted as the complete initial read.',
 'Actual author216 FINAL has6notes; each saved text differs only by one terminal newline, other fields equal. Auditor218 saved expanded summaries/prose differ from its actual FINAL and remain historical presentation. Registered Artifacts suffixes stay separate. Whole report reading and hashes do not certify unavailable universal past no-operation/did-read assertions.',
 'The admitted reference is PC. Upper-only and bounded-difference envelope classes agree by q↦max(q,gamma−||u||), so no continuous-only supremum is substituted. Compact regularity requires the precise boundaryless homeomorphic positive-balanced rational embedding-chart atlas and compatible rational lattice transitions. Broader compact/cellwise/boundary categories remain excluded; independent bouquets require direct-sum tangents and point intersection. Literal noncompact obstruction is separate from REAL regularity.',
 'All5 whole grants A224/B225/R230/S262/S272 and every qualification remain. Genuine global approximation precedes mixed MA; real actual references and signed/zero intermediate cycles persist, raw compact positive-dimensional products0 differ from dimension0. Global vague uniformity, ordinary weak/net continuity and fixed-C-only weak/BL uniformity retain their precise scopes. Finite1945 checks/builds do not prove continuum claims; initial float/layout/xref history and final disabled-shell package warning remain. Builtin cell62 still pending, no result or duplicate/tab change. Original P05.1/P05.2 remain OPEN.'
]
write(reader,dict(recorded_utc=now,source_sha256=rep['source_sha256'],source_correction_file=str(fix),source_correction_sha256=sha(fix),clarifications=clarifications,unchanged_native_combined_FAIL=True,unchanged_native_historical_INCONCLUSIVE=True,whole_math_acceptance_distinct=True,original_closed=False))
b=dict(recorded_utc=now,original='P05.1',continuation=291,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument_sha256=rep['argument_sha256'],pdf_sha256=rep['pdf_sha256'],pdf_pages=13,native_audit_round=218,native_role='ordinary worker local-source audit, NOT canonical research review',native_geometric_verdict='PASS',native_source_ledger_verdict='FAIL',native_combined_verdict='FAIL',native_historical_verdict='INCONCLUSIVE',ROOT_mathematical_verdict='PASS with exact source-correction annotations',actual_native_FINAL_sha256=sha(K/'round218-actual-native-final.json'),all7_actual_FINAL_whole_ROOT_read=True,all7_expanded_saved_notes_whole_ROOT_read=True,all23_coverage_units_unique_contents_whole_ROOT_read=True,whole_audit_source_history_unique_contents_ROOT_read=True,exact_duplicate_subtree_identity_checked=True,coverage_reasoning_alias_bindings=aliases,initial_metadata_display_truncation_preserved_and_fully_repaired=True,all115_frozen_bindings_verified=True,all67_own_artifact_bindings_verified=True,source_corrections=str(fix),source_corrections_sha256=sha(fix),reader_clarifications=str(reader),reader_clarifications_sha256=sha(reader),primary_BMPS418443_and_BBGS604670_whole_units_ROOT_reread=True,primary_other_immediate_units_previously_ROOT_read=True,whole_primary_PDF_ROOT_read_not_claimed=True,ROOT_and_auditor_safe_finite_code_and_output_exact=True,finite1945_checks_previously_ROOT_reproduced_once=True,finite_not_continuum_proof=True,ROOT_local_two_passes=[0,0],source_to_GFM_exact=True,supplied_auditor_emitters_builders_binders_orchestration_not_executed=True,source_unchanged=True,original_closed=False,protected_editor_unchanged_open=True)
write(binding,b)
scope='ENTIRE unchanged329-LF13-page291 mathematical sector plus explicit verified source corrections: compact boundaryless Hausdorff pure-dimensional positive-balanced rational homeomorphic embedding-chart atlas has dominating bounded-PC completion, actual ALL-C_b component-minimum envelopes and both literal/REAL constant regularization; locally literal PA obstacle minima rational. Full-affine global REAL-PA majorants preserve exact actual recession and interpolate ANY finite rational set before shifts. Independent direct-sum complete affine point-bouquets have ALL-continuous relative-PC and ALL-C_b global decreasing genuine regularization and synchronized finite capped roofs. Every finite noncompact rational support with admitted literal positive-growth reference has a bounded literal obstacle with universal fractional-slope error floor. All-face positivity, coefficient separation, optional qualified S272 completion/moment/topologies, d0/zero-mass and original residual scope retained. Exactly5whole grants/allclarifications.'
write(accept,dict(recorded_utc=now,grant_label='S291',cumulative_accepted_paper_number=83,continuation=291,mathematical_verdict='PASS with source corrections',accepted_mathematical_scope=scope,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument=str(D/'argument.md'),argument_sha256=rep['argument_sha256'],pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=rep['pdf_sha256'],pdf_pages=13,review_binding=str(binding),review_binding_sha256=sha(binding),source_correction_file=str(fix),source_correction_sha256=sha(fix),reader_clarifications=str(reader),reader_clarifications_sha256=sha(reader),native_source_ledger_FAIL_retained=True,native_combined_FAIL_retained=True,native_historical_INCONCLUSIVE_retained=True,automatic_acceptance=False,canonical_research_review=False,builtin_compiler_success_claimed=False,all_PDF_pages_visual_ROOT_read_claimed=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope='General higher-dimensional singular REAL-PA structural classification, dependent/positive-dimensional multi-overlap gluing, arbitrary nonseparable product obstacles, and compact boundary/cellwise/incompatible structures beyond precise atlas remain unresolved. Exact broad originalP05.1 is not solved.',protected_editor_unchanged_open=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==82 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=83,P05_1_accepted_compact_bouquet291_after218=json.loads(accept.read_text()))
    j['settled218_unreviewed_audit'].update(full_audit_coverage_ROOT_read_pending=False,whole_unique_audit_and_coverage_ROOT_read=True,mathematical_sector_accepted_with_bound_source_corrections=True,unchanged_native_source_combined_FAIL=True)
    j['current_small_batch']['accepted_paper_number']=83
    write(p,j)
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();changed=0
for i,line in enumerate(lines):
    fields=line.split('\t')
    if fields[0]=='P05.1':
        assert fields[1]=='open';fields[3]=str(int(fields[3])+1);lines[i]='\t'.join(fields);changed+=1
assert changed==1;p.write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(accepted_whole_mathematical_paper=83,grant='S291',native_source_combined_FAIL_retained=True,native_historical_INCONCLUSIVE_retained=True,binding=str(binding),binding_sha256=sha(binding),acceptance_sha256=sha(accept),source_unchanged=True,originals_solved=9,originals_open=33),indent=2))
