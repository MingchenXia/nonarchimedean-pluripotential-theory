"""Freeze completed partial author72 and the root-read geometric addendum."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
C = R/'campaigns/round-72/P16.1-public-source-explicit-strict-barrier-and-complete-unibranch-Runge-equation'
N = R/'root-checks/P16.1-round72-actual-result-20261005.json'
D = R/'root-checks/public-P16.1-round-72-final-reader'
S = R/'root-checks/continuation81-geometric-descent-source-reads'
P = R/'root-checks/P16.1-geometric-fiber-curve-descent-and-normalization-onto-20261005-continuation81.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
assert not D.exists() and not S.exists()
assert sha(N) == '6df27df531a2427f6121489e83f3fdda383702715584c18370a347318ec4b4b4'
actual = json.loads(N.read_text())
assert actual == json.loads((C/'run.json').read_text())['campaign']['result']
assert actual['candidate'] is False and [n['id'] for n in actual['notes']] == ['n1','n2','n3','n4']
seen = set()
for n in actual['notes']:
    assert set(n['support']) <= seen
    seen.add(n['id'])
W = Path(actual['workspace'])
assert W == C/'artifacts/codex-y4wRYE'
assert sha(W/'P16.1-argument.md') == '1ec6cc36bb3d915d0a3f2fab7f93df363b06cef737ba8931f59c4fd509c773e6'
native = json.loads((W/'input.json').read_text())
assert native == json.loads((C/'input.json').read_text())
assert (W/'input.json').read_bytes() == (W/'input-original.json').read_bytes()
assert (W/'assignment-original.txt').read_text() == native['assignment']
assert json.loads((W/'task-original.json').read_text()) == native['task']
assert sha(W/'input.json') == 'fd0c27528d9d0ea1bdb9dfab2d4b8014cfdc00efea182014986c2b6ae230eaf6'
status = json.loads((W/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'} and status['status'] == 'partial'
prov = json.loads((W/'source-extracts/source-provenance.json').read_text())
assert len(prov['sources']) == 10 and len(prov['excerpts']) == 51
primary = []; excerpts = []
for s in prov['sources']:
    assert sha(s['source']) == s['sha256'] == sha(W/s['copy'])
    for f in s['primary_files']:
        assert sha(f['source']) == f['sha256'] == sha(W/f['copy'])
        assert Path(f['source']).stat().st_size == f['bytes']
        primary.append({'source_id':s['id'],**f})
for e in prov['excerpts']:
    source = Path(e['source'])
    assert sha(source) == e['source_sha256']
    first, last = e['inclusive_one_based_LF']
    literal = '\n'.join(source.read_bytes().decode('utf-8').split('\n')[first-1:last])
    assert literal == e['literal'] == (W/e['literal_file']).read_bytes().decode('utf-8')
    assert sha(W/e['literal_file']) == e['literal_sha256']
    excerpts.append({k:e[k] for k in ['id','version','source','source_sha256','inclusive_one_based_LF','literal_file','literal_sha256','application','concrete_limits']})
assert len(primary) == 23
build = json.loads((W/'build-report.json').read_text())
assert len(build['results']) == 3 and all(b['returncode'] == 0 for b in build['results'])
for name, f in build['artifacts'].items():
    assert sha(W/name) == f['sha256'] and (W/name).stat().st_size == f['bytes']
info = subprocess.run(['pdfinfo',str(W/'P16.1-paper.pdf')], capture_output=True, text=True, check=True).stdout
assert 'Pages:           14' in info
files = [p for p in sorted(W.rglob('*')) if p.is_file()]
assert len(files) == 142
for p in files:
    assert not p.is_symlink() and not any(part in {'.git','.codex','.aws','.env','auth.json','campaign.sqlite','run.json'} for part in p.relative_to(W).parts)
    assert p.suffix not in {'.sqlite','.jsonl'}
D.mkdir(); preserved = []
for p in files:
    target = D/p.relative_to(W)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p,target)
    assert sha(p) == sha(target)
    preserved.append({'file':str(p.relative_to(W)),'bytes':p.stat().st_size,'sha256':sha(p)})
shutil.copyfile(N,D/'canonical-native-result.json')
now = datetime.now(timezone.utc).isoformat()
write(D/'root-preservation-and-read-state-continuation81.json',{
    'recorded_utc':now,'atom':'P16.1','round':72,'campaign':str(C),'native_workspace':str(W),'reader':str(D),
    'actual_result_sha256':sha(N),'candidate':False,'original_closed':False,
    'entire_actual_four_canonical_notes_root_read':True,'whole_argument_root_read':True,
    'argument_sha256':sha(D/'P16.1-argument.md'),'argument_LF_count':393,
    'argument_read_ranges':[[1,94],[95,190],[191,263],[264,334],[335,393]],'whole_tex_root_read':False,
    'all_source_application_limits_and_excerpt_index_root_read':True,
    'all_literal_excerpt_bodies_root_read':False,'whole_primary_bodies_root_read':False,
    'primary_file_bindings':primary,'literal_excerpt_bindings':excerpts,
    'native_input_semantically_equals_frozen_campaign':True,'native_input_preserved_byte_identically':True,
    'native_input_sha256':sha(D/'input.json'),'preserved_author_files':preserved,
    'author_two_pass_compilation':'SUCCESS','author_pdf_pages':14,
    'new_generated_mathematics_independently_reviewed':False,'complete_original_candidate_ready_for_review':False,
    'native_editor_source_preserved':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'limits':'Reproduced artifact and literal-source bindings; all new mathematical claims remain unreviewed. Analytic gates A-C, fiber compatibility and arbitrary-cardinality envelope/existence remain open.'})

assert sha(P) == '0c0f323068f29b778eb83ad24a0dd976eb1f2215e368bc80a01264105a85c112'
B = R/'shared-sources/P16-arxiv-1801.08229-20261004.txt'
assert sha(B) == '659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0'
S.mkdir(); units = []
for first,last,application in [
    (2550,2616,'Birational error theorem retains the ample class error. The final printed theta at LF2594 conflicts with the preceding L_m+H membership; the proposed correction is unreviewed.'),
    (2859,2881,'Onto PSH needs target-side approaching classes with EP; normalization homeomorphism alone does not establish onto membership.')]:
    q = S/f'BJ-LF{first}-{last}.txt'
    q.write_bytes('\n'.join(B.read_bytes().decode('utf-8').split('\n')[first-1:last]).encode('utf-8'))
    units.append({'source':str(B),'source_sha256':sha(B),'version':'1801.08229v4',
        'inclusive_one_based_LF':[first,last],'literal_file':str(q),'literal_sha256':sha(q),
        'whole_literal_body_root_read':True,'application_and_limit':application})
web_applications = [
    ('0GIQ','Geometrically unibranch irreducible schemes have normalization a universal homeomorphism; retain reduced integral finite-type hypotheses.'),
    ('0BQ3','Normal local domains are geometrically unibranch; used only for the normal intermediate target.'),
    ('0AY8','Projective birational resolution of an integral normal target has geometrically connected fibers. Properness, reducedness, domination and generic H0 identity are checked in the addendum.'),
    ('0FD6','Smooth Bertini on the blowup uses a globally generated very ample complete system and its immersion, with finitely many proper-intersection conditions.'),
    ('0FD9','Ample hyperplane sections of smooth projective connected schemes of dimension at least two are connected; properness and depth hypotheses are retained.'),
    ('0G4G','Combines smooth and connected hyperplane sections. The resulting curve maps algebraically to the original variety through the blowup.'),
    ('033G','Normality descends faithfully flatly for the finitely presented normalization data; finite birational normal algebra is the integral closure in the common fraction field.'),
    ('0CEX','Universal-homeomorphism property descends fpqc for the finite normalization. No analytic function descent follows from this alone.'),
    ('0BPZ','One local normalization point with purely inseparable residue extension yields geometric unibranchness of the descended scheme.')]
write(S/'source-read-record.json',{
    'recorded_utc':now,'proposal':str(P),'proposal_sha256':sha(P),'whole_saved_proposal_root_read':True,
    'units':units,'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'live_primary_web_reads':[{'stable_tag':tag,'url':'https://stacks.math.columbia.edu/tag/'+tag,
        'statement_and_pertinent_proof_body_root_read':True,'read_date_utc':'2026-10-05',
        'application_and_limit':app,'full_primary_file_snapshot_or_hash_asserted':False}
        for tag,app in web_applications],
    'whole_primary_bodies_root_read':False,'accepted_dependency':False,'original_closed':False,
    'new_mathematics_independently_reviewed':False,
    'conditional_antecedents':['F1 actual metric and algebraic-curve pullback compatibility','C1 countable singular Runge and genuine-membership reconstruction','C2 finite-data genuine nef compatibility and varying-class closure','Actual mixed operator projection and decreasing E1/MA compatibility'],
    'limits':'Stable live Stacks pages were read through the native web tool; only new paraphrased application derivations are retained. No full webpage hash or LF snapshot is asserted. Geometry and the explicit blowup do not establish the analytic gates.'})
print(json.dumps({'reader':str(D),'preserved_author_files':142,'primary_bindings':23,'literal_units':51,
    'source_read_record':str(S/'source-read-record.json'),'source_read_record_sha256':sha(S/'source-read-record.json'),
    'whole_argument_root_read':True,'candidate':False,'original_closed':False},indent=2))
