"""Own report finalization; reads frozen metadata, writes only own local artifacts.

Does not execute supplied programs, the finite checker, TeX, or Pandoc.
"""
import hashlib
import json
from pathlib import Path

history = json.loads(Path('frozen-historical-own-evidence-bindings.json').read_text())
comparison = json.loads(Path('whole-historical-comparison.json').read_text())
direct = {13,14,15,18,19,21,22,23,24,25,30,38,39,40,41,42,46,47,
          62,63,66,68,69,70,82,83,85,87,88,89,90,91,116,117,118,119,120,121}
math_alias = {r['history']:r['math'] for r in comparison['math_aliases']}
primary = {r['history']:r for r in comparison['primary_extracts']}
variants = {}
for kind in ['engine_differences','stdout_differences']:
    for row in comparison[kind]:
        for index in row['history_aliases']:
            variants[index] = (kind,row['canonical'])
coverage = []
for group in comparison['byte_aliases']:
    if group[0] in comparison['empty_entries']:
        method = 'verified empty byte body'
        anchor = None
    elif any(i in direct for i in group):
        anchor = next(i for i in group if i in direct)
        method = 'whole direct canonical display and assessment; exact-byte aliases'
    elif any(i in math_alias for i in group):
        anchor = next(i for i in group if i in math_alias)
        method = 'exact-byte identity with whole-displayed mathematical body'
    elif group[0] in primary:
        anchor = group[0]
        method = 'whole numbered body exact to fully read literal-LF primary unit; header hash verified'
    elif group[0] in variants:
        anchor = variants[group[0]][1]
        method = 'whole-read canonical plus ALL lossless changed-line blocks displayed and assessed'
    elif group[0] in [16,99]:
        anchor = 'own fresh 18-page PDF'
        method = 'bound hash verified; entire PDF extracted text exact to own PDF; no pixel identity claim'
    else:
        raise AssertionError(('unaccounted unique history body',group))
    for index in group:
        row = dict(index=index,path=history[index]['path'],bytes=history[index]['bytes'],
                   sha256=history[index]['sha256'],method=method,anchor=anchor,
                   direct_display_this_entry=index in direct,
                   entire_bound_content_accounted=True,past_comprehension_verified=False)
        if index in math_alias:
            row['mathematical_body_index'] = math_alias[index]
        if index in primary:
            row['primary_unit'] = primary[index]
        coverage.append(row)
coverage.sort(key=lambda row:row['index'])
assert [row['index'] for row in coverage] == list(range(122))
assert all(row['entire_numbered_body_exact'] for row in comparison['primary_extracts'])
assert all(row['bound_matches'] for row in comparison['binding_inputs'])
assert all(row['exact_match'] for row in comparison['binding_artifacts'])
assert comparison['pdf_text_equal']
Path('historical-body-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')

payload = json.loads(Path('native-notes.json').read_text())
n1,n2,n3,n4 = payload['notes']
def replace(note, old, new):
    assert old in note['text'], old
    note['text'] = note['text'].replace(old,new)

replace(n1,
    'This is distinct from the requested whole mathematical/source verdict, which is INCONCLUSIVE for the coverage gaps in n4.',
    'All33 bound mathematical bodies were displayed whole and assessed. Essential source applications PASS; exhaustive source-label accuracy FAILS narrowly as n2 explains. Universal historical assertions remain INCONCLUSIVE as n3 explains.')
replace(n1,
    'Some grant bodies/companions remain unread in this invocation, as n4 discloses.',
    'All six whole grants and every clarification/companion argument/ledger/material-change body were read. Their broad granted recursive/Radon foundations remain explicit external premises rather than new independent validations.')
n1['detailedSummary'] = (
    'All33 mathematical bodies, unchanged493-LF source and entire parallel argument, working293/294 with embedded289, and all7 actual FINAL notes were assessed. The continuous-endpoint theorem is independently reconstructed from explicit ordinary premises; unrestricted-envelope continuity uses R230. ONE ambient joint minimizer attains all page fiber minima, including boundary; whole trace, rational spatial PA geometry, actual recession and global strict decrease follow without normal independence. Original classifications remain OPEN.')

