# Chapter 65: analytic comparison and normalization — 24 September 2026

## Scope and baseline

Baseline: `178d045d1c62d468d0baad06a8a34878f710a093`. The live main branch
was clean and matched the designated origin. All drafting, builds and
PDF review used a separate export. This unit repairs the analytic
commutative-diagram proof and derives invariance of the closed test curve
and ray under section saturation and integral closure. It does not review
the remaining BHJ19 slope proof or promote any research atom. No new
independent-agent or production-verifier verdict is claimed.

## Proof and normalization

The previous proof passed from partial Bergman base ideals to an
asymptotic maximal envelope without justifying the valuative limit.
The new argument uses the integral-jump Rees convention already fixed
in Chapters 33 and 65. Choose a globally generated degree r whose Rees
Veronese is generated in degree one, with adapted weights w_i. Set
M=rL, B=max w_i and d_i=B-w_i. On R(X,M), shift degree k by kB, so the
new weights are -d_i and the cutoff is zero. The all-equal-weight case
D=max d_i=0 is treated directly.

The base ideals a_j of the degree-one pieces at -j are increasing,
M tensor a_j is globally generated, and a_D=O_X. The coefficients a_kq
of (sum a_j zeta^j)^k define the left-continuous filtration
H0(kM tensor a_k,floor(-lambda)). Coefficient multiplication, monotonicity
and the bounds 0 for q<0 and O_X for q>=kD verify its filtration axioms.
Every shifted Rees monomial belongs to this filtered space, proving
inclusion without asserting equality with all sections of the base ideals.

Inclusion gives the upper comparison. DXZ Lemma 4.10 computes the flag
curve's analytification as -sigma(v)(a), equal to max_i(-v(s_i)-d_i).
This lemma is an explicit imported analytic input, using the normalized
blowup; it is not disguised as a formal consequence of base-ideal
arithmetic. For the reverse bound, the single section s_i bounds the
potential at every tau<-d_i. Its generic Lelong number gives the lower
bound tau-v(s_i); taking tau up to -d_i proves the desired equality
without using a raw terminal filtered piece.

Powers of omitted sections justify Veronese cofinality. With actual
L-degree retained, the shifted curve and ray are

    Gamma_G(tau) = r Gamma_F((tau+B)/r),
    ell_G(t) = r ell_F(t) - B t.

Their divisorial transforms obey Gamma_G^An=r Gamma_F^An-B, giving the
finite FS formula after division by r. The initial mass and established
finite-FS property supply BJ psh extensions on both sides. BJ divisorial
determination extends equality to all semivaluations, including proper
support. The global-generation lower bound makes the common function
finite everywhere.

The algebraic invariance already proved gives identical analytifications
for the saturated and integrally closed filtrations. Their cutoffs agree
at the trivial valuation. The precise I-model and order-reflection results
of DXZ identify their interior levels, and decreasing left limits identify
the closed endpoints. Their Legendre rays therefore agree with fixed
reference metric and linearization. The final Phong--Sturm assertion
uses this corollary after the analytic identity has been proved, so the
argument does not depend circularly on normalization invariance.

For the nonnormal P1 example, weights 2 floor(j/2) become j. Termwise
comparison in the same orthonormal basis gives
0<=Phi_bar(m,t)-Phi(m,t)<=t/m. Both tail envelopes equal
log(1-p+exp(t)p). At p=1 and odd m the error is exactly t/m; setting t=m
precludes uniformity on the entire half-line. The common NA values are
0 and 1 at the two supported endpoints, and 1 at the full-support trivial
valuation. These checks distinguish finite layers, the limiting ray and
the terminal parameter.

## Primary sources and review passes

- [Darvas--Xia--Zhang, published article](https://ems.press/content/serial-article-files/50355):
  Theorem 3.12(i), p. 294; Lemma 4.5 and Definition 4.7, p. 302;
  equation (38) and Proposition 4.8, p. 303; Definition 4.9 and
  Lemma 4.10 with proof, pp. 304--305. Physical pages 26 and 34--37
  were visually checked. The paragraph before Lemma 4.10 points to
  Theorem 3.12(ii), but order reflection is part (i); the book cites
  the correct part. The existing DXZ23 key and published DXZ25 label
  are retained.
- [Boucksom--Jonsson, published article](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf):
  Theorem 4.22 and Corollary 4.23, p. 715, with the theorem's proof
  on p. 716. Physical pages 70--71 were visually checked. A psh
  extension, rather than arbitrary upper semicontinuity, is required.

The first pass reconstructed the flag comparison, the degree/shift
identities, normalization corollary and example, followed by a full build
and review of physical pages 3521--3526. The second pass made the zero-
spread case explicit before invoking the flag lemma, verified the
coefficient-filtration axioms, recalled the linear bounds locally and
clarified the dependency of the Phong--Sturm conclusion. The full revised
statement/proof sequence and citations were reread. The second full build
and physical pages 3521--3527 were then checked.

## Validation and preservation

Both full builds pass. The final PDF has 4,062 pages and 19,341,348 bytes.
The reference check finds 396 inputs and 11,821 unique labels, with no
missing input, duplicate label, dangling reference or structure error.
The open-problem inventory is unchanged: 43 atoms in 13 environments,
with tiers (0,3,8,15,17). The scoped house audit has zero errors and zero
warnings. The final build has no undefined reference/citation, rerun
request or horizontal/vertical overflow. Its 13 inherited Chapter 70
duplicate PDF destination warnings remain.

Exact checks cover 148 flag-value identities and 5,994 comparisons of
coefficient-ideal min-plus products with independent Rees-monomial
enumeration, including infinite section values and D=0. Further tests
cover 375 stable logarithmic Bergman comparisons and eight odd-degree
endpoints with t=m. These computations test examples and conventions;
they do not replace the proofs.

Before the current progress records were updated, all 4,174 tracked
baseline files except the revised chapter were byte-identical. Within
Chapter 65, everything before the diagram section and from the DH section
onward is unchanged. The six supplied integrations and original files,
CURVE_PSH, P12.1 material, research ledgers, bibliography, frozen packets,
verifier receipts and dated releases are preserved. The BHJ19 quarantine
is unchanged. Only the chapter and four current progress/audit files are
delivered; the PDF replaces the ignored current manuscript/book.pdf.
Temporary source downloads, renderings, checks and build auxiliaries are
not staged.

Reproduce source checks from manuscript/ with
`python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.

- `manuscript/book.pdf` SHA-256: `ed161738f2014b1d0fdc445f986e4941816caaa255bc5fa45129bda738058682`.

- `manuscript/parts/part6/ch65_rays_filtrations.tex` SHA-256: `b5fa8bd21011a13382c189d3a3bb341752f8c8e812248ec44df9c01f77a65c0a`.
