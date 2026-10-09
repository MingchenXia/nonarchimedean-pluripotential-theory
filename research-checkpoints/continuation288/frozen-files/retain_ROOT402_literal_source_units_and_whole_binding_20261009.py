from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
S=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
T=R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009/GR2506.13548v2-full-LOCALONLY.txt'
D=R/'primary-data-LOCALONLY/P16.7-ROOT402-atomic-point-tests-source-20261009'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(S)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
assert sha(T)=='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b'
assert not D.exists();D.mkdir()
spec=[(S,1773,1830,'CLD-1.7.1-raw-factorial-full-proof','Applied'),(S,1931,2135,'CLD-1.7.6-8-convex-max-and-atomic-full-proofs','Applied'),(S,15846,15914,'CLD-11.6.1-5-finite-flat-local-and-full-proof','Applied'),(S,19772,19819,'CLD-13.8.1-5-graded-Abhyankar-basis-criterion','Applied'),(S,20953,21008,'CLD-14.5.2-3-canonical-degree-calibration-full-proof','Applied'),(S,10595,10739,'CLD-8.9.1-4-actual-atomic-max-full-proof','Applied'),(S,27608,27671,'CLD-18.6.2-Gauss-fibre-full-proof','Corroboration-only-in402'),(T,1673,1780,'GR-v2-6.3-all-Shilov-graded-dimension-full-proof','Applied'),(T,1781,1814,'GR-v2-6.4-all-affinoid-Shilov-maximum-full-proof','Applied-reused-and-reread-no-second-reading-credit')]
units=[]
for s,lo,hi,label,role in spec:
    data=s.read_bytes().splitlines(keepends=True);q=D/(label+'-LOCALONLY.txt');q.write_bytes(b''.join(data[lo-1:hi]))
    units.append(dict(path=str(q),source=str(s),source_sha256=sha(s),LF_start=lo,LF_end=hi,bytes=q.stat().st_size,sha256=sha(q),role=role,whole_essential_statement_and_immediate_proof_ROOT_physically_read=True,source_units_LOCALONLY=True,LF_bytes_preserve_form_feeds=True,not_new_recursive_audit_of_deeper_citations=True))
write(D/'literal-unit-bindings-LOCALONLY.json',units)
q=K/'ROOT402-fresh-primary-application-and-compilation-scope-20261009.json'
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),paper=402,whole_current_mathematical_body_ROOT_physically_read=True,new_claim='Actual bounded MA atom at EVERY graded-dimension-two point, finite full-dual test and generated pointwise lower bounds; all Shilov coordinates, product compactness only',source_units=units,source_bodies_units_pixels_books_LOCALONLY=True,continuous_product_application_reused_from_ROOT398_qualified_source_scope=str(K/'ROOT398399-fresh-primary-application-and-compilation-scope-20261009.json'),all_primary_hypotheses_new_application_reconsidered=True,ordinary_foundations=['actual analytic quotient and raw mass-two geometry previously reconstructed','Berkovich relative interior/dimension and completed residue field facts','graded-field transcendence and completion initial-form identity','CLD continuous products, smooth cutoffs/partitions and calibrated integration','GR Temkin/Ducros graded reduction and classical psh bridge','Tychonoff compactness only of coordinate products'],not_all_deeper_proof_trees_freshly_reproved=True,compiler=dict(path=str(P),kind='success',message="The current source compiled successfully with the desktop editor's compiler.",initial_mathscr_package_error_repaired=True,mathematical_certification=False),UNREVIEWED=True,accepted=False,original_closed=False,protected_editor_OPEN_UNCHANGED=True,new_material_sent_to_active_native280281=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
write(q,record)
b=K/'P16.7-continuation402-ROOT-whole-paper-source-scope-and-binding-20261009.json'
write(b,dict(recorded_utc=record['recorded_utc'],paper=402,whole_paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),source_scope=dict(path=str(q),sha256=sha(q)),compiler=record['compiler'],entire_current_math_and_immediate_applied_proof_units_ROOT_physically_read=True,UNREVIEWED=True,accepted=False,original_closed=False,new_material_sent_to_active_native280281=False,protected_editor_OPEN_UNCHANGED=True,counts=record['counts']))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[280,281]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['ROOT402_atomic_tests_and_Sh ilov_point_bounds'.replace('Sh ilov','Shilov')]=dict(path=str(P),binding=str(b),UNREVIEWED=True,accepted=False,original_closed=False)
    x['updated_utc']=record['recorded_utc'];p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(paper=str(P),paper_sha256=sha(P),binding=str(b),source_units=len(units),compiler='success',solved=16,open=26,accepted_papers=97),indent=2))

