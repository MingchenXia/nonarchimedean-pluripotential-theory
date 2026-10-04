## Primary application evidence (exact LF extraction)
These are immutable source passages. Formfeeds are retained in the authoritative Markdown; they are not line boundaries. Extraction errors are not silently corrected. GR 4.2(6), although present in the selected full unit, is not used for a finite-map converse in this integration.

### GR3.5(7)

GR.txt, LF 827--885; SHA-256 `c2133ed53c731ad28c6d3049f47e3f3af27023f374e57fe0c06dac3570866455`.

```text
Proof of Proposition 3.5(7). It is immediate from the definition that subharmonicity of
u implies subharmonicity of u ◦ πk′ /k . Suppose then that u ◦ πk′ /k is subharmonic. Let
k′′ /k be another analytic extension field with k′′ non-trivially valued, and let f : Y →
X k′′ be a morphism from a smooth, connected, strictly k′′ -analytic curve. Assume that
u ◦ πk′′ /k ◦ f ̸≡ −∞, so we need to show that u ◦ πk′′ /k ◦ f is subharmonic in Thuillier’s
sense. Let K be a non-Archimedean field that is simultaneously an analytic extension of
k′ and k′′ 2.2, and consider the following commutative diagram:

                               ←   fK            πK/k′
                                                 ←
                          YK            → XK          → X k′
                          ←



                                           ←



                                                            ←




(3.10.1)                                     πK/k′′             πk′ /k
                          →



                                          →



                                                            →




                               ←                 ←                ←
                           Y       f
                                       → X k′′         →
                                                  πk′′ /k   X            u → R ∪ {−∞}.
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 17

Since u ◦ πk′ /k is subharmonic, the composition u ◦ πK/k ◦ f K is, on each connected compo-
nent C of YK , either subharmonic in Thuillier’s sense or identically −∞; since C surjects
onto Y [Duc18, 1.5.6] and u ◦ πk′′ /k ◦ f ̸≡ −∞, the latter does not happen. Replacing
X by Y and k′ /k by K/k′′ , we are reduced to showing that if X is smooth and strictly
k-analytic for k non-trivially valued and u ◦ πk′ /k is subharmonic in Thuillier’s sense, then
so is u.
   We can do this directly using Thuillier’s definition. (The converse is the difficult di-
rection: see [Thu05, Corollaire 3.4.5].) Let U ⊂ X be a strictly k-affinoid domain and
let h: U → R be a harmonic function such that u ≤ h on ∂ U. Then h ◦ πk′ /k : Uk′ =
π−1
  k′ /k
        (U) → R is harmonic by [Thu05, Proposition 2.3.18]. We have πk′ /k (∂ Uk′ ) = ∂ U by
Lemma 2.12, so u ◦ πk′ /k ≤ h ◦ πk′ /k on ∂ Uk′ . Since u ◦ πk′ /k is subharmonic in Thuillier’s
sense, this implies u ◦ πk′ /k ≤ h ◦ πk′ /k on Uk′ , so u ≤ h on U since πk′ /k : Uk′ ↠ U is
surjective. Thus u is subharmonic in Thuillier’s sense, as claimed.                          □
```

### GR3.14--3.15

GR.txt, LF 1062--1103; SHA-256 `6faf0cbe62ec3b5cfb3d2817b457a27ad9922b80938b455d944eace90e79f793`.

