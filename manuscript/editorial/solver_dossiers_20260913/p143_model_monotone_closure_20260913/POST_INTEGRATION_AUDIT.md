# P14.3 post-integration audit

Date: 2026-09-19

## Exact integration

- The theorem block in `STATEMENT.tex` is byte-for-byte identical to the
  integrated theorem `thm:p143-mp-section` in Chapter 71.
- `PROOF.tex` is byte-for-byte identical to the corresponding integrated
  proof in Chapter 71.
- The scope remark is identical in the packet and Chapter 71.
- The Chapter 72 account and the open-problem inventory both record the
  endpoint repair, the new hash-bound verdict, and the still-open reverse
  DXZ-to-MP direction.

## Structural checks

- Build closure: 282 files.
- Labels: 10986.
- Multiply defined labels: 0.
- Dangling references: 0.
- The only tag-sequence report is the already documented Chapter 71 gap
  between manual tags 71.32 and 71.36; it is not a missing reference.
- `git diff --check`: clean.

## Scope conclusion

The integrated theorem proves that every MP potential has a unique DXZ
preimage under the raw transform, conditionally on P14.2 all-point upper
semicontinuity.  It supplies a canonical order-preserving and
order-reflecting section.  No statement in the packet or integration claims
surjectivity in the opposite direction, so P14.3 remains active.
