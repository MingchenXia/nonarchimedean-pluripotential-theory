from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, obj):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
now = datetime.now(timezone.utc).isoformat()
previous = G / 'push-receipt-continuation155.json'
receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == 'd48fe25583fe15dd80b2fb673211a54752fec541'
assert receipt['manifest_sha256'] == sha(G / 'upload-manifest-continuation155.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
paper147 = R / 'deliverables/scoped-P19.2-finite-entropy-zero-endpoint'
reader145 = K / 'public-P16.5-round145-partial-equation-reader'
reader192 = K / 'public-P16.5-continuation192-relative-generation-reader'
b147 = json.loads((paper147 / 'publication-binding.json').read_text())
b145 = json.loads((reader145 / 'publication-binding.json').read_text())
b192 = json.loads((reader192 / 'publication-binding.json').read_text())
assert b147['pages'] == 4 and b147['accepted_paper_count'] == 56 and b147['actual_visual_pages'] == [1,2,4]
assert b147['review_verdict'] == 'PASS' and not b147['original_closed']
assert b145['pages'] == 16 and b145['actual_visual_pages'] == [1,8,16]
assert b145['whole_452_line_standalone_argument_root_read'] and b145['whole_58_line_source_application_ledger_root_read']
assert not b145['candidate'] and not b145['independent_review']
assert b192['pages'] == 4 and b192['actual_visual_pages'] == [1,2,4]
assert b192['whole_proof_units_root_read'] and not b192['independent_acceptance']
for b in [b147,b192]:
    assert sha(b['tex']) == b['tex_sha256'] and sha(b['pdf']) == b['pdf_sha256']
for e in b145['file_bindings']:
    assert sha(reader145 / e['name']) == e['sha256']
for b in [b147,b145,b192]:
    assert b['overfull'] == b['warnings'] == b['undefined'] == 0
    assert b['native_compile_success_observed'] is False
accept147 = K / 'P19.2-round147-endpoint-acceptance-and-original-scope-record-20261006.json'
assert json.loads(accept147.read_text())['accepted_papers_after'] == 56
ledger = K / 'P16.5-continuation192-root-source-application-and-read-scope-20261006.json'
save(ledger, {'recorded_utc':now,'classification':'Source application record for an unreviewed algebraic foundation, not acceptance.',
    'candidate_tex_sha256':b192['tex_sha256'],'whole_final_tex_separately_root_read':False,
    'all_proof_units_root_read':True,'no_primary_quotations_republished':True,
    'applications':[
        {'url':'https://arxiv.org/html/math/0002035v2','unit':'Definition1.7, Theorem1.8(i),(iii) with complete proof; Variant2.4 with complete proof.',
         'root_observed_literal_html_lines':[[189,226],[353,365]],
         'complete_stated_units_root_read':True,'whole_source_root_read':False,
         'domain':'Absolute smooth complex projective variety and actual big bundle; no relative arbitrary-field domain assumed.',
         'new_application':'One fixed time twist gives exact relative base ideals in every degree; finite-field and multiplier-ideal descent then prove the relative conclusion. This application is unreviewed.'},
        {'url':'https://stacks.math.columbia.edu/tag/02KH','unit':'Lemma30.5.2, whole statement and proof.',
         'root_observed_literal_html_lines':[[23,54]],'complete_stated_unit_root_read':True,
         'whole_stacks_project_root_read':False,
         'application':'Proper structure and resolution morphisms are quasicompact/quasiseparated, coherent sheaves are quasicoherent, field extensions are flat; transports global sections and finite log-resolution pushforwards.'},
        {'url':'https://arxiv.org/pdf/2206.07183v2','unit':'Complete previously supplied and root-read Lemmas1.5-1.7 model/section/base-ideal proofs.',
         'local_exact_read_units':[str(K / 'public-P16.5-round-102-final-reader/primary-units/BJ-addendum-base-ideals.txt')],
         'whole_source_root_read':False,'general_nonample_closure_imported':False,
         'application':'Q_B(f) from complete section lattices, with real weights approximated below by rational weights; not full P_B(f) equality.'}],
    'ordinary_background_still_to_be_checked_independently':['Characteristic-zero finite log resolutions with geometric normal crossings; equivariant resolution and linearized ample models.','Finite presentation descent, proper birational normality and generation after an ample globally generated tensor twist.'],
    'native_independent_review_round':148,'active_private_outputs_read':False,'original_closed':False})
S = K / 'current-small-batch148149-20261006-continuation156'
S.mkdir(exist_ok=False)
items = []
for n in [148,149]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    launch = json.loads((C / 'launch-record.json').read_text())
    for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256'),
                     ('argument.md','argument_sha256') if n==148 else ('input.json','input_sha256')]:
        assert sha(C / name) == f[key]
    status = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C / 'work.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    ps = subprocess.run(['ps','-o','stat=,comm=','-p',str(launch['pid'])],capture_output=True,text=True).stdout.strip()
    alive = bool(ps) and not ps.startswith('Z')
    assert status['status'] in ['running','completed']
    if status['status'] == 'running':
        assert alive and status['calls']['admitted'] == 1 and status['calls']['unsettled'] == 1
    p = S / f'round{n}-public-native-status.json'
    save(p,status)
    if not (C / 'launch-public-native-status.json').exists():
        save(C / 'launch-public-native-status.json',status)
    items.append({'round':n,'atom':'P16.5' if n==148 else 'P19.2','directory':str(C),'database':'work.sqlite',
        'observed_status':status['status'],'observed_utc':status['observedAt'],
        'native_controller_process_observed_alive':alive,'process_state':ps,
        'public_status':str(p),'public_status_sha256':sha(p),'launch_record':launch,'frozen_metadata':f,
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
        'scoped_review_only':n==148,'author_research_only':n==149,'original_closed':False,
        'private_active_output_read':False,'hot_feedback_sent':False})
