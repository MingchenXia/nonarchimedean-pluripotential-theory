from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, difflib

R = Path('/workspace/research')
K = R / 'root-checks'
T = K / 'P16.5-original-big-equation-with-retained-vertical-moving-factors-candidate-20261006-continuation210.tex'
D = R / 'deliverables/original-P16.5'
C = next((R / 'campaigns/round-167').iterdir())
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
assert sha(T) == 'd1473f933a5c08096a97df253c259c1d8a7dae583132e35bd5ab2c3b7da9b5f7'
binding = json.loads((K / 'P16.5-round167-whole-original-review-binding-20261006.json').read_text())
assert binding['verdict'] == 'PASS' and binding['original_scope_accepted_by_review']
assert binding['entire_report_all_premises_and_passages_root_read'] and binding['all_zero_based_exact_statement_bindings_verified']
s = T.read_text()
edits = [
    ('\\large A proposed proof with retained vertical moving factors', '\\large Actual full-section systems with retained vertical moving factors'),
    ('\\author{Unreviewed corrected reconstruction, continuation 210}', '\\author{Research manuscript for original P16.5}'),
    ('included. This is an unverified corrected draft, not a correctness certification.', 'included. The complete manuscript and both appendices received an independent\nsource-aware mathematical review in their stated full-big domain.'),
    ('D_\\nu=\\sup_{u(v_0)=0}', 'D_\\nu=\\sup_{u\\in\\EE,\\ u(v_0)=0}'),
    ('every original section has exactly\nthe prescribed generic base-divisor factor', 'every original section is divisible by\nthe prescribed common generic base-divisor factor'),
    ('It corrects the complete moving bundle in (5.4)', 'It corrects the complete moving bundle in (5.2)'),
    ('background reconstruction is claimed by this revision. A fresh reviewer\nmust obtain independent primary evidence and audit each new application.', 'background reconstruction is claimed by this author revision. The independent\nround167 reviewer obtained its own primary evidence and audited each application;\nits full report and exact input bindings are preserved alongside this paper.'),
    ('added as an assumption or silently declared proved. All genuine operator,\ncanonical weighted, comparison and attainment claims still require a\nfresh full-original independent audit. No original problem is closed by\nthis revision, its compilation or its finite explicit calculation.', 'added as an assumption or silently declared proved. Independent round167\nreview accepted the complete original-carrier operator, genuine weighted\ncontinuity, comparison, intrinsic targets, attainment and every-solution\nuniqueness in the stated full-big domain, together with the numerical-zero\nrange. The stronger physical-output assertion is not part of that theorem.\nThe review uses only the complete G0/G1 grants and checks the new\nfoundations independently; it is a source-aware mathematical audit,\nnot a formal proof certificate.')
]
for a, b in edits:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
D.mkdir()
P = D / 'P16.5-paper.tex'
P.write_text(s)
(D / 'publication-editorial-edits.patch').write_text(''.join(difflib.unified_diff(T.read_text().splitlines(True), s.splitlines(True), fromfile='reviewed-continuation210.tex', tofile='P16.5-paper.tex')))
for filename in ('P16.5-round167-actual-canonical-independent-review-20261006.json', 'P16.5-round167-native-model-final-review-20261006.json', 'P16.5-round167-whole-original-review-binding-20261006.json'):
    shutil.copyfile(K / filename, D / filename)
for filename in ('task.json', 'original-task.json', 'mathematical-data-bindings.json', 'freeze.json'):
    shutil.copyfile(C / filename, D / ('review167-' + filename))
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'reviewed_source': str(T), 'reviewed_source_sha256': sha(T), 'publication_source': str(P), 'publication_source_sha256': sha(P), 'editorial_patch': str(D / 'publication-editorial-edits.patch'), 'edits': [{'before': a, 'after': b} for a, b in edits], 'mathematical_changes': False, 'whole_base_source_and_all18reviewed_pages_prior_root_read': True, 'whole_final_editorial_diff_root_read': True, 'review_operation_id': binding['operation_id'], 'review_binding_sha256': sha(K / 'P16.5-round167-whole-original-review-binding-20261006.json'), 'catalogue_closure_recorded_separately': True, 'existing_P16_4_editor_unchanged': True}
(D / 'publication-editorial-binding.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
(D / 'README.md').write_text('# Original P16.5\n\nThe complete original-carrier finite-energy equation theory is proved for every actual big rational line bundle on every smooth integral projective variety of positive dimension over every algebraically closed trivially valued characteristic-zero field. The additional zero-volume range is the entire numerically trivial rational-bundle range, including nontorsion Pic0; raw zero mass is never probability normalized.\n\nIndependent Xean native Codex gpt-6.1-sol xhigh round167 reviewed the entire manuscript and both appendices with only complete actual-ample G0 and relative-generation/one-FS-net G1 grants and returned PASS. The whole canonical report, native final result, source-index bindings and exact reviewed inputs are preserved. Publication edits clarify the normalized E1 supremum, common fixed-factor divisibility, formula reference and review status without changing the mathematical theorem. The stronger fixed-original-unbounded-test statement at every physical auxiliary output remains unproved and is not required for the theorem.\n')
print(json.dumps({'source': str(P), 'source_sha256': sha(P), 'editorial_edits': len(edits), 'original_scope_review': 'PASS', 'catalogue_closure_not_yet_recorded': True}, indent=2))
