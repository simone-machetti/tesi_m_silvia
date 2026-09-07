# Capitolo 2 — controllo finale (punto 10)

File: `tesi/main/2_capitolo_2.tex` (pagine stampate 23–54). Word di riferimento: `source/capitolo_2.docx`.
Metodo (vedi `plan.md`, punto 10): lettura integrale dei 154 capoversi, controlli
meccanici A–H, correzioni sicure applicate direttamente e registrate qui, dubbi nella
sezione «Da decidere». Dopo ogni modifica: ricompilazione e verifica di fedeltà
(`strumenti/verifica_cap_2.md`).

**Stato:** tutte le correzioni applicate e confermate dall'utente (6/9/2026), compresi i
quattro punti «da decidere».

## Correzioni applicate

Le correzioni di sola forma (1–4, 7) non toccano le parole. Le 5 e 6 cambiano il testo e
sono registrate come «revisioni» in `strumenti/vcfg2.json`, insieme alle due voci che
servono al verificatore per la citazione (1) e per lo spazio (4), così la verifica di
fedeltà resta a **0 differenze**.

| N. | Posizione | Prima | Dopo | Categoria | Motivo |
|---|---|---|---|---|---|
| 1 | §2.1.1, 3° capoverso | «…nel funzionamento regolativo (Tronick, 2007; Kochanska et al., 2001**).**» | «…nel funzionamento regolativo [15,39].» | citazione | **unica citazione autore-anno rimasta in tutta la tesi**, mai convertita in `\cite`: nel Word la parentesi di chiusura era in grassetto («*).*») e lo script di migrazione non l'ha riconosciuta; il controllo C esaminava solo i `\cite` esistenti, quindi non poteva vederla. Agganciata alle voci `tronick2007` e `kochanska2001` (Kochanska, Coy & Murray, 2001), già in bibliografia. Il testo del PDF è stato poi setacciato per altri residui «(Autore, anno)» o «et al., anno»: nessuno |
| 2 | §2.1.1 (4° e 6° capoverso), §2.2.1 (4° capoverso) | punto finale in grassetto (3) | punto normale | refuso tipografico | residuo di Word (nel .docx solo la punteggiatura ha `<w:b/>`), come nel capitolo 1 |
| 3 | §2.3.4 (5° e 6° capoverso), §2.4.3 (1° capoverso) | virgola in grassetto (3) | virgola normale | refuso tipografico | idem; con la parentesi della correzione 1 fanno 7 grassetti tolti, nel capitolo non ne resta nessuno |
| 4 | §2.3.3, 3° capoverso | «sistemi di controllo [c] .» | «sistemi di controllo [c].» | spazio | spazio prima del punto, dopo la citazione |
| 5 | §2.3.4 (1°, 2°, 4° e 9° capoverso), §2.4.3 (1° capoverso), §2.3 (5° capoverso) | «una~dimensione», «transdiagnostico~si», «una~vulnerabilità», «come~dimensione», «la~struttura», «del~p factor» | spazio normale (6) | spazio | spazi unificatori dal «no-break space» di Word, come nel capitolo 1 |
| 6 | §2.3.2, 6° capoverso | «nei bambini ritardo globale dello sviluppo» | «nei bambini con ritardo globale dello sviluppo» | refuso (parola mancante) | manca la preposizione; la frase è altrimenti senza senso |
| 7 | §2.1.2, 9° capoverso; §2.4.3, 8° capoverso | «una alterazione» (2) | «un'alterazione» | uniformità | per analogia con la decisione presa al capitolo 1 su «un'elevata»: erano le uniche due «una + vocale» non elise rimaste nella tesi. **Da confermare** |
| 8 | §2.3.1, 5° capoverso | «Sonuga-Barke» spezzato a fine riga («Sonuga-/Barke», pag. 36) | cognome tenuto unito con `\mbox{}` | impaginazione | nome proprio spezzato al trattino; il verificatore ora ignora `\mbox` (`strumenti/verify.py`). **Annullata il 7/9/2026:** con il cognome indivisibile la riga «…proposto da Sonuga-Barke [50],» usciva dal margine di quasi 5 mm (segnalato dall'utente; l'avviso «Overfull» c'era nel log ma il mio conteggio, fatto con un `grep` difettoso, lo dava a zero). Il cognome torna divisibile al trattino, come nel Word: «Sonuga-/Barke [50]» è la divisione normale di un cognome composto |
| 9 | §2.3, 5° capoverso | «*p factor*» (corsivo) | «p factor» (tondo) | uniformità (deciso dall'utente) | le altre due occorrenze (§2.4, §2.4.2) e tutti gli altri termini stranieri dei capitoli 1 e 2 sono in tondo |
| 10 | §2.4.1, 3° capoverso | «comorbilità» | «comorbidità» | uniformità (deciso dall'utente) | forma usata nelle altre due occorrenze (§2.3.4); registrata come revisione in `strumenti/vcfg2.json` |

Nota sui conteggi del verificatore: il Word ha 142 gruppi di citazione riconosciuti più
quella della correzione 1, il LaTeX 143 `\cite`; i due totali ora coincidono.

## Da decidere

Nessun punto aperto. I quattro dubbi sottoposti all'utente e le decisioni prese:

1. **«p factor», corsivo o tondo.** Era in corsivo in §2.3 (così nel Word) e in tondo in
   §2.4 e §2.4.2; unico termine straniero in corsivo dei capitoli 1 e 2. **Deciso:** tondo
   ovunque (correzione 9).
2. **«comorbilità» / «comorbidità».** Entrambe corrette; «comorbidità» due volte, «comorbilità»
   una. **Deciso:** «comorbidità» ovunque (correzione 10).
3. **«DSM-5» mai sciolto** (§2.4.1, 1° capoverso). È il nome proprio del manuale, noto a chi
   legge. **Deciso:** si lascia così.
4. **«ADHD» sciolto quattro volte** (§2.2.1, §2.3.1 due volte, §2.3.3), sempre come
   «disturbo da deficit di attenzione/iperattività (ADHD)». Non è un errore e le quattro
   occorrenze stanno in sezioni diverse. **Deciso:** si lascia così.

## Controlli eseguiti senza rilievi

- **A. Ortografia e refusi.** Nessuna parola doppia, nessuno spazio doppio, nessuna
  punteggiatura doppia; accenti corretti (sé, nonché, poiché, è/e); nessun apostrofo
  sbagliato; 12 parentesi aperte e 12 chiuse; nessuna virgoletta nel capitolo.
- **B. Grammatica e sintassi.** Letti tutti i 154 capoversi: a parte la preposizione
  mancante (correzione 6), accordi, concordanze e tempi verbali corretti, nessuna frase
  sospesa, ogni capoverso chiuso dal punto.
- **C. Citazioni e rimandi.** 143 `\cite`, tutti legati con `~` alla parola precedente;
  12 rimandi `\ref`: 9 a «Capitolo 1», uno a «§1.6», uno a «sezione 2.3.1», uno a «sezione
  2.4», tutti al bersaglio giusto e stampati con il numero giusto. Le due citazioni
  narrative (Barkley 1997, Sonuga-Barke 2005) sono agganciate alle voci giuste.
- **D. Titoli.** 15 titoli (4 sezioni, 11 sottosezioni), identici al Word, tutti con la
  sola iniziale maiuscola e senza punto finale; nessun titolo cade come ultima riga di
  pagina.
- **E. Terminologia.** Termini stranieri in tondo come nel Word (l'unica eccezione è «p
  factor», vedi «Da decidere» 1): dual pathway model, developmental psychopathology,
  process-based, self-regulation, assessment, report, pattern, continuum, arousal,
  caregiver, top-down, bottom-up. Parole composte coerenti con il capitolo 1
  (co-regolazione, auto-consolazione, emotivo-motivazionali, iper-reattività,
  ipo-reattività, socio-relazionale). Trattino lungo negli intervalli (0–3, 3–6, 18–36).
  **Acronimi:** ADHD sciolto alla prima occorrenza (§2.2.1); RDoC sciolto («Research
  Domain Criteria (RDoC)») con «National Institute of Mental Health» per esteso; DSM-5
  vedi «Da decidere» 3; la sigla FE non è usata nel capitolo.
- **F. Numeri.** Il capitolo non contiene dati; le fasce d'età (0–3, 3–6, 18–36) sono
  coerenti fra loro.
- **G. Impaginazione.** Nessuna pagina quasi vuota (la pagina 54, di 18 righe, è l'ultima
  del capitolo); nessun titolo in fondo a pagina; nessuna vedova od orfana; le uniche
  parole con iniziale maiuscola spezzate a fine riga sono «Quan-titativamente» e
  «Comportamen-ti», regolari; «Sonuga-Barke» sistemato (correzione 8).

## Verifica finale

- Compilazione: 185 pagine, 0 errori, 0 righe troppo lunghe (Overfull), 0 avvisi biber.
- Fedeltà al Word: `strumenti/verifica_cap_2.md` → 15 titoli, 143 citazioni, **0 differenze**
  (5 revisioni registrate in `strumenti/vcfg2.json`); i capitoli 1, 3 e 4 restano a 0.
- Impaginazione dopo la nuova citazione: nessuna vedova od orfana in tutta la tesi, le 26
  tabelle del capitolo 4 nello stesso posto di prima.
