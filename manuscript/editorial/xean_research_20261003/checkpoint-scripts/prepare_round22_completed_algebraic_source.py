"""Prepare only the read-and-bound completed-algebraic partial theorem."""
from pathlib import Path
import datetime,hashlib,json,re

root=Path('/workspace/research');review=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-review'
out=root/'deliverables/round-22';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((review/'run.json').read_text())['campaign']['result']
att=json.loads((review/'review-read-attestation.json').read_text())
freeze=json.loads((review/'freeze.json').read_text());binding=json.loads((review/'source-artifact-binding.json').read_text())
assert result['verdict']=='PASS' and att['publish_exact_scope']
assert all(att[k] for k in ('full_report_read','all_premises_read','all_passages_read','root_full_main_and_all_canonical_notes_read'))
assert sha(review/'run.json')==att['run_sha256'] and sha(review/'argument.md')==freeze['argument_sha256']
for k,h in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(binding[k]))==freeze[h]==binding[h]
source=Path(binding['source_tex']).read_text();edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after)
    edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})

replace('Unverified research draft, 4 October 2026. This is a partial result for\nthe original P06.2 recognition problem. An author audit, source\nextraction, or a successful compilation is not mathematical\nverification.',
        'Reviewed partial theorem, 4 October 2026. This is partial progress on\nthe original P06.2 recognition problem. Independent same-model review,\nsource integrity, finite diagnostics and compilation are not formal\nverification or priority certification.', 'Publication metadata after the exact-scope independent review.')
before=source[source.index('Let K be a complete nontrivially valued'):source.index('\\textbf{Theorem B (the new gate).}')]
after=r'''Let \(K\) be a complete nontrivially valued non-Archimedean field,
let \(M/K\) be an algebraic valued extension, and let \(L\) be its
completion. All finite stages are actual embedded fields
\(K\subseteq E\subseteq M\), complete with their prescribed absolute
values. Write \(p_E:X_E\to X\), \(q_E:X_L\to X_E\), and
\(\pi:X_L\to X\). Scalar extensions use actual completed affinoid algebras.

\textbf{Theorem A (exact compact tests).} If \(X\) is good, separated
and strict, then for every pair of nonnegative integers \((a,b)\) and
every ordinary CLD form \(\beta\in A_c^{a,b}(X_L)\), there are one
finite \(E\subseteq M\) and \(\alpha_E\in A_c^{a,b}(X_E)\) such that
\(\beta=q_E^*\alpha_E\) as smooth sections. Consequently both
differentials, their compositions and exterior products with pulled-back
sections respect this identity. No dimension, boundarylessness or
positivity is required. This is descent of a compact smooth form, rather
than of an arbitrary analytic function or an arbitrary upstairs space
presentation.

'''
replace(before,after,'Typeset the unchanged field conventions and Theorem A as mathematical notation.')
replace("interior Int(V). Set D=d'd'\\,' and t\\_f=−log\\textbar f\\textbar{} for an\nanalytic unit.",
        r"interior \(\operatorname{Int}(V)\). Set \(D=d'd''\) and \(t_f=-\log|f|\) for an analytic unit.",
        'Correct prose math typesetting to match the unchanged authoritative definitions.')
