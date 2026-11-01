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
  <b>简体中文</b> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>英文 README 的译本；如有出入，以英文为准。 <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下载</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主题</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>字体</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">网站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

为 PS2 前端 [RIPPS2](https://github.com/akilluminati47/RIPPS2) 绘制的字体：用于它的菜单、按键提示、设置、为每个列表命名的视图词，以及每个想要融入其中的主题。

字母以 PS2 标志的字样为蓝本：一根纤细均匀的笔画、方正的转角、在网格上由横竖笔条搭成的字母，以及标志本身的开放字形（碗形上方没有竖干的 P、锯齿形的 2）。字形窄，所以一整行按键提示能放进 640 像素的屏幕。

| 字重款式 | 粗细 | 大小写 | 在 RIPPS2 中 |
|---|---|---|---|
| **Regular** | 细笔画 | 大写（小写也画成大写） | 提示、菜单、设置、来源名称 |
| **Bold** | 粗笔画 | 大写 | 大字形旁的标签、视图词、版本行 |
| **Bold Case** | 粗笔画 | 真正的小写 | 输入的文字、屏幕键盘、说明 |

## 预览

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## 字符集

Basic Latin、Latin-1 和 Latin Extended-A/B：每款 337 个码位。带重音的字母目前画作其基本字母。完整列表：[docs/charset.md](docs/charset.md)。

## 下载

从 [Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) 下载，或直接从本仓库获取：

| 格式 | 文件 |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2（网页） | [fonts/woff2](fonts/woff2)：同样三个 |

## 使用

**在 RIPPS2 主题中**，字体已经在 `RIPPS2.elf` 里；写上名字即可，什么都不用附带：

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) 完全用它们排版。OPL 系列的任何其他主题都可以像使用其他字体一样，从自己的文件夹使用这些 TTF。

**在网页上：**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**在电脑上：**照常安装 TTF。Regular 和 Bold 属于同一字族 *RIPPS2 Sleek*；Bold Case 是独立字族 *RIPPS2 Sleek Case*（Bold），所以两者不会冲突。

## 构建

每个字形都是高六个单位（大写高度）的网格上的一组折线；每条折线描上笔画，再把笔画合并成一条干净的轮廓。绘制代码在 [tools/make_sleek_font.py](tools/make_sleek_font.py)（RIPPS2 生成自己副本的同一个文件）；[tools/build.py](tools/build.py) 用它生成这里的一切，并为字体写入桌面程序和浏览器读取的名称与字重（RIPPS2 自己只读取轮廓）。

```
pip install -r requirements.txt
python tools/build.py
```

## 许可

- 字体：[SIL Open Font License 1.1](LICENSE-OFL)。可以使用、打包、修改；修改后的字体要换新名字。
- 工具：[MIT](LICENSE-MIT)。

不在这里：RIPPS2 的主要正文字体 Planet N Compact 属于 [Iconian Fonts](https://www.iconian.com)，仍归他们所有；为其数字 1 打的单字形补丁 RIPPS2 One 与它同属。

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下载</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主题</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>字体</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">网站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

