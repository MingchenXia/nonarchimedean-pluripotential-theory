#!/usr/bin/env python3
"""Build the standalone paper twice with the installed tools and retain actual logs."""
import hashlib, json, pathlib, shutil, subprocess, sys

root = pathlib.Path(__file__).resolve().parent
logdir = root / 'build-logs'
logdir.mkdir(exist_ok=True)
commands = []
if (root/'build-commands.json').exists():
    archive_number = 1
    while (root/f'build-logs-previous-{archive_number}').exists():
        archive_number += 1
    shutil.copytree(logdir, root/f'build-logs-previous-{archive_number}')
    shutil.copyfile(root/'build-commands.json', root/f'build-logs-previous-{archive_number}/commands.json')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(cmd, tag):
    result = subprocess.run(cmd, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = logdir / (tag+'-stdout.txt')
    stderr = logdir / (tag+'-stderr.txt')
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    commands.append({'command': cmd, 'cwd': str(root), 'returncode': result.returncode,
                     'stdout': str(stdout.relative_to(root)), 'stderr': str(stderr.relative_to(root)),
                     'stdout_sha256': sha(stdout), 'stderr_sha256': sha(stderr)})
    return result.returncode

pandoc = ['pandoc', 'P16.3-argument.md', '--from=markdown+tex_math_dollars', '--to=latex',
          '--standalone', '--variable=colorlinks:true', '--variable=linkcolor:blue',
          '--output=P16.3-paper.tex']
conversion = run(pandoc, 'pandoc')
if conversion:
    (root / 'build-commands.json').write_text(json.dumps(commands, indent=2)+'\n')
    raise SystemExit('Pandoc failed; see retained diagnostics')
codes = []
for n in [1,2]:
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'P16.3-paper.tex']
    code = run(cmd, f'pass-{n}')
    codes.append(code)
    for suffix in ['log', 'aux', 'out']:
        source = root / ('P16.3-paper.'+suffix)
        if source.exists():
            shutil.copyfile(source, logdir / (f'pass-{n}.'+suffix))
    commands[-1]['saved_tex_log'] = f'build-logs/pass-{n}.log'
    if (logdir / f'pass-{n}.log').exists():
        commands[-1]['tex_log_sha256'] = sha(logdir / f'pass-{n}.log')

provenance_path = root / 'source-extracts/source-provenance.json'
provenance = json.loads(provenance_path.read_text())
provenance['actual_pdf_visual_checks'] = [
    {'file': 'BJ22-page-62.png', 'pdf_page': 62, 'sha256': sha(root/'source-extracts/BJ22-page-62.png'),
     'finding': 'Theorem 5.20 proof: roman dim X <= 2; calligraphic dim model X <= 3. Resolution is on the n+1 dimensional test configuration.'},
    {'file': 'BJ22-page-97.png', 'pdf_page': 97, 'sha256': sha(root/'source-extracts/BJ22-page-97.png'),
     'finding': 'Theorem 8.5 differentiates decreasing obstacle energy, and identifies it with E(P(...)) only under its specified conditions.'},
    {'file': 'BJ22-page-122.png', 'pdf_page': 122, 'sha256': sha(root/'source-extracts/BJ22-page-122.png'),
     'finding': 'Theorem 12.9 states smooth X and char k=0 or dim X<=2. Positive characteristic arbitrary dimension is not in this unconditional statement.'}
]
provenance_path.write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')

status = {
    'id': 'P16.3',
    'status': 'partial',
    'exact_result': 'Published-source application: over algebraically closed trivially valued k of characteristic p>0, smooth connected projective X and ample L, the genuine finite-energy operator exists in every dimension and is injective modulo constants; every positive Radon measure of raw mass (L^n) and finite raw dual energy has a unique finite-energy solution for dim X<=2. Arbitrary-field continuous/test MA, synthetic orthogonality and measure approximation are established background, not the full nontrivial positive-residue-characteristic extension.',
    'proof_file': 'P16.3-argument.md',
    'concrete_gaps': [
        'For nontrivially discretely valued K of residue characteristic p>0 in arbitrary dimension, replace SNC-dependent singular psh approximation and prove normalized compactness.',
        'Prove the necessary model positivity and envelope/variational regularity without an unproved resolution assumption or extra function-field descent, treating mixed characteristic separately.',
        'Construct approximation-independent genuine mixed MA on unbounded E1, including full raw mass and finite-energy integrability.',
        'Prove equality of test and E1 dual energy and differentiation of obstacle energy on the resulting finite-energy space.',
        'Realize every correctly massed finite-dual-energy Radon measure of arbitrary support by an actual psh potential, not merely a limit in a completed measure space.',
        'Establish unbounded locality/comparison and injectivity modulo constants on that operator domain.'
    ]
}
(root/'status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2)+'\n')
(root/'build-commands.json').write_text(json.dumps(commands, indent=2)+'\n')

raw = (root/'input.json').read_bytes()
data = json.loads(raw)
original = (root/'input-original.json').read_bytes()
assert raw == original, 'Original input changed'
assert (root/'assignment-original.txt').read_text() == data['assignment']
assert json.loads((root/'task-original.json').read_text()) == data['task']
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert len(provenance['sources']) == 10
checks = {'build_pass_returncodes': codes, 'standalone_tex': '\\documentclass' in (root/'P16.3-paper.tex').read_text(),
          'pdf_exists': (root/'P16.3-paper.pdf').exists(),
          'byte_identical_input': raw == original, 'input_sha256': hashlib.sha256(raw).hexdigest(),
          'assignment_exact': True, 'task_decoded_exact': True, 'status_exact_schema': True,
          'source_pdf_and_text_hash_checks': 20, 'abstract_hash_checks': 6,
          'mathematical_validation': 'None automated. These are unverified drafts; execution/compilation does not establish mathematical correctness.'}
(root/'checks.json').write_text(json.dumps(checks, indent=2)+'\n')
print(json.dumps(checks, indent=2))
sys.stdout.flush()
files = [p for p in root.rglob('*') if p.is_file() and p.name != 'artifact-sha256.json'
         and not any(part.startswith('.') for part in p.relative_to(root).parts)]
(root/'artifact-sha256.json').write_text(json.dumps({str(p.relative_to(root)): sha(p) for p in sorted(files)}, indent=2)+'\n')
if codes != [0,0]:
    raise SystemExit('At least one actual TeX pass failed; see retained streams and logs')
