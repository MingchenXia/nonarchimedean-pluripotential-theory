# Ordinary currents, top cohomology, and the actual P21.3 multiplier target

Date: 1 September 2026. Author: /root/p081_weighted_repair_fresh.

## 1. Outcome and scope

None of the exact primary-source interfaces checked in SOURCE_LEDGER.md
supplies the desired general rigidity theorem for ordinary CLD positive
separately closed currents of bidegree (0,0) on arbitrary connected ordinary
opens of a smooth algebraic analytification over the original complete DVR
field of residue characteristic zero. This is a bounded literature diagnosis,
not a claim that no other relevant theorem exists.

More importantly, full constant-current rigidity is only a sufficient route
to the bidegree-(0,0) multiplier problem, not a necessary intermediate theorem.
The direct target is

\[
 h\in C(W),\quad \mathrm d'\mathrm d''[h]=0
 \quad\Longrightarrow\quad
 \mathrm d'\mathrm d''(hT)=0.                 \tag{M}
\]

Here W is an actual ordinary open, T is an ordinary positive separately
closed current on W, and h is real-valued and continuous. The printed
Chapter 72 problem asks this for h=U−V from continuous psh pairs and includes
bidegrees (p,p), 0≤p≤n−1. Consequently proving rigidity only for p=0 would
not, without an additional argument, resolve that entire printed problem.
No current is pulled back to a field extension in this diagnosis.

There is a direct sufficient function-class criterion: if both h and −h
belong locally to CLD's ordinary CPsh sheaf, then (M) holds for every
positive closed T, including the higher bidegrees. Section 5 proves this
criterion and separates it from its unproved applicability to all h in (M).

## 2. The exact ordinary-topology rigidity question

Fix a nonempty connected ordinary W of pure dimension n. Use the ordinary
CLD compact-test locally convex topology, not pointwise convergence on a
skeleton and not a weakly smooth substitute. Set

\[
 E=\mathcal A_c^{n,n}(W),\qquad
 B=\mathrm d'\mathcal A_c^{n-1,n}(W)
       +\mathrm d''\mathcal A_c^{n,n-1}(W),\qquad
 I(\alpha)=\int_W\alpha .                    \tag{1}
\]

CLD25 §§3.7, 6.4 and 7.1 define this topology and its continuous dual.
The differentials are continuous. CLD25 §7.7 defines current differentials
by transposition, so a bidegree-(0,0) continuous current is separately closed
exactly when its functional annihilates B. Stokes gives B⊂ker I.
Accordingly the continuous closed-current space is the continuous dual of
E/B, equivalently of E/closure(B). Algebraic cohomology alone does not
identify this Hausdorff quotient.

A sufficient, and for all real continuous separately closed currents also
necessary, criterion for rigidity is

\[
                       \overline B^{\,E}=\ker I.             \tag{2}
\]

For sufficiency choose ω₀∈E with I(ω₀)=1. Then
α−I(α)ω₀∈closure(B), so T(α)=T(ω₀)I(α). Such ω₀ exists because the
canonical integration current has full support; it can be chosen positive.
Positivity of T then gives T(ω₀)≥0. Conversely, if (2) fails, a point of
ker I outside the closed subspace closure(B) can be separated in the
locally convex Hausdorff quotient by a continuous linear functional.
Its pullback is separately closed but not a multiple of I. This separation
does not ensure positivity. Thus the positive-current question can be weaker
than (2).

In particular, infinite-dimensional *algebraic* top Dolbeault cohomology
does not itself construct a continuous positive nonconstant current. Nor
does it prove (2) false: the additional d'-boundaries and the closure in
the actual ordinary test topology must both be accounted for. This packet
does not assert that any particular cohomology group here is non-Hausdorff.

An ordinary-form Poincaré-duality theorem giving
H^{0,0}(W)≅Hom_R(H_c^{n,n}(W),R), with H^{0,0}(W)=R and the pairing given
by integration, would be more than enough: a d''-closed current already
defines the required algebraic functional. The difficulty is finding that
theorem for the *same W, same sheaf, and same original field*.

## 3. What the checked cohomology results do and do not imply

