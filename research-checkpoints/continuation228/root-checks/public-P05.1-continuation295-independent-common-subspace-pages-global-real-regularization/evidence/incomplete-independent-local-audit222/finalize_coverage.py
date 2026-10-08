#!/usr/bin/env python3
"""Own coverage bookkeeping. A displayed read is distinct from a hash read."""
import pathlib,json,re,hashlib
HERE=pathlib.Path(__file__).resolve().parent
B=json.loads((HERE/'frozen-bindings.json').read_text())
requests=[json.loads(v) for v in (HERE/'display-requests.jsonl').read_text().splitlines()]
def union(intervals):
    out=[]
    for lo,hi in sorted(intervals):
        if out and lo<=out[-1][1]: out[-1][1]=max(hi,out[-1][1])
        else: out.append([lo,hi])
    return out
result={}
for group,rows in B.items():
    arr=[]
    for r in rows:
        intervals=union([[q['start'],q['end']] for q in requests if q['group']==group and q['index']==r['index']])
        complete=intervals==[[0,r['characters']]]
        arr.append({'index':r['index'],'path':r['path'],'sha256':r['sha256'],'byte_match':r['match'],
                    'displayed_intervals':intervals,'characters':r['characters'],'whole_text_displayed':complete,
                    'warning':'Hash/read-request metadata is not evidence of mathematical correctness or universal historical reading.'})
    result[group]=arr
result['limitations']=['Initial aggregate tool output was truncated; exact mathematical-body and source-unit displayed ranges are separately recorded.',
    'Original-task full display truncation was NOT repaired; original completion criteria/context inspected only in the visible tail.',
    'PDF objects were hash-read, not visually read. Binary decoding character counts are bookkeeping only.',
    'Fourteen mathematical bodies are missing whole displayed reads; the requested ENTIRE audit is incomplete.',
    'Historical objects not whole displayed can have structural/log checks without acquiring whole-text-read status.']
(HERE/'whole-read-coverage.json').write_text(json.dumps(result,indent=2)+'\n')
units=[(1,26,'Preamble/title/abstract','Read. Abstract geometric claim checked below; unverified draft identity is provenance.'),
 (27,52,'Sector/primitive/main and evidence boundary','Domain exact; primitive calibrated; main conditional; historical whole-read claims not established.'),
 (53,79,'generation/boundary and unnumbered duality/continuity','Literal vertices-with-lineality sentence FAIL; needed points/pointed construction and boundary/duality verified.'),
 (80,101,'actualdual/dual/rays','Actual real max-affine, exact Delta, full-boundary continuity and FULL-space rational rec coverage checked.'),
 (102,132,'affine/approx/primalepi','Global majorant/interpolation, attained fibers, actual rec, common lower faces and scalar kernel checked.'),
 (133,185,'fiber/restriction/trace/S/dualepi/exactfiber and remark','ONE map, full image boundary, compact minimizers and exact attained fiber lowering checked; no early MA.'),
 (186,209,'tracegenerators/sync','Pointed Q carrier; ALL lifted vertices and actual trace rays; ENTIRE unbounded H equality checked.'),
 (210,233,'book and endpoint pathology','Inherited all-face secants/grouped real PCC; continuity required; spike gap checked.'),
 (234,253,'support/positive and unnumbered balance/gluing','All supports by attained fibers, independent ambient form, tangent correction, complete pages, rational walls checked.'),
 (254,280,'decrease/envelope','[4,6] eta vs next <=3 eta checked; whole R230 application continuous envelope FIRST verified; completion remains grant-dependent.'),
 (281,295,'moment and all unnumbered operator/uniformity claims','Exact qualified S272 assertions consistent with read metadata, but whole S272/S262 application audit INCONCLUSIVE.'),
 (296,345,'residual/jet/atom/realized/contact and roof convention','Subcycle/residual/coordinate atom and unrestricted roof reasoning checked; arbitrary-reference realization conditional on unread whole S272.'),
 (346,355,'all unnumbered source/evidence/scope claims and end','Scope maintained. Source direct units and local evidence checked; universal historical claims/whole-grant coverage INCONCLUSIVE.')]
paper=pathlib.Path(B['math'][25]['path']).read_text().split('\n')
labels=[]
for i,line in enumerate(paper,1):
    for label in re.findall(r'\\label\{([^}]+)\}',line):
        u=next(v for v in units if v[0]<=i<=v[1])
        labels.append({'label':label,'LF_line':i,'unit':u[2],'analysis':u[3]})
(HERE/'whole-proof-coverage.json').write_text(json.dumps({'all_paper_LF_ranges':units,'all_labels':labels,'own_conclusion':'ENTIRE request INCONCLUSIVE; all paper lines mapped, whole packet not read.'},indent=2)+'\n')
md=['# Own whole-proof and packet coverage','',
 'Every paper LF line is assigned below. This maps the ENTIRE unchanged paper, its byte-equal parallel conversion and all exact FINAL notes; it does not claim whole coverage of the unread grants. Labels use unchanged TeX source labels, not invented theorem numbering.','',
 '| LF range | Unit | Own result |','|---|---|---|']
for lo,hi,title,status in units: md.append(f'| {lo}–{hi} | {title} | {status} |')
md+=['','## All labelled equations/claims','', '| Label | LF | Unit |','|---|---:|---|']
for v in labels: md.append(f"| {v['label']} | {v['LF_line']} | {v['unit']} |")
md+=['','## All 33 mathematical bodies','', '| Index | File | Bytes match | Whole displayed and examined |','|---|---|---|---|']
for r in result['math']: md.append(f"| {r['index']} | {pathlib.Path(r['path']).name} | {r['byte_match']} | {r['whole_text_displayed']} |")
md+=['','## Six actual FINAL notes','',
 '| Note | Own assessment |','|---|---|',
 '| n1 | Premises/conventions mostly consistent; source units checked directly. Whole author read claims historical INCONCLUSIVE. Current auditor whole grant reading incomplete. |',
 '| n2 | Above affine approximation reconstructed; generation wording exception recorded. Finite grids are finite diagnostics. |',
 '| n3 | Full boundary restriction/compact lowering proof reconstructed; one T only and no intermediate MA. |',
 '| n4 | Whole-H PA synchronization/all-face Jensen/support/global decrease reconstructed. |',
 '| n5 | Actual R230 envelope domain-first use checked; raw geometry/calibration checked. Completion/arbitrary-real realization still conditional on unexamined whole grants. |',
 '| n6 | Saved/FINAL/registered comparisons and finite/conversion/build observations PASS; universal past operational/read assertions INCONCLUSIVE. |','',
 'All six actual notes have their supplied earlier-local support IDs. Own returned notes will also use only valid earlier own local IDs. No original closure or native acceptance is claimed.']
(HERE/'whole-proof-coverage.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'whole_math_bodies':sum(r['whole_text_displayed'] for r in result['math']),
    'unread_whole_math_indices':[r['index'] for r in result['math'] if not r['whole_text_displayed']],
    'paper_labels':len(labels),'paper_ranges_contiguous':all(units[i][1]+1==units[i+1][0] for i in range(len(units)-1))},indent=2))
