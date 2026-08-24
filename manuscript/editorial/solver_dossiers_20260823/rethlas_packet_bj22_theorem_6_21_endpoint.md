# Rethlas exact packet: BJ22 Theorem 6.21 critical endpoint

**Requested solver:** gpt-5.6-sol, reasoning effort xhigh.  
**Verification status before launch:** NOT VERIFIED; NO RECEIPT.  
**Promotion rule:** nothing in this packet may enter theorem typography
unless Rethlas returns a complete proof or a complete counterexample and the
exact output blocks are hashed and recorded.  
**Hard source exclusion:** do not use, cite, paraphrase, or infer from the
author's Deligne--Riemann--Roch/Deligne-pairing paper arXiv:1710.09731. The
author reports that paper contains an error.

---

## A. Solver mandate

Perform three logically separate audits.

1. **Source-proof audit.** Decide whether the monotonicity step in the
   printed proof of BJ22, Theorem 6.21 follows from its stated data. Check
   the explicit \(\mathbf P^1\) example in Section G.
2. **Conditional repair audit.** Verify line by line the proof in Section H,
   including the exact envelope hypotheses it needs and the treatment of
   points supported in \(E\).
3. **Unconditional endpoint research.** Under only the allowed inputs in
   Section D, either:
   - prove the target statement in Section B for every normal integral
     projective variety over an algebraically closed trivially valued field,
     in arbitrary characteristic;
   - give a genuine counterexample to that target statement; or
   - return OPEN-AFTER-ATTEMPT with the first precise missing lemma and a
     proof that every proposed route in the response really reduces to it.

A counterexample merely to the printed proof is not a counterexample to the
theorem. Keep these outcomes separate.

---

## B. Exact target statement

### TARGET-STATEMENT

Let \(k\) be an algebraically closed field endowed with the trivial absolute
value. Let \(X\) be a normal integral projective \(k\)-variety,
\(\theta\in N^1(X)_{\mathbf R}\), and \(E\ne0\) an effective
\(\mathbf Q\)-Cartier divisor. Put
\(\ell_E=\log|s_E|\), normalized by
\(\ell_E(v)=-v(E)\in[-\infty,0]\). If
\(\psi\in\operatorname{PSH}_{\mathrm{hom}}(X,\theta)\), then

\[
 \psi\le\ell_E
 \quad\Longleftrightarrow\quad
 \text{there exists a unique }
 u\in\operatorname{PSH}_{\mathrm{hom}}(X,\theta-[E])
 \text{ such that }\psi=\ell_E+u.
\]

The equality is an equality of sums in
\(\mathbf R\cup\{-\infty\}\). At a semivaluation supported in \(E\), its
right-hand side equals \(-\infty\); it is not interpreted as the difference
of two infinite quantities. On \(X^{\mathrm{div}}\), the residual is forced
to have the finite trace \(u(v)=\psi(v)+v(E)\).

### END-TARGET-STATEMENT

---

## C. Definitions and conventions

1. A homogeneous Fubini--Study function for a rational line bundle \(L\) is
   \[
      \phi=m^{-1}\max_j\log|s_j|,
      \qquad 0\ne s_j\in H^0(X,mL),
   \]
   for sufficiently divisible \(m\). It is denoted
   \(\phi\in\mathcal H_{\mathrm{hom}}(L)\).
2. \(\operatorname{PSH}(X,\theta)\) is the class of generically finite usc
   functions that are pointwise decreasing limits of generically finite FS
   functions whose numerical classes converge to \(\theta\), as in BJ22,
   Definition 4.1. A psh function is homogeneous if
   \(\phi(tv)=t\phi(v)\) for all \(t>0\).
3. Every homogeneous psh function is at most \(0\), vanishes at the trivial
   valuation, and is finite on \(X^{\mathrm{div}}\).
4. For an effective rational Cartier divisor \(E\),
   \(\ell_E(v)=-v(E)\). It may equal \(-\infty\) at a point whose support is
   contained in \(E\), but is finite on \(X^{\mathrm{div}}\).
