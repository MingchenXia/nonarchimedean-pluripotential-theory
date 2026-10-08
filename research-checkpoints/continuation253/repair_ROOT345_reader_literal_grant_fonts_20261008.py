from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil

R=Path('/workspace/research');D=R/'root-checks/public-P12.4-continuation345-supported-Cartier-products-and-bounded-locality-original-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=D/'P12.4-paper.tex';binding=D/'ROOT-whole-reading-and-binding-20261008.json'
assert sha(source)=='28d94a47f7020e4d03a7dcd8dc12c6af4966d19a6bf3534ced2149997eb5806c'
receipt=json.loads((R/'github-checkpoint/push-receipt-continuation252.json').read_text());assert receipt['commit_sha']=='ef17dfa600a59f3eff9e87a5eb45a4a061da2f64'
assert json.loads((R/'active-work.json').read_text())['github_pending_checkpoint'] is None
old_source=D/'ROOT-reader-before-literal-font-repair-20261008.tex';old_binding=D/'ROOT-binding-before-literal-font-repair-20261008.json'
assert not old_source.exists() and not old_binding.exists();shutil.copyfile(source,old_source);shutil.copyfile(binding,old_binding)
origin=(D/'native-origin-P12.4-paper.tex').read_text();assert sha(D/'native-origin-P12.4-paper.tex')=='c8326d65c39271bb1dc5646ddffdc065a39add9d35f0d847543440c2f0eb3a29'
pattern=re.compile(r'\\VerbatimInput\[breaklines,fontsize=\\tiny\]\{(attachments/[^}]+)\}')
parts=[]
def embed(m):
    p=D/m.group(1);s=p.read_text();assert '\\end{Verbatim}' not in s;parts.append(p)
    return '\\begin{Verbatim}[breaklines,fontsize=\\tiny]\n'+s+('' if s.endswith('\n') else '\n')+'\\end{Verbatim}'
reader=pattern.sub(embed,origin);assert len(parts)==4
header='\\usepackage[T1]{fontenc}';fonts='\\usepackage{fontspec}\n\\setmainfont{DejaVu Serif}\n\\setmonofont{DejaVu Sans Mono}'
assert reader.count(header)==2
reader=reader.replace(header,fonts,1)
encoded=reader.encode();assert all(p.read_bytes() in encoded for p in parts)
source.write_bytes(encoded)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),status='ROOT reader-only literal-appendix repair; no mathematical proof change',error='Initial global font declaration replacement also replaced one fontenc line inside the literal G331 paper appendix. The claimed byte-identical embedded00body was false before this repair.',diagnostic='Owned whole-byte containment failed for00 while01--03passed; noCR/CRLF normalization was present. Rootcause is globalstr.replace, not line-endings.',previous_reader=dict(path=str(old_source),bytes=old_source.stat().st_size,sha256=sha(old_source)),previous_binding=dict(path=str(old_binding),sha256=sha(old_binding)),corrected_reader=dict(path=str(source),bytes=source.stat().st_size,sha256=sha(source)),repair='Regenerated from immutable native origin; inlined all4original components; limited font replacement to the FIRST header occurrence. All4entire original component byte bodies are now contained in the reader.',all4_entire_literal_byte_bodies_verified=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),entire_bytes_contained=True) for p in parts],native_origin_unchanged=True,grant_attachments_unchanged=True,qualified_G331_imported_note_unchanged=True,mathematical_proof_unchanged=True,native251_frozen_reader_kept_unchanged=True,active_native251_not_given_hot_feedback=True,original_closed=False,new_paper_accepted=False,compiler_verified=False,checkpoint252_original_reader_preserved=True,prior_checkpoint252_receipt_remains_remote_historical_verification=True,new_correction_for_next_checkpoint=True,protected_P16_editor_unchanged_open=True)
(D/'ROOT-reader-literal-grant-repair-20261008.json').write_text(json.dumps(record,indent=2)+'\n')
b=json.loads(binding.read_text());b['publication_reader'].update(path=str(source),bytes=source.stat().st_size,sha256=sha(source),changes='Four original literal appendix components entirely byte-contained; font declarations changed ONLY in first native-reader header. Before-repair global font replacement is preserved and qualified separately.')
b['reader_literal_grant_repair']=dict(path=str(D/'ROOT-reader-literal-grant-repair-20261008.json'),old_claim_qualified=True,all4_current_literal_complete_bytes_verified=True,old_reader_and_binding_preserved=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
with (D/'ROOT-README.md').open('a') as stream:stream.write('\nROOTreader correction after checkpoint252: the initial global font replacement also changed one literalG331 appendix preamble line. Immutable nativeorigin,grantattachment and importedgrant note never changed. The originalreader/binding are preserved with explicitqualification; regeneration limits font substitution to the first nativeheader. ALL4original literalbyte bodies now independently match. Native251 frozen input remains unchanged and gets nohotfeedback. Compilerverification pending.\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(reader_bytes=len(encoded),reader_sha256=sha(source),all4_literal_complete_byte_bodies_match=True,native_origin_unchanged=True,original_closed=False),indent=2))
