import json
import math
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def integral(poly,lo,hi):
    return sum(c*(hi**(i+1)-lo**(i+1))/F(i+1) for i,c in enumerate(poly))

def compositions(total,length):
    if length==1:
        yield (total,)
    else:
        for i in range(total+1):
            for tail in compositions(total-i,length-1): yield (i,)+tail

def main():
    counts={}
    count=0
    for p in range(1,13):
        for l in range(p+1):
            assert F(sum(math.comb(j,l) for j in range(l,p+1)),p+1)==F(math.comb(p,l),l+1)
            count+=1
    counts['primitive_binomial_identity']={'cases':count,'domain':'1<=p<=12, 0<=l<=p'}
    coeffs=[]
    for p in range(1,13):
        for j in range(p):
            # p binom(p-1,j)t^j(1-t)^(p-1-j), times G(1/2,t).
            base=[F(0)]*p
            for k in range(p-j):
                base[j+k]=F(p*math.comb(p-1,j)*math.comb(p-1-j,k)*(-1)**k)
            left=[F(0)]+[c/F(2) for c in base]
            right=[F(0)]*(p+1)
            for k,c in enumerate(base): right[k]+=c/F(2);right[k+1]-=c/F(2)
            val=integral(left,F(0),F(1,2))+integral(right,F(1,2),F(1))
            assert val>=F(p,4**(p+1))
            coeffs.append({'p':p,'j':j,'green_coefficient':str(val),'lower_bound':str(F(p,4**(p+1)))})
    counts['midpoint_coefficients']={'cases':len(coeffs),'domain':'1<=p<=12, 0<=j<p','coefficients':coeffs}
    count=0
    vecs=list(product(range(-2,3),repeat=2))
    for psi,lam,phi in product(vecs,repeat=3):
        z=tuple(a-b for a,b in zip(psi,lam))
        d=F(sum(a*a for a in z),2);J=F(sum(a*a for a in phi),2)
        value=sum(a*b for a,b in zip(z,phi))
        assert value*value<=4*d*J
        count+=1
    counts['quadratic_target_bound']={'cases':count,'domain':'psi,lambda,phi in {-2,-1,0,1,2}^2; finite quadratic polynomial, not actual cone measures'}
    count=0
    for N in range(1,4):
        for m in range(1,7):
            betas=list(compositions(m,N+1));B=math.comb(m+N,N)
            assert len(betas)==B
            for i in range(1,N+1):
                gen=[0]*(N+1);gen[0]=m-1;gen[i]=1
                assert tuple(gen) in betas
            for ztail in product([F(0),F(1,2),F(1),F(2)],repeat=N):
                zs=(F(1),)+ztail
                terms=[]
                for beta in betas:
                    coeff=math.factorial(m)//math.prod(math.factorial(b) for b in beta)
                    terms.append(F(coeff)*math.prod(z**b for z,b in zip(zs,beta)))
                total=sum(zs)**m;maximum=max(terms)
                assert sum(terms)==total and maximum<=total<=B*maximum
                count+=1
    counts['multinomial_extended_coordinate_bounds']={'cases':count,'domain':'1<=N<=3,1<=m<=6, z_i in {0,1/2,1,2}; zero z represents an infinite tropical coordinate'}
    count=0
    for e,r,a,c in product(range(1,13),range(1,13),range(1,6),range(1,6)):
        if a*r>c*e: continue
        for power in range(1,6):
            q=(c*power)//a+1
            assert F(q,power)>F(c,a)
            assert e*q-r*power>=0
            count+=1
    counts['normal_monomial_pole_clearing']={'cases':count,'domain':'f=z^e,h=z^(-r),1<=e,r<=12,1<=a,c<=5,ar<=ce; powers 1..5'}
    count=0
    for n,d,snum,sden in product(range(1,7),range(1,11),range(1,6),range(1,6)):
        s=F(snum,sden)
        assert F(d)/(s*d)**n==s**(-n)*F(d)**(1-n)
        count+=1
    counts['radial_finite_map_scalars']={'cases':count,'domain':'1<=n<=6,1<=d<=10,s numerator and denominator 1..5'}
    def secant(t,M,level):
        if t>=0:return F(0)
        width=F(M,2**level)
        index=(t+M)//width
        left=-F(M)+index*width
        right=left+width
        return left*left+(t-left)*(right*right-left*left)/width
    count=0
    for M,level,k in product(range(1,6),range(0,6),range(0,65)):
        t=-F(M)*F(k,64)
        coarse=secant(t,M,level);fine=secant(t,M,level+1)
        assert coarse>=fine>=t*t
        count+=1
    counts['lower_growth_counterexample_secants']={'cases':count,'domain':'M=1..5, dyadic levels 0..5, t=-M k/64, k=0..64'}
    report={'status':'passed','kind':'exhaustive finite arithmetic only; not mathematical certification',
            'checks':counts,'total_cases':sum(x['cases'] for x in counts.values())}
    (ROOT/'checks-output.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','total_cases':report['total_cases'],
                      'counts':{k:v['cases'] for k,v in counts.items()}},indent=2))

if __name__=='__main__':main()
