from fractions import Fraction as Q
from pathlib import Path
import hashlib,json

R=Path('/workspace/research/root-checks')
tex=R/'P19.2-endpoint-preserving-actual-toric-model-approximation-candidate-20261006-continuation189.tex'
rows=[]
for targets,c in [([Q(1,5),Q(2,3),Q(3,2),Q(7,4),Q(5)],Q(7,9)),
                  ([Q(3,7),Q(4,9),Q(9,2)],Q(11,12)),
                  ([Q(13,17),Q(17,13)],Q(31,32))]:
    fan=[(0,1),(1,0)];blowups=[]
    for v in targets:
        target=(v.numerator,v.denominator)
        while target not in fan:
            for i,((p,q),(pp,qq)) in enumerate(zip(fan,fan[1:])):
                if Q(p,q)<v and (qq==0 or v<Q(pp,qq)):
                    new=(p+pp,q+qq);fan.insert(i+1,new)
                    blowups.append({'left':[p,q],'right':[pp,qq],'inserted':list(new)})
                    break
            else:raise AssertionError('Target cone not found')
    r=len(fan)-2
    assert all(pp*q-p*qq==1 for (p,q),(pp,qq) in zip(fan,fan[1:]))
    weights=[c*Q(i+1,r*(r+1)//2) for i in range(r)]
    slopes=[Q(p,q) for p,q in fan[1:-1]]
    coeff=[Q(0)]+[-sum((a*min(Q(p),q*v) for a,v in zip(weights,slopes)),Q(0)) for p,q in fan[1:-1]]+[Q(0)]
    assert coeff[1]==-c
    intersections=[]
    for i in range(1,r+1):
        p,q=fan[i];p0,q0=fan[i-1];p1,q1=fan[i+1]
        k=Q(p0+p1,p);assert k.denominator==1 and k*q==q0+q1
        intersection=coeff[i-1]+coeff[i+1]-k*coeff[i]
        assert intersection==weights[i-1]/q>0
        intersections.append(intersection)
    mass=1-c+sum((q*d for (_,q),d in zip(fan[1:-1],intersections)),Q(0));assert mass==1
    d2=sum((d*e for d,e in zip(coeff[1:-1],intersections)),Q(0))
    pair=-sum((a*b*min(v,w) for a,v in zip(weights,slopes) for b,w in zip(weights,slopes)),Q(0));assert d2==pair
    ordered=list(reversed(list(zip(weights,slopes))));S=Q(0);roof0=sum((a*v for a,v in ordered),Q(0));nodes=[(S,roof0)];area=Q(0);g=roof0
    for a,v in ordered:
        nextS=S+a;area+=v*(nextS*nextS-S*S)/2;g-=a*v;S=nextS;nodes.append((S,g))
    assert g==0 and S==c and -area==d2/2;nodes.append((Q(1),Q(0)))
    for i,(p,q) in enumerate(fan[1:-1],1):assert min(p*x+q*y for x,y in nodes)==-coeff[i]
    rows.append({'target_slopes':[str(v) for v in targets],'rays':[list(n) for n in fan],
        'ordinary_blowups':blowups,'central_multiplicities':[1]+[q for p,q in fan[1:-1]],
        'weights':[str(a) for a in weights],'actual_divisor_coefficients':[str(d) for d in coeff[1:-1]],
        'actual_component_degrees':[str(1-c)]+[str(d) for d in intersections],
        'mass':str(mass),'energy':str(d2/2),'entropy':str(roof0),'endpoint_raw_mass':str(1-c),
        'all_degrees_strictly_positive':True,'adjacent_determinants_one':True,
        'actual_monomial_min_orders_verified':True,'intersection_energy_equals_roof_area':True})
p=R/'P19.2-continuation189-exact-arbitrary-rational-fan-calibration-20261006.json'
assert not p.exists()
p.write_text(json.dumps({'classification':'Root exact finite arithmetic observations for candidate189; not a universal proof or acceptance certificate.',
    'candidate_tex_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),'original_closed':False,'rows':rows},indent=2)+'\n')
print(json.dumps({'checks':len(rows),'central_component_counts':[len(row['central_multiplicities']) for row in rows],
    'all_actual_arithmetic_checks_passed':True,'record':str(p)},indent=2))
