# Research status for the general non-Archimedean Monge–Ampère family

**Outcome:** all P16.1–P16.7 are unresolved in this deliverable. No complete
solution or new narrower equation theorem is claimed. There is no
P16.y.tex or P16.y-partial.tex, because a diagnostic obstruction to one
proof strategy is not a solution paper. status.json has exactly one record
per atom, with proof_file=null for each. Complete arguments for the useful
diagnostics are in diagnostic-argument.md and are summarized below.

## Scope discipline

The full input, including common notation, all seven target statements,
known endpoints, bibliography, and completion criteria, was read and is
preserved as input.json and task-input.md. A claimed solution would need
the finite-energy operator, correct mass and measure-energy domain,
existence, uniqueness modulo constants, and replacements for compactness,
envelopes, energy differentiation, and comparison in that atom's residual
scope. None of those packages has been proved here outside the established
settings. An example showing a particular proof step fails is not a
counterexample to every possible theory sought by an atom.

The psh class used in the positive diagnostic calculations is precisely
the BFJ smooth, ample, discretely valued residue-characteristic-zero class
on P^1 over C((t)). The zero-volume calculation uses ordinary nef
semipositive *model metrics*, with their actual algebraic intersection MA
measure; it does not assume a completed nonample E^1 theory. No CLD
current positivity, classical psh recognition, ordinary CLD smoothness,
weak smoothness, or Banach inverse measure is substituted for those
classes or operators.

## Primary-source audit and limitations

The local primary BFJ file *Singular semipositive metrics in
non-Archimedean geometry* was read directly, including its introduction,
field/variety hypotheses, model-metric conventions, and Section 7. It
states psh compactness and decreasing regularization for a smooth
projective analytic variety with an ample line bundle over a complete
discretely valued field of residue characteristic zero. In particular,
Theorem 7.10 makes the normalized psh space compact and gives the topology
of pointwise convergence at divisorial points; Proposition 7.5 makes the
evaluations there finite. These exact statements are quoted and checked
in diagnostic-argument.md. The local PDF's version header and internal
date differ; the exact bytes and both dates are recorded rather than
silently identifying it with a different published version.

The local general-NA-MA and PS23 packets, reference-pack manifest, and book
Chapters 28–29 were also read as secondary context. The manifest names
primary PDFs for PS23, BFJ's equation paper, GJKM, FGK and other sources,
but those named primary files are absent from this checkout, as an
unignored recursive inventory confirms. A direct fetch of
arXiv:2209.04879v2 failed with `URLError: ... Operation not permitted`.
Its command, URL, failure, and environment are retained. The named
source-dependent endpoint assertions in the catalogue have therefore not
been independently established here. In particular:

* PS23 Remark 4.4 is available here as a catalogue/secondary-packet report
  about the arbitrary-field E^1 operator, not as directly checked primary
  text. A definition of E^1 does not prove the operator or its inverse.
* The GJKM and FGK packet reports retain geometric-origin and resolution
  hypotheses in positive or mixed characteristic. The primary statements
  were unavailable, so no precise additional theorem is imported from
  them into an argument here.
* BGGJK25's invariant toric singular endpoint, BJ24b's nonfactorization
  examples, Fang25's inverse equidistribution metric, Wang25's affine
  local solution, and MPWN25's transcendental theory are treated only as
  the supplied catalogue reports. There is no claim to have independently
  verified or transported them to an active residual scope.
* The Stacks proper-plus-ample statement is catalogue-reported. Nothing
  here treats keeping an ample algebraic L and dropping projectivity as
  a nonprojective extension.

This was a local-source investigation, not a complete post-2020 literature
search. No claim that a theorem is absent from all literature is warranted
by this restricted source audit. The primary psh input is sufficient for
the finite-atomic diagnostic, but does not itself give a finite-energy
equation theorem. The source-audit and the mathematical gaps are distinct:
obtaining absent PDFs would improve the survey, while it would not by
itself supply missing new proofs.

## Failed approach A: weak approximation of arbitrary measures (P16.6)

