#!/usr/bin/env python3
"""Gera os arquivos de logo do site a partir dos originais em brand/.
Para trocar a logo: substitua os arquivos em brand/ e rode este script e depois build.py."""
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = (38, 53, 87)        # cor original da logo (#263557)
CREAM = (243, 239, 230)    # versão clara, para fundos escuros
GOLD = (196, 160, 104)


def bbox(im, thr=8):
    a = np.array(im)[..., 3]
    ys, xs = np.where(a > thr)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def tint(im, rgb):
    a = np.array(im)
    a[..., 0], a[..., 1], a[..., 2] = rgb
    return Image.fromarray(a, "RGBA")


def save(im, name, width=None, height=None):
    if width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    if height:
        im = im.resize((round(im.width * height / im.height), height), Image.LANCZOS)
    im.save(OUT / name, optimize=True)
    print(name, im.size)


icon = Image.open(ROOT / "brand" / "icone-original.webp").convert("RGBA")
icon = icon.crop(bbox(icon))
full = Image.open(ROOT / "brand" / "logo-completa-original.webp").convert("RGBA")
# faixa do nome (sem o ícone e sem "Advogado"), conforme medido na imagem original
name = full.crop((340, 905, 1665, 990))
name = name.crop(bbox(name))

for tag, rgb in (("navy", NAVY), ("light", CREAM)):
    save(tint(icon, rgb), f"logo-icone-{tag}.png", height=360)
    save(tint(name, rgb), f"logo-nome-{tag}.png", width=1000)

# favicon e ícones de app (ícone claro sobre azul-marinho)
BG = (13, 22, 38)
def tile(size, pad=0.16):
    t = Image.new("RGBA", (size, size), BG + (255,))
    ic = tint(icon, GOLD if False else CREAM)
    h = int(size * (1 - 2 * pad))
    w = round(ic.width * h / ic.height)
    if w > size * (1 - 2 * pad):
        w = int(size * (1 - 2 * pad)); h = round(ic.height * w / ic.width)
    ic = ic.resize((w, h), Image.LANCZOS)
    t.alpha_composite(ic, ((size - w) // 2, (size - h) // 2))
    return t
tile(64).save(OUT / "favicon.png"); tile(180).save(OUT / "apple-touch-icon.png")

# imagem de compartilhamento (WhatsApp, LinkedIn, Google)
og = Image.new("RGBA", (1200, 630), BG + (255,))
ic = tint(icon, CREAM); ic = ic.resize((round(ic.width * 300 / ic.height), 300), Image.LANCZOS)
nm = tint(name, CREAM); nm = nm.resize((760, round(nm.height * 760 / nm.width)), Image.LANCZOS)
og.alpha_composite(ic, ((1200 - ic.width) // 2, 90))
og.alpha_composite(nm, ((1200 - nm.width) // 2, 430))
og.convert("RGB").save(OUT / "og.png", optimize=True)
print("ok")
