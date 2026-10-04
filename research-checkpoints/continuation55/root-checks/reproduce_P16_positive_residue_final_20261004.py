from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path('/workspace/research/root-checks')
reader = ROOT / 'public-P16-round-47-final-reader-v2'
target = ROOT / 'public-P16-round-47-root-reproduction-v2'
assert not target.exists()
shutil.copytree(reader, target)
build = target / 'root-build'
build.mkdir()

def binding(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

provenance = json.loads((reader / 'source-extracts/source-provenance.json').read_text())
sources = [record['supplied'] for record in provenance['sources']]
assert len(sources) == 10
for source in sources:
    for name, digest_name in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256'),
                              ('abstract_html', 'abstract_sha256')]:
        if name in source:
            assert binding(source[name])['sha256'] == source[digest_name]
records = []

def run(label, argv):
    result = subprocess.run(argv, cwd=target, capture_output=True, text=True)
    (build / f'{label}.stdout.txt').write_text(result.stdout)
    (build / f'{label}.stderr.txt').write_text(result.stderr)
    records.append({'label': label, 'argv': argv, 'cwd': str(target), 'returncode': result.returncode})
    assert result.returncode == 0, (label, result.stderr, result.stdout[-1000:])

run('source-audit', [sys.executable, 'source_audit.py'])
run('make-paper', ['pandoc', 'P16.3-argument.md', '--from=markdown+tex_math_dollars',
                  '--to=latex', '--standalone', '--variable=colorlinks:true',
                  '--variable=linkcolor:blue', '--output=P16.3-paper.tex'])
tex = 'P16.3-paper.tex'
assert binding(target / tex) == binding(reader / tex)
for path in (reader / 'source-extracts').glob('*.txt'):
    assert binding(target / 'source-extracts' / path.name) == binding(path)
for pass_number in (1, 2):
    run(f'tex-pass-{pass_number}', ['pdflatex', '-no-shell-escape',
        '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
        '-output-directory=root-build', tex])
    shutil.copyfile(build / 'P16.3-paper.log', build / f'tex-pass-{pass_number}.log')
run('pdfinfo', ['pdfinfo', str(build / 'P16.3-paper.pdf')])
run('pdf-text', ['pdftotext', '-layout', str(build / 'P16.3-paper.pdf'), str(build / 'paper.txt')])
info = (build / 'pdfinfo.stdout.txt').read_text()
pages = int(next(line.split(':', 1)[1] for line in info.split('\n') if line.startswith('Pages:')))
for page_number in (1, pages):
    run(f'preview-{page_number}', ['pdftoppm', '-f', str(page_number), '-l', str(page_number),
        '-scale-to', '1500', '-singlefile', '-png', str(build / 'P16.3-paper.pdf'),
        str(build / f'page-{page_number}')])
final_log = (build / 'tex-pass-2.log').read_text()
diagnostics = [line for line in final_log.split('\n')
               if 'Warning' in line or 'Overfull' in line or 'Underfull' in line or line.startswith('!')]
result = {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'round': 47,
    'author_reader': str(reader), 'fresh_reproduction': str(target),
    'author_sources_preserved': True, 'all_ten_public_cache_hashes_match': True,
    'regenerated_tex_byte_identical': True, 'literal_extracts_byte_identical': True,
    'commands': records, 'final_tex_diagnostics': diagnostics, 'pages': pages,
    'pdf': {'path': str(build / 'P16.3-paper.pdf'), **binding(build / 'P16.3-paper.pdf')},
    'native_open_performed': False, 'native_compiler_result': 'success',
    'current_user_editor_P16_4_preserved': True,
    'mathematical_review_verdict': None, 'original_atom_closed': False,
    'evidence_limit': 'Reproduction and compilation do not certify the mathematical theorem.',
}
(target / 'root-reproduction-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'round': 47, 'pages': pages, 'pdf': result['pdf'], 'diagnostics': diagnostics}))
