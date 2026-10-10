from itertools import combinations
from pathlib import Path
import json, math, time

def gaussian(n,k,q=2):
    if k<0 or k>n: return 0
    a=b=1
    for j in range(k):
        a*=q**(n-j)-1; b*=q**(k-j)-1
    assert a%b==0
    return a//b

def rank(vectors):
    piv={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in piv: v^=piv[p]
            else: piv[p]=v; break
    return len(piv)

def subspaces(n):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
            for code in range(1<<len(free)):
                basis=[1<<p for p in pivots]
                for bit,(i,j) in enumerate(free):
                    if code>>bit&1: basis[i]|=1<<j
                vectors=[0]
                for b in basis: vectors += [v^b for v in vectors]
                mask=sum(1<<v for v in vectors)
                yield k,basis,tuple(vectors),mask

def cubic_discriminant(a,b,c,d):
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d

def run():
    started=time.time(); n=7
    W=set(range(1,8)); S={8,8+16,8+32,8+64,8+16+32,8+16+64}; D=W|S
    E=set(range(1,1<<n))-D; dmask=sum(1<<v for v in D)
    spaces=list(subspaces(n)); bymask={m:(k,vecs) for k,_,vecs,m in spaces}
    assert len(spaces)==len(bymask)==sum(gaussian(n,k) for k in range(n+1))
    byrank=[sum(k==j for k,_,_,_ in spaces) for j in range(n+1)]
    assert byrank==[gaussian(n,k) for k in range(n+1)]
    witnesses=[16,32,64,1+16,2+16,4+16,8+32+64]
    assert set(witnesses)<=E and rank(witnesses)==7
    c0=[sum(k==j and m&~(dmask|1)==0 for k,_,_,m in spaces) for j in range(n+1)]
    assert c0==[1,13,7,1,0,0,0,0]
    flat_counts=[0]*8; degree_counts={}; z=[0]*8; flats=0; extension_count=0
    for k,_,uvectors,umask in spaces:
        if rank(v for v in uvectors if v in E)!=k: continue
        flats+=1; flat_counts[k]+=1
        seen={umask}; queue=[umask]; counts=[0]*(n-k+1)
        while queue:
            bmask=queue.pop(); j,bvectors=bymask[bmask]; counts[j-k]+=1
            for v in D:
                if bmask>>v&1: continue
                extended=bmask|sum(1<<(x^v) for x in bvectors)
                if extended&~(umask|dmask)==0 and extended not in seen:
                    assert extended in bymask
                    seen.add(extended);queue.append(extended)
        degree=max(j for j,c in enumerate(counts) if c)
        assert k==n or 2*degree<n-k
        degree_counts[str((k,degree))]=degree_counts.get(str((k,degree)),0)+1
        extension_count+=len(seen)
        for j,c in enumerate(counts): z[k+j]+=c
    assert z==[gaussian(n,j) for j in range(n+1)]
    thresholds=[(7-k+1)//2 for k in range(7)]
    lower=[2**k*(2**h-1) for k,h in enumerate(thresholds)]
    assert lower==[15,14,28,24,48,32,64] and min(lower)>len(D)
    disc=cubic_discriminant(1,7,13,1); assert disc==-268
    W17=set(range(1,64)); S17={64+(j<<7) for j in range(589)}; D17=W17|S17
    assert len(D17)==652 and not(W17&S17)
    lines=set()
    for u,v in combinations(sorted(D17),2):
        w=u^v
        if w in D17:
            line=tuple(sorted((u,v,w))); assert set(line)<=W17
            lines.add(line)
    assert len(lines)==gaussian(6,2)==651
    rank17_witnesses=[1<<j for j in range(7,17)]+[(1<<j)+(1<<7) for j in range(6)]+[64+(1023<<7)]
    assert not(set(rank17_witnesses)&D17) and rank(rank17_witnesses)==17
    assert 6<17/2 and 652<2**15 and 589<=2**10
    p17=[gaussian(6,j) for j in range(7)]; p17[1]+=589
    assert p17==[1,652,651,1395,651,63,1]
    assert p17[1]>p17[2]<p17[3] and p17[2]**2<p17[1]*p17[3]
    result={
      'date':'2026-10-05','source':'arXiv:2607.24186v2, Theorem 1.1, Proposition 2.6, Corollary 1.3 and Appendix Theorem A.4',
      'arithmetic':'exact integers; binary vectors as bit masks; unique reduced-row-echelon subspace enumeration',
      'rank7':{'rank':7,'ground_set_size':len(E),'deleted_points':sorted(D),'spanning_witnesses':witnesses,
        'all_subspaces':len(spaces),'subspaces_by_dimension':byrank,'flat_spans':flats,'flat_spans_by_rank':flat_counts,
        'contained_deleted_subspace_coefficients':c0,'all_flat_quotient_degree_conditions_checked':True,
        'all_flat_quotient_dimension_and_degree_counts':degree_counts,'eligible_flat_and_extension_pairs':extension_count,
        'Z_coefficients_from_direct_flat_and_extension_counts':z,'Z_equals_Gaussian_rank_polynomial':True,
        'forbidden_extension_cardinality_lower_bounds':lower,'P_coefficients':[1,13,7,1],'cubic_discriminant':disc,
        'one_real_and_two_nonreal_roots':True},
      'rank17':{'rank':17,'ground_set_size':2**17-1-652,'W_dimension':6,'affine_deleted_points':589,
        'affine_set_definition':'S={64+(j<<7):0<=j<589}; W consists of nonzero vectors 1..63',
        'all_deleted_pair_line_checks':math.comb(652,2),'contained_lines':len(lines),'all_contained_lines_lie_in_W':True,
        'spanning_witnesses':rank17_witnesses,'size_and_rank_conditions_checked':True,'P_coefficients':p17,
        'strict_valley_at_degree_two':True,'log_concavity_fails_at_degree_two':True,
        'all_rank17_subspaces_or_flats_enumerated':False,'polynomial_uses_identified_known_Proposition_2_6':True},
      'scope':{'named_source_examples_only':True,'identified_known_projective_deletion_input':True,
        'general_combinatorial_proof_logically_reviewed_separately':True,'geometric_small_map_theorem_imported':False,
        'original_general_result_admitted':False,'new_independent_model_receipt':False,
        'open_problem_atom_status_changed':False},'elapsed_seconds':round(time.time()-started,3)}
    return result

if __name__=='__main__':
    result=run()
    target=Path('/tmp/matroid_KL_projective_deletion_exact_checks_20261005.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
