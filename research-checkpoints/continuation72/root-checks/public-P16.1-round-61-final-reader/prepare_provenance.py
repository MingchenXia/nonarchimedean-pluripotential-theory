"""Preserve and excerpt only the six explicitly authorized primary caches."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
obj = json.loads((ROOT / 'input.json').read_text())
if not (ROOT / 'input-original.json').exists():
    shutil.copyfile(ROOT / 'input.json', ROOT / 'input-original.json')
assert (ROOT / 'input.json').read_bytes() == (ROOT / 'input-original.json').read_bytes()
assert (ROOT / 'assignment-original.txt').read_text() == obj['assignment']
assert json.loads((ROOT / 'task-original.json').read_text()) == obj['task']
manifest = json.loads((ROOT / 'source-manifest.json').read_text())

# Labels record the extent of the use, not an independent verdict on a paper.
SPECS = {
 '1801.08229v4': [
  (435,469,'General reduced-variety conventions','Reduced, possibly nonnormal projective scope; not a smooth-only operator.'),
  (740,758,'Complete-field restriction section','Only the section and surjectivity assertion actually stated here.'),
  (759,889,'Relative integral closure and vertical Serre criterion','Preserve the specified generic fiber, vertical DVRs and multiplicities.'),
  (947,1050,'Rational PL lattice and flag ideals','Rational vector lattice; no identification with all analytic PL.'),
  (1084,1089,'All divisorial points occur on flag-ideal models','Applied to rational divisorial points in the source convention.'),
  (1419,1452,'FS correspondence and ample bundle on a given model','Positive atoms do not require a Dirac equation.'),
  (2193,2250,'Global PSH definition and model criterion','Genuine global cone retained throughout.'),
  (2428,2479,'Global approximation and smooth Laurent-field equivalence','Remark 4.19 used only with smooth connected X, char zero and ample class.'),
  (2494,2552,'Divisorial determination','Only genuine global PSH before a local representation is proved.'),
  (2819,2873,'EP, compactness and birational onto pullback','EP is indispensable for the onto assertion.'),
  (2948,3062,'Continuous envelopes and smooth nef EP','Smooth sufficient theorem is not singular EP.'),
  (3648,3746,'General-variety energy extension and normalization','Monotone extension before EP.'),
  (3770,3893,'Energy and mixed finite-energy finiteness','Actual translation-normalized energy and mixed estimates.'),
  (3916,3944,'Multilinear finite-energy pairing','Differences extend by cone-spanning, not arbitrary currents.'),
  (3978,4129,'Genuine mixed measures, mass and weighted continuity','Weighted integral is pairing with test minus pairing with zero; printed reversed signs not used.'),
  (4531,4602,'Locality and comparison','Winning-locus measure is that of the winning potential.'),
  (4780,4865,'Energy extensions and uniform derivative','Unbounded envelope-energy identity retains EP.'),
  (4919,4966,'Two-sided continuous-direction differentiation','Correct sup-norm error is |t| eta and upper endpoint has plus eta.'),
  (5136,5167,'Maximizing measures converge before attainment','Uses the actual operator, not inverse-measure construction.'),
  (5170,5301,'Coercivity, bounded-J target integration and dual-energy criterion','Correct L1 identity: 2 max(phi_i,phi)-phi_i-phi.'),
  (5405,5481,'Separation, uniqueness and global domination','No application to unglobalized local singular functions.'),
  (5650,5725,'Target completeness','Only the stated source topology and energy target.'),
  (5750,5778,'Linear-growth Diracs','Divisorial Diracs have finite dual energy; does not assert singular solvability.'),
  (6000,6168,'Strong topology, EP-surjectivity equivalence and nodal obstruction','Theorem 12.8 is conditional; Theorem 12.9 is smooth.'),
  (6190,6270,'Sequential approximation','Sequence extracted from already convergent monotone net; no EP inferred.'),
 ],
 '2609.27610v1': [
  (520,639,'Fiber descent and zero-class argument','Printed multiplier -m phi must be m phi when phi<=0; no automatic PSH descent.'),
  (639,759,'Relative local definitions and decreasing PL approximation','Auxiliary convention explicitly corrects missing support constant.'),
  (763,847,'Actual affine FS and growth definitions','Only upper growth used; log|z| contradicts literal lower-growth membership.'),
  (898,1034,'Affine PL claims and regularizable-input extensions','Arbitrary analytic PL globalization is not accepted here.'),
  (1035,1115,'Bounded local representation and determination','Negative floor, reference shift and scalar corrected; global membership remains a gate.'),
  (1117,1195,'Removable extension','Regularizability on the principal open alone does not prove controlled approximation on Y.'),
  (1252,1348,'Local products and local comparison setup','Common genuine global representation and compatibility required.'),
  (1349,1545,'Partition, integration by parts, mass and domination','Global PL extension of local pieces is an extra assertion; model atoms replace the Dirac antecedent conditionally.'),
  (1546,1576,'Smooth affine regularization','Lemma 3.25 antecedent cannot establish its own conclusion.'),
  (1696,1728,'Rossi maximum principle','Arbitrary analytic-neighborhood gluing not covered by algebraic collar formula.'),
  (1730,1793,'Hartogs polynomial coefficients','Already-Runge implication only; use strict polynomial opens.'),
  (1794,1885,'Localization hull lemma','Actual pole orders replace false denominator-power count.'),
  (1964,2044,'Supporting barrier','Direct global FS sequence supplied independently.'),
  (2100,2371,'Finite traces and curve boundary source step','Determinant and radial equality replace selected steps, not the preceding smooth extension.'),
  (2372,2565,'Split pieces, trace integer and Runge lemma','Localize gamma and handle gamma=1 separately; analytic gluing unresolved.'),
  (2566,2692,'Runge and singular-stratum induction','No conclusion without its earlier gates.'),
  (2694,2747,'Actual body geometrically unibranch envelope theorem','Inspected proof invokes weak/global 6.5; not adopted as repaired theorem.'),
 ],
 '1204.6277v2': [
  (7001,7056,'Green formula','Source sign convention controls the corner calculation.'),
  (9511,9729,'Harmonic chart balancing, including proof 7.8.4','Facet positivity reconstructed only with a finite calibrated chart refinement.'),
  (9729,9905,'Generated psh and approachability','Positive current does not itself justify every bounded local product.'),
  (10414,10540,'Continuous BT products, uniform convergence and dpsh','8.7.2 requires locally uniform continuous limits.'),
  (17538,17583,'Integer versus strict PL conventions','Real constants allowed in integer PL; strictness is an independent condition.'),
  (25435,25509,'Formal residual pre-model identification','Used only for an actual represented formal model, retaining nonnormal generic fiber.'),
  (25535,25644,'Residual-nef to psh','17.8.4 literally requires strict integer PL.'),
  (26920,27070,'Mixed current intersection theorem 18.4.7','Model and continuous compatibility only; not singular decreasing bounded convergence.'),
  (27926,28088,'Residual degrees and field extension','18.8.6 has no nontriviality hypothesis on the original field; 18.8.8 cites a strict-only result.'),
 ],
 '1608.08030v3': [
  (79,138,'Standing field scope and Theorem 1.1','Nontrivial complete K, proper scheme, strict PL metric; never apply directly over trivial k.'),
  (185,246,'Notation and strict analytic conventions','For a strict rational-domain representation over k((t)).'),
  (277,350,'Formal extension and PL equivalence proof','Formal existence alone does not give semipositivity.'),
 ],
 '1801.04713v3': [
  (168,330,'Field, skeleton, lisse and positive-Laplacian criterion','Complete algebraically closed nontrivially valued field.'),
  (800,928,'Smooth proper scope and local lisse/current comparison','Compactify a smooth curve before invoking Section 4.'),
  (1096,1612,'Theorem 4.7 and its full proof body','Continuous CLD-psh implies subharmonic; not arbitrary completed-field affine FS regularization.'),
 ],
 'tel-00010990v1': [
  (2897,2974,'Unit norms on a semistable skeleton','Inversion makes the fiber inequality an equality; outgoing slope sign positive.'),
  (3574,3615,'Unit logarithms harmonic and type I/IV behavior','Finitely many units can use one semistable affinoid model.'),
  (3783,3842,'Disk comparison and decreasing stability','3.1.8(ii): decreasing limit subharmonic or identically -infinity on components.'),
  (5322,5355,'Positive lisse Laplacian criterion and proof','Used for relative supports on curves, without ambient extension.'),
 ],
}

out = ROOT / 'source-extracts'
out.mkdir(exist_ok=True)
sources = []
for src in manifest:
    entry = dict(src)
    entry['local_files'] = {}
    for typ, key in [('pdf','pdf_sha256'), ('literal_extract','extract_sha256')]:
        origin = Path(src[typ])
        target = ROOT / 'sources' / origin.name
        if not target.exists():
            shutil.copyfile(origin, target)
        assert sha(target) == src[key], (typ, origin)
        entry['local_files'][typ] = {'path':str(target.relative_to(ROOT)), 'sha256':sha(target), 'bytes':target.stat().st_size}
    lines = (ROOT / entry['local_files']['literal_extract']['path']).read_bytes().decode('utf-8').split('\n')
    entry['lf_line_count'] = len(lines)
    entry['whole_body_audited'] = False
    entry['excerpts'] = []
    for no,(a,b,title,use) in enumerate(SPECS[src['saved_version']],1):
        assert 1 <= a <= b <= len(lines)
        literal = '\n'.join(lines[a-1:b])
        filename = f"{src['saved_version']}-LF{a}-{b}.txt"
        (out / filename).write_text(literal)
        entry['excerpts'].append({'title':title,'start_lf_1based':a,'end_lf_1based_inclusive':b,'literal':literal,'application_and_limit':use,'artifact':f'source-extracts/{filename}','sha256':hashlib.sha256(literal.encode()).hexdigest()})
    sources.append(entry)
payload = {'range_convention':"UTF-8 decode, split('\\n'); inclusive one-based LF indices; excerpts join selected entries with LF, no added trailing LF",'generated_context_is_not_a_premise':True,'sources':sources}
(out / 'source-provenance.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sources':len(sources),'pdf_text_hashes_verified':12,'literal_excerpts':sum(len(x['excerpts']) for x in sources),'input_sha256':sha(ROOT/'input.json')}))
