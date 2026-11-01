<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.it.md">Italiano</a> |
  <b>Nederlands</b> |
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

<p align="center"><sub>Vertaling van de Engelse README; bij verschillen geldt het Engels. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Downloaden</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thema's</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Lettertypen</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Het lettertype getekend voor [RIPPS2](https://github.com/akilluminati47/RIPPS2), de PS2-front end: de menu’s, knophints, instellingen, het weergavewoord dat elke lijst een naam geeft, en elk thema dat erbij wil horen.

De letters nemen het schrift van het PS2-logo als voorbeeld: één dunne, gelijkmatige lijn, rechte hoeken, letters opgebouwd uit horizontale en verticale balken op een raster, en de open vormen van het logo zelf (de P zonder stok boven de buik, de zigzag-2). Ze zijn smal, zodat een volle rij knophints op een scherm van 640 pixels past.

| Snit | Dikte | Kast | In RIPPS2 |
|---|---|---|---|
| **Regular** | dunne lijn | hoofdletters (kleine letters worden hoofdletters) | hints, menu’s, instellingen, de bronnaam |
| **Bold** | dikke lijn | hoofdletters | labels naast grote glyphs, het weergavewoord, de versieregel |
| **Bold Case** | dikke lijn | echte kleine letters | getypte tekst, het schermtoetsenbord, beschrijvingen |

## Voorbeeld

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Tekenset

Basis-Latijn, Latin-1 en Latijn Uitgebreid-A/B: 337 codepunten in elke snit. Letters met accenten worden voorlopig als hun basisletter getekend. De volledige lijst: [docs/charset.md](docs/charset.md).

## Downloaden

Via [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), of rechtstreeks uit deze repo:

| Formaat | Bestanden |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): dezelfde drie |

## Gebruik

**In een RIPPS2-thema** zitten de lettertypen al in `RIPPS2.elf`; noem ze en lever niets mee:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) is er helemaal in gezet. Elk ander thema uit de OPL-familie kan de TTF’s uit zijn eigen map gebruiken zoals elk lettertype.

**Op het web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Op een pc:** installeer de TTF’s zoals gewoonlijk. Regular en Bold zijn één familie, *RIPPS2 Sleek*; Bold Case is een eigen familie, *RIPPS2 Sleek Case* (Bold), zodat ze elkaar nooit in de weg zitten.

## Bouwen

Elke glyph is een reeks polylijnen op een raster van zes eenheden hoog (de kapitaalhoogte); elke lijn krijgt een streek en de streken worden samengevoegd tot één schone omtrek. De tekening staat in [tools/make_sleek_font.py](tools/make_sleek_font.py) (hetzelfde bestand waar RIPPS2 zijn kopieën van bouwt); [tools/build.py](tools/build.py) maakt hier alles uit en geeft de lettertypen de namen en diktes die desktopprogramma’s en browsers lezen (RIPPS2 leest alleen de omtrekken).

```
pip install -r requirements.txt
python tools/build.py
```

## Licentie

- De lettertypen: [SIL Open Font License 1.1](LICENSE-OFL). Gebruik ze, bundel ze, verander ze; een veranderd lettertype krijgt een nieuwe naam.
- De hulpmiddelen: [MIT](LICENSE-MIT).

Niet hier: Planet N Compact, de hoofdtekstletter van RIPPS2, is van [Iconian Fonts](https://www.iconian.com) en blijft van hen; RIPPS2 One, een lapje van één glyph voor de 1, hoort erbij.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Downloaden</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thema's</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Lettertypen</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

