# P07.1: shrinking neighbourhoods, stalks, and the exact CLD star

Date: 30 August 2026

Status: **isolated research dossier; no live integration; no P07.1
retirement; no production Rethlas call**.

## 1. Question audited

At the second CLD stage one starts with a decreasing family

\[
                        u_n\downarrow u,
                        \qquad u_n\in\operatorname{Psh}_{X,1}(U).
\]

For every fixed `n` and point `x`, first-stage membership supplies a
neighbourhood `V_n` of `x` and a decreasing row of smooth psh functions on
`V_n`.  The unsupported step in a naive diagonal proof is to replace all
the `V_n` by one common neighbourhood.  A stalk is a filtered colimit over
neighbourhoods and only guarantees common representatives for a **finite**
family of germs.  It does not commute with a countable product or with the
countable sequential operation used in the hierarchy.

The task was to determine whether this is merely formal or can occur inside
a source-legal affine tropical/analytic model.

## 2. Exact source-legal realization

The files `candidate_statement.tex` and `candidate_proof.tex` construct the
phenomenon on the exact star `X_B` of CLD Section 6.7.3.  The construction
uses no invented tropical structure.

Choose a distinguished full branch `b_+` and distinct branches `b_n`.  The
nested standard neighbourhood `U_n` truncates `b_1,...,b_n`.  On `b_+`, use
a smooth convex profile, constant near minus infinity, whose centre slope
is `+1`; on the exceptional branch `b_n`, use `-t`, whose centre slope is
`-1`; use zero on every other branch.  The finite centre-slope sum is zero,
and every branch is convex, so this is an ordinary CLD-smooth psh function
on `U_n`.

No neighbourhood of the centre supports representatives of all these
germs.  Indeed, a standard centre neighbourhood has only finitely many
exceptional branches.  Some `b_n` must therefore be full.  A representative
of the `n`-th germ would have derivative `-1` at the centre on that branch,
whereas smoothness makes it constant near the included endpoint and psh
convexity makes the derivative nondecreasing.  The impossible inequality is
`0 <= -1`.

This proves a precise negative statement:

> The sheaf and germ structure does not manufacture the common
> neighbourhood required by the fixed-core flattening lemma, even for a
> countable family of smooth psh germs on a bona fide affine tropical space.

## 3. Why this is not a hierarchy counterexample

The construction can be made deliberately more deceptive.  After adding a
fixed constant `C` that makes every profile positive, the rows

\[
                          2^{-k}(f_n+C)\downarrow0
\]

are decreasing smooth psh approximations to the same zero function on the
shrinking `U_n`.  The full two-index family still has no common native
domain.  Yet the target is already smooth, and positive constants give a
global decreasing approximation on all of `X_B`.

Thus failure to flatten a **chosen presentation** is not invariant under
changing the presentation.  Membership in `Psh_{X,1}` is existential.  A
genuine counterexample to first-stage collapse must prove that *every*
possible first-stage presentation of the outer limit fails on every fixed
neighbourhood.  Native-domain shrinkage of one array is insufficient.

There is a second obstruction to turning the displayed germs into global
rows.  On the CLD star, a psh function defined on a neighbourhood in which a
branch is full satisfies the branchwise convexity and exact endpoint-trace
conditions proved in the existing infinite-star theorem.  In particular, a
full branch cannot carry the negative centre slope used above.  Hence the
very feature forcing the native domain to truncate `b_n` also prevents that
germ from being the centre germ of a global psh row on a fixed open star.

The production-verified infinite-star theorem goes further: it identifies
the full psh sheaf with an explicit comparison sheaf stable under decreasing
limits and constructs a fresh fixed-neighbourhood approximation of the
limit.  Therefore `X_B` is a counterexample to automatic common
representatives of arbitrary germs, but a positive example for P07.1.

## 4. Other CLD accumulating models

### Section 6.7.4 short-arm variants

The source gives infinite families of finite arms, possibly making the
centre a tropical boundary point.  This supplies another accumulating
branch topology, but not an immediate hierarchy counterexample.  A finite
arm does not impose the constant-collar condition at minus infinity, so the
negative-slope germ above can be globally defined on that arm.  Once it is
globally defined, however, it already has a common domain; the specific
shrinking-domain obstruction disappears.  A new invariant would be needed
to prove non-approachability.

### Section 6.7.5 projective limits

CLD construct a tropical inverse limit from a projective system of
same-level tropical spaces with surjective transition maps inducing
isomorphisms on skeletal pieces.  Opens and smooth functions factor through
finite stages.  This is the most plausible source-legal setting for a
genuine rank obstruction, because a sequence of cylinder neighbourhoods may
use strictly increasing finite stages.

No concrete counterexample follows from factorization alone.  A first-stage
sequence is itself allowed to use a different finite stage at every index,
so countably many increasing stages can already occur at stage one.  A
stage-two candidate must additionally exhibit an order/positivity invariant
that all decreasing smooth approximations on one fixed cylinder satisfy and
that the proposed limit violates.  Neither CLD Section 6.7.5 nor the live
book supplies such an invariant.  Declaring the inverse-limit topology by
itself to be a counterexample would therefore be a gap.

## 5. Interaction with the fixed-core theorem

The production-verified fixed-core theorem is correctly conditional.  It
assumes that, for the decreasing family under consideration, row
approximations can be chosen on neighbourhoods of one common compact core.
The present star construction proves that this hypothesis is not a formal
consequence of taking stalks, and is not true for arbitrary preselected
rows.

It does not disprove the final sufficient criterion in that theorem.  The
criterion only asks for the **existence of suitable choices** for every
decreasing family.  For the zero family in the example, global constant rows
are suitable choices.

## 6. Literature/source search result

The local CLD 2025 text was checked at:

- Definition 8.1.1: minimal psh subsheaf and decreasing sequential limits;
- Lemma 8.1.4: transfinite filtration and eventual cardinal stabilization;
- Definition 8.1.13: locally approachable functions;
- Section 6.7.3: exact infinite-star topology, domains, smooth functions,
  constant full-branch collars, and finite slope balance;
- Sections 6.7.4--6.7.5: short-arm and projective-limit examples.

The live Chapter 15 and Chapter 72 correctly retain P07.1.  The existing
infinite-star and fixed-core packets contain no statement that a countable
family of arbitrary smooth psh germs has a common representative domain.
The new construction is therefore compatible with all live claims.

No local source or live-book result furnishes a concrete affine tropical or
analytic function of genuine CLD closure rank at least two.  The correct
status after this search is:

- **proved:** fixed neighbourhoods are not supplied by the sheaf/stalk
  formalism, even on the exact CLD infinite star;
- **proved:** shrinking native domains can occur in completely spurious
  first-stage presentations of a stage-zero function;
- **not proved:** `Psh_{X,2} != Psh_{X,1}` on any affine tropical space;
- **not found:** a natural analytic or tropical counterexample to P07.1;
- **remaining attack:** find a presentation-independent obstruction on a
  CLD Section 6.7.5 inverse limit, or prove a psh globalization theorem that
  supplies alternative fixed-core rows.

## 7. Editorial disposition

Do not integrate the candidate as a theorem before production Rethlas
verification.  If verified, its safest use is as an illustrating example
immediately after the fixed-core flattening result.  It should be described
as a quantifier/stalk warning, not as progress toward a negative answer to
P07.1 and not as a new open-problem retirement.
