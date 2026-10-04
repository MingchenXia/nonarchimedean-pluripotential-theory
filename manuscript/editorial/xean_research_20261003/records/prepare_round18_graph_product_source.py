"""Prepare the exact accepted universal graph-product manuscript."""
from pathlib import Path
import datetime, hashlib, json, re

ROOT = Path('/workspace/research')
REVIEW = ROOT/'campaigns/round-15/P05.2-graph-product-geometric-review'
OUT = ROOT/'deliverables/round-18'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
run = json.loads((REVIEW/'run.json').read_text())
result = run['campaign']['result']
attestation = json.loads((REVIEW/'review-read-attestation.json').read_text())
binding = json.loads((REVIEW/'source-artifact-binding.json').read_text())
freeze = json.loads((REVIEW/'freeze.json').read_text())
assert run['campaign']['status'] == 'completed' and result['verdict'] == 'PASS'
assert not result['premises'] and not result['passages']
assert attestation['publish_exact_scope'] and attestation['full_report_premises_and_passages_read']
assert attestation['run_sha256'] == sha(REVIEW/'run.json')
assert sha(REVIEW/'argument.md') == freeze['argument_sha256']
for key, h in [('source_tex', 'source_tex_sha256'),
               ('main_argument', 'main_argument_sha256'),
               ('declared_proof_file', 'declared_proof_sha256')]:
    assert sha(Path(binding[key])) == binding[h] == freeze[h]
source = Path(binding['source_tex']).read_text()
edits = []

def replace(before, after, reason, count=1):
    global source
    assert source.count(before) == count, (before, source.count(before))
    edits.append({'before': before, 'after': after,
                  'expected_occurrences': count, 'reason': reason})
    source = source.replace(before, after)

replace('Unverified P05.2 proof draft', 'Xean research manuscript',
        'Publication author metadata.', 2)
replace(r'\date{3 October 2026}', r'\date{4 October 2026}', 'Publication date metadata.')
replace('Universal graph-product theorem (draft).', 'Universal graph-product theorem.',
        'The exact partial theorem has now passed independent review.')
replace(
    'Status is \\textbf{partial},\ncandidate \\textbf{false}. All claims here are unverified drafts;',
    'This is a reviewed partial theorem;',
    'Remove obsolete author draft/candidate metadata; original-scope limitation retained.')

replace(r'\rho(r)', r'\rho_0(r)',
        'Reviewer clarification: use the homogeneous norm on recession vectors.', 2)
replace(
    'For a nonzero recession vector \\(r\\) of any reference affine cell,',
    'Write \\(\\rho_0(r)=\\|r_1\\|_1+\\|r_2\\|_1\\) for the homogeneous\n'
    'ambient norm of a recession vector. For a nonzero recession vector\n'
    '\\(r\\) of any reference affine cell,',
    'Reviewer clarification of existing recession estimate; no mathematical change.')
replace(
    'precisely the product of short original \\(A,B\\) stars',
    'the intersection of the local product of original \\(A,B\\) stars with that neighbourhood',
    'Reviewer clarification: the norm ball intersects the product star; it is not a product of separate norm balls.')

start = source.index('Artifacts in this fresh workspace:')
end = source.index('Bibliography:', start)
replace(source[start:end], r'''The complete frozen argument, finite diagnostic packet and independent
review receipt accompany this paper. The Xean native Codex review used
\texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning and returned PASS
for the exact universal graph-product characterization, with no essential
external theorem premises. Its full report and the immutable
argument/source bindings were read and checked. The two wording
clarifications concerning the local star neighbourhood and homogeneous
recession norm are recorded; they do not change the mathematics.

The root read the complete proof, both canonical native notes and the
author audit. The two finite local examples were recomputed in a new
directory, preserving all original artifacts. All forty-nine saturated
cone indices were also checked directly by greatest common divisors of
the ambient two-by-two minors. These finite checks are supplementary
evidence; the universal theorem is the proof above.

The saved standalone source was opened in the native editor for
compilation. The exported PDF uses that same source. Computational
review, source bindings and successful typesetting are not formal
verification or priority certification. Original P05.2's classification
of fixed arbitrary balanced pairs remains open.

''', 'Replace historical author artifact/rerun instructions by exact review and publication provenance.')

pattern = r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    match = re.fullmatch(pattern, token)
    replace(token, '\\'+match.group(1)+'{'+match.group(2)+'}',
            'Harmless explicit alphabet grouping for native unicode-math.', source.count(token))
pattern = r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    replace(token, token[0]+'{'+token[1:]+'}',
            'Harmless script grouping for native unicode-math.', source.count(token))

assert source.count(r'\end{document}') == 1
OUT.mkdir(exist_ok=False)
tex = OUT/'P05.2-universal-graph-product-contact.tex'
tex.write_text(source)
(REVIEW/'publication-edits.json').write_text(json.dumps(edits, ensure_ascii=False, indent=2)+'\n')
record = {
    'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'tex': str(tex), 'sha256': sha(tex), 'governing_review': str(REVIEW),
    'publication_edits_sha256': sha(REVIEW/'publication-edits.json'),
    'native_compilation_pending': True,
}
(ROOT/'deliverables/round-18-source-preparation.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
