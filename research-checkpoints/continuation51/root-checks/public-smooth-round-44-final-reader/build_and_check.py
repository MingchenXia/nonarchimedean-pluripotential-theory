#!/usr/bin/env python3
"""Rebuild the two proof formats, compile twice, and retain actual diagnostics."""
import hashlib
import json
import re
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / 'build'
BUILD.mkdir(exist_ok=True)

def run(command, transcript):
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    text = result.stdout + result.stderr
    (ROOT / transcript).write_text(text)
    return {'command': command, 'returncode': result.returncode,
            'transcript': transcript, 'stdout_lines': len(result.stdout.splitlines()),
            'stderr_lines': len(result.stderr.splitlines())}

checks = {'input_byte_identity': (ROOT/'input.json').read_bytes() == (ROOT/'input-original.json').read_bytes()}
original = json.loads((ROOT/'input-original.json').read_bytes())
checks['assignment_identity'] = (ROOT/'assignment-original.txt').read_text() == original['assignment']
checks['task_semantic_identity'] = json.loads((ROOT/'task-original.json').read_text()) == original['task']
checks['source_hash_checks'] = 'python3 verify_sources.py; detailed results in source-extracts/source-provenance.json'
checks['gap_exact_rational_samples'] = []
for j in [1, 2, 3, 8, 16, 32]:
    e, next_e = Fraction(1,2**j), Fraction(1,2**(j+1))
    lower_gap = 4*(e-next_e)-e-next_e
    assert lower_gap == e/2 and lower_gap > 0
    checks['gap_exact_rational_samples'].append({'j':j, 'epsilon': str(e),
                                               'worst_case_gap': str(lower_gap)})
checks['gap_general_proof'] = 'Algebraically, 4(e-e/2)-e-e/2 = e/2 for every e>0. The finite samples are diagnostics only.'
checks['mathematical_verification'] = 'Unverified draft. Input/hash/arithmetic/build checks do not certify the new mathematical arguments.'
checks['artifact_commands'] = []
checks['artifact_commands'].append(run(
    ['pandoc','-f','latex','-t','markdown+tex_math_dollars','--wrap=none','-s',
     'P02.4-paper.tex','-o','P02.4-argument.md'], 'build/pandoc-transcript.txt'))

# Turn Pandoc's theorem divisions/citation syntax into readable ordinary Markdown.
# The mathematical paragraphs and equations are unchanged; retain the raw conversion.
mdfile = ROOT / 'P02.4-argument.md'
if mdfile.exists():
    raw = mdfile.read_text()
    (BUILD / 'P02.4-pandoc-raw.md').write_text(raw)
    metadata, body = raw[4:].split('\n---\n', 1)
    abstract = re.search(r'abstract: \|\n(.*?)(?=\nauthor:)', metadata, re.S).group(1)
    abstract = '\n'.join(s.removeprefix('  ') for s in abstract.splitlines())
    body = re.sub(r'^::: \{#([^ ]+) .*\}\n', lambda m: '<a id="'+m.group(1)+'"></a>\n', body, flags=re.M)
    body = re.sub(r'^:::[^\n]*\n', '', body, flags=re.M)
    body = re.sub(r'\{reference-type="ref" reference="[^"]*"\}', '', body)
    body = re.sub(r'\[@(\w+)([^\]]*)\]', lambda m: '['+m.group(1)+(', '+m.group(2).strip() if m.group(2).strip() else '')+']', body)
    bibliography_start = body.find('\n9 W. Gubler and J. Rabinoff,')
    if bibliography_start >= 0:
        body = body[:bibliography_start]
    tex = (ROOT/'P02.4-paper.tex').read_text()
    bibtext = tex.split('\\begin{thebibliography}{9}',1)[1].split('\\end{thebibliography}',1)[0]
    bibentries = re.findall(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem|\Z)', bibtext, re.S)
    bibliography = '\n# Published sources\n\n'
    for key, text in bibentries:
        text = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', text)
        text = re.sub(r'\\url\{([^}]*)\}', r'<\1>', text)
        text = text.replace('\\S', '§')
        text = ' '.join(text.split())
        bibliography += '- **'+key+'**: '+text+'\n\n'
    mdfile.write_text('# P02.4: ordinary CLD-smooth decreasing regularization\n\n'+abstract+'\n\n'+body.strip()+'\n'+bibliography)

