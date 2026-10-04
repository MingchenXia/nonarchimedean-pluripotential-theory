"""Build the standalone TeX source from the authoritative argument, without dependencies."""
from pathlib import Path
import re


def escape_prose(s):
    out = []
    pos = 0
    pattern = re.compile(r"\\\(.*?\\\)|`[^`]*`|\*\*[^*]*\*\*|(?<!\*)\*[^*]+\*(?!\*)")
    for m in pattern.finditer(s):
        out.append(escape_plain(s[pos:m.start()]))
        t = m.group()
        if t.startswith(r"\("):
            out.append(t)
        elif t.startswith("`"):
            out.append(r"\path{" + t[1:-1] + "}")
        elif t.startswith("**"):
            out.append(r"\textbf{" + escape_plain(t[2:-2]) + "}")
        else:
            out.append(r"\emph{" + escape_plain(t[1:-1]) + "}")
        pos = m.end()
    out.append(escape_plain(s[pos:]))
    return "".join(out)


def escape_plain(s):
    replacements = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}
    return "".join(replacements.get(c, c) for c in s)


text = Path("P03.1-argument.md").read_text()
header = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\title{A noninvariant toric envelope argument for P03.1\\
\large A conditional partial theorem, not a sharp classification}
\author{Unverified research draft}
\date{4 October 2026}
\begin{document}
\maketitle
"""
lines = []
display = False
for line in text.splitlines():
    if line.startswith("# "):
        continue
    if line == r"\[":
        display = True
        lines.append(line)
    elif line == r"\]":
        display = False
        lines.append(line)
    elif display:
        lines.append(line)
    elif line.startswith("## "):
        title = re.sub(r"^\d+\.\s*", "", line[3:])
        lines.append(r"\section{" + escape_prose(title) + "}")
    else:
        lines.append(escape_prose(line))
Path("P03.1-paper.tex").write_text(header + "\n".join(lines) + "\n\\end{document}\n")

