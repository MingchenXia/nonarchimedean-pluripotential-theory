from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys

ROOT = Path('/workspace/research/root-checks')
reader = ROOT / 'public-P16-round-48-final-reader-v3'
target = ROOT / 'public-P16-round-48-root-reproduction-v3'
assert not target.exists()
shutil.copytree(reader, target)
build = target / 'root-build'
build.mkdir()

def binding(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

provenance = json.loads((reader / 'source-extracts/source-provenance.json').read_text())
assert len(provenance['sources']) == 10
for entry in provenance['sources']:
    source = entry['supplied_pointer']
    for key, digest_key in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256'),
                            ('abstract_html', 'abstract_sha256')]:
        if source.get(key):
            assert binding(source[key])['sha256'] == source[digest_key]
commands = []

def run(label, argv):
    result = subprocess.run(argv, cwd=target, capture_output=True, text=True)
    (build / f'{label}.stdout.txt').write_text(result.stdout)
    (build / f'{label}.stderr.txt').write_text(result.stderr)
    commands.append({'label': label, 'argv': argv, 'cwd': str(target), 'returncode': result.returncode})
    assert result.returncode == 0, (label, result.stderr, result.stdout[-1000:])

run('author-source-audit', [sys.executable, 'audit_sources.py'])
# Only the already-read manuscript transformer is invoked; author main is not called.
spec = importlib.util.spec_from_file_location('frozen_P16_6_builder', target / 'build_artifacts.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.manuscript()
assert binding(target / 'P16.6-paper.tex') == binding(reader / 'P16.6-paper.tex')
for path in (reader / 'source-extracts').glob('*.txt'):
    assert binding(target / 'source-extracts' / path.name) == binding(path)

# Preserve the author's extraction scheme, and add explicitly LF-delimited excerpts.
# Python splitlines counts PDF form feeds; neither its numeric ranges nor LF ranges
# are interchangeable. This addendum does not amend the frozen author provenance.
extra = {
    '1201.0187': [(1648, 1766), (1774, 1845), (1900, 1955)],
    '1201.0188': [(700, 765), (1190, 1401), (1402, 1460), (1540, 1685)],
    '2307.01697': [(677, 753), (800, 839), (850, 923), (1020, 1047), (1055, 1134), (1127, 1245)],
}
addendum = target / 'root-LF-source-addendum'
addendum.mkdir()
units = []
mismatches = []
pieces = ['# Root LF source addendum\n\n',
          'Author files are unchanged. LF denotes the newline byte, with form feeds retained inside lines. '
          'The author helper uses Python splitlines, which additionally counts form feeds. '
          'These are different range conventions; the following bodies use an explicit LF convention. '
          'This is a source-location audit, not a mathematical verdict.\n']
for entry in provenance['sources']:
    source = Path(entry['supplied_pointer']['literal_extract'])
    raw = source.read_bytes()
    lines = raw.split(b'\n')
    ranges = set(extra.get(entry['key'], []))
    for old in entry['literal_published_extracts']:
        first, last = old['first_cached_line'], old['last_cached_line']
        ranges.add((first, last))
        body = b'\n'.join(lines[first - 1:last]) + b'\n'
        if body.decode('utf-8') != old['literal_text']:
            mismatches.append({'key': entry['key'], 'first': first, 'last': last,
                               'author_file': old['file'], 'author_sha256': old['sha256'],
                               'LF_sha256': hashlib.sha256(body).hexdigest()})
    for first, last in sorted(ranges):
        assert 1 <= first <= last <= len(lines)
        body = b'\n'.join(lines[first - 1:last]) + b'\n'
        name = f'{entry["key"]}-LF-{first}-{last}.txt'
        path = addendum / name
        path.write_bytes(body)
        unit = {'source_key': entry['key'], 'source': str(source), 'source_binding': binding(source),
                'first_LF_line': first, 'last_LF_line': last, 'file': str(path), **binding(path)}
        units.append(unit)
        pieces.extend([f'\n\n## {name}\n\n', body.decode('utf-8')])
(addendum / 'literal-source-addendum.txt').write_text(''.join(pieces), encoding='utf-8')
(addendum / 'manifest.json').write_text(json.dumps({
    'created_utc': datetime.now(timezone.utc).isoformat(), 'author_provenance': binding(reader / 'source-extracts/source-provenance.json'),
    'author_declared_unit_count': sum(len(e['literal_published_extracts']) for e in provenance['sources']),
    'LF_interpretation_different_count': len(mismatches), 'different_ranges': mismatches,
    'LF_units': units, 'aggregate': binding(addendum / 'literal-source-addendum.txt'),
    'root_whole_primary_papers_read': False, 'mathematical_verdict': None,
}, ensure_ascii=False, indent=2) + '\n')

for number in (1, 2):
    run(f'tex-pass-{number}', ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
        '-halt-on-error', '-file-line-error', '-output-directory=root-build', 'P16.6-paper.tex'])
    shutil.copyfile(build / 'P16.6-paper.log', build / f'tex-pass-{number}.log')
run('pdfinfo', ['pdfinfo', str(build / 'P16.6-paper.pdf')])
run('pdf-text', ['pdftotext', '-layout', str(build / 'P16.6-paper.pdf'), str(build / 'paper.txt')])
pages = int(next(line.split(':', 1)[1] for line in (build / 'pdfinfo.stdout.txt').read_text().split('\n') if line.startswith('Pages:')))
for page in (1, pages):
    run(f'preview-{page}', ['pdftoppm', '-f', str(page), '-l', str(page), '-scale-to', '1500',
        '-singlefile', '-png', str(build / 'P16.6-paper.pdf'), str(build / f'page-{page}')])
diagnostics = [line for line in (build / 'tex-pass-2.log').read_text().split('\n')
               if 'Warning' in line or 'Overfull' in line or 'Underfull' in line or line.startswith('!')]
result = {'created_utc': datetime.now(timezone.utc).isoformat(), 'round': 48,
    'author_reader': str(reader), 'fresh_reproduction': str(target), 'author_files_preserved': True,
    'all_ten_public_cache_hashes_match': True, 'regenerated_tex_byte_identical': True,
    'author_extracts_reproduced_byte_identically': True,
    'source_range_convention_addendum': str(addendum / 'manifest.json'),
    'LF_interpretation_different_count': len(mismatches), 'commands': commands,
    'final_tex_diagnostics': diagnostics, 'pages': pages,
    'pdf': {'path': str(build / 'P16.6-paper.pdf'), **binding(build / 'P16.6-paper.pdf')},
    'native_open_performed': False, 'native_compile_result': 'success',
    'current_user_editor_P16_4_preserved': True, 'mathematical_review_verdict': None,
    'original_atom_closed': False, 'evidence_limit': 'Identity and compilation do not certify mathematics.'}
(target / 'root-reproduction-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'round':48, 'pages':pages, 'pdf':result['pdf'], 'diagnostics':diagnostics,
                  'LF_different_count':len(mismatches), 'LF_unit_count':len(units)}))
