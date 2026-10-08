"""Fresh exact finite diagnostic. No algebra packages or supplied code."""
from fractions import Fraction
from math import gcd
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
def hull(points):
    pts=sorted(set(points)); lower=[]
    for p in pts:
        while len(lower)>1:
            a,b=lower[-2:]
            cross=(b[0]-a[0])*(p[1]-b[1])-(b[1]-a[1])*(p[0]-b[0])
            if cross>0:break
            lower.pop()
        lower.append(p)
    return lower
def generators(a,b):return [(0,b),(a,0)]
def gauge(gens,w):return min(x*w[0]+y*w[1] for x,y in gens)
def area2(gens):
    h=hull(gens);p=[(0,0)]+h+[(0,0)]
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:])))
def atoms(gens):
    out={}
    for (x0,y0),(x1,y1) in zip(hull(gens),hull(gens)[1:]):
        dx,dy=x1-x0,y0-y1
        if dx<=0 or dy<=0:continue
        g=gcd(dx,dy);a,b=dy//g,dx//g;m=min(a,b)
        ray=(Fraction(a,m),Fraction(b,m));out[ray]=out.get(ray,0)+g*m
    return out
def main():
    config={'axis_exponents':list(range(1,6)),'contraction_N':list(range(1,25)),'residue_degrees':[2,3,5],'residue_powers':[1,2,4],'residue_N':[1,2,3,4]}
    (ROOT/'bounded-input.json').write_text(json.dumps(config,indent=2)+'\n')
    counts={'diagonal':0,'mixed_area':0,'moment_symmetry':0,'product_atoms':0,'strict_maximum':0,'contraction_minimum':0,'residue_difference':0};fail=[]
    ideals=[generators(a,b) for a in config['axis_exponents'] for b in config['axis_exponents']]
    def ck(kind,condition,data):
        counts[kind]+=1
        if not condition:fail.append({'kind':kind,'input':data})
    for I in ideals:
        ck('diagonal',sum(w*gauge(I,v) for v,w in atoms(I).items())==area2(I),I)
        for J in ideals:
            product=[(a+c,b+d) for a,b in I for c,d in J]
            moment=sum(w*gauge(J,v) for v,w in atoms(I).items())
            ck('mixed_area',2*moment==area2(product)-area2(I)-area2(J),[I,J])
            ck('moment_symmetry',moment==sum(w*gauge(I,v) for v,w in atoms(J).items()),[I,J])
            merged=atoms(I).copy()
            for v,w in atoms(J).items():merged[v]=merged.get(v,0)+w
            ck('product_atoms',atoms(product)==merged,[I,J])
            added=atoms(I+J)
            for v in set(atoms(I))|set(added):
                if gauge(I,v)<gauge(J,v):ck('strict_maximum',atoms(I).get(v,0)==added.get(v,0),[I,J,[str(x) for x in v]])
    for n in config['contraction_N']:
        val=min(a+b for a in range(2*n+1) for b in range(2*n+1) if 2*a+b>=2*n and a+2*b>=2*n)
        ck('contraction_minimum',val==(4*n+2)//3,n)
    for d in config['residue_degrees']:
        for r in config['residue_powers']:
            for n in config['residue_N']:
                length=lambda s:1+d*(r*s-1)
                ck('residue_difference',length(n+1)-length(n)==d*r,[d,r,n])
    out={'domain':config,'counts':counts,'total':sum(counts.values()),'failures':fail,'status':'PASS' if not fail else 'FAIL','interpretation':'Exact finite arithmetic observation only; Newton-facet interpretation and all-ring statements need mathematical proofs.'}
    (ROOT/'evidence'/'bounded-output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