The proposed route was to approximate a general finite-energy measure by
finite model/skeletal measures, solve those equations, and use compactness
to pass to a solution. Two quantitative facts are required: bounds keeping
the potentials in an energy superlevel, and convergence of the measure
pairings in the correct topology. Weak convergence of measures supplies
neither by itself.

Here is an actual analytic diagnostic. Over K=C((t)), v(t)=1, let x_s on
P^1 be the Gauss point of the zero-centered disc of radius exp(-s), and
x_0 the good-reduction point. Set

    u_k=-(1/k)min(max(v(T),0),k^4),
    nu_k=(1-1/k)delta_x0+(1/k)delta_x(k^4).

At T=0 use the bounded value -k^3; at infinity use zero. These are
continuous semipositive rational model metrics on O(1), not formal inverse
measures. On the N=k^4 successive-blowup model of P^1_R the special fiber
is a reduced chain C_0,...,C_N. The vertical coefficients are u_i=-i/k;
M.C_i has degrees 1-1/k at C_0, 1/k at C_N, zero elsewhere. Therefore
the *genuine* model MA equals nu_k, of raw mass 1.

The intersection matrix gives D^2=-k^2 and L_0.D=0. Thus

    E(u_k)=-k^2/2,
    int u_k dnu_k=-k^2,
    E^vee(nu_k)>=E(u_k)-int u_k dnu_k=k^2/2.

Every nu_k has finite dual energy: on compact normalized BFJ PSH, its two
divisorial evaluations define a finite continuous pairing with a finite
lower bound; normalized potential energy is <=0. But
||nu_k-delta_x0||_TV=2/k tends to zero. Thus even total-variation
convergence of positive correct-mass finite-energy measures need not give
a uniform bound for dual energy. In the convention that TV *distance* is
half the norm this distance is 1/k. The limit delta_x0 has the reference
solution u=0, so this is not nonexistence. It is a counterexample only to
the proposed inference from weak approximation to energy bounds.

These finite measures each have skeletal support in the known baseline.
No part of this result removes the arbitrary-support residual scope, and
no novelty for the standard curve computations is claimed. checks.py
checks the intersection matrix, nonnegative component masses, raw mass,
energy and pairings for k=1,2,3,4 using exact rational arithmetic. The
written proof supplies the result for every integer k, independently of
those finite executions.

A related harmonic-chain exploration was worked out fully at the model
and potential-energy level. Put u_i=-H_i on the N-chain. It has component
masses 1/[i(i+1)] for 1<=i<N and 1/N at i=N, energy
-sum_{i=1}^N(1/i^2)/2, and a decreasing psh limit u with finite
infimum-defined energy -sum_{i>=1}(1/i^2)/2. Its explicit candidate
limiting measure is mu=sum_{i>=1}delta_xi/[i(i+1)], approached in TV norm
2/(N+1). Tonelli gives int(-u)dmu=sum_i1/i^2<infinity, whereas
-int g_N dmu=H_N grows without bound for the normalized continuous psh
tests g_N=-min(max(v(T),0),N). Consequently the stronger bounded-pairing
condition on all PSH_0 does not hold for this measure.

The argument has a deliberate stopping point: it does not independently
identify mu with a genuine *extended* MA(u), or prove finiteness of
E^vee(mu) for the entire psh cone. A finite ray-restricted supremum has
fewer tests and cannot establish the full dual statement. Those claims
would require extra baseline operator inputs or a separate full proof.
There is no use of a ray measure as a replacement inverse MA operator.

## Failed approach B: direct variational maximization (P16.6 and others)

With fixed positive raw mass V and reference E(0)=0, the variational
functional is F_mu(phi)=E(phi)-int phi dmu, invariant under constants
only if mu(X)=V. Finite dual energy gives

    F_mu(phi)<=E^vee(mu),
    -int phi dmu<=E^vee(mu)-E(phi).

Combining the second inequality with the definition of F_mu cancels the
coefficient of E(phi); it gives no lower bound on energy of a maximizing
net. It is therefore invalid to turn boundedness of the supremum directly
into compactness inside an E^1 superlevel.

