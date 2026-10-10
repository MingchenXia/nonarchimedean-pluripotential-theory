# Wu's local non-Archimedean psh theory: primary-source audit

Date: 8 October 2026. Controlling source: Lyuhui Wu, *On the local theory of
non-archimedean psh functions*, [arXiv:2609.27610v1](https://arxiv.org/abs/2609.27610v1),
posted 23 September 2026, 55 physical pages. The complete PDF has SHA256
11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8.

All 55 pages were actually read with their complete selected text and 28
individually displayed matching rendered images. Each view has its own
sequential note and hash-pinned receipt. Prepared flags remain false; the
actual-reading ledger is separate. The PDF extraction's font-type warning
is retained, with no detected content loss in the paired visual review.
Thirteen exact elementary diagnostic families pass. Neither export nor
upload supplies reading credit.

The source claims a local psh theory, a weak/global psh comparison, a
specific smooth-approximable CLD comparison and an envelope theorem for
geometrically unibranch projective varieties over complete discretely or
trivially valued fields of equicharacteristic zero. The envelope argument
depends essentially on Theorem 6.5. This audit does **not** admit that
general comparison or envelope theorem: several literal conventions and
essential proof interfaces must be repaired or independently justified.
An intended corrected theorem may be true. The diagnostics below do not
prove the main theorem false.

## The controlling growth conflict

Definition 3.15(2), physical page 16, defines logarithmic growth by an FS
**lower** bound, while Definition 6.1(2), physical page 37, uses an FS
**upper** bound:

\[
 h\leq u+O(1),\qquad\text{versus}\qquad u\leq h+O(1).
\]

Here an affine FS function is a finite maximum of positive rational
polynomial logarithms and a finite rational floor, whose polynomial family
generates the coordinate ring. Definition 3.15(3) additionally requires a
decreasing FS presentation, while retaining its lower-growth premise.
These two printed growth classes are different even on the affine line.
They must not be silently identified.

On \(\mathbf A^1\), with \(t=\log|T|\), consider

\[
 v_j(T)=\max(t-j,0)\downarrow0.
\]

Each \(v_j\) is affine FS. Every FS function on the affine line has a
positive-degree polynomial generator and tends to infinity along large
Gauss radii. Consequently 0 fails the printed lower-growth condition.
This diagnoses the decreasing-limit conclusions of Corollary 3.18 and
Lemmas 3.24(3), 3.25(3), as literally stated; it does not refute the usual
upper logarithmic-growth convention. Logarithmic poles likewise belong
naturally to an upper-growth class and need not satisfy an FS lower bound.

A second distinction remains even among continuous functions. Set

\[
 w(T)=\max_{k\geq0}\{k\log|T|-k^2\},\qquad w(0)=0.
\]

Only finitely many terms are active on each bounded-radius set, so this
is a continuous local convex PL psh function under the intended genuine
convexity convention. It obeys

\[
 \max(\log|T|,0)\leq w+1,\qquad
 w(\eta_{e^{2m}})=m^2
 \quad(m\in\mathbf Z_{\geq0}),
\]

where the second formula follows from
\(2mk-k^2=m^2-(k-m)^2\). A finite FS function has eventual growth at most
\(A\log|T|+B\). Thus \(w\) has the printed FS lower bound but no FS upper
majorant and no decreasing global FS presentation. In particular the
first upper-majorant step of Proposition 4.19 does not follow from its
printed hypothesis. That proof also invokes Lemma 3.25(1) for a function
not yet known to belong to the lemma's regularizable class.

## Finite limits and local measure scope

Generic finiteness is part of the source's psh definition. Constants
\(-j\) decrease to the excluded identically minus-infinity function.
Finite-limit exceptions must therefore accompany the closure statements
in Proposition 2.21 and Corollary 4.18(4); the generic-finiteness premise
actually present in Corollary 4.18(1) is acknowledged and retained.
Likewise the whole product \(D=Y^{\mathrm{an}}\times\mathbf A^{1,\mathrm{an}}\)
is Runge and contains the zero section, but the vertical radius in
Proposition 5.7 is identically infinity. Its negative logarithm is
identically minus infinity. A nondegeneracy or finite-limit hypothesis
is missing from that literal general statement.

The continuous function \(w\) above also separates local from global
integrability. In the normalized one-dimensional graph calculus its slopes
jump by one at \(\log|T|=2k+1\). Its positive curvature is a locally finite
Radon measure with infinite total mass on the affine line. The constant
function 1 is therefore not globally integrable for it. This diagnoses
the global \(L^1(U,\mu)\) wording of Theorem 4.2(3), whose proof gives a
local conclusion; it does not reject a correctly formulated local
Bedford--Taylor operator or compact-carrier estimate.

Theorem 4.11(1) assigns the curvature of the maximum on \(\{u>v\}\) to
the wrong operand. On a bounded annulus take
\(u=1+|\log|T||>v=0\); the maximum has curvature \(2\delta_{\eta_1}\),
whereas \(v\) has curvature zero. The correct operand is \(u\).

## Polynomial hulls, neighbourhoods and localization

The coordinate-ring hull definition, monotonicity, increasing Runge union,
closed-subvariety quotient and compact hull arguments have elementary
algebraic/topological justifications. They can be retained with their
precise compactness hypotheses. Several printed separator inequalities
in Lemma 5.3 and Proposition 5.4(2) have reversed signs; strict separators
and a sufficiently large coordinate polytope supply the conventional
neighbourhood construction.

One must not identify the interior of every presented polytope with the
strict version of all its inequalities. Present
\(P=\{|T|\leq1\}\) also with the redundant constraint \(|1|\leq1\).
The interior contains \(\{|T|<1\}\), but every simultaneous positive
tightening imposes \(1\leq e^{-\epsilon}<1\) and is empty.
This contradicts the displayed shrinking identity in Lemma 5.3, not
polynomial convexity or a correctly proved Runge conclusion. Direct strict
norm sublevels and strict compact-carrier bounds can avoid that identity.
The FS-hull equality likewise has a direct finite-maximum/separator
argument, without assuming an FS separator vanishes on an arbitrary
unbounded neighbourhood.

The radial coefficient calculation of Lemma 5.8 has an elementary
Gauss-norm proof once the constant coefficients are strictly below their
thresholds. The valuation minimum must include the constant term.
If all positive-degree coefficients vanish, the radius is infinity and
the inverse logarithm is minus infinity; this is an extended-value case,
not a finite PL function.

The essential localization proof in Lemma 5.11 mistakes a formal
denominator power for an actual pole order. Take

\[
 f=T^2,\quad g=T,\quad r=1,\quad c_1=1,\quad c=\tfrac12,\quad
 u=\max(\log|T|,0).
\]

On \(Y_f=\mathbf G_m\),
\(u_c=w=\max(\log|T|,-\log|T|,0)\) is FS and \(w\leq u_c\) exactly.
Its term \(\log|g/f|=-\log|T|\) nonetheless has
\(c_1r=1>c\). Moreover \(g\notin(f)\), although \(g\) vanishes at every
point of \(V(f)\). The claimed nonvanishing implication requires a radical
ideal or an actual vanishing-order argument. This counterexample refutes
that estimate, not an independently corrected localization theorem.
The terminal \(\sup_L|v|\) in Proposition 5.10 is also weaker than the
required \(\sup_L v\).

## Conventions and later proof dependencies

The detailed sequential notes retain the following additional distinctions.
Some are direct literal diagnostics; others are proof obligations rather
than counterexamples.

- A model frame has norm one on its reduction tube, not on the entire
  generic scheme open. For the standard DVR model of \(\mathbf P^1\),
  \(D(1+\pi T)\) contains the generic point \(T=\pi^{-2}\), where
  \(v(1+\pi T)=-1\). Additive usc weights also correspond to the opposite
  semicontinuity of their norms.
- Definition 3.1(3) omits the touching constant in the lower affine bound.
  Literally any continuous function satisfies it locally by placing a
  constant affine function below its value; even \(-|t|\) then qualifies.
  Every intended convexity argument here uses genuine affine support.
- Connected-component generic finiteness is weaker than finiteness on
  every irreducible component. A decreasing FS family on the connected
  two-line projective curve can become identically minus infinity on one
  component and remain finite on the other. Normal varieties permit a
  different componentwise treatment; the examples do not refute their
  intended envelope statement.
- The bounded local globalization proof in Proposition 3.28 needs
  compatible reference potentials, rational rescaling and a genuine
  negative collar. Its printed FS potential is nonnegative but is used
  as though it were negative at the selected point. A change from an FS
  representative to the prescribed model form must carry its PL
  reference correction.
- Lemma 4.14's assertion that every local PL function extends globally
  fails for \(\log|T|\) on \(\mathbf G_m\subset\mathbf P^1\), since global
  finite PL functions on the compact projective line are bounded.
  Compact-carried integration by parts only needs an extension near the
  test support; a suitable PL bump and max/min clamp can provide a
  conditional local repair.
- The point blowup has \(\mathcal O(E)|_E=\mathcal O_E(-1)\), so
  \(-E\), not \(E\), is relatively ample in Lemma 3.32's proof.
- Lemma 6.6's printed Gaussian has mass \(2^{-k/2}\), not 1, and its
  inverse scale widens as \(\epsilon\downarrow0\). Its support inequality
  also uses \(l(t)\) instead of \(l(t')\). Standard normalized narrow
  convolution corrects those specific formulas; extension to partial
  infinite coordinates still uses an external tropical input.
- Lemma 6.8 assumes regularizability of \(u+c\rho\) on its charts but
  later asserts regularizability of \(u\) there. Subtracting a psh
  function does not justify that assertion. The stronger local
  hypothesis on \(u\) matches the subsequent application.
- Finite-flat fibre-algebra dimensions, their constant rank sum and the
  degree-times uniform estimate are classical algebra. Psh preservation
  of a norm metric still requires the BE21 theorem. The additive
  potential is **minus** the logarithm of the norm section, opposite the
  sign printed at the end of Proposition 6.11's proof.
- Proposition 6.12 explicitly invokes Proposition 4.19 over \(H_S(s)\).
  That completed residue field need not be discretely or trivially
  valued: an irrational-radius Gauss point has value group containing
  \(\mathbf Z+\sqrt2\mathbf Z\). Proposition 4.19 does not cover it.
  The arbitrary-field curve limsup lemma 6.13 supplies a uniqueness
  step, not the missing FS regularization input.
- A continuous integer-valued branch norm is locally constant; one
  constant on the whole chosen neighbourhood additionally needs
  connectedness or a proved branch-rank statement. Lemma 6.15 does not
  supply that argument. Its later division by \(\gamma-1\) also needs
  the possible case \(\gamma=1\) handled separately.
- Pullbacks and restrictions may be identically minus infinity on an
  entire curve component. A generic-finiteness exception is needed
  before invoking a class that excludes that function. The term
  “injective scheme morphism” and the exact analytification theorem
  also need their hypotheses checked. The notes' field-extension
  example shows the distinction from **universal** injectivity; it is
  not asserted to be a counterexample to injectivity of the original
  analytic map.
- The proof of Theorem 6.3 applies an irreducible-source proposition
  while its general reduced source can have components meeting at the
  selected point. No irreducible neighbourhood is then automatic.
  The characteristic-zero projection application avoids the
  imperfect-field regular-versus-smooth issue in the more broadly
  worded Lemma 6.16.
- Uniform smooth/PL approximation must be turned into a decreasing
  presentation on **one fixed neighbourhood**. Appendix A's bridge
  uses essential APW26a/26b preprints, listed without identifiers or
  versions, in addition to that approximation bookkeeping.

A concern raised during reading about nondiscrete fibres in Proposition
2.24 is **not** retained as an unaddressed direct-field objection: its
two-step proof first treats divisorial points on closed strata, then uses
flat openness and divisorial determination. The actual remaining question
there is the precise same-index lifting/determination justification.
Likewise closure bars visible in the matching rendered images are
acknowledged; extraction loss of those bars is not counted as a proof error.

## Admission and publication boundary

Retain the source's research direction, its exact theorem hypotheses and
the elementary convention/growth diagnostics. Do not import the general
weak/local/global or geometrically-unibranch envelope theorems without a
corrected proof and checked external inputs. The countable-subfield
reduction in Theorem 7.1 must compare actual psh PL minorants below the
obstacle; arbitrary PL functions, as literally written, do not suffice.
Contact-support inclusions and descended reference data also require their
proper scopes. None of this audit certifies the cited unversioned tropical
preprints, BE21's full norm-metric proof, or all CLD/Thuillier comparisons.

No original general theorem is promoted and no independent-model receipt
is claimed. The 42 canonical atoms and twelve formal problems retain
their statuses; general BJ22 critical homogeneous Siu/envelopes remain
OPEN and LPWZ density remains UNVERIFIED. The warning concerning BJ22
Theorem 6.21 is preserved: this new preprint is not treated as a repair
of that proof. All 425 book TeX inputs, both bibliographies, the active
4,647-page PDF and native catalogue/editor remain unchanged at this source
checkpoint. The last complete ordered whole-book pass remains 4 October.

The authorized repository evidence consists of authored notes, receipts,
hash records, diagnostics and helpers. The complete primary PDF/text/image
archive remains in the cloud and is separately hash-pinned. Book
integration, rendered reading, activation and remote verification have
their own subsequent gates.
