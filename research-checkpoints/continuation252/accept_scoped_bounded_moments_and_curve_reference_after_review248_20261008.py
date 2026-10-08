from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P12.4-continuation341-bounded-moment-measures-and-geometric-curve-reference-unreviewed'
E=D/'independent-review248';C=next((R/'campaigns/round-249').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def bound(p):p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def save(p,x):assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(D/'P12.4-paper.tex')=='d1b40bf37d047f5f37ec7a47880ac51c1e78e37bba03a043f3e6bffa61454633'
assert sha(D/'P12.4-paper.pdf')=='e26b42a63c4b06d5b592224f02d4ed000a381d2c2a1212811ed1d0ff2fdf299b'
assert load(D/'ROOT-built-in-compile-20261008.json')['tool_result']['kind']=='success'
b=load(D/'ROOT-independent-review248-whole-reading-and-binding-20261008.json');assert b['ROOT_every_actual_FINAL_note_field_physically_read'] and b['ROOT_whole_independent_proof_and_source_scope_physically_read'] and b['all_current_bindings_match']
decision=load(E/'acceptance-decision.json');assert not decision['author_mathematical_claim_replacement_required'] and decision['candidate']==False and decision['entire_original_P12_4']=='OPEN_NOT_SOLVED'
assert all(e['actual']=='supported_independent_draft' and e['expanded']=='supported_independent_draft' for e in decision['per_note'])
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93 and x['github_pending_checkpoint'] is None
st=load(E/'acceptance-decision.json')
public=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert not public['error'] and public['status'] in ['running','completed']
active=[249] if public['calls']['unsettled'] else [];now=datetime.now(timezone.utc).isoformat()
scope='Every excellent reduced local positive-dimensional germ and proper primary gauge: algebraic mixed-multiplicity moment measures on every bounded actualD tuple,allrealC/functionpresentationindependence,weak uniform and bounded decreasingNET continuity with specified limit inD,exactp=n-1arity,mass,onefactor gauge and residue-weightedtopdegree normalization. IndependentlygeometricZERO-arity Cartier reference measure onEVERYexcellentreducedcurve with allrealpresentations/everyprimarymodel and inseparableresidue-degreeexample. ExactBFJoperator specialization ONLYsmoothaffineCLOSEDalgclosedchar0germs. Empty/unit/zero/nonpure/nilpotent-boundarydiagnostic conventions explicit. No general higherdimCartiercomparison or positivearitylocality in THISpaper.'
qualification=dict(recorded_utc=now,atom='P12.4',continuation=341,status='Mandatory source/scope/reader qualifications for accepted supporting paper',exact_scope=scope,
    source_and_native_pdf_unchanged=True,source=bound(D/'P12.4-paper.tex'),pdf=bound(D/'P12.4-paper.pdf'),
    sole_incoming_grant='Entire qualifiedG331 with whole paper,mandatory source/scope annotation,source ledger and exactscope; no product/intersection/locality grant.',
    complete_G331_qualifications_required_on_import=True,complete_current_qualification_required_on_import=True,
    SH17_4_7_printing_qualification=bound(E/'source-qualification-addendum.md'),
    correct_source_application='Final correction is finite annihilator in the quotient by prior parameters, equivalently colon modulo previous parameter submodule. Literal printed unquotiented length not adopted. Author repeated17.4.6 regular proof survives; ROOTactuallyviewedprinted356.',
    published_historical_dependencies_disclosed_not_recursively_freshly_reconstructed=True,all_supports_and_full_conductor_quotient_retained=True,lower_dimension_topdegree_zero_not_deleted=True,
    no_nilpotent_generic_lengths_or_unbounded_energy_or_general_finite_map_or_arbitrary_model_cofinality_or_literal_radial_identification=True,
    reviewer_unavailable_history_distinct_from_ROOT_current_bindings=b['reviewer_historical_author_evidence'],actual_and_expanded_note_prose_distinct=True,
    review_scope='EntireimmutableauthorTeX and actual7FINAL previouslyROOTread; all7independent248FINAL fields,wholeindependentproof,sourceledger,coverage,scope and decision nowROOTread. Parallel authorargument retainedwithoutseparateROOTwhole-readclaim.',
    new_ROOT342_not_in_THIS_independent_review=True,original_closed=False,review_limit='Independent source-aware computational mathematical reconstruction, not a formal certificate, journal peerreview or priority claim.')
q=D/'mandatory-source-scope-and-reader-qualifications-after-review248-20261008.json';save(q,qualification)
rec=dict(recorded_utc=now,atom='P12.4',continuation=341,cumulative_accepted_paper_number=94,original_closed=False,fully_solved_original_atom=False,mathematical_verdict='PASS entire delimited paper after independent248 and ROOT complete proof/source/scope judgment with mandatory source qualification',exact_scope=scope,source=bound(D/'P12.4-paper.tex'),pdf=bound(D/'P12.4-paper.pdf'),pages=15,review_actual_FINAL=bound(K/'round248-actual-native-final.json'),review_binding=bound(D/'ROOT-independent-review248-whole-reading-and-binding-20261008.json'),mandatory_qualification=bound(q),whole_G331_qualifications_and_source_ledger_required=True,builtin_source_compilation_success=True,compilation_not_mathematical_acceptance=True,originals_solved=13,originals_open=29)
save(D/'scoped-paper-acceptance-after-review248-20261008.json',rec)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,historical_reviewed_scoped_papers=94,current_active_batch=active,
        P12_4_scoped_bounded_moments_curve_paper_after_review248=rec,
        P12_4_native246_whole_paper_review248=dict(round=248,status='COMPLETED; allactualFINAL and wholeproof/source/scopeROOTread; delimitedpaper341accepted94withmandatorysourcequalification',original_closed=False),
        next_work='Wholeoriginal249 independently reconstructs342geometry/locality+entirekernel+sideobligations;13solved29OPEN94accepted. OriginalP12.4stillOPEN. Finishcompiler343 withoutnewacceptance; selectnextsmallresearchproblem and publishregularverifiedcheckpoint.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();hits=0
for i,line in enumerate(lines):
    fields=line.split('\t')
    if fields[0]=='P12.4':
        assert fields[1]=='open';fields[2]='partial_bounded_moments_and_geometric_curve_reference_after_independent248';fields[3]=str(int(fields[3])+1);lines[i]='\t'.join(fields);hits+=1
assert hits==1;p.write_text('\n'.join(lines)+'\n')
s=D/'ROOT-public-draft-status-20261008.json';x=load(s);x.update(updated_utc=now,status='Accepted supporting mathematical paper after independent248; originalOPEN',paper_accepted=True,accepted_paper_number=94,original_closed=False,accepted_papers=94);s.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
(D/'ROOT-README.md').write_text('Accepted supporting15-page P12.4 mathematical paper94 after independent248 and ROOT wholeproof/source/scope review,with mandatorysourcequalification. Every boundedactualD algebraicmomentmeasure and actualgeometricexcellentreducedCURVEzeroarityreference; exactBFJpublishedsmoothscope only. Thispaperdoesnotprove generalhigherdimCartiercomparison or positivearitylocality,so originalP12.4OPEN.13solved29OPEN94accepted. FullqualifiedG331 annotation/ledger and currentmandatoryqualification requiredonimport. SH17.4.7literalprinting lacksquotient; repeated17.4.6regularproofvalid and immutableauthor/source/PDFunchanged. Reviewer unavailablehistoricalbodiesnotfreshlyattested; ROOTseparatelycheckedcurrentauthorbodies. Primarybodies/extracts/pixels/privateprovideroutputLOCALONLY; suppliedprogramsinertDATA. ProtectedP16.4editorOPENUNCHANGED.\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(accepted_paper=94,originals_solved=13,originals_open=29,current_active_batch=active),indent=2))
