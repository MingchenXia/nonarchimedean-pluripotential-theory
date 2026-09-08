# P14.8 Cantor-index repair validation

## Exact replay

The v2 proof postimage has SHA-256

```text
adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9
```

Applied with `git apply --unidiff-zero` to a fresh v2 candidate copy,
`V2_TO_V3.patch` produces a proof with
SHA-256

```text
94e6efde9dc8e14bb90ae8b63a3cfa0b0f53b024210e570e29b0b67bd450b47b
```

The only changed proof block is the Cantor initialization at v2 lines 35--46.
The v3 arithmetic is explicit:

- `ell_0=1` and `ell_m=exp(-4^m)` for `m>=1`;
- `2 ell_1=2 exp(-4)<1`;
- for `m>=1`, `2 ell_(m+1)/ell_m=2 exp(-3*4^m)<1`;
- the `m=0` capacity summand is zero and the remaining summands are `2^m`,
  so their series diverges.

Thus the stated generalized Cantor construction has the required initial
normalization, two-child geometry, nonatomic limit measure, and polar-set
criterion with no change to the later Green or mass argument.

## Isolated build

Starting from a fresh v2 candidate copy, the patched proof was compiled with

```text
SOURCE_DATE_EPOCH=1788235200 FORCE_SOURCE_DATE=1 TZ=UTC
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build completed with exit status zero.  The resulting four-page PDF has
213,509 bytes and SHA-256

```text
48331cb676cc0087b9d6c5ae859efae4c7a0c06b3f611955f17f19b204e57c1e
```

The final log has SHA-256

```text
466d8e4a11e7385890bc2c623541f090c88cdcee733fbf0c78f4bec7ae7c6247
```

and contains no TeX error, warning, unresolved reference/citation, or box
diagnostic.

## Boundary

This is a local proof repair only.  It must receive a new independent and
source-complete review on the exact v3 bytes before any P14.8 integration or
status change.
