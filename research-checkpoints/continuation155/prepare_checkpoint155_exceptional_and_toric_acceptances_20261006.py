from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
previous = G / 'push-receipt-continuation154.json'
receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == '1ac80d9f543434cdddd34b857637344cfd831f0e'
assert receipt['manifest_sha256'] == sha(G / 'upload-manifest-continuation154.json')
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
papers = []
for folder, count, pages in [('deliverables/scoped-P16.5-exceptional-big-family',54,9),
                             ('deliverables/scoped-P19.2-closed-toric-profile',55,6),
                             ('root-checks/public-P19.2-continuation190-finite-entropy-endpoint-reader',None,4)]:
    d = R / folder
    b = json.loads((d / 'publication-binding.json').read_text())
    assert b['pages'] == pages and b['actual_visual_pages']
    assert b['overfull'] == b['warnings'] == b['undefined'] == 0
    assert sha(b['tex']) == b['tex_sha256'] and sha(b['pdf']) == b['pdf_sha256']
    if count:
        assert b['accepted_paper_count'] == count and b['review_verdict'] == 'PASS'
    else:
        assert not b['independent_review'] and not b['full_P19_2_nonexistence_claim']
    assert not b['original_closed']
    papers.append((d,b))
reader140 = K / 'public-P19.2-round140-partial-endpoint-reader'
b140 = json.loads((reader140 / 'publication-binding.json').read_text())
assert b140['pages'] == 15 and b140['actual_visual_pages'] == [1,8,15]
assert b140['whole_953_line_standalone_argument_root_read'] and b140['whole_source_application_ledger_root_read']
assert not b140['candidate'] and not b140['independent_review']
for b in b140['file_bindings']:
    assert sha(reader140 / b['name']) == b['sha256']
accept143 = K / 'P16.5-round143-exceptional-acceptance-and-original-scope-record-20261006.json'
accept146 = K / 'P19.2-round146-toric-acceptance-and-original-scope-record-20261006.json'
assert json.loads(accept143.read_text())['accepted_papers_after'] == 54
assert json.loads(accept146.read_text())['accepted_papers_after'] == 55
S = K / 'current-small-batch145147-20261006-continuation155'
S.mkdir(exist_ok=False)
items = []
for n in [145,147]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    launch = json.loads((C / 'launch-record.json').read_text())
    for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256'),
                      ('input.json','input_sha256') if n == 145 else ('argument.md','argument_sha256')]:
        assert sha(C / name) == f[key]
    status = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C / 'work.sqlite')],
        cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    ps = subprocess.run(['ps','-o','stat=,comm=','-p',str(launch['pid'])], capture_output=True, text=True).stdout.strip()
    alive = bool(ps) and not ps.startswith('Z')
    assert status['status'] in ['running','completed']
    if status['status'] == 'running':
        assert alive and status['calls']['admitted'] == 1
    p = S / f'round{n}-public-native-status.json'
    save(p,status)
    lp = C / 'launch-public-native-status.json'
    if not lp.exists():
        save(lp,status)
    items.append({'round':n,'atom':'P16.5' if n == 145 else 'P19.2','directory':str(C),'database':'work.sqlite',
        'observed_status':status['status'],'observed_utc':status['observedAt'],
        'native_controller_process_observed_alive':alive,'process_state':ps,
        'public_status':str(p),'public_status_sha256':sha(p),'launch_record':launch,'frozen_metadata':f,
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
        'author_research_only':n == 145,'scoped_review_only':n == 147,'original_closed':False,
        'private_active_output_read':False,'hot_feedback_sent':False})
for n in [143,146]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    status = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C / 'work.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert status['status'] == 'completed'
    save(S / f'round{n}-completed-public-native-status.json',status)
