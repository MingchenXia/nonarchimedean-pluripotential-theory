from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
D=K/'public-P05.1-continuation291-compact-balanced-charts-and-independent-affine-branches'
C=R/'campaigns/round-222/P05.1-unchanged-independent-common-subspace-pages-whole-native-local-source-audit'
M=G/'upload-manifest-continuation225.json'; F=G/'continuation225-publication-records'; S=K/'small-batch220221-public-status-20261008-continuation225'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation224.json').read_text())
assert prior['commit_sha']=='4ee217d7a5a1902b7915b1008f359b8b1539a3e6' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
acc=D/'whole-mathematical-paper-acceptance-with-source-corrections-after-audit218-20261008.json'; a=json.loads(acc.read_text())
assert a['cumulative_accepted_paper_number']==83 and not a['original_closed'] and a['native_source_ledger_FAIL_retained'] and a['native_combined_FAIL_retained'] and a['native_historical_INCONCLUSIVE_retained']
for p,k in [(a['source'],'source_sha256'),(a['argument'],'argument_sha256'),(a['pdf'],'pdf_sha256'),(a['review_binding'],'review_binding_sha256'),(a['source_correction_file'],'source_correction_sha256'),(a['reader_clarifications'],'reader_clarifications_sha256')]:assert sha(p)==a[k]
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text()); assert f['whole_math_files']==33 and f['own_historical_files']==99 and f['only_grants']==['A224','B225','R230','S262','S272','S282']
working=[next(K.glob(f'P05.1-continuation{n}-*.json')) for n in [296,297]]
for p,n in zip(working,[296,297]):
    j=json.loads(p.read_text());assert j['continuation']==n and not j['new_mathematical_grant'] and not j['new_accepted_paper'] and not j['original_closed'] and j['not_supplied_to_active220221']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n in [220,221]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P05.1',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=83,original_closed=False,focus='220 unchanged isolated292 independent audit;221 dependent common-H joint-dual author. Whole295 independent audit222 frozen/unlaunched; complete291 mathematical sector accepted with boundsourcecorrections while unchangednative218 source/combinedFAIL andhistoryINCONCLUSIVE persist. WholeROOT296 cell extension and297 unbalancedboundary diagnostic are DATA.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==83 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha']==prior['commit_sha']
    j.update(updated_utc=now,current_small_batch=batch,prepared_whole295_audit222=f,new296297_unreviewed_working_proofs=dict(proofs=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in working],single_cell_scope='EXPLICITglobalLip continuousconvex endpoint on one rational polyhedron, actualaffine reference positiveonrec; nearestpoint error bound, rationalwalls properaux reference exactonwholecell, Lipschitz infextension and maxfloor, finiteREALPAmajorants exactfiniteQcontacts/samecellrec/global↓. Noallfacegluing/Lipderivation.',boundary_diagnostic_scope='Unbalancedorthant f=x+y+max(0,1-sqrt(xy)) hasboundedcontinuousconvexsame-recendpoint butEVERYfiniteREALPA error≥1/2 via(n²,0)/(n²,n^-2); originalbalancehypothesisfails, notoriginalcounterexample.',not_supplied_to_active220221=True,new_grant=False,new_accepted_paper=False,original_closed=False),next_work='On PUBLIC220/221 settlement read wholeactualFINAL and ownsource/proof/evidence beforeacceptance. Launchfrozen222 whole295audit onlywhen slotfree; no3rdnativecampaign. Then independentreview wholedependentcommonHpaper. Continuegeneralallfacegluing/globalLip proofroute with296/297DATA andother33original goals. Native218source/combinedFAIL unchanged, S291wholemath+bothclarifs distinct; builtin62/94/136pendingno duplicates/tabchanges; regularverifiedpushes.',github_pending_checkpoint=dict(continuation=225,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    j['new291_unreviewed_paper'].update(whole_mathematical_sector_accepted_with_source_corrections=True,accepted_paper_number=83,unchanged_native218_source_combined_FAIL_retained=True,acceptance_file=str(acc))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint225: corrected-source mathematical291 and new single-cell route\n\n9/42 original problems solved;33 open;83 accepted scoped/supporting mathematical papers. Whole291 mathematical sector is accepted with BOTH explicit source and reader clarifications; originalTeX/argument/ledger unchanged. Native218 geometricPASS, sourceledgerFAIL, combinedFAIL andhistoricalINCONCLUSIVE remain intact. ROOT read all7actualFINAL and all7distinctexpanded savednotes, every23coverage claim, completeunique audit/source/history fields and verified repeatedsubtree/string identity. Initialmetadata displaytruncation repaired in boundedcompactJSON, notignored. All115frozen and67ownartifact identities checked; priorROOT exact1945safe finitechecks and2localpasses/sourceGFM remain valid, no repeatedtests/builds.13pPDF confirmed. BMPS immediateweightdefinitions rational; realextension separatelyproved. BBGS full3.15 endsLF670. Correctedannotations are notrelabels ofnativeFAIL or historicalreading.\n\nWhole mathematicalscope retains precisecompactboundaryless homeomorphicpositivebalanced rationalatlas, allactualC_b componentminima/literalconstantregularity, full-affine exactrecession/ANYfiniteQinterpolation, independentpointbouquet ALLcontinuous globalREALregularization andfinitecappedroofs, plus everyfinite noncompactliteral fractional-slope obstruction. OriginalP05.1 generalized real/compact/singular/product/allfaceclassification remainsOPEN.\n\nNative220 and221 remain the boundedactivebatch, publicstatus only.222 wholeunchanged295 independentcommonH audit is frozen UNLAUNCHED:33wholemath/99ownhistory/4primary, exactly6wholegrants/allclarifs, native215historyINCONCLUSIVE retained, no newjointdual/nativeotherproof or sourcebias. Launch onlywhenPUBLICslotfree.\n\nNew296 is a full UNREVIEWED one-cell proof with an EXPLICIT globalLipschitz hypothesis. Elementarynearestpoint/active-row dependence gives dist<=H maxconstraintviolation. A realaffinecellreference plusinteger rationalconstraintpenalty is properonfullaffinespace yet EXACToriginalreference onwholecell. InfimalLipschitz extension andproperfloor produce convexF exactlymatchingf oncell andboundedrelativeauxGamma. The fullS291 affineprimalconstruction yieldsglobalREALPAmajorants andexactfiniteQcontacts; restrictions retainactualcellrecession andcommon4dyadic shifts↓ globally. AuxGamma is NOTa replacement onothercells and noMA is assignedbeforegenuineclosure. Arbitraryallfacegluing/globalLipderivation remainOPEN.\n\nNew297 gives a complete boundarydiagnostic: on unbalancedQorthant, f=x+y+max(0,1-sqrt(xy)) iscontinuousconvex boundedrelgamma=x+y withsameactualrec. Points(n²,0)/(n²,n^-2) haveperturbationdifference1 anddistn^-2; everyfinitecontinuousREALPA isglobalLip, yielding universaluniformerrorfloor1/2. The orthant violatesoriginalbalance, so NOTanoriginalcounterexample; its infiniteinwardboundaryslope cannotextendfiniteconvexacrossboundary. This explains why296cannotdiscardLip or treatindependentcellconvexityasglobalregularity. Bothwholeproofs excludedfromactive220221, nohotfeedback.\n\nBuiltin291cell62/292cell94/295cell136 pending; protectededitoropenunchanged, no duplicate/newtab. No primaryquotes/pixels/privateACTIVE/controllerstreams/authuploads; noforce pushverifieseveryblob/nativeGitTree/ref.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation225/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in sorted(D.rglob('*')):
    if not p.is_file() or 'LOCALONLY' in str(p.relative_to(D)):continue
    if p.suffix in ['.pdf','.aux','.out','.log'] and p!=D/'P05.1-paper.pdf':continue
    add(p)
add(Path(a['review_binding']))
for p in working:add(p)
for name in ['task.json','input.json','settings.json','freeze.json','original-task.json','mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:add(C/name)
for name in ['bind_mathematical291_with_source_corrections_after_audit218_20261008.py','prepare_common_subspace_whole_audit222_20261008.py','write_polyhedral_cell_extensions296_and_boundary_diagnostic297_20261008.py','record_verified224_20261008.py']:add(R/name)
add(G/'push-receipt-continuation224.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=83,commit_message='Bind whole mathematical291 with source corrections and advance single-cell approximation',scope='Whole13p mathematicalS291 acceptedwithbothsourceclarifs; unchangednative218source-combinedFAIL/historyINCONCLUSIVE retained. WholeROOT296 explicitLip singlecell and297 unbalancederrorfloor UNREVIEWED;222 whole295 auditfrozenNOTlaunched.9solved33open83accepted, native220221max2nohotfeedback; builtin62/94/136pending protectededitorunchanged. No private/primaryquote/pixel/authuploads, noforce exactblob/nativeGit/refverify.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=83),indent=2))
