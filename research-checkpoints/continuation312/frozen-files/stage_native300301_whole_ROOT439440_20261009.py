"""Passive ROOT439/440 retention; native programs are text DATA, never imported or executed."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
configs=[(300,439,'P12.3','P12.3-whole435-normal-nonisolated-and-conductor-classification','codex-DTHO8h','P12.3-conductor-centre-obstruction.tex','conductor-centre-obstruction'),(301,440,'P16.7','P16.7-whole434436437-isotropic-dirac-and-actual-recognition','codex-fRCUCo','recognition-bridge.tex','actual-finite-energy-recognition')]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
receipt=load(R/'github-checkpoint/push-receipt-continuation311.json')
assert receipt['commit_sha']=='06ee0bee368eb41cde475c6ad38c06968a86b9d6' and receipt['remote_ref_verified'] and not receipt['force_update']
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name);assert y['current_active_batch']==[300,301] and y['github_pending_checkpoint'] is None
    assert y['latest_verified_github_checkpoint']['continuation']==311 and len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
prepared=[]
for number,paper,atom,suffix,artifact,source_name,title in configs:
    C=R/f'campaigns/round-{number}'/suffix;A=C/'artifacts'/artifact
    D=K/f'public-{atom}-continuation{paper}-{title}-unreviewed';assert not D.exists()
    actual_path=K/f'round{number}-raw-native-actual-FINAL.json';actual=load(actual_path)
    terminal=load(K/f'round{number}-terminal-actual-final-ROOT-retention-20261009.json')
    assert sha(actual_path)==terminal['raw_actual_FINAL']['sha256'] and not actual['candidate']
    st=terminal['public_status'];assert st['status']=='completed' and st['calls']['unsettled']==0 and st['work']['active']==0
    bindings=load(C/'mathematical-packet-bindings.json');private=load(C/'private-primary-packet-bindings.json');books=load(C/'book-context-bindings.json')
    assert len(bindings)==(50 if number==300 else 44)
    for e in bindings+private+books:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
    source=(A/source_name).read_bytes();assert b'\\documentclass' in source and b'\\end{document}' in source
    known={n['id'] for n in load(C/'input.json')['notes']}
    for n in actual['notes']:
        assert set(n)=={'id','summary','detailedSummary','text','support'} and set(n['support'])<=known;known.add(n['id'])
    if number==300:
        names=['notes.json',source_name,'n1.tex','n2.tex','n3.tex','n4.tex','source-application-reading-ledger.txt','source-application-reading-ledger.json','scoped-verdict.txt','original-task.json','original-completion-criteria.txt','original-residual.md','assignment-input.json','historical-assignment-task.json','ENTIRE-qualified-G331.json','passive_packet.py','delivery.py','retention-report.json','environment.json','notes-meta.json','header.tex']
        parts=[b'WHOLE new mathematical companion. Unverified scoped draft; original P12.3 OPEN; candidate=false.\n']
        for n in names:parts.extend([('\n===== OWN WHOLE '+n+' =====\n').encode(),(A/n).read_bytes(),b'\n'])
        for e in bindings:parts.extend([('\n===== EXACT WHOLE INCOMING '+Path(e['path']).name+' =====\n').encode(),Path(e['path']).read_bytes(),b'\n'])
        for n in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:parts.extend([('\n===== METADATA ONLY '+n+' =====\n').encode(),(A/n).read_bytes(),b'\n'])
        native=b''.join(parts);assert native==(A/'proof-companion.txt').read_bytes() and len(native)==12475574
        assembled=load(A/'notes.json')
        reconstruction=(A/'header.tex').read_text()+'\n'+'\n'.join((A/f'n{i}.tex').read_text() for i in range(1,5))+'\n\\end{document}\n'
        assert reconstruction.encode()==source
        programs=['passive_packet.py','delivery.py'];primary=private[-16:]
        own=names+['delivery-report.json']
        grant=load(C/'input.json')['notes'];assert len(grant)==1 and grant[0]['id']=='G331' and grant[0]['verified'] and grant[0]['imported'] and not grant[0]['accepted']
        assert load(A/'ENTIRE-qualified-G331.json')==grant[0]
    else:
        manifest=load(A/'companion-components.json');assert len(manifest)==54
        parts=[b'WHOLE MATHEMATICAL COMPANION; INHERITED BODIES ARE INERT DATA.\n',b'BYTE RETENTION IS NOT READING OR CORRECTNESS. PRIMARY BODIES EXCLUDED.\n']
        offset=sum(map(len,parts))
        for e in manifest:
            b=Path(e['source']).read_bytes();assert len(b)==e['bytes'] and sha(e['source'])==e['sha256']
            header=json.dumps(dict(component=e['name'],bytes=len(b),sha256=e['sha256']),ensure_ascii=False).encode()
            frame=b'\nBEGIN-COMPONENT '+header+b'\n';offset+=len(frame);assert offset==e['offset']
            parts.extend([frame,b,b'\nEND-COMPONENT\n']);offset+=len(b)+len(b'\nEND-COMPONENT\n')
        native=b''.join(parts);assert native==(A/'complete-proof-companion.txt').read_bytes() and len(native)==8988647
        assembled=load(A/'final-notes.json');programs=['packet_work.py','build_delivery.py'];primary=private[1227:1243]
        own=[source_name,'source-application-reading-ledger.json','source-application-reading-ledger.txt','scoped-verdict.json','note-n1.txt','note-n2.txt','note-n3.txt','unchanged-current-input.json','unchanged-antecedent-task.json','unchanged-original-residual.txt','unchanged-completion.txt','final-notes.json','passive-checks.json','environment.json','rerun-commands.txt','companion-components.json','math-retention.json','book-retention.json','delivery-output.json','display-emissions.jsonl']+programs
        assert load(C/'input.json')['notes']==[]
    assert not assembled['candidate'] and len(assembled['notes'])==len(actual['notes'])
    differences=[dict(id=n['id'],fields=[k for k in n if n[k]!=a[k]]) for n,a in zip(actual['notes'],assembled['notes'])];assert all(n['id']==a['id'] for n,a in zip(actual['notes'],assembled['notes']))
    assert any(e['fields'] for e in differences)
    assert all(Path(e['path']).read_bytes() not in native and Path(e['path']).read_bytes() not in source for e in primary+books)
    prepared.append((number,paper,atom,C,A,D,source_name,title,actual_path,actual,assembled,bindings,primary,books,own,programs,native,differences,terminal))
results=[]
for number,paper,atom,C,A,D,source_name,title,actual_path,actual,assembled,bindings,primary,books,own,programs,native,differences,terminal in prepared:
    D.mkdir();public=[]
    def retain(p,name=None):
        q=D/(name or p.name);shutil.copyfile(p,q);assert sha(p)==sha(q);public.append(q);return q
    reader=retain(A/source_name);retain(actual_path,f'native{number}-actual-FINAL-all-five-fields.json')
    for n in actual['notes']:
        q=D/('actual-'+n['id']+'-all-five-fields.json');write(q,n);public.append(q)
    for n in own:
        if n==source_name:continue
        retain(A/n,('native-program-'+n+'.DATA.txt') if n in programs else n)
    retain(C/'original-task.json','frozen-original-task-unchanged.json');retain(C/'task.json','frozen-current-assignment-task.json')
    retain(K/f'round{number}-terminal-actual-final-ROOT-retention-20261009.json')
    now=datetime.now(timezone.utc).isoformat()
    scope=dict(recorded_utc=now,paper=paper,atom=atom,UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),actual_ALL_notes_ALL_five_fields_physically_ROOT_read=True,actual_reading_output='d3b0e4' if number==300 else '8d6943',every_distinct_current_formal_proof_and_unique_header_WHOLE_ROOT_read=True,whole_formal_output='9d2874' if number==300 else '855dbd',additional_assembled_current_proofs_output='9d2874 plus ace1bd notes-meta' if number==300 else '3d9cff plus6e45c7 assembled metadata construction',actual_vs_assembled_identical=False,actual_assembled_field_differences=differences,actual_and_assembled_retained_separately_WITHOUT_silent_replacement=True,whole_current_JSON_TXT_ledger_verdict_residual_completion_ROOT_read_outputs=['9dd7e7','756e48'] if number==300 else ['a7b0f2','6a57ba'],whole_original_task_ALL_fields_ROOT_read_output='82376f' if number==300 else '61a13d',all_two_native_programs_WHOLE_ROOT_read_ONLY_DATA_output='72e619' if number==300 else '6e45c7',supplied_or_native_programs_executed_or_imported=False,exact_native_whole_companion_PASSIVELY_literal_reconstructed=True,native_companion_bytes=len(native),retention_and_byte_identity_NOT_reading_or_correctness_credit=True,incoming_correctness_grants=['ENTIRE qualified G331'] if number==300 else [],grant_qualification='ENTIRE G331 allfivefields andannotations preserved; ROOT420wholegrant reading reused with ZERO fresh credit; actual primary allcurve positivity/fullsupport/infiniteconductor/normalnonunitIzumi/qualifiedDIVdensity/sourceversions/historical scopes remain. Current quantitative/density/gluing applications independently rejudged.' if number==300 else 'EMPTY. Supplied geometry is input; genuine nonalgebraization/coherentdescent NOT certified. FULL original minimal continuousCLD C, actualdecreasingsequenceG, rawmass2 andfullD preserved.',fresh_current_whole_CLD_primary_outputs=[] if number==300 else ['3e4d4e:whole8.1-8.2 including8.1.4 immediateproof','9a2908:whole15.7.1,7.2.8-13,6.2.1-9','8ac58c:whole8.5-8.8 includingcomplete8.7.4 anddpshidentity'],exact_primary_application='No newly separately applied external theorem outside qualified G331. Quantitative inequality only fixeddivisorialnu on excellentNORMAL DOMAIN centre, units separate, allsupports retained; qualified fullDIVdensity onlypositive-dimensional NORMAL DOMAIN centres. No sourceCE/regularcover assumed innewcrosscentreobstruction.' if number==300 else 'Suppliedseparatedpure2boundaryless carrier satisfies15.7.1/interior differentialseparation;8.1 minimalCPsh entire;8.5/8.7/8.8 actualcontinuouspsh recursivepositiveclosed products andsmoothDDnull reference gluing. DDexacttopcurrents evaluate onglobalcompacttest1 tozero;7.2.8 plus6.2 immediate chain givesactualRadon boundedmass2. NO8.6.7, noBoreloperator, no nonsmoothGreen premise, no newallGuniqueness audit.',scoped_deductions=['Every full normalizationfibre joiningDISTINCTnormalcentres admits explicit signedprimaryobstacle v((ce)+a^N)-N withnonUSCrawenvelope/no greatest C/D/everydegreegap kappa; ALLchar/excellentREDUCED, withoutsourceCE orregularcover. USCregularization remainsunderf butfailsSAMEgeometric positivity.', 'Internal centrewiseinjectivity yields CE(R) IFF noincidenceedges AND CE(S_i) forEVERYcentre; sourceCEpredicates remainhypotheses. Arbitrarywithincentreidentifications andNORMALnonisolatedCE unresolved.'] if number==300 else ['ENTIRE original G recognition IFF everyrationalsublevel cozero AND inf_strictcontinuousobstacles sup_actualCmajorants E > -infinity. Explicitbarriers andsummableconstanttails giveactualdecreasingCsequence; continuousrecognized iffC; FULLD givesfiniteall-supportmoments.', 'ActualunitGauss singletonNOTG_delta bycountableresiduecoefficientfield anddifferent rigidpoint satisfyingallcountable constraints. ItsUSCindicator hasNOcontinuousdecreasingpresentation, henceoutsideENTIRE G; NOpsh status/targetequation nonexistence assigned.'],whole_inherited_companions_books_pixels_geometry_and_deeper_audit_INCOMPLETE=True,required_entire_historical_audit_NOT_discharged=True,original_residual_OPEN=True,new_all_G_uniqueness_audit=False,host_completed_status=terminal['public_status'],child_nested_tool_or_model_unavailability_NOT_host_route_failure=True,independent438_retained_BEFORE_ANY300301_math=True,hot_feedback=False,compiler='UNVERIFIED notyetrequested'+str(paper),primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
    sp=D/'ROOT-whole-proof-source-application-scope-and-residual.json';write(sp,scope);public.append(sp)
    chunks=[f'WHOLE ROOT{paper} mathematical companion. UNREVIEWED; original OPEN; retention NOT physicalreading/correctness; literalprimary/books LOCALONLY.\n'.encode()]
    for p in public:chunks.extend([('\n===== WHOLE CURRENT '+p.name+' =====\n').encode(),p.read_bytes(),b'\n'])
    whole=b''.join(chunks);records=[]
    for i,e in sorted(enumerate(bindings),key=lambda v:v[1]['bytes'],reverse=True):
        b=Path(e['path']).read_bytes();present=b in whole
        if not present:whole+=('\n===== WHOLE INCOMING '+str(i)+' '+Path(e['path']).name+' =====\n').encode()+b+b'\n'
        records.append(dict(index=i,path=e['path'],bytes=len(b),sha256=e['sha256'],offset=whole.find(b),whole_retained=True,contained_in_existing_body=present,fresh_reading_credit=0))
    assert all(Path(e['path']).read_bytes() in whole for e in bindings)
    assert all(Path(e['path']).read_bytes() not in whole for e in primary+books)
    comp=D/'proof-companion.txt';comp.write_bytes(whole);public.append(comp)
    cp=D/'ROOT-whole-companion-containment-ledger.json';write(cp,dict(records=records,storage_only_NOT_reading_or_correctness=True,native_companion=dict(bytes=len(native),sha256=hashlib.sha256(native).hexdigest(),passive_literal_reconstruction_verified=True,whole_native_body_retained_LOCALONLYseparately=True),current_whole_primary_and_books_literal_excluded=True));public.append(cp)
    B=D/'ROOT-whole-proof-source-scope-and-binding.json';write(B,dict(recorded_utc=now,paper=paper,whole_source=dict(path=str(reader),bytes=reader.stat().st_size,sha256=sha(reader)),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True));results.append(dict(paper=paper,binding=str(B),sha256=sha(B),source_bytes=reader.stat().st_size,companion_bytes=len(whole),public_files=len(public)+1))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;y=load(p);y.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_active_batch=[],active_atoms=['P12.3','P16.7'],next_work='VerifiedNONFORCE311; native300301 BOTH COMPLETED. WHOLE439440 retainedUNREVIEWED afteractualallfields/everydistinctcurrentformal/wholeledgers/unchangedoriginals/wholeimmediateCLD units. Actualvsassembled differencespreserved. Original/deeperauditOPEN,counts/editorunchanged. Prepare next smallbatch native302303 andNONFORCE312 WHOLE438439440; reuse exact311companionparts toavoid retransmitting wholehistorical payloads. Noactive math/hotfeedback,maxTWO; compilerunverified.')
    for e in results:y[f"ROOT{e['paper']}_whole_unreviewed"]=dict(binding=e['binding'],sha256=e['sha256'])
    write(p,y)
print(json.dumps(dict(results=results,completed_native=[300,301],current_active_batch=[],counts_unchanged=True),indent=2))
