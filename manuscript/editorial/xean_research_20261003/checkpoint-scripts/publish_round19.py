"""Publish only independently audited round-19 papers, preserving old bundles."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess
import zipfile

ROOT = Path('/workspace/research')
OUT = ROOT/'deliverables/round-19'
STAGE = OUT
ENTRIES = [('P05.2', ROOT/'campaigns/round-18/P05.2-fixed-rational-reference-review', 'P05.2-fixed-rational-reference-graph-products', 'For each fixed rational-coefficient continuous actual-PC positive-at-infinity reference on the product of two nonempty finite embedded balanced rational pure graphs with positive real actual weights and rank-one positive relation cones, every bounded continuous real-PA obstacle has a rational-domain PAPC uniformly decreasing regularizable raw envelope with complete contact if and only if at least one factor is unbranched. Every prescribed rational reference on two branched factors admits a nonnegative bounded compact obstacle, unchanged asymptotic reference, exact raw envelope and full integral -8epsilon^2ab<0. Actual saturated lattices, all cycles, ends, full lines and disconnected components retained. Arbitrary-balanced-pair classification and negative extension to all real references remain open.')]


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

assert OUT.is_dir() and sorted(p.name for p in OUT.iterdir()) == ['P05.2-fixed-rational-reference-graph-products.tex']
preparation = json.loads((ROOT/'deliverables/round-19-source-preparation.json').read_text())
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
        'compilation':'The saved standalone source was opened in the native desktop editor; its built-in compiler returned success. Two installed pdfLaTeX passes compiled this same source to the exported PDF without overfull boxes, missing characters or undefined references. No installation occurred.',
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
    'previous_checkpoint':'../reviewed-papers-round-18.zip',
    'continued_goal':'All original atoms remain open; further research proceeds in small batches.'}
(STAGE/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
provenance = json.loads((ROOT/'deliverables/round-18/source-provenance.json').read_text())
provenance['round_19']='Complete879line argument/all2canonical notes/audit/research/build/source program read; exact independent PASS0/0 fully read and bound. Fixed rational-reference graph-product characterization iff one factor unbranched accepted. Every prescribed rational reference on two branched graphs has full negative integral -8epsilon^2ab, with unchanged asymptotic reference and nonnegative compact obstacle. One harmless equation-reference correction, publication metadata/native grouping and full source-definition appendix retained in frozen argument. All49 local cone indices checked independently by ambient minor gcd; sample scaling8/49. Native compiler SUCCESS firstcall; same source exported. Original42 remainopen.'
(STAGE/'source-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
workspace=Path(checked[0][5]['source_workspace'])
for name in ('local-recursion.py','local-input.json','local-output.json'):
    shutil.copyfile(workspace/name,STAGE/name)
shutil.copyfile(ROOT/'root-checks/fixed-reference-graph-products/root-check.json',STAGE/'root-finite-check.json')
(STAGE/'INDEX.txt').write_text('Reviewed partial paper, round18\nXean native Codex gpt-6.1-sol xhigh\n\nP05.2-fixed-rational-reference-graph-products.pdf: '+ENTRIES[0][3]+'\n\nComplete frozen argument, standalone TeX, exactPASS receipt and two finite local examples and saturated-index diagnostic packet included. Essential mathematics reconstructed without external theorem premises. One harmless reviewer equation-reference correction and publication/typesetting edits recorded. Native compiler verified and exact same source exported. Same-model auditing is not formal verification/priority certification. All42original remainopen.\n')
# Keep the native editor source at its final saved path.

bundle = ROOT/'deliverables/reviewed-papers-round-19.zip'
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
(ROOT/'deliverables/round-19-bundle-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
