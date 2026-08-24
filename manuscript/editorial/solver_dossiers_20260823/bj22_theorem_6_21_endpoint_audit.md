# BJ22 Theorem 6.21: critical homogeneous Siu-division endpoint

**Audit date:** 23 August 2026  
**Status:** SOURCE GAP CONFIRMED; GENERAL REPAIR OPEN AFTER ATTEMPT;
CONDITIONAL REPAIR AVAILABLE; ALL CANDIDATE-ONLY MATERIAL IS PENDING
RETHLAS.  
**Book disposition:** editorial quarantine only. This file does not authorize
a change to theorem typography in Chapter 35.  
**Excluded source:** the author's Deligne--Riemann--Roch/Deligne-pairing
paper arXiv:1710.09731 is known by the author to contain an error. It was not
consulted, is not cited below, and is forbidden as an input to any later
verification.

## 1. Exact question

Let \(k\) be an algebraically closed field with the trivial absolute value,
let \(X\) be a normal integral projective \(k\)-variety, let
\(\theta\in N^1(X)_{\mathbf R}\), and let \(E\ne0\) be an effective
\(\mathbf Q\)-Cartier divisor. Write

\[
  \ell_E:=\log|s_E|,\qquad \ell_E(v)=-v(E)\in[-\infty,0].
\]

For \(\psi\in\operatorname{PSH}_{\mathrm{hom}}(X,\theta)\), BJ22,
Theorem 6.21 asserts

\[
 \psi\le \ell_E
 \quad\Longleftrightarrow\quad
 \psi=\ell_E+u\ \text{for a unique }
 u\in\operatorname{PSH}_{\mathrm{hom}}(X,\theta-[E]).
 \tag{S}
\]

At a semivaluation supported in \(E\), the right side is an identity of
sums with value \(-\infty\); \(u\) is never defined there by subtracting
two infinite values. On \(X^{\mathrm{div}}\), where both \(\psi\) and
\(\ell_E\) are finite, its divisorial trace must be

\[
                     u(v)=\psi(v)-\ell_E(v)=\psi(v)+v(E).
 \tag{1}
\]

The converse implication and uniqueness follow from homogeneous
normalization and divisorial determination. The only issue is existence of
a psh extension of the trace in \((1)\) in the critical case.

## 2. What the published proof actually gives

BJ22, Corollary 6.17 gives a decreasing net

\[
 \psi_i\in\mathcal H_{\mathrm{hom}}(L_i),\qquad
 c_1(L_i)\longrightarrow\theta,\qquad
 \psi_i\searrow\psi.
\]

Let \(K_E=\{\ell_E=-1\}\). At the critical endpoint
\(\sup_{K_E}\psi=-1\), Dini's lemma permits rational \(t_i>0\) such that

\[
       t_i\longrightarrow1,\qquad
       \sup_{K_E}\psi_i\le -t_i.
\]

Homogeneity and normality then give the stagewise division

\[
 \rho_i:=\psi_i-t_i\ell_E
 \in\mathcal H_{\mathrm{hom}}(L_i-t_iE),\qquad
 c_1(L_i)-t_i[E]\longrightarrow\theta-[E].
 \tag{2}
\]

These facts do not imply that \(\rho_i\) decreases. For \(j\ge i\),
comparison on \(K_E\) gives the exact condition

\[
 \rho_j\le\rho_i
 \quad\Longleftrightarrow\quad
 t_j-t_i\le\inf_{K_E}(\psi_i-\psi_j).
 \tag{3}
\]

The order \(\psi_j\le\psi_i\) separately handles the locus \(v(E)=0\).
Neither Dini's lemma nor the conditions in \((2)\) imply \((3)\).
Thus BJ22, Theorem 4.5, which is a decreasing-closure theorem, cannot be
applied to the displayed residual family.

