# Proposed relative zero-volume fibration theory — UNVERIFIED

This is an operator-supplied mathematical route for independent investigation, not a theorem grant or a request to weaken the original problem. Work in the complex Kähler perturbation scope explicitly considered in family09. The original general pseudoeffective zero-volume atoms stay open for a theorem under the following additional hypotheses.

Let pi:X->B be a supplied surjective holomorphic map between connected smooth compact Kähler manifolds, dimX=n, dimB=nu, 1<=nu<n, optionally connected fibres. No smooth-fibre, product, equidimensionality or flatness assumption. Let beta be a supplied Kähler form on B and theta=pi*beta. Let m=n-nu and omega any Kähler form on X. The closed positive degree-zero current pi_*(omega^m) should be the positive constant c_omega. Prove this across critical values and state c's generic-fibre/cohomological meaning. alpha=[theta] is nef, volume zero, numerical dimension nu. State exact foundation/applications.

For any bounded beta-psh phi on B (continuous included), set U=pi*phi and C_phi=beta+ddc phi. For epsilon>0 let theta_epsilon=theta+epsilon omega and take ANY globally bounded theta_epsilon-psh u_epsilon with ||u_epsilon-U||_infinity->0. These approximating potentials need not descend to the base and no o(epsilon) rate is assumed. This is an essential proposed strengthening of the already studied smooth pullback/product case. Use ordinary bounded Bedford–Taylor products, with the stated normalization ddc=i/(2pi)partial barpartial.

Operator proposal: pi_*((theta_epsilon+ddc u_epsilon)^n)/(binom(n,nu)c_omega epsilon^m) tends weakly on B to C_phi^nu, with raw mass V_B=int_B beta^nu>0 and reference phi=0. Both c_omega and epsilon^m are a TRANSVERSE calibration, not division by zero volume on X. The carrier is the fixed supplied B of dimensionnu; bounded/minimal singularity data are retained. The proposed limiting measure is unnormalized. Probability normalization at positive epsilon may alternatively tend to C_phi^nu/V_B, but that does not recover V_B from I-equivalence. Establish independence under changing omega's representative AND its Kähler class, since the stated c_omega changes accordingly; do not pretend c itself is independent of class.

Suggested difference estimate: for a smooth test f on B, integrate the difference of top powers by parts. Factor A^n-D^n=ddc(u_epsilon-U)sum_{j=0}^{n-1}A^jD^(n-1-j), where A=theta_epsilon+ddc u_epsilon, D=theta_epsilon+ddc U. Bound +/-pi*(ddc f) by C_f pi*beta. Each positive mixed integral int_X pi*beta A^j D^(n-1-j) has the cohomological value int_X theta(theta+epsilon omega)^(n-1)=O(epsilon^m), because theta^(nu+1)=0. This should cancel the rescaling and leave O(||u_epsilon-U||), with no epsilon-rate requirement. Check every bounded-product/integration-by-parts antecedent. The exact pullback family then expands to binom(n,nu)c_omega epsilon^m C_phi^nu after pushforward plus smaller terms. Prove the bounded pullback/projection formula across singular fibres by local bounded psh approximation; do not assume it for arbitrary singular currents.

Energy proposal: E_theta_epsilon(u)=1/(n+1)sum_{j=0}^n int_X u(theta_epsilon+ddc u)^j theta_epsilon^(n-j). Show E_theta_epsilon(u_epsilon)/(binom(n,nu)c_omega epsilon^m)->E_beta(phi), with E_beta(phi)=1/(nu+1)sum_{a=0}^nu int_B phi C_phi^a beta^(nu-a), raw reference0/massV_B. Monotonicity and constant-shift law should give |E_theta_epsilon(u_epsilon)-E_theta_epsilon(U)| <=||u_epsilon-U|| int_X theta_epsilon^n. The pullback coefficient uses sum_j binom(j,a)binom(n-j,nu-a)=binom(n+1,nu+1). Prove bounded BT identities, cocycle/variational/monotonicity/concavity/shift laws at their exact stated scopes. This removes the entire auxiliary Kähler class from the limiting base energy after the explicitly chosen transverse calibration.

