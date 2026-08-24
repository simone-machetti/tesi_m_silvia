# Piano di migrazione: da Word (`source/`) a LaTeX (`tesi/`)

## Obiettivo

Trasferire i 4 capitoli e la bibliografia dai file Word in `source/` dentro il template
LaTeX in `tesi/`, **senza modificare nulla di testo, numeri, contenuto, sintassi o
grammatica**. Cambia solo la veste: font, impaginazione, tabelle rifatte in LaTeX.
Il controllo linguistico e di contenuto verrà fatto in un secondo momento.

La cartella `template/` è solo un riferimento di stile: il suo contenuto non viene usato.

---

## Materiale di partenza

| File | Contenuto | Parole | Tabelle | Immagini |
|---|---|---|---|---|
| `source/capitolo_1.docx` | 7 sezioni (1.1–1.7) + 3 sottosezioni (1.6.1–1.6.3) | 6.854 | 0 | 0 |
| `source/capitolo_2.docx` | 4 sezioni (2.1–2.4) + 11 sottosezioni | 11.619 | 0 | 0 |
| `source/capitolo_3.docx` | 8 sezioni (3.1–3.8) + 22 sottosezioni **+ APPENDICE 1** | 18.311 | 15 | 12 |
| `source/capitolo_4.docx` | 4.1–4.3 + 4.4.1/4.4.2, con 4.2.3.1–4.2.3.4 e 8 "Caso" | 14.688 | 26 | 0 |
| `source/bibliografia.docx` | 99 voci APA in lista pulita + 30 righe di "BRUTTA BOZZA" | 3.200 | – | – |
| `source/tabella.docx` | **duplicato esatto** dell'Appendice 1 già dentro `capitolo_3.docx` | – | 15 | 12 |
| `source/frontespizio.doc` | template UniGe **vuoto**, già replicato in `tesi/head/1_frontespizio.tex` | – | – | – |

Nessuna nota a piè di pagina, nessun elenco puntato o numerato in tutto il materiale:
solo paragrafi, titoli e tabelle.

Il template `tesi/` compila pulito (pdflatex + biber, 24 pagine) e ha già 4 file capitolo
che corrispondono 1:1 ai 4 capitoli del Word.

---

## Regole di lavoro fissate

- **Tabelle**: stile di quelle di esempio in `tesi/main/2_capitolo_2.tex`, cioè
  `\begin{tabular}{|l|c|c|c|}` **con le barre laterali**, più `\toprule` / `\midrule` /
  `\bottomrule` e intestazioni in `\bf{}`.
- **Impaginazione delle tabelle**:
  - **mai spezzate fra due pagine**. Unica eccezione: una tabella più alta di una pagina
    intera, e solo allora, viene divisa;
  - **flottanti**: se non entrano nel punto esatto in cui sono citate scivolano alla pagina
    vicina, e il testo scorre a riempire lo spazio. Meglio una tabella una pagina più avanti
    che mezza pagina bianca;
  - **vicine al testo che le commenta**: un `\FloatBarrier` prima di ogni sottosezione e di
    ogni «Caso» impedisce che escano dal punto che le descrive;
  - **le didascalie viaggiano dentro il flottante**, sopra o sotto la tabella a seconda di
    dov'erano nel Word, così non restano mai orfane;
  - l'aggiustamento è **solo tipografico**: nessuna parola spostata, riscritta o riordinata.
- **Citazioni**: numeriche IEEE (`\cite{...}`), come nella cartella `template/`.
  È l'**unica** eccezione concessa alla regola "non modificare il testo".
- **8 citazioni orfane** (senza voce in bibliografia): in fase di migrazione, voce
  segnaposto con i soli autore e anno ricavabili dal testo, senza inventare titoli.
  *Superato dalla fase 10:* i riferimenti reali sono stati identificati e inseriti.
- **Astle 2022**: in fase di migrazione, segnaposto separato dalle due voci "Astle 2021".
  *Superato dalla fase 10:* le voci sono state unificate in una sola, datata 2022.
- **Sezione "BRUTTA BOZZA"** in fondo a `bibliografia.docx`: scartata (materiale di lavoro,
  voci duplicate di quelle già presenti nella lista pulita).
- **Titolo capitolo 4**: *Analisi dei casi critici nei processi di regolazione tra i 18 e i
  36 mesi* (parentesi rimosse, iniziale maiuscola).
- **Front matter** (dedica, ringraziamenti, Sommario, Elenco acronimi): resta un breve
  testo in latino nelle sezioni vuote.
