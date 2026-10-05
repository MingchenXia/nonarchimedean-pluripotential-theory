#!/usr/bin/env python3
"""Small exact arithmetic checks, never a certificate of the geometric theorems."""
from fractions import Fraction
import json, pathlib, math

root=pathlib.Path(__file__).resolve().parent
blowups=[]
for n in range(2,9):
    for a in [Fraction(1,2),Fraction(1),Fraction(2)]:
        top=1+(-1)**(n-1)*a**n
        blowups.append({'dimension':n,'a':str(a),'volume_for_A_O1_on_Pn':'1',
                        'top_intersection':str(top),'degree_on_exceptional_line':str(-a)})
surface=[r for r in blowups if r['dimension']==2]
assert next(r for r in surface if r['a']=='1')['top_intersection']=='0'
assert next(r for r in surface if r['a']=='2')['top_intersection']=='-3'
sections=[]
for m in range(21):
    h0=math.comb(m+2,2)
    assert h0==(m+1)*(m+2)//2
    sections.append({'m':m,'h0_P2_O_m':h0,'h0_blowup_H_plus_E':h0,
                     'h0_zero_volume_product_pr1_O_m':m+1})
potentials=[]
for b in [Fraction(1,2),Fraction(1),Fraction(2)]:
    for t in [Fraction(0),b/2,b,2*b]:
        val=max(Fraction(0),b-t)-b
        assert -b<=val<=0
        if t>=b:assert val==-b
        if t==0:assert val==0
        potentials.append({'b':str(b),'t':str(t),'u_b_at_t_ord_D':str(val)})
out={'classification':'finite exact arithmetic checks of displayed formulas; no geometric domain exhaustiveness or proof certification',
     'blowup_parameters':blowups,'section_counts':sections,'zero_volume_potential_values':potentials,
     'checks_passed':True}
(root/'finite-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks_passed':True,'blowup_instances':len(blowups),
                  'section_degree_instances':len(sections),'potential_value_instances':len(potentials)}))
