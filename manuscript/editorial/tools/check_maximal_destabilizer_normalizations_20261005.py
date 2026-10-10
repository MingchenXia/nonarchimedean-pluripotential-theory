"""Exact normalization diagnostics, not a minimizer-convergence proof."""
from fractions import Fraction as F
from pathlib import Path
import json

degree_cases = 0
for k in range(1, 241):
    tent = [min(j, k-j) for j in range(k+1)]
    assert sum(tent) == k*k//4
    ek = F(sum(tent), k*(k+1))
    qk = 2*k*(F(1, 4)-ek)
    n2 = F(sum(v*v for v in tent), k*k*(k+1))
    if k % 2 == 0:
        assert ek == F(k, 4*(k+1))
        assert qk == F(k, 2*(k+1))
        assert n2 == F(k*k+2, 12*k*(k+1))
    else:
        assert ek == F(k-1, 4*k)
        assert qk == F(1, 2)
        assert n2 == F(k-1, 12*k)
    product = [F(j)-F(k, 2) for j in range(k+1)]
    assert sum(product) == 0
    assert sum(v*v for v in product)/((k+1)*k*k) == F(k+2, 12*k)
    degree_cases += 1

radial_cases = finite_cases = 0
for c in [F(-1), F(-3, 2), F(-1, 7)]:
    for n2 in [F(1), F(2, 3), F(7, 5)]:
        a0 = -c/n2
        assert a0*a0*n2 == -a0*c
        for a in [F(1, 10), F(1, 2), F(1), F(2), a0]:
            assert a*c+a*a*n2/2+c*c/(2*n2) == n2*(a-a0)**2/2
            radial_cases += 1
        for k in [1, 2, 3, 17, 240]:
            b0 = -2*k*k*c/n2
            assert b0*b0*n2 == -2*k*k*b0*c
            for b in [F(1, 3), F(1), F(2), b0]:
                assert 2*b*c+b*b*n2/(2*k*k)+2*k*k*c*c/n2 == n2*(b-b0)**2/(2*k*k)
                finite_cases += 1

# A rotation within a repeated-eigenvalue block is not diagonal.
A = [[F(1),F(0)],[F(0),F(1)]]
P = [[F(0),F(-1)],[F(1),F(0)]]
transpose = lambda a: list(map(list,zip(*a)))
multiply = lambda a,b: [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
assert multiply(transpose(P), P) == A
assert multiply(multiply(transpose(P), A), P) == A
assert P[0][1] != 0 and P[1][0] != 0

record = {
    'date':'2026-10-05',
    'degree_cases':degree_cases,
    'tent_spectral_sum_and_parity_formulas_exact':True,
    'tent_benchmark':{'energy':'1/4','Q_k_even':'k/(2(k+1))','Q_k_odd':'1/2','norm_squared_even':'(k^2+2)/(12k(k+1))','norm_squared_odd':'(k-1)/(12k)','limiting_norm_squared':'1/12','scope':'Exact lattice spectral arithmetic; not a destabilizer, A4 proof or independently certified general toric construction.'},
    'centered_product_norm_squared':'(k+2)/(12k)',
    'radial_penalty_scale_cases':radial_cases,
    'finite_Chow_penalty_scale_cases':finite_cases,
    'all_penalty_scale_identities_exact':True,
    'repeated_eigenvalue_block_rotation_checked':True,
    'book_and_source_clock_conversion':{'source_t':'2s','source_analytic_M':'2 book analytic M at the same squared potential','source_radial_speed':'book s-speed/2','same_NA_Mabuchi_slope':True},
    'scope':{'finite_arithmetic_only':True,'all_continuous_metric_A3_proved':False,'minimizer_convergence_A4_proved':False,'named_A4_topology_invented':False,'original_general_result_admitted':False,'new_independent_model_receipt':False,'Siu_or_general_closure_repaired':False}
}
output = Path(__file__).resolve().parents[1]/'maximal_destabilizer_exact_checks_20261005.json'
output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