If justified, strengthen both constructions to smoothly varying omega_epsilon with a Kähler limit (possibly a different Kähler class), and include changes of beta representative together with the compensating phi change and reference-energy cocycle. Do not claim arbitrary degenerate auxiliary paths. An E1 extension or independence for prescribed unbounded P-types is optional and needs a full separate proof; bounded/minimal type alone is not a full original solution. If pi has connected fibres, consider proving that continuous theta-psh functions descend to continuous beta-psh functions, with an actual argument through singular fibres and critical values, not a smooth-fibre assumption.

Known progress excluded from novelty: initial P15.1 smooth semipositive leading energy with a FIXED auxiliary Kähler class, and P15.2 P1xP1 representative-dependent original-carrier measure plus smooth pullback pushforward repair. The new task is every supplied nonproduct fibration, bounded/continuous potentials, non-descending perturbative potentials, arbitrary Kähler DIRECTIONS after explicit calibration, and no epsilon-relative convergence rate. Previous papers are fallible comparison evidence, not accepted hypotheses for this new proof. Do not claim literature priority.

Primary foundations may be precisely cited and applied without re-proving whole monographs. Every indispensable NEW bounded-product/projection/estimate/application claim needs an accessible full derivation. The selected primary BEGZ bodies below are actual mathematical evidence; transcription defects and any explicitly omitted proof remain visible. Only bounded BT constructions are needed for the proposed main statements. The full original general zero-volume problems remain open.

## Primary unit: Bounded BT convention

BEGZ arXiv:0812.3674v2, LF175--188, SHA256 6935e7b22f65e44e597df16e0d3f61db8fd131b34f83d0e0047f2612bd58bf5c.

```text
1.2. Local non-pluripolar products of currents. Let u1 , ..., up be psh func-
tions on X. If the uj ’s are locally bounded, then the fundamental work of Bedford-
Taylor [3] enables to deﬁne
                                ddc u1 ∧ ... ∧ ddc up
             MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                       5

on X as a closed positive (p, p)-current. The wedge product only depends on
the closed positive (1, 1)-currents ddc uj , and not on the speciﬁc choice of the
potentials uj .
   A very important property of this construction is that it is local in the plurifine
topology, in the following sense. If uj , vj are locally bounded psh functions on X
and uj = vj (pointwise) on a pluriﬁne open subset O of U , then
                   1O ddc u1 ∧ ... ∧ ddc up = 1O ddc v1 ∧ ... ∧ ddc vp .
This is indeed an obvious generalization of Corollary 4.3 of [4].
```

## Primary unit: Nonpluripolar definitions

BEGZ arXiv:0812.3674v2, LF189--242, SHA256 14edda72965b2b8a4d90c4cf9e4adb68eaaf60093fa10c9f376d90be736feb01.

```text
   In the case of a possibly unbounded psh function u, Bedford-Taylor have ob-
served (cf. p.236 of [4]) that it is always possible to deﬁne the non-pluripolar
part of the would-be positive measure (ddc u)n as a Borel measure. The main
issue however is that this measure is not going to be locally ﬁnite in general (see
Example 1.3 below). More generally, suppose we are trying to associate to any
p-tuple u1 , ..., up of psh functions on X a positive (a priori not necessarily closed)
(p, p)-current
                                   hddc u1 ∧ ... ∧ ddc up i
putting no mass on pluripolar subsets, in such a way that the construction is
local in the pluriﬁne topology in the above sense. Then we have no choice: since
uj coincides with the locally bounded psh function max(uj , −k) on the pluriﬁne
open subset                               \
                                   Ok := {uj > −k},
                                          j
we must have              ^               ^
                     1Ok h ddc uj i = 1Ok   ddc max(uj , −k),                    (1.1)
                            j                  j
Note that the
            V right-hand side is non-decreasing in k. This equation completely
determines h j ddc uj i since the latter is required not to put mass on the pluripolar
        S
set X − k Ok = {u = −∞}.
Definition 1.1. If u1 , ..., up are psh functions
                                             V on the complex manifold X, we
shall say that the non-pluripolar product h j ddc uj i is well-defined on X if for
each compact subset K of X we have
                      Z                ^
                  sup          ω n−p ∧   ddc max(uj , −k) < +∞               (1.2)
                     k   K∩Ok            j
for all k.
   Here ω is an auxiliary (strictly) positive (1, 1)-form on X with respect to which
masses are being measured, the condition being of course independent ofV   ω. When
(1.2) is satisﬁed, equation (1.1) indeed deﬁnes a positive (p, p)-current h j ddc uj i
on X. We will show below that it is automatically closed (Theorem 1.8).
   Condition (1.2) is always satisﬁed when p = 1, and in fact it is not diﬃcult to
show that
                               hddc ui = 1{u>−∞} ddc u.
There are however examples where non-pluripolar products are not well-deﬁned
as soon as p ≥ 2. This is most easily understood in the following situation.
6                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

Definition 1.2. A psh function u on X will be said to have small unbounded
locus if there exists a (locally) complete pluripolar closed subset A of X outside
which u is locally bounded.
   Assume that u1 , ..., up have small unbounded locus, and let A be closed com-
plete pluripolar such that each uj is locally bounded outside A V
                                                                (recall that com-
plete pluripolar subsets are stable under ﬁnite unions). Then h j ddc uj i is well-
                                          V
deﬁned iﬀ the Bedford-Taylor product j ddc uj , which is deﬁned on the open
                                                                        V
subset X −A, has locally ﬁnite mass near each point of A. In that case h j ddc uj i
                                        V
is nothing but the trivial extension of j ddc uj to X.
```

