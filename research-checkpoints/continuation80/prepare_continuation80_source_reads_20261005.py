"""Freeze only the actual literal ranges read for the conditional descent proposal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
S = R/'root-checks/continuation80-fiberwise-and-finite-data-descent-source-reads'
P = R/'root-checks/P16.1-fiberwise-zero-class-and-finite-data-envelope-descent-20261005-continuation80.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not S.exists() and P.is_file()
expected = {
    'new-primary-2609.27610v1-20261004.txt':'c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d',
    'P16-arxiv-1801.08229-20261004.txt':'659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0',
    'P16-arxiv-1805.01016-20261004.txt':'8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233',
    'Thuillier-tel-00010990v1.txt':'e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570',
}
manifest=R/'campaigns/round-72/P16.1-public-source-explicit-strict-barrier-and-complete-unibranch-Runge-equation/input-manifest.json'
sources=json.loads(manifest.read_text())['public_sources']
bindings={str(Path(d['literal_extract'])):d['extract_sha256'] for d in sources}
for name,digest in expected.items():
    source=R/'shared-sources'/name
    assert sha(source)==digest==bindings[str(source)]
assert sha(P)=='68ec10718968af4c9c656425142fecbd1069338c8287475ce3ee3c09ecec5e2e'
S.mkdir()
specs=[
    ('Wu','2609.27610v1','new-primary-2609.27610v1-20261004.txt','genuine-varying-and-fixed-class-approximants',399,446,
     'Metric definition and the stated PL/FS approximation; F1 actual reference conversion and restrictions remain new applications requiring reconstruction.'),
    ('Wu','2609.27610v1','new-primary-2609.27610v1-20261004.txt','zero-class-sign-and-flat-stratum-descent-diagnostic',563,638,
     'Correct -m phi to m phi. Openness and density alone do not justify prescribed divisorial-net lifts; the proposal instead uses bounded fibers and birational divisorial identity.'),
    ('Wu','2609.27610v1','new-primary-2609.27610v1-20261004.txt','countable-envelope-and-finite-data-extension-diagnostic',2697,2755,
     'Retain the singular local/global equality gate. Replace unsupported support-set equality by the positive pushforward/contact integral. Only finite competitors descend.'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','genuine-definition-and-varying-class-closure',2173,2250,
     'Generically finite means not identically negative infinity on any component. Actual numerical-class/metric compatibility on fibers is an additional F1 premise.'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','decreasing-finite-Hdom-majorants-and-proof',2418,2468,
     'Pre-EP ample-class majorants are a directed net, not an assumed fixed-L FS sequence. Finite Hdom nef domination must descend with the bundle data.'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','minimum-usc-extension-and-correct-zero-class-proof',2494,2535,
     'The printed BJ zero-class proof uses m phi in its trivially valued setting. It is not silently applied over arbitrary H(x).'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','continuous-obstacle-to-EP-and-compact-majorants',2905,2975,
     'Use compact decreasing closed sets to obtain feasible finite competitors, and continuous obstacle envelopes to prove EP without descending arbitrary families.'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','actual-E1-uniqueness-and-domination',5440,5477,
     'The dominated metric is actual E1 and the measure is its actual MA. New singular operator identification remains an explicit C3/C4 check.'),
    ('BJ','1801.08229v4','P16-arxiv-1801.08229-20261004.txt','EP-antecedent-and-continuous-orthogonality-proof',6300,6359,
     'Section13 explicitly assumes EP. Continuous orthogonality follows from the obstacle segment and the energy-envelope derivative; use it only after countable EP.'),
    ('BE','1805.01016v3','P16-arxiv-1805.01016-20261004.txt','cycle-mass-positive-continuous-operator-and-field-pushforward',2611,2779,
     'Smooth tropical ground-field invariance extends through uniform genuine approximants. Retain the fundamental cycle, positivity and actual reference; no formal completion operator.'),
    ('Thuillier','tel-00010990v1','Thuillier-tel-00010990v1.txt','strict-smooth-curve-harmonic-and-decreasing-subharmonic-definition',3720,3824,
     'Curve is strict smooth over a nontrivially valued auxiliary complete algebraically closed field. Sections, finite maxima and bounded decreasing limits supply subharmonicity.'),
    ('Thuillier','tel-00010990v1','Thuillier-tel-00010990v1.txt','strong-maximum-principle-proof-and-locality',3830,3945,
     'Proper connected curve: nonempty maximum set is closed by usc and open by the strong maximum principle. This does not itself establish metric restriction or Bertini.'),
]
units=[]
for author,version,name,label,first,last,limits in specs:
    source=R/'shared-sources'/name
    lines=source.read_bytes().decode('utf-8').split('\n')
    literal='\n'.join(lines[first-1:last])
    path=S/(author+'-'+label+'.txt');path.write_text(literal)
    assert path.read_bytes().decode('utf-8')==literal
    units.append({'id':author+'-'+label,'version':version,'source':str(source),
        'source_sha256':expected[name],'inclusive_one_based_LF':[first,last],
        'literal_file':str(path),'literal_sha256':sha(path),
        'selected_literal_body_root_read':True,'whole_primary_body_root_read':False,
        'new_application_independently_reviewed':False,'scope_and_limits':limits})
write(S/'source-read-record.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'units':units,'proposal':str(P),'proposal_sha256':sha(P),
    'whole_saved_proposal_root_read':True,'proposal_independently_reviewed':False,
    'accepted_dependency':False,'original_P16_1_closed':False,'original_P13_2_closed':False,
    'active_round72_73_frozen_and_no_hot_feedback':True,
    'conditional_antecedents':['F1','F2','C1','C2','C3','C4'],
    'additional_geometric_applications_to_verify':['geometric connectedness of resolution fibers',
        'projective smooth curves through prescribed points in characteristic zero',
        'complete field-extension surjectivity',
        'finite normalization/universal-homeomorphism and Hdom nef-data descent']})
print(json.dumps({'source_read_record':str(S/'source-read-record.json'),
    'source_read_record_sha256':sha(S/'source-read-record.json'),
    'literal_units':len(units),'proposal_sha256':sha(P),'accepted_dependency':False},indent=2))
