# Hostile audit of the repaired proof packet for Xia Conjecture 8.8

Date: 2026-08-24

Audited packet:
`manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`

Author-supplied comparison source:
`/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/main.tex`

Current manuscript comparison target:
`manuscript/parts/part5/ch55_okounkov_dh.tex`

## 1. Verdict

**Mathematical verdict: conditional pass.** I found no counterexample to the
repaired equality and no remaining fatal gap in the proof architecture. The two
live repairs made during this audit are valid:

1. the one-dimensional-factor branch correctly disposes of the degenerate case
   before the boundary-incidence argument in the toric component; and
2. the proof of the body inclusion (19) by multiplication with the canonical
   section is valid and avoids any possible ambiguity about applying a Minkowski
   theorem to the effective summand.

The proof is therefore a credible integration candidate **conditional on the six
imported packages stated at the beginning of the packet**. The new ingredients
that actually needed hostile checking—the finite multigraded degeneration, the
movable upper bound, the uniform convex sandwich, the pointwise completion of the
\(d_S\)-sandwich, and valuation-uniform convergence—survive the checks below.

**Verification-receipt verdict: not yet unconditional.** Two documentary issues
remain:

- the assertion that the six numbered items are the only imported assertions is
  literally false: the proof also uses standard but nontrivial algebraic and
  convex-geometric facts, and imported item 4 is not sourced within the three
  primary documents permitted for this audit;
- current Chapter 55 has an internal status contradiction and understates the
  valuation scope of the official book's algebraic Minkowski theorem.

Neither issue refutes the proof. They should be repaired before the packet is
called an exact source-closed verification receipt.

## 2. Exact audit snapshot and exclusion firewall

At the start of the audit, the supplied `main.tex` had SHA-256

```text
9a039a5070d2f82ae258d56eec22c8cb998c473b4234158ac1ddd5ebbef78298
```

which agrees with the digest recorded in the packet. The repaired packet changed
during the audit. After the latest observed change its SHA-256 was

```text
de4138a4f1e54e74eccf8528dc411283eb05448df16b60a21218cc09cd7d54dc
```

The primary documents actually checked were:

1. Mingchen Xia, *Singularities in global pluripotential theory—Lectures at
   Zhejiang University*, official author-hosted PDF
   (`https://mingchenxia.github.io/Lectures/SGPT_final.pdf`), marked “Updated on
   July 18, 2026,” SHA-256
   `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`;
2. Robert Wilms, *Intersection numbers as mixed volumes of Newton–Okounkov
   bodies*, arXiv:2502.18441v3, SHA-256
   `7ba48e15de6953c7a19accf5e72ab17d482ad9370b9c180c2b2b8feefead060c`;
3. Kiumars Kaveh and Christopher Manon, *Khovanskii bases, higher rank
   valuations, and tropical geometry*, arXiv:1610.00298v4, SHA-256
   `29336df84b61fe8e514ea6cb709a70e810b2fc4cdf51879237c5e00212c30ec4`.

The author-supplied bibliography identifies the official book as dated 29 June
2026, but the live official PDF is a later 18 July 2026 version. The packet should
identify the exact version or digest on which its imports rely.

**Exclusion rule observed.** The prohibited source named in the audit request was
not opened, cited, quoted, or used as authority in this audit. Current Chapter 55
was used only as a manuscript comparison target, not as authority for any
mathematical step that it attributes elsewhere. Historical attributions in the official book were not used
as premises; only the proofs and statements appearing in the permitted official
book itself were checked.

## 3. Findings by severity

### 3.1 No fatal finding

I tried to break each of the requested mechanisms. No attempted counterexample
survived the repaired hypotheses. In particular:

- no Khovanskii-basis equality \(Q=J\) is needed; the inclusion \(Q\subseteq J\)
  gives a toric top component and the inequality in the correct direction;
- valuation bodies can become arbitrarily sheared as the valuation varies, but
  the volume bound on the Minkowski sum supplies exactly the affine compactness
  that the John-ellipsoid argument needs;
