#!/usr/bin/env python3
"""
Verifica di fedelta' del capitolo 4: testo, celle delle tabelle e titoli.

Piu' complesso degli altri capitoli perche' il Word usa stili di titolo incoerenti
(alcuni paragrafi di testo sono formattati come "Titolo 3") e contiene 26 tabelle.
"""
import re, difflib

MD = '/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad/conv/capitolo_4.md'
TEX = '/home/simone/Downloads/tesi_m_silvia/tesi/main/4_capitolo_4.tex'
OUT = '/home/simone/Downloads/tesi_m_silvia/cap_4.md'
CIT = '\u27e6CIT\u27e7'

CITE_OK = {"Astle et al., 2021", "Astle et al., 2022", "Bayley, 2006",
           "Beauchaine & Cicchetti, 2019", "Blair & Raver, 2015", "Calkins, 2007",
           "Carlson, 2005", "Diamond, 2013", "Garon et al., 2008",
           "Hendry & Holmboe, 2021", "Hughes & Graham, 2002", "Kopp, 1982"}


def strip_md(s):
    s = re.sub(r'\\([\\`*_{}\[\]()#+\-.!"\'~<>])', r'\1', s)
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s, flags=re.S)
    s = re.sub(r'\*(.*?)\*', r'\1', s, flags=re.S)
    s = re.sub(r'\[(.*?)\]\{\.underline\}', r'\1', s, flags=re.S)
    return s


def mask_cites(s):
    def repl(m):
        inner = m.group(1)
        if re.fullmatch(r'\s*(?:19|20)\d{2}[a-z]?\s*', inner) or not re.search(r'[A-Z]', inner):
            return m.group(0)
        parts = [p.strip() for p in inner.split(';')]
        lits = [p for p in parts if not re.search(r'\b(?:19|20)\d{2}[a-z]?\b', p)]
        if lits and len(lits) < len(parts):
            return '(' + '; '.join(lits + [CIT]) + ')'
        return CIT
    return re.sub(r'\(([^()]*?\b(?:19|20)\d{2}[a-z]?)\)', repl, s)


def tokens(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '---').replace('\u2013', '--')
    s = s.replace('\u00a0', ' ').replace('\u00ad', '')
    return s.split()


# ------------------------------------------------------------------ titoli
def headings_md(md):
    lines = md.split('\n')
    out = []
    for i, line in enumerate(lines):
        s = line.strip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
        is_setext = bool(s) and bool(re.fullmatch(r'[=-]{3,}', nxt))
        s2 = re.sub(r'^#{1,6}\s*', '', s)
        is_atx = s.startswith('#')
        plain = strip_md(s2).strip()
        if not plain:
            continue
        m = re.fullmatch(r'(\d+(?:\.\d+)+)\s*(.*)', plain)
        if m and (is_atx or re.fullmatch(r'\*\*.*\*\*', s2) or is_setext):
            out.append((m.group(1), m.group(2).strip()))
        elif is_setext and not m:
            out.append(('—', plain))
    return out


def headings_tex(tex):
    """ricostruisce la numerazione che stampera' LaTeX, \setcounter compresi"""
    out = []
    c = {0: 4, 1: 0, 2: 0, 3: 0}          # 0 = capitolo (fisso), 1..3 = sez/sottosez/...
    for m in re.finditer(
            r'\\setcounter\{(section|subsection|subsubsection)\}\{(\d+)\}'
            r'|\\(section|subsection|subsubsection|paragraph)(\*?)\{([^{}]*)\}', tex):
        if m.group(1):
            c[{'section': 1, 'subsection': 2, 'subsubsection': 3}[m.group(1)]] = int(m.group(2))
            continue
        lvl = {'section': 1, 'subsection': 2, 'subsubsection': 3, 'paragraph': 4}[m.group(3)]
        star, title = m.group(4), m.group(5).strip()
        if star or lvl == 4:
            out.append(('\u2014', title))
            continue
        c[lvl] += 1
        for k in range(lvl + 1, 4):
            c[k] = 0
        out.append('.'.join(str(c[k]) for k in range(0, lvl + 1)))
        out[-1] = (out[-1], title)
    return out


