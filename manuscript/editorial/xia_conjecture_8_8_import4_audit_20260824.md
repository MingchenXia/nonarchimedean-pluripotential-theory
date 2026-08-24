# Xia Conjecture 8.8: exact audit of imported inputs 3 and 4

Date: 2026-08-24.

Audited packet:
`manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`.

## Scope and exclusion rule

This audit checks only

1. the last paragraph of Imported input 3, identifying Cao's mixed volume
   with the mixed non-pluripolar mass of the \(\mathcal I\)-model envelopes;
2. Imported input 4, concerning nef approximants, positive/movable products,
   and currents with minimal singularities.

The source explicitly excluded in the task was not used.  It is not cited by
title or identifier in any of the exact proof paths used below.  In particular,
neither Xia's *Transcendental b-divisors I* nor
Darvas--Xia's *The volume of pseudoeffective line bundles and partial
equilibrium* contains a citation to it, and the latter is the source invoked in
the proof of Xia's Theorem 3.5.  BFJ09 and BEGZ10 predate the excluded paper.

## Verdict

| Packet assertion | Verdict | Required qualification |
|---|---|---|
| Cao mixed volume equals the mixed \(\mathcal I\)-envelope mass | **Supported** | Cite Xia, Definition 3.2 and Theorem 3.5 together; Proposition 3.3 supplies the pure-volume compatibility used to pass from positive Cao self-volume to positive envelope mass. |
| A nef birational approximant has intersection at most the positive product | **Supported in the target projective setting** | State the input for big numerical divisor classes on a smooth projective variety and cite BFJ09, Proposition 2.13 (or Definition 2.5 in the effective \(\mathbb Q\)-divisor case). |
| Positive product equals ordinary intersection on nef classes | **Supported** | Cite BFJ09, Proposition 2.12. |
| The mixed non-pluripolar product of minimal currents represents the positive product | **Supported** | Cite BEGZ10, Definition 1.17.  In top degree, taking the integral gives the corresponding positive/movable intersection number. |

There is no mathematical obstruction to the uses of inputs 3 and 4 in the
packet.  The present wording is nevertheless under-cited, and the first
sentence of input 4 is broader than needed unless one explicitly chooses the
compact-Kaehler analytic definition.  The minimal safe repair is to state the
nef-approximation assertion in the smooth projective numerical-divisor
framework actually used in the proof.

## 1. Cao volume and the \(\mathcal I\)-envelope product

