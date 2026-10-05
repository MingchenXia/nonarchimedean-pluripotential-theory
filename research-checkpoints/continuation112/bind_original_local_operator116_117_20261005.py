from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

source=R/'root-checks/public-P16.1-round-92-final-reader/granted/supplied-02.txt'
assert sha(source)=='d33033e308cf564f25bfd269fb594df77f9a2fc59c428967638f7b1ab10049de'
D=R/'root-checks/P16.2-continuation117-common-collar-primary'
assert not D.exists();D.mkdir()
unit=D/'complete-original-PL-contact-bridge-and-collar-reconstruction.LF25-149.txt'
unit.write_text('\n'.join(source.read_text().split('\n')[24:149])+'\n')
common=[R/'root-checks/P16.2-continuation113-primary-binding.json',
        R/'root-checks/P16.5-continuation114-direct-foundation-binding.json',
        R/'root-checks/P16.2-continuation115-valuative-primary/binding.json']
for p in common:
    b=json.loads(p.read_text());assert sha(b['note'])==b['note_sha256'] and not b['original_closed']
local=json.loads((R/'root-checks/P16.5-continuation107-primary-units/binding.json').read_text())
for u in local['units']:assert sha(u['path'])==u['sha256']
G0=R/'root-checks/public-P16.5-round-105-terminal-draft-reader/preserved/block-00.md'
for no,name in [(116,'P16.2-original-section-local-products-and-common-collar-gate-20261005-continuation116.md'),
                (117,'P16.2-common-ample-collar-and-intrinsic-generated-local-operator-20261005-continuation117.md')]:
    note=R/'root-checks'/name
    binding=R/f'root-checks/P16.2-continuation{no}-local-operator-binding.json'
    save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),'note':str(note),'note_sha256':sha(note),
        'entire_saved_note_root_read':True,'independent_review_performed':False,'original_closed':False,
        'G0':{'path':str(G0),'sha256':sha(G0),'exact_actual_ample_domain_only':True},
        'prerequisite_proposed_bindings':[{'path':str(p),'sha256':sha(p)} for p in common],
        'reused_selected_local_primary_units':local['units'],
        'complete_selected_original_contact_and_collar_proof':{'path':str(unit),'sha256':sha(unit),
            'source':str(source),'source_sha256':sha(source),'inclusive_one_based_LF':[25,149],
            'extraction_rule':'Split LF, select inclusive interval, append one LF.',
            'entire_selected_body_root_read':True,'whole_source_body_root_read_in_this_continuation':False,
            'historical_status_labels_are_not_new_grants':True},
        'local_category':'Actual original section/reference metrics and locally finite affine-FS/contact decreasing approximants with common ordinary neighborhoods; no arbitrary classical-psh/current density claim.',
        'whole_primary_works_root_read':False,'native112_113_private_outputs_read_or_used':False,'hot_feedback_sent':False})
print(json.dumps({'proof_unit':str(unit),'proof_unit_sha256':sha(unit),'source_sha256':sha(source),
                   'new_bindings':[str(R/f'root-checks/P16.2-continuation{no}-local-operator-binding.json') for no in [116,117]],
                   'new_original_acceptances':0},indent=2))