Even if a normalized psh compactness theorem is available, attainment of
F_mu needs its own semicontinuity. An upper-semicontinuity bound for the
integral has the wrong sign after subtraction. Uniform convergence on
each one fixed skeleton permits integral convergence for a measure
supported there; it does not permit integration over arbitrary support
without a dominating or uniform-integrability argument. Such an argument
has not been proved here. All general compactness statements would have
to be used with nets; no cofinal sequence of models or metrizability is
assumed. The explicit sequences in the curve diagnostics are prescribed
families and do not replace general nets.

Finally, differentiating along phi+t f is not justified merely because
phi is psh: that affine perturbation need not remain psh. An envelope
P(phi+t f) and an energy first-variation statement for it, with all its
orthogonality and regularity hypotheses, would be needed. Neither
Euler–Lagrange identification nor uniqueness is obtained just by naming
the functional. A strong completion of measures is not yet a theorem
identifying its points with pointwise E^1 potentials.

## Failed approach C: retaining raw top-degree uniqueness at volume zero (P16.5)

The most concrete negative diagnostic lies in a zero-volume nef class.
Let X=P^1_K x P^1_K and L=pr_1^*O(1), still over C((t)). This is smooth
and projective; L is nef and pseudoeffective, nonample, with L^2=0 and
vol(L)=0 since h^0(L^m)=m+1. Use two model metrics: the good product
reference eta_0, and eta_1 obtained by pulling back from the first factor
the one-blowup curve metric with potential

    g_1=-min(max(v(T),0),1).

On the first curve model the adjusted bundle L_0-C_1 has degrees 0 and 1
on C_0 and C_1. On the product special components C_i x P^1 its
restrictions are nef pullbacks from C_i. Their squares are zero, so the
actual degree-two intersection MA of eta_1 is zero, as is that of eta_0.
The weights differ by g_1 composed with pr_1, which has values 0 and -1
at explicit product Gauss points. They are not related by a constant.
Their bounded difference also puts them in the same usual bounded
singularity-equivalence class.
All degree-two mixed measures between the two also vanish, so the usual
relative finite model energy of each is zero.

This supplies a genuine analytic counterexample to the *specific*
combination “retain raw top-degree MA, include every continuous
semipositive model metric, and require uniqueness modulo constants at
zero volume.” A positive measure of raw mass zero is zero; dividing it
by volume is undefined. It does not refute the atom, which allows a new
zero-volume convention, nor does it construct a general big nonample
theory. Reference singularity choices do not by themselves prove a
correct replacement, and a proposed restriction or additional quotient
must be stated and justified. This is standard degeneracy, not a claimed
new theorem deserving a partial solution paper.

## Failed approach D: resolve or normalize and descend (P16.1)

Pulling an ample bundle back to a resolution need not keep it ample. If
an exceptional complete curve C maps to a point, f^*L restricts trivially
to C, with degree zero. Already a point blowup of P^2 shows this. Thus a
smooth ample-polarized theorem cannot simply be applied to the pullback;
a big nef nonample theory on the source would be another unproved input.
There is then a separate descent problem for potentials, measures,
energy and their comparison/rigidity properties.

A finite normalization avoids that particular pullback issue, but not
the section/metric descent problem. The exact characteristic-zero cusp
example R_cusp=K[z^2,z^3], normalization B=K[z], has one normalization
point with unchanged residue field over the origin. For every m>=1,
(1+z)^m has nonzero coefficient m of z, and hence is outside R_cusp.
No positive power descends. This disproves an attempted descent rule
that takes a power of each normalization section; it does not rule out
norm/max constructions or approximations of the metric. Those latter
constructions would need their own proofs of the relevant psh and
finite-energy properties. Unibranchness cannot silently be supplied to
a many-branch singular target, and the cusp argument is not an analytic
MA nonexistence example.

## Failed approach E: Frobenius or alterations alone (P16.3)

