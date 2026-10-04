from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
note = R / 'root-checks/P02.4-fixed-domain-net-and-sequence-bridge-20261004.md'
out = note.with_suffix('.binding.json')
assert not out.exists()

def bind(p):
    data = Path(p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

book = R / 'book-source/manuscript/editorial/rethlas_packets_20260827'
parents = [book / 'p063_curve_cld_monotone_regularization_statement_20260827.tex',
           book / 'p063_curve_cld_monotone_regularization_proof_20260827.tex']
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'new_mathematical_note': bind(note),
    'origin': 'Root-authored compact-domain net/F_sigma sequence bridge; not a native-author or independent-review output.',
    'exact_imported_finite_lisse_regularization': [bind(p) for p in parents],
    'complete_imported_statement_and_proof_read': {'statement_LF': [1, 140], 'proof_LF': [1, 593]},
    'new_applications_checked': ['Fixed Y before all lisse indices; refinements remain trees; entire unused components capped.',
        'Actual majorants directed using a continuous comparison minimum, never a psh minimum.',
        'F_sigma necessity for continuity on compact Y; compact-piece sufficiency and explicit monotonic gap.',
        'Scalar pullbacks retain actual terms, order, and limit; not independent upstairs-family equality.',
        'Saturated projective fibers over H(c), including nonrigid points; no nonsaturated germ extension.'],
    'new_note_entirely_root_read': True,
    'published_source_bindings': [bind(R / 'shared-sources' / name) for name in
        ['Thuillier-tel-00010990v1.txt', 'GR-2506.13548v2-20261004.txt',
         'CD-1204.6277v2-20261004.txt', 'GJR-2111.05741.txt']],
    'additional_primary_read_this_turn': [{'source': 'GR-2506.13548v2-20261004.txt', 'LF': [1618, 1653],
        'scope': 'Theorem 6.1 complete statement and proof'},
        {'source': 'GJR-2111.05741.txt', 'LF': [4075, 4118],
        'scope': 'Remark 15.10 tail and Proposition 15.11 complete statement/proof; explicitly a net'}],
    'new_note_independently_accepted': False,
    'historical_review_verdict_used_as_premise': False,
    'book_copied_or_exported': False,
    'running_authors_received_feedback': False,
    'original_atoms_closed': [],
}
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(bind(out)))
