"""Own bounded Fraction checks. No supplied program is imported or executed.

The finite checks do not prove the continuum statements in the paper.
Run: python3 exact_checks.py
"""
from fractions import Fraction as Q
from itertools import combinations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = (ROOT / "certificate-input.json").read_bytes()
data = json.loads(raw)
counts = {}

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    counts[name] = counts.get(name, 0) + 1

def solve(matrix, rhs):
    """Small square rational linear system; None if singular."""
    n = len(rhs)
    a = [[Q(x) for x in row] + [Q(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        p = next((i for i in range(j, n) if a[i][j]), None)
        if p is None:
            return None
        a[j], a[p] = a[p], a[j]
        pivot = a[j][j]
        a[j] = [v / pivot for v in a[j]]
        for i in range(n):
            if i != j:
                c = a[i][j]
                a[i] = [v - c*w for v, w in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]

def diagnostic_lp(t, s):
    # x=(u,r,w_t,w_s); all rows are <= bounds.
    rows = [([-1,0,0,0], 0), ([1,0,0,0], 1), ([0,-1,0,0], 0),
            ([-1,1,-1,0], -t), ([1,-1,-1,0], t),
            ([0,-1,0,-1], -s), ([0,1,0,-1], s)]
    values = []
    for active in combinations(range(7), 4):
        x = solve([rows[i][0] for i in active], [rows[i][1] for i in active])
        if x is not None and all(sum(Q(c)*v for c,v in zip(a,x)) <= b for a,b in rows):
            values.append(x[1] + 2*x[2] + 4*x[3])
    check("LP_has_vertex", bool(values))
    return min(values)

V = [(0,1,0), (0,0,1), (0,-1,-1)]
check("dependent_normals", all(sum(v[j] for v in V)==0 for j in range(3)))
for i,j in combinations(range(3),2):
    check("distinct_pages_intersect_H", V[i][1]*V[j][2]-V[i][2]*V[j][1] != 0)

targets = []
for A0 in data["A"]:
    A = Q(A0)
    for u0 in data["u"]:
        u = Q(u0)
        for s0 in data["s"]:
            s = Q(s0)
            t = u-s
            f = max(Q(0), s-A*u)
            witness = max(Q(0), -t)-(A-1)/2
            check("relative_reference_bound", abs(f-s) <= A)
            check("witness_uniform_bound", abs(witness-f) <= (A-1)/2)
            check("positive_part_difference", 0 <= max(Q(0),s-u)-f <= A-1)
            for v in V:
                a,b = s*v[1], s*v[2]
                ref = max(abs(a),abs(b),-t,t-1)
                check("compatible_reference_exact", ref == s)
                check("compatible_reference_coercive", ref >= (abs(t)+abs(a)+abs(b))/3-1)
    for T in data["T"]:
        if T < max(1,A-1):
            continue
        t,s = -Q(T), Q(T)
        z = max(Q(0), -A*t+(1-A)*s)
        r = max(Q(0), -A*t+(1-A)*(s+1))
        check("sharp_z_value", z == T)
        check("sharp_r_value", r == T+1-A)
        check("convex_secant_spatial_identity", s == (Q(T)/(T+1))*(s+1))
        delta = Q(data["small_delta"])
        ys = [(-Q(T),delta*T*v[1],delta*T*v[2]) for v in V]
        check("legal_small_barycenter", tuple(sum(x[j] for x in ys)/3 for j in range(3)) == (-Q(T),Q(0),Q(0)))
        # Coefficients of epsilon in (T+1)(T-e)-T(T+1-A+e).
        check("sharp_constant_identity", (T+1)*T-T*(T+1-A) == A*T)
        check("sharp_error_coefficient", -(T+1)-T == -(2*T+1))
        lower = (A-1)*T/(2*(T+1))
        check("finite_lower_below_limit", lower <= (A-1)/2)
        targets.append({"A":str(A), "T":T, "finite_lower":str(lower), "proven_limit":str((A-1)/2)})
    # Two locations realize both signed errors of the witness.
    check("attainment_negative_error", -(A-1)/2 == max(Q(0),Q(0))-(A-1)/2)
    s=A+1
    check("attainment_positive_error", max(Q(0),s-1)-(A-1)/2-(s-A) == (A-1)/2)

lp_records=[]
for t0 in data["diagnostic_t"]:
    for s0 in data["diagnostic_s"]:
        t,s=Q(t0),Q(s0)
        value=diagnostic_lp(t,s)
        if s==0:
            check("LP_entire_trace_list", value == 2*max(Q(0),-t,t-1))
        if s>=0 and t+s<=0:
            check("LP_affine_region_list", value == -2*t-s)
        check("LP_global_affine_support", value >= -2*t-s)
        lp_records.append({"t":str(t),"s":str(s),"F":str(value)})
center=diagnostic_lp(Q(-1),Q(0))
endpoint=diagnostic_lp(Q(-1),Q(1,4))
check("diagnostic_PCC_cost", endpoint-center == Q(-1,4))

result={"status":"PASS", "arithmetic":"Python fractions.Fraction; no floating-point solvers",
        "input_sha256":hashlib.sha256(raw).hexdigest(),
        "checks":counts,"total_assertions":sum(counts.values()),
        "LP_active_subsets_per_point":35,"LP_records":lp_records,
        "sharp_finite_records":targets,
        "diagnostic_cost":str(endpoint-center),
        "limitation":"Exhaustive only for these explicit finite lists and the enumerated LP vertices. Continuum and limit claims are mathematical proofs in the paper."}
(ROOT/"exact-output.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["status","total_assertions","diagnostic_cost","checks"]},indent=2))
