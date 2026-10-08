from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';C=R/'campaigns/round-258/P12.3-whole-normal-surface-isolated-envelope-and-full-normalization-independent-completion';A=C/'artifacts/codex-t7x8KF'
D=K/'public-P12.3-continuation365-normal-surfaces-isolated-normal-germs-and-full-normalization-whole-candidate'
B=K/'P12.3-round258-whole-candidate365-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not B.exists()
actual=K/'round258-actual-native-final.json';assert sha(actual)=='6fea2a567df41c0ebf2e533e7dad9a6ab081d4848614dd2afb2816b583a6d28b'
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for name,e in json.loads((A/'reports/own-artifacts.json').read_text()).items():assert sha(A/name)==e['sha256'] and (A/name).stat().st_size==e['bytes']
x=json.loads(actual.read_text());n=json.loads((A/'native-notes.json').read_text());assert json.loads((A/'actual-FINAL.json').read_text())==n and n!=x and x['candidate'] is False and n['candidate'] is False
arg=(A/'argument.md').read_text();paper=(A/'P12.3-paper.md').read_text();tex=(A/'P12.3-paper.tex').read_text();checks=[]
parts=[arg]+[(A/name).read_text() for name in ['exact-scope.md','whole-source-application-ledger.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md']];assert paper=='\n\n'.join(parts)
for t,u in zip(n['notes'],x['notes']):
 assert t['id']==u['id'] and t['text']==(A/(t['id']+'.md')).read_text() and t['text'] in arg
 checks.append(dict(id=t['id'],bytes=len(t['text'].encode()),sha256=hashlib.sha256(t['text'].encode()).hexdigest(),whole_body_in_saved_note_and_argument=True,actual_equals_expanded=t['text']==u['text']))
assert len(checks)==12 and all(not e['actual_equals_expanded'] for e in checks)
table={'\\':'\\textbackslash{}','{':'\\{','}':'\\}','_':'\\_','#':'\\#','%':'\\%','&':'\\&','$':'\\$','^':'\\textasciicircum{}','~':'\\textasciitilde{}'}
def esc(s):return ''.join(table.get(c,c) for c in s)
lines=[]
for line in paper.splitlines()[4:]:
 if line.startswith('# '):lines.append('\\section*{'+esc(line[2:])+'}')
 elif line.startswith('## '):lines.append('\\subsection*{'+esc(line[3:])+'}')
 else:lines.append(esc(line))
