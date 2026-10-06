from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
D = R / 'deliverables/original-P16.5'
C = next((R / 'campaigns/round-167').iterdir())
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
T = D / 'P16.5-paper.tex'
P = D / 'P16.5-paper.pdf'
assert sha(T) == '60f24de42bfb09275e412605a9d19d30510e9c456130662cab2ceacf0aaac310'
assert sha(P) == 'e702831373fa1d67fcb1cb58cccfbf14309a7f0dfeda70f87049bf8b4f9f8ff9'
assert int(subprocess.check_output(['pdfinfo', str(P)], text=True).split('Pages:')[1].split()[0]) == 18
assert not any(s in (D / 'P16.5-paper.log').read_text() for s in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
reviewfile = K / 'P16.5-round167-actual-canonical-independent-review-20261006.json'
review = json.loads(reviewfile.read_text())
reviewbindingfile = K / 'P16.5-round167-whole-original-review-binding-20261006.json'
rb = json.loads(reviewbindingfile.read_text())
assert review['verdict'] == rb['verdict'] == 'PASS'
assert rb['original_scope_accepted_by_review'] and rb['entire_report_all_premises_and_passages_root_read']
assert rb['all_zero_based_exact_statement_bindings_verified']
assert rb['canonical_review_sha256'] == sha(reviewfile)
assert len(review['premises']) == 13 and len(review['passages']) == 18
for filename, key in [('task.json','task_sha256'), ('argument.md','argument_sha256'), ('settings.json','settings_sha256')]:
    assert sha(C / filename) == json.loads((C / 'freeze.json').read_text())[key]
pub = {'recorded_utc': now, 'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(P), 'pdf_sha256': sha(P), 'pages': 18, 'source_lines': 1681, 'whole_final_source_root_read': True, 'root_source_read_method': 'Whole previously read1678-LF210 source plus complete8 initial and3 final editorial edits; complete final patch reviewed. All18 publication pages visually read; final pages1,2,16 newly reread and remaining15 pages exact-render identical to prior whole18-page visual reading.', 'actual_visual_pages': list(range(1,19)), 'final_newly_visual_pages': [1,2,16], 'other_final_render_identical_pages': [n for n in range(1,19) if n not in (1,2,16)], 'native_final_compile': 'SUCCESS', 'two_pass_final_local_compile': 'SUCCESS', 'warnings': 0, 'overfull': 0, 'underfull': 0, 'undefined': 0, 'editorial_patch': str(D / 'publication-editorial-edits.patch'), 'editorial_patch_sha256': sha(D / 'publication-editorial-edits.patch'), 'mathematical_changes_after_review': False, 'full_original_scope_review': 'PASS', 'review_binding': str(reviewbindingfile), 'review_binding_sha256': sha(reviewbindingfile), 'complete_caller_grants': ['G0 actual ample', 'G1 relative generation and one FS net'], 'existing_editor_unchanged': True, 'review_limit': 'Source-aware computational mathematical audit by the requested native model; not a formal proof certificate or priority claim.'}
assert not (D / 'publication-binding.json').exists()
(D / 'publication-binding.json').write_text(json.dumps(pub, ensure_ascii=False, indent=2) + '\n')
scope = 'Every actual big rational line bundle on every smooth integral projective variety of dimension n>=1 over every algebraically closed trivially valued characteristic-zero field. Entire genuine original-carrier psh/E1/mixed operator, intrinsic relative finite-energy target condition, actual existence and every-solution uniqueness modulo constants, Borel comparison and arbitrary-support Radon targets; no countability, support, toric, invariance or section-ring finite-generation restrictions. Additional zero-volume range: every actual numerically trivial rational bundle, including nontorsion Pic0, with literal raw-zero equation and constant cone. Nonzero nonbig zero-volume range excluded; stronger fixed-original-unbounded physical-output assertion not required or proved.'
solution = {'atom': 'P16.5', 'fully_solved_original_atom': True, 'original_statement_unchanged': True, 'accepted_paper_number': 64, 'published_utc': now, 'exact_scope': scope, 'source': str(T), 'source_sha256': sha(T), 'pdf': str(P), 'pdf_sha256': sha(P), 'pages': 18, 'review': str(reviewfile), 'review_sha256': sha(reviewfile), 'verdict': 'PASS', 'operation_id': review['operationId'], 'reported_utc': review['reportedAt'], 'premises': 13, 'passages': 18, 'entire_report_premises_and_passages_root_read': True, 'all_zero_based_exact_statement_bindings_verified': True, 'reviewed_original_task_sha256': sha(C / 'original-task.json'), 'reviewed_review_task_sha256': rb['frozen_task_sha256'], 'reviewed_argument_sha256': rb['frozen_argument_sha256'], 'native_compilation': 'SUCCESS', 'local_two_pass_compilation': 'SUCCESS', 'publication_binding': str(D / 'publication-binding.json'), 'publication_binding_sha256': sha(D / 'publication-binding.json'), 'review_limit': pub['review_limit']}
prior = json.loads((R / 'active-work.json').read_text())
assert len(prior['fully_solved_original_atoms']) == 8 and prior['historical_reviewed_scoped_papers'] == 63 and prior['remaining_open_original_atoms'] == 34
assert 'P16.5' not in prior['fully_solved_original_atoms']
closure = K / 'P16.5-round167-original-closure-and-publication-record-20261006.json'
assert not closure.exists()
solved = sorted(prior['fully_solved_original_atoms'] + ['P16.5'])
closure.write_text(json.dumps({'recorded_utc': now, 'new_original_closure': solution, 'all_fully_solved_original_atoms': solved, 'remaining_open_original_atoms': 33, 'historical_reviewed_scoped_papers': 64, 'count_meaning': 'Cumulative independently accepted research papers, including full original-scope papers; P16.5 is new accepted paper64.', 'previous_original_closure_record': prior['original_closure_record'], 'previous_original_closure_record_sha256': prior['original_closure_record_sha256'], 'other_originals_closed': False}, ensure_ascii=False, indent=2) + '\n')
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 8 and j['historical_reviewed_scoped_papers'] == 63
    j.update(updated_utc=now, fully_solved_original_atoms=solved, remaining_open_original_atoms=33, historical_reviewed_scoped_papers=64, original_P16_5_full_solution=solution, original_closure_record=str(closure), original_closure_record_sha256=sha(closure), P16_5_actual_full_original_review167=rb, P19_2_actual_original_scope_review169=json.loads((K / 'P19.2-round169-whole-original-review-binding-20261006.json').read_text()), P19_2_completed_partial_author168=json.loads((K / 'P19.2-round168-completed-partial-original-and-input-binding-20261006.json').read_text()), P19_2_minimal_raw_mass_counterexample212=json.loads((K / 'public-P19.2-continuation212-model-energy-and-raw-profile-reader/publication-binding.json').read_text()), P19_2_launched_minimal_original_review170=json.loads(next((R / 'campaigns/round-170').iterdir()).joinpath('launch-record.json').read_text()), github_pending_checkpoint='continuation180 originalP16.5 closure and completed research evidence', goal_state='9/42 original problems independently accepted;33 open;64 cumulative accepted research papers. WholeP16.5 review167 PASS and final18-page paper published locally.169 P19.2 mathematical dS obstruction checked but exact original scope INCONCLUSIVE;168 candidatefalse partial10-page paper preserved.170 audits whole11-page minimal raw-mass/NA-energy candidate212 with only completeR; no P19.2 closure. Continue small batches of at most2 and regular GitHub checkpoints.')
    if name == 'active-work.json':
        j['full_solutions'].append(solution)
    else:
        target = next(t for t in j['targets'] if t['id'] == 'P16.5')
        assert target['closure'] == 'open' and not target['fully_solved']
        target.update(closure='solved', fully_solved=True, research_status='original_scope_completed', original_scope_solution=solution, current_remaining_gaps=[])
        target['reviewed_papers'].append({'scope': scope, 'source': str(T), 'pdf': str(P), 'review': str(reviewfile), 'full_original_atom_solved': True, 'verdict': 'PASS', 'accepted_paper_number': 64})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
rows = (R / 'checklist-current.tsv').read_text().splitlines()
for i, row in enumerate(rows):
    cells = row.split('\t')
    if cells[0] == 'P16.5':
        cells[1:4] = ['solved', 'original_scope_completed: independent whole167 PASS, final18-page actual-big and numerical-zero theorem', str(int(cells[3])+1)]
    elif cells[0] == 'P19.2':
        cells[2] = '169 mathematical dS obstruction checked, original-scope INCONCLUSIVE.168 candidatefalse partial10-page results.170 whole11-page minimal NA-energy/raw-mass obstruction review active. Original open;9/42,64 accepted papers.'
    rows[i] = '\t'.join(cells)
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
print(json.dumps({'new_original': 'P16.5', 'originals_solved': 9, 'originals_open': 33, 'cumulative_accepted_papers': 64, 'closure': str(closure), 'closure_sha256': sha(closure)}, indent=2))
