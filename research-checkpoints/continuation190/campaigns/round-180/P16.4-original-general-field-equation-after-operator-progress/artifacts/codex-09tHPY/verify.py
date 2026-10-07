#!/usr/bin/env python3
"""Record artifact checks and tool observations, without certifying mathematics."""
from pathlib import Path
import hashlib,json,subprocess,re,datetime

ROOT=Path(__file__).resolve().parent

def main():
    records=[]
    cmds=[['pdfinfo','P16.4-paper.pdf'],
          ['pdftotext','P16.4-paper.pdf','P16.4-paper.extract.txt'],
          ['pandoc','--version'],['pdflatex','--version']]
    for i,cmd in enumerate(cmds,1):
        p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
        out=f'verification-{i:02d}.stdout.txt';err=f'verification-{i:02d}.stderr.txt'
        Path(out).write_text(p.stdout);Path(err).write_text(p.stderr)
        records.append(dict(argv=cmd,returncode=p.returncode,stdout=out,stderr=err))
        assert p.returncode==0
    submission=json.loads(Path('submission.json').read_text())
    assert submission['candidate'] is False
    seen=set()
    for n in submission['notes']:
        assert n['id'] not in seen and set(n['support'])<=seen
        assert all(re.fullmatch('n[1-9][0-9]*',s) for s in n['support'])
        seen.add(n['id'])
    ledger=json.loads(Path('source-application-ledger.json').read_text())
    for entry in ledger['entries']:
        for filename in entry['snapshots']: assert Path(filename).is_file()
    tex=Path('P16.4-paper.tex').read_text()
    log=Path('P16.4-paper.log').read_text()
    pdf_text=Path('P16.4-paper.extract.txt').read_text()
    assert tex.count('\\(')>200
    assert 'Fatal error' not in log and 'Undefined control sequence' not in log
    assert 'candidate=false' in pdf_text
    assert 'Precise residual equation inputs' in pdf_text
    assert json.loads(Path('check-results.json').read_text())['status']=='PASS'
    assert all(r.get('returncode')==0 for r in json.loads(Path('environment-and-build.json').read_text())['commands'])
    result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                status='PASS artifact and finite-check observations',candidate=False,
                mathematical_certification=False,commands=records,
                registered_note_ids=sorted(seen),support_dag_valid=True,
                inline_math_pairs=tex.count('\\('),
                latex_warnings=[s for s in log.splitlines() if 'Warning' in s or 'Underfull' in s or 'Overfull' in s],
                pdf_pages=int(re.search(r'^Pages:\s+(\d+)',Path('verification-01.stdout.txt').read_text(),re.M)[1]))
    Path('final-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    paths=[p for p in ROOT.rglob('*') if p.is_file() and
           p.suffix in {'.py','.json','.md','.tex','.pdf','.txt'} and p.name!='artifact-hashes.json']
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
    Path('artifact-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
