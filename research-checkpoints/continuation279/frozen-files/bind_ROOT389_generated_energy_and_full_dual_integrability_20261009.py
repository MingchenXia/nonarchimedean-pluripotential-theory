from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P16.7-continuation389-canonical-generated-energy-and-finite-dual-integrability-working-paper-20261009.tex'
B=K/'P16.7-continuation389-ROOT-whole-proof-source-scope-and-binding-20261009.json'
A=K/'P16.7-continuation388-bounded-Green-and-full-class-radial-dual-working-paper-20261009.tex'
AB=K/'P16.7-continuation388-ROOT-whole-proof-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists()
assert sha(P)=='735e4c6cd92a4a70bc551d74863704463a16cedd2486b54b8a31abbd5ff328b0'
assert sha(A)=='7e5eb11cc158c75d94b5498f860d5545c251883a3fbdec0593538de50f21029f'
assert sha(AB)=='48eb689a58598c623049b94891b9e2d22e17d8eff785598758b83879e1b03ab0'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
t=P.read_text(); stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
    op,n=m.groups()
    if op=='begin':stack.append(n)
    else:assert stack and stack.pop()==n
assert not stack and t.count(r'\[')==t.count(r'\]') and t.count('$')%2==0
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),status='Complete new ROOT working proof UNREVIEWED under whole388 bounded hypotheses; no original closure or acceptance',paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P),ROOT_entire_source_physically_read_untruncated=True,read_LF_chunks=[[1,150],[151,300]]),whole_supporting_bounded_proof=dict(path=str(A),bytes=A.stat().st_size,sha256=sha(A),ROOT_entire_initial_and_amended_source_physically_read_untruncated=True,status='UNREVIEWED'),whole_source_scope=dict(path=str(AB),bytes=AB.stat().st_size,sha256=sha(AB),ROOT_entire_record_physically_read_untruncated=True,status='Retains every388 source/positivity/calibration boundary; no imported acceptance'),new_proof_scope=['Exact bounded energy cocycle from genuine mixed products','Canonical finite energy independent of EVERY bounded continuous decreasing presentation, via strict compact open covers, including infinite values','Generated finite-energy potentials form a convex class; canonical energy is monotone/concave, shifts byrawmass timesconstant and is polynomialdegreeatmost3 along every segment','Every positive measure with finite FULL bounded Ctheta dual has correct raw mass, integrates every generated finite-energy potential and has quantitative negative-part energy bound','Every bounded continuous decreasing presentation of generated finite-energy u converges inL1 of EVERY finiteFULLdual measure','Every genuine bounded analytic MongeAmpere measure has finiteFULLdual exactly attained at its potential, hence the preceding generatedintegrability/L1 properties'],exact_support='Whole388 bounded Green/tangent/variation/concavity/constant law and ordinary bounded positive mixed products. No unbounded operator or firstvariation theorem assumed.',remaining_scope=['No recognition of every transfinite unbounded psh function','No automatic bounded continuous presentation from a decreasing sequence of unbounded generated members','No unproved diagonal or decreasing-net flattening','No proof that L1 test family separates all canonical potentials or yields compactness','Numerical cubic segment energies do not identify an analytic unbounded MongeAmpere operator','No unbounded products/decreasingcontinuity/comparison/envelopes/orthogonality/arbitrarysupport existence or uniqueness theorem'],no_new_primary_or_recursive_source_reading_claim=True,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_generated_math_read_or_hot_feedback=False,protected_editor_OPEN_UNCHANGED=True,compilation='UNVERIFIED pending built-in requestcell143; no diagnostics or verifiedPDF observed',static_checks='Own environment-stack/display-delimiter/dollar-parity checks only, not compiler or mathematical verification',accepted_paper=False,new_correctness_grant=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
B.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(paper=str(P),paper_bytes=P.stat().st_size,paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),status='UNREVIEWED',solved=16,open=26,accepted=97),indent=2))
