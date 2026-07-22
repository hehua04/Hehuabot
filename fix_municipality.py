import pywikibot
from pywikibot import config

config.put_throttle = 5

site = pywikibot.Site()
category_ns = site.namespaces[14]

for city in ('北京', '天津', '上海', '重庆'):
    cat_title = f'{city}市邮政管理局的复函'
    cat_page = pywikibot.Page(site, cat_title, ns=category_ns)

    if not cat_page.exists():
        pywikibot.output(f'{cat_title} not found')
        continue

    text = cat_page.text
    old = '[[Category:地市级邮政管理部门的复函]]'
    new = '[[Category:省级邮政管理部门的复函]]'

    if old not in text:
        pywikibot.output(f'{cat_title} does not have 地市级 parent, skipping')
        continue

    text = text.replace(old, new)
    cat_page.text = text
    cat_page.save(summary='bot:修正直辖市复函分类父级（地市级→省级）')
