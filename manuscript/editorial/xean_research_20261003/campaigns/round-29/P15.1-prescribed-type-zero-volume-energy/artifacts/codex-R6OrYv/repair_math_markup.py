#!/usr/bin/env python3
"""One-time correction of missing inline-math opening delimiters in authored notes."""
from pathlib import Path
import re

for path in sorted(Path('.').glob('n*-*.md')):
    text = path.read_text()
    fixed = []
    display = False
    for line in text.splitlines(keepends=True):
        if line.strip() == r'\[':
            display = True
            fixed.append(line)
            continue
        if display:
            fixed.append(line)
            if line.strip() == r'\]':
                display = False
            continue
        stack = []
        insert = set()
        for i, ch in enumerate(line):
            if ch == '(':
                stack.append(i)
            elif ch == ')' and stack:
                start = stack.pop()
                end_escaped = i > 0 and line[i-1] == '\\'
                start_escaped = start > 0 and line[start-1] == '\\'
                if end_escaped and not start_escaped:
                    insert.add(start)
                elif not stack and not start_escaped and not end_escaped:
                    content = line[start+1:i]
                    math = bool(re.search(r'\\[A-Za-z]|[_^]', content))
                    math = math or content in {'X','n','d','r','q','R','W','S','P','M','L','B','A','a','b','c','u','v','w','k','j','m','t','h_i','T_u','u/2','u,v','1,1','n-1,n-1','d,d','k,k','0','c,C>0'}
                    if math:
                        insert.add(start)
                        insert.add(i)
        line = ''.join(('\\' if i in insert else '')+ch for i, ch in enumerate(line))
        fixed.append(line)
    result = ''.join(fixed)
    assert result.count(r'\(') == result.count(r'\)'), path
    path.write_text(result)
    print(path, result.count(r'\('), 'matched inline pairs')
