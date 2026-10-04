# Immutable primary-source bodies

The following are literal LF ranges from the read-only supplied sources. The supplied range hashes use LF joins without an added final LF. Form feeds, extraction defects and printed mathematical defects are retained.

## BEGZ-0812.3674v2-20261004.txt, LF249--322

SHA256 `1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2`; supplied pin matches: True.

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

## BEGZ-0812.3674v2-20261004.txt, LF810--840

SHA256 `aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e`; supplied pin matches: True.

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

## DDNL18-2049-2087-20261004.txt, LF319--347

SHA256 `e8359844609c8b19e21d4c36df028505fde5b80cc75e59f274dd4b5d282fa62e`; supplied pin matches: True.

```text

Proposition 2.1. Let θ j , j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology
classes are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j has the same singularity type as v j ,
j ∈ {1, . . . , n}. Then
                                  Z                           Z
                                        θu 1 ∧ · · · ∧ θu n =
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                            X                         X

   The proof of this result uses the arguments in [Boucksom et al. 2010, Corollary 2.15].

Proof. First we note that we can assume that the classes {θ j } are in fact big. Indeed, if this is not the
case we can just replace each θ j with θ j + εω, and using the multilinearity of the nonpluripolar product
[Boucksom et al. 2010, Proposition 1.4] we can let ε → 0 at the end of our argument to conclude the
statement for pseudoeffective classes.
   For each t ∈ 1 = {t = (t1 , . . . , tn ) ∈ Rn | t j > 0} consider u t := j t j u j , vt := j t j v j and θ t := j t j θ j.
                                                                           P                 P                    P

Clearly, {θ t } is big, and u t has the same singularities as vt . Hence it follows from [Witt Nyström 2017,
Theorem 1.2] that X (θutt )n = X (θvtt )n for all t ∈ 1. On the other hand, using multilinearity of the
                       R             R

nonpluripolar product again [Boucksom et al. 2010, Proposition 1.4], we see that both t → X (θutt )n and
                                                                                                             R

t → X (θvtt )n are homogeneous polynomials of degree n. Our last identity forces all the coefficients of
     R

these polynomials to be equal, giving the statement of our result.                                                       

```

## DDNL18-2049-2087-20261004.txt, LF448--469

SHA256 `e4220e2892907b2d1d5b17de4aa57b3b1542060bda2e4dfcf8944f945cba0c20`; supplied pin matches: True.

```text

Theorem 2.4. Let θ j, j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology classes
are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j is less singular than v j for all j ∈ {1, . . . , n}.
Then                                  Z                       Z
                                        θu 1 ∧ · · · ∧ θu n ≥
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                                   X                            X
        MONOTONICITY OF NONPLURIPOLAR PRODUCTS AND COMPLEX MONGE–AMPÈRE EQUATIONS                                    2057


Proof. By the same reason as in Proposition 2.1, we can assume that the classes {θ j } are in fact big. For
each t > 0 we set v jt := max(u j − t, v j ) for j = 1, . . . , n. Observe that the v jt converge decreasingly to v j
as t → ∞. In particular, by [Guedj and Zeriahi 2005, Proposition 3.7] the convergence holds in capacity.
As v jt and u j have the same singularity type, it follows from Proposition 2.1 that
                                   Z                          Z
                                       θu 1 ∧ · · · ∧ θu n =
                                          1            n
                                                                  θv1t ∧ · · · ∧ θvnnt .
                                                                           1
                                        X                            X

Letting t → ∞, the first part of Theorem 2.3 allows us to conclude the argument.                                       

```

## Xia-1907.06359v1-20261004.txt, LF250--265

SHA256 `ea927250996b0a51fa4f7aa3612fd7e300be9c3327b0776093caacb4cc9f97f3`; supplied pin matches: True.

```text

2.4. Integration by parts. In the sequel, for ϕ1 , ϕ2 ∈ PSH(X, θ), we write [ϕ1 ] =
[ϕ2 ] if there is a constant C > 0, such that
                                      ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C.
Theorem 2.7. Let γ1 , . . . , γn−1 ∈ PSH(X, θ). Let ϕj , ψj ∈ PSH(X, θ) (j = 1, 2).
Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 . Assume that
                                     [ϕ1 ] = [ϕ2 ],    [ψ1 ] = [ψ2 ].
Then
          Z                                                Z
(2.8)           u ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 =         v ddc u ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 .
            X                                               X

Remark 2.2. Here
ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 := θψ1 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 − θψ2 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1
is understood as a signed measure. This definition is independent of the choice of
θψ1 and θψ2 by [BEGZ10] Proposition 1.4. Other similar expressions are understood
in the same way.

```

## Xia-1907.06359v1-20261004.txt, LF780--829

SHA256 `fe693acf6a3033eb6bed734b0c9d194f4e59497e7aabf4c646bfbccf87bc72c8`; supplied pin matches: True.

```text

Corollary 2.15. Let αj (j = 0, . . . , n) be big cohomology classes on X. Let θj
(j = 0, . . . , n) be smooth representatives in αj . Let γj ∈ PSH(X, θj ) (j = 2, . . . , n).
Let ϕ1 , ϕ2 ∈ PSH(X, θ0 ), ψ1 , ψ2 ∈ PSH(X, θ1 ). Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 .
Assume that
                                 [ϕ1 ] = [ϕ2 ], [ψ1 ] = [ψ2 ].
Then
         Z                                                       Z
(2.21)        u ddc v ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn =                  v ddc u ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn .
          X                                                       X

Proof. Take α = (a0 , . . . , an ) ∈ Rn+1
                                      ≥0 . Let
                                                     n
                                                     X
                                             θα =          aj θj .
                                                     j=0

Let
                                  n
                                  X
                          γα =          aj γj ,   γ̃α = a0 ϕ1 + a1 ψ1 + γα .
                                  j=2

Note that
                    a0 u = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ2 + a1 ψ1 + γα ) ,
                    a1 v = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ1 + a1 ψ2 + γα ) .
So by Theorem 2.7,
                             Z                                       Z
                     a0 a1       u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   = a0 a1                 v ddc u ∧ θα,γ̃
                                                                                      n−1
                                                                                           α
                                                                                             .
                             X                                        X
So for a0 > 0, a1 > 0,
                             Z                           Z
                                 u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   =             v ddc u ∧ θα,γ̃
                                                                            n−1
                                                                                 α
                                                                                   .
                             X                             X
Since both sides are polynomials in a0 , . . . , an , this means that all coefficients are
equal. In particular, the coefficients of
                                                  a 2 . . . an
are equal, hence proving (2.21).                                                                                          

```

## Vu-2004.11111v1-20261004.txt, LF178--189

SHA256 `13226a964e640ebeb8283a6342682cdf2f98a328d37f5386efe3e2e844ca2cef`; supplied pin matches: True.

```text

supported by a postdoctoral fellowship of the Alexander von Humboldt Foundation.

Notation and convention. For a closed positive current T on a compact complex man-
ifold X, we denote by {T } the cohomology class of T and ν(T, x) denotes the Lelong
number of T at x. Recall that the wedge product on closed smooth forms induces the
cup-product on their de Rham cohomology classes. We use the same notation “ ∧ ” to
denote these two products.
    Recall dc = 2πi (∂ − ∂) and ddc = πi ∂∂. We use &, . to denote ≥, ≤ modulo some
multiplicative constant independent of parameters in question. For a Borel set A ⊂ X,
we denote by 1A the characteristic function of A, that means 1A is equal to 1 on A and 0
elsewhere. For every current R of order 0 on X, we denote by kRkA the mass of R on A.


```

## Vu-2004.11111v1-20261004.txt, LF580--642

SHA256 `c097f459c8e4b862a8067519ab86b09613638b11af2d3e83b3766244458bf625`; supplied pin matches: True.

```text

Theorem 2.6. Let U ⊂ Cn be an open set. Let (Tk )k be a sequence of closed positive currents
satisfying Condition (∗) so that Tk converges to a closed positive current T on U as k → ∞.
Let uj be a locally bounded psh function on U for 1 ≤ j ≤ m. Let (ujk )k∈N be a sequence of
locally bounded psh functions converging to uj in L1loc as k → ∞. Then, the convergence

                u1k ddc u2k ∧ · · · ∧ ddc umk ∧ Tk → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T    (2.10)

as k → ∞ holds provided that one of the following conditions is fulfilled:
    (i) ujk (x) ր uj (x) for every x ∈ U as k → ∞,
    (ii) ujk (x) ր uj (x) for almost everywhere x ∈ U (with respect to the Lebesgue measure)
and T has no mass on pluripolar sets,
    (iii) ujk ≥ uj for every j, k.

Proof. Given that we already have a uniform strong quasi-continuity for bounded psh
functions, the desired result can be deduced without difficulty from proofs of classical
results on the convergence of Monge-Ampère operators, for example, see [17].
   We present here a proof of Theorem 2.6 for the readers’ convenience. First of all,
observe that if ujk ր uj almost everywhere then, we have ujk ≤ uj(k+1) ≤ uj pointwise
on U and the set {x ∈ U : uj (x) 6= limk→∞ ujk (x)} is pluripolar. By the localization




                                                11
principle ([17, Page 7]), we can assume that ujk , uj are all equal to some smooth psh
function ψ outside some set K ⋐ U on U. We prove (i), (ii) simultaneously. Let

            Sjk := ddc ujk ∧ · · · ∧ ddc umk ∧ Tk ,   Sj := ddc uj ∧ · · · ∧ ddc um ∧ T.

We prove by induction in j that

                                      u(j−1)k Sjk → u(j−1) Sj                              (2.11)

k and for every 2 ≤ j ≤ m + 1 (by convention we put S(m+1)k := Tk and Sm+1 := T ). The
claim is true for j = m + 1. Suppose that it holds for (j + 1). We need to prove it for
j. Let Rj∞ be a limit current of u(j−1)k Sjk as k → ∞. By induction hypothesis (2.11) for
(j + 1) instead of j, Sjk → Sj as k → ∞. This combined with the fact that the sequence
(ujk )k converges in L1loc to uj gives

                                          Rj∞ ≤ uj−1Sj                                     (2.12)

(one can see [15, Proposition 3.2]). On the other hand, since (ujk )k is increasing, using
Corollary 2.5, we obtain

                       lim inf u(j−1)k Sjk ≥ lim inf u(j−1)s Sjk = u(j−1)s Sj
                        k→∞                   k→∞

for every s ∈ N. Letting s → ∞ in the last inequality gives

                 Rj∞ ≥ ( lim u(j−1)s )Sj = uj−1Sj + ( lim u(j−1)s − uj−1)Sj .              (2.13)
                          s→∞                             s→∞

Recall that the set of x ∈ U with uj−1(x) > lims→∞ u(j−1)s (x) is empty in the setting of
(i) and is a pluripolar set in the setting of (ii). Hence (2.11) follows from Lemma 2.1,
(2.13) and (2.12). We have proved (i) and (ii). We prove (iii) by similar induction. The
proof is finished.

Remark 2.7. By the above proof and Lemma 2.1, Property (ii) of Theorem 2.6 still holds if
instead of requiring T has no mass on pluripolar sets, we assume the following two condi-
tions:
    (i) T has no mass on Aj := {x ∈ U : uj (x) 6= limk→∞ ujk (x)} for every 1 ≤ j ≤ m and,
    (ii) the set Aj is locally complete pluripolar for every j.
    Just by replacing the usual quasi-continuity of psh functions by the stronger one given

```

