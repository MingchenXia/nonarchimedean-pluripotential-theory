from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,difflib
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-282/P16.7-whole402403404-generated-uniqueness-and-compactness'
A=C/'artifacts/codex-1WqAv3'
D=K/'public-P16.7-continuation409-ordered-energy-gaps-and-sequence-generated-net-closure-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
raw=load(K/'round282-raw-native-actual-FINAL.json');expanded=load(A/'final-notes.json')
assert raw['candidate'] is expanded['candidate'] is False and len(raw['notes'])==len(expanded['notes'])==3
known=set();pairs=[]
for a,e in zip(raw['notes'],expanded['notes']):
    assert set(a)==set(e)=={'id','summary','detailedSummary','text','support'}
    assert a['id']==e['id'] and a['support']==e['support'] and set(a['support'])<=known
    known.add(a['id']);assert (A/(e['id']+'.txt')).read_text()==e['text']+'\n'
    pairs.append(dict(id=a['id'],fields_equal={k:a[k]==e[k] for k in a},actual_text_bytes=len(a['text'].encode()),expanded_text_bytes=len(e['text'].encode()),all_actual_five_fields_ROOT_physically_read=True,all_expanded_fields_ROOT_physically_read_as_inert_write_notes_constants=True))
paper=(A/'scoped-paper.tex').read_text();ledger=(A/'source-application-reading-ledger.txt').read_text();residual=(A/'original-residual.txt').read_text()
companion='WHOLE INDEPENDENT PROOF COMPANION\nThe following TeX is the exact complete standalone proof, including every argument.\nNo omitted appendix or external project dependency.\n\n===== COMPLETE STANDALONE TEX =====\n'+paper+'\n===== COMPLETE SOURCE/APPLICATION/READING LEDGER =====\n'+ledger+'\n===== UNCHANGED ORIGINAL RESIDUAL =====\n'+residual
assert companion==(A/'proof-companion.txt').read_text()
before='Suppose $u_k\\in\\G$ decrease with lower energy bound\n$L$.'
after='Suppose $u_k\\in\\G$ decrease and set\n$L=\\inf_k E(u_k)>-\\infty$.'
assert paper.count(before)==1;corrected=paper.replace(before,after)
assert corrected.count('\\begin{document}')==corrected.count('\\end{document}')==1
captured=load(K/'round282-terminal-actual-final-ROOT-retention-20261009.json');tails=[]
assert captured['public_status']['status']=='completed' and captured['public_status']['calls']['unsettled']==0
assert captured['campaign_result']['candidate'] is False
for a,c in zip(raw['notes'],captured['campaign_result']['notes']):
    assert all(a[k]==c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(a['text'])
    tails.append(dict(id=a['id'],tail=c['text'][len(a['text']):]))
programs=[A/x for x in ['audit_inputs.py','build_deliverables.py','component_identity.py','data_paths.py','inspect_data.py','source_extras.py','verify_progress.py','write_notes.py']]
S=R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009/GR2506.13548v2-full-LOCALONLY.txt'
assert sha(S)=='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b'
U=R/'primary-data-LOCALONLY/P16.7-ROOT409-decreasing-net-and-Shilov-source-20261009';assert not U.exists();U.mkdir()
lines=S.read_bytes().split(b'\n');units=[]
for label,lo,hi in [('GR4.2-whole-statement-proof-and-context',1116,1198),('GR6.1-6.5-whole-immediate-chain',1621,1830)]:
    p=U/(label+'.txt');p.write_bytes(b'\n'.join(lines[lo-1:hi])+b'\n')
    units.append(dict(carrier=str(S),carrier_sha256=sha(S),real_LF=[lo,hi],unit=str(p),bytes=p.stat().st_size,sha256=sha(p),ROOT_whole_immediate_body_physically_read=True,LOCALONLY=True))
now=datetime.now(timezone.utc).isoformat();D.mkdir()
(D/'native-entire-scoped-paper-DATA.txt').write_text(paper)
(D/'scoped-paper.tex').write_text(corrected)
shutil.copyfile(A/'proof-companion.txt',D/'native-entire-proof-companion-DATA.txt')
root_companion=companion.replace(paper,corrected,1)
(D/'proof-companion.txt').write_text(root_companion)
for name in ['source-application-reading-ledger.txt','original-residual.txt','scoped-verdict.json','final-notes.json','n1.txt','n2.txt','n3.txt']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round282-raw-native-actual-FINAL.json',D/'raw-native-actual-FINAL.json')
shutil.copyfile(K/'round282-terminal-actual-final-ROOT-retention-20261009.json',D/'terminal-actual-FINAL-retention.json')
clarification=dict(recorded_utc=now,scope='Explicit infimum definition already present in actual n2; no theorem expansion',native_source_sha256=sha(A/'scoped-paper.tex'),ROOT_source_sha256=sha(D/'scoped-paper.tex'),source_difference=''.join(difflib.unified_diff(paper.splitlines(True),corrected.splitlines(True),fromfile='native-entire-scoped-paper-DATA',tofile='ROOT-scoped-paper')),all_other_source_characters_preserved=True,native_actual_expanded_and_original_formal_source_preserved_separately=True,mathematical_certification=False)
write(D/'ROOT-explicit-infimum-definition-clarification.json',clarification)
audit=dict(recorded_utc=now,paper=409,round=282,UNREVIEWED=True,accepted=False,original_closed=False,all_actual_five_fields_ROOT_physically_read=True,actual_expanded_pairs=pairs,all_current887_line_formal_paper_physically_read=True,whole_current_unique_ledger_residual_physically_read=True,whole_native_and_ROOT_companion_component_identity=True,native_source_definition_clarification=clarification,ROOT_fresh_primary_units=units,native_reading_ledger_historical_claims_NOT_ROOT_recursive_reading_receipts=True,whole_historical_1219_primary_manifest_and_books_NOT_ROOT_newly_read=True,incoming_correctness_grants=[],programs_physically_read_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],native_or_supplied_programs_executed_or_imported=False,terminal_tails=tails,new_ROOT_reconstruction=['I(a,b)<=3delta by positivity and ordered cubic cocycle','Q_theta_w+theta_a(f)<=1.5I+sqrt(42CI) and Q_theta_w+theta_a(w-a)<=12C give ordered integral modulus','Ordered max presentations plus finite-full-dual bounded tests and actual full-dimensional atoms pass estimate to generated weights','Countable flattening uses all presentation pairs and summable positive shifts, defining L as real energy infimum','Energy-near-infimum sequence without cofinality; arbitrary directed upper bound j_n controls full-dimensional values; actual decreasing classical psh net and all-Shilov reconstruction determine EVERY point including poles','Directed cubic interpolation supplies MA/mixed/moving-moment continuity; strict continuous majorants and sequence L1 give arbitrary-support full-dual net L1'],named_conventional_foundations_not_recursively_reproved=['Actual CLD continuous products/Green/point-atom and bounded probe foundations with their previously qualified ROOT402403404 applications','GR classical recognition/sheaf and decreasing nets, full-dimensional Shilov boundary and affine maximum at exact scopes','Carrier analytic quotient/nonalgebraization algebraic and analytic conventional inputs; native source ledger claims remain separately qualified'],unresolved=['NONORDERED normalized energy-sublevel analytic representability/compactness','Actual arbitrary obstacle envelopes/orthogonality or sufficient replacement','Adequate intrinsic E1 identification or domain independently sufficient for variational existence','EVERY arbitrary-support prescribed positive mass2 finiteFULLdual measure existence'],Gnet_equals_original_Gseq_at_finite_energy=True,any_countable_cofinality_claim=False,any_full_original_acceptance=False,primary_bodies_pixels_book_context_LOCALONLY=True,compiler_pending=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(D/'ROOT-whole-serialization-source-application-and-scope-audit.json',audit)
(D/'ROOT-review-scope.md').write_text('Whole working paper409, UNREVIEWED. Original P16.7 remains OPEN. Actual three FINALs including ALL five fields, every distinct expanded five-field body, complete887-line current formal source and unique ledger/residual were ROOT physically read. The ordered energy-gap proof and arbitrary-decreasing-net representation were reconstructed under the stated qualified CLD/GR and carrier foundations. The same original SEQUENCE-generated G contains every finite-energy decreasing-net limit; energy selection does NOT assert countable cofinality. All points/poles are reconstructed through ALL Shilov boundaries.\n\nOne formal clarification defines L=inf_k E(u_k)>-infinity in the countable flattening paragraph, exactly as actual n2 already says. The native formal source and entire native companion remain separate unmodified DATA. The corrected complete source and complete corresponding companion differ only there; all actual/expanded versions stay separate. Whole component identity and historical ledgers are not another independent recursive source audit. Fresh whole GR4.2 and6.1--6.5 immediate bodies were ROOT read; deeper conventional hypotheses remain named. Native programs were physically read as DATA and NEVER imported/executed. Primary bodies/pixels/books LOCALONLY. Compiler pending. Counts16solved26OPEN97accepted unchanged. Nonordered compactness, intrinsic recognition, envelopes and arbitrary-support existence remain OPEN. Protected P16.4 editor OPEN UNCHANGED.\n')
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=409,round=282,whole_paper=dict(path=str(D/'scoped-paper.tex'),bytes=len(corrected.encode()),sha256=sha(D/'scoped-paper.tex')),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file()],UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=audit['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[284] and x['latest_verified_github_checkpoint']['continuation']==292
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,native282_whole_unreviewed_paper409=dict(directory=str(D),binding=str(B),sha256=sha(B)),next_work='Compile whole409. Freeze285 original P16.7 whole406407409: original Gseq arbitrary decreasing-net closure, universal Gauss bounds and fixed bounded-test UI, then NONORDERED compactness/envelopes/arbitrary-support existence. Native284 continues general P12.3. Verify regular NONFORCE293, at mostTWO, unchanged counts/editor.');write(p,x)
print(json.dumps(dict(paper=409,directory=str(D),whole_source_bytes=len(corrected.encode()),whole_source_sha256=sha(D/'scoped-paper.tex'),native_source_sha256=sha(A/'scoped-paper.tex'),terminal_tails=tails,compiler='pending',original_closed=False),ensure_ascii=False,indent=2))
