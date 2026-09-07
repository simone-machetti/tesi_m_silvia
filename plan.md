# Piano delle modifiche — seconda fase

Modifiche richieste in `guideline/modifiche.docx`, con il materiale nei tre file a fianco
(`dediche.docx`, `Intro&Abstract.docx`, `4.3.3_4.4.1_rev.docx`). La cartella `guideline/`
si legge soltanto; ogni intervento va in `tesi/`.

**Metodo:** un punto alla volta, nell'ordine qui sotto. Dopo ciascuno: compilazione,
controllo del risultato, conferma dell'utente prima di passare al successivo.
Ogni testo aggiunto o modificato viene registrato in `tasks.md`, così le verifiche di
fedeltà in `strumenti/` sanno distinguere le modifiche volute dagli errori.

Stato di partenza: tesi di 180 pagine, compila pulita, quattro capitoli verificati parola
per parola contro il Word, bibliografia di 102 voci tutte citate, Appendice 1 completa.

**Decisioni già prese** (le domande aperte sono state risolte): vedi in ciascun punto.
Il nome dell'appendice è l'unico punto ancora in attesa di un'informazione, ed è stato
messo per ultimo. Undici punti in tutto.

---

## 1. Frontespizio

**File:** `tesi/head/1_frontespizio.tex`

| Campo | Valore |
|---|---|
| Corso di laurea | CORSO DI LAUREA IN Psicologia dello sviluppo tipico e atipico |
| Titolo | Profili di disregolazione nella prima infanzia: una prospettiva transdiagnostica per la valutazione precoce |
| Relatore | Prof.ssa Paola Viterbori |
| Correlatore | Prof.ssa Maria Carmen Usai |
| Candidato | Silvia Occhionero |
| Anno accademico | ANNO ACCADEMICO 2025 / 2026 |

