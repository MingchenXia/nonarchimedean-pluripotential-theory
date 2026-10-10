from pathlib import Path
import json, hashlib, subprocess, collections
repo=Path('/workspace/recovered-research-repository')
root=Path('/workspace/research')
base=repo/'manuscript/editorial/xean_research_20261003'
missing=collections.defaultdict(list)
for p in base.glob('UPLOAD_MANIFEST*.json'):
    d=json.loads(p.read_text())
    entries=list(d.get('files',[]))+[b.get('original',{}) for b in d.get('whole_body_binding',[])]
    for e in entries:
        local=e.get('local')
        sha=e.get('sha256')
        if not isinstance(local,str) or not local.startswith('/workspace/research/') or not isinstance(sha,str):
            continue
        target=Path(local)
        if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==sha:
            continue
        missing[sha].append({'local':local,'manifest':p.name,'bytes':e.get('bytes')})
pdfsha='991de3becf3cca896ec089241a9489deca3c9cbc26b57df1bc3062008a1dd3ee'
proc=subprocess.Popen(['git','cat-file','--batch-all-objects','--batch'],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
matches=[]
objects=blobs=totalbytes=0
while True:
    header=proc.stdout.readline()
    if not header:
        break
    oid,kind,size=header.decode('ascii').strip().split()
    size=int(size)
    payload=proc.stdout.read(size)
    assert len(payload)==size and proc.stdout.read(1)==b'\n'
    objects+=1
    if kind!='blob':
        continue
    blobs+=1
    totalbytes+=size
    sha=hashlib.sha256(payload).hexdigest()
    if sha not in missing and sha!=pdfsha:
        continue
    retained=root/'recovery-LOCALONLY/historical-payloads'/sha
    retained.parent.mkdir(parents=True,exist_ok=True)
    retained.write_bytes(payload)
    restored=[]
    for e in missing.get(sha,[]):
        target=Path(e['local'])
        assert root in target.parents and '..' not in target.parts
        if target.exists():
            continue
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(payload)
        restored.append(str(target))
    if sha==pdfsha:
        dest=root/'primary-data-LOCALONLY/original-document-991de3.pdf'
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(payload)
        restored.append(str(dest))
    matches.append({'git_blob':oid,'sha256':sha,'bytes':size,'retained':str(retained),'restored':restored,'matching_manifest_records':missing.get(sha,[])})
assert proc.wait()==0,proc.stderr.read().decode()
report={'objects_scanned':objects,'blobs_scanned':blobs,'blob_bytes_scanned':totalbytes,'missing_unique_hashes_before_scan':len(missing),'recovered_unique_hashes':len(matches),'matches':matches,'original_pdf_recovered':any(m['sha256']==pdfsha for m in matches),'mathematical_acceptance_credit':False,'supplied_programs_executed':False}
out=root/'recovery-LOCALONLY/git-history-recovery.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='matches'}))
