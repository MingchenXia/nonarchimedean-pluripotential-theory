from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';C=R/'campaigns/round-256/P12.6-specified-regularized-geometric-envelope-whole-original-completion';A=C/'artifacts/codex-D5Brvu'
D=K/'public-P12.6-continuation362-specified-regularized-geometric-envelope-and-full-finite-compatibility-original-candidate'
B=K/'P12.6-round256-whole-candidate362-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not B.exists()
actual=K/'round256-actual-native-final.json';assert sha(actual)=='08762a66054ebc67dc07cd782c41100a63876fa946758b83b1c5256eea89aac7'
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in json.loads((A/'evidence/final-audit.json').read_text())['artifacts']:assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
x=json.loads(actual.read_text());n=json.loads((A/'native-notes.json').read_text());localactual=json.loads((A/'actual-FINAL.json').read_text())
assert n==localactual and n!=x and n['candidate'] is True and x['candidate'] is True and [t['id'] for t in x['notes']]==[t['id'] for t in n['notes']]
arg=(A/'argument.md').read_text();tex=(A/'P12.6-paper.tex').read_text();checks=[]
for t,u in zip(n['notes'],x['notes']):
 assert t['text']==(A/'sections'/(t['id']+'.tex')).read_text() and t['text'] in arg and t['text'] in tex
 checks.append(dict(id=t['id'],entire_expanded_body_in_argument_section_and_paper=True,native_actual_equals_expanded=t['text']==u['text']))
assert len(checks)==10
grants=[];mat=json.loads((C/'mathematical-packet-bindings.json').read_text())
for p in sorted((A/'grants').iterdir()):
 if p.is_file():
  assert p.read_text() in tex and any(sha(p)==e['sha256'] and p.stat().st_size==e['bytes'] for e in mat[:14]);grants.append(dict(file=str(p),bytes=p.stat().st_size,sha256=sha(p),unchanged_qualified_component=True))
