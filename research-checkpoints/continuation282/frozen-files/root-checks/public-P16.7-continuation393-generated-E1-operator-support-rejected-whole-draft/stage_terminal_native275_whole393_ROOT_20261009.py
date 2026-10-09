from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator';A=C/'artifacts/codex-yAYOpu'
D=K/'public-P16.7-continuation393-generated-E1-operator-support-rejected-whole-draft'
V=R/'primary-data-LOCALONLY/P16.7-native275-whole-primary-and-evidence-20261009'
B=K/'P16.7-round275-whole-draft393-ROOT-proof-source-scope-and-binding-20261009.json'
Q=K/'round275-ROOT-whole-content-and-CLD-LF-unit-correction-audit-20261009.json'
T=K/'P16.7-native275-terminal-support-rejection-and-data-retention-20261009.json'
Raw=K/'round275-raw-native-final-REJECTED-support.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not V.exists() and not B.exists()
assert sha(Q)=='b69aeceabfd1ab082f92a5eab15270a5a627ed5e0711462945213a9137c1bb25'
q=load(Q);assert load(A/'final-notes.json')==load(Raw)
assert sha(A/'proof-companion.md')=='a7ecffa23f0e39743f2d82c9321ebc045ff4b3238926765f17f84d5b6b0602d2'
assert sha(A/'generated-E1-paper.tex')=='c6d42361bf7191bfbc69e03e7505e63cd65f2e3bed9c3b860661a3027c9ca084'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir();V.mkdir();public=[]
def copy_public(src,name=None):
    src=Path(src);dst=D/(name or src.name);assert 'LOCALONLY' not in dst.name
    shutil.copyfile(src,dst);public.append(dict(path=str(dst),bytes=dst.stat().st_size,sha256=sha(dst),origin=str(src),whole_body=True))
for name in ['n1.md','n2.md','n3.md','n4.md','n5.md','proof-companion.md','generated-E1-paper.tex','source-application-ledger.md','final-notes.json','note-metadata.json','scoped-verdict.json','binding-check.json','version-check.json','finite-checks.json','environment.json','build-checks.json','inspect_packet.py','verify_versions.py','finite_checks.py','build_own.py']:
    copy_public(A/name)
for p in [Raw,Q,T,R/'read_terminal_native275_whole_notes_20261009.py',R/'audit_terminal_native275_whole_identity_and_correct_CLD_units_20261009.py',Path(__file__)]:copy_public(p)
now=datetime.now(timezone.utc).isoformat()
qualification=dict(recorded_utc=now,status='Xean support-rejected terminal raw result retained as whole mathematical DATA; UNREVIEWED scoped draft, no acceptance/import/grant/original closure',actual_FINAL_bytes=46488,artifact_FINAL_bytes=46489,serialization='Five semantic notes exactly identical; key order and terminal newline differ. NO expanded new mathematical bodies.',whole_reading='All five actualFINAL complete fields physically read; all current proof content exactly those bodies plus whole4964byte ledger; uniqueTex preamble/footer physically read and whole encoding independently checked. Identity does not add duplicate physical-reading credit.',source_scope=q['source_boundary'],CLD_unit_correction=q['correction'],new_claims=['Every bounded continuous decreasing presentation of every all-direction generated finite-energy u gives same full-continuous-test analytic MA weaklimit','Mixed weaklimits/fullmass2/finiteboundeddual/selfintegral and actualunboundedfirstvariation','MovingL1 convergence for generated decreasing limits, singular-set comparison/maximum mixedlocality','Exact generated clamp recipes with excluded contactlevels and explicitdiscardedmassbounds'],limits=['Correctness independently UNREVIEWED and Xean rejected invalidsupport string; no registered note import','Full intrinsicE1 recognition and localpluripolar recognition','Separated normalized energy-sublevel compactness','All obstacle/envelope/orthogonality','Existence for EVERY arbitrary-support finitefull-dualmeasure and fulluniqueness'],compiler='UNVERIFIED; built-in request follows without opening new tab',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_hot_feedback=False,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
write(D/'ROOT-qualification.json',qualification)
(D/'README.md').write_text('Whole393: generated finite-energy analytic operator draft\n\nXean native275 settled one call, then BLOCKED its FINAL for an unknown support string in n2. The result is retained here as complete mathematical DATA, with no registered-note import, acceptance or correctness grant. All five actual notes and every unique proof/ledger/TeX segment have been read; the two FINAL serializations have identical semantic bodies but different key order/newline.\n\nThe new unreviewed proof uses bounded-energy polynomial coefficients and a proved full-space dense test lattice to construct all-direction GENERATED E1 Monge--Ampere and mixed weak limits, then finite dual, first variation, moving integrability, comparison, mixed locality and exact clamp restrictions of mass two. Intrinsic recognition/compactness/envelopes/arbitrary-measure existence/full uniqueness remain OPEN. Full proof companion and standalone TeX are included; compiler diagnostics unverified.\n\nROOT388 source-unit extraction had counted FF separators through Python splitlines despite literal-LF descriptors. The correction record identifies that cause, retains the old immutable evidence, and supplies hashes of newly read correct full literal-LF units retained LOCALONLY. All full primary source bodies/pixels and wholebook context remainLOCALONLY. No native programs executed or imported.16solved26OPEN97accepted unchanged; protected P16.4 editor OPEN UNCHANGED.\n')
for name in ['ROOT-qualification.json','README.md']:
    p=D/name;public.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),whole_body=True))
