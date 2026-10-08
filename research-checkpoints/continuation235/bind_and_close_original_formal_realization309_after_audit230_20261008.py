from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research'); K = R/'root-checks'
D = K/'public-P14.8-continuation309-general-formal-ideal-realization-candidate'
C = next((R/'campaigns/round-230').iterdir()); A = C/'artifacts/codex-reWZlk'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

rep = json.loads((D/'ROOT-reproduction-binding-20261008.json').read_text())
assert sha(D/'P14.8-paper.tex') == rep['authoritative_source_sha256'] == 'fed5ac5c0dae5bd931cc1e96b92640382b09283d0d201c32c2d1aee9e739f074'
assert sha(D/'P14.8-paper.pdf') == rep['ROOT_pdf_sha256'] == 'ec959d53bcf6cd3f6000effcb747858c4ead2370ce2801c28dd5804d49305e39'
assert rep['ROOT_pdf_pages'] == 14 and rep['copied_checker_executions'] == 1 and rep['exact_saved_example_output']
assert rep['finite_assertions'] == 847 and rep['final_warnings'] == ['Package epstopdf Warning: Shell escape feature is not enabled.']
actual = K/'round230-actual-native-final.json'; final = json.loads(actual.read_text())
assert sha(actual) == 'c8b181c3908e1b8658f588401be497cc8f814597599f6118d45d12c61e73c7d1'
assert final['candidate'] and len(final['notes']) == 6
saved = json.loads((A/'audit-notes.json').read_text())
assert saved['candidate'] and len(saved['notes']) == 6 and saved != final
comparison = []
for n, s in zip(final['notes'], saved['notes']):
    assert n['id'] == s['id'] and n['support'] == s['support']
    comparison.append(dict(id=n['id'], equal_fields=[k for k in n if n[k] == s[k]], differing_fields=[k for k in n if n[k] != s[k]]))
for filename, count in [('mathematical-packet-bindings.json',7), ('historical-own-evidence-bindings.json',38), ('private-primary-packet-bindings.json',9)]:
    rows = json.loads((C/filename).read_text()); assert len(rows) == count
    for e in rows:
        assert Path(e['path']).stat().st_size == e['bytes'] and sha(e['path']) == e['sha256']
own = json.loads((A/'own-manifest.json').read_text())['files']; assert len(own) == 29
for e in own:
    p = A/e['file']; assert p.is_relative_to(A) and p.stat().st_size == e['bytes'] and sha(p) == e['sha256']
reports = ['source-ledger.md','sufficiency.md','necessity.md','auxiliary.md','evidence.md','original-scope.md']
rest = (A/'independent-audit.md').read_text()
for n in reports:
    body = (A/n).read_text(); assert rest.count(body) == 1; rest = rest.replace(body,'',1)