**Deciso:** nome del corso in minuscolo (solo l'iniziale maiuscola), «Prof.ssa» per
entrambe le docenti.

**Layout:** oggi relatore, correlatore e candidato stanno in un unico blocco a destra.
Richiesto: relatore e correlatore **a sinistra**, candidato **a destra**. Due `minipage`
affiancate, allineate in alto.

---

## 2. Dedica

**File:** `tesi/head/2_dedica.tex`

Sostituire il segnaposto («Verba volant, scripta manent — Caius Titus») con la frase di
apertura da `dediche.docx`, in corsivo, su tre righe come nel Word:

> *Alla ricerca,*
> *che nasce dalla curiosità di osservare*
> *e dal desiderio di comprendere.*

---

## 3. Ringraziamenti

**File:** `tesi/head/3_ringraziamenti.tex`

Sostituire il testo latino segnaposto con i ringraziamenti di `dediche.docx`: 21
paragrafi, circa 1.450 parole. Testo riportato parola per parola; l'unico intervento è
la codifica LaTeX di virgolette e apostrofi.

**Deciso:** resta la riga di chiusura del template, «Genova, *data*» a sinistra e nome
della candidata a destra.

---

## 4. Abstract e Introduzione — come nel template di riferimento

**File:** `tesi/head/4_abstract.tex` (oggi «Sommario» con testo segnaposto), più un
nuovo file `tesi/main/0_introduzione.tex`.

Da `Intro&Abstract.docx`. Collocazione **verificata su `template/main.tex`**.

**Abstract — come nel template:** nel front matter, prima dell'indice, **due pagine
separate** (`\cleardoublepage` fra le due), ciascuna con il proprio `\chapter*`:
«Abstract» in italiano, poi «Abstract» in inglese. Il template usa **una sola voce
nell'indice** per entrambe le lingue («Abstract (English/Français)»): qui diventa
«Abstract (Italiano/English)».

**Introduzione — deciso:** nel corpo della tesi, prima del capitolo 1, come **capitolo
non numerato** (`\chapter*{Introduzione}` con voce nell'indice). Nel template
*Introduction* è invece il capitolo 1 numerato; qui si è scelto di non rinumerare i
quattro capitoli esistenti, così nessun numero di capitolo, sezione o tabella cambia.

In compenso i rimandi scritti a parole nel testo vengono resi automatici: è il **punto 9**.

Le sei citazioni dell'introduzione sono scritte nel Word come numeri della bibliografia
attuale. Corrispondenza già ricostruita, diventano `\cite` veri:

| Nel Word | Voce |
|---|---|
| `[2]` | Calkins (2007) |
| `[4]` | Blair & Raver (2015) |
| `[38]` | Beauchaine & Cicchetti (2019) |
| `[41]` | Astle et al. (2022) |
| `[85]` | McClelland & Cameron (2012) |
| `[78]` | Snyder et al. (2021) |

In entrambe le collocazioni queste sei opere diventano i riferimenti `[1]`–`[6]`
dell'intera tesi e la numerazione successiva slitta: automatico e corretto, la
bibliografia è in ordine di comparsa.

---

## 5. Togliere l'elenco degli acronimi

**File:** `tesi/main.tex`

Rimuovere la riga `\input{head/5_acronimi}`. Verificato: nessun capitolo usa il comando
`\ac{}`, la rimozione non rompe nulla. Il file `head/5_acronimi.tex` resta sul disco ma
non viene più incluso.

---

## 6. Testata del capitolo 3

**File:** `tesi/main/3_capitolo_3.tex`

Il titolo «La valutazione dell'autoregolazione nella prima infanzia (18–36 mesi e 3–6
anni)» è troppo lungo per la testata delle pagine e si sovrappone a «Capitolo 3».
Richiesto: togliere «(18–36 mesi e 3–6 anni)» **solo dalla testata**, lasciando intatti
titolo nella pagina di apertura e indice.

Tecnica: un `\chaptermark{...}` con il titolo breve subito dopo `\chapter{...}`. Agisce
solo sulle testate; indice e pagina di apertura non cambiano.

---

## 7. Appendice: «ETÀ IN MESI»

**File:** `strumenti/appendice.py` e `tesi/tail/appendice.tex`

Nel campo da compilare compare il testo spurio «ule2.4cm0.4pt» al posto della riga
orizzontale. Causa trovata: nel generatore, `\rule` era dentro una stringa Python non
*raw*, e `\r` è diventato un ritorno a capo. Lo stesso errore ha fatto sparire
l'apostrofo di «ETA'».

Correggere la stringa nel generatore e rigenerare l'appendice: la riga orizzontale torna a
disegnarsi, il testo spurio sparisce.

**Deciso:** l'accento corretto in italiano, quindi «**ETÀ** IN MESI».

---

## 8. Capitolo 4: integrare le sezioni revisionate

**File:** `tesi/main/4_capitolo_4.tex` — da `4.3.3_4.4.1_rev.docx`

Tre sostituzioni chirurgiche; il resto del capitolo non si tocca.

**Deciso:** il grassetto nel file di revisione marca le parti nuove. Si modificano solo
quelle, e nella tesi il grassetto **non** viene riportato.

| # | Dove | Cosa cambia | Come è marcato nel file |
|---|---|---|---|
| a | Nota sotto la Tabella 4.26 | Si aggiungono i punteggi del 10° e 20° percentile per IC, FX, WM, RG e la precisazione che sono riferimenti descrittivi interni al campione | **Nessun grassetto**: il file dà la nota completa come «definitiva». La parte nuova sono le ultime due frasi, individuate per confronto con la nota attuale |
| b | Sez. 4.3.3, paragrafo «Anche i punteggi dell'EEFQ…» | Tre frasi inserite nel mezzo, sulla collocazione dei casi rispetto al 10° e 20° percentile; prima e ultima frase invariate | In grassetto |
| c | Sez. 4.4.1, paragrafo «Un elemento di convergenza circoscritto…» | Una sola espressione: «inferiore alla media del campione totale» → «collocato tra il 10° e il 20° percentile della distribuzione osservata nel campione totale» | In grassetto |

Il file precisa che il corpo della Tabella 4.26 e il paragrafo successivo a (b) restano
invariati.

Dopo l'intervento: aggiornare `verify4.py` perché riconosca le tre sostituzioni come
volute, e ricontrollare che il resto del capitolo dia ancora 0 differenze.

---

## 9. Rimandi interni con `\ref`, così si aggiornano da soli

**File:** `tesi/main/1_capitolo_1.tex` … `4_capitolo_4.tex`

Nel testo del Word i rimandi a capitoli e sezioni sono scritti come parole
(«Capitolo 1», «sezione 2.4») e non si aggiornano se la numerazione cambia. Vanno
convertiti in `\ref` verso le etichette già presenti. Etichette **verificate, esistono
tutte**: `cap:uno`…`cap:quattro` per i capitoli, `sec:1_6`, `sec:2_4`, `sec:2_3_1`,
`sec:4_3_2`, `sec:4_3_3`, `sec:4_4_1` per le sezioni richiamate.

| Nel testo | Occorrenze | Diventa |
|---|---|---|
| «Capitolo 1» | 13 | `Capitolo~\ref{cap:uno}` |
| «Capitolo 2» | 3 | `Capitolo~\ref{cap:due}` |
| «Capitolo 3» | 3 | `Capitolo~\ref{cap:tre}` |
| «Capitoli 1, 2 e 3» | 1 | `Capitoli~\ref{cap:uno}, \ref{cap:due} e~\ref{cap:tre}` |
| «§1.6» | 1 | `§\ref{sec:1_6}` |
| «sezione 2.4», «sezione 2.3.1» | 2 | `sezione~\ref{sec:2_4}`, `sezione~\ref{sec:2_3_1}` |
| «Sezione 4.3.2», «sezione 4.3.3» | 2 | `Sezione~\ref{sec:4_3_2}`, `sezione~\ref{sec:4_3_3}` |
| «nella 4.4.1» | 3 | `nella~\ref{sec:4_4_1}` |

Circa 28 sostituzioni. I 27 rimandi alle tabelle sono già `\ref` dalla fase precedente.

**Nel PDF non cambia nulla:** i numeri stampati restano identici a oggi. Cambia solo che
da qui in avanti sopravvivono a qualunque rinumerazione. I due rimandi «Appendice 1»
restano fuori: dipendono dal nome che verrà scelto al punto 11.

Dopo l'intervento: le verifiche di fedeltà in `strumenti/` vanno istruite a leggere
`\ref{cap:uno}` come «1», altrimenti segnalerebbero 28 differenze fittizie.

---

## 10. Controllo finale

È il punto più lungo: circa 51.000 parole nei quattro capitoli, più introduzione, abstract,
ringraziamenti e appendice. Finora il testo è stato **volutamente** lasciato identico al
Word, refusi compresi; questo è il momento in cui si interviene.

### Metodo (rivisto con l'utente)

Un blocco alla volta, nell'ordine: controllo C sulle citazioni (meccanico, esito unico),
poi capitolo 1, 2, 3, 4, front matter (introduzione, abstract, ringraziamenti), appendice.

Per ogni capitolo:
- le correzioni **si applicano direttamente** nel `.tex`, senza attendere approvazione
  voce per voce — l'utente le segue con Git;
- ogni correzione viene **registrata in `cap_N.md`** (posizione, testo prima, testo dopo,
  categoria, motivo). I vecchi `cap_N.md`, che contenevano i rapporti di fedeltà della
  migrazione, vengono cancellati e i nomi riutilizzati per questo registro; i rapporti di
  fedeltà, che gli script rigenerano a ogni esecuzione, passano in `strumenti/`;
- i **dubbi** — correzioni non sicure, scelte di contenuto — non si applicano: si
  segnalano nel `cap_N.md` in una sezione «Da decidere» e si chiedono man mano;
- ogni correzione applicata entra anche fra le «revisioni volute» degli script di verifica,
  così il confronto con il Word continua a dare 0 differenze non previste;
- **a fine capitolo l'utente controlla e conferma**, poi si passa al successivo.

Quello che **non** si fa: riscrivere frasi per stile, cambiare registro o tono, toccare i
contenuti scientifici. Una frase corretta ma migliorabile viene segnalata senza modifica.

### Che cosa viene controllato

**A. Ortografia e refusi**
- parole storpiate (già viste: «delyed gratification», «assesment», «in maniera causale»
  per *casuale*), lettere doppie o mancanti, parole ripetute («il il»);
- accenti e apostrofi: «E'» per «È», «perchè» per «perché», apostrofi mancanti;
- spazi doppi, spazi prima della punteggiatura, parentesi e virgolette non chiuse.

**B. Grammatica e sintassi**
- accordi di genere e numero, concordanza soggetto-verbo, tempi verbali incoerenti;
- frasi sospese o senza verbo, ripetizioni ravvicinate della stessa parola;
- punteggiatura: virgola fra soggetto e verbo, punto mancante a fine paragrafo, uso dei
  due punti e del punto e virgola.

**C. Citazioni e riferimenti**
- **Aggancio di ogni citazione**: nuovo controllo indipendente, meccanico, che rilegge
  ogni «(Autore, anno)» del Word originale — circa 570 — e verifica che il `\cite`
  corrispondente punti a una voce con quell'autore e quell'anno. Fu fatto in migrazione;
  rifarlo da zero è un secondo paio d'occhi.
- **Rimandi interni**: ogni `\ref` a tabella, sezione, capitolo e appendice punta
  all'oggetto giusto (per esempio: nel testo del Caso 4 si rimanda alle tabelle del Caso 4).
- **Bibliografia**: uniformità delle voci (iniziali, punteggiatura, maiuscole nei titoli),
  nessuna voce doppia, nessun DOI o campo mancante dove gli altri ce l'hanno.

**D. Titoli**
- maiuscole e punteggiatura finale uniformi fra titoli dello stesso livello;
- **la sezione 4.4 manca**: esistono 4.4.1 e 4.4.2 senza un titolo padre, così anche nel
  Word. **Deciso e fatto (cap_4.md):** aggiunto il titolo «4.4 Discussione» prima di 4.4.1,
  allo stesso livello di «4.3 Risultati». Il contatore di sezione, prima forzato per far
  uscire 4.4.1 senza padre, scorre da solo;
- le 26 didascalie delle tabelle e le 23 frasi di raccordo, scritte da me nella fase
  precedente e mai rilette dall'utente (`tabelle.md`).

**E. Coerenza terminologica**
- Baby-FE / Baby FE, EEFQ, BOI, Bayley-III scritti sempre allo stesso modo;
- termini stranieri in corsivo in modo uniforme (*task impurity*, *school readiness*,
  *effortful control*, *hot/cool*…), o mai — **deciso al capitolo 3 (regola B):** corsivo
  solo per i nomi propri degli strumenti e delle loro sottoscale (*Early Childhood Behavior
  Questionnaire*, *Behavior Observation Inventory*…), tondo per tutti i termini stranieri
  comuni; titoli e didascalie sempre in tondo. Applicata a tutta la tesi (`cap_3.md`);
- **acronimi**: tolto l'elenco, ogni sigla dev'essere sciolta alla prima occorrenza
  (EEFQ, BOI, IC, FX, WM, RG, ADHD, FE, DS…).

**F. Numeri e dati** — su **tutti gli otto casi**, non a campione.
- coerenza fra prosa e tabelle: i valori citati nel testo (punteggi, percentili, numero
  di prove non valide, età, N del campione) devono coincidere con quelli in tabella;
- formato dei numeri: virgola decimale, spazi nelle percentuali, intervalli con il
  trattino giusto (18–36).

**G. Impaginazione residua** (solo segnalazioni, si sistemano insieme)
- righe isolate a inizio o fine pagina (vedove e orfane) — **fatto al capitolo 1**, su
  decisione dell'utente: vietate in tutta la tesi da `settings/custom.tex` (vedi `cap_1.md`,
  correzione 13);
