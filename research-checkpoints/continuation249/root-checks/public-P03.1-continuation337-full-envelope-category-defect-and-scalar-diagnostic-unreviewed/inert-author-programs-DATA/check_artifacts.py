"""Owned administrative checks; does not certify mathematical claims."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    required=['P03.1-paper.tex','P03.1-paper.pdf','argument.md','exact-scope.md',
              'source-application-ledger.md','whole-proof-coverage.md',
              'original-scope-and-noncircularity-decision.md','native-notes.json',
              'input-bindings.json','environment.json','prepare_evidence.py',
              'diagnostics.py','build_artifacts.py','make_notes.py','run_all.py']
    assert all((ROOT/name).is_file() for name in required)
    bindings=json.loads((ROOT/'input-bindings.json').read_text())
    for row in bindings['records']:
        data=(ROOT/row['retained']).read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256']
    for row in bindings['extracts']:
        lines=(ROOT/row['source']).read_bytes().split(b'\n')
        expected=b'\n'.join(lines[row['first_line']-1:row['last_line']])+b'\n'
        actual=(ROOT/row['retained']).read_bytes()
        assert actual==expected and sha(actual)==row['sha256']
    assert (ROOT/'input.json').read_bytes()==(ROOT/'input-bindings/session-input.json').read_bytes()
    notes=json.loads((ROOT/'native-notes.json').read_text())
    assert notes['candidate'] is False
    rows=notes['notes']
    ids=[row['id'] for row in rows]
    assert ids==['n1','n2','n3']
    seen=set()
    for row in rows:
        assert set(row)=={'id','summary','detailedSummary','text','support'}
        assert all(isinstance(row[key],str) and row[key] for key in ['id','summary','detailedSummary','text'])
        assert all(support in seen for support in row['support'])
        seen.add(row['id'])
    assert all(row['exit_code']==0 for row in json.loads((ROOT/'evidence/build.json').read_text())['runs'])
    # Bind owned files and generated artifacts. This excludes its own manifest
    # and the check output that is written after the manifest is generated.
    exclusions={'own-bindings.json','evidence/check-output.txt','evidence/check.json',
                'evidence/execution.json'}
    excluded_dirs={'input-bindings','source-extracts','.git','.agents','.codex','.aws','__pycache__'}
    records=[]
    for path in sorted(ROOT.rglob('*')):
        rel=path.relative_to(ROOT)
        if not path.is_file() or any(part in excluded_dirs for part in rel.parts):
            continue
        if str(rel) in exclusions or str(rel)=='input.json':
            continue
        data=path.read_bytes()
        records.append({'path':str(rel),'bytes':len(data),'sha256':sha(data)})
    value={'algorithm':'sha256','records':records,'self_exclusion':'own-bindings.json',
           'other_exclusions':sorted(exclusions-{'own-bindings.json'}),
           'inputs_bound_separately':'input-bindings.json',
           'meaning':'Byte identities only. No mathematical correctness or review verdict.'}
    (ROOT/'own-bindings.json').write_text(json.dumps(value,indent=2)+'\n')
    result={'required_deliverables':len(required),'bound_input_records':len(bindings['records']),
            'literal_source_excerpts':len(bindings['extracts']),'notes':ids,
            'support_graph_acyclic':True,'candidate':False,'owned_bound_files':len(records),
            'scope':'Administrative checks passed, not a mathematical proof certificate.'}
    (ROOT/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':
    main()
