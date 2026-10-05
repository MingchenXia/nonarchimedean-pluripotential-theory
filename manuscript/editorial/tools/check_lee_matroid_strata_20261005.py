"""Finite exact source checks; neither a general proof nor a verifier receipt.

Enumerate labelled matroids on at most four elements by basis exchange.
Check the coordinate-labelled cone/minor description and Lee26's printed
wedge complex. Pair checks below concern ray sets; the named augmented-fan
theorem, not this computation, supplies the geometric intersection axiom.
"""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json


def subsets(mask):
    return [s for s in range(mask + 1) if s & mask == s]


def matroids(n):
    ground = (1 << n) - 1
    for r in range(n + 1):
        candidates = [s for s in range(ground + 1) if s.bit_count() == r]
        for selector in range(1, 1 << len(candidates)):
            bases = frozenset(b for k, b in enumerate(candidates)
                              if selector & (1 << k))
            if all(any(((b ^ (1 << x)) | (1 << y)) in bases
                       for y in range(n) if (c & ~b) & (1 << y))
                   for b in bases for c in bases
                   for x in range(n) if (b & ~c) & (1 << x)):
                independent = frozenset(s for b in bases for s in subsets(b))
                ranks = {s: max((s & b).bit_count() for b in bases)
                         for s in range(ground + 1)}
                flats = frozenset(s for s in ranks
                                  if all(ranks[s | (1 << j)] > ranks[s]
                                         for j in range(n) if not s & (1 << j)))
                yield ground, bases, independent, ranks, flats


def flags(flats):
    answer = [()]
    for f in sorted(flats, key=lambda s: (s.bit_count(), s)):
        answer += [chain + (f,) for chain in list(answer)
                   if not chain or chain[-1] & f == chain[-1]]
    return answer


def vector(n, sign, support):
    return tuple(sign if support & (1 << j) else 0 for j in range(n))


def cone_rays(n, ground, independent, chain):
    return frozenset([vector(n, 1, 1 << j) for j in range(n)
                      if independent & (1 << j)]
                     + [vector(n, -1, ground & ~f) for f in chain])


