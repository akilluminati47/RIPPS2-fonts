<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <b>Français</b> |
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

<p align="center"><sub>Traduction du README anglais ; en cas de différence, l’anglais fait foi. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Télécharger</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thèmes</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Polices</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

La police dessinée pour [RIPPS2](https://github.com/akilluminati47/RIPPS2), le front end PS2 : ses menus, les aides de boutons, les réglages, le mot de vue qui nomme chaque liste, et tout thème qui veut avoir l’air de la maison.

Les lettres prennent pour modèle le lettrage du logo PS2 : un trait fin et régulier, des angles droits, des lettres faites de barres horizontales et verticales sur une grille, et les formes ouvertes du logo lui-même (le P sans fût au-dessus de sa panse, le 2 en zigzag). Elles sont étroites, si bien qu’une rangée complète d’aides de boutons tient sur un écran de 640 pixels.

| Coupe | Graisse | Casse | Dans RIPPS2 |
|---|---|---|---|
| **Regular** | trait fin | capitales (les minuscules s’affichent en capitales) | aides, menus, réglages, le nom de la source |
| **Bold** | trait épais | capitales | libellés à côté des grands glyphes, le mot de vue, la ligne de version |
| **Bold Case** | trait épais | de vraies minuscules | texte saisi, le clavier à l’écran, les descriptions |

<a id="preview"></a>

## Aperçu

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## Jeu de caractères

Latin de base, Latin-1 et Latin étendu A/B : 337 points de code dans chaque coupe. Pour l’instant, les lettres accentuées s’affichent comme leur lettre de base. La liste complète : [docs/charset.md](docs/charset.md).

<a id="download"></a>

## Téléchargement

Depuis les [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases), ou directement depuis ce dépôt :

| Format | Fichiers |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2) : les trois mêmes |

<a id="use"></a>

## Utilisation

**Dans un thème RIPPS2**, les polices sont déjà dans `RIPPS2.elf` ; nommez-les, sans rien fournir :

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) est entièrement composé avec elles. Tout autre thème de la famille OPL peut utiliser les TTF depuis son propre dossier comme n’importe quelle police.

**Sur le web :**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**Sur PC :** installez les TTF comme d’habitude. Regular et Bold forment une famille, *RIPPS2 Sleek* ; Bold Case est une famille à part, *RIPPS2 Sleek Case* (Bold), pour qu’elles ne se gênent jamais.

<a id="build"></a>

## Construction

Chaque glyphe est un ensemble de polylignes sur une grille de six unités de haut (la hauteur des capitales) ; chacune est tracée et les traits sont fusionnés en un seul contour propre. Le dessin se trouve dans [tools/make_sleek_font.py](tools/make_sleek_font.py) (le même fichier à partir duquel RIPPS2 crée ses copies) ; [tools/build.py](tools/build.py) produit tout ce qui est ici à partir de lui et donne aux polices les noms et graisses que lisent les applications et les navigateurs (RIPPS2 ne lit que les contours).

```
pip install -r requirements.txt
python tools/build.py
```

## Licence

- Les polices : [SIL Open Font License 1.1](LICENSE-OFL). Utilisez-les, intégrez-les, modifiez-les ; une police modifiée prend un nouveau nom.
- Les outils : [MIT](LICENSE-MIT).

Pas ici : Planet N Compact, la police de texte principale de RIPPS2, appartient à [Iconian Fonts](https://www.iconian.com) et le reste ; RIPPS2 One, un correctif d’un seul glyphe pour son 1, va avec elle.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Télécharger</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thèmes</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Polices</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

