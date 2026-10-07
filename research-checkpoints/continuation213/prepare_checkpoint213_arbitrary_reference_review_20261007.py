from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation213.json';F=G/'continuation213-publication-records'
S=K/'small-batch207208-public-status-20261007-continuation213'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation212.json').read_text())
assert prior['commit_sha']=='4a78924d0ed58a0e92a7752b3577973ec0c3c6ed' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=K/'public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact'
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['root_local_build_exit_codes']==[0,0] and not b['root_local_warnings']
assert b['whole1016_tex_root_read'] and b['whole290_argument_separately_root_read'] and b['whole_five_exact_final_notes_root_read']
assert sha(D/'P05.2-paper.tex')==b['source_sha256'] and not b['original_closed']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [206,207,208]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4' if n==207 else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],
        public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2 and items[0]['unsettled_calls']==0
primary=next(K.glob('P16.4-continuation275-*.json'));w=json.loads(primary.read_text())
assert not w['new_mathematical_grant'] and not w['original_closed']
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
    focus='WHOLE207 independent269 all-genus original-field curve theorem and WHOLE208 independent272 arbitrary-real-reference raw completion/common flat-jet theorem. Original P16.4 general n>=2 and P05.2 all-obstacle/nonPA sufficiency remain open.',
    new_accepted_paper=False,accepted_paper_number=78,original_closed=False)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
        P05_2_arbitrary_real_reference_completion272=dict(directory=str(D),source_sha256=b['source_sha256'],author_round=206,independent_review_round=208,
            status='UNREVIEWED same-reference raw mixed completion and arbitrary-reference flat-jet finite-PA criterion; entire source/argument/ledger/material/five exactFINAL ROOT-read,22wholeunits/four originals/73artifacts bound, checker/full normalized conversion/two clean local builds reproduced; builtin27 pending without SUCCESS.',
            pdf_pages=14,new_accepted_paper=False,original_closed=False),
        P16_4_original_BL_and_signed_CLD_application275=dict(path=str(primary),sha256=sha(primary),new_mathematical_grant=False,original_closed=False),
        next_work='Continue WHOLE207/208 independent source/application reviews, then remaining original inverse/classification sectors and other original problems; at most two61xhigh native campaigns. Full goal all42 remains; preserve actual frozen sources/editor/failures; regular verified pushes.',
        github_pending_checkpoint=dict(continuation=213,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint213: actual arbitrary-real-reference completion and common flat jets submitted for WHOLE independent review\n\n9/42 originals solved;33 open;78 accepted scoped/supporting papers. New fourteen-page native206/272 source proposes actual same-reference mixed raw completion and a separate positive convex rational-reference decomposition preserving a common local flat jet for arbitrary real reference coefficients. All1016TeX/290fullMD/47ledger/13material and FIVE exact FINAL notes ROOT-read. Exact native invocation/task/22wholemathunits/four immutable originals/all73artifacthashes/actual preserved bodies bound; native saved notes equal exactFINAL. Own finite385origin-support/14positive-circuit/22face/12saturated-cone/291collar checks, full normalizedTeX-to-Markdown conversion and two no-shell-escape clean local builds reproduced. Raw plane mass8sqrt6, corrected diamond vertices and scaled jet mass1/1024 retained. These establish finite diagnostic/provenance/rendering facts, not mathematical acceptance. Only ownPDFpages1/8/9/14 visually read; not all14. Builtin27 pending withoutSUCCESS.\n\nWHOLE208 independently reconstructs ALL13results and unnumbered assertions with exactly FOUR completeA/B/R/S262 grants and ALLclarifications,30wholeunits and fouroriginalbinder. Weak/BLuniformity ONLYeachfixedrelativeboundfamily; ALLactualrealreferences/commonrationaljetgluing/finite-PAcontactiff ALLrationalpoints/ALLfanrefinements require proofs. Original higher-dimensional all-obstacle regularization, non-PA contact sufficiency and exhaustive structural reduction remain open. WHOLE207 continues all-genus original-field curve equation269 review; original P16.4 general n>=2 remains open. At most two native61xhigh campaigns207/208.\n\nNEW ROOT275 quote-free ordinary-source application addendum records actual ORIGINALBL85 entire2.4-2.5 immediate proofs in PDF9-13/printed356-360 and literalCLDv1 whole6.9.2-6 including calibrated6.9.5 plus6.8.2 signed/zero n1scope. Recursive foundations are explicitly not all freshly read. New addendum is unreviewed, not a grant/metadata repair/hotfeedback to207. Full original copyrighted texts/PDFs/pixels remain LOCALONLY. No private active outputs, raw databases, authentication/account data or full thirdparty primary bytes published. Oldfailedrecords/frozenpaper/protectededitor unchanged. No new acceptance/originalclosure; no-force publication requires independent remote tree/blob/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation213/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for name in ['README.md','P05.2-paper.tex','P05.2-paper.pdf','argument.md','source-application-ledger.md','material-changes.md','check_certificates.py','certificate-input.json','normalize_argument.py','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json']:add(D/name)
for name in ['native-artifact-manifest.json','native-artifact-checks.json','native-input-block-manifest.json','native-primary-provenance.json','native-environment.json','native-execution-record.json','native-certificate-output.json','native-markdown-normalization.json','certificate-output.json','root-checker.stdout.txt','root-checker.stderr.txt','root-latex-pass1.stdout.txt','root-latex-pass1.stderr.txt','root-latex-pass2.stdout.txt','root-latex-pass2.stderr.txt','root-pandoc.stdout.txt','root-pandoc.stderr.txt','root-normalizer.stdout.txt','root-normalizer.stderr.txt']:add(D/'evidence'/name)
for n in [1,8,9,14]:add(D/f'evidence/root-visual-page{n}.png')
for name in ['P05.2-round206-actual-registered-partial-author-result-20261007.json','P05.2-round206-exact-native-model-final-partial-author-20261007.json','P05.2-round206-whole-arbitrary-reference-author-binding-20261007.json']:add(K/name)
add(primary)
C=next((R/'campaigns/round-208').iterdir())
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json']:add(C/name)
for name in ['bind_and_reproduce_arbitrary_reference272_20261007.py','write_curve_primary_scope275_20261007.py','prepare_arbitrary_reference272_review208_20261007.py','launch_frozen_arbitrary_reference_review208_20261007.py','record_verified212_20261007.py']:add(R/name)
add(G/'push-receipt-continuation212.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
    fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=78,
    commit_message='Submit arbitrary-real-reference raw completion and flat-jet contact criterion for whole review',
    scope='NEW14page272/native206 whole1016TeX/290MD/47ledger/13material/FIVEexactFINAL ROOTread;22wholeunits/4originals/73artifacts bound; checker/normalizedfullconversion/twoCLEANlocalbuilds reproduced. WHOLE208 reconstructs13results using FOURwholeA/B/R/S262grants/allclarifs;30wholeunits. Actualsamegamma completion/commonflatjet gluing finitePAsector only; globalweakBLrestrictionretained. Originalhigherdimall-obstacle/nonPAclassificationOPEN. WHOLE207 allgenuscurve269 reviewongoing;P16generaln>=2OPEN. ROOT275 unreviewed originalBL2.4-2.5 immediateproofpixels/literalCLDv1 signedzero n1 applicationmetadata, notgrants/repair/hotfeedback.78accepted9originals33open;atmosttwo61xhigh207208. Builtin27/113/53pendingwithoutSUCCESS. Protectededitor/frozensources/failurespreserved;no fullthirdpartyprimary/privateactive/auth/databasepublication. Verified noforce push.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=78),indent=2))
