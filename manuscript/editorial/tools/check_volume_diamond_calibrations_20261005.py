"""Exact finite research calibrations; not an analytic proof certificate."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json


def radial_integral(n, r, tau, lo, hi):
    """Integrate the expanded radial density, without the endpoint formula."""
    a, b = 1 - r, r * tau
    return sum(
        F(n * comb(n - 1, j), j + 1) * a ** (j + 1)
        * b ** (n - 1 - j) * (hi ** (j + 1) - lo ** (j + 1))
        for j in range(n)
    )


def main():
    radii = [F(0), F(1, 7), F(2, 5), F(1, 2), F(3, 4), F(6, 7), F(1)]
    slopes = [F(0), F(1, 13), F(1, 7), F(1, 4), F(1, 2),
              F(3, 4), F(6, 7), F(12, 13), F(1)]
    cases = integrals = known_line_cases = 0
    for n in range(1, 25):
        for r in radii:
            for tau in slopes:
                a, b = 1 - r, r * tau
                expected = [(a + b) ** n - b ** n,
                            1 - b ** n, (a + b) ** n]
                computed = [radial_integral(n, r, tau, F(0), F(1)),
                            radial_integral(n, r, tau, F(0), tau) + 1 - tau ** n,
                            tau ** n + radial_integral(n, r, tau, tau, F(1))]
                assert computed == expected, (n, r, tau)
                assert computed[1] + computed[2] == computed[0] + 1
                assert all(0 <= m <= 1 for m in computed)
                if r == 1:
                    assert computed[0] == 0
                    assert computed[1] == 1 - tau ** n and computed[2] == tau ** n
                    known_line_cases += 1
                cases += 1
                integrals += 3

    logistic_values = [F(1, 9), F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5)]
    positive_schur = zero_schur = 0
    for r in radii[1:]:
        for q0 in logistic_values:
            for qt in logistic_values:
                g0, gt = q0 * (1 - q0), qt * (1 - qt)
                spatial = (1 - r) * g0 + r * gt
                from_hessian = gt / r - gt * gt / spatial
                from_factored = (1 - r) * g0 * gt / (r * spatial)
                assert from_hessian == from_factored
                if r < 1:
                    assert from_hessian > 0
                    positive_schur += 1
                else:
                    assert from_hessian == 0
                    zero_schur += 1

    concave_lines = tail_checks = 0
    for increments in combinations_with_replacement(range(-2, 3), 4):
        for intercept in range(-2, 3):
            values = [F(intercept)]
            for step in reversed(increments):
                values.append(values[-1] + step)
            peak = max(values)
            for i, value in enumerate(values):
                right, left = max(values[i:]), max(values[:i + 1])
                assert min(right, left) == value
                assert max(right, left) == peak
                tail_checks += 1
            concave_lines += 1

    weakened_full_mass_failures = 0
    for n in range(1, 25):
        for lam in [F(1, 7), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            mass = (1 - lam) ** n
            assert mass < 1 and 2 * mass != mass + 1
            weakened_full_mass_failures += 1

    result = {
        "date": "2026-10-05",
        "status": "PASS_EXACT_FINITE_RESEARCH_CALIBRATIONS",
        "arithmetic": "fractions.Fraction, exact integer binomial coefficients",
        "radial_dimensions": [1, 24],
        "radial_parameter_cases": cases,
        "independently_expanded_polynomial_integrals": integrals,
        "known_weak_line_zero_mass_boundary_cases": known_line_cases,
        "positive_subgeodesic_real_Hessian_Schur_checks": positive_schur,
        "zero_weak_geodesic_real_Hessian_Schur_checks": zero_schur,
        "r_zero_scope": "formal mass-polynomial boundary only; no division-by-zero time curve",
        "concave_scalar_test_lines": concave_lines,
        "scalar_tail_min_max_checks": tail_checks,
        "weakened_full_mass_diagonal_counterchecks": weakened_full_mass_failures,
        "source_main_theorem_counterexample_asserted": False,
        "arbitrary_psh_analytic_certificate": False,
        "independent_model_receipt": False,
        "book_theorem_admission": False,
        "solved_atom_admission": False,
    }
    target = Path(__file__).resolve().parents[1] / "volume_diamond_exact_calibrations_20261005.json"
    assert not target.exists(), "Preserve a previously recorded result rather than overwriting it."
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
