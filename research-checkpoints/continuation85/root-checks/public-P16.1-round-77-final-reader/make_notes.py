#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re

root=Path(__file__).resolve().parent
paper=(root/'P16.1-argument.md').read_text()
def section(n):
    start=paper.index(f'## {n}. ')
    m=re.search(r'^## (?:\d+\. |Primary bindings)',paper[start+1:],re.M)
    end=start+1+m.start() if m else len(paper)
    return paper[start:end].strip()
def save(name,value):
    (root/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
bindings=paper[paper.index('## Primary bindings'):].strip()
build=json.loads((root/'build-report.json').read_text())
execution=json.loads((root/'execution-report.json').read_text())
page_count=int(re.search(r'Output written on .*?\((\d+) pages', (root/'build-logs/pdflatex-pass2.log').read_text()).group(1))
artifact=('\n\nArtifacts in this workspace: P16.1-argument.md, P16.1-paper.tex and P16.1-paper.pdf. '
          'Rerun: python3 rerun.py. Exact versions, whole-file hashes and inclusive one-based UTF-8 decode/split("\\n") '
          'LF excerpts are in source-extracts/source-provenance.json. These are unverified mathematical drafts; '
          'execution does not validate their correctness. No supplied draft was used as an accepted result.')
context=('Retain k algebraically closed, trivially valued and characteristic zero; X reduced irreducible projective; '
         'actual ample rational line bundles. The binding contact class consists of finite continuous rational-affine '
         'selections in analytic-unit logs on ordinary neighborhoods, with an affine support below and equal at the '
         'tested point with the SAME constant; finite-floor maxima use inactive-zero reductions. Decreasing local '
         'sequences are supplied on common neighborhoods. This is not an unrestricted positive-current converse.\n\n')
notes=[
 {'id':'n1',
  'summary':'Constructed exact compact algebraic rational PL extensions, subordinate PL partitions and same-bundle FS differences. They give an algebraic representation first for supplied continuous contact metrics, removing the arbitrary-formal-line-bundle algebraization gap; no approximation theorem for every weak metric is claimed.',
  'detailedSummary':'For reduced irreducible projective X over any algebraically closed trivially valued characteristic-zero k, finite rational selected unit-log weights admit exact compact algebraic PL extensions after original-ring principal localization and rational norm-image subdivision. Saturation cutoffs control support without multiplying variable PL functions. Every finite signed test decomposes exactly into two genuine FS metrics in one actual ample RH with the original cocycle. A supplied globally glued ample rational contact metric is first represented by BJ flag ideals, then tested on ordinary curve neighborhoods, giving nefness of its already algebraic Laurent model. Same-class FS approximation and an exact Gauss coefficient cutoff yield genuine membership. The result requires the explicit contact representation and does not globally regularize arbitrary continuous weak inputs.',
  'text':context+'\n\n'.join(section(i) for i in [2,3])+'\n\n'+bindings+artifact,
  'support':[]},
 {'id':'n2',
  'summary':'Reconstructed genuine bounded collars and signed compact IBP, including outside-support cancellation. A support-controlled telescope gives exact raw mixed mass; comparison, atom-based local domination and EP-based smooth membership follow for the specified contact class.',
  'detailedSummary':'Using n1 and the genuine primary global mixed pairing, bounded decreasing local contact tuples have reference-winning collars in a fixed actual ample bundle; their canonical potentials include the global reference p, and their raw products retain A^n scaling. Shared-collar comparison proves independence and genuine weighted convergence. Compact signed tests have same-class FS decompositions whose positive measures cancel outside the support; they need not individually vanish there. Extending the actual local reference near that support makes compact IBP a symmetric global pairing. Rational PL partitions yield raw mass (L_1...L_n) by telescoping. Genuine winning loci yield local comparison; a positive atom on an ample model avoids an inverse Dirac theorem in domination. With genuine EP, continuous-majorant nets and orthogonality establish first membership. Smooth characteristic-zero EP supplies the smooth instance; arbitrary singular EP is not assumed.',
  'text':context+'n1 supplies the exact extensions, actual metric representation and continuous contact membership used here.\n\n'+'\n\n'.join(section(i) for i in [4,5,6])+artifact,
  'support':['n1']},
 {'id':'n3',
  'summary':'Derived smooth weak UPPER-growth AFS regularization and exact principal-open removal after n2 establishes first membership, with standard geometric witness construction explicit. Independently audited canonical positive nonflat norm weights and whole-base finite AFS formulas; the weak radial trace application remains unfinished.',
  'detailedSummary':'Assume a smooth ample-boundary compactification and smooth projective domination of the one original proper birational contact witness, as furnished by explicitly retained characteristic-zero geometric background. Smooth nef local/global equality from n2 gives genuine membership to whole-floor boundary truncations; BJ5.13 is then used only on a smooth target with approaching target-side EP. BJ12.18 follows membership, and actual section localization plus low complete-system branches preserves the original affine generators. Expanding collars give controlled 2g+B bounds. Floors of v+c log|f| extend across Z(f), smooth tail envelopes remove c, and common-reference divisorial order on the one original resolved witness identifies every removed-set value. Separately, generic norm polynomial laws specialize across nonflat fibers; Cayley-Hamilton forces positive residue-character exponents, giving integer weights totaling d and exact arbitrary-radius Gauss formulas. These finite laws do not alone identify a general weak trace at nonflat points.',
  'text':context+'The analytic deduction uses n1 and n2. Its geometric compactification/domination premise and its remaining radial-trace limitation are explicit below.\n\n'+'\n\n'.join(section(i) for i in [7,8])+artifact,
  'support':['n1','n2']},
 {'id':'n4',
  'summary':f'Delivered a {page_count}-page standalone unverified partial paper, exact input preservation, pinned primary evidence and rerun checks. Genuine singular existence remains conditional on unfinished whole-base weak trace, singular Runge/EP, finite-data descent and normalization compatibility; candidate=false.',
  'detailedSummary':'The exact unchanged target and full family are preserved. n1-n3 add compact PL/IBP and smooth-gate proof drafts rather than merely repeating earlier notes. BJ already supplies the genuine general-variety finite-energy operator, raw mass V, intrinsic finite-dual-energy condition and uniqueness modulo constants; its actual 12.8 makes singular existence depend on EP. The missing applications include the whole weak radial trace, split-piece/descending-Z/Hartogs/reduced-strata chain, resolved-nef fiber constancy, countable rational unibranch EP, arbitrary-cardinality finite-data descent with relative integral closure and positive mass, and target-side normalization onto with E1/MA compatibility. Observed checks: input-original.json equals input.json byte for byte, all 23 primary hashes match, 43 literal units are pinned, all 4,467 declared finite cases pass, and Pandoc plus both pdfLaTeX passes succeed. None proves the mathematics.',
  'text':section(1)+'\n\n'+section(9)+'\n\n'+section(10)+
       '\n\nObserved execution details: input.json and input-original.json are '+str(execution['input_bytes'])+
       ' bytes with SHA256 '+execution['input_sha256']+'. All 23 supplied primary-file hashes match. '
       'The 43 literal units use inclusive one-based LF coordinates from UTF-8 bytes decode and split("\\n"). '
       'The 4,467 finite cases consist of 625 saturation partitions, 225 support-clipping values, 392 collar-margin cases, '
       '100 summable-shift inequalities and 3,125 quadratic norm identities. Pandoc and both pdfLaTeX passes return zero; '
       'the final PDF has '+str(page_count)+' pages. TeX SHA256 '+build['tex_sha256']+'; PDF SHA256 '+build['pdf_sha256']+'. '
       'Both full pass logs and exact commands are retained in build-logs and build-report.json. '
       'An initial malformed YAML header caused a failed build; it was corrected, and the initial failure outputs remain in build-logs/initial-failed-*. '
       'Compilation, finite arithmetic and hash equality are observations, not proof validation.\n\n'+
       'Artifacts: P16.1-argument.md, P16.1-paper.tex, P16.1-paper.pdf, status.json, canonical-notes.json, '
       'mathematical-audit.json, input-original.json, task-original.json, assignment-original.txt, source-extracts/source-provenance.json, '
       'finite-checks.json, execution-report.json and build-report.json. Rerun python3 rerun.py; then python3 make_notes.py; then python3 validate.py. '
       'No operator-provided supervised compute service was exposed; no resource-heavy computation was needed or launched. '
       'The unchanged original P16.1 completion criterion remains unmet. Candidate=false.',
  'support':['n1','n2','n3']}
]
save('canonical-notes.json',notes)
save('result.json',{'notes':notes,'candidate':False})
gaps=[
 'Whole-base weak trace: original-witness curve lifts, normalized slices, all completed residue-field extensions, Gauss-fiber weights and limiting equality must be checked together.',
 'Singular split-piece maximum, descending-Z, Runge-before-Hartogs, reduced-strata and final empty-Z globalization remain unreconstructed.',
 'Actual varying-reference nef fiber constancy, geometric connectedness, divisorial minimum-usc descent and countable rational geometrically unibranch EP remain to establish.',
 'Arbitrary-cardinality finite-data descent must preserve actual nonnormal generic fibers, relative integral closure, vertical R1/S2, positive raw mass, orthogonality and domination; arbitrary PSH competitors cannot simultaneously descend.',
 'Target-side approaching EP, degree-one fundamental-cycle projection and unbounded E1/MA normalization compatibility must precede unconditional singular variational compactness, differentiation and attainment.'
]
save('status.json',{'id':'P16.1-round77-compact-IBP','status':'partial',
 'exact_result':'Unverified source-based drafts establish exact compact rational PL extensions and same-bundle representation for supplied contact metrics, signed compact IBP and raw-mass/comparison/domination, and EP-based smooth membership. Smooth upper-growth/removal is derived with the standard geometric witness premise explicit. The requested singular existence theorem is not proved.',
 'proof_file':'P16.1-paper.tex','concrete_gaps':gaps})
save('mathematical-audit.json',{
 'candidate':False,
 'unverified_drafts':True,
 'new_deductions':['original-ring compact PL extensions and support gluing','algebraic model first, avoiding arbitrary formal bundle algebraization','signed compact pairings and controlled outside cancellation','raw mixed mass telescope and atom-based local domination','smooth first membership before sequential approximation','controlled upper-growth removal with actual original-witness values'],
 'primary_inputs':['BJ PL lattice, flag-ideal representation, genuine pairings, locality, domination, smooth EP and same-class regularization','Ducros compact Gamma-strict unit norm images and rational-domain density','Thuillier harmonic unit logs, maximum principle and decreasing subharmonic limits','GR represented PL curve test and GM proper residual-curve nefness','BE same-bundle continuous FS and actual continuous Deligne comparison'],
 'retained_background_premises':['characteristic-zero resolution, projective domination/Chow construction and smooth ample-boundary compactification','the formal-model refinements and analytic curve results in the pinned primary theorem proofs'],
 'not_imported':['arbitrary positive-current converse','global rational weak approximants for every continuous weak metric','arbitrary-field affine regularization','printed LOWER growth','arbitrary PSH simultaneous countable descent','normalization onto without target-side EP'],
 'concrete_gaps':gaps,
 'execution_is_not_validation':True})
save('initial-build-diagnostic.json',{'command':['python3','rerun.py'],'returncode':1,
 'cause':'Malformed header-includes YAML prevented Pandoc from producing TeX; rerun.py then reported FileNotFoundError for P16.1-paper.tex.',
 'correction':'Valid YAML sequence restored; build-report.json now records successful Pandoc and both TeX passes.',
 'retained_outputs':'build-logs/initial-failed-*'})
print(json.dumps({'notes':len(notes),'note_characters':[len(n['text']) for n in notes],
 'status_keys':list(json.loads((root/'status.json').read_text()))}))
