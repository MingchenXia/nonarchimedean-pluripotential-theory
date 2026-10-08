# Own source applications

This public artifact contains metadata and own analysis only. Long primary quotations remain in local tool reads; no pixels or full source bodies are published here. Source hashes are in frozen-bindings.json.

BMPS is arXiv 2603.08664v1, submitted 9 March 2026, manuscript 10 March 2026, literal URL https://arxiv.org/pdf/2603.08664v1. BBGS is the 2022 version of record, 44 pages, published 24 January 2022, literal URL https://link.springer.com/content/pdf/10.1007/s00209-021-02869-6.pdf. The PDF and LF-text objects are separately byte-bound. The whole PDFs were hash-read, not visually read. Immediate original units were independently read in their bound text counterparts, splitting on LF only, not form-feed.

| Source | Complete displayed LF units | Own application |
|---|---|---|
| BMPS | 254–301 | Finite rational complexes, translated tangents, inherited refinement. |
| BMPS | 418–638 | Rational formal weights, saturated normals, cycles, literal integral slopes/rational constants, tangent correction, full normal-independence and refinement proof. Lemma 2.35's AR10 delegation is excluded as unprovided authority. |
| BMPS | 691–852 | Whole PCC definitions and Lemma 3.4/Proposition 3.7. Real centers/weights but rational endpoints differ from BBGS. The rational-vertex insertion and gcd steps do not automatically establish arbitrary real/irrational variants. Sector-specific Jensen/support proofs are supplied instead. |
| BMPS | 1005–1034 | Full 3.22/3.23 unit; compactification/Dini is not used to replace the new global shift proof. |
| BMPS | 1354–1503 | Raw unnormalized recursion, degree, bounded-difference degree proof, full mixed symmetry/linearity and signed edge integration-by-parts proof, seminegative sign. |
| BMPS | 1741–1747 | Positivity at infinity on every nonzero carrier recession direction. |
| BMPS | 2253–2360 | Whole envelope statements and immediate proofs. Literal broad density and automatic continuity are not substituted for R230/new density. |
| BBGS | 196–250,379–420 | Abstract/local finite structures and Euclidean quasi-embedding domain, not a lattice-normal theorem by itself. |
| BBGS | 443–598 | Full 3.1–3.9 definitions and 3.12 three-case subdivision proof, including zero new weights and cancelling opposite interior facets. |
| BBGS | 604–704 | Full 3.15 commutation, 3.18 balance test and 3.19 proof. Its last commuting reference printed as 3.12 actually uses 3.15, as bound clarifications disclose. |
| BBGS | 1515–1555,1913–1993 | Whole endpoint definition and complete 6.1/6.2 proofs. They use REAL endpoints and subdivisions through real centers. Used to audit the convention mismatch, not to infer automatic continuity for raw BMPS-PC. Their additional weak-concavity/positivity premises are not imported. |

The primitive-to-metric bridge can be checked directly, rather than replacing normals by unit normals. In a rational m-face sigma write v_sigma for the covolume of its saturated tangent lattice, v_0=1. For a facet tau, a saturated basis of N_tau followed by a primitive inward lift n is a basis of N_sigma. Its perpendicular projection n_perp has length v_sigma/v_tau; n_perp=(v_sigma/v_tau)nu for the inward metric unit normal nu. Set metric weight z_hat(sigma)=v_sigma*z(sigma). Primitive balance projects to sum z_hat*nu=0. For an affine a with common tangent derivative, the tangent-corrected primitive term equals sum z(sigma)a_sigma(n_perp). Hence

BBGS_product(-a,z_hat)(tau)=v_tau*D_a(z)(tau).

This uses BBGS's negative product sign and the negative input -a, so convex a is converted to the concave convention. It holds for signed and zero weights. It intertwines pullbacks on same-dimensional refined cells, including zero cells. BBGS 3.12/3.15/3.18/3.19 therefore transfer refinement, commutation and balance by this covolume identity; at dimension zero v_0=1, so there is no arbitrary normal scaling or appended factorial. The formal BMPS coefficient class remains distinct: real coefficients require the compatibility-kernel scalar extension and polynomial multilinearity on a common rational carrier, not literal membership by assertion.

No ungranted external density, biconjugacy, polyhedron theorem, Alexandrov identity, operator realization or AR10 result is used. The new geometric proofs are in audit-report.md. Whole source/application coverage remains INCONCLUSIVE because the unread grant bodies and their own source ledgers can contain additional essential applications. The above immediate-unit calibration is not a whole-33-body source PASS.
