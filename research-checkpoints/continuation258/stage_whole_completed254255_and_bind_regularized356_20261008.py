from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def describe(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 x=json.loads((R/name).read_text());assert x['current_active_batch']==[] and len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None
now=datetime.now(timezone.utc).isoformat();records=[]
for q,a,j,atom,title in [(254,'codex-KRber7',357,'P12.3','decreasing-completion-finite-cover-and-normal-limit-diagnostics'),(255,'codex-EJYO2w',358,'P12.6','independent-geometric-projection-full-conductor-trace-and-raw-envelopes')]:
 C=next((R/f'campaigns/round-{q}').iterdir());A=C/'artifacts'/a;D=K/f'public-{atom}-continuation{j}-{title}-unreviewed'
 assert not D.exists()
 f=json.loads((C/'freeze.json').read_text());counts={}
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
  assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
  entries=json.loads((C/name).read_text());counts[name]=len(entries)
  for e in entries:
   assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
   if 'origin' in e:assert sha(e['origin'])==e['sha256']
 assert json.loads((A/'input.json').read_text())==json.loads((C/'input.json').read_text())
 assert (A/'original-task.json').read_bytes()==(C/'original-task.json').read_bytes()
 actual=json.loads((K/f'round{q}-actual-native-final.json').read_text());expanded=json.loads((A/'native-notes.json').read_text());assert actual['candidate'] is False and expanded['candidate'] is False
 assert [n['id'] for n in actual['notes']]==[n['id'] for n in expanded['notes']]
 known=set(f['only_grants']);body=(A/('argument.md' if q==254 else 'proof.tex')).read_text();sectionbindings=[]
 for n,e in zip(actual['notes'],expanded['notes']):
  assert n['support']==e['support'] and set(n['support'])<=known;known.add(n['id'])
  p=A/(n['id']+'.md') if q==254 else A/'sections'/(n['id']+'.tex');s=p.read_text()
  assert body.count(s)==1 and e['text'].count(s)==1
  sectionbindings.append(describe(p))
 audit=json.loads((A/'evidence/input-audit.json').read_text());entries=audit['records'] if q==254 else audit['files'];assert len(entries)==sum(counts.values())
 for e in entries:
  assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
  if 'local_path' in e:assert sha(A/e['local_path'])==e['sha256']
 if q==255:
  for e in json.loads((A/'evidence/output-hashes.json').read_text()):assert (A/e['path']).stat().st_size==e['bytes'] and sha(A/e['path'])==e['sha256']
  assert (A/'proof.tex').read_text() in (A/'P12.6-paper.tex').read_text()
  for p in (A/'attachments').iterdir():assert p.read_text() in (A/'P12.6-paper.tex').read_text()
 D.mkdir()
 for p in A.iterdir():
  if p.is_file() and p.suffix in ['.md','.tex','.json','.py']:shutil.copyfile(p,D/p.name)
 for folder in ['sections','attachments']:
  if (A/folder).exists():shutil.copytree(A/folder,D/folder)
 # Native inputs and all primary/context bodies remain at their immutable LOCAL source locations.
 # Copy mathematical/grant files only; no primary source body or source pixel is staged for publication.
 if q==254:
  for folder in ['mathematical','grants']:
   if (A/'inputs'/folder).exists():shutil.copytree(A/'inputs'/folder,D/'inputs'/folder)
 E=D/'evidence';E.mkdir()
 for p in (A/'evidence').iterdir():
  if p.is_file() and p.suffix in ['.json','.md'] and p.name!='source-rendering.md':shutil.copyfile(p,E/p.name)
 for name in ['task.json','original-task.json','freeze.json','launch-record.json','qualified-imported-note-bindings.json']:shutil.copyfile(C/name,D/f'native{q}-{name}')
 shutil.copyfile(K/f'round{q}-actual-native-final.json',D/f'actual-native{q}-final.json')
 record=dict(recorded_utc=now,native_round=q,continuation=j,atom=atom,status='ENTIRE proof/source/scope and actual FINAL read; UNREVIEWED staged manuscript, originalOPEN, no accepted paper',actual_FINAL=describe(K/f'round{q}-actual-native-final.json'),native_candidate=False,notes=len(actual['notes']),only_grants=f['only_grants'],paper=describe(D/f'{atom}-paper.tex'),whole_new_proof=describe(D/('argument.md' if q==254 else 'proof.tex')),section_bindings=sectionbindings,current_frozen_bound_counts=counts,current_native_input_semantically_equal=True,expanded_whole_body_matches_and_all_outside_fields_read=True,ROOT_reading='Entire new proof physically read in overlapping bounded chunks, all actual FINAL note fields read (254n2/n7 and255n9 reading retained across continuation), full source ledger, scope, coverage and original/acceptance decisions read. Expanded entire sections match already-read bodies; every other field/footer separately read. Whole255 argument matches proof+ledger+scope. Whole255 paper header/bridges read after exact repeated bodies removed; initial outer truncation repaired by removing the already-read exact original task. No new fresh whole reading of historical duplicated grants or full255 typeset bytes claimed.',source_scope='Exact qualified G331/G345 or G331/B341/E350 only. Earlier qualified source readings preserved; native fresh complete primary applications and source pixel are attributed to native reviewer, not a new ROOT whole-source/pixel claim. Primary bodies and pixels LOCALONLY.',scope_verdict='254 general normal envelope ORIGINAL unresolved; 255 scoped mathematical proof PASS as draft, ORIGINAL stillINCONCLUSIVE for specified regularized operator. NEW ROOT355/356 are unreviewed proposed completions and require new independent reconstruction.',compiler_status='UNVERIFIED; no successful compilation. Earlier P12.5 builtin wait1010 identifier unavailable after resume and result store absent; no claim of success or still-live job.',original_closed=False,accepted_paper=False,supplied_scripts_executed_or_imported=False,protected_editor_open_unchanged=True)
 B=K/f'{atom}-round{q}-whole-candidate{j}-ROOT-proof-source-scope-and-binding-20261008.json';assert not B.exists()
 write(B,record);write(D/'mandatory-ROOT-whole-proof-source-scope-before-new-independent-review-20261008.json',record)
 records.append(dict(round=q,continuation=j,directory=str(D),binding=str(B),paper=record['paper'],original_closed=False,accepted_paper=False))
W=K/'P12.6-continuation356-specified-USC-regularized-geometric-envelopes-open-transfer-and-full-conductor-obstructions-working-proof-20261008.md'
B=K/'P12.6-continuation356-ROOT-whole-working-proof-source-scope-and-binding-20261008.json';assert not B.exists()
record=dict(recorded_utc=now,continuation=356,atom='P12.6',status='ENTIRE new working proof UNREVIEWED; no original closure or accepted paper',proof=describe(W),ROOT_reading='Entire current new source physically read in two overlapping bounded chunks without truncation. Completed255 entire new mathematical chain/source/scope read separately; byte identity is not a fresh repeated reading.',only_grants=['Entire qualified G331','Entire qualified G345'],new_results=['Specified USC-regularized geometric operator with exact greatest-positive-member criterion','Compact quotient regularization equals whole-fibre maximum; OPEN pullback equality','Continuous full-support norm/determinant kernels imply openness','Normal/no-vertical and reduced finite-flat regularized envelope compatibility and positive-domain equivalence','General full-conductor constrained regularized descent iff positive AND full-fibre constant','Closed-image and vertical positive-at-both-ends exact counterexamples','Entire all-field node regularized operator calculation and failure of geometric positivity'],whole_native255_chain_is_DATA_to_reconstruct=True,source_scope='Flat current0BD2/00HS complete statements/proofs previously ROOT-read; full determinant/Artinian/coefficient arguments reconstructed in source. No new primary PDF pixel or recursive historical-background claim.',primary_bodies_pixels_LOCALONLY=True,original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True)
write(B,record)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,completed254255_whole_staged_unreviewed=records,P12_6_ROOT356=dict(proof=record['proof'],binding=str(B),status=record['status']),compile350_recovery='Prior cell1010 not found; no result stored; compilation UNVERIFIED, no live-job or successfulPDF claim',next_work='Freeze and launch native256 ENTIRE P12.6 358+356 specified regularization, then native257 ENTIRE P12.3 357+355 normal surface and corrected354. Only full qualified grants; at most2 calls. Push258 full new proofs and frozen packets.15solved27OPEN96papers; protectededitorOPENUNCHANGED.');write(p,x)
print(json.dumps(dict(staged=records,ROOT356=record['proof'],binding=str(B),counts_unchanged=True),indent=2))