```text
Proposition 3.14. Let X be a k-analytic curve and let h: X → R be a continuous function.
     (1) (Sheafiness) The harmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is harmonic.
     (3) The harmonic functions on X form a real vector space.
     (4) (Limits) If h is locally a uniform limit of harmonic functions, then it is harmonic.
     (5) (Maximum Principle) If h is harmonic and h attains a local extremum at x ∈ Int(X ),
         then h is constant in a neighborhood of x.
     (6) (Extension of Scalars) Let k′ /k be an analytic extension field. Then h is harmonic
         if and only if h ◦ πk′ /k : X k′ → R is harmonic.
     (7) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If h is
         harmonic then h ◦ f is harmonic, and the converse holds if f is finite and surjective.
     (8) (Boundaries) If h is harmonic on Int(X ), then it is harmonic on X .
   We will later see in Theorem 7.6 that (4) holds even for pointwise limits. The fol-
lowing proposition asserts that Definition 3.13 is equivalent to the notion of harmonicity
in [GJR21, Definition 7.2]. We assume that k is non-trivially valued as in ibid.
Proposition 3.15. Let X be a strictly k-analytic curve and let h: X → R be a continuous
function. The function h is harmonic if and only if it is R-PL and the line bundle Lh (x) ∈
Pic(red(X , x))R defined in (2.17) is numerically trivial for every point x ∈ X .
Proof. This is [GJR21, Proposition 15.7] in the rig-smooth case; we reduce to this case
                                                                         −∞
in the usual way. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let
k′ = k. Let X ′ = X ⊗b k k′ and let π: X ′ → X be the structure morphism. Let ι : X red
                                                                                      ′
                                                                                        ,→ X ′
be the underlying reduced space and let ν: Xe ′ → X red  ′
                                                            be the normalization, so that Xe ′ is
rig-smooth. Let f : Xe ′ → X denote the composition π ◦ ι ◦ ν.
   Suppose that h is harmonic. Then h ◦ f is harmonic by Proposition 3.14(6,7), so h ◦ f
is R-PL and Lh (x ′ ) is numerically trivial for all x ′ ∈ Xe ′ by the rig-smooth case. Then
h is R-PL by Lemma 3.9(6) and [GJR21, Lemma 5.3(3), Corollary 5.11], and Lh (x) is
numerically trivial for all x ∈ X by [GJR21, Proposition 7.6(1′ , 2′ )]. Conversely, suppose
that h is R-PL and that Lh (x) is numerically trivial for all x ∈ X . The same holds for
h ◦ f by [GJR21, Proposition 7.6(1′ , 2′ )], so h ◦ f is harmonic by the rig-smooth case, and
hence h is harmonic by Proposition 3.14(6,7).                                                  □
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES               21

Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X → R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′ /k is harmonic for some analytic extension field k′ /k, then
h◦πk′′ /k is R-PL for any analytic extension k′′ /k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y → X is finite and surjective and h◦ f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X ) is harmonic then h is R-PL.
```

### GR4.1--4.2

GR.txt, LF 1105--1177; SHA-256 `3aaee5628a226898b74714bb8b2e15108bf61d7d0e8d3b96afeea80f7377446f`.

```text
                     4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
  In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,
every k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →
R ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic
curve: this follows from Definition 3.4.
  Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
   (1) (Sheafiness) The classically psh functions form a sheaf on X .
   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.
   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.
   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically
       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →
       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically
       psh.
   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse
       holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce
22                                  W. GUBLER AND J. RABINOFF

that log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-
verse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a
classically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and
let f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show
that u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′ . It follows from the above that
u ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is
subharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).
    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,
then u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-
sically psh function for a finite surjective morphism f : Y → X . Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is
subharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a
connected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′
from f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-
clude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The
k′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve
W ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that
f ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a
connected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-
position W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic
curve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The
morphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □
```

### GR field conventions

GR.txt, LF 175--186; SHA-256 `457bc55b838876a08f6d41dd3948ec1f525fc28d939a64e92d4d6145228940c2`.

```text
2.1. General notation and conventions. In this paper, k will always denote a non-
Archimedean field, that is, a field k equipped with a non-Archimedean complete absolute
value | |: k → R, which may be trivial.
  The set of natural numbers N includes 0. We allow equality in a set-theoretic inclusion
S ⊂ T . For an abelian group P, let PΛ := P ⊗Z Λ. For a ring A, let A× be the group of
invertible elements.
  A topological space is called compact if it is quasi-compact and Hausdorff.
 2.2. Ground field and extensions. The valuation ring of k is denoted k◦ := {α ∈ k |
 |α| ≤ 1}, its unique maximal ideal is k◦◦ := {α ∈ k | |α| < 1}, and its residue field is
ek := k◦ /k◦◦ . An analytic extension field is a non-Archimedean field k′ endowed with an
 isometric embedding k ,→ k′ . For analytic field extensions k′ and k′′ of k, there is a joint
 analytic field extension F of k′ and of k′′ : see 2.8.
```

### GR actual joint analytic fields and scalar spaces

GR.txt, LF 254--273; SHA-256 `3db8bc8468fea029166b4e2598d763c0badaeeb707cfd5aedf634493193256ee`.

