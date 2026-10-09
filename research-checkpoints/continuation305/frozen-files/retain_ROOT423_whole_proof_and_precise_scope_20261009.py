"""Retain an independently authored same-centre proof; no active native math is read."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
D = K / 'public-P12.3-continuation422-cross-component-obstructions-and-exact-surface-gluing-unreviewed'
P = K / 'P12.3-continuation423-same-centre-pinch-threefold-envelope-failure-working-paper-20261009.tex'
Q = K / 'P12.3-continuation423-ROOT-whole-proof-source-scope-and-residual-20261009.json'
O = K / 'P12.3-continuation423-desktop-compiler-observation-20261009.json'
T = K / 'P12.3-continuation423-entire-proof-companion-20261009.txt'
B = K / 'P12.3-continuation423-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [293,294] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 304
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
text = P.read_text()
assert '\\end{document}' in text and not any(ord(c)<32 and c not in '\n\t\r' for c in text)
grant = load(D / 'qualified-G331.json')
assert grant['id']=='G331' and len(grant['text'].encode())==93375
prior = load(D / 'ROOT-whole-proof-source-application-scope-and-residual.json')
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now,paper=423,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_TeX_physically_ROOT_read_in_one_bounded_untruncated_output=True,sole_correctness_grant='ENTIRE qualified G331, all five fields/body/mandatory model/support/radial/source/audit qualifications retained. Whole body freshly ROOT read420; current all-support real geometric comparison rejudged, no new recursive primary audit credit.',proof_origin='Independent ROOT construction AFTER native294 launch and BEFORE any native293294 mathematical inspection; terminal293 compact status only. No hot feedback supplied to294.',complete_new_deductions=['Every field char!=2, irreducible excellent pinch THREEFOLD R=k[u,x,y,s]/(x^2-y^2u) has finite regular LOCAL normalization S=k[t,y,s], a SINGLE marked centre, conductor yS=(y,x), and two same-centre conductor lifts over one nonminimal-support target point.', 'Actual signed primary-model F=-v(m)-v((x+ys)+m^L)+v((y)+m^L), L>2 integer, lies[-L,-1] on EVERY semivaluation support. Genuine primary T_n=m^n(m^(Ln)+(y(t+s)^n)) have actual negative effective relativelyample Cartier presentations, positive on EVERY contracted integral curve BEFORE limits, and q_n<=F EVERYWHERE.', 'Generic normal-coordinate monomial nu(s,t+s,y)=(1,L,1) satisfies nu(I)<=o(I) for EVERY primary ideal. ENTIRE geometric comparison extends g(o)<=g(nu) to all C/D; every minorant value at o<=-L.', 'Actual semivaluation ray t=s,y=r,s=1 converges on EVERY ring element to o, while sup_nq_n=-2 there. No greatest C/D minorant and raw supremum notUSC. Every continuous minorant/every canonical degree has uniform gap>=L-2; failure stable under uniform perturbations2epsilon<L-2.', 'Every dimension>=3 by adjoining variables with ALL-support formulas unchanged; no higherdim normal-source CE theorem required. Pinch surface withouts has bijective normalized conductor boundary and qualified normal-surface CE, hence affine-line product can destroy CE with normalization still localregular.', 'Arbitrary primary-gauge transport preserves canonical ideals, obstruction and scaled gap; completion transports by exact qualified G331 theorem.'],all_supports_and_infinite_conductor_values_retained=True,source_comparison_PROVED_on_every_primary_ideal_NOT_finite_weight_sample=True,all_positivity_actual_primary_models_before_limits=True,finite_or_native_programs_executed_or_imported=False,new_fresh_primary_reading_credit=0,qualified_surface_application='Two-dimensional comparison uses ENTIRE current422n1 expanded normal-surface proof, physically ROOT read this turn, with exact excellent NORMAL local DOMAIN dimTWO hypotheses satisfied by k[t,y]_(origin). Prior fourteen complete surface/SH/BFJ units/two formula pixels retain source-reading qualifications and deeper published resolution/completion/gluing foundations. Not a new recursive source proof.',inherited_fourteen_complete_units_and_two_pixels=prior['prior_fourteen_complete_immediate_surface_SH_BFJ_units_and_two_formula_pixels'],characteristic_two='The two selected lifts coincide. Purely inseparable conductor quotient gives bijective boundary transport; higherdim CE becomes the corresponding normal regular source question, no char2 failure claimed.',residual=['General excellent NORMAL dimension>=3 CE/qualifying normal failure OPEN.', 'Universal criterion for all conductor fibres and full original P12.3 envelope package OPEN.', 'Complete deeper recursive primary/book/source audit remains qualified/incomplete; products,energy,full operators separate.'],compiler='UNVERIFIED: first actual desktop source request pending, no success observed',native293294_mathematics_NOT_read_or_supplied=True,hot_feedback=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=423,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=True,compilation_verified=False,result='PENDING; no success/diagnostics observed',source_preserved=True,local_TeX_plugin_NOT_installed=True,protected_editor_OPEN_UNCHANGED=True))
components=[('ENTIRE independently authored423 TeX',P),('ENTIRE qualified G331 all five fields and mandatory scope',D / 'qualified-G331.json'),('ENTIRE current422n1 expanded canonical/normal-surface/smooth reconstruction',D / 'n1.tex'),('ENTIRE current422 inherited application/scope/reading qualifications',D / 'ROOT-whole-proof-source-application-scope-and-residual.json'),('BYTE-UNCHANGED original task/family dossier',D / 'ROOT-unchanged-original-task.json'),('BYTE-UNCHANGED original residual',D / 'original-residual.md'),('ENTIRE newROOT423 application/scope/residual',Q),('Actual compiler observation, UNVERIFIED',O)]
parts=['ENTIRE ROOT423 proof packet. UNREVIEWED; original P12.3 OPEN.\n']
for title,p in components:
    parts += ['\n===== '+title+' =====\n',p.read_text(),'\n']
T.write_text(''.join(parts))
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=423,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,ROOT423_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Independent ROOT423 whole same-centre irreducible pinch-threefold proof retained and read; original P12.3 still OPEN. Native293 terminal compact status observed, capture actual FINAL and fully read before ROOT424/next P16.7 batch; native294 remains isolated, no math or hot feedback. NONFORCE304 verified; next305 includes whole423 and next qualified batch. Compiler unverified, counts/editor unchanged.')
    write(p,y)
print(json.dumps(dict(paper=423,source_bytes=P.stat().st_size,source_LF=len(text.splitlines()),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
