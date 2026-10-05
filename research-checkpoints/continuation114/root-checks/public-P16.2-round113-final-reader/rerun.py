#!/usr/bin/env python3
"""Reproduce local evidence, light diagnostics and the standalone documents.

This script neither downloads mathematics nor accesses historical worker paths.
Successful execution is a document/provenance check, not a proof certificate.
"""
import datetime
import hashlib
import json
import pathlib
import platform
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
LOGS = ROOT/'logs'
COMMANDS = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')


def run(label, argv, destination=None):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result=subprocess.run(argv, cwd=ROOT, capture_output=True)
    (LOGS/(label+'.stdout')).write_bytes(result.stdout)
    (LOGS/(label+'.stderr')).write_bytes(result.stderr)
    if destination is not None and result.returncode == 0:
        (ROOT/destination).write_bytes(result.stdout)
    COMMANDS.append({'label':label,'argv':argv,'cwd':str(ROOT),'started_utc':started,
                     'returncode':result.returncode,'stdout':'logs/'+label+'.stdout',
                     'stderr':'logs/'+label+'.stderr'})
    write_json(ROOT/'commands.json',COMMANDS)
    if result.returncode:
        raise RuntimeError(f'{label} failed ({result.returncode}); inspect logs/{label}.stderr and .stdout')
    return result


def verify():
    original=json.loads((ROOT/'input.json').read_text())
    assert original['notes'] == []
    assert (ROOT/'evidence/assignment.txt').read_text() == original['assignment']
    assert json.loads((ROOT/'evidence/task.json').read_text()) == original['task']
    packets=json.loads((ROOT/'evidence/packet-index.json').read_text())
    for p in packets:
        start,end=p['assignment_characters']
        payload=original['assignment'][start:end]
        assert (ROOT/p['file']).read_text() == payload
        assert sha(ROOT/p['file']) == p['sha256']
    units=json.loads((ROOT/'evidence/units-index.json').read_text())
    assert len(packets) == 18 and len(units) == 124
    for u in units:
        assert sha(ROOT/u['file']) == u['sha256']
    by_id={u['id']:u for u in units}
    premises=json.loads((ROOT/'external-premises.json').read_text())
    assert [p['index'] for p in premises] == list(range(len(premises)))
    for p in premises:
        for unit in p['literal_evidence']:
            file=ROOT/unit['file']
            assert sha(file) == unit['sha256']
            assert unit['local_inclusive_one_based_LF'] == [1,len(file.read_text().splitlines())]
            if 'unit_id' in unit:
                assert by_id[unit['unit_id']]['file'] == unit['file']
        assert p['historical_paths_opened'] is False
        assert p['whole_primary_work_read'] is False
        assert p['all_recursively_cited_proofs_read'] is False
    status=json.loads((ROOT/'status.json').read_text())
    assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
    assert status['id'] == 'P16.2' and status['concrete_gaps']
    assert (ROOT/status['proof_file']).exists()
    note_result=json.loads((ROOT/'notes.json').read_text())
    assert note_result['candidate'] is False
    seen=set()
    assert 1 <= len(note_result['notes']) <= 4
    for i,note in enumerate(note_result['notes'],1):
        assert set(note) == {'id','summary','detailedSummary','text','support'}
        assert note['id'] == f'n{i}'
        assert note['id'] not in seen
        assert set(note['support']) <= seen
        assert all(isinstance(note[k],str) and note[k] for k in ['summary','detailedSummary','text'])
        seen.add(note['id'])
    return {'supplied_packet_blocks':len(packets),'literal_primary_units':len(units),
            'external_premises':len(premises),'canonical_notes':len(seen),
            'candidate':False,'status_exact_schema':True,
            'meaning':'Evidence and document structure checks only; no mathematical certification.'}


def main():
    LOGS.mkdir(exist_ok=True)
    binding=json.loads((ROOT/'input-binding.json').read_text())
    assert sha(ROOT/'input.json') == binding['sha256'], 'Immutable supplied input changed'
    paths={name:shutil.which(name) for name in ['pandoc','xelatex','pdftotext','pdfinfo']}
    assert all(paths.values()), f'Missing existing tool: {paths}; do not install automatically'
    versions={}
    for tool in ['pandoc','xelatex']:
        result=run('version-'+tool,[paths[tool],'--version'])
        versions[tool]=result.stdout.decode(errors='replace').splitlines()[0]
    write_json(ROOT/'environment.json',{
        'python_version':sys.version,'python_executable':sys.executable,
        'platform':platform.platform(),'machine':platform.machine(),
        'cwd':str(ROOT),'existing_tool_paths':paths,'versions':versions,
        'computation':'Small exact rational grid only; no heavy computation.',
        'external_access':'No new network requests in this rerun; retained public responses only.',
        'configuration_files_read':False,'other_worker_paths_read':False,
        'limitations':'No whole-source or recursive-proof audit is implied by these executable checks.',
    })
    run('extract-packet',[sys.executable,'extract_packet.py'])
    run('preserve-units',[sys.executable,'preserve_units.py'])
    run('make-deliverables',[sys.executable,'make_deliverables.py'])
    result=verify()
    write_json(ROOT/'verification.json',result)
    run('diagnostics',[sys.executable,'diagnostics.py'],'diagnostics-output.json')
    run('pandoc',[paths['pandoc'],'P16.2-paper.md','--standalone',
                  '--from=markdown+tex_math_dollars','--to=latex','--output=P16.2-paper.tex'])
    for i in [1,2]:
        run('xelatex-pass-'+str(i),[paths['xelatex'],'-interaction=nonstopmode',
                                    '-halt-on-error','-file-line-error','P16.2-paper.tex'])
    run('pdf-text',[paths['pdftotext'],'-layout','P16.2-paper.pdf','P16.2-paper.pdf.txt'])
    info=run('pdf-info',[paths['pdfinfo'],'P16.2-paper.pdf'])
    result['document_build']={'tex_exists':(ROOT/'P16.2-paper.tex').exists(),
                              'pdf_exists':(ROOT/'P16.2-paper.pdf').exists(),
                              'pdf_info_log':'logs/pdf-info.stdout',
                              'pass_count':2,'mathematical_certification':False}
    result['diagnostic_cases']=json.loads((ROOT/'diagnostics-output.json').read_text())['homogeneous_projection']['cases']
    write_json(ROOT/'verification.json',result)
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p.name != 'artifact-manifest.json':
            files.append({'file':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
    write_json(ROOT/'artifact-manifest.json',{
        'kind':'Artifact byte manifest, not a mathematical certificate.',
        'files':files,
    })
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
