from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research')
B=R/'root-checks/P16.2-continuation113-primary-binding.json'
assert not B.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
note=R/'root-checks/P16.2-finite-fixed-bundle-approximants-before-original-descent-20261005-continuation113.md'
sources=[]
for name in ['canonical-trivial-metric.txt','nested-fixed-section-net-flattening.txt','fixed-actual-ample-section-generation.txt']:
    p=R/'root-checks/P16.2-continuation109-primary-units'/name
    sources.append({'path':str(p),'sha256':sha(p),'url':'https://arxiv.org/pdf/1801.08229v4',
                    'entire_selected_unit_root_read_again':True,'whole_primary_root_read':False})
p=R/'root-checks/P16.2-continuation109-stacks-primary/0AY8-mathematical-body.txt'
sources.append({'path':str(p),'sha256':sha(p),'url':'https://stacks.math.columbia.edu/tag/0AY8',
                'entire_selected_unit_root_read_previously':True})
B.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
    'independent_review_performed':False,'original_closed':False,'units':sources,
    'finite_inner_approximant_flattening_proof_supplied_in_note':True,
    'original_common_pole_family_not_used_for_strict_flattening_step':True,
    'remaining_dependencies':['109 original canonical metric descent','109 whole bad-fiber containment',
                              'full converse fixed-divisor cone division'],
    'active108_109_private_outputs_read_or_used':False,'hot_feedback_sent':False},indent=2)+'\n')
print(json.dumps({'binding':str(B),'sha256':sha(B)}))
