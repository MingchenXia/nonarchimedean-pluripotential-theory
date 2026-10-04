from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone

R=Path('/workspace/research'); G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
pending=G/'upload-manifest-continuation43.json'
assert sha(pending)=='2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
out=G/'local-packet-continuation49.json'; saved=G/'continuation49-local-records'
assert not out.exists() and not saved.exists()
stamp=datetime.now(timezone.utc).isoformat()
active_path=R/'active-work.json'; active=json.loads(active_path.read_text())
active['updated_utc']=stamp; active['prepared_local_followup_packet_49']=str(out)
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
check_path=R/'checklist-current.json'; check=json.loads(check_path.read_text())
assert check['fully_solved_original_atoms']==[] and len(check['targets'])==42
check['updated_utc']=stamp
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
files=[Path(__file__),R/'prepare_public_curve_draft_reviews_20261004.py',
       R/'prepare_public_regularization_batch_20261004.py',
       R/'record_public_regularization_launch_20261004.py',
       R/'public-regularization-batch-manifest-20261004.json',R/'public-regularization-batch-launch-20261004.json',
       R/'public-curves-and-CLD-batch-manifest-20261004.json',R/'public-curves-and-CLD-batch-launch-20261004.json',
       R/'P03-curve-final-source-applications-root-read-20261004.json',
       R/'P03-curve-final-source-applications-root-read-20261004.paths-addendum.json',
       R/'root-checks/snapshot_public_curves_final_20261004.py',
       R/'root-checks/reproduce_public_curves_final_20261004.py',
       R/'root-checks/record_public_curves_final_read_20261004.py',
       R/'root-checks/record_public_curve_source_paths_addendum_20261004.py']
for name in ['P03.2-local-CLD-stage-bridge-working-proof-20261004.md',
             'P03.2-local-CLD-stage-bridge-working-proof-20261004.binding.json',
             'P03.2-round39-preliminary-strict-PL-gap-20261004.md',
             'P03.2-round39-preliminary-strict-PL-gap-20261004.binding.json',
             'P03.2-round39-final-strict-PL-gap-20261004.md']:
    files.append(R/'root-checks'/name)
for name in ['P03-CLD-v2-primary-cache-and-root-read-20261004.json',
             'P03-Wanner-primary-cache-and-root-read-20261004.json',
             'P03-Thuillier-smooth-realization-root-read-20261004.json',
             'P03-general-curve-realization-and-stage-root-read-20261004.json']:
    files.append(R/'shared-sources'/name)
scopes={}
for n,atom,stem in [(39,'P03.2','P03.2-public-source-CLD-envelope-stages'),
                    (40,'P03.3','P03.3-public-source-general-curve-continuity')]:
    reader=R/'root-checks'/f'public-curves-CLD-round-{n}-final-reader'
    files.extend(p for p in reader.iterdir() if p.is_file() and p.suffix in {'.md','.tex','.json','.py','.txt','.log'})
    files.extend(p for p in (reader/'source-extracts').rglob('*') if p.is_file() and p.suffix in {'.md','.txt','.json'})
    reproduction=reader/'reproduction'; files.append(reproduction/f'{atom}-paper.pdf')
    if n==39:
        files.extend(reproduction/name for name in ['build-diagnostics.json','artifact-checks.json','build-pass1.log','build-pass2.log'])
    else:
        files.extend(p for p in (reproduction/'checks').iterdir() if p.is_file() and p.suffix in {'.json','.log','.txt','.md'})
    review=R/'campaigns'/f'round-{n}'/(stem+'-review')
    files.extend(review/name for name in ['task.json','argument.md','settings.json','freeze.json'])
    scopes[str(n)]=json.loads((reader/'status.json').read_text())
for n,stem in [(41,'P02.1-public-source-decreasing-real-PL'),(42,'P02.2-public-source-decreasing-LFS')]:
    author=R/'campaigns'/f'round-{n}'/stem
    files.extend(author/name for name in ['input.json','settings.json','input-manifest.json'])
saved.mkdir()
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    source=R/name; target=saved/name; shutil.copyfile(source,target)
    assert sha(source)==sha(target); files.append(target)
assert len(files)==len(set(files))
entries=[]
for p in files:
    assert p.is_file() and not p.is_symlink(),str(p)
    entries.append({'local':str(p),'path':'research-checkpoints/continuation49/'+str(p.relative_to(R)),
                    'sha256':sha(p),'bytes':p.stat().st_size})
packet={'prepared_utc':stamp,'state':'LOCAL ONLY; no GitHub mutation or generated-material provider submission.',
    'files':entries,'file_count':len(entries),'original_atoms':42,'fully_solved_original_atoms':[],
    'completed_draft_scope':scopes,'current_selected_atoms':['P02.1','P02.2'],
    'current_native_launch_record':str(R/'public-regularization-batch-launch-20261004.json'),
    'drafts_independently_accepted':False,
    'R39_subsidiary_TheoremC':'Unverified: strict/non-strict G-site identification is false in general; complete gap check attached. The conclusion itself is not disproved.',
    'source_read_path_correction':str(R/'P03-curve-final-source-applications-root-read-20261004.paths-addendum.json'),
    'previous_local_packet':str(G/'local-packet-continuation48.json'),
    'last_verified_remote_commit':'604fea852c6a27d4cdc83d97f17393ea67087301',
    'pending_GitHub43_manifest_sha256':sha(pending),'blocked_exports_not_resubmitted':True,
    'whole_uploaded_PDF_or_extract_included':False,'public_primary_PDF_cache_files_included':False,
    'private_transcripts_sql_auth_runtime_included':False,
    'native_editor_limitation':'Both open requests were unresponsive and terminated without output; dependent native compile calls were not reached. Editor opening/native compilation unconfirmed, sources preserved. Fresh local two-pass TeX builds succeeded.',
    'verification_limit':'All final proofs and actual canonical notes read; publication and independent acceptance remain separate. Source hashes and successful reproduction are not mathematical proof certificates.'}
out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(out),'sha256':sha(out),'files':len(entries),
                  'external_upload':False,'original_atoms_closed':0},indent=2))
