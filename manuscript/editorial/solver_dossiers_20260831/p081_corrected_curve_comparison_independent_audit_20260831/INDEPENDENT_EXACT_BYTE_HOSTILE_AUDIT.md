# Independent exact-byte hostile audit: corrected P08.1 curve comparison

Date: 2026-08-31. Auditor: independent agent `p082_independent_reaudit`.

## Verdict and limits

**PASS: 0 critical mathematical errors; 0 unresolved mathematical gaps.**

This verdict applies only to the replacement statement and current proof
identified below. It is an independent mathematical audit, not a production
receipt, acceptance decision, live-book integration, or inventory-closure claim.
The earlier unrestricted degree-zero P08.1 theorem is not a dependency. In
particular, this verdict does not rehabilitate that earlier theorem or the
historical conditional p082 strict-analytic transfer packet.

The valid conclusions are positive-degree regularization over the original
field, and degree-zero regularization **conditional on existence of one
semipositive Q-formal metric on the given line bundle over that field**. The
replacement does not assert that such a degree-zero model metric always exists.

One source-attribution omission was reported during the audit and corrected by
the author: zero curvature first gives subharmonicity of both signs by
Thuillier 3.4.12, and GR Classical 3.12 then gives harmonicity. The final proof
below contains that correction. One nonblocking source-precision observation
about common semistable models is recorded in Section 4.

## 1. Exact inputs and audit boundary

