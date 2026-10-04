#!/usr/bin/env python3
"""Read immutable inputs, copy evidence, and extract by LF only. No network."""
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
RESEARCH = Path('/workspace/research')
OLD = RESEARCH / 'campaigns/round-04/P06.2-curve-recognition-submission-repair/artifacts/codex-bcowsD'
N701 = RESEARCH / 'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-continuation/artifacts/codex-ZwIWCf'
CAMPAIGN = ROOT.parent.parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def dump(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    for name in ('sources', 'evidence', 'build'):
        (ROOT / name).mkdir(exist_ok=True)
    incoming = json.loads((ROOT / 'input.json').read_text())
    dump('original-task.json', incoming['task'])
    (ROOT / 'original-problem.txt').write_text(incoming['task']['problem'])
    (ROOT / 'completion-criteria.txt').write_text(incoming['task']['completionCriteria'])
    (ROOT / 'assignment-verbatim.txt').write_text(incoming['assignment'])
    dump('sources/caller-notes.json', incoming['notes'])
    origins = {
        'sources/n700-argument.md': RESEARCH / 'deliverables/round-07/P06.2-curve-recognition-argument.md',
        'sources/n700-review.json': RESEARCH / 'deliverables/round-07/P06.2-curve-recognition-review.json',
        'sources/n701-argument.md': N701 / 'P06.2-argument.md',
        'sources/n701-review.json': RESEARCH / 'deliverables/round-22/P06.2-completed-algebraic-all-dimensional-transport-review.json',
        'sources/n701-published-review-wrapper.md': RESEARCH / 'deliverables/round-22/P06.2-completed-algebraic-all-dimensional-transport-argument.md',
        'sources/GR.txt': OLD / 'sources/GR.txt',
        'sources/GR.pdf': OLD / 'sources/GR.pdf',
        'sources/GR.provenance.json': OLD / 'sources/GR.provenance.json',
        'sources/GJR.txt': OLD / 'sources/GJR.txt',
        'sources/GJR.pdf': OLD / 'sources/GJR.pdf',
        'sources/GJR.provenance.json': OLD / 'sources/GJR.provenance.json',
        'sources/CLD.txt': N701 / 'sources/CLD-v2.txt',
        'sources/CLD.pdf': N701 / 'sources/CLD-v2.pdf',
        'sources/Thuillier.txt': RESEARCH / 'shared-sources/Thuillier-tel-00010990v1.txt',
        'sources/Thuillier.pdf': RESEARCH / 'shared-sources/Thuillier-tel-00010990v1.pdf',
        'sources/integration-evidence.md': RESEARCH / 'P06.2-arbitrary-field-curve-recognition-integration-evidence.md',
        'sources/integration-evidence-manifest.json': CAMPAIGN / 'integration-evidence-manifest.json',
    }
    for note, review_dir in [('n700', RESEARCH / 'campaigns/round-06/P06.2-curve-recognition-embedded-evidence-review'),
                             ('n701', RESEARCH / 'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-review')]:
        for f in ('freeze.json', 'source-artifact-binding.json', 'run.json'):
            origins[f'sources/{note}-{f}'] = review_dir / f
    manifest = []
    for target, origin in origins.items():
        data = origin.read_bytes()
        (ROOT / target).write_bytes(data)
        manifest.append(dict(artifact=target, read_only_origin=str(origin), bytes=len(data), sha256=digest(data)))
    dump('sources/manifest.json', manifest)
    expected = {
        'sources/n700-argument.md': '8c46bccc1c2dd4286d3ccfc42aea70698ef8e449b9e57f962d707ecffd953a04',
        'sources/n701-argument.md': 'e7c350a209fa4b40875fa15a65875d210c306919a089cdc7b8cf918c895dbd42',
        'sources/n701-published-review-wrapper.md': 'f1577176fe748c3ee6ddd18e3feae02221aba4d4ed60d7acaadb6f8dde93d7e6',
        'sources/GR.txt': '3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b',
        'sources/GR.pdf': '83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726',
        'sources/integration-evidence.md': 'c70e6107c260f8934a1cad91b5bf8bd85845e8730050b77337b53b86dd15bee4',
    }
    for p, value in expected.items():
        assert digest((ROOT / p).read_bytes()) == value, p
    im = json.loads((ROOT / 'sources/integration-evidence-manifest.json').read_text())
    selected = [(u['label'], 'GR.txt', u['first_lf_line'], u['last_lf_line'], u['body_sha256'])
                for u in im['selected_units']]
    selected += [
        ('GR field conventions', 'GR.txt', 175, 186, None),
        ('GR actual joint analytic fields and scalar spaces', 'GR.txt', 254, 273, None),
        ('GR relative boundaries and full Lemma 2.12', 'GR.txt', 302, 390, None),
        ('GR real PL convention', 'GR.txt', 416, 431, None),
        ('GR curves, subharmonic definition and Proposition 3.5', 'GR.txt', 453, 522, None),
        ('GR two signs and harmonic definition', 'GR.txt', 1042, 1061, None),
        ('GR classical pluriharmonic definition', 'GR.txt', 1831, 1836, None),
        ('GJR field convention', 'GJR.txt', 339, 343, None),
        ('GJR PL definition and domain conventions', 'GJR.txt', 1628, 1661, None),
        ('GJR harmonic definition and numerical triviality', 'GJR.txt', 2331, 2346, None),
        ('Thuillier harmonic scalar extension full proposition', 'Thuillier.txt', 3551, 3564, None),
        ('Thuillier subharmonic comparison definition', 'Thuillier.txt', 3783, 3788, None),
        ('Thuillier semistable harmonic scalar lemma, full proof', 'Thuillier.txt', 3297, 3310, None),
    ]
    units = []
    appendix = ['## Primary application evidence (exact LF extraction)\n',
                'These are immutable source passages. Formfeeds are retained in the authoritative Markdown; they are not line boundaries. Extraction errors are not silently corrected. GR 4.2(6), although present in the selected full unit, is not used for a finite-map converse in this integration.\n']
    for index, (label, source, first, last, bound) in enumerate(selected, 1):
        data = (ROOT / 'sources' / source).read_bytes()
        lines = data.split(b'\n')
        body = b'\n'.join(lines[first-1:last])
        # The operator manifest binds exactly the join, with no added final LF.
        if bound:
            assert digest(body) == bound, (label, digest(body), bound)
        artifact = f'sources/primary-{index:02d}.txt'
        (ROOT / artifact).write_bytes(body)
        unit = dict(label=label, source=source, first_lf_line=first, last_lf_line=last,
                    artifact=artifact, body_sha256=digest(body), first_line=lines[first-1].decode(),
                    last_line=lines[last-1].decode())
        units.append(unit)
        appendix += [f'\n### {label}\n\n{source}, LF {first}--{last}; SHA-256 `{digest(body)}`.\n\n```text\n',
                     body.decode(), '\n```\n']
    dump('sources/primary-units.json', units)
    (ROOT / 'sources/primary-bodies.md').write_text(''.join(appendix))
    for note in ('n700', 'n701'):
        r = json.loads((ROOT / f'sources/{note}-review.json').read_text())
        dump(f'evidence/{note}-review-mathematics.json', dict(
            precise_scope=r['precise_scope'], freeze=r['freeze'],
            source_artifact_binding=r['source_artifact_binding'],
            review_read_attestation=r['review_read_attestation'], result=r['result']))
    dump('evidence/preparation-checks.json', dict(bound_hashes=expected, selected_units=len(units),
        extraction='bytes.split(b"\\n"), inclusive 1-based LF intervals, no final LF added',
        no_network=True, copied_files=len(manifest), mathematical_verification=False))
    print(f'Bound {len(expected)} exact hashes; copied {len(manifest)} files; extracted {len(units)} complete selected units.')

if __name__ == '__main__':
    main()
