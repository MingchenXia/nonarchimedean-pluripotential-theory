"""Own data-only duplicate audit. It is not a theorem/reading certificate."""
from pathlib import Path
import json, re, hashlib

root=Path.cwd(); p=root/'inputs/mathematical'
f=lambda i: next(p.glob(f'{i:02d}-*'))
actual=json.loads(f(35).read_text()); expanded=json.loads(f(34).read_text())
argument=f(33).read_text(); tex=f(32).read_text()
sections=re.split(r'\\section\{[^\n]+\}\n',tex)[1:8]
extra=sections[-1].split(r'\section*{Published application')[1]
sections[-1]=sections[-1].split(r'\section*{Published application')[0]
def norm(s):
    s=s.replace(r'\textasciicircum{}','^')
    s=re.sub(r'\\([_$#%&{}])',r'\1',s)
    return re.sub(r'\s+',' ',s).strip()
matches=[]
for j,n in enumerate(expanded['notes']):
    body=f(42+j).read_text()
    assert n['text']==body and body.strip() in argument
    without_header=body.split('\n',1)[1]
    assert norm(without_header)==norm(sections[j])
    matches.append({'id':n['id'],'expanded_file_exact':True,
                    'argument_exact_body':True,'tex_explicit_escaping_and_whitespace_only':True,
                    'actual_equals_expanded':actual['notes'][j]==n})
o=json.loads((root/'input.json').read_text())
grants={n['id']:n for n in o['notes']}
checks={'G331_paper_exact_in_grant':f(0).read_text() in grants['G331']['text'],
        'E350_paper_exact_in_grant':f(5).read_text() in grants['E350']['text'],
        'E350_whole_proof_exact_in_grant':f(6).read_text() in grants['E350']['text'],
        'binding40_equals57':f(40).read_bytes()==f(57).read_bytes()}
assert all(checks.values())
(root/'original-task.json').write_bytes(f(21).read_bytes())
report={'expanded_matches':matches,'qualified_duplicate_bodies':checks,
        'reading_boundary':'Actual FINAL every field read separately. Expanded proof bodies read in n1--n7 files; nonbody fields read separately. Typeset proof duplicates checked with explicit escaping, not claimed fresh duplicate readings. Header and additional bridge read. Source HTML/text immediate units read; no whole PDF visual claim. Audit success itself is not reading or mathematical correctness.',
        'paper_additional_bridge':extra.split(r'\end{document}')[0].strip(),
        'actual_note_ids':[n['id'] for n in actual['notes']],
        'original_bytes':len(f(21).read_bytes()),
        'original_sha256':hashlib.sha256(f(21).read_bytes()).hexdigest()}
(root/'reports/reading-duplicates.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'expanded_bodies':len(matches),'duplicate_checks':checks,'actual_expanded_distinct':all(not x['actual_equals_expanded'] for x in matches)}))