```text
2.8. Fiber products. The category of k-analytic spaces admits fiber products by [Ber93,
§1.4]. For analytic spaces X , Y over a k-analytic space S, we denote the fiber product by
X ×S Y . Given x ∈ X and y ∈ Y over the same point s ∈ S, there always exists z ∈ X ×S Y
mapping to x and to y with respect to the canonical projections [Duc18, 1.2.13]. For
convenience, we repeat the argument. The completed tensor product H (x)⊗         b H (s) H ( y)
contains H (x) ⊗H (s) H ( y) by a result of Gruson [Gru66, §3.2 Théorème 1(4)], so
H (x)⊗b H (s) H ( y) ̸= 0. The Berkovich spectrum of any nonzero Banach ring is nonempty
                                                                 
[Ber90, Theorem 1.2.1], and any z ′ ∈ M H (x)⊗     b H (s) H ( y) induces a point z ∈ X ×S Y
mapping to x and y. Note that H (z) is a simultaneous analytic extension field of H (x)
and of H ( y).
  Since Gruson’s result holds for Banach algebras over a non-Archimedean field, the
same argument shows that for two analytic field extensions of k, there is a joint analytic
extension of both.

2.9. Extension of scalars. Let k′ /k be an an analytic extension field. Then there is a
base extension functor (·)k′ which associates to a k-analytic space X a k′ -analytic space
X k′ , given on a k-affinoid space X = M (A ) by the k′ -affinoid space X k′ = M (A ⊗b k k′ )
[Ber90, §1.4]. We denote by πk′ /k : X k′ → X the structure map, which is closed and
surjective by [GRW17, Lemma 2.19], [Duc24, (3.1.1.2)].
```

### GR relative boundaries and full Lemma 2.12

GR.txt, LF 302--390; SHA-256 `2e820525db8b3713d077bb2e01f654e600438fc455cc464efc1f9e2ffd4c5466`.

```text
2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )
8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
                                                           ∂ X.
We will need the following lemma, which is a consequence of deep results in [CT21] in
general, although it has an elementary proof for good spaces.
Lemma 2.12. If X is a k-analytic space and k′ /k is an analytic field extension, then
                                          πk′ /k (∂ X k′ ) = ∂ X .
Proof. We have πk′ /k (∂ X k′ ) ⊂ ∂ X by 2.11(5′ ). Let x ∈ ∂ X , and let U ⊂ X be a compact
neighborhood of x. We claim that x ∈ ∂ U. If not, then there is an open neighborhood
V of x in U such that ∂ V = ; by 2.11(1′ ). If V ′ ⊂ V is a smaller open neighborhood of
x in X , then ∂ V ′ = ; as well by 2.11(3′ ) and by (2.11.4) as applied to V ′ → V → M (k).
Thus we may assume that V is open in X , which implies by 2.11(1) that x ∈ Int(X ), a
contradiction. Hence x ∈ ∂ U. If x ′ ∈ π−1      k′ /k
                                                      (x), then x ′ ∈ ∂ Uk′ if and only if x ′ ∈ ∂ X k′
for the same reason. We need to show π−1        k′ /k
                                                      (x) ∩ ∂ X k′ ̸= ;, so we may replace X by U to
assume that X is compact. In this case, the closed subset ∂ X k′ is compact; suppose that
it is disjoint from π−1
                      k′ /k
                            (x). Then πk′ /k (∂ X k′ ) is a closed subset of X not containing x, so
there exists an open neighborhood V of x such that Vk′ = π−1            k′ /k
                                                                              (V ) ⊂ Int(X k′ ). This means
that ∂ Vk′ = ; by 2.11(3,4). But x ∈ ∂ V , and boundarylessness can be checked after
extension of scalars by [CT21, Theorem 11.5]. This contradiction proves the claim. □
```

### GR real PL convention

GR.txt, LF 416--431; SHA-256 `c30a5a23188cfc7e14645e2e73e4ec8c8a374163732de3fe815591d462b04435`.