n2['summary'] = 'Essential source/raw applications PASS with exactly six whole grants. Exhaustive source-label accuracy FAILS narrowly: unused Proposition4.16 is called a Definition; no mathematical counterexample.'
n2['detailedSummary'] = (
    'All33 mathematical bodies and all clarifications were assessed. Thirteen whole immediate original ranges use literal LF, including complete BBGS3.15 through670. Common supports prove all-cycle positivity; covolume conversion holds recursively for real/signed/zero weights. Crossing realization/roof retain S272/S282 antecedents, effective residual and SAME flat germ. The unused BMPS unit-label error is a source-metadata failure; essential applications and scoped regularization pass.')
replace(n2,
    "Source applications reconstructed here pass within n1's ordinary premises and explicit grant dependencies; requested whole source verdict remains INCONCLUSIVE.",
    "Essential source applications PASS within n1's ordinary premises and exactly-six-grant dependencies. Exhaustive mathematical/source claim accuracy FAILS narrowly at the unused source label below; this is not a failed mathematical theorem.")
replace(n2,
    'In3.15 each codimension-two wedge has two rays; bisector reflection gives the same reversed coefficients. Diagonal double-sum terms are symmetric and swapping facets pairs cross terms.',
    "In3.15 fix rho of codimension2 and an incident sigma; its quotient wedge has the two facets tau,tau'. Write u=v_tau/rho,u'=v_tau'/rho. Bisector reflection gives v_sigma/tau=a u+b u' and v_sigma/tau'=a u'+b u. The double negative product expands to Σ_sigma c_sigma[a Σ_tau f_tau(u)g_tau(u)+b Σ_tau f_tau(u)g_tau'(u')]. The first term is symmetric; swap tau,tau' in the second and use continuity of facet restrictions and the second expansion to obtain the reversed product. Thus the whole paired double-sum argument works with arbitrary real/signed/zero weights, without simpliciality.")
replace(n2,
    'R230/S272/S282 whole TeX were read, but A224/B225/S262 whole bodies and eleven specified grant/companion bodies remain unassessed; therefore a whole-source PASS is not claimed.',
    'ALL33 mathematical bodies were read whole, including every grant TeX and companion argument/ledger/material changes. A224 retains its PA U34/positive-active convention; B225 retains continuity/chart-internal endpoints and noncompact rational chart-compatibility; S262 retains the corrected PC floor, exact graphsector, coupled replacement, half-jump/count, Stieltjes and topology restrictions. S272 separates rational-component cutoff/completion from SAME-flat-germ insertion into EVERY positive reference-coefficient summand. S282 retains whole affine-contact/tree/localized-domain/arrangement claims with regularity AND contact together. These remain precise whole grants, not fresh proofs of every recursive general measure foundation. Some older grant ledger ranges stop BBGS3.15 at667; its actual ending is670, included in NEW298 and my604–704 whole read.')

n3['summary'] = 'All122 bound historical contents assessed by explicit canonical/alias/difference/PDF-text methods. Finite/checker/conversion/build PASS; actual7 and saved7 prose DIFFER. Universal past chronology INCONCLUSIVE.'
n3['detailedSummary'] = (
    'All159 frozen entries match. All122 history entries are accounted for:68 unique byte bodies,26 empty, whole canonical reads, all changed log lines, exact original-unit extracts, and18-page PDF-text equality. All seven saved and actual versions are preserved; each prose field differs, IDs/supports agree, registration only adds Artifacts suffix. One safe checker run reproduces8vertices/35triples,−3/64,26961tuples,33boundary trace points,44orders/6matrices. One Pandoc conversion and three fresh TeX passes0/0/0 finish clean18p. Complete past event/read/no-operation evidence and original-task body are unavailable; historical verdict remains INCONCLUSIVE.')
replace(n3,
    'Historical verdict: INCONCLUSIVE for universal past read/no-operation assertions and complete bound-history audit. Particular comparisons and fresh execution below PASS. Frozen artifacts are not a complete past event transcript, and not every122 historical body was displayed.',
    'Historical verdict: INCONCLUSIVE for universal past read/no-operation assertions. Particular comparisons and fresh execution below PASS. All122 bound contents were assessed by whole canonical reads plus lossless aliases/changed-line blocks, original-unit comparisons and PDF-text equality. This does not claim separate raw display of every duplicate or PDF pixels. Frozen artifacts are not a complete past event transcript.')
