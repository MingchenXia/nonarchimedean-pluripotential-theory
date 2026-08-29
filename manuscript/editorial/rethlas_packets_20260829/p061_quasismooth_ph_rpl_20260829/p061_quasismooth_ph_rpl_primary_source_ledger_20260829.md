# P06.1 primary-source citation ledger

Date: 29 August 2026

This ledger records the exact source versions and the claims imported by the
quarantined packet. The PDF hashes refer to the files actually inspected for
this audit; they are not generated from the live bibliography.

## 1. Gubler--Rabinoff: classical psh and pluriharmonic functions

Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
functions on Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025,
[arXiv 2506.13548](https://arxiv.org/abs/2506.13548).

- Inspected PDF SHA-256:
  83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726.
- Definition 4.1: a classically psh function is upper semicontinuous and
  becomes subharmonic after every analytic ground-field extension and every
  morphism from an analytic curve.
- Definition 7.1: $h$ is pluriharmonic exactly when $h$ and $-h$ are
  classically psh.
- Proposition 7.2 first asserts that pluriharmonic functions are continuous.
- Proposition 7.2(2),(3): $\log|f|$ for an analytic unit is pluriharmonic,
  and pluriharmonic functions form a real vector space.
- Proposition 7.2(6): pluriharmonicity is equivalent before and after an
  arbitrary analytic extension of the ground field.
- Proposition 7.2(7): pluriharmonicity pulls back under every analytic
  morphism; the converse is asserted when the morphism is finite and
  surjective. The packet uses only the arbitrary-pullback direction for
  Temkin's cover.
- Theorem 4.3: on a good strict space over a nontrivially valued field, an
  $\mathbf R$-PL function is classically psh exactly when it is semipositive.
- Proposition 7.8: on a good, quasicompact, strict analytic space possessing
  a strictly semistable formal model, every pluriharmonic function is
  $\mathbf R$-PL.
- Section 4.1.2 and Proposition 3.15: on every strict analytic curve,
  classically pluriharmonic equals harmonic and is $\mathbf R$-PL. This
  already settles the full one-dimensional strict scope.

Source caveat: the proof of Proposition 7.8 writes the coordinate range as
$i=0,\ldots,d$, although only the node coordinates $i=0,\ldots,r$ are
guaranteed to be units in the displayed semistable chart. Those $r+1$
coordinates already give affine coordinates on the $r$-simplex and are
sufficient for the proof. The packet imports the proposition and does not
use the surplus-coordinate wording.

The live bibliography entry GR25Classical is an arXiv entry and agrees with
this title, author pair, year, and identifier.

## 2. Gubler--Jell--Rabinoff: real PL descent and harmonicity

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich spaces
based on harmonic tropicalizations*, *Bulletin de la Société Mathématique
de France* **154** (2026), no. 1, 135--238,
[doi:10.24033/bsmf.2919](https://doi.org/10.24033/bsmf.2919).

- Inspected published PDF SHA-256:
  acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c.
- Definition 5.1: $\Lambda$-PL means G-locally a finite sum
  $\sum_j\lambda_j\log|f_j|$, with $\lambda_j\in\Lambda$ and analytic units
  $f_j$.
- Section 5.2(4): $U\mapsto\operatorname{PL}_\Lambda(U)$ is a sheaf for the
  G-topology.
- Lemma 5.4(1),(2): PL functions pull back under morphisms and ground-field
  extensions.
- Proposition 5.11: if $f:X'\to X$ is finite, flat, and surjective and
  $\Lambda$ is divisible, then a function on $X$ is $\Lambda$-PL exactly
  when its pullback is. Flatness and constant local rank are used in the norm
  proof; this is not a theorem for arbitrary quasi-$\acute{e}$tale maps.
- Corollary 5.12: the same equivalence holds after passing to the completion
  of an algebraic extension of the ground field.
- Definition 7.2: an $\mathbf R$-PL function is harmonic when both signs
  are semipositive.

The packet uses the numbering in the published 2026 article. The older
preprint numbers the finite-flat and field-descent statements differently.
The live bibliography entry GJR26 agrees with the published metadata and
DOI above.

## 3. Temkin: altered local uniformization

Michael Temkin, *Altered local uniformization of Berkovich spaces*,
*Israel Journal of Mathematics* **221** (2017), 585--603,
[doi:10.1007/s11856-017-1557-0](https://doi.org/10.1007/s11856-017-1557-0),
[arXiv:1503.05729](https://arxiv.org/abs/1503.05729).

- Inspected author-final PDF SHA-256:
  eba2269c2c7e1ca7300ababccbed1f9f82359986a3a73a5ff8df0fa99961c03e.
- Section 3.3 defines a strictly semistable formal $k^\circ$-scheme by
  formal charts $\acute{e}$tale over
  $\operatorname{Spf}(k^\circ\{t_0,\ldots,t_l\}/(t_1\cdots t_m-\pi))$.
- Corollary 3.3.2: for a smooth quasicompact quasiseparated rigid space $U$
  over a complete real-valued field $K$, there are a finite $L/K$ and an
  $\acute{e}$tale covering $V\to U\otimes_KL$, with $V$ affinoid and
  possessing a strictly semistable affine formal $L^\circ$-model.
- Section 3.4: the rigid--Berkovich equivalence matches smooth with
  quasi-smooth and $\acute{e}$tale with quasi-$\acute{e}$tale.

The packet deliberately cites Corollary 3.3.2. The Berkovich translation in
Theorem 3.4.1 says that the maximal affine formal model is semistable; that
wording is not substituted for the strict model explicitly furnished by the
corollary.

## 4. De Jong--van der Put: the rigid étale sheaf criterion

A. Johan de Jong and Marius van der Put, *Étale cohomology of rigid analytic
spaces*, *Documenta Mathematica* **1** (1996), 1--56.

- Inspected journal PDF SHA-256:
  34a0f015eafeb3f418bca39378206aea0d1935acb2529ccc1d1913136a2217d4.
- Section 2.1 states that the special rigid G-topology used in the paper and
  the strong rigid G-topology have the same category of sheaves. Thus the
  G-sheaf input is not changed when Proposition 3.2.2 is applied.
- The definition immediately before Lemma 3.2.1 says that an
  $\acute{e}$tale family is a covering when the images of affinoid source
  coverings form an admissible G-cover of the target.
- Proposition 3.2.2: a presheaf on the rigid $\acute{e}$tale site is a
  sheaf if and only if (i) its restriction to the rigid/G-site of every
  object is a sheaf and (ii) the Čech equalizer is exact for each surjective
  finite $\acute{e}$tale morphism of affinoids.
- The proof factors the local pieces of a general $\acute{e}$tale cover as
  open immersions into finite $\acute{e}$tale maps and inducts on the finite
  degree. Thus no direct finite-flat refinement of Temkin's entire
  quasi-$\acute{e}$tale Berkovich map is required.

## 5. Thuillier: the local integral-slope input

Amaury Thuillier, *Th\'eorie du potentiel sur les courbes en g\'eom\'etrie
analytique non archim\'edienne. Applications \`a la th\'eorie d'Arakelov*,
doctoral thesis, Universit\'e Rennes 1, 2005, HAL tel-00010990.

- Inspected PDF SHA-256:
  fc947ea783e4680741ec23d6b9586f69e17081b9fc3b0a8d507ca9f7a3eb7a1c.
- Proposition 2.2.24(i) is the integral Newton-polygon statement on a
  strictly semistable analytic curve: the restriction of the logarithmic
  norm of an analytic function to the skeleton is integral piecewise affine.
  Its local form, after local semistable reduction, applies to an analytic
  unit along a geodesic interval in a quasi-smooth analytic curve.  The
  packet uses only this integral-slope conclusion.

## Claims proved inside the packet

The following bridges are not taken on faith from the four sources.

- Equal pullbacks of a real PL function through a finite $\acute{e}$tale
  fibre square imply constancy on every Berkovich fibre; the proof
  constructs the required fibre-square point by embedding the two finite
  separable completed residue-field extensions in a common finite complete
  valued field and putting the resulting multiplicative
  seminorm on their completed tensor product.
- The fibre-constant function is continuous because a finite surjective map
  between Berkovich affinoids is a compact-to-Hausdorff quotient map.
- The irrational multiple $\sqrt2\log|T|$ on a strict annulus is not
  $\mathbf Q$-PL. From a hypothetical admissible PL cover, affinoid
  quasicompactness gives a finite affinoid subcover. The closed intersections
  of its members with the compact skeletal interval form a finite closed
  cover, so one contains a nondegenerate subinterval. Laurent expansions
  and analytic-stalk extension are not used.  Thuillier's local
  integral-slope theorem gives integral slopes for the logarithmic norms of
  the units directly on that subinterval, hence a rational slope for every
  $\mathbf Q$-PL function, contradicting the slope $-\sqrt2$.
