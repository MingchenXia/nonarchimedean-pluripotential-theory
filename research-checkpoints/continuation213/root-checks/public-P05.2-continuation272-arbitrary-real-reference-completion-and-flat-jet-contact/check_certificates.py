"""Small exact certificates, not an all-obstacle or continuum proof.

Rerun: python check_certificates.py
Only the standard library is used. No floating point sign decisions.
"""
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path


class K:
    """Q(sqrt(2),sqrt(3)) in basis 1,sqrt2,sqrt3,sqrt6."""
    def __init__(self, *c):
        if len(c) == 1 and isinstance(c[0], K):
            self.c = c[0].c
        else:
            self.c = tuple(map(Q, c + (0,) * (4 - len(c))))

    def __add__(self, b):
        b = K(b)
        return K(*(x + y for x, y in zip(self.c, b.c)))

    __radd__ = __add__

    def __neg__(self):
        return K(*(-x for x in self.c))

    def __sub__(self, b):
        return self + -K(b)

    def __rsub__(self, b):
        return K(b) - self

    def __mul__(self, b):
        b = K(b)
        out = [Q(0)] * 4
        for i, x in enumerate(self.c):
            for j, y in enumerate(b.c):
                # bit 0 is sqrt2, bit 1 is sqrt3.
                common = i & j
                factor = (2 if common & 1 else 1) * (3 if common & 2 else 1)
                out[i ^ j] += x * y * factor
        return K(*out)

    __rmul__ = __mul__

    def __truediv__(self, b):
        return K(*(x / Q(b) for x in self.c))

    def __eq__(self, b):
        return self.c == K(b).c

    def interval(self):
        # Certified rational brackets by squaring integer endpoints.
        D = 10**12
        brackets = [(Q(1), Q(1))]
        for n in [2, 3, 6]:
            lo = math.isqrt(n * D * D)
            assert lo * lo < n * D * D < (lo + 1) ** 2
            brackets.append((Q(lo, D), Q(lo + 1, D)))
        low = high = Q(0)
        for c, (lo, hi) in zip(self.c, brackets):
            low += c * (lo if c >= 0 else hi)
            high += c * (hi if c >= 0 else lo)
        return low, high

    def positive(self):
        lo, hi = self.interval()
        assert lo > 0, (self.c, lo, hi)
        return True

    def nonnegative(self):
        return self == 0 or self.positive()

    def output(self):
        return [str(c) for c in self.c]


A, B = K(0, 1), K(0, 0, 1)


