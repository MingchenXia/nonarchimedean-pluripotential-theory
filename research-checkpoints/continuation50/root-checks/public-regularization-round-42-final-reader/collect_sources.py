"""Retain selected primary PDF pages and literal cache text; no network access."""
from pathlib import Path
import hashlib, json, subprocess, sys, platform
import fitz
from pypdf import PdfReader, PdfWriter

ROOT = Path('/workspace/research/shared-sources')
OUT = Path('source-extracts')
OUT.mkdir(exist_ok=True)
SOURCES = [
 ('GJR', 'GJR-2111.05741', 'https://arxiv.org/pdf/2111.05741',
  [2, 7, 8, 30, 31, 32, 33, 34, 37, 38, 39, 41, 42, 43, 44, 45, 47, 48, 77, 78, 79, 80],
  'Strict G-site and Definition 5.1; Example 5.3; residue models and linearity; 7.8--7.10; skeleton realization, slope-degree formula and harmonicity; 15.11 is a net.'),
 ('Thu', 'Thuillier-tel-00010990v1', 'https://theses.hal.science/tel-00010990v1/document',
  [36, 40, 41, 42, 57, 58, 65, 66, 67, 68, 70, 71, 72, 81, 82, 83, 84, 103, 104, 105, 106],
  'All-domain versus strict rigid sites; type classification; 2.2.22 and finite extension condition; harmonic functions; 3.2.1 all-domain lisse; 3.4.1--3.4.2 interpolation proof; 3.4.6 skeleton continuity; 3.4.10 polar points.'),
 ('GR-classical', 'GR-2506.13548v2-20261004', 'https://arxiv.org/pdf/2506.13548v2',
  [6, 7, 10, 11, 12, 20, 21, 22, 23, 30, 31],
  'Classical curve-test class includes minus infinity; extension and pullback; boundary extension in 3.5(3); 4.3 strict real-PL comparison; 6.1 maximum principle.'),
 ('GR-PL', 'GR-2503.05513-20261004', 'https://arxiv.org/pdf/2503.05513',
  [1, 15, 16, 17], 'Cached v1 has the curve comparison as Proposition 5.1, not Proposition 3.1 cited by the later paper.'),
 ('Wanner', 'Wanner-1801.04713v3-20261004', 'https://arxiv.org/pdf/1801.04713v3',
  [1, 28, 29, 30, 31], 'Corollary 5.4 assumes continuous finite targets and the stated residue or curve alternatives; its Dini extraction is not used.'),
 ('Berkovich', 'Berkovich-PMIHES-1993-78-5', 'https://www.numdam.org/item/PMIHES_1993__78__5_0/',
  [31, 32, 48, 50, 51, 125, 126], 'Actual PDF pages 51 and 125 contain 2.6.9 and 7.1.1; properness and H_c^0 comparison give analytic connectedness of proper factors.'),
 ('CD', 'CD-1204.6277v2-20261004', 'https://arxiv.org/pdf/1204.6277v2',
  [496, 497, 498], 'The cached PDF numbers the semiample-residue assertion as 17.8.2; 6.8.2 in GJR refers to another numbering. Use GJR 7.8--7.9 directly.')]

EXCERPTS={
 'GJR': [('strict PL definition and counterexample','Definition 5.1.','Lemma 5.4.'),
         ('LFS and fixed-germ uniform approximation','Definition 7.8.','Remark 7.11.'),
         ('strict skeleton realization and harmonicity','15.2 (Skeletons of Curves).','15.8. Let X'),
         ('regularization is a weakly smooth net','Proposition 15.11.','16.')],
 'Thu': [('type-2 refinement, exact finite extension condition','Lemme 2.2.22.','Proposition 2.2.23.'),
         ('all-domain lisse definition','Définition 3.2.1.','Remarque 3.2.3'),
         ('interpolation, monotonicity and convergence proof','Lemme 3.4.1.','Remarque 3.4.3.'),
         ('skeleton continuity','Proposition 3.4.6.','Remarque 3.4.7.')],
 'GR-classical': [('boundary extension and scalar compatibility','Proposition 3.5.','3.6. In order'),
                  ('classical class and strict real-PL comparison','Definition 4.1 (','5. CONNECTIVITY BY CURVES'),
                  ('maximum principle','Theorem 6.1 (Local Maximum Principle).','The global maximum principle for classically psh')],
 'GR-PL': [('cached-version curve comparison','Proposition 5.1. Let X','Our next goal is')],
 'Wanner': [('exact continuous-target corollary and proof','Corollary 5.4. Let X','Remark 5.5.')],
 'Berkovich': [('proper analytification','2.6.9. Proposition.','2.6.10. Proposition.'),
               ('compact-support comparison and proof','7 . 1 . 1 . Theorem.','7.1.4. Corollary.')],
 'CD': [('cached-version semiample residue implication','Proposition 17.8.2.','Remarque 17.8.3.')]
}

