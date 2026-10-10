#!/usr/bin/env python3
"""Selected exact diagnostics for a varying-class birational proof route."""
from fractions import Fraction as Q
from pathlib import Path
import json


def minimum(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def quotient_value(a, b, n):
    # a=v(x), b=v(y). None denotes +infinite valuation/zero section.
    # The proper pole is defined from the descended section, never inf-inf.
    if a is None:
        return None
    return -a + minimum(a, b) / n


def encode(v):
    return None if v is None else str(v)


orders = [2, 3, 5, 7, 11, 19]
weights = [Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2), None]
cases = []
comparisons = 0
for a in weights:
    for b in weights:
        values = [quotient_value(a, b, n) for n in orders]
        for left, right in zip(values, values[1:]):
            if left is None:
                assert right is None
            else:
                assert right is not None and left >= right
            comparisons += 1
        for n, value in zip(orders, values):
            if a is None:
                assert value is None
            else:
                assert value <= 0
                assert value - (-a) == minimum(a, b) / n
            cases.append({"a": encode(a), "b": encode(b), "n": n,
                          "descended_section_value": encode(value),
                          "limiting_pullback_trace": None if a is None else str(-a),
                          "proper_support": a is None or b is None})

jensen = []
for n in orders:
    left = quotient_value(Q(1), Q(2), n)
    right = quotient_value(Q(2), Q(1), n)
    midpoint = quotient_value(Q(3, 2), Q(3, 2), n)
    endpoint_average = (left + right) / 2
    gap = midpoint - endpoint_average
    assert gap == Q(1, 2 * n) > 0
    jensen.append({"n": n, "left_weights": [1, 2], "right_weights": [2, 1],
                   "midpoint_weights": ["3/2", "3/2"],
                   "left_value": str(left), "right_value": str(right),
                   "midpoint_value": str(midpoint),
                   "endpoint_average": str(endpoint_average),
                   "strict_convexity_violation": str(gap)})

result = {"status": "PASS: selected exact trace/support and Jensen diagnostics",
          "scope": "Bl_p(P^2) section family in classes H-E/n; not exact pullback classes.",
          "null_convention": "Null valuation means +infinity; null function value means -infinity.",
          "values": cases, "jensen_diagnostics": jensen,
          "summary": {"trace_support_cases": len(cases),
                      "monotonicity_comparisons": comparisons,
                      "strict_Jensen_violations": len(jensen)},
          "general_birational_psh_reflection_disproved": False,
          "critical_Siu_theorem_disproved": False,
          "independent_verifier_run": False,
          "book_theorem_admission": False}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"], **result["summary"]}, indent=2))
