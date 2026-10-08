from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-226/P14.8-original-formal-multiplier-ideal-data-realization-and-admissibility-paper'
A = C / 'artifacts/codex-H5hq67'
D = K / 'public-P14.8-continuation309-general-formal-ideal-realization-candidate'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, j: Path(p).write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
protected_hash = '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert not D.exists() and sha(protected) == protected_hash
assert sha(A / 'P14.8-paper.tex') == 'fed5ac5c0dae5bd931cc1e96b92640382b09283d0d201c32c2d1aee9e739f074'
b = json.loads((A / 'artifactbindings.json').read_text())
assert len(b['artifacts']) == 96
for e in b['artifacts']:
    p = A / e['file']; assert p.is_relative_to(A) and p.is_file()
    assert p.stat().st_size == e['bytes'] and sha(p) == e['sha256']
inputs = json.loads((A / 'source-inventory.json').read_text())
assert len(inputs) == 9
for e in inputs:
    assert Path(e['path']).stat().st_size == e['bytes'] and sha(e['path']) == e['sha256']
raw = (A / 'P14.8-paper.tex').read_bytes()
fenced = b'# Complete author TeX source (source-derived Markdown)\n\nThis fenced copy is the full mathematical argument, not a typeset conversion.\n\n```tex\n' + raw + b'\n```\n'
assert fenced == (A / 'paper-source.md').read_bytes()
actual = json.loads((K / 'round226-actual-native-final.json').read_text())
saved = json.loads((A / 'native-notes.json').read_text())
assert actual['candidate'] is True and saved['candidate'] is True and len(actual['notes']) == len(saved['notes']) == 5
fields = []
for a, s in zip(actual['notes'], saved['notes']):
    fields.append(dict(actual_id=a.get('id'), saved_id=s.get('id'), equal_fields=[k for k in sorted(set(a)|set(s)) if a.get(k)==s.get(k)], differing_fields=[k for k in sorted(set(a)|set(s)) if a.get(k)!=s.get(k)]))
D.mkdir(); E = D / 'evidence'; E.mkdir(); S = E / 'ROOT-reproduction'; S.mkdir(); (S / 'build').mkdir()
for name in ['verify_examples.py','example-input.json','P14.8-paper.tex']: shutil.copyfile(A / name, S / name)
with (S / 'example-check.stdout.json').open('wb') as out:
    p = subprocess.run(['python', str(S / 'verify_examples.py')], cwd=S, stdout=out, stderr=subprocess.PIPE)
(S / 'example-check.stderr.txt').write_bytes(p.stderr)
assert p.returncode == 0 and (S / 'example-output.json').read_bytes() == (A / 'example-output.json').read_bytes()
assert json.loads((S / 'example-output.json').read_text())['exact_assertions'] == 847
commands = []
for n in [1,2]:
    argv = ['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P14.8-paper.tex']
    p = subprocess.run(argv, cwd=S, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (S / f'pdflatex-pass{n}.stdout.log').write_bytes(p.stdout)
    shutil.copyfile(S / 'build/P14.8-paper.log', S / f'pdflatex-pass{n}.tex.log')
    commands.append(dict(argv=argv, exit_code=p.returncode)); assert p.returncode == 0
warnings = [l for l in (S / 'pdflatex-pass2.tex.log').read_text().splitlines() if re.search(r'Warning|Overfull|Underfull|Undefined',l)]
assert warnings == ['Package epstopdf Warning: Shell escape feature is not enabled.']
assert sha(S / 'P14.8-paper.tex') == sha(A / 'P14.8-paper.tex')
info = subprocess.run(['pdfinfo',str(S / 'build/P14.8-paper.pdf')],capture_output=True,text=True,check=True)
(S / 'pdfinfo.txt').write_text(info.stdout)
pages = int(re.search(r'^Pages:\s+(\d+)',info.stdout,re.M).group(1)); assert pages == 14
for name in ['P14.8-paper.tex','paper-source.md','argument.md','source-application-ledger.md','scope-and-gaps.md','sourcecoverage.md','execution-observations.md']: shutil.copyfile(A / name,D / name)
shutil.copyfile(S / 'build/P14.8-paper.pdf',D / 'P14.8-paper.pdf')
for name in ['round226-actual-native-final.json','round226-registered-native-result.json','round226-actual-final-extraction-binding-20261008.json']: shutil.copyfile(K / name,E / name)
for name in ['native-notes.json','artifactbindings.json','source-inventory.json','sourcecoverage.json','build-receipt.json','example-output.json','final-checks.json','final-delivery-receipt.json','initial-inventory-failure.log','environment.json','rerun.md','build-pass-1.log','build-pass-2.log']:
    p = E / 'author-evidence' / name; p.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(A / name,p)
for p in sorted((A / 'LOCALONLY').glob('initial-build-*')):
    dst = E / 'author-evidence/retained-initial-diagnostics' / p.name; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst)
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), continuation=309, author_round=226, status='Complete original P14.8 author candidate, unreviewed', original_candidate_claim=True, original_closed=False, new_accepted_paper=False, counts=dict(original_solved=9,original_open=33,accepted_scoped_papers=85), verified_author_artifacts=96, verified_bound_math_primary_original_task_files=9, all_five_actual_FINAL_notes_physically_ROOT_read=True, entire_46982_byte_TeX_physically_ROOT_read=True, entire_ledger_scope_sourcecoverage_and_declared_execution_observations_physically_ROOT_read=True, entire_saved_expanded_FINAL_prose_physically_ROOT_read=False, actual_and_saved_payloads_equal=False, actual_saved_note_field_comparison=fields, authoritative_source_sha256=sha(D / 'P14.8-paper.tex'), entire_fenced_Markdown_exact_copy=True, short_argument_MD_not_claimed_equivalent_or_whole_ROOT_read=True, safe_3340_byte_checker_and_274_byte_input_physically_ROOT_read_before_execution=True, copied_checker_executions=1, finite_assertions=847, exact_saved_example_output=True, ROOT_pdf_sha256=sha(D / 'P14.8-paper.pdf'), ROOT_pdf_pages=pages, commands=commands, final_warnings=warnings, retained_historical_failures_and_initial_build_warnings=True, author_emitters_binders_builders_not_executed=True, pending_source_validation=['H weighted singular dbar','O point extension','N coherence','C coherent Frechet closedness and Cartan B'], independent_original_scope_and_proof_audit_pending=True, no_effective_finite_algebraic_decision_procedure_claim=True, no_canonical_I_model_or_raw_mass_reconstruction_claim=True, private_active_output_read=False, hot_feedback_sent=False, protected_editor_unchanged_open=True)
write(D / 'ROOT-reproduction-binding-20261008.json',record)
assert sha(protected) == protected_hash
print(json.dumps(dict(directory=str(D),pages=pages,finite_assertions=847,source_sha256=record['authoritative_source_sha256'],author_original_candidate=True,original_closed=False),indent=2))
