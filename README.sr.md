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
  <b>Srpski</b> |
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

<p align="center"><sub>Prevod engleskog README-a; ako se razlikuju, važi engleski. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontovi</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sajt</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Pismo nacrtano za [RIPPS2](https://github.com/akilluminati47/RIPPS2), front end za PS2: njegove menije, savete za dugmad, podešavanja, reč prikaza koja imenuje svaku listu i svaku temu koja želi da izgleda kao da pripada.

Slova uzimaju natpis loga PS2 za uzor: jedan tanak, ujednačen potez, četvrtasti uglovi, slova sastavljena od vodoravnih i uspravnih prečki na mreži, i otvoreni oblici samog loga (P bez stabla iznad trbuha, cik-cak 2). Uska su, pa ceo red saveta za dugmad stane na ekran širok 640 piksela.

| Rez | Debljina | Veličina slova | U RIPPS2 |
|---|---|---|---|
| **Regular** | tanak potez | velika slova (mala se crtaju kao velika) | saveti, meniji, podešavanja, ime izvora |
| **Bold** | debeo potez | velika slova | oznake pored velikih glifova, reč prikaza, red verzije |
| **Bold Case** | debeo potez | prava mala slova | ukucani tekst, tastatura na ekranu, opisi |

## Pregled

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Skup znakova

Osnovna latinica, Latin-1 i Proširena latinica A/B: 337 kodnih tačaka u svakom rezu. Slova sa akcentima se zasad crtaju kao osnovno slovo. Cela lista: [docs/charset.md](docs/charset.md).

## Preuzimanje

Sa [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), ili direktno iz ovog repozitorijuma:

| Format | Datoteke |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (veb) | [fonts/woff2](fonts/woff2): ista tri |

## Upotreba

**U RIPPS2 temi** fontovi su već u `RIPPS2.elf`; samo ih navedite, ništa ne prilažite:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) je ceo složen u njima. Svaka druga tema iz OPL porodice može da koristi TTF datoteke iz svoje fascikle kao svaki font.

**Na vebu:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Na računaru:** instalirajte TTF datoteke kao i obično. Regular i Bold su jedna porodica, *RIPPS2 Sleek*; Bold Case je zasebna porodica, *RIPPS2 Sleek Case* (Bold), pa se dve nikad ne sudaraju.

## Izrada

Svaki glif je skup izlomljenih linija na mreži visokoj šest jedinica (visina velikih slova); svaka dobija potez, a potezi se spajaju u jedan čist obris. Crtež je u [tools/make_sleek_font.py](tools/make_sleek_font.py) (istoj datoteci iz koje RIPPS2 pravi svoje kopije); [tools/build.py](tools/build.py) iz nje pravi sve ovde i daje fontovima imena i debljine koje čitaju desktop programi i pregledači (sam RIPPS2 čita samo obrise).

```
pip install -r requirements.txt
python tools/build.py
```

## Licenca

- Fontovi: [SIL Open Font License 1.1](LICENSE-OFL). Koristite ih, prilažite, menjajte; promenjen font dobija novo ime.
- Alati: [MIT](LICENSE-MIT).

Nije ovde: Planet N Compact, glavno tekstualno pismo RIPPS2, pripada [Iconian Fonts](https://www.iconian.com) i ostaje njihovo; RIPPS2 One, zakrpa od jednog glifa za njegovu jedinicu, ide uz njega.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontovi</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sajt</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

