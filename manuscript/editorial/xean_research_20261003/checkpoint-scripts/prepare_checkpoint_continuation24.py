"""Checkpoint completed, unaccepted proof drafts without changing frozen runs."""
from pathlib import Path
import datetime, hashlib, json, shutil

root = Path('/workspace/research')
checkpoint = root / 'github-checkpoint'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
active_path = root / 'active-work.json'
active = json.loads(active_path.read_text())
for entry in active['continuations']:
    if entry['directory'].endswith('round-19/P06.2-general-finite-galois-continuation') or entry['directory'].endswith('round-20/P05.2-fixed-real-reference-continuation'):
        directory = Path(entry['directory'])
        result = json.loads((directory / 'run.json').read_text())['campaign']['result']
        assert result['candidate'] is False
        entry['worker_workspace'] = result['workspace']
        entry['state'] = 'Research completed with unaccepted partial proof draft; independent exact-scope native review running. Original atom remains open.'
active['updated_utc'] = now
active['turn_checkpoint'] = 'New finite-Galois all-pure-dimensional and every-fixed-real-reference graph-product drafts committed by native Xean. Both independent reviews running; neither new theorem granted. Latest accepted paper remains round19. All42original open.'
active['next_work'] = 'Read the complete committed drafts and canonical notes; await independent reviews, repair substantive defects in fresh campaigns, publish only accepted exact scopes, and continue solving the 42 original problems in small batches.'
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')

source_check = root / 'shared-sources/semistable-reduction-20261004/root-source-check.json'
assert not source_check.exists()
source_check.write_text(json.dumps({
    'checked_utc': now,
    'citation': 'S. Bosch and W. Lütkebohmert, Stable Reduction and Uniformization of Abelian Varieties I, Math. Ann. 270 (1985), 349–379',
    'doi': '10.1007/BF01473432',
    'public_archive': 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0270/LOG_0034.pdf',
    'printed_article_title_authors_pages_visually_verified': True,
    'theorem_7_1_printed_page_374_visually_checked': True,
    'statement_checked': 'Every smooth geometrically connected projective curve over a complete nontrivially valued non-Archimedean field has potential stable reduction when its genus is at least two, and potential semistable reduction when its genus is at most one.',
    'proof_text_read': 'Machine OCR of printed pages 374–378; theorem statement and the displayed genus inequalities and prime-to-residue-characteristic choice independently checked on the scan.',
    'ocr_corrections': ['The genus conditions are g(C)≤1 and g(C)≥1, rather than OCR strict/reversed symbols.', 'The auxiliary integer is prime to the residue characteristic, rather than the characteristic of the valued field.'],
    'unclosed_proof_dependencies': ['Earlier semistable-model, formal-fibre and genus formulas have not all been independently reconstructed.', 'The elementary affinoid subdomains of projective-line step in the proof is omitted by the source and must be supplied when required.', 'The conversion to the exact affinoid-domain/formal-boundary realization used by the curve draft is a separate obligation.'],
    'no_theorem_grant': True,
    'no_live_input_changed': True,
    'archival_scan_and_machine_ocr_retained_locally_only': True
}, ensure_ascii=False, indent=2) + '\n')

refresh = root / 'refresh_checklist.py'
s = refresh.read_text()
old = 'fresh finite-Galois all-pure-dimensions complementary-test ascent research running.'
new = 'fresh finite-Galois all-pure-dimensions complementary-test ascent draft completed, independent review running and no new grant.'
assert old in s
s = s.replace(old, new)
old = 'fresh all-real-reference graph-product campaign running via finite rational PC cone and exact rational positive-growth convex decomposition, unreviewed.'
new = 'fresh all-real-reference graph-product draft completed via finite rational PC cone and exact rational positive-growth convex decomposition, independent review running and no new grant.'
assert old in s
s = s.replace(old, new)
refresh.write_text(s)
import subprocess
subprocess.run(['python3', str(refresh)], check=True, capture_output=True)

