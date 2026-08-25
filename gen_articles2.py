# -*- coding: utf-8 -*-
"""Генератор второй партии блог-страниц."""
import pathlib

BASE = pathlib.Path(__file__).parent
SHELL = (BASE / "index.html").read_text(encoding="utf-8")

ARTICLE_CSS = """
<style>
.article{max-width:760px;margin:0 auto;padding:56px 24px}
.article h1{font-family:'Prata',serif;font-weight:400;font-size:clamp(28px,3.6vw,42px);line-height:1.2;margin-bottom:18px}
.article .meta{font-family:'Neucha',cursive;color:var(--accent);font-size:20px;margin-bottom:26px;transform:rotate(-.8deg);display:inline-block}
.article h2{font-family:'Prata',serif;font-weight:400;font-size:25px;margin:34px 0 12px}
.article p{margin-bottom:16px;color:#3d372e}
.article ul,.article ol{margin:0 0 16px 22px;color:#3d372e}
.article li{margin-bottom:8px}
.article table{width:100%;border-collapse:collapse;margin:14px 0 20px;font-size:15px}
.article th,.article td{border:1.5px solid var(--line);padding:8px 10px;text-align:left}
.article th{background:var(--paper-deep)}
.cta-box{background:var(--ink);color:var(--paper);border-radius:20px 20px 20px 5px;padding:30px;margin:36px 0;text-align:center}
.cta-box p{color:#b8ad99;margin-bottom:16px}
</style>
"""

CTA = (
    '<div class="cta-box"><h2>Попробуйте «Окошко» бесплатно</h2>'
    "<p>Настройка за минуту, первые 30 записей в месяц — без оплаты.</p>"
    '<a class="btn btn-accent" href="https://t.me/okoshko_zapisi_bot" rel="noopener">Открыть бота</a></div>'
)

