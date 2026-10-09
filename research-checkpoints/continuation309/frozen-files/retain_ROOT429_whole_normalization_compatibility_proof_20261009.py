"""Retain independent compatibility proof before settled296 mathematical inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
P=K/'P12.3-continuation429-normalization-envelope-compatibility-and-fibre-gap-working-paper-20261009.tex'
Q=K/'P12.3-continuation429-ROOT-whole-proof-source-scope-and-residual-20261009.json'
O=K/'P12.3-continuation429-desktop-compiler-observation-20261009.json'
T=K/'P12.3-continuation429-entire-proof-companion-20261009.txt'
B=K/'P12.3-continuation429-ROOT-whole-paper-source-scope-and-binding-20261009.json'
B428=K/'P12.3-continuation428-ROOT-whole-paper-source-scope-and-binding-20261009.json'
D=K/'public-P12.3-continuation426-irreducible-centres-exact-filtration-and-surface-criterion-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['current_active_batch']==[296,297] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==308
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
text=P.read_text()
assert len(text.encode())==16407 and text.count('\n')==314 and '\\end{document}' in text
assert not any(ord(c)<32 and c not in '\n\t\r' for c in text)
old=load(B428)
assert not old['accepted'] and not old['original_closed']
for e in old['public_files']:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=429,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current314LF16407byte_TeX_physically_ROOT_read=True,reading_output='947f0c, entire corrected final source bounded untruncated',earlier310LFsource_whole_read='62751f',proof_origin='Independent ROOT proof after native296297 launches BEFORE any mathematical inspection/hot feedback. Only compact296completed/297running status observed17:20:01UTC AFTER current whole source read. Settled296 mathematics still NOT read at retention.',
    sole_correctness_grant='ENTIRE qualifiedG331 ALLFIVEfields and mandatory model/support/radial/source/historical-audit qualifications, full body previously ROOTread420, exact current boundary singleton/conductor/fullfibre positive descent/primary comparison/completion/gauge applications rejudged. WHOLE428 companion retains ENTIREcarrier and all426n1/currentqualifications/originaltask/residual.',
    complete_new_deductions=[
        'Any excellentlocalDOMAIN with finite normal semilocalDOMAIN normalization and nonzero conductor: pullpR<=pS EVERYsupport, equality on EVERYfinite-conductor point, WITHOUTsourceCE.',
        'Explicit ACTUALtarget primary/unit ideals B_n=conductor J_m^n + a^(mnM) containedR give max(q_m-wconductor/(mn),-M) <=pullf ALLsupports including infiniteconductor. Positive negative-effective relativelyample primary presentations built before limits.',
        'If finite-conductor locus dense AND source envelope continuous, greatest targetC/D exists IFF source envelope constant on EVERYfullrestrictionfibre. SourcepositiveCdescent genuinelyused, notjusttopologicaldescent/minimumpositivity.',
        'Fibre discrepancyDelta forces nonUSCjump>=Delta and uniformerror>=Delta for EVERYdecreasing-completedDminorant including EVERYcanonicaldegree; noFG follows. SourceuniversalCE gives perturbationgap>=Delta-2epsilon.',
        'Complete smoothCLOSED source density proof in ANYcharacteristic: formalcoordinate recursion with invertibleJacobian, completevalued supportQUOTIENT field, actualtranslatedradiusrGauss norm after radius-sigma analytictranslation automorphism, weightedassociatedgraded domain multiplicativity, faithful all-series injection, all-element limit including infinity and exactpositive boundarynormalization. No merelydivisorial/finitecoordinate density claim.',
        'Thus arbitrary conductor geometry with normalization centres smoothAFFINE CLOSED overalgclosedCHAR0 has exact obstacle-by-obstacle compatibility criterion using qualifiedBFJ sourceCE onfiniteproduct. Samecentre anddifferentcentres bothallowed.',
        'CanonicalrawC/D equality, everydegreepointwise/uniformcriterion, fullgapFG implication and gaugegapDelta/d(v) reconstructed. Completion retains exactG331 qualifications.'],
    entire426n1_freshly_ROOT_reread_output='c146b3: complete4470-token untruncated source proof',fresh_primary_reading_credit=0,three_complete_immediate_BFJ_units='Fresh ROOT4283b19c4 reading REUSED with exact applications rejudged; no additional reading credit. Real t=m+C, fixedcomplexthinness, substantivelyclosed-simplex continuity and ALLretraction infima remain.',
    other_immediate_units_and_pixels='All prior qualified source reading retained through whole428 companion; no new whole-book/recursiveaudit or primary credit.',
    density_domain='Smooth closed germ with coefficientfieldk and formal coordinates k[[z]], algclosedk, ANYcharacteristic. No density inferred merelyfromnormality for arbitraryother sources.',
    general_criterion_domain='Explicit assumptions continuous normal-source envelope and dense finite-conductor locus; no arbitrarynormal higherdimCE inferred.',
    residual=['Intrinsic ring classification for arbitrary conductor covers remainsOPEN; universalcriterion quantifies compatibility of ALLpulled obstacles.', 'General excellentNORMALdim>=3 and highercharp/mixed sourceCE remainOPEN.', 'Full originalP12.3, products/energy/fulloperators/radial targets and complete deeperrecursiveaudit remainOPEN.'],
    compiler='UNVERIFIED, not yet requested for429 at retention',native296297_mathematics_NOT_read_or_supplied=True,hot_feedback=False,supplied_or_native_programs_executed_or_imported=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=429,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Not yet requested at retention; no success observed',source_preserved=True,no_local_TeX_plugin=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
parts=['ENTIRE ROOT429 mathematical proof packet. UNREVIEWED, originalP12.3 OPEN. Literal primary bodies LOCALONLY.\n']
components=[('ENTIRE independent429 TeX',P),('ENTIRE428 mathematical companion with ENTIREG331 ALLfields and exact426n1/originalscope',Path(old['whole_companion']['path'])),('ENTIRE428 binding and source qualifications',B428),('ENTIRE429 scope and residual',Q),('Compilerobservation UNVERIFIED',O)]
for title,p in components:
    parts += ['\n===== '+title+' =====\n',p.read_text(),'\n']
T.write_text(''.join(parts))
for _,p in components:
    assert p.read_bytes() in T.read_bytes()
assert (D/'qualified-G331.json').read_bytes() in T.read_bytes()
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=429,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT429_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLEindependentROOT429 conductor localization/normal envelope compatibility/allD gap/smooth closed fullsupport density physically read and retained BEFORE settled296 mathematics inspection. NONFORCE308 verified428. Capture actual296 FINAL, physically read allfields/allformal/exactsources before qualifiedROOT430 and nextP12.3batch. Native297 stillisolated active; maximumTWO; counts/editor unchanged.')
    write(p,y)
print(json.dumps(dict(paper=429,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
