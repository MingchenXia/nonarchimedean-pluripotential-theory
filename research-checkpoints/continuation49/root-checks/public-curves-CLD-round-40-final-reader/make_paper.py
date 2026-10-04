#!/usr/bin/env python3
"""Produce a standalone TeX article embedding the complete fresh Markdown proof."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / "P03.3-argument.md").read_text()
FORMULAS = {
    "E_X(f) = {h : X -> R : h <= f, and h is locally Fubini–Study or semipositive real PL},": r"\mathcal E_X(f)=\{h:X\to\mathbb R:\ h\le f,\ h\text{ is LFS or semipositive real PL}\},",
    "P_X(f) = sup E_X(f).": r"P_X(f)=\sup_{h\in\mathcal E_X(f)}h.",
    "0 <= P_X(f) - b_n <= 2/n everywhere on X.": r"0\le P_X(f)-b_n\le 2/n\quad\text{everywhere on }X.",
    "P_{X_F}(f o pi) = P_X(f) o pi.": r"P_{X_F}(f\circ\pi_{F/K})=P_X(f)\circ\pi_{F/K}.",
    "g(x) = min {f(y) : y in p^{-1}(x)}.": r"g(x)=\min_{y\in p^{-1}(x)} f(y).",
    "P_Y(f) = P_X(g) o p.": r"P_Y(f)=P_X(g)\circ p.",
    "sum_{e out of v} w(e) partial_e A >= 0": r"\sum_{e\text{ out of }v}w(e)\,\partial_e A\ge0",
    "-log||1|| = T_i o tau.": r"-\log\|1\|_{\mathcal O(D_i)}=T_i\circ\tau.",
    "A o tau = A(v) + sum_i s_i (T_i o tau)": r"A\circ\tau=A(v)+\sum_i s_i(T_i\circ\tau)",
    "D a(v) = sum_{vw} [w(vw)/length(vw)] (a(w)-a(v)).": r"D a(v)=\sum_{vw}\frac{w(vw)}{\ell(vw)}\bigl(a(w)-a(v)\bigr).",
    "S={v : u(v)=G(v)}.": r"S=\{v:u(v)=G(v)\}.",
    "P_Z(g)=H.": r"P_Z(g)=H.",
    "P_{Z_E}(g o pi)=H o pi.": r"P_{Z_E}(g\circ\pi_{E/K})=H\circ\pi_{E/K}.",
    "b_epsilon o pi_L = A-epsilon.": r"b_\epsilon\circ\pi_{L/K}=A-\epsilon.",
    "b_epsilon <= P_X(f) <= b_epsilon+2epsilon.": r"b_\epsilon\le P_X(f)\le b_\epsilon+2\epsilon.",
    "h_F o pi_{E/F} <= (A+epsilon) o pi_{E/L}.": r"h_F\circ\pi_{E/F}\le(A+\epsilon)\circ\pi_{E/L}.",
    "h_F <= b_epsilon o pi_F+2epsilon.": r"h_F\le b_\epsilon\circ\pi_{F/K}+2\epsilon.",
    "b_epsilon o pi_F <= P_{X_F}(f o pi_F) <= b_epsilon o pi_F+2epsilon.": r"b_\epsilon\circ\pi_{F/K}\le P_{X_F}(f\circ\pi_{F/K})\le b_\epsilon\circ\pi_{F/K}+2\epsilon.",
    "X=M(K<x,y>/(xy)).": r"X=\mathcal M\bigl(K\langle x,y\rangle/(xy)\bigr).",
    "f(y)=-a min(|y|,1)=-a|y|": r"f(y)=-a\min\{|y|,1\}=-a|y|",
    "q_n=log max(|alpha|^n,|x|),   h_n=(a/(nA)) q_n.": r"q_n=\log\max\{|\alpha|^n,|x|\},\qquad h_n=\frac{a}{nA}q_n.",
    "P_X(f)=0 on D_x minus {o}, and -a on D_y.": r"P_X(f)=\begin{cases}0&\text{on }D_x\setminus\{o\},\\-a&\text{on }D_y.\end{cases}",
}

def escape(text):
    replacements = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
                    "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
                    "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(c, c) for c in text)

def rich(text):
    parts = re.split(r"(\*\*.*?\*\*)", text)
    return "".join(r"\textbf{" + escape(p[2:-2]) + "}" if p.startswith("**")
                   else escape(p) for p in parts)

header = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\hypersetup{colorlinks=true,urlcolor=blue,linkcolor=blue}
\setlength{\emergencystretch}{4em}
\title{P03.3: Full Curve Envelopes and Actual Projective Factors}
\author{Fresh mathematical draft}
\date{4 October 2026}
\begin{document}
\maketitle
"""
body = []
for chunk in re.split(r"\n\s*\n", source.strip()):
    if chunk.startswith("# "):
        continue
    if chunk.startswith("## "):
        title = re.sub(r"^\d+\.\s*", "", chunk[3:])
        body.append(r"\section{" + escape(title) + "}")
    elif chunk in FORMULAS:
        body.append("\\[\n" + FORMULAS[chunk] + "\n\\]")
    elif re.match(r"^\d+\. ", chunk):
        items = re.split(r"\n(?=\d+\. )", chunk)
        body.append("\\begin{enumerate}\n" + "\n".join(
            r"\item " + rich(re.sub(r"^\d+\. ", "", item)) for item in items
        ) + "\n\\end{enumerate}")
    else:
        body.append(rich(chunk.replace("\n", " ")))
tex = header + "\n\n".join(body) + "\n\\end{document}\n"
(ROOT / "P03.3-paper.tex").write_text(tex)
print(f"Standalone paper embeds {len(source.split())} words of Markdown argument in {len(tex)} TeX characters.")
