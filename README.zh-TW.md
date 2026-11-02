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
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <b>繁體中文</b> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>英文 README 的譯本；如有出入，以英文為準。 <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下載</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主題</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>字型</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">網站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

為 PS2 前端 [RIPPS2](https://github.com/akilluminati47/RIPPS2) 繪製的字型：用於它的選單、按鍵提示、設定、為每個清單命名的檢視詞，以及每個想要融入其中的主題。

字母以 PS2 標誌的字樣為藍本：一根纖細均勻的筆畫、方正的轉角、在網格上由橫豎筆條搭成的字母，以及標誌本身的開放字形（碗形上方沒有豎幹的 P、鋸齒形的 2）。字形窄，所以一整行按鍵提示能放進 640 像素的螢幕。

| 字重款式 | 粗細 | 大小寫 | 在 RIPPS2 中 |
|---|---|---|---|
| **Regular** | 細筆畫 | 大寫（小寫也畫成大寫） | 提示、選單、設定、來源名稱 |
| **Bold** | 粗筆畫 | 大寫 | 大字形旁的標籤、檢視詞、版本行 |
| **Bold Case** | 粗筆畫 | 真正的小寫 | 輸入的文字、螢幕鍵盤、說明 |

<a id="preview"></a>

## 預覽

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

<a id="character-set"></a>

## 字元集

Basic Latin、Latin-1 和 Latin Extended-A/B：每款 337 個碼位。帶重音的字母目前畫作其基本字母。完整列表：[docs/charset.md](docs/charset.md)。

<a id="download"></a>

## 下載

從 [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) 下載，或直接從本儲存庫取得：

| 格式 | 檔案 |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2（網頁） | [fonts/woff2](fonts/woff2)：同樣三個 |

<a id="use"></a>

## 使用

**在 RIPPS2 主題中**，字型已經在 `RIPPS2.elf` 裡；寫上名字即可，什麼都不用附帶：

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) 完全用它們排版。OPL 系列的任何其他主題都可以像使用其他字型一樣，從自己的資料夾使用這些 TTF。

**在網頁上：**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**在電腦上：**照常安裝 TTF。Regular 和 Bold 屬於同一字族 *RIPPS2 Sleek*；Bold Case 是獨立字族 *RIPPS2 Sleek Case*（Bold），所以兩者不會衝突。

<a id="build"></a>

## 建置

每個字形都是高六個單位（大寫高度）的網格上的一組折線；每條折線描上筆畫，再把筆畫合併成一條乾淨的輪廓。繪製程式在 [tools/make_sleek_font.py](tools/make_sleek_font.py)（RIPPS2 產生自己副本的同一個檔案）；[tools/build.py](tools/build.py) 用它產生這裡的一切，並為字型寫入桌面程式和瀏覽器讀取的名稱與字重（RIPPS2 自己只讀取輪廓）。

```
pip install -r requirements.txt
python tools/build.py
```

<a id="licence"></a>

## 授權

- 字型：[SIL Open Font License 1.1](LICENSE-OFL)。可以使用、打包、修改；修改後的字型要換新名字。
- 工具：[MIT](LICENSE-MIT)。

不在這裡：RIPPS2 的主要內文字型 Planet N Compact 屬於 [Iconian Fonts](https://www.iconian.com)，仍歸他們所有；為其數字 1 打的單字形修補 RIPPS2 One 與它同屬。

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下載</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主題</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>字型</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">網站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