## Vu-2004.11111v1-20261004.txt, LF945--1115

SHA256 `b344c4bd11aa3280719cd1b8a3f08d8fff48bb7600168dd303519fb16061142d`; supplied pin matches: True.

```text

Definition 3.3. We say that the non-pluripolar product relative to T of T1 , . . . , Tm is well-
defined if (3.2) holds for every small enough local chart U of X, or equivalently, (3.7)
holds. In this case, the non-pluripolar product relative to T of T1 , . . . , Tm , which is denoted
                    ˙ i, is defined to be the current R̃ in Lemma 3.2.
by hT1 ∧ · · · ∧ Tm ∧T
   When T is the current of integration along X, we simply write hT1 ∧ · · · ∧ Tm i for the
non-pluripolar product relative to T of T1 , . . . , Tm . One can see that this is exactly the
usual non-pluripolar product of T1 , . . . , Tm defined in [2, 16, 4]. We note that in general
                             ˙ i can have mass on pluripolar sets in ∩m
the current hT1 ∧ · · · ∧ Tm ∧T                                              j=1 {uj > −∞},
see, however, Property (iii) of Proposition 3.5 below. Arguing as in the proof of [4,
Proposition 1.6], we obtain the following result.
                                                                               ˙ i is
Lemma 3.4. Assume that X is a compact Kähler manifold. Then, hT1 ∧ · · · ∧ Tm ∧T
well-defined.
    For a closed positive (1, 1)-current R, recall that the polar locus IR of R is the set of
points where potentials of R are equal to −∞. Note that by Lemma 3.1, the current
                 ˙ i has no mass on ∪m
hT1 ∧ · · · ∧ Tm ∧T                   j=1 ITj . We collect here some more basic properties of
relative non-pluripolar products.
Proposition 3.5. (i) The product hT1 ∧ · · · ∧ Tm ∧T  ˙ i is symmetric with respect to T1 , . . . , Tm .
      (ii) Given a positive real number λ, we have h(λT1 ) ∧ T2 ∧ · · · ∧ Tm ∧T˙ i = λhT1 ∧ T2 ∧
             ˙
· · · ∧ Tm ∧T i.
      (iii) Given a complete pluripolar set A such that T has no mass on A, then hT1 ∧ T2 ∧
· · · ∧ Tm ∧T˙ i also has no mass on A.
      (iv) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above. Assume that
h∧m         ˙       ′    m      ˙                                    ′     m      ˙
     j=1 Tj ∧T i, hT1 ∧ ∧j=2 Tj ∧T i are well-defined. Then h(T1 + T1 ) ∧ ∧j=2 Tj ∧T i is also well-
defined and satisfies

                (T1 + T1′ ) ∧ ∧m      ˙           m      ˙        ′    m      ˙
                               j=2 Tj ∧T ≤ hT1 ∧ ∧j=2 Tj ∧T i + hT1 ∧ ∧j=2 Tj ∧T i.             (3.12)

The equality occurs if T has no mass on IT1 ∪ IT1′ .
    (v) Let 1 ≤ l ≤ m be an integer. Let Tj′′ be a closed positive (1, 1)-current on X and Tj , T
as above for 1 ≤ j ≤ l. Assume that Tj′′ ≥ Tj for every 1 ≤ j ≤ l and T has no mass on
∪lj=1 ITj′′ −Tj . Then, we have

                             h∧lj=1Tj′′ ∧ ∧m        ˙        m      ˙
                                           j=l+1 Tj ∧T i ≥ h∧j=1 Tj ∧T i


provided that the left-hand side is well-defined.
   (vi) Let 1 ≤ l ≤ m be an integer. Assume R := h∧m               ˙          l      ˙
                                                          j=l+1 Tj ∧T i and h∧j=1 Tj ∧Ri are
                                m     ˙ i = h∧j=1 Tj ∧Ri.
well-defined. Then, we have h∧j=1 Tj ∧T         l    ˙




                                                  17
                                                                           ˙ i is well-defined.
   (vii) Let A be a complete pluripolar set. Assume that hT1 ∧T2 ∧· · ·∧Tm ∧T
Then we have

                                          ˙ i = T1 ∧ T2 ∧ · · · ∧ Tm ∧(1
               1X\A hT1 ∧ T2 ∧ · · · ∧ Tm ∧T                         ˙ X\A T ) .

In particular, the equality
                                     h∧m      ˙        m      ˙ ′
                                       j=1 Tj ∧T i = h∧j=1 Tj ∧T i

holds, where T ′ := 1X\∪m
                        j=1 ITj
                                T.

Proof. Properties (i), (ii) are clear from the definition and the proof of Lemma 3.1. We
now check (iii). Let R := h∧m          ˙
                                j=1 Tj ∧T i. Since T has no mass on the complete pluripolar
set A, using Lemma 2.1 gives 1A ∧m            c
                                       j=1 dd ujk ∧ T = 0 for every k. Using this and Lemma
3.1, we deduce that

                   1A 1∩m
                        j=1 {uj >−k}
                                     R = 1A 1∩m
                                              j=1 {uj >−k}
                                                           ∧m     c
                                                            j=1 dd ujk ∧ T = 0.


Hence R = 0 on A and (iii) follows.
   We prove (iv). We work on a small local chart U. Write Tj′ = ddc u′j , u′jk := max{u′j , −k}.
Recall Tj = ddc uj . We can assume uj , u′j ≤ 0. Let R′ := hT1′ ∧ ∧m           ˙
                                                                      j=2 Tj ∧T i and R :=
                                                                                           ′′

h(T1 + T1′ ) ∧ ∧m      ˙
                j=2 Tj ∧T i. We have


                                max{u1 + u′1 , −k} = u1k + u′1k

on {u1 + u′1 > −k} because the last set is contained in {u1 > −k} ∩ {u′1 > −k}. This
combined with Lemma 3.1 yields

                                      1Bk′′ R′′ = 1Bk′′ R + 1Bk′′ R′ ,

where Bk′′ := {u1 + u′1 > −k} ∩ ∩m
                                 j=2 {uj > −k}. Letting k → ∞ in the last equality gives
(3.12). Observe that
                              1U \Bk′′ R → 1IT1 ∪IT ′ ∪ ∪m
                                                         j=2 ITj
                                                                 R
                                                            1

as k → ∞. The last limit is equal to 1IT ′ R because R has no mass on ∪m      j=1 ITj . Moreover
                                          1
since IT1′ is complete pluripolar and T has no mass on IT1′ , by (iii), we have that 1IT ′ R = 0.
                                                                                         1
Consequently, 1U \Bk′′ R → 0 as k → ∞ and a similar property of R′ also holds. Thus we
obtain the equality in (3.12) if T has no mass on IT1 ∪ IT1′ . To get (v), we just need to
decompose Tj′′ = Tj + Tj′ for some closed positive current Tj′ and use similar arguments
as in the proof of (iv).
    We prove (vi). We can assume uj ≤ 0 for every 1 ≤ j ≤ m. Let
                                                      m
                                          −1
                                                     X
                               ψk := k         max          uj , −k + 1.
                                                      j=1


Observe that 0 ≤ ψk ≤ 1 and

                                ψk = 0         on ∪m
                                                   j=1 {uj ≤ −k}.




                                                     18
Note that R has no mass on ITj for l + 1 ≤ j ≤ m. This combined with (iii) yields
               ˙
that h∧lj=1 Tj ∧Ri   gives no mass on ITj for 1 ≤ j ≤ m. Using this and the fact that
ψk ր 1X\∪m  j=1 ITj
                    yields

                h∧lj=1Tj ∧Ri
                         ˙   = lim ψk h∧lj=1 Tj ∧Ri
                                                ˙   = lim ψk ∧lj=1 ddc ujk ∧ R.            (3.13)
                                 k→∞                     k→∞

Now since ψk R = ψk ∧m       c
                     j=l+1 dd ujk ∧ T (Lemma 3.1), we get


                           ψk ∧lj=1 ddc ujk ∧ R = ψk ∧m     c
                                                      j=1 dd ujk ∧ T.                      (3.14)

To see why the last equality is true, notice that it is clear if ujk ’s are smooth and in
general, we can use sequences of smooth psh functions decreasing to ujk for 1 ≤ j ≤ l
and the convergences of Monge-Ampère operators to obtain (3.14). Combining (3.14)
with (3.13) gives the desired assertion.
   It remains to prove (vii). Let ψk be as above.   Let A = {ϕ = −∞}, where ϕ is a
                                                  Pm
negative psh function. Define ψk := k max ϕ + j=1 uj , −k + 1. Since 0 ≤ ψk′ ≤ ψk ,
                                ′     −1
                                             

we get {ψk = 0} ⊂ {ψk′ = 0}. It follows that

        ψk′ hT1 ∧ T2 ∧ · · · ∧ Tm ∧T
                                  ˙ i = ψk′ ∧m     c           ′  m     c
                                             j=1 dd ujk ∧ T = ψk ∧j=1 dd ujk ∧ (1X\A T )

because T = 1X\A T on {ψk′ 6= 0} and the convergence of Monge-Ampère operators.
Letting k → ∞ gives the desired assertion. The proof is finished.
   The following result clarifies the relationship between the relative non-pluripolar
product and some other known notions of intersection.

```

## Vu-2004.11111v1-20261004.txt, LF1200--1247

SHA256 `e12bdb4d6ebd643be2cf987df4ee89b060c1b8930c06b2bc8c8df732630376aa`; supplied pin matches: True.