The exact primary source is Mingchen Xia,
[*Transcendental b-divisors I---Correspondence with currents*](https://mingchenxia.github.io/Papers/TB.pdf),
Section 3.1:

- Definition 3.1 defines Cao's mixed volume
  \(\langle T_1,\ldots,T_n\rangle_C\).
- Definition 3.2, equation (3.1), says that if every pure volume
  \(\operatorname{vol}T_i\) is positive, then the Darvas--Xia mixed volume is
  \[
  \int_X\bigwedge_{i=1}^n
  \bigl(\theta_i+\mathrm d\mathrm d^c
  P_{\theta_i}[\varphi_i]_{\mathcal I}\bigr).
  \]
  Equation (3.2) extends the definition to the zero-volume boundary by adding
  \(\varepsilon\omega\) and letting \(\varepsilon\downarrow0\).
- Proposition 3.3 identifies the repeated-entry mixed volume with the pure
  volume: \(\operatorname{vol}(T,\ldots,T)=\operatorname{vol}T\).
- Theorem 3.5 proves
  \[
  \langle T_1,\ldots,T_n\rangle_C
  =\operatorname{vol}(T_1,\ldots,T_n)
  \]
  for closed positive \((1,1)\)-currents on a connected compact Kaehler
  manifold.

Thus Theorem 3.5 supports the packet, but the phrase "is Theorem 3.5" is
slightly compressed: the displayed envelope integral comes from Definition
3.2, while Theorem 3.5 identifies it with Cao's construction.

The positivity transition in Section 7 of the packet is also justified.  If
"positive Cao volume" means
\(\langle T_i,\ldots,T_i\rangle_C>0\), Theorem 3.5 and Proposition 3.3 give
\[
 0<\operatorname{vol}T_i
   =\int_X
     \bigl(\theta_i+\mathrm d\mathrm d^c
       P_{\theta_i}[\varphi_i]_{\mathcal I}\bigr)^n.
\]
After putting
\(u_i=P_{\theta_i}[\varphi_i]_{\mathcal I}\), this last number is exactly the
ordinary non-pluripolar mass of \(u_i\).  Accordingly, the packet's sentence
"The positive Cao-volume hypothesis says precisely that \(u_i\) has positive
mass" is correct; it does **not** assert that the original \(\varphi_i\) has
positive raw mass.

The proof of Xia's Theorem 3.5 cites Darvas--Xia, Corollary 3.4, in
[*The volume of pseudoeffective line bundles and partial equilibrium*](https://research.chalmers.se/publication/542539/file/542539_Fulltext.pdf),
together with the corresponding result in Xia's book.  The exact cited
corollary proves convergence of the masses of the quasi-equisingular
approximants to the mass of the \(\mathcal I\)-model envelope.  This proof
path contains no use of the excluded source.

### Minimal revision for Imported input 3

Replace its last paragraph by:

> For closed positive currents \(T_i=\theta_i+\mathrm d\mathrm d^c\varphi_i\),
> Xia, *Transcendental b-divisors I---Correspondence with currents*,
> Definition 3.2 and Theorem 3.5, identifies Cao's mixed volume with the
> Darvas--Xia mixed volume.  When each pure volume is positive, Definition
> 3.2 gives this mixed volume as the mixed non-pluripolar mass of the
> \(\mathcal I\)-model envelopes.  Proposition 3.3 gives compatibility with
> the pure volume.  No result from *Transcendental b-divisors II* is needed
> for this identification.

This revision supports both the theorem statement and the reduction at the
start of Section 7.

## 2. Nef approximants and the projective positive product

The exact algebraic source is Boucksom--Favre--Jonsson,
[*Differentiability of volumes of divisors and a problem of Teissier*](https://arxiv.org/html/math/0608260v2),
Section 2:

- Definition 2.5 defines the positive intersection product of big classes as
  the least upper bound of products of nef classes obtained by subtracting
  effective \(\mathbb Q\)-divisors on modifications.
- Proposition 2.13 gives the equivalent and slightly broader formulation: if
  \(\alpha_i\) are big Cartier numerical classes on the Riemann--Zariski
  space, then \(\langle\alpha_1\cdots\alpha_p\rangle\) is the least upper
  bound of \(\beta_1\cdots\beta_p\), where every \(\beta_i\) is nef and
  \(\beta_i\leq\alpha_i\) in the pseudoeffective order.
- Proposition 2.12 proves that the positive product of nef classes equals
  their ordinary intersection product.

Apply Proposition 2.13 after regarding classes on \(X\) and \(Y\) as Cartier
classes on the Riemann--Zariski space.  If
\[
 \mu^*\alpha_i=\beta_i+\{E_i\},\qquad E_i\geq0,
\]
then \(\mu^*\alpha_i-\beta_i=\{E_i\}\) is pseudoeffective, hence
\(\beta_i\leq\alpha_i\).  For \(p=n\), numerical codimension \(n\) is
one-dimensional and the pseudoeffective order is the ordinary order on
numbers.  Therefore
\[
 \beta_1\cdots\beta_n
 \leq\langle\alpha_1,\ldots,\alpha_n\rangle.
\]

This is exactly the inequality used in equation (5): after division by
\(k\), the decomposition
\(\mu_k^*D_i=k^{-1}M_{i,k}+k^{-1}F_{i,k}\) is an admissible BFJ nef
approximant.  No transcendental extension is needed for that argument.

The current Imported input 4 starts with an unqualified statement about a
"modification" and classes \(\alpha_i\).  BFJ09 directly supports it for the
smooth projective numerical-divisor framework of the theorem.  If the sentence
is intended as a theorem for arbitrary compact Kaehler cohomology classes, it
needs a separate analytic formulation and source.  Since the proof never needs
that extra generality, restricting the sentence is the cleanest repair.

## 3. Minimal singularities and the analytic positive product

The exact analytic source is Boucksom--Eyssidieux--Guedj--Zeriahi,
[*Monge--Ampere equations in big cohomology classes*](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf),
Definition 1.17.  If \(\alpha_1,\ldots,\alpha_p\) are big classes and
\(T_{i,\min}\in\alpha_i\) have minimal singularities, it defines the positive
product by
\[
 \langle\alpha_1\cdots\alpha_p\rangle
 =\left\{\left\langle
 T_{1,\min}\wedge\cdots\wedge T_{p,\min}
 \right\rangle\right\}.
\]
The same section explicitly relates this class to the positive intersection
product of BDPP/BFJ; Proposition 1.18 supplies analytic-singularity
approximants.  In degree \(p=n\), taking the integral gives
\[
 \int_X\left\langle
 T_{1,\min}\wedge\cdots\wedge T_{n,\min}
 \right\rangle
 =\langle\alpha_1,\ldots,\alpha_n\rangle.
\]

Consequently, the last sentence of Section 7 of the packet is supported in
the target setting of big line bundles.  Its left side becomes the BEGZ
positive product by Definition 1.17, and its projective numerical
interpretation is the BFJ movable/positive intersection number.  The separate
fact that the partial body of a minimal metric is the ordinary Okounkov body
belongs to Imported input 1, not to input 4.

### Minimal revision for Imported input 4

Replace the whole item by:

> **Positive products in the projective setting.**  Let \(X\) be smooth
> projective and let \(\alpha_i\) be big numerical divisor classes.  If
> \(\mu:Y\to X\) is a modification and
> \(\mu^*\alpha_i=\beta_i+\{E_i\}\), where \(\beta_i\) is nef and
> \(E_i\geq0\), then BFJ09, Proposition 2.13, gives
> \(\beta_1\cdots\beta_n\leq
> \langle\alpha_1,\ldots,\alpha_n\rangle\).  By BFJ09, Proposition
> 2.12, positive and ordinary intersections agree on nef classes.  Finally,
> BEGZ10, Definition 1.17, identifies the cohomology class of the mixed
> non-pluripolar product of currents with minimal singularities in big
> classes with the corresponding positive product; in top degree their
> integrals therefore agree.

## 4. Bibliographic correction

The packet's prose names the right paper, but the book bibliography currently
records the key `Xiabdiv` as *Transcendental b-divisors* (2025).  The audited
source is titled *Transcendental b-divisors I---Correspondence with currents*.
The source file supplied with the author's Conjecture 8.8 proof already uses
that title and year 2026.  Updating the book entry would remove ambiguity with
the sequel.  The existing keys `BFJ09` and `BEGZ10` already contain the correct
published records.

## Final classification

**PASS AFTER CITATION/SCOPE REPAIR.**  Imported inputs 3 and 4 are sufficient
for every place they are used in the repaired proof packet.  No new theorem is
needed.  The necessary edits are bibliographic and scope-preserving: cite the
full Definition 3.2--Proposition 3.3--Theorem 3.5 chain for Cao volume, and
state the nef-approximation inequality in the smooth projective numerical
framework with BFJ09 Propositions 2.12--2.13 and BEGZ10 Definition 1.17.