In the same cusp ring in characteristic p, (1+z)^p=1+z^p does descend.
The contrast makes a limited algebraic power argument plausible in
purely inseparable situations. It supplies no replacement for the
multiplier-ideal, resolution/model-regularity, or envelope
differentiability inputs actually consumed by a variational theorem.
This is an equal-characteristic calculation; positive residue
characteristic does not make the same identity valid in a
mixed-characteristic ground field of characteristic zero.
An alteration can change the model and polarization, and descent of a
semipositive cone does not imply that mixed limiting measures commute
with it or that the energy derivative descends. No such analytic
replacement is proved in this draft. Secondary-reported positive- or
mixed-characteristic theorems with resolution hypotheses cannot be
relabeled unconditional; their unavailable primary texts are an
additional source-check limitation.

## Failed approach F: scalar extension to a discrete field (P16.4)

An isometric valued-field inclusion K->F includes v(K^*) into v(F^*).
If the latter is a Z for a>0, every nonzero subgroup is ma Z for a
positive integer m, hence discrete. Therefore nondiscrete K cannot have
a discretely valued isometric extension. The completion of the
compatible Puiseux union of C((t^(1/m))) has value group Q: all rational
values are present, and a nonzero completion limit has the same norm
as a sufficiently close term. Its values 1/m exclude discreteness in
every isometric extension. A change-of-fields approximation is a
different operation requiring new estimates and descent results.
No arbitrary-field operator follows by scalar extension of a theorem
whose hypothesis is discrete valuation.

Constructing model measures or defining an infimum energy over K does
not resolve approximant independence, mass tails, mixed products,
integration by parts, first variation, or the equation. The invariant
toric skeletal endpoint described in the input remains distinct from
these missing full-operator requirements.

## Failed approach G: remove projectivity or algebraizability while keeping local data (P16.2, P16.7)

For P16.2 the input's proper-plus-ample restriction prevents a purported
extension that simply deletes “projective” from an ample-polarized
algebraic theorem. A replacement positivity datum on a proper
nonprojective algebraizable example has not been supplied here. A local
CLD positive Hessian, a formal model on a chart, or a real Bott–Chern
class in a complex transcendental theory is not automatically such a
datum on a Berkovich space over the given K. Its psh cone and energy
would have to be defined and their compactness, envelopes, mass and
comparison proved.

For P16.7 no genuinely nonalgebraizable analytic example carrying a
verified global equation framework was obtained. Local positive
Hessians give no automatic wedge products of unbounded weights, and
gluing local potentials does not automatically fix a global reference,
mass or comparison principle. No assertion that a zero-Hessian equation
pulls back through arbitrary maps is made. Ordinary CLD smoothness and
weak smoothness are kept distinct. The affine nonproper endpoint
reported in the catalogue cannot solve the proper nonprojective axis;
the Fang inverse measure cannot be relabeled genuine MA. No attempt
here replaces arbitrary support by one skeleton.

## What would be needed next

For P16.1, prove psh/model-metric descent and energy/MA functoriality
with a valid polarization on the source; for P16.3, give analytic
envelope and regularity replacements in the residual characteristic
scope; for P16.4, construct an approximant-independent mixed operator
and its mass/first-variation/descendability properties. P16.6 needs
genuine potential completion or another attainment proof with correct
pairing control, followed by rigidity. P16.5 needs a full reference
singularity and mass convention, distinguishing positive-volume big
classes from zero-volume degeneracy. P16.2 and P16.7 first need an
explicit admissible positivity datum in an actual example of their
respective domains, and then the entire equation framework. None of
these missing statements is being assumed as an extra conditional
hypothesis to count an atom solved.

## Files, commands and evidence

Run `python prepare_sources.py`, `python checks.py`, and
`python validate_artifacts.py` in the provided workspace. README.md gives
the artifact map; commands.log retains the decisive commands and observed
exit results. source-audit.json records source snapshots, exact byte
hashes and absent named primaries. environment.json records execution
details without credentials. checks-output.json gives the exact finite
outputs, and validation-output.json checks artifact/schema consistency.
The validator also writes artifact-manifest.json with output hashes.
These are reproducibility checks, not independent proof verification.

Only small local rational calculations were performed. No operator-provided
supervised compute service was exposed to this worker, so no resource-heavy
computation was launched. The requested Xean source and authentication
were not changed, and no runtime routing change is claimed.
