"""Prepare a standalone paper only after the exact-scope review has been read and accepted."""
from pathlib import Path
import datetime,hashlib,json,re

root=Path('/workspace/research')
review=root/'campaigns/round-20/P05.2-fixed-real-reference-review'
output=root/'deliverables/round-20'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((review/'run.json').read_text())['campaign']['result']
freeze=json.loads((review/'freeze.json').read_text())
binding=json.loads((review/'source-artifact-binding.json').read_text())
attestation=json.loads((review/'review-read-attestation.json').read_text())
assert result['verdict']=='PASS'
assert attestation['publish_exact_scope'] and attestation['root_full_main_and_all_canonical_notes_read']
assert attestation['run_sha256']==sha(review/'run.json')
assert sha(review/'argument.md')==freeze['argument_sha256']
for key in ['main_argument','source_tex','declared_proof_file']:
    assert sha(Path(binding[key]))==binding[key+'_sha256']==freeze[key+'_sha256']
source=Path(binding['source_tex']).read_text()
edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after)
    edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})

replace('Unverified P05.2 partial proof draft','Xean research manuscript','Publication metadata.',2)
replace('Theorem (unverified new special-case proof).','Fixed-real-reference theorem.','Replace obsolete author-draft status after exact independent review.')
replace('This theorem is \\textbf{partial}, candidate \\textbf{false}: it does not','This is a reviewed partial theorem. It does not','Original scope remains open; remove internal candidate metadata.')
replace('All claims remain\nunverified drafts; source receipts, numerical checks and compilation are\nneither mathematical certification nor priority certification.','The exact partial theorem has passed an independent Xean review.\nSame-model review, computation and compilation are not formal\nverification or priority certification.','Replace obsolete draft status while retaining review limitations.')
start=source.index('\\subsection{Author audit, research, sources, and execution')
end=source.index('Bibliography:',start)
replace(source[start:end],r'''\subsection{Review and reproducibility}

The complete frozen argument reconstructs the finite rational cone of
actual polyhedral convex functions, the exact positive-growth convex
decomposition, the graph-cylinder contact proof, the global raw envelope,
and the full two-stage intersection calculation. The independent Xean
native Codex review used \texttt{gpt-6.1-sol} with \texttt{xhigh}
reasoning. Its complete report and exact argument, manuscript and status
bindings were read and checked before publication.

The root read the entire authoritative argument, both canonical native
notes, author audit and research limits. The exact quadratic-field
diagnostic was recomputed in a fresh directory, preserving the original
artifacts, and matched the retained output. It checks one convex
decomposition and its common rational sample-ray walls. The earlier
rational-reference diagnostics retain the actual saturated cone indices.
These computations do not establish the universal envelope or integral
theorem; those are proved above.

The complete frozen argument, authentic source definitions, standalone
source, PDF, independent review and reproducibility packet accompany the
paper. The standalone source was opened in the native LaTeX editor for
compilation. Same-model review, file bindings, computation and typesetting
are not formal verification or priority certification. The original
classification on arbitrary balanced spaces remains open.

''','Replace author execution metadata with exact review and reproducibility provenance; preserve all preceding mathematical proofs.')
start=source.index('\\subsection{Exact essential source definitions, for reviewer')
end=source.index('\\end{document}',start)
replace(source[start:end],r'''The exact defining source quotations remain in full in the accompanying
frozen argument. Every load-bearing supporting mathematical proof above
is retained in this typeset copy.

''','Retain the full quoted-definition appendix in the frozen argument bundle, without duplicating it in the paper.')
replace(r'\setmonofont[]{DejaVu Sans Mono}',r'% Native editor uses its default monospaced font.','Remove platform-specific monospaced font selection.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token)
    replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit math-alphabet grouping for native unicode-math.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit script grouping for native unicode-math.',source.count(token))
output.mkdir(exist_ok=False)
tex=output/'P05.2-fixed-real-reference-graph-products.tex'
tex.write_text(source)
(review/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'tex':str(tex),'sha256':sha(tex),'governing_review':str(review),
        'publication_edits_sha256':sha(review/'publication-edits.json'),
        'native_compilation_pending':True}
(root/'deliverables/round-20-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
