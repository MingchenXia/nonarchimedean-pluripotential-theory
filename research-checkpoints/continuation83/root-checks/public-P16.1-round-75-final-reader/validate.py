#!/usr/bin/env python3
import hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    checks=[]
    def check(label,ok):
        assert ok,label
        checks.append(label)
    check('input byte preservation',(ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes())
    data=json.loads((ROOT/'input.json').read_text())
    check('task unchanged',json.loads((ROOT/'task-original.json').read_text())==data['task'])
    check('assignment unchanged',(ROOT/'assignment-original.txt').read_text()==data['assignment'])
    status=json.loads((ROOT/'status.json').read_text())
    check('exact five status fields',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
    check('partial status',status['status']=='partial')
    output=json.loads((ROOT/'canonical-notes.json').read_text())
    check('honest candidate',output['candidate'] is False)
    check('at most four full notes',0<len(output['notes'])<=4)
    ids=[]
    for note in output['notes']:
        check('note keys '+note['id'],set(note)=={'id','summary','detailedSummary','text','support'})
        check('backward support '+note['id'],all(s in ids for s in note['support']))
        check('nonempty full text '+note['id'],len(note['text'])>2000)
        ids.append(note['id'])
    sources=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
    for source in sources['sources']:
        for f in source['files']:
            check('source copy '+f['local_file'],sha(ROOT/f['local_file'])==f['sha256'])
    for unit in sources['units']:
        check('literal hash '+unit['id'],sha(ROOT/unit['literal_file'])==unit['literal_sha256'])
        source=next(s for s in sources['sources'] if s['id']==unit['id'].split('-')[0])
        textfile=next(f['local_file'] for f in source['files'] if f['role']=='literal_extract')
        lines=(ROOT/textfile).read_bytes().decode('utf-8').split('\n')
        a,b=unit['inclusive_one_based_LF']
        check('literal LF equality '+unit['id'],(ROOT/unit['literal_file']).read_bytes()=='\n'.join(lines[a-1:b]).encode('utf-8'))
    build=json.loads((ROOT/'build-report.json').read_text())
    for f,h in build['artifacts'].items():check('build hash '+f,sha(ROOT/f)==h)
    for j in [1,2]:check('full pass log '+str(j),(ROOT/f'build-logs/tex-pass-{j}.log').stat().st_size>5000)
    check('PDF header',(ROOT/'P16.1-paper.pdf').read_bytes().startswith(b'%PDF'))
    check('diagnostics passed',json.loads((ROOT/'finite-checks.json').read_text())['status']=='all finite diagnostics passed')
    report={'status':'passed','checks':checks,'check_count':len(checks),
            'limits':'Artifact/provenance/finite-execution audit only. No certification of mathematical correctness or completion.'}
    (ROOT/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'artifact_checks':len(checks),'status':'passed'}))
if __name__=='__main__':main()