# ------------------------------------------------------------------ testo
# Nel Word le legende di codifica e le tre didascalie stavano nel corpo del testo;
# ora sono dentro \caption, quindi vanno tolte anche dal lato Word per confrontare
# la sola prosa. Il testo integrale delle didascalie e' rivedibile in tabelle.md.
FUORI_CORPO = [
    r'Codifica: 0 = esecuzione non corretta.*?risposte alle singole prove\.',
    r'Compilato dalla somministratrice al termine della valutazione\. Tre livelli di '
    r'frequenza:.*?per la maggior parte del tempo\.',
    r'Tabella 4\.1 --- Profilo dei fattori di rischio.*?compilato dai genitori\)\.',
    r'Tabella 4\.2\. Prestazioni complessive al Baby-FE nei casi selezionati',
    r'Tabella 4\.3\. Punteggi alle sottoscale EEFQ nei casi selezionati e valori di '
    r'riferimento del campione totale dello studio',
]


def text_md(md):
    lines = md.split('\n')
    keep = []
    for i, line in enumerate(lines):
        s = line.rstrip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
        if re.fullmatch(r'[=-]{3,}', s.strip()):          # sottolineatura setext
            continue
        if re.fullmatch(r'\s*-{2,}(\s+-{2,})*\s*', s):    # riga separatrice di tabella
            continue
        if s.strip() and re.fullmatch(r'[=-]{3,}', nxt):  # titolo setext
            continue
        if re.fullmatch(r'#{1,6}\s*\*\*(\d+(?:\.\d+)+)\s*.*\*\*', s.strip()):
            continue
        if re.fullmatch(r'\*\*(\d+(?:\.\d+)+)\s*.*\*\*', s.strip()):
            continue
        if re.fullmatch(r'#{1,6}\s*', s.strip()):
            continue
        keep.append(s)
    s = '\n'.join(keep)
    s = re.sub(r'^\*\*CAPITOLO 4\*\*.*$', '', s, count=1, flags=re.M)
    s = re.sub(r'^#{1,6}\s*', '', s, flags=re.M)
    s = mask_cites(s)
    s = strip_md(s)
    s = s.replace('|', ' ')
    for r in FUORI_CORPO:
        s = re.sub(r, '', s, flags=re.S)
    return s


# Frasi di raccordo aggiunte per introdurre le tabelle (vedi tabelle.md): non sono
# testo del Word e vengono tolte dal confronto.
RACCORDI = [
    r'Il profilo del Caso \d+ .{1,2} riassunto nella Tabella~\\ref\{[^}]*\}\.',
    r'Le risposte del Caso \d+ alle singole prove sono riportate nella Tabella~\\ref\{[^}]*\}\.',
    r'Il comportamento osservato durante la valutazione del Caso \d+ .{1,2} riportato '
    r'nella Tabella~\\ref\{[^}]*\}\.',
]
# I rimandi gia' presenti nel Word: il numero letterale e' ora generato da \ref.
REF_NUM = {'tab:rischio': '4.1', 'tab:babyfe_totali': '4.2', 'tab:eefq': '4.3'}


