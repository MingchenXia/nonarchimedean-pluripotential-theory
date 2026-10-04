"""Prepare exactly the accepted fixed-reference theorem for the native editor."""
from pathlib import Path
import datetime,hashlib,json,re

root=Path('/workspace/research')
d=root/'campaigns/round-18/P05.2-fixed-rational-reference-review'
out=root/'deliverables/round-19'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((d/'run.json').read_text())['campaign']['result']
f=json.loads((d/'freeze.json').read_text())
b=json.loads((d/'source-artifact-binding.json').read_text())
a=json.loads((d/'review-read-attestation.json').read_text())
assert r['verdict']=='PASS' and not r['premises'] and not r['passages']
assert a['publish_exact_scope'] and a['root_full_main_and_all_canonical_notes_read']
assert a['run_sha256']==sha(d/'run.json') and sha(d/'argument.md')==f['argument_sha256']
for p,k in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(b[p]))==b[k]==f[k]
source=Path(b['source_tex']).read_text()
edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after)
    edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})

replace('Unverified P05.2 partial proof draft','Xean research manuscript','Publication metadata.',2)
replace('Fixed-reference theorem (unverified draft).','Fixed-reference theorem.','Exact partial theorem passed independent review.')
replace('Accordingly this result has status\n\\textbf{partial}, candidate \\textbf{false}.','This is a reviewed partial theorem.','Replace author draft metadata; original-scope limitations retained.')
replace('The complete result is an unverified mathematical\ndraft, not a certified theorem.','The exact partial theorem has passed an independent Xean review.','Replace obsolete review status; review limitations recorded below.')
replace('the tangential correction in (36) subtracts','the tangential correction in (5)--(6), together with (44), subtracts','Harmless cross-reference correction explicitly requested by the reviewer.')
start=source.index('\\subsection{Author audit, source and execution')
end=source.index('Bibliography:',start)
replace(source[start:end],r'''\subsection{Review and reproducibility}

The complete frozen argument contains every load-bearing polyhedral,
graph, rational-domain, intersection and contact proof, together with
the exact source definitions. The Xean native Codex independent review
used \texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning and returned PASS
for this exact fixed-rational-reference characterization, with no
essential external theorem premises. The full review and immutable
argument, manuscript and status bindings were read and checked. Its
single harmless equation-reference correction is applied above and
recorded in the accompanying receipt.

The root read the complete argument, both canonical native notes,
author audit, research limits and finite diagnostic program. The two
specified local examples were recomputed in a new directory, preserving
the original artifacts. All forty-nine saturated plane indices were
also checked independently by greatest common divisors of ambient
two-by-two minors. The sample scaling gives \(8/49\) for
\(\varepsilon=1/7\). These are local arithmetic diagnostics only; the
whole-space envelope and complete integral are established by the
proof above.

The full frozen argument and source definitions, standalone source,
PDF, review receipt and finite diagnostic packet accompany the paper.
This standalone source was opened in the native editor for compilation.
Same-model review, file bindings, computation and typesetting are not
formal verification or priority certification. The original arbitrary
balanced-pair classification and the negative extension to every real
reference remain open.

''','Replace author execution instructions with exact review and reproducibility provenance.')
start=source.index('\\subsection{Exact essential source definitions, for reviewer')
end=source.index('\\end{document}',start)
replace(source[start:end],r'''The exact defining source quotations are retained in full in the
accompanying frozen argument. Their removal from this typeset copy
does not remove any supporting proof above.

''','Keep full quoted-definition appendix in frozen argument bundle; typeset paper retains all supporting mathematics.')
replace(r'\setmonofont[]{DejaVu Sans Mono}',r'% Native editor uses its default monospaced font.','Remove unused platform-specific font selection after definition appendix removal.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token)
    replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit math-alphabet grouping for native unicode-math.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit script grouping for native unicode-math.',source.count(token))
out.mkdir(exist_ok=False)
tex=out/'P05.2-fixed-rational-reference-graph-products.tex'
tex.write_text(source)
(d/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'tex':str(tex),'sha256':sha(tex),'governing_review':str(d),
 'publication_edits_sha256':sha(d/'publication-edits.json'),'native_compilation_pending':True}
(root/'deliverables/round-19-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
