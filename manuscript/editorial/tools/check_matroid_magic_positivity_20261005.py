"""Exact finite source checks; no general theorem or verifier receipt."""
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import json, math

def subsets(mask):
    return [s for s in range(mask+1) if s&mask==s]

def matroids(n):
    ground=(1<<n)-1
    for r in range(n+1):
        choices=[s for s in range(ground+1) if s.bit_count()==r]
        for selector in range(1,1<<len(choices)):
            bases=frozenset(b for j,b in enumerate(choices) if selector>>j&1)
            if not all(any(((b^(1<<x))|(1<<y)) in bases for y in range(n) if (c&~b)>>y&1)
                       for b in bases for c in bases for x in range(n) if (b&~c)>>x&1):continue
            ranks={s:max((s&b).bit_count() for b in bases) for s in range(ground+1)}
            flats=[s for s in ranks if all(ranks[s|(1<<j)]>ranks[s] for j in range(n) if not s>>j&1)]
            yield ground,bases,ranks,flats

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def magic(c):
    d=len(c)-1
    return [sum((-1)**(i-j)*math.comb(d-j,i-j)*c[j] for j in range(i+1)) for i in range(d+1)]

def wagner(c):
    d=len(c)-1
    values=[sum(a*k**j for j,a in enumerate(c)) for k in range(d+1)]
    return [sum((-1)**j*math.comb(d+1,j)*values[k-j] for j in range(k+1)) for k in range(d+1)]

def real_rooted_degree_at_most_three(c):
    c=trim(c);d=len(c)-1
    assert d<=3
    if d<2:return True
    if d==2:return c[1]**2-4*c[2]*c[0]>=0
    a,b,e,f=c[3],c[2],c[1],c[0]
    return b*b*e*e-4*a*e**3-4*b**3*f-27*a*a*f*f+18*a*b*e*f>=0

def truncation(ranks,flats):
    lines=sorted(f for f in flats if ranks[f]==2);ind=[]
    for I in range(1<<len(lines)):
        valid=True
        for J in subsets(I):
            if not J:continue
            union=0
            for j,F in enumerate(lines):
                if J>>j&1:union|=F
            if ranks[union]<J.bit_count()+1:valid=False;break
        if valid:ind.append(I)
    d=max(I.bit_count() for I in ind);bases=[I for I in ind if I.bit_count()==d]
    assert all(any(((b^(1<<x))|(1<<y)) in bases for y in range(len(lines)) if (c&~b)>>y&1)
               for b in bases for c in bases for x in range(len(lines)) if (b&~c)>>x&1)
    return lines,ind

def weighted_check(lines,ind,weights):
    support=sum(1<<j for j,w in enumerate(weights) if w);ind=[I for I in ind if I&~support==0]
    d=max(I.bit_count() for I in ind); c=[0]*(d+1)
    weight=lambda I:math.prod(w for j,w in enumerate(weights) if I>>j&1)
    for I in ind:c[I.bit_count()]+=weight(I)
    m=magic(c);h=wagner(c)
    bases=sorted([I for I in ind if I.bit_count()==d],key=lambda I:tuple(j for j in range(len(lines)) if I>>j&1))
    shell=[0]*(d+1);seen=[];intervals=[]
    for B in bases:
        R=sum(1<<j for j in range(len(lines)) if B>>j&1 and any((B^(1<<j))&old==B^(1<<j) for old in seen))
        interval={I for I in subsets(B) if R&I==R};assert not any(interval&old for old in intervals);intervals.append(interval)
        term=[0]*R.bit_count()+[weight(R)]
        for j,w in enumerate(weights):
            if (B&~R)>>j&1:term=multiply(term,[1,w-1])
        for j,a in enumerate(term):shell[j]+=a
        seen.append(B)
    assert set().union(*intervals)==set(ind) and shell==m
    assert all(a>=0 for a in m+h) and real_rooted_degree_at_most_three(h)
    return {'Snapper_coefficients':c,'magic_vector':m,'h_star_coefficients':h,'support_line_flats':len([w for w in weights if w]),'degree':d}

