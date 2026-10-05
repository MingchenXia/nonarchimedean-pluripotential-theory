"""Artifact checks, not mathematical verification."""
from pathlib import Path
import hashlib,json,re,sys,platform
root=Path.cwd()
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
raw=Path('input.json').read_bytes(); original=Path('input-original.json').read_bytes()
assert raw==original
text=raw.decode('utf-8'); obj=json.loads(text)
assert Path('assignment-original.txt').read_text()==obj['assignment']
match=re.search(r'"task"\s*:',text); assert match
start=match.end()
while text[start].isspace():start+=1
_,end=json.JSONDecoder().raw_decode(text,start)
assert Path('task-original.json').read_bytes()==text[start:end].encode()
assert json.loads(Path('task-original.json').read_text())==obj['task']
preserved=['input.json','input-original.json','assignment-original.txt','task-original.json']
Path('preservation.json').write_text(json.dumps({'input_sha256':digest('input.json'),'byte_identical':True,'assignment_verbatim':True,'task_literal_bytes':True,'files':[{'path':p,'bytes':Path(p).stat().st_size,'sha256':digest(p)} for p in preserved]},indent=2)+'\n')
status=json.loads(Path('status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id']=='P13.1' and status['status']=='complete_draft'
assert status['concrete_gaps']==[] and Path(status['proof_file']).is_file()
sources=json.loads(Path('sources.json').read_text()); audit=json.loads(Path('source-extracts/source-provenance.json').read_text())
assert len(sources)==len(audit['sources'])==11 and len(audit['excerpts'])==63
source_map={s['local_id']:s for s in sources}
for s in audit['sources']:
    assert s['version']==source_map[s['id']]['saved_version']
    for f in s['files']:
        assert f['matches'] is True and digest(f['path'])==f['sha256']==f['expected_sha256']
for e in audit['excerpts']:
    lines=Path(source_map[e['source']]['literal_extract']).read_text().split('\n')
    literal='\n'.join(lines[e['lf_start']-1:e['lf_end']])
    assert literal==e['literal_statement_and_proof_body']==Path(e['artifact']).read_text()
    assert hashlib.sha256(literal.encode()).hexdigest()==e['sha256']
checks=json.loads(Path('checks-output.json').read_text()); assert checks['checks_passed'] is True
build=json.loads(Path('build-report.json').read_text())
assert len(build['commands'])==4 and all(c['returncode']==0 for c in build['commands'])
assert build['input_preserved'] is True
for p,h in build['outputs_sha256'].items():assert digest(p)==h
for i in (1,2):
    log=Path(f'tex-pass-{i}.log').read_text()
    assert 'Output written on P13.1-paper.pdf' in log
    assert not re.search(r'^!',log,re.M)
    assert Path(f'tex-pass-{i}.stdout').exists() and Path(f'tex-pass-{i}.stderr').exists()
assert '\\documentclass' in Path('P13.1-paper.tex').read_text()
assert Path('P13.1-paper.pdf').read_bytes().startswith(b'%PDF')
notes=json.loads(Path('notes.json').read_text()); assert notes['candidate'] is True and len(notes['notes'])==4
seen=set()
for n in notes['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    assert n['id'] not in seen and all(x in seen for x in n['support'])
    assert all(n[key] for key in ('summary','detailedSummary','text'))
    seen.add(n['id'])
assert [n['id'] for n in notes['notes']]==['n1','n2','n3','n4']
assert 'complete draft solution of the unchanged original P13.1' in notes['notes'][-1]['text']
pages=int(re.search(r'^Pages:\s+(\d+)',Path('pdfinfo.stdout').read_text(),re.M).group(1))
assert f'({pages} pages)' in notes['notes'][-1]['text']
report={'artifact_checks_passed':True,'input_preservation':True,'source_count':11,'literal_excerpt_count':63,'status_schema_exact':True,'canonical_note_count':4,'candidate':True,'tex_passes_succeeded':2,'pdf_pages':pages,'finite_diagnostic_counts':checks['counts'],'source_hashes_verified':True,'proof_sha256':digest('P13.1-argument.md'),'notes_sha256':digest('notes.json'),'mathematical_scope':'Complete unverified draft claim; these checks establish artifact consistency and execution only. No correctness or novelty verdict.'}
Path('validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
