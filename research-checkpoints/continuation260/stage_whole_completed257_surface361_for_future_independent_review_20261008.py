from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';C=R/'campaigns/round-257/P12.3-excellent-normal-surfaces-and-whole-residual-envelope-completion';A=C/'artifacts/codex-38fJtT'
D=K/'public-P12.3-continuation361-excellent-normal-surfaces-and-full-conductor-envelopes-unreviewed'
B=K/'P12.3-round257-whole-candidate361-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not B.exists()
actual=K/'round257-actual-native-final.json';assert sha(actual)=='11cf87db8f4ed1ca27ad30983d8e6a531b3a20506c30bd99ff36084df9b19432'
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in json.loads((A/'reports/own-artifacts.json').read_text()):assert sha(A/e['file'])==e['sha256'] and (A/e['file']).stat().st_size==e['bytes']
assert sha(A/'original-task.json')==sha(C/'original-task.json')=='d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
x=json.loads(actual.read_text());n=json.loads((A/'native-notes.json').read_text());assert x['candidate'] is False and n['candidate'] is False and [t['id'] for t in x['notes']]==[t['id'] for t in n['notes']]
arg=(A/'argument.md').read_text();tex=(A/'P12.3-paper.tex').read_text();norm=lambda s:re.sub(r'\s+',' ',s).strip()
def escaped(s):
 table={'\\':r'\textbackslash{}','_':r'\_','#':r'\#','%':r'\%','&':r'\&','$':r'\$','{':r'\{','}':r'\}','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
 return ''.join(table.get(c,c) for c in s)
def rendered(s):
 parts=re.split(r'(\\\[.*?\\\])',s,flags=re.S);out=[]
 for part in parts:
  if part.startswith(r'\['):out.append(part);continue
  for line in part.splitlines():out.append(r'\section{'+escaped(line[2:])+'}' if line.startswith('# ') else escaped(line))
 return '\n'.join(out)
checks=[]
for t,u in zip(n['notes'],x['notes']):
 assert t['text']==(A/(t['id']+'.md')).read_text() and t['text'] in arg
 assert norm(rendered(t['text'])) in norm(tex)
 checks.append(dict(id=t['id'],entire_expanded_in_whole_argument=True,entire_expanded_in_note_file=True,typeset_whole_body_explicit_escaping_whitespace_only=True,actual_equals_expanded=t['text']==u['text']))
assert arg in (A/'P12.3-paper.md').read_text()
now=datetime.now(timezone.utc).isoformat();D.mkdir()
for name in ['P12.3-paper.tex','P12.3-paper.md','argument.md','native-notes.json','whole-source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','acceptance-decision.json','original-scope-and-noncircularity-decision.md','original-task.json']+[f'n{i}.md' for i in range(1,12)]:shutil.copyfile(A/name,D/name)
shutil.copyfile(actual,D/'actual-native257-final.json')
for name in ['audit_inputs.py','reading_audit.py','bounded_diagnostics.py','build_delivery.py','final_audit.py']:
 target=D/'owned-native-programs-INERT';target.mkdir(exist_ok=True);shutil.copyfile(A/name,target/name)
for p in (A/'reports').iterdir():
 if p.is_file() and p.suffix=='.json':
  target=D/'native-evidence-DATA';target.mkdir(exist_ok=True);shutil.copyfile(p,target/p.name)
write(D/'ROOT-independent-current257-duplicate-bindings.json',dict(recorded_utc=now,checks=checks,scope='ROOT owned byte comparison, not proof/source reading. All eleven expanded bodies occur in physically read wholeargument and matchTeX viaexplicit transformation; everyactual FINAL field separatelyphysicallyread.',mandatory_historical_report_qualification='native reports/reading-duplicates.json is explicitly about SEVEN native254 historical notes. It is not a current eleven-note257 verification. Native prose is qualified accordingly; this ROOT check verifies eleven current bodies independently.'))
record=dict(recorded_utc=now,round=257,continuation=361,atom='P12.3',status='ENTIRE new manuscript UNREVIEWED; future independent whole-paper audit required; originalOPEN/noacceptance',source_artifacts=str(A),paper=dict(path=str(D/'P12.3-paper.tex'),bytes=(D/'P12.3-paper.tex').stat().st_size,sha256=sha(D/'P12.3-paper.tex')),whole_argument=dict(path=str(D/'argument.md'),bytes=(D/'argument.md').stat().st_size,sha256=sha(D/'argument.md')),actual_final=dict(path=str(D/'actual-native257-final.json'),bytes=actual.stat().st_size,sha256=sha(actual),candidate=False,notes=11,intermediate_messages_excluded=6),ROOT_whole_reading='Whole53,774-byteargument physically read0:18400/18000:36000/35600:end. Every actualFINAL field readseparatelyn1-4/n5-8/n9-11. Whole10960sourceledger,3404scope,3001coverage,1317decision,2505noncircularitydecision read. All expandednontextfieldsread; full MDextraScope/Coverage readafterexactargumentremoved. TeXheader/footer read, all11 currentmathbodies independentlymatched viaexplicit escaping/whitespace; nofreshwholeTeXphysreading orsourcepixelclaim.',only_grants=['ENTIREqualifiedG331','ENTIREqualifiedB341','ENTIREqualifiedE350'],new_math='Excellent NORMAL SURFACES allchar/imperfect/mixed: finitechosen regular models ACTUALPRIMARY viafullfibreamplicity+integralpuncturedgraph; explicitnegative-definite degree matrix/principalinverse; nefCartierpushforward/effectiveexceptionalnegativity andFULLsupportC/Dprojection; greatestMAXstablepolytope; density ->ALLcontinuousobstacles; actualONEC-netextendedUSC+decreasingobstaclenets. Entireothercurve/normalfinitecover/conductor/diagnosticproofs reconstructed.',source_scope='ExactCURRENTLipman surfacehypotheses, fullnonreducedclosedfibre, residueweighteddegrees, exactBFJclosedaffinealgclosedchar0. Nativeledger sourcefreshreading attributed to native257 only unless separately ROOTphysread. Recursivepublisheddependenciesdisclosed.',mandatory_historical_report_qualification='Native seven-note duplicateaudit is HISTORICALnative254, notcurrent11note257. ROOTown11duplicatebindingseparatelysaved.',original_scope='Arbitraryexcellentnormaldimension>=3 remainsOPEN. New360notseenbynative257. Noearlypaper/originalacceptance.',source_bodies_pixels_LOCALONLY=True,supplied_programs_executed=False,protected_editor_open_unchanged=True,original_closed=False,accepted_paper=False)
write(D/'mandatory-ROOT-whole-proof-source-scope-before-new-independent-review-20261008.json',record);write(B,record)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 p=R/name;y=json.loads(p.read_text());assert len(y['fully_solved_original_atoms'])==15 and y['remaining_open_original_atoms']==27 and y['historical_reviewed_scoped_papers']==96 and y['github_pending_checkpoint'] is None
 y.update(updated_utc=now,native257_complete_surface361=dict(directory=str(D),binding=str(B),status=record['status'],original_closed=False));p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=361,paper=record['paper'],argument=record['whole_argument'],current_all11_bodies_bound=True,status=record['status']),indent=2))
