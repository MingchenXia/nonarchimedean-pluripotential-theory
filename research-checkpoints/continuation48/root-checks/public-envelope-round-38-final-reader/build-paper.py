#!/usr/bin/env python3
"""Make the standalone TeX paper from the complete Markdown argument.

Only headings and bold paragraph labels are translated. All mathematical
expressions in the argument already use TeX and are retained literally.
"""
from pathlib import Path
import re

source = Path("P03.3-argument.md").read_text()
lines = source.splitlines()
title = lines.pop(0).removeprefix("# ")
body = []
for line in lines:
    if line.startswith("## "):
        line = r"\section*{" + line[3:] + "}"
    line = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", line)
    # Never treat the usc-regularization stars in math as Markdown italics.
    if line.startswith("GR2:"):
        line = re.sub(r"\*([^*\n]+?)\*", r"\\emph{\1}", line)
    line = line.replace("finite_graph.py", r"finite\_graph.py")
    body.append(line)
header = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlength{\emergencystretch}{3em}
\title{TITLE}
\author{P03.3 implementation draft}
\date{4 October 2026}
\begin{document}
\maketitle
""".replace("TITLE", title)
Path("P03.3-paper.tex").write_text(header + "\n".join(body) + "\n\\end{document}\n")
print("Generated P03.3-paper.tex from the full P03.3-argument.md.")
