# Independent hostile exact-byte re-audit: normal-curve nonrigid localization

Date: 29 August 2026

## Frozen bytes audited

- statement: `p213_normal_curve_nonrigid_localization_statement_20260829.tex`
- SHA-256: `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`
- proof: `p213_normal_curve_nonrigid_localization_proof_20260829.tex`
- SHA-256: `f6bf21cc24ba593ca097c4facaf4a80c5c5e297ccb341d7a1ab9bd6fa7f429e0`

This audit was performed from the exact files above.  Earlier audits and automated
verdicts were not used as evidence.

## Sources checked

The source PDFs inspected were the local copies with SHA-256 hashes

- CLD25: `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`;
- Ducros, curve structure: `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

The cited uses agree with the sources:

1. CLD25, Section 15.2.2 states that every affinoid analytic space is
   holomorphically separated.
2. CLD25, Sections 11.2.3 and 11.2.5 give invariance of local dimension under
   passage to analytic domains, finiteness of the irreducible components of an
   affinoid space, and the strict dimension drop for a proper Zariski-closed
   subset of an irreducible analytic space.
3. CLD25, Sections 11.4.1--11.4.2 give both the composition rule for relative
   interiors and the boundary calculation for a domain cut out by one norm
   inequality.  They imply exactly the displayed inclusion for
   `partial(V_j/W)`: taking complements in the relative-interior composition
   formula adds the inherited boundary, while the new relative boundary is
   contained in `|f_j|=r`.
4. CLD25, Lemma 12.3.6 contains the finite separator construction used here.
   Its appeal to a nontrivial value group occurs precisely when a separator
   vanishing at the centre is shifted by a nonzero scalar.  The present proof
   replaces only that step.
5. The proof of CLD25, Theorem 16.8.5 contains the same deletion of the
   tropicalized relative boundary and proper-base-change localization.
6. Ducros, Section 4.2.18 explicitly states that, on a normal analytic curve,
   the local ring at a nonrigid point is an integral Artinian ring and hence is
   equal to its residue field `kappa(y)`.

## Hostile checks

### Connected normal affinoid implies irreducible

Let `Q` be the connected component selected in the proof.  It is an affinoid
domain and normality passes to analytic domains and to clopen components.  At
every point of a normal analytic space the local ring is a domain.  If two
Zariski irreducible components of the affinoid `Q` met at a point, their germs
would give two minimal primes of that local ring.  Thus the components are
pairwise disjoint.  An affinoid has finitely many irreducible components; each
is consequently the complement of a finite union of closed components and is
both closed and open.  Connectedness forces a single component.  This verifies
the new self-contained irreducibility paragraph; it does not silently assume
geometric normality, strictness, or a nontrivial valuation.

### Nonvanishing of a separator at the centre

Because `y` lies in the relative interior of `Q`, the germ of a function on
`Q` at `y` is a germ on `Y`.  If its value at `y` is zero, Ducros 4.2.18 makes
that germ zero.  The function then vanishes on an ordinary open subset.  On the
irreducible pure curve `Q`, a nonzero analytic function has a proper
Zariski-closed zero locus of dimension zero, while every nonempty analytic open
domain has local dimension one.  Hence the function is identically zero,
contradicting separation from the boundary point.  This is valid for all
nonrigid Berkovich point types and for a trivial ground-field valuation.

### Construction of the moment and boundary exclusion

The relative boundary of `Q` is compact.  The open separator loci therefore
have a finite subcover.  The chosen radius is strictly smaller than every
central norm.  The finite intersection `|f_i| >= r` is a compact analytic
domain, is a neighborhood of `y`, and all `f_i` are units there.  At every new
boundary face one coordinate has norm `r`, whereas its norm at `y` is at least
`2r`; an inherited boundary point is separated by one member of the finite
cover.  Therefore no boundary point has the same tropical image as `y`.

The empty-boundary case is also sound: the constant unit is a moment, and a
compact analytic domain with empty relative boundary is open in `W`.

### Proper localization

The tropical image of the compact relative boundary is compact and hence
closed in Euclidean space.  The inverse image of its complement avoids the
relative boundary, so it is an open neighborhood of `y` in `W`.  The map from
compact `V` to `R^N` is proper, and its restriction is its base change to the
open complement.  The claimed properness follows.

## Verdict

**PASS.**  Critical errors: **0**.  Proof gaps: **0**.  Citation mismatches:
**0**.  The exact statement and proof bytes listed above are suitable for a
fresh production verification.
