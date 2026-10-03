"""Publish only independently audited round-13 papers, preserving old bundles."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess
import zipfile

ROOT = Path('/workspace/research')
OUT = ROOT/'deliverables/round-13'
STAGE = OUT
ENTRIES = [('P06.2',ROOT/'campaigns/round-09/P06.2-finite-separable-ascent-review','P06.2-finite-separable-curve-ascent','For every complete nontrivially valued non-Archimedean K and every finite separable E/K, on every good separated strict boundaryless pure analytic curve including singular/nonreduced structures, every continuous finite h satisfies ordinary CLD zero-Hessian equivalence between h and its scalar pullback. Genuine forward Galois ascent by scalar polarization/Newton C1 tangential smoothing and fixed-support differentiated carrier total variation; actual normal-closure reverse descent handles nongalois extensions. Ordinary opens and cyclic cubic Q2 example included. No higher-dimensional finite-group result, infinite extension, positivity transport or original recognition/two-sign regularization closure.')]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

checked = []
for atom, directory, stem, scope in ENTRIES:
    campaign = json.loads((directory/'run.json').read_text())['campaign']
    result = campaign['result']
    assert campaign['status'] == 'completed' and result['verdict'] == 'PASS'
    assert all(type(p['premise']) is int and 0 <= p['premise'] < len(result['premises'])
               for p in result['passages'])
    attestation = json.loads((directory/'review-read-attestation.json').read_text())
    assert attestation['full_report_premises_and_passages_read'] is True
    assert attestation['run_sha256'] == sha(directory/'run.json')
    assert attestation['publish_exact_scope'] is True
    freeze = json.loads((directory/'freeze.json').read_text())
    binding = json.loads((directory/'source-artifact-binding.json').read_text())
    assert sha(directory/'argument.md') == freeze['argument_sha256']
    assert sha(Path(binding['source_tex'])) == freeze['source_tex_sha256'] == binding['source_tex_sha256']
    assert sha(Path(binding['declared_proof_file'])) == freeze['declared_proof_sha256'] == binding['declared_proof_sha256']
    if 'main_argument' in binding:
        assert sha(Path(binding['main_argument'])) == freeze['main_argument_sha256'] == binding['main_argument_sha256']
    assert all(p['statement'] == result['premises'][p['premise']] for p in result['passages'])
    edits = json.loads((directory/'publication-edits.json').read_text())
    checked.append((atom,directory,stem,scope,result,freeze,binding,attestation,edits))

assert OUT.is_dir() and sorted(p.name for p in OUT.iterdir()) == ['P06.2-finite-separable-curve-ascent.tex']
preparation = json.loads((ROOT/'deliverables/round-13-source-preparation.json').read_text())
assert preparation['native_compilation_pending'] is False and preparation['native_compile']['kind'] == 'success'
assert sha(Path(preparation['tex'])) == preparation['sha256']
build = STAGE/'build'
build.mkdir()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
papers = []

for atom,directory,stem,scope,result,freeze,binding,attestation,edits in checked:
    source = Path(binding['source_tex']).read_text()
    applied = []
    for edit in edits:
        count = source.count(edit['before'])
        assert count == edit['expected_occurrences'], repr(edit['before'])
        source = source.replace(edit['before'], edit['after'])
        applied.append({**edit,'occurrences':count})
    tex = STAGE/(stem+'.tex')
    tex.write_text(source)
    argument = STAGE/(stem+'-argument.md')
    shutil.copyfile(directory/'argument.md', argument)
    for number in (1,2):
        command = ['pdflatex','-interaction=nonstopmode','-halt-on-error',
                   '-output-directory='+str(build),tex.name]
        completed = subprocess.run(command,cwd=STAGE,capture_output=True)
        (build/(stem+'-pass-'+str(number)+'.txt')).write_bytes(completed.stdout+completed.stderr)
        if completed.returncode:
            raise RuntimeError(completed.stdout[-4000:].decode('utf-8',errors='replace'))
    log = (build/(stem+'.log')).read_text(errors='replace')
    assert not any(item in log for item in ('Overfull','Undefined control sequence',
                                           'Missing character','undefined references'))
    pdf = STAGE/(stem+'.pdf')
    shutil.copyfile(build/(stem+'.pdf'),pdf)
    info = subprocess.run(['pdfinfo',str(pdf)],text=True,capture_output=True,check=True).stdout
    pages = int(next(line.split(':',1)[1] for line in info.splitlines()
                     if line.startswith('Pages:')))
    receipt = STAGE/(stem+'-review.json')
    receipt.write_text(json.dumps({
        'generated_utc':now,'original_atom':atom,'full_original_atom_solved':False,
        'precise_scope':scope,'route':'Xean native Codex independent source-aware review',
        'model':'gpt-6.1-sol','reasoning':'xhigh',
        'review_database':str(directory/'review.sqlite'),
        'freeze':freeze,'source_artifact_binding':binding,
        'review_read_attestation':attestation,'result':result,
        'post_review_edits':applied,
        'published_files':{p.name:sha(p) for p in (tex,pdf,argument)},
        'compilation':'The saved standalone source was opened in the native desktop editor; its built-in compiler returned success. Two installed pdfLaTeX passes compiled this same source to the exported PDF without source/layout warnings. No installation occurred.',
        'native_editor_verification':preparation,
        'review_limit':'Same-model independent source-aware auditing is not formal '
          'verification, a universal original-atom resolution, or priority certification.'
    },ensure_ascii=False,indent=2)+'\n')
    papers.append({'atom':atom,'scope':scope,'pages':pages,
        'full_original_atom_solved':False,'review_database':str(directory/'review.sqlite'),
        'files':{p.name:sha(p) for p in (tex,pdf,argument,receipt)}})

results = {'generated_utc':now,'selected_atoms':['P06.2','P05.2'],
    'catalogue_atoms':42,'fully_solved_original_atoms':[],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'papers_and_supporting_note':papers,
    'previous_checkpoint':'../reviewed-papers-round-12.zip',
    'continued_goal':'All original atoms remain open; further research proceeds in small batches.'}
(STAGE/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance = json.loads((ROOT/'deliverables/round-12/source-provenance.json').read_text())
provenance['round_13']='Full finite-separable curve proof/native notes/audit and exact review read and bound, all12 premises/passages inspected. Primary Ducros Theorem3.2 full statement/proof and field/Gamma applicability additionally checked. Harmless logarithm-power punctuation, explicit non-Archimedean convention, primary citation and publication metadata recorded. Native saved source compiler verified; higher-dimensional/infinite extension and original recognition/two-sign regularization remain open.'
(STAGE/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
(STAGE/'INDEX.txt').write_text('Reviewed partial paper, round 13\nXean native Codex; gpt-6.1-sol; xhigh\n\nP06.2-finite-separable-curve-ascent.pdf: ordinary zero-Hessian forward ascent and actual reverse descent for EVERY finite separable extension on every good separated strict boundaryless pure analytic curve, including singular and nonreduced structures. Fixed-support differentiated carrier total variation; actual generic lengths retained. Ordinary opens and explicit cyclic cubic Q2 example included.\n\nComplete proof, standalone TeX and exact source-aware PASS12/12 review included. Primary underlying Ducros polyhedrality theorem verified at field/Gamma/compact-domain hypotheses; no source-dimension equality claim. Native desktop compiler verified saved source; PDF exported in two local passes. No all-dimensional finite-group or infinite extension theorem, positivity transport or original recognition/two-sign closure. All42 originals open. Earlier bundles unchanged.\n')
# Keep the native editor source at its final saved path.

bundle = ROOT/'deliverables/reviewed-papers-round-13.zip'
assert not bundle.exists()
files = sorted(path for path in OUT.iterdir() if path.is_file())
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as archive:
    for path in files:
        archive.write(path,path.name)
with zipfile.ZipFile(bundle) as archive:
    assert archive.testzip() is None
    for path in files:
        assert hashlib.sha256(archive.read(path.name)).hexdigest() == sha(path)
manifest = {'generated_utc':now,'bundle':str(bundle),'bytes':bundle.stat().st_size,
    'sha256':sha(bundle),'entry_count':len(files),
    'entries':{path.name:sha(path) for path in files},
    'fully_solved_original_atoms':[]}
(ROOT/'deliverables/round-13-bundle-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
