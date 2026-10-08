#!/usr/bin/env python3
"""Read only the two explicitly authorized binders and their exact paths."""
import hashlib
import json
from pathlib import Path

ROOT = Path('/workspace/research/campaigns/round-213/P05.2-original-all-obstacle-after-lossless-input-normalization')
OUT = Path(__file__).resolve().parent

def main():
    rows = []
    for binder in ['mathematical-packet-bindings.json', 'private-primary-packet-bindings.json']:
        for entry in json.loads((ROOT / binder).read_text()):
            p = Path(entry['path'])
            data = p.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            assert len(data) == entry['bytes'] and digest == entry['sha256'], p
            rows.append(dict(label=entry['label'], path=str(p), bytes=len(data), sha256=digest))
    (OUT / 'byte-bindings.json').write_text(json.dumps(rows, indent=2) + '\n')
    primary = json.loads((ROOT / 'private-primary-packet-bindings.json').read_text())
    # These original-source excerpts are long third-party text and remain LOCALONLY.
    units = {
        1: [(254, 301), (418, 638), (691, 852), (1000, 1030),
            (1354, 1503), (1741, 1746), (2259, 2353)],
        3: [(196, 250), (379, 420), (443, 716)]
    }
    local = OUT / 'LOCALONLY'
    local.mkdir(exist_ok=True)
    source_rows = []
    for index, ranges in units.items():
        p = Path(primary[index]['path'])
        lines = p.read_text().split('\n')  # LF line numbers; formfeeds do not increment them.
        blocks = []
        for a, b in ranges:
            blocks.append(f'LF {a}--{b}\n' + '\n'.join(lines[a-1:b]))
        target = local / (primary[index]['label'] + '-proof-units.txt')
        target.write_text('\n\n'.join(blocks) + '\n')
        source_rows.append(dict(source=str(p), target=str(target.relative_to(OUT)), ranges=ranges))
    (OUT / 'source-read-ranges.json').write_text(json.dumps(source_rows, indent=2) + '\n')
    # Byte comparison is evidence only; no hash is represented as proof-unit review.
    (OUT / 'packet-read-record.json').write_text(json.dumps({
        'all_22_packet_bodies_read': True,
        'method': 'Complete visible bounded local chunks during author reconstruction; repeat tails where a tool aggregate truncated.',
        'binding_count': len(rows),
        'grant_groups': ['A224', 'B225', 'R230', 'S262', 'S272'],
        'working_groups_not_grants': ['ROOT276', 'ROOT277', 'ROOT278', 'ROOT281'],
        'source_rule': 'Whole pertinent original proof units; not a claim to read every unrelated source theorem.',
        'native210_overall_evidence_verdict': 'INCONCLUSIVE',
        'execution_is_mathematical_acceptance': False
    }, indent=2) + '\n')
    print(json.dumps({'files_bound': len(rows), 'all_bindings_match': True,
                      'source_excerpt_policy': 'LOCALONLY', 'candidate': False}))

if __name__ == '__main__':
    main()
