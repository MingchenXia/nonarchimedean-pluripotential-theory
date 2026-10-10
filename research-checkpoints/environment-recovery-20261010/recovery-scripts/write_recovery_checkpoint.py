from pathlib import Path
import json, hashlib, shutil, datetime
root=Path('/workspace/research')
repo=Path('/workspace/recovered-research-repository')
pub=repo/'research-checkpoints/environment-recovery-20261010'
files=json.loads((root/'recovery-LOCALONLY/verified-file-recovery.json').read_text())
history=json.loads((root/'recovery-LOCALONLY/git-history-recovery.json').read_text())
archives=json.loads((root/'recovery-LOCALONLY/archive-recovery.json').read_text())
papers=json.loads((root/'recovery-LOCALONLY/solved-paper-inventory.json').read_text())
originals=json.loads((root/'recovered-original-problems.json').read_text())
hashes={r['sha256'] for r in files['records'] if r['status']=='byte-exact recovered'}|{r['sha256'] for r in history['matches']}
source_inventory=[]
for row in papers:
    candidates=[]
    for value in row['candidate_sources']:
        path=Path(value)
        assert path.is_file()
        candidates.append({'path':value,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'mathematical_status':'historical paper candidate; source recovery does not give new acceptance'})
    assert candidates
    source_inventory.append({'atom':row['id'],'historical_original_closed_in_checkpoint312':True,'sources':candidates})
status={
    'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'recovered_original_statement_count':len(originals['targets']),
    'recovered_original_inventory_sha256':hashlib.sha256((root/'recovered-original-problems.json').read_bytes()).hexdigest(),
    'original_statement_bodies_in_this_public_checkpoint':False,
    'original_pdf_byte_copy_recovered':history['original_pdf_recovered'],
    'verified_repository_and_history_unique_hashes':len(hashes),
    'upload_manifests_processed':files['manifests'],
    'earlier_snapshot_mismatches_recovered_from_history_unique_hashes':history['recovered_unique_hashes'],
    'historical_git_objects_scanned':history['objects_scanned'],
    'restored_archive_members':len(archives['records']),
    'existing_archive_PDFs_retained':sum(r['member'].endswith('.pdf') for r in archives['records']),
    'historically_solved_atoms_with_recovered_paper_sources':len(source_inventory),
    'historical_latest_conversation_counts':{'solved':17,'open':25,'accepted_scoped_papers':108},
    'history_counts_are_not_new_mathematical_acceptance':True,
    'P14_1_round328_source_and_post_checkpoint312_artifacts':'still being recovered; not present in committed Git history',
    'native344345_original_SQLite_databases':'not recovered; no duplicate launches',
    'xean_runtime_setup':'restored checksum-pinned runtime; version3.0.0',
    'native_Codex_local_login_diagnostic':'Logged in using ChatGPT; remote model authorization not reverified by a completed new turn',
    'literal_primary_bodies_and_chat_recovery_bodies':'LOCALONLY, excluded from public checkpoint',
    'protected_P16_4_source_sha256':hashlib.sha256((root/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex').read_bytes()).hexdigest(),
    'new_original_closures_this_recovery':0,
    'new_mathematical_acceptances_this_recovery':0
}
assert status['protected_P16_4_source_sha256']=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
pub.mkdir(parents=True,exist_ok=True)
(pub/'recovered-materials-status.json').write_text(json.dumps(status,indent=2)+'\n')
(pub/'recovered-solved-paper-source-index.json').write_text(json.dumps(source_inventory,indent=2)+'\n')
(root/'recovery-status.json').write_text(json.dumps(status,indent=2)+'\n')
scripts=['recovery_inventory.py','restore_verified_repository_files.py','recover_git_history_payloads.py','recover_archived_papers.py','recover_original_inventory_and_proof_index.py','recovery_solved_paper_inventory.py','write_recovery_checkpoint.py']
for name in scripts:
    dest=pub/'recovery-scripts'/name
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(root/name,dest)
print(json.dumps(status))
