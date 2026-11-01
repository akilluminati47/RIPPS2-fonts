<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <b>Deutsch</b> |
  <a href="README.it.md">Italiano</a> |
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

<p align="center"><sub>Übersetzung der englischen README; bei Abweichungen gilt das Englische. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Themes</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Schriften</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Die Schrift, gezeichnet für [RIPPS2](https://github.com/akilluminati47/RIPPS2), das PS2-Frontend: seine Menüs, Tastenhinweise, Einstellungen, das Ansichtswort, das jede Liste benennt, und jedes Theme, das dazugehören will.

Die Buchstaben nehmen sich den Schriftzug des PS2-Logos zum Vorbild: ein dünner, gleichmäßiger Strich, eckige Ecken, Buchstaben aus waagerechten und senkrechten Balken auf einem Raster, und die offenen Formen des Logos selbst (das P ohne Stamm über dem Bauch, die Zickzack-2). Sie sind schmal, sodass eine ganze Reihe Tastenhinweise auf einen 640 Pixel breiten Bildschirm passt.

| Schnitt | Stärke | Schreibung | In RIPPS2 |
|---|---|---|---|
| **Regular** | dünner Strich | Großbuchstaben (Kleinbuchstaben werden groß gezeichnet) | Hinweise, Menüs, Einstellungen, der Quellenname |
| **Bold** | kräftiger Strich | Großbuchstaben | Beschriftungen neben großen Glyphen, das Ansichtswort, die Versionszeile |
| **Bold Case** | kräftiger Strich | echte Kleinbuchstaben | getippter Text, die Bildschirmtastatur, Beschreibungen |

## Vorschau

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Zeichensatz

Basis-Lateinisch, Latin-1 und Lateinisch Erweitert-A/B: 337 Codepunkte in jedem Schnitt. Buchstaben mit Akzent werden vorerst als ihr Grundbuchstabe gezeichnet. Die ganze Liste: [docs/charset.md](docs/charset.md).

## Download

Unter [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) oder direkt aus diesem Repo:

| Format | Dateien |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (Web) | [fonts/woff2](fonts/woff2): dieselben drei |

## Verwendung

**In einem RIPPS2-Theme** stecken die Schriften schon in `RIPPS2.elf`; einfach benennen, nichts mitliefern:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) ist ganz in ihnen gesetzt. Jedes andere Theme der OPL-Familie kann die TTFs wie jede Schrift aus seinem eigenen Ordner nutzen.

**Im Web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Am PC:** die TTFs wie gewohnt installieren. Regular und Bold sind eine Familie, *RIPPS2 Sleek*; Bold Case ist eine eigene Familie, *RIPPS2 Sleek Case* (Bold), damit sich die beiden nie in die Quere kommen.

## Erstellen

Jede Glyphe ist eine Reihe von Polylinien auf einem Raster von sechs Einheiten Höhe (der Versalhöhe); jede wird nachgezogen und die Striche zu einer einzigen sauberen Kontur vereinigt. Die Zeichnung steht in [tools/make_sleek_font.py](tools/make_sleek_font.py) (derselben Datei, aus der RIPPS2 seine Kopien baut); [tools/build.py](tools/build.py) macht daraus alles hier und gibt den Schriften die Namen und Stärken, die Desktop-Programme und Browser lesen (RIPPS2 selbst liest nur die Konturen).

```
pip install -r requirements.txt
python tools/build.py
```

## Lizenz

- Die Schriften: [SIL Open Font License 1.1](LICENSE-OFL). Nutzen, beilegen, verändern; eine veränderte Schrift bekommt einen neuen Namen.
- Die Werkzeuge: [MIT](LICENSE-MIT).

Nicht hier: Planet N Compact, die Haupttextschrift von RIPPS2, gehört [Iconian Fonts](https://www.iconian.com) und bleibt deren; RIPPS2 One, ein Ein-Glyphen-Flicken für ihre 1, gehört dazu.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Themes</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Schriften</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

