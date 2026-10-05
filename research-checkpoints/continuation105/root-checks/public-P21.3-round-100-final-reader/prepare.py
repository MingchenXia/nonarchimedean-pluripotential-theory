#!/usr/bin/env python3
"""Prepare evidence and metadata from frozen inputs; no network or installs."""
import hashlib
import json
import pathlib
import platform
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(name, obj):
    (ROOT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def main():
    original = json.loads((ROOT / 'input-original.json').read_text())
    assert json.loads((ROOT / 'task-original.json').read_text()) == original['task']
    assert (ROOT / 'assignment-original.txt').read_text() == original['assignment']
    manifest = json.loads((ROOT / 'source-manifest.json').read_text())
    source = (ROOT / manifest['source']['path']).read_bytes()
    assert sha(source) == manifest['source']['sha256']
    lines = source.decode().split('\n')
    # Tighten two diagnostic intervals to their complete pertinent proof bodies.
    intervals = {'mixed-symmetry-diagnostic': (10470, 10481),
                 'bt-definition-and-closures': (10347, 10408),
                 'torus-coordinates': (16493, 16575)}
    for unit in manifest['units']:
        if unit['id'] in intervals:
            lo, hi = intervals[unit['id']]
            unit['inclusive_one_based_LF'] = [lo, hi]
            b = ('\n'.join(lines[lo-1:hi]) + '\n').encode()
            (ROOT / unit['path']).write_bytes(b)
            unit['sha256'] = sha(b)
    bound_path = ROOT / 'sources/cld-weak-multiplier-bound.txt'
    bound_bytes = bound_path.read_bytes()
    assert sha(bound_bytes) == '0448ea1b480496814c9d81b4a5443f7d6efbb05b91582305b117704008184860'
    normalized = (ROOT / 'sources/cld-weak-multiplier.txt').read_bytes()
    assert normalized == bound_bytes + b'\n'
    manifest['bound_primary_units'] = [{
        'path': 'sources/cld-weak-multiplier-bound.txt',
        'read_only_origin': '/workspace/research/campaigns/round-100/'
            'P21.3-original-mixed-symmetry-and-arbitrary-current-research/'
            'CLD-weak-multiplier-LF10257-10281.txt',
        'sha256': sha(bound_bytes),
        'inclusive_one_based_LF': [10257, 10281],
        'normalization_difference': 'The ordinary LF slice adds exactly one trailing newline.',
    }]
    dump('source-manifest.json', manifest)
    core = (ROOT / 'P21.3-core.md').read_text()
    mapping = {
        0: ['ordinary-domain', 'analytic-calculus', 'cutoffs-density'],
        1: ['generated-psh', 'generated-cpsh-diagnostic'],
        2: ['positive-decomposition', 'middle-positivity', 'positive-wedges',
            'face-positive-wedges', 'geometric-positive-wedges'],
        3: ['positive-scalar-measures', 'ordinary-product'],
        4: ['middle-matrix', 'face-positivity', 'current-topology',
            'compact-moment-image', 'chart-images'],
        5: ['form-leibniz', 'current-sheaf', 'current-differentials',
            'smooth-multiplier'],
        6: ['analytic-calculus', 'current-differentials', 'generic-lengths',
            'top-measures'],
        7: ['weak-multiplier'],
        8: ['torus-coordinates'],
    }
    units = {u['id']: u for u in manifest['units']}
    premises = []
    for i in range(9):
        pattern = rf'\*\*P{i}:.*?(?=\n\n\*\*P\d:|\n\n# Middle-positive)'
        matched = re.search(pattern, core, flags=re.S)
        assert matched, i
        premises.append({'id': f'P{i}', 'exact_statement_and_applicability': matched[0],
                         'source_version': 'CLD arXiv:1204.6277v2, 25 July 2025',
                         'primary_url': 'https://arxiv.org/pdf/1204.6277v2',
                         'evidence': [units[key] for key in mapping[i]]})
    dump('premises.json', premises)
    evidence = [
        '# Literal selected primary evidence\n',
        'Primary version: CLD arXiv:1204.6277v2, 25 July 2025. '
        'The frozen full text SHA256 is `' + manifest['source']['sha256'] + '`.\n',
        'The full primary was copied, not read in full. LF coordinates are one-based, '
        'inclusive, using UTF8 decoding followed by split("\\n"). '
        'Each unit is a literal source slice with one trailing newline. '
        'The extracted text contains PDF line-wrap and typography artifacts. '
        'Hashes identify bytes and are not mathematical acceptance.\n',
        'The explicitly bound raw weak-multiplier unit is preserved separately in '
        '`sources/cld-weak-multiplier-bound.txt`, SHA256 '
        '`0448ea1b480496814c9d81b4a5443f7d6efbb05b91582305b117704008184860`. '
        'It equals the selected LF text without the one added trailing newline.\n',
    ]
    for unit in manifest['units']:
        lo, hi = unit['inclusive_one_based_LF']
        body = (ROOT / unit['path']).read_text()
        assert sha(body.encode()) == unit['sha256']
        assert body == '\n'.join(lines[lo-1:hi]) + '\n'
        evidence += [f"## {unit['id']}\n",
                     f"Primary: <{unit['url']}>. LF {lo}–{hi}; "
                     f"unit SHA256 `{unit['sha256']}`.\n",
                     '```text\n' + body + '```\n']
    evidence_text = '\n'.join(evidence)
    (ROOT / 'P21.3-primary-evidence.md').write_text(evidence_text)
    (ROOT / 'P21.3-argument.md').write_text(core + '\n\n' + evidence_text)
    draft_records = []
    for marker, filename in [
        ('UNREVIEWED completed95', 'sources/supplied95-draft.txt'),
        ('UNREVIEWED new103', 'sources/supplied103-draft.txt'),
    ]:
        start = original['assignment'].index('BEGIN MATHEMATICAL DATA: ' + marker)
        end = original['assignment'].index('\nEND MATHEMATICAL DATA', start)
        body = original['assignment'][start:end] + '\n'
        (ROOT / filename).write_text(body)
        draft_records.append({'path': filename, 'sha256': sha(body.encode()),
                              'origin': 'literal extraction from supplied assignment',
                              'role': 'unreviewed diagnostic proposal, not granted proof'})
    dump('reading-record.json', {
        'complete_primary_read': False,
        'read_only_primary_origin': manifest['source']['read_only_origin'],
        'source_mutations': False,
        'pertinent_reading': 'Selected primary statements/proofs, including all of '
                            '8.5.1, 8.5.3–5 and 8.7.4, and the supplied literal '
                            'calculus packet. No recursive proof audit claimed.',
        'supplied_proposals': draft_records,
        'independent_review': False,
        'other_workers_or_models': False,
        'public_network_acquisition': False,
    })
    versions = {}
    for command in ['pandoc', 'pdflatex', 'pdfinfo']:
        executable = shutil.which(command)
        if executable:
            flag = '-v' if command == 'pdfinfo' else '--version'
            r = subprocess.run([executable, flag], capture_output=True, text=True)
            versions[command] = {'path': executable,
                                 'version': (r.stdout + r.stderr).splitlines()[0]}
    dump('environment.json', {
        'cwd': str(ROOT), 'python': sys.version, 'python_executable': sys.executable,
        'platform': platform.platform(), 'tools': versions,
        'network_used': False, 'installations': False,
        'supervised_heavy_compute': 'No operator-provided service supplied; not needed.',
        'resource_heavy_work_launched': False,
    })
    print('Prepared 9 exact premise records, literal primary evidence, and standalone argument.')
    print('Frozen primary SHA256:', manifest['source']['sha256'])


if __name__ == '__main__':
    main()