assert not rest.strip()
ev = json.loads((A/'evidence-observations.json').read_text())
assert ev['inventory_total'] == 96 and ev['inventory_matched'] == 25 and ev['inventory_missing'] == 71
assert ev['checker_reported_count'] == 847 and ev['static_count_derivation']['uncounted_guard_assertions'] == 25
assert ev['static_count_derivation']['literal_total_assert_evaluations_on_success'] == 872
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
sourcefix = D/'source-and-evidence-qualifications-after-audit230-20261008.json'
reader = D/'reader-qualifications-after-original-audit230-20261008.json'
binding = K/'P14.8-round230-whole-original-formal-realization309-binding-20261008.json'
accept = D/'whole-original-paper-acceptance-after-audit230-20261008.json'
closure = K/'P14.8-original-formal-data-closure-after-audit230-20261008.json'
pub = D/'evidence/independent-whole-audit230'
assert not any(p.exists() for p in [sourcefix,reader,binding,accept,closure,pub])
write(sourcefix, dict(recorded_utc=now, source_sha256=rep['authoritative_source_sha256'], source_unchanged=True, qualifications=[
    'Main H/O/N/C source applications PASS through directly available complete Demailly statement/proof units, including quantitative weighted dbar, point extension, coherence, closed coherent Frechet topology and Cartan B. Missing original editions are retained as a limitation of that historical citation route, not a gap in the permitted directly verified main route.',
    'Auxiliary DEL subadditivity and strong-openness original editions are INCONCLUSIVE; their auxiliary claims are conditional on those named results. The main arbitrary-formal-data iff and its full-real capped-integral identity do not use them.',
    'Correct the bookkeeping phrase 847 assertions: the checker reports847 selected checks and also evaluates25 uncounted guard assertions, hence872 literal successful assert evaluations. Neither finite arithmetic nor PDF compilation proves the theorem. No checker or build is repeated for this acceptance.',
    'Fenced source presentation is exactly the authoritative46982-byte TeX plus its one separatorLF inside the specified whole wrapper; raw fence payload has46983bytes. Author226 and auditor230 actual FINAL prose differ from their saved expanded prose; identities and support agree, but prose is not assumed equal.',
    'Auditor230 supplied inventory coverage is25/96, with71 absent; ROOT earlier verified96 author artifacts in its separately bound reproduction. The auditor did not newly certify absent artifacts or PDF bytes. ROOT now verifies the authoritative existing14-page PDF hash independently.',
    'Preserve the original ROOT second-pass warning-gate failure, first/second-pass diagnostics, justified third label rerun, final epstopdf no-shell warning, pending builtin134 and unverified universal historical read/operation/provider claims.'
]))
write(reader, dict(recorded_utc=now, source_sha256=rep['authoritative_source_sha256'], source_unchanged=True, qualifications=[
    'Main theorem: arbitrary nonzero coherent ideal arrays A_c at EVERY real c>0 on any connected compact Kahler manifold with smooth closed real pseudoeffective theta are realizable by a nontrivial theta-psh u iff the specified finite holomorphic dyadic-generator, fixed-chart/barrier, vanishing-current-loss, noncollapse and capped-integral certificate exists. No target psh function or multiplier-ideal operator occurs in the finite witness predicates.',
    'Necessity includes exact finite generation of the prescribed ideals, relative fixed-domain kernel truncation at common zeros without uniform-in-m division constants, exact transition-weight cancellation, boundary-safe gluing and usc tail recovery even at poles. Sufficiency gives a canonical locally integrable upper-tail representative and both germ directions of the capped-integral identity at every real exponent.',
    'This is an infinite analytic witness criterion. It quantifies all real exponents, germs, caps and scales and existential holomorphic coefficients; finite decidability, ideal-only algebraic axioms, effective complexity and canonical witness selection are not proved.',
    'Retained datum is exactly the I-array. Pointwise order gives ideal inclusion, scaling reindexes the real array/background, bounded smooth gauge changes preserve ideals, and the finite approximants recover a realization with O(1/m) curvature loss. Raw order reflection, P-sensitive data, canonical raw representatives and raw mass do not follow.',
    'The directly reconstructed Cantor family has one full-real unit I-array and raw nonpluripolar masses spanning[0,1], including zero; divisorial and zero-background endpoints are separate checked examples. No extra zero-mass DXZ interval, all-semivaluation formula, P-envelope mass claim or big non-nef energy/measure theory is asserted.',
    'ROOT elementary scope extension: a compact manifold has finitely many open connected components. Realizability is equivalent to realizability on every component, since plurisubharmonicity, local L1 and multiplier ideals are local, and finitely many componentwise realizations glue. Require nonzero restricted ideals on every component and use the audited criterion componentwise; a zero-dimensional component is a point with the unit array and a constant realization. This finite assembly is a ROOT observation, not a new claim of independent auditor reconstruction.',
    'ROOT read all six actual native230 FINAL notes and every complete unique source/sufficiency/necessity/auxiliary/evidence/original-scope report, plus proof index and coverage. The combined audit file is verified to contain each entire report exactly once and only whitespace separators. Saved expanded audit-notes prose was compared structurally, not claimed independently whole ROOT-read.',
    'Hash verification establishes identities, not semantic reading. Earlier oversized metadata/status searches and displays truncated; they are not evidence of whole semantic historical reads. The authoritative whole mathematical/source reads are separately recorded. Universal past operations and external model certification remain unverified.',
    'This closes the exact original P14.8 disjunctive assignment through meaningful arbitrary-formal-data realization. Its other two alternatives are not separately claimed solved. Other P14 atoms remain OPEN. Use BOTH mandatory annotations with any import. Ordinary native independent review is distinct from a canonical automatic-review receipt.'
]))
pub.mkdir()
safe = reports + ['independent-audit.md','proof-index.md','coverage.json','evidence-observations.json','presentation-comparison.json','commands.json','environment.json','input-integrity.json','integrity.stdout.json','own-manifest.json']
for name in safe: shutil.copyfile(A/name,pub/name)
for p in [actual,K/'round230-registered-native-result.json',K/'round230-actual-final-extraction-binding-20261008.json']:
    shutil.copyfile(p,pub/p.name)