def nullspace(columns):
    rows = [[Q(columns[j][i]) for j in range(len(columns))]
            for i in range(len(columns[0]))]
    pivots, pivot_row = [], 0
    for col in range(len(columns)):
        ind = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if ind is None:
            continue
        rows[ind], rows[pivot_row] = rows[pivot_row], rows[ind]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [x / scale for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    basis = []
    for free in range(len(columns)):
        if free not in pivots:
            v = [Q(0)] * len(columns)
            v[free] = 1
            for i, col in enumerate(pivots):
                v[col] = -rows[i][free]
            basis.append(v)
    return basis


def positive_circuits(directions):
    """Exhaust every support of size <= ambient rank+1."""
    out, supports_examined = [], 0
    for n in range(1, min(len(directions), len(directions[0]) + 1) + 1):
        for subset in itertools.combinations(range(len(directions)), n):
            supports_examined += 1
            basis = nullspace([directions[i] for i in subset])
            if len(basis) != 1:
                continue
            v = basis[0]
            if all(x < 0 for x in v):
                v = [-x for x in v]
            if not all(x > 0 for x in v):
                continue
            denom = sum(v)
            full = [Q(0)] * len(directions)
            for ind, x in zip(subset, v):
                full[ind] = x / denom
            assert all(sum(lam * d[j] for lam, d in zip(full, directions)) == 0
                       for j in range(len(directions[0])))
            out.append(full)
    return out, supports_examined


def cost(slopes, relation):
    return sum((s * lam for s, lam in zip(slopes, relation)), K(0))


def sumvec(edges):
    return tuple(sum((w * u[i] for u, w, slope in edges), K(0)) for i in range(2))


def atom(edges):
    assert sumvec(edges) == (K(0), K(0))
    return sum((w * slope for u, w, slope in edges), K(0))


def plane_checks(data):
    M = 8 * A * B
    # Transverse primitive lifts +/- coordinate vectors, tangent determinant 1.
    first_x = B - (-B)
    first_y = A - (-A)
    assert first_x == 2 * B and first_y == 2 * A
    original = [((1, 0), first_x, A), ((-1, 0), first_x, A),
                ((0, 1), first_y, B), ((0, -1), first_y, B)]
    assert atom(original) == M == K(0, 0, 0, 8)
    cutoff_rows = []
    for j in data['diamond_levels']:
        center = [((1, 0), 2 * (B - 1), A - 1), ((-1, 0), 2 * (B - 1), A - 1),
                  ((0, 1), 2 * (A - 1), B - 1), ((0, -1), 2 * (A - 1), B - 1)]
        horizontal = [((-1, 0), 2 * (B - 1), -(A - 1)),
                      ((1, 0), 2 * B, A), ((-1, 1), K(1), B - A),
                      ((-1, -1), K(1), B - A)]
        vertical = [((0, -1), 2 * (A - 1), -(B - 1)),
                    ((0, 1), 2 * A, B), ((1, -1), K(1), A - B),
                    ((-1, -1), K(1), A - B)]
        m0, mx, my = atom(center), atom(horizontal), atom(vertical)
        assert m0 == 8 * (A - 1) * (B - 1)
        assert mx == 4 * B - 2 and my == 4 * A - 2
        assert m0 + 2 * mx + 2 * my == M
        for m in [m0, mx, my]:
            m.positive()
        moment = j * (2 * mx + 2 * my)
        bound = 4 * j * M
        assert moment == 8 * j * (A + B - 1)
        (bound - moment).positive()
        # Diamond wall: tangent (1,-1), outward lift (1,0), determinant +1.
        assert abs(1 * 0 - (-1) * 1) == 1
        assert (K(1) + K(1) * 0) == 1  # added gradient (1,1) on lift
        cutoff_rows.append({'j': j, 'mass': M.output(), 'origin': m0.output(),
                            'each_x_vertex': mx.output(), 'each_y_vertex': my.output(),
                            'height_moment': moment.output(), 'bound': bound.output()})
    # An explicit convex decomposition into rational positive plane references.
    t = [Q(5, 2) - A - B / 2, A - 1, (B - 1) / 2]
    for ti in t:
        ti.positive()
    vertices = [(1, 1), (2, 1), (1, 3)]
    assert sum(t, K(0)) == 1
    assert sum((ti * p[0] for ti, p in zip(t, vertices)), K(0)) == A
    assert sum((ti * p[1] for ti, p in zip(t, vertices)), K(0)) == B
    return {'raw_reference_mass': M.output(), 'cutoffs': cutoff_rows,
            'simplex_vertices': vertices, 'weights': [ti.output() for ti in t]}


def fan_checks(data):
    es = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1)]
    pairs = list(itertools.combinations(range(4), 2))
    directions = es + [tuple(es[i][k] + es[j][k] for k in range(3)) for i, j in pairs]
    exceptional = {(0, 1), (2, 3)}
    eta = [K(1)] * 4 + [K(0 if p in exceptional else 1) for p in pairs]
    h = [K(1)] * 10
    circuits, count = positive_circuits(directions)
    zero = []
    for n, rel in enumerate(circuits):
        c_eta, c_h = cost(eta, rel), cost(h, rel)
        c_eta.nonnegative(); c_h.positive()
        if c_eta == 0:
            zero.append(n)
    assert len(zero) > 0
    # Both H1=max(eta,h-1) and H2=max(eta,h-2) have germ eta.
    actual = [(A + B) * s for s in eta]
    rational_component = [2 * s for s in eta]
    residual = [(A + B - 2) * s for s in eta]
    (A + B - 2).positive()
    for n, rel in enumerate(circuits):
        costs = [cost(sl, rel) for sl in [actual, rational_component, residual]]
        for c in costs:
            c.nonnegative()
        assert (costs[0] == 0) == (costs[1] == 0) == (costs[2] == 0)
    # Every other face, retaining both tangent signs.
    face_cases = []
    for i in range(4):
        dirs = [es[i], tuple(-x for x in es[i])] + [es[j] for j in range(4) if j != i]
        partner = 1 - i if i < 2 else 5 - i
        se = [K(1), K(-1)] + [K(-1 if j == partner else 0) for j in range(4) if j != i]
        sh = [K(1), K(-1)] + [K(0)] * 3
        cs, examined = positive_circuits(dirs)
        for rel in cs:
            assert cost(se, rel) == 0
            cost(sh, rel).nonnegative()
        face_cases.append({'face': f'singleton{i+1}', 'circuits': len(cs), 'supports_examined': examined})
    for (i, j), u in zip(pairs, directions[4:]):
        dirs = [u, tuple(-x for x in u), es[i], es[j]]
        val = 0 if (i, j) in exceptional else 1
        se = [K(val), K(-val), K(1), K(1)]
        sh = [K(1), K(-1), K(1), K(1)]
        cs, examined = positive_circuits(dirs)
        for rel in cs:
            cost(se, rel).nonnegative(); cost(sh, rel).nonnegative()
        face_cases.append({'face': f'pair{i+1}{j+1}', 'circuits': len(cs), 'supports_examined': examined})
    for i, j in pairs:
        for ray in [i, j]:
            u, v = es[ray], tuple(es[i][k] + es[j][k] for k in range(3))
            cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
            assert math.gcd(*cross) == 1  # saturated unimodular plane basis
            dirs = [u, tuple(-x for x in u), v, tuple(-x for x in v)]
            cs, examined = positive_circuits(dirs)
            se = [K(1), K(-1), K(0 if (i,j) in exceptional else 1),
                  K(0 if (i,j) in exceptional else -1)]
            for rel in cs:
                assert cost(se, rel) == 0
            face_cases.append({'face': f'top{ray+1}-{i+1}{j+1}', 'circuits': len(cs), 'supports_examined': examined})
    # Primitive inward first divisor formula at all ten rays, then raw origin mass.
    vals = dict(zip(pairs, eta[4:]))
    singleton_w = [sum((vals[tuple(sorted((i,j)))] for j in range(4) if j != i), K(0)) - 2 * eta[i]
                   for i in range(4)]
    pair_w = [eta[i] + eta[j] - vals[(i,j)] for i,j in pairs]
    first = singleton_w + pair_w
    assert all(sum((w * u[k] for w,u in zip(first,directions)), K(0)) == 0 for k in range(3))
    raw = sum((w * s for w,s in zip(first,eta)), K(0))
    assert raw == 4
    # Explicit exact convex reference decomposition on the H1/H2 coefficient plane.
    ts = [2 - (A + B) / 2, (A - 1) / 2, (B - 1) / 2]
    refs = [(1,1), (3,1), (1,3)]
    for ti in ts:
        ti.positive()
    assert sum(ts,K(0)) == 1
    assert sum((t*p[0] for t,p in zip(ts,refs)),K(0)) == A
    assert sum((t*p[1] for t,p in zip(ts,refs)),K(0)) == B
    delta, alpha, radius, lift = Q(1,64), Q(1,16), Q(1,4), Q(1,512)
    assert delta * 2 <= alpha / 2 and lift < alpha * radius / 4
    exact_germ_coefficient = sum((t * delta for t in ts), K(0))
    assert exact_germ_coefficient == delta
    scaled_mass = exact_germ_coefficient * exact_germ_coefficient * raw
    assert scaled_mass == Q(1,1024)
    # Listed finite collar checks in all six coarse cones.
    cases = 0
    for i,j in pairs:
        for a in data['collar_coordinates']:
            for b in data['collar_coordinates']:
                x = tuple(Q(a) * es[i][k] + Q(b) * es[j][k] for k in range(3))
                rho = max(map(abs,x)); hv=max(Q(a),Q(b))
                ev=abs(Q(a)-Q(b)) if (i,j) in exceptional else hv
                if radius / 2 <= rho < radius:
                    assert hv <= 2*rho and ev <= 2*rho
                    assert lift+delta*ev < alpha*rho
                    cases += 1
    return {'origin_supports_examined': count, 'origin_circuits': len(circuits),
            'origin_zero_eta_circuits': len(zero), 'face_cases': face_cases,
            'raw_eta_mass': raw.output(), 'reference_simplex': refs,
            'weights': [x.output() for x in ts], 'delta': str(delta),
            'scaled_jet_mass': scaled_mass.output(), 'saturated_fine_cones': 12,
            'collar_cases': cases}


def main():
    data = json.loads(Path('certificate-input.json').read_text())
    out = {'status': 'all exact finite assertions passed',
           'arithmetic': 'rational coordinates in Q(sqrt2,sqrt3), rational isolating sign bounds',
           'plane': plane_checks(data), 'U34': fan_checks(data),
           'limitations': 'Exhaustive only for the listed finite circuit supports, levels and points; not a proof of continuum envelopes, all-refinement classification or review acceptance.'}
    Path('evidence').mkdir(exist_ok=True)
    Path('evidence/certificate-output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'], 'plane_levels':len(out['plane']['cutoffs']),
                      'origin_circuits':out['U34']['origin_circuits'],
                      'face_cases':len(out['U34']['face_cases']),
                      'collar_cases':out['U34']['collar_cases'],
                      'raw_reference_mass':out['plane']['raw_reference_mass'],
                      'scaled_jet_mass':out['U34']['scaled_jet_mass']},indent=2))


if __name__ == '__main__':
    main()