def text_tex(tex):
    s = tex
    s = re.sub(r'^\s*%.*$', '', s, flags=re.M)
    for r in RACCORDI:
        s = re.sub(r, '', s)
    s = re.sub(r'\\caption(\[[^\]]*\])?\{(?:[^{}]|\{[^{}]*\})*\}', '', s)
    s = re.sub(r'\\ref\{(tab:[^}]*)\}', lambda m: REF_NUM.get(m.group(1), ''), s)
    s = re.sub(r'\\cite\{[^}]*\}', CIT, s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\setlength\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\(chapter|section|subsection|subsubsection|paragraph)\*?\{[^{}]*\}', '', s)
    s = re.sub(r'\\begin\{(longtable|tabular)\}\{[^{}]*(\{[^{}]*\}[^{}]*)*\}', '', s)
    s = re.sub(r'\\begin\{table\}(\[[^\]]*\])?', '', s)
    s = re.sub(r'\\begin\{minipage\}\{[^{}]*\}', '', s)
    for t in [r'\\end\{longtable\}', r'\\end\{tabular\}', r'\\end\{table\}',
              r'\\end\{minipage\}', r'\\begin\{center\}', r'\\end\{center\}',
              r'\\toprule', r'\\midrule', r'\\bottomrule', r'\\endhead',
              r'\\small', r'\\footnotesize', r'\\centering', r'\\justifying',
              r'\\FloatBarrier', r'\\par', r'\\medskip']:
        s = re.sub(t, '', s)
    s = re.sub(r'(?m)^\s*[{}]\s*$', '', s)      # graffe di raggruppamento dello stile tabella
    s = s.replace('\\\\', ' ').replace('&', ' ')
    for cmd in ['textbf', 'textit', 'emph', 'underline', 'texttt', 'textsc']:
        for _ in range(5):
            s = re.sub(r'\\%s\{([^{}]*)\}' % cmd, r'\1', s)
    s = s.replace('\\textless', '<').replace('\\textgreater', '>')
    for a, b in [('\\&', '&'), ('\\%', '%'), ('\\_', '_'), ('\\#', '#'),
                 ('\\$', '$'), ('\\{', '{'), ('\\}', '}'), ('~', ' ')]:
        s = s.replace(a, b)
    s = s.replace('\\textasciitilde', '~')   # dopo la tilde-spazio, non prima
    return s


def main():
    md = open(MD, encoding='utf-8').read()
    tex = open(TEX, encoding='utf-8').read()

    h_md, h_tex = headings_md(md), headings_tex(tex)
    a, b = text_md(md), text_tex(tex)
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    hunks = [(t, ' '.join(ta[i1:i2]), ' '.join(tb[j1:j2]), ' '.join(ta[max(0, i1 - 8):i1]))
             for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']

    ntab_md = len(re.findall(r'^\s*-{2,}\s+-{2,}', md, flags=re.M))
    ntab_tex = tex.count('\\begin{tabular}') + tex.count('\\begin{longtable}')
    ncit_a, ncit_b = a.count(CIT), b.count(CIT)

    L = ['# Capitolo 4 — verifica di fedelta\u0300\n']
    L.append('Confronto fra `source/capitolo_4.docx` e `tesi/main/4_capitolo_4.tex`.\n')
    L.append('Il testo dei due lati viene ridotto a parole — **contenuto delle celle delle '
             'tabelle compreso** — togliendo i titoli (confrontati a parte) e sostituendo '
             'ogni citazione con lo stesso segnaposto. **Se la migrazione e\u0300 fedele, la '
             'sezione "Differenze" e\u0300 vuota.**\n')

    L.append('## Titoli\n')
    same = len(h_md) == len(h_tex) and all(x[1] == y[1] and x[0] == y[0]
                                           for x, y in zip(h_md, h_tex))
    if same:
        L.append('%d titoli, tutti identici al Word, numerazione compresa. '
                 'I titoli senza numero nel Word (`Caso 1`…`Caso 8` e le loro tre '
                 'intestazioni interne) restano senza numero anche in LaTeX.\n' % len(h_md))
    else:
        L.append('**Attenzione: i titoli non coincidono.**\n')
    L.append('| Numero | Titolo nel LaTeX | Titolo nel Word | Confronto |')
    L.append('|---|---|---|---|')
    for i in range(max(len(h_md), len(h_tex))):
        x = h_md[i] if i < len(h_md) else ('—', '*assente*')
        y = h_tex[i] if i < len(h_tex) else ('—', '*assente*')
        ok = 'ok' if (x[0] == y[0] and x[1] == y[1]) else '**DIVERSO**'
        L.append('| %s | %s | %s | %s |' % (y[0], y[1], x[1], ok))
    L.append('')

    L.append('## Tabelle\n')
    L.append('- tabelle nel Word: **%d**' % ntab_md)
    L.append('- ambienti `longtable` nel LaTeX: **%d**\n' % ntab_tex)
    L.append('Il contenuto delle celle rientra nel confronto testuale qui sotto: se una '
             'cella fosse stata persa o alterata comparirebbe fra le differenze.\n')

    L.append('## Citazioni\n')
    L.append('- gruppi di citazione nel Word: **%d**' % ncit_a)
    L.append('- comandi `\\cite{}` nel LaTeX: **%d**\n' % ncit_b)

    L.append('## Differenze\n')
    if not hunks:
        L.append('**Nessuna differenza.** Testo e celle delle tabelle sono identici parola '
                 'per parola a quelli del Word.\n')
    else:
        L.append('%d differenze trovate.\n' % len(hunks))
        for t, av, bv, ctx in hunks:
            L.append('---\n')
            L.append('**contesto:** …%s\n' % ctx)
            L.append('- **Word:** `%s`' % (av if av else '(niente)'))
            L.append('- **LaTeX:** `%s`\n' % (bv if bv else '(niente)'))

    open(OUT, 'w', encoding='utf-8').write('\n'.join(L))
    print('titoli: %d Word / %d LaTeX (uguali: %s)' % (len(h_md), len(h_tex), same))
    print('tabelle: %d Word / %d LaTeX' % (ntab_md, ntab_tex))
    print('citazioni: %d Word / %d LaTeX' % (ncit_a, ncit_b))
    print('differenze: %d' % len(hunks))
    for t, av, bv, ctx in hunks[:25]:
        print('  [%s] W=%r  L=%r' % (t, av[:70], bv[:70]))


main()
