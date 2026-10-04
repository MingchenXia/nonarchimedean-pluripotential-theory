from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess

R = Path('/workspace/research')
md = R / 'root-checks/P02.4-reduced-curve-ordinary-smoothing-20261004.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(md) == '8861c2af05d5ea12d0480b585c1329e35934b4b7d2dbe591a843f3df272b4545'
out = R / 'root-checks/P02.4-reduced-curve-ordinary-paper-20261004'
out.mkdir(exist_ok=False)
tex = out / 'P02.4-reduced-curve-ordinary-paper.tex'
cmd = ['pandoc', str(md), '--standalone', '--from=markdown+tex_math_dollars',
    '--to=latex', '-V', 'geometry:margin=1in', '-V', 'fontsize=11pt',
    '-V', 'colorlinks=true', '--output', str(tex)]
run = subprocess.run(cmd, capture_output=True, text=True)
(out / 'pandoc.stdout').write_text(run.stdout)
(out / 'pandoc.stderr').write_text(run.stderr)
assert run.returncode == 0, run.stderr
def bind(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
book = R / 'book-source/manuscript/editorial/rethlas_packets_20260827'
parents = [book / 'p063_curve_cld_monotone_regularization_statement_20260827.tex',
    book / 'p063_curve_cld_monotone_regularization_proof_20260827.tex']
assert sha(parents[0]) == '767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68'
assert sha(parents[1]) == 'd1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8'
prior = R / 'root-checks/P02.4-fixed-domain-net-and-sequence-bridge-20261004.binding.json'
assert sha(prior) == 'dd00240e5f348307bc8964828c508785e115c61475c690ce7a4e58f6a59e2fce'
data = {'prepared_utc': datetime.now(timezone.utc).isoformat(),
    'origin': 'Root-authored local continuation with an exact explicitly imported finite-tree smoothing premise; not a native-author or independent-review result.',
    'mathematical_source': bind(md), 'standalone_tex': bind(tex),
    'pandoc_command': cmd, 'pandoc_returncode': run.returncode,
    'exact_imported_foundation': [bind(p) for p in parents],
    'prior_complete_imported_source_read_binding': bind(prior),
    'repeated_imported_read': {'statement_LF': [1,140], 'proof_LF': [320,500]},
    'new_mathematical_application_checks': [
        'Constant stability plus fixed compact uniform density gives actual directed smooth majorants; continuous comparison minimum is not used as a psh function.',
        'Choose branch tree interiors before a single downstream strict affinoid; finite closedness and finite clopen partition make all branch comparison sets compact.',
        'Finite target value: align all node values by shifts less than epsilon and retain a strict 2epsilon gap on every branch.',
        'Pole at node: common finite cap below every continuous comparator gives ordinary smooth psh terms and a strict 5epsilon/2 gap, including identically minus-infinity branches.',
        'Closed quotient descent identifies only the displayed normalization points; common constant neighborhoods descend to an actual ordinary neighborhood.',
        'Infimum verified separately at finite/polar nodes and nonsingular finite/polar points with simultaneous compact and pointwise constraints.',
        'F_sigma extraction is performed on the actual already aligned continuous net on one compact Y; ordinary domain and positive forms persist.',
        'All analytic scalar pullbacks use actual constructed terms, rather than equality of independent upstairs and downstairs families.',
        'Saturated projective fibers are compact connected boundaryless over H(c), including nonrigid base points; no nonsaturated-germ extension.'
    ],
    'all_new_markdown_proof_root_read': True,
    'standalone_tex_full_root_read': False,
    'local_compilation_state': 'Not yet attempted.',
    'native_editor_state': 'Not yet attempted.',
    'independent_acceptance': False, 'catalogue_original_closure': False,
    'original_atoms_closed': [], 'external_export_attempted': False,
    'native_authors_received_feedback': False,
    'published_source_bindings': [bind(R / 'shared-sources' / f) for f in
        ['Thuillier-tel-00010990v1.txt','GR-2506.13548v2-20261004.txt','CD-1204.6277v2-20261004.txt']]}
(out / 'preparation-binding.json').write_text(json.dumps(data, indent=2) + '\n')
print(json.dumps({'directory': str(out), 'tex': bind(tex), 'binding': bind(out / 'preparation-binding.json')}, indent=2))
