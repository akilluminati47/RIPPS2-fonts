<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <b>Italiano</b> |
  <a href="README.nl.md">Nederlands</a> |
  <a href="README.da.md">Dansk</a> |
  <a href="README.sv.md">Svenska</a> |
  <a href="README.pl.md">Polski</a> |
  <a href="README.cs.md">Čeština</a> |
  <a href="README.hr.md">Hrvatski</a> |
  <a href="README.sr.md">Srpski</a> |
  <a href="README.bg.md">Български</a> |
  <a href="README.ru.md">Русский</a> |
  <a href="README.el.md">Ελληνικά</a> |
  <a href="README.hu.md">Magyar</a> |
  <a href="README.ro.md">Română</a> |
  <a href="README.gl.md">Galego</a> |
  <a href="README.sq.md">Shqip</a> |
  <a href="README.tr.md">Türkçe</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fa.md">فارسی</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Traduzione del README inglese; se differiscono, vale l’inglese. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Scarica</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sito</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Il carattere disegnato per [RIPPS2](https://github.com/akilluminati47/RIPPS2), il front end per PS2: i suoi menu, i suggerimenti dei tasti, le impostazioni, la parola di vista che dà nome a ogni lista e ogni tema che voglia sembrare di casa.

Le lettere prendono a modello la scritta del logo PS2: un tratto sottile e uniforme, angoli squadrati, lettere fatte di barre orizzontali e verticali su una griglia, e le forme aperte del logo stesso (la P senza asta sopra la pancia, il 2 a zigzag). Sono strette, così un’intera fila di suggerimenti dei tasti sta in uno schermo da 640 pixel.

| Taglio | Peso | Maiuscole/minuscole | In RIPPS2 |
|---|---|---|---|
| **Regular** | tratto sottile | maiuscole (le minuscole si vedono maiuscole) | suggerimenti, menu, impostazioni, il nome della sorgente |
| **Bold** | tratto spesso | maiuscole | etichette accanto ai glifi grandi, la parola di vista, la riga della versione |
| **Bold Case** | tratto spesso | vere minuscole | testo digitato, la tastiera su schermo, descrizioni |

<a id="preview"></a>

## Anteprima

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## Set di caratteri

Latino di base, Latin-1 e Latino esteso A/B: 337 punti di codice in ogni taglio. Per ora le lettere accentate si vedono come la loro lettera base. L’elenco completo: [docs/charset.md](docs/charset.md).

## Download

Dalle [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), o direttamente da questo repository:

| Formato | File |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): gli stessi tre |

<a id="use"></a>

## Uso

**In un tema di RIPPS2** i font sono già dentro `RIPPS2.elf`; basta nominarli, senza fornire nulla:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) è composto tutto con questi. Qualsiasi altro tema della famiglia OPL può usare i TTF dalla propria cartella come qualsiasi font.

**Sul web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Su PC:** installa i TTF come al solito. Regular e Bold sono una famiglia, *RIPPS2 Sleek*; Bold Case è una famiglia a sé, *RIPPS2 Sleek Case* (Bold), così non si scontrano mai.

<a id="build"></a>

## Compilazione

Ogni glifo è un insieme di polilinee su una griglia alta sei unità (l’altezza delle maiuscole); ognuna viene tracciata e i tratti uniti in un solo contorno pulito. Il disegno si trova in [tools/make_sleek_font.py](tools/make_sleek_font.py) (lo stesso file da cui RIPPS2 crea le sue copie); [tools/build.py](tools/build.py) ne ricava tutto quello che c’è qui e dà ai font i nomi e i pesi che leggono le applicazioni desktop e i browser (RIPPS2 legge solo i contorni).

```
pip install -r requirements.txt
python tools/build.py
```

<a id="licence"></a>

## Licenza

- I font: [SIL Open Font License 1.1](LICENSE-OFL). Usali, includili, modificali; un font modificato prende un nome nuovo.
- Gli strumenti: [MIT](LICENSE-MIT).

Non è qui: Planet N Compact, il carattere principale del testo di RIPPS2, è di [Iconian Fonts](https://www.iconian.com) e resta loro; RIPPS2 One, una toppa di un solo glifo per il suo 1, va con esso.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Scarica</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sito</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

