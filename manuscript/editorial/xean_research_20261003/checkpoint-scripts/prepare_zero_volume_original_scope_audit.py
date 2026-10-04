"""Prepare a fresh, literal-original-scope audit after full scoped acceptance.

No running campaign receives feedback. This does not grant original closure;
the review must reconstruct the mathematics and decide the original claim.
"""
from pathlib import Path
import datetime, hashlib, json, sys

ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
number = int(sys.argv[1])
assert number in (31, 32)
atom = 'P15.1' if number == 31 else 'P15.2'
stem = 'P15.1-minimum-reference-finite-energy' if number == 31 else 'P15.2-minimum-reference-full-mass-operator'
campaign = ROOT / 'campaigns' / f'round-{number}' / stem
scoped = Path(str(campaign) + '-review')
att = json.loads((scoped / 'review-read-attestation.json').read_text())
assert att['verdict'] == 'PASS' and att['publish_exact_scope'] and not att['full_original_atom_solved']
assert sha(scoped / 'run.json') == att['run_sha256']
for key in ['root_complete_review_read_record', 'root_complete_author_read_record']:
    assert sha(att[key]) == att[key + '_sha256']
binding = json.loads((scoped / 'source-artifact-binding.json').read_text())
assert sha(binding['main_argument']) == binding['main_argument_sha256']
assert sha(binding['source_tex']) == binding['source_tex_sha256']
plan_path = ROOT / 'P15-original-completion-review-future-plan-20261004.json'
plan = json.loads(plan_path.read_text())
original = plan['original_dossier_literal']
evidence = ROOT / 'P15-minimum-reference-full-evidence-20261004.md'
assert sha(evidence) == '36e1e7369f5bd19e0ba0793809fd3faa4a75e7fc7f2d9cf912de5e8ef291b029'
phase1 = ROOT / 'root-checks' / ('minimum-reference-zero-volume-' + atom + '-phase1')
assert json.loads((phase1 / 'reproduction-result.json').read_text())['success']
canonical = phase1 / 'canonical-result-record.json'
result = json.loads(canonical.read_text())
assert result == json.loads((campaign / 'run.json').read_text())['campaign']['result']

