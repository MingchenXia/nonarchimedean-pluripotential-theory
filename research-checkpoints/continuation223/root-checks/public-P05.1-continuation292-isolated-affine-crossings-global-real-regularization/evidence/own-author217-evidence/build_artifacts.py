"""Own prose exporter and native-note packager; no supplied code is executed."""
import json
import re
import subprocess
from pathlib import Path

result = subprocess.run(['pandoc', '-s', '-f', 'latex', '-t', 'markdown', '--wrap=none',
                         'P05.1-paper.tex'], capture_output=True, text=True, check=True)
Path('argument.md').write_text(result.stdout)
Path('markdown-build.log').write_text(result.stderr or 'Pandoc conversion exit 0; no warnings.\n')

body = result.stdout
starts = [(m.start(), m.group(1)) for m in re.finditer(r'^# (.+)$', body, re.M)]
sections = {}
for j, (start, name) in enumerate(starts):
    end = starts[j + 1][0] if j + 1 < len(starts) else len(body)
    name = re.sub(r'\s*\{#[^}]+\}\s*$', '', name)
    sections[name] = body[start:end].strip()
def section(name):
    return sections[name]

notes = [
 {'id': 'n1',
  'summary': 'Exact five-grant and primary-source boundary; R230 gives actual continuous envelopes, S272 gives raw completion only on the genuine global approximation domain. Historical210 INCONCLUSIVE and all restrictions retained.',
  'detailedSummary': 'All 23 bound files match hashes and sizes. Entire five grant TeX bodies, all clarifications/ledgers/material changes, and WHOLE288 with embedded287 were covered. Whole redundant S262 Markdown agrees exactly with its TeX conversion; S272 agrees after disclosed presentation normalization. BBGS/BMPS immediate source units and real signed/zero primitive conversion are documented. No source automatic continuity, literal density, extra factorial, delegated AR10, unbound output or source program is used. These are dependency declarations and provenance observations, not acceptance.',
  'text': section('Dependency boundary and retained foundations') + '\n\n' + Path('source-application-ledger.md').read_text() + '\nArtifacts: input-verification.json, whole-grant-body-comparison.json, source-application-ledger.md, verify_inputs.py. Rerun: python verify_inputs.py. Source excerpts remain LOCALONLY. No supplied notes were present; named packets are recorded as inputs here rather than invalid support IDs.',
  'support': []},
 {'id': 'n2',
  'summary': 'Proved continuous-PC criterion: ordinary convexity on every complete branch and a common ambient supporting form at each rational crossing, including arbitrary branch dependencies.',
  'detailedSummary': 'Inherited rational feasible midpoint triples establish full branch convexity without coarsening; a strict quadratic maximum argument avoids a hidden uniform-local-radius premise. Finite convex subgradients are nonempty compact with continuous directional support functions. Separating their compact product from the closed ambient restriction subspace yields an ambient zero-sum tuple of negative directional cost. Rational kernel approximation and a common small rational scale produce a genuine legal finite printed violation. Sufficiency uses the common support at vertices and branch Jensen elsewhere.',
  'text': section('Rational incidence and ordinary convex facts') + '\n\n' + section('A common support at each dependent crossing') + '\nArtifacts: P05.1-paper.tex and argument.md contain these full proofs. All arguments here are finite-dimensional mathematical proofs, independent of execution and grant authority.',
  'support': []},
 {'id': 'n3',
  'summary': 'Proved global full-affine above approximation touching any prescribed finite rational sample set exactly, with actual possibly irrational recession polytope and rational spatial carriers.',
  'detailedSummary': 'The actual reference gradient polytope is not rounded. Its epigraph recession has rational spatial rays with real heights. The conjugate is finite and continuous on the entire closed polytope, including its boundary, by an active/inactive slack extension proof. Compactness selects finite rational samples. The closed sample hull plus exact recession cone has a finite convex lower boundary; its conjugate error gives a whole-space bound. Every lower face projects to rational spatial generators and projected face intersections are preserved. Appending samples preserves all error, exact recession and support minorants.',
  'text': section('Global approximation on one full affine branch') + '\nArtifacts: P05.1-paper.tex and argument.md. This is a mathematical proof over all real points, not a finite computational density result. The finite sample statement gives no interpolation on a positive-dimensional overlap.',
  'support': ['n2']},
 {'id': 'n4',
  'summary': 'Proved scoped universal global decreasing REAL regularization and actual C_b envelope domain membership on finite point-intersection complete affine arrangements; original classification remains OPEN.',
  'detailedSummary': 'All finitely many branch intersection points are included as exact samples. Above approximants retain every common support and glue after rational vertex refinements. With eta_n=2^−n, G_n=F_n+4eta_n has 4eta_n≤G_n−f≤5eta_n and next upper bound 2.5eta_n<4eta_n, giving strict global decrease and one common relative bound, with unchanged actual recession. R230 is applied exactly for the unrestricted C_b envelope, and S272 only after this genuine approximation antecedent. Non-PA/coupled obstacles are included without global obstacle-density assumptions.',
  'text': section('Exact domain and theorem') + '\n\n' + section('Gluing every crossing and a genuinely decreasing sequence') + '\nArtifacts: P05.1-paper.tex, argument.md, proof-coverage.md, scope-and-gaps.md. This proves precisely the specified geometric theorem relative to the declared R230/S272 grants. Candidate=false; original P05.1 and P05.2 remain OPEN.',
  'support': ['n1', 'n2', 'n3']},
 {'id': 'n5',
  'summary': 'Exact dependent R4 negative PCC and crossing contact obstruction for every admitted actual REAL reference; saturated raw determinant factors, repeated zeros and d! orders are proved.',
  'detailedSummary': 'The value-only gluing example has rational equal-weight average −1/6 at zero, and no ambient common support. At any crossing a saturated complete branch and rational transverse line yield a rational ambient absolute-form germ with flat PCC and positive raw atom 2^d d! sum c_i|det A_i|. The actual positive complete subcycle has an effective balanced residual. Primitive quotient factors telescope after row denominators; repeated factors vanish and d! counts actual surviving orders. Covolume conversion reproduces BBGS real signed/zero unit-normal recursion at every dimension. The actual-reference positive convex decomposition realizes one identical flat germ in every rational reference summand; a genuine finite PA rational roof proves the unrestricted envelope and exact negative contact. No full disjoint contact claim is made.',
  'text': section('An exact dependent three-plane diagnostic') + '\n\n' + section('Primitive raw calibration and all recursive factors') + '\n\n' + section('Every crossing has an actual-reference negative-contact witness') + '\nArtifacts: P05.1-paper.tex, argument.md, source-application-ledger.md, check_certificates.py, certificate-input.json and certificate-output.json. Rerun the bounded listed algebra: python check_certificates.py. The contact witness is finite PA before its raw measure is assigned.',
  'support': ['n1', 'n2']},
 {'id': 'n6',
  'summary': 'Delivered 17-page scoped author paper, full proof/source coverage and reproducibility artifacts. Listed exact checks pass and local build succeeds; none certifies continuum mathematics or original closure. Candidate=false.',
  'detailedSummary': 'Five matrix cases exhaust thirteen mixed permutations and forty listed factor words, including twenty-seven repeated zeros; the dependent PCC and three distinct affine meetings are exact. Initial truncated reads, presentation-comparison failures and first-build warnings are retained. The second safe LaTeX pass has no warnings. All programs are fresh own code, all writes are within the artifact directory, and no network/agent/heavy compute/source mutation occurred. Notes are unverified drafts; original P05.1/P05.2 and excluded domains remain open.',
  'text': section('Coverage, limits, and reproducible evidence') + '\n\n' + Path('scope-and-gaps.md').read_text() + '\n\n' + Path('execution-log.md').read_text() + '\nDeliverables: P05.1-paper.tex, P05.1-paper.pdf (17 pages), argument.md, source-application-ledger.md, scope-and-gaps.md, proof-coverage.md, native-notes.json, artifact-bindings.json, artifact-bindings.sha256, environment.json, input-verification.json, whole-grant-body-comparison.json, verify_inputs.py, check_certificates.py, certificate-input.json, certificate-output.json, build_artifacts.py, bind_artifacts.py, build-pass1.log, build-pass2.log, build-results.json, checks.log, input-checks.log, markdown-build.log and execution-log.md. Rerun commands are stated above. LOCALONLY primary excerpts are marked local-only in the manifest. Native FINAL is controlling; no substantive saved/final discrepancy is intended. Candidate=false even with the scoped theorem proved; no independent acceptance or original closure is claimed.',
  'support': ['n4', 'n5']}
]
Path('native-notes.json').write_text(json.dumps({'notes': notes, 'candidate': False}, ensure_ascii=False, indent=2) + '\n')
print('Exported own complete argument and six native notes; candidate=false.')
