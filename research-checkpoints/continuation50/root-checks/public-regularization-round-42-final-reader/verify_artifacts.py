"""Check artifact consistency; no mathematical proof validation is performed."""
from pathlib import Path
import json,hashlib
from pypdf import PdfReader

p=Path('.')
original=p/'input-original.json'; current=p/'input.json'
assert original.read_bytes()==current.read_bytes()
data=json.loads(current.read_text())
assert (p/'assignment-original.txt').read_text()==data['assignment']
assert json.loads((p/'task-original.json').read_text())==data['task']
status=json.loads((p/'status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['status']=='partial'
build=json.loads((p/'tex-build-diagnostics.json').read_text())
assert len(build['passes'])==2 and all(x['exit_code']==0 for x in build['passes'])
assert build['argument_sha256']==hashlib.sha256((p/'P02.2-argument.md').read_bytes()).hexdigest()
assert build['tex_sha256']==hashlib.sha256((p/'P02.2-paper.tex').read_bytes()).hexdigest()
sources=json.loads((p/'source-extracts/source-provenance.json').read_text())
for source in sources['sources']:
    assert source['pdf_sha256']==hashlib.sha256(Path(source['pdf']).read_bytes()).hexdigest()
    assert source['extract_sha256']==hashlib.sha256(Path(source['literal_extract']).read_bytes()).hexdigest()
    assert len(PdfReader(p/'source-extracts'/source['retained_pdf']).pages)==len(source['actual_pdf_pages'])
    raw=Path(source['literal_extract']).read_bytes()
    for excerpt in source['literal_excerpts']:
        assert raw[excerpt['byte_start']:excerpt['byte_end']].decode()==excerpt['literal_text']
result=dict(input_bytes=len(current.read_bytes()),input_byte_identical=True,
    exact_status_keys=sorted(status),source_count=len(sources['sources']),
    selected_pdf_pages=sum(len(s['actual_pdf_pages']) for s in sources['sources']),
    paper_pdf_pages=len(PdfReader(p/'P02.2-paper.pdf').pages),
    two_tex_passes_succeeded=True,mathematical_validation=False,candidate=False)
(p/'artifact-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
