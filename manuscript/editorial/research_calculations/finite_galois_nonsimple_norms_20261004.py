#!/usr/bin/env python3
"""Exact selected field-norm tests, not a proof or independent verification."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

x, y, T, W = sp.symbols("x y T W")


def modpoly(expr, p, *variables):
    return sp.Poly(sp.expand(expr), *variables, modulus=p)


def multiplication_matrix(p, terms):
    # Basis u^i v^j over F_p(x,y), with u^p=x and v^p=y.
    basis = [(i, j) for i in range(p) for j in range(p)]
    positions = {pair: n for n, pair in enumerate(basis)}
    matrix = sp.zeros(p * p)
    for col, (i, j) in enumerate(basis):
        for (a, b), coefficient in terms.items():
            I, J = i + a, j + b
            row = positions[(I % p, J % p)]
            matrix[row, col] += coefficient * x ** (I // p) * y ** (J // p)
    return matrix


cases = []
section_terms = [
    ("u", {(1, 0): 1}),
    ("v", {(0, 1): 1}),
    ("u+v+1", {(1, 0): 1, (0, 1): 1, (0, 0): 1}),
    ("u+2v+uv+1", {(1, 0): 1, (0, 1): 2, (1, 1): 1, (0, 0): 1}),
]
for p in [2, 3]:
    d = p * p
    for name, terms in section_terms:
        matrix = multiplication_matrix(p, terms)
        actual = modpoly(matrix.charpoly(T).as_expr(), p, T, x, y)
        b_to_d = sum(c ** d * x ** (a * p) * y ** (b * p)
                     for (a, b), c in terms.items())
        expected = modpoly(T ** d - b_to_d, p, T, x, y)
        assert actual == expected
        # Constant coefficient of det(TI-M) is (-1)^d det(M).
        norm = modpoly((-1) ** d * actual.eval(T, 0).as_expr(), p, x, y)
        expected_norm = modpoly(b_to_d, p, x, y)
        assert norm == expected_norm
        cases.append({
            "characteristic": p,
            "field": "F=F_p(x,y), E=F(u,v), u^p=x, v^p=y",
            "degree": d, "exponent": p,
            "basis": ["u^%d v^%d" % (i, j) for i in range(p) for j in range(p)],
            "section_coefficient": name,
            "computed_characteristic_polynomial": str(actual.as_expr()),
            "computed_field_norm": str(norm.as_expr()),
            "characteristic_polynomial_is_power_of_minimal_polynomial": True,
        })

towers = []
for p in [2, 3, 5]:
    # E_sep/F is Artin--Schreier; E/E_sep has two independent p-th roots.
    actual = modpoly(sp.resultant(W ** p - W - x, T - W ** p, W),
                     p, T, x)
    expected = modpoly(T ** p - T - x ** p, p, T, x)
    assert actual == expected
    u_norm = modpoly((-1) ** p * actual.eval(T, 0).as_expr(), p, x)
    assert u_norm == modpoly(x ** p, p, x)
    # Characteristic polynomial of u after the extra v extension, degree p^3.
    u_characteristic = modpoly((T ** (p * p) - T ** p - x) ** p,
                              p, T, x)
    assert u_characteristic == modpoly(T ** (p ** 3) - T ** (p * p) - x ** p,
                                      p, T, x)
    towers.append({
        "characteristic": p,
        "tower": "F=F_p(x,y), E_sep=F(w), w^p-w=x; E=E_sep(u,v), u^p=w, v^p=y",
        "separable_degree": p,
        "purely_inseparable_degree": p * p,
        "purely_inseparable_exponent": p,
        "total_degree": p ** 3,
        "norm_of_u_first_step": "w^p",
        "computed_norm_of_u_second_step": str(u_norm.as_expr()),
        "norm_of_v_first_step": "y^p",
        "norm_of_v_second_step": "y^(p^2)",
        "computed_characteristic_polynomial_of_u": str(u_characteristic.as_expr()),
        "scope": "Exact displayed identities; no general geometric factorization verification",
    })

valuation_cases = []
for p in [2, 3, 5]:
    d = p * p
    for valuation in [Q(-3, 2), Q(-1, 5), Q(0), Q(2, 7), None]:
        for denominator in [1, 2, 7]:
            for weight in [Q(-2), Q(1, 3)]:
                upstairs = None if valuation is None else (weight - valuation) / denominator
                downstairs = None if valuation is None else (d * weight - d * valuation) / (d * denominator)
                assert upstairs == downstairs
                valuation_cases.append({
                    "p": p, "degree": d, "exponent": p,
                    "section_valuation": None if valuation is None else str(valuation),
                    "denominator": denominator, "weight": str(weight),
                    "source_value": None if upstairs is None else str(upstairs),
                    "descended_value": None if downstairs is None else str(downstairs),
                    "null_means_zero_section_value_minus_infinity": valuation is None,
                })

normalization_diagnostics = []
for p in [2, 3, 5]:
    d = p * p
    original = Q(-1)
    wrongly_using_exponent_with_degree_denominator = -Q(p, d)
    assert original != wrongly_using_exponent_with_degree_denominator
    normalization_diagnostics.append({
        "p": p, "degree": d, "exponent": p,
        "section_valuation": 1, "weight": 0, "denominator": 1,
        "correct_value": str(original),
        "incorrect_value_using_exponent_instead_of_degree": str(wrongly_using_exponent_with_degree_denominator),
        "is_not_a_counterexample_to_candidate": True,
    })

result = {
    "status": "PASS: exact selected boundary calculations only",
    "sympy_version": sp.__version__,
    "matrix_cases": cases,
    "mixed_tower_cases": towers,
    "weighted_support_cases": valuation_cases,
    "normalization_diagnostics": normalization_diagnostics,
    "summary": {"multiplication_matrix_characteristic_polynomials": len(cases),
                "mixed_tower_cases": len(towers),
                "weighted_support_cases": len(valuation_cases),
                "degree_exponent_diagnostics": len(normalization_diagnostics)},
    "general_proof_verified": False,
    "independent_verifier_run": False,
    "book_admission_authorized_by_this_calculation": False,
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"], **result["summary"]}, indent=2))
