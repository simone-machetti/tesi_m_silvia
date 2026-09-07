# Interventi sulla bibliografia — registro

Correzioni concordate durante la revisione delle citazioni. **Tutte applicate.**
Il riferimento ai problemi di partenza è in [bib.md](bib.md).

Esito complessivo: la bibliografia passa da **106 voci** (99 dal Word + 7 segnaposto) a
**102 voci reali, verificate e tutte citate**. Nessun
`[VOCE MANCANTE]`, nessun DOI visibile, numerazione in ordine di lettura. Il testo dei
quattro capitoli è rimasto invariato: verifiche in `strumenti/` con **0 differenze**.

---

## 1. Astle et al. — unificare le due voci in una, datata 2022

**Stato:** applicato.

### Cosa è emerso dalla verifica online

Esiste **un solo** articolo, non due:

> Astle, D. E., Holmes, J., Kievit, R., & Gathercole, S. E. (2022). Annual Research Review:
> The transdiagnostic revolution in neurodevelopmental disorders. *Journal of Child
> Psychology and Psychiatry, 63*(4), 397–417. https://doi.org/10.1111/jcpp.13481

Pubblicato online il 23 luglio 2021 e a stampa nel 2022: da qui la doppia datazione nel
testo della tesi.

Le due voci presenti in `source/bibliografia.docx` sono lo stesso lavoro inserito due volte:

| Voce nel Word | Problema |
|---|---|
| **A** — *Transdiagnostic approaches to mental health problems in childhood and adolescence*, JCPP 62(8), 922–943, DOI `10.1111/jcpp.13354` | Titolo mai pubblicato con questi autori; il DOI appartiene a un altro articolo (Fristad, 2021, *Commentary: What to do with irritability?*, JCPP 62(3), 313–315) |
| **B** — *The transdiagnostic revolution in neurodevelopmental disorders*, JCPP 62(4), 397–417, DOI `10.1111/jcpp.13381` | Articolo reale, ma anno e volume sono quelli dell'anteprima online (2021, vol. 62) invece che del fascicolo (2022, vol. 63); anche il DOI ha una cifra sbagliata |

