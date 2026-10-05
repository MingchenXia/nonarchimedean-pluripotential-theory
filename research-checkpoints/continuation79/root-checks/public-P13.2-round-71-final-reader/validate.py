from pathlib import Path
import hashlib
import json
import subprocess

root=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
original=(root/'input-original.json').read_bytes()
assert (root/'input.json').read_bytes()==original
data=json.loads(original)
assert (root/'assignment-original.txt').read_bytes().decode('utf-8')==data['assignment']
assert json.loads((root/'task-original.json').read_bytes())==data['task']
for p,h in json.loads((root/'preservation.json').read_text()).items():
    assert sha(root/p)==h
status=json.loads((root/'status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['status']=='partial' and status['concrete_gaps']
notes=json.loads((root/'canonical-notes.json').read_text())
assert notes['candidate'] is False and 0<len(notes['notes'])<=4
seen=set()
for note in notes['notes']:
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    assert all(s in seen for s in note['support'])
    seen.add(note['id'])
provenance=json.loads((root/'source-extracts/source-provenance.json').read_text())
assert len(provenance['sources'])==11 and provenance['all_expected_hashes_match']
for src in provenance['sources']:
    original_bytes=Path(src['descriptor']['literal_extract']).read_bytes()
    assert (root/src['complete_literal_copy']).read_bytes()==original_bytes
    lines=original_bytes.decode('utf-8').split('\n')
    for ex in src['excerpts']:
        assert '\n'.join(lines[ex['start_LF']-1:ex['end_LF']])==ex['literal']
build=json.loads((root/'build-report.json').read_text())
assert build['two_TeX_passes_succeeded']
assert len(build['commands'])==3 and all(c['returncode']==0 for c in build['commands'])
for name in ['P13.2-argument.md','P13.2-paper.tex','P13.2-paper.pdf',
             'tex-pass-1.log','tex-pass-2.log','tex-pass-1.stdout',
             'tex-pass-2.stdout','tex-pass-1.stderr','tex-pass-2.stderr',
             'pandoc.stdout','pandoc.stderr','environment.json','checks-output.json']:
    assert (root/name).exists()
checks=json.loads((root/'checks-output.json').read_text())
assert checks['all_passed']
r=subprocess.run(['pdfinfo','P13.2-paper.pdf'],cwd=root,capture_output=True)
(root/'pdfinfo.stdout').write_bytes(r.stdout)
(root/'pdfinfo.stderr').write_bytes(r.stderr)
report={'input_byte_identical':True,'task_and_assignment_preserved':True,
        'status_schema_exact':True,'candidate':False,
        'notes_backward_support_only':True,'literal_LF_excerpts_checked':True,
        'primary_files_verified':sum(len(s['verified_files']) for s in provenance['sources']),
        'two_TeX_passes_succeeded':True,'finite_diagnostics_passed':True,
        'proof_sha256':sha(root/'P13.2-argument.md'),
        'tex_sha256':sha(root/'P13.2-paper.tex'),
        'pdf_sha256':sha(root/'P13.2-paper.pdf'),
        'mathematical_completeness_certified':False}
(root/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
