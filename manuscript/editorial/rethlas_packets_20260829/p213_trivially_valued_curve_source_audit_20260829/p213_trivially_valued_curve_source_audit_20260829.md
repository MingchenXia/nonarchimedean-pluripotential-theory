# P21.3: primary-source audit for the trivially valued curve case

Date: 29 August 2026
Status: source audit only; no theorem is promoted, no open problem is closed,
and no novelty or priority claim is made.  Every candidate below is explicitly
unverified.  No live manuscript file was changed.

## 1. Frozen inputs

The audit concerns the following exact proof artifacts.

| artifact | SHA-256 |
|---|---|
| `p21p3_curve_rigidity_virtual_annulus_bridge_statement_live_20260828.tex` | `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033` |
| `p21p3_curve_rigidity_virtual_annulus_bridge_proof_live_20260828.tex` | `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5` |
| `p21p3_curve_rigidity_arbitrary_field_reduced_statement_live_20260828.tex` | `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21` |
| `p21p3_curve_rigidity_arbitrary_field_reduced_proof_live_20260828.tex` | `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af` |
| `p213_normal_rigid_zero_atom_statement_20260829.tex` | `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac` |
| `p213_normal_rigid_zero_atom_proof_20260829.tex` | `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2` |
| `p213_rigid_exception_extension_statement_20260829.tex` | `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5` |
| `p213_rigid_exception_extension_proof_20260829.tex` | `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce` |
| `p213_componentwise_rigid_exceptions_statement_20260829.tex` | `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8` |
| `p213_componentwise_rigid_exceptions_proof_20260829.tex` | `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5` |

Primary sources inspected:

| source | exact local file | SHA-256 |
|---|---|---|
| Chambert-Loir--Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, 25 July 2025 | `/private/tmp/p21_bridge_sources/cld25.pdf` | `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719` |
| Ducros, *La structure des courbes analytiques*, arXiv:2405.10619v1 | `/private/tmp/p21_bridge_sources/ducros_curve.pdf` | `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad` |
| Gubler--Jell--Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, BSMF 154 (2026) | `/private/tmp/p21_bridge_sources/gjr26.pdf` | `acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c` |

## 2. Executive verdict

1. **The verified nontrivially valued proof does not extend verbatim.**  Its
   canonical source-localization step invokes CLD Lemma 12.3.6, whose printed
   hypothesis is that the ground valuation is nontrivial.  CLD Remark 12.3.7
   immediately says that the lemma is false over a trivially valued field and
   gives the rigid origin of the open unit disc as a counterexample.

2. **CLD's modified meaning of “strict” does not repair that failure.**  CLD
   11.8.1 changes the terminology in trivial valuation; Lemma 11.8.2 says that
   on an affinoid it still agrees with classical strictness; Remark 11.8.4 says
   that the strict germ `0<|T|<1` has no nonempty compact strict analytic
   domain.  Thus one cannot recover Lemma 12.3.6 merely by reading “strict” in
   the 2025 sense.

3. **The failure is irrelevant at the rigid counterexample for top-degree
   current tests, but this observation alone is not a proof.**  CLD Proposition
   15.2.1(a) puts the support of a smooth `(1,1)`-form on a curve in
   `{x:d_K(x)>=1}`.  Ducros 3.3.2 identifies the points with `d_K=1` on a curve
   as types 2 and 3; in particular type 1 is rigid when `K` is trivially valued.
   Hence the rigid origin in CLD Remark 12.3.7 carries no nonzero `(1,1)` test
   germ.  What is still needed is a replacement for Lemma 12.3.6 at type-2 and
   type-3 points.

4. **A curve-specific replacement is viable, but it is not yet proved in the
   packet.**  Ducros Theorem 4.5.4 gives an elementary neighborhood: a
   type-3 annular neighborhood, or at type 2 a compact-tree star with only
   finitely many gently virtual-annular branches and all other branches virtual
   discs.  Ducros Proposition 4.2.14 makes the component obtained by cutting
   the finitely many annular branches at type-2/3 cutpoints into a closed
   analytic domain.  Branch-order-one analytic germs from Ducros 4.2.6 and
   4.2.11.1--4.2.11.2 separate those finitely many boundary points.  This gives
   a precise route to a boundary-avoiding moment without a nontrivial ground
   valuation and without asking the compact domain to be strict.