5. Let \(K_E=\{v\in X^{\mathrm{an}}:\ell_E(v)=-1\}\). It is compact.
   Homogeneity promotes inequalities on \(K_E\) to rays on which \(v(E)>0\).
6. Normality gives the FS division fact: if
   \(\phi\in\mathcal H_{\mathrm{hom}}(L)\) and
   \(\phi\le t\ell_E\) for \(t\in\mathbf Q_{>0}\), then the sections in a
   presentation of \(\phi\) are divisible by \(s_{tE}\), and the quotient
   presentation defines
   \(\phi-t\ell_E\in\mathcal H_{\mathrm{hom}}(L-tE)\). This is an identity
   of sections, not pointwise subtraction at a polar point.
7. A class \(\alpha\) has the envelope property if the usc regularization
   of every bounded-above supremum of \(\alpha\)-psh functions is
   \(\alpha\)-psh. Increasing closure is equivalent to this property and is
   not part of the definition of psh.

---

## D. Allowed inputs for the unconditional branch

The solver may use only the following mathematical inputs, plus elementary
topology, convexity, commutative algebra, and projective geometry proved in
full in the response.

1. BJ22, Definition 4.1 and Theorem 4.5: minimal FS definition and
   decreasing closure with varying numerical classes.
2. BJ22, Theorem 4.7: finite maxima, sums, positive scalar multiplication,
   addition of constants in the nonhomogeneous class, and pullback, with all
   stated hypotheses. A zero coefficient means omission; never form
   \(0\cdot(-\infty)\).
3. BJ22, Theorem 4.15 and Corollary 6.17: decreasing homogeneous FS
   regularization.
4. BJ22, Theorem 4.22 and Corollary 4.23: divisorial comparison and
   determination.
5. BJ22, Lemma 2.23: stagewise FS division on a normal variety.
6. The strict-room result: if \(\psi\le t_0\ell_E\) for some \(t_0>1\),
   then the target conclusion holds by a fixed-divisor decreasing
   regularization.
7. Normal-domain facts: codimension-one divisibility of a rational section
   by an effective Cartier divisor implies regular divisibility; a
   noetherian normal domain is the intersection of its height-one DVR
   localizations.
8. Compactness of \(X^{\mathrm{an}}\), Dini's lemma for decreasing nets in
   its valid semicontinuity form, and density of \(X^{\mathrm{div}}\).
9. Standard facts about rational line bundles, canonical divisor sections,
   and the openness of the ample cone.

If another result is needed, state it as a separate lemma and prove it from
these inputs. Do not silently upgrade convergence to monotone convergence.

---

## E. Forbidden circular inputs for the unconditional branch

1. BJ22, Theorem 6.21 itself, or any restatement of it.
2. BJ22, Theorem 6.31, or the arbitrary-psh Siu decomposition derived from
   Theorem 6.21.
3. The envelope property, BJ22, Theorem 5.11 increasing closure, compactness
   of normalized psh spaces derived from EP, or the final envelope theorem
   for unibranch or normal varieties.
4. Any theorem in the supplied envelope manuscript whose proof uses
   homogeneous Siu division, including homogeneous birational reflection,
   carrier reflection, finite normal descent, alteration descent, and the
   final envelope theorem.
5. The converse Cartier or nef b-divisor correspondences in BJ22, Theorems
   6.35 and 6.40, or monotone nef-b-divisor approximation when its cited
   proof uses Theorem 6.21 or EP.
6. Boucksom--Jonsson, *Non-Archimedean Green's functions and Zariski
   decompositions*, Proposition 17 in the unconditional branch: its general
   step explicitly invokes the envelope property. It is allowed only as a
   cross-check for the conditional branch.
7. Any resolution or alteration argument unless every descent step is
   proved independently without using an item above.
8. Treating an arbitrary pointwise limit, or the family
   \(\psi_i-t_i\ell_E\), as psh without proving it is decreasing or
   providing another allowed closure theorem.
9. Subtracting \(\ell_E\) at a semivaluation supported in \(E\).
10. The author's arXiv:1710.09731 Deligne-pairing paper, in any form.

---