```text

Theorem 3.7. Assume that hT1 ∧ · · · ∧ Tm ∧T                                         ˙ i is
closed.

Proof. The proof is based on ideas from [20, 4]. We work on a local chart U as above.
By shrinking U and subtracting from uj a suitable constant, we can assume that uj ≤ 0.
Let                                         m
                                            X
                            ψk := k −1 max{   uj , −k} + 1.
                                                j=1

Observe that ψk = 0 on ∪m
                        j=1 {uj ≤ −k} and 0 ≤ ψk ≤ 1 increases to 1∩m
                                                                    j=1 {uj >−∞}
                                                                                 .
                                                                                Let
                                                              ′        ′
g : R → R be a non-negative smooth function such that g(0) = g (0) = g (1) = 0 and
g(1) = 1. Let Rk , R be as above. Since g(1) = 1 and g(0) = 0, we get g(ψk )R → R



                                               20
as k → ∞ (recall R has no mass on ∪m
                                   j=1 {uj = −∞}). Thus the desired assertion is
equivalent to proving that
                                     dR = lim d(g(ψk )R) = 0.                                    (3.19)
                                            k→∞

Since g(ψk ) = g(0) = 0 on ∪m
                            j=1 {uj ≤ −k}, we have

                            d(g(ψk )R) = d(g(ψk )Rk ) = g ′ (ψk )dψk ∧ Rk
(see [4, Lemma 1.9] or Corollary 2.5 for the second equality). Let U1 ⋐ U2 be relatively
compact open subsets of U. By the Cauchy-Schwarz inequality, we have
                  kg ′(ψk )dψk ∧ Rk kU1 . kdψk ∧ dc ψk ∧ Rk kU1 kg ′(ψk )2 Rk kU1 .
Using dψk ∧ dc ψk = ddc ψk2 − ψk ddc ψk and the Chern-Levine-Nirenberg inequality, one get
                 kdψk ∧ dc ψk ∧ Rk kU1 . kψk Rk kU2 ≤ kRk kU 2 ∩∩m
                                                                 j=1 {uj >−k}
                                                                              .1

by (3.2). On the other hand, using the equality g ′ (ψk ) = g ′ (0) = 0 on {uj ≤ −k}, we
obtain
                    g ′(ψk )2 Rk = g ′(ψk )2 1∩m
                                               j=1 {uj >−k}
                                                            Rk = g ′(ψk )2 R
converging to 0 as k → ∞ because g ′(ψk ) → g ′ (1) = 0 on ∩m
                                                            j=1 {uj > −∞}. Thus (3.19)
follows. This finishes the proof.

```

## Vu-2004.11111v1-20261004.txt, LF1259--1565

SHA256 `09034b5477c57c8812f3b677bf5ba3504db9a417938f90d7fb91fd28903246a8`; supplied pin matches: True.

```text



4     Monotonicity
In this section, we present a monotonicity property for relative non-pluripolar products.
We begin with the following simple lemma.
Lemma 4.1. Let U be an open subset of Cn . Let (ulj )l be a sequence of psh functions on U
and uj a psh function on U for 1 ≤ j ≤ m. Let (Tl )l be a sequence of closed positive currents
satisfying Condition (∗) and Tl converges to a closed positive current T on U as l → ∞.
Assume that one of the following conditions is satisfied:
    (i) ulj ≥ uj and ulj converges to uj in L1loc as l → ∞.
    (ii) ulj increases to uj as l → ∞ almost everywhere and T has no mass on pluripolar
sets.
    Then, for every smooth weakly positive form Φ with compact support in U, we have
                           Z                            Z
                    lim inf h∧j=1 dd uj ∧Tl i ∧ Φ ≥ h∧m
                                 m    c l ˙                       c   ˙
                                                            j=1 dd uj ∧T i ∧ Φ.
                      l→∞     U                            U




                                                  21
    When T is the current of integration along X, a related statement in the compact
setting was given in [8, Theorem 2.3].

Proof. Let Φ be a smooth weakly positive form with compact support in U. Assume (i)
holds. Let uljk := max{ulj , −k} which converges to ujk := max{uj , −k} in L1loc as l → ∞
and uljk ≥ ujk . Put

                        Rl := h∧m     c l ˙
                                j=1 dd uj ∧Tl i,              Rkl := ∧m     c l
                                                                      j=1 dd ujk ∧ T.


Similarly, we define R, Rk by using the formula of Rl , Rkl respectively with ulj , uljk replaced
by uj , ujk . Since ulj ≥ uj , we get
                         Z                           Z
                                             l
                            1∩m      l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {uj >−k}
                                                                      Rkl ∧ Φ.              (4.1)
                         U                                     U

By Theorem 2.6, we get Rkl → Rk as l → ∞. Using this together with the fact that when
k is fixed, uljk is uniformly bounded in l, we see that the strong uniform quasi-continuity
for ujk with respect to (Tl )l (see Theorem 2.4) implies
              Z                                    Z
                                   l
      lim inf     1∩mj=1 {uj >−k}
                                  Rk ∧ Φ = lim inf     1∩m j=1 {ujk >−k}
                                                                         Rkl ∧ Φ
        l→∞     U                            l→∞     U
                                           Z                                 Z
                                         ≥     1∩m
                                                 j=1 {ujk >−k}
                                                                Rk ∧ Φ =        1∩m
                                                                                  j=1 {uj >−k}
                                                                                               Rk ∧ Φ
                                           Z U                                U

                                         =     1∩m
                                                 j=1 {uj >−k}
                                                               R ∧ Φ.
                                                 U

This combined with (4.1) yields
        Z                                 Z
           1∩m
             j=1 {uj >−k}
                          R ∧ Φ ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            Rkl ∧ Φ
         U                          l→∞    U
                                          Z                                 Z
                                                              l
                                ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            R ∧ Φ ≤ lim inf   Rl ∧ Φ
                                           l→∞       U                             l→∞   U

for every k. Letting k → ∞ in the last inequality and noticing that R has no mass on
∪mj=1 {uj = −∞} give the desired assertion.
    Now assume (ii). Note that
                                     ulj ≤ ul+1
                                            j   ≤ uj
for every l, j. Thus, {ulj > −k} ⊂ {ul+1 j   > −k} ⊂ {uj > −k} and ũj := liml→∞ ulj ≤ uj .
Using this and arguments similar to those in the previous paragraph, we have
                           Z                         Z
                                             l
                   lim inf   1∩m     l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {ũj >−k}
                                                                       R ∧ Φ.
                     l→∞       U                                   U

Letting k → ∞ gives
                                       Z                 Z
                                           l
                             lim inf       R ∧Φ≥              1∩m
                                                                j=1 {ũj >−∞}
                                                                              R ∧ Φ.
                              l→∞      U                 U




                                                         22
Recall that {uj > ũj } is pluripolar. This coupled with the fact that T has no mass on
pluripolar sets and Property (iii) of Proposition 3.5 yields
                          Z            Z                        Z
                              l
                  lim inf    R ∧Φ≥       1∩j=1 {uj >−∞} R ∧ Φ =
                                            m                     R ∧ Φ.
                     l→∞     U                U                                 U

This finishes the proof.

    Recall that for closed positive (1, 1)-currents R1 , R2 on X, we say that R1 is less sin-
gular than R2 if for every local chart U and psh function wj on U such that Rj = ddc wj
on U for j = 1, 2, then w2 ≤ w1 + O(1) on compact subsets of U; and R1 , R2 are of the
same singularity type if w1 ≤ w2 + O(1) and w2 ≤ w1 + O(1) on compact subsets of U. The
following generalizes [8, Proposition 2.1], see also [21, 18].
Proposition 4.2. Let X be a compact complex manifold of dimension n. Let m be an integer
such that 1 ≤ m ≤ n. Let T be a closed positive current of bi-degree (p, p) on X. Let Tj , Tj′
be closed positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are of the same
singularity type and Tj = ddc uj + θj , Tj′ := ddc u′j + θj , where θj is a smooth form and
u′j , uj are θj -psh functions, for every 1 ≤ j ≤ m. Assume that for every J, J ′ ⊂ {1, . . . , m}
                                                             ˙ i is well-defined. Then, for every
such that J ∩ J ′ = ∅, the product h∧j∈J Tj ∧ ∧j ′ ∈J ′ Tj′′ ∧T
    c
dd -closed smooth form Φ, we have
                      Z                              Z
                            ′           ′ ˙                             ˙ i ∧ Φ.
                         hT1 ∧ · · · ∧ Tm ∧T i ∧ Φ =   hT1 ∧ · · · ∧ Tm ∧T                  (4.2)
                     X                                     X

Proof. By compactness of X, we can assume uj , u′j ≤ 0. By the hypothesis, {uj = −∞} =
{u′j = −∞} and wj := uj − u′j is bounded outside {uj = −∞}. Without loss of generality,
we can assume that

                                                  |wj | ≤ 1                                  (4.3)

outside {uj = −∞}. Let A := ∪m  j=1 {uj = −∞} which is a complete pluripolar set. Put
ujk := max{uj , −k}, ujk := max{u′j , −k} and
                      ′


                                                   n
                                                   X
                              ψk := k −1 max{            (uj + u′j ), −k} + 1                (4.4)
                                                   j=1


which is quasi-psh and 0 ≤ ψk ≤ 1, ψk (x) increases to 1 for x 6∈ A. We have ψk (x) = 0 if
uj (x) ≤ −k or u′j (x) ≤ −k for some j. Put wjk := ujk − u′jk . By (4.3), we have

                                                  |wjk | ≤ 1                                 (4.5)

on X. Let J, J ′ ⊂ {1, . . . , n} with J ∩ J ′ = ∅ and

                    RJJ ′ k := ∧j∈J (ddc ujk + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ k + θj ′ ) ∧ T.

The last current is the difference of two closed positive (|J| + |J ′ | + p, |J| + |J ′ | + p)-
currents. Hence, RJJ ′ k might not be positive in general and it is not clear how to control



                                                     23
its mass as k → ∞. This is a subtle point which we need to pay attention to. The relative
non-pluripolar product

                           RJJ ′ := ∧j∈J (ddc uj + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ + θj ′ )∧T
                                                                                       ˙

exists by our assumption. Let

                                  Bk := ∩j∈J {uj > −k} ∩ ∩j ′ ∈J ′ {u′j ′ > −k}.

By Lemma 3.2, we get
                                            0 ≤ 1Bk RJJ ′ = 1Bk RJJ ′ k
for every J, J ′ , k. Put R̃JJ ′ := 1X\A RJJ ′ . The last current is closed (for example see [4,
Remark 1.10]) and positive because RJJ ′ ≥ 0. Using the fact that {ψk 6= 0} ⊂ Bk \A, we
get

                                         ψk R̃JJ ′ = ψk RJJ ′ = ψk RJJ ′ k .                                        (4.6)

Claim. Let j ′′ ∈ {1, . . . , m}\(J ∪J ′ ). Let Φ be ddc -closed smooth form of bi-degree (p′ , p′ )
on X, where p′ := n − |J| − |J ′ | − p − 1. Then
                                    Z
                                lim     ψk ddc wj ′′k ∧ RJJ ′ k ∧ Φ = 0.                   (4.7)
                                     k→∞       X
                                                                              Pm
We prove Claim. Let ω be a Hermitian metric on X. Let η :=                       j=1 2 θj . We have
  c       −1
dd ψk + k η ≥ 0 for every k. By integration by parts and (4.6),
  Z                                Z                              Z
          c                                   c
     ψk dd wj ′′ k ∧ RJJ ′ k ∧ Φ =   wj ′′k dd (ψk RJJ ′ k ∧ Φ) =   wj ′′k ddc (ψk R̃JJ ′ ∧ Φ). (4.8)
     X                                     X                                        X

Observe that

                      ddc (ψk R̃JJ ′ ∧ Φ) = ddc ψk ∧ Φ ∧ R̃JJ ′ + 2dψk ∧ dc Φ ∧ R̃JJ ′

because ddc Φ = 0 and Φ is of bi-degree (p′ , p′ ). Write dc Φ locally as a complex linear
combination of forms like τj ∧ Φj , where τj is a (0, 1)-form or a (1, 0)-form and Φj is a
positive form. Hence, we can use the Cauchy-Schwarz inequality to obtain
 Z                                       Z                                                  21  Z                      21
                       c
      wj ′′ k dψk ∧ d Φ ∧ R̃JJ ′ ≤                 |wj2′′k |dψk ∧ dc ψk ∧ R̃JJ ′ ∧ Φ0                  R̃JJ ′ ∧ Φ0 ∧ ω          ,
  X                                            X                                                   X

                              ′
where Φ0 := ω n−|J|−|J |−1 . We deduce that
             Z                                                       Z                                     21
                                                                 1
                                     c                                                  c
                     wj ′′k dψk ∧ d Φ ∧ R̃JJ ′ . kR̃JJ ′ k       2            dψk ∧ d ψk ∧ R̃JJ ′ ∧ Φ0
                 X                                                        X

by (4.5). Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set A. Using
this, Remark 2.7 and the fact that R̃JJ ′ has no mass on A, we get

                      lim dψk ∧ dc ψk ∧ R̃JJ ′ = lim (ddc ψk2 − ψk ddc ψk ) ∧ R̃JJ ′ = 0
                     k→∞                                 k→∞




                                                            24
(we recall that to get Remark 2.7 for R̃JJ ′ and ψk , we need to use the strong quasi-
continuity of ψk with respect to the capacity associated to R̃JJ ′ ). Thus we obtain
                                 Z
                            lim     wj ′′ k dψk ∧ dc Φ ∧ R̃JJ ′ = 0.                 (4.9)
                                k→∞   X

On the other hand, since
 Z                                  Z                               Z
               c                                 c
     wj ′′ k dd ψk ∧ Φ ∧ R̃JJ ′ = −   dwj ′′k ∧ d ψk ∧ Φ ∧ R̃JJ ′ +   wj ′′k dc ψk ∧ dΦ ∧ R̃JJ ′ ,
    X                                 X                                        X

using similar arguments, we get
                                      Z
                                lim           wj ′′k ddc ψk ∧ Φ ∧ R̃JJ ′ = 0
                              k →∞
                                ′
                                          X

Combining this with (4.9) and (4.8) yields (4.7). Claim follows.
                               ˙ i − hT1′ ∧ · · · Tn′ ∧T
   Now let S := hT1 ∧ · · · Tn ∧T                     ˙ i. Using Tjk = Tjk
                                                                         ′
                                                                           + ddc wjk , one can
check that
            Z               Z                             Z
                                    m
               ψk S ∧ Φ =       ψk ∧j=1 Tjk ∧ T ∧ Φ −        ψk ∧m    ′
                                                                 j=1 Tjk ∧ T ∧ Φ
                X                X                                 X
                                m Z
                                X
                                              s−1 ′
                            =             ψk ∧j=1 Tjk ∧ ddc wsk ∧ ∧m
                                                                   j=s+1 Tjk ∧ T ∧ Φ.
                                s=1   X


This together with Claim yields hS, Φi = limk→∞ hψk S, Φi = 0 for every ddc -closed smooth
Φ. This finishes the proof.
Remark 4.3. Our proof of Proposition 4.2 still works if Tj′ , Tj are not in the same cohomol-
ogy class. In this case, one just needs to modify (4.2) accordingly.
  The following result is the monotonicity property of relative non-pluripolar products
mentioned in Introduction.
Theorem 4.4. Let X be a compact Kähler manifold of dimension n. Let Tj , Tj′ be closed
positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are in the same cohomology
class for every j and Tj′ is less singular than Tj for 1 ≤ j ≤ m. Let T be a closed positive
current on X. Then, we have
                                           ˙ i ≤ hT1′ ∧ · · · ∧ Tm′ ∧T
                                                                    ˙ i .
                                                
                          hT1 ∧ · · · ∧ Tm ∧T                                        (4.10)

Proof. Write Tj = ddc uj + θj , Tj′ = ddc u′j + θj . Without loss of generality, we can assume
that u′j ≥ uj . For l ∈ N, put ulj := max{uj , u′j − l} which is of the same singularity type as
u′j . Notice that ddc ulj + θj ≥ 0. Since X is Kähler, the current h∧m        c l       ˙
                                                                        j=1 (dd uj + θj )∧T i is of
                                                                  m      c l       ˙ i as l → ∞.
mass uniformly bounded in l. Let S be a limit current of h∧j=1 (dd uj + θj )∧T
         l
Since uj decreases to uj as l → ∞, we can apply Lemma 4.1 to get

                                              S ≥ h∧m      ˙
                                                    j=1 Tj ∧T i.

Consequently, {S} ≥ {h∧m          ˙
                           j=1 Tj ∧T i}. Using Proposition 4.2, we see that {S} is equal to
   m    ′˙
{h∧j=1 Tj ∧T i}. The desired assertion, hence, follows. This finishes the proof.



                                                      25

```

