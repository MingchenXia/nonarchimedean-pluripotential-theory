# Chapter 60: model measures, pairing and energy normalization

Date: 23 September 2026.
Baseline: `3e63d207c7c7bef93cbbe44c706c783ceaa9423e`.
Scope: Sections 60.2–60.3 of `parts/part5/ch60_mp_psh.tex`.
The preceding model constructions and the text from the monotone completion
onward retain their baseline bytes. This unit expands established model
calculus and its examples; it proposes no new research result.

## Mathematical checks and additions

The model-independence argument, signed mass-one statement, nef positivity,
weighted Zariski calculation and real first-variation proof from the
22 September audit were rechecked and preserved. The central multiplicity
is explicitly ord_E(X_0), distinct from the associated normalized point.
The point model has no exceptional component in dimension zero. In positive
dimension, extra divisors of a smooth domination have image dimension below
n and contribute zero by projection formula. Neither signed mass nor model
independence requires nefness; positivity uses nef restrictions.

The new formulas give MA_beta(0) as the atom at the trivial valuation and
MA_beta(phi+a)=MA_beta(phi) for real a. The product model proves the first;
the full central fibre restricts trivially to every component, proving the
second even for the signed model measures.

The deformation-to-the-normal-cone example now proves its relative
Kähler assertion. The tautological O(-E_1) of the blowup is relatively
ample. Relative projective embeddings give local metrics positive on the
kernel of the blowup differential, and base partitions preserve that
positivity. On each central component the pulled-back Kähler form is
semipositive with exactly that kernel. Compactness gives a common small
positive coefficient for both components. The proof states why this
coefficient is uniform. The connected intersection P(N_Z/X) and the two
multiplicity-one components justify the interval. The point calculations
in dimensions one and at least two, and the P2 energy and discrepancy
numbers, retain their values and hypotheses.

`prop:mp-pairing-normalization` proves the three structural identities:
insertion of (0,1) gives the mixed background volume; n+1 zero-potential
classes have zero product; simultaneous rational scaling of the potentials
multiplies the pairing by q. The integer case uses the resolved normalized
base change t=s^m, degree m, and the already established divisor-potential
formula. Real linearity includes real model functions. The rational case
first uses their established PL representability, then b(q·phi)=a·phi.
No integer-degree map is asserted for a nonintegral rational number.

Model testing then proves MA_beta(q·phi)=(s_q)_*MA_beta(phi), s_q(v)=qv.
The proof checks the reciprocal action on the test function explicitly:
(q^(-1)·psi)(v)=q^(-1)psi(qv). Finite signed measures are determined by the
uniformly dense PL lattice, so the identity holds without a positivity
assumption on the background beyond positive top self-intersection.

The Zariski square formula now has a semantic label. Equality means that
the vertex values are constant on each component of the graph whose edges
have positive mixed intersection weight. Polarization gives the exact
bilinear formula and weighted Cauchy–Schwarz, including zero seminorms.
On the point-blowup model of P2, Gamma=alpha_model restricts to zero on
E_1. The mixed edge weight and E_1 squared against Gamma both vanish,
although the potential of E_1 has values 0 and 1. Thus relative nefness
does not justify reducing the kernel to constants on the whole dual complex.

Finally the text derives E(0)=0, E(phi+a)=E(phi)+a,
J(phi)=phi(v_triv)-E(phi), translation invariance of J, and homogeneity
of E and J under rational scaling. The translation calculation uses
F^2=0 and F B^n=V_alpha for the full fibre F. Concavity and the first
variation at zero give J>=0 on the real model psh class. In dimension
zero E evaluates the constant function and J is zero. These calculations
remain within model functions and do not silently extend rational scaling
to an irrational parameter.

## Source verification

The exact primary source is Mesquita-Piccione's
[18 September 2025 author version](https://arxiv.org/html/2409.06221v2),
already identified in the book by `MPTropicalV2`. Printed pages 36–39
were read, rendered and inspected for this unit:

- Section 4.2.1 and Definition 4.2.3, p. 36: measure and pairing.
- Proposition 4.2.4, pp. 37–38: constants, zero potentials, scaling and testing.
- Lemma 4.2.6 and Remark 4.2.7, pp. 38–39: Zariski and Cauchy–Schwarz.
- Definition 4.2.9 and its ensuing calculation, p. 39: energy and variation.

The source PDF SHA-256 is
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The displayed b_E=v_E(X_0) in Proposition 4.2.4(v) is not copied:
the book uses the unnormalized order for the multiplicity. The source's
extra fibre factor in the zero-potential proof and extra index in the
base-change intersection sentence are likewise replaced by dimensionally
correct products with n+1 factors. The published bibliography entry and
all frozen source records are unchanged; the live citations identify the
checked author version rather than assigning its locators to the journal.
The earlier relative-ampleness construction and Demailly–Păun componentwise
positivity criterion are used with their existing verified hypotheses.

## Second pass and validation

After the first full build and inspection of physical pages 3347–3354,
a second complete statement/proof/source/prose pass checked the signed
measure scope, all multiplicities, the degree-m projection formula,
reciprocal test-function scaling, zero graph weights, dimension zero,
the two-component positivity parameter and the point example. It made the
uniform positivity argument explicit and recalled the multiplicity at the
start of the measure section. Final page revisions keep formula introductions
with their displays. The final complete build and the same scoped page
inspection were repeated. This is not an all-page visual review.

- Full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`:
  PASS, **3,973 pages, 18,903,183 bytes**.
- Reference and input audit: **390 TeX files, 11,614 unique labels**;
  no missing input, duplicate label, dangling reference or structure defect.
- Final log: no unresolved reference/citation, multiply-defined label,
  rerun request, or horizontal/vertical overflow. Existing underfull/class
  warnings remain.
- Scoped strict house audit: zero errors, one reviewed warning about the
  exact-version arXiv entry. Strict mode therefore returns 1; no warning-free
  strict pass or clean whole-book house audit is claimed.
- Inventory: PASS, **45 atoms / 14 formal environments**, tiers
  **(0,5,8,15,17)**. No new atom retirement.
- Whitespace check: `git diff --check` passes.

Final Chapter 60 SHA-256: `e99a46e84caaae928d291c736d26bb7e6d07318ae115ac5b8440d09ecf984613`.
Final live PDF SHA-256: `09b1851d0d65e7e3f930b3e51fb22e21ab75eccb19e2bf6fcbd3bcc7bc166cd1`.

The completed P12.1 source integration remains at commit `2de7848`.
The user-supplied PDF in Downloads and its archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The Chapter 70 normalized-links fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
P12.2–P12.6, author originals, bibliography, historical audits, frozen proof
packets, verifier receipts and dated releases are unchanged. No independent
agent or production-verifier pass is claimed. The PDF remains the ignored
live build product. The overall book audit continues with the monotone
completion and the precise finite-dimensional divisorial estimates.