private_sources=[Path(e['path']) for e in load(C/'private-primary-packet-bindings.json')+load(C/'book-context-bindings.json')]+[Path(e['path']) for e in q['fresh_correct_full_primary_units']]+[K/'round275-terminal-inspection-LOCALONLY.json']+[p for p in A.rglob('*') if p.is_file()]
seen={};records=[]
for src in private_sources:
    h=sha(src)
    if h not in seen:
        dst=V/('whole-blob-'+h+src.suffix);shutil.copyfile(src,dst);assert sha(dst)==h;seen[h]=dst
    records.append(dict(origin=str(src),archive_path=str(seen[h]),bytes=src.stat().st_size,sha256=h,whole_body=True,LOCALONLY=True,correctness_grant=False))
write(V/'retention-manifest-LOCALONLY.json',dict(recorded_utc=now,files=records,distinct_whole_blobs=len(seen),all_source_bodies_book_pixels_LOCALONLY=True,retention_not_reading_or_correctness=True))
rec=dict(recorded_utc=now,round=275,continuation=393,status=qualification['status'],public_directory=str(D),public_files=public,whole_reading_and_scope=qualification,source_identity_audit=dict(path=str(Q),sha256=sha(Q)),private_retention=dict(path=str(V),records=len(records),distinct_whole_blobs=len(seen),manifest_sha256=sha(V/'retention-manifest-LOCALONLY.json')),accepted=False,original_closed=False,new_correctness_grant=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
write(B,rec)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['current_active_batch']==[276] and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,latest_whole_unreviewed_P16_7=dict(continuation=393,directory=str(D),binding=str(B),binding_sha256=sha(B),native_status='BLOCKED support rejection; rawDATA only',accepted=False,original_closed=False),next_work='Freeze next independentP16.7 native277 ENTIRE393 including corrected literalLF sourceunits, strict valid support-ID policy. Target intrinsic compactness/envelopes/orthogonality/arbitrary-measure existence/fulluniqueness. Native276 formalBIG remains independent, at mostTWO. Publish282 beforelaunch.');write(p,x)
print(json.dumps(dict(directory=str(D),binding=str(B),binding_sha256=sha(B),public_files=len(public),private_records=len(records),private_whole_blobs=len(seen),accepted=False,original_closed=False),indent=2))
