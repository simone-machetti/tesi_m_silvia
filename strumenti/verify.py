#!/usr/bin/env python3
"""
Confronta il testo del capitolo Word con quello del .tex generato e scrive cap_N.md.

Entrambi i lati vengono ridotti a testo semplice: via i titoli (confrontati a parte),
le citazioni sostituite dallo stesso segnaposto, la formattazione rimossa.
Se la migrazione e' fedele il diff finale e' vuoto.
"""
import re, sys, json, difflib

CIT = '\u27e6CIT\u27e7'


def unescape_tex(s):
    for a, b in [('\\&', '&'), ('\\%', '%'), ('\\_', '_'), ('\\#', '#'),
                 ('\\$', '$'), ('\\{', '{'), ('\\}', '}'), ('\\textasciitilde', '~'),
                 ('~', ' '), ('\\ldots', '...'), ('``', '"'), ("''", '"')]:
        s = s.replace(a, b)
    return s


def strip_md(s):
    """markdown di pandoc -> testo semplice"""
    s = re.sub(r'\\([\\`*_{}\[\]()#+\-.!"\'])', r'\1', s)
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s, flags=re.S)
    s = re.sub(r'\*(.*?)\*', r'\1', s, flags=re.S)
    s = re.sub(r'\[(.*?)\]\{\.underline\}', r'\1', s, flags=re.S)
    s = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', s, flags=re.S)
    return s


