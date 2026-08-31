# -*- coding: utf-8 -*-
"""Costruisce un .tex autoconsistente col solo capitolo 4, pronto per pandoc -> docx.

I numeri (sezioni, tabelle, citazioni) vengono presi dall'estratto compilato e
scritti in chiaro, perche' Word non li genera da solo.
"""
import re, json, subprocess, sys

TESI = '/home/simone/Downloads/tesi_m_silvia/tesi/'
aux  = open(TESI + 'estratto_cap4.aux', encoding='utf-8').read()

sec_num = dict(re.findall(r'\\newlabel\{(sec:[^}]*)\}\{\{([\d.]+)\}', aux))
tab_num = dict(re.findall(r'\\newlabel\{(tab:[^}]*)\}\{\{([\d.]+)\}', aux))
order, seen = [], set()
for k in re.findall(r'\\abx@aux@cite\{0\}\{([^}]*)\}', aux):
    if k not in seen: seen.add(k); order.append(k)
cite_num = {k: i for i, k in enumerate(order, start=1)}

s = open(TESI + 'main/4_capitolo_4.tex', encoding='utf-8').read()

# --- citazioni: \cite{a,b} -> [1], [2]
def cites(m):
    ns = sorted(cite_num[k.strip()] for k in m.group(1).split(','))
    return '[' + '], ['.join(str(n) for n in ns) + ']'
s = re.sub(r'~?\\cite\{([^}]*)\}', cites, s)

# --- rimandi alle tabelle
s = re.sub(r'~?\\ref\{(tab:[^}]*)\}', lambda m: ' ' + tab_num[m.group(1)], s)

# --- numeri di sezione scritti in chiaro nel titolo
def numbered(m):
    cmd, title, lab = m.group(1), m.group(2), m.group(3)
    n = sec_num.get(lab)
    return '\\%s{%s %s}' % (cmd, n, title) if n else '\\%s{%s}' % (cmd, title)
s = re.sub(r'\\(section|subsection|subsubsection)\{((?:[^{}]|\{[^{}]*\})*)\}\s*\n\s*\\label\{(sec:[^}]*)\}',
           numbered, s)

# --- didascalie: numero in chiaro, l'argomento breve non serve a Word
def caption(m):
    full, lab = m.group(2), m.group(3)
    return '\\caption{Tabella %s: %s}' % (tab_num[lab], ' '.join(full.split()))
s = re.sub(r'\\caption(\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}\s*\n\\label\{(tab:[^}]*)\}',
           caption, s)

# --- impalcature che a Word non servono
s = re.sub(r'\\FloatBarrier\s*', '', s)
s = re.sub(r'\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}\s*', '', s)
s = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}\s*', '', s)
s = re.sub(r'\\label\{[^}]*\}\s*', '', s)
s = re.sub(r'\\begin\{table\}\[[^\]]*\]', r'\\begin{table}', s)
s = re.sub(r'\\centering\s*', '', s)
s = re.sub(r'\\par\\medskip\s*', '\n\n', s)
s = re.sub(r'\\begin\{minipage\}\{\\textwidth\}\\justifying\s*', '', s)
s = re.sub(r'\\end\{minipage\}\s*', '\n\n', s)
s = re.sub(r'\{\\small \\setlength\{\\tabcolsep\}\{\d+pt\}\s*', '', s)
s = re.sub(r'\n\}\n', '\n', s)
s = s.replace('\\subsubsection*{', '\\subsubsection{').replace('\\paragraph*{', '\\paragraph{')
s = re.sub(r'>\{[^{}]*\}', '', s)        # modificatori di colonna: Word non li usa

# --- larghezze di colonna: senza queste Word dimensiona sul contenuto e la tabella
#     sfora il margine. Ogni riga di colonne viene riscritta in p{} che sommano a 14.6 cm.
LARGHEZZE = {
    '|l|c|c|l|l|l|l|l|':  [1.7, 1.5, 1.5, 1.9, 2.2, 1.9, 2.2, 1.7],   # 4.1 fattori di rischio
    '|l|l|':              [4.3, 10.3],                                # schede di sintesi
    '|l|c|l|':            [8.0, 2.4, 4.2],                            # prove e osservazioni
    '|l|l|l|l|l|':        [2.4, 2.4, 3.4, 2.8, 3.6],                  # 4.25 prestazioni
    '|l|c|c|c|c|':        [5.4, 2.3, 2.3, 2.3, 2.3],                  # 4.26 EEFQ
}
LARG_PER_TABELLA = []
def colonne(m):
    spec = m.group(1)
    base = re.sub(r'p\{[\d.]+cm\}', 'l', spec)
    w = LARGHEZZE.get(base)
    if not w:
        sys.exit('larghezze non definite per lo schema di colonne: ' + base)
    LARG_PER_TABELLA.append(w)
    return '\\begin{tabular}{|' + '|'.join('p{%scm}' % x for x in w) + '|}'
s = re.sub(r'\\begin\{tabular\}\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', colonne, s)

# --- titolo del capitolo
s = s.replace('\\chapter{', '\\chapter{Capitolo 4 --- ', 1)

# --- bibliografia dall'estratto compilato
bib = subprocess.run(['pdftotext','-layout', TESI + 'biblio_flat.pdf','-'],
                     capture_output=True, text=True).stdout
voci = []
for line in bib.split('\n'):
    m = re.match(r'\s*\[(\d+)\]\s+(.*\S)\s*$', line)
    if m: voci.append((int(m.group(1)), ' '.join(m.group(2).split())))
voci.sort()
if len(voci) != len(cite_num):
    sys.exit('voci bibliografia %d, citazioni %d' % (len(voci), len(cite_num)))

def esc(t):
    return t.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#').replace('_', r'\_')

biblio = ['\\chapter*{Bibliografia}', '']
for n, t in voci:
    biblio.append('[%d] %s' % (n, esc(t)))
    biblio.append('')

doc = r'''\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[italian]{babel}
\usepackage{booktabs}
\usepackage{graphicx}
\begin{document}
''' + s + '\n\n' + '\n'.join(biblio) + '\n\\end{document}\n'

open('/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad/cap4_docx.tex','w',encoding='utf-8').write(doc)
json.dump(LARG_PER_TABELLA, open('/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad/larghezze.json','w'))
print('sezioni numerate:', len(sec_num), '| tabelle:', len(tab_num), '| citazioni:', len(cite_num))
print('tabelle con larghezze assegnate:', len(LARG_PER_TABELLA))
print('voci di bibliografia:', len(voci))
