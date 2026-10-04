"""Package the exact reviewed finite graph-product theorem and verified source."""
from pathlib import Path
import datetime,hashlib,json,shutil,zipfile
r=Path('/workspace/research');d=r/'campaigns/round-24/P05.2-finitely-many-graph-products-review';out=r/'deliverables/round-24';stem='P05.2-finitely-many-graph-products'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
j=json.loads((d/'run.json').read_text());result=j['campaign']['result'];f=json.loads((d/'freeze.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text());att=json.loads((d/'review-read-attestation.json').read_text());edits=json.loads((d/'publication-edits.json').read_text())
assert j['campaign']['status']=='completed' and result['verdict']=='PASS' and result['premises']==[] and result['passages']==[]
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read','root_full_main_and_all_canonical_notes_read','publish_exact_scope'))
assert att['run_sha256']==sha(d/'run.json') and att['freeze_sha256']==sha(d/'freeze.json') and att['source_artifact_binding_sha256']==sha(d/'source-artifact-binding.json')
assert sha(d/'argument.md')==f['argument_sha256']==att['argument_sha256']
for k,h in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:assert sha(Path(b[k]))==b[h]==f[h]
w=Path(f['source_workspace']);assert sha(w/'status.json')==f['source_status_sha256']
s=Path(b['source_tex']).read_text()
for e in edits:
    assert s.count(e['before'])==e['expected_occurrences'];s=s.replace(e['before'],e['after'])
tex=out/(stem+'.tex');pdf=out/(stem+'.pdf');assert tex.read_text()==s
prep=json.loads((r/'deliverables/round-24-source-preparation.json').read_text())
assert sha(tex)==prep['sha256'] and sha(d/'publication-edits.json')==prep['publication_edits_sha256']
native=json.loads((r/'deliverables/round-24-native-verification.json').read_text());ex=json.loads((out/'export-evidence.json').read_text())
assert native['native_compilation_success'] and native['native_compile']['kind']=='success' and native['source_sha256']==sha(tex)
assert ex['source_sha256']==sha(tex) and ex['pdf_sha256']==sha(pdf) and not ex['source_changed'] and not any(ex['final_notices'].values())
assert len(ex['runs'])==2 and all(x['exit_code']==0 for x in ex['runs'])
visual={'checked_utc':now,'pdf_sha256':sha(pdf),'pages':ex['pages'],'image':str(out/'first-page.png'),'image_sha256':sha(out/'first-page.png'),'first_page_visually_inspected':True,'observation':'Title, scope, definition, theorem and displayed formulas legible with no clipping on first page. Remaining pages checked by compilation diagnostics only.'}
(r/'deliverables/round-24-visual-check.json').write_text(json.dumps(visual,indent=2)+'\n')
scope='For every finite d>=2 and every product of d nonempty finite embedded balanced rational pure graphs with actual positive REAL weights and saturated lattices, for EACH prescribed continuous rational-domain real-PA actual-PC reference positive at infinity, EVERY bounded continuous rational-domain real-PA obstacle has an actual rational-domain PAPC raw envelope in gamma+O(1), uniform decreasing PAPC regularization and complete d-stage contact iff all factor local relation cones have rank one and at most ONE factor branches. Every failed criterion has a compact obstacle with exact regularizable PAPC raw envelope unchanged at infinity and a completely evaluated negative integral. Higher-relation failure gives -d!(delta epsilon M) product_{j>=2}(2delta b_jw_j); two rank-one branching factors give -(d!/2!)8kappa^2ab product_{j>=3}(2kappa b_jw_j). The original arbitrary balanced-carrier classification remains open.'
arg=out/(stem+'-argument.md');shutil.copyfile(d/'argument.md',arg)
receipt=out/(stem+'-review.json')
receipt.write_text(json.dumps({'generated_utc':now,'original_atom':'P05.2','full_original_atom_solved':False,'precise_scope':scope,'route':'Xean native Codex independent review','model':'gpt-6.1-sol','reasoning':'xhigh','review_database':str(d/'review.sqlite'),'review_run_sha256':sha(d/'run.json'),'freeze':f,'source_artifact_binding':b,'review_read_attestation':att,'result':result,'post_review_edits':edits,'published_files':{p.name:sha(p) for p in (tex,pdf,arg)},'native_editor_verification':native,'export_verification':ex,'visual_verification':visual,'review_limit':'Same-model independent review is not formal verification, original-atom closure or priority certification.'},ensure_ascii=False,indent=2)+'\n')
results={'generated_utc':now,'selected_atoms':['P06.2','P05.2'],'catalogue_atoms':42,'fully_solved_original_atoms':[],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','papers_and_supporting_note':[{'atom':'P05.2','scope':scope,'pages':ex['pages'],'full_original_atom_solved':False,'review_database':str(d/'review.sqlite'),'files':{p.name:sha(p) for p in (tex,pdf,arg,receipt)},'native_compilation_verification':'SUCCESS on exact unchanged source','local_pdf_export':'two successful unchanged-source passes with zero final warnings'}],'previous_checkpoint':'../reviewed-papers-round-23.zip','continued_goal':'All42 originals open; specified-tree smoothing independently reviewed separately, all-K curve recognition integration running.'}
(out/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance={'generated_utc':now,'original_upload_file_id':'file_000000009b3c820a8780270d7426f8b0','original_pdf_sha256':'991de3becf3cca896ec089241a9489deca3c9cbc26b57df1bc3062008a1dd3ee','scope':scope,'source_workspace':str(w),'frozen_source_bindings':b,'root_read_record':json.loads((d/'root-draft-read-record.json').read_text()),'review_read_attestation':att,'source_snapshots':json.loads((w/'source-hashes.json').read_text()),'source_selections':json.loads((w/'source-excerpts.json').read_text()),'imports':'No essential external theorem premises. All supporting mathematical proofs reconstructed. Integral source conventions and real extension distinguished. Primary/comparison appendices remain in complete frozen argument. Canonical native notes are explicitly distinct from author-local notes.','native_editor_verification':native,'export_verification':ex}
(out/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
files=[tex,pdf,arg,receipt,out/'results.json',out/'source-provenance.json',out/'export-evidence.json']
for name in ('diagnostics.py','diagnostic-input.json','diagnostic-output.json'):
    p=out/name;shutil.copyfile(w/name,p);files.append(p)
for origin,name in [(r/'root-checks/many-graph-product-draft-phase2/root-rerun-and-read-in-progress.json','root-finite-rerun.json'),(d/'root-draft-read-record.json','root-complete-read-record.json'),(r/'deliverables/round-24-native-verification.json','native-verification.json')]:
    p=out/name;shutil.copyfile(origin,p);files.append(p)
p=out/'INDEX.txt';p.write_text('Reviewed partial theorem, round24\nXean native Codex gpt-6.1-sol xhigh\n\n'+scope+'\n\nExact independent PASS, complete frozen argument, standalone source/PDF and finite recursive diagnostics included. Native desktop compilation SUCCESS on unchanged source, two clean local PDF exports. Only first page visually inspected. Same-model review and arithmetic are not formal verification or priority certification. All42originals remain open; goalactive.\n');files.append(p)
bundle=r/'deliverables/reviewed-papers-round-24.zip';assert not bundle.exists()
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files):z.write(p,p.name)
with zipfile.ZipFile(bundle) as z:
    assert z.testzip() is None and all(hashlib.sha256(z.read(p.name)).hexdigest()==sha(p) for p in files)
m={'generated_utc':now,'bundle':str(bundle),'bytes':bundle.stat().st_size,'sha256':sha(bundle),'entry_count':len(files),'entries':{p.name:sha(p) for p in sorted(files)},'fully_solved_original_atoms':[],'native_verification':'SUCCESS on unchanged source; two clean local exports'}
(r/'deliverables/round-24-bundle-manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps(m,indent=2))
