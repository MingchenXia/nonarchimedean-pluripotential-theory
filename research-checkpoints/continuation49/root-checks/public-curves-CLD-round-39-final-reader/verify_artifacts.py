#!/usr/bin/env python3
"""Verify only reproducibility artifacts, never mathematical correctness."""
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    inp=json.loads((R/'input.json').read_text())
    status=json.loads((R/'status.json').read_text())
    assert list(status)==['id','status','exact_result','proof_file','concrete_gaps']
    assert (R/'input.json').read_bytes()==(R/'input-original.json').read_bytes()
    assert (R/'assignment-original.txt').read_text()==inp['assignment']
    assert json.loads((R/'task-original.json').read_text())==inp['task']
    prov=json.loads((R/'source-extracts/source-provenance.json').read_text())
    n=0
    for src in prov['sources']:
        assert digest(Path(src['pdf']))==src['pdf_sha256']
        assert digest(Path(src['literal_extract']))==src['extract_sha256']
        pages=Path(src['literal_extract']).read_text().split('\f')
        for lit in src['literal_pages']:
            p=R/lit['file']; assert p.read_text()==pages[lit['pdf_page']-1]
            assert digest(p)==lit['sha256'];n+=1
    build=json.loads((R/'build-diagnostics.json').read_text())
    assert build['all_steps_succeeded'] and len(build['steps'])==3
    assert all(s['exit_code']==0 for s in build['steps'])
    tex=(R/'P03.2-paper.tex').read_text()
    assert '\\begin{document}' in tex and '\\end{document}' in tex
    for term in ['Theorem A','Theorem B','Theorem C','split-node','remains open','ordinary']:
        assert term in tex,term
    assert '\\input{P03.2-argument' not in tex
    report={'artifact_checks_passed':True,'sources':len(prov['sources']),'literal_pages':n,
            'tex_pass_exit_codes':[s['exit_code'] for s in build['steps'][1:]],
            'status_keys':list(status),'input_original_byte_identical':True,
            'standalone_tex_sha256':digest(R/'P03.2-paper.tex'),'argument_sha256':digest(R/'P03.2-argument.md'),
            'mathematical_certificate':False,'limitation':'Checks establish artifact consistency and compilation, not theorem correctness.'}
    (R/'artifact-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__':main()
