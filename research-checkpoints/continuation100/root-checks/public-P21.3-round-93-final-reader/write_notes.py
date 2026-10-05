from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def main():
    premises = json.loads((ROOT / "premises.json").read_text(encoding="utf-8"))
    summaries = [
        ("n1", "All-ordinal generated-Psh cone operations and actual ordinary signed test measures, for the full target ambient scope; no Psh-to-CPsh recognition or universal multiplier claim.", "Proves cone closure at every sheafified ordinal successor and limit, so finite continuous generated-Psh differences form a vector space. Builds signed compact Radon measures for canonical curvature and ordinary positive-current multiplier tests with middle-positive decomposition, exact differential duality and retained generic lengths. Lists the complete primary-premise set with versions, LF bodies, hashes and applicability. These are foundations, not a solution of P21.3.", []),
        ("n2", "Exact ORIGINAL-pair dual reduction: pair-tested weak closure equals exact finite interpolation and signed curvature-relation preservation; failure would yield actual Psh potentials, but no failure or universal closure is established.", "For every fixed target W,T, proves equivalence of the original continuous generated-Psh pair predicate, closure of ambient Hessian test measures in the topology tested on Psh-continuous differences, exact finite interpolation on actual psh tuples, and preservation of every signed curvature dependence. Finite-dimensional separation splits coefficients into two admissible psh functions on the same analytic open. It improves the stronger all-continuous-kernel certificate by retaining original-pair membership, but does not verify the condition for arbitrary singular currents or construct a counterexample. Every-open quantification remains explicit.", ["n1"]),
        ("n3", "Printed CLD continuous-recognition successor proof assumes continuous predecessor approximants; fixed-domain Dini does not repair intermediate sheafification. Precise universal pairwise gap remains; P21.3 unresolved.", "Audits every ordinal operation and recognition step, distinguishing safe cone closure and CPsh inclusion from the missing reverse-recognition successor. Preserves literal pertinent source statements and full selected proofs. Documents ordinary-local fixed-neighbourhood and positive-gluing requirements; topological/Euclidean diagnostics are not analytic counterexamples. Notes the actual CPsh scope of the multiplier-positivity proof and GJR's field/function/current distinctions. Reports the full manuscript/PDF, indexed primary evidence and reproducibility packet with exact unresolved finite-interpolation condition and candidate=false.", ["n1", "n2"]),
    ]
    notes = []
    for nid, summary, detailed, support in summaries:
        body = (ROOT / f"{nid}.md").read_text(encoding="utf-8")
        if nid == "n1":
            body += "\nComplete external premises and primary passage indices:\n"
            for p in premises:
                body += f"\nPremise {p['index']}: {p['statement']}\nApplicability: {p['applicability']}\n"
                for q in p["passages"]:
                    body += f"Evidence (premise {q['premise']}): {q['url']}, inclusive UTF8 LF {q['lf_first']}-{q['lf_last_inclusive']}; complete literal body {q['quote_file']}. Unit hashes are preserved in source-manifest.json.\n"
            body += "\nFull cached-source hashes: CLD v2 64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085; GJR v3 57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3. These are the supplied primary paths copied read-only into this workspace; neither complete primary text was read.\n"
        notes.append({"id": nid, "summary": summary, "detailedSummary": detailed,
                      "text": body, "support": support})
    (ROOT / "notes.json").write_text(json.dumps({"notes": notes, "candidate": False}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"notes": len(notes), "candidate": False, "support": [n["support"] for n in notes]}))

if __name__ == "__main__":
    main()
