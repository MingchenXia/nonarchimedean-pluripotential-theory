from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
R = Path('/workspace/research'); K = R/'root-checks'
A276 = R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual/artifacts/codex-9EYfi9'
A277 = R/'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation/artifacts/codex-9XWoHU'
D396 = K/'public-P12.3-continuation396-corrected-formal-BIG-and-isolated-CE-unreviewed'
D397 = K/'public-P16.7-continuation397-generated-operator-and-all-test-I-estimate-unreviewed'
assert not D396.exists() and not D397.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in [276,277]:
    x=json.loads((K/f'round{n}-raw-native-actual-FINAL.json').read_text()); assert not x['candidate']
old = 'Since d^q T subset P, compose multiplication by d^q in the first factor, Psi, and 1 tensor phi. This is an S-linear map T completed-tensor T->S and after mu it is phi(d^q z)=d phi(z).'
new = 'Since d T subset P in ROOT-MODULE notation, compose multiplication by d in the first root factor, Psi, and 1 tensor phi. This is an S-linear map T completed-tensor T->S and after mu it is phi(d z)=d phi(z).'
proof=(A276/'whole-proof.md').read_text(); assert proof.count(old)==1
fixed=proof.replace(old,new)
tex=(A276/'P12.3-formal-BIG-and-envelope.tex').read_text()
table={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','$':r'\$','%':r'\%','&':r'\&','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
escape=lambda s: ''.join(table.get(c,c) for c in s)
assert tex.count(escape(old))==1
tex=tex.replace(escape(old),escape(new))
correction=r'''
\section*{ROOT correction and current review boundary}
This is a new corrected working-paper version, not the immutable native
FINAL. The actual native276 root-module paragraph wrote multiplication
by $d^q$ and $\phi(d^q z)=d\phi(z)$ for an $R$-linear map
$\phi:R^{1/q}\to R$. That formula is false in root-module notation.
The inclusion proved immediately before it is $dR^{1/q}\subset P$.
The corrected lift precomposes multiplication by $d$ on $R^{1/q}$,
then the completed free-module lift, then $1\widehat\otimes\phi$.
Under root multiplication its diagonal reduction is
$\phi(dzw)=d\phi(zw)$ for all pure root tensors, and hence for the
completed finite module by continuity. It preserves the entire root
kernel because this reduction factors through multiplication.
The standard isomorphism $F_*^eR\to R^{1/q}$, $F_*^ez\mapsto z^{1/q}$,
identifies this root multiplication by $d$ with multiplication by
$d^q$ on the underlying Frobenius source. Thus the Frobenius-source
formula is $\phi(F_*^e(d^q z))=d\phi(F_*^ez)$.
The output multiplier and subsequent all-degree different/diagonal
inclusion are unchanged after this explicit correction; their complete
mathematical claims still require independent review.

All seven actual native276 note bodies and all five fields were read.
The complete source bodies and actual FINAL are retained separately.
Entire proof and metadata blocks match the standalone source under an
independently implemented serialization; literal historical grant and
appendix matching is identity, not a fresh recursive proof reading.
The immediately applied CEMS Setting2.1, Definition2.2, Lemmas2.3--2.4
and their whole immediate proofs, and Stacks15.27.3--4 with the
15.8.8--9 criteria, were freshly read at their exact hypotheses.
Historical Wang pixel-reading and other qualified foundations remain
attached. Sources, literal source units, pixels and whole book chapters
remain local. No native or supplied program was executed or imported.
The formal BIG and isolated perfect-residue characteristic-$p$ CE
claims are UNREVIEWED. General original P12.3 remains OPEN.
'''
tex=tex.replace('\\maketitle\n','\\maketitle\n'+correction,1)
D396.mkdir(); D397.mkdir()
(D396/'whole-proof-corrected.md').write_text(fixed)
(D396/'P12.3-paper.tex').write_text(tex)
for name in ['native-notes.json','expanded-notes.json','whole-proof.md','whole-reading-ledger.md','whole-source-application-ledger.md','coverage.md','independent-scoped-verdict.md','original-residual.md']:
    shutil.copyfile(A276/name,D396/('native-UNREVIEWED-'+name))
for name in ['final-notes.json','proof-companion.md','scoped-paper.tex','source-application-ledger.md','scoped-verdict.json','n1.md','n2.md','n3.md','n4.md','n5.md']:
    shutil.copyfile(A277/name,D397/name)
for n,d in [(276,D396),(277,D397)]:
    shutil.copyfile(K/f'round{n}-raw-native-actual-FINAL.json',d/'actual-native-FINAL.json')
    shutil.copyfile(K/f'round{n}-terminal-actual-final-ROOT-retention-20261009.json',d/'terminal-actual-FINAL-retention.json')
    files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),whole_body=True) for p in sorted(d.iterdir()) if p.is_file()]
    b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=n,continuation=396 if n==276 else 397,status='UNREVIEWED scoped mathematical working paper; no correctness grant',public_files=files,actual_FINAL_is_authoritative_separate_record=True,actual_equals_artifact_semantic_notes=n==276,all_actual_note_bodies_and_all_five_fields_physically_ROOT_read=True,expanded_mathematical_bodies_physically_ROOT_read=n==277,exact_entire_serialization_audit=str(K/'round276277-ROOT-whole-serialization-and-unique-framing-audit-20261009.json'),entire_unique_source_framing_physically_ROOT_read=True,duplicate_matching_NOT_fresh_duplicate_or_recursive_reading=True,supplied_or_native_programs_executed_or_imported=False,compiler_UNVERIFIED=True,accepted=False,original_closed=False,all_full_primary_sources_units_pixels_whole_books_LOCALONLY=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
    if n==276:
        b.update(ROOT_mathematical_correction=dict(original_paragraph=old,corrected_paragraph=new,root_source_multiplier='d',underlying_Frobenius_source_multiplier='d^q',output_multiplier='d',immutable_native_artifacts_unchanged=True,corrected_theorem_reuse_requires_this_record=True),direct_scope=['completed-diagonal BIG subadditivity draft over complete normal char-p perfect-residue rings','entire isolated formal CE draft on every semivaluation support'],original_residual=['nonisolated normal dimension>=3','mixed characteristic/imperfect/general excellent cases','general Jensen lower hemicontinuity'])
    else:
        b.update(direct_scope=['all-stage generated analytic MA and mixed operators','all-test I bound coefficient42','bounded continuous local divisor-current consequence'],original_residual=['intrinsic recognition and actual generated representative closure','separated normalized sublevel compactness','envelopes/orthogonality','every finite-full-dual arbitrary-support equation','full uniqueness modulo constants'],actual_and_expanded_all_five_texts_DIFFER=True,CLD_PL_fresh_ROOT_literal_LF=[23458,23671],CLD_primary_pixels_freshly_read=False,ROOT394395_bridge_NOT_in_native277_frozen_input=True)
    write(d/'ROOT-whole-proof-source-scope-and-binding.json',b)
print(json.dumps(dict(staged=[str(D396),str(D397)],root_correction_applied_once=True,accepted=False,original_closed=False,protected_editor_open_unchanged=True),indent=2))
