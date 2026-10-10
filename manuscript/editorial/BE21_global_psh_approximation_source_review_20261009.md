# Global Fubini–Study approximation and field-extension descent: source audit

Date: 9 October 2026. Controlling primary source: Boucksom–Eriksson,
*Spaces of norms, determinant of cohomology and Fekete points in
non-Archimedean geometry*, Advances in Mathematics 378 (2021), 107501.
The cached published PDF has 125 physical pages, including its cover.
This checkpoint actually reads physical pages 60–71 with complete text,
six individually displayed matching images and sequential notes/receipts.
This includes all of Section 7 and its beginning/end seams. Seven pages
overlap the three previous related selections; only 61, 65, 66, 67 and 68
are new distinct pages. The four-checkpoint union is 58 of 125 pages,
with 67 unread in those checkpoints. This is not a whole-article reading.

The first view-preparation helper expected an incorrect heading on the
wrong page and failed before creating images, selected text or a source
directory. Its helper and zero-credit failure record are frozen. Fresh v2
uses statement guards and includes the actual Section 7 beginning. No
failed preparation is counted as reading. Seven elementary diagnostic
families pass; they are finite exact fixtures and ordinary mathematical
checks, rather than independent-model certification of general theorems.

## Three positivity categories

Section 7 has a projective scheme over a complete valued field as its
standing domain. In the non-Archimedean case, Definition 7.2 uses a
semiample rational line bundle and a decreasing **net** of global
Fubini–Study metrics. It defines global psh in that class; it does not
identify every locally CLD-psh weight with a global metric in this class.
Stein-factor and reduction invariance have separate earlier inputs.

Model nefness tests degrees on projective special-fibre curves. A nef
metric in Definition 7.7 is a uniform limit of nef model metrics.
Theorem 7.8 identifies continuous global psh and nef metrics when the
field is nontrivially valued and the rational line bundle is **ample**.
One direction uses pure FS/semiample model equivalence. The other uses
an ample model of the same generic line bundle on a dominating projective
model, then rational perturbations of the pulled-back nef model. Its
printed $\mathcal H$ denotes the ample model previously named
$\mathcal A$; it is not an additional unspecified polarization. Relative
ampleness, model domination and model-metric invariance remain cited
classical inputs. Remark 7.10 expects the merely semiample extension;
it records missing nef-model descent to Stein factorization, potentially
via a relative local Hodge-index result. It does not prove that extension.

Smooth semipositivity in Definition 7.11 is a curvature condition.
Psh-regularizability in Definition 7.13 is a decreasing smooth-semipositive
net presentation. Theorem 7.14 proves that global FS-psh implies this
regularizability for a semiample rational line bundle. The reverse
identification of all these categories is not asserted by that theorem.
The cited CLD smooth regularized maximum uses a finite generating family
without common zeros; ordinary log-of-sum-of-squares at a non-Archimedean
rational zero is not substituted for that input.

## Decreasing nets and the corrected sequence argument

Lemma 7.4 flattens nested decreasing approximations using positive
constant margins and compactness. Its literal order on triples is a
preorder if different triples represent the same function; quotienting
equal representations gives a directed partially ordered set. The
pointwise limit and directedness argument are unchanged. A general net
is not replaced by a sequence without justification.

For continuous global psh metrics, Dini's lemma gives uniform convergence
of the defining decreasing net, so Corollary 7.6 identifies their class
with the uniform closure of the allowed FS metrics. The converse's
printed claim about shifting every prescribed uniformly convergent
sequence is too strong. On two reduced projective points, take

$$
u_i=\left(\frac{(-1)^i}{i},-\frac{(-1)^i}{i}\right).
$$

These are FS metrics on the trivial line bundle and converge uniformly
to zero. If $u_i+c_i$ were decreasing, then

$$
c_i-c_{i+1}\ge\frac1i+\frac1{i+1}.
$$

