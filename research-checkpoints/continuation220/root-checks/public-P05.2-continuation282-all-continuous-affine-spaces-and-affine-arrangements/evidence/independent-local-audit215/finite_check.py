"""Independent bounded exact arithmetic; never imports supplied programs."""
import fractions,itertools,json,math,pathlib
F=fractions.Fraction
OWN=pathlib.Path(__file__).resolve().parent
data=json.loads((OWN/'certificate-input.json').read_text())
def determinant(m):
    n=len(m); s=F(0)
    for perm in itertools.permutations(range(n)):
        parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        p=F((-1)**parity)
        for i,j in enumerate(perm):p*=F(m[i][j])
        s+=p
    return s
def elimination(m):
    a=[[F(x) for x in r] for r in m]; out=F(1)
    for k in range(len(a)):
        pivot=next((j for j in range(k,len(a)) if a[j][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];out=-out
        v=a[k][k];out*=v
        for j in range(k+1,len(a)):
            q=a[j][k]/v
            a[j]=[x-q*y for x,y in zip(a[j],a[k])]
    return out
def root(q):
    q=F(q);a=math.isqrt(q.numerator);b=math.isqrt(q.denominator)
    assert a*a==q.numerator and b*b==q.denominator
    return F(a,b)
rows=[]
for r in data['rows']:
    det=determinant(r['matrix']);assert det==elimination(r['matrix']);d=len(r['matrix'])
    rows.append({'name':r['name'],'determinant':str(det),'raw_atom':str(F(r['weight'])*2**d*math.factorial(d)*abs(det)),'distinct_factor_orders':math.factorial(d)})
# Primitive saturated complements for (1,1),(1,-1).
kernel=(1,-1); complement=(1,0)
assert determinant([kernel,complement])==1
first=2*sum(x*y for x,y in zip((1,1),complement))
second=sum(abs(sum(x*y for x,y in zip((1,-1),direction))) for direction in [kernel,tuple(-x for x in kernel)])
mixed=first*second; assert mixed==8
crossing=8*(abs(determinant([[1,0],[0,1]]))+abs(determinant([[0,0],[0,1]])))
assert crossing==8
samples=list(map(F,data['primal_samples']));heights=[root(1+x*x) for x in samples]
tests=[]
for p in map(F,data['primal_tests']):
    g=max(p*x-y for x,y in zip(samples,heights)); actual=-root(1-p*p);assert g==actual
    tests.append({'dual_position':str(p),'sample_conjugate':str(g),'actual_conjugate':str(actual),'error':str(actual-g)})
tensor=[]
for d in data['dimensions']:
    count=0
    for ps in itertools.product(map(F,data['primal_tests']),repeat=d):
        assert sum(max(p*x-y for x,y in zip(samples,heights)) for p in ps)==-sum(root(1-p*p) for p in ps)
        count+=1
    tensor.append({'dimension':d,'rational_primal_positions':len(samples)**d,'dual_tuples_exhausted':count})
result={'status':'PASS','kind':'exhaustive finite exact-fraction results only','determinant_rows':rows,'primitive_index_two_mixed_mass':str(mixed),'primitive_index_two_self_mass':str(2*mixed),'transverse_arrangement_atom':str(crossing),'flat_pair_cost':'0','primal_dual_rows':tests,'cartesian_samples':tensor,'continuum_claim_certified_by_execution':False,'candidate':False}
(OWN/'finite-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
