"""Prepare native-editor paper only after the exact review is accepted and read."""
from pathlib import Path
import datetime,hashlib,json,re
root=Path('/workspace/research');review=root/'campaigns/round-22/P05.2-arbitrary-graph-product-review';out=root/'deliverables/round-23'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((review/'run.json').read_text())['campaign']['result'];freeze=json.loads((review/'freeze.json').read_text());binding=json.loads((review/'source-artifact-binding.json').read_text());att=json.loads((review/'review-read-attestation.json').read_text())
assert result['verdict']=='PASS' and att['publish_exact_scope'] and att['root_full_main_and_all_canonical_notes_read']
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read'))
assert att['run_sha256']==sha(review/'run.json') and sha(review/'argument.md')==freeze['argument_sha256']
for key,hkey in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:assert sha(Path(binding[key]))==binding[hkey]==freeze[hkey]
source=Path(binding['source_tex']).read_text();edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before));source=source.replace(before,after);edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})
replace('Unverified P05.2 partial proof draft','Xean research manuscript','Publication metadata.',2)
replace('Theorem (unverified broader special-case proof).','Finite two-graph theorem.','Exact-scope independent review has been read and accepted.')
replace('This is a substantial special case of the original P05.2, with status\n\\textbf{partial} and candidate \\textbf{false}.','This is a reviewed partial theorem toward the original P05.2.','Replace internal author draft metadata; original scope stays open.')
replace('All results are unverified drafts. Same-model\nauthor audit, compilation and finite arithmetic diagnostics do not\nestablish mathematical correctness or priority.','The exact partial theorem has passed an independent Xean review.\nSame-model review, computation and compilation are not formal\nverification or priority certification.','Replace obsolete draft status, retain review limits.')
replace('B=\\max\\bigl(0,\\ \\max_{\\sigma\\in\\Sigma}',
        'B_{\\eta}=\\max\\bigl(0,\\ \\max_{\\sigma\\in\\Sigma}',
        'Reviewer harmless notation correction: coercivity constant is separate from graph vertex B.')
replace('\\eta\\geq m\\rho-B.', '\\eta\\geq m\\rho-B_{\\eta}.',
        'Same coercivity constant notation in (31), without changing the inequality.')
replace('quotient normals, so cancel. If its dimension equals the tested facet',
        'quotient normals, so cancel; any additional incident pieces have zero\ninherited weight. If its dimension equals the tested facet',
        'Reviewer harmless clarification of refinement cancellation.')
start=source.index('\\subsection{Author audit, source boundaries and');end=source.index('Bibliography:',start)
replace(source[start:end],r'''\subsection{Review and reproducibility}

The complete frozen argument reconstructs the finite rational cone of
actual polyhedral convex functions, exact positive-growth decomposition,
intrinsic graph convexity, product projection, full cylinder contact proof,
rank-one two-branch obstruction and new higher-relation obstruction.
All these mathematical proofs are retained above. The independent Xean
native Codex review used \texttt{gpt-6.1-sol} with \texttt{xhigh}
reasoning. Its complete report, premises and passages were read and
bound to the exact immutable argument, manuscript and status.

The root directly read all new proof and source-comparison text,
including the complete existing one-dimensional dossier, and all three
canonical native notes. Every reused argument portion was checked for
exact text equality to the previously fully read parent proof.
Each new application was assessed; previous verdicts supplied no
supporting theorem grant. All fourteen source snapshots were rebound
to their unchanged origins.

The three specified higher-relation local-fan arithmetic examples were
recomputed in a fresh directory and matched the retained exact outputs.
An independent cross-times-line calculation enumerates nineteen merged
plane vertices for one explicit obstacle, with total mass sixteen and
complete contact integral minus one half. These computations check
specified examples; the universal envelope and complete integral claims
rest on the mathematical proofs above.

The complete frozen argument, exact source definitions and comparison
bodies, standalone source, PDF, independent review and diagnostic packet
accompany the paper. The standalone source was opened in the native
LaTeX editor for compilation. Same-model review, file bindings,
computation and typesetting are not formal verification or priority
certification. The original arbitrary balanced-space classification
remains open.

''','Replace execution metadata with exact review and reproducibility provenance; all preceding supporting mathematics retained.')
start=source.index('\\subsection{Exact essential source definitions, for reviewer');end=source.index('\\end{document}',start)
replace(source[start:end],r'''The exact defining source quotations, inspected comparison proof
bodies and existing one-dimensional dossier are retained in full in the
accompanying frozen argument. Every load-bearing supporting mathematical
proof above is retained in this typeset copy.

Quotation erratum: the flattened multiplier in the companion comparison
extract of BMPS Lemma~3.4 is \(S/\varepsilon\), multiplying its weighted
Jensen difference. The frozen raw quotation is preserved; the direct
PC-to-PAPC proof above is unchanged.


''','Quoted/comparison appendices remain in the frozen argument bundle; no supporting proof is removed.')
replace(r'\setmonofont[]{DejaVu Sans Mono}',r'% Native editor uses its default monospaced font.','Remove platform-specific font selection without installation.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token);replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit math-alphabet grouping for native unicode-math.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):replace(token,token[0]+'{'+token[1:]+'}','Explicit script grouping for native unicode-math.',source.count(token))
out.mkdir(exist_ok=False);tex=out/'P05.2-arbitrary-finite-graph-products.tex';tex.write_text(source)
(review/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(tex),'sha256':sha(tex),'governing_review':str(review),'publication_edits_sha256':sha(review/'publication-edits.json'),'native_compilation_pending':True}
(root/'deliverables/round-23-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
