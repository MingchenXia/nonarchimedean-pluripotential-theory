"""Retain whole independent431 before any settled297 mathematics inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
P=K/'P12.3-continuation431-normal-finite-cover-maxima-and-envelope-transfer-working-paper-20261009.tex'
Q=K/'P12.3-continuation431-ROOT-source-scope-and-residual-20261009.json'
O=K/'P12.3-continuation431-desktop-compiler-observation-20261009.json'
T=K/'P12.3-continuation431-entire-proof-companion-20261009.txt'
B=K/'P12.3-continuation431-ROOT-whole-paper-source-scope-and-binding-20261009.json'
D=K/'public-P12.3-continuation430-formal-group-quotients-and-wild-separable-conductors-unreviewed'
G=K/'public-P12.3-continuation426-irreducible-centres-exact-filtration-and-surface-criterion-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['current_active_batch']==[298] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==309
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
text=P.read_text()
assert len(text.encode())==17055 and text.count('\n')==341 and '\\end{document}' in text
assert not any(ord(c)<32 and c not in '\n\t\r' for c in text)
old=load(D/'ROOT-whole-proof-source-scope-and-binding.json')
assert not old['accepted'] and not old['original_closed']
for e in old['public_files']:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
prior=load(D/'ROOT-whole-proof-source-application-scope-and-residual.json')
units=prior['all_six_complete_immediate_BFJ_units_freshly_ROOT_physically_reread']
assert len(units)==6
for e in units:
    assert e['literal_body_LOCALONLY'] and sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=431,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_source_ROOT_physically_read=True,reading_outputs=['fce57d: whole source before compaction','9ec816: whole17055B341LF source after context recovery,4264tokens untruncated'],proof_origin='Independent ROOT derivation AFTER native298 launch, BEFORE any active298 mathematics or any settled297 mathematics inspection. No hot feedback.',sole_correctness_grant='ENTIRE qualifiedG331 ALLFIVEfields with all source/model/support/radial/historical-audit qualifications, unchanged complete JSON and text retained. Full carrier previously ROOTread420; exact n3 freshROOTread b63015 before431 authorship, current applications rejudged.',
    complete_new_deductions=[
        'Finite DOMAIN extension of excellentNORMALlocalDOMAIN target, all semilocal source centres, any characteristic and inseparability: full fibre min(wJ)=min_l v(C_l(J))/l via R-MODULE characteristic polynomial, unique product of ALL least-valued roots, quotient Gauss evaluation after killing support.',
        'Intermediate coefficient ideals may be zero/nonprimary; ACTUAL D_l=C_l+a^(Nl) primary/unit truncations prove full fibreMAX of negative source primary profile is finiteMAX of negative target actualAMPLE primary profiles.',
        'Full fibreMAX preserves independently geometric C and actual decreasing-net D including partial/all bottom; uniform contraction, left adjunction to pullback, least fibreconstant majorant, idempotence. Ordinary full fibreMAX continuity for ALLcontinuoussigned functions by integer-weight finite-trace Lp uniform limit, separate from positivity.',
        'Exact raw C and D envelope pullback for EVERYsignedcontinuoustarget obstacle, without group or flatness or any sourceCE assumption. Source raw envelope is automatically FULLfibreconstant. Greatest C/D exists target IFF pulled source obstacle greatest exists; known actual sourceCE descends.',
        'Raw Jensen inequality for arbitrary signedcontinuoussource obstacle; finite-domain towers compose maxima where targets/intermediate normal, with extended base gauges.',
        'Exact canonical contraction I_m=J_mcapR; generic-degree norm coefficient ideal contained I_nm by EVERYtargetcanonical test; everydegree uniform error beta_floor(N/n)+(n-1)||vI1||/N and all-degree source-model bound n(K0+||vI1||)/N. No false conjugates-in-Jm premise, no arbitrarycontinuousrate or FG.',
        'Every actually supplied smoothAFFINE CLOSEDalgclosedCHAR0 finite regular source, and exact formal power-series source viaG331completion, gives target universalCE with no groupaction/flatness. No arbitrarynormalgerm assumed to admit finite regularcover.'],
    current430_n1_and_scope_whole_ROOT_reread='86757e: whole8832B n1 canonical/smooth proof and8082B scope; complete applications rejudged',
    immediate_BFJ_units_reused_with_zero_new_primary_reading_credit=units,
    previous_complete_primary_reading_outputs=prior['current_primary_reading_outputs'],
    exact_BFJ_application=prior['exact_source_application'],
    normal_target_trace_boundary='ENTIRE G331 n3: generic inseparable length q, positive integer FULLfibre support weights, semilocal allcentres, allsupports quotient-fields first, integrality over NORMALtarget and compact gauge-lattice density. No defectless valuation formula or valuation-transitivity blackbox.',
    normality_essential=True,arbitrary_finite_regular_cover_NOT_assumed=True,
    gauge_completion='Bounded positive continuous common fibreconstant denominator transports profiles/max/envelopes/canonicaltests; canonical ideals unchanged for transported obstacle. ExactG331 boundary/cone completion homeomorphism only, no arbitrarymodelcategory/formalinvariantidentity.',
    residual=['General excellentNORMAL dimension>=3 remainsOPEN; higherdim positive/mixed regular-source universalCE remainsOPEN.', 'Intrinsic universal conductor classification and full originalP12.3 remainOPEN.', 'Products/energy/fulloperators/literal radial comparison separate; deeper recursive source/book/pixel audit incomplete.'],
    compiler='UNVERIFIED, not yet requested431 at retention',native297_mathematics_NOT_read=True,native298_ACTIVE_mathematics_NOT_read=True,hot_feedback=False,supplied_or_native_programs_executed_or_imported=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=431,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Not yet requested at retention; no success observed',source_preserved=True,no_local_TeX_plugin=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
components=[('ENTIRE independent431 proof',P),('ENTIREqualifiedG331 ALLfivefields JSON',G/'qualified-G331.json'),('ENTIREqualifiedG331 complete text',G/'qualified-G331.txt'),('ENTIREcurrent430 n1 canonical and smooth proof',D/'n1.tex'),('ENTIREcurrent430 reading ledger',D/'source-application-reading-ledger.md'),('ENTIREcurrent430 scoped verdict',D/'scoped-verdict.md'),('ENTIREcurrent430 ROOTsource qualifications',D/'ROOT-whole-proof-source-application-scope-and-residual.json'),('ENTIREunchanged original task',D/'original-task.json'),('ENTIREoriginal completion criteria',D/'original-completion-criteria.txt'),('ENTIREcurrent original residual',D/'original-residual.md'),('ENTIRE429 source-scope qualifications',K/'P12.3-continuation429-ROOT-whole-proof-source-scope-and-residual-20261009.json'),('ENTIRE431 scope and residual',Q),('Compiler observation UNVERIFIED',O)]
parts=['ENTIRE ROOT431 mathematical proof packet. UNREVIEWED, originalP12.3 OPEN. Complete primary bodies/pixels/books LOCALONLY.\n']
for title,p in components:
    parts.extend(['\n===== '+title+' =====\n',p.read_text(),'\n'])
T.write_text(''.join(parts))
body=T.read_bytes()
for _,p in components:
    assert p.read_bytes() in body
for e in units:
    assert Path(e['path']).read_bytes() not in body
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=431,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],components=[dict(title=title,path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for title,p in components],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],retention_is_NOT_reading_or_correctness_credit=True,primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT431_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Independent WHOLE431 normal finite-cover maxima/exact raw envelope transfer/everydegree norm bounds retained BEFORE settled297 mathematical inspection. NONFORCE309 verified WHOLE429430/frozen298. Capture only settled297 actualFINAL; active298 remains isolated; maxTWO native; counts/editor unchanged. Compiler431 unverified.')
    write(p,y)
print(json.dumps(dict(paper=431,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
