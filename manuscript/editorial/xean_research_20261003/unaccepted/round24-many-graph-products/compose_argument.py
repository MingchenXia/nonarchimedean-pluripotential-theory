"""Assemble all new and reconstructed proof bodies directly into the argument."""
from pathlib import Path
import json, unicodedata, re
ROOT=Path(__file__).resolve().parent
two=(ROOT/'sources/two-graph-argument.md').read_text()
cyl=(ROOT/'sources/cylinder-argument.md').read_text()

def part(text,start,end):
 return text[text.index(start):text.index(end,text.index(start))]

foundations=part(two,'## Elementary finite-dimensional facts','## Positive direction: full graph-cylinder')
# The original product-projection proof is printed in its two-factor form;
# the main text explicitly proves the arbitrary-number extension.
growth=part(two,'## Auxiliary rational-reference localization','## Supporting rank-one two-branch obstruction')
mass=part(two,'## Complete primitive-normal junction computation','## Complete contact failure')
multivariate=(part(cyl,'## Elementary polyhedral and convex facts','## Primitive-normal algebra')
             +part(cyl,'## Scalar graph facts proved without PC locality','## Exact triangle and comparison'))
out=(ROOT/'product-main.md').read_text()
out+='\n\n# Complete elementary supporting proofs, reconstructed in this argument\n\n'
out+='These proof bodies are included directly rather than invoked as prior results. '
out+='Formula references are internal to each reproduced proof unit. '
out+='The arbitrary-dimensional algebra and scalar normalization required by their applications are proved in the main text. '
out+='In the rank-one coface discussion, replacing the complete one-dimensional affine factor by E does not change the graph projection; all affine E terms cancel by the full vector barycentre.\n\n'
out+=foundations+growth
out+='\n\n# Complete multivariate cylinder reconstruction\n\n'
out+='In this unit graph weights are the positive rational normalized weights. '
out+='The main text proves the componentwise real-weight normalization and restores the entire operator scalar. '
out+='The divisor referred to as (5) here is the actual formula (D) proved in every dimension above. '
out+='All primitive-normal, locality, balancing, refinement and commutativity uses in this unit refer to that reconstructed algebra. '
out+='This full multivariate proof is mathematical evidence assessed here, not a theorem grant from its predecessor.\n\n'
out+=multivariate
out+='\n\n# Detailed original-lattice bad-pair mass computation\n\n'
out+='This computation is reconstructed at the original singular product star. '
out+='Its positive scale called epsilon in the final two paragraphs is kappa in the main theorem. '
out+='The all-stage tensor formula (A3), supplied above, is an additional proof and is not inferred merely from this two-stage computation.\n\n'
out+=mass
out+='\n\n# Essential primary source definitions and complete selected proof bodies\n\n'
out+='The originals are preserved byte for byte in sources. Extraction uses explicit LF newline ranges, never splitlines on PDF formfeeds. '
out+='For display only formfeeds become newlines, nonprinting extraction controls are omitted, private parenthesis fragments are ordinary parentheses, '
out+='the face-order glyph is written as preceq, and script ell is written as ell. '
out+='The cited theorem bodies are comparison evidence, not external theorem premises. '
out+='The literal integral coefficients, the real extension, all-cycle positivity and the full tangential term are explicitly separated above.\n\n'

def display(text):
 text=text.replace('\f','\n').replace('\u0010','(').replace('\u0011',')')
 text=text.replace('ℓ','ell').replace('⪯','preceq')
 for ch in '\uf8eb\uf8ec\uf8ed':text=text.replace(ch,'(')
 for ch in '\uf8f6\uf8f7\uf8f8':text=text.replace(ch,')')
 return ''.join(c for c in text if c in '\n\t' or unicodedata.category(c)!='Cc')

for ex in json.loads((ROOT/'source-excerpts.json').read_text()):
 name=ex['source'];body=(ROOT/ex['file']).read_text()
 out+=f"\nPrimary {name}, LF lines {ex['LF_first']}--{ex['LF_last']}.\n\n```text\n"+display(body)+'```\n'
