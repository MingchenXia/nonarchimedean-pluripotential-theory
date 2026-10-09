from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P16.7-continuation407-Gauss-skeleton-bounds-and-bounded-test-uniform-integrability-working-paper-20261009.tex'
Q=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
S=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
U=R/'primary-data-LOCALONLY/P16.7-ROOT407-Gauss-and-uniform-tails-source-20261009'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(Q)=='135691524d4efb8d41e827c44a08b32962ade20dc4f042d932f244365a726f0d'
assert sha(S)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
text=P.read_text(); marker='% APPEND_COMPLETE_CURRENT402_BODY_HERE'; assert text.count(marker)==1 and not U.exists()
source=Q.read_text(); start=source.index('\\section{The actual analytic object and proof foundations}'); end=source.index('\\end{document}',start); body=source[start:end]
assert body and '\\end{document}' not in body
P.write_text(text.replace(marker,body)); assert body in P.read_text() and marker not in P.read_text()
U.mkdir(); lines=S.read_bytes().split(b'\n'); units=[]
for name,lo,hi in [('CLDv2-5.10.1-whole-statement-proof-and-5.10.2-reconstruction',6928,6995),('CLDv2-14.5.2-3-whole-calibration-statement-proof',20953,21008)]:
    unit=U/f'{name}-literal-real-LF{lo}-{hi}-LOCALONLY.txt'; data=b'\n'.join(lines[lo-1:hi])+b'\n'; unit.write_bytes(data)
    units.append(dict(path=str(unit),bytes=len(data),sha256=sha(unit),real_newline_LF=[lo,hi],whole_immediate_applied_unit_physically_read=True,LOCALONLY=True))
now=datetime.now(timezone.utc).isoformat(); scope=K/'ROOT407-fresh-Gauss-and-tail-proof-source-and-compilation-scope-20261009.json'
rec=dict(recorded_utc=now,paper=407,new_complete_unique_math_body_ROOT_physically_read=True,new_working_theorems=['two actual coordinate-annulus comparisons prove normalized Gauss bounds minus one half to zero and coordinate one-half Lipschitz estimates','reference curvature measure support proved by Laurent cancellation and exact raw calibrated density two','fixed continuous bounded-test gradient measures dominated by finite bounded mixed measures','uniform T-minus-one-half negative-part tail bound against each fixed bounded test MA measure','actual decreasing-net/pole passage by Radon continuous-net integral theorem'],whole402_math_appendix=dict(path=str(Q),sha256=sha(Q),bytes=Q.stat().st_size,math_body_bytes=len(body.encode()),math_body_sha256=hashlib.sha256(body.encode()).hexdigest(),literal_identity=True,new_independent_audit_or_correctness_grant=False),primary_source=dict(path=str(S),sha256=sha(S),LOCALONLY=True),fresh_literal_units=units,qualified_previous_sources=['GRv2 unnumbered Section1.2 smooth recognition; Proposition4.2 whole scalar extension/pullback and decreasing-net units; Theorem6.4 affinoid maximum','actual all-stage CLD Green/gradient/energy construction fully supplied in appendix','canonical Gauss norms, annulus Shilov endpoints, moment-form dimension rule and compact quotient geometry at exact torus hypotheses'],exploratory_whole_book_first_stage_fragment_read_but_NOT_used_as_premise=True,partial_CLD18_4_and15_6_exploration_NOT_applied_or_claimed_whole=True,entire_recursive_primary_audit=False,explicit_not_claimed=['arbitrary finite-full-dual measure uniform tails without additional domination','arbitrary-coordinate-limit representability or actual energy-sublevel compactness','countable dense set or full-support Radon measure on the actual nonmetrizable space','upper-envelope regularity, arbitrary-support equation existence or full original P16.7'],compiler=dict(kind='pending'),primary_bodies_units_pixels_books_LOCALONLY=True,native_or_supplied_programs_executed_or_imported=False,hot_feedback_sent=False,protected_editor_OPEN_UNCHANGED=True,UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
write(scope,rec); binding=K/'P16.7-continuation407-ROOT-whole-paper-source-scope-and-binding-20261009.json'
write(binding,dict(recorded_utc=now,paper=407,whole_paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),source_scope=dict(path=str(scope),sha256=sha(scope)),compiler=dict(kind='pending'),UNREVIEWED=True,accepted=False,original_closed=False,counts=rec['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    path=R/name; state=json.loads(path.read_text())
    assert state['github_pending_checkpoint'] is None and state['latest_verified_github_checkpoint']['continuation']==290 and state['current_active_batch']==[282,283]
    assert len(state['fully_solved_original_atoms'])==16 and state['remaining_open_original_atoms']==26 and state['historical_reviewed_scoped_papers']==97
    state.update(updated_utc=now,ROOT407_Gauss_and_uniform_tail_working_proof=dict(paper=str(P),sha256=sha(P),binding=str(binding),compiler='pending',UNREVIEWED=True,original_closed=False)); write(path,state)
print(json.dumps(dict(paper=str(P),bytes=P.stat().st_size,sha256=sha(P),literal402_math_body_bound=True,primary_units_LOCALONLY=True,compiler='pending',UNREVIEWED=True,original_closed=False),indent=2))