## Primary unit: Properties and convergence lemma

BEGZ arXiv:0812.3674v2, LF249--322, SHA256 1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2.

```text
    We now collect some basic properties of non-pluripolar products.
Proposition 1.4. Let u1 , ..., up be psh functions on X.
    • The operator                              ^
                            (u1 , ..., up ) 7→ h ddc uj i
                                                 j
         is local in theVplurifine topology whenever well-defined.
       • The current h j ddc uj i and the fact that it is well-defined both only depend
         on the currents ddc uj , not on the specific potentials uj .
       • Non-pluripolar products, which are obviously symmetric, are also multi-
         linear in the following sense: if v1 is a further psh function, then
                           ^                       ^                      ^
     h(ddc u1 + ddc v1 ) ∧    ddc uj i = hddc u1 ∧   ddc uj i + hddc v1 ∧    ddc uj i
                          j≥2                        j≥2                        j≥2

         in the sense that the left-hand side is well-defined iff both terms in the
         right-hand side are, and equality holds in that case.
Proof. Let us prove the ﬁrst point. If uj and vj are psh functions on X such
that uj = vj on a given pluriﬁne open subset O, then the locally bounded psh
functions max(uj , −k) and max(vj , −k) also coincide on O. If we set
                            \               \
                      Ek := {uj > −k} ∩ {vj > −k},
                                 j                   j

then we infer
                      ^                                      ^
              1O∩Ek       ddc max(uj , −k) = 1O∩Ek               ddc max(vj , −k),
                      j                                      j

hence in the limit               ^               ^
                             1O h ddc uj i = 1O h ddc vj i
                                 j                       j
              MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                               7

as desired by Lemma 1.5 below.
   We now prove the second point. Let wj be pluriharmonic on X, and let K be a
compact subset. We can ﬁnd C > 0 such that wj ≤ C on an open neighborhood
V of K. On the pluriﬁne open subset
                  \                         \
             Ok := {uj + wj > −k} ∩ V ⊂ {uj > −k − C} ∩ V
                         j                               j

the following locally bounded psh functions coincide:
     max(uj + wj , −k) = max(uj , −wj − k) + wj = max(uj , −k − C) + wj .
Since ddc wj = 0, it follows that
   Z           ^                         Z                         ^
         n−p          c
       ω     ∧    dd max(uj + wj , −k) =                 ω n−p ∧       ddc max(uj , −k − C)
    Ok           j                                  Ok             j
                     Z                              ^
                ≤    T                    ω n−p ∧       ddc max(uj , −k − C)
                         j {uj >−k−C}∩V             j
which is uniformly bounded in k by assumption, and the second point is proved.
   The proof of the last point is similarly easy but tedious and will be left to the
reader.                                                                           
                                                          V
Lemma 1.5. Assume that the non-pluripolar product h j ddc uj i is well-defined.
Then for every sequence of Borel subsets Ek such that
                                       \
                                Ek ⊂ {ui > −k}
                                             j
          S
and X −    k Ek is pluripolar, we have
                                   ^                        ^
                         lim 1Ek       ddc max(uj , −k)i = h ddc uj i
                         k→∞
                                   j                           j

against all bounded measurable functions.
Proof. This follows by dominated convergence from
                             ^                               ^
        (1∩j {uj >−k} − 1Ek ) ddc max(uj , −k)i ≤ (1 − 1Ek )h ddc uj i.
                                   j                                        j

                                                                                              
```

