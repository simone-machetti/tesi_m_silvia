# Front matter e introduzione — controllo finale (punto 10)

File: `tesi/head/1_frontespizio.tex`, `tesi/head/2_dedica.tex`, `tesi/head/3_ringraziamenti.tex`,
`tesi/head/4_abstract.tex` (italiano e inglese), `tesi/main/0_introduzione.tex`, più indice ed
elenco delle tabelle generati da LaTeX. Word di riferimento: `guideline/dediche.docx`
(ringraziamenti e frase di apertura), `guideline/Intro&Abstract.docx` (introduzione e i due
abstract), `source/frontespizio.doc` (frontespizio).
Metodo (vedi `plan.md`, punto 10, H): stessi controlli A–G dei capitoli, più confronto
parola per parola con i Word e verifica di indice, elenco delle tabelle e numerazione
delle pagine sul PDF.

**Stato:** controllato e confermato dall'utente (7/9/2026); una sola modifica.

## Correzioni applicate

| N. | Posizione | Prima | Dopo | Categoria | Motivo |
|---|---|---|---|---|---|
| 1 | Frontespizio | «Candidato:» | «Candidata:» | uniformità (deciso dall'utente) | etichetta del modello di dipartimento (`source/frontespizio.doc`) al maschile generico; la candidata è una donna |

I testi (ringraziamenti, introduzione, abstract) sono identici ai Word e non presentano
refusi.

## Da decidere

Nessun punto aperto. I due dubbi sottoposti all'utente e le decisioni prese:

1. **Abstract, sigla EEFQ mai sciolta** («mediante EEFQ» / «through the EEFQ», così nel
   Word). **Deciso:** si lascia così.
2. **Frontespizio, «Candidato:».** **Deciso:** «Candidata:» (correzione 1).

## Controlli eseguiti senza rilievi

- **Fedeltà ai Word.** Ringraziamenti: 1465 parole, 0 differenze rispetto a
  `dediche.docx` (le virgolette dritte del Word sono rese con virgolette tipografiche).
  Introduzione e i due abstract: 735 parole, 0 differenze rispetto a `Intro&Abstract.docx`;
  le tre coppie di citazioni, scritte nel Word come numeri della bibliografia, sono i
  `\cite` giusti e stampano [1,2], [3,4], [5,6]. Frase di apertura identica al Word, in
  corsivo su tre righe allineate a destra.
- **A. Ortografia e refusi.** Nessuna parola doppia, nessuno spazio doppio o prima della
  punteggiatura; accenti e apostrofi corretti; 7 coppie di virgolette nei ringraziamenti,
  tutte chiuse; nessun grassetto o spazio unificatore residuo.
- **B. Grammatica.** Letti i 24 capoversi dei ringraziamenti, i 4 dell'introduzione e i
  due abstract: nessun rilievo. L'abstract inglese è corretto e sillabato con le regole
  inglesi (`otherlanguage`).
- **C. Citazioni.** Le 6 citazioni dell'introduzione sono legate con `~` alla parola
  precedente; nessun rimando `\ref` (l'introduzione del Word non cita i capitoli).
- **D. Titoli, indice, elenco delle tabelle.** Indice completo e nell'ordine giusto:
  «Abstract (Italiano/English)» (p. i), «Introduzione» (p. 1), i quattro capitoli con tutte
  le sezioni fino al terzo livello e le voci «Caso 1»…«Caso 8», il nuovo «4.4 Discussione»,
  «Elenco delle tabelle» (p. 140), «A Protocollo di somministrazione e scoring del Baby-FE»
  (p. 143), «Bibliografia» (p. 161). Elenco delle tabelle: le 26 tabelle del capitolo 4 con
  i titoli brevi di `tabelle.md`; le tabelle dell'appendice, per scelta della fase
  precedente, non sono flottanti e non vi compaiono. L'ultima pagina dell'indice (viii) ha
  solo due voci: è il normale trabocco dell'indice, nessun intervento.
- **E. Terminologia e sigle.** Frontespizio: titolo con le iniziali maiuscole scelte
  dall'utente, «Prof.ssa» per relatrice e correlatrice, corso di laurea in minuscolo,
  «ANNO ACCADEMICO 2025 / 2026» senza grassetto (decisioni F1). Sigle: vedi «Da decidere» 1.
- **F. Numeri.** Abstract: «66 bambini», «otto casi» coerenti con il capitolo 4;
  introduzione: «18 e i 36 mesi», «18–36 mesi» coerenti con il resto.
- **G. Impaginazione.** Numerazione: frontespizio, retro, dedica, retro e le quattro
  pagine dei ringraziamenti senza numero né testata; abstract italiano a p. i, inglese a
  p. iii (retri bianchi ii e iv), indice v–viii, introduzione 1–2 in stile «plain» senza
  testata, capitolo 1 da p. 3. Titolo del frontespizio su due righe senza sillabazione;
  nessuna vedova od orfana; nessun nome proprio o sigla spezzati a fine riga (le parole
  spezzate sono comuni: «rappre-sentato», «regu-latory», «Al-l'interno»…). L'ultima pagina
  dei ringraziamenti ha 23 righe più il nome, con lo spazio deciso in F3.

## Verifica finale

- Compilazione: 185 pagine, 0 errori, 0 righe troppo lunghe (Overfull), 0 avvisi biber.
- I quattro capitoli restano a 0 differenze.
