# Capitolo 4 — controllo finale (punto 10)

File: `tesi/main/4_capitolo_4.tex` (pagine stampate 95–139). Word di riferimento: `source/capitolo_4.docx`.
Metodo (vedi `plan.md`, punto 10): lettura integrale dei 145 capoversi e delle 26 tabelle,
controlli meccanici A–H, **controllo F su tutti gli otto casi** (ogni numero della prosa
confrontato con le tabelle), rilettura delle 26 didascalie e delle 23 frasi di raccordo di
`tabelle.md`, correzioni sicure applicate direttamente e registrate qui, dubbi nella sezione
«Da decidere». Dopo ogni modifica: ricompilazione e verifica di fedeltà
(`strumenti/verifica_cap_4.md`).

**Stato:** tutte le correzioni applicate e confermate dall'utente (7/9/2026), compresi i
quattro punti «da decidere», due dei quali verificati sui dati grezzi (i due Excel in
`source/`).

## Correzioni applicate

Le correzioni di testo (2, 4, 5) e quelle che cambiano la spaziatura vista dal verificatore
(3) sono registrate in `strumenti/revisioni_cap4.json`; il titolo aggiunto (1) è nella
lista `TITOLI_AGGIUNTI` di `strumenti/verify4.py`. Il capitolo resta a **0 differenze**.

| N. | Posizione | Prima | Dopo | Categoria | Motivo |
|---|---|---|---|---|---|
| 1 | §4.4 | 4.4.1 e 4.4.2 senza titolo padre; numerazione forzata con `\setcounter` | nuovo titolo **«4.4 Discussione»** (`\section`, etichetta `sec:4_4`), contatore libero | struttura (deciso in `plan.md`, D) | nel Word mancava; l'indice ora mostra 4.4 sopra 4.4.1 e 4.4.2 |
| 2 | §4.1.2, 5° capoverso; §4.4.1, 1° capoverso | «Early Executive Function Questionnaire» | «Early Executive Function**s** Questionnaire» | refuso (nome proprio) | è il nome dello strumento (Hendry & Holmboe, 2021), già al plurale nel titolo di §4.2.3 e nelle altre 4 occorrenze |
| 3 | §4.2.3, 1° capoverso del BOI | «Behavior Observation Inventory[102]» (citazione attaccata alla parola) | «Behavior Observation Inventory [102]» | spazio | unico `\cite` della tesi senza `~` davanti; nel Word la citazione era attaccata |
| 4 | §4.4.2, 3°, 7° e 9° capoverso | «descritta nella 4.4.1», «mostrato nella 4.4.1», «discusso nella 4.4.1» | «…nella sezione 4.4.1» (3) | refuso (parola mancante) | così nel Word; ovunque altrove il rimando è «nella sezione …» |
| 5 | §4.3.3, 3° capoverso | «nella Sezione 4.3.2» | «nella sezione 4.3.2» | uniformità | unica «Sezione» maiuscola della tesi |
| 6 | §4.2.3, EEFQ, 3° capoverso | «"Mai" e "Sempre"» (virgolette dritte) | «“Mai” e “Sempre”» | refuso tipografico | virgolette dritte: in LaTeX escono storte; ora come nelle altre virgolette della tesi |
| 7 | §4.2.2 e §4.4.2 | «Baby-/FE» spezzato al trattino a fine riga (pagine 101 e 133) | «Baby-FE» tenuto unito con `\mbox{}` | impaginazione | come «Sonuga-Barke» al capitolo 2 |
| 8 | §4.2.3 e §4.3.3 (`settings/custom.tex`) | «Invento-ry», «Question-naire», «dell'EE-FQ» spezzati con le regole italiane | niente sillabazione per EEFQ, Inventory, Questionnaire | impaginazione | eccezioni con `\babelhyphenation[italian]`; il vecchio `\hyphenation{scoring}` nel preambolo finiva nelle regole inglesi e viene spostato lì. babel-italian tratta l'apostrofo come lettera, quindi «dell'EEFQ» va elencato a parte |

