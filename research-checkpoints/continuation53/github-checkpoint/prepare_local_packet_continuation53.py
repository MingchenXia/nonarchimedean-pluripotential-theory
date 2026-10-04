from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous = G / 'local-packet-continuation52.json'
assert sha(previous) == '159783a27f09a2b58094cc990dd3ba45fc198c875d72712e299c9748253051b4'
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
out = G / 'local-packet-continuation53.json'
saved = G / 'continuation53-local-records'
assert not out.exists() and not saved.exists()
stamp = datetime.now(timezone.utc).isoformat()
nodal = R / 'root-checks/P16.1-nodal-obstruction-paper-20261004'
nodal_build = json.loads((nodal / 'build-result.json').read_text())
assert sha(nodal / 'local-pdf/P16.1-nodal-obstruction-paper.pdf') == '39776a133ae532a429653ea20d250f80585f4b09d5a2ae1cc7bba56afd0b6a06'
nodal_record = nodal / 'root-final-read-and-visual.json'
assert not nodal_record.exists()
nodal_record.write_text(json.dumps({
    'recorded_utc': stamp, 'entire_new_proof_markdown_root_read': True,
    'proof_markdown': str(R / 'root-checks/P16.1-nodal-normalization-obstruction-20261004.md'),
    'proof_markdown_sha256': sha(R / 'root-checks/P16.1-nodal-normalization-obstruction-20261004.md'),
    'entire_tex_root_read': True, 'tex_LF_lines': 346,
    'tex_sha256': sha(nodal / 'P16.1-nodal-obstruction-paper.tex'),
    'native_open_result': 'queued; actual UI opening not observed', 'native_compile_result': 'success',
    'actual_visual_pdf_pages': [1,4],
    'visual_result': 'First and last pages legible with no clipping; whole-PDF visual inspection is not asserted.',
    'mathematical_scope': 'Explicit nodal rational curve over C((t)), genuine degree-two continuous operator obstruction; finite-energy nonexistence is conditional on three stated singular-theory interfaces. Unibranch and higher-dimensional cases remain open.',
    'public_background_origin_and_exact_application_checks_explicit': True,
    'build_record_sha256': sha(nodal / 'build-result.json'),
    'independent_mathematical_acceptance': False, 'original_atom_closed': False,
    'provider_or_GitHub_export_attempted': False, 'hot_feedback_sent': False}, indent=2) + '\n')
saved.mkdir()
completed = []
files = [Path(__file__), R / 'prepare_public_P16_final_reviews_20261004.py',
    R / 'root-checks/snapshot_public_P16_final_20261004.py',
    R / 'root-checks/reproduce_public_P16_final_20261004.py',
    R / 'root-checks/P16.1-nodal-normalization-obstruction-20261004.md',
    R / 'root-checks/prepare_nodal_obstruction_paper_20261004.py',
    R / 'root-checks/build_nodal_obstruction_paper_20261004.py']
for number, atom, slug in [(45,'P16.1','P16.1-public-source-singular-finite-energy-equations'),
                           (46,'P16.4','P16.4-public-source-arbitrary-field-finite-energy-equations')]:
    author = R / 'campaigns' / f'round-{number}' / slug
    reader = R / 'root-checks' / f'public-P16-round-{number}-final-reader'
    reproduction = R / 'root-checks' / f'public-P16-round-{number}-root-reproduction'
    review = author.with_name(slug + '-review')
    run = json.loads((author / 'run.json').read_text())['campaign']
    assert run['status'] == 'completed' and run['error'] is None and run['result']['candidate'] is False
    read = json.loads((reader / 'complete-root-read.json').read_text())
    assert read['entire_final_argument_root_read'] and read['all_actual_canonical_notes_all_fields_and_support_root_read']
    command = ['/workspace/xean/.xean/cloud/bun/bin/bun','--no-install','--no-env-file',
        '/workspace/xean/packages/cli/src/index.ts','status',str(author/'campaign.sqlite')]
    status_run = subprocess.run(command,cwd='/workspace/xean',capture_output=True,text=True)
    assert status_run.returncode == 0, status_run.stderr
    status = json.loads(status_run.stdout)
    assert status['status'] == 'completed'
    status_path = saved / f'{atom}-native-status.json'
    status_path.write_text(json.dumps(status,indent=2) + '\n')
    completed.append({'round':number,'atom':atom,'status':'completed','candidate':False,
        'canonical_note_count':3,'final_reader':str(reader),'root_read':str(reader/'complete-root-read.json'),
        'reproduction':str(reproduction/'root-reproduction-result.json'),
        'review_directory':str(review),'review_freeze_sha256':sha(review/'freeze.json'),
        'review_state':'LOCAL PREPARED ONLY; never submitted',
        'status_file':str(status_path),'status_sha256':sha(status_path),
        'independently_accepted':False,'original_atom_closed':False})
    files.append(status_path)
    for directory in (reader,reproduction,review):
        for p in sorted(directory.rglob('*')):
            if p.is_file():
                assert not p.is_symlink()
                assert not any(w in str(p.relative_to(directory)).lower() for w in ('transcript','session','events'))
                assert p.suffix in {'.md','.tex','.pdf','.txt','.json','.py','.log','.aux','.out','.png','.sh'}
                files.append(p)