Candidate directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_positive_degree_and_zero_criterion_candidate_20260831`

| File | Audited SHA256 |
| --- | --- |
| statement.tex | `5158fe6399885289ba2e9bf7a57f7da32a87fdb7b7d6e6b5bc20879e054564b6` |
| proof.tex | `99028d9d33abcfe31e42dd6f5e1aedb6c00822c5408ef46da4ef692ed2ef3a17` |
| README.md | `a2bae10eaf4fccffef57cf0eedf6f3c4db6c5bb0f9b1aea2f882d981b3acb1bd` |

The initially read proof had hash
`bdc92f510ff03e253ec401ba27134f4b13176d2c0b1730b3490909ee0b098b12`.
It was superseded during this audit by the author's explicit zero-curvature
citation repair. The revised passage and final hash were checked. Only the
current hash in the table receives the verdict.

The auditor did not modify the candidate, its support files, any earlier audit,
or the live manuscript. No production service was called. This audit did not
independently rerun LaTeX compilation; mathematical correctness and source
hypotheses are the subject of this report. The statement/proof control-byte
check excludes bytes 0x00-0x08, 0x0B-0x0C, 0x0E-0x1F, and 0x7F.

## 2. Primary-source ledger

The cited local PDFs were read at the relevant theorem and proof passages;
the crucial pages were also rendered and visually inspected. Extracted text
was not accepted where its symbols were corrupt. This mattered especially for
Thuillier and Gubler 1998. PDF page numbers below are one-based physical pages;
printed page numbers are distinguished explicitly.

| Source | Exact passages checked | Scope actually used |
| --- | --- | --- |
| GJKM, arXiv:1712.00980v3 | Theorem 1.1; Definition 2.8; Proposition 2.9(viii) and proof; Proposition 2.11 and Lemma 2.13; Definition 3.4; Propositions 3.5(c), 3.7 and proofs; semistable-model sentence opening the proof of Theorem 3.1 | Nontrivial complete real-valued field; smooth projective curve; integral value-group-affine graph functions; outgoing-slope positivity; finite normal envelope base change. Physical pp. 7-10 were visually checked. |
| Thuillier thesis | Lemma 2.2.22; Proposition 3.2.4; Theorems 3.4.12 and 3.4.19, including the latter's proof | Strict smooth analytic curves; finite semistable skeletal factorization; type-II point insertion after finite separable extension; global directed lisse metric approximation. Physical pp. 58-59, 84, 108-109, 112-113 were visually checked. |
| GM, arXiv:1608.08030v3 | Theorem 1.1; Sections 2.1-2.2; Proposition 2.10; Proposition 2.18; Lemma 3.3; Proposition 3.5; Sections 4.7-4.8; Propositions 4.11, 4.13 | Proper algebraic/formal metric equality; finite definition inside the completed algebraic closure; nefness on any representing model and its scalar-extension reflection; ample extension on a dominating model. Physical pp. 11-13, 17-18 were visually checked. |
| GR Classical, arXiv:2506.13548 | Sections 1.2, 3.12, 4.1.2; Proposition 3.14 | CLD-psh implies curve subharmonic; harmonic iff both signs subharmonic; maximum principle and scalar extension. Physical pp. 19-20 were visually checked. |
| GR PL, arXiv:2503.05513 | Proposition 5.1 and its proof | Good smooth strict curve over a nontrivially valued field; local R-PL subharmonicity equivalent to nef residue line bundle. Physical p. 15 was visually checked. |
| CLD, current local PDF | Proposition 8.1.5; Section 11.1.9; Theorem 18.1.6; Corollary 18.1.7 and its proof | Pullback of the transfinite psh stages; scalar-extension surjectivity; Poincare--Lelong and mass with residue-field degrees. Physical pp. 196, 301, 502-503 were visually checked. |
| Gubler 1998, Local heights | Section 3, especially 3.8 and Definition 3.10 | Positive coefficients of the vertical cycle of a topologically nilpotent constant; reduction and scalar descent. Physical pp. 14-17, printed pp. 74-77, were visually checked because text extraction is unreadable. |

The official arXiv records for [GJKM](https://arxiv.org/abs/1712.00980),
[GM](https://arxiv.org/abs/1608.08030), and
[GR Classical](https://arxiv.org/abs/2506.13548) were checked for source identity.
The algebraic background is also independently recorded by
[Stacks, proper curves are projective](https://stacks.math.columbia.edu/tag/0A26)
and [Stacks, degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ):
degree is the Euler-characteristic difference, is invariant under field
extension, and positive degree on a proper integral curve is equivalent to
ampleness. These facts require neither a rational point nor a perfect field.

### Source-text cautions

1. Thuillier 3.4.19 has stray symbols in its printed statement (including an
   unintroduced open set). Its proof explicitly constructs metrics on the
   global line bundle, checks harmonic transition functions, and indexes them
   by a filtered set of finite subsets. The replacement correctly invokes that
   proof, not an unsupported extrapolation of the statement.
2. The isolated curvature sign in the paragraph before Thuillier 3.4.18 is
   inconsistent with its immediately surrounding norm convention. The audit
   follows the explicit weight `-log ||s||`, Poincare--Lelong, and the outgoing
   slope formula, which agree. It does not copy that isolated sign.
3. The unrestricted nef conclusion of GJKM Theorem 3.1 and the disputed
   nonemptiness assertion in Theorem 3.10 are not used. Reading the semistable
   reduction sentence in the proof of 3.1 does not import its envelope
   conclusion.

## 3. Curvature, signs, and the elementary graph argument

Smoothness and geometric connectedness give geometric integrality. Properness
makes the analytification compact, boundaryless, and good; algebraicity makes
it strict. Thus the curve comparisons and proper-curve degree formula apply.
The transition identity for weights has the correct minus sign. A nonzero
meromorphic section exists on the integral algebraic curve and is regular in
the meromorphic sense required by CLD 18.1.6. The resulting divisor mass counts
closed points with `[k(P):K]`, not as unweighted atoms.

For `Delta f = sum(outgoing slopes)`, integration by parts gives
`E(f) = -integral f Delta f`. At an oriented interior bend the contribution is
`r_right-r_left`. Therefore a convex bend is positive; at a vertex the
opposite endpoint sign is automatically included. The graph matrix has only
constants in its kernel and has image exactly the total-mass-zero vectors.
Loops count twice in the valence and have zero contribution for a function
affine on the entire loop. The one-vertex/no-edge case is separately handled.

For `Delta g = m(delta_y-delta_x)`, the maximum is attained at x and the minimum
at y (possibly on larger constant plateaux). Hence
`E(g)=m osc(g)`. Applying Cauchy--Schwarz to a shortest x-to-y path gives
`osc(g) <= m d(x,y)`. Normalizing at any graph point puts zero between the
extremes. Thus the stated sup-norm bound, including its sign, is correct;
summing normalized potentials gives the finite-transport bound.

No effective-resistance lower bound, commensurability of edge lengths, or
rationality of the uncorrected harmonic slopes is assumed.

## 4. Lisse reduction, point types, and model realization

Thuillier's global approximants increase as norms and hence decrease as
additive weights. Their continuous nonnegative error functions decrease
pointwise to zero. Compactness plus directedness gives a finite-subcover Dini
argument. It yields a sequence by selecting one approximant for each positive
accuracy; it does not require metrizability of the Berkovich curve or a
countable cofinal family of models.

The relative weight of two lisse metrics is a global lisse function. On a
finite skeleton it is real piecewise affine, not necessarily a real linear
combination of global Q-model functions. The replacement makes no such
identification.

Over the algebraically closed field the value group Gamma is a nonzero
Q-vector subspace of R and hence dense. On a semistable annulus its Gamma
coordinates are type II. A type-III breakpoint lies in an edge and has valence
two. Since the reference curvature is supported at type-II points, a
type-III curvature atom of the lisse subharmonic metric has nonnegative mass.
The graph transport removes exactly that atom and adds the same positive mass
at a nearby type-II point. The sup error tends to zero. The old type-III
point has zero bend after this operation, so it can be deleted as a vertex.
Remaining type-II subdivision points can be inserted in a strict semistable
model by Thuillier 2.2.22; its finite separable extension is trivial over the
algebraically closed field. This does not assert that type-III subdivision
points already correspond to strict formal components.

Nonblocking citation precision: Thuillier 3.2.4 supplies factorization and
2.2.22 supplies point insertion. Making the initially chosen formal reference
model, and hence its closed form, determined on a common semistable model also
uses the usual semistable-domination theorem. This is explicitly recalled in
the proof of GJKM 3.7 and in the opening semistable-reduction sentence of the
proof of GJKM 3.1, attributed there to Bosch--Lutkebohmert Section 7. This
standard geometric input is independent of the disputed nef-envelope claim.
It verifies the hypothesis that the reference form is determined on the
model used for GJKM 3.7. It would be useful to cite this input more explicitly
in Step 3, but the underlying inference is valid.

## 5. Rational interpolation and its curvature margin

The new measure assigning `d/|V|` to every vertex has the same total mass as
the original curvature. The graph potential exists, and mixing it with weight
lambda gives the strict lower bound `sigma=lambda*d/|V|` at each original
vertex. This is precisely where positive degree is essential.

Finite vertex values can be approximated in Gamma closely enough to control
all edge slopes, because the graph has finitely many positive edge lengths.
For an oriented edge with endpoint difference D and length ell, the proposed
breakpoint satisfies

`r_minus*t + r_plus*(ell-t) = D`.

The inequalities `r_minus < D/ell < r_plus` imply `0<t<ell`. Rational slopes,
`D,ell in Gamma`, and divisibility imply `t in Gamma`; also the new value
`q_v+r_minus*t` belongs to Gamma. Thus the construction preserves endpoints
exactly, including a loop's repeated endpoint. It produces one continuous
global function.

At the inserted point, the curvature gain is `r_plus-r_minus>0`. At each
original vertex every outgoing slope changes by less than delta, so its
curvature remains above `sigma-valence*delta>sigma/2`. In fact the endpoint
losses exactly balance the added bend masses globally. Subdivision creates no
uncontrolled negative curvature elsewhere.

After a common integer clears the finitely many rational slopes, the function
is integral Gamma-affine in the exact sense of GJKM Definition 3.4. Proposition
3.5(c) therefore realizes it as a Q-model function; Proposition 3.7 applies
with residue weights one over the algebraically closed field. This is not an
inference that all real piecewise affine functions are model functions.

The uniform estimate `eta+delta*max(edge length)` follows by integrating the
slope error from one endpoint. First making lambda small, then delta small
relative to the positive margin, and finally vertex errors small proves
arbitrary accuracy. The construction genuinely avoids the irrational-cycle
obstruction: it permits small positive bend masses and strictly positive
vertex curvature, unlike the degree-zero situation where all curvature must
vanish.

## 6. Original-field descent and the ample refinements

The completed algebraic closure F is complete and algebraically closed.
The pulled-back curve stays smooth and geometrically integral. Pullback of
CLD-psh weights is justified through the functorial transfinite stages, so the
upstairs result applies.

GM 2.18(b) is applied only with compact C and F equal to the completed
algebraic closure. These are its essential restrictions. After clearing
denominators, a representing model over the finite definition field exists.
GM 3.5 says that its base change is nef because the associated metric is
semipositive; GM 3.3 reflects nefness back to that finite field. Descent of the
metric alone is not silently substituted for descent of semipositivity.

Model constants in `Q(-log|K_i^*|)` are dense. Subtracting a constant between
`1/i` and `2/i` gives the claimed lower error `3/i` and puts the approximant
below the target. A finite normal extension containing K_i exists even in the
inseparable case. GJKM 2.11 explicitly covers finite normal extensions, using
its purely inseparable and Galois cases. It is not applied directly to F/K.
Surjectivity first transfers the inequalities from F to the finite normal
field, and then transfers the envelope inequality back to K. Letting i grow
gives `P_theta(u)=u` on the original curve.

The de Rham class is ample since `deg L>0`. In fact, once the proof has shown
`P_theta(u)=u` with u continuous and finite, Proposition 2.9(viii) alone gives
the required uniform model approximation. Its proof is the directed-max/Dini
argument. Thus no use of the disputed degree-zero nonemptiness assertion is
hidden in the additional citation of the ample Theorem 1.1.

GM's algebraic/formal equivalence is valid over arbitrary nontrivial complete
fields for proper schemes. Proposition 4.11 gives an ample extension of a
positive tensor power on a model dominating the chosen nef model. Rational
mixing therefore takes place on a single model and preserves the generic
Q-line bundle L. Every special-fibre component gets positive degree. The
curve ampleness criterion and the fibrewise criterion cited in GM 4.13 give
relative ampleness; no smooth or reduced special fibre is required here.

A sufficiently high power is generated by finitely many model sections. At
each analytic point these sections have norm at most one and at least one has
norm one, giving the displayed maximum formula and its Fubini--Study metric.
Rational roots recover the Q-model metric on L. Base change preserves these
models, nefness, ampleness, and the generating sections. Surjectivity of the
analytic scalar-extension projection preserves the sup distance, so the same
sequence gives the asserted approximation over every complete extension.

## 7. Degree zero and numerical triviality

Positive curvature of total mass zero vanishes. The revised Step 1 correctly
uses Thuillier 3.4.12 and GR Classical 3.12 to deduce harmonicity of local
weights. Given one semipositive Q-formal metric, GM 3.5 and GR PL 5.1 make its
weights subharmonic as well; the same mass argument makes it harmonic. The
logarithmic ratio with the target is therefore a global continuous harmonic
function. Compactness and the harmonic maximum principle make it constant.

Constants from `Q(-log|K^*|)` can approximate that real constant because K is
nontrivially valued. Multiplication by their exponentials gives Q-formal
metrics and changes no curvature. Conversely, any nonempty sequence of
semipositive Q-formal metrics supplies one such metric. This proves exactly
the stated if-and-only-if, without inferring existence from generic nefness.

For numerical triviality the divisor in the degree ledger is `div(rho)`, not
the special fibre as a supposed Cartier divisor. The model is flat, so the
nonzero constant rho is a nonzerodivisor. In Gubler 1998 Section 3.8 its order
on every component of an algebraically closed reduced-special-fibre model is
`-log|rho|>0`. Definition 3.10 transports the cycle through finite reduction
and field descent. Hence all coefficients lambda_Y(rho) on the original
special-fibre components are strictly positive. Combined with GM 4.8, generic
degree zero and nefness force every component degree to vanish separately.
Proper integral curves in a curve model's special fibre are its
one-dimensional irreducible components, so this is numerical triviality, not
merely vanishing of one weighted total. Constant shifts preserve it, and
scalar extension preserves both nefness of the bundle and its inverse.

## Final disposition

The replacement is mathematically suitable to proceed to its separately
required exact-current production verification. This audit itself grants no
production acceptance. Its pass is not conditional on the superseded P08.1
claim and makes no assertion about unrestricted degree-zero model existence.

The companion SHA256SUMS binds this report, the three principal candidate
files, and the local primary-source PDFs. Rendered source pages remain only
in the isolated scratch directory
`/private/tmp/p081_replacement_source_audit_20260831.v12GiM`; no source PDF was
altered or re-exported.
