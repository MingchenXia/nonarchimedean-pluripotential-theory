#!/usr/bin/env python3
"""Owned, idempotent repair of two initial note files' inline math delimiters."""
from pathlib import Path

for name in ['n1.md', 'n2.md']:
    p = Path(name)
    s = p.read_text()
    # Subsequent reruns detect the already repaired start of the argument.
    if r'\(R\)' in s or r'\(k\)' in s:
        continue
    s = s.replace(r'D\)', 'D)')
    out, i, display = [], 0, False
    while i < len(s):
        if s.startswith(r'\[', i):
            display = True
        if s.startswith(r'\]', i):
            display = False
        if not display and s[i] == '(':
            j, depth = i + 1, 1
            while j < len(s) and depth:
                if s[j] == '(':
                    depth += 1
                elif s[j] == ')':
                    depth -= 1
                j += 1
            if depth:
                raise ValueError('Unbalanced inline parentheses')
            out.append(r'\(' + s[i + 1:j - 1] + r'\)')
            i = j
        else:
            out.append(s[i])
            i += 1
    p.write_text(''.join(out))
