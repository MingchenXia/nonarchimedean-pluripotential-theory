# Local preflight — P14.2 V6 repaired source-stage candidate

This record describes reproducible local evidence for the exact frozen tree
`/private/tmp/p142_hostile_repair_v6_20260909`; it is not a smoke receipt or
production result.

- `shasum -a 256 SHA256SUMS` returned
  `3511b635413d7ace9013edd278216017096d7359ac5dd2b3155cbf179c83e97f`.
- `shasum -a 256 -c SHA256SUMS` verified all 57 rows after the final test run.
- With `PYTHONDONTWRITEBYTECODE=1` and the pinned verification Python,
  `python -B -m unittest discover -s tests -q` completed after the final freeze:

  ```
  Ran 179 tests in 24.334s
  OK
  ```

- The direct integrity command executed `check_manifest`, `check_catalog`,
  `check_release_pins`, and `check_code_contract` from the exact candidate and
  printed `PASS_RELEASE_INTEGRITY_GATES`.
- The root and directories are mode `0555`; staged regular files are mode
  `0444`. No bytecode cache, artifact, smoke output, symlink, or special file
  is in the staged release tree.

The full release-checker main routine is intentionally not claimed here,
because it includes the downstream smoke validation gate.
