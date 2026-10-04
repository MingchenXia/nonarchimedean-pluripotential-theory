#!/usr/bin/env python3
"""Archive only the supplied public caches and literal selected PDF pages."""
import hashlib
import json
import pathlib
import platform
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
CACHE = pathlib.Path("/workspace/research/shared-sources")
DEST = ROOT / "source-extracts"
DEST.mkdir(exist_ok=True)

SOURCES = [
    ("GJR", "GJR-2111.05741", "https://arxiv.org/pdf/2111.05741",
     "arXiv:2111.05741v3, 7 March 2025",
     [(30, 36), (44, 48), (76, 80)],
     "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
     "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3"),
    ("GRa", "GR-2506.13548v2-20261004", "https://arxiv.org/pdf/2506.13548v2",
     "arXiv:2506.13548v2, 17 September 2025",
     [(7, 14), (21, 23), (30, 34)],
     "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
     "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b"),
    ("GRb", "GR-2503.05513-20261004", "https://arxiv.org/pdf/2503.05513",
     "arXiv:2503.05513v1, 7 March 2025",
     [(1, 3), (15, 20)],
     "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
     "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c"),
    ("Thu", "Thuillier-tel-00010990v1", "https://theses.hal.science/tel-00010990v1/document",
     "HAL tel-00010990v1, 2005 thesis; PDF page = printed page + 14 in the used chapter",
     [(56, 59), (65, 68), (75, 78), (82, 85)],
     "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
     "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570"),
    ("Ber", "Berkovich-PMIHES-1993-78-5", "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
     "Publications IHES 78 (1993), Etale cohomology for non-Archimedean analytic spaces",
     [(73, 77), (125, 126)],
     "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
     "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d"),
    ("CD", "CD-1204.6277v2-20261004", "https://arxiv.org/pdf/1204.6277v2",
     "arXiv:1204.6277v2, 25 July 2025; consulted, not needed by the proof",
     [],
     "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
     "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"),
]

APPLICATIONS = [
    dict(source="GJR", statements="Definition 5.1; Remark 5.2(4,5); Corollary 5.9",
         hypotheses="Good strictly analytic spaces; nontrivial valuation; real coefficients.",
         use="Local formal Cartier metrics give actual real-PL membership; membership glues in the G-topology and the ordinary topology.",
         restriction="Semipositivity does not glue from a G-cover alone; it is checked at ordinary germs by degrees."),
    dict(source="GJR", statements="15.1-15.4; Proposition 15.5(1,2); proof of Proposition 15.7",
         hypotheses="Compact rig-smooth curve with strictly semistable formal model; legal subdivision vertices in the value group in the dense case.",
         use="Legal affine star functions are vertical Cartier metrics. Degree equals weighted outgoing slope sum on a proper reduction component. Relative-boundary reduction components are affine and impose no nef degree sign.",
         restriction="No arbitrary irrational subdivision is asserted to be a formal subdivision; no global rational slope commensurability is assumed."),
    dict(source="GJR", statements="Proposition 5.11 and its norm proof; Corollaries 5.12,5.13; Proposition 7.7",
         hypotheses="Good strict spaces and divisible coefficient group R; finite Galois extensions in our application.",
         use="An invariant average of semipositive real-PL functions descends as a semipositive real-PL function.",
         restriction="Uses addition and averaging, never a maximum of real-PL functions."),
    dict(source="GJR", statements="Proposition 7.6; Definition 7.8",
         hypotheses="Good strictly analytic source and target, nontrivial valuation.",
         use="Semipositive and harmonic real-PL functions pull back along analytic morphisms and all analytic scalar extensions. LFS is a subclass of semipositive real PL.",
         restriction="Only the full union, not a separate LFS-only envelope, is identified."),
    dict(source="Thu", statements="Theorem 2.3.8 and its proof; Proposition 3.2.4; Proposition 3.2.7 and proof; Lemma 3.2.8 and proof; Corollary 3.2.9",
         hypotheses="Strict rig-smooth affinoid, pure dimension one; finite separable extension for embedding/semistable reduction. Density and representation are applied on an ambient smooth boundaryless projective curve.",
         use="After finite extensions, every continuous obstacle is uniformly approximable on the entire affinoid by a finite-skeleton affine obstacle. A Tietze extension puts the obstacle on the ambient projective curve.",
         restriction="Thuillier-lisse is not initially declared real PL; formal real-PL membership is separately proved after legal subdivisions."),
    dict(source="GRa", statements="Theorem 4.3; Definition 4.1; Proposition 4.2; Theorem 6.1; Lemma 6.2; Theorem 6.5 and proof",
         hypotheses="Nontrivial valuation and good strict space for Theorem 4.3; unrestricted analytic scalar extensions and curve morphisms in Definition 4.1.",
         use="Every competitor is classically psh. Harmonic comparison bounds the full family. Uniform limits are classically psh. Each affinoid curve component has nonempty relative boundary.",
         restriction="Positivity alone is never used to infer continuity."),
    dict(source="GRa", statements="2.9; 2.11(5'); Lemma 3.9(1,4,6) and proof",
         hypotheses="Analytic scalar extensions; reduced strict curves, perfect field for rig-smooth normalization.",
         use="Scalar projections are surjective and closed; extended relative boundary is contained over base relative boundary. Homeomorphic normalization gives a further continuity sector using real-PL descent.",
         restriction="No openness of arbitrary scalar projection, and no automatic preservation of homeomorphic normalization under extensions, is asserted."),
    dict(source="Ber", statements="Corollary 3.7.4, following Theorem 3.7.2 and Corollary 3.7.3",
         hypotheses="Smooth morphisms in Berkovich's sense, including absence of relative boundary.",
         use="Actual projective-bundle and smooth proper-projective-factor projections are open. With properness, their fiber minimum of a continuous obstacle is continuous.",
         restriction="Does not say that a scalar projection is open."),
    dict(source="Ber", statements="Theorem 7.1.1 and its proof",
         hypotheses="Compactifiable scheme over a complete non-Archimedean field; abelian torsion sheaf. Our scheme is proper and connected and our sheaf is constant Z/2.",
         use="In degree zero properness identifies compact-support with ordinary cohomology. Comparison excludes a nontrivial clopen analytic partition, proving that the actual proper fibers are analytically connected.",
         restriction="Used only for connectedness, not for envelope descent or continuity."),
]

