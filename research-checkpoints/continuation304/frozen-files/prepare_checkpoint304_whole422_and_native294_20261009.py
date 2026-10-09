from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation304-publication-records'
M = G / 'upload-manifest-continuation304.json'
D = K / 'public-P12.3-continuation422-cross-component-obstructions-and-exact-surface-gluing-unreviewed'
C = R / 'campaigns/round-294/P12.3-whole422-irreducible-conductor-centres-and-normal-residual'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation303.json')
assert prior['commit_sha'] == '5e1f5b0c4df72d9f4f4cd045cb8bf913859f8908' and prior['tree_sha'] == '143f3d8aeaa6df62eca8e223e7f0a64c681dc0de' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 422 and not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [R / n for n in ['audit_and_stage_native292_whole_paper422_ROOT_20261009.py', 'read_terminal_native292_whole_actual_notes_20261009.py', 'capture_terminal_native292_actual_FINAL_20261009.py', 'prepare_native294_whole422_irreducible_conductor_centres_20261009.py', 'launch_frozen_native294_checked_20261009.py', 'record_verified_checkpoint303_20261009.py']]
paths += [C / n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation303.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 303 and y['current_active_batch'] == [293,294]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
F.mkdir()
for p in paths:
    rel = p.relative_to(R)
    assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q = F / 'frozen-files' / rel
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p,q)
    assert sha(q) == sha(p)
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=304,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE304 whole UNREVIEWED422 and frozen294 metadata including only unproved marked-centre/irreducible proposals. Active293294 math excluded. Continue original residual, compiler unverified, counts/editor unchanged.')
    write(p,y)
