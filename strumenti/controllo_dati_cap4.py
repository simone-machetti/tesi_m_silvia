#!/usr/bin/env python3
"""
Controllo sistematico dei dati del capitolo 4 contro i due Excel in source/
(dataset completo e foglio di analisi). Confronta Tabella 4.1, le 8 schede, le 8 tabelle
delle prove, le 7 tabelle BOI, le Tabelle 4.25 e 4.26 e le affermazioni numeriche della
prosa; ricalcola totali, percentili e statistiche del campione. Uso, dalla radice del repo:
    python3 strumenti/controllo_dati_cap4.py
Vedi cap_4.md, sezione «Controllo sistematico sui dati grezzi».
"""
import re, openpyxl, statistics, math
from decimal import Decimal, ROUND_HALF_UP
TEX='tesi/main/4_capitolo_4.tex'; t=open(TEX).read()
# ---------------- tabelle del tex
def clean(c):
    c=re.sub(r'\\(textbf|emph|textit)\{([^{}]*)\}',r'\2',c); c=c.replace('\\newline',' ').replace('\\textasciitilde','~').replace('\\textless','<')
    return re.sub(r'\s+',' ',c.replace('\\\\','')).strip()
tabs={}
for m in re.finditer(r'\\begin\{table\}.*?\\label\{([^}]*)\}(.*?)\\end\{table\}', t, re.S):
    rows=[[clean(c) for c in l.split('&')] for l in m.group(2).split('\n') if '&' in l]
    tabs[m.group(1)]=rows
# ---------------- excel
B=openpyxl.load_workbook('source/BabyFe 2026 x analisi luglio 2026.xlsx', data_only=True, read_only=True)
rows=list(B['Foglio1'].iter_rows(values_only=True)); H=[str(h).strip() if h else h for h in rows[0]]
D=[dict(zip(H,r)) for r in rows[1:] if r[0]]
norm=lambda s: str(s).replace(' ','').upper()
A=openpyxl.load_workbook('source/Analisi per Sivia.xlsx', data_only=True, read_only=True)
an={norm(r[0]):(r[1],r[2]) for r in A['BabyFE'].iter_rows(values_only=True) if r[0] and r[0]!='codice'}
ee={norm(r[0]):r[1:5] for r in A['EEFQ'].iter_rows(values_only=True) if r[0] and r[0]!='codice'}
stats={r[7]:r[8:13] for r in A['EEFQ'].iter_rows(values_only=True) if r[7] and str(r[7]).startswith('EEFQ')}
CASI={1:'06MD-SF03',2:'18CO-AC03',3:'19AM-AC10',4:'23IB-AC05',5:'AC08',6:'VR07',7:'AQ11',8:'AQ07'}
R={k:[d for d in D if norm(d['codice'])==v][0] for k,v in CASI.items()}
err=[]; ok=0
def chk(cond,msg):
    global ok
    if cond: ok+=1
    else: err.append(msg)
