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
  <b>Čeština</b> |
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

<p align="center"><sub>Překlad anglického README; pokud se liší, platí angličtina. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Stáhnout</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motivy</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Písma</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Písmo nakreslené pro [RIPPS2](https://github.com/akilluminati47/RIPPS2), front end pro PS2: jeho nabídky, nápovědy tlačítek, nastavení, slovo pohledu, které pojmenovává každý seznam, a každý motiv, který chce vypadat jako domácí.

Písmena se řídí nápisem loga PS2: jeden tenký, rovnoměrný tah, hranaté rohy, písmena složená z vodorovných a svislých pruhů na mřížce a otevřené tvary samotného loga (P bez dříku nad bříškem, klikatá 2). Jsou úzká, takže celá řada nápověd tlačítek se vejde na obrazovku širokou 640 pixelů.

| Řez | Tloušťka | Velikost písmen | V RIPPS2 |
|---|---|---|---|
| **Regular** | tenký tah | verzálky (malá písmena se kreslí jako velká) | nápovědy, nabídky, nastavení, název zdroje |
| **Bold** | silný tah | verzálky | popisky u velkých glyfů, slovo pohledu, řádek verze |
| **Bold Case** | silný tah | skutečná malá písmena | psaný text, klávesnice na obrazovce, popisy |

## Ukázka

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Znaková sada

Základní latinka, Latin-1 a Rozšířená latinka A/B: 337 kódových bodů v každém řezu. Písmena s diakritikou se zatím kreslí jako jejich základní písmeno. Celý seznam: [docs/charset.md](docs/charset.md).

## Stažení

Z [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), nebo přímo z tohoto repozitáře:

| Formát | Soubory |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): tytéž tři |

## Použití

**V motivu RIPPS2** jsou písma už uvnitř `RIPPS2.elf`; stačí je uvést, nic nepřikládejte:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) je jimi celý vysázený. Jakýkoli jiný motiv z rodiny OPL může použít soubory TTF ze své vlastní složky jako každé písmo.

**Na webu:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Na PC:** nainstalujte soubory TTF jako obvykle. Regular a Bold jsou jedna rodina, *RIPPS2 Sleek*; Bold Case je samostatná rodina, *RIPPS2 Sleek Case* (Bold), takže se nikdy nepletou.

## Sestavení

Každý glyf je sada lomených čar na mřížce vysoké šest jednotek (výška verzálek); každá dostane tah a tahy se sloučí do jednoho čistého obrysu. Kresba je v [tools/make_sleek_font.py](tools/make_sleek_font.py) (ve stejném souboru, ze kterého RIPPS2 sestavuje své kopie); [tools/build.py](tools/build.py) z ní vytvoří vše, co je zde, a dá písmům názvy a tloušťky, které čtou desktopové aplikace a prohlížeče (RIPPS2 čte jen obrysy).

```
pip install -r requirements.txt
python tools/build.py
```

## Licence

- Písma: [SIL Open Font License 1.1](LICENSE-OFL). Používejte je, přikládejte je, upravujte je; upravené písmo dostane nový název.
- Nástroje: [MIT](LICENSE-MIT).

Není zde: Planet N Compact, hlavní textové písmo RIPPS2, patří [Iconian Fonts](https://www.iconian.com) a zůstává jejich; RIPPS2 One, jednoglyfová záplata pro jeho jedničku, patří k němu.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Stáhnout</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motivy</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Písma</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

