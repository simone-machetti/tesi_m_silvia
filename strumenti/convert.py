#!/usr/bin/env python3
"""
Converte un capitolo Word (gia' passato per `pandoc -t latex`) nel formato del
template tesi/: titoli LaTeX + citazioni numeriche \cite{}.

Il testo NON viene toccato: si trasformano solo i titoli e le citazioni.
Se incontra una citazione non mappata si ferma con errore, cosi' nulla passa
inosservato.
"""
import re, sys, json, collections

# ---------------------------------------------------------------- mappa citazioni
# stringa autore+anno come compare nel testo  ->  chiave in References.bib
CITE = {
    "Allotey et al., 2018": "allotey2018",
    "Astle et al., 2021": "astle2021",
    "Astle et al., 2022": "astle2022",
    "Barkley, 1997": "barkley1997",
    "Bayley, 2006": "bayley2006",
    "Beauchaine, 2015": "beauchaine2015",
    "Beauchaine & Cicchetti, 2019": "beauchaine2019",
    "Beauchaine & McNulty, 2013": "beauchaine2013mcnulty",
    "Berni et al., 2025": "berni2025",
    "Bernier, Carlson & Whipple, 2010": "bernier2010",
    "Bernier et al., 2010": "bernier2010",
    "Bishop et al., 2017": "bishop2017",
    "Blair, 2010": "blair2010",
    "Blair & Ku, 2022": "blair2022",
    "Blair & Raver, 2015": "blair2015",
    "Blair & Razza, 2007": "blair2007",
    "Blair & Ursache, 2011": "blair2011ursache",
    "Bradley & Corwyn, 2002": "bradley2002",
    "Calkins, 2007": "calkins2007",
    "Calkins & Fox, 2002": "calkins2002fox",
    "Calkins & Hill, 2007": "calkins2007hill",
    "Calkins & Leerkes, 2011": "calkins2011",
    "Carlson, 2005": "carlson2005",
    "Caspi et al., 2014": "caspi2014",
    "Chronis-Tuscano et al., 2009": "chronistuscano2009",
    "Cicchetti, 2006": "cicchetti2006",
    "Cicchetti & Rogosch, 2002": "cicchetti2002",
    "Cicchetti & Toth, 2009": "cicchetti2009",
    "Clark et al., 2008": "clark2008",
    "Cole, Martin & Dennis, 2004": "cole2004",
    "Cole, Martin, & Dennis, 2004": "cole2004",
    "Cole et al., 2004": "cole2004",
    "Cole et al., 1994": "cole1994",
    "Cuevas & Bell, 2014": "cuevas2014",
    "Cuthbert & Insel, 2013": "cuthbert2013",
    "Dalgleish et al., 2020": "dalgleish2020",
    "Daunhauer & Fidler, 2011": "daunhauer2011",
    "Degnan & Fox, 2007": "degnan2007",
    "Diamond, 2013": "diamond2013",
    "Doebel, 2020": "doebel2020",
    "Duckworth & Kern, 2011": "duckworth2011",
    "Egger & Angold, 2006": "egger2006",
    "Eisenberg et al., 2010": "eisenberg2010",
    "Evans, Li & Whipple, 2013": "evans2013",
    "Evans et al., 2013": "evans2013",
    "Fidler, 2005": "fidler2005",
    "Fidler et al., 2009": "fidler2009",
    "Fletcher-Watson, 2022": "fletcherwatson2022",
    "Fox, 1994": "fox1994",
    "Fox et al., 2005": "fox2005",
    "Friedman & Miyake, 2017": "friedman2017",
    "Gandolfi et al., 2014": "gandolfi2014",
    "Gardiner & Iarocci, 2017": "gardiner2017",
    "Garon, Bryson & Smith, 2008": "garon2008",
    "Garon et al., 2008": "garon2008",
    "Gartstein & Rothbart, 2003": "gartstein2003",
    "Gioia et al., 2003": "gioia2003",
    "Graziano & Garcia, 2016": "graziano2016",
    "Hendry & Holmboe, 2021": "hendry2021",
    "Hughes & Graham, 2002": "hughes2002",
    "Isquith et al., 2004": "isquith2004",
    "Kagan et al., 1987": "kagan1987",
    "Karreman et al., 2006": "karreman2006",
    "Kochanska, 2001": "kochanska2001",
    "Kochanska et al., 2001": "kochanska2001",
    "Kochanska et al., 2000": "kochanska2000",
    "Kochanska & Aksan, 2006": "kochanska2006",
    "Kopp, 1982": "kopp1982",
    "Kotov et al., 2017": "kotov2017",
    "Lanfranchi et al., 2010": "lanfranchi2010",
    "Mazefsky et al., 2013": "mazefsky2013",
    "McClelland & Cameron, 2012": "mcclelland2012",
    "Meins et al., 2001": "meins2001",
    "Mischel et al., 1989": "mischel1989",
    "Miyake et al., 2000": "miyake2000",
    "Miyake & Friedman, 2012": "miyake2012",
    "Montagna & Nosarti, 2016": "montagna2016",
    "Montroy et al., 2016": "montroy2016",
    "Morris et al., 2007": "morris2007",
    "Nigg, 2017": "nigg2017",
    "Nolen-Hoeksema & Watkins, 2011": "nolenhoeksema2011",
    "Porges et al., 1994": "porges1994",
    "Posner & Rothbart, 2000": "posner2000",
    "Putnam et al., 2006": "putnam2006",
    "Rothbart & Bates, 2006": "rothbart2006",
    "Rothbart & Rueda, 2005": "rothbart2005",
    "Rothbart, Sheese, & Posner, 2007": "rothbart2007",
    "Rothbart, Sheese & Posner, 2007": "rothbart2007",
    "Rubin et al., 2009": "rubin2009",
    "Rutter, 1989": "rutter1989",
    "Sameroff, 2009": "sameroff2009",
    "Samson et al., 2014": "samson2014",
    "Slade, 2005": "slade2005",
    "Snyder et al., 2021": "snyder2021",
    "Sonuga-Barke, 2005": "sonugabarke2005",
    "Sonuga-Barke et al., 2016": "sonugabarke2016",
    "Sroufe, 1996": "sroufe1996",
    "Sroufe, 2005": "sroufe2005",
    "Sroufe, 2009": "sroufe2009",
    "Toplak, West, & Stanovich, 2013": "toplak2013",
    "Toplak, West & Stanovich, 2013": "toplak2013",
    "Toplak et al., 2013": "toplak2013",
    "Tronick, 2007": "tronick2007",
    "Tronick & Beeghly, 2011": "tronick2011",
    "Ursache, Blair & Raver, 2012": "ursache2012",
    "Ursache et al., 2012": "ursache2012",
    "Vallotton & Ayoub, 2011": "vallotton2011",
    "Vygotskij, 1962": "vygotsky1962",
    "Vygotsky, 1962": "vygotsky1962",
    "Wellman, 2014": "wellman2014",
    "Wellman, Cross & Watson, 2001": "wellman2001",
    "Wellman et al., 2001": "wellman2001",
    "Zelazo, 2015": "zelazo2015",
    "Zelazo, 2020": "zelazo2020",
    "Zelazo et al., 2003": "zelazo2003",
    "Zelazo et al., 2020": "zelazo2020blair",
    "Zelazo & Carlson, 2012": "zelazo2012",
    "Garon, Bryson, & Smith, 2008": "garon2008",
    "Snyder, Miyake, & Hankin, 2021": "snyder2021",
    "Porges, Doussard-Roosevelt, & Maiti, 1994": "porges1994",
    "Kochanska, Coy, & Murray, 2001": "kochanska2001",
    "Mischel, Shoda, & Rodriguez, 1989": "mischel1989",
    "Gioia, Espy, & Isquith, 2003": "gioia2003",
    "Putnam, Gartstein, & Rothbart, 2006": "putnam2006",
    "Rothbart et al., 2003": "gartstein2003",
}

