"""Create review-bound publications without changing frozen authors or reviews."""
from pathlib import Path
import datetime, hashlib, json, re, sys

ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
number = int(sys.argv[1])
assert number in (31, 32)
atom = 'P15.1' if number == 31 else 'P15.2'
stem = 'P15.1-minimum-reference-finite-energy' if number == 31 else 'P15.2-minimum-reference-full-mass-operator'
review = ROOT / 'campaigns' / f'round-{number}' / (stem + '-review')
att = json.loads((review / 'review-read-attestation.json').read_text())
binding = json.loads((review / 'source-artifact-binding.json').read_text())
result = json.loads((review / 'review-result.json').read_text())
assert att['verdict'] == result['verdict'] == 'PASS' and att['publish_exact_scope']
assert sha(review / 'run.json') == att['run_sha256']
original = Path(binding['source_tex'])
assert sha(original) == binding['source_tex_sha256']
source = original.read_text()
edits = []

def replace(before, after, reason, expected=1):
    global source
    assert source.count(before) == expected, (before, source.count(before))
    source = source.replace(before, after)
    edits.append({'before': before, 'after': after, 'expected_occurrences': expected, 'reason': reason})

if number == 31:
    replace('Authoritative single-worker research draft, 4 October 2026. Status:\npartial; original atom remains open.',
            'Xean research manuscript, 4 October 2026. The complete proof passed an\nindependent review at the scope stated below. Original P15.1 remains open\npending a separate audit of the full question.', 'Update completed scoped review provenance.')
    replace('This is an unverified mathematical draft addressing only P15.1. No prior\nreview verdict or prior note is a hypothesis.',
            'This paper addresses P15.1 at the scope stated below. No prior review\nverdict or prior note is a mathematical hypothesis.', 'Replace obsolete author draft metadata.')
    start = source.index('\\subsection{Execution and artifact\ncontract}')
    end = source.index('\\end{document}', start)
    replace(source[start:end], '', 'Move author execution bookkeeping into the full supporting dossier; preserve all mathematical arguments and limitations.')
else:
    replace('Author: native Codex execution in the fresh assigned workspace. Date: 4\nOctober 2026. Status: \\textbf{partial}; unverified mathematical draft.\nThe original P15.2 atom remains open. Only this atom is investigated;\nenergy integrability is used solely to specify a common operator\nsubdomain.',
            'Xean research manuscript, 4 October 2026. The complete proof passed an\nindependent review at its stated scope. Original P15.2 remains open\npending a separate audit of the full question. Energy integrability\nspecifies a common operator subdomain.', 'Update completed scoped review provenance.')
    replace(r'Condition (\emph{), give', 'Condition (*), give', 'Restore literal star misparsed as Markdown emphasis.')
    replace(r'Condition (}) has', 'Condition (*) has', 'Close the same literal-star conversion repair.')
review_text = r'''\section*{Review and supporting evidence}

The complete proof passed an independent Xean native Codex review using
\texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning. Its entire report,
PREMISECOUNT premises and PASSAGECOUNT source passages were read and bound
to the frozen proof, TeX source and author status. All new mathematical
arguments, actual canonical notes and the author manuscript were read in
full. All 24 selected literal primary-source bodies were authenticated;
unchanged complete primary reads were explicitly reused. The separate
StonyBrook source authenticates the DGMS real smooth $dd^c$ lemma and its
complete selected proof. The GZ bounded capacity hypothesis and Vu bounded
product-factor hypothesis are retained through the proved truncation
applications. Literal source defects are preserved in the dossier; the
new proofs use the correct intrinsic one-half gradient identity.

REPROTEXT

Publication edits update review provenance and typesetting and remove
execution bookkeeping. They do not repair a mathematical gap or change
the theorem. The full frozen proof, complete primary units, source audits,
canonical notes, review and root read records accompany this manuscript.
Native editor compilation and local PDF export are recorded separately.
Same-model independent review, compilation and file integrity are not
formal verification or literature-priority certification. Original ATOM
closure requires a separate audit against the exact original question;
the present acceptance is limited to the theorem stated in this paper.

'''
repro = ('A fresh copied build reproduced byte-identical mathematical proof and\nTeX source. Execution checks are evidence of reproducibility, not analytic\ncorrectness.' if number == 31 else
         'A fresh copied build reproduced byte-identical mathematical proof,\nTeX source and literal primary annex. The full argument differs only in\nthe execution paragraph containing the newly generated PDF digest; that\nsingle substitution was verified. Execution checks are reproducibility\nevidence, not analytic correctness.')
review_text = review_text.replace('PREMISECOUNT', str(len(result['premises']))).replace('PASSAGECOUNT', str(len(result['passages']))).replace('REPROTEXT', repro).replace('ATOM', atom)
replace('\\end{document}', review_text + '\\end{document}', 'Append scoped review, source qualification and accurate reproducibility provenance.')
pattern = r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    m = re.fullmatch(pattern, token)
    replace(token, '\\' + m.group(1) + '{' + m.group(2) + '}', 'Explicit native math-alphabet grouping.', source.count(token))
pattern = r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    replace(token, token[0] + '{' + token[1:] + '}', 'Explicit native script grouping.', source.count(token))
output = ROOT / 'deliverables' / f'round-{number}'
output.mkdir(exist_ok=False)
tex = output / (stem + '.tex')
tex.write_text(source)
edit_path = review / 'publication-edits.json'
assert not edit_path.exists()
edit_path.write_text(json.dumps(edits, ensure_ascii=False, indent=2) + '\n')
record = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'atom': atom,
          'tex': str(tex), 'sha256': sha(tex), 'governing_review': str(review),
          'publication_edits_sha256': sha(edit_path), 'native_compilation_pending': True,
          'full_original_atom_solved': False}
p = ROOT / 'deliverables' / f'round-{number}-source-preparation.json'
assert not p.exists()
p.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
