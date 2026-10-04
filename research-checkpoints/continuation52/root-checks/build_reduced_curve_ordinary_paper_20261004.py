from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess

R = Path('/workspace/research')
d = R / 'root-checks/P02.4-reduced-curve-ordinary-paper-20261004'
tex = d / 'P02.4-reduced-curve-ordinary-paper.tex'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(tex) == 'b433f1288f19689ffe6c3649bade5b9cfb70bbaa9bf6e2bfc904499539328ea3'
assert sha(d / 'preparation-binding.json') == 'e2ace7c4f235bdf699c87712c7992604d10867a19e485f9ffa59a4fcebc1eef3'
assert not (d / 'native-editor-result.json').exists()
native = {'requested_utc': '2026-10-04 15:16:49 UTC', 'exec_cell': '1804',
    'path': str(tex), 'source_sha256': sha(tex),
    'open_result': {'status': 'queued', 'threadId': '01a100b0-99da-770b-a765-a51e5c89404d'},
    'compile_result': {'path': str(tex), 'kind': 'success',
        'message': "The current source compiled successfully with the desktop editor's compiler."},
    'editor_open_verified': False, 'editor_close_requested': False,
    'compiler_confirmed_success': True, 'exported_pdf_returned': False}
(d / 'native-editor-result.json').write_text(json.dumps(native, indent=2) + '\n')
out = d / 'local-pdf'
out.mkdir(exist_ok=False)
copied = out / tex.name
shutil.copyfile(tex, copied)
assert copied.read_bytes() == tex.read_bytes()
commands = []
for pass_number in (1, 2):
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex.name]
    run = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    (out / f'pdflatex-pass-{pass_number}.stdout').write_text(run.stdout)
    (out / f'pdflatex-pass-{pass_number}.stderr').write_text(run.stderr)
    log = out / (tex.stem + '.log')
    if log.exists(): shutil.copyfile(log, out / f'pdflatex-pass-{pass_number}.log')
    warnings = [s for s in run.stdout.split('\n') if re.search(r'Warning|Overfull|Underfull|^!', s)]
    commands.append({'pass': pass_number, 'command': cmd, 'returncode': run.returncode, 'warnings': warnings})
    assert run.returncode == 0, run.stdout[-3000:]
pdf = out / (tex.stem + '.pdf')
text_file = out / (tex.stem + '.pdf.txt')
extract = subprocess.run(['pdftotext', '-layout', str(pdf), str(text_file)], capture_output=True, text=True)
assert extract.returncode == 0, extract.stderr
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True)
assert info.returncode == 0, info.stderr
(out / 'pdfinfo.txt').write_text(info.stdout)
pages = int(re.search(r'^Pages:\s+(\d+)', info.stdout, re.M).group(1))
def bind(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
result = {'built_utc': datetime.now(timezone.utc).isoformat(),
    'root_full_tex_read': {'LF': [1,508], 'all_mathematics_read': True},
    'native_compilation': bind(d / 'native-editor-result.json'),
    'native_open_state': 'Queued; actual editor opening is not independently observed.',
    'native_compile_success': True, 'standalone_source': bind(tex),
    'local_pdf_export_purpose': 'Produce a standalone downloadable PDF; native compilation returns diagnostics without an exported PDF.',
    'local_source_byte_equal_to_native_compiled_source': True,
    'commands': commands, 'pdf': bind(pdf), 'pdf_pages': pages,
    'pdftotext_returncode': extract.returncode, 'pdf_text': bind(text_file),
    'pdf_visual_inspection': 'Not yet performed.',
    'mathematical_independent_acceptance': False, 'original_atoms_closed': [],
    'hot_feedback_sent': False, 'external_export_attempted': False}
(d / 'build-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'pdf': bind(pdf), 'pages': pages, 'passes': commands,
    'native_compile_success': True, 'build_result': bind(d / 'build-result.json')}, indent=2))
