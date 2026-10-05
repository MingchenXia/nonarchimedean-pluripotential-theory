"""Freeze only authorized primary caches and verify literal LF excerpts."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

APPLICATIONS = {
 "BJ": {
  "checked_applications": [
   "Conventions allow reduced possibly nonnormal projective varieties. Relative integral closure preserves the prescribed generic fiber; vertical DVR and multiplicity conventions are retained.",
   "The rational PL lattice and density, ample models on a determination, generated PSH cone, divisorial order determination, and Sections 7--12 genuine intersection/finite-energy theory are used with their general-variety scope.",
   "Raw mixed weights are b_E times restricted intersection degrees; E is normalized by (n+1)V. Weighted continuity 7.21 is used rather than unweighted 7.19 for winning-locus limits.",
   "Theorem 12.8 is an EP/surjectivity/completeness equivalence, not singular EP. Theorem 5.20 and Remark 4.19 retain smoothness. Lemma 5.13 onto pullback retains approaching larger classes with EP.",
   "Two-sided derivative 8.5 and bounded-J integration 9.19 are read before variational attainment. Printed sign slips in weighted pairing and absolute-difference formulas are explicitly corrected in the argument."
  ],
  "concrete_limits": "No singular envelope theorem is inferred from the global operator, strict concavity, topological normalization, or the conditional general-variety equation theorem. Real ample global theory does not establish real-class EP."
 },
 "W": {
  "checked_applications": [
   "Definitions 3.1 and 3.15 are audited: the contact constant is retained in the minorant, finite-affine infinite coordinates require zero coefficients, upper growth replaces the incompatible printed lower growth only in auxiliary local lemmas.",
   "Local mass/IBP, Rossi 5.6, damping 3.30, trace 6.12, Runge 6.14--6.16, and envelope 7.1 proof bodies are checked as diagnostic proposed arguments, not accepted theorem premises.",
   "The open weak trace extension precedes radial equality. The integer trace needs local constancy on a shrink, and gamma=1 requires no division by gamma-1. W 7.1 explicitly depends on weak/global 6.5."
  ],
  "concrete_limits": "Public v1; no correctness or peer-review verdict. Weak trace extension, full weak Runge induction, and singular EP remain unresolved in this reconstruction. Correcting auxiliary definitions does not redefine genuine global PSH."
 },
 "CLD": {
  "checked_applications": [
   "8.7.2 is used only for locally uniform convergence of continuous functions. Bounded decreasing discontinuous products instead use a common genuine global representation and BJ weighted continuity.",
   "17.8.4 is nef-to-psh for strict integer PL; 18.8.4 is the represented integer-PL residual-degree/current equivalence; 18.8.6 permits complete extension of an already represented positive metric.",
   "18.4.7 model compatibility keeps residual degrees, defects and multiplicities. Continuous model locality is used before bounded-limit locality.",
   "Printed 12.2.4 dimension equality is not used; constant moments show why only Ducros's upper bound is appropriate."
  ],
  "concrete_limits": "No unsupported general positive-current pullback/converse, or automatic real-PL/model membership. The strict/nonstrict wording change in 18.8.8 is not substituted for the actual strict theorem."
 },
 "GM": {
  "checked_applications": [
   "2.8/2.10 are applied after actual strict G-cover, frame, tensor-denominator and norm-one transition construction. The metric is on the specified line bundle.",
   "2.7 extends an actual formal metric on a compact strictly analytic domain, not an unspecified relative PL selection. 2.6 and projective domination 2.4 supply the proper algebraic/projective representation.",
   "3.11 is applied to the globally represented metric after residue-nef local models. Lemma 3.3 detects field nefness only for an already represented K-model."
  ],
  "concrete_limits": "K is nontrivially valued and complete; properness/compactness and strict domains are checked first. The avoidable GM4.12 generic-class requirement is not used; auxiliary ample bundles may have non-descending generic class."
 },
 "Wa": {
  "checked_applications": [
   "Section 2 common semistable skeleton, lisse membership and positive outgoing-slope Laplacian criterion apply over complete algebraically closed nontrivially valued fields.",
   "Section 4 has a smooth proper algebraic curve hypothesis: a locally algebraic curve is compactified smoothly before applying it only on the original open. The main curve slope proof instead uses Section 2 and Thuillier."
  ],
  "concrete_limits": "Local algebraicity of a smooth analytic curve does not make the coordinate pullbacks algebraic; they remain analytic units. No arbitrary punctured-neighborhood radial limit is claimed."
 },
 "Th": {
  "checked_applications": [
   "2.2.24, 2.3.20/2.3.21 give unit-log skeleton factorization, harmonic balancing and type I/IV local constancy. All units use one model.",
   "3.4.4 supplies the positive lisse-Laplacian criterion; 3.1.8(ii) passes decreasing limits with the identically minus-infinity alternative.",
   "Disk harmonic comparison and 3.1.9 give the boundary Gauss-point radial equality at rational centers, including logarithmic poles."
  ],
  "concrete_limits": "The field and smooth curve hypotheses are retained. Affinoid boundary slopes are not tested on the curve open; finite real breakpoints are allowed."
 },
 "BE": {
  "checked_applications": [
   "5.14 and 5.16(vi), including proofs, express a represented rational model function as an exact pure FS difference on a common generic class M.",
   "5.17 and product sections add a cancelling pure FS metric on aH_K-M, so both final FS metrics lie on the same descending aH_K. Laurent coefficients are expanded only for these final sections.",
   "7.8 is applied to ample generic bundles and nef represented models over nontrivial K, with general-variety scope. The proof uses a consistent auxiliary ample model A and epsilon tending to zero.",
   "7.2/7.6 and field FS compatibility connect actual FS-defined cones, uniform approximations and exact Gauss descent. 8.18/CLD compatibility retains genuine intersection weights."
  ],
  "concrete_limits": "No envelope or finite-energy singular existence is supplied by this nef-to-FS theorem. Laurent expansions are not taken over the completed algebraic closure Omega. Exact FS differences are not asserted semipositive."
 },
 "GR": {
  "checked_applications": [
   "Actual strict-G Q-PL membership is proved before Proposition 5.1 or Corollary 5.4. The latter tests every smooth analytic curve map over one algebraically closed analytic extension.",
   "5.1 uses local algebraicity only for the source curve; coordinate pullbacks stay analytic units. Corrected relative contact minorants give the positive curve slopes independently.",
   "Remark 1.8's warning about general R-PL positive-current pullback/converse is retained."
  ],
  "concrete_limits": "Continuous finite affine selection alone is not model membership. Rational slopes/constants are used in the new strict representation; no semipositive rational approximation of arbitrary real slopes is assumed."
 },
 "D": {
  "checked_applications": [
   "Published Theorem 3.2 is applied to compact Gamma-strict analytic domains with finitely many units, yielding a finite c-polytope image and dimension at most the analytic dimension.",
   "Actual valued-field image Theorem 1.2 and its closedness/dimension proof are recorded. All branch-equality hyperplanes refine the polytope; continuity fixes a finite selection on each connected relative cell.",
   "Closure preimages are finite strict Laurent domains after clearing rational slopes and constants, and form an admissible G-cover."
  ],
  "concrete_limits": "The dimension equality printed in CLD is unnecessary and fails for constant moments. Noncompact arbitrary relative subsets are not automatically finite rational polytopes."
 },
 "GJR": {
  "checked_applications": [
   "7.1 supplies residue-nef formal models on sufficiently small strict neighborhoods. 7.4 relates the already represented paracompact model to pointwise semipositivity.",
   "7.6(2') permits analytic-field detection of semipositivity. The neighborhood, line-bundle frame and global represented model hypotheses are checked separately."
  ],
  "concrete_limits": "These statements detect model nefness; they do not construct arbitrary analytic gluing, weak trace extension, singular EP, or equation attainment."
 }
}

def main():
    manifest = json.loads((ROOT / "source-manifest.json").read_text())
    ranges = json.loads((ROOT / "source-extracts/ranges.json").read_text())
    (ROOT / "sources").mkdir(exist_ok=True)
    records = []
    checks = []
    for item in manifest:
        sid = item["id"]
        files = {}
        for kind, record in item["verified_files"].items():
            extension = Path(record["path"]).suffix
            local = ROOT / "sources" / f"{sid}-{kind}{extension}"
            if not local.exists():
                local.write_bytes(Path(record["path"]).read_bytes())
            data = local.read_bytes()
            digest = sha(data)
            assert digest == record["sha256"], (sid, kind)
            files[kind] = {
                "authorized_path": record["path"],
                "local_copy": str(local.relative_to(ROOT)),
                "sha256": digest, "bytes": len(data),
                "matches_supplied": record["matches_supplied"]
            }
            checks.append({"source": sid, "kind": kind, "hash_matches": True})
        source_text = (ROOT / files["literal_extract"]["local_copy"]).read_text()
        lines = source_text.split("\n")
        excerpts = []
        for entry in ranges:
            if entry["source"] != sid:
                continue
            lo, hi = entry["start_LF"], entry["end_LF"]
            expected = "\n".join(lines[lo - 1:hi])
            assert 1 <= lo <= hi <= len(lines)
            assert entry["literal"] == expected
            artifact = Path("source-extracts") / entry["artifact"]
            assert (ROOT / artifact).read_text() == expected
            excerpts.append({**entry, "artifact": str(artifact), "literal_sha256": sha(expected.encode()),
                             "application_scope": APPLICATIONS[sid]})
        records.append({
            "id": sid, "saved_version": item["saved_version"],
            "title": item.get("title", "Formes differentielles reelles et courants sur les espaces de Berkovich"),
            "public_source": item["public_source"], "files": files,
            "LF_split_count": len(lines), "whole_source_audit_claimed": False,
            **APPLICATIONS[sid], "literal_statements_and_proof_bodies": excerpts
        })
    result = {
        "index_rule": "Inclusive one-based LF ranges in UTF-8 text.split('\\n'); literals joined by LF without an added trailing newline.",
        "scope": "Only ten user-authorized primary caches. Extracted/read passages are not a whole-source audit; source results and new arguments remain unverified mathematical drafts.",
        "sources": records,
        "hash_checks": checks,
        "excerpt_count": sum(len(r["literal_statements_and_proof_bodies"]) for r in records)
    }
    (ROOT / "source-extracts/source-provenance.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"sources": len(records), "files": len(checks), "literal_excerpts": result["excerpt_count"], "all_hashes_match": True}))

if __name__ == "__main__":
    main()
