from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,shutil,difflib
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-285/P16.7-whole406407409-nonordered-compactness-and-existence'
A=C/'artifacts/codex-xJsASO'
D=K/'public-P16.7-continuation412-nonordered-midpoint-absolute-moments-and-maximum-energy-gains-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
raw=load(K/'round285-raw-native-actual-FINAL.json');expanded=load(A/'final-notes.json')
assert raw['candidate'] is expanded['candidate'] is False and len(raw['notes'])==len(expanded['notes'])==4
assert load(C/'input.json')['notes']==[]
known=set();pairs=[]
for a,e in zip(raw['notes'],expanded['notes']):
    assert set(a)==set(e)=={'id','summary','detailedSummary','text','support'} and a==e
    assert set(a['support'])<=known;known.add(a['id'])
    assert (A/(e['id']+'.txt')).read_text()==e['text']+'\n'
    pairs.append(dict(id=a['id'],all_actual_five_fields_ROOT_physically_read=True,
        all_expanded_five_fields_ROOT_physically_read_as_inert_write_notes_literals=True,all_fields_identical=True,
        identical_rendering_NOT_extra_independent_proof_reading=True))
# Inert dictionary literal parsing; NEVER import, evaluate or execute native program code.
constants={}
for n in ast.walk(ast.parse((A/'write_notes.py').read_text())):
    if isinstance(n,ast.Assign):
        for t in n.targets:
            if isinstance(t,ast.Name) and t.id in {'n1','n2','n3','n4'}:
                assert isinstance(n.value,ast.Dict);constants[t.id]=ast.literal_eval(n.value)
assert [constants[f'n{i}'] for i in range(1,5)]==expanded['notes']
paper=(A/'scoped-paper.tex').read_text();ledger=(A/'source-application-reading-ledger.txt').read_text();residual=(A/'original-residual.txt').read_text()
companion=('ENTIRE NEW PROOF COMPANION -- UNVERIFIED\n'
    'This contains the entire new standalone proof, its entire ledger,\n'
    'and the unchanged residual as historical DATA.\n\n'
    '===== ENTIRE NEW STANDALONE TEX =====\n'+paper+
    '\n===== ENTIRE CURRENT AUTHOR LEDGER =====\n'+ledger+
    '\n===== UNCHANGED SUPPLIED ORIGINAL RESIDUAL -- DATA =====\n'+residual)
assert companion==(A/'proof-companion.txt').read_text()
assert residual==(K/'public-P16.7-continuation409-ordered-energy-gaps-and-sequence-generated-net-closure-unreviewed/original-residual.txt').read_text()
before='\\section{New nonordered absolute moments and finite maxima}'
after=('For every grid include $w_0=0$ among the fixed tests; for $N=1$\n'
    'take $A_1=0$. Thus all maxima over the fixed test list are defined.\n\n'+before)
