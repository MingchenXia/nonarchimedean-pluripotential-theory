# Validation record

Date: 8 September 2026.

The original 31 August checker failed before its own checks because the
historical `/private/tmp` snapshot no longer exists.  The failure is recorded
as an input-path failure, not converted into a pass.

The replacement checker was run from this directory with
`node check_current_candidate.mjs`.  It returned
`PASS_REPRODUCIBLE_FROZEN_INPUTS_ONLY`: all eight bound files had their
recorded SHA-256 values, the P14.3 packet had 10 unique labels and 10 internal
reference uses, and it had no duplicate or unresolved internal references.

The unchanged frozen P14.3 packet was then compiled in LaTeX draft mode in a
new disposable output directory.  The sequence was two draft TeX runs around
BibTeX and one final draft TeX run, with the source directory supplied only as
the bibliography search path.  The final log had SHA-256
`1848b83a7e5e895d0605d82b1f5f0c863ad8577535c028be605f19220100ca14` and
contained no warning, error, overfull/underfull-box, undefined-reference,
undefined-citation, or multiply-defined-label diagnostic.  Draft mode wrote
no PDF.

This is mechanical and reproducibility evidence only.  It does not validate
the new dominated-divisorial theorem mathematically, transfer any historical
review to a changed theorem, authorize a live integration, or retire P14.3.
