"""Small independent exact checks. These do not certify analytic claims."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def inverse(a):
    n = len(a)
    aug = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        p = next(k for k in range(i, n) if aug[k][i])
        aug[i], aug[p] = aug[p], aug[i]
        z = aug[i][i]
        aug[i] = [x / z for x in aug[i]]
        for k in range(n):
            if k != i:
                z = aug[k][i]
                aug[k] = [x-z*y for x, y in zip(aug[k], aug[i])]
    return [row[n:] for row in aug]

def kernel(n, edges):
    lap = [[F(0) for _ in range(n)] for _ in range(n)]
    for v, w, ell in edges:
        if v == w:  # Both loop incidences cancel for vertex-affine functions.
            continue
        c = 1 / F(ell)
        lap[v][v] += c; lap[w][w] += c
        lap[v][w] -= c; lap[w][v] -= c
    grounded = inverse([row[1:] for row in lap[1:]]) if n > 1 else []
    k = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n): k[i][j] = grounded[i-1][j-1]
    return lap, k

def bilinear(k, p, q):
    return sum((p[i]*k[i][j]*q[j] for i in range(len(p)) for j in range(len(q))), F(0))

def main():
    # Deliberately independent rational-length domain, not the author's Q(sqrt(2)) grid.
    graphs = [
        ('singleton', 1, []),
        ('self_loop', 1, [(0, 0, F(2, 3))]),
        ('parallel', 2, [(0, 1, F(2, 3)), (0, 1, F(5, 4))]),
        ('triangle', 3, [(0, 1, F(2, 3)), (1, 2, F(5, 4)), (2, 0, F(7, 5))]),
        ('cycle_branch', 4, [(0, 1, F(2, 3)), (1, 2, F(5, 4)), (2, 0, F(7, 5)), (2, 3, F(3, 2))]),
        ('loop_subdivision', 3, [(0, 1, F(2, 3)), (1, 2, F(5, 4)), (2, 0, F(7, 5))]),
    ]
    a = F(5, 7); cases = 0; domains = []
    for name, n, edges in graphs:
        lap, k = kernel(n, edges)
        assert all(k[i][j] == k[j][i] and k[i][j] >= 0 for i in range(n) for j in range(n))
        mu0 = [a / n] * n
        count = 0
        for weights in product((1, 2, 3), repeat=n):
            mu = [a*w/sum(weights) for w in weights]
            u = [sum((k[i][j]*(mu0[j]-mu[j]) for j in range(n)), F(0)) for i in range(n)]
            # lap = -Delta_out.
            assert [sum((lap[i][j]*u[j] for j in range(n)), F(0)) for i in range(n)] == [mu0[i]-mu[i] for i in range(n)]
            i00 = bilinear(k, mu0, mu0); imm = bilinear(k, mu, mu); c0 = bilinear(k, mu0, mu)
            energy = sum((u[i]*(mu[i]+mu0[i]) for i in range(n)), F(0))/2
            functional = energy-sum((u[i]*mu[i] for i in range(n)), F(0))
            assert energy == (i00-imm)/2
            assert functional == (imm-2*c0+i00)/2
            count += 1; cases += 1
        domains.append({'name':name, 'vertices':n, 'edges':[[v,w,str(l)] for v,w,l in edges], 'target_tuples':count})
    # Triangle core with a branched attached tree. Verify common initial depth on all 36 pairs.
    core = [(0,1,F(2,3)), (1,2,F(5,4)), (2,0,F(7,5))]
    _, old = kernel(3, core)
    _, new = kernel(6, core+[(2,3,F(1,2)), (3,4,F(3,4)), (3,5,F(4,5))])
    projected = [0,1,2,2,2,2]
    depths = {2:F(0), 3:F(1,2), 4:F(5,4), 5:F(13,10)}
    for x in range(6):
        for y in range(6):
            added = F(0)
            if x >= 2 and y >= 2:
                added = min(depths[x],depths[y]) if x == y or x in (2,3) or y in (2,3) else F(1,2)
            assert new[x][y] == old[projected[x]][projected[y]] + added
    atomic = []
    for m in (2,4,8,16,32):
        points = [F(2*i+1,2*m) for i in range(m)]
        integral = sum((min(x,y)*(a/m)**2 for x in points for y in points), F(0))
        atomic.append({'atoms':m,'I':str(integral),'limiting_I':str(a*a/3)})
    result = {'status':'exhaustive finite exact result in the explicitly listed rational-length domain; not an analytic proof',
              'raw_mass':str(a),'graphs':domains,'target_tuples':cases,'tree_kernel_pairs':36,
              'nonatomic_interval':{'kernel':'min(x,y)','u':'-a*(x-x^2/2)','I':str(a*a/3),'E':str(-a*a/6),'F':str(a*a/6),'atomic':atomic},
              'author_450_bend_grid_independently_rerun':False,'author_build_independently_rerun':False}
    (ROOT/'independent-finite-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'target_tuples':cases,'tree_kernel_pairs':36,'interval_I':str(a*a/3),'success':True}))

if __name__ == '__main__': main()
