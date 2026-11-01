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
  <b>Cebuano</b>
</p>
<!-- /i18n -->

<p align="center"><sub>Hubad sa README nga Iningles; kung lahi, ang Iningles ang sundon. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Mga font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Ang typeface nga gidrowing para sa [RIPPS2](https://github.com/akilluminati47/RIPPS2), ang front end sa PS2: ang mga menu niini, mga hint sa button, mga setting, ang pulong sa view nga nagngalan sa matag lista, ug matag tema nga gustong magtan-aw nga sakop niini.

Ang mga letra mosunod sa sinulat sa logo sa PS2: usa ka nipis ug patas nga linya, kuwadradong mga kanto, mga letra nga gitukod gikan sa pahigda ug patindog nga mga bar sa usa ka grid, ug ang abli nga mga porma sa logo mismo (ang P nga walay tangkay ibabaw sa tiyan niini, ang zigzag nga 2). Pig-ot sila, mao nga ang usa ka tibuok laray sa mga hint sa button mohaum sa screen nga 640 pixel.

| Cut | Gibag-on | Gidak-on sa letra | Sa RIPPS2 |
|---|---|---|---|
| **Regular** | nipis nga linya | dagkong letra (ang gagmay gidrowing nga dako) | mga hint, menu, setting, ang ngalan sa source |
| **Bold** | baga nga linya | dagkong letra | mga label tupad sa dagkong glyph, ang pulong sa view, ang linya sa release |
| **Bold Case** | baga nga linya | tinuod nga gagmay nga letra | gi-type nga teksto, ang keyboard sa screen, mga paghulagway |

## Silip

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Set sa mga karakter

Basic Latin, Latin-1 ug Latin Extended-A/B: 337 ka code point sa matag cut. Sa pagkakaron, ang mga letra nga may tuldik gidrowing ingon nga ilang batakang letra. Ang tibuok lista: [docs/charset.md](docs/charset.md).

## I-download

Gikan sa [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), o direkta gikan niining repo:

| Format | Mga file |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): ang samang tulo |

## Paggamit

**Sa usa ka tema sa RIPPS2** anaa na sa sulod sa `RIPPS2.elf` ang mga font; nganli lang sila ug ayaw pagpadala og bisan unsa:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

Ang [RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) tibuok nga gisulat niini. Bisan unsang laing tema sa pamilya sa OPL makagamit sa mga TTF gikan sa kaugalingon niining folder sama sa bisan unsang font.

**Sa web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Sa PC:** i-install ang mga TTF sama sa naandan. Ang Regular ug Bold usa ka pamilya, *RIPPS2 Sleek*; ang Bold Case kaugalingong pamilya, *RIPPS2 Sleek Case* (Bold), aron dili sila magbangga.

## Paghimo

Ang matag glyph usa ka hugpong sa mga polyline sa usa ka grid nga unom ka unit ang gitas-on (ang gitas-on sa dagkong letra); ang matag usa gihatagan og linya ug ang mga linya gihiusa ngadto sa usa ka limpyo nga outline. Ang drowing anaa sa [tools/make_sleek_font.py](tools/make_sleek_font.py) (ang samang file nga gigikanan sa mga kopya sa RIPPS2); ang [tools/build.py](tools/build.py) maghimo sa tanan dinhi gikan niini ug mohatag sa mga font og mga ngalan ug gibag-on nga gibasa sa mga desktop app ug browser (outline ra ang gibasa sa RIPPS2).

```
pip install -r requirements.txt
python tools/build.py
```

## Lisensya

- Ang mga font: [SIL Open Font License 1.1](LICENSE-OFL). Gamita, iapil, usba; ang giusab nga font adunay bag-ong ngalan.
- Ang mga himan: [MIT](LICENSE-MIT).

Wala dinhi: ang Planet N Compact, ang nag-unang typeface sa teksto sa RIPPS2, iya sa [Iconian Fonts](https://www.iconian.com) ug magpabilin nga ila; ang RIPPS2 One, usa ka tapak nga usa ra ka glyph para sa 1 niini, kauban niini.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Mga font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

