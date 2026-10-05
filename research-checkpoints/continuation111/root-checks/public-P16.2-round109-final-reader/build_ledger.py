"""Construct a literal evidence ledger; do not access unsupplied source paths."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
units = json.loads((ROOT/'evidence/supplied-new/index.json').read_text())
selected = [0,1,2,3,4,7,8,9,10,11,14,15,17,19,20,21,22,23,29,30,31,32,33,34,35,36,38]
for i, u in enumerate(units):
    u['selected_literal_read'] = i in selected
    u['whole_primary_read'] = False
    u.pop('locally_read', None)
    u['coordinate_verification'] = 'Supplied source coordinates retained; full primary source bytes not downloaded or independently matched.'
    p = ROOT/u['local_file']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == u['local_sha256']
    declared = u.get('sha256',u.get('body_sha256'))
    if declared:
        assert declared == u['local_sha256']
(ROOT/'evidence/supplied-new/index.json').write_text(json.dumps(units,ensure_ascii=False,indent=2)+'\n')

whole = json.loads((ROOT/'supplied/block-02.json').read_text())
whole_records = []
for key, literal in whole.items():
    assert hashlib.sha256(literal.encode()).hexdigest() == key
    p = ROOT/'evidence/ample-primary'/f'{key}.txt'
    p.write_text(literal)
    whole_records.append(dict(file=str(p.relative_to(ROOT)), sha256=key,
                              selected_literal_read=key.startswith(('8e04c8','33518f','309dcf')),
                              whole_primary_read=False))
(ROOT/'evidence/ample-primary/index.json').write_text(json.dumps(whole_records,indent=2)+'\n')

def uref(i):
    u=units[i]
    return dict(file=u['local_file'],sha256=u['local_sha256'],url=u['url'],
                version=u.get('version',u.get('url','').split('/')[-1] if 'arxiv' in u.get('url','') else 'supplied Stacks page retrieval'),
                supplied_source_sha256=u.get('source_sha256',u.get('source_text_sha256')),
                coordinates=u.get('inclusive_one_based_LF',u.get('inclusive_LF',u.get('inclusive_renderer_lines'))),
                coordinate_rule=u.get('coordinate_rule',u.get('text_rule','inclusive one-based LF of supplied primary transcript')))

records = [
 dict(id='G',kind='task_grant',statement='Exact supplied full P16.1 theorem on geometrically unibranch projective carriers and actual ample rational bundles over algebraically closed trivial characteristic-zero fields.',application='Only smooth projective Y and actual ample A, with raw V=A^n; never applied to nonprojective X.',evidence=['supplied/block-00.txt'],status='granted in exact scope'),
 dict(id='R',kind='external_primary',statement='Temkin Theorem 1.2.1 gives finite regular-final blowup resolution for Noetherian quasi-excellent generically reduced schemes over Q.',application='Integral finite-type projective Chow source, Rees algebra projectivity, perfect-field smoothness; no claim of reading recursively cited algorithms.',url='https://arxiv.org/pdf/0904.1592v2',version='0904.1592v2',evidence=[r for r in whole_records if Path(r['file']).stem.startswith(('8e04c8','33518f'))],coordinates='Literal renderer L82--91 and L1693--1886; one complete pertinent theorem proof unit.',status='supplied selected statement and complete pertinent proof read'),
 dict(id='C',kind='external_primary',statement='Stacks Chow Lemma 30.18.1 and Remark 30.18.2 give proper birational quasi-projective refinement and dense reduced closure choice.',application='Original X proper integral over k; resulting proper immersion is closed, so source is projective over k.',evidence=[uref(32),uref(33)],status='selected complete supplied bodies read'),
 dict(id='F',kind='external_primary',statement='Stacks 37.53.6 gives structure-sheaf equality/geometric connectedness on normal integral base; 33.17.3(4) puts any normal-base point with a quasi-finite lift in the isomorphism locus.',application='Normal smooth original X, reduced integral Y, generic fiber Spec k(X); used for whole bad fibers and saturation.',evidence=[uref(34),uref(35)],status='selected complete supplied bodies read'),
 dict(id='K',kind='external_primary',statement='Positive coherent twists are globally generated; proper ample Serre vanishing holds; coherent Euler characteristics are numerical polynomials with the support-dimension bound.',application='Actual ample bundles on Y and possibly nonreduced Cartier T; supplies h0(T,mF)=O(m^(n-1)).',evidence=[uref(20),uref(21),uref(22)],status='selected complete supplied bodies read'),
 dict(id='Z',kind='external_primary',statement='A section of an invertible sheaf on a locally Noetherian scheme is regular iff it avoids associated points.',application='Finite associated points on T; injectivity reconstructed by associated-prime zero-divisor criterion.',evidence=[uref(23)],status='statement read; printed proof omitted; mechanism reconstructed, not claimed source-read'),
 dict(id='S',kind='external_primary',statement='BJ 2.23 actual normal-base section division, 6.17 homogeneous approximation, 6.24 pointwise homogeneous decomposition.',application='Only normal projective Y; divided net is not assumed monotone; normalized ample compactness repair in Section 4.',evidence=[uref(1),uref(8),uref(10)],status='selected statements and pertinent proofs read'),
 dict(id='D',kind='external_primary',statement='BJ 4.22/4.23 give all-point divisorial determination; 5.6 gives divisorial nonnegligibility.',application='Normal projective Y; finite sigma on common function-field divisorial valuations; original Div topology defined via actual values.',evidence=[uref(4),uref(7)],status='selected statements and pertinent proofs read'),
 dict(id='N',kind='diagnostic_primary',statement='BJ 4.6 extended-valued flattening proof and printed 6.21 divided-net monotonicity assertion require the diagnostics in Section 4; actual ample fixed-bundle regularization remains within G.',application='No use of arbitrary extended-valued directedness or monotonicity of divided nets.',evidence=[uref(30),uref(31),uref(9)],status='read; faulty displayed inferences are not adopted as premises'),
 dict(id='P',kind='external_primary',statement='BJ 4.10 convex composition and 7.47 capacity estimates permit an actual E1 pole with alpha=1/(n+2).',application='Only actual ample Y,A; t^n factor retained; no use of larger printed exponent range.',evidence=[uref(36),uref(38)],status='complete relevant supplied statement/proof units read'),
 dict(id='U',kind='external_primary',statement='BE 7.14 semiample smooth regularization and 8.3--8.6 continuous uniform mixed-product extension, including trivial valuation.',application='Actual ample A; smooth and real-valued continuous stages only; BE7.8 is not used.',evidence=[uref(14),uref(15)],status='complete relevant supplied statement/proof units read'),
 dict(id='H',kind='external_primary',statement='CLD18.1.2 unit logarithm Hessian zero and 8.8.5 continuous local product invariance under harmonic additions.',application='Actual frames on X minus polar image; conditional boundaryless analytification; no unbounded extension inferred.',evidence=[uref(17),uref(19)],status='complete relevant supplied units read'),
 dict(id='HU',kind='scope_audit_primary',statement='CLD8.7.2 requires local uniform convergence of continuous psh functions for its mixed-current continuity.',application='Does not prove bounded discontinuous decreasing endpoints or gate L.',url='https://arxiv.org/pdf/1204.6277v2',version='1204.6277v2',evidence=[r for r in whole_records if Path(r['file']).stem.startswith('309dcf')],coordinates='Supplied complete literal proof unit; original LF coordinates not supplied for this dictionary entry and not invented.',status='complete supplied statement/proof read; used as a negative scope check'),
 dict(id='A',kind='unresolved_primary_audit',statement='Proper nonprojective analytification is compact Hausdorff; proper surjective maps are closed analytic quotients; valuative centers are compatible with morphisms and residue-field extensions.',application='Scalar/metric descent and saturated analytic complement in Section3; topological Radon lemma itself proved.',evidence=[],status='application explained; exact primary statement/proof bindings missing'),
 dict(id='L',kind='unproved_mathematical_gate',statement='Intrinsic unbounded local original-metric product, independent of arbitrary local semipositive approximation, agrees with the global ample transferred measure and has the asserted nonpluripolar and mixed/weighted extension.',application='Needed before Section8 transported measures can be claimed as the required genuine original MA operator.',evidence=[],status='unproved; continuous compatibility and distinguished global reference-floor limit do not discharge it'),
 dict(id='T',kind='unresolved_primary_audit',statement='Complete/unimodular fan properness/smoothness, fan refinement proper morphism, invariant divisor and invariant curve correspondence in the precise toric example.',application='Section11 test only; finite integer checks and local character calculation are provided separately.',evidence=[],status='primary statement/proof bodies not retrieved'),
 dict(id='B0',kind='baseline_external_algebra',statement='Smooth local rings are regular local UFDs; finite-type regular schemes over perfect fields are smooth; finite-type fields have dimension equal to function-field transcendence degree; proper integral varieties over algebraically closed fields have constant global functions.',application='Explicit baseline facts in Sections2--3; no additional new primary bodies for these facts were retrieved.',evidence=[],status='named standard inputs; separate full primary audit incomplete'),
 dict(id='B1',kind='baseline_external_topology',statement='Riesz representation for positive functionals on C(K), normality of compact Hausdorff spaces, Radon inner regularity on open sets.',application='Full Radon inverse application proved in Section7.1; no metric-space assumption.',evidence=[],status='named standard functional-analysis inputs; no claim of new primary reading')]

ledger=dict(scope='external premises and exact task grant; no historical proposal or verdict grant',records=records,
            documentary_warning='Literal hash matches and coordinates do not prove the mathematical premises or applications.')
(ROOT/'premise-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(records=len(records),literal_dictionary_units=len(whole_records),new_literal_units=len(units),hash_discrepancies=0,unproved_gate='L'),indent=2))