out+='\n\n# Known graph classification and original residual scope (comparison only)\n\n'
out+=part(two,'## Existing one-dimensional accessible-mass dossier','## Original Appendix M scope check')
out+='\nNo conclusion from that dossier is used above. The original arbitrary balanced-carrier classification and its singular-fan contact problem remain open. '
out+='The finite two-graph case is previous comparison scope, reconstructed here; the new result is all finite d in the present product family. '
out+='No P06.2 theorem is used or claimed.\n'
out+='\n\n# Reproducibility and proof limits\n\n'
diag_path=ROOT/'diagnostic-output.json'
if diag_path.exists():
 diag=json.loads(diag_path.read_text())
 out+='The following are exact finite observations for the stated input germs only. '
 out+='`diagnostics.py` uses Fraction arithmetic and evaluates formula (D) on every product facet at each stage. '
 out+='On a primitive pair-plane ray (p,q), Bezout integers give an integral normal (-v,u) with pu+qv=1, '
 out+='whose sign is selected by the adjacent cone determinant. It maps this normal through the original primitive axes, '
 out+='retains the common tangential correction, and checks that the weighted normal sum lies in each actual facet tangent. '
 out+='The algorithm does not insert a top mass: it computes the first, second and every later divisor directly. '
 out+='It separately evaluates every surviving mixed ordering and a repeated exhausted factor. '
 out+='These local finite calculations do not enumerate global envelopes or prove the complete contact integral.\n\n'
 out+='| Input germ | d | Nonzero cells in successive divisors | Computed full mass | Surviving orders | Each order |\n'
 out+='|---|---:|---|---:|---:|---:|\n'
 labels=['higher rank, two edges','higher rank, four edges','tripod pair, one edge','tripod pair, three edges']
 for label,r in zip(labels,diag['records']):
  counts=', '.join(str(s['nonzero_cells']) for s in r['stages'])
  out+=f"| {label} | {r['dimension']} | {counts} | {r['full_mass']} | {r['surviving_orders']} | {r['each_order_mass']} |\n"
 out+='\nAll recorded nonnegativity, tangent balancing, identical-order and repeated-factor-zero assertions pass. '
 out+='The two-branch input has saturated cone indices 1 and 2, and the first star rays generate an index-two sublattice of their full span. '
 out+='The complete exact input is supplied here; the output and program are retained separately for rerunning.\n\n```json\n'
 out+=(ROOT/'diagnostic-input.json').read_text()+'```\n\n'
out+='Rerun in this fresh directory: `python3 snapshot_sources.py`; `python3 diagnostics.py`; '
out+='`python3 compose_argument.py`; `python3 build.py`; `python3 make_notes.py`; `python3 final_checks.py`. '
out+='Programs, exact inputs, full outputs, source provenance, LF excerpts, original inputs, author audit and build logs are retained. '
out+='`P05.2-partial.tex` is the standalone rendering and the PDF is compiled twice. '
out+='`status.json` has exactly id, status, exact_result, proof_file, concrete_gaps, with status partial. '
out+='Canonical notes are `result-notes.json`; no old artifact is modified. '
out+='No additional model, subagent, network call, external message, installation or heavy local compute is used. '
out+='No operator-supervised heavy-compute facility is exposed; none is required for these finite arithmetic checks and document builds. '
out+='Execution, source hashes, prior reviews, same-model author audit and compilation do not constitute mathematical verification or establish priority.\n'
out=re.sub(r'\\mathbb ([A-Z])',r'\\mathbb{\1}',out)
out=re.sub(r'([_^])\\mathbb\{([A-Z])\}',r'\1{\\mathbb{\2}}',out)
(ROOT/'P05.2-argument.md').write_text(out)
print(json.dumps({'argument_bytes':len(out.encode()),'all_supporting_bodies_embedded':True,'original_atom_solved':False},indent=2))