needle = 'Full manifests were frozen locally.'
replace(n3,needle,needle + (
    ' There are68 unique historical byte bodies and26 empty entries. Nine entries equal whole-read mathematical bodies;13 numbered source extracts exactly match fully read original LF units and header hashes. All unique programs/notes/bindings/configuration bodies were read whole as DATA. The whole clean engine/stdout canonicals plus ALL changed-line blocks cover six engine variants and two stdout variants; no warning-only or hash-only substitute is claimed. Author binding30inputs/82artifacts were checked against bound inputs/artifacts; earlier audit1 has67artifacts, later audit2 has82, belonging to distinct states. Every entry and method is recorded in historical-body-coverage.json and full comparisons in whole-historical-comparison.json.'))
needle = 'Complete transient native transcript evidence is not supplied.'
replace(n3,needle,needle + (
    ' Whole inspected interval-reader code prints then records requested intervals, and historical audit code merges them. Successful interval coverage cannot prove that earlier output was untruncated or its repairs actually read. The inspected ROOT helper contains an outside-P16 hash-read expression and copy/publish actions; code is not an execution trace. I did not execute it or access that outside path. Hence it cannot establish universal restricted-access/no-operation claims.'))
needle = 'No repeat build was run and no PDF byte-identity claim is made, since date metadata is fresh.'
replace(n3,needle,needle + (
    ' The inspected own finish_history.py separately ran ONCE, with fixed-argv pdftotext -layout on own and two bound historical PDFs. All3returned0/emptydiagnostics,66,124textbytes/18formfeeds and identical text SHA256c40e8cf416d9d8b5c240e9b1510355453739810fa130e85a7f9c3ca1772f6acd. This is full extracted-text equality, not pixel/layout or PDF-byte identity; it reran neither checker nor TeX.'))
replace(n3,
    'An initial aggregate manifest output and part of a ledger table truncated; manifest identification was repaired by whole-entry inventory/frozen snapshots, and ledger tail repaired by standalone character reads[16000,18664),[18664,18912). Requested display logs are not comprehension certificates.',
    'Initial aggregate manifest/NEW298 ledger displays truncated and were repaired with whole inventory/snapshots and standalone ledger tails[16000,18664),[18664,18912). A later aggregate S262 material-change/S272 ledger display truncated; [4500,4963) of the former and ENTIRE[0,12399) of the latter repaired it. An aggregate history-difference output also truncated; compact lossless blocks and a separate whole first-engine block display repaired every variant. An own metadata inspection returned KeyError for an incorrect key; corrected read displayed existing results without re-execution. Requested display logs are not comprehension certificates.')
n3['text'] += (
    '\n\nIndependent whole293 diagnostic: in R3 with coordinates(t,x,y), the pages have common t-axis and saturated normal vectors v1=(0,1,0),v2=(0,0,1),v3=(0,−1,−1), so v1+v2+v3=0. Huber(z)=z²/2 for |z|≤1 and |z|−1/2 otherwise has continuous nondecreasing derivative. f_i(t,s)=Huber(t)+Huber(s) is convex with −1≤f_i−(|t|+|s|)≤0. At every real trace point Huber\'(t)dt supports ALL pages, so the original endpoint is PC and regularizable by n1. For lifts(0,0,0),(1,0,1/2),(1/2,1/4,5/32) plus exact epi(|t|+|s|), the plane t/2−3s/8 agrees on the sample triangle and is a lower support. On the trace, a third-sample coefficient lambda contributes5lambda/32 in height and at leastlambda/4 normal recession cost; replacing it with equal first-two coefficients costslambda/4, improving by5lambda/32. Thus the ENTIRE trace is−t for t≤0,t/2 for0≤t≤1,t−1/2 for t≥1. At z=(1/2,0,0), the three endpoints z+v_i/8 lie in genuine incident rational triangles with barycentrics(1/4,1/4,1/2), average to z and each cost13/64 versus16/64 at the center. Hence the legal PCC cost is−3/64. Any common support would force p(v_i)≤−3/8, contradicting their actual zero sum. This failed gluing has shared trace but is NOT PC and gets no MA; it is not a nonregularizability example. The8-vertex/35-triple certificate is checked separately from this continuum reasoning.')
n3['support'] = ['n1']

n4['summary'] = 'Whole33 mathematical bodies and all122 bound historical contents assessed; scoped mathematics/essential applications PASS, unused source-label FAIL, universal history INCONCLUSIVE. Original P05.1/P05.2 OPEN; candidate=false.'
n4['detailedSummary'] = (
    'Delivered own reconstruction, all contiguous/unnumbered proof coverage, whole-six-grant/all-clarification scope, source-application and seven-actual-FINAL assessment, full distinct saved history, frozen bindings and safe finite/build records. All bound contents are accounted for by explicit methods. Strict all-claim source accuracy fails at an unused label; no scoped mathematical counterexample was found. Universal past chronology and the unavailable unbound original-task body remain evidence limitations. No canonical acceptance, original classification or complete original-task solution is claimed.')