5. **The rigid zero-atom estimate also has a viable direct repair.**  Its only
   genuinely nontrivial-valuation step is the use of strict/admissible radii
   tending to zero.  CLD Example 11.4.2 defines the closed disc `D(0,r)` and
   identifies its Gauss boundary for every real `r>0`, without a value-group
   condition.  Replacing all “admissible radii” by arbitrary real radii preserves
   the finite-flat tube, the two radial transition bands, and the exact
   calibrated total variation `2d`; arbitrary real `r` tend to zero even in
   trivial valuation.  This rewrite must still receive a full proof and Rethlas
   verification.

6. **GJR26 cannot be cited as a trivial-valuation source.**  Its section 2.2
   fixes, for the whole paper, a complete field with nontrivial valuation.
   Consequently GJR Lemma 6.14, Corollary 3.18, Remark 3.20, and section 8.13
   cannot be imported into the trivial case.  The particular uses in the
   verified proof have replacements in Ducros and CLD, listed below.

7. **CLD Corollary 16.8.6 is not a shortcut to the desired current theorem.**
   In trivial valuation it passes to `K((T))`, but only for currents already
   constructed as products of curvature currents.  It does not pull back an
   arbitrary positive closed `(0,0)` current.  Moreover its exceptional-set
   threshold is `H^{n-p}` for a product of `p` curvature currents.  For a curve
   curvature measure (`n=p=1`) this is `H^0`; a singleton is not
   `H^0`-negligible.  It therefore does not prove the required rigid zero-atom
   statement.

The resulting status is **viable replacement theorem, not yet established**.
No statement below may be cited as a theorem until the four promotion gates in
section 8 have been discharged.

## 3. What CLD25 already supplies in trivial valuation

CLD 0.2.15 explicitly says that the theory is valid in trivial valuation.  The
following printed results used by the P21.3 curve argument carry no
nontrivial-valuation hypothesis and therefore remain available:

- currents, positivity, order zero, and Radon representation: sections 7.1--7.2,
  Propositions 7.2.8--7.2.9;
- transposition and closedness of integration: 7.7.4 and Lemma 7.7.5;
- pullback of psh functions and Bedford--Taylor positivity/pushforward:
  Proposition 8.1.5, Lemma 8.5.5, Proposition 8.5.6;
- finite-at-a-point and finite-flat localization: 11.6.3 and Lemma 11.6.5(a),
  together with Remark 11.4.7;
- arbitrary-radius discs and their boundary: Example 11.4.2;
- tropical polyhedrality and canonical calibration: Theorem 12.2.4,
  Corollary 12.2.5, Lemma 13.3.8, section 14.3.2, Lemma 14.3.4, and
  Proposition 14.4.2;
- local moment descriptions of forms/functions: Proposition 15.1.1(b) and
  Corollary 15.1.2;
- nilreduction and the form variant: Proposition 15.1.3;
- support and smooth separation/cutoffs: Proposition 15.2.1, section 15.2.2,
  Corollary 15.2.4, Proposition 15.2.8, and Corollary 15.2.9;
- integration and cycles: Proposition 16.6.3.

The exact negative source statements are equally important:

- Lemma 12.3.6 assumes `|K^x| != {1}`;
- Remark 12.3.7 says Lemma 12.3.6 is false for trivial valuation;
- Theorem 16.8.5 assumes nontrivial valuation and its proof invokes Lemma
  12.3.6;
- 11.8.1--11.8.5 alter strictness at the level of Temkin reductions but do not
  restore compact strict representatives.

## 4. Exact proof-byte audit

### 4.1 General current calculus

In the reduced proof, lines 4--21 and 269--305 use CLD current calculus,
moment presentations, proper pushforward, and canonical calibration.  These
ingredients are valuation-independent.  Lines 22--24 are not: the cited
boundary-avoiding moment is Lemma 12.3.6, and the cited proof of Theorem
16.8.5 consumes it.

**Status:** the calculus survives; the localization supplying a proper tropical
pushforward must be replaced.

### 4.2 Canonical source localization

The bridge proof uses CLD Lemma 12.3.6 exactly at lines 20--25 and uses the
localization from the proof of CLD Theorem 16.8.5 at lines 35--43.  This is the
principal invalid step in trivial valuation.

The following part is still valid after a replacement boundary separator is
constructed:

- form block: CLD Proposition 15.1.1(b), bridge lines 10--13;
- smooth cutoff factorization through an analytic moment: CLD Corollary
  15.1.2, bridge lines 14--18;
- concatenation of finite moment blocks, bridge lines 27--33;
- properness after deleting the boundary image, bridge lines 35--47;
- finite source cover and smooth partition, bridge lines 49--58, using CLD
  Corollary 15.2.9.

Thus the missing assertion is exactly the existence, at a point supporting a
`(1,1)` test germ, of a compact analytic neighborhood and a finite analytic
moment separating that point from the relative boundary.