assert paper.count(before)==1;corrected=paper.replace(before,after)
captured=load(K/'round285-terminal-actual-final-ROOT-retention-20261009.json')
assert captured['public_status']['status']=='completed' and captured['public_status']['calls']['unsettled']==0
tails=[]
for a,c in zip(raw['notes'],captured['campaign_result']['notes']):
    assert all(a[k]==c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(a['text'])
    tails.append(dict(id=a['id'],tail=c['text'][len(a['text']):]))
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[286] and x['latest_verified_github_checkpoint']['continuation']==295
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
U=R/'primary-data-LOCALONLY/P16.7-ROOT412-finite-grid-fibre-and-calibration-source-20261009';assert not U.exists();U.mkdir()
specs=[('1216-CLD-18.6.1-LF27560-27607-LOCALONLY.txt',[27560,27607]),
    ('1217-CLD-18.6.2-LF27608-27671-LOCALONLY.txt',[27608,27671]),
    ('CLD-14.5.2-3-through-proof-end.txt',[20953,21042])]
units=[]
for fn,lf in specs:
    src=A/'LOCALONLY-primary'/fn;dst=U/fn;shutil.copyfile(src,dst)
    units.append(dict(path=str(dst),bytes=dst.stat().st_size,sha256=sha(dst),origin=str(src),real_LF=lf,
        applied_immediate_statements_and_complete_proofs_ROOT_physically_read=True,irrelevant_partial_neighbor_units_NOT_claimed_applied=True,LOCALONLY=True))
programs=[A/x for x in ['build_deliverables.py','check_delivery.py','read_packet.py','read_primary.py','verify_progress.py','write_notes.py']]
now=datetime.now(timezone.utc).isoformat();D.mkdir()
(D/'native-entire-scoped-paper-DATA.txt').write_text(paper);(D/'scoped-paper.tex').write_text(corrected)
(D/'native-entire-proof-companion-DATA.txt').write_text(companion)
(D/'proof-companion.txt').write_text(companion.replace(paper,corrected,1))
for fn in ['source-application-reading-ledger.txt','source-application-reading-ledger.json','original-residual.txt','scoped-verdict.json','final-notes.json','n1.txt','n2.txt','n3.txt','n4.txt']:
    shutil.copyfile(A/fn,D/fn)
shutil.copyfile(K/'round285-raw-native-actual-FINAL.json',D/'raw-native-actual-FINAL.json')
shutil.copyfile(K/'round285-terminal-actual-final-ROOT-retention-20261009.json',D/'terminal-actual-FINAL-retention.json')
clarification=dict(recorded_utc=now,scope='Make nonempty fixed-test choice explicit, including the singleton N=1 grid; no theorem expansion',
    native_source_sha256=sha(A/'scoped-paper.tex'),ROOT_source_sha256=sha(D/'scoped-paper.tex'),
    source_difference=''.join(difflib.unified_diff(paper.splitlines(True),corrected.splitlines(True),fromfile='native-entire-scoped-paper-DATA',tofile='ROOT-scoped-paper')),
    all_other_source_characters_preserved=True,mathematical_certification=False)
write(D/'ROOT-nonempty-grid-test-list-clarification.json',clarification)
audit=dict(recorded_utc=now,paper=412,round=285,UNREVIEWED=True,accepted=False,original_closed=False,actual_expanded_pairs=pairs,
    entire_current_592_line_formal_source_and_unique_ledger_residual_ROOT_physically_read=True,
    whole_native_and_corrected_companion_component_identity=True,native_reading_ledger_historical_claims_NOT_ROOT_recursive_receipts=True,
    whole_historical_1224_primary_manifest_and_books_NOT_ROOT_newly_read=True,incoming_correctness_grants=[],ROOT_fresh_primary_units=units,
    native_programs_physically_read_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],
    native_or_supplied_programs_executed_or_imported=False,terminal_tails=tails,ROOT_grid_test_clarification=clarification,
    new_ROOT_reconstruction=['Exact midpoint cubic deficit I/8 from affine positive second derivative',
        'Actual fixed Gauss-fibre path gradient bounds, finite grids and normalized reference values give Omega_C(I)->0',
        'Continuous smooth absolute-value derivative, signed Radon Green pairing and all-test estimate yield both endpoint absolute moving moments',
        'Tangent at each endpoint and actual finite maximum give both maximum energy gains <=H_C(I)',
        'Actual point atoms plus ordered energy-gap modulus give Cauchyness at EVERY full2 point without a uniform-in-x assertion',
        'Variational deficits bound I<=4(sum deficits) on actual normalized sublevels',
        'Finite bounded-MA domination gives scoped coercivity, L1(mu) and measurable limits, never an analytic representative'],
    ROOT411_separate_later_new_input='Universal finite-full-dual coercivity/solid domination/normalized Dirac duals are proved separately in ROOT411; not supplied to active285 or286',
    unresolved=['Nonordered actual analytic representative/compactness','Adequate intrinsic finite-energy domain','Actual envelopes/orthogonality or sufficient replacements',
        'EVERY arbitrary-support finiteFULLdual prescribed-measure existence','Entire deeper historical geometric/generated/descent primary audit'],
    primary_bodies_pixels_books_LOCALONLY=True,compiler_pending=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(D/'ROOT-whole-serialization-source-application-and-scope-audit.json',audit)
(D/'ROOT-review-scope.txt').write_text('Whole working paper412, UNREVIEWED; original P16.7 OPEN. All four actual five-field notes, all literal expanded five-field dictionaries, ENTIRE592-line native formal source and unique ledgers/residual/verdict were ROOT physically read. Native programs read as DATA and NEVER imported/executed. The sole ROOT formal clarification includes the zero test in every finite-grid list and chooses A1=0 for N=1; native entire source/companion remain separately unchanged.\n\nNew nonordered bounded midpoint, endpoint absolute-moment, finite maximum-energy and all-full-point Cauchy proofs are reconstructed under their qualified actual Green/CLD/GR hypotheses. Fresh complete immediate CLD18.6.1--2 and14.5.2--3-through-proof-end bodies were read for fixed-fibre path/calibration applications. Deeper conventional and historical chains remain qualified, not freshly recursively certified. Complete actual analytic nonordered representation/compactness and general prescribed-measure existence remain OPEN. ROOT411 independently proves universal coercivity beyond this native finite-domination sector; it was authored after native285 freeze and is a separate future input. Compiler pending. Counts16solved26OPEN97accepted unchanged; primary bodies/pixels/books LOCALONLY; protected editor OPEN UNCHANGED.\n')
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=412,round=285,whole_paper=dict(path=str(D/'scoped-paper.tex'),bytes=len(corrected.encode()),sha256=sha(D/'scoped-paper.tex')),
    public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file()],
    UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=audit['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,native285_whole_unreviewed_paper412=dict(directory=str(D),binding=str(B),sha256=sha(B)),
        next_work='Compile whole412 and combine nonordered midpoint/absolute moments/maximum-energy with whole ROOT411 universal coercivity. Freeze287 original P16.7 representability/envelopes/existence with whole411412, native286 continues. Regular verified NONFORCE296, at mostTWO, counts/editor unchanged.')
    write(p,x)
print(json.dumps(dict(paper=412,directory=str(D),source_bytes=len(corrected.encode()),source_sha256=sha(D/'scoped-paper.tex'),native_source_bytes=len(paper.encode()),
    primary_units=len(units),terminal_tails=tails,compiler='pending',original_closed=False),ensure_ascii=False,indent=2))
