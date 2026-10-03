"""Publish only independently audited round-06 papers, preserving old bundles."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess
import zipfile

ROOT = Path('/workspace/research')
OUT = ROOT/'deliverables/round-06'
STAGE = ROOT/'deliverables/round-06-staging'
ENTRIES = [
    ('P06.2', ROOT/'campaigns/round-05/P06.2-finite-galois-ascent-continuation-review', 'P06.2-quadratic-curves',
     'Ordinary CLD zero-Hessian ascent and descent on every good separated strict boundaryless pure analytic curve, including singular and nonreduced curves, through a quadratic Galois E/K with a unit a satisfying |a|=|a-sigma(a)|=1; finite towers of such stages. Separately, the finite-separable reverse implication. Scalar polynomial approximation alone gives no higher-dimensional form ascent, arbitrary field-extension recognition or two-sign regularization.'),
    ('P05.2', ROOT/'campaigns/round-05/P05.2-real-universal-embedded-evidence-review', 'P05.2-all-real-products',
     'For every positive-growth real-PA PC reference and every bounded real-PA obstacle on the stated direct-lattice products of rank-one balanced rational ray stars times complete affine space, regularizability and exact contact hold iff at most one star is branched. With two branched factors every reference admits an actual PAPC envelope and complete negative contact defect; no ambient-extension hypothesis. Finite rational spatial domains are retained. Arbitrary balanced-pair classification and literal integral-slope claims remain open.'),
]

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

assert not OUT.exists() and not STAGE.exists()
STAGE.mkdir()
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
        'compilation':'Two installed pdfLaTeX passes. The native editor/compiler '
          'previously had no registered handler; the current editor request also '
          'did not return. Source and independently compiled PDF are preserved. '
          'No installation occurred; built-in compilation is unverified.',
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
    'previous_checkpoint':'../reviewed-papers-round-05.zip',
    'continued_goal':'All original atoms remain open; further research proceeds in small batches.'}
(STAGE/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance = json.loads((ROOT/'deliverables/round-05/source-provenance.json').read_text())
provenance['round_06']='Complete principal exact-scope reports, all premises and bound passages, source hashes and recorded harmless publication edits. P05 review embeds and reconstructs the full positive supporting proof. The P06 principal review uses compact finite-cover cutoffs; a supplemental broad unused source statement is preserved with a root caveat.'
(STAGE/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
supp = ROOT/'campaigns/round-05/P06.2-finite-galois-ascent-embedded-review'
(STAGE/'P06.2-supplemental-review-with-caveat.json').write_text(json.dumps({
    'native_result':json.loads((supp/'run.json').read_text())['campaign']['result'],
    'root_attestation':json.loads((supp/'review-read-attestation.json').read_text()),
    'publication_basis':'The principal compact-specialization review governs the quadratic theorem. The broader supplemental premise at zero-based index 10 is unused and is not certified; the native receipt is preserved verbatim.'
},ensure_ascii=False,indent=2)+'\n')
(STAGE/'INDEX.txt').write_text(
    'Reviewed partial papers, round 06\nXean native Codex; gpt-6.1-sol; xhigh\n\n'
    'P06.2-quadratic-curves.pdf: restricted quadratic Galois zero-Hessian '
    'ascent/descent on arbitrary pure analytic curves; finite towers and '
    'separate finite-separable reverse implication.\n'
    'P05.2-all-real-products.pdf: exact all-real-reference product criterion, '
    'including actual regularizable envelopes with complete negative defects '
    'when at least two star factors branch.\n\n'
    'Each paper has standalone TeX, unchanged frozen review argument and full '
    'independent exact-scope review receipt. P05 includes its complete supporting '
    'positive proof. P06 has a separate preserved supplemental receipt with an '
    'unused overbroad cutoff premise caveat; its principal review certifies the '
    'compact specialization actually used. PASS is not formal verification or '
    'priority certification. All original atoms remain open. Earlier immutable '
    'papers remain in reviewed-papers-round-05.zip and preceding bundles.\n')
STAGE.rename(OUT)

bundle = ROOT/'deliverables/reviewed-papers-round-06.zip'
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
(ROOT/'deliverables/round-06-bundle-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
