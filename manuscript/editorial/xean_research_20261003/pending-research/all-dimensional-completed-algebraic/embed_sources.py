"""Embed complete primary units used by the proof, preserving cached text.

Run from this workspace: python embed_sources.py
No network and no writes to source origins. Markers are complete-unit boundaries,
not output-budget cuts. Source-internal references remain source references.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "sources"

# Anchored patterns prevent extraction from tables of contents or prior citations.
CLD_UNITS = [
    ("CLD 1.3.6: J and the differential signs", r"^Lemme 1\.3\.6\.", r"^1\.3\.7\."),
    ("CLD 1.9.4: closed-subset extension, whole proof", r"^Lemme 1\.9\.4\.", r"^1\.9\.5\."),
    ("CLD 1.9.8-9: differentials and dimension nullity", r"^1\.9\.8\.", r"^1\.9\.10\."),
    ("CLD 3.3.3: ambient coefficient representatives", r"^3\.3\.3\.", r"^Définition 3\.3\.4\."),
    ("CLD 3.3.10-12: wedge, Leibniz, pullback", r"^3\.3\.10\.", r"^3\.3\.13\."),
    ("CLD 3.4.4: compact-image nullity, whole proof", r"^Proposition 3\.4\.4\.", r"^Corollaire 3\.4\.5\."),
    ("CLD 5.4.3-4: compact charts are pleasant", r"^Définition 5\.4\.3\.", r"^Proposition 5\.4\.5\."),
    ("CLD 5.8.1-5: top forms and actual variation measures", r"^5\.8\.1\.", r"^5\.8\.6\."),
    ("CLD 5.10.1: integration/pushforward, whole proof", r"^Proposition 5\.10\.1\.", r"^5\.10\.2\."),
    ("CLD 5.11.1: Stokes and the separate symmetric Green statement", r"^Proposition 5\.11\.1\.", r"^\fCHAPITRE 6"),
    ("CLD 6.2.1-2: ordinary smooth forms", r"^Définition 6\.2\.1\.", r"^6\.2\.3\."),
    ("CLD 7.3.5: continuous/non-tropical multiplier currents, full ending", r"^7\.3\.5\.", r"^Proposition 7\.3\.6\."),
    ("CLD 11.1.1-2: Banach spectra and affinoid foundations", r"^11\.1\.1\.", r"^Exemple 11\.1\.3\."),
    ("CLD 11.1.5-10: rational neighborhoods, good spaces, tensors, residue fields", r"^11\.1\.5\.", r"^11\.1\.11\."),
    ("CLD 11.2.2-3: separatedness and all local dimensions", r"^11\.2\.2\.", r"^Remarque 11\.2\.4\."),
    ("CLD 11.4.1: relative-interior composition equality", r"^11\.4\.1\.", r"^Exemple 11\.4\.2\."),
    ("CLD 11.4.4: actual finite-module Banach algebras", r"^11\.4\.4\.", r"^11\.4\.5\."),
    ("CLD 11.7.7: strict affinoid neighborhood bases", r"^11\.7\.7\.", r"^\f322"),
    ("CLD 13.3.1-3: degree and Artinian base change, complete lemma proof", r"^13\.3\.1\.", r"^13\.3\.4\."),
    ("CLD 14.1.8: compact pleasant moments", r"^Proposition 14\.1\.8\.", r"^Proposition 14\.1\.9\."),
    ("CLD 14.1.12: compatible skeletal refinements, complete proof", r"^Proposition 14\.1\.12\.", r"^Lemme 14\.2\.1\."),
    ("CLD 14.2.2: actual constant finite-flat degrees, complete proof", r"^Proposition 14\.2\.2\.", r"^Proposition 14\.2\.3\."),
    ("CLD 14.3.2-6: canonical calibration and scalar projection, complete proof endings", r"^14\.3\.2\.", r"^14\.4\.1\."),
    ("CLD 14.4.3: same-carrier restriction factor, full body", r"^Remarque 14\.4\.3\.", r"^Définition 14\.5\.1\."),
    ("CLD 14.5.1-2: positive summed image calibration", r"^Définition 14\.5\.1\.", r"^Proposition 14\.5\.3\."),
    ("CLD 15.1.1: ordinary unit descriptions, complete proof", r"^Proposition 15\.1\.1\.", r"^Corollaire 15\.1\.2\."),
    ("CLD 15.2.2: good Hausdorff implies local holomorphic separation", r"^15\.2\.2\.", r"^Lemme 15\.2\.3\."),
    ("CLD 15.2.5: compact cutoff, entire stated proof", r"^Corollaire 15\.2\.5\.", r"^Théorème 15\.2\.6"),
    ("CLD 15.3.1: canonical scalar top-measure projection, full proof", r"^Proposition 15\.3\.1\.", r"^Proposition 15\.3\.2\."),
    ("CLD 15.7.1-2: pure analytic tropical structure and domain compatibility", r"^Théorème 15\.7\.1\.", r"^Remarque 15\.7\.3\."),
    ("CLD A.2.3-4: supporting compact-cutoff argument, full proofs", r"^Lemme A\.2\.3\.", r"^Théorème A\.2\.5"),
]
OTHER_UNITS = [
    ("Ducros-2012.txt", "Ducros Theorem 3.2: correct upper bound and full primary proof",
     r"^Théorème 3\.2\. Soit X[^\n]*dimension d,", r"^\(3\.3\) Remarque\."),
    ("Berkovich-1993.txt", "Berkovich 1.5.3-5: boundaryless finite maps and base-change interiors",
     r"^\s*1\.5\.3\. Examples", r"^\s*1\.5\.6\. Remark"),
]


def extract(filename, title, start, end):
    data = (SOURCES / filename).read_text()
    starts = list(re.finditer(start, data, re.M))
    if len(starts) != 1:
        raise ValueError((title, "start match count", len(starts)))
    begin = starts[0].start()
    stop = re.search(end, data[starts[0].end():], re.M)
    if stop is None:
        raise ValueError((title, "missing end marker"))
    finish = starts[0].end() + stop.start()
    body = data[begin:finish]
    # Preserve the source body byte-for-byte in its artifact. Form-feed page
    # separators are displayed as newlines in the embedded rendering only.
    key = f"primary-{len(records)+1:02d}"
    artifact = SOURCES / (key + ".txt")
    artifact.write_text(body)
    record = {
        "id": key, "title": title, "source": filename,
        "first_line": data[:begin].count("\n") + 1,
        "last_line": data[:finish].count("\n"),
        "end_boundary_pattern": end,
        "end_boundary_preview": data[finish:finish+110],
        "bytes": len(body.encode()),
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "ending": body.rstrip().splitlines()[-1],
        "complete_selected_unit": True,
    }
    records.append(record)
    return (f"### {key}: {title}\n\n"
            f"Cached primary {filename}, lines {record['first_line']} to "
            f"{record['last_line']}. The next primary heading is the extraction "
            "boundary; no output-budget truncation was used. Source typography "
            "and OCR artifacts are retained.\n\n```text\n" +
            body.replace("\f", "\n").rstrip() + "\n```\n\n")


records = []
appendix = (
    "## Embedded primary-source bodies\n\n"
    "The following are exact cached primary units, not campaign descriptions. "
    "Each selected statement has its full source ending and all of the proof "
    "printed for that unit. They import the stated analytic foundations; they "
    "do not independently reprove the entire CLD theory or every source-internal "
    "reference. Mathematical typography in text extraction can be defective. "
    "The restricted, explicit uses in the argument control applicability. "
    "In particular, the false universal dimension equality in CLD 12.2.4 and "
    "the broad compact-support formulation in 15.2.9 are excluded. Ducros 3.2 "
    "supplies the correct upper bound. The source manifest records whole-file "
    "origins and hashes; hashes are integrity data only. In the PDF rendering "
    "alone, unsupported monospaced norm bars and slanted inequalities are "
    "written as ||, <=, and >=, and the ffi ligature is expanded. Invisible "
    "OCR control bytes are displayed explicitly. The authoritative Markdown "
    "and individual primary text artifacts retain their original bytes.\n\n"
)
for title, start, end in CLD_UNITS:
    appendix += extract("CLD-v2.txt", title, start, end)
for filename, title, start, end in OTHER_UNITS:
    appendix += extract(filename, title, start, end)
appendix += "**End of embedded primary bodies and authoritative argument.**\n"
(SOURCES / "primary-units.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
(SOURCES / "primary-bodies.md").write_text(appendix)
argument = ROOT / "P06.2-argument.md"
text = argument.read_text()
marker = "<!-- PRIMARY_APPENDIX_INSERTION_POINT -->"
if marker in text:
    text = text[:text.index(marker)] + appendix
else:
    text = text[:text.index("## Embedded primary-source bodies")] + appendix
argument.write_text(text)
print(json.dumps({"primary_units": len(records), "embedded_bytes": len(appendix.encode()),
                  "argument_bytes": len(text.encode()), "all_end_markers_found": True}))
