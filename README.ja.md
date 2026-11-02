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
  <a href="README.gl.md">Galego</a> |
  <a href="README.sq.md">Shqip</a> |
  <a href="README.tr.md">Türkçe</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fa.md">فارسی</a> |
  <b>日本語</b> |
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

<p align="center"><sub>英語の README の翻訳です。内容が異なる場合は英語版が正です。 <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">ダウンロード</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">テーマ</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>フォント</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">ウェブサイト</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

PS2 フロントエンド [RIPPS2](https://github.com/akilluminati47/RIPPS2) のために描いた書体です。メニュー、ボタンのヒント、設定、各リストを名づけるビュー語、そして RIPPS2 になじみたいすべてのテーマに使われます。

文字は PS2 ロゴのレタリングを手本にしています。細く均一な一本の線、角ばった角、グリッド上の水平・垂直の棒で組んだ文字、そしてロゴ自身の開いた形（ボウルの上に縦線のない P、ジグザグの 2）。幅が狭いので、ボタンのヒントを一列すべて 640 ピクセルの画面に収められます。

| カット | ウェイト | 大文字小文字 | RIPPS2 での用途 |
|---|---|---|---|
| **Regular** | 細い線 | 大文字（小文字も大文字で描画） | ヒント、メニュー、設定、ソース名 |
| **Bold** | 太い線 | 大文字 | 大きなグリフ横のラベル、ビュー語、リリース行 |
| **Bold Case** | 太い線 | 本物の小文字 | 入力テキスト、オンスクリーンキーボード、説明文 |

<a id="preview"></a>

## プレビュー

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## 文字セット

Basic Latin、Latin-1、Latin Extended-A/B：各カット 337 コードポイント。アクセント付きの文字は今のところ基本文字として描画されます。全一覧：[docs/charset.md](docs/charset.md)。

<a id="download"></a>

## ダウンロード

[Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) から、またはこのリポジトリから直接：

| 形式 | ファイル |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2（ウェブ） | [fonts/woff2](fonts/woff2)：同じ 3 つ |

<a id="use"></a>

## 使い方

**RIPPS2 のテーマでは**フォントはすでに `RIPPS2.elf` に入っています。名前を指定するだけで、何も同梱する必要はありません：

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) はすべてこの書体で組まれています。OPL 系のほかのテーマも、自分のフォルダーの TTF をほかのフォントと同じように使えます。

**ウェブでは：**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**PC では：** いつもどおり TTF をインストールします。Regular と Bold は一つのファミリー *RIPPS2 Sleek*、Bold Case は別のファミリー *RIPPS2 Sleek Case*（Bold）なので、ぶつかることはありません。

<a id="build"></a>

## ビルド

各グリフは高さ 6 ユニット（キャップハイト）のグリッド上の折れ線の集まりで、それぞれに線を引き、その線を一つのきれいなアウトラインに合成します。描画は [tools/make_sleek_font.py](tools/make_sleek_font.py)（RIPPS2 が自分のコピーを作るのと同じファイル）にあり、[tools/build.py](tools/build.py) がそこからここにあるすべてを作り、デスクトップアプリやブラウザが読む名前とウェイトをフォントに付けます（RIPPS2 自身はアウトラインだけを読みます）。

```
pip install -r requirements.txt
python tools/build.py
```

<a id="licence"></a>

## ライセンス

- フォント：[SIL Open Font License 1.1](LICENSE-OFL)。使っても、同梱しても、改変しても構いません。改変したフォントには新しい名前を付けます。
- ツール：[MIT](LICENSE-MIT)。

ここにないもの：RIPPS2 の主な本文書体 Planet N Compact は [Iconian Fonts](https://www.iconian.com) のもので、そのままです。その 1 を直す 1 グリフのパッチ RIPPS2 One もそれに付随します。

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">ダウンロード</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">テーマ</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>フォント</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">ウェブサイト</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