## Vu-2005.13241v3-20261004.txt, LF121--655

SHA256 `ac897767ca0a5f2aaccf93220b4393ba919af1d21d12d7f2a378207e1955b157`; supplied pin matches: True.

```text

fined in a way similar to that of the usual non-pluripolar product. The
product h m        ˙
          V
            j=1 Tj ∧T i is a well-defined closed positive current of bi-degree
(m + p, m + p); and h m           ˙
                         V
                           j=1 Tj ∧T i is symmetric with respect to T1 , . . . , Tm
and is homogeneous.
    For every closed positive (1, 1)-current P , we denote by IP the set of
x ∈ X so that local potentials of P are equal to −∞ at x. Note that IP
is a locally complete pluripolar set. The following is deduced from [14,
Proposition 3.5].

Proposition 2.1. (i) Given a locally complete pluripolar set A such that T
has no mass on A, then h m         ˙
                          V
                            j=1 Tj ∧T i also has no mass on A.
   (ii) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above.
Assume that T has no mass on IT1 ∪ IT1′ . Then we have
                            m
                            ^                     m
                                                  ^                       m
                                                                          ^
(2.1)       (T1 + T1′ ) ∧            ˙
                                  Tj ∧T = hT1 ∧            ˙ i + hT1′ ∧
                                                        Tj ∧T                      ˙ i.
                                                                                Tj ∧T
                            j=2                   j=2                     j=2
4                                                                    Duc- Viet Vu

                                                             Vm
   (iii) Let 1 ≤ l ≤ m be an integer. Then for R := h                   ˙
                                                               j=l+1 Tj ∧T i, there
holds h m
                         Vl
                 ˙               ˙
       V
          j=1 Tj ∧T i = h j=1 Tj ∧Ri.
   (iv) The equality
                             m
                             ^            m
                                          ^
                            h Tj ∧T           ˙ ′i
                                   ˙ i = h Tj ∧T
                             j=1           j=1
               ′
holds, where T := 1X\   Sm          T.
                          j=1 ITj


    We also need the following result.
Theorem 2.2. ([14, Theorem 2.6, Remark 2.7]) Let uj be a locally bounded
plurisubharmonic (psh) function on an open subset U of Cn for 1 ≤ j ≤ m.
Let (ujk )k∈N be a sequence of locally bounded psh functions increasing to uj
almost everywhere as k → ∞. Let T be a closed positive current on U. Then,
the convergence

(2.2)      u1k ddc u2k ∧ · · · ∧ ddc umk ∧ T → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T

as k → ∞ holds provided that T has no mass on Aj := {x ∈ U : uj (x) 6=
limk→∞ ujk (x)} for every 1 ≤ j ≤ m and the set Aj is locally complete
pluripolar for every j.
    Recall that a dsh function on X is the difference of two quasiplurisub-
harmonic (quasi-psh for short) functions on X (see [9]). These functions
are well-defined outside pluripolar sets. Let v be a dsh function on X.
Write v = ϕ1 − ϕ2 , where ϕ1 , ϕ2 are quasi-psh function. Hence v(x) is
well-defined for x ∈ X\A, where A := {ϕ1 = −∞} ∪ {ϕ2 = −∞}. The
function v is said to be bounded in X if there exists a constant C such that
|v(x)| ≤ C for every x ∈ X\A.
    We say that v is T -admissible (or admissible with respect to T ) if there
exist quasi-psh functions ϕ1 , ϕ2 on X such that v = ϕ1 − ϕ2 and T has
no mass on {ϕj = −∞} for j = 1, 2. In particular, if T has no mass on
pluripolar sets, then every dsh function is T -admissible. Assume now that
v is T -admissible. The following is a direct consequence of Proposition 2.1
(i).
Lemma 2.3. If v is T -admissible, then v is also admissible with respect to
h m       ˙
 V
   j=1 Tj ∧T i.

   Recall that if v = ϕ1 − ϕ2 for some bounded quasi-psh functions ϕ1 , ϕ2
on X (note X is compact), the current dv ∧ dc v ∧ T is, by definition, equal
to
             1 c
(2.3)          dd (ϕ1 − ϕ2 )2 ∧ T − (ϕ1 − ϕ2 )ddc (ϕ1 − ϕ2 ) ∧ T.
             2
Convexity of the class of currents with finite energy                      5

We notice that in the above formula the function (ϕ1 − ϕ2 )2 is locally the
difference of two bounded psh functions. More precisely, we can assume
ϕj is ω-psh function for j = 1, 2, where ω is a Kähler form on X, and
consider an open local chart U such that ω = ddc φ for some smooth psh
function φ on U. By adding to φ a big constant, we can even assume that
ϕj + φ ≥ 0 on U for j = 1, 2. Thus (ϕj + φ)2 and (ϕ1 + ϕ2 + 2φ)2 are psh
on U for j = 1, 2, and

(2.4)      (ϕ1 − ϕ2 )2 = (2(ϕ1 + φ)2 + 2(ϕ2 + φ)2 ) − (ϕ1 + ϕ2 + 2φ)2

which is the difference of two bounded psh functions on U.
   Consider another dsh function w which is equal to the difference of
two locally bounded psh functions and T is of bi-degree (n − 1, n − 1), we
have
(2.5)
2dv ∧ dc w ∧ T = d(v + w) ∧ dc (v + w) ∧ T − dv ∧ dc v ∧ T − dw ∧ dc w ∧ T.

However, in general, even when v is bounded, v might not be the differ-
ence of two bounded quasi-psh functions. Hence, the current “dv∧dc v∧T ”
is not well-defined in the above sense. We will introduce below the cur-
                ˙ i in the spirit of non-pluripolar products. Before going
rent hdv ∧ dc v ∧T
into details, we need the following auxiliary estimate.

Lemma 2.4. Let ω be a Kähler form on X. Let ϕ1 , ϕ2 be bounded ω-psh
functions on X and v := ϕ1 − ϕ2 . Let T be a closed positive current of bi-
dimension (1, 1) on X. Then, there exists a constant C independent of ϕ1 , ϕ2
such that
                        Z
(2.6)                     dv ∧ dc v ∧ T ≤ CkvkL∞ .
                            X

Proof. We have
                   Z                             Z
                                 c
            I :=       dv ∧ d v ∧ T = −                  vddc v ∧ T
                   X
                   Z                                 X

              =−    v(ddc ϕ1 − ddc ϕ2 ) ∧ T
                 ZX                       Z
                        c
              =−    v(dd ϕ1 + ω) ∧ T +      v(ddc ϕ2 + ω) ∧ T
                       X                                  X
                           2 Z
                           X
              ≤ kvkL∞                    (ddc ϕj + ω) ∧ T
                           j=1       X
                           Z
              = 2kvkL∞               T ∧ω
                             X
6                                                                      Duc- Viet Vu

by Stokes’ theorem. The desired estimate follows. The proof is finished.


    Assume now that v is T -admissible. Let ϕ1 , ϕ2 be quasi-psh functions
such that v = ϕ1 − ϕ2 and T has no mass on {ϕj = −∞} for j = 1, 2. Let
ϕj,k := max{ϕj , −k} for every j = 1, 2 and k ∈ N. Put vk := ϕ1,k − ϕ2,k .
Since vk is the difference of two bounded quasi-psh functions, using (2.3),
we obtain

                Qk := dvk ∧ dc vk ∧ T = ddc vk2 ∧ T − vk ddc vk ∧ T.

Let ω be a Kähler form so that ϕj is ω-psh for j = 1, 2. Let U be a local
chart on X such that ω = ddc φ on U for some psh function φ such that
ϕj,k + φ ≥ 0 on U for j = 1, 2 (we fix k). By (2.4) applied to ϕj,k + φ, we
have

Qk = 2ddc (ϕ1,k + φ)2 ∧ T + 2ddc (ϕ2,k + φ)2 ∧ T − ddc (ϕ1,k + ϕ2,k + 2φ)2 ∧ T
        − (vk ddc ϕ1,k ∧ T − vk ddc ϕ2,k ∧ T )

on U. By the plurifine locality with respect to T ([14, Theorem 2.9]) ap-
plied to each term in the right-hand side of the last equality, we have

(2.7)                   1T2j=1 {ϕj >−k} Qk = 1T2j=1 {ϕj >−k} Qk′

for every k ′ ≥ k.
                          ˙ i is well-defined if the mass of 1T2 {ϕ >−k} Qk
   We say that hdv ∧ dc v ∧T                                   j=1  j

on X is bounded uniformly in k. In this case, using (2.7) implies that there
exists a positive current Q on X such that for every bounded Borel form
Φ on X, we have

                        hQ, Φi = lim h1T2j=1 {ϕj >−k} Qk , Φi.
                                   k→∞

                      ˙ i to be the current Q. This agrees with the classical
We define hdv ∧ dc v ∧T
definition if v is the difference of two bounded quasi-psh functions. This
definition is independent of the choice of ϕ1 , ϕ2 by Lemma 2.5 below. If w
is another T -admissible dsh function and T is of bi-dimension (1, 1) such
                             ˙ i, hdw ∧ dcw ∧T
that the currents hdv ∧ dc v ∧T             ˙ i, and hd(v + w) ∧ dc(v + w)∧T
                                                                          ˙ i
                                         c ˙
are all well-defined, we define hdv ∧ d w ∧T i using (2.5) formally.
Lemma 2.5. Let ϕ′1 , ϕ′2 be quasi-psh functions on X such that v = ϕ′1 − ϕ′2
and T has no mass on {ϕ′j = −∞} for j = 1, 2. Let ϕ′j,k , Q′k be the func-
tion and current associated to ϕ′j defined similarly as ϕj,k and Qk respec-
tively. Then if 1T2j=1 {ϕj >−k} Qk is of mass bounded uniformly on k then so is
Convexity of the class of currents with finite energy                                    7

1T2j=1 {ϕ′j >−k} Q′k , and

(2.8)                        Q = lim h1T2j=1 {ϕ′j >−k}Q′k , Φi
                                  k→∞

for every bounded Borel form Φ on X.

Proof. Since v = ϕ′1 − ϕ′2 , we get

                                  ϕ1 + ϕ′2 = ϕ′1 + ϕ2 .

Put vk′ := ϕ′1,k − ϕ′2,k , A′k := 2j=1 {ϕ′j > −k}, and Ak := 2j=1 {ϕj > −k}.
                                 T                            T

We have Q′k = dvk′ ∧ dc vk′ ∧ T , and vk = vk′ on Ak ∩ A′k which is open in the
plurifine topology. We claim that

(2.9)                           1Ak ∩A′k Q′k = 1Ak ∩A′k Qk .

This is a sort of plurifine locality statement and can be essentially de-
duced from the plurifine locality for bounded psh functions (here we have
vk = vk′ on Ak ∩ A′k but vk , vk′ are only dsh). We give details for readers’
convenience. Before doing so, we will show that the desired assertion is a
direct consequence of (2.9). First observe that 1A′k Q′k has no mass on the
pluripolar set {ϕj = −∞} for j = 1, 2 by Proposition 2.1 (i) and the fact
that T has no mass on {ϕj = −∞}. It follows that

                    1A′k Q′k = lim 1A′k ∩As Q′k
                                s→∞
                             = lim 1A′k ∩As Q′s
                                s→∞
                             ≤ lim 1A′s ∩As Q′s
                                s→∞
                             = lim 1A′s ∩As Qs ≤ lim 1As Qs = Q,
                                s→∞                 s→∞

where we used (2.7) applied to Q′k in the second equality and (2.9) in the
third equality. By exchanging the role of Q′k and Qk , we also obtain that

                                      1Ak Qk ≤ R,

for every limit current R of (1A′k Q′k )k as k → ∞. Hence (2.8) follows.
   We go back to the proof of (2.9). Write

dvk ∧ dc vk ∧ T = dvk ∧ dc (vk − vk′ ) ∧ T + d(vk − vk′ ) ∧ dc vk′ ∧ T + dvk′ ∧ dc vk′ ∧ T.

Denote by R1 , R2 the first and second currents in the right-hand side of
the last equality. In order to obtain (2.9), it suffices to check that Rj = 0
8                                                                    Duc- Viet Vu

on Ak ∩ A′k for j = 1, 2. Observe

     R1 = dvk ∧ dc (ϕ1,k + ϕ′2,k − ϕ′1,k − ϕ2,k ) ∧ T
        = dϕ1,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ1,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T −
                                                                         

          dϕ2,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ2,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T .
                                                                        


Each term in the right-hand side of the above equality is equal to 0 on
Ak ∩ A′k thanks to the plurifine locality and the fact that

               ϕ1,k + ϕ′2,k = ϕ1 + ϕ′2 = ϕ′1 + ϕ2 = ϕ′1,k + ϕ2,k

on Ak ∩ A′k . Hence R1 = 0 on Ak ∩ A′k . Similarly we get R2 = 0 on Ak ∩ A′k .
This finishes the proof.
                                                                  ˙ i is
Lemma 2.6. Assume that v is bounded. Then, the current hdv ∧ dc v ∧T
well-defined.

Proof. Let the notation be as in the proof of Lemma 2.4. Let ω be a Kähler
form on X such that ϕ1 , ϕ2 are ω-psh. Note that ϕjk is also ω-psh for every
j, k. Observe that since v is bounded, there exists a constant C such that
ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C. Thus, there exists a constant C so that

                                 kvk kL∞ ≤ C

for every k. Using this and Lemma 2.4, one gets

                             kQk k . kvk kL∞ ≤ C

for some constant C independent of k. Hence, the desired assertion fol-
lows. This finishes the proof.

      Let T1 , . . . , Tm be closed positive (1, 1)-currents on X and R := hT1 ∧
           ˙ i. We define
· · · ∧ Tm ∧T

               hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hdv ∧ dc v ∧Ri.
                                                              ˙

When T ≡ 1, we write the left-hand side of the last equality simply as
hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm i.
                                            ˙ i is defined similarly if p + m =
   The current hdv ∧ dc w ∧ T1 ∧ · · · ∧ Tm ∧T
n − 1, where T is of bi-degree (p, p). We put

                   hddc v ∧T
                          ˙ i := hddc ϕ1 ∧T
                                         ˙ i − hddcϕ2 ∧T
                                                      ˙ i.

Define
                   hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hddc v ∧Ri.
                                                          ˙
Convexity of the class of currents with finite energy                            9

   By Proposition 2.1 (iii), this definition agrees with the T -relative non-
pluripolar product of ddc v, T1 , . . . , Tm if v is quasi-psh. When T ≡ 1, we
                                                              ˙ i. In this case the
write hddc v ∧ T1 ∧ · · · ∧ Tm i for hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
product hddc v ∧ T1 ∧ · · · ∧ Tm i is the one defined in the paragraph right
after Theorem 1.2 in [12].
   By admissibility and Proposition 2.1 (ii), we can check that if v, w are
dsh functions which are admissible with respect to T , then

                    hddc (v + w)∧T
                                ˙ i = hddc v ∧T
                                             ˙ i + hddcw ∧T
                                                         ˙ i.

   Here is an integration by parts formula for relative non-pluripolar prod-
ucts.
Theorem 2.7. Let T be a closed positive current of bi-degree (n − 1, n − 1)
on X. Let v, w be bounded T -admissible dsh functions on X. Then, we have
              Z                Z                   Z
                     c ˙
(2.10)           whdd v ∧T i =   vhdd w ∧T i = − hdw ∧ dc v ∧T
                                       c ˙                     ˙ i.
                X                  X                      X

   The last result was proved in [4, Theorem 1.14] if v, w can be written
as the differences of psh functions which are locally bounded outside a
closed locally complete pluripolar set; see also [1, 13].

Proof. We use ideas from the proof of [14, Proposition 4.2]. Let ϕ1 , ϕ2 , ϕ3 , ϕ4
be negative quasi-psh functions on X such that v = ϕ1 −ϕ2 and w = ϕ3 −ϕ4
and T has no mass on 4j=1 {ϕj = −∞}. Let ω be a Kähler form on X such
                       S

that ϕj is ω-psh for every 1 ≤ j ≤ 4. Put

           ψ := ϕ1 + ϕ2 + ϕ3 + ϕ4 ,       ψk := k −1 max{ψ, −k} + 1.

and ϕjk := max{ϕj , −k} for 1 ≤ j ≤ 4. Observe that 0 ≤ ψk ≤ 1. Let x ∈ X
such that ψk (x) > 0. We have

                ϕ1 (x) + ϕ2 (x) + ϕ3 (x) + ϕ4 (x) = ψ(x) > −k.

This combined with the property that ϕj ≤ 0 for every 1 ≤ j ≤ 4 yields
that ϕj (x) > −k for every 1 ≤ j ≤ 4. We infer that
                                         4
                                         \
(2.11)                     {ψk 6= 0} ⊂       {ϕj > −k}.
                                         j=1


   Put vk := ϕ1k − ϕ2k and wk := ϕ3k − ϕ4k . Since v and w are bounded,
the functions vk , wk are bounded uniformly in k.
10                                                                      Duc- Viet Vu

              S4
   Let A :=    j=1 {ϕj = −∞}. By admissibility and Proposition 2.1 (i), we
see that

(2.12)                       1A h(ddcϕj + ω)∧T
                                            ˙ i = 0.

Using (2.12), we can consider w as a bounded function with respect to the
                              ˙ i. Using (2.11), we have
trace measure of h(ddc ϕj + ω)∧T

      wψk ddc ϕjk ∧ T = w1{ϕj >−k} ψk hddc ϕj ∧T
                                              ˙ i
                         = whddc ϕj ∧T
                                    ˙ i + w(1{ϕj >−k} ψk − 1)hddcϕj ∧T
                                                                    ˙ i.

The second term in the right-hand side of the last equality converges
weakly to 0 as k → ∞ by the fact that ψk → 1 pointwise outside A as
k → ∞ and Lebesgue’s dominated convergence theorem. Hence

                       whddcϕj ∧T
                               ˙ i = lim wψk ddc ϕjk ∧ T.
                                          k→∞

Applying the last equality to j = 1, 2, and using v = ϕ1 − ϕ2 , we obtain

(2.13)        whddcv ∧T
                     ˙ i = lim wψk ddc vk ∧ T = lim wk ψk ddc vk ∧ T.
                               k→∞                            k→∞

Here in the second equality we used the fact that w = wk on {ϕ3 > −k} ∩
{ϕ4 > −k} which contains {ψk 6= 0}. We also have an analogous formula
by exchanging the roles of v, w. Thus,

(2.14)    whddcv ∧T
                 ˙ i − vhddc w ∧T
                               ˙ i = lim ψk (wk ddc vk − vk ddc wk ) ∧ T.
                                                    k→∞

By integration by parts for bounded psh functions, we have
         Z                                     Z
                      c          c
(2.15)       ψk (wk dd vk − vk dd wk ) ∧ T = −    wk dψk ∧ dc vk ∧ T +
           X                                    X
                                                      Z
                                                         vk dψk ∧ dc wk ∧ T.
                                                                    X

Denote by I1 , I2 the first and second term in the right-hand side of the
last equality. We will check that Ij → 0 as k → ∞ for j = 1, 2. Using the
Cauchy-Schwarz inequality, the boundedness of vk , wk and Lemma 2.4, we
infer
               Z                   21  Z                        21
                            c                     2       c
       |I1 | ≤      dψk ∧ d ψk ∧ T     ×     |wk | dvk ∧ d vk ∧ T
                   X                                      X
               Z                         21
           .           dψk ∧ dc ψk ∧ T          .
                   X
Convexity of the class of currents with finite energy                       11

Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set {ψ =
−∞}. Using this, Theorem 2.2 and the fact that T has no mass on {ψ =
−∞}, we get

           lim dψk ∧ dc ψk ∧ T = lim (ddc ψk2 − ψk ddc ψk ) ∧ T = 0
           k→∞                     k→∞

Thus we obtain

(2.16)                            lim I1 = 0.
                                 k→∞

By similarity, we also get I2 → 0 as k → ∞. Combining this with (2.15)
and (2.13) gives the first desired equality of (2.10). We prove the second
one similarly as follows. Put u := v + w, and

               uk := max{ϕ1 + ϕ3 , −k} − max{ϕ2 + ϕ4 , −k}.

By (2.11) observe that

             1{ψk >0} max{ϕ1 + ϕ3 , −2k} = 1{ψk >0} (ϕ1k + ϕ3k )

and a similar equality for ϕ2 , ϕ4 also holds. Thus, by plurifine locality, we
get

2hdv ∧ dc w ∧T
            ˙ i = hdu ∧ dc u∧T
                            ˙ i − hdv ∧ dc v ∧T
                                             ˙ i − hdw ∧ dc w ∧T
                                                              ˙ i
                 = lim ψk hdu2k ∧ dc u2k ∧T
                                         ˙ i − hdvk ∧ dc vk ∧T
                                                            ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i
                                   

                 = lim ψk hd(vk + wk ) ∧ dc (vk + wk )∧T
                                                      ˙ i − hdvk ∧ dc vk ∧T
                                                                         ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i .
                                  


Consequently

                  hdv ∧ dc w ∧T
                             ˙ i = lim ψk hdvk ∧ dc wk ∧T
                                                       ˙ i.
                                    k→∞

It follows that
  Z                                      Z
          c ˙              c ˙
      vhdd w ∧T i + hdv ∧ d w ∧T i = lim    ψk (vk ddc wk + dvk ∧ dc wk ) ∧ T
    X                                k→∞ X
                                           Z
                                   = − lim    vk dψk ∧ dc wk ∧ T
                                         k→∞    X

which is equal to 0 by analogous arguments as in the proof of (2.16). This
finishes the proof.
12                                                                                          Duc- Viet Vu

Corollary 2.8. Let v, w be bounded dsh functions on X. Then, for every
closed smooth form Φ of right bi-degree, we have
            Z                  m
                               ^                  Z                      m
                                                                         ^
                        c                                    c
(2.17)              whdd v ∧         Tj i ∧ Φ =           vhdd w ∧             Tj i ∧ Φ =
                X              j=1                    X                  j=1
                                                                     Z                      m
                                                                                            ^
                                                                                    c
                                                                 −        hdv ∧ d w ∧             Tj i ∧ Φ.
                                                                     X                      j=1

Proof. By writing Φ as the difference of two closed positive forms, we can
assume that Φ is positive. The desired formula is a direct consequence of
Theorem 2.7 applied to T := hT1 ∧ · · · ∧ Tm i ∧ Φ.

    We recall that the first inequality of (2.17) was proved in [12, Theorem
1.2] and [16] when m = n and the cohomology classes of Tj ’s are big.
One should notice a crucial point that the integration by parts formulae
obtained in [12, 16] contain no term involving dv ∧ dc w. Such a term is
essential in applications, especially, in the pluricomplex energy theory. The
following result is more general than Theorem 2.7. We will need it later.
Theorem 2.9. Let T a closed positive current of bi-degree (n − 1, n − 1) on
X. Let v, w be bounded T -admissible dsh functions on X. Let χ : R → R be
a C 3 function. Then we have
(2.18)
   Z                   Z                        Z
                           ′′
             c ˙
      χ(w)hdd v ∧T i =                c ˙
                         vχ (w)hdw ∧ d w ∧T i +   vχ′ (w)hddcw ∧T
                                                               ˙ i.
        X                            X                                          X

   A quick heuristic reason explaining why (2.18) should hold is because
dd χ(w) = χ′′ (w)dw∧dc w+χ′ (w)ddcw if w is a bounded quasi-psh function.
    c


Proof. We first note that [14, Lemma 5.7] still holds for dsh functions
which are the differences of two bounded quasi-psh functions. Now, to
obtain the desired equality, we just follow the proof of Theorem 2.7 ver-
batim with χ(w) in place of w. The only thing we need to clarify is the
computation concerning ddc χ(wk ) ∧ T . To this end, it suffices to use [14,
Lemma 5.7] because wk is the difference of two bounded quasi-psh func-
tions. This finishes the proof.



```

