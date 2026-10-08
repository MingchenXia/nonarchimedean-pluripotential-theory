from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-248').iterdir())
A=C/'artifacts/codex-n1GL1o';D=K/'public-P12.4-continuation341-bounded-moment-measures-and-geometric-curve-reference-unreviewed'
E=D/'independent-review248'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bound(p):p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not E.exists()
own=json.loads((A/'reports/own-bindings.json').read_text())['files'];inputs=json.loads((A/'reports/input-bindings.json').read_text())
assert len(own)==109 and len(inputs)==57
for e in own:
    p=A/e['path'];assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
for e in inputs:
    for p in [Path(e['source']),A/e['local']]:assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
current=json.loads((C/'input.json').read_text());native=json.loads((A/'input.json').read_text());assert current==native and [n['id'] for n in current['notes']]==['G331']
actual=json.loads((K/'round248-actual-native-final.json').read_text());expanded=json.loads((A/'native-notes.json').read_text());assert len(actual['notes'])==len(expanded['notes'])==7 and actual['candidate']==expanded['candidate']==False
matrix=[{key:u[key]==v[key] for key in ['id','summary','detailedSummary','text','support']} for u,v in zip(actual['notes'],expanded['notes'])]
E.mkdir()
for name in ['independent-review.md','whole-proof.md','whole-source-application-ledger.md','whole-proof-coverage.md','original-scope-and-noncircularity.md','acceptance-decision.json','native-notes.json','source-qualification-addendum.md','bounded-evidence-input.json','n1.md','n2.md','n3.md','n4.md','n5.md','n6.md','n7.md']:shutil.copyfile(A/name,E/name)
reports=E/'reports';reports.mkdir()
for p in sorted((A/'reports').iterdir()):
    if p.is_file() and p.suffix in ['.json','.md']:shutil.copyfile(p,reports/p.name)
for folder in ['review-data/actual','review-data/expanded']:
    t=E/folder;t.mkdir(parents=True)
    for p in sorted((A/folder).iterdir()):
        if p.is_file() and p.suffix=='.json':shutil.copyfile(p,t/p.name)
inert=E/'inert-reviewer-programs-DATA';inert.mkdir()
for name in ['audit_packets.py','own_evidence.py','finish_review.py']:shutil.copyfile(A/name,inert/name)
shutil.copyfile(K/'round248-actual-native-final.json',E/'actual-native-FINAL.json')
assert sha(D/'P12.4-paper.tex')=='d1b40bf37d047f5f37ec7a47880ac51c1e78e37bba03a043f3e6bffa61454633'
assert sha(D/'P12.4-paper.pdf')=='e26b42a63c4b06d5b592224f02d4ed000a381d2c2a1212811ed1d0ff2fdf299b'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=248,continuation=341,status='Whole independent review ROOT read; delimited mathematical scopePASS with mandatory source qualification; finalpaperacceptancepending',
    ROOT_every_actual_FINAL_note_field_physically_read=True,ROOT_whole_independent_proof_and_source_scope_physically_read=True,whole_proof_read_chunks='0:18000 and18000:end; entire independentreview,sourceledger,sourceaddendum,coverage,scope and decision read.',
    ROOT_prior_whole_author_TeX_and_actual_FINAL_read=True,ROOT_parallel_author_argument_separately_whole_read=False,
    own_records=109,input_bound_bodies=57,input_source_and_retained_body_checks=114,all_current_bindings_match=True,current_native_whole_inputs_equal=True,
    actual_expanded_whole_equal=actual==expanded,actual_expanded_fields_equal=matrix,review_actual_FINAL=bound(E/'actual-native-FINAL.json'),whole_independent_proof=bound(E/'whole-proof.md'),source_qualification=bound(E/'source-qualification-addendum.md'),
    primary_source_pixel_ROOT_actually_viewed=bound(A/'reports/source-pages/SH-356.png'),pixel_reading='SHprinted356: confirms the colon length is unquotiented. ThisROOTfreshpixelread is only thispage, notallsourcepages.',
    source_application_correction='Use finite annihilator in final parameter quotient, equivalently colon modulo previous parameter submodule. RepeatedSH17.4.6 regular argument remains valid; literal17.4.7 printing not adopted.',
    reviewer_historical_author_evidence='Reviewer57suppliedbodies includes21historicalevidence;54of62oldownentriesavailable. ROOTseparatelycheckedall62physicalauthorownand62inputbodiesbeforeD341stage. No unavailablefreshreview attestation is invented.',
    immutable_author_source_pdf_unchanged=True,primary_bodies_extracts_pixels_and_private_provider_output_not_copied=True,supplied_programs_ROOT_executed_or_imported=False,
    original_closed=False,paper_accepted=False,original_candidate=False,counts_unchanged=dict(solved=13,open=29,papers=93),protected_editor_open_unchanged=True)
(D/'ROOT-independent-review248-whole-reading-and-binding-20261008.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(directory=str(E),checked_own=len(own),checked_input_bodies=len(inputs),source_sha256=sha(D/'P12.4-paper.tex'),original_closed=False),indent=2))
