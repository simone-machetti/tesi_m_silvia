#!/bin/bash
# Ricostruisce gli ausiliari LaTeX da cui mkdocx.py prende numeri e bibliografia.
set -e
cd /home/simone/Downloads/tesi_m_silvia/tesi

cat > estratto_cap4.tex <<'TEX'
\documentclass[a4paper,12pt,fleqn]{book}
\PassOptionsToPackage{x11names,dvipsnames}{xcolor}
\input{settings/template.tex}
\input{settings/custom.tex}
\begin{document}
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}
\setcounter{chapter}{3}
\setlength{\parskip}{1em}
\mainmatter
\setcounter{chapter}{3}
\input{main/4_capitolo_4}
\backmatter
\input{tail/biblio}
\end{document}
TEX
latexmk -pdf -interaction=nonstopmode estratto_cap4.tex > /dev/null 2>&1
echo "estratto compilato"
