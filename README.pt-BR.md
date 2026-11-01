<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <b>Português (Brasil)</b> |
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

<p align="center"><sub>Tradução do README em inglês; se diferirem, vale o inglês. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Baixar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

A fonte desenhada para o [RIPPS2](https://github.com/akilluminati47/RIPPS2), o front end de PS2: seus menus, dicas de botões, configurações, a palavra de exibição que nomeia cada lista e todo tema que queira parecer da casa.

As letras têm como modelo o letreiro do logotipo do PS2: um traço fino e uniforme, cantos retos, letras feitas de barras horizontais e verticais numa grade, e as formas abertas do próprio logotipo (o P sem haste acima do bojo, o 2 em zigue-zague). São estreitas, então uma fileira inteira de dicas de botões cabe numa tela de 640 pixels.

| Corte | Peso | Caixa | No RIPPS2 |
|---|---|---|---|
| **Regular** | traço fino | maiúsculas (minúsculas viram maiúsculas) | dicas, menus, configurações, o nome da fonte de jogos |
| **Bold** | traço grosso | maiúsculas | rótulos ao lado de glifos grandes, a palavra de exibição, a linha da versão |
| **Bold Case** | traço grosso | minúsculas de verdade | texto digitado, o teclado na tela, descrições |

## Prévia

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Conjunto de caracteres

Latim básico, Latin-1 e Latim Estendido-A/B: 337 pontos de código em cada corte. Por enquanto, letras acentuadas aparecem como a letra base. A lista completa: [docs/charset.md](docs/charset.md).

## Download

Pelos [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), ou direto deste repositório:

| Formato | Arquivos |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): os mesmos três |

## Uso

**Num tema do RIPPS2** as fontes já estão dentro do `RIPPS2.elf`; é só nomeá-las, sem enviar nada:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

O [RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) é todo composto com elas. Qualquer outro tema da família OPL pode usar os TTF da própria pasta como qualquer fonte.

**Na web:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**No PC:** instale os TTF como de costume. Regular e Bold são uma família, *RIPPS2 Sleek*; Bold Case é uma família própria, *RIPPS2 Sleek Case* (Bold), então as duas nunca se misturam.

## Compilação

Cada glifo é um conjunto de polilinhas numa grade de seis unidades de altura (a altura das maiúsculas); cada uma recebe um traço e os traços se unem num único contorno limpo. O desenho está em [tools/make_sleek_font.py](tools/make_sleek_font.py) (o mesmo arquivo de onde o RIPPS2 gera suas cópias); [tools/build.py](tools/build.py) gera tudo daqui a partir dele e dá às fontes os nomes e pesos que apps de desktop e navegadores leem (o RIPPS2 lê só os contornos).

```
pip install -r requirements.txt
python tools/build.py
```

## Licença

- As fontes: [SIL Open Font License 1.1](LICENSE-OFL). Use, distribua, modifique; uma fonte modificada ganha um nome novo.
- As ferramentas: [MIT](LICENSE-MIT).

Não está aqui: Planet N Compact, a fonte principal de texto do RIPPS2, é da [Iconian Fonts](https://www.iconian.com) e continua sendo dela; RIPPS2 One, um remendo de um glifo para o seu 1, vai junto com ela.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Baixar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Fontes</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

