# Chapter 55 toric zero-volume theorem: repair proposal

**Prepared:** 2026-08-24 (Asia/Shanghai)  
**Live theorem:** `thm:ok-toric-zero-mass`  
**Rethlas report inspected:** `/private/tmp/rethlas_ch55_integrated_20260824.json`  
**Editing status:** proposal only; Chapter 55 was not edited  
**Forbidden dependency:** arXiv:1710.09731 and every route through it are
excluded.

## Verdict

The equality `nu_Cao(T)=dim Delta(T)` is defensible in the stated smooth
projective toric integral/rational setting, but the present Chapter 55 proof
does not prove it.  The sentence saying that toric asymptotic
Riemann--Roch identifies Cao's section-growth term with
`lambda_n(K+epsilon Q)` suppresses all of the hard interfaces singled out by
Rethlas: the exact multiplier ideal, chartwise strict-interior shifts, global
character gluing, lattice normalization, rational subsequences, existence of
the inner `m`-limit, and the precise form of Cao's criterion.

The theorem should be retained only if the expansion below is inserted (or an
equivalent fully cited global toric section-count lemma is proved earlier).
If that expansion is not included, the theorem should be downgraded to a
conditional remark or removed from Chapter 55; the current two-paragraph proof
must not remain labeled as complete.

The same interface is compressed in Chapter 69, lines 520--573.  That chapter
should be synchronized with the repair.  In particular, Cao's Proposition 4.4
is printed with an actual inner limit, whereas Chapter 69 currently defines a
`varlimsup`.  In the toric case the lattice argument proves the limit exists,
but the general statement attributed to Cao should reproduce the source
before specializing.

## Required conventions

Fix the character and cocharacter lattices
`M=Hom(T,C^*)` and `N=Hom(C^*,T)`, and normalize Lebesgue measure
`lambda_M` on `M_R` so that a fundamental parallelepiped of `M` has volume
one.  If `D` is rational, choose a positive integer `q` such that `qD` is an
integral toric divisor and replace

`(D,T,varphi,K)` by `(qD,qT,qvarphi,qK)`.

This does not change either `nu_Cao(T)` or `dim K`.  The proof may therefore
start in the integral case.  Choose a very ample integral toric divisor `A`,
a smooth invariant positive metric on it, and its full-dimensional moment
polytope `Q`.

On the open torus, let `F_T:N_R -> R` be the convex weight of the invariant
metric and define the Newton body explicitly by the closed effective domain

`K = closure(dom(F_T^*))`.

This is a nonempty compact convex subset of the moment polytope of `D`.
If `F_A` is the smooth toric weight of `A`, convex conjugacy gives

`closure(dom((F_T+epsilon F_A)^*)) = K+epsilon Q`.

Indeed, the conjugate of a sum is the lower-semicontinuous infimal
convolution; after taking the displayed closures, its effective domain is the
sum of the two compact closed domains, so no further closure ambiguity remains.
This proves the displayed toric addition formula rather than merely announcing
it.

## The global toric section-count lemma that is missing

For rational `epsilon>0`, set

`B_epsilon=K+epsilon Q`

and, for positive integers `m` with `m epsilon` integral, set

`W_{m,epsilon}=H^0(X,O_X(mD+m epsilon A) tensor I(m varphi))`.

The needed lemma is

`lim_{m -> infinity, m epsilon in Z} dim W_{m,epsilon}/m^n
 = lambda_M(B_epsilon)`.

There is no factor `n!`: lattice-normalized Euclidean volume is the leading
coefficient of the character count divided by `m^n`; the algebraic volume of
the corresponding graded series is `n! lambda_M(B_epsilon)`.

### Complete proof of the lemma

1. The multiplier ideal of an invariant weight is invariant.  Hence
   `W_{m,epsilon}` is a torus representation with a basis of distinct
   characters.  Let `E_{m,epsilon} subset M` be its set of weights.  Then
   `dim W_{m,epsilon}=#E_{m,epsilon}`.  The character basis and its local
   exponent vectors are the standard toric dictionary in `CLS11`, Section
   4.3.

2. Cover `X` by the finitely many smooth affine charts `U_sigma` associated
   to maximal cones.  Choose the toric frame of `D+epsilon A` on each chart.
   For `u in M`, let
   `a_{sigma,m,epsilon}(u) in Z^n` be the exponent vector of the local
   coefficient of the character section `chi^u`.  It is affine-linear in
   `(u,m)` and satisfies

   `a_{sigma,m,epsilon}(u)
     =m a_{sigma,1,epsilon}(u/m)`.

   Let `P_sigma(varphi)` be Guenancia's local Newton convex body of the local
   toric psh weight.  Theorem 1.13 of `Guenancia12`, with the book's
   multiplier-ideal convention, gives the exact chartwise condition

   `z^alpha in I(m varphi|U_sigma)
      iff alpha+1_sigma in Int(m P_sigma(varphi))`.

   Consequently

   `u in E_{m,epsilon}`

   if and only if, on every maximal chart, the local exponent is holomorphic
   and

   `a_{sigma,1,epsilon}(u/m)+1_sigma/m
       in Int(P_sigma(varphi))`.

   This explicitly retains both the strict interior and the fixed
   anticanonical `1_sigma` shift.