ARTICLES = [
    dict(
        slug="skolko-stoit-onlain-zapis",
        title="Сколько стоит онлайн-запись для мастера в 2026: сравнение цен — Окошко",
        desc="Полная таблица цен сервисов онлайн-записи в России 2026: YClients, DIKIDI, Telegram-боты. Бесплатные тарифы, скрытые платежи и что выгоднее частному мастеру.",
        meta="обзор цен 2026",
        h1="Сколько стоит онлайн-запись<br>в 2026 году",
        body="""
<p>Собрали актуальные цены сервисов записи, которыми пользуются частные мастера в России. Цены проверены на официальных сайтах в августе 2026.</p>

<table>
<tr><th>Сервис</th><th>Бесплатно?</th><th>Платный тариф</th><th>Нюансы</th></tr>
<tr><td><b>Окошко</b> (Telegram)</td><td>до 30 записей/мес</td><td>300⭐ (~300₽)/мес или 100⭐/нед</td><td>оплата звёздами, карта не нужна</td></tr>
<tr><td>DIKIDI Basic</td><td>да</td><td>LITE от ~300₽/мес</td><td>веб-кабинет, не бот</td></tr>
<tr><td>YClients</td><td>нет</td><td>от 690₽/мес, лицензия от 3 мес</td><td>полный комбайн для салонов</td></tr>
<tr><td>Recordo (TG)</td><td>до 40 записей/мес</td><td>890₽/мес</td><td>оплата только картой</td></tr>
<tr><td>724bot (TG)</td><td>триал 7 дней</td><td>490₽/мес</td><td>без бесплатного тарифа</td></tr>
<tr><td>AETHEL (TG)</td><td>триал 7 дней</td><td>от 590₽/мес</td><td>нужно создавать своего бота</td></tr>
</table>

<h2>На что смотреть кроме цены</h2>
<ul>
<li><b>Где живут ваши клиенты.</b> Если в Telegram — нативный бот удобнее веб-кабинета: ни логинов, ни приложений.</li>
<li><b>Напоминания включены?</b> Экономия на no-show окупает подписку сама (по данным Авито — до +30% заказов).</li>
<li><b>Что нужно от вас.</b> Карта? ИП? Свой сервер? Чем меньше требований — тем быстрее старт.</li>
<li><b>Микротарифы.</b> Недельная подписка удобна для проверки сервиса без годовых обязательств.</li>
</ul>

<h2>Вывод</h2>
<p>Для соло-мастера разумный бюджет на запись — 0–300₽/мес. Всё, что дороже, оправдано только при сети салонов и сотрудниках. Начинайте с бесплатного тарифа, переходите на платный, когда запись начнёт приносить деньги.</p>
""",
        cta_text="Бесплатный тариф «Окошко» — без карты и срока.",
    ),
    dict(
        slug="bot-zapisi-svoimi-rukami",
        title="Бот записи своими руками или готовый сервис: что выбрать — Окошко",
        desc="Стоит ли писать телеграм-бот записи самостоятельно: время разработки, подводные камни (двойные записи, напоминания, часовые пояса) и когда готовый сервис выгоднее.",
        meta="для техничных мастеров",
        h1="Бот записи:<br>сделать самому или купить?",
        body="""
<p>Если вы умеете программировать, соберёте простой бот записи за вечер — туториалов полно. Но «работает у меня на столе» и «работает у клиентов» разделяют месяцы. Честный разбор обеих дорог.</p>

<h2>Что вы обязаны построить сами (если сами)</h2>
<ul>
<li>Генерация слотов из графика + длительности услуг;</li>
<li><b>Атомарную защиту от двойной записи</b> — два клиента жмут одновременно, кто-то должен получить отказ;</li>
<li>Напоминания за сутки и за 2 часа + обработку отмен;</li>
<li>Часовые пояса (клиент в другом регионе — и всё съехало);</li>
<li>Хостинг 24/7, бэкапы, мониторинг падений;</li>
<li>Поддержку: «у меня не записывается» придётся разбирать вам же.</li>
</ul>

<h2>Что вы получаете с готовым сервисом</h2>
<ul>
<li>Все пункты выше — уже решённые и обкатанные чужими ошибками;</li>
<li>Обновления и починку бесплатно;</li>
<li>Ваше время — на клиентов, а не на поддержку себя в роли хостера.</li>
</ul>

<h2>Арифметика</h2>
<p>Час работы мастера — от 1000₽. Свой бот отнимет минимум 40–60 часов на старте плюс несколько часов в месяц на обслуживание. Готовый PRO-тариф — около 300₽/мес. Считайте сами, что дешевле: ваше время стоит дороже кода.</p>

<h2>Когда свой бот оправдан</h2>
<p>Если это ваш пет-проект для обучения — конечно делайте, отличная практика. Для бизнеса берите готовое и не смешивайте роли «мастер» и «сисадмин самого себя».</p>
""",
        cta_text="Готовый вариант можно проверить бесплатно — без карты.",
    ),
]


def build(page):
    head_old = SHELL[SHELL.index("<title>") : SHELL.index("</head>")]
    head_new = (
        f"<title>{page['title']}</title>\n"
        f'<meta name="description" content="{page["desc"]}">\n'
        f'<meta property="og:title" content="{page["title"]}">\n'
        f'<link rel="stylesheet" href="/okoshko-site/styles.css">\n'
        f"{ARTICLE_CSS}\n"
    )
    html = SHELL.replace(head_old, head_new)
    start = html.index('<div class="wrap">')
    end = html.index("  <footer>")
    article = f"""
<div class="wrap">
  <article class="article">
    <a class="back" href="/okoshko-site/">← главная</a><br><br>
    <span class="meta">{page['meta']}</span>
    <h1>{page['h1']}</h1>
    {page['body']}
    {CTA}
  </article>

  <footer>
    <span>© 2026 Окошко · <a href="/okoshko-site/">главная</a></span>
    <span><a href="https://t.me/okoshko_zapisi_bot">Telegram-бот</a></span>
  </footer>
</div>
"""
    html = html[:start] + article.strip("\n") + "\n\n" + html[end:]
    out = BASE / "blog" / page["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    return page["slug"]


if __name__ == "__main__":
    for a in ARTICLES:
        print("built:", build(a))
