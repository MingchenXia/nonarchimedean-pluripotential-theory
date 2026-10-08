from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
W=K/'P12.3-P12.6-continuation359-explicit-normalization-formula-and-exact-positive-domain-on-reduced-surface-boundaries-working-proof-20261008.md'
B=K/'P12.3-P12.6-continuation359-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();assert not B.exists()
for q,expected in [(256,'ac95a1135b126796b9970ffb0a0924623cec2fc00086157154ef29656c414d51'),(257,'7773844e1fa237e945fd448fe709d202abc848bc3527c2682a8462f7b7cc0ba4')]:
 C=next((R/f'campaigns/round-{q}').iterdir());assert sha(C/'input.json')==expected
 for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes'];assert str(W)!=e.get('origin')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();record=dict(recorded_utc=now,continuation=359,atoms=['P12.3','P12.6'],status='ENTIRE new working proof UNREVIEWED, held for FUTURE independent reconstruction, no hot feedback',proof=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W)),ROOT_reading='Entire saved source physically read in two overlapping bounded chunks; complete conductor-mask paragraph corrected/read to avoid false iff at finite v(c)>=N. No current frozen input was modified.',only_correctness_grant='ENTIRE qualified G331 at mandatory source/model/support scope',explicit_mathematical_hypothesis='Every marked normal-centre finite continuous obstacle has a greatest geometric C envelope CE. Surface corollary requires ENTIRE new unreviewed355 geometry/source proof independently reconstructed, not a correctness import.',new_results=['Whole USC-regularized base envelope equals max of actual source envelope on every FULL normalization fibre, under CE','Exact equivalence of base positivity, base raw continuity, source full-fibre constancy and fibre-maximum continuity','Every reduced excellent dimension<=2 corollary CONDITIONAL on full355 reconstruction','Uniform nonexpansivity and closed positive finite-continuous domain with ONE gauge cocycle'],limits='No arbitrary normal>=3 CE; no unconditional extendedUSC/pole formula without source continuity; no finite generic/sample substitute for whole conductor quotient test; no original or paper acceptance.',not_in_frozen_native256257=True,hot_feedback_sent=False,source_bodies_pixels_LOCALONLY=True,original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True)
B.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==258
 x.update(updated_utc=now,ROOT359_normalization_formula=dict(proof=record['proof'],binding=str(B),status=record['status']));p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(proof=record['proof'],binding=str(B),not_in_ACTIVE_inputs=True,counts_unchanged=True),indent=2))
