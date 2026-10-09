"""Retain an independent arbitrary-field power-cover proof before native294 math inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
D = K / 'public-P12.3-continuation422-cross-component-obstructions-and-exact-surface-gluing-unreviewed'
P = K / 'P12.3-continuation425-conductor-power-cover-dichotomy-working-paper-20261009.tex'
Q = K / 'P12.3-continuation425-ROOT-whole-proof-source-scope-and-residual-20261009.json'
O = K / 'P12.3-continuation425-desktop-compiler-observation-20261009.json'
T = K / 'P12.3-continuation425-entire-proof-companion-20261009.txt'
B = K / 'P12.3-continuation425-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [294,295] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 305
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
text = P.read_text()
assert len(text.encode()) == 17763 and text.count('\n') == 374
assert '\\end{document}' in text and not any(ord(c)<32 and c not in '\n\t\r' for c in text)
grant = load(D / 'qualified-G331.json')
assert grant['id'] == 'G331' and len(grant['text'].encode()) == 93375
prior = load(D / 'ROOT-whole-proof-source-application-scope-and-residual.json')
B423 = K / 'P12.3-continuation423-ROOT-whole-paper-source-scope-and-binding-20261009.json'
old = load(B423)
assert old['paper'] == 423 and not old['accepted'] and not old['original_closed']
for e in old['public_files']:
    assert sha(e['path']) == e['sha256']
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now,paper=425,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_374_LF_17763_byte_TeX_physically_ROOT_read_in_one_bounded_untruncated_output=True,whole_prior423_325_LF_TeX_freshly_ROOT_reread=True,sole_correctness_grant='ENTIRE qualified G331, all five fields and every mandatory model/support/radial/source/historical-audit qualification. Full body freshly ROOT read420; exact current real geometric comparison, conductor-boundary quotient/bijectivity and positive order/isometric descent applications rejudged. No current fresh primary reading credit or new complete recursive source audit.',proof_origin='Independent ROOT exponent/field/characteristic generalization AFTER native295 launch, BEFORE any native294295 mathematical inspection. Only native294 settled compact status observed after current whole source read. No hot feedback.',complete_new_deductions=[
    'Every field k and e>=2, finite free A-module ring R=A plus y times tA through t^(e-1)A, t^e=u, is an excellent irreducible local domain with a SINGLE marked regular finite normalization S and exact conductor yS. Reduced conductor quotient is k[u,s,Z] inside k[t,s,Z].',
    'If e has prime-to-characteristic part>1, a finite coefficient extension kappa contains a nontrivial e-th root zeta even when k does not. Actual centred semivaluations t=s and t=zeta*s with y=Z=0 restrict to the SAME nonminimal target support u=s^e. Source lifts distinct because t-s values infinity and1.',
    'For every dimension>=3 and integerL>2, actual signed primary-model F=-v(m)-v((y(t-s))+m^L)+v((y)+m^L) lies[-L,-1] on EVERYsupport/infiniteconductorlift. Actualprimary T_n=m^n(m^(Ln)+(y(t-s)^n)) yield q_n<=F with negative effective relativelyample Cartier presentation positive on EVERYcontractedcurve BEFORElimit.',
    'Generic normalization monomial nu(s,t-s,y,Z)=(1,L,1,1,...) gives nu(I)<=o(I) for EVERYprimaryideal via surviving pure s^order monomial. ENTIREqualified geometric comparison yields g(o)<=g(nu) for EVERY C/D, minorant at o<=-L. Finite-extension monomialray t=zeta*s,y=r,s=1 tends to o on EVERYelement, whereas sup_nq_n(v_r)=-2.',
    'No greatest C/Dminorant, same finite rawsupremum notUSC, everycontinuousminorant and EVERYcanonicaldegree uniformerror>=L-2. Failure stable if2epsilon<L-2; ALLfields includingchar2 with e3, no groundfieldroot-of-unity assumption.',
    'For purep-power e>=2 incharp, Frobenius f^e belongs downstairs gives UNIQUE all-support conductor extension w(f)=v(f^e)/e, even imperfectk. Fullnormalizationboundarybijective; C/D order/isometric/CE equivalence to regularnormalS, no higherdimpositivechartheorem inferred.',
    'For EVERYfield and EVERYexponent, omitting s,Z gives a surface with UNIQUE normalizedDVRconductorboundary. Fullbijection plus qualified excellentnormaldimTWOCE proves targetuniversalCE. Adding ONEaffinecoordinate destroysCE whenever separablepart>1; e2 outsidechar2,e3 inchar2 gives everyfieldexample.',
    'Completeformalpower-series analogues proved via SAMEfinitefree modules, explicitnormalization/conductor, all-positive genericmonomialleastterms, all-elementpathconvergence and Frobenius formula. Exactother-primary-gauge transport preservescanonicalideals and rescalesgap(L-2)/d(o).'],all_supports_including_nonminimal_and_infinite_conductor_retained=True,field_extension_only_for_constructing_actual_semivaluations_NOT_changing_original_ring=True,no_ground_field_roots_of_unity_assumed=True,normal_source_CE_NOT_used_for_failure=True,all_positive_competitors_actual_primary_models_before_limits=True,finite_or_native_programs_executed_or_imported=False,new_fresh_primary_reading_credit=0,qualified_surface_application='ENTIRE422n1 qualified normal-surface proof previously physically ROOT read; exact domainS2=k[t,y]_(origin) and its completeformalversion are excellentNORMALlocalDOMAINdimTWO overANYfield. Same14whole immediate surface/SH/BFJ units and2formula images retain prior reading/source qualifications and conventional deeper resolution/completion/gluing boundaries. Not fresh primary or recursive audit credit.',inherited_fourteen_complete_units_and_two_pixels=prior['prior_fourteen_complete_immediate_surface_SH_BFJ_units_and_two_formula_pixels'],residual=['General excellent NORMAL dimension>=3 CE remains OPEN; no normal CE counterexample.', 'Higherdimradicialcase transported to regularnormalS, whose originalchar/scope restrictions remain; no blanketpureinseparablepositiveCE claim.', 'Universal criterion for arbitrary finite conductor covers and full originalP12.3 OPEN.', 'Complete deeper recursive source/book/audit qualifications remain incomplete; products,energy,full operators separate.'],compiler='UNVERIFIED: first actual desktop request pending, cell886; no success observed',native294295_mathematics_NOT_read_or_supplied=True,hot_feedback=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=425,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=True,function_cell='886',compilation_verified=False,result='PENDING; no success/diagnostics observed',source_preserved=True,local_TeX_plugin_NOT_installed=True,protected_editor_OPEN_UNCHANGED=True))
components=[('ENTIRE independently authored425 TeX',P),('ENTIRE prior423 companion: qualifiedG331 allfields, whole422n1 surface proof and original unchanged dossier/residual',Path(old['whole_companion']['path'])),('ENTIRE prior423 whole-binding and qualifications',B423),('ENTIRE newROOT425 application/scope/residual',Q),('Actual compiler observation, UNVERIFIED',O)]
parts=['ENTIRE ROOT425 proof packet. UNREVIEWED; original P12.3 OPEN.\n']
for title,p in components:
    parts += ['\n===== '+title+' =====\n',p.read_text(),'\n']
T.write_text(''.join(parts))
assert (D / 'qualified-G331.json').read_bytes() in T.read_bytes()
assert P.read_bytes() in T.read_bytes()
public = [P,Q,O,T]
write(B,dict(recorded_utc=now,paper=425,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,ROOT425_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Independent ROOT425 whole arbitrary-field conductor-power-cover dichotomy retained/read BEFORE native294295math inspection. NONFORCE305 verified423424; next306 whole425 and qualified nextbatch. Native294 settled compact status observed, captureactualFINAL and physically read everyactual/formalfield beforeROOT426. Native295 stillisolated on actualnonskeletalequation. Originalcounts/editor unchanged; compilerunverified.')
    write(p,y)
print(json.dumps(dict(paper=425,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
