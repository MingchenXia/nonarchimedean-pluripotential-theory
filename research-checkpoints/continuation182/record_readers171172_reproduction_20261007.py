from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
out = []
for n, atom, worker, pages, expected in ((171, 'P16.4', 'codex-89WpBw', 12, '5501f07febccc59850c980f1183b5d954c55ba1b42bf631786ac2fb71ff30206'), (172, 'P14.4', 'codex-YpNB0s', 10, 'a6f7734f6ed598c6e89d6a689226f744a28fb7c4cef23494cb45500bbd12cc29')):
    C = next((R / f'campaigns/round-{n}').iterdir()); W = C / 'artifacts' / worker
    D = K / f'public-{atom}-round{n}-partial-reader'; T = D / f'{atom}-paper.tex'; P = D / f'{atom}-paper.pdf'
    assert sha(T) == sha(W / T.name) == expected
    assert int(subprocess.check_output(['pdfinfo', str(P)], text=True).split('Pages:')[1].split()[0]) == pages
    log = (D / f'{atom}-paper.log').read_text()
    assert not any(s in log for s in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
    for i in (1, 2):
        assert 'Output written on ' + P.name in (D / f'compile-pass{i}-LOCALONLY.txt').read_text()
    dest = D / 'root-reproduction-and-publication-binding-20261007.json'
    assert not dest.exists()
    j = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n, 'atom': atom, 'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(P), 'pdf_sha256': sha(P), 'pages': pages, 'source_lines': len(T.read_text().splitlines()), 'whole_standalone_source_and_all_native_note_fields_root_read': True, 'local_fresh_passes': 2, 'local_compile': 'SUCCESS', 'local_warnings': 0, 'local_overfull': 0, 'local_underfull': 0, 'local_undefined': 0, 'first_and_last_pdf_pages_visual_read': True, 'actual_visual_pages': [1, pages], 'all_pdf_pages_visual_read': False, 'native_compile': 'requested; result pending', 'independent_mathematical_acceptance': False, 'original_closed': False, 'source_ledger_sha256': sha(D / 'source-application-ledger.json'), 'kernel_canonical_author_result_exists': n == 171, 'protected_editor_unchanged': True, 'no_private_active_output_read': True, 'no_hot_feedback': True}
    dest.write_text(json.dumps(j, indent=2) + '\n'); out.append(j)
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(out, indent=2))
