"""Small exact examples; these do not verify the analytic theorems."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

def main():
    checks = []
    grid = [F(i, 8) for i in range(9)]
    cases = 0
    for chi in product(grid, repeat=3):
        if max(chi) != 1:
            continue
        total = F(0)
        rho = []
        for v in chi:
            r = min(v, 1 - total)
            rho.append(r)
            total += r
        assert all(0 <= r <= c for r, c in zip(rho, chi))
        assert total == 1
        cases += 1
    checks.append({"id": "partition-grid", "kind": "exhaustive finite illustration", "grid": "{0,1/8,...,1}^3 with max=1", "cases": cases, "result": "nonnegative subordinate allocations sum to one"})
    shifts = []
    for r in range(2, 9):
        previous, current = F(1, 4 ** (r-1)), F(1, 4 ** r)
        B_previous, B_current = F(8, 3)*previous, F(8, 3)*current
        worst_increment = current + previous + B_current - B_previous
        assert worst_increment == current - previous < 0
        shifts.append({"r": r, "worst_increment": str(worst_increment)})
    checks.append({"id": "summable-shifts", "kind": "exact arithmetic examples", "values": shifts})
    annuli = []
    for r in range(2, 9):
        old_C = -r + 1
        old_R = r + 2
        assert 1 - old_R < old_C
        annuli.append({"r": r, "C_previous": old_C, "R_previous": old_R, "bound": 1-old_R})
    checks.append({"id": "annular-collar", "kind": "exact arithmetic examples", "values": annuli})
    # Common representation on the inner domain: u/A=Phi+G exactly.
    u, A, v, p, M = F(-2,3), F(7), F(-2), F(3,5), F(2)
    h = A*v + M + 1
    Psi = max(u-h, F(0))
    Phi = Psi/A + p
    G = v-p+(M+1)/A
    assert h < -M and Phi+G == u/A
    checks.append({"id": "common-reference-scalar", "kind": "exact arithmetic example", "Phi_plus_G": str(Phi+G), "u_over_A": str(u/A), "floor_inactive": True})
    # Exact length-two determinant: det(T0 I + T1 mult_z)=T0^2-a T1^2.
    checks.append({"id": "length-two-trace", "kind": "symbolic identity proved in the paper", "algebra": "k[z] over k[a], a=z^2", "multiplication_matrix": [["T0", "a*T1"], ["T1", "T0"]], "determinant": "T0^2-a*T1^2", "u": "max(log|z|,-1)", "trace": "max(log|a|,-2)", "center_dimension": 2})
    result = {"scope": "Finite exact illustrations and a displayed determinant identity. No numerical or exhaustive check of an infinite geometric/analytic theorem.", "checks": checks, "passed": True}
    Path("algebra-checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"passed": True, "partition_cases": cases, "groups": len(checks)}))

if __name__ == "__main__":
    main()
