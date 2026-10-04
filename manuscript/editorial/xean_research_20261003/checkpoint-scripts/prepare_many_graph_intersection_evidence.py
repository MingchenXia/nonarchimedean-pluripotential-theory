"""Fresh future evidence; no in-flight worker or review is changed."""
from pathlib import Path
import datetime,hashlib,json,re
r=Path('/workspace/research');s=r/'shared-sources/many-graph-product-intersection-20261004';src=s/'Allermann-Rau-0709.3705.txt';raw=src.read_text();start=re.search(r'^Definition 3\.1 \(Rational functions\)',raw,re.M);end=re.search(r'^Definition 3\.8 \(Affine Cartier divisors\)',raw,re.M);assert start and end and end.start()>start.start();body=raw[start.start():end.start()]
p=r/'P05.2-many-graph-intersection-primary-evidence.md';assert not p.exists()
p.write_text(r'''# Fallible evidence for the future many-graph product step

Prepared after both current P05/P06 campaigns were admitted; neither live
input nor review is changed. No new theorem is accepted.

Primary source: Lars Allermann and Johannes Rau, First Steps in Tropical
Intersection Theory, arXiv:0709.3705v3, PDF header20January2009; journal DOI
10.1007/s00209-009-0483-1. The official abstract page identifies both authors,
title and DOI. Source retrieval metadata is retained alongside the PDF.
The source works with INTEGER cycle weights and integral-slope rational
functions, with real additive constants. The exact real scalar extension
under discussion requires a separate argument; a source statement alone
does not grant that extension or the many-factor envelope theorem.

The root read Definition3.1 through Proposition3.7 in full, including the
normal, refinement, balancing and commutativity proofs. The whole selected
unit is reproduced below. Only formfeeds are replaced by newlines for display;
source bytes, LF ranges and body hashes remain bound separately.

## Proposed all-dimensional reconstruction, not an accepted lemma

At a codimension-two face theta of a k-cycle, translate the germ to zero,
subtract an ambient REAL affine extension of the common tangent linear part
of each function, and quotient by span(theta) with lattice N/N_theta.
N_theta is saturated, and each image N_sigma/N_theta remains saturated in
the ambient quotient: if a positive multiple of a class has a lift in
N_sigma, saturation of N_sigma puts that lift itself in N_sigma.
Thus primitive quotient normals and all plane indices are retained exactly.
The incident germ becomes a balanced two-dimensional fan. Additional
rational cuts make its two-cones pointed. For primitive rays r,s of each
cone, top weight omega_rs and chi_rs=[N_cone:Zr+Zs], balancing gives

    sum_{s adjacent to r} (omega_rs/chi_rs) s = t_r r,
    D_h(r) = sum_s (omega_rs/chi_rs) h(s) - t_r h(r).

Sum D_h(r)r over all rays. In the first sum each unordered cone contributes
omega_rs (h(s)r+h(r)s)/chi_rs. Substituting the top balancing identities
in the second sum gives exactly the same contributions. The sum is zero.
This proves balancing of the first divisor at the chosen theta. Since theta
was arbitrary, the actual (k-1)-cycle is balanced globally, subject to the
localization/refinement facts which must themselves be proved.

With first-divisor balancing established, subtracting an ambient affine
function from the outer slot changes no divisor. The full second coefficient
in the quotient is

    sum_{unordered {r,s}} (omega_rs/chi_rs)
          [h(s)g(r)+h(r)g(s)] - sum_r t_r h(r)g(r).

Both terms are symmetric. Retain the tangential term explicitly; do not
substitute a shorter printed formula without verifying its cancellation.
This proves the proposed mixed commutativity at theta and, by all faces,
globally. Together with direct normal-lift independence and the three
minimal-old-face cases for refinement, this appears to reconstruct the
all-k recursion needed by the new product step using elementary fan algebra.
This remains a FALLIBLE proposed proof requiring an independent audit.

For coefficient extension one can separately use the finite rational
homogeneous continuity equations for affine pieces on a fixed rational
complex and the finite rational balancing equations for cycle weights.
Choose rational bases and clear denominators; real functions/weights are
finite real linear combinations of permitted integral data. Bilinearity
extends identities, not positivity. Positivity against all ordinary-open
REAL nonnegative local cycles needs the independent genuine-PCC argument
and rational generation of its balanced nonnegative cone. Do not infer it
from arbitrary signed basis expansion.

The factor intersection rule, compact raw-envelope pinning, complete
contact integral, positivity and every neighborhood quantifier in
P05.2-finite-many-graph-product-proposal.md remain separate obligations.
Hash/source correctness does not prove any new application.

## Complete selected primary statement/proof unit

```text
'''+body.replace('\f','\n').rstrip()+'\n```\n')
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
m={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(p),'sha256':sha(p),'source_pdf':str(s/'Allermann-Rau-0709.3705.pdf'),'source_pdf_sha256':sha(s/'Allermann-Rau-0709.3705.pdf'),'source_text':str(src),'source_text_sha256':sha(src),'selected_first_LF_line':raw[:start.start()].count('\n')+1,'selected_last_LF_line':raw[:end.start()].count('\n'),'selected_body_sha256':hashlib.sha256(body.encode()).hexdigest(),'full_selected_definition_and_proofs_read':True,'source_scope_integer_cycles_integral_slopes':True,'no_live_input_changed':True,'no_new_theorem_accepted':True}
(s/'root-primary-read-and-evidence.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m,indent=2))
