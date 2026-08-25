# -*- coding: utf-8 -*-
import pathlib

p = pathlib.Path(__file__).resolve().parent / "index.html"
h = p.read_text(encoding="utf-8")

old = (
    '<span>© 2026 Окошко · запись клиентов для частных мастеров</span>\n'
    '    <span><a href="https://t.me/okoshko_zapisi_bot">Telegram-бот</a> · <a href="/">лендинг</a></span>'
)
new = (
    '<span>© 2026 Окошко · запись клиентов для частных мастеров</span>\n'
    '    <span>\n'
    '      <a href="https://t.me/okoshko_zapisi_bot">Telegram-бот</a> ·\n'
    '      <a href="/okoshko-site/blog/oplata-bez-karty/">запись без карты</a> ·\n'
    '      <a href="/okoshko-site/blog/yclients-dorogo/">YClients vs Окошко</a> ·\n'
    '      <a href="/okoshko-site/blog/klienty-ne-prichodjat/">против no-show</a>\n'
    '    </span>'
)

if old in h:
    h = h.replace(old, new, 1)
    p.write_text(h, encoding="utf-8")
    print("footer updated")
else:
    print("pattern not found — check manually")
