# -*- coding: utf-8 -*-
"""Controllo C, parte (a): ogni \cite del LaTeX contro il (Autore, anno) del Word originale.
Allineamento per contesto: le parole che precedono la citazione nel LaTeX vengono cercate
nel testo del Word, e la citazione che segue nel Word viene confrontata con la voce bib."""
import re, unicodedata, json, sys
SP='/tmp/claude-1000/-home-simone-Downloads-tesi-m-silvia/4d74be00-3d12-4c77-9974-5780b0160f34/scratchpad/'
TESI='/home/simone/Downloads/tesi_m_silvia/tesi/'
YEAR=r'(?:1[89]|20)\d{2}[a-z]?'

def deacc(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
def key(s): return re.sub(r'[^a-z]','',deacc(s).lower())

# --- bibliografia: chiave -> (cognomi, anno)
bib={}
for m in re.finditer(r'@\w+\{([^,]+),(.*?)\n\}', open(TESI+'tail/References.bib',encoding='utf-8').read(), re.S):
    k,body=m.group(1),m.group(2)
    au=re.search(r'author\s*=\s*\{(.*?)\},?\n',body,re.S); yr=re.search(r'year\s*=\s*\{(\d{4})\}',body)
    cognomi=[key(a.split(',')[0]) for a in re.split(r'\s+and\s+',au.group(1))] if au else []
    bib[k]=(cognomi, yr.group(1) if yr else '')

def norm_words(t):
    t=unicodedata.normalize('NFC',t).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    t=t.replace('``','"').replace("''",'"').replace('---','—').replace('--','–')
    return t

def tex_plain(t):
    t=re.sub(r'(?<!\\)%.*$','',t,flags=re.M)
    t=re.sub(r'\\(?:label|ref|chaptermark|titlespacing\*?|setcounter|addcontentsline)\{[^}]*\}(\{[^}]*\})*','',t)
    t=re.sub(r'\\(?:begin|end)\{[^}]*\}(\[[^\]]*\])?(\{[^}]*\})*','',t)
    t=re.sub(r'\\caption(\[[^\]]*\])?\{','',t)
    t=re.sub(r'\\(?:textbf|emph|textit|uline|section|subsection|subsubsection|paragraph|chapter)\*?\{','',t)
    t=re.sub(r'\\[a-zA-Z]+\*?','',t)
    return t.replace('~',' ').replace('{','').replace('}','').replace('&',' ')

def md_plain(t):
    t=re.sub(r'!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?',' ',t)
    t=re.sub(r'\{[.#][^}]*\}',' ',t)
    t=re.sub(r'(?m)^[ \t>]*#{1,6}[ \t]*',' ',t); t=re.sub(r'(?m)^[ \t>]+',' ',t)
    t=re.sub(r'(?m)^\s*[-=]{3,}(\s+-{3,})*\s*$',' ',t)
    t=re.sub(r'\\([.\-#_*\[\]()~<>&$%{}"\'])',r'\1',t); t=re.sub(r'\*+','',t); t=t.replace('|',' ')
    return t

CAP={1:'1_capitolo_1',2:'2_capitolo_2',3:'3_capitolo_3',4:'4_capitolo_4'}
esiti=[]; tot=0
for n,f in CAP.items():
    tex=open(TESI+'main/'+f+'.tex',encoding='utf-8').read()
    md=open(SP+'conv/capitolo_%d.md'%n,encoding='utf-8').read()
    W=norm_words(md_plain(md)); Wc=re.sub(r'\s+',' ',W)
    # posizioni delle citazioni nel tex, con contesto precedente
    tp=norm_words(tex_plain(re.sub(r'\\cite\{([^}]*)\}', r' CITE<\1> ', tex)))
    tp=re.sub(r'\s+',' ',tp)
    cursore=0                                   # ricerca progressiva: l'ordine e' lo stesso nei due testi
    for m in re.finditer(r' ?CITE<([^>]*)> ?', tp):
        tot+=1
        keys=[k.strip() for k in m.group(1).split(',')]
        pre=tp[:m.start()].split()[-7:]
        pos=-1
        for L in (7,5,4,3):
            ctx=' '.join(pre[-L:]); pos=Wc.find(ctx, cursore)
            if pos>=0: break
        if pos<0:
            esiti.append((n,keys,'CONTESTO NON TROVATO',' '.join(pre))); continue
        cursore=pos
        after=Wc[pos+len(ctx):][:260]
        # forme: " (Autore, anno; ...)", " 1 (Autore, anno)" (numero di un \ref tolto),
        # "Autore, anno)" (parentesi aperta prima, es. "(IBQ-R; Gartstein & Rothbart, 2003)"),
        # narrativa "Kopp (1982)"
        g=re.match(r'\s*(?:[\d.§]+\s*)?\(([^()]*?'+YEAR+r'[^()]*)\)', after)
        if not g and pre and pre[-1].endswith(';'):
            g=re.match(r'\s*([^()]*?'+YEAR+r'[^()]*)\)', after)
        if g:
            parts=[q.strip() for q in g.group(1).split(';') if re.search(YEAR,q)]
        else:
            g2=re.match(r'\s*\(('+YEAR+r')\)', after)
            if not g2: esiti.append((n,keys,'CITAZIONE WORD NON TROVATA',' '.join(pre)+' | '+after[:60])); continue
            parts=[pre[-1]+', '+g2.group(1)]
        if len(parts)!=len(keys):
            esiti.append((n,keys,'NUMERO DIVERSO',' ; '.join(parts))); continue
        for q,k in zip(parts,keys):
            yr=re.search(YEAR,q).group(0)[:4]
            testa=re.sub(r'\bet al\.?','',q.split(',')[0]) if ',' in q else q
            sur=[key(x) for x in re.findall(r"[A-ZÀ-Ü][\wÀ-ÿ'’\-]+", testa)]
            if not sur: sur=[key(pre[-1])]                       # narrativa: cognome prima della parentesi
            cog,by=bib.get(k,([],''))
            ok_year = (yr==by) or (k=='astle2022' and yr in('2021','2022')) or (k=='meins2001' and yr=='2001')
            ok_sur = any(any(s==c or c.startswith(s) or s.startswith(c) for c in cog) for s in sur) \
                     or (k=='vygotsky1962' and 'vygotskij' in sur) or (k=='gartstein2003' and 'rothbart' in sur)
            if not (ok_year and ok_sur):
                esiti.append((n,[k],'NON CORRISPONDE',f'Word: «{q}»  ->  bib {k}: {cog[:3]} {by}'))
print('citazioni esaminate:', tot, '| problemi:', len(esiti))
for e in esiti: print('  cap %d %-30s %-26s %s' % (e[0], ','.join(e[1])[:30], e[2], e[3][:110]))
