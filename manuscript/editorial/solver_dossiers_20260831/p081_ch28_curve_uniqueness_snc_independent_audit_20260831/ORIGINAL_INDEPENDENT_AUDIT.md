# Independent audit of the original Ch28 SNC uniqueness proof

31 August 2026. Auditor: p213_skeletal_hostile.

## Scope and original-byte verdict

The new intersection-theoretic argument is mathematically sound under the
stated original BFJ signature: complete DVR, residue characteristic zero,
smooth connected projective curve, and semipositive real closed model form
with ample generic class. It avoids the false claim that reduced semistable
models are cofinal over the original field.

The ORIGINAL exact proof nevertheless has a source-hypothesis interface
that should be made explicit before scope-complete acceptance: Ch05's
standing convention at line 59 says geometrically connected, whereas Ch28
assumes only connected. Its citations to Ch05 cofinality and density cannot
silently erase that extra standing hypothesis. The required extension is
valid; a separate exact revised1 addendum in this directory checks its
primary-source justification. Thus this original report records correct
core mathematics and a repairable scope-interface omission, not a final
production acceptance of the original proof bytes.

I am independent of the root-authored uniqueness proof, but I authored the
earlier weighted-energy proposal used as the copied chapter baseline.
Accordingly this report does not independently certify that baseline's
mathematical changes. It audits the new uniqueness proof, its unchanged
proposition, the cited interfaces, and exact assembly isolation only.

## Exact original input

Author directory:
p081_ch28_curve_uniqueness_snc_repair_20260831 under
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831.

- uniqueness_proof.tex, 3917 bytes, SHA256
  d7f5c93d3bdb0d747a537122d656ad4cdf4a158553bf9c11756d72cdf1682e9a.
- patched/ch28_finite_energy_measures.tex, 177263 bytes, SHA256
  8c27a6812bf18c9a664a74494ecbcc0ccf7fa10c6f0b2e6f949d691cc8e56106.
- chapter.patch, 31373 bytes, SHA256
  e9eae955c84096c2eafca3d9ddc49659f64edaff544999cecda6d3e5e09e07c5.
- MANIFEST.json, 2487 bytes, SHA256
  1210a9ce790d504df5e4346c477a78b63e507781239068ed6011cbd4f6bd13a3.

All eight author-manifest entries were independently rehashed and
size-checked with zero mismatches. The exact source-interface hashes and
the full results are in VALIDATION.json and this audit's MANIFEST.json.

## Proposition and admissible inputs

The unchanged proposition prop:ch28-curve-uniqueness, live lines 2147--2154,
assumes continuous phi,psi in E1 and equality of their Monge--Ampere measures.
The standing hypotheses at live lines 58--80 supply ordinary connectedness,
the original BFJ field regime, and a semipositive real model reference of
ample class. No support restriction on the common measure is needed for
this uniqueness assertion. No existence assertion is being proved.

Continuity on the compact analytic curve makes both functions finite and
bounded. E1 functions are psh, and their nonpluripolar measures agree with
the bounded measures: for a bounded potential the truncation defining the
nonpluripolar measure is eventually the potential itself. This interface
is also stated and proved in the unchanged Ch26
prop:ch26-npp-basic, lines 1789--1810. It does not use the new Ch26 graph
construction that I authored.

The term "real model function" is important. D_U below is a real Cartier
divisor; it need not be a rational divisor or define a Q-formal metric.
The manuscript's real model-function space permits precisely this finite
real linear combination. No value-group membership or rational-slope
realization is required to choose this test function.

## Step-by-step hostile check

### 1. Passing equality of measures to every model test

Original proof lines 7--25 use Ch24 prop:ch24-continuous-uniform.
Its actual statement at Ch24 lines 2060--2124 supplies uniform real-model
approximants and weak convergence under the matching BFJ hypotheses.
The selection interface in Ch22 cor:ch22-continuous-decreasing-sequence,
lines 2972--2994, was read with its proof. This is a sequence selected from
the regularizing directed family by uniform error; it is not an assumption
that the set of models has a countable cofinal subsystem.

For a fixed arbitrary real model function h, Ch24 model integration by
parts applies without requiring h to be psh. In dimension one,
MA(phi_j)-MA(psi_j)=ddc(phi_j-psi_j), because the reference terms cancel.
Integration by parts then gives the displayed identity.

The measure ddc h is fixed, finite, signed, and atomic. Uniform convergence
of phi_j-psi_j therefore implies convergence of its integral, bounded in
error by total_variation(ddc h) times the uniform error. On the other side,
h is continuous, so weak convergence and equality of the limiting
Monge--Ampere measures give zero. This proves integral u ddc h=0 for every
real model h. There is no unjustified passage to a distributional
Laplacian of an arbitrary continuous function and no integration against a
moving signed measure.

