# P07.1 infinite-star × infinite-collar product: repair ledger

## Dependency-closed run 1

- Verdict: `wrong`.
- Checked item: `pi_dddabcb5edbe492cf0dc8342`.
- Critical error: the moving-clamp construction began at `n=1`, although
  `-n` need not lie in the original finite tail and the interval `I_n` could
  be empty.
- Gap: the full-star-endpoint argument did not separately handle a target
  which is identically `-infinity` on the connected finite product stratum.

## Repairs

1. Choose `N` with `-N<r'`, work only with `n>=N`, explicitly prove
   `kappa_n([-infinity,r'))` lies in the nonempty interval
   `I_n=[-n,r'+2 delta]` and below the original upper bound, and reindex at
   the end.
2. At a full star endpoint, apply the extended-real convexity dichotomy
   first.  Exact traces plus constant approximants handle the identically
   `-infinity` case; truncation and uniform smoothing are used only in the
   finite case.

The first request and exact response remain archived in
`model_run_dependency_closed/`.

## Repaired dependency-closed run

- Verdict: `correct`.
- Checked item: `pi_6e42f81c8aed3484a0f4ce21`.
- Critical errors: `0`.
- Gaps: `0`.
- The repaired exact request and response are archived in
  `model_run_repaired_dependency_closed/`.

## Typography-corrected final run

- A page-image audit found that two displayed spacing commands had lost
  their TeX backslashes, printing literal `qquad`/`quad` text.
- The mathematical content was unchanged, but the proof SHA-256 changed to
  `d915ae5a407e65ef82a9eb02d205c0cd3e8871e6ba0c8dfec94b182d2edff49c`.
- The exact corrected packet was therefore submitted again.
- Verdict: `correct`.
- Checked item: `pi_7f64cae4c772b9edf730c3eb`.
- Critical errors: `0`.
- Gaps: `0`.
- The final exact request and response are archived in
  `model_run_typography_corrected_dependency_closed/`.