The summed lower bound diverges, so $c_i\to0$ is impossible. This direct
diagnostic was already recorded in the norm-dependency checkpoint and
is rechecked here; it does not refute uniform closure. Choose instead
a subsequence with $\|u_k-u\|_\infty\le2^{-k}$ and put
$c_k=3\cdot2^{-k}$. Then

$$
c_k-c_{k+1}=2^{-k}+2^{-(k+1)}
$$

dominates the positive pointwise increment. The shifted subsequence
decreases to the same limit. The same elementary correction obtains a
decreasing smooth presentation from the uniform regularized maxima in
Theorem 7.14; Lemma 7.4 handles subsequent nested nets.

## The norm FS operator and its two extension statements

Definition 7.15 takes a norm on a basepoint-free subspace $V$ of global
sections. In the non-Archimedean diagonal case it gives

$$
\operatorname{FS}(\alpha)=
\max_i\{\log|s_i|-\log\alpha(s_i)\}.
$$

Theorem 7.16 proves continuity and global pshness for every finite
norm by diagonalizable norm density and the estimate

$$
\|\operatorname{FS}(\alpha)-\operatorname{FS}(\beta)\|_\infty
\le d_\infty(\alpha,\beta).
$$

It does not assert that every norm is diagonalizable. Lemma 7.20 gives
**exact** non-Archimedean FS pullback for the scalar-extended original
norm. The printed orthogonal basis of $H^0(L)$ in its proof must be a
basis of the specified $V$ when $V$ is proper. This differs from the
metric-induced norms on the entire extended section space, whose
comparison is the **asymptotic** Theorem 6.6. Confusing these statements
would discard the error that the final descent proof actually controls.

The printed Archimedean real-field evaluation step requires a separate
typing clarification. For the standard Euclidean norm on the real
sections $(X_0,X_1)$ of $\mathcal O(1)$ on $\mathbf P^1_{\mathbf R}$,
evaluation at $[1:i]$ has real-unit-ball supremum $1$, since
$|a+ib|^2=a^2+b^2$ for real $a,b$. The complex Hermitian-unit-ball
supremum is $\sqrt2$, attained at $(1,-i)/\sqrt2$. Thus the literal
equality of these two suprema, and the real-coefficient version of the
complex optimum in Lemma 7.17, are not arguments under literal real
sections. The intended conjugation-invariant convention can be typed
by complexifying before evaluation. This diagnoses the displayed step;
it does not refute an intended correctly typed FS theorem. The current
book's field-extension interface uses the explicit non-Archimedean max
proof. The earlier norm-complexification theory is not recursively
certified by this selection.

Definition 7.21 uses reduced sections, so nilpotent sections are not
silently assigned a nondegenerate analytic norm. Lemma 7.23 has the
correct directions: $\operatorname{FS}(\phi)\le\phi$, fixed points for
norm-FS presentations, preservation of the reduced section supnorm,
and a 1-Lipschitz metric operator. Theorem 7.22 gives a necessary
fixed-point condition for genuine FS metrics at sufficiently divisible
powers; its wording is not replaced by an unproved converse.

## What the regular envelope limit proves

For a bounded metric on a semiample rational line bundle, let $P$ be the
pointwise envelope over global psh competitors and $Q$ the envelope over
FS, equivalently continuous global psh, competitors. They satisfy
$Q\le P\le\phi$; $Q$ is lower semicontinuous. Proposition 7.25 identifies
$Q(\phi)=P(\phi_*)$, where $\phi_*$ is the **lower** regularization of
the obstacle. The printed approximants tend to the competitor $\psi$,
rather than to $\phi$ as one sentence says.

Theorem 7.26 proves

$$
\frac1m\operatorname{FS}(m\phi)\longrightarrow Q(\phi),
\qquad m\in N(L),\quad m\longrightarrow\infty,
$$

where $N(L)$ is the semigroup of globally-generated integral powers.
Section-product norm submultiplicativity gives superadditive FS weights,
then the Fekete limit. The normalized sequence need not be monotone:
$a_m=\lfloor m/2\rfloor$ is superadditive but $a_2/2>a_3/3$.
It is therefore insufficient to apply Dini directly to all normalized
powers without a further argument.