def r1(x):  # arrotondamento a 1 decimale, mezzo verso l'alto, virgola
    return str(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')
PROVE=['1libro_cane','2memory','3WM_update','4A_non_B','5spost_invis','6.costruzioni','7 turnazione','8 cubi','9impasto','10statua','11bolle','12anelli','13torta','14forno','15gioco']
def pv(d,k):
    for h in d:
        if h and h.replace(' ','')==k.replace(' ',''): return d[h]
    raise KeyError(k)
def tot_nv(d):
    vals=[pv(d,p) for p in PROVE[1:14]]
    return sum(v for v in vals if v in (0,1,2)), sum(1 for v in vals if v in (8,9))
# ---------------- Tabella 4.1
sino=lambda v: 'SÌ' if v==2 else '--'
for k,row in zip(range(1,9), tabs['tab:rischio'][1:]):
    d=R[k]; att=[str(k),'F' if d['sex']==2 else 'M',str(d['età_mesi2026']),sino(d['pretermine']),sino(d['probl_nascita']),sino(d['preocc']),sino(d['visite_suggerite']),sino(d['visite_fatte']),str(sum(1 for v in (d['pretermine'],d['probl_nascita'],d['preocc'],d['visite_suggerite'],d['visite_fatte']) if v==2))]
    chk(row==att,'Tabella 4.1 Caso %d: tex %s != excel %s'%(k,row,att))
# ---------------- schede
REDD={1:'nettamente al di sotto della media',2:'al di sotto della media',3:'nella media',4:'al di sopra della media',5:'nettamente al di sopra della media'}
for k in range(1,9):
    rows_=tabs['tab:caso%d_scheda'%k]; d=R[k]; cell={r[0]:r[1] for r in rows_}
    chk(cell['Genere']==('Femmina' if d['sex']==2 else 'Maschio'),'Scheda Caso %d: genere'%k)
    chk(cell['Età alla somministrazione']=='%d mesi'%d['età_mesi2026'],'Scheda Caso %d: età'%k)
    an_=cell['Dati anamnestici (questionario compilato dai genitori)']
    if d['peso_nascita'] and d['peso_nascita']>1000: chk(('%d g'%d['peso_nascita']) in an_,'Scheda Caso %d: peso %s non citato'%(k,d['peso_nascita']))
    chk((('pretermine' in an_) == (d['pretermine']==2)),'Scheda Caso %d: pretermine'%k)
    chk(('a termine' in an_)==(d['pretermine']==1) or k==8,'Scheda Caso %d: a termine'%k)
    chk(('parto naturale' in an_)==(d['tipo_nascita']==1),'Scheda Caso %d: parto naturale'%k)
    chk((('problemi segnalati alla nascita' in an_) or ('cardiopatia' in an_ and d['probl_nascita']==2))==(d['probl_nascita']==2) or (d['probl_nascita']==1 and ('nessun problema' in an_.lower() or 'Nessun problema' in an_)),'Scheda Caso %d: problemi alla nascita (excel %s)'%(k,d['probl_nascita']))
    chk(('Preoccupazione dei genitori' in an_ or 'preoccupazione dei genitori' in an_)==(d['preocc']==2),'Scheda Caso %d: preoccupazione (excel %s)'%(k,d['preocc']))
    chk(('suggerite' in an_)==(d['visite_suggerite']==2),'Scheda Caso %d: visite suggerite (excel %s)'%(k,d['visite_suggerite']))
    chk(('effettuate' in an_)==(d['visite_fatte']==2),'Scheda Caso %d: visite effettuate (excel %s)'%(k,d['visite_fatte']))
    if d['bilingue'] in (1,2): chk(('Contesto bilingue' in an_)==(d['bilingue']==2) and ('non bilingue' in an_)==(d['bilingue']==1),'Scheda Caso %d: bilingue (excel %s)'%(k,d['bilingue']))
    nf=d['num_figli']; 
    if nf in (0,1): chk('unic' in an_,'Scheda Caso %d: figlio unico (excel num_figli=%s)'%(k,nf))
    elif nf==2: chk('due figli' in an_,'Scheda Caso %d: due figli'%k)
    elif nf==3: chk('tre figli' in an_,'Scheda Caso %d: tre figli'%k)
    chk(REDD[d['reddito']] in an_,'Scheda Caso %d: reddito (excel %s -> %s)'%(k,d['reddito'],REDD[d['reddito']]))
    if d['cittadin']==2 and k==7: chk('cittadinanza non italiana' in an_,'Scheda Caso 7: cittadinanza')
    if k==8: chk("Nato all'estero" in an_ and 'quindici mesi' in an_ and d['dove nato']==2 and d['In italia_mesi']==15,'Scheda Caso 8: nato all\'estero / 15 mesi')
# ---------------- prove
ESITO={'0':'non corretta','1':'parziale','2':'corretta','NV':'non valutabile','n.d.':'dato mancante'}
code=lambda v: {9:'NV',8:'n.d.'}.get(v,str(v))
for k in range(1,9):
    rows_=tabs['tab:caso%d_prove'%k][1:]; d=R[k]
    chk(len(rows_)==15,'Prove Caso %d: %d righe'%(k,len(rows_)))
    for i,(row,p) in enumerate(zip(rows_,PROVE)):
        chk(row[1]==code(pv(d,p)),'Prove Caso %d, prova %d: tex %s != excel %s'%(k,i+1,row[1],code(pv(d,p))))
        chk(row[2]==ESITO[row[1]],'Prove Caso %d, prova %d: esito %s incoerente con punteggio %s'%(k,i+1,row[2],row[1]))
# ---------------- BOI
FREQ={'0':'mai o raramente','1':'qualche volta','2':'per la maggior parte del tempo'}
for k in range(1,9):
    lab='tab:caso%d_boi'%k; d=R[k]; bail=[d['Bailey_%d'%i] for i in range(1,14)]
    if lab not in tabs: chk(all(v==8 for v in bail),'BOI Caso %d: tabella assente ma excel ha dati %s'%(k,bail)); continue
    rows_=tabs[lab][1:]; chk(len(rows_)==13,'BOI Caso %d: %d righe'%(k,len(rows_)))
    for i,(row,v) in enumerate(zip(rows_,bail)):
        chk(row[1]==str(v),'BOI Caso %d, item %d (%s): tex %s != excel %s'%(k,i+1,row[0],row[1],v))
        chk(row[2]==FREQ[row[1]],'BOI Caso %d, item %d: frequenza %s incoerente'%(k,i+1,row[2]))
# ---------------- Tabella 4.25
def perc_label(tot):
    th={3:'10°',7:'25°',11:'50°',16:'~75°',18:'90°'}
    if tot<3: return '<10°'
    if tot in th: return th[tot]
    if 3<tot<7: return 'tra 10° e 25°'
    if 7<tot<11: return 'tra 25° e 50°'
    if 11<tot<16: return 'tra 50° e 75°'
    if 16<tot<18: return 'tra 75° e 90°'
    return '>90°'
for k,row in zip(range(1,9), tabs['tab:babyfe_totali'][1:9]):
    d=R[k]; nv_an,tot_an=an[norm(CASI[k])]; tot_c,nv_c=tot_nv(d)
    att=['Caso %d'%k,str(d['età_mesi2026']),str(tot_an),str(nv_an),perc_label(tot_an)]
    chk(row==att,'Tabella 4.25 Caso %d: tex %s != atteso %s'%(k,row,att))
    chk((tot_c,nv_c)==(tot_an,nv_an),'Tabella 4.25 Caso %d: ricalcolo prove 2-14 (%d,%d) != foglio analisi (%d,%d)'%(k,tot_c,nv_c,tot_an,nv_an))
# ---------------- Tabella 4.26
means={'IC':stats['EEFQ_IC_MEDIA'][3],'FX':stats['EEFQ_FX_MEDIA'][3],'WM':stats['EEFQ_WM_MEDIA'][3],'RG':stats['EEFQ_RG_MEDIA'][3]}
sds={'IC':stats['EEFQ_IC_MEDIA'][4],'FX':stats['EEFQ_FX_MEDIA'][4],'WM':stats['EEFQ_WM_MEDIA'][4],'RG':stats['EEFQ_RG_MEDIA'][4]}
raw=[l for l in re.search(r'\\label\{tab:eefq\}(.*?)\\end\{tabular\}', t, re.S).group(1).split('\n') if '&' in l]
bold_cells=set()
for k,l in zip(range(1,9), raw[1:9]):
    cells=l.split('&')
    for j,c in enumerate(cells[1:5]):
        if '\\textbf' in c: bold_cells.add((k,['IC','FX','WM','RG'][j]))
for k,row in zip(range(1,9), tabs['tab:eefq'][1:9]):
    vals=ee[norm(CASI[k])]
    att=['Caso %d'%k]+[r1(v) if v is not None else 'n.d.' for v in vals]
    chk(row==att,'Tabella 4.26 Caso %d: tex %s != excel %s'%(k,row,att))
    for j,sc in enumerate(['IC','FX','WM','RG']):
        v=vals[j]
        if v is None: continue
        low = v <= means[sc]-sds[sc] + 1e-9
        low_r = float(r1(v).replace(',','.')) <= float(r1(means[sc]-sds[sc]).replace(',','.'))
        chk(((k,sc) in bold_cells)==low_r,'Tabella 4.26 Caso %d %s: grassetto=%s ma valore %s vs soglia %.2f (arrot. %s)'%(k,sc,(k,sc) in bold_cells,r1(v),means[sc]-sds[sc],r1(means[sc]-sds[sc])))
chk(tabs['tab:eefq'][9]==['Media campione totale']+[r1(means[s]) for s in ['IC','FX','WM','RG']],'Tabella 4.26 riga Media: %s'%tabs['tab:eefq'][9])
chk(tabs['tab:eefq'][10]==['DS campione totale']+[r1(sds[s]) for s in ['IC','FX','WM','RG']],'Tabella 4.26 riga DS: %s'%tabs['tab:eefq'][10])
# ---------------- percentili EEFQ 10°/20° e Baby-FE dal dataset completo
def pct(vals,p,method):
    v=sorted(vals); n=len(v)
    if method=='spss':  # weighted average x(n+1)p
        r=(n+1)*p; i=int(math.floor(r)); f=r-i
        if i<1: return v[0]
        if i>=n: return v[-1]
        return v[i-1]+f*(v[i]-v[i-1])
    if method=='excel_inc':
        r=1+(n-1)*p; i=int(math.floor(r)); f=r-i
        return v[i-1]+f*(v[i]-v[i-1]) if i<n else v[-1]
note=re.search(r'10° e al 20° percentile[^:]*: (.*?)\. Tali', t).group(1)
print('NOTA 4.26 nel tex:', note)
for sc,col in [('IC','EEFQ_IC_MEDIA'),('FX','EEFQ_FX_MEDIA'),('WM','EEFQ_WM_MEDIA'),('RG','EEFQ_RG_MEDIA')]:
    vals=[d[col] for d in D if isinstance(d[col],(int,float))]
    print('  %s (n=%d): 10°/20° spss = %s / %s ; excel.inc = %s / %s'%(sc,len(vals),r1(pct(vals,.10,'spss')),r1(pct(vals,.20,'spss')),r1(pct(vals,.10,'excel_inc')),r1(pct(vals,.20,'excel_inc'))))
tots=[]
for d in D:
    vals=[pv(d,p) for p in PROVE[1:14]]
    if all(v is None for v in vals): continue
    tots.append(sum(v for v in vals if v in (0,1,2)))
print('Baby-FE totali ricalcolati su %d bambini: percentili 10/25/50/75/90 spss = %s ; excel.inc = %s ; nota tex: 10=3 25=7 50=11 75=16 90=18'%(len(tots),[round(pct(tots,p,'spss'),1) for p in (.1,.25,.5,.75,.9)],[round(pct(tots,p,'excel_inc'),1) for p in (.1,.25,.5,.75,.9)]))
# ---------------- campione (§4.2.1)
n=len(D); f=sum(1 for d in D if d['sex']==2); m=sum(1 for d in D if d['sex']==1)
ages=[d['età_mesi2026'] for d in D if isinstance(d['età_mesi2026'],(int,float))]
print('Campione: righe excel=%d, F=%d (%.0f%%), M=%d (%.0f%%), età %d-%d, media %.1f, DS %.1f'%(n,f,100*f/n,m,100*m/n,min(ages),max(ages),statistics.mean(ages),statistics.stdev(ages)))
bil=[d['bilingue'] for d in D if d['bilingue'] in (1,2)]; print('  bilingue: %.0f%% (su %d validi)'%(100*sum(1 for b in bil if b==2)/len(bil),len(bil)))
nat=[d['dove nato'] for d in D if d['dove nato'] in (1,2)]; print('  nati in Italia: %.0f%%'%(100*sum(1 for b in nat if b==1)/len(nat)))
eg=[d['età_genit'] for d in D if isinstance(d['età_genit'],(int,float))]; ea=[d['età_altro'] for d in D if isinstance(d['età_altro'],(int,float))]
print('  età genitori: %.1f e %.1f'%(statistics.mean(eg),statistics.mean(ea)))
from collections import Counter
print('  istruzione (moda):', Counter(d['istruz'] for d in D).most_common(2), ' reddito:', sorted(Counter(d['reddito'] for d in D if d['reddito']).items()))
tex421=re.search(r'Il campione inizialmente previsto.*?Genova\.', t, re.S).group(0)
for s in ['70 bambini','66 bambini','38 femmine (58\\%)','28 maschi (42\\%)','tra i 18 e i 38 mesi','29,2 mesi','DS = 4,8','quattro asili nido']: chk(s in tex421,'§4.2.1: manca «%s»'%s)
tex422=re.search(r'Una quota consistente.*?medio-bassi\.', t, re.S).group(0)
for s in ['64\\%','97\\%','34 e 38 anni','diploma di scuola superiore']: chk(s in tex422,'§4.2.1 bis: manca «%s»'%s)
# ---------------- affermazioni numeriche della prosa (4.3.3 / 4.4)
totali={k:an[norm(CASI[k])][1] for k in CASI}; nvs={k:an[norm(CASI[k])][0] for k in CASI}
chk(min(totali.values())==0 and max(totali.values())==16,'prosa: range totali')
chk(sum(1 for v in totali.values() if v<=7)==6,'prosa: sei casi entro il 25°'); chk(sorted(k for k,v in totali.items() if v<3)==[2,3,4],'prosa: tre casi sotto il 10°')
chk(min(nvs.values())==0 and max(nvs.values())==13,'prosa: range prove non valide')
chk((totali[7],totali[6],totali[8])==(3,12,4) and (totali[4],totali[5])==(1,7),'prosa: punteggi per età')
chk((R[7]['età_mesi2026'],R[6]['età_mesi2026'],R[8]['età_mesi2026'])==(27,28,29) and (R[4]['età_mesi2026'],R[5]['età_mesi2026'])==(37,38),'prosa: età 27-29 e 37-38')
chk(nvs[8]==5 and nvs[5]==3 and nvs[2]==13 and nvs[4]==1 and nvs[3]==0,'prosa: prove non valide citate (Casi 8, 5, 2, 4, 3)')
print('\nCONTROLLI SUPERATI: %d   PROBLEMI: %d'%(ok,len(err)))
for e in err: print('  !!', e)
