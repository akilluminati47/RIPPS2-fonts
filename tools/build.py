"""Builds everything in this repo from tools/make_sleek_font.py (the drawing, as RIPPS2 uses it):

    fonts/ttf/RIPPS2Sleek-Regular.ttf, RIPPS2Sleek-Bold.ttf, RIPPS2Sleek-BoldCase.ttf
    fonts/woff2/  the same three for the web
    docs/         logo.png, a preview per weight, charset.md

    pip install fonttools shapely brotli pillow
    python tools/build.py
"""
import os
import sys
import unicodedata

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import make_sleek_font as sleek  # noqa: E402

CUTS = [  # (file stem, label, build arguments)
    ('RIPPS2Sleek-Regular', 'Regular', dict(bold=False)),
    ('RIPPS2Sleek-Bold', 'Bold', dict(bold=True)),
    ('RIPPS2Sleek-BoldCase', 'Bold Case', dict(bold=True, case=True)),
]
BG, INK, SOFT, BLUE = (5, 10, 28), (236, 242, 255), (150, 168, 210), (60, 110, 240)


def preview(ttf, label, out, case):
    W, H = 1600, 760 if case else 650
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    for y in range(H):  # RIPPS2's night: a blue haze toward the bottom
        t = y / H
        d.line([(0, y), (W, y)], fill=(5 + int(8 * t * t), 10 + int(22 * t * t), 28 + int(70 * t * t)))
    f = lambda s: ImageFont.truetype(ttf, s)
    d.text((70, 50), 'RIPPS2 SLEEK  ' + label.upper(), font=f(30), fill=BLUE)
    d.text((70, 110), 'KILL IT', font=f(150), fill=INK)
    d.text((70, 300), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', font=f(58), fill=INK)
    if case:
        d.text((70, 380), 'abcdefghijklmnopqrstuvwxyz', font=f(58), fill=INK)
    d.text((70, 460 if case else 380), '0123456789 !?&@#%()[]+-=/:;,.', font=f(58), fill=SOFT)
    d.text((70, 560 if case else 480),
           'Memory card in slot 1 is formatted.' if case else 'LAUNCH DISC   STORAGE   MEMORY FILES',
           font=f(46), fill=INK)
    d.text((70, 640 if case else 560),
           'The quick brown fox jumps over the lazy dog' if case else 'CROSS RUN    TRIANGLE OPTIONS    START MENU',
           font=f(40), fill=SOFT)
    im.save(out, optimize=True)


def logo(ttf, out):
    W, H = 1200, 360
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bg = Image.new('RGBA', (W, H))
    bd = ImageDraw.Draw(bg)
    for y in range(H):  # a dark banner, so it reads on GitHub's light and dark pages alike
        t = y / H
        bd.line([(0, y), (W, y)], fill=(5 + int(8 * t * t), 10 + int(22 * t * t), 28 + int(70 * t * t), 255))
    mask = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, W - 1, H - 1), radius=36, fill=255)
    im.paste(bg, (0, 0), mask)
    d = ImageDraw.Draw(im)
    big, small = ImageFont.truetype(ttf, 170), ImageFont.truetype(ttf, 46)
    tw = d.textlength('RIPPS2', font=big)
    d.text(((W - tw) / 2, 40), 'RIPPS2', font=big, fill=INK)
    sw = d.textlength('SLEEK', font=small)
    d.text(((W - sw) / 2, 250), 'SLEEK', font=small, fill=BLUE)
    im.save(out, optimize=True)


def charset(ttfs, out):
    t = TTFont(ttfs[0])
    cmap = t.getBestCmap()
    rows = ['# Character set', '',
            'Every cut maps the same %d code points. Accented letters draw as their base letter (the drawing has no'
            ' accents yet); in Regular and Bold the lowercase draws as the capitals, in Bold Case it is a true'
            ' lowercase.' % len(cmap), '',
            '| Block | Characters |', '|---|---|']
    blocks = {}
    for cp in sorted(cmap):
        name = 'Basic Latin' if cp < 0x80 else 'Latin-1' if cp < 0x100 else 'Latin Extended'
        blocks.setdefault(name, []).append(chr(cp))
    for name, chars in blocks.items():
        shown = ''.join(c if c not in '|\\`*_<>' else '\\' + c for c in chars if unicodedata.category(c)[0] != 'Z')
        rows.append('| %s (%d) | %s |' % (name, len(chars), shown))
    open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(rows) + '\n')


# How each cut presents itself to a computer: RIPPS2 reads only the outlines, but desktop apps and browsers
# go by these. Regular and Bold are one family (400 and 700); Bold Case is its own family, RIPPS2 Sleek Case,
# in Bold, so it never collides with Bold when installed.
NAMES = {
    'RIPPS2Sleek-Regular': ('RIPPS2 Sleek', 'Regular', 400),
    'RIPPS2Sleek-Bold': ('RIPPS2 Sleek', 'Bold', 700),
    'RIPPS2Sleek-BoldCase': ('RIPPS2 Sleek Case', 'Bold', 700),
}


def present(font, stem):
    family, style, weight = NAMES[stem]
    full = family + ' ' + style
    ps = family.replace(' ', '') + '-' + style
    version = font['name'].getDebugName(5) or 'Version 1.2'
    for nid, value in ((1, family), (2, style), (3, '%s;%s' % (ps, version.split()[-1])), (4, full), (6, ps)):
        font['name'].setName(value, nid, 3, 1, 0x409)
        font['name'].setName(value, nid, 1, 0, 0)
    os2, head = font['OS/2'], font['head']
    os2.usWeightClass = weight
    bold = style == 'Bold'
    os2.fsSelection = (os2.fsSelection & ~0x61) | (0x20 if bold else 0x40)  # BOLD or REGULAR, never both
    head.macStyle = (head.macStyle & ~1) | (1 if bold else 0)


def main():
    ttfs = []
    for stem, label, kw in CUTS:
        ttf = os.path.join(ROOT, 'fonts', 'ttf', stem + '.ttf')
        font = sleek.build('square', **kw)
        present(font, stem)
        font.save(ttf)
        ttfs.append(ttf)
        f = TTFont(ttf)
        f.flavor = 'woff2'
        f.save(os.path.join(ROOT, 'fonts', 'woff2', stem + '.woff2'))
        preview(ttf, label, os.path.join(ROOT, 'docs', 'preview-%s.png' % stem.split('-')[1].lower()), kw.get('case', False))
        print('built', stem)
    logo(ttfs[1], os.path.join(ROOT, 'docs', 'logo.png'))
    charset(ttfs, os.path.join(ROOT, 'docs', 'charset.md'))


if __name__ == '__main__':
    main()