For completeness, the uniformity when $Q$ is continuous can be obtained
within the existing proof's inputs. A finite compact cover chooses powers
whose normalized FS weights are within a given positive error of $Q$.
A common multiple $M$ dominates all these weights by superadditivity,
giving one uniform approximation. In each residue class modulo $M$ that
occurs in $N(L)$, choose one positive representative $b_r\in N(L)$.
For sufficiently large $m$ in that class, $m=kM+b_r$. Superadditivity
then bounds the normalized $m$ weight below by the $M$ approximation
with an $O(1/m)$ remainder from finitely many bounded continuous $b_r$
weights. The upper bound is $Q$. This proves uniform convergence in
that hypothesis; conversely a uniform limit of continuous weights is
continuous. This explanatory completion does not prove that $Q$ is
continuous for every continuous obstacle.

Corollary 7.27 preserves reduced section norms under $P$ and $Q$.
Continuity of envelopes is a separate property. Lemma 7.29's first
opening names the wrong hypothesis for the implication being proved.
Under the upper-envelope psh-closure property, the usc regularization
of $P(\phi)$ is psh and remains below continuous $\phi$, hence is at
most $P(\phi)$ by its defining maximality. Since $P(\phi)=Q(\phi)$ is
already lsc, this gives continuity. Conversely, apply continuous $P$
to a decreasing continuous-majorant net of a usc upper envelope. This
proves the stated equivalence without proving either property universally.

The source's Conjecture 7.30 and its known-case list are dated 2021.
The listed non-Archimedean cases concern smooth varieties: curves;
discretely or trivially valued residue characteristic zero; and a
positive-characteristic function-field case with resolution assumed in
dimension $n+d$. These are not an exhaustive present literature status,
nor a general critical homogeneous Siu/envelope theorem.

## Continuous global field descent without a general envelope assumption

Theorem 7.31 uses projective geometrically reduced $X$, a continuous
metric $\phi$, semiample rational $L$ and arbitrary complete $F/K$.
In the non-Archimedean formulation it says that $\phi$ is global psh
if and only if $\phi_F$ is global psh. If the latter is psh, then
$Q(\phi_F)=\phi_F$ is already continuous, so Theorem 7.26 gives its
uniform FS approximation. With that error denoted $\varepsilon_m$,
the exact norm-FS pullback, surjectivity of analytic field projection
and 1-Lipschitz estimate give

$$
\left\|\frac1m\operatorname{FS}(m\phi)-\phi\right\|_\infty
\le\varepsilon_m+
\frac1m d_\infty\!\left(\|\cdot\|_{m\phi_F},
                         (\|\cdot\|_{m\phi})_F\right).
$$

Theorem 6.6 makes the second term vanish. This uses a particular
already-psh continuous obstacle on the extension, and therefore does
not assume general envelope continuity. It retains all global,
continuity, polarization and geometric reducedness premises. No
arbitrary local upper-semicontinuous weak-psh descent follows.

The end seam preserves the fundamental top-dimensional cycle with generic
local-ring lengths. For a finite fibre algebra the Dirac weight is
composition length times residue degree, equal to its vector-space
dimension; no multiplicity factor is dropped.

Earlier Demailly/Ohsawa–Takegoshi, Fornaess–Narasimhan, CLD regularized
maxima, linear norm density, model geometry, relative ampleness, analytic
projection and classical topology remain attributed inputs. The 4,659-page
book, 425 core TeX inputs, both bibliographies, native catalogue/editor
and all 42 atoms/twelve problems are unchanged during this source-only
checkpoint. General BJ22 critical homogeneous Siu/envelopes remain OPEN;
LPWZ density UNVERIFIED, and the BJ22 Theorem 6.21 proof warning stays
binding. No original general theorem or independent-model receipt is claimed.
