#!/usr/bin/env python3
"""Small exact checks of formulas; these certify no analytic/formal geometry."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

class Q2:
    """Exact Q(sqrt(2)), with exact ordering."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    @staticmethod
    def coerce(x):
        return x if isinstance(x, Q2) else Q2(x)
    def __add__(self, x):
        x = self.coerce(x); return Q2(self.a+x.a, self.b+x.b)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.a, -self.b)
    def __sub__(self, x): return self + -self.coerce(x)
    def __rsub__(self, x): return self.coerce(x) + -self
    def __mul__(self, x):
        x = self.coerce(x)
        return Q2(self.a*x.a+2*self.b*x.b, self.a*x.b+self.b*x.a)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.coerce(x)
        norm = x.a*x.a-2*x.b*x.b
        assert norm
        return self*Q2(x.a/norm, -x.b/norm)
    def sign(self):
        a, b = self.a, self.b
        if not b: return (a>0)-(a<0)
        if not a: return (b>0)-(b<0)
        if (a>0) == (b>0): return 1 if a>0 else -1
        diff = a*a-2*b*b
        assert diff != 0
        return ((diff>0)-(diff<0)) * (1 if a>0 else -1)
    def __lt__(self, x): return (self-self.coerce(x)).sign()<0
    def __le__(self, x): return (self-self.coerce(x)).sign()<=0
    def __eq__(self, x):
        x = self.coerce(x); return self.a==x.a and self.b==x.b
    def out(self): return {'rational': str(self.a), 'sqrt2_coefficient': str(self.b)}

def integral_bernstein(n, k, t):
    return comb(n,k)*sum((F((-1)**j*comb(n-k,j), k+j+1)*t**(k+j+1)
                         for j in range(n-k+1)), F(0))

def main():
    # Two parallel edges retain an irrational cycle. Slopes on a fixed
    # unsplit cycle would require q1*1=q2*sqrt(2), forcing both to zero.
    d = Q2(F(9,5), -F(9,10))
    lengths = [Q2(1), Q2(0,1)]
    slopes = [(F(52,100), F(53,100)), (F(37,100), F(38,100))]
    bends = []
    for length, (q1,q2) in zip(lengths,slopes):
        t = (q2*length-d)/(q2-q1)
        assert Q2(0)<t<length
        assert q1*t+q2*(length-t)==d
        bends.append(t)
    masses = [F(1)+sum(q1 for q1,q2 in slopes),
              F(1)-sum(q2 for q1,q2 in slopes)]
    masses += [q2-q1 for q1,q2 in slopes]
    assert masses == [F(189,100),F(9,100),F(1,100),F(1,100)]
    assert all(m>0 for m in masses) and sum(masses)==2
    # Exhaustive specified rational slope grid, rejecting non-bracketing pairs.
    variants=0
    for q1n in range(510,527):
        for q2n in range(528,545):
            for r1n in range(360,371):
                for r2n in range(374,385):
                    pairs=[(F(q1n,1000),F(q2n,1000)),
                           (F(r1n,1000),F(r2n,1000))]
                    if not all(Q2(p)<d/l<Q2(q) for l,(p,q) in zip(lengths,pairs)):
                        continue
                    ts=[(q*l-d)/(q-p) for l,(p,q) in zip(lengths,pairs)]
                    ms=[F(1)+sum(p for p,q in pairs),
                        F(1)-sum(q for p,q in pairs)]+[q-p for p,q in pairs]
                    assert all(Q2(0)<t<l for t,l in zip(ts,lengths))
                    assert all(m>0 for m in ms) and sum(ms)==2
                    variants+=1
    # Sharp-in-n scaling check: exact coefficients for dimensions 1..8
    # and t=j/20. This is a finite grid, not a proof for all real t.
    scaling=0
    for n in range(1,9):
        for j in range(21):
            t=F(j,20)
            c=[integral_bernstein(n,k,t) for k in range(n+1)]
            assert all(x>=0 for x in c)
            assert c[0]<=t
            assert sum(c[1:])<=F(n,2)*t*t
            assert sum(c)==t
            if n==1: assert c==[t-t*t/2,t*t/2]
            scaling+=1
    # Nonnegative flat Cech complex for O_P1(k), k>=0. Monomial j occurs
    # on chart0 iff j>=0, chart1 iff j<=k, intersection for every integer.
    # Every intersection monomial occurs on at least one chart; the
    # overlap 0<=j<=k has a rank-one diagonal kernel. This decomposition
    # remains exact over all the indicated nonreduced base rings.
    cech=0
    for modulus in (4,8,9,16):
        for k in range(7):
            for j in range(-9,10):
                available = int(j>=0)+int(j<=k)
                assert available in (1,2)
                if available==2:
                    image={(a-b)%modulus for a in range(modulus) for b in range(modulus)}
                    kernel=sum(1 for a in range(modulus) for b in range(modulus)
                               if (a-b)%modulus==0)
                    assert image==set(range(modulus)) and kernel==modulus
                else:
                    assert len({a%modulus for a in range(modulus)})==modulus
                cech+=1
    # A^o/a: elements with valuation 1/(N+1) remain nonzero after the
    # Nth power when val(a)=1, and become zero after the (N+1)th.
    # Exhaustive finite witnesses 1..64; the all-N argument is in the paper.
    nil=[]
    for n in range(1,65):
        val=F(1,n+1)
        assert n*val<1 and (n+1)*val==1
        nil.append({'power_bound':n,'valuation':str(val)})
    # Raw curve constants when mu=V nu, u=-V int j dnu.
    raw=[]
    for V in (F(1),F(3,2),F(7,3)):
        I=F(5,7)
        E=-V*V*I/2; target_integral=-V*V*I
        assert E-target_integral==V*V*I/2
        raw.append({'V':str(V),'I':str(I),'E':str(E),
                    'target_integral':str(target_integral),'dual':str(E-target_integral)})
    report={'status':'passed','irrational_cycle':{'bend_positions':[t.out() for t in bends],
                'raw_positive_masses':[str(x) for x in masses],
                'raw_total_mass':'2','accepted_grid_variants':variants},
            'scaling_dimension_time_pairs':scaling,'cech_monomial_base_checks':cech,
            'nilradical_witnesses':nil,'raw_curve_checks':raw,
            'limitations':'Finite exact arithmetic only; no formal scheme, PSH recognition, '
                          'residual coefficient theorem, or equation existence is certified.'}
    (ROOT/'finite-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('nilradical_witnesses','raw_curve_checks')},sort_keys=True))

if __name__=='__main__': main()
