# Chapter 54: volume continuity and a decreasing mass drop

Audit date: 23 September 2026.

## Proof reconstructed

The proof of Theorem 54.4.1 now distinguishes three limits:
the metric-family index, the initial test-curve level, and the shrinking
Kähler perturbation. The old paragraph incorrectly described the last
interchange as one of two increasing limits.

Write V_omega(Gamma) for the mass of the initial component.
The expanded proof establishes a bound uniform in every metric Gamma:

    0 <= V_(delta omega_0)(Gamma) - vol(Gamma) <= C(delta),
    C(delta) = sum_(a=0)^(n-1) binom(n,a)
               integral_X Omega^a wedge (delta omega_0)^(n-a).

Here Omega >= theta+omega_0 and 0 < delta < 1.
Each term of C(delta) contains a positive power of delta, so this
bound tends to zero independently of the metric index.
The proof uses the previously recorded transition mass identity,
then compares S = theta+omega'+ddc psi to
R = Omega+ddc psi. The difference R-S is a smooth semipositive form.
Mixed mass monotonicity compares R to the smooth representative only
after integration. No unsupported current inequality S <= Omega is used.
The cofinality of the perturbations omega' <= delta omega_0 is explicit.

For an increasing family, regularized suprema over the metric index
and the initial-level parameter commute as suprema of the same psh
family. The resulting initial potentials increase and are bounded by
zero. The fixed-background d_S convergence and mass-continuity
theorems are cited precisely. The final inequality

    vol(sup_i Gamma^i) <= sup_i vol(Gamma^i) + C(delta)

justifies passage to the perturbation limit. Translation and positive
scaling are also checked at the initial level, with the perturbation
scaled by lambda^(-1).

## Strict decrease with positive limiting volume

The new projective-line example uses the already computed hyperplane
test curve Lambda, whose level s has mass 1-s for 0 <= s <= 1.
For 0 < a < 1 set

    Gamma^j_tau = Lambda_(a(1+tau/j)) for tau <= 0,
    Gamma^j_tau = -infinity for tau > 0.

Affine parameter change and the closed terminal cutoff give I-model
test curves. Every nontrivial level has mass at least 1-a.
The curves decrease in j, have common terminal parameter zero, and
vanish for tau <= -j. Thus every initial mass is 1.
At each fixed finite tau <= 0 the levels converge to Lambda_a,
so the limit is a constant test curve with initial mass 1-a.
The fixed-class positive-mass limit theorem and its transition
compatibility place the same example in the full inverse system.
Hence the strict inequality is 1-a < 1, even with positive-volume limit.

The mass profile 1-a max(1+tau/j,0) displays the two noncommuting
iterated limits explicitly. This is not the earlier zero-mass
noncollapse counterexample: it concerns the initial-level supremum
within a fixed positive class.

The second mathematical pass checked the parameter order, concavity,
closed cutoff, all interior masses, the initial levels, both limits,
the positive-mass embedding and the source/target class in rescaling.
Independently, the hyperplane profile is constant for s <= r and has
second s-derivative -1/(s(1-s)) for r < s < 1; the first derivatives
match at s=r. This confirms the concavity used in the construction.
The conclusions use exact formulas, not numerical sampling.

## Precise primary sources

The author's supplied chapter_NApotential.tex,
chapter_testcurve.tex and chapter_comp.tex were read without alteration.
Exact locators were checked against the author's
[final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
dated 18 July 2026:

- Corollaries 6.2.4 and 6.2.5, page 210: increasing convergence in d_S
  and continuity of nonpluripolar mass in d_S.
- Proposition 9.4.3, pages 316--317: the increasing test-curve
  supremum and its initial-level identity.
- Proposition 13.2.13, pages 430--431: increasing continuity of volume
  and the uniform Kähler-perturbation estimate.
- The paragraph following Definition 13.2.6, page 431: the decreasing
  volume inequality and failure of its reverse in general.

Physical source pages 226, 332--333 and 446--447 were rendered and
inspected. Corollary 6.2.5 is the mass-continuity input here; it is not
confused with the different I-volume theorem numbered Theorem 6.2.5.
The new precise citations use XiaBook. The separately versioned
operations-paper bibliography entries were not changed.

The general d_S and nonpluripolar-product results remain source inputs.
This unit reconstructs their application and supplies an elementary
worked example; it asserts no new research-frontier theorem or priority.

## Validation and preservation

The full build succeeds with 3,933 pages and 18,677,443 bytes.
The 389-file TeX closure has 11,531 unique labels, with no missing input,
duplicate label, dangling reference or structural defect.
There are no unresolved references or citations and no horizontal or
vertical overflows; the pre-existing class-name warning remains.
The actual edited block passes the strict writing audit with zero errors
and zero warnings. Physical pages 3222--3226 and 3229 were rendered
and inspected, including the full new proof, example, following section
and final source note. The final prose pass was rebuilt; all inspected
pages except page 3224 match the prior rasters byte for byte, and that
changed page was re-inspected.

The active research inventory remains 46 atoms in 14 formal environments,
with tiers (0,5,8,16,17). No research-atom closure is claimed.

PDF SHA-256: 8883972b1c865088be3aa3e99b8d7f1bbd5d0730554822e9cfc027831396e077

Chapter 54 SHA-256: b60653fb0995258409d3532aca09729a102d32f2c8f220afb4eec639f0cbb192

Source PDF SHA-256:
c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706

Read-only source and recovery checksums:

- chapter_NApotential.tex: 81dc584fdf60b7907551f6d2b1493fb740594bf94b27b2092ffd8df7f53516d1
- chapter_testcurve.tex: b39e18f7e00c84916d791b54d8040bf6a2ad9a923f2c8e3497170ca2da7594d0
- chapter_comp.tex: c8cb2b9c6cbcc9a1b6965f23802eaed6891fcc23b965163a37a227e53497f7cb
- CURVE_PSH.tex (both copies): 9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9


Only Chapter 54 and the current editorial progress records were changed.
The supplied author sources, CURVE_PSH.tex and its recovered copy,
frozen proof packets, production verifier records, research classifications
and dated release artifacts were preserved. The current PDF is an
ignored local build artifact.
This is a local mathematical/source/style/build/visual audit, not an
independent-agent or production Rethlas verification.

The next bounded audit checks the analytic trace construction in
Chapter 54: its natural domain, common target background and precise
source for independence of the chosen approximation.
