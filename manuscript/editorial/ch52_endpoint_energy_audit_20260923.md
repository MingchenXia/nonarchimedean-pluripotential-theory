# Chapter 52: closed endpoints, relative energy and loss of mass — 23 September 2026

## Endpoint and Legendre arguments

The terminal level of a normalized maximal test curve is now proved to be
a nontrivial psh function with supremum zero. Its mass is not required to
be positive. The proof uses the compact nested zero sets of normalized
levels; the decreasing limit retains a zero and cannot be identically
minus infinity. Scalar closedness at an interior parameter follows by
comparing the left-limit psh function with the level off a later polar
set, then using uniqueness of psh representatives.

The forward Legendre proof no longer infers that a raw supremum is psh
merely from the psh supremum theorem. That theorem initially gives only
its usc regularization. The argument now uses the common null set from
Fubini and scalar convexity, Kiselman's principle for the inverse
regularized transform, and biconjugacy to identify the raw supremum
with its regularization. The second pass makes the rational-parameter
reduction and hence measurability explicit.

The inverse-transform domain retains the correct closed inequality
tau <= sup_X ell_1. Equality at the endpoint is justified separately:
ell_t-Ct is decreasing and sup-normalized, so its compact zero sets
prevent collapse. For larger tau, the upper bound t(C-tau) tends to
minus infinity. The proof does not infer endpoint noncollapse from
an upper bound alone.

## Energy and source scope

Equation (52.9) is the unnormalized relative energy. Dividing it by
the reference mass m = M_theta(phi), not by the mass of the terminal
level, gives the normalized formula. For phi = V_theta, m is the
class volume and this agrees with published DXZ equation (5).
For a general reference model potential the mass may be smaller.
The integral is well defined in extended arithmetic; its nonpositive
sign alone does not prove convergence. Bounded curves have a zero
integrand on a lower half-line and a bounded remainder on a finite interval.

The general relative finite-energy correspondence is attributed precisely
to Xia's Theorem 9.2.1 and equation (9.21). DXZ Theorem 2.6(ii) supplies
the published relative maximal-test-curve correspondence; its part (iii)
uses the V_theta finite-energy convention. General geodesicity and
relative energy equality remain explicit imported analytic inputs.

A constant-level curve with cutoff c has ray phi+ct and raw energy cm.
On degree-two P1 this is 2c, while the probability-normalized energy
is c. This also shows that terminal mass need not vanish. The existing
hyperplane curve supplies the opposite endpoint behavior: a nontrivial
psh endpoint of zero mass.

A further source check distinguished annular variables. DXZ equations
(6) and (10) use t = -log|z|^2. Xia's Section 4.1 also uses
sigma = -log|z|. For the same annular family,

    ell_t = tilde_ell_(t/2),
    Gamma_tau = tilde_Gamma_(2 tau),
    E_radial(ell) = E_radial(tilde_ell)/2.

This conversion is separate from division by the reference mass.
The final version states it explicitly rather than saying that the
two sources always use the same annular coordinate.

## Correction to decreasing limits

The former decreasing-limit assertion required only a common lower
bound for terminal parameters. That bound prevents an empty common
parameter interval but does not preserve positive mass.
The corrected statement retains the hypothesis of DXZ Lemma 2.8:
the limiting potential has positive mass at some common interior level.
The proof separates nontriviality, envelope fixedness, and positive mass.

The counterexample uses the existing degree-one P1 hyperplane curve
Lambda. Set phi_j = Lambda_(1-1/j) and form constant-level curves
with initial potential phi_j and common cutoff zero. All are I-model
positive-mass curves, with mass 1/j. They decrease to the Green
potential G_H on every interior level. Since theta+ddc G_H = [H],
the limit has zero non-pluripolar mass and is excluded by (52.6).
This is an elementary consequence of the established example, not
a new research-frontier theorem.

Exact arithmetic checked 12 combinations of reference mass and signed
cutoff, including zero cutoff, for raw/probability energies and radial
rescaling. Six numerical envelope profiles independently confirm the
decrease to log(a_0), and the level masses 1/j were checked exactly.
The proof of zero limiting mass is the current calculation, not the
numerical sampling.

## Exact source record

The [published DXZ article](https://ems.press/content/serial-article-files/50355?nt=1),
Comment. Math. Helv. 100 (2025), 269--322, was checked at equation (5)
on page 279; equation (6) on page 280; equation (10) on page 281;
Lemma 2.4 and Theorem 2.6 on page 282; and Lemma 2.8 on page 283.
The existing key DXZ23 is retained. PDF SHA-256:
`467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`.

The author's [public final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf)
has the July 18, 2026 cover date and 549 pages. The checked locators are
Remark 9.1.1 (page 284), Proposition 9.1.4 (page 288), equation (9.5)
(page 286), Lemma 9.2.1 (pages 290--291), Lemma 9.2.4
(pages 293--295), and Theorem 9.2.1 with equation (9.21) (page 295).
The theorem page was rendered and inspected.
PDF SHA-256:
`c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`.

The supplied local manuscript was checked separately, without editing it:

- author/chapter_testcurve.tex, labels rmk:extendtestcur, prop:Gammaclosed,
  lma:testcurvelegusc, lma:LegendsRtoTC, thm:Legenbij, eq:tcfiniteenergy
  and eq:RWNenergy; SHA-256
  `b39e18f7e00c84916d791b54d8040bf6a2ad9a923f2c8e3497170ca2da7594d0`.
- author/chapter_rays.tex, Section 4.1 annular convention and
  def:radialMAenergy2; SHA-256
  `8820b58006e794e5acf5631449978b21eafef3060e6f689135b4e88dc97e53b6`.

The manuscript retains its bibliography, style and notation. Chapter 62
has only the one-word date correction from August to September in its
closing source note, matching its existing section heading. The 2026
research-claim classifications were not expanded or newly verified.

## Validation and preservation

The initial and second-pass full builds succeeded. After the final
radial-coordinate correction, the full PDF has 3,927 pages and
18,644,548 bytes, with no unresolved reference or citation and no
horizontal or vertical overflow. Final physical pages 3193--3200 and
3203 were rendered and inspected, covering every revised Chapter 52
block and its boundaries. The Chapter 62 source-note date was also
checked in the final PDF.

The actual final edited blocks pass the strict writing audit with
zero errors and zero warnings. The full closure has 389 TeX files
and 11,515 unique labels, with no missing input, duplicate label,
dangling reference or structural defect. The inventory remains
46 active atoms in 14 formal environments, with tiers (0,5,8,16,17).
The second pass checked scalar extended arithmetic, endpoint
noncollapse, measurability, the raw/regularized supremum distinction,
the inverse closed domain, both mass normalizations, both radial
parameters, and the counterexample to the old decreasing-limit scope.

PDF SHA-256:
`f0d099865e2ab1bd20ea83a4de32812d871365f905a035186ec9ff0f0adf18af`

Chapter 52 SHA-256:
`e2767d543b391ab3b295246165852a266377b05dbd6ac627b0ebec46b9cdd80e`

Chapter 62 SHA-256:
`3e868c8797ca563a1654e46bdd704272188bfce54edb9639d909434f1d7fff36`

The Chapter 62 factor-n block retains SHA-256
`204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25`.
The supplied CURVE_PSH.tex and both consulted author chapters
are unchanged. No frozen research packet, verifier record,
bibliography database or dated release artifact was edited.
The current PDF remains an ignored local build artifact.
This is a source and proof audit, not a new production Rethlas gate
or an independent-agent verification. The general relative
correspondence remains an explicit source input.