## Primary unit: Full integration-by-parts theorem and lemma

BEGZ arXiv:0812.3674v2, LF626--762, SHA256 59d8ae8186c59c9beb538816fed649a432c4bd8de0ccccc3501c3c2877126824.

```text
   We now establish a somewhat technical-looking integration-by-parts theorem
in this context that will be crucial in order to establish the basic properties of
weighted energy functionals in Proposition 2.8.
Theorem 1.14. Let A ⊂ X be a closed complete pluripolar subset, and let Θ be
a closed positive current on X of bidimension (1, 1). Let ϕi and ψi , i = 1, 2 be
quasi-psh functions on X that are locally bounded on X − A. If u := ϕ1 − ϕ2 and
v := ψ1 − ψ2 are globally bounded on X, then
          Z                   Z                    Z
                 uddc v ∧ Θ =       vddc u ∧ Θ = −      dv ∧ dc u ∧ Θ.
           X−A                 X−A                   X−A

  Note that the (signed) measureR ddc ϕi ∧ Θ deﬁned on X − A has ﬁnite total
mass thus so does ddc u ∧ Θ and X−A vddc u ∧ Θ is therefore well-deﬁned since
v is bounded (and deﬁned everywhere). The last integral is also well deﬁned by
Lemma 1.15 below and the Cauchy-Schwarz inequality.

Proof. As is well-known, if ϕ ≥ 0 is a bounded psh function, the identity
                          ddc ϕ2 = 2dϕ ∧ dc ϕ + 2ϕddc ϕ
enables to deﬁne dϕ ∧ dc ϕ ∧ Θ as a positive measure, which shows that dc ϕ ∧ Θ :=
dc (ϕΘ) is a current of order 0 by the Cauchy-Schwarz inequality. By linearity we
can therefore make sense of vdc u ∧ Θ and du ∧ dc u ∧ Θ as currents of order 0 on
X − A. By Lemma 1.15 below the positive measure du ∧ dc u ∧ Θ on X − A has
ﬁnite total mass, thus so does the current of order 0 vdc u∧ Θ by Cauchy-Schwarz.
   We claim that
              d[vdc u ∧ Θ] = dv ∧ dc u ∧ Θ + vddc u ∧ Θ on X − A.            (1.5)
To show this, we argue locally. We can then assume that u and v are locally
bounded psh functions by bilinearity. Let uk and vk be smooth psh functions
decreasing towards u and v respectively. Since dc u ∧ Θ has order 0, we see that
vk dc u ∧ Θ converges to vdc u ∧ Θ by monotone convergence. Since the right-hand
side of the desired formula is continuous along decreasing sequences of bounded
psh functions by Bedford-Taylor’s theorem, we can thus assume that v is smooth
and psh. Now uk Θ converges to uΘ, thus vdc uk ∧ Θ → vdc uk ∧ Θ, and we are
done by another application of Bedford-Taylor’s theorem to the right-hand side.
   In particular (1.5) shows that d[vdc u ∧ Θ] is a current of order 0 on X − A.
Let us somewhat abusively denote by 1X−A vdc u ∧ Θ and 1X−A d[vdc u ∧ Θ] the
trivial extensions to X. We are going to show that
                     d[1X−A vdc u ∧ Θ] = 1X−A d[vdc u ∧ Θ]                   (1.6)
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                    15

as currents on X. By Stokes’ theorem we will thus have
                            Z
                                  d[vdc u ∧ Θ] = 0,
                                X−A
and the desired formulae will follow by (1.5).
   The proof of (1.6) will again follow rather closely Sibony’s proof of the Skoda-
El Mir extension theorem [41, 18]. Note that (1.6) is a local equality, and that it
clearly holds on X −A. We will thus focus on a ﬁxed small enough neighbourhood
U of a given point 0 ∈ A. Since A is complete pluripolar around 0, we may by
deﬁnition ﬁnd a psh function τ on U such that {τ = −∞} = A near 0. If we pick
a smooth non-decreasing convex function χ on R such that χ(t) = 0 for t ≤ 1/2
and χ(1) = 1 and ﬁnally set
                                   wk := χ(eτ /k ),
then 0 ≤ wk ≤ 1 is a bounded psh function on U vanishing on A, and the
sequence wk increases to 1 pointwise on U − A as k → ∞. Now choose a smooth
non-decreasing function 0 ≤ θ(t) ≤ 1, t ∈ R such that θ ≡ 0 near 0 and θ ≡ 1
near 1 (we of course cannot require θ to be convex here). It then follows that
θ(wk ) vanishes near A and θ(wk ) → 1 pointwise on U − A, whereas θ ′ (wk ) → 0
pointwise on U . As a consequence we get
                        θ(wk )vdc u ∧ Θ → 1U −A vdc u ∧ Θ
and
                   θ(wk )d[vdc u ∧ Θ] → 1U −A d[vdc u ∧ Θ]
on U as k → ∞. Since
         d[θ(wk )vdc u ∧ Θ] = θ ′ (wk )vdwk ∧ dc u ∧ Θ + θ(wk )d[vdc u ∧ Θ]
by Lemma 1.9, we are thus reduced to showing that
                             θ ′ (wk )vdwk ∧ dc u ∧ Θ → 0
on U as k → ∞. But if ψ ≥ 0 is a given smooth function on U with compact
support, Cauchy-Schwarz implies
                Z                           2
                  ψθ ′ (wk )vdwk ∧ dc u ∧ Θ
               Z                     Z                                
           ≤       ψdwk ∧ dc wk ∧ θ         ψθ ′ (wk )2 v 2 du ∧ dc u ∧ Θ ,

and one concludes since
                    Z                 Z
                            c
                  2 ψdwk ∧ d wk ∧ Θ ≤   ψddc wk2 ∧ Θ
                                      Z
                                    =   wk2 ddc ψ ∧ Θ

is bounded whereas       Z
                             ψθ ′ (wk )2 v 2 du ∧ dc u ∧ Θ → 0

by dominated convergence since θ ′ (wk )2 → 0 pointwise.                         
16               S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

Lemma 1.15. Let ϕ1 and ϕ2 be two quasi-psh functions on X that are locally
bounded on an open subset U . If the difference u := ϕ1 − ϕ2 is globally bounded
on X, then
                          Z
                              du ∧ dc u ∧ Θ < +∞.
                                           U

Proof. By Demailly’s approximation theorem [19] we can ﬁnd decreasing se-
                               (k)
quences of smooth functions ϕi decreasing towards ϕi as k → ∞ and such
          (k)
that ddc ϕi ≥ −ω for some ﬁxed large enough Kähler form ω (see also [10]).
                                                                       (k)   (k)
Since u = ϕ1 − ϕ2 is bounded by assumption, it follows that uk := ϕ1 − ϕ2
can be taken to be uniformly bounded with respect to k. We can thus assume
that 0 ≤ uk ≤ C for all k.
  Now the formula ddc v 2 = 2vddc v + 2dv ∧ dc v and Bedford-Taylor’s continuity
theorem implies by polarization identities that
                                     (k)             (k)
                       lim dϕi             ∧ dc ϕj ∧ Θ = dϕi ∧ dc ϕj ∧ Θ
                         k

weakly on U for any two i, j, hence also
                             duk ∧ dc uk ∧ Θ → du ∧ dc u ∧ Θ
weakly on U . We thus get
                 Z                          Z
                    du ∧ dc u ∧ Θ ≤ lim inf   duk ∧ dc uk ∧ Θ,
                   U                                         k        X

and our goal is to show that the right-hand integrals are uniformly bounded. Now
Stokes theorem yields
                      Z                       Z
                                c
                         duk ∧ d uk ∧ Θ = −      uk ddc uk ∧ Θ
                         X                                               X
                         Z                                       Z
                                               (k)                             (k)
                     =           uk ddc ϕ2 ∧ Θ −                         uk ddc ϕ1 ∧ Θ.
                             X                                       X
For each i = 1, 2 we have
                                                           (k)                       (k)
                       0 ≤ uk (ω + ddc ϕi ) ≤ C(ω + ddc ϕi )
hence                        Z                                                Z
                                                  (k)
                   0≤                uk (ω + ddc ϕi ) ∧ Θ ≤ C                        ω∧Θ
                                 X                                              X
so that              Z                         Z                                    Z
                                                             (k)
                −C           ω∧Θ≤                    uk ddc ϕi ∧ Θ ≤ C                      ω∧Θ
                        X                       X                                       X
                                                                 R            c
for all k, and the uniform boundedness of                            X duk ∧ d uk ∧ Θ follows.    
```

