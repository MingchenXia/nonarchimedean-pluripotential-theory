from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, shutil

R = Path('/workspace/research'); K = R / 'root-checks'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for n, atom in [(131, 'P19.1'), (132, 'P16.5')]:
    inspection = json.loads((K / f'{atom}-round{n}-completed-native-inspection-LOCALONLY.json').read_text())
    assert inspection['campaign']['status'] == 'completed'
    assert inspection['campaign']['result']['candidate'] is False
    W = Path(inspection['campaign']['result']['workspace'])
    D = K / f'public-{atom}-round{n}-partial-research-reader'
    D.mkdir(exist_ok=True)
    assert not (D / 'publication-binding.json').exists()
    names = [atom + '-argument.md', atom + '-paper.tex', atom + '-paper.pdf',
             'status.json', 'source-application-ledger.json']
    for name in names:
        if (D / name).exists():
            assert sha(D / name) == sha(W / name)
        else:
            shutil.copyfile(W / name, D / name)
    status = json.loads((D / 'status.json').read_text())
    assert status['status'] == 'PARTIAL'
    logpath = W / 'build/P19.1-paper.log' if n == 131 else W / 'P16.5-paper.log'
    log = logpath.read_text()
    assert not any(s in log for s in ['Overfull', 'undefined', 'Warning', '! LaTeX Error'])
    pdf = D / (atom + '-paper.pdf')
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
    pages = int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
    binding = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n,
               'native_workspace': str(W), 'status': status, 'candidate': False,
               'independent_review': False, 'original_closed': False, 'accepted_count_change': 0,
               'whole_mathematical_markdown_root_read': True,
               'whole_generated_tex_separately_root_read': False,
               'whole_source_application_ledger_root_read': True,
               'native_two_pass_compile_reported': True,
               'root_observed_final_log': {'path': str(logpath), 'sha256': sha(logpath),
                                           'overfull': log.count('Overfull'),
                                           'undefined': log.count('undefined'), 'warnings': log.count('Warning')},
               'pages': pages, 'actual_visual_pages': [],
               'native_editor_compile_success_observed': False, 'existing_editor_unchanged': True,
               'files': [{'name': name, 'bytes': (D / name).stat().st_size, 'sha256': sha(D / name)} for name in names]}
    (D / 'publication-binding.json').write_text(json.dumps(binding, ensure_ascii=False, indent=2) + '\n')
    for page in [1, (pages + 1) // 2, pages]:
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', '90', '-png',
                        '-singlefile', str(pdf), str(D / f'page-{page}')], capture_output=True, check=True)
    print(json.dumps({'directory': str(D), 'pages': pages, 'pdf_sha256': sha(pdf)}, indent=2))
