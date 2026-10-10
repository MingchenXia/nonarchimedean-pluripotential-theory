# Finite common chambers and formal orthogonal bases

Date: 4 October 2026. This book-external derivation makes the algebraic
steps of Li, arXiv:2505.11087v1, Section 3.2 explicit. It supplies formal
basis existence from stated local expansion and uniform-Lipschitz inputs,
and then links to the earlier convergent truncation. It makes no priority
claim, new-book theorem admission or independent model-verifier claim.

## Local expansion input

Fix \(K=\mathbb C((t))\), \(\operatorname{ord}(t)=1\), integers
\(b_0,\ldots,b_m>0\), \(m\geq1\), and the closed rational simplex

\[
 \Delta_b=\{x\in\mathbb R_{\geq0}^{m+1}:\sum b_ix_i=1\}.
\]

Let \(R\) be an integral \(\mathbb C\)-algebra, regarded as a space of
coefficient functions on a stratum. Put
\(A=R[[z_0,\ldots,z_m]][z_0^{-1},\ldots,z_m^{-1}]\); its individual
elements have exponent support bounded below coordinatewise. The
substitution \(t=z^b\) embeds \(K\) in \(A\).
Let \(V\subset A\) be a \(K\)-vector space of finite dimension \(d\geq1\).
The inclusion is faithful; nonzero vectors have nonzero expansions.
For \(v=\sum f_\alpha z^\alpha\ne0\), define

\[
 \gamma_x(v)=\min_{f_\alpha\ne0}\alpha\cdot x,
 \qquad \gamma_x(0)=+\infty.                               \tag{1}
\]

The coordinatewise lower bound and Dickson's lemma give finitely many
minimal support exponents. They realize (1) on the whole closed simplex.
Here the elementary finiteness argument is as follows: after translating
the support into \(\mathbb N^{m+1}\), any infinite sequence has an infinite
subsequence nondecreasing in each coordinate, by successive extraction
in the finitely many coordinates. It cannot be an antichain of distinct
minimal elements. Every support element has a minimal predecessor inside
its finite coordinate box, so the finitely many minimal elements suffice.
Thus \(\gamma_x(v)\) is finite, continuous, concave and piecewise affine.
Multiplication by \(t^q\) adds \(q\), and multiplication by a unit in
\(\mathbb C[[t]]\) preserves its leading coefficient up to its nonzero
constant term. Consequently the usual scalar and ultrametric valuation
rules hold. The domain hypothesis on \(R\) excludes vanishing products;
the coefficient functions are not themselves assigned a further valuation.

Assume every \(\gamma(v)\) is \(B\)-Lipschitz on \(\Delta_b\) for one
fixed \(B\). In the geometric application \(B=Cl\) at fixed tensor
degree \(l\); no claim of a common finite wall set for every degree is made.
The existence of this faithful local expansion of the formal global
section space remains an explicit geometric/formal-completion input.

## Finite affine possibilities modulo integer constants

Use independent coordinates \(x_1,\ldots,x_m\), with
\(x_0=(1-\sum_{j=1}^m b_jx_j)/b_0\). A support exponent \(\alpha\)
that dominates on a nonempty open subset has affine form

\[
 \alpha\cdot x=\frac{\alpha_0}{b_0}
   +\sum_{j=1}^m\left(\alpha_j-\frac{b_j}{b_0}\alpha_0\right)x_j.
                                                               \tag{2}
\]

The Lipschitz bound bounds every slope in (2) by a constant depending only
on \(B\) and the fixed coordinate norm. Subtract the unique integer
multiple \(qb\) that puts \(\beta_0=\alpha_0-qb_0\) in
\(\{0,\ldots,b_0-1\}\). This changes the affine form by the integer \(q\)
and leaves its slopes unchanged. Each integer
\(\beta_j=\alpha_j-qb_j\) is now bounded, because

\[
 \beta_j=\left(\alpha_j-\frac{b_j}{b_0}\alpha_0\right)
          +\frac{b_j}{b_0}\beta_0.
\]