diagnostics = {'runs': []}
command = ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
           '-output-directory=build','P02.4-paper.tex']
for number in [1,2]:
    record = run(command, f'build/tex-pass-{number}-transcript.txt')
    log = BUILD / 'P02.4-paper.log'
    if log.exists():
        saved = BUILD / f'tex-pass-{number}.log'
        shutil.copyfile(log, saved)
        lines = log.read_text(errors='replace').splitlines()
        record['saved_log'] = str(saved.relative_to(ROOT))
        record['warnings'] = [s for s in lines if 'Warning' in s]
        record['layout_diagnostics'] = [s for s in lines if 'Overfull' in s or 'Underfull' in s]
        record['error_lines'] = [s for s in lines if s.startswith('!') or re.search(r'\.tex:\d+:',s)]
        record['output_line'] = next((s for s in lines if s.startswith('Output written')), None)
    diagnostics['runs'].append(record)

pdf = BUILD / 'P02.4-paper.pdf'
if pdf.exists():
    shutil.copyfile(pdf, ROOT / 'P02.4-paper.pdf')
    info = run(['pdfinfo','P02.4-paper.pdf'], 'build/pdfinfo.txt')
    checks['artifact_commands'].append(info)
    diagnostics['pdf_sha256'] = hashlib.sha256(pdf.read_bytes()).hexdigest()
    diagnostics['pdf_bytes'] = pdf.stat().st_size

diagnostics['interpretation'] = 'Compilation success and hashes are document-integrity evidence only, not mathematical correctness evidence.'
(ROOT/'build-diagnostics.json').write_text(json.dumps(diagnostics,indent=2)+'\n')
checks['all_input_checks_passed'] = all(checks[k] for k in ['input_byte_identity','assignment_identity','task_semantic_identity'])
checks['two_tex_passes_succeeded'] = all(x['returncode']==0 for x in diagnostics['runs'])
checks['markdown_generated'] = checks['artifact_commands'][0]['returncode']==0
(ROOT/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')

status = {
    'id':'P02.4',
    'status':'partial',
    'exact_result': 'Arbitrary-target decreasing ordinary CLD-smooth psh sequences on specified countably dense-field curve sectors, including finite unibranch algebraic normalization; all targets on saturated proper-projective-fibre products; a classical boundary spike obstructing every local continuous sequence for uncountable residue field, with an explicit ordinary smooth positive-form sequence for that spike when the residue field is countable. The full original characterization is not solved.',
    'proof_file':'P02.4-argument.md',
    'concrete_gaps': [
        'All arbitrary noninvariant classical psh sheaf germs on nonsaturated higher-dimensional charts; saturated-domain constancy does not cover them.',
        'A sharp geometric necessary-and-sufficient range for every target, beyond the proved sufficient curve sector and particular boundary-spike obstruction.',
        'Boundaryless curves with nonzero residual Picard harmonic quotient; failure of harmonic ordinary smoothness has not been proved to obstruct approximation.',
        'General multibranch or nonalgebraic singular curves and synchronization/descent of ordinary smooth approximants under general finite normalization.',
        'Arbitrary-target sequence extraction over fields without a countable dense subset.',
        'Non-algebraically-closed bases and strict scalar descent; constructed sequences are compatible with all scalar pullbacks but no general descent theorem is proved.',
        'General overlap gluing of independently constructed tropical-chart approximants; overlaps here use actual globally defined functions on one fixed neighborhood.'
    ]}
assert list(status) == ['id','status','exact_result','proof_file','concrete_gaps']
(ROOT/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')

summary = json.dumps({'input_checks':checks['all_input_checks_passed'],
                  'markdown_generated':checks['markdown_generated'],
                  'tex_returncodes':[x['returncode'] for x in diagnostics['runs']],
                  'tex_warnings':[x.get('warnings',[]) for x in diagnostics['runs']],
                  'tex_layout':[x.get('layout_diagnostics',[]) for x in diagnostics['runs']]},indent=2)
(ROOT/'build-check-output.txt').write_text(summary+'\n')
print(summary)
