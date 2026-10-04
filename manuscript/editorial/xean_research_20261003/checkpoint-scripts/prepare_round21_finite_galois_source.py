"""Prepare the reviewed finite-Galois paper; never alter its frozen proof."""
from pathlib import Path
import datetime, hashlib, json, re

root = Path('/workspace/research')
review = root/'campaigns/round-19/P06.2-general-finite-galois-review'
out = root/'deliverables/round-21'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = json.loads((review/'run.json').read_text())['campaign']['result']
att = json.loads((review/'review-read-attestation.json').read_text())
freeze = json.loads((review/'freeze.json').read_text())
binding = json.loads((review/'source-artifact-binding.json').read_text())
assert result['verdict'] == 'PASS' and att['publish_exact_scope']
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read','root_full_main_and_all_canonical_notes_read'))
assert att['run_sha256'] == sha(review/'run.json')
assert sha(review/'argument.md') == freeze['argument_sha256']
for key, hash_key in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(binding[key])) == freeze[hash_key] == binding[hash_key]
source = Path(binding['source_tex']).read_text()
edits = []
def replace(before, after, reason, count=1):
    global source
    assert source.count(before) == count, (before, source.count(before))
    source = source.replace(before, after)
    edits.append(dict(before=before, after=after, reason=reason, expected_occurrences=count))

replace('Unverified proof draft, 4 October 2026. Author audit only. The original',
        'Reviewed partial theorem, 4 October 2026. The original', 'Publication status after exact-scope independent review.')
replace('establishes the requested finite-Galois gate if the proof withstands\nindependent review.',
        'establishes the finite-Galois current-transport gate and has passed\nan independent Xean review.', 'Publication status; retain the original recognition gap.')
replace('interior is its ordinary topological interior; relative interior is\npreserved by base change, including complete ground-field extension.',
        'interior is its ordinary topological interior. Under base change,\ninterior points remain interior; only this inclusion and the resulting\nstability of boundarylessness are used, including for complete\nground-field extension.', 'Clarify the restricted base-change fact already used in the proof and explicitly required by the reviewer; no equality claim.')
replace('The self-audit, source-integrity checks, finite diagnostics, and two\ndocument compilations are evidence about the draft and its artifacts;\nthey are not formal verification or priority certification. The original\natom has status partial and candidate=false. The source appendix below\nis part of this authoritative argument; it is not replaced by references\nto earlier campaign arguments or review receipts.',
        r'''The complete authoritative argument, both canonical native notes,
all thirty-three embedded primary units, author audit and research limits
were read before publication. The independent Xean native Codex review
used \texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning and returned
PASS for this precise partial theorem. Its full report, all twenty-seven
premises and all forty passages were read; passage indices and exact
statement matches were checked. Frozen proof, source, status and
primary-body bindings accompany the review.

The primary-source quotations, with their complete supplied proofs,
remain in the accompanying frozen argument. The following harmless
source-display errata were already avoided by the mathematical proof:
graded commutativity has exponent $(p+q)(p'+q')$; the one-point cutoff
is one near the first point and zero near the second; the comparison in
CLD 5.10.1(a) is equality; the finite case in 13.3.3 has
$\dim_y(Y)=0$; pushed volume in 15.3.1 equals downstairs volume; and
11.4.1 uses the inverse image of $\operatorname{Int}(Y/X)$.
Raw frozen quotations are preserved unchanged. Relative-interior base
change is used only as preservation of interior points, as stated above.

The standalone source was opened in the native LaTeX editor for
compilation. Same-model review, finite diagnostics, source integrity and
compilation are not formal verification or priority certification.
The full original recognition problem remains open.''', 'Replace internal execution metadata with exact review provenance and separately disclose harmless source-display errata.')
start = source.index('\\subsection{Embedded primary-source')
end = source.index('\\end{document}', start)
replace(source[start:end], r'''\subsection{Sources and accompanying material}

The accompanying complete frozen argument embeds the essential primary
units from Chambert-Loir and Ducros, \emph{Formes diff\'erentielles
r\'eelles et courants sur les espaces de Berkovich},
\url{https://arxiv.org/abs/1204.6277v2}; Ducros,
\emph{Espaces de Berkovich, polytopes, squelettes et th\'eorie des
mod\`eles}, \url{https://arxiv.org/abs/1203.6498v3}; and Berkovich,
\emph{\'Etale cohomology for non-Archimedean analytic spaces},
Publ. Math. IHES 78 (1993). The independently checked CLD composition
statement supplies the boundary facts needed here. The exact imported
foundations A--G and every load-bearing new proof above remain in this
typeset paper. Primary quotations are retained in the frozen argument
rather than duplicated in this rendering.

''', 'Keep all quoted primary bodies in the full frozen argument bundle; preserve all foundations and supporting mathematical proofs in the paper.')
replace(r'\setmonofont[]{DejaVu Sans Mono}', '% Native editor uses its default monospaced font.', 'Remove platform-specific monospaced font selection.')
pattern = r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    m = re.fullmatch(pattern, token)
    replace(token, '\\'+m.group(1)+'{'+m.group(2)+'}', 'Explicit math-alphabet grouping for native unicode-math.', source.count(token))
pattern = r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern, source)):
    replace(token, token[0]+'{'+token[1:]+'}', 'Explicit script grouping for native unicode-math.', source.count(token))
out.mkdir(exist_ok=False)
tex = out/'P06.2-finite-galois-all-dimensional-ascent.tex'
tex.write_text(source)
(review/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record = {'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'tex':str(tex),'sha256':sha(tex),'governing_review':str(review),
          'publication_edits_sha256':sha(review/'publication-edits.json'),
          'native_compilation_pending':True}
(root/'deliverables/round-21-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