n4['text'] = '''Separate verdicts: scoped mathematical proof PASS; essential source applications PASS; the combined demand that EVERY mathematical/source claim be accurate FAILS narrowly because an explicitly unused BMPS Proposition4.16 is labelled Definition4.16. Historical universal past read/no-operation verdict INCONCLUSIVE. These are compatible: the metadata error does not refute the theorem, and complete bound-content assessment does not supply a missing past event transcript. Original P05.1/P05.2 remain OPEN; candidate=false. This is one ordinary local-source worker audit, not canonical review, automatic acceptance or original closure.

The exact assessed domain is finite distinct COMPLETE rational equal-d affine pages, ALL pairwise intersections the ONE rational affine H with0≤dimH<d, dependent normal quotients allowed, arbitrary positive REAL weights, actual REAL continuous PC PA reference on genuine finite rational spatial geometry with strictly positive recession. All continuous bounded-relative PC endpoints and ALL actual unrestricted C_b obstacles, including coupled/nonPA/nonseparable data, are covered. Approximation is genuine finite rational-spatial REAL PA, globally strictly decreasing and uniformly convergent, preserving SAME actual recession before any MA assignment. H=0 is separate. Multiple overlaps/nonincident extra pages/general singular/abstract/literal categories/full original classification and general nonPA contact classification are excluded.

All33 mathematical packet bodies(index0–32) were displayed whole and assessed. Exactly six whole caller grants A224/B225/R230/S262/S272/S282 with EVERY clarification are retained, including S282's whole paper/all6clarifications. Working293/294, ENTIRE embedded289 and NEW298 are DATA, not extra grants. All seven actual native221 FINAL notes and all seven saved versions were read separately and preserved fully; no substitution or semantic-identity claim. Whole grant recursive/Radon foundations remain declared dependencies rather than newly validated general foundations. R230 gives actual unrestricted envelope continuity first, n1's new density supplies genuine domain second, S272 gives MA third.

Main TeX was read in literal LF1–100,101–195,196–280,281–380,381–493. Parallel Markdown was read in characters[0,14000),[14000,28000),[28000,42000),[42000,56000),[56000,65095). Whole294 including embedded289 was read[0,14000),[14000,28000),[28000,36553); whole293 separately. Final earlier gaps were repaired by whole A224/B225/S262 TeX, S262/S272/S282 companion arguments and every ledger/material-change body. S262 material-change truncation was repaired at[4500,4963); S272 ledger ENTIRE[0,12399) was separately read. Whole-proof-coverage.md covers every equation(CS,RC,PH,JF,SM,LF,RAW), inline and untagged display, surrounding unnumbered claim, operator/domain/scope/evidence assertion, preamble and bibliography. J1–J7 and embeddedT3/K1–K6 are accounted for: old independent groupwise Jensen is confined to direct quotients and replaced by the ONE simultaneous ambient-support construction on dependent pages.

The contiguous own map is LF1–34 role/preamble/abstract;35–57 domain/PCC/grants;58–85 rational perspective density and all hull/cone/elimination premises;86–114 full supports/Lipschitz/subgradients;115–142 whole-boundary continuity/extended biconjugacy;143–182 pageconvexity/common supports;183–204 actual gamma/Delta/exact recessioncones;205–231 primal samples/rational projected faces/scalar kernel;232–275 joint dual/boundary fibers/simultaneous minima;276–316 lowering/all real trace supports;317–339 ENTIRE PAtrace epigraph/rational common carrier;340–358 H=0/strict shifts/all-C_b endpoint-before-MA;359–398 whole293 diagnostic;399–429 balance/residual/raw signs/recursive chain/IBP/mass;430–437 S272 moment/topologies;438–457 flat-jet determinant/actual-reference roof;458–468 whole scope/source/finite-evidence claims;469–482 history/config/repro/role;483–493 bibliography. The mathematical reasoning is in n1–n3 and independent-reconstruction.md; the map is coverage, not an execution-based proof.

All13 whole immediate BMPS/BBGS original ranges in n2 were read, using literal LF rather than formfeed-counting splitlines; BBGS3.15 ends670, not667. All122 historical entries are accounted for by whole canonical reads plus exact-byte aliases, ALL changed-line blocks, entire exact primary-extract matches or entire PDF-text comparison. There are68 unique byte bodies/26emptyentries,9mathaliases/13primaryextracts,6enginevariants/2stdoutvariants. No independent raw redisplay of every duplicate or PDF pixel identity is claimed. historical-body-coverage.json gives every entry's method; whole-historical-comparison.json retains complete comparisons. All159 binding entries match recorded bytes/hashes. These identification/coverage results cannot establish earlier comprehension or a universal negative past-operation claim. The original-task.json body is NOT bound; its freeze hash is not contents. Bound frozen task/input were read as DATA and missing contents were not inferred.

All7 controlling actual FINAL dispositions were assessed: author n1 grants/scope remains conditional ordinary author data; n2 PCcriterion/primalfoundations PASS; n3 ONE joint fibers/lowering PASS; n4 whole-trace geometry/strict approximation PASS with R230-before-density-before-S272; n5 diagnostic PASS but failedgluing unmeasured; n6 raw/calibration/contact applications PASS under exact S272/S282 premises; n7 particular artifacts/configuration/repro PASS, universal past read/no-operation INCONCLUSIVE. EVERY actual-vs-saved prose field differs while IDs/supports agree, both candidatefalse; registration adds only its bound Artifacts suffix. ROOT's repaired field-summary is not a whole saved-draft read certificate. Author initial failures/warnings, later extra clean author rerun, historical ROOT reproduction, and my ONE fresh checker/three-pass build remain distinct. Native210/native215 historicalINCONCLUSIVE and author213 saved/FINAL discrepancy remain supplied DATA; no excluded native was accessed.

No unbound/privateACTIVE/othernative/native218219220222/compact291/isolated292/independent295/newS291S292/ROOT296297, outside proof repair or hot feedback supplied a premise. Bound historical helpers were read only, never executed. No network/web/agent/nestedprovider/heavycompute/protected editor action or supplied-source/runtime/auth/account/HOME/CODEX_HOME/proxy/CA modification occurred in my tool sequence. Only fresh own artifacts were written. No supervised heavy facility was exposed or needed. The inspected ROOT helper's outside-P16 expression was not accessed or executed. Launch/settings record native gpt-6.1-sol/xhigh/onecall; absence of independent backend attestation does not contradict the recorded invocation.

Deliverables: audit-report.md; independent-reconstruction.md; source-application-audit.md; whole-proof-coverage.md/body-coverage.json; historical-audit.md/historical-body-coverage.json; frozen-verification.json and three frozen manifest snapshots; full actual/saved/registered note copies; note-field-comparison.json/own-evidence-comparison.json/whole-historical-comparison.json; native-notes.json; unchanged local source/PDF/Markdown; own finite checker/input/output and all environment/Pandoc/TeX logs; own-reproduction.json; artifact-bindings.json. Long original text is LOCALONLY. Programs and exact argv are retained. Read-only comparison reruns: python audit_io.py inventory; python record_evidence.py. For fresh checker/build reproduction copy own reproduce.py,finite_check.py,exact-input.json,P05.1-paper.tex into a fresh directory and run python reproduce.py there, preserving initial logs. Own finish_history.py makes read-only bound comparisons and PDF-text extraction; preserve initial outputs on rerun. The notes are unverified audit drafts. No complete original classification or original-task solution is claimed.'''
n4['support'] = ['n1','n2','n3']
payload['candidate'] = False
assert all(n['id']==f'n{i+1}' for i,n in enumerate(payload['notes']))
for i,note in enumerate(payload['notes']):
    assert all(s in [n['id'] for n in payload['notes'][:i]] for s in note['support'])
Path('native-notes.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')

bindings=[]
for path in sorted(Path('.').iterdir()):
    if path.is_file() and path.name != 'artifact-bindings.json':
        data=path.read_bytes()
        bindings.append(dict(filename=path.name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
Path('artifact-bindings.json').write_text(json.dumps(bindings,indent=2)+'\n')
print(json.dumps(dict(mathematical_bodies=33,historical_entries=len(coverage),
                     unique_historical_bodies=comparison['unique_byte_bodies'],
                     own_notes=len(payload['notes']),own_bound_artifacts=len(bindings),candidate=False)))