- un titolo come ultima riga di una pagina;
- parole spezzate male a fine riga: nomi propri, sigle, termini inglesi («Baby-/FE»);
- pagine quasi vuote non giustificate.

**H. Front matter, introduzione, abstract, appendice**
- stessi controlli A-F su introduzione, abstract italiano e inglese, ringraziamenti;
- appendice: refusi nelle 15 tabelle e nella legenda, nomi delle prove coerenti con le
  tabelle del capitolo 4 («Oggetto nascosto (A-non-B)», «Torta nel forno»…);
- indice ed elenco delle tabelle completi e coerenti con il testo.

### Conferme previste

Una a fine blocco: quattro per i capitoli, una per il front matter, una per l'appendice,
più l'esito del controllo C sulle citazioni consegnato per primo.

**Controllo C: fatto**, esito in `controllo_citazioni.md` — 363 citazioni su 363
corrette, 36 rimandi tutti a bersaglio, bibliografia senza anomalie (più una citazione
rimasta in chiaro, trovata e convertita al capitolo 2: 364).

### Stato finale (7/9/2026): punto 10 completato

Tutti i blocchi controllati e confermati dall'utente, nell'ordine previsto. Verbali:
`cap_1.md`, `cap_2.md`, `cap_3.md`, `cap_4.md`, `cap_0.md` (front matter), `cap_A.md`
(appendice); ogni verbale elenca le correzioni applicate (posizione, prima, dopo,
categoria, motivo), i dubbi sottoposti e le decisioni prese, i controlli senza rilievi.

