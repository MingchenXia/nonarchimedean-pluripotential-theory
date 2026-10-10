"""One-shot checks of scalar identities, interior bounds and excluded boundaries.

These finite calculations do not certify a geometric construction or a
principal convergence theorem. The universal argument is in the companion
research dossier, outside the manuscript.
"""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

out = Path(__file__).with_suffix('.json')
assert not out.exists(), 'Preserve the existing calculation receipt.'
y, p, tau, a, w = sp.symbols('y p tau a w', positive=True)
closed = (y*p/(1+y*p) - y/(1+y))/(2*tau)
assert sp.cancel(closed - y*(p-1)/(2*tau*(1+y)*(1+y*p))) == 0
logistic = sp.exp(w)/(sp.exp(w)+sp.exp(-2*a*tau))
assert sp.simplify(sp.diff(logistic,a)-2*tau*logistic*(1-logistic)) == 0
first = (sp.log(1+sp.exp(w+2*tau))-sp.log(1+sp.exp(w)))/(2*tau)
second = (sp.exp(w+2*tau)/(1+sp.exp(w+2*tau))
          -sp.exp(w)/(1+sp.exp(w)))/(2*tau)
assert sp.simplify(sp.diff(first,w)-second) == 0

mp.mp.dps = 350
cases = eligible = boundary = 0
for tt in [1,4,16,64,256]:
    tnum = mp.mpf(tt)
    for delta in [mp.mpf(1)/16,mp.mpf(1)/8,mp.mpf(1)/4]:
        for j in range(17):
            x = delta+(1-2*delta)*j/16
            q0 = 1/(1+mp.exp(2*tnum*x))
            q1 = 1/(1+mp.exp(2*tnum*(x-1)))
            fsecond = (q1-q0)/(2*tnum)
            assert 0 < fsecond <= 1/(2*tnum)
            if 2*delta*tnum >= mp.log(4):
                assert fsecond >= 1/(4*tnum)
                eligible += 1
            cases += 1
    for x in [mp.mpf(-1),mp.mpf(0),mp.mpf(1),mp.mpf(2)]:
        q0 = 1/(1+mp.exp(2*tnum*x))
        q1 = 1/(1+mp.exp(2*tnum*(x-1)))
        fsecond = (q1-q0)/(2*tnum)
        assert fsecond < 1/(4*tnum)
        boundary += 1

result = {'date':'2026-10-04','status':'PASS_SCALAR_AND_BOUNDARY_CHECKS',
          'sympy_version':sp.__version__,'decimal_precision':mp.mp.dps,
          'exact_symbolic_identities':3,'interior_parameter_cases':cases,
          'interior_cases_meeting_stated_threshold':eligible,
          'boundary_or_exterior_cases_failing_strong_interior_bound':boundary,
          'scope':'Scalar algebra and finite high-precision parameter checks only; not geometric verification or a universal proof.',
          'active_manuscript_changed':False,
          'independent_model_verifier_verdict':False}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
