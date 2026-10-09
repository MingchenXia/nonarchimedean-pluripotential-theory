"""Retain independently authored quotient proof before active296297 math inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
D = K / 'public-P12.3-continuation426-irreducible-centres-exact-filtration-and-surface-criterion-unreviewed'
P = K / 'P12.3-continuation428-finite-group-quotient-envelopes-and-norm-filtration-working-paper-20261009.tex'
Q = K / 'P12.3-continuation428-ROOT-whole-proof-source-scope-and-residual-20261009.json'
O = K / 'P12.3-continuation428-desktop-compiler-observation-20261009.json'
T = K / 'P12.3-continuation428-entire-proof-companion-20261009.txt'
B = K / 'P12.3-continuation428-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p,x: Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [296,297] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 307
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
text = P.read_text()
assert len(text.encode()) == 20229 and text.count('\n') == 394
assert '\\end{document}' in text and not any(ord(c)<32 and c not in '\n\t\r' for c in text)
grant = load(D / 'qualified-G331.json')
assert grant['id'] == 'G331' and len(grant['text'].encode()) == 93375
prior = load(D / 'ROOT-whole-proof-source-application-scope-and-residual.json')
binding426 = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert not binding426['accepted'] and not binding426['original_closed']
for e in binding426['public_files']:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
primary = R / 'primary-data-LOCALONLY/P12.3-ROOT413-algebraic-field-root-descent-source-20261009'
units = [
    ('BFJ-3.15-3.25-whole-model-envelope-and-immediate-proofs.txt',9469,'977badc4250c8fc939c4783596444879b465898abf9bf196bb7541886c425a47'),
    ('BFJ-setting-and-modification-domain.txt',2562,'5e9e6db704db66b554203c3cda46bab40c913ddc83720bf59fcc850567dfa552'),
    ('BFJ-simple-modification-domain.txt',2061,'71ee469f9c1ba566053ad5dfc91ab289009046479329e97595e3c747e6734c68')]
for n,size,h in units:
    assert (primary/n).stat().st_size == size and sha(primary/n) == h
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now,paper=428,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_394_LF_20229_byte_TeX_physically_ROOT_read=True,reading_outputs=['abc669','c977f5','75b75b'],proof_origin='Independent ROOT proof AFTER both native296297 launches, BEFORE any active296297 mathematical inspection. No hot feedback. Earlier20227-byte source physically read twice; retention guard detected one accidental formfeed in fraction, repaired before any retention mutation. Entire corrected20229-byte current source physically ROOT reread in one bounded untruncated output75b75b.',sole_correctness_grant='ENTIRE qualified G331 including ALL FIVE fields and mandatory source/model/support/radial/historical-audit qualifications. Entire body physically ROOT read420. Exact current applications rejudged; entire n3 coefficient-norm/lattice-density proof and n9 smooth BFJ all-retraction qualification physically freshly ROOT reread, outputs940fde/a20b16. Earlier current426 exact boundary/density/normal-surface sections also physically reread. No model-category equivalence inferred.',
    full_deductions=[
        'ExcellentNORMAL localDOMAIN R=S^G, excellentNORMAL semilocalDOMAIN S finiteR, finiteG of orderh; no faithfulness or invertibility ofh. Gauge aS and every marked centre/prime/infinite support preserved.',
        'Coefficient ideal of product of orbit linear forms, using finite R-MODULE generators, is generator-independent and unit-or-primary. Every source semivaluation satisfies vN_G(J)=sum_gamma gamma*w(J), by Gauss coefficient minimum on the valued quotient fraction field. No unsupported valuation-extension transitivity or defectlessness premise.',
        'Equal restriction makes finite positive orbit averages agree on EVERY boundary-power ideal gauge. Rational difference lattice separates EVERY coordinate and centre; compact density gives equal orbit supports. Full boundary VS/G is homeomorphic to VR, not merely minimal or divisorial fibres.',
        'Positive norm-one orbit trace sends actual C and actual decreasing-net D into target C/D. Finite orbit maxima dominate every source competitor and positively descend, giving exact raw envelope pullback for EVERY continuous signed target obstacle. Greatest minorants exist iff invariant pulled source obstacle has one.',
        'Complete canonical A_m argument gives equality of raw C/D suprema, EVERY-degree pointwise convergence, uniform convergence iff raw envelope continuous, and greatestD implies continuous greatestC. No finite generation used.',
        'Canonical target I_m=source J_m capR, N_G(J_m) subset I_hm, and pullh_mR<=h_mS<=pullh_hmR. Every n>=h has uniform error <=beta_floor(n/h)+(h-1)||vI1||/n whenever source invariant envelope continuous. Every positive profile constructed before limits.',
        'Every finite quotient of a smooth affine CLOSED germ over algclosedCHAR0 has universal continuous geometric envelopes in EVERYdimension. Elementary invariant-ring finiteness, normality, unique fixed-point source fibre and localized invariants proved. Example ac=b^2 times affine(d-2)-space gives NORMAL NONISOLATED singularities of everyd>=3.',
        'Completion transports actual boundary/cone/envelope via exact primary contraction, without asserting arbitrary formal-invariant/completion identity. Primary gauge transport preserves canonical ideals and positive fibre constants. DimensionTWO source application retains allfield/equalmixed qualifications, with no new highercharp/mixedCE.'],
    three_complete_immediate_BFJ_units_freshly_ROOT_physically_reread=[dict(path=str(primary/n),bytes=size,sha256=h,literal_body_LOCALONLY=True) for n,size,h in units],fresh_primary_output='3b19c4, whole untruncated immediate setting/simple-modification/BFJ3.15-3.25 statements and proofs',
    exact_BFJ_application='Published smoothAFFINE CLOSED germ over algclosedCHAR0 only. Complete3.18 proof uses REAL t=m+C and thinness bounded on FIXEDsimple dual complex, not entireboundary. Closed-simplex3.11 and ALLretraction infima extend to every support. Prior multiplier/principalization/Izumi and deeper conventional analytic sources remain disclosed; no recursive completion credit.',
    other_eleven_whole_immediate_units_and_two_formula_pixels='Retained prior413/416/422/426 reading and application qualifications; NO fresh primary reading credit. Entire426n1 and scope retained below. No literal primary body/pixel/book is published.',
    inherited_source_scope_426=prior,
    residual=['General excellent NORMAL dimension>=3 universalCE OPEN.', 'Higher-dimensional positive/mixed-characteristic regular sourceCE OPEN except stated known sectors.', 'Necessary-and-sufficient criterion for arbitrary nonnormal conductor fibres OPEN.', 'No arbitrary singular germ assumed to admit finite smooth quotient cover. Products/energy/full operators/radial CLD separate.', 'Complete deeper recursive source audit incomplete; originalP12.3 remainsOPEN.'],
    compiler='UNVERIFIED; no actual native compiler success yet',native296297_mathematics_NOT_read_or_supplied=True,hot_feedback=False,supplied_or_native_programs_executed_or_imported=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=428,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Not yet requested at retention; no success observed',source_preserved=True,local_TeX_plugin_NOT_installed=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
components=[('ENTIRE independent428 TeX',P),('ENTIRE qualifiedG331 ALLfields and qualifications',D/'qualified-G331.json'),('ENTIRE qualifiedG331 text carrier',D/'qualified-G331.txt'),('ENTIRE current426n1 normal-surface/smooth proof',D/'n1.tex'),('ENTIRE current426n1 actualALLfivefields',D/'actual-n1-all-five-fields.json'),('ENTIRE current426 source-application qualifications',D/'ROOT-whole-proof-source-application-scope-and-residual.json'),('ENTIRE unchanged originaltask',D/'original-task.json'),('ENTIRE originalcompletioncriteria',D/'original-completion-criteria.txt'),('ENTIRE unchanged originalresidual',D/'original-residual.md'),('ENTIRE428 ROOTscope',Q),('Compilerobservation UNVERIFIED',O)]
parts=['ENTIRE ROOT428 mathematical proof packet. UNREVIEWED, originalP12.3 OPEN. Primary literal bodies LOCALONLY.\n']
for title,p in components:
    parts += ['\n===== '+title+' =====\n',p.read_text(),'\n']
T.write_text(''.join(parts))
for _,p in components:
    assert p.read_bytes() in T.read_bytes()
for n,_,_ in units:
    assert (primary/n).read_bytes() not in T.read_bytes()
public = [P,Q,O,T]
write(B,dict(recorded_utc=now,paper=428,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT428_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLE independentROOT428 finite-group quotient/orbit/norm/everydegree proof physically read and retained BEFORE active296297 math inspection. Next NONFORCE308 publication. Native296297 isolated; maximumTWO, no hot feedback. Counts16/42,26OPEN,97accepted and protectededitor unchanged; compilerunverified.')
    write(p,y)
print(json.dumps(dict(paper=428,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
