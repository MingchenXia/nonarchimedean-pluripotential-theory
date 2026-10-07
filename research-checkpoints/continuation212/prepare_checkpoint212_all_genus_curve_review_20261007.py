from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation212.json'; F=G/'continuation212-publication-records'
S=K/'small-batch206207-public-status-20261007-continuation212'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation211.json').read_text())
assert prior['commit_sha']=='b479d3a6e43969c678a289a4383334b141718a14' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=K/'public-P16.4-continuation269-all-genus-original-field-curve-equation'
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['root_local_build_exit_codes']==[0,0] and not b['root_local_warnings']
assert b['whole1105_tex_root_read'] and b['whole399_argument_separately_root_read'] and b['whole_five_exact_final_notes_root_read']
assert sha(D/'P16.4-paper.tex')==b['source_sha256'] and not b['original_closed']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in [205,206,207]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==206 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],
        public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2 and items[0]['unsettled_calls']==0
working=[next(K.glob(f'P16.4-continuation{n}-*.json')) for n in [273,274]]
for p in working:
    w=json.loads(p.read_text());assert not w['new_mathematical_grant'] and not w['original_closed']
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
    focus='Original206 P05.2 higher-dimensional arbitrary-reference/all-obstacle classification; WHOLE207 independent mathematical/source review of native205 NEW15page all-genus original-field curve equation269. Original n>=2 P16.4 remains open.',
    new_accepted_paper=False,accepted_paper_number=78,original_closed=False)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
        P16_4_all_genus_curve_equation269=dict(directory=str(D),source_sha256=b['source_sha256'],author_round=205,independent_review_round=207,
            status='UNREVIEWED whole actual curve inverse/everypoint/field theorem; entire source/argument/ledger/scope/five exactFINAL ROOT-read,46wholeunits/62originals bound, checker/exactconversion/two clean local builds reproduced; builtin113 pending without SUCCESS.',
            pdf_pages=15,new_accepted_paper=False,original_closed=False),
        P16_4_weighted_FS_and_reference_scope_working273274=[dict(path=str(q),sha256=sha(q),new_mathematical_grant=False,original_closed=False) for q in working],
        next_work='Continue WHOLE207 independent all-genus curve review and original206 higher-dimensional polyhedral classification, then remaining original sectors; at most two61xhigh native campaigns. Full original goal remains all42, no stopping at supporting-sector completion. Preserve failed evidence, frozen source/current editor; regular verified pushes.',
        github_pending_checkpoint=dict(continuation=212,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint212: actual all-genus curve equation submitted for WHOLE independent review\n\n9/42 original problems solved;33 open;78 accepted scoped/supporting papers. No new acceptance or original closure. NEW native205/269 fifteen-page paper proposes actual original-bundle FS recognition without whole-mod-a generation/H1 antecedents, genuine raw curvature, arbitrary-support intrinsic-target inverse for all genera, EVERYsolution EVERYpoint uniqueness and actual singular invariance before original-field descent. Entire1105-lineTeX/399-lineargument/47-line25-applicationledger/9-linescope and FIVEexactFINALnotes ROOT-read. Decoded native invocation/task/46wholemathunits/62immutableoriginals/all26artifacthashes/exactnative-canonical equality bound. Saved native notes equal exactFINAL. Native input serialization differs28bytes but decoded exact mathematical input equality verified. One pre-mutation ROOT binding attempt encountered a different native extraction index schema; the final checker verifies label/exact-body bytes without an added newline.\n\nOwn finite checker reproduced150energy/450positive-bend/36tree-kernelcases and nonatomic interval/Cech examples; exact Pandoc conversion and two no-shell-escape local builds reproduced clean,15pages. These checks establish provenance/finite diagnostics and rendering, not analytic correctness. Only own PDF pages1/6/9/12/15 visually checked; not all15. Builtin compiler113 requested and pending withoutSUCCESS; previous265 builtin53 also remains pending. Protected current editor preserved.\n\nWHOLE207 independent source/application reader now reconstructs EVERY assertion in unchanged269, using exactly EIGHT completeO/D/N/T/Q/C/G/M grants and ALL clarifications;33wholeunits and explicit62 original bindings. Particular attention to literal CLDv1 SIGNED/ZERO component coefficients and real-weight carrier/trace/radial applications; no metadata repair or graph-only review. Native269 finite anchor uses O integrability at an already-E1 solution, not M at a changed reference. General n>=2 original equation remains OPEN.\n\nNEW ROOT273/274 are UNREVIEWED future data: actual signed weightedFS curvature through positive auxiliary bundles/CLD linearity, realIII weights and true tree trace; exact M selected-reference scope correction to earlier268C9/273T7 plus direct true-FS graph/radial uniform anchor bound. Frozen old sources unchanged;273/274 deliberately NOT supplied as grants or material paper repair in207.\n\nOriginal206 continues higher-dimensional/all-obstacle polyhedral classification after accepted entire graph theory and new arbitrary-reference completion route271. At most two campaigns206/207, exact Xean native61xhigh; no active-private-output/hot feedback. Failed250/198 and failed255/200 remain unchanged; no full third-party primary text/images/databases/auth/account data uploaded. Publication is no-force with full remote tree/blob/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation212/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for name in ['README.md','P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','scope-and-gaps.md','finite_checks.py','finite-inputs.json','finite-output.json','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json']:add(D/name)
for name in ['native-artifact-manifest.json','native-finite-output.json','native-finite-checks.log','native-environment.json','native-reproduce.sh','native-supplied-index.json','native-frozen-manifest.json','root-checker.stdout.txt','root-checker.stderr.txt','root-latex-pass1.stdout.txt','root-latex-pass1.stderr.txt','root-latex-pass2.stdout.txt','root-latex-pass2.stderr.txt']:add(D/'evidence'/name)
for n in [1,6,9,12,15]:add(D/f'evidence/root-visual-page{n}.png')
for name in ['P16.4-round205-actual-registered-partial-author-result-20261007.json','P16.4-round205-exact-native-model-final-partial-author-20261007.json','P16.4-round205-whole-all-genus-curve-author-binding-20261007.json']:add(K/name)
for p in working:add(p)
C=next((R/'campaigns/round-207').iterdir())
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json']:add(C/name)
for name in ['bind_and_reproduce_all_genus_curve269_20261007.py','write_actual_weighted_FS_trace273_20261007.py','write_exact_reference_scope_and_anchor274_20261007.py','prepare_all_genus_curve269_review207_20261007.py','launch_frozen_all_genus_curve_review207_20261007.py','record_verified211_20261007.py']:add(R/name)
add(G/'push-receipt-continuation211.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
    fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=78,
    commit_message='Submit actual all-genus curve inverse and every-point theorem for whole independent review',
    scope='NEW15page269/native205 whole source/argument/ledger/scope/FIVEexactFINAL ROOTread,46wholeunits/62originals/26artifacthashes bound; checker/exactconversion/two clean local builds reproduced. WHOLE207 independent actual-source/application reader uses EIGHTwholegrants/ALLclarifs,33wholeunits; SIGNED/ZERO CLDv1 coefficients and true realFS trace/radial/everypoint descent need reconstruction. ROOT273/274 unreviewed signed-weightedFS applications/exact-Mscope/direct-anchor-bound futuredata, deliberately not supplied as grants/repair. Native269 uses O integrability at E1 anchor, not changed-reference M moment. Original206 higherdim arbitraryref/all-obstacle polyhedral classification continues. At most two61xhigh campaigns;78accepted9originals33open. Builtin113/53 pending withoutSUCCESS. Frozen sources/editor/failures preserved; no fullthirdpartyprimary/privateactive/auth/database publication. Verified noforce push.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=78),indent=2))
