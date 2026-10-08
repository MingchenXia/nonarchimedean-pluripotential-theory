from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
P=R/'primary-data-LOCALONLY/P12.3-BdFF-isolated-envelope-20261008'
W=K/'P12.3-continuation360-normal-isolated-characteristic-zero-envelope-continuity-from-primary-upper-approximation-working-proof-20261008.md'
B=K/'P12.3-continuation360-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
M=G/'upload-manifest-continuation259.json';F=G/'continuation259-publication-records';S=K/'small-batch256-257-public-status-20261008-continuation259'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not B.exists() and not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation258.json').read_text())
assert prior['commit_sha']=='568aed3f9ac956a05ce665857881cc44766606e6' and not prior['force_update'] and all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(P/'BdFF-volume-isolated-singularity-author-published.pdf')=='44f52824c1bec3fd59631ec78567c587b718bda70bfc2241ec5311fc50346666'
assert sha(P/'BdFF-volume-isolated-singularity-author-published.txt')=='2ea47b9a20e1c59a7b48c71b5e751bb0550a595d7065a675b619d8b655436506'
campaigns={q:next((R/f'campaigns/round-{q}').iterdir()) for q in [256,257]}
for q,C in campaigns.items():
 assert sha(C/'input.json')=={256:'ac95a1135b126796b9970ffb0a0924623cec2fc00086157154ef29656c414d51',257:'7773844e1fa237e945fd448fe709d202abc848bc3527c2682a8462f7b7cc0ba4'}[q]
 for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
  for e in json.loads((C/name).read_text()):
   assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
   assert str(W)!=e.get('origin') and '/P12.3-BdFF-isolated-envelope-20261008/' not in e.get('origin','')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();metadata=[]
for p in sorted(P.iterdir()):
 if p.is_file():metadata.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),LOCALONLY=True,source_url='https://sebastien.boucksom.perso.math.cnrs.fr/publis/BdFF.pdf'))
