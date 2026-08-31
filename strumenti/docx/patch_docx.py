# -*- coding: utf-8 -*-
"""Scrive nel .docx la geometria di pagina e le larghezze delle tabelle.

Pandoc 2.9 non ricava le larghezze di colonna dal LaTeX: senza queste Word
dimensiona le colonne sul contenuto e le tabelle sforano il margine laterale.
Le larghezze sono scelte in base all'intestazione di ciascuna tabella.
"""
import zipfile, re, sys

DOCX = '/home/simone/Downloads/tesi_m_silvia/capitolo_4_tesi.docx'

# A4 in twip (1 cm = 567), margini 2,5 cm -> 16,0 cm utili
PAGE_W, MARG = 11906, 1417
UTILE = PAGE_W - 2 * MARG

# larghezze in cm (sommano a 16,0) e, dove serve, corpo del carattere in mezzi punti:
# con otto colonne le intestazioni non entrano a corpo pieno e Word spezza le parole.
SCHEMI = {
    ('Caso', 'Genere'):        ([1.6, 1.7, 1.6, 2.3, 2.2, 2.2, 2.7, 1.7], 18),  # 4.1 fattori di rischio
    ('Genere',):               ([4.5, 11.5], None),                        # schede di sintesi
    ('Prova',):                ([8.5, 3.0, 4.5], None),                    # prestazione al Baby-FE
    ('Comportamento',):        ([6.5, 3.2, 6.3], None),                    # osservazione BOI
    ('Caso', 'Età (mesi)'):    ([2.4, 2.4, 3.8, 3.2, 4.2], 20),            # 4.25 prestazioni complessive
    ('Caso', 'IC'):            ([6.0, 2.5, 2.5, 2.5, 2.5], None),          # 4.26 sottoscale EEFQ
}

def testo(cell):
    return ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', cell)).strip()

def larghezze(tbl):
    riga = re.search(r'<w:tr[ >].*?</w:tr>', tbl, re.S).group(0)
    celle = [testo(c) for c in re.findall(r'<w:tc>.*?</w:tc>', riga, re.S)]
    for chiave, (w, sz) in SCHEMI.items():
        if len(w) == len(celle) and all(celle[i] == k for i, k in enumerate(chiave)):
            return w, sz
    sys.exit('schema di colonne non riconosciuto: %r' % celle)

z = zipfile.ZipFile(DOCX)
parts = {n: z.read(n) for n in z.namelist()}
z.close()
xml = parts['word/document.xml'].decode('utf-8')

out, pos, n = [], 0, 0
for m in re.finditer(r'<w:tbl>.*?</w:tbl>', xml, re.S):
    t = m.group(0)
    cm, sz = larghezze(t)
    tw = [int(round(UTILE * c / sum(cm))) for c in cm]
    tw[-1] += UTILE - sum(tw)

    t = re.sub(r'<w:tblW[^/]*/>',
               '<w:tblW w:type="pct" w:w="5000"/><w:tblLayout w:type="fixed"/>', t)
    griglia = '<w:tblGrid>' + ''.join('<w:gridCol w:w="%d"/>' % x for x in tw) + '</w:tblGrid>'
    if '<w:tblGrid>' in t:
        t = re.sub(r'<w:tblGrid>.*?</w:tblGrid>', griglia, t, flags=re.S)
    else:
        t = t.replace('</w:tblPr>', '</w:tblPr>' + griglia, 1)

    contatore = [0]
    def cella(mc):
        i = contatore[0] % len(tw); contatore[0] += 1
        c, w = mc.group(0), '<w:tcW w:w="%d" w:type="dxa"/>' % tw[i]
        if '<w:tcW' in c:      return re.sub(r'<w:tcW[^/]*/>', w, c)
        if '<w:tcPr>' in c:    return c.replace('<w:tcPr>', '<w:tcPr>' + w, 1)
        return c.replace('<w:tc>', '<w:tc><w:tcPr>' + w + '</w:tcPr>', 1)
    t = re.sub(r'<w:tc>.*?</w:tc>', cella, t, flags=re.S)

    if sz:                                   # corpo ridotto dentro la tabella
        t = re.sub(r'<w:rPr>', '<w:rPr><w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (sz, sz), t)
        t = re.sub(r'<w:r>(?!<w:rPr>)',
                   '<w:r><w:rPr><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>' % (sz, sz), t)
    out.append(xml[pos:m.start()]); out.append(t); pos = m.end(); n += 1
out.append(xml[pos:])
xml = ''.join(out)

SECTPR = (f'<w:sectPr><w:pgSz w:w="{PAGE_W}" w:h="16838"/>'
          f'<w:pgMar w:top="{MARG}" w:right="{MARG}" w:bottom="{MARG}" w:left="{MARG}"'
          f' w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>')
if re.search(r'<w:sectPr\s*/>', xml):
    xml = re.sub(r'<w:sectPr\s*/>', SECTPR, xml)
elif '<w:sectPr' not in xml:
    xml = xml.replace('</w:body>', SECTPR + '</w:body>')

parts['word/document.xml'] = xml.encode('utf-8')
with zipfile.ZipFile(DOCX, 'w', zipfile.ZIP_DEFLATED) as zo:
    for k, d in parts.items():
        zo.writestr(k, d)
print('tabelle sistemate:', n, '| larghezza utile: %.1f cm' % (UTILE / 567))
