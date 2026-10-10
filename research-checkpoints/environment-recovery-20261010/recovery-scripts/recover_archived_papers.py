from pathlib import Path, PurePosixPath
import json, hashlib, zipfile, re
repo=Path('/workspace/recovered-research-repository')
root=Path('/workspace/research')
base=repo/'manuscript/editorial/xean_research_20261003/bundles'
records=[]
for archive in sorted(base.glob('*.zip')):
    archive_sha=hashlib.sha256(archive.read_bytes()).hexdigest()
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            member=PurePosixPath(info.filename)
            if info.is_dir():
                continue
            if member.is_absolute() or '..' in member.parts or (info.external_attr>>16)&0o170000==0o120000:
                raise ValueError('unsafe archive member')
            payload=z.read(info)
            retained=root/'recovery-LOCALONLY/archive-extraction'/archive_sha/str(member)
            retained.parent.mkdir(parents=True,exist_ok=True)
            retained.write_bytes(payload)
            target=None
            if archive.name=='reviewed-papers.zip' and member.parts[0]=='papers':
                target=root/str(member)
            elif archive.name.startswith('reviewed-papers-round-'):
                roundname=archive.stem.removeprefix('reviewed-papers-')
                if member.parts[0]==roundname:
                    target=root/'deliverables'/str(member)
                elif len(member.parts)==1:
                    target=root/'deliverables'/roundname/str(member)
            status='retained in recovery archive directory'
            if target is not None:
                if not target.exists():
                    target.parent.mkdir(parents=True,exist_ok=True)
                    target.write_bytes(payload)
                    status='original path restored'
                elif target.read_bytes()==payload:
                    status='original path already byte-identical'
                else:
                    status='existing original path preserved; distinct historical archive copy retained'
            records.append({'archive':str(archive),'archive_sha256':archive_sha,'member':str(member),'sha256':hashlib.sha256(payload).hexdigest(),'bytes':len(payload),'retained':str(retained),'original_path':str(target) if target else None,'status':status})
out=root/'recovery-LOCALONLY/archive-recovery.json'
out.write_text(json.dumps({'records':records,'programs_executed':False,'mathematical_acceptance_credit':False},indent=2)+'\n')
print(json.dumps({'members_recovered':len(records),'original_paths_restored':sum(r['status']=='original path restored' for r in records),'PDFs_retained':sum(r['member'].endswith('.pdf') for r in records),'TeX_sources_retained':sum(r['member'].endswith('.tex') for r in records)}))
