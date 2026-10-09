"""Passive ROOT435 reconstruction; every native program is inert DATA."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,ast

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-298/P12.3-whole429430-normal-finite-cover-envelope-transfer'
A=C/'artifacts/codex-oWd0eW'
D=K/'public-P12.3-continuation435-normal-finite-cover-maxima-and-reduced-compatibility-unreviewed'
raw=K/'round298-raw-native-actual-FINAL.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and sha(raw)=='921e43007b66a33e7fef5a1ac24baec98d377cfb07def852f9b8137bda98c140'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
 y=load(R/n);assert y['current_active_batch']==[299] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==310
 assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
actual,assembled=load(raw),load(A/'notes.json')
assert actual['candidate'] is False and assembled['candidate'] is False and actual['notes']==assembled['notes'] and len(actual['notes'])==5
known={'G331'}
for n in actual['notes']:
 assert set(n)=={'id','summary','detailedSummary','text','support'} and set(n['support'])<=known
 assert (A/'notes'/(n['id']+'.tex')).read_bytes()==n['text'].encode();known.add(n['id'])
bindings=load(C/'mathematical-packet-bindings.json');private=load(C/'private-primary-packet-bindings.json');context=load(C/'book-context-bindings.json')
assert len(bindings)==50 and len(private)==1260 and len(context)==3
cache={}
for e in bindings+private+context:
 if e['path'] not in cache:cache[e['path']]=(Path(e['path']).stat().st_size,sha(e['path']))
 assert cache[e['path']]==(e['bytes'],e['sha256'])
for i,n in [(34,'original-completion-criteria.txt'),(35,'original-residual.md'),(36,'original-task.json')]:assert (A/n).read_bytes()==Path(bindings[i]['path']).read_bytes()
# Parse syntax ONLY to extract a literal; never evaluate, execute or import native code.
tree=ast.parse((A/'assemble_delivery.py').read_text())
headers=[x.value.value for x in tree.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='header' for t in x.targets) and isinstance(x.value,ast.Constant) and isinstance(x.value.value,str)]
assert len(headers)==1
source=headers[0]+'\n'.join(n['text'] for n in actual['notes'])+'\n\\appendix\n'
escape={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','|':r'\textbar{}'}
for name in ['source-application-reading-ledger.md','scoped-verdict.md']:
 source+='\\section{Exact scope attachment: '+name+'}\n'+''.join(escape.get(c,c) for c in (A/name).read_text())+'\n'
source+='\\end{document}\n'
assert source==(A/'P12.3-normal-finite-cover-transfer.tex').read_text() and len(source.encode())==55931 and source.count('\n')==830
assert sum(len(n['text'].encode()) for n in actual['notes'])==39971 and sum(n['text'].count('\n') for n in actual['notes'])==726
assert not any(ord(c)<32 and c not in '\n\r\t' for c in source)
# Literal byte reconstruction of the ENTIRE current native companion from known data.
parts=[b'ENTIRE new mathematical companion. UNVERIFIED scoped draft; original P12.3 OPEN; candidate=false. Literal primary units/pixels/books LOCALONLY.\n']
own=['notes.json','P12.3-normal-finite-cover-transfer.tex','source-application-reading-ledger.md','scoped-verdict.md','original-task.json','original-completion-criteria.txt','original-residual.md','assignment-task.json','exact_checks.py','exact-check-input.json','reports/exact-checks.json','retain_inputs.py','reconstruct_native_companion.py','assemble_delivery.py','verify_delivery.py','rerun.py','reports/environment.json','reports/input-byte-audit.json','reports/current296-field-identity.json','reports/native-companion-reconstruction.json']
for n in own:parts.extend([('\n===== OWN WHOLE '+n+' =====\n').encode(),(A/n).read_bytes(),b'\n'])
native=b''.join(parts)
extra=A/'retained-data/native296-exact-reconstructed-companion.txt'
assert extra.stat().st_size==9522630 and sha(extra)=='c03a7ca4f38348bedea8cc4f92c6ffb80fcceb7835d6d74d4242f31442b3a66a'
incoming=bindings+[dict(path=str(extra),bytes=extra.stat().st_size,sha256=sha(extra))]
for e in sorted(incoming,key=lambda e:e['bytes'],reverse=True):
 b=Path(e['path']).read_bytes()
 if b not in native:native+=('\n===== EXACT WHOLE INCOMING '+Path(e['path']).name+' =====\n').encode()+b+b'\n'
for n in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:native+=('\n===== METADATA ONLY '+n+' =====\n').encode()+(C/n).read_bytes()+b'\n'
assert native==(A/'proof-companion.txt').read_bytes() and len(native)==19803437
primary=private[-16:]
assert all(Path(e['path']).read_bytes() not in native and Path(e['path']).read_bytes() not in source.encode() for e in primary)
P=R/'primary-data-LOCALONLY/P12.3-ROOT413-algebraic-field-root-descent-source-20261009'
names=['BFJ-setting-and-modification-domain.txt','BFJ-simple-modification-domain.txt','BFJ-1.10-1.15-whole-immediate-chain.txt','BFJ-2.1-2.8-whole-immediate-chain.txt','BFJ-3.1-3.14-whole-immediate-chain.txt','BFJ-3.15-3.25-whole-model-envelope-and-immediate-proofs.txt']
assert {sha(P/n) for n in names}=={e['sha256'] for e in private[1246:1252]}
D.mkdir();public=[]
def retain(p,n=None):
 q=D/(n or p.name);shutil.copyfile(p,q);assert sha(q)==sha(p);public.append(q);return q
retain(raw,'native298-actual-FINAL-all-five-fields.json');retain(A/'notes.json','native298-assembled-notes-separate-from-actual.json')
reader=retain(A/'P12.3-normal-finite-cover-transfer.tex');retain(A/'P12.3-normal-finite-cover-transfer.tex','native-standalone-DATA.tex')
for n in actual['notes']:
 p=D/('actual-'+n['id']+'-all-five-fields.json');write(p,n);public.append(p);retain(A/'notes'/(n['id']+'.tex'))
for n in ['source-application-reading-ledger.md','scoped-verdict.md','original-residual.md','original-task.json','original-completion-criteria.txt','assignment-task.json','exact-check-input.json']:retain(A/n)
for n in ['assemble_delivery.py','reconstruct_native_companion.py','retain_inputs.py','verify_delivery.py','exact_checks.py','rerun.py']:retain(A/n,'native-program-'+n+'.DATA.txt')
for p in sorted((A/'reports').iterdir()):
 if p.is_file():retain(p,'native-report-'+p.name)
retain(K/'round298-terminal-actual-final-ROOT-retention-20261009.json')
grant=load(C/'input.json')['notes'];assert len(grant)==1 and grant[0]['id']=='G331' and grant[0]['verified'] and grant[0]['imported'] and not grant[0]['accepted']
gp=D/'ENTIRE-qualified-G331-all-fields-and-annotations.json';write(gp,grant[0]);public.append(gp)
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=435,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),actual_FINAL=dict(path=str(raw),sha256=sha(raw),ALLfive_notes_ALLfivefields_physically_ROOT_read=True,reading_outputs=['070a4f:n1n2 ALLfivefields','d2fde9:n3n4 ALLfivefields','265d00:n5 ALLfivefields']),actual_vs_assembled_ALLfivefields_STRUCTURALLY_IDENTICAL=True,actual_and_assembled_bytes_separately_retained=True,every_current_formal_note_text_BYTE_IDENTICAL_to_actual_already_fully_read=True,all_five_distinct_proofs726LF39971B_ROOT_read=True,formal_duplicate_byte_comparison_output='fbbc72; no additional physical reading credit',whole_unique_header_ledger_verdict_original_residual_completion_ROOT_read=True,scope_reading_outputs=['241bd2:WHOLEuniqueheader','8b4b4d:WHOLEledger/verdict/residual/completion','e4ac6c:originalproblemLF1-120 decoded','b21456:originalproblemLF121-231 andcriterion decoded'],initial_originaltask_JSON_display_f133e3_had_middisplay_truncation_NOwholecredit=True,all_SIX_current_native_programs_ROOT_physically_read_ONLY_DATA=True,program_reading_outputs=['de4c99:assemble/reconstruct/retain WHOLE','81d52a:verify/exact/rerun WHOLE'],supplied_or_native_programs_executed_or_imported=False,source_ROOT_passive_literal_reconstruction=True,native19803437B_companion_ROOT_passive_literal_reconstruction=True,source_math_or_separator_changes_NONE=True,sole_correctness_grant='ENTIREqualifiedG331 ALLfivefields andallannotations; verified/importedtrue acceptedfalse. Wholebody ROOTread420 retainedwithscope; exactcurrentapplications rejudged, includingn6 qualifieddivisorialdensity onDOMAINcentres. ZERO newwholegrantreadingcredit.',all_six_complete_immediate_BFJ_units_fresh_ROOT_physically_read=[dict(path=str(P/n),bytes=(P/n).stat().st_size,sha256=sha(P/n),literal_body_LOCALONLY=True) for n in names],current_primary_reading_outputs=['9de1ae:setting/simple/1.10-1.15 ENTIRE','678b17:2.1-2.8 and3.1-3.14 ENTIRE','289545:3.15-3.25 ENTIRE includingcomplete3.9/3.10 proofs'],exact_source_application='SmoothAFFINE CLOSEDalgclosedCHAR0 orits exactcompletion ONLY; realt=m+C inwhole3.18, fixedcomplexthinness, substantiveCLOSEDface3.11 andALLretractions forallnonminimal supports. Exactprimarycontraction; actualfinite-domaincover assumed not universallyconstructed. Conventionalprincipalization/multiplier-subadditivity/Izumi remainpublishedqualifieddependencies, notcompletefreshrecursiveaudit.',complete_new_scoped_deductions=['Anycharacteristic finiteDOMAINextension overexcellentNORMALlocalDOMAIN: fullfibreleastroot minimum via characteristiccoefficients labelledinseparablelengths andsupportquotientGauss, exactprimarytruncation andLCM ideal B giveONEactualnegativeAMPLE rationalprimary maximum; actualC/D preserved.', 'ExactRAW C/D envelopepullback for ALLcontinuoussignedpulledobstacles, withoutCE/Galois/group/flatness. KnownsourceCE descends; canonicalcontraction, everydegreeuniformconvergence, conditionalall-supportsourceK0/m =>targetn(K0+M1)/degree.', 'FULLconductorcriterion extends to excellentREDUCEDtargets ofarbitrarydimension/equidimensionality whennormalizationcentres havequalifyingfinitecoveredCEsources. Actualconductor-primarylocalization; GRANTEDG331n6 supportzeroDIVdensity makesfiniteconductor locusdense. GreatesttargetC/D IFFcontinuoussourceenvelopefullfibreconstant; discrepancynonUSC/everydegreegap andstable2epsilon.', 'Actualfinitecovers fromsmoothAFFINE CLOSEDalgclosedCHAR0 centres orformalcoordinates giveknownsourceCE/targetCE withNOgroup/flatness premise. Reducedcurvegeometricmin(f,0) andliteralradialdistinction reconstructed, notneworiginalclosure.'],all50_incoming_math_bodies_retained_WHOLE_NOTreading_credit=True,entire_inherited426_and429430_companions_books_pixels_and_deeper_audit_INCOMPLETE=True,native_finite_diagnostics_ONLY_DATA_observations=load(A/'reports/exact-checks.json'),residual=['GeneralNORMALnonisolatedexcellenthigherdim continuity, highercharp/mixedsourceCE, intrinsicarbitraryconductorclassification OPEN.','No universalfinitequalifyingregularcover constructed. FulloriginalP12.3/deeperaudit OPEN; products/energy/fulloperators separate.'],native299_COMPLETED_compact_ONLY_terminal_math_NOT_read=True,independent431434_retained_BEFORE298math=True,hot_feedback=False,compiler='UNVERIFIED notyetinvoked435',all16_immediate_primary_units_excluded_from_public=True,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
sp=D/'ROOT-whole-proof-source-application-scope-and-residual.json';write(sp,scope);public.append(sp)
parts=[b'ENTIRE ROOT435 mathematical packet. UNREVIEWED originalP12.3 OPEN; literal primary bodies/pixels/books LOCALONLY. Retention not reading or correctness.\n']
for p in public:parts.extend([('\n===== WHOLE CURRENT '+p.name+' =====\n').encode(),p.read_bytes(),b'\n'])
whole=b''.join(parts);records=[]
for i,e in sorted(enumerate(bindings),key=lambda x:x[1]['bytes'],reverse=True):
 b=Path(e['path']).read_bytes();present=b in whole
 if not present:whole+=('\n===== WHOLE INCOMING '+str(i)+' '+Path(e['path']).name+' =====\n').encode()+b+b'\n'
 records.append(dict(index=i,bytes=len(b),sha256=e['sha256'],whole_body_retained=True,contained_in_existing_whole_body=present,fresh_reading_credit=0))
assert all(Path(e['path']).read_bytes() in whole for e in bindings) and all(Path(e['path']).read_bytes() not in whole for e in primary)
comp=D/'proof-companion.txt';comp.write_bytes(whole);public.append(comp)
cp=D/'ROOT-whole-companion-containment-ledger.json';write(cp,dict(storage_only_NOTreading_or_correctness_credit=True,records=records,all16_complete_immediate_primary_units_excluded=True,native_companion=dict(path=str(A/'proof-companion.txt'),bytes=len(native),sha256=sha(A/'proof-companion.txt'),exact_literal_reconstruction_checked=True,complete_body_LOCALLYretained_separately_not_appendedagain=True)));public.append(cp)
B=D/'ROOT-whole-proof-source-scope-and-binding.json';write(B,dict(recorded_utc=now,paper=435,whole_source=dict(path=str(reader),bytes=reader.stat().st_size,sha256=sha(reader)),exact_native_source=dict(path=str(D/'native-standalone-DATA.tex'),bytes=len(source.encode()),sha256=sha(D/'native-standalone-DATA.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for n in ['active-work.json','checklist-current.json']:
 p=R/n;y=load(p);y.update(updated_utc=now,active_atoms=['P12.3','P16.7'],ROOT435_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLEqualified435 actual298ALLfivefields/726LFproofs/currentuniqueledger/verdict/originaltask/residual/sixinertprograms/sixwholeBFJunits read; source/native19803437Bcomp passivelyliteralreconstructed; all50incomingmathwhole. Compile435 thenfreeze smallnextbatch orinspectsettled299 afterindependent434retention. NONFORCE311 nextWHOLE434435 withboundedsegmentedtransport. Counts/editor unchanged,fulloriginalsOPEN,deeperauditincomplete,nohotfeedback,maxTWO.');write(p,y)
print(json.dumps(dict(paper=435,source_bytes=reader.stat().st_size,source_LF=source.count('\n'),native_companion_bytes=len(native),ROOT_companion_bytes=comp.stat().st_size,public_files=len(public)+1,all50_math_bodies_whole=True,all16_literal_primary_units_excluded=True,accepted=False,original_closed=False,binding=str(B)),indent=2))
