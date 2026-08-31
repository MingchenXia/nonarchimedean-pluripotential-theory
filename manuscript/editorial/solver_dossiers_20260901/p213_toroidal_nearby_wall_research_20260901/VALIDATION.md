# Author validation and preservation

Date: 1 September 2026. Candidate only; independent and production gates open.

## Mathematical and finite checks

The complete proof includes the global closed-center choice, the actual
Rees-chart non-zero-divisor/cotangent check, the positive-support subtraction
termination measure, the retained-ray shear convention, weighted slice
normalization, whole closed-simplex face compatibility, residual coordinate
independence and proper-curve component argument. None of these is replaced
by the finite checks below.

check_construction.mjs is read-only. It ran 640 deterministic primitive-ray
cases in lattice dimensions 3,4,5,6 (relative dimensions 2,3,4,5), with
nonnegative original multiplicities including zero horizontal entries.
Across 25,581 extraction steps, with maximum 99 in a case, it checked exact
BigInt reconstruction, determinant plus/minus one, positive vertical center,
strict integer decrease and primitive termination. It then checked the
shear determinant and multiplicities exactly. A floating distance check
at budget 0.0001 supplements, but is not the proof of, the exact convergence
formula in Section 5. All checks passed.

The note has 17 distinct equation tags. The four initial authored text/code
files were checked for forbidden control bytes; zero were found. The final
freeze separately checks all authored text/code files. There is no TeX
compilation or PDF artifact claim.

## Prefreeze revisions and source inspection

The first completed draft was 22,510 bytes with SHA-256
1716b6028e839860307cae44b7afacadfc01288e20351908785c881a864ac194.
It was not frozen. Root then requested explicit residual-coordinate and
series-tail reasoning on faces, and a direct cotangent proof of regularity.
Those changes are disclosed in SOURCE_LEDGER.md; the final construction
check was rerun and records the updated note hash in CONSTRUCTION_CHECKS.json.
There is no claim that the first draft had passed independent review.

BFJ and GRW source hypotheses were read directly. Eleven complete source
pages were rendered and viewed. Rendering exited zero with the Fontconfig
cache warnings recorded verbatim in SOURCE_QA.json; no cache permissions
were changed. Owned temporary PNGs were removed after recording hashes.
No original/frozen source or manuscript file was changed.

## Freeze and gates

MANIFEST.json pins seven packet files and four local primary-source files,
for 11 entries. SHA256SUMS includes those entries and the manifest, for
12 checksums. The read-only checker verifies the freeze when these files
are present. It reports byte mismatches as failures.

This is a new authored research candidate. No independent PASS, production
submission, integration authorization, live chapter/inventory mutation,
git action or permission bypass is included. The exact scoped construction
still requires independent mathematical review and the unchanged production
gate before any promotion. Wider mixed-characteristic scope, arbitrary
model capture and current consequences are not established.