snapshot = checkpoint / 'continuation24-uploaded-live-records'
snapshot.mkdir(exist_ok=False)
prefix = 'manuscript/editorial/xean_research_20261003/'
files = []
def add(path, target, mutable=False):
    path = Path(path)
    assert path.is_file(), path
    if mutable:
        destination = snapshot / (str(len(files)) + '-' + path.name)
        shutil.copyfile(path, destination)
        path = destination
    files.append({'local': str(path), 'path': prefix + target,
                  'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})

for round_number, name, label, proof, audit in [
    ('19', 'P06.2-general-finite-galois', 'general-finite-galois', 'P06.2-argument.md', 'self-audit.md'),
    ('20', 'P05.2-fixed-real-reference', 'fixed-real-reference-graph-products', 'P05.2-argument.md', 'author-self-audit.md')]:
    directory = root / ('campaigns/round-' + round_number) / (name + '-continuation')
    result = json.loads((directory / 'run.json').read_text())['campaign']['result']
    workspace = Path(result['workspace'])
    add(directory / 'run.json', 'unreviewed-drafts/' + label + '/canonical-research-run.json')
    for filename in [proof, 'status.json', audit]:
        add(workspace / filename, 'unreviewed-drafts/' + label + '/' + filename)
    for filename in ['research-notes.md', 'research-evidence.md', 'artifact-checks.json', 'checks.json', 'real-sum-output.json', 'local-output.json']:
        if (workspace / filename).is_file():
            add(workspace / filename, 'unreviewed-drafts/' + label + '/' + filename)
    review = root / ('campaigns/round-' + round_number) / (name + '-review')
    for filename in ['argument.md', 'task.json', 'settings.json', 'freeze.json', 'source-artifact-binding.json']:
        add(review / filename, 'pending-reviews/' + label + '/' + filename)

for filename in ['source-provenance.json', 'root-source-check.json']:
    add(source_check.parent / filename, 'source-checks/BL1985-I/' + filename)
add(checkpoint / 'push-receipt-continuation23.json', 'records/push-receipt-continuation23.json')
for filename in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv', 'refresh_checklist.py']:
    add(root / filename, filename, mutable=True)
add(Path(__file__), 'checkpoint-scripts/' + Path(__file__).name)
summary = snapshot / 'CHECKPOINT.txt'
summary.write_text('Checkpoint24: Native Xean gpt-6.1-sol xhigh completed new P06 finite-Galois all-pure-dimensional complementary-test and P05 every-fixed-real-reference graph-product proof drafts. Both exact-scope independent reviews are running. These new claims remain unaccepted and do not close either original atom. Latest accepted paper is round19. Public-primary BL1985-I citation and visually checked theorem statement recovered; indispensable proof-chain obligations remain. Archival PDF/OCR are retained locally, not redistributed. All42original problems remain open and the goal is active.\n')
add(summary, 'CHECKPOINT.txt')
manifest = {'generated_utc': now, 'repository': 'MingchenXia/nonarchimedean-pluripotential-theory',
            'branch': 'codex/xean-research-20261003',
            'expected_previous_checkpoint': '1fb3b633b079e6e8a64c6b8d9feb6b219045ae5c',
            'files': files, 'scope': 'Unaccepted completed partial drafts, pending independent reviews and primary-source authentication; all42original open.'}
path = checkpoint / 'upload-manifest-continuation24.json'
assert not path.exists()
path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
script = (checkpoint / 'push_checkpoint_continuation23.py').read_text().replace('continuation23', 'continuation24')
script = script.replace('Checkpoint real reference cone route and curve source audit', 'Checkpoint completed partial drafts and independent review inputs')
path = checkpoint / 'push_checkpoint_continuation24.py'
assert not path.exists()
path.write_text(script)
print(json.dumps({'files': len(files), 'manifest': str(checkpoint / 'upload-manifest-continuation24.json')}))
