# -*- coding: utf-8 -*-
"""Генерация og:image (1200x630) для обоих лендингов."""
import pathlib

from PIL import Image, ImageDraw, ImageFont

BASE = pathlib.Path(__file__).resolve().parent
FONTS = pathlib.Path(r"C:\Windows\Fonts")

SERIF = FONTS / "georgia.ttf"  # системная с кириллицей, близка к Prata по духу
SANS = FONTS / "segoeui.ttf"


def make(path, bg, accent, title_lines, sub, badge):
    img = Image.new("RGB", (1200, 630), bg)
    d = ImageDraw.Draw(img)
    # точечная текстура
    for x in range(0, 1200, 26):
        for y in range(0, 630, 26):
            d.ellipse([x, y, x + 2, y + 2], fill=tuple(min(c + 14, 255) for c in bg))

    # окошко-логотип
    d.rounded_rectangle([70, 80, 150, 160], radius=22, fill=accent)
    d.rounded_rectangle([86, 96, 134, 144], radius=12, fill=(255, 253, 248))
    f_logo = ImageFont.truetype(str(SANS), 34)
    d.text((170, 100), "ОКОШКО" if "Окошко" in badge else "N8N·RU", font=f_logo, fill=accent)

    f_title = ImageFont.truetype(str(SERIF), 72)
    y = 230
    for line in title_lines:
        d.text((70, y), line, font=f_title, fill=(38, 33, 26) if sum(bg) > 600 else (250, 245, 236))
        y += 92

    f_sub = ImageFont.truetype(str(SANS), 30)
    d.text((70, y + 16), sub, font=f_sub, fill=(107, 98, 84) if sum(bg) > 600 else (184, 173, 153))

    # бейдж
    f_badge = ImageFont.truetype(str(SANS), 28)
    bw = int(f_badge.getlength(badge)) + 56
    d.rounded_rectangle([70, 520, 70 + bw, 576], radius=999, fill=accent)
    d.text((98, 532), badge, font=f_badge, fill=(255, 255, 255))
    img.save(path, "PNG")
    print("saved", path)


make(
    BASE / "og-main.png",
    (250, 245, 236), (232, 89, 12),
    ["Запись клиентов —", "в одно окошко"],
    "Для частных мастеров. Напоминания сами. Карта не нужна.",
    "Бесплатно до 30 записей/мес",
)

p2 = pathlib.Path(r"D:\N8NStore\site")
p2.mkdir(exist_ok=True)
make(
    p2 / "og-store.png",
    (246, 244, 251), (112, 72, 232),
    ["Готовые n8n-", "шаблоны под RU"],
    "Селлерам, агентствам, фрилансерам. Импорт за 2 минуты.",
    "Оплата звёздами Telegram",
)