## Vu-2005.13241v3-20261004.txt, LF656--827

SHA256 `7c4a6f848d72b6bc891d56b0cdf8b543bf9c1522324504029100073e1d6b9ba9`; supplied pin matches: True.

```text

3       Currents with finite relative energy
Let X be a compact Kähler manifold. Let α1 , . . . , αm be pseudoeffective
(1, 1)-classes of X and T a closed positive current on X. Let Pj be a closed
Convexity of the class of currents with finite energy                                 13

positive (1, 1)-current in the class αj for 1 ≤ j ≤ m. Put P := (P1 , . . . , Pm ).
We define EP (T ) to be the set of m-tuple (T1 , . . . , Tm ) of closed positive
(1, 1)-currents such that Tj ∈ αj and Tj is more singular than Pj and
                                m
                                ^                     m
                                                      ^
                           {h            ˙ i} = {h
                                      Tj ∧T                    ˙ i}.
                                                            Pj ∧T
                                j=1                   j=1

Notice that for every current Pj′ in αj such that Pj′ has the same singular-
ities as Pj for 1 ≤ j ≤ m, by the monotonicity of relative non-pluripolar
products (see (1.1)), we have

                                       EP (T ) = EP′ (T ).

Hence, when Pj has minimal singularities in αj for 1 ≤ j ≤ m, we recover
the class E(α1 , . . . , αm , T ) of currents of full mass intersection introduced
in [14, 4] because we have

                             EP (T ) = E(α1 , . . . , αm , T )

in this case.
    Let χ ∈ W − . Write Pj = ddc ϕj + θj , where θj is a smooth form and ϕj is
a negative θj -psh function. Let (T1 , . . . , Tm ) ∈ EP (T ). Let uj be a negative
θj -psh function so that Tj = ddc uj + θj and uj ≤ ϕj for 1 ≤ j ≤ m. For a
negative Borel function ξ, we put
                                           XZ       ^         ^
(3.1)       Eξ,P (T1 , . . . , Tm ; T ) :=     −ξ      Tj ∧         ˙ ,
                                                                 Pj ∧T
                                             J    X          j∈J       j6∈J

where the sum is taken over every subset J of {1, . . . , m}. The (T, P)-
relative joint χ-energy of T1 , . . . , Tm is, by definition, Eξ,P (T1 , . . . , Tm ; T ),
where
                                                             
                    ξ := χ (u1 − ϕ1 ) + · · · + (um − ϕm ) .
The last energy depends on the choice of uj , ϕj but its finiteness does not.
That notion generalizes those in [4, 11, 14], see also [5] for the local
setting.
    For every closed positive (1, 1)-current P , let IP be the set of x ∈ X so
that the potentials of P are equal to −∞ at x. Note that IP is a complete
pluripolar set. By Proposition 2.1 (iv), the right-hand side of (3.1) remains
unchanged if we replace T by 1X\ Sm         j=1 IPj
                                                    T . Hence, in practice, we can
                             Sm
assume T has no mass on j=1 IPj . We denote by Eχ,P (T ) the subset of
EP (T ) containing every (T1 , . . . , Tm ) such that their (T, P)-relative joint
χ-energy is finite.
14                                                                                   Duc- Viet Vu

   Here is a monotonicity for the class Eχ,P (T ) when Pj = P for every
1 ≤ j ≤ m. This generalizes [14, Theorem 5.8].
Theorem 3.1. Let P = ddc ϕ + θ be a closed positive (1, 1)-current and P :=
(P, . . . , P ) (m times P ). Let χ ∈ W − with |χ(0)| ≤ 1. Let (T1 , . . . , Tm ) ∈
Eχ,P (T ) and (T1′ , . . . , Tm′ ) ∈ EP (T ) such that Tj = ddc uj + θ, Tj′ = ddc u′j + θ
such that uj , u′j are θ-psh and uj ≤ u′j ≤ ϕ. Put
                                                                
                           ξ := χ (u1 − ϕ) + · · · + (um − ϕ) .

Then we have

                 Eξ (T1′ , . . . , Tm′ ; T ) ≤ c1 Eξ (T1 , . . . , Tm ; T ) + c2 ,

for some constants c1 , c2 > 0 independent of χ. In particular, (T1′ , . . . , Tm′ ) ∈
Eχ,P (T ).

Proof. As mentioned above, we can assume that T has no mass on IP =
{ϕ = −∞}. Note here that {ϕ = −∞} ⊂ {uj = −∞}. Put

                               ujk := max{uj , ϕ − k} − ϕ

which is a bounded dsh function and

                                    Tjk := ddc ujk + P.

Observe that ujk ’s are admissible with respect to T . Define u′jk , Tjk
                                                                      ′
                                                                         simi-
larly. Put
                    m
                    X
             v :=         (uj − ϕj ),    vk := max{v, −k},             ξk = χ(vk ).
                    j=1

Note that ξ = χ(v). With these notations and a suitable integration by
parts ready in our hands (Theorem 2.9) replacing [14, Lemma 5.7]), the
proof goes exactly as in the proof of [14, Theorem 5.8]. The only minor
modifications are: the Kähler form ω is substituted by P and the wedge
products appearing in the proof of [14, Theorem 5.8] need to be replaced
by T -relative non-pluripolar products. This finishes the proof.

     The following is a direct consequence of Theorem 3.1.
Corollary 3.2. Let P, P be as in Theorem 3.1. Let P ′ be a current in {P }
which is of the same singularity type as P . Then, for P′ = (P ′ , . . . , P ′) (m
times P ′), we have
                            Eχ,P′ (T ) = Eχ,P(T ).
Convexity of the class of currents with finite energy                            15

   For every closed positive (1, 1)-current P , we define the class Em,P (T )
(resp. Eχ,m,P (T )) to be the set of currents T1 ∈ {P } such that (T1 , . . . , T1 )
belongs to EP (T ) (resp. Eχ,P (T )), where P = (P, . . . , P ) (m times P ). The
last space was introduced in [6] when T is the constant function equal
to 1. As in the case of the usual class of currents of full mass intersection
([11, Proposition 2.2]), notice that
                                          [
                           Em,P (T ) =           Eχ,m,P (T ).
                                         χ∈W −


Let α be a pseudoeffective (1, 1)-class. By Corollary 3.2, we see that the
notion of the weighted class Eχ,m,P (T ) makes sense if we replace P by its
equivalent class (in terms of singularity type) of (1, 1)-currents. Hence,
we can define Em (α, T ) (resp. Eχ,m(α, T )) to be the set Em,P (T ) (resp.
Eχ,m,P (T )), where P is a current with minimal singularities in α.
Theorem 3.3. Let U be an open subset in Cn . Let T be a closed positive
current on U and uj , u′j bounded psh functions on U for 1 ≤ j ≤ m, where
m ∈ N. Let vj , vj′ be psh functions on U for 1 ≤ j ≤ q. Assume that uj = u′j
on W := qj=1 {vj > vj′ } for 1 ≤ j ≤ m. Then we have
         T


(3.2)       1W ddc u1 ∧ · · · ∧ ddc um ∧ T = 1W ddc u′1 ∧ · · · ∧ ddc u′m ∧ T.

Proof. If vj , vj′ are all bounded, then the desired assertion is Theorem 2.9
in [14]. In general, observe that
                                          ∞
                                          [
                          {vj > vj′ } =               ′
                                              {vjk > vjk },
                                          k=1

                                             ′
                                                . Let Wk := qj=1 {vjk > vjk
                                                                         ′
                                                           T
where vjk := max{vj , −k} and similarly for vjk                             }.
                    S∞             ′
We have W = k=1 Wk and uj = uj on Wk . Applying [14, Theorem 2.9]
to uj , u′j , Wk gives

         1Wk ddc u1 ∧ · · · ∧ ddc um ∧ T = 1Wk ddc u′1 ∧ · · · ∧ ddc u′m ∧ T

for every k. Hence, the desired assertion follows. This finishes the proof.


   Now, using Theorems 3.1 and 3.3 instead of [14, Theorem 5.8] and
[14, Theorem 2.9] respectively, and following arguments in the proof of
[14, Theorems 5.9 and 5.1], we immediately obtain the following result.

Theorem 3.4. For χ ∈ W − , the sets Eχ,m,P (T ) and Em,P (T ) are convex.
16                                                              Duc- Viet Vu

     Finally, we would like to make the following comment.
                    +
Remark 3.5. Let WM     be the class of weights introduced in [11, Page 462].
Using arguments from the proof of [11, Lemma 3.5] and that of Theorem
                                                        +
3.4, we can prove the convexity of Eχ,m,P (T ) for χ ∈ WM .


Acknowledgements
The author would like to thank referees for their remarks improving the
presentation of the paper.



```