- the extra comparisons \(\eta_j\le u\le\psi_j\) do not follow from mere
  \(d_S\)-convergence, but the repaired tail/order-closure argument proves them;
- the flag in Wilms's theorem may depend on \(\varepsilon\), which is harmless
  because the theorem takes a supremum rather than claiming attainment by a
  fixed valuation.

### 3.2 Source-closure issue: imported item 4 is not verified by the three permitted primary documents

Packet lines 44–45 say that no assertion beyond the six numbered packages is
imported. Even if this is read as “no theorem-level input beyond the list,” item 4
itself—the mixed nef-approximation inequality for movable products, equality of
movable and ordinary products for nef classes, and the identification using
minimal singularities—is not a result I located in the three permitted primary
documents.

The author-supplied TeX cites other literature for these facts; current Chapter 55
also cites other literature for the minimal-singularity specialization. Those
sources were deliberately not used here under the audit restriction.

**Effect.** This is not a mathematical gap if item 4 is explicitly accepted as an
axiom/import. It prevents the packet from being described as source-closed under
only the three named primary documents.

**Minimal repair.** Replace

> “The proof below is conditional only on the following established inputs. No
> other assertion is imported.”

by

> “The proof is conditional on the following theorem-level inputs, together with
> the standard algebraic and convex-geometric facts used explicitly below.”

Then either (a) retain item 4 as an explicitly accepted input without claiming it
was verified in the three-source audit, or (b) provide a separately authorized
primary source and exact theorem numbers. The last minimal-singularity paragraph
can also be labeled a corollary requiring the final sentence of item 4; it is not
needed for the metric theorem itself.

### 3.3 Source-closure issue: standard but nontrivial facts are used outside the numbered ledger

The proof additionally uses, among other facts:

- Abhyankar's inequality and the one-dimensional-leaf consequence;
- the multigraded Hilbert polynomial/fundamental-cycle dictionary;
- nonnegativity of degrees of globally generated divisors;
- Bernstein–Kushnirenko, John, and Blaschke;
- strict volume monotonicity for full-dimensional convex bodies;
- openness of the big cone and existence of effective \(\mathbb Q\)-representatives
  of big rational classes.

Most are completely standard and are used correctly. The issue is only the
absolute phrase “No other assertion is imported.” Imported item 6 does mention
Bernstein–Kushnirenko, but the others are not all listed.

### 3.4 A newly added bibliographic input falls outside the permitted source set

In the latest observed packet, imported item 3 adds a citation to Xia,
*Transcendental b-divisors*, Theorem 3.5, for identification with Cao's mixed
volume. That document is not one of the three primary sources permitted by the
audit request, so it was not opened or used here.

The citation is not logically needed in this packet: the theorem statement already
**defines** the mixed metric volume to be the mixed non-pluripolar product of the
\(\mathcal I\)-model envelopes, and every proof step uses that displayed definition.

**Minimal repair.** Delete the four-line attribution from the source-restricted
packet, or label it as an unverified bibliographic note outside the proof ledger.
No mathematical argument changes.

### 3.5 Current Chapter 55 has a status contradiction

Current Chapter 55, lines 811–818, says the conjecture is not marked proved or
closed. Lines 935–946 repeat that it is unverified and is not used. But lines
965–967 say:

> “the mixed-volume identity is an identity on the positive-volume locus only:
> it is a theorem there”

Those statements cannot all be current simultaneously. This is an editorial
finding only; the chapter was not edited.

**Minimal repair after the proof receives its intended verification status.** Pick
one status and make all three locations agree. Until then, replace “it is a theorem
there” by “the claimed identity is restricted to that locus.”

### 3.6 Current Chapter 55 understates the valuation scope of algebraic superadditivity

