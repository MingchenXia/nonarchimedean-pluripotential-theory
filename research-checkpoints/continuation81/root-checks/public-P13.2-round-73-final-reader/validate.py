import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def main():
    checks=[]
    def check(name,value):
        assert value,name
        checks.append(name)
    check('byte-identical input preservation',(ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes())
    input_data=json.loads((ROOT/'input.json').read_bytes())
    check('assignment preserved',(ROOT/'assignment-original.txt').read_text()==input_data['assignment'])
    check('task unchanged',json.loads((ROOT/'task-original.json').read_bytes())==input_data['task'])
    status=json.loads((ROOT/'status.json').read_text())
    check('exact status schema',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
    check('partial and concrete original gaps',status['status']=='partial' and len(status['concrete_gaps'])>=5)
    result=json.loads((ROOT/'canonical-notes.json').read_text())
    check('candidate flag false',result['candidate'] is False)
    check('at most four full notes',1<=len(result['notes'])<=4)
    seen=set()
    for n in result['notes']:
        check('complete note '+n['id'],set(n)=={'id','summary','detailedSummary','text','support'} and len(n['text'])>1000)
        check('backward local support '+n['id'],all(s in seen for s in n['support']))
        seen.add(n['id'])
    sources=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
    check('all seventeen sources',len(sources['sources'])==17)
    for f in sources['verified_files']:
        check('source file hash '+f['id']+' '+f['kind'],hashlib.sha256(Path(f['path']).read_bytes()).hexdigest()==f['sha256'])
    for e in sources['excerpts']:
        lines=(ROOT/'source-extracts'/f"{e['id']}-full.txt").read_bytes().decode('utf-8').split('\n')
        check('literal LF coordinates '+e['file'],'\n'.join(lines[e['lf_start']-1:e['lf_end']])==e['literal'])
    build=json.loads((ROOT/'build-report.json').read_text())
    check('two successful retained TeX passes',len([c for c in build['commands'] if c['label'].startswith('tex-pass-') and c['returncode']==0])==2)
    for filename,meta in build['artifacts'].items():
        check('compiled artifact hash '+filename,hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==meta['sha256'])
    arithmetic=json.loads((ROOT/'checks-output.json').read_text())
    check('finite diagnostics passed',arithmetic['status']=='passed' and arithmetic['total_cases']==29067)
    report={'status':'passed','checks':checks,'count':len(checks),
            'candidate':False,'limitation':'Artifact integrity and finite arithmetic only; no mathematical correctness verdict.'}
    (ROOT/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','artifact_checks':len(checks),'candidate':False},indent=2))

if __name__=='__main__':main()
