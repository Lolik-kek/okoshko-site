# -*- coding: utf-8 -*-
import pathlib

p = pathlib.Path(__file__).resolve().parent / "index.html"
h = p.read_text(encoding="utf-8")

i = h.index("<footer>")
end = h.index("</footer>")
footer_old = h[i : end + len("</footer>")]

links = (
    '<span><a href="https://t.me/okoshko_zapisi_bot">Telegram-бот</a></span>\n'
    '    <span>\n'
    '      <a href="/okoshko-site/blog/oplata-bez-karty/">запись без карты</a> ·\n'
    '      <a href="/okoshko-site/blog/yclients-dorogo/">YClients vs Окошко</a> ·\n'
    '      <a href="/okoshko-site/blog/klienty-ne-prichodjat/">против no-show</a>\n'
    '    </span>'
)
# внутри footer есть свой <span>©...</span>; заменяем только второй span со ссылками
start_span = h.index("<span>", i + len("<span>© 2026"))
end_span = h.index("</span>", start_span) + len("</span>")
h = h[:start_span] + links + h[end_span:]

p.write_text(h, encoding="utf-8")
print("footer updated, new len:", len(h))