## F. Exact source obstruction

Suppose

\[
 \psi_i\searrow\psi,\quad
 \psi_i\in\mathcal H_{\mathrm{hom}}(L_i),\quad
 c_1(L_i)\to\theta,
\]

and choose \(t_i\to1\) with
\(\sup_{K_E}\psi_i\le-t_i\). Stagewise division gives

\[
 \rho_i=\psi_i-t_i\ell_E
 \in\mathcal H_{\mathrm{hom}}(L_i-t_iE).
\]

For \(j\ge i\), the residual order on \(K_E\) is equivalent to

\[
 \rho_j\le\rho_i
 \quad\Longleftrightarrow\quad
 t_j-t_i\le\inf_{K_E}(\psi_i-\psi_j).
\]

The printed proof asserts residual monotonicity from monotonicity of
\((\psi_i)\) alone. Audit this assertion.

---

## G. Counterexample candidate to the proof inference

### COUNTEREXAMPLE-CANDIDATE

Let \(X=\mathbf P^1_k\), let \(p\in X(k)\), set \(E=p\), and write
\(\ell=\log|s_E|\le0\). For \(n\ge2\), define

\[
 c_n=1-\frac1{2n},\qquad
 t_n=1-\frac1n,\qquad
 \psi_n=c_n\ell.
\]

Then
\(\psi_n\in\mathcal H_{\mathrm{hom}}(c_nE)\),
\(c_n[E]\to[E]\), and \(\psi_n\searrow\ell\). Also
\(c_n\ge t_n\), hence \(\psi_n\le t_n\ell\), and \(t_n\uparrow1\).
But

\[
 \rho_n=\psi_n-t_n\ell=\frac1{2n}\ell
\]

is strictly increasing at every divisorial valuation \(v\) with \(v(E)>0\).
Equivalently, on \(K_E\),

\[
 t_{n+1}-t_n=\frac1{n(n+1)}
 >\frac1{2n(n+1)}
 =\inf_{K_E}(\psi_n-\psi_{n+1}).
\]

Thus the source hypotheses do not imply that the residuals decrease. The
target theorem itself remains true in this example, since its residual is
\(0\in\operatorname{PSH}_{\mathrm{hom}}(0)\).

### END-COUNTEREXAMPLE-CANDIDATE

Required audit: check membership in the exact homogeneous FS classes, all
inequality directions, and the last arithmetic identity. State explicitly
that this refutes only the proof inference.

---

## H. Conditional repair candidate

### CONDITIONAL-REPAIR-STATEMENT

Use the hypotheses of TARGET-STATEMENT and fix an ample class \(\omega\).
Set \(\alpha=\theta-[E]\). Assume there exists a sequence
\(\varepsilon_m\downarrow0\) such that every class
\(\alpha+\varepsilon_m\omega\) has the envelope property by a proof that is
independent of TARGET-STATEMENT and of all forbidden inputs depending on it.
Then the conclusion of TARGET-STATEMENT holds.

### END-CONDITIONAL-REPAIR-STATEMENT

### CONDITIONAL-REPAIR-PROOF

The reverse implication and uniqueness are immediate from homogeneous
normalization and divisorial determination. Assume \(\psi\le\ell_E\).
For every rational \(0<t<1\), the strict-room theorem applied to the
divisor \(tE\) gives

\[
 u_t:=\psi-t\ell_E
 \in\operatorname{PSH}_{\mathrm{hom}}(X,\theta-t[E]),
\]

because \(\psi\le\ell_E=t^{-1}\ell_{tE}\) and \(t^{-1}>1\). This is an
identity on \(X^{\mathrm{div}}\); its psh extension is supplied by the
strict-room theorem, so no difference of infinities is formed.

Fix \(m\). By openness of the ample cone, for all rational \(t<1\)
sufficiently close to \(1\),

\[
 \beta_{m,t}:=\varepsilon_m\omega-(1-t)[E]
\]

is ample. Since the zero function is \(\beta_{m,t}\)-psh, addition gives