- **`tabella.docx`**: non usato, è il duplicato dell'Appendice.

---

## Assunzioni adottate

1. **Titoli capitolo**: rimosso il prefisso `CAPITOLO N –` perché il numero lo genera il
   template; il resto verbatim.
2. **Gerarchia**: `x.y` → `\section`, `x.y.z` → `\subsection`, `x.y.z.w` → `\subsubsection`.
   La numerazione automatica riproduce esattamente quella del Word.
3. **4.4.1 e 4.4.2 non hanno un "4.4" padre** nel Word: nessun titolo inventato, si forza il
   contatore così escono esattamente `4.4.1` e `4.4.2`.
4. **"Caso 1…8"**, "Scheda di sintesi", "Prestazione al Baby-FE", "Osservazione…" restano
   **non numerati**, come nel Word (titoli con `*`).
5. **Le 23 tabelle-caso non hanno didascalia** nel Word: restano senza `\caption` e quindi
   fuori dall'Elenco delle tabelle. Solo Tabella 4.1, 4.2, 4.3 hanno una didascalia, che
   viene riprodotta come `\caption`.
6. **`\listoffigures`** risulterebbe vuoto (le uniche immagini sono icone dentro le celle
   dell'Appendice): proposta di rimuoverlo. `\listoftables` mostrerà 3 voci.
7. In `4.2.3` diversi **paragrafi di testo corrente hanno per errore stile "Titolo 3"** nel
   Word: resi come testo normale.
8. Titoli con spazio mancante (`1.1I processi`, `1.3Principali`): il numero lo genera LaTeX,
   quindi lo spazio torna corretto senza toccare il testo.
9. Corsivi, grassetti e sottolineature del Word riprodotti 1:1.
10. Dati del frontespizio (titolo tesi, relatore, candidato, A.A.): restano i placeholder,
    nel `.doc` non c'è nessun dato.
11. ~~**`\nocite{*}`**: serve a stampare tutte le voci, comprese quelle mai citate.~~
    *Superata dalla fase 10:* eliminato, non essendoci più voci orfane da stampare.
12. ~~**Astle 2021**: le 12 citazioni agganciate alla prima delle due voci.~~
    *Superata dalla fase 10:* voci unificate, tutte e 27 le citazioni puntano lì.

---

## File di controllo consegnati

| File | Contenuto |
|---|---|
| `bib.md` | Registro delle anomalie del materiale di partenza: citazioni orfane, doppio Astle 2021, `Vygotskij`/`Vygotsky`, voci fuori formato, voci mai citate. **Tutti i punti sono stati poi risolti** nella fase 10. |
| `tasks.md` | Registro dei sette interventi sulla bibliografia decisi punto per punto, con le fonti della verifica e l'esito. |
| `cap_1.md` … `cap_4.md` | Diff paragrafo per paragrafo fra il testo del Word e il testo del LaTeX, normalizzato su spazi e virgolette. Se il capitolo è migrato correttamente il diff mostra **solo** le sostituzioni di citazione `(Kopp, 1982)` → `[12]`. Qualunque altra riga nel diff è un errore da correggere. |

---

## Problemi noti nel materiale di partenza

Rilevati durante l'analisi e lasciati inizialmente intatti perché sono contenuto.
**Risolti tutti nella fase 10**, uno per uno e con verifica su fonte: il dettaglio è in
`tasks.md`, il registro dei problemi in `bib.md`.

| Citazione nel testo | Occorrenze | Situazione |
|---|---|---|
| `Astle et al., 2022` | 15 | In bibliografia ci sono **due voci Astle 2021**; la seconda ("The transdiagnostic revolution…") è in realtà del 2022. |
| `Zelazo, 2003` | 2 | Voce assente in bibliografia |
| `Friedman & Miyake, 2017` | 2 | Voce assente in bibliografia |
| `Rothbart, 2003` | 1 | Voce assente in bibliografia |
| `Calkins & Fox, 2002` | 1 | Voce assente in bibliografia |
| `Blair & Ursache, 2011` | 1 | Voce assente in bibliografia |
| `Beauchaine & McNulty, 2013` | 1 | Voce assente in bibliografia |
| `Bayley, 2006` | 1 | Voce assente in bibliografia |
| `Vygotskij, 1962` | 1 | In bibliografia è `Vygotsky, 1962` (grafia diversa) |

Altri punti segnalati:

- La voce **Gandolfi et al. (2014)** in bibliografia è in formato Frontiers, non APA come
  tutte le altre.
- **Fletcher-Watson (2022)** e **Zelazo, Blair & Willoughby (2020)** sono in bibliografia
  ma non risultano mai citate nel testo (entrambe poi rimosse nella fase 10).
- Nel capitolo 4 manca l'intestazione di sezione **4.4**, pur essendoci 4.4.1 e 4.4.2.
- Il **Caso 2** ha 2 tabelle invece di 3: l'osservazione comportamentale non è disponibile.

---

## Stato di avanzamento

| # | Fase | Stato | Esito |
|---|---|---|---|
| 1 | Preparazione (pacchetti, immagini) | ✅ | 5 pacchetti aggiunti, 8 immagini in `tesi/images/` |
| 2 | Bibliografia | ✅ | 106 voci (99 reali + 7 segnaposto); riviste poi nella fase 10 |
| 3 | Capitolo 1 | ✅ | 10 titoli, 67 citazioni, **0 differenze** |
| 4 | Capitolo 2 | ✅ | 15 titoli, 142 citazioni, **0 differenze** |
| 5 | Capitolo 3 (Appendice esclusa) | ✅ | 30 titoli, 144 citazioni, **0 differenze** |
| 6 | Capitolo 4 | ✅ | 49 titoli, 26 tabelle, 10 citazioni, **0 differenze** |
| 7 | **Appendice 1** | ⏸ **in sospeso** | da decidere dove collocarla |
| 8 | Front matter e chiusura | ✅ | compila pulito, 161 pagine |
| 9 | Impaginazione delle tabelle | ✅ | 26 tabelle da `longtable` a flottante intero |
| 10 | Revisione delle citazioni | ✅ | 7 interventi sulla bibliografia, vedi `tasks.md` |

### Dettagli della fase 7 (da fare)

15 tabelle a 5 colonne con celle lunghe e icone inline. Sono le uniche tabelle della tesi
più alte di una pagina: per queste vale l'eccezione alla regola, cioè verranno divise
(`longtable` orizzontale). Le 8 immagini sono già estratte in `tesi/images/`:
`app_stella.png`, `app_item_opzionale.png`, `app_cronometro_1..4`, `app_stop_1..2`.

**Decisione aperta:** l'Appendice resta in fondo al capitolo 3 come nel Word, oppure
diventa un `\appendix` a fine tesi?

### Dettagli della fase 9 (fatta)

Le 26 tabelle del capitolo 4 erano `longtable`, che per costruzione si spezza fra le
pagine. Sono state riscritte come flottanti `table` + `tabular`: un flottante non si
spezza mai. Nessuna delle 26 supera l'altezza di una pagina, quindi non è stato necessario
dividerne nessuna. Verifica sul PDF: nessun avviso «Float too large», riempimento medio
delle pagine del capitolo 82,9% (era 82,5% con le `longtable`), 161 pagine invece di 163.

### Dettagli della fase 10 (fatta)

Revisione completa della bibliografia, condotta punto per punto con l'utente e registrata in
`tasks.md`: unificazione delle due voci Astle in una sola datata 2022, inserimento delle sei
voci citate ma assenti dal Word (identificate dal contesto e verificate su fonte), grafia
italiana per Vygotskij, rimozione della voce mai citata Fletcher-Watson, correzione di
Karreman, Meins, Ursache e Berni, numerazione in ordine di comparsa nel testo, DOI e URL
nascosti. La bibliografia passa da 106 voci (99 dal Word + 7 segnaposto) a **102 voci reali,
verificate e tutte citate**: voci del `.bib` e citazioni del testo coincidono esattamente.
Il testo dei capitoli non è cambiato: le verifiche in `strumenti/` danno 0 differenze su
tutti e quattro.

### Modifiche al template rispetto alla versione di partenza

- `settings/custom.tex`: aggiunti `longtable`, `tabularx`, `makecell`, `ragged2e`,
  `pdflscape`, `xurl`, `placeins`; DOI e URL attivati in biblatex; `\paragraph` reso titolo
  a blocco; parametri di posizionamento dei flottanti allargati (`\topfraction` 0.9,
  `\bottomfraction` 0.8, `\textfraction` 0.07, `\floatpagefraction` 0.75, fino a 5 tabelle
  per pagina) perché una tabella spostata non lasci vuoti.
- `main.tex`: `\listoffigures` commentato (nessuna figura nei capitoli).
- `tail/biblio.tex`: aggiunto `\emergencystretch` per i DOI lunghi.
- `head/`: tolto il `\cite` di esempio dal Sommario, accorciati i testi in latino,
  commentati i segnaposto.
