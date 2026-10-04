#!/usr/bin/env python3
"""Assemble authoritative proofs, native notes and audits; compile TeX twice."""
import hashlib
import json
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent
os.chdir(ROOT)

def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

commands = []
def run(args, log):
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pathlib.Path(log).write_text(result.stdout)
    commands.append(dict(argv=args, returncode=result.returncode, output_file=log))
    if result.returncode:
        print(result.stdout[-8000:])
        raise RuntimeError(f'Command failed: {args}')
    return result.stdout

run([sys.executable, 'verify_sources.py'], 'source-check.log')
run([sys.executable, 'coefficient_check.py'], 'coefficient-check.log')
assert sha('input.json') == '5950ca2b12dc2202093de059446f0076db58a9cc861e1e57ce8c82edc371753b'
raw_input = json.loads(pathlib.Path('input.json').read_text())
assert raw_input['assignment'] == pathlib.Path('assignment-original.txt').read_text()
assert raw_input['task'] == json.loads(pathlib.Path('task-original.json').read_text())

note_files = ['n1-bounded.md', 'n2-finite.md', 'n3-obstruction.md', 'n4-scope.md']
texts = [pathlib.Path(p).read_text() for p in note_files]
main = '# P15.1: prescribed-type unnormalized energy — partial result\n\n'
main += 'Authoritative mathematical argument, independent investigation, 4 October 2026. '
main += 'Original atom remains open; no claim concerning P15.2 or P15.3.\n\n'
main += '\n\n'.join(texts)
pathlib.Path('P15.1-proof.md').write_text(main)
annex = pathlib.Path('source-bodies.md').read_text()
pathlib.Path('P15.1-argument.md').write_text(main+'\n\n'+annex)

run(['pandoc', 'P15.1-proof.md', '--from', 'markdown+tex_math_single_backslash',
     '--to', 'latex', '--standalone', '--output', 'P15.1-partial.tex',
     '-V', 'documentclass:article', '-V', 'geometry:margin=1in', '-V', 'fontsize:11pt',
     '-V', 'colorlinks:true', '-M', 'title:P15.1: Prescribed-type unnormalized energy',
     '-M', 'date:4 October 2026'], 'pandoc.log')
# xurl's path formatter allows a 64-character digest to wrap in the audit paragraph.
tex = pathlib.Path('P15.1-partial.tex').read_text()
tex = re.sub(r'\\texttt\{([0-9a-f]{64})\}', lambda m: r'\path{'+m.group(1)+'}', tex)
pathlib.Path('P15.1-partial.tex').write_text(tex)
for pass_no in (1, 2):
    run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'P15.1-partial.tex'],
        f'pdflatex-pass-{pass_no}.log')
run(['pdftotext', 'P15.1-partial.pdf', 'P15.1-pdf-text.txt'], 'pdf-extract.log')
pdfinfo = run(['pdfinfo', 'P15.1-partial.pdf'], 'pdfinfo.log')
extracted = pathlib.Path('P15.1-pdf-text.txt').read_text()
assert 'concentration counterexample' in extracted
assert 'truncation identity' in extracted
assert 'class-convergent' in extracted

summaries = [
    ('For any pseudoeffective zero-volume class and actual bounded reference type, proves a cocycle, concave raw energy independent of Kähler representatives, and leading relative energy limits along class-convergent auxiliary forms with bounded potentials. No fibration; P15.1 remains open.',
     'The actual-current degree d<n is auxiliary-form independent, all same-type products above d vanish, and the degree-d energy has positive raw mass, an actual anchor, exact cocycles, constant shifts and sup-norm stability. Correct intrinsic Dirichlet IBP proves concavity, including an affine d=0 case. Its leading epsilon coefficient is independent of representatives, even for auxiliary classes converging without smooth representative convergence, provided moving potentials converge uniformly to a bounded-equivalent fixed potential. The differential-measure check requires a fixed or smoothly convergent full form and the sufficient o(epsilon) potential rate; it is not a P15.2 closure.'),
    ('Proves a genuine more-singular relative full-mass, finite joint linear-weight extension: exact capped truncation integrals, decreasing continuity, finite cocycles, concavity and same-type/fixed-class reference changes. No unbounded perturbation theorem.',
     'Using Vu v3 convexity with exact source hypotheses, every finite-family degree-d mixed product has full mass and integrable joint weights. Locality plus equal mass makes each truncation weighted integral exactly a capped integral against the limiting mixed measure. This yields the finite energy, independence of all decreasing bounded-type approximants, decreasing monotone continuity, mixed cocycles and bounded anchor changes. Fixed auxiliary-class representative independence passes through truncations. A sublogarithmic singularity example proves the domain genuinely includes unbounded differences. Increasing-sequence continuity and unbounded variations/path limits are not asserted.'),
    ('Analytic counterexample: fixed-class auxiliary representatives can make rescaled positive-perturbation relative energies diverge for one fixed, full-mass finite-energy unbounded potential. Refutes an unbounded strengthening, not P15.1 itself.',
     'On P1 x P1 with the pullback nef zero-volume class, a sublogarithmic base potential has finite degree-one energy and full mass. Smooth positive auxiliary forms in one fixed Kähler class concentrate a half-mass bump in radius exp(-epsilon^(-2/a)). The potential has finite full relative top energy at each positive epsilon, yet the rescaled energy equals its finite leading energy plus epsilon times its integral against the concentrating base form, which tends to minus infinity. A fixed smooth representative instead gives the finite leading limit. The bounded theorem is unaffected; uniform lower weighted-coefficient control cannot be deduced from degree-d finite energy.'),
    ('Characterizes the coarsest reference-scale equivalence for the bounded energy family, gives scale/type examples, and records verified source/build evidence and concrete remaining P15.1 gaps. Status partial; candidate false.',
     'Mixed auxiliary-class energies define linear functionals on Sym^(n-d) H^(1,1); their common kernel characterizes exactly when two formal scale tensors give the same whole bounded energy family. Product examples show a raw scale matters and actual reference degree can differ within one class. This characterization does not certify a universal minimal reference for all unbounded domains or supply a lower-dimensional geometric carrier. All 14 supplied LF pins match; printed source defects are preserved and corrected only in new calculations. TeX compiles twice and exact coefficient diagnostics pass, neither of which establishes analytic correctness. Original input strings remain intact; no network, extra models, subagents or heavy compute are used.')
]
notes = []
native_texts = [pathlib.Path(f'native-n{i}.md').read_text() for i in range(1, 5)]
for i, (text_body, (summary, detail)) in enumerate(zip(native_texts, summaries), start=1):
    supports = [] if i == 1 else ([f'n{j}' for j in range(1, i)] if i >= 3 else ['n1'])
    notes.append(dict(id=f'n{i}', summary=summary, detailedSummary=detail, text=text_body, support=supports))
