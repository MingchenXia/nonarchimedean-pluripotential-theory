#!/usr/bin/env python3
"""Small exact arithmetic evidence; not a proof checker or a geometric experiment."""
from fractions import Fraction as F
import json,pathlib
out={'classification':'exact finite arithmetic checks only; geometric and analytic claims are proved in the paper'}
sigma=F(-1);h=[F(-4,5),F(-9,10)];t=[F(7,10),F(17,20)];r=[a-b*sigma for a,b in zip(h,t)]
assert h[1]<h[0] and all(a<=b*sigma for a,b in zip(h,t)) and r[1]>r[0]
out['divided_monotonicity_inference']={'sigma':str(sigma),'h':[str(a) for a in h],
    't':[str(a) for a in t],'quotients':[str(a) for a in r],
    'conclusion':'h decreases and each bound holds, while the divided numerical values increase; this disproves the inference alone'}
psi=F(-7,5);referenceA=F(2,3);referenceD=F(-1,4);logf=F(-3,2)
sig=logf+referenceD;u=sig+psi;hA=psi-referenceA;hL=u-referenceA-referenceD
assert hL==hA+logf
out['metric_frame_sign']={'hA':str(hA),'logf':str(logf),'hL':str(hL),'identity':'hL=hA+logf; exact norm-convention arithmetic'}
bl=[]
for a in [F(1,2),F(1),F(2)]:
    bl.append({'a':str(a),'self_intersection':str(1-a*a),'degree_on_E':str(-a),
               'volume_from_proved_section_formula':'1'})
out['big_blowup_diagnostic']=bl
vals=[]
for b in [F(1),F(2)]:
    vals.append({'b':str(b),'generic_value':'0','values':[{'t':str(q),'u_b':str(max(F(0),b-q)-b)}
                     for q in [F(0),F(1,2),F(1),F(2),F(3)]]})
assert vals[0]['values'][3]['u_b']=='-1'
out['zero_volume_semiample_diagnostic']={'section_dimension':'m+1', 'square':'0','volume':'0',
         'top_measure':'zero, by positivity and raw mass; mathematical proof uses BE, not this computation','potential_values':vals}
V=F(5,9);c=F(3);mass=V
assert V*c-mass*c==0
out['raw_translation']={'V':str(V),'c':str(c),'energy_shift':str(V*c),'objective_shift':'0 for target mass V',
         'zero_mass_policy':'No quotient by zero is computed or defined.'}
pathlib.Path('diagnostics-output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