In sintesi:
- capitoli 1–3: residui di Word (grassetti su punteggiatura, spazi unificatori), tre refusi
  («assesment», «nei bambini ritardo globale», «seconda infanzia»), una citazione
  autore-anno rimasta in chiaro, uniformità («un'elevata», «comorbidità», «Blair e
  Raver», «p factor» in tondo), due ripetizioni riscritte; regola dei corsivi (B) per tutta
  la tesi; vedove e orfane vietate ovunque (`settings/custom.tex`);
- capitolo 4: titolo «4.4 Discussione», nome dell'EEFQ al plurale, rimandi «nella sezione
  4.4.1», Tabella 4.1 con le visite sdoppiate (verificato sui dati grezzi), Tabella 4.26
  con le righe di riferimento in tondo, percentili in cifre, DS sciolta; tutti i numeri
  degli otto casi confrontati con i due Excel (`strumenti/controllo_dati_cap4.py`, 620
  controlli, 0 discrepanze);
- front matter: «Candidata:»; appendice: 24 correzioni di forma e legenda ricomposta.
- Sillabazione: eccezioni per «scoring», «EEFQ», «Inventory», «Questionnaire» registrate
  nella lingua giusta con `\babelhyphenation`; «Baby-FE» e «Sonuga-Barke» non più spezzati.