## Vu-2005.13241v3-20261004.txt, LF828--884

SHA256 `d0915796895621146bb871da1cea5244607f9d37b9146f2d202a099a9eb96e7f`; supplied pin matches: True.

```text

References
 [1] E. B EDFORD AND B. A. TAYLOR, A new capacity for plurisubharmonic
     functions, Acta Math., 149 (1982), pp. 1–40.

 [2]       , Fine topology, Šilov boundary, and (ddc )n , J. Funct. Anal., 72
       (1987), pp. 225–251.

 [3] R. J. B ERMAN , S. B OUCKSOM , V. G UEDJ , AND A. Z ERIAHI , A vari-
     ational approach to complex Monge-Ampère equations, Publ. Math.
     Inst. Hautes Études Sci., 117 (2013), pp. 179–245.

 [4] S. B OUCKSOM , P. E YSSIDIEUX , V. G UEDJ , AND A. Z ERIAHI , Monge-
     Ampère equations in big cohomology classes, Acta Math., 205 (2010),
     pp. 199–262.

 [5] U. C EGRELL, Pluricomplex energy, Acta Math., 180 (1998), pp. 187–
     217.

 [6] T. DARVAS , E. D I N EZZA , AND C. H. LU, Monotonicity of nonpluripo-
     lar products and complex Monge-Ampère equations with prescribed sin-
     gularity, Anal. PDE, 11 (2018), pp. 2049–2087.

 [7]        , On the singularity type of full mass currents in big cohomology
       classes, Compos. Math., 154 (2018), pp. 380–409.

 [8] T. DARVAS , E. D I N EZZA , AND C. H. LU, Log-concavity of volume and
     complex Monge-Ampère equations with prescribed singularity, Math.
     Ann., 379 (2021), pp. 95–132.
Convexity of the class of currents with finite energy                 17

 [9] T.-C. D INH AND N. S IBONY, Distribution des valeurs de transforma-
     tions méromorphes et applications, Comment. Math. Helv., 81 (2006),
     pp. 221–258.

[10] D. T. D O AND D.-V. V U, Complex Monge-Ampère equations with solu-
     tions in finite energy classes. arXiv:2010.08619, 2020. to appear in
     Math. Res. Lett.

[11] V. G UEDJ AND A. Z ERIAHI, The weighted Monge-Ampère energy
     of quasiplurisubharmonic functions, J. Funct. Anal., 250 (2007),
     pp. 442–482.

[12] C. H. LU, Comparison of Monge-Ampère capacities, Ann. Polon. Math.,
     126 (2021), pp. 31–53.

[13] N. S IBONY, Quelques problèmes de prolongement de courants en anal-
     yse complexe, Duke Math. J., 52 (1985), pp. 157–197.

[14] D.-V. V U, Relative non-pluripolar product of currents, Ann. Global
     Anal. Geom., 60 (2021), pp. 269–311.

[15] D. W ITT N YSTRÖM, Monotonicity of non-pluripolar Monge-Ampère
     masses, Indiana Univ. Math. J., 68 (2019), pp. 579–591.

[16] M. X IA, Integration by parts formula for non-pluripolar products.
     arXiv:1907.06359, 2019.


```

