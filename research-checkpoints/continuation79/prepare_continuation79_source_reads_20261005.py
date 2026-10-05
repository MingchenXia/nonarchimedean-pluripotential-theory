"""Freeze source ranges actually read for the new, unreviewed Runge proposal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
S = R/'root-checks/continuation79-explicit-strict-potential-and-Runge-source-reads'
P = R/'root-checks/P16.1-explicit-strict-potential-localized-hull-and-Runge-reconstruction-20261005-continuation79.md'
source = R/'shared-sources/new-primary-2609.27610v1-20261004.txt'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not S.exists() and P.is_file()
lines = source.read_bytes().decode('utf-8').split('\n')
assert len(lines) == 2912
S.mkdir()
units = []
specifications = [
    ('extended-tropical-convexity-and-PL-definitions',645,700,
     'Diagnostic definitions and approximation statement. The new strict construction uses an explicit multinomial maximum, not a Gaussian-extension assertion.'),
    ('affine-polytopes-and-retained-generators',860,905,
     'Actual affine FS arguments must retain the closed embedding generators. Closed-polytope topological interiors are not silently identified with strict norm inequalities.'),
    ('already-regularizable-growth-and-decreasing-clipping',950,1038,
     'Reconstruct the pre-EP compactification and whole-floor-collar proof. Do not apply local/global equality or a fixed-class FS sequence to a function before proving genuine global membership.'),
    ('Runge-hulls-compactness-exhaustion-and-Rossi',1532,1730,
     'Rossi uses a continuous rational compact perturbation. Correct the printed norm inequalities and use strict margins for polynomial neighborhoods; previous local closure statements here assume EP.'),
    ('Hartogs-radius-and-sublevel-Runge',1731,1837,
     'Use explicitly strict polynomial domains for the exact coefficient radius formula. Topological interior of a closed polytope may contain norm-equality points. Compact sup limits need no uniform Dini claim for an usc target.'),
    ('localization-original-pole-counting-diagnostic',1838,1890,
     'The printed denominator-power count is false for nonreduced f, as f=z^2 and h=z^{-1} shows. Replace it by actual normalization divisor orders and one finite-module annihilator in the original ring.'),
    ('strict-convex-potential-and-local-hull-diagnostic',1963,2081,
     'The new proposal replaces the Gaussian extension by explicit soft maximum and multinomial estimates. The original-u local regularization hypothesis is needed when replacing rho by rho-prime; regularity of u+c*rho does not imply regularity of u.'),
    ('local-to-global-Hartogs-assembly-diagnostic',2082,2110,
     'Countable-density and product-witness hypotheses are retained. Reconstruct the localized hull and Hartogs conversion without assuming singular EP.'),
    ('finite-smooth-base-weak-trace-and-radial-diagnostic',2200,2372,
     'Open weak trace requires smooth regularization and principal-open removal. Boundary equality uses fixed positive integer slicing weights and direct radial subharmonic comparison over H(s), avoiding arbitrary-H(s) affine regularization.'),
    ('split-piece-Runge-full-proof-diagnostic',2373,2533,
     'Read the complete contradiction. Repair open versus compact sets, whole-base continuity, locally constant integer weights, gamma=1, the c-factor in the gap, the wrong winning-locus formula, common-witness gluing, and finite pullback generator retention.'),
    ('finite-projection-and-two-singular-inductions',2534,2696,
     'Read full descending-Z and singular-stratum inductions. Keep reduced singular loci, finite-base open restrictions, projection at all conjugates, local Nakayama and the actual preimage of the chosen affine target open.'),
    ('unibranch-envelope-and-cardinality-extension-diagnostic',2697,2755,
     'Read full W7.1 proof. Countable descent is for finite PL tests/reference data; all arbitrary PSH competitors do not descend to one field. Correct pullback directions and retain orthogonality, positive MA base change and domination antecedents.'),
]
for label, first, last, scope in specifications:
    literal = '\n'.join(lines[first-1:last])
    path = S/(label+'.txt')
    path.write_text(literal)
    assert path.read_bytes().decode('utf-8') == literal
    units.append({'id':label,'version':'2609.27610v1','source':str(source),
                  'source_sha256':sha(source),'inclusive_one_based_LF':[first,last],
                  'literal_file':str(path),'literal_sha256':sha(path),
                  'selected_literal_body_root_read':True,'whole_primary_body_root_read':False,
                  'new_application_independently_reviewed':False,'scope_and_limits':scope})
write(S/'source-read-record.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'units':units,'proposal':str(P),'proposal_sha256':sha(P),
    'whole_saved_proposal_root_read':True,'proposal_independently_reviewed':False,
    'accepted_dependency':False,'original_P16_1_closed':False,
    'active_round70_frozen_and_no_hot_feedback':True,
    'reconstruction_antecedents_still_required':['G1','G2','G3','G4']})
print(json.dumps({'source_read_record':str(S/'source-read-record.json'),
    'source_read_record_sha256':sha(S/'source-read-record.json'),
    'literal_units':len(units),'proposal_sha256':sha(P),
    'original_P16_1_closed':False},indent=2))
