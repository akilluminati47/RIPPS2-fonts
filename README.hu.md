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
  <b>Magyar</b> |
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

<p align="center"><sub>Az angol README fordítása; eltérés esetén az angol az irányadó. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Letöltés</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Témák</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Betűtípusok</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Weboldal</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

A [RIPPS2](https://github.com/akilluminati47/RIPPS2), a PS2 front end számára rajzolt betűtípus: a menüi, a gombtippek, a beállítások, a nézetszó, amely minden listát megnevez, és minden téma, amely odatartozónak akar látszani.

A betűk a PS2-logó feliratát veszik mintául: egyetlen vékony, egyenletes vonal, szögletes sarkok, rácson vízszintes és függőleges szárakból épített betűk, és maga a logó nyitott formái (a P szár nélkül a hasa fölött, a cikcakkos 2). Keskenyek, így egy teljes sor gombtipp elfér egy 640 pixel széles képernyőn.

| Változat | Vastagság | Kis- és nagybetű | A RIPPS2-ben |
|---|---|---|---|
| **Regular** | vékony vonal | nagybetűk (a kisbetűk nagybetűként jelennek meg) | tippek, menük, beállítások, a forrás neve |
| **Bold** | vastag vonal | nagybetűk | címkék nagy jelek mellett, a nézetszó, a verziósor |
| **Bold Case** | vastag vonal | valódi kisbetűk | begépelt szöveg, a képernyő-billentyűzet, leírások |

<a id="preview"></a>

## Előnézet

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## Karakterkészlet

Alap latin, Latin-1 és Kiterjesztett latin A/B: 337 kódpont minden változatban. Az ékezetes betűk egyelőre alapbetűjükként jelennek meg. A teljes lista: [docs/charset.md](docs/charset.md).

<a id="download"></a>

## Letöltés

A [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) oldalról, vagy közvetlenül ebből a tárolóból:

| Formátum | Fájlok |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): ugyanaz a három |

<a id="use"></a>

## Használat

**Egy RIPPS2-témában** a betűtípusok már benne vannak a `RIPPS2.elf` fájlban; csak nevezd meg őket, semmit nem kell mellékelni:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

A [RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) teljes egészében ezekkel van szedve. Az OPL-család bármely más témája a saját mappájából használhatja a TTF-eket, mint bármely betűtípust.

**A weben:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**PC-n:** telepítsd a TTF-eket a szokásos módon. A Regular és a Bold egy család, *RIPPS2 Sleek*; a Bold Case külön család, *RIPPS2 Sleek Case* (Bold), így sosem ütköznek.

<a id="build"></a>

## Összeállítás

Minden jel törött vonalak halmaza egy hat egység magas rácson (a nagybetű-magasság); mindegyik vonalat kap, és a vonalak egyetlen tiszta körvonallá olvadnak. A rajz a [tools/make_sleek_font.py](tools/make_sleek_font.py) fájlban van (ugyanabban, amelyből a RIPPS2 a saját másolatait készíti); a [tools/build.py](tools/build.py) ebből készít mindent, ami itt van, és megadja a betűtípusoknak azokat a neveket és vastagságokat, amelyeket az asztali programok és a böngészők olvasnak (a RIPPS2 csak a körvonalakat olvassa).

```
pip install -r requirements.txt
python tools/build.py
```

<a id="licence"></a>

## Licenc

- A betűtípusok: [SIL Open Font License 1.1](LICENSE-OFL). Használd, csomagold, módosítsd őket; a módosított betűtípus új nevet kap.
- Az eszközök: [MIT](LICENSE-MIT).

Nincs itt: a Planet N Compact, a RIPPS2 fő szövegbetűje, az [Iconian Fonts](https://www.iconian.com) tulajdona, és az is marad; a RIPPS2 One, egy egyjeles folt az egyesére, hozzá tartozik.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Letöltés</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Témák</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Betűtípusok</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Weboldal</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