for p in sorted(nodal.rglob('*')):
    if p.is_file():
        assert p.suffix in {'.md','.tex','.pdf','.txt','.json','.log','.aux','.out','.png','.stdout','.stderr'}
        files.append(p)
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
assert active['full_solutions'] == []
active['updated_utc'] = stamp
active['prepared_local_followup_packet_53'] = str(out)
active['current_public_P16_equation_batch']['status_checkpoint'] = completed
for campaign in active['current_public_P16_equation_batch']['campaigns']:
    campaign['state'] = 'Author completed with candidate=false; entire proof and canonical chain root read, freshly reproduced; review locally prepared only.'
active['new_local_nodal_obstruction_paper'] = {'root_record':str(nodal_record),
    'paper_tex':str(nodal/'P16.1-nodal-obstruction-paper.tex'),
    'paper_pdf':str(nodal/'local-pdf/P16.1-nodal-obstruction-paper.pdf'),
    'independently_accepted':False,'original_target_closed':False}
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. R45/R46 completed partial drafts are fully root read and reproducible, with reviews prepared locally only. Local nodal obstruction paper is compiled and root read. Four earlier rejected exports remain pending specific approval; none retried.'
active['next_work'] = 'Continue a small original/public-source-only research batch; preserve frozen author outputs and local review packets. Do not retry rejected generated-material exports without their pending specific approval.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2) + '\n')
check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert len(check['targets']) == 42 and check['fully_solved_original_atoms'] == []
assert all(t['fully_solved'] is False and t['closure'] == 'open' for t in check['targets'])
check['updated_utc'] = stamp
check['active_atoms'] = []
for t in check['targets']:
    item = next((c for c in completed if c['atom'] == t['id']),None)
    if item:
        t['research_status'] = 'partial; independent review pending'
        t['current_focus'] = 'Completed narrower finite-energy curve theorem; complete root read and reproduction passed. Independent review packet locally prepared only, not submitted. Original scope remains open.'
        t.setdefault('local_unaccepted_drafts',[]).append(item)
        status = json.loads((Path(item['final_reader'])/'status.json').read_text())
        t['current_concrete_gaps'] = status['concrete_gaps']
reviewed = sum(len(t['reviewed_papers']) for t in check['targets'])
covered = sum(bool(t['reviewed_papers']) for t in check['targets'])
assert reviewed == 37 and covered == 13
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2) + '\n')
with (R/'checklist-current.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in check['targets']:
        w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    dest = saved / name
    shutil.copyfile(R/name,dest)
    assert sha(dest) == sha(R/name)
    files.append(dest)
assert len(files) == len(set(files))
entries = [{'local':str(p),'path':'research-checkpoints/continuation53/'+str(p.relative_to(R)),
            'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
packet = {'prepared_utc':stamp,'state':'LOCAL ONLY; no provider or GitHub export attempted.',
    'files':entries,'file_count':len(entries),'original_atoms':42,'fully_solved_original_atoms':[],
    'reviewed_scoped_papers':reviewed,'original_ids_with_reviewed_scoped_papers':covered,
    'completed_native_drafts':completed,'local_nodal_paper_independently_accepted':False,
    'previous_local_packet':str(previous),'previous_local_packet_sha256':sha(previous),
    'last_verified_remote_commit':'604fea852c6a27d4cdc83d97f17393ea67087301',
    'pending_GitHub43_manifest_sha256':sha(pending),'rejected_exports_not_resubmitted':True,
    'whole_uploaded_PDF_or_full_extract_included':False,'original_mathematical_family_in_inputs':True,
    'private_transcripts_sql_auth_runtime_included':False,
    'verification_limit':'Root proof reading, source application checks, clean builds and finite examples do not establish independent acceptance or full original closure.'}
out.write_text(json.dumps(packet,ensure_ascii=False,indent=2) + '\n')
print(json.dumps({'manifest':str(out),'files':len(entries),'sha256':sha(out),
    'reviewed_scoped_papers':reviewed,'original_ids_covered':covered,'uploaded':False,'original_atoms_closed':0},indent=2))