## Primary unit: Positive products and nef volume convention

BEGZ arXiv:0812.3674v2, LF810--840, SHA256 aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e.

```text
Definition 1.17. Let α1 , ...αp ∈ H 1,1 (X, R) be big cohomology classes, and let
Ti,min ∈ αi be a positive current with minimal singularities. Then the cohomology
class of the non-pluripolar product hT1,min ∧ · · · ∧ Tp,min i is independent of the
choice of Ti,min ∈ αi with minimal singularities. It will be denoted by
                              hα1 · · · αp i ∈ H p,p (X, R)
18                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

and called the positive product of the αi . If α1 , ..., αn are merely psef, we set
                      hα1 · · · αp i := lim h(α1 + εβ) · · · (αp + εβ)i
                                      ε→0

where β ∈ H 1,1 (X, R) is an arbitrary Kähler class.
     As a special case, given a big class α the positive number
                                      vol(α) := hαn i
is called the volume of α
   Some explanations are in order. The positive product hα1 · · · αp i is not multi-
linear since the fact that T ∈ α and T ′ ∈ α′ both have minimal singularities
(in their respective cohomology classes) doesn’t imply that T + T ′ has minimal
singularities in α + α′ . Positive products are however homogeneous and non-
decreasing in each variable αi thanks to Theorem 1.16 when the αi ’s is big (with
respect to the partial order on cohomology induced by positive currents). These
two properties imply in a completely formal way (cf. Proposition 2.9 in [14]) that
hα1 · ... · αp i depends continuously on the p-tuple (α1 , ..., αp ) of big classes. We
can thus extend positive products to psef classes αi as indicated, the existence
of the limit and its independence on β being easy to check by monotonicity of
positive products.
   As an important special case, note that the positive product of nef classes αi
coincides with their ordinary cup-product, that is
                                 hα1 · · · αp i = α1 · · · αp .
   The volume vol(α) considered here coincides (as it should!) with the one
introduced in [11]. In fact:
```

