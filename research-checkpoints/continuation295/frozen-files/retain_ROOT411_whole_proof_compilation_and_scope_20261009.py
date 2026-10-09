from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation411-quadratic-energy-scaling-solid-duals-and-variational-coercivity-working-paper-20261009.tex'
S=K/'P16.7-continuation411-ROOT-source-application-scope-and-residual-20261009.json'
Q=K/'P16.7-continuation411-ROOT-actual-native-editor-compiler-success-20261009.json'
T=K/'P16.7-continuation411-entire-proof-companion-20261009.txt'
B=K/'P16.7-continuation411-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [S,Q,T,B])
paper=P.read_text();assert paper.count('\\begin{document}')==paper.count('\\end{document}')==1
assert '\\label{coeff}\\\\' in paper and 'by normalizing decreasing\ncontinuous presentations' in paper
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[285,286]
    assert x['latest_verified_github_checkpoint']['continuation']==294
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
old407=K/'P16.7-continuation407-Gauss-skeleton-bounds-and-bounded-test-uniform-integrability-working-paper-20261009.tex'
old409=K/'public-P16.7-continuation409-ordered-energy-gaps-and-sequence-generated-net-closure-unreviewed/scoped-paper.tex'
assert sha(old407)=='8c376c0f2d0470329fd61c9c7cc3a2a2fd4eecee4ba9d60b12bed588cbb05692'
assert sha(old409)=='6a32bb619ff94e973e5ccd04e7883aaa78f0dff6f6445cbbefb6347dd2ecc430'
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=411,author='ROOT own independent derivation; no extra model/native campaign',
    UNREVIEWED=True,accepted=False,original_closed=False,all_new_current_unique_proof_body_ROOT_physically_read=True,
    whole_current_formal_source_physically_read_LF_windows=[[1,245],[246,520]],
    tiny_final_source_fixes_ROOT_physically_reread=['Standard align row break','Normalize decreasing presentations; normalized terms need not decrease'],
    actual_current_background_applications=[dict(path=str(old407),sha256=sha(old407),whole_applied_LF_window=[40,204],
        application='All-stage annulus/polyannulus Gauss bound and actual reference theta² measure; fresh current application body read'),
        dict(path=str(old409),sha256=sha(old409),whole_applied_LF_windows=[[178,357],[358,440]],
        application='Actual continuous Green/energy/full dual/generated L1/point atom foundations; fresh current applied bodies read')],
    analytic_foundations_qualified=True,incoming_correctness_grants=[],
    previously_qualified_primary_units_reused_NOT_extra_independent_reading_credit=True,
    new_recursive_audit_of_entire_deeper_GR_CLD_or_quotient_source_chain_claimed=False,
    new_ROOT_complete_proofs=['Exact C=A+2q0/3+q1/3, -E(ta)=tA+t²(1-t/3)q0+t³q1/3; A<=1 gives -E(ta)<=t+3t²C/2',
        'Full mass2 Legendre dual equivalent to normalized energy-unit integral bound N, with E*<=2N+3N²/2',
        'Every finite-full-dual measure B gives integral(-a)<=1+B+sqrt(6BC), extending to actual generated weights through normalized L1 presentations',
        'Universal variational coercivity and explicit energy bound for functional superlevels, without presuming an actual maximizer',
        'Mass2 bounded domination mu<=lambda nu gives finite full dual bound lambda(1+B)+3lambda²B/2',
        'Actual bounded point atom plus NEW solidity gives finite full dual for EVERY total-dimension2 normalized Dirac 2delta_x',
        'Countable finite-cost Radon mixtures and their dominated measures preserve full dual and the specified uniform-tail sector',
        'Every specified countable sequence of full2 points admits explicit strictly positive summable-cost weights; no density/full support assumed'],
    unresolved=['NONORDERED normalized energy-sublevel actual analytic representation/compactness',
        'Adequate intrinsic finite-energy domain recognition',
        'Actual obstacle envelopes/orthogonality or sufficient replacements',
        'EVERY arbitrary-support finiteFULLdual prescribed-measure existence, including actual Dirac equations',
        'Uniform integrability for EVERY finiteFULLdual measure outside the explicit mixture/domination sector'],
    active285286_math_NOT_inspected_or_supplied=True,hot_feedback_sent=False,
    native_or_supplied_programs_executed_or_imported=False,primary_bodies_pixels_book_context_LOCALONLY=True,
    counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(S,scope)
compiler=dict(recorded_utc=now,path=str(P),paper=411,sha256=sha(P),kind='success',
    message="The current source compiled successfully with the desktop editor's compiler.",actual_result_observed=True,
    tool='codex_app.compile_latex_document',mathematical_certification=False,UNREVIEWED=True,accepted=False,original_closed=False,
    protected_editor_OPEN_UNCHANGED=True)
write(Q,compiler)
T.write_text('ENTIRE ROOT411 proof companion\n\n===== COMPLETE STANDALONE TEX =====\n'+paper+
    '\n===== COMPLETE SOURCE/APPLICATION/SCOPE/RESIDUAL RECORD =====\n'+S.read_text())
write(B,dict(recorded_utc=now,paper=411,whole_paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),
    source_scope=dict(path=str(S),bytes=S.stat().st_size,sha256=sha(S)),
    whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),
    compiler=dict(kind='success',actual_result_observed=True,result_record=str(Q),result_record_sha256=sha(Q)),
    public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in [P,S,Q,T]],
    UNREVIEWED=True,accepted=False,original_closed=False,counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,ROOT_own_whole_unreviewed_paper411=dict(binding=str(B),sha256=sha(B),compiler='success'),
        next_work='Publish verified NONFORCE295 whole ROOT411 quadratic scaling, full-dual solidity/Dirac criteria and universal variational coercivity. Native285286 continue; no hot feedback. On terminal285 read ALL actual/expanded proofs, then freeze next P16.7 with whole411 only after full reconstruction. At mostTWO, counts/editor unchanged.')
    write(p,x)
print(json.dumps(dict(paper=411,source_bytes=P.stat().st_size,source_sha256=sha(P),source_LF_lines=len(paper.split('\n')),
    binding=str(B),compiler='success',original_closed=False,accepted=False),indent=2))
