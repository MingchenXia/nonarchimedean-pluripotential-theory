from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, re
R=Path('/workspace/research'); K=R/'root-checks'
S=R/'primary-data-LOCALONLY/P12.3-formal-Noether-different-primary-20261009'
W=S/'dependencies-LOCALONLY'; V=W/'Wang1994-pages-and-OCR-LOCALONLY'
P=K/'P12.3-continuation392-Noether-different-and-completed-Cartier-products-working-paper-20261009.tex'
B=K/'P12.3-continuation392-ROOT-whole-proof-source-scope-and-binding-20261009.json'
Q=K/'P12.3-Wang1994-formal-normalization-ROOT-primary-pixel-reading-scope-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not Q.exists() and sha(B)=='c5164cdedc0184639122196ae03997cd441a3dfd7d859820cdd080892d1733a8'
assert sha(W/'Wang1994-official.pdf')=='c1d47394134659e0b6f56ad4398b7c24e5aad57a713a3718ad71a2c0c7f11b99'
assert sha(W/'Wang1994-official-full-OCR-LOCALONLY.txt')=='89a013dce6e2d04b05284127fb9683186d65370a20c904a30d5bdb65abf933f8'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat(); pages=[]
for n in range(11,17):
    p=V/f'page-{n:02d}.png'; pages.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),PDF_one_based_page=n,printed_page=n+586,ROOT_actual_pixels_physically_viewed=True,detail='original'))
record=dict(recorded_utc=now,official_full_scanned_PDF=dict(path=str(W/'Wang1994-official.pdf'),bytes=(W/'Wang1994-official.pdf').stat().st_size,sha256=sha(W/'Wang1994-official.pdf'),pages=22),full_OCR=dict(path=str(W/'Wang1994-official-full-OCR-LOCALONLY.txt'),bytes=45862,sha256=sha(W/'Wang1994-official-full-OCR-LOCALONLY.txt'),retained_complete=True,NOT_whole_physically_read=True,OCR_not_pixels=True),physically_viewed_pages=pages,entire_applied_units=['Definition4.1 fixed coefficient-field normalizations and Definition4.2 finite-presentation relative Jacobian, printed597','Lemma4.3 full statement and ENTIRE immediate proof, printed598','Proposition4.4 full statement and immediate proof printed598--599; char0 context only','Proposition4.5 full statement printed599 and ENTIRE postponed proof printed601--602; exact complete equidimensional perfect-characteristic-p hypotheses; cited universal-finite/analytic backgrounds not all recursively read'],context_read=['Definition4.6, Remark4.7, Proposition4.8 with its citation, Remark4.9, Proposition4.10 and full proof, Corollary4.11 with full proof, Definition4.12, Proposition4.13 statement, Theorem4.14 statement and entire proof printed599--601'],scope_correction='Wang4.3 sum uses the fixed coefficient field and parameter power-series normalizations. ROOT392 now uses exactly that sum, sufficient for its primary multiplier. Other regular finite subrings remain allowed by the direct root/lift theorem but are not needed for this source identification.',finite_field_scope='Prime-avoidance choices may alter minimal generators by m^2; no assumption of infinite residue field. Draft supplies explicit finite-prime avoidance explanation, independently unreviewed.',deeper_background_not_fresh_whole_audited=['Wang references4/6 for universal-finite derivations and analytic separability','Complete formal Jacobian criterion entire recursive tree','Whole Wang22page paper','Whole ITjac3/Liu/Ua22/Dao primary papers'],all_full_primary_PDF_OCR_pixels_and_literal_units_LOCALONLY=True,source_program_execution_or_import=False,new_correctness_grant=False,accepted_paper=False,original_closed=False)
write(Q,record)
shutil.copyfile(B,W/'ROOT392-first-binding-before-pixel-correction-LOCALONLY.json')
x=load(B); x['recorded_utc']=now; x['supersedes_previous_unpublished_binding_sha256']='c5164cdedc0184639122196ae03997cd441a3dfd7d859820cdd080892d1733a8'
x['paper']=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P),ROOT_entire_current_source_physically_read_untruncated=True,whole_read='Entire saved amended paper, one untruncated tool output; prior full body and changed paragraph separately read')
x['fresh_Wang_pixel_record']=dict(path=str(Q),sha256=sha(Q),full_immediate_Lemma4_3_and_Proposition4_5_proofs_physically_read=True)
x['source_boundary']='Exact ITjac3/Liu units and actual officialWang597--602 pixels read. Fixed-coefficient-field normalization sum now matches Wang4.3. Full formalJacobian criterion recursive background remains named published foundation, not new reading credit. Full source bodies/pixels LOCALONLY.'
x['new_direct_proof_scope'][4]='Fixed coefficient-field normalizationJacobian generators have compatible lifts, finite sums possibly different normalizations; direct theorem also allows other regular finite subrings'
text=P.read_text(); stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',text):
    if m[1]=='begin':stack.append(m[2])
    else:assert stack and stack.pop()==m[2]
assert not stack and text.count('\\[')==text.count('\\]') and len(re.findall(r'(?<!\\)\$',text))%2==0
write(B,x)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,latest_unreviewed_ROOT_formal_Noether_different_paper=dict(continuation=392,paper=str(P),paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),fresh_Wang_pixel_record=str(Q),accepted=False,original_closed=False));write(p,x)
print(json.dumps(dict(paper_bytes=P.stat().st_size,paper_sha256=sha(P),binding_sha256=sha(B),Wang_reading_record_sha256=sha(Q),new_correctness_grant=False,original_closed=False),indent=2))
