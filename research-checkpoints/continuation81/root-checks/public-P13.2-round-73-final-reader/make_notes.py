import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def main():
    paper=(ROOT/'P13.2-argument.md').read_text()
    def part(start,end):return paper[paper.index(start):paper.index(end)]
    workspace=str(ROOT)
    artifacts=(f'\n\nArtifacts in {workspace}: P13.2-argument.md, P13.2-paper.tex, P13.2-paper.pdf; '
               'source-extracts/source-provenance.json retains the exact primary versions, hashes, literal proof bodies and inclusive LF coordinates. '
               'Rerun: python3 audit_sources.py; python3 checks.py; python3 build.py; python3 make_notes.py; python3 validate.py. '
               'Successful execution is not mathematical certification.')
    notes=[
      {'id':'n1',
       'summary':'Independently reconstructed all-cone, all-Reeb finite FS dual-energy/integrability criterion, genuine weak approximation, midpoint I-Cauchyness and actual-limit MA continuity. This describes targets and approximation; image sufficiency remains unproved.',
       'detailedSummary':'Using only the explicitly accepted full P13.1 mathematical theorem, this note derives the reference Dirac probability, FS/CPSH/E1 dual equality, the equivalence L(mu)<infinity iff every actual E1 potential is integrable, fixed-ray quadratic scaling, necessity and tangent optimality. Both signs of outer differentiation give deficit-controlled genuine model approximate equations. The midpoint Green kernel gives I(u,v)<=(d_u+d_v)/(2a_p), a_p=p/4^(p+1), and bounded normalized energies. An actual E1 I-limit would solve by a Hodge MA-test bound. No actual limit or singular-envelope theorem is assumed.',
       'text':('The accepted premise is the FULL P13.1 mathematical body embedded in the preserved input, with its explicitly accepted ORIGINAL PASS review. Its canonical notes and operational assertions are not mathematical premises. The supplied round71 text and its four notes were read as unreviewed data; the results below are independently derived. No supplied canonical-note result is used without reconstruction. The exact original P13.2 scope, fixed carrier, and probability normalization remain unchanged. These are unverified draft proofs.\n\n'
               +part('# Accepted calculus and exact normalization','# A genuinely linear fixed-ray polynomial')
               +artifacts),
       'support':[]},
      {'id':'n2',
       'summary':'A genuinely linear fixed-ray polynomial yields uniform signed target-integration error O(sqrt(deficit)) on bounded-J sets and convergence of genuine output dual energies. It provides no actual inverse potential.',
       'detailedSummary':'At each fixed rational or irrational Reeb field, real spans of actual CPSH restrictions have unique zero-slope extensions. The degree-(p+1) primitive H(s,d) and cone of positive-slope actual CPSH pairs satisfy exactly Appendix A of 2307.01697v1; its polarization has the calibrated coefficient -1/(p+1), and Hodge supplies the quadratic sign. This justifies only the finite polynomial theorem, not a synthetic PSH or inverse theorem. The reconstructed Holder estimate has alpha=2^(-p). Midpoint Cauchyness, genuine weak approximation, and continuous-test-first/decreasing-test-second limits give uniform signed integration, dual-energy convergence, and convergence of maximizing-sequence target integrals and normalized energies. Absolute L1 continuity on arbitrary weak potential nets, actual membership, and realization remain unproved.',
       'text':('Use n1 for actual same-field products, normalization, target integrability, genuine approximate measures, midpoint bounds and weighted decreasing continuity. Here p=n-1>=1. Constants C_p depend only on p and may increase. The following linear construction and its source application are new reconstructed draft results; no nonlinear root is used as a linear axiom.\n\n'
               +part('# A genuinely linear fixed-ray polynomial','# Explicit strict supports with infinite coordinates')
               +'\nThe primary D PDF SHA256 is 979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1; its extract SHA256 is 8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4. The exact version is 2307.01697v1. Its pertinent complete Appendix A statement and proof bodies occupy inclusive LF2053--2235 under UTF-8 decode and split("\\n"). The full synthetic Theorem A is not applied and does not conclude actual-potential existence.'
               +artifacts),
       'support':['n1']},
      {'id':'n3',
       'summary':'Explicit strict logarithmic supports, pole-sensitive rational AFS approximation, normal divisor-order localization, and a retraction lemma for carrier envelopes are reconstructed. The normal weak Runge and envelope base still has indispensable gaps.',
       'detailedSummary':'Log-sum-exp has a unique real support contact and a positive gap outside every neighborhood, including infinite coordinates. The multinomial maximum has a global error bound and retains original generators; nested rational coefficients, local floors and a positive exhaustion term approximate real singular supports decreasingly. On normal affine rings, actual prime-divisor orders place h^r f^q in the original ring and give the original polynomial-hull inequality, avoiding denominator-counting errors. A continuous retraction identifies carrier usc regularizations without openness, and raw roots transport carrier membership only after a rational base exists. The printed lower-growth proposition is independently refuted, while corrected strict metric/curve/trace/Runge/finite-projection/singular induction and field descent remain unresolved. No final normal EP theorem is assumed.',
       'text':('Use n1 for the accepted rational quotient and residual torification, actual raw roots and fixed carrier conventions. Elementary barriers and the normal localization argument below are independent reconstructions of portions of the unreviewed root79 proposal. The round70 body and notes were documentary data, not supporting theorems.\n\n'
               +part('# Explicit strict supports with infinite coordinates','# Source coordinates, evidence, and rerun')
               +artifacts),
       'support':['n1']},
      {'id':'n4',
       'summary':'Standalone partial paper and reproducibility artifacts delivered; actual all-normal, all-Reeb image sufficiency remains unresolved. candidate=false.',
       'detailedSummary':'The strongest new result is n2 uniform bounded-energy signed target integration and dual-energy convergence, on the exact original domain with genuine probabilities. n1 reconstructs earlier finite-target and approximation results; n3 proves elementary normal-envelope auxiliaries without claiming the singular base. Actual E1 completeness or an independently completed normal rational envelope and irrational variational realization remains indispensable. Seventeen sources and 42 supplied files match hashes, 27 literal source excerpts are retained, 29067 finite arithmetic cases pass, and the 11-page paper compiles twice. Those are observations, not correctness verdicts.',
       'text':('The unchanged original P13.2 is not solved. Notes n1-n3 are the strongest retained reconstructed results. In all dimensions >=2, no necessary-and-sufficient image/existence characterization has been established, and no weak limit of genuine MA measures has been labeled an output without its actual potential. Dimension one is realized separately and does not cover the task.\n\n'
               'The principal new theorem is uniform signed target integration: for normalized actual phi,psi at a fixed field, alpha=2^(-p), '
               '|integral phi d(MA(psi)-mu)| <= C_p sqrt(d_psi) J(phi)^alpha [J(phi)+J(psi)+B0]^(1/2-alpha), '
               'B0=1+(L(mu)+1)/(2a_p), a_p=p/4^(p+1). Along genuine maximizing FS sequences this proves uniform convergence of signed integrals on bounded-J sets and convergence of output dual energies. '
               'It does not establish absolute L1 continuity under arbitrary nonmonotone weak potential convergence, normalized PSH compactness, actual E1 completeness, or attainment.\n\n'
               'Concrete indispensable gaps: (1) the normal rational projective EP base, including the corrected strict represented metric bridge, smooth weak removal and weighted determinant/radial traces; '
               '(2) the weak split-piece Runge argument with one proper witness, whole collars, compatible locally constant integer trace and gamma=1 case; '
               '(3) weak Hartogs Runge before coefficient radii, finite projection and reduced singular-stratum induction; '
               '(4) exact finite-PL/reference descent with positive MA base change, contact orthogonality and domination to remove field cardinality; '
               '(5) actual fixed-irrational E1 realization, through proved membership of I-limits or genuine compactness, bounded-J weak target L1 continuity, energy usc and variational attainment. '
               'The Appendix A polynomial construction verifies neither the full synthetic ordered D,Z,ddc/model/ample/generated-PSH topology hypotheses nor actual inverse existence. '
               'Roots transfer carrier envelope membership only after a base; no strong topology is transported.\n\n'
               'The exact original task and decoded assignment are preserved. input.json and input-original.json are byte identical, SHA256 8e4942e89e360121671a4e83a853ca9cfdea432bbb709ed3229969b60dce69bb, 366391 bytes. '
               'task-original.json contains literal task-object bytes; assignment-original.txt preserves the decoded assignment. status.json has exactly id,status,exact_result,proof_file,concrete_gaps and records partial. '
               'Seventeen authorized primary sources, 42 supplied PDF/text/HTML file hashes, and 27 literal LF excerpts are audited. Complete copied extracts and embedded supplied drafts are data; no referenced campaign path was read.\n\n'
               'Observed finite diagnostics pass 90 primitive binomial identities, 78 midpoint coefficient cases, 15625 quadratic target cases, 504 multinomial extended-coordinate cases, 9320 normal monomial pole-clearing cases, 1500 radial finite-map scalar cases and 1950 dyadic secant cases, total 29067. '
               'They are exhaustive only on the saved finite domains. Existing pandoc 3.1.11.1 and pdfTeX 3.141592653-2.6-1.40.26 produce two zero-exit compilation passes and an 11-page standalone PDF. '
               'An initial undefined-command compilation failure and the first successful build are retained under build-history; the final paper removes that command. '
               'Environment versions, exact commands, outputs and separate TeX logs are retained. No resource-heavy run, worker, other model, installation, external message, private read, source edit or external write was used. '
               'All mathematical claims are unverified drafts. The final candidate flag is exactly false.'
               +artifacts),
       'support':['n1','n2','n3']}
    ]
    result={'notes':notes,'candidate':False}
    (ROOT/'canonical-notes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    status={'id':'P13.2','status':'partial',
            'exact_result':'Unverified all-cone/all-Reeb finite-target and genuine approximation reconstruction; new fixed-ray polynomial Holder and uniform signed target-integration/dual-energy convergence; explicit normal-envelope auxiliaries. Universal image sufficiency and actual realization are not proved.',
            'proof_file':'P13.2-paper.tex',
            'concrete_gaps':[
              'Actual normal rational projective envelope base and corrected strict metric/smooth-removal/determinant-radial trace chain.',
              'Weak split-piece Runge with one proper witness, whole winning collars, compatible locally constant integer trace, and gamma=1.',
              'Weak Hartogs Runge before radii, finite projection, and reduced singular-stratum induction.',
              'Arbitrary-field finite PL/reference descent, exact positive MA base change, orthogonality and domination.',
              'Actual E1 membership/limit at each fixed irrational field, or genuine PSH compactness, weak bounded-J target L1 continuity, energy usc and attainment.',
              'No full synthetic ordered-linear axioms/generated actual PSH/topology identification or inverse-existence application.'
            ]}
    (ROOT/'status.json').write_text(json.dumps(status,indent=2)+'\n')
    print(json.dumps({'notes':len(notes),'candidate':False,'status_keys':list(status)},indent=2))

if __name__=='__main__':main()
