"""Freeze reviewed fibration papers and their publication/review evidence."""
from pathlib import Path
import datetime, hashlib, json, shutil

r = Path('/workspace/research'); cp = r / 'github-checkpoint'
parent = '5d85116a913c50e509e185d87e97760b1abe75e1'
active = json.loads((r / 'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha'] == parent
assert active['selected_atoms'] == ['P15.1', 'P15.2'] and not active['full_solutions']
snapshot = cp / 'continuation40-uploaded-live-records'; snapshot.mkdir(exist_ok=False)
prefix = 'manuscript/editorial/xean_research_20261003/'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
files = []

def add(path, target, mutable=False):
    path = Path(path); assert path.is_file(), path
    if mutable:
        copy = snapshot / (str(len(files)) + '-' + path.name)
        shutil.copyfile(path, copy); path = copy
    assert prefix + target not in {x['path'] for x in files}
    files.append({'local': str(path), 'path': prefix + target, 'sha256': sha(path)})

for n, atom, stem in [(27, 'P15.2', 'P15.2-relative-zero-volume-operator'),
                      (28, 'P15.1', 'P15.1-relative-zero-volume-energy')]:
    out = r / f'deliverables/round-{n}'
    manifest = json.loads((r / f'deliverables/round-{n}-bundle-manifest.json').read_text())
    assert not manifest['full_original_atom_solved']
    for name, h in manifest['entries'].items():
        assert sha(out / name) == h; add(out / name, f'round-{n}/' + name)
    for name in (f'reviewed-papers-round-{n}.zip', f'round-{n}-bundle-manifest.json',
                 f'round-{n}-source-preparation.json', f'round-{n}-native-verification.json',
                 f'round-{n}-native-verification-v2.json', f'round-{n}-visual-check.json'):
        add(r / 'deliverables' / name, 'bundles/' + name)
    add(out / 'first-page.png', f'round-{n}/first-page.png')
    for path in sorted((out / 'export-build').glob('*')):
        if path.suffix != '.pdf': add(path, f'round-{n}/export-build/' + path.name)
    d = r / f'campaigns/round-{n}' / (stem + '-review')
    f = json.loads((d / 'freeze.json').read_text()); w = Path(f['source_workspace'])
    for name in ('freeze.json', 'source-artifact-binding.json', 'review-read-attestation.json',
                 'task.json', 'settings.json', 'publication-edits.json', 'review-result.json'):
        add(d / name, f'round-{n}/review-inputs/' + name)
    author_names = ['status.json', f'{atom}-argument.md', f'{atom}-partial.tex', 'rerun.py']
    author_names += (['prepare_evidence.py', 'author-audit.md', 'notes.json'] if n == 27 else
        ['extract_sources.py', 'author-audit.json', 'canonical-notes.json', 'checks.json', 'build-evidence.json'])
    for name in author_names: add(w / name, f'round-{n}/frozen-author/' + name)
    evidence = w / 'evidence' if n == 27 else w
    for path in sorted(evidence.glob('BEGZ-LF*.txt')):
        add(path, f'round-{n}/selected-primary/' + path.name)
    add(evidence / 'source-provenance.json', f'round-{n}/frozen-author/source-provenance.json')
    for path in sorted((r / f'root-checks/relative-zero-volume-{atom}-phase1').glob('*.txt')):
        add(path, f'round-{n}/root-reproduction/' + path.name)

for name in ('record_zero_volume_fibration_root_read.py', 'record_zero_volume_fibration_reviews.py',
             'prepare_zero_volume_fibration_papers.py', 'export_zero_volume_fibration_papers.py',
             'export_zero_volume_fibration_papers_v2.py', 'publish_zero_volume_fibration_papers.py',
             'refresh_checklist.py'):
    add(r / name, 'reproduction-scripts/' + name, mutable=name == 'refresh_checklist.py')
add(r / 'deliverables/zero-volume-fibration-export-metadata-failure.json',
    'records/zero-volume-fibration-export-metadata-failure.json')
add(cp / 'push-receipt-continuation39.json', 'records/push-receipt-continuation39.json')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(r / name, name, mutable=True)
add(Path(__file__), 'checkpoint-scripts/' + Path(__file__).name)
push = cp / 'push_checkpoint_continuation40.py'; assert not push.exists()
s = (cp / 'push_checkpoint_continuation39.py').read_text()
s = s.replace('continuation39', 'continuation40').replace(
    'Checkpoint prescribed-type source evidence and unresolved extension',
    'Publish reviewed relative zero-volume fibration operator and energy papers')
push.write_text(s); add(push, 'checkpoint-scripts/' + push.name)
note = snapshot / 'CHECKPOINT.txt'
note.write_text('Checkpoint40: separate 11-page operator and 12-page energy papers in '
    'the supplied-fibration bounded scope, both independently PASS through Xean native '
    'Codex gpt-6.1-sol xhigh. All canonical notes, full proofs and author TeX, essential '
    'primary bodies and full reviews were read and hash-bound. Fresh copied author '
    'reproduction succeeded with byte-identical TeX. Final sources compiled successfully '
    'in the native editor and two clean local PDF export passes each. First pages visually '
    'checked; remaining pages checked by compilation diagnostics. Native response-parser '
    'metadata failure and unchanged successful correction preserved. Exact scope includes '
    'critical fibres and non-descending bounded perturbations with no epsilon-relative '
    'rate; requires a supplied holomorphic fibration. No general pseudoeffective or '
    'unbounded prescribed-type theorem, minimal carrier or E1 extension claimed. '
    'No complete archival primary PDF/text or private native transcript uploaded. '
    'All 42 original problems remain open. Goal active; next batch ONLY P15.1/P15.2.\n')
add(note, 'CHECKPOINT.txt')
manifest = {'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository': 'MingchenXia/nonarchimedean-pluripotential-theory',
    'branch': 'codex/xean-research-20261003', 'expected_previous_checkpoint': parent,
    'files': files, 'scope': 'Two independently reviewed supplied-fibration bounded partial theorems; all originals open.'}
p = cp / 'upload-manifest-continuation40.json'; assert not p.exists()
p.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files)}))
