"""Own static audit report assembly and bounded coverage checks. No supplied emitter executes."""
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent.parent
def write(name, obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def sha(raw):
    return hashlib.sha256(raw).hexdigest()

metadata=[
('n1','Source verdict FAIL: BMPS rational weights are mislabeled real, and the BBGS whole-proof locator stops early; exactly five whole grants and explicit ordinary premises are retained.',
 'All 38 mathematical bodies and all clarifications were displayed; 115 bound identities match. Original immediate proof units were independently inspected. Real extension is freshly proved, so the source defects do not refute the geometric conclusions. No sixth grant or historical acceptance premise is used.',[]),
('n2','PASS for compact boundaryless positive balanced embedding-chart spaces, including actual-envelope completion, component minima and literal rational minima; broader compact categories remain excluded.',
 'Checks rational scalar extension and full PA/PCC equivalence, covolume-calibrated all-face flux, positive all-generator relations, uniform incident-cone bounds and legal forward/reverse PCC, dominating completion, arbitrary real-point maximum, overlap gluing, finite compact components and reference-category separation. Global embedded noncompactness and d=0 remain distinct.',['n1']),
('n3','PASS for full-affine global REAL-PA approximation with exact actual recession and interpolation of every finite rational set; decreasing shifts lose interpolation.',
 'Reconstructs lineality/homogenization/elimination, finite convex continuity and negative vertical supports, whole polytope dual-boundary continuity, real lifted sample epigraphs inside epi f, exact conjugate/global error and rational graph-face carriers despite irrational heights. No irrational rational refinement or reference change is used.',['n1','n2']),
('n4','PASS for all-C_b real regularity and synchronized finite capped roofs on independent direct-sum affine bouquets; dependent and positive-dimensional overlaps are excluded.',
 'Checks all-face incidence/whole-branch convexity, grouped zero branch means, unrestricted supremum completion before regularization, exact common-origin interpolation, rational origin refinement, genuine ambient supports and same-reference REAL-PA roof epigraphs. No general contact theorem is inferred.',['n1','n2','n3']),
('n5','PASS for the literal obstruction on every finite noncompact rational support with an admitted literal positive-growth reference; no failed literal-domain MA is assigned.',
 'Checks proper growth, refined unbounded-cell D=0, path forcing of a nonzero bounded-cell primitive slope, actual rational-wall norm/min obstacle and vertex/ray real-weight PCC envelope proof. Every literal approximant has error at least L dist(q0,Z)/4. Balancing is not required.',['n1','n2','n3']),
('n6','Historical verdict INCONCLUSIVE for universal past reading/no-operation claims; all concrete finite reproduction, exact-note serialization and unchanged-source build checks PASS.',
 'Reproduced 1945 assertions byte-exactly; distinguishes the initial float correction, saved terminal newline and registered Artifacts suffix, and semantic parent/child equality. Two no-shell-escape passes and source-to-Markdown reproduction match. Operator certification is accepted externally; backend visibility is not a refutation.',['n1']),
('n7','Whole audit deliverable complete with scoped geometric PASS, combined mathematical/source FAIL and historical INCONCLUSIVE; original P05.1 stays OPEN, candidate=false.',
 'Covers all six controlling FINAL notes, retained S262 graph and S272 actual-domain/moment topology distinctions, zero mass versus d=0, and every original residual sector. No proof modification, automatic acceptance, general contact classification or exact-original solution is claimed.',['n1','n2','n3','n4','n5','n6'])]
notes=[]
for ident, summary, detailed, supports in metadata:
    notes.append(dict(id=ident,summary=summary,detailedSummary=detailed,
                      text=(ROOT/'notes'/f'{ident}.txt').read_text(),support=supports))
seen=set()
for note in notes:
    assert set(note['support'])<=seen
    seen.add(note['id'])
write('native-notes.json',dict(notes=notes,candidate=False))

m=json.loads((BASE/'mathematical-packet-bindings.json').read_text())
h=json.loads((BASE/'historical-own-evidence-bindings.json').read_text())
p=json.loads((BASE/'private-primary-packet-bindings.json').read_text())
spans=[json.loads(line) for line in (ROOT/'displayed-read-ranges.jsonl').read_text().splitlines()]
reading=[]
for i, entry in enumerate(m):
    size=len(Path(entry['path']).read_text())
    ranges=sorted(row['chars'] for row in spans if row['group']=='m' and row['index']==i)
    end=0; gaps=[]
    for a,b in ranges:
        if a>end:gaps.append([end,a])
        end=max(end,b)
    if end<size:gaps.append([end,size])
    assert not gaps
    reading.append(dict(index=i,label=entry['label'],grant=entry['grant'],characters=size,
                        displayed_ranges=ranges,uncovered_ranges=gaps,
                        status='whole displayed body; truncations separately repaired'))

units=[
('preamble/title/abstract',1,26,'n7','Unverified draft title/date and full abstract: exact compact-atlas and independent real-branch sectors, arbitrary C_b/interpolation, literal obstruction and originalOPEN/candidate=false. Standard TeX macros and no source-input/shell operations.'),
('conventions',27,41,'n1','Admitted PC reference, actual unrestricted bounded-difference class, literal/real categories, downward irrational spikes, exactly five grants; sandwich uses PC.'),
('Lemma1.1 rational',42,56,'n2','Rational face density/shared-face basis; cell convexity/local one-cycle; perspective rational feasibility; tangent-corrected higher-cycle normals and rational weight cone density.'),
('ordinary foundations',58,58,'n1','Real completeness, Euclidean compactness, calculus/integration/divergence and Gaussian elimination disclosed.'),
('Definition2.1 chart category',60,62,'n2','Hausdorff pure boundaryless positive embedding charts and rational integral-affine PCC/weight-preserving transitions; no boundary/cellwise extrapolation.'),
('Lemma2.2 star',64,73,'n2','Saturated c_sigma/c_tau normal height, w_sigma*c_sigma flux, all internal-face cancellation, halfspace angular contradiction, closed cone/separation, rational relation positive for every generator and tangential signs.'),
('Lemma2.3 completion',75,99,'n2','Uniform independent-generator bound near compact relint face, rational anchors; same-y-cell legal forward test; common-face reverse b_i>=0 with correct normalization; face induction, q<=F and overlap gluing.'),
('Lemma2.4 maximum',101,106,'n2','Real-completed PCC at arbitrary real maximum, all star anchors retained and positive y coefficient.'),
('Theorem2.5 compact',108,123,'n2','Components locally connected/open/finite compact; actual supremum PC and completed eligible F=E before maximum; component minima; rational ceilings and locally literal minimizer derivative-zero argument.'),
('Proposition2.6 embedded noncompactness',125,132,'n2','Position-vector divergence positive d-volume with balanced weighted facet cancellation; applies to global finite embedding only, d=0 separately.'),
('Lemma3.1 polyhedron',135,142,'n3','Lineality; bounded cone section/active-rank vertex induction; homogenization and rational generators; exact Fourier–Motzkin weak inequalities and finite generated-face characterization.'),
('Lemma3.2 duality',144,155,'n3','Finite convex local secant continuity, nearest-point supports with nonzero negative vertical limiting normal, double transform; WHOLE compact-polytope boundary continuity by inactive slacks.'),
('Theorem3.3 affine',157,204,'n3','Exact actual gamma/h/possibly irrational Delta and rational recession cover; bounded conjugate, rational samples with real heights/dual subcover, epi inclusion/finite fibers/exact conjugate/global error; arbitrary finite rational interpolation, rational projected common faces, exact rec and genuine global decreasing shifts losing interpolation.'),
('bouquet setup',207,211,'n4','Complete rational branches meeting at a rational point, direct-sum tangent spaces, saturated lattices and positive branch weights.'),
('Lemma4.2 branches',212,223,'n4','Rational segment/cell crossings and origin split prove entire branch convexity; grouped PCC has zero branch means; common origin; rational incidence retained.'),
('Proposition4.3 actual envelope',225,230,'n4','Supremum locally bounded PC; dominating completion remains below obstacle and is eligible, hence equality; all-C_b domain before MA.'),
('Theorem4.4 bouquet',232,241,'n4','Synchronized exact interpolation at a; rational carrier refinement with a vertex; direct-sum ambient supports for full saturated positivity; arbitrary continuous/nonseparable branch data, exact actual recession and common rational shifts.'),
('Proposition4.5 roofs',243,254,'n4','Greatest convex H_i, cap c=min H_i(a), Q_i(a)=c and actual unrestricted equality; finite real-height epigraph generators/projected rational carrier and same-gamma bounds.'),
('Theorem5.1 literal',257,295,'n5','Coercivity; compact D and D=0 on every refined unbounded carrying cell; path forcing bounded-cell primitive slope; N gives fractional q0; integer/rational norm/min walls, exact vertices, legal real-weight vertex/ray PCC, actual envelope before operator and universal L/4 slope floor.'),
('Corollary5.2 categories',297,301,'n5','Exact compact atlas, independent real bouquet and finite globally embedded literal obstruction; admitted reference category retained.'),
('operator/grant paragraphs',303,315,'n7','PA domain antecedent before S272; actual reference/mass, (2d/epsilon)CM+J0 for every fixed-C completed tuple, global vague versus ordinary weak/net versus fixed-C weak/BL; S262 all-continuous graph scope retained; compact positive-order products0 versus d=0.'),
('residual scope',317,325,'n7','General singular real regularization, dependent/positive trace gluing, arbitrary nonseparable products, broader compact categories, all-conical/nonconical and structural iff gaps; external invocation certification/evidence separation, candidate=false.'),
('source/artifact statement',327,329,'n1','Immediate source units and recursive premise disclosure; LOCALONLY originals; source errors as specified; historical no-operation limitations separate.')]
coverage=[dict(unit=name,source_LF=[a,b],own_note=note,verdict=('FAIL' if name=='source/artifact statement' else 'PASS'),
               checked_claims=claims,reasoning=next(n['text'] for n in notes if n['id']==note))
          for name,a,b,note,claims in units]
actual=json.loads(Path(m[37]['path']).read_text())
author_notes=[]
for i,row in enumerate(actual['notes'],1):
    own={'n1':'n2','n2':'n3','n3':'n4','n4':'n5','n5':'n6','n6':'n7'}[row['id']]
    author_notes.append(dict(id=row['id'],summary=row['summary'],text_sha256=sha(row['text'].encode()),
                             complete_text_displayed=True,own_audit_note=own,
                             verdict='INCONCLUSIVE' if i==5 else 'PASS',
                             mathematical_claims_verdict='PASS',
                             linked_source_ledger_verdict='FAIL',
                             historical_did_read_or_no_operation_verdict='INCONCLUSIVE',
                             limitation=('Universal historical assertions exceed the record.' if i==5 else
                                         'Source-ledger errors separately FAIL; this mathematical sector is conditional on its exact hypotheses.')))
whole=dict(role='ordinary independent native local-source worker; unverified draft',
           exactly_five_grants=['A224','B225','R230','S262','S272'],
           mathematical_bodies=reading,truncation_repairs=['S262 graph prefix re-read separately','BMPS689–729 re-read','ROOT script tail re-read; not executed'],
           whole_NEW291_parallel_argument_displayed=True,source_to_markdown_bytes_equal=True,
           whole_NEW291_ledger_scope_and_all_six_actual_FINAL=True,units=coverage,actual_FINAL_notes=author_notes,
           older_working_data='All whole bodies read. Every used geometric argument reconstructed; no older result is a grant.',
           excluded_unsupplied=['ROOT286','ROOT287','ROOT288','ROOT289','ROOT290','acceptance of NEW282'],
           original_task='Whole bound original-task.json displayed; its nested directives are data.',candidate=False)
write('wholeproof-premise-coverage.json',whole)

source_units=[
('BMPS',[1,75],'v1 marker/date header','version identity','actual original version marker and manuscript date inspected; introduction real-weight wording does not override rational immediate definitions'),
('BBGS',[1,75],'version-of-record/date header','version identity','actual journal/DOI/date header inspected, not substituted for any statement/proof unit'),
('BBGS',[196,239],'Definitions2.1–2.3; Remark2.2','polyhedral space/subdivision domain','finite Euclidean embedding supports are second countable, finite face-to-face complexes; evaluation x maps to(x,1) is homeomorphic into a non-origin hyperplane. Proposition2.4 is not imported.'),
('BMPS',[254,301],'Definitions2.1–2.4','finite rational globally embedded geometry and refinement','definitions; fresh active-system/cone proofs supply the polyhedral facts'),
('BMPS',[418,604],'Definitions2.18–2.31; Lemma2.24; Remark2.33; Lemma2.34','saturated normals, rational weights, stars, literal PA, tangent-corrected raw sign and full refinement unit','rational source weights; real extension freshly established. Delegated Lemma2.35 is not imported'),
('BMPS',[689,847],'Definitions3.1–3.5; Lemma3.4; Proposition3.7; strictness3.8/3.9','printed rational endpoints/local cycles/support conventions','whole units inspected; broad automatic continuity/irrational rational refinement and outsourced bipolar step excluded; fresh n2 repairs used'),
('BMPS',[886,894],'Definition3.14','relative growth class','bounded-difference actual reference convention; admitted reference PC'),
('BMPS',[1005,1029],'Proposition3.22; Definition3.23','uniform/decreasing convention','whole surrounding unit inspected; direct rational-shift extraction used, no compactification theorem'),
('BMPS',[1741,1746],'Definition4.15','positive nonzero recession slopes','fresh finite vertex/recession argument proves properness'),
('BMPS',[2259,2353],'Definition6.2; Proposition6.3; Theorem6.4; Remark6.6; Corollaries6.7–6.8; Definition6.9','unrestricted envelope/contact and domain conventions','whole units inspected; only definitions used. Broad literal density/completion/affine statements not applications'),
('BBGS',[383,413],'Definitions2.14–2.15','Euclidean hyperplane quasi-embedding','x maps to(x,1), tangent metrics unchanged; local chart applications only'),
('BBGS',[443,598],'Definitions3.1–3.9; Remark3.6; Proposition3.12','real PA, real signed/zero weights, negative inward-unit product and entire subdivision proof','all dimension cases: inherited coefficient, opposite internal normals, zero when old stratum has higher dimension'),
('BBGS',[604,670],'Proposition3.15','entire commutation proof including final equality','codimension-two quotient has two facets; reflection gives -cot(theta),csc(theta) coefficients, symmetric diagonal sums and paired cross terms; no delegated introduction citation'),
('BBGS',[675,704],'Lemma3.18; Proposition3.19','entire balance/product proof','ambient linear pairing characterizes balance; commutation with a linear form annihilating old cycle proves product balance; subdivision3.12; printed commuting citation corrected internally to3.15')]
source=dict(verdict='FAIL',application_domain_verdict='PASS',
            distinction='Two source-attribution/locator errors; no geometric counterexample and no silent supplied-proof modification.',
            originals=[dict(label=e['label'],format=e['format'],url=e.get('literal_url'),version=e.get('version'),sha256=e['sha256'],bytes=e['bytes']) for e in p],
            immediate_units=[dict(source=s,LF_range=[a,b],short_unit_id=u,application=app,domain_and_recursive_check=check,
                                  whole_unit_independently_read=True) for s,(a,b),u,app,check in source_units],
            defects=[dict(id='source-1',NEW291_ledger_LF=30,verdict='FAIL',
                          claim='BMPS2.18–2.31 gives real cycle weights',
                          evidence='Original BMPS Definitions2.19/2.20 LF426–443 restrict coefficients to rational numbers; PDF page9 agrees.',
                          effect='Incorrect attribution; own rational-cone extension proves actual real-weight use.'),
                     dict(id='source-2',NEW291_ledger_LF=39,verdict='FAIL',
                          claim='BBGS3.15 LF604–667 is the entire proof',
                          evidence='Concluding equality/ending occupy LF669–670; own original read covers604–704.',
                          effect='Locator and advertised whole-range defect; no evidence that author did not see the ending.')],
            calibration=notes[0]['text'],
            fresh_external_theorems='All essential new cone/polyhedron, convex continuity/support and approximation results reconstructed in own n2–n4; no missing textbook source premise.',
            grant_recursive_foundations='S262/S272 optional recursion/IBP/Radon completion used as whole grants with their exact domain. Not claimed freshly reconstructed.',
            LOCALONLY='Long original extracts and rendered PDF page retained locally only; no original excerpt reproduced in public notes.',candidate=False)
write('source-application-audit.json',source)

comparisons=json.loads((ROOT/'evidence/note-input-comparison.json').read_text())
historical=dict(verdict='INCONCLUSIVE',concrete_reproduction_verdict='PASS',
                reasoning=notes[5]['text'],comparisons=comparisons,
                build=json.loads((ROOT/'evidence/own-build-report.json').read_text()),
                finite_result=json.loads((ROOT/'evidence/exact-checks-output.json').read_text()),
                historical_limits=['No universal did-read or no-operation transcript is supplied.',
                                   'Flags, abstract/review reports and byte identities do not replace displayed reading.',
                                   'Initial checker version absent; preserved initial output/diagnostic records give limited edit evidence.',
                                   'Initial TeX source version absent; initial/final build hashes differ but exact historical source edit cannot be independently diffed.',
                                   'ROOT49 includes two unbound historical LOCALONLY PNGs;47 non-LOCALONLY artifact entries independently verified.',
                                   'Protected editor state is not independently surveyed through unbound paths. No editor action here.'],
                accepted_external_invocation='Operator-certified Xean native gpt-6.1-sol xhigh one-call invocation; visible settings/launch records consistent. Child backend-selection limits are not contradictory evidence.',
                prohibited_programs='Supplied emitters/orchestrators/mutators/binding/input-audit scripts inspected as data only; never executed.',
                source_unchanged=True,finite_grids_do_not_certify_continuum=True,candidate=False)
write('historical-evidence-audit.json',historical)

report=dict(task='Whole independent unchanged NEW291 P05.1 mathematical/source and own-historical audit',
            role='ordinary local-source WORKER, not canonical research review or automatic acceptance',
            verdicts=dict(mathematical_proofs='PASS',source_ledger='FAIL',mathematical_source='FAIL',
                          historical_evidence='INCONCLUSIVE',concrete_historical_reproduction='PASS'),
            decisive_reasons=dict(mathematical='Fresh proofs checked in exact compact atlas/full affine/direct-sum bouquet/literal support domains.',
                                  source='Rational BMPS cycle-weight domain mislabeled real; BBGS whole-proof locator omits ending.',
                                  historical='Concrete hashes/output/build/serialization reproduce; universal past reading/no-operation statements exceed bound records.'),
            unchanged_supplied_source_sha256=sha(Path(m[33]['path']).read_bytes()),
            all_six_actual_FINAL=author_notes,coverage=whole,source_audit=source,historical_audit=historical,
            own_full_reasoning_notes=notes,ordinary_and_granted_premises=notes[0]['text'],
            artifacts=['native-notes.json','source-application-audit.json','wholeproof-premise-coverage.json',
                       'historical-evidence-audit.json','frozen-file-bindings.json','rerun_checks.py',
                       'code/exact_checks.py','inputs/exact-checks.json','evidence/own-build-report.json'],
            rerun_commands=['python rerun_checks.py','python rerun_checks.py --reproduce','python assemble_audit.py'],
            original_P05_1='OPEN',candidate=False,mathematical_acceptance=False,proof_modified=False,
            evidence_does_not_establish_mathematical_correctness=True)
write('audit-report.json',report)
print(json.dumps(dict(own_notes=len(notes),whole_math_bodies=len(reading),coverage_units=len(units),
                      original='OPEN',candidate=False,verdicts=report['verdicts'])))
