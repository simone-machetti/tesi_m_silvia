#!/usr/bin/env python3
"""
Convertitore dedicato al capitolo 4.

Il Word di questo capitolo usa gli stili di titolo in modo incoerente: alcuni
paragrafi di testo corrente sono formattati come "Titolo 3", i "Caso N" come
"Titolo 1". Qui la struttura viene ricostruita dalla numerazione visibile nel
testo, non dagli stili Word. Le 26 tabelle vengono riscritte nello stile del
template (barre laterali + booktabs).

Il testo delle celle e dei paragrafi non viene toccato.
"""
import re, sys, collections
sys.path.insert(0, '/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad')

SRC = '/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad/conv/capitolo_4.tex'
DST = '/home/simone/Downloads/tesi_m_silvia/tesi/main/4_capitolo_4.tex'

CITE = {
    "Astle et al., 2021": "astle2021", "Astle et al., 2022": "astle2022",
    "Bayley, 2006": "bayley2006", "Beauchaine & Cicchetti, 2019": "beauchaine2019",
    "Blair & Raver, 2015": "blair2015", "Calkins, 2007": "calkins2007",
    "Carlson, 2005": "carlson2005", "Diamond, 2013": "diamond2013",
    "Garon et al., 2008": "garon2008", "Hendry & Holmboe, 2021": "hendry2021",
    "Hughes & Graham, 2002": "hughes2002", "Kopp, 1982": "kopp1982",
}

report = collections.Counter()
unmapped = collections.Counter()

# larghezze di colonna per forma di tabella
SPEC = {
    8: (r'|l|c|c|>{\centering\arraybackslash}p{1.9cm}|>{\centering\arraybackslash}p{1.9cm}|'
        r'>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{2.0cm}|'
        r'>{\centering\arraybackslash}p{1.1cm}|'),
    2: (r'|>{\raggedright\arraybackslash}p{4.3cm}|>{\raggedright\arraybackslash}p{9.2cm}|'),
    3: r'|l|c|l|',
    5: r'|l|c|c|c|c|',
}
SPEC_42 = (r'|l|>{\centering\arraybackslash}p{1.9cm}|>{\centering\arraybackslash}p{2.6cm}|'
           r'>{\centering\arraybackslash}p{2.3cm}|>{\centering\arraybackslash}p{3.0cm}|')


def unescape(s):
    return s.replace('\\&', '&').replace('\\%', '%').replace('\\_', '_').replace('\\#', '#')


