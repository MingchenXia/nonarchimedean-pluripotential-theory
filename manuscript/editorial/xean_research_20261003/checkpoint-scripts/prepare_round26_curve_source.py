"""Prepare the reviewed recognition-only curve paper without mathematical repairs."""
from pathlib import Path
import datetime,hashlib,json,re
r=Path('/workspace/research');d=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
out=r/'deliverables/round-26';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
att=json.loads((d/'review-read-attestation.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text())
assert att['verdict']=='PASS' and att['publish_exact_scope'] and att['run_sha256']==sha(d/'run.json')
source=Path(b['source_tex']).read_text();assert sha(Path(b['source_tex']))==b['source_tex_sha256'];edits=[]
def replace(before,after,reason,count=1):
    global source
    assert source.count(before)==count,(before,source.count(before))
    source=source.replace(before,after);edits.append({'before':before,'after':after,'expected_occurrences':count,'reason':reason})
replace('P06.2 integration research draft','Xean research manuscript','Publication metadata.',2)
start=source.index('This document gives a complete integration argument')
end=source.index('All spaces are actual Berkovich analytic spaces',start)
replace(source[start:end],r'''This paper proves the arbitrary-field intrinsic curve recognition theorem
using the exact supporting proofs for completed-algebraic current transport
and algebraically closed intrinsic curve recognition, and precisely stated
published foundations. The new integration passed an independent Xean
review. Its full frozen argument retains both complete supporting bodies
and the primary quotations. Original P06.2 remains open in arbitrary
dimension; the theorem below covers dimension one.

''','Replace obsolete draft bookkeeping while preserving exact special scope.')
start=source.index('\\subsection{Evidence, author audit, and')
end=source.index('\\subsection{References}',start)
replace(source[start:end],r'''\subsection{Review and supporting evidence}

The independent Xean native Codex review used \texttt{gpt-6.1-sol} with
\texttt{xhigh} reasoning. Its full report, forty-three premises and
seventy-five primary-source passages were read and bound to the unchanged
new argument, source and partial status. The review reconstructed the
supporting proofs and accepted the new integration at precisely its stated
curve scope. Historical verdicts are not premises of the new theorem.

The new argument, all three actual canonical native notes and all sixteen
selected new primary bodies were read. All twenty-three source and support
copies were checked against unchanged origins. Both complete supporting
arguments were matched to their previously fully read, exactly reviewed
bytes; the authoritative transport main and its distinct published wrapper
remain separately bound. The companion argument contains the whole chain,
including finite extensions, completed-algebraic compact-test descent,
actual componentwise purity and calibrations, reduction, closed-curve
restriction, normalization and intrinsic curve recognition.

For version clarity, the GJR results cited inside GR Proposition 3.15
as Lemma 5.3(3) and Corollary 5.11 are Lemma 5.4(3) and Corollary 5.12
in GJR v3. In the supporting curve-image proof, the quotient \(A/I\)
is a strict affinoid integral algebra defining a closed analytic subspace;
it is not asserted to define an analytic domain. The original quotation
bytes, including transcription defects, are retained in the companion
evidence. The precise statements and reconstructed applications above
govern the mathematics.

The packet includes the source, PDF, complete frozen proof and supporting
bodies, full new review, source provenance, canonical notes and read records.
Native editor compilation and local PDF exports are recorded separately.
Same-model review, compilation and file integrity are not formal verification
or priority certification. No ordinary-smooth approximation theorem or
arbitrary-dimensional recognition theorem is claimed.

''','Replace execution appendix with completed review provenance, exact harmless terminology and version corrections. All mathematical argument preceding this metadata remains intact.')
pattern=r'\\(mathbb|mathcal|mathbf|mathrm)\s*([A-Za-z])(?![A-Za-z])'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    m=re.fullmatch(pattern,token);replace(token,'\\'+m.group(1)+'{'+m.group(2)+'}','Explicit native math-alphabet grouping.',source.count(token))
pattern=r'([_^])\\(mathbb|mathcal|mathbf|mathrm)\{([A-Za-z])\}'
for token in dict.fromkeys(m.group(0) for m in re.finditer(pattern,source)):
    replace(token,token[0]+'{'+token[1:]+'}','Explicit native script grouping.',source.count(token))
out.mkdir(exist_ok=False);tex=out/'P06.2-arbitrary-field-curve-recognition.tex';tex.write_text(source)
p=d/'publication-edits.json';assert not p.exists();p.write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(tex),'sha256':sha(tex),
 'governing_review':str(d),'publication_edits_sha256':sha(p),'native_compilation_pending':True,'full_original_atom_solved':False}
(r/'deliverables/round-26-source-preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
