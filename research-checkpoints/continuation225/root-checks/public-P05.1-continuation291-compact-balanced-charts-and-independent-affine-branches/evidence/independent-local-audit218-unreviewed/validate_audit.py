"""Own finite deliverable checks; not mathematical certification."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
def read(name):return json.loads((root/name).read_text())
n=read('native-notes.json'); seen=set()
for note in n['notes']:
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    assert note['id'] not in seen and set(note['support'])<=seen
    assert all(isinstance(note[k],str) and note[k] for k in ['id','summary','detailedSummary','text'])
    assert note['text']==(root/'notes'/f"{note['id']}.txt").read_text()
    seen.add(note['id'])
assert len(seen)==7 and n['candidate'] is False
r=read('audit-report.json');w=read('wholeproof-premise-coverage.json')
assert r['candidate'] is False and r['original_P05_1']=='OPEN'
assert r['proof_modified'] is False and r['mathematical_acceptance'] is False
assert r['own_full_reasoning_notes']==n['notes']
assert len(w['mathematical_bodies'])==38 and all(not e['uncovered_ranges'] for e in w['mathematical_bodies'])
assert len(w['actual_FINAL_notes'])==6 and w['whole_NEW291_parallel_argument_displayed']
assert w['exactly_five_grants']==['A224','B225','R230','S262','S272']
assert len(w['units'])==23
assert len(read('frozen-file-bindings.json'))==115 and all(e['matches'] for e in read('frozen-file-bindings.json'))
assert read('source-application-audit.json')['verdict']=='FAIL'
assert read('historical-evidence-audit.json')['verdict']=='INCONCLUSIVE'
assert read('evidence/exact-checks-output.json')['assertions']==1945
build=read('evidence/own-build-report.json')
assert [e['exit_code'] for e in build['passes']]==[0,0]
assert build['pandoc']['exit_code']==0 and build['pandoc']['source_to_markdown_byte_match']
assert build['source_before']==build['source_after']==hashlib.sha256((root/'build/P05.1-paper.tex').read_bytes()).hexdigest()
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name in ['own-artifact-bindings.json','validation-report.json']:
        continue
    if '.git' in p.parts:continue
    raw=p.read_bytes()
    files.append(dict(filename=str(p.relative_to(root)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
                      LOCALONLY=p.relative_to(root).parts[0]=='LOCALONLY'))
(root/'own-artifact-bindings.json').write_text(json.dumps(dict(files=files,candidate=False,
                     meaning='Own artifact identities only; not proof correctness'),indent=2)+'\n')
result=dict(own_notes=7,valid_earlier_supports=True,whole_mathematical_bodies=38,
            covered_NEW291_units=23,actual_FINAL_notes=6,bound_unchanged_files=115,
            required_deliverables_present=True,own_artifacts=len(files),candidate=False,
            original='OPEN',mathematical_certification=False)
(root/'validation-report.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
