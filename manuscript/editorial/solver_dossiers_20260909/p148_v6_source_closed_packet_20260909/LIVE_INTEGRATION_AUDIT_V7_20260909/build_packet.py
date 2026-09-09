#!/usr/bin/env python3
"""Materialize the fixed-source P14.8 V7 exact-live audit packet.

The packet does not edit the manuscript.  It binds the source-bound V6
dichotomy to exact line ranges in the current Chapter 51 and Chapter 72
sources and records hashes for every input used in that comparison.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


AUDIT = Path(__file__).resolve().parent
REPO = AUDIT.parents[4]
V6 = AUDIT.parent
CH51 = REPO / "manuscript/parts/part5/ch51_complex_prerequisites.tex"
CH72 = REPO / "manuscript/parts/part6/ch72_major_open_problems.tex"
INVENTORY = REPO / "manuscript/editorial/open_problem_atomic_inventory_20260824.md"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lines(path: Path, start: int, end: int) -> str:
    source = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(source[start - 1 : end]) + "\n"


def git_head() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
    ).strip()


def write(name: str, text: str) -> None:
    (AUDIT / name).write_text(text, encoding="utf-8")


def main() -> None:
    head = git_head()
    sources = {
        "chapter51": CH51,
        "chapter72": CH72,
        "inventory": INVENTORY,
        "v6_statement": V6 / "STATEMENT_V6.md",
    }
    pins = {
        "git_head": head,
        "files": {name: {"path": str(path.relative_to(REPO)), "sha256": digest(path)}
                  for name, path in sources.items()},
        "ranges": {
            "ch51_scope_and_comparisons": [96, 166],
            "ch51_strong_openness": [1553, 1638],
            "ch51_i_preorder": [3210, 3237],
            "ch51_i_envelope_and_projection": [3290, 3461],
            "ch51_npp_bidegree_one": [2112, 2154],
            "ch51_npp_ledger": [2168, 2185],
            "ch51_cantor_family": [3780, 3885],
            "ch72_p148_status": [2861, 2892],
            "inventory_p148_status": [892, 929],
        },
        "v6_statement_sha256": "4e4256d738ec65dea040e82b3b40bffb233197e9f466c07166760196cc13c04e",
    }
    write("RELEASE_PINS.json", json.dumps(pins, indent=2, sort_keys=True) + "\n")

    statement = r"""This is a conditional exact-text comparison, not a new
mathematical theorem or an assertion that this prompt authenticates a Git
revision.  Given that the source excerpts reproduced in this proof context
are exact current Chapter 51/72 and inventory texts, those excerpts establish
precisely the two assertions in the supplied frozen P14.8 V6 statement:

1. For a realizable \(\mathcal I\)-class \(d=[\varphi]_{\mathcal I}\) in
   \(\operatorname{{PSH}}(X,\theta)\),
   \(\mathcal R_\theta(d)=P_\theta[\varphi]_{{\mathcal I}}\) is well defined
   and is the unique normalized \(\mathcal I\)-model representative in that
   class, without a positive-nonpluripolar-mass hypothesis.
2. On \(\mathbf P^1\), the live polar-Cantor family \(\varphi_s\),
   \(0\le s\le1\), is contained in one \(\mathcal I\)-class and has raw
   nonpluripolar mass \(1-s\).  Hence its endpoint of raw mass zero has the
   canonical normalized \(\mathcal I\)-model representative \(0\), of mass
   one; neither a raw representative nor its raw mass descends to the
   \(\mathcal I\)-quotient.

The comparison asserts no realization result for arbitrary formal ideal data,
no all-semivaluation formula, no DXZ terminal-slice result, and no extension
to a different setting.  The supplied Chapter 72 and inventory excerpts keep
P14.8 open; this review does not retire it.  The separately generated
`RELEASE_PINS.json` is provenance metadata for a local integrity check, not
an authenticated premise of this model review.
"""
    write("AUDIT_STATEMENT.md", statement.replace("{head}", head))

    v6_statement = (V6 / "STATEMENT_V6.md").read_text(encoding="utf-8")
    v6_statement_indented = "\n".join(f"    {row}" for row in v6_statement.splitlines()) + "\n"
    pins_text = (AUDIT / "RELEASE_PINS.json").read_text(encoding="utf-8")
    ch51_scope = lines(CH51, 96, 166)
    ch51_strong_openness = lines(CH51, 1553, 1638)
    ch51_i_preorder = lines(CH51, 3210, 3237)
    ch51_projection = lines(CH51, 3290, 3461)
    ch51_npp_bidegree_one = lines(CH51, 2112, 2154)
    ch51_npp_ledger = lines(CH51, 2168, 2185)
    ch51_cantor = lines(CH51, 3780, 3885)
    ch72_status = lines(CH72, 2861, 2892)
    inventory_status = lines(INVENTORY, 892, 929)
    statement_body = statement.replace("{head}", head)
    context = r"""# theorem thm:p148-v7-exact-live-integration

## statement

{statement_body}

## proof

### Comparison target and provenance boundary

The indented V6 statement below is supplied solely as the frozen text against
which the reproduced Chapter 51 result is compared.  No previous verifier
receipt, hash, or Git identity is used as an authenticated mathematical
premise in this review.  The JSON block at the end is explicitly untrusted
local provenance metadata; the packet's separate `check_packet.py` verifies
it against the working tree before submission.

The question for this review is therefore narrow: assuming the reproduced
source excerpts are faithful, do they state and prove the same positive and
negative dichotomy as the supplied V6 target text, without broadening it?

### Audit argument