### 4.3 Curve-specific candidate replacement for Lemma 12.3.6

The needed construction has all of its geometric dependencies identified:

1. By CLD Proposition 15.2.1(a), only `d_K(y)=1` must be treated.  Ducros
   3.3.2 makes such a curve point type 2 or 3.
2. Ducros Theorem 4.5.4 gives a compact-tree elementary neighborhood.  At
   type 3 it is virtual-annular.  At type 2, deletion of the center gives all
   virtual discs plus only finitely many gently virtual annuli.
3. Cut each of those finitely many annuli at a nearby type-2/3 skeleton point,
   retain every virtual-disc component in full, and retain the center-side
   annular collars.  Ducros Proposition 4.2.14 supplies the closed analytic
   domain with exactly those cutpoints as relative boundary; compactness comes
   from the compact-tree closure in Theorem 4.5.4.
4. At type 2, branches are the closed points of the residual curve by Ducros
   3.3.5.2 and 4.2.11.1.  The density `kappa(y) -> H(y)` in Ducros 4.2.6 lifts a
   residue uniformizer of each of the finitely many cut branches to an analytic
   unit germ having branch order one.  At type 3, Ducros 4.2.11.2 supplies a
   germ with nonzero annular slope.  Ducros Proposition 4.3.9 and
   4.3.10.2--4.3.10.3 give cofinal virtual-annular collars.
5. Shorten once so that every chosen germ is an analytic unit.  Its norm is
   constant on every retained virtual disc (Ducros 3.6.32.3) and affine with
   the prescribed nonzero slope on its selected annular collar (Ducros
   3.6.22--3.6.24 and 3.6.35.8).  Concatenating one separator per boundary
   cutpoint therefore makes the center tropical value different from every
   boundary tropical value.
6. Append the form, prescribed-moment, and cutoff blocks using CLD
   Proposition 15.1.1(b) and Corollary 15.1.2.  Projection to the separator
   block preserves boundary avoidance.  The existing bridge lines 35--47 then
   prove the required properness and extension-by-zero conclusion.

This is a complete dependency list, but steps 3--5 still need to be written as
a formal proof.  In particular, one must record the relative-boundary equality,
not merely a topological picture of the star.

### 4.4 Virtual-annulus ray and branch bridge

Most of the bridge is already over an arbitrary complete field in Ducros:

- residual curves and branch valuations: 3.3.5.2, 4.2.6, 4.2.9,
  4.2.11.1;
- cofinal virtual-annular sections: Proposition 4.3.9(2) and
  4.3.10.2--4.3.10.3;
- annular monomial norm and canonical retraction: 3.6.22--3.6.24 and
  3.6.35.8--3.6.35.10;
- elementary stars: Theorem 4.5.4;
- graph and arc topology: Theorem 3.5.1 and 1.3.5, 1.3.12.

Three edits are mandatory:

1. Bridge proof lines 98--100 and 254--255 say “finite separable extension.”
   Ducros Proposition 4.3.9(2) gives a finite splitting extension in general
   and says it may be chosen separable only when the ground valuation is
   nontrivial.  In trivial valuation the word “separable” must be deleted.
2. Bridge proof lines 83--84 and 183--185 cite the lifting construction in GJR
   Lemma 6.14.  It must be replaced by the already present density argument
   from Ducros 4.2.6; no GJR citation is legal here.
3. Bridge proof line 158 and the reduced proof lines 44--48 cite GJR 8.13,
   Corollary 3.18, and Remark 3.20.  Euclidean primitivity in the constructed
   ray is immediate from the appended coordinate of branch order one.
   Source-annular integral-affine structure and expansion are supplied by
   Ducros 3.6.22--3.6.24 and CLD 14.3.2, Lemma 14.3.4, and Proposition
   14.4.2.  Local finiteness of the active target star follows from the finite
   moment block and Ducros Proposition 4.2.4(ii), not from GJR.

The statement's remark at lines 227--244 must likewise say “virtual annulus
after a finite splitting extension,” not “strict annulus after a finite separable
extension.”

### 4.5 Smooth current classification

The reduced proof lines 152--438 have no further hidden dependence on a
nontrivial valuation once sections 4.2--4.4 are replaced:

- the Euclidean divergence calculation, lines 155--195, is real analysis;
- type-3 comparison uses the two annular rays from Ducros 4.2.11.2;
- type-2 comparison uses the residual-curve divisor functional and
  Riemann--Roch over the actual residue field, lines 317--404;
