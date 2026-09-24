# Chapter 63: volume normalization and contact masses — 24 September 2026

## Scope and proof obligations

Baseline: `569bacee156a340d22f2df1a50a2772f14c8e291`. The pending
threshold-variation commit was successfully pushed to the designated origin
at the start of this round, after an initial fetch failed with a GitHub TLS
error. Revision took place in a temporary archive of the baseline, with
no live manuscript build or concurrent source edit.

The new Chapter 63 section makes the numerical normalization explicit on
one fixed connected compact Kähler manifold of positive dimension, in one
fixed Kähler class of volume V > 0. Neither the background nor the potential
is scaled when switching from probability energies to mass-V energies.
The unnormalized test-curve energy is V times the MP energy and equals the
unnormalized energy of its zero-initial maximal ray divided by time. The
reference volume, rather than a possibly zero terminal mass, enters the
conversion. The ordinary-norm/squared-norm convention is separately recalled.

For a positive measure nu of mass V, the dual energy is defined on the same
finite-energy potentials. Factoring V out of every competitor proves the
identity E_raw^vee(nu) = V E^vee(nu/V); all integrals are finite because
nu/V has finite energy. The closed mass simplex is used, including zero
coordinates. Distinct divisor orders and a nonempty list are explicit.
Multiplying the two already proved Legendre formulas by V gives both raw
formulas, including attainment and uniqueness of the minimizing mass vector.
The threshold gradient is the raw contact mass and sums to V. For mass
variation with class and support fixed, the outside V and the direction
h/V cancel, giving minus the pairing with the sup-normalized solution.
This also checks the inward derivative on boundary faces; inactive slack
in an arbitrary optimizing threshold does not enter this derivative.

The model/ray paragraph retains f_D >= 1, the factor n in the scalar
coefficient, the exact model/potential identities, and the Mabuchi slope
inequality. Dividing both M and J by V preserves their coercivity constant.
It does not supply a new entropy-slope equality or remove the model
normalization. Integrating A_total = A_reduced + 1 adds 1 to probability
entropy and V to mass-V entropy. A constant ray independently detects the
incorrect shift. The existing Chapter 62 closing interface needs no edit.
The Chapter 63 comparison ledger now says probability-normalized radial
energy. No equality of Monge--Ampère operators is inferred from an order
isomorphism of psh cones.

## Curve verification

For the two divisor orders at 0 and infinity on P1 with degree d > 0,
the raw constrained energy is the integral of the positive residual degree
(d - lambda_+ - (lambda-b)_+)_+, with the lower-end correction d*lambda_0.
Exact integration gives the three branches in the text. Their derivative
is the second raw mass, ranging from d to zero; the two raw masses sum to d.
The dual value is (m_1^2+m_2^2)/2. The interior maximizing threshold and
both boundary half-lines are explicit. At d=2 and b=0 the raw gradient
is (1,1), while the probability gradient is (1/2,1/2).

Exact rational arithmetic used degrees 1/3, 1, 3/2, 2 and 5, with 49
thresholds per degree and 21 mass fractions per degree. It checked 245
piecewise volume integrals, 5,145 Legendre inequalities and attaining
choices, 4,410 threshold first-order remainder bounds, and 2,205 mass
first-order remainders. The independent integral was evaluated by summing
trapezoids at every affine breakpoint and zero of the residual degree.
For the mass derivative, the solution's two endpoint values are -m_1 and
-m_2, and the exact remainder in tangent direction (h,-h) is h^2. These
calculations verify the example and do not replace the general proof.

## Sources and limits of verification

The published [Darvas--Xia--Zhang article](https://ems.press/content/serial-article-files/50355?nt=1)
was reopened through the publisher PDF's extracted text. Theorem 2.6(iii),
p. 282, and equation (34) and Theorem 3.17, p. 299, use the reference-volume
normalization and the stated finite-energy correspondence. The bibliography
key DXZ23 already identifies the published 2025 article. The established
book energy correspondence, including the MP analytic existence input,
is used with its existing scope; this unit does not reprove it. Fresh PDF
screenshot/download attempts failed at the network layer. This round's DXZ
check uses the accessible publisher text and the earlier full PDF audit,
not a claim of a fresh visual PDF check. Its previously recorded exact PDF
SHA-256 is `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`.

[MPWN25 version 1](https://arxiv.org/html/2509.09442v1), Section 2.3.2,
p. 12, defines the probability dual energy and states integrability.
Theorem 9.1.1, p. 31, includes f_D >= 1 and the factor V^{-1} in both
model identities. Both pages were rendered and inspected from the cached
exact source PDF, SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.
The missing factor n in the source's scalar coefficient is handled by the
existing verified book correction, whose bytes are preserved. No published
replacement for this exact version was established in this round.

The real-weight duality, threshold differentiability and inward mass
variation are taken from the completed Chapter 62 proofs. This is a local
two-pass normalization/consequence audit, not a new independent-agent audit
or production-verifier receipt. All 45 research atoms and the completed
P12.1 integration keep their existing statuses.

## Second pass and final validation

The second pass reread the entire new section against the fixed-class
hypotheses, finite integrals, both extremization signs, zero masses,
normalization of the derivative direction, scalar coefficient, discrepancy
shift and inequality direction. It made the mass domain and optimizing
half-lines explicit and placed the numerical discussion in its own section.
It repaired the first build's 4.81392pt display overflow and the following
page break without changing prior mathematical statements.

Both full-book build rounds completed. The final PDF has 4,001 pages and
19,053,742 bytes, with no unresolved reference/citation, multiply defined
label, rerun request, or horizontal/vertical overflow. The source closure
has 390 inputs and 11,695 unique labels. The problem inventory remains
45 active atoms in 14 environments, with tier counts (0,5,8,15,17).
The scoped house audit reports zero errors and one reviewed warning for
the exact MPWN preprint; strict mode therefore exits 1 for that warning.
Physical pages 3450--3452 were inspected in the first pass; final physical
pages 3450--3453 and 3455 were rendered and inspected, including the
section transition and the changed comparison-ledger entry.

Final PDF SHA-256:
`1f092168ccd73e57ce38dbe2479ab8b8fbdc1f9e810462768492488d63c8bcf1`.
Final Chapter 63 SHA-256:
`338ba799c0809d5f47e53838bcf90fd093ddda3ed8dbded8dfad3336f0b11545`.

Removing the new section and reversing the single comparison-ledger wording
change recovers the entire baseline Chapter 63 byte for byte. Every other
tracked source was compared against the 4,139-file baseline before updating
progress records. Chapters 60--62, all frozen verifier-backed passages,
P12.1 integration/provenance, supplied originals, bibliography, frozen
packets, verifier receipts and dated release artifacts are unchanged.
Only the current ignored book.pdf is replaced by the checked PDF. The
five-file revision unit contains Chapter 63 and the four current progress
and audit records; no generated build files are committed.
