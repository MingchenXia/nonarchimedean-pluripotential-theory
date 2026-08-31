# Revised2 change and dependency ledger

Date: 31 August 2026. Status: isolated author revision, exact independent and production review pending.

## Frozen sources

The unchanged source bytes are recorded in `MANIFEST.json`. The previous assembly is the parent directory; it remains frozen. The underlying weighted revised1 and real-class F revised1 packets are not edited. The separate pedagogy findings are in the sibling `p081_ch29_ch31_pedagogy_review_20260831/PEDAGOGY_FINDINGS.md`.

## Mathematical repair in Ch31

The real-form reverse direction under `eq:curve-slope-criterion` is expanded. On the actual determining model, represent the real numerical form by finitely many real multiples of model line-bundle classes. On local frames form the real lisse weight H from their rational formal weights and the actual rational model potential.

Real linearity gives equality of signed curvature measures only. Frame changes add harmonic analytic-unit logarithms; another representative of the same numerical model class leaves every component degree and hence the local curvature current unchanged. These explanations make the local computation independent of the chosen presentation without pretending the real form is one metrized line bundle.

The positivity direction is now explicit: downstairs weighted positivity makes the local lisse weights subharmonic by Thuillier Theorem 3.4.12(ii); scalar pullback preserves subharmonicity by Corollary 3.4.5; the upstairs component formula then gives nonnegativity of each individual component degree on a common determining semistable model. Real numerical nefness reflects by the degree/projection argument already proved in Ch29. The forward direction uses ordinary scalar pushforward only to preserve positivity. No individual lifted sign is inferred from a positive pushed-forward sum.

This is a proof expansion for the same actual-model criterion, not an enlargement to arbitrary BFJ-psh functions. In particular, the factorization through the original skeleton remains an explicit assumption.

## Worked diagnostics

1. The new nonsplit blowup example starts with a closed point of separable residue degree r greater than one on the special fibre of the projective line over a complete DVR. The exceptional component has constant field of degree r; the original component has constant field degree one; their node nevertheless has the same weight r at both endpoints. For the vertical bundle O(E), the component degrees over the base residue field are r and minus r, the model potential has endpoint values zero and one, and its weighted slope masses agree exactly. The degree over the exceptional component's own constant field is minus one, so the calculation exhibits the missing factor rather than just restating the convention. The unramified splitting check is also given. This is a signed-curvature normalization example, not a semipositive degree-zero existence claim.

2. The two-edge graph of analytic lengths one and square root of two and unit conductances has normalized equation ΔU=δ_y−δ_q. The slopes are square root of two minus two and one minus square root of two. Integral masses therefore do not force rational slopes. The example is explicitly an abstract graph calculation, not a claimed realization over any specified field.

Both examples are new mathematical exposition and need exact independent and production review.

## Pedagogy and notation

- Ch29 distinguishes real coefficients of the background model class from rational model competitors before the theorem; equality to zero is numerical model equality.
- A proof roadmap separates the real-class envelope, elementary Green lemma, point reference, equation solution, and downstream model-reference specialization.
- The completed algebraic closure is Ω rather than the competing graph-function symbol F or the confusing C_K.
- Thuillier-lisse and ordinary CLD-smooth are distinguished; the local-current cancellation in the point-reference construction is made explicit.
- The atomic Green approximants are finite linear combinations of kernels, and local weights h_j and h are introduced before their curvature comparison.
- A bridge explicitly separates the real piecewise affine approximation from later rational formal approximation.
- Ch31 explains c_e versus the whole-edge matrix coefficient c_e/ℓ_e. Subdivision preserves the analytic coordinate and conductance, while the new lengths sum to the old length.
- The node parameter is α and the discrete exponent is n. The solution proposition now independently fixes q.

## Proof dependency direction and exclusions

The real-class envelope uses its own rational chord construction and finite normal descent. It does not depend on the weighted equation solution.

The weighted equation uses the elementary Ch31 Green lemma and the point-reference construction, followed by the accepted P063 and corrected positive P081 inputs only over the completed algebraic closure and explicit descent of actual rational approximants. The Green lemma itself does not depend on any analytic existence theorem.

The Ch31 model-reference proposition is downstream of the completed Ch29 equation theorem. The expanded local real-form criterion uses the already established model-curvature comparison and the real nef-reflection argument, not the downstream equation proposition.

Preserving the label `eq:curve-slope-criterion` does not validate older callers with broader hypotheses. Parent/root owns the separate Ch23 consumer repair. The independently reported Ch26/Ch28 weighted-energy mismatch remains a separate integration issue. No file in any of those chapters is edited here.

## Mechanical validation only

All previously existing labels from both live chapters and the frozen first assembly are retained. The standalone fragments must compile in draft mode with no unresolved references or citations. The exact combined diff must pass `git apply --check`; it must not be applied. These checks are byte/syntax/assembly checks, not mathematical verification or production acceptance.
