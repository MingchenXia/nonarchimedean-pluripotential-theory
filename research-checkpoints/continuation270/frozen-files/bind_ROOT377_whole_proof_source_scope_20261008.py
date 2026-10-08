from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); K = R / 'root-checks'
S = R / 'primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008'
G = R / 'primary-data-LOCALONLY/P12.3-test-ideal-uniform-approximation-20261008'
P = K / 'P12.3-continuation377-isolated-positive-characteristic-envelopes-working-paper-20261008.tex'
B = K / 'P12.3-continuation377-ROOT-whole-proof-source-scope-and-binding-20261008.json'
U = S / 'ROOT377-full-literal-applied-source-units-LOCALONLY.json'
assert not B.exists() and not U.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
bound = lambda p: dict(path=str(p), bytes=Path(p).stat().st_size, sha256=sha(p))
records = []
def capture(p, begin, end, unit, use, reading):
    lines = p.read_text().splitlines(keepends=True)
    text = ''.join(lines[begin-1:end])
    assert text
    item = dict(unit=unit, source=bound(p), one_based_lines=[begin,end],
                literal_text=text, literal_text_bytes=len(text.encode()),
                literal_text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                application=use, ROOT_reading=reading, source_not_operational_authority=True)
    records.append(item)
capture(S/'Stacks-0535.txt',71,108,'Current Stacks 15.27.3 and 15.27.4 complete statements and immediate proofs',
        'Rank-one canonical-module strict transform on first-Fitting blowup is invertible',
        'Fresh ROOT physical full reading of this entire applied interval, with dependencies below')
for tag in ('07ZA','07ZC','07ZD','080Z','07Z3','080R','07Z7'):
    p = S / ('Stacks-'+tag+'.txt')
    lines = p.read_text().splitlines(keepends=True)
    end = next(i for i,s in enumerate(lines) if s.startswith('Comments'))
    capture(p,1,end,'Current Stacks '+tag+' complete mathematical statement and immediate proof',
            'Fitting base change, generator criterion, local freeness, strict-transform generators, blowup chart, adjugate minors',
            'Fresh ROOT full physical reading of mathematical statement and proof; navigation/comments do not supply mathematics')
capture(S/'CEMS-anticanonical-1412.6453v4.txt',134,261,
        'Corrected CEMS v4 Setting2.1 and definitions/trace/localization/Cartier-shift2.2-2.4',
        'Big test ideals on normal F-finite schemes, large-exponent trace formula, boundary comparison and Cartier shift',
        'Fresh ROOT complete reading through bounded overlapping chunks; no discarded v3 or uncorrected Lemma2.10 applied')
capture(S/'Smolkin-subadditivity-1805.08739v3.txt',120,695,
        'Corrected Smolkin v3 entire Sections2 and3',
        'Big Cartier test ideals, diagonal restriction, tensor Hom, full3.11 and3.12 proofs; singular Jacobian subadditivity',
        'Fresh ROOT entire Sections2 and3 read in overlapping untruncated chunks; printed finite-field descent defect separately treated by faithful-flatness argument in ROOT377')
capture(G/'GJKM-whole-primary.txt',738,754,'GJKM4.6 entire statement and immediate proof',
        'Exact smooth projective-over-affine scope and identification of relative Castelnuovo-Mumford regularity theorem BS20.4.13',
        'Fresh ROOT complete reading; GJKM theorem itself not applied to singular Y; deeper BS book proof not freshly read')
capture(S/'Takagi-singular-formulas-math0410612v2.txt',368,443,'Takagi2.5-2.7 complete units',
        'Independent cross-check of Jacobian formula; not fresh reconstruction of every Matlis-duality/tight-closure foundation',
        'Fresh ROOT complete statements and immediate proofs in interval; upstream Proposition2.1 not claimed fully read')
capture(S/'Takagi-singular-formulas-math0410612v2.txt',560,655,'Takagi Section4 through complete4.5',
        'Independent graded/asymptotic subadditivity and ideal-multiplication cross-check',
        'Fresh ROOT complete bounded interval; exact big-versus-finitistic notation retained')