def run():
    assert not real_rooted_degree_at_most_three([1,1,1])
    assert real_rooted_degree_at_most_three([1,3,3,1])
    assert not real_rooted_degree_at_most_three([1,13,7,1])
    counts={};total=0;rows=[]
    for n in range(1,5):
        count=0
        for ground,bases,ranks,flats in matroids(n):
            if any(ranks[1<<j]==0 for j in range(n)):continue
            count+=1;lines,ind=truncation(ranks,flats);assignments=0;degrees={}
            for weights in product(range(3),repeat=len(lines)):
                result=weighted_check(lines,ind,weights);assignments+=1
                d=result['degree'];degrees[str(d)]=degrees.get(str(d),0)+1
            rows.append({'n':n,'rank':ranks[ground],'bases':sorted(bases),'line_flats':lines,'assignments':assignments,'degree_counts':degrees})
            total+=assignments
        counts[str(n)]=count
    assert counts=={'1':1,'2':2,'3':6,'4':27} and total==2032
    transform_cases=0
    for d in range(7):
        for i in range(d+1):
            c=[0]*i+[math.comb(d-i,k) for k in range(d-i+1)];h=wagner(c);first=[0]*(d+1);last=[0]*(d+1)
            for sigma in permutations(range(1,d+2)):
                des=sum(a>b for a,b in zip(sigma,sigma[1:]))
                if sigma[0]==i+1:first[des]+=1
                if sigma[-1]==d+1-i:last[des]+=1
            assert h==first==last;transform_cases+=1
    named=[]
    graphs=[('path',[3,6,12],[1,3,3,1]),('triangle_and_tail',[3,5,6,12],[1,4,6,3]),('cycle',[3,6,9,12],[1,4,6,4]),('K4_minus_one_edge',[3,5,6,9,10],[1,5,10,8]),('K4',[3,5,6,9,10,12],[1,6,15,16])]
    for name,edges,expected in graphs:
        for kind,r in [('Boolean',4),('U3_4',3)]:
            ranks={s:min(r,s.bit_count()) for s in range(16)};flats=[s for s in ranks if all(ranks[s|(1<<j)]>ranks[s] for j in range(4) if not s>>j&1)]
            lines,ind=truncation(ranks,flats);w=[int(F in edges) for F in lines];x=weighted_check(lines,ind,w)
            if kind=='Boolean':assert x['Snapper_coefficients']==expected
            else:assert x['Snapper_coefficients']==[1,len(edges),math.comb(len(edges),2)]
            named.append({'graph':name,'matroid':kind,**x})
    surface=[]
    for weights in product(range(3),repeat=6):
        s=sum(weights);square=s*s-sum(w*w for w in weights);canonical_pairing=-2*s
        rr=[Fraction(1),Fraction(-canonical_pairing,2),Fraction(square,2)]
        direct=[1,s,sum(weights[i]*weights[j] for i,j in combinations(range(6),2))]
        assert rr==direct
        surface.append(direct)
    assert named[-1]['h_star_coefficients']==[1,19,10]
    aux=[Fraction(1)]
    for j in range(1,4):aux=multiply(aux,[Fraction(j),Fraction(2-j)])
    aux=[x/math.factorial(3) for x in aux]
    assert aux==[Fraction(1),Fraction(2,3),Fraction(-1,3),Fraction(0)]
    result={'date':'2026-10-05','source':'Li arXiv:2609.24917v1, Theorems 3.6/3.7, Examples 3.9--3.11',
      'method':'Exact integer independence and shelling enumeration; binomial magic transform; exact finite-difference Wagner transform; degree<=3 discriminants; separate rational surface Riemann--Roch arithmetic',
      'loopless_nonempty_labelled_matroids':36,'loopless_matroids_by_ground_size':counts,'integer_weight_domain':[0,1,2],
      'weight_assignments':total,'all_Dilworth_basis_exchange_and_weighted_shelling_identities_pass':True,'all_magic_vectors_nonnegative':True,'all_h_star_coefficients_nonnegative':True,'all_h_star_exact_real_root_criteria_pass':True,
      'refined_Eulerian_transform_and_convention_cases':transform_cases,'refined_Eulerian_direct_permutations_max_degree':6,
      'rank3_uniform_surface_Riemann_Roch_cases':len(surface),'surface_form':'diag(1,-1,-1,-1,-1,-1,-1) on H,E_F; D=sum(w_F)(H-E_F), K=-3H+sum(E_F)',
      'known_named_graph_examples':named,'finite_matroid_records':rows,
      'excluded_literal_auxiliary_step':{'source':'Li Proposition 5.7 proof, page 25','linear_coefficient_nonnegative_iff_weight_ge_degree_literal_step':False,'degree':3,'weight':2,'magic_vector':[str(x) for x in aux],'actual_linear_coefficient':'weight*H_degree-degree=2/3','full_magic_positivity':False,'main_matroid_proof_depends_on_step':False,'main_theorem_refuted':False,'general_proof_repair_imported':False},
      'scope':{'identified_known_Euler_functional_and_Snapper_input':True,'finite_tests_only':True,'nonproper_toric_Euler_pushforward_claimed':False,'arbitrary_real_weight_extension':False,'original_general_result_admitted':False,'new_independent_model_receipt':False,'open_problem_atom_changed':False}}
    return result

if __name__=='__main__':
    r=run();(Path(__file__).resolve().parents[1] / 'matroid_magic_positivity_exact_checks_20261005.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ['finite_matroid_records','known_named_graph_examples']},indent=2))