Chapter 55, lines 682–716, restricts its algebraic superadditivity proposition to
flag valuations and calls that restriction binding. In the official July 18 book,
Chapter 10.3 fixes an arbitrary surjective full-rank valuation, and Proposition
10.3.10 states the Minkowski inclusion in that setting. Proposition 10.3.8 gives
the order inclusion in the same setting. Thus the broader valuation scope used in
the repaired packet is supported by the permitted official book.

This does not damage the packet. It means Chapter 55 is more conservative than
the exact official-book statement and should not be used to narrow the packet's
scope.

## 4. Finite-level multigraded degeneration

### 4.1 One-dimensional leaves and the graded field

The step is correct. Surjectivity onto \(\mathbb Z^n_{\rm lex}\) gives rational rank
\(n\). Abhyankar's inequality forces the residue field to be algebraic over
\(\mathbb C\), hence equal to \(\mathbb C\). Each nonzero leaf is therefore
one-dimensional. Since every degree occurs, choosing \(u_\ell\) with
\(\nu(u_\ell)=e_\ell\) gives the multiplicative graded isomorphism

\[
\mathbb C[\mathbb Z^n]\simeq \operatorname{gr}_\nu F.
\]

Negative exponents are harmless because the source is a field. Rescaling the
chosen basis vectors to make their initial forms monomials is legitimate.

### 4.2 Exact Kaveh–Manon scope

Kaveh–Manon Lemma 2.16 says exactly that the matrix-weight initial ideal is
contained in the valuation initial ideal. Applied to the presentation by the
\(f_{ij}\), this is \(Q\subseteq J\), the direction used in the packet.

Kaveh–Manon Proposition 8.10 is stated for an arbitrary ideal
\(I\subset k[x]\) and an arbitrary rational matrix weight
\(M\in\mathbb Q^{r\times N}\). It supplies a rational scalar weight with the same
initial ideal. It therefore applies to the packet's multihomogeneous prime ideal.
Because each multidegree piece is finite dimensional and the scalar filtration
respects multidegree, equation (2) follows.

No finite Khovanskii basis is asserted or required. A hostile attempt to demand
\(Q=J\) would be attacking a stronger, unused statement.

### 4.3 Toric component and leading mixed degree

The exponent differences generating \(\mathbb Z^n\) makes the character-ring map
surjective, hence the torus map is a closed immersion. Thus \(Z\) is irreducible of
dimension \(n\). Since \(Q\subseteq J\), \(Z\subset Y_0\); equality of the diagonal
Hilbert polynomials gives \(\dim Y_0=n\), making \(Z\) a top-dimensional component.
The top cycle has positive generic multiplicities, and each globally generated
\(H_i\) has nonnegative degree on every component. The inequality (3) has the
correct direction.

For maximum source precision, one may add that irrelevant-ideal torsion does not
change the eventual multigraded Hilbert polynomial and that
\(\mathcal O(1,\ldots,1)\) is ample on the product. This is explanatory, not a gap.

### 4.4 Degenerate factor and boundary incidence

The live repair is necessary for the stated incidence count and is correct. If
some \(W_i\) is one-dimensional, \(P_i\) is a point, so the mixed volume with
\(P_i\) as one entry is zero. The right-hand side of (1) is nonnegative (indeed
the corresponding hyperplane class is zero), so (1) follows immediately.

An exact degenerate test is

\[
F=\mathbb C(x,y),\qquad W_1=\langle1\rangle,\qquad
W_2=\langle1,x,y\rangle
\]

with the lowest-term lexicographic valuation. The combined differences generate
\(\mathbb Z^2\), and the joint map is birational, but there is no positive-dimensional
hyperplane parameter in the first \(\mathbb P^0\)-factor. The original uniform
“codimension one per factor” sentence does not describe this case. The repaired
zero-mixed-volume branch does.

Once every \(\dim W_i\ge2\), a fixed boundary point imposes one independent linear
condition on each factor's hyperplane parameter. The incidence variety has
dimension at most

\[
\dim(\text{hyperplane parameter space})-1,
\]

