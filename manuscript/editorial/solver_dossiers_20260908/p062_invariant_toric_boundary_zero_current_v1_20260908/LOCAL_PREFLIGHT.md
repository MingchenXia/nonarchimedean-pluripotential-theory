# Local preflight — P06.2 invariant split-toric boundary subcase

Completed before external review:

1. `latexmk -pdf -interaction=nonstopmode -halt-on-error SYNTAX_CHECK.tex`
   produced `SYNTAX_CHECK.pdf` successfully.  The standalone file has no
   bibliography, so its six citation warnings are expected and not proof
   errors.
2. The primary BGJKK25 PDF was rechecked at its exact load-bearing locations:
   equation (5.5) (p. 29); Remark 5.3.8 and Proposition 5.3.10(iv) (pp.
   29--30); Proposition 2.3.4 (pp. 11--12); the proof of Theorem 3.1.4
   (pp. 14--15); and equation (3.11) (p. 18).
3. The direct current calculation in the proof of Proposition 5.3.10(iv)
   uses continuity, factorization, canonical-skeleton support, and (5.7);
   its psh hypothesis is used only later to infer positivity.  The candidate
   invokes only that current calculation.
4. The retained endpoint is local: `prop:ch18-harmonic-basic` supplies
   harmonicity after local CLD smoothness, and GR25Classical Theorem 4.3 is
   applied to both signs.  No arbitrary-germ or non-invariant claim is made.

The first model-backed review archived in `VERIFICATION_RUN_V1_20260908`
returned `wrong` with zero mathematical critical errors and one provenance
gap: the proof invoked the internal live-book harmonicity proposition without
an authenticated dependency.  The frozen V1 request and response are kept as
the audit record.

The revised candidate removes that dependency.  It directly writes the
affine functional annihilating `sigma` as a real linear combination of
characters in `M intersect sigma^perp`; each is an analytic unit on the
affine toric chart.  Gubler--Rabinoff Proposition 4.2(2),(3) then gives the
two-sided classical psh conclusion directly.

The source closure was strengthened once more after inspecting the primary
Gubler--Jell--Rabinoff source, Definition 7.2 (p. 40): on a good strict
domain, the two-sided semipositivity of a real-PL function is exactly GJR
harmonicity.  With the good-strict domain hypothesis made explicit in the
statement, Gubler--Rabinoff Theorem 4.3 promotes the already proved two-sided
classical psh conclusion to that semipositivity.  The new exact bytes again
pass the standalone TeX syntax check.

The approved dependency-closed V3 packet was submitted with
`VERIFIER_CONTEXT.tex` as its exact proof dependency.  It returned final
`correct` on 9 September 2026 for
`pi_30ec53e8836ba1d2b08fdf64`, with zero critical errors and zero gaps.  The
archived SHA-256 values are:

```text
statement  8d69697806c33d59531b5d3247a2f9e0c1d07e313d329c15a2432646134a544a
proof      c17e99ebb54f45003d78f55670a978092294b44a7c4536b78d7207ec52cfda85
context    d05e43c19e5c5444baa0718078da4315c86394e528ffedee0a8ce62b29785b4d
request    6fc001dd8058960a93a53b09c280d802db2513cb373b1d28953b1173f5d2bd5d
response   5d934f2c8fc9017ce73234c76b58fae1029b1c5c5a9f8cff11b4667d7bf36d2b
headers    8d4e67bd07bc2666c6311f625bd7447be99abf95eed6b0826c5306d8e19956f6
```

The V2 directory records the authorization-gate outcome; there is no V2
verifier verdict.  The verified V3 theorem is now integrated as a narrow
live-book P06.2 extension, without retiring the open atom.
