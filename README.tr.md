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
  <b>Türkçe</b> |
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

<p align="center"><sub>İngilizce README’nin çevirisi; farklılık olursa İngilizce geçerlidir. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">İndir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temalar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Yazı tipleri</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web sitesi</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

![RIPPS2 Sleek](docs/logo.png)

# RIPPS2 Sleek

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/tools-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/akilluminati47/RIPPS2-fonts?style=flat-square)](https://github.com/akilluminati47/RIPPS2-fonts/releases)
[![RIPPS2](https://img.shields.io/badge/made_for-RIPPS2-3c6ef0?style=flat-square)](https://github.com/akilluminati47/RIPPS2)

PS2 ön ucu [RIPPS2](https://github.com/akilluminati47/RIPPS2) için çizilen yazı tipi: menüleri, düğme ipuçları, ayarları, her listeyi adlandıran görünüm sözcüğü ve oraya ait görünmek isteyen her tema.

Harfler PS2 logosunun yazısını örnek alır: tek, ince, eşit bir çizgi, köşeli köşeler, bir ızgara üzerinde yatay ve dikey çubuklardan kurulan harfler ve logonun kendi açık biçimleri (karnının üstünde gövdesi olmayan P, zikzaklı 2). Dardırlar, bu yüzden tam bir düğme ipucu satırı 640 piksellik bir ekrana sığar.

| Kesim | Kalınlık | Harf | RIPPS2 içinde |
|---|---|---|---|
| **Regular** | ince çizgi | büyük harf (küçük harfler büyük çizilir) | ipuçları, menüler, ayarlar, kaynağın adı |
| **Bold** | kalın çizgi | büyük harf | büyük glifler yanında etiketler, görünüm sözcüğü, sürüm satırı |
| **Bold Case** | kalın çizgi | gerçek küçük harf | yazılan metin, ekran klavyesi, açıklamalar |

## Önizleme

### Regular

![Regular](docs/preview-regular.png)

### Bold

![Bold](docs/preview-bold.png)

### Bold Case

![Bold Case](docs/preview-boldcase.png)

## Karakter kümesi

Temel Latin, Latin-1 ve Genişletilmiş Latin A/B: her kesimde 337 kod noktası. Aksanlı harfler şimdilik temel harfleri olarak çizilir. Tam liste: [docs/charset.md](docs/charset.md).

## İndir

[Releases](https://github.com/akilluminati47/RIPPS2-fonts/releases) sayfasından ya da doğrudan bu depodan:

| Biçim | Dosyalar |
|---|---|
| TTF | [fonts/ttf](fonts/ttf): `RIPPS2Sleek-Regular.ttf`, `RIPPS2Sleek-Bold.ttf`, `RIPPS2Sleek-BoldCase.ttf` |
| WOFF2 (web) | [fonts/woff2](fonts/woff2): aynı üçü |

## Kullanım

**Bir RIPPS2 temasında** yazı tipleri zaten `RIPPS2.elf` içindedir; adlarını verin, hiçbir şey göndermeyin:

```
default_font=builtin:ripps2sleek       # Regular
font3=builtin:ripps2sleekbold          # Bold
font1=builtin:ripps2sleekcase          # Bold Case
```

[RIPgrid](https://github.com/akilluminati47/RIPPS2-themes) tamamen bunlarla dizilmiştir. OPL ailesinin başka her teması TTF dosyalarını herhangi bir yazı tipi gibi kendi klasöründen kullanabilir.

**Web’de:**

```css
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 400; src: url("RIPPS2Sleek-Regular.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek"; font-weight: 700; src: url("RIPPS2Sleek-Bold.woff2") format("woff2"); }
@font-face { font-family: "RIPPS2 Sleek Case"; font-weight: 700; src: url("RIPPS2Sleek-BoldCase.woff2") format("woff2"); }
```

**PC’de:** TTF dosyalarını her zamanki gibi kurun. Regular ve Bold tek bir ailedir, *RIPPS2 Sleek*; Bold Case ayrı bir ailedir, *RIPPS2 Sleek Case* (Bold), böylece ikisi asla çakışmaz.

## Derleme

Her glif, altı birim yüksekliğinde (büyük harf yüksekliği) bir ızgara üzerindeki kırık çizgilerden oluşur; her birine çizgi verilir ve çizgiler tek temiz bir dış hatta birleştirilir. Çizim [tools/make_sleek_font.py](tools/make_sleek_font.py) dosyasındadır (RIPPS2’nin kendi kopyalarını kurduğu aynı dosya); [tools/build.py](tools/build.py) buradaki her şeyi ondan yapar ve yazı tiplerine masaüstü programlarının ve tarayıcıların okuduğu adları ve kalınlıkları verir (RIPPS2 yalnızca dış hatları okur).

```
pip install -r requirements.txt
python tools/build.py
```

## Lisans

- Yazı tipleri: [SIL Open Font License 1.1](LICENSE-OFL). Kullanın, paketleyin, değiştirin; değiştirilen yazı tipi yeni bir ad alır.
- Araçlar: [MIT](LICENSE-MIT).

Burada yok: RIPPS2’nin ana metin yazısı Planet N Compact, [Iconian Fonts](https://www.iconian.com) firmasınındır ve onların kalır; 1 rakamı için tek glifli bir yama olan RIPPS2 One da onunla gider.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">İndir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temalar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPCSX2">RIPPCSX2</a> &nbsp;&middot;&nbsp; <b>Yazı tipleri</b> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web sitesi</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

