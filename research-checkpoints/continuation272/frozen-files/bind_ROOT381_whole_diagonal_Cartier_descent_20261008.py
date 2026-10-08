from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
P=K/'P12.3-continuation381-faithfully-flat-diagonal-Cartier-descent-working-paper-20261008.tex'
S=R/'primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008'
T=S/'Smolkin-subadditivity-1805.08739v3.txt';V=S/'Smolkin-subadditivity-1805.08739v3.pdf'
U=S/'ROOT381-entire-Smolkin-3.12-LF574-695-LOCALONLY.txt'
B=K/'P12.3-continuation381-ROOT-whole-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists()
assert sha(P)=='a779d03e37aec5c1b8feeda0d8c15b8aa2003e85c816908b55b1a5af2c4a4383'
assert sha(T)=='31cc75a107e7a297eb1e0672bbfe8a33f6bf00a6907be2f150e9b690d018c17d'
assert sha(V)=='693b633dd4802d4559e07bc4c7917d556ba03c3e0e010f0fc819e9d6a8438194'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
raw=b'\n'.join(T.read_bytes().split(b'\n')[573:695])+b'\n'
if U.exists():assert U.read_bytes()==raw
else:U.write_bytes(raw)
assert U.read_text().startswith('Theorem 3.12.') and 'The second assertion follows from Theorem 2.8.' in ' '.join(U.read_text().split())
now=datetime.now(timezone.utc).isoformat()
b=dict(recorded_utc=now,paper=381,atom='P12.3',status='UNREVIEWED complete independent module lemma with conditional application to an external infinite-field inclusion. Original remains OPEN; no new accepted paper.',whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),
    whole_paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P),ROOT_entire_saved_proof_and_scope_physically_read=True,untruncated_overlapping_LF_intervals=[[1,165],[160,270]]),
    new_theorem='Any finite-type R over PERFECT charp field k, any PERFECT field extension k-prime, and every e: actual diagonal-compatible Hom kernel and its quotient restriction image D_e commute with field extension. Liftability descends faithfully flatly. Neither normality nor reducedness needed for this module statement.',
    entire_chain='Explicit finite Frobenius via q-bounded monomials and perfect coefficients; finite presentations of F_*R/F_*S/F_*I; precise Phi(F_*x tensor c)=F_*(x tensor c^q), inverse c^(1/q) and all scalar relations; Hom flat change via kernel of finite matrix; compatibility kernel Hom(F_*S,S)->Hom(F_*I,S/I); exact quotient restriction; flat image and faithfully flat cokernel; ideal-multiplied-map inclusion descent; Fitting of differentials fixed-index base change.',
    source_application=dict(url='https://arxiv.org/abs/1805.08739v3',units='ENTIRE Theorem3.12 statement and immediate proof including finite and infinite field paragraphs',inclusive_LF_interval=[574,695],fresh_ROOT_physical_read_intervals=[[540,650],[645,702]],full_text=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),full_PDF=dict(path=str(V),bytes=V.stat().st_size,sha256=sha(V)),full_literal_unit=dict(path=str(U),bytes=U.stat().st_size,sha256=sha(U),LOCALONLY=True),application='Printed finite-field retraction is NOT accepted as an L-module structure. Own module lemma repairs actual diagonal-liftability reduction PROVIDED separate infinite-perfect-field Jacobian inclusion and its reduced/equidimensional/dimension hypotheses independently justified. No wholesale correctness grant to source.',pixel_reading='Earlier ROOT377 physical view of Smolkin PDF page11 retained with exact hash; no new fresh pixel reading asserted here.',deeper_foundation='HH Noether-normalization input in infinite-field proof has not been freshly reconstructed here and is not a premise of own module theorem.'),
    not_proved=['Test-ideal field base change','Independent entire infinite-field Jacobian inclusion/HH theorem','Singular test-ideal subadditivity','Global trace-tail presentation','All-support geometric envelope approximation','Mixed/nonalgebraic/nonisolated original P12.3 completion'],
    no_active_campaign_feedback=True,already_frozen377_unchanged=True,source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,full_primary_units_and_pixels_LOCALONLY=True,compiler='Built-in request115 pending; no success/PDF/export/install or new editor tab claimed.',protected_editor_open_unchanged=True)
B.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['ROOT381_unreviewed_diagonal_Cartier_descent']=dict(paper=str(P),paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),whole_original_solved=False,new_accepted_paper=False,no_active_campaign_feedback=True);x['updated_utc']=now;p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(paper=381,paper_bytes=P.stat().st_size,paper_sha256=sha(P),binding_sha256=sha(B),literal_unit_bytes=U.stat().st_size,literal_unit_sha256=sha(U),no_original_closure=True,solved=16,open=26,papers=97),indent=2))
