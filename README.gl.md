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
  <b>Galego</b> |
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

<p align="center"><sub>Tradución do README en inglés; se difiren, vale o inglés. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

O tipo de letra debuxado para [RIPPS2](https://github.com/akilluminati47/RIPPS2), o front end de PS2: os seus menús, as pistas de botóns, os axustes, a palabra de vista que nomea cada lista e cada tema que queira parecer da casa.

As letras toman como modelo o rótulo do logotipo de PS2: un trazo fino e uniforme, esquinas rectas, letras feitas de barras horizontais e verticais sobre unha grella, e as formas abertas do propio logotipo (o P sen hasta sobre a barriga, o 2 en zigzag). Son estreitas, así que unha fila enteira de pistas de botóns cabe nunha pantalla de 640 píxeles.

| Corte | Grosor | Caixa | En RIPPS2 |
|---|---|---|---|
| **Regular** | trazo fino | maiúsculas (as minúsculas debúxanse como maiúsculas) | pistas, menús, axustes, o nome da orixe |
| **Bold** | trazo groso | maiúsculas | etiquetas xunto a glifos grandes, a palabra de vista, a liña de versión |
| **Bold Case** | trazo groso | minúsculas de verdade | texto escrito, o teclado en pantalla, descricións |

## Vista previa

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Xogo de caracteres

Latín básico, Latin-1 e Latín estendido A/B: 337 puntos de código en cada corte. Polo de agora as letras con acento debúxanse como a súa letra base. A lista completa: [docs/charset.md](docs/charset.md).

## Descarga

Dende [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), ou directamente deste repositorio:

| Formato | Ficheiros |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): os mesmos tres |

## Uso

**Nun tema de RIPPS2** as fontes xa están dentro de `RIPPS2.elf`; nomeaas e non envíes nada:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) está composto enteiro con elas. Calquera outro tema da familia OPL pode usar os TTF dende o seu propio cartafol coma calquera fonte.

**Na web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Nun PC:** instala os TTF coma sempre. Regular e Bold son unha familia, *RIPPS2 Sleek*; Bold Case é unha familia á parte, *RIPPS2 Sleek Case* (Bold), así que nunca chocan.

## Compilación

Cada glifo é un conxunto de poliliñas sobre unha grella de seis unidades de alto (a altura das maiúsculas); cada unha trázase e os trazos únense nun único contorno limpo. O debuxo está en [tools/make_sleek_font.py](tools/make_sleek_font.py) (o mesmo ficheiro do que RIPPS2 constrúe as súas copias); [tools/build.py](tools/build.py) fai todo o de aquí a partir del e dá ás fontes os nomes e grosores que len as aplicacións de escritorio e os navegadores (RIPPS2 só le os contornos).

```
pip install -r requirements.txt
python tools/build.py
```

## Licenza

- As fontes: [SIL Open Font License 1.1](LICENSE-OFL). Úsaas, inclúeas, modifícaas; unha fonte modificada leva un nome novo.
- As ferramentas: [MIT](LICENSE-MIT).

Non está aquí: Planet N Compact, o tipo principal de texto de RIPPS2, é de [Iconian Fonts](https://www.iconian.com) e segue a ser seu; RIPPS2 One, un parche dun só glifo para o seu 1, vai con el.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

