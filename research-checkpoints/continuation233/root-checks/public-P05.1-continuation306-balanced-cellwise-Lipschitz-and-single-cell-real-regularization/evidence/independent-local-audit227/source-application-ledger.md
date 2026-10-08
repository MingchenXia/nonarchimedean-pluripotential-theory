# Independent source-application ledger

Verdict: **PASS for the essential applications in unchanged new306, with explicit historical metadata errors retained**. This is not an unqualified approval of every old ledger sentence or evidence of an old reading act. Source ledgers, working papers and actual/saved author notes are proposals being checked. Only the four locally bound BMPS/BBGS primary files were used; nothing was fetched from their printed URLs. The proofs needed for the new mathematics are in `reconstructed-proof.md`.

## Exact primary bytes and coordinate convention

| Primary | Version | Bytes | SHA-256 |
|---|---|---:|---|
| BMPS PDF | Botero–Mazzon–Pille-Schneider, arXiv:2603.08664v1; submitted 9 March 2026, manuscript 10 March | 774717 | `5cf7e68ee9113f1dc813f9aefa5f9ca72cba02fc4fa688f1a61e4b7f0d1223e7` |
| BMPS text | Same bound version; 3209 literal LF bytes | 231317 | `c4475ad5cf4e8fce3eb6add155fdb81e352cbe079ca0d7646553f8a3e8ad9271` |
| BBGS PDF | Botero–Burgos Gil–Sombra, Math. Z. 301 (2022), 1631–1674; publisher version, 24 January 2022 | 696627 | `c2817a01e51ac3781e94005cb587c185ac7e6cc5fe654feda6c5341eaf6a5846` |
| BBGS text | Same bound publisher version; 2420 literal LF bytes | 148757 | `87f8f8d2d51e523c4ecf5f8429875da16994abbe74132ce05886d1782e90b635` |

Literal identifiers in the supplied originals are https://arxiv.org/pdf/2603.08664v1 and https://link.springer.com/content/pdf/10.1007/s00209-021-02869-6.pdf. They are identity metadata, not network accesses. Coordinates below use `bytes.split(b'\n')`, one-based inclusive source lines. Counts use `bytes.count(b'\n')`. Formfeeds are not newlines. PDF bytes were hashed; no complete PDF-pixel reading or text/PDF pixel identity is asserted.

## Entire immediate original units independently obtained

Every named theorem/proof unit in this table was obtained directly from the bound original text in bounded output, not from an author paraphrase. The broader ranges include neighboring definitions or complete units needed to specify the application. In particular, BBGS 3.15 was displayed through its final equality and proof-ending sentence at literal LF670.