## Primary unit: Full bounded/minimal energy proposition

BEGZ arXiv:0812.3674v2, LF1120--1222, SHA256 c1037903ef8126d0cb75ab0138d6ee5076fd0dd4d64ab91c9bcbad63e9124be2.

```text
2.2. Weighted energy functionals. By a weight function, we will mean a
smooth increasing function χ : R → R such that χ(−∞) = −∞ and χ(t) = t for
t ≥ 0.
Definition 2.7. Let χ be a weight function. We define the χ-energy of a θ-psh
function with minimal singularities ϕ as
                                n Z
                          1 X                                n−j
               Eχ (ϕ) :=              (−χ)(ϕ − ϕmin )hT j ∧ Tmin i      (2.1)
                         n+1        X      j=0

with T = θ + ddc ϕ and Tmin = θ + ddc ϕmin .
  Recall that we have ﬁxed an arbitrary θ-psh function ϕmin with minimal sin-
gularities on X. Note that the χ-energy functional for χ(t) = t is nothing but
the Aubin-Mabuchi energy functional (up to a minus sign, cf. [2, 37] and [5] for
the extension to the singular setting).
  The next proposition contains important properties of the χ-energy.
Proposition 2.8. Let χ be a convex weight function. Then the following prop-
erties hold.
     (i) For any θ-psh function ϕ with minimal singularities the sequence
                            Z
                                                      n−j
                       j 7→    (−χ)(ϕ − ϕmin )hT j ∧ Tmin i
                                      X
          as in (2.1) is non-decreasing. In particular we have
                           Z
                 Eχ (ϕ) ≤    (−χ)(ϕ − ϕmin )MA (ϕ) ≤ (n + 1)Eχ (ϕ)
                               X
           if ϕ ≤ ϕmin .
      (ii) The χ-energy ϕ 7→ Eχ (ϕ) is non-increasing.
     (iii) If ϕk decreases to ϕ with minimal singularities, then Eχ (ϕk ) → Eχ (ϕ).
Proof. Let u := ϕ − ϕmin ≤ 0. Note that χ(u) + ϕmin is also a θ-psh function
with minimal singularities, since
                ddc χ(u) = χ′ (u)ddc u + χ′′ (u)du ∧ dc u ≥ −(θ + ddc ϕmin ).                (2.2)
It follows that the bounded functions u and χ(u) are both diﬀerences of quasi-
psh functions which are locally bounded on the complement X − A of a closed
complete pluripolar subset A. We can thus apply the integration-by-parts formula
of Theorem 1.14 to get
Z                                     Z
                             n−j−1                                         n−j−1
    (−χ)(ϕ − ϕmin )hT j+1 ∧ Tmin   i=      (−χ)(u)(Tmin + ddc u) ∧ T j ∧ Tmin
 X                                               X−A
          Z                                           Z
                                       j      n−j                                        n−j−1
      =             (−χ)(ϕ − ϕmin )T       ∧ Tmin +             χ′ (u)du ∧ dc u ∧ T j ∧ Tmin
              X−A                                         X−A
                                  Z
                                                              n−j
                              ≥        (−χ)(ϕ − ϕmin )hT j ∧ Tmin i
                                   X
for j = 0, ..., n − 1, and (i) follows.
              MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                            25

  In order to prove (ii) let v ≥ 0 be a bounded function such that ϕ + v is still
θ-psh. We will show that the derivative at t = 0 of the function t 7→ e(t) :=
Eχ (ϕ + tv) is ≤ 0. Indeed integration by parts yields
                Xn Z
                                        n−j                         n−j
   − e′ (0) =             vχ′ (u)T j ∧ Tmin + jχ(u)ddc v ∧ T j−1 ∧ Tmin
                      j=0 X−A
                      Xn Z
                                                n−j                         n−j
              =                   vχ′ (u)T j ∧ Tmin + jvddc χ(u) ∧ T j−1 ∧ Tmin
                      j=0   X−A

                      Xn Z
                                                n−j                                  n−j
              ≥                   vχ′ (u)T j ∧ Tmin + jvχ′ (u)(T − Tmin ) ∧ T j−1 ∧ Tmin
                      j=0   X−A
                             Z
              = (n + 1)                    vχ′ (u)T n ≥ 0,
                                 X−A
by (2.2).
   Finally let us prove (iii). If ϕk decreases to ϕ, then χ(ϕk − ϕmin ) + ϕmin
is a sequence of θ-psh functions decreasing towards χ(ϕ − ϕmin ) + ϕmin , thus
Bedford-Taylor’s theorem implies that
                                   lim Tkj ∧ Tmin
                                              n−j          n−j
                                                  = T j ∧ Tmin
                                       k
and
                                          n−j
                  lim χ(ϕk − ϕmin )Tkj ∧ Tmin                      n−j
                                              = χ(ϕ − ϕmin )T j ∧ Tmin
                   k
weakly on X − A. But Theorem 1.16 implies that the total masses also converge,
since in fact       Z                 Z
                                       Tkj ∧ Tmin
                                              n−j
                                                  =                     n−j
                                                                 T j ∧ Tmin
                              X−A                        X−A
for all k, the thus trivial extensions converge on the whole of X, i.e.
                                  limhTkj ∧ Tmin
                                             n−j             n−j
                                                 i = hT j ∧ Tmin i
                                   k
Since χ(ϕk − ϕmin ) is uniformly bounded, it follows from Bedford-Taylor’s mono-
tone convergence theorem [4] that
             Z                               Z
                                j    n−j                             n−j
         lim   χ(ϕk − ϕmin )hTk ∧ Tmin i =       χ(ϕ − ϕmin )hT j ∧ Tmin i
          k       X                                          X
for all j, which concludes the proof.                                                      
```