manifest = {"sources": [], "checked_applications": APPLICATIONS,
            "pdf_visual_checks": [
                {"source": "GJR", "pdf_page": 78,
                 "resolution": "Read actual PDF image: dense Gamma requires vertices in Sigma(Gamma); Proposition 15.5(2) imposes no boundary sign."},
                {"source": "Thu", "pdf_page": 85, "printed_page": 71,
                 "resolution": "Read actual PDF image: Corollary 3.2.9 concerns A^0(X), density in C^0(X,R); it does not itself establish semipositivity or formal-model membership."}],
            "proof_status": "Unverified mathematical draft; source hashes and execution are not correctness certificates."}
diagnostics = []
for key, stem, url, version, ranges, want_pdf, want_text in SOURCES:
    pdf, txt = CACHE / (stem + ".pdf"), CACHE / (stem + ".txt")
    got_pdf = hashlib.sha256(pdf.read_bytes()).hexdigest()
    got_txt = hashlib.sha256(txt.read_bytes()).hexdigest()
    assert got_pdf == want_pdf and got_txt == want_text, key
    entry = dict(id=key, public_source=url, exact_version=version,
                 pdf=str(pdf), pdf_sha256=got_pdf, literal_cache=str(txt),
                 literal_cache_sha256=got_txt, selected_pages=[])
    for first, last in ranges:
        out = DEST / f"{key}-pdf-pages-{first}-{last}.txt"
        cmd = ["pdftotext", "-f", str(first), "-l", str(last), "-layout", str(pdf), str(out)]
        cp = subprocess.run(cmd, capture_output=True, text=True)
        assert cp.returncode == 0, cp.stderr
        diagnostics.append(dict(command=cmd, exit_code=cp.returncode, stderr=cp.stderr))
        literal = out.read_text()
        entry["selected_pages"].append(dict(pdf_first=first, pdf_last=last,
                                             artifact=str(out.relative_to(ROOT)),
                                             literal_pdf_text=literal))
    manifest["sources"].append(entry)
(DEST / "source-provenance.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
for key, stem, page, output in [
        ("GJR", "GJR-2111.05741", 78, "gjr-78"),
        ("Thu", "Thuillier-tel-00010990v1", 85, "thuillier-85")]:
    cmd = ["pdftoppm", "-f", str(page), "-l", str(page), "-scale-to", "1800",
           "-png", "-singlefile", str(CACHE / (stem + ".pdf")), str(ROOT / "checks" / output)]
    cp = subprocess.run(cmd, capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    diagnostics.append(dict(command=cmd, exit_code=cp.returncode, stderr=cp.stderr))
(ROOT / "checks" / "source-extraction-diagnostics.json").write_text(json.dumps(diagnostics, indent=2) + "\n")
versions = {}
for tool in ("pdflatex", "pdftotext", "pdfseparate", "pdfunite"):
    cp = subprocess.run([tool, "--version" if tool == "pdflatex" else "-v"], capture_output=True, text=True)
    versions[tool] = (cp.stdout + cp.stderr).splitlines()[:3]
(ROOT / "checks" / "environment.json").write_text(json.dumps(
    dict(python=sys.version, platform=platform.platform(), tools=versions,
         compute="Small local text/PDF work only; no supervised heavy compute needed.",
         execution_route="No alternate model, worker, runtime or account was invoked. The requested model/reasoning route cannot be independently authenticated by this workspace."),
    indent=2) + "\n")
print(json.dumps(dict(sources=len(SOURCES), selected_ranges=sum(len(s[4]) for s in SOURCES),
                      hash_checks="all matched supplied hashes", provenance="source-extracts/source-provenance.json")))
