# CY volume normalization and mass of interior chamber charts

Date: 4 October 2026. This conditional, book-external derivation supplies
the volume and initial generic-mass inputs of the reduced-SNC analytic
route. It keeps the published arithmetic weights and does not promote a
general CY theorem or any of the 42 open-problem statuses. No independent
verifier or new numerical experiment is claimed.

## Signature and the controlling volume theorem

Let a smooth projective meromorphic degeneration have connected complex
fibres of dimension \(n\geq1\), geometrically integral generic fibre,
and a global meromorphic relative canonical trivialization whose
restriction \(\Omega_t\) is nowhere zero for \(t\ne0\).
Assume a supplied regular projective SNC model
\(\mathcal X_0=\sum_i b_iE_i\), with positive integral multiplicities.
The resulting positive smooth volume \(\nu_t=|\Omega_t|^2\) has analytic
singularities in the model sense. Its normalization

\[
                 \mu_t=\nu_t/\nu_t(X_t)                 \tag{1}
\]

is the probability volume prescribed by the fibrewise CY equation.
Existence, uniqueness, smooth parameter dependence, polarization and the
other analytic inputs of that equation remain separate imports.

Write the relative logarithmic canonical discrepancy as
\(\sum_i a_iE_i\), put \(\kappa=\min_i a_i/b_i\), and let
\(m\) be the dimension of its essential subcomplex. The dyadic application
below requires \(1\leq m\leq n\). Volume convergence itself includes
\(m=0\). Set \(T=-\log|t|\). Boucksom–Jonsson's published Theorem 3.4
and Lemma 3.5, JEP 4 (2017), printed pp. 103–104 / PDF physical pp. 18–19,
give

\[
 \frac{|t|^{-2\kappa}\nu_t}{(2\pi T)^m}
 \longrightarrow
 \Lambda_0:=\sum_{\dim\sigma=m}
       \frac{R_\sigma}{b_\sigma}\lambda_\sigma,
 \qquad
 R_\sigma=\int_{Y_\sigma}\operatorname{Res}_{Y_\sigma}(\psi),
 \quad b_\sigma=\gcd_{i\in J_\sigma}b_i.                 \tag{2}
\]

Here Theorem 3.4 first concerns the model hybrid space. Published
Corollary 4.11, physical p. 28 / printed p. 113, gives the same weighted
formula on the inverse-limit hybrid space; Section 4.6, physical p. 29 /
printed p. 114, identifies its projective central fibre with the
Berkovich space. This supplies the NA hybrid upgrade using the published
normalization. Boucksom, arXiv:2510.10239v2, Theorem 6.6 also records
the volume asymptotic and weak hybrid limit.
The hypotheses and analytic/NA antecedents of these imports are not
freshly proved by this note. In (2), \(\lambda_\sigma\) is integral-affine
Lebesgue measure, not a probability measure. The positive residual
measure has finite mass on each top-dimensional essential stratum.
With its actual integral-affine face volume, put

\[
 Z_0=\sum_\sigma\frac{R_\sigma}{b_\sigma}
                       \lambda_\sigma(\sigma)>0,
 \quad
 w_\sigma=\frac{R_\sigma\lambda_\sigma(\sigma)}{b_\sigma Z_0}.
                                                               \tag{3}
\]

Consequently

\[
 |t|^{-2\kappa}\nu_t(X_t)\sim(2\pi)^m Z_0 T^m,
 \qquad
 \mu_0=\sum_\sigma w_\sigma
                \frac{\lambda_\sigma}{\lambda_\sigma(\sigma)}.
                                                               \tag{4}
\]

Weak convergence of probabilities follows by dividing (2) by its total
mass, using properness over a fixed closed disc. A continuous cutoff
equal to one near the central fibre gives the total-mass limit; all
small fibres lie in that neighborhood. The arithmetic and face-volume
factors in (3) are retained even when a different source denotes
probability Lebesgue measure on each face by \(\sigma_J\).

## One raw volume for both Hilbert estimates

Use throughout the two Hilbert estimates the raw measure

