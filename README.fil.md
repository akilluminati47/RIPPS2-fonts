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
  <b>Filipino</b> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Salin ng README sa Ingles; kung magkaiba, ang Ingles ang masusunod. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Mga font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Ang typeface na iginuhit para sa [RIPPS2](https://github.com/akilluminati47/RIPPS2), ang front end ng PS2: ang mga menu nito, mga hint ng button, mga setting, ang salita ng view na nagpapangalan sa bawat listahan, at bawat tema na gustong magmukhang kabilang dito.

Ang mga titik ay ginaya sa sulat ng logo ng PS2: isang manipis at pantay na guhit, kuwadradong mga sulok, mga titik na binuo mula sa pahalang at patayong mga bar sa isang grid, at ang mga bukas na hugis ng logo mismo (ang P na walang tangkay sa ibabaw ng tiyan nito, ang zigzag na 2). Makikitid ang mga ito, kaya kasya ang isang buong hanay ng mga hint ng button sa screen na 640 pixel.

| Cut | Kapal | Laki ng titik | Sa RIPPS2 |
|---|---|---|---|
| **Regular** | manipis na guhit | malalaking titik (ang maliliit ay iginuguhit na malaki) | mga hint, menu, setting, ang pangalan ng source |
| **Bold** | makapal na guhit | malalaking titik | mga label sa tabi ng malalaking glyph, ang salita ng view, ang linya ng release |
| **Bold Case** | makapal na guhit | tunay na maliliit na titik | tinipang teksto, ang on-screen keyboard, mga paglalarawan |

## Silip

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Set ng mga character

Basic Latin, Latin-1 at Latin Extended-A/B: 337 code point sa bawat cut. Sa ngayon, iginuguhit ang mga titik na may tuldik bilang kanilang batayang titik. Ang buong listahan: [docs/charset.md](docs/charset.md).

## I-download

Mula sa [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), o direkta mula sa repo na ito:

| Format | Mga file |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): ang parehong tatlo |

## Paggamit

**Sa isang tema ng RIPPS2** nasa loob na ng `RIPPS2.elf` ang mga font; pangalanan lang ang mga ito at walang ipapadala:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

Ang [RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) ay buong isinulat gamit ang mga ito. Anumang ibang tema sa pamilya ng OPL ay puwedeng gumamit ng mga TTF mula sa sarili nitong folder tulad ng anumang font.

**Sa web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Sa PC:** i-install ang mga TTF gaya ng dati. Ang Regular at Bold ay iisang pamilya, *RIPPS2 Sleek*; ang Bold Case ay sariling pamilya, *RIPPS2 Sleek Case* (Bold), kaya hindi sila nagbabanggaan.

## Pagbuo

Bawat glyph ay isang hanay ng mga polyline sa isang grid na anim na unit ang taas (ang taas ng malaking titik); bawat isa ay ginuguhitan at pinagsasama ang mga guhit sa iisang malinis na balangkas. Ang guhit ay nasa [tools/make_sleek_font.py](tools/make_sleek_font.py) (ang parehong file na pinagmumulan ng mga kopya ng RIPPS2); ang [tools/build.py](tools/build.py) ang gumagawa ng lahat ng narito mula roon at nagbibigay sa mga font ng mga pangalan at kapal na binabasa ng mga desktop app at browser (balangkas lang ang binabasa ng RIPPS2).

```
pip install -r requirements.txt
python tools/build.py
```

## Lisensya

- Ang mga font: [SIL Open Font License 1.1](LICENSE-OFL). Gamitin, isama, baguhin; ang binagong font ay may bagong pangalan.
- Ang mga tool: [MIT](LICENSE-MIT).

Wala rito: ang Planet N Compact, ang pangunahing typeface ng teksto ng RIPPS2, ay pag-aari ng [Iconian Fonts](https://www.iconian.com) at nananatiling kanila; ang RIPPS2 One, isang tagpi na iisang glyph para sa 1 nito, ay kasama nito.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Mga font</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