assert '\n'.join(lines) in tex
assert sha(A/'original-task.json')==sha(C/'original-task.json')=='d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
now=datetime.now(timezone.utc).isoformat();D.mkdir()
for name in ['P12.3-paper.tex','P12.3-paper.md','argument.md','native-notes.json','whole-source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','acceptance-decision.json','original-scope-and-noncircularity-decision.md','original-task.json']+[f'n{i}.md' for i in range(1,13)]:shutil.copyfile(A/name,D/name)
shutil.copyfile(actual,D/'actual-native258-final.json');shutil.copyfile(A/'actual-FINAL.json',D/'native-artifact-actual-FINAL-expanded-DATA.json');shutil.copytree(A/'reports',D/'reports')
inert=D/'owned-native-programs-INERT';inert.mkdir()
for name in ['audit_inputs.py','reading_audit.py','read_data.py','bounded_diagnostics.py','build_delivery.py','final_audit.py']:shutil.copyfile(A/name,inert/name)
grants=D/'entire-qualified-grants';grants.mkdir();write(grants/'input-qualified-notes.json',json.loads((C/'input.json').read_text())['notes'])
for i,e in enumerate(json.loads((C/'mathematical-packet-bindings.json').read_text())[:15]):shutil.copyfile(e['path'],grants/(f'{i:02d}-'+Path(e['path']).name))
write(D/'ROOT-independent-current258-whole-body-bindings.json',dict(recorded_utc=now,checks=checks,entire_MD_components_exact=True,entire_TeX_own_escape_transcription_of_read_MD_exact=True,scope='Exactduplicate coverage, not fresh84k typesetbody reading or theoremverification'))
record=dict(recorded_utc=now,round=258,continuation=365,atom='P12.3',status='ENTIRE scoped manuscript physicallyread/source/scopechecked; independent whole365+new363364 review PENDING, original candidateFALSE; not accepted',paper=dict(path=str(D/'P12.3-paper.tex'),bytes=(D/'P12.3-paper.tex').stat().st_size,sha256=sha(D/'P12.3-paper.tex')),whole_argument=dict(path=str(D/'argument.md'),bytes=(D/'argument.md').stat().st_size,sha256=sha(D/'argument.md')),actual_final=dict(path=str(D/'actual-native258-final.json'),bytes=actual.stat().st_size,sha256=sha(actual),candidate=False,notes=12,intermediate_messages_excluded=7),ROOT_whole_reading='ENTIRE61298argument read0:17100/16700:33800/33400:50600/50200:end. EVERYrealactualFINALfield readn1-4/n5-8/n9-12 separately; ALLexpandednontextfieldsread,12mathbodiesexactargument/note files. Whole12089sourceledger/3113scope/3202coverage/2455originalscope/1429decisionphysread. CompleteMDexactconcatofallreadparts; entireTexescapedpartsbytevalidatedbyOWNexplicitmapping, fullfreshheader/footerphysread, nofreshduplicatetypesetbodyclaim.',only_grants=['ENTIREqualifiedG331','ENTIREqualifiedB341','ENTIREqualifiedE350'],mandatory_actual_expanded_qualification='ONLYactual-native258-final.json isactual49494-byte Xean settledFINAL. Nativeartifactlocalactual-FINAL equals66436-byteexpandednative-notes, andALL12actualtextsDIFFER fromexpandedtexts; bothseparatelyretainedandread. ExpandedlocalartifactrenamedexplicitlyDATA.',mandatory_historical_duplicate_qualification='Seven-note254readingreceipt isnot11current257or12new258. ROOTcurrent258full12bindingsareseparate; nativewholecurrent257 readingattributedtonative258.',primary_source_scope='Native258 fullimmediateappliedsourceunits/pixels attributedtonative258, notROOTfreshwholeduplicates. ROOTfreshcomplete0C23statement/immediateproofandENTIRE0B5S30.16.1-3, recententireBdFF1.12/2.9-2.17/2.24-2.25/3.17/4.11proofs+PDF47 readingretained. Earlierfullsurfaceimmediateunits ROOTread retained. Exactclosedaffinealgclosedchar0BFJ specialization,allcharSURFACEdimension2sourcehypotheses; allrecursivepublishedfoundations/sourcecorrections retained.',ROOT_n10_capacity_explication='Forz_j=-min(vX,j) inC, E350 symmetry/coordinate monotonicitygives F(z_j,phi)<=F(z_j,-1)=2 forEVERYcapacitytestphi in[-1,0]D. OrdinarymonotoneBorel integralinz_j yields integralvX dmu(phi)<=2; MarkovthereforeCap{vX>T}<=2/T. This suppliesexplicitreasonwhyreference momentboundherecontrolseverycapacitytest, withoutassumingz finiteenergy.',new_math='FullnormalSURFACEs allfields/char; isolatednormalclosedalgclosedchar0anydim; exactBFJsmooth; actualdominatingfinitecoverCE/nonflatnonisolatedsectors; ONECextendedUSC/netstabilityonCE; fullfinitecontinuousnormalizationMAXwithexactpositive domain; allreducedcurvesgeometricclipping; fullDdecreasingclosure beforeenergy; exactdiagnostics notnormalcounterexamples.',residual='Generalnormal>=3 outsideisolated/smooth/actual-cover sectors stillOPEN; no unconditionalextendedUSC/polenormalizationMAX. New363364ROOTlocalfinitecorrectionproofs areNOTinput/native258results.',supplied_programs_executed=False,source_bodies_pixels_LOCALONLY=True,original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-before-new-independent-review-20261008.json',record);write(B,record)
active=[]
for q in [258,259]:
 cc=next((R/f'campaigns/round-{q}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(cc/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert st['status']=='completed' and st['calls']['unsettled']==0 and not st['error']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 p=R/name;y=json.loads(p.read_text());assert len(y['fully_solved_original_atoms'])==15 and y['remaining_open_original_atoms']==27 and y['historical_reviewed_scoped_papers']==96 and y['github_pending_checkpoint'] is None
 y.update(updated_utc=now,current_active_batch=active,native258_complete365=dict(directory=str(D),binding=str(B),status=record['status'],original_closed=False),completed_native259_original_P12_6_review=dict(actual_final=str(K/'round259-actual-native-final.json'),candidate=True,status='Completedunsettled0, ENTIREROOTproof/source/scope readingPENDING, noacceptance'));p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=365,paper=record['paper'],argument=record['whole_argument'],all12actual_and_expanded_distinguished=True,all12whole_bodies_and_full_MD_TeX_bound=True,current_active_batch=active,status=record['status']),indent=2))
