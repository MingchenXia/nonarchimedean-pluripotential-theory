"""Package already native-compiled standalone papers without changing sources."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys, zipfile

root = Path('/workspace/research')
number = int(sys.argv[1])
assert number in (20,21)
out = root/f'deliverables/round-{number}'
configs = {
20: ('P05.2','campaigns/round-20/P05.2-fixed-real-reference-review',
     'P05.2-fixed-real-reference-graph-products',
     'For each prescribed real-coefficient continuous actual-PC positive-at-infinity reference on a product of two nonempty finite embedded balanced rational pure graphs with positive real weights and rank-one positive relation cones, every bounded continuous real-PA rational-domain obstacle has an actual rational-domain PAPC uniformly decreasing regularizable raw envelope with complete contact iff at least one factor is unbranched. If both factors branch, every prescribed real reference admits a nonnegative compact bounded obstacle, unchanged reference at infinity, an exact actual PAPC raw envelope and full contact integral -8*epsilon^2*a*b<0. Actual saturated lattices, all valences, cycles, ends, full lines and disconnected components retained. The arbitrary-balanced-pair classification, literal integral-slope coefficient convention and analytic realization are not settled.'),
21: ('P06.2','campaigns/round-19/P06.2-general-finite-galois-review',
     'P06.2-finite-galois-all-dimensional-ascent',
     'For every finite Galois E/K over a complete nontrivially valued K and every actual good separated strict boundaryless pure n-dimensional K-analytic X, n>=1, finite continuous real h has ordinary zero Hessian iff its scalar pullback does, against every compact complementary (n-1,n-1) form. Wild ramification, all components and actual nilpotent generic lengths are retained. Reverse transport uses canonical scalar projection without a degree factor. Completed-algebraic, mixed-finite, transcendental transport, classical recognition and two-sign ordinary smooth regularization are not claimed.')}
atom,relative,stem,scope = configs[number]
directory = root/relative
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
run = json.loads((directory/'run.json').read_text())
result = run['campaign']['result']
att = json.loads((directory/'review-read-attestation.json').read_text())
freeze = json.loads((directory/'freeze.json').read_text())
binding = json.loads((directory/'source-artifact-binding.json').read_text())
assert run['campaign']['status']=='completed' and result['verdict']=='PASS'
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read','publish_exact_scope','root_full_main_and_all_canonical_notes_read'))
assert att['run_sha256']==sha(directory/'run.json')
assert att['freeze_sha256']==sha(directory/'freeze.json')
assert att['source_artifact_binding_sha256']==sha(directory/'source-artifact-binding.json')
assert sha(directory/'argument.md')==freeze['argument_sha256']==att['argument_sha256']
for key,hash_key in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(binding[key]))==freeze[hash_key]==binding[hash_key]
assert sha(Path(freeze['source_workspace'])/'status.json')==freeze['source_status_sha256']
assert all(type(p['premise']) is int and 0<=p['premise']<len(result['premises']) and p['statement']==result['premises'][p['premise']] for p in result['passages'])
edits = json.loads((directory/'publication-edits.json').read_text())
reconstructed = Path(binding['source_tex']).read_text()
for edit in edits:
    assert reconstructed.count(edit['before'])==edit['expected_occurrences']
    reconstructed = reconstructed.replace(edit['before'],edit['after'])
tex = out/(stem+'.tex')
assert tex.read_text()==reconstructed
prep = json.loads((root/f'deliverables/round-{number}-source-preparation.json').read_text())
assert not prep['native_compilation_pending'] and prep['native_compile']['kind']=='success'
assert prep['sha256']==sha(tex) and prep['publication_edits_sha256']==sha(directory/'publication-edits.json')
pdf = out/(stem+'.pdf')
log = pdf.with_suffix('.log').read_text(errors='replace')
notices = {x:log.count(x) for x in ('Overfull','Underfull','Missing character','Undefined control sequence','undefined references')}
assert not any(notices.values())
for i in (1,2):
    output = (out/f'export-pass-{i}.stdout.txt').read_text(errors='replace')
    assert 'Output written on' in output and 'Fatal error' not in output
info = subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
pages = int(next(l.split(':',1)[1] for l in info.splitlines() if l.startswith('Pages:')))
visual = json.loads((root/f'deliverables/round-{number}-visual-check.json').read_text())
assert visual['pdf_sha256']==sha(pdf) and visual['pages']==pages
argument = out/(stem+'-argument.md')
shutil.copyfile(directory/'argument.md',argument)
receipt = out/(stem+'-review.json')
receipt.write_text(json.dumps({'generated_utc':now,'original_atom':atom,'full_original_atom_solved':False,
    'precise_scope':scope,'route':'Xean native Codex independent source-aware review','model':'gpt-6.1-sol','reasoning':'xhigh',
    'review_database':str(directory/'review.sqlite'),'freeze':freeze,'source_artifact_binding':binding,
    'review_read_attestation':att,'result':result,'post_review_edits':edits,
    'published_files':{p.name:sha(p) for p in (tex,pdf,argument)},
    'native_editor_verification':prep,'export_verification':visual,
    'compilation':'Native compiler returned SUCCESS; two pdfLaTeX passes exported the exact same unchanged saved source. No installation occurred.',
    'review_limit':'Same-model independent review is not formal verification, a resolution of the original atom, or priority certification.'},ensure_ascii=False,indent=2)+'\n')
results = {'generated_utc':now,'selected_atoms':['P06.2','P05.2'],'catalogue_atoms':42,'fully_solved_original_atoms':[],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'papers_and_supporting_note':[{'atom':atom,'scope':scope,'pages':pages,'full_original_atom_solved':False,
       'review_database':str(directory/'review.sqlite'),'files':{p.name:sha(p) for p in (tex,pdf,argument,receipt)}}],
    'previous_checkpoint':f'../reviewed-papers-round-{number-1}.zip',
    'continued_goal':'All 42 original atoms remain open; research continues in small batches.'}
(out/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance = {'generated_utc':now,'original_upload_file_id':'file_000000009b3c820a8780270d7426f8b0',
    'original_pdf_sha256':'991de3becf3cca896ec089241a9489deca3c9cbc26b57df1bc3062008a1dd3ee',
    'source_workspace':freeze['source_workspace'],'frozen_source_bindings':binding,
    'root_read_record':json.loads((directory/'root-draft-read-record.json').read_text()),
    'review_read_attestation':att,'scope':scope,
    'imports':'No essential external theorem premises; exact definitions and all supporting proofs are included.' if number==20 else
    'Primary CLD and Ducros analytic foundations are imported under the explicit restricted hypotheses; the new algebraic, Banach, support and collar proofs are reconstructed. All 33 supplied primary units are retained in the complete frozen argument. Interior base change is inclusion only. Source-display errata are separately disclosed; frozen raw quotations are unchanged.'}
(out/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
files = [tex,pdf,argument,receipt,out/'results.json',out/'source-provenance.json']
workspace = Path(freeze['source_workspace'])
if number==20:
    for name in ('real-sum-diagnostic.py','real-sum-output.json'):
        target=out/name
        shutil.copyfile(workspace/name,target)
        files.append(target)
    for name in ('root-check.json',):
        target=out/'root-real-reference-check.json'
        shutil.copyfile(root/'root-checks/fixed-real-reference-graph-products'/name,target)
        files.append(target)
    for name in ('local-recursion.py','local-input.json','local-output.json'):
        target=out/name
        shutil.copyfile(workspace/name,target)
        files.append(target)
    target=out/'root-saturated-index-check.json'
    shutil.copyfile(root/'root-checks/fixed-reference-graph-products/root-check.json',target)
    files.append(target)
else:
    for source in sorted((workspace/'diagnostics').iterdir()):
        if source.is_file() and source.suffix in ('.py','.json'):
            target=out/source.name
            shutil.copyfile(source,target)
            files.append(target)
index=out/'INDEX.txt'
index.write_text(f'Reviewed partial theorem, round {number}\nXean native Codex gpt-6.1-sol xhigh\n\n{stem}.pdf: {scope}\n\nComplete frozen argument, standalone TeX, PDF, exact independent review, provenance and finite diagnostic packet included. Computations are diagnostics, not proofs of the universal result. Same-model review is not formal verification or priority certification. All 42 original atoms remain open.\n')
files.append(index)
bundle=root/f'deliverables/reviewed-papers-round-{number}.zip'
assert not bundle.exists()
assert len({p.name for p in files})==len(files)
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(files):
        archive.write(path,path.name)
with zipfile.ZipFile(bundle) as archive:
    assert archive.testzip() is None
    assert all(hashlib.sha256(archive.read(p.name)).hexdigest()==sha(p) for p in files)
manifest={'generated_utc':now,'bundle':str(bundle),'bytes':bundle.stat().st_size,'sha256':sha(bundle),
          'entry_count':len(files),'entries':{p.name:sha(p) for p in sorted(files)},'fully_solved_original_atoms':[]}
(root/f'deliverables/round-{number}-bundle-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