start=source.index('\\subsection{11. Audit and reproduction')
end=source.index('\\subsection{Embedded primary-source',start)
replace(source[start:end],r'''\subsection{11. Review, source boundaries and reproducibility}

The complete new mathematical core, both canonical native notes, author
audit and research limits were read before publication. All thirty-three
primary bodies were checked byte for byte against authentic origins and
the identical previously fully read bodies; this was exact source reuse,
rather than a new fresh reading of the entire quotation appendix.
Every new application was assessed in the present proof. The independent
Xean native Codex review used \texttt{gpt-6.1-sol} with \texttt{xhigh}
reasoning and returned PASS for Theorems A and B. The complete report,
all twenty-three premises and all thirty-two passages were read and
their exact indices, statements and immutable proof bindings checked.

The complete quoted primary units and their printed proofs remain in
the accompanying frozen argument. Source-internal references remain
normal primary references; this paper imports the exact stated analytic
foundations, rather than claiming to reprove their entire underlying
theories. The reviewer verified the essential CLD and published Ducros
sources independently. CLD's composition statement supplies the needed
boundary facts; the additional Berkovich citation adds no indispensable
premise. Base change preserves interior points; no unrestricted equality
of relative interiors is used.

Harmless source-display corrections, already avoided by this proof,
are recorded separately: graded commutativity uses
\((p+q)(p'+q')\); rational localization retains its ambient algebra;
relative-interior composition uses \(g^{-1}(\operatorname{Int}(Y/X))\);
the Artinian case has \(\dim_y(Y)=0\); the target volume in scalar
projection is downstairs volume; CLD 5.10.1(a)'s comparison is equality;
and the cutoff has the correct values near the two function images,
with its neighborhood inside a point-separating open. Section 3.4 supplies
that cutoff proof independently. Frozen raw quotations are unchanged.

The small rational-norm, exterior-basis and unreduced-algebra diagnostics
are finite reproducibility evidence. They do not prove the analytic
theorems. The standalone source was submitted to the native LaTeX editor
for compilation. Same-model review, computation and compilation are
not formal verification or priority certification. Original classical
recognition and the further bridges explicitly excluded above remain open.

''','Replace internal execution metadata with exact review provenance and harmless source-display errata; preserve all mathematical proofs in Sections1--10.')
start=source.index('\\subsection{Embedded primary-source')
end=source.index('\\end{document}',start)
replace(source[start:end],r'''\subsection{Primary sources and accompanying argument}

Chambert-Loir and Ducros, \emph{Formes diff\'erentielles r\'eelles et
courants sur les espaces de Berkovich},
\url{https://arxiv.org/abs/1204.6277v2}; Ducros,
\emph{Espaces de Berkovich, polytopes, squelettes et th\'eorie des
mod\`eles}, Confluentes Math. 4 (2012), 1250007,
\url{https://www.numdam.org/item/10.1142/S1793744212500077/};
Berkovich, \emph{\'Etale cohomology for non-Archimedean analytic spaces},
Publ. Math. IHES 78 (1993), 5--161.

The accompanying frozen argument retains all thirty-three full selected
primary bodies. Every load-bearing supporting mathematical proof and
the exact imported foundations above are retained in this rendering.

''','Retain full quoted primary-source bodies in the frozen argument bundle, without duplicating the appendix in the paper.')
for family,font in [('main','DejaVu Serif'),('sans','DejaVu Sans'),('mono','DejaVu Sans Mono')]:
    replace('\\set'+family+'font[]{'+font+'}','% Native editor uses its default '+family+' font.','Remove a platform-specific font unavailable in the native editor; no installation.')
symbols={'Γ':r'\Gamma','α':r'\alpha','β':r'\beta','γ':r'\gamma','δ':r'\delta','ε':r'\varepsilon','ζ':r'\zeta','θ':r'\theta','λ':r'\lambda','μ':r'\mu','ξ':r'\xi','π':r'\pi','σ':r'\sigma','τ':r'\tau','χ':r'\chi','ψ':r'\psi','ω':r'\omega',
         '→':r'\to','↦':r'\mapsto','∈':r'\in','∉':r'\notin','∏':r'\prod','∑':r'\sum','−':'-','∘':r'\circ','∧':r'\wedge','∩':r'\cap','∫':r'\int','≠':r'\ne','≤':r'\le','≥':r'\ge','⊆':r'\subseteq','⊇':r'\supseteq','⊗':r'\otimes'}
for character,command in symbols.items():
    if character in source:
        replace(character,r'\ensuremath{'+command+'}','Render an unchanged Unicode mathematical symbol with its standard LaTeX command in text and math contexts.',source.count(character))
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    match=re.fullmatch(pattern,token)
    replace(token,'\\'+match.group(1)+'{'+match.group(2)+'}','Explicit math-alphabet grouping for native unicode-math.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit script grouping for native unicode-math.',source.count(token))
out.mkdir(exist_ok=False);tex=out/'P06.2-completed-algebraic-all-dimensional-transport.tex';tex.write_text(source)
(review/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(tex),'sha256':sha(tex),
        'governing_review':str(review),'publication_edits_sha256':sha(review/'publication-edits.json'),'native_compilation_pending':True}
(root/'deliverables/round-22-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
