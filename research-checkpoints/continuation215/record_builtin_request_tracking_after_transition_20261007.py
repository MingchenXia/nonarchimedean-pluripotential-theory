from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

K=Path('/workspace/research/root-checks')
entries=[
('public-P16.4-continuation265-actual-positive-curve-models-and-raw-formal-curvature','P16.4-paper.tex','53','WAIT_TRACKING_CELL_NOT_FOUND','exec cell 53 not found'),
('public-P16.4-continuation269-all-genus-original-field-curve-equation','P16.4-paper.tex','113','WAIT_TRACKING_CELL_NOT_FOUND','exec cell 113 not found'),
('public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact','P05.2-paper.tex','27','PENDING_CURRENT_EXEC_CELL','Script running with cell ID 27')]
for folder,name,cell,status,observed in entries:
    D=K/folder;p=D/'builtin-request-tracking-addendum-after-environment-transition-20261007.json'
    assert not p.exists()
    source=D/name;b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
    digest=hashlib.sha256(source.read_bytes()).hexdigest();assert digest==b['source_sha256']
    d=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source=str(source),source_sha256=digest,
        original_request_cell=cell,current_tracking_status=status,last_wait_response=observed,
        actual_compiler_diagnostics_returned=False,builtin_compilation_success=False,
        lost_wait_cell_is_not_a_compiler_failure_or_unavailable_diagnostic=True,
        local_reproduction_build_exit_codes=b['root_local_build_exit_codes'],
        local_reproduction_warnings=b['root_local_warnings'],source_preserved=True,
        new_compiler_request_launched=False,new_accepted_paper=False,original_closed=False,
        frozen_old_request_addenda_unchanged=True,active_independent_audits_not_modified=True,
        protected_current_editor_unchanged_open=True)
    p.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(dict(path=str(p),status=status,source_sha256=digest,local_builds=b['root_local_build_exit_codes'],builtin_success=False)))

