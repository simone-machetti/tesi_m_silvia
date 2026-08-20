# Bibliografia — punti da controllare

Elenco delle anomalie trovate confrontando le citazioni nel testo dei 4 capitoli con
l'elenco di `source/bibliografia.docx`.

**Niente di quanto segue è stato corretto.** La migrazione riproduce il Word così com'è;
questa è la lista di cose da sistemare nel controllo di contenuto.

La bibliografia in LaTeX è `tesi/tail/References.bib`: 99 voci reali (dall'elenco
alfabetico del Word) + 7 segnaposto, per un totale di 106.

---

## 1. Citazioni nel testo senza voce in bibliografia

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

**Da fare:** completare le 7 voci segnaposto in `References.bib` con i dati bibliografici
reali, oppure rimuovere le citazioni dal testo.

---

## 2. Il caso Astle: due voci con lo stesso anno

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

**Da controllare:** con ogni probabilità la voce B è in realtà del **2022** (JCPP, 63(4)) ed
è quella a cui si riferiscono le 15 citazioni `Astle et al., 2022`. Se è così, basta
correggere l'anno della voce B, ripuntare le citazioni su `astle2021b` ed eliminare il
segnaposto `astle2022`. **Non l'ho fatto io perché è una modifica di contenuto.**

---

## 3. Vygotskij / Vygotsky — stessa opera, due grafie

- In bibliografia: `Vygotsky, L. S. (1962). Thought and language. MIT Press.`
- Nel testo (cap. 2, 1 occorrenza): `(Vygotskij, 1962; Zelazo, 2015; Vallotton & Ayoub, 2011)`

È la stessa opera con la traslitterazione italiana del cognome. Ho agganciato la citazione
alla voce esistente `vygotsky1962` invece di creare un doppione. **Da controllare** se si
vuole uniformare la grafia.

---

## 3-bis. `Rothbart et al., 2003` — aggancio dedotto dal contesto

Nel capitolo 3 compare una volta la citazione `(Rothbart et al., 2003)`, che non
corrisponde a nessuna voce con quella forma. Nel contesto — un elenco di questionari
sul temperamento e sull'*effortful control* — e considerato che poche righe prima lo
stesso capitolo cita `(IBQ-R; Gartstein & Rothbart, 2003)`, si tratta quasi certamente
della stessa opera.

L'ho quindi agganciata alla voce esistente **Gartstein & Rothbart (2003)** invece di
creare un segnaposto. È l'unico aggancio dedotto dal contesto in tutta la migrazione:
**da confermare**, ed eventualmente da uniformare anche nel testo.

---

## 4. Voci in bibliografia mai citate nel testo

Restano stampate nel PDF (vedi nota sotto), ma nessun punto del testo le richiama:

- **Fletcher-Watson, S. (2022)** — *Evidence-based practice and neurodiversity*, Autism, 26(1), 3–5
- **Astle et al. (2021)**, voce B — vedi punto 2

---

## 5. Refusi nelle voci, riprodotti così come sono

| Voce | Problema |
|---|---|
| `Karreman et al. (2006)` | intervallo di pagine scritto `561 579`, senza trattino |
| `Gandolfi et al. (2014)` | unica voce in formato Frontiers invece che APA: `Gandolfi E, Viterbori P, Traverso L and Usai MC (2014) … Front. Psychol. 5:381` |
| `Meins et al. (2001)` | autori indicati come `Meins, E., et al.`, senza l'elenco completo |
| `Miyake et al. (2000)` | il testo del link DOI è scritto `htps://doi.org/…` (manca la *t*); l'indirizzo vero dietro il link è però corretto, quindi in `References.bib` il DOI è giusto |
| `Berni et al. (2025)` | titolo in corsivo e senza volume/pagine (articolo probabilmente ancora *online first*) |
| `Ursache et al. (2012)` | manca volume, numero e pagine |
| `McClelland & Cameron (2012)` | nel Word la voce è spezzata su due righe da un a-capo manuale |

---

## 6. Ordine della bibliografia

L'elenco del Word **non è perfettamente alfabetico**: ci sono alcune inversioni, per esempio

- `Caspi` prima di `Carlson`
- `Diamond` → `Doebel` → `Degnan`
- `Garon` → `Gardiner` → `Gartstein`
- `Samson` prima di `Sameroff`

Ho mantenuto **l'ordine esatto del Word**, inversioni comprese, invece di riordinare
alfabeticamente. Se preferisci l'ordinamento automatico si cambia con una riga.

---

## 7. Scelte tecniche adottate (segnalate, non decise di nascosto)

- **`\nocite{*}` in `main.tex`** — con lo stile IEEE verrebbero stampate solo le voci
  effettivamente citate, e la bibliografia scenderebbe da 99 a ~97 voci. Con `\nocite{*}`
  vengono stampate tutte, nell'ordine del Word.
- **DOI e URL attivi** — il template di riferimento in `template/` li nasconde
  (`doi=false, url=false`). Li ho attivati perché nel Word i DOI ci sono e nasconderli
  significherebbe perdere contenuto. Si disattivano cambiando due parole in
  `tesi/settings/custom.tex`.
- **Sezione "BRUTTA BOZZA"** — le 30 righe in fondo a `bibliografia.docx` (con il blocco
  "PER CAPITOLO 2") non sono state riportate. Verificato: sono duplicati di voci già
  presenti nell'elenco pulito, nessun riferimento citato nel testo va perso.
- **Ordine dei numeri dentro una citazione multipla** — lo stile IEEE ordina i numeri in
  modo crescente, quindi `(Kopp, 1982; Calkins, 2007)` diventa `[15], [57]` e non
  `[57], [15]`. È il comportamento normale dello stile: cambia l'ordine dei numeri, non
  quali riferimenti sono citati.
- **`tail/ordine_bibliografia.tex`** — file generato automaticamente da `References.bib`.
  Serve solo a fissare l'ordine di stampa. Se aggiungi o sposti voci nel `.bib`, va
  rigenerato.

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