The relevant Ch24 model-measure and integration-by-parts statement/proof
interfaces, lines 468--530 and 798--849, were read in full at the portions
used. They expressly retain the component factor b_E.

### 2. Turning the continuous function's vertex data into one model test

On any regular SNC model determining omega, set U_i=u(x_Ei) and
D_U=sum_i b_i U_i E_i. The finite values U_i are allowed real coefficients.
Regularity makes every prime component Cartier. The normalized evaluation
of its model function is

    phi_DU(x_Ei)=(b_i U_i)/b_i=U_i.

This local valuation identity is independent of geometric connectedness.
It also follows directly from the component normalization in Ch24, so the
extra Ch05 standing convention is immaterial for this local formula.

The signed measure ddc(phi_DU) is supported on the component points and has
coefficient b_i(D_U.E_i). Consequently

    integral u ddc(phi_DU)
      =sum_i b_i U_i(D_U.E_i)
      =D_U^2.

This equality does NOT assert that u itself is a model function or that
u=phi_DU globally. Equality of values at the finite support of the test
measure is enough. This is the central reason the new proof works.

### 3. Weighted negative square and its equality case

With the actual multiplicities, the principal special-fiber identity
sum_j b_j(E_j.E_i)=0 gives

    -D_U^2
      =sum_{i<j} b_i b_j(E_i.E_j)(U_i-U_j)^2.

This is a direct real-linear algebraic identity on a regular surface and
was independently expanded. It agrees with the unchanged Ch20
eq:ch20-hodge-laplacian, lines 1307--1374. No disputed graph modulus-length
normalization is used. Each off-diagonal intersection is a degree over
the residue field, positive when the components meet; nonrational points
retain their residue degrees. The factors b_i b_j are not dropped.

Thus zero square forces equal vertex values along each incidence. This
also handles node blowups inserting multiplicity-two components: they are
retained as test vertices, not incorrectly replaced by reduced-model
vertices. A residue-degree-c intersection simply contributes the positive
factor c and cannot cancel a nonzero squared difference.

### 4. Connected special fiber without geometric connectedness

This paragraph was checked independently, not inferred from Ch05's
geometric-connectedness convention. A proper flat model has a finite
R-module A=H0(model,O), hence A is pi-adically complete. Flatness and density
of the generic fiber give an injection A into H0(X,O_X).

A disconnected special fiber determines a nontrivial open-and-closed
partition on every infinitesimal thickening: all those thickenings have
the same underlying topological space. Their characteristic idempotents
are compatible. Formal functions and completeness would produce a
nontrivial idempotent in A. Since X is smooth and connected, its regular
irreducible components are disjoint and there is only one; hence X is
integral. Properness makes H0(X,O_X) a finite field extension of K. That
field has no nontrivial idempotents, a contradiction.

This argument does not require H0(X,O_X)=K, residue-rational components,
or geometric connectedness. Connectedness of a finite union of
irreducible components implies connectedness of its incidence graph.
All U_i on the model therefore equal one number; the one-component case
is immediate.

### 5. Common constants and density

The resolution input gives cofinal SNC models with arbitrary positive
component multiplicities, not reduced semistable models. Common
domination can also be required to dominate a model determining omega.
A proper birational domination of normal models is an isomorphism at the
generic point of each old prime divisor. Its strict transform therefore
represents the same normalized divisorial valuation. Constants on
dominating models agree at these retained points; common domination makes
one global constant.

Every divisorial point can be included as such a component after
domination and SNC resolution. Divisorial density and continuity then
give u=c on all of X_an. Density alone would not suffice without the
continuity assumed here. No retraction formula for MA, no common reduced
semistable determining model for the approximating potentials, and no
uniform convergence on an increasing family of graphs is used.

As written in the original bytes, the Ch05 citations in this last step
need the connectedness-scope clarification noted at the start. The new
revised1 paragraph is reviewed separately.

## Dependency and assembly boundary

The proof uses the original BFJ approximation and model-measure package,
the elementary weighted intersection square, proper connectedness, and
SNC/divisorial topology. It does not use the old curve retraction claims
in Ch21/Ch25, the new Ch26 real graph bridge, the real-class curve envelope
candidate, CLD positivity transfer, or disputed GJKM nonemptiness.

Read-only reconstruction shows the original copied chapter equals the
exact frozen weighted-energy parent with ONLY the old uniqueness proof
replaced by uniqueness_proof.tex. The proposition is byte-for-byte
unchanged. The unified diff against the live source equals chapter.patch
byte-for-byte; git apply --check passes without applying it. All 170
original chapter labels remain and the sole extra label is
eq:ch28-curve-uniqueness-model-test. There are no duplicate labels.

This is not independent approval of the energy parent or of every
untouched statement in the full Ch28 copy. It is not a proof for arbitrary
nontrivially valued fields or arbitrary singular E1 potentials. Production
review, coordinated integration, and full-book validation remain separate.
No frozen author input or live source was modified.