def rank_matrix(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot_row = 0
    for j in range(len(a[0])):
        k = next((k for k in range(pivot_row, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[k], a[pivot_row] = a[pivot_row], a[k]
        divisor = a[pivot_row][j]
        a[pivot_row] = [x / divisor for x in a[pivot_row]]
        for k in range(pivot_row + 1, len(a)):
            if a[k][j]:
                c = a[k][j]
                a[k] = [x - c * y for x, y in zip(a[k], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def cochain_check(n, independent, ranks, flats, p):
    d = max(ranks.values())
    states = [[] for _ in range(d + 1)]
    for f in sorted(flats):
        for i in sorted(independent):
            if i & f != i:
                continue
            a = ranks[f] - i.bit_count()
            for s in subsets(f & ~i):
                if s.bit_count() == a - p and (i | s) in independent:
                    states[a].append((i, f, s))
    maps = []
    for a in range(d):
        positions = {state: j for j, state in enumerate(states[a + 1])}
        columns = []
        for i, f, s in states[a]:
            column = {}

            def wedge(target_i, target_f, support, coefficient):
                for j in range(n):
                    bit = 1 << j
                    if not support & bit or s & bit:
                        continue
                    target = (target_i, target_f, s | bit)
                    assert target in positions, ('wedge leaves basis', p, target)
                    sign = (-1) ** (s & (bit - 1)).bit_count()
                    k = positions[target]
                    column[k] = column.get(k, 0) + coefficient * sign

            for j in range(n):
                if i & (1 << j):
                    wedge(i ^ (1 << j), f, 1 << j, -1)
            for h in flats:
                if f & h == f and ranks[h] == ranks[f] + 1:
                    wedge(i, h, h & ~f, 1)
            columns.append({k: v for k, v in column.items() if v})
        maps.append(columns)
    for a in range(d - 1):
        for col in maps[a]:
            composed = {}
            for k, c in col.items():
                for j, v in maps[a + 1][k].items():
                    composed[j] = composed.get(j, 0) + c * v
            assert all(v == 0 for v in composed.values()), ('d squared', p, a)
    differential_ranks = []
    for a, columns in enumerate(maps):
        matrix = [[col.get(k, 0) for col in columns]
                  for k in range(len(states[a + 1]))]
        differential_ranks.append(rank_matrix(matrix))
    homology = [len(states[a])
                - (differential_ranks[a - 1] if a else 0)
                - (differential_ranks[a] if a < d else 0)
                for a in range(d + 1)]
    expected = [sum(ranks[f] == p for f in flats) if a == p else 0
                for a in range(d + 1)]
    assert homology == expected, ('cohomology mismatch', p, homology, expected)
    return {'p': p, 'chain_dimensions': [len(x) for x in states],
            'differential_ranks_over_Q': differential_ranks,
            'cohomology_dimensions': homology}


records = []
counts = {}
total_strata = total_pairs = total_cones = 0
for n in range(5):
    count = 0
    for ground, bases, independent, ranks, flats in matroids(n):
        count += 1
        cones = []
        for chain in flags(flats - {ground}):
            for i in sorted(independent):
                if all(i & f == i for f in chain):
                    rays = cone_rays(n, ground, i, chain)
                    assert rank_matrix(list(rays)) == len(rays)
                    cones.append((i, chain, rays))
        assert len({rays for _, _, rays in cones}) == len(cones)
        strata_count = pairs_count = 0
        for f in sorted(flats):
            for j in sorted(independent):
                if j & f != j:
                    continue
                strata_count += 1
                live = [k for k in range(n) if (f & ~j) & (1 << k)]

                def project(rays):
                    return frozenset(v for ray in rays
                                     if any(v := tuple(ray[k] for k in live)))

                meeting = [(i, chain, rays) for i, chain, rays in cones
                           if j & i == j and (f == ground or f in chain)]
                projected = {project(rays) for _, _, rays in meeting}
                minor_independent = {i & ~j for i in independent
                                     if j & i == j and i & f == i}
                minor_proper_flats = {g & ~j for g in flats
                                      if j & g == j and g & f == g and g != f}
                expected = {project(cone_rays(n, f & ~j, i, chain))
                            for chain in flags(minor_proper_flats)
                            for i in minor_independent
                            if all(i & h == i for h in chain)}
                assert projected == expected
                for (_, _, ra), (_, _, rb) in combinations(meeting, 2):
                    shared = ra & rb
                    assert project(shared) == project(ra) & project(rb)
                    for k in range(n):
                        if j & (1 << k):
                            assert vector(n, 1, 1 << k) in shared
                    if f != ground:
                        assert vector(n, -1, ground & ~f) in shared
                    pairs_count += 1
        cochains = [cochain_check(n, independent, ranks, flats, p)
                    for p in range(max(ranks.values()) + 1)]
        records.append({'n': n, 'bases_as_bitmasks': sorted(bases),
                        'rank': max(ranks.values()), 'loops_bitmask': min(flats),
                        'augmented_cones': len(cones), 'admissible_strata': strata_count,
                        'projected_common_ray_pairs': pairs_count,
                        'flat_counts_by_rank': [sum(ranks[f] == a for f in flats)
                                                for a in range(max(ranks.values()) + 1)],
                        'wedge_complexes': cochains})
        total_cones += len(cones)
        total_strata += strata_count
        total_pairs += pairs_count
    counts[str(n)] = count
assert counts == {'0': 1, '1': 2, '2': 5, '3': 16, '4': 68}
uniform = next(r for r in records if r['n'] == 4 and r['rank'] == 3
               and len(r['bases_as_bitmasks']) == 4)
assert uniform['flat_counts_by_rank'] == [1, 4, 6, 1]
report = {'scope': 'Finite exact source diagnostic; no general proof, independent model receipt, active TeX import, or atom retirement.',
          'primary': 'Lee, arXiv:2604.00750v1, Lemma 4.7/Proposition 4.8, Lemma 5.4/Proposition 5.5.',
          'matroid_enumeration': 'All nonempty equicardinal basis collections satisfying the basis exchange axiom, on labelled ground sets of sizes zero through four.',
          'counts_by_ground_set_size': counts, 'matroids_checked': len(records),
          'total_augmented_cones': total_cones, 'total_admissible_strata': total_strata,
          'projected_common_ray_pairs': total_pairs,
          'geometric_intersection_scope': 'Symbolic ray-set compatibility only; the known augmented-fan theorem supplies the geometric common-face property. No general projected-complex theorem is inferred from samples.',
          'd_squared_zero': True, 'wedge_complex_cohomology_matches_flat_counts': True,
          'coefficient_field_used': 'Q with exact Fraction elimination; no torsion calculation or integral extension claimed.',
          'U_3_4': uniform, 'records': records}
target = Path(__file__).resolve().parents[1] / 'lee_matroid_strata_exact_checks_20261005.json'
encoded = json.dumps(report, indent=2, sort_keys=True) + '\n'
if target.exists():
    assert target.read_text() == encoded, 'Refusing to replace different dated evidence.'
else:
    target.write_text(encoded)
print(json.dumps({k: report[k] for k in ['matroids_checked', 'counts_by_ground_set_size',
                                       'total_augmented_cones', 'total_admissible_strata',
                                       'projected_common_ray_pairs', 'd_squared_zero',
                                       'wedge_complex_cohomology_matches_flat_counts']}, indent=2))