def strip_tex(s):
    """LaTeX generato -> testo semplice"""
    s = re.sub(r'\\cite\{[^}]*\}', CIT, s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    for cmd in ['textbf', 'textit', 'emph', 'underline', 'texttt', 'textsc']:
        for _ in range(4):
            s = re.sub(r'\\%s\{([^{}]*)\}' % cmd, r'\1', s)
    s = re.sub(r'\\(chapter|section|subsection|subsubsection|paragraph)\*?\{([^{}]*)\}',
               r'\n\2\n', s)
    s = re.sub(r'\\pagestyle\{[^}]*\}', '', s)
    s = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', s)
    return unescape_tex(s)


def mask_cites_md(s):
    """le stesse citazioni (Autore, anno) diventano il segnaposto"""
    def repl(m):
        inner = m.group(1)
        if re.fullmatch(r'\s*(?:19|20)\d{2}[a-z]?\s*', inner):
            return m.group(0)
        if not re.search(r'[A-Z]', inner):
            return m.group(0)
        # come nel convertitore: le parti senza anno (sigle di strumenti) restano
        parts = [p.strip() for p in inner.split(';')]
        lits = [p for p in parts if not re.search(r'\b(?:19|20)\d{2}[a-z]?\b', p)]
        if lits and len(lits) < len(parts):
            return '(' + '; '.join(lits + [CIT]) + ')'
        return CIT
    return re.sub(r'\(([^()]*?\b(?:19|20)\d{2}[a-z]?)\)', repl, s)


def mask_narrative_md(s, narrative):
    for phrase in narrative:
        base = phrase[:phrase.rindex('(')].rstrip()
        s = s.replace(phrase, base + ' ' + CIT)
    return s


def tokens(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '---').replace('\u2013', '--')
    s = s.replace('\u00a0', ' ')
    return s.split()


def headings_md(s):
    out = []
    for line in s.split('\n'):
        line = line.strip()
        line = re.sub(r'^#{1,6}\s*', '', line)
        m = re.fullmatch(r'\*\*(\d+(?:\.\d+)+)\s*(.*?)\*\*', line)
        if m:
            out.append((m.group(1), strip_md(m.group(2)).strip()))
    return out


def headings_tex(s, chapnum):
    out = []
    counters = [chapnum, 0, 0, 0]
    for m in re.finditer(r'\\(section|subsection|subsubsection)\{([^{}]*)\}', s):
        lvl = {'section': 1, 'subsection': 2, 'subsubsection': 3}[m.group(1)]
        counters[lvl] += 1
        for i in range(lvl + 1, 4):
            counters[i] = 0
        num = '.'.join(str(counters[i]) for i in range(lvl + 1))
        out.append((num, m.group(2).strip()))
    return out


def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    md = open(cfg['md'], encoding='utf-8').read()
    tex = open(cfg['tex'], encoding='utf-8').read()
    narrative = cfg.get('narrative', {})
    n = cfg['number']

    # ---- titoli
    h_md = headings_md(md)
    h_tex = headings_tex(tex, n)

    # ---- testo
    a = md
    a = re.sub(r'^\*\*[A-ZÀ-Ü][^\n]*\*\*\s*$', '', a, count=1, flags=re.M)  # titolo capitolo
    a = re.sub(r'^#{1,6}\s*', '', a, flags=re.M)
    a = re.sub(r'^\*\*(\d+(?:\.\d+)+)\s*(.*?)\*\*\s*$', '', a, flags=re.M)  # titoli sezione
    a = mask_narrative_md(a, narrative)
    a = mask_cites_md(a)
    a = strip_md(a)

    b = tex
    b = re.sub(r'\\chapter\{[^{}]*\}', '', b)
    b = re.sub(r'\\(section|subsection|subsubsection)\{[^{}]*\}', '', b)
    b = strip_tex(b)

    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)

    hunks = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        hunks.append((tag, ' '.join(ta[i1:i2]), ' '.join(tb[j1:j2]),
                      ' '.join(ta[max(0, i1 - 8):i1])))

    # ---- scrittura report
    L = []
    L.append('# Capitolo %d — verifica di fedelta\u0300\n' % n)
    L.append('Confronto fra `source/capitolo_%d.docx` e `tesi/main/%d_capitolo_%d.tex`.\n'
             % (n, n, n))
    L.append('Il testo dei due lati viene ridotto a parole, togliendo i titoli (confrontati '
             'a parte qui sotto) e sostituendo ogni citazione con lo stesso segnaposto. '
             '**Se la migrazione e\u0300 fedele, la sezione "Differenze" e\u0300 vuota.**\n')

    if cfg.get('note'):
        L.append('> **Nota.** %s\n' % cfg['note'])
    L.append('## Titoli\n')
    if len(h_md) == len(h_tex) and all(x[1] == y[1] for x, y in zip(h_md, h_tex)):
        L.append('%d titoli, tutti identici al Word (numerazione compresa).\n' % len(h_md))
        L.append('| Numero | Titolo | Comando |')
        L.append('|---|---|---|')
        lvl = {1: 'section', 2: 'subsection', 3: 'subsubsection'}
        for (num, txt) in h_tex:
            L.append('| %s | %s | `\\%s` |' % (num, txt, lvl[num.count('.')]))
    else:
        L.append('**Attenzione: i titoli non coincidono.**\n')
        L.append('| Word | LaTeX |')
        L.append('|---|---|')
        for x, y in zip(h_md, h_tex):
            mark = '' if x[1] == y[1] else ' **DIVERSO**'
            L.append('| %s %s | %s %s%s |' % (x[0], x[1], y[0], y[1], mark))
        for x in h_md[len(h_tex):]:
            L.append('| %s %s | *assente* |' % x)
        for y in h_tex[len(h_md):]:
            L.append('| *assente* | %s %s |' % y)
    L.append('')

    ncit_a = a.count(CIT)
    ncit_b = b.count(CIT)
    L.append('## Citazioni\n')
    L.append('- gruppi di citazione nel Word: **%d**' % ncit_a)
    L.append('- comandi `\\cite{}` nel LaTeX: **%d**' % ncit_b)
    L.append('- riferimenti totali richiamati: **%d**\n'
             % sum(len(m.group(1).split(',')) for m in re.finditer(r'\\cite\{([^}]*)\}', tex)))
    if ncit_a != ncit_b:
        L.append('**Attenzione: i due numeri non coincidono.**\n')
    else:
        L.append('I due numeri coincidono: ogni citazione del Word ha il suo `\\cite`.\n')

    L.append('## Differenze\n')
    if not hunks:
        L.append('**Nessuna differenza.** Il testo del capitolo e\u0300 identico parola per '
                 'parola a quello del Word.\n')
    else:
        L.append('%d differenze trovate.\n' % len(hunks))
        for tag, av, bv, ctx in hunks:
            L.append('---\n')
            L.append('**contesto:** …%s\n' % ctx)
            L.append('- **Word:** `%s`' % (av if av else '(niente)'))
            L.append('- **LaTeX:** `%s`\n' % (bv if bv else '(niente)'))

    open(cfg['out'], 'w', encoding='utf-8').write('\n'.join(L))
    print('titoli: %d Word / %d LaTeX' % (len(h_md), len(h_tex)))
    print('citazioni: %d Word / %d LaTeX' % (ncit_a, ncit_b))
    print('differenze di testo: %d' % len(hunks))
    for tag, av, bv, ctx in hunks[:20]:
        print('  [%s] Word=%r  LaTeX=%r' % (tag, av[:80], bv[:80]))


main()
