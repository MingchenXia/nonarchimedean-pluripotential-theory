from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks';W=K/'P12.3-P12.5-continuation354-graded-primary-limits-with-vanishing-energy-and-nonpositive-pointwise-limit-working-proof-20261008.md'
B=K/'P12.3-P12.5-continuation354-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists()
proof=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W));now=datetime.now(timezone.utc).isoformat()
source=next(e for e in json.loads((next((R/'campaigns/round-255').iterdir())/'private-primary-packet-bindings.json').read_text()) if Path(e['path']).name=='BdFFU-singular-multiplier-ideals.txt')
assert sha(source['path'])==source['sha256'] and Path(source['path']).stat().st_size==source['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
states=[]
for rnd in [254,255]:
    C=next((R/f'campaigns/round-{rnd}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status']=='completed' and st['calls']['unsettled']==0
    actual=json.loads((K/f'round{rnd}-actual-native-final.json').read_text());assert actual['candidate'] is False
    states.append(dict(round=rnd,public_status=st,actual_FINAL_sha256=sha(K/f'round{rnd}-actual-native-final.json'),candidate=False,ROOT_whole_reading_complete=False))
record=dict(recorded_utc=now,continuation=354,atoms=['P12.3','P12.5'],status='Entire new working proof UNREVIEWED; no original closure or paperacceptance',proof=proof,ROOT_reading='Whole initial proof physically fullcat without truncation; two precise current clarification paragraphs and skipped source definition preamble then read completely. No fresh duplicate entiregrant claim.',only_prerequisites=['EntirequalifiedG331','EntirequalifiedG345','EntirequalifiedE350 with mandatory source/scope qualifications'],new_example='Everyfield regularsurface R=k[x,y]_(x,y), gradedprimary J_j=(x,y^j), u_j=-v(J_j)/j increases to h=-1 atsupport(x) and0elsewhere; monomialw_M approaches thatpoint so hnotUSC/notD. Exactlength m^rJ_j^s=r(r+1)/2+rs+js(s+1)/2 =>rawmass1/j, energy1/(2j), productTVto0. FullCauchySchwarz/Markov givesCap{u_j<-epsilon}<=1/(epsilon sqrt(j)), hence Cap(Z)=0; nonpositive pointwiselimitcannotbeidentifiedwithD bycapacity/energy alone.',primary_source_binding=source,fresh_exploratory_source_reading='BoundBdFFU text LF1--260,260--332,335--481 plus325--355gaprepair. Whole immediate2.1--2.5/2.6 and3.1--3.4/3.1proof read; sourceusesfunction-field Val_X andboundeddiscrepancysets, notallnonminimal-supportsection. LiteralTEXTorientation/convexity/USC discrepancies recordedwithoutsourcechange/PDFpixelclaim. No such theorem applied to newexample.',limitations='Specified gradedfamily supremum, notFULL continuousobstacleenvelope; doesnotrefuteacceptedE350 orsmoothBFJCE or353goodcover. No arbitraryincreasingDclosure/pointwiserepresentativeidentification. OriginalP12.3OPEN, P12.5existingacceptance unchanged.',source_bodies_pixels_LOCALONLY=True,no_supplied_programs_executed_or_imported=True,private_ACTIVE254255_math_inspected_or_hotfed_during_construction=False,protected_editor_open_unchanged=True,original_closed=False,accepted_paper=False)
B.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=[],completed254255_awaiting_ROOT_whole_reading=states,P12_3_P12_5_ROOT354=dict(proof=proof,binding=str(B),status=record['status']),next_work='ROOT readENTIRE completed254255proof/source/scope/actualFINAL/expandednotes before acceptance. BothcandidateFALSE; new355normalSURFACEscheme/matrixproof and356regularization finite-mapcalculus beingdeveloped, NOactivejobs.15solved27OPEN96papers;verifiedGitHub257,compile1010pending,protectededitorOPENUNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(ROOT354=proof,binding=str(B),completed_rounds=[254,255],active=[],counts_unchanged=True),indent=2))
