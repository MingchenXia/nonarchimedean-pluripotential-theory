# P14.8 v4 source package

## Attached primary sources

The review packet attaches these exact local source copies as proof
dependencies:

| Source | SHA-256 |
| --- | --- |
| S. Boucksom, *Singularities of plurisubharmonic functions and multiplier ideals* | `4a3fa01a21b1cc66fe174460732fe80a29914f26279c04d2824223fc7d9ab0a4` |
| S. Boucksom, P. Eyssidieux, V. Guedj, A. Zeriahi, *Monge--Ampère equations in big cohomology classes*, arXiv:0812.3674v2 | `890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7` |

## Interfaces used

1. Boucksom, Lemma 2.6: for an increasing sequence of psh functions
   converging almost everywhere to a psh limit, point Lelong numbers decrease
   to the Lelong number of the limit. Boucksom, Lemma 10.5 permits a very
   general point of a prime divisor to compute each generic Lelong number in a
   countable family. Together with Choquet's lemma, these give the
   increasing-envelope step in the proof.

2. Boucksom, Corollary 10.18: multiplier-ideal membership is characterized
   by the divisorial Lelong profile and log discrepancies. Applying it to
   every positive integral scaling shows that equal divisorial profiles give
   equal multiplier-ideal towers. Conversely, the analytic-approximation
   inequalities used in the proof of Theorem 10.13 give the correct
   discrepancy-dependent squeeze
   $\nu_E(\varphi)\ge m^{-1}\operatorname{ord}_E\mathcal I(m\varphi)
   \ge\nu_E(\varphi)-A(E)/m$; equality of the full towers therefore gives
   equality of profiles.

3. BEGZ, Section 1.2 and Proposition 1.4: the degree-one nonpluripolar
   product is well-defined, local where the potential is locally bounded, and
   gives no mass to pluripolar sets. Those are the only nonpluripolar-product
   properties used in the curve computation.

4. The generalized-Cantor logarithmic-capacity criterion used in the explicit
   construction is the classical criterion cited in the candidate as
   Carleson, *Selected Problems on Exceptional Sets*, p. 31. The proof uses
   only the displayed divergence calculation and the resulting polarity.

## Deliberate exclusions

This packet does **not** use a pointwise $n/m$ estimate for divisorial
valuations, global truncation positivity for arbitrary smooth backgrounds,
levelwise truncation multilinearity or closedness, unrestricted mixed-mass
monotonicity, or a one-sided $\mathcal I$-preorder equivalence. Those were
the unrelated defective supporting claims in the rejected v3 dependency.