# citazioni narrative: "Autore (anno)" -> chiave. Il nome resta nel testo, cambia
# solo l'anno tra parentesi, che diventa il numero della citazione.
NARRATIVE = {}   # popolata da un file di config per capitolo


def unescape(s):
    """riporta il LaTeX di pandoc a testo semplice, per il confronto con la mappa"""
    return s.replace('\\&', '&').replace('\\%', '%').replace('\\_', '_').replace('\\#', '#')


def convert_cites(text, report):
    """(Autore, anno; Autore, anno) -> \\cite{k1,k2}"""
    def repl(m):
        inner = m.group(1)
        parts = [p.strip() for p in inner.split(';')]
        keys, literals, bad = [], [], False
        for p in parts:
            plain = unescape(p).strip()
            if not re.search(r'\b(?:19|20)\d{2}[a-z]?\b', plain):
                # non e' una citazione (es. la sigla di uno strumento): resta com'e'
                literals.append(p)
                continue
            if plain not in CITE:
                report['unmapped'][plain] += 1
                bad = True
                continue
            keys.append(CITE[plain])
        if bad or not keys:
            return m.group(0)              # lasciata intatta, segnalata
        report['converted'] += len(keys)
        cites = '\\cite{' + ','.join(keys) + '}'
        if literals:
            return '(' + '; '.join(literals + [cites]) + ')'
        return cites

    # gruppo parentetico che contiene almeno un anno e nessuna parentesi annidata
    pattern = re.compile(r'\(([^()]*?\b(?:19|20)\d{2}[a-z]?)\)')
    out, pos = [], 0
    for m in pattern.finditer(text):
        inner = unescape(m.group(1)).strip()
        # salta i gruppi che sono solo un anno: sono citazioni narrative
        if re.fullmatch(r'(?:19|20)\d{2}[a-z]?', inner):
            continue
        # salta i gruppi che non sembrano citazioni (es. "(3--6 anni)")
        if not re.search(r'[A-Z]', inner):
            continue
        out.append(text[pos:m.start()])
        out.append(repl(m))
        pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