so a general tuple avoids the boundary. Bernstein–Kushnirenko then computes the
intersection on the dense torus with the stated \(n!\) normalization.

## 5. Movable upper bound

The passage from the finite-level estimate to (4) is correct conditional on
imported item 4.

For a big complete series, the official book's proof of Proposition 10.3.1
constructs, in one degree, values differing by every standard basis vector. If
those sections occur in degree \(p_0\), then after replacing \(p_0\) by a common
multiple \(p=rp_0\), the sections

\[
s_0^r,\qquad s_js_0^{r-1}
\]

still differ by \(e_j\). At degree \(k=mp\), the analogous products preserve those
unit differences. This supplies the lattice hypothesis at every level in the
chosen arithmetic progression.

The claim that the complete maps at levels divisible by \(p\) are birational is
also valid: the complete system at level \(mp\) contains the symmetric-power
subsystem giving the Veronese of a birational level-\(p\) map.

On a common resolution,

\[
\mu_k^*(kD_i)=M_{i,k}+F_{i,k}
\]

with \(M_{i,k}\) basepoint free. The joint morphism is birational onto \(Y_k\), so
projection gives the mixed degree \(M_{1,k}\cdots M_{n,k}\). The nef approximation
has the correct direction, and dividing by \(k^n\) is correct because the
finite-level polytopes are unnormalized. Official-book Proposition 10.3.4 gives
Hausdorff convergence along the arithmetic progression as well.

**Minimal clarity repair.** Packet lines 212–217 compress the two power arguments
above into one sentence. Adding the displayed \(s_0^r,s_js_0^{r-1}\) construction
would make the lattice claim locally checkable, but no new hypothesis is needed.

## 6. Corrected convex sandwich

The corrected lemma is valid, and all three numerical hypotheses are doing real
work.

After independent translations of the \(i\)-quadruples, \(0\in B_{i,j}\), so each
body is contained in \(S_j=\sum_iB_{i,j}\). The determinant bounds in (9) have the
correct directions:

\[
\frac{\kappa_n}{M}\le |\det L_j|\le
\frac{n^n\kappa_n}{v}.
\]

The lower bound keeps transformed inner volumes positive and transfers mixed-volume
convergence back; the upper bound makes transformed volume gaps tend to zero.
Blaschke selection applies simultaneously to the finite family of \(4n\) bodies.
At the limit, full dimensionality plus equal volume and inclusion forces equality.

Three exact failure tests show why the repaired statement must not be weakened:

1. **Omit the bounds on \(D_j\).** In dimension one take
   \(A_j=B_j=C_j=[0,1]\) and \(D_j=[0,j]\). All data involving only
   \(A,B,C\) are perfect, but \(|V(C_j)-V(D_j)|=j-1\).
2. **Omit the positive lower volume.** In dimension two take
   \(A_1=C_1=\{0\}\), \(D_1=B_1=[0,e_1]\), and
   \(A_2=B_2=C_2=D_2=[0,e_2]\). All two-dimensional inner/outer volume gaps
   are zero and the sum lies in the unit square, but
   \(V(C_1,C_2)=0\) while \(V(D_1,D_2)>0\).
3. **Omit the bound on \(\lambda_2(B_1+B_2)\).** Let
   \(A_1=B_1=C_1=D_1=[0,j]\times[0,j^{-1}]\),
   \(A_2=C_2=[0,j^{-1}]\times[0,j]\), and
   \(B_2=D_2=[0,j^{-1}]\times[0,j+1]\). The individual outer-minus-inner
   area tends to zero, but the mixed-volume change grows like \(j/2\).

The packet has all four inclusions and all three numerical hypotheses, so none of
these counterexamples applies.

## 7. Pointwise completion of the \(d_S\)-sandwich

The repaired argument is correct and matches the exact scope of official-book
Proposition 6.2.5, which says that the \(P\)-preorder is closed under simultaneous
\(d_S\)-limits.

For a fixed \(j\), monotonicity gives