The local copy of the published article was checked directly. Its proof
says: “Since \((\psi_i)\) is a decreasing net, \((\psi_i')\) is
decreasing on \(X^{\mathrm{div}}\).” The coefficient \(t_i\) varies, so
this sentence omits exactly the term tested in \((3)\).

## 3. A counterexample to the monotonicity inference

The following is a counterexample to the proof inference, not to
\((S)\). It is candidate-only until Rethlas checks the exact arithmetic.

Take \(X=\mathbf P^1\), a closed point \(p\in X\), \(E=p\), and
\(\ell=\log|s_E|\). For integers \(n\ge2\), set

\[
 c_n=1-\frac1{2n},\qquad t_n=1-\frac1n,\qquad
 \psi_n=c_n\ell.
\]

Then

\[
 \psi_n\in\mathcal H_{\mathrm{hom}}(c_nE),\qquad
 c_n[E]\to[E],\qquad \psi_n\searrow\ell,
\]

because \(c_n\uparrow1\) and \(\ell\le0\). Since \(c_n\ge t_n\),

\[
                         \psi_n\le t_n\ell,
\]

and \(t_n\uparrow1\). Nevertheless

\[
 \rho_n=\psi_n-t_n\ell=\frac1{2n}\ell
\]

is strictly increasing along every divisorial ray on which \(v(E)>0\).
On \(K_E\),

\[
 t_{n+1}-t_n=\frac1{n(n+1)},\qquad
 \inf_{K_E}(\psi_n-\psi_{n+1})=\frac1{2n(n+1)}.
\]

Thus \((3)\) fails by the factor \(2\). All stages are genuine
homogeneous Fubini--Study functions of rational classes. In this example
\((S)\) is still true: the endpoint residual is
\(0\in\operatorname{PSH}_{\mathrm{hom}}(0)\).

This also shows why merely choosing \(t_i\uparrow1\), or passing to a
cofinal subnet, does not repair the source proof.

## 4. Results that survive without an envelope theorem

### 4.1 Strict room

If

\[
                       \psi\le t_0\ell_E\quad\text{for some }t_0>1,
\]

then the homogeneous regularizing functions eventually satisfy
\(\psi_i\le\ell_E\). Division by the fixed divisor \(E\) produces a
decreasing residual net. This proves \((S)\) for normal projective \(X\)
in arbitrary characteristic under the strict hypothesis. This is already
proved internally in Chapter 35.

### 4.2 Every subcritical coefficient

Assume only \(\psi\le\ell_E\). For every rational \(0<t<1\), apply the
strict result to the divisor \(tE\): since

\[
  \psi\le\ell_E=t^{-1}\ell_{tE},\qquad t^{-1}>1,
\]

one obtains

\[
 u_t:=\psi-t\ell_E
 \in\operatorname{PSH}_{\mathrm{hom}}(X,\theta-t[E]).
 \tag{4}
\]

On \(X^{\mathrm{div}}\), \(u_t\uparrow u\) as \(t\uparrow1\), where
\(u\) is the trace in \((1)\). This is an increasing limit and hence lies
outside BJ22, Theorem 4.5. The missing endpoint is precisely the assertion
that this particular increasing limit is psh.

## 5. A rigorous conditional endpoint repair

The following proof is pending Rethlas as an exact integration packet. It
is a reconstruction of the mechanism used in Boucksom--Jonsson,
*Non-Archimedean Green's functions and Zariski decompositions*,
Proposition 17, specialized to a normal variety and a rational Cartier
divisor. No priority or novelty claim is made.

Fix an ample class \(\omega\). Put \(\alpha=\theta-[E]\), and assume:

> **Independent envelope input.** For a sequence
> \(\varepsilon_m\downarrow0\), each class
> \(\alpha+\varepsilon_m\omega\) has the envelope property by a proof that
> does not use \((S)\), BJ22, Theorem 6.31, or any theorem depending on
> them.

For fixed \(m\), choose rational \(t<1\) close enough to \(1\) that

\[
 \varepsilon_m\omega-(1-t)[E]\in\operatorname{Amp}(X).
\]

By \((4)\) and addition of the zero potential in this ample difference
class,

\[
        u_t\in\operatorname{PSH}_{\mathrm{hom}}
        (X,\alpha+\varepsilon_m\omega).
\]

The family is bounded above by \(0\) and increases with \(t\). The
independent envelope property gives

\[
 U_m:=\left(\sup_{t<1}u_t\right)^*
 \in\operatorname{PSH}
 (X,\alpha+\varepsilon_m\omega).
 \tag{5}
\]

BJ22, Theorem 5.6, which says divisorial points are nonnegligible, gives
\[
                         U_m|_{X^{\mathrm{div}}}=u.
\]
The trace \(u\) is homogeneous. Since the scaling action preserves the psh
class, the scaled function \(s\mathbin{\cdot}U_m\) is psh and has the same
divisorial trace as \(U_m\) for every \(s>0\). Divisorial determination
therefore shows that \(U_m\) is homogeneous.

For different \(m\), the functions \(U_m\) have the same divisorial
trace. BJ22, Theorem 4.22 applied in both directions shows that they are
the same upper-semicontinuous function \(U\), even though their psh
classes differ. Thus

\[
 U\in\operatorname{PSH}_{\mathrm{hom}}
 (X,\alpha+\varepsilon_m\omega)\quad\text{for every }m.
\]

Closedness in the numerical class, BJ22, Theorem 4.5, yields

\[
                 U\in\operatorname{PSH}_{\mathrm{hom}}(X,\alpha).
\]

Its divisorial trace is \((1)\), hence divisorial determination gives
\(\psi=\ell_E+U\) on all of \(X^{\mathrm{an}}\). No subtraction at a
proper-support point has occurred.

This establishes the endpoint whenever the displayed envelope inputs are
known independently. In particular:

- if \(X\) is smooth and \(\operatorname{char}k=0\), the
  Boucksom--Jonsson addendum, Theorem A supplies them without invoking
  Theorem 6.21;
- if \(X\) is smooth of dimension at most \(2\), the same theorem supplies
  them in arbitrary characteristic, so the rational-Cartier statement above
  follows;
- for a normal projective curve, normality implies smoothness, so the result
  holds in arbitrary characteristic;
- under the smooth characteristic-zero standing assumptions,
  Boucksom--Jonsson's later Proposition 17 proves the corresponding
  statement for effective real divisors.

The argument does not provide a noncircular proof for a general normal
projective variety in arbitrary characteristic when its envelope property
is itself being proved using homogeneous Siu division.

## 6. Why the obvious alternative routes are circular

1. Closure of a bounded-above increasing psh net is equivalent to the
   envelope property, by BJ22, Theorem 5.11. Applying it to \((4)\) is the
   conditional proof above, not an unconditional repair.
2. BJ22, Theorem 6.31 invokes Theorem 6.21.
3. The converse directions of BJ22, Theorems 6.35 and 6.40 use Theorem
   6.21 and compactness supplied by the envelope property.
4. Pullback to a resolution or alteration is safe, but the birational
   reflection and finite-descent packages used in the book's envelope proof
   invoke homogeneous Siu division. Without a new independent descent
   theorem, this route closes the same loop.
5. Pointwise subtraction is undefined at semivaluations supported in \(E\),
   and nonmonotone convergence of the residuals is not a psh closure axiom.
6. The later Green-functions Proposition 17 explicitly uses the envelope
   property in its general step. It is a post-envelope confirmation, not an
   unconditional proof of the input to the envelope theorem.

## 7. Clean formulation of the unresolved input

At the homogeneous FS level, multiplication by the canonical section gives
the bijection

\[
 \mathcal H_{\mathrm{hom}}(L-E)
 \longrightarrow
 \{\phi\in\mathcal H_{\mathrm{hom}}(L):\phi\le\ell_E\},\qquad
 u\longmapsto u+\ell_E.
\]

The unresolved endpoint asks whether this bijection survives the minimal
decreasing closure used to define psh functions:

\[
 \operatorname{PSH}_{\mathrm{hom}}(\theta-E)
 \stackrel{?}{\longrightarrow}
 \{\psi\in\operatorname{PSH}_{\mathrm{hom}}(\theta):
   \psi\le\ell_E\}.
 \tag{F}
\]

Injectivity and the forward inclusion are elementary; surjectivity is
\((S)\). Thus the genuinely local target is an order-closed
fixed-divisor face lemma. Proving \((F)\) from the FS definition, without
arbitrary increasing closure, would repair the endpoint and avoid the
envelope theorem. No such proof was located in the sources checked here.

This reformulation and any attempted proof of it are pending Rethlas.

## 8. Source and file ledger

Primary sources checked:

- BJ22, Definition 4.1; Theorems 4.5, 4.7, 4.15, 4.22, 5.6, 5.11,
  and 6.21; Corollaries 4.23 and 6.17; Lemma 2.23.
- Boucksom--Jonsson addendum, Theorem A and its multiplier/test-ideal proof.
- Boucksom--Jonsson, *Non-Archimedean Green's functions and Zariski
  decompositions*, Proposition 17.

Local source hashes at the time of this audit:

- BJ22 PDF:
  8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52;
- BJ22 extracted text:
  af5a9b9d62570a37d9ad11d139e99353e8b50f1f1c55557fbfcf2cb37cca0c8f;
- Chapter 35 as observed during the audit:
  45d39f528be1a0092be409e24f3aec575256ce10d6782dec831ff12e96a34851.

The Chapter 35 hash is observational only: another proof-depth pass may
change that file. No edit to Chapter 35 was made in this task.

## 9. Disposition

| Item | Status |
|---|---|
| Strict endpoint \(\psi\le t_0\ell_E,\ t_0>1\) | proved internally, normal/arbitrary characteristic |
| Fixed rational \(t<1\) residual | proved internally, normal/arbitrary characteristic |
| Printed monotonicity inference in BJ22, Theorem 6.21 | false; explicit \(\mathbf P^1\) candidate counterexample above, pending Rethlas |
| Critical endpoint assuming independently established nearby EP | complete conditional proof, pending exact Rethlas audit |
| Smooth characteristic zero | literature-supported through independent EP; later Proposition 17 confirms and extends to real divisors |
| Smooth dimension at most \(2\), arbitrary characteristic, \(E\) rational Cartier | follows from independent EP and the conditional proof |
| General normal projective \(X\), arbitrary characteristic, without EP | OPEN AFTER ATTEMPT; no counterexample to the theorem found |