3. Unfolding `K=closure(dom(F_T^*))` in the same toric frames gives the global-local
   compatibility identity

   `{x in M_R : a_{sigma,1,epsilon}(x)
       in P_sigma(varphi) for every maximal sigma}
       =K+epsilon Q`.

   To prove it, subtract the Cartier vector of `D` on `U_sigma`.  The local
   Newton set is the translate of `K` by that Cartier vector plus the dual
   cone.  The Cartier vectors of `A` are the vertices of `Q`.  Intersecting
   the resulting closed conditions over the complete fan is equivalent to
   the support-function inequalities for
   `h_K+epsilon h_Q`, hence cuts out `K+epsilon Q`.  This also checks that the
   signs in the local exponent convention and in the global Newton body agree.

4. Because the cover is finite and the shifts `1_sigma/m` tend uniformly to
   zero, the exact strict conditions in step 2 converge to the closed
   conditions in step 3.  More explicitly, for every compact
   `C subset Int(B_epsilon)`, all points of
   `C intersect m^{-1}M` occur in `m^{-1}E_{m,epsilon}` for all sufficiently
   divisible `m`; and for every `delta>0`,

   `m^{-1}E_{m,epsilon} subset (B_epsilon)_delta`

   for all sufficiently large divisible `m`.  The first assertion follows
   from the positive minimum of the finitely many strict chart margins on
   `C`.  For the second, otherwise a convergent bounded sequence outside the
   `delta`-neighborhood would limit to a point satisfying all closed chart
   conditions, contradicting step 3.

5. Since `epsilon>0` and `Q` has interior, `B_epsilon` is
   full-dimensional.  Its boundary has Lebesgue measure zero.  Choose an
   interior point `b` and exhaust its interior by
   `C_eta=(1-eta)B_epsilon+eta b`.  Apply the elementary lattice Riemann-sum
   formula

   `#(mC intersect M)/m^n -> lambda_M(C)`

   to `C_eta` and to arbitrarily small outer parallel bodies of
   `B_epsilon`.  (The formula follows by surrounding every lattice point by
   its covolume-`m^{-n}` fundamental cell; the symmetric difference tends to
   the boundary, which has measure zero.)  Step 4 then squeezes
   `#E_{m,epsilon}/m^n` to `lambda_M(B_epsilon)`.  This proves existence of
   the actual limit, not merely a limsup, and proves the lemma.

The third step is essential.  Merely applying Guenancia chart by chart and
then asserting the answer is `K+epsilon Q` leaves precisely the global gluing
gap identified by Rethlas.

## Completion with Cao's criterion

Define, exactly in Cao's normalization,

`S_A(epsilon)
 =lim_{m -> infinity, m epsilon in Z}
   h^0(X,O_X(mD+m epsilon A) tensor I(m varphi))/m^n`.

The preceding lemma gives

`S_A(epsilon)=lambda_M(K+epsilon Q)>0`.

Cao's Proposition 4.4 states that, for the projective pair `(D,varphi)`,

`lim_{epsilon downarrow 0, epsilon rational}
 log S_A(epsilon)/log epsilon
 = n-nu_Cao(T)`.

No upper-regularized multiplier ideal has been substituted here: Cao first
compares it asymptotically with the ordinary `I(m varphi)`, and the toric
count above uses that same ordinary ideal.

Put `d=dim K`.  Let `V=span(K-K)` and choose an orthogonal complement.  A
relative `d`-ball lies in `K` after translation, while an `n`-ball lies in
`Q`; these give

`c epsilon^(n-d) <= lambda_M(K+epsilon Q)`.

Conversely, bound `K` in a fixed box in its affine `d`-plane and `Q` in a
fixed `n`-box.  The Minkowski sum lies in a box with `d` side lengths bounded
independently of `epsilon` and `n-d` side lengths `O(epsilon)`, so

`lambda_M(K+epsilon Q) <= C epsilon^(n-d)`.

After taking logarithms and dividing by `log epsilon`, the constants
disappear and the quotient tends to `n-d`.  Cao's criterion therefore gives
`nu_Cao(T)=d`.

## Minimal safe disposition

- **Preferred:** insert the explicit Newton-body definition, the five-step
  toric section-count lemma, Cao's exact criterion, and the final tube
  estimate into Chapter 55; then synchronize Chapter 69 and submit the exact
  repaired source to Rethlas.
- **Acceptable shorter route:** cite a previously proved theorem in the book
  that contains exactly the global section-count lemma above, including the
  strict shifts and actual limit.  The current Chapter 69 paragraph is not yet
  sufficiently explicit to serve as that citation boundary.
- **If neither is done:** downgrade `thm:ok-toric-zero-mass` to a conditional
  statement or remove it.  Do not leave the present proof as a complete proof.

## Source checks relevant to the repair

- `Cao14`, Proposition 4.4, uses the logarithmic order of the actual
  normalized section-count limit and the ordinary multiplier ideal
  `I(m varphi)`; the rational divisibility convention must be stated.
- `Guenancia12`, Theorem 1.13, says that a monomial `z^alpha` belongs to the
  multiplier ideal of a toric psh weight exactly when
  `alpha+1` lies in the interior of its Newton convex body.
- `CLS11`, Section 4.3, supplies the toric character basis and local exponent
  dictionary; it does not by itself prove the multiplier-ideal condition or
  the asymptotic squeeze.
