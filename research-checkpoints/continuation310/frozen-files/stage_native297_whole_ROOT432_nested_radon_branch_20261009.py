"""Passively reconstruct and retain native297 as whole UNREVIEWED ROOT432."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
C=R/'campaigns/round-297/P16.7-whole427-whole-dirac-and-actual-analytic-representation'
A=C/'artifacts/codex-2F0f8X'
D=K/'public-P16.7-continuation432-nested-nonskeletal-radon-equations-and-fan-obstruction-unreviewed'
raw=lambda p:Path(p).read_bytes()
sha=lambda p:hashlib.sha256(raw(p)).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['current_active_batch']==[298] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==309
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
F=K/'round297-raw-native-actual-FINAL.json'
assert sha(F)=='016adb95f9971b02ec4b1f26d3047b264b51b7ebdf6098aa915d7237923697bb'
actual=load(F)
assembled=load(A/'final-notes.json')
assert actual==assembled and actual['candidate'] is False and len(actual['notes'])==4
assert all(set(n)=={'id','summary','detailedSummary','text','support'} for n in actual['notes'])
assert all(n==load(A/f'actual-{n["id"]}-all-five-fields.json') for n in actual['notes'])
artifact=load(A/'artifact-bindings.json')
for e in artifact:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
math=load(C/'mathematical-packet-bindings.json')
retained=load(A/'retained-mathematical-bindings.json')
assert len(math)==len(retained)==40
for e in retained:
    p=A/e['local']
    assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
    assert raw(p)==raw(math[e['index']]['path'])
ledger=load(A/'source-application-reading-ledger.json')
units=ledger['applied_primary_units']
private=load(C/'private-primary-packet-bindings.json')
assert len(units)==15 and ledger['incoming_correctness_grants']==[]
for e in units:
    p=Path(e['path'])
    assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
    assert e['sha256']==private[e['index']]['sha256']

# Parse syntax and accept only literal nodes; native code is never evaluated,
# executed, imported, or used as an executable implementation.
tree=ast.parse((A/'prepare_artifacts.py').read_text())
abstracts=[n.value.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='abstract' for t in n.targets) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str)]
assert len(abstracts)==1
old=Path(math[37]['path']).read_text()
paper=old[:old.index('\\title{')]+'\\title{Nested nonskeletal Radon branch equations\\\\and a translated finite-fan obstruction}\n'+old[old.index('\\author{'):]
start=paper.index('\\begin{abstract}')
end=paper.index('\\end{abstract}',start)+len('\\end{abstract}')
paper=paper[:start]+abstracts[0]+paper[end:]
paper=paper.replace('\\begin{thebibliography}{9}',(A/'new-residual-proofs.tex').read_text()+'\n\\begin{thebibliography}{9}')
assert paper.encode()==raw(A/'standalone.tex')
assert len(paper.encode())==167735 and paper.count('\n')==3376
assert raw(A/'new-residual-proofs.tex') in paper.encode()
tree=ast.parse((A/'package_artifacts.py').read_text())
def literal_list(name):
    nodes=[n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)]
    assert len(nodes)==1 and isinstance(nodes[0],ast.List)
    assert all(isinstance(v,ast.Constant) and isinstance(v.value,(str,bytes)) for v in nodes[0].elts)
    return [v.value for v in nodes[0].elts]
own=literal_list('own')
parts=literal_list('parts')
assert all(isinstance(x,str) for x in own) and all(isinstance(x,bytes) for x in parts)
for name in own:
    body=raw(A/name)
    parts.extend([f'\n===== WHOLE OWN BODY {name}; bytes={len(body)}; SHA256={hashlib.sha256(body).hexdigest()} =====\n'.encode(),body])
native=b'\n'.join(parts)
for e in sorted(retained,key=lambda e:e['bytes'],reverse=True):
    body=raw(A/e['local'])
    if body not in native:
        header=f'\n===== WHOLE SUPPLIED MATHEMATICAL INERT DATA index={e["index"]}; {e["local"]}; bytes={len(body)}; SHA256={hashlib.sha256(body).hexdigest()} =====\n'.encode()
        native+=header+body+b'\n'
assert native==raw(A/'proof-companion.txt') and len(native)==7036826
assert all(raw(A/e['local']) in native for e in retained)
for e in units:
    assert raw(e['path']) not in native
assert sha(A/'original-residual.txt')=='51185c35d2ead7f1c728e98c171c151a4364fadbe047d360f2c3539366a324a0'
assert raw(A/'unchanged-original-task.json')==raw(math[38]['path'])
D.mkdir()
public=[]
def copy(source,name):
    p=D/name
    p.write_bytes(raw(source))
    public.append(p)
    return p
for e in artifact:
    p=Path(e['path'])
    if p.name=='proof-companion.txt':
        continue
    name=('native-program-'+p.name+'.DATA.txt') if p.suffix=='.py' else p.name
    copy(p,name)
P=copy(A/'standalone.tex','P16.7-nested-radon-branch-and-fan-obstruction.tex')
copy(F,'native297-actual-FINAL-all-five-fields.json')
copy(A/'final-notes.json','native297-assembled-notes-separate-from-actual.json')
copy(K/'round297-terminal-actual-final-ROOT-retention-20261009.json','round297-terminal-actual-final-ROOT-retention-20261009.json')
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=432,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),incoming_correctness_grants=[],actual_ALLfour_ALLfivefields_physically_ROOT_read=True,actual_reading_outputs=['972b74: n1n2 allfields whole4982tokens','69e881: n3n4 allfields whole3001tokens'],actual_assembled_structurally_identical=True,all_distinct_current552LF29837B_formal_physically_ROOT_read=True,formal_reading_outputs=['5dc1b7:1-280LF whole','bac597:281-552LF whole'],unique_current_header_ledger_verdict_residual_originaltask_physically_ROOT_read=True,scope_reading_outputs=['c4d093','3e7d0d','840fbe','378275','4c260d','913e02'],ALLfive_current_native_programs_physically_ROOT_read_ONLY_DATA=True,program_reading_outputs=['f0dd10','ecbb78','d8b955'],native_programs_executed_or_imported=False,source_and_companion_passive_literal_reconstruction_exact=True,
    all15_complete_immediate_primary_units_fresh_ROOT_physically_read=units,
    primary_reading_outputs=['4fcc95: whole18.6.1 and18.6.2','db7db0: whole5.10.1-2 and14.5.2-3proofend','e6d73b:wholeGR6.1-6.5','b1b5a1:wholeCLD8.1.7-8/8.2.4carrier','e08304:productcarrier1-180','3dd8c5:productcarrier181-369','bf33ea:whole15.7.1/5.11.1/GR1.2','f4db05:whole7.2.8-13/11.6/13.8','b7214b:wholeGR4.1-4.2 andcomplete4.2carrier'],
    exact_new_primary_applications='Actual ordinary-open ratio map w1/w2 and fixedH(eta1)curve w2 use18.6.2twice, coefficient1 andprimitiveintegerdet1; translation/inversion fixedfibres preserveactualboundaries. Identity translatedtorus moment saturatedZ2 actualdegree1,CLD14.5.2-3/5.10.1(c)(d) andownconvexconvolution prove raw2! area coefficient. Fullminimalcontinuoussheaf8.1.7-8 and8.2.4; genuine recursiveproducts8.5/8.7/8.8 preserveactualcollar andlocaluniformlimits. Allcontests7.2.8-13. GR6.3/6.4 only onactualcontinuouspresentationpotentials;6.5NOTrecognition;8.6.7NOTused.',
    complete_new_scoped_deductions=['Actualmixed B(qc,qd)=delta_g+delta_xmin, anyrealdepths.', 'EveryfinitepositiveRadon depthdistributionmassM<=1 hasFULLD finite IFF S=int tail^(3/2) finite; actualoriginalCcutoffsdecrease, actualGMA=(2-M)delta_g+pushzeta, E=-1/3-S/3,D=1/6+2S/3.', 'BoundedcontinuousIFFint sqrt(tail) finite; elseactualextendedcontinuousweightinfiniteonlyrigidP withnomassP. Explicit c^-2dc on[1,infinity) givesS3,E-4/3,D13/6.', 'At qualifiedfoundationboundary allactualGuniqueness modulo constants andnonorderedcanonicalrepresentation inTHISlargerbranchsector; rawBorelnoassignedMA.', 'EVERYspecifiedoutsidequadrantfixedfiniteREALaffinemaxfan hasactualGausmass>=1, preservedweaklimits andactualGpresentations; routeobstruction only.', 'Whole2delta_x1/8 familyrestrictedobjective=3/8, NOTfullD upperbound ornonexistence.'],
    inherited_current427_standalone_137655B_and6551521Bcompanion_NOT_CURRENT_end_to_end_ROOT_read=True,whole40incoming_math_retained_NOT_reading_credit=True,native_entire_current_reading_claim_NOT_independent_ROOT_complete_audit=True,deeper_recursive_primary_book_geometry_descent_audit_INCOMPLETE=True,genuine_nonalgebraization_and_coherent_descent_NOT_certified=True,conventional_foundations='Smooth partitions/Berkovichbases/Temkingraded/Ducrosfiniteflat/intersection/WannerThuillier andfullboundedmoduli/calculus historical proof qualification retained; no conventionalfoundation convertedtoincominggrant.',residual=['Generaleligiblearbitrarysupportexistence OPEN; generaldominatedanalyticrecognition OPEN; whole2delta_x equation OPEN.', 'Actualgeneralenvelopes/variationinputs andgenuinegeometry/deeperaudit OPEN; fullP16.7 OPEN.'],native298_ACTIVE_mathematics_NOT_read_or_hotfed=True,hot_feedback=False,compiler='UNVERIFIED notyetrequested432',literal_primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
Q=D/'ROOT-whole-proof-source-application-scope-and-residual.json'
write(Q,scope)
public.append(Q)
O=D/'ROOT-desktop-compiler-observation.json'
write(O,dict(recorded_utc=now,paper=432,path=str(P),source_sha256=sha(P),compilation_verified=False,actual_builtin_compile_request_invoked=False,source_preserved=True,protected_editor_OPEN_UNCHANGED=True,no_new_tabs=True))
public.append(O)
comp=native+b'\n===== WHOLE ROOT432 source qualifications =====\n'+raw(Q)+b'\n===== WHOLE actual settled FINAL =====\n'+raw(F)+b'\n===== WHOLE ROOTcompiler observation =====\n'+raw(O)+b'\n'
T=D/'proof-companion.txt'
T.write_bytes(comp)
public.append(T)
assert all(raw(A/e['local']) in comp for e in retained)
assert all(raw(e['path']) not in comp for e in units)
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=432,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_literal_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT432_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLE432 nestednonskeletalRadonbranch equation/actualunboundedsolutions andrestrictedfanobstruction retainedafterALLactualfields/allnewformal/currentuniquescope andALL15immediateprimaryROOTreading. FulloriginalP16.7 OPEN. Prepare nextsmallP16.7native299withWHOLE432; maxTWO includingisolated298. PublishWHOLE431432regularNONFORCE310. Counts/editor unchanged; compilerunverified.')
    write(p,y)
print(json.dumps(dict(paper=432,source_bytes=P.stat().st_size,source_LF=paper.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=len(public)+1,binding=str(B),accepted=False,original_closed=False),indent=2))