```text
2.16. PL functions. We will assume k is non-trivially valued when we discuss PL func-
tions. Let Λ be a subgroup of R which is either divisible or equal to Z. We consider a
good, strictly k-analytic space PX . A function h: X → R is called Λ-piecewise linear or
Λ-PL if G-locally we have h = j λ j log | f j | for finitely many λ j ∈ Λ and invertible ana-
lytic functions f j . Here we use the G-topology of X generated by the strictly k-analytic
domains. We refer to [GJR21, Section 5] for more on Λ-PL functions.

2.17. Reduction of germs. For a good, strictly k-analytic space X over a non-trivially
valued field, Temkin [Tem00] introduced the reduction of the germ (X , x) at x ∈ X as
an open subset of a Zariski–Riemann space PHf(x)/ek of H    f(x)/ek. Roughly speaking, it
is the projective limit of all canonical reductions Spec(A  f) where M (A ) ranges over
all k-affinoid neighborhoods of x. The germ (X , x) is naturally a quasicompact locally
ringed space. See also [CD12, Section 6.1] for an excellent summary. An R-PL function
h: X → R induces a residue line bundle L(h) ∈ Pic(X , x)R . This was introduced in [CD12],
and is explained in [GJR21, Section 6]. We call h semipositive at x if L(h) is nef in the
sense of [GJR21, Section 7]. A semipositive R-PL function is semipositive at all x ∈ X .
```

### GR curves, subharmonic definition and Proposition 3.5

GR.txt, LF 453--522; SHA-256 `9dcb2805b2ec6b27e3bf02e0a53f1c0b2c7315348e4784b83535ec01c56e0cd8`.

```text
  In this section, we generalize Thuillier’s theory [Thu05] of subharmonic functions from
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
   (1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
        Proposition 3.3.7]
   (2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
   (3) If X is an affinoid k-analytic curve, then ∂ X coincides with the Shilov boundary
        of X . [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X → R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X → R ∪ {−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂ X and every harmonic function h: U → R, if u ≤ h on ∂ U
then u ≤ h on U.
  Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞ to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪ {−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′ /k, every smooth, connected,
strictly k′ -analytic curve Y , and every morphism Y → X k′ , the composition
                                        πk′ /k     u
                              Y −→ X k′ −→ X −→ R ∪ {−∞}
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              11

is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X → R ∪ {−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X → R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
  Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper
semicontinuous function.
   (1) (Sheafiness) The subharmonic functions form a sheaf on X .
   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.
   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .
   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.
   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
       Int(X ), then u is constant in a neighborhood of x.
   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic
       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.
   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u
       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and
       surjective.
   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,
       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.
  Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense
```

### GR two signs and harmonic definition

GR.txt, LF 1042--1061; SHA-256 `318b4943b3933359360281150a468635684abb39a253ab4213bea738c8d91cca`.

```text
3.12. Now we turn to harmonic functions. Let X be a smooth, strictly k-analytic curve
with k non-trivially valued and let h: X → R be a function. We claim that h is harmonic
in the sense of (3.2) if and only if h and −h are subharmonic (in our sense or Thuillier’s—
see (3.4.2)). This is implicit in Thuillier’s thesis, but it requires justification. Suppose then
that h: X → R is harmonic. Then ±h are subharmonic by [Thu05, Proposition 2.3.13 and
Corollaire 3.1.12]. Conversely, suppose that ±h are subharmonic. This implies that h is
continuous. Let U ⊂ X be a strictly affinoid domain. By [Thu05, Lemme 2.3.9], there
exists a unique harmonic function h′ : U → R that coincides with h on ∂ U. By definition
20                                 W. GUBLER AND J. RABINOFF

of subharmonicity, we have h ≤ h′ on U. By the same argument as applied to −h, we see
that h = h′ on U, so that h is harmonic on U. As U was arbitrary, h is harmonic.
  By 3.12, the following definition recovers Thuillier’s definition of harmonicity on a
smooth, strictly k-analytic curve, and even on a strictly affinoid rig-smooth curve us-
ing [Thu05, Corollaire 2.3.14].
Definition 3.13 (Harmonic functions). Let X be a k-analytic curve for a possibly trivially
valued non-Archimedean field k. A function h: X → R is harmonic if h and −h are both
subharmonic.
   The advantage of this definition is that the following basic properties of harmonic func-
tions follow immediately from the corresponding properties of subharmonic functions.
```

### GR classical pluriharmonic definition

GR.txt, LF 1831--1836; SHA-256 `0bd4c30d65b35555f71d71cbbf90ab669b5da34b14f565e51040614c2270376b`.

