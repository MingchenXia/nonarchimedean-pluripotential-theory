"""Freeze the next local research packet while external export approval is pending."""
from pathlib import Path
import datetime, hashlib, json, shutil

R=Path('/workspace/research');CP=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
active=json.loads((R/'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha']=='604fea852c6a27d4cdc83d97f17393ea67087301'
pending=active['github_pending_checkpoint']
assert pending['files']==76 and 'pending' in pending['state']
assert sha(pending['manifest'])==pending['manifest_sha256']
snapshot=CP/'continuation44-local-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/'
files=[]
def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        copy=snapshot/(str(len(files))+'-'+path.name);shutil.copyfile(path,copy);path=copy
    destination=prefix+target
    assert destination not in {f['path'] for f in files},destination
    files.append({'local':str(path),'path':destination,'sha256':sha(path)})

for n,atom,stem in [(29,'P15.1','P15.1-prescribed-type-zero-volume-energy'),
                    (30,'P15.2','P15.2-prescribed-type-zero-volume-operator')]:
    out=R/f'deliverables/round-{n}'
    manifest=json.loads((R/f'deliverables/round-{n}-bundle-manifest.json').read_text())
    for name,digest in manifest['entries'].items():
        assert sha(out/name)==digest;add(out/name,f'deliverables/round-{n}/'+name)
    add(manifest['bundle'],'deliverables/'+Path(manifest['bundle']).name)
    for name in ['bundle-manifest.json','source-preparation.json','native-request-status.json','visual-check.json']:
        p=R/f'deliverables/round-{n}-{name}';add(p,'deliverables/'+p.name)
    add(out/'first-page.png',f'deliverables/round-{n}/first-page.png')
    review=R/f'campaigns/round-{n}'/(stem+'-review')
    for name in ['review-result.json','review-read-attestation.json','publication-edits.json']:
        add(review/name,f'campaigns/round-{n}/'+review.name+'/'+name)
    phase2=R/'root-checks'/('prescribed-type-zero-volume-'+atom+'-phase2')
    for p in sorted(phase2.iterdir()):
        if p.is_file():add(p,'root-checks/'+phase2.name+'/'+p.name)

batch=json.loads((R/'minimum-reference-zero-volume-batch-manifest.json').read_text())
for c in batch['campaigns']:
    d=Path(c['directory'])
    for name in ['input.json','settings.json','input-manifest.json']:
        add(d/name,'campaigns/'+d.parent.name+'/'+d.name+'/'+name)
    if c['round']==32:
        for name in ['input-v2.json','input-label-correction-v2.json']:
            add(d/name,'campaigns/'+d.parent.name+'/'+d.name+'/'+name)

for name in ['record_prescribed_type_additional_sources.py','record_prescribed_type_zero_volume_review.py',
             'prepare_prescribed_type_zero_volume_paper.py','prepare_prescribed_type_zero_volume_energy_paper_v2.py',
             'export_prescribed_type_zero_volume_paper.py','export_prescribed_type_zero_volume_paper_pending_native.py',
             'publish_prescribed_type_zero_volume_papers.py','prepare_zero_volume_minimum_reference_batch.py',
             'review_minimum_reference_after_completion.py']:
    add(R/name,'checkpoint-scripts/'+name)
for name in ['P15-minimum-reference-full-evidence-20261004.md','minimum-reference-zero-volume-batch-manifest.json',
             'P15-degree-zero-point-carrier-future-proposal-20261004.json']:
    add(R/name,'future-research/'+name)
add(R/'shared-sources/prescribed-type-additional-primary-read-20261004.json',
    'shared-sources/prescribed-type-additional-primary-read-20261004.json')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py']:
    add(R/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
note=snapshot/'CHECKPOINT.txt'
note.write_text('Local packet44: rounds29/30 scoped prescribed-type energy/operator results independently PASS12prem/22pass and PASS10prem/25pass, fully root read/bound and published as separate16/10-page papers with two clean local PDF passes each. Native editor opening/compilation responses remain unconfirmed and are explicitly pending; no native success claimed. New rounds31/32 minimum-reference energy/full-mass operator research running with immutable full proofs/source evidence and independent reviews queued. Degree-zero singleton proposal is future UNVERIFIED evidence, not injected into running campaigns. All42 original problems remain open; goalACTIVE. This packet is local only. Automatic approval review rejected the prior76-file export; the existing specific approval question remains pending. No push script or network mutation is made here. No credentials, SQL, private native transcripts, whole primary PDFs or whole archival text files included.\n')
add(note,'CHECKPOINT.txt')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003',
        'state':'LOCAL_ONLY: independent prepared packet; no external push attempted or authorized by elapsed time',
        'last_successful_remote_commit':active['github_checkpoint']['commit_sha'],
        'prior_pending_export_manifest':pending['manifest'],
        'prior_pending_export_manifest_sha256':pending['manifest_sha256'],
        'files':files,'files_count':len(files),'private_raw_transcripts_or_whole_primary_PDFs':False,
        'fully_solved_original_atoms':[]}
path=CP/'local-packet-continuation44.json';assert not path.exists()
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'local_packet':str(path),'sha256':sha(path),'files':len(files),'network_mutation':False}))
