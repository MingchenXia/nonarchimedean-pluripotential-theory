from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation254.json';F=G/'continuation254-publication-records';S=K/'small-batch252-public-status-20261008-continuation254'
D4=K/'public-P12.4-continuation345-supported-Cartier-products-and-bounded-locality-original-candidate';D5=K/'public-P12.5-continuation347-original-finite-energy-and-decreasing-net-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation253.json').read_text());assert prior['commit_sha']=='82ad5f09155a291b494a5b546c889c9b9f9d3fe9' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
accept=json.loads((D4/'whole-original-paper-acceptance-after-review251-20261008.json').read_text());assert accept['original_closed'] and accept['cumulative_accepted_paper_number']==95
assert sha(D4/'P12.4-paper.tex')==accept['source']['sha256'] and sha(D5/'P12.5-paper.tex')=='e95d6c4440e66d1d70f7ed99b2377f236bec4b74307336dd36a705c08a08ac62'
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for rnd in [250,251,252]:
    c=next((R/f'campaigns/round-{rnd}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed'];p=S/f'round{rnd}-public-native-status.json';write(p,st);items.append(dict(round=rnd,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2 and set(active)<=set([252])
observation=D4/'ROOT-built-in-compile-observation-after-review251-20261008.json'
write(observation,dict(observed_utc=now,path=str(D4/'P12.4-paper.tex'),source_bytes=(D4/'P12.4-paper.tex').stat().st_size,source_sha256=sha(D4/'P12.4-paper.tex'),tool='codex_app.compile_latex_document',exec_cell='906',status='PENDING; no result or compiler diagnostics returned. Mathematical original acceptance recorded separately; PDF UNVERIFIED.',compiler_result_received=False,compiler_success_claimed=False,source_or_tab_modified_by_ROOT=False,protected_P16_editor_unchanged_open=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==14 and x['remaining_open_original_atoms']==28 and x['historical_reviewed_scoped_papers']==95 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=254,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Independent252 reconstructs originalP12.5 plus entire346 Borel/nonpolar/capacity/comparison. OriginalP12.4 accepted95 after entire251/ROOT proof/source/scope; PDF call906 unverified. Push254, then originalP12.6 finite geometric products/envelopes compatibility.14solved28OPEN95papers; max2nativegpt6.1solxhigh; no active private output or hotfeedback.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint254: originalP12.4 solved and completeP12.5 independent review launched\n\n14/42 original problems solved,28OPEN,95acceptedpapers. P12.4 is a WHOLE ORIGINAL mathematical solution after native249, independent251, and ROOT physical whole proof/source/scope reading. Its actual supported Artinian Cartier Euler/Koszul intersection, independent positiveREALnefatomic core/refinement invariance, fixedPRIMARY c0 actual image on ONE refinement, function/modelindependence, ordinaryOPENlocality and prescribedD-limit fullNET continuity are proved. Onegaugeweight, closedresidueweightednormalization/fullconductor/all-support and lowerdegree/curve/empty/nilpotent qualifications remain mandatory. LiteralSH17.4.7 requires finiteCURRENTquotient annihilator, not printedunquotientedcolonlength. ExactpublishedBFJoperator onlyclosedaffinealgclosedchar0 plusdirectDVR/empty. EntireG331 grant+annotation+ledger+scope remains required. Independent251 froze OLDreader with literalfontsubstitution; ROOT corrected BEFOREcompletion, all4currentliteralgrantbodybytes match. Immutableauthor and frozenreview inputs unchanged; mandatoryannotation explains old/currenthistory.95counts mathematicalsourcepaper acceptance; BUILTINcompile906 still has no result, so PDF UNVERIFIED. No typesetting success/error fabricated.\n\nNative250 completed originalP12.5 candidateTRUE. All9actualFINAL fields, entire59625character NEW TeXmathematicalcore,whole source/scope/coverage/decision ROOTread; fullqualifiedG331/B341 literalappendices exactbytes match alreadywhole-readgrants. No freshphysicalwhole251146Breading claimed.33own and52origin/local104 checks match. Whole unchanged251kstandaloneTeX,expanded55kargument,proofs,exactoriginal/assignment,allauthor metadata and inertprograms retained. Native original-task.json here correctly preserves originalproblem plus trailingnewlines, unlike native249; ROOT initial staging assumption was corrected BEFOREdirectorycreation. A second preacceptance ROOT bytecheck wrongly included two bindingmanifestattachments as literalappendices; corrected to the4explicitliteralgrantcomponents before acceptance mutation. Neither assertion failure changed a mathematicalsource or counts.\n\nNative252 gpt-6.1-sol xhigh independently reconstructs ENTIRE candidate250 and ALLnewROOT346 boundedtestalgebra/BorelstrictMAX/nonpolarcutoffs/canonicaltruncationTV/capacity/strictcomparison/quasicontinuity. Only completequalifiedG331/B341 correctnessgrants; 342/344/346 are wholeUNREVIEWED proofs, no P12.4 candidate/reviewgrant. Full bookchapter/packets are CONTEXTDATA, not authority and not a theorem grant; privatecompletecontextbodies and primarysourcebodies/pixels stayLOCALONLY, bindingmetadata retained. Frozen252 inputs remainunchanged; no privateACTIVEoutput read/hotfeedback. P12.5/P12.3/P12.6 remainOPEN. ProtectedP16editor OPENUNCHANGED. Current-targetP12.2 stale row reconciled to alreadyexisting acceptance91 without countincrement. Gitpush uses sameauthorizedrepo/branch/auth, nonforce and completeblob/tree/refverification.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.png','.pdf'];assert not any(t in rel.parts for t in ['source-pages','source-images','primary-data-LOCALONLY'])
    target=target or 'research-checkpoints/continuation254/'+str(rel);assert target not in seen;seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D4,D5]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for rnd in [250,252]:
    c=next((R/f'campaigns/round-{rnd}').iterdir())
    for name in ['task.json','original-task.json','input.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
        p=c/name
        if p.exists():add(p)
    for name in ['book-context-bindings.json','historical-own-evidence-bindings.json']:
        p=c/name
        if p.exists():add(p)
    if rnd==252:
        for e in json.loads((c/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for p in [K/'P12.4-round251-whole-original-supported-products345-ROOT-binding-20261008.json',K/'P12.2-target-row-reconciliation-existing-acceptance91-20261008.json',R/'capture_completed_whole_original_review251_20261008.py',R/'stage_energy_candidate347_and_prepare_whole_review252_20261008.py',R/'launch_whole_original_energy_review252_20261008.py',R/'accept_whole_original_P12_4_after_review251_20261008.py',R/'record_verified253_20261008.py',G/'push-receipt-continuation253.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=28,historical_reviewed_scoped_papers=95,commit_message='Solve original P12.4 supported bounded products; freeze whole finite-energy independent review',scope='14solved28OPEN95papers.WholeoriginalP12.4 mathematicalacceptance/251fullreview and qualifiers; standaloneenergycandidate347/250actual plus252fullfrozen independentreview of candidate and346. Compile906 pending, PDF unverified.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,originals_solved=14,originals_open=28,accepted_papers=95),indent=2))
