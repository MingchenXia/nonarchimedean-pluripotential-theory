from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation403-generated-uniqueness-by-two-actual-Gauss-fibres-working-paper-20261009.tex'
P402=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
S=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
U=R/'primary-data-LOCALONLY/P16.7-ROOT403-two-actual-Gauss-fibres-source-20261009'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(S)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
assert sha(P402)=='69236b72acdfd53fc29a6187ff2747f932c5c5fcfbaa59d3ba543ae0f5ff3b99'
assert sha(P)=='59c5a48976c7a33a079a7702c97396aeb4f32b2a1a7d535587bc38a61c763ea2'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert not U.exists();U.mkdir()
lines=S.read_bytes().splitlines(keepends=True)
units=[]
for name,a,b,use in [
('CLD-13.8.8',19858,19917,'Full line-point Abhyankar scalar-extension graded residue, finite over the compositum; no surface energy extension'),
('CLD-14.4.3',20924,20935,'Same-ground-field finite extension curve calibration factor, distinct from normalized varying-ground-field integration'),
('CLD-14.5.2-3',20953,21008,'Whole local curve canonical degree-one calibration statement and immediate proof'),
('CLD-15.3.1-2',21710,21743,'Whole normalized varying-ground-field measure integration statements and immediate proofs; only15.3.1 needed'),
('CLD-16.1.1',22158,22170,'Whole normalized base change of fundamental currents statement and immediate proof'),
('CLD-18.6.1',27560,27607,'Whole relative curvature-to-fibre statement and immediate proof, disclosed18.3-18.4 deeper inputs'),
('CLD-18.6.2',27608,27671,'Whole actual single-function Gauss-fibre curvature corollary and immediate proof')]:
    p=U/f'{name}-LF{a}-{b}-LOCALONLY.txt';p.write_bytes(b''.join(lines[a-1:b]))
    units.append(dict(source='CLDv2',source_sha256=sha(S),literal_LF=[a,b],local_unit_path=str(p),bytes=p.stat().st_size,sha256=sha(p),ROOT_immediate_statement_and_whole_proof_physically_read=True,qualified_application=use,deeper_proof_tree_freshly_recursively_read=False,full_body_LOCALONLY=True))
now=datetime.now(timezone.utc).isoformat()
Q=K/'ROOT403-fresh-primary-application-and-compilation-scope-20261009.json'
B=K/'P16.7-continuation403-ROOT-whole-paper-source-scope-and-binding-20261009.json'
scope=dict(recorded_utc=now,paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_new_mathematical_body_ROOT_physically_read=True,exact_ROOT402_appendix_whole_body=dict(source_path=str(P402),source_sha256=sha(P402),body_bytes=19974,body_sha256='9e20154a57896b0ef81ef54f893ab090c80efbf514e071be05b0cf13a9045de5',exact_identity=True,second_independent_source_reading=False),fresh_applied_source_units=units,GR_source_scope_inherited_from_ROOT402=True,standing_foundations=['Reconstructed actual analytic quotient and nonalgebraization','CLD continuous products at all stages, Radon representation, smooth cutoffs/Stokes/approximation','Standard scalar-extension surjectivity and algebraic closedness of completed algebraic closure','Graded Abhyankar inequality and tower additivity','CLD relative curvature/intersection foundations18.3-18.4 and normalized calibration definitions','GRv2 smooth recognition, decreasing closure and all affinoid Shilov maximum at original hypotheses'],new_proof_steps=['Actual generated operator/full dual/all FOUR moving moments reconstructed by cubic interpolation','Uniform-energy ALL bounded-test gradient estimate I/2+sqrt(42CI)','Finite Gauss-disc lifting proved directly by nested discs and polynomial factorization','Actual curve degree-one Dirichlet endpoint control and normalized finite extension','Positive single-function Gauss-fibre current/global bounded cap controls strong curve norms','Two ACTUAL separate coordinate fibre paths to the joint Gauss point, not an analytic Shilov section','Point atoms supply finite full-dimensional endpoint limits','All skeleton coordinate-radius paths and all-Shilov reconstruction give pointwise generated uniqueness including poles'],compiler=dict(kind='success',path=str(P),tool='codex_app.compile_latex_document',actual_result_observed=True),UNREVIEWED=True,accepted=False,original_closed=False,new_correctness_grant=False,supplied_or_native_programs_executed_or_imported=False,source_bodies_pixels_books_LOCALONLY=True,no_active_campaign_hot_feedback=True,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),residual=['Maximal intrinsic E1 recognition','Actual energy-sublevel representability and compactness','Envelope or proved variational replacement','Arbitrary-support full-finite-dual equation existence'])
write(Q,scope)
write(B,dict(recorded_utc=now,paper=scope['paper'],source_scope=dict(path=str(Q),sha256=sha(Q)),compiler=scope['compiler'],exact_ROOT402_appendix=scope['exact_ROOT402_appendix_whole_body'],accepted=False,original_closed=False,UNREVIEWED=True,claim='Complete WORKING proof of pointwise uniqueness in the actual decreasing-generated class; not original full P16.7 closure',counts=scope['counts'],local_primary_bodies_not_exported=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint'] is None
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT403_generated_pointwise_uniqueness_working_proof=dict(paper=str(P),sha256=sha(P),binding=str(B),UNREVIEWED=True,original_closed=False),next_work='Publish whole402403 then full terminal280281 mathematical reconstruction. Independently audit complete two-actual-Gauss-fibre generated uniqueness, continue actual compactness/envelopes/existence. No acceptance or count change.')
    write(p,x)
print(json.dumps(dict(paper=str(P),binding=str(B),source_scope=str(Q),compiler='success',literal_source_units=len(units),UNREVIEWED=True,solved=16,open=26,accepted_papers=97),indent=2))