| Original unit and actual displayed LF range | Formal hypotheses and conclusion | Application and audit result |
|---|---|---|
| BMPS 2.1–2.4, LF254–301 | Rational affine polyhedra, finite complexes/refinements and global embedding; tangent lattice uses span(sigma-sigma). | New306's fixed finite geometry. All closed faces are retained. Rational coefficients can be denominator-cleared without changing saturated lattices. PASS. |
| BMPS 2.18–2.31, 2.24, 2.33–2.35 vicinity, LF418–614 | Primitive inward quotient normals; BMPS 2.19/2.20 define **rational** weights/cycles; literal PA has integral tangent slopes and rational constants. Positive divisor uses the tangent-corrected primitive convention. The complete 2.34 proof handles inherited/new subdivision faces. | The original rational category is distinguished from actual real scalar extension and from actual positive real balancing. 2.35's delegated AR10 proof is not imported. New balance inheritance and covolume conversion are proved independently; the BBGS chain is separately read. PASS for these uses. |
| BMPS 3.1–3.9, LF689–847 | Printed PCC has rational endpoints, real coefficients in [0,1], and its center may be **real**. The common face may equal the cell. PA convexity/support/strictness discussion. | L0 uses only the rational-center subfamily and proves full feasible perspective density. No irrational center is made a rational vertex. Automatic PC continuity in 3.4, broad density consequences, and an external bipolar proof in 3.7 are not used. Explicit continuity of f is essential. PASS. |
| BMPS 3.14, LF886–894 | Actual gamma+O(1) growth class. | The actual reference is retained on X and on sigma; the full-hull Gamma is only an auxiliary. Upper-only raw envelope classes are compared explicitly to two-sided ones. PASS. |
| BMPS 3.22–3.23, LF1005–1034 | Uniform/decreasing approximation convention and its printed proof. | Only the approximation convention is used. The dyadic +4eta extraction is independently proved; no compactification/Dini or all-printed-PC equivalence is imported. PASS. |
| BMPS 4.15, LF1741–1747 | Strictly positive recession on each nonzero admitted cell recession direction. | C2 checks its actual ell premise; independently proves coercivity on ALL nonzero full-hull directions, including those outside rec(sigma). L's theorem does not assume this growth. No 4.13/4.16 operator theorem is used to fill a domain gap. PASS. |
| BMPS 6.2–6.9, LF2253–2358 | Actual raw upper-growth envelope, regularity and contact/operator-domain antecedents. Entire immediate statement/proof units, including 6.3/6.4 and 6.6–6.8, were displayed. | Definitions locate the original task. R230 is used only as its qualified whole completion grant. No automatic BMPS continuity/density, complete-affine/conical blanket regularity, or endpoint MA without genuine PA closure is inferred. PASS for the definitions and restricted consequences. |
| BBGS 2.1–2.3, LF196–242; 2.14–2.15, LF379–413 | Euclidean quasi-embedding/category and tangent metrics. | For the globally embedded geometry, x -> (x,1) gives the required horizontal tangents with their unchanged metric. Cellwise quasi-embedding is not converted to an arbitrary homeomorphic balanced atlas. PASS. |
| BBGS 3.1–3.9 and 3.6, LF443–533 (displayed within LF443–598) | Real continuous PA; real cycle weights including signed/zero; restriction/subdivision; product is negative inward-unit-normal derivative. | Actual weights may be real here. This is not the rational BMPS coefficient category, nor proof that an arbitrary real-height max has rational spatial walls. The negative sign is retained in the calibration. PASS. |
| BBGS 3.12, entire LF533–598 | Restriction and subdivision commute with product, including all three relative-dimensional cases. New equal opposite facets cancel; lower strata in a larger old cell give zero. | Valid on every fixed/common carrying subdivision under the stated metric. It supplies no high-dimensional PA approximation/gluing theorem. New L balance inheritance is also checked directly. PASS. |
| BBGS 3.15, entire LF604–670 (displayed within LF599–704) | Commutation of two real PA factors. The full proof expands both codimension-two sums, reflects the two oriented perpendiculars, and pairs cross terms; coefficients are -cot(theta) and csc(theta), with the diagonal and swapped cross sums equal. | Complete local proof available; no delegated historical reference is imported. The quotient removes common lineality and has the two facets of a pointed planar cone, including a nonsimplicial original top cell. Optional recursive convention comparison retains -f and every saturated covolume. This is not an approximation theorem. PASS. |
| BBGS 3.18–3.19, entire LF675–704 | Pairing all ambient linear forms characterizes balanced conormal sums; real PA products preserve balance after refinement. | Intermediate signed/zero weights are legal. 3.19's printed commutation reference to 3.12 points to the equality actually proved in 3.15; the complete equality was read. PASS with this locator correction. |

Rerun bounded source reads, for example: `python read_bound.py primary 1 689 847 --lf` and `python read_bound.py primary 3 604 670 --lf`. `reader-ranges.jsonl` records issued reads, not a certificate that an oversized output was successfully displayed. Display repairs and whole-body methodology are in `evidence-report.md`.

## Conversion with sign and recursive saturated covolumes

For a k-cell sigma and saturated facet rho, a facet lattice basis plus a primitive quotient lift is a cell lattice basis. Its perpendicular projection has length c_sigma/c_rho, independent of which primitive lift is chosen. Multiply the actual lattice coefficient by c_sigma. Unit normal balance then follows from primitive balance modulo T_rho, since the common factor c_rho multiplies the entire conormal sum. This applies in every tangent dimension, with arbitrary lineality.

