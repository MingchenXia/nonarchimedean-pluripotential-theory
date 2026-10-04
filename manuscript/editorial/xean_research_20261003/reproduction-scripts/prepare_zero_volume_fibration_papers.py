"""Prepare two reviewed standalone sources; mathematics remains unchanged."""
from pathlib import Path
import datetime
import hashlib
import json
import re

root = Path('/workspace/research')
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
for atom, number, relative, filename, counts in [
    ('P15.2', 27, 'round-27/P15.2-relative-zero-volume-operator', 'P15.2-relative-zero-volume-operator.tex', (5, 6)),
    ('P15.1', 28, 'round-28/P15.1-relative-zero-volume-energy', 'P15.1-relative-zero-volume-energy.tex', (6, 9)),
]:
    review = root / 'campaigns' / (relative + '-review')
    attestation = json.loads((review / 'review-read-attestation.json').read_text())
    binding = json.loads((review / 'source-artifact-binding.json').read_text())
    assert attestation['verdict'] == 'PASS' and attestation['publish_exact_scope']
    assert attestation['run_sha256'] == sha(review / 'run.json')
    original = Path(binding['source_tex'])
    assert sha(original) == binding['source_tex_sha256']
    source = original.read_text()
    edits = []

    def replace(before, after, reason, expected=1):
        global source
        assert source.count(before) == expected, (atom, before, source.count(before))
        source = source.replace(before, after)
        edits.append({'before': before, 'after': after, 'expected_occurrences': expected, 'reason': reason})

    if atom == 'P15.2':
        replace('Xean research author draft', 'Xean research manuscript', 'Publication metadata.', 2)
        replace(
            'Partial progress for P15.2; the original general pseudoeffective zero-volume atom remains open. Author draft, 4 October 2026. No literature-priority or independent-verification claim is made.',
            'This paper proves a relative base Monge--Ampère theorem for a supplied holomorphic fibration. Its complete argument passed an independent Xean review at this exact bounded scope. The original general pseudoeffective zero-volume problem P15.2 remains open. No literature-priority claim is made.',
            'Replace author-draft bookkeeping with the completed exact-scope review status.',
        )
        replace(
            '\\end{enumerate}',
            r'''\item
  P. Deligne, P. Griffiths, J. Morgan, and D. Sullivan,
  \emph{Real homotopy theory of K\"ahler manifolds}, Invent. Math. 29
  (1975), 245--274, Lemma 5.11 and Remark 5.14. The compact K\"ahler
  \(dd^c\) lemma identifies the de Rham and Bott--Chern representative
  changes used above.
\end{enumerate}''',
            'Make the standard dd-c foundation behind the existing cohomology parenthesis explicit; no change to the theorem or proof.',
        )
    else:
        replace('Author research draft', 'Xean research manuscript', 'Publication metadata.', 2)
        start = source.index('The operator proposal and the earlier comparison papers are unverified')
        end = source.index('Throughout,', start)
        replace(source[start:end], r'''The proof uses the precisely stated standard foundations and the new
applications proved below. The unverified operator proposal and earlier
comparison papers supply no mathematical premise. Original research
inputs and the complete frozen argument remain in the supporting packet.
An independent Xean review accepted exactly the bounded supplied-fibration
scope, including the optional continuous-descent assertion at its separate
connected-fibre hypothesis.

''', 'Replace input-file bookkeeping with completed exact-scope review provenance.')
        start = source.index('\\subsection{Execution, evidence, and')
        end = source.index('\\end{document}', start)
        replace(source[start:end], '', 'Replace obsolete execution appendix with the review/evidence paragraph below; the complete mathematical proof and limitations preceding it remain intact.')

    review_text = r'''\section*{Review and supporting evidence}

The independent Xean native Codex review used \texttt{gpt-6.1-sol} with
\texttt{xhigh} reasoning. The entire report, PREMISECOUNT premises and
PASSAGECOUNT primary-source passages were read and bound to the unchanged
author argument, TeX source and partial status. The reviewer reconstructed
the new applications of the standard bounded Bedford--Taylor calculus,
integration by parts, cohomological mass identities and geometric
foundations. No substantive mathematical repair was required.

The complete author argument and both actual canonical native notes were
read. Six supplied primary bodies were checked against their exact LF
bytes and source hashes. Both diagnostic and two-pass document builds
were repeated in fresh copies, producing TeX byte-identical to the frozen
author source. Publication edits update review provenance, citations and
explicit math-alphabet grouping. The supporting packet preserves the
full frozen argument, review, canonical notes, source provenance and read
records; native editor compilation and PDF exports are recorded separately.

This review establishes the stated special-case result. Same-model review,
document compilation and file integrity are not formal verification or
priority certification. The original general problem ATOM remains open;
no general carrier construction, minimum-reference theorem, unbounded
prescribed-type extension or arbitrary degenerate perturbation path is
claimed.

'''
    review_text = review_text.replace('PREMISECOUNT', str(counts[0])).replace('PASSAGECOUNT', str(counts[1])).replace('ATOM', atom)
    replace('\\end{document}', review_text + '\\end{document}', 'Append completed review and supporting-evidence provenance.')
    pattern = r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
    for token in dict.fromkeys(match.group(0) for match in re.finditer(pattern, source)):
        match = re.fullmatch(pattern, token)
        replace(token, '\\' + match.group(1) + '{' + match.group(2) + '}', 'Explicit native math-alphabet grouping.', source.count(token))
    pattern = r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
    for token in dict.fromkeys(match.group(0) for match in re.finditer(pattern, source)):
        replace(token, token[0] + '{' + token[1:] + '}', 'Explicit native script grouping.', source.count(token))

    output = root / 'deliverables' / ('round-' + str(number))
    output.mkdir(exist_ok=False)
    tex = output / filename
    tex.write_text(source)
    edits_path = review / 'publication-edits.json'
    assert not edits_path.exists()
    edits_path.write_text(json.dumps(edits, ensure_ascii=False, indent=2) + '\n')
    prepared = {
        'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'atom': atom, 'tex': str(tex), 'sha256': sha(tex),
        'governing_review': str(review),
        'publication_edits_sha256': sha(edits_path),
        'native_compilation_pending': True, 'full_original_atom_solved': False,
    }
    path = root / 'deliverables' / ('round-' + str(number) + '-source-preparation.json')
    assert not path.exists()
    path.write_text(json.dumps(prepared, indent=2) + '\n')
    print(json.dumps(prepared, indent=2))