Fonti: [PubMed 34296774](https://pubmed.ncbi.nlm.nih.gov/34296774/) ·
[UEA Research Portal](https://research-portal.uea.ac.uk/en/publications/annual-research-review-the-transdiagnostic-revolution-in-neurodev/) ·
[Wiley 10.1111/jcpp.13481](https://acamh.onlinelibrary.wiley.com/doi/10.1111/jcpp.13481)

### Decisione presa

Unificare in **una sola voce**, con **anno 2022** e i dati del fascicolo a stampa.

### Cosa fare in concreto

1. In `tesi/tail/References.bib`, tenere **una sola** voce Astle, con chiave `astle2022`:
   - autori: Astle, D. E. and Holmes, J. and Kievit, R. and Gathercole, S. E.
   - titolo: *Annual Research Review: The transdiagnostic revolution in neurodevelopmental disorders*
   - rivista: Journal of Child Psychology and Psychiatry
   - anno **2022**, volume **63**, numero **4**, pagine **397--417**
   - DOI **10.1111/jcpp.13481**
2. Eliminare la voce A (chiave `astle2021`) — non corrisponde a nessuna pubblicazione.
3. Eliminare il segnaposto `astle2022` creato durante la migrazione, sostituito dalla voce reale.
4. Ripuntare su `astle2022` tutte le **27 citazioni**: le 12 che ora usano `astle2021` e le
   15 che ora usano il segnaposto.

### Effetti

- Nel testo **non cambia una parola**: con lo stile numerico IEEE l'anno non è visibile,
  si vede solo `[n]`. Cambia solo a quale numero puntano le 27 citazioni, che diventa uno
  solo invece di due.
- La bibliografia passa da 99 voci reali a **98**, e da 7 segnaposto a **6**: totale **104**.
- Si chiudono i punti 1 (riga *Astle et al., 2022*), 2 e 4 (voce B mai citata) di `bib.md`.

---

## 2. Aggiungere le sei voci citate ma assenti dalla bibliografia

**Stato:** applicato.

Sei citazioni del testo non avevano una voce corrispondente nel Word ed erano state rese
come segnaposto `[VOCE MANCANTE]`. I riferimenti reali sono stati ricostruiti dal contesto
della frase in cui compaiono e verificati online. Vanno inseriti in
`tesi/tail/References.bib` al posto dei rispettivi segnaposto.

### 2.1 Zelazo et al. (2003) — cap. 3, 2 citazioni · chiave `zelazo2003`

> Zelazo, P. D., Müller, U., Frye, D., & Marcovitch, S. (2003). The development of executive
> function in early childhood. *Monographs of the Society for Research in Child Development,
> 68*(3), vii–137.

Contesto: «controllo attentivo, inibizione comportamentale, memoria di lavoro e flessibilità
cognitiva» (Diamond, 2013; Zelazo et al., 2003).
Fonte: [Wiley](https://www.wiley.com/en-ae/The+Development+of+Executive+Function+in+Early+Childhood-p-9781405122542)

### 2.2 Friedman & Miyake (2017) — cap. 3, 2 citazioni · chiave `friedman2017`

> Friedman, N. P., & Miyake, A. (2017). Unity and diversity of executive functions:
> Individual differences as a window on cognitive structure. *Cortex, 86*, 186–204.
> https://doi.org/10.1016/j.cortex.2016.04.023

Contesto: il concetto di *task impurity*, citato insieme a Miyake et al. (2000).
Fonte: [PubMed 27251123](https://pubmed.ncbi.nlm.nih.gov/27251123/)

### 2.3 Calkins & Fox (2002) — cap. 3, 1 citazione · chiave `calkins2002fox`

> Calkins, S. D., & Fox, N. A. (2002). Self-regulatory processes in early personality
> development: A multilevel approach to the study of childhood social withdrawal and
> aggression. *Development and Psychopathology, 14*(3), 477–498.
> https://doi.org/10.1017/S095457940200305X

Fonte: [PubMed 12349870](https://pubmed.ncbi.nlm.nih.gov/12349870/)

### 2.4 Blair & Ursache (2011) — cap. 3, 1 citazione · chiave `blair2011ursache`

Forma **indicata dall'utente**, da usare così com'è:

> Blair, C., & Ursache, A. (2011). A bidirectional model of executive functions and
> self-regulation. *Handbook of self-regulation: Research, theory, and applications, 2*,
> 300–320.

Nota: il titolo usa «model» (non «theory», variante che circola nel repository NYU).

*In fase di implementazione* la voce è stata inserita come capitolo di volume, aggiungendo
curatori (Vohs & Baumeister) ed editore (Guilford Press): è un capitolo dello stesso volume
di Calkins & Leerkes (2011), che in bibliografia compare già in forma completa, e le due
sarebbero risultate incoerenti a poche righe di distanza. Il titolo resta quello indicato.

### 2.5 Beauchaine & McNulty (2013) — cap. 3, 1 citazione · chiave `beauchaine2013mcnulty`

> Beauchaine, T. P., & McNulty, T. (2013). Comorbidities and continuities as ontogenic
> processes: Toward a developmental spectrum model of externalizing psychopathology.
> *Development and Psychopathology, 25*(4pt2), 1505–1528.
> https://doi.org/10.1017/S0954579413000746

Fonte: [PubMed 24342853](https://pubmed.ncbi.nlm.nih.gov/24342853/)

### 2.6 Bayley (2006) — cap. 4, 1 citazione · chiave `bayley2006`

> Bayley, N. (2006). *Bayley Scales of Infant and Toddler Development, Third Edition:
> Administration manual*. Harcourt Assessment.

È il manuale dello strumento usato nello studio, non un articolo, e la Bayley-III del 2006
non è una pubblicazione singola ma un kit: Administration Manual, Technical Manual e moduli
di registrazione, tutti stesso autore, stesso anno, stesso editore.

**Scelto l'Administration Manual**, coerente con il modo in cui la tesi lo richiama: il testo
parla di procedure di somministrazione e codifica, e precisa che il *Behavior Observation
Inventory* «non prevede l'attribuzione di punteggi standardizzati», cioè non attinge al
Technical Manual. Editore *Harcourt Assessment*, il nome all'epoca della pubblicazione
(acquisita da Pearson nel 2008, che oggi distribuisce lo strumento).

Nel `.bib` la voce non ha il campo `edition`: l'edizione è già dentro il titolo, e lo stile
la stamperebbe due volte.

**Resta da verificare, se rilevante:** esiste un adattamento italiano della Bayley-III
(Ferri, Orsini e Stoppa, Giunti). Se le somministrazioni sono state condotte con l'edizione
italiana anziché con l'originale americana, la voce corretta sarebbe quella dell'adattamento
e converrebbe esplicitarlo anche nel testo — modifica di contenuto, quindi da valutare a
parte. Nel testo attuale non c'è alcun accenno alla versione usata.

### Effetti

- Spariscono tutti e sei i segnaposto `[VOCE MANCANTE]`: insieme al punto 1, la bibliografia
  non contiene più voci incomplete.
- Nel testo **non cambia una parola**: cambia solo il riferimento a cui puntano 8 citazioni.
- La bibliografia arriva a **104 voci, tutte reali** (98 dal Word + 6 aggiunte qui).
- Si chiude il punto 1 di `bib.md`, tranne la riga `Vygotskij, 1962` che rientra nel punto
  successivo.

---

## 3. Confermare i due agganci dedotti dal contesto

**Stato:** applicato.

Sono i due soli punti in cui la migrazione non ha seguito il Word alla lettera: una
citazione è stata collegata a una voce che non le corrisponde esattamente. Entrambi gli
agganci sono ora confermati.

### 3.1 Vygotskij / Vygotsky — usare la grafia italiana

Nel Word la voce è `Vygotsky, L. S. (1962). Thought and language. MIT Press.`, mentre il
testo (cap. 2, 1 occorrenza) cita `(Vygotskij, 1962; …)`. Stessa opera, traslitterazione
diversa del cognome russo. La citazione era già stata agganciata alla voce esistente
`vygotsky1962`, senza creare un doppione.

**Deciso:** stampare la voce con la **grafia italiana**, coerente con quella usata nel testo:

> Vygotskij, L. S. (1962). *Thought and language*. MIT Press.

Da fare: cambiare il campo `author` della voce `vygotsky1962` in `Vygotskij, L. S.`.
La chiave resta invariata. Essendo l'unica voce sotto la V, l'ordine non cambia.

Con lo stile numerico la grafia **non compare più nel testo** (si vede solo `[n]`):
il cambiamento è visibile solo nella pagina della bibliografia.

### 3.2 `Rothbart et al., 2003` = Gartstein & Rothbart (2003)

Nel capitolo 3 la citazione `(Rothbart et al., 2003)` non corrisponde a nessuna voce. Due
righe più avanti lo stesso paragrafo cita `(IBQ-R; Gartstein & Rothbart, 2003)`, cioè lo
strumento di cui la prima citazione parla: è la stessa opera, citata una volta con il
secondo autore al posto del primo.

**Confermato:** entrambe puntano alla voce già esistente `gartstein2003`, senza creare un
settimo segnaposto.

Da fare: nessuna modifica a `References.bib` — l'aggancio è già quello. Resta facoltativo
uniformare anche il testo (`Rothbart et al., 2003` → `Gartstein & Rothbart, 2003`), che però
con lo stile numerico non produce alcuna differenza visibile.

### Effetti

- Nessun segnaposto in più: le due citazioni restano agganciate a voci reali.
- Si chiudono i punti 3 e 3-bis di `bib.md` e l'ultima riga rimasta del punto 1.

---

## 4. Togliere le voci mai citate

**Stato:** applicato.

Due voci compaiono nell'elenco del Word ma nessuno dei quattro capitoli le richiama:

> Fletcher-Watson, S. (2022). Evidence-based practice and neurodiversity: Implications for
> research and clinical work. *Autism, 26*(1), 3–5.

> Zelazo, P. D., Blair, C. B., & Willoughby, M. T. (2020). Executive function: Implications
> for education (NCER 2017-2000). National Center for Education Research.

La seconda è emersa solo dopo l'applicazione del punto 6: finché il `\nocite` forzato
registrava tutte le voci in anticipo, compariva comunque nel PDF e sembrava usata.

**Deciso:** rimuoverle entrambe da `tesi/tail/References.bib`.

### Effetti

- La bibliografia scende a **102 voci**, tutte reali e tutte richiamate dal testo.
- **Conseguenza sul punto 7 di `bib.md`:** dopo i punti 1 e 4 non resta più nessuna voce
  non citata, quindi `\nocite{*}` diventa superfluo — la bibliografia si genera da sola.
  Applicato nel punto 6.
- Si chiude il punto 4 di `bib.md`.

---

## 5. Correggere i dati sbagliati o incompleti in quattro voci

**Stato:** applicato.

Delle sette voci segnalate nel punto 5 di `bib.md`, **tre si erano già sistemate** durante
la migrazione e non richiedono nulla: `gandolfi2014` (era in formato Frontiers, ora
normalizzata), `miyake2000` (nel Word il testo del link diceva `htps://`, ma il DOI nel
`.bib` è corretto) e `mcclelland2012` (era spezzata su due righe, ora è una voce unica).

Restano quattro voci, tutte verificate online.

### 5.1 `karreman2006` — intervallo di pagine senza trattino

Nel Word: `561 579`. Correggere in:

```
pages = {561--579}
```

### 5.2 `meins2001` — anno e volume sbagliati, autori troncati

Il titolo e le pagine della voce corrispondono a un articolo del **2002**, non del 2001:
il vol. 73 di *Child Development* è del 2002. Sostituire con la forma corretta:

> Meins, E., Fernyhough, C., Wainwright, R., Das Gupta, M., Fradley, E., & Tuckey, M.
> (2002). Maternal mind-mindedness and attachment security as predictors of theory of mind
> understanding. *Child Development, 73*(6), 1715–1726.
> https://doi.org/10.1111/1467-8624.00501

Cambia quindi: anno `2001` → `2002`, volume `72` → `73`, elenco autori completo al posto di
`Meins, E. and others`, titolo con l'iniziale «Maternal», più il DOI.

**Alternativa scartata, da riaprire solo se necessario:** esiste anche un *Meins et al.
(2001)* reale — *Rethinking maternal sensitivity: Mothers' comments on infants' mental
processes predict security of attachment at 12 months*, JCPP 42(5), 637–648 — anch'esso
compatibile con il contesto del capitolo 1. È stata scelta la lettura del 2002 perché il
titolo e le pagine della voce nel Word sono inequivocabilmente quelli di quell'articolo.

Fonte: [PubMed 12487489](https://pubmed.ncbi.nlm.nih.gov/12487489/)

### 5.3 `ursache2012` — titolo troncato e dati mancanti

Nel Word il titolo si ferma a «school readiness» e mancano volume, numero e pagine.
Sostituire con la forma completa:

> Ursache, A., Blair, C., & Raver, C. C. (2012). The promotion of self-regulation as a means
> of enhancing school readiness and early achievement in children at risk for school
> failure. *Child Development Perspectives, 6*(2), 122–128.
> https://doi.org/10.1111/j.1750-8606.2011.00209.x

Fonte: [PubMed 32226480](https://pubmed.ncbi.nlm.nih.gov/32226480/)

### 5.4 `berni2025` — ordine degli autori e forma *online first*

L'assenza di volume e pagine è corretta (articolo *online first*), ma va aggiunta
l'indicazione «Advance online publication» e corretto l'ordine degli autori:

- Word: Berni, **Guzzetta**, Scatigna, **Pecini**, Igliozzi, Mazzotti, Calderoni, Martinelli, Tancredi
- Pubblicato: Berni, Scatigna, Igliozzi, Mazzotti, Calderoni, Martinelli, Tancredi, **Guzzetta**, **Pecini**

> Berni, M., Scatigna, S., Igliozzi, R., Mazzotti, S., Calderoni, S., Martinelli, A.,
> Tancredi, R., Guzzetta, A., & Pecini, C. (2025). Exploring the predictive role of early
> executive functions and self-regulation on functional outcome in neurodevelopmental
> disorders: A systematic review and meta-analysis. *Neuropsychology Review*. Advance online
> publication. https://doi.org/10.1007/s11065-025-09683-5

**Riserva:** la pagina dell'editore è dietro login, quindi l'ordine degli autori proviene da
due ricerche indipendenti ma non dalla fonte primaria. Se è disponibile il PDF, vale la pena
una verifica diretta.
Fonte: [Springer](https://link.springer.com/article/10.1007/s11065-025-09683-5)

### Effetti

- Quattro voci passano da incomplete o errate a corrette e verificate.
- Nel testo **non cambia una parola**: nessuna di queste correzioni è visibile nel corpo del
  testo, nemmeno il cambio d'anno di Meins, perché con lo stile numerico l'anno compare solo
  in bibliografia.
- Si chiude il punto 5 di `bib.md`.

---

## 6. Numerare la bibliografia nell'ordine di comparsa nel testo

**Stato:** applicato.

Oggi la bibliografia è stampata **nell'ordine dell'elenco del Word**, inversioni comprese
(`Caspi` prima di `Carlson`, `Diamond → Doebel → Degnan`, `Garon → Gardiner → Gartstein`,
`Samson` prima di `Sameroff`). Questo ordine non è alfabetico e non è quello di comparsa nel
testo: i numeri `[n]` risultano quindi sparsi.

**Deciso:** numerare le voci **nell'ordine in cui compaiono nel testo**, così che i numeri
crescano a mano a mano che si legge e restino crescenti anche dentro una citazione multipla
(`[3], [17]`).

### Cosa fare in concreto

Non serve aggiungere niente: è il comportamento **nativo** dello stile IEEE, oggi disattivato
da una forzatura. Basta rimuoverla.

1. Eliminare il file `tesi/tail/ordine_bibliografia.tex` (38 righe di `\nocite` espliciti che
   registrano tutte le voci in anticipo, nell'ordine del Word).
2. Togliere la riga `\input{tail/ordine_bibliografia}` da `tesi/main.tex` (riga 12).
3. Ricompilare: `style=ieee` numera da sé in ordine di citazione.

### Effetti

- I numeri `[n]` crescono seguendo la lettura: `[1]` è la prima opera citata nel capitolo 1.
- **Sparisce la manutenzione:** il file forzato andava rigenerato a ogni modifica di
  `References.bib`, e con i punti 1-5 le modifiche sono molte.
- **Si chiude anche il punto 7 di `bib.md` relativo a `\nocite{*}`:** serviva a stampare le
  voci mai citate, ma dopo il punto 1 (unificazione Astle) e il punto 4 (rimozione
  Fletcher-Watson) **tutte le voci risultano citate**, quindi non serve più.
- **Contropartita accettata:** la bibliografia non è più alfabetica, quindi non si può
  cercare un autore per cognome — ci si arriva dal numero nel testo. È il compromesso
  normale degli stili numerici ed è quello che adotta anche il template in `template/`.
- Nel testo **non cambia una parola**: cambiano solo i numeri.

---

## 7. Nascondere DOI e URL nella bibliografia stampata

**Stato:** applicato.

Durante la migrazione DOI e URL erano stati **attivati** per non perdere contenuto rispetto
al Word, dove 78 voci su 106 hanno un DOI. Il template di riferimento in `template/` li
nasconde invece.

**Deciso:** nasconderli, per una bibliografia più compatta e coerente con il template.

### Cosa fare in concreto

In `tesi/settings/custom.tex` (riga 70), da:

```latex
\usepackage[style=ieee,doi=true,isbn=false,url=true,eprint=false]{biblatex}
```

a:

```latex
\usepackage[style=ieee,doi=false,isbn=false,url=false,eprint=false]{biblatex}
```

### Effetti

- I DOI **restano tutti in `References.bib`**: non viene cancellato niente, semplicemente
  non vengono stampati. Per rimostrarli bastano due parole.
- La bibliografia si accorcia di circa una riga per voce e occupa meno pagine.
- Diventano superflui, ma innocui, il pacchetto `xurl` in `custom.tex` e
  l'`\emergencystretch` in `tail/biblio.tex`, aggiunti per spezzare i DOI lunghi a fine
  riga. Si possono lasciare dove sono.
- Si chiude il punto 7 di `bib.md`.

---

# Riepilogo

| # | Intervento | Effetto sul testo | Esito |
|---|---|---|---|
| 1 | Astle: unificare le due voci, anno 2022 | nessuno | 27 citazioni su una voce sola |
| 2 | Aggiungere le 6 voci mancanti | nessuno | nessun `[VOCE MANCANTE]` |
| 3 | Vygotskij (grafia italiana) + conferma Gartstein & Rothbart | nessuno | fatto |
| 4 | Togliere le 2 voci mai citate | nessuno | fatto |
| 5 | Correggere Karreman, Meins, Ursache, Berni | nessuno | fatto |
| 6 | Numerare in ordine di comparsa nel testo | solo i numeri | `[1]` = Kopp 1982 |
| 7 | Nascondere DOI e URL | nessuno | 0 DOI stampati |

Nessuno dei sette interventi ha toccato una parola del testo dei capitoli: agiscono tutti su
`References.bib` e sulla configurazione.

## Verifiche eseguite dopo l'implementazione

- Compilazione pulita, nessun errore, **160 pagine** (erano 161).
- Biber: **nessun avviso**, nessuna citazione irrisolta.
- Fedeltà del testo, con gli script in `strumenti/`: cap. 1 → 0 differenze, cap. 2 → 0,
  cap. 3 → 0, cap. 4 → 0 (49 titoli e 26 tabelle invariati).
- Bibliografia stampata: 102 voci numerate da `[1]` a `[102]`, `[1]` = Kopp (1982), cioè la
  prima opera citata nel capitolo 1. Voci del `.bib` e citazioni del testo coincidono
  esattamente: 102 e 102.
- Controllo a campione sul PDF delle sei voci nuove e delle quattro corrette: tutte rese
  correttamente, Fletcher-Watson assente, ordine autori di Berni aggiornato.

## Dettagli scelti in fase di implementazione

- **Blair & Ursache (2011)** è stata inserita come capitolo di volume, con curatori
  (Vohs & Baumeister) ed editore (Guilford Press), invece che nella forma compressa
  fornita. Motivo: è un capitolo dello stesso volume di Calkins & Leerkes (2011), che in
  bibliografia compare già in forma completa; le due voci sarebbero altrimenti risultate
  incoerenti a due righe di distanza. Il titolo resta quello indicato, con «model».
  Si torna indietro in una riga se preferibile.
- **Meins** mantiene la chiave `meins2001` benché l'articolo sia del 2002, per non toccare
  le citazioni nei capitoli. La chiave non è visibile nel PDF.

---

# Interventi sulle tabelle

## 8. Didascalie e riferimenti per tutte le 26 tabelle

**Stato:** applicato.

Oggi solo 3 tabelle su 26 hanno una didascalia e sono richiamate dal testo. Le altre 23 —
8 schede di sintesi, 8 prestazioni al Baby-FE, 7 osservazioni del comportamento — non hanno
titolo e non sono mai nominate. Inoltre nel file non esiste un solo `\caption`, `\label` o
`\ref`: il numero «4.2» è battuto a mano in tre punti indipendenti (didascalia, testo,
Elenco delle tabelle), senza nulla che ne garantisca l'allineamento.

### Decisioni prese

| Aspetto | Decisione |
|---|---|
| Didascalia | Titolo + breve descrizione su tutte e 26 |
| Posizione | **Sempre sopra** la tabella, mai sotto |
| Formattazione | Predefinita: niente corsivo, niente grassetto |
| Numerazione | Per capitolo, **4.1 … 4.26**, nell'ordine di comparsa |
| Legende di codifica | **Assorbite** nella descrizione, perdendo il corsivo |
| Righe «Nota.» | **Restano sotto** la tabella, sono note di corredo |
| Rimandi nel testo | Tutte e 26 richiamate; forma scelta da me, vedi sotto |

### Forma dei rimandi

Scelta: **una frase di raccordo nuova prima di ogni tabella**, senza toccare le frasi già
presenti nel Word.

Il motivo è che le legende di codifica, assorbite nella didascalia, lasciano vuoto lo spazio
fra l'intestazione del caso e la tabella: la frase di raccordo lo riempie e assolve al
rimando. In più resta valido il principio seguito finora — si aggiunge, non si riscrive.

Modelli:

- «La Tabella 4.X riassume il profilo del Caso N.»
- «Le risposte del Caso N alle singole prove sono riportate nella Tabella 4.X.»
- «Il comportamento osservato durante la valutazione del Caso N è riportato nella Tabella 4.X.»

### Modelli di didascalia

Struttura: `\caption[Titolo breve]{Titolo. Descrizione.}` — l'argomento opzionale tiene
leggibile l'Elenco delle tabelle, che passa da 3 a 26 voci.

- **Scheda di sintesi:** «Caso N: scheda di sintesi. Genere, età alla somministrazione, dati
  anamnestici dal questionario compilato dai genitori ed eventuale diagnosi.»
- **Prestazione al Baby-FE:** «Caso N: prestazione al Baby-FE. Punteggio ed esito nelle 15
  prove.» seguita dalla legenda di codifica esistente, riportata parola per parola.
- **Osservazione:** «Caso N: osservazione del comportamento durante la valutazione.» seguita
  dalla legenda esistente sul Behavior Observation Inventory.

Le tre didascalie già presenti vengono convertite in `\caption`, private del numero letterale
(che genera LaTeX) e completate con una descrizione dove manca.

### Conseguenza da tenere presente

Numerando in ordine di comparsa, le 23 tabelle-caso si inseriscono in mezzo: le due tabelle
aggregate finali, oggi **4.2 e 4.3, diventano 4.25 e 4.26**. I tre rimandi già presenti nel
Word cambiano quindi numero visibile («cfr. Tabella 4.2» → «cfr. Tabella 4.25»). Con `\ref`
l'aggiornamento è automatico e resta coerente per sempre, ma il numero letto dal lettore non
è più quello del Word.

### Rottura della regola di fedeltà

È il primo intervento che **aggiunge testo assente dal Word**: 23 titoli, 23 descrizioni e
23 frasi di raccordo. Da qui in avanti il capitolo 4 non è più identico all'originale e le
verifiche in `strumenti/` segnaleranno le aggiunte.

Contromisure adottate:

- **`tabelle.md`**: elenca tutte e 26 le didascalie e tutte e 23 le frasi di raccordo, una
  per una, con il testo integrale. Le parti provenienti dal Word (le legende di codifica)
  sono marcate in corsivo, così si distingue a colpo d'occhio ciò che è stato scritto ex novo.
- **`verify4.py` aggiornato**: didascalie e frasi di raccordo vengono escluse dal confronto
  su entrambi i lati, così la verifica continua a coprire la **prosa** del capitolo. Esito
  dopo l'intervento: **0 differenze**, cioè nessuna parola del Word è stata toccata.

### Esito

- 26 didascalie con titolo e descrizione, tutte sopra la tabella, in formattazione predefinita.
- 26 `\caption` e 26 `\label`; **27 rimandi** nel testo (la tabella 4.25 è richiamata due volte).
- Elenco delle tabelle: da 3 a **26 voci**, numerate 4.1 → 4.26.
- Nessun numero di tabella più battuto a mano: erano tre punti indipendenti per ciascuna.
- Compilazione pulita, nessun riferimento irrisolto, 162 pagine (erano 160).
- Nessuna tabella spezzata fra due pagine, nessun avviso «Float too large».

### Modifiche alle tre didascalie preesistenti

Erano disomogenee e due su tre avevano solo il titolo. Sono state uniformate al modello
titolo + descrizione, il che ha comportato un lieve riadattamento del testo del Word:

| | Word | Ora |
|---|---|---|
| 4.1 | «Profilo dei fattori di rischio dei bambini selezionati (dati dal questionario compilato dai genitori).» | «Profilo dei fattori di rischio dei bambini selezionati. Dati tratti dal questionario compilato dai genitori.» |
| 4.25 | «Prestazioni complessive al Baby-FE nei casi selezionati» | stesso titolo, con descrizione aggiunta su età, punteggio totale, prove non valide e percentile |
| 4.26 | «Punteggi alle sottoscale EEFQ nei casi selezionati e valori di riferimento del campione totale dello studio» | stesso testo come titolo, con descrizione aggiunta sulle quattro sottoscale |

### Scelta di dettaglio

Il prefisso del caso usa il trattino lungo e non i due punti — «Caso 1 --- scheda di
sintesi» invece di «Caso 1: scheda di sintesi» — perché LaTeX antepone già «Tabella 4.2:»
e ne sarebbero risultati due due-punti di fila nella stessa riga.

---

# Seconda fase — modifiche da `guideline/modifiche.docx`

Riferimento: il piano in `plan.md`. Un punto alla volta, con conferma dell'utente.

## F1. Frontespizio

**File:** `tesi/head/1_frontespizio.tex`

| Campo | Valore inserito |
|---|---|
| Corso di laurea | CORSO DI LAUREA IN — a capo — Psicologia dello sviluppo tipico e atipico |
| Titolo | Profili di Disregolazione nella Prima Infanzia: Una Prospettiva Transdiagnostica per la Valutazione Precoce (*title case* scelta dall'utente) |
| Relatore | Prof.ssa Paola Viterbori |
| Correlatore | Prof.ssa Maria Carmen Usai |
| Candidato | Silvia Occhionero |
| Anno accademico | ANNO ACCADEMICO 2025 / 2026, senza grassetto |

**Stato:** confermato.

Layout: il blocco unico a destra è diventato due colonne allineate in alto — relatore e
correlatore a sinistra, candidato a destra. Il resto della pagina (logo, dipartimento,
spaziature, anno in grassetto centrato) è quello del template.

Le etichette restano quelle del template e delle modifiche: «Relatore», «Correlatore»,
«Candidato». Se si preferiscono le forme femminili (Relatrice, Correlatrice, Candidata)
si cambiano tre parole.

## F2. Dedica

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/head/2_dedica.tex`

Sostituito il segnaposto del template («Verba volant, scripta manent — Caius Titus») con
la frase di apertura di `guideline/dediche.docx`, riportata parola per parola, in corsivo,
su tre righe come nel Word, allineata a destra come nel template:

> *Alla ricerca,*
> *che nasce dalla curiosità di osservare*
> *e dal desiderio di comprendere.*

Pagina senza numero né testata, a 3 cm dal margine superiore, come prevedeva il template.
Tolto anche il blocco `center` vuoto che il template lasciava in fondo alla pagina.

## F3. Ringraziamenti

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/head/3_ringraziamenti.tex`

Sostituito il testo latino segnaposto con i ringraziamenti di `guideline/dediche.docx`:
24 paragrafi, 1.465 parole, riportati parola per parola (conversione con pandoc, nessun
comando LaTeX nel corpo, solo virgolette tipografiche). Verifica parola per parola contro
il Word: 0 differenze.

In chiusura, dopo 2,5 cm di spazio, il solo nome della candidata allineato a destra: la
data del template («Genova, *data*») è stata tolta su richiesta dell'utente.

Corretto un difetto del template emerso ora che la sezione occupa quattro pagine: lo stile
«fancy» stampava sulle pagine successive alla prima la testata «Capitolo 0» (un
`\chapter*` non ha numero). Le pagine dei ringraziamenti sono ora tutte senza numero né
testata, come frontespizio e dedica: la numerazione romana parte dagli abstract, dove il
template azzera il contatore.

La tesi passa da 180 a 183 pagine.

## F4. Abstract e Introduzione

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/head/4_abstract.tex` (riscritto), `tesi/main/0_introduzione.tex` (nuovo),
`tesi/main.tex` (una riga).

**Abstract**, come nel template di riferimento: nel front matter, due pagine separate
(`\cleardoublepage` fra le due), ciascuna con `\chapter*{Abstract}`; italiano a pagina i,
inglese a pagina iii, quest'ultimo dentro `otherlanguage{english}` per la sillabazione.
Una sola voce nell'indice: «Abstract (Italiano/English)». Sostituisce il «Sommario»
segnaposto.

**Introduzione**: capitolo non numerato in apertura del corpo della tesi, prima del
capitolo 1, con voce nell'indice; parte a pagina 1. Stile di pagina «plain» per evitare la
testata «Capitolo 0». Le tre coppie di citazioni, scritte nel Word come numeri della
bibliografia, sono diventate `\cite`:

| Nel Word | `\cite` |
|---|---|
| [2], [4] | `calkins2007,blair2015` |
| [38], [41] | `beauchaine2019,astle2022` |
| [85], [78] | `mcclelland2012,snyder2021` |

**Effetto sulla bibliografia:** queste sei opere sono ora i riferimenti [1]–[6]
dell'intera tesi, nell'ordine in cui compaiono nell'introduzione; tutti gli altri numeri
sono slittati di conseguenza. Verificato nel PDF: [1] Calkins 2007, [2] Blair & Raver
2015, [3] Beauchaine & Cicchetti 2019, [4] Astle et al. 2022, [5] McClelland & Cameron
2012, [6] Snyder et al. 2021.

Verifica parola per parola contro il Word: introduzione 429 parole, abstract italiano 152,
abstract inglese 155 — **0 differenze** in tutti e tre.

La tesi passa da 183 a 187 pagine.

## F5. Elenco degli acronimi

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/main.tex`

Tolta la riga `\input{head/5_acronimi}`. Verificato prima dell'intervento: nessun capitolo
usa il comando `\ac{}`, e nessun altro file richiama l'elenco. Il file
`head/5_acronimi.tex` resta sul disco ma non viene più incluso; il pacchetto `acronym`
resta caricato in `custom.tex`, innocuo.

Effetto: sparisce la pagina «Elenco degli acronimi» (con i tre acronimi di esempio del
template) e la sua voce nell'indice. Dagli abstract si passa direttamente all'indice.

## F6. Testata del capitolo 3

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/main/3_capitolo_3.tex`

Aggiunto, subito dopo il `\chapter{...}`, un `\chaptermark` con il titolo breve «La
valutazione dell'autoregolazione nella prima infanzia». Agisce solo sulle testate: la
pagina di apertura del capitolo e l'indice conservano il titolo intero con «(18–36 mesi e
3–6 anni)». Verificato nel PDF: la testata delle pagine del capitolo 3 non si sovrappone
più a «Capitolo 3».

### Regressione trovata e corretta lungo la strada

Controllando la testata è emerso che **le testate erano sparite in tutti i capitoli**, non
solo nel terzo. Causa: il template ridefinisce lo stile «plain» con `\fancyhf{}`, che con
la versione di fancyhdr installata azzera i campi delle testate **in modo globale**; i
`\pagestyle{plain}` introdotti oggi per abstract e introduzione, venendo prima del corpo,
le cancellavano per sempre. Prima di oggi nessun `\pagestyle{plain}` precedeva i capitoli
e il difetto non si vedeva.

Correzione, in `settings/custom.tex`: la definizione delle testate è ora raccolta nel
comando `\testatecapitoli`, richiamato al caricamento (nessun cambiamento rispetto a
prima) e in `main/1_capitolo_1.tex` subito dopo il `\pagestyle{fancy}`, dove il corpo
della tesi riprende lo stile con le testate. Verificato: testate presenti nei capitoli 1,
2, 3 e 4; numeri romani su abstract e indice; introduzione alle pagine 1-2, capitolo 1 da
pagina 3.

## F7. Appendice: «ETÀ IN MESI»

**Stato:** applicato, in attesa di conferma.

**File:** `strumenti/appendice.py` (generatore) e `tesi/tail/appendice.tex` (rigenerato).

Il testo spurio «ule2.4cm0.4pt» veniva dal generatore: `\rule` stava in una stringa
Python non *raw* e `\r` era diventato un ritorno a capo; lo stesso errore aveva mangiato
l'apostrofo di «ETA'». Corretta la stringa e rigenerata l'appendice: nel `.tex` cambia
una sola riga, il resto è identico.

Deciso: accento corretto in italiano, «ETÀ IN MESI».

Sistemata anche l'impaginazione della riga, che con le tre linee da compilare ripristinate
non entrava più nella pagina e spezzava «VALUTAZIO-NE»: i tre campi sono ora blocchi
indivisibili distribuiti su una riga sola, con le linee leggermente più corte
(2,0 / 1,6 / 2,0 cm).

Nota per il punto 11: il titolo dell'appendice, «Protocollo di somministrazione e scoring
del Baby-FE», nella pagina di apertura va a capo spezzando «sco-ring». Se il titolo
cambierà con il nome scelto, si sistemerà lì.

## F8. Capitolo 4: tre sostituzioni da `4.3.3_4.4.1_rev.docx`

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/main/4_capitolo_4.tex`; `strumenti/verify4.py` e il nuovo
`strumenti/revisioni_cap4.json` per la verifica.

Come deciso, sono state modificate solo le parti marcate in grassetto nel file di
revisione, e il grassetto non è stato riportato nella tesi. Per la nota della tabella, che
nel file non ha grassetto, la parte nuova è stata individuata per confronto con la nota
attuale.

| # | Dove | Intervento | Parole aggiunte |
|---|---|---|---|
| a | Nota sotto la Tabella 4.26 | Aggiunte in coda due frasi: i punteggi del 10° e 20° percentile per IC, FX, WM, RG e la precisazione che sono riferimenti descrittivi interni al campione | +57 |
| b | Sez. 4.3.3, paragrafo «Anche i punteggi dell'EEFQ…» | Inserite tre frasi fra «…per i Casi 1, 5 e 6.» e «Il Caso 3 presenta…», sulla collocazione dei casi rispetto al 10° e 20° percentile | +120 |
| c | Sez. 4.4.1, paragrafo «Un elemento di convergenza circoscritto…» | «inferiore alla media del campione totale» → «collocato tra il 10° e il 20° percentile della distribuzione osservata nel campione totale» | +8 |

Ogni stringa da sostituire è stata cercata nel file e trovata esattamente una volta; il
testo nuovo proviene dalla conversione pandoc del file di revisione, senza ribattitura.
Il corpo della Tabella 4.26 e il paragrafo successivo a (b) sono rimasti invariati, come
richiesto dal file.

**Verifica:** le tre sostituzioni sono registrate in `strumenti/revisioni_cap4.json` e
`verify4.py` le applica anche al lato Word prima del confronto, così segnala solo ciò che
non è previsto. Esito dopo l'intervento: 49 titoli, 26 tabelle, **0 differenze**. Le tre
frasi nuove sono state ritrovate nel PDF.

La tesi passa da 185 a 187 pagine.

### F8-bis. Grassetto nella prosa della 4.3.3

Su segnalazione dell'utente. Due frasi intere del paragrafo sulle singole prove erano in
grassetto — «L'Asta con anelli presenta invece un andamento differente…» e «Nel complesso,
pertanto, l'analisi delle singole attività…». Così anche nel Word originale, ma senza
ragione tipografica: con ogni probabilità sono marcature di rilettura mai rimosse, come
quelle del file di revisione. Riportate al tondo; il testo non cambia.

Il grassetto nelle tabelle della stessa sezione è invece **voluto** e resta: nella
Tabella 4.26 evidenzia i punteggi almeno una deviazione standard sotto la media, come
spiega la nota; le intestazioni di colonna sono in grassetto come in tutte le tabelle.

## F9. Rimandi interni con `\ref`

**Stato:** applicato, in attesa di conferma.

**File:** `tesi/main/2_capitolo_2.tex`, `3_capitolo_3.tex`, `4_capitolo_4.tex`;
`strumenti/verify.py` e `verify4.py` per la verifica.

I rimandi a capitoli e sezioni scritti a parole nel Word sono ora `\ref` verso etichette
già esistenti: **33 sostituzioni** (12 nel capitolo 2, 9 nel 3, 12 nel 4; nessuna nel
capitolo 1, che non rimanda ad altri capitoli).

| Nel Word | Occorrenze | Ora |
|---|---|---|
| Capitolo 1 | 19 | `Capitolo~\ref{cap:uno}` |
| Capitolo 2 | 4 | `Capitolo~\ref{cap:due}` |
| Capitolo 3 | 4 | `Capitolo~\ref{cap:tre}` (compreso «nel Capitolo 3.» a fine frase) |
| Capitoli 1, 2 e 3 | 1 | `Capitoli~\ref{cap:uno}, \ref{cap:due} e~\ref{cap:tre}` |
| §1.6 | 1 | `§\ref{sec:1_6}` |
| sezione 2.4 · sezione 2.3.1 | 2 | `sezione~\ref{sec:…}` |
| Sezione 4.3.2 · sezione 4.3.3 | 2 | `Sezione~\ref{sec:…}` |
| nella 4.4.1 | 3 | `nella~\ref{sec:4_4_1}` |

I 27 rimandi alle tabelle erano già `\ref`. I due rimandi «Appendice 1» del capitolo 3
restano da fare al punto 11, quando ci sarà il nome. Le righe di commento nei file sono
state escluse dalla sostituzione.

**Nel PDF non cambia nulla**: i numeri stampati sono identici a prima (controllati a
campione: «cfr. Capitolo 1, §1.6», «nei Capitoli 1, 2 e 3», «nella Sezione 4.3.2»,
«discusso nella 4.4.1», «descritto nel Capitolo 3.»). Compilazione senza riferimenti
irrisolti.

**Verifica:** `verify.py` e `verify4.py` riportano ora `\ref{cap:…}` e `\ref{sec:…}` al
numero corrispondente prima del confronto. Esito: capitoli 1, 2, 3 e 4 tutti a
**0 differenze**.

## F11. Nome dell'appendice

**Stato:** applicato, in attesa di conferma. (Fatto prima del punto 10 su richiesta.)

**Deciso:** titolo «Protocollo di somministrazione e scoring del Baby-FE», invariato;
contrassegno con la **lettera**, come LaTeX fa da sé.

Indice e pagina di apertura coincidevano già («A Protocollo di somministrazione e scoring
del Baby-FE»). L'unico disallineamento era nel testo del capitolo 3, dove i due rimandi
dicevano «Appendice 1».

**File:** `tesi/main/3_capitolo_3.tex` — i due rimandi sono ora `Appendice~\ref{app:babyfe}`
e nel PDF escono come «Appendice A» (sez. 3.7.3 e 3.8). Come al punto 9, restano allineati
a qualunque cambiamento futuro.

**Titolo dell'appendice:** nella pagina di apertura andava a capo spezzando «sco-ring».
Aggiunto `\hyphenation{scoring}` in `settings/custom.tex`: la parola non viene più
sillabata, in nessun punto della tesi, e il titolo va a capo su «…somministrazione e /
scoring del Baby-FE».

**Verifica:** `verify.py` riconosce ora anche `\ref{app:…}` e, tramite una voce
`revisioni` in `strumenti/vcfg3.json`, sa che «Appendice 1» → «Appendice A» è voluto
(due occorrenze). Tutti e quattro i capitoli a 0 differenze.

## F11-bis. Titoli dei capitoli nella pagina di apertura

Su segnalazione dell'utente: il titolo del capitolo 1 andava a capo con una sillaba sola
(«…sviluppo tipi- / co»).

**File:** `tesi/settings/template.tex` — il riquadro del titolo di capitolo è ora
a bandiera e senza sillabazione (`\raggedright`, `\hyphenpenalty=10000`): i titoli vanno
a capo solo fra le parole. Capitolo 1: «L'autoregolazione nello sviluppo / tipico».
Vale per tutti i capitoli e per l'appendice.

Dal confronto delle cinque aperture è emerso un secondo difetto, preesistente: il titolo
del capitolo 3 occupa tre righe e lo spazio fisso che il template lascia sotto il titolo
(30pt) è pensato per due, così la sezione 3.1 finiva attaccata all'ultima riga.
**File:** `tesi/main/3_capitolo_3.tex` — solo per questo capitolo la spaziatura dopo il
titolo è portata a 60pt e poi ripristinata; gli altri capitoli non cambiano.

`verify.py` istruito a ignorare il comando di spaziatura. Tutti i capitoli a 0 differenze.

## F12. Quattro richieste di impaginazione (fra l'11 e il 10)

**Stato:** applicato, in attesa di conferma.

### a. Pagina 113 quasi bianca

Causa: la barriera `\FloatBarrier` che precedeva ogni «Caso N». Quando il paragrafo di
chiusura di un caso traboccava di poche righe sulla pagina seguente, la barriera spingeva
il caso successivo alla pagina ancora dopo, lasciando la pagina con due righe sole. Le
barriere fra un caso e l'altro sono state tolte (8); restano le 11 prima delle
sottosezioni. Verificato: nessuna tabella scivola nel caso successivo, la pagina 113 è
piena e il Caso 5 inizia lì. Le uniche pagine poco piene rimaste sono le ultime pagine di
introduzione, capitolo 3 e capitolo 4, e il retro bianco prima del capitolo 2: normali.
La tesi passa da 187 a 185 pagine.

### b. Citazioni legate alla parola precedente

362 `\cite` erano preceduti da uno spazio normale, spezzabile: la citazione poteva finire
a inizio riga da sola. Lo spazio è ora `~` in tutti e quattro i capitoli (l'introduzione
lo aveva già). Nessuna citazione resta preceduta da spazio spezzabile.

### c. Citazioni multiple

Erano già tutte in un solo comando (`\cite{a,b,c}`) fin dalla migrazione: non esistono
`\cite` affiancati da unire. Lo stile IEEE le stampava come «[2], [9], [10]».

**Deciso:** forma compatta in una sola parentesi, senza spazi: «[2,9,10]». In
`settings/custom.tex` biblatex usa ora `citestyle=numeric-comp` con `\multicitedelim`
ridotto alla sola virgola; la bibliografia resta in stile IEEE. Le sequenze di numeri
consecutivi vengono compresse in intervalli, «[54–56]», come nell'uso IEEE. Verificato nel
PDF: nessuna citazione nel vecchio formato.

### d. Titoli senza sillabazione

Oltre ai titoli di capitolo (F11-bis), ora anche sezioni, sottosezioni, sotto-sottosezioni
e paragrafi sono a bandiera e senza sillabazione: vanno a capo solo fra le parole
(`\titleformat` in `settings/custom.tex`). Verificato: nessun titolo di sezione nel PDF
termina una riga con un trattino.

Tutti i capitoli a 0 differenze; compilazione senza errori né Overfull.

## F10. Controllo finale (punto 10), capitolo per capitolo

**Stato:** completato il 7/9/2026, tutti i blocchi confermati dall'utente. Metodo in
`plan.md` (punto 10): per ogni capitolo, correzioni sicure applicate direttamente e
registrate in `cap_N.md`, dubbi nella sezione «Da decidere», conferma dell'utente a fine
capitolo. Ordine: controllo C citazioni (fatto,
`controllo_citazioni.md`) → cap. 1 → 2 → 3 → 4 → front matter (`cap_0.md`) →
appendice (`cap_A.md`).

Preparazione: i vecchi `cap_1..4.md` (verbali di fedeltà della migrazione) sono stati
tolti; i verificatori scrivono ora in `strumenti/verifica_cap_N.md` (`out` in
`strumenti/vcfg1..3.json`, `OUT` in `strumenti/verify4.py`), così `cap_N.md` resta il
verbale delle correzioni.

| Capitolo | Stato | Correzioni | Da decidere |
|---|---|---|---|
| 1 | fatto e confermato (6/9/2026) | 9 grassetti su punteggiatura tolti, 2 spazi unificatori (`~`) resi normali, «seconda infanzia» → «prima infanzia», «una elevata» → «un'elevata», «Clancy Blair e Cybele Raver» → «Blair e Raver», vedove e orfane vietate in tutta la tesi | nessuno |
| 2 | fatto e confermato (6/9/2026) | citazione autore-anno rimasta in chiaro convertita in `\cite` (unica in tutta la tesi), 7 grassetti su punteggiatura tolti, 6 spazi unificatori resi normali, spazio prima del punto, «nei bambini ritardo globale» → «nei bambini con ritardo globale», «una alterazione» → «un'alterazione» (2), «Sonuga-Barke» non più spezzato, «p factor» in tondo, «comorbilità» → «comorbidità» | nessuno (DSM-5 e le quattro forme estese di ADHD restano come sono, su decisione dell'utente) |
| 3 | fatto e confermato (6/9/2026) | «assesment» → «assessment»; regola dei corsivi (B: corsivo solo per i nomi degli strumenti e delle sottoscale, tondo per i termini stranieri comuni) applicata a tutta la tesi, capitolo 4 compreso; due ripetizioni riscritte (§3.6, §3.1.1) | nessuno |
| 4 | fatto e confermato (7/9/2026), chiuso dopo il controllo sistematico sugli Excel | titolo «4.4 Discussione» aggiunto (contatore non più forzato); «Early Executive Function Questionnaire» → «Functions» (2); citazione del BOI staccata dalla parola; «nella 4.4.1» → «nella sezione 4.4.1» (3); «Sezione» → «sezione»; virgolette dritte «"Mai"» → «“Mai”»; «Baby-/FE» e «EE-/FQ», «Invento-/ry», «Question-/naire» non più spezzati (`\babelhyphenation`); Tabella 4.1 con le visite sdoppiate in «suggerite»/«effettuate» (verificato sull'Excel: spiega il 3 del Caso 2) e testo di §4.3.1 adeguato; Tabella 4.26 con le righe Media/DS in tondo; percentili in cifre in §4.4.1; DS sciolta in §4.2.1; numeri degli 8 casi, 26 didascalie e 23 raccordi controllati e confrontati con i due Excel con lo script `strumenti/controllo_dati_cap4.py` (620 controlli, 0 discrepanze) | soglie 10°/20° dell'EEFQ nella nota della Tabella 4.26 (due valori a 0,1 dal ricalcolo), «circa 34 e 38 anni» (dataset: 34,6 e 37,9); nessuna nota sul totale a 13 prove della Tabella 4.25, su decisione dell'utente |
| Front matter | fatto e confermato (7/9/2026) | «Candidato:» → «Candidata:» sul frontespizio; ringraziamenti, introduzione e abstract identici ai Word, indice ed elenco delle tabelle completi, numerazione delle pagine corretta (`cap_0.md`) | nessuno (EEFQ resta sigla negli abstract, su decisione dell'utente) |
| Appendice | fatto e confermato (7/9/2026) | 24 correzioni di forma nelle 15 tabelle e nella legenda: refusi («PUNTEGGI0», «delyed», «causale»), virgolette non chiuse, spazi, accordi grammaticali, «procedere con la richiesta 2», punteggi tutti in grassetto, legenda ricomposta con le icone accanto alle voci giuste (`cap_A.md`) | nessuno («di costituire» resta, su decisione dell'utente) |

**Finalizzazione (7/9/2026).** Ricompilazione pulita da zero (`latexmk -C` e poi build
completo): 185 pagine, 0 errori, 0 Overfull, 0 Underfull, 0 avvisi LaTeX, 0 avvisi biber;
nessun riferimento irrisolto («??») né segnaposto nel PDF; 102 voci in bibliografia = 102
voci nel `.bib` = 102 chiavi citate; tutti i font incorporati; link senza bordi né colori
(stampa pulita). Aggiunti i metadati del file PDF in `settings/custom.tex` (`\hypersetup`:
titolo, autrice, oggetto, lingua), prima vuoti. Il PDF finale è `tesi/main.pdf`.

Vedove e orfane: **deciso e fatto** al capitolo 1 (l'utente ha preferito non aspettare la
fine). `\widowpenalty` e `\clubpenalty` a 10000 in `settings/custom.tex`, agganciati a
`\extrasitalian` perché babel-italian li riporta a 3000 a ogni selezione dell'italiano
(inizio documento e dopo l'abstract inglese): con l'assegnazione semplice non cambiava
nulla. Verificato: nessuna vedova o orfana in tutta la tesi, 185 pagine, le 26 tabelle del
capitolo 4 nello stesso posto di prima, 0 differenze in tutti i capitoli. Dettagli in
`cap_1.md`, correzione 13.
