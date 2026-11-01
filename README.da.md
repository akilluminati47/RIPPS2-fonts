<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.it.md">Italiano</a> |
  <a href="README.nl.md">Nederlands</a> |
  <b>Dansk</b> |
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

<p align="center"><sub>Oversættelse af den engelske README; hvis de afviger, gælder den engelske. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Hent</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temaer</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Skrifttyper</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Websted</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Skrifttypen tegnet til [RIPPS2](https://github.com/akilluminati47/RIPPS2), PS2-frontenden: dens menuer, knaphints, indstillinger, visningsordet der navngiver hver liste, og hvert tema der vil se ud som en del af den.

Bogstaverne har PS2-logoets skrift som forbillede: én tynd, jævn streg, firkantede hjørner, bogstaver bygget af vandrette og lodrette bjælker på et gitter, og logoets egne åbne former (P’et uden stamme over buen, zigzag-2’tallet). De er smalle, så en hel række knaphints passer på en skærm på 640 pixels.

| Snit | Vægt | Bogstaver | I RIPPS2 |
|---|---|---|---|
| **Regular** | tynd streg | versaler (små bogstaver tegnes som versaler) | hints, menuer, indstillinger, kildens navn |
| **Bold** | kraftig streg | versaler | etiketter ved store glyffer, visningsordet, versionslinjen |
| **Bold Case** | kraftig streg | ægte små bogstaver | indtastet tekst, skærmtastaturet, beskrivelser |

## Forhåndsvisning

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Tegnsæt

Basislatin, Latin-1 og Udvidet Latin A/B: 337 kodepunkter i hvert snit. Bogstaver med accent tegnes indtil videre som deres grundbogstav. Hele listen: [docs/charset.md](docs/charset.md).

## Hent

Fra [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), eller direkte fra dette repo:

| Format | Filer |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): de samme tre |

## Brug

**I et RIPPS2-tema** ligger skrifttyperne allerede i `RIPPS2.elf`; navngiv dem og send intet med:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) er sat helt i dem. Ethvert andet tema i OPL-familien kan bruge TTF-filerne fra sin egen mappe som enhver skrifttype.

**På nettet:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**På en pc:** installér TTF-filerne som sædvanligt. Regular og Bold er én familie, *RIPPS2 Sleek*; Bold Case er sin egen familie, *RIPPS2 Sleek Case* (Bold), så de to aldrig støder sammen.

## Byg

Hver glyf er et sæt polylinjer på et gitter seks enheder højt (versalhøjden); hver får en streg, og stregerne smeltes sammen til én ren kontur. Tegningen ligger i [tools/make_sleek_font.py](tools/make_sleek_font.py) (den samme fil, som RIPPS2 bygger sine kopier fra); [tools/build.py](tools/build.py) laver alt her ud fra den og giver skrifttyperne de navne og vægte, som skrivebordsprogrammer og browsere læser (RIPPS2 læser kun konturerne).

```
pip install -r requirements.txt
python tools/build.py
```

## Licens

- Skrifttyperne: [SIL Open Font License 1.1](LICENSE-OFL). Brug dem, pak dem med, ændr dem; en ændret skrifttype får et nyt navn.
- Værktøjerne: [MIT](LICENSE-MIT).

Ikke her: Planet N Compact, RIPPS2’s primære tekstskrift, tilhører [Iconian Fonts](https://www.iconian.com) og forbliver deres; RIPPS2 One, en rettelse på én glyf til dens 1-tal, hører med til den.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Hent</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temaer</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Skrifttyper</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Websted</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