The source ledger records four distinct limitations. Ordinary local
Poincaré lemmas concern one differential, not a real-manifold de Rham
resolution in total degree. Ordinary top cohomology already has known
curve obstructions. Tropical-manifold duality assumes special local
models, not merely a full-rank moment. The better curve duality of the
weakly smooth theory uses a different test sheaf.

The relevant compact-support direct-limit theorems do allow refinement of
forms and cohomology classes. They do not assert (2), positivity of a
separating functional, or identification of constants on every source sheet.
In particular a connected source does not force a chosen moment's
full-rank locus to be connected. Adding a moment may connect pieces by
cells contracted by the original moment. One must prove the required
comparison across those cells; connectedness alone does not do so.
No fixed-moment example is treated here as a counterexample to (M).

## 4. Extensions exist; closed extension is the unresolved issue

Let E_sm and E_w denote top compact ordinary and weakly smooth test spaces.
GJR, harmonic-tropicalization paper, §12.1 gives E_sm the induced subspace
topology from E_w. Hence Hahn–Banach gives a noncanonical continuous
linear extension of an ordinary current. Claiming that no such extension
exists would be wrong. CLD25 Theorem 7.4.4, Proposition 7.4.5 and Corollary
7.4.6 additionally give canonical positive C⁰-continuous evaluation on
compact G-smooth G-form representatives under their stated tropical-space
hypotheses. The weakly smooth forms have such piecewise representatives
(GJR Proposition 10.14 and Remark 10.15).

Neither observation licenses differential commutation for an arbitrary
ordinary closed T on the additional primitives. CLD25 (7.7.2.2) explicitly
retains a boundary current for a G-form. GJR Remark 10.11 similarly
distinguishes polyhedral derivatives from current derivatives. Thus mere
positive evaluation is not the missing theorem; the missing issue is
annihilation of the new boundary tests.

Here is an elementary algebraic diagnostic, independent of any analytic
extension construction. Put

\[
 B_w=\mathrm d'\mathcal A_{w,c}^{n-1,n}(W)
       +\mathrm d''\mathcal A_{w,c}^{n,n-1}(W).
\]

An ordinary functional T has an algebraic extension to E_w annihilating
B_w if and only if

\[
                         T(E_{sm}\cap B_w)=0.                \tag{3}
\]

Necessity follows by restriction. For sufficiency, T is well-defined on
the image of E_sm in E_w/B_w, and a linear functional extends from that
subspace to the whole vector space. Continuity and positivity remain
additional conditions. If a weak-form trace theorem identifies B_w with
the weak integration kernel, then (3) already forces T to vanish on the
ordinary integration kernel. In that situation silently assuming a closed
extension imports essentially the desired rigidity rather than proving it.

This observation does not say that a closed extension cannot exist. It
identifies the compatibility that must be proved before weak-form duality
can be used on arbitrary ordinary currents.

## 5. Direct ordinary multiplication criteria

### 5.1 The two-sided ordinary CPsh criterion

Let C be the smallest subsheaf of continuous functions generated by ordinary
smooth functions with positive smooth Hessian and closed under local
uniform limits. This is precisely CLD25 CPsh, Definition 8.1.7. No
identification with every distributionally psh continuous function is
assumed.

For a fixed positive closed T, let P_T(U) consist of continuous f on U
for which d'd''(fT|_U) is positive. This is a sheaf. It contains ordinary
smooth psh functions by the ordinary Leibniz identity and positivity of
their Hessians. It is stable under uniform limits: for a compact ordinary
test α, the signed Radon measure μ_T^α gives

\[
 |\langle(f_j-f)T,\alpha\rangle|
 \leq\|f_j-f\|_{\operatorname{supp}\alpha}
                  |\mu_T^\alpha|(W)\longrightarrow0.
\]

Current differentiation is continuous and the positive cone is weakly
closed. Therefore C⊂P_T. This is the argument of CLD25 Lemma 8.5.5,
using its continuous CPsh definition; it makes no Bedford–Taylor
independence assumption.

If h and −h are locally in C, both S=d'd''(hT) and −S are positive.
Positive test forms span the symmetric test space and S is symmetric,
so S=0. Local identities glue on ordinary opens. This establishes the
sufficient criterion at the original field and in all relevant bidegrees.

