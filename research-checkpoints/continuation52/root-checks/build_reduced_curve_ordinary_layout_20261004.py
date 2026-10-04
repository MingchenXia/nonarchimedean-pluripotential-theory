from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess

d = Path('/workspace/research/root-checks/P02.4-reduced-curve-ordinary-paper-20261004')
tex = d / 'P02.4-reduced-curve-ordinary-paper-layout.tex'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(tex) == 'c5aeeee3b18360e99a8e5fb655f32c91863b0b09d10fcc0193723684ea1eb6e1'
original = d / 'P02.4-reduced-curve-ordinary-paper.tex'
assert sha(original) == 'b433f1288f19689ffe6c3649bade5b9cfb70bbaa9bf6e2bfc904499539328ea3'
layout = json.loads((d / 'layout-only-successor.json').read_text())
reconstructed = original.read_text()
for c in layout['exact_changes']:
    assert reconstructed.count(c['old']) == 1
    reconstructed = reconstructed.replace(c['old'], c['new'])
assert reconstructed == tex.read_text()
native_path = d / 'native-editor-layout-result.json'
assert not native_path.exists()
native_path.write_text(json.dumps({'requested_utc': '2026-10-04 15:19:33 UTC',
    'exec_cell': '1809', 'path': str(tex), 'source_sha256': sha(tex),
    'open_result': {'status': 'queued', 'threadId': '01a100b0-99da-770b-a765-a51e5c89404d'},
    'compile_result': {'path': str(tex), 'kind': 'success',
        'message': "The current source compiled successfully with the desktop editor's compiler."},
    'editor_open_verified': False, 'editor_close_requested': False,
    'compiler_confirmed_success': True, 'exported_pdf_returned': False}, indent=2) + '\n')
out = d / 'local-pdf-layout'
out.mkdir(exist_ok=False)
shutil.copyfile(tex, out / tex.name)
assert (out / tex.name).read_bytes() == tex.read_bytes()
commands = []
for n in (1, 2):
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex.name]
    run = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    (out / f'pdflatex-pass-{n}.stdout').write_text(run.stdout)
    (out / f'pdflatex-pass-{n}.stderr').write_text(run.stderr)
    log = out / (tex.stem + '.log')
    if log.exists(): shutil.copyfile(log, out / f'pdflatex-pass-{n}.log')
    warnings = [s for s in run.stdout.split('\n') if re.search(r'Warning|Overfull|Underfull|^!', s)]
    commands.append({'pass': n, 'command': cmd, 'returncode': run.returncode, 'warnings': warnings})
    assert run.returncode == 0, run.stdout[-3000:]
pdf = out / (tex.stem + '.pdf')
text_file = out / (tex.stem + '.pdf.txt')
extract = subprocess.run(['pdftotext', '-layout', str(pdf), str(text_file)], capture_output=True, text=True)
assert extract.returncode == 0, extract.stderr
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True)
assert info.returncode == 0, info.stderr
(out / 'pdfinfo.txt').write_text(info.stdout)
pages = int(re.search(r'^Pages:\s+(\d+)', info.stdout, re.M).group(1))
preview_commands = []
for n, name in ((1, 'first-page'), (pages, 'last-page')):
    cmd = ['pdftoppm', '-f', str(n), '-l', str(n), '-singlefile', '-scale-to', '1500', '-png', str(pdf), str(out / name)]
    run = subprocess.run(cmd, capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    preview_commands.append({'command': cmd, 'returncode': run.returncode})
def bind(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
result = {'built_utc': datetime.now(timezone.utc).isoformat(),
    'root_source_read': 'Original LF1-508 fully read; all five exact reference-layout replacements read and byte-reconstructed. No mathematical change.',
    'native_compilation': bind(native_path), 'native_compile_success': True,
    'native_open_state': 'Queued; actual editor opening is not independently observed.',
    'standalone_source': bind(tex), 'layout_provenance': bind(d / 'layout-only-successor.json'),
    'local_pdf_export_purpose': 'Produce a standalone downloadable PDF after native success; native compiler exports no PDF.',
    'local_source_byte_equal_to_native_compiled_source': True,
    'commands': commands, 'pdf': bind(pdf), 'pdf_pages': pages,
    'pdf_text': bind(text_file), 'pdftotext_returncode': extract.returncode,
    'preview_commands': preview_commands, 'pdf_visual_inspection': 'Not yet performed.',
    'mathematical_independent_acceptance': False, 'original_atoms_closed': [],
    'hot_feedback_sent': False, 'external_export_attempted': False}
(d / 'build-layout-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'pdf': bind(pdf), 'pages': pages, 'passes': commands,
    'build_result': bind(d / 'build-layout-result.json')}, indent=2))
