# Hostile audit: P11 moving-center Radon--Riesz counterexample

Date: 25 August 2026

Audited exact files:

- `p11_bj_radon_riesz_p2_counterexample_statement_exact_20260825.tex`;
- `p11_bj_radon_riesz_p2_counterexample_source_aware_proof_exact_20260825.tex`;
- `tmp/pdfs/bj22_global_trivial.pdf`.

No live chapter was edited.  The original malformed packet was not sent.
After the TeX/hash repair, production round one was sent and rejected as
recorded below; its artifacts are preserved.

## Verdict

**Mathematical construction: PASS after the divisor-support repair below.**

**Exact frozen round-two packet: PASS.**  Guarded production run
`20260825T042017Z_948e2b7cde7d`, item
`pi_0b7126d51ccabcab1920a96d`, returned `final/correct` under
`gpt-5.6-sol`/`xhigh`, with 0 critical errors and 0 gaps.  Both process
guards completed and the wrapper returned code 0.

The moving-center construction is a valid counterexample to the implication
asked about in Boucksom--Jonsson, Question 11.16.  The exhaustion and strong
gap checks pass as originally written.  The initial hostile audit did not
detect a cancellation flaw in the weak-convergence paragraph; guarded
production run `20260825T040646Z_948e2b7cde7d` correctly rejected it.  The
divisor-support argument below repairs the proof.  The earlier exact bytes
also had a false dependency hash and invalid TeX delimiters; those defects
were repaired before the rejected run and remain documented below.

## 1. Weak convergence: PASS after repair

Let `r=ord_D(f)` and write `div(f)=rD+E`, with `D` not a component of `E`.
The intersection `D ∩ Supp(E)` is finite.  At every closed point `p` outside
that set, a local equation `x` of `D` gives `f=x^r u` with
`u in O_{X,p}^times`.  The exceptional-divisor valuation of the blowup at
`p` has value one on `x` and zero on `u`.  Hence

```text
ord_{p_j}(f)=r=ord_D(f)
```

eventually for each fixed `f`.  Pairwise distinctness of the `p_j` is exactly
what makes the sequence eventually avoid each finite exceptional set.

The rejected residue-only argument was insufficient.  For example, locally
with `D=(x=0)`, the rational function `(x+y^2)/y^2` has residue one on `D`,
but is not a unit at `(x,y)` and has exceptional valuation `-1`.  Passing to
the support of the full residual divisor prevents this cancellation.

Boucksom--Jonsson, Section 1.1.1, defines `X^val` with the topology of
pointwise convergence on `k(X)^times`; Section 11.3 calls the topology on
`X^lin` inherited from `X^an` the weak topology.  Thus the displayed eventual
equality proves the required weak convergence.  No common birational model or
resolution is used.

## 2. Exhaustion normalization: PASS

Definition 1.26 gives

```text
T_L(v)=sup {m^{-1} v(s) : m>=1, 0!=s in H^0(X,mL)}.
```

Lemma 4.46 identifies this with the Alexander--Taylor exhaustion
`T_omega({v})` when `omega=c_1(L)`.

For `L=O_{P^2}(1)`, the multiplicity at a smooth point of a nonzero degree
`m` homogeneous polynomial is at most `m`, with equality for `X_j^m`.
The exceptional divisor of the blowup at `p_j` computes this multiplicity,
so `T_omega(ord_{p_j})=1`.  The multiplicity of the fixed line `D` in a
degree `m` polynomial is likewise at most `m`, again with equality for
`X_j^m`, so `T_omega(ord_D)=1`.  There is no missing volume, degree, or
polarization factor.

## 3. Strong gap from Lemma 11.7: PASS

Boucksom--Jonsson equation (11.4) defines `d_infty`, and Lemma 11.7 gives the
exact section formula

```text
d_infty(v,w)=sup_{m>=1, 0!=s in H^0(X,mL)}
             m^{-1}|v(s)-w(s)|.
```

Choose a line `H_j` through `p_j` distinct from `D`, with defining section
`Y_j`.  Then the exceptional valuation satisfies `ord_{p_j}(Y_j)=1`, while
`ord_D(Y_j)=0`.  The `m=1` term therefore gives
`d_{infty,omega}(v_j,v)>=1` for every `j`.  Together with weak convergence
and the constant exhaustion values, this directly negates the
characterization proposed in Question 11.16.  Section 11 assumes only that
`X` is irreducible; the cited definition and lemmas impose no
characteristic-zero hypothesis, so the `P^2` construction works in arbitrary
characteristic.

## 4. Historical exact-byte blockers (repaired)

### 4.1 False local-source digest

The proof and the existing dossier claim that
`tmp/pdfs/bj22_global_trivial.pdf` has SHA-256

```text
50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948.
```

The actual SHA-256 of that named local file is

```text
8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52.
```

The latter digest agrees with the pre-existing repository checksum ledger
`manuscript/editorial/rethlas_packets_20260824/SHA256SUMS`.  The PDF pages
were also visually inspected at Definition 1.26, Lemma 4.46, Lemma 11.7,
and Question 11.16; their statements support the argument.

### 4.2 Invalid TeX delimiters

Both frozen TeX files systematically use literal parentheses where math
delimiters are required, for example

```text
Let (k) be ...
fix a line (D\subset X).
Choose ... (p_j\in D(k)).
```

This is not merely cosmetic: `\subset`, `\in`, subscripts, superscripts,
and similar commands occur outside math mode.  A minimal `pdflatex`
compilation of the exact statement stops at the line containing
`(D\subset X)` with

```text
! Missing $ inserted.
! ==> Fatal error occurred, no output PDF file produced!
```

## 5. Round-two preflight

The three repairs above are complete.  A clean minimal wrapper containing
the exact statement and proof compiled twice with `pdflatex`; the final pass
had no fatal error, undefined control sequence, or undefined reference, and
the rendered two-page PDF was visually inspected.  The round-two request was
also checked byte-for-byte against both frozen TeX files before submission.

The original malformed statement had SHA-256
`f421c11237ddb1124c7520e00b1a435e9e4d28c012fa0688c11e7c9ffbae68fe`;
the original malformed proof had SHA-256
`bbb7bd5dbc571ba3deaeac5feb6aff5997a2d695c795b8ba941eedab776c690a`.
Those hashes identify the original malformed packet before the first repair.
The first minimally formatted proof was separately frozen and rejected in
production; its full response and guards are preserved.  The current
round-two frozen hashes are:

- statement: `948e2b7cde7dc32411bea2acb46f6fa821e65afaa8cb8a546ec01759416cfb6c`;
- proof: `46875db7cbe7869e95195f6345989df85031c82d0b52df298e0427515100e959`;
- exact request: `882f866c365ddf88206c9d1df32a7b399e2de5f9deaf64bdc10eec689e3144e0`.

The API response, aggregate manifest and verification, item verification
and log, both process guards, and an exact-hash production receipt are
preserved under `manuscript/editorial/rethlas_receipts_20260825/`.  Round
one's `final/wrong` artifacts and superseded bytes remain separately
preserved.  No live file was edited.
