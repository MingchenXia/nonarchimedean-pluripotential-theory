"""Publish exact-scoped reviewed mathematics; keep native UI verification separate."""
from pathlib import Path
import datetime, hashlib, json, shutil, zipfile, sys

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def write_new(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

additional_path = R / 'shared-sources/prescribed-type-additional-primary-read-20261004.json'
additional = load(additional_path)
assert sha(additional_path) == '4b9fbaf4614ec85e3115091cd7d301d3b5f76063ea75cd94e3f4fe93a973e707'
number = int(sys.argv[1]); assert number in (31,32)
for n, atom, stem in [(number, 'P15.1' if number==31 else 'P15.2',
                      'P15.1-minimum-reference-finite-energy' if number==31 else 'P15.2-minimum-reference-full-mass-operator')]:
    out = R / f'deliverables/round-{n}'
    d = R / f'campaigns/round-{n}' / (stem+'-review')
    phase1 = R / 'root-checks' / ('minimum-reference-zero-volume-'+atom+'-phase1')
    phase2 = R / 'root-checks' / ('minimum-reference-zero-volume-'+atom+'-phase2')
    run = load(d/'run.json'); result = run['campaign']['result']
    freeze = load(d/'freeze.json'); binding = load(d/'source-artifact-binding.json')
    att = load(d/'review-read-attestation.json')
    author = load(phase1/'complete-read-before-review.json')
    review_read = load(phase2/'complete-review-read-record.json')
    repro = load(phase1/'reproduction-result.json')
    assert run['campaign']['status'] == 'completed' and result['verdict'] == 'PASS'
    nprem,npass=len(result['premises']),len(result['passages'])
    assert nprem>0 and npass>0
    assert result == load(d/'review-result.json') == load(phase2/'canonical-review-result.json')
    for passage in result['passages']:
        assert type(passage['premise']) is int and 0 <= passage['premise'] < nprem
        assert passage['statement'] == result['premises'][passage['premise']]
    assert att['publish_exact_scope'] and not att['full_original_atom_solved']
    assert att['run_sha256'] == sha(d/'run.json')
    assert att['canonical_review_result_sha256'] == sha(phase2/'canonical-review-result.json')
    assert att['source_artifact_binding_sha256'] == sha(d/'source-artifact-binding.json')
    for key in ['root_complete_review_read_record','root_complete_author_read_record']:
        assert sha(att[key]) == att[key+'_sha256']
    assert author['all_new_mathematical_core_files_fully_directly_read']
    assert author['all_author_TEX_LF_entries_directly_read'] > 0
    assert author['all_actual_canonical_note_texts_summaries_support_fully_directly_read']
    assert author['canonical_result_record_sha256'] == sha(phase1/'canonical-result-record.json')
    for key in ['entire_report_directly_read','all_premises_directly_read',
                'all_passages_directly_read','all_zero_based_indices_and_exact_statements_verified']:
        assert review_read[key]
    assert review_read['review_freeze_sha256'] == sha(d/'freeze.json') == binding['original_freeze_sha256']
    assert sha(d/'argument.md') == freeze['argument_sha256'] == binding['review_argument_sha256']
    for key, digest in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),
                        ('declared_proof_file','declared_proof_sha256')]:
        assert sha(binding[key]) == binding[digest] == freeze[digest]
    worker = Path(freeze['source_workspace'])
    assert sha(worker/'status.json') == freeze['source_status_sha256'] == binding['source_status_sha256']
    assert repro['success'] and repro['frozen_author_proof_and_TEX_unchanged']
    if n==31:
        assert repro['fresh_generated_proof_and_TEX_byte_identical']
        assert repro['copied_proof_sha256'] == binding['main_argument_sha256']
    else:
        assert repro['fresh_generated_mathematical_core_TEX_and_literal_annex_byte_identical']
        assert not repro['fresh_generated_full_argument_byte_identical']
        assert repro['author_full_argument_sha256'] == binding['main_argument_sha256']
        assert repro['copied_proof_sha256'] == author['all_new_mathematical_core_files_fully_directly_read'][0]['sha256']
    assert repro['copied_TEX_sha256'] == binding['source_tex_sha256']
    edits = load(d/'publication-edits.json'); source = Path(binding['source_tex']).read_text()
    for edit in edits:
        assert source.count(edit['before']) == edit['expected_occurrences']
        source = source.replace(edit['before'],edit['after'])
    tex = out/(stem+'.tex'); pdf = out/(stem+'.pdf')
    preparation = load(R/f'deliverables/round-{n}-source-preparation.json')
    assert source == tex.read_text() and sha(tex) == preparation['sha256']
    assert sha(d/'publication-edits.json') == preparation['publication_edits_sha256']
    export = load(out/'export-evidence.json')
    assert sha(tex) == export['source_sha256'] and sha(pdf) == export['pdf_sha256']
    assert not export['source_changed'] and len(export['runs']) == 2
    assert all(x['exit_code'] == 0 for x in export['runs'])
    assert not any(export['final_notices'].values())
    native_path = R/f'deliverables/round-{n}-native-verification.json'
    if native_path.exists():
        native = load(native_path)
        assert native['source_sha256'] == sha(tex)
        assert native['native_compilation_confirmed'] and native['tool_result']['kind'] == 'success'
    else:
        request = load(R/f'deliverables/round-{n}-native-request-status.json')
        assert request['source_sha256'] == sha(tex)
        native = {'recorded_utc':now,'source_sha256':sha(tex),
                  'native_compilation_confirmed':False,'native_editor_opening_confirmed':False,
                  'tool_result':{'kind':'pending'},'request_status':request,
                  'live_compiler_cell': request['compile_cell'],
                  'limitation':'Native opening and compilation were requested but no response was received by packet creation. The files remain saved and editable; opening is unconfirmed. The PDF passed two local TeX builds. A future native result will be a separate addendum.'}
    visual = {'recorded_utc':now,'inspection_utc':'2026-10-04 09:12 UTC' if n==32 else now,
              'pdf_sha256':sha(pdf),'pages':export['pages'],'image':str(out/'first-page.png'),
              'image_sha256':sha(out/'first-page.png'),'first_page_visually_inspected':True,
              'observation':'Title, text, displayed formulae and page footer are legible with no clipping.',
              'all_pages_visually_inspected':False}
    write_new(R/f'deliverables/round-{n}-visual-check.json',visual)
    argument = out/(stem+'-argument.md'); assert not argument.exists()
    shutil.copyfile(d/'argument.md',argument)
    scope = freeze['source_status']['exact_result']
    limitations = freeze['source_status']['concrete_gaps']
    receipt = out/(stem+'-review.json')
    write_new(receipt,{'generated_utc':now,'original_atom':atom,'full_original_atom_solved':False,
                      'precise_scope':scope,'limitations':limitations,'route':'Xean native Codex independent review',
                      'model':'gpt-6.1-sol','reasoning':'xhigh','review_run_sha256':sha(d/'run.json'),
                      'freeze':freeze,'source_artifact_binding':binding,'review_read_attestation':att,
                      'result':result,'post_review_edits':edits,'additional_source_record_sha256':sha(additional_path),
                      'published_files':{p.name:sha(p) for p in [tex,pdf,argument]},
                      'native_editor_verification':native,'export_verification':export,'visual_verification':visual,
                      'review_limit':'Same-model independent review is not formal verification, original-problem closure or priority certification.'})
    write_new(out/'results.json',{'generated_utc':now,'selected_atoms':['P15.1','P15.2'],
              'catalogue_atoms':42,'fully_solved_original_atoms':[],'route':'Xean native Codex',
              'model':'gpt-6.1-sol','reasoning':'xhigh','papers_and_supporting_note':[
                  {'atom':atom,'scope':scope,'limitations':limitations,'full_original_atom_solved':False,
                   'pages':export['pages'],'files':{p.name:sha(p) for p in [tex,pdf,argument,receipt]}}]})
    source_audit = worker/'source-audit.json'
    write_new(out/'source-provenance.json',{'generated_utc':now,'source_workspace':str(worker),
              'source_metadata':load(source_audit),'source_metadata_sha256':sha(source_audit),
              'complete_primary_body_bindings':author['all_24_source_appendix_bodies_bound_to_complete_primary_reads'],
              'standard_foundations':author['standard_foundations'],
              'complete_primary_read_records':author['primary_read_records'],
              'additional_complete_primary_source_units':additional,
              'additional_source_record_sha256':sha(additional_path),
              'primary_bodies_and_new_applications_fully_root_read':True,
              'frozen_source_binding':binding,'publication_edits_sha256':sha(d/'publication-edits.json'),
              'post_review_changes':'Completed review provenance, accurate reproducibility and typesetting. Frozen author/review inputs remain unchanged; all publication edits replay exactly.',
              'historical_DGMS_read_record_note':'Earlier IAS403 and standard-foundation-only authentication remain recorded. The separate fresh StonyBrook source unit now authenticates the complete printed proof.',
              'whole_archival_PDFs_and_texts_local_only':True})
    copies = {phase1/'canonical-result-record.json':'canonical-native-result.json',
              phase1/'complete-read-before-review.json':'root-complete-author-read.json',
              phase2/'complete-review-read-record.json':'root-complete-review-read.json',
              phase1/'reproduction-result.json':'root-reproduction-result.json',
              d/'review-read-attestation.json':'review-read-attestation.json',
              R/f'deliverables/round-{n}-visual-check.json':'visual-check.json'}
    for src,name in copies.items():
        assert not (out/name).exists();shutil.copyfile(src,out/name)
    write_new(out/'native-editor-verification.json',native)
    (out/'INDEX.txt').write_text('Reviewed minimum-reference zero-volume theorem\n\n'+scope+
        '\n\nRemaining original scope:\n'+'\n'.join(limitations)+
        '\n\nThe packet contains full frozen proof, essential primary bodies, complete independent review, canonical native notes, root read/reproduction records, additional source authentication and PDF export evidence. Native editor verification is pending where stated. Same-model review is not formal verification. Original problem completion is pending a separate audit; no original closure is claimed by this packet.\n')
    names = [tex.name,pdf.name,argument.name,receipt.name,'results.json','source-provenance.json',
             *copies.values(),'native-editor-verification.json','export-evidence.json','INDEX.txt']
    entries = {name:sha(out/name) for name in names}
    bundle = R/f'deliverables/reviewed-papers-round-{n}.zip';assert not bundle.exists()
    with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(out/name,name)
    with zipfile.ZipFile(bundle) as archive:
        assert set(archive.namelist()) == set(entries)
        for name,digest in entries.items():assert hashlib.sha256(archive.read(name)).hexdigest()==digest
    write_new(R/f'deliverables/round-{n}-bundle-manifest.json',{'created_utc':now,
              'bundle':str(bundle),'sha256':sha(bundle),'bytes':bundle.stat().st_size,
              'entries':entries,'full_original_atom_solved':False})
    print(json.dumps({'round':n,'atom':atom,'pages':export['pages'],'bundle':str(bundle),
                     'sha256':sha(bundle),'entries':len(entries),'native_compilation_confirmed':native['native_compilation_confirmed'],
                     'fully_solved_original_atoms':[]}))
