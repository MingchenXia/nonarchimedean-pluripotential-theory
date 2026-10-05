"""Bind selected primary bodies to the unreviewed divisor-reference construction."""
from pathlib import Path
import hashlib
import json

R = Path('/workspace/research')
S = R / 'root-checks/public-P16.1-round-92-final-reader/sources/S1-literal_extract.txt'
N = R / 'root-checks/P16.5-fixed-effective-divisor-relative-equations-20261005-continuation106.md'
D = R / 'root-checks/P16.5-continuation106-primary-units'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
assert sha(S) == '659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0'
assert 'BJ4.23 then gives equality everywhere' in N.read_text()
D.mkdir()
lines = S.read_bytes().decode().split('\n')
specifications = [
    ('fs-functions-and-addition', 1180, 1240),
    ('actual-section-division-2-23', 1270, 1289),
    ('psh-addition-scaling-4-7', 2301, 2368),
    ('maximum-principle-4-12', 2381, 2397),
    ('divisorial-determination-4-22', 2494, 2533),
    ('zariski-pluripolar-4-36', 2590, 2613),
    ('pluripolar-negligible-5-3', 2720, 2757),
    ('divisorial-nonnegligibility-ample-compactness', 2770, 2844),
    ('homogeneous-approximation-6-17', 3160, 3255),
    ('printed-division-diagnostic-6-21', 3258, 3275),
    ('homogeneous-decomposition-6-24', 3290, 3354),
    ('siu-decomposition-6-31', 3419, 3435),
    ('finite-energy-zero-negligible-mass-13-2', 6309, 6338),
]
units = []
for identifier, a, z in specifications:
    assert 0 < a <= z <= len(lines)
    p = D / (identifier + '.txt')
    p.write_bytes(('\n'.join(lines[a-1:z]) + '\n').encode())
    assert p.read_bytes() == ('\n'.join(lines[a-1:z]) + '\n').encode()
    units.append({'id': identifier, 'path': str(p), 'sha256': sha(p),
                  'inclusive_one_based_LF': [a, z], 'one_trailing_newline_added': True,
                  'source': str(S), 'source_sha256': sha(S),
                  'url': 'https://arxiv.org/pdf/1801.08229v4'})
record = {
    'construction': str(N), 'construction_sha256': sha(N),
    'construction_entire_root_read': True, 'independently_reviewed': False,
    'original_P16_5_closed': False,
    'primary_version': 'Boucksom--Jonsson arXiv:1801.08229v4',
    'full_primary_source': str(S), 'full_primary_sha256': sha(S),
    'whole_primary_root_read': False,
    'selected_intervals_root_read': True,
    'units': units,
    'proof_boundary': 'Section1.1 supplies its own ample compactness repair; no monotonicity of h_i-t_i sigma_D is assumed. Local product identification, exact Kodaira input binding and full-original reference scope still require audit.',
}
(D / 'binding.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'construction_sha256': sha(N), 'binding': str(D / 'binding.json'),
                  'units': len(units), 'original_closed': False}, indent=2))
