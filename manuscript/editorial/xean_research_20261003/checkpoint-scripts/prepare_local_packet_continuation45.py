"""Freeze a local-only checkpoint; do not retry either blocked export."""
from pathlib import Path
import datetime, hashlib, json, shutil

R = Path('/workspace/research')
CP = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
active = json.loads((R / 'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha'] == '604fea852c6a27d4cdc83d97f17393ea67087301'
pending = active['github_pending_checkpoint']
assert sha(pending['manifest']) == pending['manifest_sha256']
assert pending['files'] == 76 and 'pending' in pending['state']
snapshot = CP / 'continuation45-local-records'
snapshot.mkdir(exist_ok=False)
prefix = 'manuscript/editorial/xean_research_20261003/'
files = []

def add(path, target, mutable=False):
    path = Path(path)
    assert path.is_file(), path
    if mutable:
        copy = snapshot / (str(len(files)) + '-' + path.name)
        shutil.copyfile(path, copy)
        path = copy
    destination = prefix + target
    assert destination not in {f['path'] for f in files}, destination
    files.append({'local': str(path), 'path': destination, 'sha256': sha(path)})

for n, atom, stem, worker in [
    (31, 'P15.1', 'P15.1-minimum-reference-finite-energy', 'codex-7YBaVo'),
    (32, 'P15.2', 'P15.2-minimum-reference-full-mass-operator', 'codex-UNkbGs')]:
    out = R / f'deliverables/round-{n}'
    manifest_path = R / f'deliverables/round-{n}-bundle-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    for name, pin in manifest['entries'].items():
        assert sha(out / name) == pin
        add(out / name, f'deliverables/round-{n}/' + name)
    assert sha(manifest['bundle']) == manifest['sha256']
    add(manifest['bundle'], 'deliverables/' + Path(manifest['bundle']).name)
    for name in ['bundle-manifest.json', 'source-preparation.json', 'native-request-status.json', 'visual-check.json']:
        p = R / f'deliverables/round-{n}-{name}'
        add(p, 'deliverables/' + p.name)
    add(out / 'first-page.png', f'deliverables/round-{n}/first-page.png')
    if n == 31:
        p = R / 'deliverables/round-31-spacing-notice-visual-check.json'
        add(p, 'deliverables/' + p.name)
        add(out / 'spacing-paragraph-page.png', 'deliverables/round-31/spacing-paragraph-page.png')
    review = R / f'campaigns/round-{n}' / (stem + '-review')
    for name in ['review-result.json', 'review-read-attestation.json', 'publication-edits.json']:
        add(review / name, f'campaigns/round-{n}/' + review.name + '/' + name)
    for phase in [1, 2]:
        d = R / 'root-checks' / (f'minimum-reference-zero-volume-{atom}-phase{phase}')
        for p in sorted(d.glob('*.json')):
            add(p, 'root-checks/' + d.name + '/' + p.name)
    author = R / f'campaigns/round-{n}' / stem / 'artifacts' / worker
    names = [atom + '-partial.tex', atom + '-argument.md', 'source-audit.json',
             'author-audit.json', 'research-audit.json', 'build-audit.json',
             'status.json', 'build.py', 'verify_sources.py']
    names += ['n1.md', 'n2.md', 'n3.md', 'n4.md', 'native_note_texts.py', 'coefficient_check.py'] if n == 31 else ['P15.2-proof.md', 'package_notes.py', 'checks.py', 'execution-audit.md']
    for name in names:
        add(author / name, f'campaigns/round-{n}/' + stem + '/author/' + name)
    audit = R / f'campaigns/round-{n}' / (stem + '-original-scope-audit')
    for name in ['construction-memo.md', 'original-dossier.txt', 'argument.md', 'task.json', 'settings.json', 'freeze.json']:
        add(audit / name, f'campaigns/round-{n}/' + audit.name + '/' + name)
    if n == 32:
        name = 'submission-auto-review-rejection.json'
        add(audit / name, f'campaigns/round-{n}/' + audit.name + '/' + name)

batch_path = R / 'observable-zero-volume-batch-manifest.json'
batch = json.loads(batch_path.read_text())
assert not batch['launched'] and not batch['external_submission']
for c in batch['campaigns']:
    d = Path(c['directory'])
    assert sha(d / 'input.json') == c['input_sha256']
    assert sha(d / 'settings.json') == c['settings_sha256']
    for name in ['input.json', 'settings.json', 'input-manifest.json']:
        add(d / name, 'campaigns/' + d.parent.name + '/' + d.name + '/' + name)
for name in ['P15-original-completion-review-future-plan-20261004.json',
             'P15-observable-carrier-future-proposal-20261004.md',
             'P15-observable-unbounded-potentials-future-addendum-20261004.md',
             'P15-observable-weighted-convergence-future-addendum-20261004.md',
             'P15-degree-zero-more-singular-rigidity-future-addendum-20261004.md',
             'P15-observable-carrier-full-evidence-20261004.md',
             'observable-zero-volume-batch-manifest.json']:
    add(R / name, 'future-research/' + name)
for name in ['record_minimum_reference_zero_volume_root_read.py',
             'record_minimum_reference_operator_reproduction_v2.py',
             'record_minimum_reference_zero_volume_review.py',
             'prepare_minimum_reference_zero_volume_paper.py',
             'export_minimum_reference_zero_volume_paper.py',
             'publish_minimum_reference_zero_volume_papers.py',
             'publish_minimum_reference_zero_volume_papers_v2.py',
             'prepare_zero_volume_original_scope_audit.py',
             'prepare_observable_zero_volume_batch.py',
             'refresh_checklist_minimum_reference.py']:
    add(R / name, 'checkpoint-scripts/' + name)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(R / name, name, mutable=True)
add(Path(__file__), 'checkpoint-scripts/' + Path(__file__).name)
note = snapshot / 'CHECKPOINT.txt'
note.write_text('Local packet45. R31 energy exact scoped PASS10premises/28passages and R32 operator exact scoped PASS11premises/26passages fully root read, source-bound and reproduced, published16/14-page papers and full supporting packets. Native opening/compiler requests remain unconfirmed; two successful local PDF builds each; one energy spacing notice directly visually checked. Reproduction R32 mathematical core/TEX/primary annex byte-identical; full argument differs only in new PDF digest, exact substitution bound and initial overstrict assertion preserved. Literal-original-scope audits for both targets prepared locally; P15.2 submission was rejected by automatic approval review because of unpublished generated research, explicit user approval requested. No original audit launched. The next fresh two-target observable-carrier batch33/34 is prepared LOCAL_ONLY, all new proposals UNVERIFIED and no provider submission attempted. All42originalsopen; goalACTIVE. GitHub43 remains blocked pending its specific export approval; last remote604fea852c6a27d4cdc83d97f17393ea67087301. This packet makes no network mutation and generates no push script. No credentials, SQL, private raw native transcripts, whole primary PDFs or whole archival texts are included.\n')
add(note, 'CHECKPOINT.txt')
record = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'repository': 'MingchenXia/nonarchimedean-pluripotential-theory',
          'branch': 'codex/xean-research-20261003',
          'state': 'LOCAL_ONLY; no network mutation, external upload or retry of a blocked action.',
          'last_successful_remote_commit': active['github_checkpoint']['commit_sha'],
          'prior_pending_export_manifest': pending['manifest'],
          'prior_pending_export_manifest_sha256': pending['manifest_sha256'],
          'files': files, 'files_count': len(files), 'private_raw_transcripts_or_whole_primary_PDFs': False,
          'fully_solved_original_atoms': []}
out = CP / 'local-packet-continuation45.json'
assert not out.exists()
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'local_packet': str(out), 'sha256': sha(out), 'files': len(files), 'network_mutation': False}))
