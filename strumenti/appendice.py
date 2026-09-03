# -*- coding: utf-8 -*-
"""Converte in LaTeX le tabelle dell'Appendice 1 (protocollo Baby-FE)."""
import zipfile, re, hashlib, os
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
MC = '{http://schemas.openxmlformats.org/markup-compatibility/2006}'
DOCX = '/home/simone/Downloads/tesi_m_silvia/source/capitolo_3.docx'
IMGDIR = '/home/simone/Downloads/tesi_m_silvia/tesi/images/'

z = zipfile.ZipFile(DOCX)
rels = dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"',
                       z.read('word/_rels/document.xml.rels').decode()))
# media del docx -> file gia' presenti in tesi/images (confronto per contenuto)
noti = {}
for f in os.listdir(IMGDIR):
    if f.startswith('app_'):
        noti[hashlib.md5(open(IMGDIR + f, 'rb').read()).hexdigest()] = os.path.splitext(f)[0]
def nome_img(target):
    dati = z.read('word/' + target.lstrip('/'))
    return noti.get(hashlib.md5(dati).hexdigest())

ESC = {'&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_',
       '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
def esc(s):
    s = s.replace('\\', r'\textbackslash{}')
    s = ''.join(ESC.get(c, c) for c in s)
    s = s.replace('—', '---').replace('–', '--')
    s = s.replace('’', "'").replace('‘', '`')
    s = re.sub(r'“([^”]*)”', r"``\1''", s).replace('“', '``').replace('”', "''")
    return s

def marcatori(r_):
    pr = r_.find(W + 'rPr'); m = set()
    if pr is not None:
        if pr.find(W + 'b') is not None: m.add('b')
        if pr.find(W + 'i') is not None: m.add('i')
        u = pr.find(W + 'u')
        if u is not None and u.get(W + 'val', 'single') != 'none': m.add('u')
    return frozenset(m)

def avvolgi(txt, m):
    if not txt.strip(): return txt
    if 'u' in m: txt = r'\uline{%s}' % txt
    if 'i' in m: txt = r'\emph{%s}' % txt
    if 'b' in m: txt = r'\textbf{%s}' % txt
    return txt

def corse(nodo):
    """I run in ordine di documento, scendendo solo nel ramo mc:Choice degli
    AlternateContent: nel ramo mc:Fallback Word ripete lo stesso testo, che
    altrimenti finirebbe due volte (succede nella tabella 10)."""
    for figlio in nodo:
        if figlio.tag == MC + 'AlternateContent':
            scelta = figlio.find(MC + 'Choice')
            if scelta is not None:
                yield from corse(scelta)
            continue
        if figlio.tag == W + 'r':
            yield figlio
            yield from corse(figlio)   # caselle di testo annidate dentro un disegno
        else:
            yield from corse(figlio)

def paragrafo(p):
    """Fonde le sequenze contigue con la stessa formattazione: Word le spezza
    in decine di run e senza fusione uscirebbe un \\textbf per ogni parola."""
    pezzi, corr, marks = [], '', None
    for r_ in corse(p):
        blip = r_.find('.//' + A + 'blip')
        if blip is not None:
            if corr: pezzi.append(avvolgi(esc(corr), marks)); corr, marks = '', None
            tgt = rels.get(blip.get(R + 'embed'), '')
            nome = nome_img(tgt)
            ext = r_.find('.//' + WP + 'extent')
            h = float(ext.get('cy')) / 914400 * 2.54 if ext is not None else 0.5
            if nome:
                pezzi.append(r'\raisebox{-0.2\height}{\includegraphics[height=%.2fcm]{images/%s}}'
                             % (min(h, 1.0), nome))
            continue
        # solo i w:t figli diretti: con iter() si scenderebbe anche nelle caselle
        # di testo annidate nei disegni, contando quel testo una seconda volta
        t = ''.join(x.text or '' for x in r_.findall(W + 't'))
        if not t: continue
        m = marcatori(r_)
        if m == marks: corr += t
        else:
            if corr: pezzi.append(avvolgi(esc(corr), marks))
            corr, marks = t, m
    if corr: pezzi.append(avvolgi(esc(corr), marks))
    return ''.join(pezzi).strip()

def cella(tc):
    par = [paragrafo(p) for p in tc.findall(W + 'p')]
    return r' \newline '.join(x for x in par if x)

def span(tc):
    pr = tc.find(W + 'tcPr')
    gs = pr.find(W + 'gridSpan') if pr is not None else None
    return int(gs.get(W + 'val')) if gs is not None else 1

# La tabella e' composta in orizzontale e poi ruotata di 90 gradi su una pagina
# che resta verticale: in stampa il lettore gira il libro, e il numero di pagina
# non viene ruotato con essa. La larghezza utile diventa quindi l'altezza del testo.
LARG = [3.2, 2.8, 7.8, 5.0, 1.0]          # cm: con separatori e filetti ~20,9
                                          # contro i 22,19 di altezza del testo
COLS = '|' + '|'.join('p{%scm}' % x for x in LARG) + '|'
TABCOLSEP = 3.0 / 28.45                   # 3pt in cm

def largh_span(i, s):
    """Larghezza di una cella che ne unisce piu' d'una: le colonne fuse piu'
    lo spazio fra loro, altrimenti il testo va a capo troppo presto."""
    return sum(LARG[i:i + s]) + (s - 1) * 2 * TABCOLSEP

def tabella(idx):
    root = ET.fromstring(z.read('word/document.xml'))
    t = list(root.iter(W + 'tbl'))[idx]
    # niente ambiente center: lo spazio verticale che aggiunge basta a far
    # traboccare il riquadro ruotato e a lasciare una pagina bianca
    # niente minipage: forzerebbe la larghezza a \textheight e il riquadro
    # ruotato risulterebbe piu' alto della pagina. La tabella si dimensiona da se'.
    out = [r'\clearpage', r'\noindent\centerline{%',
           r'\rotatebox{90}{%',
           r'\footnotesize', r'\setlength{\tabcolsep}{3pt}',
           r'\begin{tabular}{%s}' % COLS, r'\toprule']
    for i, tr in enumerate(t.findall(W + 'tr')):
        celle, tot = [], 0
        for tc in tr.findall(W + 'tc'):
            s = span(tc)
            tx = cella(tc)
            if s > 1:
                celle.append(r'\multicolumn{%d}{|p{%.2fcm}|}{%s}' % (s, largh_span(tot, s), tx))
            else:
                celle.append(tx)
            tot += s
        while tot < 5: celle.append(''); tot += 1
        out.append('  ' + ' & '.join(celle) + r' \\')
        if i == 0: out.append(r'\midrule')
    out += [r'\bottomrule', r'\end{tabular}', r'}}']
    return '\n'.join(out)

if __name__ == '__main__':
    import sys
    print(tabella(int(sys.argv[1]) - 1))

# ---------------------------------------------------------------- legenda
def legenda():
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body'); figli = list(body)
    ultima = max(i for i, c in enumerate(figli) if c.tag == W + 'tbl')
    righe = []
    for c in figli[ultima + 1:]:
        if c.tag != W + 'p': continue
        t = paragrafo(c)
        if t: righe.append(t)
    return righe

def documento():
    out = [r'\chapter{Protocollo di somministrazione e scoring del Baby-FE}',
           r'\label{app:babyfe}', '',
           r'\thispagestyle{plain}', '',
           r'\noindent\textbf{CODICE:}~\rule{3.2cm}{0.4pt}\quad'
           r'\textbf{ETA'' IN MESI:}~\rule{2.4cm}{0.4pt}\quad'
           r'\textbf{DATA DI VALUTAZIONE:}~\rule{2.8cm}{0.4pt}', '']
    for i in range(15):
        out.append(tabella(i)); out.append('')
    out += [r'\clearpage', '', r'\section*{Legenda}', '']
    for r_ in legenda():
        out.append(r_); out.append('')
    return '\n'.join(out)
