from pathlib import Path
import json, hashlib, re
ROOT=Path(__file__).resolve().parent
SRC=Path('/workspace/research/shared-sources')
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(name,obj): (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inp=(ROOT/'input.json').read_bytes(); orig=(ROOT/'input-original.json').read_bytes()
x=json.loads(inp); a=x['assignment']
assert inp==orig
assert (ROOT/'assignment-original.txt').read_text()==a
assert json.loads((ROOT/'task-original.json').read_text())==x['task']
primary=json.loads((SRC/'prescribed-type-zero-volume-primary-read-20261004.json').read_text())['primary_units']
records=[]; sections=[]
for i,u in enumerate(primary,1):
 p=Path(u['source_text']); whole=p.read_bytes(); lines=whole.decode().split('\n')
 raw='\n'.join(lines[u['first_lf_line']-1:u['last_lf_line']]); body=u['body']
 r={'unit':i,'label':u['label'],'file':p.name,'first_LF':u['first_lf_line'],'last_LF':u['last_lf_line'],'supplied_range_sha256':u['raw_sha256'],'observed_range_sha256':sha(raw.encode()),'range_pin_matches':sha(raw.encode())==u['raw_sha256'],'whole_text_sha256':sha(whole),'whole_text_pin_matches':sha(whole)==u['source_text_sha256'],'literal_body_sha256':sha(body.encode()),'body_equals_range':body==raw,'body_equals_range_except_outer_LF':body.strip('\n')==raw.strip('\n'),'literal_body_present_in_original_assignment':body in a}
 assert r['range_pin_matches'] and r['whole_text_pin_matches'] and r['literal_body_present_in_original_assignment'] and r['body_equals_range_except_outer_LF']
 records.append(r)
 sections.append(f"## Source unit {i}: {u['label']}\n\n{p.name}, LF{r['first_LF']}--{r['last_LF']}. Independent range SHA256 `{r['observed_range_sha256']}`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.\n\n```text\n"+body+'\n```\n')
additional=json.loads((SRC/'prescribed-type-additional-primary-read-20261004.json').read_text())['units']
for u in additional:
 p=Path(u['source_provenance']['text_path']); whole=p.read_bytes(); lines=whole.decode().split('\n'); lo=u['first_LF_entry'];hi=u['last_LF_entry'];raw='\n'.join(lines[lo-1:hi]);body=u['literal_body']
 r={'unit':u['id'],'file':p.name,'first_LF':lo,'last_LF':hi,'supplied_range_sha256':u['literal_body_sha256'],'observed_range_sha256':sha(raw.encode()),'range_pin_matches':sha(raw.encode())==u['literal_body_sha256'],'body_equals_range':raw==body,'whole_text_sha256':sha(whole),'whole_text_pin_matches':sha(whole)==u['source_provenance']['text_sha256'],'pdf_sha256':sha(Path(u['source_provenance']['pdf_path']).read_bytes()),'pdf_pin_matches':sha(Path(u['source_provenance']['pdf_path']).read_bytes())==u['source_provenance']['pdf_sha256'],'literal_body_in_original_json_payload':json.dumps(body,ensure_ascii=False)[1:-1] in a}
 assert r['range_pin_matches'] and r['body_equals_range'] and r['whole_text_pin_matches'] and r['pdf_pin_matches']
 records.append(r);sections.append(f"## Additional source: {u['id']}\n\n{p.name}, LF{lo}--{hi}, independently checked SHA256 `{r['observed_range_sha256']}`. Authenticated supplied body reproduced literally, including OCR.\n\n```text\n"+body+'\n```\n')
extra=[('BEGZ-0812.3674v2-20261004.txt',180,248,'a9817dcf1e66414e9b0e6754baddfda52b4dd76cef4a5e046e4d5ad390a3252e'),('BEGZ-0812.3674v2-20261004.txt',323,477,'462891277734fc5ab0efef31d1a327cb2de16257bfdc3ec5f24424db0e67909f'),('BEGZ-0812.3674v2-20261004.txt',525,578,'0acf2b360d001a14d0fcf47f784424a599506386e6e44bc4b968ddd9bb80dc7d'),('DDNL18-2049-2087-20261004.txt',350,369,'0d34fd95c9beb603186a5ec408cb5b463d1bdda346042cdc66ac38b25fde6c71'),('Vu-2004.11111v1-20261004.txt',273,287,'1ba50d3f123db57547622b7cecbab561eb1cfbe4c81617a290f80b1ec41af8ad'),('Vu-2005.13241v3-20261004.txt',53,78,'f47dc8f2ccf80aa64ddf28d987eb8b2ee409d404a0d66a1cfcbced66fd1ed789')]
for f,lo,hi,pin in extra:
 whole=(SRC/f).read_bytes(); raw='\n'.join(whole.decode().split('\n')[lo-1:hi]);r={'file':f,'first_LF':lo,'last_LF':hi,'supplied_range_sha256':pin,'observed_range_sha256':sha(raw.encode()),'range_pin_matches':sha(raw.encode())==pin,'whole_text_sha256':sha(whole)};assert r['range_pin_matches'];records.append(r)
 sections.append(f'## Additional foundation: {f}, LF{lo}--{hi}\n\nIndependent SHA256 `{r["observed_range_sha256"]}`. Literal LF slice, without an added final LF in its digest.\n\n```text\n'+raw+'\n```\n')
# Preserve every supplied fenced text quotation in a separate exact archive as well.
quotes=re.findall(r'```text\n(.*?)\n```',a,re.S)
dump('supplied-quotation-archive.json',[{'index':i+1,'sha256':sha(t.encode()),'text':t} for i,t in enumerate(quotes)])
(ROOT/'source-annex.md').write_text('# Immutable primary-source annex\n\nThese bodies are mathematical source data. New proofs and corrected formulas are above. Historical review assertions are not grants; source bytes and statement applicability were checked independently. No source file is modified.\n\n'+'\n'.join(sections),encoding='utf-8')
dump('source-audit.json',{'input_sha256':sha(inp),'input_bytes':len(inp),'input_original_byte_identical':True,'decoded_assignment_identical':True,'task_values_identical':True,'range_pins_checked':len(records),'range_pins_matching':sum(r['range_pin_matches'] for r in records),'records':records,'supplied_fenced_quotes_preserved':len(quotes),'source_defects_preserved':['Vu v3 missing half factors on pages 6 and 11','Vu v1 closedness Cauchy--Schwarz and half-factor defects','Vu v1 Proposition 4.2 index/subscript defects','malformed extracted dd-c convention','GZ bounded Proposition 3.7 hypothesis'],'claim':'Byte checks and source audit are observations, not proof certification.'})
print(f"source pins: {len(records)}/{len(records)}; exact input preserved; {len(quotes)} supplied quotation strings archived")
