#!/usr/bin/env python3
"""Check the exact active-problem crosswalk for Chapter 72.

This is an editorial consistency gate.  It verifies the active identifiers,
their placement under the twelve formal Chapter 72 problem environments,
and the published tier totals.  It deliberately does not make a mathematical
claim about whether any problem is open.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INVENTORY = ROOT / "manuscript/editorial/open_problem_atomic_inventory_20260824.md"
CHAPTER = ROOT / "manuscript/parts/part6/ch72_major_open_problems.tex"

EXPECTED_GROUPS = (
    ("prob:frontier-classical-regularization", ("P02.1", "P02.2", "P02.3", "P02.4")),
    ("prob:frontier-unibranch-local-envelope", ("P03.1", "P03.2", "P03.3")),
    ("prob:frontier-local-ma", ("P04.1", "P04.2", "P04.3", "P04.4")),
    ("prob:frontier-polyhedral-regularity", ("P05.1", "P05.2", "P05.5")),
    ("prob:frontier-pluriharmonic", ("P06.2",)),
    ("prob:frontier-singular-local", ("P12.2", "P12.3", "P12.4", "P12.5", "P12.6")),
    ("prob:frontier-affine-cone-ma", ("P13.1", "P13.2")),
    ("prob:frontier-mp-pseff", ("P14.1", "P14.4", "P14.5", "P14.6", "P14.8")),
    ("prob:frontier-zero-volume", ("P15.1", "P15.2", "P15.3")),
    ("prob:frontier-general-ma", ("P16.1", "P16.2", "P16.3", "P16.4", "P16.5", "P16.6", "P16.7")),
    ("prob:frontier-hybrid-ytd", ("P19.1", "P19.2", "P19.3", "P19.4")),
    ("prob:frontier-cross-fan-upstairs", ("P21.3",)),
)
EXPECTED_IDENTIFIERS = tuple(identifier for _, identifiers in EXPECTED_GROUPS for identifier in identifiers)
EXPECTED_TIERS = Counter({"T1": 0, "T2": 3, "T3": 7, "T4": 15, "T5": 17})
COUNT_DECLARATION = "12 formal problem environments = 42 active atomic research questions."
TIER_DECLARATION = "Tier counts: (T1,T2,T3,T4,T5) = (0,3,7,15,17)."
RETIRED_FRONTIER_LABELS = (
    "prob:frontier-cld-hierarchy",
    "prob:frontier-cld-global-metric",
)

HEADING = re.compile(r"^### `(prob:frontier-[^`]+)` ---", re.MULTILINE)
ACTIVE = re.compile(r"^- \*\*(P\d{2}\.\d+)\*\* `\[(T[1-5]); open(?:[;\] ])", re.MULTILINE)
CHAPTER_LABEL = re.compile(r"\\label\{(prob:frontier-[^}]+)\}")


class InventoryError(ValueError):
    """An exact editorial inventory invariant has drifted."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InventoryError(message)


def grouped_active_atoms(inventory: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    headings = list(HEADING.finditer(inventory))
    actual = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(inventory)
        identifiers = tuple(match.group(1) for match in ACTIVE.finditer(inventory, heading.end(), end))
        actual.append((heading.group(1), identifiers))
    return tuple(actual)


def audit() -> dict[str, object]:
    inventory = INVENTORY.read_text(encoding="utf-8")
    chapter = CHAPTER.read_text(encoding="utf-8")
    require(COUNT_DECLARATION in inventory, "published active-problem count declaration drifted")
    require(TIER_DECLARATION in inventory, "published tier-count declaration drifted")

    actual_groups = grouped_active_atoms(inventory)
    require(actual_groups == EXPECTED_GROUPS, "active identifiers or their problem-environment placement drifted")

    active_atoms = [(match.group(1), match.group(2)) for match in ACTIVE.finditer(inventory)]
    identifiers = tuple(identifier for identifier, _ in active_atoms)
    require(identifiers == EXPECTED_IDENTIFIERS, "active identifiers are not the exact ordered 42-atom list")
    tiers = Counter(tier for _, tier in active_atoms)
    tier_order = ("T1", "T2", "T3", "T4", "T5")
    require(
        tuple(tiers[tier] for tier in tier_order)
        == tuple(EXPECTED_TIERS[tier] for tier in tier_order),
        "active tier totals drifted",
    )

    problem_blocks = re.findall(r"\\begin\{problem\}(.*?)\\end\{problem\}", chapter, re.DOTALL)
    chapter_labels = tuple(label for block in problem_blocks for label in CHAPTER_LABEL.findall(block))
    all_frontier_labels = tuple(CHAPTER_LABEL.findall(chapter))
    retained_labels = tuple(label for label in all_frontier_labels if label not in chapter_labels)
    require(retained_labels == RETIRED_FRONTIER_LABELS,
            "retained historical frontier labels drifted")
    for label in RETIRED_FRONTIER_LABELS:
        require(
            re.search(r"\\begin\{remark\}(?:\[[^]]*\])?\s*\\label\{" + re.escape(label) + r"\}", chapter),
            f"retired frontier label {label} must remain on its historical remark",
        )
    expected_labels = tuple(label for label, _ in EXPECTED_GROUPS)
    require(chapter.count(r"\begin{problem}") == len(expected_labels), "Chapter 72 formal problem-environment count drifted")
    require(chapter_labels == expected_labels, "Chapter 72 formal problem labels drifted")

    return {
        "audit": "PASS_OPEN_PROBLEM_INVENTORY",
        "scope": "editorial identifiers, placement, tier totals, and Chapter 72 labels; not mathematical openness",
        "formal_problem_environments": len(expected_labels),
        "active_atomic_questions": len(identifiers),
        "tiers": {tier: tiers[tier] for tier in tier_order},
        "identifiers": identifiers,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the passing inventory summary as JSON")
    args = parser.parse_args()
    try:
        report = audit()
    except (OSError, InventoryError) as error:
        print(f"FAIL_OPEN_PROBLEM_INVENTORY: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        tiers = report["tiers"]
        print(
            "PASS_OPEN_PROBLEM_INVENTORY: "
            f"{report['active_atomic_questions']} active atoms across "
            f"{report['formal_problem_environments']} Chapter 72 environments; "
            f"tiers T1={tiers['T1']}, T2={tiers['T2']}, T3={tiers['T3']}, "
            f"T4={tiers['T4']}, T5={tiers['T5']}"
        )


if __name__ == "__main__":
    main()