\[
 u_t\in\operatorname{PSH}_{\mathrm{hom}}
 (X,\theta-t[E]+\beta_{m,t})
 =\operatorname{PSH}_{\mathrm{hom}}
 (X,\alpha+\varepsilon_m\omega).
\]

These functions are bounded above by \(0\), and on
\(X^{\mathrm{div}}\) they increase as \(t\uparrow1\) to

\[
                        u(v)=\psi(v)+v(E).
\]

The assumed envelope property gives

\[
 U_m:=\left(\sup_{t<1}u_t\right)^*
 \in\operatorname{PSH}
 (X,\alpha+\varepsilon_m\omega).
\]

BJ22, Theorem 5.6 implies that usc regularization does not change the
supremum at a divisorial point, hence
\(U_m|_{X^{\mathrm{div}}}=u\). The trace \(u\) is homogeneous. Since the
scaling action preserves the psh class,
\(s\mathbin{\cdot}U_m\) is psh and has the same divisorial trace as \(U_m\)
for every \(s>0\); divisorial determination therefore shows that \(U_m\)
is homogeneous. For \(m,m'\), BJ22, Theorem 4.22 applied
first to \(U_m\) with usc obstacle \(U_{m'}\), and then in the reverse
direction, gives \(U_m=U_{m'}\) on \(X^{\mathrm{an}}\). Denote the common
function by \(U\). Then

\[
 U\in\operatorname{PSH}_{\mathrm{hom}}
 (X,\alpha+\varepsilon_m\omega)
 \quad\text{for every }m.
\]

Closedness with respect to the numerical class, BJ22, Theorem 4.5, yields
\(U\in\operatorname{PSH}_{\mathrm{hom}}(X,\alpha)\). On
\(X^{\mathrm{div}}\), one has \(\psi=\ell_E+U\). Both sides are usc and
\(\theta\)-psh; divisorial determination gives the identity on all of
\(X^{\mathrm{an}}\). At points supported in \(E\), this is the identity
\(-\infty=-\infty+U\), not a subtraction.

### END-CONDITIONAL-REPAIR-PROOF

Audit every use of Theorems 4.5, 4.22, and 5.6. Determine whether the
envelope assumption can be weakened further without becoming circular.

Literature cross-check: the mechanism should agree with
Boucksom--Jonsson, *Non-Archimedean Green's functions and Zariski
decompositions*, Proposition 17. Under smooth characteristic-zero
hypotheses their later result handles effective real divisors. The
Boucksom--Jonsson addendum, Theorem A provides the independent envelope
input when \(X\) is smooth and either \(\operatorname{char}k=0\) or
\(\dim X\le2\).

---

## I. Preferred unconditional target lemma

Try first to prove or disprove the following face-closure assertion directly
from Sections C and D.

### FIXED-DIVISOR-FACE

For every normal integral projective \(X\), every effective rational
Cartier divisor \(E\), and every
\(\theta\in N^1(X)_{\mathbf R}\), multiplication by the canonical section
induces a bijection

\[
 \operatorname{PSH}_{\mathrm{hom}}(X,\theta-[E])
 \longrightarrow
 \{\psi\in\operatorname{PSH}_{\mathrm{hom}}(X,\theta):
   \psi\le\ell_E\},
 \qquad u\longmapsto u+\ell_E.
\]

### END-FIXED-DIVISOR-FACE

At the FS level this is Lemma 2.23. The hard point is surjectivity after the
minimal decreasing closure. A valid proof must construct an actual
decreasing FS net for the residual, or prove a new closure principle from
the allowed inputs. Pointwise convergence without monotonicity is
insufficient.

---

## J. Adversarial checklist

Before returning VERIFIED, answer every item.

1. Does the argument work for nets, not only sequences?
2. Are rational denominators of \(L_i\), \(E\), and \(t_iE\)
   synchronized?
3. Is every stagewise quotient a regular section by normality?
4. Is every invoked limit decreasing, unless an envelope property is
   explicitly assumed in the conditional branch?
5. At \(v(E)=0\), is residual order checked separately from the slice
   \(K_E\)?
6. At \(v(E)=+\infty\), is no expression \(\psi-\ell_E\) formed?
7. Does the proof accidentally assume resolution in positive
   characteristic?
8. Does any descent theorem used depend on homogeneous Siu division?
9. Does a b-divisor correspondence used in the proof depend on Theorem 6.21
   or on EP?
10. Does the proof use countable cofinality of the model or regularization
    system?
11. Does the proof handle classes on the boundary of the pseudoeffective
    cone?
12. Does the proposed counterexample refute the theorem, or only
    monotonicity?
13. Test \(E=0\), \(X=\mathbf P^1\), \(\psi=\ell_E\), and the explicit
    family in Section G.
14. Confirm that arXiv:1710.09731 and all Deligne-pairing arguments are
    absent.

---

## K. Required output schema

Return exactly these sections.

1. SOURCE-AUDIT-VERDICT: VALID or GAP, followed by a complete proof.
2. COUNTEREXAMPLE-AUDIT: VALID, INVALID, or NEEDS-CORRECTION, followed by
   the checked computation.
3. CONDITIONAL-REPAIR-VERDICT: VERIFIED, INVALID, or NEEDS-CORRECTION,
   followed by a line-by-line dependency audit.
4. UNCONDITIONAL-VERDICT: VERIFIED, COUNTEREXAMPLE, or OPEN-AFTER-ATTEMPT.
5. EXACT-STATEMENT: the strongest theorem actually established, with all
   hypotheses.
6. EXACT-PROOF or EXACT-COUNTEREXAMPLE: a self-contained argument.
7. DEPENDENCY-DAG: every non-elementary input and whether it depends on EP
   or Theorem 6.21.
8. GENERALITY: characteristic, singularities, Cartier coefficients, and
   dimension.
9. FAILURE-MODES-CHECKED: responses to all fourteen items in Section J.
10. NOVELTY-STATUS: distinguish literature reconstruction, correction of a
    proof step, and any genuinely new lemma. Do not make a priority claim.

If the unconditional verdict is OPEN-AFTER-ATTEMPT, identify the first exact
missing implication and preserve TARGET-STATEMENT as unverified in its full
generality.

---

## L. Hashing and receipt instructions

1. Work in UTF-8 with LF line endings and no trailing spaces.
2. Preserve the exact TARGET-STATEMENT, COUNTEREXAMPLE-CANDIDATE,
   CONDITIONAL-REPAIR-STATEMENT, and CONDITIONAL-REPAIR-PROOF blocks in the
   solver input. Do not silently normalize notation.
3. After the solver returns, save the raw response unchanged.
4. Extract each returned section from its heading through the byte
   immediately before the next heading. Include one terminal LF.
5. Compute SHA-256 for:
   - the full raw solver response;
   - EXACT-STATEMENT;
   - EXACT-PROOF or EXACT-COUNTEREXAMPLE;
   - the concatenation of EXACT-STATEMENT, one LF, and the proof or
     counterexample;
   - DEPENDENCY-DAG;
   - the exact Chapter 35 theorem-and-proof block proposed for promotion, if
     any;
   - the entire Chapter 35 file after integration, if any.
6. Record model, reasoning effort, launch timestamp, completion timestamp,
   receipt or job identifier, all hashes, and the exact source-file hashes
   in the verification ledger.
7. Re-run Rethlas if any mathematical byte in a verified block changes.
   Typography-only reflow outside the hashed block does not preserve a
   whole-file receipt.
8. A GAP verdict for the source proof is not a verification of
   TARGET-STATEMENT. A VERIFIED conditional proof is not an unconditional
   receipt. Ledger entries must preserve this distinction.

Local source hashes supplied with this packet:

- BJ22 PDF:
  8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52;
- BJ22 extracted text:
  af5a9b9d62570a37d9ad11d139e99353e8b50f1f1c55557fbfcf2cb37cca0c8f;
- Chapter 35 at the time the source audit was run:
  45d39f528be1a0092be409e24f3aec575256ce10d6782dec831ff12e96a34851.

The Chapter 35 hash is observational and may be superseded by concurrent
proof-depth editing. Recompute it immediately before launch.