\[
                    \nu'_t=|t|^{-2\kappa}\nu_t.           \tag{5}
\]

It is smooth and positive on each nonzero fibre and has total mass
comparable to \(T^m\). It defines the same probability (1). The scalar
does not require a meromorphic trivialization \(t^{-\kappa}\Omega\):
\(\kappa\) can be rational, and such a trivialization need not exist
over the original parameter field. The model coefficients become
\(a'_i=a_i-\kappa b_i\), which are nonnegative, with zero coefficients
exactly on essential components.

For the degree-\(l\) Hilbert logarithm, the change from \(\nu\) to
\(\nu'\) adds \(\kappa T/l\). The OT/Bergman upper bound therefore
changes its constant by at most \(|\kappa|\). The lower Fourier bound
must use (5) too. This checks the same-measure condition of
`li_uniform_fs_composition_20261004.md`; a probability volume is not
silently substituted into one of the two integrals.

## Local raw and probability comparisons

Fix a top-dimensional essential face with \(|J|=m+1\), and take an
adapted chart around a point in the relative interior of its stratum,
away from all other central components. In coordinates

\[
 t=\prod_{i=0}^m z_i^{b_i},\qquad w\in W\subset\mathbb C^{n-m},
                                                               \tag{6}
\]

all the local discrepancy coefficients \(a'_i\) are zero.
Boucksom's Lemma 6.12, physical p. 37, gives
\(\nu'_t=\rho|\Omega^{\mathrm{log}}_t|^2\) with \(\rho\) smooth,
strictly positive on the model chart, and

\[
 \Omega^{\mathrm{log}}_t
   =\pm b_0^{-1}\,d\log z_1\wedge\cdots\wedge d\log z_m
                         \wedge dw_1\wedge\cdots\wedge dw_{n-m}.
                                                               \tag{7}
\]

This follows by wedging with \(dt/t=\sum_i b_i d\log z_i\).
On a compact transverse polydisc and a fixed interior chamber margin,
the density is bounded above and below. On each root sheet the raw
volume is thus comparable, with fixed multiplicity-dependent constants,
to logarithmic angular/radial volume times ordinary transverse volume.
Summing finitely many sheets retains comparability. Dividing by (4)
gives probability density comparable to \(T^{-m}\) times that volume.
The comparison with the volume of

\[
 g_t=T^{-1}\sum_{j=1}^m |dz_j/z_j|^2+\sum_a|dw_a|^2
                                                               \tag{8}
\]

is uniform, since its real volume has the same \(T^{-m}\) factor.
This comparison permits multiplicities. It does **not** prove the
Poincaré or Fourier steps on a disconnected angular fibre. Those steps
are supplied by the earlier analytic derivation only on a reduced SNC
model; the obstruction and the conditional cover route are recorded
separately in `li_nonreduced_obstruction_and_ramified_descent_20261004.md`.

## Selecting generic charts with almost all probability mass

Fix a degree and hence finitely many chamber-wall hyperplanes in each
of finitely many charts. Let \(\eta>0\). The finite positive measure
in (2) assigns mass zero to face boundaries and these hyperplanes.
Residual measures on the top-dimensional essential strata are finite:
the boundary coefficients in their adjunction formula are strictly
less than one. This is Boucksom's Lemma 6.10 / Definition 6.11, physical
p. 36, and the corresponding published BJ residue construction.

Choose compact transverse sets \(K_J\) in the relative interiors of
these strata capturing all but an assigned small part of the total
weighted residual mass. Inner regularity justifies this even if the
residual density is unbounded near the omitted boundary. Cover the
\(K_J\) by finitely many relatively compact adapted charts. Compact
sets in distinct strata can be given disjoint neighborhoods here;
they lie away from all other components. Choose smooth nonnegative
cutoffs \(\chi_a\) supported inside these charts such that

\[
 \sum_a\chi_a\leq1\text{ on the model},\qquad
 \sum_a\chi_a=1\text{ on the selected }K_J.               \tag{9}
\]

The transverse projections of their supports lie in fixed compact
polydiscs. In every relevant top face choose a finite union
\(\Sigma_a\) of compact polytopes inside chamber interiors, with a
positive distance from face boundaries and walls. The face-volume
discard can be made arbitrarily small, since only finitely many null
hyperplanes and boundaries were removed. The boundary of \(\Sigma_a\)
has Lebesgue measure zero.

The local convergence with cutoffs, not just the global NA weak limit,
is the essential input. BJ Lemma 3.5 gives

\[
 \int_{X_t}\chi_a\,1_{\{\operatorname{Log}_t\in\Sigma_a\}}d\mu_t
 \longrightarrow
 \frac{\int_{Y_J}\chi_a\operatorname{Res}_{Y_J}(\psi)}
      {b_J Z_0}\lambda_J(\Sigma_a).                     \tag{10}
\]

Indicator convergence follows from the local weak convergence and the
null boundary. Equivalently, Boucksom's local Theorem 6.13 gives the
same assertion in its own residual/probability-face conventions, with
its constant \(c_J\) still present. Formula (10) avoids comparing
unmatched residual normalizations across the two sources.

Allocate the residual discard, face/wall discard, and eventual finite
sum convergence error so their total is less than \(\eta\).
For all sufficiently small \(t\), (9)–(10) imply that the union

\[
 V_t=\bigcup_a\{\chi_a>0,\ \operatorname{Log}_t\in\Sigma_a\}
 \quad\text{satisfies}\quad \mu_t(V_t)\geq1-\eta.        \tag{11}
\]

Indeed the integral of the sum of the selected cutoffs is at most
\(\mu_t(V_t)\), and its limit has the prescribed mass. This supplies
compact transverse charts as well as logarithmic chamber margins.
A NA weak limit alone would not control the transverse projection of
the selected complex points.

The finitely many polytope parts can be assigned measurably to their
first chart and chamber. Fixed interior margins make all vanishing
coordinates small, uniformly in the part; the dyadic core cover applies
after shrinking the parameter disc. Its energy and variance discards
must be included in a new total budget. They do not cost zero mass:
starting (11) with a sufficiently small fraction of the final tolerance
leaves the budget required in `li_dyadic_parent_cover_repair_20261004.md`.
Every radius and wall margin here is at a fixed degree and tolerance.
No estimate uniformly up to walls or uniformly in degree follows.

## Printed normalization discrepancy in the recent exposition

The actual PDF physical p. 39 of arXiv:2510.10239v2 prints in Theorem
6.14 the complex central measure \(\sum_J c_Je^{2\Psi_J}\), but the
skeletal measure \(\sum_J(\int e^{2\Psi_J})\sigma_J\), while explicitly
calling \(\sigma_J\) mass-one Lebesgue measure. The local Theorem 6.13
on physical p. 37 retains \(c_J\) in both limits. This is an actual
displayed normalization mismatch, not a lost absolute-value bar in text
extraction. This note uses the published (2), or retains the local
\(c_J\) in both places; it does not use the coefficient-free display.

A local mass check illustrates why the constant need not be one.
For \(t=z_0^b\) with ordinary transverse coordinates and logarithmic
form \(dz_0/z_0\wedge dw\), the relative form is \(dw/b\).
There are \(b\) sheets, each of volume \(b^{-2}|dw|^2\).
The total is \(b^{-1}|dw|^2\), whereas the residual form is \(|dw|^2\).
Thus the local vertex constant is \(1/b\) in these conventions.
This is a local normalization diagnostic, not a counterexample to a
principal connected-family CY theorem. The published arithmetic formula
and the correct local convergence suffice for (4) and (10).

## Scope of the application

The stated global canonical/model input gives the same raw volume for
the two Hilbert inequalities, its \(T^m\) mass normalization, local
logarithmic comparison and almost-full interior chart mass. It also gives
the independent weak hybrid probability limit needed in the conditional
FS-to-MA passage. Uniform Skoda, the geometric/model category, semistable
presentation, punctured-family continuity and the remaining analytic
imports must still be matched to the intended family. A rational scalar
shift is not semistable reduction; a volume comparison is not a
Poincaré estimate. No new book theorem, verifier verdict or status change
is made.
