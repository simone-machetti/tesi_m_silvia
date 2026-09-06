# Controllo C — citazioni e riferimenti

Primo blocco del controllo finale (`plan.md`, punto 10). Verifica meccanica, rifatta da
zero e indipendente da quella eseguita durante la migrazione. Script:
`strumenti/controllo_citazioni.py`.

## a. Ogni citazione del testo contro il Word originale

Per ciascun `\cite` dei quattro capitoli — **363 in tutto** — le parole che lo precedono
sono state cercate nel testo del Word originale, ed è stata letta la citazione
«(Autore, anno)» che lì segue. Per ogni autore-anno così ricavato è stato verificato che
la voce di `References.bib` puntata dal `\cite` abbia quel cognome fra gli autori e quell'anno.

**Esito: 363 su 363 corrette.** Nessuna citazione punta a una voce con autore o anno
diversi da quelli scritti nel Word.

Casi particolari, tutti verificati a mano:
- le 12 citazioni narrative («Kopp (1982)», «Berni e colleghi (2025)»…), dove il cognome
  sta prima della parentesi;
- le 5 citazioni «(SIGLA; Autore, anno)», come «(IBQ-R; Gartstein & Rothbart, 2003)»;
- le 27 citazioni Astle, scritte nel Word come 2021 o 2022 e ora tutte sulla voce unica
  del 2022 (tasks.md, punto 1);
- «Vygotskij, 1962» sulla voce `vygotsky1962` e «Rothbart et al., 2003» su Gartstein &
  Rothbart (2003), agganci confermati dall'utente (tasks.md, punto 3).

**Integrazione (controllo del capitolo 2, `cap_2.md`):** questo controllo partiva dai
`\cite` esistenti, quindi non poteva vedere una citazione mai convertita. Nel capitolo 2
(§2.1.1) ne è rimasta una in chiaro, «(Tronick, 2007; Kochanska et al., 2001).», sfuggita
alla migrazione perché nel Word la parentesi di chiusura era in grassetto. Ora è
`\cite{tronick2007,kochanska2001}`; i `\cite` dei quattro capitoli diventano **364**. Il testo
del PDF è stato setacciato per altri residui «(Autore, anno)» o «et al., anno» in tutta
la tesi: nessuno.

## b. Rimandi interni

- **104 etichette** definite, **36 rimandi distinti**, nessun rimando senza bersaglio.
- Ogni etichetta di sezione `sec:a_b_c` corrisponde al numero effettivo a.b.c; `cap:uno`…
  `cap:quattro` valgono 1…4; `app:babyfe` vale A.
- Nelle otto schede-caso del capitolo 4, ogni rimando `\ref{tab:casoN_…}`, ogni etichetta e
  ogni didascalia «Caso N» stanno dentro il blocco del Caso N. Nessun incrocio.
- I 27 rimandi alle tabelle e i 33 a capitoli e sezioni stampano gli stessi numeri del
  Word (verificato ai punti F9 e F11 di tasks.md).

## c. Bibliografia

102 voci: 87 articoli, 8 capitoli di volume, 7 libri. Nessun titolo duplicato. Tutte le
voci hanno autore, titolo e anno; gli articoli hanno rivista, volume e pagine (unica
eccezione voluta: Berni et al. 2025, *online first*, con la nota «Advance online
publication»); i capitoli hanno volume ed editore; i libri hanno l'editore. Iniziali
sempre separate da spazio, intervalli di pagine sempre con il trattino lungo. Nessuna
anomalia.

## Conclusione

Le citazioni e i riferimenti non richiedono correzioni. Il controllo finale prosegue con
i capitoli (grammatica, refusi, titoli, terminologia, numeri).
