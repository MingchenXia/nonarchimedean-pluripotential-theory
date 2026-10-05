"""Freeze supplied primary LF bodies without altering source extraction bytes."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "CLD": {
        "file": "sources/CLD-v2.txt",
        "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
        "version": "arXiv:1204.6277v2, 25 July 2025",
        "url": "https://arxiv.org/pdf/1204.6277v2",
    },
    "GJR": {
        "file": "sources/GJR-v3.txt",
        "sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
        "version": "arXiv:2111.05741v3, 7 March 2025",
        "url": "https://arxiv.org/pdf/2111.05741v3",
    },
}
UNITS = [
    ("cld-ordinary-domain", "CLD", 14983, 15012, "11.1.7: compact neighbourhoods, ordinary opens and analytic domains"),
    ("cld-form-leibniz", "CLD", 3769, 3803, "3.3.10–12: exterior products, differential Leibniz and restriction"),
    ("cld-generated-psh", "CLD", 9729, 9781, "8.1.1–4: generated Psh, cone and ordinal construction"),
    ("cld-generated-cpsh", "CLD", 9797, 9863, "8.1.7–11: CPsh construction and printed recognition proof"),
    ("cld-positive-decomposition", "CLD", 7359, 7381, "6.5.2: compact middle-positive decomposition, full proof"),
    ("cld-middle-positivity", "CLD", 7918, 7981, "7.2.1–7: positivity, pointedness, locality and wedge"),
    ("cld-positive-scalar-measures", "CLD", 7983, 8011, "7.2.8: positive scalar currents and Radon measures, full proof"),
    ("cld-ordinary-product", "CLD", 8054, 8076, "7.2.11–12: coefficient measures and ordinary multiplication"),
    ("cld-top-measures", "CLD", 6733, 6808, "5.8.1–6: canonical top-form measures and continuous scalar integrals"),
    ("cld-current-sheaf", "CLD", 7756, 7818, "7.1.6–7: ordinary restriction and current sheaf, full proof"),
    ("cld-current-differentials", "CLD", 9309, 9381, "7.7.1–5: differential convention and double-differential duality"),
    ("cld-cutoffs-density", "CLD", 21619, 21696, "15.2.2–9: good Hausdorff applicability, cutoffs and density"),
    ("cld-analytic-calculus", "CLD", 22105, 22126, "15.7.1–2: pure analytic calculus and domain compatibility"),
    ("cld-generic-lengths", "CLD", 23434, 23459, "16.6.3: integration equals associated-cycle integration, full proof"),
    ("cld-cpsh-multiplier", "CLD", 10287, 10326, "8.5.3–5: smooth identity and exact CPsh proof"),
    ("cld-bt-definition", "CLD", 10347, 10383, "8.6.1–5: open problem, definition and elementary examples"),
    ("gjr-field-convention", "GJR", 339, 343, "2.2: nontrivial-valued field convention"),
    ("gjr-forms-scope", "GJR", 3185, 3191, "Section 10: good strict space scope"),
    ("gjr-weak-harmonic", "GJR", 3365, 3386, "10.17: weakly smooth zero form-Hessian criterion, full proof"),
    ("gjr-strong-current", "GJR", 3618, 3636, "12.1–2: topology, strong currents and restriction"),
    ("gjr-current-psh", "GJR", 2529, 2581, "7.13–15: current-positive psh definition and PL consequences"),
]

PREMISES = [
    (0, "An analytic space has compact-neighbourhood bases, and ordinary opens are analytic domains with the canonical restricted structure (CLD 11.1.7). A topologically separated pure n-dimensional analytic space, over a complete non-Archimedean field with either valuation, has the canonical calibrated CLD level-n tropical calculus. Analytic-domain calculus agrees with restriction. For a pure closed analytic subspace Y, its integration current equals that of its associated cycle, so actual generic component multiplicities are retained.", ["cld-ordinary-domain", "cld-analytic-calculus", "cld-generic-lengths"], "The target X is separated, pure and good; its ordinary open W carries restricted analytic and calibrated structures. We never replace delta_X by delta_Xred."),
    (1, "CLD Definition 8.1.1 defines Psh as the smallest ordinary subsheaf of functions with values in R union {-infinity} containing smooth positive-Hessian functions and closed under decreasing sequential limits. In Lemma 8.1.4 successors use ordinary-local decreasing limits and limits use ordinary-local membership at earlier ranks. Lemma 8.1.2 states that Psh is an upper-semicontinuous convex cone containing constants.", ["cld-generated-psh"], "Only the finite continuous slice is used for potentials. The cone assertion is also proved independently at every ordinal below; no continuity of intermediate approximants is assumed. The locally-integrable wording in the printed stabilization proof is not used."),
    (2, "On the support scope of CLD Proposition 6.5.2, every compact symmetric smooth (q,q) form is a difference of two compact middle-positive smooth forms. Its support hypothesis holds for compact support on almost-good analytic spaces. CLD Definition 7.2.1 uses symmetric currents tested against middle-positive forms for middle positivity.", ["cld-positive-decomposition", "cld-middle-positivity"], "Good implies almost good here, and W is good and boundaryless. No spanning by strongly positive forms is used."),
    (3, "On a locally differentially separated level-n tropical space, a positive scalar current is a positive Radon measure (CLD 7.2.8). Pairing a middle-positive current T with a complementary middle-positive smooth form eta gives its positive coefficient measure (7.2.11). Compact eta gives compact support. A locally bounded Borel function f has the ordinary order-zero product fT, and it agrees with smooth multiplication (7.2.12).", ["cld-positive-scalar-measures", "cld-ordinary-product", "cld-middle-positivity"], "Target finite continuous functions are locally bounded. Only positive coefficient measures of middle-positive tests and their differences are used; the broad strongly-positive spanning inference in 7.2.9 is not imported."),
    (4, "Ordinary forms have exterior products, differential Leibniz rules and compatible restriction (CLD 3.3.10–12). Ordinary CLD currents restrict and form a sheaf on locally differentially separated spaces (7.1.6–7). Their differential convention satisfies d'^2=d''^2=0, d''d'=-d'd'', d'd''J=Jd'd'', and <d'd''S,alpha>=<S,d'd''alpha> (7.7.1–5).", ["cld-form-leibniz", "cld-current-sheaf", "cld-current-differentials"], "Thus symmetric Hessians and symmetric multiplier Hessians can be tested on symmetric forms, and the displayed identities are on the actual ordinary open W."),
    (5, "A good Hausdorff analytic space is locally holomorphically and differentially separated. Compact sets inside opens admit compact smooth cutoffs. Compactly supported continuous scalars can be approximated uniformly by compact smooth scalars within the given open (CLD 15.2.2–7). Smooth compact top forms have their canonical finite signed Radon measures; multiplication by locally integrable scalars agrees with integration against these measures (5.8.1–6).", ["cld-cutoffs-density", "cld-top-measures"], "The target W has this scope for either valuation. All tests have compact support, so no global paracompactness assumption is added."),
    (6, "CLD Definition 8.1.7 defines CPsh as the smallest ordinary continuous subsheaf containing smooth positive-Hessian functions and stable under uniform sequential limits. Lemma 8.1.8 gives its corresponding sheafified ordinal stages. For smooth scalar f and symmetric doubly closed ordinary T, d'd''(fT)=d'd''f wedge T (8.5.3–4); positive smooth factors preserve middle positivity (7.2.7). The actual proof of 8.5.5 establishes multiplier positivity for CPsh by this definition and uniform convergence.", ["cld-generated-cpsh", "cld-cpsh-multiplier", "cld-middle-positivity"], "Used to audit what the printed proof actually gives, and for the known smooth-factor consistency check. Proposition 8.1.11's reverse recognition is not a premise."),
    (7, "GJR v3 works over complete nontrivially valued K. On its good strict space scope, Proposition 10.17 equates weak smoothness with zero weak form-Hessian to GJR harmonicity (hence real PL). Section 7.13 defines its psh term by positivity of the ordinary Hessian current, rather than CLD's generated sheaf. Sections 12.1–2 define strong currents as continuous functionals on weakly smooth test forms and provide restriction to ordinary currents.", ["gjr-field-convention", "gjr-forms-scope", "gjr-weak-harmonic", "gjr-current-psh", "gjr-strong-current"], "These bodies are scope diagnostics only. We do not identify a zero ordinary current with a zero weak form, convert arbitrary generated Psh differences to real PL, or infer positive closed lift and ordinary product compatibility."),
]

def main():
    texts = {}
    for k, s in SOURCES.items():
        raw = (ROOT / s["file"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == s["sha256"], k
        texts[k] = raw.decode("utf-8").split("\n")
        s["bytes"] = len(raw)
        s["lf_split_entries"] = len(texts[k])
        s["entire_primary_read"] = False
    by_id = {}
    bodies = []
    for uid, source, lo, hi, title in UNITS:
        # Literal substring determined by inclusive one-based LF indices.
        # No newline conversion, whitespace cleaning or glyph repair.
        body = "\n".join(texts[source][lo-1:hi])
        target = f"sources/{uid}.txt"
        (ROOT / target).write_bytes(body.encode("utf-8"))
        by_id[uid] = {
            "id": uid, "source": source, "title": title, "file": target,
            "lf_first": lo, "lf_last_inclusive": hi,
            "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "url": SOURCES[source]["url"], "version": SOURCES[source]["version"],
        }
        bodies.append(f"## {uid}: {title}\n\nVersion: {SOURCES[source]['version']}. Primary: {SOURCES[source]['url']}.\n\nUTF8 bytes decoded and split('\\n'); inclusive one-based LF {lo}–{hi}.\nSource hash: `{SOURCES[source]['sha256']}`. Unit hash: `{by_id[uid]['sha256']}`.\n\nLiteral statement/proof body; extraction typography and control characters are retained.\n\n```text\n{body}\n```\n")
    premises = []
    for idx, statement, units, applicability in PREMISES:
        passages = []
        for uid in units:
            unit = by_id[uid]
            passages.append({"premise": idx, "url": unit["url"],
                             "unit": uid, "lf_first": unit["lf_first"],
                             "lf_last_inclusive": unit["lf_last_inclusive"],
                             "quote_file": unit["file"], "sha256": unit["sha256"]})
        premises.append({"index": idx, "statement": statement,
                         "applicability": applicability, "passages": passages})
    (ROOT / "premises.json").write_text(json.dumps(premises, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    manifest = {"sources": SOURCES, "units": list(by_id.values()),
                "line_convention": "raw UTF8 bytes .decode('utf-8').split('\\n'); inclusive one-based LF indices; no splitlines() normalization",
                "reading_scope": "Only selected pertinent source bodies were read. Neither complete primary book/paper was read. Printed proofs relying on other results are external source evidence, not independent verification of every dependency."}
    (ROOT / "source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    appendix = "# Literal primary evidence for the P21.3 continuation\n\nThese are supplied read-only primary cache bodies, not other worker proofs. No historical review verdict is a premise. The whole primary sources were not read. Hashes identify bytes and do not establish mathematical correctness.\n\n"
    for p in premises:
        appendix += f"## External premise {p['index']}\n\n{p['statement']}\n\nApplicability: {p['applicability']}\n\nBodies: "+", ".join(x['unit'] for x in p['passages'])+".\n\n"
    appendix += "\n".join(bodies)
    (ROOT / "P21.3-primary-evidence.md").write_bytes(appendix.encode("utf-8"))
    print(json.dumps({"sources_verified": len(SOURCES), "literal_units": len(UNITS),
                      "external_premises": len(premises), "complete_primary_read": False}))

if __name__ == "__main__":
    main()