records=[]
for key, stem, url, numbers, check in SOURCES:
    pdf=ROOT/(stem+'.pdf'); literal=ROOT/(stem+'.txt')
    reader=PdfReader(pdf); writer=PdfWriter()
    document=fitz.open(pdf)
    literal_text=literal.read_text()
    raw=literal_text.split('\f')
    # Cache segments may contain extra formfeeds, so preserve them without calling them PDF pages.
    selected_raw=[]
    for n in numbers:
        writer.add_page(reader.pages[n-1])
        text=document[n-1].get_text()
        (OUT/f'{key}-pdf-page-{n:03}.txt').write_text(text)
        if n<=len(raw): selected_raw.append(f'\nCACHE SEGMENT {n} (not a PDF page assertion)\n'+raw[n-1])
    writer.write(OUT/f'{key}-selected-pages.pdf')
    (OUT/f'{key}-literal-cache-segments.txt').write_text('\f'.join(selected_raw))
    excerpts=[]
    for label,start,end in EXCERPTS[key]:
        offset=literal_text.find(start)
        assert offset>=0,(key,start)
        finish=literal_text.find(end,offset+len(start))
        if finish<0:
            assert key=='GJR' and start=='Proposition 15.11.'
            finish=literal_text.find('16. EXAMPLE',offset)
            if finish<0: finish=literal_text.find('16. ',offset)
        assert finish>offset,(key,end)
        excerpts.append(dict(label=label,byte_start=len(literal_text[:offset].encode()),
            byte_end=len(literal_text[:finish].encode()),literal_text=literal_text[offset:finish]))
    records.append(dict(id=key,public_source=url,pdf=str(pdf),literal_extract=str(literal),
        pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
        extract_sha256=hashlib.sha256(literal.read_bytes()).hexdigest(),
        actual_pdf_pages=numbers,page_count=len(reader.pages),application_check=check,
        retained_pdf=f'{key}-selected-pages.pdf',literal_excerpts=excerpts,
        literal_segment_warning='Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection.'))

checks=[
 dict(id='strict-real-PL-realization',premises=['GJR 5.1, 15.4--15.7','Thu 2.2.22'],
      application='Only type-2 vertices are added; K is algebraically closed, so the finite separable extension is K itself. At a type-2 star the basis has slopes 0 or 1, value 0 at the centre and value-group edge lengths. Each basis is integral PL on a strict domain. Arbitrary real slopes enter only as real coefficients of those bases.',status='proved in argument'),
 dict(id='fixed-perturbation',premises=['GJR 7.8, 15.2, 15.7'],
      application='One initial finite skeleton contains every positive-genus residue point. The Dirichlet graph potential has positive outgoing-slope sum at those interior vertices and zero elsewhere. A constant makes it nonnegative. Strict PL plus subharmonicity gives nef residues; positive-degree real classes on a proper smooth curve are ample.',status='proved in argument'),
 dict(id='arbitrary-target-and-sequence',premises=['Thu 3.4.1--3.4.2, 3.4.6, 3.4.10','GR-classical 4.1.2'],
      application='No continuity assumption is added. Interpolants agree with the finite target at type-2 points; type-3 equality follows from skeleton convexity; other points follow from 3.4.1. Lindelof extraction on rational strict sublevel sets uses a countably dense ground field.',status='proved in argument'),
 dict(id='proper-factors',premises=['GR-classical 4.2, 6.1','Berkovich 2.6.9, 7.1.1'],
      application='Fibres over H(c) are compact and boundaryless. H_c^0 comparison for proper geometrically connected algebraic factors gives topological connectedness over every analytic extension. The maximum principle forces fibre constancy; actual local sections make the descended target classically psh.',status='proved in argument'),
 dict(id='boundary-obstruction',premises=['GR-classical 3.5(3), 4.1.2'],
      application='The spike is defined on the closed disc, whose actual analytic boundary is its Gauss point. It is zero on the interior, so the boundary extension assertion applies. The no-sequence conclusion uses continuity and the uncountable residue branches only.',status='proved in argument'),
 dict(id='OCR-and-numbering',premises=[],application='Visually inspected actual PDF GJR page 47, Thu pages 57, 103, 104, and CD page 497. Thu 2.2.22(i) says finite separable iff the vertices are type (2). Thu 3.4.2 uses all finite subsets of I(Y), not only type (2). GJR 7.10 states uniform convergence and does not state decreasing convergence. CD in this cache has 17.8.2.',status='checked against primary PDFs')]
(OUT/'source-provenance.json').write_text(json.dumps(dict(sources=records,application_checks=checks,proof_status='Unverified mathematical draft; hashes and execution do not certify proofs.'),ensure_ascii=False,indent=2)+'\n')
environment=dict(python=sys.version,platform=platform.platform(),
    pdflatex=subprocess.check_output(['pdflatex','--version'],text=True).splitlines()[0],
    fitz=fitz.VersionBind,
    commands=['python collect_sources.py','python finite_diagnostics.py','python build_documents.py','python verify_artifacts.py'])
Path('environment.json').write_text(json.dumps(environment,indent=2)+'\n')
print(json.dumps({'sources':len(records),'selected_pages':sum(len(r['actual_pdf_pages']) for r in records),'hashes_recorded':True}))