native = dict(notes=notes, candidate=False)
pathlib.Path('notes.json').write_text(json.dumps(native, ensure_ascii=False, indent=2)+'\n')

status = dict(id='P15.1', status='partial',
              exact_result='For arbitrary pseudoeffective zero-volume classes and actual references, bounded-type degree-d raw energy has cocycle, concavity, fixed-class representative independence, and leading perturbative limits for uniformly convergent bounded-type potentials along any class-convergent Kähler representatives. A genuine joint-linear finite-energy extension has decreasing continuity and reference/cocycle properties. A fixed-class concentration example refutes the unbounded extension of the auxiliary-path limit.',
              proof_file='P15.1-argument.md',
              concrete_gaps=[
                  'Original P15.1 is not claimed solved: the construction has explicitly scoped bounded and joint-finite-energy domains.',
                  'The unbounded class-convergent auxiliary-representative path limit is false without added control (explicit analytic counterexample).',
                  'General lower-degree weighted integrability/control and unbounded moving-potential perturbative limits are not established, even for fixed forms in the general reference setting.',
                  'Only decreasing monotone continuity and finite-dimensional bounded variation are proved; arbitrary increasing continuity and unbounded differential/path calculus remain unproved here.',
                  'No universal minimal scale for unbounded domains, geometric d-dimensional carrier, numerical-dimension identification, or general leading class-volume coefficient theorem is provided.'
              ])
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
pathlib.Path('status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2)+'\n')

versions = {}
for program in ('python', 'pandoc', 'pdflatex', 'pdfinfo'):
    binary = shutil.which(program)
    if binary:
        result = subprocess.run([binary, '--version'] if program != 'pdfinfo' else [binary, '-v'],
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        versions[program] = dict(path=binary, version=result.stdout.splitlines()[0])
audit = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(), cwd=str(ROOT),
             platform=platform.platform(), python=sys.version, versions=versions,
             input_sha256=sha('input.json'), commands=commands,
             tex_compilation_passes=2, pdf_sha256=sha('P15.1-partial.pdf'),
             pdf_info=pdfinfo, note_support_validation='all supports are earlier local note IDs',
             source_validation='14/14 supplied LF-range pins match',
             mathematical_certification=False)
pathlib.Path('build-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')
author = dict(requested_execution='Xean native Codex gpt-6.1-sol xhigh',
              execution='Native available Codex session; no additional model or subagent',
              exact_model_attestation='Not independently exposed by this runtime',
              authorship='Independent mathematical investigation and artifact assembly in the assigned workspace',
              external_feedback_used=False, network_used=False, installation_used=False,
              source_status='Standard source foundations; no literature-priority or independent correctness verdict',
              prohibited_changes_performed=False, original_input_sha256=sha('input.json'))
pathlib.Path('author-audit.json').write_text(json.dumps(author, indent=2)+'\n')
research = dict(status='partial', proof_claims=['n1','n2'], analytic_counterexample='n3',
                reference_scope='n4', supplied_fibration_assumption=False,
                rejected_extensions=[
                    'Rate-free or full-form-free measure assertion for arbitrary auxiliary class paths',
                    'Class-convergent representative path theorem for all unbounded finite-energy potentials',
                    'Identification of actual-reference degree with class numerical dimension',
                    'Full positive-epsilon energy representative independence'],
                source_defects=['Vu v3 printed missing one-half in repeated square expansions/cutoffs',
                                'Vu v1 Proposition 4.2 m/n and subscript defects',
                                'Vu v1 dc/ddc malformed plain-text extraction'],
                source_defect_handling='Immutable quotations; correct intrinsic half-factor with direct cutoff estimates',
                heavy_computation=False, supervised_compute_needed=False,
                independent_review=False,
                limitations=status['concrete_gaps'])
pathlib.Path('research-audit.json').write_text(json.dumps(research, indent=2)+'\n')

known = set()
for note in notes:
    assert set(note['support']) <= known
    known.add(note['id'])
manifest = {}
for path in sorted(ROOT.iterdir()):
    if path.is_file() and path.name != 'artifact-manifest.json':
        manifest[path.name] = dict(bytes=path.stat().st_size, sha256=sha(path))
pathlib.Path('artifact-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print('Build complete: 2 successful pdflatex passes; PDF extraction checks passed.')
print('Source pins: 14/14. Exact Vandermonde diagnostics: '+str(json.loads(pathlib.Path('coefficient-check.json').read_text())['vandermonde_cases'])+' cases.')
print('Status: partial. Native notes: n1, n2, n3, n4. Candidate: false.')
