"""Finite checks of known uniform-matroid formulas, using exact arithmetic.

This checks source identities and named examples, not a general geometric
identification or an independent production-model verification receipt.
Run from any directory; results are written beside the editorial audit.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import json


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [0]


def add(p, q):
    return trim([(p[k] if k < len(p) else 0) +
                 (q[k] if k < len(q) else 0)
                 for k in range(max(len(p), len(q)))])


def scaled(p, a, shift=0):
    return trim([0] * shift + [a * x for x in p])


def divmod_poly(p, q):
    p, q = list(map(Q, trim(p))), list(map(Q, trim(q)))
    assert q != [0]
    out = [Q(0)] * max(1, len(p) - len(q) + 1)
    while p != [0] and len(p) >= len(q):
        k = len(p) - len(q)
        a = p[-1] / q[-1]
        out[k] += a
        p = add(p, scaled(q, -a, k))
    return trim(out), p


def derivative(p):
    return trim([k * p[k] for k in range(1, len(p))])


def gcd_poly(p, q):
    while trim(q) != [0]:
        p, q = q, divmod_poly(p, q)[1]
    return scaled(p, Q(1) / p[-1])


def variations(signs):
    s = [x for x in signs if x]
    return sum(a != b for a, b in zip(s, s[1:]))


def root_counts(p):
    """Sturm counts after removing zero roots and repeated factors."""
    p = trim(p)
    assert p != [0]
    zeros = 0
    while p[0] == 0:
        zeros += 1
        p = p[1:]
    square_free, remainder = divmod_poly(p, gcd_poly(p, derivative(p)))
    assert remainder == [0]
    seq = [square_free, derivative(square_free)]
    if seq[-1] == [0]:
        seq.pop()
    else:
        while True:
            r = divmod_poly(seq[-2], seq[-1])[1]
            if r == [0]:
                break
            seq.append(scaled(r, -1))
    sign = lambda x: (x > 0) - (x < 0)
    neg = variations([sign(s[-1]) * (-1) ** (len(s)-1) for s in seq])
    at0 = variations([sign(s[0]) for s in seq])
    pos = variations([sign(s[-1]) for s in seq])
    return {'zero_root_multiplicity': zeros,
            'nonzero_square_free_degree': len(square_free)-1,
            'distinct_negative_roots': neg-at0,
            'distinct_positive_roots': at0-pos,
            'all_roots_real': neg-pos == len(square_free)-1}


def eulerian(n):
    p = [1]
    for m in range(1, n+1):
        p = trim([(k+1) * (p[k] if k < len(p) else 0) +
                  (m-k) * (p[k-1] if k else 0) for k in range(m)])
    return p


def derangement(n):
    p = [0]
    for k in range(n+1):
        p = add(p, scaled(eulerian(k), (-1)**(n-k) * C(n, k)))
    return p


def ordinary(r, n, i):
    p = [0]
    for j in range(r):
        a = C(n, j) * sum(C(n-j-l, r-j-1) * C(n-r-l, i-1)
                         for l in range(1, n-r-i+2))
        p = add(p, scaled(derangement(j), a, r-j-1))
    return p


def modified(r, n, i):
    p = [0]
    for s in range(r):
        a = C(n, s) * sum(C(n-s-l, r-s-1) * C(n-r-l, i-1)
                         for l in range(1, n-r-i+2))
        p = add(p, scaled(eulerian(s), a, r-s))
    return p


def independence_count(r, n, i):
    return C(n, r+i) * C(r+i-1, i-1)


def augmented(r, n, i):
    return add(modified(r, n, i), scaled([1], independence_count(r,n,i), r))


def chow(r, n):
    p = [1]
    for rank in range(2,r+1):
        d = [0]
        for j in range(rank):
            d = add(d,scaled(derangement(j),C(n,j)))
        p = add(scaled(p,1,1),d)
    return p


def augmented_chow(r, n):
    p = [1]
    for k in range(r):
        p = add(p,scaled(chow(r-k,n-k),C(n,k),1))
    return p


def magic_expansion(weights, degree):
    p = [0]
    for k, a in enumerate(weights):
        p = add(p, scaled([C(degree-k, j) for j in range(degree-k+1)], a, k))
    return p


def transform(p, kind):
    q = [0]
    for k, a in enumerate(p):
        term = derangement(k) if kind == 'D' else ([1] if k == 0 else [0]+eulerian(k))
        q = add(q, scaled(term, a))
    return q


def reverse(p, degree):
    assert len(trim(p))-1 <= degree
    return trim(list(reversed(p + [0]*(degree+1-len(p)))))


def proper_chains(h):
    """All strict subset flags from empty to h, without a retral formula."""
    if not h:
        yield [frozenset()]
        return
    def extend(flag):
        left = sorted(h-flag[-1])
        for size in range(1, len(left)+1):
            for extra in combinations(left, size):
                new = flag[-1] | frozenset(extra)
                if new == h:
                    yield flag+[new]
                else:
                    yield from extend(flag+[new])
    yield from extend([frozenset()])


def direct_weak_basis(r, n, i):
    p, rank_selected, flags = [0]*r, [0]*r, 0
    ground = frozenset(range(1,n+1))
    for hs in combinations(sorted(ground), r-1):
        h = frozenset(hs)
        available = sorted(ground-h)[:-1]  # every u needs a successor
        for flag in proper_chains(h):
            if any(len(flag[k]-flag[k-1]) == 1 and
                   next(iter(flag[k]-flag[k-1])) != max(flag[k+1]-flag[k-1])
                   for k in range(1, len(flag)-1)):
                continue
            flags += 1
            for us in combinations(available, i):
                if len(flag) > 1 and len(h-flag[-2]) == 1 and us[0] >= min(h-flag[-2]):
                    continue
                p[len(flag)-1] += 1
                ranks = {len(f) for f in flag}
                for j in range(r):
                    if ranks == {0} | set(range(j,r)):
                        rank_selected[j] += 1
    return trim(p), rank_selected, flags


def main():
    # Validate the polynomial arithmetic's counting conventions independently.
    for n in range(8):
        a, d = [0]*max(1,n), [0]*max(1,n)
        for w in permutations(range(1,n+1)):
            k = sum(v > j for j,v in enumerate(w,1))
            a[k] += 1
            if all(v != j for j,v in enumerate(w,1)):
                d[k] += 1
        assert trim(a) == eulerian(n) and trim(d) == derangement(n)
    assert root_counts([1,0,1])['all_roots_real'] is False
    assert root_counts([0,1,2,1]) == {
        'zero_root_multiplicity':1, 'nonzero_square_free_degree':1,
        'distinct_negative_roots':1, 'distinct_positive_roots':0,
        'all_roots_real':True}
    rows, direct, chow_rows = [], [], []
    for n in range(1,13):
        for r in range(1,n+1):
            h, ha = chow(r,n), augmented_chow(r,n)
            if r == n:
                assert h == eulerian(n)
            oh, ah = root_counts(h), root_counts(ha)
            assert oh['all_roots_real'] and ah['all_roots_real']
            chow_rows.append({'r':r,'n':n,'ordinary_Chow':h,
                              'augmented_and_modified_Chow':ha,
                              'ordinary_Sturm':oh,'augmented_Sturm':ah})
    for n in range(2,13):
        for r in range(1,n):
            for i in range(1,n-r+1):
                h, hm = ordinary(r,n,i), modified(r,n,i)
                # Sept Theorem 1.4: nonnegative magic basis and deranged map.
                weights = [sum(C(n-m-1,r+i-m-1)*C(i+k-m-1,i-1)
                               for m in range(k+1)) for k in range(r)]
                f = magic_expansion(list(reversed(weights)),r-1)
                assert reverse(transform(f,'D'),r-1) == h
                # Lemma 7.6 and Theorem 1.6: independent magic expansion.
                c = [sum(C(n-r-l,i-1)*C(n-l-p,r-p-1)*C(l-1+p,p)
                         for l in range(1,n-r-i+2)) for p in range(r)]
                g = magic_expansion(c,r-1)
                assert reverse(transform(g,'A'),r) == hm
                contraction = [0]
                for k in range(r):
                    contraction = add(contraction,scaled(ordinary(r-k,n-k,i),C(n,k),1))
                assert contraction == hm
                oh, mh = root_counts(h), root_counts(hm)
                assert oh['all_roots_real'] and mh['all_roots_real']
                rows.append({'r':r,'n':n,'i':i,'ordinary':h,'modified':hm,
                             'augmented':augmented(r,n,i),
                             'ordinary_Sturm':oh,'modified_Sturm':mh})
                if n <= 7:
                    hp,w,flags = direct_weak_basis(r,n,i)
                    assert hp == h
                    for j in range(r):
                        if j == 1:
                            assert w[j] == w[0]
                            continue
                        assert w[j] == f[j]
                    count = sum(min(js) < min(bs)
                                for bs in combinations(range(1,n+1),r)
                                for js in combinations(sorted(set(range(1,n+1))-set(bs)),i))
                    assert count == independence_count(r,n,i)
                    direct.append({'r':r,'n':n,'i':i,'ordinary':hp,
                                   'rank_selected_weak_flags_and_wedges':w,
                                   'weak_flags_enumerated':flags,
                                   'independence_basis_elements':count})
    a38 = augmented(3,8,4)
    a430 = augmented(4,30,24)
    assert a38 == [0,140,372,259]
    assert a430 == [0,1319500,9083815,8789785,8811999]
    assert 372**2-4*259*140 == -6656
    assert a430[2] > a430[3] < a430[4]
    m38, m430 = modified(3,8,4), modified(4,30,24)
    assert root_counts(m38)['all_roots_real'] and root_counts(m430)['all_roots_real']
    # Literal j=1 auxiliary count is excluded; d_1=0 kills this term.
    _, w, _ = direct_weak_basis(3,4,1)
    literal = C(4,1)*sum(C(4-1-l,3-1-1)*C(4-3-l,0) for l in range(1,2))
    assert w[0] == w[1] == 3 and literal == 8 and derangement(1) == [0]
    literal_augmented_recurrence = add(scaled(augmented_chow(1,4),1,1),
                                      add(eulerian(0),scaled(eulerian(1),4)))
    assert literal_augmented_recurrence == [5,1,1]
    assert augmented_chow(2,4) == [1,5,1]
    result={'date':'2026-10-05','scope':'Finite checks of identified known source formulas; no general geometric identification or original result admission.',
            'coefficient_order':'ascending powers of x',
            'uniform_parameter_range':{'n':[2,12],'r':[1,'n-1'],'i':[1,'n-r']},
            'parameter_triples':len(rows),'direct_basis_triples':len(direct),
            'zero_homological_degree_parameter_pairs':len(chow_rows),
            'all_formula_transform_and_contraction_identities_pass':True,
            'all_ordinary_and_modified_Sturm_counts_pass':True,
            'permutation_definitions_checked_through_n':7,
            'named_examples':{'U_3_8_i4':{'augmented':a38,'modified':m38,'discriminant':-6656,'roots':root_counts(a38),'modified_roots':root_counts(m38)},
                              'U_4_30_i24':{'augmented':a430,'modified':m430,'augmentation_contribution':independence_count(4,30,24),'unimodal':False,'modified_roots':root_counts(m430)}},
            'excluded_literal_auxiliary_count':{'source':'Binder--Vecchi v1, Definition 6.1 and displayed count in proof of Lemma 6.2','r':3,'n':4,'i':1,'j':1,'actual_W0_and_W1':3,'literal_binomial_expression':8,'d1_zero':True,'main_real_rootedness_theorem_refuted':False},
            'excluded_BV_augmented_recurrence':{'source':'Branden--Vecchi published p. 8, proof of Theorem 3.1; Eulerian normalization as defined on p. 4','r':2,'n':4,'literal_recurrence_output':literal_augmented_recurrence,'augmented_Chow_polynomial':augmented_chow(2,4),'used_as_augmented_real_rootedness_input':False,'main_theorem_refuted':False},
            'rows':rows,'direct_basis_rows':direct,'Chow_rows':chow_rows,
            'new_independent_model_receipt':False}
    out=Path(__file__).resolve().parents[1]/'augmented_singular_polynomial_exact_checks_20261005.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','direct_basis_rows','Chow_rows']},indent=2))


if __name__ == '__main__':
    main()
