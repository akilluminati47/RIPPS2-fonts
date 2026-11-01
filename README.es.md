<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <b>Español</b> |
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
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Traducción del README en inglés; si difieren, vale el inglés. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fuentes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

El tipo de letra dibujado para [RIPPS2](https://github.com/akilluminati47/RIPPS2), el front end de PS2: sus menús, las pistas de botones, los ajustes, la palabra de vista que nombra cada lista y cada tema que quiera parecer de la casa.

Las letras toman como modelo las del logotipo de PS2: un trazo fino y uniforme, esquinas rectas, letras hechas de barras horizontales y verticales sobre una cuadrícula, y las formas abiertas del propio logotipo (la P sin asta sobre su panza, el 2 en zigzag). Son estrechas, así que una fila entera de pistas de botones cabe en una pantalla de 640 píxeles.

| Corte | Grosor | Caja | En RIPPS2 |
|---|---|---|---|
| **Regular** | trazo fino | mayúsculas (las minúsculas se dibujan como mayúsculas) | pistas, menús, ajustes, el nombre de la fuente |
| **Bold** | trazo grueso | mayúsculas | etiquetas junto a glifos grandes, la palabra de vista, la línea de versión |
| **Bold Case** | trazo grueso | minúsculas de verdad | texto escrito, el teclado en pantalla, descripciones |

## Vista previa

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Juego de caracteres

Latín básico, Latin-1 y Latín Extendido-A/B: 337 puntos de código en cada corte. Por ahora las letras acentuadas se dibujan como su letra base. La lista completa: [docs/charset.md](docs/charset.md).

## Descarga

Desde [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), o directamente de este repositorio:

| Formato | Archivos |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): los mismos tres |

## Uso

**En un tema de RIPPS2** las fuentes ya están dentro de `RIPPS2.elf`; nómbralas y no envíes nada:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) está compuesto entero con ellas. Cualquier otro tema de la familia OPL puede usar los TTF desde su propia carpeta como cualquier fuente.

**En la web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**En un PC:** instala los TTF como siempre. Regular y Bold son una familia, *RIPPS2 Sleek*; Bold Case es una familia aparte, *RIPPS2 Sleek Case* (Bold), así que nunca chocan.

## Compilación

Cada glifo es un conjunto de polilíneas sobre una cuadrícula de seis unidades de alto (la altura de mayúsculas); cada una se traza y los trazos se unen en un único contorno limpio. El dibujo vive en [tools/make_sleek_font.py](tools/make_sleek_font.py) (el mismo archivo del que RIPPS2 construye sus copias); [tools/build.py](tools/build.py) hace todo lo de aquí a partir de él y da a las fuentes los nombres y grosores que leen las aplicaciones de escritorio y los navegadores (RIPPS2 solo lee los contornos).

```
pip install -r requirements.txt
python tools/build.py
```

## Licencia

- Las fuentes: [SIL Open Font License 1.1](LICENSE-OFL). Úsalas, inclúyelas, modifícalas; una fuente modificada lleva un nombre nuevo.
- Las herramientas: [MIT](LICENSE-MIT).

No está aquí: Planet N Compact, el tipo de texto principal de RIPPS2, es de [Iconian Fonts](https://www.iconian.com) y sigue siendo suyo; RIPPS2 One, un parche de un solo glifo para su 1, va con él.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fuentes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