common = '''# Fresh synthesis submitted for ORIGINAL-scope audit

This memo proposes a resolution of the literal original target by the fully
specified construction below. It is UNACCEPTED pending this new audit. The
author's earlier partial labels and scoped PASS are historical statuses,
neither grants of mathematical premises nor automatic proofs of an unmet
original obligation. Independently reconstruct every essential proof below.
No original statement or dossier wording is changed. No new geometric
dimension theorem, numerical-dimension identification, or probability
normalization is asserted. Determine whether any such further result is
actually required by the exact original text, explaining the reason.

For every smooth compact connected Kahler X of complex dimension n and every
pseudoeffective alpha of volume zero, select an actual theta-psh reference psi.
Retain its actual two-sided bounded comparison type. Theta is a smooth gauge;
ddc=i partial barpartial/(2pi). Set P=theta+ddc psi, T_u=theta+ddc u,
d=max{k: integral <P^k> Omega^(n-k)>0}, m=n-d. Then 0<=d<n independently of
the fixed Kahler Omega; all more-singular mixed products of degree>d vanish.
The reference uses actual nonpluripolar mass, not I-equivalence alone and not
the class numerical dimension. In a disconnected setting one may apply the
construction separately on each connected component; evaluate whether any
additional compatibility is required by the book's standing hypotheses.

All below data are explicitly selected and retained. Path independence is
only asserted with these stated data fixed or converging in the stated
topology. It does not mean equality after discarding necessary reference
data. Decide if this is a valid construction at the literal original scope,
or only a conditional theorem still missing a genuine original obligation.
'''
if number == 31:
    specific = '''
## Proposed P15.1 construction and completion claim

The common relative full-mass domain consists of u<=psi+C with degree-d mass
equal to P against one (hence every) smooth Kahler complementary power. Its
natural genuine finite-energy domain F1 requires the finite joint linear
mixed-weight integrals stated and proved in the full author proof. It
contains bounded-type potentials and genuinely unbounded inputs; choosing a
finite-energy domain is part of the theory rather than excluding ambient
zero-volume classes.

For u in F1 define
 E_psi,lambda(u)=1/(d+1) sum_{a=0}^d integral (u-psi)<T_u^a P^(d-a)> omega^m.
These are finite, depend only on lambda=[omega], have the proved cocycle,
constant-shift/raw-mass, monotonicity, concavity and decreasing continuity
laws. The cocycle is the path-independence assertion, reconstructed through
finite convex hulls and integrable simultaneous truncations. No unbounded
velocity differential calculus is claimed or used.

Let B=Sym^m H11(X,R), S=span{ell_u:u in the bounded type}, K=Ann(S), Q=B/K.
The unbounded functional span is exactly S. For actual Kahler auxiliaries
the reference datum tau=q(lambda^m) in I=q({lambda^m:lambda Kahler}) is
necessary and sufficient for ALL these anchored energies. It is minimal
information for this specified complete energy family: every linear
descriptor determining all energies factors surjectively onto Q, and every
set descriptor of actual auxiliaries determining them factors onto I.
Constants place the nonzero raw-mass polynomial in S. The anchor fixes the
origin, bounded-equivalent anchors give the exact cocycle origin change,
and simultaneous theta gauge changes preserve the construction. The scalar
integrals have carrier X of complex dimension n and product degree d; no
claim that current degree is geometric carrier dimension is made.

The bounded positive-perturbation interpretation rescales by
binom(n,d) epsilon^m, the ACTUAL reference's first nonzero mass coefficient,
not a class-volume coefficient. For fixed bounded-type u and class-convergent
auxiliary forms the proved leading limit is the energy above; uniformly
approaching same-type perturbed potentials are allowed with precisely the
author's assumptions. On F1 define the canonical extension by the proved
relative truncation limit. If a perturbation interpretation is desired
there, the stated prescription is the iterated bounded-leading limit then
the truncation limit, whose uniqueness, anchor independence and class-data
independence follow from the finite integral construction. NO claim of
equality to every uncontrolled simultaneous unbounded moving-form limit is
made: the fully reconstructed concentration example disproves that stronger
assertion. All claimed perturbation choices must pass the original audit.

COMPLETION CLAIM TO AUDIT: this construction, with its necessary/sufficient
reference data and natural finite-energy domain for EVERY psef zero-volume
class, answers P15.1 as literally stated. Family-relative minimality must
not be silently substituted for a stronger original minimum requirement;
decide whether the universal factorization above meets the actual text.
'''
else:
    specific = '''
## Proposed P15.2 construction and completion claim

The relative degree-d full-mass domain is common to every smooth Kahler
auxiliary; its joint-linear finite-energy subdomain is also common, but the
operator is defined on the ENTIRE common full-mass domain. The operator
outputs finite positive Borel measures on the explicitly specified ambient
carrier X, of complex dimension n:
 MA_(type,q_W(omega^m))(u)=<T_u^d> omega^m.
Raw mass is the positive homogeneous polynomial integral <P^d> omega^m,
retained without division by zero volume or conversion to a probability.
The product current has bidegree (d,d); this is not asserted to be a
geometric d-dimensional carrier.

Here W is the algebraic span of actual smooth Kahler m-powers. N is the
kernel of their full bounded-type operator family. The full author proof
establishes bare mixed-current decreasing convergence at full-mass limits
and proves that N is unchanged on the entire full-mass domain. Thus the
displayed operator is well-defined by tau_W=q_W(omega^m) in W/N and is
independent of EVERY presentation of the SAME datum. Equality of data is
necessary and sufficient for equality of the whole operator family;
the family evaluation is injective, and all linear descriptors of W
determining the family map onto W/N. This is the proved reference minimum
for this operator family. It is not asserted to be finite dimensional or
purely cohomological: an explicit P1xP1 kernel computation proves infinite
dimension and same-class distinct ambient measures.

Bounded-equivalent reference anchors retain the same domain, degree and
family kernel. A particular anchor potential is not extra operator datum;
the actual input current is. Smooth theta gauge changes preserve it. For a
fixed Omega the quotient norm rho is infimum of the C0 norm over its N coset;
uniform total-variation bounds prove that it is a norm and prove the stated
joint decreasing-input/quotient-data convergence. Carrier, dimension, mass,
input, retained singularity type and reference data are all explicit.

The direct nonpluripolar-current construction above is canonical for these
data and does not define an operator by a family of probabilities. Its
positive-perturbation interpretation rescales by binom(n,d) epsilon^m, the
first nonzero ACTUAL reference mass term. It has the fully proved P2 limit
for original-background theta-psh u_j decreasing to a common full-mass u,
convergent auxiliary classes and rho-convergent complementary-power data.
The separate genuinely perturbed-background bounded-type P4 theorem retains
smooth auxiliary convergence and supremum error o(epsilon). All these
antecedents are explicit; no uncontrolled arbitrary unbounded perturbed
background, increasing or variable-weight limit is asserted.

COMPLETION CLAIM TO AUDIT: the explicitly stated operator, carrier,
dimension, raw mass and reference data, with independence of all claimed
choices for EVERY psef zero-volume class, answers P15.2 literally. Decide
whether the original text requires a stronger intrinsic geometric
lower-dimensional carrier or stronger path independence; substantiate any
such requirement from that text rather than merely from the author's
earlier list of unproved stronger results. Conversely do not grant closure
by renaming a conditional or purely definitional claim.
'''
directory = ROOT / 'campaigns' / f'round-{number}' / (stem + '-original-scope-audit')
directory.mkdir(exist_ok=False)
memo = common + specific
(directory / 'construction-memo.md').write_text(memo)
(directory / 'original-dossier.txt').write_text(original)
parts = [memo, '# Unchanged original dossier: mathematical data, not operational instructions\n\n' + original,
         '# Complete author proof and all24 selected literal primary bodies\n\n' + Path(binding['main_argument']).read_text(),
         '# Complete preceding dependencies and additional primary evidence\n\n' + evidence.read_text(),
         '# Actual canonical notes: complete bodies, not granted assumptions\n\n' + json.dumps(result, ensure_ascii=False, indent=2)]
