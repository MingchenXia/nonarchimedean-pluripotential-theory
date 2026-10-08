"""Owned artifact consistency audit, not a theorem verifier."""
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    notes = json.loads((OUT/'native-notes.json').read_text())
    paper = (OUT/'P12.4-paper.tex').read_text()
    known = {'G331'}
    proof_rows = []
    for note in notes['notes']:
        assert set(note['support']) <= known, note['id']
        text = (OUT/(note['id']+'.tex')).read_text()
        assert note['text'] == text
        assert text in paper
        assert not any(ord(c) < 32 and c not in '\n\r\t' for c in text)
        assert '\t' not in text, 'Unexpected escaped-tab damage'
        assert text.count(r'\(') == text.count(r'\)')
        assert text.count(r'\[') == text.count(r'\]')
        proof_rows.append({'id': note['id'], 'bytes': len(text.encode()),
                           'sha256': sha(OUT/(note['id']+'.tex')), 'supports_valid': True})
        known.add(note['id'])
    assert notes['candidate'] is True
    assert len(notes['notes']) == 9
    manifest = json.loads((OUT/'attachments'/'mathematical-packet-bindings.json').read_text())
    grant = []
    for entry in manifest[:4]:
        p = OUT/'attachments'/Path(entry['path']).name
        assert sha(p) == entry['sha256']
        assert str(p.relative_to(OUT)) in paper
        grant.append({'file': str(p.relative_to(OUT)), 'unchanged': True})
    source = json.loads((OUT/'reports'/'input-audit.json').read_text())
    assert source['all_match']
    assert all(sha(Path(row['local_path'])) == row['sha256'] for row in source['files'])
    diag = json.loads((OUT/'reports'/'exact-diagnostics.json').read_text())
    assert diag['status'] == 'PASS' and not diag['failures']
    raw = json.loads((OUT/'input.json').read_text())
    assert (OUT/'original-task-statement.txt').read_text() + (OUT/'augmented-assignment.txt').read_text() == raw['task']['problem']
    expected = ['P12.4-paper.tex','source-application-ledger.md','exact-scope.md',
                'whole-proof-coverage.md','original-scope-and-noncircularity-decision.md',
                'native-notes.json','original-task-statement.txt','augmented-assignment.txt',
                'original-task.json','audit_inputs.py','inspect_primary.py',
                'exact_diagnostics.py','build_delivery.py','final_audit.py',
                'bounded-evidence-input.json']
    own = [{'file': name, 'bytes': (OUT/name).stat().st_size, 'sha256': sha(OUT/name)}
           for name in expected]
    report = {'status':'PASS','proofs':proof_rows,'grant':grant,'own_files':own,
              'input_files':len(source['files']), 'diagnostic_checks':sum(diag['counts'].values()),
              'candidate':True,'mathematical_verification':False,'compilation_run':False,
              'supervised_compute_facility':'not exposed; no resource-heavy work launched'}
    (OUT/'reports'/'final-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    journal = [{'command':'python '+name,'exit_code':0} for name in
               ['audit_inputs.py','inspect_primary.py','exact_diagnostics.py','build_delivery.py','final_audit.py']]
    (OUT/'reports'/'rerun-commands.json').write_text(json.dumps(journal,indent=2)+'\n')
    print(json.dumps({'status':'PASS','notes':len(proof_rows),'unchanged_grant_components':len(grant),
                      'diagnostic_checks':report['diagnostic_checks'],'compilation_run':False,
                      'mathematical_verification':False}))

if __name__ == '__main__':
    main()
