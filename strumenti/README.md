# Strumenti della migrazione

Script usati per portare i capitoli da `source/*.docx` a `tesi/main/*.tex` e per
verificare che il testo non sia cambiato. Servono a **rifare** o **ricontrollare** la
migrazione: se non ti interessano, questa cartella si può cancellare senza toccare la tesi.

## Come funziona

I `.docx` non vengono letti direttamente: prima si passano per pandoc, che produce LaTeX
con la punteggiatura tipografica e gli escape corretti.

```bash
cd source
pandoc -f docx -t latex --wrap=none capitolo_1.docx -o /tmp/conv/capitolo_1.tex
pandoc -f docx -t markdown --wrap=none capitolo_1.docx -o /tmp/conv/capitolo_1.md
```

Il `.tex` alimenta la conversione, il `.md` serve come termine di paragone nella verifica.
I percorsi dei file intermedi sono scritti dentro i `.json` e vanno aggiornati se cambi
cartella.

## Script

| File | Cosa fa |
|---|---|
| `convert.py` | capitoli 1-3: titoli LaTeX + citazioni `\cite{}`. Contiene la mappa citazione → chiave bib. **Si ferma con errore se incontra una citazione che non sa agganciare**, così nessuna passa inosservata. |
| `convert4.py` | capitolo 4: come sopra, più la ricostruzione della struttura (nel Word gli stili di titolo sono incoerenti) e la riscrittura delle 26 tabelle nello stile del template. |
| `verify.py` | capitoli 1-3: riduce Word e LaTeX a parole e li confronta. Scrive `cap_N.md`. |
| `verify4.py` | capitolo 4: come sopra, includendo le celle delle tabelle e i titoli non numerati. Scrive `cap_4.md`. |

```bash
python3 convert.py cfg1.json     # scrive tesi/main/1_capitolo_1.tex
python3 verify.py  vcfg1.json    # scrive cap_1.md
python3 convert4.py              # capitolo 4 (percorsi dentro lo script)
python3 verify4.py               # scrive cap_4.md
```

## Se aggiungi voci a References.bib

`tesi/tail/ordine_bibliografia.tex` fissa l'ordine di stampa della bibliografia e va
rigenerato:

```bash
cd tesi
grep -o '^@[a-z]*{[^,]*' tail/References.bib | sed 's/.*{//' > /tmp/keys.txt
```

poi si riscrivono le righe `\nocite{...}` in gruppi da quattro, nell'ordine del file.
