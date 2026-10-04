"""Preserve completed drafts and local checks, without external submission."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def write_new(p, data):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

p35 = R / 'root-checks/original-envelope-round-35-final-reader'
canon = json.loads((p35 / 'canonical-result.json').read_text())
assert canon['candidate'] is False and len(canon['notes']) == 3
read35 = p35 / 'complete-root-argument-read.json'
write_new(read35, {
    'recorded_utc': stamp,
    'historical_full_reads': {
        'argument': 'Final complete argument read in two untruncated units on 2026-10-04 around 10:24 UTC.',
        'canonical_notes': 'All three actual native canonical texts, summaries, detailed summaries and support arrays read around 10:25 UTC.',
        'source_provenance': 'Entire final source-provenance record read around 10:51 UTC.',
    },
    'argument_sha256': sha(p35 / 'P03.1-argument.md'),
    'canonical_result_sha256': sha(p35 / 'canonical-result.json'),
    'source_provenance_sha256': sha(p35 / 'source-provenance.json'),
    'actual_canonical_note_ids': [n['id'] for n in canon['notes']],
    'local_notes_json_is_not_the_canonical_result': True,
    'full_TeX_read': False,
    'root_executed_author_helpers': False,
    'native_editor_verified': False,
    'independent_review_launched': False,
    'accepted_new_analytic_theorem': False,
    'original_atom_closed': False,
    'mathematical_scope': 'Conditional toric reconstruction. Foundations F1/F2/F3 and the original semipositive-RPL or locally-Fubini-Study bridge are unverified; no advance beyond the previously recorded toric sector is accepted.',
    'record_is_read_and_scope_evidence_not_a_proof_certificate': True,
})

source = R / 'shared-sources/Thuillier-tel-00010990v1.txt'
# Python splitlines also splits form feeds. Bind the tool-read LF interval exactly.
lines = source.read_text().split('\n')
unit = '\n'.join(lines[4103:4277]) + '\n'
source_read = R / 'shared-sources/P03-Thuillier-smooth-realization-root-read-20261004.json'
write_new(source_read, {
    'recorded_utc': stamp,
    'public_url': 'https://theses.hal.science/tel-00010990v1/document',
    'original_text_cache': str(source),
    'source_sha256': sha(source),
    'LF_first_line': 4104,
    'LF_last_line': 4277,
    'unit_sha256': hashlib.sha256(unit.encode()).hexdigest(),
    'full_unit_read_untruncated': True,
    'contents': 'Definitions 3.2.1; Propositions 3.2.2, 3.2.4 and 3.2.5 including their complete proofs; Proposition 3.2.7 and Lemma 3.2.8 including complete proofs.',
    'standing_hypotheses': 'Smooth strictly k-analytic curve. Semistable realization in Proposition 3.2.4 uses finite separable field extension and legal skeletal decompositions.',
    'OCR_condition': 'Literal public extraction has corrupted French glyphs. This record does not silently repair the source or resolve ambiguous symbols.',
    'new_application_accepted': False,
    'current_author_inputs_changed': False,
})

out = G / 'local-packet-continuation47.json'
snapshot = G / 'continuation47-local-records'
assert not out.exists() and not snapshot.exists()
snapshot.mkdir()
files = [Path(__file__), source_read,
    R / 'prepare_original_envelope_continuity_review_20261004.py',
    R / 'prepare_public_source_envelope_continuations_20261004.py',
    R / 'record_public_source_envelope_launch_20261004.py',
    R / 'public-source-envelope-continuation-manifest-20261004.json',
    R / 'public-source-envelope-continuation-launch-20261004.json',
    R / 'P03-public-primary-cache-manifest-20261004.json',
    R / 'shared-sources/P03-additional-public-primary-root-read-20261004.json',
]
for n in [35, 36]:
    directory = R / 'root-checks' / f'original-envelope-round-{n}-final-reader'
    files.extend(p for p in directory.iterdir()
                 if p.is_file() and p.suffix in {'.md', '.tex', '.json', '.py', '.sh', '.log'})
    if n == 36:
        files.append(directory / 'reproduction/P03.3-paper.pdf')
for n, stem in [(37, 'P03.1-public-source-geometric-positivity'),
                (38, 'P03.3-public-source-geometric-continuity')]:
    directory = R / 'campaigns' / f'round-{n}' / stem
    files.extend(directory / name for name in ['input.json', 'input-manifest.json', 'settings.json'])
review = R / 'campaigns/round-36/P03.3-original-envelope-continuity-review'
files.extend(review / name for name in ['task.json', 'argument.md', 'settings.json', 'freeze.json', 'submission-auto-review-rejection.json'])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    src = R / name
    dst = snapshot / name
    shutil.copy2(src, dst)
    assert sha(src) == sha(dst)
    files.append(dst)
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file(), str(p)
    entries.append({'local': str(p),
                    'path': 'research-checkpoints/continuation47/' + str(p.relative_to(R)),
                    'sha256': sha(p), 'bytes': p.stat().st_size})
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
write_new(out, {
    'prepared_utc': stamp,
    'state': 'LOCAL ONLY; no GitHub mutation, model call, review resubmission or current-author feedback.',
    'files': entries, 'file_count': len(entries),
    'original_atoms': 42, 'fully_solved_original_atoms': [],
    'selected_atoms': ['P03.1', 'P03.3'],
    'completed_draft_scope': {'round35': 'Unverified conditional toric reconstruction; no accepted new analytic result.',
                              'round36': 'Fully read and locally reproduced abstract graph/topological criterion; every geometric application remains unverified, independent review blocked pending approval.'},
    'current_batch': 'Rounds 37 and 38 native authors running from original tasks and five published primary caches; output drafts not included or accepted before completion.',
    'previous_local_packet': str(G / 'local-packet-continuation46.json'),
    'last_verified_remote_commit': '604fea852c6a27d4cdc83d97f17393ea67087301',
    'pending_GitHub43_manifest_sha256': sha(pending),
    'blocked_original_scope_audit_not_resubmitted': True,
    'blocked_P03_3_review_not_resubmitted': True,
    'whole_uploaded_PDF_or_extract_included': False,
    'private_raw_conversations_sql_auth_runtime_included': False,
    'public_primary_PDF_cache_files_included': False,
    'native_editor_limitation': 'Historical native tools returned No handler; latest R36 requests were unresponsive and terminated without diagnostics. Sources preserved; local reproduction PDF included. Native verification and editor opening are unconfirmed.',
})
print(json.dumps({'manifest': str(out), 'sha256': sha(out), 'files': len(entries),
                  'external_upload': False, 'original_atoms_closed': 0}, indent=2))
