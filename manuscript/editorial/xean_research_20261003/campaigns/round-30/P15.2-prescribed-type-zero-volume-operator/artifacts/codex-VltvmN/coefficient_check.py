#!/usr/bin/env python3
"""Finite exact arithmetic diagnostic, not an analytic proof."""
import json
from math import comb
from pathlib import Path

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

checks = 0
for n in range(1, 31):
    for k in range(n + 1):
        for j in range(k + 1):
            observed = sum(choose(a, j) * choose(n-a, k-j) for a in range(n+1))
            expected = comb(n+1, k+1)
            assert observed == expected, (n, k, j, observed, expected)
            checks += 1
out = {
    "kind": "exhaustive finite exact-integer diagnostic",
    "range": "1 <= n <= 30; 0 <= k <= n; 0 <= j <= k",
    "checks": checks, "passed": checks, "failed": 0,
    "analytic_correctness_established": False,
    "all_n_proof": "Subset counting in P15.2-argument.md Section 7.",
    "identity": "sum_a C(a,j) C(n-a,k-j) = C(n+1,k+1)",
}
Path(__file__).with_name("coefficient-check.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out))
