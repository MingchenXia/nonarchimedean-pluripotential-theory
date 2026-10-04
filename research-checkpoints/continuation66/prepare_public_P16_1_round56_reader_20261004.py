"""Preserve the completed unreviewed round56 result without changing it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R/'campaigns/round-56/P16.1-public-source-noncircular-local-extension-unibranch-equation'
run = json.loads((C/'run.json').read_text())['campaign']['result']
assert run['kind'] == 'notes' and run['candidate'] is False
assert [n['id'] for n in run['notes']] == ['n1','n2','n3','n4']
W = Path(run['workspace'])
assert W == C/'artifacts/codex-aL8dxB'
D = R/'root-checks/public-P16.1-round-56-final-reader'
assert not D.exists()
shutil.copytree(W,D)
(D/'canonical-notes.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks = []
for p in sorted(W.rglob('*')):
 if p.is_file():
  q = D/p.relative_to(W)
  assert p.read_bytes() == q.read_bytes()
  checks.append({'relative_path':str(p.relative_to(W)),'bytes':p.stat().st_size,'sha256':sha(p)})
provenance = json.loads((D/'source-extracts/source-provenance.json').read_text())
assert len(provenance['excerpts']) == 40
for s in provenance['sources']:
 for f in s['files']:
  assert sha(D/f['local_file']) == f['expected_sha256']
  assert sha(f['supplied_cache']) == f['expected_sha256']
for e in provenance['excerpts']:
 p = D/e['source_file'];q = D/e['excerpt_file']
 assert sha(p) == e['source_sha256']
 actual = '\n'.join(p.read_text().split('\n')[e['LF_start']-1:e['LF_end']])
 assert actual == e['literal_statement_and_proof'] == q.read_text()
 assert sha(q) == e['excerpt_sha256']
input_saved = json.loads((D/'input.json').read_text())
input_campaign = json.loads((C/'input.json').read_text())
assert (D/'input.json').read_bytes() == (D/'input-original.json').read_bytes()
assert input_saved == input_campaign
assert json.loads((D/'task-original.json').read_text()) == input_campaign['task']
assert (D/'assignment-original.txt').read_text() == input_campaign['assignment']
status = json.loads((D/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id'] == 'P16.1' and status['status'] == 'partial'
record = {
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'original_workspace':str(W),'frozen_reader':str(D),
 'candidate':False,'original_problem_solved':False,
 'entire_completed_native_result_and_all_four_notes_root_read':True,
 'whole_argument_root_read':True,'argument_LF_count':1247,
 'whole_tex_root_read':False,
 'source_metadata_root_read':True,'all_literal_excerpts_byte_reproduced':True,
 'literal_excerpts':40,'all_literal_excerpt_bodies_root_read':False,
 'whole_primary_source_bodies_root_read':False,
 'root_independent_tex_compilation':'NOT_YET_RUN',
 'native_editor_compilation':'NOT_YET_REQUESTED',
 'independent_correctness_review':'NOT_LAUNCHED',
 'binding_checks':checks,
 'evidence_limit':'Preservation and LF bindings only; new mathematical claims unreviewed.'
}
(D/'root-preservation-and-read-state-continuation66.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reader':str(D),'files':len(checks),'argument_sha256':sha(D/'P16.1-argument.md'),'pdf_sha256':sha(D/'P16.1-paper.pdf'),'canonical_result_sha256':sha(D/'canonical-notes.json'),'literal_bindings':40,'candidate':False},indent=2))