There are therefore finitely many possible normalized exponent vectors
\(\beta\), independent of \(v\). Let \(\mathcal F\) be their finite set
of affine forms \(f_\beta(x)=\beta\cdot x\).
For every \(v\), its lower envelope is determined by support exponents
active on open sets: any redundant exponent can be removed from that
envelope, including on the boundary by continuity. Within that one vector,
two active exponents obey

\[
 \alpha\cdot x=f(x)+q,\qquad \alpha'\cdot x=f'(x)+q'.
\]

Their equality locus is \(f-f'=q'-q\). Include, as walls, all proper
hyperplane cuts

\[
 \{x\in\Delta_b:f(x)-f'(x)=a\},
 \qquad f,f'\in\mathcal F,\quad a\in\mathbb Z,             \tag{3}
\]

that intersect the simplex. There are finitely many: each difference is
bounded on the compact simplex, so only finitely many integers \(a\)
are possible. Identical forms are not walls. The **integer translates**
in (3) are included because arbitrary \(K\)-coefficients shift valuations
by integer orders; counting slopes alone would not establish the claim.

Let \(O\) be a nonempty full-dimensional connected component of the
relative interior minus these walls. Every \(v\ne0\) has one unique
leading exponent \(\alpha(v,O)\) throughout \(O\).
If two distinct exponents have affine forms equal on an open subset of
\(\Delta_b\), their difference is \(cb\), with constant value \(c\);
equality to zero forces \(c=0\), so they were the same exponent.
Any other equality of distinct active affine forms would lie on (3).
The chamber is a rational polyhedron and contains a rational point.

## Leading-coefficient criterion, with all scalar orders

For \(v_1,\ldots,v_r\ne0\), write their leading data on \(O\) as
\(f_i z^{\alpha_i}\). Partition the \(\alpha_i\) into classes modulo
\(\mathbb Zb\). They are orthogonal simultaneously on \(O\), meaning

\[
 \gamma_x\Bigl(\sum_i a_iv_i\Bigr)
 =\min_i\{\operatorname{ord}(a_i)+\gamma_x(v_i)\}
 \quad(a_i\in K,\ x\in O),                               \tag{4}
\]

if and only if the \(f_i\) are \(\mathbb C\)-linearly independent
within each such class.

To prove sufficiency, fix \(x\in O\) and nonzero coefficients. Each
leading exponent in the sum is
\(\alpha_i+\operatorname{ord}(a_i)b\). If two of their values attain
the same minimum at \(x\), (3) implies their affine functions agree on
all of \(O\); the preceding open-set argument makes their exponent
vectors equal. Thus all indices attaining that minimum belong to one
class. The coefficient of the common leading monomial is
\(\sum \operatorname{lc}(a_i)f_i\), which is nonzero by independence.
Subleading scalar powers and subleading section terms have strictly
larger value. This proves (4).

Conversely, if \(\sum c_if_i=0\) is a nontrivial dependence within one
class, choose integers \(q_i\) aligning all
\(\alpha_i+q_ib\). The combination \(\sum c_it^{q_i}v_i\) cancels
that leading term, so its value is strictly greater than the common
minimum at every \(x\in O\), or it is zero. This violates (4).
The coefficient relation is over \(\mathbb C\), the residue field of
\(K\); it is not a relation over the full function field of the stratum.

## Formal basis existence and the cancellation limit

Start with any nonzero vector and inductively build an orthogonal
collection \(v_1,\ldots,v_r\), \(r<d\). Such a collection is
\(K\)-linearly independent by (4). Pick \(v\) outside its span \(U\).
If appending \(v\) satisfies the criterion, append it. Otherwise the
leading coefficient of \(v\) lies in the \(\mathbb C\)-span of the
leading coefficients of \(v_i\) in its exponent class; independence of
the old collection rules out a relation involving only the old vectors.
Subtract a combination \(\sum c_it^{q_i}v_i\) aligning that leading
exponent. The residual stays outside \(U\) and has strictly greater
valuation throughout \(O\). Repeat as long as no vector can be appended.

Choose a rational \(x_*\in O\). Every value in (1) lies in
\(Q^{-1}\mathbb Z\) for one denominator \(Q\) depending on \(x_*\).
If the process were infinite, the residual values would be strictly
increasing in this discrete group and hence would tend to \(+\infty\).
At each cancellation, an exponent used for \(v_i\) satisfies

\[
 q_i+\gamma_{x_*}(v_i)=\gamma_{x_*}(\text{current residual}).
\]

Every exponent used later therefore tends to \(+\infty\). The partial
coefficients \(a_i^{(j)}\) converge in the complete field \(K\) to
\(a_i\). Set \(r=v-\sum a_iv_i\). The ultrametric inequality gives

\[
 \gamma_{x_*}\Bigl(\sum_i(a_i-a_i^{(j)})v_i\Bigr)
 \geq\min_i\{\operatorname{ord}(a_i-a_i^{(j)})
                           +\gamma_{x_*}(v_i)\}\longrightarrow+\infty.
\]

Together with the residual values tending to infinity, this forces
\(\gamma_{x_*}(r)=+\infty\), so \(r=0\) by faithfulness. That would
put \(v\) in \(U\), a contradiction. The cancellation process must
stop, allowing one more vector. After \(d\) steps the collection is a
\(K\)-basis orthogonal at every point of \(O\).

This proof checks the convergence of the coefficient series and the
vanishing of their residual separately. It does not equate an infinite
formal sum with its limit without either check, and it does not require
a general finite-dimensional norm-equivalence theorem.

## The checked Lipschitz input and convergent transfer

For a smooth connected projective variety over \(K\), choose an SNC
model in the sense of BFJ (including its irreducible-stratum convention)
and a model reference for an ample \(L\). The author-hosted JAG proof
copy of Boucksom–Favre–Jonsson, *Singular semipositive metrics in
non-Archimedean geometry*, Theorem 6.1, physical page 34, supplies a
uniform facewise Lipschitz constant for all \(\theta\)-psh model
functions. Its Section 6 proof, pages 34–41, was freshly read and viewed.
This checkpoint cites that exact author-copy locator; its placeholder
publication header is not treated as a fresh inspection of the printed
2016 journal pages. The standing field is complete discretely valued,
with residue characteristic zero, satisfied by \(\mathbb C((t))\).

For a nonzero \(s\in H^0(lL)\), take \(k\) large enough that sections
\(\sigma_i\) generate \(klL\). Add \(s^k\), and choose integer weights
\(c_i\) sufficiently large that the FS model potential

\[
 \Phi=\frac1{kl}\max\{k\log\|s\|,\log\|\sigma_i\|-c_i\}
\]

equals \(l^{-1}\log\|s\|\) on the fixed compact dual complex. Such
weights exist because the model norm of \(s\) is continuous and positive
there, while the auxiliary norms are bounded above. Integer weights
can be realized by powers of \(t\), so this is a rational FS **model**
potential, within the checked theorem's scope. No extension from model
potentials to arbitrary real weights is required here. Applying Theorem
6.1 yields \(B=Cl\), independent of \(s\). Relative global generation
for the auxiliary ample power and the standard FS-model construction
are explicit geometric imports; they are not replaced by a claim about
an ungenerated section family.

There are finitely many faces and finitely many chambers at each fixed
degree. On the compact global skeleton, the model norms of the nonzero
formal sections are finite and continuous. Given the convergent section
module and its identification with \(V_K\), the
[earlier finite truncation](li_convergent_chamber_transfer_20261004.md)
now converts these constructed formal bases to convergent meromorphic
bases, retaining orthogonality on each chamber. Its finite matrices and
the [inverse-minor construction](li_finite_constraints_repair_20261004.md)
then bypass the collapsed quotients of the source's Section 3.3.

The algebraic formal-basis assumption is thereby derived from the local
expansion and Lipschitz hypotheses in this dossier. The faithful
geometric expansion, section-module/base-change identification, generic
mass and complex Fourier estimates, and the final hybrid approximation
remain separate application gates. No single convergence radius or wall
set for all tensor degrees is asserted. The active manuscript and all
42 problem statuses remain unchanged.
