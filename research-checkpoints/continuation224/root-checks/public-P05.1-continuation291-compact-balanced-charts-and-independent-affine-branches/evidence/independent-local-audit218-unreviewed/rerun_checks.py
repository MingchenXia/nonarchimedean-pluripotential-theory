"""Own bounded audit reproduction. Never executes supplied orchestration/emitter code.

Default: read only the three bound manifests and their paths, compare bytes/JSON.
--reproduce: copy the inspected checker/input and unchanged TeX into a NEW own
subdirectory, run bounded Fraction checks, two no-shell-escape builds and pandoc.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, platform, re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent.parent
MANIFESTS = ['mathematical-packet-bindings', 'historical-own-evidence-bindings',
             'private-primary-packet-bindings']

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reproduce', action='store_true')
    args = ap.parse_args()
    bindings = {name: json.loads((BASE / (name + '.json')).read_text()) for name in MANIFESTS}
    rows = []
    for group, entries in bindings.items():
        for i, entry in enumerate(entries):
            raw = Path(entry['path']).read_bytes()
            rows.append(dict(group=group, index=i, label=entry['label'], path=entry['path'],
                             sha256=digest(raw), expected_sha256=entry['sha256'],
                             matches=digest(raw) == entry['sha256'] and len(raw) == entry['bytes'],
                             bytes=len(raw), LF_lines=raw.count(b'\n'), grant=entry.get('grant', False)))
    assert len(rows) == 115 and all(row['matches'] for row in rows)
    write(ROOT / 'frozen-file-bindings.json', rows)
    m, h = bindings[MANIFESTS[0]], bindings[MANIFESTS[1]]
    def raw(group, i):
        return Path(group[i]['path']).read_bytes()
    final = json.loads(raw(m, 37))
    saved = json.loads(raw(h, 38))
    reg = json.loads(raw(h, 50))
    regnotes = reg['notes']
    assert len(final['notes']) == len(saved['notes']) == len(regnotes) == 6
    assert final['candidate'] is False and saved['candidate'] is False
    suffixes = []
    for a, b, c in zip(final['notes'], saved['notes'], regnotes):
        assert a.keys() == b.keys() == c.keys()
        assert all(a[k] == b[k] == c[k] for k in a if k != 'text')
        assert b['text'] == a['text'] + '\n'
        assert c['text'].startswith(a['text'] + '\n\nArtifacts: ')
        suffixes.append(c['text'][len(a['text']):])
    assert len(set(suffixes)) == 1
    comparisons = dict(
        actual_FINAL_equals_ROOT_bytes=raw(m,37) == raw(h,49),
        saved_each_text_adds_exactly_one_terminal_newline=True,
        all_remaining_note_fields_equal=True,
        actual_and_saved_text_bytes_equal=[a['text']==b['text'] for a,b in zip(final['notes'],saved['notes'])],
        registered_suffix=suffixes[0],
        registered_is_actual_FINAL=False,
        parent_child_semantic_equal=json.loads(raw(h,20))==json.loads(raw(h,69)),
        parent_child_bytes_equal=raw(h,20)==raw(h,69),
        source_author_ROOT_math_bytes_equal=raw(h,4)==raw(h,55)==raw(m,33),
        checker_author_ROOT_own_bytes_equal=raw(h,10)==raw(h,65)==(ROOT/'code/exact_checks.py').read_bytes(),
        inputs_author_ROOT_own_bytes_equal=raw(h,21)==raw(h,58)==(ROOT/'inputs/exact-checks.json').read_bytes(),
        arithmetic_author_ROOT_own_bytes_equal=raw(h,18)==raw(h,64)==(ROOT/'evidence/exact-checks-output.json').read_bytes(),
        source_own_unchanged=(ROOT/'build/P05.1-paper.tex').read_bytes()==raw(m,33),
        own_markdown_bytes_equal=(ROOT/'build/argument.md').read_bytes()==raw(m,34))
    assert comparisons['actual_FINAL_equals_ROOT_bytes']
    assert comparisons['parent_child_semantic_equal'] and not comparisons['parent_child_bytes_equal']
    assert all(comparisons[k] for k in ['source_author_ROOT_math_bytes_equal','checker_author_ROOT_own_bytes_equal',
                                      'inputs_author_ROOT_own_bytes_equal','arithmetic_author_ROOT_own_bytes_equal',
                                      'source_own_unchanged','own_markdown_bytes_equal'])
    initial, current = json.loads(raw(h,17)), json.loads(raw(h,18))
    differences = {k: [initial.get(k),current.get(k)] for k in initial.keys()|current.keys()
                   if initial.get(k)!=current.get(k)}
    comparisons['initial_final_parsed_output_differences'] = differences
    artifact_manifest=json.loads(raw(h,47))
    own_author_files={str(Path(e['path']).relative_to(BASE/'immutable-own-historical-evidence/author216')):e
                      for e in h[:47]}
    checked=[]; unavailable=[]
    for e in artifact_manifest['files']:
        if e['local_only']:
            unavailable.append(e['filename'])
            continue
        actual_entry=own_author_files[e['filename']]
        assert e['sha256']==actual_entry['sha256'] and e['bytes']==actual_entry['bytes']
        checked.append(e['filename'])
    assert len(checked)==47 and len(unavailable)==2
    comparisons['author_artifact_manifest_nonLOCALONLY_verified']=47
    comparisons['author_artifact_manifest_LOCALONLY_unbound']=unavailable
    comparisons['ROOT_49_verification_flag_independently_fully_reproduced']=False
    write(ROOT/'evidence/note-input-comparison.json', comparisons)
    if args.reproduce:
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        dest = ROOT / ('rerun-' + stamp)
        dest.mkdir()
        for dirname in ['code','inputs','evidence','logs','build']:
            (dest/dirname).mkdir()
        shutil.copyfile(ROOT/'code/exact_checks.py',dest/'code/exact_checks.py')
        shutil.copyfile(ROOT/'inputs/exact-checks.json',dest/'inputs/exact-checks.json')
        source = raw(m,33)
        assert not re.search(rb'\\(?:input|include|write18|openin|openout)\b', source)
        (dest/'build/P05.1-paper.tex').write_bytes(source)
        commands=[]
        def run(argv, cwd, log):
            proc=subprocess.run(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (dest/log).write_text(proc.stdout)
            commands.append(dict(argv=argv,cwd=str(cwd.relative_to(ROOT)),exit_code=proc.returncode,log=log))
            assert proc.returncode==0
        run([sys.executable,'code/exact_checks.py'],dest,'logs/exact-checks.log')
        assert (dest/'evidence/exact-checks-output.json').read_bytes()==raw(h,18)
        for i in [1,2]:
            run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex'],
                dest/'build',f'logs/build-pass-{i}.log')
        run(['pandoc','-f','latex','-t','gfm','--wrap=none','P05.1-paper.tex','-o','argument.md'],
            dest/'build','logs/pandoc.log')
        assert (dest/'build/P05.1-paper.tex').read_bytes()==source
        assert (dest/'build/argument.md').read_bytes()==raw(m,34)
        write(dest/'reproduction-report.json',dict(commands=commands,source_sha256=digest(source),
                                                  output_assertions=1945,mathematical_certification=False))
        print(json.dumps(dict(reproduction_directory=str(dest.relative_to(ROOT)),exit_codes=[0,0,0,0])))
    print(json.dumps(dict(bound_files=115,hash_matches=True,comparison_checks=True,candidate=False)))

if __name__ == '__main__':
    main()
