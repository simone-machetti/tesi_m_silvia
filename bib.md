# Bibliografia — anomalie del materiale di partenza

Elenco delle anomalie trovate confrontando le citazioni nel testo dei 4 capitoli con
l'elenco di `source/bibliografia.docx`.

> **Stato: tutti i punti sono stati risolti.** Le decisioni prese, con le fonti della
> verifica e il dettaglio degli interventi, sono in [tasks.md](tasks.md). Questo file
> resta come registro di che cosa non tornava nel materiale di partenza.

La bibliografia in LaTeX è `tesi/tail/References.bib`: era di 99 voci reali + 7 segnaposto
(106 in tutto), ora è di **102 voci reali, verificate e tutte citate**.

---

## 1. Citazioni nel testo senza voce in bibliografia — RISOLTO

Otto citazioni compaiono nel testo ma non hanno una voce corrispondente nell'elenco del
Word. Con lo stile numerico IEEE ogni citazione deve agganciarsi a una voce, quindi ho
creato una **voce segnaposto** contenente solo autore e anno come compaiono nel testo.
Nessun titolo, rivista o pagina è stato inventato: nel PDF quelle voci appaiono come
`[VOCE MANCANTE — citata nel testo come "…"]`.

| # | Citazione nel testo | Dove | Occorrenze | Chiave segnaposto |
|---|---|---|---|---|
| 1 | `Astle et al., 2022` | cap. 2 (13), cap. 3 (2) | **15** | `astle2022` |
| 2 | `Zelazo et al., 2003` | cap. 3 | 2 | `zelazo2003` |
| 3 | `Friedman & Miyake, 2017` | cap. 3 | 2 | `friedman2017` |
| 4 | `Calkins & Fox, 2002` | cap. 3 | 1 | `calkins2002fox` |
| 5 | `Blair & Ursache, 2011` | cap. 3 | 1 | `blair2011ursache` |
| 6 | `Beauchaine & McNulty, 2013` | cap. 3 | 1 | `beauchaine2013mcnulty` |
| 7 | `Bayley, 2006` | cap. 4 | 1 | `bayley2006` |
| 8 | `Vygotskij, 1962` | cap. 2 | 1 | *nessuno* — vedi punto 3 |

**Risolto** (tasks.md, punti 1 e 2): i riferimenti reali sono stati identificati dal
contesto di ciascuna citazione e verificati su PubMed, Wiley e Springer. Tutti e sette i
segnaposto sono spariti. `Vygotskij, 1962` è confluito nel punto 3.

---

## 2. Il caso Astle: due voci con lo stesso anno — RISOLTO

Nell'elenco del Word ci sono **due voci Astle et al. datate 2021**:

| Voce | Titolo | Rivista |
|---|---|---|
| A | Annual research review: Transdiagnostic approaches to mental health problems in childhood and adolescence | JCPP, 62(8), 922–943 |
| B | Annual research review: The transdiagnostic revolution in neurodevelopmental disorders | JCPP, 62(4), 397–417 |

Il testo però cita **sia `Astle et al., 2021` (12 volte) sia `Astle et al., 2022` (15 volte)**.

Come deciso, ho tenuto le tre cose separate senza fare ipotesi:

- `Astle et al., 2021` nel testo → voce **A** (chiave `astle2021`)
- voce **B** (chiave `astle2021b`) resta in bibliografia con l'anno 2021 come nel Word,
  ma **non è citata da nessun punto del testo**
- `Astle et al., 2022` nel testo → voce segnaposto separata (chiave `astle2022`)

**Risolto** (tasks.md, punto 1). La verifica online ha mostrato che di articoli Astle ne
esiste **uno solo**: *The transdiagnostic revolution in neurodevelopmental disorders*,
JCPP 63(4), 397–417, **2022**, DOI `10.1111/jcpp.13481`, pubblicato online nel luglio 2021
e a stampa nel 2022 — da qui la doppia datazione nel testo. La voce A non corrisponde a
nessuna pubblicazione e il suo DOI appartiene a un altro articolo. Le due voci sono state
unificate in una sola, datata 2022, su cui puntano tutte e 27 le citazioni.

---

## 3. Vygotskij / Vygotsky — stessa opera, due grafie — RISOLTO

- In bibliografia: `Vygotsky, L. S. (1962). Thought and language. MIT Press.`
- Nel testo (cap. 2, 1 occorrenza): `(Vygotskij, 1962; Zelazo, 2015; Vallotton & Ayoub, 2011)`

È la stessa opera con la traslitterazione italiana del cognome. La citazione era già
agganciata alla voce esistente, senza doppioni. **Risolto** (tasks.md, punto 3): la voce è
ora stampata con la grafia italiana `Vygotskij`, coerente con quella usata nel testo.

---

## 3-bis. `Rothbart et al., 2003` — aggancio dedotto dal contesto — CONFERMATO

Nel capitolo 3 compare una volta la citazione `(Rothbart et al., 2003)`, che non
corrisponde a nessuna voce con quella forma. Nel contesto — un elenco di questionari
sul temperamento e sull'*effortful control* — e considerato che poche righe prima lo
stesso capitolo cita `(IBQ-R; Gartstein & Rothbart, 2003)`, si tratta quasi certamente
della stessa opera.

