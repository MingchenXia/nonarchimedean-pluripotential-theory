"""Publish only the exact reviewed arbitrary-field intrinsic curve theorem."""
from pathlib import Path
import datetime, hashlib, json, shutil, zipfile
r=Path('/workspace/research');out=r/'deliverables/round-26'
d=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
stem='P06.2-arbitrary-field-curve-recognition'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
j=json.loads((d/'run.json').read_text());review=j['campaign']['result']
f=json.loads((d/'freeze.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text())
att=json.loads((d/'review-read-attestation.json').read_text());edits=json.loads((d/'publication-edits.json').read_text())
assert j['campaign']['status']=='completed' and review['verdict']=='PASS'
assert len(review['premises'])==43 and len(review['passages'])==75
for p in review['passages']:assert p['statement']==review['premises'][p['premise']]
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read','root_full_main_and_all_canonical_notes_read','publish_exact_scope'))
assert att['run_sha256']==sha(d/'run.json') and att['freeze_sha256']==sha(d/'freeze.json') and att['source_artifact_binding_sha256']==sha(d/'source-artifact-binding.json')
assert sha(d/'argument.md')==f['argument_sha256']==att['argument_sha256']
for k,h in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:assert sha(Path(b[k]))==b[h]==f[h]
w=Path(f['source_workspace']);assert sha(w/'status.json')==f['source_status_sha256']
s=Path(b['source_tex']).read_text()
for e in edits:
    assert s.count(e['before'])==e['expected_occurrences'];s=s.replace(e['before'],e['after'])
tex=out/(stem+'.tex');pdf=out/(stem+'.pdf');assert tex.read_text()==s
prep=json.loads((r/'deliverables/round-26-source-preparation.json').read_text())
assert sha(tex)==prep['sha256'] and sha(d/'publication-edits.json')==prep['publication_edits_sha256']
native=json.loads((r/'deliverables/round-26-native-verification.json').read_text())
ex=json.loads((out/'export-evidence.json').read_text())
assert native['native_compilation_success'] and native['native_compile']['kind']=='success' and native['source_sha256']==sha(tex)
assert ex['source_sha256']==sha(tex) and ex['pdf_sha256']==sha(pdf) and not ex['source_changed'] and not any(ex['final_notices'].values())
assert len(ex['runs'])==2 and all(x['exit_code']==0 for x in ex['runs'])
visual={'checked_utc':now,'pdf_sha256':sha(pdf),'pages':ex['pages'],'image':str(out/'first-page.png'),
 'image_sha256':sha(out/'first-page.png'),'first_page_visually_inspected':True,
 'observation':'Final first page legible, opening theorem and displayed current identity visible without clipping. Theorem continues on next page. Remaining pages checked by compilation diagnostics only.'}
(r/'deliverables/round-26-visual-check.json').write_text(json.dumps(visual,indent=2)+'\n')
scope='For ANY complete nontrivially valued non-Archimedean K, every actual good separated strict boundaryless PURE analytic curve X, and every finite continuous real h with ordinary CLD D[h]=0 against ALL ordinary compact scalar tests and actual generic Artinian lengths: h is GR-harmonic, classically pluriharmonic, G-local real PL and GJR-harmonic. For EVERY analytic L/K, EVERY separated pure analytic L-curve Y, and EVERY analytic map f:Y to X_L, the finite continuous composite is GR-harmonic; if Y is smooth strict it is Thuillier-harmonic. Singular/nonreduced structures, unequal generic lengths, imperfect fields and every characteristic included; every ordinary open included. This recognizes FUNCTIONS by completed-algebraic current transport, intrinsic recognition upstairs, and published harmonic-function descent. No arbitrary transcendental-current ascent or ordinary-smooth decreasing psh approximation is established. Original arbitrary-dimensional P06.2 remains open.'
arg=out/(stem+'-argument.md');shutil.copyfile(d/'argument.md',arg)
receipt=out/(stem+'-review.json');assert not receipt.exists()
receipt.write_text(json.dumps({'generated_utc':now,'original_atom':'P06.2','full_original_atom_solved':False,
 'precise_scope':scope,'route':'Xean native Codex independent review','model':'gpt-6.1-sol','reasoning':'xhigh',
 'review_database':str(d/'review.sqlite'),'review_run_sha256':sha(d/'run.json'),'freeze':f,'source_artifact_binding':b,
 'review_read_attestation':att,'result':review,'post_review_edits':edits,
 'published_files':{p.name:sha(p) for p in (tex,pdf,arg)},'native_editor_verification':native,
 'export_verification':ex,'visual_verification':visual,
 'review_limit':'Same-model independent review is not formal verification, original-atom closure or priority certification.'},ensure_ascii=False,indent=2)+'\n')
results={'generated_utc':now,'selected_atoms':['P06.2','P05.2'],'catalogue_atoms':42,'fully_solved_original_atoms':[],
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'papers_and_supporting_note':[{'atom':'P06.2','scope':scope,'full_original_atom_solved':False,'pages':ex['pages'],
 'files':{p.name:sha(p) for p in (tex,pdf,arg,receipt)}}]}
(out/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance={'generated_utc':now,'source_workspace':str(w),
 'source_manifest':json.loads((w/'sources/manifest.json').read_text()),
 'primary_units':json.loads((w/'sources/primary-units.json').read_text()),
 'full_supports_and_primary_bodies_retained_in_complete_argument':True,
 'all_16_new_primary_bodies_fully_directly_root_read':True,
 'all_23_source_support_copies_rebound_to_unchanged_origins':True,
 'known_gate_support_full_previous_root_read_reused_unchanged':True,
 'n701_main_and_published_wrapper_separately_bound':True,
 'post_review_changes':'Metadata, exact version references, closed-subspace terminology clarification and native math grouping only. No new mathematical step.',
 'frozen_source_binding':b,'publication_edits_sha256':sha(d/'publication-edits.json')}
(out/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
copies={d/'root-draft-read-record.json':'root-complete-read-record.json',
 d/'review-read-attestation.json':'review-read-attestation.json',
 r/'root-checks/arbitrary-field-curve-integration-phase1/canonical-result-record.json':'canonical-native-result.json',
 r/'deliverables/round-26-native-verification.json':'native-editor-verification.json'}
for src,name in copies.items():shutil.copyfile(src,out/name)
(out/'INDEX.md').write_text('# Arbitrary-field intrinsic curve recognition\n\nTen-page independently reviewed recognition theorem on every actual good separated strict boundaryless pure curve over any complete nontrivial field. Includes singularities, nilpotents, imperfect and positive-characteristic fields, all field extensions and curve maps, and ordinary opens. Original arbitrary-dimensional P06.2 remains open.\n\nThe packet contains the paper, complete frozen proof with all essential supporting bodies and primary quotations, full independent review, source provenance, canonical native notes, complete read records, and exact native compilation/local export evidence. Same-model review is not formal verification or priority certification.\n')
names=[tex.name,pdf.name,arg.name,receipt.name,'results.json','source-provenance.json',*copies.values(),'export-evidence.json','INDEX.md']
entries={n:sha(out/n) for n in names}
bundle=r/'deliverables/reviewed-papers-round-26.zip';assert not bundle.exists()
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for n in names:z.write(out/n,n)
with zipfile.ZipFile(bundle) as z:
    assert set(z.namelist())==set(entries)
    for n,h in entries.items():assert hashlib.sha256(z.read(n)).hexdigest()==h
manifest={'created_utc':now,'bundle':str(bundle),'sha256':sha(bundle),'bytes':bundle.stat().st_size,'entries':entries,
 'full_original_atom_solved':False}
(r/'deliverables/round-26-bundle-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'bundle':str(bundle),'sha256':sha(bundle),'pages':ex['pages'],'entries':len(entries),'full_original_atoms_solved':0},indent=2))
