from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,re
R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation394-curve-restrictions-of-generated-weights-working-paper-20261009.tex'
B=K/'P16.7-continuation394-ROOT-whole-proof-source-scope-and-binding-20261009.json'
S=R/'primary-data-LOCALONLY/P16.7-curve-test-Wanner-primary-20261009'
F=R/'shared-sources/Wanner-1801.04713v3.txt';PDF=R/'shared-sources/Wanner-1801.04713v3.pdf'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists() and not S.exists()
assert sha(F)=='e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f'
assert sha(PDF)=='8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
S.mkdir();shutil.copyfile(F,S/'Wanner1801.04713v3-full-LOCALONLY.txt');shutil.copyfile(PDF,S/'Wanner1801.04713v3-full-LOCALONLY.pdf')
shutil.copyfile(R/'shared-sources/Wanner-1801.04713v3.provenance.json',S/'Wanner-retrieval-provenance-LOCALONLY.json')
lines=F.read_text().split('\n');units=[]
for lo,hi,scope in [(1,180,'Full introduction exactstanding algebraicallyclosed complete nontrivial field/proper smooth algebraic curve/theorem statements'),(219,285,'Entire2.3harmonic definition/2.4subharmonic definition/2.5sheaf proposition with cited immediate proof and adjacent context'),(470,665,'Entire3.14 positivity/3.16 currentPSH/3.19sheaf fullproof/3.20 smoothPSH fullproof/3.21smoothpullback remark'),(990,1611,'ENTIRE4.6 statement+immediateproof AND4.7 statement+ENTIRE immediate proof, then4.8')]:
    p=S/f'Wanner-real-LF-{lo}-{hi}-LOCALONLY.txt';p.write_text('\n'.join(lines[lo-1:hi])+'\n');units.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),source=str(F),source_sha256=sha(F),literal_LF_inclusive=[lo,hi],line_convention="split('\\n') / sed; FF remains inside line",scope=scope,ROOT_entire_untruncated_physical_read=True,actual_PDF_pixels_NOT_newly_read=True,deep_recursive_cited_proofs_NOT_all_newly_read=True,LOCALONLY=True))
text=P.read_text();stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',text):
    if m[1]=='begin':stack.append(m[2])
    else:assert stack and stack.pop()==m[2]
assert not stack and text.count('\\[')==text.count('\\]') and len(re.findall(r'(?<!\\)\$',text))%2==0
now=datetime.now(timezone.utc).isoformat()
rec=dict(recorded_utc=now,status='Whole ROOT394 new curve-test recognition-direction draft UNREVIEWED; originalP16.7 OPEN',paper=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P),ROOT_entire_final_saved_source_physically_read_untruncated=True),direct_scope=['Finite continuous all-stage minimalCPsh pulls back to finite classicalsubharmonic functions on tests by minimal-sheaf uniform closure','Tests EXACTLY open subsets of smooth proper algebraic curves over complete algebraicallyclosed nontrivial extensions L/K, actualmaps into basechangedopen torus chart','All decreasing boundedcontinuous thetaPSH presentations give USC harmoniccomparison after adding localrho, even atpoles; classicalsubharmonic oncomponents notidenticallyminusinfinity','Strictaffinoid curve boundarymaximum and infiniteboundary propagation'],named_source_foundations=['Exact Wanner4.7 under its completealgclosed/nontrivial/smoothproperalgebraic hypotheses','Thuillierharmonic definition andlocality/sheaf2.5 with exactcited background','Ordinarysmoothunitmoment pullback/DD chainrule andpositive(1,1)form/currentintegration, no arbitrarypositivecurrent pullback','ActualX quotient/nonalgebraization remains separate prior geometric source scope; only torusopen atlas used bythispaper'],whole_primary_units=units,version='Exactarxiv1801.04713v3 snapshot8Nov2018; no byteclaimto2019publishedarticle',unproved=['Converseintrinsic/curve-test recognition or global bounded presentations','Everypossible nonalgebraic analytic curve test beyondstatedscope','Higherdimension globalShilovmaximum','Separated surface energy-sublevel compactness','Intrinsiclocalpluripolarrecognition','All continuousobstacleenvelopes/orthogonality','Arbitrary-support finite-energy measure existence andfulluniqueness'],source_reading_boundary='Whole exactappliedWanner statements/immediateproof units read fromfulltext; no freshactualPDFpixel/deeprecursiveThuillier/model/semistable proof-tree/wholeWanner readingclaim',static_checks='Own environmentstack/displaydelimiter/dollarparity only; not compiler or mathverification',compilation='UNVERIFIED built-in request follows withprotectededitor unchanged',all_full_primary_bodies_literal_units_pixels_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_hot_feedback=False,protected_editor_OPEN_UNCHANGED=True,accepted=False,new_correctness_grant=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
B.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['current_active_batch']==[276,277] and x['github_pending_checkpoint'] is None
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,latest_unreviewed_ROOT_curve_test_paper=dict(continuation=394,paper=str(P),paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),accepted=False,original_closed=False),next_work='Native276 formalBIG and277 intrinsicE1 remain independent. ROOT actualcurve/source comparison and surfacecompactness/uniqueness gaps. Publish283 wholeROOT394+277launch, no hotfeedback/closure/countchange.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(paper=str(P),paper_bytes=P.stat().st_size,paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),private_full_primary_units=len(units),accepted=False,original_closed=False),indent=2))
