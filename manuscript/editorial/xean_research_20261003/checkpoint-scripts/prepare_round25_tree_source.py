"""Create a standalone rendering of the exact reviewed tree construction."""
from pathlib import Path
import datetime, hashlib, json, re
r=Path('/workspace/research')
d=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review'
out=r/'deliverables/round-25'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
att=json.loads((d/'review-read-attestation.json').read_text())
review=json.loads((d/'run.json').read_text())['campaign']['result']
b=json.loads((d/'source-artifact-binding.json').read_text())
assert review['verdict']=='PASS' and att['publish_exact_scope']
assert att['run_sha256']==sha(d/'run.json') and att['source_artifact_binding_sha256']==sha(d/'source-artifact-binding.json')
source=Path(b['source_tex']).read_text()
assert sha(Path(b['source_tex']))==b['source_tex_sha256']
edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after)
    edits.append({'before':before,'after':after,'reason':reason,'expected_occurrences':count})
replace('Unverified research draft for P06.2','Xean research manuscript','Publication metadata.')
replace('certification. All arguments below are author drafts.',
        'certification. The exact conditional construction passed an independent Xean review;\nthe full frozen argument and review accompany this manuscript.',
        'Replace obsolete author-draft metadata; preserve conditional scope.')
replace('IV, Theorem 1.3 and Corollary 1.4','IV, Theorem 1.3 and Example 1.3.3','Reviewer harmless citation correction.')
replace('I, Theorem 6.9]{Hart}','I, Corollary 6.10, following Theorem 6.9]{Hart}','Reviewer harmless citation correction.')
replace('Chapter IV, Theorem 1.3 and Corollary 1.4.','Chapter IV, Theorem 1.3 and Example 1.3.3.','Reviewer harmless bibliography correction.')
replace('Chapter I, Theorem 6.9, for projective completion of a nonsingular curve.',
        'Chapter I, Corollary 6.10 following Theorem 6.9, for the open projective completion.',
        'Reviewer harmless bibliography correction.')
replace('(\\cite[IV, 17.6]{EGA}, applied to the finite-presentation formal\ncharts)',
        '(\\cite[IV, 17.6]{EGA}; \\cite[I.5.3.11]{FK};\n\\cite[Tags 00UE and 0ALI]{Stacks}, applied to the finite-presentation\nformal charts)',
        'Clarify the standard formal-etale foundations explicitly checked by the reviewer; argument unchanged.')
replace('The substantive proposed advance is','The substantive construction is','Publication metadata.')
replace('construction. P05.2 is untouched. Candidate remains false.',
        'construction. The original arbitrary-dimensional P06.2 remains open.',
        'Retain scope and replace internal candidate bookkeeping.')
insert=r'''\paragraph{Review and supporting evidence.}
The independent Xean native Codex review used \texttt{gpt-6.1-sol}
with \texttt{xhigh} reasoning and accepted precisely this conditional
construction. Its full report, sixteen premises and twenty-six source
passages were read and bound to the unchanged argument, source and status.
The new proof, all three canonical native notes and all seventeen selected
primary bodies were read. A fresh-copy reproduction preserved the argument
and source bytes and compiled successfully. These checks support reviewability;
they are not formal verification or priority certification.

The source quotations and full mathematical argument accompany the paper.
In Thuillier's normalized residual-function statement, the residual divisor
and its orders are independent of the normalizing scalar; the residual
function can change by a nonzero residue-field scalar. This distinction
does not alter any slope or divisor calculation above. The supplied model,
tree and harmonic factorization remain hypotheses throughout.

'''
replace('\\begin{thebibliography}{9}',insert+'\\begin{thebibliography}{99}','Add exact review provenance and harmless scalar clarification.')
replace('\\bibitem{Hart}',r'''\bibitem{FK} K. Fujiwara and F. Kato,
\emph{Foundations of Rigid Geometry I}, arXiv:1308.4734,
Proposition I.5.3.11 (formal etale reduction criterion).
\bibitem{Stacks} The Stacks Project, Tags 00UE and 0ALI,
\url{https://stacks.math.columbia.edu/tag/00UE},
\url{https://stacks.math.columbia.edu/tag/0ALI}.
\bibitem{Hart}''','Bibliographic details for unchanged formal-etale foundations.')
replace(r'\texttt{5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719}',
        r'\nolinkurl{5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719}',
        'Allow long provenance hash to wrap.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token)
    replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit native math-alphabet grouping.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit native script grouping.',source.count(token))
out.mkdir(exist_ok=False)
tex=out/'P06.2-specified-semistable-tree-regularization.tex'
tex.write_text(source)
assert not (d/'publication-edits.json').exists()
(d/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'tex':str(tex),'sha256':sha(tex),'governing_review':str(d),
 'publication_edits_sha256':sha(d/'publication-edits.json'),
 'native_compilation_pending':True,'full_original_atom_solved':False}
(r/'deliverables/round-25-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