## Additional foundation: BEGZ-0812.3674v2-20261004.txt, LF323--477

SHA256 `462891277734fc5ab0efef31d1a327cb2de16257bfdc3ec5f24424db0e67909f`.

```text

  A crucial point for what follows is that non-pluripolar products of globally
deﬁned currents are always well-deﬁned on compact Kähler manifolds:
Proposition 1.6. Let T1 , ..., Tp be closed positive (1, 1)-currents on a compact
Kähler manifold X. Then their non-pluripolar product hT1 ∧ ... ∧ Tp i is well-
defined.
Proof. Let ω be a Kähler form on X. In view of the third point of Proposi-
tion 1.4, upon adding a large multiple of ω to the Tj ’s we may assume that their
cohomology classes are Kähler classes. We can thus ﬁnd Kähler forms ωj and
ωj -psh functions ϕj such that Tj = ωj + ddc ϕj . Let U be a small open subset of
8                S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

X on which ωj = ddc ψj , where ψj ≤ 0 is a smooth psh function on U , so that
Tj = ddc uj on U with uj := ψj + ϕj . The bounded psh functions on U
                                           ψj + max(ϕj , −k)
and
                                 max(uj , −k)
coincide on the pluriﬁne open subset {uj > −k} ⊂ {ϕj > −k}, thus we have
                     Z                  ^
                                  n−p
                       T        ω     ∧   ddc max(uj , −k)
                               j {uj >−k}                       j
                     Z                                  ^
                 =       T                ω n−p ∧        (ωj + ddc max(ϕj , −k))
                             j {uj >−k}                     j
                              Z                 ^
                         ≤            ω n−p ∧       (ωj + ddc max(ϕj , −k)).
                                  X             j
But the latter integral is computed in cohomology, hence independent of k, and
this shows that (1.2) is satisﬁed on U , qed.                                
Remark 1.7. The same property extends to the case where X is a compact com-
plex manifold in the Fujiki class, that is bimeromorphic to a compact Kähler
manifold. Indeed there exists in that case a modiﬁcation µ : X ′ → X with
X ′ compact Kähler. Since µ is an isomorphism outside closed analytic (hence
pluripolar) subsets, it is easy to deduce that hT1 ∧ ... ∧ Tp i is well-deﬁned on X
from the fact that hµ∗ T1 ∧ ... ∧ µ∗ Tp i is well-deﬁned on X ′ , and in fact
                         hT1 ∧ ... ∧ Tp i = µ∗ hµ∗ T1 ∧ ... ∧ µ∗ Tp i.
On the other hand it seems to be unknown whether ﬁniteness of non-pluripolar
products holds on arbitrary compact complex manifolds.
  Building on the proof of the Skoda-El Mir extension theorem, we will now
prove the less trivial closedness property of non-pluripolar products.
Theorem 1.8. Let T1 , ..., Tp be closed positive (1, 1)-currents on a complex man-
ifold X whose non-pluripolar product is well-defined. Then the positive (p, p)-
current hT1 ∧ ... ∧ Tp i is closed.
Proof. The result is of course local, and we can assume that X is a small neigh-
borhood of 0 ∈ Cn . The proof will follow rather closely Sibony’s exposition of
the Skoda-El Mir theorem [39], cf. also [18, pp. 159-161].
   Let uj ≤ 0 be a local potential of Tj near 0 ∈ Cn , and for each k consider the
closed positive current of bidimension (1, 1)
                                      ^
                           Θk := ρ ∧    ddc max(uj , −k)
                                                    j

and the pluriﬁne open subset
                                                    \
                                          Ok :=      {uj > −k}
                                                        j
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                          9

so that 1Ok Θk converges towards
                                  ρ ∧ hT1 ∧ ... ∧ Tp i
by (1.1). Here ρ is a positive (n − p − 1, n − p − 1)-form with constant coeﬃcients,
so that Θk has bidimension (1, 1). It is enough to show that
                                  lim d (1Ok Θk ) = 0
                                 k→∞
for any choice ofP
                 such a form ρ.
   Let also u := j uj , so that u ≤ −k outside Ok , and set

                                    wk := χ(eu/k ),
where χ(t) is a smooth convex and non-decreasing function of t ∈ R such that
χ(t) = 0 for t ≤ 1/2 and χ(1) = 1. We thus see that 0 ≤ wk ≤ 1 is a non-
decreasing sequence of bounded psh functions deﬁned near 0 ∈ Cn with wk = 0
outside Ok and wk → 1 pointwise outside the pluripolar set {u = −∞}. Finally
let 0 ≤ θ(t) ≤ 1 be a smooth non-decreasing function of t ∈ R such that θ(t) = 0
for t ≤ 1/2 and θ ≡ 1 near t = 1. The functions θ(wk ) are bounded, non-
decreasing in k and we have
                                 θ(wk ) ≤ 1Ok
since θ(wk ) ≤ 1 vanishes outside Ok . Note also that θ ′ (wk ) vanishes outside Ok ,
and converges to 0 pointwise outside {u = −∞}.
   Our goal is to show that
                                 lim d (1Ok Θk ) = 0.
                                 k→∞
But we have
                0 ≤ (1Ok − θ(wk )) Θk ≤ (1 − θ(wk )) hT1 ∧ ... ∧ Tp i,
and the latter converges to 0 by dominated convergence since θ(wk ) → 1 pointwise
outside the polar set of u, which is negligible for hT1 ∧...∧Tp i. It is thus equivalent
to show that
                                lim d (θ(wk )Θk ) = 0.
                                k→∞
Since wk is a bounded psh function, Lemma 1.9 below shows that the chain rule
applies, that is
                       d (θ(wk )Θk ) = θ ′ (wk )dwk ∧ Θk .
Recall that dwk ∧ Θk has order 0 by Bedford-Taylor, so that the right-hand side
makes sense. Now let ψ be a given smooth 1-form compactly supported near 0
and let τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the support of ψ. The
Cauchy-Schwarz inequality implies
  Z                     2   Z                      Z                    
      ′                                   c               ′     2
     θ (wk )ψ ∧ dwk ∧ Θk ≤       τ dwk ∧ d wk ∧ Θk       θ (wk ) ψ ∧ ψ ∧ Θk .

But on the one hand we have
                    Z                  Z
                  2 τ dwk ∧ d wk ∧ Θk ≤ τ ddc wk2 ∧ Θk
                             c
10                  S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI
                               Z                      Z
                           =       wk2 ddc τ ∧ Θk =        wk2 ddc τ ∧ Θk
                                                      Ok
since wk vanishes outside Ok , and the last integral is uniformly bounded since
0 ≤ wk ≤ 1 and 1Ok Θk has uniformly bounded mass by (1.2). On the other hand
we have
                   θ ′ (wk )2 Θk = θ ′ (wk )2 1Ok Θk ≤ θ ′ (wk )2 hT1 ∧ ... ∧ Tp i
since θ ′ (wk ) also vanishes outside Ok , and we conclude that
                                       Z
                                 lim      θ ′ (wk )2 ψ ∧ ψ ∧ Θk = 0
                                   k→∞

by dominated convergence since θ ′ (wk ) → 0 pointwise ouside the polar set of u,
which is negligible for hT1 ∧ ... ∧ Tp i. The proof is thus complete.          
Lemma 1.9. Let Θ be a closed positive (p, p)-current on a complex manifold X,
f be a smooth function on R and v be a bounded psh function. Then we have
                                     d(f (v)Θ) = f ′ (v)dv ∧ Θ.
Proof. This is a local result, and we can thus assume that Θ has bidimension (1, 1)
by multiplying it by constant forms as above. The result is of course true when
v is smooth. As we shall see the result holds true in our case basically because v
belongs to the Sobolev space L21 (Θ), in the sense that dv ∧ dc v ∧ Θ is well-deﬁned.
Indeed the result is standard when Θ = [X], and proceeds by approximation.
Here we let vk be a decreasing sequence of smooth psh functions converging
pointwise to v. We then have f (vk )θ → f (v)Θ by dominated convergence, thus
it suﬃces to show that
                               lim f ′ (vk )dvk ∧ Θ = f ′ (v)dv ∧ Θ.
                               k→∞
We write
                                                       
 f ′ (vk )dvk ∧ Θ − f ′ (v)dv ∧ Θ = f ′ (vk ) − f ′ (v) dvk ∧ Θ + f ′ (v)(dvk − dv) ∧ Θ.
Let ψ be a test 1-form and τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the
support of ψ. Cauchy-Schwarz implies
                        Z                                   2
                                               
                            f ′ (vk ) − f ′ (v) ψ ∧ dvk ∧ Θ
               Z                                          Z                  
                       ′
                                    2
                                     ′                                      c
           ≤         f (vk ) − f (v) ψ ∧ ψ ∧ Θ                   τ dvk ∧ d vk ∧ Θ .
The second factor is bounded since dvk ∧ dc vk ∧ Θ converges to dv ∧ dc v ∧ Θ by
Bedford-Taylor’s monotone convergence theorem, and the ﬁrst one converges to
0 by dominated convergence. We similarly have
                          Z                            2
                            f ′ (v)(dvk − dv) ∧ ψ ∧ Θ
            Z                     Z                              
                  ′   2                                c
         ≤       f (v) ψ ∧ ψ ∧ Θ        τ d(vk − v) ∧ d (vk − v) ∧ Θ ,
where now the ﬁrst factor is bounded while the second one tends to 0 by Bedford-
Taylor once again, and the proof is complete.                                 

```

