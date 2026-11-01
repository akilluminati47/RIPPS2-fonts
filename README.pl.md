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
  <b>Polski</b> |
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

<p align="center"><sub>Tłumaczenie angielskiego README; w razie różnic obowiązuje wersja angielska. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Pobierz</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motywy</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Czcionki</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Strona</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Krój pisma narysowany dla [RIPPS2](https://github.com/akilluminati47/RIPPS2), front endu PS2: jego menu, podpowiedzi przycisków, ustawień, słowa widoku nazywającego każdą listę i każdego motywu, który chce wyglądać swojsko.

Litery biorą za wzór napis z logo PS2: jedna cienka, równa kreska, kwadratowe narożniki, litery zbudowane z poziomych i pionowych belek na siatce oraz otwarte kształty samego logo (P bez trzonu nad brzuszkiem, zygzakowata 2). Są wąskie, więc cały rząd podpowiedzi przycisków mieści się na ekranie o szerokości 640 pikseli.

| Odmiana | Grubość | Wielkość liter | W RIPPS2 |
|---|---|---|---|
| **Regular** | cienka kreska | wersaliki (małe litery rysowane jako wielkie) | podpowiedzi, menu, ustawienia, nazwa źródła |
| **Bold** | gruba kreska | wersaliki | etykiety przy dużych glifach, słowo widoku, linia wersji |
| **Bold Case** | gruba kreska | prawdziwe małe litery | wpisywany tekst, klawiatura ekranowa, opisy |

## Podgląd

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Zestaw znaków

Podstawowa łacina, Latin-1 i Łacina rozszerzona A/B: 337 punktów kodowych w każdej odmianie. Na razie litery z akcentami rysowane są jako ich litera bazowa. Pełna lista: [docs/charset.md](docs/charset.md).

## Pobieranie

Z [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) lub prosto z tego repozytorium:

| Format | Pliki |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): te same trzy |

## Użycie

**W motywie RIPPS2** czcionki są już w `RIPPS2.elf`; wystarczy je podać, niczego nie dołączając:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) jest w całości złożony nimi. Każdy inny motyw z rodziny OPL może używać plików TTF z własnego folderu jak każdej czcionki.

**W sieci:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Na PC:** zainstaluj pliki TTF jak zwykle. Regular i Bold to jedna rodzina, *RIPPS2 Sleek*; Bold Case to osobna rodzina, *RIPPS2 Sleek Case* (Bold), więc nigdy się nie zderzają.

## Budowanie

Każdy glif to zestaw linii łamanych na siatce wysokiej na sześć jednostek (wysokość wersalików); każda dostaje kreskę, a kreski są łączone w jeden czysty kontur. Rysunek jest w [tools/make_sleek_font.py](tools/make_sleek_font.py) (tym samym pliku, z którego RIPPS2 buduje swoje kopie); [tools/build.py](tools/build.py) robi z niego wszystko, co tu jest, i nadaje czcionkom nazwy i grubości czytane przez programy i przeglądarki (sam RIPPS2 czyta tylko kontury).

```
pip install -r requirements.txt
python tools/build.py
```

## Licencja

- Czcionki: [SIL Open Font License 1.1](LICENSE-OFL). Używaj ich, dołączaj, zmieniaj; zmieniona czcionka dostaje nową nazwę.
- Narzędzia: [MIT](LICENSE-MIT).

Nie ma tu: Planet N Compact, głównego kroju tekstu RIPPS2, który należy do [Iconian Fonts](https://www.iconian.com) i pozostaje ich; RIPPS2 One, jednoglifowa łatka do jego 1, idzie razem z nim.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Pobierz</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motywy</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Czcionki</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Strona</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

