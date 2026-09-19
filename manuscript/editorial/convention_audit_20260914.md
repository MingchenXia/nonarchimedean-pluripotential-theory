# Cross-chapter convention audit

Date: 14 September 2026.  Scope: every file reachable from `book.tex`.
Method: enumerate each site that fixes or uses a normalization, compare
against the declaration in `frontmatter/conventions.tex` and
`appendices/appJ_normalizations.tex`, and re-derive the disputed cases.
No LaTeX build was run.

The motivation was that this book's subject is a dictionary between five
theories, so convention drift corrupts results silently and across chapter
boundaries.  Two live problems were found in eight conventions; both are
fixed.  The other six are consistent and are recorded here so that a future
pass does not re-litigate them.

## Finding 1 --- model-function sign in Chapter 33 (fixed)

`frontmatter/conventions.tex` fixes the sign by
`phi_D = log|O(D)| = -log|f| = v_x(f)`, so effective vertical divisors give
nonnegative model functions, and `(60.4)` states the same as
`phi_D(v_E) = b_E^{-1} ord_E(D)`.  Chapter 46 derives the special-fibre
case explicitly: `phi_{X_0}(v_E) = b_E^{-1} ord_E(X_0) = 1`.

The proof of `lem:ch33-effectivity` wrote
`phi_D(v_E) = sigma(v_E)(D) = -b_E^{-1} ord_E(O_X(-D))`.  Read the way the
same proof uses `ord_E` two lines earlier --- applied to an ideal, where
`ord_E(a) >= 0` characterizes `a` inside the structure sheaf --- this gives
`-b_E^{-1} ord_E(D)`, the wrong sign.  It then contradicts three things at
once: the lemma's own conclusion that `D` is effective exactly when
`phi_D(v_E) >= 0`, the same criterion as used in Chapters 32, 34 and 35, and
`(60.4)`.  The expression is now written as `b_E^{-1} ord_E(D)`, with the
two senses of `ord_E` --- of an ideal and of a divisor --- distinguished
explicitly, and the effectivity chain spelled out.

## Finding 2 --- the radial parameter is absent from Appendix J (fixed)

`conventions.tex` says Appendix J "records the conversion used in each
comparison theorem", and Appendix J is otherwise thorough.  But neither its
ray section, nor its translation table, nor its unit tests mentioned the
radial parameter, even though the book uses two of them:

- `t = -log|zeta|^2`, the squared-norm default, declared in Chapters 52, 56
  and 71;
- `s = -log|t|`, the ordinary-norm parameter, used in Chapters 65, 66, 67
  and 68 where the base coordinate is itself called `t`.

They differ by a factor of two, `t = 2s` and `phi_t = 2 psi_s`.  The book
does handle this --- Chapter 65 has a dedicated factor-two firewall,
`sec:rf-factor-two-firewall`, and Chapters 66 and 68 convert explicitly ---
but the conversion lived only in scattered chapter-local remarks, not in the
appendix designed to hold it.  This is the convention with the book's only
recorded error history: the Chapter 67 scaling ledger stated its factor `m`
in the `v(t)=1` normalization when it belongs to `v(s)=1`, contradicting its
own item (1).

Appendix J now declares the conversion as `(J.35)`, carries a
`Radial parameter` row in the translation table, and has a ninth unit test:
halving the radial parameter must leave a slope unchanged and halve a
weight.  Its equation tags were renumbered to stay sequential.

## Verified consistent --- do not re-open without new evidence

- **Special-fibre test.**  `phi_{X_s} = 1` under `v_K(pi) = 1`, stated
  identically in Chapters 18, 20, 24, 30, 31, 32, 33, 46, Appendices J, K, L
  and the conventions chapter, and derived in Chapter 46.
- **Discretely valued normalization.**  `v_K(varpi) = 1` throughout
  Chapters 30 and 33.
- **Complex Poincare--Lelong.**  `ddc = (i/2pi) partial bar-partial` with
  `ddc log|f|^2 = [div f]`, and the half-logarithm form beside it.
- **CLD Poincare--Lelong.**  `d'd''log|f| = delta_{div f}` in Chapters 14
  and 15, matching `(J.17)`, with `d'd''v(f) = -delta_{div f}` as the
  companion.
- **Lelong-number normalization.**  `nu_E(log|f|^2) = ord_E(f)`, stated
  identically in Chapters 56, 57 and 60, and implied by the complex
  Poincare--Lelong row.
- **Monge--Ampere mass.**  `MA^u = V MA` declared in Chapter 30, used in
  Chapters 46--50 and 64, with Chapter 64's normalization laboratory and
  Appendix J's total-mass unit test agreeing.
- **Reduced versus total discrepancy.**  `A^NA = A^tot - 1` on the
  `X x C` slice, with Appendix J warning against identifying either with the
  homogeneous cone function `A_X`.  Chapter 62's related wording was
  corrected separately in the 14 September pass.

## Not covered

Lagerberg orientation and toric coordinate conventions were spot-checked
against their Appendix J rows but not exhaustively traced.  Nothing here is
a substitute for a build: the audit is a source-text comparison, and
Appendix J's own tag renumbering in particular should be seen rendered.