def convert_narrative(text, report):
    """Autore (anno) -> Autore \\cite{key}, secondo la mappa NARRATIVE"""
    for phrase, key in NARRATIVE.items():
        n = text.count(phrase)
        if n == 0:
            report['narrative_missing'].append(phrase)
            continue
        year = re.search(r'\((\d{4})\)', phrase).group(1)
        text = text.replace(phrase, phrase[:phrase.rindex('(')].rstrip() + ' \\cite{%s}' % key)
        report['converted'] += n
    return text


def debold(s):
    """toglie i \\textbf{} (anche piu' run adiacenti), lascia il resto"""
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\textbf\{([^{}]*)\}', r'\1', s)
    return s


def convert_headings(text, chapnum, chaptitle, report):
    lines = text.split('\n')
    out = []
    for line in lines:
        s = line.strip()
        # una riga e' un titolo se, tolto il grassetto, inizia con "N.N" o "N.N.N"
        plain = debold(s).strip()
        m = re.fullmatch(r'(\d+(?:\.\d+)+)\s*(.*)', plain) if s.startswith('\\textbf{') else None
        if m:
            num, title = m.group(1), m.group(2).strip()
            depth = num.count('.')
            cmd = {1: 'section', 2: 'subsection', 3: 'subsubsection'}[depth]
            indent = {1: '    ', 2: '        ', 3: '            '}[depth]
            lbl = num.replace('.', '_')
            out.append('%s\\%s{%s}' % (indent, cmd, title))
            out.append('%s\\label{sec:%s}' % (indent, lbl))
            report['headings'].append('%s %s -> \\%s' % (num, title, cmd))
            continue
        out.append(line)
    return '\n'.join(out)


def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    global NARRATIVE
    NARRATIVE = cfg.get('narrative', {})
    text = open(cfg['input'], encoding='utf-8').read()

    report = {'converted': 0, 'unmapped': collections.Counter(),
              'headings': [], 'narrative_missing': []}

    # 1. via il titolo del capitolo dalla prima riga
    text = re.sub(r'^\\textbf\{[^}]*\}\s*\n', '', text, count=1)

    # 2. citazioni narrative, poi parentetiche
    text = convert_narrative(text, report)
    text = convert_cites(text, report)

    # 3. titoli
    text = convert_headings(text, cfg['number'], cfg['title'], report)

    # 4. rientro del corpo del testo sotto i titoli
    body = []
    indent = '        '
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            body.append('')
        elif s.startswith('\\section'):
            indent = '        '; body.append(line)
        elif s.startswith('\\subsection'):
            indent = '            '; body.append(line)
        elif s.startswith('\\subsubsection'):
            indent = '                '; body.append(line)
        elif s.startswith('\\label'):
            body.append(line)
        else:
            body.append(indent + s)

    head = '\\chapter{%s}\n\\label{cap:%s}\n' % (cfg['title'], cfg['label'])
    if cfg.get('pagestyle'):
        head += '\\pagestyle{fancy}\n'
    open(cfg['output'], 'w', encoding='utf-8').write(head + '\n'.join(body).rstrip() + '\n')

    print('titoli convertiti: %d' % len(report['headings']))
    for h in report['headings']:
        print('   ', h)
    print('citazioni convertite: %d' % report['converted'])
    if report['narrative_missing']:
        print('!! narrative non trovate nel testo:')
        for p in report['narrative_missing']:
            print('   ', p)
    if report['unmapped']:
        print('!! CITAZIONI NON MAPPATE:')
        for k, v in report['unmapped'].most_common():
            print('   %3dx  %s' % (v, k))
        sys.exit(1)
    print('OK — nessuna citazione non mappata')


main()
