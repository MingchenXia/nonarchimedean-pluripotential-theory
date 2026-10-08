"""Owned bounded static artifact audit. It is not a mathematical verifier."""
import hashlib
import json
import pathlib

HERE=pathlib.Path(__file__).resolve().parent
required=['P12.3-paper.tex','argument.md','source-application-ledger.md','exact-scope.md',
          'whole-proof-coverage.md','original-scope-and-noncircularity-decision.md',
          'acceptance-decision.json','native-notes.json','original-task.json']
checks={'required_files':all((HERE/p).is_file() for p in required)}
native=json.loads((HERE/'native-notes.json').read_text())
decision=json.loads((HERE/'acceptance-decision.json').read_text())
checks['candidate_false']=native['candidate'] is False and decision['candidate'] is False
seen={'G331','B341','E350'}
for n in native['notes']:
    checks[n['id']+'_body_matches']=(HERE/(n['id']+'.md')).read_text()==n['text']
    checks[n['id']+'_support_order']=all(s in seen for s in n['support'])
    seen.add(n['id'])
exact=(HERE/'inputs/mathematical/21-21-exact-original-task-after-review245.json').read_bytes()
checks['original_exact']=(HERE/'original-task.json').read_bytes()==exact and len(exact)==17550
checks['original_hash']=hashlib.sha256(exact).hexdigest()=='d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
audit=json.loads((HERE/'evidence/input-audit.json').read_text())
checks['bound_record_count']=audit['count']==68
for r in audit['records']:
    b=(HERE/r['local_path']).read_bytes()
    checks['retained_'+r['local_path']]=len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
tex=(HERE/'P12.3-paper.tex').read_text()
checks['display_math_balance']=tex.count('\\[')==tex.count('\\]')
checks['standalone_source']=tex.count('\\begin{document}')==1 and tex.count('\\end{document}')==1
checks['no_source_include']='\\input{' not in tex and '\\include{' not in tex
checks['not_compiled']=not any((HERE/('P12.3-paper.'+ext)).exists() for ext in ['pdf','aux','log'])
diag=json.loads((HERE/'evidence/finite-diagnostics.json').read_text())
checks['finite_declared_cases']=diag['length_cases']==64 and diag['difference_cases']==48 and diag['profile_cases']==272 and diag['all_passed']
report={'all_passed':all(checks.values()),'checks':checks,
        'limitations':'Static identity/support/source balance only; no compiler or mathematical verification.'}
(HERE/'evidence/final-audit.json').write_text(json.dumps(report,indent=2)+'\n')
owned=[]
for p in sorted(HERE.rglob('*')):
    if p.is_file() and 'inputs' not in p.parts and p.name not in ['input.json','own-files.json'] and '.git' not in p.parts:
        b=p.read_bytes();owned.append({'path':str(p.relative_to(HERE)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(HERE/'evidence/own-files.json').write_text(json.dumps({'records':owned,'not_math_verification':True},indent=2)+'\n')
print(json.dumps({'checks':len(checks),'all_passed':report['all_passed'],
                  'owned_files':len(owned),'compiled':False,'candidate':False}))
if not report['all_passed']:
    raise SystemExit(1)