In particular it applies to local uniform limits of ordinary smooth
functions with zero smooth Hessian, including local real combinations of
logarithms of analytic units. It does not show that every h in (M) has
such approximants. The missing general input is

\[
 h\in C(W),\quad d'd''[h]=0
       \quad\Longrightarrow\quad h,-h\in CPsh_{ordinary,loc}. \tag{4}
\]

CLD25 Proposition 8.3.1 gives the required reverse distributional-to-psh
implication for smooth functions only. The equality d'd''[U]=d'd''[V]
for two CPsh functions does not formally put their difference, or its
negative, in CPsh. In particular, subtraction is not a permitted closure
operation. No source checked here establishes (4) in the full target scope.

### 5.2 A narrower boundary-approximation criterion

For p=0 and each ordinary η∈A_c^{n−1,n−1}(W), it would suffice to
approximate h d'd''η by ordinary elements b_j∈B in a controlled C⁰
module, as follows. Require a compact K⊂W, finitely many fixed ordinary
top forms θ₁,…,θ_N supported in K, and continuous source functions
a_{j,l} with

\[
 h\,d'd''\eta-b_j=\sum_{l=1}^N a_{j,l}\theta_l,
       \qquad \max_l\|a_{j,l}\|_K\longrightarrow0.            \tag{5}
\]

The equality can be taken in the space of forms with continuous source
coefficients; their evaluation is the Radon-measure extension of ordinary
positive currents. In particular h is not presumed to factor through a
fixed tropical chart. All b_j are actual sums of differentials of compact
ordinary primitives on W.

Then T(b_j)=0 and

\[
 |\langle hT,d'd''\eta\rangle|
 \leq\sum_l\|a_{j,l}\|_K\,|\mu_T^{\theta_l}|(W)
       \longrightarrow0.
\]

Thus (M) follows. This asks for boundary approximation only for the
specific multiplier family h d'd''η, not for every zero-integral top form.
The hypothesis d'd''[h]=0 supplies necessary integration compatibility,
but not the approximation (5). Existence of (5) is not proved here.
This formulation also avoids confusing ordinary C^∞ test convergence
with the weaker coefficient control available specifically to positive
order-zero currents.

## 6. Source cautions directly relevant to the proposed shortcut

CLD25 §8.6.1 and Definition 8.6.2, pp.207–208, explicitly isolate the
equal-Hessian independence property as the Bedford–Taylor condition on
T. Proposition 8.11.1 and Corollary 8.11.2, pp.220–222, assume it.
They cannot be used to establish that predicate for an arbitrary T.

Corollary 8.11.3, p.223, prints a positive-closed hypothesis but its proof
invokes the preceding corollary without establishing its Bedford–Taylor
hypothesis. It is therefore not a justified source interface for this
shortcut. This is a missing hypothesis/proof interface in that argument,
not a claimed counterexample to its conclusion. In addition, “harmonic”
in Definition 7.8.2 is generated locally by PL harmonic functions;
Remark 7.8.3 warns against identifying it with every continuous kernel
element of d'd''.

Also do not use the literal Corollary 8.6.7 to assert that multiplying a
Bedford–Taylor current by any positive continuous function retains
closedness. Its definition includes closedness, whereas already on an
ordinary real interval u times the integration current is not closed for
positive smooth u with nonzero derivative. This elementary closure
omission is not a P21.3 counterexample and no general CLD errata audit is
attempted here.

## 7. Recommended bounded next target and status

For the actual multiplier problem, first test (4) on the precise local
class of h produced by the manuscript's existing reductions. Prove the
ordinary approximation statement for that class, or give a genuine
obstruction; do not replace its ordinary topology by weak smoothness.
If that is unavailable, (5) gives a more localized target involving the
specific multiplier tests. Full trace-kernel density (2) is a stronger
alternative and may be unnecessary.

This packet supplies no common-constant theorem, no arbitrary-current
base change, no all-chart propagation proof, and no retirement of P21.3
or any other open problem. Prior normal-curve and polycylinder results
printed in Chapter 72 are context, not re-audited inputs here. No live
chapter, inventory, earlier dossier, or production gate is changed.
