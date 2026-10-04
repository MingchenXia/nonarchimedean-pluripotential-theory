"""Exact arithmetic for a Siu-proof repair diagnostic, not a general solver.

The universal obstruction is proved in the accompanying research dossier.
This script checks the displayed two-section model and finite normalization
and additive-constant witnesses; it does not produce an independent receipt.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

script = Path(__file__).resolve()
output = script.with_suffix('.json')
assert not output.exists(), 'Preserve the dated finite record.'
ns = [2,3,4,8,16,32]
scales = [F(1),F(2),F(10),F(1,3)]
rows = []
for n in ns:
    c = F(n-1,n)
    exponents = [(n+1,n-1),(n,n)]
    assert all(a+b == 2*n for a,b in exponents)
    for branch in ['p','q','other']:
        for s in scales:
            lp,lq = (-s,F(0)) if branch=='p' else ((F(0),-s) if branch=='q' else (F(0),F(0)))
            section_value = max(a*lp+b*lq for a,b in exponents)/n
            assert section_value == lp+c*lq
            ell = lp+lq
            assert section_value <= c*ell
            residual = section_value-c*ell
            assert residual == lp/n
            rows.append({'n':n,'branch':branch,'scale':str(s),'psi_from_sections':str(section_value),'ell_E':str(ell),'admissible_t':str(c),'section_defined_residual':str(residual),'fixed_bundle_degree':2,'residual_bundle_degree':str(2-2*c)})
monotonicity = []
constant_witnesses = []
for n,m in zip(ns,ns[1:]):
    ta,tb = F(n-1,n),F(m-1,m)
    delta = tb-ta
    assert delta>0
    assert F(-1,n)<F(-1,m)
    monotonicity.append({'earlier_n':n,'later_n':m,'psi_p_drop':0,'t_increase':str(delta),'residual_p_increase_at_unit_scale':str(delta),'required_monotonicity_inequality_fails':True})
    for ca,cb in [(F(0),F(0)),(F(2),F(-100)),(F(-20),F(0)),(F(-50),F(-1000))]:
        s=max(F(1),(ca-cb)/delta+1)
        excess=delta*s+cb-ca
        assert s>0 and excess>0
        constant_witnesses.append({'earlier_n':n,'later_n':m,'earlier_added_constant':str(ca),'later_added_constant':str(cb),'positive_divisorial_scale':str(s),'later_minus_earlier_corrected_residual':str(excess)})
record={'date':'2026-10-04','script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
    'construction':{'variety':'P^1 over an algebraically closed trivially valued field','p':'z0=0','q':'z1=0','E':'p+q','theta':'c1(O(2))','psi_n':'(1/n) max(log|z0^(n+1) z1^(n-1)|, log|z0^n z1^n|)','fixed_bundle':'O(2)','m_n': 'n','n_minimum':2},
    'section_and_branch_checks':rows,'section_and_branch_check_count':len(rows),
    'finite_monotonicity_witnesses':monotonicity,'finite_constant_witnesses':constant_witnesses,
    'universal_argument_in_dossier_not_replaced_by_finite_sampling':True,
    'proper_support_endpoint_case':{'canonical_choice_t_n':'1-1/n','residual':'(1/n) log|s_p|','limit_on_divisorial_points':0,'pointwise_limit_at_p_endpoint':'-infinity','pointwise_limit_on_other_points':0,'raw_global_pointwise_limit_is_not_usc':True},
    'theorem_6_21_counterexample':False,'new_open_problem_solution':False,
    'independent_model_verification_receipt':False,'active_book_source_changed':False}
output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'section_branch_checks':len(rows),'finite_monotonicity_witnesses':len(monotonicity),'finite_constant_witnesses':len(constant_witnesses),'all_exact_arithmetic_checks_pass':True,'output':str(output)},indent=2))