assert len(grants)==14
now=datetime.now(timezone.utc).isoformat();D.mkdir()
for name in ['P12.6-paper.tex','argument.md','native-notes.json','whole-source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','acceptance-decision.json','original-scope-and-noncircularity-decision.md','bounded-input.json']:shutil.copyfile(A/name,D/name)
shutil.copyfile(actual,D/'actual-native256-final.json');shutil.copyfile(A/'actual-FINAL.json',D/'native-artifact-actual-FINAL-expanded-DATA.json');shutil.copyfile(C/'original-task.json',D/'original-task.json')
for folder in ['sections','grants','evidence']:shutil.copytree(A/folder,D/folder)
inert=D/'owned-native-programs-INERT';inert.mkdir()
for name in ['audit_inputs.py','bounded_checks.py','inspect_source.py','build_delivery.py','final_audit.py']:shutil.copyfile(A/name,inert/name)
write(D/'ROOT-independent-current256-whole-body-bindings.json',dict(recorded_utc=now,checks=checks,qualified_grants=grants,scope='ROOTowned byte comparisons, not mathematical proofs or freshreading ofgrant duplicates'))
record=dict(recorded_utc=now,round=256,continuation=362,atom='P12.6',status='ENTIRE ORIGINAL COMPLETION CLAIM candidateTRUE, independent whole-proof/source/scope review PENDING; not accepted',source_artifacts=str(A),paper=dict(path=str(D/'P12.6-paper.tex'),bytes=(D/'P12.6-paper.tex').stat().st_size,sha256=sha(D/'P12.6-paper.tex')),whole_argument=dict(path=str(D/'argument.md'),bytes=(D/'argument.md').stat().st_size,sha256=sha(D/'argument.md')),actual_final=dict(path=str(D/'actual-native256-final.json'),bytes=actual.stat().st_size,sha256=sha(actual),candidate=True,notes=10,intermediate_messages_excluded=10),ROOT_whole_reading='Whole58,363-byteargument physically read0:16800/16400:33200/32800:49600/49200:end. EveryactualFINALfield readseparatelyn1-3/n4-6/n7-8/n9-10; outer truncationofactualn10 repaired withentire n10read. Whole9040sourceledger wasfully reread separatelyafteroutertruncation. Whole4225scope,3193coverage,1477decision,5444original-scope decision read. All expandednontextfieldsread; all10expandedmathbodies exactinargument/sections/newpaper. Newpaperfullheader/bridge/footerreadafterLONGESTFIRST removalofexact alreadyreadproof/grant bodies; nofreshduplicategrantproofreading claimed.',only_grants=['ENTIREqualifiedG331','ENTIREqualifiedG345'],new_math='SpecifiedwholeUSC E positive-domain, compactquotient/fibreMAXregularization, all-test/full-supportkernelopenness, normalNOvertical/REDUCEDflatMAXC-D/openregularizedcommutation; generalconstrainedFULLconductor iffpositiveANDfibconst; nodeEXACTE nonDreversalONE; normalVERTICAL/noninjectivepositivebothONEcounterexamples; actualPRIMARYgeometricprojection BEFOREmoduleforms/Chow/fullclosedweights/reduced varying d_P; fullconductoradmissibleONEarbitrarysourceslot viaC=(B tensorS)_red withtopdegree1; determinantflatfulladmissibility; justifiedtowers/ONEgauge includingH_c/lambda; noforcedscopecompletion.',mandatory_documentary_qualification='Native localactual-FINAL.json equals expandednative-notes.json butDIFFERS fromtheACTUAL Xean settled lastagent_message. Onlyactual-native256-final.json isthatimmutable54839-byteoutput. All10actualtextsDIFFER fromexpandedTeXprooftexts andwerephysicallyreadseparately. Nativeclaims/reportactual_expanded_fields_equal refer ONLYitslocalartifact pair, notcapturedactualnativeFINAL.',mandatory_project_scope_qualification='StatementscallingP12.5 energyunresolved meanNOTresolvedbythisP12.6paper: projectP12.5 alreadyaccepted ENTIREqualifiedE350 at96papers. It isnotaninputgrant here, andno E350theorem isimported.',primary_scope='Nativecompleteimmediateprimaryreadings/pixelSH370 attributedtonative256 only, unlessseparatelyROOTphysread; allSOURCEbodies/pixelsLOCALONLY. ExactBFJclosedaffinealgclosedchar0, correctedKeeler/SHcurrentquotient-annihilator, PRIMARY/fullSUPPORT/actualgeometry/boundedprescribedDNET/fullconductor/nonredGENERICrankexclusion retained.',original_scope='CandidateTRUE isnewclaim tojudgeimpartiallyagainstWHOLEimmutable17641-byteoriginalandfamily6.2/6.3. Positive-envelopeexistenceP12.3 separate; noacceptance/countincreasebeforeindependentwholeproofandscopeaudit.',original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True,supplied_programs_executed=False,source_bodies_pixels_LOCALONLY=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-before-new-independent-review-20261008.json',record);write(B,record)
assert (D/'original-task.json').stat().st_size==17641 and sha(D/'original-task.json')=='5dec90e839c4ca9ba081f3bfc8ef4774c433c18f47ffb4a8833b708fd8a1d3ae'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 p=R/name;y=json.loads(p.read_text());assert len(y['fully_solved_original_atoms'])==15 and y['remaining_open_original_atoms']==27 and y['historical_reviewed_scoped_papers']==96 and y['github_pending_checkpoint'] is None
 y.update(updated_utc=now,native256_complete_finite_compatibility362=dict(directory=str(D),binding=str(B),status=record['status'],original_closed=False));p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=362,paper=record['paper'],argument=record['whole_argument'],all10bodies_and14grants_bound=True,actual_expanded_distinction=True,status=record['status']),indent=2))