\[
\eta_j\le\eta_k\le u_k\quad(k\ge j).
\]

Apply order closure to the constant net \(\eta_j\) and the tail \(u_k\to u\).
This yields \(\eta_j\preceq_Pu\). Since both are normalized model potentials, this
is the pointwise inequality \(\eta_j\le u\). The upper argument is identical using
\(u_k\le\psi_k\le\psi_j\).

The extra explanation of model-projecting the upper sequence is also valid:
monotonicity of \(P_\theta\) preserves decrease, model projection preserves the
\(d_S\)-class, and \(u_j=P_\theta[u_j]\le P_\theta[\widetilde\psi_j]\).
The lower sequence in the official sandwich construction is already model after
discarding finitely many terms.

The normalization/modelness is essential to turn \(P\)-order into a pointwise
order. Mere \(d_S\)-convergence cannot compare chosen representatives: additive
constants have zero \(d_S\)-distance. The packet does not make that invalid
inference.

The finite diagonal subsequence argument is legitimate.

## 8. Valuation-uniform convergence

The proof of (12) is sound.

### 8.1 Four inclusions

The repaired pointwise sandwiches give

\[
\eta_{i,j}\le \varphi_{i,j},\varphi_i\le\psi_{i,j}.
\]

Pointwise order implies the corresponding \(\mathcal I\)-preorder, so official-book
Proposition 10.3.8 gives all four convex inclusions required in (6). There is no
remaining unsupported inclusion involving the limit potential.

### 8.2 Uniform numerical bounds

The diagonal body-volume formula removes the varying valuation from all scalar
volume bounds. Official-book Corollary 7.3.1 gives convergence of the Cao volumes.
Since there are finitely many \(i\), after discarding a finite initial segment one
common \(v>0\) works.

Repeated official-book Proposition 10.3.10 gives

\[
\sum_iB_{i,j}\subseteq
\Delta_{\nu_j}\!\left(\sum_i\theta_i,\sum_i\psi_{i,j}\right),
\]

and Proposition 10.3.8 places this in the complete-series body of
\(L_1\otimes\cdots\otimes L_n\). Its Euclidean volume is fixed independently of
\(j\) and \(\nu_j\). This is precisely the uniform tightness missing from
fixed-valuation Hausdorff continuity.

**Minimal clarity repair.** Say explicitly that, after deleting finitely many
indices, every outer, inner, and tensor-sum body occurring here is on the positive
volume locus. This follows from \(d_S\)-mass continuity and positivity of the
limiting masses, so it is not a new hypothesis.

### 8.3 Passage to suprema

If uniform convergence failed, the choice of \(\nu_j\) is legitimate after shrinking
the failure constant if the supremum is not attained. The final inequality

\[
|\sup f_j-\sup f|\le\sup|f_j-f|
\]

is exactly what is needed. The argument never claims valuation-uniform Hausdorff
convergence of the bodies.

## 9. Analytic-singularity reduction

### 9.1 Resolution and rationality

The packet repairs the source's type mismatch. On the common log resolution,

\[
\alpha_i=\{R_i\}=\pi^*c_1(L_i)-\{D_i\}\in N^1(Y)_\mathbb Q.
\]

The official book makes \(\alpha_i\) nef, and \(\alpha_i^n>0\) makes it big.
Official-book Remark 10.3.1, equation (10.22), then applies to the big rational
divisor class and gives the translation formula (15). Thus applying the algebraic
movable upper bound is type-correct.

The mixed non-pluripolar product on \(X\) equals the Bedford–Taylor product of the
bounded residual currents on \(Y\), hence the cohomological intersection
\(\alpha_1\cdots\alpha_n\). The packet's equation (14) has the correct
normalization.

### 9.2 Wilms approximation

Wilms Theorem 1.1 in v3 has exactly the packet's scope: ample
\(\mathbb Q\)-line bundles on an irreducible projective \(n\)-fold, one admissible
flag for the full tuple, and