```text
                               7. PLURIHARMONIC FUNCTIONS
  In this section, we consider a k-analytic space X over any non-Archimedean field k.
Following the discussion of harmonic functions on curves in 3.12, we generalize this
notion as follows to higher dimensions.
Definition 7.1. A function h: X → R is called pluriharmonic if h and −h are classically
psh functions (see Definition 4.1).
```

### GJR field convention

GJR.txt, LF 339--343; SHA-256 `ce419b7d82b4e853c82fcbe59d69b526f31ff5cea7a4f682dc826b900dba6b0d`.

```text
2.2. Non-Archimedean Fields. Throughout the whole paper, we fix a field K that is
complete with respect to a non-trivial non-Archimedean complete absolute value de-
noted | |: K → R. We will call this a non-trivially valued non-Archimedean field. A non-
Archimedean extension field is a non-Archimedean field K ′ equipped with an isometric
embedding K ,→ K ′ .
```

### GJR PL definition and domain conventions

GJR.txt, LF 1628--1661; SHA-256 `105c91a086cb4d4bb27760f4bcbed6bd8bfa19bbd1b817109ac725b11a27921e`.

```text
to fix our ideas. We will find it useful to work slightly more generally with piecewise
linear functions with slopes contained in an additive subgroup Λ ⊂ R, and in some cases
new arguments are needed. In practice we will usually take Λ = Z, Q, or R, in which case
either Λ = Z or Λ is divisible.
   In this section, K is a non-Archimedean field with a non-trivial valuation v and value
group Γ := v(K × ) ⊂ R. We consider a good strictly K-analytic space X and an additive
subgroup Λ ⊂ R. Recall from 2.3 that a strictly analytic space is good provided that that
every point has a strictly affinoid neighbourhood. Most strictly analytic spaces occurring
in practice are good: for example, any strictly affinoid space, a space with no boundary,
or an analytic subdomain of the analytification of an algebraic variety. We restrict our
attention to good spaces as then the coherent modules on the Berkovich space X are
the same as the coherent modules on the space X G endowed with the G-topology [Ber93,
Proposition 1.3.4], which makes it reasonable to work with line bundles on X . We always
               FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                       31

use the G-topology on X generated by the strictly affinoid domains. Let C(X ) be the space
of continuous real functions on X .
Definition 5.1. A function h: X → R is called piecewise Λ-linear or Λ-PL if there exists a
                                                                                                    ×
G-covering {XP i } of X such that for each i, there are finitely many λi j ∈ Λ and f i j ∈ O (X i )
with h|X i = j λi j log | f i j |. A Z-PL function is called piecewise linear or PL.
  We denote the group of PL functions on X by PL(X ), and the group of Λ-PL functions
by PLΛ (X ). These are subgroups of C(X ).
5.2. Some remarks:
   (1) A function h: X → R is PL if and only if there exists a G-covering {X i } of X and
       f i ∈ O (X i )× such that h|X i = log | f i |.
   (2) The set of Λ-PL functions on X forms a group since any two G-coverings {X i } and
       {X ′j } admit the common refinement {X i ∩ X ′j }.
   (3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.
   (4) The presheaf U 7→ PLΛ (U) is a sheaf in the G-topology, and therefore in the ana-
       lytic topology as well.
   (5) A function h: X → R is Λ-PL if and only if there exists a G-covering {X i } of
       X suchPthat for each i, there are finitely many λi j ∈ Λ and hi j ∈ PL(X i ) with
       h|X i = j λi j hi j .
```

### GJR harmonic definition and numerical triviality

GJR.txt, LF 2331--2346; SHA-256 `224d6b851b30d23490090985374ba845adea25b889f7b6c2b940d10f5c163da7`.