## Additional foundation: DDNL18-2049-2087-20261004.txt, LF350--369

SHA256 `0d34fd95c9beb603186a5ec408cb5b463d1bdda346042cdc66ac38b25fde6c71`.

```text

2017, Theorem 4.26] for a proof of this result, which is merely a slight generalization of [Xing 1996,
Theorem 1].

Proposition 2.2. Let  ⊂ Cn be an open set. Suppose { f j } j are uniformly bounded quasicontinuous func-
                                                                                     j         j                  j
tions which converge in capacity to another quasicontinuous function f on . Let {u 1 } j , {u 2 } j , . . . , {u n } j
be uniformly bounded plurisubharmonic functions on , converging in capacity to u 1 , u 2 , . . . , u n respec-
tively. Then we have the following weak convergence of measures:
                                j            j
                         f j i∂ ∂u
                                ¯ ∧ i∂ ∂u
                                   1
                                       ¯ ∧ · · · ∧ i∂ ∂u
                                          2
                                                      ¯ nj → f i∂ ∂u
                                                                  ¯ 1 ∧ i∂ ∂u
                                                                           ¯ 2 ∧ · · · ∧ i∂ ∂u
                                                                                            ¯ n.

   The following lower-semicontinuity property of nonpluripolar products will be key in the sequel:

```

## Additional foundation: Vu-2005.13241v3-20261004.txt, LF64--87

SHA256 `f2355af21c2c2cdd4f567398969baf6b565884c1ea2aa8229c4349aa085a5510`.

```text

where Tj,min is a current with minimal singularities in the class {Tj } for
1 ≤ j ≤ m.
   Let α be a pseudoeffective (1, 1)-class. Denote by Em (α, T ) the set of
currents P ∈ α such that P, . . . , P (m times P ) are of T -relative full mass
intersection.
   Recall that W − is the set of convex increasing functions χ from R to
R such that χ(−∞) = −∞. Let χ ∈ W − . We can define Eχ,m(α, T ) to be
the subclass of Em (α, T ) consisting of P such that P has finite (T -relative)
χ-energy. When T ≡ 1 and m = n, the class Eχ,m (α, T ) generalizes the
usual class of currents with finite energy in [4, 11], see also [5] for the
local setting. We refer to Section 3 for details. For the moment, we note
here that                              [
                         Em (α, T ) =      Eχ,m (α, T ).
                                      χ∈W −

Here is our main result.

Theorem 1.1. The sets Eχ,m (α, T ) and Em (α, T ) are convex.

   The last result was proved in [14, Theorem 1.3] in the case where α is
Kähler. When m = n and T ≡ 1, the convexity Eχ,m (α, T ) was conjectured
in [4]. It was later answered affirmatively in [7, Corollary 2.12] in this
setting. The proof in [7] doesn’t extend directly to our setting because it
uses, in a crucial way, Monge-Ampère equations in big classes.

```