record=dict(recorded_utc=now,continuation=360,atom='P12.3',status='ENTIRE new working proof UNREVIEWED, held for FUTURE independent reconstruction, no ACTIVE feedback',proof=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W)),ROOT_whole_reading='Entire current proof physically read in overlapping character chunks0:12300 and11900:end. Two final source-scope corrections were written and fully read. Complete immediate source proofs and fresh PDF pixels read as specified below; no recursive-whole-foundations claim.',only_correctness_grant='ENTIRE qualifiedG331 actual primary-model cone/comparison/full-boundary density/finite MAX/scaling/uniform completion, exact mandatory source/model/support scope; no355 or other unreviewed proof correctness import',private_primary_metadata=metadata,source_complete_immediate_units=['Section1 algebraically-closed-characteristic-zero setting and b-divisor definitions/sign','Lemma1.8 statement/proof','Lemma1.12 entire statement/proof','Section2.1 whole2.1-2.8','Definition2.9/Lemmas2.10-2.11/Proposition2.12/Corollary2.13 entire statements/proofs','Proposition2.15/Definition2.16/Remark2.17 and2.18 whole statements/proofs','Definition3.12 throughTheorem3.17 entire immediate units/proofs','EntireSections4.1-4.2 through4.11 immediate statements/proofs'],fresh_SOURCE_pixel_reading=dict(pdf_pages=[22,41,46,47],printed_pages=[1476,1495,1500,1501],scope='These exact pages only; all inequality directions physically confirmed, no wholePDF pixelclaim'),mandatory_source_qualifications=['Literal integralCartier4.11 version only; rational signed obstacle denominators cleared before applying','W=0 handleddirectly; eventual primary multiplierideals obtained only whenW nonzero','Correction ideals havecosupport contained{0}, may beUNIT; no false strictprimary assumption ondefectideal/Gorenstein/smooth case','Source approximation is coefficientwise; newfinite-trace comparison plusqualifiedfull-divisor density proves uniformall-support estimate','No nefpushforward/allpropermodels-as-geometric-core assertion; source tracevariationalenvelope used onACTUALdetermining primarymodel','Every discontinuousD competitor controlled byONEactualC-majorant atfinitevertices BEFORE density'],new_result='Normal closed algebraic germs over algclosedchar0 with regular orisolatedsingular point inALLdimensions: finitecontinuousgeometric envelopes CONTINUOUS, extendedUSC greatestD envelopes/poles anddecreasingobstaclenetstability. Wholeprimary-model/fullSUPPORT proof, ONEgauge factor.',recursive_published_dependencies='Singular/asymptotic multiplierideal foundations, Takagi subadditivity, char0resolution, ordinarylocalization andlatticeStoneWeierstrass disclosed publishedinputs, notfully rederivedhistoricalproofs.',scope='Arbitraryexcellent normal>=3 nonisolated andpositive/mixedchar remainOPEN; nooriginal acceptance orclassical/CLD identification. Companion359 stillrequireswholeindependentreconstruction.',not_in_frozen_native256257=True,hot_feedback_sent=False,source_bodies_pixels_LOCALONLY=True,original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True)
write(B,record);F.mkdir();S.mkdir();items=[]
for q,C in campaigns.items():
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
write(F/'BdFF-published-primary-acquisition-metadata-LOCAL-body-excluded.json',json.loads((P/'acquisition-records.json').read_text()))
up=R/'primary-data-LOCALONLY/BdFFU-page11-20261008-ROOT-exploratory.png'
write(F/'BdFFU-exploratory-reading-EXCLUDED-as-proof-premise.json',dict(recorded_utc=now,pixel=dict(path=str(up),bytes=up.stat().st_size,sha256=sha(up),LOCALONLY=True),fresh_complete_immediate_reading='Previouslyretained primaryBdFFU TXT intro1.1-1.3, setting2.1-2.2, entire4.1theorem4.2lemma andall4.1proof. ExactPDFpage11freshphysicalpixel confirms literal nu(IN)=-1 inproof whiledefinednormalizedsection is+1.',scope='Exploratoryonly; sourcefunction-field valuations exclude nonminimal infinitySUPPORT. Noapplication/noofficialerratumclaim/nofreshwholeupdatedversion. Not aninput toROOT360 orACTIVE256257.'))
write(F/'compiler-observation.json',dict(recorded_utc=now,builtin_cell33='Existing358 source submitted, boundedwaitstillrunning at latest observation; compilation UNVERIFIED, noPDFexport/successclaim',protected_editor_open_unchanged=True,extra_tabs=False))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==258
 x.update(updated_utc=now,ROOT360_isolated_char0_normal_envelope=dict(proof=record['proof'],binding=str(B),status=record['status']),current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=259,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue ACTIVE256257 wholeoriginal native independentwork without reading/hotfeedback; new359/360 frozen forFUTURE reconstruction. Verify259exactGit tree/allblobs/ref.15solved27OPEN96papers, protectededitorOPENUNCHANGED.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint259: full normalization formula and isolated normal envelope theorem

15/42 originals solved,27OPEN,96acceptedpapers; no new acceptance. Entire newROOT359 proves underEXPLICITnormal-centre continuity that USCregularized geometric baseenvelope equals the maximum ofactual sourceenvelopes on EVERYfullnormalization fibre, with exactpositive-domain criterion. Its all-reduced-surface corollary stillrequires whole355 independent reconstruction. Entire newROOT360 supplies the normal-centre continuity hypothesis forNORMALclosed algebraic germs overALGEBRAICALLYCLOSEDchar0 withREGULARorISOLATEDsingular point inALLdimensions: actual primary-model Cartiercone first, exactpublishedBdFF variationalnef envelope andprimaryUPPERapproximation, rationaldenominator clearing/zero-unit corrections, finite determining-model error ->uniformallDIVISORS ->allSUPPORT bydensity. EveryD competitor usesONEactualcontinuousmajorant atfinitevertices beforedensity; dense rational signedprofilelattice givesALLfinitecontinuousobstacles; ONEC-net givespoles/extendedUSC envelopes andcompactness givesdecreasingobstaclenetstability. OnlyfullqualifiedG331 grant. Wholeproof/source/scope mandatory qualifications are retained, not fragment acceptance. Generalnonisolated/positive-or-mixedchar higherdim normal original remainsOPEN.

NewpublishedBdFF primary PDF/text acquired directly fromofficialauthorURL afterweb-fetch timeout; exactcompleteimmediateappliedunits andfreshPDFpages22,41,46,47 were physicallyread. Primarybodies/pixelsstayLOCALONLY; onlymetadata public. DifferentBdFFU4.1 entireimmediateproof andpage11minus-sign exploratoryobservation are notproofpremises andnotofficialerrata. All newwork is heldforFUTUREnativeindependentreconstruction andnotin frozenACTIVE256257inputs; those two publicstatuses only were read. No active mathematics orhotfeedback, extra campaigns/agents, suppliedprogram execution orcredentials changes. ProtectedP16.4editorOPENUNCHANGED, no extra tab. Builtin358compilation remainsUNVERIFIED.

Sameexplicitly authorizedrepository/branch. Nonforceparent comparison, independentGit-tree reproduction, everyremote blob/ref verified before reportingpushcompletion. Wholeown acquisition/binding/preparationhelpers published; no broad source-body upload.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation259/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for pattern in ['P12.3-P12.6-continuation359-*','P12.3-continuation360-*']:
 for p in K.glob(pattern):
  if p.is_file():add(p)
for p in [R/'record_whole_normalization_formula359_held_for_future_review_20261008.py',R/'acquire_primary_BdFF_isolated_envelope_packet_20261008.py',R/'record_verified258_20261008.py',G/'push-receipt-continuation258.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=27,historical_reviewed_scoped_papers=96,commit_message='Record full normalization formula and isolated normal characteristic-zero envelope proof',scope='15solved27OPEN96papers. Entireunreviewed359360 withfullsource/support qualifications, futureindependentreview only. Primarybodies/pixelsLOCALONLY, noacceptance.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),ROOT360=record['proof'],active_rounds=active,solved=15,open=27,papers=96),indent=2))