```text
Definition 7.2. A Λ-PL function h: X → R is called semipositive at a point x ∈ X if it
satisfies the equivalent conditions of Proposition 7.1, and it is harmonic at x if both h
and −h are semipositive at x. We say that h is semipositive if it is semipositive at all
points of X .
   A harmonic function on X is an R-PL function h: X → R which is harmonic at all points
of X . A Λ-PL harmonic function is called Λ-harmonic.
7.3. Some remarks:
   (1) A Λ-PL function h is harmonic at x ∈ X if and only if Lh (x) is numerically trivial.
       Equivalently, there exists a paracompact neighbourhood U of x, a formal K ◦ -
       model U of U, and a numerically trivial element L ∈ M (U)Λ , such that h = hL .
   (2) Semipositivity and harmonicity are insensitive to the group Λ, in the following
       sense: if h ∈ PLΛ (X ), then h is semipositive at a point x if and only if its image in
       PLR (X ) is semipositive at x.
   (3) Semipositivity and harmonicity of h at x is intrinsic to the germ of h in PLΛ (X , x).
       In particular, the semipositive (resp. harmonic) functions on X form a sheaf in
       the analytic topology. (They do not form a sheaf in the G-topology).
```

### Thuillier harmonic scalar extension full proposition

Thuillier.txt, LF 3551--3564; SHA-256 `352b93b53190d7d0b173538f4a762d78c63d3a03b253a680db05ad2e4ffbb209`.

```text
  Étant donné un domaine k-anoïde Y d'une ourbe k-analytique lisse X , nous noterons
H(Y ) le sous-espa e ve toriel
                                   Γ(Y − ∂Y, HX ) ∩ C0 (Y, R)
de C0 (|Y |, R) ; vu le orollaire 2.3.14, ette notation oïn ide ave elle introduite pré édem-
ment lorsque Y est stri tement k-anoïde.
   La orrespondan e Y 7→ H(Y ) est un préfais eau sur le G-site XG de X qui prolonge
évidemment le préfais eau sur le site XR déni au début de 2.3.3.
Proposition 2.3.18.  Soient X une ourbe stri tement k -analytique lisse et K une ex-
tension non ar himédienne de k ; notant XK pour X ⊗       b k K et pK le morphisme anonique
XK → X , pK HX ⊂ HX ⊗
              ∗
                          b kK .
Démonstration. C'est une onséquen e immédiate de la dénition du fais eau HX et du
lemme 2.3.5.                                                                                      2
```

### Thuillier subharmonic comparison definition

Thuillier.txt, LF 3783--3788; SHA-256 `db1a6300516b398b3b02986c03c2ef2e3773dbcc369362f7a7ed7cf6dbdd1353`.

```text
3.1.2. Fon tions sous-harmoniques.
Définition 3.1.5.  Soit Ω un ouvert de X ; une fon tion u : Ω → R ∪ {−∞} est dite
sous-harmonique si elle est semi- ontinue supérieurement, n'est identiquement égale à −∞
sur au une omposante onnexe de Ω et satisfait à la ondition suivante : pour tout domaine
stri tement k-anoïde Y dans X et toute fon tion h ∈ H(Y ),
                                  (u|∂Y ≤ h|∂Y ) =⇒ (u|Y ≤ h).
```

### Thuillier semistable harmonic scalar lemma, full proof

Thuillier.txt, LF 3297--3310; SHA-256 `509a497641391582651fc124e97eeaf9ca28609881dd7824df099d63895bc77b`.

```text
Lemme 2.3.5.  Soient X         une S - ourbe simplement semi-stable (quasi- ompa te ) et K/k
une extension non-ar himédienne ; une fon tion h ∈ C0 (|Xη |, R) appartient au sous-espa e
H(X ) si et seulement si la fon tion p∗K h appartient au sous-espa e H(X ×S Spf(K ◦ )).
Démonstration. Le morphisme anonique pK : Xη ⊗            b k K → Xη induit un isomorphisme
G-lo al surje tif S(X )K → S(X ) de polyèdres entiers pondérés (proposition 2.2.21) et, les
 omposantes irrédu tibles anes de la K   e - ourbe Xs ⊗e K   e étant les images ré iproques des
                                                           k
                                                             −1
 omposantes irrédu tibles anes de Xs , ∂(Xη ⊗  b k K) = pK (∂Xη )) ∩ S0 (X ×S Spf(K ◦ )). Ce i
implique, pour tout fon tion Φ ∈ A (S(X )), que la fon tion p∗K Φ appartient à A0 (S(X )K ) et
                                     0

que le support de la mesure ddc Φ = (pK )∗ ddc p∗K Φ est ontenu dans ∂Xη si et seulement si
 elui de la mesure ddc p∗K Φ est ontenu dans ∂(Xη ⊗  b k K).                                  2
```
