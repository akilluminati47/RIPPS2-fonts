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
  <b>Română</b> |
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

<p align="center"><sub>Traducerea README-ului în engleză; dacă diferă, este valabilă engleza. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descarcă</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fonturi</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Fontul desenat pentru [RIPPS2](https://github.com/akilluminati47/RIPPS2), front end-ul pentru PS2: meniurile sale, indiciile de butoane, setările, cuvântul de vizualizare care numește fiecare listă și fiecare temă care vrea să pară de-a casei.

Literele iau drept model inscripția logo-ului PS2: o singură linie subțire și uniformă, colțuri drepte, litere făcute din bare orizontale și verticale pe o grilă, și formele deschise ale logo-ului însuși (P fără tijă deasupra burții, 2 în zigzag). Sunt înguste, astfel încât un rând întreg de indicii de butoane încape pe un ecran de 640 de pixeli.

| Variantă | Grosime | Majuscule/minuscule | În RIPPS2 |
|---|---|---|---|
| **Regular** | linie subțire | majuscule (minusculele apar ca majuscule) | indicii, meniuri, setări, numele sursei |
| **Bold** | linie groasă | majuscule | etichete lângă glife mari, cuvântul de vizualizare, linia versiunii |
| **Bold Case** | linie groasă | minuscule adevărate | text tastat, tastatura de pe ecran, descrieri |

## Previzualizare

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Set de caractere

Latină de bază, Latin-1 și Latină extinsă A/B: 337 de puncte de cod în fiecare variantă. Deocamdată literele cu diacritice apar ca litera lor de bază. Lista completă: [docs/charset.md](docs/charset.md).

## Descărcare

De la [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), sau direct din acest depozit:

| Format | Fișiere |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): aceleași trei |

## Utilizare

**Într-o temă RIPPS2** fonturile sunt deja în `RIPPS2.elf`; numește-le și nu trimite nimic:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) este cules în întregime cu ele. Orice altă temă din familia OPL poate folosi fișierele TTF din propriul folder, ca pe orice font.

**Pe web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Pe PC:** instalează fișierele TTF ca de obicei. Regular și Bold sunt o singură familie, *RIPPS2 Sleek*; Bold Case este o familie separată, *RIPPS2 Sleek Case* (Bold), ca să nu se încurce niciodată.

## Construire

Fiecare glifă este un set de linii frânte pe o grilă înaltă de șase unități (înălțimea majusculelor); fiecare primește o linie, iar liniile sunt unite într-un singur contur curat. Desenul se află în [tools/make_sleek_font.py](tools/make_sleek_font.py) (același fișier din care RIPPS2 își construiește copiile); [tools/build.py](tools/build.py) face din el tot ce este aici și dă fonturilor numele și grosimile pe care le citesc aplicațiile și browserele (RIPPS2 citește doar contururile).

```
pip install -r requirements.txt
python tools/build.py
```

## Licență

- Fonturile: [SIL Open Font License 1.1](LICENSE-OFL). Folosește-le, include-le, modifică-le; un font modificat primește un nume nou.
- Instrumentele: [MIT](LICENSE-MIT).

Nu este aici: Planet N Compact, fontul principal de text al RIPPS2, aparține [Iconian Fonts](https://www.iconian.com) și rămâne al lor; RIPPS2 One, un petic de o glifă pentru cifra 1, merge cu el.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descarcă</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fonturi</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

