#!/usr/bin/env python3
"""Rebuild and audit the documentary deliverable offline. This does not verify proofs."""
import datetime,hashlib,json,os,pathlib,platform,re,shutil,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parent
os.chdir(ROOT);(ROOT/'logs').mkdir(exist_ok=True)
history=[]
def command(argv,label):
    r=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    (ROOT/f'logs/{label}.stdout.txt').write_text(r.stdout)
    (ROOT/f'logs/{label}.stderr.txt').write_text(r.stderr)
    history.append({'argv':argv,'cwd':str(ROOT),'returncode':r.returncode,
                    'stdout':f'logs/{label}.stdout.txt','stderr':f'logs/{label}.stderr.txt'})
    if r.returncode:
        (ROOT/'logs/commands.json').write_text(json.dumps(history,indent=2)+'\n')
        raise RuntimeError(f'{label} failed: see logs/{label}.stderr.txt')
    print(label,'OK')
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
env={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(ROOT),
     'platform':platform.platform(),'python':sys.version,'tools':{},
     'scope':'Only supplied workspace files and preserved public-primary data. No tools installed; no heavy computation.',
     'compute_facility':'No supervised compute service exposed or needed.',
     'proof_status':'unverified mathematical draft; byte/compilation/arithmetic success is not mathematical certification'}
for t in ['python3','pandoc','pdflatex','pdftotext']:
    p=shutil.which(t);assert p,f'missing existing {t}'
    a=[p,'-v'] if t=='pdftotext' else [p,'--version']
    r=subprocess.run(a,capture_output=True,text=True)
    env['tools'][t]={'path':p,'version':(r.stdout+r.stderr).splitlines()[:3]}
(ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
for s in ['preserve_inputs.py','build_evidence.py','diagnostics.py','build_result.py']:
    command([sys.executable,s],s[:-3])
assert (ROOT/'input.json').read_bytes()==(ROOT/'preserved/input-original.json').read_bytes()
input_data=json.loads((ROOT/'input.json').read_text())
assert json.loads((ROOT/'preserved/task-original.json').read_text())==input_data['task']
assert (ROOT/'preserved/assignment-original.txt').read_text()==input_data['assignment']
checked=0
for mf in ['preserved/manifest.json','primary-units/manifest.json','primary-dictionary/manifest.json']:
    for r in json.loads((ROOT/mf).read_text()):
        assert sha(r['artifact'])==r['sha256'],r['artifact'];checked+=1
for r in json.loads((ROOT/'preserved/manifest.json').read_text()):
    if 'character_interval' in r:
        a,b=r['character_interval'];assert input_data['assignment'][a:b].encode()==(ROOT/r['artifact']).read_bytes()
ledger=json.loads((ROOT/'external-premises.json').read_text())
assert [r['id'] for r in ledger['external_premises']]==[f'E{i}' for i in range(11)]
premise_bodies=0
for r in ledger['external_premises']:
    assert r['statement'] and r['url'] and r['version'] and r['pertinent_statement_and_proof_bodies']
    for b in r['pertinent_statement_and_proof_bodies']:
        assert sha(b['artifact'])==b['sha256'];premise_bodies+=1
        lo,hi=b['local_inclusive_LF'];assert 1<=lo<=hi<=len((ROOT/b['artifact']).read_text().split('\n'))
grant=ledger['grant'];assert grant['id']=='G0'
assert sha(grant['complete_supplied_body']['artifact'])==grant['complete_supplied_body']['sha256']
res=json.loads((ROOT/'canonical-result.json').read_text());notes=res['notes']
assert 1<=len(notes)<=4
known=set()
for n in notes:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    assert n['id'] not in known and all(s in known for s in n['support'])
    assert all(n[k] for k in ['summary','detailedSummary','text'])
    known.add(n['id'])
status=json.loads((ROOT/'status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id']==notes[-1]['id']
command(['pandoc','P16.5-paper.md','--standalone','--from=markdown+tex_math_dollars',
         '--to=latex','--output=P16.5-paper.tex'], 'pandoc')
for i in [1,2]:
    command(['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.5-paper.tex'],f'pdflatex-pass-{i}')
command(['pdftotext','-layout','P16.5-paper.pdf','P16.5-paper-rendered.txt'],'pdftotext')
rendered=(ROOT/'P16.5-paper-rendered.txt').read_text()
assert 'Theorem 1' in rendered and 'Theorem 2' in rendered and 'Appendix' in rendered
log=(ROOT/'P16.5-paper.log').read_text()
warnings=[s for s in log.splitlines() if 'Warning' in s or 'Overfull' in s]
ver={'input_sha256':sha('input.json'),'preserved_artifacts_checked':checked,
     'external_premises':11,'task_grants':1,'premise_body_bindings_checked':premise_bodies,
     'canonical_note_ids':[n['id'] for n in notes],'support_edges':{n['id']:n['support'] for n in notes},
     'status_keys':list(status),'candidate':res['candidate'],
     'pdf_pages_from_formfeeds':rendered.count('\f'),'latex_warnings':warnings,
     'limitations':'Checks are documentary only. No source-wide arXiv binary hash or mathematical verification is claimed.'}
artifacts=['P16.5-paper.md','P16.5-paper.tex','P16.5-paper.pdf','canonical-result.json','status.json',
           'external-premises.json','diagnostics-output.json','preserve_inputs.py','build_evidence.py',
           'diagnostics.py','build_result.py','canonical-note-texts.json','rerun.py']
ver['deliverable_sha256']={p:sha(p) for p in artifacts}
(ROOT/'verification.json').write_text(json.dumps(ver,indent=2)+'\n')
(ROOT/'logs/commands.json').write_text(json.dumps(history,indent=2)+'\n')
print(json.dumps(ver,indent=2))