write(F / 'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[293,294],new_papers=[422],all_actual_five_fields_distinct_expanded_proofs_and_unique_scopes_ROOT_physically_read=True,actual_FINAL_distinct_from_native_assembled_notes_preserved=True,whole_source_and_companion_ROOT_literal_reconstruction=True,prior14_complete_immediate_surface_SH_BFJ_units_and2formula_pixels_qualifications_retained=True,current_fresh_primary_credit=0,ENTIRE_G331_prior420_read_and_new_normal_bound_density_zero_dichotomy_applications_rejudged=True,full_recursive_deeper_source_audit_NOT_complete=True,compilation_UNVERIFIED=True,frozen294_marked_centre_and_irreducible_routes_UNPROVED_proposals_only=True,active293294_mathematics_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json',dict(recorded_utc=now,paper415='first connection closed, second pending',paper416='first pending',paper417='pending prior revision, current unverified',paper418='first pending',paper419='first pending',paper420='first correct-current-source request pending',paper421='first pending',paper422='first actual request pending',compiler_verified=False,no_success_observed=True,source_errors_NOT_reported=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint304: cross-component conductor obstructions and exact surface gluing\n\nWHOLE UNREVIEWED ROOT422 retains the actual settled native292 FINAL, all five actual notes and all five distinct expanded proofs, entire579668-byte standalone and5357181-byte ROOT companion. Actual final summary/detailedSummary/text fields DIFFER from native assembled fields; both complete sets are preserved distinctly, never substituted or falsely identified. ROOT physically read all actual/formal current proof bodies, entire unique preamble/abstract/ledger/verdict/unchanged residual and three native programs only as inert DATA, then independently literally reconstructed the whole source/native companion. Fourteen prior complete immediate surface/SH/BFJ units and two formula pixels retain exact reading/source qualifications, current ROOT fresh-primary-creditZERO. ENTIRE qualified93375-byte G331 was freshly ROOT read420; its normal-order-bound and all-support divisorial-density/zero-dichotomy applications were freshly reread/rejudged422. No complete deeper recursive book/source audit claimed.\n\nA signed primary-model obstacle on the excellent normal-crossing surface has no greatest geometric C/D minorant, exact canonical error1/2 in EVERY degree and an open neighbourhood of failures. Every positive approximant is an ACTUAL negative effective relatively ample primary-model divisor, positive on EVERY contracted integral curve before limit identification. Any normalization fibre connecting DIFFERENT MINIMAL COMPONENTS gives a signed model obstruction, hence positive-dimensional intersections of distinct irreducible components obstruct universal CE in every dimension/characteristic/residue field. The proof uses actual conductor idempotent separators, normal-centre divisorial coercivity and all-support density with NETS, without source CE or higher-dimensional resolution.\n\nFor precisely qualified regular normal surface branches glued along the same marked DVR with principal kernels and finite normalization, the raw target envelope equals each source envelope off the conductor and the minimum conductor value at the identified point. Greatest C/D minorants exist exactly when ALL source conductor values agree. Actual primary truncation proves geometric positive gluing. Mixed-characteristic crossings and every-dimensional field crossings fail. Excellent reduced local dimension<=TWO with NORMAL component rings has universal CE iff every pairwise component intersection is zero-dimensional. General normal dimension>=3, higher-dimensional positive/mixed source CE, irreducible nonnormal same-centre fibres and unrestricted gluing remain OPEN; no normal CE counterexample or full original P12.3 closure is claimed.\n\nNative294 frozen metadata contains ONLY UNPROVED ROOT proposals: replace component idempotents by semilocal CRT and conductor powers to obstruct fibres connecting DIFFERENT MARKED NORMALIZATION CENTRES, including irreducible self-crossing R=k[u,v,z]/(v²-u²(1+u)) in char!=2; separately examine same-centre pinch-threefold conductor fibres. The worker must independently prove/refute every all-support/geometric bridge. Native293 independently pursues actual Radon existence/attainment. Both use authorized Xean signed-in official Codex gpt-6.1-sol xhigh, maximumTWO. No active293294 mathematics or hot feedback published. Desktop requests remain pending/unverified; no success claimed. Literal primary bodies/pixels/books LOCALONLY, protected P16.4 editor OPEN UNCHANGED, counts16/42originals solved,26OPEN,97accepted scoped papers. NONFORCE verification binds every actual file path/blob/native Git root/parent/tree/final ref.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation304/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint cross-component conductor obstructions and exact surface gluing', scope='Whole UNREVIEWED422 and frozen294 unproved marked-centre/irreducible proposals; active293294 math excluded, compilation unverified, original OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation304.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation304.index')
subprocess.run(git + ['read-tree', prior['tree_sha']], env=env, capture_output=True, check=True)
entries = []
groups = {}
for e in items:
    data = Path(e['local']).read_bytes()
    data.decode('utf-8')
    assert hashlib.sha256(data).hexdigest() == e['sha256']
    h = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert subprocess.run(git + ['hash-object', '-w', e['local']], capture_output=True, text=True, check=True).stdout.strip() == h
    entries.append(dict(path=e['path'], mode='100644', type='blob', sha=h))
    groups.setdefault(h, e)
    subprocess.run(git + ['update-index', '--add', '--cacheinfo', '100644', h, e['path']], env=env, capture_output=True, check=True)
expected = subprocess.run(git + ['write-tree'], env=env, capture_output=True, text=True, check=True).stdout.strip()
API = G / 'api-recovery-continuation304'
API.mkdir()
chunks = []
chunk = []
size = 0
for h, e in groups.items():
    item = dict(path=h, mode='100644', type='blob', content=Path(e['local']).read_text())
    n = len(json.dumps(item, ensure_ascii=True).encode())
    if chunk and size + n > 250000:
        chunks.append(chunk)
        chunk = []
        size = 0
    chunk.append(item)
    size += n
if chunk:
    chunks.append(chunk)
sizes = []
for i, ch in enumerate(chunks):
    p = API / f'content-chunk-{i}.json'
    p.write_text(json.dumps(dict(tree=ch), ensure_ascii=True, indent=2) + '\n')
    sizes.append(p.stat().st_size)
write(API / 'connector-plan.json', dict(repository=prior['repository'], branch=prior['branch'], parent=prior['commit_sha'], base_tree=prior['tree_sha'], expected_tree=expected, manifest_sha256=sha(M), entries=entries, content_chunks=len(chunks), content_chunk_bytes=sizes, commit_message=load(M)['commit_message'], force=False))
print(json.dumps(dict(manifest=str(M), manifest_sha256=sha(M), listed_files=len(files), actual_files=len(items), content_chunks=len(chunks), content_chunk_bytes=sizes, expected_tree=expected, primary_bodies_published=False), indent=2))