L'ho quindi agganciata alla voce esistente **Gartstein & Rothbart (2003)** invece di
creare un segnaposto. **Confermato** (tasks.md, punto 3). Resta facoltativo uniformare
anche il testo, che però con lo stile numerico non produce differenze visibili.

---

## 4. Voci in bibliografia mai citate nel testo — RISOLTO

Nessun punto del testo le richiama:

- **Fletcher-Watson, S. (2022)** — *Evidence-based practice and neurodiversity*, Autism,
  26(1), 3–5. **Rimossa** (tasks.md, punto 4).
- **Astle et al. (2021)**, voce B — **risolta** con l'unificazione del punto 2.
- **Zelazo, Blair & Willoughby (2020)** — *Executive function: Implications for education*
  (NCER 2017-2000). **Emersa dopo**: nell'analisi iniziale non era stata rilevata perché il
  `\nocite` forzato la faceva comunque comparire nel PDF. **Rimossa** anch'essa.

Dopo questi interventi le voci del `.bib` e le citazioni del testo coincidono esattamente:
102 voci, 102 citate.

---

## 5. Refusi nelle voci — RISOLTO

| Voce | Problema |
|---|---|
| `Karreman et al. (2006)` | intervallo di pagine scritto `561 579`, senza trattino |
| `Gandolfi et al. (2014)` | unica voce in formato Frontiers invece che APA: `Gandolfi E, Viterbori P, Traverso L and Usai MC (2014) … Front. Psychol. 5:381` |
| `Meins et al. (2001)` | autori indicati come `Meins, E., et al.`, senza l'elenco completo |
| `Miyake et al. (2000)` | il testo del link DOI è scritto `htps://doi.org/…` (manca la *t*); l'indirizzo vero dietro il link è però corretto, quindi in `References.bib` il DOI è giusto |
| `Berni et al. (2025)` | titolo in corsivo e senza volume/pagine (articolo probabilmente ancora *online first*) |
| `Ursache et al. (2012)` | manca volume, numero e pagine |
| `McClelland & Cameron (2012)` | nel Word la voce è spezzata su due righe da un a-capo manuale |

**Risolto** (tasks.md, punto 5). Tre voci si erano già normalizzate durante la migrazione
(`Gandolfi`, `Miyake`, `McClelland`). Le altre quattro sono state corrette e verificate su
fonte: `Karreman` (pagine), `Meins` (anno 2002 e volume 73, autori completi, titolo),
`Ursache` (titolo completo, volume, numero, pagine), `Berni` (ordine autori e forma
*online first*).

---

## 6. Ordine della bibliografia — RISOLTO

L'elenco del Word **non è perfettamente alfabetico**: ci sono alcune inversioni, per esempio

- `Caspi` prima di `Carlson`
- `Diamond` → `Doebel` → `Degnan`
- `Garon` → `Gardiner` → `Gartstein`
- `Samson` prima di `Sameroff`

Ho mantenuto **l'ordine esatto del Word**, inversioni comprese, invece di riordinare
alfabeticamente. **Risolto** (tasks.md, punto 6): la bibliografia è ora numerata
nell'ordine in cui le opere compaiono nel testo, comportamento predefinito dello stile
IEEE. Le inversioni non si pongono più e il file di ordinamento forzato è stato eliminato.

---

## 7. Scelte tecniche adottate (segnalate, non decise di nascosto) — RISOLTE

- **`\nocite{*}` in `main.tex`** — serviva a stampare anche le voci mai citate. Dopo
  l'unificazione di Astle e la rimozione di Fletcher-Watson non serve più: **eliminato**
  insieme al file di ordinamento forzato (tasks.md, punto 6).
- **DOI e URL attivi** — il template di riferimento in `template/` li nasconde
  (`doi=false, url=false`). **Ora nascosti anche qui** (tasks.md, punto 7): i DOI restano
  in `References.bib`, semplicemente non vengono stampati.
- **Sezione "BRUTTA BOZZA"** — le 30 righe in fondo a `bibliografia.docx` (con il blocco
  "PER CAPITOLO 2") non sono state riportate. Verificato: sono duplicati di voci già
  presenti nell'elenco pulito, nessun riferimento citato nel testo va perso.
- **Ordine dei numeri dentro una citazione multipla** — lo stile IEEE ordina i numeri in
  modo crescente. Con la numerazione per ordine di comparsa, `(Kopp, 1982; Calkins, 2007)`
  — la prima citazione della tesi — è diventata `[1], [2]`.
- **`tail/ordine_bibliografia.tex`** — **eliminato**. Serviva a forzare l'ordine del Word e
  andava rigenerato a ogni modifica del `.bib`. Con la numerazione in ordine di citazione
  non serve piu' alcuna manutenzione.

---

## 8. Numeri della migrazione

| | citazioni nel testo | riferimenti richiamati |
|---|---|---|
| Capitolo 1 | 67 gruppi | 96 |
| Capitolo 2 | 142 gruppi | 223 |
| Capitolo 3 | 144 gruppi | 234 |
| Capitolo 4 | 10 gruppi | 16 |
| **Totale** | **363 gruppi** | **569** |

Tutte convertite, nessuna lasciata indietro: il convertitore si ferma con errore se
incontra una citazione che non sa agganciare a una voce di `References.bib`.
