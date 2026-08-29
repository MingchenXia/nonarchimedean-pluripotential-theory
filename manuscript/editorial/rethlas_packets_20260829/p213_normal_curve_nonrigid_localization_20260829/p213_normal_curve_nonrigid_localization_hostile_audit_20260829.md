# Hostile audit: normal-curve nonrigid localization

Date: 29 August 2026

Status: **PASS on mathematical completeness; zero critical gaps found.**
This is an audit of a quarantine candidate, not a promotion or novelty claim.
The statement and proof were not edited.

## Frozen bytes

- statement SHA-256:
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`
- proof SHA-256:
  `7aa7e3fb69bbf01878fc589cecdcf8982a151ed9254ab0ad22af1d382d30b55a`

The primary sources checked were:

- `/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`;
- `/private/tmp/p21_bridge_sources/ducros_curve.pdf`, SHA-256
  `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

## 1. Affinoid connected component and analytic interior

Proof lines 7--17 are sound.

An affinoid neighborhood exists by goodness and can be chosen inside the
prescribed open set.  Its connected components are the finitely many clopen
affinoid domains defined by primitive idempotents, so the component `Q`
containing `y` remains compact and affinoid.  Since the original affinoid is an
analytic neighborhood and `Q` is open in it, `Q` is still an analytic
neighborhood of `y`; hence `y` belongs to `Int(Q/W)`.

Normality passes to analytic domains by CLD 11.3.1.  The same section states
that connected components of the normalization correspond to irreducible
components.  Since a normal space is its own normalization, connected normal
`Q` is irreducible.  Pure dimension one passes to analytic domains by CLD
11.2.3.

No connectedness, affinoidness, normality, or interior gap occurs here.

## 2. The empty-relative-boundary branch

Proof lines 19--23 are correct, although one source sentence could be made
more explicit in a later editorial rewrite.

For a separated analytic domain, the proof of CLD Lemma 11.4.10 records that
`Int(Q/W)` equals the topological interior of `Q` in `W`.  Thus
`partial(Q/W)=empty` implies `Q=Int(Q/W)`, so `Q` is open in `W`.  It is
already compact.  With the constant unit moment, the boundary image is empty,
`Omega=R`, and `U=Q`; the constant map from compact `Q` to `R` is proper.

The proof's assertion “`Q` is both open and compact” is therefore justified;
it is not an unsupported implication from topological compactness.

## 3. Nonvanishing of every separator and the identity principle

Proof lines 25--46 are correct.

Because `y` is in the ordinary interior of `Q`, the ordinary local rings of
`Y` and `Q` at `y` agree.  Ducros 4.2.18 says that at a nonrigid point of a
normal analytic curve

`O_{Y,y}=kappa(y)`.

If `f_z(y)=0`, its germ is therefore zero, so `f_z` vanishes on an ordinary
open neighborhood of `y`.  If `f_z` were nonzero on `Q`, normality makes `Q`
reduced and the zero locus a proper Zariski closed subset.  Irreducibility and
CLD 11.2.5 make every such subset have dimension strictly below one, whereas
CLD 11.2.3 makes every nonempty analytic open subset of the pure curve
one-dimensional.  This contradiction proves `f_z=0` on `Q`, contrary to the
separation inequality at `z`.

The argument uses ordinary open germs, not a false assertion that evaluation
zero always implies a zero germ.  The field local ring at the nonrigid normal
point is exactly what makes that implication legal.

## 4. Compact domain and iterative relative-boundary inclusion

Proof lines 48--75 are correct.

The boundary `partial(Q/W)` is compact.  Holomorphic separation in the
affinoid `Q` produces the open cover by the sets `Q_z`; finite extraction is
valid.  Since every selected `f_i(y)` is nonzero, the real number

`r=(1/2) min_i |f_i(y)|`

is positive.  The simultaneous inequalities `|f_i|>=r` define a compact
analytic domain `V` and strict inequalities at `y` make it an analytic
neighborhood.  Every `f_i` is invertible on `V`.

For clarity, the compressed “applied successively” sentence at proof lines
67--70 expands as follows.  Put

`V_0=Q`, `V_j=V_{j-1} cap {|f_j|>=r}`.

The boundary-composition identity CLD (11.4.1.3) gives

`partial(V_j/W) subset partial(V_j/V_{j-1}) union
 (V_j cap partial(V_{j-1}/W))`.

CLD (11.4.2.2), together with its preceding boundaryless-base-change
argument, gives

`partial(V_j/V_{j-1}) subset {|f_j|=r}`.

Induction yields

`partial(V/W) subset partial(Q/W) union union_i {|f_i|=r}`.

This is exactly the inclusion used.  It does not require equality, and it
does not lose a boundary contribution from an earlier inequality.  The two
cases at lines 70--74 therefore separate every point of `partial(V/W)` from
`y` in at least one moment coordinate.

## 5. Final openness and properness

Proof lines 77--85 are correct.

The relative boundary is a closed subset of compact `V`; its tropical image
is compact, hence its complement `Omega` is open.  The set `U` is open in
`V` and misses `partial(V/W)`, so it lies in `Int(V/W)`.  Since `V` is a
separated analytic domain, this relative interior is the topological interior
in `W`; consequently `U` is open in `W`.  Boundary avoidance puts `y` in
`U`.

The continuous map `F_trop:V->R^N` is proper because `V` is compact and
`R^N` is Hausdorff.  The restriction `F_trop:U->Omega` is its base change by
the open immersion `Omega->R^N`; properness is stable under base change.

No closedness-at-infinity or source-boundary term is missing.

## 6. Scope and residual risk

The proof establishes only the stated normal, pure one-dimensional,
nonrigid case.  It does not contradict CLD Remark 12.3.7, because the rigid
origin in that counterexample does not have the field-local-ring property
used at proof lines 33--46.

The only editorial improvements suggested by this audit are to cite the
proof of CLD Lemma 11.4.10 at the two uses of “relative interior equals
topological interior” and to display the nested-domain boundary induction.
Those are source-expansion improvements, not mathematical gaps.

Subject to the project's required production Rethlas and independent source
verification, this packet is a viable replacement for the nonrigid
localization input over a possibly trivially valued field.
