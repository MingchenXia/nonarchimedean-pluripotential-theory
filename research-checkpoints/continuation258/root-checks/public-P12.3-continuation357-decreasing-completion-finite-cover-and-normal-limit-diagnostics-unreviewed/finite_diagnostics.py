"""Owned bounded stdlib checks. No supplied module is imported or executed.

Exact finite domain: n,k=1..8 for parity-semigroup monomial quotients;
n=1..16 and 17 rational/infinite coordinate pairs for profile formulas.
Universal asymptotics and geometric claims are proved in n5.md, not inferred.
"""
from fractions import Fraction
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

def quotient_length(n, k):
    generators = [(2*n, 0), (2, 2*n-2), (0, 4*n)]
    powers = []
    for i in range(k+1):
        for j in range(k-i+1):
            l = k-i-j
            powers.append((i*generators[0][0]+j*generators[1][0],
                           j*generators[1][1]+l*generators[2][1]))
    count = 0
    # A difference of two M exponents is in M automatically. Membership
    # therefore asks only coordinatewise domination by a product exponent.
    for x in range(2*n*k):
        least_y = min(y for gx, y in powers if gx <= x)
        count += (least_y+1)//2 if x % 2 == 0 else least_y//2
    return count

lengths = []
for n in range(1,9):
    vals = [quotient_length(n,k) for k in range(1,9)]
    # Independent finite differences, compared with the proved coefficient.
    differences = [vals[i+2]-2*vals[i+1]+vals[i] for i in range(6)]
    lengths.append({'n':n, 'k_1_to_8_lengths':vals,
                    'second_differences':differences,
                    'proved_multiplicity':2*n*n+2*n,
                    'all_differences_match':all(d==2*n*n+2*n for d in differences)})

pairs = [(Fraction(1), Fraction(j,2)) for j in range(2,10)]
pairs += [(Fraction(j,2), Fraction(1)) for j in range(3,10)]
pairs += [(None, Fraction(1)), (Fraction(1), None)]
profiles = []
for n in range(1,17):
    for a,b in pairs:
        def monomial_value(x,y):
            if (x and a is None) or (y and b is None):
                return None
            return x*(a or 0)+y*(b or 0)
        raw = [monomial_value(n,0), monomial_value(1,n-1), monomial_value(0,2*n)]
        value = min(t for t in raw if t is not None)/n
        formula = Fraction(2) if a is None else (Fraction(1) if b is None or a<=b else min(Fraction(1)+(a-1)/n,Fraction(2)))
        profiles.append({'n':n, 'a':str(a) if a is not None else 'infinity',
                         'b':str(b) if b is not None else 'infinity',
                         'minus_profile':str(value),'matched':value==formula,
                         'bounded':1<=value<=2})

report = {'finite_only':True,'n_k_domain':'1<=n,k<=8',
          'profile_domain':'1<=n<=16; 17 explicitly listed rational/infinite pairs',
          'length_cases':64, 'difference_cases':48*1,
          'profile_cases':len(profiles), 'lengths':lengths,'profiles':profiles,
          'all_passed':all(row['all_differences_match'] for row in lengths) and
                       all(row['matched'] and row['bounded'] for row in profiles),
          'limitations':'No finite-window extrapolation, topology, positivity or energy theorem is certified. See n5 for universal proofs.'}
(HERE/'evidence'/'finite-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['length_cases','difference_cases','profile_cases','all_passed']}))
if not report['all_passed']:
    raise SystemExit(1)