batch = {'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
    'maximum_concurrent_campaigns':2,
    'focus':'Independent actual arbitrary-field relative multiplier-generation review148 and unchanged original singular-start-relative-data approximation author149.'}
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    o = json.loads(p.read_text())
    assert len(o['fully_solved_original_atoms']) == 8 and o['remaining_open_original_atoms'] == 34 and o['historical_reviewed_scoped_papers'] == 56
    o.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation156 frozen',
        'P19_2_accepted_finite_entropy_endpoint_paper147':b147,'completed_original_big_research145_full_reader':b145,
        'P16_5_relative_generation_candidate192':b192,'current_relative_generation_review148':items[0],
        'original_approximation_research149':items[1],
        'next_native_launch_order':['Read completed148 whole canonical review; if its exact foundation is accepted, rebuild the entire unchanged original P16.5 including all remaining weighted/attainment/comparison bridges. Otherwise repair its exact gap.',
            'Read completed149 whole canonical original research result before full-scope review or precise further repair.'],
        'next_work':'Continue original P16.5 and P19.2 in batches of at most two; supporting-scope acceptance never closes the originals.',
        'goal_state':'8/42 originals solved;34 open;56 independently accepted papers. Continue small batches.'})
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
tsv = R / 'checklist-current.tsv'
out = []
for line in tsv.read_text().splitlines():
    z = line.split('\t')
    if z[0] == 'P16.5':
        z[2] = 'All-big-surface equation PASS142 and exceptional-big equation PASS143. Original145 completed PARTIAL with16-page whole reader; relative arbitrary-field generation replacement192 independent review148 '+items[0]['observed_status']+'. Full original open.'
    if z[0] == 'P19.2':
        z[2] = 'Entire closed toric profile PASS146 and finite-initial-entropy absolute zero-endpoint counterexample PASS147. Unchanged original singular-start-relative-data model approximation author149 '+items[1]['observed_status']+'. Full residual original open.'
    out.append('\t'.join(z))
tsv.write_text('\n'.join(out)+'\n')
D = G / 'continuation156-publication-records'
D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    shutil.copyfile(R / name,D / name)
save(D / 'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':56,
    'new_original_closure':None,'new_accepted_supporting_paper':str(accept147),
    'accepted147':'Whole exact CPn n>=2 finite-initial-H absolute zero-endpoint counterexample independently PASS; four-page final. Canonical defective task-metadata passage retained and excluded from external evidence; nine genuine primary passages cover all five external premises.',
    'completed_partial145':'All five canonical notes, complete452-line manuscript and58-line source ledger root-read; unchanged sixteen-page compiled paper. Relative generation and later whole equation bridges remain explicitly conditional.',
    'new_unreviewed192':'Four-page algebraic relative-generation replacement via exact uniform compactification and finite-field descent; independent review148. No general closure or equation theorem is granted.',
    'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files = []
pdfparents = {paper147,reader145,reader192}
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix == '.pdf':
        assert p.parent in pdfparents
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation156/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S]:
    for p in sorted(directory.iterdir()):
        add(p)
for folder,names in [(paper147,['P19.2-paper.tex','P19.2-paper.pdf','publication-binding.json']),
                     (reader145,['P16.5-paper.md','P16.5-paper.tex','P16.5-paper.pdf','source-ledger.md','publication-binding.json'])]:
    for name in names:
        add(folder / name)
for p in [Path(b192['tex']),Path(b192['pdf']),reader192 / 'publication-binding.json',ledger,accept147,
    K / 'P19.2-round147-actual-scoped-independent-review-20261006.json',
    K / 'P16.5-round145-completed-author-result-PUBLIC-20261006.json',
    K / 'P16.5-round145-completed-partial-and-original-scope-record-20261006.json',
    previous,R / 'record_verified155_20261006.py',R / 'accept_and_publish_endpoint147_20261006.py',
    R / 'publish_completed_partial145_reader_20261006.py',
    R / 'prepare_generation_review148_and_original_approximation149_20261006.py',
    R / 'launch_frozen_generation148_and_original_approximation149_20261006.py',Path(__file__)]:
    add(p)
for n in [148,149]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json','task.json','settings.json',
                 'argument.md' if n==148 else 'input.json']:
        add(C / name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D / name,'manuscript/editorial/xean_research_20261003/'+name)
M = G / 'upload-manifest-continuation156.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'],
    'remaining_open_atoms':34,'historical_reviewed_scoped_papers':56,
    'commit_message':'Publish finite-entropy endpoint counterexample and actual relative-generation repair',
    'scope':'Independent scoped PASS147 with4-page final, accepted papers55 to56, originals8/42 unchanged. Completed original145 partial: allfive canonical notes, entire452-line paper/source ledger root-read and16-page compiled reader. New4-page actual arbitrary-field relative-generation candidate192 in independent148; unchanged original singular-start-relative-data approximation author149. No active private outputs, hot feedback, editor or runtime/account changes.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),
    'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc']} for x in items]},indent=2))
