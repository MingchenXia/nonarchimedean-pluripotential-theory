#!/usr/bin/env python3
"""Verify supplied/HTTP literal data, check finite arithmetic, and build with existing tools."""
import hashlib, json, os, pathlib, platform, subprocess, sys

root=pathlib.Path(__file__).resolve().parent
logs=root/'logs';logs.mkdir(exist_ok=True)
commands=[]
def run(argv,label,check=True):
    proc=subprocess.run(argv,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (logs/(label+'.stdout')).write_bytes(proc.stdout)
    (logs/(label+'.stderr')).write_bytes(proc.stderr)
    commands.append({'argv':argv,'cwd':str(root),'returncode':proc.returncode,
                     'stdout':'logs/'+label+'.stdout','stderr':'logs/'+label+'.stderr'})
    if check and proc.returncode:
        (logs/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
        sys.stderr.write(proc.stderr.decode(errors='replace')[-2500:])
        sys.stderr.write(proc.stdout.decode(errors='replace')[-3500:])
        raise SystemExit(proc.returncode)
    return proc

environment={'python':sys.version,'platform':platform.platform(),'machine':platform.machine(),
 'cwd':str(root),'allowed_computation':'lightweight source binding and finite rational arithmetic only',
 'network_observation':'Local urllib original-PDF request denied with Operation not permitted; public primary HTTP renderer was available in the authoring session.',
 'compute_service':'No supervised compute service exposed; none required or used.',
 'tools_installed_by_this_task':False}
for name,argv in [('pandoc',['pandoc','--version']),('pdftex',['pdflatex','--version'])]:
    p=run(argv,'version-'+name)
    environment[name]=p.stdout.decode(errors='replace').split('\n')[0]
(root/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
run([sys.executable,'make_evidence.py'],'evidence')
run([sys.executable,'finite_checks.py'],'finite-checks')
status=json.loads((root/'status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['status']=='incomplete' and status['concrete_gaps']
if (root/'notes.json').exists():
    packet=json.loads((root/'notes.json').read_text())
    assert packet['candidate'] is False and len(packet['notes'])<=4
    prior=set()
    for i,n in enumerate(packet['notes'],1):
        assert n['id']=='n'+str(i)
        assert set(n)=={'id','summary','detailedSummary','text','support'}
        assert set(n['support'])<=prior
        prior.add(n['id'])
    (logs/'note-support-check.json').write_text(json.dumps({'note_count':len(prior),'backward_supports_only':True,'candidate':False},indent=2)+'\n')
run(['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex',
     '--output=P16.5-paper.tex'],'pandoc')
for pass_id in [1,2]:
    run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex'],
        'pdflatex-pass-'+str(pass_id))
pdf=root/'P16.5-paper.pdf'
assert pdf.read_bytes().startswith(b'%PDF-') and pdf.stat().st_size>1000
(logs/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
excluded={'artifact-manifest.json'}
manifest=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name in excluded or any(x in p.parts for x in ['.git','.agents','.codex','.aws','__pycache__']):continue
    b=p.read_bytes()
    manifest.append({'path':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'artifact-manifest.json').write_text(json.dumps({'files':manifest,'meaning':'byte binding only; no mathematical certification'},indent=2)+'\n')
print(json.dumps({'status':status['status'],'candidate':False,'pdf_bytes':pdf.stat().st_size,
                  'manifest_files':len(manifest),'proof_file':status['proof_file']},sort_keys=True))