write(pub/'ROOT-publication-binding.json', dict(recorded_utc=now, frozen_files_verified=54, own_files_verified=29, copied_files=[dict(file=n,sha256=sha(pub/n)) for n in safe], third_party_sources_and_page_images_not_copied=True, supplied_programs_not_executed_or_imported=True, actual_FINAL_controlling=True, actual_saved_note_field_comparison=comparison))
write(binding, dict(recorded_utc=now,continuation=309,native_round=230,author_round=226,source_sha256=rep['authoritative_source_sha256'],ROOT_pdf_sha256=rep['ROOT_pdf_sha256'],pages=14,mathematical_verdict='PASS whole main theorem',essential_source_verdict='PASS directly verified permitted route',original_scope_verdict='PASS arbitrary-formal-data disjunction',bounded_evidence_verdict='PASS with mandatory qualifications',auxiliary_DEL_SO_original_editions='INCONCLUSIVE and conditional; not main premises',actual_native_FINAL_sha256=sha(actual),all6_actual_FINAL_ROOT_read=True,all6_unique_expanded_proof_reports_ROOT_read=True,combined_report_exact_whole_assembly_verified=True,saved_expanded_prose_not_claimed_whole_ROOT_read=True,frozen_files_verified=54,own_files_verified=29,source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),source_unchanged=True,no_checker_or_build_repeated=True,ordinary_review_not_canonical_automatic_receipt=True,original_closed=True,protected_editor_unchanged_open=True))
accepted = dict(recorded_utc=now,atom='P14.8',grant_label='O309',cumulative_accepted_paper_number=88,continuation=309,fully_solved_original_atom=True,original_closed=True,completion_alternative='Meaningful arbitrary-formal-data analytic realization criterion',mathematical_verdict='PASS whole original alternative with BOTH mandatory annotations',source=str(D/'P14.8-paper.tex'),source_sha256=rep['authoritative_source_sha256'],pdf=str(D/'P14.8-paper.pdf'),pdf_sha256=rep['ROOT_pdf_sha256'],pages=14,review_binding=str(binding),review_binding_sha256=sha(binding),source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),both_annotations_required_on_import=True,original_statement_unchanged=True,other_P14_original_atoms_closed=False,canonical_automatic_acceptance=False,builtin_compiler_success_claimed=False,originals_solved=10,originals_open=32)
write(accept,accepted)
write(closure,dict(**accepted,acceptance_record=str(accept),acceptance_record_sha256=sha(accept),scope='Every real-index coherent formal array: exact restricted analytic certificate iff complex psh realization; no assumed realizability, positive-mass requirement, raw/P-type reconstruction or finite decision algorithm. Finite connected-component assembly as annotated.'))
for filename in ['active-work.json','checklist-current.json']:
    p=R/filename; x=json.loads(p.read_text())
    assert x['historical_reviewed_scoped_papers']==87 and len(x['fully_solved_original_atoms'])==9 and x['remaining_open_original_atoms']==33 and x['github_pending_checkpoint'] is None
    assert 'P14.8' not in x['fully_solved_original_atoms']
    x['fully_solved_original_atoms'].append('P14.8'); x['fully_solved_original_atoms'].sort(key=lambda a:tuple(int(v) for v in a[1:].split('.')))
    x.update(updated_utc=now,historical_reviewed_scoped_papers=88,remaining_open_original_atoms=32,P14_8_original_formal_realization309_acceptance=accepted,next_work='Continue solving all remaining32original atoms in batches of at most2native Xean gpt-6.1-sol xhigh campaigns. General P14.8 formal-data alternative now solved with both mandatory annotations. P05.1 all-face research231 active; correct failed P1 representative step229 in source308; prepare verified GitHub checkpoint235. Preserve authentication and protected editor.')
    x['new309_original_formal_ideal_candidate'].update(original_closed=True,new_accepted_paper=True,acceptance_record=str(accept),acceptance_record_sha256=sha(accept))
    x['original_candidate_audit230'].update(completed=True,original_closed=True,mathematical_verdict='PASS',essential_source_verdict='PASS',original_scope_verdict='PASS',actual_FINAL=str(actual),actual_FINAL_sha256=sha(actual))
    if filename=='active-work.json': x['full_solutions'].append(dict(atom='P14.8',fully_solved_original_atom=True,original_statement_unchanged=True,source=accepted['source'],source_sha256=accepted['source_sha256'],pdf=accepted['pdf'],pdf_sha256=accepted['pdf_sha256'],pages=14,acceptance_record=str(accept),acceptance_record_sha256=sha(accept),both_annotations_required=True))
    else:
        target=next(t for t in x['targets'] if t['id']=='P14.8'); assert not target['fully_solved']
        target.update(closure='solved',fully_solved=True,research_status='original_scope_completed: whole original audit230 PASS arbitrary-formal-data alternative',reviewed_papers=[accepted],current_focus='Original disjunctive atom closed by analytic formal-data criterion; separate alternatives and other P14 atoms remain separate.')
        x['active_atoms']=['P05.1'];x['original_closure_record']=str(closure);x['original_closure_record_sha256']=sha(closure)
    write(p,x)
lines=(R/'checklist-current.tsv').read_text().splitlines(); changes=0
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P14.8':
        assert row[1]=='open' and row[3]=='0';row[1]='solved';row[2]='original_scope_completed: whole original audit230 PASS arbitrary formal-data realization iff at every real exponent, infinite analytic witness';row[3]='1';lines[i]='\t'.join(row);changes+=1
assert changes==1;(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(original_closed='P14.8',originals_solved=10,originals_open=32,accepted_papers=88,acceptance_sha256=sha(accept),binding_sha256=sha(binding)),indent=2))