Scansione finale del PDF (185 pagine, 0 errori, 0 Overfull, 0 avvisi LaTeX e biber, dopo
il ripasso del log descritto in `tasks.md`, «Errata»: i conteggi precedenti erano falsati
da un `grep` difettoso): nessuna vedova od orfana, nessun titolo in fondo a pagina,
nessuna citazione autore-anno in chiaro, nessuna sigla spezzata («Sonuga-Barke» torna
divisibile al trattino per non uscire dal margine); le 26 tabelle del capitolo 4 sulla
pagina del primo richiamo o su quella dopo; i quattro capitoli a 0 differenze rispetto al
Word con le revisioni registrate. Restano com'erano, su decisione dell'utente: nota sul totale a 13
prove (Tabella 4.25), soglie del 10°/20° percentile dell'EEFQ e «circa 34 e 38 anni»
(§4.2.1), EEFQ come sigla negli abstract, «di costituire» (Appendice, Tabella 6).

---

## 11. Nome dell'appendice, uniforme in indice, testo e appendice

**Per ultimo**, in attesa del messaggio WhatsApp con il nome da usare.

Oggi il nome compare in tre forme diverse:

| Dove | Oggi |
|---|---|
| Indice | «A Protocollo di somministrazione e scoring del Baby-FE» |
| Capitolo 3, due rimandi (sez. 3.7.3 e 3.8) | «Appendice 1» |
| Titolo dell'appendice | «Protocollo di somministrazione e scoring del Baby-FE», lettera A |

A seconda del nome scelto cambia la tecnica: se resta la lettera («Appendice A»), basta
allineare i due rimandi nel testo; se serve il numero («Appendice 1»), va cambiata la
numerazione delle appendici da lettere a cifre. In entrambi i casi i due rimandi nel
capitolo 3 diventano `\ref{app:babyfe}`, come al punto 9.
