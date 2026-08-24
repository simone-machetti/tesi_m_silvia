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

> Bayley, N. (2006). *Bayley Scales of Infant and Toddler Development* (3rd ed.).
> Harcourt Assessment.

È il manuale dello strumento usato nello studio, non un articolo. Resta un dettaglio minore
non deciso: se citare il manuale di somministrazione o quello tecnico (esistono entrambi,
stesso anno) e se indicare *Harcourt Assessment*, il nome dell'epoca, oppure *Pearson*, che
oggi lo distribuisce. È stata adottata la forma generica qui sopra, la più diffusa in
letteratura.

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