capture(S/'HLS-mixed-characteristic-generation-published2024.txt',1554,1703,
        'Published HLS2024 Setting7.1 through completeLemma7.5',
        'Excluded source-scope shortcut: this section additionally assumes regularity and uses its stated linear-series definition',
        'Fresh ROOT complete full statements/proofs; no mixed-characteristic envelope grant')
capture(S/'HLS-mixed-characteristic-generation-published2024.txt',1800,1890,
        'Published HLS2024 entire Section8 mathematical questions',
        'Conjecture8.3 is not a global subadditivity theorem',
        'Fresh ROOT physical full reading of entire questions section; no source theorem imported from conjectures')
U.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
data=P.read_bytes()
assert data.startswith(b'\\documentclass') and data.rstrip().endswith(b'\\end{document}')
protected=K/'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
public=[]
for rec in records:
    public.append({k:v for k,v in rec.items() if k!='literal_text'})
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),continuation=377,atom='P12.3',
       status='ENTIRE ROOT working proof physically read; independent native reconstruction required',
       paper=bound(P),full_paper_ROOT_physical_reading=True,
       reading_method='Whole saved source read in overlapping bounded untruncated chunks, followed by reading all four small amendments and their context; no hash substitutes for physical reading',
       physical_whole_primary_book_reading_claim=False,private_literal_unit_ledger=bound(U),
       applied_primary_units=public,
       physically_viewed_primary_pixels=[dict(**bound(S/'Smolkin-v3-page11-ROOT-finite-field-descent.png'),one_based_pdf_page=11,physically_viewed_by_ROOT=True,application='Printed finite-field L-module-via-linear-retraction wording confirmed; independent faithful-flat descent repair proposed')],
       source_versions=['Smolkin1805.08739v3 corrected3.12/5.15','CEMS1412.6453v4 corrected including published too-strong2.10','Takagi math0410612v2','HLS published2024 separate from arxiv2106.14329v4','Current Stacks public primary fetched8Oct2026'],
       new_proposed_sector='ALL finite CONT obstacles for isolated normal AFFINE finite-type PERFECT characteristicp closed codim>=2 germs, all dimensions and all semivaluation supports; boundedUSC greatest ONE-C-net envelope; exact primary-gauge cocycle',
       model_gate='Canonical-module Fitt1 blowup and finite normalization, effective fibre-supported Delta with K_Y+Delta CARTIER, actual primary graph realization; no smooth resolution premise',
       main_bound='0<=P(f_C)-g_m<=(c vJ+vJac(Y/k)+v(bF))/m<=(c+a+b)N_J/m on every normalized support',
       independent_verification_targets=['Actual primary common-model graph and rank-one canonical-module strict transform','Scheme-global test divisor and large-exponent trace formula','Relative regularity over affine base; BS20.4.13 complete proof not ROOT freshly read','Correct Frobenius-linearity of global-section source maps','All-support finiteness and directions of Jacobian/pair test-ideal containments','Finite-field corrected faithful-flat diagonal-map descent','Signed lattice density, positive homogeneity, no upward-limit positivity recognition'],
       only_existing_correctness_grant='WHOLE qualified G331 P12.2 comparison with mandatory source/scope qualifications; no envelope/energy/resolution consequence imported',
       residual_original=['Nonisolated normal all-characteristic whole-link envelope continuity','Mixed characteristic and imperfect/nonalgebraic excellent scope','All nonnormal normalization/conductor positive-domain rules and complete original comparison'],
       original_P12_3_closed=False,new_accepted_paper=False,solved_original_atoms=16,open_original_atoms=26,accepted_papers=97,
       source_bodies_literal_units_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,
       supplied_programs_executed=False,protected_editor=bound(protected),protected_editor_open_unchanged=True,
       native_compiler_result='Not yet verified',no_new_editor_tab=True)
B.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(paper=bound(P),binding=bound(B),private_literal_units=bound(U),units=len(records),original_closed=False,new_accepted_paper=False),indent=2))