The live standing hypotheses supply the compact K\"ahler ambient setting and
smooth background form.  The \(\mathcal I\)-preorder defines equality of
complete integral multiplier-ideal towers, while the exact strong-openness
package supplies the needed converse: equality at every integral scale is
equivalent to equality of all divisorial Lelong numbers.  Thus the projection
proof's finite-maximum and increasing-envelope steps preserve the required
\(\mathcal I\)-class; this does not rely merely on the one-way valuative
criterion.  The live projection theorem then proves membership and
idempotence.  Its corollary establishes exactly the V6 positive assertion:
the construction depends only on the realizable class, is normalized, and a
normalized fixed point in that class is unique, with no positive-mass
assumption.

The live Cantor lemma chooses \(\ell_0=1\) and
\(\ell_m=\mathrm e^{{-4^m}}\) for \(m\ge1\), including the child-fitting and
capacity-divergence checks.  The live example then makes the full family
\(\varphi_s=sG_\mu\), proves zero Lelong numbers and therefore
\(\mathcal I(m\varphi_s)=\mathcal O_X\), and therefore places all members in
one \(\mathcal I\)-class.  The included bidegree-one identity and ledger
give the nonpluripolar mass calculation \(1-s\); no \(P\)-equivalence claim
is needed for this audit.  The example identifies the envelope of the common
class with \(0\), and its endpoint sentence is exactly V6's
non-reconstruction conclusion.

The Chapter 72 and inventory excerpts preserve the same exclusions: the
terminal filtration corollary is not being reused to reconstruct an arbitrary
zero-mass potential, and P14.8 is not declared retired by this audit.  Thus
the comparison neither adds a theorem nor promotes the result beyond the two
stated readings.

### Frozen V6 target statement (comparison-only)

The following indented block is a verbatim copy of `STATEMENT_V6.md`.
Indentation prevents it from being parsed as a second theorem item in this
audit.

{v6_statement_indented}

### Exact live Chapter 51 extract: ambient scope and comparisons

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
96–166.

```tex
{ch51_scope}```

### Exact live Chapter 51 extract: strong openness and Lelong recovery

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
1553–1638.

```tex
{ch51_strong_openness}```

### Exact live Chapter 51 extract: \(\mathcal I\)-preorder

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3210–3237.

```tex
{ch51_i_preorder}```

### Exact live Chapter 51 extract: envelope, projection, and reconstruction

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3290–3461.

```tex
{ch51_projection}```

### Exact live Chapter 51 extract: polar-Cantor family

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3780–3885.

```tex
{ch51_cantor}```

### Exact live Chapter 51 extract: bidegree-one product

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
2112–2154.

```tex
{ch51_npp_bidegree_one}```

### Exact live Chapter 51 extract: nonpluripolar ledger

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
2168–2185.

```tex
{ch51_npp_ledger}```

### Exact live Chapter 72 status boundary

Source: `manuscript/parts/part6/ch72_major_open_problems.tex`, lines
2861–2892.

```tex
{ch72_status}```

### Exact live inventory status boundary

Source: `manuscript/editorial/open_problem_atomic_inventory_20260824.md`,
lines 892–929.

```markdown
{inventory_status}```

### Untrusted local provenance metadata

```json
{pins_text}```
"""
    for marker, value in (
        ("{statement_body}", statement_body),
        ("{v6_statement_indented}", v6_statement_indented),
        ("{ch51_scope}", ch51_scope),
        ("{ch51_strong_openness}", ch51_strong_openness),
        ("{ch51_i_preorder}", ch51_i_preorder),
        ("{ch51_projection}", ch51_projection),
        ("{ch51_npp_bidegree_one}", ch51_npp_bidegree_one),
        ("{ch51_npp_ledger}", ch51_npp_ledger),
        ("{ch51_cantor}", ch51_cantor),
        ("{ch72_status}", ch72_status),
        ("{inventory_status}", inventory_status),
        ("{pins_text}", pins_text),
    ):
        context = context.replace(marker, value)
    write("AUDIT_PROOF_CONTEXT.md", context)

    scope = """# Scope and release conditions

This packet contains only a conditional exact-text comparison of P14.8 V6
against reproduced Chapter 51 construction and Chapter 72/inventory boundary
texts.  The local integrity checker separately binds those excerpts to the
working tree.  The accepted V7 model review is recorded in
`V7_ASTRA_VERIFICATION.json`, but it used `gpt-6-astra`/`xhigh`; the
inventory retirement rule still requires a production `gpt-5.6-sol`/`xhigh`
verdict for the exact current statement and proof.  The packet does not
modify the book or claim that P14.8 is already retired.

If an independent production review finds this exact-live claim correct with
no critical errors or gaps, the result would satisfy the remaining
exact-live-integration verifier gate.  Retirement would still require a
separate update of the live Chapter 72 and inventory status, followed by a
book build and normal repository verification.
"""
    write("AUDIT_SCOPE.md", scope)
    readme = """# P14.8 V7 exact-live integration audit packet

`build_packet.py` materializes this packet from exact source-line ranges at
the current Git revision and writes `RELEASE_PINS.json`.  The proof context
contains the frozen V6 target statement and all live source extracts required
for the limited comparison.  `SHA256SUMS` is an inventory and integrity
manifest for the packet after materialization.  The accepted V7 audit is a
source-and-boundary gate, not the required `gpt-5.6-sol` production gate.
"""
    write("README.md", readme)

    manifest_names = [
        "AUDIT_PROOF_CONTEXT.md",
        "AUDIT_SCOPE.md",
        "AUDIT_STATEMENT.md",
        "README.md",
        "RELEASE_PINS.json",
        "V7_REVIEW_ROUND0.md",
        "V7_REVIEW_ROUND1.md",
        "V7_ASTRA_VERIFICATION.json",
        "build_packet.py",
        "check_packet.py",
    ]
    rows = [f"{digest(AUDIT / name)}  {name}" for name in manifest_names]
    write("SHA256SUMS", "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
