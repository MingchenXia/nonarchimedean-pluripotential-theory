"""Fresh artifact/support/input consistency audit; not mathematical verification."""
import pathlib,json,hashlib,datetime,platform,sys
P=pathlib.Path.cwd(); sha=lambda b:hashlib.sha256(b).hexdigest()
required=['whole-proof.md','P12.5-paper.tex','whole-source-application-ledger.md','independent-review.md',
          'whole-proof-coverage.md','original-scope-and-noncircularity.md','acceptance-decision.json','native-notes.json',
          'audit_inputs.py','audit_review.py','finite_diagnostics.py','diagnostic-input.json','generate_delivery.py']
assert all((P/f).is_file() for f in required)
n=json.loads((P/'native-notes.json').read_text());known={'G331','B341'}
for note in n['notes']:
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    assert all(s in known for s in note['support']);known.add(note['id'])
assert n['candidate'] and json.loads((P/'acceptance-decision.json').read_text())['candidate']
assert json.loads((P/'evidence/finite-diagnostics.json').read_text())['status']=='PASS'
assert all(r['match'] for r in json.loads((P/'evidence/input-bindings.json').read_text()))
tex=(P/'P12.5-paper.tex').read_bytes()
assert tex.count(b'\\end{document}')==3 # literal G331, literal B341, and own closing
for f in ['G331-qualified.txt','B341-qualified.txt']:
    assert (P/'inputs/grants'/f).read_bytes() in tex
assert not (P/'P12.5-paper.pdf').exists()
files=[]
for path in sorted(P.rglob('*')):
    if path.is_file() and '.git' not in path.parts and path.name not in ['own-artifact-hashes.json','final-audit.json']:
        b=path.read_bytes();files.append({'path':str(path.relative_to(P)),'bytes':len(b),'sha256':sha(b)})
(P/'evidence/own-artifact-hashes.json').write_text(json.dumps(files,indent=2))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS artifact/support/input consistency only',
     'required_files':required,'notes':len(n['notes']),'candidate':n['candidate'],'recorded_files':len(files),
     'compiled':False,'editor_accessed':False,'protected_P16':'UNACCESSED_UNCHANGED',
     'supplied_programs_executed_or_imported':False,'supervised_compute_provided':False,'heavy_compute':False,
     'environment':{'python':sys.version,'platform':platform.platform(),'cwd':str(P)},
     'mathematical_correctness_verified_by_execution':False}
(P/'evidence/final-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
