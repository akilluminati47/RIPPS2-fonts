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
  <b>Svenska</b> |
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

<p align="center"><sub>Översättning av den engelska README; vid skillnader gäller den engelska. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Ladda ner</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teman</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Typsnitt</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Webbplats</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Typsnittet ritat för [RIPPS2](https://github.com/akilluminati47/RIPPS2), PS2-frontenden: dess menyer, knapptips, inställningar, visningsordet som namnger varje lista och varje tema som vill se ut att höra till.

Bokstäverna har PS2-logotypens text som förebild: ett tunt, jämnt streck, fyrkantiga hörn, bokstäver byggda av vågräta och lodräta staplar på ett rutnät, och logotypens egna öppna former (P:et utan stam ovanför bågen, sicksack-tvåan). De är smala, så en hel rad knapptips får plats på en skärm på 640 pixlar.

| Snitt | Vikt | Skiftläge | I RIPPS2 |
|---|---|---|---|
| **Regular** | tunt streck | versaler (gemener ritas som versaler) | tips, menyer, inställningar, källans namn |
| **Bold** | kraftigt streck | versaler | etiketter bredvid stora glyfer, visningsordet, versionsraden |
| **Bold Case** | kraftigt streck | äkta gemener | inskriven text, skärmtangentbordet, beskrivningar |

<a id="preview"></a>

## Förhandsvisning

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## Teckenuppsättning

Grundläggande latin, Latin-1 och Utökad latin A/B: 337 kodpunkter i varje snitt. Bokstäver med accent ritas tills vidare som sin grundbokstav. Hela listan: [docs/charset.md](docs/charset.md).

<a id="download"></a>

## Ladda ner

Från [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), eller direkt från det här repot:

| Format | Filer |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (webb) | [fonts/woff2](fonts/woff2): samma tre |

<a id="use"></a>

## Användning

**I ett RIPPS2-tema** finns typsnitten redan i `RIPPS2.elf`; ange dem och skicka inget med:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) är helt satt i dem. Alla andra teman i OPL-familjen kan använda TTF-filerna från sin egen mapp som vilket typsnitt som helst.

**På webben:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**På en dator:** installera TTF-filerna som vanligt. Regular och Bold är en familj, *RIPPS2 Sleek*; Bold Case är en egen familj, *RIPPS2 Sleek Case* (Bold), så att de två aldrig krockar.

<a id="build"></a>

## Bygga

Varje glyf är en uppsättning polylinjer på ett rutnät sex enheter högt (versalhöjden); var och en får ett streck och strecken slås ihop till en enda ren kontur. Ritningen finns i [tools/make_sleek_font.py](tools/make_sleek_font.py) (samma fil som RIPPS2 bygger sina kopior från); [tools/build.py](tools/build.py) gör allt här utifrån den och ger typsnitten de namn och vikter som skrivbordsprogram och webbläsare läser (RIPPS2 läser bara konturerna).

```
pip install -r requirements.txt
python tools/build.py
```

<a id="licence"></a>

## Licens

- Typsnitten: [SIL Open Font License 1.1](LICENSE-OFL). Använd dem, packa med dem, ändra dem; ett ändrat typsnitt får ett nytt namn.
- Verktygen: [MIT](LICENSE-MIT).

Inte här: Planet N Compact, RIPPS2:s huvudsakliga textsnitt, tillhör [Iconian Fonts](https://www.iconian.com) och förblir deras; RIPPS2 One, en lapp på en glyf för dess 1:a, hör till det.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Ladda ner</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teman</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Typsnitt</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Webbplats</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

