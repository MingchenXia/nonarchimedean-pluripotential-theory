"""Owned consistency checks; not a mathematical proof checker."""
import pathlib,json,hashlib
from review_data import BASE,OUT,digest
def main():
    n=json.loads((OUT/'native-notes.json').read_text());seen={'G331'};fail=[]
    for note in n['notes']:
        if any(s not in seen for s in note['support']):fail.append('invalid support '+note['id'])
        if note['text'].rstrip()!=(OUT/(note['id']+'.md')).read_text().rstrip():fail.append('note mismatch '+note['id'])
        seen.add(note['id'])
    grants=[]
    for p in (OUT/'qualified-G331').iterdir():
        original=BASE/'immutable-mathematical-DATA'/p.name
        equal=p.read_bytes()==original.read_bytes();grants.append({'file':p.name,'unchanged':equal})
        if not equal:fail.append('grant mismatch '+p.name)
    required=['whole-proof.md','whole-source-application-ledger.md','independent-review.md','whole-proof-coverage.md','original-scope-and-noncircularity.md','acceptance-decision.json','native-notes.json']
    for f in required:
        if not (OUT/f).is_file():fail.append('missing '+f)
    d=json.loads((OUT/'acceptance-decision.json').read_text())
    if not (n['candidate']==d['candidate'] and len(n['notes'])==9):fail.append('status mismatch')
    evidence=json.loads((OUT/'evidence'/'bounded-output.json').read_text())
    if evidence['total']!=2060 or evidence['failures']:fail.append('unexpected diagnostics')
    for p in list(OUT.glob('*.md'))+list(OUT.glob('*.py')):
        if any(ord(c)<32 and c not in '\n\r\t' for c in p.read_text()):fail.append('control character '+p.name)
    owned=[digest(p) for p in sorted(OUT.rglob('*')) if p.is_file() and not any(part.startswith('.') or part=='__pycache__' for part in p.relative_to(OUT).parts) and p.name!='final-consistency.json']
    report={'status':'PASS' if not fail else 'FAIL','failures':fail,'notes':len(n['notes']),'grant_copies':grants,'required_deliverables':required,'own_files':owned,'interpretation':'Artifact consistency and exact finite evidence only; not mathematical validation.'}
    (OUT/'evidence'/'final-consistency.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'notes':9,'failures':fail,'owned_files':len(owned),'grant_copies':grants},indent=2))
if __name__=='__main__':main()
