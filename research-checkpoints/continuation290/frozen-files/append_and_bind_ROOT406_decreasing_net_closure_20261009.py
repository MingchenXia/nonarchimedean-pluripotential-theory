from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P16.7-continuation406-energy-bounded-decreasing-nets-and-sequential-flattening-working-paper-20261009.tex'
Q=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
T=R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009/GR2506.13548v2-full-LOCALONLY.txt'
U=R/'primary-data-LOCALONLY/P16.7-ROOT406-decreasing-net-closure-source-20261009'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(Q)=='135691524d4efb8d41e827c44a08b32962ade20dc4f042d932f244365a726f0d'
assert sha(T)=='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
text=P.read_text(); marker='% APPEND_COMPLETE_CURRENT402_BODY_HERE'
assert text.count(marker)==1 and not U.exists()
source=Q.read_text(); start=source.index('\\section{The actual analytic object and proof foundations}'); end=source.index('\\end{document}',start)
body=source[start:end]; assert body and '\\end{document}' not in body
P.write_text(text.replace(marker,body))
assert body in P.read_text() and marker not in P.read_text()
U.mkdir(); data=T.read_bytes().split(b'\n'); literal=b'\n'.join(data[1115:1198])+b'\n'
unit=U/'GRv2-Proposition4.2-whole-immediate-proof-and-context-LF1116-1198-LOCALONLY.txt'; unit.write_bytes(literal)
now=datetime.now(timezone.utc).isoformat()
scope=K/'ROOT406-fresh-decreasing-net-proof-primary-application-and-compilation-scope-20261009.json'
record=dict(recorded_utc=now,paper=406,new_complete_abstract_proof_ROOT_physically_read=True,new_mathematical_claims=['canonical energy as all strict continuous majorant infimum','actual energy-bounded decreasing-net closure with canonical energy equality','countable supplied-presentation diagonal for decreasing sequences without countable dense set','Radon monotone CONTINUOUS-net integral theorem and full bounded-dual L1 convergence','all full-dimensional/Shilov point bounds and pole reconstruction in the net-generated class'],primary_full_source=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T),LOCALONLY=True),fresh_literal_primary_unit=dict(path=str(unit),bytes=unit.stat().st_size,sha256=sha(unit),literal_real_newline_LF=[1116,1198],complete_GR4_2_statement_and_immediate_proof_physically_read=True,recursive_GR3_5_5_proof_not_freshly_read=True,LOCALONLY=True),whole402_appendix=dict(path=str(Q),bytes=Q.stat().st_size,sha256=sha(Q),mathematical_body_bytes=len(body.encode()),mathematical_body_sha256=hashlib.sha256(body.encode()).hexdigest(),exact_literal_identity=True,another_independent_fresh_reading=False,whole_402_working_proof_supplied_not_correctness_grant=True),ordinary_backgrounds=['compact Hausdorff normality/Urysohn and directed finite-cover compactness','finite Radon open-set inner regularity and scalar layer-cake integrals','exact earlier qualified all-stage CLD Green/energy and point-atom construction','GRv2 smooth classical recognition unnumbered Section1.2 and all-Shilov dimension/maximum units at exact hypotheses'],explicit_not_claimed=['arbitrary measurable-net monotone convergence','sequence/net class equality or arbitrary-net countable cofinality','arbitrary coordinate-limit representability or closed evaluation image','arbitrary-support equation existence or full original P16.7'],compiler=dict(kind='pending'),primary_bodies_units_pixels_books_LOCALONLY=True,native_or_supplied_programs_executed_or_imported=False,hot_feedback_sent=False,protected_editor_OPEN_UNCHANGED=True,UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
write(scope,record)
binding=K/'P16.7-continuation406-ROOT-whole-paper-source-scope-and-binding-20261009.json'
write(binding,dict(recorded_utc=now,paper=406,whole_paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),source_scope=dict(path=str(scope),sha256=sha(scope)),compiler=dict(kind='pending'),UNREVIEWED=True,accepted=False,original_closed=False,counts=record['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    path=R/name; state=json.loads(path.read_text())
    assert state['github_pending_checkpoint'] is None and state['latest_verified_github_checkpoint']['continuation']==289 and state['current_active_batch']==[282,283]
    assert len(state['fully_solved_original_atoms'])==16 and state['remaining_open_original_atoms']==26 and state['historical_reviewed_scoped_papers']==97
    state.update(updated_utc=now,ROOT406_actual_decreasing_completion_working_proof=dict(paper=str(P),sha256=sha(P),binding=str(binding),compiler='pending',UNREVIEWED=True,original_closed=False))
    write(path,state)
print(json.dumps(dict(paper=str(P),bytes=P.stat().st_size,sha256=sha(P),literal_full402_math_body_bound=True,source_literal_retained_LOCALONLY=True,compiler='pending',UNREVIEWED=True,original_closed=False),indent=2))
