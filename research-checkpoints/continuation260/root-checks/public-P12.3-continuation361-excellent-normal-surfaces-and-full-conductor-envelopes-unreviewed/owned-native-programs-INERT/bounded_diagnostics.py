"""Small owned exact arithmetic diagnostics; no universal inference."""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
import json

root=Path.cwd(); output={}
def solve(mat,rhs):
    a=[[Q(x) for x in row]+[Q(rhs[i])] for i,row in enumerate(mat)]
    n=len(a)
    for j in range(n):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None: return None
        a[j],a[piv]=a[piv],a[j]; d=a[j][j];a[j]=[x/d for x in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j];a[i]=[x-d*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
matrices=[{'M':[[-2,1],[1,-2]],'b':[1,1],'f':[-1,-3],'B':4},
 {'M':[[-2,1,0],[1,-3,1],[0,1,-2]],'b':[1,1,1],'f':[-1,-3,-1],'B':5},
 {'M':[[-3,1,1],[1,-2,0],[1,0,-2]],'b':[1,1,1],'f':[-1,-4,-2],'B':5}]
matrix_rows=[];identities=inverses=maxpairs=0
for case in matrices:
    M,b,f,B=case['M'],case['b'],case['f'],case['B'];n=len(b);A=[[-x for x in r] for r in M];Ab=[dot(r,b) for r in A]
    assert all(x>=0 for x in Ab) and any(x>0 for x in Ab)
    for t in product(range(-3,4),repeat=n):
        z=[Q(t[i],b[i]) for i in range(n)]
        lhs=dot(t,[dot(r,t) for r in A]);rhs=sum(Ab[i]*b[i]*z[i]**2 for i in range(n))+sum(-A[i][j]*b[i]*b[j]*(z[i]-z[j])**2 for i in range(n) for j in range(i+1,n))
        assert lhs==rhs and (lhs>0 or all(x==0 for x in t));identities+=1
    for k in range(1,n+1):
        for J in combinations(range(n),k):
            S=[[A[i][j] for j in J] for i in J]
            for j in range(k):assert all(x>=0 for x in solve(S,[int(i==j) for i in range(k)]))
            inverses+=1
    inequalities=[]
    for i in range(n):
        ei=[int(i==j) for j in range(n)]
        inequalities.extend([(ei,Q(min(0,b[i]*f[i]))),([-x for x in ei],Q(B*b[i]))])
    inequalities.extend([([-x for x in row],Q(0)) for row in M])
    feasible=lambda x:all(dot(a,x)<=r for a,r in inequalities)
    vertices=set()
    for inds in combinations(range(len(inequalities)),n):
        x=solve([inequalities[i][0] for i in inds],[inequalities[i][1] for i in inds])
        if x is not None and feasible(x):vertices.add(tuple(x))
    greatest=tuple(max(x[i] for x in vertices) for i in range(n));assert feasible(greatest)
    for x,y in product(vertices,repeat=2):assert feasible(tuple(max(a,b) for a,b in zip(x,y)));maxpairs+=1
    matrix_rows.append({'vertices':len(vertices),'greatest':[str(x) for x in greatest]})
output['matrices']={'reference_identity_cases':identities,'principal_inverses':inverses,'vertex_max_pairs':maxpairs,'cases':matrix_rows}

# Independent finite monomial generator enumeration, rather than the formula.
smooth_rows=[]; smooth_cases=0
for j in range(1,9):
    for r in range(0,7):
        for s in range(0,7):
            gens=[(r+s-i-h,j*i+h) for i in range(s+1) for h in range(r+1)]
            count=sum(not any(a>=x and b>=y for x,y in gens) for a in range(r+s) for b in range(r+j*s))
            expected=r*(r+1)//2+r*s+j*s*(s+1)//2
            assert count==expected;smooth_cases+=1
            if j==2 and r==1 and s==1:smooth_rows.append(count)
output['smooth_staircase']={'cases':smooth_cases,'j2_r1_s1_length':smooth_rows[0]}

parity=[];diffs=0
for n in range(1,9):
    seq=[]
    for k in range(1,9):
        G=[(2*n*i+2*j,(2*n-2)*j+4*n*(k-i-j)) for i in range(k+1) for j in range(k-i+1)]
        count=sum((a+b)%2==0 and not any(a>=x and b>=y for x,y in G) for a in range(2*n*k) for b in range(4*n*k))
        seq.append(count)
    for k in range(6):assert seq[k+2]-2*seq[k+1]+seq[k]==2*n*n+2*n;diffs+=1
    parity.append({'n':n,'lengths':seq})
output['parity_lengths']={'cases':64,'second_differences':diffs,'sequences':parity}
profile_cases=0
pairs=[(Q(1),Q(k,2)) for k in range(2,13)]+[(Q(k,2),Q(1)) for k in range(3,15)]+[(None,Q(1)),(Q(1),None)]
for n in range(1,25):
    for a,b in pairs:
        middle=a if n==1 else (a+(n-1)*b if a is not None and b is not None else None)
        raw=min(x for x in [(n*a if a is not None else None),middle,(2*n*b if b is not None else None)] if x is not None)
        val=-raw/n
        expected=Q(-2) if a is None else (Q(-1) if b is None or a<=b else -min(1+(a-1)/n,Q(2)))
        assert val==expected;profile_cases+=1
output['normal_profiles']={'cases':profile_cases}
inputs={'matrix_cases':matrices,'matrix_integer_t_range':[-3,3], 'smooth_j':[1,8],'smooth_r_s':[0,6], 'parity_n_k':[1,8], 'profile_n':[1,24], 'profile_pairs':[[str(a) if a is not None else 'infinity',str(b) if b is not None else 'infinity'] for a,b in pairs]}
(root/'inputs/bounded-diagnostic-input.json').write_text(json.dumps(inputs,indent=2)+'\n')
(root/'reports/bounded-diagnostics.json').write_text(json.dumps({'status':'PASS','scope':'Exhaustive ONLY on the declared finite arithmetic domains. No geometry or universal theorem verified.',**output},indent=2)+'\n')
print(json.dumps({'status':'PASS','matrix_identity':identities,'principal_inverses':inverses,'max_pairs':maxpairs,'smooth_cases':smooth_cases,'parity_cases':64,'parity_differences':diffs,'profile_cases':profile_cases}))
