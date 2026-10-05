"""Bind actual selected primary reading and record the verified109 receipt."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
B = R / 'root-checks/P16.2-continuation110-primary-units'
O = R / 'campaigns/round-37/P03.1-public-source-geometric-positivity/artifacts/codex-7S9ct1'
note = R / 'root-checks/P16.2-original-continuous-majorants-and-Radon-lift-20261005-continuation110.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists()
B.mkdir()
source = next(u for u in json.loads((O / 'source-provenance.json').read_text())['sources'] if u['id'] == 'Ber')
assert sha(source['pdf']) == source['actual_pdf_sha256']
assert sha(source['literal_extract']) == source['actual_text_sha256']
pages = Path(source['literal_extract']).read_text().split('\f')
extract = O / 'source-extracts/Ber-analytification-and-properness.literal.txt'
assert extract.read_text() == '\f'.join(pages[47:51])
assert sha(extract) == '8d68d0f58de891353afc5b4cf9fce0c1b70375c455a89f193d707cd3780341c0'
p = B / 'Berkovich-analytic-functor-separatedness-and-surjectivity.txt'
shutil.copyfile(extract, p)
units = [{
    'path': str(p), 'sha256': sha(p), 'url': source['url'],
    'version': 'Berkovich, Etale cohomology for non-Archimedean analytic spaces, IHES78(1993)',
    'full_pdf': source['pdf'], 'actual_pdf_sha256': sha(source['pdf']),
    'full_literal_text': source['literal_extract'], 'actual_text_sha256': sha(source['literal_extract']),
    'inclusive_one_based_pdf_pages': [48, 51],
    'extraction_rule': 'UTF-8 decoded full text split on form feed; join pages[47:51] with form feed; no added LF.',
    'selected_statement_and_proof_units_used': ['2.6.1', '2.6.7', '2.6.8'],
    'entire_selected_unit_root_read': True, 'whole_primary_root_read': False,
    '2_6_9_printed_statement_present_but_cross_referenced_proof_not_read_or_used': True,
}]
u = next(u for u in json.loads((R / 'root-checks/P16.5-continuation106-primary-units/binding.json').read_text())['units']
         if u['id'] == 'divisorial-determination-4-22')
assert sha(u['path']) == u['sha256']
p = B / 'BJ-divisorial-inequalities-to-usc-obstacles.txt'
shutil.copyfile(u['path'], p)
units.append({**u, 'original_selection': u['path'], 'path': str(p),
              'entire_selected_unit_root_read': True, 'whole_primary_root_read': False})
binding = {'recorded_utc': datetime.now(timezone.utc).isoformat(),
           'note': str(note), 'note_sha256': sha(note), 'entire_note_root_read': True,
           'independent_review_performed': False, 'original_closed': False,
           'units': units, 'exact_ample_grant_only': 'P16.1 theorem reviewed99',
           'new_math_dependencies_unreviewed': ['109 full genuine cone and whole bad-fiber vanishing',
                                              '108 actual E1 polar test', '109 genuine local products'],
           'active108_109_private_outputs_read_or_used': False,
           'hot_feedback_sent': False}
(B / 'binding.json').write_text(json.dumps(binding, ensure_ascii=False, indent=2) + '\n')
receipt = json.loads((G / 'push-receipt-continuation109.json').read_text())
assert receipt['commit_sha'] == '6c479cb43325976f9bb0ad13fc391ff495c125e2'
assert sha(G / 'upload-manifest-continuation109.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                              'independent_native_git_tree_verified'])
assert len(receipt['fully_solved_original_atoms']) == 6
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms']) == 6
    d['updated_utc'] = receipt['verified_utc']
    d['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    d['github_pending_checkpoint'] = None
    d['continuation110_unreviewed_P16_2'] = {'note': str(note), 'sha256': sha(note),
                                          'binding': str(B / 'binding.json'), 'original_closed': False,
                                          'hot_feedback_sent': False}
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'latest_verified_commit': receipt['commit_sha'], 'binding': str(B / 'binding.json'),
                  'note_sha256': sha(note), 'original_closed': False}, indent=2))
