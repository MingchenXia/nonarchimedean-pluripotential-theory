# Bounded-to-smooth Monge--Ampère regularity: source review

**Research-only checkpoint.** The controlling baseline is
`9dcc792d632394167cbb1e8bec0e1f0199233a4d`. Read Papa Badiane,
Chinh H. Lu and Ahmed Zeriahi,
[*Complex Monge--Ampère equations on Hermitian Manifolds: From bounded to smooth solutions*, arXiv:2610.06473v1](https://arxiv.org/abs/2610.06473v1),
submitted 5 October 2026 at 15:02:53 UTC, in all **23 actual pages**.
All pages, proofs and references were displayed and their full extracted
text read in twelve sheets. No result from this paper is yet admitted
into active TeX. The extraction's font-type warning is retained; the
actual rendered equations were inspected.

The PDF has 418,086 bytes and SHA-256
`ebd50dcc95674e20b8f9897421d65dc9737e01a7a6ff00b51f468099cfa0062e`.
The full-reading record SHA-256 is
`5762bf37c2fb1edafd9f4f3b67499818e5c4d1a0ebbf5e4dceaee5af6d139180`;
the view manifest SHA-256 is
`8ac5dc1d6c40cbb8b2370254c0c6c697e410e9b0ce8ddc64dba8fae63d8f53f3`.
The acquisition record remains unchanged with its historical false
reading flags. The separate full-reading record controls the completed
reading, without reinterpreting acquisition as proof verification.

## Main statement and proof structure

Theorem 1.1, actual page 2, assumes a compact Hermitian manifold X,
a smooth semipositive real (1,1)-form theta, and an analytic-singularity
potential rho such that theta+ddc rho dominates 2 epsilon_0 omega_X.
Let D be its singularity set, f smooth on X times R, and psi^+, psi^-
quasi-psh and smooth on an arbitrary open set Omega. A **given bounded**
theta-psh solution of

    (theta+ddc phi)^n = exp(f(x,phi)+psi^+-psi^-) omega_X^n

is claimed smooth on **Omega minus D**. This conditional regularity does
not assert existence, global smoothness across D, or uniqueness of the
original equation. No monotonicity of f in the unknown is imposed.
Omega need not be Zariski open. The bounded solution forces the density
exp(psi^+-psi^-) to be integrable, but that implication does not reverse
to existence of the original equation without further conditions.

In the smooth Kähler case, pages 6--8 introduce g(x,t)=f(x,t)-t and
solve the auxiliary equation with density exp(u_j+g(x,v_j)), where
v_j approximates the prescribed bounded solution. The Laplacian test
adds a positive quadratic expression in v_j, allowing absorption of
its derivative terms without assuming derivative bounds on v_j in
advance. Uniform potential and trace bounds give a limiting u. Both u
and the prescribed phi solve the same **strictly increasing auxiliary**
equation, so the domination principle identifies u=phi. The final
Evans--Krylov and Schauder steps also require the appropriate regularized
trace bounds and uniform ellipticity; smoothness is not obtained merely
by differentiating the original equation at a bounded weak potential.

Pages 8--12 treat degenerate Kähler data with envelopes, relative lower
bounds, and a local trace bound away from the singular data and D.
Pages 12--17 treat Hermitian torsion with a concave function gamma of
phi-rho-epsilon_0 psi^- plus a positive constant. The actual backgrounds
are theta+j^{-1} omega_X. Their first and second derivatives are
uniformly controlled. Pointwise inequalities theta<=omega<=omega_X
alone would not control the background derivative constants used in the
proof of Proposition 4.1. The natural limit locus remains Omega minus D.
General quasi-psh data also require explicit curvature rescaling and
regularization bookkeeping; the proof sections impose theta-psh
representatives and cannot erase that step by notation.

Corollary 1.2, page 3, pulls a bounded solution on a compact klt variety
to a resolution, using a Hermitian form and an adapted measure. It
claims smoothness on the regular locus. The pullback loses strict
positivity along the exceptional set. Adapted-density integrability,
the positivity barrier and the pullback/descent chain remain separate
primary inputs. This checkpoint does not certify the whole singular
extension or a global continuity assertion from this corollary alone.

## Existence, order and integrability

Theorem 1.3 on page 3 prints an ordered bounded subsolution and
supersolution criterion, and smoothness in Omega. Its detailed
Theorem 5.1 on page 18 additionally assumes exp(psi^+-psi^-) in L^p
for p>1 and concludes smoothness only on Omega minus D. The actual
proof on pages 19--21 is reviewed in that stronger scope; it does not
clear the introductory assertion under only L^1 data.

The iteration chooses A above the upper bound of the derivative of f
on the bounded order interval, so h(x,t)=f(x,t)-At is non-increasing.
Starting at the subsolution, the positive-exponent equation with frozen
h gives an increasing sequence confined below the supersolution.
Monotone Monge--Ampère convergence then gives a bounded solution.
Theorem 5.4 uses the normalizing constant c(t) for a frozen right-hand
side and its continuity. When f is non-decreasing, existence of both
barriers is the relevant criterion; integrability alone is insufficient.
For decreasing f, the ordering of the two barriers matters. The Fano
example on page 21 has barriers in the wrong order and supplies no
existence theorem. An auxiliary equation's uniqueness is distinct from
uniqueness of this original equation.

## Fresh primary dependency reading

All **38 dependency pages** were displayed and their full selected text
read in 21 sheets. Only the nine-page Székelyhidi--Tosatti paper was read
in full; the other three files have selected reading.

| Exact primary edition | Actual pages read | Checked scope |
| --- | --- | --- |
| Guedj--Lu envelopes III, 2107.01938v1, 5 July 2021, 11:12:56 UTC; 34 pages | 1--3, 8--13, 17--18, 26--29 | Theorem B; mildly singular domination and its consequences; global oscillation estimate; positive-exponent bounded existence; regularization and the torsion calculation in the higher-regularity proof |
| Székelyhidi--Tosatti, 0912.1808v2, 26 March 2010, 16:33:08 UTC; nine pages | 1--9, complete | Theorem 1.1 for a smooth compact Kähler background, bounded potential and arbitrary smooth dependence on the unknown; short-time derivative estimates and stationarity proof |
| Demailly, author-hosted Chern regularization paper; twenty pages | 1--2, 5--6, 11--13 | Theorems 1.1 and 4.1; fiberwise quasi-holomorphic exponential map; normalized equation (3.1); curvature/Lelong loss and the start of its estimate proof |
| Nguyen, 1501.00891v1, 5 January 2015, 15:26:22 UTC; 35 pages | 1--3, 13--16 | Positive-exponent Hermitian existence/uniqueness, nonzero density, Gauduchon bounds, comparison, and the complete displayed Theorem 2.1 proof |

The dependency reading record SHA-256 is
`51d2995b1fb6cd0e79f929a2d73f08b770b706457667b60965cc372edd12c803`;
its view manifest SHA-256 is
`e73db29c8502f0bee214b2eaf8026afc4267ef5f50d78b03c8a4f2729aac7395`.
Individual PDF/text hashes, URLs, status and exact page selections are
embedded in the manifest. ArXiv editions remain distinct from journal
editions. In particular GL Theorem 4.2's proof continues on unselected
page 30, and Demailly's estimate continues on unselected page 14;
neither complete proof is claimed freshly read here. The earlier
modified comparison, full envelope inputs, book-length elliptic
regularity and the remaining flow computations keep their imported
scope. Nguyen's page 15 anchors its smooth input to Cherrier's
Theorem 1, printed 373; that publisher page itself was not downloaded
or freshly inspected. Aubin--Yau alone does not supply the Hermitian
existence input cited on the new paper's page 17.

## Literal diagnostics

These are direct substitutions or formula comparisons, not an original
theorem or a certified complete repair. The current diagnostic record
has SHA-256
`c56c1d6071deb89c15e911bfb5c091c80bbb5386e2a0127f6cf40057a32ae515`.

1. Pages 7 and 11 add an invalid factor n to a trace product inequality.
   For n=2, identity reference, omega_phi=diag(100,1) and
   omega_v=diag(100,1/100), the two sides are 10201/100 and 10001/50.
   Lemma 2.1's weaker inequality without n is valid and is sufficient
   for the following derivative absorption.
2. Page 2's non-decreasing integrability-only existence assertion fails
   in the Kähler case: theta=omega_X=omega, psi^±=0 and f=log(2)
   would equate total mass V to 2V with V>0. This tests the introduction,
   not conditional Theorem 1.1.
3. Page 20's supersolution shift adds inf(phi_t0) where subtraction is
   needed. For f(x,t)=t, t0=0 and phi_t0=-2 constant, the printed shift
   is -4 and its required inequality 1<=exp(-4) fails. Subtracting the
   infimum produces 0. An initial positive-constant test did not witness
   failure and was corrected in a new immutable diagnostic version;
   both earlier versions retain their historical bytes.
4. Page 20 gives f=exp(t) as an example of limits minus/plus infinity;
   its limit at minus infinity is instead zero.
5. Page 12 differentiates h(x)+2t+exp(-t/2) incorrectly. The derivative
   is 2-(1/2)exp(-t/2), not 2-exp(-t). The entire proposed global
   singular example is not certified by this differentiation.
6. Page 18's Proposition 4.2 freezes v where the prescribed solution
   is needed for the stated limit identification. For theta=omega_X
   Kähler, v=0, f=0, psi^±=0 and given phi=1, its auxiliary constants
   converge to 0. Both Laplacians vanish in this test, so it does not
   refute the conclusion; the printed approximation alone does not
   identify the prescribed potential.
7. Page 12's Hölder display reverses the psi^+-psi^- sign when taking
   the density power. The standard argument keeps that positive sign.
8. Page 8 omits epsilon^{-2n} in the displayed fiber convolution with
   fixed Lebesgue measure. For a unit-integral cutoff and constant 1,
   its output is epsilon^{2n}, rather than 1. Demailly's actual page 6,
   equation (3.1), contains the required factor. The primary normalized
   formula controls any subsequent exposition.

There are further notation and citation issues: Section 5.3 changes
the letters for its extremal envelopes, and some local-locus statements
omit D. Varying L^1 dominators require uniform integrability or a
summable-subsequence majorant, as used explicitly in GL actual 27,
rather than an unqualified fixed-dominator argument. None of these
diagnostics is presented as a counterexample to correctly scoped
conditional regularity or as a complete proof repair.

## Preservation and continuation

All 425 active inputs, both bibliographies, 108 protected inputs,
58 prior frozen manifests and 115 prior exports retain their baseline
bytes. The checked **4,388-page book** and every generated book file
are unchanged. All 42 complete canonical statuses, twelve families,
tier counts 0/3/7/15/17, the open toric candidate and the native
catalogue source/PDF retain their bytes and scope. README and the
programme are the only changed tracked baseline files; the other
5,036 retain their hashes. Inventory and whitespace checks pass.
No fresh unchanged-book build, book PDF review, native compilation,
editor/tab change, independent model call or verification receipt is
claimed.

The next integration candidate is the previously published smooth
Kähler bounded-to-smooth result and the explicitly scoped frozen-limit
identification, connecting the book's mean-field, small-parameter and
regularity discussion. A broader degenerate Hermitian theorem, the
singular descent, general L^1 barrier existence, arbitrary full-mass
regularity and Fang's 2610.06719v1 Hessian paper need their separate
checks. No new canonical problem, solved status or general Siu/closure
repair is added. Cloud GitHub synchronization uses the existing work
branch and PR and explicitly fetches both main and work.
