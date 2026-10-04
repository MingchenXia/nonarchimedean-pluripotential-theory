"""Prepare a reviewed manuscript with replayable metadata and conversion edits."""
from pathlib import Path
import datetime, hashlib, json, re, sys
ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
number = int(sys.argv[1]); assert number in (29, 30)
atom = 'P15.1' if number == 29 else 'P15.2'
stem = 'P15.1-prescribed-type-zero-volume-energy' if number == 29 else 'P15.2-prescribed-type-zero-volume-operator'
review = ROOT / 'campaigns' / ('round-' + str(number)) / (stem + '-review')
att = json.loads((review / 'review-read-attestation.json').read_text())
binding = json.loads((review / 'source-artifact-binding.json').read_text())
result = json.loads((review / 'review-result.json').read_text())
assert att['verdict'] == result['verdict'] == 'PASS' and att['publish_exact_scope']
assert sha(review / 'run.json') == att['run_sha256']
original = Path(binding['source_tex']); assert sha(original) == binding['source_tex_sha256']
source = original.read_text(); edits = []
def replace(before, after, reason, expected=1):
    global source
    assert source.count(before) == expected, (before, source.count(before))
    source = source.replace(before, after)
    edits.append({'before': before, 'after': after, 'expected_occurrences': expected, 'reason': reason})
if number == 30:
    replace('Author: native Codex execution in the fresh assigned workspace. Date:\n2026-10-04. Status: \\textbf{partial}. This is a research draft, not an\nindependently certified theorem. Only P15.2 is addressed. Energy is\nincluded as a primitive and a perturbation diagnostic for this operator;\nno closure of P15.1 or P15.3 is claimed.',
            'Xean research manuscript, 4 October 2026. This paper proves the stated\nprescribed-type operator theorem for arbitrary pseudoeffective zero-volume\nclasses. Its complete proof passed an independent Xean review at this\nexact scope. Energy is included as a bounded primitive and a perturbation\ndiagnostic. The original general problem P15.2 remains open.',
            'Replace draft execution metadata with the completed exact-scope review status.')
    replace(r'Condition (\emph{).', 'Condition (*).', 'Restore the literal star misparsed as Markdown emphasis.')
    replace(r'Condition (}) means', 'Condition (*) means', 'Close the same literal-star conversion repair.')
    start = source.index('The finite coefficient identity in Section 7 is checked')
    end = source.index('\\end{document}', start)
    replace(source[start:end], '', 'Remove obsolete author execution bookkeeping; preserve the entire theorem, proof and residual-scope comparison.')
else:
    replace('Authoritative mathematical argument, independent investigation, 4\nOctober 2026. Original atom remains open; no claim concerning P15.2 or\nP15.3.',
            'Xean research manuscript, 4 October 2026. The complete proof passed an\nindependent Xean review at its stated scope. The original general problem\nP15.1 remains open; no closure of P15.2 or P15.3 is claimed.',
            'Completed exact-scope review provenance.')
    replace('All assertions are\nmathematical drafts, not independently certified results.',
            'The bounded theorem, finite-energy extension and analytic concentration\ncounterexample were independently reviewed at exactly the hypotheses\nstated below. Same-model review is not formal verification.',
            'Replace obsolete draft status with the exact-scope review status.')
    start = source.index('\\subsection{Audit and rerun contract}')
    end = source.index('\\end{document}', start)
    replace(source[start:end], '', 'Remove obsolete execution bookkeeping; preserve all mathematical proofs, examples and remaining scope.')
review_text = r'''\section*{Review and supporting evidence}

An independent Xean native Codex review used \texttt{gpt-6.1-sol} with
\texttt{xhigh} reasoning. Its complete report, PREMISECOUNT premises and
PASSAGECOUNT source passages were read and bound to the frozen author
proof, TeX source and partial status. The new mathematical applications,
all actual canonical notes and author manuscript were read in full.
Complete primary-source bodies were authenticated by exact source ranges;
unchanged prior complete primary reads were explicitly reused. Fresh copied
builds reproduced byte-identical proof and TeX sources. These records and
the full source dossier are retained in the supporting packet.

The literature foundations are precisely stated standard theorems applied
with checked hypotheses. Printed and extracted source defects remain in
the literal dossier. The new proofs use the correct intrinsic one-half
gradient identity, consistent differential normalization and the usual
Cauchy--Schwarz estimate. Cutoff indicators used here tend to one; their
monotonicity is essential when applying the source cutoff lemma. Source
statements whose printed proofs cite prior literature are distinguished
from the new applications proved in this paper.

Publication changes update review provenance and repair mathematical
typesetting only. Native editor compilation and two-pass PDF export are
recorded separately. Same-model independent review, document compilation
and file integrity are not formal verification or priority certification.
The paper establishes its stated scoped result; the original general
problem ATOM remains open with the limitations recorded above.

'''
review_text = review_text.replace('PREMISECOUNT', str(len(result['premises']))).replace('PASSAGECOUNT', str(len(result['passages']))).replace('ATOM', atom)
replace('\\end{document}', review_text + '\\end{document}', 'Append completed exact-scope review and evidence provenance.')
pattern = r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    m = re.fullmatch(pattern, token)
    replace(token, '\\' + m.group(1) + '{' + m.group(2) + '}', 'Explicit native math-alphabet grouping.', source.count(token))
pattern = r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    replace(token, token[0] + '{' + token[1:] + '}', 'Explicit native script grouping.', source.count(token))
output = ROOT / 'deliverables' / ('round-' + str(number)); output.mkdir(exist_ok=False)
tex = output / (stem + '.tex'); tex.write_text(source)
edit_path = review / 'publication-edits.json'; assert not edit_path.exists()
edit_path.write_text(json.dumps(edits, ensure_ascii=False, indent=2)+'\n')
record = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'atom': atom, 'tex': str(tex), 'sha256': sha(tex), 'governing_review': str(review),
          'publication_edits_sha256': sha(edit_path), 'native_compilation_pending': True,
          'full_original_atom_solved': False}
p = ROOT / 'deliverables' / ('round-' + str(number) + '-source-preparation.json'); assert not p.exists()
p.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