For a continuous affine factor f, extend its tangential face derivative to an ambient affine form. Subtract it in every incident derivative; balance cancels the ambient extension's contribution. In the BBGS product the negative sign becomes the positive primitive divisor when the factor is -f:

    BBGS_product(-f, c_sigma * lattice_cycle)(rho)
       = c_rho * BMPS_positive_divisor(f, lattice_cycle)(rho).

Apply this at k=d,d-1,...,1. Intermediate cycles may be signed or zero. At vertices c=1, so the terminal raw coefficient has the original lattice convention. No factorial, Euclidean-edge substitution, unsaturated lattice, or mass normalization is introduced. This is the only freshly checked recursive convention comparison; the whole older mixed completion remains a qualified S272 premise rather than a recursively reproved theorem. New306 has no fresh MA application to its nonPA extension or isolated cell.

## Six whole qualified grants and annotations

| Whole input | Bound math indices | Reusable exact scope; limiting qualification |
|---|---|---|
| A224 | 0–1 | Actual finite PA strict-growth/contact obstruction in its specified geometry, with active PC-cost conditions and coefficient restrictions. No arbitrary real classification. |
| B225 | 2–3 | Positive spanning/maximum and finite globally embedded noncompactness. No exclusion of compact abstract atlases. Main spanning is independently proved here. |
| R230 | 4–5 | Actual continuous completion and ALL-C_b unrestricted envelope under continuous reference/obstacle, including the original raw competitor class. No PA density, trace synchronization or operator-domain conclusion. |
| S262 | 6–11 | Whole paper plus reader/acceptance annotations, with source ledger/material as DATA. All-continuous finite balanced graph sector; genuine relative PA operator domain and fixed-C weak/BL distinctions. No higher-dimensional gluing. |
| S272 | 12–17 | Whole actual-real-reference mixed completion in genuine uniform/decreasing PA closure, signed/zero cycles and zero mass; proper rational-component height, ordinary weak/net continuity, global vague uniformity, fixed-C-only uniform weak/BL. Its historical native210 evidence INCONCLUSIVE remains historical. Ledger/material do not add grants. |
| S291 | 18–24 | Entire unchanged mathematical paper together with BOTH source correction and reader clarification. Exact boundaryless homeomorphic rational embedding-chart atlas; independent direct-sum complete affine point bouquets; actual full-affine rational-spatial real majorants. No positive-dimensional overlap gluing or arbitrary atlas reduction. Original native218 source FAIL, combined FAIL and history INCONCLUSIVE remain unchanged. |

Exactly these six are whole grants. Working296/297/299 (25–27), new306 TeX/argument/ledger/scope (28–31), and actual native224 FINAL (32) are unreviewed mathematical/evidence data under this audit. All 33 bodies have been read. Saved expanded notes are separate evidence, not extra mathematical grants. No native225/226, new304/305, S292/S298, privateACTIVE, unbound proofs or current reviewer feedback was accessed.

## Errors and differences that do not alter the current mathematical proof

1. S262/S272's original ledgers use LF604–667 while describing BBGS 3.15 as complete; that range omits its final equality and ending. S291's bound correction supplies the correct LF604–670 and explicitly does not certify historical reading. The present audit directly reads the full unit. An old locator error is retained as an old error, not silently converted to a past PASS.
2. S291's original ledger labels BMPS 2.19/2.20 weights real. They are rational. Its correction and reader annotation separate BBGS's real formal domain and the independently justified extension. New306's actual real hypotheses and independent flux proof are valid without relabeling BMPS.
3. BMPS 3.2 allows a possible REAL center with rational endpoints and real coefficients. The historical first rational-center interpretation was corrected. L0 deliberately uses a rational-center SUBFAMILY and feasible perspective density, so the correction leaves that proof valid.
4. The current task asks for a sum penalty; the frozen author task and unchanged new306 print a maximum penalty. Both vanish on the entire cell and satisfy the distance/coercivity arguments. `reconstructed-proof.md` proves both without editing the unchanged paper. The abstract's word “polyhedrally-concave” is inconsistent with its printed convex inequalities; the theorems and proofs consistently use convexity.

These distinctions justify PASS for current essential-source validity, while retaining historical source/combined FAIL and historical evidence INCONCLUSIVE. Author assertions, hashes, builds and finite tests are not proof of this verdict.
