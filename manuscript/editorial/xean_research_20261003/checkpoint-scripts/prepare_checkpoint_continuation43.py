"""Freeze completed prescribed-type drafts and full independent review inputs."""
from pathlib import Path
import datetime, hashlib, json, shutil
r = Path('/workspace/research'); cp = r / 'github-checkpoint'
parent = '604fea852c6a27d4cdc83d97f17393ea67087301'
active = json.loads((r / 'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha'] == parent
assert active['selected_atoms'] == ['P15.1', 'P15.2'] and not active['full_solutions']
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
snapshot = cp / 'continuation43-uploaded-live-records'; snapshot.mkdir(exist_ok=False)
prefix = 'manuscript/editorial/xean_research_20261003/'; files = []
def add(p, target, mutable=False):
    p = Path(p); assert p.is_file(), p
    if mutable:
        dest = snapshot / (str(len(files)) + '-' + p.name); shutil.copyfile(p, dest); p = dest
    assert prefix + target not in {x['path'] for x in files}
    files.append({'local': str(p), 'path': prefix + target, 'sha256': sha(p)})
for c in active['continuations'][-2:]:
    camp = Path(c['directory']); review = Path(c['queued_review_directory'])
    x = json.loads((camp / 'run.json').read_text())['campaign']['result']
    assert x['candidate'] is False
    w = Path(x['workspace']); atom = c['atom']; rnd = camp.parent.name
    freeze = json.loads((review / 'freeze.json').read_text())
    assert sha(w / (atom + '-argument.md')) == freeze['main_argument_sha256']
    assert sha(w / (atom + '-partial.tex')) == freeze['source_tex_sha256']
    for f in sorted(w.iterdir()):
        if f.is_file() and f.suffix in {'.md', '.tex', '.py', '.json'} and f.name not in {'input.json', 'input-original.json', 'task-original.json'}:
            add(f, 'campaigns/' + rnd + '/' + camp.name + '/artifacts/' + w.name + '/' + f.name)
    for f in sorted(w.glob('*initial*failed*')):
        if f.is_file(): add(f, 'campaigns/' + rnd + '/' + camp.name + '/artifacts/' + w.name + '/' + f.name)
    for name in ('argument.md', 'freeze.json', 'source-artifact-binding.json', 'task.json', 'settings.json'):
        add(review / name, 'campaigns/' + rnd + '/' + review.name + '/' + name)
    check = Path(c['root_phase1'])
    for f in sorted(check.iterdir()):
        if f.is_file(): add(f, 'root-checks/' + check.name + '/' + f.name)
add(r / 'record_prescribed_type_zero_volume_root_read.py', 'checkpoint-scripts/record_prescribed_type_zero_volume_root_read.py')
add(cp / 'push-receipt-continuation42.json', 'records/push-receipt-continuation42.json')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv', 'refresh_checklist.py'):
    add(r / name, name, mutable=True)
add(Path(__file__), 'checkpoint-scripts/' + Path(__file__).name)
push = cp / 'push_checkpoint_continuation43.py'; assert not push.exists()
s = (cp / 'push_checkpoint_continuation42.py').read_text().replace('continuation42', 'continuation43').replace(
    'Checkpoint relative-energy source reads and future reference compression',
    'Checkpoint completed prescribed-type drafts and frozen independent reviews')
push.write_text(s); add(push, 'checkpoint-scripts/' + push.name)
note = snapshot / 'CHECKPOINT.txt'
note.write_text('Checkpoint43: ONLY P15.1/P15.2. Both prescribed-type general pseudoeffective zero-volume research campaigns completed, candidate=false. Full new mathematical cores, actual canonical notes, author TeX and audits/scripts directly root read; every selected source appendix body is bound to a complete direct primary read or explicit exact unchanged prior complete read. Fresh copied builds reproduce byte-identical mathematical proofs and TeX. P15.1 claims joint finite-energy extension/decreasing continuity/cocycles and an analytic fixed-class representative concentration counterexample; P15.2 claims bounded-type operator and more-singular relative-full-mass decreasing continuity. Both independent native Xean gpt-6.1-sol xhigh reviews RUNNING; NO NEW THEOREM ACCEPTED. Operator author TeX has a cosmetic Condition (*) emphasis conversion defect noted for later publication repair. Initial energy delimiter failure preserved. No private native transcripts, SQL databases, whole primary PDFs or whole archival texts uploaded. Earlier accepted papers immutable. All42originalsopen; goalACTIVE.\n')
add(note, 'CHECKPOINT.txt')
manifest = {'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'repository': 'MingchenXia/nonarchimedean-pluripotential-theory',
            'branch': 'codex/xean-research-20261003', 'expected_previous_checkpoint': parent,
            'files': files, 'scope': 'Completed unreviewed drafts, full frozen independent review evidence and root reproduction; no new theorem acceptance.'}
p = cp / 'upload-manifest-continuation43.json'; assert not p.exists()
p.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'files': len(files), 'manifest': str(p), 'sha256': sha(p)}))