- globalization uses the graph structure and type-1/type-4 unibranch facts in
  Ducros Theorem 3.5.1, Theorem 4.2.5, Theorem 4.5.4, and 4.5.19.1;
- disappearance of test forms at the endpoint set follows from CLD
  Proposition 15.2.1(a).

**Status:** viable conditional on the curve-specific source-localization lemma
and the GJR-free annular rewrite.  The current cannot be transported to a
nontrivially valued scalar extension; the proof must remain downstairs over
`K`.

### 4.6 Normal rigid zero atom

In the exact normal proof:

- lines 7--68 (DVR coordinate and local finite-flatness) are valuation-
  independent; line 10 should say “affinoid neighborhood,” not “strict
  affinoid neighborhood,” since strict compact representatives need not exist;
- lines 69--87 introduce admissible radii;
- lines 93--181 are the radial cutoff, calibrated pushforward, positivity, and
  transposition estimate; the cited CLD results have no nontrivial-valuation
  hypothesis;
- lines 182--184 are the only explicit use of nontriviality: admissible radii
  tend to zero.

The candidate repair is to choose arbitrary real
`0<r<R<R_0`.  CLD Example 11.4.2 supplies `D(0,s)` and its single Gauss
boundary for every real `s>0`.  Finite morphisms are stable under analytic
base change (CLD 11.4.4), so restriction of the finite-flat tube to these
discs and annuli remains finite flat.  CLD Corollary 15.1.2 makes the radial
plateau smooth, and Lemma 13.3.8 plus Proposition 14.4.2 gives the same total
variation `2d`.  Letting arbitrary real `r` tend to zero yields the same final
estimate.

**Status:** viable exact rewrite, but unverified.  It is not a consequence of
CLD Corollary 16.8.6 for the `H^0` reason in section 2.

### 4.7 Rigid-exception extension

The rigid-exception proof lines 7--44 (graph connectedness), 59--86 (support
of top-degree forms away from rigid points), and 88--113 (continuous
Bedford--Taylor algebra) use source statements valid in trivial valuation.
Its only unavailable input is the smooth classification at lines 52--58.

**Status:** it extends once the smooth candidate theorem is verified.  No
additional trivial-valuation lemma is needed.

### 4.8 Reduced, nonreduced, and componentwise passage

The componentwise proof lines 126--142 use a strict-affinoid
Nullstellensatz and finite strict affinoid algebras.  That exact argument is
not available for a general CLD-strict germ over a trivially valued field,
because CLD Remark 11.8.4 forbids the needed compact strict neighborhood.

Two replacements have precise sources:

1. Let `Z_i` be the inverse image in a normal component curve of the
   zero-dimensional conductor/intersection locus.  If a point of `Z_i` were
   nonrigid, Ducros 4.2.18 would make its normal curve local ring a field.  A
   coherent proper zero-dimensional support cannot have a nonzero germ at
   such a point: its defining ideal in that field is either the unit ideal or
   zero, and the latter would put a full one-dimensional neighborhood in the
   support.  Hence every point of `Z_i` is rigid.  A point of `Z` has a
   preimage under finite normalization; the corresponding completed residue
   field extension is finite, so rigidity descends to `Z`.
2. Strictness of the normalization should be proved germwise, not with a
   compact strict affinoid.  CLD Lemma 11.8.5 characterizes a strict germ by
   torsion of the degrees modulo `|K^x|`.  Under a finite morphism
   `H(y)/H(x)` is finite, so its value-group quotient is finite; torsion at
   `x` therefore implies torsion at `y`.  This gives CLD-strictness of each
   normalization germ.

All other componentwise steps are valuation-independent: excellence and
finite normalization (CLD 11.1.10 and 11.3.1), nilreduction (CLD Proposition
15.1.3), form support (CLD Proposition 15.2.1), integration versus cycles
(CLD Proposition 16.6.3), finite proper pushforward, measure splitting, and
the graph argument.

**Status:** the componentwise target is viable conditional on the smooth
classification and arbitrary-radius zero-atom lemma.  The two replacements
above still require full written proofs and verification.

## 5. Why the scalar-extension shortcut is insufficient

The desired classification concerns an arbitrary positive, `d'`-closed and
`d''`-closed CLD current of bidegree `(0,0)`.  There is no cited pullback of an
arbitrary current along `X_{K((T))}->X`, and the verified proof deliberately
avoids asserting one.  CLD Corollary 16.8.6 instead starts with psh functions,
pulls those functions back, forms their curvature product upstairs, and then
pushes that specially constructed current down by the Shilov section.  This
does not manufacture an upstairs current corresponding to arbitrary `T`.

Therefore both current rigidity and branchwise balancing must be proved over
the original trivially valued field.

