#!/usr/bin/env python3
"""Small exact checks of displayed formulas, not checks of analytic/model actuality."""
from fractions import Fraction as Q
from math import comb
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

class Quad:
    """Exact ordered Q(sqrt(2)); sqrt(2) is the positive root."""
    def __init__(self, a=0, b=0): self.a, self.b = Q(a), Q(b)
    @staticmethod
    def coerce(x): return x if isinstance(x, Quad) else Quad(x)
    def __add__(self, x):
        x = self.coerce(x); return Quad(self.a+x.a, self.b+x.b)
    __radd__ = __add__
    def __neg__(self): return Quad(-self.a, -self.b)
    def __sub__(self, x): return self + -self.coerce(x)
    def __rsub__(self, x): return self.coerce(x) - self
    def __mul__(self, x):
        x = self.coerce(x)
        return Quad(self.a*x.a+2*self.b*x.b, self.a*x.b+self.b*x.a)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.coerce(x); norm = x.a*x.a-2*x.b*x.b
        if not norm: raise ZeroDivisionError
        return self * Quad(x.a/norm, -x.b/norm)
    def __rtruediv__(self,x): return self.coerce(x)/self
    def sign(self):
        a,b=self.a,self.b
        if b == 0: return (a>0)-(a<0)
        if a == 0: return (b>0)-(b<0)
        if a > 0 and b > 0: return 1
        if a < 0 and b < 0: return -1
        c = a*a-2*b*b
        return ((c>0)-(c<0)) * ((a>0)-(a<0))
    def __lt__(self,x): return (self-self.coerce(x)).sign()<0
    def __le__(self,x): return (self-self.coerce(x)).sign()<=0
    def __gt__(self,x): return (self-self.coerce(x)).sign()>0
    def __ge__(self,x): return (self-self.coerce(x)).sign()>=0
    def __eq__(self,x):
        x=self.coerce(x); return self.a==x.a and self.b==x.b
    def abs(self): return -self if self.sign()<0 else self
    def record(self): return dict(rational=str(self.a), sqrt2_coefficient=str(self.b))

sqrt2=Quad(0,1)
prototype_d=Q(9,10)*(2-sqrt2)
prototype=[]
for length,q1,q2 in [(Quad(1),Q(52,100),Q(53,100)),(sqrt2,Q(37,100),Q(38,100))]:
    t=(prototype_d-q2*length)/(q1-q2)
    assert 0<t<length
    assert q1*t+q2*(length-t)==prototype_d
    prototype.append(t.record())
assert Q(189,100)+Q(9,100)+Q(1,100)+Q(1,100)==2
assert prototype_d == Q(9,10)*(2-sqrt2)
assert (prototype_d-(-127+90*sqrt2)*Q(52,100) -
        (1-(-127+90*sqrt2))*Q(53,100)) == 0

# Reconstruct two parallel irrational edges with movable positive bends.
# Q(sqrt(2)) is a divisible value-group prototype, not a model of every field.
interpolation_cases=0
max_denominator=20000
for weights in [(Q(1),Q(1)),(Q(2),Q(3,2)),(Q(1,2),Q(4))]:
    conductance=weights[0]+weights[1]/sqrt2
    for theta in [(Q(1),Q(1)),(Q(-1),Q(3)),(Q(3),Q(-1))]:
        for target in [(Q(2),Q(0)),(Q(0),Q(2)),(Q(1),Q(1))]:
            for epsilon in [Q(1,4),Q(1,10),Q(1,25)]:
                desired=[(1-epsilon)*a+epsilon for a in target]
                d=(desired[0]-theta[0])/conductance
                old=[Quad(theta[0]),Quad(theta[1])]
                bends=[]
                for length,weight in zip([Quad(1),sqrt2],weights):
                    c=d/length
                    # Exact bisection on a rational grid; strict bracket even at equality.
                    lo,hi=-100*max_denominator,100*max_denominator
                    assert Q(lo,max_denominator)<c<Q(hi,max_denominator)
                    while hi-lo>1:
                        mid=(lo+hi)//2
                        if Q(mid,max_denominator)<c: lo=mid
                        else: hi=mid
                    q1=Q(lo,max_denominator)
                    q2=Q(hi+1,max_denominator)
                    assert q1<c<q2
                    t=(d-q2*length)/(q1-q2)
                    assert 0<t<length
                    assert q1*t+q2*(length-t)==d
                    old[0]+=weight*q1; old[1]-=weight*q2
                    bends.append(weight*(q2-q1))
                assert all(x>0 for x in old+bends)
                assert sum(old+bends,Quad(0))==2
                interpolation_cases+=1

# Check the Bernstein expansion and its explicit linear-plus-quadratic bound.
energy_cases=0
for n in range(1,11):
    vectors=[[Q(k+1) for k in range(n+1)], [Q(0)]+[Q(1)]*n,
             [Q(1)]+[Q(0)]*n]
    vectors += [[Q(int(k==j)) for k in range(n+1)] for j in range(n+1)]
    for A in vectors:
        B=sum(A)/Q(n+1)
        for t in [Q(i,20) for i in range(21)]:
            value=t/Q(n+1)*sum(comb(j,k)*t**k*(1-t)**(j-k)*A[k]
                                    for j in range(n+1) for k in range(j+1))
            assert value<=t*A[0]+Q(n*(n+1),2)*t*t*B
            if t==1: assert value==B
            if t==0: assert value==0
            energy_cases+=1

# The raw curve energy normalization is quadratic in V.
raw_cases=0
for V in [Q(1,3),Q(1),Q(2),Q(7,2)]:
    for I in [Q(0),Q(1,7),Q(3,2),Q(10)]:
        E=-V*V*I/2; integral=-V*V*I
        assert E-integral==V*V*I/2
        raw_cases+=1

# Reduction modulo a of a dense rank-one valuation ring need not have nilpotent nilradical.
nilpotence_cases=0
for N in range(1,101):
    valuation=Q(1,N+1)
    assert N*valuation<1 and (N+1)*valuation>=1
    nilpotence_cases+=1

result=dict(status='passed', arithmetic='fractions and exact Q(sqrt(2))',
            interpolation_cases=interpolation_cases, energy_cases=energy_cases,
            raw_curve_mass_cases=raw_cases, nilpotence_cases=nilpotence_cases,
            prototype_bend_positions=prototype,
            prototype_curvature=['189/100','9/100','1/100','1/100'],
            limitations='Finite formula checks only. No formal model, psh endpoint, source theorem, '
                        'generic curve, equation existence, or original closure is certified.')
(HERE/'finite-check-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