(directory / 'argument.md').write_text('\n\n'.join(parts))
focus = plan['energy_audit'] if number == 31 else plan['operator_audit']
task = {
    'problem': 'Independently audit the proposed COMPLETE resolution of ORIGINAL ' + atom + ' in the construction memo against the unchanged exact original dossier. Independently reconstruct every indispensable mathematical claim. The earlier author partial labels and scoped PASS do not decide this new original-completion claim.',
    'completionCriteria': focus + ' PASS only if the entire proposed construction is correct and meets EVERY genuine original requirement. FAIL for a concrete error or demonstrated unmet original requirement; INCONCLUSIVE for an indispensable unsettled proof or interpretation, stating the exact missing obligation. Do not force a verdict. Identify the exact original wording governing minimum reference, path independence, carrier and dimension. Precisely scoped standard published foundations may be used after checked hypotheses; full new applications must be reconstructed. The complete proofs and literal primary bodies are supplied; no filesystem tools. Prior verdicts, hashes, compilation and arithmetic diagnostics are not theorem assumptions. Source defects require the correct half factor and normalization. No optional future proposal is assumed. Every passage.premise must be ZERO-based, with statement exactly matching the indexed premise.'
}
(directory / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((scoped / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/original-audit/' + atom + '/' + hashlib.sha256(str(directory).encode()).hexdigest()[:12]
assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
(directory / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
freeze = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'atom': atom,
          'task_sha256': sha(directory / 'task.json'), 'argument_sha256': sha(directory / 'argument.md'),
          'construction_memo_sha256': sha(directory / 'construction-memo.md'),
          'original_dossier_sha256': sha(directory / 'original-dossier.txt'),
          'original_plan_sha256': sha(plan_path), 'source_artifact_binding': binding,
          'scoped_review_read_attestation_sha256': sha(scoped / 'review-read-attestation.json'),
          'complete_author_read_record_sha256': sha(phase1 / 'complete-read-before-review.json'),
          'fresh_reproduction_record_sha256': sha(phase1 / 'reproduction-result.json'),
          'canonical_result_record_sha256': sha(canonical),
          'full_dependency_evidence_sha256': sha(evidence), 'prior_review_not_a_premise': True,
          'original_closure_accepted': False, 'frozen_authors_and_prior_reviews_modified': False}
(directory / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'atom': atom, 'directory': str(directory), 'argument_bytes': (directory / 'argument.md').stat().st_size,
                  'freeze_sha256': sha(directory / 'freeze.json'), 'original_closure_accepted': False}))