## 6. Unverified candidate statements

The statements in this section are targets only.  They are included because
every dependency has been identified above; they are not proved by this audit.

### Candidate A: full-dimension source localization on a curve

Let `K` be complete and trivially valued.  Let `Y` be a good separated
CLD-strict quasi-smooth `K`-analytic curve without boundary, let `y` satisfy
`d_K(y)=1`, and let `W` be an open neighborhood of `y`.  Given an ordinary
CLD-smooth `(1,1)` form near `y`, a finite analytic moment block, and an
optional smooth source cutoff, there should exist a compact analytic
neighborhood `V` of `y` in `W` and a concatenated analytic moment `F` such
that

`F_trop(y) notin F_trop(partial(V/W))`,

the form and cutoff factor through the appropriate blocks of `F`, and, for
`Omega=R^N\F_trop(partial(V/W))` and
`U=F_trop^{-1}(Omega)`, the map `F_trop:U->Omega` is proper.  The compact
domain `V` is not required to be strict.

Dependencies: CLD Proposition 15.2.1, Proposition 15.1.1, Corollary 15.1.2;
Ducros 3.3.2, Proposition 4.2.14, Theorem 4.5.4, 4.2.6,
4.2.11.1--4.2.11.2, Proposition 4.3.9, 3.6.22--3.6.24, and
3.6.35.8--3.6.35.10.

### Candidate B: zero atom at a normal rigid interior point

Let `K` be complete and trivially valued, let `X` be a good separated
`K`-analytic space, and let `y` be a rigid interior point whose ordinary local
ring is normal and whose germ is purely one-dimensional.  If `u` is a
continuous CLD-psh function near `y`, then the positive measure
`d'd''[u]` should have no atom at `y`.

Dependencies: the DVR/finite-flat part of the verified normal proof; CLD
Example 11.4.2, 11.4.4, 11.6.3, Lemma 11.6.5(a), Corollary 15.1.2, Lemma
13.3.8, Proposition 14.4.2, Lemma 8.5.5, Proposition 7.2.8, and Lemma
7.7.5.

### Candidate C: smooth current rigidity over a trivially valued field

Let `K` be complete and trivially valued, and let `Y` be a connected good
separated CLD-strict rig-smooth `K`-analytic curve without boundary.  Every
positive `d'`- and `d''`-closed CLD current of bidegree `(0,0)` on `Y` should
be `c delta_Y` for a unique `c>=0`.

Dependencies: Candidate A; the GJR-free annular bridge in section 4.4; the
valuation-independent Euclidean, residual-curve Riemann--Roch, and graph
arguments in reduced-proof lines 152--438.

### Candidate D: componentwise extension

Under the hypotheses of the verified componentwise statement, but with `K`
complete and trivially valued, the same classification and continuous-psh
Bedford--Taylor conclusion should hold, provided the normalizations have the
same locally finite rigid rig-smooth-exception sets.

Dependencies: Candidates B and C; the germwise normalization-strictness and
conductor-rigidity replacements in section 4.8; all valuation-independent
nilreduction, cycle, support, and measure-splitting steps of the verified
componentwise proof.

## 7. Required changes to a future proof packet

A future packet must not edit the verified nontrivial-valuation artifacts in
place.  It should be a new, quarantine-only packet and must:

1. prove Candidate A with an explicit closed analytic domain and exact
   relative boundary, citing Ducros Proposition 4.2.14;
2. remove every GJR26 dependency and every claim of a separable splitting
   extension;
3. rewrite the radial lemma using arbitrary real radii and prove all base-change
   and support assertions for the transition annuli;
4. replace the strict-affinoid conductor paragraph by the germwise arguments
   in section 4.8;
5. distinguish ordinary smooth CLD forms from weakly smooth forms throughout;
6. preserve the “downstairs current” firewall: no pullback of an arbitrary
   current to `K((T))` or to a splitting field;
7. state explicitly that compact source domains in Candidate A may be
   non-strict.

## 8. Promotion gates

No candidate can be integrated or removed from the open-problem inventory
until all of the following hold:

1. a complete source-aware proof packet discharges Candidate A and the
   GJR-free annular bridge;
2. a separate complete packet discharges Candidate B with arbitrary real
   radii;
3. the smooth, rigid-exception, and componentwise compositions are audited
   against their exact frozen dependencies, including the germwise strictness
   and conductor arguments;
4. each new mathematical result receives production Rethlas verification with
   `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical errors, and zero
   remaining gaps, followed by an independent source audit.

Until then the trivially valued one-dimensional P21.3 residual remains open.
