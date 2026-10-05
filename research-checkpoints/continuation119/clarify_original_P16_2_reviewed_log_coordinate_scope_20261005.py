from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json,shutil,subprocess
R=Path('/workspace/research');D=R/'deliverables/original-P16.2';p=D/'P16.2-core.md'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(p)=='4b8934b31ebf1fdafb613fedacaf97dd2c41d9b0d9a224664db8f0123d662a25'
v=json.loads((R/'root-checks/P16.2-round115-actual-full-original-review-20261005.json').read_text())
paragraph=next(x for x in v['report'].split('\n\n') if 'Continuity alone would not establish factorization' in x)
assert 'explicit functions of logarithmic coordinates' in paragraph
S=D/'prior-checkpoint118';assert not S.exists();S.mkdir()
for name in ['P16.2-core.md','P16.2-paper.tex','P16.2-paper.pdf','P16.2-original-closure.json','publication-build-and-root-reading.json']:
    shutil.copyfile(D/name,S/name)
old=p.read_text();text=old
before='The support inequality and equality have the **same constant**. Finite-floor logarithmic maxima'
after='The support inequality and equality have the **same constant**. Each finite selection is a specified single function of its logarithmic coordinate vector, with affine pieces supplied on that coordinate image. Every finite affine FS maximum used in Section 10 has this property. Continuity alone does not imply factorization of an arbitrary fiber-dependent selector; no such selector is included here. Finite-floor logarithmic maxima'
assert text.count(before)==1;text=text.replace(before,after)
before='Suppose a finite continuous rational-affine selection is supplied near a compact set and its used coordinates are unit logarithms there.'
after='Suppose a finite continuous rational-affine function of the specified logarithmic coordinates is supplied near a compact set, with unit coordinates there and its finite affine selection rule given on the coordinate image.'
assert text.count(before)==1;text=text.replace(before,after)
p.write_text(text)
(D/'P16.2-core.reviewed-log-coordinate-scope.patch').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),text.splitlines(True),fromfile='checkpoint118/P16.2-core.md',tofile='current/P16.2-core.md')))
subprocess.run(['pandoc',str(p),'--standalone','--from=markdown+tex_math_dollars','--to=latex',
    '--pdf-engine=xelatex','--output',str(D/'P16.2-paper.tex')],check=True,capture_output=True,text=True)
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'reason':'Make the published auxiliary lemma state precisely the logarithmic-coordinate factorization already checked in canonical review115. An arbitrary pointwise selector would be an unjustified broader claim.',
    'actual_canonical_scope_paragraph':paragraph,'canonical_operation_id':v['operationId'],
    'old_core_sha256':sha(S/'P16.2-core.md'),'core_sha256':sha(p),
    'old_tex_sha256':sha(S/'P16.2-paper.tex'),'tex_sha256':sha(D/'P16.2-paper.tex'),
    'old_PDF_sha256':sha(S/'P16.2-paper.pdf'),
    'accepted_original_theorem_or_generated_operator_category_changed':False,
    'new_unreviewed_mathematical_premise_imported':False,
    'historical_review_and_checkpoint118_preserved':True,
    'PDF_rebuild_and_native_compile_pending':True,
    'original_count_incremented':False,'existing_P16_4_editor_changed_or_new_tab_opened':False}
(D/'publication-reviewed-log-coordinate-scope-clarification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'core_sha256':sha(p),'tex_sha256':sha(D/'P16.2-paper.tex'),
    'original_count_unchanged':7,'native_compile_and_PDF_rebuild_pending':True},indent=2))