batch = {'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
    'maximum_concurrent_campaigns':2,
    'focus':'Entire original arbitrary-big-class equation author145 and independent finite-initial-entropy zero-endpoint diagnostic review147.'}
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    assert j['historical_reviewed_scoped_papers'] == 55
    j.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation155 frozen',
        'P16_5_accepted_exceptional_final_paper143':papers[0][1],
        'P19_2_accepted_closed_toric_final_paper146':papers[1][1],
        'P19_2_finite_initial_entropy_endpoint_candidate190':papers[2][1],
        'completed_approximation_research140_full_reader':b140,
        'original_full_big_equation_research145':items[0],
        'current_finite_entropy_endpoint_review147':items[1],
        'next_native_launch_order':['Independently review entire original145 proof if candidate=true; otherwise repair its precise completed mathematical gaps.',
            'Read completed147 canonical evidence before accepting or repairing the finite-initial-entropy endpoint diagnostic.'],
        'next_work':'Continue full original P16.5 and unchanged residual P19.2, preserving accepted exact-scope papers and frozen active inputs.',
        'goal_state':'8/42 originals solved;34 open;55 independently accepted papers. Continue small batches.'})
    for key,n,ap in [('current_exceptional_equation_review143',143,accept143),('current_toric_profile_review146',146,accept146)]:
        old = j.get(key,{})
        old.update({'round':n,'observed_status':'completed','review_verdict':'PASS','acceptance_record':str(ap),'original_closed':False})
        j[key] = old
    if 'original_full_big_equation_research144' in j:
        j['original_full_big_equation_research144'].update({'observed_status':'blocked','native_controller_process_observed_alive':False,
            'provider_calls_admitted':0,'error':'Codex worker is not configured','corrected_fresh_retry_round':145})
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
tsv = R / 'checklist-current.tsv'
out = []
for line in tsv.read_text().splitlines():
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'Whole all-big SURFACE equation PASS142 and entire exceptional nonnef-big family PASS143. Original arbitrary-big research145 '+items[0]['observed_status']+'.'
    if row[0] == 'P19.2':
        row[2] = 'Entire closed one-branch finite-height toric P profile including zero-mass endpoint PASS146, final6-page paper. Finite-initial-H zero-endpoint diagnostic190 review147 '+items[1]['observed_status']+'. Original full residual open.'
    out.append('\t'.join(row))
tsv.write_text('\n'.join(out)+'\n')
D = G / 'continuation155-publication-records'
D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    shutil.copyfile(R / name,D / name)
save(D / 'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':55,
    'new_original_closure':None,'new_accepted_supporting_papers':[str(accept143),str(accept146)],
    'completed_partial140':'Complete953-line argument and entire source ledger root-read; unchanged preserved native PDF has15 pages, contrary to its14-page narrative.',
    'new_unreviewed190':'Explicit P^n, every n>=2, isolated finite-H full-mass E1 start erasing an absolute zero-mass endpoint;4-page paper. No full residual nonexistence claim.',
    'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files = []
pdfparents = {d for d,b in papers} | {reader140}
def add(p,remote=None):
    p = Path(p)
    assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix == '.pdf':
        assert p.parent in pdfparents
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation155/'+str(p.relative_to(R)),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S]:
    for p in sorted(directory.iterdir()):
        add(p)
for d,b in papers:
    for p in [Path(b['tex']),Path(b['pdf']),d / 'publication-binding.json']:
        add(p)
for n in ['P19.2-argument.md','P19.2-paper.tex','P19.2-paper.pdf','source-application-ledger.json','publication-binding.json']:
    add(reader140 / n)
for p in [accept143,accept146,K / 'P16.5-round143-actual-scoped-independent-review-20261006.json',
          K / 'P19.2-round146-actual-scoped-independent-review-20261006.json',previous,
          R / 'record_verified154_20261006.py',R / 'accept_and_publish_exceptional143_20261006.py',
          R / 'accept_and_publish_toric146_20261006.py',R / 'publish_completed_partial140_reader_20261006.py',
          R / 'prepare_toric_closed_profile_independent_review146_20261006.py',R / 'launch_frozen_toric_closed_profile_review146_20261006.py',
          R / 'prepare_finite_entropy_endpoint_review147_20261006.py',R / 'launch_frozen_finite_entropy_endpoint_review147_20261006.py',
          R / 'build_finite_entropy_endpoint_candidate190_20261006.py',Path(__file__)]:
    add(p)
for n in [146,147]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json','task.json','argument.md','settings.json']:
        if name == 'launch-public-native-status.json' and not (C / name).exists():
            continue
        add(C / name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D / name,'manuscript/editorial/xean_research_20261003/'+name)
M = G / 'upload-manifest-continuation155.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'],
    'remaining_open_atoms':34,'historical_reviewed_scoped_papers':55,
    'commit_message':'Publish independently accepted exceptional-big equation and closed toric-profile approximation',
    'scope':'Whole exceptional-big-family equation PASS143,9-page final; whole finite-height one-branch toric profile including zero-mass terminal PASS146,6-page final. Accepted supporting papers53 to55,originals8/42 unchanged. New4-page finite-initial-entropy absolute endpoint diagnostic190 in independent147; unchanged original arbitrary-big author145 continues. Completed partial140 full953-line proof and source ledger root-read,15-page preserved paper. No active private outputs, hot feedback, or runtime/account changes.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),
    'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc']} for x in items]},indent=2))