\[
(A_1\cdots A_n)=n!V(\Delta(A_1),\ldots,\Delta(A_n)).
\]

For nef and big \(\alpha_i\), choose common rational \(c\) with
\(c\alpha_i-H\) big. A big rational class admits an effective rational
representative \(E_i\). The identity (17) is algebraically correct, and
\(\beta_i=\alpha_i+\varepsilon H\) is ample for rational \(\varepsilon>0\).

The live repair of (19) is valid. After clearing denominators, multiplication by
the canonical section of the effective summand injects the section values of the
scaled \(\beta_i\)-series into those of the actual divisor \(A_i\). Numerical
invariance identifies \(\Delta(A_i)\) with \(\Delta(\alpha_i)\). The resulting point
\(\nu(E_i)\) is only a translation, so the lower mixed-volume estimate carries the
factor \((1+c\varepsilon)^{-n}\). Letting rational \(\varepsilon\downarrow0\) is
legitimate.

No fixed flag as \(\varepsilon\to0\) is needed.

## 10. \(\mathcal I\)-envelope reduction and general metrics

The positive-Cao-volume versus positive-raw-mass distinction is handled correctly
in the repaired packet.

Set \(u_i=P_{\theta_i}[\varphi_i]_{\mathcal I}\). Official-book Proposition 3.2.6
gives \(u_i\sim_{\mathcal I}\varphi_i\) and shows that the \(\mathcal I\)-envelope
is a model potential. Equivalently, the packet's direct maximality argument is
valid after normalization. Therefore:

- the partial body is unchanged;
- the left side in the theorem is, by definition, the mixed non-pluripolar product
  of these \(u_i\);
- positive Cao volume is exactly positive raw mass for \(u_i\).

An \(\mathcal I\)-model potential is \(\mathcal I\)-good. Official-book Theorem
7.1.1 supplies analytic-singularity \(d_S\)-approximants whose currents are Kähler.
The analytic case applies at each level. Official-book Theorem 6.2.1 gives
continuity of the mixed non-pluripolar products, while the newly proved uniform
statement (12) gives convergence of the suprema. The limit in (20) is therefore
valid.

This reduction also blocks the familiar false inference

\[
\text{positive Cao volume}\Longrightarrow\text{positive raw mass of the original
potential}.
\]

The packet never needs that implication: it first replaces the original potential
by its \(\mathcal I\)-model representative.

## 11. Comparison with the author-supplied source

The repaired packet materially improves the supplied TeX in all places needed by
the proof:

1. it proves the two pointwise limit comparisons rather than attributing them in
   one sentence to order closure/mass continuity;
2. it states the simultaneous finite subsequence extraction;
3. it makes the four inclusions in the convex sandwich logically visible;
4. it records \(\alpha_i\in N^1(Y)_\mathbb Q\) before using algebraic bodies;
5. it treats the \(\mathbb P^0\)-factor before the boundary incidence count;
6. it gives a section-theoretic proof of (19);
7. it proves that the \(\mathcal I\)-model representative is also a model
   representative and has positive mass.

The supplied source remains useful as provenance, but the repaired packet—not the
terse corresponding sentences in `main.tex`—is the proof object that survived this
audit.

## 12. Final recommendation

Accept the packet as a **conditional mathematical proof** after making the following
small source/status repairs:

1. record the exact July 18, 2026 official-book version or its digest;
2. weaken the “no other assertion is imported” sentence and label imported item 4
   as an accepted external input unless a separately authorized primary citation
   is added;
3. remove or quarantine the newly added citation outside the permitted
   three-source audit boundary;
4. state explicitly in the uniformity proof that a finite initial segment is
   discarded so every auxiliary body is defined on the positive-volume locus;
5. synchronize Chapter 55's status sentences and reconsider its unnecessary
   flag-only restriction after a verification receipt is issued.

No change to the theorem statement, no additional geometric hypothesis, and no
change to the supremum over all surjective lexicographic valuations is required.
