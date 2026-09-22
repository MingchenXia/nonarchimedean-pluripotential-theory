# Chapter 46: finite pairings and model tests — 22 September 2026

## Mathematical correction

The mixed-measure construction now uses the real-valued vector-space
pairing (46.17). The earlier proof conflated that extension with the
ample-psh-only infimum construction. Its initial decomposition for a
test in PL+ was legitimate, but the following remark incorrectly extended
the same assertion to every PL function.

An arbitrary real PL test is written as f+ minus f-, with both functions
psh for a common ample background. They are bounded and of finite energy.
Linearity and independence of representation come from the finite
multilinear pairing. For a nonnegative test, f+ >= f-. Adding epsilon times
an ample class to the other nef backgrounds gives positivity by ample
monotonicity; the finite pairing is polynomial in epsilon, so positivity
persists at epsilon = 0. The argument requires
PSH(theta) intersect vec(E1) when theta is nef, not an unspecified
finite-energy class for a boundary nef class.

Two direct computations explain the excluded shortcuts. For the blowup
of P1 x A1 at (p,0), the exceptional curve E satisfies
(C omega_X + E).E = -1 for every positive C. Thus increasing a pulled-back
ample class does not make phi_E psh. For phi = phi_(-cE), with rational
0 < c < 1, the nonnegative test f = -phi has integral c^2 against
MA(phi), whereas the dominating model competitor 0 has test integral
zero. The infimum of the nonnegative competitor integrals is therefore
zero. A difference of two energy infima cannot be replaced by that
infimum of differences.

The revised construction also:

- explains extension from the convex cone of coupled ample psh pairs,
  using additivity to prove independence of cone decompositions;
- avoids claiming that negating a psh potential gives a psh potential in
  the negative background;
- produces arbitrary signed measures by differences of coupled positive
  pairs, instead of separately decomposing classes and functions;
- states decreasing continuity in a common ample finite-energy class,
  including the finite-energy limit;
- bounds total variation by a finite sum of fixed intersection masses
  before passing from PL tests to continuous tests;
- proves integrability using decreasing model approximants of the psh
  constituents, rather than truncations of an arbitrary vector-space
  difference;
- uses divisorial determination and almost-everywhere finiteness to
  identify different representatives of a finite-energy test.

The nearby polar-set proposition now has the same precise domain.
Its historical label is retained for existing references, but the text
does not claim full mass on the linear-growth locus. The former
attribution of that stronger support claim to BJ Proposition 7.19 was
unsupported: integrability of each test gives a null set for each test,
not for their arbitrary union. Likewise, weak limits of divisorial
measures need not remain on that locus.

## Checked primary dependencies

The published primary source is
[Boucksom–Jonsson, Global pluripotential theory over a trivially valued
field](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf),
Annales de la Faculté des Sciences de Toulouse 31 (2022), 647–836.
The checked locators are Remark 4.14 and Theorem 4.15(iii), printed
pages 712–714; Lemma 7.13 and Theorem 7.14, pages 753–754;
Lemma 7.15 and Remark 7.16, page 755; Theorem 7.18 and
Proposition 7.19, pages 756–757; and Corollaries 7.48–7.49,
page 772. The finite-energy estimates and the vector pairing remain
explicit source inputs. No new research theorem or problem retirement
is claimed.

## Second pass and scoped validation

- Rechecked signs on E, the two atomic masses, the c^2 test integral,
  the epsilon-polynomial limit, the coupled-pair decompositions and
  almost-everywhere independence of representatives.
- The new and rewritten blocks pass the strict Mingchen writing audit:
  zero errors and zero warnings. This is not a claim that the legacy
  chapter passes that style audit.
- The Chapter 46 scoped build grew from 123 to 124 pages. Both builds
  have the same 22 unresolved external-reference occurrences; the final
  scoped log has no unresolved citation or overfull box.
- Physical pages 85–89 of the final scoped PDF were rendered and read.
  The finite-pairing statement, the four construction steps, the two
  counterexamples and the polar-set consequence have no clipping or
  overlapping formulas.
- The source check initially retained the known missing Chapter 70 input.
  After the author supplied that file during this revision, the complete
  closure passed: 389 files, 11,475 labels, no missing input, duplicate
  label, dangling reference or per-file structural defect.
- The active research inventory remains 46 atoms in 14 formal
  environments, with tiers (0,5,8,16,17).

## Follow-up located by this pass

Chapter 49, cor:ch49-mass-in-lin, uses an outer-capacity estimate for
{T_omega > N} that still needs a separate audit: a bound for the sublevel
set of one normalized psh test cannot be applied to their arbitrary
union. Its accompanying claim to reprove the Chapter 46 proposition
also needs correction. No certification of that argument is included
in this receipt.

The adjacent curve discussion also needs its next detailed pass: general
finite-energy profiles need not be eventually constant, and the
endpoint/Dirichlet formulas must use the distributional second derivative
and legitimate limiting operations. The current proof repair does not
certify those earlier formulas. Chapter 60's maximal-ray argument remains
in the continuation queue.

The subsequent full 3,403-page build also passes with all references
resolved; its production inputs and remaining layout warnings are
recorded in [the recovery build receipt](source_recovery_build_20260922.md).
