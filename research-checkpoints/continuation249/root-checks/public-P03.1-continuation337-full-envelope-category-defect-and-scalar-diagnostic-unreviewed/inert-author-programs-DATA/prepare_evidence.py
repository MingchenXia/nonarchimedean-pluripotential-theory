"""Owned, bounded source retention. Reads data; never imports supplied programs."""
from pathlib import Path
import hashlib
import json
import platform
import shutil
import sys

ROOT = Path(__file__).resolve().parent
CAMPAIGN = Path('/workspace/research/campaigns/round-244/P03.1-original-normal-full-envelope-positivity-PDF-control-repair')
SOURCES = Path('/workspace/research/shared-sources')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')

def main():
    out = ROOT / 'input-bindings'
    out.mkdir(exist_ok=True)
    manifests = [('mathematical-packet-bindings.json', 9, 'mathematical-data'),
                 ('private-primary-packet-bindings.json', 10, 'primary')]
    records, total = [], 0
    for name, count, subdir in manifests:
        raw = (CAMPAIGN / name).read_bytes()
        (out / name).write_bytes(raw)
        entries = json.loads(raw)
        assert len(entries) == count
        dest = out / subdir
        dest.mkdir(exist_ok=True)
        for entry in entries:
            source = Path(entry['path'])
            permitted = (CAMPAIGN / 'immutable-mathematical-DATA') if subdir == 'mathematical-data' else SOURCES
            assert source.parent == permitted
            assert source.suffix in {'.tex', '.md', '.json', '.txt', '.pdf'}
            body = source.read_bytes()
            total += len(body)
            assert total <= 32 * 1024 * 1024
            assert len(body) == entry['bytes']
            assert digest(body) == entry['sha256']
            target = dest / source.name
            target.write_bytes(body)
            records.append({'source': str(source), 'retained': str(target.relative_to(ROOT)),
                            'bytes': len(body), 'sha256': digest(body),
                            'mathematical_correctness_grant': False})
    for name in ['original-task.json']:
        body = (CAMPAIGN / name).read_bytes()
        (out / name).write_bytes(body)
        records.append({'source': str(CAMPAIGN / name), 'retained': str((out / name).relative_to(ROOT)),
                        'bytes': len(body), 'sha256': digest(body), 'mathematical_correctness_grant': False})
    book = Path('/workspace/research/book-source/manuscript')
    inspected = [
        'editorial/solver_dossiers_20260912/p031_polydisc_ground_field_perron_v3_20260912/STATEMENT.tex',
        'editorial/solver_dossiers_20260912/p031_polydisc_ground_field_perron_v3_20260912/PROOF.tex',
        'editorial/solver_dossiers_20260925/p031_isolated_scalar_defect_v62_20260925/STATEMENT_LIVE.tex',
        'editorial/solver_dossiers_20260925/p031_isolated_scalar_defect_v62_20260925/PROOF_LIVE.tex',
    ]
    for rel in inspected:
        source = book / rel
        body = source.read_bytes()
        assert len(body) <= 64 * 1024
        target = out / 'inspected-book-data' / source.parent.name / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        records.append({'source': str(source), 'retained': str(target.relative_to(ROOT)),
                        'bytes': len(body), 'sha256': digest(body),
                        'mathematical_correctness_grant': False,
                        'use': 'Inspected data, not a proof dependency of the retained new results.'})
    body = (ROOT / 'input.json').read_bytes()
    (out / 'session-input.json').write_bytes(body)
    records.append({'source': 'input.json', 'retained': 'input-bindings/session-input.json',
                    'bytes': len(body), 'sha256': digest(body), 'mathematical_correctness_grant': False})
    # Exact text bodies, including complete immediate proofs where printed.
    specs = [
        ('GR1-definitions', 'GR-2506.13548v2-20261004.txt', 483, 536),
        ('GR1-classical-and-PL', 'GR-2506.13548v2-20261004.txt', 1107, 1201),
        ('GR1-affinoid-and-limit', 'GR-2506.13548v2-20261004.txt', 1785, 1831),
        ('GR1-boundary-convention', 'GR-2506.13548v2-20261004.txt', 299, 396),
        ('GJR-PL', 'GJR-2111.05741.txt', 1640, 1698),
        ('GJR-nef', 'GJR-2111.05741.txt', 2279, 2340),
        ('GJR-pullback-and-LFS', 'GJR-2111.05741.txt', 2385, 2454),
        ('GR2-curve-PL-proof', 'GR-2503.05513-20261004.txt', 802, 843),
        ('Thu-comparison-and-local-maximum', 'Thuillier-tel-00010990v1.txt', 3783, 3898),
    ]
    extracts = ROOT / 'source-extracts'
    extracts.mkdir(exist_ok=True)
    extracted = []
    for label, name, first, last in specs:
        source = out / 'primary' / name
        # splitlines() treats PDF form-feed controls as line separators;
        # the recorded ranges instead use literal LF lines, as sed/nl do.
        lines = source.read_bytes().split(b'\n')
        body = b'\n'.join(lines[first-1:last]) + b'\n'
        target = extracts / (label + '.txt')
        target.write_bytes(body)
        extracted.append({'id': label, 'source': str(source.relative_to(ROOT)),
                          'first_line': first, 'last_line': last,
                          'retained': str(target.relative_to(ROOT)), 'sha256': digest(body),
                          'method': 'literal text-line slice; complete primary PDFs also retained'})
    dump(ROOT / 'input-bindings.json', {'records': records, 'bounded_packet_bytes': total,
                                      'bound_bytes': 32 * 1024 * 1024, 'extracts': extracted})
    dump(ROOT / 'environment.json', {'python': sys.version, 'platform': platform.platform(),
                                    'tex_engine_path': shutil.which('pdflatex'),
                                    'third_party_python_packages': [],
                                    'supplied_programs_executed_or_imported': False,
                                    'resource_heavy_work': False,
                                    'supervised_compute': 'Not needed for these bounded operations; no heavy job launched.',
                                    'external_editor_actions': [], 'agents_spawned': 0,
                                    'requested_native_model': 'gpt-6.1-sol', 'requested_reasoning': 'xhigh',
                                    'runtime_model_independently_verified': False})
    print(json.dumps({'matched_mathematical_files': 9, 'matched_primary_files': 10,
                      'bounded_packet_bytes': total, 'literal_excerpts': len(extracted)}))

if __name__ == '__main__':
    main()
