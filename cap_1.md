# Capitolo 1 — controllo finale (punto 10)

File: `tesi/main/1_capitolo_1.tex` (pagine stampate 3–22). Word di riferimento: `source/capitolo_1.docx`.
Metodo (vedi `plan.md`, punto 10): lettura integrale degli 80 capoversi, controlli
meccanici A–H, correzioni sicure applicate direttamente e registrate qui, dubbi nella
sezione «Da decidere» e chiesti all'utente. Dopo ogni modifica: ricompilazione e verifica
di fedeltà (`strumenti/verifica_cap_1.md`).

**Stato:** tutte le correzioni applicate, comprese le quattro decise dall'utente il 6/9/2026.

## Correzioni applicate

Le correzioni 1–9 sono di sola forma (nessuna parola cambia). Le 10–12 cambiano il testo e
sono registrate come «revisioni» in `strumenti/vcfg1.json`, così la verifica di fedeltà
resta a **0 differenze**. La 13 è un'impostazione globale in `settings/custom.tex`.

| N. | Posizione | Prima | Dopo | Categoria | Motivo |
|---|---|---|---|---|---|
| 1 | §1.1, 3° capoverso | «poco mediato**,** nonché» | «poco mediato, nonché» | refuso tipografico | virgola in grassetto: residuo di Word (nel .docx la virgola ha `<w:b/>` mentre le parole intorno hanno `w:b val=0`) |
| 2 | §1.1, 3° capoverso | «del contesto**,** sostenute» | «del contesto, sostenute» | refuso tipografico | idem |
| 3 | §1.4, 1° capoverso | «funzioni esecutive (FE)**,** considerate» | «(FE), considerate» | refuso tipografico | idem |
| 4 | §1.4, 3° capoverso | «(unity and diversity)**.** Secondo» | «(unity and diversity). Secondo» | refuso tipografico | punto in grassetto, stesso residuo |
| 5 | §1.4, 3° capoverso | «controllo inibitorio**,** memoria di lavoro **e** flessibilità cognitiva**.**» | «controllo inibitorio, memoria di lavoro e flessibilità cognitiva.» | refuso tipografico | virgola, congiunzione e punto in grassetto |
| 6 | §1.4, 4° capoverso | «Diamond [9]**,** che distingue» | «Diamond [9], che distingue» | refuso tipografico | idem |
| 7 | §1.4, 6° capoverso | «“cool” e “hot”**,** evidenziando» | «“cool” e “hot”, evidenziando» | refuso tipografico | idem |
| 8 | §1.4, 10° capoverso | «(3–6 anni)~si osserva» | «(3–6 anni) si osserva» | spazio | spazio unificatore (`~`, dal «no-break space» di Word) al posto di uno spazio normale: invisibile a stampa ma impedisce l'a capo in quel punto |
| 9 | §1.5, 7° capoverso | «del comportamento,~rappresenta» | «del comportamento, rappresenta» | spazio | idem |
| 10 | §1.5, 8° capoverso | «che emergono nella seconda infanzia» | «che emergono nella prima infanzia» | contenuto (deciso dall'utente) | in tutta la tesi 18–36 mesi è «prima infanzia»; «seconda infanzia» era l'unica occorrenza e indicava un'età sbagliata |
| 11 | §1.6.1, 2° capoverso | «una elevata intensità» | «un'elevata intensità» | uniformità (deciso dall'utente) | nel resto della tesi sempre «un'elevata» (5 volte) |
| 12 | §1.3, 8° capoverso | «proposto da Clancy Blair e Cybele Raver» | «proposto da Blair e Raver» | uniformità (deciso dall'utente) | unico autore citato nel testo con nome e cognome; ovunque altrove solo il cognome |
| 13 | tutta la tesi (`settings/custom.tex`) | vedove e orfane permesse | vedove e orfane vietate | impaginazione (deciso dall'utente) | vedi sotto |

In totale nel testo: 9 comandi `\textbf{}` su punteggiatura tolti (6 virgole, 2 punti, una
«e»), 2 spazi unificatori sostituiti, 3 ritocchi di parole. Nel capitolo non resta alcun
grassetto o corsivo nel corpo del testo, come nel Word.

### Correzione 13: vedove e orfane

Nel capitolo 1 c'erano tre vedove (ultima riga di un capoverso sola in cima a pagina 11,
18 e 21) e un'orfana (prima riga di un capoverso sola in fondo a pagina 14). In tutta la
tesi la stessa scansione ne trovava una ventina.

In `settings/custom.tex` i due parametri `\widowpenalty` e `\clubpenalty` sono ora a 10000
(divieto). Un primo tentativo con l'assegnazione semplice non aveva effetto: babel-italian
riporta i due valori a 3000 (solo «scoraggiate») ogni volta che seleziona l'italiano, cioè
a inizio documento e di nuovo dopo l'abstract inglese. Per questo l'impostazione è
agganciata a `\extrasitalian` (`\addto\extrasitalian{...}`), che viene eseguito in quei
momenti; un test con cambio di lingua conferma 10000 prima e dopo.

Effetto verificato sul PDF ricompilato: nessuna vedova o orfana in tutta la tesi (le due
sole righe segnalate dalla scansione sono nel frontespizio e in una cella di tabella
dell'appendice, non capoversi); 185 pagine come prima; tutte le 26 tabelle del capitolo 4
restano sulla stessa pagina del primo richiamo o su quella dopo, come prima; nessuna
riga troppo lunga.

## Da decidere

Nessun punto aperto.

## Controlli eseguiti senza rilievi

- **A. Ortografia e refusi.** Nessuna parola doppia, nessuno spazio doppio, nessuno spazio
  prima della punteggiatura, nessuna punteggiatura doppia; accenti corretti (perché, poiché,
  né, cioè, è/e); nessun apostrofo sbagliato (nessun «un'» davanti a maschile, nessun
  «qual'è»); parentesi e virgolette bilanciate. Le due sole virgolette del capitolo
  («unità e diversità», «cool»/«hot») sono virgolette alte doppie, come nel Word.
- **B. Grammatica e sintassi.** Letti tutti gli 80 capoversi: accordi, concordanze e tempi
  verbali corretti, nessuna frase sospesa, ogni capoverso chiuso dal punto.
- **C. Citazioni e rimandi.** Già fatto nel controllo C (`controllo_citazioni.md`): 67 gruppi
  di citazione nel Word e 67 `\cite` nel LaTeX, tutti agganciati alla voce giusta e tutti
  legati alla parola precedente con `~`. Nel capitolo non ci sono `\ref`.
- **D. Titoli.** 10 titoli (7 sezioni, 3 sottosezioni), identici al Word, tutti con la sola
  iniziale maiuscola e senza punto finale; nessun titolo cade come ultima riga di pagina.
- **E. Terminologia.** I termini stranieri sono tutti in tondo, come nel Word, che nel
  capitolo 1 non ha corsivi: bottom-up, top-down, caregiver, effortful control, situational
  compliance, committed compliance, cool, hot, problem solving, school readiness, scaffolding,
  mind-mindedness, framework, pattern, arousal, continuum, unity and diversity. Parole
  composte scritte sempre allo stesso modo in tutta la tesi: co-regolazione (mai
  «coregolazione»), auto-consolazione, socio-relazionali, emotivo-motivazionali,
  eteroregolazione, autocontrollo. Trattino lungo in «sonno–veglia», «caregiver–bambino» e in
  tutti gli intervalli (18–36, 24–36, 3–6, 3–4).
  **Acronimi:** l'unica sigla del capitolo è FE, sciolta alla prima occorrenza («funzioni
  esecutive (FE)», §1.4); dopo la definizione il capitolo continua a scrivere «funzioni
  esecutive» per esteso, quindi la sigla serve ai capitoli successivi.
- **F. Numeri.** Il capitolo non contiene dati; le fasce d'età (18–36 mesi, 24–36 mesi, 3–6
  anni, 3–4 anni) sono coerenti fra loro e con i titoli.
- **G. Impaginazione.** Nessuna pagina quasi vuota (la pagina 21, di 19 righe, è l'ultima del
  capitolo); nessuna sillabazione anomala di nomi propri, sigle o termini inglesi (l'unica
  parola con iniziale maiuscola spezzata è «Com-portamenti», pag. 20, regolare). Vedove e
  orfane: risolte con la correzione 13.

## Verifica finale

- Compilazione: 185 pagine, 0 errori, 0 righe troppo lunghe (Overfull), 0 avvisi biber.
- Fedeltà al Word: `strumenti/verifica_cap_1.md` → 10 titoli, 67 citazioni, **0 differenze**
  (con le 3 revisioni di testo registrate in `strumenti/vcfg1.json`); anche i capitoli 2, 3
  e 4 restano a 0 differenze dopo il cambio di impaginazione.
