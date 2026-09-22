#!/usr/bin/env python3
r"""Check the actual TeX input closure of the monograph.

Run from manuscript/: python3 editorial/tools/refcheck.py
Missing inputs, duplicate labels, dangling references, and structural
defects return a nonzero exit status. Commented TeX is not part of the build.
"""
import os
import re
from collections import Counter

PAT = re.compile(r'\\(?:input|include|draftinclude)\{([^}]*)\}')


def uncommented(text):
    lines = []
    for line in text.splitlines(keepends=True):
        for index, char in enumerate(line):
            if char != '%':
                continue
            cursor = index - 1
            while cursor >= 0 and line[cursor] == '\\':
                cursor -= 1
            if (index - cursor - 1) % 2 == 0:
                line = line[:index] + ('\n' if line.endswith('\n') else '')
                break
        lines.append(line)
    return ''.join(lines)


def read(path):
    for candidate in (path, path + '.tex'):
        if os.path.isfile(candidate):
            candidate = os.path.normpath(candidate)
            with open(candidate, encoding='utf-8') as stream:
                return candidate, stream.read()
    return None, None


def scan_closure(root='book.tex'):
    files, missing, visited = [], [], set()
    stack = [(None, root)]
    while stack:
        parent, requested = stack.pop()
        filename, source = read(requested)
        if filename is None:
            missing.append((parent, requested))
            continue
        if filename in visited:
            continue
        visited.add(filename)
        files.append(filename)
        for child in PAT.findall(uncommented(source)):
            child = child.strip()
            # The definition of \draftinclude contains a literal #1 argument.
            if not child.startswith('#'):
                stack.append((filename, child))
    return files, missing


def closure(root='book.tex'):
    files, missing = scan_closure(root)
    if missing:
        raise FileNotFoundError('Missing TeX inputs: ' + ', '.join(p for _, p in missing))
    return files


def refs_used(source):
    groups = re.findall(
        r'\\(?:[cC]ref|ref|eqref|pageref|autoref)\*?\{([^}]*)\}',
        uncommented(source),
    )
    return {label.strip() for group in groups for label in group.split(',')}


def main():
    files, missing = scan_closure()
    sources = {filename: uncommented(read(filename)[1]) for filename in files}
    labels, source_of = Counter(), {}
    for filename, source in sources.items():
        for label in re.findall(r'\\label\{([^}]*)\}', source):
            labels[label] += 1
            source_of.setdefault(label, []).append(filename)
    duplicates = sorted(label for label, count in labels.items() if count > 1)
    print('files in build closure: %d' % len(files))
    print('missing inputs:        %d' % len(missing))
    for parent, requested in missing:
        print('MISSING %s -> %s' % (parent or '<root>', requested))
    print('labels in closure:      %d' % len(labels))
    print('multiply defined:      %d' % len(duplicates))
    for label in duplicates:
        print('    %s -> %s' % (label, source_of[label]))

    dangling = 0
    for filename, source in sources.items():
        absent = sorted(refs_used(source) - set(labels))
        if absent:
            dangling += len(absent)
            print('DANGLING %s: %s' % (filename, absent))
    print('dangling references:    %d' % dangling)

    print('--- per-file structure ---')
    issues = 0
    for filename, source in sources.items():
        opened = Counter(re.findall(r'\\begin\{([a-zA-Z*]+)\}', source))
        closed = Counter(re.findall(r'\\end\{([a-zA-Z*]+)\}', source))
        environments = dict(opened - closed) or dict(closed - opened)
        unescaped = re.sub(r'\\[{}]', '', source)
        braces = unescaped.count('{') - unescaped.count('}')
        tags = re.findall(r'\\tag\{\d+\.(\d+[A-Za-z]?)\}', source)
        bases = [int(re.match(r'\d+', tag).group()) for tag in tags]
        bad_tags = bool(tags) and (bases != sorted(bases) or len(tags) != len(set(tags)))
        if environments or braces or bad_tags:
            issues += 1
            print('%s: env=%s braces=%d tags=%s' % (
                filename, environments or 'ok', braces, tags if bad_tags else 'ok'))
    if not issues:
        print('all clean')
    return int(bool(missing or duplicates or dangling or issues))


if __name__ == '__main__':
    raise SystemExit(main())
