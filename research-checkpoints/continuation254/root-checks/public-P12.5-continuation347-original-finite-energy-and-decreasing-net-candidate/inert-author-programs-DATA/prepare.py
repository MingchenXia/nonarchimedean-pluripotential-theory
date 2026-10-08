"""Fresh data-only retention helper. Does not import or execute supplied code."""
import hashlib, json, pathlib, platform, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent
CAMPAIGN = ROOT.parent.parent
records = []
for kind, manifest_name in [('mathematical','mathematical-packet-bindings.json'), ('primary','private-primary-packet-bindings.json')]:
    manifest_path = CAMPAIGN / manifest_name
    raw = manifest_path.read_bytes()
    dest = ROOT / 'inputs' / manifest_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    for i, record in enumerate(json.loads(raw)):
        src = pathlib.Path(record['path'])
        body = src.read_bytes()
        digest = hashlib.sha256(body).hexdigest()
        assert digest == record['sha256'], str(src)
        assert len(body) == record['bytes'], str(src)
        local = ROOT / 'inputs' / kind / src.name
        local.parent.mkdir(parents=True, exist_ok=True)
        assert not local.exists() or local.read_bytes() == body
        local.write_bytes(body)
        records.append(dict(record, local=str(local.relative_to(ROOT)), actual_bytes=len(body), actual_sha256=digest))
task = json.loads((ROOT/'input.json').read_text())
problem, separator, augmented = task['task']['problem'].partition('ROOT AUTHORIZED WHOLE ORIGINAL RECONSTRUCTION')
assert separator
(ROOT/'original-problem.txt').write_text(problem)
(ROOT/'augmented-assignment.txt').write_text(separator+augmented+'\n\n'+task['assignment'])
(ROOT/'original-task.json').write_text(json.dumps({'problem':problem}, ensure_ascii=False, indent=2)+'\n')
(ROOT/'task-with-augmented-assignment.json').write_text(json.dumps(task['task'], ensure_ascii=False, indent=2)+'\n')
reports=ROOT/'reports'; reports.mkdir(exist_ok=True)
(reports/'input-hashes.json').write_text(json.dumps(records, indent=2)+'\n')
(reports/'environment.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'python':sys.version, 'platform':platform.platform(), 'cwd':str(ROOT), 'tools':'Own Python standard library only; no supplied executables; no agent or heavy compute.', 'compute_facility':'No operator supervised compute supplied; no resource-heavy computation required.'},indent=2)+'\n')
print(json.dumps({'retained':len(records),'mathematical':sum('/mathematical/' in r['local'] for r in records),'primary':sum('/primary/' in r['local'] for r in records),'all_bound_hashes_and_sizes_match':True}))
