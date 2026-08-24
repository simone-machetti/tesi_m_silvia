# -*- coding: utf-8 -*-
"""longtable -> flottante 'table' che non si spezza fra due pagine.
Le didascalie adiacenti entrano nel flottante, cosi' viaggiano con la tabella.
Nessuna parola viene aggiunta, tolta o spostata nella sequenza del testo."""
import re, sys

path  = sys.argv[1]
lines = open(path, encoding='utf-8').read().split('\n')
N     = len(lines)

CAP   = re.compile(r'^\\(?:addcontentsline\{lot\}|textbf\{Tabella|emph\{Tabella|emph\{Nota\.)')
STYLE = re.compile(r'^\\(?:small|footnotesize|scriptsize|setlength\{\\tabcolsep\})')

def blank(i):     return 0 <= i < N and lines[i].strip() == ''
def txt(i):       return lines[i].strip() if 0 <= i < N else ''

# ---------------------------------------------------------------- 1. individua
tables = []            # (start, end, style, spec, body, cap_before, cap_after)
i = 0
while i < N:
    if txt(i) != r'\begin{center}':
        i += 1; continue
    j = i + 1
    style = []
    while j < N and STYLE.match(txt(j)):
        style.append(txt(j)); j += 1
    if j >= N or not txt(j).startswith(r'\begin{longtable}'):
        i += 1; continue
    spec = txt(j)[len(r'\begin{longtable}'):]
    body = []
    j += 1
    while j < N and txt(j) != r'\end{longtable}':
        if txt(j) != r'\endhead': body.append(lines[j])
        j += 1
    if j >= N: break
    j += 1
    if txt(j) != r'\end{center}':
        i += 1; continue
    end = j                      # ultima riga del blocco

    # didascalia che precede
    before, k = [], i - 1
    while blank(k): k -= 1
    while k >= 0 and CAP.match(txt(k)):
        before.insert(0, txt(k)); k -= 1
        while blank(k): k -= 1
    start = k + 1                # prima riga del blocco (didascalia compresa)

    # didascalia/nota che seguono
    after, k = [], end + 1
    while True:
        kk = k
        while blank(kk): kk += 1
        if kk < N and CAP.match(txt(kk)):
            after.append(txt(kk)); k = kk + 1
        else:
            break
    end = k - 1
    tables.append((start, end, style, spec, body, before, after))
    i = k

# ---------------------------------------------------------------- 2. riscrive
out, i, ti = [], 0, 0
while i < N:
    if ti < len(tables) and i == tables[ti][0]:
        _, end, style, spec, body, before, after = tables[ti]
        while out and out[-1].strip() == '': out.pop()
        out.append('')
        out.append(r'\begin{table}[htbp]')
        out.append(r'\centering')
        if before:
            out.append(r'\begin{minipage}{\textwidth}\justifying')
            out.extend(before)
            out.append(r'\end{minipage}')
            out.append(r'\par\medskip')
        if style: out.append('{' + ' '.join(style))
        out.append(r'\begin{tabular}' + spec)
        out.extend(body)
        out.append(r'\end{tabular}')
        if style: out.append('}')
        if after:
            out.append(r'\par\medskip')
            out.append(r'\begin{minipage}{\textwidth}\justifying')
            out.extend(after)
            out.append(r'\end{minipage}')
        out.append(r'\end{table}')
        out.append('')
        i = end + 1; ti += 1; continue
    out.append(lines[i]); i += 1

res = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
# --- barriere: la tabella non esce dal caso o dalla sezione che la descrive
res = re.sub(r'(?m)^([ \t]*)(\\subsubsection\*\{Caso )', r'\\FloatBarrier\n\n\1\2', res)
res = re.sub(r'(?m)^([ \t]*)(\\subsection\{)',           r'\\FloatBarrier\n\n\1\2', res)
res = res.rstrip() + '\n\n\\FloatBarrier\n'
open(path, 'w', encoding='utf-8').write(res)
print('tabelle convertite:', len(tables))
