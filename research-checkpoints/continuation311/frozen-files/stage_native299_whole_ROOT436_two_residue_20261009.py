"""Own passive ROOT436 staging. Native/supplied programs are DATA only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, sys

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-299/P16.7-whole432-two-point-mass-and-whole-dirac'
A=C/'artifacts/codex-iX4CHY'
D=K/'public-P16.7-continuation436-two-residue-radon-and-family-limit-unreviewed'
reader=D/'P16.7-two-residue-radon-and-family-limit.tex'
raw=K/'round299-raw-native-actual-FINAL.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert sha(raw)=='7ad95061555d0712bc3afd52db34f933b4abbb56734373604c3e80befabbe850'
native_source=(A/'standalone.tex').read_text()
old='Choose units $a_1,a_2,b_1,b_2\\in K$ with\n$|a_1-a_2|=|b_1-b_2|=1$.'
new='Choose $a_1,a_2,b_1,b_2\\in K$ with\n$|a_1|=|a_2|=|b_1|=|b_2|=1$ and\n$|a_1-a_2|=|b_1-b_2|=1$.'
assert native_source.count(old)==1
corrected=native_source.replace(old,new)
primary_excerpt=R/'primary-data-LOCALONLY/P16.7-ROOT436-smooth-cutoff-density-partition-source-20261009/CLD-6.2.1-9-LF7070-7150-whole-immediate-chain-LOCALONLY.txt'
carrier=R/'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1/private-primary-DATA-LOCALONLY/004-004-CLD-literal_extract.txt'
assert sha(carrier)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
excerpt=b'\n'.join(carrier.read_bytes().split(b'\n')[7069:7150])+b'\n'
if sys.argv[1]=='prepare':
    assert not D.exists();D.mkdir()
    reader.write_text(corrected)
    primary_excerpt.parent.mkdir(parents=True,exist_ok=True);primary_excerpt.write_bytes(excerpt)
    print(json.dumps(dict(mode='prepare',source=str(reader),bytes=reader.stat().st_size,LF=corrected.count('\n'),sha256=sha(reader),reading_required_before_final=True,norm_one_explicit_correction_only=True)))
    raise SystemExit
assert sys.argv[1]=='final' and reader.read_text()==corrected and primary_excerpt.read_bytes()==excerpt
assert not (D/'ROOT-whole-proof-source-scope-and-binding.json').exists()
for n in ['active-work.json','checklist-current.json']:
    y=load(R/n);assert y['current_active_batch']==[] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==310
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
actual=load(raw);assembled=load(A/'final-notes.json')
assert actual['notes']==assembled['notes'] and actual['candidate'] is assembled['candidate'] is False and len(actual['notes'])==3
known=set()
for n in actual['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'} and set(n['support'])<=known;known.add(n['id'])
bindings=load(C/'mathematical-packet-bindings.json');private=load(C/'private-primary-packet-bindings.json');context=load(C/'book-context-bindings.json')
assert (len(bindings),len(private),len(context))==(40,1242,17)
cache={}
for e in bindings+private+context:
    if e['path'] not in cache:cache[e['path']]=(Path(e['path']).stat().st_size,sha(e['path']))
    assert cache[e['path']]==(e['bytes'],e['sha256'])
assert sha(A/'original-residual.txt')=='51185c35d2ead7f1c728e98c171c151a4364fadbe047d360f2c3539366a324a0'
assert sha(A/'unchanged-original-task.json')=='8dd54853b9d191f59be5a2e9497b895a774be1eec6b3980823fd27062fddc0ff'
assert load(C/'input.json')['notes']==[]
own=['standalone.tex','source-application-reading-ledger.json','source-application-reading-ledger.txt','scoped-verdict.json','original-residual.txt','unchanged-original-task.json','input.json','check-output.json','environment.json','commands.txt','final-notes.json']
native_parts=[b'LOCAL MATHEMATICAL DATA COMPANION. Retention is not physical reading, correctness, or a grant. Supplied program bodies are INERT DATA. All new results are unverified scoped drafts. Literal immediate primary bodies excluded.\n']
for n in own:native_parts.extend([('\nBEGIN OWN ARTIFACT '+n+'\n').encode(),(A/n).read_bytes(),('\nEND OWN ARTIFACT '+n+'\n').encode()])
for e in bindings:
    p=A/'retained-mathematical-DATA'/Path(e['path']).name
    assert p.read_bytes()==Path(e['path']).read_bytes()
    native_parts.extend([('\nBEGIN INCOMING WHOLE INERT DATA '+p.name+'\n').encode(),p.read_bytes(),('\nEND INCOMING WHOLE INERT DATA '+p.name+'\n').encode()])
native=b''.join(native_parts);assert native==(A/'proof-companion.txt').read_bytes() and len(native)==7964342
for e in load(A/'companion-component-manifest.json'):
    assert hashlib.sha256(native[e['offset']:e['offset']+e['bytes']]).hexdigest()==e['sha256']
primary=private[1227:1242]+[private[4]]
assert all(Path(e['path']).read_bytes() not in native for e in primary)
public=[reader]
def retain(p,n=None):
    q=D/(n or p.name);shutil.copyfile(p,q);assert sha(q)==sha(p);public.append(q);return q
retain(raw,'native299-actual-FINAL-all-five-fields.json');retain(A/'final-notes.json','native299-assembled-notes-separate-from-actual.json');retain(A/'standalone.tex','native-standalone-DATA.tex')
for n in actual['notes']:
    p=D/('actual-'+n['id']+'-all-five-fields.json');write(p,n);public.append(p)
for n in ['source-application-reading-ledger.json','source-application-reading-ledger.txt','scoped-verdict.json','original-residual.txt','unchanged-original-task.json','input.json','environment.json','commands.txt','check-output.json','package-output.json','delivery-check-output.json','companion-component-manifest.json','retention.json','read-displays.jsonl']:retain(A/n,'native-'+n)
for n in ['packet_tools.py','checks.py','delivery_check.py','package.py','write_notes.py']:retain(A/n,'native-program-'+n+'.DATA.txt')
retain(K/'round299-terminal-actual-final-ROOT-retention-20261009.json')
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=436,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),incoming_correctness_grants=[],actual_ALLthree_notes_ALLfivefields_physically_ROOT_read=True,actual_reading_outputs=['31978e:n1','73adce:n2','c3a7bd:n3'],actual_vs_assembled_ALLfivefields_STRUCTURALLY_IDENTICAL=True,formal_expansion564LF28650B_WHOLE_ROOT_read_outputs=['a5e8c2:LF1-280','ffc966:LF281-564'],ROOT_reader_correction='Only explicitly require |a1|=|a2|=|b1|=|b2|=1, missing from ambiguous native units-in-K wording. This is needed for claimed chart and global log-max identities. Exact native source/actual notes retained separately unchanged.',corrected_ROOT_reader_WHOLE_read=True,corrected_reader_reading_record='ROOT436 corrected source read in bounded untruncated LF1-285 and286-565 before final staging',whole_current_JSON_TXT_ledger_verdict_residual_ROOT_read_outputs=['ccea84:TXT/verdict/residual','181b01:JSONledger'],whole_original_task_and_completion_ROOT_read_outputs=['d0450a:decodedproblemLF1-120 pluscriterion','202223:LF121-230','ce4324:LF231-318'],all_five_native_programs_WHOLE_ROOT_read_ONLY_DATA_outputs=['462edf:packet_tools/checks/delivery_check','818779:package ALLchars','238d69:write_notes chars0-14400','285ffc:write_notes chars14400-end'],supplied_or_native_programs_executed_or_imported=False,native7964342B_companion_PASSIVELY_exact_byte_reconstructed=True,whole40_incoming_math_bodies_retained_NOTwhole_reading_credit=True,whole_source_and_current_scope_reading_NOTwhole_historical_audit=True,all15_complete_immediate_primary_units_reused_from432_ZEROextra_reading_credit=[dict(path=e['path'],bytes=e['bytes'],sha256=e['sha256'],LOCALONLY=True) for e in private[1227:1242]],fresh_entire_CLD6_2_1_9_statement_and_immediate_proof=dict(path=str(primary_excerpt),bytes=primary_excerpt.stat().st_size,sha256=sha(primary_excerpt),literal_LF=[7070,7150],whole_physical_reading_output='1f5b6b',LOCALONLY=True),exact_current_primary_application='15.7.1 local differential separation; compact Hausdorff paracompact domain;6.2.4-8 smooth cutoffs/density/partitions;5.11.1 empty-boundary Stokes extended by reconstructed strong-gradient uniformly closed sheaf;8.5/8.7/8.8 actual recursive products/fixed proper fibres;18.6.1/2 actual translations/inversions and determinant-one ratio maps, ALLpositive real radii, degreeone;7.2.8-13 Radon/allcontinuous tests. AppendixA anddeeperrecursivefoundations remainqualified, notfreshlyaudited.',new_scoped_deductions=['Actual two distinct norm-one residue centres, both coordinate residues different: six-slot positive GLOBAL logmax plusordinarycollar gives MA=delta_x1+delta_x2 withNOg; independent fourcorner masses each<=1 andfullenergy/dual.', 'Actual samebranch nestedmixedproducts andcrossbranchsignedidentity yieldTWOindependentRadonlaws mass<=1 each. FULLD finiteIFFsumintT_i^(3/2)finite, actualC/G presentations, E=-1/3-S/3,D=1/6+2S/3; c^-2lawonEACHbranch fullnongmass2 unboundedE-7/3,D25/6.', 'Newrestricted moving-centre family weaklimits retainmass<=1 inEACHfixedordinaryresiduebidisc. This doesNOTobstructENTIREC/G orquadraticpencil434, whichwasretainedindependentlyBEFOREnative299inspection.'],native299_child_route_statement_qualification='Actual notes n3 report no nested native/service calls exposed inside solver. This is DATA about child tools, not evidence host route failed. ROOT launch/status attest one completed official signed-in Xean nativeCodexCLI gpt-6.1-sol xhigh codex-exec call; no extra nested call required.',host_native_launch_record=load(C/'launch-record.json'),host_completed_status=load(K/'round299-terminal-actual-final-ROOT-retention-20261009.json')['public_status'],independent433434_retained_BEFORE_native299_math=True,hot_feedback=False,native_prior3376LF_standalone_only1_1100_read_and_INCOMPLETE=True,whole_inherited_companions_books_pixels_geometry_and_recursive_audit_INCOMPLETE=True,new_all_G_uniqueness_audit=False,residual=['Prescribed whole2delta_oldisotropicx1/8 remainsOPEN; generalanalyticrecognition/arbitrarysupport/envelopecompactness/fullP16.7 OPEN.', 'Genuine nonalgebraization/coherentdescent andwholedeeperauditOPEN; nooriginalclosure or acceptance.'],compiler='UNVERIFIED notyetrequested436',primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
sp=D/'ROOT-whole-proof-source-application-scope-and-residual.json';write(sp,scope);public.append(sp)
parts=[b'ENTIRE ROOT436 mathematical packet. UNREVIEWED originalP16.7 OPEN; literal primary bodies/pixels/books LOCALONLY. Retention not reading or correctness.\n']
for p in public:parts.extend([('\n===== WHOLE CURRENT '+p.name+' =====\n').encode(),p.read_bytes(),b'\n'])
whole=b''.join(parts);records=[]
for i,e in sorted(enumerate(bindings),key=lambda x:x[1]['bytes'],reverse=True):
    b=Path(e['path']).read_bytes();present=b in whole
    if not present:whole+=('\n===== WHOLE INCOMING '+str(i)+' '+Path(e['path']).name+' =====\n').encode()+b+b'\n'
    records.append(dict(index=i,bytes=len(b),sha256=e['sha256'],whole_body_retained=True,contained_in_existing_whole_body=present,fresh_reading_credit=0))
assert all(Path(e['path']).read_bytes() in whole for e in bindings)
assert all(Path(e['path']).read_bytes() not in whole for e in primary) and excerpt not in whole
comp=D/'proof-companion.txt';comp.write_bytes(whole);public.append(comp)
cp=D/'ROOT-whole-companion-containment-ledger.json';write(cp,dict(storage_only_NOTreading_or_correctness_credit=True,records=records,all16_current_primary_bodies_and_fresh6_2_chain_excluded=True,native_companion=dict(path=str(A/'proof-companion.txt'),bytes=len(native),sha256=sha(A/'proof-companion.txt'),exact_reconstruction_checked=True,whole_retained_LOCALLYseparately_notappendedagain=True)));public.append(cp)
B=D/'ROOT-whole-proof-source-scope-and-binding.json';write(B,dict(recorded_utc=now,paper=436,whole_source=dict(path=str(reader),bytes=reader.stat().st_size,sha256=sha(reader)),exact_native_source=dict(path=str(D/'native-standalone-DATA.tex'),bytes=len(native_source.encode()),sha256=sha(D/'native-standalone-DATA.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for n in ['active-work.json','checklist-current.json']:
    p=R/n;y=load(p);y.update(updated_utc=now,ROOT436_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='RetainedWHOLE436 actual299ALLthreeALLfivefields/fullcorrected565LFsource/allcurrentledgers/task/residual/5inertprograms/whole6.2cutoffchain. Independent434 remainsseparatewholequadraticpencil2Dirac. Next437 angledegeneration rigorousproof, thenfreeze nextfew native300301 andNONFORCE311 boundedsegmentedWHOLE434435436437. Counts/editor unchanged; alloriginalresiduals/deeperaudit OPEN.');write(p,y)
print(json.dumps(dict(paper=436,source_bytes=reader.stat().st_size,source_LF=corrected.count('\n'),native_companion_bytes=len(native),ROOT_companion_bytes=len(whole),public_files=len(public)+1,binding=str(B),accepted=False,original_closed=False),indent=2))
