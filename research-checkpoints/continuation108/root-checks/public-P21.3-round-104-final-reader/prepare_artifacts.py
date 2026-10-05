#!/usr/bin/env python3
"""Prepare a reproducible proof packet from frozen input and inspected sources."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent

def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source = ROOT / 'P21.3-new-proofs.md'
main = source.read_text()
main = main.replace('[BGJKK], arXiv:2102.07392, the public PDF examined in this run,',
                    '[BGJKK], arXiv:2102.07392v1, 15 February 2021, the public PDF examined in this run,')
main = main.replace('1578--1649 and 2595--2645', '1578--1654 and 2595--2645')
main = main.replace("This PDF's exact version header is recorded in `literature-bindings.json`; an unversioned retrieval is not represented as a version-frozen byte download.",
                    "The inspected PDF header is v1, 15 February 2021. The catalogue instead cites the 2025 published article; this run checked the identified preprint units, not every unit of the published revision. Version-specific passage bindings are also in `literature-bindings.json`; web-rendered text is not represented as frozen PDF bytes.")
main = main.replace('public arXiv PDF, version header and retrieval bindings in `literature-bindings.json`.',
                    'arXiv:2102.07392v1, 15 February 2021; version header and retrieval bindings in `literature-bindings.json`.')
source.write_text(main)

evidence = (ROOT / 'supplied-primary-evidence.md').read_text()
(ROOT / 'P21.3-primary-evidence.md').write_text(evidence)
(ROOT / 'P21.3-argument.md').write_text(main + '\n\n# Appendix: literal supplied primary statement and proof units\n\n' + evidence)

bindings = []
def web_unit(name, url, version, log, lo, hi, scope):
    result = json.loads((ROOT / log).read_text())
    rows = {}
    fetch_url = url.split('#', 1)[0]
    if fetch_url == 'https://arxiv.org/pdf/2102.07392v1':
        fetch_url = 'https://arxiv.org/pdf/2102.07392'
    for block in result.get('content', []):
        if block.get('type') != 'text':
            continue
        # One returned text block can concatenate several documents whose
        # rendered line numbers overlap. Select by the document header first.
        for section in re.split(r'\n-{20,}\n', block['text']):
            if '(' + fetch_url + ')' not in section.splitlines()[0]:
                continue
            for row in section.splitlines():
                m = re.match(r'L(\d+)(?:@P[\d-]+)?: (.*)', row)
                if m:
                    number = int(m.group(1))
                    if lo <= number <= hi:
                        if number in rows:
                            assert rows[number] == row, (name, number)
                        rows[number] = row
    assert len(rows) == hi-lo+1, (name, len(rows), hi-lo+1)
    path = ROOT / 'sources' / (name + '-web-unit.txt')
    path.write_text('\n'.join(rows[i] for i in range(lo,hi+1)) + '\n')
    bindings.append({'id':name,'primary_url':url,'version':version,
                     'retrieved_http_url':fetch_url,
                     'unit_file':str(path.relative_to(ROOT)),
                     'web_rendered_line_interval':[lo,hi],
                     'unit_sha256':digest(path),'retrieved_output':log,
                     'scope':scope,'pdf_bytes_downloaded':False})

web_unit('gr-generated-comparison', 'https://arxiv.org/html/2506.13548v2#S1.SS2',
         'arXiv:2506.13548v2, 17 September 2025', 'logs/search-03.json', 94, 98,
         'Literature scope check only: one direction to classically psh; no converse used.')
web_unit('gr-pl-recognition', 'https://arxiv.org/html/2506.13548v2#S4',
         'arXiv:2506.13548v2, 17 September 2025', 'logs/search-05.json', 677, 684,
         'Literal rendered statement and proof; nontrivial valuation, already real-PL. Not a new proof premise.')
web_unit('bgjkk-regularization', 'https://arxiv.org/pdf/2102.07392v1#page=19',
         'arXiv:2102.07392v1, 15 February 2021; header observed', 'logs/search-06.json', 1483, 1519,
         'Literal rendered Theorem 3.3.4 statement/proof, on tropical toric N_Sigma; diagnostic only.')
web_unit('bgjkk-current-product', 'https://arxiv.org/pdf/2102.07392v1#page=20',
         'arXiv:2102.07392v1, 15 February 2021; header observed', 'logs/search-12.json', 1578, 1654,
         'Literal rendered Theorem 4.1.2 statement/proof; smooth fan, Lagerberg currents, not arbitrary analytic currents.')
web_unit('bgjkk-metric-comparison', 'https://arxiv.org/pdf/2102.07392v1#page=33',
         'arXiv:2102.07392v1, 15 February 2021; header observed', 'logs/search-04.json', 2595, 2645,
         'Literal rendered Theorem 6.1.1 statement/proof; toric metrics and constructed Chern products.')
web_unit('jell-smooth-kernel', 'https://arxiv.org/pdf/1409.0676v3#page=19',
         'arXiv:1409.0676v3, 29 July 2016', 'logs/search-12.json', 1673, 1720,
         'Literal rendered Corollary 4.6 statement/proof; smooth first differential kernel. Not a new proof premise.')
write_json('literature-bindings.json',bindings)

appendix = '\n\n# Appendix: inspected literature scope-check units\n\n'
appendix += ('These are literal source extracts for diagnostic scope checks, not '
             'additional analytic-current approximation premises. Web line labels '
             'are retained and are distinguished from frozen PDF bytes.\n\n')
appendix += ('## Euclidean convolution, CLD v2 section 1.6.6\n\n'
             '<https://arxiv.org/pdf/1204.6277v2#page=38>, 25 July 2025; '
             'one-based inclusive LF 1698--1762 in the frozen supplied source.\n\n'
             '```text\n' + (ROOT/'sources/cld-euclidean-convolution.txt').read_text() + '```\n\n')
for unit in bindings:
    appendix += ('## ' + unit['id'] + '\n\n' + unit['version'] + '\n\n<' +
                 unit['primary_url'] + '>; actual retrieved URL <' + unit['retrieved_http_url'] +
                 '>. Web-rendered lines ' + str(unit['web_rendered_line_interval']) +
                 '; unit SHA256 `' + unit['unit_sha256'] + '`.\n\n```text\n' +
                 (ROOT/unit['unit_file']).read_text() + '```\n\n')
(ROOT/'P21.3-argument.md').write_text(main +
    '\n\n# Appendix: literal supplied primary statement and proof units\n\n' + evidence + appendix)

write_json('premises.json', [
    {'id':'E0','exact_result':'Ordinary opens, canonical restriction, local differential separation, compact smooth cutoffs and scalar uniform density as stated in the paper.',
     'source':'CLD arXiv:1204.6277v2, 25 July 2025','primary_url':'https://arxiv.org/pdf/1204.6277v2#page=423',
     'units':['ordinary-domain','analytic-calculus','cutoffs-density'],'applicability':'Good separated pure analytic ordinary opens; either valuation; compact support, no global paracompactness.'},
    {'id':'E1','exact_result':'Ordinary currents are continuous duals of all complementary compact smooth tests, weak topology is evaluation, symmetry projects diagonal tests, restriction and current sheaf as stated in the paper.',
     'source':'CLD v2, 7.1.1--7','primary_url':'https://arxiv.org/pdf/1204.6277v2#page=155',
     'units':['current-topology','current-sheaf'],'applicability':'Actual ordinary test spaces on the fixed N; no single-chart algebraic dual.'},
    {'id':'E2','exact_result':'Compact symmetric tests admit differences of compact middle-positive tests; middle-positive currents are symmetric and nonnegative on these tests; ordinary locality and pointedness.',
     'source':'CLD v2, 6.5.2, 7.2.1--4','primary_url':'https://arxiv.org/pdf/1204.6277v2#page=148',
     'units':['positive-decomposition','middle-positivity'],'applicability':'Good implies almost good; support condition holds for compact tests in the original spaces.'},
    {'id':'E3','exact_result':'Positive coefficient Radon measures with compact support; ordinary continuous multiplication obeys inequality (1). Positive weak nets permit fixed continuous scalar multiplication by the supplied Lemmas 1--2 and the reproduced eventual-mass proof.',
     'source':'CLD v2, 7.2.8, 7.2.11--12, 8.5.1; explicitly supplied reviewed core Lemmas 1--2',
     'primary_url':'https://arxiv.org/pdf/1204.6277v2#page=163','units':['positive-scalar-measures','ordinary-product','weak-multiplier'],
     'applicability':'Middle-positive ordinary currents, continuous scalar in every varying-current limit. Supplied middle-cone continuity grant retained.'},
    {'id':'E4','exact_result':'The two first current differentials act by duality, are weakly continuous, square to zero and anticommute; D commutes with symmetry and satisfies diagonal Hessian duality.',
     'source':'CLD v2, 3.3.10--12, 7.7.1--5','primary_url':'https://arxiv.org/pdf/1204.6277v2#page=186',
     'units':['form-leibniz','current-differentials'],'applicability':'All actual compatible degrees. Both first differential images retained in B.'},
    {'id':'E5','exact_result':'Original canonical integration is positive and doubly closed on boundaryless spaces; integration matches analytic-cycle current with actual generic lengths.',
     'source':'CLD v2, 5.8.1--5, 7.7.4, 15.7.1, 16.6.3','primary_url':'https://arxiv.org/pdf/1204.6277v2#page=459',
     'units':['top-measures','analytic-calculus','current-differentials','generic-lengths'],
     'applicability':'Original canonical calibration, singularities and nilpotents retained.'},
    {'id':'G','exact_result':'The explicitly supplied reviewed core Theorem 3 closure operations, with finite continuous generated pairs, locally bounded generated differentiating factor and the exact permitted degrees, as stated in the paper.',
     'source':'Supplied mathematical core and scoped103 review, retained verbatim in local files',
     'primary_url':None,'units':['supplied-core.md','supplied-review.json'],
     'applicability':'Only constructed compatible currents; no density, reverse recognition, counterexample, or universal P21.3 grant.'}
])

write_json('status.json', {
 'id':'P21.3',
 'status':'partial-unresolved',
 'exact_result':'Proved fixed-neighborhood finite-test/dual equivalences for positive exhaustion, the positive-plus-both-first-exact test bipolar identity, and an exact compact-mass scalar quotient criterion for arbitrary middle-positive doubly closed ordinary currents. Neither missing geometric criterion is established.',
 'proof_file':'P21.3-argument.md',
 'concrete_gaps':[
  'No proof that every arbitrary allowed current is locally in the weak positive closure of the precise constructed-current cone on one fixed ordinary neighborhood; equality G*=closure(P+B) remains unproved.',
  'No proof that every separately generated continuous equal-canonical-curvature difference has zero normalized scalar defect against all positive doubly closed currents; the positive-plus-first-exact test certificates remain unconstructed.',
  'No generated-Psh recognition of both signs of the arbitrary difference on a fixed ordinary neighborhood.',
  'No analytic counterexample consisting of an original ambient space, separately admissible continuous pair, canonical upstairs Hessian equality, allowed T, and compact smooth detector.',
  'Primary literature search was selected, not exhaustive; the toric preprint inspected is v1 (2021), distinct from the catalogue publication (2025). The supplied reviewed calculus is used only as its explicit grant.'
 ]
})

commands = [['python','--version'],['pandoc','--version'],['pdflatex','--version'],['pdftotext','-v']]
versions=[]
for command in commands:
    r=subprocess.run(command,capture_output=True,text=True)
    versions.append({'command':command,'exit_code':r.returncode,'output':(r.stdout+r.stderr).splitlines()[:3]})
write_json('environment.json', {'python':sys.version,'platform':sys.platform,'cwd':str(ROOT),
 'versions':versions,'requested_execution':'Native Codex gpt-6.1-sol/xhigh; no worker/model dispatch used',
 'heavy_compute':'Not needed; no supervised facility supplied or launched',
 'network':'Raw shell curl failed due to unreachable configured proxy; public primary sources inspected through available web tool',
 'mathematical_audit':False})

print('Prepared proof, exact premises, literature bindings, status, and environment records.')
