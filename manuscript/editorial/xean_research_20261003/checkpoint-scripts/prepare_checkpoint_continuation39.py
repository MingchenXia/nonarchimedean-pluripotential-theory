"""Freeze future source preparation without accepting new mathematical claims."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

root = Path('/workspace/research')
checkpoint = root / 'github-checkpoint'
parent = '9f0124525843b4c543eb7b097ee67543fabd1bd5'
active_path = root / 'active-work.json'
active = json.loads(active_path.read_text())
assert active['github_checkpoint']['commit_sha'] == parent
assert active['selected_atoms'] == ['P15.1', 'P15.2']
assert not active['full_solutions']
proposal = root / 'P15-prescribed-type-leading-products-future-proposal.json'
evidence = root / 'shared-sources/zero-volume-prescribed-type-future-source-read-20261004.json'
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
assert sha(proposal) == '67b00b3d09a52edd99fe934ebbaf170b024adfb0c6012d2a7e0c6b88451a7c2d'
assert sha(evidence) == '790e028be540b68da646d5569b2c96f8e336d9431e5f121d60099b09475d235f'
active['future_prescribed_type_leading_products'] = {
    'proposal': str(proposal),
    'proposal_sha256': sha(proposal),
    'primary_read_record': str(evidence),
    'primary_read_record_sha256': sha(evidence),
    'status': 'Unverified future mathematical proposal only. No new campaign admitted; not injected into either running fibration worker. Dimensional carrier, minimum reference data, concavity and full finite-energy extension remain unresolved. All original atoms remain open.',
}
active['updated_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')

snapshot = checkpoint / 'continuation39-uploaded-live-records'
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
    assert prefix + target not in {item['path'] for item in files}
    files.append({'local': str(path), 'path': prefix + target, 'sha256': sha(path)})

add(proposal, 'proposed-inputs/prescribed-type-leading-products/' + proposal.name)
add(evidence, 'source-authentication/prescribed-type-leading-products/' + evidence.name)
for name in ('Xia-1907.06359v1-20261004-provenance.json', 'DDNL18-2049-2087-20261004-provenance.json'):
    add(root / 'shared-sources' / name, 'source-authentication/prescribed-type-leading-products/' + name)
add(checkpoint / 'push-receipt-continuation38.json', 'records/push-receipt-continuation38.json')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(root / name, name, mutable=True)
add(Path(__file__), 'checkpoint-scripts/' + Path(__file__).name)
push = checkpoint / 'push_checkpoint_continuation39.py'
assert not push.exists()
push_source = (checkpoint / 'push_checkpoint_continuation38.py').read_text()
push_source = push_source.replace('continuation38', 'continuation39')
push_source = push_source.replace('Checkpoint two zero-volume fibration research inputs', 'Checkpoint prescribed-type source evidence and unresolved extension')
push_source = push_source.replace("ROOT/'api-requests'", "ROOT/'api-requests-continuation39'")
push.write_text(push_source)
add(push, 'checkpoint-scripts/' + push.name)
note = snapshot / 'CHECKPOINT.txt'
note.write_text(
    'Checkpoint39: active batch remains ONLY P15.1/P15.2 through Xean native Codex '
    'gpt-6.1-sol xhigh. Both research calls running; independent-review preparers '
    'waiting for committed frozen proofs. No new theorem accepted. Future-only '
    'source evidence contains exact fully read primary units from Xia integration '
    'by parts and published DDNL mixed-mass monotonicity, with literal source '
    'dates, convention differences and big/pseudoeffective scope retained. '
    'New prescribed-type leading-product proposal is unverified and was not '
    'injected into running workers. It separates actual prescribed-current mixed '
    'mass from class volume and explicitly leaves dimensional carrier, minimum '
    'reference data, concavity and full finite-energy extension unresolved. '
    'No archival complete primary PDF/text or private native transcript uploaded. '
    'Previously reviewed papers remain immutable. All42 originals open; goal active.\n'
)
add(note, 'CHECKPOINT.txt')
manifest = {
    'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository': 'MingchenXia/nonarchimedean-pluripotential-theory',
    'branch': 'codex/xean-research-20261003',
    'expected_previous_checkpoint': parent,
    'files': files,
    'scope': 'Unverified future P15 prescribed-type source evidence and mathematical proposal. Existing two native fibration campaigns continue unchanged. No new theorem acceptance.',
}
manifest_path = checkpoint / 'upload-manifest-continuation39.json'
assert not manifest_path.exists()
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'files': len(files), 'manifest': str(manifest_path), 'sha256': sha(manifest_path)}))
