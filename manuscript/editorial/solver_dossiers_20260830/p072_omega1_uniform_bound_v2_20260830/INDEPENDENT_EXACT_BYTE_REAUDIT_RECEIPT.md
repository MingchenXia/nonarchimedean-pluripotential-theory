# Independent exact-byte re-audit: P07.2 v2

Date: 2026-08-30 (Asia/Shanghai)

## Frozen mathematical identity

- `statement.tex`:
  `37ca59d5bd863e6af4d46ed18d1cf1c4cfcdb45aeeac1f25631fa582750985f8`
- `proof.tex`:
  `9cb9222dbd307d4ff21c0043951a5c0b4a65dec645012fe5e5584b86808a6b5b`

These hashes were recomputed before and after the re-audit and agree with
the requested v2 identities.  Neither file was modified.

## Verdict

**Pass: ready for production Rethlas submission of these exact mathematical
bytes.**

- Critical mathematical errors: **0**.
- Gaps: **0**.

This receipt is an independent source audit and compilation check, not a
production Rethlas verdict.

## Exact v1-to-v2 comparison

The complete unified diff against the audited v1 payload shows only the
following changes:

1. the opening comment in each mathematical file now identifies v2;
2. `statement.tex` deletes the under-specified generalization to an arbitrary
   sheaf hierarchy and replaces it with the explicit scope firewall that no
   finite, fixed countable, or first-stage bound is claimed;
3. `proof.tex` deletes the corresponding abstract-generalization paragraph
   and retains the same scope firewall.

All CLD-specific hypotheses, displayed claims, ordinal arguments, compact-core
construction, sheaf gluing, minimality argument, and continuous-hierarchy
argument are otherwise byte-for-byte unchanged.  Thus the sole v1 gap has
been removed without changing the already-audited principal theorem.

## Rechecked mathematical obligations

1. CLD Lemma 8.1.4(c) gives the asserted sheaf-theoretic local union at the
   limit ordinal \(\omega_1\), equivalently the ordinary union on every
   stalk; no fixed earlier stage on an arbitrary open set is claimed.
2. Local compactness and Hausdorffness from CLD Section 3.1.1 give a compact
   core \(K\) with \(x\in K^\circ\subseteq K\subseteq U\).
3. For each row, a finite cover of \(K\), a finite maximum of local ranks,
   monotonicity, and the sheaf axiom give one rank \(\beta_n<\omega_1\) on a
   neighbourhood containing the same \(K\).
4. The one open set \(V=K^\circ\) works for all countably many rows; no
   countable intersection of neighbourhoods occurs.
5. \(\alpha=\sup_n\beta_n<\omega_1\), and
   \(\alpha+1<\omega_1\); the successor-stage definition therefore places
   the decreasing limit in stage \(\alpha+1\) locally.
6. This proves closure of \(\operatorname{Psh}_{X,\omega_1}\) under the
   generating decreasing-limit operation.  Minimality of
   \(\operatorname{Psh}_X\) and CLD's reverse transfinite inclusion give
   \(\operatorname{Psh}_{X,\omega_1}=\operatorname{Psh}_X\).
7. CLD Proposition 8.1.11 at \(\gamma=\omega_1\) gives the continuous
   identity exactly as stated.
8. The result supplies a universal, space-independent ordinal bound for
   every affine \(G\)-tropical space.  Under the inventory's current literal
   wording it is sufficient, after production verification, to retire P07.2.
   It does not establish first-stage collapse and does not retire P07.1.

## Closure of the v1 gap

The v1 audit's only gap concerned an undefined class of arbitrary sheaf
hierarchies and omitted structural hypotheses for a countably-ary successor
operation.  V2 makes no such assertion.  Both the statement and proof now
end with a precise limitation to the named CLD hierarchies.  The gap is
therefore closed, rather than merely deferred.

## Independent compilation

Copies of the exact v2 statement, proof, and wrapper were compiled only in

`/private/tmp/p072_omega1_v2_exact_audit_20260830_reaudit`

using

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error minimal_compile.tex
```

The build completed in two resolved passes and produced a three-page PDF.
The final log contains no undefined citation, undefined reference, multiply
defined label, or TeX error.  The independent PDF SHA-256 was

`f1fb5cf5d3494f22f9ce8528b60e33c88a8fed4d5df27b603848d5589810379d`.

No existing package artifact was compiled, rewritten, or deleted during
this v2 re-audit.  The only addition to the package is this receipt.