def debold(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\textbf\{([^{}]*)\}', r'\1', s)
    return s


# ------------------------------------------------------------------ citazioni
def convert_cites(text):
    def repl(m):
        parts = [p.strip() for p in m.group(1).split(';')]
        keys, literals, bad = [], [], False
        for p in parts:
            plain = unescape(p).strip()
            if not re.search(r'\b(?:19|20)\d{2}[a-z]?\b', plain):
                literals.append(p); continue
            if plain not in CITE:
                unmapped[plain] += 1; bad = True; continue
            keys.append(CITE[plain])
        if bad or not keys:
            return m.group(0)
        report['cite'] += len(keys)
        c = '\\cite{' + ','.join(keys) + '}'
        return '(' + '; '.join(literals + [c]) + ')' if literals else c

    pat = re.compile(r'\(([^()]*?\b(?:19|20)\d{2}[a-z]?)\)')
    out, pos = [], 0
    for m in pat.finditer(text):
        inner = unescape(m.group(1)).strip()
        if re.fullmatch(r'(?:19|20)\d{2}[a-z]?', inner) or not re.search(r'[A-Z]', inner):
            continue
        out.append(text[pos:m.start()]); out.append(repl(m)); pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


# ------------------------------------------------------------------ tabelle
def convert_table(m):
    ncol = len(m.group(1))
    body = m.group(2)

    header, rest = None, body
    if '\\endhead' in body:
        pre, rest = body.split('\\endhead', 1)
        pre = pre.replace('\\toprule', '').replace('\\midrule', '').strip()
        header = pre.replace('\\tabularnewline', '').strip()
    rest = rest.replace('\\toprule', '').replace('\\midrule', '').replace('\\bottomrule', '')
    rows = [r.strip() for r in rest.split('\\tabularnewline') if r.strip()]

    # header vero solo se tutte le celle sono in grassetto
    hcells = [c.strip() for c in header.split('&')] if header else []
    is_header = bool(hcells) and all(c.startswith('\\textbf{') for c in hcells)

    idx = report['tab'] = report['tab'] + 1
    spec = SPEC_42 if idx == 25 else SPEC[ncol]

    L = ['\\begin{center}']
    if ncol == 8:
        L.append('\\small')
        L.append('\\setlength{\\tabcolsep}{3pt}')
    elif idx == 25:
        L.append('\\small')
        L.append('\\setlength{\\tabcolsep}{4pt}')
    L.append('\\begin{longtable}{%s}' % spec)
    L.append('\\toprule')
    if is_header:
        L.append(header + ' \\\\')
        L.append('\\midrule')
        L.append('\\endhead')
    elif header:
        rows.insert(0, header)
    for r in rows:
        L.append(r + ' \\\\')
    L.append('\\bottomrule')
    L.append('\\end{longtable}')
    L.append('\\end{center}')
    return '\n'.join(L)


def main():
    s = open(SRC, encoding='utf-8').read()

    # 1. via la prima riga: e' il titolo del capitolo, che ora lo fa \chapter
    s = re.sub(r'^\\textbf\{CAPITOLO 4\}[^\n]*\n', '', s, count=1)

    # 2. via gli artefatti di pandoc
    s = re.sub(r'\\hypertarget\{[^}]*\}\{%\n', '', s)
    for _ in range(6):
        s = re.sub(r'\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{(?:[^{}]|\{[^{}]*\})*\}',
                   r'\1', s)
    s = re.sub(r'\\label\{[^}]*\}\}', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)

    # 2. tabelle
    s = re.sub(r'\\begin\{longtable\}\[\]\{@\{\}(\w+)@\{\}\}(.*?)\\end\{longtable\}',
               convert_table, s, flags=re.S)

    # 3. citazioni
    s = convert_cites(s)

    # 4. titoli
    UNNUM_L3 = re.compile(r'^Caso \d+$')
    UNNUM_L4 = {'Scheda di sintesi', 'Prestazione al Baby-FE',
                'Osservazione del comportamento durante la valutazione '
                '(Behavior Observation Inventory della Bayley-III)'}
    out = []
    headings = []
    forced_section = False
    for line in s.split('\n'):
        raw = line.strip()
        # riga-titolo di pandoc (\section{..}, \subsection{..}, \paragraph{..})
        mh = re.fullmatch(r'\\(?:section|subsection|subsubsection|paragraph)\{(.*)\}', raw)
        content = mh.group(1) if mh else (raw if raw.startswith('\\textbf{') else None)
        if content is None:
            out.append(line); continue

        plain = debold(content).strip()
        if not plain:
            continue                                     # titolo vuoto: si butta

        mnum = re.fullmatch(r'(\d+(?:\.\d+)+)\s*(.*)', plain)
        if mnum:
            num, title = mnum.group(1), mnum.group(2).strip()
            depth = num.count('.')
            cmd = {1: 'section', 2: 'subsection', 3: 'subsubsection'}[depth]
            ind = {1: '    ', 2: '        ', 3: '            '}[depth]
            # 4.4.1 e 4.4.2 non hanno un "4.4" nel Word: si forza il contatore
            if num.startswith('4.4') and not forced_section:
                out.append('    % Nel Word non esiste un titolo "4.4": esistono solo')
                out.append('    % 4.4.1 e 4.4.2. Il contatore viene forzato per riprodurre')
                out.append('    % esattamente quella numerazione, senza inventare un titolo.')
                out.append('    \\setcounter{section}{4}')
                out.append('    \\setcounter{subsection}{0}')
                forced_section = True
            out.append('%s\\%s{%s}' % (ind, cmd, title))
            out.append('%s\\label{sec:%s}' % (ind, num.replace('.', '_')))
            headings.append((num, title, cmd))
            continue

        if UNNUM_L3.fullmatch(plain):
            out.append('            \\subsubsection*{%s}' % plain)
            out.append('            \\addcontentsline{toc}{subsubsection}{%s}' % plain)
            headings.append(('—', plain, 'subsubsection*'))
            continue

        if plain in UNNUM_L4:
            out.append('                \\paragraph*{%s}' % plain)
            headings.append(('—', plain, 'paragraph*'))
            continue

        # non e' un titolo: e' testo corrente marcato per errore come titolo nel Word
        if mh:
            report['destyled'] += 1
            out.append(content)
        else:
            out.append(line)

    s = '\n'.join(out)
    s = re.sub(r'\n{3,}', '\n\n', s)

    # 5. le tre tabelle numerate del Word entrano nell'Elenco delle tabelle con il
    #    loro testo originale, senza aggiungere nessuna didascalia visibile in pagina.
    for lbl, pattern in [
        ('Tabella 4.1 --- Profilo dei fattori di rischio dei bambini selezionati',
         r'(\\emph\{Tabella 4\.1 [^}]*\})'),
        ('Tabella 4.2. Prestazioni complessive al Baby-FE nei casi selezionati',
         r'(\\textbf\{Tabella 4\.2\.[^}]*\})'),
        ('Tabella 4.3. Punteggi alle sottoscale EEFQ nei casi selezionati',
         r'(\\textbf\{Tabella 4\.3\.[^}]*\})'),
    ]:
        s, k = re.subn(pattern,
                       lambda m: '\\addcontentsline{lot}{table}{%s}\n%s' % (lbl, m.group(1)),
                       s, count=1)
        report['lot'] += k

    head = ("\\chapter{Analisi dei casi critici nei processi di regolazione "
            "tra i 18 e i 36 mesi}\n\\label{cap:quattro}\n\n")
    open(DST, 'w', encoding='utf-8').write(head + s.strip() + '\n')

    print('titoli: %d' % len(headings))
    for n, t, c in headings:
        print('   %-8s %-70s %s' % (n, t[:70], c))
    print('tabelle convertite: %d' % report['tab'])
    print('voci aggiunte all\'elenco tabelle: %d' % report['lot'])
    print('paragrafi ripuliti da stile-titolo errato: %d' % report['destyled'])
    print('citazioni convertite: %d' % report['cite'])
    if unmapped:
        print('!! NON MAPPATE:')
        for k, v in unmapped.most_common():
            print('   %3dx %s' % (v, k))
        sys.exit(1)
    print('OK')


main()
