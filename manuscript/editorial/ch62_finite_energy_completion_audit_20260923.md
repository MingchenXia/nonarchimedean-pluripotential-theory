# Chapter 62: finite-energy completion and fixed-complex entropy — 23 September 2026

## Scope of this revision

This unit reconstructs the proof of Theorem 62.4.1. Its three
potential-theoretic conditions and the normalized model condition
retain the same positive coercivity constant. The separate
all-big-model condition remains only an implication into this
equivalence, as recorded in the preceding normalization audit.
No research-frontier claim or new theorem scope is added.

## Proof obligations made explicit

1. **The nonentropy term.** The published synthetic twisted-energy
   theorem gives a strongly continuous real-valued functional on
   finite-energy measures. With twisting class K_X, its trace is
   n alpha^(n-1).K_X / V = -s. On model potentials the functional is
   s E_alpha + E_alpha^(K_X). A decreasing model net, strong
   Monge--Ampère continuity and decreasing continuity of the finite
   mixed pairings extend this identity to every finite-energy
   potential. The application records the orthogonality and submean
   value hypotheses. Entropy convergence is treated separately.

2. **General finite-energy measures.** The Chapter 61 simultaneous
   strong and entropy approximation is transferred through the
   sup-normalized Calabi--Yau homeomorphism. Infinite entropy is
   handled before taking a limit: the nonentropy term is finite,
   so Mabuchi energy is positive infinity and coercivity is automatic.

3. **The fixed-complex envelope.** The retraction majorant gives
   u <= P(h composed with r), with equality on the supporting
   dual complex. The domination principle, with u as reference,
   proves equality everywhere. This replaces the former unsupported
   attribution to locality alone.

4. **Interpolation and support.** The geometric subdivision input
   keeps the same embedded monomial complex and admits compatible
   snc models of arbitrarily small mesh. Retraction compatibility
   then identifies their retractions. Convexity and uniform
   continuity give 0 <= h_j-h <= epsilon_j, with epsilon_j -> 0,
   for affine interpolation of the actual real vertex values.
   The divisor coefficients are b_(j,k) h(w_(j,k)), including
   central-fiber multiplicities. Real PL functions suffice.
   The envelope inequalities give uniform and strong convergence.
   Before applying the positive-product support formula, each
   obstacle is translated to f_D >= 1. Its envelope measure is
   unchanged and is supported at vertices of the fixed complex.

5. **Entropy.** Reduced discrepancy on that one complex extends to
   one continuous PL test function on the whole space. All the
   measures are supported on the complex, so their entropies are
   integrals of this fixed function. Weak convergence now suffices.
   The argument does not integrate an arbitrary lower semicontinuous
   function under weak convergence, or assume that arbitrary
   smooth-center blowups preserve the embedded dual complex.

## Primary sources and retained inputs

- [Boucksom--Jonsson, published author offprint](http://sebastien.boucksom.perso.math.cnrs.fr/publis/BJ_synthetic.pdf),
  Contemporary Mathematics 810 (2025), 159--208,
  DOI 10.1090/conm/810/16207: equation (4.2), page 191, and
  Proposition 4.5, pages 192--193. The downloaded file is the
  publisher's offprint, not a preprint substituted for an unchecked
  published locator. Its PDF SHA-256 is
  `4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498`.
  The proposition and its continuity hypotheses were checked against
  the extracted text and the rendered published page.
- [MPWN25, arXiv version 1](https://arxiv.org/html/2509.09442v1),
  proof of Theorem 9.2.1, especially implication (3) => (2):
  the model realization with the same embedded dual complex is
  retained as a geometric source input. Lemma 7.2.4 identifies the
  corresponding fixed-complex entropy convergence. The interpolation,
  multiplicity factors, envelope bounds and fixed-test integral are
  written out in the book.
- The full Calabi--Yau, locality, envelope and quasi-metric
  theorems retain their existing source status. The new proof does
  not replace them with an independent research verification.
  The normalized intersection formula is invoked only after
  checking f_D >= 1.

The direct AMS download returned HTTP 403, and the author's HTTPS
host had a certificate-name mismatch. The publicly linked offprint
was obtained through the author's HTTP endpoint without disabling
certificate verification. No third-party PDF was added to the repository.

## Second mathematical pass

The second pass checked the sign of the trace against the frozen
factor-n normalization, all three implications with one delta,
decreasing nets rather than an unproved sequential regularization,
the infinite-entropy case, the direction of domination, the image
and composition identities for retractions, barycentric
interpolation on the original faces, the multiplicities at new
vertices, and the order of support and entropy arguments.
It made the hypotheses of the imported strong-continuity theorem
explicit before its application.

## Validation and preservation

The exact revised proof passed the strict writing audit with zero
errors and zero warnings. The full input closure contains 389 TeX
files and 11,507 unique labels, with zero missing inputs, duplicate
labels, dangling references or structural defects. The active
inventory check passes unchanged: 46 atoms in 14 formal problem
environments, with tiers (0,5,8,16,17).

Both the initial and second-pass complete builds succeeded.
The final PDF has 3,921 pages and 18,614,747 bytes, with zero
unresolved references or citations and zero horizontal or vertical
overflow. Physical pages 3352--3355 (printed pages 3284--3287)
were rendered and inspected after the second pass. The source diff
is whitespace-clean.

PDF SHA-256:
`9e9a370bcbd33ac36e541a0ecbab318bc0522d439b4cd5fcbb0a7eaf0e1db43d`

Chapter 62 SHA-256:
`14cf136871b821aaa51c260fff959ce426a1376f1619beaa213af0f1e8e0417d`

The factor-n verification block is byte-identical, with SHA-256
`204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25`.
The supplied CURVE_PSH.tex remains byte-identical to the author's
download, with SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
No other chapter source, frozen research packet, verifier record,
bibliography database or dated release artifact was changed.
The generated current PDF remains an ignored local build artifact.
No independent-agent audit or new production research gate is claimed.