| 9 | Tabella 4.1 e §4.3.1, 2° capoverso | colonna «Visite specialistiche» (una sola), Caso 2 con «3» fattori ma due «SÌ» | colonne «Visite suggerite» e «Visite effettuate»; l'elenco dei fattori nel testo diventa «…il suggerimento di visite specialistiche, la loro effettuazione…» | contenuto (deciso dall'utente, verificato sull'Excel) | nel dataset le visite sono due variabili e il conteggio dei fattori le somma entrambe: il Caso 2 è l'unico con tutte e due a «sì», da cui il 3. I totali non cambiano; ora le colonne li spiegano. Le 9 righe della tabella sono registrate come revisioni. Con nove colonne la tabella sforava il margine destro di circa 4 mm (senza avviso nel log): su indicazione dell'utente «(mesi)» va a capo sotto «Età», la prima colonna ha l'intestazione «Caso» e sotto i soli numeri 1–8, e le colonne fisse sono state ristrette; «Pretermine» sta su una riga. Misurata sul PDF, la tabella è larga 14,3 cm su 14,7 di giustezza, con 2 mm di aria per lato e nessuna intestazione spezzata. **Ritocco finale (7/9/2026):** il log segnalava ancora «Preoccup.» e «Pretermine» più larghi della cella di 1,4 pt (avviso nascosto dal `grep` difettoso, vedi tasks.md); ridotto il margine interno delle celle da 3 a 2 pt e riportate le colonne a 1,9 / 1,6 cm: tabella larga 13,8 cm, 4,8 mm di aria per lato, 0 Overfull |
| 10 | Tabella 4.26 | righe «Media» e «DS» in grassetto | in tondo | uniformità (deciso dall'utente) | il grassetto resta solo ai punteggi almeno una DS sotto la media, come dice la nota |
| 11 | §4.4.1, 1°, 2°, 4° e 10° capoverso | «settantacinquesimo», «venticinquesimo», «cinquantesimo», «decimo» percentile (8) | «75°», «25°», «50°», «10°» | uniformità (deciso dall'utente) | come in §4.3.3 e nel resto di §4.4.1; registrate come revisioni |
| 12 | §4.2.1, 1° capoverso | «(DS = 4,8)» | «(deviazione standard, DS = 4,8)» | acronimo (deciso dall'utente) | prima occorrenza della sigla, mai sciolta |

Non fatto, su decisione dell'utente: la nota sulla regola del punteggio totale della
Tabella 4.25 (vedi «Da decidere» 2).

Già fatte al capitolo 3 e registrate in `cap_3.md` (correzione 2): regola dei corsivi
(«pre-step» e «modulo zero» in tondo, nomi degli strumenti in corsivo nella prosa, tondo
nei titoli e nelle didascalie) e i 6 spazi unificatori tolti attorno a quei termini.

## Da decidere

Nessun punto aperto. I quattro dubbi sottoposti all'utente, l'esito della verifica sui
dati grezzi e le decisioni prese:

1. **Tabella 4.1, Caso 2: «N. fattori = 3» ma le colonne dicevano 2.** Verificato
   sull'Excel (`source/BabyFe 2026 x analisi luglio 2026.xlsx`, codice 18CO-AC03): il
   questionario ha due variabili, «visite suggerite» e «visite fatte», entrambe a «sì» solo
   per il Caso 2; il conteggio dei fattori somma cinque variabili mentre la tabella ne
   mostrava quattro. Per gli altri sette casi i due conteggi coincidono. **Deciso:**
   sdoppiare la colonna (correzione 9), nessun totale cambia.
2. **Tabella 4.25: il punteggio totale è calcolato su 13 prove, non su 15, e nessuno lo
   dice.** Sommando i punteggi delle tabelle dei casi si ottiene un valore diverso dal
   totale (Caso 1: 20 contro 16). I totali tornano tutti, per tutti e otto i casi, se si
   escludono la prova 1 (Lettura condivisa) e la prova 15 (Gioco libero) e si contano fra
   le «prove non valide» anche i dati mancanti (n.d.):

   | Caso | somma prove 2–14 | totale in tabella | NV + n.d. fra le prove 2–14 | non valide in tabella |
   |---|---|---|---|---|
   | 1 | 16 | 16 | 0 | 0 |
   | 2 | 0 | 0 | 13 | 13 |
   | 3 | 2 | 2 | 0 | 0 |
   | 4 | 1 | 1 | 1 | 1 |
   | 5 | 7 | 7 | 3 | 3 |
   | 6 | 12 | 12 | 1 | 1 |
   | 7 | 3 | 3 | 1 + 1 | 2 |
   | 8 | 4 | 4 | 4 + 1 | 5 |

   Ma §4.2.3 dice solo «I punteggi ottenuti vengono successivamente sommati», le didascalie
   parlano di «quindici prove» e chi somma la Tabella 4.3 non ritrova il 16. **Proposta:**
   aggiungere alla nota della Tabella 4.25 una frase del tipo: «Il punteggio totale è la
   somma dei punteggi delle tredici prove dalla 2 alla 14: la Lettura condivisa e il Gioco
   libero, attività di apertura e di chiusura della batteria, non concorrono al punteggio.
   Le prove con dato mancante sono conteggiate fra le prove non valide.» Verificato
   sull'Excel, prova per prova, per tutti gli otto casi: totale e numero di prove non
   valide escono esattamente sommando le prove dalla 2 alla 14 e contando fra le non
   valide sia le prove rifiutate (codice 9) sia quelle con dato mancante (codice 8);
   l'Excel non dice perché le prove 1 e 15 siano escluse (il foglio di analisi riporta i
   totali già calcolati) e il protocollo in Appendice A assegna un punteggio 0–2 anche a
   quelle due prove. **Deciso dall'utente: nessuna nota.** La tesi resta com'è.
3. **Tabella 4.26: le righe «Media» e «DS» erano tutte in grassetto** (così nel Word), ma la
   nota dice che il grassetto segnala i punteggi almeno una deviazione standard sotto la
   media. **Deciso:** righe di riferimento in tondo (correzione 10).
4. **§4.4.1: percentili scritti in lettere** mentre §4.3.3 e lo stesso §4.4.1 usano «75°»,
   «10°», «20°». **Deciso:** cifre con «°» ovunque per i percentili (correzione 11); i
   conteggi in lettere («tredici prove», «quindici prove») restano.
5. **Sigla DS mai sciolta** (§4.2.1). **Deciso:** scritta per esteso alla prima occorrenza
   (correzione 12).

### Controllo sistematico sui dati grezzi (Excel in `source/`), 7/9/2026

Su richiesta dell'utente, prima di chiudere il capitolo, tutti i dati sono stati
ricontrollati con uno script (`strumenti/controllo_dati_cap4.py`) contro il dataset
completo (`BabyFe 2026 x analisi luglio 2026.xlsx`) e il foglio di analisi (`Analisi per
Sivia.xlsx`). Gli otto casi corrispondono ai codici 06MD-SF03, 18CO-AC03, 19AM-AC10,
23IB-AC05, AC08, VR07, AQ11, AQ07; i 66 bambini del campione sono le righe del dataset con
almeno una prova (esclusi VR12, AQ12, AQ08).

**620 controlli superati, 0 discrepanze** (l'unico avviso dello script, sulla
«preoccupazione» del Caso 7, è un falso positivo: la scheda dice «Non risulta espressa
preoccupazione», coerente con il dato):
- Tabella 4.1: genere, età, le cinque variabili di rischio e il totale, per tutti i casi;
- le 8 schede: genere, età, peso alla nascita, tipo di parto, problemi alla nascita,
  preoccupazione, visite suggerite/effettuate, bilinguismo, numero di figli, reddito
  percepito, cittadinanza (Caso 7), paese di nascita e mesi in Italia (Caso 8);
- le 8 tabelle delle prove: 120 punteggi (0/1/2, NV = codice 9, n.d. = codice 8) e la
  coerenza fra punteggio ed esito in ogni riga;
- le 7 tabelle BOI: 91 valori e la coerenza fra valore e frequenza; per il Caso 2 il
  dataset ha tutti i 13 item mancanti, coerente con «non disponibile»;
- Tabella 4.25: età, totale, prove non valide e collocazione percentile di ogni caso;
  totali e prove non valide ricalcolati dalle prove 2–14 coincidono con il foglio di
  analisi; le soglie della nota (10° = 3, 25° = 7, 50° = 11, 75° = 16, 90° = 18) sono
  riprodotte esattamente ricalcolando i percentili sui 66 totali (metodo SPSS);
- Tabella 4.26: i 30 punteggi EEFQ, medie e DS (arrotondamento a un decimale, mezzo verso
  l'alto), e le celle in grassetto = esattamente i valori almeno una DS sotto la media;
- §4.2.1: 66 bambini, 38 femmine (58 %), 28 maschi (42 %), età 18–38, media 29,2, DS 4,8,
  64 % esposti a più lingue, 97 % nati in Italia, diploma come titolo più frequente,
  reddito medio-basso, quattro nidi;
- le affermazioni numeriche di §4.3.3 e §4.4: intervalli dei totali e delle prove non
  valide, sei casi entro il 25°, tre sotto il 10°, punteggi per età, prove non valide
  citate per i Casi 2, 3, 4, 5 e 8.

**Due punti segnalati alla candidata; l'utente ha deciso di lasciare il testo così
com'è (7/9/2026).** Nessuna modifica fatta:
1. **Soglie del 10° e 20° percentile dell'EEFQ nella nota della Tabella 4.26** («IC = 2,8 e
   3,3; FX = 3,4 e 3,9; WM = 3,5 e 4,0; RG = 3,3 e 3,7»): non compaiono in nessuno dei due
   Excel. Ricalcolate sui 66 bambini con il metodo di SPSS (n = 65, 61, 65, 62 per
   sottoscala) risultano IC = **2,7** e 3,3; FX = 3,4 e 3,9; WM = 3,5 e 4,0; RG = 3,3 e
   **3,8**: due valori differiscono di 0,1. Nessun altro metodo o sottoinsieme (listwise
   n = 59, tutti i 69) riproduce i valori della nota. Se i valori corretti fossero 2,7 e 3,8,
   cambierebbe una sola frase: in §4.3.3 il Caso 6 (RG = 3,8) sarebbe «in corrispondenza
   del 20° percentile» anche nella regolazione, non «appena al di sopra». Tutte le altre
   collocazioni restano valide con entrambe le soglie.
2. **§4.2.1, «l'età media dei due genitori è di circa 34 e 38 anni»**: dal dataset 34,6 e
   37,9; arrotondando sarebbero «circa 35 e 38». Dettaglio.

### Verifica sui dati grezzi (prima lettura)

Oltre ai due punti sopra, sono stati confrontati con i due Excel e trovati identici:
genere, età e fattori di rischio degli otto casi (Tabella 4.1); i dati delle otto schede di
sintesi (peso alla nascita, tipo di parto, problemi, preoccupazione, visite, bilinguismo,
numero di figli, reddito percepito, paese di nascita e mesi in Italia del Caso 8); i 15
punteggi alle prove di ogni caso; totali, prove non valide e soglie dei percentili della
Tabella 4.25; i 30 punteggi EEFQ, le medie e le deviazioni standard della Tabella 4.26
(arrotondamenti compresi: per esempio 3,25 → 3,3 e 1,246 → 1,2); i numeri del campione in
§4.2.1 (66 bambini, 38 femmine 58 %, 28 maschi 42 %, età 18–38 mesi, media 29,2, DS 4,8,
64 % esposti a più lingue, 97 % nati in Italia, età dei genitori 34,6 e 37,9 anni, diploma
come titolo più frequente, reddito percepito medio-basso, quattro nidi di Genova).

## Controlli eseguiti senza rilievi

- **A. Ortografia e refusi.** Nessuna parola doppia, nessuno spazio doppio o prima della
  punteggiatura, nessuna punteggiatura doppia; accenti e apostrofi corretti; parentesi
  bilanciate. Nessun grassetto o spazio unificatore residuo di Word nella prosa (i
  grassetti sono solo nelle intestazioni delle tabelle e nelle celle evidenziate).
- **B. Grammatica e sintassi.** Letti tutti i 145 capoversi: accordi, concordanze e tempi
  corretti; «la bambina»/«il bambino» coerenti con il genere di ogni caso; nessuna frase
  sospesa.
- **C. Citazioni, rimandi, didascalie.** 10 `\cite`, tutti ora legati con `~`; 44 rimandi
  `\ref` (27 a tabelle, 9 a capitoli, 8 a sezioni), tutti al bersaglio giusto e ognuno
  dentro il proprio caso. Le 26 didascalie e le 23 frasi di raccordo di `tabelle.md`
  sono state rilette una per una: corrette e coerenti con le tabelle (nel Caso 2, senza
  tabella BOI, la frase dice che l'osservazione non è disponibile). Nessuna modifica.
- **D. Titoli.** 49 titoli identici al Word (numerati e non), più il nuovo 4.4; le voci
  «Caso 1»…«Caso 8» compaiono nell'indice sotto 4.3.2, senza numero, come previsto.
- **E. Terminologia.** Sigle sciolte alla prima occorrenza: EEFQ (§4.1.2), BOI (§4.4.1,
  prima volta che la sigla è usata), IC/FX/WM/RG (§4.3.3), N (§4.3.3). «Bayley-III» non è
  mai sciolto: è il nome proprio dello strumento, lasciato come DSM-5. «Baby-FE» sempre con
  il trattino (92 volte). Corsivi secondo la regola B (`cap_3.md`).
- **F. Numeri, su tutti gli otto casi.**
  - Età e genere: identici in Tabella 4.1, nelle otto schede, in Tabella 4.25 e nella prosa
    (27–38 mesi; «i tre casi di 27–29 mesi» = Casi 7, 6, 8 con 3, 12, 4; «37 e 38 mesi» =
    Casi 4 e 5 con 1 e 7).
  - Fattori di rischio: le colonne di Tabella 4.1 corrispondono alle schede per tutti i
    casi; il totale torna per sette casi su otto (Caso 2: vedi «Da decidere» 1).
  - Prestazioni: ogni affermazione della prosa sui singoli casi trova riscontro nelle
    tabelle delle prove (Caso 1: difficoltà su Memory con spostamento, Oggetto nascosto con
    spostamento, Sparabolle; Caso 3: due prove parziali, Gioco della statua e Asta con
    anelli; Caso 5: riuscite in Memory e Cubi nella scatola, 4 NV; Caso 6: riuscite in
    Lettura, Memory, Oggetto nascosto, Sparabolle; Caso 7: riuscite in Lettura, Sparabolle,
    Gioco libero; Caso 8: 4 NV + 1 n.d.).
  - Osservazione del comportamento: le sette descrizioni in prosa riportano esattamente i
    livelli delle tabelle BOI (per esempio Caso 6: entusiasmo 0, emozioni positive ed
    esplorazione 1, paura/ansia 1, tutto il resto 2 e distraibilità 0).
  - Tabella 4.25: i percentili di ogni caso sono coerenti con le soglie della nota (10° = 3,
    25° = 7, 50° = 11, 75° = 16); «sei casi entro il 25°», «tre sotto il 10°» (Casi 2, 3, 4),
    «tra 0 e 16», «prove non valide tra 0 e 13», «mediana 11»: tutto torna. Totali: vedi
    «Da decidere» 2.
  - Tabella 4.26: le celle in grassetto sono esattamente quelle almeno una DS sotto la
    media (IC < 3,2; FX < 3,9; WM ≤ 4,0; RG ≤ 4,0), e ogni collocazione rispetto al 10° e
    al 20° percentile scritta in §4.3.3 e §4.4.1 corrisponde alle soglie della nota (Caso 8
    sotto il 10° in IC e FX; Caso 5 in WM e RG; Casi 1 e 7 fra 10° e 20° in IC; Caso 4 in FX;
    Caso 7 in WM; Caso 1 = 10° in RG; Caso 6 = 20° in WM e appena sopra in RG; Caso 3 vicino
    alle medie). Dati mancanti (Caso 2 tutto, Caso 8 RG) coerenti con §4.3.3, §4.4.1 e §4.4.2.
  - Campione: 70 previsti, 66 valutati (38 femmine 58 %, 28 maschi 42 %: 38 + 28 = 66 ✓),
    «N = 66» ovunque; 15 prove, punteggio 0–2, EEFQ 28 item e risposte 1–7.
  - Fascia d'età: il capitolo parla di 18–36 mesi ma §4.2.1 dichiara 18–38 e due casi hanno
    37 e 38 mesi; il testo lo riconosce esplicitamente, quindi nessun intervento.
- **G. Impaginazione.** Nessuna vedova od orfana; nessun titolo in fondo a pagina; le 26
  tabelle stanno sulla pagina del primo richiamo o su quella dopo; nessun «Baby-/FE»,
  «EE-/FQ», «Invento-/ry» dopo le correzioni 7 e 8; la pagina 139 è l'ultima del capitolo.

## Verifica finale

- Compilazione: 185 pagine, 0 errori, 0 righe troppo lunghe (Overfull), 0 avvisi biber.
- Fedeltà al Word: `strumenti/verifica_cap_4.md` → 49 titoli, 10 citazioni, **0 differenze**
  (24 revisioni in `strumenti/revisioni_cap4.json`, titolo 4.4 in `TITOLI_AGGIUNTI`; il
  verificatore ora comprime gli spazi delle tabelle di pandoc prima di applicarle);
  capitoli 1, 2 e 3 a 0.
