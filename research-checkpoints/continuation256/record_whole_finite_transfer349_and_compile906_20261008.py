from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';P=R/'primary-data-LOCALONLY/P12.6-finite-flat-geometric-transfer-20261008'
W=K/'P12.6-continuation349-normal-and-flat-envelope-transfer-single-trace-slot-projection-and-towers-working-proof-20261008.md'
B=K/'P12.6-continuation349-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
D=K/'public-P12.4-continuation345-supported-Cartier-products-and-bounded-locality-original-candidate'
Q=D/'builtin-compiler906-unavailable-observation-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not B.exists() and not Q.exists()
assert W.stat().st_size==23720
assert sha(D/'P12.4-paper.tex')=='33f59bd3c4c504aec02aedfceca4d32fdb0ebde83e1be837ce10ab966550a6ed'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
sources=json.loads((P/'acquisition-records.json').read_text());bindings=[]
for e in sources:
    for kind in ['html','text']:
        p=Path(e[kind+'_path']);assert sha(p)==e[kind+'_sha256'] and p.stat().st_size==e[kind+'_bytes'];bindings.append(bind(p))
now=datetime.now(timezone.utc).isoformat()
write(B,dict(recorded_utc=now,continuation=349,atom='P12.6',proof=bind(W),status='Complete UNREVIEWED working proof; originalOPEN, no paperaccepted',ROOT_whole_reading='Entire saved proof physically read in summary-preserved0:17000 and fresh16500:end; fresh0:16500 repeated. All units complete without output truncation. Both immediate official primary units text fully physically read; no new PDFpixel or recursive-full-proof claim.',only_prerequisites=['Entire qualifiedG331 normal-domain trace/fullpositive descent','Entire qualifiedG345 actualgeometric supported products/boundedcalculus'],new_results=['Normal-target/no-vertical finitefibre maximum C/D and exact unrestricted RAWenvelope identity','ExactlyONE arbitrarysourcepotential mixedtrace projection with inseparability and actualgeometric finiteprojection reconstructed','Fullconductor-admissible single-trace-slot identity','Reducedfiniteflat determinanttrace fullsupport includingArtinianfiberlengths; automaticconductor admissibility and geometricproduct identity','Reducedfiniteflat C/D fibremaximum and unrestrictedRAWenvelope identity','Unnormalizedtrace/projection towers; varyingdegree normalizedaverages obstruction; ONEgaugefactor'],limitations='Neither ROOT348/349 is an incomingcorrectnessgrant. No P12.3 generalenvelope regularity/arbitrarysupclass; no universalnonnormal max/trace; no severalnonpulledtraceproductidentity; noninjective maps factor exactimage without quotientpshextension or closed-imageenvelopecommutation.',private_primary_full_units=bindings,acquisition_metadata=bind(P/'acquisition-records.json'),fresh_source_units=['Stacks0BD2 CURRENT31.18.6 fullstatement/immediateproof','Stacks00HS10.39.19 fullstatement/immediateproof'],book_fragment_context=bind(R/'book-source/manuscript/parts/part6/fragments/ch70_finite_transfer_conductor.tex'),book_fragment_reading='Priorfreshphysical lines275--440 only, mathematicalCONTEXTDATA not wholefragment/acceptedgrant/authority.',source_bodies_pixels_LOCALONLY=True,private_ACTIVE252_253_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True))
write(Q,dict(recorded_utc=now,source=bind(D/'P12.4-paper.tex'),builtin_compiler_call='functions.exec cell906 started approximately15:30 UTC',observed_exact_tool_output='No handler registered for tool: codex_app.compile_latex_document',observation='functions.wait906 completed at16:44:34 UTC with unavailabletoolhandler; no LaTeXdiagnostics or compiledPDF returned.',compilation_verified=False,compiler_success_claimed=False,PDF_export_claimed=False,mathematical_acceptance95_unchanged=True,source_modified=False,new_editor_tab_opened=False,protected_P16_editor_open_unchanged=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==14 and x['remaining_open_original_atoms']==28 and x['historical_reviewed_scoped_papers']==95 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,P12_6_ROOT349=dict(proof=str(W),binding=str(B),status='Whole UNREVIEWED proof physically ROOTread, NOTsuppliednative252253; noacceptance'),P12_4_builtin_compile906=dict(status='UNVERIFIED unavailabletoolhandler',observation=str(Q)),next_work='Capture completed252 actual FINAL and whole independent P12.5 proof/source/scope. Native253 P12.6 stillactive; doNOThotfeednew349. Checkpoint256 new349/privateprimarymetadata/compileunavailableobservation.14solved28OPEN95papers; protectededitorunchanged.')
    write(p,x)
print(json.dumps(dict(ROOT349=bind(W),binding=bind(B),compiler906_unverified_observation=bind(Q),counts_unchanged=True),indent=2))
