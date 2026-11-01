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
  <b>Русский</b> |
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

<p align="center"><sub>Перевод английского README; при расхождениях верен английский. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Скачать</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Темы</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Шрифты</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Сайт</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

Шрифт, нарисованный для [RIPPS2](https://github.com/akilluminati47/RIPPS2), фронтенда для PS2: его меню, подсказок кнопок, настроек, слова вида, которое называет каждый список, и любой темы, которая хочет выглядеть своей.

Буквы берут за образец надпись логотипа PS2: один тонкий ровный штрих, прямые углы, буквы из горизонтальных и вертикальных полос на сетке и открытые формы самого логотипа (P без ножки над чашей, двойка зигзагом). Они узкие, поэтому целый ряд подсказок кнопок помещается на экране шириной 640 пикселей.

| Начертание | Насыщенность | Регистр | В RIPPS2 |
|---|---|---|---|
| **Regular** | тонкий штрих | прописные (строчные рисуются как прописные) | подсказки, меню, настройки, имя источника |
| **Bold** | толстый штрих | прописные | подписи рядом с крупными глифами, слово вида, строка версии |
| **Bold Case** | толстый штрих | настоящие строчные | вводимый текст, экранная клавиатура, описания |

## Образцы

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Набор символов

Базовая латиница, Latin-1 и Расширенная латиница A/B: 337 кодовых точек в каждом начертании. Пока буквы с диакритикой рисуются как их базовая буква. Полный список: [docs/charset.md](docs/charset.md).

## Скачать

Со страницы [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) или прямо из этого репозитория:

| Формат | Файлы |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (веб) | [fonts/woff2](fonts/woff2): те же три |

## Использование

**В теме RIPPS2** шрифты уже есть внутри `RIPPS2.elf`; просто укажите их, ничего не прикладывая:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) целиком набран ими. Любая другая тема семейства OPL может использовать TTF из своей папки, как любой шрифт.

**В вебе:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**На ПК:** установите TTF как обычно. Regular и Bold составляют одно семейство, *RIPPS2 Sleek*; Bold Case — отдельное семейство, *RIPPS2 Sleek Case* (Bold), так что они никогда не конфликтуют.

## Сборка

Каждый глиф — набор ломаных на сетке высотой шесть единиц (высота прописных); каждая обводится штрихом, а штрихи объединяются в один чистый контур. Рисунок лежит в [tools/make_sleek_font.py](tools/make_sleek_font.py) (том же файле, из которого RIPPS2 собирает свои копии); [tools/build.py](tools/build.py) делает из него всё, что здесь есть, и даёт шрифтам имена и насыщенность, которые читают программы и браузеры (сам RIPPS2 читает только контуры).

```
pip install -r requirements.txt
python tools/build.py
```

## Лицензия

- Шрифты: [SIL Open Font License 1.1](LICENSE-OFL). Используйте, включайте в комплект, изменяйте; изменённый шрифт получает новое имя.
- Инструменты: [MIT](LICENSE-MIT).

Здесь нет: Planet N Compact, основной текстовый шрифт RIPPS2, принадлежит [Iconian Fonts](https://www.iconian.com) и остаётся их; RIPPS2 One, заплатка из одного глифа для его единицы, идёт вместе с ним.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Скачать</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Темы</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Шрифты</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Сайт</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

