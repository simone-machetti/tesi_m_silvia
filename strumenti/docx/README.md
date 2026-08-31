# Estrazione del capitolo 4 in Word

Genera `capitolo_4_tesi.docx`: il solo capitolo 4, con le 26 tabelle e in fondo la
bibliografia delle opere citate nel capitolo.

## Perché serve una procedura e non un solo comando

Due limiti di pandoc 2.9 (la versione installata):

- **non ha `pandoc-citeproc` né `--citeproc`**, quindi non sa risolvere i `\cite{}`.
  La bibliografia viene perciò ricavata compilando un estratto LaTeX e riprendendone
  il testo già formattato dallo stile IEEE: le voci risultano identiche a quelle della tesi.
- **non legge le larghezze di colonna** dalle tabelle LaTeX. Senza larghezze Word
  dimensiona le colonne sul contenuto e le tabelle sforano il margine: vanno quindi
  scritte a mano nel `.docx` dopo la conversione.

## Passi

```bash
bash strumenti/docx/build_estratto.sh          # compila l'estratto: numeri e bibliografia
python3 strumenti/docx/mkdocx.py               # produce il .tex autoconsistente
pandoc -f latex -t docx \
       --reference-doc=strumenti/docx/riferimento.docx \
       /tmp/.../cap4_docx.tex -o capitolo_4_tesi.docx
python3 strumenti/docx/patch_docx.py           # geometria pagina + larghezze tabelle
```

## Scelte

- **Citazioni rinumerate da 1 a 11**, nell'ordine in cui compaiono nel capitolo: un estratto
  autonomo con i numeri della tesi (`[4]`, `[41]`…) sarebbe illeggibile e la bibliografia
  avrebbe buchi.
- **Numeri scritti in chiaro** — titoli di sezione, «Tabella 4.7:», «nella Tabella 4.7» —
  perché Word non li genera da solo.
- **`riferimento.docx`**: documento di riferimento di pandoc con lo stile *Body Text*
  giustificato.
- **Pagina A4, margini 2,5 cm, tabelle larghe esattamente quanto il testo** (16 cm),
  a impaginazione fissa. La tabella dei fattori di rischio e quella delle prestazioni
  complessive usano un corpo ridotto: con otto e cinque colonne le intestazioni non
  entrerebbero e Word spezzerebbe le parole a metà.

## Verifiche fatte sul file prodotto

- 26 tabelle confrontate **cella per cella** con `source/capitolo_4.docx`: identiche.
- Confronto parola per parola con l'originale: nessun testo perso.
- Conversione in PDF e controllo dei riquadri: **nessuna parola fuori dai margini**.
