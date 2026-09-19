#!/usr/bin/env python3
r"""Cross-reference checker for the monograph.

Run from manuscript/:   python3 editorial/tools/refcheck.py

Resolves the ACTUAL input graph starting at book.tex, following \input,
\include and the book's own \draftinclude macro transitively.  This matters:
several chapters \input files under editorial/ (solver dossiers, rethlas
packets), so a checker that globs parts/+appendices/ alone reports hundreds
of false "dangling" references -- and one that globs editorial/** instead is
too permissive, since not every packet there is actually inputted.

Reports: build closure size, label count, multiply-defined labels, dangling
references, per-file environment balance, brace delta and \tag{} sequences.
"""
import re, io, os, sys
from collections import Counter

PAT = re.compile(r'\\(?:input|include|draftinclude)\{([^}]*)\}')

def read(p):
    for cand in (p, p + '.tex'):
        if os.path.isfile(cand):
            return cand, io.open(cand, encoding='utf-8', errors='replace').read()
    return None, None

def closure(root='book.tex'):
    seen, stack, visited = [], [root], set()
    while stack:
        f, s = read(stack.pop())
        if f is None or f in visited:
            continue
        visited.add(f); seen.append(f)
        stack.extend(m.strip() for m in PAT.findall(s) if not m.startswith('#'))
    return seen

def refs_used(s):
    used = set(re.findall(r'\\(?:C?ref|eqref)\{([^}]*)\}', s))
    multi = set()
    for u in list(used):
        if ',' in u:
            used.discard(u); multi |= {x.strip() for x in u.split(',')}
    return used | multi

def main():
    files = closure()
    labs, srcof = Counter(), {}
    for f in files:
        s = io.open(f, encoding='utf-8', errors='replace').read()
        for L in re.findall(r'\\label\{([^}]*)\}', s):
            labs[L] += 1; srcof.setdefault(L, []).append(f)
    dups = sorted(k for k, v in labs.items() if v > 1)
    print("files in build closure: %d" % len(files))
    print("labels in closure:      %d" % len(labs))
    print("multiply defined:       %d" % len(dups))
    for k in dups:
        print("    %s -> %s" % (k, [os.path.basename(x) for x in srcof[k]]))

    S = set(labs); dangling = 0
    for f in files:
        s = io.open(f, encoding='utf-8', errors='replace').read()
        miss = sorted(u for u in refs_used(s) if u not in S and '%' not in u)
        if miss:
            dangling += len(miss); print("DANGLING %s: %s" % (f, miss))
    print("dangling references:    %d" % dangling)

    print("--- per-file structure ---")
    issues = 0
    for f in files:
        s = io.open(f, encoding='utf-8', errors='replace').read()
        op = Counter(re.findall(r'\\begin\{([a-zA-Z*]+)\}', s))
        cl = Counter(re.findall(r'\\end\{([a-zA-Z*]+)\}', s))
        env = dict(op - cl) or dict(cl - op)
        t = re.sub(r'\\[{}]', '', s)
        br = t.count('{') - t.count('}')
        tags = [int(m) for m in re.findall(r'\\tag\{\d+\.(\d+)\}', s)]
        tagbad = bool(tags) and tags != list(range(1, len(tags) + 1))
        if env or br or tagbad:
            issues += 1
            print("%s: env=%s braces=%d tags=%s" %
                  (f, env or 'ok', br, tags if tagbad else 'ok'))
    if not issues:
        print("all clean")

if __name__ == '__main__':
    main()
