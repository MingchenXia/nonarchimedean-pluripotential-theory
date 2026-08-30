# Precision repair ledger

This frozen candidate is derived from the independently audited endpoint-only
dossier.  The independent receipt is
`../p062_annulus_endpoint_only_dossier_20260830/INDEPENDENT_HOSTILE_AUDIT.md`,
SHA-256
`02f11da24f3003d489d7a8c64157a813a9c8c97e52ce28996e8ea011d13dc297`.
Its verdict is PASS for the one-dimensional half-closed and closed annulus
argument only.

The three requested precision edits are implemented as follows.

1. **Closed tube stated exactly.**  The proof defines
   `bar(X)_y={|P(T)|<=S}` and proves, from coefficient bounds and strict
   dominance, that it is the entire closed disc `{|T|<=s}`.  The finite map
   from this compact disc is used only for topology and local degrees.
2. **No closed trace of an undefined function.**  The proof never extends `h`
   to `bar(X)_y\A`.  For `q<S`, all points over the target Gauss point lie in
   the open tube `X_y subset A`.  A compact-complement argument for the finite
   map forces those fibres into every neighbourhood of `eta_s`; continuity of
   `h` on `A` then gives the trace limit directly.
3. **No unnecessary one-branch assertion.**  The proof merely observes that
   `X_y` is ambient open and contained in the endpoint circle, hence in the
   absolute interior.  It explicitly says that no identification with one
   specified residue branch is needed.  No connectedness claim is used.

The exact theorem packet retains arbitrary complete non-Archimedean `K`, a
nontrivial valuation, and `r,R in |K^x|`.  It asserts only the three
one-dimensional annulus variants.  Product, polycylinder, and
higher-dimensional endpoint assertions are explicitly excluded.
