"""Capture rerun outputs and check delivery consistency without claiming a proof check."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
archive=ROOT/'build-initial'
if (ROOT/'build-report.json').exists() and not archive.exists():
    archive.mkdir()
    for name in ['build-report.json','P13.1-paper.tex','P13.1-paper.pdf',
                 'pandoc-conversion.stdout.txt','pandoc-conversion.stderr.txt',
                 'tex-pass-1.stdout.txt','tex-pass-1.stderr.txt','tex-pass-1.log',
                 'tex-pass-2.stdout.txt','tex-pass-2.stderr.txt','tex-pass-2.log']:
        if (ROOT/name).exists(): shutil.copyfile(ROOT/name,archive/name)

report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'epistemic_status':'Artifact consistency and finite execution checks; not mathematical verification.',
        'commands':[]}
for name in ['audit_sources.py','checks.py','build.py']:
    argv=[sys.executable,name]
    p=subprocess.run(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stem=Path(name).stem
    (ROOT/f'{stem}.stdout.txt').write_bytes(p.stdout)
    (ROOT/f'{stem}.stderr.txt').write_bytes(p.stderr)
    report['commands'].append({'argv':argv,'returncode':p.returncode,
                               'stdout':f'{stem}.stdout.txt','stderr':f'{stem}.stderr.txt'})
    assert p.returncode==0,(name,p.stderr.decode())

assert (ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes()
inp=json.loads((ROOT/'input.json').read_text())
assert (ROOT/'assignment-original.txt').read_text()==inp['assignment']
assert json.loads((ROOT/'task-original.json').read_text())==inp['task']
status=json.loads((ROOT/'status.json').read_text())
assert list(status)==['id','status','exact_result','proof_file','concrete_gaps']
assert status['status']=='partial'
provenance=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
assert len(provenance['sources'])==8
excerpt_count=sum(len(s['excerpts']) for s in provenance['sources'])
assert excerpt_count==55
for source in provenance['sources']:
    for excerpt in source['excerpts']:
        b=(ROOT/excerpt['file']).read_bytes()
        assert b==excerpt['literal'].encode('utf-8')
        assert hashlib.sha256(b).hexdigest()==excerpt['sha256']
build=json.loads((ROOT/'build-report.json').read_text())
assert build['two_successful_tex_passes']
for fname,meta in build['artifacts'].items():
    assert hashlib.sha256((ROOT/fname).read_bytes()).hexdigest()==meta['sha256']
report['warnings']={}
for num in [1,2]:
    lines=(ROOT/f'tex-pass-{num}.log').read_text().splitlines()
    report['warnings'][f'pass_{num}']=[x for x in lines if 'Warning' in x or 'Overfull' in x or 'Missing character' in x]
report['input_original_byte_identical']=True
report['source_hash_checks']=8
report['literal_excerpt_checks']=excerpt_count
report['two_successful_tex_passes']=True
report['status_schema_checked']=True
report['result_status']='partial'
report['mathematical_solution_claimed']=False
(ROOT/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
