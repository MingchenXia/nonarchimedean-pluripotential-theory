from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
dictionary=R/'campaigns/round-99/P16.1-original-self-contained-full-review/primary-literal-body-dictionary.json'
expected='874dd983a3cbaf8744b9beaf27b49bcf2305591c97e411699dfd91d6b420cceb'
body=json.loads(dictionary.read_text())[expected]
assert hashlib.sha256(body.encode()).hexdigest()==expected
unit=K/'P16-Ducros-published3.2-whole-selected-statement-and-proof-20261005.txt'
assert not unit.exists();unit.write_bytes(body.encode())
responses=[K/'P16-root-independent-Ducros-first-fetch-failure-20261005.json',
           K/'P16-root-independent-Ducros-published-and-erratum-response-20261005.json',
           K/'P16-root-independent-Ducros-complete3.2-response-20261005.json']
save(K/'P16-root-independent-Ducros-density-and-erratum-observation-20261005.json',{
    'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'published_primary_URL':'https://cml.centre-mersenne.org/item/10.1142/S1793744212500077.pdf',
    'version':'Published Confluentes Mathematici4(4)1250007, DOI10.1142/S1793744212500077',
    'selected_whole3_2_unit':str(unit),'selected_whole3_2_sha256':sha(unit),
    'original_dictionary':str(dictionary),'original_dictionary_sha256':sha(dictionary),
    'original_source_local_inclusive_one_based_LF':[2077,2155],
    'original_full_text':'/workspace/research/shared-sources/Ducros-published-1250007-20261005-continuation72.txt',
    'original_full_text_sha256':sha(R/'shared-sources/Ducros-published-1250007-20261005-continuation72.txt'),
    'entire_selected3_2_statement_and_printed_proof_root_read':True,
    'fresh_complete3_2_renderer_reference':'turn612821view0',
    'fresh_complete3_2_renderer_lines':[2029,2113],
    'fresh_density_subproof_renderer_lines':[2064,2083],
    'first_native_fetch_failed':True,'retry_native_published_PDF_fetch_succeeded':True,
    'actual_native_responses':[{'path':str(p),'sha256':sha(p)} for p in responses],
    'erratum_URL':'https://www.numdam.org/item/10.5802/cml.7.pdf',
    'erratum_version':'Confluentes Mathematici5(2)(2013)47--48, DOI10.5802/cml.7',
    'erratum_native_renderer_reference':'turn441776view0',
    'entire_erratum_printed_body_root_read':True,'erratum_renderer_read_lines':[0,161],
    'erratum_subject':'Replacement of the page36 finite universally separating function argument in2.8 by a model-theoretic finite-basis argument.',
    'application':'Common collars use only3.2 compact unit norm-images and3.2.1 principal-localization density; the erroneous2.8 finite separating function argument is not used in this application.',
    'whole57_page_original_work_root_read':False,
    'all_recursively_referenced_background_proofs_read':False,
    'original_full_review_or_original_closure_claimed':False,
    'native114_115_private_outputs_read_or_used':False,'hot_feedback_sent':False,
    'whole_third_party_PDF_downloaded_or_published_by_this_helper':False})
print(json.dumps({'selected_unit':str(unit),'selected_sha256':sha(unit),
    'observation':str(K/'P16-root-independent-Ducros-density-and-erratum-observation-20261005.json'),
    'original_count_incremented':False},indent=2))
