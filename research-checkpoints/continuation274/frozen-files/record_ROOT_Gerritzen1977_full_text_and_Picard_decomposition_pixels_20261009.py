from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
S=Path('/workspace/research/primary-data-LOCALONLY/P16.7-polyannulus-Picard-primary-20261008')
T=S/'Gerritzen-1977-Picard-decompositions.txt'; P=S/'Gerritzen-1977-Picard-decompositions.pdf'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(T)=='43304b8cbb8dc196b22bf2f72489174c5f9a4e503c0cdcbf85ea53c91e60cc4c'
assert sha(P)=='c0add5d770881409d357722aa497d7df4d4270ac5745d43c2ca1c17fa67895a7'
lines=T.read_bytes().split(b'\n'); assert len(lines)==1015 and lines[-1]==b'\x0c'
U=S/'ROOT-full-Gerritzen1977-section3.1-3.2-LF581-711-LOCALONLY.txt'
O=S/'public-ROOT-Gerritzen1977-full-text-and-decomposition-reading.json'
assert not U.exists() and not O.exists()
U.write_bytes(b'\n'.join(lines[580:711])+b'\n'); images=[]
for i in [10,11,12]:
    p=S/f'ROOT-Gerritzen-1977-PDF-{i}.png'; assert p.is_file()
    images.append(dict(path=str(p),PDF_one_based_page=i,printed_page=i+21,bytes=p.stat().st_size,sha256=sha(p),fresh_ROOT_whole_pixel_physically_read=True,LOCALONLY=True))
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source_title='L. Gerritzen, Zerlegungen der Picard-Gruppe nichtarchimedischer holomorpher Räume, Compositio35(1977),23-38',source_url='https://www.numdam.org/item/CM_1977__35_1_23_0.pdf',source_PDF_sha256=sha(P),source_text_sha256=sha(T),entire_retained_1015_LF_delimited_segments_ROOT_physically_read_untruncated=True,source_final_segment_is_form_feed=True,physical_text_intervals_inclusive=[[1,180],[181,400],[401,640],[641,840],[841,1014],[1014,1015]],OCR_missing_formulas_not_fabricated=True,fresh_whole_pixels=images,literal_unit=dict(path=str(U),bytes=U.stat().st_size,sha256=sha(U),inclusive_LF_interval=[581,711],LOCALONLY=True),pixel_exact_scope='Entire sections3.1 and3.2, Theorems2/3 statements and immediate unit-group/sheaf derivations, Lemma6 statement and its entire immediate factorization proof, with OCR-missing formulas checked on printed31-33.',source_stated_decompositions=['Pic(X times E) = Pic(X) directsum H1(X,G1)','Pic(X times L) = Pic(X) directsum H1(X,G1) directsum H1(X,Gminus1) directsum H1(X,Z_X)'],hypotheses='k complete nontrivially non-Archimedean, X holomorphic space in source sense; E closed unit disc, L its boundary unit circle, sheaves/cohomology in holomorphic G-topology. The connected affinoid unit decomposition is local; exponent term sheaf Z_X accounts for components.',exact_G1='Strictly convergent power series units with constant coefficient1, higher coefficients pointwise modulus<1; Gminus1 same negative powers.',source_dependency_boundary='Both global Pic decompositions use section2 Theorem1 local triviality over X. Its entire retained OCR text was physically read but not all missing formulas repaired by source pixels. Laurent unit classification also cites Gerritzen1970 Lemma1; deeper cited proof not newly whole-read. No new independent full source correctness grant.',what_this_checks='The source-stated Pic decomposition contains extra cohomology summands, so cannot be invoked as unconditional arbitrary-affinoid Pic homotopy invariance. Does not refute specific pure-factor or hole-filling proof; the extra groups may vanish for its particular factors.',all_full_source_literal_unit_pixels_LOCALONLY=True,no_other_ACTIVE_math_read_or_feedback=True,no_native_or_supplied_program_execution=True,new_accepted_paper=False,whole_original_solved=False)
O.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(public_metadata=str(O),public_metadata_sha256=sha(O),literal_unit_bytes=U.stat().st_size,source_pixels=len(images),new_grant=False,original_closed=False),indent=2))
