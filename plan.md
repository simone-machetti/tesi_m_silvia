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

## 10. Controllo finale di grammatica, sintassi e titoli

È il punto più lungo: circa 51.000 parole nei quattro capitoli, più introduzione,
abstract, ringraziamenti e appendice. Finora il testo è stato **volutamente** lasciato
identico al Word, refusi compresi; questo è il momento in cui si interviene.

**Metodo:** un capitolo alla volta. Per ciascuno produco un elenco in `revisione.md`
con, per ogni punto: posizione, testo attuale, correzione proposta, motivo.
**Non applico nulla finché non approvi l'elenco.** Poi applico solo le voci approvate,
ricompilo e riverifico.

Cosa cerco:
- refusi e parole storpiate (già visti: «delyed gratification», «assesment», «in maniera
  causale» dove si intende *casuale*);
- apostrofi usati come accenti («E'» per «È»), doppi spazi, parentesi e virgolette non
  chiuse;
- accordi, concordanze, punteggiatura;
- coerenza dei titoli: maiuscole, punteggiatura finale, forma («Caso 1» vs «CASO 1»);
- rimandi interni: numeri di tabella, sezione e capitolo citati nel testo, dopo tutte le
  rinumerazioni fatte;
- coerenza terminologica (Baby-FE / Baby FE, EEFQ, BOI).

Cosa **non** faccio: riscrivere frasi per stile, cambiare il registro, toccare i
contenuti scientifici. Se una frase è corretta ma migliorabile, la segnalo a parte senza
proporre una modifica.

Conferme previste: una per capitolo (quattro), più una per front matter e appendice.

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
