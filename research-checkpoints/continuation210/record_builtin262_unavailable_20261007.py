from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

K = Path('/workspace/research/root-checks')
D = K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact'
p = D/'root-builtin-unavailable-addendum-20261007.json'
assert not p.exists()
sha = lambda q: hashlib.sha256(q.read_bytes()).hexdigest()
b = json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert sha(D/'P05.2-paper.tex') == b['source_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
d = dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
         requested_tool='codex_app.compile_latex_document', request_cell='23',
         requested_saved_source=str(D/'P05.2-paper.tex'),
         source_sha256=b['source_sha256'],
         returned_result='No handler registered for tool: codex_app.compile_latex_document',
         builtin_available=False, builtin_success=False,
         separate_prior_local_build_exit_codes=b['root_local_build_exit_codes'],
         source_preserved=True, protected_current_editor_open_unchanged=True,
         frozen_round204_math_inputs_unchanged=True,
         earlier_pending_compile_requests_resolved_by_this_result=False,
         mathematical_verdict=None, original_closed=False)
p.write_text(json.dumps(d, indent=2)+'\n')
print(json.dumps(d, indent=2))
