"""Publish a standalone rendering only after reading and binding exact PASS."""
from pathlib import Path
import datetime,hashlib,json,re
r=Path('/workspace/research');d=r/'campaigns/round-24/P05.2-finitely-many-graph-products-review';out=r/'deliverables/round-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j=json.loads((d/'run.json').read_text());result=j['campaign']['result']
f=json.loads((d/'freeze.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text());a=json.loads((d/'review-read-attestation.json').read_text())
assert j['campaign']['status']=='completed' and result['verdict']=='PASS' and a['publish_exact_scope']
assert all(a[k] for k in ('full_report_read','all_premises_read','all_passages_read','root_full_main_and_all_canonical_notes_read'))
assert a['run_sha256']==sha(d/'run.json') and a['freeze_sha256']==sha(d/'freeze.json')
for k,h in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:assert sha(Path(b[k]))==b[h]==f[h]
source=Path(b['source_tex']).read_text();edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after);edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})
replace('P05.2 unverified partial proof draft','Xean research manuscript','Publication metadata.',2)
replace('Theorem (unverified finite-product classification).','Finite-product classification theorem.','Exact-scope independent review accepted.')
start=source.index('This closes only the specified finite-product family')
end=source.index('\\subsection{Recursive intersection',start)
replace(source[start:end],r'''This theorem classifies the specified finite-product family in the
declared real coefficient category. The original P05.2 classification
on arbitrary balanced carriers remains open. Literal integral-slope
coefficients, analytic realization, general singular-fan contact and
P06.2 are outside the theorem's scope. The complete original task,
frozen argument, supporting proofs, exact primary quotations and
independent review accompany this manuscript.

''','Replace internal execution metadata while retaining every scope limitation.')
start=source.index('There is no intentionally unresolved step within this claimed')
end=source.index('\\section{Complete elementary supporting',start)
replace(source[start:end],r'''The exact finite-product theorem has passed an independent Xean
review. All supporting mathematical proofs are retained below. Source
quotations and comparison dossiers accompany the complete frozen
argument. Same-model review, finite arithmetic, compilation and file
integrity are not formal verification or priority certification.

''','Replace obsolete draft status; supporting mathematical proofs unchanged.')
needle='its predecessor.\n\n\\subsection{Elementary polyhedral and convex'
replace(needle,r'''its predecessor.

For the inherited labels in this reconstruction, (1) denotes the sole
positive rank-one star relation, (2) denotes contact identity (C),
(3) denotes raw-envelope definition (E), and (5) denotes the full
divisor formula (D). These are aliases for the same formulas above.

\subsection{Elementary polyhedral and convex''','Reviewer harmless correction of inherited internal equation aliases.')
replace('the tangential correction in (5)--(6), with','the tangential correction in (D), with','Point to the complete divisor formula used in the calculation.')
replace('By (35) the local germ of \\(P-P(o)\\) is \\(\\varepsilon H\\). Constants',
        'By (J) the local germ of \\(P-P(o)\\) is \\(\\kappa H\\). Constants',
        'Reviewer harmless reference correction and explicit scale identification.')
replace('=8\\varepsilon^2ab.          \\tag{47}', '=8\\kappa^2ab.          \\tag{47}',
        'Same scale identification in the unchanged mass formula.')
start=source.index('\\section{Essential primary source definitions and complete selected')
end=source.index('\\end{document}',start)
replace(source[start:end],r'''\section{Review, sources and reproducibility}

The independent Xean native Codex review used
\texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning. Its full report was
read and bound to the exact immutable argument, manuscript and partial
status. The verdict covers this finite graph-product family. No
completion of the original arbitrary balanced-carrier problem is
claimed.

All new proofs and all three canonical native notes were read. Every
reused primary or comparison passage was checked for exact equality
with previously fully read text; all remaining lines were read directly.
All nineteen source snapshots were checked against their unchanged
origins, and all twelve selected raw source bodies were checked against
their exact inclusive LF coordinates and displayed copies.

The accompanying frozen argument retains the complete primary source
quotations and the existing one-dimensional comparison dossier. They
are comparison evidence. The complete mathematical dependency chain
is reconstructed in this manuscript; prior reviews are not theorem
premises. Integral source coefficients and the declared real extension
are distinguished throughout.

The four local recursive computations in dimensions three and five
were rerun from a fresh copy and matched the retained exact outputs.
Their full masses are \(64/49\), \(576000/26411\), \(64/567\), and
\(6400/6561\). They test specified local germs, all successive divisor
stages, all surviving orders and an exhausted repeated factor. They
do not enumerate global envelopes or prove universal contact integrals.
Those conclusions rest on the proofs above.

The packet contains the standalone source and PDF, complete frozen
argument, exact independent review, source provenance, and full finite
diagnostic program, input and output. Native editor verification and
local PDF export results are recorded separately. Same-model review,
typesetting and arithmetic are not formal verification or priority
certification.

\begin{thebibliography}{9}
\bibitem{BMPS}
A.~M.~Botero, E.~Mazzon and L.~Pille--Schneider,
\emph{Monge--Amp\`ere measures on balanced polyhedral spaces},
arXiv:2603.08664v1 (2026),
\url{https://arxiv.org/abs/2603.08664v1}.
\bibitem{AR}
L.~Allermann and J.~Rau,
\emph{First steps in tropical intersection theory},
arXiv:0709.3705v3 (2009),
\url{https://arxiv.org/abs/0709.3705v3};
\emph{Math.~Z.} \textbf{264} (2010), 633--670.
\end{thebibliography}

''','Primary/comparison/execution appendices retained in complete companion argument; all preceding supporting mathematics retained in the paper.')
replace(r'\setmonofont[]{DejaVu Sans Mono}',r'% Native editor uses its default monospaced font.','Remove platform-specific font dependency.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token);replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit math-alphabet grouping for native unicode-math.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit script grouping for native unicode-math.',source.count(token))
out.mkdir(exist_ok=False);tex=out/'P05.2-finitely-many-graph-products.tex';tex.write_text(source)
assert not (d/'publication-edits.json').exists()
(d/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(tex),'sha256':sha(tex),'governing_review':str(d),'publication_edits_sha256':sha(d/'publication-edits.json'),'native_compilation_pending':True,'full_original_atom_solved':False}
(r/'deliverables/round-24-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
